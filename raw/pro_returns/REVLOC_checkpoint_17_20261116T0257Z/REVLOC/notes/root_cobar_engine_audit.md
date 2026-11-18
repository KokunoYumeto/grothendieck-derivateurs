# Root audit of the finite bottom-sigma cobar engine

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026, before checkpoint16. Generic engine review PASS;
the actual connected-cover input is still being computed.

Read all of `code/EH5_bottom_sigma_cobar.py`. The engine uses the
standard Milnor coproduct and a LEFT operation-dual homology comodule.
The normalized cobar complex is Abar tensor-power-s tensor M; the
module coaction therefore appends its algebra factor at the right.
The low nonprimitive xi2 example checks this convention beyond
primitive-only examples. The homology operation-word evaluation runs
the leftmost written Steenrod operation first, as required by duality.

The conversion from Sq-power matrices solves the complete pairing
system against Milnor monomials. It verifies every redundant word,
so inconsistent Adem actions are rejected. The resulting coaction is
checked for full coassociativity. The finite boundary matrix includes
every graded basis vector, not just those with a bottom or endpoint
coordinate. Its square is checked to be zero.

The mod-two elimination records exact witnesses. A boundary result
is checked by applying the full differential to its reported preimage.
A nonboundary result supplies a functional on every cobar-two basis
vector which annihilates every cobar-one boundary column and evaluates
to one on the proposed cycle. The full descending-pivot projection
is used for this functional; the early-stop membership reduction is
not mistaken for a linear projection.

Root reran the four generic module checks. They agree with the
sphere Ext^{2,9} class, its vanishing in the mod-two Moore comodule,
its nonvanishing in the mod-four Moore comodule, and the independently
specified xi2 coaction example. These checks certify the engine, not
the missing actual L-module input or an Adams permanence statement.

For the primary algebra convention, root opened John Milnor,
*The Steenrod Algebra and Its Dual*, Ann. Math.67(1958),150--171,
at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Milnor-A.pdf .
Theorem2 and its triangular-pairing proof are on pp159--161;
Theorem3 and its proof are on p162; Appendix1 on p171 gives the
mod-two polynomial generators and states the corresponding changes.
These are the polynomial dual, coproduct and basis-pairing inputs
used by the code. The original PDF text was opened; no new raw
reference file was added to the deliverable tree.

The exact actual input under construction is H_*(P14;F2) through
degree14, with H15(P14)=0. The image of h0h3 in the full L module
can differ because of degree15 cobar boundaries, so it must not be
substituted for this fourteen-stage test.
