"""Exact arithmetic check of the barycentric prism used in C4.12.

The proof is the displayed all-dimensional telescoping identity; this
certificate checks all increasing basis simplices on five vertices for
several augmentation-preserving maps, including a non-idempotent map.
"""
from fractions import Fraction as F
from itertools import combinations


def add(target, source, scalar=F(1)):
    for key, value in source.items():
        target[key] = target.get(key, F(0)) + scalar * value
        if not target[key]:
            del target[key]
    return target


def unit(v):
    return {v: F(1)}


def wedge(vectors):
    ans = {(): F(1)}
    for vector in vectors:
        nxt = {}
        for simplex, coefficient in ans.items():
            for v, value in vector.items():
                if v in simplex:
                    continue
                sign = (-1) ** sum(w > v for w in simplex)
                key = tuple(sorted(simplex + (v,)))
                add(nxt, {key: coefficient * value * sign})
        ans = nxt
    return ans


def boundary(chain):
    ans = {}
    for simplex, coefficient in chain.items():
        for i in range(len(simplex)):
            add(ans, {simplex[:i] + simplex[i+1:]: coefficient},
                F((-1) ** i))
    return ans


def chain_map(chain, h):
    ans = {}
    for simplex, coefficient in chain.items():
        add(ans, wedge([h[v] for v in simplex]), coefficient)
    return ans


def prism(chain, h):
    ans = {}
    for simplex, coefficient in chain.items():
        for i in range(len(simplex)):
            vectors = ([h[v] for v in simplex[:i+1]]
                       + [unit(v) for v in simplex[i:]])
            add(ans, wedge(vectors), coefficient * (-1) ** i)
    return ans


maps = [
    [unit(v) for v in range(5)],
    [unit(0) for _ in range(5)],
    [{0: F(1, 2), 1: F(1, 2)},
     {1: F(1, 3), 2: F(2, 3)},
     {0: F(1, 3), 1: F(1, 3), 2: F(1, 3)},
     {0: F(2), 2: F(-1)},
     {1: F(1, 4), 2: F(3, 4)}],
]
checked = 0
for h in maps:
    assert all(sum(v.values()) == 1 for v in h)
    for size in range(1, 6):
        for simplex in combinations(range(5), size):
            chain = {simplex: F(1)}
            lhs = add(boundary(prism(chain, h)), prism(boundary(chain), h))
            rhs = add(dict(chain), chain_map(chain, h), F(-1))
            assert lhs == rhs, (simplex, lhs, rhs)
            checked += 1

low_rank = maps[-1]
for size in (4, 5):
    for simplex in combinations(range(5), size):
        assert chain_map({simplex: F(1)}, low_rank) == {}

print("Augmentation-preserving maps checked:", len(maps))
print("Increasing basis simplices checked:", checked)
print("Degrees checked: 0 through 4, with augmented boundary in degree 0.")
print("Identity verified exactly: boundary*H + H*boundary = id - exterior(h).")
print("The third map has signed rational entries and is not idempotent.")
print("Its image is supported on 3 vertices; exterior powers 4 and 5 vanish.")
print("No finite-dimensional test replaces the all-dimensional proof.")
