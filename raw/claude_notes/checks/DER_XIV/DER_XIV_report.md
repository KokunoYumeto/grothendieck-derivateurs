# Chapter XIV: audit and commentary report

**Commentary, mathematical audit, and independently supplied proofs:** GPT-6 Astra (OpenAI, ChatGPT Pro mode). Completed on 10 November 2026. This credit does not certify any subsequent assembly or editing with another model or editor.

## Sources and extent of the work

The reading authority was the attached eleven-leaf PDF of Chapter XIV, version 7 October 2010. All leaves were rendered and visually inspected against the complete supplied LaTeX transcription. Text extraction was a secondary aid; formulas, indices, arrowheads, cube edges, and the doubtful identity mark were checked visually. The online copy of the same chapter was also consulted. No source page is missing from this package.

| Attached PDF leaf | Edition printed page | Manuscript page | Content |
|---|---:|---|---|
| 1 | Unnumbered | None | Title |
| 2 | Unnumbered | None | Editorial notice |
| 3 | 1 | 1, then 2 | Initial motivation and start of Definition 1 |
| 4 | 2 | 2, then 3 | Definition; Cart (1), (2), start of (3) |
| 5 | 3 | 3, then 4 | Cart (3); cube and footnotes; Cart (4) |
| 6 | 4 | 4, then 5 | Cart (5); Corollary 1 |
| 7 | 5 | 6 | Corollary 2 and weak universality |
| 8 | 6 | 7, then 8 | Duality, additivity, examples, Proposition 1 |
| 9 | 7 | None | Editors’ postface: replacement criterion |
| 10 | 8 | None | Editors’ loop counterexample and rectangle |
| 11 | 9 | None | End of the rectangle argument and the final cube |

The supplied FORMAT.md, builder, style, cumulative bibliography, and entire index of earlier commentary blocks were read. The index has no direct Chapter XIV overlap. Its entries for DER_I-a, manuscript p. 7, and DER_III–V, manuscript p. 75, are referenced for the earlier coherent-square and loop-square discussions. Continuity decisions are based on this supplied index; they are not a claim to have rechecked the full text of those earlier companions.

## Transcription decisions

No substantive transcription error was detected. The corrections register has three entries: two `edition_slip_kept` and one `doubt_resolved`. The edition really prints “a un carré” without the grave accent on PDF leaf 3 and “carrés h-cartésien” without plural agreement on leaf 5. Both remain as printed. The two vertical strokes on the `X`-to-`X` edge of the strict comparison cube on leaf 10 denote the identity, matching the final cube on leaf 11; the existing `\parallel` is retained and its uncertainty comment is resolved.

All displayed squares and all five cubes were checked, including the placement of I and II, both dotted fourth-component edges, and both zero-endomorphism labels. The two substantive false proposals are retained in the source and audited mathematically; they are not recast as transcription corrections. No silent repair of Proposition 1 or the additive speculation has been made.

## Mathematical audit and principal findings

The claims register contains 65 entries: 60 covering the manuscript and editors’ mathematical content and five registering the commentary’s formal deductions. The source status of an axiom is `assumed`; its failure in the proposed model example is recorded separately. The register distinguishes stated results from supplied proofs, and the two directions of Cart (3) and Proposition 1 from one another.

The formal cube corollary is correct, including the stronger hypothesis of only the bottom and two opposite lateral faces. The commentary gives the complete pasting argument and also derives Cart (5)(b) from Cart (1)–(3). Corollary 1 follows by taking the identity on the boundary. Corollary 2 is correct and uses only the existence part of Cart (5); conversely its weak universal property implies that part of the axiom.

Proposition 1’s sufficient direction is definitional. Its necessary direction is false: an ordinary square in the localized category can have both cartesian and noncartesian coherent realizations. The editors’ strict comparison is the zero endomorphism of the loop object. The commentary proves the replacement criterion with exactly the printed fibrancy assumptions, including the equivalence of “some” and “every” replacement and the right-properness exception. These are supplied details of correct assertions, not newly alleged gaps in the postface.

The postface refutes **cancellation**, not positive composition. Positive composition for the homotopy-image class of every Quillen model category is proved here by two applications of the full and conservative arrow comparison, first for the model category and then for its arrow model category. This avoids the false supposition that arbitrary incoherent cubes lift. The stable analogue for arbitrary triangulated categories is also located in Christensen and Frankland (2022, Proposition 6.11).

The two-term example uses cohomological degrees, `X=k[0]`, `C=(k→k)` with identity differential in degrees 0 and 1, and `P=k[-1]`. The comparison for a filling indexed by a scalar λ is multiplication by λ; its cone is `k --λ--> k`. The displayed contraction transports the strict pullback to filling −1 with the chosen sign convention, while the strict zero-edge square has filling 0. The exact-arithmetic check verifies the contraction identity, the chain-map equation, and that transport sign. The proof for an arbitrary field is in the prose, not inferred from finitely many numerical tests.

Additivity alone does not imply coincidence of the two square classes: ordinary pullbacks and pushouts in vector spaces give a counterexample. The marked development proves three precise consequences of the literal axioms: a distinguished square along a monomorphism is an ordinary pullback; binary products force all pullbacks to exist and force the class to be exactly the ordinary pullbacks; and coincidence of the literal left and right structures in a pointed category forces every object to be zero. Binary products, rather than additive enrichment, suffice for the main theorem. Each proof was independently checked, including the orientations of the kernel-pair pasting and the final use of isomorphism invariance.

The coherent repair is stated with its correct quantifiers. Restriction identifies cartesian coherent squares with coherent cospans by fully faithful right Kan extension. Fourth-vertex invertibility concerns a coherent morphism; full pasting and cancellation concern a coherent rectangle. Stability is the additional condition giving coincidence of coherent cartesian and cocartesian squares. External derived Hom has the expected continuity; an internal version requires specified closed monoidal and adjunction data.

## Literature verification and limits

Fourteen distinct references are included, with cumulative keys reused where available. Every entry has a DOI or URL and a `verified:` note identifying the actual scope and version checked. The main modern sources are Groth (2013, Lemma 1.9, Propositions 1.20, 3.12, 3.13, 3.17, and the cited stable/additive material), Groth–Ponto–Shulman (2014, Theorems 6.1 and 7.1 in arXiv v2), Cisinski (2003, Theorem 6.11 and Proposition 6.13), and the cited passages of Lurie’s *Higher Topos Theory* and *Higher Algebra*. The historical paragraphs use the specified passages of *Pursuing Stacks*, the Thomason letter, and Heller’s introduction. No direct influence on this draft is inferred merely from chronological proximity.

Krause’s minimal-weak-kernel comparison is an established antecedent to the rigidity argument; it is cited rather than presented as a new theorem. The further monomorphism/pasting and binary-products consequences are marked `\ours`. The search checked the original postface, Groth’s coherent-square treatment, Krause’s weak-kernel discussion, and combinations of “quadrangulated”, “quadrangulée”, “Cart (5)”, “additive”, “pullbacks”, “weak kernels”, “right minimal”, and “monomorphism”. No prior statement of these exact consequences of this particular axiom list was located. That bounded result establishes neither originality nor priority.

Version distinctions matter. The Hovey book citations use the accessible 213-leaf author typescript, whose pagination is not assumed identical to the printed book. The sheaf-complex citations refer to arXiv math/9909024v1, including Theorem 2.2 and Proposition 2.12; its submission stamp and the PDF’s later typesetting date are recorded. Christensen–Frankland page locators refer to the author version of 7 June 2021. Hatcher’s cited online PDF includes the corrected reprinting. Groth’s Proposition 3.13 leaves its proof to the reader; the commentary gives the relevant mechanism and points to the parallel higher-categorical proof instead of claiming that Groth prints a proof there.

The general nonuniqueness remarks on manuscript pp. 5–6 have a limited status. They hold for the intended homotopy-image class, which fails the complete axioms, and cannot occur under the binary-products hypothesis of the proved theorem. This work neither constructs a nonordinary model of all five axioms without binary products nor proves collapse in that unrestricted setting. It therefore does not label the unrestricted remarks globally false, or call their status a recognized open problem. The manuscript’s informal request for further compatibility rules likewise does not specify a single current open conjecture.

## Reader format, implementation, and reproducibility

The six requested files are supplied with the built reader, the verified source needed to regenerate it, the supplied builder, a compatible local copy of the style, and the code used for preparation and verification. The supplied `build_reader.py` is unchanged. The source body is unchanged except for resolving the one uncertainty comment and normalizing CRLF line endings to LF. Every mathematical token and both printed slips remain.

Reader-only support changes load `fontspec` with `no-math` to preserve the source's bold-Delta math glyphs and load `mathtools` for its final `\mathllap`. They provide English hyphenation for the commentary while retaining French for the source, set an A4 text area, enable URL breaking, and place edition printed-page labels in the left margin and manuscript labels in the right using nonfloating `marginnote` annotations. Empty printed-page marginalia on the preliminary leaves are suppressed. Long exact-word anchors are kept out of commentary headings. The builder's last manuscript span extends mechanically through the postface; exact `p8:<words>` anchors are therefore used there, but visible headings explicitly say “Editors” and give printed pages. No manuscript page is invented for the postface.

The style’s source labels are a presentation repair; the literal anchors remain in `blocks.tex` and are checked by the supplied builder. A future version of the format could support explicit editorial-page anchors, but this package does not require a schema change. The overview has no `\chapter` or `\section` command. Citations use the requested natbib commands and the builder’s `plainnat` bibliography style.

The two scripts under `analysis/` preserve the initial audit-register generation. The delivered registers incorporate the subsequent review and the edits in `code/finalize_registers.py`; those draft generators need not be rerun to build the reader. The `code/` directory also contains source preparation, the final citation/credit layout adjustment, exact-arithmetic example checks, source-integrity checks, page rendering, final validation, environment bootstrap, and ZIP packaging. `SHA256SUMS.json` records the packaged file hashes.

### Completed build and inspection

The supplied builder accepted all 13 blocks, their literal anchors, all register rows, and all 14 bibliography keys. The reader was compiled with LuaHBTeX 1.18.0 and BibTeX 0.99d in the required order: LuaLaTeX once to write the auxiliary file, BibTeX, then two further LuaLaTeX passes. All commands exited successfully. The final LuaLaTeX log has **zero warnings, zero errors, zero unresolved citations or references, zero missing characters, and zero overfull or underfull boxes**. BibTeX emitted no warning or error.

The completed reader has **21 A4 pages**. Its overview occupies reader pages **18–20**, satisfying the two-to-five-page requirement; the bibliography begins later on page 20. All 21 pages were rendered at 120 dpi with Poppler and visually reviewed. The final review checked the five source cubes, ordinary and coherent square diagrams, mathematical displays, commentary continuations, source-page annotations, credit paragraph, and wrapping of the bibliography URLs. The bold-Delta font issue, the overlapping source-page notes, adjacent citation groups, and split credit were repaired and rechecked. The final cube on reader page 6 has a clear gap above the folio.

The exact-arithmetic example checks pass. They verify the contraction, comparison chain map, and transported comparison scalar −1, with representative scalar cases confirming the computed cone dimensions. The separate source-integrity check confirms exact body equality after the single resolved comment and newline normalization, and byte equality of the builder with the supplied kit. The final file/schema/anchor validation passes; its machine-readable record is `qa/verification.json`. Visual-review details, source-integrity evidence, the final build logs, dependency hashes, and example-check output are included.

On a complete TeX installation, rebuild from the package directory with:

```sh
python3 build_reader.py DER_XIV
lualatex -interaction=nonstopmode -halt-on-error DER_XIV_reader.tex
bibtex DER_XIV_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XIV_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XIV_reader.tex
python3 code/verify_deliverables.py
```

The session's TeX installation lacked the Lua font loader, French language support, and generated format/configuration files. `python3 code/bootstrap_tex.py --build` repaired that environment locally and executed the same build sequence. Its two Debian-package URLs and SHA-256 hashes are pinned in the script and `qa/tex_dependency_manifest.json`; no system installation was modified. The script requires an existing LuaHBTeX/TeX Live installation, `curl`, and `dpkg-deb`. Downloaded packages and generated font caches are reproducible intermediates and are omitted from the ZIP. `python3 code/render_qa.py` regenerates the page PNGs and contact sheets; it requires Poppler and Pillow.

## Credit

The commentary is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Grothendieck’s text and the editors’ postface remain separately attributable to their source. The result is prepared for later editorial assembly; no later Claude or human editing, checking, or certification is claimed.
