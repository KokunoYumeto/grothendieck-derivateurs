import sys, time
sys.path.insert(0, sys.argv[1])
from posethom import *
# six-object S^2 poset: elements (i,eps), i in 0..2, eps in 0,1 ; (i,e)<(j,d) iff i<j
els = [(i, e) for i in range(3) for e in range(2)]
leq = [[(x == y) or (x[0] < y[0]) for y in els] for x in els]
allsig = {(x, y) for x in range(6) for y in range(6) if leq[x][y]}
# sanity: the poset itself is S^2
up = [sum(1 << j for j in range(6) if leq[i][j] and i != j) for i in range(6)]
print("Y itself betti", betti(6, up, maxdim=3))
for base in (0, 4):
    for k in range(1, 4):
        tau = '+-' * k
        t0 = time.time()
        objs, upp = path_poset(leq, allsig, tau, base, base)
        b, core, nch = betti(len(objs), upp, maxdim=3)
        print("base", els[base], "tau", tau, "objects", len(objs), "core", core, "chains", nch, "betti", b, "t=%.1fs" % (time.time() - t0), flush=True)
