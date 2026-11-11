#!/usr/bin/env python3
"""Direct independent check of the uniform closure operator used in E.1."""
from pathlib import Path
from itertools import product
import json
from path_chain import paths
le=lambda p,q:all(x<=y for x,y in zip(p,q))
rows=[]
for n in range(2,7):
 for a,b in product(range(3),repeat=2):
  P=paths(n,a,b)
  if a in [0,2]:
   lo=tuple([a]+[0]*(2*n-1)+[b]);assert lo in P and all(le(lo,p) for p in P)
  elif b==2:
   hi=tuple([1,1]+[2]*(2*n-1));assert hi in P and all(le(p,hi) for p in P)
  elif b==0:
   hi=tuple([1,1]+[2]*(2*n-3)+[0,0]);assert hi in P and all(le(p,hi) for p in P)
  else:
   const=tuple([1]*(2*n+1));Q=[p for p in P if p!=const]
   assert all(not le(p,const) and not le(const,p) for p in Q)
   u=tuple([1,1,2]+[0]*(2*n-3)+[1]);assert u in Q
   def R(p):
    k=p.index(0);assert k>=3 and k%2==1
    return p[:2]+(2,)*(k-2)+p[k:]
   assert all(R(p) in Q and le(p,R(p)) and le(u,R(p)) for p in Q)
   assert all(R(p)==p for p in Q if le(u,p))
   assert all(not le(p,q) or le(R(p),R(q)) for p in Q for q in Q)
  rows.append({'n':n,'a':a,'b':b,'objects':len(P),'formula_verified':True})
# Walking retraction R. Multiplication is tested as g after f.
ends={'1A':('A','A'),'1B':('B','B'),'i':('A','B'),'r':('B','A'),'e':('B','B')}
comp={}
for f,g in product(ends,repeat=2):
 if ends[f][1]!=ends[g][0]:continue
 if f.startswith('1'):h=g
 elif g.startswith('1'):h=f
 else:h={('i','r'):'1A',('r','i'):'e',('e','e'):'e',('i','e'):'i',('e','r'):'r'}[(f,g)]
 comp[f,g]=h
for f,g,h in product(ends,repeat=3):
 if (f,g) in comp and (g,h) in comp:assert comp[comp[f,g],h]==comp[f,comp[g,h]]
summary={'closure_operator_checks':rows,'walking_retraction':{'arrows':ends,'composition':[[*k,v] for k,v in comp.items()]}}
p=Path(__file__).with_name('chain_closure_check_output.json');p.write_text(json.dumps(summary,indent=2));print('Verified 45 endpoint/length cases and walking-retraction associativity')
