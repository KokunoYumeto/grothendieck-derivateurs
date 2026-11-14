"""Explore the finite relative simplex cylinder in dimension two.

This script constructs its poset by the explicit colimit identifications,
checks antisymmetry, and records the domain sizes for fixed-boundary maps.
"""
from itertools import combinations
from pathlib import Path
import json

def flags(vertices):
    faces=[frozenset(x) for k in range(1,len(vertices)+1) for x in combinations(vertices,k)]
    out=[]
    def visit(c):
        out.append(frozenset(c))
        for s in faces:
            if c[-1]<s:visit(c+[s])
    for s in faces:visit([s])
    return out
n=2
src=flags(tuple(range(n+1))); allq=flags(tuple(range(n+2)))
top=frozenset(range(n+1))
boundary=[c for c in src if max(c,key=len)!=top]
def proj(c):
    return frozenset(frozenset(n if v==n+1 else v for v in s) for s in c)
def cls(c):
    pc=proj(c)
    return ('b',pc) if max(pc,key=len)!=top else ('i',c)
classes=list(dict.fromkeys(cls(c) for c in allq)); ids={c:i for i,c in enumerate(classes)}
N=len(classes); reach=[1<<i for i in range(N)]
for c in allq:
    ci=ids[cls(c)]
    for k in range(1,len(c)):
        for sub in combinations(c,k):reach[ids[cls(frozenset(sub))]]|=1<<ci
for k in range(N):
    for i in range(N):
        if (reach[i]>>k)&1:reach[i]|=reach[k]
assert all(not ((reach[i]>>j)&1 and (reach[j]>>i)&1) for i in range(N) for j in range(i))
unknown=[c for c in src if max(c,key=len)==top]
allowed={c:[r for r in range(N) if all((reach[ids[('b',a)]]>>r)&1 for a in boundary if a<=c)] for c in unknown}
print('Quotient size',N,'unknown values',len(unknown),'domain sizes',sorted(map(len,allowed.values())))
# Store serialization for followup exact solvers; finite ids are stable here.
def encode(c):return sorted([sorted(s) for s in c],key=lambda s:(len(s),s))
data={'n':n,'classes':[[tag,encode(c)] for tag,c in classes],
      'reach':reach,'source':[encode(c) for c in src],
      'unknown':[encode(c) for c in unknown],
      'allowed': [allowed[c] for c in unknown],
      'source_le':[[i,j] for i,c in enumerate(unknown) for j,d in enumerate(unknown) if c<d],
      'start':[ids[cls(c)] for c in unknown],
      'end':[ids[cls(frozenset(frozenset(n+1 if v==n else v for v in s) for s in c))] for c in unknown]}
Path(__file__).with_suffix('.json').write_text(json.dumps(data)+'\n')
