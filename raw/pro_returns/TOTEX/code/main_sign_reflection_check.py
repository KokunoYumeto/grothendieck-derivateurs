#!/usr/bin/env python3
"""Exact checks for G(P)=Hom(P,Z)/sign and its animated reflection."""
from itertools import product
import json
import sympy as sp

I = sp.eye(2)
S = sp.Matrix([[0, 1], [1, 0]])
minus, norm = S - I, I + S
assert S * S == I
assert minus * norm == sp.zeros(2)
assert norm * minus == sp.zeros(2)
assert minus.nullspace() == [sp.Matrix([1, 1])]
assert norm.nullspace() == [sp.Matrix([-1, 1])]
# The primitive kernel generators are exactly image columns; this checks
# integral exactness, rather than only the equality of rational ranks.
assert norm[:, 0] == sp.Matrix([1, 1])
assert minus[:, 0] == sp.Matrix([-1, 1])
augment = sp.Matrix([[1, 1]])
assert augment * minus == sp.zeros(1, 2)
assert augment.nullspace() == [sp.Matrix([-1, 1])]

orbit_checks = []
for rank in range(5):
    vectors = list(product(range(-2, 3), repeat=rank))
    zero = (0,) * rank
    fixed = [v for v in vectors if v == tuple(-x for x in v)]
    assert fixed == [zero]
    reps = {min(v, tuple(-x for x in v)) for v in vectors}
    assert len(reps) == (len(vectors) + 1) // 2
    orbit_checks.append({
        "rank": rank, "sample_vectors": len(vectors),
        "sign_orbits": len(reps), "fixed_points": len(fixed)
    })

# The sign tensor has d_n = -2 for odd n and 0 for even n.
d = {n: (-2 if n % 2 else 0) for n in range(1, 13)}
assert all(d[n] * d[n + 1] == 0 for n in range(1, 12))
homology = {}
for n in range(11):
    dn, next_d = (0 if n == 0 else d[n]), d[n + 1]
    if dn != 0:
        result = "0"
        assert next_d == 0
    elif next_d == 0:
        result = "Z"
    else:
        result = f"Z/{abs(next_d)}"
    assert result == ("Z/2" if n % 2 == 0 else "0")
    homology[n] = result

print(json.dumps({
    "group": "C2",
    "resolution": "integrally exact 2-periodic resolution checked using primitive kernel/image generators",
    "action": "sign on Z",
    "orbit_checks": orbit_checks,
    "homology_degrees_0_through_10": homology,
    "uniform_proof": "H_0 and all positive even degrees are Z/2; all odd degrees vanish"
}, indent=2))
