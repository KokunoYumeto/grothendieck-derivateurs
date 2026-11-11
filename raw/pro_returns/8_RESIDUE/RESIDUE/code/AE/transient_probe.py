#!/usr/bin/env python3
"""Exploratory rational-homology probe; not an unbounded comparison proof."""
from relative_posets import fixed_paths,beat_core
from sympy import Matrix
R={(i,j) for i in range(4) for j in range(i,4)}
W={(i,i) for i in range(4)}|{(0,2),(1,3)}
for n in range(1,6):
 P=fixed_paths(4,R,W,2*n,1,2);r=beat_core(P,R)
 points=[tuple(x) for c in r['core_paths'] for x in c];N=len(points)
 less=lambda a,b:a!=b and all((x,y) in R for x,y in zip(points[a],points[b]))
 chains=[[(i,) for i in range(N)]]
 for d in range(1,5):chains.append([c+(j,) for c in chains[-1] for j in range(N) if less(c[-1],j)])
 ranks=[0]
 for d in range(1,5):
  idx={c:i for i,c in enumerate(chains[d-1])};mat=[[0]*len(chains[d]) for _ in chains[d-1]]
  for j,c in enumerate(chains[d]):
   for i in range(d+1):mat[idx[c[:i]+c[i+1:]]][j]+=(-1)**i
  ranks.append(Matrix(mat).rank() if mat and chains[d] else 0)
 print(n,len(P),N,list(map(len,chains)),[len(chains[d])-ranks[d]-ranks[d+1] for d in range(4)],flush=True)
