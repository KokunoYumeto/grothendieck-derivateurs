# Own checks for the review of the GALOIS answer. Claude (Fable 5.2), 11 November 2026.
# Written from the statements in sections/A.tex and sections/D.tex; no code of the answer is used.
# Run:  python -I check_galois.py > check_galois.out
from itertools import combinations, product


class Cat:
    """Finite category: objects, arrows (hashable), src, tgt, comp(g, f) = g after f, ident."""

    def __init__(self, objs, arrows, src, tgt, comp, ident):
        self.objs = list(objs)
        self.arrows = list(arrows)
        self.src, self.tgt, self.comp, self.ident = src, tgt, comp, ident

    def check(self):
        A = set(self.arrows)
        out = {x: [f for f in self.arrows if self.src[f] == x] for x in self.objs}
        pairs = triples = 0
        for f in self.arrows:
            assert self.comp(f, self.ident[self.src[f]]) == f
            assert self.comp(self.ident[self.tgt[f]], f) == f
            for g in out[self.tgt[f]]:
                gf = self.comp(g, f)
                assert gf in A and self.src[gf] == self.src[f] and self.tgt[gf] == self.tgt[g]
                pairs += 1
                for h in out[self.tgt[g]]:
                    assert self.comp(h, gf) == self.comp(self.comp(h, g), f)
                    triples += 1
        return pairs, triples

    def components(self):
        parent = {x: x for x in self.objs}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for f in self.arrows:
            parent[find(self.src[f])] = find(self.tgt[f])
        return len({find(x) for x in self.objs})

    def h1_mod2(self):
        """dim H_1 of the nerve with F_2 coefficients (normalized chains)."""
        ids = set(self.ident.values())
        nd = [f for f in self.arrows if f not in ids]
        idx = {f: i for i, f in enumerate(nd)}
        oidx = {x: i for i, x in enumerate(self.objs)}
        d1 = []
        for f in nd:
            v = 0
            if self.src[f] != self.tgt[f]:
                v = (1 << oidx[self.src[f]]) | (1 << oidx[self.tgt[f]])
            d1.append(v)
        out = {x: [f for f in nd if self.src[f] == x] for x in self.objs}
        d2 = []
        for f in nd:
            for g in out[self.tgt[f]]:
                v = (1 << idx[f]) ^ (1 << idx[g])
                gf = self.comp(g, f)
                if gf not in ids:
                    v ^= 1 << idx[gf]
                d2.append(v)
        return len(nd) - rank2(d1) - rank2(d2), len(nd), len(d2)


def rank2(rows):
    basis = {}
    r = 0
    for v in rows:
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                r += 1
                break
    return r


print("== A.5: the 1-complete class for set coefficients fails two-out-of-three (e -> BC_2 -> e)")
G = [0, 1]
R = [0, 1]  # regular C_2-set, s acts by x -> x+1
funcs = list(product(R, repeat=2))
equiv = [f for f in funcs if all(f[(x + 1) % 2] == (f[x] + 1) % 2 for x in R)]
print("functions R -> R:", len(funcs), "| equivariant:", len(equiv))
print("fixed points of R:", [x for x in R if (x + 1) % 2 == x], "| orbits of R: 1 | points of underlying set: 2")
# trivial actions: every function between trivial C_2-sets is equivariant, so r^* is fully faithful.
assert len(funcs) == 4 and len(equiv) == 2

print()
print("== D.3: composition fails for the weak rational fibrations (E -> B -> [1])")
# B: objects a, b; arrows: id_a; ('b', g) automorphisms of b; ('ab', g): a -> b.  Postcomposition adds labels.
Bobj = ['a', 'b']
Barr = [('ida',)] + [('b', g) for g in G] + [('ab', g) for g in G]
Bsrc = {('ida',): 'a', **{('b', g): 'b' for g in G}, **{('ab', g): 'a' for g in G}}
Btgt = {('ida',): 'a', **{('b', g): 'b' for g in G}, **{('ab', g): 'b' for g in G}}


def Bcomp(g, f):
    if f == ('ida',):
        return g
    if f[0] == 'ab':
        return ('ab', (f[1] + g[1]) % 2)
    return ('b', (f[1] + g[1]) % 2)


Bc = Cat(Bobj, Barr, Bsrc, Btgt, Bcomp, {'a': ('ida',), 'b': ('b', 0)})
print("B: objects", len(Bobj), "arrows", len(Barr), "| composable pairs, triples checked:", Bc.check())


def label(f):
    return 0 if f == ('ida',) else f[1]


# E = category of elements of L, L(a) = L(b) = C_2, the arrow with label g acts by z -> g + z
Eobj = [(x, z) for x in Bobj for z in G]
Earr = [(f, z) for f in Barr for z in G]
Esrc = {(f, z): (Bsrc[f], z) for f in Barr for z in G}
Etgt = {(f, z): (Btgt[f], (z + label(f)) % 2) for f in Barr for z in G}
Ec = Cat(Eobj, Earr, Esrc, Etgt, lambda g, f: (Bcomp(g[0], f[0]), f[1]),
         {(x, z): (Bc.ident[x], z) for x in Bobj for z in G})
print("E: objects", len(Eobj), "arrows", len(Earr), "| pairs, triples:", Ec.check())
# covering: each base arrow has exactly one lift with given source and exactly one with given target
for f in Barr:
    for z in G:
        assert sum(1 for e in Earr if e[0] == f and Esrc[e] == (Bsrc[f], z)) == 1
        assert sum(1 for e in Earr if e[0] == f and Etgt[e] == (Btgt[f], z)) == 1
print("p: E -> B is a covering (unique lifts with prescribed source, and with prescribed target)")


def full_sub(C, objs):
    objs = set(objs)
    arr = [f for f in C.arrows if C.src[f] in objs and C.tgt[f] in objs]
    return Cat(list(objs), arr, C.src, C.tgt, C.comp, {x: C.ident[x] for x in objs})


F0 = full_sub(Ec, [('a', z) for z in G])
F1 = full_sub(Ec, [('b', z) for z in G])
print("fibre of qp over 0: objects", len(F0.objs), "arrows", len(F0.arrows), "components", F0.components())
print("fibre of qp over 1: objects", len(F1.objs), "arrows", len(F1.arrows), "components", F1.components(),
      "| exactly one arrow between each ordered pair:",
      all(sum(1 for f in F1.arrows if F1.src[f] == x and F1.tgt[f] == y) == 1 for x in F1.objs for y in F1.objs))
assert F0.components() == 2 and F1.components() == 1
print("H^0 with constant rational coefficients: Q^2 over 0 and Q over 1: the direct image of the constant")
print("coefficient along qp is not locally constant, while q (transport e -> BC_2, rationally a constant-")
print("coefficient equivalence) and p (a covering) each have the weak property.")
print("D.12 uses the same two categories: G_disc -> EG is the pullback of e -> BC_2 along EG -> BC_2;")
print("components 2 and 1, so the pullback of a W_0-map along a covering is not in W_0.")

print()
print("== D.4 / D.5: the twisted C_2-extension H of the face poset K of the tetrahedron boundary")
verts = [0, 1, 2, 3]
Kobj = [frozenset(s) for n in (1, 2, 3) for s in combinations(verts, n)]
Karr = [(x, y) for x in Kobj for y in Kobj if x <= y]
print("K: objects", len(Kobj), "arrows", len(Karr), "| strict inclusions", sum(1 for x, y in Karr if x != y),
      "| chains x<y<z", sum(1 for x, y in Karr if x != y for z in Kobj if y < z))
sigma = (frozenset({0}), frozenset({0, 1}), frozenset({0, 1, 2}))


def make_H(twist):
    def c(u, v):
        return 1 if twist and (u[0], u[1], v[1]) == sigma else 0
    arr = [(u, m) for u in Karr for m in G]
    src = {(u, m): u[0] for u in Karr for m in G}
    tgt = {(u, m): u[1] for u in Karr for m in G}

    def comp(g, f):
        return ((f[0][0], g[0][1]), (f[1] + g[1] + c(f[0], g[0])) % 2)
    return Cat(Kobj, arr, src, tgt, comp, {x: ((x, x), 0) for x in Kobj})


for twist in (True, False):
    H = make_H(twist)
    pairs, triples = H.check()
    h1, n1, n2 = H.h1_mod2()
    print("H (cocycle %s): objects %d arrows %d | composable pairs %d triples %d | components %d | dim H_1(F_2) = %d"
          % ("on sigma" if twist else "zero", len(H.objs), len(H.arrows), pairs, triples, H.components(), h1))

# E = B x_K H, where B = K with a new object a, B(a, x) = K(x0, x), r(a) = x0
x0 = frozenset({0})


def make_E(twist):
    def c(u, v):
        return 1 if twist and (u[0], u[1], v[1]) == sigma else 0
    objs = Kobj + ['a']
    barr = [('k', x, y) for (x, y) in Karr] + [('a', 'a', y) for y in Kobj if x0 <= y] + [('a', 'a', 'a')]

    def r(o):
        return x0 if o == 'a' else o
    arr = [(b, m) for b in barr for m in G]
    src = {(b, m): b[1] for b in barr for m in G}
    tgt = {(b, m): b[2] for b in barr for m in G}

    def comp(g, f):
        b1, b2 = f[0], g[0]
        s, t = b1[1], b2[2]
        kind = 'a' if s == 'a' else 'k'
        u = (r(b1[1]), r(b1[2]))
        v = (r(b2[1]), r(b2[2]))
        return ((kind, s, t), (f[1] + g[1] + c(u, v)) % 2)
    ident = {x: (('k', x, x), 0) for x in Kobj}
    ident['a'] = (('a', 'a', 'a'), 0)
    return Cat(objs, arr, src, tgt, comp, ident)


for twist in (True, False):
    E = make_E(twist)
    pairs, triples = E.check()
    h1, n1, n2 = E.h1_mod2()
    Fa = full_sub(E, ['a'])
    print("E (cocycle %s): objects %d arrows %d | pairs %d triples %d | components %d | dim H_1(F_2) = %d | fibre over 0: %d object, %d arrows"
          % ("on sigma" if twist else "zero", len(E.objs), len(E.arrows), pairs, triples, E.components(), h1,
             len(Fa.objs), len(Fa.arrows)))
print("Reading: H -> K is a fibration and opfibration with fibre BC_2 and identity transports, so BH -> BK = S^2 is")
print("a homotopy fibre sequence (Quillen's Theorem B) and pi_1(BH) is a quotient of C_2; it is then abelian and")
print("equals H_1. With the cocycle on sigma H_1(F_2) = 0, so BH is simply connected; with the zero cocycle it is C_2.")
print("E retracts onto H up to natural transformation; its fibre over 0 in [1] is BC_2, and BC_2 -> E is not in W_1.")
