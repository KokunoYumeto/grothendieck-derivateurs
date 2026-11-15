"""Generic connected convex-embedding stress test for repaired beta gluing.

This is not an AKR C.1 construction. It exhaustively generates unlabelled
connected simple target graphs up to --vertices (default 6), all nonempty
connected strongly convex induced source images, and every isomorphism
between two distinct such images. Point-transition cycles are excluded.
It tests whether every copy remains strongly geodesically convex at k=n.
Cases covered by the proved large-target bound are counted separately.
"""
from collections import defaultdict, deque
from itertools import combinations, permutations, product
from pathlib import Path
import argparse
import json
import time


def edges_of(adj):
    return [(u, v) for u, ns in enumerate(adj) for v in ns if u < v]


def distances(adj, source):
    d = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in d:
                d[w] = d[v] + 1
                queue.append(w)
    return d


def canonical_code(adj, pairs):
    blocks = defaultdict(list)
    for v, ns in enumerate(adj):
        blocks[len(ns)].append(v)
    best = None
    for choices in product(*(permutations(blocks[d]) for d in sorted(blocks))):
        order = sum((tuple(c) for c in choices), ())
        code = sum((1 << bit) for bit, (i, j) in enumerate(pairs)
                   if order[j] in adj[order[i]])
        if best is None or code < best:
            best = code
    return best


def connected_graphs(size):
    pairs = list(combinations(range(size), 2))
    seen = set()
    for mask in range(1 << len(pairs)):
        if mask.bit_count() < size - 1:
            continue
        adj = [set() for _ in range(size)]
        for bit, (u, v) in enumerate(pairs):
            if mask & (1 << bit):
                adj[u].add(v)
                adj[v].add(u)
        if len(distances(adj, 0)) != size:
            continue
        code = canonical_code(adj, pairs)
        if code in seen:
            continue
        seen.add(code)
        canonical = [set() for _ in range(size)]
        for bit, (u, v) in enumerate(pairs):
            if code & (1 << bit):
                canonical[u].add(v)
                canonical[v].add(u)
        yield canonical


def convex_subsets(adj, dd):
    n = len(adj)
    out = []
    for mask in range(1, (1 << n) - 1):
        inside = tuple(v for v in range(n) if mask & (1 << v))
        outside = [v for v in range(n) if not mask & (1 << v)]
        if all(dd[u][w] + dd[w][v] != dd[u][v]
               for u, v in combinations(inside, 2) for w in outside):
            out.append(inside)
    return out


def relation(f, g):
    fixed = {x for x, y in zip(f, g) if x == y}
    step = {x: y for x, y in zip(f, g) if x != y}
    active = set(step) | set(step.values())
    paths = []
    for start in sorted(set(step) - set(step.values())):
        path = [start]
        while path[-1] in step:
            path.append(step[path[-1]])
        paths.append(path)
    if {v for path in paths for v in path} != active:
        return None
    return fixed, paths, active


def beta(i, t, length, k):
    if i <= 2 * k:
        u = t + i
        return u if u <= 2 * k else u + 2 * k - length + 1
    u = t - i + 6 * k - length + 2
    return u if u > 2 * k else t - i + 4 * k


def glue(adj, f, g, k):
    fixed, paths, active = relation(f, g)
    s = 4 * k + 1
    fixed_tags = {v: j for j, v in enumerate(sorted(fixed))}
    offset = len(fixed_tags)
    coords = {v: (j, t, len(path)) for j, path in enumerate(paths)
              for t, v in enumerate(path)}
    private = [v for v in range(len(adj)) if v not in fixed | active]
    private_tags = {v: j for j, v in enumerate(private)}
    size = offset + s * (len(paths) + len(private))
    maps = []
    out = [set() for _ in range(size)]
    for i in range(s):
        alpha = []
        for v in range(len(adj)):
            if v in fixed:
                alpha.append(fixed_tags[v])
            elif v in active:
                j, t, length = coords[v]
                alpha.append(offset + s * j + beta(i, t, length, k))
            else:
                alpha.append(offset + s * (len(paths) + private_tags[v]) + i)
        assert len(set(alpha)) == len(alpha)
        maps.append(alpha)
        for u, v in edges_of(adj):
            a, b = alpha[u], alpha[v]
            out[a].add(b)
            out[b].add(a)
    for i in range(s):
        left, right = ((g, f) if i < 2 * k else
                       (g, g) if i == 2 * k else
                       (f, g) if i < 4 * k else (f, f))
        assert [maps[i][v] for v in left] == [maps[(i + 1) % s][v] for v in right]
    return out, maps


def convex_failure(adj, maps, old_dist, diameter):
    for index, alpha in enumerate(maps):
        image = set(alpha)
        inverse = {v: u for u, v in enumerate(alpha)}
        for a in image:
            for b in adj[a] & image:
                if old_dist[inverse[a]][inverse[b]] != 1:
                    return {'copy': index, 'source_vertex': inverse[a],
                            'target_vertex': inverse[b], 'copy_map': alpha,
                            'outside_path': [a, b], 'outside_length': 1,
                            'old_distance': old_dist[inverse[a]][inverse[b]],
                            'failure_type': 'new edge inside vertex image'}
        for source, start in enumerate(alpha):
            first = (start, False)
            parent = {first: None}
            level = {first: 0}
            queue = deque([first])
            while queue:
                state = queue.popleft()
                v, left_image = state
                d = level[state]
                if left_image and v in image and d <= old_dist[source][inverse[v]]:
                    path = [v]
                    cursor = state
                    while parent[cursor] is not None:
                        cursor = parent[cursor]
                        path.append(cursor[0])
                    path.reverse()
                    return {'copy': index, 'source_vertex': source,
                            'target_vertex': inverse[v], 'copy_map': alpha,
                            'outside_path': path, 'outside_length': d,
                            'old_distance': old_dist[source][inverse[v]]}
                if d == diameter:
                    continue
                for w in adj[v]:
                    nxt = (w, left_image or w not in image)
                    if nxt not in parent:
                        parent[nxt] = state
                        level[nxt] = d + 1
                        queue.append(nxt)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vertices', type=int, default=6)
    args = parser.parse_args()
    start = time.monotonic()
    counts = defaultdict(int)
    for size in range(2, args.vertices + 1):
        for adj in connected_graphs(size):
            counts['target_graphs'] += 1
            dd = [distances(adj, v) for v in range(size)]
            diameter = max(d for row in dd for d in row.values())
            groups = defaultdict(list)
            for subset in convex_subsets(adj, dd):
                groups[len(subset)].append(subset)
            for subsets in groups.values():
                for f in subsets:
                    for image in subsets:
                        if f == image:
                            continue
                        for g in permutations(image):
                            if any((f[j] in adj[f[i]]) != (g[j] in adj[g[i]])
                                   for i, j in combinations(range(len(f)), 2)):
                                continue
                            data = relation(f, g)
                            if data is None:
                                counts['excluded_point_cycles'] += 1
                                continue
                            counts['acyclic_convex_pairs'] += 1
                            n = max([2] + [len(path) for path in data[1]])
                            k, s = n, 4 * n + 1
                            if s > (2 * n - 2) * (diameter + 1):
                                counts['covered_by_proved_large_target_bound'] += 1
                                continue
                            counts['explicit_gluings_tested'] += 1
                            out, maps = glue(adj, f, g, k)
                            fail = convex_failure(out, maps, dd, diameter)
                            if fail:
                                result = {'scope': 'generic connected convex graphs; not an actual C.1 category',
                                          'target_vertices': size, 'target_edges': edges_of(adj),
                                          'f': f, 'g': g, 'n': n, 'k': k, 's': s,
                                          'failure': fail, 'counts': dict(counts)}
                                print(json.dumps(result, indent=2), flush=True)
                                Path(__file__).with_suffix('.failure.json').write_text(json.dumps(result, indent=2))
                                return
        print(json.dumps({'completed_target_size': size, 'counts': dict(counts),
                          'seconds': time.monotonic() - start}), flush=True)
    print(json.dumps({'status': 'no failure in stated finite scope',
                      'max_target_vertices': args.vertices, 'counts': dict(counts),
                      'seconds': time.monotonic() - start}), flush=True)


if __name__ == '__main__':
    main()
