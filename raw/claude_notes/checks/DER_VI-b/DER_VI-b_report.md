# Les Dérivateurs, VI-b: audit and reader report

## Completion and scope

The package is complete. It contains the six files required by `FORMAT.md`, the assembled reader in TeX and PDF, the corrected working transcription, the original supplied text and PDF, the supplied builder and format, the companion styles, the earlier-package index, and the audit, mathematical-check, integration, compilation, and packaging scripts. The compiled reader has **67 pages**. The overview occupies parts of **three pages**, beginning on reader page 64; the bibliography begins on page 66.

The supplied PDF contains **50 leaves, printed Chapter VI pages 39–88, manuscript pages 64–145**. The prompt's printed range 41–90 is offset by two pages. The opening diagram precedes the manuscript-page-64 marker, and the last leaf stops during the second adjunction square on manuscript page 145. Every part of the supplied transcription is covered by the attached PDF. The report, audit, and correction register distinguish manuscript pages, printed edition pages, and PDF leaves. Correction-register page numbers count the attached leaves from one.

| Component | Completed extent |
| --- | --- |
| Source coverage | All 50 supplied PDF leaves and all 82 manuscript pages |
| Claim audit | 263 entries; every manuscript page is represented |
| Correction and resolution register | 77 entries |
| Original reading flags | All 47 `% [sic]` lines and all 3 explicit `% ??` doubts accounted for |
| Commentary | 43 anchored blocks: 25 exposition, 6 development, 5 examples, 2 context, 2 status, and 3 later-history blocks |
| Marked commentator contributions | 9 fully proved propositions, examples, or corollaries marked `\ours` |
| Bibliography | 13 distinct works, with verified primary-source pinpoints and version qualifications |
| Reader | 67 pages, including the overview and bibliography |

The commentary occupies approximately 24 full-page equivalents, measured from the heights of its printed gray margin bars; the overview is additional. This measurement describes the actual typeset extent rather than estimating pages from a word count. The commentary source has 17,079 whitespace-separated tokens and the overview 1,477; these counts include TeX commands and mathematics and are not linguistic word counts.

## Editorial method and source fidelity

The edition's PDF governs every reading. We compared the full supplied text with it, inspected the doubtful diagrams and indices, and returned to the PDF whenever a formula appeared mathematically incorrect. The French source body is preserved except for **two corrections to arrow styles**: the curved arrows on manuscript pages 141 and 144 are solid in the PDF and were incorrectly transcribed as dashed. The diagram doubt on manuscript page 76 is resolved without changing its reading. The author's “Canulé” is retained; the transcription's speculative “Annulé?” comment has been replaced by a verification note.

The register contains 2 `transcription` records, 3 `doubt_resolved` records, and 72 `edition_slip_kept` records. These categories need not match the three explicit question markers one for one: the two arrow doubts are classified as transcription errors, while the doubt-resolution category also records the “Canulé” reading and a notation issue. Several source annotations concern more than one issue. The file `verification/flag_coverage.csv` maps every original flagged line to its correction-register record or records.

Slips printed in the edition remain in the French text, including the outer-opposite formulas, variance labels, the use of the path replacement where the comma replacement is needed, and the mistaken indices in the final adjunction formulas. The register gives the intended readings, and the English commentary explains their mathematical consequences. An automated comparison of the complete original and corrected document bodies, with comments removed, accepts only the two arrow-style changes. It is an editorial safeguard, not a substitute for the PDF audit.

The earlier-package index was read for continuity. It was not treated as access to the full earlier commentaries. The overlap with VI-a at manuscript pages 64–70 is handled through references to the indexed constructions, with additional explanation where the new argument needs it. We also consulted the complete Chapter VI PDF at manuscript pages 43–45 for the standing axioms and at pages 168–169, printed page 103, for the later proof of proper base change. No missing part of this excerpt had to be supplied from an external transcription.

## How to read the claim audit

The `proof_status` column records the treatment in the source. Present validity, completed proofs, later results, and counterexamples belong in `gap_or_error`, `repair`, `references`, and `notes`, as required by `FORMAT.md`.

| Source status | Entries |
| --- | ---: |
| proved | 120 |
| stated | 67 |
| sketched | 18 |
| assumed | 18 |
| conjectured | 9 |
| open | 17 |
| false | 14 |

Thus **17 does not count questions still open today**. For example, the unrestricted pointwise-detection question remains `open` as a record of footnote 66, while its present negative answer is proved in the commentary. Similarly, `false` includes an editorial annotation, a rejected inference, or a displayed formula whose intended statement is true after correction. It does not mean that fourteen principal theorems of the chapter are false. Most of the structural arguments survive; the commentary supplies their omitted coherence, naturality, and hypothesis checks.

## Principal mathematical findings

### Fine types, local constancy, and the comparison functors

The controlling distinction throughout the excerpt is between three weak-equivalence classes over a base category. Right-fine equivalence tests the comma categories $s\backslash X$; left-fine equivalence tests $X/s$; coarse equivalence tests the total category. The comma construction $\Phi_S X$ is a replacement within the fine relative type. The path construction $C_S X$ performs local-constant reflection and need only preserve the coarse type. Keeping these two replacements separate resolves several otherwise misleading formulas later in the excerpt.

For ordinary nerve weak equivalences, the canonical fine-to-coarse comparison is an equivalence exactly when the base is a **groupoid**. The stronger “equivalent to a discrete category” condition in the annotation to manuscript page 71 is false. A nontrivial one-object groupoid already supplies a counterexample to that condition. The commentary proves the precise criterion using representable presheaves and records it as a modest contribution to this audit, with the surrounding presheaf interpretation grounded in Lurie (2009, Theorem 2.2.1.2) and Cisinski (2009).

The outer opposite appearing in the annotations on manuscript pages 71 and 115 is also incorrect for the ordinary localizations under discussion. Taking opposite categories sends a functor $X\to Y$ to a functor $X^{\mathrm{op}}\to Y^{\mathrm{op}}$ in the same direction. The comparison is therefore $\mathrm{HOT}^{o}_W(S)\simeq\mathrm{HOT}_W(S^{\mathrm{op}})$, without an additional opposite on the target category. The opposite derivator is a different construction and is explained separately. Both reflection adjunctions keep the same order of adjoints.

The right- and left-fine labels attached to the local and colocal tests on manuscript page 82 are reversed. The later formulas on page 94 give the correct assignment: the discrete-fibration tests $S/s$ detect the left-fine class, and the discrete-opfibration tests $s\backslash S$ detect the right-fine class. The added root audit entry `VIb-R001` and the commentary at page 83 reconcile these passages explicitly. The corresponding variance slip at page 136 is likewise recorded without altering the edition.

### Coherence, universal equivalences, and the abstract replacement argument

The two unit insertions in a coaugmented endofunctor require attention, but the relevant coherence follows formally when both are invertible. For a natural transformation $\eta:1\to T$, invertibility of $T\eta$ and $\eta T$ forces their equality. The commentary gives the cancellation argument and connects it with the standard localization criterion, rather than marking a known categorical lemma as a new result (Lurie, 2009, Proposition 5.2.7.4).

The manuscript-page-84 question about universal weak equivalences has an affirmative answer for the actual source replacement under the standing Theorem–Scholie hypotheses (`VIb-A077`). Coarse and fibrewise equivalences agree between Hot-fibrant objects, those objects remain Hot-fibrant after arbitrary strict pullback, and each pulled-back fibre map is an original fibre map. Universal and coarse equivalences therefore agree on the relevant fibrant objects. Naturality then makes the replacement invert coarse equivalences universally, and the preceding coherence lemma supplies the reflection. This argument does not impose an additional nerve homotopy-pullback hypothesis on the source construction. A separately marked proposition gives a useful homotopy-pullback criterion for other replacements; its stated hypothesis remains essential to that separate result.

The lifting argument on manuscript pages 91–94 is valid. Its omitted functoriality and naturality checks are supplied, including the use of pullback and composition stability to keep path objects inside the fibrant class. The dependency annotation in footnote 59 overlooks those earlier uses; the principal theorem does not fail for that reason. The deformation hypothesis A alone suffices for Theorem–Scholie 2, part II; the additional path-composition hypothesis A′ is unnecessary. The commentary proves the conclusion directly and relates it to the established deformation theorem for derived adjunctions (Riehl, 2014, Theorem 2.2.11).

The distinction between Grothendieck's sparse axioms and a full model-category structure is maintained. In a full model category, pullback between slices is right Quillen and preserves weak equivalences between fibrant objects without requiring global right properness. Thomason's model structure on categories is not identified with the Grothendieck-fibration class used here. The correction to the Dwyer-retract argument affects Thomason's properness proof, not the existence of his model structure (Thomason, 1980; Cisinski, 1999; Riehl & Verity, 2022, Appendix C.1).

### Properness and strict base change

The formula in manuscript-page-120 Corollary 2 cannot use $C_S X$ for an arbitrary fine relative type. For $X=\{0\}\to(0\to1)$, the comma fibres are $*$ at 0 and $\varnothing$ at 1, whereas local-constant reflection is constant at $*$. Pullback at 1 distinguishes them. The corrected argument uses $\Phi_S X$; the source formula is preserved and its failure is fully exhibited (`VIb-C009`–`VIb-C011`).

The proper-base-change conjecture on manuscript page 122 is proved later by Grothendieck himself, at manuscript pages 168–169, printed page 103. The later proof has been checked in the complete chapter, and the reader supplies the elementary argument at the point where this excerpt needs it. The modern proper/smooth framework is compared with Maltsiniotis (2005, Definition 1.1 and Theorem 1.2), with the dual convention stated explicitly.

For $W_\infty$, strict pullback along a fixed functor $f$ preserves all right-fine weak equivalences if and only if $f$ is proper. The proof tests the maps from a point into its comma replacement and reads contractibility of the resulting lifting categories. For an arbitrary fundamental localizer, the corresponding characterization requires that this preservation hold after **every change of base of $f$**. A worked example using the nonemptiness localizer and $e\to BG$ shows why fixed-base preservation alone cannot replace that requirement. These statements answer the question on manuscript page 123 (`VIb-C019`); their proofs and the localizer qualification appear together in the development block anchored at manuscript page 126.

The three-object span $E=(v\leftarrow u\to w)\to(0\to1)$, with $u,v$ over 0 and $w$ over 1, provides a small explicit separation. It is a Hot-fibration and preserves coarse equivalences after base change in the indicated sense, but it is not proper and its strict pullback fails to preserve a right-fine equivalence. The empty comma category at $v$ makes the failure visible. The proof checks the Cartesian lift, the fibre transition, the universal coarse equivalence, and the failed fine test, rather than relying on a diagrammatic assertion (`VIb-C031`). An independent review of the properness argument and this example is included in `parts/b_peer_review_c.md`.

The saturation gap at manuscript pages 124–126 is closed by the later theorem that every fundamental localizer is strongly saturated (Cisinski, 2006, Proposition 4.2.4 in the consulted author version). The commentary also explains why the relevant restricted presentation inherits the needed coarse saturation through its functor to the total-category localization, even when the presentation is not a full subcategory.

### Locally constant diagrams and the derivator axioms

The varying-base prederivator consisting only of locally constant space diagrams has left and right adjoints to restriction, but fails the pointwise Kan-extension axiom Der 4. The distinction matters: existence of both adjoints does not imply the derivator axioms. For the inclusion $a:\{0\}\to(0\to1)$, the locally constant left adjoint is constant at the point. Its value at 1 is therefore $*$, while the corresponding pointwise comma formula is indexed by the empty category and gives $\varnothing$. The reader proves this obstruction and separates it from Cisinski's derivator of locally constant coefficients on a **fixed** category with an additional varying diagram parameter (Cisinski, 2009, Corollary 3.11 and Theorem 3.13; `VIb-C035`–`VIb-C036`).

The same interval inclusion shows that commuting with local-constant reflection is possible beyond Hot-fibrations (`VIb-C032`). The argument checks both the commutation and the failed universal fibre condition. Transport by base 2-cells is then developed with its variance, cleavage dependence, and naturality under arbitrary functors, using the vertical transformations and their fibrewise cylinder homotopies.

The unrestricted question in footnote 66 has a negative answer **even for strongly saturated weak equivalences** (`VIb-C042`). The new development block constructs a small category as a disjoint union of finite categories, equipped with projection to the walking retraction. The inverse image of the isomorphisms under this projection is strongly saturated. For a countable discrete diagram shape there is a uniform three-arrow morphism whose coordinate images are all isomorphisms, but any coordinate inverse requires an unbounded number of localization letters. Every global localization morphism has finite word length, so there is no global inverse. The proof supplies the categories, their relations, the pointwise inverse calculation, the lower bound, and the strong-saturation argument in full.

The finite check in `code/check_der2_counterexample.py` confirms the required lower bounds for odd sizes 1 through 19. It is supporting verification, not the proof for all sizes. The construction and proof were independently checked during integration. A positive criterion using a suitable short calculus of fractions at every diagram level is stated with its literature source (Lagkas Nikolos, 2018, Proposition 4.2.8 and Remark 4.2.19). The standard model-category derivator remains covered by Groth (2013, Proposition 1.30).

The adjacent infinite-product assertion fails for a simpler reason: a family of finite connected fences can have unbounded distances between chosen endpoints. Each separate groupoid completion is terminal, while the product has no finite zigzag joining the two chosen tuples. The commentary proves the exact bounded-distance criterion, including the identity-padding construction in the positive direction (`VIb-C045`). This does not disprove Der 1 for homotopy types; the model-category presentation supplies the uniform representatives and homotopies absent in an arbitrary localization.

### Integration and the final adjunction

Composition of structure maps realizes integration, and the pointwise homotopy-colimit interpretation explains its relation to the total homotopy type. For ordinary weak equivalences, the Hot-fibration hypothesis in footnote 67 does ensure that direct image preserves locally constant types: the comma transition functors are weak equivalences, and homotopy colimits with locally constant coefficients are invariant under them. The reader gives this argument at manuscript page 137 and cites Cisinski (2009, Proposition 1.24), with the opposite indexing convention specified (`VIb-C061`).

The final adjunction is completed through both triangle identities. In particular, the failed first attempt at the counit is distinguished from the corrected map $i_X^{-1}\operatorname{pr}_1$. Pulling back the replacement unit need not be a fine equivalence, and an interval example shows the failure. The last square, at manuscript page 145, follows from the naturality of the comma-replacement unit; comparison of the two projections and cancellation of the unit complete the triangle that the supplied excerpt leaves unfinished (`VIb-C074`–`VIb-C077`).

## Research status and qualifications

The nine `\ours` markings identify proofs or developments supplied in this commentary: the canonical-comparison criterion; the conditional universal-comparison proposition; the properness characterization; the nonemptiness-localizer example; the three-object Hot-fibration example; the interval obstruction to Der 4; its commutation corollary; the infinite-product fence example; and the strongly saturated Der 2 counterexample. Each is stated with its hypotheses and proved completely. Literature checks are recorded in the surrounding blocks. The marking claims neither historical priority nor an exhaustive search of unpublished work. Known categorical localization and deformation results are cited as known rather than included in this count.

Several limits remain explicit. The Der 2 counterexample uses a **countably infinite discrete** diagram shape; it does not decide a version restricted to finite non-discrete shapes. The fixed-base properness characterization is asserted for $W_\infty$; the general-localizer version requires stability after all changes of base. The extra homotopy-pullback criterion for arbitrary replacements is conditional, whereas the particular universal-equivalence question for the source's replacement has been answered under the source's standing hypotheses. The locally constant direct-image statement is explained in the ordinary space case; it is not silently promoted to every unspecified relative-category presentation.

The broader programme involving two oriented fine structures and “bi-site” cohomology is not a single precisely formulated theorem in these pages. An arbitrary pair $(M,W)$ does not intrinsically supply both oriented structures and all the required Kan-extension data. We describe what additional structure the later theories use, without claiming to settle an undefined general programme. No assertion that these remaining variants are open throughout the current literature is made merely from failure to locate a reference.

## Primary-source verification and references

All thirteen bibliography entries include a URL or DOI and a `verified:` note identifying what was actually read. Existing cumulative keys are reused where applicable. Duplicate entries and repeated BibTeX fields have been removed. The most consequential pinpoints are recorded below; full bibliographic data and all checked items are in `DER_VI-b_references.bib`.

| Primary work | Material verified and used |
| --- | --- |
| Grothendieck (1983), *Pursuing Stacks*, §69 | Edited extract, printed pages 1–3, on the SGA 5 motivation, diagram categories, and integration; editorial notes distinguished from the original text |
| Grothendieck (1990), *Les dérivateurs*, Chapter VI | Entire supplied excerpt; full chapter at manuscript pages 43–45 and 168–169 |
| Gabriel and Zisman (1967), *Calculus of fractions and homotopy theory* | Chapter I, §§1.1–1.2, finite-path construction, relations, and universal property, inspected in the scanned book |
| Thomason (1980), “Cat as a closed model category” | Definitions 2.1–2.3, Theorem 4.9, Proposition 5.4, and Corollary 5.5 |
| Cisinski (1999), “La classe des morphismes de Dwyer n'est pas stable par rétractes” | Counterexample, Lemma 4, Proposition 2, and repair of the properness argument |
| Maltsiniotis (2005), “Structures d'asphéricité, foncteurs lisses, et fibrations” | Definition 1.1; Theorem 1.2 and dual properness criterion; Theorem 3.8 and proof; later statements inspected without removing their hypotheses |
| Cisinski (2006), *Les préfaisceaux comme modèles des types d'homotopie* | Proposition 4.2.4 and proof, with Corollary 1.4.7 and Proposition 4.2.3, in the 370-page author PDF, printed page 162, PDF leaf 186 |
| Cisinski (2009), “Locally constant functors” | Published 22-page version: definitions and early homotopy-invariance results, Proposition 1.24, Proposition 3.10, Corollary 3.11, and Theorem 3.13, with relevant proofs |
| Lurie (2009), *Higher topos theory* | Theorem 2.2.1.2 and Proposition 5.2.7.4, including the localization proof |
| Groth (2013), “Derivators, pointed derivators and stable derivators” | Published Propositions 1.24, 1.26, and 1.30, including the model-category construction |
| Riehl (2014), *Categorical homotopy theory* | Definition 2.2.1, Remark 2.2.2, Theorems 2.2.8–2.2.11, and right-deformation discussion |
| Lagkas Nikolos (2018), *Levelwise modules and localization in derivators* | Thesis metadata; Corollary 4.2.5, Proposition 4.2.8 and its Der 2 argument, and Remark 4.2.19 |
| Riehl and Verity (2022), *Elements of ∞-category theory* | Lemma 1.2.19 and Appendix C.1, especially Lemmas C.1.10–C.1.11, in the author's PDF; published metadata checked |

The Cisinski (2006) pinpoint refers to the consulted 370-page author version, not to an assumed pagination or numbering in the 416-page publication. The Cisinski (2009) pinpoints refer to the published article rather than the shorter 2008 preprint. The Riehl and Riehl–Verity notes likewise specify the author PDFs used. These distinctions are retained in the bibliography so that a reader can reproduce each check. The sources are cited for the statements they establish; the commentary's finite constructions are not attributed to those authors.

## Compilation, visual checks, and reproducibility

The supplied `build_reader.py` is unchanged. It validates the required files and anchors and assembles the reader. The final pipeline runs transcription verification, integration, the supplied builder, LuaLaTeX, BibTeX, two further LuaLaTeX passes, and editorial/PDF validation. Every stage exits successfully. The final logs contain **no LaTeX errors, undefined citations or references, missing glyphs, overfull boxes, or BibTeX warnings**. Every text block lies within the page bounds. Selected pages containing dense mathematics, the new Der 2 proof, the final adjunction, the overview, and the bibliography are visually inspected in the rendered PDF.

There are sixteen nonfatal margin-note repositioning warnings and one underfull horizontal box in a preserved French editorial annotation near the beginning of the reader. They do not produce clipping or missing text. The logs are included rather than suppressed. The source's long diagrams fit the page, and citations resolve to the verified bibliography.

The installed engine is LuaHBTeX 1.17.0, TeX Live 2023. This environment initially lacked a generated LuaLaTeX format, a filename database, `luaotfload`, and `babel-french`. The included bootstrap creates a workspace-local format from the installed LaTeX kernel, replacing only the unavailable OpenType-loader startup with a legacy-font selection. It modifies no system files. The fallback style uses Latin Modern Type 1 fonts, explicit Unicode accent mappings, and Babel's imported locale information. French hyphenation is disabled in that fallback; English hyphenation is enabled. This is an actual LuaLaTeX build. A complete TeX installation takes the normal `fontspec` and French/English Babel route instead.

Production changes to the preamble and companion style provide the font fallback, page geometry, diagram sizing, English language scope inside commentary, short manuscript-anchor headers, readable bibliography paragraphs, and PDF attribution metadata. They do not emend the French mathematical content. The standard rebuilding commands and the tested minimal-runtime command are documented in `README.md`.

`verification/validation.json` records the final counts, source preservation, flag coverage, page coverage, reference checks, page geometry, and log findings. `verification/flag_coverage.csv` provides the complete flag-to-register correspondence. The relevant LuaLaTeX, BibTeX, builder, and validation logs accompany them. The package also contains a manifest and SHA-256 checksums; the packaging script checks ZIP integrity and verifies every manifested member against its hash. External research PDFs and disposable build caches are not included. The original user-supplied PDF and text are included for an independent editorial check.

The validation scripts check assembly, readings, finite combinatorial instances, and reproducibility. They do not certify mathematical truth automatically. The proofs were checked by reading their hypotheses and arguments, with independent reviews of the properness constructions and of the strongly saturated Der 2 counterexample.

## Attribution

This package is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). The project supplied the series editing credit “edited with Claude (Anthropic)”; no separate Claude editing operation has been performed or independently verified in this session. No personal authorship is claimed. The `\ours` convention identifies contributions to the commentary and makes no claim of historical priority.
