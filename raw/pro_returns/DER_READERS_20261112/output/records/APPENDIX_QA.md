# Companion and new-results appendix

Paths and rebuild commands in this report are relative to the extracted `output/` directory.

## Delivered result

`companion/LesDerivateurs_companion.pdf` has **1,906 pages**. The new chapter occupies physical PDF pages **1,862–1,882** (printed pages 1,857–1,877). It contains all twelve entries in `NEW_RESULTS.md`, each with its exact inventory statement, manuscript bearing, provenance, the available cited statement and proof, and a paragraph headed **GPT-6 Astra's reading**. The opening preserves the inventory's limited-search and no-priority framing. The closing list preserves the statements found to be known and their references.

The supplied companion's **64 part and definition files are byte-identical** to their sources. The master adds the appendix input, a quotation-glyph alias, and fitting hooks for large `tikzcd` diagrams. Seven bibliography entries supply references used by the supplied parts or the appendix. The source mathematics has not been rewritten to solve layout problems.

## Build and verification

Four LuaLaTeX passes and a successful BibTeX run produced a stable final PDF. The final pass reports:

| Check | Result |
|---|---:|
| LaTeX errors | 0 |
| Package or LaTeX warnings | 0 |
| Undefined references or citations | 0 |
| Missing glyph warnings | 0 |
| Overfull horizontal boxes | 15 |
| Overfull vertical boxes | 7 |
| Underfull boxes | 27 |
| Largest horizontal excess | 39.36911 pt |
| Largest vertical excess | 5.5976 pt |

The box diagnostics occur in the inherited companion. The appendix has no overfull-box diagnostics. They are retained and reported; they have not been hidden by changing TeX's warning thresholds. The final sanitized log and all build-pass console outputs are included among the `APPENDIX_*` records. Intermediate TeX files, caches and raw logs are excluded from the deliverable.

All twenty-one appendix pages were rendered and inspected in the appendix proof. Final-book checks covered the opening pages, selected long source formulas and diagrams, the new chapter, the transition to the bibliography, and the final bibliography page. Physical pages 211 and 213 show the formerly oversized implication diagrams fitting within the page; the largest chart necessarily uses small type, with its vector content available for enlargement. No clipping was observed in these checks. The final full PDF text was scanned for email addresses and absolute personal or workspace paths; no hits were found. Source and bibliography deliverables received the same privacy check.

## Source availability and proof limitations

The appendix preserves the supplied claims and identifies their actual proof status. Its reading paragraphs do not stand in for the later independent peer review requested by the inventory.

- **Entry 3:** the source recalls the cardinal Kan–Thurston bound from memory. Its detailed bound, compatible classifying-space models, and limit-stage comparison are not supplied.
- **Entry 6:** the cited census program and run directory are absent. The statement, counts, and stated enumeration method are reproduced as source reports; the appendix does not claim to have rerun the census.
- **Entry 7:** the source cites James–EHP, Miller and arithmetic-square input, Kahn–Priddy, and Snaith in compressed forms. The appendix reproduces the available proof and names these dependencies. The source's separate, unproved accessibility speculation is outside the inventory entry and is not promoted to a theorem.
- **Entry 8:** the inventory says “only” in its description of homology localizers. The cited arguments establish their stated homology cases and a counterexample for the weak-homotopy localizer. The appendix explicitly records that these arguments do not prove the stronger inventory wording.
- **Entry 9:** the trefoil working note cited by the review is absent. The review supplies an argument paragraph, but no complete fibre, local-system, and base-change computation; the reading identifies the missing calculation.
- **Entry 10:** the supplied proof points to manuscript pages 102–103 and 112. The appendix labels that proof by reference and does not represent it as an expanded independent derivation.
- **Entry 11:** the reproduced proof retains its collage construction and affine-category exactness dependencies. The affine-category theorem is attributed to Isbell–Mitchell (1973), Theorem 3, as the supplied review requires. The accompanying direct calculations are preserved.
- **Entry 12:** the referenced email-claims check is absent. The available CATHOT proof and finite-group K-theory verification are reproduced and identified.

The other entries' reading paragraphs state the scope of their written proofs and external inputs individually. No absent file has been reconstructed or silently represented as available.

## Rebuilding

`records/scripts/build_appendix.py` extracts the selected source passages from the third supplied archive, creates the appendix, and integrates the companion. Its outputs include `APPENDIX_SOURCE_EXTRACTS.md`, `APPENDIX_VALIDATION.json`, and `APPENDIX_TYPESETTING_MAP.tsv`. These preserve archive member names, exact inventory cells, source-location identifiers, extraction hashes, and the one-glyph-at-a-time typography mapping used for Markdown mathematical text.

With a working LuaLaTeX distribution and BibTeX, run `records/scripts/build_appendix_compile.py` with `--companion companion --records records`. The wrapper records each exit code, writes sanitized logs, reports final warnings and the PDF hash, and removes raw auxiliary logs. It also accepts `--engine` and `--format` for a LuaTeX installation using a separately supplied LaTeX format.

The complete final compile statistics and PDF SHA-256 are in `APPENDIX_COMPILE_STATUS.json`.
