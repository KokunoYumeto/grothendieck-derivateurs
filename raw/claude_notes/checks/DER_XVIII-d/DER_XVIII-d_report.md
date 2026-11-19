# Les Dérivateurs, Chapter XVIII, part d: audit and commentary report

Commentary, audit, and mathematical developments produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. This report does not certify any subsequent assembly or editing with Claude or another system.

## Scope and documentary method

The entire supplied transcription was read, from its opening continuation through the unfinished argument on manuscript page 429. The authoritative attachment contains 45 PDF leaves: leaves 121–165 of the editors’ complete Chapter XVIII file, printed edition pages 119–163, and manuscript pages 316–429. The opening paragraph continues manuscript page 315. Manuscript page 320 is explicitly cancelled in the edition; no mathematical text has been reconstructed for it.

The three page systems remain distinct. The correction register uses the one-based leaf number in the attached PDF. Manuscript pages identify commentary anchors and claim locations. Printed edition pages and manuscript-page markers appear in the reader’s margin. For this attachment, PDF leaf number equals printed edition page minus 118.

All 45 authoritative leaves were rendered and inspected visually. Extracted PDF text assisted navigation, with the page image controlling disputed formulas, subscripts, arrows, and words. The audit includes definitions, named results, substantive unnumbered assertions, intermediate inferences, questions, diagrams, and footnotes.

The transcription contains **64 [sic] occurrences on 63 lines**, together with **two doubtful-reading annotation lines**. All 65 flag-bearing lines were checked. The oblique arrow at manuscript page 336 has both arrowheads, as transcribed. The curved marginal mark at page 379 is nonverbal; no linguistic interpretation has been invented.

No verified difference between a mathematical reading in the transcription and the supplied edition PDF was found. The correction register has **121 edition_slip_kept rows and two doubt_resolved rows**, with no transcription row. Several records concern additional slips found during the mathematical reading, and some aggregate adjacent flags. “Edition slip” means that the problematic reading is printed in the authority. It does not assign the error to the manuscript, decipherment, or electronic typesetting; no facsimile comparison establishing that further attribution was undertaken.

The edition’s mathematical readings remain in the text. The prepared source resolves the two doubtful-reading comments and makes rendering-only repairs: nested circled TikZ labels no longer inherit arrow-label math hooks; the two bold capital Deltas at manuscript page 423 use a mathematical bold-symbol command; and a missing space after an oval box at page 326 is restored. The original uploaded transcription is separately preserved. These changes, the bilingual layout, and the title page are reproducible in the source-preparation script.

The supplied earlier commentary index ends with DER_XIIapp and contains no Chapter XVIII blocks. Consequently no comparison with a preceding Chapter XVIII commentary was possible from that index. The apparatus invents no predecessor title or cross-reference.

## Contents and status conventions

The six prescribed files are complete. The archive also contains the built reader source and PDF, prepared source, unchanged kit builder and companion style, original inputs, authored code, interval working files, and validation records.

| Component | Extent |
|---|---:|
| Commentary blocks | 31, covering all six permitted kinds |
| Commentary length | Approximately 14,700 whitespace-delimited tokens, including TeX |
| Claim register | 223 rows |
| Correction register | 123 rows |
| Bibliography | 14 entries |
| Development blocks | 6 |
| Result-level “ours” markers | 8 |

All **56 in-range numbered units** have substantive audit coverage: 4.13.17–39; 4.14.1–26 and its four subordinate lemmas/corollaries; and 4.15.1–3. The claim register also covers the relevant unnumbered material. The overview occupies three rendered pages, within the requested two-to-five-page range.

The source-treatment convention follows FORMAT.md. “Proved,” “sketched,” “stated,” “assumed,” “conjectured,” and “open” describe what the source does. Modern repairs and counterexamples belong in the other columns. “False” means that an assertion or inference fails as written, including a false intermediate cardinal-arithmetic claim. Missing proof details alone do not justify that label.

| Source-treatment status | Rows |
|---|---:|
| Proved | 100 |
| Sketched | 46 |
| Stated | 50 |
| Assumed | 5 |
| Conjectured | 5 |
| False as written | 16 |
| Open in the source | 1 |

These are **audit-row counts, not counts of independent theorems**. A single error may affect several corollary components, while one row may enumerate several parts of a statement. Some source conjectures receive positive or negative answers in the commentary while retaining their source status.

Grothendieck’s cardinal convention is translated consistently. “Grand devant \(\pi\)” requires cocones on diagrams with at most \(\pi\) arrows, and therefore means modern \(\pi^+\)-filteredness. His \(\pi\)-accessible objects are modern \(\pi^+\)-presentable objects. The parameter \(\pi\) itself need not be regular. Accessibility of a full subcategory in its ambient category retains the behavior of the inclusion; abstract accessibility alone is insufficient for several conclusions at issue here.

## Cofinality, presentations, and envelopes: pages 316–374

Lemma 4.13.17 is valid with its ordinal-colimit hypotheses. A final functor need not have a final strict inverse image of a final full subcategory without those hypotheses; the even and odd cofinal subsets of the ordered natural numbers illustrate the obstruction. The commentary completes the final-colimit comparison and proves that the successor-stage equalizations on pages 323–327 are redundant. The two adjacent-composite identities and earlier naturality already imply the remaining squares. This simplifies a valid proof rather than refuting the lemma.

Theorem 4.13.22 is explained through adapted presentations. The proof begins with small ambient objects and then restricts to stages lying in the accessible subcategory. The full category of divisible abelian groups supplies a worked example using countable divisible enlargements. The presentation of the rationals by cyclic groups shows why an arbitrary filtered presentation does not suffice.

At page 336, the claim that the initial ordinal of a singular cardinal is large before every smaller cardinal is false. Choosing an ordinal of cardinality \((\pi'_0)^+\leq\pi\) supplies precisely the filteredness required by the proof without enlarging its final rank.

Proposition 4.13.24 needs ordinal-colimit closure or an explicit retract-closure replacement. Footnote 152 removes the former without retaining the latter. The commentary disproves the weakened assertion using the full replete category of two-element sets: an ordinal diagram with a fixed nonidentity idempotent has a singleton colimit. Thus the small part of its Ind-image is larger than the original category. The corrected correspondence retains ordinal closure or imposes retract closure.

The GCH shortcut on pages 347–348 is false for singular cardinals of small cofinality. The instance \(\lambda=\aleph_\omega\), \(\mu=\aleph_0\) refutes the assertion \(\lambda^\mu=\lambda\) for all \(\lambda>\mu\). A cofinality restriction repairs that shortcut. The alternative enlargement by sufficiently large powers of two remains valid.

The qualitative inverse-image theorem 4.13.31 survives. Corollary 4.13.32 contains a wrong ambient-category symbol and a rank mismatch: the proof uses \(\pi\) useful for the ambient category, whereas the hypothesis states usefulness of \(\pi_0\). A common sufficiently large rank repairs the argument; the narrower unstrengthened bound is not certified.

The essential-image conjecture 4.13.33 fails even after retract closure. The commentary works out the split-monomorphism example in Rosický (2009, Example 3.5(1)) and Brooke-Taylor and Rosický (2017, Remark 3.3(2)). Forgetting chosen retractions gives a retract-closed full image. At every regular rank, a chain of split inclusions of ordered sets has a colimit inclusion that does not split. The conclusion is failure of accessible embedding; no unnecessary assertion about every abstract accessibility structure of the full image is made.

The controlled small-envelope questions on pages 354–355 receive a complete positive proof. If an accessible category admits all small \(\kappa\)-filtered colimits and the colimits of a small family of small shapes, then the smallest replete full envelope of a small family of objects under those operations is accessible and accessibly embedded. The proof chooses \(\pi\) with \(\pi^{<\kappa}=\pi\), completes bounded subcategories of an indexing category through \(\kappa\) stages, and expresses the indexing category as a \(\pi^+\)-filtered union of those bounded subcategories. The Ind construction supplies the envelope. Retract closure is obtained explicitly from the ordinal \(\kappa\).

Lemma 4.13.38 receives a shorter finite-witness proof. In the exceptional-vertex construction, the incoming cocone arrows must be included before the vertex is declared weakly terminal in the small category. The local printed category-name slips are recorded separately. Continuity of the adapted diagram remains essential.

## Marked constructions, adjoints, and epimorphisms: pages 369–390

Theorem 4.14.1 expresses marked universal conditions as accessible comparison maps being invertible. The diagrams must be defined on the cone or cocone categories, not merely their bases, as the edition accidentally prints. The target completeness hypotheses are retained.

The proof of 4.14.3 invokes target filtered colimits absent from its hypotheses. Adding the specified \(L_{\pi_0}\) condition on the target validates that proof. Accessibility of the target alone does not justify the invocation. The related incomplete-target assertions in 4.14.6(a) and 4.14.7 are not certified by formal duality. The later target-free theorem proved in the extract concerns existing limit cones; the corresponding colimit-cone assertion includes the epimorphism problem.

The continuous-functor assertions in 4.14.9, the left-adjoint half of 4.14.10, and the covariant half of 4.14.11 are false. A complete Bass-type construction on groups preserves all small limits but has no representing group. It uses simple finitary alternating groups of unbounded cardinality, with only set-many nontrivial factors on each argument. SGA 4 I.8.12.9 already supplies the obstruction, and Grothendieck recalls it on manuscript pages 50–52. The repair requires accessibility together with continuity, as in Tendas (2022, Theorems 2.9 and 2.11). The cocontinuous/right-adjoint assertion under the source’s pseudo-topos hypothesis remains valid.

The comparison tests for isomorphisms, monomorphisms, and limit cones are reconstructed using small families of representable functors. Generation and strong generation are distinguished. If pushouts exist, an arrow is epic exactly when the codiagonal from its self-pushout is invertible. The commentary proves this criterion and the resulting accessible epimorphism locus. Examples include surjections of sets and the ring epimorphism \(\mathbb Z\to\mathbb Q\), whose tensor-product pushout is calculated.

Question 4.14.15 retains the source status “open.” The commentary proves
\[
 \operatorname{Epi}(\mathcal K)\text{ accessible and accessibly embedded}
 \Longrightarrow \mathcal K\text{ co-wellpowered}.
\]
For each \(X\), an accessible iso-comma construction gives its epimorphic-quotient preorder. An accessible preorder is essentially small: an object is determined up to isomorphism by the subset of a fixed small set of presentable generators mapping to it. The complete argument appears at the page-390 anchor.

Bagaria et al. (2015, pp. 574–575) record a measurable-cardinal lower bound for universal co-wellpoweredness and a strongly-compact-cardinal sufficient assumption. Together with the proved implication, this gives a necessary large-cardinal lower bound for a universal affirmative epimorphism assertion. It does not determine that assertion’s exact consistency strength or prove a converse. Positselski’s 2026 work was screened through its publisher abstract and metadata; its subject is pure epimorphisms, and no result about all epimorphisms is inferred from that screening.

## Sections, collages, and ranks: pages 391–429

The qualitative section, cartesian/cocartesian section, comma, and iso-comma accessibility theorems are valid. The proofs use products, inserters, equifiers, and accessible isomorphism loci, with the coherence of a nonsplit cleavage retained. The cospan-section construction of 4.14.21 is checked on objects and morphisms and is not circular in its subsequent application.

The fixed-rank condition in 4.14.18(b) differs by variance. For a fibration, the natural-transformation equalizer proves pointwise presentability sufficient. For an opfibration, its Hom factors involve transported source objects, whose presentability does not follow from filtered-colimit preservation. The counterexample uses constant transport on sets with value \(B\), \(|B|=\lambda\). The section \((\varnothing,B\to1)\) has finite component values but is not \(\lambda\)-presentable. Quotients identifying fewer than \(\lambda\) elements at each stage give the witnessing filtered diagram. Requiring transported source objects also to be presentable repairs the sufficient condition.

A separate example refutes the first numerical pointwise equality in 4.14.18(c) and the pointwise equality in 4.14.20(c). The opfibration classified by \(\mathbf1\to\mathcal P(S)\), selecting \(S\), has a unique section. That section is cocartesian and presentable at every rank, while its forced value \(S\) need not be presentable at the printed rank. The later extra fibre-skeleton bound excludes the example. Its precise sufficiency in full generality is not independently certified; a common strong accessibility rank for transports and evaluations gives a safe eventual repair.

Corollary 4.14.20(b) survives. For a cocartesian section, the transported source is isomorphic to the target component, so pointwise presentability supplies the missing Hom-source bound. The unrestricted opfibration counterexample does not apply to this restricted statement.

The adjunction directions in the necessity argument for 4.14.23.1 are reversed in the edition. In the opfibration case, extended transport is left adjoint to inclusion of the target fibre. In the fibration case, inclusion of the source fibre is left adjoint to extended transport. Lemma 4.14.23.2 is correct; the commentary supplies its common-rank and strong-generator proof.

Corollary 4.14.25(1) omits the closed fibre’s filtered-colimit hypothesis from one side of an equivalence. A nonempty counterexample uses an ordinal closed fibre without a greatest element, a terminal open fibre, and singleton cross-Hom sets. The printed right side holds while the total category lacks the required filtered colimit. Adding the missing closed-fibre hypothesis repairs the equivalence.

Theorem 4.14.26 validly extends section accessibility to intervalwise accessible data without a fibration structure. The inserter’s arrows and equations are described explicitly. The hooked arrow from an inserter to its product category is a notation slip: the forgetful functor need not be full.

The explicit bound in 4.15.2(c), and hence its use in (d), fails. Contravariant preservation ranks are bounded by \(\pi_1\) in the statement, while the proof uses them below \(\pi_0\). The opfibration of \(X\mapsto X^K\) on sets, with \(|K|=\aleph_1\), supplies a ZFC counterexample. Set \(\pi_0=\aleph_0\), \(\pi_1=2^{\aleph_1}\), and \(\pi=\beth_{\omega_1}\). All printed size and power bounds hold. A lower-fibre set of size \(\pi\) is presentable at that rank in its fibre but not in the total category, because \(\pi^{\aleph_1}>\pi\). The commentary gives the cardinal arithmetic and the witnessing diagram. Choosing \(\pi_0\) initially above all contravariant preservation ranks repairs the qualitative construction.

Two independent notation errors in 4.15.2(c) are recorded: the total category has the asserted filtered colimits, and the Ind-equivalence uses the union of small objects from all fibres. A one-object category with a non-split idempotent gives a worked example explaining the separate hypothesis on idempotents in the base.

## Supplementary reading and limits of certification

The official complete Chapter XVIII was consulted for the background in 4.4.4, 4.11.1, and 4.13.11–15; the warning on pages 50–52; the pseudo-topos definition near page 106; and the continuation on pages 430–432, 452, and 462–463. This is supplementary reading, not a claim that those pages belong to the attachment.

Page 430 confirms the missing contravariant rank usage. Pages 431–432 supply the reverse presentability argument after the forward inclusion is repaired. Page 452 still invokes the then-unproved 4.8.13. The later 4.15.10–11 on pages 462–463 justify the constant-subdiagram step with the strict inequality \(\pi>|\mathcal C|\). Qualitative accessibility follows after enlargement; the equality boundary is not certified here.

The following limitations remain explicit:

1. The third variant of 4.13.21 is verified under the sufficient cardinal closure condition of the bounded-index proof. Its exact inference from the bare additional ordinal-colimit hypothesis is not established here.
2. The weaker printed rank condition in 4.13.32 is not independently certified; the common-rank repair is valid.
3. The incomplete-target colimit clauses in 4.14.3, 4.14.6(a), and 4.14.7 are not established by the checked proofs. No invented counterexample is supplied.
4. The later extra fibre-skeleton bound in 4.14.18(c) excludes the counterexample, but its full numerical sufficiency is not certified.
5. The weakened adjunction hypotheses suggested in footnote 172 are not proved by the checked argument and are not asserted to have a known counterexample.
6. The equality case \(\pi=|\mathcal C|\) of the constant-subdiagram lemma and the exact consistency strength of the unrestricted epimorphism assertion are not settled.

These are limits of verification, not new declarations that the modern literature has open problems at every such point. The audit covers the statements even when their strongest printed formulations remain uncertified.

## Literature verification

Every bibliography entry has a URL or DOI and an explicit note describing the version and verification scope. Existing cumulative keys are reused. Comparisons concern the accessible-category mathematics of these pages; unrelated derivator references have not been added merely because they were examples in the task prompt.

| Work | Verification scope |
|---|---|
| Grothendieck, Chapter XVIII | Entire attached range, all flagged readings, and the specific supplementary portions listed above. |
| Artin, Grothendieck, and Verdier (1972), SGA 4 I | 8.7.2–8.7.3; 8.12.7–8.12.9; 8.13.2. The manuscript’s additional citations I.8.8.5 and I.9.8 are identified without claiming fresh inspection of their proofs. |
| The Stacks Project, Tags 04AX and 09WN | Filtered-colimit and cofinality definitions and the cited eventual-equality/cofinality criteria. |
| Gabriel and Ulmer (1971) | Publisher metadata and contents only; historical use. |
| Makkai and Paré (1989) | Publisher metadata and theorem attribution through inspected primary papers; the original book proof was unavailable. |
| Adámek and Rosický (1994) | Publisher metadata and Chapter 2 synopsis, including Proposition 2.23; the original proof was unavailable, and an independent proof is given. |
| Rosický (2009) | Author manuscript Example 3.5(1) and publisher metadata. |
| Brooke-Taylor and Rosický (2017) | Accepted version, Section 2, Theorems 3.2 and 3.4, Remark 3.3(2), Corollary 3.5; version-specific numbering retained. |
| Lurie (2009) | Author-hosted Higher Topos Theory, Proposition 5.4.7.11, Remarks 5.4.7.13–14, Lemma 5.4.7.15, and the relevant construction. |
| Tendas (2022) | Publisher full text, Theorems 2.9 and 2.11 with relevant proofs. |
| Positselski (2024) | Published introduction and relevant results in Sections 3–10, including section constructions and Lemmas 10.6–10.7. Chain-colimit and abelian hypotheses are retained. |
| Bagaria et al. (2015) | Published Corollary 7.6 and proof, and pp. 574–575. The underlying book references cited there were not separately verified. |
| Positselski (2026) | Publisher abstract and metadata, including publication on 30 January 2026; no full-text theorem claimed as checked. |

The current-status search was renewed on 10 November 2026 for the relevant epimorphism, co-wellpoweredness, image, section, and rank questions. Only primary publications or author/institutional copies support mathematical conclusions. Failure to locate an exact formulation is a bounded search outcome, not proof of priority or exhaustive absence from the literature.

The eight marked developments are the successor-stage simplification, retract counterexample, small-envelope proof, epimorphism/co-wellpoweredness implication, two section counterexamples, finite-poset fibrewise presentability test, and power-functor rank counterexample. Each has a precise statement and complete argument. “Ours” credits the supplied argument without asserting novelty.

## Reader construction and validation

The kit builder and companion style remain unchanged. The prepared transcription supplies A4 layout, dedicated margins for both page systems, bilingual hyphenation, a title page, and the documented typography repairs. English commentary uses the kit’s grey rule and smaller type. The full French source remains present.

On a normal LuaLaTeX installation, run these commands in the archive’s top-level directory:

    python build_reader.py DER_XVIII-d
    lualatex -interaction=nonstopmode -halt-on-error DER_XVIII-d_reader.tex
    bibtex DER_XVIII-d_reader
    lualatex -interaction=nonstopmode -halt-on-error DER_XVIII-d_reader.tex
    lualatex -interaction=nonstopmode -halt-on-error DER_XVIII-d_reader.tex

The first LuaLaTeX pass produces the auxiliary file for BibTeX; the two subsequent passes resolve citations. The environment-specific helper documents local restoration of the session’s incomplete TeX installation, which a normal installation need not repeat.

<!-- build-verification:start -->
The complete build passed: the unmodified builder, the first LuaLaTeX pass, BibTeX, and both resolving LuaLaTeX passes all exited successfully. The final reader has **66 PDF pages**. Its overview occupies physical PDF pages **62–64**, a total of 3 pages.

| Final check | Result |
|---|---:|
| Undefined citations or references | 0 |
| Missing glyphs | 0 |
| Overfull boxes | 0 |
| Text spans outside page bounds | 0 |
| Underfull paragraph-box warnings | 2 |
| Automatically moved margin notes | 23 |

The two underfull warnings concern ordinary paragraph spacing and a long bibliography URL. The margin-note warnings record TeX moving source-page labels to avoid collisions. All were examined in the rendered PDF; none produces clipped content or overlapping text. The log is not represented as warning-free.

The reader PDF SHA-256 is:

    c70e9182143ef03994e4fe215dc1d620a90da26887dc11c1a92958b403f8ae22

The built reader TeX SHA-256 is:

    7fa155524cc1e1a8eba3d273fb22efc63819b136d32b3f72e157770288fc2e90

<!-- build-verification:end -->

Automated validation covers exact CSV schemas, row widths, allowed values, unique claim IDs, paired blocks, block kinds, anchor resolution, bibliography keys and metadata, placement of result markers, preservation of source readings, and PDF text bounds. Independent reading checked every false-status row, all 56 numbered units, and all supplied annotation flags. The four table generators and the final refinement were rerun in an isolated directory; every generated row matched the recorded interval tables. Validation records and final build logs are included.

Every final page was inspected in contact sheets, with representative or potentially difficult pages examined at full size. Checks included nested diagrams, long formulas, source-footnote boundaries, commentary continuations, overview, and bibliography. The review found and repaired missing spaces after result markers and after the oval box. Ordinary running-text page breaks were retained where no content or readability defect arose.

## Archive and reproduction

The six prescribed files and the built reader source and PDF are at the root. Prepared source and kit build files are beside them. The source directory preserves the original transcription, authoritative attachment, prompt, earlier index, and cumulative bibliography. Authored audit generators, integration, preparation, rendering, validation, and environment-repair scripts are in the code directory. The four interval sources and reports are preserved for traceability.

External literature PDFs, downloaded package archives, and font caches are excluded. Their source locations and verification scopes appear in the bibliography and environment report. The portable rebuild needs Python, LuaLaTeX with the named packages, and BibTeX. Recreating the working integration uses the directory arrangement explained in the reproduction README.

The correction register remains an apparatus beside the source. Its “should_read” field explains the intended mathematical reading of an edition slip; it is not an instruction to rewrite the French text automatically.
