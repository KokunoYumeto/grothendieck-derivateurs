"""Sanity audit of D.11 on naturally labelled posets of size at most four.

Tests all monotone maps to the three-element chain whose required lift
posets reduce to a point by beat-point deletion.  It checks the actual
minimum comma posets in every nonempty target simplex.  Acyclicity here
is an independent finite check, not a substitute for the manuscript's
homotopy-initiality proof.
"""
from fractions import Fraction
from itertools import combinations, product
import json


def rank(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        x = a[r][c]
        a[r] = [v/x for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                x = a[i][c]
                a[i] = [v-x*w for v, w in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def chains(vertices, le):
    result = []
    def visit(prefix):
        if prefix:
            result.append(tuple(prefix))
        for v in vertices:
            if not prefix or (v != prefix[-1] and le(prefix[-1], v)):
                visit(prefix+[v])
    visit([])
    return result


def beat_contractible(vertices, le):
    rest = list(vertices)
    while len(rest) > 1:
        for x in rest:
            lower = [y for y in rest if y != x and le(y, x)]
            upper = [y for y in rest if y != x and le(x, y)]
            lower_max = any(all(le(z, y) for z in lower) for y in lower)
            upper_min = any(all(le(y, z) for z in upper) for y in upper)
            if lower_max or upper_min:
                rest.remove(x)
                break
        else:
            return False
    return len(rest) == 1


def acyclic(vertices, le):
    if not vertices:
        return False
    cs = chains(vertices, le)
    bydim = {}
    for chain in cs:
        bydim.setdefault(len(chain)-1, []).append(chain)
    ranks = {0: 1}
    for dim in range(1, max(bydim)+1):
        lower = {c: i for i, c in enumerate(bydim[dim-1])}
        mat = [[0 for _ in bydim[dim]] for _ in lower]
        for j, c in enumerate(bydim[dim]):
            for k in range(dim+1):
                mat[lower[c[:k]+c[k+1:]]][j] += (-1)**k
        ranks[dim] = rank(mat)
    return all(len(ss) == ranks.get(d, 0)+ranks.get(d+1, 0)
               for d, ss in bydim.items())


counts = {"posets": 0, "monotone_maps": 0, "maps_with_beat_contractible_lifts": 0,
          "nonempty_fibre_cell_posets": 0, "minimum_commas_checked": 0,
          "maximum_comma_objects": 0}
for n in range(1, 5):
    verts = tuple(range(n))
    possible = list(combinations(verts, 2))
    for bits in product([False, True], repeat=len(possible)):
        rel = {(v,v) for v in verts} | {e for e,b in zip(possible,bits) if b}
        if any((a,b) in rel and (b,c) in rel and (a,c) not in rel
               for a,b,c in product(verts, repeat=3)):
            continue
        le = lambda a,b: (a,b) in rel
        counts["posets"] += 1
        pc = chains(verts, le)
        for f in product(range(3), repeat=n):
            if any(le(a,b) and f[a] > f[b] for a,b in product(verts, repeat=2)):
                continue
            counts["monotone_maps"] += 1
            if not all(beat_contractible([r for r in verts if le(p,r) and f[r] == q], le)
                       for p in verts for q in range(f[p],3)):
                continue
            counts["maps_with_beat_contractible_lifts"] += 1
            for size in range(1,4):
                for sigma in combinations(range(3),size):
                    cells = [frozenset(c) for c in pc if tuple(sorted({f[v] for v in c})) == sigma]
                    if cells:
                        counts["nonempty_fibre_cell_posets"] += 1
                    for a,b in product(cells,repeat=2):
                        if a <= b:
                            assert le(min(b), min(a))
                    for p in verts:
                        if f[p] != sigma[0]:
                            continue
                        comma = [c for c in cells if all(le(p,r) for r in c)]
                        assert acyclic(comma, lambda a,b: a <= b), (rel,f,sigma,p,comma)
                        counts["minimum_commas_checked"] += 1
                        counts["maximum_comma_objects"] = max(counts["maximum_comma_objects"],len(comma))
counts["all_assertions_passed"] = True
counts["scope"] = "All naturally labelled posets on 1..4 objects and all monotone maps to [2] having beat-contractible outgoing lift posets."
counts["limitation"] = "Rational acyclicity is a finite sanity check; weak contractibility and canonical initiality are proved by induction in D.11."
print(json.dumps(counts, indent=2, sort_keys=True))
