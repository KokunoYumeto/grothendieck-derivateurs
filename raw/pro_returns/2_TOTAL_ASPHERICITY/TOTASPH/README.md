# TOTASPH

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Read

TOTASPH_paper.pdf contains Parts A–H. Open means unresolved in this work, not necessarily in the literature. TOTASPH_results.csv has one row per numbered statement, with final numbering and page references. The statement field preserves LaTeX mathematics. TOTASPH_report.md records source reading, calculations, corrections, and limitations. Bibliography notes identify verified and unverified sources.

## Build

From this directory, on a complete TeX Live installation:

~~~sh
mkdir -p build
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build TOTASPH_paper.tex
~~~

Keep sections beside the main source. Packages include fontspec, AMS mathematics, mathtools, microtype, booktabs, longtable, enumitem, natbib, hyperref, tikz-cd, and fancyhdr. Fonts are Latin Modern. No shell escape is required.

The optional code/root_tex_dependencies.py and code/root_build.py repair the original restricted environment using a private TeX tree; they are unnecessary on a normal complete installation. Downloaded packages are not bundled.

## Reproduce mathematical checks

Use Python 3 and SymPy, from this directory:

~~~sh
python code/ag_finite_examples.py
python code/root_monoid_checks.py
python code/root_presheaf_checks.py
python code/cd_affine_simplex.py
python code/cd_affine_polynomials.py
python code/cd_finite_checks.py
python code/f_check.py
python code/f_low_truncation.py
~~~

Saved outputs and complete category tables are in code. Computations corroborate finite instances; universal proofs are in the paper. Source-inspection helpers need the original attachments or network retrieval, Poppler, and occasionally Tesseract; they are provenance records, not prerequisites for mathematical verification.

After editing and compiling:

~~~sh
python code/root_finalize.py --ledger
~~~

The --bibliography option merges source audit records before compilation; --package creates the delivery ZIP after PDF inspection. The PDF-inspection helper uses PyMuPDF and Pillow. The root-level results CSV is authoritative; subsidiary ledgers preserve working audits.

