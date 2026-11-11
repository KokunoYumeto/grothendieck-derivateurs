"""Own checks for the review of POLES (Claude, Fable 5.2, 11 November 2026).

Written from the statements in POLES sections/B.tex, D.tex, F.tex; uses nothing from the
answer's code folder.  Run:  python -I check_poles.py > check_poles.out

1. B.7 / B.8: the finite category A (face category of a triangulated presentation complex of
   <a,b | a^5 b^-3, b^3 (ab)^-2>), its integral homology, a non-trivial functor to A_5, and the
   two-cone category X = A * {u,t}: U, V sieves, U, V with terminal objects, X with the homology
   of a point.  Consequence: U -> X is in W_infty and A -> V is not.
2. B.13: the four-object category K(g) for the fold {a0,a1} -> e is connected with H_1 = Z.
3. F.8: the endomorphism alpha of the free group on x,y: identity on the abelianization, and two
   different homomorphisms to S_3 that agree on its image (so alpha is not surjective).
4. D.6: all monotone maps from the six-element circle poset P to sd P have degree 0.
"""
from itertools import product, combinations
from fractions import Fraction


# ---------------------------------------------------------------- finite categories
class Cat:
    """objects: list; arrows: dict name -> (src, tgt); comp: dict (g, f) -> g.f ; ident: obj -> name"""

    def __init__(self, objects, arrows, comp, ident):
        self.objects, self.arrows, self.comp, self.ident = objects, arrows, comp, ident

    def check(self):
        A = self.arrows
        for o in self.objects:
            assert A[self.ident[o]] == (o, o)
        n = 0
        for f, (s, t) in A.items():
            assert self.comp[(f, self.ident[s])] == f and self.comp[(self.ident[t], f)] == f
            for g, (s2, t2) in A.items():
                if s2 == t:
                    h = self.comp[(g, f)]
                    assert A[h] == (s, t2)
                    n += 1
                else:
                    assert (g, f) not in self.comp
        out = {}
        for f, (s, t) in A.items():
            out.setdefault(t, []).append(f)  # arrows by target? we need arrows starting at t
        start = {}
        for f, (s, t) in A.items():
            start.setdefault(s, []).append(f)
        m = 0
        for f, (s, t) in A.items():
            for g in start.get(t, []):
                for h in start.get(A[g][1], []):
                    assert self.comp[(h, self.comp[(g, f)])] == self.comp[(self.comp[(h, g)], f)]
                    m += 1
        return n, m

    def chains(self, maxdim=6):
        """non-degenerate simplices of the nerve: strings of composable non-identity arrows"""
        ids = set(self.ident.values())
        start = {}
        for f, (s, t) in self.arrows.items():
            if f not in ids:
                start.setdefault(s, []).append(f)
        C = [[(o,) for o in self.objects]]
        level = [(f,) for f in self.arrows if f not in ids]
        while level and len(C) <= maxdim:
            C.append(level)
            nxt = []
            for c in level:
                for g in start.get(self.arrows[c[-1]][1], []):
                    nxt.append(c + (g,))
            level = nxt
        assert not level, "nerve has simplices above maxdim"
        return C

    def boundary_matrices(self):
        C = self.chains()
        ids = set(self.ident.values())
        mats = []
        for n in range(1, len(C)):
            idx = {c: i for i, c in enumerate(C[n - 1])}
            M = [[0] * len(C[n]) for _ in C[n - 1]]
            for j, c in enumerate(C[n]):
                faces = []
                if n == 1:
                    s, t = self.arrows[c[0]]
                    faces = [(1, (t,)), (-1, (s,))]
                else:
                    faces.append((1, c[1:]))
                    for i in range(1, n):
                        h = self.comp[(c[i], c[i - 1])]
                        faces.append(((-1) ** i, None if h in ids else c[:i - 1] + (h,) + c[i + 1:]))
                    faces.append(((-1) ** n, c[:-1]))
                for sgn, f in faces:
                    if f is not None:
                        M[idx[f]][j] += sgn
            mats.append(M)
        return [len(c) for c in C], mats


def smith_diag(M):
    """non-zero entries of a diagonalization of an integer matrix by row and column operations
    (the abelian group it presents is the sum of Z/d over these entries, plus a free part)"""
    M = [row[:] for row in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    diag = []
    r = 0
    while r < min(rows, cols):
        best = None
        for i in range(r, rows):
            for j in range(r, cols):
                if M[i][j] != 0 and (best is None or abs(M[i][j]) < best[0]):
                    best = (abs(M[i][j]), i, j)
            if best and best[0] == 1:
                break
        if best is None:
            break
        _, i, j = best
        M[r], M[i] = M[i], M[r]
        for row in M:
            row[r], row[j] = row[j], row[r]
        while True:
            p = M[r][r]
            dirty = False
            for i in range(r + 1, rows):
                if M[i][r] != 0:
                    q = M[i][r] // p
                    M[i] = [a - q * b for a, b in zip(M[i], M[r])]
                    if M[i][r] != 0:
                        M[r], M[i] = M[i], M[r]
                        dirty = True
                        break
            if dirty:
                continue
            for j in range(r + 1, cols):
                if M[r][j] != 0:
                    q = M[r][j] // p
                    for row in M[r:]:
                        row[j] -= q * row[r]
                    if M[r][j] != 0:
                        for row in M[r:]:
                            row[r], row[j] = row[j], row[r]
                        dirty = True
                        break
            if not dirty:
                break
        diag.append(abs(M[r][r]))
        r += 1
    return diag


def homology(cat):
    ranks, mats = cat.boundary_matrices()
    diags = [smith_diag(M) for M in mats]
    H = []
    for n, rk in enumerate(ranks):
        r_out = len(diags[n - 1]) if n >= 1 else 0          # rank of d_n : C_n -> C_{n-1}
        r_in = len(diags[n]) if n < len(mats) else 0          # rank of d_{n+1}
        tors = [d for d in (diags[n] if n < len(mats) else []) if d != 1]
        H.append((rk - r_out - r_in, tors))
    return ranks, H


# ---------------------------------------------------------------- 1. the category A
def build_A():
    words = ["aaaaaBBB", "bbbBABA"]
    verts = ["v", "c0", "c1"]
    edges = {"a": ("v", "v"), "b": ("v", "v")}       # (vertex 0, vertex 1)
    tris = {}
    for k, w in enumerate(words):
        n = len(w)
        for i in range(n):
            edges[f"r{k}_{i}"] = (f"c{k}", "v")
        for i, L in enumerate(w):
            r_i, r_j = f"r{k}_{i}", f"r{k}_{(i + 1) % n}"
            # faces (d0, d1, d2) = (edge 12, edge 02, edge 01)
            tris[f"t{k}_{i}"] = (L, r_j, r_i) if L.islower() else (L.lower(), r_i, r_j)
    dim = {**{x: 0 for x in verts}, **{x: 1 for x in edges}, **{x: 2 for x in tris}}

    def face(s, theta):
        """theta^* s for an increasing injection theta given as a tuple of vertex positions"""
        if len(theta) == dim[s] + 1:
            return s
        if dim[s] == 1:
            return edges[s][theta[0]]
        d0, d1, d2 = tris[s]
        if len(theta) == 2:
            return {(1, 2): d0, (0, 2): d1, (0, 1): d2}[theta]
        # vertex i of a triangle: via its edges
        i = theta[0]
        return {0: edges[d2][0], 1: edges[d2][1], 2: edges[d1][1]}[i]

    # semisimplicial identities: the three vertices of each triangle are well defined
    for t, (d0, d1, d2) in tris.items():
        assert edges[d2][0] == edges[d1][0] and edges[d2][1] == edges[d0][0] and edges[d1][1] == edges[d0][1], t

    objects = verts + list(edges) + list(tris)
    arrows, ident = {}, {}
    for s in objects:
        n = dim[s]
        for m in range(n + 1):
            for theta in combinations(range(n + 1), m + 1):
                name = (face(s, theta), s, theta)
                arrows[name] = (name[0], s)
                if m == n:
                    ident[s] = name
    comp = {}
    for f in arrows:
        for g in arrows:
            if g[0] == f[1]:
                comp[(g, f)] = (f[0], g[1], tuple(g[2][i] for i in f[2]))
    return Cat(objects, arrows, comp, ident), dict(edges=edges, tris=tris, dim=dim, words=words)


def perm_mul(p, q):
    """first p, then q (permutations of range(5) as tuples)"""
    return tuple(q[p[i]] for i in range(len(p)))


def perm_inv(p):
    r = [0] * len(p)
    for i, x in enumerate(p):
        r[x] = i
    return tuple(r)


def cyc(n, *cycles):
    p = list(range(n))
    for c in cycles:
        for i, x in enumerate(c):
            p[x - 1] = c[(i + 1) % len(c)] - 1
    return tuple(p)


def local_system(A, data):
    e5 = tuple(range(5))
    ga, gb = cyc(5, (1, 4, 3, 2, 5)), cyc(5, (1, 2, 3))
    ok = None
    # the answer composes right to left; try both conventions and keep the one closing both relators
    for conv in ("ltr", "rtl"):
        mul = perm_mul if conv == "ltr" else (lambda p, q: perm_mul(q, p))
        g = {"a": ga, "b": gb}
        good = True
        for k, w in enumerate(data["words"]):
            cur = e5
            for i, L in enumerate(w):
                g[f"r{k}_{i}"] = cur
                cur = mul(cur, g[L]) if L.islower() else mul(cur, perm_inv(g[L.lower()]))
            good &= (cur == e5)
        if good:
            ok = (conv, mul, g)
            break
    assert ok, "relators do not map to the identity"
    conv, mul, g = ok
    edges, tris, dim = data["edges"], data["tris"], data["dim"]

    def h(s, j):
        """group element of the path from vertex 0 to vertex j inside the simplex s"""
        if j == 0:
            return e5
        if dim[s] == 1:
            return g[s]
        d0, d1, d2 = tris[s]
        return g[d2] if j == 1 else g[d1]

    F = {f: h(f[1], f[2][0]) for f in A.arrows}
    # cocycle on triangles and functoriality on all composable pairs
    for t, (d0, d1, d2) in tris.items():
        assert g[d1] == mul(g[d2], g[d0]), t
    for (gg, f), hh in A.comp.items():
        assert F[hh] == mul(F[gg], F[f])
    image = set(F.values())
    return conv, len(image)


def two_cones(A):
    objects = A.objects + ["u", "t"]
    arrows, comp, ident = dict(A.arrows), dict(A.comp), dict(A.ident)
    for c in ("u", "t"):
        ident[c] = ("id", c)
        arrows[("id", c)] = (c, c)
        for o in A.objects:
            arrows[("cone", o, c)] = (o, c)
    for f, (s, t) in list(arrows.items()):
        for g, (s2, t2) in list(arrows.items()):
            if s2 == t and (g, f) not in comp:
                if g[0] == "id":
                    comp[(g, f)] = f
                elif f[0] == "id":
                    comp[(g, f)] = g
                else:                       # g is a cone arrow, f an arrow of A
                    comp[(g, f)] = ("cone", s, t2)
    return Cat(objects, arrows, comp, ident)


def full_sub(cat, objs):
    objs = set(objs)
    arrows = {f: st for f, st in cat.arrows.items() if st[0] in objs and st[1] in objs}
    comp = {k: v for k, v in cat.comp.items() if k[0] in arrows and k[1] in arrows}
    return Cat([o for o in cat.objects if o in objs], arrows, comp, {o: cat.ident[o] for o in objs})


def is_sieve(cat, objs):
    objs = set(objs)
    return all(s in objs for f, (s, t) in cat.arrows.items() if t in objs)


def has_terminal(cat):
    for o in cat.objects:
        cnt = {x: 0 for x in cat.objects}
        for f, (s, t) in cat.arrows.items():
            if t == o:
                cnt[s] += 1
        if all(v == 1 for v in cnt.values()):
            return o
    return None


print("1. The acyclic category A and its two cones (POLES B.7, B.8)")
A, data = build_A()
print("   A: objects", len(A.objects), "arrows", len(A.arrows), "composable pairs, triples checked", A.check())
ranks, H = homology(A)
print("   normalized nerve chain ranks", ranks, " homology (free rank, torsion):", H)
assert ranks == [35, 124, 90] and H == [(1, []), (0, []), (0, [])]
conv, size = local_system(A, data)
print("   functor A -> A_5 (a = (1 4 3 2 5), b = (1 2 3)), convention", conv, ": functorial on all pairs; image has", size, "elements")
assert size > 1
X = two_cones(A)
print("   X = A with two cone points: objects", len(X.objects), "arrows", len(X.arrows), "checked", X.check())
U, V = A.objects + ["u"], A.objects + ["t"]
print("   U, V sieves:", is_sieve(X, U), is_sieve(X, V), " U cap V = A:", set(U) & set(V) == set(A.objects),
      " terminal objects of U, V:", has_terminal(full_sub(X, U)), has_terminal(full_sub(X, V)))
assert is_sieve(X, U) and is_sieve(X, V)
ranksX, HX = homology(X)
print("   X: chain ranks", ranksX, " homology:", HX)
assert HX[0] == (1, []) and all(h == (0, []) for h in HX[1:])
print("   BX is the suspension of the connected BA: simply connected (van Kampen) and acyclic, so contractible.")
print("   Hence U -> X is in W_infty and A -> V is not: W(7 bis), Loc (6'b), Loc (6 b) fail for W_infty.")

print("2. K(g) for the fold {a0,a1} -> e (POLES B.13)")
objs = ["a0", "a1", "b", "t"]
arr = {("id", o): (o, o) for o in objs}
for a in ("a0", "a1"):
    for x in ("b", "t"):
        arr[(a, x)] = (a, x)
comp = {}
for f, (s, t) in arr.items():
    for g, (s2, t2) in arr.items():
        if s2 == t:
            comp[(g, f)] = f if g[0] == "id" else g
K = Cat(objs, arr, comp, {o: ("id", o) for o in objs})
K.check()
print("   chain ranks, homology:", homology(K), " (connected, H_1 = Z: W_0-aspherical while the fold is not in W_0)")

print("3. The endomorphism alpha: x -> x, y -> y x y x^-1 y^-1 of the free group (POLES F.8)")
word = [("y", 1), ("x", 1), ("y", 1), ("x", -1), ("y", -1)]
print("   exponent sums of alpha(y): x", sum(e for l, e in word if l == "x"), " y", sum(e for l, e in word if l == "y"),
      " (identity on the abelianization)")
S3 = [p for p in product(range(3), repeat=3) if len(set(p)) == 3]
found = []
for px in S3:
    table = {}
    for py in S3:
        val = tuple(range(3))
        for l, e in word:
            p = px if l == "x" else py
            val = perm_mul(val, p if e == 1 else perm_inv(p))
        table.setdefault(val, []).append(py)
    for val, ys in table.items():
        if len(ys) > 1:
            found.append((px, val, ys))
print("   pairs of homomorphisms F -> S_3 with the same value on x and on alpha(y), different on y:", len(found))
print("   one of them: x ->", found[0][0], " alpha(y) ->", found[0][1], " y -> one of", found[0][2])
assert found

print("4. Monotone maps P -> sd P for the six-element circle poset (POLES D.6)")
Pv = [frozenset([i]) for i in range(3)]
Pe = [frozenset(c) for c in combinations(range(3), 2)]
P = Pv + Pe
leP = lambda p, q: p <= q
sd = [(p,) for p in P] + [(v, e) for v in Pv for e in Pe if v < e]
leS = lambda c, d: set(c) <= set(d)
# the nerve of sd P is a 12-cycle; fix a cyclic orientation by walking it
adj = {c: [d for d in sd if d != c and (leS(c, d) or leS(d, c))] for c in sd}
assert all(len(v) == 2 for v in adj.values())
cyc_order = [sd[0], adj[sd[0]][0]]
while len(cyc_order) < 12:
    nxt = [d for d in adj[cyc_order[-1]] if d != cyc_order[-2]]
    cyc_order.append(nxt[0])
pos = {c: i for i, c in enumerate(cyc_order)}
# the nerve of P is a 6-cycle: walk it
adjP = {p: [q for q in P if q != p and (p < q or q < p)] for p in P}
walk = [P[0], adjP[P[0]][0]]
while len(walk) < 6:
    walk.append([q for q in adjP[walk[-1]] if q != walk[-2]][0])
count, degrees = 0, set()
for vals in product(sd, repeat=6):
    f = dict(zip(P, vals))
    if all(leS(f[v], f[e]) for v in Pv for e in Pe if v < e):
        count += 1
        steps = 0
        for i in range(6):
            a, b = pos[f[walk[i]]], pos[f[walk[(i + 1) % 6]]]
            d = (b - a) % 12
            assert d in (0, 1, 11)
            steps += {0: 0, 1: 1, 11: -1}[d]
        assert steps % 12 == 0
        degrees.add(steps // 12)
print("   monotone maps:", count, " degrees occurring:", sorted(degrees))
assert degrees == {0}
print("all checks passed")
