"""Finite categories, nerves and homology. Written for the review of TOTASPH
(Claude, Fable 5.2); independent of the answer's code, which was neither run nor imported.

A category is given by: objects (list), arrows (dict name -> (src, tgt)), ident (dict obj -> arrow name),
comp (dict (g, f) -> g.f for composable f: a->b, g: b->c).
"""


class Cat:
    def __init__(self, objects, arrows, ident, comp):
        self.objects = list(objects)
        self.arrows = dict(arrows)
        self.ident = dict(ident)
        self.comp = dict(comp)

    def check(self):
        """All category axioms; returns the number of composable triples checked."""
        A = self.arrows
        for o in self.objects:
            assert A[self.ident[o]] == (o, o)
        for f, (a, b) in A.items():
            assert self.comp[(f, self.ident[a])] == f, (f, 'right unit')
            assert self.comp[(self.ident[b], f)] == f, (f, 'left unit')
        n = 0
        for f, (a, b) in A.items():
            for g, (b2, c) in A.items():
                if b2 != b:
                    assert (g, f) not in self.comp
                    continue
                gf = self.comp[(g, f)]
                assert A[gf] == (a, c)
                for h, (c2, d) in A.items():
                    if c2 != c:
                        continue
                    assert self.comp[(h, gf)] == self.comp[(self.comp[(h, g)], f)], ('assoc', h, g, f)
                    n += 1
        return n

    def hom(self, a, b):
        return [f for f, (s, t) in self.arrows.items() if s == a and t == b]

    def nonid(self):
        ids = set(self.ident.values())
        return [f for f in self.arrows if f not in ids]

    def simplices(self, maxdim):
        """Nondegenerate simplices of the nerve (chains of non-identity arrows) up to dimension maxdim."""
        ni = self.nonid()
        out_by_src = {}
        for f in ni:
            out_by_src.setdefault(self.arrows[f][0], []).append(f)
        S = [[(o,) for o in self.objects]]
        cur = [(f,) for f in ni]
        d = 1
        while d <= maxdim and cur:
            S.append(cur)
            nxt = []
            for s in cur:
                t = self.arrows[s[-1]][1]
                for g in out_by_src.get(t, []):
                    nxt.append(s + (g,))
            cur = nxt
            d += 1
        return S

    def boundary_matrices(self, maxdim):
        """Normalized chain complex of the nerve: simplex counts and sparse matrices d_k, k = 1..maxdim."""
        S = self.simplices(maxdim)
        ids = set(self.ident.values())
        idx = [{s: i for i, s in enumerate(level)} for level in S]
        mats = []
        for k in range(1, len(S)):
            ent = {}
            for j, s in enumerate(S[k]):
                if k == 1:
                    a, b = self.arrows[s[0]]
                    faces = [(1, (b,)), (-1, (a,))]
                else:
                    faces = [(1, s[1:])]
                    for i in range(1, k):
                        c = self.comp[(s[i], s[i - 1])]
                        if c in ids:
                            continue  # degenerate face: zero in normalized chains
                        faces.append(((-1) ** i, s[:i - 1] + (c,) + s[i + 1:]))
                    faces.append(((-1) ** k, s[:-1]))
                for sg, face in faces:
                    r = idx[k - 1][face]
                    ent[(r, j)] = ent.get((r, j), 0) + sg
            mats.append((len(S[k - 1]), len(S[k]), ent))
        return [len(l) for l in S], mats


def rank_mod(nrows, ncols, ent, p):
    rows = {}
    for (r, c), v in ent.items():
        v %= p
        if v:
            rows.setdefault(r, {})[c] = v
    rk = 0
    pivots = {}
    for r in list(rows):
        row = rows[r]
        while row:
            c = min(row)
            if c in pivots:
                piv = pivots[c]
                f = row[c]
                for cc, vv in piv.items():
                    nv = (row.get(cc, 0) - f * vv) % p
                    if nv:
                        row[cc] = nv
                    else:
                        row.pop(cc, None)
            else:
                inv = pow(row[c], p - 2, p)
                pivots[c] = {cc: (vv * inv) % p for cc, vv in row.items()}
                rk += 1
                break
    return rk


def betti(cat, maxdim, p):
    """Simplex counts in dimensions 0..maxdim and Betti numbers mod p; the Betti number in the top
    dimension computed is only an upper bound unless the nerve has no simplices above maxdim."""
    counts, mats = cat.boundary_matrices(maxdim)
    ranks = [0] + [rank_mod(m[0], m[1], m[2], p) for m in mats] + [0]
    b = []
    for k in range(len(counts)):
        b.append(counts[k] - ranks[k] - (ranks[k + 1] if k + 1 < len(ranks) else 0))
    return counts, b


def components(objs, edges):
    par = {o: o for o in objs}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for a, b in edges:
        par[find(a)] = find(b)
    return len({find(o) for o in objs})


def comma_under(F_obj, F_arr, A, B, b):
    """b\\A for a functor F: A -> B (objects and the edges of its underlying graph)."""
    objs = [(a, beta) for a in A.objects for beta in B.hom(b, F_obj[a])]
    edges = []
    for f, (a, a2) in A.arrows.items():
        for beta in B.hom(b, F_obj[a]):
            edges.append(((a, beta), (a2, B.comp[(F_arr[f], beta)])))
    return objs, edges


def is_final(F_obj, F_arr, A, B):
    res = {}
    for b in B.objects:
        objs, edges = comma_under(F_obj, F_arr, A, B, b)
        res[b] = (len(objs), components(objs, edges) if objs else 0)
    return all(n > 0 and c == 1 for n, c in res.values()), res


def check_functor(F_obj, F_arr, A, B):
    for o in A.objects:
        assert F_arr[A.ident[o]] == B.ident[F_obj[o]]
    for f, (a, b) in A.arrows.items():
        assert B.arrows[F_arr[f]] == (F_obj[a], F_obj[b])
    for (g, f), gf in A.comp.items():
        assert B.comp[(F_arr[g], F_arr[f])] == F_arr[gf]


def poset_cat(objs, leq):
    arrows = {(a, b): (a, b) for a in objs for b in objs if leq(a, b)}
    ident = {a: (a, a) for a in objs}
    comp = {((b, c), (a, b)): (a, c) for (a, b) in arrows for (b2, c) in arrows if b2 == b}
    return Cat(objs, arrows, ident, comp)


def collage_cov(A, K_obj, K_arr, new='x'):
    """A_K: adjoin a source object `new` with Hom(new, a) = K(a) for a covariant K: A -> Set.
    K_obj: object -> list of elements; K_arr: arrow -> dict element -> element."""
    objects = A.objects + [new]
    arrows = dict(A.arrows)
    ident = dict(A.ident)
    comp = dict(A.comp)
    idn = ('id', new)
    arrows[idn] = (new, new)
    ident[new] = idn
    comp[(idn, idn)] = idn
    for a in A.objects:
        for h in K_obj[a]:
            arrows[('k', a, h)] = (new, a)
            comp[(('k', a, h), idn)] = ('k', a, h)
    for f, (a, b) in A.arrows.items():
        for h in K_obj[a]:
            comp[(f, ('k', a, h))] = ('k', b, K_arr[f][h])
    return Cat(objects, arrows, ident, comp)


def elements_cov(A, K_obj, K_arr):
    """El_A(K) for covariant K: arrow (a,h) -> (b, K(f)h) for f: a -> b."""
    objects = [(a, h) for a in A.objects for h in K_obj[a]]
    arrows, ident, comp = {}, {}, {}
    for f, (a, b) in A.arrows.items():
        for h in K_obj[a]:
            arrows[(f, h)] = ((a, h), (b, K_arr[f][h]))
    for a in A.objects:
        for h in K_obj[a]:
            ident[(a, h)] = (A.ident[a], h)
    for (f, h), (s, t) in arrows.items():
        for g, (b, c) in A.arrows.items():
            if b == t[0]:
                comp[((g, t[1]), (f, h))] = (A.comp[(g, f)], h)
    return Cat(objects, arrows, ident, comp)


def elements_contra(U, H_obj, H_arr):
    """U/H for a presheaf H: arrow (u, H(a)k) -> (v, k) for a: u -> v. H_arr: arrow -> dict k -> H(a)k."""
    objects = [(u, h) for u in U.objects for h in H_obj[u]]
    arrows, ident, comp = {}, {}, {}
    for a, (u, v) in U.arrows.items():
        for k in H_obj[v]:
            arrows[(a, k)] = ((u, H_arr[a][k]), (v, k))
    for u in U.objects:
        for h in H_obj[u]:
            ident[(u, h)] = (U.ident[u], h)
    for (a, k), (s, t) in arrows.items():
        for (b, l), (s2, t2) in arrows.items():
            if s2 == t:
                comp[((b, l), (a, k))] = (U.comp[(b, a)], l)
    return Cat(objects, arrows, ident, comp)


def monoid_cat(elems, unit, mul):
    """One-object category; g.f = mul[(g, f)]."""
    arrows = {m: ('*', '*') for m in elems}
    comp = {(g, f): mul[(g, f)] for g in elems for f in elems}
    return Cat(['*'], arrows, {'*': unit}, comp)


def add_terminal(C, new='s'):
    objects = C.objects + [new]
    arrows = dict(C.arrows)
    ident = dict(C.ident)
    comp = dict(C.comp)
    for o in objects:
        arrows[('to', o, new)] = (o, new)
    ident[new] = ('to', new, new)
    for f, (a, b) in C.arrows.items():
        comp[(('to', b, new), f)] = ('to', a, new)
    for o in objects:
        comp[(('to', new, new), ('to', o, new))] = ('to', o, new)
    return Cat(objects, arrows, ident, comp)


def add_initial(C, new='o'):
    objects = [new] + C.objects
    arrows = dict(C.arrows)
    ident = dict(C.ident)
    comp = dict(C.comp)
    for o in objects:
        arrows[('from', new, o)] = (new, o)
    ident[new] = ('from', new, new)
    for f, (a, b) in C.arrows.items():
        comp[(f, ('from', new, a))] = ('from', new, b)
    for o in objects:
        comp[(('from', new, o), ('from', new, new))] = ('from', new, o)
    return Cat(objects, arrows, ident, comp)


def full_sub(C, objs):
    objs = list(objs)
    arrows = {f: st for f, st in C.arrows.items() if st[0] in objs and st[1] in objs}
    comp = {(g, f): v for (g, f), v in C.comp.items() if g in arrows and f in arrows}
    return Cat(objs, arrows, {o: C.ident[o] for o in objs}, comp)


def pushout_sieve(X, Uobjs, C, p_obj, p_arr):
    """Ordinary pushout X +_U C in Cat for a full sieve U in X and a functor p: U -> C.
    Objects: C + (X minus U). Hom(c, t), t outside U, is the coend over u in U of C(c, p u) x X(u, t),
    computed by union-find on the generating relation (d.p(al), pi) ~ (d, pi.al).
    Returns the category and the map (c, t, (d, pi)) -> arrow name."""
    Uobjs = list(Uobjs)
    U = full_sub(X, Uobjs)
    T = [o for o in X.objects if o not in Uobjs]
    for f, (a, b) in X.arrows.items():
        assert not (b in Uobjs and a not in Uobjs), 'not a sieve'
    objects = [('C', c) for c in C.objects] + [('T', t) for t in T]
    arrows, ident, comp = {}, {}, {}
    for f, (a, b) in C.arrows.items():
        arrows[('C', f)] = (('C', a), ('C', b))
    for c in C.objects:
        ident[('C', c)] = ('C', C.ident[c])
    for (g, f), v in C.comp.items():
        comp[(('C', g), ('C', f))] = ('C', v)
    for f, (a, b) in X.arrows.items():
        if a in T and b in T:
            arrows[('T', f)] = (('T', a), ('T', b))
    for t in T:
        ident[('T', t)] = ('T', X.ident[t])
    for (g, f), v in X.comp.items():
        if ('T', g) in arrows and ('T', f) in arrows:
            comp[(('T', g), ('T', f))] = ('T', v)
    cls = {}
    for c in C.objects:
        for t in T:
            pairs = [(d, pi) for u in Uobjs for d in C.hom(c, p_obj[u]) for pi in X.hom(u, t)]
            par = {x: x for x in pairs}

            def find(x):
                while par[x] != x:
                    par[x] = par[par[x]]
                    x = par[x]
                return x
            for al, (u, u2) in U.arrows.items():
                for d in C.hom(c, p_obj[u]):
                    for pi in X.hom(u2, t):
                        x1 = (C.comp[(p_arr[al], d)], pi)
                        x2 = (d, X.comp[(pi, al)])
                        par[find(x1)] = find(x2)
            for x in pairs:
                r = find(x)
                cls[(c, t, x)] = ('X', c, t, r)
                arrows[('X', c, t, r)] = (('C', c), ('T', t))
    for (c, t, (d, pi)), name in cls.items():
        comp[(name, ('C', C.ident[c]))] = name
        comp[(('T', X.ident[t]), name)] = name
        for e, (c0, c1) in C.arrows.items():
            if c1 == c:
                v = cls[(c0, t, (C.comp[(d, e)], pi))]
                assert comp.get((name, ('C', e)), v) == v, 'composition not well defined'
                comp[(name, ('C', e))] = v
        for g, (t0, t1) in X.arrows.items():
            if t0 == t and t1 in T:
                v = cls[(c, t1, (d, X.comp[(g, pi)]))]
                assert comp.get((('T', g), name), v) == v, 'composition not well defined'
                comp[(('T', g), name)] = v
    return Cat(objects, arrows, ident, comp), cls
