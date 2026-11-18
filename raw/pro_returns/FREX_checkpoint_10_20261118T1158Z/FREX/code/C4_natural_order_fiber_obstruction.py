"""Finite obstruction to ordering all natural-order restriction fibers.

Only the literal point-indicator bases and positive pullback matrices
are considered. This does not exclude a change of basis or a different
stabilized monoid realization.
"""
from collections import Counter
from itertools import permutations


def linear_image(basis, value):
    result = 0
    for i, b in enumerate(basis):
        if value & (1 << i):
            result ^= b
    return result


orders = sorted({tuple(linear_image(b, v) for v in range(1, 8))
                 for b in permutations(range(1, 8), 3)
                 if len({linear_image(b, v) for v in range(1, 8)}) == 7})
assert len(orders) == 168
plane_A, plane_B = (1, 2, 3), (1, 4, 5)
types = list(permutations((0, 1, 2)))
index = {order: i for i, order in enumerate(types)}
counts = Counter()
for order in orders:
    a = tuple(plane_A.index(v) for v in order if v in plane_A)
    b = tuple(plane_B.index(v) for v in order if v in plane_B)
    counts[index[a], index[b]] += 1
assert all(sum(counts[i, j] for j in range(6)) == 28 for i in range(6))
assert all(sum(counts[i, j] for i in range(6)) == 28 for j in range(6))
assert len(counts) > 6 + 6 - 1
print("Natural orders of the punctured 3-dimensional F_2-space:", len(orders))
print("Two planes:", plane_A, plane_B)
print("Order types, using local indices:", types)
print("Joint fiber cardinality matrix:")
for i in range(6):
    print(" ".join(f"{counts[i,j]:2d}" for j in range(6)))
print("Nonempty intersections:", len(counts))
print("Upper bound for two partitions into six interval blocks: 11.")
print("Thus no linear order makes every fiber of both restrictions convex.")
print("The literal positive pullback diagram has no ordered-fiber word lift.")
