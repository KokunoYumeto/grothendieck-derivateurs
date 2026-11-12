# Final PDF visual and delivery checks

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026.

This record brings together the final page-image inspections and the automated source/PDF checks. Visual observations apply to the pages listed in the reports below. Full-document checks state their own measured scope. Physical page numbers count from the first PDF page, including the title page.

## Final artifacts and compile results

| PDF | Pages | Final-pass errors | Missing glyphs | Unresolved references | Package warnings |
|---|---:|---:|---:|---:|---:|
| French diplomatic | 915 | 0 | 0 | 0 | 1 |
| French corrected with apparatus | 1,082 | 0 | 0 | 0 | 1 |
| French reading | 899 | 0 | 0 | 0 | 1 |
| English diplomatic | 915 | 0 | 0 | 0 | 1 |
| English corrected with apparatus | 1,061 | 0 | 0 | 0 | 1 |
| English reading | 902 | 0 | 0 | 0 | 1 |
| French annotated master, default projection | 915 | 0 | 0 | 0 | 1 |
| English annotated master, default projection | 915 | 0 | 0 | 0 | 1 |
| Integrated companion | 1,906 | 0 | 0 | 0 | 0 |

The reader/master warning is the recorded `epstopdf` notice that shell escape is disabled. Their final passes have zero rerun requests and zero backend warnings. The exact source/PDF hashes and full box diagnostics are in `COMPILE_STATUS.tsv`, the per-book build JSON files, and the README. The companion's build and diagnostics are recorded in `APPENDIX_COMPILE_STATUS.json`.

## Rendered-page evidence

| Report | Final artifact and inspected physical pages |
|---|---|
| `PDF_DIPLOMATIC_QA.md` | French diplomatic: 1, 2, 3, 35, 191, 320, 340, 580, 915. English diplomatic: 1, 2, 3, 37, 190, 230, 319, 338, 915. The report binds these samples to the final PDF hashes. |
| `PDF_FR_QA.md` | French apparatus: 83, 115, 253, 344, 928, 939, 1050, 1082. French reading: 3, 81, 86, 113, 245, 335, 555, 752, 899. |
| `PDF_EN_QA.md` | English apparatus: 2, 3, 88, 116, 235, 253, 325, 441, 934, 942, 949, 959, 960, 961, 985, 1030, 1061. English reading: 2, 3, 85, 103, 111, 112, 244, 727, 728, 729, 753, 769, 788, 793, 880, 902. |
| `APPENDIX_QA.md` | All twenty-one appendix pages, located at physical pages 1862–1882 in the integrated companion, together with selected full-book opening, long-formula, diagram, bibliography-transition, and final-page checks. The fitted implication charts are checked at physical 211 and 213. |

The diplomatic sample comprises 18 pages, the French corrected/reading sample 17 pages, and the English corrected/reading sample 33 pages: **68 selected reader pages** in total, in addition to the companion review. The detailed reports identify how the final renders were inspected or compared with previously inspected identical pixels. Temporary page images are reproducible with `scripts/render_pdf_qa.py` and are excluded from the delivery archives.

The selected wide formulas and long correction-register entries remain complete and visible inside the physical pages. Some formulas extend beyond the principal text measure; the compile diagnostics retain those distances. Large implication charts use reduced type to fit, with vector content available for enlargement. The inspected pages show the chart arrows and labels, author footnotes, and apparatus provenance without visible clipping at the selected loci.

## Specific projection and layout checks

- **Adjacent source-page labels:** the Chapter II edition `p. 61` and manuscript `[page 98]` labels occupy separate vertical positions after the shared margin-layout repair. The final French apparatus 115, French reading 113, and English reading 112 samples show the separation.
- **Boxed manuscript anchor:** the unique source `\mspin{page 39}` is visible in the right margin on French reading 86, English apparatus 88, and English reading 85, clear of the long brace/table.
- **Chapter VI author triangle:** the reading projection retains both author rows and both branches at manuscript pp. 197–198. French reading 245 and English reading 244 show the retained triangle; English apparatus 253 shows the corresponding source and editorial alternative. Exact source-cell ownership is checked by the independent omission replay.
- **Chapter XVIII author notes:** the English reading samples show notes 19/20 at 727–729, note 58 at 753, and note 105 at 793. French reading 752 shows note 58. Their retained text and numbering agree with the documented projection operations.
- **Editorial doubt marks:** the six spaced `[\,?]` source occurrences are absent at the six inspected final English reading loci. The spacing-aware scan of all 902 English reading pages returns zero bracketed-question matches. Exact omission replay covers both languages, including all 26 plain doubt-marker operations per language.
- **Correction-register headers and long entries:** the final French register uses “Apparat des corrections”; the English register uses “Apparatus of corrections”. First, long, continued, and final entries were inspected. The English ENV0364 continuation on 961 remains fully visible despite its logged 13.67697 pt excess beyond the principal text measure.
- **Credits and rights:** the exact front-matter wording is checked against the supplied notices. Within each language, the credits/rights page has identical extracted text and rendered pixels across the three forms, as recorded in `PACKAGING_CREDITS_VALIDATION.json`.

## Final local margin refinements

The complete margin scan identified two actual ink collisions beyond the initial 68 full-page samples: edition `p. 58` with a comma on French reading physical 603, and manuscript `[page 152]` with the closing mathematical expression on English diplomatic physical 438. The builder now moves the former label right by 6 TeX points and the latter by 20 TeX points, using unit-scoped exact-argument overrides. Each rule is shared by the three forms of its language and its annotated master. `MARGIN_PLACEMENTS.tsv` records the source units, decision identifiers, and pre-repair artifact identities.

Both repaired loci were rendered at high scale from the completed new PDFs and visually checked in two independent GPT-6 Astra review passes. The labels are visibly separated from the author's punctuation and formula, and their complete text remains inside the page. All eight rebuilt PDFs have the preceding page counts and diagnostic counts. Exact source/anchor and independent body/omission audits pass again on the rebuilt artifacts.

`MARGIN_REFINEMENT_COMPARISON.json` and `.md` compare the eight new PDFs with the preceding PDF set preserved in checkpoint 7. The comparison passes on all **7,604 reader/master pages**: **7,596 pages are exactly unchanged**, and the remaining eight contain exactly their permitted label translation with no unexpected difference. All **68 initial full-page sample images are pixel-identical**. It checks exact non-target text/glyph, page, vector, image, link and annotation geometry; the report describes the small coordinate-serialization allowance for the target translations and the explicitly handled shared PDF paint operation. `MARGIN_LAYOUT_AUDIT.json` and `.tsv` record the final whole-reader label scan, reviewed geometry candidates, and measured clearance at the two repaired source anchors. The two repaired-page crops supplement the initial full-page sample list. The final label scan covers all **5,774 standalone-reader pages** and **19,196 recognized margin labels**. Its **30 geometry candidates at 21 file/page locations** were freshly rendered: 18 have visibly separated ink, and 12 are fragments of their own wrapped label. The report records **zero confirmed remaining collisions and zero unreviewed candidates**. `MARGIN_LAYOUT_REVIEW.json` binds every visual decision to the exact PDF hash and candidate geometry.

## Complete-document checks

`VALIDATION.json` checks all 243 units per language, their final plans, the master/standalone projection correspondence, exact source replay, every anchor sequence, and current source/PDF hashes. All 1,879 correction rows have recorded terminal outcomes. The independent `APPENDIX_READER_NOTES_AUDIT.json` verifies the exact reading bodies against 977 logged operations per language, including author/editor ownership at the interleaved diagram and signed footnotes.

The delivery audit checks **all nine PDFs and all 9,510 pages**, PDF metadata, link URIs, and the approved text payload for private paths and email addresses. It reports **zero privacy findings**. Each of the **1,982 French and 1,623 English apparatus identifiers** has exactly one PDF named destination, a valid destination page, and exactly one inbound annotation whose rectangle contains the visible matching identifier. Both default annotated-master PDFs match their diplomatic standalone PDFs page by page in exact extracted text, page rectangles, media/crop boxes, and rotation, covering 915 pages in each language. Final evidence is in `DELIVERY_VALIDATION.json` and `DELIVERY_APPARATUS_LINKS.tsv`.

The source, typesetting, and visual records report the operations and observations above. The appendix's mathematical reading paragraphs preserve the supplied proof dependencies and missing-source limitations; those paragraphs and `APPENDIX_QA.md` state the scope of each assessment.
