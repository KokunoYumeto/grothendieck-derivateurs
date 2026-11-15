"""Verify one exact finite-simple-group warning for the diagonal-block search.

Permutations are one-line tuples on {0,1,2,3,4}; multiplication p*q is
p composed with q.  The commutator is [a,x] = a*x*a^-1*x^-1.
This verifies a finite example only.  It makes no assertion about the
infinite simple target groups in the outstanding dimension-two problem.
"""
from itertools import permutations
import json
from pathlib import Path


def mul(p, q):
    return tuple(p[q[i]] for i in range(5))


def inv(p):
    return tuple(p.index(i) for i in range(5))


def comm(a, x):
    return mul(mul(mul(a, x), inv(a)), inv(x))


def even(p):
    return sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0


identity = tuple(range(5))
group = {p for p in permutations(range(5)) if even(p)}
constants = [
    (1, 2, 3, 4, 0),
    (1, 2, 3, 4, 0),
    (1, 2, 4, 0, 3),
    (0, 1, 3, 4, 2),
    (0, 2, 1, 4, 3),
    (0, 2, 1, 4, 3),
]
assert len(group) == 60
assert all(a in group and a != identity for a in constants)
values = set(group)
ranks = [len(values)]
for a in constants:
    values = {comm(a, x) for x in values}
    ranks.append(len(values))
assert ranks == [60, 12, 6, 4, 3, 2, 1]
assert values == {identity}

# Independently check every substitution, without the intermediate image sets.
for x in group:
    y = x
    for a in constants:
        y = comm(a, y)
    assert y == identity

result = {
    "group": "A5",
    "permutation_convention": "(p*q)(i)=p(q(i)); zero-based one-line tuples",
    "commutator_convention": "[a,x]=a*x*a^-1*x^-1",
    "constants_in_order_from_inner_to_outer": constants,
    "successive_image_cardinalities": ranks,
    "final_image": list(values),
    "substitutions_checked": len(group),
    "conclusion": "The sixfold indicated commutator composition is identically 1 on A5.",
    "scope": "Finite simple example only; no infinite-target conclusion.",
}

# The repetition-free variant also fits the distinct-coefficient condition
# arising from a repetition-free enumeration in the diagonal construction.
distinct_constants = [
    (1, 2, 3, 4, 0),
    (1, 2, 4, 0, 3),
    (0, 1, 3, 4, 2),
    (0, 2, 1, 4, 3),
    (0, 3, 4, 1, 2),
    (1, 4, 3, 0, 2),
]
assert len(set(distinct_constants)) == len(distinct_constants)
assert all(a in group and a != identity for a in distinct_constants)
distinct_values = set(group)
distinct_ranks = [len(distinct_values)]
for a in distinct_constants:
    distinct_values = {comm(a, x) for x in distinct_values}
    distinct_ranks.append(len(distinct_values))
assert distinct_ranks == [60, 12, 6, 5, 3, 2, 1]
assert distinct_values == {identity}
for x in group:
    y = x
    for a in distinct_constants:
        y = comm(a, y)
    assert y == identity
result["distinct_constants_variant"] = {
    "constants_in_order_from_inner_to_outer": distinct_constants,
    "successive_image_cardinalities": distinct_ranks,
    "final_image": list(distinct_values),
    "substitutions_checked": len(group),
}
path = Path(__file__).with_name("a_nested_commutator_checks.json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
