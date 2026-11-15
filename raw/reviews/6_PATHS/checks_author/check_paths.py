# Own checks for the review of the PATHS answer (GPT-6 Astra, ChatGPT Pro mode).
# Written by Claude Fable 5.2, 11 Nov 2026. Uses nothing from the answer's code folder.
# Run: python -I check_paths.py > check_paths.out
import itertools
from fractions import Fraction

# ---------------------------------------------------------------- finite categories
class Cat:
    """objects: list; arrows: dict name -> (src, tgt); comp: dict (g, f) -> name of g after f.
    Identities are named ('id', x)."""
    def __init__(self, objects, arrows, comp):
        self.ob = list(objects)
        self.ar = dict(arrows)
        for x in self.ob:
            self.ar[('id', x)] = (x, x)
        self.comp = dict(comp)

    def c(self, g, f):
        assert self.ar[f][1] == self.ar[g][0], (g, f)
        if f[0] == 'id' if isinstance(f, tuple) else False:
            return g
        if g[0] == 'id' if isinstance(g, tuple) else False:
            return f
        return self.comp[(g, f)]

    def is_id(self, f):
        return isinstance(f, tuple) and f[0] == 'id'

    def check(self):
        A = list(self.ar)
        n = 0
        for f in A:
            for g in A:
                if self.ar[f][1] != self.ar[g][0]:
                    continue
                gf = self.c(g, f)
                assert self.ar[gf] == (self.ar[f][0], self.ar[g][1])
                for h in A:
                    if self.ar[g][1] != self.ar[h][0]:
                        continue
                    assert self.c(h, gf) == self.c(self.c(h, g), f)
                    n += 1
        return n

    def betti(self, top=5):
        """rational Betti numbers of the nerve, by nondegenerate simplices."""
        non = [f for f in self.ar if not self.is_id(f)]
        simp = [[(x,) for x in self.ob], [(f,) for f in non]]
        while len(simp) <= top + 1:
            nxt = [s + (g,) for s in simp[-1] for g in non if self.ar[s[-1]][1] == self.ar[g][0]]
            if not nxt:
                break
            simp.append(nxt)
        idx = [{s: i for i, s in enumerate(level)} for level in simp]

        def faces(s, n):
            out = []
            if n == 1:
                f = s[0]
                return [((self.ar[f][1],), 1), ((self.ar[f][0],), -1)]
            out.append((s[1:], 1))
            for i in range(1, n):
                g = self.c(s[i], s[i - 1])
                if not self.is_id(g):
                    out.append((s[:i - 1] + (g,) + s[i + 1:], (-1) ** i))
            out.append((s[:-1], (-1) ** n))
            return out

        ranks = [0]
        for n in range(1, len(simp)):
            rows = []
            for s in simp[n]:
                row = {}
                for t, sg in faces(s, n):
                    j = idx[n - 1][t]
                    row[j] = row.get(j, 0) + sg
                rows.append({j: Fraction(v) for j, v in row.items() if v})
            ranks.append(rank(rows))
        ranks.append(0)
        return [len(simp[n]) - ranks[n] - ranks[n + 1] for n in range(min(top + 1, len(simp)))], [len(l) for l in simp]


def rank(rows):
    piv = {}
    r = 0
    for row in rows:
        row = dict(row)
        while row:
            j = min(row)
            if j in piv:
                p = piv[j]
                c = row[j] / p[j]
                for k, v in p.items():
                    nv = row.get(k, 0) - c * v
                    if nv == 0:
                        row.pop(k, None)
                    else:
                        row[k] = nv
            else:
                piv[j] = row
                r += 1
                break
    return r


def poset_cat(elements, leq):
    ar = {}
    for x in elements:
        for y in elements:
            if x != y and leq(x, y):
                ar[(x, y)] = (x, y)
    comp = {}
    for (x, y) in ar:
        for (y2, z) in ar:
            if y == y2:
                comp[((y, z), (x, y))] = (x, z)
    return Cat(elements, ar, comp)


def monotone_maps(src, leq_s, tgt, leq_t):
    rel = [(x, y) for x in src for y in src if x != y and leq_s(x, y)]
    for vals in itertools.product(tgt, repeat=len(src)):
        f = dict(zip(src, vals))
        if all(leq_t(f[x], f[y]) for x, y in rel):
            yield f

print("== A.9, D.10, D.13: the face poset P of the boundary of a triangle")
V = [frozenset([i]) for i in range(3)]
E = [frozenset([0, 1]), frozenset([1, 2]), frozenset([0, 2])]
P = V + E
leqP = lambda x, y: x <= y
cycP = [V[0], E[0], V[1], E[1], V[2], E[2]]           # hexagon
posP = {x: i for i, x in enumerate(cycP)}

def degree(f, cyc_src, pos_t, m):
    # winding of the image of the closed hexagon; successive images are equal or adjacent in the m-cycle
    tot = 0
    k = len(cyc_src)
    for i in range(k):
        a, b = pos_t[f[cyc_src[i]]], pos_t[f[cyc_src[(i + 1) % k]]]
        d = (b - a) % m
        if d == m - 1:
            d = -1
        assert d in (-1, 0, 1), d
        tot += d
    assert tot % m == 0
    return tot // m

cnt = {}
for f in monotone_maps(P, leqP, P, leqP):
    d = degree(f, cycP, posP, 6)
    cnt[d] = cnt.get(d, 0) + 1
print("monotone maps P -> P by degree:", dict(sorted(cnt.items())), "total", sum(cnt.values()))

sd = [frozenset([x]) for x in P] + [frozenset([v, e]) for v in V for e in E if v < e]
leqS = lambda x, y: x <= y
cycS = []
for i in range(6):
    a, b = cycP[i], cycP[(i + 1) % 6]
    cycS += [frozenset([a]), frozenset([a, b])]
posS = {x: i for i, x in enumerate(cycS)}
assert len(set(cycS)) == 12 and set(cycS) == set(sd)
cnt = {}
for f in monotone_maps(P, leqP, sd, leqS):
    d = degree(f, cycP, posS, 12)
    cnt[d] = cnt.get(d, 0) + 1
print("monotone maps P -> sd P by degree:", dict(sorted(cnt.items())), "total", sum(cnt.values()))
last = {c: max(c, key=len) for c in sd}               # last element of a chain = its largest face
print("degree of the last-element map sd P -> P:", degree(last, cycS, posP, 6))
print("Betti of BP:", poset_cat(P, leqP).betti()[0])

print("== D.9: the diamond 0 < a, b < 1 with W = identities, 0->a, 0->b")
D4 = ['0', 'a', 'b', '1']
le = lambda x, y: x == y or x == '0' or y == '1'
join = lambda x, y: y if le(x, y) else x if le(y, x) else '1'
W = {(x, x) for x in D4} | {('0', 'a'), ('0', 'b')}
maps = [(x, y) for x in D4 for y in D4 if le(x, y)]
two3 = all(((x, y) in W) + ((y, z) in W) + ((x, z) in W) != 2 for x in D4 for y in D4 for z in D4 if le(x, y) and le(y, z))
def intrinsic(i):
    A, B = i
    # pushout functor A\M -> B\M, X |-> X v B, must send W-maps under A to W-maps
    return all((join(X, B), join(Y, B)) in W for (X, Y) in W if le(A, X))
cof = [m for m in maps if intrinsic(m)]
print("two-out-of-three:", two3)
print("intrinsic cofibrations:", cof)
fact = all(any((x, t) in cof and (t, y) in W for t in D4 if le(x, t) and le(t, y)) for (x, y) in maps)
print("every map = intrinsic cofibration then W:", fact, "; cofibrant objects:", [x for x in D4 if ('0', x) in cof])

print("== D.12: the nine-vertex fence; edges of Ex^2 are monotone maps of the five-vertex fence")
fle = lambda x, y: x == y or (x % 2 == 0 and abs(x - y) == 1)
F5, F9 = list(range(5)), list(range(9))
ends = set((f[0], f[4]) for f in monotone_maps(F5, fle, F9, fle))
print("(0,4) in edges:", (0, 4) in ends, " (4,8):", (4, 8) in ends, " (0,8):", (0, 8) in ends)

print("== D.2, D.3: the pointed category E with objects 0, x and End(x) = {1, z}")
arE = {'u': ('0', 'x'), 'v': ('x', '0'), 'z': ('x', 'x')}
compE = {('v', 'u'): ('id', '0'), ('u', 'v'): 'z', ('z', 'z'): 'z', ('z', 'u'): 'u', ('v', 'z'): 'v'}
Ecat = Cat(['0', 'x'], arE, compE)
print("associativity triples checked:", Ecat.check())
hom = lambda a, b: [f for f, (s, t) in Ecat.ar.items() if (s, t) == (a, b)]
print("|Hom(x,p)| for p = 0, x:", len(hom('x', '0')), len(hom('x', 'x')), " needed for x*x:", len(hom('x', 'x')) ** 2)

print("== D.5: X = suspension of the crown Y; B = two parallel arrows")
Y = ['r0', 'r1', 'q0', 'q1']
X = Y + ['s', 'n']
def leX(a, b):
    if a == b: return True
    if a[0] == 'r' and b[0] == 'q': return True
    if a in Y and b in ('s', 'n'): return True
    return False
print("Betti of BY:", poset_cat(Y, leX).betti()[0], " Betti of BX:", poset_cat(X, leX).betti()[0])
Bcat = Cat(['a', 'b'], {'f': ('a', 'b'), 'g': ('a', 'b')}, {})
print("Betti of BB:", Bcat.betti()[0])
img = {('r0', 'q0'): 'f', ('r1', 'q0'): 'f', ('r1', 'q1'): 'f', ('r0', 'q1'): 'g'}
gamma = {('r0', 'q0'): 1, ('r1', 'q0'): -1, ('r1', 'q1'): 1, ('r0', 'q1'): -1}
im = {}
for e, c in gamma.items():
    im[img[e]] = im.get(img[e], 0) + c
print("image of the cycle gamma in B:", im, "(f - g generates H_1(BB))")
nYB = sum(1 for _ in monotone_maps(Y, leX, X, leX))
print("objects of X^Y:", nYB, " objects of X^B = arrows of X incl. identities:", sum(1 for a in X for b in X if leX(a, b)))

print("== D.19: e -> BC2 -> e and locally constant sets")
C2 = [0, 1]
endo = list(itertools.product(C2, repeat=2))
equi = [h for h in endo if all(h[(x + 1) % 2] == (h[x] + 1) % 2 for x in C2)]
print("endofunctions of the regular C2-set:", len(endo), " equivariant:", len(equi))

print("== D.23: alpha(x) = x, alpha(y) = y x y x^-1 y^-1 on the free group; images in S3")
def mul(p, q): return tuple(p[q[i]] for i in range(3))
def inv(p):
    r = [0] * 3
    for i, v in enumerate(p): r[v] = i
    return tuple(r)
def gen(gs):
    S = {(0, 1, 2)}
    fr = list(S)
    while fr:
        n = [mul(a, g) for a in fr for g in gs]
        fr = [x for x in set(n) if x not in S]
        S |= set(fr)
    return S
x, y = (1, 0, 2), (2, 1, 0)
ay = mul(mul(mul(mul(y, x), y), inv(x)), inv(y))
print("rho(alpha(y)) == rho(x):", ay == x, " |<rho x, rho y>| =", len(gen([x, y])), " |<rho alpha x, rho alpha y>| =", len(gen([x, ay])))

print("== E.6, E.11: the five-element monoid R = {1, e_ij}, e_ij e_kl = e_il")
R = ['1'] + [(i, j) for i in range(2) for j in range(2)]
def rm(a, b):
    if a == '1': return b
    if b == '1': return a
    return (a[0], b[1])
print("associative:", all(rm(rm(a, b), c) == rm(a, rm(b, c)) for a in R for b in R for c in R),
      " e*r and r*e never the unit:", all(rm((0, 0), r) != '1' and rm(r, (0, 0)) != '1' for r in R))
arR = {r: ('*', '*') for r in R if r != '1'}
compR = {(a, b): rm(a, b) for a in arR for b in arR}
print("Betti of BR through degree 4:", Cat(['*'], arR, compR).betti(top=4)[0])

print("== E.7, E.12: the category C (type S^2), its cone D, and the pushout Q for n = 1")
arC = {'lam': ('x', 'z'), 'mu': ('x', 'z'), 'r': ('z', 'a'), 'v': ('z', 'b'), 'eta': ('x', 'a'), 'theta': ('x', 'b')}
compC = {('r', 'lam'): 'eta', ('r', 'mu'): 'eta', ('v', 'lam'): 'theta', ('v', 'mu'): 'theta'}
C = Cat(['x', 'z', 'a', 'b'], arC, compC)
print("C: associativity triples", C.check(), " Betti", C.betti()[0])
# E.12: the fork z->a, z->b in C is final: c\Y nonempty connected for every c
fork = ['z', 'a', 'b']
for c in C.ob:
    obj = [(y, f) for y in fork for f, (s, t) in C.ar.items() if (s, t) == (c, y)]
    par = {o: o for o in obj}
    def find(o):
        while par[o] != o: o = par[o]
        return o
    for (y, f) in obj:
        for g, (s, t) in C.ar.items():
            if s == y and t in fork and g in ('r', 'v', ('id', 'z'), ('id', 'a'), ('id', 'b')):
                par[find((y, f))] = find((t, C.c(g, f)))
    print("  comma category %s\\fork: %d objects, %d components" % (c, len(obj), len({find(o) for o in obj})))
# D = C with a terminal object s
arD = dict(arC); compD = dict(compC)
for o in C.ob:
    arD[('t', o)] = (o, 's')
for f, (s, t) in arC.items():
    compD[(('t', t), f)] = ('t', s)
Dc = Cat(['x', 'z', 'a', 'b', 's'], arD, compD)
print("D = C with terminal object: triples", Dc.check(), " Betti", Dc.betti()[0])
# P_1 = [1] x (0 -> 1 <- 2); A_1 = sieve of the l_i, u_0, u_2
Pob = [(e, i) for e in (0, 1) for i in (0, 1, 2)]
phi = lambda i, j: i == j or j == 1
leP1 = lambda p, q: p[0] <= q[0] and phi(p[1], q[1])
P1 = poset_cat(Pob, leP1)
A1 = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]
print("Betti of P_1:", P1.betti()[0], " of A_1:", poset_cat(A1, leP1).betti()[0])
Fob = {(0, 0): 'z', (1, 0): 'b', (0, 1): 'a', (0, 2): 'a', (1, 2): 'a'}
Far = {((0, 0), (0, 1)): 'r', ((0, 0), (1, 0)): 'v', ((0, 2), (0, 1)): ('id', 'a'), ((0, 2), (1, 2)): ('id', 'a')}
assert all(leP1(p, q) for (p, q) in Far) and len(Far) == sum(1 for p in A1 for q in A1 if p != q and leP1(p, q))
# crossing arrows d -> u_1: coend over w in A_1 of D(d, F w) x P(w, u_1), P(w, u_1) a singleton
u1 = (1, 1)
assert all(leP1(w, u1) for w in A1)
cross = {}
for d in Dc.ob:
    el = [(w, f) for w in A1 for f, (s, t) in Dc.ar.items() if (s, t) == (d, Fob[w])]
    par = {o: o for o in el}
    def find(o):
        while par[o] != o: o = par[o]
        return o
    for (w, f) in el:
        for (p, q), g in Far.items():
            if p == w:
                par[find((w, f))] = find((q, Dc.c(g, f)))
    cross[d] = {o: find(o) for o in el}
    print("  Hom_Q(%s, u_1): %d classes" % (d, len(set(cross[d].values()))))
arQ = dict(arD); compQ = dict(compD)
for d in Dc.ob:
    for cl in set(cross[d].values()):
        arQ[('x', d, cl)] = (d, 'u1')
for d in Dc.ob:
    for (w, f), cl in cross[d].items():
        for g, (s, t) in Dc.ar.items():
            if t == d and not Dc.is_id(g):
                compQ[(('x', d, cl), g)] = ('x', s, cross[s][(w, Dc.c(f, g))])
Q = Cat(Dc.ob + ['u1'], arQ, compQ)
print("Q: objects", len(Q.ob), " arrows incl. identities", len(Q.ar), " associativity triples", Q.check())
print("Betti of Q:", Q.betti()[0], " (source of the cobase change: D, contractible; S^3 expected)")
