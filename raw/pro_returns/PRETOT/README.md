# PRETOT research package

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

## Deliverables

`PRETOT_paper.pdf` is the complete mathematical paper in Parts A–G. `PRETOT_paper.tex` is its self-contained LuaLaTeX source, including the formatted reference list. `PRETOT_references.bib` gives the same bibliography in machine-readable form, with opened/not-opened verification notes. `PRETOT_results.csv` has exactly one row per numbered statement. `PRETOT_report.md` records the source audit, computations, corrections, search bounds, and residual questions. The main result is a finite universal counterexample to Part A, labelled `A:counterexample` in the source and ledger.

The `code` directory contains the exact checkers, the complete finite multiplication/action data, the integer splitting matrices, and their outputs. Files in `code/outputs` are the recorded results, not inputs requiring network access. All paths used by the mathematical checkers are relative to their own script directory.

## Requirements

The mathematical programs require Python 3 and SymPy. No SageMath, GAP, floating-point linear algebra, external database, or network connection is required. The code uses only the standard library and SymPy. The PDF requires LuaLaTeX with the standard article, AMS, Latin Modern, microtype, geometry, enumitem, natbib, hyperref, and fancyhdr packages.

## Mathematical reproduction

Run the generator first. The two independent readers do not import its implementation; they inspect the generated integer JSON certificate.

```bash
python code/main_counterexample.py
python code/audit_certificate.py
python code/independent_projectivity_check.py
python code/quotient_action_tests.py
python code/bounded_search.py
python code/check_truncated_composition.py
python code/check_sieve_examples.py
python code/path_checks.py
python code/diagram_tests.py
python code/semisimplicial_affine_checks.py
python code/appendix_gluing_check.py
```

These commands may be called from any working directory by replacing each script path with its absolute path. Every program prints its result and/or saves its deterministic report in `code/outputs`. The two main generated input files are `main_counterexample_data.json` and `projectivity_certificate.json`. No finite action test is claimed to prove the universal totality property: the theorem uses the projective module splitting, and the finite checks verify that splitting.

The bounded search covers labelled monoids of order at most four with right acts of size at most three, and ordered one-way categories with at most seven arrows including identities and presheaves with each value at most two and total size at most four. The absence result comes from full fundamental-group presentations; it is not an assertion of higher acyclicity based on a truncated nerve.

## PDF and result ledger

On a complete TeX Live installation:

```bash
lualatex -interaction=nonstopmode -halt-on-error PRETOT_paper.tex
lualatex -interaction=nonstopmode -halt-on-error PRETOT_paper.tex
lualatex -interaction=nonstopmode -halt-on-error PRETOT_paper.tex
python code/assemble_results.py
```

The source does not require BibTeX: its APA-style reference list is embedded. The separate `.bib` file is supplied for reuse and provenance.

Alternatively, `python code/build_pdf.py` performs three LuaLaTeX passes and checks the final log for errors, undefined references/citations, duplicate labels, and overfull boxes. On the source-only TeX environment used here it also bootstraps a local format and font map under `.build`, using the installed Type 1 fonts. Its explicitly named local Type 1 kernel variant removes only the unavailable OpenType-loader startup; the paper and other kernel startup code are unchanged. This fallback changes no system files and downloads nothing. A normal complete TeX installation uses its ordinary format.

After a rebuild, `python code/assemble_results.py` checks the statement/metadata bijection and updates the CSV with the displayed theorem numbers and PDF start pages. `code/result_metadata.json` contains the human-reviewed statements, dependencies, manuscript locations, and limitations.

## Interpretation of verification

“Machine checked” means exhaustive checks of the specified finite structures or exact integer identities by these programs. It does not mean a formal proof-assistant development. The universal categorical and topological assertions are proved in the paper. The computation bounds, inaccessible article bodies, and unsolved auxiliary assertions are retained explicitly in the report.
