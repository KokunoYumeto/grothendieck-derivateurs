"""Exact F_2 tensor calculations for the two-Moore Lie retract in D.1.8.

This checks finite linear algebra only. The geometric interpretation is
recorded separately and is not inferred from the program alone.
"""

from itertools import combinations, product
import json
from pathlib import Path


def xor_sets(a, b):
    return a.symmetric_difference(b)


def bracket_words(words, letter):
    result = set()
    for word in words:
        for term in (word + (letter,), (letter,) + word):
            if term in result:
                result.remove(term)
            else:
                result.add(term)
    return result


def dynkin(word):
    result = {word[:1]}
    for letter in word[1:]:
        result = bracket_words(result, letter)
    return result


def permute(word, permutation):
    return tuple(word[i] for i in permutation)


def phi(word):
    """Iterated projection p_3: 010,100 ->0; 011,101 ->1."""
    value = word[0]
    for i in range(1, len(word), 2):
        triple = (value, word[i], word[i + 1])
        if triple in ((0, 1, 0), (1, 0, 0)):
            value = 0
        elif triple in ((0, 1, 1), (1, 0, 1)):
            value = 1
        else:
            return None
    return value


def initial_words(k, initial):
    result = set()
    for choices in product((0, 1), repeat=k):
        word = (initial,)
        for choice in choices:
            word += (choice, 1 - choice)
        result.add(word)
    return result


def image(k, initial, permutation):
    result = set()
    for word in initial_words(k, initial):
        result ^= dynkin(permute(word, permutation))
    return result


def coefficient(words, permutation, output):
    return sum(phi(permute(word, permutation)) == output for word in words) % 2


def dynkin_expansion(word):
    """Uncancelled closed-form expansion, independent of bracket_words.

    At each commutator step the new letter is put on the right or left.
    Left-hand choices occur in reverse order, followed by the first
    letter and the right-hand choices in their original order.
    """
    for choices in product((0, 1), repeat=len(word) - 1):
        left = [word[i + 1] for i, choice in enumerate(choices) if choice]
        right = [word[i + 1] for i, choice in enumerate(choices) if not choice]
        yield tuple(reversed(left)) + word[:1] + tuple(right)


def raw_count(k, initial, embedding, projection):
    return sum(
        phi(permute(term, projection)) == initial
        for word in initial_words(k, initial)
        for term in dynkin_expansion(permute(word, embedding))
    )


def main():
    n = 11
    k = (n - 1) // 2
    permutations = [tuple(range(n))]
    labels = ["identity"]
    for a, b in combinations(range(n), 2):
        permutation = list(range(n))
        permutation[a], permutation[b] = permutation[b], permutation[a]
        permutations.append(tuple(permutation))
        labels.append(f"({a + 1} {b + 1})")

    images = [image(k, 0, perm) for perm in permutations]
    columns = [
        tuple(coefficient(words, perm, 0) for perm in permutations)
        for words in images
    ]
    witness = None
    for a, b in combinations(range(len(permutations)), 2):
        for c, d in combinations(range(len(permutations)), 2):
            matrix = [[columns[a][c], columns[b][c]],
                      [columns[a][d], columns[b][d]]]
            if (matrix[0][0] * matrix[1][1]
                    + matrix[0][1] * matrix[1][0]) % 2:
                witness = (a, b, c, d, matrix)
                break
        if witness:
            break
    if witness is None:
        print("No rank-two minor among identity and transpositions")
        return

    a, b, c, d, matrix = witness
    upper_images = [image(k, 1, permutations[t]) for t in (a, b)]
    upper = [[coefficient(words, permutations[t], 1)
              for words in upper_images] for t in (c, d)]
    assert matrix == upper, (matrix, upper)
    assert [labels[a], labels[b]] == ["identity", "(1 8)"]
    assert [labels[c], labels[d]] == ["identity", "(1 3)"]
    assert matrix == [[1, 1], [1, 0]]
    raw_matrices = [
        [[raw_count(k, initial, permutations[j], permutations[i])
          for j in (a, b)] for i in (c, d)]
        for initial in (0, 1)
    ]
    assert raw_matrices[0] == raw_matrices[1] == [[3125, 3125], [3039, 2460]]
    assert [[entry % 2 for entry in row] for row in raw_matrices[0]] == matrix
    # Check the closed-form expansion against the commutator recurrence
    # on all source words used by the two actual geometric embeddings.
    for initial in (0, 1):
        for j in (a, b):
            for word in initial_words(k, initial):
                permuted = permute(word, permutations[j])
                expansion = set()
                for term in dynkin_expansion(permuted):
                    expansion.symmetric_difference_update((term,))
                assert expansion == dynkin(permuted)
    result = {
        "n": n,
        "embedding_permutations": [labels[a], labels[b]],
        "projection_permutations": [labels[c], labels[d]],
        "lower_matrix": matrix,
        "upper_matrix": upper,
        "embedding_word_counts": [len(images[a]), len(images[b])],
        "independent_uncancelled_counts_lower": raw_matrices[0],
        "independent_uncancelled_counts_upper": raw_matrices[1],
        "closed_form_checked_against_recurrence": True,
    }
    output = Path(__file__).parent / "outputs" / "I_lie_moore.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
