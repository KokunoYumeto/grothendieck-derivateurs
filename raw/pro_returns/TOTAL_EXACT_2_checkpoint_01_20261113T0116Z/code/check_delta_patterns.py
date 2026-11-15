"""Finite checks supporting the infinite Δ_inj coefficient-pattern argument.
The mathematical proof applies to every increasing injection: it inserts zero
coordinates and hence preserves the ordered list of nonzero coefficients.
"""
from itertools import combinations
import json

alpha = (1, 1, -1)
beta = (1, 0, 0)

def push(vector, injection, target_size):
    result = [0] * target_size
    for coefficient, target in zip(vector, injection):
        result[target] += coefficient
    return tuple(result)

def pattern(vector):
    return tuple(x for x in vector if x)

counts = {}
for size in range(3, 10):
    injections = list(combinations(range(size), 3))
    for injection in injections:
        assert pattern(push(alpha, injection, size)) == pattern(alpha)
        assert pattern(push(beta, injection, size)) == pattern(beta)
    counts[size] = len(injections)
assert pattern(alpha) != pattern(beta)
assert sum(alpha) == sum(beta) == 1

terms = [(1, (0, 1, 2)), (-1, (0, 1, 3)), (1, (0, 2, 3))]
assert sum(weight for weight, _ in terms) == 1

def affine_push(vector):
    result = [0] * 4
    for weight, injection in terms:
        for i, coefficient in enumerate(push(vector, injection, 4)):
            result[i] += weight * coefficient
    return result

assert affine_push(alpha) == affine_push(beta) == [1, 0, 0, 0]
print(json.dumps({
    "alpha": alpha,
    "beta": beta,
    "ordered_nonzero_patterns": [pattern(alpha), pattern(beta)],
    "injections_checked_by_target_size": counts,
    "ordinary_set_colimit_components_distinct_by_invariant": True,
    "abelian_colimit_augmentations": [sum(alpha), sum(beta)],
    "affine_equalizer": terms,
    "common_affine_image": affine_push(alpha),
    "scope": "Finite checks support the general zero-insertion proof; they do not replace it."
}, indent=2))
