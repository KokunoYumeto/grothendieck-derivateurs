#!/usr/bin/env python3
"""Exact signed-lex flag distinction on shared-coordinate edge pairs.

All 12 test pairs are free amalgams of two ordered three-point edges
along one strong singleton. Their positivity and all singleton/edge
strongness conditions are checked exhaustively. Distinct flags disagree
on at least one of these pairs; this is an exact finite certificate for
the last combinatorial step in Proposition G.24.
"""
from itertools import permutations,product
from pathlib import Path
import json

flags=[(i,j,x,y) for i,j in permutations(range(3),2)
       for x,y in product((-1,1),repeat=2)]
profiles=[]
for shared in range(3):
 for signs in product((-1,1),repeat=2):
  e=[];f=[];cursor=iter(signs)
  for k in range(3):
   base=3*k
   if k==shared:e.append(base);f.append(base)
   elif next(cursor)==1:e.append(base);f.append(base+1)
   else:e.append(base+1);f.append(base)
  points=sorted(set(e+f));rename={v:i for i,v in enumerate(points)}
  edges=[tuple(rename[v] for v in w) for w in (e,f)]
  masks=[sum(1<<v for v in w) for w in edges]
  n=len(points)
  delta=[2*m.bit_count()-3*sum(m&em==em for em in masks) for m in range(1<<n)]
  assert min(delta[1:])>0
  for b in masks+[1<<i for i in range(n)]:
   assert all(delta[m]>delta[b] for m in range(1<<n) if m!=b and m&b==b)
  profiles.append(dict(shared=shared,signs=signs,e=e,f=f))

def cmp(flag,profile):
 i,j,x,y=flag;e=profile['e'];f=profile['f']
 a=(x*e[i],y*e[j]);b=(x*f[i],y*f[j])
 return (a>b)-(a<b)

signatures=[tuple(cmp(f,p) for p in profiles) for f in flags]
assert len(set(signatures))==24
witnesses=[]
for i,j in permutations(range(24),2):
 k=next(k for k in range(len(profiles)) if signatures[i][k]!=signatures[j][k])
 witnesses.append(dict(first=i,second=j,profile=k))
assert len(witnesses)==552
report=dict(flags=flags,profiles=profiles,signatures=signatures,
            differing_ordered_pairs=witnesses,exact=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('12 strong shared-coordinate edge-pair types checked on every subset.')
print('24 distinct signed lexicographic flags have 24 distinct comparison signatures.')
print('All 552 ordered unequal flag pairs have an explicit disagreement witness.')
print('PASS: exact finite comparison certificate; no global word extension is asserted.')
