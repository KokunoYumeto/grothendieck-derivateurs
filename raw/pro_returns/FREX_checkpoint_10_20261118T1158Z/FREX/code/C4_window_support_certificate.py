"""Exact finite checks for the unbounded two-arrow support obstruction.

The proof's lower bound is symbolic. This certificate verifies its coordinate
tracking on all short closed walks in several finite shift graphs and gives
an explicit integral affine witness of support 2n+1 for n=1,...,8.
"""
from collections import Counter, defaultdict
from itertools import combinations

def incidence(edges):
    out = Counter()
    for edge, coefficient in edges.items():
        out[edge[:-1]] += coefficient
        out[edge[1:]] -= coefficient
    return {vertex: coefficient for vertex, coefficient in out.items() if coefficient}

for n in range(1, 9):
    long_sequence = tuple(range(2*n+1))
    short_sequence = tuple(j for j in long_sequence if j != n)
    witness = Counter()
    for i in range(n+1):
        witness[long_sequence[i:i+n+1]] += 1
    for i in range(n):
        witness[short_sequence[i:i+n+1]] -= 1
    assert len(witness) == 2*n+1
    assert sum(witness.values()) == 1
    assert not incidence(witness)
    print(f"n={n}: integral affine witness support={len(witness)}, augmentation=1, incidence=0; PASS")

for n in range(2, 7):
    adjacency = defaultdict(list)
    for edge in combinations(range(n+4), n+1):
        first, last = edge[:-1], edge[1:]
        adjacency[first].append((last, 1))
        adjacency[last].append((first, -1))
    checks = [0]
    def extend(start, path, signs):
        if len(signs) >= n-1:
            return
        for nxt, sign in adjacency[path[-1]]:
            if nxt == start:
                steps = signs+[sign]
                sums = [0]
                for step in steps:
                    sums.append(sums[-1]+step)
                h = 1+max(sums)
                assert h <= n+min(sums)
                vertices = path+[start]
                value = start[h-1]
                assert all(vertex[h-s-1] == value for vertex, s in zip(vertices, sums))
                assert sums[-1] == 0
                checks[0] += 1
            elif nxt not in path:
                extend(start, path+[nxt], signs+[sign])
    for start in adjacency:
        extend(start, [start], [])
    print(f"n={n}: {checks[0]} short closed-walk checks, all signed augmentations zero; PASS")
