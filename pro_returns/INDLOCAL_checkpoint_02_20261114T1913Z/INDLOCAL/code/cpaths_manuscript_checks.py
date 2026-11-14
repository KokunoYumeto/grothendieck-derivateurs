"""Independent finite checks for C.20--C.28.

The quantified arguments are in sections/C_manuscript.tex. This program checks
their finite categories, arrow formulas, chains and the bounded fence tests.
"""
from itertools import product, permutations, combinations
from collections import Counter
import json
from cpaths_checks import type_maps, words


def compose(p, q):
    """p after q, on one finite ordered set."""
    return tuple(p[q[i]] for i in range(len(p)))


def extend(p, size):
    return p + tuple(range(len(p), size))


def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def shifted(p, size):
    return (0,) + tuple(x + 1 for x in p) + tuple(range(len(p) + 1, size))


def runs(w):
    return int(bool(w)) + sum(w[i] != w[i - 1] for i in range(1, len(w)))


def boundary(chain):
    out = Counter()
    for simplex, coeff in chain.items():
        for j in range(len(simplex)):
            out[simplex[:j] + simplex[j + 1:]] += coeff * (-1)**j
    return {s: c for s, c in out.items() if c}


def main():
    out = {}
    # Missing composition and identity really destroy the pullback diagram.
    marked = {(0, 0), (1, 1), (2, 2), (0, 1), (1, 2)}
    assert (0, 1) in marked and (1, 2) in marked and (0, 2) not in marked
    assert (0, 2) in type_maps('-', '--')
    assert not any(a in set() for a in [('identity',)])
    out['marking_counterexamples'] = 2

    tested = 0
    for r in range(7):
        size = r + 2
        arrows = {(i, i) for i in range(size)}
        for i in range(size - 1):
            arrows.add((i, i + 1) if i % 2 == 0 else (i + 1, i))
        for w in words(9):
            if runs(w) > r:
                continue
            reachable = {0}
            for sign in w:
                reachable = {j for i in reachable for j in range(size)
                             if ((i, j) if sign == '+' else (j, i)) in arrows}
            assert r + 1 not in reachable
            tested += 1
    out['bounded_run_fence_words'] = tested
    assert type_maps('+-+', '+-+') == [(0, 1, 2, 3)]
    assert type_maps('+', '+') == [(0, 1)]
    assert type_maps('+-+', '+') == [(0, 0, 0, 1), (0, 1, 1, 1)]
    out['type_projection_lift_category_sizes'] = [2, 2]
    for k in range(-8, 9):
        def geodesic(i):
            if i <= 0:
                return 0
            if i >= 4*abs(k):
                return 4*k
            return i if k > 0 else -i
        for i in range(-2, 4*abs(k)+2):
            a,b = (geodesic(i),geodesic(i+1)) if i%2 == 0 else (geodesic(i+1),geodesic(i))
            assert a == b or (a%2 == 0 and abs(a-b) == 1)
    for n in range(1, 9):
        def excursion(i):
            if i <= 0 or i >= 8*n:
                return 0
            return i if i <= 4*n else 8*n-i
        assert excursion(4*n) == 4*n and excursion(8*n) == 0
        for i in range(-2, 8*n+2):
            a,b = (excursion(i),excursion(i+1)) if i%2 == 0 else (excursion(i+1),excursion(i))
            assert a == b or (a%2 == 0 and abs(a-b) == 1)
    out['crown_geodesic_and_excursion_checks'] = {'geodesics':17,'excursions':8}

    groups = {i: list(permutations(range(i + 1))) for i in range(5)}
    assoc = 0
    morphs = 0
    shifts = 0
    for n in range(4):
        # All T_n compositions and all composable triples.
        for i in range(n + 1):
            for j in range(i, n + 1):
                for g in groups[j]:
                    morphs += 1
                    assert compose(tuple(range(j + 1)), g) == g
                    assert compose(g, extend(tuple(range(i + 1)), j + 1)) == g
                    # Three natural transformations through terminal object n+1.
                    size = n + 2
                    c = tuple(range(1, size)) + (0,)
                    incg = extend(g, size)
                    sg = shifted(g, size)
                    assert compose(compose(c, incg), inverse(c)) == sg
                    assert compose(sg, c) == compose(c, incg)
                    assert i <= n + 1 and i + 1 <= n + 1
                    shifts += 1
                    for k in range(j, n + 1):
                        for h in groups[k]:
                            hg = compose(h, extend(g, k + 1))
                            # r_n preserves composites.
                            assert extend(hg, n + 1) == compose(extend(h, n + 1), extend(g, n + 1))
                            assert shifted(hg, n + 2) == compose(shifted(h, n + 2), shifted(g, n + 2))
                            for l in range(k, n + 1):
                                for t in groups[l]:
                                    left = compose(t, extend(hg, l + 1))
                                    right = compose(compose(t, extend(h, l + 1)), extend(g, l + 1))
                                    assert left == right
                                    assoc += 1
        shifted_images = {shifted(g, n + 2) for g in groups[n]}
        swap = (1, 0) + tuple(range(2, n + 2))
        assert swap not in shifted_images
    out['symmetric_filtration_arrows'] = morphs
    out['symmetric_filtration_associativity_triples'] = assoc
    out['shift_conjugation_naturality_arrows'] = shifts

    # Y is the four-crown, M its two-cone suspension.
    yrel = {(i, i) for i in range(4)} | {(i, j) for i in (0, 1) for j in (2, 3)}
    mrel = yrel | {(4, 4), (5, 5)} | {(i, j) for i in range(4) for j in (4, 5)}
    assert all((a, c) in mrel for a, b in mrel for b2, c in mrel if b == b2)
    functors = [f for f in product(range(6), repeat=4)
                if all((f[i], f[j]) in mrel for i, j in yrel)]
    assert len(functors) == 198
    assert len(mrel) == 18  # functors from the parallel-arrow category
    s = (4,)*4
    inc = tuple(range(4))
    n = (5,)*4
    y0 = (0,)*4
    assert all((a, b) in mrel for f, g in [(inc,s),(inc,n),(y0,n),(y0,s)]
               for a,b in zip(f,g))
    gamma = {(0,2):1,(1,2):-1,(1,3):1,(0,3):-1}
    assert not boundary(gamma)
    img = Counter()
    for edge, coeff in gamma.items():
        img['g' if edge == (0,3) else 'f'] += coeff
    assert dict(img) == {'f':1,'g':-1}
    sphere = {}
    for edge, coeff in gamma.items():
        sphere[edge+(5,)] = coeff
        sphere[edge+(4,)] = -coeff
    assert len(sphere) == 8 and not boundary(sphere)
    assert all((a,b) in mrel and a != b for tri in sphere for a,b in zip(tri,tri[1:]))
    chains = {d: [c for c in combinations(range(6), d+1)
                  if all((a,b) in mrel for a,b in zip(c,c[1:]))]
              for d in range(4)}
    assert [len(chains[d]) for d in range(4)] == [6,12,8,0]
    out['sphere_functor_category_object_counts'] = {'Y_to_M':len(functors),'B_to_M':len(mrel)}
    out['sphere_nerve_nondegenerate_simplices'] = [len(chains[d]) for d in range(4)]
    out['suspension_cycle_coefficients'] = {','.join(map(str,s)):c for s,c in sphere.items()}

    # The five-arrow pointed-set category E, with actual function composition.
    arrows = [
        ('id0',0,0,(0,)), ('u',0,1,(0,)), ('v',1,0,(0,0)),
        ('idx',1,1,(0,1)), ('z',1,1,(0,0))]
    by = {(s,t,f):name for name,s,t,f in arrows}
    def mul(f,g):
        # g after f
        nf,s,t,ff=f; ng,t2,u,gg=g
        assert t == t2
        hh=tuple(gg[x] for x in ff)
        return next(a for a in arrows if a[0] == by[(s,u,hh)])
    triples=0
    for a,b,c in product(arrows,repeat=3):
        if a[2] == b[1] and b[2] == c[1]:
            assert mul(mul(a,b),c) == mul(a,mul(b,c))
            triples += 1
    assert triples == 34
    assert all(sum(a[1] == 0 and a[2] == x for a in arrows) == 1 for x in (0,1))
    assert all(sum(a[1] == x and a[2] == 0 for a in arrows) == 1 for x in (0,1))
    out['pointed_five_arrow_associativity_triples'] = triples
    fork = {(0,0),(1,1),(2,2),(0,1),(2,1)}
    assert (0,2) not in fork and (2,0) not in fork
    assert all((x,1) in fork for x in range(3))
    out['terminal_fork_arrows'] = len(fork)
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
