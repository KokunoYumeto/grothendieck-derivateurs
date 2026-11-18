#!/usr/bin/env python3
"""Exact free-group fold of the finite twisted chart's U,V and Q words.

This checks group ranks only. It does not assert a positive-basis construction
or a functor on the whole predimension category.
"""
from pathlib import Path
from collections import Counter
import json
import sympy as sp

report=json.loads(Path(__file__).with_name('G_twisted_lex_chains.json').read_text())
words=report['best']['point_words'];n=report['n'];edges=report['edges']
qs=[words[a][z['p']:] for (a,b,c),z in zip(edges,report['best']['rectangle_lengths'])]
allwords=words+qs
# Signed integer edge labels; no assumptions on text-alphabet case.
letters={a:i+1 for i,a in enumerate(sorted(set(sum(allwords,[]))))}
w=[[letters[x] for x in word] for word in allwords]
es=[];vertex=1
for word in w:
 s=0
 for j,a in enumerate(word):
  t=0 if j==len(word)-1 else vertex
  if t:vertex+=1
  es.extend(((s,a,t),(t,-a,s)));s=t
parent=list(range(vertex))
def find(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
changed=True
while changed:
 changed=False;out={}
 for s,a,t in es:
  s,t=find(s),find(t)
  if (s,a) in out:
   u=find(out[s,a])
   if u!=t:parent[t]=u;changed=True
  else:out[s,a]=t
folded={(find(s),a,find(t)) for s,a,t in es}
vs={s for s,a,t in folded}|{t for s,a,t in folded}
rank=len(folded)//2-len(vs)+1
counts=[Counter(word) for word in w]
patterns=sorted({tuple(c[a] for c in counts) for a in letters.values()})
mat=sp.Matrix(len(w),len(patterns),lambda i,j:patterns[j][i])
ab_rank=mat.rank()
print('Point generators:',2*n,'edge Q generators:',len(edges))
print('Folded graph vertices:',len(vs),'unoriented edges:',len(folded)//2,'rank:',rank)
print('Abelian image rank:',ab_rank,'conjugacy presentation rank:',2*n)
assert rank==ab_rank==2*n
print('PASS: finite conjugacy presentation maps isomorphically onto a free group of expected rank.')
print('The last conclusion uses its private-vertex freeness and Hopficity; no global positive-basis inference.')
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(vertices=len(vs),edges=len(folded)//2,
 group_rank=rank,abelian_rank=ab_rank,presentation_rank=2*n,finite_only=True),indent=2)+'\n')
