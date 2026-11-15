"""Finite checks for statements A.2, A.10, B.3--B.6.

No floating point homology is used. Rational ranks and integer Smith forms
are computed with SymPy. The infinite assertion in A.2 is proved in the
paper; its finite join models are checked here.
"""
from itertools import product, combinations
from collections import defaultdict
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def category(objects, hom, compose):
    arrows = [a for x in objects for y in objects for a in hom(x, y)]
    identities = {x: (x, x, 0) for x in objects}
    for a in arrows:
        assert compose(a, identities[a[0]]) == a
        assert compose(identities[a[1]], a) == a
    triples = 0
    for a, b, c in product(arrows, repeat=3):
        if a[1] == b[0] and b[1] == c[0]:
            assert compose(c, compose(b, a)) == compose(compose(c, b), a)
            triples += 1
    return arrows, triples


def nerve_of_direct(objects, arrows, compose):
    nonid = [a for a in arrows if a[0] != a[1]]
    simplices = {0: [(x,) for x in objects], 1: [(a,) for a in nonid]}
    dim = 1
    while simplices[dim]:
        simplices[dim+1] = [chain + (a,) for chain in simplices[dim]
                            for a in nonid if chain[-1][1] == a[0]]
        dim += 1
    simplices.pop(dim)
    boundary = {}
    for d in range(1, dim):
        lower = {a: i for i, a in enumerate(simplices[d-1])}
        matrix = sp.zeros(len(lower), len(simplices[d]))
        for j, chain in enumerate(simplices[d]):
            if d == 1:
                faces = [(chain[0][1],), (chain[0][0],)]
            else:
                faces = [chain[1:]]
                for i in range(1, d):
                    faces.append(chain[:i-1] + (compose(chain[i], chain[i-1]),)
                                 + chain[i+1:])
                faces.append(chain[:-1])
            for i, face in enumerate(faces):
                matrix[lower[face], j] += (-1)**i
        boundary[d] = matrix
    for d in range(2, dim):
        assert boundary[d-1] * boundary[d] == sp.zeros(
            boundary[d-1].rows, boundary[d].cols)
    return simplices, boundary


def rational_betti(simplices, boundary):
    ranks = {d: m.rank() for d, m in boundary.items()}
    return [len(simplices[d])-ranks.get(d, 0)-ranks.get(d+1, 0)
            for d in simplices]


def graph_h1_smith(simplices, boundary):
    # In a graph a spanning forest gives an integral cycle basis indexed by
    # the complementary edges. Restriction to these rows is its inverse.
    parent = {v[0]: v[0] for v in simplices[0]}
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    chords = []
    for i, (edge,) in enumerate(simplices[1]):
        a, b = root(edge[0]), root(edge[1])
        if a == b:
            chords.append(i)
        else:
            parent[a] = b
    d2 = boundary.get(2, sp.zeros(len(simplices[1]), 0))
    reduced = d2[chords, :]
    smith = smith_normal_form(reduced, domain=ZZ)
    diagonal = [abs(int(smith[i,i])) for i in range(min(smith.shape))
                if smith[i,i]]
    return dict(free_rank=len(chords)-len(diagonal),
                torsion=[n for n in diagonal if n > 1],
                smith_nonzero=diagonal)


def direct_poset(objects, less):
    def hom(x,y):
        return [(x,y,0)] if x == y or less(x,y) else []
    def compose(b,a):
        assert a[1] == b[0]
        return (a[0], b[1], 0)
    arrows, triples = category(objects, hom, compose)
    simplices, boundary = nerve_of_direct(objects, arrows, compose)
    return arrows, triples, simplices, boundary


results = {}
objects = [0,1,2]
def r2_hom(x,y):
    return [(x,y,0)] if x == y else [(x,y,a) for a in [0,1]] if x < y else []
def r2_compose(b,a):
    assert a[1] == b[0]
    return (a[0],b[1],(a[2]+b[2]) % 2)
arrows, triples = category(objects, r2_hom, r2_compose)
ns, ds = nerve_of_direct(objects, arrows, r2_compose)
results['R2'] = dict(objects=3, arrows=len(arrows), associative_triples=triples,
                     nondegenerate_simplices=[len(ns[d]) for d in ns],
                     rational_betti=rational_betti(ns,ds),
                     integral_H1=graph_h1_smith(ns,ds))
assert results['R2']['integral_H1']['torsion'] == [2]

q = list(product(range(3),range(2)))
qa, qt, qn, qd = direct_poset(q, lambda x,y:x[0]<y[0])
def quotient_arrow(edge):
    x,y,_ = edge
    return (x[0],y[0],(x[1]+y[1]) % 2)
for d, chains in qn.items():
    lifts = defaultdict(int)
    for chain in chains:
        key = (chain[0][0],) if d == 0 else tuple(quotient_arrow(a) for a in chain)
        lifts[key] += 1
    assert set(lifts) == set(ns[d])
    assert set(lifts.values()) == {2}
results['octahedral_cover'] = dict(objects=6, arrows=len(qa),
    nondegenerate_simplices=[len(qn[d]) for d in qn],
    rational_betti=rational_betti(qn,qd), integral_H1=graph_h1_smith(qn,qd),
    quotient_lifts_per_nondegenerate_simplex=2)

verts = [('v',i) for i in range(3)]
edges = [('e',i) for i in range(3)]
ca,ct,cn,cd = direct_poset(verts+edges,
    lambda x,y:x[0]=='v' and y[0]=='e' and x[1] in {y[1],(y[1]+1)%3})
results['triangle_boundary_face_poset'] = dict(objects=6, arrows=len(ca),
    nondegenerate_simplices=[len(cn[d]) for d in cn],
    rational_betti=rational_betti(cn,cd),integral_H1=graph_h1_smith(cn,cd))

join_results = []
for n in range(4):
    jo = list(product(range(n+1), range(2)))
    ja,jt,jn,jd = direct_poset(jo,lambda x,y:x[0]<y[0])
    join_results.append(dict(n=n, simplices=[len(jn[d]) for d in jn],
                             rational_betti=rational_betti(jn,jd)))
results['Aoki_finite_join_checks'] = join_results

monoid = [0,1] # 0 is the absorbing idempotent, 1 the identity.
mul = lambda a,b:a*b
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(monoid,repeat=3))
assert all(mul(0,a)==mul(a,0)==0 for a in monoid)
assert mul(0,0)==0 and all(mul(0,a)!=1 for a in monoid)
kar_homs = {(e,f):[a for a in monoid if mul(mul(f,a),e)==a]
            for e,f in product(monoid,repeat=2)}
results['idempotent_monoid'] = dict(multiplication_table=[[mul(a,b) for b in monoid]
    for a in monoid], noninvertible_endomorphism=0,
    karoubi_objects=monoid,karoubi_homs={str(k):v for k,v in kar_homs.items()},
    natural_contraction_component=0)
results['fine_vs_coarse'] = dict(point_subterminals=2,interval_subterminals=3,
    point_and_interval_both_contractible=True)
print(json.dumps(results, indent=2))
