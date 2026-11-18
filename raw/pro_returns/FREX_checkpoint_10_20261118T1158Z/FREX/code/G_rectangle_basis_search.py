#!/usr/bin/env python3
"""Search bifix rectangle word systems with full ambient free group.

Exploratory finite search only.  A negative search result proves nothing
outside its enumerated range.  The Stallings folding is combinatorial.
"""
import argparse
import itertools
import json
import random
from G_rectangle_local import bifix, determinant


def fold(words):
    edges = []
    vertex = 1
    for word in words:
        source = 0
        for i, letter in enumerate(word):
            target = 0 if i == len(word) - 1 else vertex
            if target:
                vertex += 1
            edges.extend([(source, letter, target),
                          (target, letter.upper(), source)])
            source = target
    parent = list(range(vertex))

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    changed = True
    while changed:
        changed = False
        outgoing = {}
        for source, letter, target in edges:
            source, target = root(source), root(target)
            key = source, letter
            if key in outgoing:
                previous = root(outgoing[key])
                if previous != target:
                    parent[target] = previous
                    changed = True
            else:
                outgoing[key] = target
    folded = sorted({(root(s), a, root(t)) for s, a, t in edges})
    vertices = {s for s, _, _ in folded} | {t for _, _, t in folded}
    return len(vertices), len(folded) // 2 - len(vertices) + 1, folded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials', type=int, default=100000)
    parser.add_argument('--seed', type=int, default=20261118)
    parser.add_argument('--max-length', type=int, default=5)
    parser.add_argument('--mixed-difference', action='store_true')
    args = parser.parse_args()
    rng = random.Random(args.seed)
    candidates = bifix_count = unimodular_count = 0
    found = None
    histogram = {}
    for trial in range(args.trials):
        p, r, q, s = [''.join(rng.choice('abc') for _ in range(
            rng.randint(1, args.max_length))) for _ in range(4)]
        words = [p + q, r + q, p + s, r + s]
        candidates += 1
        difference = [r.count(a) - p.count(a) for a in 'abc']
        if args.mixed_difference and not (min(difference) < 0 < max(difference)):
            continue
        if not bifix(words):
            continue
        bifix_count += 1
        matrix = [[word.count(a) for word in words[:3]] for a in 'abc']
        det = determinant(matrix)
        if abs(det) != 1:
            continue
        unimodular_count += 1
        vertices, rank, edges = fold(words)
        histogram[vertices] = histogram.get(vertices, 0) + 1
        if vertices == 1 and rank == 3:
            found = dict(p=p, r=r, q=q, s=s, words=words,
                         determinant=det, folded_edges=edges, trial=trial)
            break
    print(json.dumps(dict(parameters=vars(args), candidates=candidates,
                          bifix=bifix_count, unimodular=unimodular_count,
                          folded_vertex_histogram=histogram, found=found,
                          negative_results_are_only_exploratory=True), indent=2))


if __name__ == '__main__':
    main()
