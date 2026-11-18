#!/usr/bin/env python3
"""Primary Sq4/Sq2 obstruction quotient in H_*(Q Sigma K(F2,2)).

Uses the free polynomial Dyer--Lashof basis through degree12. No
iterated Dyer--Lashof generator occurs below15. Computes the exact
subspace Sq4_*(ker Sq2_*) for degrees3..8. This is a necessary
primary-operation test, not a realization or nullification theorem.
"""
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json
import D2_fiber_poly_check as b

MAX = 12
b.GEN_SQ[3][1] = {(0, 0, 2, 0)}
def monomials(n):
    return [ex for ex in product(range(n//2+1), range(n//3+1),
                                range(n//5+1), range(n//9+1))
            if sum(v*d for v,d in zip(ex,(2,3,5,9))) == n]

gens = {}
for d in range(3, MAX+1):
    for ex in monomials(d-1):
        name = 's(' + '*'.join(f'{g}^{k}' for g,k in zip('uvwt',ex) if k) + ')'
        gens[name] = {'degree':d, 'ex':ex}
units = {info['ex']: name for name,info in gens.items()}
for name,info in list(gens.items()):
    d=info['degree']
    for s in range(d+1, MAX-d+1):
        gens[f'Q{s}[{name}]']={'degree':d+s, 'q':s, 'unit':name}
names=sorted(gens, key=lambda g:(gens[g]['degree'],g))

@lru_cache(None)
def basis(n,start=0):
    if n == 0:return ((),)
    out=[]
    for i in range(start,len(names)):
        g=names[i];d=gens[g]['degree']
        if d>n:break
        for tail in basis(n-d,i):out.append(tuple(sorted((g,)+tail)))
    return tuple(sorted(set(out)))

def xor(*items):
    out=set()
    for x in items:out.symmetric_difference_update(x)
    return out
def mul(p,q):
    out=set()
    for x,y in product(p,q):
        z=tuple(sorted(x+y))
        if z in out:out.remove(z)
        else:out.add(z)
    return out

@lru_cache(None)
def sqgen(r,g):
    if r==0:return frozenset({(g,)})
    info=gens[g];d=info['degree']
    if 'ex' in info:
        target=d-1-r
        if target<2:return frozenset()
        return frozenset((units[ex],) for ex in monomials(target)
                         if info['ex'] in b.csq(r,ex))
    s=info['q'];x=info['unit'];out=set()
    for t in range(r//2+1):
        n,k=s-r,r-2*t
        if n<0 or k<0 or k>n or comb(n,k)%2==0:continue
        for term in sqgen(t,x):
            assert len(term)==1
            y=term[0];dy=gens[y]['degree'];qy=s-r+t
            if qy<dy:continue
            z=(y,y) if qy==dy else (f'Q{qy}[{y}]',)
            assert all(j in gens for j in z),(r,g,z)
            out=xor(out,{tuple(sorted(z))})
    return frozenset(out)

@lru_cache(None)
def sq(r,m):
    if not m:return frozenset({()}) if r==0 else frozenset()
    if len(m)==1:return sqgen(r,m[0])
    return frozenset(xor(*(mul(sqgen(i,m[0]),sq(r-i,m[1:]))
                           for i in range(r+1))))

def encode(p,ba):
    pos={x:i for i,x in enumerate(ba)}
    return sum(1<<pos[x] for x in p)
def decode(v,ba):return [list(m) for i,m in enumerate(ba) if (v>>i)&1]
def span_basis(vectors):
    piv={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return list(piv.values())

rows=[]
for n in range(3,9):
    source=basis(n+4);mid=basis(n+2);target=basis(n)
    piv={};images=[]
    for m in source:
        v=encode(sq(2,m),mid);w=encode(sq(4,m),target)
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i][0];w^=piv[i][1]
            else:piv[i]=(v,w);break
        if v==0:images.append(w)
    wb=span_basis(images)
    annih=[x for x in range(1<<len(target))
           if all((x&w).bit_count()%2==0 for w in wb)]
    ab=span_basis(annih)
    rows.append({'degree':n,'source_dimension':len(source),
                 'target_basis':[list(x) for x in target],
                 'image_rank':len(wb),'image_basis':[decode(x,target) for x in wb],
                 'annihilator_basis':[decode(x,target) for x in ab]})

# Independent universal relations on the computed range.
for n in range(3,MAX+1):
    for m in basis(n):
        assert not xor(*(sq(1,x) for x in sq(1,m))),('Sq1Sq1',m)
        left=xor(*(sq(2,x) for x in sq(2,m)))
        right=xor(*(sq(1,x) for x in sq(3,m)))
        assert left==right,('homology dual Adem Sq2Sq2=Sq3Sq1',m,left,right)

dest=Path(__file__).parent/'outputs'/'D2_Qsource_primary.json'
result={'status':'PASS','scope':__doc__.strip(),'generators':gens,'rows':rows}
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','rows':rows,'output':str(dest)},indent=2))
