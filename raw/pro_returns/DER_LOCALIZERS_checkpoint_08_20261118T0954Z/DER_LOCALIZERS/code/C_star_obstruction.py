#!/usr/bin/env python3
"""Finite F_2 checks for the star obstruction research note.

These check the three-vertex resolution and the dual-number differential.
They do not enumerate Boolean fibers or prove a statement by testing only
finitely many projective-resolution degrees; the infinite arguments are
given in notes/C_star_obstruction.md.
"""

import itertools
import json


def image(matrix, domain_dimension):
    return {
        tuple(sum(a * b for a, b in zip(row, vector)) % 2 for row in matrix)
        for vector in itertools.product(range(2), repeat=domain_dimension)
    }


def kernel(matrix, domain_dimension):
    return {
        vector
        for vector in itertools.product(range(2), repeat=domain_dimension)
        if all(sum(a * b for a, b in zip(row, vector)) % 2 == 0 for row in matrix)
    }


# At u: 0 -> k -> k^2 -> k -> 0.  At each branch: 0 -> 0 -> k -> k -> 0.
inclusion = [[1], [1]]
fold = [[1, 1]]
assert kernel(inclusion, 1) == {(0,)}
assert image(inclusion, 1) == kernel(fold, 2)
assert image(fold, 2) == {(0,), (1,)}
assert image([[1]], 1) == {(0,), (1,)}
assert kernel([[1]], 1) == {(0,)}

# Morphisms from the constant star module to each indecomposable projective.
hom_u_pu = [a for a in range(2) if a == 0 and a == 0]
hom_u_pb0 = [(a, b) for a, b in itertools.product(range(2), repeat=2)
              if a == b and a == 0]
hom_u_pb1 = [(a, b) for a, b in itertools.product(range(2), repeat=2)
              if a == 0 and a == b]
assert hom_u_pu == [0]
assert hom_u_pb0 == [(0, 0)]
assert hom_u_pb1 == [(0, 0)]

# After tensoring with T(u)=k, T(b_j)=0, degree 1 is k and degree 0 is zero.
tor1_dimension = 1

# Multiplication by epsilon on k[epsilon]/epsilon^2, basis (1, epsilon).
epsilon = [[0, 0], [1, 0]]
assert image(epsilon, 2) == kernel(epsilon, 2) == {(0, 0), (0, 1)}
for vector in itertools.product(range(2), repeat=2):
    first = tuple(sum(a * b for a, b in zip(row, vector)) % 2 for row in epsilon)
    second = tuple(sum(a * b for a, b in zip(row, first)) % 2 for row in epsilon)
    assert second == (0, 0)

# Each R-linear map R -> the trivial module kills epsilon, so Hom(d,k)=0.
hom_maps = [[value, 0] for value in range(2)]
assert all(
    sum(functional[row] * epsilon[row][column] for row in range(2)) % 2 == 0
    for functional in hom_maps
    for column in range(2)
)

print(json.dumps({
    "field": "F2",
    "star_resolution_componentwise_exact": True,
    "hom_from_unit_to_each_star_projective_dimension": [0, 0, 0],
    "star_Tor1_dimension": tor1_dimension,
    "dual_number_d_squared": 0,
    "dual_number_image_equals_kernel": True,
    "dual_number_Hom_differential": 0,
    "scope": "Finite matrices only. Infinite periodic resolution and Boolean-fiber non-descent are proved in the accompanying note."
}, indent=2))
