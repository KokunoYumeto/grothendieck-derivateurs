#!/usr/bin/env python3
"""Exact finite warning: C_2-cellular S_3 does not have 2-primary homology.

No external packages.  Compute normalized group homology over F_3 through
degree three.  The coequalizer presentation is checked by word reduction and
permutation multiplication; the presentation's standard dihedral normal form
has at most six elements, and its six-element permutation image is exhibited.
"""
from itertools import permutations, product
import json


def compose(g, h):
    return tuple(g[h[i]] for i in range(3))


def word_value(word, a, b):
    value = (0, 1, 2)
    for letter in word:
        value = compose(value, a if letter == 'a' else b)
    return value


def reduced_free_product_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)


def normalized_boundary_columns(group, degree, prime):
    identity = (0, 1, 2)
    nonidentity = tuple(g for g in group if g != identity)
    lower_basis = tuple(product(nonidentity, repeat=degree - 1))
    rows = {simplex: i for i, simplex in enumerate(lower_basis)}
    columns = []
    for simplex in product(nonidentity, repeat=degree):
        column = {}
        faces = [(simplex[1:], 1), (simplex[:-1], (-1) ** degree)]
        for i in range(1, degree):
            merged = compose(simplex[i - 1], simplex[i])
            if merged == identity:
                continue
            face = simplex[:i - 1] + (merged,) + simplex[i + 1:]
            faces.append((face, (-1) ** i))
        for face, coefficient in faces:
            row = rows[face]
            value = (column.get(row, 0) + coefficient) % prime
            if value:
                column[row] = value
            else:
                column.pop(row, None)
        columns.append(column)
    return columns


def rank_mod_prime(columns, prime):
    pivots = {}
    for original in columns:
        vector = dict(original)
        while vector:
            row = min(vector)
            coefficient = vector[row]
            if row not in pivots:
                inverse = pow(coefficient, -1, prime)
                pivots[row] = {i: v * inverse % prime for i, v in vector.items()}
                break
            basis_vector = pivots[row]
            for i, value in basis_vector.items():
                updated = (vector.get(i, 0) - coefficient * value) % prime
                if updated:
                    vector[i] = updated
                else:
                    vector.pop(i, None)
    return len(pivots)


def boundary_squared_zero(columns, lower_columns, prime):
    for column in columns:
        composite = {}
        for middle, coefficient in column.items():
            for row, value in lower_columns[middle].items():
                composite[row] = (composite.get(row, 0) + coefficient * value) % prime
        if any(composite.values()):
            return False
    return True


def main():
    a = (1, 0, 2)
    b = (0, 2, 1)
    identity = (0, 1, 2)
    assert reduced_free_product_word('babab' * 2) == ''
    assert reduced_free_product_word('a' + 'babab') == 'ababab'
    assert word_value('babab', a, b) == a
    assert word_value('ababab', a, b) == identity
    normal_forms = ['', 'ab', 'abab', 'a', 'aba', 'ababa']
    image = {word_value(word, a, b) for word in normal_forms}
    group = tuple(permutations(range(3)))
    assert image == set(group)
    boundaries = {n: normalized_boundary_columns(group, n, 3) for n in range(1, 5)}
    assert all(boundary_squared_zero(boundaries[n], boundaries[n - 1], 3)
               for n in range(2, 5))
    ranks = {n: rank_mod_prime(boundaries[n], 3) for n in range(1, 5)}
    homology = {n: 5 ** n - ranks[n] - ranks[n + 1] for n in range(1, 4)}
    assert homology == {1: 0, 2: 0, 3: 1}
    print(json.dumps({
        'group': 'S_3',
        'order': len(group),
        'coequalizer_maps': ['generator -> a', 'generator -> babab'],
        'presentation': '<a,b | a^2=b^2=(ab)^3=1>',
        'six_distinct_normal_forms': normal_forms,
        'coefficients': 'F_3',
        'normalized_bar_boundary_ranks': ranks,
        'homology_dimensions': homology,
        'boundary_squared_zero': True,
        'conclusion': 'C_2-cellular as a group; BS_3 is not 2-primary',
    }, indent=2))


if __name__ == '__main__':
    main()
