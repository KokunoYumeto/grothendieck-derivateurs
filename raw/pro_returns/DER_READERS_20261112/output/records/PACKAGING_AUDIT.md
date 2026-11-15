# Packaging readiness audit

## Scope and outcome

**Pass.** The input, source, correction-decision, reproducibility, editorial-ownership, six-book credits/rights, privacy, and focused margin-layout checks are complete. All six final reader PDFs and both annotated-master PDFs compiled without errors or missing glyphs. The full reader validation agrees with the final source/PDF hashes and reports zero issues. Both visible margin-label collisions found by this audit have been repaired and rechecked; no visible collision or unreviewed candidate remains.

An earlier compiler-reported grouping defect was repaired in the French decision fixture at `DER_XVIII-d:74`: the complete nested subscript in `\cardred\mathcal{M}_{\pi_0}` is grouped. It changes neither the intended reading nor the variant/row counts. The frozen French and English plans were regenerated and independently replayed after that repair. The final unit-scoped margin placements are common assembly changes recorded in `MARGIN_PLACEMENTS.tsv`; the correction plans and source anchor calls remain unchanged.

## Input manifest coverage

Every manifest-listed member was read directly from its attached archive and compared with its declared byte count and SHA-256, the verified extraction, and `MANIFEST_VERIFIED.tsv`. The original-path field was not copied into the audit records.

| Archive | Manifest members | Result |
|---|---:|---|
| `DER_01_french_transcription.zip` | 341 | Exact archive/extraction/record agreement; no unlisted payload members |
| `DER_02_english_translation.zip` | 289 | Exact archive/extraction/record agreement; no unlisted payload members |
| `DER_03_companion_newresults_conventions.zip` | 91 | Exact archive/extraction/record agreement; no unlisted payload members |

The combined inventory has **721 members** and no missing extracted file, hash discrepancy, or unmatched verification row. Exact archive hashes and detailed checks are in `PACKAGING_INPUT_VALIDATION.json`.

## Decision coverage and clean replay

| Layer | Final count | Outcome |
|---|---:|---|
| French correction source rows | 1,879 | 1,707 applied; 79 merged; 64 no change; 29 rejected with reasons |
| French actual variants | 1,982 | Exact original-source offsets; no identity or overlapping variants |
| English actual variants | 1,623 | Every French variant and every source row has a terminal English outcome |
| Explicit French decision entries | 95 | 93 no-change/rejected rows plus two applied rows with a separate decision |
| Convention table rows audited | 223 | 171 glossary, 26 notation, and 26 typesetting rows |
| Flagged convention entries | 17 | Reasons and retained/proposed renderings recorded |

Both plans were regenerated in a fresh isolated workspace containing only members extracted from the three original archives, the packaged resolver scripts, and the packaged decision files. No scratch manual-decision files were present. The regenerated JSON files are **byte-identical** to the frozen plans:

- French: `646e450030a3f36d27b9cb3c649f347ffeb0fcccbc0ba4f0f80ff78916fd0c92`.
- English: `dd3d0e7db9d7110cb9b4639ddf476eb75a7904d68a76936ab7cb4af35e423666`.

`PACKAGING_REPLAY_VALIDATION.json` records this result. The French resolver successfully used all ten fixtures from `decisions/source/french/`; their manifest hashes match the packaged files. English replay used `EN_TRANSFER_DECISIONS.json` and the supplied source inputs. It has no dependency on the working manual-transfer scripts.

## Required output inventory

The six requested standalone reader TeX files, both annotated masters, the appendix, the integrated companion master, and the requested change/decision/convention/apparatus tables are present. The change tables have the required `page`, `place`, `before`, `after`, and `source` columns. `README.md` documents the preserved `output/` directory layout, the original input archives, replay commands, dependencies, counts, and compilation reporting.

The companion directory contains all 64 part/definition files used by its master, the companion style, bibliography, generated bibliography, and the appendix. Its final 1,906-page PDF matches `APPENDIX_COMPILE_STATUS.json` and records zero LaTeX errors, undefined citations/references, or missing glyphs. The twelve appendix statements and source provenance are separately recorded in `APPENDIX_VALIDATION.json`.

The final books have the following page counts. Each final pass reports zero errors, missing glyphs, undefined references, and unsettled references; each reader/master has one documented package warning that shell escape is disabled.

| Language | Diplomatic | Corrected with apparatus | Reading | Annotated master |
|---|---:|---:|---:|---:|
| French | 915 | 1,082 | 899 | 915 |
| English | 915 | 1,061 | 902 | 915 |

The source audit reports 977 reading-omission records per language and no source/projection differences. Both masters match the corresponding diplomatic PDF text and geometry exactly. All 3,605 apparatus destinations have a valid visible incoming marker. `PDF_DIPLOMATIC_QA.md` records the refreshed 18-page inspection of the two 915-page diplomatic PDFs, including titles, credits, prefaces, dense formulas, large diagrams and final pages. `PDF_FR_QA.md`, `PDF_EN_QA.md`, and the aggregate `PDF_VISUAL_QA.md` document the remaining form-specific visual samples. Completed checkpoints are recorded in `CHECKPOINTS.json`.

## Source-layer inventory and count definitions

`SOURCE_LAYER_COUNTS.tsv` has 92 rows generated by `scripts/count_source_layers.py` from the 243 original units in each language. It reports three distinct measurements with their scope: source lines containing a literal string, exact lexical control-word occurrences, and all literal occurrences. Complete-unit measurements include preambles and comments; body measurements exclude text outside `\begin{document}` and `\end{document}`; the comment-free body also removes unescaped TeX comments. No macro is executed by this inventory.

All six supplied French inventory figures are reproduced exactly by counting **complete-unit source lines containing the literal string**, once per matching line. The English units yield the same matching-line counts:

| Literal string | Matching source lines |
|---|---:|
| `\printedpage` | 1,419 |
| `\msp` | 2,266 |
| `\footnote` | 1,432 |
| `\texttt{[` | 818 |
| `% [sic]` | 899 |
| `% ??` | 20 |

These literal strings can be prefixes of longer control words, and several occurrences can share a line. The exact-control-word counts expose those two effects:

| Exact control word | Complete units | Document body | Body without comments |
|---|---:|---:|---:|
| `\printedpage` | 1,419 | 1,176 | 1,176 |
| `\msp` | 2,265 | 2,022 | 2,022 |
| `\mspin` | 2 | 1 | 1 |
| `\footnote` | 776 | 775 | 773 |
| `\footnotetext` | 113 | 113 | 111 |
| `\footnotemark` | 98 | 97 | 95 |
| `\footnotesize` | 543 | 54 | 54 |

The raw literal `\footnote` prefix has **1,530 occurrences = 776 + 113 + 98 + 543**, on the 1,432 matching lines. The raw `\msp` prefix has 2,267 occurrences, comprising 2,265 exact `\msp` tokens and two `\mspin` tokens, on 2,266 matching lines. There are 931 raw literal `\texttt{[` occurrences on 818 lines, and 902 literal `% [sic]` occurrences on 899 lines. These are lexical measurements. They do not supply a semantic footnote or editorial-note count.

The actual source-body anchor sequence contains **1,176 edition anchors, 2,022 `\msp` anchors and one `\mspin` anchor**, or 3,199 anchors per language. The source/projection audit proves preservation of this sequence, its arguments and its order. Author-footnote preservation is established by the independent ownership and projection replay, including the interleaved Chapter VI diagram and signed material; it does not follow from a prefix count.


## Rights and complete repository credits

All six current front matters were checked directly against `repo/README.md` and `repo/RIGHTS_NOTICE.md`. Each contains its required rights paragraph **verbatim** in the correct language. The front-matter text occurs exactly in the emitted standalone source. The English forms contain the exact requested credit “translated by GPT-6.1 Sol (OpenAI, effort max).” All six carry “AI-transcribed”, “AI-translated”, and “AI-produced corrections”; the prohibited alternative credit phrase is absent from all six complete sources and compiled PDF text.

The contributor/role comparison covers Grothendieck; the three edition editors and their ownership of deciphering and notes; Claude Opus 5.5’s transcription, integration, edition comparisons, English prompt/checks/fixes/completeness/book; GPT-6 Astra’s companion, register, corrections and raw research answers; Claude Fable 5.2’s reviewed-answer contributions and raw-answer reviews; both glossary contributors; and GPT-6 Astra’s OpenAI/ChatGPT Pro build credit. The reviewed-answer counts—eight blocks, seven paragraphs, nineteen register rows, and three bibliography entries—are retained in both languages.

For each language, the credits/rights page has identical extracted text **and identical rendered pixels** across its three forms. The visually reviewed diplomatic credits page therefore also verifies the rendering of the identical apparatus and reading credits pages. `PACKAGING_CREDITS_VALIDATION.json` contains the six front hashes, exact rights-paragraph hashes, PDF hashes, role list, and rendering-equality results. No credit or rights source was edited in this audit.

## Privacy and packaging selection

A scan of the substantive records, reader sources, companion sources, and decision fixtures found no private machine paths or e-mail addresses. Full extracted text and PDF metadata of all six successfully compiled reader PDFs and the companion likewise produced zero such matches. `PACKAGING_PDF_PRIVACY.json` identifies the exact six final reader PDF hashes that were scanned. All match the completed compile records; the files were unchanged throughout extraction and rendering checks. The original address placeholders remain redacted. Portable interpreter shebangs and standard TeX installation paths in executable build scripts are implementation dependencies, not copied private source paths.

Raw compiler logs beside the reader PDFs do contain machine paths. They must remain outside the final archive selection; sanitized equivalents are already under `records/build/`. The parent packager explicitly excludes raw reader `.aux`, `.out`, `.toc`, and `.log` files and all Python cache files. Those working build intermediates remain outside the archive whitelist.

With the parent’s authorization, six stale preview/debug records were moved out of the delivery tree: both records for each of `DER_FR_corrige_apparat_preview`, `DER_FR_texte_de_lecture_preview`, and `DER_FR_glyph_debug`. The final output tree therefore does not present those failed/intermediate diagnostics as final compilation evidence.

## Reproducibility dependencies

All data dependencies are either in the three supplied archives or in the packaged records. The French part-to-unit mapping uses the supplied corrected-part headers; corrections themselves address the original transcription. English conventions additionally use the supplied `terms_DER.txt`. The reader builder’s local `reader_support.py` module is packaged. The standalone readers compile from their own single TeX files using the documented standard TeX packages and fonts.

The scripts expect the documented workspace layout, with the archives extracted under `work/fr`, `work/en`, and `work/comp` and the delivered files under `output/`. The final ZIPs preserve that `output/` prefix. A standard complete LuaLaTeX installation avoids dependence on the temporary local TeX recovery directory. Exact PDF bytes can vary across TeX/font versions; source and decision hashes provide the reproducible textual identity.

The large change-log fields are valid TSV but exceed Python’s default CSV field limit. Consumers using Python’s CSV reader must raise `csv.field_size_limit` before loading them; the README documents this.

## Focused margin-layout audit

`scripts/scan_margin_layout.py` scans the text geometry of all six PDFs only after their hashes match successful compile records. It recognizes edition and manuscript labels in the right margin, then reports intersections with another label or nonlabel text above a small positive tolerance: area at least 1 square point, width at least 0.25 point, and height at least 0.5 point. It does not compare ordinary mathematical glyphs with each other. Font ascent/descent rectangles can intersect while the printed ink remains separate, so every candidate is reviewed from a rendered crop.

The full final scan covers **5,774 physical pages** and **19,196 recognized margin labels**. It reports **30 candidates at 21 file/page locations**: twelve parts of a single wrapped label, nine visibly separated label pairs, and nine visibly separated body-text/label pairs. Every final candidate was freshly rendered and reviewed. `MARGIN_LAYOUT_AUDIT.json` reports `status: pass`, 18 candidates with no visible collision, twelve parts of their own label, zero confirmed collisions, and zero unreviewed candidates. The exact-PDF-bound decisions are retained in `MARGIN_LAYOUT_REVIEW.json`.

The initial scan had identified two genuine collision locations. In French reading physical page 603, the comma after `W(1,2,3,6,7,8)` crossed the gray `p` of edition label `p. 58`; in English diplomatic physical page 438, the final `X_0` and closing parenthesis in the smoothness equivalence crossed manuscript label `[page 152]`. The two unit-scoped placement rules now give the formerly colliding labels positive horizontal body-text-box clearances of **2.762 and 2.890 PDF points**, respectively. All six affected instances across the three forms were rendered and are clear. `MARGIN_LAYOUT_AUDIT.md` gives every affected physical page, position and measured clearance.

The earlier Chapter II edition-page-61/manuscript-page-98 collision is absent in all six forms. Their label rectangles have a positive vertical gap of **1.215–1.216 PDF points** and a clear ink gap. The boxed-source manuscript page 39 is also in the right margin, with no candidate intersection. Fresh final renderings were inspected for all twelve of those file/page locations. The separate before/after geometry comparison records the narrowly bounded effect of the two final label placements.

## Validation scope and archive integrity

The complete source and plan checks preserve all original unit hashes, source intervals, editorial text, anchors, and apparatus provenance. The French whole-unit audit reports 243 units and 965 parsed editorial-note spans unchanged. The independent editorial-ownership audit covers both annotated masters, signed material outside brackets, the Chapter VI interleaved author/editor diagram, and retained author material inside the signed footnote. Its source/projection checks pass with zero differences.

Several checks address separate risks. Balanced braces and dollar parity alone do not detect an ungrouped repeated subscript; final LuaLaTeX compilation exposed that issue, and an explicit repeated-script check now supplements French validation. Reader replay through a shared parser is supplemented by an independent ownership audit. A successful compile and a font-box intersection scan alone cannot establish visual clearance; the margin candidate renders identified the two placement defects described above.

The full final reader validation accounts for all 1,879 correction rows, agrees with every final standalone source/PDF hash, and reports zero issues. The six-reader rights/credits/privacy refresh passes against those same PDF bytes. The complete nine-PDF delivery validation additionally checks the companion, masters, apparatus links, PDF metadata and link URIs, and the master/diplomatic text-and-geometry identities. Its results and the final archive evidence are recorded by `DELIVERY_VALIDATION.json`, `DELIVERY_MANIFEST.tsv`, and the external archive receipt.

The packaging scripts retain the documented output layout and exclude raw compiler auxiliaries, previews, caches and stale build passes. Sanitized current-pass logs remain deliverable. The manifest excludes its own row; the external receipt records the completed archive hashes. The packager reopens each ZIP and verifies every member's byte count, SHA-256, CRC, unique path and deterministic timestamp, and enforces the requested size bound. It refuses a changed payload after final validation. This packaging audit has no unresolved source, correction, rights, privacy, reproducibility or margin-layout finding.
