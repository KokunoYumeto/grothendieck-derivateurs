# Reviewer's own code (Claude Fable 5.2), 12 Nov 2026. Homology of finite posets (order complexes)
# with weak-point reduction; path posets F_tau(M;a,b) of a relative poset (M,Sigma), arbitrary verticals.
import itertools, sys
from fractions import Fraction

def reduce_poset(n, up, down):
    """up[i], down[i]: bitmasks of elements strictly above/below i. Remove weak points
    (strict up-set or strict down-set is a cone). Returns list of surviving elements."""
    alive = (1 << n) - 1
    changed = True
    comp = [up[i] | down[i] | (1 << i) for i in range(n)]
    while changed:
        changed = False
        for x in range(n):
            if not (alive >> x) & 1: continue
            for S in (up[x] & alive, down[x] & alive):
                if S == 0:
                    continue
                # is there y in S comparable to all of S ?
                T = S; ok = False
                while T:
                    y = (T & -T).bit_length() - 1
                    T &= T - 1
                    if S & ~comp[y] == 0:
                        ok = True; break
                if ok:
                    alive &= ~(1 << x); changed = True; break
    return [i for i in range(n) if (alive >> i) & 1]

def rank_mod_p(rows, p):
    """rows: list of dict col->val ; gaussian elimination mod p (sparse)."""
    piv = {}
    r = 0
    for row in rows:
        row = {c: v % p for c, v in row.items() if v % p}
        while row:
            c = min(row)
            if c in piv:
                pr = piv[c]; f = row[c]
                for cc, vv in pr.items():
                    nv = (row.get(cc, 0) - f * vv) % p
                    if nv: row[cc] = nv
                    else: row.pop(cc, None)
            else:
                inv = pow(row[c], p - 2, p)
                row = {cc: (vv * inv) % p for cc, vv in row.items()}
                piv[c] = row; r += 1
                break
    return r

def betti(n, up, maxdim=3, p=32003, reduce=True, down=None):
    """Betti numbers b_0..b_maxdim (mod p) of order complex of poset given by strict-up bitmasks."""
    if down is None:
        down = [0] * n
        for i in range(n):
            T = up[i]
            while T:
                j = (T & -T).bit_length() - 1; T &= T - 1
                down[j] |= 1 << i
    elems = reduce_poset(n, up, down) if reduce else list(range(n))
    aliveMask = 0
    for e in elems: aliveMask |= 1 << e
    # enumerate chains up to length maxdim+2
    chains = [[(e,) for e in elems]]
    for d in range(1, maxdim + 2):
        nxt = []
        for ch in chains[-1]:
            T = up[ch[-1]] & aliveMask
            while T:
                j = (T & -T).bit_length() - 1; T &= T - 1
                nxt.append(ch + (j,))
        chains.append(nxt)
        if not nxt: break
    while len(chains) < maxdim + 2: chains.append([])
    idx = [{c: i for i, c in enumerate(cs)} for cs in chains]
    ranks = [0]
    for d in range(1, maxdim + 2):
        rows = []
        for c in chains[d]:
            row = {}
            for k in range(d + 1):
                f = c[:k] + c[k + 1:]
                row[idx[d - 1][f]] = (-1) ** k
            rows.append(row)
        ranks.append(rank_mod_p(rows, p))
    b = []
    for d in range(0, maxdim + 1):
        b.append(len(chains[d]) - ranks[d] - ranks[d + 1])
    return b, len(elems), [len(c) for c in chains]

def path_poset(leq, sigma, tau, a, b):
    """objects: sequences c_0=a..c_n=b; '+' edge: c_{i-1}<=c_i ; '-' edge: c_i<=c_{i-1} with (c_i,c_{i-1}) in sigma.
    order: pointwise. returns (objs, up)"""
    m = len(leq); n = len(tau)
    objs = []
    def rec(seq):
        i = len(seq)
        if i == n + 1:
            if seq[-1] == b: objs.append(tuple(seq))
            return
        prev = seq[-1]
        for y in range(m):
            if tau[i - 1] == '+':
                ok = leq[prev][y]
            else:
                ok = leq[y][prev] and ((y, prev) in sigma)
            if ok:
                seq.append(y); rec(seq); seq.pop()
    if n == 0:
        return ([(a,)] if a == b else []), ([0] if a == b else [])
    rec([a])
    N = len(objs)
    up = [0] * N
    for i in range(N):
        ci = objs[i]
        for j in range(N):
            if i != j:
                cj = objs[j]
                if all(leq[x][y] for x, y in zip(ci, cj)):
                    up[i] |= 1 << j
    return objs, up
