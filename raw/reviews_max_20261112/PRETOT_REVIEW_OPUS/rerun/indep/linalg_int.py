"""Exact integer linear algebra for the PRETOT review (pure Python, no SymPy).

Smith normal form by elementary row/column operations over Z, determinant and
inverse by fraction-free / Fraction elimination.  Written by Claude Opus 5.5,
12 Nov 2026, independently of the return's code.
"""
from fractions import Fraction


def smith_diagonal(rows, ncols):
    """Nonzero invariant factors of an integer matrix given as a list of row lists."""
    A = [list(r) for r in rows]
    m = len(A)
    n = ncols
    diag = []
    r = 0
    c = 0
    # work on the submatrix A[r:, c:]
    while r < m and c < n:
        # find a nonzero entry of minimal absolute value in the submatrix
        best = None
        for i in range(r, m):
            Ai = A[i]
            for j in range(c, n):
                v = Ai[j]
                if v and (best is None or abs(v) < best[0]):
                    best = (abs(v), i, j)
                    if best[0] == 1:
                        break
            if best and best[0] == 1:
                break
        if best is None:
            break
        _, i, j = best
        A[r], A[i] = A[i], A[r]
        for row in A:
            row[c], row[j] = row[j], row[c]
        while True:
            p = A[r][c]
            done = True
            # clear column c
            for i in range(r + 1, m):
                if A[i][c]:
                    q = A[i][c] // p
                    if q:
                        Ar, Ai = A[r], A[i]
                        for j in range(c, n):
                            if Ar[j]:
                                Ai[j] -= q * Ar[j]
                    if A[i][c]:
                        done = False
            # clear row r
            for j in range(c + 1, n):
                if A[r][j]:
                    q = A[r][j] // p
                    if q:
                        for i in range(r, m):
                            if A[i][c]:
                                A[i][j] -= q * A[i][c]
                    if A[r][j]:
                        done = False
            if done:
                # divisibility condition: p must divide every remaining entry
                bad = None
                for i in range(r + 1, m):
                    for j in range(c + 1, n):
                        if A[i][j] % p:
                            bad = (i, j)
                            break
                    if bad:
                        break
                if bad is None:
                    break
                i, j = bad
                for jj in range(c, n):
                    A[r][jj] += A[i][jj]
                continue
            # move the smallest nonzero entry of row r / column c to the pivot
            best = (abs(p), r, c)
            for i in range(r + 1, m):
                if A[i][c] and abs(A[i][c]) < best[0]:
                    best = (abs(A[i][c]), i, c)
            for j in range(c + 1, n):
                if A[r][j] and abs(A[r][j]) < best[0]:
                    best = (abs(A[r][j]), r, j)
            _, i, j = best
            if i != r:
                A[r], A[i] = A[i], A[r]
            if j != c:
                for row in A:
                    row[c], row[j] = row[j], row[c]
        diag.append(abs(A[r][c]))
        r += 1
        c += 1
    return diag


def homology_from_boundaries(dims, boundaries):
    """dims[k] = rank of C_k; boundaries[k] = rows of d_k: C_k -> C_{k-1} (k >= 1),
    given as a (dims[k-1] x dims[k]) list of rows.  Returns [(free rank, torsion)]."""
    inv = {}
    for k, B in boundaries.items():
        inv[k] = smith_diagonal(B, dims[k]) if dims[k] and dims[k - 1] else []
    out = []
    for k in range(len(dims)):
        rk_out = len(inv.get(k, []))          # rank of d_k
        rk_in = len(inv.get(k + 1, []))       # rank of d_{k+1}
        free = dims[k] - rk_out - rk_in
        tors = [x for x in inv.get(k + 1, []) if x > 1]
        out.append((free, tors))
    return out


def det_int(M):
    """Exact determinant of a square integer matrix (Bareiss)."""
    A = [list(r) for r in M]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k]), None)
            if sw is None:
                return 0
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def inverse_int(M):
    """Inverse of a unimodular integer matrix, checked to be integral."""
    n = len(M)
    A = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[c])]
    inv = [[A[i][n + j] for j in range(n)] for i in range(n)]
    assert all(x.denominator == 1 for row in inv for x in row), 'inverse not integral'
    return [[int(x) for x in row] for row in inv]
