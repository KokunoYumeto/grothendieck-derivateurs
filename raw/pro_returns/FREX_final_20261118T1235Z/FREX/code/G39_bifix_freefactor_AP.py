#!/usr/bin/env python3
"""Cone-compatible bifix free-monoid amalgamation fails.
Both group maps are isomorphisms and the positive abelian matrices agree.
"""
import json
from pathlib import Path
from sympy import Matrix

def inv(w):return tuple(-a for a in reversed(w))
def red(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return tuple(out)
def mul(*ws):return red(sum(ws,()))
def subst(w,images):
 return mul(*(images[a] if a>0 else inv(images[-a]) for a in w))
def bifix(ws):
 for i,a in enumerate(ws):
  for j,b in enumerate(ws):
   if i==j:continue
   assert not(len(a)<=len(b) and b[:len(a)]==a)
   assert not(len(a)<=len(b) and b[-len(a):]==a)
 return True
x,y,z=(1,),(2,),(3,)
# Intermediate alphabet t,b,c.
sigma={1:(2,1),2:(2,3,1),3:(3,3,1)}
c=mul(z,inv(x),y,inv(z));t=mul(inv(c),inv(c),z);b=mul(x,inv(t))
siginv={1:t,2:b,3:c}
checks=0
for r in range(1,4):
 assert subst(sigma[r],siginv)==(r,);checks+=1
 assert subst(siginv[r],sigma)==(r,);checks+=1
# t maps to acb in the first target and ABC in the second target.
i0={1:(1,3,2),2:(2,),3:(3,)};j0={1:(1,2,3),2:(2,),3:(3,)}
i={r:subst(sigma[r],i0) for r in range(1,4)}
j={r:subst(sigma[r],j0) for r in range(1,4)}
iinv={1:mul(t,inv(b),inv(c)),2:b,3:c}
jinv={1:mul(t,inv(c),inv(b)),2:b,3:c}
for fmap,finv in [(i,iinv),(j,jinv)]:
 for r in range(1,4):
  assert subst(fmap[r],finv)==(r,);checks+=1
  assert subst(finv[r],fmap)==(r,);checks+=1
assert checks==18
assert i=={1:(2,1,3,2),2:(2,3,1,3,2),3:(3,3,1,3,2)}
assert j=={1:(2,1,2,3),2:(2,3,1,2,3),3:(3,3,1,2,3)}
assert bifix(list(i.values())) and bifix(list(j.values()))
Mi=Matrix([[i[k].count(r) for k in range(1,4)]for r in range(1,4)])
Mj=Matrix([[j[k].count(r) for k in range(1,4)]for r in range(1,4)])
assert Mi==Mj==Matrix([[1,1,1],[2,2,1],[1,2,3]])
assert Mi.det()==1
assert subst(b,i)==subst(b,j)==(2,)
assert subst(c,i)==subst(c,j)==(3,)
assert subst(t,i)==(1,3,2) and subst(t,j)==(1,2,3)
# The common recovered b,c give acb=Abc. Equal lengths force a=A,
# and cancellation then forces cb=bc, contradicting monoid injection.
assert red((3,2,-3,-2))!=( )
res={'first_images':i,'second_images':j,'both_bifix':True,
     'both_free_group_maps_are_isomorphisms':True,
     'inverse_identities_checked':checks,
     'identical_abelian_matrix':[[int(v) for v in Mi.row(r)] for r in range(3)],
     'determinant':int(Mi.det()),'positive_cones_identified':True,
     'recovered_source_words':{'t':t,'b':b,'c':c},
     'recovered_images_i':{'t':subst(t,i),'b':subst(b,i),'c':subst(c,i)},
     'recovered_images_j':{'t':subst(t,j),'b':subst(b,j),'c':subst(c,j)},
     'forced_equation':'acb=Abc with b=B,c=C',
     'length_then_prefix_consequence':'a=A, then cb=bc',
     'scope':'no injective amalgam in any locally free monoid, despite identical positive abelian cones'}
print(json.dumps(res,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
