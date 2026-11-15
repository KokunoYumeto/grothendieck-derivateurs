"""Independent finite certificate for absolute Theorem A != relative Theorem A.

The global class is defined in the proof: pi_0-bijections, with the additional
W_infinity requirement only when source and target are connected.  Its global
axioms are established mathematically, not inferred from this finite program.
For finite groupoids, W_infinity is checked exactly by equivalence of groupoids.
No other audit or search program is imported.
"""

from dataclasses import dataclass
from itertools import product
from pathlib import Path


LOG = []


def say(value):
    LOG.append(str(value))


@dataclass
class Category:
    name: str
    objects: tuple
    arrows: tuple
    source: dict
    target: dict
    identity: dict
    composition: dict  # (second, first) -> second o first

    def validate(self):
        assert set(self.source) == set(self.target) == set(self.arrows)
        assert set(self.identity) == set(self.objects)
        pairs = {(b, a) for b, a in product(self.arrows, repeat=2)
                 if self.target[a] == self.source[b]}
        assert set(self.composition) == pairs
        for x in self.objects:
            i = self.identity[x]
            assert self.source[i] == self.target[i] == x
        for a in self.arrows:
            assert self.composition[a, self.identity[self.source[a]]] == a
            assert self.composition[self.identity[self.target[a]], a] == a
        triples = 0
        for b, a in pairs:
            ba = self.composition[b, a]
            assert self.source[ba] == self.source[a]
            assert self.target[ba] == self.target[b]
            for c in self.arrows:
                if self.source[c] == self.target[b]:
                    triples += 1
                    assert self.composition[c, ba] == self.composition[self.composition[c, b], a]
        say(f'PASS {self.name}: units, {len(pairs)} composition pairs, {triples} associative triples')

    def dump(self):
        say(f'CATEGORY {self.name}: objects={self.objects!r}')
        for a in self.arrows:
            say(f'  arrow {a!r}: {self.source[a]!r} -> {self.target[a]!r}')
        say(f'  identities={self.identity!r}')
        for (b, a), ba in self.composition.items():
            say(f'  compose({b!r}, {a!r}) = {ba!r}')

    def components(self):
        todo = set(self.objects)
        components = []
        while todo:
            component = {next(x for x in self.objects if x in todo)}
            while True:
                bigger = component | {
                    self.target[a] for a in self.arrows if self.source[a] in component
                } | {
                    self.source[a] for a in self.arrows if self.target[a] in component
                }
                if bigger == component:
                    break
                component = bigger
            todo -= component
            components.append(frozenset(component))
        return tuple(components)

    def hom(self, x, y):
        return tuple(a for a in self.arrows if self.source[a] == x and self.target[a] == y)

    def check_groupoid(self):
        inverses = {}
        for a in self.arrows:
            possible = [b for b in self.hom(self.target[a], self.source[a])
                        if self.composition[b, a] == self.identity[self.source[a]]
                        and self.composition[a, b] == self.identity[self.target[a]]]
            assert len(possible) == 1
            inverses[a] = possible[0]
        say(f'PASS {self.name}: all arrows invertible, inverses={inverses!r}')
        for x in self.objects:
            group = self.hom(x, x)
            multiplication = [[self.composition[b, a] for a in group] for b in group]
            say(f'  Aut({x!r})={group!r}; multiplication rows=second, columns=first: {multiplication!r}')


@dataclass
class Functor:
    name: str
    domain: Category
    codomain: Category
    objects: dict
    arrows: dict

    def validate(self):
        assert set(self.objects) == set(self.domain.objects)
        assert set(self.arrows) == set(self.domain.arrows)
        for a in self.domain.arrows:
            fa = self.arrows[a]
            assert self.codomain.source[fa] == self.objects[self.domain.source[a]]
            assert self.codomain.target[fa] == self.objects[self.domain.target[a]]
        for x in self.domain.objects:
            assert self.arrows[self.domain.identity[x]] == self.codomain.identity[self.objects[x]]
        for (b, a), ba in self.domain.composition.items():
            assert self.arrows[ba] == self.codomain.composition[self.arrows[b], self.arrows[a]]
        say(f'PASS functor {self.name}: objects={self.objects!r}; arrows={self.arrows!r}')

    def component_map(self):
        ds = self.domain.components()
        cs = self.codomain.components()
        images = []
        for d in ds:
            candidates = [j for j, c in enumerate(cs)
                          if {self.objects[x] for x in d} <= c]
            assert len(candidates) == 1
            images.append(candidates[0])
        return tuple(images)

    def component_bijection(self):
        images = self.component_map()
        return len(images) == len(set(images)) == len(self.codomain.components())

    def fully_faithful(self):
        for x, y in product(self.domain.objects, repeat=2):
            ds = self.domain.hom(x, y)
            cs = self.codomain.hom(self.objects[x], self.objects[y])
            images = [self.arrows[a] for a in ds]
            if len(images) != len(set(images)) or set(images) != set(cs):
                return False
        return True

    def w_for_finite_groupoids(self):
        if not self.component_bijection():
            return False
        return len(self.domain.components()) != 1 or self.fully_faithful()


def groupoid(name, objects, labels):
    """Chaotic groupoid on objects times the one-object additive label group."""
    arrows = tuple((x, y, k) for x, y in product(objects, repeat=2) for k in labels)
    source = {a: a[0] for a in arrows}
    target = {a: a[1] for a in arrows}
    identity = {x: (x, x, 0) for x in objects}
    composition = {(b, a): (a[0], b[1], a[2] ^ b[2])
                   for b, a in product(arrows, repeat=2) if a[1] == b[0]}
    return Category(name, tuple(objects), arrows, source, target, identity, composition)


def comma(functor, c, name):
    """Literal over-comma category, constructed using its defining equation."""
    D, C = functor.domain, functor.codomain
    objects = tuple((x, g) for x in D.objects
                    for g in C.hom(functor.objects[x], c))
    arrows = []
    source, target = {}, {}
    for (x, g), (y, h) in product(objects, repeat=2):
        for a in D.hom(x, y):
            if C.composition[h, functor.arrows[a]] == g:
                identifier = (a, g, h)
                arrows.append(identifier)
                source[identifier], target[identifier] = (x, g), (y, h)
    arrows = tuple(arrows)
    identity = {(x, g): (D.identity[x], g, g) for x, g in objects}
    composition = {(b, a): (D.composition[b[0], a[0]], a[1], b[2])
                   for b, a in product(arrows, repeat=2) if target[a] == source[b]}
    return Category(name, objects, arrows, source, target, identity, composition)


def coproduct(left, right, name):
    cats = {0: left, 1: right}
    objects = tuple((t, x) for t, C in cats.items() for x in C.objects)
    arrows = tuple((t, a) for t, C in cats.items() for a in C.arrows)
    source = {(t, a): (t, cats[t].source[a]) for t, a in arrows}
    target = {(t, a): (t, cats[t].target[a]) for t, a in arrows}
    identity = {(t, x): (t, cats[t].identity[x]) for t, x in objects}
    composition = {((t, b), (t, a)): (t, ba)
                   for t, C in cats.items() for (b, a), ba in C.composition.items()}
    return Category(name, objects, arrows, source, target, identity, composition)


C = groupoid('C=BC2', ('*',), (0, 1))
B = groupoid('B=E(C2)', (0, 1), (0,))
A = groupoid('A=E(C2) x BC2', (0, 1), (0, 1))
point = groupoid('e', ('*',), (0,))

p = Functor('p:B->C', B, C,
            {x: '*' for x in B.objects},
            {a: ('*', '*', a[0] ^ a[1]) for a in B.arrows})
u = Functor('u:A->B', A, B, {x: x for x in A.objects},
            {a: (a[0], a[1], 0) for a in A.arrows})
pu = Functor('p u:A->C', A, C, {x: '*' for x in A.objects},
             {a: p.arrows[u.arrows[a]] for a in A.arrows})

for cat in (C, B, A, point):
    cat.dump()
    cat.validate()
    cat.check_groupoid()
    say(f'  components={cat.components()!r}')
for functor in (p, u, pu):
    functor.validate()

BC = comma(p, '*', 'B/c')
AC = comma(pu, '*', 'A/c')
uc = Functor('u/c:A/c->B/c', AC, BC,
             {x: x for x in AC.objects},
             {(a, g, h): (u.arrows[a], g, h) for a, g, h in AC.arrows})
for cat in (BC, AC):
    cat.dump()
    cat.validate()
    cat.check_groupoid()
    say(f'  components={cat.components()!r}')
uc.validate()

assert len(A.components()) == len(B.components()) == 1
assert u.component_bijection()
assert not u.fully_faithful()
assert not u.w_for_finite_groupoids()
assert len(AC.objects) == len(BC.objects) == 4
assert len(AC.arrows) == 16 and len(BC.arrows) == 8
assert len(AC.components()) == len(BC.components()) == 2
assert uc.component_bijection()
assert uc.w_for_finite_groupoids()
assert not uc.fully_faithful()

for cat in (BC, AC):
    # Each comma object is (x, g); g is the unique-object C2 arrow (*,*,k).
    invariants = {obj: obj[0] ^ obj[1][2] for obj in cat.objects}
    for a in cat.arrows:
        assert invariants[cat.source[a]] == invariants[cat.target[a]]
    assert {frozenset(x for x in cat.objects if invariants[x] == t) for t in (0, 1)} == set(cat.components())
    say(f'PASS {cat.name}: components are exactly the level sets of t=x+g in C2')

say('PASS global u: connected groupoids, Aut_A(0)=C2 -> Aut_B(0)=1; u is not W')
say('PASS only comma comparison u/c: four objects, two components; pi_0 bijective, so u/c is W')
say('PASS relative Theorem A fails at the one-object, two-arrow base BC2')

# Complete arrow-category retract showing why full retract saturation is absent.
D = coproduct(C, point, 'BC2 coproduct e')
Q = coproduct(point, point, 'e coproduct e')
f = Functor('f:BC2->e', C, point, {'*': '*'}, {a: point.identity['*'] for a in C.arrows})
w = Functor('w:BC2+e->e+e', D, Q, {x: x for x in D.objects},
            {(t, a): (t, point.identity['*']) for t, a in D.arrows})
alpha = Functor('alpha:BC2->BC2+e', C, D, {'*': (0, '*')},
                {a: (0, a) for a in C.arrows})
rho = Functor('rho:BC2+e->BC2', D, C, {x: '*' for x in D.objects},
              {(t, a): a if t == 0 else C.identity['*'] for t, a in D.arrows})
beta = Functor('beta:e->e+e', point, Q, {'*': (0, '*')},
               {a: (0, a) for a in point.arrows})
sigma = Functor('sigma:e+e->e', Q, point, {x: '*' for x in Q.objects},
                {a: point.identity['*'] for a in Q.arrows})
for cat in (D, Q):
    cat.dump()
    cat.validate()
    cat.check_groupoid()
    say(f'  components={cat.components()!r}')
for functor in (f, w, alpha, rho, beta, sigma):
    functor.validate()
for x in C.objects:
    assert rho.objects[alpha.objects[x]] == x
    assert w.objects[alpha.objects[x]] == beta.objects[f.objects[x]]
for a in C.arrows:
    assert rho.arrows[alpha.arrows[a]] == a
    assert w.arrows[alpha.arrows[a]] == beta.arrows[f.arrows[a]]
for x in point.objects:
    assert sigma.objects[beta.objects[x]] == x
for a in point.arrows:
    assert sigma.arrows[beta.arrows[a]] == a
for x in D.objects:
    assert f.objects[rho.objects[x]] == sigma.objects[w.objects[x]]
for a in D.arrows:
    assert f.arrows[rho.arrows[a]] == sigma.arrows[w.arrows[a]]
assert w.w_for_finite_groupoids() and not f.w_for_finite_groupoids()
say('PASS arrow-category retract: rho alpha=Id, sigma beta=Id, w alpha=beta f, f rho=sigma w')
say('PASS w is W (two components), but its retract f is not W (connected and nonfaithful)')
say('CONCLUSION: finite certificate confirms the relative failure and the failure of full arrow-retract closure')

output = Path(__file__).with_suffix('.out.txt')
output.write_text('\n'.join(LOG) + '\n')
for line in LOG:
    if line.startswith('PASS') or line.startswith('CONCLUSION'):
        print(line)
print('Complete category and functor tables:', output)
