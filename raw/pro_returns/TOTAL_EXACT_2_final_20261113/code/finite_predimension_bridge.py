"""Exact finite audit of the alternating strict-predimension bridge.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.
This program checks prescribed examples, not a category search. It builds
the actual set quotient by union-find; uses exact rational coordinates;
checks all factor/edge incidences; and checks positivity and d-closedness
over ALL target vertex subsets using the independently validated integer
min-cut routine in predimension_cone_certificates.py. General validity is
proved separately in sections/predimension_stabilizers.tex and audited in
notes/finite_predimension_stabilizer_audit.md.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json

from predimension_cone_certificates import (
    Hypergraph, all_subsets, closed_certificate, positive_certificate,
)


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[y] = x


def induced(source, target, mapping):
    assert len(mapping) == source.n
    assert list(mapping) == sorted(set(mapping))
    expected = {tuple(sorted(mapping[v] for v in e)) for e in source.edges}
    actual = {e for e in target.edges if set(e) <= set(mapping)}
    assert expected == actual


def exhaustive_closed(graph, subset):
    subset = set(subset)
    baseline = graph.delta(subset)
    assert all(graph.delta(u) > baseline for u in all_subsets(graph.n) if subset < u)


def cyclic_interval(indices, s):
    indices = set(indices)
    if not indices:
        return False
    return any(indices == {(start + j) % s for j in range(len(indices))}
               for start in indices)


def build_and_check(name, D, E, B, C, d0, d1):
    B, C = frozenset(B), frozenset(C)
    F = B & C
    for graph in (D, E):
        assert all(graph.delta(u) > 0 for u in all_subsets(graph.n) if u)
        # The chosen inputs belong to both categories in the theorem.
        for atom in [{v} for v in range(graph.n)] + [set(e) for e in graph.edges]:
            exhaustive_closed(graph, atom)
    exhaustive_closed(D, B)
    exhaustive_closed(D, C)
    for mapping in (d0, d1):
        induced(D, E, mapping)
        exhaustive_closed(E, mapping)
    assert all(d0[x] == d1[x] for x in F)

    delta_E = E.delta(range(E.n))
    m = max(len(B), len(C))
    gap = min([d0[x + 1] - d0[x] for x in range(D.n - 1)]
              + [d1[x + 1] - d1[x] for x in range(D.n - 1)] or [1])
    displacement = max(abs(d1[x] - d0[x]) for x in range(D.n))
    N = max(4, (3 * (delta_E + 2 * m)) // 2 + 1,
            (2 * displacement) // gap + 1)
    s = 2 * N
    assert s > 3 * (delta_E + 2 * m)
    assert Fraction(2 * displacement, N) < gap

    labels = [(0, v) for v in range(E.n)]
    labels += [(i, v) for i in range(1, s) for v in range(D.n)]
    raw = {label: i for i, label in enumerate(labels)}
    dsu = DSU(len(labels))

    def occurrence(i, x):
        if i == 0:
            return raw[0, d0[x]]
        if i == s:
            return raw[0, d1[x]]
        return raw[i, x]

    for i in range(s):
        for x in B if i % 2 == 0 else C:
            dsu.union(occurrence(i, x), occurrence(i + 1, x))

    def coordinate(label):
        i, x = label
        if i == 0:
            return Fraction(x)
        j = i // 2
        step = j if i % 2 == 0 or x in B else j + 1
        return Fraction((N - step) * d0[x] + step * d1[x], N)

    classes = {}
    for index, label in enumerate(labels):
        classes.setdefault(dsu.find(index), []).append(label)
    coordinates = {}
    for root, occurrences in classes.items():
        values = {coordinate(label) for label in occurrences}
        assert len(values) == 1, (name, occurrences, values)
        coordinates[root] = values.pop()
        indices = [i for i, _ in occurrences]
        assert len(indices) == len(set(indices)), (name, occurrences)

    ordered_roots = sorted(classes, key=lambda root: (coordinates[root], min(classes[root])))
    positions = {root: i for i, root in enumerate(ordered_roots)}
    maps = []
    for i in range(s):
        size = E.n if i == 0 else D.n
        maps.append(tuple(positions[dsu.find(raw[i, v])] for v in range(size)))
    edges = set()
    for i, mapping in enumerate(maps):
        source = E if i == 0 else D
        edges.update(tuple(sorted(mapping[v] for v in e)) for e in source.edges)
    Z = Hypergraph(len(classes), tuple(sorted(edges)))
    for i, mapping in enumerate(maps):
        induced(E if i == 0 else D, Z, mapping)

    for i in range(s):
        j = (i + 1) % s
        overlap = B if i % 2 == 0 else C
        expected = {positions[dsu.find(occurrence(i, x))] for x in overlap}
        assert set(maps[i]) & set(maps[j]) == expected

    full = {positions[dsu.find(raw[0, d0[x]])] for x in F}
    point_visibility = []
    for vertex, root in enumerate(ordered_roots):
        indices = sorted(i for i, _ in classes[root])
        if vertex in full:
            assert indices == list(range(s))
        else:
            assert len(indices) <= 3 and cyclic_interval(indices, s)
        point_visibility.append(indices)
    edge_visibility = []
    for edge in Z.edges:
        by_points = set.intersection(*(set(point_visibility[v]) for v in edge))
        by_edges = set()
        for i, mapping in enumerate(maps):
            source = E if i == 0 else D
            copied = {tuple(sorted(mapping[v] for v in e)) for e in source.edges}
            if edge in copied:
                by_edges.add(i)
        assert by_points == by_edges
        assert cyclic_interval(by_edges, s)
        edge_visibility.append(sorted(by_edges))

    # Check the whole alternating sequence, including its endpoints in E.
    sequence = [tuple(maps[0][d0[x]] for x in range(D.n))]
    sequence.extend(maps[1:])
    sequence.append(tuple(maps[0][d1[x]] for x in range(D.n)))
    for i in range(s):
        for x in B if i % 2 == 0 else C:
            assert sequence[i][x] == sequence[i + 1][x]
    assert all(list(mapping) == sorted(set(mapping)) for mapping in sequence)

    positivity = positive_certificate(Z)
    # Identical factor images need only one all-subset optimization.
    closure = {}
    for mapping in maps:
        key = tuple(sorted(mapping))
        if key not in closure:
            closure[key] = closed_certificate(Z, mapping)
    gaps = [check[1] - cert["delta"] for cert in closure.values() for check in cert["checks"]]
    histogram = dict(sorted(Counter(len(indices) for indices in point_visibility).items()))
    triple_wrap = [v for v, indices in enumerate(point_visibility)
                   if v not in full and indices == [0, 1, s - 1]]
    if name == "crossing_endpoint_images":
        assert triple_wrap, "The fixture must actually exercise the three-index fibre."
    if name == "equal_whole_bases":
        assert any(len(indices) == s for indices in edge_visibility)
    record = {
        "name": name, "N": N, "s": s,
        "source_D": {"n": D.n, "edges": D.edges},
        "source_E": {"n": E.n, "edges": E.edges},
        "B": sorted(B), "C": sorted(C), "F": sorted(F), "d0": d0, "d1": d1,
        "delta_E": delta_E, "m": m, "gap": gap, "displacement": displacement,
        "target": {"n": Z.n, "edges": Z.edges, "delta": Z.delta(range(Z.n))},
        "factor_maps": maps, "point_occurrences": [classes[root] for root in ordered_roots],
        "rational_coordinates": [[coordinates[root].numerator, coordinates[root].denominator]
                                 for root in ordered_roots],
        "point_visibility": point_visibility, "edge_visibility": edge_visibility,
        "visibility_histogram": histogram, "three_index_wrap_vertices": triple_wrap,
        "positive_checks": positivity, "closed_factor_checks": list(closure.values()),
        "minimum_nonempty_delta": min(check[1] for check in positivity),
        "minimum_strict_factor_increment": min(gaps) if gaps else None,
    }
    print(name + ":", "N=" + str(N), "factors=" + str(s),
          "vertices=" + str(Z.n), "edges=" + str(len(Z.edges)),
          "delta=" + str(record["target"]["delta"]))
    print("  point visibility multiplicities:", histogram,
          "; three-index wrap vertices:", triple_wrap)
    print("  exact minima: nonempty delta=", record["minimum_nonempty_delta"],
          "; strict factor increment=", record["minimum_strict_factor_increment"],
          "; distinct closed factor images=", len(closure))
    print("  PASS: strict quotient fibres, induced factors, edge routing, rational ordered cocone, all-subset d-closure.")
    return record


def main():
    W = Hypergraph(3, ((0, 1, 2),))
    crossing = Hypergraph(5, ((0, 1, 2), (1, 3, 4)))
    shared_middle = Hypergraph(5, ((0, 2, 3), (1, 2, 4)))
    cases = [
        ("crossing_endpoint_images", W, crossing, {0}, {1}, (1, 3, 4), (0, 1, 2)),
        ("equal_point_bases", W, shared_middle, {1}, {1}, (0, 2, 3), (1, 2, 4)),
        ("whole_left_base", W, shared_middle, {0, 1, 2}, {1}, (0, 2, 3), (1, 2, 4)),
        ("equal_whole_bases", W, W, {0, 1, 2}, {0, 1, 2}, (0, 1, 2), (0, 1, 2)),
    ]
    records = [build_and_check(*case) for case in cases]
    path = Path(__file__).with_name("finite_predimension_bridge_certificates.json")
    path.write_text(json.dumps({"method": "actual union-find quotient, rational coordinates, exact integer min-cut",
                                "cases": records}, indent=2) + "\n")
    replay = json.loads(path.read_text())
    assert [case["name"] for case in replay["cases"]] == [case[0] for case in cases]
    for case in replay["cases"]:
        graph = Hypergraph(case["target"]["n"], tuple(tuple(e) for e in case["target"]["edges"]))
        for forced, value, witness in case["positive_checks"]:
            assert forced in witness and graph.delta(witness) == value > 0
        for cert in case["closed_factor_checks"]:
            image = set(cert["image"])
            assert graph.delta(image) == cert["delta"]
            for extra, value, witness in cert["checks"]:
                assert image | {extra} <= set(witness)
                assert graph.delta(witness) == value > cert["delta"]
    print("Certificate:", path.name, "bytes", path.stat().st_size,
          "SHA256", hashlib.sha256(path.read_bytes()).hexdigest())
    print("PASS: four prescribed finite checks supplement the universal bridge proof; they do not prove totality by enumeration.")


if __name__ == "__main__":
    main()
