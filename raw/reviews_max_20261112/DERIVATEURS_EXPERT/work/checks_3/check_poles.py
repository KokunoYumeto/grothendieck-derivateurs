# Own checks for the POLES review (Claude Fable 5.2, 12 Nov 2026). Independent of the return's code.
# 1. B.7: the acyclic presentation <a,b | a^5 b^-3, b^3 (ab)^-2> and its A_5 quotient.
# 2. F.8 / C.5 / C.10: alpha(x)=x, alpha(y)=y x y x^-1 y^-1; two homomorphisms to S_3 that agree after alpha.
# 3. D.6: every monotone map P -> sd P (P = face poset of the boundary of a triangle) has degree 0.
# 4. H.5: the four-object category Q has the homology of S^2; collapsing the sieve U gives the arrow category.
# 5. Trefoil: Fox calculus gives the Alexander polynomial t^2 - t + 1 (used in my direct proof that W_Z fails 7F).
from itertools import product, permutations
from fractions import Fraction

# ---------- 1 ----------
def compose(p, q):            # p after q, permutations of {1..5} as dicts
    return {i: p[q[i]] for i in q}
def cyc(*c, n=5):
    d = {i: i for i in range(1, n + 1)}
    for k in range(len(c)):
        d[c[k]] = c[(k + 1) % len(c)]
    return d
ident = cyc()
a = cyc(1, 4, 3, 2, 5); b = cyc(1, 2, 3)
def power(p, k):
    r = ident
    for _ in range(k):
        r = compose(p, r)
    return r
ab = compose(a, b)
assert power(a, 5) == ident and power(b, 3) == ident and power(ab, 2) == ident and a != ident
det = 5 * 1 - (-2) * (-3)
assert det == -1
print("1. a^5 = b^3 = (ab)^2 = 1 in A_5, a != 1; ab =", ab, "; det of relation matrix =", det)

# ---------- 2 ----------
def pmul(p, q): return tuple(p[q[i]] for i in range(3))
def pinv(p): return tuple(p.index(i) for i in range(3))
e3 = (0, 1, 2); s12 = (1, 0, 2); s13 = (2, 1, 0)
def ev(word, img):
    r = e3
    for ch in word:
        g = img[ch.lower()]
        r = pmul(r, pinv(g) if ch.isupper() else g)
    return r
alpha = {'x': 'x', 'y': 'yxyXY'}
h0 = {'x': s12, 'y': s12}; h1 = {'x': s12, 'y': s13}
assert all(ev(alpha[g], h0) == ev(alpha[g], h1) for g in 'xy') and h0 != h1
expo = {g: (alpha[g].count('x') - alpha[g].count('X'), alpha[g].count('y') - alpha[g].count('Y')) for g in 'xy'}
assert expo == {'x': (1, 0), 'y': (0, 1)}
# orbits of the pulled-back action on {0,1,2}
def orbits(gens):
    rem = set(range(3)); out = []
    while rem:
        o = {min(rem)}
        while True:
            n = o | {g[i] for g in gens for i in o} | {pinv(g)[i] for g in gens for i in o}
            if n == o: break
            o = n
        out.append(sorted(o)); rem -= o
    return out
print("2. h0.alpha = h1.alpha, exponent sums", expo, "; orbits of rho:", orbits([s12, s13]),
      "; orbits of rho.alpha:", orbits([ev(alpha['x'], h1), ev(alpha['y'], h1)]))

# ---------- 3 ----------
V = ['v0', 'v1', 'v2']; E = ['e0', 'e1', 'e2']
below = {('v0', 'e0'), ('v1', 'e0'), ('v1', 'e1'), ('v2', 'e1'), ('v2', 'e2'), ('v0', 'e2')}
P = V + E
def leP(x, y): return x == y or (x, y) in below
chains = [(x,) for x in P] + [(x, y) for (x, y) in sorted(below)]
def leS(c, d): return set(c) <= set(d)
# oriented 12-cycle of sd P: v0, (v0,e0), e0, (v1,e0), v1, (v1,e1), e1, (v2,e1), v2, (v2,e2), e2, (v0,e2)
cyc12 = [('v0',), ('v0', 'e0'), ('e0',), ('v1', 'e0'), ('v1',), ('v1', 'e1'), ('e1',), ('v2', 'e1'), ('v2',),
         ('v2', 'e2'), ('e2',), ('v0', 'e2')]
pos = {c: i for i, c in enumerate(cyc12)}
cyc6 = ['v0', 'e0', 'v1', 'e1', 'v2', 'e2']
count = 0; degs = set()
for imgs in product(chains, repeat=6):
    f = dict(zip(P, imgs))
    if all(leS(f[x], f[y]) for (x, y) in below):
        count += 1
        # degree: sum of signed steps along the 6-cycle; consecutive images are equal or adjacent on the 12-cycle
        tot = 0
        for k in range(6):
            p, q = pos[f[cyc6[k]]], pos[f[cyc6[(k + 1) % 6]]]
            d = (q - p) % 12
            assert d in (0, 1, 11)
            tot += {0: 0, 1: 1, 11: -1}[d]
        assert tot % 12 == 0
        degs.add(tot // 12)
print("3. monotone maps P -> sd P:", count, "; degrees occurring:", sorted(degs))

# ---------- 4 ----------
# Q: objects a,b,z,x; r:a->z, v:b->z, lam,mu:z->x, al=lam r=mu r : a->x, be=lam v=mu v : b->x.
objs = ['a', 'b', 'z', 'x']
arr = {'ia': ('a', 'a'), 'ib': ('b', 'b'), 'iz': ('z', 'z'), 'ix': ('x', 'x'), 'r': ('a', 'z'), 'v': ('b', 'z'),
       'lam': ('z', 'x'), 'mu': ('z', 'x'), 'al': ('a', 'x'), 'be': ('b', 'x')}
idn = {'a': 'ia', 'b': 'ib', 'z': 'iz', 'x': 'ix'}
def comp(g, f):                # g after f
    assert arr[f][1] == arr[g][0]
    if f == idn[arr[f][0]]: return g
    if g == idn[arr[g][1]]: return f
    return {('lam', 'r'): 'al', ('mu', 'r'): 'al', ('lam', 'v'): 'be', ('mu', 'v'): 'be'}[(g, f)]
nonid = [k for k in arr if k not in idn.values()]
# nondegenerate nerve chains: 0-simplices objects; n-simplices strings of composable non-identity arrows
simp = {0: [(o,) for o in objs], 1: [(f,) for f in nonid]}
simp[2] = [(f, g) for f in nonid for g in nonid if arr[f][1] == arr[g][0]]
simp[3] = [(f, g, h) for (f, g) in simp[2] for h in nonid if arr[g][1] == arr[h][0]]
def faces(s):
    n = len(s)
    if n == 1:
        f = s[0]; return [((arr[f][1],), 1), ((arr[f][0],), -1)]
    out = [(s[1:], 1)]
    for i in range(1, n):
        c = comp(s[i], s[i - 1])
        t = s[:i - 1] + (c,) + s[i + 1:]
        out.append((t if c not in idn.values() else None, (-1) ** i))
    out.append((s[:-1], (-1) ** n))
    return out
def rank(M):
    M = [[Fraction(x) for x in row] for row in M]; r = 0
    rows, cols = len(M), len(M[0]) if M else 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                fct = M[i][c] / M[r][c]
                M[i] = [x - fct * y for x, y in zip(M[i], M[r])]
        r += 1
    return r
def bmat(n):
    idx = {s: i for i, s in enumerate(simp[n - 1])}
    M = [[0] * len(simp[n - 1]) for _ in simp[n]]
    for j, s in enumerate(simp[n]):
        for t, sg in faces(s):
            if t is not None: M[j][idx[t]] += sg
    return M
dims = [len(simp[k]) for k in range(4)]
rk = [0] + [rank(bmat(n)) if simp[n] else 0 for n in (1, 2, 3)]
betti = [dims[k] - rk[k] - (rk[k + 1] if k + 1 < 4 else 0) for k in range(3)]
print("4. Q: nondegenerate chains", dims, "; Betti numbers (rational) b0,b1,b2 =", betti)
# collapsing U={a,b,z} to a point: r, v become identities, so lam = lam r = al = mu r = mu : one arrow e -> x.

# ---------- 5 ----------
# trefoil group <x,y | x y x = y x y>; Fox derivatives of w = x y x y^-1 x^-1 y^-1, abelianized x,y -> t.
# d/dx: 1 + xy - x y x y^-1 x^-1 -> 1 + t^2 - t ; so the Alexander polynomial is t^2 - t + 1 (one-row matrix).
import sympy as sp
t = sp.symbols('t')
ddx = 1 + t * t - t
ddy = t - t * t - 1          # x - x y x y^-1 - x y x y^-1 x^-1 y^-1 -> t - t^2 - 1
assert sp.simplify(ddx + ddy) == 0
print("5. Fox row for the trefoil:", [sp.expand(ddx), sp.expand(ddy)], "; Alexander polynomial t^2 - t + 1;",
      "Lambda/(t^2-t+1) has rank 2 over Z, so H_1 of the infinite cyclic cover is Z^2, not 0")
