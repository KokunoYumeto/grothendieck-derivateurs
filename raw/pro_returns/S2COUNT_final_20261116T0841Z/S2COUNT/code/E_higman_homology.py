#!/usr/bin/env python3
"""Integral cellular checks for Higman doubles and finite star amalgams.

The proof of asphericity uses injective graphs of groups; this program checks
the ordinary cellular boundary and its Smith invariants, not asphericity.
An oriented edge glues the generator a in two copies of Higman's group.
The edge-cylinder presentation has four generators per vertex and one
extra relator a_i a_0^{-1} per edge of the star.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def higman_matrix():
    # Relators a^-1 b a b^-2, b^-1 c b c^-2,
    # c^-1 d c d^-2, d^-1 a d a^-2.
    m = sp.zeros(4, 4)
    for j in range(4):
        m[(j + 1) % 4, j] = -1
    return m


def star_matrix(k):
    # The underlying graph is a tree, whose maximal tree is collapsed.
    n = 4 * (k + 1)
    m = sp.zeros(n, n + k)
    h = higman_matrix()
    for v in range(k + 1):
        m[4*v:4*v+4, 4*v:4*v+4] = h
    for v in range(1, k + 1):
        m[0, n+v-1] = -1
        m[4*v, n+v-1] = 1
    return m


def main():
    h = higman_matrix()
    print("Higman ordinary boundary d2:")
    print(h)
    print("det(d2) =", h.det())
    assert abs(h.det()) == 1
    print("Higman: H0=Z; H1=H2=0.")
    for k in range(1, 9):
        m = star_matrix(k)
        snf = smith_normal_form(m, domain=ZZ)
        ds = [abs(snf[j, j]) for j in range(min(snf.shape))]
        assert ds == [1] * m.rows
        h2 = m.cols - m.rows
        assert h2 == k
        print(f"star k={k}: generators={m.rows}, relators={m.cols}, "
              f"all nonzero Smith invariants=1; H1=0, H2=Z^{h2}")
    print("All finite matrix checks passed. No claim of computational "
          "asphericity verification is made.")


if __name__ == "__main__":
    main()
