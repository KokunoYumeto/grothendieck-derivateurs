# Chapter XVII, part b: mathematical audit and commentary

**Commentary and audit produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).** This credit concerns the files delivered here. It neither attributes the commentary to a person nor certifies subsequent assembly or editing with another system.

## Scope and reading

The audit covers the supplied excerpt continuously, including its opening continuation of manuscript p. 57 and all material through p. 118: Corollary 3.5 to Corollary 6.5. The three numbering systems remain separate.

| Numbering system | Extent |
|---|---|
| Attached PDF leaves | 1–32 |
| Leaves of the editors' complete Chapter XVII file | 31–62, including its preliminary leaves |
| Edition printed pages | 29–60 |
| Manuscript pages | Tail of 57, then 58–118 |

For this excerpt, **PDF leaf = printed page − 28**. Its opening continuation has no new manuscript-page marker.

All 1,592 lines of the original transcription were read, including formulas, diagrams, footnotes, and proof transitions. All 32 authoritative PDF leaves were rendered and visually inspected in three overlapping ranges. Formula and variance suspicions were checked against these images before classification. The initial suspicion about the comma category on p. 70 was rejected: `i'\I` is correct after the switch to presheaves.

The supplied format, earlier-commentary index, cumulative bibliography, and assembly code were read. The index ends at Chapter XII's appendix and contains no XVII-a entry. The commentary refers to the indexed collage and terminal-fibre discussions without claiming access to an unavailable XVII-a companion. Nonduplication with that absent commentary cannot be certified.

Immediate dependencies were checked in the complete official XVII PDF: definition (2.2) and Theorem 2.1, ms. 25–27, and Cof0–Cof3, ms. 39. The old derivator axioms were checked against Chapters XVI and XIX. Chapter XV, Proposition 4.2, its proof and corollaries, ms. 29–31, and the following discussion on ms. 32–36 were checked for the lifting-closure comparison. These supplementary checks have their own bibliography notes.

## Deliverables and coverage

The six required files are complete. The package also contains the built reader, unchanged supplied builder and style, corrected transcription, untouched original transcription, authoritative excerpt PDF, and reproducible assembly and validation code.

| Deliverable | Extent |
|---|---|
| `DER_XVII-b_blocks.tex` | 26 anchored English blocks; approximately 11,900 whitespace-delimited words of TeX, including four development blocks |
| `DER_XVII-b_overview.tex` | Approximately 1,600 words; three reader pages; no section or chapter commands |
| `DER_XVII-b_claims.csv` | 180 individually identified rows |
| `DER_XVII-b_corrections.csv` | 59 decisions: 52 retained edition defects, five transcription corrections, two resolved doubts |
| `DER_XVII-b_references.bib` | 20 distinct entries, reusing cumulative keys where available; each has URL/DOI and a specific verification note |
| `DER_XVII-b_report.md` | This report |
| `DER_XVII-b_reader.tex` and `.pdf` | Complete interleaved reader; 50 A4 pages in the checked build |

The claims comprise 15 definitions, six axioms, 42 propositions, 106 claims, four questions, three conjectures, and four remarks. The source-status counts are 110 `proved`, 42 `stated`, nine `sketched`, seven `assumed`, six `false`, four `open`, and two `conjectured`. These labels describe the source's treatment or an invalid assertion or inference as written. An `open` entry at a historical question does not assert that it remains open today; subsequent resolution and hypotheses appear in the other columns.

The independent coverage crosswalk accounts for all **38 original flags**—36 `[sic]` and two `??`—as well as **33 numbered headings, 105 tagged displays, and all 17 source footnotes, numbered 18–34**. Related proof steps are separated when their status or hypotheses differ. Routine equations within a single argument are traced to the corresponding claim rows. See `evidence/validation_audit.json` and its readable `.txt` summary.

Every claim has an explicit manuscript locator. Source prose references are normalized to bibliography keys, and references to incremental working filenames are replaced by final block titles and manuscript anchors.

## Transcription decisions

The untouched input is `source/DER_XVII-b_text_original.tex`. The idempotent `code/prepare_text.py` produces the working text and records every operation in `evidence/source_changes.json`. Edition slips are not applied as corrections. Original `% [sic]` and `% ??` comments remain as traceable provenance; every one is resolved in the register.

| Location | Genuine transcription correction applied |
|---|---|
| §3.10, ms. 65; PDF leaf 4 | The edition's discretionary line-end division `intro- / duite` is joined as `introduite`; the adjacent `associé` edition slip is retained. |
| Closure notation across §§4–6 | Postfix `postilde`, `cl`, `tl`, and corresponding empty accents are rendered as superscript closure tildes; prefix accents such as `\tilde{C}` remain unchanged. |
| Ms. 94; PDF leaf 19 | `TC'_0` is placed beneath the underbrace of `v_!(TC_0)`, rather than on the closure of the whole expression. |
| (6.1.11), ms. 100; leaf 22 | The cofibrant-subcategory subscript is restored on `M(I)` inside the argument of `u_!`. |
| (6.2.3), ms. 106; leaf 25 | The diagonal label is restored to the edition's `η(0)`; a separate edition-slip row explains the intended `η(∂)`. |

The mark in (6.1.7) is visually resolved as a superscript tilde, not a breve. The crossed two-headed arrow in Remark 5.4 records lifting together with factorization; it is not algebraic addition. These are the two doubtful readings.

Retained defects include the artinian/noetherian errors, the omitted `I_0` in (4.8.1), the extra initial equality in (5.5), missing tildes in its proof, `TW` for `TC` on ms. 88, `T` for `TC` on ms. 95, the incorrect page reference on ms. 96, the repeated `U` in the definition of `X_V`, and substitutions of a projective lifting class for the relative class actually assumed in the final induction. Exact readings and evidence are in the register. All input grammatical flags were individually checked; this was not expanded into general French copyediting.

The other working-preamble changes concern presentation: English for commentary and overview, page dimensions and stable marginal labels, URL breaking, an identification header, and PDF metadata. They do not alter mathematical readings. The supplied builder and style remain unchanged.

## Mathematical conclusions

### Adjunctions, variance, and size

Remark 3.6 correctly distinguishes a functor constructed through an equivalent localization from a derived adjunction. The commentary supplies the walking-arrow counterexample and identifies the missing comparison transformation. Deformation data and absolute derived functors give precise repairs, cited to Riehl, Theorems 2.2.8 and 2.2.11, and Maltsiniotis's unnumbered absolute-adjunction theorem.

The mapping-cylinder proof of Theorem 3.7 is sound under its indexing and colimit hypotheses. The exposition verifies mixed hom-sets, the adjunction between target inclusion and retraction, initial comma objects, cofilteredness, extension by the initial object, inheritance of the order conditions, and composition of the descended adjunctions. A derived coproduct is worked through this construction.

The arbitrary-target inference on ms. 66 requires qualification in the finite-colimit branch. Finite sets, with all maps cofibrations and isomorphisms weak equivalences, satisfy that branch, but restriction along `e → Bℤ` has no left adjoint. The development proves the sharper criterion: the forgetful functor on finite `G`-sets has a left adjoint exactly when the intersection of all finite-index subgroups has finite index. It also distinguishes existence of an abstract adjoint from the pointwise comma-colimit formula. The transfinite branch is not refuted.

In §3 the diagrams are covariant, written `M(I°)`. In §§4–6, `M(I)=Fun(I^op,M)`. Thus the former artinian hypothesis becomes noetherianity in the presheaf convention; the corresponding topology belongs to the opposite poset. This explains both the actual variance defects and the correctness of the comma symbol on p. 70. Chapter XIX, Proposition 3.2 and §3.4, explicitly gives the corrected presheaf formulation. The older axiom Dér 3 means full faithfulness of constant diagrams when the index has a final object, not existence of a final object of `D(e)`.

### Small generation, closures, and transfer

The small-object and transfer constructions are valid under their collected hypotheses. The commentary supplies the cardinal bound, attaching-map construction, intrinsic-cofibration argument, and transposition of lifting problems. Individual accessibility of objects is kept distinct from local presentability of the category.

The coproduct lemma in footnote 25 is proved by well-ordering the summands and replacing each domain summand by its codomain through a pushout. For a map of families, each component of its free-diagram image is a coproduct of coefficient maps. This is the assertion used in transfer; internal structure maps of the diagram can also involve folds.

Footnote 23 has two different answers. Proposition 5.8 proves its fibration equality. Equality with the raw free-image class is false: a fixed point included in its union with a free `ℤ/2`-orbit is a pushout of a free trivial cofibration but is not itself free. The Q-closure equality is the correct formulation, as in Theorem 6.1(b).

Propositions 5.2 and 5.8 receive complete proofs. After the second factorization is available, a two-stage pushout and retract argument proves retract stability of weak equivalences without presupposing retract stability of trivial cofibrations. This validates the subsequent comparison with modern closed model structures. Transfer identifies the trivial cofibrations by constructing their cells and retracting an arbitrary target trivial cofibration onto a suitable factor. The nonclosed variant does not silently acquire retract closure.

### Precise limitation in (5.5)

Under the original hypotheses of Proposition 5.1, the printed argument proves

\[
TC\subseteq\widetilde C\cap W\subseteq\operatorname{Retr}(TC)
\subseteq\widetilde{TC},\qquad
\widetilde{\widetilde C\cap W}=\widetilde{TC},
\]

and equality of the corresponding right lifting classes. These suffice for the earlier use concerning `F'_~ = F'`. The extra first equality in (5.5), asserting that `\widetilde C ∩ W` itself is Q-closed, is not established by that proof. Its opening equality with `Retr(TC)` also precedes the additional retract hypothesis required for the reverse inclusion.

**The audit does not decide that extra equality under every original hypothesis of Definition 4.4.** No counterexample meeting all those assumptions was established; absence of a proof is not used to label it false. The safe repair is the proved chain and equality of Q-closures. A sufficient additional hypothesis is the second factorization `(TC,F)`, for example supplied by Corollary 5.5: it gives retract stability of `W` and `\widetilde{TC}=Retr(TC)`, so the stronger equality follows. The later transfer theorem is fully justified independently of the unsupported earlier display.

### The filtered-colimit heuristic

The expectation on ms. 97 is refuted by a complete special closed triple on abelian groups. For `A=ℤ[1/2]`, weak equivalences are the maps inverted by `Hom(A,−)`, cofibrations are their left lifting class, and every map is a fibration. The generating cofibrations are `0→A` and the fold `A⊕A→A`; the second left class consists of isomorphisms. Both factorizations, both lifting systems, all model axioms, and accessibility of every object are checked.

The sequence of weak equivalences `0→ℤ`, with transition squares `(id,×2)`, has colimit `0→ℤ[1/2]`, which is not a weak equivalence. The example does preserve `ℵ₁`-filtered colimits. Raptis and Rosický, Proposition 4.1, provide the general positive statement at an appropriate regular cardinal. Specialness therefore does not force ordinary filtered-colimit stability.

### Projective diagrams and the final induction

Theorem 6.1 correctly constructs projective diagram structures and derived left Kan adjunctions. Its order-theoretic comparison has a printed direction error: for presheaves the sufficient hypothesis is noetherianity of `I`, as correctly stated in Corollary 6.3. The inverse sequence of tails `{k≥n}` in the injection–surjection model structure on sets gives a complete counterexample to the literal artinian version.

The omitted proof of Lemma 6.2.5 is supplied with exactly its pushout hypothesis. The test at the first vertex is encoded by `F ⊔_{B_1} B_0`, so no terminal object or factorization axiom is imported. Its second component condition is redundant once the first component and relative latching map lie in the left class.

The Zorn argument in Corollary 6.3 is valid. The exposition includes the naturality check and the role of well-foundedness. Latching-colimit existence is inherited from the earlier relative-class definition; pushouts alone would not supply it. The provisional restriction hypothesis in Corollary 6.2 is discharged by 6.4 and 6.5 within this excerpt. A simplicial-set diamond computes every latching object and shows why objectwise cofibrancy does not suffice.

The final restriction criterion is explained through products of evaluations. A development proves its converse for a poset source, using the characterization of projective presheaves as coproducts of representables. The concluding block derives the pointwise homotopy Kan formula using free generators and the discrete opfibration `i'\I→I`, needing only the available colimits. The broader derivator theorem and coherent-diagram comparison are related to precise results of Cisinski, Groth, and Lurie, with hypotheses and variance explicit.

## Literature verification and limits

Verification notes describe checks made in this audit, not merely notes inherited from earlier packages. Mathematical citations use primary sources. Numbering follows the identified version where necessary: Rădulescu-Banu version 4; Maltsiniotis's English 2006 preprint for the theorem with 2007 publication metadata; Riehl's author-hosted 292-page PDF; Riehl–Verity version 3; Raptis–Rosický version 2. Hirschhorn's scanned formulas were inspected visually.

Nineteen entries have substantive passage-level checks. **Quillen (1967) deliberately has a metadata-only note.** Its original I.§4, Theorem 3 locator is reproduced historically from Grothendieck, not represented as independently read. The checked Riehl Theorem 2.2.11 supports the mathematical adjunction. The exact Anderson passage was not located: the formal counterexample is validated without certifying Grothendieck's account of Anderson's wording or hypotheses.

The four development blocks have complete proofs: the finite-action criterion, abelian-group filtered-colimit example, inverse-sequence diagnostic, and poset restriction converse. Their results are marked `\ours` only in development blocks, with bounded literature-search statements. They are continuations assembled from established methods, not priority claims; no exhaustive novelty search is asserted.

Historical motivation is tied to the checked opening of *Pursuing Stacks* §69 and point 1 of the letter to Thomason of 2 April 1991. SGA 5 is mentioned as Grothendieck's stated motivation there, not as an independently audited source for a theorem used here. The commentary avoids retrospective attributions without a checked comparison.

## Build and reproducibility

The supplied builder validates the six files and inserts all 26 blocks at valid anchors. The standard sequence is:

```bash
python build_reader.py DER_XVII-b
lualatex -interaction=nonstopmode -halt-on-error DER_XVII-b_reader.tex
bibtex DER_XVII-b_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XVII-b_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XVII-b_reader.tex
```

All five commands succeeded in the checked build. Its final LuaLaTeX log contains **no errors, warnings, undefined references or citations, missing glyphs, or overfull or underfull boxes**. `code/build_all.py` records results in `evidence/build-0.log` through `build-4.log`.

The environment initially lacked format caches, Lua font-loading modules, French support, and the aggregate font map. These were repaired entirely within the workspace. `code/tex_environment.py` and `code/bootstrap_tex.py` document the configuration and dependencies; system directories and the user's home directory were not modified. The bootstrap's default inspection was run and all five cached inputs matched their recorded hashes. Its reconstructed `--apply` path was not rerun against the completed reader; mutable download URLs are protected by pinned hashes, so changed upstream bytes are rejected. A complete TeX Live installation can run the standard commands directly.

The independent validator passes all 1,947 checks of schemas, enum values, IDs, flags, page coordinates, numbered-item coverage, citation keys, verification notes, source-edit replay, and assembly consistency. Detailed and readable crosswalks are included. All 50 reader pages were visually inspected. The final adjusted pages were rendered again and rechecked; page-by-page records and closeouts are `evidence/qa_*.md`. The review covers insertion boundaries, formulas, diagrams, margin labels, clipping, and overlap. The overview occupies reader pages 46–48. The original transcription, authoritative excerpt PDF, and all five supplied kit files match their attachments byte for byte where retained.

Downloaded external books, research page images, TeX caches, and font databases are excluded from the delivery. The user-supplied authoritative excerpt is included. The single ZIP contains the six required files, both built reader files, necessary source/build support, relevant code, compact verification evidence, and a SHA-256 manifest. `code/README.md` distinguishes the final rebuild sequence from the earlier construction scripts. The archive is checked for CRC errors after creation.
