# CATHOT

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).** 10 November 2026. No priority is claimed.

This archive contains the complete audit of Parts A–G in the supplied CATHOT prompt. The paper distinguishes proofs, refutations, cited known inputs, and exact questions not settled by this audit. Its 90 numbered assertions comprise 59 Proved, 14 Refuted, 11 Known, and 6 Open assertions. These status labels do not constitute independent human certification of the proofs.

## Main files

| File | Content |
|---|---|
| `CATHOT_paper.pdf` | The paper, produced with LuaLaTeX. |
| `CATHOT_paper.tex`, `sections/`, `CATHOT_paper.bbl` | Complete typesetting sources and generated bibliography. |
| `CATHOT_results.csv` | One row per numbered assertion, with its full statement, status, proof location, dependencies, manuscript locations, and notes. |
| `CATHOT_references.bib` | Bibliography with verified/unverified annotations. |
| `CATHOT_report.md` | Source audit, corrections, computation scope, searches, and unresolved questions. |
| `code/` | Authored computations, scripts, outputs, final compilation evidence, and environment diagnostics. |
| `research/` | Authored contribution metadata and audit notes needed to reproduce assembly. Complete third-party papers are excluded. |
| `ARCHIVE_MANIFEST.json` | SHA-256 hashes of the archive's other members. |

## Unresolved assertions

The six Open identifiers are D.6 (sequential finite-category tests for S²), E.6 (strict retraction preserving the same Cat hot class under fibrancy), E.17 (invariant small ind-objects and groupoid-stage presentations), E.26 (fully quantified general path-type comparison systems), E.27 (general relative path concatenation), and G.17 (remaining realization and RP²-poset arrow questions). Each assertion records the proved range and the precise missing step. “Open” means unsettled in this audit, not a verified claim of literature-wide openness.

## Reproduction

With Python, SymPy, PyMuPDF, Pillow, and a normal TeX Live installation providing LuaLaTeX, BibTeX, fontspec, natbib, and the packages named in the source, run from this directory:

```bash
python code/assemble.py
python code/build.py
python code/assemble.py
python code/validate_package.py
```

The second assembly adds final PDF page numbers to the CSV. Computations are separate scripts; their recorded outputs state their exact scope. The expensive exhaustive enumeration is not required to rebuild the paper. `code/render_pdf_qa.py` renders every page into a sibling directory for layout inspection.

The authoring environment initially had an incomplete TeX installation. `code/setup_lualatex.py` and `code/run_with_tex.py` document the workspace-only repair used for the final build. They are optional on a normal installation; their diagnostic configuration records authoring paths. Historical failed build logs are retained under clearly named files or `code/build_history/`; `code/build_final.out`, `code/build_pass_4.out`, and `code/final_lualatex.log` identify the final successful build.

Some source-preparation and retrieval scripts require the original supplied background archive or network access to the exact primary-source URLs they record. Those inputs are not silently replaced by the companion's assertions. The recent Ben-Bassat finite-monoid realization theorem and the external order-five/order-six monoid classification are explicitly cited Known dependencies; their entire proofs or searches are not claimed to have been independently repeated here.
