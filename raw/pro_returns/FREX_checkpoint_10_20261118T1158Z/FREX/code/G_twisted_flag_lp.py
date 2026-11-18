#!/usr/bin/env python3
"""Finite real-length feasibility for the 576 signed-lex q/s regimes.

This is exploratory: HiGHS floating-point statuses are not formal
infeasibility certificates. Same-flag feasibility has the exact elementary
constant-U, constant-V proof stated in the progress notes. No global word
lift or nonexistence is inferred from these scalar tests.
"""
from itertools import permutations, product
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
from G_cross_lift_rank_search import EDGES

FLAGS=[(i,j,eps,eta) for i,j in permutations(range(3),2)
       for eps,eta in product((-1,1),repeat=2)]

def ordered(edges,flag):
 i,j,eps,eta=flag
 return sorted(range(len(edges)),key=lambda t:(eps*edges[t][i],eta*edges[t][j]))

def test(n,edges,fq,fs):
 # Variables U[0:n], V[n:2n], Q[2n:2n+m], S[2n+m:2n+2m].
 m=len(edges); size=2*n+2*m
 eq=[]
 for e,(a,b,c) in enumerate(edges):
  row=np.zeros(size);row[b]=1;row[a]-=1;row[n+c]+=1;row[n+a]-=1;eq.append(row)
  row=np.zeros(size);row[2*n+m+e]=1;row[2*n+e]=-1;row[n+c]=-1;row[a]=1;eq.append(row)
 ub=[];rhs=[]
 for e,(a,b,c) in enumerate(edges):
  for x in (a,b):
   row=np.zeros(size);row[2*n+e]=1;row[x]=-1;ub.append(row);rhs.append(-1)
 for flag,offset in ((fq,2*n),(fs,2*n+m)):
  order=ordered(edges,flag)
  for x,y in zip(order,order[1:]):
   row=np.zeros(size);row[offset+x]=1;row[offset+y]=-1;ub.append(row);rhs.append(-1)
 result=linprog(np.ones(size),A_ub=np.array(ub),b_ub=np.array(rhs),
                A_eq=np.array(eq),b_eq=np.zeros(len(eq)),bounds=(1,None),
                method='highs')
 return result.status

shapes={
 'X11':(11,EDGES),
 'grid2':(8,[(0,2,6),(0,5,7),(1,4,6),(1,3,7)]),
 # The 3x3 grid with one edge removed has six outer vertices,
 # eight incident private middle vertices, and one isolated middle vertex.
 # A full nine-edge grid would not have strong edge copies; it is excluded.
 'grid3_minus_edge':(15,[(i,3+(i*3+j),12+j) for i in range(3) for j in range(3) if (i,j)!=(2,2)]),
}
for k,mids in enumerate(permutations(range(2,6))):
 shapes['grid2_order_'+str(k)]=(8,[(0,mids[0],6),(0,mids[1],7),(1,mids[2],6),(1,mids[3],7)])
rows=[]
for name,(n,edges) in shapes.items():
 edge_masks=[sum(1<<x for x in e) for e in edges]
 delta=[2*mask.bit_count()-3*sum(mask&em==em for em in edge_masks) for mask in range(1<<n)]
 assert min(delta[1:])>0
 for base in [1<<x for x in range(n)]+edge_masks:
  assert all(delta[mask]>delta[base] for mask in range(1<<n) if mask!=base and mask&base==base)
 print(name,'exact nonempty subset and strong singleton/edge checks passed',flush=True)
 statuses=[]
 for iq,fq in enumerate(FLAGS):
  statuses.append([test(n,edges,fq,fs) for fs in FLAGS])
 counts={str(status):sum(row.count(status) for row in statuses) for status in sorted(set(sum(statuses,[])))}
 assert all(statuses[i][i]==0 for i in range(24))
 print(name,'flags=',len(FLAGS)**2,'status_counts=',counts,flush=True)
 rows.append(dict(name=name,n=n,edges=edges,statuses=statuses,counts=counts))
report=dict(flags=FLAGS,shapes=rows,
 status_meaning={'0':'feasible numerical optimum','2':'numerically infeasible'},
 formal_certificate=False,finite_scalar_constraints_only=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
common=[(i,j) for i in range(24) for j in range(24)
        if all(row['statuses'][i][j]==0 for row in rows)]
print('Pairs numerically feasible in all shapes:',len(common))
print('No assertion of global word feasibility or formal nonexistence.')
