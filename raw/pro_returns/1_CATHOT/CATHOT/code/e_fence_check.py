"""Finite index audit for the exact identity-collar homotopy of E.23.

This checks off-by-one/parity formulas.  The proof for all integers is in
sections/E_path.tex; this bounded audit is not substituted for that proof.
"""
from itertools import product


def arrow(i, j):
    return i == j or (i % 2 == 0 and abs(i - j) == 1)


def phi(j, i):
    if i <= -j - 2:
        return i + 2
    if i <= -j:
        return -j
    return i


def psi(j, i):
    if i <= j:
        return i
    if i <= j + 2:
        return j
    return i - 2


vertices = range(-64, 1)
edges = [(i, k) for i in vertices for k in (i - 1, i + 1)
         if k in vertices and arrow(i, k)]
for j in range(31):
    assert phi(j, 0) == 0
    for a, b in edges:
        assert arrow(phi(j, a), phi(j, b)), (j, a, b)
        if phi(j, a) != phi(j, b):
            assert (a > b) == (phi(j, a) > phi(j, b))
    for i in vertices:
        a, b = phi(j, i), phi(j + 1, i)
        if j % 2:
            a, b = b, a
        assert arrow(a, b), (j, i, a, b)
    for a, b in edges:
        # The fence is thin, so the two existing composites coincide.
        p, q = (j, j + 1) if j % 2 == 0 else (j + 1, j)
        assert arrow(phi(p, a), phi(p, b))
        assert arrow(phi(p, b), phi(q, b))
        assert arrow(phi(p, a), phi(q, a))
        assert arrow(phi(q, a), phi(q, b))
        assert arrow(phi(p, a), phi(q, b))
for i in vertices:
    assert phi(0, i) == min(i + 2, 0)
print('Index audit: 31 collar positions, 65 vertices, functors and naturality PASS')

positive_vertices = range(65)
positive_edges = [(i, k) for i in positive_vertices for k in (i - 1, i + 1)
                  if k in positive_vertices and arrow(i, k)]
for j in range(31):
    assert psi(j, 0) == 0
    for a, b in positive_edges:
        assert arrow(psi(j, a), psi(j, b)), (j, a, b)
        if psi(j, a) != psi(j, b):
            assert (a > b) == (psi(j, a) > psi(j, b))
    for i in positive_vertices:
        a, b = psi(j, i), psi(j + 1, i)
        if j % 2:
            a, b = b, a
        assert arrow(a, b), (j, i, a, b)
    for a, b in positive_edges:
        p, q = (j, j + 1) if j % 2 == 0 else (j + 1, j)
        assert arrow(psi(p, a), psi(q, b))
for i in positive_vertices:
    assert psi(0, i) == max(i - 2, 0)
print('Right-collar audit: 31 positions, 65 vertices, functors and naturality PASS')
print('Both reparametrizations preserve every noncollapsed forward/backward direction.')

count = 0
for length in range(0, 9, 2):
    for values in product((0, 1), repeat=length + 1):
        path = dict(zip(range(-length, 1), values))

        def c(i):
            return path[max(i, -length)]

        if any(c(i) > c(k)
               for i in range(-length, 1)
               for k in (i - 1, i + 1)
               if -length <= k <= 0 and arrow(i, k)):
            continue
        count += 1
        for j in range(length + 3):
            assert c(phi(j, 0)) == c(0)
            for i in range(-length - 5, 1):
                a, b = c(phi(j, i)), c(phi(j + 1, i))
                if j % 2:
                    a, b = b, a
                assert a <= b
                if j >= length:
                    assert c(phi(j, i)) == c(i)
print(f'Walking-arrow audit: all {count} half-fence paths of lengths 0,2,4,6,8 PASS')
print('All checked transformations fix both eventual endpoints and become identities.')
