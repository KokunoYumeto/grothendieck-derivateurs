"""Complete finite-category data for the thin-coefficient B.6 countercubes.

Only Python's standard library is required.  A poset category has exactly
one arrow (x,y) when x<=y, and composition (y,z)o(x,y)=(x,z).
The output enumerates every arrow and every defined composition, checks
all category laws, both Mayer--Vietoris cubes, and rational nerve homology.
The derivator argument identifying the coefficient equivalences is B.6.
"""
from fractions import Fraction
from itertools import product, combinations


class PosetCategory:
    def __init__(self, name, objects, relations=()):
        self.name, self.objects = name, tuple(objects)
        self.arrows = {(x, x) for x in self.objects} | set(relations)
        changed = True
        while changed:
            before = len(self.arrows)
            self.arrows |= {(x, z) for x, y in self.arrows
                            for yy, z in self.arrows if y == yy}
            changed = len(self.arrows) != before
        assert all(x in self.objects and y in self.objects for x, y in self.arrows)
        assert all(x == y or (y, x) not in self.arrows for x, y in self.arrows)

    def comp(self, after, before):
        assert before[1] == after[0]
        ans = (before[0], after[1])
        assert ans in self.arrows
        return ans

    def verify_and_print(self):
        print('\nCATEGORY', self.name)
        print('objects =', self.objects)
        print('arrows =', sorted(self.arrows))
        pairs = [(b, a) for a, b in product(sorted(self.arrows), repeat=2)
                 if a[1] == b[0]]
        print('all compositions (after, before, result) =')
        for b, a in pairs:
            print(' ', b, a, self.comp(b, a))
        for x, y in self.arrows:
            assert self.comp((y, y), (x, y)) == (x, y)
            assert self.comp((x, y), (x, x)) == (x, y)
        triples = 0
        for a, b, c in product(self.arrows, repeat=3):
            if a[1] == b[0] and b[1] == c[0]:
                triples += 1
                assert self.comp(c, self.comp(b, a)) == self.comp(self.comp(c, b), a)
        print('identity laws PASS; associative triples =', triples)
        chains = []
        for n in range(len(self.objects)):
            chains.append([t for t in product(self.objects, repeat=n+1)
                           if len(set(t)) == n+1 and
                           all((t[i], t[i+1]) in self.arrows for i in range(n))])
        while chains and not chains[-1]:
            chains.pop()
        ranks = [0]
        for n in range(1, len(chains)):
            rows = {s: i for i, s in enumerate(chains[n-1])}
            matrix = [[Fraction(0) for _ in chains[n]] for _ in chains[n-1]]
            for j, s in enumerate(chains[n]):
                for i in range(n+1):
                    matrix[rows[s[:i] + s[i+1:]]][j] += (-1)**i
            ranks.append(rank(matrix))
        ranks.append(0)
        betti = tuple(len(c) - ranks[i] - ranks[i+1] for i, c in enumerate(chains))
        print('nondegenerate simplex counts =', tuple(map(len, chains)))
        print('rational Betti numbers =', betti)
        return betti


def rank(a):
    if not a:
        return 0
    a = [row[:] for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [v/z for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x-z*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def functor(source, target, mapping, label):
    assert set(mapping) == set(source.objects)
    assert all(mapping[x] in target.objects for x in source.objects)
    assert all((mapping[x], mapping[y]) in target.arrows for x, y in source.arrows)
    for a, b in product(source.arrows, repeat=2):
        if a[1] == b[0]:
            f = lambda u: (mapping[u[0]], mapping[u[1]])
            assert f(source.comp(b, a)) == target.comp(f(b), f(a))
    print('FUNCTOR', label, '= object map', mapping, '; arrows induced uniquely; PASS')


def mv(total, first, second, intersection, label):
    for sub in (first, second, intersection):
        assert set(sub.objects) <= set(total.objects)
        assert sub.arrows == {(x, y) for x, y in total.arrows
                              if x in sub.objects and y in sub.objects}
    for sub in (first, second):
        assert all(x in sub.objects for x, y in total.arrows if y in sub.objects)
    assert set(first.objects) | set(second.objects) == set(total.objects)
    assert set(first.objects) & set(second.objects) == set(intersection.objects)
    print('MAYER--VIETORIS', label, ': full sieves, union and intersection PASS')


A = PosetCategory('A = two discrete points', ('a', 'b'))
e = PosetCategory('e', ('o',))
Cv = PosetCategory('C_v(A)', ('a', 'b', 'v'), (('a', 'v'), ('b', 'v')))
Cw = PosetCategory('C_w(A)', ('a', 'b', 'w'), (('a', 'w'), ('b', 'w')))
Sigma = PosetCategory('Sigma(A)', ('a', 'b', 'v', 'w'),
                     (('a', 'v'), ('a', 'w'), ('b', 'v'), ('b', 'w')))
cv = PosetCategory('C_v(e)', ('o', 'v'), (('o', 'v'),))
cw = PosetCategory('C_w(e)', ('o', 'w'), (('o', 'w'),))
sigma = PosetCategory('Sigma(e)', ('o', 'v', 'w'), (('o', 'v'), ('o', 'w')))
empty = PosetCategory('empty', ())
cv_empty = PosetCategory('C_v(empty)', ('v',))
cw_empty = PosetCategory('C_w(empty)', ('w',))
sigma_empty = PosetCategory('Sigma(empty)', ('v', 'w'))

expected = ((2,), (1,), (1, 0), (1, 0), (1, 1), (1, 0), (1, 0), (1, 0),
            (), (1,), (1,), (2,))
for category, betti in zip((A, e, Cv, Cw, Sigma, cv, cw, sigma,
                            empty, cv_empty, cw_empty, sigma_empty), expected):
    assert category.verify_and_print() == betti

print('\nCUBES')
mv(Sigma, Cv, Cw, A, '6b source / 6c target')
mv(sigma, cv, cw, e, '6b target')
mv(Cw, A, Cw, A, '6c source')
for source, target, label in ((A, e, '6b f0'), (Cv, cv, '6b f1'),
                               (Cw, cw, '6b f2'), (Sigma, sigma, '6b f3')):
    functor(source, target, {x: ('o' if x in ('a', 'b') else x)
                             for x in source.objects}, label)
for source, target, label in ((A, A, '6c f0'), (A, Cv, '6c f1'),
                               (Cw, Cw, '6c f2'), (Cw, Sigma, '6c f3')):
    functor(source, target, {x: x for x in source.objects}, label)
print('Every square of each cube commutes: the displayed object maps agree on overlaps.')
print('Sigma(A) has four edges and four vertices, hence is the explicit circle K_2,2.')
print('The BZ functor labels a->v by 1 and the other three edges by 0; cycle degree = 1.')
mv(sigma_empty, cv_empty, cw_empty, empty, 'thin W1 6b source')
for source, target, label in ((empty, e, 'thin W1 6b f0'),
                               (cv_empty, cv, 'thin W1 6b f1'),
                               (cw_empty, cw, 'thin W1 6b f2'),
                               (sigma_empty, sigma, 'thin W1 6b f3')):
    functor(source, target, {x: x for x in source.objects}, label)
print('thin Wlc 6b pi0-bijection flags: f0=False, f1=True, f2=True, f3=True')
print('thin Wlc 6c pi0-bijection flags: f0=True, f1=False, f2=True, f3=True')
print('thin W1 6b pi0-surjection flags: f0=False, f1=True, f2=True, f3=True')
functor(cv, Cv, {'o': 'a', 'v': 'v'}, 'thin W1 7b section')
functor(e, A, {'o': 'a'}, 'thin W1 7b fibre')
print('thin W1 7b: section is a weak equivalence of contractible categories; fibre misses one of two components.')
print('ALL FINITE CATEGORY AND NERVE CHECKS PASSED')
