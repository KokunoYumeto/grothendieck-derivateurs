#!/usr/bin/env python3
"""Exact certificate for the surviving local rectangle in Part G.

This is a diagram only on V,W.  It is not an extension to C_delta.
All verification is integral/combinatorial; no numerical solver is used.
"""
from itertools import combinations, permutations
import json
from pathlib import Path

WORDS = {"u1": "ac", "u2": "bc", "u3": "d",
         "v1": "bacca", "v2": "e", "v3": "aacca"}
ALPHABET = "abcde"


def inverse(w):
    return w.swapcase()[::-1]


def reduce_group(w):
    stack = []
    for letter in w:
        if stack and stack[-1] == letter.swapcase():
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


def determinant(matrix):
    n = len(matrix)
    answer = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        term = (-1) ** inversions
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        answer += term
    return answer


def counts(w):
    return [w.count(a) for a in ALPHABET]


def bifix(ws):
    return all(not (a.startswith(b) or b.startswith(a)
                    or a.endswith(b) or b.endswith(a))
               for a, b in combinations(ws, 2))


def main():
    core = [WORDS[x] for x in ("u1", "u2", "v3", "v1")]
    assert bifix(core)
    relator = (WORDS["u2"] + inverse(WORDS["u1"])
               + WORDS["v3"] + inverse(WORDS["v1"]))
    assert reduce_group(relator) == ""
    for point in (1, 2, 3):
        assert bifix([WORDS[f"u{point}"], WORDS[f"v{point}"]])
    names = ("u1", "u2", "v3", "u3", "v2")
    matrix = [[counts(WORDS[name])[i] for name in names] for i in range(5)]
    det = determinant(matrix)
    assert det == -1
    relation = [counts(WORDS["u2"])[i] - counts(WORDS["u1"])[i]
                + counts(WORDS["v3"])[i] - counts(WORDS["v1"])[i]
                for i in range(5)]
    assert relation == [0] * 5
    result = {
        "scope": "Only the full subcategory with objects V,W; no global extension claimed",
        "words": WORDS,
        "core_is_bifix_code": True,
        "each_point_map_is_injective": True,
        "free_group_relator_reduces_to": "identity",
        "abelianization_minor_columns": names,
        "abelianization_minor_determinant": det,
        "abelianization_kernel": "primitive incidence relation only",
        "status": "PASS",
    }
    print(json.dumps(result, indent=2))
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
