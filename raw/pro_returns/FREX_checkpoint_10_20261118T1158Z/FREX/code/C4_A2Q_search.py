"""Exact finite tests for one A_2(Q) affine family. No all-module claim."""
from itertools import combinations
from fractions import Fraction as F
import random, json, time
random.seed(20261118)

def gf2solve(rows,n):
 rows=rows[:]; pivot=[]; rank=0
 for j in range(n):
  v=next((i for i in range(rank,len(rows)) if (rows[i]>>j)&1),None)
  if v is None: continue
  rows[rank],rows[v]=rows[v],rows[rank]
  for i in range(len(rows)):
   if i!=rank and (rows[i]>>j)&1: rows[i]^=rows[rank]
  pivot.append(j); rank+=1
 for row in rows[rank:]:
  if row>>n: return None
 pset=set(pivot); free=[j for j in range(n) if j not in pset]
 particular=sum(((rows[i]>>n)&1)<<j for i,j in enumerate(pivot))
 basis=[]
 for f in free:
  v=1<<f
  for i,j in enumerate(pivot):
   if (rows[i]>>f)&1:v|=1<<j
  basis.append(v)
 return particular,basis

def rational_consistent(n, qs):
 # Variables only b_ij with i>0; gauge b_0j=0. Gaussian exact sparse rows.
 es=list(combinations(range(1,n),2)); ix={x:i for i,x in enumerate(es)}
 basis={}
 for q in qs:
  for tri,val in [((0,1,2),1),((0,1,3),0),((0,2,3),0),((1,2,3),1)]:
   a,b,c=(q[x] for x in tri); row={}
   for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
    if e[0]:row[ix[e]]=F(s)
   rhs=F(val)
   while row:
    p=min(row); coeff=row[p]
    if p not in basis:
     row={j:v/coeff for j,v in row.items()}; rhs/=coeff
     basis[p]=(row,rhs);break
    br,bb=basis[p]
    for j,v in br.items():
     row[j]=row.get(j,F(0))-coeff*v
     if not row[j]:del row[j]
    rhs-=coeff*bb
   else:
    if rhs:return False,None
 sol=[F(0)]*len(es)
 for p,(row,rhs) in sorted(basis.items(),reverse=True):
  sol[p]=rhs-sum(v*sol[j] for j,v in row.items() if j!=p)
 return True,{str(e):str(sol[i]) for i,e in enumerate(es) if sol[i]}

for n in range(4,12):
 qs=list(combinations(range(n),4)); pairs=list(combinations(range(n),2)); pi={e:i for i,e in enumerate(pairs)}
 # all six position-pair arrows to Q, compared to (0,1)
 aps=list(combinations(range(4),2)); rows=[0]*(5*len(pairs))
 for z,q in enumerate(qs):
  base=pi[(q[0],q[1])]
  for i,(a,b) in enumerate(aps[1:]):
   rows[i*len(pairs)+base]^=1<<z
   rows[i*len(pairs)+pi[(q[a],q[b])]]^=1<<z
 rows.append(((1<<len(qs))-1)|(1<<len(qs)))
 ans=gf2solve(rows,len(qs))
 print('n',n,'Qcopies',len(qs),'solvable',ans is not None,flush=True)
 if ans is None:continue
 v,basis=ans
 print('kernel dimension',len(basis),'particular weight',v.bit_count(),flush=True)
 best=None
 for attempt in range(20000):
  if attempt:
   # random greedy descent within the affine solution space
   v0=v
   for _ in range(2):
    for w in random.sample(basis,len(basis)):
     if (v0^w).bit_count()<v0.bit_count() or random.random()<.003:v0^=w
   if random.random()<.1:
    v0=v
    for w in basis:
     if random.randrange(2):v0^=w
  else:v0=v
  support=[q for i,q in enumerate(qs) if (v0>>i)&1]
  if best is None or len(support)<best:
   best=len(support);print('best weight',best,flush=True)
  ok,cochain=rational_consistent(n,support)
  if ok:
   out={'n':n,'support':support,'cochain':cochain,'attempt':attempt}
   print('FOUND',json.dumps(out),flush=True)
   open('FREX/code/C4_A2Q_found.json','w').write(json.dumps(out,indent=2))
   raise SystemExit
 print('none in 20000 tested solutions',flush=True)
