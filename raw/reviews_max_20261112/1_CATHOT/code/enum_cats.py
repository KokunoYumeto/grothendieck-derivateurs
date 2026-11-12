# enum_cats.py -- own exhaustive enumeration of all finite categories with k >= 2 objects and N arrows
# (identities counted), connected, with exact integral homology H_1..H_3 of the nerve.
# No reduction by isomorphism except: the non-identity arrows are listed in non-decreasing order of (source,target).
import sys, itertools, time, json
import numpy as np
import networkx as nx
from catlib import *

def assignments(k, m):
    pairs = [(i, j) for i in range(k) for j in range(k)]
    for combo in itertools.combinations_with_replacement(range(len(pairs)), m):
        yield [pairs[c] for c in combo]

def connected(k, st):
    G = nx.Graph(); G.add_nodes_from(range(k))
    for (i, j) in st: G.add_edge(i, j)
    return nx.is_connected(G)

def main(Nmax, kmin=2):
    res = {}
    for N in range(2, Nmax + 1):
        for k in range(kmin, N + 1):
            m = N - k
            t0 = time.time()
            ncat = 0; trip = {}; ex = {}
            for st in assignments(k, m):
                if not connected(k, st): continue
                s = list(range(k)) + [p[0] for p in st]
                t = list(range(k)) + [p[1] for p in st]
                tabs, nodes = enum_tables(N, k, s, t, maxsol=2000000)
                for T in tabs:
                    ncat += 1
                    Tl = T.tolist()
                    H = homology(N, k, s, t, Tl, 3)
                    key = hom_str(H[1:4])
                    trip[key] = trip.get(key, 0) + 1
                    if key not in ex or len(ex[key]) < 12: ex.setdefault(key, []).append({"s": s, "t": t, "comp": Tl})
            if ncat:
                print("N=%d arrows, k=%d objects: %d connected labelled categories (%.1fs)" % (N, k, ncat, time.time() - t0), flush=True)
                for key in sorted(trip):
                    print("     (H1,H2,H3) = %-22s : %d" % (key, trip[key]), flush=True)
            res["%d,%d" % (N, k)] = {"count": ncat, "triples": trip, "examples": ex}
    json.dump(res, open("enum_cats_upto%d.json" % Nmax, "w"))

if __name__ == "__main__":
    main(int(sys.argv[1]))
