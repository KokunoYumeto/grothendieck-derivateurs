# cup_products.py -- cup products in H^*(BM; F_p) for the 6-element monoid of Sweeney's Example 5.2 (with identity),
# computed in the normalized bar cochain complex.  Evidence for hunch H3 (is BM a wedge of spheres?).
import itertools, sys
import flint

# elements: 0 = 1, 1 = x00, 2 = x01, 3 = x10, 4 = x11, 5 = y ; x_ij x_kl = x_il ; y x_ij = x_0j ; x_ij y = x_i0 ; y y = x00
names = ["1", "x00", "x01", "x10", "x11", "y"]
def mul(a, b):
    if a == 0: return b
    if b == 0: return a
    ra = 0 if a == 5 else (a - 1) // 2          # row index of a (y behaves like x00)
    cb = 0 if b == 5 else (b - 1) % 2           # column index of b
    return 1 + 2 * ra + cb
T = [[mul(a, b) for b in range(6)] for a in range(6)]
for a in range(6):
    for b in range(6):
        for c in range(6):
            assert T[T[a][b]][c] == T[a][T[b][c]]
n = 6; m = 5
def index(c):
    r = 0
    for x in c: r = r * m + (x - 1)
    return r
def boundary_entries(deg):
    ent = {}
    for j, c in enumerate(itertools.product(range(1, n), repeat=deg)):
        def add(face, sign):
            i = index(face); ent[(i, j)] = ent.get((i, j), 0) + sign
        add(c[1:], 1)
        for i in range(1, deg):
            h = T[c[i - 1]][c[i]]
            if h != 0: add(c[:i - 1] + (h,) + c[i + 1:], (-1) ** i)
        add(c[:-1], (-1) ** deg)
    return ent
def coboundary(deg, p):
    """matrix of d^deg : C^deg -> C^{deg+1} (transpose of the boundary C_{deg+1} -> C_deg)"""
    ent = boundary_entries(deg + 1)
    A = flint.nmod_mat(m ** (deg + 1), m ** deg, p)
    for (i, j), v in ent.items():
        if v % p: A[j, i] = v % p
    return A
def col(v, p):
    A = flint.nmod_mat(len(v), 1, p)
    for i, x in enumerate(v):
        if x % p: A[i, 0] = x % p
    return A
def hstack(A, B, p):
    C = flint.nmod_mat(A.nrows(), A.ncols() + B.ncols(), p)
    for i in range(A.nrows()):
        for j in range(A.ncols()):
            if int(A[i, j]): C[i, j] = int(A[i, j])
        for j in range(B.ncols()):
            if int(B[i, j]): C[i, A.ncols() + j] = int(B[i, j])
    return C
def is_coboundary(z, deg, p, D):
    """is the cochain z in C^deg in the image of d^{deg-1}?"""
    A = D[deg - 1]
    return hstack(A, col(z, p), p).rank() == A.rank()
def generator(deg, p, D):
    """a cocycle in C^deg that is not a coboundary (H^deg is one-dimensional here)"""
    X, nullity = D[deg].nullspace()
    for k in range(nullity):
        z = [int(X[i, k]) for i in range(X.nrows())]
        if not is_coboundary(z, deg, p, D):
            return z
    return None
def cup(f, df, g, dg, p):
    out = [0] * (m ** (df + dg))
    for c in itertools.product(range(1, n), repeat=df + dg):
        a = f[index(c[:df])]
        if a:
            b = g[index(c[df:])]
            if b: out[index(c)] = (a * b) % p
    return out
res = []
for p in (2, 3, 32003):
    D = {k: coboundary(k, p) for k in range(1, 5)}
    betti = [m ** k - D[k].rank() - D[k - 1].rank() if k > 1 else m - D[1].rank() for k in range(1, 5)]
    x2 = generator(2, p, D); x3 = generator(3, p, D)
    c22 = cup(x2, 2, x2, 2, p)
    line = "p=%d: Betti b^1..b^4 = %s; x2^2 is a coboundary: %s" % (p, betti, is_coboundary(c22, 4, p, D))
    print(line, flush=True); res.append(line)
    D[5] = coboundary(5, p)
    c23 = cup(x2, 2, x3, 3, p); c32 = cup(x3, 3, x2, 2, p)
    line = "p=%d: x2.x3 is a coboundary: %s; x3.x2 is a coboundary: %s (H^5 has dimension %d)" % (
        p, is_coboundary(c23, 5, p, D), is_coboundary(c32, 5, p, D), m ** 5 - D[5].rank() - D[4].rank())
    print(line, flush=True); res.append(line)
open("cup_products.out", "w").write("\n".join(res) + "\n")
