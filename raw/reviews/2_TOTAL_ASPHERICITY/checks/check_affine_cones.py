"""TOTASPH C.8-C.10: augmentation-one integral combinations t of injections [n] -> [M] with t.h independent of
the injection h: [m] -> [n], for n = 1, 2, 3. Own implementation of the construction (Claude, Fable 5.2), and a
direct check on the injections themselves; the answer's code was neither run nor imported.

Polynomials are dicts {exponent tuple: integer coefficient}.
"""
import itertools
from collections import defaultdict


def padd(p, q, s=1):
    r = defaultdict(int, p)
    for e, c in q.items():
        r[e] += s * c
    return {e: c for e, c in r.items() if c}


def pmul(p, q):
    r = defaultdict(int)
    for e, c in p.items():
        for f, d in q.items():
            r[tuple(a + b for a, b in zip(e, f))] += c * d
    return {e: c for e, c in r.items() if c}


def ppow(p, k, nv):
    r = {tuple([0] * nv): 1}
    for _ in range(k):
        r = pmul(r, p)
    return r


def substitute(p, subs, nv):
    """p(subs[0], .., subs[nv-1]) for polynomials subs[i] in nv variables."""
    cache = {}
    r = {}
    for e, c in p.items():
        term = {tuple([0] * nv): c}
        for i, a in enumerate(e):
            if a:
                if (i, a) not in cache:
                    cache[(i, a)] = ppow(subs[i], a, nv)
                term = pmul(term, cache[(i, a)])
        r = padd(r, term)
    return r


def merge(p, i):
    """D_i: identify variables i and i+1 (exponents add) and renumber."""
    r = defaultdict(int)
    for e, c in p.items():
        r[e[:i] + (e[i] + e[i + 1],) + e[i + 2:]] += c
    return {e: c for e, c in r.items() if c}


def cone_poly(n, k):
    """C_{n,k}: homogeneous polynomial in z_0..z_{n+1}, value 1 at (1,..,1), with y_i^k D_i(C) independent of i."""
    if n == 0:
        return {(0, 0): 1}
    Q = cone_poly(n - 1, 2 * k)                 # in y_0..y_n
    nv = n + 2
    lifts = []
    for i in range(n + 1):
        mono = {tuple(0 if l == i else k for l in range(n + 1)): 1}
        Fi = pmul(Q, mono)                      # in y_0..y_n
        # lift to z_0..z_{n+1}: y_l = z_l for l <= i, y_l = z_{l+1} for l > i (z_{i+1} does not occur)
        lift = {}
        for e, c in Fi.items():
            lift[e[:i + 1] + (0,) + e[i + 1:]] = c
        lifts.append(lift)

    # The substitutions rho_S of Lemma C.8 set x_i = 0 (i in S) in the coordinates x_i = z_i - z_{i+1},
    # u = z_{n+1}; they commute with one another (a retraction "replace z_i by z_{i+1}" would not).
    def one(j):
        return {tuple(1 if l == j else 0 for l in range(nv)): 1}
    # z_j = u + sum_{i >= j} x_i, written in the variables (x_0, .., x_n, u)
    z_in_x = [dict() for _ in range(nv)]
    for j in range(nv):
        q = one(nv - 1)
        for i in range(j, n + 1):
            q = padd(q, one(i))
        z_in_x[j] = q
    # x_i = z_i - z_{i+1}, u = z_{n+1}, written in the variables z
    x_in_z = [padd(one(i), one(i + 1), -1) for i in range(n + 1)] + [one(nv - 1)]
    lifts = [substitute(l, z_in_x, nv) for l in lifts]

    def rho(p, S):
        return {e: c for e, c in p.items() if all(e[i] == 0 for i in S)}

    C = {}
    idx = list(range(n + 1))
    for size in range(1, n + 2):
        for S in itertools.combinations(idx, size):
            vals = [rho(lifts[i], S) for i in S]
            assert all(v == vals[0] for v in vals), 'prescriptions disagree on an intersection'
            C = padd(C, vals[0], (-1) ** (size + 1))
    C = substitute(C, x_in_z, nv)
    assert len(C) and all(len(e) == nv for e in C)
    return C


def injection_from_gaps(e):
    """Gaps (e_0, .., e_{n+1}) -> strictly increasing g: [n] -> [M], M = n + sum(e)."""
    g = []
    pos = e[0]
    g.append(pos)
    for i in range(1, len(e) - 1):
        pos += e[i] + 1
        g.append(pos)
    return tuple(g), g[-1] + e[-1]


for n in (1, 2, 3):
    P = cone_poly(n, 1)
    degs = {sum(e) for e in P}
    assert len(degs) == 1
    d = degs.pop()
    M = n + d
    assert M == 2 ** (n + 1) - 2
    t = {}
    for e, c in P.items():
        g, top = injection_from_gaps(e)
        assert top == M and len(g) == n + 1 and all(g[i] < g[i + 1] for i in range(n)) and g[0] >= 0
        t[g] = c
    aug = sum(t.values())
    assert aug == 1

    def compose(t, h):
        r = defaultdict(int)
        for g, c in t.items():
            r[tuple(g[x] for x in h)] += c
        return {g: c for g, c in r.items() if c}

    # all strictly increasing h: [m] -> [n], every m <= n: t.h depends only on m
    nvals = 0
    for m in range(0, n + 1):
        vals = [compose(t, h) for h in itertools.combinations(range(n + 1), m + 1)]
        assert all(v == vals[0] for v in vals), (n, m)
        nvals += len(vals)
        if m < n:
            assert sum(vals[0].values()) == 1
    print(f'n={n}: M={M}, {len(t)} injections with non-zero coefficient (of {sum(1 for _ in itertools.combinations(range(M+1), n+1))}), '
          f'augmentation {aug}, max |coefficient| {max(abs(c) for c in t.values())}; '
          f't.h independent of h for all {nvals} injections h into [{n}]: True')
    if n == 1:
        print('   t =', ' '.join(f'{c:+d}*{g}' for g, c in sorted(t.items())))

# not filtered: the two maps [0] -> [1] are never equalized by an injection
print('no injection c: [1] -> [N] has c(0) = c(1): not filtered (immediate)')
# not sifted: comparison of the two marked points is invariant
print('ALL ASSERTIONS PASSED')
