# Final margin-layout audit

## Outcome

**Pass.** All six final reader PDFs were scanned after their source and PDF SHA-256 values matched successful compile records. The scan covers **5,774 physical pages** and **19,196 recognized margin labels**. Every reported candidate has been visually reviewed against these final PDF bytes. There are **zero confirmed remaining collisions** and **zero unreviewed candidates**.

Two visible overlaps found during the first scan have been repaired: the French Chapter XV edition label `p. 58` and the English Chapter XII, 5 manuscript label `[page 152]`. Their unit-scoped placement decisions are recorded in `MARGIN_PLACEMENTS.tsv`. The correction plans and source anchor calls remain unchanged.

## Final scan coverage

| PDF | Pages | Recognized labels | Geometry candidates |
|---|---:|---:|---:|
| `DER_FR_diplomatique.pdf` | 915 | 3,199 | 6 |
| `DER_FR_corrige_apparat.pdf` | 1,082 | 3,199 | 4 |
| `DER_FR_texte_de_lecture.pdf` | 899 | 3,200 | 3 |
| `DER_EN_diplomatic.pdf` | 915 | 3,199 | 5 |
| `DER_EN_corrected_apparatus.pdf` | 1,061 | 3,199 | 8 |
| `DER_EN_reading.pdf` | 902 | 3,200 | 4 |

The 30 final geometry candidates occur at 21 file/page locations. Twelve are the prime or parenthetical text belonging to the same wrapped manuscript label. Nine involve adjacent labels whose font rectangles intersect slightly but whose ink is visibly separated. Nine involve body text near a label; fresh rendered crops confirm separate ink, including the close formula punctuation in French diplomatic page 456 and the translation gloss in English diplomatic page 866 / apparatus page 883.

`MARGIN_LAYOUT_REVIEW.json` records the decision for each candidate. Each review key includes the PDF SHA-256, file, physical page, label and other text, and both rectangles. A changed PDF or candidate geometry cannot silently inherit a decision. `scripts/scan_margin_layout.py` replays those decisions into `MARGIN_LAYOUT_AUDIT.json` and `.tsv`.

## Repaired label positions

The following horizontal clearances are measured in PDF points between the label rectangle and the rightmost body-text rectangle sharing its vertical band. All six affected instances were rendered and visually checked.

| PDF | Physical page | Label | Left edge, PDF pt | Body-text clearance, PDF pt |
|---|---:|---|---:|---:|
| `DER_FR_diplomatique.pdf` | 615 | `p. 58` | 516.214 | 2.762 |
| `DER_FR_corrige_apparat.pdf` | 622 | `p. 58` | 516.214 | 20.153 |
| `DER_FR_texte_de_lecture.pdf` | 603 | `p. 58` | 516.214 | 2.762 |
| `DER_EN_diplomatic.pdf` | 438 | `[page 152]` | 530.161 | 2.890 |
| `DER_EN_corrected_apparatus.pdf` | 448 | `[page 152]` | 530.161 | 142.851 |
| `DER_EN_reading.pdf` | 433 | `[page 152]` | 530.161 | 142.851 |

The French rule adds 6 TeX points inside the existing edition-label margin box; the English rule adds 20 TeX points inside the existing manuscript-label margin box. These become approximately 5.978 and 19.925 PDF points. Both formerly colliding passages now have a visible gap.

## Chapter II targets

The edition-page-61/manuscript-page-98 pair and the boxed-source manuscript page 39 were checked in every form. The paired labels have a positive vertical rectangle gap of 1.215–1.216 PDF points and a clear ink gap. The manuscript-page-39 label is in the right margin, clear of body text and diagrams. Fresh final renderings were inspected for all twelve file/page locations.

| PDF | Edition 61 / manuscript 98, physical page | Manuscript 39, physical page |
|---|---:|---:|
| `DER_FR_diplomatique.pdf` | 113 | 87 |
| `DER_FR_corrige_apparat.pdf` | 115 | 88 |
| `DER_FR_texte_de_lecture.pdf` | 113 | 86 |
| `DER_EN_diplomatic.pdf` | 112 | 85 |
| `DER_EN_corrected_apparatus.pdf` | 116 | 88 |
| `DER_EN_reading.pdf` | 112 | 85 |

## Method and limits

The script identifies right-margin edition and manuscript text labels by position, prefix, font and color. It compares label/label and label/nonlabel-text rectangles only. The candidate threshold is an intersection area of at least 1 square point, width of at least 0.25 point, and height of at least 0.5 point. Text rectangles include font ascent and descent, which explains the harmless geometry candidates.

The first scan found 36 candidates at 23 file/page locations. High-magnification review confirmed three overlapping glyph pairs at two locations; the two placement changes removed those collisions. The final remaining candidates have exactly the previously reviewed text and geometry and were also freshly rendered. Focused crops were inspected at 4× resolution, with the closest initial punctuation/formula cases inspected at 10–12×. Working images are excluded from the deliverables.

This audit checks text-label geometry and the explicitly rendered targets. It does not classify arbitrary mathematical glyph overlaps or PDF vector paths. The separate `MARGIN_REFINEMENT_COMPARISON.json` compares the eight reader/master PDFs against the preceding checkpoint, including text, vector, page and sample-pixel geometry.
