# Full-target extension of the bottom Adams certificate

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Proved as D.2.58. Root independently passed the complete
final wrapper and actual topological input; the algebraic extension and
actual ell identity were independently audited by the other research agents.
The full-target incoming Adams d2 is not evaluated.

## 1. Actual topological input

The independent hand proof in `sections/D2_sigma_ell_input.tex` establishes
an actual class ell14 on L such that

    Sq1 ell14 = Sq2 z13,
    z13 = Sq4 Sq2 a7.

Its double cohomology suspension is the coefficient functional of the
ordinary Browder word {d5,x6}, where x is dual to v_B^2 and beta x=d+e.
The explicit primitive r12={d,x}+b{b,d} belongs to the actual E edge and
has coefficient one. The exact ambient functional identity is

    Sq1({d,x}*) = (xi x)*.

The next two bar constructions give surjectivity H13(E)->H15(L), hence
injectivity of double cohomology suspension in degree15, without assuming
the additional degree13 Eilenberg--Moore edge calculation. Thus the
identity holds in the actual L, not just in an ambient free-E2 module.

## 2. Complete symbolic cobar extension

Let Phi be the eleven-term functional of D.2.57. Interpret its module
coordinates by the same actual cohomology classes a7,s9,z13 on L. Add

    Phi_new([xi1|xi1]m14) = <ell14,m14>.

Every old incoming column with module degree <=13 is unchanged. With
module degree14, the only incoming algebra factor is xi1^2, which is
primitive, so it cannot produce the new supported pair. The old functional
still vanishes on these columns by the truncated quotient calculation.

Every degree15 incoming column is [xi1]m15. Among the old eleven supported
pairs, precisely two start with xi1, so

    Phi(d[xi1]m15) = <Sq8 a7 + Sq2 z13,m15>
                  = <Sq2 z13,m15>.

The extra term contributes <Sq1 ell14,m15>, cancelling this. There are no
incoming module degrees greater than15 in internal degree16. The bottom
cycle [xi1|xi1^8]a7 still pairs to one, and therefore the image of h0h3 is
nonzero in Ext_A^{2,16}(H^*L,F2).

This proof uses the actual ell identity and accounts for every new column;
it does not rely on a rank computation or a complete degree15 basis.

## 3. Independent exact matrix check

Input `code/outputs/I_L15_primary.json` has 104 classes, dimensions
1,2,2,5,8,11,17,25,33 in degrees7--15. Its additional geometric-extension
audit is independent of the symbolic proof above. The generic engine gives

    C1/C2/C3 = 166/362/519;
    rank d1/rank d2 = 125/234;
    Ext^{2,16} dimension = 3;
    target is a nonboundary.

All redundant operation-word pairings, the left Milnor coaction identity,
and d^2 pass. Saved outputs are

- `code/outputs/EH5_L15_Milnor_coaction.json`;
- `code/outputs/EH5_L15_bottom_sigma_cobar.json`;
- `code/outputs/EH5_L15_ell_functional_certificate.json`.

Gaussian elimination chooses L14_24 for the additional functional. The
hand-defined coefficient {d,x}* is L14_22. These differ by a Sq1-cycle.
The last file checks the exact hand normalization: the old eleven terms
plus [xi1|xi1]L14_22 annihilate every one of the 166 incoming columns and
pair to one with the bottom target. All column counts are recorded.

## 4. Exact remaining scope

The nonzero Ext class has no outgoing Adams differential by naturality
from the permanent sphere class. The only possible incoming differential
is d2 from Ext_A^{0,15}(H^*L,F2); every later source would have negative
Adams filtration. Unlike the actual fourteen-skeleton, L can have H15, so
that incoming d2 is a genuine unresolved interface.

No Adams permanence, value of h_M l4, or evaluation of the final AHSS d8
and its theta-zero source-changing image is inferred from this Ext result.
