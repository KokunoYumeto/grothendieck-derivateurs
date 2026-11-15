# models_check.py -- own verification of the explicit small models (review of CATHOT G.9-G.11 and e-mail claim (g)).
import itertools, sys
from catlib import *

def cat_from_arrows(k, arrows, compfun):
    """arrows: list of (name, src, tgt) for non-identity arrows; compfun(g,f) -> name of g o f or ('id', obj)."""
    names = ["id%d" % i for i in range(k)] + [a[0] for a in arrows]
    N = len(names)
    s = list(range(k)) + [a[1] for a in arrows]
    t = list(range(k)) + [a[2] for a in arrows]
    ix = {n: i for i, n in enumerate(names)}
    comp = [[-1] * N for _ in range(N)]
    for g in range(N):
        for f in range(N):
            if t[f] != s[g]: continue
            if f < k: comp[g][f] = g
            elif g < k: comp[g][f] = f
            else: comp[g][f] = ix[compfun(names[g], names[f])]
    check_category(N, k, s, t, comp)
    return N, k, s, t, comp, names

out = []
def report(label, C, maxdeg):
    N, k, s, t, comp = C[:5]
    H = homology(N, k, s, t, comp, maxdeg)
    line = "%-46s objects=%d arrows=%d  H_0..H_%d = %s" % (label, k, N, maxdeg, hom_str(H))
    print(line, flush=True); out.append(line)
    return H

# 1. two parallel arrows: S^1
C = cat_from_arrows(2, [("a", 0, 1), ("b", 0, 1)], None)
report("parallel pair 0 => 1 (S^1)", C, 3)

# 2. Grothendieck's Z (XII app. ms. 10-11): objects 0,a,b,c; lam,mu:0->a; beta:a->b; gamma:a->c; beta.lam=beta.mu, gamma.lam=gamma.mu
def compZ(g, f):
    if g == "beta" and f in ("lam", "mu"): return "bl"
    if g == "gamma" and f in ("lam", "mu"): return "gl"
    raise KeyError((g, f))
C = cat_from_arrows(4, [("lam", 0, 1), ("mu", 0, 1), ("beta", 1, 2), ("gamma", 1, 3), ("bl", 0, 2), ("gl", 0, 3)], compZ)
report("Grothendieck's Z, XIIapp ms.10-11 (S^2)", C, 4)

# 3. R_2: objects 0,1,2; Hom(i,j)=Z/2 for i<j; composition = addition mod 2
arr = [("%d%d_%d" % (i, j, e), i, j) for (i, j) in [(0, 1), (1, 2), (0, 2)] for e in (0, 1)]
def compR(g, f):
    eg = int(g[-1]); ef = int(f[-1])
    return "02_%d" % ((eg + ef) % 2)
R2 = cat_from_arrows(3, arr, compR)
H = report("R_2: 3 objects, Hom(i,j)=Z/2 (RP^2)", R2, 4)
# surface check: each nondegenerate edge lies in exactly two nondegenerate triangles; vertex links are circles
N, k, s, t, comp, names = R2
ch = nerve_chains(N, k, s, t, comp, 3)
assert len(ch[3]) == 0, "R_2 has no nondegenerate 3-simplices"
edges = ch[1]; tris = ch[2]
inc = {e: 0 for e in edges}
tri_edges = {}
for (f, g) in tris:
    es = [(g,), (int(comp[g][f]),), (f,)]
    tri_edges[(f, g)] = es
    for e in es: inc[e] += 1
assert all(v == 2 for v in inc.values())
line = "   R_2: %d vertices, %d edges, %d triangles, Euler characteristic %d; every edge in exactly 2 triangles" % (k, len(edges), len(tris), k - len(edges) + len(tris))
print(line); out.append(line)
# vertex links: graph on (edge-ends at v), one link-edge per triangle corner at v; check each link is a single cycle
import networkx as nx
for v in range(k):
    G = nx.MultiGraph()
    for (f, g), es in tri_edges.items():
        verts = [s[f], t[f], t[g]]           # vertices 0,1,2 of the triangle; edges: d0=(g) joins v1,v2; d1 joins v0,v2; d2=(f) joins v0,v1
        opp = {0: es[0], 1: es[1], 2: es[2]}   # edge opposite to vertex i
        for i in range(3):
            if verts[i] == v:
                a, b = [opp[j] for j in range(3) if j != i]
                G.add_edge(a, b)
    assert nx.is_connected(G) and all(d == 2 for _, d in G.degree()), "link not a circle"
line = "   R_2: every vertex link is a single cycle => BR_2 is a closed connected surface with chi=1, H_1=Z/2 => RP^2"
print(line); out.append(line)

# 4. P_2 = {1} + 2x2 rectangular band
def band_table():
    names = ["1"] + ["x%d%d" % (i, j) for i in (0, 1) for j in (0, 1)]
    ix = {n: i for i, n in enumerate(names)}
    n = len(names)
    T = [[0] * n for _ in range(n)]
    for a in names:
        for b in names:
            if a == "1": c = b
            elif b == "1": c = a
            else: c = "x%s%s" % (a[1], b[2])
            T[ix[a]][ix[b]] = ix[c]
    return names, T
names2, T2 = band_table()
C = monoid_as_category(T2); check_category(*C)
report("P_2 = 1 + 2x2 rectangular band (S^2)", C, 4)

# 5. P_3 = P_2 + {q, r}
def p3_table():
    names = ["1"] + ["x%d%d" % (i, j) for i in (0, 1) for j in (0, 1)] + ["q", "r"]
    ix = {n: i for i, n in enumerate(names)}
    n = len(names)
    T = [[0] * n for _ in range(n)]
    for a in names:
        for b in names:
            if a == "1": c = b
            elif b == "1": c = a
            elif a[0] == "x" and b[0] == "x": c = "x%s%s" % (a[1], b[2])
            elif a[0] == "x": c = "x%s0" % a[1]          # x_ij q = x_ij r = x_i0
            elif b[0] == "x": c = b                        # q x = r x = x
            else: c = a                                    # q^2=qr=q, r^2=rq=r
            T[ix[a]][ix[b]] = ix[c]
    return names, T
names3, T3 = p3_table()
C = monoid_as_category(T3); check_category(*C)
report("P_3 = P_2 + {q,r} (S^3)", C, 3)
# opposite monoid has the same classifying space; check as a consistency test
T3op = [[T3[b][a] for b in range(7)] for a in range(7)]
C = monoid_as_category(T3op); check_category(*C)
report("P_3 opposite", C, 3)

# 6. C_2
C = monoid_as_category([[0, 1], [1, 0]]); check_category(*C)
report("C_2 (RP^infinity)", C, 6)

open("models_check.out", "w").write("\n".join(out) + "\n")
