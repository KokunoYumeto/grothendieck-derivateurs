"""Exact finite-category check used in GALOIS F.6.

The category is the poset of nonempty proper subsets of {0,1,2,3}.
There is one arrow S -> T iff S is a subset of T; composition is inclusion.
The program checks the category axioms, constructs its normalized nerve
through dimension three, and computes exact integral boundary invariants.
"""
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

objects = tuple(range(1, 15))
leq = lambda s, t: (s & t) == s
arrows = tuple((s, t) for s in objects for t in objects if leq(s, t))
compose = lambda g, f: (f[0], g[1])
assert all((s, s) in arrows for s in objects)
for f in arrows:
    assert compose((f[1], f[1]), f) == f
    assert compose(f, (f[0], f[0])) == f
for f in arrows:
    for g in arrows:
        if f[1] != g[0]:
            continue
        assert compose(g, f) in arrows
        for h in arrows:
            if g[1] == h[0]:
                assert compose(h, compose(g, f)) == compose(compose(h, g), f)

cells = {n: [] for n in range(4)}
for n in range(4):
    for chain in combinations(objects, n + 1):
        if all(leq(chain[i], chain[i+1]) for i in range(n)):
            cells[n].append(chain)

def boundary(n):
    index = {c:i for i,c in enumerate(cells[n-1])}
    d = Matrix.zeros(len(cells[n-1]), len(cells[n]))
    for j, c in enumerate(cells[n]):
        for k in range(n+1):
            d[index[c[:k] + c[k+1:]], j] += (-1)**k
    return d

d1, d2, d3 = (boundary(n) for n in (1, 2, 3))
assert d1*d2 == Matrix.zeros(len(cells[0]), len(cells[2]))
assert d2*d3 == Matrix.zeros(len(cells[1]), len(cells[3]))
s1, s2 = smith_normal_form(d1, domain=ZZ), smith_normal_form(d2, domain=ZZ)
i1 = [abs(s1[i,i]) for i in range(min(s1.shape)) if s1[i,i]]
i2 = [abs(s2[i,i]) for i in range(min(s2.shape)) if s2[i,i]]
assert i1 == [1]*13
assert i2 == [1]*23
assert [len(cells[n]) for n in range(4)] == [14,36,24,0]
assert len(cells[1])-len(i1)-len(i2) == 0
print('Objects: nonempty proper subsets of a four-element set (bitmasks 1..14).')
print(f'Arrows, including identities: {len(arrows)}; all composition and identity axioms verified.')
print('Nondegenerate nerve simplex counts in dimensions 0,1,2,3:', [len(cells[n]) for n in range(4)])
print('Boundary compositions d1*d2 and d2*d3: zero.')
print('Smith nonzero invariants d1:', i1)
print('Smith nonzero invariants d2:', i2)
print('Integral homology: H0=Z, H1=0, H2=Z, Hn=0 for n>2.')
print('Explanation: im(d2) is primitive in C1 since every nonzero Smith invariant is 1; rank(ker d1)=rank(im d2)=23.')
print('Euler characteristic:', sum((-1)**n*len(cells[n]) for n in range(4)))
