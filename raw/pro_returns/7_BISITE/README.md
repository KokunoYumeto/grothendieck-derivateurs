# BISITE

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

Open BISITE_paper.pdf for the complete mathematics. Its source is
BISITE_paper.tex with included sections. BISITE_results.csv is the exact
statement registry; BISITE_references.bib is the unified, verified-source
bibliography. BISITE_report.md records sources, corrections, computations,
conditional dependencies and remaining tasks.

## Build

With a normal LuaLaTeX installation containing the standard mathematical
packages, fontspec, Latin Modern, apacite and BibTeX, run from this directory:

    lualatex -interaction=nonstopmode -halt-on-error BISITE_paper.tex
    bibtex BISITE_paper
    lualatex -interaction=nonstopmode -halt-on-error BISITE_paper.tex
    lualatex -interaction=nonstopmode -halt-on-error BISITE_paper.tex

Alternatively, code/build_paper.py supports the minimal TeX distribution
used during preparation and records each pass. If that distribution lacks
the Lua font loader, code/prepare_tex.py first downloads its public runtime
packages from official CTAN mirrors into a local cache. The preparation
output records exact download hashes. No system installation is modified.
The standard apacite package supplies APA author-date citations and
references; its runtime is included in the optional preparation step.

## Mathematical checks

Run the certificate suite:

    python code/validate_package.py --checks

The individual programs and their original outputs are retained in code.
The mathematical certificate programs use Python's standard library. The
combined package validator additionally uses Poppler (pdfinfo, pdftotext
and pdffonts). Rendering contact sheets uses Poppler and Pillow.
The source-extraction programs additionally need the original attached
background archive in the sibling background directory; the supplied
copyrighted papers are not duplicated in this return archive. The core
mathematical certificates do not need those source files or network access.
The search code is retained separately from its independent hand-certificate
checker; the exploratory size-six search is not a required reproduction step.

MANIFEST.json gives the SHA-256 digest and byte count of every delivered
file except itself. code/package_artifacts.py recreates the single ZIP and
checks its CRC, member paths and manifest against the actual archived bytes.

## Scope

The paper labels every statement Proved, Refuted, Known or Open. It gives
exact hypotheses, variance, localizer and coefficient conditions. The
conditional implication C.9 above dimension two is not a verification of
the unrefereed 2026 model-structure claim. The four outstanding tasks are
B.21, C.10, D.12 and F.18. All proofs and finite examples remain subject to
independent mathematical review.
