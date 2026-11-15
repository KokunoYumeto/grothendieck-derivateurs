#!/usr/bin/env python3
"""Independent finite certificates for INDLOCAL A.9 and the HNN word check.

The group-theoretic contradiction in A.9 is proved in the paper.  These
checks certify its finite source complexes and its specified retraction
on integral cellular chains.  No finite search is used to infer a general
asphericity or simplicity statement.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def faces(vertices, max_size):
    return {k - 1: list(combinations(vertices, k)) for k in range(1, max_size + 1)}


def boundary(chains, d):
    if d == 0:
        return sp.zeros(0, len(chains[0]))
    low = {s: i for i, s in enumerate(chains[d - 1])}
    result = sp.zeros(len(low), len(chains.get(d, [])))
    for j, simplex in enumerate(chains.get(d, [])):
        for k in range(len(simplex)):
            result[low[simplex[:k] + simplex[k + 1:]], j] = (-1) ** k
    return result


def homology_certificate(chains):
    maxd = max(chains)
    bs = {d: boundary(chains, d) for d in range(maxd + 1)}
    bs[maxd + 1] = sp.zeros(len(chains[maxd]), 0)
    for d in range(1, maxd + 1):
        assert bs[d - 1] * bs[d] == sp.zeros(bs[d - 1].rows, bs[d].cols)
    betti = [len(chains[d]) - bs[d].rank() - bs[d + 1].rank()
             for d in range(maxd + 1)]
    # Every nonzero Smith invariant equal to one certifies absence of
    # torsion in each ambient chain quotient, hence in its homology subgroup.
    smith = {}
    for d in range(1, maxd + 1):
        mat = smith_normal_form(bs[d], domain=ZZ)
        diag = [int(mat[i, i]) for i in range(min(mat.shape)) if mat[i, i]]
        assert all(abs(x) == 1 for x in diag)
        smith[str(d)] = diag
    return {"simplex_counts": [len(chains[d]) for d in range(maxd + 1)],
            "betti": [int(x) for x in betti],
            "boundary_smith_nonzero": smith,
            "torsion_free": True}


def free_product_reduce(word, modulus):
    stack = []
    for factor, exponent in word:
        if factor == 'g':
            exponent %= modulus
        if exponent == 0:
            continue
        if stack and stack[-1][0] == factor:
            exponent += stack.pop()[1]
            if factor == 'g':
                exponent %= modulus
            if exponent == 0:
                continue
        stack.append((factor, exponent))
    return stack


def cyclic_reduce(word, modulus):
    word = free_product_reduce(word, modulus)
    while len(word) > 1 and word[0][0] == word[-1][0]:
        # Conjugate the first syllable to the end, then reduce.
        word = free_product_reduce(word[1:] + word[:1], modulus)
    return word


def main():
    tetrahedron_boundary = homology_certificate(faces(range(4), 3))
    triangle = homology_certificate(faces(range(3), 3))
    assert tetrahedron_boundary['betti'] == [1, 0, 1]
    assert triangle['betti'] == [1, 0, 0]
    # Cellular complexes for S^2 and S^2 wedge S^2 have zero differential.
    inclusion = sp.Matrix([[1], [0]])
    retraction = sp.Matrix([[1, 0]])
    assert retraction * inclusion == sp.eye(1)
    assert inclusion * retraction != sp.eye(2)
    assert len(retraction.nullspace()) == 1
    w = [('g', 1), ('t', 1), ('g', -1), ('t', -1),
         ('g', 1), ('t', 2), ('g', -1), ('t', -2)]
    checks = []
    for modulus in range(2, 13):
        for h in range(modulus):
            length = len(cyclic_reduce(w + [('g', h)], modulus))
            expected = 6 if (h + 1) % modulus == 0 else 8
            assert length == expected
            checks.append({'order_g': modulus, 'h_power': h, 'length': length})
    out = {
        'tetrahedron_boundary': tetrahedron_boundary,
        'triangle': triangle,
        'wedge_retraction': {'i': [[1], [0]], 'r': [[1, 0]],
                            'r_i_identity': True, 'kernel_rank': 1},
        'hnn_finite_cyclic_special_cases': checks,
        'all_checks_passed': True,
    }
    dest = Path(__file__).with_name('a_finite_checks.json')
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k:v for k,v in out.items()
                      if k != 'hnn_finite_cyclic_special_cases'}, indent=2))
    print('HNN cyclic-reduction checks:', len(checks))

if __name__ == '__main__':
    main()
