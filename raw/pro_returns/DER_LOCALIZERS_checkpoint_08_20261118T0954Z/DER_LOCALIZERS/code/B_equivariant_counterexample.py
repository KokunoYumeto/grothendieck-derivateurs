#!/usr/bin/env python3
"""Finite certificate for B.13; the unbounded RLP is proved in B.tex."""
from itertools import product, combinations

G = (0, 1)
APEX = 2
E_OBJECTS = G
D_OBJECTS = G + (APEX,)
E_ARROWS = {(a, b) for a in G for b in G}
D_ARROWS = E_ARROWS | {(a, APEX) for a in G} | {(APEX, APEX)}


def compose(f, g):
    assert f[1] == g[0]
    return (f[0], g[1])


def action_object(g, a):
    return a if a == APEX else g ^ a


def action_arrow(g, f):
    return tuple(action_object(g, a) for a in f)


def check_category(objects, arrows):
    assert {(a, a) for a in objects} <= arrows
    triples = 0
    for f, g in product(arrows, repeat=2):
        if f[1] == g[0]:
            assert compose(f, g) in arrows
    for f, g, h in product(arrows, repeat=3):
        if f[1] == g[0] and g[1] == h[0]:
            assert compose(compose(f, g), h) == compose(f, compose(g, h))
            triples += 1
    for g in G:
        assert {action_arrow(g, f) for f in arrows} == arrows
        for f, h in product(arrows, repeat=2):
            if f[1] == h[0]:
                assert action_arrow(g, compose(f, h)) == compose(
                    action_arrow(g, f), action_arrow(g, h)
                )
    assert all(action_object(1, action_object(1, a)) == a for a in objects)
    terminal = [b for b in objects if all((a, b) in arrows for a in objects)]
    fixed = [a for a in objects if action_object(1, a) == a]
    return triples, terminal, fixed


e_check = check_category(E_OBJECTS, E_ARROWS)
d_check = check_category(D_OBJECTS, D_ARROWS)
assert E_ARROWS <= D_ARROWS
assert e_check[1] == [0, 1] and e_check[2] == []
assert d_check[1] == [APEX] and d_check[2] == [APEX]
assert all((b, a) in E_ARROWS for a, b in E_ARROWS)  # E is a groupoid.


def nerve(objects, arrows, degree):
    return {
        xs for xs in product(objects, repeat=degree + 1)
        if all((xs[i], xs[i + 1]) in arrows for i in range(degree))
    }


def act(g, simplex):
    return tuple(action_object(g, a) for a in simplex)


def face(simplex, i):
    return simplex[:i] + simplex[i + 1:]


def degeneracy(simplex, i):
    return simplex[:i] + (simplex[i],) + simplex[i:]


nerve_rows = []
for n in range(7):
    en = nerve(E_OBJECTS, E_ARROWS, n)
    dn = nerve(D_OBJECTS, D_ARROWS, n)
    assert en <= dn
    assert len(en) == 2 ** (n + 1)
    assert len(dn) == 2 ** (n + 2) - 1
    efixed = {x for x in en if act(1, x) == x}
    dfixed = {x for x in dn if act(1, x) == x}
    assert not efixed and dfixed == {(APEX,) * (n + 1)}
    for xs in dn:
        assert act(1, xs) in dn
        if n:
            for i in range(n + 1):
                assert face(act(1, xs), i) == act(1, face(xs, i))
        for i in range(n + 1):
            assert degeneracy(act(1, xs), i) == act(1, degeneracy(xs, i))
    nerve_rows.append((n, len(en), len(dn), len(efixed), len(dfixed)))


# All small C2-set actions are involutions. Verify the fixed-point emptiness
# invariant for sectioned-interval generators in these finite models.
def involutions(n):
    def extend(remaining, partial):
        if not remaining:
            yield tuple(partial[i] for i in range(n))
            return
        a = min(remaining)
        rest = remaining - {a}
        yield from extend(rest, partial | {a: a})
        for b in sorted(rest):
            yield from extend(rest - {b}, partial | {a: b, b: a})
    yield from extend(set(range(n)), {})


def subsets(xs):
    return (set(c) for k in range(len(xs) + 1) for c in combinations(xs, k))


generator_checks = 0
for lsize in range(5):
    for lact in involutions(lsize):
        ls = set(range(lsize))
        for ks in subsets(tuple(ls)):
            if {lact[k] for k in ks} != ks:
                continue
            for isize in range(1, 5):
                for iact in involutions(isize):
                    for e in range(isize):
                        if iact[e] != e:
                            continue
                        target = set(product(ls, range(isize)))
                        source = {(l, e) for l in ls} | set(product(ks, range(isize)))
                        sf = {x for x in source if (lact[x[0]], iact[x[1]]) == x}
                        tf = {x for x in target if (lact[x[0]], iact[x[1]]) == x}
                        assert bool(sf) == bool(tf)
                        generator_checks += 1

print('E_category_objects_arrows', len(E_OBJECTS), len(E_ARROWS))
print('D_category_objects_arrows', len(D_OBJECTS), len(D_ARROWS))
print('E_associativity_triples_terminal_objects_fixed_vertices', e_check)
print('D_associativity_triples_terminal_objects_fixed_vertices', d_check)
print('E_is_groupoid', True)
print('nerve_degree_E_size_D_size_E_fixed_D_fixed', nerve_rows)
print('fixed_support_generator_checks', generator_checks)
print('unextendible_equivariant_map', 'identity E cannot extend over fixed cone vertex')
print('certificate_passed', True)
