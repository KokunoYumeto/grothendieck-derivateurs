#!/usr/bin/env python3
"""Independent exact minor certificates for the saved signed-lex twisted X11 model."""
from collections import Counter
from pathlib import Path
import json
import sympy as sp
src=Path(__file__).with_name('G_twisted_lex_chains.json')
d=json.loads(src.read_text());w=d['best']['point_words'];n=d['n']
# Canonical alphabet labels: least global word position in each class, numbered1...
minimum={};at=0
for word in w:
 for old in word:
  at+=1;minimum.setdefault(old,at)
w=[[minimum[x] for x in word] for word in w]
# Reconstruct the equivalence relation independently as connected components,
# rather than reusing the union-find search implementation.
lengths=d['best']['lengths'];offsets=[0]
for size in lengths:offsets.append(offsets[-1]+size)
assert offsets[-1]==2898
adj=[set() for _ in range(offsets[-1])]
def pair(left,right):
 assert len(left)==len(right)
 for x,y in zip(left,right):adj[x].add(y);adj[y].add(x)
qblocks=[];sblocks=[]
for (a,b,c),z in zip(d['edges'],d['best']['rectangle_lengths']):
 p,q,r,s=(z[k] for k in 'pqrs')
 pair(list(range(offsets[a],offsets[a]+p)),list(range(offsets[n+c]+s,offsets[n+c+1])))
 qb=list(range(offsets[a]+p,offsets[a+1]));qblocks.append(qb)
 pair(qb,list(range(offsets[b]+r,offsets[b+1])))
 pair(list(range(offsets[b],offsets[b]+r)),list(range(offsets[n+a]+s,offsets[n+a+1])))
 sb=list(range(offsets[n+c],offsets[n+c]+s));sblocks.append(sb)
 pair(sb,list(range(offsets[n+a],offsets[n+a]+s)))
for qb in qblocks:pair(qb,qblocks[0][-len(qb):])
for sb in sblocks:pair(sb,sblocks[0][:len(sb)])
component={}
for x in range(len(adj)):
 if x in component:continue
 todo=[x];seen={x}
 while todo:
  y=todo.pop()
  for z in adj[y]:
   if z not in seen:seen.add(z);todo.append(z)
 label=min(seen)+1
 for y in seen:component[y]=label
rebuilt=[[component[x] for x in range(offsets[i],offsets[i+1])] for i in range(2*n)]
assert rebuilt==w
from itertools import combinations
for x,y in combinations(w,2):
 assert x!=y[:len(x)] and y!=x[:len(y)]
 assert x!=y[-len(x):] and y!=x[-len(y):]
assert len(set(component.values()))==1213
print('Independent position-graph reconstruction:2898 positions,1213 classes; saved words match.')
counts=[Counter(word) for word in w]
alphabet=sorted(minimum.values())
patterns={}
for letter in alphabet:
 pattern=tuple(c[letter] for c in counts)
 patterns.setdefault(pattern,letter)
patterns=list(patterns.items())
mat=sp.Matrix(2*n,len(patterns),lambda i,j:patterns[j][0][i])
rows=list(mat.T.rref()[1]);cols=list(mat[rows,:].rref()[1])
minor=mat.extract(rows,cols);det=int(minor.det())
assert len(rows)==d['expected_rank']==16 and det!=0
point=dict(rows=[i+1 for i in rows],columns=[patterns[j][1] for j in cols],
           determinant=det,matrix=[list(map(int,minor.row(i))) for i in range(minor.rows)])
print('Point minor rows:',point['rows'])
print('Point minor alphabet labels:',point['columns'])
print('Point minor determinant:',det)
edge=[]
for e,((a,b,c),z) in enumerate(zip(d['edges'],d['best']['rectangle_lengths'])):
 p=w[a][:z['p']];q=w[a][z['p']:];r=w[b][:z['r']];s=w[n+c][:z['s']]
 ims=[p,q,r,s,w[c],w[n+b]];cs=[Counter(x) for x in ims]
 letters=sorted(set().union(*(set(x) for x in ims)))
 em=sp.Matrix(6,len(letters),lambda i,j:cs[i][letters[j]])
 ec=list(em.rref()[1]);e_minor=em[:,ec];e_det=int(e_minor.det())
 assert len(ec)==6 and e_det!=0
 row=dict(edge=e,columns=[letters[j] for j in ec],determinant=e_det,
          matrix=[list(map(int,e_minor.row(i))) for i in range(6)])
 edge.append(row)
 print('Edge',e,'minor labels',row['columns'],'determinant',e_det)
incidence=sp.zeros(len(d['edges']),2*n)
for j,(a,b,c) in enumerate(d['edges']):
 incidence[j,b]+=1;incidence[j,a]-=1
 incidence[j,n+c]+=1;incidence[j,n+a]-=1
ic=list(incidence.rref()[1]);idet=int(incidence[:,ic].det())
assert abs(idet)==1
relation=dict(columns=[x+1 for x in ic],determinant=idet)
print('Incidence matrix unit minor:',relation)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(point=point,edges=edge,incidence=relation),indent=2)+'\n')
print('All certificates use exact integer arithmetic. PASS')
