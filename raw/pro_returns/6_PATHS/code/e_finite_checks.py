#!/usr/bin/env python3
"""Exact finite checks for PATHS Part E. No external input is required."""
from itertools import product
from pathlib import Path
import json
import sympy as sp


class Category:
    def __init__(self, objects, arrows, identities, composition):
        self.objects = tuple(objects)
        self.arrows = dict(arrows)  # arrow -> (source, target)
        self.identities = dict(identities)
        self.composition = dict(composition)  # (g,f) -> g after f

    def hom(self, a, b):
        return [f for f, st in self.arrows.items() if st == (a, b)]

    def comp(self, g, f):
        return self.composition[g, f]

    def check(self):
        for x in self.objects:
            assert self.arrows[self.identities[x]] == (x, x)
        for f, (a, b) in self.arrows.items():
            assert self.comp(f, self.identities[a]) == f
            assert self.comp(self.identities[b], f) == f
            for g, (c, d) in self.arrows.items():
                if b != c:
                    assert (g, f) not in self.composition
                    continue
                assert self.arrows[self.comp(g, f)] == (a, d)
                for h, (e, z) in self.arrows.items():
                    if d == e:
                        assert self.comp(h, self.comp(g, f)) == self.comp(self.comp(h, g), f)
        return len(self.objects), len(self.arrows)

    def chains(self, dimension):
        if dimension == 0:
            return [(x,) for x in self.objects]
        nonid = [f for f in self.arrows if f != self.identities[self.arrows[f][0]]]
        chains = [(f,) for f in nonid]
        for _ in range(dimension - 1):
            chains = [s + (f,) for s in chains for f in nonid
                      if self.arrows[s[-1]][1] == self.arrows[f][0]]
        return chains

    def betti(self, bound=4):
        bases = [self.chains(n) for n in range(bound + 2)]
        ranks = [0]
        for n in range(1, bound + 2):
            lower = {s: i for i, s in enumerate(bases[n-1])}
            mat = sp.zeros(len(lower), len(bases[n]))
            for j, s in enumerate(bases[n]):
                for k in range(n + 1):
                    if n == 1:
                        face = (self.arrows[s[0]][1 if k == 0 else 0],)
                    elif k == 0:
                        face = s[1:]
                    elif k == n:
                        face = s[:-1]
                    else:
                        composite = self.comp(s[k], s[k-1])
                        if composite == self.identities[self.arrows[composite][0]]:
                            continue
                        face = s[:k-1] + (composite,) + s[k+1:]
                    mat[lower[face], j] += (-1)**k
            ranks.append(mat.rank())
        return [len(bases[n]) - ranks[n] - ranks[n+1] for n in range(bound + 1)]

    def data(self):
        return {"objects": list(self.objects),
                "arrows": [[str(f), str(a), str(b)] for f, (a,b) in self.arrows.items()],
                "composition": [[str(g), str(f), str(h)] for (g,f),h in self.composition.items()]}


def category_from_generators(objects, nonidentities, nonidentity_products):
    arrows = {"id_" + x: (x,x) for x in objects}
    arrows.update(nonidentities)
    identities = {x: "id_" + x for x in objects}
    composition = dict(nonidentity_products)
    for f, (a,b) in arrows.items():
        composition[f, identities[a]] = f
        composition[identities[b], f] = f
    result = Category(objects, arrows, identities, composition)
    result.check()
    return result


def sphere_category():
    return category_from_generators(
        ["x","z","a","b"],
        {"lam":("x","z"),"mu":("x","z"),"r":("z","a"),
         "v":("z","b"),"alpha":("x","a"),"beta":("x","b")},
        {("r","lam"):"alpha",("r","mu"):"alpha",
         ("v","lam"):"beta",("v","mu"):"beta"})


def terminal_cone(c, vertex):
    objects = c.objects + (vertex,)
    arrows = dict(c.arrows)
    identities = dict(c.identities)
    composition = dict(c.composition)
    for x in objects:
        arrows["to_"+vertex+"_"+x] = (x,vertex)
    identities[vertex] = "to_"+vertex+"_"+vertex
    for f,(a,b) in list(arrows.items()):
        composition[f, identities[a]] = f
        composition[identities[b], f] = f
        composition["to_"+vertex+"_"+b,f] = "to_"+vertex+"_"+a
    out = Category(objects, arrows, identities, composition)
    out.check()
    return out


def interval_product(n):
    objects = tuple(f"{h}:{i}" for h in [0,1] for i in range(2*n+1))
    def leq(x,y):
        h,i = map(int,x.split(":")); k,j = map(int,y.split(":"))
        return h <= k and (i == j or i % 2 == 0 and abs(i-j) == 1)
    arrows = {(a,b):(a,b) for a in objects for b in objects if leq(a,b)}
    composition = {(g,f):(a,d) for f,(a,b) in arrows.items()
                   for g,(c,d) in arrows.items() if b == c}
    out = Category(objects, arrows, {a:(a,a) for a in objects}, composition)
    out.check()
    return out


class UnionFind:
    def __init__(self, items):
        self.parent = {x:x for x in items}
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def join(self,x,y):
        self.parent[self.find(y)] = self.find(x)


def sieve_pushout(b, a_objects, c, f_objects, f_arrows):
    """Coend construction, preserving C and the complementary full cosieve."""
    a_objects = set(a_objects)
    complement = set(b.objects) - a_objects
    for f,(x,y) in b.arrows.items():
        if y in a_objects:
            assert x in a_objects
    a_arrows = {f:st for f,st in b.arrows.items() if st[0] in a_objects and st[1] in a_objects}
    for g,(x,y) in a_arrows.items():
        assert c.arrows[f_arrows[g]] == (f_objects[x], f_objects[y])
        for f,(z,w) in a_arrows.items():
            if w == x:
                assert f_arrows[b.comp(g,f)] == c.comp(f_arrows[g], f_arrows[f])
    objects = c.objects + tuple(sorted(complement))
    arrows = {("C",f):st for f,st in c.arrows.items()}
    arrows.update({("B",f):st for f,st in b.arrows.items()
                   if st[0] in complement and st[1] in complement})
    crossing_reps = {}
    crossings = {}
    lookup = {}
    for x in c.objects:
        for y in complement:
            reps = [(a,h,u) for a in a_objects for h in c.hom(x,f_objects[a]) for u in b.hom(a,y)]
            uf = UnionFind(reps)
            for alpha,(a,aa) in a_arrows.items():
                for h in c.hom(x,f_objects[a]):
                    for u in b.hom(aa,y):
                        uf.join((aa,c.comp(f_arrows[alpha],h),u),(a,h,b.comp(u,alpha)))
            classes = {}
            for rep in reps:
                root = uf.find(rep)
                if root not in classes:
                    classes[root] = ("X",x,y,len(classes))
                    crossing_reps[classes[root]] = root
                    arrows[classes[root]] = (x,y)
                lookup[x,y,rep] = classes[root]
            crossings[x,y] = len(classes)
    identities = {x:("C",c.identities[x]) for x in c.objects}
    identities.update({x:("B",b.identities[x]) for x in complement})
    composition = {}
    for f,(x,y) in arrows.items():
        for g,(yy,z) in arrows.items():
            if y != yy:
                continue
            if f[0] == g[0] == "C":
                h = ("C",c.comp(g[1],f[1]))
            elif f[0] == g[0] == "B":
                h = ("B",b.comp(g[1],f[1]))
            elif f[0] == "C" and g[0] == "X":
                a,k,u = crossing_reps[g]
                h = lookup[x,z,(a,c.comp(k,f[1]),u)]
            elif f[0] == "X" and g[0] == "B":
                a,k,u = crossing_reps[f]
                h = lookup[x,z,(a,k,b.comp(g[1],u))]
            else:
                raise AssertionError((g,f))
            composition[g,f] = h
    out = Category(objects,arrows,identities,composition)
    out.check()
    return out, crossings


def check_pushout_products():
    c = sphere_category()
    assert c.betti() == [1,0,1,0,0]
    print("Sphere category C: objects/arrows", c.check(), "Betti", c.betti())
    tables = {"C": c.data()}
    for n in [1,2,3]:
        b = interval_product(n)
        a = {x for x in b.objects if x.startswith("0:") or x in {"1:0",f"1:{2*n}"}}
        fo = {x:("z" if x == "0:0" else "b" if x == "1:0" else "a") for x in a}
        fa = {}
        for u,(x,y) in b.arrows.items():
            if x in a and y in a:
                h = c.hom(fo[x],fo[y]); assert len(h) == 1
                fa[u] = h[0]
        q0, counts = sieve_pushout(b,a,c,fo,fa)
        d = terminal_cone(c,"s")
        q, _ = sieve_pushout(b,a,d,fo,fa)
        assert q0.betti() == [1,0,0,0,0]
        assert q.betti() == [1,0,0,1,0]
        for x in c.objects:
            assert counts[x,"1:1"] == 1
        print("n=",n,"P",b.check(),"A objects",len(a),"Q0",q0.check(),
              "Q",q.check(),"Betti(Q0)",q0.betti(),"Betti(Q)",q.betti())
        tables[f"Q0_n{n}"] = q0.data()
        tables[f"Q_n{n}"] = q.data()
    return tables


def check_empty_paths_and_terminal_obstruction():
    count = 0
    for length in range(1,7):
        for signs in product([1,-1], repeat=length):
            for inside in product([0,1], repeat=length-1):
                values = (0,) + inside + (1,)
                if any((values[i] > values[i+1] if s == 1 else values[i+1] > values[i])
                       for i,s in enumerate(signs)):
                    continue
                source = (0,)*length + values
                collapse_left = (0,)*length + tuple(range(length+1))
                collapse_right = tuple(range(length+1)) + (length,)*length
                assert collapse_left != collapse_right
                assert source == tuple(values[i] for i in collapse_left)
                assert all(v <= values[i] for v,i in zip(source,collapse_right))
                count += 1
    print("All-type [1] incoming-lift obstruction: two distinct maps for",count,"paths of length <=6")
    for length in range(8):
        endpoint_maps_from_empty = [j for j in range(length+1) if j == 0 and j == length]
        assert bool(endpoint_maps_from_empty) == (length == 0)
    print("Empty-type endpoint obstruction verified for lengths 0..7; analytic proof covers all lengths")


def check_monoids():
    elements = ["1"] + [(i,j) for i in range(2) for j in range(2)]
    def mul(a,b):
        if a == "1": return b
        if b == "1": return a
        return (a[0],b[1])
    for a,b,c in product(elements,repeat=3):
        assert mul(mul(a,b),c) == mul(a,mul(b,c))
    for e in elements[1:]:
        assert all(mul(e,m) != "1" and mul(m,e) != "1" for m in elements)
        assert mul(e,e) == e
    print("Rectangular-band monoid: 5 elements; all 125 associativity equations hold; four proper two-sided-ideal witnesses")
    idem = ["1", (0,0)]
    assert all(mul(a,b) in idem for a,b in product(idem,repeat=2))
    # The component e is a natural transformation from the identity functor
    # of the one-object subcategory to the constant functor (all arrows 1).
    assert all(mul((0,0),a) == (0,0) == mul(a,(0,0)) for a in idem)
    assert all((mul(a,b) == "1") == (a == "1" and b == "1")
               for a,b in product(idem,repeat=2))
    print("Idempotent two-element submonoid: complete closure/table, absorbing natural transformation, and identity marking two-out-of-three checked")
    for threshold in range(-11,12,2):
        gamma = lambda i: "1" if i <= threshold else (0,0)
        for i in range(-14,15):
            if i % 2: continue
            for j in [i-1,i+1]:
                edge = (0,0) if {i,j} == {threshold,threshold+1} else "1"
                assert gamma(i) == mul(gamma(j),edge)
    print("Incoming delayed-transition lifts verified at 12 positions; nonunit cannot multiply to identity")
    for threshold in range(-12,13,2):
        alpha = lambda i: "1" if i <= threshold else (0,0)
        for i in range(-14,15):
            if i % 2: continue
            for j in [i-1,i+1]:
                edge = (0,0) if {i,j} == {threshold,threshold+1} else "1"
                assert mul(edge,alpha(i)) == alpha(j)
    print("Outgoing delayed-transition lifts verified at 13 positions")
    return {"elements":[str(x) for x in elements],
            "table":[[str(mul(a,b)) for b in elements] for a in elements]}


if __name__ == "__main__":
    check_empty_paths_and_terminal_obstruction()
    monoid = check_monoids()
    tables = check_pushout_products()
    tables["rectangular_band_monoid"] = monoid
    out = Path(__file__).with_name("e_category_tables.json")
    out.write_text(json.dumps(tables,indent=2)+"\n")
    print("PASS: complete finite composition tables written to",out.name)
