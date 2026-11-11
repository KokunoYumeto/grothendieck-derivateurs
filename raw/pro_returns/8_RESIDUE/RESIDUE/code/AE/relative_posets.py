#!/usr/bin/env python3
"""All relative posets up to four objects, up to isomorphism.
Complete finite fixed-alternating-type computation through length six.
Output is NOT asserted to compute the unbounded full path category.
"""
from itertools import product, permutations, combinations
from pathlib import Path
import json,csv

def canon(n,R,W=None):
    vals=[]
    for p in permutations(range(n)):
        r=''.join('1' if (p[i],p[j]) in R else '0' for i in range(n) for j in range(n))
        if W is not None:r+=':'+''.join('1' if (p[i],p[j]) in W else '0' for i in range(n) for j in range(n))
        vals.append(r)
    return min(vals)

def posets(n):
    pairs=list(combinations(range(n),2));seen=set()
    for mask in range(1<<len(pairs)):
        R={(i,i) for i in range(n)}|{p for k,p in enumerate(pairs) if mask>>k&1}
        if any((i,k) not in R for i,j in R for j2,k in R if j==j2):continue
        key=canon(n,R)
        if key in seen:continue
        seen.add(key);yield R

def markings(n,R):
    edges=sorted(R-{(i,i) for i in range(n)});seen=set()
    for bits in range(1<<len(edges)):
        W={(i,i) for i in range(n)}|{p for k,p in enumerate(edges) if bits>>k&1}
        if any(sum([((i,j) in W),((j,k) in W),((i,k) in W)])==2 for i,j in R for j2,k in R if j==j2):continue
        key=canon(n,R,W)
        if key in seen:continue
        seen.add(key);yield W

def fixed_paths(n,R,W,L,a,b):
    out=[]
    def go(p):
        k=len(p)-1
        if k==L:
            if p[-1]==b:out.append(tuple(p))
            return
        for x in range(n):
            if ((x,p[-1]) in W if k%2==0 else (p[-1],x) in R):go(p+[x])
    go([a]);return out

def beat_core(P,R):
    N=len(P);lower=[0]*N;upper=[0]*N
    for i in range(N):
        for j in range(i):
            if all((x,y) in R for x,y in zip(P[i],P[j])):
                upper[i]|=1<<j;lower[j]|=1<<i
            if all((y,x) in R for x,y in zip(P[i],P[j])):
                upper[j]|=1<<i;lower[i]|=1<<j
    active=(1<<N)-1;cert=[]
    changed=True
    while changed:
        changed=False
        indices=active
        while indices:
            one=indices&-indices;i=one.bit_length()-1;indices-=one
            lo=lower[i]&active;up=upper[i]&active
            target=None
            test=lo
            while test:
                bit=test&-test;j=bit.bit_length()-1;test-=bit
                if lo&~(lower[j]|bit)==0:target=(j,'down');break
            if target is None:
                test=up
                while test:
                    bit=test&-test;j=bit.bit_length()-1;test-=bit
                    if up&~(upper[j]|bit)==0:target=(j,'up');break
            if target is not None:
                active^=one;cert.append([i,*target]);changed=True
    unseen=active;comps=[]
    while unseen:
        bit=unseen&-unseen;unseen-=bit;st=[bit.bit_length()-1];comp=[]
        while st:
            i=st.pop();comp.append(i);nei=(lower[i]|upper[i])&unseen;unseen&=~nei
            while nei:
                bit=nei&-nei;nei-=bit;st.append(bit.bit_length()-1)
        comps.append(comp)
    return {'objects':N,'nonidentity_arrows':sum(x.bit_count() for x in upper),
     'component_count':len(comps),'core_component_sizes':[len(c) for c in comps],
     'all_components_contractible_certified':all(len(c)==1 for c in comps),
     'core_paths':[[P[i] for i in c] for c in comps], 'beat_certificate':cert}

def main():
    output=Path(__file__).parent;types=[];rows=[];proofs=[]
    for n in range(0,5):
        ps=list(posets(n));print('posets',n,len(ps),flush=True)
        for pi,R in enumerate(ps):
            for wi,W in enumerate(markings(n,R)):
                ident=f'P{n}_{pi:02d}_W{wi:02d}'
                types.append({'id':ident,'objects':n,'order':sorted(R),'marking':sorted(W),'canonical':canon(n,R,W)})
                for L in [2,4,6]:
                    for a in range(n):
                        for b in range(n):
                            P=fixed_paths(n,R,W,L,a,b);r=beat_core(P,R)
                            rows.append({'id':ident,'poset_objects':n,'path_objects':r['objects'],'type_length':L,'a':a,'b':b,
                             **{k:v for k,v in r.items() if k not in ('objects','core_paths','beat_certificate')}})
                            proofs.append({'id':ident,'L':L,'a':a,'b':b,'core_paths':r['core_paths'],'beat_certificate':r['beat_certificate']})
        print('completed',n,'relative types',len(types),'endpoint rows',len(rows),flush=True)
    (output/'relative_posets_catalogue.json').write_text(json.dumps(types,indent=2))
    (output/'relative_posets_certificates.json').write_text(json.dumps(proofs,separators=(',',':')))
    with (output/'relative_posets_table.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    summary={'relative_types':len(types),'endpoint_rows':len(rows),
      'rows_with_nondiscrete_core':sum(not r['all_components_contractible_certified'] for r in rows),
      'maximum_path_objects':max(r['path_objects'] for r in rows)}
    (output/'relative_posets_summary.json').write_text(json.dumps(summary,indent=2));print(summary)
if __name__=='__main__':main()
