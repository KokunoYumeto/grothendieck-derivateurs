"""Exact finite certificates for the predimension path-cone constructions.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.
The general claims are proved in the accompanying TeX. This program checks
the finite path table, the universal ordered seven-cycle, and concrete cone
maps, including a positive-predimension object with no closed raw point.
Minimum predimensions are computed by an integer maximum-closure/min-cut
reduction, independently compared with exhaustive subset checks on the
seven-cycle. No floating-point ranks or sampled subset tests are used.
"""
from collections import deque
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import hashlib
import json


@dataclass(frozen=True)
class Hypergraph:
    n: int
    edges: tuple

    def delta(self, vertices):
        vertices = set(vertices)
        return 2 * len(vertices) - 3 * sum(set(e) <= vertices for e in self.edges)


class Dinic:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]

    def add(self, u, v, capacity):
        f = [v, capacity, None]
        r = [u, 0, f]
        f[2] = r
        self.adj[u].append(f)
        self.adj[v].append(r)

    def flow(self, source, sink):
        value = 0
        while True:
            level = [-1] * len(self.adj)
            level[source] = 0
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v, cap, _ in self.adj[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[sink] < 0:
                break
            position = [0] * len(self.adj)

            def push(u, amount):
                if u == sink:
                    return amount
                while position[u] < len(self.adj[u]):
                    edge = self.adj[u][position[u]]
                    v, cap, reverse = edge
                    if cap and level[v] == level[u] + 1:
                        got = push(v, min(cap, amount))
                        if got:
                            edge[1] -= got
                            reverse[1] += got
                            return got
                    position[u] += 1
                return 0

            while True:
                amount = push(source, 10**12)
                if not amount:
                    break
                value += amount
        reachable = {source}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, cap, _ in self.adj[u]:
                if cap and v not in reachable:
                    reachable.add(v)
                    queue.append(v)
        return value, reachable


def minimum_delta(graph, forced=()):
    """Minimize delta(U) over vertex subsets containing the forced set.

    An edge-node has profit 3 and forces its three vertex-nodes, whose costs
    are 2 each. All profitable available edge-nodes are included at optimum.
    Thus a maximum closed-set weight is -min delta, exactly over integers.
    """
    forced = frozenset(forced)
    source = graph.n + len(graph.edges)
    sink = source + 1
    network = Dinic(sink + 1)
    infinity = 1 + 2 * graph.n + 3 * len(graph.edges)
    for v in range(graph.n):
        network.add(v, sink, 2)
    for i, edge in enumerate(graph.edges):
        node = graph.n + i
        network.add(source, node, 3)
        for v in edge:
            network.add(node, v, infinity)
    for v in forced:
        network.add(source, v, infinity)
    cut, reachable = network.flow(source, sink)
    vertices = sorted(v for v in range(graph.n) if v in reachable)
    result = cut - 3 * len(graph.edges)
    assert forced <= set(vertices)
    assert graph.delta(vertices) == result
    return result, vertices


def positive_certificate(graph):
    checks = []
    for v in range(graph.n):
        value, witness = minimum_delta(graph, [v])
        checks.append([v, value, witness])
        assert value > 0
    return checks


def closed_certificate(graph, vertices):
    vertices = frozenset(vertices)
    baseline = graph.delta(vertices)
    checks = []
    for v in range(graph.n):
        if v not in vertices:
            value, witness = minimum_delta(graph, vertices | {v})
            checks.append([v, value, witness])
            assert value > baseline, (vertices, baseline, v, value, witness)
    return {"image": sorted(vertices), "delta": baseline, "checks": checks}


def induced_embedding(source, target, mapping):
    assert len(mapping) == source.n
    assert list(mapping) == sorted(set(mapping))
    image = set(mapping)
    mapped = {tuple(sorted(mapping[v] for v in edge)) for edge in source.edges}
    restricted = {edge for edge in target.edges if set(edge) <= image}
    assert mapped == restricted
    return closed_certificate(target, image)


def cone(graph):
    n = graph.n
    centre = 3 * n
    paths = {}
    edges = list(graph.edges)
    for x in range(n):
        r, s = n + 2 * x, n + 2 * x + 1
        a, b, d = 3 * n + 1 + 3 * x, 3 * n + 2 + 3 * x, 3 * n + 3 + 3 * x
        path = ((x, r, a), (r, s, b), (s, centre, d))
        assert all(tuple(sorted(edge)) == edge for edge in path)
        paths[x] = path
        edges.extend(path)
    result = Hypergraph(6 * n + 1, tuple(sorted(edges)))
    return result, centre, paths


def cone_map(source, target, mapping):
    n, m = source.n, target.n
    out = list(mapping)
    for x in range(n):
        out.extend([m + 2 * mapping[x], m + 2 * mapping[x] + 1])
    out.append(3 * m)
    for x in range(n):
        out.extend(3 * m + 1 + 3 * mapping[x] + j for j in range(3))
    return tuple(out)


def graph_from_named(order, edges):
    labels = {v: i for i, v in enumerate(order)}
    return Hypergraph(len(order), tuple(sorted(tuple(sorted(labels[v] for v in e)) for e in edges)))


def all_subsets(n):
    for mask in range(1 << n):
        yield {v for v in range(n) if mask & (1 << v)}


def main():
    certificate = {"method": "exact integer min-cut plus exhaustive subset comparison"}
    # The five-new-vertex path lemma: all 31 nonempty relative subsets.
    requirements = ({0, 2}, {0, 1, 3}, {1, 4})
    table = []
    for vertices in all_subsets(5):
        if not vertices:
            continue
        edges = sum(required <= vertices for required in requirements)
        value = 2 * len(vertices) - 3 * edges
        assert value >= 1
        table.append([sorted(vertices), edges, value])
    certificate["relative_path_table"] = table
    print("Length-three relative path: 31/31 nonempty subsets strictly positive.")

    order = ["u", "v", "p", "ru", "su", "rv", "sv", "c", "au", "bu", "du", "av", "bv", "dv"]
    named_edges = [("u", "v", "p"), ("u", "ru", "au"), ("ru", "su", "bu"), ("su", "c", "du"),
                   ("v", "rv", "av"), ("rv", "sv", "bv"), ("sv", "c", "dv")]
    seven = graph_from_named(order, named_edges)
    subset_values = [(vertices, seven.delta(vertices)) for vertices in all_subsets(seven.n)]
    assert min(value for vertices, value in subset_values if vertices) == 2
    atoms = [{v} for v in range(seven.n)] + [set(e) for e in seven.edges]
    seven_checks = []
    for atom in atoms:
        true_min = min(value for vertices, value in subset_values if atom < vertices)
        computed = closed_certificate(seven, atom)
        assert min(check[1] for check in computed["checks"]) == true_min
        seven_checks.append(computed)
    # Verify the universal cycle and its augmentation, with binary endpoints
    # always the first two vertices in the induced linear order.
    edge_index = {edge: i for i, edge in enumerate(seven.edges)}
    coefficients = [0] * len(seven.edges)
    labels = {v: i for i, v in enumerate(order)}
    for edge, sign in zip(named_edges, [1, -1, -1, -1, 1, 1, 1]):
        coefficients[edge_index[tuple(sorted(labels[v] for v in edge))]] = sign
    boundary = [0] * seven.n
    for edge, coefficient in zip(seven.edges, coefficients):
        boundary[edge[0]] -= coefficient
        boundary[edge[1]] += coefficient
    assert not any(boundary)
    assert sum(coefficients) == 1
    certificate["seven_cycle"] = {"order": order, "edges": seven.edges, "coefficients": coefficients,
                                  "all_subsets": len(subset_values), "atom_checks": seven_checks}
    print("Universal ordered seven-cycle: all 16384 subsets checked; 14 points and 7 edges d-closed; cycle augmentation 1.")

    # A positive object in the unrestricted category with NO closed raw point.
    dense = Hypergraph(5, ((0, 1, 2), (0, 1, 3), (0, 2, 4)))
    dense_values = [(vertices, dense.delta(vertices)) for vertices in all_subsets(dense.n)]
    assert min(value for vertices, value in dense_values if vertices) == 1
    for v in range(dense.n):
        assert any(value <= 2 for vertices, value in dense_values if {v} < vertices)
    dense_cone, centre, _ = cone(dense)
    certificate["non_atom_closed_example"] = {
        "n": dense.n, "edges": dense.edges,
        "positive": positive_certificate(dense_cone),
        "old_embedding": induced_embedding(dense, dense_cone, tuple(range(dense.n))),
        "centre": closed_certificate(dense_cone, {centre})}
    print("Unrestricted five-vertex example: positive delta, no closed raw point; its 31-vertex cone is positive, with closed old copy and centre.")

    # Concrete composable arrows W -> loose four-cycle -> that cycle plus a point.
    word = Hypergraph(3, ((0, 1, 2),))
    cycle = Hypergraph(8, tuple(sorted(tuple(sorted((i, (i + 1) % 4, 4 + i))) for i in range(4))))
    larger = Hypergraph(9, cycle.edges)
    f = (0, 1, 4)
    g = tuple(range(8))
    fg = tuple(g[v] for v in f)
    maps = []
    for name, source, target, mapping in [("f", word, cycle, f), ("g", cycle, larger, g), ("gf", word, larger, fg)]:
        original = induced_embedding(source, target, mapping)
        fs, cs, _ = cone(source)
        ft, ct, _ = cone(target)
        mapped = cone_map(source, target, mapping)
        extension = induced_embedding(fs, ft, mapped)
        assert mapped[cs] == ct
        assert mapped[:source.n] == mapping
        maps.append({"name": name, "old": original, "cone": extension, "mapping": mapped})
    ff = cone_map(word, cycle, f)
    gg = cone_map(cycle, larger, g)
    assert tuple(gg[v] for v in ff) == cone_map(word, larger, fg)
    assert cone_map(cycle, cycle, tuple(range(cycle.n))) == tuple(range(cone(cycle)[0].n))
    certificate["composable_maps"] = maps
    print("Cone maps on W -> C4 -> C4+point: induced d-closed embeddings; identity, composition, inclusion and centre naturality checked exactly.")

    fc, centre, paths = cone(cycle)
    path_checks = []
    for x, path in paths.items():
        vertices = set(v for edge in path for v in edge)
        path_checks.append({"x": x, "path": closed_certificate(fc, vertices),
                            "edges": [closed_certificate(fc, edge) for edge in path]})
    certificate["actual_paths"] = path_checks
    print("All 8 designated three-edge paths in F(C4), and all 24 constituent hyperedges, are d-closed.")
    target = Path(__file__).with_name("predimension_cone_certificates.json")
    target.write_text(json.dumps(certificate, indent=2) + "\n")
    readback = json.loads(target.read_text())
    assert readback["seven_cycle"]["all_subsets"] == 16384
    assert len(readback["relative_path_table"]) == 31
    print("Certificate:", target.name, "bytes", target.stat().st_size,
          "SHA256", hashlib.sha256(target.read_bytes()).hexdigest())
    print("PASS: exact finite checks supplement, and do not replace, the general proofs.")


if __name__ == "__main__":
    main()
