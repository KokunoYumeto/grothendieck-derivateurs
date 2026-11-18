# A4.5 report: the countable H-space gate

## Result and status

The integrated statement is `sections/A4_hspace_review.tex`, Claim A4.5. For every prime p and every simply connected H-space H with p-primary reduced integral homology, ordinary BC_p-acyclicity is equivalent to reversible BC_p-asphericity. Equivalently,

`P_BCp(Sigma H)=*  iff  P_BCp H=*`.

For A.4 at p=2, the equality of the lower and upper primary sphere-null classes is therefore equivalent to ordinary BC_2-acyclicity of every **countable simply connected primary sphere-null H-space**. It suffices to use the countable reduced products J(Sigma X) arising from the previous A4.2 domain.

The proof and all transfers were independently reconstructed by the parent before integration, as recorded in its message of 18 November 2026: “Root independently re-proved all those transfers and sees no gap.” Parent owns the independent re-proof event in the combined check ledger. Our own events record the targeted proof and primary-source checks. The main A.4 equality, third-element and full-fibre-size problems remain open.

## Why the reduction has more content than a loop-space normal form

The replacement X→J(Sigma X) is indeed a normal-form operation for reversible predicates. The additional theorem is the equivalence between ordinary and reversible BC_p-acyclicity on the H-space domain. Its proof uses Bousfield's Key Lemma 1.6 to split a null H-space off its symmetric-product GEM; it is not a formal property of a reversible class or an assumed commutation between nullification and suspension.

The retained test spaces stay countable. The restricted domain is proper: Sigma BC_p belongs to the earlier countable domain but has no H-space multiplication, as shown by its primitive mod-p cohomology classes in degrees two and three and its zero positive-degree cup products. This example is already lower-class; it witnesses strictness of the quantified source domain, not strictness of the interval.

The parent controls the formal stopping-rule movement decision. No novelty or priority claim is made, and the classification of the surviving H-spaces is still the exact unresolved question.

## Auxiliary equivalent formulation

A separator exists exactly when a noncontractible simply connected primary H-space is both sphere-null as a source and BC_p-null as a target. Nullification preserves primary homology, simple connectivity and the H-structure in the situation used here. Its preservation of sphere-nullity follows from the universal property against each loop of every sphere target, and is checked for all positive source suspensions as well as components.

The nullified H-space need not have a countable CW model. No such countability is asserted or used. The countable gate retains the original H before its nullification.

## Source-opening and search ledger

1. **Bousfield 1996:** <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf>. Printed p.34, Theorem 1.1 and the cone-attachment construction; printed p.35, Key Lemma 1.6, its proof, the Dold–Thom GEM display, and Theorem 1.7's proof stating finite-product preservation. Opened directly at web reference `turn739374038view0` and rechecked against the local full text. The 1996 Key Lemma is the imported primary theorem. Its cited earlier 1994 Corollary 6.9 was not independently opened in this block. Existing key `ABousfield1996` is reused.
2. **Bousfield 1997:** already opened original at <https://www.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf>, Lemma 8.13 and proof. The independently checked A34.2 supplies the arbitrary-primary-GEM killing statement. Existing key `ABousfield1997` is reused.
3. **James 1955:** <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/jamesred.pdf>. Section 1's reduced-product CW construction, concatenation and filtration; Theorem 5.6, p.183, and proof pp.184–187 including the finite-subcomplex/countable passage at (5.15). Opened at references `turn581607883view0`, `turn652962587view0`, `turn652962587view1`. New owned bibliography key `A4James1955`. Parent independently opened the same original theorem and its proof.
4. **Sullivan input:** the already opened Miller source and the primary localized/completed comparison of A4.2 establish BC_p-nullity of the sphere targets. No new version or stronger finite-type hypothesis is imported here.
5. **Prior-art search scope:** parent searched combinations of H-space, sphere, nullification, Miller and Bousfield, and found no exact statement of this gate. This is a search/access report, not evidence of originality.

The longer proof-development note `notes/A4_Hspace_draft.md` records the exact transfers and remaining question. It is superseded for integrated statement numbering and status by the section and this report.

## A4.6: the finitely generated unstable-algebra subfamily

Claim A4.6 is appended to the same section. At every prime p, a simply connected primary sphere-null H-space whose mod-p cohomology is finitely generated as an algebra over the Steenrod algebra is ordinarily BC_p-acyclic. The published Castellana–Crespo–Scherer Theorem 7.2 makes its nullification have finite total mod-p cohomology. The homology UCT then bounds its primary integral homology. A nonzero last integral homology group would give a nonzero top Ext class with Z_(p) coefficients; vanishing of higher cohomology lets it lift through the entire sphere Postnikov tower, contradicting sphere-nullity. This handles arbitrary, including divisible, primary integral homology groups.

The parent independently reconstructed this deduction and opened the published theorem, its complete proof and supporting André–Quillen argument before accepting A4.6. Parent owns the independent re-proof event. Our added targeted proof event and results row are in the owned A4_hspace metadata files.

The complete development and source/search ledger are in `notes/A4_hspace_finiteness.md`; the new primary reference is `A4CCSDeconstruct2007` in `notes/A4_hspace_attempt_references.bib`. The final publication is used, not its earlier author-manuscript numbering or superseded supporting proof. Finite generation as an unstable algebra is not replaced by degreewise finite type. No realization of a candidate by finitely generated H-subspaces has been proved, so this exclusion does not settle the general gate.

## A4.7: finite cohomology extraction and the endpoint dichotomy

Claim A4.7 is appended to the same section. A connected primary space with finite nonzero total mod-p homology generates a finite nonzero primary complex under reversible aspherical closure. The construction is the cofiber of the p-fold suspension co-H map; its integral homology is finite primary in finitely many degrees, so Hatcher Proposition 4C.1 gives a finite CW model. The input is total mod-p finiteness, not finite integral homology of the original source.

The supplied REVLOC D.3.3 then implies that adjoining this source to BC_p reaches W_{Z[1/p]}. Its entire argument is included in A4.7 with exact primary references, rather than an unaudited reference to supplied background. Arone–Mahowald's published Proposition 3.1, Theorem 4.1 and full proof were opened; the finite layer connectivity was checked from Theorem 2.1. Bousfield2001 Corollary4.8 was read in its original special-nullifier convention. Published Barthel–Heuts–Meier2021 Theorem3.1 explicitly supplies the arbitrary finite suspension version needed here, with its exact d-connected hypothesis. The final Moore-nullification step is proved directly using first nonzero homotopy, so no extra Serre-class theorem is silently assumed. Full opening locators, local files and failed retrieval paths are recorded in `notes/A4_size_routes.md` Section4.

For a simply connected primary H-space with mod-p cohomology finitely generated as an algebra over the Steenrod algebra, CCS Theorem7.2 makes P_BCp H have finite total cohomology. If it is contractible, adjoining H leaves the lower endpoint; otherwise the extraction lemma and rechecked finite-addition theorem force the upper endpoint. This works without sphere-nullity and extends to any set/class presentation over BC_p by such H-spaces.

This does not prove that every localizer in the interval has a presentation by such sources, does not replace finite generation with degreewise finite type, and supplies neither a third point nor a uniform bound on the full fibre. Parent owns the final independent re-proof and stopping-rule assessment. Metadata rows were written with the CSV library and validated for missing/extra columns.

## A4.8: exact finite-loop presentations

The actual little-cubes filtration, rather than its stable splitting alone, proves min Rev(X)=min Rev(Omega^m Sigma^m X) for every connected well-pointed X and finite m. May Proposition2.6 gives NDR/cofiber filtration pairs with free-equivariant smash-power quotients, and Corollary4.6 plus pointed homotopy-colimit closure makes these quotients aspherical whenever X is. The approximation Theorem6.1 gives the forward implication; the finite suspension-loop adjunction retract and reversible desuspension give the converse.

Every primary interval class therefore has a presentation over BC_p by simply connected primary double-loop spaces Omega² Sigma³X, preserving set or class scope. This removes the loop-structure obstacle, but not finite Steenrod generation or the lack of a uniform cardinal bound. In particular, the replacement of a finite Moore generator supplies an explicit reason finite generation cannot be expected in general, using the single CCS–Hemmi exclusion incorporated into A34.6. The converse is not asserted for the infinite-loop functor Q.

Exact source openings and the full independent construction are recorded in `notes/A4_size_routes.md` Section5. Existing key `A3May1972` denotes the author-hosted 2007 transcription; original printed page images were not obtained here. Root independently proposed and checked the same filtration route; root owns its independent event and the joint same-hour progress assessment.
