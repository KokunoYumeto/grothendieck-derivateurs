"""The 2-skeleton K of Poincare's dodecahedral space (Kirby-Scharlemann, Description 5).

Opposite faces of a regular dodecahedron are identified by pushing each face through
the solid and twisting it by 2*pi/10 about the axis of the push, right-hand screw.
The quotient is a CW complex with one 3-cell; removing an open ball from the 3-cell
leaves a space that deformation retracts onto the 2-skeleton K. This script counts
the cells of K and computes pi_1(K) from its cell structure (spanning tree in the
1-skeleton, one relator per 2-cell), then the order of that group by coset enumeration.
Floating-point geometry is used only to match vertices (tolerance 1e-9).
"""
import math
from itertools import product

phi = (1 + 5 ** 0.5) / 2
V = [p for p in product((1, -1), repeat=3)]
for s1, s2 in product((1, -1), repeat=2):
    V += [(0, s1 / phi, s2 * phi), (s1 / phi, s2 * phi, 0), (s2 * phi, 0, s1 / phi)]
V = [tuple(float(c) for c in v) for v in V]
assert len(V) == 20

dot = lambda u, v: sum(a * b for a, b in zip(u, v))
sub = lambda u, v: tuple(a - b for a, b in zip(u, v))
add = lambda u, v: tuple(a + b for a, b in zip(u, v))
scal = lambda c, u: tuple(c * a for a in u)
cross = lambda u, v: (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
norm = lambda u: math.sqrt(dot(u, u))

# face normals: vertices of the dual icosahedron
N = []
for s1, s2 in product((1, -1), repeat=2):
    N += [(0, s1 * phi, s2), (s2, 0, s1 * phi), (s1 * phi, s2, 0)]
N = [scal(1 / norm(n), n) for n in N]


def face_of(n):
    d = [dot(v, n) for v in V]
    m = max(d)
    idx = [i for i in range(20) if abs(d[i] - m) < 1e-9]
    assert len(idx) == 5
    c = scal(1 / 5, tuple(sum(V[i][t] for i in idx) for t in range(3)))
    e1 = sub(V[idx[0]], c)
    e1 = scal(1 / norm(e1), e1)
    e2 = cross(n, e1)              # (e1, e2, n) right-handed: counterclockwise seen from outside
    idx.sort(key=lambda i: math.atan2(dot(sub(V[i], c), e2), dot(sub(V[i], c), e1)))
    return idx, m


faces = [face_of(n) for n in N]
h = faces[0][1]


def rot(axis, ang, x):
    """Rotation by ang about the unit vector axis (right-hand rule), Rodrigues formula."""
    c, s = math.cos(ang), math.sin(ang)
    return add(add(scal(c, x), scal(s, cross(axis, x))), scal((1 - c) * dot(axis, x), axis))


def vid(x):
    js = [j for j in range(20) if norm(sub(V[j], x)) < 1e-9]
    assert len(js) == 1, x
    return js[0]


# pairing map for the face with outward normal n: push along -n, twist +36 deg about -n
pair = {}
for fi, n in enumerate(N):
    minus_n = scal(-1, n)
    fj = [j for j in range(12) if norm(add(N[j], n)) < 1e-9][0]
    images = {}
    for i in faces[fi][0]:
        y = rot(minus_n, math.pi / 5, add(V[i], scal(-2 * h, n)))
        images[i] = vid(y)
    assert set(images.values()) == set(faces[fj][0])
    pair[fi] = (fj, images)
for fi in range(12):           # consistency: the pairing of the opposite face is the inverse
    fj, m = pair[fi]
    assert all(pair[fj][1][m[i]] == i for i in m)
print("face pairings defined, vertex-to-vertex, mutually inverse: True")

# union-find on vertices and on directed edges
parent = {}


def find(x):
    parent.setdefault(x, x)
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(x, y):
    parent[find(x)] = find(y)


dir_edges = set()
for idx, _ in faces:
    for t in range(5):
        a, b = idx[t], idx[(t + 1) % 5]
        dir_edges |= {("e", a, b), ("e", b, a)}
for fi in range(12):
    fj, m = pair[fi]
    idx = faces[fi][0]
    for t in range(5):
        a, b = idx[t], idx[(t + 1) % 5]
        union(("v", a), ("v", m[a]))
        union(("e", a, b), ("e", m[a], m[b]))
        union(("e", b, a), ("e", m[b], m[a]))

vclasses = {find(("v", i)) for i in range(20)}
dclasses = {find(e) for e in dir_edges}
assert all(find(("e", a, b)) != find(("e", b, a)) for (_, a, b) in dir_edges)
nV, nE, nF = len(vclasses), len(dclasses) // 2, 6
print(f"cells of K: {nV} vertices, {nE} edges, {nF} faces; chi(K) = {nV - nE + nF}")
print("vertex class sizes:", sorted(sum(1 for i in range(20) if find(('v', i)) == c) for c in vclasses))

# 1-skeleton of K, spanning tree, generators
gen_of = {}                       # directed edge class -> (generator index, +1/-1)
edges = []
for (_, a, b) in sorted(dir_edges):
    c, cr = find(("e", a, b)), find(("e", b, a))
    if c in gen_of or cr in gen_of:
        continue
    k = len(edges)
    edges.append((find(("v", a)), find(("v", b))))
    gen_of[c], gen_of[cr] = (k, 1), (k, -1)
tree, seen = set(), {next(iter(vclasses))}
changed = True
while changed:
    changed = False
    for k, (u, w) in enumerate(edges):
        if (u in seen) != (w in seen):
            tree.add(k)
            seen |= {u, w}
            changed = True
assert seen == vclasses and len(tree) == nV - 1
nongen = [k for k in range(nE) if k not in tree]

from sympy.combinatorics.free_groups import free_group
F, *x = free_group(" ".join(f"x{k}" for k in nongen))
gx = dict(zip(nongen, x))
rels, done = [], set()
for fi in range(12):
    fj, _ = pair[fi]
    if fj in done:
        continue
    done.add(fi)
    idx, w = faces[fi][0], F.identity
    for t in range(5):
        k, s = gen_of[find(("e", idx[t], idx[(t + 1) % 5]))]
        if k not in tree:
            w = w * gx[k] ** s
    rels.append(w)
print(f"presentation of pi_1(K): {len(nongen)} generators, {len(rels)} relators")
for r in rels:
    print("  ", r)

from sympy.combinatorics.fp_groups import FpGroup
from sympy import Matrix
Kgrp = FpGroup(F, rels)
print("order of pi_1(K) by coset enumeration:", Kgrp.order())
M = Matrix([[r.exponent_sum(g) for g in x] for r in rels])
print("abelianization matrix determinant:", M.det())
