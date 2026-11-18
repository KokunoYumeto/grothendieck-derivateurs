#!/usr/bin/env python3
"""One-Browder-bracket fiber sector through degree eleven.

Uses the Serre coalgebra, the divided-power Pontryagin product on
K(F2,2), and Browder/Steenrod Cartan. Does not enumerate the entire
E2 homology, prove realization of a map, or compute homotopy groups.
"""
from pathlib import Path
from itertools import product,combinations
from functools import lru_cache
from math import comb
import json
import sys
root=Path(__file__).parent
sys.path.insert(0,str(root))
import D2_fiber_poly_check as b
b.GEN_SQ[3][1]={(0,0,2,0)}
zero=(0,0,0,0)
def deg(e):return sum(x*y for x,y in zip(e,(2,3,5,9)))
exs=sorted([e for e in product(range(6),range(4),range(3),range(2)) if 2<=deg(e)<=11],key=lambda e:(deg(e),e))
labels={e:b.LABEL.get(e,'['+','.join(map(str,e))+']') for e in exs}
rev={v:k for k,v in labels.items()}
names=sorted(rev,key=lambda x:(deg(rev[x]),x))

def xor(*ss):
 o=set()
 for s in ss:o.symmetric_difference_update(s)
 return o

def bm(e,f):
 g=tuple(a+c for a,c in zip(e,f))
 return g if all(comb(a+c,a)%2 for a,c in zip(e,f)) else None

@lru_cache(None)
def splits(name):
 e=rev[name]
 return tuple((left,tuple(a-c for a,c in zip(e,left))) for left in product(*(range(a+1) for a in e)))

def bracket(x,y):
 return None if x==y else tuple(sorted((x,y)))

def md(m):
 pair,ls=m
 return deg(rev[pair[0]])+deg(rev[pair[1]])+1+sum(deg(rev[x]) for x in ls)

@lru_cache(None)
def polys(n,start=0):
 if n==0:return ((),)
 out=[]
 for i in range(start,len(names)):
  x=names[i];d=deg(rev[x])
  if d>n:break
  for tail in polys(n-d,i):out.append(tuple(sorted((x,)+tail)))
 return tuple(out)

@lru_cache(None)
def basis(n):
 out=[]
 for x,y in combinations(names,2):
  d=deg(rev[x])+deg(rev[y])+1
  if d<=n:
   out.extend((bracket(x,y),ls) for ls in polys(n-d))
 return tuple(sorted(out))

@lru_cache(None)
def sq_label(k,x):
 if k==0:return (x,)
 return tuple(labels[e] for e in exs if deg(e)==deg(rev[x])-k and rev[x] in b.csq(k,e))

@lru_cache(None)
def sq(k,m):
 pair,ls=m
 if not ls:
  out=set()
  for i in range(k+1):
   for x in sq_label(i,pair[0]):
    for y in sq_label(k-i,pair[1]):
     z=bracket(x,y)
     if z is not None:out.symmetric_difference_update({(z,())})
  return frozenset(out)
 out=set()
 for i in range(k+1):
  for x in sq_label(i,ls[0]):
   for pr,tail in sq(k-i,(pair,ls[1:])):
    out.symmetric_difference_update({(pr,tuple(sorted((x,)+tail)))})
 return frozenset(out)

@lru_cache(None)
def rho(m):
 pair,ls=m
 out=set()
 for e,f in splits(pair[0]):
  if e==zero:continue
  for g,h in splits(pair[1]):
   if g==zero:continue
   pair2=bracket(labels[e],labels[g])
   if pair2 is None:continue
   base=bm(f,h)
   if base is not None:out.symmetric_difference_update({((pair2,()),base)})
 for x in ls:
  nxt=set()
  for (pr,tail),base in out:
   for e,f in splits(x):
    v=bm(base,f)
    if v is None:continue
    tail2=tail if e==zero else tuple(sorted(tail+(labels[e],)))
    nxt.symmetric_difference_update({((pr,tail2),v)})
  out=nxt
 return frozenset(out)

def showm(m):
 pair,ls=m
 return ('*'.join(ls)+'*' if ls else '')+'{'+','.join(pair)+'}'
def show(p):return ' + '.join(showm(m) for m in sorted(p)) or '0'

def linear(p,k):return xor(*(sq(k,m) for m in p))

source=basis(11)
coords=[]
columns=[]
for m in source:
 c=set()
 for n,e in rho(m):
  if e!=zero:c.add(('rho',n,e))
 for k in (1,2,4):
  for n in sq(k,m):c.add((f'Sq{k}',n,zero))
 columns.append(c)
 coords=sorted(set(coords)|c,key=str)
R=(bracket('a','c'),())
target={('Sq4',R,zero)}
position={c:i for i,c in enumerate(coords)}
def enc(c):return sum(1<<position[x] for x in c)
piv={}
for j,c in enumerate(columns):
 v=enc(c);track=1<<j
 while v:
  p=v.bit_length()-1
  if p in piv:v^=piv[p][0];track^=piv[p][1]
  else:piv[p]=(v,track);break
v=enc(target);track=0
while v:
 p=v.bit_length()-1
 if p not in piv:break
 v^=piv[p][0];track^=piv[p][1]
assert v==0,'no one-bracket candidate'
solution={m for i,m in enumerate(source) if (track>>i)&1}
assert xor(*(set(rho(m)) for m in solution))=={(m,zero) for m in solution}
assert not linear(solution,1) and not linear(solution,2)
assert linear(solution,4)=={R}
# Exact independent check of all basis beta-square and Adem Sq2-square.
for n in range(6,12):
 for m in basis(n):
  assert not linear(sq(1,m),1)
  assert linear(sq(2,m),2)==linear(linear(sq(1,m),2),1)
result={'status':'PASS','scope':__doc__.strip(),'ambient_one_bracket_dimension':len(source),
        'candidate':show(solution),'Sq1':show(linear(solution,1)),
        'Sq2':show(linear(solution,2)),'Sq4':show(linear(solution,4)),
        'coaction':'candidate tensor1; hence in the previously proved fiber factor',
        'conclusion':'The AI9 demand beta=Sq2=0,Sq4=R has a genuine fiber-homology solution. No ordinary-map realization inferred.'}
p=root/'outputs'/'I_k1_bracket_fiber.json';p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
