"""Exhaustive elementary checks for the remaining finite Part D examples."""
from D_verify_finite import cat
from itertools import product
import json
import sympy as sp

objs=list(product(range(2),(-1,1)))
ars=[(a,b) for a in objs for b in objs if a==b or a[0]<b[0]]
Z=cat(objs,ars,{a:a[0] for a in ars},{a:a[1] for a in ars},{x:(x,x) for x in objs},lambda g,f:(f[0],g[1]),'four-object circle')
# Trivial two-sheet bundle; sheet swap is a nonidentity automorphism over Z.
BO=list(product(objs,(0,1)))
BA=list(product(ars,(0,1)))
B=cat(BO,BA,{a:(a[0][0],a[1]) for a in BA},{a:(a[0][1],a[1]) for a in BA},{x:((x[0],x[0]),x[1]) for x in BO},lambda g,f:(Z.comp(g[0],f[0]),f[1]),'trivial two-sheet bundle')
so=lambda x:(x[0],1-x[1]);sa=lambda a:(a[0],1-a[1])
for a in BA:
 assert B.src[sa(a)]==so(B.src[a]) and B.tgt[sa(a)]==so(B.tgt[a])
 assert sa(sa(a))==a
for (g,f),h in B.composition.items():assert B.comp(sa(g),sa(f))==sa(h)
assert any(so(x)!=x for x in BO)
# E=C2 discrete with diagonal quotient E x Z. Its two-element orbits
# have a unique representative with E-coordinate zero.
def refl(x):return(x[0],-x[1]) if x[0]==0 else x
def refl_arrow(a):return(refl(a[0]),refl(a[1]))
def image_obj(g,z):return refl(z) if g else z
def image_arrow(g,a):return refl_arrow(a) if g else a
for g,z in product((0,1),objs):
 assert image_obj(g,z)==image_obj(1-g,refl(z))
for g,a in product((0,1),ars):
 assert image_arrow(g,a)==image_arrow(1-g,refl_arrow(a))
for g in (0,1):
 for (v,u),w in Z.composition.items():
  assert Z.comp(image_arrow(g,v),image_arrow(g,u))==image_arrow(g,w)
# Proper cosieve {1}->[1]: arrow/comma lists.
Iars=[(0,0),(1,1),(0,1)]
I=cat([0,1],Iars,{a:a[0] for a in Iars},{a:a[1] for a in Iars},{x:(x,x) for x in (0,1)},lambda g,f:(f[0],g[1]),'interval')
comma_counts=[len([a for a in Iars if a[0]==1 and a[1]==b]) for b in (0,1)]
assert comma_counts==[0,1]
# Trivial-to-sign equivariant Hom has equation (-1)f=f, rank 1.
nullity=1-sp.Matrix([[-2]]).rank()
assert nullity==0
print(json.dumps({'circle':Z.verify(),'trivial_bundle':B.verify(),'sheet_swap_nonidentity':True,'regular_quotient_isomorphism_to_Z_checked':True,'proper_cosieve_comma_object_counts':comma_counts,'Q_trivial_to_sign_Hom_dimension':int(nullity),'underlying_Hom_dimension':1},indent=2))
