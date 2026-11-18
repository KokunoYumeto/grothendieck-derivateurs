"""Finite certificates for the explicit infinite-product counterexample.

The general proof is in G.12. This program does not infer the infinite
statement from a finite search: it verifies the sharp finite bound used
there, and the exact path lengths in the defining zigzag poset.
"""
from collections import deque
from itertools import product
import json


def arrow(a, b):
    return a == b or a % 2 == 0 and abs(a - b) == 1


def main():
    bound = 30
    rel = {(a, b) for a in range(bound + 1) for b in range(bound + 1)
           if arrow(a, b)}
    assert all((i, i) in rel for i in range(bound + 1))
    assert all(a == b or (b, a) not in rel for a, b in rel)
    assert all((a, c) in rel for a, b in rel for bb, c in rel if b == bb)
    assert all(abs(a - b) <= 1 for a, b in rel)
    distances = {0: 0}
    queue = deque([0])
    while queue:
        a = queue.popleft()
        for b in range(bound + 1):
            if ((a, b) in rel or (b, a) in rel) and b not in distances:
                distances[b] = distances[a] + 1
                queue.append(b)
    assert all(distances[n] == n for n in range(bound + 1))

    checked = 0
    labels = range(5)
    # All coordinate choices for arrows between tuples of length at most three.
    for source_length in range(1, 4):
        for target_length in range(1, 4):
            for source in product(labels, repeat=source_length):
                for target in product(labels, repeat=target_length):
                    for choice in product(range(source_length), repeat=target_length):
                        if all(arrow(source[choice[j]], target[j]) for j in range(target_length)):
                            checked += 1
                            assert max(target) <= max(source) + 1
                            if source_length == target_length and len(set(choice)) == source_length:
                                assert max(source) <= max(target) + 1
    print(json.dumps({
        "finite_zigzag_vertices": bound + 1,
        "arrows_including_identities": len(rel),
        "distance_from_zero": distances,
        "finite_tuple_morphisms_checked": checked,
        "forward_bound": "max(target) <= max(source)+1",
        "inverse_W_bound": "max(source) <= max(target)+1",
        "infinite_conclusion": "proved by the uniform-bound argument in G.12, not by this finite check",
        "all_assertions": "passed"
    }, indent=2))


if __name__ == "__main__":
    main()
