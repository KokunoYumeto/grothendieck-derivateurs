#!/usr/bin/env python3
"""Integral binary relative chains in degrees8--10.

This certifies the finite chain algebra and the coefficient four in
the cochain obstruction. The topological relative-cell comparison,
Whitehead normalization and scope of the choices require the separate
mathematical audit in root_D2_canonical_ten_lead.md.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Degree9 basis r=e3aa,t=e2ab,t'=e2ba.
d9=s.Matrix([[-2,-2,2]])
# Degree10 basis e4aa,e3ab,e3ba,e2bb,e2ac,e2ca.
d10=s.Matrix([[0,2,-2,0,0,0],
              [0,-1,1,2,0,0],
              [0,1,-1,2,0,0]])
assert d9*d10==s.zeros(1,6)
# Full integral kernel basis w=t-r,w'=t'+r. Any kernel vector has
# r=-t+t', proving saturation without relying on rational nullspace.
K=s.Matrix([[-1,1],[1,0],[0,1]])
bound=s.Matrix([[0,-1,1,2,0,0],[0,1,-1,2,0,0]])
assert K*bound==d10
snf=smith_normal_form(bound,domain=ZZ)
invariants=[abs(int(snf[i,i])) for i in range(2)]
assert invariants==[1,4]
R,T,U=s.symbols('R T U')
ds=2*R-T+U
dv=2*T+2*U
assert s.expand(dv-2*ds)==4*(T-R)
assert s.expand(ds.subs(U,T-2*R))==0
assert s.expand(dv.subs(U,T-2*R))==4*(T-R)
out={
 'status':'PASS','d9':d9.tolist(),'d10':d10.tolist(),
 'kernel_basis':K.tolist(),'boundaries_in_kernel':bound.tolist(),
 'H8':'Z/2','H9':'Z/4','smith_nonzero_entries':invariants,
 'cochain_identity':'dv-2ds=4(T-R)',
 'scope':'Finite integral chain algebra only; no full-source extension or nullification claim.'}
out={k:([[int(t) for t in row] for row in v] if k in
 ('d9','d10','kernel_basis','boundaries_in_kernel') else v)
 for k,v in out.items()}
dest=Path(__file__).parent/'outputs'/'D2_canonical_relative_chain.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','H9':'Z/4','obstruction_modulus':4,
                  'output':str(dest)}))
