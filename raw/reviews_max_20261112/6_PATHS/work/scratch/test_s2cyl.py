import sys, time
sys.path.insert(0, sys.argv[1])
from posethom import *
from test_more_lib import path_poset_fast, closure
Y = [(i, e) for i in range(3) for e in range(2)]
yleq = lambda x, y: x == y or x[0] < y[0]
els = [(y, e) for e in range(2) for y in Y]
leq = [[yleq(x[0], y[0]) and x[1] <= y[1] for y in els] for x in els]
hor = [(i, j) for i, x in enumerate(els) for j, y in enumerate(els) if leq[i][j] and x[1] == y[1]]
sig = closure(leq, hor + [(0, 6)])
print("marked", len(sig), "of", sum(map(sum, leq)), "arrows (incl. identities)")
kmax = int(sys.argv[2])
for k in range(1, kmax + 1):
    tau = '+-' * k
    for (a, b) in [(0, 0), (0, 6), (6, 0), (6,6)]:
        t0 = time.time()
        objs, upp = path_poset_fast(leq, sig, tau, a, b)
        if not objs: print(tau, (a, b), "empty"); continue
        elems = reduce_poset(len(objs), upp, None) if False else None
        bt, core, nch = betti(len(objs), upp, maxdim=2)
        print(tau, (a, b), "objects", len(objs), "core", core, "chains", nch, "betti", bt, "t=%.1f" % (time.time() - t0), flush=True)
