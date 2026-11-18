"""Finite exploratory test for independently ordered F_2-vector spaces.

Tests whether normalized, isomorphism-invariant weights on natural orders
in dimension two extend to every reference order in dimension three.
This is a necessary finite consistency test, not a full exactness proof.
"""
from itertools import permutations
import numpy as np
import sympy as sp


def linmap(basis, x):
    y = 0
    for i, b in enumerate(basis):
        if (x >> i) & 1:
            y ^= b
    return y


def rref_mod(mat, p):
    a = np.array(mat, dtype=np.int64) % p
    pivots = []
    r = 0
    for c in range(a.shape[1]):
        possible = np.flatnonzero(a[r:, c])
        if not len(possible):
            continue
        z = r + int(possible[0])
        a[[r, z]] = a[[z, r]]
        a[r] = (a[r] * pow(int(a[r, c]), -1, p)) % p
        coeff = a[:, c].copy()
        coeff[r] = 0
        a = (a - coeff[:, None] * a[r]) % p
        pivots.append(c)
        r += 1
        if r == a.shape[0]:
            break
    return a, pivots


def null_mod(mat, p):
    a, piv = rref_mod(mat, p)
    free = [c for c in range(a.shape[1]) if c not in piv]
    out = []
    for c in free:
        v = np.zeros(a.shape[1], dtype=np.int64)
        v[c] = 1
        for i, z in enumerate(piv):
            v[z] = -a[i, c] % p
        out.append(v)
    return np.array(out, dtype=np.int64)


pts = tuple(range(1, 8))
nat = sorted({tuple(linmap(b, x) for x in pts)
              for b in permutations(pts, 3)
              if len({linmap(b, x) for x in pts}) == 7})
assert len(nat) == 168
planes = sorted({tuple(sorted((x, y, x ^ y)))
                 for x in pts for y in pts if x != y})
assert len(planes) == 7
perms3 = list(permutations(range(3)))
pindex = {v: i for i, v in enumerate(perms3)}
A = np.zeros((42, 168), dtype=np.int64)
for col, order in enumerate(nat):
    for i, plane in enumerate(planes):
        induced = tuple(plane.index(x) for x in order if x in plane)
        A[6*i+pindex[induced], col] = 1

seen = set()
refs = []
for order in permutations(pts):
    if order in seen:
        continue
    refs.append(order)
    for g in nat:
        seen.add(tuple(g[x-1] for x in order))
assert len(refs) == 30 and len(seen) == 5040

# Rows are natural orders of each labelled plane in its canonical labels;
# columns are the six weight types relative to its induced reference order.
Bs = []
for ref in refs:
    B = np.zeros((42, 6), dtype=np.int64)
    for i, plane in enumerate(planes):
        rp = tuple(x for x in ref if x in plane)
        for j, sigma in enumerate(perms3):
            natural = tuple(rp[z] for z in sigma)
            rowtype = tuple(plane.index(x) for x in natural)
            B[6*i+pindex[rowtype], j] = 1
    Bs.append(B)

print('F_2 vectors, dimensions 2 and 3')
print('natural orders:', len(nat), 'planes:', len(planes),
      'reference-order isomorphism types:', len(refs))
AT = sp.Matrix(A.T)
left = AT.nullspace()
print('Q marginal rank:', 42-len(left))
C = sp.Matrix.vstack(*(sp.Matrix.hstack(*left).T*sp.Matrix(B) for B in Bs))
system = C.col_join(sp.ones(1, 6))
rhs = sp.zeros(C.rows, 1).col_join(sp.ones(1, 1))
print('Q constraint rank:', C.rank(), 'normalized solutions:',
      sp.linsolve((system, rhs)))
for p in (2, 3, 5, 7, 11, 13):
    L = null_mod(A.T, p)
    C = np.vstack([L @ B % p for B in Bs])
    coeff = np.vstack((C, np.ones((1, 6), dtype=np.int64)))
    rhs = np.zeros((len(coeff), 1), dtype=np.int64)
    rhs[-1, 0] = 1
    aug = np.hstack((coeff, rhs))
    rr, piv = rref_mod(aug, p)
    inconsistent = any(not row[:6].any() and row[6] for row in rr)
    print('p=', p, 'marginal rank=', 42-len(L),
          'constraint rank=', len(rref_mod(C, p)[1]),
          'normalized consistent=', not inconsistent)
    if not inconsistent:
        v = np.zeros(6, dtype=np.int64)
        for i, col in enumerate(piv):
            if col < 6:
                v[col] = rr[i, 6]
        assert np.all(coeff @ v % p == rhs[:, 0])
        print('one normalized weight vector:', v.tolist())

L = null_mod(A.T, 2)
constraints = [L @ B % 2 for B in Bs]
def aug_in_span(C):
    return len(rref_mod(C, 2)[1]) == len(rref_mod(
        np.vstack((C, np.ones((1, 6), dtype=np.int64))), 2)[1])

selected = next(((i,) for i, C in enumerate(constraints) if aug_in_span(C)), None)
if selected is None:
    selected = next(((i,j) for i in range(30) for j in range(i+1,30)
                     if aug_in_span(np.vstack((constraints[i],constraints[j])))), None)
if selected is None:
    selected = tuple(range(30))
C = np.vstack([constraints[i] for i in selected])
rhs = np.ones((6, 1), dtype=np.int64)
rr, piv = rref_mod(np.hstack((C.T, rhs)), 2)
coef = np.zeros(C.shape[0], dtype=np.int64)
for i, col in enumerate(piv):
    if col < C.shape[0]:
        coef[col] = rr[i, -1]
assert np.array_equal(coef @ C % 2, np.ones(6, dtype=np.int64))
print('F2 contradiction reference types:', selected)
print('dimension2 permutations, 0-based:', perms3)
certificate = []
for j, ri in enumerate(selected):
    dual = coef[j*len(L):(j+1)*len(L)] @ L % 2
    if not dual.any():
        continue
    # Thirteen left-null generators give 8192 candidates; exhaustively
    # minimize the parity certificate, without relying on an optimizer.
    if len(selected) == 1:
        best = dual
        for mask in range(1 << len(L)):
            bits = np.array([(mask >> h) & 1 for h in range(len(L))])
            candidate = bits @ L % 2
            if int(candidate.sum()) < int(best.sum()) and np.array_equal(
                    candidate @ Bs[ri] % 2, np.ones(6, dtype=np.int64)):
                best = candidate
        dual = best
    assert not (dual @ A % 2).any()
    terms = []
    for row in np.flatnonzero(dual):
        plane = planes[row//6]
        sigma = perms3[row%6]
        terms.append(tuple(plane[k] for k in sigma))
    induced = (dual @ Bs[ri] % 2).tolist()
    certificate.append((refs[ri], terms, induced))
    print('reference order:', refs[ri])
    print('even-parity natural-plane-order events:', terms)
    print('induced coefficient vector on universal dim2 weights:', induced)
assert all(sum(induced[j] for _,_,induced in certificate) % 2 == 1
           for j in range(6))
print('F2 dual certificate verified: sum of zero parity expressions is augmentation.')
for order in nat:
    pos = {v:i for i,v in enumerate(order)}
    median = (pos[3] < pos[4] < pos[7]) or (pos[7] < pos[4] < pos[3])
    parity = ((pos[2] < pos[1]) + (pos[1] < pos[6])
              + (pos[2] < pos[5]) + (pos[5] < pos[6]) + median)
    assert parity % 2 == 0
for order in permutations((1,2,3)):
    pos = {v:i for i,v in enumerate(order)}
    median = (pos[1] < pos[2] < pos[3]) or (pos[3] < pos[2] < pos[1])
    assert ((pos[2] < pos[1]) + (pos[3] < pos[2]) + median) % 2 == 1
print('Simplified five-plane coordinate identity verified on all168 natural orders.')
print('Normalized contradiction verified on all six source natural orders.')
print('This finite calculation does not establish global coherence or Ramsey.')
