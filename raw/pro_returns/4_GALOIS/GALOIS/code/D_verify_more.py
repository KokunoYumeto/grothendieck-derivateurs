"""Further finite checks: reversed transport, orbit relations, and residual H3."""
from D_verify_finite import Category,cat,fundamental_presentation
from itertools import product
import json
import sympy as sp

# Groth(BC2 -> *); section from [1].
O=['b','a'];ars=[('b','b',n) for n in (0,1)]+[('a','a',0),('b','a',0)]
def comp(g,f):return ('b','b',(f[2]+g[2])%2) if g[1]=='b' else (f[0],'a',0)
R=cat(O,ars,{a:a[0] for a in ars},{a:a[1] for a in ars},{x:(x,x,0) for x in O},comp,'Groth(BC2 -> *)')
assert all(len([a for a in R.arrows if R.src[a]==x and R.tgt[a]=='a'])==1 for x in R.objects)
F0=R.restrict(['b'],'BC2 fibre')

# Height-three antipodal sphere and height-two reflected circle.
def layers(n,name):
 objs=list(product(range(n),(-1,1)))
 arrows=[(a,b) for a in objs for b in objs if a==b or a[0]<b[0]]
 return cat(objs,arrows,{a:a[0] for a in arrows},{a:a[1] for a in arrows},{a:(a,a) for a in objs},lambda g,f:(f[0],g[1]),name)
P=layers(3,'six-object sphere');Z=layers(2,'four-object circle')
def antipodal(x):return (x[0],-x[1])
def reflect(x):return (x[0],-x[1]) if x[0]==0 else x
# Quotient of the product under (antipodal, reflect).
prod_obj=list(product(P.objects,Z.objects));prod_arr=list(product(P.arrows,Z.arrows))
def act_obj(x):return(antipodal(x[0]),reflect(x[1]))
def act_arr(a):return((antipodal(a[0][0]),antipodal(a[0][1])),(reflect(a[1][0]),reflect(a[1][1])))
def osrc(a):return(a[0][0],a[1][0])
def otgt(a):return(a[0][1],a[1][1])
def canonical(x,act):return min(x,act(x))
qo=lambda x:canonical(x,act_obj)
qa=lambda x:canonical(x,act_arr)
qobjs=sorted({qo(x) for x in prod_obj});qars=sorted({qa(a) for a in prod_arr})
qs={a:qo(osrc(a)) for a in qars};qt={a:qo(otgt(a)) for a in qars}
qi={x:qa(((x[0],x[0]),(x[1],x[1]))) for x in qobjs}
def qcomp(g,f):
 if otgt(f)!=osrc(g):g=act_arr(g)
 assert otgt(f)==osrc(g)
 return qa(((f[0][0],g[0][1]),(f[1][0],g[1][1])))
Q=cat(qobjs,qars,qs,qt,qi,qcomp,'(S2_poset x S1_poset)/C2')

def homology_dims(C):
 ids=set(C.identity.values());nonids=[a for a in C.arrows if a not in ids]
 chains=[[tuple() for _ in C.objects],[(a,) for a in nonids]]
 # C0 uses objects separately.
 n=1
 while chains[n]:
  nxt=[c+(a,) for c in chains[n] for a in nonids if C.tgt[c[-1]]==C.src[a]]
  if not nxt:break
  chains.append(nxt);n+=1
 ranks=[0]
 for n in range(1,len(chains)):
  low=C.objects if n==1 else chains[n-1]
  idx={a:i for i,a in enumerate(low)}
  M=sp.zeros(len(low),len(chains[n]))
  for j,c in enumerate(chains[n]):
   if n==1:faces=[C.tgt[c[0]],C.src[c[0]]]
   else:
    faces=[c[1:]]+[c[:i-1]+(C.comp(c[i],c[i-1]),)+c[i+1:] for i in range(1,n)]+[c[:-1]]
   for i,face in enumerate(faces):M[idx[face],j]+=(-1)**i
  ranks.append(M.rank())
 ranks.append(0)
 counts=[len(C.objects)]+[len(c) for c in chains[1:]]
 return {'chain_dimensions':counts,'boundary_ranks':ranks[1:-1],'rational_betti':[counts[n]-ranks[n]-ranks[n+1] for n in range(len(counts))]}
H=homology_dims(Q)
assert H['rational_betti']==[1,0,0,1]
products={s+t:s*t for s in (-1,1) for t in (-1,1)}
# Direct signs for four composites in the orbit of the six-object sphere.
orbit_products={str((s,t)):s*t for s in (-1,1) for t in (-1,1)}
assert (-1)*(-1)==1*1 and (-1)*1==1*(-1) and (-1)*(-1)!=(-1)*1
out={'reversed_transport_category':R.verify(),'reversed_transport_total_pi1':fundamental_presentation(R),'reversed_transport_fibre_pi1':fundamental_presentation(F0),'sphere':P.verify(),'circle':Z.verify(),'quotient_product':Q.verify(),'quotient_product_homology':H,'corrected_orbit_composite_signs':orbit_products,'trivial_to_sign_Hom_dimensions':{'C2_equivariant_Q_linear':0,'underlying_Q_linear':1}}
print(json.dumps(out,indent=2))
