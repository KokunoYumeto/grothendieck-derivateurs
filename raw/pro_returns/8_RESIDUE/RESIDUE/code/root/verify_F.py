"""Exact finite witnesses and affine cones for Part F; no exhaustion claims."""
from finite_categories import *
from itertools import combinations, permutations, product
from pathlib import Path
import sympy as sp
import json
# Unordered two-subset action on FI objects of cardinality 0,1,2,3.
objects=[(n,S) for n in range(4) for S in combinations(range(n),2)]
arrows=[]
for x,y in product(objects,repeat=2):
 n,S=x;m,T=y
 for f in permutations(range(m),n):
  if set(f[i] for i in S)==set(T):arrows.append((x,y,f))
C=Category(objects,arrows,{a:a[0] for a in arrows},{a:a[1] for a in arrows},{x:(x,x,tuple(range(x[0]))) for x in objects},lambda g,f:(f[0],g[1],tuple(g[2][i] for i in f[2])), 'FI2action')
info=C.check();info['pi1']=pi1_presentation(C)
assert info['pi1']['identified_group']=='C2'
# Scope guard for F.4: disconnected finite shapes are not forced filtered.
# For a discrete indexing category the Grothendieck construction and ordinary
# Cat-colimit are both the same coproduct, for every diagram (definitionally).
discrete_two=poset(2,lambda i,j:i==j,'discrete two objects')
scope_guard=discrete_two.check()
scope_guard['components']=len(discrete_two.components())
scope_guard['common_successors_of_0_and_1']=[r for r in discrete_two.objects
 if discrete_two.hom[0,r] and discrete_two.hom[1,r]]
assert scope_guard['components']==2 and not scope_guard['common_successors_of_0_and_1']
scope_guard['universal_comparison']='Both categories are the coproduct, by definition for every diagram.'
# Polynomial interpolation construction from scratch, integer symbolic coefficients.
def affine_polynomial(n,k=1):
 z=sp.symbols('z0:'+str(n+2))
 if n==0:return sp.Integer(1),z
 q,y=affine_polynomial(n-1,2*k)
 # Replace recursively named variables by target z-with-merged-coordinate lifts.
 # F_i(y) = Q(y) product_{l!=i} y_l^k.  Lift D_i via y_l=z_l for l<=i, z_{l+1} otherwise.
 lifts=[]
 for i in range(n+1):
  F=q*sp.prod(y[l]**k for l in range(n+1) if l!=i)
  lifts.append(sp.expand(F.subs({y[l]:(z[l] if l<=i else z[l+1]) for l in range(n+1)}, simultaneous=True)))
 # Inclusion-exclusion uses independent coordinates x_i=z_i-z_{i+1}, u=z_{n+1}.
 xx=sp.symbols('x0:'+str(n+1)); uu=sp.Symbol('u')
 liftx=[sp.expand(v.subs({z[j]:uu+sum(xx[j:]) for j in range(n+2)},simultaneous=True)) for v in lifts]
 out=0
 for size in range(1,n+2):
  for S in combinations(range(n+1),size):
   subst={xx[i]:0 for i in S}
   phi=sp.expand(liftx[S[0]].subs(subst,simultaneous=True))
   for i in S:assert sp.expand(liftx[i].subs(subst,simultaneous=True)-phi)==0
   out+=(-1)**(size+1)*phi
 out=out.subs({**{xx[i]:z[i]-z[i+1] for i in range(n+1)},uu:z[-1]},simultaneous=True)
 out=sp.expand(out)
 assert out.subs(dict.fromkeys(z,1))==1
 yy=sp.symbols('y0:'+str(n+1)); vals=[]
 for i in range(n+1):
  sub={z[j]:(yy[j] if j<=i else yy[j-1]) for j in range(n+2)}
  vals.append(sp.expand(yy[i]**k*out.subs(sub,simultaneous=True)))
 assert all(sp.expand(v-vals[0])==0 for v in vals)
 return out,z
cones=[]
for n in range(1,4):
 P,z=affine_polynomial(n)
 pol=sp.Poly(P,*z);deg=pol.total_degree();M=n+deg
 terms=[]
 for powers,coeff in pol.terms():
  pos=[];j=powers[0];pos.append(j)
  for gap in powers[1:n+1]:j+=gap+1;pos.append(j)
  terms.append({'injection':pos,'coefficient':int(coeff)})
 assert sum(x['coefficient'] for x in terms)==1
 # Verify every injection [m]->[n], not just cofaces.
 for m in range(n):
  values=[]
  for h in combinations(range(n+1),m+1):
   d={}
   for term in terms:
    key=tuple(term['injection'][j] for j in h)
    d[key]=d.get(key,0)+term['coefficient']
   values.append({a:b for a,b in d.items() if b})
  assert all(v==values[0] for v in values)
 cones.append({'n':n,'target_M':M,'terms':terms,'all_parallel_injections_equalized':True})
out={'FI_two_subset_action_through_cardinality_3':info,'affine_cones':cones,'F4_connectedness_scope_guard':scope_guard,'scope':'The FI computation is a finite witness plus an explicitly proved all-size deformation retraction. Polynomial checks n<=3 corroborate the inductive proof, not an extrapolation.'}
Path(__file__).with_name('F_output.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'FI_objects':len(C.objects),'FI_arrows':len(C.arrows),'FI_pi1':info['pi1']['identified_group'],'cones':[{k:v for k,v in x.items() if k!='terms'} for x in cones],'all_checks_passed':True},indent=2))
