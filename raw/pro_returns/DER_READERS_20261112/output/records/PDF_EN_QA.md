# English reader PDF visual QA

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026.

## Scope and status

This record covers independent visual samples from the English corrected text with apparatus and the English reading text. The PDF pages were rendered with PyMuPDF at a 1.45 scale (104.4 dpi) and opened as page images. Page numbers below are **physical PDF pages, counted from one**, including the title page. In these samples the printed running page number is one less than the physical page number.

The inspection addresses visible text, mathematical glyphs, diagrams, page anchors, footnote placement, and correction-register wrapping. It does not certify every page by visual inspection or validate the mathematical arguments. Source and projection invariants have their separate audit records.

**Final result:** all targeted checks below pass on the final PDFs. The six spacing-variant editorial doubt marks are absent from the reading form, the register has its own running header, and the adjacent Chapter II page anchors are visibly separated. No remaining clipped glyph, lost diagram component, or overlapping label was observed in the inspected final samples. No source, correction plan, or PDF was modified by this visual inspection.

The sample comprises **17 apparatus pages and 16 reading pages**. Both PDFs were rerendered after the final rebuild. Final front-matter images on apparatus pages 2–3 and reading pages 2–3, and apparatus page 116, are pixel-identical to their previously inspected images. For eight sampled register pages, the final pixels below image row 100 are identical to the previous sample; the only changed region is the running header. The first and last final register headers and the overflow continuation on page 961 were opened again. All other changed targeted pages were opened from the final renders.

## Final margin-refinement carryover

The final margin refinement moves one label outside this report's sample list in each English PDF. All **33 sampled pages** retain exactly equal extracted text, text-span positions, vector drawings, and rendered pixels in the new release. `MARGIN_REFINEMENT_COMPARISON.json` and `.md` compare every page of all eight reader/master PDFs against the saved preceding files: 7,604 pages in total, with 7,596 exactly unchanged pages and only the eight permitted label moves. The full RGB pixels of all 68 previously reviewed reader samples, including these 33, match exactly at the same 1.45 scale. The identities below are the new PDF and source hashes. The moved-label pages are reviewed separately in the final margin audit.

## PDF identities

| Form | File | Pages | Bytes | Final SHA-256 |
|---|---|---:|---:|---|
| Corrected with apparatus | `output/EN/DER_EN_corrected_apparatus.pdf` | 1,061 | 6,551,750 | `30cb37db498e4decf10701ac0ff3c579282170bba3be808c577617eb71b39fd6` |
| Reading text | `output/EN/DER_EN_reading.pdf` | 902 | 5,962,207 | `eb43fd6b673ef04ee3403e43057ff8838a74501d39162232d3a3d117a4b97d7b` |

Both final files completed two stable passes with zero TeX errors, undefined-command reports, unsettled-reference reports, backend warnings, and missing-glyph messages. Each retains one package warning: `epstopdf` reports that shell escape is disabled. The final PDF and source hashes were independently matched to `output/records/build/DER_EN_corrected_apparatus.json` and `output/records/build/DER_EN_reading.json`.

Source SHA-256 values:

- Apparatus TeX: `53bd8ecfc116421029d0330b63e5855d3caf2fc5895e3a78572b0f4c6aa4d056`.
- Reading TeX: `a1bf554df02116d96b394f16255a8194e4e5d51e5b4d10df6b5655d72a79067f`.

## Front matter and dense mathematical pages

| Form | Physical page(s) | Material inspected | Observation |
|---|---:|---|---|
| Both | 2 | Credits, source ownership, rights notice | The credits and rights notice fit inside the page. The displayed source address is complete. No clipping or overlap was visible. |
| Apparatus | 3 | Preface and editorial/apparatus ownership | Paragraphs, quotations, and form descriptions are legible and separated. |
| Reading | 3 | Reading preface | The explanatory text includes the handling of the Chapter XIV afterword, Chapter XIII references, and author quotations in note 58. The paragraph ending previously corrected by the assembler reads continuously. |
| Apparatus | 116 | Chapter II chart, edition pp. 60–61 / manuscript pp. 97–98 | The large chart and its arrow labels fit on the page. Type is substantially reduced to fit the chart; zoom is useful. The footnotes below remain separate from the diagram. |
| Reading | 103 | Chapter II orthogonality examples | The former spaced doubt mark following “convex circled” is absent; the sentence, nearby formulas, and marginal page labels remain legible. |
| Reading | 111–112 | Chapter II chart and adjacent prose | Arrows, chart labels, and explanatory text are visible. The two former doubt marks are absent. On page 112, the edition anchor p. 61 is above manuscript anchor [page 98], with visible space between them. The large chart type is reduced to fit; zoom is useful. |
| Apparatus | 235 | Chapter VI Cartesian diagrams and long Hom expression | The long line extends past the main text measure, but the visible expression stays inside the physical page. The diagrams and their labels remain visible. No clipped glyph was observed. |
| Apparatus | 325 | Chapter VII path diagrams and brace conditions | Vertical diagrams, arrow labels, braces, and accompanying formulas remain readable. No visible overlap or clipping was found in the sample. |
| Apparatus | 441 | Chapter XII.5 Proposition 14, stacked square/integral diagrams | Both large bracketed diagrams fit. The dense lower line and footnote 90 remain visibly separated by the footnote region. |
| Reading | 769 | Chapter XVIII Proposition 4.8.2 | The proposition, displays, and implications are visible and legible. The former doubt mark after “canonical injection” is absent. |
| Reading | 788 | Chapter XVIII 4.9.6.8 and preceding diagrams | Both upper diagrams, the implication chain, and lower formulas are visible. The former doubt mark after “we know” is absent. |
| Reading | 880 | End of Chapter XVIII, essential-image paragraph | The former doubt mark after “Conversely, every” is absent. The adjoining limit formulas and lower-page text remain visible. |
| Reading | 902 | End of Chapter XIX | Questions 3.13–3.15 and the closing author paragraph are complete within the page. The right-hand page anchors are legible. |

The final apparatus log's largest body overfull box is 61.82962 pt; the register-specific overfull box identified for this review is 13.67697 pt. A box warning gives a distance beyond TeX's text measure. The visual observations above concern whether the sampled material is visibly lost or collides after it is placed on the actual PDF page. The apparatus has 32 overfull horizontal boxes and one overfull vertical box (maximum 1.35669 pt); the reading text has 26 and two respectively (maximum vertical 2.03893 pt). The compile records retain their exact diagnostics.

## Boxed manuscript anchor

The single `\mspin{page 39}` occurrence comes from Chapter II, source unit pp. 26–30. It lies inside a boxed diagram and uses the dedicated margin-note placement. The final `[page 39]` label is visible in the right margin on **apparatus physical page 88** and **reading physical page 85**, beside the middle of the large brace/table. In both forms it is separate from the diagram labels and the lower edition anchor p. 26. The brace, the lower displayed implication, and footnotes 46–49 remain visible.

## Chapter VI interleaved triangle

| Form | Physical page | Observation |
|---|---:|---|
| Apparatus | 253 | At manuscript p. 198, the author's triangle in the left columns and the bracketed editorial alternative in the right columns are both visible. The two author branches and their target labels are complete. Subsequent displayed functor arrays remain visible. |
| Reading | 244 | The author's triangle retains both rows, both branches, and all three author objects. The editorial alternative and its surrounding brackets are absent. The following arrays remain complete, with no orphan bracket or visible diagram clipping. |

These images were compared as corresponding projections of the same interleaved source diagram. The whole before/after source operation is recorded separately in the reading-omission TSV.

## Chapter XVIII author footnotes

| Physical reading page(s) | Note(s) | Observation |
|---:|---|---|
| 727 | 16, 17, and beginning of 19 | Notes 16 and 17 are legible. Author note 19 starts with “Other conditions”. The removed editorial note 18 has no visible text or printed note marker. |
| 728 | Call to 20 | The in-text note 20 call is visible after the equalization clause. Dense Hom displays and the diagram remain legible. |
| 729 | Continuation of 19; notes 20 and 21 | The retained list continuation for note 19 is legible. Note 20 starts “A bit brief” and preserves the author's incomplete wording; no editorial incomplete-sentence label remains. No overlap with the body was observed. |
| 753 | 58 | The quotation beginning “cf. simpler result above, if C is strictly generating” and the marginal corollary are visible in the footnote. The editorial framing and signature are absent. The retained author material fits within the footnote region. |
| 793 | 105 | The author note beginning “A bit short! The argument ought to be spelled out with care” is visibly numbered 105 and fits below the rule. The preceding dense limit expressions remain clear. |

The note-number checks supply visual evidence for the two hidden counter advances described in the README. They do not count or independently inspect every footnote in the book.

## Correction-register samples

| Physical apparatus page(s) | Entries or location | Observation |
|---:|---|---|
| 934 | First register page, ENV0001 onward | The register heading, chapter grouping, source/correction labels, and source-row references are readable. The final running header says “Apparatus of corrections”. The last visible entry continues onto the following page without clipping. |
| 942 | ENV0106 and adjacent entries | The long prose source and corrected text wrap across multiple lines. The monospaced literal TeX remains readable. |
| 949 | ENV0226, clamping display | The long before/after display source wraps inside the page. The entry continues at a page boundary; its visible lines do not collide. |
| 959 | ENV0351 and preceding entries | The long before/after prose and mathematical source text wrap cleanly. The source-row reference remains visible at the end. |
| 960–961 | ENV0364, register-specific 13.67697 pt overflow | The entry begins at the bottom of 960 and continues at the top of 961. The first correction line extends past the main text measure but remains fully visible inside the physical page. Its following line and source reference are clear; the next entry starts separately. |
| 985 | ENV0716–ENV0718, Hom and fibre-product expressions | Long literal expressions wrap across several lines with all visible punctuation and command text inside the page. The following entries remain separated. |
| 1030 | ENV1229–ENV1231, including ENV1230 | The cardinal-renaming quotations and corrections wrap cleanly. Source references and subsequent entry labels remain visible. |
| 1061 | Final register page, ENV1620–ENV1623 | The register ends with ENV1623 and its source reference. No last-line truncation or extra continuation is visible. The final running header says “Apparatus of corrections”. |

## Findings and targeted closure

### Spaced editorial doubts

The earlier reading sample exposed six bracketed question marks matching the spacing-aware PDF-text expression `\[\s*\?\s*\]`. Their source spelling is `[\,?]`. The assembler confirmed that they are editorial uncertainty marks under the source edition's stated convention and added their removal to the reading projection. Their physical page locations remained the same after the final rebuild:

| Physical page | Earlier context |
|---:|---|
| 103 | “convex circled [ ?] weakly closed subsets” |
| 111 | “operations of 7.4 a) [ ?]” |
| 112 | Chart label “X pseudo-cofiltering [ ?]” |
| 769 | “canonical injection [ ?]” |
| 788 | “we know [ ?]” |
| 880 | “Conversely, every [ ?] x” |

All six final pages were opened as images and the marks are absent at the identified positions. A spacing-aware scan of the text of **all 902 final reading pages returned zero matches**. The omission TSVs independently contain 26 `plain_editorial_doubt` rows and 977 total rows per language, including the six source-spacing variants. The apparatus retains editorial doubt marks under its stated projection policy; its scan is not an omission test.

Final spacing-aware residual scan: **PASS — zero matches**.

### Register running header

The earlier register carried “Chapter XIX” into pages containing corrections from other chapters. The final header reads “Apparatus of corrections”. The first and last register pages, physical 934 and 1061, were visually rechecked; the header is also visible on physical 961. **PASS**.

### Chapter II page-anchor collision

The earlier reading page 112 superimposed edition p. 61 and manuscript [page 98]. The assembler's shared `marginfix` placement now stacks these labels. On final physical page 112 they are visibly separated at the upper-right edge without losing chart text or arrows. The nearby p. 62 and [page 99] labels are also visible. **PASS**.

### Final closure

Final register overflow continuation, changed-page inspection, the unique boxed anchor, retained author footnotes, and exact PDF/source hash correspondence all pass within the scope described here. The complete physical sample lists are:

- Apparatus: **2, 3, 88, 116, 235, 253, 325, 441, 934, 942, 949, 959, 960, 961, 985, 1030, 1061**.
- Reading: **2, 3, 85, 103, 111, 112, 244, 727, 728, 729, 753, 769, 788, 793, 880, 902**.

Scratch page images are inspection intermediates and are excluded from the delivered records archive.
