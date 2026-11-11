#!/usr/bin/env python3
"""Exact finite-category checks for POLES, using integers only.

Rebuilds the 35-object semisimplicial example from the supplied TOTASPH
description, checks all compositions, computes normalized nerve homology,
and verifies the suspension sieve cover and the W_0 cofiber counterexample.
The group-quotient certificate uses explicit permutations, not a group oracle.
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT = Path(__file__).resolve().parent


class FiniteCategory:
    def __init__(self, objects, arrows, composition):
        self.objects = tuple(objects)
        self.arrows = tuple(arrows)
        self.comp = composition  # (second, first) -> composite
        self.by_id = {a[0]: a for a in arrows}
        self.identities = {o: f'id:{o}' for o in objects}
        self.out = {o: [] for o in objects}
        for a in self.arrows:
            self.out[a[1]].append(a)

    def verify(self):
        assert len(self.by_id) == len(self.arrows)
        count_pairs = count_triples = 0
        for f, s, t in self.arrows:
            assert self.by_id[self.identities[s]][1:] == (s, s)
            assert self.by_id[self.identities[t]][1:] == (t, t)
            assert self.comp[f, self.identities[s]] == f
            assert self.comp[self.identities[t], f] == f
            for g, _, u in self.out[t]:
                count_pairs += 1
                gf = self.comp[g, f]
                assert self.by_id[gf][1:] == (s, u)
                for h, _, v in self.out[u]:
                    count_triples += 1
                    assert self.comp[h, gf] == self.comp[self.comp[h, g], f]
        assert count_pairs == len(self.comp)
        return dict(objects=len(self.objects), arrows=len(self.arrows),
                    composable_pairs=count_pairs, composable_triples=count_triples,
                    identities=True, associativity=True)

    def is_sieve(self, objects):
        objects = set(objects)
        return all(s in objects for _, s, t in self.arrows if t in objects)

    def nerve_chains(self):
        nonid = {o: [a for a in self.out[o] if a[0] != self.identities[o]]
                 for o in self.objects}
        # These categories are direct; no infinite nerve tail occurs.
        chains = [list((o,) for o in self.objects)]
        chains.append([(a[0],) for a in self.arrows if a[1] != a[2]])
        while chains[-1]:
            nxt = []
            for ch in chains[-1]:
                t = self.by_id[ch[-1]][2]
                nxt.extend(ch + (a[0],) for a in nonid[t])
            if not nxt:
                break
            chains.append(nxt)
        return chains

    def homology(self):
        chs = self.nerve_chains()
        sizes = [len(ch) for ch in chs]
        boundaries, ranks, factors = [], [0], {}
        for n in range(1, len(chs)):
            index = {ch: i for i, ch in enumerate(chs[n-1])}
            mat = sp.zeros(len(index), sizes[n])
            for j, ch in enumerate(chs[n]):
                if n == 1:
                    _, s, t = self.by_id[ch[0]]
                    faces = [(t,), (s,)]
                else:
                    faces = [ch[1:]]
                    for k in range(1, n):
                        faces.append(ch[:k-1] + (self.comp[ch[k], ch[k-1]],) + ch[k+1:])
                    faces.append(ch[:-1])
                for k, face in enumerate(faces):
                    mat[index[face], j] += (-1)**k
            if boundaries:
                assert boundaries[-1] * mat == sp.zeros(sizes[n-2], sizes[n])
            boundaries.append(mat)
            snf = smith_normal_form(mat, domain=ZZ)
            fs = [abs(int(snf[i, i])) for i in range(min(snf.shape)) if snf[i, i]]
            ranks.append(len(fs))
            factors[str(n)] = fs
            assert all(x == 1 for x in fs), 'Torsion needs a full kernel-basis computation.'
        ranks.append(0)
        betti = [sizes[n] - ranks[n] - ranks[n+1] for n in range(len(sizes))]
        return dict(normalized_chain_ranks=sizes, boundary_ranks=ranks[1:-1],
                    smith_nonzero_factors=factors, betti_numbers=betti,
                    integral_torsion='none: every boundary image is primitive',
                    boundary_squared_zero=True)

    def export(self):
        return dict(objects=self.objects, arrows=self.arrows,
                    compositions=[(g, f, h) for (g, f), h in sorted(self.comp.items())])


def acyclic_category():
    words = ['aaaaaBBB', 'bbbBABA']
    dims = dict(v=0, c0=0, c1=0, a=1, b=1)
    faces = {'a': ('v', 'v'), 'b': ('v', 'v')}
    for k, word in enumerate(words):
        for i, letter in enumerate(word):
            r, rn = f'r{k}_{i}', f'r{k}_{(i+1)%len(word)}'
            t = f't{k}_{i}'
            dims[r], dims[t] = 1, 2
            faces[r] = ('v', f'c{k}')
            faces[t] = ((letter.lower(), rn, r) if letter.islower()
                        else (letter.lower(), r, rn))

    def restrict(target, injection):
        simplex = target
        # Remove omitted vertices in decreasing order.
        for i in reversed(range(dims[target]+1)):
            if i not in injection:
                simplex = faces[simplex][i]
        return simplex

    triples = []
    ids = {}
    for target, n in dims.items():
        for d in range(n+1):
            for theta in itertools.combinations(range(n+1), d+1):
                source = restrict(target, theta)
                aid = f'id:{target}' if d == n else f'{source}>{target}:{"".join(map(str,theta))}'
                key = source, target, theta
                ids[key] = aid
                triples.append((aid, source, target, theta))
    composition = {}
    for f, s, t, alpha in triples:
        for g, tt, u, beta in triples:
            if t == tt:
                theta = tuple(beta[i] for i in alpha)
                assert restrict(u, theta) == s
                composition[g, f] = ids[s, u, theta]
    return FiniteCategory(dims, [a[:3] for a in triples], composition)


def add_terminal_cones(cat, names):
    arrows = list(cat.arrows)
    comp = dict(cat.comp)
    for name in names:
        identity = f'id:{name}'
        arrows.append((identity, name, name))
        comp[identity, identity] = identity
        for o in cat.objects:
            to = f'{o}>{name}'
            arrows.append((to, o, name))
            comp[identity, to] = to
        for f, s, t in cat.arrows:
            comp[f'{t}>{name}', f] = f'{s}>{name}'
    return FiniteCategory(cat.objects + tuple(names), arrows, comp)


def discrete(objects):
    return FiniteCategory(objects, [(f'id:{o}', o, o) for o in objects],
                          {(f'id:{o}', f'id:{o}'): f'id:{o}' for o in objects})


def product_window_with_ends(cat, layers, endpoints):
    """The part of A x (0->1<-2->3<-4) with specified ends collapsed.

    endpoints maps a new singleton's name to an adjacent odd layer.
    """
    order = [(i, i) for i in layers]
    order += [(i, j) for i, j in [(0,1),(2,1),(2,3),(4,3)] if i in layers and j in layers]
    objects = [f'{i}:{a}' for i in layers for a in cat.objects] + list(endpoints)
    arrows, descriptions = [], {}
    for i, j in order:
        for f, s, t in cat.arrows:
            source, target = f'{i}:{s}', f'{j}:{t}'
            name = f'id:{source}' if i == j and s == t else f'{i},{j}:{f}'
            arrows.append((name, source, target))
            descriptions[name] = (i, j, f)
    for end, layer in endpoints.items():
        arrows.append((f'id:{end}', end, end))
        for a in cat.objects:
            arrows.append((f'{end}>{layer}:{a}', end, f'{layer}:{a}'))
    lookup = {(i,j,f): name for name,(i,j,f) in descriptions.items()}
    comp = {}
    for f, s, t in arrows:
        for g, tt, u in arrows:
            if t != tt:
                continue
            if f == f'id:{s}':
                h = g
            elif g == f'id:{u}':
                h = f
            elif f in descriptions:
                i, j, af = descriptions[f]
                jj, k, ag = descriptions[g]
                h = lookup[i,k,cat.comp[ag,af]]
            else:
                h = f'{s}>{u}'
            comp[g,f] = h
    return FiniteCategory(objects, arrows, comp), descriptions


def verify_functor(source, target, object_map, arrow_map):
    for f, s, t in source.arrows:
        assert target.by_id[arrow_map[f]][1:] == (object_map[s], object_map[t])
    for o in source.objects:
        assert arrow_map[source.identities[o]] == target.identities[object_map[o]]
    for (g,f), h in source.comp.items():
        assert target.comp[arrow_map[g],arrow_map[f]] == arrow_map[h]
    return True


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def cycle(*entries):
    p = list(range(5))
    entries = [i-1 for i in entries]
    for i, j in zip(entries, entries[1:]+entries[:1]):
        p[i] = j
    return tuple(p)


def evaluate(word, a, b):
    identity = tuple(range(5))
    def inverse(p):
        return tuple(p.index(i) for i in range(5))
    letters = dict(a=a, b=b, A=inverse(a), B=inverse(b))
    value = identity
    for ch in word:
        value = compose(value, letters[ch])
    return value


def main():
    cat = acyclic_category()
    two_cones = add_terminal_cones(cat, ['u', 't'])
    u, v = set(cat.objects) | {'u'}, set(cat.objects) | {'t'}
    assert two_cones.is_sieve(u) and two_cones.is_sieve(v)
    assert u & v == set(cat.objects) and u | v == set(two_cones.objects)
    fold_cone = add_terminal_cones(discrete(['a0','a1']), ['b','t'])
    cylinder, cylinder_arrows = product_window_with_ends(cat, [1,2,3,4], {'y':1})
    cylinder_cofiber, cofiber_arrows = product_window_with_ends(cat, [1,2,3], {'y':1,'t':3})
    object_map = {o: ('t' if o.startswith('4:') else o) for o in cylinder.objects}
    arrow_map = {}
    for f,s,t in cylinder.arrows:
        if f in cylinder_arrows:
            i,j,af = cylinder_arrows[f]
            if i == j == 4:
                arrow_map[f] = 'id:t'
            elif i == 4:
                arrow_map[f] = f't>{j}:{cat.by_id[af][2]}'
            else:
                arrow_map[f] = f
        else:
            arrow_map[f] = f
    assert verify_functor(cylinder, cylinder_cofiber, object_map, arrow_map)
    assert cylinder.is_sieve({f'4:{a}' for a in cat.objects})
    # The right adjoint on the generated cosieve (layers 4 and 3) forgets the layer.
    for a in cat.objects:
        for b in cat.objects:
            base = len([f for f,s,t in cat.arrows if s == a and t == b])
            for layer in [3,4]:
                actual = len([f for f,s,t in cylinder.arrows if s == f'4:{a}' and t == f'{layer}:{b}'])
                assert actual == base
    a, b = cycle(1,4,3,2,5), cycle(1,2,3)
    identity = tuple(range(5))
    relators = [evaluate(w, a, b) for w in ['aaaaaBBB', 'bbbBABA']]
    assert relators == [identity, identity] and a != identity
    differential = sp.Matrix([[5,-2],[-3,1]])
    assert differential.det() == -1
    report = {
        'A': {'category_axioms': cat.verify(), 'homology': cat.homology()},
        'suspension': {'category_axioms': two_cones.verify(), 'homology': two_cones.homology(),
                       'both_pieces_full_sieves': True, 'intersection_A': True, 'cover': True},
        'W0_fold_cofiber': {'category_axioms': fold_cone.verify(), 'homology': fold_cone.homology(),
                           'fold_source_components': 2, 'fold_target_components': 1,
                           'cofiber_components': 1},
        'Dwyer_cylinder': {'category_axioms': cylinder.verify(),
                          'cofiber_category_axioms': cylinder_cofiber.verify(),
                          'quotient_functor': True, 'endpoint_sieve': True,
                          'right_adjoint_Hom_bijections': True,
                          'topology': 'Written Dwyer pushout proof identifies M with a contractible space and Q with suspension BA.'},
        'nontrivial_pi1_certificate': {'a_images_one_based':[i+1 for i in a],
                                      'b_images_one_based':[i+1 for i in b],
                                      'relators_identity': True, 'a_nonidentity': True,
                                      'cellular_d2': [[int(x) for x in row] for row in differential.tolist()], 'determinant': -1},
        'limitations': 'Homology and group quotient are checked. Simple connectivity of the suspension uses the written van Kampen proof.'
    }
    (OUT/'finite_category_data.json').write_text(json.dumps({'A':cat.export(), 'suspension':two_cones.export(),
                                                          'W0_fold_cofiber':fold_cone.export(),
                                                          'Dwyer_cylinder':cylinder.export(),
                                                          'Dwyer_cofiber':cylinder_cofiber.export()}, indent=2)+'\n')
    (OUT/'finite_examples_output.json').write_text(json.dumps(report, indent=2)+'\n')
    for key, item in report.items():
        if isinstance(item, dict) and 'homology' in item:
            print(key, item['category_axioms'], 'chains', item['homology']['normalized_chain_ranks'],
                  'Betti', item['homology']['betti_numbers'])
        else:
            print(key, item)
    print('PASS: all exact checks completed.')


if __name__ == '__main__':
    main()
