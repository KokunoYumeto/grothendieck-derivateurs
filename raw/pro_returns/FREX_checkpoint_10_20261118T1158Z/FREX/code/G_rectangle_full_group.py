#!/usr/bin/env python3
"""Exact V,W rectangle certificate including a two-sided free-group inverse.

The finite search that suggested these words is separate.  This file checks
the displayed certificate directly and makes no global-extension assertion.
"""
import json
from pathlib import Path
from G_rectangle_local import reduce_group as red, inverse as inv, bifix, determinant
from G_rectangle_basis_search import fold


def substitute(w, assignment):
    return red(''.join(assignment[c] if c.islower()
                       else inv(assignment[c.lower()]) for c in w))


def main():
    x, y, z = 'cbabbaab', 'caabbaab', 'cbbbaab'
    w = red(y + inv(x) + z)
    assert w == 'cabbaab'
    words = dict(u1=x, u2=y, v3=z, v1=w, u3='d', v2='e')
    assert bifix(list(words.values()))
    assert red(y + inv(x) + z + inv(w)) == ''
    matrix = [[word.count(a) for word in (x, y, z)] for a in 'abc']
    assert determinant(matrix) == -1
    difference = [y.count(a) - x.count(a) for a in 'abc']
    assert difference == [1, -1, 0]

    # Formal inverse in free letters x,y,z, with uppercase denoting inverses.
    formal_w = red('yXz')
    A = red('y' + inv(formal_w))
    t = red(formal_w + 'Z')
    B = red(inv(t) + A)
    C = red(inv(B * 3 + A * 2 + B) + 'z')
    inverse_map = dict(a=red(inv(C) + A + C),
                       b=red(inv(C) + B + C), c=C)
    forward_map = dict(x=x, y=y, z=z)
    for letter, word in inverse_map.items():
        assert substitute(word, forward_map) == letter
    for letter, word in forward_map.items():
        assert substitute(word, inverse_map) == letter
    vertices, rank, folded = fold([x, y, z, w])
    assert vertices == 1 and rank == 3
    result = dict(
        scope='Full subcategory V,W only; extension to C_delta remains unconstructed',
        words=words,
        six_words_form_bifix_code=True,
        original_group_relator=True,
        abelianization_minor_determinant=-1,
        incidence_difference=difference,
        free_group_basis=['u1', 'u2', 'v3', 'u3', 'v2'],
        inverse_certificate=inverse_map,
        all_six_inverse_compositions_verified=True,
        stallings_vertices=vertices, stallings_rank=rank,
        status='PASS')
    data = json.dumps(result, indent=2) + '\n'
    print(data, end='')
    Path(__file__).with_suffix('.json').write_text(data)


if __name__ == '__main__':
    main()
