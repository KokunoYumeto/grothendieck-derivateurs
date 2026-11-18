"""Exact Fox-chain check for the trefoil obstruction, over Z and every field."""
from pathlib import Path
import json
import sympy as s

t = s.Symbol("t")
word = [(0,1),(1,1),(0,1),(1,-1),(0,-1),(1,-1)]
prefix = s.Integer(1)
derivatives = [s.Integer(0), s.Integer(0)]
for gen, sign in word:
    if sign == 1:
        derivatives[gen] += prefix
        prefix *= t
    else:
        prefix /= t
        derivatives[gen] -= prefix
derivatives = [s.expand(x) for x in derivatives]
polynomial = t*t-t+1
assert prefix == 1
assert derivatives == [polynomial, -polynomial]
assert s.expand((t-1)*sum(derivatives)) == 0
ordinary_boundary = [int(x.subs(t,1)) for x in derivatives]
assert ordinary_boundary == [1,-1]
assert s.Poly(polynomial,t).LC() == 1
assert polynomial.subs(t,0) == 1
report = {
    "relator":"x y x y^-1 x^-1 y^-1",
    "images":{"x":"t","y":"t"},
    "cyclic_cover_d1":["t-1","t-1"],
    "cyclic_cover_d2":[str(x) for x in derivatives],
    "ordinary_d2":ordinary_boundary,
    "ordinary_integral_homology":{"H0":"Z","H1":"Z","Hn_n_ge_2":"0"},
    "kernel_d1_basis":[1,-1],
    "Alexander_module":"Z[t,t^-1]/(t^2-t+1)",
    "all_fields_check":"Degree 2 and nonzero constant term survive in every characteristic; hence nonunit in every k[t,t^-1].",
    "checks_passed":True
}
out = Path(__file__).parent/"outputs"/"EH5_trefoil.json"
out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
