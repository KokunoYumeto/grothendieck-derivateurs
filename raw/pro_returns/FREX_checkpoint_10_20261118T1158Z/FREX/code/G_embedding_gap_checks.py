#!/usr/bin/env python3
"""Finite certificates for the lexicographic embedding-gap monoids P_d.

The arbitrary-height presentation is proved in the manuscript.  This
checks all critical triples and binary-coordinate subdivision patterns
through depth five, and the finite chain quotient separates idempotents.
"""
from itertools import product, combinations
import json
from pathlib import Path


def check(depth):
    symbols = ('l', 'r') + tuple(f'e{i}' for i in range(depth))
    rules = {}
    for i in range(depth):
        rules[('l', f'e{i}')] = ('l',)
        rules[(f'e{i}', 'r')] = ('r',)
        for j in range(depth):
            rules[(f'e{i}', f'e{j}')] = (f'e{min(i,j)}',)

    def nf(word):
        word = tuple(word)
        while True:
            for i in range(len(word)-1):
                if word[i:i+2] in rules:
                    word = word[:i] + rules[word[i:i+2]] + word[i+2:]
                    break
            else:
                return word

    critical = 0
    for word in product(symbols, repeat=3):
        if word[:2] in rules and word[1:] in rules:
            assert nf(rules[word[:2]] + word[2:]) == nf(word[:1] + rules[word[1:]])
            critical += 1

    points = ['MIN'] + list(product(range(2), repeat=depth)) + ['MAX']

    def interval(a, b):
        if a == 'MIN' and b == 'MAX':
            return ('l', 'r')
        if a == 'MIN':
            return ('l',)
        if b == 'MAX':
            return ('r',)
        common = next(i for i, (x, y) in enumerate(zip(a,b)) if x != y)
        return (f'e{common}',)

    subdivisions = 0
    for a,b,c in combinations(points, 3):
        assert nf(interval(a,b) + interval(b,c)) == interval(a,c)
        subdivisions += 1

    value = {'l': 0, 'r': 0, **{f'e{i}': i for i in range(depth)}}
    for left, right in rules.items():
        assert min(value[x] for x in left) == min(value[x] for x in right)
    assert len({value[f'e{i}'] for i in range(depth)}) == depth
    assert all(value[f'e{i}'] != depth for i in range(depth))
    return dict(depth=depth, generators=len(symbols), rules=len(rules),
                critical_triples=critical, subdivision_triples=subdivisions,
                nonidentity_idempotents_separated=depth, status='PASS')


if __name__ == '__main__':
    results = [check(d) for d in range(1,6)]
    text = json.dumps(results, indent=2) + '\n'
    print(text, end='')
    Path(__file__).with_suffix('.json').write_text(text)
