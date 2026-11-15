#!/usr/bin/env python3
"""Reproduce the finite checks used in STRATA Parts C and D.

Run: python3 code/CD_checks.py
Requires Python 3 and sympy. This script verifies finite category axioms,
all relevant naturality equations, lifting-poset certificates, and normalized
nerve/simplicial boundary matrices. Rational homology is never used here as
a substitute for a proof of weak contractibility.
"""
from itertools import product, combinations
from dataclasses import dataclass
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


@dataclass
class Category:
    objects: tuple
    arrows: dict
    identities: dict
    composition: dict

    def comp(self, g, f):
        return self.composition[g, f]

    def hom(self, x, y):
        return [a for a, ends in self.arrows.items() if ends == (x, y)]

    def verify(self):
        pairs = triples = 0
        for a, (x, y) in self.arrows.items():
            assert self.comp(a, self.identities[x]) == a
            assert self.comp(self.identities[y], a) == a
        for f, g in product(self.arrows, repeat=2):
            x, y = self.arrows[f]
            y1, z = self.arrows[g]
            if y != y1:
                assert (g, f) not in self.composition
                continue
            pairs += 1
            assert self.arrows[self.comp(g, f)] == (x, z)
            for h, (z1, _) in self.arrows.items():
                if z == z1:
                    triples += 1
                    assert self.comp(h, self.comp(g, f)) == self.comp(self.comp(h, g), f)
        return pairs, triples

    def is_sieve(self, subset):
        return all(x in subset for x, y in self.arrows.values() if y in subset)

    def full(self, subset):
        subset = set(subset)
        arrows = {a: st for a, st in self.arrows.items() if set(st) <= subset}
        return Category(tuple(x for x in self.objects if x in subset), arrows,
                        {x: self.identities[x] for x in subset},
                        {k: v for k, v in self.composition.items() if k[0] in arrows and k[1] in arrows})


def make_category(objects, extra_arrows, extra_composites):
    ids = {x: 'id_' + str(x) for x in objects}
    arrows = {ids[x]: (x, x) for x in objects} | extra_arrows
    comp = dict(extra_composites)
    for f, (x, y) in arrows.items():
        comp[f, ids[x]] = f
        comp[ids[y], f] = f
    C = Category(tuple(objects), arrows, ids, comp)
    C.verify()
    return C


def poset(objects, generating_pairs):
    relation = {(x, x) for x in objects} | set(generating_pairs)
    while True:
        nxt = relation | {(x, z) for x, y in relation for y1, z in relation if y == y1}
        if nxt == relation:
            break
        relation = nxt
    assert all(x == y or (y, x) not in relation for x, y in relation)
    arrows = {(x, y): (x, y) for x, y in relation}
    comp = {((y, z), (x, y)): (x, z) for x, y in relation for y1, z in relation if y == y1}
    return Category(tuple(objects), arrows, {x: (x, x) for x in objects}, comp)


def verify_endofunctor(C, obj, arr):
    assert set(obj) == set(C.objects) and set(arr) == set(C.arrows)
    for a, (x, y) in C.arrows.items():
        assert C.arrows[arr[a]] == (obj[x], obj[y])
    for x in C.objects:
        assert arr[C.identities[x]] == C.identities[obj[x]]
    for (g, f), h in C.composition.items():
        assert arr[h] == C.comp(arr[g], arr[f])


def verify_natural(C, F, G, eta):
    fo, fa = F
    go, ga = G
    for x in C.objects:
        assert C.arrows[eta[x]] == (fo[x], go[x])
    for a, (x, y) in C.arrows.items():
        assert C.comp(ga[a], eta[x]) == C.comp(eta[y], fa[a])


def identity_functor(C):
    return ({x: x for x in C.objects}, {a: a for a in C.arrows})


def terminal_objects(C):
    return [y for y in C.objects if all(len(C.hom(x, y)) == 1 for x in C.objects)]


def initial_objects(C):
    return [x for x in C.objects if all(len(C.hom(x, y)) == 1 for y in C.objects)]


def connected_components(C):
    remain = set(C.objects)
    out = []
    while remain:
        component = {next(iter(remain))}
        while True:
            new = component | {y for x, y in C.arrows.values() if x in component}
            new |= {x for x, y in C.arrows.values() if y in component}
            if new == component:
                break
            component = new
        remain -= component
        out.append(component)
    return out


def crossing(C, A):
    objs = tuple(a for a, (x, y) in C.arrows.items() if x in A and y not in A)
    arrows = {}
    for f, g in product(objs, repeat=2):
        a, b = C.arrows[f]
        a1, b1 = C.arrows[g]
        for u, v in product(C.hom(a, a1), C.hom(b, b1)):
            if C.comp(v, f) == C.comp(g, u):
                arrows[(f, g, u, v)] = (f, g)
    ids = {f: (f, f, C.identities[C.arrows[f][0]], C.identities[C.arrows[f][1]]) for f in objs}
    comp = {}
    for f, g in product(arrows, repeat=2):
        if arrows[f][1] == arrows[g][0]:
            comp[g, f] = (f[0], g[1], C.comp(g[2], f[2]), C.comp(g[3], f[3]))
    E = Category(objs, arrows, ids, comp)
    E.verify()
    return E


def nerve_chains(C):
    chains = [[(x,) for x in C.objects]]
    nonid = [a for a in C.arrows if a not in C.identities.values()]
    chains.append([(a,) for a in nonid])
    for _ in range(2, len(C.objects) + 1):
        nxt = [chain + (a,) for chain in chains[-1] for a in nonid
               if C.arrows[chain[-1]][1] == C.arrows[a][0]]
        if not nxt:
            break
        chains.append(nxt)
    return chains


def nerve_boundaries(C):
    chains = nerve_chains(C)
    boundaries = [sp.zeros(0, len(chains[0]))]
    for n in range(1, len(chains)):
        matrix = sp.zeros(len(chains[n-1]), len(chains[n]))
        rows = {chain: i for i, chain in enumerate(chains[n-1])}
        for j, chain in enumerate(chains[n]):
            for k in range(n + 1):
                if n == 1:
                    face = (C.arrows[chain[0]][1 if k == 0 else 0],)
                elif k == 0:
                    face = chain[1:]
                elif k == n:
                    face = chain[:-1]
                else:
                    face = chain[:k-1] + (C.comp(chain[k], chain[k-1]),) + chain[k+1:]
                if n > 1 and any(a in C.identities.values() for a in face):
                    continue
                matrix[rows[face], j] += (-1)**k
        boundaries.append(matrix)
    return chains, boundaries


def report_chain_complex(name, sizes, d):
    for n in range(2, len(d)):
        assert d[n-1] * d[n] == sp.zeros(d[n-1].rows, d[n].cols)
    ranks = [m.rank() for m in d] + [0]
    betti = [sizes[n] - ranks[n] - ranks[n+1] for n in range(len(sizes))]
    smith = []
    for m in d[1:]:
        sm = smith_normal_form(m, domain=ZZ)
        vals = [abs(int(sm[i, i])) for i in range(min(sm.rows, sm.cols)) if sm[i, i]]
        smith.append(vals)
    print(name, 'chains=', sizes, 'Betti_Q=', betti, 'nonzero_Smith_boundary_entries=', smith)
    return betti


def report_nerve(name, C):
    pairs, triples = C.verify()
    print(name, 'objects=', len(C.objects), 'arrows=', len(C.arrows),
          'composable_pairs=', pairs, 'composable_triples=', triples,
          'components=', len(connected_components(C)))
    chains, boundaries = nerve_boundaries(C)
    return report_chain_complex(name, list(map(len, chains)), boundaries)


def report_complex(name, maximal_faces):
    faces = {tuple(sorted(s)) for face in maximal_faces
             for k in range(1, len(face)+1) for s in combinations(face, k)}
    chains = [sorted(s for s in faces if len(s) == k) for k in range(1, max(map(len, faces))+1)]
    d = [sp.zeros(0, len(chains[0]))]
    for n in range(1, len(chains)):
        m = sp.zeros(len(chains[n-1]), len(chains[n]))
        rows = {s: i for i, s in enumerate(chains[n-1])}
        for j, face in enumerate(chains[n]):
            for k in range(n+1):
                m[rows[face[:k] + face[k+1:]], j] += (-1)**k
        d.append(m)
    return report_chain_complex(name, list(map(len, chains)), d)


def check_lifts(name, P, Q, f):
    # The extremum tests for strict cartesian/opcartesian lifts below are
    # complete only over [1]. For a longer base they would just be the
    # precartesian/preopcartesian tests, so reject such input here.
    assert Q.objects == (0, 1) and set(Q.arrows) == {(0, 0), (0, 1), (1, 1)}
    assert all((f[x], f[y]) in Q.arrows for x, y in P.arrows.values())
    proper = smooth = opfib = fib = True
    print(name, 'map=', f)
    for direction in ('outgoing', 'incoming'):
        for p in P.objects:
            for q in Q.objects:
                allowed = (f[p], q) in Q.arrows if direction == 'outgoing' else (q, f[p]) in Q.arrows
                if not allowed:
                    continue
                objects = [z for z in P.objects if f[z] == q and
                           ((p, z) in P.arrows if direction == 'outgoing' else (z, p) in P.arrows)]
                L = P.full(objects)
                mins, maxs = initial_objects(L), terminal_objects(L)
                # All test cases have an explicit initial/terminal contraction or are empty.
                assert not objects or mins or maxs
                contractible = bool(objects)
                print(' ', direction, (p, q), 'objects=', objects, 'initial=', mins, 'terminal=', maxs)
                if direction == 'outgoing':
                    proper &= contractible
                    opfib &= bool(mins)
                else:
                    smooth &= contractible
                    fib &= bool(maxs)
    result = (proper, smooth, fib, opfib)
    print(name, '(proper,smooth,fibration,opfibration)=', result)
    return result


def main():
    print('STRATA C/D finite verification; all assertions must pass.')
    parallel = make_category(('a', 'b'), {'r': ('a', 'b'), 's': ('a', 'b')}, {})
    assert parallel.is_sieve({'a'})
    assert report_nerve('C.4_parallel', parallel) == [1, 1]
    E = crossing(parallel, {'a'})
    assert len(connected_components(E)) == 2
    report_nerve('C.4_crossing', E)

    seven = make_category(('a', 't', 's'),
        {'alpha': ('a', 't'), 'beta': ('a', 't'), 'gamma': ('t', 's'), 'delta': ('a', 's')},
        {('gamma', 'alpha'): 'delta', ('gamma', 'beta'): 'delta'})
    assert seven.is_sieve({'a'})
    Fobj = {'a': 'a', 't': 's', 's': 's'}
    Farr = {'id_a': 'id_a', 'id_t': 'id_s', 'id_s': 'id_s', 'alpha': 'delta', 'beta': 'delta', 'gamma': 'id_s', 'delta': 'delta'}
    Robj = {x: 'a' for x in seven.objects}
    Rarr = {f: 'id_a' for f in seven.arrows}
    verify_endofunctor(seven, Fobj, Farr)
    verify_endofunctor(seven, Robj, Rarr)
    verify_natural(seven, identity_functor(seven), (Fobj, Farr), {'a':'id_a','t':'gamma','s':'id_s'})
    verify_natural(seven, (Robj,Rarr), (Fobj,Farr), {'a':'id_a','t':'delta','s':'delta'})
    report_nerve('C.10_seven_arrow', seven)
    E = crossing(seven, {'a'})
    assert terminal_objects(E) == ['delta']
    Et = E.full(['alpha','beta'])
    assert len(connected_components(Et)) == 2
    report_nerve('C.10_total_crossing', E)
    print('C.10 crossing over t has',len(connected_components(Et)),'components; relative naturality PASS')

    eleven = make_category((0,1,'t','s'),
        {'a':(0,1),'beta':(1,'t'),'gamma':(1,'t'),'c':(0,'t'),
         '0s':(0,'s'),'1s':(1,'s'),'ts':('t','s')},
        {('beta','a'):'c',('gamma','a'):'c',('1s','a'):'0s',
         ('ts','beta'):'1s',('ts','gamma'):'1s',('ts','c'):'0s'})
    assert eleven.is_sieve({0,1})
    Fobj={0:0,1:1,'t':'s','s':'s'}
    Farr={'id_0':'id_0','id_1':'id_1','id_t':'id_s','id_s':'id_s',
          'a':'a','beta':'1s','gamma':'1s','c':'0s','0s':'0s','1s':'1s','ts':'id_s'}
    Robj={0:0,1:1,'t':1,'s':1}
    Rarr={'id_0':'id_0','id_1':'id_1','id_t':'id_1','id_s':'id_1',
          'a':'a','beta':'id_1','gamma':'id_1','c':'a','0s':'a','1s':'id_1','ts':'id_1'}
    verify_endofunctor(eleven,Fobj,Farr)
    verify_endofunctor(eleven,Robj,Rarr)
    verify_natural(eleven,identity_functor(eleven),(Fobj,Farr),{0:'id_0',1:'id_1','t':'ts','s':'id_s'})
    verify_natural(eleven,(Robj,Rarr),(Fobj,Farr),{0:'id_0',1:'id_1','t':'1s','s':'1s'})
    report_nerve('C.11_eleven_arrow',eleven)
    print('C.11 relative naturality PASS')

    triangle_edges=[(0,1),(1,2),(0,2)]
    assert report_complex('C.5_boundary_triangle',triangle_edges)==[1,1]
    assert report_complex('C.5_filled_triangle',[(0,1,2)])==[1,0,0]
    sphere=[edge+(apex,) for edge in triangle_edges for apex in (3,4)]
    assert report_complex('C.11_double_cone_circle',sphere)==[1,0,1]
    diagonal=sp.Matrix([[1],[1]])
    assert diagonal.rank()==1
    assert list(smith_normal_form(diagonal,domain=ZZ))==[1,0]
    print('C.7 coker(diagonal Z -> Z^2): free rank=',2-diagonal.rank(),'; no torsion')

    Q=poset((0,1),[(0,1)])
    point=poset(('p',),[])
    assert check_lifts('D.5_point_at_0',point,Q,{'p':0})==(False,True,True,False)
    assert check_lifts('D.5_point_at_1',point,Q,{'p':1})==(True,False,False,True)
    over_one = point.full([p for p in point.objects if (0, 1) in Q.arrows])
    fibre_one = point.full([p for p in point.objects if 0 == 1])
    # A limit of a constant finite set consists of one value per component.
    # This includes the empty indexing category, with its singleton limit.
    source_cardinality = 2 ** len(connected_components(over_one))
    target_cardinality = 2 ** len(connected_components(fibre_one))
    assert (source_cardinality, target_cardinality) == (2, 1)
    print('D.5 failed right base change at 1: source cardinality', source_cardinality,
          ', target cardinality', target_cardinality)
    diamond=poset(('x','a','b','c'),[('x','a'),('x','b'),('a','c'),('b','c')])
    report_nerve('D.6_diamond',diamond)
    assert check_lifts('D.6_diamond_map',diamond,Q,{'x':0,'a':1,'b':1,'c':1})==(True,True,True,False)
    empty=poset((),[])
    assert check_lifts('D.7_empty',empty,Q,{})==(True,True,True,True)
    closures = {p: [q for q in Q.objects if (p, q) in Q.arrows] for p in Q.objects}
    assert closures == {0: [0, 1], 1: [1]}
    print('D.9 closures for downset topology:', closures)
    print('ALL CHECKS PASSED')


if __name__=='__main__':
    main()
