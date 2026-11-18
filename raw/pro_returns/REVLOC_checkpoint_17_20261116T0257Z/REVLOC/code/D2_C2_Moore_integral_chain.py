#!/usr/bin/env python3
"""Integral chains of D2^(2) M(Z/2,2); no stable wedge splitting asserted."""
import json
from pathlib import Path
from sympy import Matrix
# Degree4: aa. Degree5: ab,ba,U=e1aa. Degree6: bb,H=e1ab,J=e1ba.
# Degree7: Z=e1bb. Tensor labels have |a|=2, |b|=3 and db=2a.
d5=Matrix([[2,2,0]])
d6=Matrix([[2,1,-1],[-2,-1,1],[0,-2,-2]])
d7=Matrix([[2],[-2],[2]])
assert d5*d6==Matrix.zeros(1,3) and d6*d7==Matrix.zeros(3,1)
# Integral changes of basis: (L=ab,W=dH,U) and (H,D=-H-J,V=bb-H+J).
B5=Matrix([[1,1,0],[0,-1,0],[0,-2,1]])
B6=Matrix([[0,0,1],[1,-1,-1],[0,-1,1]])
assert abs(B5.det())==abs(B6.det())==1
r5=d5*B5;r6=B5.inv()*d6*B6;r7=B6.inv()*d7
assert r5==Matrix([[2,0,0]])
assert r6==Matrix([[0,0,0],[1,0,0],[0,4,0]])
assert r7==Matrix([[0],[0],[2]])
# Exact identity behind the undecided Browder comparison.
H=Matrix([0,1,0]);J=Matrix([0,0,1]);bb=Matrix([1,0,0])
D=-H-J;V=bb-H+J
assert V==bb+D+2*J
out={"status":"PASS","source":"D2^(2) M(Z/2,2)",
     "differentials":{"d5":d5.tolist(),"d6":d6.tolist(),"d7":d7.tolist()},
     "unimodular_basis5":B5.tolist(),"unimodular_basis6":B6.tolist(),
     "reduced_differentials":{"d5":r5.tolist(),"d6":r6.tolist(),"d7":r7.tolist()},
     "integral_homology":{"H4":"Z/2","H5":"Z/4{U}","H6":"Z/2{V}"},
     "comparison":"V=bb+D+2J; dD=4U; dZ=2V",
     "scope":"Only integral chain reduction; stable eta attachments and the cover-map image remain uncomputed."}
dest=Path(__file__).resolve().parent/'outputs'/'D2_C2_Moore_integral_chain.json'
dest.write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
