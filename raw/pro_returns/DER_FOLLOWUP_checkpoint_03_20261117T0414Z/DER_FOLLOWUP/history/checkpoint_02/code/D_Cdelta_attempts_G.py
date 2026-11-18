#!/usr/bin/env python3
"""Verify the finite obstruction to a globally ordered positive-basis ansatz.

This does not decide the C_delta FreeMon comparison question.
"""
from itertools import combinations
from pathlib import Path
import json

vertices = frozenset(range(1, 6))
edges = (frozenset((1, 3, 4)), frozenset((1, 2, 5)))

def subsets(items):
    items = sorted(items)
    for n in range(len(items) + 1):
        for sub in combinations(items, n):
            yield frozenset(sub)

def delta(sub):
    return 2 * len(sub) - 3 * sum(edge <= sub for edge in edges)

positivity = all(delta(sub) > 0 for sub in subsets(vertices) if sub)
closed = []
for edge in edges:
    extensions = [sub for sub in subsets(vertices) if edge < sub]
    closed.append(all(delta(sub) > delta(edge) for sub in extensions))
assert positivity and all(closed)

# Coordinate order U1,...,U5,V1,...,V5.  Each row is the edge equation
# U_b-U_a+V_c-V_a=0.  Their difference equals two strictly positive gaps
# when U increases and V decreases in the supplied linear order.
rows = []
for edge in edges:
    a, b, c = sorted(edge)
    row = [0] * 10
    row[b - 1] += 1
    row[a - 1] -= 1
    row[5 + c - 1] += 1
    row[5 + a - 1] -= 1
    rows.append(row)
difference = [x - y for x, y in zip(*rows)]
expected = [0, -1, 1, 0, 0, 0, 0, 0, 1, -1]
assert difference == expected

result = {
    "vertices": sorted(vertices),
    "edges": [sorted(edge) for edge in edges],
    "delta_full": delta(vertices),
    "all_nonempty_induced_subobjects_positive": positivity,
    "both_W_images_strictly_closed": closed,
    "edge_relation_rows": rows,
    "row_difference": difference,
    "contradiction": "(U3-U2)+(V4-V5)=0 with both summands strictly positive",
    "scope": "Refutes only globally nested U-prefixes/V-suffixes; not arbitrary positive bases.",
    "assertions": "passed",
}
root = Path(__file__).resolve().parents[1]
(root / "code/outputs/D_Cdelta_attempts_G.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
