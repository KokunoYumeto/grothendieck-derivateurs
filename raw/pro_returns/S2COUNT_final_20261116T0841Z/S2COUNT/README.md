# S2COUNT research package

The main question is settled negatively, with an optimal six-arrow example. Parts A–D and the requested audits are proved in the paper. The full task is **INCOMPLETE** because the dimension-two resolution cases in E2–E4 remain undecided here. Begin with `S2COUNT_report.md` and `S2COUNT_results.csv` for the exact scope.

## Contents

`S2COUNT_paper.tex` inputs four main section files from `sections/`; that directory also retains independently drafted proof contributions. The compiled LuaLaTeX PDF contains the complete integrated arguments. `S2COUNT_references.bib` records a verification status for every entry; only cited entries appear in the printed bibliography. Exploratory references are not mathematical assumptions. `notes/` preserves proof development and independent audit records. `code/` contains independent finite verification programs and their outputs. `logs/` and `qa/` preserve build and rendering checks. Exact superseded checkpoint versions are retained under `history/`, indexed by content hash in `logs/checkpoint_content_history.json`.

The final archive is `S2COUNT_final.zip`. `code/verify_preservation.py` checks every retained earlier-checkpoint file against its recorded hash; its final result is `logs/final_preservation_check.json`. The two public-source files omitted from later packages are individually identified in the report and provenance index. All authored material is retained.

## Reproduction

Run these commands from this directory:

```sh
python3 code/A_monoid_verify.py
c++ -O2 -std=c++17 code/B_small_categories.cpp -o code/B_small_categories
code/B_small_categories
python3 code/CD_finite_telescope.py
python3 code/E_higman_homology.py
python3 code/CD_E_FDOS_one_pass_check.py
python3 code/CD_E_identity_matrix_counterexample.py
python3 code/CD_E_Jonsson_cycles.py
python3 code/assemble_records.py
bash code/build_paper.sh
```

The Python verification programs use the standard library. The additional normal-subset experiment is explicitly exploratory and does not prove the unresolved group construction. The TeX build script uses LuaLaTeX and BibTeX and creates a private format/font map when the minimal runtime requires it. A normal complete TeX installation may instead use `lualatex`, `bibtex`, `lualatex`, `lualatex` on `S2COUNT_paper`.

For the rendering check, `python3 code/render_pdf_qa.py S2COUNT_paper.pdf qa/current` uses Poppler's `pdftoppm` and Pillow to render every page and prepare numbered contact sheets. Reading the build log and visually inspecting those images are separate checks; rendering alone does not certify layout.

Finite enumeration verifies all multiplication and composition tables in the ranges stated in the paper. It does not establish an infinite homotopy type; the sphere equivalence, resolutions, cardinal arguments and comparisons have separate mathematical proofs.

## Inputs

The user-supplied background archive and source scans are not redistributed. Downloaded public-source copies are also omitted; the bibliography gives their provenance, and the package manifest records excluded input filenames and checksums. All authored proof notes, code, outputs and work records are retained. Checkpoint ZIPs are snapshots of the complete deliverable directory and are never overwritten.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.
