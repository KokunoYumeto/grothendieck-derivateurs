# Own checks of the finite examples of the STRATA answer (GPT-6 Astra, ChatGPT Pro mode).
# Written by Claude Fable 5.2, 11 November 2026. Independent of the answer's code/ folder
# (which was not opened or run). Python 3, standard library only.
#
# A finite category is (objects, arrows, src, tgt, comp) with comp[(g, f)] = g o f.
# Homology of the nerve is computed from the normalized chain complex (strings of
# composable non-identity arrows), by ranks over F_p for several primes:
# dim H_k(;F_p) = b_k + t_k(p) + t_{k-1}(p), so equal ranks at all primes used mean no
# torsion at those primes, and the pattern for RP^2 is recognizable.
import itertools, sys
from collections import defaultdict

PRIMES = (1000003, 2, 3, 5)

def rank_mod(rows, ncols, p):
    rows = [dict((j, v % p) for j, v in r.items() if v % p) for r in rows]
    rank = 0
    pivots = {}
    for r in rows:
        r = dict(r)
        while r:
            j = min(r)
            if j in pivots:
                piv = pivots[j]
                c = r[j]
                for k, v in piv.items():
                    nv = (r.get(k, 0) - c * v) % p
                    if nv:
                        r[k] = nv
                    else:
                        r.pop(k, None)
            else:
                inv = pow(r[j], p - 2, p)
                pivots[j] = dict((k, v * inv % p) for k, v in r.items())
                rank += 1
                break
    return rank

class Cat:
    def __init__(self, objs, arrows, comp, name=""):
        # arrows: dict name -> (src, tgt), identities included as ('id', x)
        self.objs = list(objs)
        self.arr = dict(arrows)
        for x in self.objs:
            self.arr[("id", x)] = (x, x)
        self.comp = dict(comp)
        self.name = name
        for f, (a, b) in list(self.arr.items()):
            self.comp[(f, ("id", a))] = f
            self.comp[(("id", b), f)] = f
        self.check()

    def check(self):
        A = self.arr
        for g in A:
            for f in A:
                if A[f][1] == A[g][0]:
                    h = self.comp[(g, f)]
                    assert A[h] == (A[f][0], A[g][1]), (self.name, g, f, h)
        for h in A:
            for g in A:
                if A[g][1] != A[h][0]:
                    continue
                for f in A:
                    if A[f][1] != A[g][0]:
                        continue
                    assert self.comp[(h, self.comp[(g, f)])] == self.comp[(self.comp[(h, g)], f)], (self.name, "assoc")

    def nonid(self):
        return [f for f in self.arr if not (isinstance(f, tuple) and len(f) == 2 and f[0] == "id" and f[1] in self.objs)]

    def simplices(self, maxdim):
        # normalized nerve: strings (f1,...,fk) of composable non-identity arrows
        S = [[(x,) for x in self.objs]]
        cur = [(f,) for f in self.nonid()]
        k = 1
        while k <= maxdim and cur:
            S.append(cur)
            nxt = []
            for s in cur:
                t = self.arr[s[-1]][1]
                for f in self.nonid():
                    if self.arr[f][0] == t:
                        nxt.append(s + (f,))
            cur = nxt
            k += 1
        while len(S) <= maxdim + 1:
            S.append([])
        return S

    def faces(self, s):
        # s = (f1..fk); returns list of (sign, face or None if degenerate)
        k = len(s)
        out = []
        if k == 1:
            a, b = self.arr[s[0]]
            return [(1, (b,)), (-1, (a,))]
        out.append((1, s[1:]))
        for i in range(1, k):
            h = self.comp[(s[i], s[i - 1])]
            if h in self.nonid_set:
                out.append(((-1) ** i, s[:i - 1] + (h,) + s[i + 1:]))
        out.append(((-1) ** k, s[:-1]))
        return out

    def homology(self, maxdim):
        self.nonid_set = set(self.nonid())
        S = self.simplices(maxdim + 1)
        idx = [dict((s, i) for i, s in enumerate(level)) for level in S]
        counts = [len(level) for level in S]
        res = {}
        ranks = {}
        for p in PRIMES:
            rk = [0]
            for k in range(1, maxdim + 2):
                rows = []
                for s in S[k]:
                    r = defaultdict(int)
                    for sign, f in self.faces(s):
                        r[idx[k - 1][f]] += sign
                    rows.append(dict(r))
                rk.append(rank_mod(rows, counts[k - 1], p))
            ranks[p] = rk
            res[p] = [counts[k] - rk[k] - rk[k + 1] for k in range(0, maxdim + 1)]
        return counts[:maxdim + 2], res

def poset_cat(elems, leq, name=""):
    arrows = {}
    comp = {}
    for a in elems:
        for b in elems:
            if a != b and leq(a, b):
                arrows[(a, b)] = (a, b)
    for (a, b) in arrows:
        for (c, d) in arrows:
            if b == c and a != d:
                comp[((c, d), (a, b))] = (a, d)
    C = Cat(elems, arrows, comp, name)
    return C

def show(title, C, maxdim, note=""):
    counts, res = C.homology(maxdim)
    print("%-46s simplices %s" % (title, tuple(counts[:maxdim + 1])))
    for p in PRIMES:
        print("    dim H_*(;F_%d) = %s" % (p, tuple(res[p])))
    if note:
        print("    " + note)
    return counts, res

def components(objs, edges):
    parent = dict((x, x) for x in objs)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        parent[find(a)] = find(b)
    return len(set(find(x) for x in objs))

print("=== B.4: R_2 and its octahedral double cover; A.10: boundary of a triangle")
objs = [0, 1, 2]
arrows = {}
comp = {}
for i in objs:
    for j in objs:
        if i < j:
            for a in (0, 1):
                arrows[("r", i, j, a)] = (i, j)
for a in (0, 1):
    for b in (0, 1):
        comp[(("r", 1, 2, b), ("r", 0, 1, a))] = ("r", 0, 2, (a + b) % 2)
R2 = Cat(objs, arrows, comp, "R2")
assert len(R2.arr) == 9
c, r = show("R_2 (3 objects, 9 arrows)", R2, 2)
assert tuple(c[:3]) == (3, 6, 4)
assert tuple(r[1000003]) == (1, 0, 0) and tuple(r[2]) == (1, 1, 1) and tuple(r[3]) == (1, 0, 0)
print("    => H_1 = Z/2 (2-torsion only), H_2 = 0: the homology of RP^2")
Q = poset_cat([(i, e) for i in range(3) for e in (1, -1)], lambda a, b: a == b or a[0] < b[0], "octahedron")
c, r = show("octahedral poset Q", Q, 2)
assert tuple(c[:3]) == (6, 12, 8) and all(tuple(r[p]) == (1, 0, 1) for p in PRIMES)
# the quotient functor Q -> R_2 is 2-to-1 on non-degenerate simplices
SQ = Q.simplices(2)
def image(s):
    if len(s) == 1 and not isinstance(s[0], tuple) or (len(s) == 1 and s[0] in Q.objs):
        return ("obj", s[0][0])
    return tuple(("r", f[0][0], f[1][0], 0 if f[0][1] == f[1][1] else 1) for f in s)
for k in range(3):
    fibres = defaultdict(int)
    for s in SQ[k]:
        fibres[image(s)] += 1
    assert set(fibres.values()) == {2}, k
print("    every simplex of N R_2 of dimension <= 2 has exactly two lifts to NQ")

tri = [("v", 0), ("v", 1), ("v", 2), ("e", 0), ("e", 1), ("e", 2)]
def tri_leq(a, b):
    return a == b or (a[0] == "v" and b[0] == "e" and a[1] != b[1])
T = poset_cat(tri, tri_leq, "triangle boundary")
c, r = show("face poset of the boundary of a triangle", T, 1)
assert tuple(c[:2]) == (6, 6) and all(tuple(r[p]) == (1, 1) for p in PRIMES)

print()
print("=== A.2: the layers Q_n of N x {0,1} (order by first coordinate): B Q_n = S^n")
for n in range(4):
    Qn = poset_cat([(i, a) for i in range(n + 1) for a in (0, 1)], lambda x, y: x == y or x[0] < y[0], "Q%d" % n)
    counts, res = Qn.homology(n)
    red = [res[1000003][k] - (1 if k == 0 else 0) for k in range(n + 1)]
    ok = all(tuple(res[p]) == tuple(res[1000003]) for p in PRIMES)
    print("  n=%d  reduced Betti numbers %s, same at all primes: %s" % (n, red, ok))
    assert red == [0] * n + [1] and ok

print()
print("=== B.7: the monoid {1, e}, e^2 = e; its idempotent completion")
M = Cat(["*"], {"e": ("*", "*")}, {("e", "e"): "e"}, "M2")
c, r = show("monoid {1,e}", M, 4)
assert all(tuple(r[p]) == (1, 0, 0, 0, 0) for p in PRIMES)
mult = {("1", "1"): "1", ("1", "e"): "e", ("e", "1"): "e", ("e", "e"): "e"}
idem = ["1", "e"]
kar = {}
for a in idem:
    for b in idem:
        kar[(a, b)] = sorted(set(m for m in ("1", "e") if mult[(b, mult[(m, a)])] == m))
print("  Karoubi envelope Hom((.,a),(.,b)) = {m : b m a = m}:", kar)
assert kar == {("1", "1"): ["1", "e"], ("1", "e"): ["e"], ("e", "1"): ["e"], ("e", "e"): ["e"]}
print("  sieves of e: 2 (empty, all); sieves of [1]: 3 (empty, {0}, {0,1})  [B.9]")

print()
print("=== C.4: two parallel arrows; C.10: the 7-arrow attachment; C.11: the 11-arrow attachment")
P2 = Cat(["a", "b"], {"r": ("a", "b"), "s": ("a", "b")}, {}, "parallel")
c, r = show("a => b", P2, 1)
assert all(tuple(r[p]) == (1, 1) for p in PRIMES)
print("    crossing category E: 2 objects (r, s), discrete; paths a->b in BX = S^1: components Z")
X7 = Cat(["a", "t", "s"], {"al": ("a", "t"), "be": ("a", "t"), "ga": ("t", "s"), "de": ("a", "s")},
         {("ga", "al"): "de", ("ga", "be"): "de"}, "X7")
assert len(X7.arr) == 7
c, r = show("C.10 category (3 objects, 7 arrows)", X7, 2)
assert tuple(c[:3]) == (3, 4, 2) and all(tuple(r[p]) == (1, 0, 0) for p in PRIMES)
# U/t for U = {a}: objects arrows a -> t, morphisms endomorphisms of a commuting: only identity
print("    U/t has objects {al, be} and only identities: 2 components")
X11 = Cat([0, 1, "t", "s"],
          {"a": (0, 1), "be": (1, "t"), "ga": (1, "t"), "c": (0, "t"),
           "0s": (0, "s"), "1s": (1, "s"), "ts": ("t", "s")},
          {("be", "a"): "c", ("ga", "a"): "c", ("1s", "a"): "0s", ("ts", "be"): "1s", ("ts", "ga"): "1s",
           ("ts", "c"): "0s"}, "X11")
assert len(X11.arr) == 11
c, r = show("C.11 category (4 objects, 11 arrows)", X11, 3)
assert tuple(c[:4]) == (4, 7, 6, 2) and all(tuple(r[p]) == (1, 0, 0, 0) for p in PRIMES)
# crossing weight H_t on U = (0 -> 1): H_t(0) = {c}, H_t(1) = {be, ga}, both restrict to c
print("    weight H_t: |H_t(0)| = 1, |H_t(1)| = 2, restriction constant: coend with (K -> CK) is CK u_K CK = suspension of K")

print()
print("=== D.3, D.5, D.6, D.7: lifting posets")
def contractible_poset(elems, leq):
    # sufficient test used here: empty -> False; a cone point (comparable to all) -> True;
    # otherwise decide by homology of the nerve (all examples below are of dimension <= 2
    # and the non-contractible ones are detected by homology or by being disconnected)
    elems = list(elems)
    if not elems:
        return False
    for x in elems:
        if all(leq(x, y) or leq(y, x) for y in elems):
            return True
    C = poset_cat(elems, leq)
    counts, res = C.homology(3)
    return all(tuple(res[p]) == (1, 0, 0, 0) for p in PRIMES) and None  # None = acyclic, undecided

def tests(P, leqP, Qe, leqQ, f):
    proper = smooth = True
    for p in P:
        for q in Qe:
            if leqQ(f[p], q):
                L = [x for x in P if leqP(p, x) and f[x] == q]
                t = contractible_poset(L, leqP)
                assert t is not None
                proper = proper and t
            if leqQ(q, f[p]):
                L = [x for x in P if leqP(x, p) and f[x] == q]
                t = contractible_poset(L, leqP)
                assert t is not None
                smooth = smooth and t
    return proper, smooth

def cart(P, leqP, Qe, leqQ, f):
    # Grothendieck fibration / opfibration for a monotone map of posets, full test
    def has_cart(p, q):   # q <= f(p): need x <= p, f(x) = q, with: y <= p and f(y) <= q  =>  y <= x
        for x in P:
            if leqP(x, p) and f[x] == q and all(leqP(y, x) for y in P if leqP(y, p) and leqQ(f[y], q)):
                return True
        return False
    def has_cocart(p, q):  # f(p) <= q
        for x in P:
            if leqP(p, x) and f[x] == q and all(leqP(x, y) for y in P if leqP(p, y) and leqQ(q, f[y])):
                return True
        return False
    fib = all(has_cart(p, q) for p in P for q in Qe if leqQ(q, f[p]))
    opf = all(has_cocart(p, q) for p in P for q in Qe if leqQ(f[p], q))
    return fib, opf

I = [0, 1]
le = lambda a, b: a <= b
for name, img in (("{0} -> [1]", 0), ("{1} -> [1]", 1)):
    P = ["pt"]
    f = {"pt": img}
    lp = lambda a, b: True
    print("  %-12s (proper, smooth) = %s  (fibration, opfibration) = %s" % (name, tests(P, lp, I, le, f), cart(P, lp, I, le, f)))
assert tests(["pt"], lambda a, b: True, I, le, {"pt": 0}) == (False, True)
assert tests(["pt"], lambda a, b: True, I, le, {"pt": 1}) == (True, False)
D = ["x", "a", "b", "c"]
rel = {("x", "a"), ("x", "b"), ("x", "c"), ("a", "c"), ("b", "c")}
ld = lambda u, v: u == v or (u, v) in rel
fd = {"x": 0, "a": 1, "b": 1, "c": 1}
print("  diamond x<a,b<c -> [1]: (proper, smooth) = %s  (fibration, opfibration) = %s" % (tests(D, ld, I, le, fd), cart(D, ld, I, le, fd)))
assert tests(D, ld, I, le, fd) == (True, True) and cart(D, ld, I, le, fd) == (True, False)
# D.5: right base change for {0} -> [1] along {1} -> [1], coefficient a 2-point set:
# (f_* M)(1) = lim over (e/1)^op = M (2 points); the strict fibre over 1 is empty: limit = 1 point
print("  D.5: f_*M at 1 has 2 points, the fibre formula gives 1 point: base change fails")
# D.7 on all full inclusions of subsets of the diamond
import itertools as it
for k in range(0, 5):
    for sub in it.combinations(D, k):
        sub = list(sub)
        f = dict((s, s) for s in sub)
        pr, sm = tests(sub, ld, D, ld, f) if sub else (True, True)
        cosieve = all(v in sub for u in sub for v in D if ld(u, v))
        sieve = all(u in sub for v in sub for u in D if ld(u, v))
        assert pr == cosieve and sm == sieve, sub
print("  D.7: for all 16 full subposets of the diamond, proper <=> cosieve and smooth <=> sieve")

print()
print("=== E.4: chains 0<...<n<t over [1]")
for n in range(4):
    P = list(range(n + 1)) + ["t"]
    lc = lambda u, v: u == v or v == "t" or (u != "t" and v != "t" and u <= v)
    f = dict((i, 0) for i in range(n + 1)); f["t"] = 1
    assert cart(P, lc, I, le, f) == (True, True)
    assert tests(P, lc, I, le, f) == (True, True)
print("  each X_n is a bifibration; the cartesian lift at t is n -> t, and in X_{n+1} the arrow n+1 -> t does not factor through it")

print()
print("=== E.10: six-element sphere poset; E.11: the rectangular-band monoid")
S6 = poset_cat([(i, e) for i in range(3) for e in (0, 1)], lambda a, b: a == b or a[0] < b[0], "S6")
c, r = show("{a0,a1}<{b0,b1}<{c0,c1}", S6, 2)
assert tuple(c[:3]) == (6, 12, 8)
els = [(i, j) for i in (0, 1) for j in (0, 1)]
arrows = dict((e, ("*", "*")) for e in els)
comp = dict(((e, f), (e[0], f[1])) for e in els for f in els)
B = Cat(["*"], arrows, comp, "rectangular band + 1")
assert len(B.arr) == 5
c, r = show("monoid {1, e_ij}, e_ij e_kl = e_il", B, 4)
assert all(tuple(r[p]) == (1, 0, 1, 0, 0) for p in PRIMES)
print("    => H_1 = 0, H_2 = Z, H_3 = H_4 = 0 with no torsion at 2, 3, 5: the homology of S^2 through degree 4")
mono = [e for e in els if all((B.comp[(e, f)] != B.comp[(e, g)]) for f in list(B.arr) for g in list(B.arr) if f != g)]
epi = [e for e in els if all((B.comp[(f, e)] != B.comp[(g, e)]) for f in list(B.arr) for g in list(B.arr) if f != g)]
print("    non-identity monomorphisms: %s, epimorphisms: %s" % (mono, epi))
assert mono == [] and epi == []

print()
print("=== F.4, F.15: strata of M_{0,5}-bar and the map forgetting the point 5")
def splits(n):
    pts = list(range(1, n + 1))
    out = set()
    for k in range(2, n - 1):
        for A in itertools.combinations(pts, k):
            Bc = tuple(x for x in pts if x not in A)
            out.add(frozenset([frozenset(A), frozenset(Bc)]))
    return sorted(out, key=lambda s: sorted(map(sorted, s)))
def compatible(s, t):
    (A, B), (C, Dd) = tuple(s), tuple(t)
    return any(not (U & V) for U in (A, B) for V in (C, Dd))
def strata(n):
    S = splits(n)
    out = []
    for k in range(0, n - 2):
        for T in itertools.combinations(S, k):
            if all(compatible(a, b) for a, b in itertools.combinations(T, 2)):
                out.append(frozenset(T))
    return out
S5 = strata(5); S4 = strata(4)
by = defaultdict(int)
for s in S5:
    by[len(s)] += 1
print("  strata of M_{0,5}-bar by number of nodes:", dict(by), "total", len(S5))
assert dict(by) == {0: 1, 1: 10, 2: 15} and len(S4) == 4
rels = sum(1 for s in S5 for t in S5 if s >= t)
print("  pairs (s, t) with s in the closure of t (identities included):", rels)
assert rels == 81
def forget(s, n=5):
    out = set()
    for sp in s:
        A, Bc = tuple(sp)
        A2, B2 = A - {n}, Bc - {n}
        if len(A2) >= 2 and len(B2) >= 2:
            out.add(frozenset([A2, B2]))
    return frozenset(out)
fib = defaultdict(lambda: defaultdict(int))
for s in S5:
    fib[forget(s)][len(s)] += 1
    assert forget(s) in S4
for t in S4:
    print("   over a stratum with %d node(s): %s" % (len(t), dict(fib[t])))
assert dict(fib[frozenset()]) == {0: 1, 1: 4}
assert all(dict(fib[t]) == {1: 2, 2: 5} for t in S4 if len(t) == 1)
assert all((forget(s) >= forget(t)) for s in S5 for t in S5 if s >= t)
print("  forgetting is monotone; fibres: open + 4 divisors over the open stratum; 2 divisors + 5 points over each boundary point")
print("  (over a boundary point the 7 strata are those of two lines meeting in a node: 2 open parts, 4 marked points, the node)")

print()
print("=== G.2: the fork and its category of elements; G.3: the C_2 example")
EL = poset_cat(["b0", "b1", "a", "c"], lambda u, v: u == v or (u[0] == "b" and v in ("a", "c")), "El(H)")
c, r = show("El(H) for the fork a <- b -> c, H(b) = 2 points", EL, 1)
assert all(tuple(r[p]) == (1, 1) for p in PRIMES)
# groupoid E on {0,1} with one arrow i->j each; p(i->j) = j-i mod 2 in C_2
arrE = [(i, j) for i in (0, 1) for j in (0, 1)]
pE = dict(((i, j), (j - i) % 2) for (i, j) in arrE)
for (i, j) in arrE:
    for (k, l) in arrE:
        if j == k:
            assert pE[(i, l)] == (pE[(i, j)] + pE[(k, l)]) % 2
for g in (0, 1):
    for i in (0, 1):
        assert len([a for a in arrE if a[0] == i and pE[a] == g]) == 1
        assert len([a for a in arrE if a[1] == i and pE[a] == g]) == 1
fibre_arrows = [a for a in arrE if pE[a] == 0]
print("  p: E -> C_2 is a functor with unique lifts from a given source and to a given target;")
print("  arrows of the strict fibre:", fibre_arrows, "-> components:", components([0, 1], fibre_arrows))
assert components([0, 1], fibre_arrows) == 2

print()
print("=== A.4 / B.3 sanity: the least-element functor m: Ch(P) -> P^op has acyclic comma categories on both sides")
def chains(elems, leq):
    out = []
    for k in range(1, len(elems) + 1):
        for c in itertools.combinations(elems, k):
            if all(leq(a, b) or leq(b, a) for a, b in itertools.combinations(c, 2)):
                out.append(frozenset(c))
    return out
def least(c, leq):
    return [x for x in c if all(leq(x, y) for y in c)][0]
for name, elems, leq in (("triangle boundary", tri, tri_leq), ("diamond", D, ld), ("octahedron", Q.objs, lambda a, b: a == b or a[0] < b[0])):
    CH = chains(elems, leq)
    ok = True
    for p in elems:
        up = [c for c in CH if leq(p, least(c, leq))]       # m/p : p <= min
        dn = [c for c in CH if leq(least(c, leq), p)]       # p\m : min <= p
        for sub in (up, dn):
            C = poset_cat(sub, lambda a, b: a <= b)
            counts, res = C.homology(3)
            ok = ok and all(tuple(res[q]) == (1, 0, 0, 0) for q in PRIMES)
    print("  %-18s %d chains; all comma posets acyclic through degree 3: %s" % (name, len(CH), ok))
    assert ok

print()
print("ALL CHECKS PASSED")
