#!/usr/bin/env python3
"""Exact p=2 twisted-cover search on one seven-macro-triple template.

Pair the fourteen lifted W slots; the old private-vertex injectivity
forces each actual edge to occur an even number of times.  Thus all
possible identifications on this template are covered by these pairings,
up to further optional vertex identifications.  A failure is only a
bounded search outcome, never a theorem of nonexistence in the category.
"""
import collections
import itertools
import json
from pathlib import Path
import time

MACROS = [('z', 'D', 'H'), ('A', 'z', 'I'), ('B', 'E', 'z'),
          ('A', 'E', 'J'), ('C', 'D', 'J'), ('C', 'F', 'H'),
          ('B', 'F', 'I')]
NAMES = sorted(set(sum((list(t) for t in MACROS), [])))
IDX = {(a, i): 2*j+i for j, a in enumerate(NAMES) for i in range(2)}
COPIES = [tuple(IDX[a, i] for a in t for i in range(2)) for t in MACROS]
SLOTS = [(q[0], q[3], q[4]) for q in COPIES]
SLOTS += [(q[1], q[2], q[5]) for q in COPIES]
ORDER = {(q[i], q[i+1]) for q in COPIES for i in range(5)}


def matchings(xs):
    if not xs:
        yield []
    else:
        first = xs[0]
        for i in range(1, len(xs)):
            second = xs[i]
            for tail in matchings(xs[1:i]+xs[i+1:]):
                yield [(first, second)]+tail


def analyze(pairs, count):
    parent = list(range(20))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i, j in pairs:
        for a, b in zip(SLOTS[i], SLOTS[j]):
            a, b = find(a), find(b)
            if a != b:
                parent[b] = a
    reps = [find(a) for a in range(20)]
    if any(len({reps[a] for a in q}) != 6 for q in COPIES):
        count['copy_collapsed'] += 1
        return None
    vertices = set(reps)
    arrows = {(reps[a], reps[b]) for a, b in ORDER}
    vv, order = set(vertices), []
    while vv:
        low = sorted(a for a in vv if not any(y == a and x in vv for x, y in arrows))
        if not low:
            count['order_cycle'] += 1
            return None
        a = low[0]
        order.append(a)
        vv.remove(a)
    count['ordered_quotients'] += 1
    position = {a: i for i, a in enumerate(order)}
    qcopies = [tuple(position[reps[a]] for a in q) for q in COPIES]
    assert all(tuple(sorted(q)) == q for q in qcopies)
    edges = set(tuple(position[reps[a]] for a in e) for e in SLOTS)
    assert all(tuple(sorted(e)) == e for e in edges)
    multiplicity = collections.Counter(tuple(position[reps[a]] for a in e) for e in SLOTS)
    assert all(v % 2 == 0 for v in multiplicity.values())
    eset = [frozenset(e) for e in sorted(edges)]
    if any({e for e in eset if e <= set(q)} !=
           {frozenset((q[0], q[3], q[4])), frozenset((q[1], q[2], q[5]))}
           for q in qcopies):
        count['not_induced'] += 1
        return None
    unions = {frozenset()}
    for e in eset:
        unions |= {u | e for u in list(unions)}
    def delta(u):
        return 2*len(u)-3*sum(e <= u for e in eset)
    if any(delta(u) <= 0 for u in unions if u):
        count['not_positive'] += 1
        return None
    allvertices = frozenset(range(len(order)))
    for q in qcopies:
        base = frozenset(q)
        candidates = {base | u for u in unions}
        candidates |= {base | {a} for a in allvertices-base}
        if any(delta(u) <= 6 for u in candidates if base < u):
            count['not_strong'] += 1
            return None
    count['survivors'] += 1
    # Directly test the actual ordered P=2-tuples after quotienting.
    marginals = []
    for i in range(3):
        marginals.append(collections.Counter((q[2*i], q[2*i+1]) for q in qcopies))
    for i in (1, 2):
        assert all((marginals[i][t]-marginals[0][t]) % 2 == 0
                   for t in set(marginals[i]) | set(marginals[0]))
    return dict(pairing=pairs, vertices=len(order), edges=sorted(edges),
                Q_copies=qcopies, delta=delta(allvertices),
                witness=[1]*7, names=NAMES,
                quotient=[position[reps[a]] for a in range(20)])


def main():
    start = time.monotonic()
    counts = collections.Counter()
    hits = []
    for pairs in matchings(list(range(14))):
        counts['pairings'] += 1
        hit = analyze(pairs, counts)
        if hit is not None:
            hits.append(hit)
            print('SURVIVOR', json.dumps(hit), flush=True)
    result = dict(counts=dict(counts), hits=hits,
                  elapsed_seconds=round(time.monotonic()-start, 3),
                  scope='One macro template; a negative search does not exclude all larger targets or additional identifications.')
    print('RESULT', json.dumps(result), flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
