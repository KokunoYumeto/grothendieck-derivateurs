"""TOTASPH A.12-A.13 (the 35-object acyclic category and its double cone) and C.12-C.13 on all monoids
of order <= 4. Own code (Claude, Fable 5.2); the answer's code was neither run nor imported."""
import itertools
from fincat import Cat, betti, monoid_cat, add_terminal

# ---------- A.12: category of simplices of the semisimplicial presentation complex <a,b | a^5 b^-3, b^3 (ab)^-2>
words = ['aaaaaBBB', 'bbbBABA']
verts = ['v', 'c0', 'c1']
edges = {'a': ('v', 'v'), 'b': ('v', 'v')}          # edge: (d_1 = source vertex, d_0 = target vertex)
tris = {}
for k, w in enumerate(words):
    nk = len(w)
    for i in range(nk):
        edges[('r', k, i)] = (f'c{k}', 'v')         # r_{k,i}: c_k -> v
    for i, ch in enumerate(w):
        l = ch.lower()
        j = (i + 1) % nk
        # triangle with ordered vertices (c_k, v, v): d_0 = edge 12, d_1 = edge 02, d_2 = edge 01
        if ch.islower():
            tris[('t', k, i)] = (l, ('r', k, j), ('r', k, i))
        else:
            tris[('t', k, i)] = (l, ('r', k, i), ('r', k, j))

# semisimplicial identities d_i d_j = d_{j-1} d_i (i < j) on triangles, with edge faces (d_0, d_1) = (target, source)
def dv(e, i):
    return edges[e][1] if i == 0 else edges[e][0]
for t, (e0, e1, e2) in tris.items():
    f = (e0, e1, e2)
    for i in range(3):
        for j in range(i + 1, 3):
            assert dv(f[j], i) == dv(f[i], j - 1), (t, i, j)

# the category: objects = simplices; arrows sigma -> tau = increasing injections theta with theta^* tau = sigma
def face(simplex, dim, theta):
    """theta: tuple of vertex positions (increasing) of a simplex of dimension dim; returns the face."""
    if len(theta) == dim + 1:
        return simplex
    if dim == 1:
        return dv(simplex, 1) if theta == (0,) else dv(simplex, 0)
    if dim == 2:
        e0, e1, e2 = tris[simplex]
        if len(theta) == 2:
            return {(1, 2): e0, (0, 2): e1, (0, 1): e2}[theta]
        # a vertex of the triangle: vertex 0 = source of e2, vertex 1 = target of e2, vertex 2 = target of e1
        return {0: dv(e2, 1), 1: dv(e2, 0), 2: dv(e1, 0)}[theta[0]]
    raise ValueError

simplices = [(x, 0) for x in verts] + [(e, 1) for e in edges] + [(t, 2) for t in tris]
arrows, ident, comp = {}, {}, {}
for (tau, d) in simplices:
    for m in range(d + 1):
        for theta in itertools.combinations(range(d + 1), m + 1):
            sig = face(tau, d, theta)
            arrows[(sig, tau, theta)] = ((sig, m), (tau, d))
for (x, d) in simplices:
    ident[(x, d)] = (x, x, tuple(range(d + 1)))
for g, (s2, t2) in arrows.items():
    for f, (s1, t1) in arrows.items():
        if t1 == s2:
            th = tuple(g[2][i] for i in f[2])
            comp[(g, f)] = (f[0], g[1], th)
            assert comp[(g, f)] in arrows
A = Cat(simplices, arrows, ident, comp)
ntr = A.check()
print(f'A.12: A has {len(A.objects)} objects, {len(A.arrows)} arrows; {ntr} composable triples associative')
for p in (2, 3, 5, 7, 11, 1000003):
    counts, b = betti(A, 3, p)
    print(f'   simplices {counts}; Betti mod {p}: {b}')
    assert b == [1, 0, 0]

# the A_5 certificate (right-to-left composition): a -> (1 4 3 2 5), b -> (1 2 3)
def cyc(*c):
    p = {i: i for i in range(1, 6)}
    for i, x in enumerate(c):
        p[x] = c[(i + 1) % len(c)]
    return p
def mulp(p, q):          # p after q
    return {i: p[q[i]] for i in range(1, 6)}
def inv(p):
    return {v: k for k, v in p.items()}
pa, pb = cyc(1, 4, 3, 2, 5), cyc(1, 2, 3)
idp = {i: i for i in range(1, 6)}
def evalw(w):
    r = idp
    for ch in w:             # the word read left to right as a product x_1 x_2 ... (right-to-left action)
        g = {'a': pa, 'b': pb, 'A': inv(pa), 'B': inv(pb)}[ch]
        r = mulp(r, g)
    return r
print('   relators map to the identity of A_5:', [evalw(w) == idp for w in words], '; image of a non-trivial:', pa != idp)
assert all(evalw(w) == idp for w in words)

# A.13: two cone points over A
X = add_terminal(A, 'u')
objs = X.objects + ['t']
arr = dict(X.arrows); idn = dict(X.ident); cmp_ = dict(X.comp)
for o in A.objects + ['t']:
    arr[('to', o, 't')] = (o, 't')
idn['t'] = ('to', 't', 't')
for f, (s, t) in A.arrows.items():
    cmp_[(('to', t, 't'), f)] = ('to', s, 't')
for o in A.objects + ['t']:
    cmp_[(('to', 't', 't'), ('to', o, 't'))] = ('to', o, 't')
X2 = Cat(objs, arr, idn, cmp_)
X2.check()
print(f'A.13: X has {len(X2.objects)} objects, {len(X2.arrows)} arrows; U = A + u has {len(X.objects)} objects, {len(X.arrows)} arrows')
for p in (2, 3, 5, 1000003):
    counts, b = betti(X2, 4, p)
    print(f'   simplices {counts}; Betti mod {p}: {b}')
    assert b == [1, 0, 0, 0]

# ---------- C.12 / C.13 on all monoids of order <= 4 (unit = 0), labelled tables
def solvable_over_Z(rows, rhs):
    """Is rows * t = rhs solvable over Z?  Integer row reduction to echelon (Hermite) form of the transpose problem:
    we column-reduce the matrix [rows] by unimodular column operations, tracking nothing else, and solve
    forward. rows: list of lists (m x n)."""
    m, n = len(rows), len(rows[0])
    Mx = [list(r) for r in rows]
    b = list(rhs)
    col = 0
    piv = []
    for r in range(m):
        # make row r have at most one non-zero entry among columns >= col, by the Euclidean algorithm on columns
        while True:
            nz = [c for c in range(col, n) if Mx[r][c] != 0]
            if len(nz) <= 1:
                break
            c0 = min(nz, key=lambda c: abs(Mx[r][c]))
            for c in nz:
                if c != c0:
                    q = Mx[r][c] // Mx[r][c0]
                    for rr in range(m):
                        Mx[rr][c] -= q * Mx[rr][c0]
        nz = [c for c in range(col, n) if Mx[r][c] != 0]
        if nz:
            c0 = nz[0]
            for rr in range(m):
                Mx[rr][col], Mx[rr][c0] = Mx[rr][c0], Mx[rr][col]
            piv.append((r, col))
            col += 1
    # now the matrix is lower-triangular-like in the new column basis: solve y forward
    y = [0] * n
    pc = {r: c for r, c in piv}
    for r in range(m):
        s = sum(Mx[r][c] * y[c] for c in range(n) if c not in (pc.get(r),))
        if r in pc:
            c = pc[r]
            num = b[r] - sum(Mx[r][cc] * y[cc] for cc in range(c))
            if num % Mx[r][c]:
                return False
            y[c] = num // Mx[r][c]
        else:
            if sum(Mx[r][cc] * y[cc] for cc in range(n)) != b[r]:
                return False
    return True

tot = {}
for order in (1, 2, 3, 4):
    E = list(range(order))
    nonunit = E[1:]
    cells = [(g, f) for g in nonunit for f in nonunit]
    count = hyp = filt = 0
    for vals in itertools.product(E, repeat=len(cells)):
        mul = {(g, f): (f if g == 0 else g) for g in E for f in E if g == 0 or f == 0}
        mul.update(dict(zip(cells, vals)))
        if any(mul[(mul[(h, g)], f)] != mul[(h, mul[(g, f)])] for h in E for g in E for f in E):
            continue
        count += 1
        # filtered: for all a, b there is c with c a = c b
        is_filtered = all(any(mul[(c, a)] == mul[(c, b)] for c in E) for a in E for b in E)
        # hypothesis of C.12: for all x, a there is t in Z[M], augmentation 1, with t x = t x a
        ok = True
        for x in E:
            for a in E:
                rows = []
                rhs = []
                for mth in E:   # coefficient of m in t x - t x a
                    rows.append([(1 if mul[(y, x)] == mth else 0) - (1 if mul[(mul[(y, x)], a)] == mth else 0) for y in E])
                    rhs.append(0)
                rows.append([1] * order)
                rhs.append(1)
                if not solvable_over_Z(rows, rhs):
                    ok = False
                    break
            if not ok:
                break
        hyp += ok
        filt += is_filtered
        assert (not ok) or is_filtered, ('C.12 fails', mul)
        assert (not is_filtered) or ok
    tot[order] = (count, hyp, filt)
    print(f'C.12: order {order}: {count} labelled monoid tables; affine hypothesis holds for {hyp}; filtered: {filt}; '
          f'hypothesis => filtered in every case (and conversely)')
print('ALL ASSERTIONS PASSED')
