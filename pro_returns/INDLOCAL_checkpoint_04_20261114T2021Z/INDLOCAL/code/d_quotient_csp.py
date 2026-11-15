"""Exact bounded-fence CSP in the dimension-two relative simplex cylinder."""
import json,time
from collections import deque
from pathlib import Path
from functools import lru_cache
D=json.loads(Path(__file__).with_name('d_quotient_probe.json').read_text())
up=D['reach'];N=len(up);down=[sum(1<<j for j in range(N) if (up[j]>>i)&1) for i in range(N)]
M=len(D['unknown'])
def bits(s):
 while s:
  z=s&-s;yield z.bit_length()-1;s-=z

def solve(length,nodecap=200000):
 V=(length+1)*M
 domains=[sum(1<<r for r in D['allowed'][i%M]) for i in range(V)]
 for i,x in enumerate(D['start']):domains[i]=1<<x
 for i,x in enumerate(D['end']):domains[length*M+i]=1<<x
 edges=[]
 for t in range(length+1):
  edges.extend((t*M+i,t*M+j) for i,j in D['source_le'])
 for t in range(length):
  edges.extend(((t*M+i,(t+1)*M+i) if t%2==0 else ((t+1)*M+i,t*M+i)) for i in range(M))
 adj=[[] for _ in range(V)]
 for k,(a,b) in enumerate(edges):adj[a].append(k);adj[b].append(k)
 nodes=0;begin=time.monotonic()
 def prop(ds,queue):
  queue=deque(queue);pending=set(queue)
  while queue:
   k=queue.popleft();pending.discard(k);a,b=edges[k]
   da,db=ds[a],ds[b]
   na=sum(1<<v for v in bits(da) if up[v]&db)
   if not na:return False
   nb=sum(1<<v for v in bits(db) if down[v]&na)
   if not nb:return False
   for j,old,new in [(a,da,na),(b,db,nb)]:
    if old!=new:
     ds[j]=new
     for e in adj[j]:
      if e!=k and e not in pending:queue.append(e);pending.add(e)
  return True
 if not prop(domains,range(len(edges))):
  return {'length':length,'satisfiable':False,'nodes':0,'arc_consistency_refutation':True}
 unresolved=sum(d.bit_count()>1 for d in domains)
 print('length',length,'AC variables',unresolved,'domain max',max(d.bit_count() for d in domains),flush=True)
 def dfs(ds):
  nonlocal nodes
  nodes+=1
  if nodes>nodecap:raise RuntimeError('cap')
  choices=[(d.bit_count(),-len(adj[i]),i) for i,d in enumerate(ds) if d.bit_count()>1]
  if not choices:return ds
  _,_,i=min(choices)
  for v in bits(ds[i]):
   nd=ds.copy();nd[i]=1<<v
   if prop(nd,adj[i]):
    out=dfs(nd)
    if out:return out
  return None
 try:
  sol=dfs(domains)
 except RuntimeError:
  return {'length':length,'satisfiable':None,'nodes':nodes,'seconds':time.monotonic()-begin}
 if sol:
  vals=[next(bits(d)) for d in sol]
  assert all((up[vals[a]]>>vals[b])&1 for a,b in edges)
  route=[vals[t*M:(t+1)*M] for t in range(length+1)]
 else:route=None
 return {'length':length,'satisfiable':bool(sol),'nodes':nodes,'seconds':time.monotonic()-begin,'route':route}
results=[]
for length in [2,4,6,8,10,12]:
 r=solve(length);results.append(r);print(json.dumps(r),flush=True)
 Path(__file__).with_suffix('.out').write_text(json.dumps(results,indent=2)+'\n')
 if r['satisfiable']:break
