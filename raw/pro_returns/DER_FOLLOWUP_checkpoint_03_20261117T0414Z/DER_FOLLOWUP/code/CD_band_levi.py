"""Exhaustive Levi-equidivisibility check for the five-element band.

The nonunits are a 2-by-2 rectangular band; 1 is adjoined.
Its classifying space is S^2 by Fiedorowicz 2002, unnumbered lemma.
The finite check illustrates why equidivisibility alone is insufficient.
AI-produced, GPT-6 Astra, ChatGPT Pro, 17 November 2026.
"""

from itertools import product

one = "1"
elements = (one,) + tuple(product(range(2), repeat=2))


def mul(a, b):
    if a == one:
        return b
    if b == one:
        return a
    return (a[0], b[1])


for a, b, c in product(elements, repeat=3):
    assert mul(mul(a, b), c) == mul(a, mul(b, c))

equations = 0
for a, b, c, d in product(elements, repeat=4):
    if mul(a, b) != mul(c, d):
        continue
    equations += 1
    witnesses = [
        w for w in elements
        if (a == mul(c, w) and d == mul(w, b))
        or (c == mul(a, w) and b == mul(w, d))
    ]
    assert witnesses, (a, b, c, d)

print("monoid elements:", elements)
print("associativity checked on 125 triples")
print("equal-product quadruples checked:", equations)
print("every quadruple has a left/right Levi factor")
print("The monoid is equidivisible, but B(M) is S^2 (Fiedorowicz2002).")
print("Therefore equidivisibility alone cannot imply asphericity.")
