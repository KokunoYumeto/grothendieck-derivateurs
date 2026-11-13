"""Exact binary block checks in generated repaired C.1 substages.

This is a targeted structural diagnostic, not a generic graph-atlas search.
It also constructs a genuine point attachment whose new induced circle
meets one incoming generating image in a two-edge path. All maps come
from the prescribed finite-stage model.
"""

from collections import defaultdict, deque
import json
from pathlib import Path

from finite_akr_intersections import build as build_old
from finite_akr_point_fixed import build as build_point


def graph(C, x):
    G = [set() for _ in range(C.size[x])]
    for b in C.hom.get((1, x), ()):
        assert b[1] not in G[b[0]], "binary edges must be simple"
        G[b[0]].add(b[1])
        G[b[1]].add(b[0])
    return G


def component_count(G):
    unseen = set(range(len(G)))
    count = 0
    while unseen:
        root = unseen.pop()
        stack = [root]
        while stack:
            u = stack.pop()
            for v in G[u] & unseen:
                unseen.remove(v)
                stack.append(v)
        count += 1
    return count


def cyclic_blocks(G):
    """Tarjan's edge-stack algorithm, with iterative depth-first search."""
    discovery = [-1] * len(G)
    low = [-1] * len(G)
    parent = [-1] * len(G)
    clock = 0
    edge_stack = []
    blocks = []
    for root in range(len(G)):
        if discovery[root] >= 0:
            continue
        discovery[root] = low[root] = clock
        clock += 1
        stack = [(root, iter(G[root]))]
        while stack:
            u, iterator = stack[-1]
            try:
                v = next(iterator)
            except StopIteration:
                stack.pop()
                p = parent[u]
                if p >= 0:
                    low[p] = min(low[p], low[u])
                    if low[u] >= discovery[p]:
                        block_edges = []
                        while edge_stack:
                            edge = edge_stack.pop()
                            block_edges.append(edge)
                            if edge == (p, u):
                                break
                        vertices = {v for e in block_edges for v in e}
                        if len(vertices) >= 3:
                            blocks.append({'vertices': len(vertices), 'edges': len(block_edges),
                                           'cycle_rank': len(block_edges) - len(vertices) + 1})
                continue
            if discovery[v] < 0:
                parent[v] = u
                discovery[v] = low[v] = clock
                clock += 1
                edge_stack.append((u, v))
                stack.append((v, iter(G[v])))
            elif v != parent[u] and discovery[v] < discovery[u]:
                low[u] = min(low[u], discovery[v])
                edge_stack.append((u, v))
        assert not edge_stack
    return blocks


def partial_two_tree_certificate(G):
    """Degree <=2 elimination with filling, an exact K4-minor-free test.

    Eliminating a degree-two vertex with a new neighbor edge is a graph
    minor, and reconstructing it is a partial-two-tree extension. Thus
    complete elimination certifies treewidth at most two. Failure only
    records the residual core; no positive K4 assertion is used below.
    """
    adjacency = {v: set(neighbors) for v, neighbors in enumerate(G)}
    queue = deque(v for v, neighbors in adjacency.items() if len(neighbors) <= 2)
    removed = []
    while queue:
        v = queue.popleft()
        if v not in adjacency or len(adjacency[v]) > 2:
            continue
        neighbors = sorted(adjacency[v])
        fill = None
        if len(neighbors) == 2:
            a, b = neighbors
            if b not in adjacency[a]:
                adjacency[a].add(b)
                adjacency[b].add(a)
                fill = [a, b]
        for w in neighbors:
            adjacency[w].remove(v)
            if len(adjacency[w]) <= 2:
                queue.append(w)
        del adjacency[v]
        removed.append([v, neighbors, fill])
    return {
        'complete_elimination': not adjacency,
        'vertices_eliminated': len(removed),
        'fill_edges': sum(record[2] is not None for record in removed),
        'residual_vertices': len(adjacency),
        'residual_edges': sum(map(len, adjacency.values())) // 2,
    }


def inspect(C, target, label):
    G = graph(C, target)
    blocks = cyclic_blocks(G)
    edges = sum(map(len, G)) // 2
    components = component_count(G)
    shapes = defaultdict(int)
    for block in blocks:
        shapes[(block['vertices'], block['edges'], block['cycle_rank'])] += 1
    return {
        'label': label,
        'target': C.names[target],
        'vertices': len(G), 'edges': edges,
        'components': components,
        'cycle_rank': edges - len(G) + components,
        'cactus': all(block['cycle_rank'] == 1 for block in blocks),
        'cyclic_block_shapes': [{'vertices': v, 'edges': e, 'cycle_rank': r, 'multiplicity': multiplicity}
                                for (v, e, r), multiplicity in sorted(shapes.items())],
        'partial_two_tree': partial_two_tree_certificate(G),
    }


def distance_two_birth():
    C = build_old('k1')
    source = C.names.index('Q_0_1_0_2')
    old_graph = graph(C, source)
    center = next(v for v, neighbors in enumerate(old_graph) if len(neighbors) == 2)
    left, right = sorted(old_graph[center])
    assert len(old_graph[left]) == len(old_graph[right]) == 1
    target, n = C.qfilter('Q_K2_P13_distance_two_points', 0, source,
                         (left,), (right,), 153, 3)
    assert n == 3
    G = graph(C, target)
    assert sum(map(len, G)) // 2 - len(G) + component_count(G) == 1
    degree = list(map(len, G))
    queue = deque(v for v, d in enumerate(degree) if d <= 1)
    removed = set()
    while queue:
        v = queue.popleft()
        if v in removed:
            continue
        removed.add(v)
        for w in G[v] - removed:
            degree[w] -= 1
            if degree[w] <= 1:
                queue.append(w)
    circle_set = set(range(len(G))) - removed
    assert all(len(G[v] & circle_set) == 2 for v in circle_set)
    start = min(circle_set)
    circle = [start]
    previous = None
    current = start
    while True:
        following = min((G[current] & circle_set) - {previous})
        if following == start:
            break
        circle.append(following)
        previous, current = current, following
    assert set(circle) == circle_set
    assert len(circle) == 306
    best = None
    for f in sorted(C.hom[source, target]):
        overlap = set(f) & circle_set
        intersection_edges = sorted([u, v] for u in overlap for v in G[u] & overlap if u < v)
        record = {'source_map': list(f), 'circle_vertices_in_image': sorted(overlap),
                  'circle_edges_in_image': intersection_edges}
        if best is None or len(intersection_edges) > len(best['circle_edges_in_image']):
            best = record
    assert len(best['circle_vertices_in_image']) == 3
    assert len(best['circle_edges_in_image']) == 2
    return C, target, {
        'old_source': C.names[source], 'old_source_size': C.size[source],
        'old_path': [left, center, right],
        'defining_pair_source': 'V', 'defining_point_pair': [left, right],
        'n': 3, 's': 153, 'a_parameters': ['2', '8/5', '128/85'],
        'new_circle_length': len(circle), 'new_circle_vertices_in_cyclic_order': circle,
        'new_circle_is_induced': True,
        'maximum_generating_copy_intersection_vertices': 3,
        'maximum_generating_copy_intersection_edges': 2,
        'witness': best,
        'conclusion': 'The one-edge proper-overlap claim for every newborn induced cycle is false in actual C.1.',
    }


def selected_wheel_certificate(C, target):
    G = graph(C, target)
    hub = max(range(len(G)), key=lambda v: len(G[v]))
    assert len(G[hub]) == 153
    connected = {hub}
    todo = [hub]
    while todo:
        u = todo.pop()
        for v in G[u] - connected:
            connected.add(v)
            todo.append(v)
    rim = connected - {hub}
    assert len(rim) == 6579
    assert all(len(G[v] & rim) == 2 for v in rim)
    start = min(G[hub])
    order = [start]
    previous = None
    current = start
    while True:
        following = min((G[current] & rim) - {previous})
        if following == start:
            break
        order.append(following)
        previous, current = current, following
    assert set(order) == rim
    spoke_positions = [i for i, v in enumerate(order) if v in G[hub]]
    lengths = [((spoke_positions[(i + 1) % 153] - spoke_positions[i]) % len(order))
               for i in range(153)]
    assert set(lengths) == {43}
    positions = spoke_positions[:3]
    a, b, c = [order[i] for i in positions]
    paths = [[hub, a], [hub, b], [hub, c],
             order[positions[0]:positions[1] + 1],
             order[positions[1]:positions[2] + 1],
             order[positions[2]:] + order[:positions[0] + 1]]
    branch = {hub, a, b, c}
    interiors = set()
    endpoints = set()
    for path in paths:
        assert all(v in G[u] for u, v in zip(path, path[1:]))
        assert len(path) == len(set(path))
        assert not (set(path[1:-1]) & (branch | interiors))
        interiors.update(path[1:-1])
        endpoints.add(tuple(sorted((path[0], path[-1]))))
    assert len(endpoints) == 6
    old_target = C.names.index('Q_0_1_0_1')
    f, g = sorted(C.hom[1, old_target])[:2]
    certificate = {
        'source': 'W', 'old_target': C.names[old_target],
        'f': f, 'g': g, 'n': 3, 's': 153,
        'a_parameters': ['2', '8/5', '128/85'],
        'hub': hub, 'spokes': 153, 'rim_segments': 153,
        'each_rim_segment_edges': 43,
        'binary_nontrivial_component_vertices': len(connected),
        'K4_branch_vertices': [hub, a, b, c],
        'six_pairwise_internally_disjoint_K4_paths': paths,
    }
    destination = Path(__file__).with_name('akr_selected_wheel_certificate.json')
    destination.write_text(json.dumps(certificate, indent=2) + '\n')
    return {
        'f': f, 'g': g, 'hub': hub, 'spokes': 153,
        'rim_segments': 153, 'each_rim_segment_edges': 43,
        'K4_subdivision_verified': True,
        'K4_branch_vertices': [hub, a, b, c],
        'six_path_edge_lengths': [len(path) - 1 for path in paths],
        'certificate_file': destination.name,
        'conclusion': 'A genuine C.1 stage already has a subdivided wheel, hence is neither cactus nor series-parallel.',
    }


def main():
    records = []
    wheel = None
    for mode in ('selected_k2', 'critical_k3'):
        C = build_old(mode)
        records.append(inspect(C, len(C.size) - 1, mode))
        if mode == 'selected_k2':
            wheel = selected_wheel_certificate(C, len(C.size) - 1)
    for slots, source, label in (((0, 1), 'P12', 'P12_edge_points'),
                                 ((0, 2), 'P12', 'P12_v3_points'),
                                 ((0, 1), 'P13', 'P13_edge_points')):
        C, _, target = build_point(slots, source)
        records.append(inspect(C, target, label))
    C, target, certificate = distance_two_birth()
    records.append(inspect(C, target, 'P13_distance_two_points'))
    output = {'scope': 'Only the six specified actual generated substages; no all-stage graph-class inference.',
              'structural_checks': records, 'selected_wheel_certificate': wheel,
              'two_edge_overlap_certificate': certificate}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
