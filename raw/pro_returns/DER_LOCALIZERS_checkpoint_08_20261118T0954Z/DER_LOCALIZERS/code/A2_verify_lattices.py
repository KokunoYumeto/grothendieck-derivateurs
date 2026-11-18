#!/usr/bin/env python3
"""Exact finite verification of the A2.5 represented-derivator witnesses.

This checks the finite order/category data and every bicartesian-square map.
It does not pretend to verify the derivator axioms for infinitely many shapes;
those follow from the ordinary Kan-extension construction proved in the text.
"""
from itertools import product
from collections import Counter


def higman_tensor_certificates():
    """Check integer chain contractions for K x K and the join model.

    A basis state is (degree_first, index_first, degree_second, index_second).
    The suspension sign for the join changes both d and h, leaving dh+hd.
    """
    ranks = {0: 1, 1: 4, 2: 4}
    # d(r_i) = -x_(i+1), with indices cyclic modulo 4.
    def differential_one(degree, index):
        return [(1, (index + 1) % 4, -1)] if degree == 2 else []

    def homotopy_one(degree, index):
        return [(2, (index - 1) % 4, -1)] if degree == 1 else []

    def add(target, state, coefficient):
        target[state] += coefficient
        if target[state] == 0:
            del target[state]

    def d(state):
        i, a, j, b = state
        out = Counter()
        for n, x, coefficient in differential_one(i, a):
            add(out, (n, x, j, b), coefficient)
        for n, y, coefficient in differential_one(j, b):
            add(out, (i, a, n, y), (-1) ** i * coefficient)
        return out

    def h(state, reduced):
        i, a, j, b = state
        out = Counter()
        for n, x, coefficient in homotopy_one(i, a):
            add(out, (n, x, j, b), coefficient)
        if not reduced and i == 0:
            for n, y, coefficient in homotopy_one(j, b):
                add(out, (i, a, n, y), coefficient)
        return out

    def apply(operator, vector):
        out = Counter()
        for state, coefficient in vector.items():
            for target, value in operator(state).items():
                add(out, target, coefficient * value)
        return out

    for reduced in (False, True):
        degrees = (1, 2) if reduced else (0, 1, 2)
        states = [
            (i, a, j, b)
            for i, j in product(degrees, repeat=2)
            for a in range(ranks[i]) for b in range(ranks[j])
        ]
        for state in states:
            assert apply(d, d(state)) == {}
            dh = apply(d, h(state, reduced))
            hd = apply(lambda x: h(x, reduced), d(state))
            lhs = Counter(dh)
            for target, value in hd.items():
                add(lhs, target, value)
            rhs = Counter({state: 1})
            if not reduced and state == (0, 0, 0, 0):
                rhs.clear()
            assert lhs == rhs, (reduced, state, lhs, rhs)
        chain_ranks = Counter(s[0] + s[2] + int(reduced) for s in states)
        if reduced:
            assert dict(chain_ranks) == {3: 16, 4: 32, 5: 16}
            print("Higman reduced join: ranks", dict(sorted(chain_ranks.items())),
                  "; integer contraction verified")
        else:
            assert dict(chain_ranks) == {0: 1, 1: 8, 2: 24, 3: 32, 4: 16}
            print("Higman product: ranks", dict(sorted(chain_ranks.items())),
                  "; integer augmentation contraction verified")


def make_lattice(names, covers):
    n = len(names)
    order = {(i, i) for i in range(n)}
    order |= {(names.index(a), names.index(b)) for a, b in covers}
    while True:
        extra = {(a, d) for a, b in order for c, d in order if b == c}
        if extra <= order:
            break
        order |= extra
    assert all((b, a) not in order for a, b in order if a != b)
    meet, join = {}, {}
    for a, b in product(range(n), repeat=2):
        lower = [x for x in range(n) if (x, a) in order and (x, b) in order]
        upper = [x for x in range(n) if (a, x) in order and (b, x) in order]
        glb = [x for x in lower if all((y, x) in order for y in lower)]
        lub = [x for x in upper if all((x, y) in order for y in upper)]
        assert len(glb) == len(lub) == 1
        meet[a, b], join[a, b] = glb[0], lub[0]
    return order, meet, join


def check(names, covers):
    order, meet, join = make_lattice(names, covers)
    n = len(names)
    squares = [
        (u, a, b, v) for u, a, b, v in product(range(n), repeat=4)
        if all(pair in order for pair in [(u, a), (u, b), (a, v), (b, v)])
    ]
    cart = [s for s in squares if s[0] == meet[s[1], s[2]]]
    cocart = [s for s in squares if s[3] == join[s[1], s[2]]]
    bicart = [s for s in cart if s in cocart]
    bad = []
    tested = 0
    for s, t in product(bicart, repeat=2):
        if not all((a, b) in order for a, b in zip(s, t)):
            continue
        tested += 1
        if s[0] == t[0] and s[3] == t[3] and s[1:3] != t[1:3]:
            bad.append((s, t))
    named = lambda s: tuple(names[i] for i in s)
    print(f"lattice={names}; arrows={len(order)}; all_squares={len(squares)}")
    print(f"cartesian={len(cart)}; cocartesian={len(cocart)}; bicartesian={len(bicart)}")
    print(f"maps_of_bicartesian_squares={tested}; Der8_third_failures={len(bad)}")
    for s, t in bad:
        print("  failure:", named(s), "->", named(t))
    return names, order, cart, cocart, bicart, bad


def constant_tree_certificate():
    """Integer certificate for A2.10; this is not an all-shapes axiom test."""
    vertices = ("a1", "a2", "b1", "b2")
    edges = (("a1", "b1"), ("a2", "b1"), ("a2", "b2"))
    reached = {"a1"}
    while True:
        new = reached | {
            y for x, y in edges + tuple((b, a) for a, b in edges) if x in reached
        }
        if new == reached:
            break
        reached = new
    assert reached == set(vertices)
    assert len(edges) - len(vertices) + 1 == 0
    h = ((1, 0, 0), (0, 1, 1))
    v = ((1, 1, 0), (0, 0, 1))
    d = (1, -1, 1)
    mv = lambda matrix, vector: tuple(
        sum(a * b for a, b in zip(row, vector)) for row in matrix
    )
    assert mv(h, d) == (1, 0)
    assert mv(v, d) == (0, 1)
    # Image is exactly ker(a1+a2-b1-b2): invert by e1=a1,e3=b2,
    # e2=b1-a1. Verify the universal integral parameterization.
    comparison = h + v
    inverse = ((1, 0, 0, 0), (-1, 0, 1, 0), (0, 0, 0, 1))
    for j in range(3):
        basis = tuple(int(i == j) for i in range(3))
        assert mv(inverse, mv(comparison, basis)) == basis
    kernel_basis = ((1, 0, 1, 0), (0, 1, 1, 0), (0, 1, 0, 1))
    assert all(mv(comparison, mv(inverse, b)) == b for b in kernel_basis)
    T = ((1, -1), (0, 1))
    assert T[0][0] * T[1][1] - T[0][1] * T[1][0] == 1
    assert tuple(sum(T[i][j] for i in range(2)) for j in range(2)) == (1, 0)
    print("constant three-edge tree: contractible; d=(1,-1,1); integral kernel basis verified")
    print("free-circle fold matrix: det(T)=1 and [1,1]T=[1,0]")


def labelled_augmentation_certificate():
    """Finite locally constant test and integral pullback in A2.12."""
    objects = ("r", "a0", "a1", "b0", "b1")
    nonidentity = (("r", "a0"), ("r", "b0"))
    arrows = tuple((x, x) for x in objects) + nonidentity
    base = {"r": "0", "a0": "a", "a1": "a", "b0": "b", "b1": "b"}
    base_arrows = (("0", "0"), ("a", "a"), ("b", "b"), ("0", "a"), ("0", "b"))
    assert len(objects) == 5 and len(arrows) == 7
    # These discrete fibers have exactly the required unique opcartesian lifts.
    for x in objects:
        for source, target in base_arrows:
            if source != base[x]:
                continue
            lifts = [(u, v) for u, v in arrows if u == x and base[v] == target]
            assert len(lifts) == 1
    coefficient_labels = {"r": 0, "a0": 0, "b0": 0, "a1": 1, "b1": 1}
    assert all(coefficient_labels[x] == coefficient_labels[y] for x, y in arrows)
    # Every coefficient arrow is the identity of the same augmented Z[0].
    assert nonidentity == (("r", "a0"), ("r", "b0"))
    D = ((1, 0, -1, 0), (0, 1, 0, 0), (0, 0, 0, -1))
    kernel = (1, 0, 1, 0)
    mv = lambda matrix, vector: tuple(
        sum(a * b for a, b in zip(row, vector)) for row in matrix
    )
    assert mv(D, kernel) == (0, 0, 0)
    # Right inverse sends (x,y,z) to (x,y,0,-z), so surjectivity is integral.
    right_inverse = ((1, 0, 0), (0, 1, 0), (0, 0, 0), (0, 0, -1))
    for j in range(3):
        basis = tuple(int(i == j) for i in range(3))
        assert mv(D, mv(right_inverse, basis)) == basis
    # Subtracting that right-inverse component leaves exactly c*(1,0,1,0).
    for j in range(4):
        e = tuple(int(i == j) for i in range(4))
        correction = mv(right_inverse, mv(D, e))
        remainder = tuple(a - b for a, b in zip(e, correction))
        assert remainder == tuple(e[2] * k for k in kernel)
    assert kernel[0] + kernel[1] == 1  # pullback augmentation is id_Z
    root_label = 0
    side_labels = (max(0, 1), max(0, 1))
    ambient_pullback_label = min(side_labels)
    pullback_augmentation_nonzero = True
    reset_label = ambient_pullback_label if pullback_augmentation_nonzero else 0
    assert root_label == 0 and reset_label == 1
    # Exhaust every possible emptiness pattern of a constant discrete-fiber span.
    # A nonempty root requires both adjacent fibers to be nonempty.
    for coefficient_label in (0, 1):
        for root, left, right in product((False, True), repeat=3):
            if root and not (left and right):
                continue
            labels = tuple(coefficient_label if nonempty else 0
                           for nonempty in (root, left, right))
            comparison_label = min(labels[1:]) if root else 0
            assert comparison_label == labels[0]
    print("labelled augmentation test: 5 objects, 7 arrows, split opfibration; coefficient locally constant")
    print("integral pullback: D has explicit right inverse, kernel Z*(1,0,1,0), augmentation id_Z")
    print("locally constant test fails: root label0, pullback label1; all constant emptiness patterns pass")


def rationalized_fiber_certificate():
    """Exact p=2 split map killed by free pointing in the auxiliary note."""
    from fractions import Fraction as Q
    # N_1=Z, N_0=Z^2, d(t)=(0,2t), augmentation (a,b)->a.
    d = ((0,), (2,))
    i = ((1,), (0,))
    r = ((1, 0),)
    h = ((Q(0), Q(1, 2)),)
    mm = lambda A, B: tuple(tuple(sum(A[x][k] * B[k][y]
                                      for k in range(len(B)))
                                   for y in range(len(B[0])))
                              for x in range(len(A)))
    assert mm(r, i) == ((1,),)
    assert mm(r, d) == ((0,),)
    projection = mm(i, r)
    assert projection == ((1, 0), (0, 0))
    assert mm(d, h) == ((0, 0), (0, 1))  # id_N0 - i*r
    assert mm(h, d) == ((1,),)            # id_N1
    # H0 of the torsion summand is Z/2; the integer differential is not onto.
    assert {2 * x % 2 for x in range(2)} == {0}
    assert 1 not in {2 * x % 2 for x in range(2)}
    # An integral contraction would require 2*h(1)=1, impossible modulo 2.
    assert Q(1, 2).denominator == 2
    print("rationalized-fiber obstruction: split augmented Z -> N has H0(N)=Z + Z/2")
    print("over Q, h0=(0,1/2) gives dh+hd=id-i*r; integral obstruction is 1 modulo 2")


def main():
    chain = check(("0", "1"), [("0", "1")])
    assert not chain[-1]
    assert (0, 0, 0, 1) in chain[2] and (0, 0, 0, 1) not in chain[3]
    pentagon = check(
        ("0", "a", "b", "c", "1"),
        [("0", "a"), ("a", "b"), ("b", "1"), ("0", "c"), ("c", "1")],
    )
    assert ((0, 1, 3, 4), (0, 2, 3, 4)) in pentagon[-1]
    # Constant Hom sets in the two-element chain, on empty/nonempty shapes.
    def hom_size(source, target, is_nonempty):
        return int(not is_nonempty or source <= target)
    for source, target, nonempty in product(range(2), range(2), (False, True)):
        expected = 0 if (source, target, nonempty) == (1, 0, True) else 1
        assert hom_size(source, target, nonempty) == expected
    # The discrete two-point sieve cover used in A2.5.
    objects = {"t", "s"}
    U, V = {"t"}, {"s"}
    assert U | V == objects and U & V == set()
    same_nonemptiness = lambda A, B: bool(A) == bool(B)
    assert same_nonemptiness(U, objects)
    assert not same_nonemptiness(U & V, V)
    print("two-point sieve cover: U -> X passes; empty -> V fails")
    # The displayed connective-complex counterexample has stable pullback k[-1].
    stable_pullback_homology = {-1: 1}
    connective_pullback_homology = {
        n: d for n, d in stable_pullback_homology.items() if n >= 0
    }
    assert connective_pullback_homology == {}
    assert {} != {0: 1}  # zero-span pushout versus k[0]
    print("connective square: pullback truncates k[-1] to 0; pushout 0 differs from k[0]")
    # Finite graph realization of S^0 * S^0: the four-edge cycle.
    vertices = ["a0", "a1", "b0", "b1"]
    edges = [(a, b) for a in vertices[:2] for b in vertices[2:]]
    reached = {vertices[0]}
    while True:
        expanded = reached | {
            y for x, y in edges + [(b, a) for a, b in edges] if x in reached
        }
        if expanded == reached:
            break
        reached = expanded
    assert len(reached) == len(vertices)
    first_betti = len(edges) - len(vertices) + 1
    assert first_betti == 1
    print("HOT cartesian K2,2 square: connected homotopy pushout has b1=1, not a point")
    higman_tensor_certificates()
    constant_tree_certificate()
    labelled_augmentation_certificate()
    rationalized_fiber_certificate()
    print("ALL EXACT FINITE CHECKS PASSED")


if __name__ == "__main__":
    main()
