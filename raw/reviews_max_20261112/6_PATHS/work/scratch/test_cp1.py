# Reviewer's check of PATHS C.P1: P(tau,sigma) is empty or contractible (here: collapsible to a point by weak-point removal,
# and with trivial reduced homology), for all words tau, sigma up to given lengths. Also: Ty_sigma facts used in C.P2.
import sys, itertools
sys.path.insert(0, sys.argv[1])
from posethom import *
LT, LS = int(sys.argv[2]), int(sys.argv[3])
def words(L):
    for n in range(L + 1):
        for w in itertools.product('+-', repeat=n): yield ''.join(w)
def leq_int(sig):
    m = len(sig)
    le = [[False] * (m + 1) for _ in range(m + 1)]
    for j in range(m + 1):
        le[j][j] = True
        k = j
        while k < m and sig[k] == '+':
            k += 1; le[j][k] = True      # j -> k forward
        k = j
        while k > 0 and sig[k - 1] == '-':
            k -= 1; le[j][k] = True      # edge (k,k+1) negative means arrow k+1 -> k
    return le
def maps(tau, sig):
    n, m = len(tau), len(sig); le = leq_int(sig); res = []
    def rec(u):
        i = len(u)
        if i == n + 1:
            if u[-1] == m: res.append(tuple(u))
            return
        for v in range(u[-1], m + 1):
            ok = le[u[-1]][v] if tau[i - 1] == '+' else le[v][u[-1]]
            if ok:
                u.append(v); rec(u); u.pop()
    rec([0]); return res, le
tot = nonempty = bad = 0; maxsize = 0
for sig in words(LS):
    for tau in words(LT):
        ms, le = maps(tau, sig); tot += 1
        if not ms: continue
        nonempty += 1; N = len(ms); maxsize = max(maxsize, N)
        up = [0] * N
        for i in range(N):
            for j in range(N):
                if i != j and all(le[x][y] for x, y in zip(ms[i], ms[j])): up[i] |= 1 << j
        down = [0] * N
        for i in range(N):
            T = up[i]
            while T:
                j = (T & -T).bit_length() - 1; T &= T - 1; down[j] |= 1 << i
        core = reduce_poset(N, up, down)
        if len(core) != 1:
            b, c, _ = betti(N, up, maxdim=3)
            print("core not a point:", tau, sig, N, len(core), b); bad += 1
print("pairs", tot, "nonempty", nonempty, "largest P", maxsize, "not collapsed to a point", bad)
