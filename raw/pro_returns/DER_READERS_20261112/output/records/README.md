# Les Dérivateurs: six readers, annotated masters, and the companion appendix

Alexander Grothendieck, *Les Dérivateurs* (1990–1991), from the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis. Reader construction, apparatus, appendix assembly, and the present audit: **GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026**.

This release contains the French and English texts in diplomatic, corrected-with-apparatus, and plain-reading forms. Each language has one annotated master from which its three standalone readers are emitted. The records account for all **1,879** supplied `edition_slip_kept` correction rows and all **223** supplied convention entries. The final plans contain **1,982 French variants** and **1,623 English variants**. The companion includes a chapter covering all **12** entries in `NEW_RESULTS.md`, preserving the supplied statements, available proofs, attribution, and recorded limitations.

**Release assembly status: complete.** The six readers, both annotated masters, and integrated companion have compiled successfully. The correction plans, exact source projections, and final PDF associations pass their recorded checks. The release includes all nine PDFs. Each audit below identifies the source or artifact it checks and the evidence for its result.

This is the authoritative README at `output/records/README.md`. The copies at the root of the three delivery ZIPs contain the same release description. All paths below are relative to the common extraction directory unless an archive member is explicitly named.

## 1. Delivery layout

Extract the three delivery ZIPs into the same directory, preserving their `output/` prefix. For a complete rebuild from the original inputs, put the three original source ZIPs in a sibling `upload/` directory. The verification script creates `work/fr/`, `work/en/`, and `work/comp/`.

| Delivery ZIP | Principal contents |
|---|---|
| `DER_READERS_FR.zip` | `output/FR/`: three French standalone `.tex` readers and their PDFs; the French annotated master and its compiled default-form PDF; a root copy of this README |
| `DER_READERS_EN.zip` | `output/EN/`: three English standalone `.tex` readers and their PDFs; the English annotated master and its compiled default-form PDF; a root copy of this README |
| `DER_READERS_RECORDS.zip` | `output/records/`: change logs, correction plans, decisions, validation reports, sanitized build logs, and scripts; `output/companion/`: the appendix, integrated companion sources, bibliography, style, and rebuilt PDF; a root copy of this README |

The final payload inventory is `output/records/DELIVERY_MANIFEST.tsv`; the source, PDF, and privacy checks are in `output/records/DELIVERY_VALIDATION.json`. **All nine PDFs are included; no PDF is omitted.** The packager enforces a strict 100,000,000-byte limit for each ZIP and reopens each archive to verify its member list, byte counts, SHA-256 values, and ZIP CRCs. The archive sizes and complete archive hashes are reported in the external `DER_READERS_ARCHIVES.json` receipt and with the final delivery. That receipt remains outside the three ZIPs to avoid a circular archive hash.

### Readers and masters

| Standalone source | Language and form |
|---|---|
| `output/FR/DER_FR_diplomatique.tex` | French diplomatic text: the transcribed printed readings, including retained slips and editorial notes |
| `output/FR/DER_FR_corrige_apparat.tex` | Corrected French with one linked marker and one register entry for each adopted variant |
| `output/FR/DER_FR_texte_de_lecture.tex` | Corrected French with the logged editorial omissions, neutral lacuna signs, and no correction apparatus |
| `output/EN/DER_EN_diplomatic.tex` | The supplied published English translation, with common composition repairs |
| `output/EN/DER_EN_corrected_apparatus.tex` | Corrected English with the French corrections that affect the translation and the adopted English convention changes |
| `output/EN/DER_EN_reading.tex` | Corrected English with the same reading-text policy as the French |

`output/FR/DER_FR_annotated_master.tex` and `output/EN/DER_EN_annotated_master.tex` are self-contained LuaLaTeX masters. `\DERform` selects `0` for diplomatic, `1` for corrected with apparatus, and `2` for plain reading. The default is `0`; a PDF bearing an annotated master's stem therefore represents its default diplomatic projection. Each standalone reader is also a single LaTeX file and does not need the original unit files for compilation.

### Companion

`output/companion/appendix_new_results.tex` is the new chapter. `LesDerivateurs_companion.tex` inputs it before the bibliography. The directory also contains `LesDerivateurs_companion.pdf`, the `.bib` and generated `.bbl`, `derivateurs_companion.sty`, `OVERLAPS.md`, and the supplied `parts/` files. The companion's **64 part and definition files remain byte-identical** to their supplied versions. Its master gains the appendix input, a quotation-glyph alias, and fitting hooks for oversized diagrams; seven bibliography entries provide references used by the supplied material or the appendix. The existing companion overlap policy remains documented by its supplied `OVERLAPS.md`. Evidence: `APPENDIX_COMPILE_STATUS.json` and `APPENDIX_QA.md`.

## 2. Sources and verification

The source of record is the French transcription at commit **f42cfdd**, release **v2026-11-11b**, and the supplied English `translation/` units. Both have **243 units**, covering **1,176 edition pages**. The 32 corrected French parts are supporting input; the build applies exact edits to the unchanged transcription units. It does not substitute those corrected parts for the source of record.

The input verifier checked every manifest-listed member for both byte length and SHA-256 before extraction. It records archive-relative paths and deliberately omits the manifests' original local-path column.

| Original input archive | Verified members | SHA-256 |
|---|---:|---|
| `DER_01_french_transcription.zip` | 341 | `13c6ef40618170a95610a6244993b6991c1932b64e9b04b712e1dbdce6ecf3bb` |
| `DER_02_english_translation.zip` | 289 | `d64e21847bb7f6627fd107d91080a2f1ef48dd066b53b503500d11238b9afdf8` |
| `DER_03_companion_newresults_conventions.zip` | 91 | `b1c3a262a89734a07e92ab0d7ffbb487ccdfafacff60a5b1e0d74631febc4068` |
| **Total** | **721** | Individual member evidence: `MANIFEST_VERIFIED.tsv` |

### Reconciliation of the supplied source-layer inventory

`SOURCE_LAYER_COUNTS.tsv` reproduces all six supplied French inventory figures from the 243 complete unit files. For a literal prefix, it counts each pair **(unit, source-line number)** once when that line contains the prefix, including preambles and comments. Repeated occurrences on one line contribute one matching line. The same procedure gives the same six figures for the paired English units.

| Literal prefix or marker | Matching source lines | Literal occurrences in complete units |
|---|---:|---:|
| `\printedpage` | 1,419 | 1,419 |
| `\msp` | 2,266 | 2,267 |
| `\footnote` | 1,432 | 1,530 |
| `\texttt{[` | 818 | 931 |
| `% [sic]` | 899 | 902 |
| `% ??` | 20 | 20 |

The TSV also counts exact TeX control words and repeats the measurement on document bodies with and without comments. The 1,530 complete-unit occurrences of the `\footnote` prefix comprise **776 `\footnote` + 113 `\footnotetext` + 98 `\footnotemark` + 543 `\footnotesize`** tokens. Their uncommented-body counts are respectively **773, 111, 95, and 54**. The exact `\printedpage` body count is 1,176 after the 243 local definitions are excluded. The manuscript-body commands are 2,022 `\msp` plus one `\mspin`. These explicit token and scope definitions account for the source inventories; preservation of author footnotes and editorial ownership is checked by exact source/projection replay and the logged omission operations in section 5.

`INPUT_ARCHIVES.json` gives the archive byte counts and hashes. The French source already incorporates the recorded transcription corrections and resolved doubts, subject to the five overrulings in `transcription/DECISIONS.md` and `.json`. The English units already incorporate the **41 fixes** recorded in their supplied `checks/FIXES.jsonl`. These are the starting texts, so those earlier fixes are not applied a second time.

The supplied completeness ledger contains **50** reviewed English items: **26 fixed** and **24 retained with reasons**. Its retained items comprise the editors' AQT glosses, source illegibility, and journal names. The supplied English README reports the scope and measured limitations of that comparison. This build preserves that provenance; it does not claim a new independent literary review of every sentence. Source references: ZIP 2 `COMPLETENESS_20261112.csv`, `checks/`, and `README.md`.

## 3. How the three forms are generated

`scripts/build_readers.py` reads one exact-offset change plan for each language. An edit contains the source unit, start and end offsets, exact original `before` string, replacement `after` string, source-row identifiers, location, and reason. Offsets count Python Unicode characters in the **original unchanged unit**, before correction or composition repair. The builder checks the source slice and rejects overlapping or identity variants.

The annotated master stores the source hash, the privacy-cleaned original source, every variant, and the three projections of each unit in a canonical JSON payload. A generated Lua table holds the same projection pieces for direct compilation. The standalone files are emitted from those master pieces. The validation compares the Lua table with the JSON representation, compares each emitted reader with its master projection, and compares the master's variants with the current final plan. The standalone files are never maintained as three independent edited texts.

Unit-local definitions remain scoped to their unit. The shared preamble supplies packages, fonts, page-margin commands, and the apparatus commands. The supplied English reader's definition adapter is included as `scripts/reader_support.py`; it handles local definitions when assembling complete source documents into one book. Common assembly transformations and their before/after contexts are recorded in `CHANGES_FR.tsv` and `CHANGES_EN.tsv`.

In the apparatus form, each variant receives one `FRV…` or `ENV…` marker linked to one register item. Markers are placed at a complete TeX-block boundary so that inserting a marker cannot split a formula, alignment, or diagram. The register supplies the precise source locus. A preamble-definition change has one entry associated with the unit opening and applies to that definition's uses in the unit. Printed and corrected readings are quoted as literal LaTeX, preserving identification of local macros and symbols.

The diplomatic and reading forms have **zero apparatus entries**. Reading-text omissions and repairs shared by all three forms have separate records; they do not create correction-apparatus entries. `APPARATUS_COUNTS.md` gives the counts per chapter, kind, and form.

## 4. Correction and convention accounting

### French source rows

All **1,879** `edition_slip_kept` rows have a terminal decision, with no unresolved or partial rows:

| Row outcome | Count | Meaning in this build |
|---|---:|---|
| `applied` | 1,707 | The row contributes one or more actual source changes |
| `merged` | 79 | The same source place and correction is already represented; its provenance is retained on the shared variant |
| `no_change` | 64 | The reviewed row produces no new source variant; the reason is recorded |
| `rejected` | 29 | The proposed amendment is not adopted; the source reading and reason remain in the decision table |
| **Total** | **1,879** | Complete source-row coverage |

These rows yield **1,982 actual French variants**. A row can specify several disjoint changes, and repeated rows can share a variant; source-row counts and apparatus-entry counts therefore have separate definitions. `CORRECTIONS_DECIDED.tsv` contains **95 decisions**: the 64 no-change cases, 29 rejected proposals, and two adopted corrections with an explicit additional decision. The complete row-to-variant mapping is in `FR_CORRECTION_COVERAGE.tsv`; per-part totals are in `FR_CORRECTION_COUNTS.tsv`.

### English transfer

Every French variant has an English transfer outcome. Of **1,982** transfer records, **1,464** apply a change and **518** have no additional English effect. These outcomes include French spelling or agreement repairs already expressed correctly in English. Across the original **1,879 source rows**, **1,253** have an applied English effect and **626** have no additional effect. Duplicate or nested effects are composed into one nonoverlapping English variant with all contributing provenance retained.

The final English plan has **1,623 variants**: **1,388 edition-slip**, **226 typesetting**, and **9 glossary** variants. `EN_TRANSFER_AUDIT.tsv` and `.json` connect every French variant to its English result. `EN_SOURCE_ROW_AUDIT.tsv` accounts for every original correction row. `EN_TRANSFER_DECISIONS.json` supplies **1,070 explicit source-row decisions** for replay; it is a required input, not an optional explanatory file.

### Conventions

The audit covers **171 glossary**, **26 notation**, and **26 typesetting** entries, for **223** entries in all. `CONVENTIONS_AUDIT.tsv` records each entry's disposition, evidence, and affected final identifiers. `GLOSSARY_FLAGGED.tsv` contains **17 entries** whose proposed global treatment was not adopted, with a reason and proposed source-preserving rendering. Several are notation or typesetting entries; the requested filename covers the whole supplied convention audit.

The adopted convention pass contributes **237 exact edits before composition**: nine glossary changes and 228 typesetting changes. Two typesetting changes are contained in larger transferred edition-slip changes, so their provenance is retained in those larger final entries. Examples of adopted changes are the supplied rendering of *système projectif*, the specified rendering of *limites inductives filtrantes*, later repetitions of the English `(gear)` gloss after the first book-wide occurrence of *fourbi*, documented calligraphic-X encoding, and roman `def` abbreviations. Chapter-specific letters, opposite-category glyphs, arrow lengths, inequality signs, and macro meanings remain governed by their source occurrences and documented corrections.

The **59 bold-Delta encoding repairs** use `\boldsymbol{\Delta}` where the requested LuaLaTeX build otherwise lost the intended glyph. They are common composition repairs in all forms, recorded outside the variant apparatus. Their supplied evidence is `conventions/TYPESETTING.csv:2` and `companion_corrections/DER_I-a_corrections.csv:1`.

### Change-log scope

`CHANGES_FR.tsv` and `CHANGES_EN.tsv` use the requested columns `page`, `place`, `before`, `after`, `source`. They include actual variants, common repairs, and the documented assembly differences needed to turn complete unit documents into one reader, including the shared preamble, front matter, chapter boundaries, and the apparatus register. Their total row counts therefore exceed the number of correction entries. Source IDs beginning `BUILD-` identify composition or assembly records; `FRV…` and `ENV…` identify apparatus variants.

The TSVs are UTF-8 tables with standard CSV quoting and a tab delimiter. Before/after fields can contain literal newlines, so use a table reader rather than counting physical lines. Some complete assembly fields exceed Python's default CSV field limit; a Python consumer can set `csv.field_size_limit(100000000)` before reading the change logs.

The final change logs contain **4,511 French rows** (1,982 variants, 60 shared unit repairs, and 2,469 assembly records) and **3,872 English rows** (1,623 variants, 59 shared unit repairs, and 2,190 assembly records). Reading omissions are fully enumerated separately in `EDITORIAL_NOTES_FR.tsv` and `EDITORIAL_NOTES_EN.tsv`.

## 5. Editorial notes, author annotations, and page anchors

The Künzer–Malgoire–Maltsiniotis editorial wording remains verbatim in each language's diplomatic and corrected forms. In English, this means the supplied translation of those notes. Front matter explains their ownership and their original typewriter-bracket convention. The new apparatus has its own identifiers and register.

The plain-reading projection removes the logged editorial interventions, including reports of struck-out words, the editors' Chapter XIV afterword, the signed editor-only footnote, and isolated editorial `[?]` doubt marks. It retains the other author text and author footnotes. In Chapter XVIII note 58, the editors transmit two quotations of Grothendieck's marginal annotations: the reading text retains those author quotations and the marginal corollary while removing the surrounding editorial framing. The Chapter XIII reference sections remain, with their editorial attribution, as the reading preface states. No struck-out words that are absent from the supplied transcription have been reconstructed.

Two removals of automatically numbered editorial footnotes leave a hidden `\stepcounter{footnote}` in the reading projection. These occur in Chapter XVIII units pp. 16–20 and 91–95 and keep the following author notes numbered 19/20 and 105 as in the source. The editorial text and printed marker disappear; the counter advance preserves the source's later numbering. At Chapter VI manuscript pp. 197–198, an author triangle and the editors' alternative occupy different columns of one two-row diagram. The reading projection keeps the exact first three author cells of each row and removes the editorial columns. The whole before/after diagram is recorded, so a bracket-based omission cannot consume the author's second row.

Each language has **977 logged omission or wrapper operations**:

| Reading operation | Count per language |
|---|---:|
| Bracketed editorial notes | 910 |
| Editorial front notes | 19 |
| Editorial contents note | 1 |
| Inline page labels handled separately from running text | 9 |
| Plain editorial doubt marks | 26 |
| Empty display wrapper after editorial removal | 1 |
| Empty editorial footnote markers | 6 |
| Interleaved diagram with author cells retained | 1 |
| Chapter XIV afterword spans | 2 |
| Signed editor-only footnote | 1 |
| Editorial framing removed while author quotations remain | 1 |
| **Total** | **977** |

The 26 plain doubt marks include six source-spacing variants written as `[\,?]`, located by the spacing-aware final scan. These are recorded text operations, including wrappers and partial framing; they are not a count of independently authored editorial notes. **Eleven** operations per language leave the neutral `[…]` sign for missing or illegible text. No words are supplied at those gaps. The exact removal or retention strings appear in the omission TSVs. The independent replay in `APPENDIX_READER_NOTES_AUDIT.json` verifies the reading bodies against those records and additionally checks the signed-note and author-quotation cases.

The source-body inventory has **1,176 edition anchors** and **2,023 manuscript anchors** per language: 2,022 `\msp` invocations and one `\mspin`. Every form retains their arguments and sequence. Reading-text page numbers are marginal; repeated inline page labels are handled explicitly. These counts concern invocations in the 243 unit bodies. For example, the 1,419 `\printedpage` command occurrences in complete source units also include their 243 local definitions. A command-occurrence count and a retained-page-anchor count must be read with their stated scope. Evidence: `ANCHORS_FR.tsv`, `ANCHORS_EN.tsv`, `BUILD_FR.json`, `BUILD_EN.json`, and the per-unit validation records.

## 6. Shared composition repairs

The three known compilation defects are addressed in all reader forms. The first empty-cell diagram baseline in XIIc pp. 61–64 uses the supplied English repair; the later valid baseline remains in place. The shared preamble loads `mathtools` for the Chapter XIV `\mathllap` use. The assembled source and master loader preserve local footnote definitions without the earlier Chapter XV parameter-token failure. These changes are recorded as build behavior, with final compilation supplying the executable check.

Two unit-scoped margin-placement decisions keep a page label clear of a body overrun. In French Chapter XV unit pp. 56–60, edition label `p. 58` moves right by 6 TeX points; in English Chapter XIIb unit pp. 61–65, manuscript label `[page 152]` moves right by 20 TeX points. Each rule applies to all three forms of its language. The exact original anchor call and all body tokens remain unchanged; only the target label receives horizontal space inside its existing margin box. `MARGIN_PLACEMENTS.tsv` records the decisions and the observed pre-repair PDFs. The affected unit assembly rows in `CHANGES_FR.tsv` and `CHANGES_EN.tsv` name `BUILD-MARGIN-FR-XV-58` and `BUILD-MARGIN-EN-XIIb-152`. `MARGIN_REFINEMENT_COMPARISON.json` passes across all 7,604 reader/master pages: 7,596 pages are exactly unchanged, and exactly eight target labels move with no unexpected difference. All 68 previously reviewed full-page images have identical rendered pixels. The final margin audit reviews every one of its 30 geometry candidates and reports zero remaining collisions and zero unreviewed candidates.

The 59 bold-Delta glyph repairs described above are also shared. `CHANGES_FR.tsv` has 60 explicit unit-repair records, including the French XIIc fix; the supplied English unit already has that diagram fix, so `CHANGES_EN.tsv` has 59. Broader assembly changes, including package loading and definition scoping, are logged separately.

Edition page breaks are reflowed for a continuous book while their page anchors remain. The shared `marginfix` package stacks adjacent edition and manuscript margin labels; their anchor arguments and order remain unchanged. The single boxed-source `\mspin` label uses the retained margin-note route and is checked in the final page samples. Diagrams that exceed the available width or height are fitted to the page. This changes their display scale; the source formula and diagram tokens remain available in the single-file sources. Final box warnings and visual inspections are reported below rather than being suppressed by raising diagnostic thresholds.

## 7. The twelve-entry appendix and its evidential scope

The chapter opens with `NEW_RESULTS.md`'s own framing: the search was limited, no priority is claimed, and readers who know a reference are invited to provide it. Each of its twelve sections contains the exact inventory statement, the available cited statement and proof, manuscript bearing, the inventory's “proved by” and “checked by” attribution, and a separately labelled **GPT-6 Astra's reading**. That reading is the present editorial assessment of the supplied argument, not the later independent peer review.

`APPENDIX_VALIDATION.json` records inventory-statement hashes, extracted-source hashes, source members and locations, and the twelve provenance records. `APPENDIX_SOURCE_EXTRACTS.md` preserves the selected source text. `APPENDIX_TYPESETTING_MAP.tsv` records the mathematical glyph and script conversions used to typeset Markdown source passages. No claims from STRATA, PATHS, BISITE, or RESIDUE have been added beyond the inventory's own references.

| Entry | Subject as recorded in the supplied inventory | Source or reading limitation recorded in the appendix |
|---|---|---|
| 1 | Finite monoids, finite dimension, and bounded homology | Available source proof and its external inputs are reproduced; the inventory's unchecked status remains visible |
| 2 | Maps from finite-group classifying spaces under a cohomological bound | Available source proof and cited input are reproduced with their attribution |
| 3 | Kan–Thurston without small quotients and the ind-category statement | The source recalls the cardinal bound from memory; detailed compatible models and the limit-stage comparison are not supplied |
| 4 | Uncountably many homotopy classes of maps to the two-sphere | Available source argument is reproduced with its stated scope and dependencies |
| 5 | The thirty-four-arrow lower bound for the projective plane | Available source argument is reproduced; its provenance and unchecked status are preserved |
| 6 | The reported census of small categories | The cited programs and run directory are absent; the reported census was not rerun |
| 7 | The reversible localizer defined by two-local spheres | Compressed uses of the named external theorems are identified; the source's separate unproved accessibility speculation is not promoted to an appendix theorem |
| 8 | The two-cone counterexample to the reverse axiom | The reading identifies the gap between the inventory's word “only” and the scope actually established by the supplied arguments |
| 9 | The reported trefoil argument for failure of Loc (7 F) | The cited working note is absent; the supplied paragraph lacks the full fibre, local-system, and base-change computation |
| 10 | Totality and the fixed-origin path category | The available proof is by reference to manuscript pages 102–103 and 112; no expanded independent derivation is claimed |
| 11 | Exact colimits, total asphericity, and injective ordinals | The cited collage and affine-category inputs remain explicit, including Isbell–Mitchell (1973), Theorem 3 |
| 12 | The projective-plane counterexample for finite monoids | The cited claims-check file is absent; the available CATHOT proof and finite-group K-theory verification are reproduced |

The absent cited members are listed exactly in `APPENDIX_VALIDATION.json`: the CATHOT `work/code/` directory, its `EMAIL_CLAIMS_CHECK.md`, and the expert's `work/checks_3/own_thoughts_before_reading.md`. Their absence is part of the source record. No missing proof file or computation has been silently recreated.

The closing list retains the references the inventory identifies as known: Isbell–Mitchell (1973), Harvey (1971), and Cisinski's *Astérisque* 308, Corollary 4.2.22. Their presence records the supplied inventory's literature attribution. The validation scripts establish source and structural correspondence; they do not certify the truth or originality of all mathematical statements in the manuscript or appendix.

## 8. Compile status, diagnostics, and visual review

The final reader and master compile records are `output/records/build/<stem>.json`, with sanitized per-pass logs beside them. Each record ties the PDF to the SHA-256 of the exact source compiled and includes return codes, errors, missing glyphs, unresolved references, rerun requests, package warnings, and box diagnostics. The final `VALIDATION.json` additionally checks that reader PDF hashes and source hashes match these records and that the masters contain the final plans. `COMPILE_STATUS.tsv` is the consolidated release summary.

### Final compile summary

These are the last-pass figures from the corresponding build records. Each master row concerns its default diplomatic projection. Numbers in the “warnings” column count package/LaTeX warnings; box diagnostics have their own column. All eight reader/master builds completed in two passes. Their final passes have zero rerun requests and zero backend warnings.

| PDF stem | Pages | Passes | Errors | Missing glyphs | Undefined references/citations | Warnings | Overfull h/v boxes |
|---|---:|---:|---:|---:|---:|---:|---|
| `DER_FR_diplomatique` | 915 | 2 | 0 | 0 | 0 | 1 | 31 / 1 |
| `DER_FR_corrige_apparat` | 1,082 | 2 | 0 | 0 | 0 | 1 | 36 / 1 |
| `DER_FR_texte_de_lecture` | 899 | 2 | 0 | 0 | 0 | 1 | 27 / 1 |
| `DER_EN_diplomatic` | 915 | 2 | 0 | 0 | 0 | 1 | 29 / 0 |
| `DER_EN_corrected_apparatus` | 1,061 | 2 | 0 | 0 | 0 | 1 | 32 / 1 |
| `DER_EN_reading` | 902 | 2 | 0 | 0 | 0 | 1 | 26 / 2 |
| `DER_FR_annotated_master` | 915 | 2 | 0 | 0 | 0 | 1 | 31 / 1 |
| `DER_EN_annotated_master` | 915 | 2 | 0 | 0 | 0 | 1 | 29 / 0 |
| `LesDerivateurs_companion` | 1,906 | 4 LuaLaTeX + BibTeX | 0 | 0 | 0 | 0 | 15 / 7 |

Each reader/master has the same single package warning: `Package epstopdf Warning: Shell escape feature is not enabled.` The build deliberately disables shell escape; the final PDFs are present, and the compile records report no failed conversion or missing glyph. Box diagnostics are retained as follows.

| PDF stem | Underfull h/v boxes | Largest overfull h/v excess (pt) |
|---|---|---|
| `DER_FR_diplomatique` | 40 / 0 | 59.28604 / 0.72427 |
| `DER_FR_corrige_apparat` | 113 / 0 | 59.76820 / 1.90341 |
| `DER_FR_texte_de_lecture` | 18 / 0 | 59.76820 / 0.39241 |
| `DER_EN_diplomatic` | 30 / 0 | 61.82962 / 0.00000 |
| `DER_EN_corrected_apparatus` | 142 / 0 | 61.82962 / 1.35669 |
| `DER_EN_reading` | 11 / 0 | 61.82962 / 2.03893 |
| `DER_FR_annotated_master` | 40 / 0 | 59.28604 / 0.72427 |
| `DER_EN_annotated_master` | 30 / 0 | 61.82962 / 0.00000 |

### Delivered PDF checksums

| PDF stem | SHA-256 |
|---|---|
| `DER_FR_diplomatique` | `ea63b05972a83fa916b041dd5c85441ea6b6da0401eee5e2f27f7f0a527aa4ad` |
| `DER_FR_corrige_apparat` | `08c6e300cff88207d0a1ebda84e49284f622ef2ad4ac983a63c8b226ee10fdb1` |
| `DER_FR_texte_de_lecture` | `158d9b545a5434c61c97d2bb8c28baddd6bed31a34d5dda61c5fd2c19867a59e` |
| `DER_EN_diplomatic` | `544d3b3f84665aa0c7e29db2f43306254f648d897656ed9bd2cb590655f439d1` |
| `DER_EN_corrected_apparatus` | `30cb37db498e4decf10701ac0ff3c579282170bba3be808c577617eb71b39fd6` |
| `DER_EN_reading` | `eb43fd6b673ef04ee3403e43057ff8838a74501d39162232d3a3d117a4b97d7b` |
| `DER_FR_annotated_master` | `cd4a5d286b349ef65ab16ca4b01eb0885efaba7088b3459807e7b4264153a7df` |
| `DER_EN_annotated_master` | `bc06085d66aa1339943cda859069c8dfa0359390e7877eb870d17ccccaca151b` |
| `LesDerivateurs_companion` | `540e11219d653839893926254caaa8309dda3963a2e015a5764421b6609f7697` |

The companion status is already recorded in `APPENDIX_COMPILE_STATUS.json`: **1,906 pages**, no LaTeX errors, undefined references/citations, package warnings, or missing-glyph warnings; 15 overfull horizontal boxes, 7 overfull vertical boxes, and 27 underfull boxes. The largest reported excesses are 39.36911 pt horizontally and 5.5976 pt vertically. These box diagnostics occur in the inherited companion; the appendix has no overfull-box diagnostics. Its new chapter occupies physical PDF pages **1,862–1,882**. `APPENDIX_QA.md` describes the twenty-one-page appendix inspection and selected final-book checks.

The selected final reader pages pass the visual checks recorded in `PDF_VISUAL_QA.md`, `PDF_FR_QA.md`, `PDF_EN_QA.md`, and `PDF_DIPLOMATIC_QA.md`. Their explicit page lists include long formulas and apparatus entries, large diagrams, credits and rights, page anchors, the retained author triangle, and author footnotes. The companion report covers all twenty-one appendix pages and selected surrounding book pages. These are the recorded visual samples; they do not claim independent visual inspection of every page.

The delivery audit scans **all nine PDFs and all 9,510 pages**, together with PDF metadata, link URIs, and the complete approved text payload, and reports **zero privacy findings**. It verifies all **1,982 French and 1,623 English apparatus destinations**, each with exactly one valid inbound link whose rectangle contains its visible identifier. Both default master PDFs match their standalone diplomatic PDFs in exact extracted text, page rectangles, media/crop boxes, and rotation across all 915 pages in each language. Evidence: `DELIVERY_VALIDATION.json` and `DELIVERY_APPARATUS_LINKS.tsv`.

## 9. Reproduction

### Required software and inputs

The source-replay and construction scripts use the Python standard library. The delivery PDF audit additionally uses PyMuPDF and pypdf; rendered-page review also uses Pillow. The independent `audit_packaging_fronts.py` privacy pass uses Poppler’s `pdftotext`. The exact installed versions are recorded in `RUNTIME_VERSIONS.json`. This build used Python 3.12; Python 3.12 is the documented reproduction target. The commands below assume UTF-8 as Python's default text encoding; `python -X utf8` forces that mode on platforms with another default. No model API, account credential, or network request is required to rerun the delivered construction scripts against the supplied source ZIPs and reviewed fixtures.

Compilation requires a functioning **LuaLaTeX** installation with French and English language support, **BibTeX** for the companion, and the fonts **DejaVu Sans** and **DejaVu Sans Mono** for the apparatus. The reader preamble uses `fontspec`, `babel`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `mathrsfs`, `tikz-cd`/PGF, `enumitem`, `array`, `ragged2e`, `marginnote`, `marginfix`, `lmodern`, `geometry`, `xcolor`, `fancyhdr`, `xurl`, `adjustbox`, `hyperref`, and `luacode`. The companion additionally uses `microtype`, `etoolbox`, `needspace`, and `booktabs`, plus its bundled style. Install their normal transitive dependencies and fonts through a complete TeX distribution. The source repository recommends TeX Live 2025 or later; the completed companion's actual engine is recorded as LuaHBTeX 1.18.0 with a LuaLaTeX format and BibTeX 0.99d.

The execution workspace needed local recovery of LuaLaTeX support files, French language data, a format, and font maps. Those recovered runtime files and caches are not needed by the standalone sources on a complete TeX installation and are not promised as a portable frozen TeX distribution. `compile_books.py` detects a local recovery tree when present; its fallback tree layout is specific to the build environment. For a clean-machine reproduction, use the installed `lualatex` command and a working standard TeX configuration.

PDF hashes identify the delivered artifacts. PDF creation metadata, package versions, font versions, and engine behavior can affect binary hashes and pagination on another installation. Exact source/decision replay is validated separately; the release does not claim a pinned, byte-identical PDF environment.

### A. Verify and extract the original source ZIPs

Run all Python commands from the common directory containing `upload/` and `output/`:

```bash
python output/records/scripts/verify_inputs.py upload work output/records
python output/records/scripts/count_source_layers.py
```

The three required original archive names are the names in section 2. The delivery ZIPs provide the finished sources and records; full source verification and reconstruction also require those original input ZIPs.

### B. Replay the reviewed correction decisions

```bash
python output/records/scripts/resolve_french.py
python output/records/scripts/validate_french_plan.py
python output/records/scripts/resolve_english.py
python output/records/scripts/audit_english_plan.py
```

French decision fixtures are included in `output/records/decisions/source/french/`. Their `MANIFEST.json` gives hashes and byte counts; `README.txt` gives precedence. The resolver reads `manual.json`, then `manual_*.json` in lexical order, with later entries overriding earlier decisions for the same row. It uses the packaged fixtures on a fresh build. An existing `work/corrections_fr/manual.json` selects the development fixture directory instead, so use a clean `work/` tree to reproduce the delivered fixtures.

The English resolver's **default** command builds the complete combined plan from `EN_TRANSFER_DECISIONS.json`, the French plan, the original paired units, the convention tables, and ZIP 2 `scripts/terms_DER.txt`. Its `--conventions-only` mode is a diagnostic mode and does not reproduce the final combined plan. `transfer_english.py` alone writes a provisional transfer result; use `resolve_english.py` for the deliverable plan.

Final plan hashes:

| Plan | SHA-256 |
|---|---|
| `FR_CORRECTION_PLAN.json` | `646e450030a3f36d27b9cb3c649f347ffeb0fcccbc0ba4f0f80ff78916fd0c92` |
| `EN_CHANGE_PLAN.json` | `dd3d0e7db9d7110cb9b4639ddf476eb75a7904d68a76936ab7cb4af35e423666` |

### C. Build both annotated masters and all six sources

```bash
python output/records/scripts/build_readers.py --language both
python output/records/scripts/validate_readers.py --sources-only
python output/records/scripts/build_appendix_reader_audit.py
```

To emit the three flat readers again from an existing master without rerunning the source decision stage:

```bash
python output/records/scripts/build_readers.py --emit output/FR/DER_FR_annotated_master.tex
python output/records/scripts/build_readers.py --emit output/EN/DER_EN_annotated_master.tex
```

Keep the bundled script files together under `output/records/scripts/`; several scripts derive the common root from that location. Both direct master compilation and direct reader compilation should run in the file's own directory. The master loader opens its canonical master filename, so keep that filename unchanged.

### D. Compile and validate the readers

```bash
python output/records/scripts/compile_books.py --passes 4 \
  output/FR/DER_FR_diplomatique.tex \
  output/FR/DER_FR_corrige_apparat.tex \
  output/FR/DER_FR_texte_de_lecture.tex \
  output/EN/DER_EN_diplomatic.tex \
  output/EN/DER_EN_corrected_apparatus.tex \
  output/EN/DER_EN_reading.tex \
  output/FR/DER_FR_annotated_master.tex \
  output/EN/DER_EN_annotated_master.tex

python output/records/scripts/validate_readers.py
python output/records/scripts/build_appendix_reader_audit.py
```

The compile wrapper uses `lualatex` with shell escape disabled and halts on a TeX error. It performs up to the requested number of passes, stopping after at least two successful passes when references and outlines no longer request a rerun. The final validation checks the current final plans against the masters and the source/PDF hashes against the compile records. `--sources-only` is useful before compilation but is not the final PDF validation command.

For direct selection of another master projection, for example the French apparatus form, run from `output/FR/`:

```bash
lualatex --no-shell-escape -interaction=nonstopmode -halt-on-error \
  -jobname=DER_FR_master_apparatus \
  '\def\DERform{1}\input{DER_FR_annotated_master.tex}'
```

Repeat the direct engine command until its references settle. The emitted standalone sources are the simpler entry points for the six named delivery PDFs. `check_chapter_compilation.py FR` and `check_chapter_compilation.py EN` provide optional chapter-level diagnostics; their temporary PDFs are not substitutes for the complete books.

### E. Rebuild the appendix and integrated companion

```bash
python output/records/scripts/build_appendix.py \
  --source work/comp --output output/companion --records output/records

python output/records/scripts/build_appendix_compile.py \
  --companion output/companion --records output/records
```

The companion compile wrapper performs four LuaLaTeX passes with BibTeX after the first pass. It also accepts `--engine` and `--format` for an installation exposing a LuaTeX binary and a separate LaTeX format. A fresh wrapper run writes `APPENDIX_REBUILD_STATUS.json`; the delivered build's richer provenance and visual-review status are in `APPENDIX_COMPILE_STATUS.json` and `APPENDIX_QA.md`.

### F. Final delivery verification and packaging

Run after the complete PDF builds and visual review:

```bash
python output/records/scripts/validate_delivery.py
python output/records/scripts/package_deliverables.py
```

The validator checks the final source/PDF associations, all apparatus destinations and their visible inbound links, exact default-master PDF text and page geometry, and privacy across every payload text file and every PDF page. It writes `COMPILE_STATUS.tsv`, the final `DELIVERY_VALIDATION` reports, `DELIVERY_APPARATUS_LINKS.tsv`, and `DELIVERY_MANIFEST.tsv`. The packager preserves the `output/` layout and includes the reviewed fixtures and scripts. It excludes auxiliary files and temporary previews, creates the three ZIPs below 100 MB each, then reopens them to verify every byte count, SHA-256, and ZIP CRC. Its outer archive receipt is `deliverables/DER_READERS_ARCHIVES.json`; it stays outside the ZIPs to avoid a circular self-hash.

`scan_margin_layout.py` records the full six-reader text-label geometry and identifies candidates for visual review. `audit_packaging_fronts.py` reproduces the six-front exact rights/credits, rendered equality, and independent PDF privacy checks. `compare_margin_refinement.py` compares the final reader/master PDFs with the preserved preceding PDFs and reproduces the two-label placement audit; its baseline is the PDF set preserved in checkpoint 7, arranged under the baseline directory documented by its command-line help. These supplementary audits record the exact PDF hashes they inspect.

Replaying the historical margin-refinement comparison additionally requires the eight preceding PDFs and their matching compile JSON files, preserved in [DER_READERS_checkpoint_7.zip](https://chatgpt.com/library?file_id=libfile_c9d265d591048191b6ebd30300e07479&account_id=personal). Extract that checkpoint separately, then copy its four `FR/*.pdf` files, four `EN/*.pdf` files, and eight corresponding `records/build/DER_*.json` files into the flat directory `work/pre_margin_refinement/`. Run `python output/records/scripts/compare_margin_refinement.py --baseline work/pre_margin_refinement --jobs 2`. The report records every required baseline hash. The standard source rebuild described above uses the three original source ZIPs and packaged decisions.

`render_pdf_qa.py` reproduces the selected-page PNGs used for visual review. For example, pass a reader PDF followed by `--pages 1 3 245 753`. Its generated images and contact sheet remain temporary review files.

`checkpoint.py` can preserve an explicitly completed subset during a long build. It accepts a checkpoint number and completed reader stems, verifies their compile records, and creates `DER_READERS_checkpoint_<n>.zip`. `CHECKPOINTS.json` records the saved checkpoints. A checkpoint's status applies only to the reader stems it lists; the final validation and delivery records supersede its intermediate state.

## 10. Record map

| Record | Purpose |
|---|---|
| `MANIFEST_VERIFIED.tsv`, `INPUT_ARCHIVES.json` | Original input verification without private original paths |
| `SOURCE_LAYER_COUNTS.tsv`, `scripts/count_source_layers.py` | Supplied matching-line inventory, literal occurrences, exact control words, and document-body counts |
| `FR_CORRECTION_PLAN.json`, `EN_CHANGE_PLAN.json` | Exact original-offset variants with source provenance |
| `FR_CORRECTION_COVERAGE.tsv`, `FR_CORRECTION_COUNTS.tsv` | Every French source-row decision and per-part totals |
| `CORRECTIONS_DECIDED.tsv` | No-change, rejected, and explicitly qualified adopted decisions |
| `decisions/source/french/`, `EN_TRANSFER_DECISIONS.json` | Reviewed reproducibility inputs |
| `EN_TRANSFER_AUDIT.tsv` / `.json`, `EN_SOURCE_ROW_AUDIT.tsv` | Every French-variant and original-row English outcome |
| `EN_CONVENTIONS_PLAN.json`, `CONVENTIONS_AUDIT.tsv` | The complete convention pass and its row-by-row audit |
| `GLOSSARY_FLAGGED.tsv`, `EN_CONVENTIONS_PROTECTED.tsv` | Flagged convention entries and protected candidates |
| `CHANGES_FR.tsv`, `CHANGES_EN.tsv` | Variants, shared repairs, and assembly differences |
| `EDITORIAL_NOTES_FR.tsv`, `EDITORIAL_NOTES_EN.tsv` | Exact reading-text omission and retention operations |
| `ANCHORS_FR.tsv`, `ANCHORS_EN.tsv` | Per-unit anchor counts, sequence hashes, and agreement across forms |
| `MARGIN_PLACEMENTS.tsv`, `MARGIN_LAYOUT_AUDIT.json`, `MARGIN_LAYOUT_REVIEW.json`, `MARGIN_REFINEMENT_COMPARISON.json` | Two local label-placement decisions, complete reader margin scan, and before/after PDF comparison |
| `BUILD_FR.json`, `BUILD_EN.json`, `APPARATUS_COUNTS.md` | Build inventories and per-chapter/form counts |
| `FR_CORRECTION_VALIDATION.json`, `EN_PLAN_VALIDATION.json` | Plan provenance, source offsets, protected text, and structural checks |
| `VALIDATION_FR.json`, `VALIDATION_EN.json`, `VALIDATION.json` | Current-master/reader/plan correspondence and final compilation associations |
| `APPENDIX_READER_NOTES_AUDIT.json` | Independent exact-body and omission-record replay for both languages |
| `APPENDIX_VALIDATION.json`, `APPENDIX_SOURCE_EXTRACTS.md`, `APPENDIX_TYPESETTING_MAP.tsv` | Appendix statement/source/provenance and typography evidence |
| `APPENDIX_COMPILE_STATUS.json`, `APPENDIX_QA.md`, `APPENDIX_*` logs | Delivered companion compilation and recorded visual inspection |
| `build/`, `COMPILE_STATUS.tsv`, `PDF_VISUAL_QA.md`, `PDF_FR_QA.md`, `PDF_EN_QA.md`, `PDF_DIPLOMATIC_QA.md` | Final reader/master diagnostics and visual-review records |
| `DELIVERY_MANIFEST.tsv`, `DELIVERY_VALIDATION.json` | Final package inventory, file hashes, size, and privacy checks |
| `scripts/` | Verification, resolution, construction, compilation, audit, and packaging programs |

## 11. Credits, rights, and privacy

The following credits come from ZIP 1 `repo/README.md` and `repo/RIGHTS_NOTICE.md`, with the English provenance also documented by ZIP 2 `README.md`:

- **Author:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991).
- **Edition transcribed:** M. Künzer, J. Malgoire and G. Maltsiniotis, Universités de Montpellier II et Paris VII. The deciphering, edition, and editors' notes are theirs. The edition's page is <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>.
- **Transcription:** AI-transcribed by Claude Opus 5.5 (Anthropic).
- **Companion commentary, claim register, and corrections:** AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checked and integrated by Claude Opus 5.5 (Anthropic).
- **Commentary from reviewed answers:** eight commentary blocks in II-a, III–V, and XIIb-a, seven paragraphs of other blocks, nineteen claim-register rows, and three bibliography entries were AI-produced by Claude Fable 5.2 (Anthropic) from GPT-6 Astra answers that it reviewed. The relevant records identify the answer and reviewer.
- **Earlier transcription corrections:** the companion corrections above; macro-definition corrections and changes absent from the tables were compared with the edition pages by Claude Opus 5.5, as recorded in `transcription/DECISIONS.md`.
- **English:** AI-translated; **translated by GPT-6.1 Sol (OpenAI, effort max)**. Glossary by Claude Fable 5.2 and Claude Opus 5.5; prompt, checks, fixes, completeness comparison, and the published English book by Claude Opus 5.5 (Anthropic).
- **Raw research outputs:** answers AI-produced by GPT-6 Astra; reviews by Claude Fable 5.2, with the individual source attributions preserved.
- **This build:** GPT-6 Astra (OpenAI, ChatGPT Pro mode). The present work includes reader construction, AI-produced corrections and apparatus, the documented audits, and appendix assembly. The appendix retains each source's separate “proved by” and “checked by” credit.

Each reader carries the required credit and rights statement in its own language. The English rights statement is reproduced here from the supplied notice:

> The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.

The French text in that notice is:

> Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Là où nous détenons des droits, sur la transcription, la traduction, les corrections et la composition produites par IA, ils sont dédiés au domaine public sous CC0 1.0. Cette édition est publiée à des fins pédagogiques et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, ouvrez une issue sur GitHub et nous la retirerons.

Editors' addresses remain `[e-mail address removed]`. Delivered readers, source payloads, and records use archive-relative references; personal and execution-local paths are removed from delivered text and sanitized logs. Raw source manifests with their original-path column and raw runtime logs are not copied into the release records. The final delivery privacy report identifies the inspected payload and PDF-text scope.
