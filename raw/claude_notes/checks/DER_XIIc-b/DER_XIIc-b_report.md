# DER_XIIc-b: completed audit and commentary

**Commentary and audit:** GPT-6 Astra (OpenAI, ChatGPT Pro mode). No human authorship is claimed. Subsequent assembly or editing with Claude is outside the work certified here.

## Scope and authority

The entire attached extract was read and audited: **PDF leaves 1–34**, **edition printed pages 145–178**, and **manuscript pages 228–275**. These three systems remain distinct in the registers. Although the prompt labels the package section 6, part 2, its actual contents are the end of section 6 followed by sections 7 and 8. The audit follows those contents, including the continued opening footnote, duplicate proposition/corollary numbers, and the appendix through its final corollary.

The attached edition PDF is the authority for readings. All 34 leaves were rendered and visually inspected, with overlapping responsibility at transitions; source paragraphs, formulas, indices and diagrams were compared with the TeX. The full official XIIc file was consulted for preceding definitions and hypotheses on manuscript pages 207–210 and 215–218. The supplied continuity index ends with DER_VII-a and supplies no immediately preceding XIIc-a entries. Relevant earlier commentary in DER_VI-b is referenced, but overlap coverage absent from the index cannot be certified.

## Completed files

| Required file | Contents |
| --- | --- |
| `DER_XIIc-b_blocks.tex` | 32 anchored English blocks; approximately 11,700 whitespace-delimited words including TeX notation. |
| `DER_XIIc-b_overview.tex` | Approximately 1,460 words; three reader pages. |
| `DER_XIIc-b_claims.csv` | 150 audit entries covering all 48 manuscript pages. |
| `DER_XIIc-b_corrections.csv` | 46 entries: 43 retained edition slips, one mathematical transcription correction, and two groups of mechanical diagram corrections. |
| `DER_XIIc-b_references.bib` | 16 distinct references, with cumulative keys reused and precise verification notes. |
| `DER_XIIc-b_report.md` | Scope, findings, limitations, verification and reproduction. |

The ZIP also contains the assembled reader TeX and **50-page PDF**, corrected source input, unchanged supplied builder, adjusted style, original source and kit files, constituent audit evidence, finite-check scripts, assembly and validation scripts, and final build logs. Downloaded third-party papers and the large temporary TeX distribution/cache are excluded; their URLs, verification scopes and reproducible setup instructions are included.

There are 18 exposition blocks, six worked-example blocks, five later-development blocks, two context blocks and one development block. Current status appears within the relevant exposition and later-development blocks. The development supplies complete proofs, marks its result with `\ours`, names the literature checked, and claims no priority.

## Audit conventions

Source-proof statuses are **72 proved, 20 sketched, 43 stated, four assumed, three conjectured, three open and five false**. These record the source's treatment, as FORMAT.md requires. The three `open` entries are historical questions at their appearance in the text; their repair and notes columns explain the resolutions. None is asserted to remain open today. A later proof does not retrospectively change a deferred source proof into a completed source proof.

Separate rows cover genuine changes of assertion, including the recalled relative-fibre conditions, footnote qualifications, diagram-localization lemmas, functoriality, converse implications and definitions. Routine steps expressing one assertion are grouped. A false inference is distinguished from a true intended conclusion, and an edition slip from a transcription error.

All **23 original `% [sic]` flags**, representing **24 readings**, were checked and preserved. There are **no `% ??` flags** in the supplied source and none remains unresolved. The register includes additional unflagged edition slips. An independent whole-body comparison confirms that all 43 retained edition slips remain unchanged after accounting for the exact alpha correction and mechanical diagram formatting. Its mapping and checker are included in the audit evidence.

## Mathematical findings

### Cylinders and gluing

The fence interval with at least two peaks has the required endpoint Dwyer property. The mapping-cylinder factorization and Proposition 16 are valid under their stated assumptions. The commentary gives the intrinsic coslice definition of W-cofibration and the relevant couniversal-weak-equivalence argument. A two-point category mapping to a point gives a nine-vertex tree cylinder and an eight-edge circle cofiber. The finite-check script verifies those graph invariants and all seven slices used in the pasting proof.

Proposition 17's integral argument is valid once the transcription's alpha is restored to an interior natural transformation. Proposition 18 on page 236 uses only forward W(7 bis). The incorrect slice annotation on page 238 does not destroy its initial object or the proof. Thomason's cellular Dwyer factorization is distinguished from his false retract assertion; Cisinski's 1999 counterexample does not invalidate the particular factorization used here. The later infinity-categorical Dwyer-pushout comparison is cited with its checked preprint numbering.

### Deferred localization lemmas: complete modern repair

Lemmas 1 and 2 are deferred on pages 249 and 251, with the omission acknowledged again on page 257. The companion repairs them **under the original terminal-object, pullback and left-factorization hypotheses**, with the intrinsic definition of W-fibration. It adds neither functorial factorization nor global fibrancy.

The crucial verification is that trivial intrinsic fibrations are universal weak equivalences. Factor an arbitrary base map as a weak equivalence followed by an intrinsic fibration. The latter preserves the first weak equivalence on pullback; the base-changed original fibration preserves the comparison over the weak-equivalence factor. Two-out-of-three finishes the verification. Thus Cisinski's left-derivability axioms hold.

Every full intermediate category between Fib_W(S) and M/S has the same fibrant objects, and the restricted limits and factorizations demanded by those axioms remain among them. Cisinski (2010, Proposition 1.8) supplies condition (c). The companion then defines relative-leg fibration structures on good cospans and good squares, checks factorization and pullback, and verifies AP1/AP2 for the inclusions. Theorem 3.12 proves both localization equivalences. This argument was independently reviewed against the published definitions, proof and approximation theorem. A separate elementary proof explains the shorter route available with functorial factorization and identifies that hypothesis as additional. The source's historical proof statuses remain unchanged.

### Cartesian tests and the integral criterion

The fixed-base product retains the full span and its projections. The localization-of-adjunction argument descends the unit, counit and triangle identities. A moving-base calculation proves homotopicality on good cospans. The groupoid example `* -> BG <- *` yields the discrete groupoid G as homotopy pullback, with the isofibration and its strict fibre computed explicitly.

Replacement-independence in Proposition 19, invariance under objectwise weak equivalences, and pasting are proved directly from left factorization and intrinsic Fib_W. These proofs do not use the deferred adjunction lemmas. Strong saturation is used precisely when an arrow inverted by localization must be recognized as an original member of W. A nonempty finite-set example verifies failure of the excluded converse.

Proposition 20 is valid under its strong localizer hypotheses. The natural transformation of diagrams induces `X_tildeQ -> X_Q`; the edition reverses that arrow. Its printed orientation remains in the reader, while the commentary uses the correctly typed comparison. Chapter XVI, Proposition 1.3 and Loc(3′ bis)(a), supplies the precise fibrewise-to-total result; the weaker asphericity assertion is not substituted for it. The two-point span's integral is a four-edge circle, agreeing with the earlier eight-edge cylinder model.

### The appendix

The initial proposition under full W(7 bis) survives after repairing the gluing circularity identified by the source. Chapter XVI §3 identifies Brown's lemma but explicitly does not prove it there. The needed result is the dual of Brown's published Part I, §4, Lemma 2, whose proof was inspected. It supplies ordinary gluing, not the conservative converse.

The companion proves that pointwise cofibers of a coherent map of homotopy-pushout squares again form a homotopy-pushout square, by commuting homotopy colimits. It distinguishes the formal implication from a weak equivalence to a terminal cofiber from the additional reverse detection property. Associativity proves that cofiber detection is equivalent to conservative homotopy pushouts in the coherent formulation. The intended cocartesian Cons 2 then follows from Cons 1.

| False source entry | Page | Diagnosis |
| --- | --- | --- |
| XIIcb-A038 | 238 | The slice annotated Phi is Delta²; its initial object remains 2. |
| XIIcb-C020 | 269–270 | The full reduction of converse cube implications also requires cofiber detection. |
| XIIcb-C035 | 273 | Literal cartesian Cons 2 is false even in a stable example; the intended word is cocartesian. |
| XIIcb-C037 | 274 | The general implication `a and c => b` fails under mere cofiber theory, terminal object and retract closure. |
| XIIcb-C038 | 274 | Corollary 1 incorrectly equates the valid object-level retract criterion with that general map-of-squares implication. |

The counterexample to the general theorem is fully worked out. Hatcher's finite acyclic noncontractible complex has cellular boundary matrix `[[5,-2],[-3,1]]`, determinant -1, and a nontrivial permutation representation of its fundamental group. Its suspension is contractible. For a simplicial representative K, compare the squares with vertices `(K,K,CK,CK)` and `(K,*,CK,CK/K)`. Both compute homotopy pushouts. Their zeroth, second and third component maps are weak equivalences, whereas `K -> *` is not. All the theorem's other printed assumptions hold. Independent exact calculations check the matrix and permutation relations.

For literal Cons 2, finite acyclic complexes B and C sit inside an acyclic D with nonacyclic intersection A. The displayed inclusions are degreewise monomorphisms and intrinsic W-cofibrations. Acyclicity, the strict pullback and the cofibration property are all proved. The object-level retract argument remains valid; cofibration representatives under the terminal object make the retractions literal. Adding cofiber detection repairs the false general assertions. The final Corollary 2 already includes that conservative hypothesis and remains valid. Its stable form is explained through Mayer–Vietoris triangles, without identifying conservativity with stability.

## Transcription and presentation changes

The one mathematical PDF-to-TeX discrepancy is alpha on PDF leaf 6 / manuscript page 235. The edition has an interior natural transformation `i_Y phi_Q => i`; the supplied TikZ had attached it as a functor from Y to the punctured-square integral. The exact replacement appears in the CSV and machine-readable patch and was visually checked after compilation.

The two mechanical rows record consistent escaped ampersands in all 102 source TikZ diagrams, with nested arrays protected, and invisible matrix cells needed by baseline coordinates and free-ending continuation arrows. These add no mathematical objects or visible labels. All visible source arrow orientations except the actual alpha transcription error are retained, including the edition's reversed lambda.

Presentation changes are isolated in the assembly script and style: A4 geometry, restrained running headers and opening credit, English roman commentary, compact page-only commentary headings, source margin labels, and scaling of the single exceptionally wide product diagram. Fontspec's no-math option preserves legacy bold Greek glyphs. Hyperlinked footnote anchors are disabled for the unnumbered continued footnote. A commentary anchor was moved to the end of the page-254 formula to avoid interrupting the source sentence between “ou en” and its continuation. The supplied builder is unchanged; its checksum is recorded.

Visual review also led to five exact layout-only patches: the opening factorization's column spacing, separation of the cylinder's retraction labels, placement of its long dotted projection, and vertical-label placement in the two appendix cubes. They preserve every quoted mathematical label, arrow direction and endpoint. Commentary headings reserve enough space for opening prose. The exact patches and the final visual-check record are included.

## Literature verification and limits

All 16 entries have a URL or DOI and a specific `verified:` note. Cumulative keys were reused and duplicate cumulative entries consolidated. The theorem numbers for Hackney–Ozornova–Riehl–Rovelli and Groth–Ponto–Shulman refer explicitly to the checked arXiv versions; publication metadata was verified separately.

Brown's original axioms and gluing proofs, Cisinski's published derivability and approximation results, Groth's published adjunction/essential-image/pasting results, and the relevant parts of Chapter XVI were inspected. The original **1979** Thomason proof was **not** inspected: only its publisher metadata and abstract were checked directly, while its statement and a later proof were checked in Chachólski and Scherer, arXiv v1, Theorem 26.8 and Corollary 26.9. The **1980** Thomason paper was checked separately. The bibliography preserves this distinction.

Historical discussion of SGA 5 comes from the checked section 69 of *Pursuing Stacks* and the 2 April 1991 letter to Thomason, not an independent audit of SGA 5. No exhaustive search of all later literature is claimed. The diagnostic cube is an application of a classical example developed here, with its checked literature identified and no priority claim. No present-day open problem is inferred merely from an absent source proof.

## Build and reproduction

The unmodified supplied builder accepts all six files, 32 anchors, citation keys, CSV headers, unique IDs and enumerated values. The reader was built with LuaLaTeX, BibTeX and two subsequent LuaLaTeX passes. Final passes have **no errors, undefined citations or references, missing glyphs, overfull boxes or underfull boxes**. BibTeX has no errors or warnings. Eleven ordinary LaTeX messages report automatic movement of source margin labels; they remain in the logs rather than being suppressed and were checked visually.

`validation.json` records the register counts, all 48 manuscript pages, 34 edition markers, bibliography checks and reader pagination. Every PDF page was rendered for visual inspection; `visual_qa.md` records the final review. Finite computational checks supplement the proofs rather than replacing them.

On a complete TeX Live installation, run in the extracted ZIP directory:

```bash
python build_reader.py DER_XIIc-b
lualatex -interaction=nonstopmode -halt-on-error DER_XIIc-b_reader.tex
bibtex DER_XIIc-b_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XIIc-b_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XIIc-b_reader.tex
```

To reconstruct assembled inputs, first run `python code/assemble_companion.py`. The included final audit fragments incorporate peer-review refinements and are the authoritative assembly inputs. Historical register-authoring scripts are retained for provenance.

The initial environment had incomplete TeX configuration. A process-local repair used existing read-only data plus checksum-verified Debian LuaTeX/French packages, generating the format within the workspace. Setup scripts, package manifest and wrapper are included. No system or home-directory files were changed. A normal TeX Live installation does not require this repair.
