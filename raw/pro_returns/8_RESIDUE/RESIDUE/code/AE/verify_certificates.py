#!/usr/bin/env python3
"""Independent certificate verification; exact integral homology of small cores."""
from pathlib import Path
from itertools import product
from sympy import Matrix,zeros,ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form
import json
from relative_posets import fixed_paths
P=Path(__file__).parent

def integral_homology(points,R,degree=3):
 N=len(points)
 greater=[[j for j in range(N) if i!=j and all((x,y) in R for x,y in zip(points[i],points[j]))] for i in range(N)]
 chains=[[(i,) for i in range(N)]]
 for d in range(1,degree+2):chains.append([c+(j,) for c in chains[-1] for j in greater[c[-1]]])
 boundaries=[zeros(0,N)]
 for d in range(1,degree+2):
  idx={c:i for i,c in enumerate(chains[d-1])};mat=zeros(len(idx),len(chains[d]))
  for j,c in enumerate(chains[d]):
   for k in range(d+1):mat[idx[c[:k]+c[k+1:]],j]+=(-1)**k
  boundaries.append(mat)
 for d in range(1,len(boundaries)-1):assert boundaries[d]*boundaries[d+1]==zeros(boundaries[d].rows,boundaries[d+1].cols)
 result=[]
 for d in range(degree+1):
  m=boundaries[d];nextb=boundaries[d+1];dim=m.cols
  if not m.rows or not m.cols:
   rank=0;v_inv=Matrix.eye(dim)
  else:
   dd,uu,vv=smith_normal_decomp(DomainMatrix.from_Matrix(m).convert_to(ZZ))
   D=dd.to_Matrix();rank=sum(D[i,i]!=0 for i in range(min(D.shape)));v_inv=vv.to_Matrix().inv()
  coords=v_inv*nextb;assert coords[:rank,:]==zeros(rank,nextb.cols)
  rel=coords[rank:,:]
  S=smith_normal_form(rel,domain=ZZ) if rel.rows and rel.cols else rel
  diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
  result.append({'free_rank':dim-rank-len(diag),'torsion':[x for x in diag if x!=1]})
 return {'simplices_by_degree':list(map(len,chains)),'homology':result}

cats={x['id']:x for x in json.loads((P/'relative_posets_catalogue.json').read_text())}
certs=json.loads((P/'relative_posets_certificates.json').read_text())
exceptions=[]
for c in certs:
 cat=cats[c['id']];R=set(map(tuple,cat['order']));W=set(map(tuple,cat['marking']))
 paths=fixed_paths(cat['objects'],R,W,c['L'],c['a'],c['b']);active=set(range(len(paths)))
 def lt(i,j):return i!=j and all((x,y) in R for x,y in zip(paths[i],paths[j]))
 for i,j,direction in c['beat_certificate']:
  assert i in active and j in active
  side={k for k in active if lt(k,i)} if direction=='down' else {k for k in active if lt(i,k)}
  assert j in side
  assert all(k==j or (lt(k,j) if direction=='down' else lt(j,k)) for k in side)
  active.remove(i)
 assert sorted(paths[i] for i in active)==sorted(tuple(p) for comp in c['core_paths'] for p in comp)
 if any(len(comp)>1 for comp in c['core_paths']):
  points=[tuple(p) for comp in c['core_paths'] for p in comp]
  exceptions.append({'id':c['id'],'length':c['L'],'a':c['a'],'b':c['b'],**integral_homology(points,R)})

# Check M, the normalized integral two-cocycle c(e_ij,e_kl)=j*k,
# and a primitive bar cycle pairing to 1 with this integral cocycle.
M=[None,(0,0),(0,1),(1,0),(1,1)]
def mul(a,b):return b if a==0 else a if b==0 else M.index((M[a][0],M[b][1]))
def coc(a,b):return 0 if a==0 or b==0 else M[a][1]*M[b][0]
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(range(5),repeat=3))
assert all(coc(a,b)+coc(mul(a,b),c)==coc(b,c)+coc(a,mul(b,c)) for a,b,c in product(range(5),repeat=3))
z={(1,1):1,(1,3):-1,(2,1):-1,(2,3):1};boundary=[0]*5
for (a,b),v in z.items():boundary[b]+=v;boundary[mul(a,b)]-=v;boundary[a]+=v
assert boundary==[0]*5
assert sum(v*coc(a,b) for (a,b),v in z.items())==1

# Finite central extension by C2; all multiplication and nerve orbit equations.
X=list(product(range(2),range(5),range(2))) # C-arrow, base, central coordinate
q=lambda x:(x[1],(x[0]+x[2])%2)
comp=lambda x,y:((x[0]+y[0])%2,mul(x[1],y[1]),(x[2]+y[2]+coc(x[1],y[1]))%2)
compE=lambda x,y:(mul(x[0],y[0]),(x[1]+y[1]+coc(x[0],y[0]))%2)
act=lambda x,b:((x[0]+b)%2,x[1],(x[2]-b)%2)
assert all(q(comp(x,y))==compE(q(x),q(y)) for x,y in product(X,repeat=2))
assert all(comp(act(x,a),act(y,b))==act(comp(x,y),(a+b)%2) for x,y,a,b in product(X,X,range(2),range(2)))
for length in range(4):
 for seq in product(X,repeat=length):
  orbit={tuple(act(x,b) for x,b in zip(seq,bits)) for bits in product(range(2),repeat=length)}
  assert len(orbit)==2**length
  assert len({tuple(q(x) for x in s) for s in orbit})==1
summary={'verified_beat_certificates':len(certs),'exceptional_cores_integral_homology':exceptions,
 'rectangular_monoid_associativity_equations':125,'integer_cocycle_equations':125,
 'bar_cycle_cocycle_pairing':1,'central_extension_action_checked_through_nerve_degree':3}
(P/'verification_output.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
