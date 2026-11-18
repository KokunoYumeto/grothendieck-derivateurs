#!/usr/bin/env python3
"""Exact finite check of the alternative W8-bis glyph in A.3."""
from itertools import product
from sympy import Matrix, zeros


def span_total(n):
    # n discrete objects in the middle and one object in each outer fibre.
    obj = tuple(range(n + 2))
    rel = {(x, x) for x in obj} | {(x, y) for x in range(n) for y in (n, n + 1)}
    composable = [(a, b, c) for a, b, c in product(obj, repeat=3)
                  if (a, b) in rel and (b, c) in rel]
    assert all((a, c) in rel for a, b, c in composable)
    quadruples = [(a, b, c, d) for a, b, c, d in product(obj, repeat=4)
                  if (a, b) in rel and (b, c) in rel and (c, d) in rel]
    # A thin category has at most one composite with each pair of endpoints.
    assert all((a, d) in rel for a, b, c, d in quadruples)
    edges = sorted((a, b) for a, b in rel if a != b)
    triangles = [(a, b, c) for a, b, c in composable if a != b and b != c]
    assert not triangles
    d1 = zeros(len(obj), len(edges))
    for j, (a, b) in enumerate(edges):
        d1[a, j], d1[b, j] = -1, 1
    betti = (len(obj) - d1.rank(), len(edges) - d1.rank())
    print({"middle_objects": n, "total_objects": len(obj), "arrows": len(rel),
           "composable_pairs": len(composable), "associativity_triples": len(quadruples),
           "nerve_chain_ranks": [len(obj), len(edges)], "betti_Q": betti})
    print("boundary_d1 =", d1.tolist())
    return obj, rel, edges, d1, betti


src, src_rel, src_edges, src_d1, src_h = span_total(2)
tgt, tgt_rel, tgt_edges, tgt_d1, tgt_h = span_total(1)
f = {0: 0, 1: 0, 2: 1, 3: 2}
assert all((f[a], f[b]) in tgt_rel for a, b in src_rel)
f0 = zeros(len(tgt), len(src))
for a in src:
    f0[f[a], a] = 1
f1 = zeros(len(tgt_edges), len(src_edges))
for j, (a, b) in enumerate(src_edges):
    f1[tgt_edges.index((f[a], f[b])), j] = 1
assert tgt_d1 * f1 == f0 * src_d1
middle_h0 = Matrix([[1, 1]])
assert middle_h0.rank() == 1 and len(middle_h0.nullspace()) == 1
assert src_h == (1, 1) and tgt_h == (1, 0)
print("outer maps: identities on one-object categories")
print("middle H0 map:", middle_h0.tolist(), "; kernel generator:", middle_h0.nullspace()[0].T.tolist())
print("All functor, composition, associativity, and chain-map checks passed.")
print("The two outer maps are HZ equivalences; the middle and total maps are not.")
