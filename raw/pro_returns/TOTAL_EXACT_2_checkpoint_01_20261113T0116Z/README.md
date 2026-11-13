# TOTEX2: incomplete interruption checkpoint

The primary research process stopped with an automatic prompt rejection.
This checkpoint preserves verified proofs and the exact unresolved steps.
It does **not** solve the main implication, the universal triple assertion,
the individual field implications, or the all-stage AKR persistence claim.

Start with `TOTEX2_report.md`. Its first line is `INCOMPLETE`; its outcome
table covers every requested item and all nine leads. `TOTEX2_paper.pdf`
contains the integrated mathematical record, and `TOTEX2_results.csv`
has exactly one row for each numbered statement. The marked bibliography
distinguishes opened mathematical texts from bibliographic records only.

## Rebuild the paper

From the extracted package root:

```sh
python code/build_pdf.py
```

This needs a TeX Live installation with LuaLaTeX, BibTeX, Latin Modern,
AMS packages, natbib, hyperref, microtype, geometry, booktabs, longtable,
mathtools, enumitem and array. On an ordinary complete installation it
uses the installed format. The optional workspace bootstrap writes only
inside `.build/`, supplies a local Type 1 variant of the installed LaTeX
kernel, and does not alter system configuration. Compilation and reference
checks are recorded under `code/outputs/`.

`code/literature_harness_check.py` and its output retain an earlier failed
XeLaTeX format check. That failure was a toolchain issue before TeX-source
processing. It is superseded by the successful integrated LuaLaTeX build.
Other historical build logs are retained as execution records.

## Mathematical checks

```sh
python code/check_delta_patterns.py
python code/topology_ty_verify.py
python code/topology_akr_component_probe.py
```

The first two programs use the Python standard library. The third uses
the included `topology_akr_reference.py`, an explicitly attributed copy
of the supplied independent review implementation. The finite scope and
enumeration counts appear in each output and the report. No finite check
is used as proof of a universal-stage or all-actions statement.

`topology_akr_ocr.py` requires PyMuPDF and Tesseract, plus the original
background archive extracted to `../background/`. It creates source
inspection intermediates under `work/akr_ocr/`. The source-retrieval
programs require network access and save downloaded texts under
`work/sources/`. Neither full downloaded source texts nor OCR page images
are included in this checkpoint. The original user attachments remain
the source for background material.

## Rebuild the index and verify the artifacts

`build_results_report.mjs` authors and inspects the requested seven-column
CSV using the `@oai/artifact-tool` package. It requires Node.js and that
package in the module search path. In the original workspace the runtime
was supplied through `CODEX_PRIMARY_RUNTIME_NODE` and
`CODEX_PRIMARY_RUNTIME_NODE_MODULES`; the dependency link itself is omitted
from the ZIP. The CSV and report are already present and need no runtime
to read. Regenerate them after rebuilding the PDF, so that page numbers
come from the current LaTeX labels:

```sh
node code/build_results_report.mjs
python code/verify_package.py
```

The verifier requires PyMuPDF, Pillow, and Poppler's `pdftoppm`. It checks
the exact CSV schema, theorem coverage, open-statement status, report
coverage, PDF text bounds, and LaTeX diagnostics, then renders every page
under a sibling `tmp/totex2_pdf_qa/` directory. The final visual review is
recorded separately in `code/visual_review.json`.

`sync_recovery_fragments.py` is a recovery-maintenance record. It needs
the original sibling `TOTEX2` working tree and is not required to rebuild
or use this standalone checkpoint. `package_checkpoint.py` creates the
archive and its content manifest. No previous saved checkpoint is replaced.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026.
No claim of priority.
