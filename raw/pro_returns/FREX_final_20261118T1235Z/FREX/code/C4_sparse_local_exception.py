#!/usr/bin/env python3
"""A finite-target F2/Q affine-equalizer separation inside ordered C_delta.

This certifies only the displayed target.  A later target could have a
rational equalizer, so it is not a global familywise separation theorem.
All predimension minima are checked by exact private-vertex elimination.
"""
import itertools
import json
from pathlib import Path

from sympy import Matrix


def main():
    labels = ['B', 'A', 'C', 'E', 'z', 'D', 'F', 'J', 'H', 'I']
    triples = [('z', 'D', 'H'), ('A', 'z', 'I'), ('B', 'E', 'z'),
               ('A', 'E', 'J'), ('C', 'D', 'J'), ('C', 'F', 'H'),
               ('B', 'F', 'I')]
    pos = {x: i for i, x in enumerate(labels)}
    triples = [tuple(pos[x] for x in t) for t in triples]
    assert all(a < b < c for a, b, c in triples)
    assert all(len(set(t) & set(u)) <= 1
               for t, u in itertools.combinations(triples, 2))
    vertices = labels + [f'{t}{i}' for i in range(7) for t in ('x', 'y')]
    edges, qcopies = [], []
    for i, (a, b, c) in enumerate(triples):
        x, y = 10+2*i, 11+2*i
        edges.extend([frozenset((a, x, y)), frozenset((b, c, y))])
        qcopies.append((a, b, c, x, y))
    # For each selected subset, explicitly minimize over all four private
    # choices in each independent gadget.  This proves the closed formula,
    # and covers every one of the 2^24 actual vertex subsets.
    minimum = {}
    formula_checks = 0
    for bits in range(1 << 10):
        selected = {i for i in range(10) if bits >> i & 1}
        total = 2*len(selected)
        for a, b, c in triples:
            costs = [2*(ix+iy) - 3*(a in selected and ix and iy)
                     - 3*(b in selected and c in selected and iy)
                     for ix, iy in itertools.product((0, 1), repeat=2)]
            expected = -2 if {a, b, c} <= selected else (
                -1 if {b, c} <= selected and a not in selected else 0)
            assert min(costs) == expected
            formula_checks += 1
            total += min(costs)
        minimum[bits] = total
        assert bits == 0 or total > 0
    # When no selected vertex is present, every nonempty private subset
    # has no edge and has positive predimension.
    assert minimum[0] == 0
    strong_q_min = []
    for i, triple in enumerate(triples):
        base = sum(1 << v for v in triple)
        extension_min = min(v for bits, v in minimum.items()
                            if bits != base and bits & base == base)
        assert minimum[base] == 4
        assert extension_min > 4
        # At the same selected subset, the i-th private pair is forced;
        # every other private gadget intersects this triple in at most
        # one selected vertex, so adding its vertices costs at least 1.
        assert all(len(set(triple) & set(t)) <= 1
                   for j, t in enumerate(triples) if i != j)
        strong_q_min.append(extension_min)
    strong_singleton_min = []
    for point in range(10):
        base = 1 << point
        larger = min(v for bits, v in minimum.items()
                     if bits != base and bits & base == base)
        assert larger > 2
        strong_singleton_min.append(larger)
    # Enumerate ALL induced copies of Q, not merely the seven proposed
    # ones.  Two Q edges meet at their greatest vertex, so candidate edge
    # pairs exhaust all copies.  Their prescribed total order is rigid.
    qtype = {frozenset((0, 3, 4)), frozenset((1, 2, 4))}
    all_qcopies = set()
    for e, f in itertools.combinations(edges, 2):
        if len(e & f) != 1:
            continue
        vv = tuple(sorted(e | f))
        vi = {v: j for j, v in enumerate(vv)}
        induced = {frozenset(vi[v] for v in h) for h in edges if h <= set(vv)}
        if induced == qtype:
            all_qcopies.add(vv)
    assert all_qcopies == set(qcopies)
    # Three singleton arrows select positions a,b,c.  Rows record b-a
    # and c-a.  Unused singleton rows would be zero and do not matter.
    rows = [[0]*7 for _ in range(20)]
    for j, (a, b, c) in enumerate(triples):
        rows[b][j] += 1
        rows[a][j] -= 1
        rows[10+c][j] += 1
        rows[10+a][j] -= 1
    d = Matrix(rows)
    assert d.rank() == 7
    all_ones = Matrix.ones(7, 1)
    defect = d * all_ones
    assert all(int(v) % 2 == 0 for v in defect)
    assert sum(all_ones) % 2 == 1
    dual, params = d.T.gauss_jordan_solve(all_ones)
    dual = dual.subs({x: 0 for x in params})
    assert d.T*dual == all_ones
    # Smith normal form additionally records the exact torsion mechanism.
    from sympy.matrices.normalforms import smith_normal_form
    from sympy.polys.domains import ZZ
    snf = smith_normal_form(d, domain=ZZ)
    invariant_factors = [abs(int(snf[i, i])) for i in range(7)]
    # Independent exhaustive verification of the two-star bridge used to
    # prove the SAME family eventually has an integral affine equalizer.
    # Outer minima are 0,1,2.  Each block adds b,c,x,x',y above them.
    bridge_edges = []
    bridge_q = []
    for j, (a, ap) in enumerate(((0, 1), (1, 2))):
        b, c, x, xp, y = range(3+5*j, 8+5*j)
        bridge_edges.extend([frozenset((a, x, y)),
                             frozenset((ap, xp, y)),
                             frozenset((b, c, y))])
        bridge_q.extend([frozenset((a, b, c, x, y)),
                         frozenset((ap, b, c, xp, y))])
    bridge_minima = {frozenset((0, 2)): 100}
    bridge_minima.update({q: 100 for q in bridge_q})
    for bits in range(1, 1 << 13):
        ss = frozenset(v for v in range(13) if bits >> v & 1)
        dd = 2*len(ss) - 3*sum(e <= ss for e in bridge_edges)
        assert dd > 0
        for base in bridge_minima:
            if base < ss:
                bridge_minima[base] = min(bridge_minima[base], dd)
    assert all(value > 4 for value in bridge_minima.values())
    report = {
        'vertices': vertices,
        'edges': [sorted(e) for e in edges],
        'selected_triples': [[vertices[v] for v in t] for t in triples],
        'Q_copies': [list(q) for q in qcopies],
        'vertex_count': len(vertices), 'edge_count': len(edges),
        'delta_full': 2*len(vertices)-3*len(edges),
        'selected_subsets_checked': len(minimum),
        'private_formula_checks': formula_checks,
        'minimum_nonempty_selected_delta': min(v for b, v in minimum.items() if b),
        'minimum_by_selected_cardinality': [
            min(v for b, v in minimum.items() if b.bit_count() == k)
            for k in range(11)],
        'Q_strict_selected_extension_minima': strong_q_min,
        'selected_singleton_strict_extension_minima': strong_singleton_min,
        'all_induced_Q_copies_count': len(all_qcopies),
        'matrix': rows, 'rank_Q': d.rank(),
        'smith_invariant_factors': invariant_factors,
        'F2_witness': [1]*7,
        'integral_marginal_defect': list(map(int, defect)),
        'Q_dual_certificate': list(map(str, dual)),
        'two_star_bridge_vertex_count': 13,
        'two_star_bridge_edge_count': len(bridge_edges),
        'two_star_bridge_subsets_checked': (1 << 13)-1,
        'two_star_bridge_strict_extension_minima': list(bridge_minima.values()),
        'scope': 'Finite-target separation. The companion proof shows this same family is integrally equalizable at a larger target.'
    }
    print(json.dumps(report, indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
