#!/usr/bin/env python3
"""Exact finite checks for H.2 and I.4. No third-party dependencies."""
import json
from itertools import product
from pathlib import Path


def run():
    # H.2: one object, identity 1, nonidentity absorbing idempotent e.
    arrows = ('1', 'e')
    mul = lambda a, b: '1' if a == b == '1' else 'e'
    assert all(mul('1', a) == mul(a, '1') == a for a in arrows)
    assert all(mul(mul(a, b), c) == mul(a, mul(b, c))
               for a, b, c in product(arrows, repeat=3))
    # Outgoing lifts of C -> * form x/C: k:a->b iff k*a=b.
    hom = {a: {b: [k for k in arrows if mul(k, a) == b]
               for b in arrows} for a in arrows}
    assert all(len(hom['1'][b]) == 1 for b in arrows)
    assert all(mul('e', a) == mul(a, 'e') == 'e' for a in arrows)
    action = {'1': (0, 1), 'e': (0, 0)}
    assert all(tuple(action[a][action[b][x]] for x in (0, 1))
               == action[mul(a, b)] for a, b in product(arrows, repeat=2))
    fixed = [x for x in (0, 1) if all(action[a][x] == x for a in arrows)]
    assert fixed == [0]

    # I.4: finite posets, and the exact incoming-lift object sets.
    chain = (0, 1)
    point = (0,)
    def incoming(source, target, image, x, b):
        if not b <= image[x]:
            return None  # no base arrow to test
        return [y for y in source if y <= x and image[y] == b]
    p_lifts = {str(x): incoming(chain, point, {0: 0, 1: 0}, x, 0)
               for x in chain}
    pg_lifts = incoming(point, point, {0: 0}, 0, 0)
    g_lifts = incoming(point, chain, {0: 1}, 0, 0)
    assert p_lifts == {'0': [0], '1': [0, 1]}
    assert all(x in ys and all(y <= x for y in ys)
               for x, ys in ((0, p_lifts['0']), (1, p_lifts['1'])))
    assert pg_lifts == [0] and g_lifts == []
    result = {
        'H.2': {'objects': 1, 'arrows': 2, 'category_laws': True,
                'outgoing_lift_hom_sets': hom, 'initial_lift': '1',
                'zero_natural_transformation': 'e', 'coefficient_values': [0, 1],
                'categorical_limit': fixed, 'constant_geometric_sections': [0, 1]},
        'I.4': {'p_incoming_lifts': p_lifts, 'pg_incoming_lifts': pg_lifts,
                'g_incoming_lifts_at_arrow_0_to_1': g_lifts,
                'p_smooth': True, 'pg_smooth': True, 'g_smooth': False,
                'cancellation_counterexample': True}
    }
    destination = Path(__file__).with_name('small_counterexamples.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
