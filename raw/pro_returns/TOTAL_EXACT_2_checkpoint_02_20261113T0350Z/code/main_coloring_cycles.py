#!/usr/bin/env python3
"""Finite exploratory test; not a category construction or a universal proof.

For a cycle C_n, enumerate all proper 3-colourings.  Let D have columns
whose blocks are the vertex marginals minus the first-vertex marginal.
Compute the least positive augmentation of an integral vector in ker D,
using column Hermite normal form of [D; augmentation].

This distinguishes a finite bad-colouring obstruction from the stronger
integral affine obstruction.  It does not assert that the finite systems
extend to a quasi-filtered, exact, or total category.
"""
import itertools
from sympy import Matrix, ilcm
from sympy.matrices.normalforms import hermite_normal_form


def main():
    print("n,proper_colourings,rank_D,augmentation_generator")
    for n in range(3, 10):
        colourings = [
            x for x in itertools.product(range(3), repeat=n)
            if all(x[i] != x[(i + 1) % n] for i in range(n))
        ]
        matrix = Matrix([
            [int(x[i] == c) - int(x[0] == c) for x in colourings]
            for i in range(1, n) for c in range(3)
        ])
        augmented = matrix.col_join(Matrix([[1] * len(colourings)]))
        basis = hermite_normal_form(augmented)
        target = Matrix([0] * (augmented.rows - 1) + [1])
        coordinates, parameters = basis.gauss_jordan_solve(target)
        assert parameters.rows == 0
        assert basis * coordinates == target
        generator = 1
        for coordinate in coordinates:
            generator = ilcm(generator, coordinate.q)
        # HNF columns are an integral lattice basis; these denominators
        # therefore give the exact order of the target in its saturation.
        assert all((generator * v).q == 1 for v in coordinates)
        print(f"{n},{len(colourings)},{matrix.rank()},{generator}")
    certificate = [
        (1, (0, 1, 0, 1, 2)),
        (1, (2, 0, 2, 1, 0)),
        (-1, (2, 1, 2, 1, 0)),
        (1, (1, 0, 2, 0, 2)),
        (-1, (1, 0, 2, 1, 2)),
        (1, (1, 2, 0, 1, 0)),
        (-1, (1, 2, 0, 1, 2)),
    ]
    assert all(all(x[i] != x[(i + 1) % 5] for i in range(5))
               for coefficient, x in certificate)
    assert sum(coefficient for coefficient, x in certificate) == 1
    marginals = [
        [sum(coefficient for coefficient, x in certificate if x[i] == c)
         for c in range(3)] for i in range(5)
    ]
    assert marginals == [[1, 0, 0]] * 5
    print("C5 signed certificate:", certificate)
    print("C5 marginals:", marginals)
    print("Scope: finite local constraint only; no category exactness claim.")


if __name__ == "__main__":
    main()
