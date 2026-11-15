"""Independent recomputation of PRETOT Theorem A.5 (Claude Opus 5.5, 12 Nov 2026).

Written from the statements of the paper only; it imports nothing from the
return's code and reads none of its data files, except in section 9, where the
shipped certificate is read and checked against tables built here.

 1. The semisimplicial set K^ss (3 vertices, 17 edges, 15 triangles) from the two words,
    its chain complex, the presentation-complex differential and its determinant.
 2. The edge-path group of K^ss and the A_5 assignment (all triangle relations).
 3. The simplicial set K (free degeneracy completion) through level 2; all functor laws.
 4. M = End_Delta([2]) (10 elements), the right action on H = K_2, the category M/H
    (52 objects, 520 arrows), E = Delta_{<=2}/K (75, 1177), A = Delta_inj/K^ss (35, 159).
 5. The comparisons E -> A (functor, section, natural transformation, all naturality
    squares) and M/H -> E (retraction data and comma contractions).
 6. Integral homology of the finite nerve of A by my own Smith normal form.
 7. The R6 test: El over A of the vertex action L, 52 objects, 221 arrows, H = (Z, Z^28, 0).
 8. Projectivity by my own construction: Dold-Kan at level 2 with the Moore complex
    N_k = intersection of ker d_i for i >= 1, an explicit chain-level section sigma, the
    decomposition a = n2 + s0 n1 + s1 n1' + s0 s0 n0, my own S (180x52) and R (52x180);
    R S = I and equivariance for all ten monoid elements.
 9. My own reader of the shipped certificate, against the tables of section 4.
Usage: python -I thmA5_indep.py <output_dir> [<shipped_outputs_dir>]
"""
import sys
import json
from itertools import combinations, combinations_with_replacement
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE))
from linalg_int import smith_diagonal, homology_from_boundaries, det_int, inverse_int  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'out'
SHIPPED = Path(sys.argv[2]) if len(sys.argv) > 2 else None
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


# ---------------------------------------------------------------- monotone maps
def mono(m, n):
    return [tuple(t) for t in combinations_with_replacement(range(n + 1), m + 1)]


def inj(m, n):
    return [tuple(t) for t in combinations(range(n + 1), m + 1)]


def after(b, a):            # b o a : apply a first
    return tuple(b[x] for x in a)


def epi_mono(f):
    im = sorted(set(f))
    return tuple(im.index(x) for x in f), tuple(im)     # (eta surjective, beta injective)


def coface(n, i):           # delta^i : [n-1] -> [n], omits i
    return tuple(j for j in range(n + 1) if j != i)


def codegen(n, i):          # sigma^i : [n+1] -> [n], hits i twice
    return tuple(j if j <= i else j - 1 for j in range(n + 2))


# ---------------------------------------------------------------- 1. K^ss
WORDS = ['aaaaaBBB', 'bbbBABA']
VERTS = ['v', 'c0', 'c1']
EDGES = ['a', 'b'] + [f'r{k}.{i}' for k, w in enumerate(WORDS) for i in range(len(w))]
TRIS = [f't{k}.{i}' for k, w in enumerate(WORDS) for i in range(len(w))]
DIM = {x: 0 for x in VERTS}
DIM.update({x: 1 for x in EDGES})
DIM.update({x: 2 for x in TRIS})
EV = {'a': ('v', 'v'), 'b': ('v', 'v')}                 # (vertex 0, vertex 1) = (source, target)
for k, w in enumerate(WORDS):
    for i in range(len(w)):
        EV[f'r{k}.{i}'] = (f'c{k}', 'v')
TF = {}                                                  # triangle -> (d0, d1, d2)
for k, w in enumerate(WORDS):
    n = len(w)
    for i, ch in enumerate(w):
        lo, hi = f'r{k}.{i}', f'r{k}.{(i + 1) % n}'
        TF[f't{k}.{i}'] = (ch.lower(), hi, lo) if ch.islower() else (ch.lower(), lo, hi)


def tri_vertices(t):
    d0, d1, d2 = TF[t]
    v0, v1 = EV[d2]
    v1b, v2 = EV[d0]
    assert v1 == v1b and EV[d1] == (v0, v2), t
    return (v0, v1, v2)


def face(x, beta):
    """beta^* x for an injection beta : [l] -> [dim x]."""
    k = DIM[x]
    if beta == tuple(range(k + 1)):
        return x
    if k == 1:
        return EV[x][beta[0]]
    if k == 2:
        if len(beta) == 2:
            missing = next(j for j in range(3) if j not in beta)
            return TF[x][missing]
        return tri_vertices(x)[beta[0]]
    raise ValueError


def section1():
    # simplicial identities on K^ss: d_i d_j = d_{j-1} d_i (i < j) on triangles
    for t in TRIS:
        for j in range(3):
            for i in range(j):
                e1 = face(t, coface(2, j))
                e2 = face(t, coface(2, i))
                assert face(e1, coface(1, i)) == face(e2, coface(1, j - 1))
    C = {0: VERTS, 1: EDGES, 2: TRIS}
    d1 = [[0] * len(EDGES) for _ in VERTS]
    for j, e in enumerate(EDGES):
        d1[VERTS.index(EV[e][1])][j] += 1
        d1[VERTS.index(EV[e][0])][j] -= 1
    d2 = [[0] * len(TRIS) for _ in EDGES]
    for j, t in enumerate(TRIS):
        for i in range(3):
            d2[EDGES.index(TF[t][i])][j] += (-1) ** i
    for r in range(len(VERTS)):
        for c in range(len(TRIS)):
            assert sum(d1[r][m] * d2[m][c] for m in range(len(EDGES))) == 0
    hom = homology_from_boundaries([3, 17, 15], {1: d1, 2: d2})
    say(f'1. K^ss: counts (3,17,15); integral homology of its chain complex {hom}')
    assert hom == [(1, []), (0, []), (0, [])]
    # presentation complex: exponent sums of a, b in the two relators
    P = [[sum(1 if ch == 'a' else -1 if ch == 'A' else 0 for ch in w) for w in WORDS],
         [sum(1 if ch == 'b' else -1 if ch == 'B' else 0 for ch in w) for w in WORDS]]
    say(f'   presentation complex <a,b | aaaaaBBB, bbbBABA>: cellular d2 (rows a,b; columns relators) = {P}, det = {det_int(P)}')
    assert P == [[5, -2], [-3, 1]] and det_int(P) == -1
    return d1, d2


# ---------------------------------------------------------------- 2. edge-path group and A_5
def section2():
    def perm(cycle):
        p = list(range(5))
        for i, x in enumerate(cycle):
            p[x - 1] = cycle[(i + 1) % len(cycle)] - 1
        return tuple(p)

    def mul(p, q):          # product "p then q" written left to right as path composition
        return tuple(q[p[x]] for x in range(5))   # x -> p -> q   (path order)
    e = tuple(range(5))
    pinv = lambda p: tuple(sorted(range(5), key=lambda i: p[i]))
    g = {'a': perm((1, 4, 3, 2, 5)), 'b': perm((1, 2, 3))}
    # spanning tree r0.0, r1.0; going around the polygon fixes every r
    for k, w in enumerate(WORDS):
        cur = e
        for i, ch in enumerate(w):
            g[f'r{k}.{i}'] = cur
            letter = g[ch.lower()] if ch.islower() else pinv(g[ch.lower()])
            cur = mul(cur, letter)
        assert cur == e, 'relator not trivial in A_5'
    # every triangle: path [01] then [12] equals [02]
    for t in TRIS:
        d0, d1, d2 = TF[t]
        assert mul(g[d2], g[d0]) == g[d1], t
    assert g['r0.0'] == e and g['r1.0'] == e
    # image: generated by g(a), g(b)
    grp = {e}
    todo = [e]
    while todo:
        x = todo.pop()
        for h in (g['a'], g['b']):
            y = mul(x, h)
            if y not in grp:
                grp.add(y)
                todo.append(y)
    even = all(sum(1 for i in range(5) for j in range(i + 1, 5) if p[i] > p[j]) % 2 == 0 for p in grp)
    say(f'2. edge-path group of K^ss -> S_5 with tree {{r0.0, r1.0}}: all 15 triangle relations hold; image has {len(grp)} elements, all even (= A_5)')
    assert len(grp) == 60 and even
    # the same with the other composition convention
    mul2 = lambda p, q: tuple(p[q[x]] for x in range(5))
    for w in WORDS:
        cur = e
        for ch in w:
            cur = mul2(cur, g[ch.lower()] if ch.islower() else pinv(g[ch.lower()]))
        assert cur == e
    say('   (both relators also vanish with the opposite composition convention)')


# ---------------------------------------------------------------- 3. K through level 2
NONDEG = {0: VERTS, 1: EDGES, 2: TRIS}


def K(n):
    return [(x, rho) for k in range(n + 1) for x in NONDEG[k] for rho in mono(n, k) if set(rho) == set(range(k + 1))]


KN = {n: K(n) for n in range(3)}
KI = {n: {s: i for i, s in enumerate(KN[n])} for n in range(3)}


def pull(s, theta):
    """K(theta)(s) for s in K_n and theta : [m] -> [n]."""
    x, rho = s
    eta, beta = epi_mono(after(rho, theta))
    return (face(x, beta), eta)


def section3():
    say(f'3. K: level sizes {[len(KN[n]) for n in range(3)]}')
    assert [len(KN[n]) for n in range(3)] == [3, 20, 52]
    count = 0
    for n in range(3):
        for m in range(3):
            for l in range(3):
                for b in mono(m, n):
                    for a in mono(l, m):
                        for s in KN[n]:
                            assert pull(pull(s, b), a) == pull(s, after(b, a))
                            count += 1
        for s in KN[n]:
            assert pull(s, tuple(range(n + 1))) == s
    say(f'   all {count} functor-law instances on Delta_<=2 hold')


# ---------------------------------------------------------------- 4. M, H, the categories
M = mono(2, 2)
H = KN[2]


def section4():
    assert len(M) == 10
    ident = (0, 1, 2)
    for g in M:
        for f in M:
            for h in M:
                assert after(after(h, g), f) == after(h, after(g, f))
    # right action h.m = K(m) h ; (h.m).m' = h.(m o m')
    act = {(h, m): pull(h, m) for h in H for m in M}
    for h in H:
        assert act[h, ident] == h
        for m1 in M:
            for m2 in M:
                assert act[act[h, m1], m2] == act[h, after(m1, m2)]
    # M/H: objects H, arrows (h, m) : h.m -> h ; composition (h,m) o (h.m, m') = (h, m o m')
    objs = H
    arrows = [(h, m) for h in H for m in M]
    src = {(h, m): act[h, m] for h, m in arrows}
    pairs = 0
    triples = 0
    for (h, m) in arrows:
        for m2 in M:
            f = (act[h, m], m2)            # f : h.m.m2 -> h.m
            comp = (h, after(m, m2))
            assert src[comp] == src[f]
            pairs += 1
            for m3 in M:
                g3 = (act[h, after(m, m2)], m3)
                assert (h, after(after(m, m2), m3)) == (h, after(m, after(m2, m3)))
                triples += 1
    say(f'4. M = End([2]): {len(M)} elements; M/H: {len(objs)} objects, {len(arrows)} arrows, '
        f'{pairs} composable pairs, {triples} triples (right-action and associativity laws hold)')
    assert (len(objs), len(arrows)) == (52, 520)
    # E = Delta_<=2 / K
    Eobj = [(n, s) for n in range(3) for s in KN[n]]
    Earr = [(alpha, (n, s)) for (n, s) in Eobj for m in range(3) for alpha in mono(m, n)]
    say(f'   E = Delta_<=2/K: {len(Eobj)} objects, {len(Earr)} arrows')
    assert (len(Eobj), len(Earr)) == (75, 1177)
    # A = Delta_inj / K^ss
    Aobj = VERTS + EDGES + TRIS
    Aarr = [(beta, x) for x in Aobj for l in range(DIM[x] + 1) for beta in inj(l, DIM[x])]
    say(f'   A = Delta_inj/K^ss: {len(Aobj)} objects, {len(Aarr)} arrows')
    assert (len(Aobj), len(Aarr)) == (35, 159)
    return act, Eobj, Earr, Aobj, Aarr


# ---------------------------------------------------------------- 5. comparisons
def section5(Eobj, Earr, Aobj, Aarr):
    # E-arrow (alpha, (n,s)) : (m, pull(s,alpha)) -> (n, s)
    def esrc(f):
        alpha, (n, s) = f
        return (len(alpha) - 1, pull(s, alpha))

    # A-arrow (beta, x) : face(x,beta) -> x
    def ret_obj(o):
        n, (x, rho) = o
        return x

    def ret_arr(f):
        alpha, (n, (x, rho)) = f
        eta, beta = epi_mono(after(rho, alpha))
        return (beta, x)
    # functor laws for ret
    checked = 0
    for f in Earr:
        src = esrc(f)
        b, x = ret_arr(f)
        assert face(x, b) == ret_obj(src)
    # composition: all composable pairs g o f
    by_target = {}
    for f in Earr:
        by_target.setdefault(f[1], []).append(f)
    for g in Earr:
        gs = esrc(g)
        for f in by_target.get(gs, []):
            gf = (after(g[0], f[0]), g[1])
            bg, xg = ret_arr(g)
            bf, xf = ret_arr(f)
            bgf, xgf = ret_arr(gf)
            assert xf == face(xg, bg) and (after(bg, bf), xg) == (bgf, xgf)
            checked += 1
    # section inc(x) = (dim x, (x, id))
    def inc_obj(x):
        k = DIM[x]
        return (k, (x, tuple(range(k + 1))))
    for x in Aobj:
        assert ret_obj(inc_obj(x)) == x
    for (beta, x) in Aarr:
        f = (beta, inc_obj(x))
        assert esrc(f) == inc_obj(face(x, beta)) and ret_arr(f) == (beta, x)
    # natural transformation id_E => inc o ret, component at (n,(x,rho)) is (rho, inc(x))
    nat = 0
    for f in Earr:
        alpha, (n, (x, rho)) = f
        (m, (x1, rho1)) = esrc(f)
        eta_t = (rho, inc_obj(x))
        eta_s = (rho1, inc_obj(x1))
        assert esrc(eta_t) == (n, (x, rho)) and esrc(eta_s) == (m, (x1, rho1))
        b, _ = ret_arr(f)
        left = (after(eta_t[0], alpha), eta_t[1])          # eta_t o f
        right = (after(b, eta_s[0]), inc_obj(x))           # inc(ret f) o eta_s
        assert left == right
        nat += 1
    say(f'5. E -> A: functor on all {checked} composable pairs, section, and all {nat} naturality squares of id => inc o ret hold')
    # M/H -> E: full subcategory on degree 2; each object c=(n,s) is a retract of d=(2, s.r_n)
    cont = 0
    for (n, s) in Eobj:
        i_n = tuple(range(n + 1))
        r_n = tuple(min(j, n) for j in range(3))
        d = (2, pull(s, r_n))
        i_arr = (i_n, d)                 # (n, pull(pull(s,r_n), i_n)) -> d
        r_arr = (r_n, (n, s))            # (2, pull(s, r_n)) -> (n, s)
        assert esrc(i_arr) == (n, s) and esrc(r_arr) == d
        assert after(r_n, i_n) == tuple(range(n + 1))      # r o i = id
        # every f : c -> d' (d' in degree 2) satisfies (f o r) o i = f
        for (alpha, tgt) in [f for f in Earr if f[1][0] == 2 and esrc(f) == (n, s)]:
            fr = after(alpha, r_n)
            assert after(fr, i_n) == alpha
            cont += 1
    say(f'   M/H -> E: all 75 objects are retracts of degree-2 objects; {cont} comma-contraction equations hold')


# ---------------------------------------------------------------- 6. homology of A
def nerve_homology(objects, arrows, compose, is_id):
    nonid = [a for a in arrows if not is_id(a)]
    out_of = {}
    for a in nonid:
        out_of.setdefault(a[0], []).append(a)
    chains = [[(o,) for o in objects], [(a,) for a in nonid]]
    while chains[-1]:
        nxt = []
        for c in chains[-1]:
            last = c[-1]
            for b in out_of.get(last[1], []):
                nxt.append(c + (b,))
        chains.append(nxt)
    chains.pop()
    idx = [{c: i for i, c in enumerate(ch)} for ch in chains]
    bnd = {}
    for n in range(1, len(chains)):
        B = [[0] * len(chains[n]) for _ in chains[n - 1]]
        for j, c in enumerate(chains[n]):
            if n == 1:
                a = c[0]
                B[idx[0][(a[1],)]][j] += 1
                B[idx[0][(a[0],)]][j] -= 1
                continue
            B[idx[n - 1][c[1:]]][j] += 1                       # d_0
            B[idx[n - 1][c[:-1]]][j] += (-1) ** n              # d_n
            for i in range(1, n):
                h = compose(c[i], c[i - 1])
                if not is_id(h):
                    B[idx[n - 1][c[:i - 1] + (h,) + c[i + 1:]]][j] += (-1) ** i
        bnd[n] = B
    dims = [len(ch) for ch in chains]
    return dims, homology_from_boundaries(dims, bnd)


def section6(Aobj, Aarr):
    # arrows of A as (source, target, beta); composition (y->z via b2) o (x->y via b1) = b2 o b1
    arr = [(face(x, beta), x, beta) for (beta, x) in Aarr]
    look = {a: a for a in arr}

    def compose(g, f):
        assert f[1] == g[0]
        return (f[0], g[1], after(g[2], f[2]))
    is_id = lambda a: len(a[2]) == DIM[a[1]] + 1
    dims, hom = nerve_homology(Aobj, arr, compose, is_id)
    say(f'6. nerve of A: chain ranks {dims}; integral homology {hom}')
    assert dims == [35, 124, 90] and hom == [(1, []), (0, []), (0, [])]


# ---------------------------------------------------------------- 7. R6
def section7():
    Lval = {0: [0], 1: [0, 1], 2: ['*']}
    objs = [(x, l) for x in VERTS + EDGES + TRIS for l in Lval[DIM[x]]]
    arrows = []
    for x in VERTS + EDGES + TRIS:
        n = DIM[x]
        for k in range(n + 1):
            for beta in inj(k, n):
                y = face(x, beta)
                for l in Lval[k]:
                    if n == 2:
                        lt = '*'
                    elif k == n:
                        lt = l
                    else:                       # k = 0, n = 1: vertex beta(0) of [1]
                        lt = beta[l]
                    arrows.append(((y, l), (x, lt), beta))

    def compose(g, f):
        assert f[1] == g[0]
        return (f[0], g[1], after(g[2], f[2]))
    is_id = lambda a: a[0] == a[1] and len(a[2]) == DIM[a[1][0]] + 1
    dims, hom = nerve_homology(objs, arrows, compose, is_id)
    say(f'7. R6 restricted-action category: {len(objs)} objects, {len(arrows)} arrows; chain ranks {dims}; homology {hom}')
    assert (len(objs), len(arrows)) == (52, 221) and dims == [52, 169, 90]
    assert hom == [(1, []), (28, []), (0, [])]


# ---------------------------------------------------------------- 8. my own splitting
def vec_add(u, w, c=1):
    r = dict(u)
    for k, v in w.items():
        r[k] = r.get(k, 0) + c * v
        if r[k] == 0:
            del r[k]
    return r


def section8(act):
    # ---- Q = Z[D0] + Z[D1]^2 + Z[D2]^15 ; copy c has generator GEN[c] in K
    U = ['r0.0', 'r1.0']
    GEN = ['v'] + U + TRIS
    CD = [DIM[x] for x in GEN]                      # copy dimensions (0,1,1,2,...,2)
    Qb = {n: [(c, al) for c in range(len(GEN)) for al in mono(n, CD[c])] for n in range(3)}
    Qi = {n: {q: i for i, q in enumerate(Qb[n])} for n in range(3)}
    say(f'8. Q = Z[D0]+Z[D1]^2+Z[D2]^15: level ranks {[len(Qb[n]) for n in range(3)]}')
    assert [len(Qb[n]) for n in range(3)] == [50, 97, 159]

    def kop(vec, theta):            # operator K(theta) on a vector of Z[K_n]
        r = {}
        for s, c in vec.items():
            r = vec_add(r, {pull(s, theta): c})
        return r

    def qop(vec, theta):
        r = {}
        for (c, al), v in vec.items():
            r = vec_add(r, {(c, after(al, theta)): v})
        return r

    def kd(vec, n, i):
        return kop(vec, coface(n, i))

    def ks(vec, n, i):
        return kop(vec, codegen(n, i))

    def qd(vec, n, i):
        return qop(vec, coface(n, i))

    def qs(vec, n, i):
        return qop(vec, codegen(n, i))

    def phi(vec):                   # Q -> Z[K], (c, alpha) -> K(alpha)(GEN[c], id)
        r = {}
        for (c, al), v in vec.items():
            g = GEN[c]
            r = vec_add(r, {pull((g, tuple(range(CD[c] + 1))), al): v})
        return r
    # ---- chain level: C(K^ss) with bases VERTS, EDGES, TRIS; Nbar(Q) with nondegenerate (c, injective alpha)
    QN = {n: [(c, al) for (c, al) in Qb[n] if len(set(al)) == len(al)] for n in range(3)}

    def nd_boundary_Q(n, q):        # sum (-1)^i d_i, dropping degenerate simplices
        r = {}
        c, al = q
        for i in range(n + 1):
            al2 = after(al, coface(n, i))
            if len(set(al2)) == len(al2):
                r = vec_add(r, {(c, al2): (-1) ** i})
        return r

    def nd_boundary_K(n, x):
        r = {}
        for i in range(n + 1):
            r = vec_add(r, {face(x, coface(n, i)): (-1) ** i})
        return r
    # adapted bases and sigma on them
    top = lambda c: (c, tuple(range(CD[c] + 1)))
    adapted = {0: [{'v': 1}] + [nd_boundary_K(1, u) for u in U],
               1: [{u: 1} for u in U] + [nd_boundary_K(2, t) for t in TRIS],
               2: [{t: 1} for t in TRIS]}
    images = {0: [{top(0): 1}] + [nd_boundary_Q(1, top(1 + k)) for k in range(2)],
              1: [{top(1 + k): 1} for k in range(2)] + [nd_boundary_Q(2, top(3 + j)) for j in range(15)],
              2: [{top(3 + j): 1} for j in range(15)]}
    basis = {0: VERTS, 1: EDGES, 2: TRIS}
    sigma = {}
    for n in range(3):
        Bm = [[adapted[n][j].get(x, 0) for j in range(len(basis[n]))] for x in basis[n]]   # columns = adapted vectors
        dB = det_int(Bm)
        say(f'   adapted basis in degree {n}: determinant {dB}')
        assert abs(dB) == 1
        Binv = inverse_int(Bm)
        # sigma(x) for a standard basis vector x = sum_j Binv[j][x] * adapted_j
        for xi, x in enumerate(basis[n]):
            r = {}
            for j in range(len(basis[n])):
                if Binv[j][xi]:
                    r = vec_add(r, images[n][j], Binv[j][xi])
            sigma[x] = r
    # chain map and section checks at the quotient level
    def phibar(vec, n):             # N̄(Q)_n -> C_n(K^ss)
        r = {}
        for (c, al), v in vec.items():
            s = pull((GEN[c], tuple(range(CD[c] + 1))), al)
            assert s[1] == tuple(range(n + 1))
            r = vec_add(r, {s[0]: v})
        return r
    for n in range(3):
        for x in basis[n]:
            assert phibar(sigma[x], n) == {x: 1}
            if n:
                lhs = {}
                for q, v in sigma[x].items():
                    lhs = vec_add(lhs, nd_boundary_Q(n, q), v)
                rhs = {}
                for y, v in nd_boundary_K(n, x).items():
                    rhs = vec_add(rhs, sigma[y], v)
                assert lhs == rhs
    say('   sigma: C(K^ss) -> Nbar(Q) is a chain map with phibar o sigma = id')

    # Moore projections in Q: level 1: 1 - s0 d1 ; level 2: (1 - s0 d1)(1 - s1 d2)
    def moore_Q(vec, n):
        if n == 0:
            return vec
        if n == 1:
            return vec_add(vec, qs(qd(vec, 1, 1), 0, 0), -1)
        y = vec_add(vec, qs(qd(vec, 2, 2), 1, 1), -1)
        y = vec_add(y, qs(qd(y, 2, 1), 1, 0), -1)
        assert not qd(y, 2, 1) and not qd(y, 2, 2)
        return y

    def sigma_moore(vec, n):        # vec: a Moore element of Z[K_n]; returns its image in N(Q)_n
        # class mod degenerates = coefficients of nondegenerate simplices (x, id)
        r = {}
        for (x, rho), v in vec.items():
            if rho == tuple(range(n + 1)):
                r = vec_add(r, sigma[x], v)
        return moore_Q(r, n)

    def F2(h):                      # F on a basis element of Z[K_2]
        a = {h: 1}
        n0 = kd(kd(a, 2, 2), 1, 1)
        n1p = vec_add(kd(a, 2, 2), ks(n0, 0, 0), -1)
        n1 = vec_add(kd(a, 2, 1), kd(a, 2, 2), -1)
        n2 = vec_add(vec_add(vec_add(a, ks(n1, 1, 0), -1), ks(n1p, 1, 1), -1), ks(ks(n0, 0, 0), 1, 0), -1)
        # Moore conditions and reconstruction
        assert not kd(n1, 1, 1) and not kd(n1p, 1, 1) and not kd(n2, 2, 1) and not kd(n2, 2, 2)
        rec = vec_add(vec_add(vec_add(n2, ks(n1, 1, 0)), ks(n1p, 1, 1)), ks(ks(n0, 0, 0), 1, 0))
        assert rec == a
        r = sigma_moore(n2, 2)
        r = vec_add(r, qs(sigma_moore(n1, 1), 1, 0))
        r = vec_add(r, qs(sigma_moore(n1p, 1), 1, 1))
        r = vec_add(r, qs(qs(sigma_moore(n0, 0), 0, 0), 1, 0))
        return r
    Fimg = {h: F2(h) for h in H}
    # phi o F = id on Z[K_2]
    for h in H:
        assert phi(Fimg[h]) == {h: 1}
    # F is M-equivariant: F(h.m) = F(h).m
    for h in H:
        for m in M:
            assert Fimg[act[h, m]] == qop(Fimg[h], m)
    say('   F = N^-1(sigma) at level 2: phi o F = id on Z[H] and F(h.m) = F(h).m for all 52 x 10 pairs')
    # ---- embed Q_2 into (ZM)^18 and back
    Mi = {g: i for i, g in enumerate(M)}

    def incl(c):
        n = CD[c]
        return tuple(range(n + 1))      # i_n : [n] -> [2]

    def retr(c):
        n = CD[c]
        return tuple(min(j, n) for j in range(3))   # r_n : [2] -> [n]
    nfree = len(GEN)
    S = [[0] * len(H) for _ in range(10 * nfree)]
    R = [[0] * (10 * nfree) for _ in range(len(H))]
    Hi = {h: i for i, h in enumerate(H)}
    for j, h in enumerate(H):
        for (c, al), v in Fimg[h].items():
            S[10 * c + Mi[after(incl(c), al)]][j] += v
    for c in range(nfree):
        for g in M:
            col = 10 * c + Mi[g]
            q = (c, after(retr(c), g))
            for s, v in phi({q: 1}).items():
                R[Hi[s]][col] += v
    # R S = I
    for i in range(len(H)):
        for j in range(len(H)):
            assert sum(R[i][k] * S[k][j] for k in range(10 * nfree)) == (1 if i == j else 0)
    # equivariance: S(h.m) = S(h).m and R(x.m) = R(x).m, free right action (c,g).m = (c, g o m)
    for m in M:
        for j, h in enumerate(H):
            moved = [0] * (10 * nfree)
            for k in range(10 * nfree):
                if S[k][j]:
                    c, gi = divmod(k, 10)
                    moved[10 * c + Mi[after(M[gi], m)]] += S[k][j]
            assert moved == [S[k][Hi[act[h, m]]] for k in range(10 * nfree)]
        for k in range(10 * nfree):
            c, gi = divmod(k, 10)
            k2 = 10 * c + Mi[after(M[gi], m)]
            moved = [0] * len(H)
            for i in range(len(H)):
                if R[i][k]:
                    moved[Hi[act[H[i], m]]] += R[i][k]
            assert moved == [R[i][k2] for i in range(len(H))]
    nzS = sum(1 for row in S for x in row if x)
    nzR = sum(1 for row in R for x in row if x)
    say(f'   my certificate: S {10 * nfree}x{len(H)} ({nzS} nonzero entries), R {len(H)}x{10 * nfree} ({nzR} nonzero); '
        f'R S = I_52; S and R equivariant for all 10 elements of M')
    return S, R


# ---------------------------------------------------------------- 9. the shipped certificate
def section9(act):
    if SHIPPED is None:
        say('9. shipped certificate: not given')
        return
    c = json.loads((SHIPPED / 'projectivity_certificate.json').read_text(encoding='utf-8'))
    basis_H = [(x, tuple(r)) for k, x, r in c['basis_H']]
    basis_M = [tuple(g) for g in c['basis_M']]
    # their names r0_0 / t0_0 versus mine r0.0 / t0.0
    ren = lambda name: name.replace('_', '.')
    bh = [(ren(x), r) for x, r in basis_H]
    assert sorted(bh) == sorted(H) and sorted(basis_M) == sorted(M)
    hi = {h: i for i, h in enumerate(bh)}
    mi = {g: i for i, g in enumerate(basis_M)}
    S = [[0] * c['inclusion_S']['cols'] for _ in range(c['inclusion_S']['rows'])]
    R = [[0] * c['retraction_R']['cols'] for _ in range(c['retraction_R']['rows'])]
    for i, j, v in c['inclusion_S']['entries']:
        S[i][j] += v
    for i, j, v in c['retraction_R']['entries']:
        R[i][j] += v
    nH, nF = len(bh), len(S)
    assert (nH, nF) == (52, 180)
    for i in range(nH):
        for j in range(nH):
            assert sum(R[i][k] * S[k][j] for k in range(nF)) == (1 if i == j else 0)
    for m in M:
        for j, h in enumerate(bh):
            moved = [0] * nF
            for k in range(nF):
                if S[k][j]:
                    cc, gi = divmod(k, 10)
                    moved[10 * cc + mi[after(basis_M[gi], m)]] += S[k][j]
            assert moved == [S[k][hi[act[h, m]]] for k in range(nF)]
        for k in range(nF):
            cc, gi = divmod(k, 10)
            k2 = 10 * cc + mi[after(basis_M[gi], m)]
            moved = [0] * nH
            for i in range(nH):
                if R[i][k]:
                    moved[hi[act[bh[i], m]]] += R[i][k]
            assert moved == [R[i][k2] for i in range(nH)]
    say('9. shipped certificate read with MY action tables: R S = I_52 and both equivariances for all 10 elements hold')


def main():
    section1()
    section2()
    section3()
    act, Eobj, Earr, Aobj, Aarr = section4()
    section5(Eobj, Earr, Aobj, Aarr)
    section6(Aobj, Aarr)
    section7()
    section8(act)
    section9(act)
    say('ALL CHECKS PASSED')
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'thmA5_indep.out').write_text('\n'.join(LOG) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
