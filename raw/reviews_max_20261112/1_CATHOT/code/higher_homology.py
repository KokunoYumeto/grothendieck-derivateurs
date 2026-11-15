# higher_homology.py -- mod-p Betti numbers of BM in higher degrees via the normalized bar complex (sparse fill, flint ranks)
import sys, itertools, time, json
import numpy as np
import flint

def bar_rank(T, n, deg, p):
    """rank mod p of d_deg: C_deg -> C_{deg-1} of the normalized bar complex of the monoid with table T (identity 0)."""
    m = n - 1                      # non-identity elements 1..n-1
    ncols = m ** deg; nrows = m ** (deg - 1) if deg > 1 else 1
    A = flint.nmod_mat(nrows, ncols, p)
    if deg == 1:
        return 0                   # d_1 = 0 for a monoid (one object)
    def index(c):
        r = 0
        for x in c: r = r * m + (x - 1)
        return r
    ent = {}
    for j, c in enumerate(itertools.product(range(1, n), repeat=deg)):
        def add(face, sign):
            i = index(face)
            ent[(i, j)] = ent.get((i, j), 0) + sign
        add(c[1:], 1)
        for i in range(1, deg):
            h = T[c[i - 1]][c[i]]          # product of consecutive entries (bar convention)
            if h != 0:
                add(c[:i - 1] + (h,) + c[i + 1:], (-1) ** i)
        add(c[:-1], (-1) ** deg)
    for (i, j), v in ent.items():
        if v % p: A[i, j] = v % p
    return A.rank()

def betti(T, maxdeg, p):
    n = len(T); m = n - 1
    ranks = {d: bar_rank(T, n, d, p) for d in range(1, maxdeg + 2)}
    return [m ** d - ranks[d] - ranks[d + 1] for d in range(1, maxdeg + 1)]

if __name__ == "__main__":
    order = int(sys.argv[1]); maxdeg = int(sys.argv[2])
    tabs = np.load("monoid_classes_order%d.npy" % order)
    primes = [2, 3, 5, 32003]
    out = []
    for idx, T in enumerate(tabs):
        T = T.tolist()
        b = betti(T, 2, 32003)
        b2 = betti(T, 2, 2)
        if b[0] == 0 and b2[0] == 0 and (b[1] > 0 or b2[1] > 0):      # H_1 = 0 mod 2 and rationally, H_2 nonzero
            t0 = time.time()
            res = {p: betti(T, maxdeg, p) for p in primes}
            line = "class %d  table %s\n     Betti b_1..b_%d: " % (idx, T, maxdeg) + "; ".join("p=%d: %s" % (p, res[p]) for p in primes) + "  (%.0fs)" % (time.time() - t0)
            print(line, flush=True); out.append(line)
    open("higher_homology_order%d.out" % order, "w").write("\n".join(out) + "\n")
