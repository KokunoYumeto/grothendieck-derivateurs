# catlib.py -- own code of the max-effort review (Claude Fable 5.2), 12 Nov 2026.
# Finite categories as "partial monoids": arrows 0..N-1, arrows 0..k-1 are the identities of
# objects 0..k-1, s[a], t[a] in 0..k-1, comp[g][f] = g after f (defined iff t[f] == s[g]), -1 otherwise.
import itertools
import numpy as np
from numba import njit
import flint

@njit(cache=True)
def _enum(N, k, s, t, maxsol):
    comp = -np.ones((N, N), dtype=np.int8)
    for f in range(N):
        comp[f, s[f]] = f      # f o id_{s f}
        comp[t[f], f] = f      # id_{t f} o f
    # unknown cells
    cells = np.zeros((N * N, 2), dtype=np.int64)
    nc = 0
    for g in range(k, N):
        for f in range(k, N):
            if t[f] == s[g]:
                cells[nc, 0] = g; cells[nc, 1] = f; nc += 1
    # candidate lists
    cand = -np.ones((nc, N), dtype=np.int64)
    ncand = np.zeros(nc, dtype=np.int64)
    for c in range(nc):
        g = cells[c, 0]; f = cells[c, 1]
        for h in range(N):
            if s[h] == s[f] and t[h] == t[g]:
                cand[c, ncand[c]] = h; ncand[c] += 1
    # triples (h,g,f) of non-identity arrows, f first
    trip = np.zeros((N * N * N, 3), dtype=np.int64)
    nt = 0
    for h in range(k, N):
        for g in range(k, N):
            if t[g] != s[h]:
                continue
            for f in range(k, N):
                if t[f] == s[g]:
                    trip[nt, 0] = h; trip[nt, 1] = g; trip[nt, 2] = f; nt += 1
    sols = np.zeros((maxsol, N, N), dtype=np.int8)
    nsol = 0
    nodes = 0
    if nc == 0:
        sols[0] = comp
        return sols, 1, 0
    idx = -np.ones(nc, dtype=np.int64)   # current candidate index per cell
    pos = 0
    while pos >= 0:
        idx[pos] += 1
        if idx[pos] >= ncand[pos]:
            idx[pos] = -1
            comp[cells[pos, 0], cells[pos, 1]] = -1
            pos -= 1
            continue
        comp[cells[pos, 0], cells[pos, 1]] = cand[pos, idx[pos]]
        nodes += 1
        ok = True
        for i in range(nt):
            h = trip[i, 0]; g = trip[i, 1]; f = trip[i, 2]
            a = comp[g, f]; b = comp[h, g]
            if a >= 0 and b >= 0:
                l = comp[h, a]; r = comp[b, f]
                if l >= 0 and r >= 0 and l != r:
                    ok = False
                    break
        if not ok:
            continue
        if pos == nc - 1:
            if nsol < maxsol:
                sols[nsol] = comp
            nsol += 1
        else:
            pos += 1
    return sols, nsol, nodes

def enum_tables(N, k, s, t, maxsol=400000):
    s = np.array(s, dtype=np.int64); t = np.array(t, dtype=np.int64)
    sols, nsol, nodes = _enum(N, k, s, t, maxsol)
    if nsol > maxsol:
        raise RuntimeError("maxsol too small: %d" % nsol)
    return sols[:nsol].copy(), nodes

def check_category(N, k, s, t, comp):
    """Full independent check of the category axioms (pure Python)."""
    for f in range(N):
        assert comp[f][s[f]] == f and comp[t[f]][f] == f
    for g in range(N):
        for f in range(N):
            c = comp[g][f]
            if t[f] == s[g]:
                assert c >= 0 and s[c] == s[f] and t[c] == t[g]
            else:
                assert c == -1
    for h in range(N):
        for g in range(N):
            if t[g] != s[h]: continue
            for f in range(N):
                if t[f] != s[g]: continue
                assert comp[h][comp[g][f]] == comp[comp[h][g]][f]
    return True

def nerve_chains(N, k, s, t, comp, maxdeg):
    """Nondegenerate simplices of the nerve up to degree maxdeg: tuples (f1,...,fn) of
    non-identity arrows, f1 first, t[f_i] == s[f_{i+1}].  Degree 0: objects."""
    chains = [[(o,) for o in range(k)]]
    nonid = list(range(k, N))
    cur = [(f,) for f in nonid]
    chains.append(cur)
    for n in range(2, maxdeg + 1):
        nxt = []
        for c in cur:
            last = c[-1]
            for f in nonid:
                if s[f] == t[last]:
                    nxt.append(c + (f,))
        chains.append(nxt)
        cur = nxt
    return chains

def boundary_matrix(N, k, s, t, comp, chains, n):
    """Matrix of d_n: C_n -> C_{n-1} (rows = (n-1)-simplices, cols = n-simplices), normalized."""
    rows = {c: i for i, c in enumerate(chains[n - 1])}
    cols = chains[n]
    M = [[0] * len(cols) for _ in range(len(rows))]
    for j, c in enumerate(cols):
        if n == 1:
            f = c[0]
            M[rows[(t[f],)]][j] += 1
            M[rows[(s[f],)]][j] -= 1
            continue
        # d_0: drop first arrow
        M[rows[c[1:]]][j] += 1
        # d_i, 0<i<n: compose f_i and f_{i+1}
        for i in range(1, n):
            h = comp[c[i]][c[i - 1]]
            if h >= k:
                face = c[:i - 1] + (int(h),) + c[i + 1:]
                M[rows[face]][j] += (-1) ** i
        # d_n: drop last arrow
        M[rows[c[:-1]]][j] += (-1) ** n
    return M

def snf_diag(M):
    if len(M) == 0 or len(M[0]) == 0:
        return []
    A = flint.fmpz_mat(len(M), len(M[0]), [x for row in M for x in row])
    S = A.snf()
    r = min(S.nrows(), S.ncols())
    return [abs(int(S[i, i])) for i in range(r) if int(S[i, i]) != 0]

def homology(N, k, s, t, comp, maxdeg):
    """Integral homology H_0..H_maxdeg of the nerve as list of (free rank, torsion list)."""
    chains = nerve_chains(N, k, s, t, comp, maxdeg + 1)
    diags = {}
    for n in range(1, maxdeg + 2):
        if len(chains[n]) == 0:
            diags[n] = []
        else:
            diags[n] = snf_diag(boundary_matrix(N, k, s, t, comp, chains, n))
    out = []
    for n in range(0, maxdeg + 1):
        rk_n = len(diags[n]) if n >= 1 else 0
        rk_n1 = len(diags[n + 1])
        free = len(chains[n]) - rk_n - rk_n1
        tors = sorted(d for d in diags[n + 1] if d > 1)
        out.append((free, tuple(tors)))
    return out

def hom_str(H):
    def one(h):
        free, tors = h
        parts = []
        if free == 1: parts.append("Z")
        elif free > 1: parts.append("Z^%d" % free)
        parts += ["Z/%d" % d for d in tors]
        return "+".join(parts) if parts else "0"
    return "(" + ", ".join(one(h) for h in H) + ")"

def monoid_as_category(table):
    """table: n x n list, element 0 = identity, table[a][b] = a*b.  As one-object category with
    comp[g][f] = g after f := g*f (the classifying space does not depend on this convention up to homeo)."""
    n = len(table)
    comp = [[table[g][f] for f in range(n)] for g in range(n)]
    return n, 1, [0] * n, [0] * n, comp
