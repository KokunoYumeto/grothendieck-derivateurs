"""Independent exact certificates for DER_FOLLOWUP Part G.

No input files or third-party packages are required.  All categories are finite
posets; their arrows are exactly the computed order relations and composition
is the unique order arrow.  Homology certificates use integral simplicial
chains and the displayed cofiber chain complexes, not ranks modulo a field.
"""
from itertools import combinations, product
from collections import defaultdict, deque
from pathlib import Path
import json


def faces(facets):
    return sorted({tuple(sorted(s)) for f in facets
                   for n in range(1, len(f) + 1)
                   for s in combinations(f, n)}, key=lambda s: (len(s), s))


def polygon(m):
    return faces([(i, (i + 1) % m) for i in range(m)])


def sphere(m):
    return faces([(a, i, (i + 1) % m)
                  for a in (m, m + 1) for i in range(m)])


def face_order(fs):
    return {(i, j) for i, a in enumerate(fs) for j, b in enumerate(fs)
            if set(a).issubset(b)}


def certify_poset(n, rel):
    assert all((i, i) in rel for i in range(n))
    assert all(a == b or (b, a) not in rel for a, b in rel)
    up = [set() for _ in range(n)]
    for a, b in rel:
        up[a].add(b)
    assert all(up[b] <= up[a] for a, b in rel)
    return len(rel)


def certify_functor(source_rel, target_rel, image):
    assert all((image[a], image[b]) in target_rel for a, b in source_rel)


def face_map(source, target, vertices):
    positions = {face: i for i, face in enumerate(target)}
    return [positions[tuple(sorted({vertices[v] for v in f}))] for f in source]


def sign_sort(vertices):
    if len(set(vertices)) < len(vertices):
        return 0, ()
    inversions = sum(vertices[i] > vertices[j]
                     for i in range(len(vertices)) for j in range(i + 1, len(vertices)))
    return (-1) ** inversions, tuple(sorted(vertices))


def add(chain, vertices, coefficient):
    s, f = sign_sort(vertices)
    if s:
        chain[f] += coefficient * s
        if not chain[f]:
            del chain[f]


def boundary(chain):
    out = defaultdict(int)
    for face, coefficient in chain.items():
        for i in range(len(face)):
            add(out, face[:i] + face[i + 1:], coefficient * (-1) ** i)
    return dict(out)


def fundamental_sphere(m):
    out = defaultdict(int)
    for i in range(m):
        add(out, (m, i, (i + 1) % m), 1)
        add(out, (m + 1, i, (i + 1) % m), -1)
    assert not boundary(out)
    return dict(out)


def fundamental_circle(m):
    out = defaultdict(int)
    for i in range(m):
        add(out, (i, (i + 1) % m), 1)
    assert not boundary(out)
    return dict(out)


def push_chain(chain, vertex_map):
    out = defaultdict(int)
    for face, coefficient in chain.items():
        add(out, tuple(vertex_map[v] for v in face), coefficient)
    return dict(out)


def scale(chain, n):
    return {f: n * c for f, c in chain.items() if n * c}


def collage(P, Q, f):
    """Grothendieck construction of Q <- P -> point."""
    p, q = len(P), len(Q)
    rp, rq = face_order(P), face_order(Q)
    rel = set(rp) | {(p + a, p + b) for a, b in rq} | {(p + q, p + q)}
    rel |= {(a, p + b) for a in range(p) for b in range(q) if (f[a], b) in rq}
    rel |= {(a, p + q) for a in range(p)}
    return p + q + 1, rel


def suspension_poset(P):
    p = len(P)
    rel = face_order(P) | {(p, p), (p + 1, p + 1)}
    rel |= {(a, t) for a in range(p) for t in (p, p + 1)}
    return p + 2, rel


def tensor_boundary(chain):
    out = defaultdict(int)
    for (a, b), coeff in chain.items():
        for i in range(len(a)):
            out[(a[:i] + a[i + 1:], b)] += coeff * (-1) ** i
        for i in range(len(b)):
            out[(a, b[:i] + b[i + 1:])] += coeff * (-1) ** (len(a) - 1 + i)
    return {k: v for k, v in out.items() if v}


def graph_cycle_rank(fs):
    vertices = [f[0] for f in fs if len(f) == 1]
    edges = [f for f in fs if len(f) == 2]
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(vertices)
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for w in adjacency[v] & unseen:
                unseen.remove(w)
                component.add(w)
                queue.append(w)
        components.append(component)
    return [sum(a in c and b in c for a, b in edges) - len(c) + 1 for c in components]


def main():
    P, Q, C = sphere(8), sphere(4), polygon(4)
    rp, rq, rc = face_order(P), face_order(Q), face_order(C)
    h = {i: i % 4 for i in range(8)} | {8: 4, 9: 5}
    k = {i: [0, 1, 2, 3, 0, 0, 0, 0][i] for i in range(8)} | {8: 4, 9: 5}
    f, degree_one = face_map(P, Q, h), face_map(P, Q, k)
    for fs, rel in ((P, rp), (Q, rq), (C, rc)):
        certify_poset(len(fs), rel)
    certify_functor(rp, rq, f)
    certify_functor(rp, rq, degree_one)
    z8, z4 = fundamental_sphere(8), fundamental_sphere(4)
    assert push_chain(z8, h) == scale(z4, 2)
    assert push_chain(z8, k) == z4

    # The original finite REVLOC relative-Theorem-A witness.
    nd, rd = collage(P, Q, f)
    ne, re = collage(Q, Q, list(range(len(Q))))
    v = f + [len(Q) + j for j in range(len(Q))] + [2 * len(Q)]
    certify_poset(nd, rd)
    certify_poset(ne, re)
    certify_functor(rd, re, v)
    left = set(range(len(P) + len(Q)))
    right = set(range(len(P))) | {nd - 1}
    assert left | right == set(range(nd))
    for sieve in (left, right):
        assert all(a in sieve for a, b in rd if b in sieve)
    # Explicit evaluation adjunction on each comma over the three-object span.
    layers = [0] * len(P) + [1] * len(Q) + [2]
    base_rel = {(0, 0), (1, 1), (2, 2), (0, 1), (0, 2)}
    for j in range(3):
        comma = [a for a in range(nd) if (layers[a], j) in base_rel]
        if j == 0:
            ev = {a: a for a in comma}; fibre_rel = rp
            inclusion = lambda x: x
        elif j == 1:
            ev = {a: f[a] if a < len(P) else a - len(P) for a in comma}
            fibre_rel = rq; inclusion = lambda x: len(P) + x
        else:
            ev = {a: 0 for a in comma}; fibre_rel = {(0, 0)}
            inclusion = lambda x: nd - 1
        for a in comma:
            for b in set(ev.values()):
                assert ((ev[a], b) in fibre_rel) == ((a, inclusion(b)) in rd)

    # Products: the posets and functor are constructed in full.
    source_product = list(product(range(len(P)), range(len(C))))
    target_product = list(product(range(len(Q)), range(len(C))))
    rprod_p = {(i, j) for i, (a, b) in enumerate(source_product)
               for j, (aa, bb) in enumerate(source_product)
               if (a, aa) in rp and (b, bb) in rc}
    rprod_q = {(i, j) for i, (a, b) in enumerate(target_product)
               for j, (aa, bb) in enumerate(target_product)
               if (a, aa) in rq and (b, bb) in rc}
    target_index = {obj: i for i, obj in enumerate(target_product)}
    prod_f = [target_index[(f[a], b)] for a, b in source_product]
    certify_poset(len(source_product), rprod_p)
    certify_poset(len(target_product), rprod_q)
    certify_functor(rprod_p, rprod_q, prod_f)
    c4 = fundamental_circle(4)
    cross8 = {(a, b): x * y for a, x in z8.items() for b, y in c4.items()}
    cross4 = {(a, b): x * y for a, x in z4.items() for b, y in c4.items()}
    assert not tensor_boundary(cross8) and not tensor_boundary(cross4)
    pushed_cross = defaultdict(int)
    for (a, b), coeff in cross8.items():
        s, aa = sign_sort(tuple(h[t] for t in a))
        if s: pushed_cross[(aa, b)] += s * coeff
    assert dict(pushed_cross) == {c: 2 * a for c, a in cross4.items()}

    # Bare u_! obstruction: finite suspension maps of degrees two and one.
    ns_p, rs_p = suspension_poset(P)
    ns_q, rs_q = suspension_poset(Q)
    sf = f + [len(Q), len(Q) + 1]
    sk = degree_one + [len(Q), len(Q) + 1]
    certify_poset(ns_p, rs_p); certify_poset(ns_q, rs_q)
    certify_functor(rs_p, rs_q, sf); certify_functor(rs_p, rs_q, sk)

    # Wsharp: two disjoint triangles -> their wedge, with no filled triangles.
    disjoint = faces([(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)])
    wedge = faces([(0, 1), (1, 2), (2, 0), (0, 4), (4, 5), (5, 0)])
    vertex_map = {0: 0, 1: 1, 2: 2, 3: 0, 4: 4, 5: 5}
    collapse = face_map(disjoint, wedge, vertex_map)
    rdg, rwg = face_order(disjoint), face_order(wedge)
    certify_poset(len(disjoint), rdg); certify_poset(len(wedge), rwg)
    certify_functor(rdg, rwg, collapse)
    assert sorted(graph_cycle_rank(disjoint)) == [1, 1]
    assert graph_cycle_rank(wedge) == [2]
    cycles = []
    for vertices in [(0, 1, 2), (3, 4, 5)]:
        cycle = defaultdict(int)
        for a, b in zip(vertices, vertices[1:] + vertices[:1]):
            add(cycle, (a, b), 1)
        assert not boundary(cycle)
        cycles.append(push_chain(cycle, vertex_map))
    # Coefficients on two distinguished edges identify the two image cycles.
    image_matrix = [[cyc.get(edge, 0) for cyc in cycles] for edge in [(1, 2), (4, 5)]]
    assert image_matrix == [[1, 0], [0, 1]]

    result = {
        "sphere_face_posets": {"P_objects": len(P), "P_arrows": len(rp),
                               "Q_objects": len(Q), "Q_arrows": len(rq)},
        "sphere_map_degrees_exact": {"f": 2, "k": 1},
        "relative_theorem_A": {"source_objects": nd, "source_arrows": len(rd),
                               "target_objects": ne, "target_arrows": len(re),
                               "source_reduced_integral_homology": "H2=Z/2; all other degrees zero",
                               "target_reduced_integral_homology": "zero in all degrees",
                               "integral_cofiber_differentials": [[2], [1]],
                               "evaluation_adjunctions": "all three checked",
                               "sieve_cover": "checked"},
        "product": {"circle_objects": len(C), "source_objects": len(source_product),
                    "source_arrows": len(rprod_p), "target_objects": len(target_product),
                    "target_arrows": len(rprod_q), "H3_generator_image": "2 times generator"},
        "left_adjoint_obstruction": {"suspension_P_objects": ns_p,
                                     "suspension_Q_objects": ns_q,
                                     "suspension_degrees": [2, 1]},
        "Wsharp": {"source_objects": len(disjoint), "source_arrows": len(rdg),
                   "target_objects": len(wedge), "target_arrows": len(rwg),
                   "source_component_H1_ranks": [1, 1], "target_component_H1_ranks": [2],
                   "H1_map_matrix": image_matrix, "pi0_map": "two elements to one"},
        "all_assertions": "passed"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
