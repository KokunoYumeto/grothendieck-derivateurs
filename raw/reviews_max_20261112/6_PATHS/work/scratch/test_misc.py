# Reviewer's own checks: (1) D.5: H_1 of the component of the constant map s in the poset X^Y;
# (2) A.6: existence of an augmentation-one integral combination t of injections [n]->[M] with t d^i independent of i.
import sys, itertools
sys.path.insert(0, sys.argv[1])
from posethom import *
# ---- (1) D.5
# X: Y = {r0,r1,q0,q1} (r_i<q_j) plus s,n above everything in Y ; index r0,r1,q0,q1,s,n = 0..5
def xleq(a, b):
    if a == b: return True
    if a in (0, 1) and b in (2, 3, 4, 5): return True
    if a in (2, 3) and b in (4, 5): return True
    return False
Yel = [0, 1, 2, 3]
funs = []
for vals in itertools.product(range(6), repeat=4):
    if all(xleq(vals[r], vals[q]) for r in (0, 1) for q in (2, 3)): funs.append(vals)
print("monotone maps Y->X:", len(funs))
N = len(funs)
up = [0] * N
for i in range(N):
    for j in range(N):
        if i != j and all(xleq(a, b) for a, b in zip(funs[i], funs[j])): up[i] |= 1 << j
b, core, nch = betti(N, up, maxdim=2)
print("X^Y: betti", b, "core", core)
# monotone maps from parallel-arrow category B=(a=>b) to poset X  = arrows of X
print("X^[1] objects:", sum(xleq(a, b) for a in range(6) for b in range(6)))
# component structure: H_0 of X^Y and which component contains const_s; H_1 total rank is of all components.
# ---- (2) A.6
from fractions import Fraction
def solve_int(n, M):
    inj = list(itertools.combinations(range(M + 1), n + 1))
    faces = list(itertools.combinations(range(M + 1), n))
    fidx = {f: i for i, f in enumerate(faces)}
    rows = []
    for i in range(n):          # t d^i - t d^{i+1} = 0
        for f in faces:
            row = [0] * len(inj)
            rows.append(row)
        base = len(rows) - len(faces)
        for k, g in enumerate(inj):
            a = g[:i] + g[i + 1:]; bb = g[:i + 1] + g[i + 2:]
            rows[base + fidx[a]][k] += 1
            rows[base + fidx[bb]][k] -= 1
    # integer solvability of rows*x=0, sum x = 1 : compute integer kernel lattice gcd of augmentation
    # kernel via column-style HNF: maintain basis of kernel lattice incrementally
    import math
    basis = [[1 if i == j else 0 for j in range(len(inj))] for i in range(len(inj))]
    for row in rows:
        vals = [sum(r * v for r, v in zip(row, bvec)) for bvec in basis]
        # reduce basis so that only one vector has nonzero val (euclid), then drop it
        while True:
            nz = [i for i, v in enumerate(vals) if v != 0]
            if len(nz) <= 1: break
            i0 = min(nz, key=lambda i: abs(vals[i]))
            for i in nz:
                if i != i0:
                    q = vals[i] // vals[i0]
                    if q:
                        basis[i] = [x - q * y for x, y in zip(basis[i], basis[i0])]
                        vals[i] -= q * vals[i0]
        if nz:
            basis.pop(nz[0])
    g = 0
    for bvec in basis: g = math.gcd(g, sum(bvec))
    return len(inj), len(basis), g
for n, M in [(1, 2), (1, 3), (2, 4), (2, 5), (2, 6)]:
    k, rk, g = solve_int(n, M)
    print("n=%d M=%d: injections %d, kernel rank %d, gcd of augmentations on kernel = %d -> %s" % (n, M, k, rk, g, "augmentation-one equalizing combination exists" if g == 1 else "none with augmentation one"))
