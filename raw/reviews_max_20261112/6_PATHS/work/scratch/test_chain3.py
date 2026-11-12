import sys, time
sys.path.insert(0, sys.argv[1])
from posethom import *
# M=[2], Sigma = identities + (0->2). Localization = walking retract: A=0~2, B=1; i:A->B, r:B->A, ri=1.
leq = [[x <= y for y in range(3)] for x in range(3)]
sig = {(0, 0), (1, 1), (2, 2), (0, 2)}
# expected pi_0 Map_L(a,b): rows a, cols b  (A=0, B=1, A=2)
expected = {(0,0):1,(0,1):1,(0,2):1,(1,0):1,(1,1):2,(1,2):1,(2,0):1,(2,1):1,(2,2):1}
for k in range(1, 6):
    tau = '+-' * k
    out = []
    for a in range(3):
        for b in range(3):
            objs, upp = path_poset(leq, sig, tau, a, b)
            if not objs:
                out.append(((a, b), 'empty')); continue
            bt, core, nch = betti(len(objs), upp, maxdim=3)
            out.append(((a, b), len(objs), core, bt))
    print(tau)
    for o in out: print("   ", o, "expected b0", expected[o[0]])
    sys.stdout.flush()
