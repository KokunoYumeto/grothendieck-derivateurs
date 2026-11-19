# Chapter II-b: audit and commentary report

**Commentary, mathematical developments, and audit by GPT-6 Astra (OpenAI, ChatGPT Pro mode).**

This report concerns the work supplied in this package. It does not attribute that work to a person or certify any subsequent editorial assembly with another model.

## 1. Corpus and method

The authoritative source is the complete attached `DER_II-b_pages.pdf`, comprising 35 leaves. Every supplied leaf was read and visually inspected against the transcription. The scope is Chapter II, manuscript pages 45–99, including the inserted pages 63bis and 64bis and the explicit blank page 68. The attached PDF is complete for this transcription; no missing leaf had to be supplied from another edition.

The three pagination systems are distinct. Attached PDF leaf 1 is printed edition page 29 and leaf 31 of the editors' complete chapter PDF. Throughout this package,

\[
\text{printed edition page}=\text{attached PDF leaf}+28,
\qquad
\text{complete chapter PDF leaf}=\text{attached PDF leaf}+30.
\]

The correction register uses **attached PDF leaf numbers**, never manuscript or printed page numbers. Manuscript labels in the claims register and commentary anchors retain the inserted `bis` pages. The reader's own page numbers constitute a fourth, purely navigational sequence and are not used as evidence locators.

The supplied `FORMAT.md`, `index_earlier.md`, cumulative bibliography, builder, and style were read. The overlap through manuscript page 53 was audited anew, while the commentary refers back to the preceding package's treatments of cofinality, the missing pointwise-limit hypothesis, biasphericity and lax epimorphisms. Substantial new commentary starts on manuscript page 54. Earlier definitions in the editors' complete Chapter II were consulted only where needed to fix the changing PS1/PS2 and weak-filtered terminology. The supplied PDF remains the authority for the present text.

The work was divided into three contiguous mathematical scopes, then integrated and cross-checked. The two new fixed-derivator examples, the transporter idempotence argument, the isofibration theorem, the open-image proof, the initial-object argument, and the six-class table received independent mathematical checks. These checks tested the proofs themselves, not merely agreement between summaries.

## 2. Deliverables and register conventions

The six prescribed files are complete:

| File | Contents |
| --- | --- |
| `DER_II-b_blocks.tex` | 30 anchored blocks, approximately 11,900 whitespace-delimited words, covering all six permitted commentary kinds |
| `DER_II-b_overview.tex` | A standalone English overview, approximately 1,600 words and three pages in the compiled reader |
| `DER_II-b_claims.csv` | 254 audit entries |
| `DER_II-b_corrections.csv` | 80 evidence-grounded records |
| `DER_II-b_references.bib` | 23 distinct references with URL or DOI and an explicit verification-scope note |
| `DER_II-b_report.md` | This report, including limitations and reproduction guidance |

The claims comprise 34 definitions, four axioms, 51 propositions, 144 claims, 11 questions, and ten remarks. Their source-status distribution is 67 `proved`, 45 `sketched`, 108 `stated`, four `assumed`, nine `open`, and 21 `false`. The last category means false **as written** or an invalid inference; it does not imply 21 independent false theorems. Some rows distinguish parts of a proposition, or a valid conclusion from its invalid justification.

`proof_status` describes the source's presentation under the stipulated convention. In particular, a question left open in the manuscript retains `open` even when the commentary supplies an answer. Present mathematical status belongs in `repair`, `references`, and `notes`. Conversely, a correctly sketched proof is not classified as false because details are supplied here. Assertions cancelled by the author were checked individually rather than being assigned a blanket negative status.

The correction records comprise three actual transcription errors, four resolved doubts, and 73 edition slips retained in the source. All 34 existing `% [sic]` flags and all four `% ??` flags are covered. Multiple correction records can concern one flag, and additional errors were found beyond those already flagged. The three mathematical transcription repairs are the endpoints of implication arrows in the final diagrams. The other exact source replacements resolve the four doubt comments; they do not change the corresponding printed mathematical readings.

The source has been preserved at three levels. `original/DER_II-b_text.tex` is the unmodified supplied transcription. `DER_II-b_transcription.tex` is its complete editable form after the recorded transcription repairs and doubt resolutions. `DER_II-b_text.tex` is the reader input, with content-neutral layout adaptations. Printed mathematical errors remain in both latter forms and are explained in the register and commentary. `DER_II-b_reader.tex` and its compiled PDF are included as requested.

## 3. Main mathematical findings

### Reconstruction of diagrams: manuscript pages 45–65

The ordinary factorization criterion in Proposition 4.1 remains the governing result. Two qualifications matter. Its Kan-extension formulation needs the relevant comma-shaped limits or colimits; the earlier package already isolates that existence issue. Its undercategory clause (d′) has the wrong cofinality orientation in the edition: the map must be co-cofinal in Definition 3.3's convention. The inclusion of the final object into the walking arrow refutes the literal printed clause. The correction is explained at the end of the proposition's proof, without changing the diplomatic source.

The question on manuscript pages 54–56 has a definite negative answer. Invertibility of the right-adjoint unit on all representables is density, not absolute density. Taking the full subcategory of sets on a singleton and a two-element set, and selecting the singleton, passes every representable-unit test but leaves the identity of the two-element set with no factorization. The commentary proves this directly and identifies its established conceptual setting in Riehl's density theorem and Adámek–El Bashir–Sobral–Velebil's characterization of lax epimorphisms. It is presented as an application of known distinctions, without an originality label.

The four-object example on pages 57–58 is checked by computing all six factorization categories over the walking composable pair. All have contractible nerves. Pulling back over the long edge nevertheless produces two disconnected objects. The full argument also explains why replacing the source by an equivalent category does not repair the universal-equivalence obstruction. This distinguishes homotopical epimorphisms from strict universal equivalences, in agreement with the later criterion of Groth and Šťovíček (2016, Theorem 6.10 in the checked arXiv v3).

Proposition 4.4 is substantially correct. The commentary gives the full slice-counit argument, carefully separating the tests provided by global diagrams from all tests on a slice. The printed Hom expression and constant-object subscripts contain type errors, which the proof itself determines. Conservativity of the relevant left Kan extension supplies exactly the missing detection step.

The conservative part of Corollary 4.7 is valid. Its parenthetical faithful assertion is false for general coherent derivators. A discrete fibration from a three-object fork to an interval sends a specified nonsplit short exact sequence of quiver representations to a split sequence. It therefore kills a nonzero degree-one derived morphism, even though binary coproducts in the coefficient derived category are faithful. The proof computes the Kan extension and an explicit splitting. It does not confuse joint conservativity of evaluation with joint faithfulness.

The proposed converse from D-connectedness to D-biasphericity on page 64bis is false. For the derivator represented by the two-element complete lattice, every diagram on a free directed two-cycle is constant. Restriction to one vertex is an isomorphism of diagram categories, but the identity of the other vertex has an empty factorization category. Both conservative-product and conservative-coproduct hypotheses fail in this example, so it respects Corollary 4.7. The literal printed question says “aspherical”; that literal claim is formally excluded by full faithfulness. The surrounding discussion clearly concerns biasphericity, and both readings are audited separately.

Finally, the composition exception in footnote 60 is incorrect: restriction along a composite is a composite of restriction functors, and composites of fully faithful functors are fully faithful. The separate assertion that all seven classes depend only on the associated class of weak equivalences is not thereby settled; its fixed-coefficient connectedness case is explicitly left unverified here.

### Stabilizers, polarities, and transporters: manuscript pages 66–89

The cancelled ending of §4 contains valid conclusions and invalid justifications. For $A\subseteq W$, the composite $NS$ is idempotent. For a pullback- and composition-closed class $L$ in `Cat`, the composite $SN$ is also idempotent for a fundamental localizer, even if identities were not explicitly required in $L$. The commentary proves the latter by separating the empty-domain case from the case where a nonempty fibre yields a product-and-retract test. Retract closure is cited correctly as a theorem of Cisinski (2006, Proposition 4.2.4, published p. 183), rather than conflated with the weak-saturation axiom.

The stronger auxiliary equalities in the printed justification can fail. With the maximal localizer and categorical equivalences, the two point inclusions into the walking isomorphism show that a stabilizer need not be a closed right-hand class. They also show directly that the stabilizer construction is not antitone. For $L=\varnothing$ and a proper $W$, the separate auxiliary equality $NSN(L)=N(L)$ fails, while $SN$-idempotence survives. These are different assertions and receive separate audit rows.

The polarity argument in §5 is valid once its two levels are distinguished: subsets of a poset, and elements representing principal lower sets. Formula (5.20) conflates them and omits closure of an ambient supremum. The corrected formula is

\[
A^{\cup\cap}=\downarrow c(\bigvee A)
=\downarrow c\bigl(\bigvee_{a\in A}c(a)\bigr),
\qquad c=\alpha_0\beta_0.
\]

The two one-dimensional subspaces of $\mathbf F_2^2$ give a complete counterexample to taking the ambient join without its closure. The ensuing closure and fixed-point theorems remain valid. The classical examples receive their necessary hypotheses: a separating dual pair, the relevant weak closure, inclusion of the origin in bipolar closures, and Krull-closed subgroups in infinite Galois theory. The dense cyclic Frobenius subgroup provides an explicit counterexample to the unrestricted subgroup claim.

The lifting example is indeed an elementwise relation between two arrows, quantified over all squares; the author retracts the contrary suggestion. A closed pair of lifting classes alone supplies no factorization theorem. The commentary makes this distinction using Riehl (2014, Definition 11.2.1).

Section 6 replaces preservation of $A$ by transport into a fixed $W$. The full transporter adjunction is proved, with all arrows in a slice included in its test. The original domain $\mathcal Q$ is too restrictive: composition-closed classes are not closed under arbitrary unions, and a transporter need not compose. The correction at (6.7) is essential. A closed pair on a four-object chain proves the second point under the abstract composition/isomorphism hypotheses of the section. Its $W$ is explicitly **not** claimed to be a fundamental localizer on categories or to satisfy two-out-of-three.

Proposition 6.1 is proved completely. For a closed pair, the right class is composition-closed exactly when it is the stabilizer of the left class. The historical block relates intrinsic $W$-fibrations to the 1991 Thomason letter and Rezk's sharp maps, including the exact role of right properness. The page-89 equivalence-stabilizer question is settled positively: the class is precisely the isofibrations. Both directions are proved, including the walking-isomorphism test for necessity, and the result is related to Rezk's categorical model structure.

### Cofiltered categories and functors: manuscript pages 90–99

The changing weak terminology is translated into three explicit conditions: a common predecessor for each pair, a commuting predecessor square for each cospan, and equalization of parallel arrows. This prevents the weaker irreducibility condition from being silently identified with the local square condition. Proposition 7.3 and the composition corollary are proved with these conditions separated.

The page-91 question about arbitrary base change has a finite-poset counterexample. Pulling back the cofiltered inclusion $\{1\}\to[1]$ along a four-object diamond produces a connected upper fork without a common predecessor for its two branches. The pullback is neither locally cofiltered nor locally weakly cofiltered. The change-of-base map is not co-étale, so the example respects the valid preservation statement in Remark 7.2. The same diamond exposes the printed variance slip concerning étale maps.

Proposition 7.4(c) must use the lower open generated by the image of $U$, not by the image of the whole slice. The literal target in print is already wrong for $U=\varnothing$. The proof correctly uses the intended definition, and the commentary supplies its full reconstruction, including the two comparison-map variances. Remark 7.5(1) repeats the missing restriction to $U$; it is recorded separately. Several étale labels in the displayed proof are unjustified, but the component-inclusion argument proves the intended statement without them.

The initial-object question in Remark 7.5(2) is settled positively. Discrete fibrations lift initial objects componentwise; the second operation selects unions of components; and a nonempty lower open contains the initial object of its ambient component. For general cofiltered categories, the later minimal-localizer theorem removes the extra Loc(8) assumption when $W$ is a fundamental localizer (Cisinski, 2004, Theorem 2.2.11).

The five separating examples in the final diagrams are worked out explicitly. The six-class table records every membership, including the common-cone invariant for a nontrivial group and the connected cone categories for the simplex category. The local condition is related to preservation of finite connected limits, the cofiltered condition to preservation of all finite limits, and the total-connectedness condition to siftedness in the opposite variance. The final block identifies the functors as representably flat in the terminology checked in Tendas (2024, Remark 2.4).

## 4. Literature verification and remaining limits

Every bibliography entry states what was actually checked and which version supplies the cited numbering. Cumulative keys are reused where available; duplicate cumulative entries were not propagated. No entry has a bare, unexplained `verified` note.

The main exact locators include Groth and Šťovíček's arXiv v3 Definition 6.1, Remark 6.3 and Theorem 6.10; Groth's published derivator axioms and represented examples; Riehl's online density chapter and 2014 weak-factorization definition; Ganter and Wille's first English edition §0.4; Milne's version 5.10, Proposition 7.12 and Theorem 7.13; Maltsiniotis's Definition 4.6, Theorem 4.13 and Example 4.17; Rezk's sharp-map Propositions 2.2 and 2.7; Cisinski's 2004 minimality theorem and 2006 retract-closure theorem; and Tendas's full publisher-text Remark 2.4. The original text of *Pursuing Stacks* §69 was distinguished from later editorial annotations, and the 1991 letter was checked at its printed pages 3–5.

Several verification boundaries are material. For Adámek–El Bashir–Sobral–Velebil (2001), publisher metadata and the abstract were available, but the full article PDF could not be retrieved. Its abstract explicitly supports the conceptual equivalences used; the relevant proof in the present reader is supplied independently. For Adámek–Rosický–Vitale (2010), metadata and the indexed author-preprint text of Remark 1.1(i) were checked; no full-paper verification is claimed. Morris's annihilator proposition was read in the publisher's primary-text extract. Schaefer and Wolff's bipolar theorem and separation proof were read through indexed primary text; full PDF retrieval failed. Shulman's 2011 post was checked through its indexed opening discussion, with Tendas supplying the full-text reference for the substantive flatness definition. These limitations are stated in the corresponding entries.

The following matters are not represented as settled beyond the evidence obtained:

1. Footnote 55's request for a single formulation encompassing the cited later Chapter XVIII cofinality result was not turned into a new unification theorem. The later Chapter XVIII and SGA4 cross-references were not independently re-proved here.
2. The dependence of fixed-D connectedness only on $W_{\D}$ is not established by the source's failed converse, and no counterexample to that distinct dependence assertion is claimed.
3. No precise matching theorem was located for the proposed general bilocal characterization of the biaspherical stabilizer or for complete intrinsic descriptions of both mixed transporters. This is a bounded search result, not a declaration that all formulations remain open today.
4. The exact lexical expansion of the printed French abbreviation “respée” was not guessed. Its visible reading is certain and its mathematical qualification is explicit in the adjacent parenthesis; that qualification is fully audited.

The five marked developments have complete proofs and statements of the sources checked. Their marks identify supplied mathematical work, not priority. Known results, including density and the isofibration characterization, are treated as known rather than relabelled as original.

## 5. Reader production, verification, and reproduction

The original builder and style are retained. All commentary anchors satisfy the format and locate a unique requested passage where a substring is used. Both CSVs have the exact prescribed headers and permitted enums; all claim IDs are unique. Citation keys resolve and bibliography entries have explicit verification notes and a URL or DOI.

The source's largest five summary diagrams cannot be made legible simply by shrinking the transcription's wide TikZ matrices. The reader therefore uses three **vector facsimile panels extracted from the authoritative attached PDF** for manuscript pages 97, 98 and 99. All diagram text, arrows, examples, and the relevant footnote are retained. Only surrounding page labels outside the diagrams are removed where the reader already supplies them. The complete corrected TikZ remains in `DER_II-b_transcription.tex`. This is a layout decision, not a mathematical emendation. Extraction coordinates and the reproducible script are included.

Other layout adaptations provide English hyphenation for the commentary, French for the source, consistent page margins, and fitting of displays only when they exceed the line width. Equation tags stay outside the fitted math boxes. A label in the seven-class diagram is given an opaque background, with arrow routing and drawing order adjusted so the diagonal does not cross its text; commentary headings are kept with their opening lines. Adjacent edition and manuscript page labels share one marginal box to prevent collisions. The four source doubts are replaced by explicit resolution comments. Edition-slip comments remain in the complete transcription. The supplied source, audited transcription, layout source, exact replacement list, and preparation script make these operations inspectable.

The included `scripts/build.sh` performs assembly, source preparation, the supplied builder, LuaLaTeX, BibTeX, and the two subsequent LuaLaTeX passes. A normal current TeX Live installation can compile the assembled reader directly. This container initially lacked the LuaLaTeX format, Lua font-loading dependencies, language configuration, and generated font maps; the included setup scripts build a local configuration without modifying system files. Those environment repairs do not change the mathematics. Runtime font/package caches and downloaded third-party books or papers are excluded from the delivery.

The final validation record and compile logs are included under `evidence/` and `logs/`. The validation checks the complete six-file contract, all anchors, bibliography keys, register structure, and the absence of unresolved source doubts. PDF verification covers every rendered page, with separate full-size inspection of the dense facsimile panels and substantive example pages. Any harmless TeX messages about displaced marginal page labels or the French package's legacy list interface are distinguished from compilation errors; no such message is used to excuse missing content, unresolved citations, or a failed build.

For a future version of the format, the most useful extension would be a dedicated present-status column beside `proof_status`, and a declared machine-readable page map. Both distinctions are currently expressed in the prescribed existing fields and the evidence files. The main mathematical source need not be silently corrected to make the reader useful: the present separation of diplomatic text, evidence register, and anchored repair is retained throughout.
