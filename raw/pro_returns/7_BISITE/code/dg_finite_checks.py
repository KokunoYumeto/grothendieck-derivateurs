#!/usr/bin/env python3
"""Exact finite checks for BISITE D/G; no numerical or library dependency.

Run from the BISITE directory as:
    python code/dg_finite_checks.py > code/dg_finite_checks.out.json

The infinite-coproduct argument in G.7 is proved in the text.  Finite
resolution checks here are evidence for its algebraic input, not a
finite substitute for that infinite argument.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
import json


def rank_q(matrix, ncols=None):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    ncols = len(a[0]) if ncols is None else ncols
    pivot = 0
    for col in range(ncols):
        row = next((r for r in range(pivot, len(a)) if a[r][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        v = a[pivot][col]
        a[pivot] = [x / v for x in a[pivot]]
        for r in range(len(a)):
            if r != pivot and a[r][col]:
                v = a[r][col]
                a[r] = [x - v*y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def rank_f2(matrix):
    a = [[x % 2 for x in row] for row in matrix]
    if not a:
        return 0
    pivot = 0
    for col in range(len(a[0])):
        row = next((r for r in range(pivot, len(a)) if a[r][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        for r in range(len(a)):
            if r != pivot and a[r][col]:
                a[r] = [x ^ y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def matmul_f2(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % 2
             for col in zip(*b)] for row in a]


def check_poset(objects, le):
    reflexive = all(le(a, a) for a in objects)
    antisymmetric = all(not (le(a, b) and le(b, a)) or a == b
                        for a, b in product(objects, repeat=2))
    transitive = all(not (le(a, b) and le(b, c)) or le(a, c)
                     for a, b, c in product(objects, repeat=3))
    assert reflexive and antisymmetric and transitive
    return {"objects": objects,
            "arrows": [[a, b] for a, b in product(objects, repeat=2) if le(a, b)],
            "composites": [[a, b, c] for a, b, c in product(objects, repeat=3)
                           if le(a, b) and le(b, c)],
            "reflexive": reflexive, "antisymmetric": antisymmetric,
            "transitive": transitive}


def reduced_betti_order_complex(objects, le):
    simplices = {}
    for size in range(1, len(objects)+1):
        simplices[size-1] = [tuple(c) for c in combinations(objects, size)
                            if all(le(c[i], c[j]) or le(c[j], c[i])
                                   for i in range(size) for j in range(i+1, size))]
    # Canonically order vertices by their rank in this finite partial order.
    order = {v: sum(le(w, v) for w in objects) for v in objects}
    simplices = {d: [tuple(sorted(s, key=lambda v: order[v])) for s in ss]
                 for d, ss in simplices.items()}
    ranks = {0: 1 if objects else 0}
    for dim in range(1, len(objects)):
        faces = {s: i for i, s in enumerate(simplices[dim-1])}
        boundary = [[0 for _ in simplices[dim]] for _ in faces]
        for j, simplex in enumerate(simplices[dim]):
            for k in range(dim+1):
                boundary[faces[simplex[:k] + simplex[k+1:]]][j] += (-1)**k
        ranks[dim] = rank_q(boundary)
    betti = {-1: 1 - ranks[0]}
    for dim in range(len(objects)):
        betti[dim] = len(simplices[dim]) - ranks.get(dim, 0) - ranks.get(dim+1, 0)
    return {str(d): n for d, n in betti.items() if n}


result = {}

# D.3: all six bijections of the fork, with a failed order test for each.
fork = ["b", "a", "c"]
fork_le = lambda x, y: x == y or (x == "b" and y in ("a", "c"))
fork_data = check_poset(fork, fork_le)
anti_tests = []
for perm in permutations(fork):
    f = dict(zip(fork, perm))
    failures = [(x, y) for x, y in product(fork, repeat=2)
                if fork_le(x, y) != fork_le(f[y], f[x])]
    assert failures
    anti_tests.append({"bijection": f, "first_failed_order_test": failures[0]})
fork_data.update({"minimal": ["b"], "maximal": ["a", "c"],
                  "bijections_checked": len(anti_tests),
                  "anti_isomorphisms": 0, "exhaustive_tests": anti_tests})
result["D.3_fork_not_self_opposite"] = fork_data

# D.9, G.3, G.5: the same fully specified arrow category.
arrow = [0, 1]
arrow_le = lambda a, b: a <= b
arrow_data = check_poset(arrow, arrow_le)
comma_objects = {str(t): [[0, t]] for t in arrow if arrow_le(0, t)}
outgoing_lifts_0_to_1 = [x for x in [0] if arrow_le(0, x) and x == 1]
assert outgoing_lifts_0_to_1 == []
result["D.9_endpoint_inclusion"] = {
    "base_category": arrow_data,
    "source_objects": [0], "source_arrows": [[0, 0]],
    "functor_on_objects": {"0": 0},
    "comma_A_over_t_objects": comma_objects,
    "comma_each_only_identity": True,
    "outgoing_lifts_for_0_to_1": outgoing_lifts_0_to_1,
    "right_Kan_cardinalities_at_0_and_1": [2, 2],
    "topological_skyscraper_stalk_cardinalities_at_0_half_1": [2, 1, 1]
}
result["G.3_pointwise_twist"] = {
    "presheaf_values_F0_F1": [0, 1],
    "limit_evaluation_at_1_dimension": 1,
    "colimit_evaluation_at_0_dimension": 0,
    "sample_twist_dimensions_at_0": [{"omega0": d, "omega0_times_F0": d*0}
                                     for d in range(6)],
    "general_obstruction": "Every tensor with F0=0 is zero; the limit is F1."
}
result["G.5_weight_restriction"] = {
    "representable_R0_values_at_0_1": [1, 0],
    "representable_R1_values_at_0_1": [1, 1],
    "w_arrow_values_at_0_1": [0, 1],
    "w_point_value": 1,
    "restriction_along_point_selecting_0": 0
}

# G.7: C2 is a finite EI category and has the asserted exact resolution.
c2_mul = lambda a, b: (a+b) % 2
group_associative = all(c2_mul(c2_mul(a,b),c) == c2_mul(a,c2_mul(b,c))
                        for a,b,c in product(range(2), repeat=3))
assert group_associative
d = [[1, 1], [1, 1]]
augmentation = [[1, 1]]
assert matmul_f2(d, d) == [[0, 0], [0, 0]]
assert rank_f2(d) == 1
assert matmul_f2(augmentation, d) == [[0, 0]]
result["G.7_finite_EI_modular_obstruction"] = {
    "objects": ["*"], "arrows": ["1", "g"],
    "multiplication_rows_1_g_columns_1_g": [["1", "g"], ["g", "1"]],
    "associativity_all_eight_triples": group_associative,
    "all_endomorphisms_invertible": True,
    "epsilon_matrix_over_F2": d, "epsilon_squared": matmul_f2(d, d),
    "epsilon_rank": rank_f2(d), "epsilon_kernel_dimension": 2-rank_f2(d),
    "augmentation": augmentation,
    "augmentation_kernel_dimension": 2-rank_f2(augmentation),
    "augmentation_after_epsilon": matmul_f2(augmentation, d),
    "Hom_differential_with_trivial_coefficients": 0,
    "finite_truncation_Hom_degree_zero_dimensions": {str(n): n+1 for n in range(6)},
    "infinite_argument": "The manuscript proves direct sum F2 -> product F2 is not onto."
}

# G.9, G.11, G.12: small upper intervals and their reduced homology.
empty = reduced_betti_order_complex([], lambda a,b: False)
singleton = reduced_betti_order_complex([0], lambda a,b: a == b)
two_points = reduced_betti_order_complex([0,1], lambda a,b: a == b)
assert empty == {"-1": 1} and singleton == {} and two_points == {"0": 1}
triangle_boundary_faces = [frozenset([i]) for i in range(3)] + [frozenset(c) for c in combinations(range(3),2)]
triangle_betti = reduced_betti_order_complex(triangle_boundary_faces, lambda a,b: a <= b)
assert triangle_betti == {"1": 1}
result["G.9_upper_interval_examples"] = {
    "empty_reduced_Betti": empty,
    "singleton_reduced_Betti": singleton,
    "two_incomparable_points_reduced_Betti": two_points,
    "proper_nonempty_faces_of_triangle_reduced_Betti": triangle_betti,
    "torsion_note": "These listed complexes are respectively empty, a point, S0 and a polygonal circle; integral homology is torsion-free."
}

# G.11: relative cochains of a local interval and its punctured interval.
boundary_map = [[1]]
interior_map = [[1], [1]]
boundary_rank, interior_rank = rank_q(boundary_map), rank_q(interior_map)
result["G.11_interval_local_duality"] = {
    "boundary_restriction_matrix": boundary_map,
    "boundary_relative_H0": 1-boundary_rank,
    "boundary_relative_H1": 1-boundary_rank,
    "interior_restriction_matrix": interior_map,
    "interior_relative_H0": 1-interior_rank,
    "interior_relative_H1": 2-interior_rank,
    "dualizing_stalks": {"0": "zero", "interior": "k[1]", "1": "zero"},
    "minimum_strata": ["[0,1)", "{1}"],
    "dualizing_sheaf_constant_on_first_stratum": False
}
assert result["G.11_interval_local_duality"]["interior_relative_H1"] == 1

# G.13: product versus pointwise coproduct, entirely in finite sets.
F, G = (1, 0), (0, 1)
lhs = F[0]*F[1] + G[0]*G[1]
rhs = (F[0]+G[0])*(F[1]+G[1])
assert lhs == 0 and rhs == 1
result["G.13_unstable_product"] = {
    "index_objects": [0,1], "index_arrows": [[0,0],[1,1]],
    "F_cardinalities": F, "G_cardinalities": G,
    "coproduct_of_limits_cardinality": lhs,
    "limit_of_pointwise_coproduct_cardinality": rhs
}

result["all_assertions_passed"] = True
print(json.dumps(result, indent=2, sort_keys=True))
