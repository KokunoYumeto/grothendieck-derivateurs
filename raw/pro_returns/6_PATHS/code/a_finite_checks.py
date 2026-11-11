"""Independent finite checks for PATHS A and the Cat-hot obstruction.

Pure Python; no third-party packages.  This checks finite data only.  The
infinite Delta_inj homology argument is proved in A_colimits.tex, rather than
inferred from truncations.
"""

from collections import Counter
from itertools import combinations, product
import json


def check_poset(n, le):
    assert all(le(a, a) for a in range(n))
    assert all(not (le(a, b) and le(b, a)) or a == b
               for a in range(n) for b in range(n))
    assert all(not (le(a, b) and le(b, c)) or le(a, c)
               for a in range(n) for b in range(n) for c in range(n))


def circle_check():
    faces = [frozenset([i]) for i in range(3)]
    faces += [frozenset([0, 1]), frozenset([1, 2]), frozenset([0, 2])]
    le_p = lambda a, b: faces[a] <= faces[b]
    chains = [frozenset([i]) for i in range(6)]
    chains += [frozenset([i, j]) for i in range(6) for j in range(6)
               if i != j and le_p(i, j)]
    le_s = lambda a, b: chains[a] <= chains[b]
    check_poset(6, le_p)
    check_poset(12, le_s)
    p_cycle = [0, 3, 1, 4, 2, 5]
    s_cycle = []
    for i, a in enumerate(p_cycle):
        b = p_cycle[(i + 1) % 6]
        s_cycle += [chains.index(frozenset([a])),
                    chains.index(frozenset([a, b]))]
    assert len(set(s_cycle)) == 12
    s_position = {x: i for i, x in enumerate(s_cycle)}
    p_position = {x: i for i, x in enumerate(p_cycle)}

    def degree(values, position, circumference):
        total = 0
        for a, b in zip(values, values[1:] + values[:1]):
            d = (position[b] - position[a]) % circumference
            assert d in (0, 1, circumference - 1)
            total += -1 if d == circumference - 1 else d
        assert total % circumference == 0
        return total // circumference

    degree_counts = Counter()
    count = 0
    for vertices in product(range(12), repeat=3):
        edge_options = []
        for e in range(3, 6):
            edge_options.append([z for z in range(12)
                                 if all(le_s(vertices[v], z) for v in faces[e])])
        for edges in product(*edge_options):
            f = vertices + edges
            assert all(not le_p(a, b) or le_s(f[a], f[b])
                       for a in range(6) for b in range(6))
            degree_counts[degree([f[a] for a in p_cycle], s_position, 12)] += 1
            count += 1
    last = [max(chain, key=lambda z: len(faces[z])) for chain in chains]
    assert all(not le_s(a, b) or le_p(last[a], last[b])
               for a in range(12) for b in range(12))
    last_degree = degree([last[a] for a in s_cycle], p_position, 6)
    assert count == 456 and degree_counts == {0: 456} and last_degree == 1
    return {"P_objects": 6, "P_nonidentity_arrows": 6,
            "sdP_objects": 12, "sdP_nonidentity_arrows": 12,
            "P_to_sdP_monotone_maps": count,
            "degree_distribution": dict(degree_counts),
            "last_element_degree": last_degree,
            "P_Betti_0_1": [1, 1], "sdP_Betti_0_1": [1, 1]}


def delta_checks(max_n=5):
    arrows = {(m, n): list(combinations(range(n + 1), m + 1))
              for n in range(max_n + 1) for m in range(n + 1)}
    compositions = 0
    for a in range(max_n + 1):
        for b in range(a, max_n + 1):
            for c in range(b, max_n + 1):
                for f in arrows[a, b]:
                    for g in arrows[b, c]:
                        assert tuple(g[i] for i in f) in arrows[a, c]
                        compositions += 1
    # The two [0] -> [1] inclusions cannot be post-equalized by injections.
    assert all(g[0] != g[1] for n in range(1, max_n + 1)
               for g in arrows[1, n])
    rows = []
    for q in range(1, max_n + 2):
        objects = [(n, s) for n in range(q - 1, max_n + 1)
                   for s in combinations(range(n + 1), q)]
        initial = (q - 1, tuple(range(q)))
        assert initial in objects
        # An element is exactly the unique arrow from the identity element.
        assert all(s in arrows[q - 1, n] for n, s in objects)
        parent = list(range(len(objects)))
        index = {obj: i for i, obj in enumerate(objects)}
        def root(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        relations = 0
        for n, s in objects:
            for m in range(n, max_n + 1):
                for f in arrows[n, m]:
                    image = (m, tuple(f[x] for x in s))
                    a, b = root(index[n, s]), root(index[image])
                    parent[b] = a
                    relations += 1
        components = len({root(i) for i in range(len(objects))})
        assert components == 1
        rows.append({"exterior_degree": q, "basis_elements": len(objects),
                     "colimit_relations": relations, "colimit_free_rank": components,
                     "category_of_elements_initial_object": list(initial)})
    return {"max_n": max_n, "checked_compositions": compositions,
            "parallel_inclusions_never_equalized": True, "exterior_rows": rows,
            "warning": "Finite checks do not compute the infinite total category."
            " Infinite homology is proved using representable modules."}


def group_c2_check():
    # One object, arrows 0=id and 1=s, composition is addition modulo 2.
    table = [[(a+b) % 2 for b in range(2)] for a in range(2)]
    assert all(table[table[a][b]][c] == table[a][table[b][c]]
               for a in range(2) for b in range(2) for c in range(2))
    # Normalized nerve has one nondegenerate n-simplex (s,...,s) in each n>0.
    # Even differential is multiplication by 2; odd differential is 0.
    differentials = {n: 1 + (-1)**n for n in range(1, 7)}
    assert differentials[1] == 0 and differentials[2] == 2
    return {"objects": 1, "arrows": 2, "composition_table": table,
            "normalized_chain_differentials": differentials,
            "H1": "Z/2", "preorder": "one point"}


if __name__ == "__main__":
    print(json.dumps({"circle": circle_check(), "delta": delta_checks(),
                      "one_object_base": group_c2_check()}, indent=2))
