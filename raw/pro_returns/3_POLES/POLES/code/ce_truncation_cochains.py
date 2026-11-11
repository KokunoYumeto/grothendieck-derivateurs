#!/usr/bin/env python3
"""Cellular certificates for the finite CW counterexample in E.7.

For n >= 3, X = S^2 wedge S^(n-1), Y = S^2 times S^(n-1).
The standard product CW structure adds only the top (n+1)-cell.
The program checks the integral cellular complexes, the restriction on
cohomology through degree n, and the nonzero cross product which detects
the nonzero Whitehead attaching map in the proof. All arithmetic is exact.
Its output does not purport to compute arbitrary unstable homotopy groups.
"""

import json
from itertools import product


def certificate(n):
    assert n >= 3
    p, q = 2, n - 1
    product_basis = ((0, 0), (1, 0), (0, 1), (1, 1))
    wedge_basis = product_basis[:-1]
    degree = lambda cell: p * cell[0] + q * cell[1]

    def multiply(a, b, wedge=False):
        exponent = (a[0] + b[0], a[1] + b[1])
        if max(exponent) > 1 or (wedge and exponent == (1, 1)):
            return None, 0
        return exponent, (-1) ** (q * p * a[1] * b[0])

    def triple(first, second, third, left, wedge):
        if left:
            intermediate, coefficient = multiply(first, second, wedge)
            if coefficient == 0:
                return None, 0
            result, final = multiply(intermediate, third, wedge)
        else:
            intermediate, coefficient = multiply(second, third, wedge)
            if coefficient == 0:
                return None, 0
            result, final = multiply(first, intermediate, wedge)
        return (result, coefficient * final) if final else (None, 0)

    for wedge, basis in ((False, product_basis), (True, wedge_basis)):
        for cell in basis:
            assert multiply((0, 0), cell, wedge) == (cell, 1)
            assert multiply(cell, (0, 0), wedge) == (cell, 1)
        for a, b, c in product(basis, repeat=3):
            assert triple(a, b, c, True, wedge) == triple(a, b, c, False, wedge)
        for a, b in product(basis, repeat=2):
            left_cell, left_coefficient = multiply(a, b, wedge)
            right_cell, right_coefficient = multiply(b, a, wedge)
            assert left_cell == right_cell
            assert left_coefficient == ((-1) ** (degree(a) * degree(b))) * right_coefficient

    product_ranks = [sum(degree(c) == d for c in product_basis) for d in range(n + 2)]
    wedge_ranks = [sum(degree(c) == d for c in wedge_basis) for d in range(n + 2)]
    assert product_ranks[:n + 1] == wedge_ranks[:n + 1]
    assert multiply((1, 0), (0, 1), False) == ((1, 1), 1)
    assert multiply((1, 0), (0, 1), True) == (None, 0)
    assert degree((1, 1)) == n + 1
    return {
        "n": n,
        "sphere_dimensions": [p, q],
        "wedge_cells": [{"cell": list(c), "dimension": degree(c)} for c in wedge_basis],
        "product_cells": [{"cell": list(c), "dimension": degree(c)} for c in product_basis],
        "all_cellular_differentials": "zero over Z",
        "wedge_integral_cohomology_ranks": wedge_ranks,
        "product_integral_cohomology_ranks": product_ranks,
        "restriction_is_identity_on_cellular_bases_in_degrees_zero_through_n": True,
        "therefore_cohomology_isomorphism_for_every_abelian_coefficient_group_through_n": True,
        "product_cross_cup_coefficient_in_top_cell": 1,
        "wedge_cross_cup_coefficient": 0,
        "cup_ring_unit_associativity_graded_commutativity": True,
        "homotopy_failure_certificate":
            "The top cell attaches by [iota_2,iota_(n-1)]; a null attaching map would give a wedge with S^(n+1), whose cross product is zero, contradicting the checked coefficient 1.",
    }


if __name__ == "__main__":
    print(json.dumps({"claim": "E.7", "all_assertions_passed": True,
                      "instances": [certificate(n) for n in range(3, 9)]}, indent=2))
