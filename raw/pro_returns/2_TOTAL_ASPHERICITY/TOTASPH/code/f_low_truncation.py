"""Finite W_0/W_1 sieve-composition counterexamples for Part F.

Run from any directory with Python 3 and sympy available.  The shared
f_check module supplies exhaustive category/functor/naturality checks
and integral normalized-nerve homology.  This file constructs every
arrow and composition, verifies the classical right adjoint and the
deformation onto the initial cone, constructs the composite slice,
and prints complete target arrow/composition tables.
"""

import json

from f_check import Category, functor_check, natural_check, homology


def full_subcategory(C, objects):
    objects = list(objects)
    selected = set(objects)
    arrows = {f: st for f, st in C.arrows.items()
              if st[0] in selected and st[1] in selected}
    return Category(objects, arrows,
                    {a: C.identities[a] for a in objects},
                    {(g, f): h for (g, f), h in C.composition.items()
                     if f in arrows and g in arrows})


def make_v(parallel):
    objects = ['a', 'b']
    arrows = {'id_a': ('a', 'a'), 'id_b': ('b', 'b')}
    if parallel:
        arrows.update(alpha=('a', 'b'), beta=('a', 'b'))
    ids = {'a': 'id_a', 'b': 'id_b'}
    comp = {}
    for f, (a, b) in arrows.items():
        comp[ids[b], f] = f
        comp[f, ids[a]] = f
    return Category(objects, arrows, ids, comp)


def initial_cone(V):
    objects = ['o'] + V.objects
    arrows = dict(V.arrows)
    arrows['id_o'] = ('o', 'o')
    arrows.update({f'from_o_{a}': ('o', a) for a in V.objects})
    ids = {'o': 'id_o', **V.identities}
    comp = {}
    for f, (a, b) in arrows.items():
        for g, (bb, c) in arrows.items():
            if b != bb:
                continue
            if f == ids[a]:
                h = g
            elif g == ids[b]:
                h = f
            elif a == 'o':
                h = f'from_o_{c}'
            else:
                h = V.comp(g, f)
            comp[g, f] = h
    return Category(objects, arrows, ids, comp)


def lower_copy(V, B):
    objects = [('old', a) for a in B.objects]
    objects += [('low', a) for a in V.objects]
    arrows = {('old', f): (('old', a), ('old', b))
              for f, (a, b) in B.arrows.items()}
    arrows.update({('low', f): (('low', a), ('low', b))
                   for f, (a, b) in V.arrows.items()})
    arrows.update({('cross', f): (('low', a), ('old', b))
                   for f, (a, b) in V.arrows.items()})
    ids = {('old', a): ('old', B.identities[a]) for a in B.objects}
    ids.update({('low', a): ('low', V.identities[a]) for a in V.objects})
    comp = {}
    for f, (a, b) in arrows.items():
        for g, (bb, c) in arrows.items():
            if b != bb:
                continue
            if f[0] == g[0] == 'old':
                h = ('old', B.comp(g[1], f[1]))
            elif f[0] == g[0] == 'low':
                h = ('low', V.comp(g[1], f[1]))
            elif f[0] == 'low' and g[0] == 'cross':
                h = ('cross', V.comp(g[1], f[1]))
            elif f[0] == 'cross' and g[0] == 'old':
                h = ('cross', B.comp(g[1], f[1]))
            else:
                raise AssertionError((f, g))
            comp[g, f] = h
    return Category(objects, arrows, ids, comp)


def terminal_cone(X):
    objects = X.objects + ['t']
    arrows = dict(X.arrows)
    arrows[('id_t',)] = ('t', 't')
    arrows.update({('to_t', a): (a, 't') for a in X.objects})
    ids = {**X.identities, 't': ('id_t',)}
    comp = {}
    for f, (a, b) in arrows.items():
        for g, (bb, c) in arrows.items():
            if b != bb:
                continue
            if g == ('id_t',):
                h = f
            elif g[0] == 'to_t':
                h = ('to_t', a)
            else:
                h = X.comp(g, f)
            comp[g, f] = h
    return Category(objects, arrows, ids, comp)


def comma_slice(C, source_objects, target):
    objects = [(u, a) for u in source_objects for a in C.hom(u, target)]
    arrows = {}
    for x in objects:
        for y in objects:
            for f in C.hom(x[0], y[0]):
                if C.comp(y[1], f) == x[1]:
                    arrows[x, y, f] = (x, y)
    ids = {x: (x, x, C.identities[x[0]]) for x in objects}
    comp = {}
    for f, (x, y) in arrows.items():
        for g, (yy, z) in arrows.items():
            if y == yy:
                comp[g, f] = (x, z, C.comp(g[2], f[2]))
    return Category(objects, arrows, ids, comp)


def sieve_check(C, objects):
    objects = set(objects)
    assert all(a in objects for a, b in C.arrows.values() if b in objects)
    return True


def tables(C):
    return {
        'objects': [repr(a) for a in C.objects],
        'arrows': [{'arrow': repr(f), 'source': repr(a), 'target': repr(b)}
                   for f, (a, b) in C.arrows.items()],
        'composition': [{'after': repr(g), 'before': repr(f), 'result': repr(h)}
                        for (g, f), h in C.composition.items()]
    }


def check_example(parallel):
    V = make_v(parallel)
    B = initial_cone(V)
    X = lower_copy(V, B)
    Y = terminal_cone(X)
    V0 = full_subcategory(X, [('low', v) for v in V.objects])
    closure = {b for a, b in X.arrows.values() if a in V0.objects}
    expected = {('low', v) for v in V.objects} | {('old', v) for v in V.objects}
    assert closure == expected
    W = full_subcategory(X, [a for a in X.objects if a in closure])
    for C in [V, B, X, Y, V0, W]:
        C.check()
    sieve_check(X, V0.objects)
    sieve_check(Y, X.objects)
    sieve_check(Y, V0.objects)

    # a:V0 -> W has right adjoint forgetting the copy.
    Robj = {a: ('low', a[1]) for a in W.objects}
    Rarr = {f: ('low', f[1]) for f in W.arrows}
    functor_check(W, V0, Robj, Rarr)
    Jobj = {a: a for a in V0.objects}
    Jarr = {f: f for f in V0.arrows}
    functor_check(V0, W, Jobj, Jarr)
    eps = {a: W.identities[a] if a[0] == 'low'
           else ('cross', V.identities[a[1]]) for a in W.objects}
    natural_check(W, W, Robj, Rarr,
                  {a: a for a in W.objects}, {f: f for f in W.arrows}, eps)
    assert all(Rarr[eps[a]] == V0.identities[Robj[a]] for a in W.objects)
    assert all(eps[a] == V0.identities[a] for a in V0.objects)

    # r:X -> B and j:B -> X satisfy rj=id and Id_X -> jr, relative to B.
    robj = {a: a[1] for a in X.objects}
    rarr = {f: f[1] for f in X.arrows}
    jobj = {a: ('old', a) for a in B.objects}
    jarr = {f: ('old', f) for f in B.arrows}
    functor_check(X, B, robj, rarr)
    functor_check(B, X, jobj, jarr)
    assert all(robj[jobj[a]] == a for a in B.objects)
    assert all(rarr[jarr[f]] == f for f in B.arrows)
    jr_obj = {a: jobj[robj[a]] for a in X.objects}
    jr_arr = {f: jarr[rarr[f]] for f in X.arrows}
    eta = {a: X.identities[a] if a[0] == 'old'
           else ('cross', V.identities[a[1]]) for a in X.objects}
    natural_check(X, X, {a: a for a in X.objects},
                  {f: f for f in X.arrows}, jr_obj, jr_arr, eta)
    assert all(len(B.hom('o', a)) == 1 for a in B.objects)
    assert all(len(Y.hom(a, 't')) == 1 for a in Y.objects)

    # Construct the composite boundary category rather than only naming it.
    S = comma_slice(Y, V0.objects, 't')
    S.check()
    sobj = {v: (('low', v), ('to_t', ('low', v))) for v in V.objects}
    sarr = {f: (sobj[a], sobj[b], ('low', f))
            for f, (a, b) in V.arrows.items()}
    functor_check(V, S, sobj, sarr)
    assert set(sobj.values()) == set(S.objects)
    assert set(sarr.values()) == set(S.arrows)
    assert len(sobj) == len(set(sobj.values()))
    assert len(sarr) == len(set(sarr.values()))
    sv = homology(S)
    expected_betti = [1, 1] if parallel else [2]
    assert sv['integral_homology_free_ranks'] == expected_betti
    assert homology(X)['integral_homology_free_ranks'][0] == 1
    assert all(b == 0 for b in homology(X)['integral_homology_free_ranks'][1:])
    assert len(Y.objects) == 6
    assert len(Y.arrows) == (21 if parallel else 15)
    return {
        'case': 'parallel_arrow_circle_W1' if parallel else 'discrete_pair_W0',
        'V': {**V.check(), **homology(V)},
        'B_initial_cone': {**B.check(), **homology(B)},
        'X_lower_copy': {**X.check(), **homology(X)},
        'Y_terminal_cone': {**Y.check(), **homology(Y)},
        'composite_boundary_slice': {**S.check(), **sv},
        'both_inclusions_and_composite_are_full_sieves': True,
        'first_factor_classical_right_adjoint_and_triangles_verified': True,
        'X_deformation_onto_B_verified': True,
        'B_initial_and_Y_terminal_objects_verified': True,
        'composite_slice_isomorphism_to_V_verified': True,
        'target_complete_tables': tables(Y)
    }


if __name__ == '__main__':
    print(json.dumps([check_example(False), check_example(True)], indent=2))
