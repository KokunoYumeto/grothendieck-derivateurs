"""Check the input of TOTEX Proposition C.3: for every object T of the repaired K1, the full down-set
D_T = {X : K1(X,T) nonempty} has H_2(El_{D_T}(H|D_T)) = 0 for H = h_V/(c v_1 ~ c v_2).
Also lists, for every object of K1, the homology of El over its down-set.  Own code (akr_indep.py)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import akr_indep as A

def restrict(C, keep):
    D = A.Cat(); old = {}
    for x in sorted(keep):                       # keep V=0 and W=1 first so object numbers 0,1 stay V, W
        old[x] = D.add(C.name[x], C.size[x])
    D.hom.clear()
    for (x, y), fs in C.hom.items():
        if x in keep and y in keep: D.hom[(old[x], old[y])] = set(fs)
    return D

C = A.Cat(); A.stage_K1(C)
n = len(C.size)
for T in range(n):
    keep = {X for X in range(n) if C.hom.get((X, T))}     # the full down-set D_T (contains T)
    if 0 not in keep:
        print(f"{C.name[T]:>12}: D_T = {sorted(keep)} contains no V, so H|D_T is empty"); continue
    D = restrict(C, keep)                                    # V stays object 0; W is object 1 iff W in D_T
    counts, bds = A.element_nerve(D, [(0, 1)] if 1 in keep else [])
    b = A.betti(counts, bds, 1000003); b2 = A.betti(counts, bds, 2)
    print(f"{C.name[T]:>12}: down-set size {len(keep)}, Betti F_p {b}, F_2 {b2}")
