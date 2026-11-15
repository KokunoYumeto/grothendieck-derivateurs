"""Exact checks for the binary icosahedral group 2I (POINCARE_SPINE_CHECK.md).

All arithmetic is exact, in Q(sqrt5) (pairs of Fractions). Steps:
  1. Build the 120 icosians (unit quaternions over Q(sqrt5)); check closure.
  2. Find q_a, q_b with q_a^5 = q_b^3 = (q_a q_b)^2 = -1 that generate the group;
     coset enumeration (sympy) gives |<a,b | a^5 b^-3, b^3 (ab)^-2>| = 120,
     so pi_1(P) is isomorphic to the icosian group.
  3. Conjugacy classes, element orders.
  4. Nine characters: chi_{Sym^k V}(g) = U_k(Re g) (Chebyshev, 2nd kind),
     their Galois conjugates, and V (x) V'. Exact Gram matrix = identity and
     9 classes => complete character table.
  5. Frobenius-Schur indicators nu(chi) = (1/|G|) sum_g chi(g^2).
  6. m_H = #{chi : chi(1) = 2, nu(chi) = -1}; cross-check by two surjections
     R[G] -> H with different real parts (no use of the FS theorem).
"""
from fractions import Fraction as Fr
from itertools import permutations, product


class Q5:
    """a + b*sqrt(5), a and b rational."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        o = q5(o)
        return Q5(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, o):
        o = q5(o)
        return Q5(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return q5(o) - self

    def __mul__(self, o):
        o = q5(o)
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def __truediv__(self, o):
        o = q5(o)
        n = o.a * o.a - 5 * o.b * o.b
        r = self * Q5(o.a, -o.b)
        return Q5(r.a / n, r.b / n)

    def __eq__(self, o):
        o = q5(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def sigma(self):
        return Q5(self.a, -self.b)

    def __float__(self):
        return float(self.a) + float(self.b) * 5 ** 0.5

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        return f"({self.a}{'+' if self.b > 0 else '-'}{abs(self.b)}r5)"


def q5(x):
    return x if isinstance(x, Q5) else Q5(x)


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def qconj(p):
    return (p[0], -p[1], -p[2], -p[3])


def qsigma(p):
    return tuple(x.sigma() for x in p)


def qnorm(p):
    return p[0] * p[0] + p[1] * p[1] + p[2] * p[2] + p[3] * p[3]


ONE = (Q5(1), Q5(0), Q5(0), Q5(0))
MINUS_ONE = (Q5(-1), Q5(0), Q5(0), Q5(0))
half = Fr(1, 2)
phi = Q5(half, half)           # (1+sqrt5)/2
phi_inv = Q5(-half, half)      # (-1+sqrt5)/2 = phi - 1


def is_even(perm):
    p, s = list(perm), 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s == 1


def icosians(even=True):
    els = set()
    for i in range(4):                      # +-1, +-i, +-j, +-k
        for s in (1, -1):
            v = [Q5(0)] * 4
            v[i] = Q5(s)
            els.add(tuple(v))
    for signs in product((1, -1), repeat=4):  # (+-1 +-i +-j +-k)/2
        els.add(tuple(Q5(Fr(s, 2)) for s in signs))
    base = [Q5(0), Q5(half), phi_inv * half, phi * half]
    for perm in permutations(range(4)):
        if is_even(perm) != even:
            continue
        for signs in product((1, -1), repeat=3):
            vals = [base[0], signs[0] * base[1], signs[1] * base[2], signs[2] * base[3]]
            els.add(tuple(vals[perm[t]] for t in range(4)))
    return els


def closure(gens):
    elems = {ONE}
    frontier = [ONE]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = qmul(x, g)
                if y not in elems:
                    elems.add(y)
                    new.append(y)
        frontier = new
    return elems


def order(g):
    n, x = 1, g
    while x != ONE:
        x = qmul(x, g)
        n += 1
    return n


def qpow(g, n):
    x = ONE
    for _ in range(n):
        x = qmul(x, g)
    return x


def U(k, c):
    """Chebyshev polynomial of the second kind: U_k(cos t) = sin((k+1)t)/sin t."""
    u0, u1 = Q5(1), 2 * c
    if k == 0:
        return u0
    for _ in range(k - 1):
        u0, u1 = u1, 2 * c * u1 - u0
    return u1


def main():
    # 1. the group
    for parity in (True, False):
        G = icosians(parity)
        ok = len(G) == 120 and all(qnorm(g) == 1 for g in G) and \
            all(qmul(g, h) in G for g in G for h in G)
        print(f"icosians with {'even' if parity else 'odd'} permutations: "
              f"{len(G)} elements, unit norm and closed under product: {ok}")
        if ok:
            break
    assert ok
    G = sorted(G, key=lambda q: tuple((x.a, x.b) for x in q))

    # 2. generators satisfying the relations, and the presented group's order
    qb = (Q5(half), Q5(half), Q5(half), Q5(half))
    cands = [g for g in G if g[0] == phi * half and qmul(g, qb)[0] == 0]
    qa = cands[0]
    print("q_a =", qa, " q_b =", qb)
    print("q_a^5 = -1:", qpow(qa, 5) == MINUS_ONE, "| q_b^3 = -1:", qpow(qb, 3) == MINUS_ONE,
          "| (q_a q_b)^2 = -1:", qpow(qmul(qa, qb), 2) == MINUS_ONE)
    print("<q_a, q_b> has order", len(closure([qa, qb])))
    from sympy.combinatorics.free_groups import free_group
    from sympy.combinatorics.fp_groups import FpGroup
    F, a, b = free_group("a b")
    Pgrp = FpGroup(F, [a**5 * b**-3, b**3 * (a * b)**-2])
    print("order of <a,b | a^5 b^-3, b^3 (ab)^-2> by coset enumeration:", Pgrp.order())

    # 3. conjugacy classes and element orders
    classes, seen = [], set()
    for g in G:
        if g in seen:
            continue
        cl = {qmul(qmul(h, g), qconj(h)) for h in G}
        seen |= cl
        classes.append(sorted(cl, key=lambda q: tuple((x.a, x.b) for x in q)))
    classes.sort(key=lambda c: (order(c[0]), -float(c[0][0])))
    print("number of conjugacy classes:", len(classes))
    from collections import Counter
    print("element orders:", dict(sorted(Counter(order(g) for g in G).items())))
    print("elements of order 2:", [g for g in G if order(g) == 2])

    # 4. characters
    names = ["1", "2", "3", "4", "5", "6", "2'", "3'", "4'"]

    def chi(name, g):
        c = g[0]
        if name == "2'":
            return U(1, c.sigma())
        if name == "3'":
            return U(2, c.sigma())
        if name == "4'":
            return U(1, c) * U(1, c.sigma())
        return U(int(name) - 1, c)

    print("\nclass | size | order | Re(g) (exact) | character values (float)")
    for c in classes:
        g = c[0]
        vals = " ".join(f"{float(chi(n, g)):7.3f}" for n in names)
        print(f"  size {len(c):3d}  ord {order(g):2d}  Re {g[0]!r:>12}  {vals}")
    print("  columns:", names)

    def inner(n1, n2):
        s = Q5(0)
        for g in G:
            s = s + chi(n1, g) * chi(n2, qconj(g))
        return s / 120

    gram_ok = all(inner(n1, n2) == (1 if n1 == n2 else 0) for n1 in names for n2 in names)
    print("\nGram matrix of the nine characters is the identity (exact):", gram_ok)
    degs = {n: chi(n, ONE) for n in names}
    print("degrees:", {n: str(d) for n, d in degs.items()},
          " sum of squares:", sum((d * d for d in degs.values()), Q5(0)))

    # 5. Frobenius-Schur indicators
    fs = {}
    for n in names:
        s = Q5(0)
        for g in G:
            s = s + chi(n, qmul(g, g))
        fs[n] = s / 120
    print("Frobenius-Schur indicators:", {n: str(v) for n, v in fs.items()})
    faithful = {n: chi(n, MINUS_ONE) == -degs[n] for n in names}
    print("-1 acts as -1 (faithful on the centre):", faithful)

    # 6. m_H and the Wedderburn decomposition of R[G]
    mH = [n for n in names if fs[n] == -1 and degs[n] == 2]
    print("\nquaternionic (nu = -1):", [n for n in names if fs[n] == -1])
    print("real (nu = +1):", [n for n in names if fs[n] == 1])
    print("complex (nu = 0):", [n for n in names if fs[n] == 0])
    print("m_H(2I) = #{chi : chi(1) = 2, nu = -1} =", len(mH), mH)
    parts = []
    for n in names:
        d = int(degs[n].a)
        parts.append(f"M_{d}(R)" if fs[n] == 1 else (f"M_{d // 2}(H)" if fs[n] == -1 else f"M_{d}(C)"))
    print("R[2I] =", " x ".join(parts))

    # cross-check without the FS theorem: iota and sigma.iota are injective homomorphisms
    # G -> unit quaternions; both images contain 1,i,j,k, so both give R-algebra surjections
    # R[G] -> H; their real parts differ at q_a, so they factor through different simple factors.
    sG = {qsigma(g) for g in G}
    print("\nsigma(G): 120 elements:", len(sG) == 120, "| unit norm:", all(qnorm(g) == 1 for g in sG),
          "| closed:", all(qmul(g, h) in sG for g in sG for h in sG))
    basis = [ONE, (Q5(0), Q5(1), Q5(0), Q5(0)), (Q5(0), Q5(0), Q5(1), Q5(0)), (Q5(0), Q5(0), Q5(0), Q5(1))]
    print("1, i, j, k lie in G and in sigma(G):", all(x in G and x in sG for x in basis))
    print("Re(q_a) =", qa[0], " Re(sigma(q_a)) =", qa[0].sigma(), " differ:", qa[0] != qa[0].sigma())
    n_deg2 = sum(1 for n in names if degs[n] == 2)
    print("number of irreducible characters of degree 2 (upper bound for m_H):", n_deg2)


if __name__ == "__main__":
    main()
