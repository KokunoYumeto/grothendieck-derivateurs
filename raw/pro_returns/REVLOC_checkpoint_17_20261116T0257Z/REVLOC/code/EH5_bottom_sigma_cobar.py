#!/usr/bin/env python3
"""Exact normalized Milnor-cobar test for the bottom h0*h3 class.

Input is a finite graded LEFT comodule over the dual mod-two Steenrod algebra:
  {"classes": [{"id": "a7", "degree": 7}, ...],
   "coaction": {"x": [{"milnor": [r1,r2,r3], "lower": "a7"}, ...]},
   "bottom": "a7", "internal_degree": 16}
The coaction lists only reduced terms.  It is dual to the convention
<a tensor x, psi(m)> = <a*x,m> and uses
  Delta(xi_n) = sum_i xi_(n-i)^(2^i) tensor xi_i.

The cobar is Abar_*^tensor(s) tensor M.  Keys are printed (m; a1|...|as),
but the M coaction APPENDS its algebra term on the right.  This is important:
putting the term at the left would require the opposite coproduct.

All calculations are exact over F2.  A nonboundary certificate is an explicit
linear functional annihilating every boundary column and taking value one on
the cycle.  A boundary certificate is an explicit cobar-one preimage.
The script proves no Adams permanence theorem; that interface is separate.
"""
from __future__ import annotations

import argparse
import itertools
import json
from functools import lru_cache
from pathlib import Path

NGEN = 4
WEIGHTS = tuple((1 << (i + 1)) - 1 for i in range(NGEN))
ZERO = (0,) * NGEN


def mono(values):
    values = tuple(int(x) for x in values)
    if len(values) > NGEN or any(x < 0 for x in values):
        raise ValueError(f"Invalid Milnor monomial: {values}")
    return values + (0,) * (NGEN - len(values))


def mdeg(a):
    return sum(x * w for x, w in zip(a, WEIGHTS))


def mmul(a, b):
    return tuple(x + y for x, y in zip(a, b))


def toggle(out, term):
    if term in out:
        out.remove(term)
    else:
        out.add(term)


def pmul(p, q):
    out = set()
    for a, b in p:
        for c, d in q:
            toggle(out, (mmul(a, c), mmul(b, d)))
    return out


@lru_cache(None)
def generator_coproduct(n):
    out = set()
    for i in range(n + 1):
        left, right = [0] * NGEN, [0] * NGEN
        if n - i:
            left[n - i - 1] = 1 << i
        if i:
            right[i - 1] = 1
        out.add((tuple(left), tuple(right)))
    return frozenset(out)


@lru_cache(None)
def coproduct(a):
    out = {(ZERO, ZERO)}
    for i, exponent in enumerate(a, 1):
        factor = set(generator_coproduct(i))
        while exponent:
            if exponent & 1:
                out = pmul(out, factor)
            exponent >>= 1
            if exponent:
                factor = pmul(factor, factor)
    return frozenset(out)


@lru_cache(None)
def reduced_coproduct(a):
    return frozenset((b, c) for b, c in coproduct(a) if b != ZERO and c != ZERO)


@lru_cache(None)
def monomials(degree):
    if degree < 0:
        return ()
    out = []

    def visit(index, left, exponents):
        if index == NGEN:
            if left == 0:
                out.append(tuple(exponents))
            return
        for exponent in range(left // WEIGHTS[index] + 1):
            visit(index + 1, left - exponent * WEIGHTS[index], exponents + [exponent])

    visit(0, degree, [])
    return tuple(out)


@lru_cache(None)
def tensors(length, degree):
    if length == 0:
        return ((),) if degree == 0 else ()
    out = []
    for first_degree in range(1, degree - length + 2):
        for first in monomials(first_degree):
            for tail in tensors(length - 1, degree - first_degree):
                out.append((first,) + tail)
    return tuple(out)


def check_coalgebra(max_degree):
    for degree in range(max_degree + 1):
        for a in monomials(degree):
            left, right = set(), set()
            for b, c in coproduct(a):
                for d, e in coproduct(b):
                    toggle(left, (d, e, c))
                for d, e in coproduct(c):
                    toggle(right, (b, d, e))
            if left != right:
                raise AssertionError(("Coalgebra is not coassociative", a, left ^ right))


@lru_cache(None)
def operation_words(degree):
    """All words in Sq^(2^i) of the specified total degree."""
    if degree == 0:
        return ((),)
    return tuple((first,) + tail for first in (1, 2, 4, 8)
                 if first <= degree for tail in operation_words(degree - first))


@lru_cache(None)
def pairing(word, a):
    """Pair Sq^word[0] ... Sq^word[-1] with a Milnor monomial."""
    if not word:
        return int(a == ZERO)
    if len(word) == 1:
        return int(a == mono([word[0]]))
    value = 0
    first = mono([word[0]])
    for left, right in coproduct(a):
        if left == first:
            value ^= pairing(word[1:], right)
    return value


def comodule_from_squares(data):
    """Convert homology Sq_*^(1,2,4,8) matrices to a left Milnor coaction.

    Generator words span each required degree of A.  For every source and
    lower class, solve the complete pairing system; all remaining words are
    checked too, so inconsistent Adem data is rejected rather than extended.
    """
    degrees = {x["id"]: int(x["degree"]) for x in data["classes"]}
    operators = {}
    for exponent, matrix in data["operations"].items():
        exponent = int(exponent)
        operators[exponent] = {}
        for x, image in matrix.items():
            if x not in degrees:
                raise ValueError(("Unknown operation source", x))
            out = set()
            for y in image:
                if y not in degrees or degrees[x] - degrees[y] != exponent:
                    raise ValueError(("Inhomogeneous operation", exponent, x, y))
                toggle(out, y)
            operators[exponent][x] = out

    @lru_cache(None)
    def act(word, x):
        image = {x}
        for exponent in word:
            out = set()
            for y in image:
                for z in operators.get(exponent, {}).get(y, ()):
                    toggle(out, z)
            image = out
        return frozenset(image)

    coaction = {x: [] for x in degrees}
    max_gap = max(degrees.values()) - min(degrees.values())
    checked_word_actions = 0
    for gap in range(1, max_gap + 1):
        mons = monomials(gap)
        words = operation_words(gap)
        rows = [bits(j for j, a in enumerate(mons) if pairing(word, a)) for word in words]
        # Keep an independent square pairing matrix; combine rows together
        # with their operation-word selector to solve every evaluation vector.
        pivots = {}
        for i, row in enumerate(rows):
            vector, selector = row, 1 << i
            while vector:
                p = vector.bit_length() - 1
                if p not in pivots:
                    pivots[p] = (vector, selector)
                    break
                other, other_selector = pivots[p]
                vector ^= other
                selector ^= other_selector
        if len(pivots) != len(mons):
            raise AssertionError(("Sq powers do not span required Milnor degree", gap))
        for x, dx in degrees.items():
            for y, dy in degrees.items():
                if dx - dy != gap:
                    continue
                evaluations = bits(i for i, word in enumerate(words) if y in act(word, x))
                solution = 0
                # Each pivot row has lower column indices only, so ascending
                # substitution solves the transposed evaluation problem.
                for p in sorted(pivots):
                    row, selector = pivots[p]
                    rhs = (selector & evaluations).bit_count() & 1
                    rhs ^= ((row ^ (1 << p)) & solution).bit_count() & 1
                    if rhs:
                        solution |= 1 << p
                for i, row in enumerate(rows):
                    if ((row & solution).bit_count() & 1) != ((evaluations >> i) & 1):
                        raise AssertionError(("Inconsistent Steenrod/Adem action", gap, x, y, words[i]))
                checked_word_actions += len(words)
                for j in positions(solution):
                    coaction[x].append({"milnor": list(mons[j]), "lower": y})
    result = {key: value for key, value in data.items() if key != "operations"}
    result["coaction"] = coaction
    result["conversion_audit"] = {"all_generator_word_pairings_checked": True,
                                  "checked_word_actions": checked_word_actions,
                                  "max_operation_degree": max_gap}
    Comodule(result).check()
    return result


class Comodule:
    def __init__(self, data):
        self.degrees = {x["id"]: int(x["degree"]) for x in data["classes"]}
        if len(self.degrees) != len(data["classes"]):
            raise ValueError("Duplicate class IDs")
        self.ids = sorted(self.degrees, key=lambda x: (self.degrees[x], x))
        self.reduced = {x: set() for x in self.ids}
        for x, entries in data.get("coaction", {}).items():
            if x not in self.degrees:
                raise ValueError(f"Unknown coaction input {x}")
            for entry in entries:
                a, y = mono(entry["milnor"]), entry["lower"]
                if a == ZERO or y not in self.degrees:
                    raise ValueError(("Invalid reduced coaction term", x, a, y))
                if self.degrees[y] + mdeg(a) != self.degrees[x]:
                    raise ValueError(("Inhomogeneous coaction", x, a, y))
                toggle(self.reduced[x], (a, y))
        self.bottom = data.get("bottom", self.ids[0])
        self.internal = int(data.get("internal_degree", 16))

    def full(self, x):
        return self.reduced[x] | {(ZERO, x)}

    def check(self):
        for x in self.ids:
            left, right = set(), set()
            for a, y in self.full(x):
                for b, c in coproduct(a):
                    toggle(left, (b, c, y))
                for b, z in self.full(y):
                    toggle(right, (a, b, z))
            if left != right:
                raise AssertionError(("Left coaction is not coassociative", x, left ^ right))

    def basis(self, filtration):
        return [(x, tensor) for x in self.ids
                for tensor in tensors(filtration, self.internal - self.degrees[x])]

    def differential(self, key):
        x, tensor = key
        out = set()
        for i, a in enumerate(tensor):
            for b, c in reduced_coproduct(a):
                toggle(out, (x, tensor[:i] + (b, c) + tensor[i + 1:]))
        for a, y in self.reduced[x]:
            toggle(out, (y, tensor + (a,)))
        return out


def bits(indices):
    out = 0
    for i in indices:
        out ^= 1 << i
    return out


def positions(value):
    while value:
        lowest = value & -value
        yield lowest.bit_length() - 1
        value ^= lowest


class ColumnSpace:
    def __init__(self, columns):
        self.pivots = {}
        for i, col in enumerate(columns):
            vector, witness = self.reduce(col, 1 << i)
            if vector:
                self.pivots[vector.bit_length() - 1] = (vector, witness)

    def reduce(self, vector, witness=0):
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in self.pivots:
                break
            col, chain = self.pivots[pivot]
            vector ^= col
            witness ^= chain
        return vector, witness


def format_mono(a):
    return "*".join(f"xi{i}" + (f"^{n}" if n != 1 else "")
                    for i, n in enumerate(a, 1) if n) or "1"


def format_key(key):
    x, tensor = key
    return "[" + "|".join(format_mono(a) for a in tensor) + "] " + x


def calculate(data):
    module = Comodule(data)
    module.check()
    max_algebra_degree = module.internal - min(module.degrees.values())
    check_coalgebra(max_algebra_degree)
    bases = {s: module.basis(s) for s in (1, 2, 3)}
    indices = {s: {key: i for i, key in enumerate(bases[s])} for s in bases}
    matrices = {}
    for s in (1, 2):
        matrices[s] = [bits(indices[s + 1][term] for term in module.differential(key))
                       for key in bases[s]]
    for i, col in enumerate(matrices[1]):
        second = 0
        for j in positions(col):
            second ^= matrices[2][j]
        if second:
            raise AssertionError(("Cobar d squared nonzero", format_key(bases[1][i])))
    target = (module.bottom, (mono([1]), mono([8])))
    if target not in indices[2]:
        raise ValueError("Target [xi1|xi1^8] bottom is not in the requested bidegree")
    target_index = indices[2][target]
    target_vector = 1 << target_index
    if matrices[2][target_index]:
        raise AssertionError("The proposed bottom h0*h3 representative is not a cocycle")
    boundaries = ColumnSpace(matrices[1])
    residual, witness = boundaries.reduce(target_vector)
    rank_d2 = len(ColumnSpace(matrices[2]).pivots)
    result = {
        "convention": "Left Milnor comodule; cobar Abar^tensor(s) tensor M; coaction appended at right",
        "internal_degree": module.internal,
        "filtration": 2,
        "stem": module.internal - 2,
        "class_count": len(module.ids),
        "class_dimensions": {str(d): sum(v == d for v in module.degrees.values())
                             for d in sorted(set(module.degrees.values()))},
        "cobar_dimensions": {str(s): len(bases[s]) for s in bases},
        "rank_d1": len(boundaries.pivots),
        "rank_d2": rank_d2,
        "ext_dimension": len(bases[2]) - rank_d2 - len(boundaries.pivots),
        "coassociative": True,
        "d_squared_zero": True,
        "target": format_key(target),
        "target_is_cycle": True,
        "target_is_boundary": residual == 0,
    }
    if residual == 0:
        result["boundary_preimage"] = [format_key(bases[1][i]) for i in positions(witness)]
        check = 0
        for i in positions(witness):
            check ^= matrices[1][i]
        assert check == target_vector
    else:
        free_bit = residual.bit_length() - 1
        # This reduction may stop at a nonpivot above free_bit.  Full projection
        # is needed for a linear functional, so reduce all pivots descending.
        def projection(vector):
            for pivot in sorted(boundaries.pivots, reverse=True):
                if (vector >> pivot) & 1:
                    vector ^= boundaries.pivots[pivot][0]
            return vector
        projected_target = projection(target_vector)
        free_bit = projected_target.bit_length() - 1
        functional = bits(j for j in range(len(bases[2]))
                          if (projection(1 << j) >> free_bit) & 1)
        assert (functional & target_vector).bit_count() & 1
        assert all((functional & col).bit_count() % 2 == 0 for col in matrices[1])
        result["nonboundary_functional"] = [format_key(bases[2][j]) for j in positions(functional)]
        result["certificate_checks"] = {"annihilates_all_boundaries": True, "pairs_one_with_target": True}
    return result


def self_test():
    sphere = {"classes": [{"id": "a7", "degree": 7}], "bottom": "a7"}
    moore2 = {"classes": [{"id": "a7", "degree": 7}, {"id": "b8", "degree": 8}],
              "coaction": {"b8": [{"milnor": [1], "lower": "a7"}]}, "bottom": "a7"}
    moore4 = {"classes": moore2["classes"], "bottom": "a7"}
    results = {"sphere": calculate(sphere), "Moore2": calculate(moore2), "Moore4": calculate(moore4)}
    assert results["sphere"]["ext_dimension"] == 1
    assert not results["sphere"]["target_is_boundary"]
    assert results["Moore2"]["target_is_boundary"]
    assert not results["Moore4"]["target_is_boundary"]
    # Independently specified coaction detecting Sq^2 Sq^1 (the xi2 term)
    # checks the left-comodule order convention beyond primitive examples.
    ordered = {"classes": [{"id": "a7", "degree": 7}, {"id": "b8", "degree": 8},
                           {"id": "c10", "degree": 10}],
               "coaction": {"b8": [{"milnor": [1], "lower": "a7"}],
                             "c10": [{"milnor": [0, 1], "lower": "a7"},
                                      {"milnor": [2], "lower": "b8"}]}, "bottom": "a7"}
    results["ordered_xi2_comodule"] = calculate(ordered)
    ordered_sq = {"classes": ordered["classes"], "bottom": "a7",
                  "operations": {"1": {"b8": ["a7"]}, "2": {"c10": ["b8"]}}}
    converted = comodule_from_squares(ordered_sq)
    assert Comodule(converted).reduced == Comodule(ordered).reduced
    results["operation_conversion"] = converted["conversion_audit"]
    return {"self_tests_passed": True, "tests": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--coaction-output", type=Path,
                        help="Write the coaction converted from an operations input")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = self_test()
    elif args.input:
        data = json.loads(args.input.read_text())
        if "operations" in data:
            data = comodule_from_squares(data)
            if args.coaction_output:
                args.coaction_output.parent.mkdir(parents=True, exist_ok=True)
                args.coaction_output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        result = calculate(data)
    else:
        parser.error("Specify --input or --self-test")
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(json.dumps({"output": str(args.output),
                          "self_tests_passed": result.get("self_tests_passed"),
                          "target_is_boundary": result.get("target_is_boundary"),
                          "ext_dimension": result.get("ext_dimension")}))
    else:
        print(encoded)


if __name__ == "__main__":
    main()
