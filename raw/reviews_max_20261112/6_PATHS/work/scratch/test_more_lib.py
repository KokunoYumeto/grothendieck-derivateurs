import sys, time
sys.path.insert(0, sys.argv[1])
from posethom import *

def path_poset_fast(leq, sigma, tau, a, b):
    m = len(leq); n = len(tau)
    objs = []
    def rec(seq):
        i = len(seq)
        if i == n + 1:
            if seq[-1] == b: objs.append(tuple(seq))
            return
        prev = seq[-1]
        for y in range(m):
            ok = leq[prev][y] if tau[i - 1] == '+' else (leq[y][prev] and (y, prev) in sigma)
            if ok:
                seq.append(y); rec(seq); seq.pop()
    rec([a])
    N = len(objs)
    # mask[i][v] = objects with c_i = v ; geq[i][v] = objects with c_i >= v
    mask = [[0] * m for _ in range(n + 1)]
    for j, c in enumerate(objs):
        for i, v in enumerate(c): mask[i][v] |= 1 << j
    geq = [[0] * m for _ in range(n + 1)]
    for i in range(n + 1):
        for v in range(m):
            g = 0
            for y in range(m):
                if leq[v][y]: g |= mask[i][y]
            geq[i][v] = g
    up = []
    full = (1 << N) - 1
    for j, c in enumerate(objs):
        u = full
        for i, v in enumerate(c): u &= geq[i][v]
        up.append(u & ~(1 << j))
    return objs, up

def closure(leq, gens):
    m = len(leq)
    s = set(gens) | {(x, x) for x in range(m)}
    ch = True
    while ch:
        ch = False
        for (x, y) in list(s):
            for (y2, z) in list(s):
                if y == y2 and (x, z) not in s:
                    s.add((x, z)); ch = True
    return s

def run(name, leq, sig, pairs, ks, maxdim=2, types=None):
    print("==", name, "| marked non-identity arrows:", sorted(p for p in sig if p[0] != p[1]))
    for k in ks:
        tau = '+-' * k
        for (a, b) in pairs:
            t0 = time.time()
            objs, upp = path_poset_fast(leq, sig, tau, a, b)
            if not objs:
                print("  ", tau, (a, b), "empty"); continue
            bt, core, nch = betti(len(objs), upp, maxdim=maxdim)
            print("  ", tau, (a, b), "objects", len(objs), "core", core, "betti", bt, "t=%.1f" % (time.time() - t0), flush=True)

