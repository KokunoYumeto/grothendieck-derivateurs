# Part A.5 and Lead 1: completed findings

The outcome is fully proved in `sections/A5.tex`, A5.1–A5.4.

| Hypotheses in addition to literal XVI Loc(1)–(3) and forward excision Loc(6′a) | Strong saturation Loc(1ter) | Relative Theorem A Loc(3bis) |
|---|---|---|
| None | Yes | No in general |
| Accessibility Loc(9) | Yes | No in general |
| Filtered-colimit closure Loc(8) | Yes | Yes |
| Both Loc(8) and Loc(9) | Yes | Yes |

The counterexample is the explicitly defined class `W_fin`: equivalences on fundamental groupoids, isomorphisms on integral homology, and ordinary weak equivalences except on finitely many connected components. It is defined for every functor of small categories. Its aspherical objects are exactly weakly contractible categories, so absolute Theorem A follows from Quillen's Theorem A. Finite forward excision follows from van Kampen, integral Mayer–Vietoris, and the finite image of the set of bad components. All weak saturation axioms are checked. It is strongly saturated by the independent finite-cofibration argument of A5.1.

`W_fin` is genuinely accessible: the proof establishes preservation of aleph1-filtered colimits and generation by countable witness-closed subfunctors. It does not confuse accessibility with ordinary filtered-colimit closure. The failure of the relative axiom is an infinite disjoint union of copies of one finite-category inclusion `Q→P`; every comma functor over the discrete base N is this inclusion, while the total map has infinitely many bad components. The same sequence of finite coproducts witnesses failure of Loc(8) and even sequential Loc(8bis).

The finite inclusion has a completely enumerated categorical presentation: P is the double collage of the degree-one and degree-two face-poset maps from the suspended hexagon to the suspended triangle. P has 58 objects and 518 arrows. Q is its two-pole subcategory with two objects and four arrows. Its classifying pair is the section circle in the mapping torus of a degree-two sphere map. The universal-cover relative differential is `2t−1`; its augmentation is 1, but its cokernel is Z[1/2]. Thus the inclusion is a pi1 and integral homology equivalence but is not a weak homotopy equivalence.

The source-based positive result uses only the CF1–CF4 axioms of a precofibration category. A finite double-collage construction proves that simplicial monomorphisms in `iDelta^{-1}W` are closed under pushout. Mapping cylinders supply factorizations. Literal Loc(1c) supplies the split-retract weak saturation hypothesis in Rădulescu-Banu Theorem 7.2.7, which gives saturation without arbitrary coproduct or sequential-composition axioms CF5/CF6. Nerve and last-vertex comparison transfer saturation back to Cat. The proof does not use a derivator or relative Theorem A, avoiding Grothendieck's footnote 55 circularity.

## Sources opened and exact use

1. Cisinski, *Astérisque* 308: primary author-hosted PDF opened, exact Theorem 6.1.18 gives W_infinity contained in every weak fundamental localizer. Proposition 3.4.25 and Theorem 4.2.15 were rechecked for the positive implication with Loc(8), together with their exact thesis counterparts in B.8. Definition of Ex and Proposition 2.1.39 supply a finitary, countability-preserving Kan replacement in the accessibility proof; preservation of filtered colimits follows directly from its finite representable formula.
2. Andrei Rădulescu-Banu, *Cofibrations in Homotopy Theory*, arXiv:math/0610009v4, dated 8 February 2009: complete primary PDF downloaded from https://arxiv.org/pdf/math/0610009v4 and read locally. The web PDF renderer returned `DisabledError` (`turn206712573view0`), while direct retrieval succeeded. Read Definition 1.1.1 (CF1–CF4 versus CF5–CF6), Definitions 7.2.5–7.2.6, and Theorem 7.2.7 with its proof. The split-retract formula in the extraction contains an incorrectly typed identity subscript; our proof writes the obvious typed identity and does not depend on that typo. The theorem is used exactly for precofibration categories, not the stronger countably cocomplete notion.
3. Quillen, *Higher algebraic K-theory: I*: primary scan hosted at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf opened (`turn206712573view1`) and downloaded. Section 1, Theorem A and its dual form were read on PDF p. 9; Proposition 3 on filtered colimits was also read. The scan has two printed paginations, so the proof cites section/theorem instead of choosing an ambiguous page number.
4. DER_FOLLOWUP G.9: read its whole proof and checked the exact step supplied by Loc(8); the finite collage argument itself does not use Loc(8). The comparison identifies W through the natural last-vertex functor rather than confusing nerve with the right adjoint of the simplex-category functor.
5. XVI manuscript transcription, ms. 1–3, 17, 71–76, 117–118: checked literal definitions of Loc1(c), Loc3/3bis, forward excision, filtered closure, and accessibility, and that footnotes 55 and 56 are Grothendieck's own text.

## Searches and discarded approaches

- Exact French weak-localizer searches and `Cisinski localisateur fondamental faible`: located Maltsiniotis *Astérisque* 301 and alternative expositions. They were not used because the opened Cisinski theorem is exact. No claim is made about unopened results in those hits.
- `Brown cofibration category saturated weak equivalences two out of six` and related finite-cofibration saturation queries: located Rădulescu-Banu Theorem 7.2.7. It resolves the saturation part without a filtered-colimit assumption.
- `Quillen Higher algebraic K theory I pdf`: the university-hosted primary scan was opened.
- `"finite components" "weak equivalences" "accessible" homotopy`: no directly matching prior source for the finite-exception construction was found. We make no priority claim.
- First attempted counterexample: maps with pi1 and integral homology equivalence and a globally perfect universal-cover relative chain cone. This appears to work via induction of perfect modules, but the proof introduces unnecessary derived-category machinery. It was replaced by the simpler finite-exception class, whose all-category axioms and accessibility are established directly. No claim from the abandoned construction is needed.
- Simple-homotopy equivalences were considered and rejected immediately as a candidate: weak localizer axioms already imply containment of all ordinary weak homotopy equivalences, by Cisinski 6.1.18.

## Reproduction

Run `python code/A5_finite_component_counterexample.py` with Python and SymPy. Saved output verifies 58 objects, 518 arrows, 1,920 composable pairs, 4,924 associativity triples, degrees 1 and 2, chain ranks (5,17,24,12), integral homology (Z,Z,0,0), and the exact Laurent-polynomial obstruction. The computation checks the finite data; the statements for all small categories and the infinite coproduct are proved in the text. There is no remaining gap in A.5 or Lead 1.
