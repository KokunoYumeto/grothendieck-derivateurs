"""Independent check of the explicit finite models of Part G (reviewer's code; python -I finite_models.py).

 - P_2 (5 elements) and P_3 (7 elements): associativity; integral homology of the normalized bar
   complex in low degrees (Smith normal form, sympy); exactness of the projective resolutions
   written in G.9 and G.10, checked as complexes of free abelian groups (Smith normal form).
 - R_2 (3 objects, 9 arrows): associativity and integral homology (Z, Z/2, 0, 0).
 - the join posets S^0 * ... * S^0 with 2n+2 objects: arrow count 2(n+1)^2 and homology of S^n.
"""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enum_small_categories import chains, boundary_rows, rank_mod
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def smith_diag(rows, ncols):
    if not rows or ncols == 0:
        return []
    M = Matrix(len(rows), ncols, lambda i, j: rows[i].get(j, 0))
    S = smith_normal_form(M, domain=ZZ)
    return [abs(S[i, i]) for i in range(min(S.shape)) if S[i, i] != 0]


def integral_homology(n, m, src, tgt, comp, kmax):
    """H_0..H_kmax of the normalized nerve as (free rank, torsion list)."""
    C = chains(n, m, src, tgt, kmax + 1)
    diag = {0: []}
    for k in range(1, kmax + 2):
        diag[k] = smith_diag(boundary_rows(n, m, src, tgt, comp, C, k), len(C[k - 1]))
    out = []
    for k in range(kmax + 1):
        rank = len(C[k]) - len(diag[k]) - len(diag[k + 1])
        out.append((rank, [d for d in diag[k + 1] if d != 1]))
    return out


def check_assoc(m, mul):
    for a in range(m):
        for b in range(m):
            for c in range(m):
                assert mul[mul[a][b]][c] == mul[a][mul[b][c]]


# ---------- P_2: 0 = identity, x_ij -> 1 + 2i + j ; x_ij x_kl = x_il
def x(i, j):
    return 1 + 2 * i + j

names2 = ['1', 'x00', 'x01', 'x10', 'x11']
mul2 = [[0] * 5 for _ in range(5)]
for a in range(5):
    mul2[0][a] = a
    mul2[a][0] = a
for i, j, k, l in itertools.product(range(2), repeat=4):
    mul2[x(i, j)][x(k, l)] = x(i, l)
check_assoc(5, mul2)

# ---------- P_3 = P_2 + {q=5, r=6}
mul3 = [[0] * 7 for _ in range(7)]
for a in range(7):
    mul3[0][a] = a
    mul3[a][0] = a
for i, j, k, l in itertools.product(range(2), repeat=4):
    mul3[x(i, j)][x(k, l)] = x(i, l)
Q, R = 5, 6
for i, j in itertools.product(range(2), repeat=2):
    mul3[x(i, j)][Q] = x(i, 0)
    mul3[x(i, j)][R] = x(i, 0)
    mul3[Q][x(i, j)] = x(i, j)
    mul3[R][x(i, j)] = x(i, j)
mul3[Q][Q] = Q; mul3[Q][R] = Q; mul3[R][R] = R; mul3[R][Q] = R
check_assoc(7, mul3)
print("P_2 (5 elements) and P_3 (7 elements): associative, identity 1: OK")


def monoid_as_category(mul):
    m = len(mul)
    # the answer writes products ab in the monoid; as a one-object category take g after f := g*f
    comp = {(g, f): mul[g][f] for g in range(m) for f in range(m)}
    return 1, m, [0] * m, [0] * m, comp

for name, mul, kmax, sphere in (("P_2", mul2, 4, 2), ("P_3", mul3, 3, 3)):
    n, m, src, tgt, comp = monoid_as_category(mul)
    H = integral_homology(n, m, src, tgt, comp, kmax)
    print(f"{name}: integral bar homology H_0..H_{kmax} (rank, torsion) = {H}")
    want = [(1, [])] + [(0, [])] * (sphere - 1) + [(1, [])] + [(0, [])] * (kmax - sphere)
    assert H == want
    # the opposite convention (g after f := f*g) gives the opposite monoid; same classifying space
    comp_op = {(g, f): mul[f][g] for g in range(m) for f in range(m)}
    assert integral_homology(1, m, src, tgt, comp_op, kmax) == want
    # all elements idempotent => universal group trivial => simply connected
    assert all(mul[a][a] == a for a in range(m))
print("P_2, P_3: all elements idempotent (pi_1 = 1); bar homology agrees with S^2, S^3 in the computed range: OK")


# ---------- the resolutions of G.9 and G.10 as complexes of free abelian groups
def right_mult_matrix(mul, basis_src, w):
    """matrix (rows = basis_src elements) of c -> c*w in Z[M], w = dict element->coeff; columns = all elements."""
    m = len(mul)
    rows = []
    for c in basis_src:
        row = {}
        for el, co in w.items():
            p = mul[c][el]
            row[p] = row.get(p, 0) + co
        rows.append(row)
    return rows


def exact_at(rows_in, rows_out, nmid):
    """rows_in: matrix of d_{k+1} into the middle group Z^nmid; rows_out: matrix of d_k out of it.
    Exactness over Z  <=>  d_k d_{k+1} = 0, rank d_{k+1} + rank d_k = nmid, and the image of d_{k+1}
    is saturated (all invariant factors of d_{k+1} equal 1)."""
    # composition zero
    for r in rows_in:
        acc = {}
        for j, cj in r.items():
            for l, cl in rows_out[j].items():
                acc[l] = acc.get(l, 0) + cj * cl
        assert all(v == 0 for v in acc.values()), "d d != 0"
    din = smith_diag(rows_in, nmid) if rows_in else []
    width = max([max(r) for r in rows_out if r] + [0]) + 1
    dout = smith_diag(rows_out, width) if rows_out else []
    return len(din) + len(dout) == nmid and all(d == 1 for d in din)


def restrict(rows, cols):
    """re-express rows (dict over all monoid elements) in the ordered basis `cols`; fail if outside."""
    idx = {c: i for i, c in enumerate(cols)}
    out = []
    for r in rows:
        assert all(k in idx for k, v in r.items() if v != 0), "image not in the stated module"
        out.append({idx[k]: v for k, v in r.items() if v != 0})
    return out

# G.9:  0 -> R x00 (+) R x01 --d2--> R --d1--> R x00 --eps--> Z -> 0
M2 = list(range(5))
Rx00 = [x(0, 0), x(1, 0)]         # abelian basis of R x00 (checked below)
Rx01 = [x(0, 1), x(1, 1)]
for a in M2:
    assert mul2[a][x(0, 0)] in Rx00 and mul2[a][x(0, 1)] in Rx01
d1 = restrict(right_mult_matrix(mul2, M2, {x(1, 0): 1, x(0, 0): -1}), Rx00)       # R -> R x00
d2 = [{c: 1} for c in Rx00] + [{c: 1} for c in Rx01]                                # inclusion sum into R (cols = elements)
eps = [{0: 1} for _ in Rx00]
ok = (exact_at(d1, eps, 2) and exact_at(d2, d1, 5) and len(smith_diag(d2, 5)) == 4
      and len(smith_diag(eps, 1)) == 1)
assert ok
print("G.9 resolution of Z over Z[P_2]: exact at every spot, d2 injective, eps onto: OK")

# G.10: 0 -> R x01 (+) R q --d3--> R x00 (+) R --d2--> R q --d1--> R x00 --eps--> Z -> 0
M3 = list(range(7))
Rq = [x(0, 0), x(1, 0), Q, R]
for a in M3:
    assert mul3[a][Q] in Rq and mul3[a][x(0, 0)] in Rx00 and mul3[a][x(0, 1)] in Rx01
d1 = restrict(right_mult_matrix(mul3, Rq, {x(1, 0): 1, x(0, 0): -1}), Rx00)         # R q -> R x00
# middle term basis: Rx00 (2) then R (7)
d2 = restrict([{c: 1} for c in Rx00], Rq) + restrict(right_mult_matrix(mul3, M3, {R: 1, Q: -1}), Rq)
# d3(c, d) = (0, c + d): source basis Rx01 (2) then Rq (4); target coordinates 2 + element index
d3 = [{2 + c: 1} for c in Rx01] + [{2 + c: 1} for c in Rq]
eps = [{0: 1} for _ in Rx00]
ok = (exact_at(d1, eps, 2) and exact_at(d2, d1, 4) and exact_at(d3, d2, 9)
      and len(smith_diag(d3, 9)) == 6 and len(smith_diag(eps, 1)) == 1)
assert ok
print("G.10 resolution of Z over Z[P_3]: exact at every spot, d3 injective, eps onto: OK")
print("   (projectivity of R x_ij and R q: images of the idempotent endomorphisms c -> c*x_ij, c -> c*q of R)")
for idem, mulx in ((x(0, 0), mul2), (x(0, 1), mul2), (x(0, 0), mul3), (x(0, 1), mul3), (Q, mul3)):
    assert mulx[idem][idem] == idem

# ---------- R_2: objects 0,1,2 ; Hom(i,j) = Z/2 for i<j
arrows = [(0, 0, 0), (1, 1, 0), (2, 2, 0)] + [(i, j, e) for i in range(3) for j in range(i + 1, 3) for e in range(2)]
idx = {a: k for k, a in enumerate(arrows)}
src = [a[0] for a in arrows]
tgt = [a[1] for a in arrows]
comp = {}
for g in arrows:
    for f in arrows:
        if f[1] == g[0]:
            comp[(idx[g], idx[f])] = idx[(f[0], g[1], (f[2] + g[2]) % 2 if f[0] != g[1] else 0)]
m = len(arrows)
for h in range(m):
    for g in range(m):
        for f in range(m):
            if tgt[f] == src[g] and tgt[g] == src[h]:
                assert comp[(comp[(h, g)], f)] == comp[(h, comp[(g, f)])]
H = integral_homology(3, m, src, tgt, comp, 3)
print(f"R_2: {m} arrows, 3 objects; integral homology H_0..H_3 = {H}")
assert H == [(1, []), (0, [2]), (0, []), (0, [])]
C = chains(3, m, src, tgt, 3)
print(f"   nondegenerate simplices by dimension: {[len(c) for c in C]} (dimension 2: nerve is a 2-complex; chi = {3-6+4})")

# ---------- join posets
for nn in (1, 2, 3):
    objs = [(lev, e) for lev in range(nn + 1) for e in range(2)]
    arr = [(a, a) for a in objs] + [(a, b) for a in objs for b in objs if a[0] < b[0]]
    idx = {a: k for k, a in enumerate(sorted(arr, key=lambda t: (t[0] != t[1], t)))}
    # identities first, in the order of objs
    order = [(a, a) for a in objs] + [t for t in arr if t[0] != t[1]]
    idx = {t: k for k, t in enumerate(order)}
    oi = {a: k for k, a in enumerate(objs)}
    src = [oi[t[0]] for t in order]
    tgt = [oi[t[1]] for t in order]
    comp = {(idx[g], idx[f]): idx[(f[0], g[1])] for g in order for f in order if f[1] == g[0]}
    assert len(objs) == 2 * nn + 2 and len(order) == 2 * (nn + 1) ** 2
    H = integral_homology(len(objs), len(order), src, tgt, comp, nn + 1)
    assert H == [(1, [])] + [(0, [])] * (nn - 1) + [(1, [])] + [(0, [])]
    print(f"join poset for S^{nn}: {len(objs)} objects, {len(order)} arrows, homology of S^{nn}: OK")
print("ALL MODEL CHECKS PASSED")
