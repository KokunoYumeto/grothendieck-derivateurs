#!/usr/bin/env python3
"""Check the finite obstruction to inferring asphericity from an exponent matrix.

Presentation used in Mikhailov--Orr, arXiv:1306.6065, Example 3.2:
    <a,b | a^5=b^3, b^3=(ba)^2>.
The exponent matrix has determinant -1, but the group has order 120.
An ordinary two-dimensional presentation complex for this nontrivial finite
group cannot be aspherical.  Row/column Nielsen transformations can turn
the exponent matrix into the identity without changing that obstruction.

Requires SymPy.  The computation is a finite check, not the topological
proof of the obstruction.
"""

import sympy
from sympy import Matrix
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup


def main():
    free, a, b = free_group("a,b")
    relators = [a**5 * b**-3, b**3 * (b * a)**-2]
    exponent = Matrix([
        [sum(sign for letter, sign in r.array_form if letter == generator)
         for generator in (a.array_form[0][0], b.array_form[0][0])]
        for r in relators
    ])
    assert exponent == Matrix([[5, -3], [-2, 1]])
    assert exponent.det() == -1
    presented = FpGroup(free, relators)
    assert presented.order() == 120
    permutation_group, hom = presented._to_perm_group()
    aa, bb = hom(a), hom(b)
    identity = permutation_group.identity
    assert hom(relators[0]) == identity
    assert hom(relators[1]) == identity
    common = aa**5
    assert common == bb**3 == (bb * aa)**2
    assert common.order() == 2
    assert common * aa == aa * common
    assert common * bb == bb * common
    assert permutation_group.order() == 120
    assert permutation_group.is_transitive()
    print("SymPy version:", sympy.__version__)
    print("Presentation: <a,b | a^5=b^3, b^3=(ba)^2>")
    print("Exponent matrix:", exponent.tolist())
    print("Determinant:", exponent.det())
    print("Todd--Coxeter group order:", presented.order())
    print("Permutation image order:", permutation_group.order())
    print("Orders of a, b, ba:", aa.order(), bb.order(), (bb * aa).order())
    print("Order of common central element a^5=b^3=(ba)^2:", common.order())
    print("PASS: unimodular exponent matrix does not ensure asphericity")


if __name__ == "__main__":
    main()
