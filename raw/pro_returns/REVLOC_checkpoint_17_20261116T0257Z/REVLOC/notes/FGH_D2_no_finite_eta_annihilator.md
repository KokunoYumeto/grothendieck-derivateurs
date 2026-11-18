# The finite eta-annihilator route is impossible

2026-11-15. Direct audit for the prime-two extension of the Thom-detection
argument in D.2.14. This closes the proposed finite-spectrum route; it does
not decide the prime-two CP-infinity localizing ideal.

## Exact statement

If F is a nonzero finite 2-local spectrum, the map

    eta smash id_F : Sigma F -> F

is nonzero. In particular neither A1, nor any finite A(n)-free spectrum,
nor any finite spectrum of higher chromatic type can supply the proposed
eta-annihilator.

## Proof

Suppose eta smash id_F were zero. The unit of the E1 endomorphism ring
End(F) would kill eta. The universal property of the E1 quotient then
gives a unital E1 ring map

    S//eta -> End(F).

Carrick, Proposition 3.10, identifies S//eta with the 2-local Ravenel
spectrum T(1). Its mod-two homology is F2[x_2], with

    psi(x_2) = zeta_1^2 tensor 1 + 1 tensor x_2.

Consequently, for every k >= 0,

    psi(x_2^(2^k))
      = zeta_1^(2^(k+1)) tensor 1 + 1 tensor x_2^(2^k).

The unit of H_*End(F) is nonzero. Indeed finite duality identifies

    HF2 smash End(F)
      ~= End_{HF2}(HF2 smash F),

and takes the unit to the identity on the nonzero graded vector space
H_*F. A nonzero finite 2-local spectrum has nonzero mod-two homology:
otherwise its bounded, finitely generated Z_(2)-homology vanishes by
Nakayama, and the finite connective-after-shift stable Hurewicz argument
forces F=0.

Naturality of the displayed coaction now forces the image of every
x_2^(2^k) in H_*End(F) to be nonzero. If one were zero, its coaction
would be zeta_1^(2^(k+1)) tensor 1, which is nonzero. This contradicts
the bounded homology of the finite spectrum End(F). Therefore eta F
is nonzero.

No inference from homology-level annihilation to nullity is involved.
Conversely this proof explains why free A(n)-cohomology cannot make
eta null as a map of a finite spectrum, even if an initial Adams
filtration representative vanishes.

## Primary source and exact interface

Christian Carrick, *Chromatic defect, Wood's theorem, and higher real
K-theories*, arXiv:2402.17519v2 (1 November 2025):

<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/carrick4.pdf>

Opened the full primary PDF. Section 3.2, printed pp.22--23:

- Proposition 3.10 identifies the E1 quotient S//eta with T(1).
- Remark 3.11 explicitly says eta E=0 iff E admits a T(1)-module
  structure, by applying the quotient universal property to End(E).
- The paragraph immediately after Remark 3.11 gives the exact coaction
  formula above and the bounded-homology contradiction for End(Ceta).
  The proof here replaces Ceta by F and explicitly verifies the only
  extra point, the nonzero unit in H_*End(F).

Thus no A1 chart computation is required. The proof is the same finite
endomorphism-ring obstruction already visible in Carrick's example.

## E1 Thom-detection interface also audited

The proposed extension of the Thom lemma from E-infinity to E1 rings is
valid. Work first in left R-modules. An extension of the bottom unit
S^(-2) -> Sigma^(-2)R across Th(-L) corresponds, by the Thom colimit
adjunction, to a natural transformation of R-module local systems

    R smash S^(-L) -> constant Sigma^(-2)R.

It is an equivalence at the basepoint and hence at every point of the
connected base CP-infinity. Applying pointwise F_R(-,R) gives an
equivalence in right R-modules

    S^L smash R ~= constant Sigma^2 R.

Its Thom orientation gives D smash R -> Sigma^2 R, where
D=Sigma-infinity reduced CP-infinity, with unit bottom restriction.
Restricting along S->R gives a nonzero map D->Sigma^2R. This contradicts
F(D,R)=0. The argument needs no commutative Picard category.

The exact primary colimit/orientation interface was independently
reopened in Ando--Blumberg--Gepner--Hopkins--Rezk (2014), Definitions
2.20 and 2.22, Theorem 2.24 (also summarized in Definitions 1.4--1.5
and Theorem 1.7):

<https://www.math.columbia.edu/~thaddeus/blumberg/5.pdf>.

The first map S^(-2)->Th(-L) in the twisted Euler sequence is a Thom
fiber inclusion: its Borel-model source identifies with
ES1_+ smash S^(-2), and restriction at any point of contractible ES1
is the fiber inclusion. This verifies the required unit condition.

The finite eta-annihilator deduction proposed from this valid E1 lemma
cannot be implemented, by the theorem above.
