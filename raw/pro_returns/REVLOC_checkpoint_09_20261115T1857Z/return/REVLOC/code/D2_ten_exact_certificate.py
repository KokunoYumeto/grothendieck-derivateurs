#!/usr/bin/env python3
"""Exact finite algebra used in D.2.22--D.2.24.

Checks the integral quadratic-chain Smith form, both mixed-label
Bockstein representatives, the complete eighteen-row primary relation,
and all four parameter values in the final group presentation. This
does not certify the geometric input, source completeness, or the
identification of a homotopy attaching map from its detectors; those
are proved in the manuscript and reviewed separately.
"""
from itertools import product
from pathlib import Path
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
import D2_fiber_poly_check as poly


def smith(matrix):
    s = smith_normal_form(Matrix(matrix), domain=ZZ)
    return [abs(int(s[i, i])) for i in range(min(s.shape))]


# Degree-nine cycles are v,z. Degree-ten generators are q,h,h'.
boundary = Matrix([[4, -1, 1], [0, -4, -4]])
assert smith(boundary) == [1, 8]
assert boundary * Matrix([-2, -4, 4]) == Matrix([0, 0])
assert boundary * Matrix([0, 1, 1]) == Matrix([0, -8])

# Sq2 and Sq4 entries in the complete H10(F) basis. A set is a
# mod-two sum; these are the independently audited CLM table entries.
table = {
    'DA': ({'W'}, set()), 'EA': ({'W'}, set()),
    'FA': ({'W'}, set()), 'Z2': ({'W'}, set()),
    'ZU': (set(), set()), 'U2': (set(), set()),
    'D2': (set(), {'d6'}),
    'Q10': ({'M', 'C', 'W'}, {'f6'}),
    'Pp': ({'W'}, {'f6'}), 'Pr': (set(), set()),
    'B1': ({'J2'}, set()), 'B2': ({'J2'}, set()),
    'B3': (set(), set()),
    'B4': ({'J1', 'J2', 'J3'}, {'d6', 'e6'}),
    'B5': ({'J1', 'J3'}, {'d6', 'e6'}),
    'B6': ({'J2'}, set()), 'B7': (set(), set()),
    'B8': (set(), set()),
}
assert len(table) == 18
psi = {name: int('J1' in q2) ^ int('e6' in q4)
       for name, (q2, q4) in table.items()}
assert not any(psi.values())
assert [name for name, (q2, _) in table.items() if 'J1' in q2] == ['B4', 'B5']

# Independent source Cartan calculation, not merely a stored table.
w, uv, u2v, uw, t = ((0, 0, 1, 0), (1, 1, 0, 0),
                    (2, 1, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1))
assert poly.csq(4, w) == {t}
assert t not in poly.csq(4, uv)
assert t not in poly.csq(2, u2v)
assert t not in poly.csq(2, uw)

# Final generators p,x,y,s. Normal forms have all four coefficients
# in {0,1}; wrapping x or y contributes a*p or b*p, respectively.
normal_forms = list(product(range(2), repeat=4))
cases = []
for a, b in product(range(2), repeat=2):
    relations = [[2, 0, 0, 0], [-a, 2, 0, 0],
                 [-b, 0, 2, 0], [0, 0, 0, 2]]
    invariants = [d for d in smith(relations) if d != 1]
    assert invariants == ([2, 2, 2, 2] if a == b == 0 else [2, 2, 4])

    def add(g, h):
        p, x, y, s = (g[i] + h[i] for i in range(4))
        return ((p + a * (x // 2) + b * (y // 2)) % 2,
                x % 2, y % 2, s % 2)

    def hur(g):
        p, x, y, s = g
        return ((4 * p - 2 * a * x - 2 * b * y) % 8, x, y)

    zero = (0, 0, 0, 0)
    for g, h in product(normal_forms, repeat=2):
        expected = ((hur(g)[0] + hur(h)[0]) % 8,
                    hur(g)[1] ^ hur(h)[1], hur(g)[2] ^ hur(h)[2])
        assert hur(add(g, h)) == expected
    assert all(add(add(g, g), add(g, g)) == zero for g in normal_forms)
    kernel = [g for g in normal_forms if hur(g) == (0, 0, 0)]
    assert kernel == [(0, 0, 0, 0), (0, 0, 0, 1)]
    assert len({hur(g) for g in normal_forms}) == 8
    # An order-at-most-two spherical class reducing to K1+K5 exists
    # precisely when the two retained even-nu bits agree.
    order_two_lifts = [g for g in normal_forms
                       if g[1:3] == (1, 1) and add(g, g) == zero]
    assert bool(order_two_lifts) == (a == b)
    cases.append({'a': a, 'b': b, 'invariant_factors': invariants,
                  'group_order': 16, 'hurewicz_image_order': 8,
                  'hurewicz_kernel': kernel,
                  'order_two_K1_plus_K5_lifts': order_two_lifts})

result = {
    'status': 'PASS',
    'quadratic_chain_boundary': boundary.tolist(),
    'quadratic_smith_invariants': [1, 8],
    'mixed_label_sum_boundary': [0, -8],
    'Psi_all_18_evaluations': psi,
    'unit_source_Cartan_tests': 4,
    'parameter_cases': cases,
    'scope': __doc__.strip(),
}
dest = Path(__file__).parent / 'outputs' / 'D2_ten_exact_certificate.json'
dest.write_text(json.dumps(result, indent=2, default=int) + '\n')
print(json.dumps({'status': 'PASS', 'table_rows': 18, 'parameter_cases': 4,
                  'exact_group_addition_checks': 1024, 'output': str(dest)}))
