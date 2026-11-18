#!/usr/bin/env python3
"""Exact finite checks for the positive-matrix attempt note.

This checks the explicitly finite no-FreeMon-lift example and the exact
rank-one Nielsen-splitting identities. It does not test or prove a universal
FreeMon statement about C_delta.
"""
from pathlib import Path
import itertools
import json


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter.swapcase():
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)


def inverse(word):
    return ''.join(letter.swapcase() for letter in reversed(word))


def substitute(word, images):
    return reduce_word(''.join(images[c] if c.islower() else inverse(images[c.lower()])
                               for c in word))


def abelianize(word, alphabet):
    return [word.count(c) - word.count(c.upper()) for c in alphabet]


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def main():
    f = [[1], [1]]
    g = [[1, 0], [0, 1]]
    h = [[0, 1], [1, 0]]
    assert matmul(g, f) == matmul(h, f)
    candidates = sorted(set(''.join(p) for p in itertools.permutations('ab')))
    rows = []
    for word in candidates:
        lhs = word
        rhs = ''.join({'a': 'b', 'b': 'a'}[c] for c in word)
        rows.append({'f_word': word, 'g_f': lhs, 'h_f': rhs, 'equal': lhs == rhs})
    assert len(rows) == 2 and all(not row['equal'] for row in rows)

    group_h = {'a': 'abA', 'b': 'a'}
    group_h_inverse = {'a': 'b', 'b': 'Bab'}
    assert substitute('ab', group_h) == 'ab'
    compositions = {}
    for c in 'ab':
        compositions[c] = {
            'h_inverse_h': substitute(substitute(c, group_h), group_h_inverse),
            'h_h_inverse': substitute(substitute(c, group_h_inverse), group_h),
        }
        assert set(compositions[c].values()) == {c}
    group_matrix = [list(row) for row in zip(*(abelianize(group_h[c], 'ab') for c in 'ab'))]
    assert group_matrix == h

    new_to_old = {'x': 'aG', 'y': 'b', 'z': 'gb'}
    old_to_new = {'a': 'xzY', 'b': 'y', 'g': 'zY'}
    tau = {'a': 'ba', 'b': 'bab', 'g': 'g'}
    expected = {'x': 'yx', 'y': 'yxz', 'z': 'zxz'}
    actual = {}
    for c in 'xyz':
        assert substitute(new_to_old[c], old_to_new) == c
        actual[c] = substitute(substitute(new_to_old[c], tau), old_to_new)
        assert actual[c] == expected[c]
        assert actual[c].islower()
    for c in 'abg':
        assert substitute(old_to_new[c], new_to_old) == c

    report = {
        'status': 'all exact finite checks passed',
        'scope': 'Finite direct positive-matrix diagram and one Nielsen splitting only; no C_delta conclusion',
        'matrix_diagram': {'f': f, 'g': g, 'h': h, 'gf': matmul(g, f), 'hf': matmul(h, f)},
        'all_possible_FreeMon_f_words': rows,
        'free_group_lift': {
            'h': group_h, 'inverse': group_h_inverse, 'both_composites': compositions,
            'h_ab': substitute('ab', group_h), 'abelianization': group_matrix,
        },
        'nielsen_basis': {'new_to_old': new_to_old, 'old_to_new': old_to_new},
        'tau_in_new_basis': actual,
        'exhaustiveness_reason': 'A nonnegative word with abelianization (1,1) is exactly ab or ba; identity and transposition columns force the letter images of g and h.',
    }
    out = Path(__file__).resolve().parent / 'outputs' / 'D_positive_checks.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
