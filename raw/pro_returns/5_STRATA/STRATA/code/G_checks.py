"""Exact finite checks for G.2/G.3 and a mixed EI test in B.5.

Run from the package root: python3 code/G_checks.py.
The general assertions are proved in the paper, not inferred from tests.
"""
from itertools import product
import json
import sympy as sp


def verify(objects, arrows, source, target, identities, compose):
    obj, arr = set(objects), set(arrows)
    assert all(source[a] in obj and target[a] in obj for a in arrows)
    for a in arrows:
        assert compose(a, identities[source[a]]) == a
        assert compose(identities[target[a]], a) == a
    pairs = triples = 0
    for a, b in product(arrows, repeat=2):
        if target[a] == source[b]:
            c = compose(b, a)
            assert c in arr and source[c] == source[a] and target[c] == target[b]
            pairs += 1
    for a, b, c in product(arrows, repeat=3):
        if target[a] == source[b] and target[b] == source[c]:
            assert compose(c, compose(b, a)) == compose(compose(c, b), a)
            triples += 1
    return {"objects": len(objects), "arrows": len(arrows),
            "composable_pairs_checked": pairs, "associative_triples_checked": triples}


def height_one_poset(objects, strict):
    arrows = [(x, x) for x in objects] + list(strict)
    source = {a: a[0] for a in arrows}
    target = {a: a[1] for a in arrows}
    identities = {x: (x, x) for x in objects}
    def compose(b, a):
        assert a[1] == b[0]
        return (a[0], b[1])
    result = verify(objects, arrows, source, target, identities, compose)
    nonid = [a for a in arrows if a[0] != a[1]]
    assert not any(a[1] == b[0] for a, b in product(nonid, repeat=2))
    boundary = sp.zeros(len(objects), len(nonid))
    for j, (s, t) in enumerate(nonid):
        boundary[objects.index(s), j] = -1
        boundary[objects.index(t), j] = 1
    result.update({"arrows_complete": arrows, "d1": [[int(v) for v in row] for row in boundary.tolist()],
                   "integral_H0_rank": int(len(objects) - boundary.rank()),
                   "integral_H1_rank": int(len(nonid) - boundary.rank()),
                   "positive_degree_torsion": []})
    return result


out = {}
out["G2_initial_fork"] = height_one_poset(["b", "a", "c"],
                                           [("b", "a"), ("b", "c")])
out["G2_element_circle"] = height_one_poset(["b0", "b1", "a", "c"],
    [("b0", "a"), ("b0", "c"), ("b1", "a"), ("b1", "c")])
assert out["G2_initial_fork"]["integral_H1_rank"] == 0
assert out["G2_element_circle"]["integral_H1_rank"] == 1

bo, ba = ["*"], [0, 1]
bs = bt = {0: "*", 1: "*"}
bi = {"*": 0}
bcomp = lambda b, a: (a+b) % 2
out["G3_base_C2"] = verify(bo, ba, bs, bt, bi, bcomp)
out["G3_base_C2"]["composition_table"] = [[bcomp(b, a) for a in ba] for b in ba]

eo = [0, 1]
ea = list(product(eo, repeat=2))
es, et = {a: a[0] for a in ea}, {a: a[1] for a in ea}
ei = {x: (x, x) for x in eo}
def ecomp(b, a):
    assert a[1] == b[0]
    return (a[0], b[1])
def projection(a):
    return (a[1]-a[0]) % 2
out["G3_translation_groupoid"] = verify(eo, ea, es, et, ei, ecomp)
for a, b in product(ea, repeat=2):
    if et[a] == es[b]:
        assert projection(ecomp(b, a)) == bcomp(projection(b), projection(a))
for x, g in product(eo, ba):
    outgoing = [a for a in ea if es[a] == x and projection(a) == g]
    incoming = [a for a in ea if et[a] == x and projection(a) == g]
    assert len(outgoing) == len(incoming) == 1
out["G3_translation_groupoid"].update(
    {"arrows_complete": ea, "projection_on_arrows": {str(a): projection(a) for a in ea},
     "unique_lifts_with_each_source_and_target": True,
     "every_object_terminal": True})
pa = [a for a in ea if projection(a) == 0]
assert pa == [(0, 0), (1, 1)]
out["G3_strict_pullback"] = {"objects": eo, "arrows_complete": pa,
    "pi0_source": 2, "pi0_target": 1, "is_W0": False}

mo = [0, 1]
ma = ["id0", "g", "id1", "a"]
ms = {"id0": 0, "g": 0, "id1": 1, "a": 0}
mt = {"id0": 0, "g": 0, "id1": 1, "a": 1}
mi = {0: "id0", 1: "id1"}
def mcomp(b, a):
    assert mt[a] == ms[b]
    if a == mi[ms[a]]:
        return b
    if b == mi[mt[b]]:
        return a
    if b == "a":
        return "a"
    assert a == b == "g"
    return "id0"
out["B5_mixed_EI_candidate"] = verify(mo, ma, ms, mt, mi, mcomp)
out["B5_mixed_EI_candidate"]["status"] = "An unresolved geometric-sheaf test in this audit, not a counterexample."
print(json.dumps(out, indent=2))
