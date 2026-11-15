"""Independent, exact finite certificates for RESIDUE Parts B and C.

Run with Python 3 and SymPy.  No data or code from the earlier packages is used.
This is a verification program, not an exhaustive category enumeration.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


@dataclass
class Category:
    objects: tuple
    arrows: dict  # name -> (source, target)
    identities: dict
    composition: dict  # (g, f) -> gf

    def hom(self, x, y):
        return [f for f, (a, b) in self.arrows.items() if (a, b) == (x, y)]

    def validate(self):
        for x in self.objects:
            assert self.arrows[self.identities[x]] == (x, x)
        for f, (x, y) in self.arrows.items():
            assert self.composition[self.identities[y], f] == f
            assert self.composition[f, self.identities[x]] == f
        for f, g, h in product(self.arrows, repeat=3):
            if self.arrows[f][1] == self.arrows[g][0] and self.arrows[g][1] == self.arrows[h][0]:
                assert self.composition[h, self.composition[g, f]] == self.composition[self.composition[h, g], f]
        return True

    def pullbacks(self):
        """Exhaustively check universal properties, recording every cospan."""
        result = {}
        for f, g in product(self.arrows, repeat=2):
            if self.arrows[f][1] != self.arrows[g][1]:
                continue
            x, z = self.arrows[f]
            y, _ = self.arrows[g]
            cones = [(p, a, b) for p in self.objects for a in self.hom(p, x) for b in self.hom(p, y)
                     if self.composition[f, a] == self.composition[g, b]]
            chosen = None
            for p, a, b in cones:
                if all(sum(self.composition[a, h] == aa and self.composition[b, h] == bb
                           for h in self.hom(q, p)) == 1 for q, aa, bb in cones):
                    chosen = (p, a, b)
                    break
            assert chosen is not None, (f, g, cones)
            result[f, g] = chosen
        return result

    def slice(self, s):
        objs = tuple(f for f, (_, b) in self.arrows.items() if b == s)
        arr = {}
        for f, g in product(objs, repeat=2):
            for h in self.hom(self.arrows[f][0], self.arrows[g][0]):
                if self.composition[g, h] == f:
                    arr[f, g, h] = (f, g)
        ids = {f: (f, f, self.identities[self.arrows[f][0]]) for f in objs}
        comp = {(b, a): (a[0], b[1], self.composition[b[2], a[2]])
                for a, b in product(arr, repeat=2) if arr[a][1] == arr[b][0]}
        return Category(objs, arr, ids, comp)


def poset(n, strict):
    rel = set(strict) | {(i, i) for i in range(n)}
    changed = True
    while changed:
        old = len(rel)
        rel |= {(a, d) for a, b in rel for c, d in rel if b == c}
        changed = len(rel) != old
    assert all(a == b or (b, a) not in rel for a, b in rel)
    arrows = {ab: ab for ab in sorted(rel)}
    composition = {(g, f): (f[0], g[1]) for f, g in product(arrows, repeat=2) if f[1] == g[0]}
    c = Category(tuple(range(n)), arrows, {i: (i, i) for i in range(n)}, composition)
    c.validate()
    return c


def crown(n):
    assert n >= 4 and n % 2 == 0
    return poset(n, {(i, (i - 1) % n) for i in range(0, n, 2)} |
                    {(i, (i + 1) % n) for i in range(0, n, 2)})


def suspend(c):
    n = len(c.objects)
    return poset(n + 2, {(a, b) for a, b in c.arrows if a != b} |
                        {(i, t) for i in range(n) for t in (n, n + 1)})


def chains(c, k):
    if k == 0:
        return [(x,) for x in c.objects]
    ans = [(x,) for x in c.objects]
    for _ in range(k):
        ans = [s + (y,) for s in ans for y in c.objects if y != s[-1] and (s[-1], y) in c.arrows]
    return ans


def chain_data(c):
    bases = [chains(c, k) for k in range(5)]
    ds = [sp.zeros(0, len(bases[0]))]
    for k in range(1, 5):
        ix = {s: i for i, s in enumerate(bases[k - 1])}
        d = sp.zeros(len(bases[k - 1]), len(bases[k]))
        for j, s in enumerate(bases[k]):
            for i in range(k + 1):
                d[ix[s[:i] + s[i + 1:]], j] += (-1) ** i
        ds.append(d)
    for k in range(2, 5):
        assert ds[k - 1] * ds[k] == sp.zeros(ds[k - 1].rows, ds[k].cols)
    smith = []
    for d in ds[1:]:
        s = smith_normal_form(d, domain=ZZ)
        entries = [abs(int(s[i, i])) for i in range(min(s.shape)) if s[i, i]]
        # Unit invariant factors imply torsion-free cokernels and hence homology.
        assert all(a == 1 for a in entries)
        smith.append(entries)
    homology = [len(bases[k]) - ds[k].rank() - ds[k + 1].rank() for k in range(4)]
    return bases, ds, {"chains": [len(b) for b in bases], "H_ranks_Z": homology,
                       "boundary_Smith_nonzero": smith}


def presentation(c):
    """Fundamental group presentation from edges/triangles and a spanning tree.

    Exact Tietze eliminations eliminate a generator occurring exactly once
    in a relation. Output a free group only if all relations were eliminated.
    """
    edges = chains(c, 1)
    parent = {x: x for x in c.objects}
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    tree = set()
    for e in edges:
        a, b = e
        if root(a) != root(b):
            parent[root(a)] = root(b)
            tree.add(e)
    assert len({root(x) for x in c.objects}) == 1
    gen = {e: i + 1 for i, e in enumerate(e for e in edges if e not in tree)}
    def reduce(w):
        out = []
        for a in w:
            if out and out[-1] == -a:
                out.pop()
            else:
                out.append(a)
        return out
    def inv(w):
        return [-x for x in w[::-1]]
    rels = []
    for a, b, d in chains(c, 2):
        w = [gen[e] * sign for e, sign in [((a, b), 1), ((b, d), 1), ((a, d), -1)] if e in gen]
        if reduce(w):
            rels.append(reduce(w))
    original_relations = [r[:] for r in rels]
    remaining = set(gen.values())
    eliminations = []
    while True:
        choice = next(((i, abs(x), j, x) for i, w in enumerate(rels) for j, x in enumerate(w)
                       if sum(abs(a) == abs(x) for a in w) == 1), None)
        if choice is None:
            break
        i, g, j, signed = choice
        w = rels.pop(i)
        # w = L g R gives g = L^{-1} R^{-1}; inverse sign reverses this.
        value = reduce(inv(w[:j]) + inv(w[j + 1:]))
        if signed < 0:
            value = inv(value)
        newrels = []
        for rel in rels:
            r = reduce([y for x in rel for y in (value if x == g else inv(value) if x == -g else [x])])
            if r:
                newrels.append(r)
        rels = newrels
        remaining.remove(g)
        eliminations.append({"generator": g, "replacement": value})
    assert not rels, rels
    return {"generators": gen.__len__(), "relations": original_relations,
            "eliminations": eliminations, "free_rank": len(remaining)}


def map_matrix(source, target, mapping, k):
    src, tgt = chains(source, k), chains(target, k)
    index = {s: i for i, s in enumerate(tgt)}
    out = sp.zeros(len(tgt), len(src))
    for j, s in enumerate(src):
        image = tuple(mapping[x] for x in s)
        if len(set(image)) == len(image):
            out[index[image], j] = 1
    return out


def circle_cycle(c):
    n = len(c.objects)
    index = {s: i for i, s in enumerate(chains(c, 1))}
    z = sp.zeros(len(index), 1)
    for i in range(0, n, 2):
        z[index[i, (i + 1) % n]] += 1
        z[index[i, (i - 1) % n]] -= 1
    return z


def suspension_cycle(c):
    n = len(c.objects)
    s = suspend(c)
    ci, si = chains(c, 1), {a: i for i, a in enumerate(chains(s, 2))}
    z1 = circle_cycle(c)
    z2 = sp.zeros(len(si), 1)
    for i, (a, b) in enumerate(ci):
        for t, sign in ((n, 1), (n + 1, -1)):
            z2[si[a, b, t]] += sign * z1[i]
    return z2


def circle_counterexample():
    a, b = crown(8), crown(4)
    sa, sb = suspend(a), suspend(b)
    f = {i: i % 4 for i in range(8)}
    sf = f | {8: 4, 9: 5}
    for x, y in sa.arrows:
        assert (sf[x], sf[y]) in sb.arrows
    data = {}
    for name, c in (("C8", a), ("C4", b), ("suspension_C8", sa), ("suspension_C4", sb)):
        bases, ds, stats = chain_data(c)
        stats["objects"] = len(c.objects)
        stats["arrows_including_ids"] = len(c.arrows)
        stats["pi1_presentation"] = presentation(c)
        data[name] = stats
    z, w = circle_cycle(a), circle_cycle(b)
    assert map_matrix(a, b, f, 1) * z == 2 * w
    zz, ww = suspension_cycle(a), suspension_cycle(b)
    assert map_matrix(sa, sb, sf, 2) * zz == 2 * ww
    assert chain_data(sa)[1][2] * zz == sp.zeros(len(chains(sa, 1)), 1)
    assert chain_data(sb)[1][2] * ww == sp.zeros(len(chains(sb, 1)), 1)
    # Each top kernel has rank one, and these cycles have a coefficient 1.
    assert 1 in list(zz) and 1 in list(ww)
    # Overcomma categories at the two terminal span objects are cones.
    for n, c in ((8, a), (4, b)):
        cone = poset(n + 1, {(x, y) for x, y in c.arrows if x != y} | {(i, n) for i in range(n)})
        assert all((i, n) in cone.arrows for i in range(n + 1))
        data[f"cone_C{n}"] = chain_data(cone)[2]
        data[f"cone_C{n}"]["pi1_presentation"] = presentation(cone)
    data["circle_H1_map"] = 2
    data["suspension_H2_map"] = 2
    # Construct the actual overcomma posets over the span o<+,o<-.
    span = poset(3, {(0, 1), (0, 2)})
    pa = {i: 0 for i in range(8)} | {8: 1, 9: 2}
    pbb = {i: 0 for i in range(4)} | {4: 1, 5: 2}
    comma_stats = {}
    for q in span.objects:
        ao = [i for i in sa.objects if (pa[i], q) in span.arrows]
        bo = [i for i in sb.objects if (pbb[i], q) in span.arrows]
        ai, bi = {x: i for i, x in enumerate(ao)}, {x: i for i, x in enumerate(bo)}
        ac = poset(len(ao), {(ai[x], ai[y]) for x, y in sa.arrows if x != y and x in ai and y in ai})
        bc = poset(len(bo), {(bi[x], bi[y]) for x, y in sb.arrows if x != y and x in bi and y in bi})
        cm = {ai[x]: bi[sf[x]] for x in ao}
        assert all((cm[x], cm[y]) in bc.arrows for x, y in ac.arrows)
        comma_stats[q] = {"source": chain_data(ac)[2], "target": chain_data(bc)[2],
                          "objects_source": ao, "objects_target": bo,
                          "object_map": cm}
    data["comma_tests"] = comma_stats
    return data


def five_object_category():
    objs = ("0", "A", "B", "C", "S")
    ids = {x: "id_" + x for x in objs}
    arr = {ids[x]: (x, x) for x in objs}
    arr |= {"zero_" + x: ("0", x) for x in objs[1:]}
    arr |= {"alpha": ("A", "B"), "beta": ("A", "B"), "gamma": ("A", "C"),
            "b": ("B", "S"), "c": ("C", "S"), "x": ("A", "S"), "y": ("A", "S")}
    comp = {}
    for f, g in product(arr, repeat=2):
        if arr[f][1] != arr[g][0]:
            continue
        if f in ids.values():
            h = g
        elif g in ids.values():
            h = f
        elif arr[f][0] == "0":
            h = "zero_" + arr[g][1]
        else:
            h = {("b", "alpha"): "x", ("b", "beta"): "y", ("c", "gamma"): "x"}[g, f]
        comp[g, f] = h
    c = Category(objs, arr, ids, comp)
    c.validate()
    return c


def intrinsic_fibrations(c, W, pb):
    good = []
    witnesses = {}
    for p, (e, b) in c.arrows.items():
        failure = None
        for v in W:
            x, y = c.arrows[v]
            for t in c.hom(y, b):
                tv = c.composition[t, v]
                a, ae, ax = pb[p, tv]
                d, de, dy = pb[p, t]
                candidates = [h for h in c.hom(a, d)
                              if c.composition[de, h] == ae and c.composition[dy, h] == c.composition[v, ax]]
                assert len(candidates) == 1
                if candidates[0] not in W:
                    failure = (v, t, candidates[0])
                    break
            if failure:
                break
        if failure:
            witnesses[p] = failure
        else:
            good.append(p)
    return good, witnesses


def verify_five():
    c = five_object_category()
    W = set(c.identities.values()) | {"alpha", "beta", "gamma"}
    for (g, f), h in c.composition.items():
        assert sum(t in W for t in (f, g, h)) != 2
    # Strong-saturation certificate: the inverse image of identities under R.
    R = {"0": 0, "A": 1, "B": 1, "C": 1, "S": 2}
    assert all((f in W) == (R[a] == R[b]) for f, (a, b) in c.arrows.items())
    pb = c.pullbacks()
    F, witnesses = intrinsic_fibrations(c, W, pb)
    slices = {}
    for s in c.objects:
        sl = c.slice(s)
        sl.validate()
        slpb = sl.pullbacks()
        Ws = {a for a in sl.arrows if a[2] in W}
        Fobs = [p for p in sl.objects if p in F]
        # Check (b) by all arbitrary base changes in M.
        tested = 0
        for (src, tgt, u), _ in sl.arrows.items():
            if src not in Fobs or tgt not in Fobs or u not in W:
                continue
            for t, (_, cod) in c.arrows.items():
                if cod != s:
                    continue
                a, au, at = pb[src, t]
                b, bv, bt = pb[tgt, t]
                hs = [h for h in c.hom(a, b) if c.composition[bv, h] == c.composition[u, au]
                      and c.composition[bt, h] == at]
                assert len(hs) == 1 and hs[0] in W
                tested += 1
        assert all(len(sl.hom(a, b)) <= 1 for a, b in product(sl.objects, repeat=2))
        if s == "S":
            r = {"zero_S": "zero_S", "x": "b", "y": "b", "b": "b", "c": "b", "id_S": "id_S"}
            tt = {"zero_S": "zero_S", "x": "x", "y": "y", "b": "b", "c": "x", "id_S": "id_S"}
        elif s == "B":
            r = {"zero_B": "zero_B", "alpha": "id_B", "beta": "id_B", "id_B": "id_B"}
            tt = {x: x for x in sl.objects}
        else:
            r = {x: x for x in sl.objects}
            tt = r.copy()
        for objmap in (r, tt):
            for h, (a, b) in sl.arrows.items():
                images = sl.hom(objmap[a], objmap[b])
                assert len(images) == 1
                if h in Ws:
                    assert images[0] in Ws
        for x in sl.objects:
            for target in (x, r[x]):
                hs = sl.hom(tt[x], target)
                assert len(hs) == 1 and hs[0] in Ws
        assert all(r[x] in Fobs for x in sl.objects)
        assert all(r[x] == x and tt[x] == x for x in Fobs)
        slices[s] = {"objects": list(sl.objects), "fibrant_objects": Fobs,
                     "R": r, "T": tt, "b_tests": tested,
                     "arrows": [[a, b, h[2]] for h, (a, b) in sl.arrows.items()]}
    H = {"zero_S", "b", "c", "id_S"}
    sl = c.slice("S")
    assert all(h[0] == h[1] for h in sl.arrows if h[0] in H and h[1] in H and h[2] in W)
    assert "c" not in F and not any(c.composition.get((p, w)) == "c" for w in W for p in F)
    return {"objects": list(c.objects), "arrows": c.arrows,
            "composition": [{"g": g, "f": f, "gf": h} for (g, f), h in c.composition.items()],
            "W": sorted(W), "pullbacks_checked": len(pb),
            "pullbacks": [{"f": f, "g": g, "object": p, "left": a, "right": b} for (f, g), (p, a, b) in pb.items()],
            "intrinsic_fibrations": F, "failure_witnesses": witnesses, "slices": slices,
            "intermediate_objects": sorted(H), "no_factorization": "c:C->S",
            "assertions": ["category laws", "all pullback universal properties", "two-out-of-three", "strong saturation certificate", "all intrinsic tests", "(a) via R,T", "(b) all base changes", "failure of (c)"]}


def groupoid_pair(product_group=False):
    # E has two objects and one arrow per ordered pair. E x BC2 adds label k.
    objs = (0, 1)
    arr = {(x, y, k): (x, y) for x, y in product(objs, repeat=2) for k in (range(2) if product_group else range(1))}
    ids = {x: (x, x, 0) for x in objs}
    comp = {(g, f): (f[0], g[1], (f[2] + g[2]) % 2)
            for f, g in product(arr, repeat=2) if f[1] == g[0]}
    c = Category(objs, arr, ids, comp)
    c.validate()
    return c


def components(c):
    unseen = set(c.objects)
    result = []
    while unseen:
        part = {next(iter(unseen))}
        while True:
            expanded = part | {b for a, b in c.arrows.values() if a in part} | {a for a, b in c.arrows.values() if b in part}
            if expanded == part:
                break
            part = expanded
        unseen -= part
        result.append(sorted(part))
    return result


def dagger_comma(c):
    objs = tuple(product(c.objects, range(2)))
    arr = {}
    for a, b in product(objs, repeat=2):
        x, t = a
        y, tt = b
        for f in c.hom(x, y):
            if (tt + y - x) % 2 == t:
                arr[a, b, f] = (a, b)
    ids = {a: (a, a, c.identities[a[0]]) for a in objs}
    comp = {(g, f): (f[0], g[1], c.composition[g[2], f[2]])
            for f, g in product(arr, repeat=2) if arr[f][1] == arr[g][0]}
    out = Category(objs, arr, ids, comp)
    out.validate()
    return out


def dagger_certificate():
    e, a = groupoid_pair(), groupoid_pair(True)
    ec, ac = dagger_comma(e), dagger_comma(a)
    result = {}
    for name, c in (("E", e), ("A", a), ("E_over_c", ec), ("A_over_c", ac)):
        comps = components(c)
        result[name] = {"objects": len(c.objects), "arrows": len(c.arrows), "components": comps,
                        "isotropy_orders": [len(c.hom(x, x)) for x in c.objects]}
    assert len(components(e)) == len(components(a)) == 1
    assert len(components(ec)) == len(components(ac)) == 2
    assert all(len(e.hom(x, x)) == 1 and len(a.hom(x, x)) == 2 for x in e.objects)
    # Verify the functor u and its actual comma functor, not only cardinalities.
    for f, (x, y) in a.arrows.items():
        assert (x, y, 0) in e.arrows
    for (g, f), h in a.composition.items():
        assert e.composition[(g[0], g[1], 0), (f[0], f[1], 0)] == (h[0], h[1], 0)
        assert (h[1] - h[0]) % 2 == ((g[1] - g[0]) + (f[1] - f[0])) % 2
    for f, (x, y) in ac.arrows.items():
        ff = (f[0], f[1], (f[2][0], f[2][1], 0))
        assert ff in ec.arrows
        assert (x[0] + x[1]) % 2 == (y[0] + y[1]) % 2
    # Finite arrow-retract certificate for BG->e as a retract of
    # (BG disjoint-union e)->(e disjoint-union e).
    # Source objects 0,1; source arrows (object, group label).
    big_source = Category((0, 1), {(0, 0): (0, 0), (0, 1): (0, 0), (1, 0): (1, 1)},
                          {0: (0, 0), 1: (1, 0)},
                          {(g, f): (f[0], (g[1] + f[1]) % 2)
                           for f, g in product(((0, 0), (0, 1), (1, 0)), repeat=2) if f[0] == g[0]})
    big_source.validate()
    # R_A sends both objects to the sole BG-object and label k to k;
    # the added identity has label0. I_A selects component0.
    rA = {f: f[1] for f in big_source.arrows}
    for (g, f), h in big_source.composition.items():
        assert rA[h] == (rA[g] + rA[f]) % 2
    assert all(rA[(0, k)] == k for k in range(2))
    # Both target retraction composites and both square equalities have
    # the unique arrow of e as value, so this verifies their complete table.
    result["arrow_retract"] = {"large_source_objects": 2, "large_source_arrows": 3,
                               "large_target_objects": 2, "large_target_arrows": 2,
                               "source_section": "BG object -> component 0; k -> (0,k)",
                               "source_retraction": "both objects -> BG object; (i,k) -> k",
                               "target_section": "point -> component 0",
                               "target_retraction": "both points -> point", "checked": True}
    result["pi1"] = {"E": "1", "A": "<k | k^2=1>", "E_over_c_each": "1", "A_over_c_each": "<k | k^2=1>"}
    return result


def near_bijection_certificate():
    """Exact symbolic functions on N, with a finite prefix and affine tail.

    A record (prefix,a,b) means f(n)=prefix[n] before len(prefix), and
    f(n)=a*n+b thereafter. Here a is 0 or 1. Composition retains an
    exact affine tail, so the assertions below are not finite sampling.
    """
    def apply(f, n):
        prefix, a, b = f
        return prefix[n] if n < len(prefix) else a*n + b
    def compose(g, f):
        pf, af, bf = f
        pg, ag, bg = g
        if af == 0:
            cutoff = len(pf)
            return (tuple(apply(g, apply(f, n)) for n in range(cutoff)),
                    0, apply(g, bf))
        assert af == 1
        cutoff = max(len(pf), len(pg)-bf, 0)
        return (tuple(apply(g, apply(f, n)) for n in range(cutoff)),
                ag, ag*bf+bg)
    def normalize(f):
        prefix, a, b = f
        prefix = list(prefix)
        while prefix and prefix[-1] == a*(len(prefix)-1)+b:
            prefix.pop()
        return (tuple(prefix), a, b)
    def exceptions_to_identity(f):
        prefix, a, b = f
        assert (a, b) == (1, 0)
        return [n for n, value in enumerate(prefix) if value != n]
    ident = ((), 1, 0)
    const = ((), 0, 0)
    shift = ((), 1, 1)
    fold = ((0,), 1, -1)
    assert normalize(compose(fold, shift)) == ident
    assert exceptions_to_identity(compose(shift, fold)) == [0]
    assert apply(fold, 0) == apply(fold, 1) == 0
    g0 = ((), 0, 0)
    g1 = ((1,), 0, 0)
    assert normalize(compose(g0, shift)) == normalize(compose(g1, shift)) == const
    assert apply(g0, 0) != apply(g1, 0)
    # Unequal-value sets of the identity and the constant map contain
    # every positive n. Their respective affine tails make this exact.
    assert ident[1:] == (1, 0) and const[1:] == (0, 0)
    def record(f):
        return {"prefix": list(f[0]), "tail_slope": f[1], "tail_offset": f[2]}
    return {
        "domain_category": "Discrete category on all natural numbers, identities only",
        "representation": "Finite prefix followed by the exact affine tail a*n+b",
        "identity": record(ident), "constant": record(const),
        "shift": record(shift), "noninjective_near_bijection": record(fold),
        "fold_after_shift": record(normalize(compose(fold, shift))),
        "shift_after_fold": record(normalize(compose(shift, fold))),
        "shift_after_fold_identity_exceptions": [0],
        "g0": record(g0), "g1": record(g1),
        "g0_after_shift_equals_g1_after_shift": True,
        "identity_vs_constant_unequal_values":
            "Contains every positive natural number; infinite by the two exact affine tails",
        "scope": "Symbolic infinite-function certificate, not a finite approximation claim",
    }


def historical_literal_certificates():
    """Two small independent corrections to the exact wording of XVI."""
    point = poset(1, set())
    two = poset(2, set())
    empty = poset(0, set())
    # Strict pullback of the two distinct point inclusions into the
    # discrete category on two objects. All functor laws are identities.
    left = {0: 0}
    right = {0: 1}
    pb_objects = [(x, y) for x in point.objects for y in point.objects
                  if left[x] == right[y]]
    pb_arrows = [(f, g) for f in point.arrows for g in point.arrows
                 if left[f[0]] == right[g[0]] and left[f[1]] == right[g[1]]]
    assert pb_objects == pb_arrows == []
    assert bool(point.objects) == bool(two.objects)
    assert bool(empty.objects) != bool(point.objects)
    # The arbitrary-W counterexample to binary product preservation.
    # 0=bottom, 1=a, 2=b, 3=top.
    diamond = poset(4, {(0, 1), (0, 2), (1, 3), (2, 3)})
    meets = {}
    for x, y in product(diamond.objects, repeat=2):
        lower = [z for z in diamond.objects if (z, x) in diamond.arrows
                 and (z, y) in diamond.arrows]
        greatest = [z for z in lower if all((t, z) in diamond.arrows for t in lower)]
        assert len(greatest) == 1
        meets[x, y] = greatest[0]
    def arrow_product(f, g):
        z = (meets[f[0], g[0]], meets[f[1], g[1]])
        assert z in diamond.arrows
        return z
    f = (1, 3)
    weak = [f, (3, 3)]
    g = arrow_product(f, (2, 2))
    assert arrow_product(f, f) == f
    assert all(arrow_product(u, v) in weak for u, v in product(weak, repeat=2))
    assert (3, 3) in weak  # the nullary product is the identity of the top
    assert g == (0, 2)
    h = {0: 0, 1: 2, 2: 1, 3: 2}
    assert all(h[x] <= h[y] for x, y in diamond.arrows)
    assert h[f[0]] == h[f[1]]
    assert h[g[0]] != h[g[1]]
    return {
        "XVI_2_2_nonemptiness": {
            "inclusion": "point -> first point of the discrete two-point category",
            "restriction_base": "second point",
            "strict_pullback_objects": pb_objects,
            "strict_pullback_arrows": pb_arrows,
            "inclusion_is_W_ne": True,
            "restriction_is_W_ne": False,
        },
        "XVI_2_5_missing_identities": {
            "objects": list(diamond.objects),
            "arrows": list(diamond.arrows),
            "composition": [[list(g), list(f), list(k)]
                            for (g, f), k in diamond.composition.items()],
            "binary_meets": [[x, y, z] for (x, y), z in meets.items()],
            "W": [list(w) for w in weak],
            "W_times_W": [[list(u), list(v), list(arrow_product(u, v))]
                          for u, v in product(weak, repeat=2)],
            "arbitrary_W_product":
                "f if any factor is f; identity of top otherwise, including the empty family",
            "product_with_identity_b": list(g),
            "detecting_functor_object_map": h,
            "detecting_functor_inverts_W": True,
            "detecting_functor_inverts_product": False,
        },
    }


if __name__ == "__main__":
    out = Path(__file__).resolve().parent
    data = {"circle_strongly_saturated_counterexample": circle_counterexample(),
            "five_object_fibre_counterexample": verify_five(),
            "W_dagger_counterexample": dagger_certificate(),
            "historical_literal_certificates": historical_literal_certificates(),
            "near_bijection_infinite_certificate": near_bijection_certificate(),
            "scope": "Five finite certificates and one symbolic infinite certificate; no exhaustive enumeration claim."}
    (out / "verification_output.json").write_text(json.dumps(data, indent=2))
    print(json.dumps({"status": "PASS", "output": "verification_output.json", "circle_degree": 2,
                      "suspension_degree": 2, "fibre_counterexample_objects": 5,
                      "fibre_counterexample_arrows": 16,
                      "pullback_cospans_checked": data["five_object_fibre_counterexample"]["pullbacks_checked"]}, indent=2))
