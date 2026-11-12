#!/usr/bin/env python3
"""Independent exact reader of the finite projectivity certificate.

Does not import or execute its generating program. Uses only Python integer
arithmetic and the two JSON certificates delivered with PRETOT.
"""
from pathlib import Path
import json
from itertools import product

SCRIPT = Path(__file__).resolve()
DATA = SCRIPT.parent / 'outputs'
# The delivered JSON certificates live next to the programs under outputs/.
# Run main_counterexample.py first if rebuilding them from the construction.
d = json.loads((DATA / 'main_counterexample_data.json').read_text())
c = json.loads((DATA / 'projectivity_certificate.json').read_text())
M = [tuple(x) for x in d['monoid_elements']]
H = [(k, x, tuple(r)) for k, x, r in d['H_elements']]
assert M == [tuple(x) for x in c['basis_M']]
assert H == [(k, x, tuple(r)) for k, x, r in c['basis_H']]
mul, act = d['multiplication'], d['right_action']
unit = d['identity_index']
for g, f in product(range(10), repeat=2):
    assert M[mul[g][f]] == tuple(M[g][j] for j in M[f])
for g, f, e in product(range(10), repeat=3):
    assert mul[mul[g][f]][e] == mul[g][mul[f][e]]
for h, g, f in product(range(52), range(10), range(10)):
    assert act[act[h][g]][f] == act[h][mul[g][f]]
for h in range(52):
    assert act[h][unit] == h
    k, name, rho = H[h]
    for a in range(10):
        q = tuple(rho[j] for j in M[a])
        support = tuple(sorted(set(q)))
        face = name
        for j in reversed(range(k+1)):
            if j not in support:
                face = d['faces'][face][j]
        normalized = (len(support)-1, face,
                      tuple(support.index(j) for j in q))
        assert H[act[h][a]] == normalized

def dense(s):
    a = [[0]*s['cols'] for _ in range(s['rows'])]
    seen = set()
    for i,j,v in s['entries']:
        assert type(v) is int and (i,j) not in seen
        seen.add((i,j)); a[i][j] = v
    return a

S, R = dense(c['inclusion_S']), dense(c['retraction_R'])
assert len(S) == 180 and len(S[0]) == 52
assert len(R) == 52 and len(R[0]) == 180
for i,j in product(range(52), repeat=2):
    assert sum(R[i][k]*S[k][j] for k in range(180)) == int(i==j)
for a in range(10):
    free = [10*k+mul[g][a] for k in range(18) for g in range(10)]
    for j in range(52):
        image = [0]*180
        for k in range(180): image[free[k]] += S[k][j]
        assert image == [S[k][act[j][a]] for k in range(180)]
    for j in range(180):
        image = [0]*52
        for k in range(52): image[act[k][a]] += R[k][j]
        assert image == [R[k][free[j]] for k in range(52)]
report = ('Independent certificate audit: PASS\n'
          '10-element monoid: all 100 products and 1000 associativity cases verified.\n'
          '52-element right action: all 5200 action laws and 520 independently reconstructed pulls verified.\n'
          'Integer matrices S:180x52, R:52x180: all 2704 entries of RS=I verified.\n'
          'All 10 equivariance identities for each of S and R verified.\n'
          'Conclusion: Z[H] is a retract of the free right Z[M]-module of rank 18.\n')
print(report, end='')
(DATA/'independent_certificate_audit.out').write_text(report)
