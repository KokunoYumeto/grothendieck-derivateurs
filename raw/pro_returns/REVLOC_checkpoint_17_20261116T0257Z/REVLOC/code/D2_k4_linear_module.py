#!/usr/bin/env python3
"""Exact necessary Steenrod-module test for the fourth-suspension linear branch.

Tests arbitrary degree-minus-three linear maps on reduced H*(K(F2,2)),
commuting with all squares in the indicated finite range. Fixes only
u^3 to v; every other coefficient remains free. No multiplicativity, map realization, or
nullification conclusion is assumed. Adem and Cartan are implemented directly.
"""
from functools import lru_cache
from math import comb
from pathlib import Path
import argparse, json

DEG=(2,3,5,9,17,33,65)
NAME=('u','v','w','t','s','r','z')
ZERO=(0,)*len(DEG)

def parity(items):
    out=set()
    for x in items:
        if x in out: out.remove(x)
        else: out.add(x)
    return frozenset(out)

@lru_cache(None)
def adem(word):
    word=tuple(x for x in word if x)
    for i in range(len(word)-1):
        a,b=word[i:i+2]
        if a<2*b:
            terms=[]
            for j in range(a//2+1):
                top=b-j-1; bot=a-2*j
                if 0<=bot<=top and comb(top,bot)%2:
                    nw=word[:i]+(a+b-j,)+( (j,) if j else () )+word[i+2:]
                    terms.extend(adem(nw))
            return parity(terms)
    return frozenset((word,))

@lru_cache(None)
def admissible_value(word):
    if not word: return (1,)+(0,)*(len(DEG)-1)
    excess=word[0]-sum(word[1:])
    if excess>2: return None
    if excess==2:
        val=admissible_value(word[1:])
        return tuple(2*x for x in val) if val is not None else None
    expected=tuple(2**i for i in reversed(range(len(word))))
    assert word==expected, (word,excess)
    return tuple(int(i==len(word)) for i in range(len(DEG)))

@lru_cache(None)
def gen_sq(i,k):
    if k<0 or k>DEG[i]: return frozenset()
    word=(k,)+tuple(2**j for j in reversed(range(i)))
    return parity(val for w in adem(word)
                  if (val:=admissible_value(w)) is not None)

@lru_cache(None)
def sq(m,k):
    if k==0:return frozenset((m,))
    if k<0 or k>sum(a*b for a,b in zip(m,DEG)) or m==ZERO:
        return frozenset()
    i=next(i for i,a in enumerate(m) if a)
    rest=list(m);rest[i]-=1;rest=tuple(rest)
    return parity(tuple(a+b for a,b in zip(x,y))
                  for j in range(min(k,DEG[i])+1)
                  for x in gen_sq(i,j) for y in sq(rest,k-j))

@lru_cache(None)
def basis(n,i=0):
    if n<0:return ()
    if i==len(DEG):return ((),) if n==0 else ()
    return tuple((j,)+rest for j in range(n//DEG[i]+1)
                 for rest in basis(n-j*DEG[i],i+1))

def fmt(m):
    return '*'.join(n if a==1 else f'{n}^{a}'
                    for n,a in zip(NAME,m) if a) or '1'

def validate(n):
    # Every admissible-basis identity and every Adem relation is checked
    # on every polynomial monomial for which total degree is at most n.
    checks=0
    for d in range(2,n+1):
        for m in basis(d):
            assert sq(m,0)==frozenset((m,))
            if 2*d<=n: assert sq(m,d)==frozenset((tuple(2*x for x in m),))
            for a in range(1,n-d+1):
                for b in range(1,n-d-a+1):
                    if a>=2*b:continue
                    lhs=parity(y for x in sq(m,b) for y in sq(x,a))
                    rhs=parity(y for j in range(a//2+1)
                               if 0<=a-2*j<=b-j-1 and comb(b-j-1,a-2*j)%2
                               for x in sq(m,j) for y in sq(x,a+b-j))
                    assert lhs==rhs,(fmt(m),a,b,lhs,rhs)
                    checks+=1
    return checks

def run(n,trace=False):
    variables=[(d,m,t) for d in range(5,n+1)
               for m in basis(d) for t in basis(d-3)]
    vid={v:i for i,v in enumerate(variables)}
    piv={}; rows=[]; constraints=0; contradiction=None
    def add(cols,rhs,description):
        nonlocal constraints,contradiction
        constraints+=1
        if trace:rows.append(description)
        v=0
        for c in cols:v^=1<<c
        ancestry=(1<<(constraints-1)) if trace else 0
        while v:
            p=v.bit_length()-1
            if p in piv:
                pv,pr,pa=piv[p];v^=pv;rhs^=pr;ancestry^=pa
            else:
                piv[p]=(v,rhs,ancestry);return True
        if rhs:
            contradiction=[rows[i] for i in range(len(rows)) if (ancestry>>i)&1] if trace else True
            return False
        return True
    m=next(m for m in basis(6) if fmt(m)=='u^3')
    t=next(t for t in basis(3) if fmt(t)=='v')
    add([vid[(6,m,t)]],1,{'fixed':['u^3','v',1]})
    for outdeg in range(5,n+1):
        if contradiction:break
        outbasis=basis(outdeg-3)
        for d in range(2,outdeg):
            if contradiction:break
            k=outdeg-d
            for m in basis(d):
                image=sq(m,k)
                for t in outbasis:
                    cols=[vid[(outdeg,x,t)] for x in image]
                    if d>=5:
                        cols.extend(vid[(d,m,z)] for z in basis(d-3) if t in sq(z,k))
                    if not add(cols,0,{'square':k,'input':fmt(m),'output_coefficient':fmt(t)}):break
                if contradiction:break
    result={'max_degree':n,'variables':len(variables),'constraints_processed':constraints,
            'rank':len(piv),'consistent':not bool(contradiction),
            'scope':__doc__.strip()}
    if contradiction:result['contradiction']=contradiction
    else:
        # Deterministic solution: free variables zero, then increasing pivots.
        solution=0
        for p,(v,rhs,_) in sorted(piv.items()):
            val=rhs^((v&solution).bit_count()%2)
            if val:solution|=1<<p
        assert all(((v&solution).bit_count()%2)==rhs for v,rhs,_ in piv.values())
        result['one_solution']=[{'degree':d,'input':fmt(m),'output':fmt(t)}
                               for i,(d,m,t) in enumerate(variables) if (solution>>i)&1]
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max',type=int,default=24)
    parser.add_argument('--trace',action='store_true');parser.add_argument('--validate',type=int,default=18)
    args=parser.parse_args()
    checks=validate(args.validate)
    ans=run(args.max,args.trace);ans['Adem_checks']=checks
    path=Path(__file__).parent/'outputs'/f'D2_k4_linear_module_{args.max}.json'
    path.write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps({k:v for k,v in ans.items() if k not in ('one_solution','contradiction')},indent=2))
    if ans.get('contradiction'):print(json.dumps(ans['contradiction'],indent=2))
    print(path)
