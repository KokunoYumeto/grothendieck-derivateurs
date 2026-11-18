#!/usr/bin/env python3
"""Exact finite atom certificate for the voltage-cover exclusion theorem."""
import itertools
import json
from pathlib import Path


def main():
    edges = [frozenset(e) for e in ((0,3,6),(0,4,7),(0,5,8),
                                  (1,3,7),(2,4,8))]
    vertices = frozenset(range(9))
    def delta(s):
        return 2*len(s)-3*sum(e <= s for e in edges)
    checks = 0
    minima = {}
    for n in range(10):
        values = [delta(frozenset(t)) for t in itertools.combinations(range(9), n)]
        checks += len(values)
        minima[n] = min(values)
    assert delta(vertices) == 3
    assert all(minima[n] >= 3 for n in range(2, 10))
    assert minima[1] == 2
    assert all(len(e & f) <= 1 for e,f in itertools.combinations(edges,2))
    edge_union_minima = {
        n:min(len(frozenset().union(*ee)) for ee in itertools.combinations(edges,n))
        for n in range(1,6)}
    assert edge_union_minima == {1:3,2:5,3:6,4:8,5:9}
    # The p=2 cover sigma_b=(01), sigma_c=id; verify the role-constant
    # section and every strict extension of it directly.
    lifted = []
    for e in edges:
        a,b,c = sorted(e)
        lifted += [frozenset((2*a+i,2*b+(i^1),2*c+i)) for i in range(2)]
    section = frozenset([2*a for a in range(3)] +
                        [2*b+1 for b in range(3,6)] +
                        [2*c for c in range(6,9)])
    outside = sorted(set(range(18))-section)
    section_delta = lambda s: 2*len(s)-3*sum(e <= s for e in lifted)
    assert section_delta(section) == 3
    assert {e for e in lifted if e <= section} == {
        frozenset(2*v+(1 if 3 <= v < 6 else 0) for v in e) for e in edges}
    extension_min = min(section_delta(section|set(t))
                        for n in range(1,10)
                        for t in itertools.combinations(outside,n))
    assert extension_min > 3
    report = {
        'vertices': ['a0','a1','a2','b0','b1','b2','c0','c1','c2'],
        'edges': [sorted(e) for e in edges],
        'delta': 3, 'vertex_subsets_checked': checks,
        'minimum_delta_by_subset_size': minima,
        'minimum_vertices_in_edge_subfamilies': edge_union_minima,
        'proper_nonempty_strong_subsets': 'exactly the nine singletons',
        'selected_singleton_arrows': [0,1,2],
        'p2_cover_section': sorted(section),
        'p2_section_strict_extensions_checked': 511,
        'p2_section_minimum_strict_extension_delta': extension_min,
        'scope': 'The arbitrary-fiber and filtered-colimit claims are proved symbolically in the companion theorem, not inferred from this p=2 computation.'
    }
    print(json.dumps(report,indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
