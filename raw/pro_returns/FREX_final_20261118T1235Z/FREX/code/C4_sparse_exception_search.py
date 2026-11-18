#!/usr/bin/env python3
"""Exact finite-target search, not a test of global categorical exactness.

Enumerate ordered C_delta targets with n<=7 and at most 3 hyperedges.
For each edge-containing strong Q type and each strong P type with at
least three arrows P->Q, test the full parallel family.  A reported hit
has an F_2 affine equalizer in this R but none over Q in this same R.
The complete category may supply a rational witness at a later target.
"""
import argparse
import itertools
import json
import time
from pathlib import Path

from sympy import Matrix


def f2_row_basis(rows):
    basis = {}
    for x in rows:
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                break
    return basis


def in_f2_span(x, basis):
    while x:
        p = x.bit_length() - 1
        if p not in basis:
            return False
        x ^= basis[p]
    return True


def analyze_target(n, edges, counts, hits, maxhits):
    full = (1 << n) - 1
    delta = [0] * (1 << n)
    for mask in range(1, full + 1):
        delta[mask] = 2 * mask.bit_count() - 3 * sum(mask & e == e for e in edges)
        if delta[mask] <= 0:
            return
    counts['positive_targets'] += 1
    mindelta = delta[:]
    strong = []
    for mask in range(full, -1, -1):
        larger = [mindelta[mask | (1 << v)] for v in range(n) if not mask >> v & 1]
        if not larger or delta[mask] < min(larger):
            strong.append(mask)
        if larger:
            mindelta[mask] = min(mindelta[mask], min(larger))
    strong = [s for s in strong if s]
    vertices = {s: tuple(v for v in range(n) if s >> v & 1) for s in strong}
    types = {}
    groups = {}
    for s in strong:
        vv = vertices[s]
        pos = {v: i for i, v in enumerate(vv)}
        et = tuple(sorted(tuple(pos[v] for v in range(n) if e >> v & 1)
                          for e in edges if e & s == e))
        typ = (len(vv), et)
        types[s] = typ
        groups.setdefault(typ, []).append(s)
    for qtype, qcopies in groups.items():
        if not qtype[1] or len(qcopies) < 3:
            continue
        q0 = qcopies[0]
        qp = {v: i for i, v in enumerate(vertices[q0])}
        pfamilies = {}
        for p0 in strong:
            if p0 & q0 == p0:
                pfamilies.setdefault(types[p0], []).append(tuple(qp[v] for v in vertices[p0]))
        for ptype, family in pfamilies.items():
            family.sort()
            if len(family) < 3:
                continue
            counts['tested_families_at_targets'] += 1
            pcopies = groups[ptype]
            pi = {s: i for i, s in enumerate(pcopies)}
            nr = (len(family) - 1) * len(pcopies)
            nc = len(qcopies)
            rows = [[0] * nc for _ in range(nr)]
            f2rows = [0] * nr
            for j, qmask in enumerate(qcopies):
                qv = vertices[qmask]
                images = [sum(1 << qv[k] for k in pp) for pp in family]
                assert all(s in pi for s in images)
                for i in range(1, len(family)):
                    a = (i - 1) * len(pcopies) + pi[images[i]]
                    b = (i - 1) * len(pcopies) + pi[images[0]]
                    rows[a][j] += 1
                    rows[b][j] -= 1
                    f2rows[a] ^= 1 << j
                    f2rows[b] ^= 1 << j
            if in_f2_span((1 << nc) - 1, f2_row_basis(f2rows)):
                continue
            counts['f2_affine_at_target'] += 1
            rows = [row for row in rows if any(row)]
            d = Matrix(rows) if rows else Matrix.zeros(0, nc)
            rank = d.rank()
            rank_aug = d.col_join(Matrix([[1] * nc])).rank()
            if rank_aug > rank:
                counts['also_rational_at_target'] += 1
                continue
            counts['exceptional_targets'] += 1
            hit = {
                'n': n,
                'edges': [[v for v in range(n) if e >> v & 1] for e in edges],
                'P_type': ptype,
                'Q_type': qtype,
                'family_P_subsets_in_Q': family,
                'Q_copies': [vertices[s] for s in qcopies],
                'P_copies': [vertices[s] for s in pcopies],
                'D': rows,
                'rank_Q': rank,
                'rank_aug_Q': rank_aug,
            }
            # Produce exact rational dual and a binary affine witness.
            solution, parameters = d.T.gauss_jordan_solve(Matrix.ones(nc, 1))
            zero = {p: 0 for p in parameters}
            hit['rational_dual'] = [str(x.subs(zero)) for x in solution]
            if nc <= 22:
                hit['f2_witness_mask'] = next(
                    t for t in range(1, 1 << nc)
                    if t.bit_count() % 2 and
                    all((t & r).bit_count() % 2 == 0 for r in f2rows))
            hits.append(hit)
            print('LOCAL_EXCEPTION', json.dumps(hit), flush=True)
            if len(hits) >= maxhits:
                raise StopIteration


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--nmax', type=int, default=7)
    ap.add_argument('--emax', type=int, default=3)
    ap.add_argument('--maxhits', type=int, default=10)
    ap.add_argument('--json', type=Path)
    args = ap.parse_args()
    counts = {k: 0 for k in ('enumerated_targets', 'positive_targets',
                            'tested_families_at_targets', 'f2_affine_at_target',
                            'also_rational_at_target', 'exceptional_targets')}
    hits = []
    start = time.monotonic()
    complete = True
    try:
        for n in range(1, args.nmax + 1):
            triples = [sum(1 << v for v in t) for t in itertools.combinations(range(n), 3)]
            for e in range(min(args.emax, (2*n - 1)//3, len(triples)) + 1):
                for edges in itertools.combinations(triples, e):
                    counts['enumerated_targets'] += 1
                    analyze_target(n, edges, counts, hits, args.maxhits)
            print('DONE_N', n, json.dumps(counts), flush=True)
    except StopIteration:
        complete = False
    report = dict(scope=vars(args) | {'json': str(args.json) if args.json else None},
                  complete=complete, counts=counts, hits=hits,
                  elapsed_seconds=round(time.monotonic()-start, 3),
                  caveat='Finite target only; no global exactness conclusion.')
    print('RESULT', json.dumps(report), flush=True)
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
