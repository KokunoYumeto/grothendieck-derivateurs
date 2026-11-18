"""Exact certificates for C4:three-arrow-high-degree, r=2,...,5.

Checks the actual generator-path anchors, oriented cube boundary,
invariant affine-volume cocycle, and nonzero pairing. No floating point.
"""
from collections import Counter
from functools import cmp_to_key
from itertools import permutations, product
from math import factorial


def lamp(d):
    return tuple(sorted((i, v) for i, v in d.items() if v))


def add(f, g):
    d = Counter(dict(f))
    for i, v in g:
        d[i] += v
    return lamp(d)


def neg(f):
    return tuple((i, -v) for i, v in f)


def shift(f, n):
    return tuple((i+n, v) for i, v in f)


def mul(g, h):
    f, m = g
    k, n = h
    return add(f, shift(k, m)), m+n


def inv(g):
    f, m = g
    return shift(neg(f), -m), -m


def order_cmp(g, h):
    f, m = mul(inv(g), h)
    if m:
        return -1 if m > 0 else 1
    if f:
        return -1 if f[-1][1] > 0 else 1
    return 0


def det(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*p-a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator//prev
        for i in range(k+1, n):
            a[i][k] = 0
        prev = p
    return sign*a[-1][-1]


def omega(vectors):
    r = len(vectors)
    ds = [dict(v) for v in vectors]
    support = [i for d in ds for i in d]
    if not support:
        return 0
    return sum(det([[d.get(j+i, 0) for d in ds] for i in range(r)])
               for j in range(min(support)-r+1, max(support)+1))


def cocycle(simplex):
    f0 = simplex[0][0]
    return omega([add(g[0], neg(f0)) for g in simplex[1:]])


def parity(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i+1, len(p)))


def triangulate(indices, base):
    out = Counter()
    for p in permutations(indices):
        vertices = [base]
        for i in p:
            vertices.append(mul((((i, 1),), 0), vertices[-1]))
        out[tuple(vertices)] += parity([indices.index(i) for i in p])
    return out


def boundary(chain):
    out = Counter()
    for simplex, coeff in chain.items():
        for i in range(len(simplex)):
            out[simplex[:i]+simplex[i+1:]] += (-1)**i*coeff
    return Counter({s: c for s, c in out.items() if c})


def translate_chain(chain, g):
    return Counter({tuple(mul(g, v) for v in s): c
                    for s, c in chain.items()})


def run(r):
    zero, a, t = ((), 0), (((0, 1),), 0), ((), 1)
    ti = inv(t)
    cube = {(lamp({i: bit for i, bit in enumerate(bits)}), 0)
            for bits in product((0, 1), repeat=r)}
    p0, paths = set(cube), []
    for i in range(r):
        lower = {v for v in cube if dict(v[0]).get(i, 0) == 0}
        current, records = lower, []
        for step in [ti]*i+[a]+[t]*i:
            nxt = {mul(step, g) for g in current}
            p0.update(current)
            p0.update(nxt)
            records.append((step, current, nxt))
            current = nxt
        assert current == {mul((((i, 1),), 0), g) for g in lower}
        paths.append(records)
    q = p0 | {mul(a, g) for g in p0} | {mul(t, g) for g in p0}
    p = {g for g in q if mul(a, g) in q and mul(t, g) in q}
    assert p0 <= p <= q and p
    ps = sorted(p, key=cmp_to_key(order_cmp))
    for generator in (a, t):
        image = [mul(generator, g) for g in ps]
        assert all(order_cmp(image[i], image[i+1]) < 0
                   for i in range(len(image)-1))
    for records in paths:
        for step, current, nxt in records:
            if step == ti:
                assert nxt <= p
                assert {mul(t, g) for g in nxt} == current
            else:
                assert current <= p
                assert {mul(step, g) for g in current} == nxt

    z, expected_boundary, face_checks = triangulate(list(range(r)), zero), Counter(), 0
    for i in range(r):
        lower = triangulate([j for j in range(r) if j != i], zero)
        upper = translate_chain(lower, (((i, 1),), 0))
        for s, c in upper.items():
            expected_boundary[s] += (-1)**i*c
        for s, c in lower.items():
            expected_boundary[s] -= (-1)**i*c
        chain = lower
        for step, current, nxt in paths[i]:
            assert all(set(s) <= current for s in chain)
            chain = translate_chain(chain, step)
            assert all(set(s) <= nxt for s in chain)
            face_checks += len(chain)
        assert chain == upper
    expected_boundary = Counter({s: c for s, c in expected_boundary.items() if c})
    assert boundary(z) == expected_boundary
    value = sum(k*cocycle(s) for s, k in z.items())
    assert value == factorial(r)
    dc_checks = 0
    for s in z:
        assert all(order_cmp(s[i], s[i+1]) < 0 for i in range(r))
        for v in cube:
            extended = (v,)+s
            assert sum((-1)**i*cocycle(extended[:i]+extended[i+1:])
                       for i in range(r+2)) == 0
            dc_checks += 1
        for generator in (a, t, ti):
            assert cocycle(tuple(mul(generator, v) for v in s)) == cocycle(s)
    print(f"r={r}: |P0|={len(p0)}, |P|={len(p)}, |Q|={len(q)}, "
          f"cube_simplices={len(z)}, path_face_checks={face_checks}, "
          f"coboundary_checks={dc_checks}, pairing={value}; PASS")


if __name__ == "__main__":
    for r in range(2, 6):
        run(r)
    print("All exact certificates passed; no modular uniformity or ultraproduct totality claimed.")
