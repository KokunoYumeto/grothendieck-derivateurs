"""Exact generic counterexample to ordering every repaired necklace.

The increasing maps below are not asserted to occur among actual C.1
arrows. They show that the sufficiently-large-k hypothesis in the generic
ordered-necklace theorem cannot be replaced by k>=the point-path bound.
"""
from pathlib import Path
import json
from akr_connected_convex_search import glue, relation

k, n = 11, 3
d, s = 2 * k, 4 * k + 1
M = d * (d + 1)
f = tuple(2 * r for r in range(M + 1))
g = tuple(2 * r + s for r in range(M + 1))
target_size = 2 * M + s + 1
assert all(x < y for x, y in zip(f, f[1:]))
assert all(x < y for x, y in zip(g, g[1:]))
fixed, paths, active = relation(f, g)
assert not fixed and len(paths) == M + 1 and all(len(p) == 2 for p in paths)
assert k >= n >= 2 and s % (3*n) == 0 and s // (3*n) == 5
_, alphas = glue([set() for _ in range(target_size)], f, g, k)
rows = []
previous = M
cycle = []
for i in range(s):
    current = previous - d if i <= d else previous + d + 1
    assert 0 <= current <= M
    old_in = f[previous] if i <= d else g[previous]
    old_out = g[current] if i <= d else f[current]
    assert old_out == old_in + 1
    incoming = alphas[i][old_in]
    outgoing = alphas[i][old_out]
    if i == 0:
        cycle.append(incoming)
    else:
        assert cycle[-1] == incoming
    cycle.append(outgoing)
    rows.append({'copy': i, 'source_in': previous, 'source_out': current,
                 'old_smaller': old_in, 'old_larger': old_out,
                 'target_smaller_required': incoming, 'target_larger_required': outgoing})
    previous = current
assert previous == M and cycle[0] == cycle[-1]
assert len(set(cycle[:-1])) == s
assert len(cycle) == s + 1
result = {
    'scope': 'generic finite ordered-set diagram; not shown to occur in C.1',
    'parameters': {'k': k, 'n': n, 's': s, 'd': d, 'M': M, 's_over_3n': 5},
    'source_size': M + 1, 'old_target_size': target_size,
    'old_maps': {'f(r)': '2*r', 'g(r)': '2*r+s', 'domain': [0, M]},
    'nontrivial_point_path_sizes': [2],
    'new_target_size': len(set(v for alpha in alphas for v in alpha)),
    'strict_precedence_cycle_length': s,
    'strict_precedence_cycle': cycle,
    'strict_comparison_certificate': rows,
    'conclusion': 'No linear order on the repaired target makes every copy map increasing.',
}
print(json.dumps(result, indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2))
