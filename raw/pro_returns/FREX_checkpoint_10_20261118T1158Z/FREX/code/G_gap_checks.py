#!/usr/bin/env python3
"""Finite certificates for the coloured interval monoid and prefix basis.

This checks the finitely presented three-colour instance.  The manuscript
proves the arbitrary-colour presentation and the unbounded naturality claim.
Only the Python standard library is used.
"""
from itertools import combinations, product

COLOURS = (0, 1, 2)
ALPHABET = ("l", "r", "e", "L1", "R1", "L2", "R2")
RULES = {
    ("e", "e"): ("e",),
    ("l", "e"): ("l",),
    ("e", "r"): ("r",),
}
for a in (1, 2):
    RULES[("e", f"L{a}")] = (f"L{a}",)
    RULES[(f"R{a}", "e")] = (f"R{a}",)
    RULES[(f"L{a}", f"R{a}")] = ("e",)


def nf(word):
    word = tuple(word)
    while True:
        for i in range(len(word) - 1):
            replacement = RULES.get(word[i:i + 2])
            if replacement is not None:
                word = word[:i] + replacement + word[i + 2:]
                break
        else:
            return word


def L(a):
    return ("e",) if a == 0 else (f"L{a}",)


def R(a):
    return ("e",) if a == 0 else (f"R{a}",)


def interval(left, right):
    if left is None and right is None:
        return ("l", "r")
    if left is None:
        return nf(("l",) + L(right))
    if right is None:
        return nf(R(left) + ("r",))
    return nf(R(left) + L(right))


critical = 0
for word in product(ALPHABET, repeat=3):
    if word[:2] in RULES and word[1:] in RULES:
        left = nf(RULES[word[:2]] + word[2:])
        right = nf(word[:1] + RULES[word[1:]])
        assert left == right, (word, left, right)
        critical += 1
print(f"Three-colour presentation: {len(ALPHABET)} generators, {len(RULES)} rules.")
print(f"All {critical} overlapping critical triples agree.")
print("All rules decrease word length; hence these checks certify confluence.")

subdivisions = 0
for left in (None,) + COLOURS:
    for middle in COLOURS:
        for right in COLOURS + (None,):
            assert nf(interval(left, middle) + interval(middle, right)) == interval(left, right)
            subdivisions += 1
print(f"All {subdivisions} colour-and-endpoint subdivision identities hold.")

injections = 0
gap_checks = 0
for n in range(1, 7):
    for target in product(COLOURS, repeat=n):
        target_gaps = tuple(interval(a, b) for a, b in zip((None,) + target, target + (None,)))
        for m in range(1, n + 1):
            for embedding in combinations(range(n), m):
                source = tuple(target[i] for i in embedding)
                source_gaps = tuple(interval(a, b) for a, b in zip((None,) + source, source + (None,)))
                boundaries = (-1,) + embedding + (n,)
                for j in range(m + 1):
                    image = ()
                    for k in range(boundaries[j] + 1, boundaries[j + 1] + 1):
                        image += target_gaps[k]
                    assert nf(image) == source_gaps[j]
                    gap_checks += 1
                injections += 1
print(f"Colimit cocone checked on {injections} colour-preserving injections, target size <= 6.")
print(f"Individual gap images checked: {gap_checks}.")


def freely_reduce(word):
    result = []
    for token in word:
        if result and result[-1] == -token:
            result.pop()
        else:
            result.append(token)
    return tuple(result)


def invert(word):
    return tuple(-t for t in reversed(word))


def substitute(word, images):
    result = ()
    for token in word:
        image = images[abs(token)]
        result += image if token > 0 else invert(image)
    return freely_reduce(result)


prefix_checks = 0
for n in range(1, 9):
    # n points, n+1 gaps, prefix generators p_1,...,p_n,total.
    prefixes = {j: tuple(range(1, j + 1)) for j in range(1, n + 2)}
    inverse_basis = {1: (1,)}
    inverse_basis.update({j: (-(j - 1), j) for j in range(2, n + 2)})
    for j in range(1, n + 2):
        assert substitute(prefixes[j], inverse_basis) == (j,)
        assert substitute(inverse_basis[j], prefixes) == (j,)
    for m in range(1, n + 1):
        for embedding in combinations(range(1, n + 1), m):
            boundaries = (0,) + embedding + (n + 1,)
            gap_images = {j + 1: tuple(range(boundaries[j] + 1, boundaries[j + 1] + 1)) for j in range(m + 1)}
            for j in range(1, m + 1):
                assert substitute(tuple(range(1, j + 1)), gap_images) == prefixes[embedding[j - 1]]
                prefix_checks += 1
            assert substitute(tuple(range(1, m + 2)), gap_images) == prefixes[n + 1]
            prefix_checks += 1
print("Prefix/total basis and its inverse checked through 8 points.")
print(f"Naturality equations checked: {prefix_checks}.")
print("PASS")
