# The finite normalized-cobar test for the bottom sigma class

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Proved as D.2.57. The generic engine, complete 71-class
actual input, four-class quotient calculation, and hand topological proof
have passed independent audits. The proof uses an ordinary finite P14 and
its actual four-class quotient, not a minimal stable or unstable CW model.
The final d8 and the source-changing image remain unresolved.

## Exact convention and finite range

The operation-dual homology coaction is LEFT:

    psi(m) = sum tau tensor m',
    <a tensor x,psi(m)> = <a*x,m>.

Use the standard Milnor coproduct

    Delta xi_n = sum_i xi_(n-i)^(2^i) tensor xi_i.

The normalized cobar is Abar_*^(tensor s) tensor M. Its differential splits
each algebra tensor by the reduced coproduct and appends the reduced
coaction of M at the RIGHT end. The implementation prints a key as
`(m; a1|...|as)` for convenience, but the tensor order is the one just stated.
No unrecorded switch to the opposite coproduct is allowed.

The candidate class is `[xi1|xi1^8] tensor a7` at (s,t)=(2,16). The internal
dual-algebra degree is at most nine, so only xi1,xi2,xi3 occur. The incoming
cobar-one group could use module degree fifteen, which is zero for the
fourteen-stage. The outgoing cobar-three group uses module degrees at most
thirteen. Thus the exact degree-at-most-fourteen target comodule is enough.

## Engine and certificates

`code/EH5_bottom_sigma_cobar.py` implements the following exact F2 steps.

1. Generate Milnor monomials and the multiplicative coproduct, checking its
   coassociativity through the necessary algebra degree.
2. Accept either the complete reduced left coaction or homology matrices for
   Sq1,Sq2,Sq4 (Sq8 is supported but cannot act in this target range).
3. For operation input, use every word in the square-power generators. Pair
   such a word with each Milnor monomial using the iterated standard
   coproduct. Solve the complete full-rank pairing system and verify every
   redundant word equation. This checks the Adem constraints rather than
   assuming a chosen extension of the three generator matrices.
4. Verify the resulting full left-comodule coassociativity. Form the cobar
   differentials C1->C2 and C2->C3, and check d²=0 for every C1 basis vector.
5. Test the specified bottom cocycle against the entire image C1->C2. If it
   is a boundary, emit its exact C1 preimage. Otherwise emit an explicit
   functional on C2 annihilating every boundary column and evaluating to one
   on the target. The latter is verified directly against every column.

The saved generic test output is
`code/outputs/EH5_bottom_sigma_cobar_selftest.json`. It checks the known
one-dimensional sphere Ext^{2,9}, nonvanishing of h0h3 on the sphere and
mod-four Moore, its explicit boundary on the mod-two Moore, and the
nonprimitive coaction

    psi_red b8=xi1 tensor a7,
    psi_red c10=xi2 tensor a7 + xi1² tensor b8.

The last example checks the actual operation order: its Sq2_* followed by
Sq1_* is nonzero, while the opposite order is zero. It is also independently
converted from those Sq matrices to precisely the displayed coaction.

These tests validate the finite algebra implementation. The separately
audited actual topological input uses the suspension quotients proved in
D.2.56, including both reversed-product/Browder relations in degree fourteen.
The manuscript needs only the four-class submodule and its hand proof.

## Actual ordinary-skeleton interface

Let P14 be the ordinary finite fourteen-skeleton of a finite-type CW model
of L under its bottom sphere. Restriction from L is an isomorphism in
cohomology through thirteen and is injective in fourteen. Consequently the
actual four-class Steenrod submodule restricts unchanged and dualizes to the
required comodule quotient of H_*(P14). No identification of the entire
H14(P14) with H14(L), and no minimal CW construction, is needed.

The tested h0h3 image is nonzero in Ext by the complete thirteen-column
certificate. It cannot support an Adams differential, being the image of the
permanent sphere class. It cannot be hit: the only possible incoming
differential to filtration two is d2 from Ext^{0,15}, zero because P14 has
H15=0. Finite-spectrum convergence detects a nonzero stable image of
2alpha-sigma. This rules out both remaining incoming AHSS d6 and d7 because
every nonzero subgroup of the bottom Z4 contains that element. Root and both
other research agents independently passed this actual-skeleton argument.

## Newly opened primary algebra source

Milnor, *The Steenrod Algebra and Its Dual*, Annals of Mathematics 67 (1958),
150--171, original scan:
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Milnor-A.pdf

Opened the original PDF, Theorem 3 on printed p162 and Appendix 1 on printed
p171. The former gives the dual coproduct; the appendix supplies the
prime-two polynomial algebra with generator degrees 2^n−1 and transfers the
preceding formulas to this case. The normalized code uses exactly that
coproduct. No original scan or screenshot is copied into the authored tree.
