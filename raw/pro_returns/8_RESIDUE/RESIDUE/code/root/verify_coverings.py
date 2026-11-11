"""Exact finite chain checks supporting D.12; not a universal search."""
from pathlib import Path
import json
import math
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def cyclic_permutation(d):
    p = sp.zeros(d)
    for i in range(d):
        p[(i + 1) % d, i] = 1
    return p


def main():
    rows = []
    for d in range(1, 13):
        differential = 2 * cyclic_permutation(d) - sp.eye(d)
        diagonal = smith_normal_form(differential, domain=sp.ZZ)
        invariants = [abs(int(diagonal[i, i])) for i in range(d)]
        assert invariants == [1] * (d - 1) + [2**d - 1]
        assert abs(int(differential.det())) == 2**d - 1
        assert all(sum(differential[i, j] for i in range(d)) == 1
                   for j in range(d))
        rows.append({"orbit_length": d, "integral_differential":
                     [list(map(int, differential.row(i))) for i in range(d)],
                     "smith_diagonal": invariants,
                     "cokernel": "0" if d == 1 else f"Z/{2**d - 1}",
                     "degree_d_pullback_orbits": math.gcd(d, d)})
    result = {"status": "PASS", "scope": "Finite cycles of lengths 1 through 12; exact integer matrices",
              "rows": rows, "infinite_cycle":
              "Handled algebraically in D.12: Z[t,t^-1]/(2t-1) = Z[1/2]."}
    Path(__file__).with_name("coverings_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "cycle_lengths": [1, 12],
                      "determinants": [2**d - 1 for d in range(1, 13)]}, indent=2))


if __name__ == "__main__":
    main()
