#!/usr/bin/env python3
"""Independent bounded presheaf search. Exact presentations and Smith forms.

Bounds: labelled monoids of order <=4, nonempty right acts of size <=3;
skeletal one-way categories with <=7 arrows (identities included),
presheaves with each value <=2 and total cardinality <=4.
No anti-isomorphism identification is used: variance is preserved.
"""
from itertools import product, combinations_with_replacement
from pathlib import Path
import json, time
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT=Path(__file__).resolve().parent/'outputs'; OUT.mkdir(exist_ok=True)
LOG=[]
def say(s): print(s,flush=True); LOG.append(s)
def inv(w): return tuple(-x for x in reversed(w))
def reduce_word(w):
    s=[]
    for x in w:
        if s and s[-1]==-x: s.pop()
        else: s.append(x)
    while len(s)>1 and s[0]==-s[-1]: s=s[1:-1]
    return tuple(s)
def canon(w):
    w=reduce_word(w)
    if not w:return ()
    v=inv(w)
    return min([w[i:]+w[:i] for i in range(len(w))]+[v[i:]+v[:i] for i in range(len(v))])
def simplify(gens,rels):
    rels=set(canon(r) for r in rels); rels.discard(())
    gens=set(gens); steps=[]
    while True:
        choice=None
        for r in sorted(rels,key=lambda w:(len(w),w)):
            for i,x in enumerate(r):
                if sum(abs(y)==abs(x) for y in r)==1:
                    choice=(r,i,x);break
            if choice:break
        if not choice:break
        r,i,x=choice; rest=r[i+1:]+r[:i]
        sub=inv(rest) if x>0 else rest
        g=abs(x);steps.append([g,list(sub)]);gens.remove(g)
        new=set()
        for w in rels:
            if w==r:continue
            ww=[]
            for y in w:
                ww.extend(sub if y==g else inv(sub) if y==-g else (y,))
            z=canon(ww)
            if z:new.add(z)
        rels=new
    return sorted(gens),sorted(rels),steps

def presentation(nobj,arrows,comp,ids):
    parent=list(range(nobj))
    def root(x):
        while parent[x]!=x: parent[x]=parent[parent[x]];x=parent[x]
        return x
    tree=set()
    for i,(s,t) in enumerate(arrows):
        x,y=root(s),root(t)
        if x!=y:parent[x]=y;tree.add(i)
    if len({root(x) for x in range(nobj)})!=1:return None
    numbered={a:i+1 for i,a in enumerate(j for j in range(len(arrows)) if j not in tree and j not in ids)}
    rels=[]
    for (g,f),h in comp.items():
        rels.append(tuple(z for z in (numbered.get(g,0),numbered.get(f,0),-numbered.get(h,0)) if z))
    gens,rels,steps=simplify(numbered.values(),rels)
    if not gens:return {'perfect':True,'trivial':True,'eliminations':len(steps)}
    pos={g:i for i,g in enumerate(gens)}
    mat=sp.zeros(len(rels),len(gens))
    for i,r in enumerate(rels):
        for g in r:mat[i,pos[abs(g)]]+=1 if g>0 else -1
    s=smith_normal_form(mat,domain=ZZ)
    factors=[abs(int(s[i,i])) for i in range(min(s.shape)) if s[i,i]]
    perfect=len(factors)==len(gens) and all(x==1 for x in factors)
    return {'perfect':perfect,'trivial':False,'generators':gens,'relations':[list(w) for w in rels],
            'H1_free_rank':len(gens)-len(factors),'H1_torsion':[x for x in factors if x>1]}

def elem_category(k,s,t,table,hvals,act):
    objects=[(u,h) for u in range(k) for h in range(hvals[u])]; oi={x:i for i,x in enumerate(objects)}
    arrows=[]; lookup={}
    for a in range(len(s)):
        for h in range(hvals[t[a]]):
            lookup[a,h]=len(arrows);arrows.append((oi[s[a],act[a][h]],oi[t[a],h]))
    comp={}
    for g in range(len(s)):
        for f in range(len(s)):
            if t[f]!=s[g]:continue
            for h in range(hvals[t[g]]):
                comp[lookup[g,h],lookup[f,act[g][h]]]=lookup[table[g][f],h]
    ids={lookup[u,h] for u in range(k) for h in range(hvals[u])}
    return len(objects),arrows,comp,ids

def monoids(n):
    T=[[0]*n for _ in range(n)]
    for a in range(n): T[0][a]=T[a][0]=a
    cells=[(g,f) for g in range(1,n) for f in range(1,n)]
    for values in product(range(n),repeat=len(cells)):
        for (g,f),v in zip(cells,values):T[g][f]=v
        if all(T[h][T[g][f]]==T[T[h][g]][f] for h,g,f in product(range(1,n),repeat=3)):
            yield [r[:] for r in T]

def partitions(n):
    def rec(a):
        if len(a)==n:yield tuple(a);return
        for x in range(max(a,default=-1)+2):yield from rec(a+[x])
    yield from rec([])
def left_quotients(T):
    n=len(T)
    return [p for p in partitions(n) if all(p[T[g][a]]==p[T[g][b]] for g,a,b in product(range(n),repeat=3) if p[a]==p[b])]

def search_monoids():
    rows=[]; survivors=[]
    for n in range(1,5):
        row={'order':n,'labelled_monoids':0,'right_acts':0,'connected_acts':0,'H1_zero':0,
             'trivial_pi1_certified':0,'quotients_of_left_regular':0}
        for T in monoids(n):
            row['labelled_monoids']+=1;row['quotients_of_left_regular']+=len(left_quotients(T))
            for q in range(1,4):
                funcs=list(product(range(q),repeat=q));fi={f:i for i,f in enumerate(funcs)}
                ft=[[fi[tuple(f[g[x]] for x in range(q))] for g in funcs] for f in funcs]
                ident=fi[tuple(range(q))]
                for rr in product(range(len(funcs)),repeat=n-1):
                    aidx=(ident,)+rr
                    if any(aidx[T[g][f]]!=ft[aidx[f]][aidx[g]] for g in range(1,n) for f in range(1,n)):continue
                    row['right_acts']+=1
                    act=[funcs[i] for i in aidx]
                    ec=elem_category(1,[0]*n,[0]*n,T,[q],act)
                    pp=presentation(*ec)
                    if pp is None:continue
                    row['connected_acts']+=1
                    if pp['perfect']:
                        row['H1_zero']+=1
                        if pp['trivial']:row['trivial_pi1_certified']+=1
                        else:survivors.append({'kind':'monoid','table':T,'H':q,'action':act,'presentation':pp})
        rows.append(row);say('MONOID '+json.dumps(row))
    return rows,survivors

def one_way_categories():
    # Object order is fixed. Every finite acyclic category admits such an order.
    for k in range(1,8):
        pairs=[(i,j) for i in range(k) for j in range(i+1,k)]
        for narr in range(k,8):
            for extras in combinations_with_replacement(pairs,narr-k):
                s=list(range(k))+[x[0] for x in extras];t=list(range(k))+[x[1] for x in extras]
                T=[[-1]*narr for _ in range(narr)]
                for f in range(narr):T[f][s[f]]=T[t[f]][f]=f
                cells=[(g,f) for g in range(k,narr) for f in range(k,narr) if t[f]==s[g]]
                opts=[[h for h in range(k,narr) if s[h]==s[f] and t[h]==t[g]] for g,f in cells]
                for vals in product(*opts):
                    for (g,f),v in zip(cells,vals):T[g][f]=v
                    if all(T[h][T[g][f]]==T[T[h][g]][f] for h,g,f in product(range(k,narr),repeat=3) if t[f]==s[g] and t[g]==s[h]):
                        yield k,s,t,[r[:] for r in T]

def search_one_way():
    rows={n:{'arrows':n,'ordered_labelled_categories':0,'presheaves':0,'connected_acts':0,
             'H1_zero':0,'trivial_pi1_certified':0} for n in range(1,8)};survivors=[]
    for k,s,t,T in one_way_categories():
        n=len(s);row=rows[n];row['ordered_labelled_categories']+=1
        for hv in product(range(3),repeat=k):
            if not 1<=sum(hv)<=4:continue
            choices=[list(product(range(hv[s[a]]),repeat=hv[t[a]])) for a in range(k,n)]
            for selected in product(*choices):
                act=[tuple(range(hv[u])) for u in range(k)]+list(selected)
                if any(act[T[g][f]]!=tuple(act[f][act[g][h]] for h in range(hv[t[g]])) for g in range(k,n) for f in range(k,n) if t[f]==s[g]):continue
                row['presheaves']+=1
                ec=elem_category(k,s,t,T,hv,act);pp=presentation(*ec)
                if pp is None:continue
                row['connected_acts']+=1
                if pp['perfect']:
                    row['H1_zero']+=1
                    if pp['trivial']:row['trivial_pi1_certified']+=1
                    else:survivors.append({'kind':'one_way','k':k,'s':s,'t':t,'table':T,'H':hv,'action':act,'presentation':pp})
    for row in rows.values():say('ONE_WAY '+json.dumps(row))
    return list(rows.values()),survivors

def main():
    t0=time.monotonic();mr,ms=search_monoids();cr,cs=search_one_way();ss=ms+cs
    result={'monoids':mr,'one_way_categories':cr,'perfect_pi1_survivors':ss,
            'method':'Every connected element category with H1=0 was subjected to exact, reversible Tietze eliminations; empty presentation certifies trivial pi1. Thus no acyclic nontrivial-pi1 example is excluded by finite homology truncation.',
            'runtime_seconds':round(time.monotonic()-t0,3)}
    say(f'SURVIVORS with H1=0 and not certified pi1=1: {len(ss)}')
    say('Elapsed seconds: '+str(result['runtime_seconds']))
    (OUT/'bounded_search.json').write_text(json.dumps(result,indent=2))
    (OUT/'bounded_search.out').write_text('\n'.join(LOG)+'\n')
if __name__=='__main__':main()
