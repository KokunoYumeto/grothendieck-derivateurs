# Chapter XIII-a: audit, commentary, and verification report

**Commentary, mathematical audit, and developments: GPT-6 Astra (OpenAI, ChatGPT Pro mode).** This credit identifies the work delivered here. It does not certify any subsequent assembly or editing by Claude or by another person or system.

## Scope and authority

The audit covers the whole supplied excerpt: **manuscript pages 1–60**, corresponding to **printed edition pages 1–33** and **leaves 3–35 of the attached PDF**. Leaves 1–2 are preliminary matter. The attached electronic edition, dated 25 January 2004, is the authority for readings. The supplied TeX is a transcription to be checked against that edition; neither the surviving manuscript nor a different edition was substituted for it.

All sixty manuscript pages were read. The mathematical statements, displays, arrow directions, indices, and relevant cross-references were compared with the supplied PDF. All thirty-three mathematical leaves were rendered and visually inspected, with overlapping checks at segment boundaries. The two doubtful readings and all nineteen pre-existing `[sic]` flags were checked visually. A complete page correspondence is supplied in `verification/page_map.json`.

The work was divided into three contiguous audits, with integration and independent checks of the most consequential arguments. The early segment covers pp. 1–20; the middle segment covers pp. 21–40; the late segment covers pp. 41–60. This division is recorded only to make the provenance of the checks reviewable; the delivered commentary is assembled in manuscript order.

The supplied earlier-commentary index contains entries only through **DER_VII-a**. It was searched and used for the relevant continuity references, including the previous treatment of comparing replacements and the distinction between common and object-dependent bounds. The absence of an index for Chapters VIII–XII prevents a claim that duplication against those unavailable installments has been excluded. No missing installment was invented or represented as read.

The attached excerpt ends during the opening theorem of Section 6. Its continuation at manuscript p. 61 and the forward reference to p. 63 were not verified. The complete chapter's online metadata was checked, but conclusions about the continuation are not included in this audit. Likewise, Chapter XII's seven localizer axioms, cited but not reproduced in the excerpt, are not silently identified with a different modern list of axioms.

## Deliverables and interpretation of the registers

The six required files are present at the archive root:

| File | Content |
|---|---|
| `DER_XIII-a_blocks.tex` | 43 anchored commentary blocks, in full mathematical prose |
| `DER_XIII-a_overview.tex` | The standalone overview, within the required two-to-five-page range |
| `DER_XIII-a_claims.csv` | 301 individual source-audit entries |
| `DER_XIII-a_corrections.csv` | 35 records: 33 retained edition slips or qualifications and 2 resolved doubts |
| `DER_XIII-a_references.bib` | 23 distinct references, with verification and version notes |
| `DER_XIII-a_report.md` | This report |

The archive also contains the built `DER_XIII-a_reader.tex` and PDF, the working transcription and reader style, the original supplied builder and format instructions, the original input TeX and authority PDF, the section sources, and the executed reproducibility code. Downloaded third-party literature PDFs are verification sources and are not redistributed in this archive.

The `proof_status` field describes the source's treatment. A source assertion can therefore remain `stated`, `sketched`, or `conjectured` even when the commentary now proves it. `false` is used for a false assertion or an invalid inference as written, and does not automatically classify the intended conclusion as false. The repair, reference, and notes fields identify the present result. Definitions and axioms are separately registered, including the repeated axioms in the revised formulation. The audit does not use “open” as a synonym for “we did not locate a proof.”

The correction ledger concerns readings and identifiable slips. A mathematical gap whose printed expression is unambiguous belongs in the claims register, rather than being disguised as a transcription correction. No substantive new transcription discrepancy was found. In particular, the two `% ??` entries both reproduce what is visibly printed:

1. On PDF leaf 16, the tilde ends before the final superscript star. The literal expression is retained. A separate edition-slip row explains the mathematically intended closure of the union with the left orthogonal.
2. On PDF leaf 18, the strict inclusion is printed as a superset symbol with a separate not-equal sign below it. The transcription is faithful.

Every retained edition slip remains in the working text. Existing bracketed editorial corrections remain alongside the original readings. The p. 16 grammar flag in the supplied TeX suggested `lui`; the plural antecedent supports `leur`, and the ledger explains that distinction while preserving the edition's `leurs`. Such editorial judgments are not applied as silent changes to the source.

## Mathematical findings

### Lifting classes, small objects, and intrinsic properness: pp. 1–14

The opening Galois calculus and closure results are correct. The commentary supplies proofs of the pushout, transfinite-composition, and retract properties and explains the distinction between a class generated by cellular attachment and its retract closure. The small-object construction is proved with an explicit regular-cardinal bound on the domains. It uses all attaching squares to obtain functorial factorizations. The parenthetical weakening of cocompleteness is interpreted with the exact colimit and smallness requirements stated.

The source's “couple de Quillen” is a weak factorization system when the orthogonal equalities and factorization both hold. It is not a Quillen adjunction. Its “catégorie de modèles” initially means a relative category with two-out-of-three, and is not yet a modern model category. The commentary makes these terminological distinctions where they affect an argument.

Proposition 4 and Corollary 1 supply the required base-change argument for universal weak equivalences. Their proof is expanded before they are used to justify the saturation construction. A fully worked three-object example shows why the factorization hypothesis cannot be dropped: in the chain `0<1<2`, with weak arrows the identities and `0→2`, that nonidentity weak arrow is an intrinsic W-fibration but is not universally weak. The failure of the necessary factorization is explicitly identified. An exhaustive finite checker verifies all squares, intrinsic-fibration tests, and possible factorizations in this example.

The context block relates the purpose of the auxiliary classes to the letter to Thomason of 2 April 1991. Its use of Brown's one-sided theory is tied to the checked source passages, without assigning a later theorem to Grothendieck's historical formulation.

### Recognition, accessibility, and maximal classes: pp. 14–26

The serious problem in the conjectural recognition argument is the passage from constructional stability to a lifting characterization or to a small generating set. The inference on p. 17 is invalid as given. This does not prove that the particular intrinsic classes can never be left lifting classes. The intended implication `(a)⇒(a′)` is repaired directly by applying the small-object argument to the two sets actually supplied in `(a)`.

Three notions are kept separate throughout: closure under filtered colimits, accessibility of a full subcategory of the arrow category, and generation of a lifting class by a set. The complete order-embedding example in `Pos` demonstrates that an accessible, accessibly embedded, left lifting class with factorizations need not be cofibrantly generated. The proof includes the explicit factorization and the cardinal argument excluding any proposed generating set. The example is credited to the relevant literature and is not marked as an original result.

The intersection conjecture on p. 20, interpreted in the source's explicit set-generation sense, has a later affirmative answer: Makkai and Rosický's theorem on combinatorial cellular categories gives the required intersection, and their diagram result gives set generation of pointwise cellular classes. The cited numbering is that of the author preprint dated 21 November 2013. These statements are not left labelled as unresolved.

Smith's recognition theorem supplies a precise additional-hypothesis repair of the larger programme. Under condition `(a)`, if the weak-equivalence subcategory is accessible and accessibly embedded, the two initial small-object factorizations give the universal-equivalence criterion needed to check the closure of trivial cofibrations. Smith recognition then produces a proper combinatorial model structure. The proof records where the new solution-set hypothesis enters. Filtered-colimit closure alone is not presented as if it supplied that hypothesis.

The necessary right-closure condition in pp. 21–26 is proved independently of accessibility. The inclusion squares of footnote 17 are valid for an existing closed weak structure: its actual four classes provide the intermediate inclusions. The unsupported claim that all the surrounding intrinsic vertices are lifting closed is kept distinct from those valid inclusions.

For `Cat`, the commentary gives a complete proof of the discrete-category obstruction to condition IV. Testing against long contractible zigzag posets shows that a functor with LLP against every universally weakly equivalent functor is injective on connected components. A nonempty discrete terminal projection therefore belongs to the relevant right closure; with at least two objects it is not a weak equivalence. The missing nonemptiness qualification in the printed parenthesis is recorded. This example does not settle the separate maximal-condition-III converse.

### Exactness and homotopy: pp. 27–34

Footnote 20 is false for the four designated classes. Assuming choice, take sets with every map weak, both `C` and `TC` the injections, `F` the surjections, and `TF` the surjections whose fibres are singleton or infinite. The commentary checks both factorizations, both lifting properties, every required stability property, and intrinsic properness. The classes `C,F,W` are retract closed and left exactness holds, but the two-element terminal projection is absent from `TF`. The repaired assertion replaces `TF` by its retract closure, which is `F∩W`.

Exactness nevertheless permits a stronger positive result. If `W=TF∘TC`, factoring a map of `C∩W` and applying the original lifting axiom makes it a retract of a map of `TC`. It consequently lifts against every fibration. The dual argument applies to `F∩W`. Thus

\[
(C,TC,F,TF)\longmapsto(C,C\cap W,F,F\cap W)
\]

produces a biexact, possibly nonclosed, proper Quillen structure with the same `C,F,W`. No retract-closure assumption is needed for this completion. Stability of the enlarged trivial classes uses the universal-equivalence criterion and intrinsic properness. The source's original designated classes need not already equal their completions; this is why the positive theorem is consistent with the counterexample.

This lemma resolves the doubts on pp. 32–34 positively. The commentary proves homotopy-cartesian square exactness by lifting a cylinder endpoint against a fibration; the dual proof gives homotopy-cocartesian exactness. The extra exact structure on the cospan diagram category in the source's proposed route is unnecessary for this conclusion. Suspension and loop sequences are interpreted in the pointed setting; no triangulated structure is asserted without stability.

The comparison with fibrant-cofibrant objects is proved under the weak axioms before exactness is assumed. Under exactness, an explicit quotient by the congruence generated by both homotopies gives the localization. The completion then provides the usual individual homotopy relations for a cofibrant source and a fibrant target. The fully faithful adjoint and calculus-of-fractions statements are justified by the universal property of fibrant replacement in the homotopy quotient, including the two Ore conditions.

Footnote 22 is resolved by separating path-object conventions. For designated `TC–F` diagonal factorizations, lifting proves that every such path object gives the same reflexive, symmetric raw relation. A dual application of Kurz–Rosický's reflexive-graph example shows that this relation need not be transitive under the weak axioms, even when every object is cofibrant and fibrant. The full construction and its two weak factorization systems are proved in the commentary. An exact variant shows why arbitrary noncofibrant sources must still be distinguished in the ordinary model setting. By contrast, the existential relation allowing some `W–F` path object is an equivalence relation for every fibrant target: the pullback concatenation proof is supplied in full. The excerpt does not explicitly choose between these conventions. The audit consequently records conditional positive and negative answers, rather than attributing an unqualified false assertion to an unspecified convention.

Five results are marked `\ours`: the three-object counterexample, the zigzag proof of the discrete obstruction, the fibre-cardinality counterexample, the joint-congruence quotient description, and exact completion of the trivial classes. Each has a complete argument and a statement of the relevant literature checked. These labels identify developments supplied in the commentary; they make no priority claim. Other elementary applications of known results are attributed rather than labelled new.

### Diagram categories and the variance of Kan extensions: pp. 35–50

The evaluation formula is proved with the presheaf convention explicit:

\[
(\alpha_{s!}A)(t)=\coprod_{\operatorname{Hom}_I(t,s)}A.
\]

It transports a lifting square precisely when the requisite copowers preserve the left class. Finite-Hom hypotheses are used where the source has only finite colimits. The complete walking-arrow calculation shows that an injective right class is controlled by the target component and the relative matching map. A two-object diagram of sets gives the promised failure of pointwise surjectivity to imply injective trivial fibrancy.

The modern injective construction establishes Theorem 2 under the actual small-generation condition `(a′)`. The commentary uses Makkai–Rosický's pointwise cellular result and gives the remaining compatibility/retract argument. The weaker recognition conditions are not certified merely by citing the modern injective-model theorem.

Both Kan-extension formulas retain the opposite comma categories required by presheaves. The transfer of lifting through an adjunction is proved by a bijection of fillers. The monomorphic-edge criterion and the sieve restriction-of-limits criterion receive complete proofs.

Grothendieck's withdrawal on pp. 49–50 is mathematically necessary. The commentary exhibits an ordinary pullback changing from empty to a point under an objectwise weak equivalence, and an ordinary pushout changing from a circle to a point. It also supplies a derived-product example in pointed spaces: a homotopy coproduct is sent to a torus, whereas the corresponding coproduct of the products is a wedge of circles. The fundamental groups distinguish them. These examples separate preservation of weak equivalences from the two homotopical exactness properties.

### Complexes, derivators, and admissibility: pp. 51–60

For infinitely many indexing objects, individually bounded-below complexes need not share a lower bound. The family `(Z[n])_{n≥0}` proves the failure of the relevant arbitrary product in `D⁺(Ab)`. The argument does not pretend to prove that no weak quillenization of the underlying relative category can exist. K-injective resolutions and combinatorial structures supply unbounded derived operations for Grothendieck abelian categories. A periodic cyclic-group resolution demonstrates why preserving a bounded subcategory is a separate issue. Spaltenstein's original scope is distinguished from the general Grothendieck-category theorem.

The elementary derivator arguments separate finite products, detection of isomorphisms, and the historical local-constancy axiom. The latter is related to Cisinski's precise theorem for locally constant diagrams and nerve weak equivalences. It is not confused with the axiom now usually called Der3. The later comparison with Quillen presentations and infinity-categories retains the actual hypotheses and kinds of morphisms used by Renaudin and by Riehl–Verity.

Under the literal uniform closed exact hypotheses at p. 57, the completion retract argument shows that both trivial-class equalities already hold. The extra one-sided clause is therefore redundant when the domain contains the terminal shape. A full graph-factorization proof of the dual Ken Brown lemma shows that **every existing ordinary right Kan extension is admissible**. The argument requires the right Kan extension to exist; it does not infer arbitrary limits from finite completeness. Auxiliary pointwise arguments involving left Kan extensions are qualified by their required coproducts.

Finally, a noetherian sober Alexandrov `T₀` space is finite. The proof identifies irreducible closed sets with directed lower ideals, obtains the ascending-chain condition and scatteredness, and uses a maximal finite open subset. It follows that the ostensibly broader poset class on p. 60 gives no additional shapes under the usual Alexandrov convention. The proof uses the ordinary classical choice principles of the surrounding arguments. It is presented as an application of known order-topological facts, not a new theorem.

## Matters not settled or not certified

The following limitations concern precise mathematical or source questions, rather than unfinished coverage of the attached pages.

| Question or scope | What this audit establishes |
|---|---|
| The p. 20 small-subfamily assertion under exactly the manuscript's assumptions | The checked recognition and cellular results do not prove it in that generality; a precise added accessibility/solution-set hypothesis gives the stated repair. No claim of a recognised current open problem is made. |
| The full maximal-class recognition equivalences and the condition-III converse | Valid implications and necessary closure conditions are proved separately; the discrete `Cat` example disproves IV but does not settle every converse involving III. |
| Footnote 22: path-object convention | Resolved conditionally: designated `TC–F` paths can give a nontransitive relation; the existential `W–F` relation is transitive for a fibrant target. The convention not explicitly fixed in the excerpt is not silently imposed on the author. |
| Chapter XII's seven localizer axioms | They are cited by the source but absent from the supplied excerpt; equivalence with a modern axiom list is not asserted. |
| Earlier-commentary overlap beyond Chapter VII | The supplied index stops there; no claim of having checked unavailable installments is made. |
| The theorem's continuation after manuscript p. 60 | Outside the supplied excerpt and not represented as read. |

## Bibliographic verification

Every bibliography entry has a DOI or URL and a `verified:` note describing the exact extent of inspection. Keys already present in the cumulative bibliography are reused. Duplicate cumulative entries are not copied into the new bibliography. Publication dates and numbering of inspected preprints are distinguished explicitly.

The principal checked passages include Riehl's small-object treatment; Beke's Theorem 1.7 and its solution-set discussion; Makkai–Rosický's Theorem 3.2, Corollary 3.4, and Remark 3.8; Rosický's corrected 2021 discussion of accessible and combinatorial structures; Brown's fibrant-object axioms and factorization lemma; Thomason's existence and properness results; Cisinski's model and derivable-category results; Barwick's 2007 v2 diagram theorems; Groth's published derivator results; the unbounded-complex sources; Renaudin's published Theorems 3.3.2 and 3.4.4; Riehl–Verity's Proposition 5.3.9 and Remark 5.3.10; and Kurz–Rosický's Definition 3.1, Observation 3.3, and Example 3.6 in the author preprint dated 21 October 2004. In the last example, the commentary defines the right class by its literal lifting property, including each specified target edge in a multigraph, and verifies the needed graph construction directly.

The version qualification is material in several cases. The Barwick numbering is from the 2007 v2, not the expanded 2010 article. The Makkai–Rosický numbering is from the 21 November 2013 preprint. Cisinski–Déglise is checked in its December 2007 v1, with 2009 publication metadata. Cisinski's *Higher Categories and Homotopical Algebra* is checked in the author's corrected electronic version dated 30 July 2026. Quillen's bounded-complex example was inspected in the revised TEXromancers edition; original 1967 page numbering is not certified. Picado–Pultr's relevant proposition was checked through an indexed excerpt of the primary first-edition text, rather than unrestricted access to the whole book. The commentary supplies the complete finiteness argument independently.

Verification of a quoted theorem does not imply a claim to have independently reproved every result in the cited publication. Detailed passage-level records are also preserved in the three section reports. No specific Baues result is attributed without an inspected source.

## Build, layout, and reproducibility

The supplied `build_reader.py` is retained unchanged and was executed on the six final-format files. The LuaLaTeX/BibTeX build uses an initial LuaLaTeX pass, BibTeX, and two further LuaLaTeX passes. The archive includes the generated bibliography and final verification logs. A supplemental validator checks the citation inventory, exact anchors, CSV consistency, source-page coverage, retained flags, and the restricted kinds of transcription changes. A separate rendering script checks every PDF page and records the overview range and geometric text bounds.

The working style makes presentation-only adjustments: A4 margins with room for the original page labels, microtypography, English language selection inside commentary, normal upright commentary type, abbreviated page labels in block headings, and flexible spacing in the edition's typewriter prose. Full anchors remain unchanged in the machine-readable source. The long Section 2 heading receives an explicit line break; any additional display-only edits are enumerated in `code/layout_edits.json`. The two doubt comments are marked resolved, with the literal readings retained. No `edition_slip_kept` correction is automatically applied.

The environment initially supplied LuaHBTeX and package files but lacked the format and Lua font-loading components. The code therefore prepares a workspace-local TeX runtime from public TeX Live archives, with a recorded download manifest. No system directory was changed. A small compatibility definition is required because the downloaded French Babel package expects a metadata command absent from the installed 2024 LaTeX kernel; this reader does not use that metadata facility. On a complete modern TeX installation, the ordinary build needs no such runtime preparation.

Rebuild on a complete TeX installation with:

```sh
python3 code/build.py --system-tex
python3 code/validate.py
python3 code/render_verify.py
```

To reproduce the runtime used for this delivery, first run `python3 code/prepare_tex_runtime.py`, then omit `--system-tex`. The local-runtime preparation expects the base TeX Live package tree provided by this environment; it is not a universal TeX installer. The mathematical examples and CSV-generation scripts are included under `code/` and `sections/`.

The exact final page count, successful process exits, remaining informational package/placement messages, rendering review, and file hashes are recorded in `verification/`. There is no claim of formal proof-assistant verification. The finite example checker is supplementary evidence for that example; the other proofs are mathematical arguments checked in the commentary.

## Final delivery verification

The delivered reader has **60 pages**. The standalone overview
occupies reader pp. 56–58, sharing its
last page with the beginning of the bibliography. All five build subprocesses
returned exit code zero: the supplied Python builder, the initial LuaLaTeX pass,
BibTeX, and the two subsequent LuaLaTeX passes.

The final log contains no undefined citations, missing characters, overfull
boxes, or underfull boxes. The remaining messages are the French Babel legacy
list notice and automatic movement of source-page margin labels. Every page
was rendered and visually reviewed; the labels remain separated, the final
commentary ends without an orphan continuation page, and the overview and
bibliography are legible. Geometric extraction found no text beyond page
boundaries and no Unicode replacement characters. The review record is
`verification/visual_review.json`.

The supplemental validator passes with zero errors. It accounts for all
21 original doubt/sic flags and confirms that
the edition readings are preserved after reversing the documented
presentation-only edits. The counts are 43 commentary blocks,
301 claim-register rows, 35 correction
records, and 23 distinct bibliography entries.

The archive contains a SHA-256 manifest of all other members. The packaging
script checks every archived member against that manifest and verifies ZIP
CRC integrity. The PDF's SHA-256 is
`b9ef939181b59fcf05855ceb6a0fd5f8baa4525cca8b09e1c7afa61edf61e5e6`.
