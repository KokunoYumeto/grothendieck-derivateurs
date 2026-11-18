#!/usr/bin/env python3
"""Fixed-length unification for extending the G.11 rectangle to X_11.

This samples integer length vectors and solves all word-position equalities
exactly.  It is a finite experiment, not a nonexistence theorem.
"""
import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
import sympy as sp
from G_cross_lift_rank_search import UF, EDGES, N

TEMPLATES = {'ua': 'cbabbaab', 'ub': 'caabbaab',
             'va': 'cabbaab', 'vc': 'cbbbaab'}


def solution(lengths, templates=None, inverse_matrix=None):
    templates = TEMPLATES if templates is None else templates
    offsets = [0]
    for length in lengths:
        offsets.append(offsets[-1] + length)
    uf = UF(offsets[-1])
    edge_words = []
    for a, b, c in EDGES:
        if inverse_matrix is None:
            beta = lengths[a] - lengths[N+a]
            alpha = lengths[b] - lengths[N+a]
            gamma = 7*lengths[N+a] - 3*lengths[a] - 3*lengths[b]
        else:
            alpha, beta, gamma = map(int, inverse_matrix*sp.Matrix(
                [lengths[a], lengths[b], lengths[N+c]]))
        assert min(alpha, beta, gamma) > 0
        size = dict(a=alpha, b=beta, c=gamma)
        positions = {}
        for name, vertex in [('ua', a), ('ub', b), ('va', N+a), ('vc', N+c)]:
            at = offsets[vertex]
            for letter in templates[name]:
                segment = list(range(at, at + size[letter]))
                if letter not in positions:
                    positions[letter] = segment
                else:
                    for x, y in zip(positions[letter], segment):
                        uf.union(x, y)
                at += size[letter]
            assert at == offsets[vertex+1]
        edge_words.append(positions)
    columns = defaultdict(lambda: [0]*(2*N))
    for i in range(2*N):
        for j in range(offsets[i], offsets[i+1]):
            columns[uf.find(j)][i] += 1
    patterns = list(set(map(tuple, columns.values())))
    matrix = sp.Matrix(2*N, len(patterns), lambda i, j: patterns[j][i])
    words = [[uf.find(j) for j in range(offsets[i], offsets[i+1])]
             for i in range(2*N)]
    edge_maps = []
    edge_ranks = []
    for (a, b, c), pos in zip(EDGES, edge_words):
        images = [[uf.find(j) for j in pos[letter]] for letter in 'abc']
        images += [words[c], words[N+b]]
        counts = [Counter(word) for word in images]
        alphabet = sorted(set().union(*(set(word) for word in images)))
        em = sp.Matrix(5, len(alphabet), lambda i, j: counts[i][alphabet[j]])
        edge_ranks.append(em.rank())
        edge_maps.append(images)
    return matrix.rank(), len(columns), patterns, edge_ranks, words, edge_maps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--trials', type=int, default=50)
    ap.add_argument('--seed', type=int, default=20261118)
    ap.add_argument('--perturbation', type=int, default=4)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    d = sp.zeros(len(EDGES), 2*N)
    for j, (a,b,c) in enumerate(EDGES):
        d[j,b] += 1; d[j,a] -= 1; d[j,N+c] += 1; d[j,N+a] -= 1
    kernel = d.nullspace()
    assert len(kernel) == 16
    hist = Counter()
    best = None
    for trial in range(args.trials):
        perturb = sp.zeros(2*N, 1)
        for vec in kernel:
            perturb += rng.randint(-args.perturbation, args.perturbation)*vec
        perturb = list(map(int, perturb))
        scale = 14*max(map(abs, perturb)) + 1
        lengths = [scale*(8 if i<N else 7) + perturb[i] for i in range(2*N)]
        rank, alphabet, patterns, edge_ranks, words, edge_maps = solution(lengths)
        hist[rank] += 1
        if best is None or (rank, min(edge_ranks)) > (best['rank'], min(best['edge_ranks'])):
            best = dict(trial=trial, rank=rank, expected_rank=16,
                        alphabet_size=alphabet, edge_ranks=edge_ranks,
                        lengths=lengths, count_patterns=patterns,
                        point_words=words, edge_maps=edge_maps)
            print(f'trial={trial} rank={rank}/16 alphabet={alphabet} edge_ranks={edge_ranks}', flush=True)
        if rank == 16 and min(edge_ranks) == 5:
            print('Found full incidence rank with all edge maps of full abelian rank.', flush=True)
            break
    report = dict(parameters=vars(args), tried=trial+1,
                  rank_histogram=dict(sorted(hist.items())), best=best,
                  negative_results_are_only_exploratory=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print('Exact rank histogram:', dict(sorted(hist.items())), flush=True)
    print('Finite search only; no global-extension or nonexistence claim.', flush=True)


if __name__ == '__main__':
    main()
