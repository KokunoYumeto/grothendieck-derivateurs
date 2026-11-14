"""Exact finite certificate for the eight-step subdivided triangle prism.

The proof uses the lifted rows in the actual 25-object poset Q=c Sd^2 Delta^2.
The quotient calculation is an independent exhaustive minimality check only.
"""
from itertools import combinations, product
from collections import deque
from pathlib import Path
import json

faces = [frozenset(s) for n in range(1, 4) for s in combinations(range(3), n)]
chains = []
for n in range(1, 4):
    for s in combinations(faces, n):
        s = tuple(sorted(s, key=lambda x: (len(x), tuple(x))))
        if all(s[i] < s[i + 1] for i in range(n - 1)):
            chains.append(frozenset(s))
side = [c for c in chains if all(f <= frozenset([1, 2]) for f in c)]
assert len(chains) == 25 and len(side) == 5

def C(*strings):
    return frozenset(frozenset(map(int, s)) for s in strings)

lifted_rows = [
    [C('0'), C('0','01'), C('01'), C('1','01'), C('1')],
    [C('0'), C('0','01','012'), C('01','012'), C('1','01','012'), C('1')],
    [C('0'), C('0','012'), C('012'), C('1','012'), C('1')],
    [C('0'), C('0','012'), C('012'), C('1','12','012'), C('1','12')],
    [C('0'), C('0','012'), C('012'), C('12','012'), C('12')],
    [C('0'), C('0','012'), C('012'), C('2','12','012'), C('2','12')],
    [C('0'), C('0','012'), C('012'), C('2','012'), C('2')],
    [C('0'), C('0','02','012'), C('02','012'), C('2','02','012'), C('2')],
    [C('0'), C('0','02'), C('02'), C('2','02'), C('2')],
]
for row in lifted_rows:
    assert all(c in chains for c in row)
    assert row[0] <= row[1] and row[2] <= row[1]
    assert row[2] <= row[3] and row[4] <= row[3]
    assert row[0] == C('0') and row[4] in side
for k, (row, nxt) in enumerate(zip(lifted_rows, lifted_rows[1:])):
    if k % 2 == 0:
        assert all(a <= b for a, b in zip(row, nxt))
    else:
        assert all(b <= a for a, b in zip(row, nxt))

qmap = {c: ('e' if c in side else c) for c in chains}
verts = list(dict.fromkeys(qmap.values()))
rel = {(qmap[c], qmap[d]) for c, d in product(chains, repeat=2) if c <= d}
while True:
    new = rel | {(a,d) for a,b in rel for c,d in rel if b == c}
    if new == rel:
        break
    rel = new
assert all(a == b or (b,a) not in rel for a,b in rel)
a, b = qmap[C('0')], 'e'
paths = [(a,x,y,z,b) for x,y,z in product(verts, repeat=3)
         if (a,x) in rel and (y,x) in rel and (y,z) in rel and (b,z) in rel]
p01 = tuple(qmap[c] for c in lifted_rows[0])
p02 = tuple(qmap[c] for c in lifted_rows[-1])
index = {p:i for i,p in enumerate(paths)}
parents = {index[p01]:None}
queue = deque(parents)
while queue:
    k = queue.popleft()
    if k == index[p02]:
        break
    p = paths[k]
    for l,q in enumerate(paths):
        if l not in parents and (all((x,y) in rel for x,y in zip(p,q))
                                  or all((y,x) in rel for x,y in zip(p,q))):
            parents[l] = k
            queue.append(l)
assert index[p02] in parents
route = []
k = index[p02]
while k is not None:
    route.append(k)
    k = parents[k]
route.reverse()
assert len(route) - 1 == 8

def label(c):
    return '[' + ','.join(''.join(map(str,sorted(f)))
                          for f in sorted(c,key=lambda f:(len(f),tuple(f)))) + ']'
res = {
    'Q_objects':len(chains),
    'degenerate_side_objects':len(side),
    'lifted_rows_are_functors':True,
    'lifted_transformations': ['forward','backward'] * 4,
    'first_endpoint_fixed':True,
    'last_endpoint_stays_on_degenerate_side':True,
    'lifted_rows':[[label(c) for c in row] for row in lifted_rows],
    'quotient_vertices':len(verts),
    'fixed_endpoint_4paths':len(paths),
    'shortest_comparison_path_in_quotient':len(route)-1,
}
report = json.dumps(res,indent=2)+'\n'
print(report, end='')
Path(__file__).with_suffix('.out').write_text(report)
