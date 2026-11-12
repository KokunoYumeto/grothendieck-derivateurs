# Independent reader note and author-text audit

**Status: PASS.** This audit covers both annotated masters and all six emitted reader sources. It reads the verified original units and replays the recorded changes without importing the reader builder or its editorial-note parser.

## Results

| Check or count | French | English |
|---|---:|---:|
| Original units checked | 243 | 243 |
| Exact variant intervals | 1982 | 1623 |
| Recorded reading omissions or replacements | 977 | 977 |
| Neutral signs for missing or illegible text | 11 | 11 |
| Original source hashes match | Pass | Pass |
| Embedded original sources match | Pass | Pass |
| Diplomatic bodies preserve the source | Pass | Pass |
| Apparatus bodies contain the exact recorded variants | Pass | Pass |
| Editorial source strings remain unchanged | Pass | Pass |
| Every reading-body byte is explained by recorded changes | Pass | Pass |
| All source page anchors occur in the same order | Pass | Pass |
| Unit forms equal the master projection pieces | Pass | Pass |
| Standalone files exactly equal their master projections | 3/3 | 3/3 |
| Unexplained source or projection differences | 0 | 0 |
| Remaining bracketed editorial markers in reading bodies | 0 | 0 |

Variant intervals are exact edits, and are not counts of correction-table rows. Duplicate table rows can share an interval, and a row can require several intervals. Omission records also count structural cleanup and retained-author replacements; they are not a census of distinct editorial assertions.

## What exact replay proves

For every unit, the diplomatic body equals the original body after the declared common typesetting repairs, page-break reflow, privacy redaction, and the separately added editorial attribution label. Removing apparatus markers from the corrected apparatus body gives exactly the original body with its recorded variants. Applying the omission ledger to that corrected body gives exactly the reading body. This checks all body characters. The separate ownership review below establishes which parts of a recorded span belong to the editors and which author parts its replacement must retain; exact replay alone does not establish ownership.

The audit also replays every omission source string against the original body. All ledger strings are present unchanged, including the complete unbracketed editorial passages. The shared bold-Delta repair does not occur in any logged editorial passage. Every source anchor argument and its order are checked in all three projections of both languages.

## Editorial ownership decisions checked against the supplied sources

1. **Plain question marks.** The edition front note states: “Un point d'interrogation entre crochets signifie que l'on n'est pas sûr du mot qui précède.” All twenty-six plain doubt markers in each language, including six with TeX spacing inside the brackets, were inspected in context. They mark uncertainty about the preceding word or expression. The reading form removes the marker and retains that word or expression. Diplomatic and apparatus forms retain the markers. Evidence: the introductory editorial note in `transcription/Der-ChI-234/Der-ChI-234_p001-005.tex` and the twenty-six `plain_editorial_doubt` ledger records.

2. **Table-of-contents note.** The final note in `transcription/dertbmt/dertbmt_p001-005.tex` describes the electronic edition’s chapter division and manuscript pagination. Its source wording is retained and attributed in diplomatic/apparatus forms; the reading form omits the exact note and its separator. The table entries remain.

3. **Chapter XIV afterword.** The section expressly headed `Postface des éditeurs` / `Editors’ afterword`, printed pages 7–9, is editorial. The reading form omits its two unit spans, while retaining all page anchors. Both other forms preserve its full text. Sources: `transcription/Der-ChXIV-07-10-10/Der-ChXIV-07-10-10_p006-010.tex` and `_p011-011.tex`, with the corresponding translation units.

4. **Signed Chapter XVIII footnotes.** The chapter’s front note expressly identifies `N. Éd.` as the mark of editor-added footnotes. In `der-ch18_p016-020.tex`, only the third, signed editorial footnote and its separating comma are removed. The two preceding author footnotes remain. The exact replay checks their complete contents.

5. **Author quotations inside footnote 58.** In `der-ch18_p046-050.tex`, the editors explicitly attribute two marginal annotations to Grothendieck: the quotation beginning “cf. résultat plus simple ci-dessus” and the following corollary. The reading form retains those exact author strings, including the original footnote command, and removes the editorial attribution prose and the nested editorial insertion `[une]` / `[a]`. Separate exact-string assertions verify the quotation, the corollary, and their complete retained footnote in both languages. The reading prefaces explain this treatment.

6. **Chapter XIII reference material.** Its front note identifies the final indexes, axiom list, glossary, and bibliography as compiled by the editors. These reference sections remain, with their editorial authorship stated in the reading preface.

7. **Struck-out and missing-text reports.** The short notes reporting crossed-out words or passages disappear with the other editorial notes. Their surrounding author prose and proofs remain through the exact-body invariant. All eleven neutral replacements were inspected: each records missing or illegible text, including a missing page, theorem number, index, or continuation. The fourteen longest bracketed omissions were also inspected, including array and diagram closings and the definition crossing a printed-page boundary.

## Interleaved diagrams and line-break ownership

All eight original bracket-note spans containing alignment row breaks were inspected in each language, including their surrounding source cells. No further single-row bracket-note span contains an alignment separator. One span, Chapter VI manuscript pages 197–198, interleaves the author’s left triangle with the editors’ right triangle in a single matrix. Its ledger record now replaces the whole matrix by the exact first three columns of both rows. This retains the author’s apex, both lower objects, and both arrows. The other seven spans contain no interleaved author cell. The audit asserts the complete retained VI triangle and the exact inventory of reviewed spans.

| Source unit | Ownership finding |
|---|---|
| `Der-ChI-234/Der-ChI-234_p041-045.tex` | The two final rows of a label tabular belong entirely to the editor note; the preceding author rows remain. |
| `Der-ChV-234/Der-ChV-234_p001-005.tex` | The bracket opens before a separate display and owns its complete array. |
| `Der-ChVI-345/Der-ChVI-345_p121-125.tex` | One shared matrix interleaves the author left triangle and editor right triangle. The reading projection retains author columns 1–3 of both rows. |
| `Der-ChVII-456/Der-ChVII-456_p041-045.tex` | The bracket owns the separately displayed editorial cancellation diagram. |
| `Der-ChXIIc-30-03-03/Der-ChXIIc-30-03-03_p056-060.tex` | The bracket owns a separate editorial replacement diagram and its surrounding display. |
| `Der-ChXIII-25-01-04/Der-ChXIII-25-01-04_p006-010.tex` | The bracket owns the entire editorial definition and its displayed square diagram. |
| `Der-ChXV-05-11-10/Der-ChXV-05-11-10_p006-010.tex` | The note continues across one array line break; author expressions occur only before its opening and after its closing bracket. |
| `der-ch18/der-ch18_p146-150.tex` | The note continues across one array line break; no author expression is interleaved between the bracket boundaries. |

## Footnote markers and numbering

The six empty-note removals and the newly removed signed editorial footnote were inspected. All seven remove a complete `\footnote` call; none removes only a `\footnotetext` while leaving its paired marker. The five explicit optional numbers 7, 10, 75, 80, and 93 have no separate `\footnotemark` reference in their respective chapters. Explicit-number `\footnote[n]` does not advance the standard LaTeX counter; the installed LaTeX kernel’s `\@xfootnote` definition was checked for this point.

The other two omissions remove implicit-number notes and therefore retain an invisible `\stepcounter{footnote}`. In Chapter XVIII `p016-020`, editor note 18 is omitted and the following author notes remain 19 and 20. In `p091-095`, editor note 104 is omitted and the following author note remains 105. The audit independently simulates the relevant LaTeX counter operations and asserts the original and reading numbers of all three affected author notes in both languages. Their author words are covered by the full-body replay.

| Affected author note | Source number | French reading | English reading |
|---|---:|---:|---:|
| Autres conditions | 19 | 19 | 19 |
| Un peu bref | 20 | 20 | 20 |
| Un peu court | 105 | 105 | 105 |

## Omission ledger breakdown

| Recorded event kind | French | English |
|---|---:|---:|
| `editorial_afterword` | 2 | 2 |
| `editorial_contents_note` | 1 | 1 |
| `editorial_display_wrapper` | 1 | 1 |
| `editorial_footnote_marker` | 6 | 6 |
| `editorial_framing_author_quotes_retained` | 1 | 1 |
| `editorial_front_note` | 19 | 19 |
| `editorial_note` | 910 | 910 |
| `inline_page_duplicate` | 9 | 9 |
| `interleaved_editorial_diagram` | 1 | 1 |
| `plain_editorial_doubt` | 26 | 26 |
| `signed_editorial_footnote` | 1 | 1 |

## Reproduction and snapshot identity

Run `python output/records/scripts/build_appendix_reader_audit.py` from the extracted workspace. The script writes `APPENDIX_READER_NOTES_AUDIT.json` and this report, and exits unsuccessfully if any source, projection, ownership, or replay check fails. The JSON includes all per-unit checks and the six standalone-source hashes.

| Audited input | SHA-256 |
|---|---|
| Reader builder | `90834f9edb8c5227912b29739f9ab0b78d8d38e787b710b7e26c12e019e8f3eb` |
| French annotated master | `dea1c06df9425f60f3a7504acb3c8d2e740c4bbf67d10d9e34b3d491112041bf` |
| English annotated master | `6e8989fb6e99b8efa8f1e3a442111657f6a939800254fcfcf0b8ef7ce0235caa` |
| French omission ledger | `c5d221fe7cb5ddd8aceef77186a8d39023c9ac5e507f4d8e2ba1dd508609971d` |
| English omission ledger | `ea9e385d2c355af48f0ff2aaa844dbe67d67f91d1cc34d2390d76938c4ed9ea9` |

These are textual and ownership checks for the identified snapshot. The reader compilation and visual layout checks are recorded separately in the main build records. No original source unit is modified by this audit.
