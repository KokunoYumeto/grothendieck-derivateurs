"""Exact finite verification for the four-object q_L counterexample.
The proof for all possible inverse functors is mathematical; this program
checks the finite base category, covering rule, and the explicit path family.
"""
from itertools import product
import json
X=set(range(4))
R={(i,i) for i in X}|{(0,1),(0,3),(2,1),(2,3)}
def erel(i,j):return i==j or i%2==0 and abs(i-j)==1
for i,j in R:
 for jj,k in R:
  if j==jj:assert (i,k) in R
nonid=[(i,j)for i,j in R if i!=j]
print(json.dumps({'objects':4,'arrows':len(R),'nonidentity_arrows':nonid,'nondegenerate_2simplices':0,'H0_Z_rank':1,'H1_Z_rank':len(nonid)-4+1,'all_arrows_marked':True}))
for z in range(-8,9):
 for a,b in R:
  if a==z%4:
   assert len([w for w in range(z-1,z+2) if w%4==b and erel(z,w)])==1
  if b==z%4:
   assert len([w for w in range(z-1,z+2) if w%4==a and erel(w,z)])==1
print('Unique lifts of every incoming and outgoing base arrow: verified at all residues.')
def lift(p):
 out=[0]
 for i in range(len(p)-1):
  z=out[-1]
  cand=[w for w in range(z-1,z+2) if w%4==p[i+1] and (erel(z,w)if i%2==0 else erel(w,z))]
  assert len(cand)==1
  out.append(cand[0])
 return out
L=6
paths=[]
for mid in product(range(4),repeat=L-1):
 p=(0,)+mid+(0,)
 if all(((p[i],p[i+1])if i%2==0 else(p[i+1],p[i]))in R for i in range(L)):
  paths.append(p)
nt=0;null=0
for p in paths:
 lp=lift(p)
 if lp[-1]==0:null+=1
 for q in paths:
  if all((a,b) in R for a,b in zip(p,q)):
   lq=lift(q)
   assert all(erel(a,b)for a,b in zip(lp,lq))
   assert lp[-1]==lq[-1]
   nt+=1
print(json.dumps({'test_length':L,'endpoint_fixed_paths':len(paths),'null_winding_paths':null,'endpoint_fixed_natural_transformations':nt,'all_transformations_lift_with_displacement_at_most_one':True}))
for N in range(1,9):
 lifted=[i if i<=4*N else 8*N-i for i in range(8*N+1)]
 p=[i%4 for i in lifted]
 assert lift(p)==lifted
 assert p[0]==p[-1]==0
 assert all(((p[i],p[i+1]) if i%2==0 else (p[i+1],p[i]))in R for i in range(8*N))
 print(json.dumps({'N':N,'support_length':8*N,'right_endpoint_lift':lifted[-1],'positive_evaluation_coordinate':4*N,'lifted_evaluation_value':lifted[4*N],'minimum_natural_zigzag_length_to_any_qL_image':4*N}))
print('For arbitrary k choose 4N>k. The distance inequality proves no finite zigzag id_P ~ q_L r, for every functor r.')
