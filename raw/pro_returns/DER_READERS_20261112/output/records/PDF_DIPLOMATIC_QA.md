# Diplomatic PDF visual review

Final review: GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026.

The selected diplomatic pages were rendered with PyMuPDF to PNG at 1.45 times the PDF coordinate scale (104.4 dpi) and opened as page images during the visual review. Their observations carry over to the final PDF identities through the exact image comparison below. **No clipped content, overlapping text, missing-glyph boxes, or broken diagram boundaries were observed in the reviewed pages.** The PNGs are working files and are excluded from the delivery. This review made no changes to the sources, correction plans, or PDFs.

This is a focused visual review of 18 pages, supplemented by the full-book compilation and privacy checks. It does not claim page-by-page visual inspection of both books. Page numbers below are **physical PDF pages**, including the unnumbered title page; the running book-page number is one lower after that title.

## Final margin-refinement carryover

The final margin refinement moves one label outside this report's sample list in each diplomatic PDF. All **18 sampled pages** retain exactly equal extracted text, text-span positions, vector drawings, and rendered pixels in the new release. `MARGIN_REFINEMENT_COMPARISON.json` and `.md` compare every page of all eight reader/master PDFs against the saved preceding files: 7,604 pages in total, with 7,596 exactly unchanged pages and only the eight permitted label moves. The full RGB pixels of all 68 previously reviewed reader samples, including these 18, match exactly at the same 1.45 scale. The identities below are the new PDF and source hashes. The moved-label pages are reviewed separately in the final margin audit.

## Reviewed files

| File | Total PDF pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `output/FR/DER_FR_diplomatique.pdf` | 915 | 6,087,076 | `ea63b05972a83fa916b041dd5c85441ea6b6da0401eee5e2f27f7f0a527aa4ad` |
| `output/EN/DER_EN_diplomatic.pdf` | 915 | 6,076,518 | `544d3b3f84665aa0c7e29db2f43306254f648d897656ed9bd2cb590655f439d1` |

The PDF hashes and the corresponding TeX hashes match the completed build records `output/records/build/DER_FR_diplomatique.json` and `output/records/build/DER_EN_diplomatic.json`. The source SHA-256 values are:

- French: `1806e8761c91763907a9e2825ac7953fd1d01db0ff104e15efaf7a05695e9220`.
- English: `8bc0159090ddc848f905b6966ff4a57a375aa402697b35a3f67c8965252cd38e`.

## Page selection and observations

| Review target | French PDF pages | English PDF pages | Observation |
|---|---|---|---|
| Title | 1 | 1 | Author, title, language/form, edition credit, and date are clear and centered. Accented characters render correctly. |
| Credits and rights | 2 | 2 | The repository credits, explicit AI-production wording, translator credit, build credit, edition URL, and complete language-specific rights statement are legible. No text is clipped. |
| Preface | 3 | 3 | The explanation of anchors, editorial notes, and apparatus is readable and separated from the body. Page numbering is clear. |
| Early dense formulas | 35 | 37 | Multiple functors, subscripts, arrows, displayed formulas, and editorial brackets remain readable. The French page's base-change diagram and the English page's footnotes are complete. Margin anchors do not cover the formulas or prose. |
| Large Chapter VI diagrams | 191 | 190 | The French page contains the second large category diagram; the English page contains both related diagrams. Their arrows, labels, dotted comparison maps, and accompanying footnotes fit on the page. Small labels remain legible when zoomed; no diagram is cropped. |
| Long path diagrams | 320 | 319 | The extended chain and its overbraces remain inside the page boundary. Labels and endpoint ellipses are visible, including the French chain near the lower edge and the English diagram's final “useful part” underbrace. |
| Wide Chapter IX display | 340 | 338 | The multiline functor/composition display uses part of the right margin but remains complete and readable. The chapter opening and edition's signed note are clearly identified. The address placeholder remains redacted. Adjacent edition and manuscript anchors are separately visible. |
| Other widest logged material | 580 | 230 | French: the cardinal estimate, equality sign, and underbrace captions remain readable inside the physical page. English: the long base-change theorem sentence extends beyond the nominal text block but is fully inside the page, above a distinct footnote region. No page anchor covers either passage. |
| Final page | 915 | 915 | Question 3.15, closing prose, and manuscript/edition anchors are present; each page ends cleanly without a truncated line. The French page also contains Question 3.14; the English page starts with its continuation. |

The exact final physical sample lists are French **1, 2, 3, 35, 191, 320, 340, 580, 915** and English **1, 2, 3, 37, 190, 230, 319, 338, 915**. The mathematical content was used to locate the corresponding final pages before rendering.

## Relation to compiler warnings

The inspected wide displays retain some of the source's long mathematical constructions. Their overfull-box warnings are still reported; a zero-error compile is not described as a zero-warning compile.

| Book | Largest overfull horizontal box | Overfull horizontal boxes | Overfull vertical boxes | Missing glyphs | Undefined or unsettled references |
|---|---:|---:|---:|---:|---:|
| FR diplomatic | 59.28604 pt | 31 | 1 | 0 | 0 |
| EN diplomatic | 61.82962 pt | 29 | 0 | 0 | 0 |

The French maximum at running page 339 corresponds to physical page 340; the English maximum at running page 229 corresponds to physical page 230. Both specific pages were visually inspected. The French overfull vertical box has a maximum of 0.72427 pt. The other reviewed overflow pages are listed above.

Both final build records contain two stable passes, zero TeX errors, zero undefined-command and unsettled-reference reports, zero missing-glyph messages, and zero backend warnings. Each has one package warning: `epstopdf` reports that shell escape is disabled. These diagnostics and the visible extent of a sampled formula have their stated scopes; this sample does not certify every page or the mathematical arguments.

Full extracted-text and metadata privacy checks are recorded separately in `PACKAGING_PDF_PRIVACY.json` and the packaging audit. The corrected and reading forms have their own final visual records, `PDF_FR_QA.md` and `PDF_EN_QA.md`; this record concerns the two diplomatic forms only.
