"""Finite exact checks for the simplex-code argument in A.33.

This verifies the two linear-algebra identities used by the proof, not the
Ramsey theorem or the all-module conclusion.  Subspaces are enumerated once
through reduced-row-echelon bases over F2; all arithmetic is exact.
"""

from collections import Counter
from itertools import combinations, product, permutations
from math import factorial


def parity(x):
    return x.bit_count() & 1


def subspace_bases(n, k):
    for pivots in combinations(range(n), k):
        pivot_set = set(pivots)
        slots = [(i, j) for i, p in enumerate(pivots)
                 for j in range(p + 1, n) if j not in pivot_set]
        for bits in product((0, 1), repeat=len(slots)):
            basis = [1 << p for p in pivots]
            for bit, (i, j) in zip(bits, slots):
                basis[i] |= bit << j
            yield tuple(basis)


def span(basis):
    result = [0]
    for b in basis:
        result += [v ^ b for v in result]
    return set(result)


total = 0
for q in range(1, 7):
    dual = tuple(range(1, 1 << q))
    codes = [sum(parity(ell & v) << j for j, ell in enumerate(dual))
             for v in range(1 << q)]
    assert len(set(codes)) == 1 << q
    checked = 0
    for p in range(1, q + 1):
        multiplicity = 1 << (q - p)
        for basis in subspace_bases(q, p):
            subspace = span(basis)
            restrictions = Counter(
                sum(parity(ell & b) << i for i, b in enumerate(basis))
                for ell in dual
            )
            assert all(restrictions[alpha] == multiplicity
                       for alpha in range(1, 1 << p))
            assert restrictions[0] == multiplicity - 1
            support = 0
            for v in subspace:
                support |= codes[v]
            assert support.bit_count() == ((1 << p) - 1) * multiplicity
            intersection = {v for v, code in enumerate(codes)
                            if code & ~support == 0}
            assert intersection == subspace
            checked += 1
    total += checked
    print(f"q={q}: {checked} nonzero subspaces; restriction multiplicities "
          "and W_P intersect Q = P passed")

# Check the elementary finite-order restriction fact used for both independent
# order coordinates.  Every induced order has exactly N!/n! preimages.
order_cases = 0
for n in range(1, 7):
    for k in range(1, n + 1):
        subset = set(range(k))
        counts = Counter(tuple(x for x in perm if x in subset)
                         for perm in permutations(range(n)))
        assert len(counts) == factorial(k)
        assert set(counts.values()) == {factorial(n) // factorial(k)}
        order_cases += 1

print(f"PASS: {total} simplex-code subspace identities and "
      f"{order_cases} exact uniform-order restriction cases")
