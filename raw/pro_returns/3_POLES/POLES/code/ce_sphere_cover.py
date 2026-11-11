#!/usr/bin/env python3
"""Finite certificates for Claim C.3 (n = 0, 1, 2, 3).

P_n is the nonempty proper face poset of the (n+1)-simplex.
The two cones and their union are literal finite poset categories.
The script verifies the entire relation, all category laws, the covers,
and every functor in the two cubes. It computes integral boundaries,
checks d^2=0 over Z, and computes mod-2 Betti numbers by exact bit arithmetic.
It does not infer integral homotopy groups from mod-2 homology. The
identification as a simplex-boundary subdivision and its suspension,
verified combinatorially here, is the sphere proof in C.3.

No external packages are used. Run from any directory:
    python3 ce_sphere_cover.py
Output is deterministic JSON on stdout.
"""

from collections import defaultdict
from itertools import product
import json


class Poset:
    def __init__(self, name, objects, relation):
        self.name = name
        self.objects = tuple(objects)
        self.relation = frozenset(relation)
        self.arrows = tuple(sorted(self.relation))

    def leq(self, source, target):
        return (source, target) in self.relation

    def compose(self, after, before):
        assert before[1] == after[0]
        assert before in self.relation and after in self.relation
        result = (before[0], after[1])
        assert result in self.relation
        return result

    def category_certificate(self):
        for a in self.objects:
            assert self.leq(a, a)
        for a, b in self.arrows:
            assert a == b or not self.leq(b, a)
            assert self.compose((b, b), (a, b)) == (a, b)
            assert self.compose((a, b), (a, a)) == (a, b)
        composable_pairs = 0
        composable_triples = 0
        for a, b, c in product(self.objects, repeat=3):
            if self.leq(a, b) and self.leq(b, c):
                composable_pairs += 1
                assert self.compose((b, c), (a, b)) == (a, c)
                for d in self.objects:
                    if self.leq(c, d):
                        composable_triples += 1
                        left = self.compose((c, d), self.compose((b, c), (a, b)))
                        right = self.compose(self.compose((c, d), (b, c)), (a, b))
                        assert left == right == (a, d)
        return {
            "objects": len(self.objects),
            "arrows_including_identities": len(self.arrows),
            "composable_pairs_checked": composable_pairs,
            "composable_triples_checked": composable_triples,
            "identities_composition_associativity": True,
        }

    def chains(self):
        levels = [[(a,) for a in self.objects]]
        while levels[-1]:
            following = [c + (b,) for c in levels[-1] for b in self.objects
                         if c[-1] != b and self.leq(c[-1], b)]
            if not following:
                break
            levels.append(following)
        return levels


def rank_mod_two(columns):
    pivots = {}
    for column in columns:
        while column:
            pivot = column.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = column
                break
            column ^= pivots[pivot]
    return len(pivots)


def nerve_certificate(category):
    chains = category.chains()
    indices = [{simplex: i for i, simplex in enumerate(level)} for level in chains]
    boundaries = [[]]
    ranks = [0]
    for degree in range(1, len(chains)):
        columns = []
        bits = []
        for simplex in chains[degree]:
            column = {}
            bit_column = 0
            for i in range(degree + 1):
                face = simplex[:i] + simplex[i + 1:]
                index = indices[degree - 1][face]
                column[index] = (-1) ** i
                bit_column ^= 1 << index
            columns.append(column)
            bits.append(bit_column)
        boundaries.append(columns)
        ranks.append(rank_mod_two(bits))
    for degree in range(2, len(chains)):
        for column in boundaries[degree]:
            composite = defaultdict(int)
            for middle_index, coefficient in column.items():
                for bottom_index, bottom_coefficient in boundaries[degree - 1][middle_index].items():
                    composite[bottom_index] += coefficient * bottom_coefficient
            assert all(coefficient == 0 for coefficient in composite.values())
    ranks.append(0)
    betti = [len(level) - ranks[d] - ranks[d + 1] for d, level in enumerate(chains)]
    return {
        "nondegenerate_simplex_counts": [len(level) for level in chains],
        "boundary_squared_zero_over_integers": True,
        "mod_two_boundary_ranks": ranks[1:-1],
        "mod_two_betti_numbers": betti,
    }


def check_functor(source, target, object_map):
    assert set(object_map) == set(source.objects)
    assert all(b in target.objects for b in object_map.values())
    for a, b in source.arrows:
        assert target.leq(object_map[a], object_map[b])
    # In a thin category, object map and arrow preservation give identity
    # and composition preservation, since there is at most one arrow.
    return True


def check_sieve(ambient, subcategory):
    subset = set(subcategory.objects)
    assert subcategory.relation == frozenset((a, b) for a, b in ambient.arrows
                                            if a in subset and b in subset)
    assert all(a in subset for a, b in ambient.arrows if b in subset)
    return True


def check_cover(ambient, left, right, intersection):
    check_sieve(ambient, left)
    check_sieve(ambient, right)
    assert set(left.objects) | set(right.objects) == set(ambient.objects)
    assert set(left.objects) & set(right.objects) == set(intersection.objects)
    assert left.relation & right.relation == intersection.relation
    assert left.relation | right.relation == ambient.relation
    for level in ambient.chains():
        for simplex in level:
            assert all(a in left.objects for a in simplex) or all(a in right.objects for a in simplex)
    return True


def build(n):
    full = (1 << (n + 2)) - 1
    faces = tuple(range(1, full))
    plus, minus = full, full + 1

    def relation(objects):
        return [(a, b) for a, b in product(objects, repeat=2)
                if a == b or (a in faces and (b in (plus, minus) or (a & b) == a))]

    p = Poset("P", faces, relation(faces))
    cp = Poset("C_plus", faces + (plus,), relation(faces + (plus,)))
    cm = Poset("C_minus", faces + (minus,), relation(faces + (minus,)))
    s = Poset("S", faces + (plus, minus), relation(faces + (plus, minus)))
    point = Poset("point", (0,), [(0, 0)])

    # Explicit certificate that P is exactly the proper nonempty face poset.
    assert set(faces) == set(range(1, (1 << (n + 2)) - 1))
    assert all(p.leq(a, b) == ((a & b) == a) for a, b in product(faces, repeat=2))
    assert all(cp.leq(a, plus) for a in cp.objects)
    assert all(cm.leq(a, minus) for a in cm.objects)
    assert not s.leq(plus, minus) and not s.leq(minus, plus)
    check_cover(s, cp, cm, p)
    check_cover(cm, p, cm, p)
    check_cover(point, point, point, point)

    # The four vertical maps for clause 6b; all horizontals are inclusions.
    for category in (p, cp, cm, s):
        check_functor(category, point, {a: 0 for a in category.objects})
    # The four vertical maps for clause 6c and every horizontal arrow.
    for source, target in ((p, p), (p, cp), (cm, cm), (cm, s),
                           (p, cm), (p, s), (cp, s)):
        check_functor(source, target, {a: a for a in source.objects})
    # All cube equalities are literal equalities on objects and arrows:
    # the 6b maps are constant, and every 6c map is an inclusion.

    categories = {}
    for category in (p, cp, cm, s):
        categories[category.name] = {
            **category.category_certificate(),
            **nerve_certificate(category),
        }
    expected_p = [0] * (n + 1)
    expected_p[0] = 1
    expected_p[n] += 1
    expected_s = [1] + [0] * n + [1]
    assert categories["P"]["mod_two_betti_numbers"] == expected_p
    assert categories["S"]["mod_two_betti_numbers"] == expected_s
    for name in ("C_plus", "C_minus"):
        assert categories[name]["mod_two_betti_numbers"] == [1] + [0] * (n + 1)
    return {
        "n": n,
        "face_vertex_set": list(range(n + 2)),
        "face_objects_encoded_by_nonempty_proper_bitmasks": list(faces),
        "added_cone_object_codes": {"plus": plus, "minus": minus},
        "exact_simplex_boundary_face_poset": True,
        "two_terminal_cones_and_unreduced_suspension_verified": True,
        "all_full_sieve_and_cover_conditions": True,
        "all_cube_functors_and_commutative_faces": True,
        "categories": categories,
        "clause_6b_vertical_Wn_membership": [False, True, True, True],
        "clause_6c_vertical_Wn_membership": [True, False, True, True],
        "homotopy_membership_justification":
            "Exact face-poset and suspension identification, with terminal cone objects, as proved in C.3; mod-2 homology is an independent check.",
    }


if __name__ == "__main__":
    print(json.dumps({"claim": "C.3", "all_assertions_passed": True,
                      "instances": [build(n) for n in range(4)]}, indent=2))
