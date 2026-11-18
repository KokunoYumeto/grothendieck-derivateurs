#!/usr/bin/env python3
"""Finite certificate for B.12; no external dependencies.

The base [1] has objects 0,1 and one nonidentity arrow 0->1.
A presheaf on Delta x [1] whose simplicial components are constant
is determined by the finite [1]-diagram recorded here.
"""
from itertools import product

objects = (0, 1)
arrows = ((0, 0), (0, 1), (1, 1))

def compose(g, f):
    assert f[1] == g[0]
    result = (f[0], g[1])
    assert result in arrows
    return result

for f, g, h in product(arrows, repeat=3):
    if f[1] == g[0] and g[1] == h[0]:
        assert compose(h, compose(g, f)) == compose(compose(h, g), f)

def representable(target):
    values = {source: tuple(a for a in arrows if a == (source, target))
              for source in objects}
    restrictions = {}
    for f in arrows:
        restrictions[f] = {x: compose(x, f) for x in values[f[1]]}
        assert all(y in values[f[0]] for y in restrictions[f].values())
    return values, restrictions

r0, rho0 = representable(0)
r1, rho1 = representable(1)
u = (0, 1)
yoneda = {a: {x: compose(u, x) for x in r0[a]} for a in objects}
for a in objects:
    assert len(set(yoneda[a].values())) == len(r0[a])
for f in arrows:
    for x in r0[f[1]]:
        assert rho1[f][yoneda[f[1]][x]] == yoneda[f[0]][rho0[f][x]]

support0 = {a for a in objects if r0[a]}
support1 = {a for a in objects if r1[a]}
assert support0 == {0}
assert support1 == {0, 1}
assert len(r0[0]) == len(r1[0]) == 1
assert len(r0[1]) == 0 and len(r1[1]) == 1

def elements(values, restrictions):
    objs = tuple((a, x) for a in objects for x in values[a])
    morphisms = []
    for source, target in product(objs, repeat=2):
        for f in arrows:
            if f == (source[0], target[0]) and restrictions[f][target[1]] == source[1]:
                morphisms.append((source, target, f))
    terminal = [t for t in objs
                if all(sum(1 for s, z, f in morphisms if s == x and z == t) == 1
                       for x in objs)]
    return objs, tuple(morphisms), terminal

el0 = elements(r0, rho0)
el1 = elements(r1, rho1)
assert len(el0[0]) == 1 and len(el0[1]) == 1 and len(el0[2]) == 1
assert len(el1[0]) == 2 and len(el1[1]) == 3 and len(el1[2]) == 1
assert el0[2][0] == (0, (0, 0))
assert el1[2][0] == (1, (1, 1))

# Cardinal formula for a pointwise interval generator:
# |L union_K (K x I)| = |L| + |K| (|I|-1), |L x I| = |L||I|.
# Sectioned I is nonempty, so both vanish exactly when L is empty.
finite_generator_checks = 0
for l in range(5):
    for k in range(l + 1):
        for interval_size in range(1, 5):
            source_size = l + k * (interval_size - 1)
            target_size = l * interval_size
            assert (source_size == 0) == (target_size == 0) == (l == 0)
            finite_generator_checks += 1

print('base_objects:', objects)
print('base_arrows:', arrows)
print('y(0)_values:', r0)
print('y(1)_values:', r1)
print('Yoneda_mono_components:', yoneda)
print('source_support:', sorted(support0))
print('target_support:', sorted(support1))
print('evaluation_0: bijection between singleton sets')
print('evaluation_1: empty -> singleton')
print('elements_y(0):', len(el0[0]), 'objects,', len(el0[1]), 'arrows; terminal:', el0[2])
print('elements_y(1):', len(el1[0]), 'objects,', len(el1[1]), 'arrows; terminal:', el1[2])
print('finite_generator_cardinality_checks:', finite_generator_checks)
print('RESULT: the Yoneda mono is a weak equivalence at 0 and violates support invariance at 1.')
