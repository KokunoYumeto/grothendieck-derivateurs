"""Check the integral cycles in Obraztsov (1996), p. 277, relation (2.2).

The proof in CD_E_Jonsson_obstruction.tex is symbolic and does not depend
on this finite check.  This code checks the word-level exponent formula,
including free cancellation, for a collection of small parameter values.
The admissible small-cancellation parameters in the cited construction
are much larger; the exponent identity is independent of those bounds.
"""


def reduce_word(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result


def power(word, exponent):
    if exponent < 0:
        return [-letter for letter in reversed(word)] * (-exponent)
    return word * exponent


def exponent_sums(word):
    return tuple(sum((1 if z > 0 else -1) for z in word if abs(z) == i)
                 for i in (1, 2))


checked = 0
for h in (3, 4, 7, 12):
    for n in (1, 4, 9):
        for t in (1, 2, 3):
            for aq, cq in ((1, 1), (-1, 2), (2, -1)):
                a, c = power([1], aq), power([2], cq)
                commutator = power(a, -1) + power(c, -1) + a + c
                A = a + power(commutator, t)
                vectors = []
                for k in (6, 7, 8):
                    R = power(c, -1) + power(A, n)
                    for j in range(h - 1):
                        R += c + power(A, n + 30 * j + k)
                    vector = exponent_sums(reduce_word(R))
                    predicted = (
                        aq * (h*n + 15*(h-2)*(h-1) + (h-1)*k),
                        cq * (h-2),
                    )
                    assert vector == predicted
                    vectors.append(vector)
                assert all(vectors[0][i] - 2*vectors[1][i] + vectors[2][i] == 0
                           for i in (0, 1))
                assert len(set(vectors)) == 3
                checked += 1

print(f"PASS: {checked} parameter choices; 3 relators each; "
      "word exponent sums and (1,-2,1) integral cycle verified.")
