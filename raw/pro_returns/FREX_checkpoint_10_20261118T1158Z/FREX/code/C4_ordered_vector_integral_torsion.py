"""Exact finite certificate for the integral ordered-vector torsion note.

This verifies the integer functions underlying the all-target proof;
it does not compute a derived colimit or assert a monoid lift.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations


def indicators(rank, triple):
    x1, x2, x3 = triple
    between = (rank[x1] < rank[x2] < rank[x3]
               or rank[x3] < rank[x2] < rank[x1])
    return [int(rank[x2] < rank[x1]),
            int(rank[x1] < rank[x2]),
            int(rank[x1] < rank[x2]),
            int(between),
            int(rank[x3] < rank[x2])]


nat_P = list(permutations((1, 2, 3)))
h_P = []
for order in nat_P:
    rank = {v: i for i, v in enumerate(order)}
    total = sum(indicators(rank, (1, 2, 3)))
    assert total % 2 == 1
    h_P.append((total - 1) // 2)


def linear_image(basis, value):
    result = 0
    for i, b in enumerate(basis):
        if value & (1 << i):
            result ^= b
    return result


nat_Q = sorted({tuple(linear_image(basis, v) for v in range(1, 8))
                for basis in permutations(range(1, 8), 3)
                if len({linear_image(basis, v)
                        for v in range(1, 8)}) == 7})
assert len(nat_Q) == 168
maps = ((1, 2, 3), (1, 6, 7), (2, 5, 7),
        (3, 4, 7), (3, 6, 5))
reference_order = (1, 2, 3, 4, 6, 5, 7)
reference_rank = {v: i for i, v in enumerate(reference_order)}
for triple in maps:
    assert triple[0] ^ triple[1] == triple[2]
    assert list(map(reference_rank.get, triple)) == sorted(
        map(reference_rank.get, triple))

h_Q = []
restriction_counts = [Counter() for _ in maps]
for order in nat_Q:
    rank = {v: i for i, v in enumerate(order)}
    total = sum(indicators(rank, triple)[j]
                for j, triple in enumerate(maps))
    assert total % 2 == 0
    h_Q.append(total // 2)
    for j, triple in enumerate(maps):
        restriction_counts[j][tuple(triple.index(v) + 1
                                    for v in order if v in triple)] += 1
for counts in restriction_counts:
    assert len(counts) == 6 and set(counts.values()) == {28}

mean_P = Fraction(sum(h_P), len(h_P))
mean_Q = Fraction(sum(h_Q), len(h_Q))
assert mean_P == Fraction(2, 3)
assert mean_Q == Fraction(7, 6)
assert mean_Q - mean_P == Fraction(1, 2)

print("Natural orders: P =", len(nat_P), "; Q =", len(nat_Q))
print("All five maps preserve the reference order and linear addition.")
print("All restriction fibers have cardinality 28.")
print("Integer identity on P: sum f_j = 1 + 2 h_P.")
print("h_P value counts:", sorted(Counter(h_P).items()))
print("Integer identity on Q: sum a_j^* f_j = 2 h_Q.")
print("h_Q value counts:", sorted(Counter(h_Q).items()))
print("Uniform average h_P =", mean_P)
print("Uniform average h_Q =", mean_Q)
print("Uniform average h_Q - h_P =", mean_Q - mean_P)
print("Certificate verified: [1] = 2v and mu(v) = 1/2.")
print("The image of v in colim(N / Z*1) has order exactly 2.")
