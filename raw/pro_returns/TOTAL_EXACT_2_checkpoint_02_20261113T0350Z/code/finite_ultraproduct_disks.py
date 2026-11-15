"""Exact finite certificates for the disk ultraproduct obstruction.

This constructs the explicit disks in notes/finite_compactness_route.md.
It is not a search through finite categories. No finite execution proves
the ultraproduct assertion; that assertion has a separate universal proof.

Only integer arithmetic and combinatorial elementary collapses are used.
The serialized certificates are replayed against freshly built boundary
matrices. Run from any working directory; outputs are beside this script.
"""
from collections import defaultdict, deque
from hashlib import sha256
from itertools import combinations, permutations
from pathlib import Path
import json


def parity(perm):
    return -1 if sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


def build(n):
    assert n >= 0
    vertex = lambda i, j: 3 * i + (j % 3)
    center = 3 * (n + 1)
    oriented = []
    for i in range(n):
        for j in range(3):
            a, b = vertex(i, j), vertex(i, j + 1)
            c, d = vertex(i + 1, j + 1), vertex(i + 1, j)
            oriented.extend(((a, b, c), (a, c, d)))
    for j in range(3):
        oriented.append((vertex(n, j), vertex(n, j + 1), center))
    faces = set()
    for triangle in oriented:
        for size in (1, 2, 3):
            faces.update(tuple(sorted(face)) for face in combinations(triangle, size))
    faces = sorted(faces, key=lambda face: (len(face), face))
    face_index = {face: index for index, face in enumerate(faces)}
    edges = set()
    triangles = set()
    filling_by_triangle = {}
    for triangle in oriented:
        top = face_index[tuple(sorted(triangle))]
        for perm in permutations(range(3)):
            flag = (
                face_index[(triangle[perm[0]],)],
                face_index[tuple(sorted((triangle[perm[0]], triangle[perm[1]])))],
                top,
            )
            assert flag not in filling_by_triangle
            triangles.add(flag)
            filling_by_triangle[flag] = parity(perm)
            edges.update(combinations(flag, 2))
    edges, triangles = sorted(edges), sorted(triangles)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d2 = [
        {edge_index[(b, c)]: 1, edge_index[(a, c)]: -1, edge_index[(a, b)]: 1}
        for a, b, c in triangles
    ]
    outer = defaultdict(int)
    for j in range(3):
        a, b = j, (j + 1) % 3
        e = face_index[tuple(sorted((a, b)))]
        outer[edge_index[(face_index[(a,)], e)]] += 1
        outer[edge_index[(face_index[(b,)], e)]] -= 1
    outer = {e: c for e, c in outer.items() if c}
    filling = [filling_by_triangle[triangle] for triangle in triangles]
    return faces, edges, triangles, d2, outer, filling


def make_certificate(n):
    faces, edges, triangles, d2, outer, filling = build(n)
    incident = [set() for _ in edges]
    for t, boundary in enumerate(d2):
        for e in boundary:
            incident[e].add(t)
    assert all(len(cofaces) in (1, 2) for cofaces in incident)
    assert {e for e, cofaces in enumerate(incident) if len(cofaces) == 1} == set(outer)
    active_t = set(range(len(triangles)))
    active_e = set(range(len(edges)))
    queue = deque(e for e, cofaces in enumerate(incident) if len(cofaces) == 1)
    triangle_collapses = []
    while queue:
        e = queue.popleft()
        if e not in active_e or len(incident[e]) != 1:
            continue
        t = next(iter(incident[e]))
        assert t in active_t
        active_t.remove(t)
        active_e.remove(e)
        triangle_collapses.append((t, e))
        for other in d2[t]:
            incident[other].remove(t)
            if other in active_e and len(incident[other]) == 1:
                queue.append(other)
    assert not active_t
    at_vertex = [set() for _ in faces]
    for e in active_e:
        for v in edges[e]:
            at_vertex[v].add(e)
    active_v = set(range(len(faces)))
    queue = deque(v for v, adjacent in enumerate(at_vertex) if len(adjacent) == 1)
    tree_collapses = []
    while queue:
        v = queue.popleft()
        if v not in active_v or len(at_vertex[v]) != 1:
            continue
        e = next(iter(at_vertex[v]))
        active_e.remove(e)
        active_v.remove(v)
        tree_collapses.append((v, e))
        for endpoint in edges[e]:
            at_vertex[endpoint].remove(e)
            if endpoint in active_v and len(at_vertex[endpoint]) == 1:
                queue.append(endpoint)
    assert not active_e and len(active_v) == 1
    return {
        "n": n,
        "triangle_collapses": triangle_collapses,
        "tree_collapses": tree_collapses,
        "remaining_vertex": next(iter(active_v)),
        "filling": filling,
        "boundary": sorted(outer.items()),
    }


def replay(certificate):
    n = certificate["n"]
    faces, edges, triangles, d2, outer, expected_filling = build(n)
    assert (len(faces), len(edges), len(triangles)) == (18 * n + 13, 54 * n + 30, 36 * n + 18)
    assert certificate["filling"] == expected_filling
    assert dict(certificate["boundary"]) == outer and len(outer) == 6
    boundary = defaultdict(int)
    for coefficient, column in zip(certificate["filling"], d2):
        assert coefficient in (-1, 1)
        for edge, value in column.items():
            boundary[edge] += coefficient * value
    assert {e: c for e, c in boundary.items() if c} == outer
    boundary_boundary = defaultdict(int)
    for e, coefficient in outer.items():
        a, b = edges[e]
        boundary_boundary[b] += coefficient
        boundary_boundary[a] -= coefficient
    assert not any(boundary_boundary.values())
    active_t = set(range(len(triangles)))
    active_e = set(range(len(edges)))
    active_v = set(range(len(faces)))
    cofaces = defaultdict(set)
    for t, column in enumerate(d2):
        for e in column:
            cofaces[e].add(t)
    for t, e in certificate["triangle_collapses"]:
        assert t in active_t and e in active_e
        assert cofaces[e] & active_t == {t}
        assert d2[t][e] in (-1, 1)
        active_t.remove(t)
        active_e.remove(e)
    assert not active_t
    assert len(active_e) == len(faces) - 1
    adjacent = defaultdict(set)
    for e in active_e:
        for v in edges[e]:
            adjacent[v].add(e)
    for v, e in certificate["tree_collapses"]:
        assert v in active_v and e in active_e
        assert adjacent[v] & active_e == {e}
        assert v in edges[e]
        active_v.remove(v)
        active_e.remove(e)
    assert not active_e and active_v == {certificate["remaining_vertex"]}
    return {
        "n": n,
        "original_disk_vertices_edges_triangles": [3 * n + 4, 9 * n + 6, 6 * n + 3],
        "nerve_vertices_edges_triangles": [len(faces), len(edges), len(triangles)],
        "fixed_boundary_support": len(outer),
        "integer_boundary_verified": True,
        "unit_pivots_replayed": len(certificate["triangle_collapses"]),
        "tree_collapses_replayed": len(certificate["tree_collapses"]),
        "integral_boundary_ranks_d1_d2": [len(faces) - 1, len(triangles)],
        "unique_filling_support_and_l1_norm": len(triangles),
        "collapse_to_one_vertex_verified": True,
    }


def main():
    chosen_n = (0, 1, 2, 3, 8, 32)
    certificates = [make_certificate(n) for n in chosen_n]
    payload = json.dumps(certificates, separators=(",", ":"), sort_keys=True).encode()
    path = Path(__file__).with_name("finite_ultraproduct_disks_certificates.json")
    path.write_bytes(payload)
    for certificate in json.loads(path.read_text()):
        print(json.dumps(replay(certificate), sort_keys=True))
    print(json.dumps({"certificate_file": path.name, "bytes": len(payload), "sha256": sha256(payload).hexdigest()}))
    print("Scope: exact finite certificate replay for the six listed N; the all-N formulas and ultraproduct conclusion are proved in notes/finite_compactness_route.md.")


if __name__ == "__main__":
    main()
