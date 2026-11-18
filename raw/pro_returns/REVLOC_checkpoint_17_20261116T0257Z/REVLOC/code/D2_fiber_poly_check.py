#!/usr/bin/env python3
"""Exact finite certificate for polynomial fibre classes in D.2.18--20.

This checks coproducts and Sq_*^1,2,4 in degrees at most nine using
only the polynomial Serre algebra and Cartan. It does not certify the
Browder/top-operation formulas or any homotopy attachment interface.
Those are proved separately from the opened CLM source in the paper.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

GEN_DEG = (2, 3, 5, 9)
LABEL = {
    (1, 0, 0, 0): 'a', (0, 1, 0, 0): 'b',
    (2, 0, 0, 0): 'c', (0, 0, 1, 0): 'd',
    (1, 1, 0, 0): 'e', (3, 0, 0, 0): 'f',
    (0, 2, 0, 0): 'x', (2, 1, 0, 0): 'g',
    (1, 0, 1, 0): 'h', (4, 0, 0, 0): 'i',
    (1, 2, 0, 0): 'j', (0, 1, 1, 0): 'l',
    (3, 1, 0, 0): 'm', (2, 0, 1, 0): 'n',
    (0, 3, 0, 0): 'o', (0, 0, 0, 1): 't',
}
EXP = {v: k for k, v in LABEL.items()}
ZERO = (0, 0, 0, 0)

def xor(*sets):
    out = set()
    for s in sets:
        out.symmetric_difference_update(s)
    return out

def mul(a, b):
    out = set()
    for x in a:
        for y in b:
            out.symmetric_difference_update({tuple(sorted(x + y))})
    return out

def term(*letters):
    return {tuple(sorted(letters))}

def pol(*words):
    return xor(*(term(*w) for w in words))

def tensor_mul(a, b):
    out = set()
    for l, r in a:
        for s, t in b:
            out.symmetric_difference_update({
                (tuple(sorted(l+s)), tuple(sorted(r+t)))})
    return out

def delta_label(label):
    ex = EXP[label]
    out = set()
    for left in product(*(range(n+1) for n in ex)):
        right = tuple(n-m for n, m in zip(ex, left))
        l = () if left == ZERO else (LABEL[left],)
        r = () if right == ZERO else (LABEL[right],)
        out.add((l, r))
    return out

def delta(poly):
    out = set()
    for word in poly:
        d = {((), ())}
        for label in word:
            d = tensor_mul(d, delta_label(label))
        out.symmetric_difference_update(d)
    return out

def reduced_delta(poly):
    return {p for p in delta(poly) if p[0] and p[1]}

# Cohomology polynomials are finite sets of exponent vectors over F2.
def cmul(a, b):
    out = set()
    for x in a:
        for y in b:
            out.symmetric_difference_update({tuple(i+j for i, j in zip(x, y))})
    return out

GEN_SQ = [
    {0: {(1,0,0,0)}, 1: {(0,1,0,0)}, 2: {(2,0,0,0)}},
    {0: {(0,1,0,0)}, 2: {(0,0,1,0)}, 3: {(0,2,0,0)}},
    {0: {(0,0,1,0)}, 1: {(0,2,0,0)}, 4: {(0,0,0,1)},
     5: {(0,0,2,0)}},
    {0: {(0,0,0,1)}},
]

def csq(k, exponent):
    total = {0: {ZERO}}
    for g, count in enumerate(exponent):
        for _ in range(count):
            nxt = {}
            for i, poly in total.items():
                for j, value in GEN_SQ[g].items():
                    if i+j <= k:
                        nxt[i+j] = xor(nxt.get(i+j, set()), cmul(poly, value))
            total = nxt
    return total.get(k, set())

def deg(ex):
    return sum(a*b for a, b in zip(ex, GEN_DEG))

def sq_label(k, label):
    if k == 0:
        return term(label)
    target = EXP[label]
    return {(name,) for ex, name in LABEL.items()
            if deg(ex) == deg(target)-k and target in csq(k, ex)}

def sq(k, poly):
    out = set()
    for word in poly:
        total = {0: {()}}
        for label in word:
            nxt = {}
            for i, value in total.items():
                for j in range(k-i+1):
                    nxt[i+j] = xor(nxt.get(i+j, set()),
                                   mul(value, sq_label(j, label)))
            total = nxt
        out.symmetric_difference_update(total.get(k, set()))
    return out

def show(poly):
    if not poly:
        return '0'
    words = []
    for w in sorted(poly):
        c = Counter(w)
        words.append(''.join(x + (str(c[x]) if c[x] > 1 else '')
                             for x in sorted(c)) or '1')
    return '+'.join(words)

def show_tensor(d):
    return [show({l})+' tensor '+show({r}) for l, r in sorted(d)]

CLASSES = {
    'A4': pol('aa'),
    'z5': pol('e', 'ab'),
    'p3': pol('f', 'ac', 'aaa'),
    'P7': pol('g', 'ae', 'bc', 'aab'),
    'Q7': pol('h', 'ad'),
    'W8': pol('aaaa'),
    'C8': pol('cc'),
    'L8': pol('l', 'bd'),
    'M8': pol('j', 'ax', 'be', 'abb'),
    'ZA9': mul(pol('aa'), pol('e', 'ab')),
    'Pm9': pol('m', 'ag', 'ce', 'aae', 'bf', 'aaab'),
    'Pn9': pol('n', 'ah', 'cd', 'aad'),
    'Po9': pol('o', 'bx', 'bbb'),
}
EXPECTED = {
    'A4': (set(), set(), set()),
    'z5': (pol('aa'), set(), set()),
    'p3': (set(), pol('aa'), set()),
    'P7': (CLASSES['p3'], CLASSES['z5'], set()),
    'Q7': (set(), CLASSES['z5'], set()),
    'W8': (set(), set(), set()),
    'C8': (set(), set(), CLASSES['A4']),
    'L8': (CLASSES['Q7'], pol('bb'), set()),
    'M8': (CLASSES['Q7'], CLASSES['p3'], set()),
    'ZA9': (CLASSES['W8'], set(), set()),
    'Pm9': (CLASSES['W8'], set(), set()),
    'Pn9': (set(), xor(CLASSES['P7'], CLASSES['Q7']), CLASSES['z5']),
    'Po9': (xor(CLASSES['L8'], CLASSES['M8']),
            xor(CLASSES['P7'], CLASSES['Q7']), CLASSES['z5']),
}

def main():
    report = []
    for name, value in CLASSES.items():
        rd = reduced_delta(value)
        if name == 'C8':
            assert rd == {(('a','a'), ('a','a'))}, (name, rd)
        elif name == 'ZA9':
            want = {(l, r) for l in CLASSES['A4'] for r in CLASSES['z5']}
            want |= {(r, l) for l in CLASSES['A4'] for r in CLASSES['z5']}
            assert rd == want, (name, rd)
        else:
            assert not rd, (name, rd)
        operations = tuple(sq(k, value) for k in (1,2,4))
        assert operations == EXPECTED[name], (name, operations, EXPECTED[name])
        report.append({'class': name, 'polynomial': show(value),
                       'reduced_coproduct': show_tensor(rd),
                       'Sq1': show(operations[0]), 'Sq2': show(operations[1]),
                       'Sq4': show(operations[2])})
    output = {
        'status': 'PASS', 'field': 'F2', 'max_degree': 9,
        'scope': '13 polynomial classes: coproducts and 39 operation values; no homotopy or top-operation claims',
        'classes': report,
    }
    dest = Path(__file__).parent/'outputs'/'D2_fiber_poly_check.json'
    dest.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'classes': len(report),
                      'operation_values': 3*len(report), 'output': str(dest)}))

if __name__ == '__main__':
    main()
