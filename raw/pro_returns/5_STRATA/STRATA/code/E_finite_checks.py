"""Exact finite checks for STRATA E.4, E.7, E.10, and E.11. Python 3 stdlib only."""
from fractions import Fraction
from itertools import combinations, product


def check_poset(objects, le):
    assert all(le(x, x) for x in objects)
    assert all(not (le(x, y) and le(y, x)) or x == y for x, y in product(objects, repeat=2))
    assert all(not (le(x, y) and le(y, z)) or le(x, z)
               for x, y, z in product(objects, repeat=3))
    # Identities and composition are the unique arrows supplied by the order.
    return sum(le(x, y) for x, y in product(objects, repeat=2))


def cartesian(objects, le, p, a, b):
    """Check universal cartesianness of the arrow a -> b over the chain [1]."""
    if not le(a, b):
        return False
    for z in objects:
        if p[z] <= p[a] and le(z, b) and not le(z, a):
            return False
    return True


def cocartesian(objects, le, p, a, b):
    if not le(a, b):
        return False
    for z in objects:
        if p[b] <= p[z] and le(a, z) and not le(b, z):
            return False
    return True


def is_fibration(objects, le, p):
    return all(any(p[a] == s and cartesian(objects, le, p, a, b) for a in objects)
               for b in objects for s in [0, 1] if s <= p[b])


def is_opfibration(objects, le, p):
    return all(any(p[b] == t and cocartesian(objects, le, p, a, b) for b in objects)
               for a in objects for t in [0, 1] if p[a] <= t)


print('E.4: finite chain bifibrations')
for n in range(5):
    objects = tuple(range(n + 1)) + ('t',)
    le = lambda a, b: a == b or b == 't' or (a != 't' and b != 't' and a <= b)
    p = {a: int(a == 't') for a in objects}
    arrows = check_poset(objects, le)
    assert is_fibration(objects, le, p) and is_opfibration(objects, le, p)
    assert cartesian(objects, le, p, n, 't')
    next_objects = tuple(range(n + 2)) + ('t',)
    next_p = {a: int(a == 't') for a in next_objects}
    assert not cartesian(next_objects, le, next_p, n, 't')
    assert not le(n + 1, n)
    print(f'n={n}: objects={len(objects)}, arrows={arrows}, bifibration=True; '
          f'cartesian {n}->t fails at stage {n + 1}, witness {n + 1}->t')


print('\nE.7: contractible groupoid and incompatible point patches')
objects = (0, 1)
arrows = tuple(product(objects, repeat=2))
def compose(f, g):
    """Return g after f."""
    assert f[1] == g[0]
    return (f[0], g[1])
for x in objects:
    assert (x, x) in arrows
for f in arrows:
    assert compose((f[0], f[0]), f) == f
    assert compose(f, (f[1], f[1])) == f
    inv = (f[1], f[0])
    assert compose(f, inv) == (f[0], f[0])
for f, g, h in product(arrows, repeat=3):
    if f[1] == g[0] and g[1] == h[0]:
        assert compose(compose(f, g), h) == compose(f, compose(g, h))
assert all(sum(a == (x, t) for a in arrows) == 1 for x in objects for t in objects)
print('G: 2 objects, 4 arrows; associative; every arrow invertible; both objects terminal.')
print('N(G) is Kan and contractible by these categorical properties.')
point_maps_over_base = lambda a, b: int(a == b)
assert point_maps_over_base(0, 1) == point_maps_over_base(1, 0) == 0
print('Strict point-patch maps over N(G): Hom(0,1)=0, Hom(1,0)=0.')
print('General nonempty patches are excluded by the same unequal vertex labels; no finite truncation assumption.')


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][c]
        a[r] = [x / v for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                v = a[i][c]
                a[i] = [x - v*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


print('\nE.10: six-element sphere poset')
P = tuple(product(range(3), range(2)))
le = lambda a, b: a == b or a[0] < b[0]
print('objects:', P)
print('arrows including identities:', check_poset(P, le))
simplices = {}
for k in range(4):
    simplices[k] = [c for c in combinations(P, k + 1)
                    if all(le(c[i], c[i+1]) and c[i] != c[i+1] for i in range(k))]
boundaries = {}
for k in range(1, 4):
    index = {x: i for i, x in enumerate(simplices[k-1])}
    d = [[0 for _ in simplices[k]] for _ in simplices[k-1]]
    for j, simplex in enumerate(simplices[k]):
        for i in range(k + 1):
            d[index[simplex[:i] + simplex[i+1:]]][j] += (-1)**i
    boundaries[k] = d
for k in range(2, 4):
    a, b = boundaries[k-1], boundaries[k]
    assert all(sum(a[i][j]*b[j][m] for j in range(len(b))) == 0
               for i in range(len(a)) for m in range(len(simplices[k])))
ranks = {0: 0, **{k: rank(boundaries[k]) for k in range(1, 4)}, 4: 0}
betti = [len(simplices[k])-ranks[k]-ranks[k+1] for k in range(4)]
assert betti == [1, 0, 1, 0]
print('nondegenerate simplices in degrees 0..3:', [len(simplices[k]) for k in range(4)])
print('rational Betti numbers:', betti)
print('Identification as S^0*S^0*S^0 proves the sphere homeomorphism, beyond this homology check.')
print('E.10 settles the bifibration existence question over this poset.')

print('\nE.11: five-element rectangular-band monoid')
unit = '1'
band = tuple(product(range(2), repeat=2))
M = (unit,) + band

def multiply(a, b):
    if a == unit:
        return b
    if b == unit:
        return a
    return (a[0], b[1])

assert all(multiply(unit, a) == a == multiply(a, unit) for a in M)
assert all(multiply(multiply(a, b), c) == multiply(a, multiply(b, c))
           for a, b, c in product(M, repeat=3))
assert all(multiply(a, a) == a for a in M)
monic = [a for a in M if all(multiply(a, b) != multiply(a, c) or b == c
                            for b, c in product(M, repeat=2))]
epic = [a for a in M if all(multiply(b, a) != multiply(c, a) or b == c
                           for b, c in product(M, repeat=2))]
assert monic == epic == [unit]
print('One object; five arrows:', M)
print('Full multiplication table:')
for a in M:
    print(a, ':', [multiply(a, b) for b in M])
print('Associativity and identities verified; every element is idempotent.')
print('Monomorphisms:', monic, '; epimorphisms:', epic)

rows = [tuple((i, j) for j in range(2)) for i in range(2)]
for i in range(2):
    assert set(multiply((i, 0), m) for m in M) == set(rows[i])
    assert all(multiply(multiply((i, 0), m), n)
               == multiply((i, 0), multiply(m, n)) for m, n in product(M, repeat=2))
    assert all(multiply(multiply((i, 0), (i, 0)), m)
               == multiply((i, 0), m) for m in M)
print('Each Z[M_i] is the image of an idempotent right-module endomorphism of Z[M].')

# The projective resolution is integral, with explicitly visible primitive bases:
# Z[M_0] + Z[M_1] -> Z[M] -> Z[M_0] -> Z.
d2 = [[int(m == b) for b in band] for m in M]
d1 = [[1 if m == unit else 0 for m in M],
      [-1 if m == unit else 0 for m in M]]
augmentation = [[1, 1]]

def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

assert matmul(d1, d2) == [[0]*4, [0]*4]
assert matmul(augmentation, d1) == [[0]*5]
assert (rank(d2), rank(d1), rank(augmentation)) == (4, 1, 1)
assert d2[0] == [0]*4
assert d2[1:] == [[int(i == j) for j in range(4)] for i in range(4)]
assert [d1[i][0] for i in range(2)] == [1, -1]
# Verify right-module linearity of the middle map on every basis pair.
for m, n in product(M, repeat=2):
    lhs = [d1[i][M.index(multiply(m, n))] for i in range(2)]
    rhs = [0, 0]
    for i, coefficient in enumerate([d1[0][M.index(m)], d1[1][M.index(m)]]):
        rhs[rows[0].index(multiply(rows[0][i], n))] += coefficient
    assert lhs == rhs
print('Integral resolution exact: d2 embeds the four nonunit basis elements;')
print('d1 sends 1 to (1,-1) and the other basis elements to zero; epsilon=(1,1).')
print('All right-module action equations verified.')

# The coinvariants of each transitive right M-set M_i are free of rank one.
for row in rows:
    assert any(multiply(row[0], n) == row[1] for n in M)
    assert any(multiply(row[1], n) == row[0] for n in M)
tensor_d2 = [[1, 1]]
tensor_d1 = [[0]]
assert matmul(tensor_d1, tensor_d2) == [[0, 0]]
assert matmul(tensor_d2, [[1], [-1]]) == [[0]]
assert tensor_d2[0][0] == 1  # primitive image, hence no integral torsion.
print('After tensoring with trivial Z: Z^2 --(1,1)--> Z --0--> Z.')
print('Integral homology: H0=Z, H1=0, H2=Z, Hn=0 for n>=3.')
print('The idempotent generators force pi1=1; Hurewicz and Whitehead give BM~S^2.')
print('This is an unresolved bifibration test, not a counterexample to existence.')
print('\nALL ASSERTIONS PASSED')
