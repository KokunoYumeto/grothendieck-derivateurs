# enum_monoids.py -- own exhaustive enumeration of all monoids of order n (labelled, identity = element 0),
# reduction to isomorphism/anti-isomorphism classes, and exact (H_1,H_2,H_3) of the classifying space.
import sys, itertools, time, json
import numpy as np
from catlib import *

def canon_classes(tabs):
    """tabs: array (m, n, n) of multiplication tables with identity 0.  Returns dict canonical-bytes -> index of a
    representative, classes up to isomorphism and anti-isomorphism (BM and B(M^op) are homeomorphic)."""
    m, n, _ = tabs.shape
    best = None
    for anti in (False, True):
        base = tabs.transpose(0, 2, 1) if anti else tabs
        for p in itertools.permutations(range(1, n)):
            perm = np.array((0,) + p, dtype=np.int64)       # new label of old element
            inv = np.argsort(perm)
            # new table: T'[perm[a]][perm[b]] = perm[T[a][b]]  <=>  T'[x][y] = perm[T[inv[x]][inv[y]]]
            newt = perm[base[:, inv][:, :, inv]]
            flat = newt.reshape(m, n * n).astype(np.uint8)
            if best is None:
                best = flat.copy()
            else:
                # lexicographic minimum row-wise
                diff = flat != best
                first = diff.argmax(axis=1)
                has = diff.any(axis=1)
                rows = np.arange(m)
                less = has & (flat[rows, first] < best[rows, first])
                best[less] = flat[less]
    reps = {}
    for i in range(m):
        key = best[i].tobytes()
        if key not in reps:
            reps[key] = i
    return reps, best

def main(nmax):
    summary = {}
    for n in range(1, nmax + 1):
        t0 = time.time()
        tabs, nodes = enum_tables(n, 1, [0] * n, [0] * n, maxsol=400000)
        m = len(tabs)
        reps, best = canon_classes(tabs.astype(np.int64))
        # isomorphism classes only (no anti): recount
        t1 = time.time()
        triples = {}
        examples = {}
        for key, i in reps.items():
            T = tabs[i].tolist()
            H = homology(n, 1, [0] * n, [0] * n, T, 3)
            tr = hom_str(H[1:4])
            triples[tr] = triples.get(tr, 0) + 1
            examples.setdefault(tr, T)
        t2 = time.time()
        print("order %d: %d labelled monoids (identity fixed), %d search nodes, %d classes up to iso+anti-iso; enumeration %.1fs, homology %.1fs"
              % (n, m, nodes, len(reps), t1 - t0, t2 - t1), flush=True)
        for tr in sorted(triples):
            print("    (H1,H2,H3) = %-28s : %d classes" % (tr, triples[tr]), flush=True)
        summary[n] = {"labelled": m, "classes_iso_anti": len(reps), "triples": triples, "examples": examples}
    json.dump(summary, open("enum_monoids_upto%d.json" % nmax, "w"), indent=0)

if __name__ == "__main__":
    main(int(sys.argv[1]))
