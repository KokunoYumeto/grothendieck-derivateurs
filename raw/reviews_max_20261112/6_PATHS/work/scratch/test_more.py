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

which = sys.argv[2]
# crown Z: 0,2 minimal; 1,3 maximal; 0<1,0<3,2<1,2<3
Z = [[x == y or (x % 2 == 0 and y % 2 == 1) for y in range(4)] for x in range(4)]
if which == 'crown3':
    # three of four edges marked: localization = B N (free monoid on one generator): Map(0,0) = N discrete
    sig = closure(Z, [(0, 3), (2, 1), (2, 3)])
    run("crown, edges 0<3, 2<1, 2<3 marked (0<1 unmarked): expect Map_L(0,0)=N discrete", Z, sig, [(0, 0), (1, 1), (0, 1), (1, 0)], [1, 2, 3, 4, 5])
if which == 'crownall':
    sig = closure(Z, [(0, 1), (0, 3), (2, 1), (2, 3)])
    run("crown, all marked: expect Z discrete", Z, sig, [(0, 0), (1, 1)], [1, 2, 3, 4, 5])
if which == 'cyl':
    # M = Z x [1]; element (z,e) -> index 2*z+e? use z + 4*e
    els = [(z, e) for e in range(2) for z in range(4)]
    leq = [[Z[x[0]][y[0]] and x[1] <= y[1] for y in els] for x in els]
    hor = [(i, j) for i, x in enumerate(els) for j, y in enumerate(els) if leq[i][j] and x[1] == y[1]]
    sig1 = closure(leq, hor)
    run("Z x [1], horizontal marked: L = S^1 x [1]; Map((0,0),(0,1)) = Z discrete; Map((0,1),(0,0)) empty", leq, sig1, [(0, 4), (0, 0), (4, 0)], [1, 2, 3, 4])
    sig2 = closure(leq, hor + [(0, 4)])
    print("   closure size", len(sig2), "of", sum(map(sum, leq)))
    run("Z x [1], horizontal + one vertical (0,0)->(0,1) marked (proper subset): L = S^1 groupoid; all Map = Z discrete", leq, sig2, [(0, 4), (0, 0), (4, 0), (4, 4)], [1, 2, 3, 4])
