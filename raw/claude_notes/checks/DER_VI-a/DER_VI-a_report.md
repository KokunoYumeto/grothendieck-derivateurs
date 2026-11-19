# Les Dérivateurs, Chapter VI-a: audit report

Completed 9 November 2026. Scope: Chapter VI, printed pages 1–43, manuscript pages 1–70, in the electronic edition of 9 November 2001.

## Deliverables and reading conventions

The package contains the six files specified in `FORMAT.md`, the complete interleaved reader in TeX and PDF, the corrected transcription, the unchanged supplied builder, the adapted companion style, the original inputs, and the code and verification records used to produce them. There are **37 commentary blocks**, **280 claim records**, **59 source decisions**, and **14 bibliography entries**. The overview occupies **three pages**. The commentary has approximately 13,200 whitespace-delimited words, including TeX notation.

The French source and English commentary remain visually distinct. A vertical rule identifies each commentary block. The contents gives the manuscript anchor on the left and the reader page on the right. Margin labels preserve the printed and manuscript page references. The original title and editorial notice follow the reader's cover and contents.

The claim register records the status of the assertion actually made in the source. A false inference remains `false` even when the intended conclusion is subsequently proved by another argument. A conjecture in the manuscript need not be a present open problem: the resolution belongs in `repair`, `references`, and `notes`. Repeated assertions are consolidated only when their locations and hypotheses remain explicit. The counts by kind are 46 definitions, 25 axioms, 62 propositions, 106 claims, 13 questions, 13 remarks, and 15 conjectures. The status counts are 94 proved, 24 sketched, 110 stated, 15 assumed, 16 conjectured, and 21 false. These are counts of source assertions, not of distinct errors or currently open mathematical problems.

## Source authority and the missing final pages

The attached `DER_VI-a_pages.pdf` has **43 physical pages**, including two unnumbered preliminaries. It therefore contains only printed pages **1–41**, ending mid-manuscript page 68. The TeX continues through printed page 43 and the opening of manuscript page 70. This discrepancy was resolved against the editors' complete Chapter VI PDF:

<https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChVI-345.pdf>

All 43 physical pages of the attachment have exactly the same extracted text as the first 43 pages of that complete PDF. This is a page-by-page text identity check, not a claim of byte identity between the PDF containers. Physical pages 44–45 supply printed pages 42–43. Those pages are included separately as `qa/supplement_printed42-43.pdf`. The source URL and hashes are recorded in `qa/source_provenance.json`; `fetch_source.py` retrieves the complete edition for reproducing the comparison.

The attached PDF has SHA-256 `0d96bb6ec3e6e57edfa52c22883f530ed4dd44eb8ca82c53ff49953716a5c9c6`. The complete edition has SHA-256 `a34d2a82e911dafd70b3962664fbfe36dc3d54c2273da0df443a22871b493569`.

Every source page within scope was read and inspected visually, with enlargements for doubtful arrows, diagram origins, font distinctions, footnote numbering, and the readings underlying substantive error findings. The supplementary pages received the same treatment. The audit stops at the supplied transcription's endpoint: the theorem–scholium begins on manuscript page 70, but its continuation on pages 71–81 is outside this package.

### Source decisions

The ledger contains **10 transcription repairs**, **44 edition slips preserved**, and **5 resolved doubts**. Its `pdf_page` counts physical pages, including the preliminaries; entries 44–45 expressly identify the supplemental source. The preamble-level font repair uses `all`.

There are 34 literal `% [sic]` markers on 33 source lines. One line has two markers, and another marker identifies two slips. All **35 flagged readings** were checked against the facsimile and represented in the ledger. Nine further edition-level mathematical readings are recorded. They remain in the source, including the outer opposites, the coarse/fine equality on manuscript page 47, and the covariant square printed in a contravariant discussion. For `edition_slip_kept`, the `should_read` field is explanatory; it does not indicate a silent alteration of the source.

All three `% ??` uncertainties were resolved: the dotted constructions on page 8 originate in the homotopy-fibration region; the comparison on page 13 is a plain line without an arrowhead; and the category name after bold *dans* on page 30 has ordinary mathematical weight. Two further suspected errors required no correction. On page 19, the unit can indeed be regarded in `Cat/X`, as a section of the forgetful projection. On page 43, a one-headed implication states a valid weaker consequence of the equivalence proved in the prose.

Nine repairs explicitly number footnotes 7–13 and 39–40. Optional LaTeX footnote numbers do not advance the counter, so those originally unnumbered commands produced incorrect numbers. The final rendered sequence is 1–45; note 16 already has a correct explicit counter reset in the supplied source. Note text is unchanged. The tenth repair adds `no-math` to `fontspec`: the original mixture of OpenType text and legacy mathematical fonts otherwise loses the bold Delta glyph. No mathematical expression is changed by this repair. The source labels manuscript page 48 as blank and explicitly states that there is no page 48; the register therefore has no separate assertion assigned to it.

## Mathematical findings and repairs

### Axioms and comparison hypotheses

The original L4 is the absolute asphericity criterion; L4 bis on manuscript page 44 is the relative comma-category criterion. The commentary does not substitute one for the other without proof. It expands the initial implication from L1, L2 bis, and the original L5: interval invariance gives invariance under adjunctions; a twisted-arrow construction gives opposite invariance; applying the fibration axiom to the opposite comma resolution yields relative descent. This establishes the implication under that stronger package. It does not claim a logical-independence theorem for weaker axiom lists. Cisinski's modern definition uses the relative formulation directly (Cisinski, 2004, Definition 1.1.3 and Remark 1.1.4).

The original L5 passes from fibrewise to total equivalence for Cartesian maps between fibrations. The new L5 on page 43 detects fibrewise equivalence from total equivalence between homotopy fibrations. Their strengths are different. The pure coarse comparison across the thirteen categories uses natural weak-equivalence units and does not require the new L5. The latter is used to identify coarse and fine classes on internal objects and realize their common theory as the full locally constant part of the fine theory.

For a map over a base, total, strict fibrewise, overcategory, and undercategory equivalence are distinguished throughout. The latter two are the left-fine and right-fine conditions. The appropriate properness or smoothness criterion identifies strict fibres with comma fibres (Maltsiniotis, 2005, Theorem 1.2, Corollary 4.16, and Theorem 5.4). The inclusion `{0} → [1]` over `[1]` is a total weak equivalence of split fibrations and is left-fine, but its fibre and right-comma map at 1 are the map from the empty category to a point. Fibre evaluation detects that it cannot become invertible in the fibrewise localization. This refutes the initial withdrawn comparison and the literal coarse/fine equality on page 47; the correct border equality is fibrewise/fine.

### Strictification, naturality, and variance

A Cartesian functor need not preserve chosen lifts strictly. The constant fibration `[1] × BC2 → [1]` admits a Cartesian endofunctor that twists the chosen lift. The extension `BC4 → BC2` gives a fibration without a splitting. These distinguish fullness and ordinary essential surjectivity from the homotopical comparison actually sought; the latter remains valid after the appropriate repair (Grothendieck, 1971, Exposé VI, §§8–9).

The free split adjunction is proved with splitting-preserving morphisms, by explicit formulas and the uniqueness of Cartesian lifts. Its right-fine unit is proved by a comma contraction. An arbitrary functor over the base does not make the pullback retraction strictly natural, nor necessarily natural up to an invertible comparison before localization. The development at page 57 constructs the canonical, possibly noninvertible comparison. Natural transformations over the base become equalities after fine localization because the cylinder projection is fine. This supplies the natural isomorphism needed in the localized proof.

The covariant theory is `HOT_W(S^op)`, with no outer opposite on the category. Opposite total categories preserve the direction of functors between them. The contradictory prose and editorial formula on pages 33 and 50–51 are confirmed edition readings, while the central display on page 50 already has the correct variance. All printed forms are retained and audited separately.

The inference from `k ψ ≅ id` to fullness of `k` on arbitrary pairs of objects is false. A discrete two-object category mapping to the terminal category supplies the counterexample. The same equation does prove essential surjectivity of `k` and faithfulness of `ψ`. The audit labels this particular inference false without denying the eventual equivalence theorem proved by later arguments.

### Homological and truncated counterexamples

The integral-homology suspicion on page 43 is settled by the perfect functor

`B(Z[1/2] ⋊_2 Z) → BZ`.

Its strict fibre is `B Z[1/2]`, with first integral homology `Z[1/2]` and zero higher positive homology; the latter is proved from the filtered-colimit presentation of the group. The mapping-torus sequence shows that the total projection is an integral homology isomorphism, since `1 − 2` is invertible on the nonzero fibre homology. Surjectivity of the group homomorphism verifies perfectness directly. The simpler action-groupoid covering example treats coefficient rings in which the covering degree is invertible, and its pullback along a contractible perfect cover disproves L6 as well (Hatcher, 2002, Example 2.48, for the standard homological calculation).

Finite homotopy truncations fail the new L5 and L6. A perfect replacement of the point over `K(A,n+1)` has contractible total space and fibre `K(A,n)`; the self-pullback gives the L6 obstruction. Conversely, under the standing inclusions `W_infinity ⊆ W ⊆ W_0`, iterated loop fibres show that the new L5 forces `W = W_infinity`. The component condition is essential: the maximal class of all functors refutes the shortened unqualified list in footnote 28. Cisinski's characterization includes the corresponding hypothesis on components (Cisinski, 2004, Theorem 2.3.6).

### The reflection and its modern interpretation

The final reflection lemma works with its stated hypotheses. For `Σ0 ⊆ Σ`, `CΣ ⊆ Σ0`, a natural unit in `Σ`, and its components at `CX` in `Σ0`, the fine-to-coarse localization has a fully faithful right adjoint induced by `C`. Both triangle identities are proved. In the fine localization put `T = RP`, `a = e_(Tx)`, and `b = T(e_x)`. Naturality at `e_x`, then application of `T` and cancellation of the invertible `b`, gives `T(b) = T(a)`. Naturality at `a` and `b` gives `T(a) = e_(T²x)` and `T(b)a = e_(T²x)b`; cancellation yields `a = b`. The generally noninvertible `e_x` is never cancelled. Path concatenation supplies an additional geometric proof, not a missing-coherence repair.

For ordinary weak homotopy equivalences the modern theory is the homotopy category of coherent space-valued diagrams. Its locally constant part is the homotopy category of spaces over the groupoid completion of the base. The homotopy category is taken after forming the slice. The point over `BZ` has endomorphism group `Z` in this category, but only one endomorphism in the ordinary slice of the homotopy category. The interval example computes the reflector of `B → A` as the constant diagram on `A` and distinguishes the separate right adjoint determined by `B` (Thomason, 1980; Lurie, 2009; Cisinski, 2009).

## Developments, continuity, and unresolved scope

Exactly two blocks are marked `development`, each with `\ours` after its result heading. The first is the integral-homology application. Its ingredients are standard; the checked passages are Hatcher's mapping-torus calculation and Cisinski's discussion of homological local constancy. The second is the localized-naturality repair for arbitrary functors, compared with the strict/pseudo and splitting formulations in Emmenegger et al. (2024), §§2 and 5. The claims about not finding these particular applications are confined to those checked sources. Neither marking asserts priority or an exhaustive literature search.

The free split adjunction, the formal reflection lemma, the Hopf example, and the truncation argument are expanded without being advertised as new. The path-category construction itself is an input from outside this excerpt; its use and required properties are checked here. The supplied earlier-package index was read for continuity, especially the coherence and evaluation discussions in DER_I-a. Full earlier packages were not supplied and were not represented as independently re-audited.

The audit does not call the weakest absolute-versus-relative axiom relationship a settled independence result or a current open research problem. It proves the implications needed here and records the hypothesis missing from the weaker printed argument. The continuation beyond manuscript page 70 remains outside the assigned scope.

## Literature verification

Cumulative bibliography keys are reused wherever applicable. Every entry has a URL or DOI. Under `FORMAT.md`, `note = {verified}` means that the source was opened; it does not mean that every page of a book was read. The scope is recorded below. Cisinski 2009 theorem numbers are from the published version; its preprint has different §3 numbering.

| Key | Material checked |
| --- | --- |
| `Grothendieck1990VI` | The assigned pages in the complete edition, including the two supplemental pages. |
| `Grothendieck1983` | *Pursuing Stacks*, §69, for diagram-localization and integration of homotopy types. |
| `Grothendieck1991Letter` | Letter to Thomason, 2 April 1991, for the programme's historical framing. |
| `GrothendieckSGA1` | Exposé VI, §§8–9 and §11(a): pseudofunctors, cleavages, splittings, group extensions, and the arrow category. |
| `Cisinski2004Minimal` | Definition 1.1.3, Remark 1.1.4, Proposition 1.1.5, and Theorems 2.2.11, 2.3.2, 2.3.6. |
| `Cisinski2009LocallyConstant` | Published equation (1.7.1), Scholium 1.26, Corollary 2.5 with its left proper combinatorial hypothesis, Proposition 3.10, Theorem 3.13, Proposition 4.4, and Corollary 4.5. |
| `Maltsiniotis2005Asphericite` | Theorem 1.2 in the introduction and its dual explanation, Corollary 4.16, and Theorem 5.4. |
| `Hatcher2002` | Examples 2.48, 4.45, and 4.51: mapping-torus homology and the Hopf bundle. |
| `EmmeneggerMesitiRosoliniStreicher2024` | Publisher metadata and arXiv version 2, especially the introduction, §§2 and 5, Theorems 2.6 and 5.4. The publisher's full PDF could not be retrieved; the opened preprint supplies the mathematical text. |
| `Gray1966` | Publisher metadata and DOI. The full proceedings PDF exceeded retrieval limits. The classical attribution is corroborated by Emmenegger et al.; no unread Gray passage or absence claim is invoked. |
| `GabrielZisman1967` | The Rochester scan was opened but its text was not extractable. Classical bibliographic context only: all localization arguments needed here are supplied directly, without unsupported pinpoints or absence claims. |
| `Groth2013` | Definition 1.8, Lemma 1.9, and Proposition 1.30, for strong derivators and coherent-arrow realization in the claim register. |
| `Thomason1980` | Introduction and Theorem 4.9. The objectwise comparison of projective diagram models is explained with its assumptions. |
| `Lurie2009HTT` | Theorems 2.2.1.2 and 3.2.0.1; Propositions 4.2.4.4, 4.3.3.7, and 5.2.7.4. Space-valued and category-valued straightening are distinguished. |

No reference is certified from a search snippet alone. This is targeted verification of the chapter, not a complete bibliographic survey through the completion date. The full author–year publication data and links are in `DER_VI-a_references.bib`; the reader follows the supplied author–year bibliography workflow.

## Build and verification

The supplied `build_reader.py` is unchanged. It checks and assembles all 37 blocks. `validate_audit.py` adds checks of CSV enums, unique IDs, source markers, control characters, per-block placement of `\ours`, explicit footnote numbering, citation keys, reference verification fields, overview length, and the final compiler log. Its JSON output and final build logs are in `qa/`.

The executed workflow is:

```bash
python audit_source.py
python merge_audit.py
python build_all.py --isolated
python validate_audit.py
python pdf_audit.py --reader
```

The build script runs the supplied builder, LuaLaTeX, BibTeX, and two further LuaLaTeX passes. All five stages exit 0. The final log has no LaTeX errors, missing characters, undefined references or citations, or overfull boxes. Remaining diagnostics are ordinary margin-label displacement notices and an underfull line in a long typewriter editorial bracket. They were inspected visually, cause no collision or clipping, and were not hidden by suppressing diagnostics.

The runtime had LuaHBTeX 1.17 from TeX Live 2023 but lacked the format, Lua font-loader support, French patterns, and font-map configuration needed by the source. `bootstrap_tex.py` builds an isolated support tree without changing system files. The six package archives, source URLs, hashes, and code are included. The compatible Babel French package is the archived TeX Live 2023 release. On a complete normal TeX Live installation, run `python build_all.py` without `--isolated`. To reproduce this restricted runtime, first run `python bootstrap_tex.py`. PDF inspection uses PyMuPDF and Pillow; neither is required for TeX compilation.

Every reader page was rendered and visually checked. Independent reviews covered the middle and late sections, with full-size checks of dense diagrams, footnotes, mathematical glyphs, the overview, and the bibliography. The reviews corrected detached footnote calls, spacing after the development marker, an oversized diagram, early forced page breaks that stranded text, an accidental form-feed in a CSV note, a claim's page label, and a reference to thirteen functors where the source has thirteen categories. Mathematical cross-review checked the original-L5 proof, integral homology, localized naturality, both reflection triangles, and the slice example. These are mathematical checks performed by AI agents, not proof-assistant certification.

### Reader adaptations and format proposals

The companion style adds an English cover and contents, restrained links, concise manuscript anchor headings, language selection, and a reference entry in the contents. The source preamble adds English alongside French, A4 geometry, microtypography, and display-break penalties. Two early numbered-page hard breaks become continuous pagination, matching later source pages. Margin labels are ragged right, and the largest five-column diagram has smaller column separation. These are typesetting changes; the original source and style remain in `source/`.

Future versions of the builder could validate each block's `\ours` restriction, the 20-character substring minimum, CSV enums and duplicate IDs, and accidental control characters. The added validator performs these checks without changing the original builder. A richer reference-verification field could distinguish metadata, opened scans, and checked theorem text. Separate physical PDF, printed, and manuscript page fields would prevent the boundary ambiguity encountered here.

## Credit

The requested project credit was: “by GPT-6 Astra (OpenAI, ChatGPT Pro mode), edited with Claude (Anthropic)”. This audit and commentary were produced with GPT-6 Astra and cross-reviewed by GPT agents in this session. No Claude editing pass was available or carried out here, so the requested credit is recorded without certifying that part of it. The cover credits the work actually performed. No person's authorship is claimed for the AI-produced commentary; the source's author and editorial credits are preserved.
