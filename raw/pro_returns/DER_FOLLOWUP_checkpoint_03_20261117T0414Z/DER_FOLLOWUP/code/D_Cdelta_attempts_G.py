#!/usr/bin/env python3
"""Verify finite obstructions in the independent C_delta investigation.

This does not decide the C_delta FreeMon comparison question.
"""
from itertools import combinations
from pathlib import Path
import json

vertices = frozenset(range(1, 6))
edges = (frozenset((1, 3, 4)), frozenset((1, 2, 5)))

def subsets(items):
    items = sorted(items)
    for n in range(len(items) + 1):
        for sub in combinations(items, n):
            yield frozenset(sub)

def delta(sub):
    return 2 * len(sub) - 3 * sum(edge <= sub for edge in edges)

positivity = all(delta(sub) > 0 for sub in subsets(vertices) if sub)
closed = []
for edge in edges:
    extensions = [sub for sub in subsets(vertices) if edge < sub]
    closed.append(all(delta(sub) > delta(edge) for sub in extensions))
assert positivity and all(closed)

# Coordinate order U1,...,U5,V1,...,V5.  Each row is the edge equation
# U_b-U_a+V_c-V_a=0.  Their difference equals two strictly positive gaps
# when U increases and V decreases in the supplied linear order.
rows = []
for edge in edges:
    a, b, c = sorted(edge)
    row = [0] * 10
    row[b - 1] += 1
    row[a - 1] -= 1
    row[5 + c - 1] += 1
    row[5 + a - 1] -= 1
    rows.append(row)
difference = [x - y for x, y in zip(*rows)]
expected = [0, -1, 1, 0, 0, 0, 0, 0, 1, -1]
assert difference == expected

# A pure bifix, biunitary free submonoid whose free-group completion map
# is noninjective.  Its language is ((a|d)(b|c))*.  These exact DFA
# transformation checks prove purity and left unitarity for ALL words,
# not just a bounded word enumeration.  Right unitarity follows because
# every accepted word returns the deterministic automaton to state zero.
rectangle_code = ("ab", "ac", "db", "dc")
assert len(set(rectangle_code)) == 4
assert {len(w) for w in rectangle_code} == {2}
alphabet = "abcd"
# States 0=expect a/d (accept), 1=expect b/c, 2=dead.
letter_transform = {
    "a": (1, 2, 2), "d": (1, 2, 2),
    "b": (2, 0, 2), "c": (2, 0, 2),
}
identity = (0, 1, 2)
transform_words = {identity: ""}
todo = [identity]
while todo:
    old = todo.pop()
    for letter in alphabet:
        new = tuple(letter_transform[letter][old[s]] for s in range(3))
        if new not in transform_words:
            transform_words[new] = transform_words[old] + letter
            todo.append(new)

for trans in transform_words:
    state = 0
    for power in range(1, 4):
        state = trans[state]
        if state == 0:
            assert trans[0] == 0  # purity; any first return is <=3
    if trans[0] == 0:
        assert {s for s in range(3) if trans[s] == 0} == {0}

def free_reduce(letters):
    stack = []
    for letter in letters:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return stack

def inverse_word(word):
    return [-x for x in reversed(word)]

def expanded_kernel(code):
    image = {i + 1: [alphabet.index(c) + 1 for c in w]
             for i, w in enumerate(code)}
    preimage = [1, -3, 4, -2]  # x z^{-1} w y^{-1}
    assert free_reduce(preimage) == preimage
    expanded = []
    for letter in preimage:
        word = image[abs(letter)]
        expanded.extend(word if letter > 0 else inverse_word(word))
    assert free_reduce(expanded) == []
    return {"preimage_reduced_word": preimage,
            "expanded_image": expanded,
            "reduced_image": free_reduce(expanded)}

rectangle_kernel = expanded_kernel(rectangle_code)
even_binary_kernel = expanded_kernel(("aa", "ab", "ba", "bb"))

result = {
    "vertices": sorted(vertices),
    "edges": [sorted(edge) for edge in edges],
    "delta_full": delta(vertices),
    "all_nonempty_induced_subobjects_positive": positivity,
    "both_W_images_strictly_closed": closed,
    "edge_relation_rows": rows,
    "row_difference": difference,
    "contradiction": "(U3-U2)+(V4-V5)=0 with both summands strictly positive",
    "scope": "Refutes only globally nested U-prefixes/V-suffixes; not arbitrary positive bases.",
    "pure_bifix_code_certificate": {
        "code": rectangle_code,
        "uniform_length": 2,
        "dfa_states": {"0": "expect a/d; accepting", "1": "expect b/c", "2": "dead"},
        "letter_transformations": letter_transform,
        "complete_transformation_monoid": [
            {"transformation": trans, "witness_word": word}
            for trans, word in sorted(transform_words.items())
        ],
        "all_transformation_power_returns_force_first_return": True,
        "all_accepting_transformations_have_zero_preimage_only_zero": True,
        "pure_for_all_words": True,
        "left_unitary_for_all_words": True,
        "right_unitary_for_all_words": True,
        "group_kernel": rectangle_kernel,
        "scope": "Pure bifix and biunitary do not imply group-completion injectivity; this is not asserted to be a saturated fixed submonoid."
    },
    "D9_even_binary_code_group_kernel": even_binary_kernel,
    "assertions": "passed",
}
root = Path(__file__).resolve().parents[1]
(root / "code/outputs/D_Cdelta_attempts_G.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
