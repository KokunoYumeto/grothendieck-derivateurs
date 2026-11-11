#!/usr/bin/env python3
"""Exact finite checks used in CATHOT Parts B--C.

These checks do not replace the infinite group and infinite fence proofs.
No external package is needed. Output is deterministic.
"""
from fractions import Fraction
from collections import deque
import json


def perm_cycle(n, cycle):
    p = list(range(n))
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        p[a] = b
    return tuple(p)


def pmul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def pinv(p):
    q = [0] * len(p)
    for a, b in enumerate(p):
        q[b] = a
    return tuple(q)


def clifford_mul(x, y):
    """Clifford algebra Cl_{4,0}(Q), bit mask basis, e_i^2=1."""
    out = {}
    for a, x_a in x.items():
        for b, y_b in y.items():
            swaps = sum((b & ((1 << i) - 1)).bit_count()
                        for i in range(4) if a & (1 << i))
            key = a ^ b
            out[key] = out.get(key, 0) + (-1) ** swaps * x_a * y_b
    return {k: v for k, v in out.items() if v}


def scaled(x, q):
    return {k: q * v for k, v in x.items()}


def reflection_vector(i, j):
    return {1 << i: Fraction(1), 1 << j: Fraction(-1)}


def free_reduce(word, modulus):
    """Normal form in C_modulus * Z: (0,k) in C_m, (1,k) in Z."""
    out = []
    for factor, exponent in word:
        if factor == 0:
            exponent %= modulus
        if not exponent:
            continue
        if out and out[-1][0] == factor:
            exponent += out.pop()[1]
            if factor == 0:
                exponent %= modulus
        if exponent:
            out.append((factor, exponent))
    return out


def cyclic_reduce(word, modulus):
    out = free_reduce(word, modulus)
    while len(out) > 1 and out[0][0] == out[-1][0]:
        a = out.pop(0)
        out = free_reduce(out + [a], modulus)
    return out


def run():
    records = {}
    # The fresh-point commutator is a 3-cycle even if g moves other points.
    g = pmul(perm_cycle(8, [0, 1, 4]), perm_cycle(8, [5, 6, 7]))
    tau = perm_cycle(8, [0, 2, 3])
    commutator = pmul(pmul(pmul(g, tau), pinv(g)), pinv(tau))
    assert commutator == perm_cycle(8, [0, 1, 2])
    records['fresh_point_commutator'] = {'verified': True,
                                       'result_cycle': [0, 1, 2]}

    a = scaled(clifford_mul(reflection_vector(0, 1),
                            reflection_vector(2, 3)), Fraction(1, 2))
    b = scaled(clifford_mul(reflection_vector(0, 2),
                            reflection_vector(1, 3)), Fraction(1, 2))
    assert clifford_mul(a, a) == {0: Fraction(-1)}
    assert clifford_mul(b, b) == {0: Fraction(-1)}
    assert clifford_mul(a, b) == scaled(clifford_mul(b, a), -1)
    records['spin_lifts_of_klein_four_generators'] = {
        'a_squared': '-1', 'b_squared': '-1', 'ab_equals_minus_ba': True}

    tested = 0
    minimum_length = None
    for m in range(2, 17):
        for g in range(1, m):
            w = [(0, g), (1, 1), (0, -g), (1, -1),
                 (0, g), (1, 2), (0, -g), (1, -2)]
            assert len(cyclic_reduce(w, m)) > 1
            for h in range(m):
                v = cyclic_reduce(w + [(0, h)], m)
                assert len(v) > 1
                minimum_length = min(minimum_length or len(v), len(v))
                tested += 1
    records['simple_envelope_word_checks'] = {
        'base_groups': 'C_m for 2 <= m <= 16',
        'all_nonidentity_g_and_all_h': tested,
        'minimum_cyclically_reduced_length_of_wh': minimum_length}

    fence_records = []
    for maximum in [2, 4, 8, 16, 32, 64]:
        vertices = range(maximum + 1)
        arrows = {(v, v) for v in vertices}
        arrows |= {(v, u) for v in vertices if v % 2 == 0
                   for u in (v - 1, v + 1) if 0 <= u <= maximum}
        # Transitivity verifies that this is the arrow set of a poset category.
        for x, y in arrows:
            for yy, z in arrows:
                if y == yy:
                    assert (x, z) in arrows
        adjacency = {v: set() for v in vertices}
        for x, y in arrows:
            if x != y:
                adjacency[x].add(y)
                adjacency[y].add(x)
        distance = {0: 0}
        queue = deque([0])
        while queue:
            v = queue.popleft()
            for u in adjacency[v]:
                if u not in distance:
                    distance[u] = distance[v] + 1
                    queue.append(u)
        assert distance[maximum] == maximum
        assert len(distance) == maximum + 1
        nonidentity = len(arrows) - (maximum + 1)
        assert nonidentity == maximum
        fence_records.append({'objects': maximum + 1,
                              'arrows_including_identities': len(arrows),
                              'distance_0_to_maximum': distance[maximum],
                              'nerve_euler_characteristic': 1,
                              'nondegenerate_simplices_above_dimension_1': 0})
    records['finite_fence_truncations'] = fence_records
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    run()
