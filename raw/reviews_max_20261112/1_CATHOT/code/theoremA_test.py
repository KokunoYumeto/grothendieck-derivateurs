# theoremA_test.py -- consistency tests (not a proof) of Ben-Bassat's Theorem A (arXiv:2610.38760v1, Definition 3.3):
# build M(Y,f) for the smallest cases and compare mod-p Betti numbers of BM(Y,f) with those of Cof(|f|).
import itertools, sys
import flint
from catlib import nerve_chains, boundary_matrix, check_category, homology, hom_str

def monotone_maps(j, k):
    """all weakly monotone maps [j] -> [k] as tuples of length j+1"""
    return [m for m in itertools.product(range(k + 1), repeat=j + 1) if all(m[i] <= m[i + 1] for i in range(j))]

def build_M(n, Yn, pull, edge_label, L_names, L_mul, L_one):
    """M(Y,f) = O_{n+1}^op + Y_n x L x {0..n}.  pull(theta, y) in Y_n for theta in O_{n+1};
    edge_label(y, i) = hol_i(y) in L (label of the edge from vertex i to vertex n)."""
    O = monotone_maps(n, n)
    ident = tuple(range(n + 1))
    elems = [("O", th) for th in O] + [("I", y, l, i) for y in Yn for l in L_names for i in range(n + 1)]
    # put the identity first
    elems.remove(("O", ident)); elems = [("O", ident)] + elems
    ix = {e: a for a, e in enumerate(elems)}
    def mul(a, b):
        if a[0] == "O" and b[0] == "O":
            th, ph = a[1], b[1]                   # theta^op phi^op = (phi o theta)^op
            return ("O", tuple(ph[th[x]] for x in range(n + 1)))
        if a[0] == "O" and b[0] == "I":
            th = a[1]; _, y, l, i = b
            return ("I", pull(th, y), L_mul[(edge_label(y, th[n]), l)], i)
        if a[0] == "I" and b[0] == "O":
            _, y, l, i = a; th = b[1]
            return ("I", y, l, th[i])
        _, y, l, i = a; _, y2, l2, i2 = b
        return ("I", y, L_mul[(L_mul[(l, edge_label(y2, i))], l2)], i2)
    N = len(elems)
    T = [[ix[mul(elems[a], elems[b])] for b in range(N)] for a in range(N)]
    # monoid axioms
    for a in range(N):
        assert T[0][a] == a and T[a][0] == a
    for a in range(N):
        for b in range(N):
            ab = T[a][b]
            for c in range(N):
                assert T[ab][c] == T[a][T[b][c]]
    return elems, T

def betti_mod_p(T, p, maxdeg):
    N = len(T)
    comp = T
    s = [0] * N; t = [0] * N
    chains = nerve_chains(N, 1, s, t, comp, maxdeg + 1)
    ranks = {}
    for d in range(1, maxdeg + 2):
        M = boundary_matrix(N, 1, s, t, comp, chains, d)
        A = flint.nmod_mat(len(M), len(M[0]), [x % p for r in M for x in r], p)
        ranks[d] = A.rank()
    return [len(chains[d]) - (ranks[d] if d >= 1 else 0) - ranks[d + 1] for d in range(1, maxdeg + 1)]

out = []
def say(x):
    print(x, flush=True); out.append(x)

# --- Y = Delta^1 / boundary, n = 1: Y_1 = {"*", "s"} ---
Y1 = ["*", "s"]
def pull1(th, y):
    return y if th == (0, 1) else "*"
C2 = {("1", "1"): "1", ("1", "g"): "g", ("g", "1"): "g", ("g", "g"): "1"}
triv = {("1", "1"): "1"}
for a in ("g", "1"):
    def lab(y, i, a=a):
        return a if (y == "s" and i == 0) else "1"
    el, T = build_M(1, Y1, pull1, lab, ["1", "g"], C2, "1")
    b2 = betti_mod_p(T, 2, 3); b3 = betti_mod_p(T, 3, 3)
    say("Example 3.2, f = f_%s: order %d; Betti numbers b_1..b_3 mod 2: %s, mod 3: %s" % (a, len(T), b2, b3))
    if a == "g":
        assert len(T) == 11 and b2 == [0, 1, 1] and b3 == [0, 1, 0]     # RP^inf/RP^1
        H = homology(len(T), 1, [0] * len(T), [0] * len(T), T, 2)
        say("   integral H_0..H_2 = %s  (expected for Cof(RP^1 -> RP^inf): Z, 0, Z)" % hom_str(H))
    else:
        assert len(T) == 11 and b2 == [1, 2, 1] and b3 == [0, 1, 0]     # BC_2 v S^2
# --- A_2 = M(S^1_Delta, *) with L trivial: order 7, expected S^2 ---
el, T = build_M(1, Y1, pull1, lambda y, i: "1", ["1"], triv, "1")
H = homology(len(T), 1, [0] * len(T), [0] * len(T), T, 3)
say("A_2 = M(S^1_Delta,*): order %d; integral H_0..H_3 = %s (expected S^2)" % (len(T), hom_str(H)))
assert len(T) == 7 and hom_str(H) == "(Z, 0, Z, 0)"
# --- A_3 = M(S^2_Delta, *): Y = Delta^2/boundary, n = 2: Y_2 = {"*", "top"}; order 10 + 3*2 = 16, expected S^3 ---
Y2 = ["*", "top"]
def pull2(th, y):
    return y if th == (0, 1, 2) else "*"
el, T = build_M(2, Y2, pull2, lambda y, i: "1", ["1"], triv, "1")
b2 = betti_mod_p(T, 2, 3); b3 = betti_mod_p(T, 3, 3)
say("A_3 = M(S^2_Delta,*): order %d; b_1..b_3 mod 2: %s, mod 3: %s (expected S^3: [0,0,1])" % (len(T), b2, b3))
assert len(T) == 16 and b2 == [0, 0, 1] and b3 == [0, 0, 1]
# --- Y = sk_2 N(C_2), L trivial, n = 2: Y_2 = C_2^2; order 10 + 3*4 = 22, expected Sigma RP^2 ---
Yc = [(x, y) for x in "1g" for y in "1g"]
def pullN(th, y):
    # 2-simplex (g1,g2) of N(C_2) = chain v0 -g1-> v1 -g2-> v2 ; pull back along th:[2]->[2]: new labels = products
    g = [y[0], y[1]]
    def seg(i, j):       # product of labels from vertex i to vertex j (i<=j)
        r = "1"
        for q in range(i, j): r = C2[(r, g[q])]
        return r
    return (seg(th[0], th[1]), seg(th[1], th[2]))
el, T = build_M(2, Yc, pullN, lambda y, i: "1", ["1"], triv, "1")
b2 = betti_mod_p(T, 2, 2); b3 = betti_mod_p(T, 3, 2)
say("M(sk_2 N(C_2),*): order %d; b_1,b_2 mod 2: %s, mod 3: %s (expected Sigma RP^2: mod 2 [0,1], mod 3 [0,0])" % (len(T), b2, b3))
assert len(T) == 22 and b2 == [0, 1] and b3 == [0, 0]
open("theoremA_test.out", "w").write("\n".join(out) + "\n")
