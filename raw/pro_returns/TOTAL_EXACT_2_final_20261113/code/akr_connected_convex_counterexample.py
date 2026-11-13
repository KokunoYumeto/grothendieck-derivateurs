"""Connected generic counterexample to unrestricted beta convexity.

This graph diagram is NOT asserted to occur among actual C.1 arrows.
It uses s45,n3 (k11), and convex half-cycle paths of length46.
"""
from pathlib import Path
import json
from akr_connected_convex_search import distances, glue, relation, edges_of

L, n, k = 46, 3, 11
s = 4 * k + 1
size = 2 * L + 2
T = [{(v - 1) % size, (v + 1) % size} for v in range(size)]
f = tuple(range(L + 1))
g = tuple(range(L + 1, 2 * L + 2))
dd = [distances(T, v) for v in range(size)]
for image in (set(f), set(g)):
    for u in image:
        for v in image:
            assert all(dd[u][w] + dd[w][v] != dd[u][v]
                       for w in set(range(size)) - image)
assert all((j in T[i]) == (g[j] in T[g[i]])
           for i in range(L + 1) for j in range(L + 1))
fixed, paths, active = relation(f, g)
assert not fixed and len(paths) == L + 1 and all(len(p) == 2 for p in paths)
assert k >= n >= max(map(len, paths))
assert s % (3 * n) == 0 and s // (3 * n) == 5
Z, alphas = glue(T, f, g, k)
index_cycle = list(range(2 * k + 1)) + list(range(4 * k, 2 * k, -1)) + [0]
assert len(index_cycle) == s + 1
bridge_path = [s * (0 if step % 2 == 0 else L) + column
               for step, column in enumerate(index_cycle)]
assert all(v in Z[u] for u, v in zip(bridge_path, bridge_path[1:]))
start, end = alphas[0][f[0]], alphas[0][f[-1]]
assert bridge_path[0] == start and bridge_path[-1] == end
assert len(bridge_path) - 1 == s < dd[f[0]][f[-1]] == L
image = set(alphas[0])
assert any(v not in image for v in bridge_path)
assert distances(Z, start)[end] == s
assert len(distances(Z, start)) == len(Z)
result = {
    'scope': 'generic finite connected graph diagram; not shown to occur in C.1',
    'parameters': {'L': L, 'n': n, 'k': k, 's': s, 's_over_3n': s // (3*n)},
    'source': {'vertices': L + 1, 'edges': L, 'graph': 'path'},
    'old_target': {'vertices': size, 'edges': size, 'graph': 'cycle'},
    'f': f, 'g': g,
    'strong_convexity_of_both_source_images': True,
    'component_maps_injective': True,
    'nontrivial_point_path_sizes': sorted(set(map(len, paths))),
    'new_target': {'vertices': len(Z), 'edges': len(edges_of(Z)), 'components': 1},
    'copy': 0, 'old_vertices': [f[0], f[-1]], 'old_distance': L,
    'new_vertices': [start, end], 'new_distance': s,
    'explicit_outside_bridge_path': bridge_path,
    'copy_vertex_set': sorted(image),
}
print(json.dumps(result, indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2))
