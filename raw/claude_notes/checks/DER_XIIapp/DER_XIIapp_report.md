# Chapter XII appendix: audit report

**Commentary, audit, and mathematical developments:** GPT-6 Astra (OpenAI, ChatGPT Pro mode).  
**Date:** 10 November 2026.

The French source is Alexander Grothendieck's, in the electronic edition deciphered and transcribed by M. Künzer, J. Malgoire, and G. Maltsiniotis. This delivery does not certify any subsequent assembly or editing with Claude or another system.

## Scope and continuity

The whole supplied appendix was read: all 14 PDF leaves, including the title; edition pages 1–13; manuscript pages 1–18. Every leaf was rendered and visually inspected. The attached PDF covers the complete transcription, so no missing source page had to be reconstructed.

The three page systems are kept distinct. Corrections use PDF leaf numbers; claims and commentary anchors use manuscript numbers. The reader labels edition markers `ed.` and manuscript markers `ms.` in the margin, independently of its own pagination.

| PDF leaves | Edition pages | Manuscript pages represented |
|---|---|---|
| 1 | Unnumbered title | — |
| 2–4 | 1–3 | 1–4 |
| 5–6 | 4–5 | 5–7 |
| 7–9 | 6–8 | 8–12 |
| 10–12 | 9–11 | 12–16 |
| 13–14 | 12–13 | 16–18 |

The supplied `index_earlier.md` stops at `DER_VII-a` and contains no appendix blocks to duplicate. Relevant earlier entries in `DER_II-a`, manuscript pages 35–36, are cited by their supplied titles. Their full companion files were not supplied; no claim is made to have inspected them. The mathematical assertions used from other chapters were checked in the editors' primary PDFs.

## Collation

`DER_XIIapp_corrections.csv` has **26 records**. One substantive transcription reading was changed: the PDF prints `\{0\}\cup\{0,1\}` on manuscript page 5, while the supplied transcription silently substituted “et.” The printed union was restored. Its intended meaning is separately recorded as an edition slip, since literal set union would contradict “deux objets.”

A second applied repair concerns LaTeX serialization. The three-object diagram inside the italic proposition on manuscript page 13 contained raw ampersands inside a macro argument and did not compile. Escaped separators with `ampersand replacement=\&` preserve every object, arrow, and word.

Both `% ??` flags are resolved. The curved `c_{i+1}` arrow is solid. The script letter in display (**) and the covering-category display is `\mathcal X`, also confirmed from the PDF's CMSY glyph information. The printed `[?]` after “pour” on manuscript page 14 is the edition's own uncertainty. It remains; the original manuscript would be needed to decide that word.

Every existing `% [sic]` flag was checked. The undefined `a_0` and `u_0`, unclosed parenthesis, provisional `H^2`, wrong base `S`, inconsistent ambient-category names, and linguistic slips remain in the French source. The ledger also records the missing argument of `Hom_X(b×b)`, `F` for the corner category `V`, the repeated `π_1(V'_0)≃Z`, and the intended crossing comma category. A printed index slip is distinguished from a false inference: replacing `H^2` by `H^1` does not repair the false cokernel calculation.

The source's existing editorial brackets, including corrections and uncertainties, are preserved. Presentational changes are documented below and in the saved transcription diff.

## Main mathematical results

### Exact products and the monoid example

The opening simple-connectivity proof is complete once its printed notation slips are understood. The product determines a terminal object in the groupoid completion. The stronger weak-contractibility proposition is false, but the later four-object example does not satisfy its product hypothesis.

For the actual two-object category `X_G`, the opfibration and spectral sequence are valid. The provisional derived-limit calculation omits the transposition and common retraction. The commentary supplies a projective resolution for the full indexing category and computes all derived limits. It proves that `BX_G` is **2-connected for every monoid G**, whereas `H³(BX_C₂; F₂) ≅ F₂`. The finite 26-arrow counterexample survives, with its first obstruction in degree three.

The opening footnote's stronger assertion—failure of 2-connectivity under the exact product hypotheses—is also verified. A separate three-object family `Y_r`, for `r≥1`, has classifying space homotopy equivalent to a wedge of `(r−1)(r−2)/2` two-spheres. The new source's comma category retracts up to homotopy onto the subdivided complete graph; the total nerve is a mapping cone over a contractible base. Thus `Y_3` has 21 arrows, an actual categorical product, and homotopy type `S²`. Neither the failed monoid calculation nor the weaker presheaf condition is used to establish this.

### Representable spans, sphere models, and boundaries

A pushout of representables is computed pointwise as the component set of a bipartite multigraph. Its terminality forces simple connectivity. If one leg is monic, the relevant components are stars; an explicit category-of-elements comparison and Quillen's Theorem A prove the asphericity asserted in the source.

The proposed retraction of the four-object category onto the parallel-arrow circle is impossible: its equalizing relations would identify the two distinct arrows. Its nerve is two cones on that circle, hence `S²`. Adding two terminal vertices gives the six-object `S³` pushout obstruction. These are proved directly from the nerves, without an unrestricted converse to a comma-category criterion. The repeated source claim `π₁(V'_0)≃Z` is false, and this degree-three obstruction does not prove the extension to every `W⊆W₁`.

The boundary discussion separates local asphericity over the cosieve closure from asphericity over the entire ambient category. The four exceptional slices are contractible but have no final object. Both closed Dwyer inclusions used to transport the obstruction are verified by explicit adjoints. The reflection step on manuscript page 16 is repaired using the two additional horizontal weak equivalences in that specific square. The higher-dimensional extension carries the same finite obstruction to every cubical boundary of dimension at least two, with a complete proof.

### Total asphericity and gluing

The total-asphericity question uses the universal left-Kan-extension convention of this chapter, expressly distinguished by the editors from the terminology of *Pursuing Stacks*. Filtered categories satisfy it. The commentary proves directly that the category of elements of the resulting filtered colimit of representables is filtered. Both `(N,≤)` and the one-object category of an unsplit idempotent lack a terminal object; the latter also makes the nonrepresentable terminal presheaf explicit. The source's own correction in Chapter XII, manuscript page 109, footnote 78, and the earlier Chapter II argument are cited.

The final `W∞` gluing conjecture is proved. For a full sieve `A`, its complementary cosieve `B`, and the ordinary category `E` of crossing arrows, the specified comparison

`hocolim(BA ← BE → BB) → BX`

is a weak homotopy equivalence. Mixed simplices cross once, giving an explicit double mapping cylinder. Thomason's theorem, in a checked contravariant formulation, identifies its bridge with `BE`. Compatibility with the specified natural transformation is proved, so the conclusion concerns the manuscript's canonical comparison.

The finite acyclic-link construction disproves reflection of weak equivalences by this homotopy pushout for `W∞`. The source's axiom labels require care: Chapter XVI's full reversible Loc (6) would supply reflection, but that stronger condition fails for `W∞`; Chapter XV uses Loc (6) differently, and the appendix literally writes Loc (6a′), whereas XVI writes Loc (6′a). The commentary records the checked formulations and does not silently identify these differently placed primes. The exact chronological convention intended by the appendix's bare labels could not be certified. This does not affect the proved `W∞` comparison or its membership in every `W⊇W∞`.

The covering-descent argument is written out, including both mixed composition laws. Higher local systems follow from the proved homotopy pushout. Replacing crossing arrows by the usual all-paths space fails already for the parallel-arrow circle: its new bridge has components indexed by the integers and produces a countable wedge of circles. The excerpt does not define the morphisms of its raw path category. The calculation is explicitly restricted to the usual homotopically correct all-paths model.

## Source status and literature

The claim ledger covers definitions, propositions, questions, subsidiary assertions, and the cartesian/cocartesian labels in the source diagrams. `proof_status` describes the source according to `FORMAT.md`; repairs and later proofs are placed in their own columns. True counterexample conclusions with defective sketches are distinguished from the particular false computations used to support them. Commentators' statements are identified in the notes.

Every bibliography entry has a URL or DOI and a specific verification note. The supplied cumulative keys are reused when they identify the same work. Cegarra's paper supplies checked proofs of the comparison and spectral sequence. Thomason's 1979 metadata and theorem statement were checked, but his original full article and proof were not directly inspected; the bibliography states this. Thomason's 1980 pushout theorem and Cisinski's correction were read in the primary texts. The later Dwyer-map and cartesian-model results identify the exact checked preprint versions and verified publication metadata. Giraud is cited for historical terminology with limited metadata-and-description verification, not as an unchecked source of the higher result.

Six results carry `\ours`: the base resolution, repaired low-degree monoid calculation, `Y_r` product family, higher-dimensional boundary extension, finite-poset acyclic-link application, and exact open–closed gluing specialization. Each is proved completely. Established ingredients are cited, and the exact formulations not located in the checked sources are identified. The markers record the work supplied here, with no priority claim or assertion of an exhaustive literature search.

No exhaustive classification of totally aspherical categories, minimal arrow count, or definition of unspecified path-category morphisms is claimed. The editorial `[?]` and changing localizer labels are explicitly bounded source limitations, not concealed gaps in the proved statements.

## Exact supplementary computations

Independent reviews checked the main proofs, overview consistency, and completeness of the source-claim inventory. Supplementary computations are recorded in `verification/math_checks.txt`; their scripts are included in `notes/`.

The four-object sphere has normalized nerve counts `(4,6,4)` and rational Betti numbers `(1,0,1)`, with an explicit nonzero integral 2-cycle. The six-object double cone has counts `(6,14,16,8)` and Betti numbers `(1,0,0,1)`. The cubical adjunctions were checked on all relevant elements in dimensions 2, 3, and 4; the commentary proves the general-dimensional assertion.

For `X_C₂`, counts through degree three are `(2,24,386,6200)`, and boundary ranks over `F₂` are `(1,23,363)`. Streaming all 99,586 degree-four simplices gives rank 5,836, so the third Betti number is `6200−363−5836=1`. No floating-point rank calculation is used. These finite checks supplement the integral homotopy-type proofs and the all-monoid theorem; they do not replace them.

## Build and reproduction

The archive contains the six requested files, corrected transcription, assembled reader TeX and PDF, supplied builder, style, source PDF, computation and production code, and verification records. The original transcription and kit instructions are retained under `source/`.

The supplied `build_reader.py` is unchanged. Style adjustments select English inside commentary, show compact manuscript-page labels instead of full anchors, wrap URLs, space the `\ours` marker, and add explicit credit and PDF metadata. The transcription's preamble adds English support, geometry, microtypography, and separated marginal labels. The solid induction arc has more bend for label clearance. Apart from the recorded union reading and matrix serialization repair, no mathematical reading of the French source was altered.

On a normal TeX Live installation with LuaLaTeX, French Babel, TikZ, the standard math fonts, and the packages named in the source/style, run:

```bash
python build_reader.py DER_XIIapp
lualatex -interaction=nonstopmode -halt-on-error DER_XIIapp_reader.tex
bibtex DER_XIIapp_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XIIapp_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XIIapp_reader.tex
```

`python code/build.py` runs the sequence and saves logs. `code/assemble.py` reproduces the integration of saved fragments. `code/render_reader.py` renders every page and records text extents. The optional bootstrap script documents repairs to the audit container's incomplete TeX installation; these are environment changes. The small integral/rational checks require SymPy; visual rendering additionally uses Poppler, PyMuPDF, and Pillow.

### Final production result

The supplied builder accepts all **22 commentary blocks**, all exact anchors, both CSV schemas, and all **20 references**. The final audit contains **145 claim rows** and **26 correction records** (two applied transcription/serialization repairs, twenty-one retained edition slips, and three resolved-reading records). The two original `% ??` flags are both resolved.

LuaLaTeX, BibTeX, and two subsequent LuaLaTeX passes completed successfully. The final LuaLaTeX log contains **no errors, warnings, undefined citations, missing glyphs, overfull boxes, or underfull boxes**. The reader has **31 pages**. Its overview occupies **reader pages 27–29**, within the requested two-to-five-page limit. Every page was rendered, and the final visual reviews are included in `verification/`. No text bounding box extends outside a PDF page. Source-body comparison mechanically confirms that only the documented reading/serialization changes and diagram clearance differ after comments and the preamble are excluded.

The final PDF SHA-256 is `77220911a31d67277ba18e2eb7327f1d0c312895c84f00b6096b9b1734e0ad25`. Detailed machine checks are in `verification/validation.json`; the final build logs, bibliography log, source diff, and exact computation outputs are preserved alongside it.
