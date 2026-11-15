#!/usr/bin/env python3
"""Exhaustive independent finite-poset direct-image stalk audit.

For each isomorphism class of P,Q with <=5 objects, enumerate ALL monotone
maps between the chosen representatives. Classify properness by explicit
simplicial collapse of every outgoing lifting poset. Noncontractibility is
certified by Q or F2 homology; a case lacking either certificate aborts.

For every proper map and every target simplex support, compute both stalks
for the constant coefficient and indicator of every principal cosieve.
The categorical stalk uses the order complex of P_{<=q0} intersect cosieve.
The geometric stalk uses the actual product-of-simplices cells of the fibre,
with the signed CELLULAR boundary. No minimum-functor initiality test or
prior BISITE program is used. All field ranks are exact.
"""
from itertools import combinations, permutations, product
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
from math import gcd
import argparse, csv, json, time

OUT=Path(__file__).resolve().parent

def bitrel(n,mask):
    pairs=list(combinations(range(n),2)); rel={(i,i) for i in range(n)}
    rel|={p for k,p in enumerate(pairs) if mask>>k&1}
    if any((i,k) not in rel for i,j in rel for jj,k in rel if j==jj):return None
    return tuple(sum(1<<j for ii,j in rel if ii==i) for i in range(n))

def canonical(rel):
    n=len(rel)
    return min(tuple(sum(((rel[p[i]]>>p[j])&1)<<j for j in range(n))
                       for i in range(n)) for p in permutations(range(n)))

def posets(n):
    seen={}
    for mask in range(1<<(n*(n-1)//2)):
        r=bitrel(n,mask)
        if r is not None: seen.setdefault(canonical(r),r)
    return tuple(seen[k] for k in sorted(seen))

@lru_cache(None)
def chains(rel,subset):
    vals=[i for i in range(len(rel)) if subset>>i&1]
    return tuple(s for k in range(1,len(vals)+1) for s in combinations(vals,k)
                 if all(rel[a]>>b&1 for a,b in zip(s,s[1:])))

def rank_Q(A):
    if not A:return 0
    a=[list(map(int,r)) for r in A]; nr=len(a);nc=len(a[0]); row=0
    for col in range(nc):
        pivot=next((j for j in range(row,nr) if a[j][col]),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]; piv=a[row][col]
        for j in range(row+1,nr):
            v=a[j][col]
            if not v:continue
            d=gcd(abs(piv),abs(v));aa=piv//d;bb=v//d
            a[j]=[aa*x-bb*y for x,y in zip(a[j],a[row])]
            d=0
            for x in a[j][col+1:]:d=gcd(d,abs(x))
            if d>1:a[j]=[x//d for x in a[j]]
        row+=1
        if row==nr:break
    return row

def rank_F2(A):
    piv={}
    for r in A:
        x=sum((v&1)<<j for j,v in enumerate(r))
        while x:
            j=x.bit_length()-1
            if j in piv:x^=piv[j]
            else:piv[j]=x;break
    return len(piv)

def homology(cell_by_dim,boundary):
    dims=[len(c) for c in cell_by_dim]; ranks=[(0,0)]; previous=None
    for d in range(1,len(dims)):
        idx={c:i for i,c in enumerate(cell_by_dim[d-1])}
        a=[[0]*dims[d] for _ in range(dims[d-1])]
        for j,c in enumerate(cell_by_dim[d]):
            for face,sign in boundary(c):
                a[idx[face]][j]+=sign
        if previous is not None:
            for row in previous:
                support=[(i,v) for i,v in enumerate(row) if v]
                for col in range(dims[d]):
                    assert sum(v*a[i][col] for i,v in support)==0, 'boundary squared nonzero'
        ranks.append((rank_Q(a),rank_F2(a)))
        previous=a
    ranks.append((0,0))
    out=tuple(tuple(dims[d]-ranks[d][f]-ranks[d+1][f]
                    for d in range(len(dims))) for f in (0,1))
    return tuple(tuple(list(x)+[0]*(5-len(x))) for x in out)

@lru_cache(None)
def order_homology(rel,subset):
    ss=chains(rel,subset)
    by=tuple(tuple(s for s in ss if len(s)==d+1) for d in range(5))
    return homology(by,lambda s:((s[:i]+s[i+1:],(-1)**i) for i in range(len(s))))

@lru_cache(None)
def collapsible(rel,subset):
    ss=set(chains(rel,subset))
    if not ss:return False
    while len(ss)>1:
        found=False
        # Delete a free codimension-one face and its unique maximal coface.
        for tau in sorted(ss,key=lambda x:(-len(x),x)):
            if len(tau)<=1 or any(set(tau)<set(z) for z in ss):continue
            for i in range(len(tau)):
                sig=tau[:i]+tau[i+1:]
                co=[z for z in ss if set(sig)<set(z)]
                if co==[tau] or (len(co)==1 and co[0]==tau):
                    ss.remove(sig);ss.remove(tau);found=True;break
            if found:break
        if not found:return False
    return len(next(iter(ss)))==1

@lru_cache(None)
def contractibility(rel,subset):
    if collapsible(rel,subset):return True
    h=order_homology(rel,subset)
    if h!=((1,0,0,0,0),(1,0,0,0,0)):return False
    raise RuntimeError(('uncertified acyclic lifting poset',rel,subset,h))

@lru_cache(None)
def fibre_homology(rel,levels,subset):
    # levels=-1 excludes an object; otherwise levels range through 0,...,r-1.
    r=max(levels,default=-1)+1
    if r==0:return ((0,)*5,(0,)*5)
    allowed=subset&sum(1<<i for i,v in enumerate(levels) if v>=0)
    cells=tuple(s for s in chains(rel,allowed)
                if set(levels[i] for i in s)==set(range(r)))
    by=tuple(tuple(s for s in cells if len(s)-r==d) for d in range(5))
    def boundary(s):
        counts=[sum(levels[i]==l for i in s) for l in range(r)]
        local=[0]*r
        for j,i in enumerate(s):
            l=levels[i]
            if counts[l]>1:
                sign=(-1)**(sum(c-1 for c in counts[:l])+local[l])
                yield s[:j]+s[j+1:],sign
            local[l]+=1
    return homology(by,boundary)

def proper(P,Q,f):
    for p in range(len(P)):
        for q in range(len(Q)):
            if Q[f[p]]>>q&1:
                ss=sum(1<<r for r in range(len(P)) if P[p]>>r&1 and f[r]==q)
                if not contractibility(P,ss):return False
    return True

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max',type=int,default=5);args=ap.parse_args()
    start=time.time(); cats={n:posets(n) for n in range(args.max+1)}
    assert [len(cats[n]) for n in cats]==[1,1,2,5,16,63][:args.max+1]
    stats=[]; failures=[]; total={'monotone_maps':0,'proper_maps':0,'stalk_coefficient_tests':0}
    with (OUT/f'poset_direct_image_maps_max{args.max}.csv').open('w',newline='') as out:
        cols=['source_size','source_index','target_size','target_index','map','stalk_coefficient_tests','all_Q_equal','all_F2_equal']
        writer=csv.DictWriter(out,fieldnames=cols);writer.writeheader()
        for np,ps in cats.items():
            for nq,qs in cats.items():
                stat={'source_size':np,'target_size':nq,'monotone_maps':0,'proper_maps':0,'tests':0}
                for ip,P in enumerate(ps):
                    pairs=[(a,b) for a in range(np) for b in range(a+1,np) if P[a]>>b&1]
                    for iq,Q in enumerate(qs):
                        for f in product(range(nq),repeat=np):
                            if not all(Q[f[a]]>>f[b]&1 for a,b in pairs):continue
                            stat['monotone_maps']+=1
                            if not proper(P,Q,f):continue
                            stat['proper_maps']+=1;tests=0;equal_Q=True;equal_F2=True
                            coefficients=[(1<<np)-1]+[P[p] for p in range(np)]
                            for sig in chains(Q,(1<<nq)-1):
                                levels=tuple(sig.index(v) if v in sig else -1 for v in f)
                                base=sum(1<<p for p in range(np) if Q[f[p]]>>sig[0]&1)
                                for support in coefficients:
                                    left=order_homology(P,base&support)
                                    right=fibre_homology(P,levels,support)
                                    tests+=1
                                    equal_Q=equal_Q and left[0]==right[0]
                                    equal_F2=equal_F2 and left[1]==right[1]
                                    if left!=right:
                                        failures.append({'P':P,'Q':Q,'f':f,'sigma':sig,'coefficient_support':support,'categorical':left,'geometric':right})
                            stat['tests']+=tests
                            writer.writerow(dict(zip(cols,[np,ip,nq,iq,''.join(map(str,f)),tests,equal_Q,equal_F2])))
                stats.append(stat);out.flush()
                total['monotone_maps']+=stat['monotone_maps'];total['proper_maps']+=stat['proper_maps'];total['stalk_coefficient_tests']+=stat['tests']
                print(json.dumps(stat),flush=True)
    summary={'max_objects':args.max,'poset_isomorphism_classes':{n:len(v) for n,v in cats.items()},
       'enumeration':'all maps between representatives; no quotient by map isomorphisms',
       'totals':total,'failures':failures,'by_sizes':stats,
       'seconds':round(time.time()-start,3),
       'cache_sizes':{'orders':order_homology.cache_info().currsize,'fibres':fibre_homology.cache_info().currsize}}
    (OUT/f'poset_direct_image_summary_max{args.max}.json').write_text(json.dumps(summary,indent=2)+'\n')
    (OUT/f'poset_representatives_max{args.max}.json').write_text(json.dumps(cats,indent=2)+'\n')
    print(json.dumps({'totals':total,'failures':len(failures),'seconds':summary['seconds']}),flush=True)
    assert not failures

if __name__=='__main__':main()
