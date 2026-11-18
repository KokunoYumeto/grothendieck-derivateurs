"""Verify one finite obstruction to a particular positive chart.

This is NOT an obstruction to every positive basis or FreeMon diagram.
It only excludes making every edge ratio u_b u_a^{-1}=v_a v_c^{-1}
positive and nonempty in the same functorial chart.
AI-produced, GPT-6 Astra, ChatGPT Pro, 17 November 2026.
"""

from itertools import combinations

n = 13
edges = (
    (0, 4, 5),
    (0, 1, 9),
    (1, 2, 10),
    (2, 3, 11),
    (3, 4, 12),
    (5, 6, 7),
    (7, 8, 9),
)
edge_masks = tuple(sum(1 << x for x in e) for e in edges)


def delta(mask):
    return 2 * mask.bit_count() - 3 * sum(
        (mask & e) == e for e in edge_masks
    )


all_masks = range(1, 1 << n)
minimum = min(delta(mask) for mask in all_masks)
assert minimum > 0
assert delta((1 << n) - 1) == 5
for e in edge_masks:
    assert delta(e) == 3
    for mask in all_masks:
        if mask != e and mask & e == e:
            assert delta(mask) > 3, (e, mask, delta(mask))

print("vertices:", n)
print("ordered hyperedges:", edges)
print("nonempty vertex subsets checked:", (1 << n) - 1)
print("minimum delta:", minimum)
print("delta of the whole object:", delta((1 << n) - 1))
print("all seven one-edge embeddings are strictly closed")
print("Ratio-chart length equations: U_b-U_a=W_c-W_a>0")
print("Edges (0,4,5),(0,1,9) give U4-U1=W5-W9.")
print("Edges through 1,2,3,4 give U4-U1>0.")
print("Edges through 5,7,9 give W5-W9<0.")
print("Contradiction for this chart only; general positivity is not decided.")
