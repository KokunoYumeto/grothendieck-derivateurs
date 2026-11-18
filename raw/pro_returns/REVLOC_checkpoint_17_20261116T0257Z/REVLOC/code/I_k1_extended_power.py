#!/usr/bin/env python3
"""Integral arity-two Moore-chain audit for the k=1 finite source.

The complex is P_*(C2) tensor_{Z[C2]} (M tensor M), using the
signed transposition and the standard periodic free resolution.
This certifies only integral homology of the stable extended-power
summand. It does not compute unstable attaching maps or extend a map.
"""
from pathlib import Path
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def snf(matrix):
    dm = DomainMatrix.from_Matrix(matrix).convert_to(sp.ZZ)
    return tuple(x.to_Matrix() for x in smith_normal_decomp(dm))


def chain(bottom, modulus, limit):
    words = ('aa', 'ab', 'ba', 'bb')
    deg = {'aa': 2*bottom, 'ab': 2*bottom+1,
           'ba': 2*bottom+1, 'bb': 2*bottom+2}
    bases = {n: [(n-deg[w], w) for w in words if n >= deg[w]]
             for n in range(limit+2)}
    trans = {'aa': ('aa', (-1)**bottom), 'ab': ('ba', 1),
             'ba': ('ab', 1), 'bb': ('bb', (-1)**(bottom+1))}
    label = {'aa': [], 'ab': [('aa', (-1)**bottom*modulus)],
             'ba': [('aa', modulus)],
             'bb': [('ab', modulus), ('ba', (-1)**(bottom+1)*modulus)]}
    diffs = {}
    for n in range(1, limit+2):
        out = sp.zeros(len(bases[n-1]), len(bases[n]))
        positions = {x: i for i, x in enumerate(bases[n-1])}
        for j, (resolution_degree, word) in enumerate(bases[n]):
            if resolution_degree:
                tw, sign = trans[word]
                out[positions[(resolution_degree-1, tw)], j] += sign
                out[positions[(resolution_degree-1, word)], j] += (
                    -1 if resolution_degree % 2 else 1)
            for next_word, coefficient in label[word]:
                out[positions[(resolution_degree, next_word)], j] += (
                    (-1)**resolution_degree*coefficient)
        diffs[n] = out
    for n in range(2, limit+2):
        assert diffs[n-1]*diffs[n] == sp.zeros(
            len(bases[n-2]), len(bases[n]))
    return bases, diffs


def homology(bottom, modulus, limit):
    bases, diffs = chain(bottom, modulus, limit)
    answer = []
    for n in range(2*bottom, limit+1):
        d = diffs[n]
        diag, left, right = snf(d)
        assert diag == left*d*right
        rank = d.rank()
        incoming = right.inv()*diffs[n+1]
        assert incoming[:rank, :] == sp.zeros(rank, incoming.cols)
        reduced = incoming[rank:, :]
        inv, _, _ = snf(reduced)
        torsion = [abs(int(inv[i, i])) for i in
                   range(min(inv.rows, inv.cols))
                   if abs(inv[i, i]) > 1]
        free = reduced.rows - reduced.rank()
        answer.append({'degree': n, 'torsion': torsion,
                       'free_rank': free,
                       'chain_basis': [f'e{i}({w})' for i, w in bases[n]],
                       'differential': [list(map(int, row))
                                        for row in d.tolist()]})
    return answer


if __name__ == '__main__':
    result = {
        'scope': __doc__.strip(),
        'status': 'PASS: every integral differential squares to zero; '
                  'Smith decompositions checked with both basis matrices.',
        'D2_M2_3': homology(3, 2, 13),
        'D2_M4_5': homology(5, 4, 13),
    }
    destination = Path(__file__).parent/'outputs'/'I_k1_extended_power.json'
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: [{'degree': row['degree'],
                            'torsion': row['torsion'],
                            'free_rank': row['free_rank']}
                           for row in value]
                      if isinstance(value, list) else value
                      for key, value in result.items()}, indent=2))
