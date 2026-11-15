#!/usr/bin/env python3
"""Exact checks for finite colored-word categories and affine cones.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
The unbounded proof is in examples_results.tex. These are independent finite
checks of arrow typing/composition and of the colored lifting of each cone.
The auxiliary interpolation implementation is copied, with provenance, from
attached PRETOT_return/code/semisimplicial_affine_checks.py and audited here.
"""
from collections import defaultdict
from itertools import product, combinations
from pathlib import Path
import json
from examples_affine_base import cone, to_injection_combination


def arrows(w, v):
    return [a for a in combinations(range(len(v)), len(w))
            if tuple(v[i] for i in a) == w]


def compose(b, a):
    return tuple(b[i] for i in a)


def clean(d):
    return {a: c for a, c in d.items() if c}


def post(t, a):
    result = defaultdict(int)
    for f, c in t.items():
        result[compose(f, a)] += c
    return clean(result)


def finite_category(m, max_len=3):
    words = [w for n in range(max_len + 1) for w in product(range(m), repeat=n)]
    hom = {(w, v): arrows(w, v) for w in words for v in words}
    count_arrows = sum(map(len, hom.values()))
    count_pairs = count_triples = 0
    for w in words:
        identity = tuple(range(len(w)))
        assert hom[w, w] == [identity]
        for v in words:
            for a in hom[w, v]:
                assert compose(a, identity) == a
                assert compose(tuple(range(len(v))), a) == a
                for u in words:
                    for b in hom[v, u]:
                        ba = compose(b, a)
                        assert ba in hom[w, u]
                        count_pairs += 1
                        for z in words:
                            for c in hom[u, z]:
                                assert compose(c, ba) == compose(compose(c, b), a)
                                count_triples += 1
    assert all(len(hom[(), w]) == 1 for w in words)
    atoms = [w for w in words if w and not any(v and v != w and hom[v, w] for v in words)]
    assert len(atoms) == m
    return {'m': m, 'max_word_length': max_len, 'objects': len(words),
            'arrows': count_arrows, 'composable_pairs': count_pairs,
            'composable_triples': count_triples,
            'initial_empty_word': True, 'noninitial_atoms': len(atoms),
            'identities_and_associativity': True}


def colored_cones(m, max_len=4):
    checked_words = checked_subword_embeddings = 0
    targets = []
    for length in range(1, max_len + 1):
        n = length - 1
        poly = cone(n, 1)
        blocks = n + poly.total_degree() + 1
        base = to_injection_combination(poly, n, blocks - 1)
        target = tuple(range(m)) * blocks
        for w in product(range(m), repeat=length):
            t = {tuple(m * f[i] + w[i] for i in range(length)): c
                 for f, c in base.items()}
            assert sum(t.values()) == 1
            for f in t:
                assert tuple(target[i] for i in f) == w
                assert all(i < j for i, j in zip(f, f[1:]))
            witnesses = {}
            for k in range(length + 1):
                for a in combinations(range(length), k):
                    p = tuple(w[i] for i in a)
                    value = post(t, a)
                    if p in witnesses:
                        assert witnesses[p] == value
                    else:
                        witnesses[p] = value
                    checked_subword_embeddings += 1
            checked_words += 1
        targets.append({'source_length': length, 'target_blocks': blocks,
                        'target_length': len(target), 'support': len(base)})
    return {'m': m, 'max_source_length': max_len,
            'words_checked': checked_words,
            'subword_embeddings_checked': checked_subword_embeddings,
            'all_parallel_same_color_word_embeddings_equalized': True,
            'all_augmentations_one': True, 'targets': targets}


def main():
    report = {'finite_category_checks': [finite_category(m) for m in (2, 3, 4)],
              'colored_affine_cone_checks': [colored_cones(m) for m in (2, 3, 4)],
              'scope': 'Finite checks only; universal exactness proved symbolically in paper.',
              'exclusion_scope': 'This finite computation does not prove the final-image exclusion; the paper gives its separate support-orbit proof.',
              'all_checks_passed': True}
    out = json.dumps(report, indent=2) + '\n'
    path = Path(__file__).with_name('examples_colored_words.out')
    path.write_text(out)
    print(out, end='')

if __name__ == '__main__':
    main()
