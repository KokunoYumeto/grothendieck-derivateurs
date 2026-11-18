#!/usr/bin/env python3
"""Independent finite-table checks for the finite-stage telescope in Part C3.

Only Python's standard library is used.  The uniform construction is proved
in the manuscript; this program checks actual composition tables, functors,
and transition squares for the six-element witness and stages 0,...,5.
Composition mul(g,f) means g after f.
"""
from dataclasses import dataclass


@dataclass
class Cat:
    objects: tuple
    arrows: dict
    identities: dict
    products: dict

    def mul(self, g, f):
        return self.products[g, f]

    def check(self):
        assert set(self.identities) == set(self.objects)
        assert set(self.arrows.values()) <= {
            (x, y) for x in self.objects for y in self.objects
        }
        outgoing = {x: [] for x in self.objects}
        for a, (x, y) in self.arrows.items():
            outgoing[x].append(a)
            assert self.mul(a, self.identities[x]) == a
            assert self.mul(self.identities[y], a) == a
        pairs = triples = 0
        for f, (x, y) in self.arrows.items():
            for g in outgoing[y]:
                z = self.arrows[g][1]
                gf = self.mul(g, f)
                assert self.arrows[gf] == (x, z)
                pairs += 1
                for h in outgoing[z]:
                    assert self.mul(h, gf) == self.mul(self.mul(h, g), f)
                    triples += 1
        assert pairs == len(self.products)
        return pairs, triples


@dataclass
class Functor:
    source: Cat
    target: Cat
    objects: dict
    arrows: dict

    def check(self):
        assert set(self.objects) == set(self.source.objects)
        assert set(self.arrows) == set(self.source.arrows)
        for x in self.source.objects:
            assert self.arrows[self.source.identities[x]] == \
                self.target.identities[self.objects[x]]
        for a, (x, y) in self.source.arrows.items():
            assert self.target.arrows[self.arrows[a]] == \
                (self.objects[x], self.objects[y])
        for (g, f), gf in self.source.products.items():
            assert self.arrows[gf] == self.target.mul(self.arrows[g], self.arrows[f])


def identity(c):
    return Functor(c, c, {x: x for x in c.objects}, {a: a for a in c.arrows})


def compose(g, f):
    assert f.target is g.source
    return Functor(f.source, g.target,
                   {x: g.objects[f.objects[x]] for x in f.source.objects},
                   {a: g.arrows[f.arrows[a]] for a in f.source.arrows})


def constant(c, d, obj):
    return Functor(c, d, {x: obj for x in c.objects},
                   {a: d.identities[obj] for a in c.arrows})


def monoid(extra):
    # 1 is represented by '1'; x_ij by (i,j); y_j by ('y',j).
    elements = ('1', (0, 0), (0, 1), (1, 0), (1, 1)) + \
        tuple(('y', j) for j in range(extra))

    def mul(a, b):
        if a == '1':
            return b
        if b == '1':
            return a
        ay = a[0] == 'y'
        by = b[0] == 'y'
        if ay and by:
            return (0, 0)
        if ay:
            return (0, b[1])
        if by:
            return (a[0], 0)
        return (a[0], b[1])

    return Cat((0,), {a: (0, 0) for a in elements}, {0: '1'},
               {(g, f): mul(g, f) for g in elements for f in elements})


def terminal():
    return Cat((0,), {'id': (0, 0)}, {0: 'id'}, {('id', 'id'): 'id'})


def spread(c, n):
    objects = tuple((i, x) for i in range(n + 1) for x in c.objects)
    arrows = {('id', i, x): ((i, x), (i, x))
              for i in range(n + 1) for x in c.objects}
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            for a, (x, y) in c.arrows.items():
                arrows[('a', i, j, a)] = ((i, x), (j, y))

    def mul(g, f):
        if f[0] == 'id':
            return g
        if g[0] == 'id':
            return f
        return ('a', f[1], g[2], c.mul(g[3], f[3]))

    products = {(g, f): mul(g, f)
                for g, (y, z) in arrows.items()
                for f, (x, yy) in arrows.items() if y == yy}
    p = Cat(objects, arrows, {(i, x): ('id', i, x) for i, x in objects}, products)
    forget = Functor(p, c, {(i, x): x for i, x in objects},
                     {a: c.identities[a[2]] if a[0] == 'id' else a[3]
                      for a in arrows})
    return p, forget


def span(a, b, c, f, g):
    """Grothendieck construction of b <- a -> c (covariant span)."""
    cats = (a, b, c)
    maps = {1: f, 2: g}
    objects = tuple((t, x) for t, d in enumerate(cats) for x in d.objects)
    arrows = {('i', t, h): ((t, x), (t, y))
              for t, d in enumerate(cats) for h, (x, y) in d.arrows.items()}
    for t, fun in maps.items():
        for x in a.objects:
            for h, (z, y) in cats[t].arrows.items():
                if z == fun.objects[x]:
                    arrows[('x', t, x, h)] = ((0, x), (t, y))

    def mul(v, u):
        if u[0] == v[0] == 'i':
            assert u[1] == v[1]
            t = u[1]
            return ('i', t, cats[t].mul(v[2], u[2]))
        if u[0] == 'i' and v[0] == 'x':
            assert u[1] == 0
            t = v[1]
            x = a.arrows[u[2]][0]
            return ('x', t, x, cats[t].mul(v[3], maps[t].arrows[u[2]]))
        if u[0] == 'x' and v[0] == 'i':
            t = u[1]
            assert v[1] == t
            return ('x', t, u[2], cats[t].mul(v[2], u[3]))
        raise AssertionError('two cross arrows cannot be composable in a span')

    products = {(v, u): mul(v, u)
                for v, (y, z) in arrows.items()
                for u, (x, yy) in arrows.items() if y == yy}
    d = Cat(objects, arrows,
            {(t, x): ('i', t, cats[t].identities[x]) for t, x in objects}, products)
    inclusions = tuple(Functor(cat, d,
                              {x: (t, x) for x in cat.objects},
                              {h: ('i', t, h) for h in cat.arrows})
                       for t, cat in enumerate(cats))
    return d, inclusions


def span_map(source, target, fa, fb, fc):
    maps = (fa, fb, fc)
    omap = {(t, x): (t, maps[t].objects[x]) for t, x in source.objects}
    amap = {}
    for a in source.arrows:
        if a[0] == 'i':
            amap[a] = ('i', a[1], maps[a[1]].arrows[a[2]])
        else:
            amap[a] = ('x', a[1], fa.objects[a[2]], maps[a[1]].arrows[a[3]])
    return Functor(source, target, omap, amap)


def equal(f, g):
    return f.objects == g.objects and f.arrows == g.arrows


def run(max_stage=5):
    m, sphere, pt = monoid(1), monoid(0), terminal()
    for c in (m, sphere, pt):
        c.check()
    stages = []
    print('S2COUNT C3 finite-stage table verification')
    print('n  P_objects P_arrows  K_objects K_arrows  J_objects J_arrows  J_pairs J_triples')
    for n in range(max_stage + 1):
        p, forget = spread(m, n)
        k, ki = span(p, pt, m, constant(p, pt, 0), forget)
        j, ji = span(pt, k, sphere, constant(pt, k, (2, 0)), constant(pt, sphere, 0))
        for c in (p, k, j):
            checks = c.check()
        for fun in (forget,) + ki + ji:
            fun.check()
        alpha = compose(ji[1], ki[2])
        beta = constant(m, j, (2, 0))
        alpha.check()
        beta.check()
        # Retraction to the fixed sphere summand.
        ro = {obj: 0 for obj in j.objects}
        ra = {}
        for a in j.arrows:
            if a[0] == 'i' and a[1] == 2:
                ra[a] = a[2]
            elif a[0] == 'x' and a[1] == 2:
                ra[a] = a[3]
            else:
                ra[a] = sphere.identities[0]
        retract = Functor(j, sphere, ro, ra)
        retract.check()
        assert equal(compose(retract, ji[2]), identity(sphere))
        assert equal(compose(retract, alpha), compose(retract, beta))
        print(n, len(p.objects), len(p.arrows), len(k.objects), len(k.arrows),
              len(j.objects), len(j.arrows), *checks)
        if stages:
            pp, kk, jj, aa, bb = stages[-1]
            incp = Functor(pp, p, {x: x for x in pp.objects}, {a: a for a in pp.arrows})
            inck = span_map(kk, k, incp, identity(pt), identity(m))
            incj = span_map(jj, j, identity(pt), inck, identity(sphere))
            for fun in (incp, inck, incj):
                fun.check()
            assert equal(compose(incj, aa), alpha)
            assert equal(compose(incj, bb), beta)
        stages.append((p, k, j, alpha, beta))
    print('PASS: all tables associative, all identities valid, all functors and transition squares checked.')
    print('The proof of nontriviality at every stage uses the all-degree integral homology theorem for BM,')
    print('not a finite-range homology inference.  The colimit equivalence uses the filtered comma category proof.')


if __name__ == '__main__':
    run()
