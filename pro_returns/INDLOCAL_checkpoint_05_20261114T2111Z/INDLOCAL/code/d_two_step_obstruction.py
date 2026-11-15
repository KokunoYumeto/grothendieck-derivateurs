"""Finite core of the fibrant-completion obstruction to two-step extension.

F is infinite and its fibrancy is proved in the paper by the explicit horn
small-object construction. This script checks exactly the seven-point input.
"""
from itertools import product
from collections import deque
from pathlib import Path
import json
# 0,1,2,3,4 are the original P4; 5,6 are its new boundary endpoints.
N=7
rel={(i,i) for i in range(N)}|{(0,1),(2,1),(2,3),(4,3),(0,5),(4,6)}
assert all((a,c) in rel for a,b in rel for bb,c in rel if b==bb)
def paths(a,b):
 return [(a,x,y,z,b) for x,y,z in product(range(N),repeat=3)
         if (a,x) in rel and (y,x) in rel and (y,z) in rel and (b,z) in rel]
def distance(a,b):
 adj={v:set() for v in range(N)}
 for x,y in rel:
  if x!=y:adj[x].add(y);adj[y].add(x)
 todo=deque([(a,0)]);seen={a}
 while todo:
  x,d=todo.popleft()
  if x==b:return d
  for y in adj[x]-seen:seen.add(y);todo.append((y,d+1))
assert paths(0,4)==[(0,1,2,3,4)]
assert paths(5,6)==[]
assert (5,0) not in rel and (6,4) not in rel
result={'objects':N,'nonidentity_arrows':len(rel)-N,
        'old_endpoint_distance':distance(0,4),
        'new_endpoint_distance':distance(5,6),
        'old_fixed_endpoint_P4_functors':paths(0,4),
        'new_fixed_endpoint_P4_functors':paths(5,6),
        'reverse_boundary_arrows_absent':True,
        'connected_tree':len(rel)-N==N-1}
report=json.dumps(result,indent=2)+'\n'
print(report,end='')
Path(__file__).with_suffix('.out').write_text(report)
