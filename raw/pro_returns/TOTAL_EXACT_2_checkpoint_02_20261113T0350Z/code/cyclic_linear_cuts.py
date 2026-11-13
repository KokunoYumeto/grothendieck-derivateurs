#!/usr/bin/env python3
"""Exact finite checks for the independent linear/cyclic order candidate.

Only standard-library integer arithmetic is used.  The proof does not
depend on a search bound: every possible cut on the chosen four-point
object and every degree-three cyclic order is enumerated.
"""

from itertools import permutations
from math import factorial


def cyclic_orders(size):
    return [(0,) + tail for tail in permutations(range(1, size))]


def face(order, deleted):
    remaining = [x - (x > deleted) for x in order if x != deleted]
    zero = remaining.index(0)
    return tuple(remaining[zero:] + remaining[:zero])


def boundary(degree):
    source = cyclic_orders(degree + 1)
    target = cyclic_orders(degree)
    target_index = {order: i for i, order in enumerate(target)}
    matrix = [[0 for _ in source] for _ in target]
    for j, order in enumerate(source):
        for deleted in range(degree + 1):
            matrix[target_index[face(order, deleted)]][j] += (-1) ** deleted
    return source, target, matrix


def matmul(left, right):
    assert len(left[0]) == len(right)
    return [
        [sum(x * right[k][j] for k, x in enumerate(row))
         for j in range(len(right[0]))]
        for row in left
    ]


def nonzero_entries(matrix):
    return sum(value != 0 for row in matrix for value in row)


def main():
    cycle = (0, 2, 1, 3)
    four_edges = ((0, 1), (1, 2), (2, 3), (0, 3))
    five_edges = ((0, 1), (1, 2), (0, 2), (1, 3), (0, 3))
    print("Four-point linear order: 1 < 2 < 3 < 4")
    print("Four-point cyclic order: (1,3,2,4)")
    print("Four-edge order: 12,23,34,14")
    print("Five-edge order: 12,23,13,24,14")
    for cut in range(len(cycle)):
        cut_order = cycle[cut:] + cycle[:cut]
        position = {x: i for i, x in enumerate(cut_order)}
        chi = lambda pair: int(position[pair[0]] > position[pair[1]])
        four = tuple(map(chi, four_edges))
        five = tuple(map(chi, five_edges))
        winding = four[0] + four[1] + four[2] - four[3]
        negative_triangle = five[0] + five[1] - five[2]
        positive_triangle = five[0] + five[3] - five[4]
        assert (winding, negative_triangle, positive_triangle) == (1, 1, 0)
        print(f"cut order {tuple(x + 1 for x in cut_order)}: "
              f"four={four}, five={five}, identities=(1,1,0)")
    print("Integral four-arrow contradiction: all four weighted colors c imply 2c=1.")
    print("Five-arrow contradiction over every nonzero ring: c=1 and c=0.")
    print()

    boundaries = {}
    for degree in range(1, 5):
        source, target, matrix = boundary(degree)
        boundaries[degree] = matrix
        assert len(source) == factorial(degree)
        print(f"d_{degree}: {len(target)} x {len(source)}, "
              f"nonzero entries = {nonzero_entries(matrix)}")
        if degree <= 3:
            print(f"matrix = {matrix}")
        if degree >= 2:
            composite = matmul(boundaries[degree - 1], matrix)
            assert nonzero_entries(composite) == 0
            print(f"d_{degree - 1} d_{degree} = 0 (verified)")

    assert boundaries[1] == [[0]]
    assert boundaries[2] == [[1, 1]]
    assert nonzero_entries(boundaries[3]) == 0
    print("C_2 = Z^2; ker d_2 = Z(1,-1); im d_3 = 0.")
    print("Therefore H_2 = Z, integrally and with primitive generator (1,-1).")
    print("The one 1-cell is killed by a degree-one 2-cell, so pi_1 = 0.")
    print("No claim about quasi-filteredness of all categories of elements is made.")


if __name__ == "__main__":
    main()
