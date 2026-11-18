#!/usr/bin/env python3
"""Three actual degree-fourteen fiber tests: finite algebra certificate.

The geometric split T ~ B x F, and the identification of the low fiber
basis, are proved in D.2.18. This script checks only their finite diagonal
and Steenrod algebra consequences. It does not calculate an integral
spectral-sequence extension or a homotopy group.
"""
from itertools import product
from pathlib import Path
import json
import D2_fiber_poly_check as a

# Complete Serre monomial labels through degree fourteen. The next
# polynomial generator has degree seventeen and cannot enter this check.
for ex in product(range(8), range(5), range(3), range(2)):
    if 0 < a.deg(ex) <= 14 and ex not in a.LABEL:
        a.LABEL[ex] = 'L' + ''.join(map(str, ex))
a.LABEL[(0, 0, 2, 0)] = 's'
a.EXP = {name: ex for ex, name in a.LABEL.items()}
# The only extra generator operation needed in this degree range.
a.GEN_SQ[3][1] = {(0, 0, 2, 0)}

TESTS = {'ZP': a.term('x', 'i'),
         'ZQ': a.term('c', 's'),
         'ZR': a.term('d', 't')}

def eval_poly_functional(poly, support):
    return len(poly & support) % 2

def square_pair(poly, support):
    # <theta^2,z> = <theta tensor theta, Delta z>. Every degree-seven
    # tensor factor here is polynomial, so the low projection table
    # completely specifies the pulled-back functionals.
    return sum(l in support and r in support for l, r in a.delta(poly)) % 2

def frobenius_dual(poly):
    # Diagonal coefficients, i.e. dual of cup-square in characteristic 2.
    return {l for l, r in a.delta(poly) if l == r}

def rank_mod2(rows):
    rows = [list(row) for row in rows]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                rows[i] = [x ^ y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank

def main():
    # Pullbacks under r:T->F, restricted to polynomial H7(T):
    # r^*(V*+P*) detects bc, r^*(P*+Q*) detects bc+ad.
    theta1 = {tuple(sorted(('b', 'c')))}
    theta2 = theta1 | {tuple(sorted(('a', 'd')))}
    A4dual = {('a', 'a')}
    expected_steps = {
        'ZP': [a.term('c', 'c'), set(), set()],
        'ZQ': [a.term('a', 'x'), a.term('a', 'b'), a.term('a', 'a')],
        'ZR': [a.term('b', 'd'), a.term('a', 'b'), a.term('a', 'a')],
    }
    expected_frobenius = {'ZP': a.term('b', 'c'),
                          'ZQ': a.term('a', 'd'), 'ZR': set()}
    reports, matrix = [], []
    for name, poly in TESTS.items():
        steps, cur = [], poly
        for k in (6, 3, 1):
            cur = a.sq(k, cur)
            steps.append(cur)
        assert steps == expected_steps[name], (name, steps)
        fd = frobenius_dual(poly)
        assert fd == expected_frobenius[name], (name, fd)
        row = [square_pair(poly, theta1), square_pair(poly, theta2),
               eval_poly_functional(steps[-1], A4dual)]
        matrix.append(row)
        reports.append({'test': name, 'representative_in_T': a.show(poly),
                        'dual_frobenius': a.show(fd),
                        'Sq_star_6': a.show(steps[0]),
                        'Sq_star_3_Sq_star_6': a.show(steps[1]),
                        'Sq_star_1_Sq_star_3_Sq_star_6': a.show(steps[2]),
                        'pairing_row': row})
    assert matrix == [[1, 1, 0], [0, 1, 1], [0, 0, 1]], matrix
    assert rank_mod2(matrix) == 3
    result = {
        'status': 'PASS', 'field': 'F2', 'degree': 14,
        'scope': 'Finite Serre/Cartan and diagonal calculation; geometric retraction proved separately',
        'columns': ['(V*+P*)^2', '(P*+Q*)^2', 'Sq6 Sq3 Sq1 A4*'],
        'matrix': matrix, 'rank': 3, 'tests': reports,
    }
    dest = Path(__file__).parent / 'outputs' / 'D2_degree14_pairing_check.json'
    dest.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'rank': 3, 'matrix': matrix,
                      'output': str(dest)}))

if __name__ == '__main__':
    main()
