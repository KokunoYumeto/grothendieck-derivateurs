# S2COUNT research package

The main question is settled negatively, with an optimal six-arrow example. Parts A–D and the requested audits are proved in the paper. The full task is **INCOMPLETE** because the dimension-two resolution cases in E2–E4 remain undecided here. Begin with `S2COUNT_report.md` and `S2COUNT_results.csv` for the exact scope.

## Contents

`S2COUNT_paper.tex` inputs the four files in `sections/`. The compiled LuaLaTeX PDF contains the complete integrated arguments. `S2COUNT_references.bib` records a verification status for every entry; only cited entries appear in the printed bibliography. Exploratory references are not mathematical assumptions. `notes/` preserves proof development and independent audit records. `code/` contains independent finite verification programs and their outputs. `logs/` and `qa/` preserve build and rendering checks.

## Reproduction

Run these commands from this directory:

```sh
python3 code/A_monoid_verify.py
c++ -O2 -std=c++17 code/B_small_categories.cpp -o code/B_small_categories
code/B_small_categories
python3 code/CD_finite_telescope.py
python3 code/E_higman_homology.py
python3 code/assemble_records.py
bash code/build_paper.sh
```

The Python verification programs use the standard library. The additional normal-subset experiment is explicitly exploratory and does not prove the unresolved group construction. The TeX build script uses LuaLaTeX and BibTeX and creates a private format/font map when the minimal runtime requires it. A normal complete TeX installation may instead use `lualatex`, `bibtex`, `lualatex`, `lualatex` on `S2COUNT_paper`.

Finite enumeration verifies all multiplication and composition tables in the ranges stated in the paper. It does not establish an infinite homotopy type; the sphere equivalence, resolutions, cardinal arguments and comparisons have separate mathematical proofs.

## Inputs

The user-supplied background archive and source scans are not redistributed. Downloaded public-source copies are also omitted; the bibliography gives their provenance, and the package manifest records excluded input filenames and checksums. All authored proof notes, code, outputs and work records are retained. Checkpoint ZIPs are snapshots of the complete deliverable directory and are never overwritten.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.
