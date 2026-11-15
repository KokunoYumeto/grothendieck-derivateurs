# Final French corrected and reading PDF review

Review date: 12 November 2026. Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode).

This report records visual inspection of selected rendered pages of the final French corrected-with-apparatus and reading PDFs. Page numbers below are physical PDF page numbers, including the title page. The source and correction audits cover all 243 units; this visual review covers the pages explicitly listed below.

## Artifacts inspected

| PDF | Pages | SHA-256 |
|---|---:|---|
| `output/FR/DER_FR_corrige_apparat.pdf` | 1,082 | `08c6e300cff88207d0a1ebda84e49284f622ef2ad4ac983a63c8b226ee10fdb1` |
| `output/FR/DER_FR_texte_de_lecture.pdf` | 899 | `158d9b545a5434c61c97d2bb8c28baddd6bed31a34d5dda61c5fd2c19867a59e` |

The pages were rendered with `scripts/render_pdf_qa.py` and examined as full-page images. A final unit-scoped placement repair then moved edition label `p. 58` by 6 TeX points in Chapter XV across the three French forms. `MARGIN_REFINEMENT_COMPARISON.json` compares the preceding and delivered PDFs; the listed visual sample pages are among its exact old/new pixel comparisons. The repaired reading-page 603 label was additionally rendered at high scale and visually confirmed clear of the author comma. The source body and anchor arguments remain unchanged. Temporary page images are reproducible from the delivered PDFs and are excluded from the release archives.

## Corrected-with-apparatus sample

| Physical page | Inspection and observation |
|---:|---|
| 83 | Dense cohomological formulas and diagrams remain readable; marginal source-page labels and surrounding prose are visible. |
| 115 | The large Chapter II implication chart fits the page. The grey edition label `p. 61` and manuscript label `[page 98]` occupy separate vertical positions. The following source-page anchor is visible. |
| 253 | Wide base-change formula, surrounding footnotes, and correction markers are complete and distinguishable. |
| 344 | Chapter IX opening, long formulas, editorial notes, and correction markers are visible. Long mathematics extends into the available side space without clipping at the page edge in this sample. |
| 928 | The correction register begins with the running header “Apparat des corrections”; identifiers, locations, readings, replacements, and provenance are legible. |
| 939 | Long literal-LaTeX entry FRV0149 wraps across lines with its source and replacement intact. |
| 1050 | The long cardinal-paragraph entry FRV1502 wraps through its full before/after text. |
| 1082 | The final register entries and running header are present and complete. |

## Reading-text sample

| Physical page | Inspection and observation |
|---:|---|
| 3 | The reading preface explains editorial omissions, retained author material, and page anchors. Its text and layout are complete. |
| 81 | The wide exact sequence remains complete and readable; surrounding text and source-page labels remain visible. |
| 86 | The unique `\mspin{page 39}` source anchor appears as `[page 39]` in the right margin beside the long Chapter II display, clear of its text. The `p. 26` label and footnotes remain visible. |
| 113 | The large Chapter II chart is fitted to the page. Edition `p. 61` and manuscript `[page 98]` labels are separated; subsequent anchors and footnotes remain visible. |
| 245 | The retained author triangle at manuscript pp. 197–198 has both rows and both downward arrows. The following author formulas and prose remain present. |
| 335 | The Chapter IX opening and long category/composition formulas are complete. Margin anchors are visible. |
| 555 | The end of Chapter XIV retains the author's text, proposition, diagram, and source anchors after the logged editorial-afterword omission. |
| 752 | Chapter XVIII author note 58 retains the transmitted author quotation and marginal corollary. The note is readable at the foot of the page. |
| 899 | The end of Chapter XIX, final questions, attention marks, and manuscript anchors through `[page 50]` are present. |

## Result and associated checks

The 17 inspected pages showed complete visible content at the selected wide-formula, chart, editorial-projection, footnote, and long-apparatus loci. The final compile records have zero errors, missing glyphs, unresolved references, rerun requests, and backend warnings. Each of these two PDFs has one `epstopdf` package warning that shell escape is disabled. Box diagnostics remain reported in their build JSON files and in `COMPILE_STATUS.tsv`.

`VALIDATION.json` checks the exact source replay, master projections, anchors, and apparatus counts. `APPENDIX_READER_NOTES_AUDIT.json` independently replays reading omissions and checks the author-diagram and author-footnote cases. `DELIVERY_VALIDATION.json` supplies the completed release's PDF, privacy, and apparatus-link checks. The consolidated visual-review record is `PDF_VISUAL_QA.md`.
