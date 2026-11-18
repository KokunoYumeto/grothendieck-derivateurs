# DER_FOLLOWUP

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

Start with `DER_FOLLOWUP_report.md`: its first table gives the outcome of every
Part item and every Lead, including any explicitly unresolved requested subcase.
The working package must not be described as complete while that table contains
an unresolved case.

## Main files

- `DER_FOLLOWUP_paper.tex` and `DER_FOLLOWUP_paper.pdf`: the master manuscript,
  with the full proofs in `sections/`.
- `DER_FOLLOWUP_results.csv`: one row per numbered mathematical statement.
- `DER_FOLLOWUP_references.bib`: annotated opened/not-opened bibliography.
- `DER_FOLLOWUP_report.md`: outcomes, corrections, computations, full source
  access ledger, typesetting checks, and checkpoint preservation.
- `notes/`: proof audits, detailed source/search records and attempted routes.
- `code/` and `code/outputs/`: reproducible verification and retained output.
- `build/`: complete compilation logs, runtime setup, development PDFs and
  rendered page samples. The master PDF is the current mathematical text;
  development PDFs remain historical records.
- `history/`: exact superseded checkpoint files and their SHA-256 manifest.

Attached input files are deliberately excluded. Primary source files fetched
during the work are retained as audit evidence; they are external source
reproductions, not newly authored deliverables.

## Compile with an ordinary TeX installation

From this directory, using LuaLaTeX, BibTeX, and the packages listed in the
master preamble:

```bash
lualatex -file-line-error -interaction=nonstopmode -halt-on-error DER_FOLLOWUP_paper.tex
bibtex DER_FOLLOWUP_paper
lualatex -file-line-error -interaction=nonstopmode -halt-on-error DER_FOLLOWUP_paper.tex
lualatex -file-line-error -interaction=nonstopmode -halt-on-error DER_FOLLOWUP_paper.tex
```

The workspace had an incomplete system TeX installation. A local runtime repair
is therefore included under `build/tex_runtime/`, with exact download URLs,
archive hashes and licenses. If reusing that runtime after extracting elsewhere,
run `python3 code/G_setup_tex.py` to refresh the absolute paths in
`environment.json`, then `python3 code/build_paper.py`. The build script uses the
recorded environment, executes the four commands, retains all logs under a new
timestamp, and checks errors, warnings and overfull boxes. It does not suppress
warnings or alter the mathematical source.

## Mathematical checks

Python 3 is required. The integer linear algebra checks use SymPy. Rendering
uses Poppler (`pdftoppm`) and Pillow; PyMuPDF is used only for inspection helpers.
Run these from any working directory; each writes to `code/outputs/`:

```bash
python3 code/A_cocycle_checks.py
python3 code/B_type_checks.py
python3 code/CD_finite_checks.py
python3 code/CD_freefactor_checks.py
python3 code/E_acts_checks.py
python3 code/F_five_act.py
python3 code/F_strict_composition_check.py
python3 code/G_finite_witnesses.py
python3 code/G_zigzag_bound.py
```

The programs check explicit finite algebra and homology certificates. The full
universal statements, infinite examples and categorical comparisons are proved
in the manuscript; no universal theorem is inferred from bounded enumeration.

`G_manifest_check.py` audits supplied inputs and requires the original background
package beside the workspace. Source-fetch scripts require their recorded
network endpoints. Neither is required to run the mathematical checks above.
The R19 Lean sources were read at the pinned commit; no local Lean execution
is claimed. The project metadata and the Mathlib pull-request state are recorded
separately from what is mathematically used.

## Regenerate the register and report

```bash
python3 code/assemble_register.py
python3 code/F_bibliography_ledger.py
python3 code/assemble_report.py
```

These merge the maintained fragments in `notes/`, verify labels/statuses and
source-access notes, and retain summaries in `code/outputs/`. The report's source
of substantive prose is `notes/report_core.md`.

`render_pdf_qa.py` creates the page images and contact sheets. Visual inspection
is a separate step; the script does not assert that it occurred. The reviewed
manifest gives the exact PDF hashes and pages actually inspected.

`preserve_checkpoints.py` compares existing hourly checkpoint ZIPs beside this
directory with the current files. It retains every changed or missing prior
file byte for byte under `history/checkpoint_NN/` and records the active
replacement. It never creates, overwrites, renames or removes a checkpoint ZIP.
The hourly cadence is controlled separately.
