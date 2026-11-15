"""Exact certificates for the finite free-factor nerve-colimit example.

The group and matrix certificates are exact.  Reduced-word enumeration is
explicitly bounded and supplements, rather than replaces, the all-word
free-product normal-form proof in notes/finite_simplicial_group_route.md.
No external packages are required.
"""

from itertools import combinations
import json


def reduced(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return tuple(result)


def inverse(word):
    return tuple(-letter for letter in reversed(word))


def multiply(*words):
    return reduced(letter for word in words for letter in word)


def substitute(word, images):
    return multiply(*(images[letter] if letter > 0
                      else inverse(images[-letter]) for letter in word))


def determinant(matrix):
    """Integer Bareiss determinant, including pivot sign changes."""
    a = [list(row) for row in matrix]
    size = len(a)
    if size == 0:
        return 1
    sign, previous = 1, 1
    for k in range(size - 1):
        pivot_row = next((r for r in range(k, size) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, size):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def minors(matrix, size):
    for rows in combinations(range(len(matrix)), size):
        for columns in combinations(range(len(matrix[0])), size):
            submatrix = [[matrix[r][c] for c in columns] for r in rows]
            yield rows, columns, determinant(submatrix)


def matrix_vector(matrix, vector):
    return [sum(x * y for x, y in zip(row, vector)) for row in matrix]


def reduced_words(length, alphabet=(1, -1, 2, -2)):
    if length == 0:
        yield ()
        return
    for prefix in reduced_words(length - 1, alphabet):
        for letter in alphabet:
            if not prefix or prefix[-1] != -letter:
                yield prefix + (letter,)


def main():
    # a=1, c=2, b=3.  The two source maps are f=(a,c), g=(ab,cb^2).
    generators = {1: (1,), 2: (2,), 3: (3,)}
    automorphism = {1: (1, 3), 2: (2, 3, 3), 3: (3,)}
    inverse_automorphism = {1: (1, -3), 2: (2, -3, -3), 3: (3,)}
    compositions = {}
    for key, word in generators.items():
        left = substitute(substitute(word, automorphism), inverse_automorphism)
        right = substitute(substitute(word, inverse_automorphism), automorphism)
        assert left == right == word
        compositions[str(key)] = {"inverse_after_forward": left,
                                  "forward_after_inverse": right}

    # Normal-closure certificates for the group coequalizer.
    r_a = multiply((1,), inverse(automorphism[1]))
    r_c = multiply((2,), inverse(automorphism[2]))
    recovered_b = multiply((-1,), inverse(r_a), (1,))
    redundant_r_c = multiply((2, -1), r_a, r_a, (1, -2))
    assert recovered_b == (3,)
    assert redundant_r_c == r_c
    kill_b = {1: (1,), 2: (2,), 3: ()}
    assert substitute(r_a, kill_b) == substitute(r_c, kill_b) == ()
    assert all(substitute(generators[i], kill_b) == (i,) for i in (1, 2))

    # The four columns are f(a), f(c), g(a), g(c) in
    # H_1(BF_3) direct_sum H_1(BF_2), with minus the fold on the last rows.
    mv = [[1, 0, 1, 0],
          [0, 1, 0, 1],
          [0, 0, 1, 2],
          [-1, 0, -1, 0],
          [0, -1, 0, -1]]
    kernel_generator = [2, -1, -2, 1]
    assert matrix_vector(mv, kernel_generator) == [0] * 5
    # Last coordinate one makes this vector primitive.  The unit 3-minor
    # plus vanishing 4-minors prove rank three and torsion-free cokernel.
    unit_minor = next((rows, cols, det) for rows, cols, det in minors(mv, 3)
                      if abs(det) == 1)
    four_minors = list(minors(mv, 4))
    assert all(det == 0 for _, _, det in four_minors)
    assert kernel_generator[-1] == 1
    difference = [[0, 0], [0, 0], [-1, -2]]
    assert matrix_vector(difference, [2, -1]) == [0, 0, 0]

    # Supplement only: explicitly test every nonempty reduced source word
    # through length nine.  The proof for arbitrary length is in the note.
    max_length = 9
    word_counts = []
    for length in range(1, max_length + 1):
        count = 0
        for word in reduced_words(length):
            image = substitute(word, automorphism)
            assert any(abs(letter) == 3 for letter in image)
            assert image != word
            count += 1
        assert count == 4 * 3 ** (length - 1)
        word_counts.append(count)

    result = {
        "example": "F(a,c) => F(a,c,b), f=(a,c), g=(ab,cb^2)",
        "nielsen_inverse_generator_checks": compositions,
        "presentation_certificates": {
            "r_a": r_a,
            "r_c": r_c,
            "b_equals_a_inverse_r_a_inverse_a": recovered_b,
            "r_c_equals_c_a_inverse_r_a_squared_a_c_inverse": redundant_r_c,
            "quotient_kills_b_and_retracts_onto_F_a_c": True
        },
        "mayer_vietoris": {
            "matrix": mv,
            "rank": 3,
            "primitive_kernel_generator": kernel_generator,
            "unit_3_minor": {"rows": unit_minor[0], "columns": unit_minor[1],
                             "determinant": unit_minor[2]},
            "all_4_minors_zero": True,
            "number_of_4_minors": len(four_minors),
            "kernel": "Z",
            "cokernel": "Z^2",
            "difference_matrix": difference,
            "difference_kernel_generator": [2, -1]
        },
        "bounded_supplement_only": {
            "maximum_reduced_word_length": max_length,
            "counts_by_length": word_counts,
            "nonempty_words_checked": sum(word_counts),
            "all_g_images_have_nonzero_b_letters": True,
            "unbounded_intersection_claim_uses_written_normal_form_proof": True
        }
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
