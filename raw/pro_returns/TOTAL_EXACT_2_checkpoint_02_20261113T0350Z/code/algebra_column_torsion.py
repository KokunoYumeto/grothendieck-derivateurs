"""Find an explicit torsion column cokernel for a finite three-level category.

The category has p, q, x, three arrows a_i:p->q, and arrows g:q->x.
The triples specify composites g a_i in the set of arrows c_v:p->x.
Adjoining a terminal object makes this a finite filtered (hence total) category
without changing the displayed module at x.
"""
from itertools import combinations, permutations
import json

import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def matrix(triples, n):
    d = S.zeros(2*n, len(triples))
    for j, (v0, v1, v2) in enumerate(triples):
        d[v1,j] += 1
        d[v0,j] -= 1
        d[n+v2,j] += 1
        d[n+v0,j] -= 1
    return d


def run():
    for n in range(3, 6):
        candidates = list(permutations(range(n), 3))
        for count in range(2, min(7, len(candidates))+1):
            for triples in combinations(candidates, count):
                d = matrix(triples,n)
                snf = smith_normal_form(d, domain=ZZ)
                diagonal = [int(snf[i,i]) for i in range(min(snf.shape))]
                torsion = [abs(v) for v in diagonal if abs(v)>1]
                if torsion:
                    result = {
                        "vertices":n,
                        "triples":triples,
                        "column_matrix":[[int(v) for v in row] for row in d.tolist()],
                        "smith_diagonal":diagonal,
                        "torsion_invariants":torsion,
                        "free_rank":2*n-d.rank(),
                    }
                    result["category_verification"] = verify_category(triples)
                    reduced = S.Matrix([[1,0,-1,-1],[0,1,0,1],
                                        [0,1,-1,-1],[1,0,1,0]])
                    w = S.Matrix([1,1,-1,-1])
                    v = S.Matrix([1,0,1,0])
                    assert triples == ((0,1,2),(0,2,1),(1,0,2),(1,2,0))
                    assert reduced.det() == 3
                    assert reduced[:3,:3].det() == -1
                    assert reduced*w == 3*v
                    assert reduced.inv()*v == w/3
                    result["reduced_matrix"] = [list(map(int,row)) for row in reduced.tolist()]
                    result["reduced_determinant"] = int(reduced.det())
                    result["unit_3x3_minor"] = int(reduced[:3,:3].det())
                    result["order_three_class"] = list(map(int,v))
                    result["triple_preimage"] = list(map(int,w))
                    result["unique_rational_preimage"] = [str(vv) for vv in reduced.inv()*v]
                    return result
    raise AssertionError("No example in the stated search")


def verify_category(triples):
    objects = ('p','q','x','t')
    arrows = {f'id_{o}':(o,o) for o in objects}
    arrows.update({f'a{i}':('p','q') for i in range(3)})
    arrows.update({f'g{j}':('q','x') for j in range(4)})
    arrows.update({f'c{v}':('p','x') for v in range(3)})
    arrows.update({f'u_{o}':(o,'t') for o in objects[:-1]})

    def compose(f,g): # f after g
        assert arrows[g][1] == arrows[f][0]
        if f.startswith('id_'):
            return g
        if g.startswith('id_'):
            return f
        if arrows[f][1] == 't':
            return f'u_{arrows[g][0]}'
        if f.startswith('g') and g.startswith('a'):
            return f'c{triples[int(f[1:])][int(g[1:])]}'
        raise AssertionError((f,g))

    pairs = [(f,g) for f in arrows for g in arrows if arrows[g][1]==arrows[f][0]]
    for f,g in pairs:
        fg=compose(f,g)
        assert arrows[fg] == (arrows[g][0],arrows[f][1])
    for f,(a,b) in arrows.items():
        assert compose(f,f'id_{a}') == f
        assert compose(f'id_{b}',f) == f
    triple_count=0
    for f,g in pairs:
        for h in arrows:
            if arrows[h][1] == arrows[g][0]:
                assert compose(f,compose(g,h)) == compose(compose(f,g),h)
                triple_count+=1
    for a in objects:
        assert len([f for f in arrows if arrows[f]==(a,'t')]) == 1
    return {"objects":list(objects),"arrows":arrows,
            "arrow_count":len(arrows),"composable_pairs_checked":len(pairs),
            "associativity_triples_checked":triple_count,
            "identities_verified":True,"terminal_object_verified":"t"}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
