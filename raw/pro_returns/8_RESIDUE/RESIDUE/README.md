# RESIDUE research package

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026.
No priority is claimed.

This is a substantive, explicitly incomplete answer to the attached ten-part
research request. Read the scope statement on the paper's first page and the
exact outstanding-obligation table in `RESIDUE_report.md`. The `Open` status
means that this return has not settled the stated obligation; it is not a claim
that the literature contains no answer.

## Main files

| File | Contents |
|---|---|
| `RESIDUE_paper.tex`, `RESIDUE_paper.pdf` | The paper, in Parts A–J, with numbered status labels and proofs |
| `RESIDUE_results.csv` | One row per numbered statement, with the seven requested columns |
| `RESIDUE_references.bib` | Author–date bibliography; every record states verification scope |
| `RESIDUE_report.md` | Source audit, corrections, computations, and exact unresolved obligations |
| `sections/` | Included TeX sections, authoring fragments, register metadata, and detailed audit logs |
| `sections/BC_historical_audit.csv` | Statement-by-statement historical audit |
| `tables/D_BISITE_B15.csv` | All 48 reconstructed scalar entries in the inherited eight-map table |
| `code/` | Mathematical programs, finite certificates, tables, and recorded outputs; document build and verification programs |
| `MANIFEST.sha256` | SHA-256 checksums of the packaged files other than the manifest itself |

The supplied background archive and downloaded literature are not
redistributed. Intermediate literature extractions and compiled binaries are
excluded. The mathematical program sources and their completed output tables
are included.

## Requirements

The mathematical computations use Python 3.12 and SymPy 1.14.0. The monoid
enumerator uses a C++17 compiler. The PDF uses LuaLaTeX, BibTeX, latexmk, and
standard TeX Live packages: geometry, Latin Modern, AMS, mathtools, mathrsfs,
booktabs, longtable, enumitem, needspace, natbib, microtype, hyperref, and xcolor. PDF
quality checks additionally use Poppler (`pdfinfo`, `pdffonts`, `pdftoppm`),
Pillow, and pypdf. The Python dependency versions used are recorded in
`code/root/runtime_versions.json`.

## Rebuild the paper

From the extracted `RESIDUE` directory:

```sh
python3 code/root/assemble.py
python3 code/root/build_pdf.py
```

The first command deterministically assembles the source fragments, reference
records, result register, and report. It checks that numbered statements and
register rows agree and that all citation keys resolve. The second command
runs LuaLaTeX/BibTeX through latexmk and writes an explicit build-status record.
On a complete TeX installation the ordinary alternative is:

```sh
latexmk -lualatex -interaction=nonstopmode -halt-on-error RESIDUE_paper.tex
```

The paper deliberately uses embedded Type 1 Latin Modern and mathematical
fonts. The supplied runtime lacked the standard LuaLaTeX format index, so the
build script creates a local format cache when necessary. Its missing optional
OpenType loader emits a startup fallback notice in that runtime; the final
build log and status record retain that notice. This does not supply or claim
OpenType support. There are no undefined controls, unresolved citations,
missing characters, or overfull boxes in the delivered PDF.

## Reproduce the mathematical computations

Run the following from the directory **containing** the extracted `RESIDUE`
directory. The C++ enumerator's output path is relative to that directory.
All Python programs locate their main output beside their own source.

```sh
g++ -O3 -std=c++17 RESIDUE/code/AE/monoids.cpp -o RESIDUE/code/AE/monoids
RESIDUE/code/AE/monoids 2> RESIDUE/code/AE/monoids_run.txt
python3 RESIDUE/code/AE/monoid_classification.py > RESIDUE/code/AE/monoids_classification_run.txt
python3 RESIDUE/code/AE/path_chain.py > RESIDUE/code/AE/path_chain_run.txt
python3 RESIDUE/code/AE/chain_closure_check.py > RESIDUE/code/AE/chain_closure_check_run.txt
python3 RESIDUE/code/AE/relative_posets.py > RESIDUE/code/AE/relative_posets_run.txt
python3 RESIDUE/code/AE/verify_certificates.py > RESIDUE/code/AE/verification_run.txt
python3 RESIDUE/code/AE/core_fundamental_groups.py > RESIDUE/code/AE/core_fundamental_groups_run.txt
python3 RESIDUE/code/AE/complete_homotopy_table.py > RESIDUE/code/AE/complete_homotopy_table_run.txt
python3 RESIDUE/code/AE/transient_probe.py > RESIDUE/code/AE/transient_probe_run.txt
python3 RESIDUE/code/BC/verify_counterexamples.py
python3 RESIDUE/code/root/verify_D.py > RESIDUE/code/root/D_stdout.txt
python3 RESIDUE/code/root/verify_F.py > RESIDUE/code/root/F_stdout.txt
python3 RESIDUE/code/root/verify_coverings.py > RESIDUE/code/root/coverings_stdout.txt
python3 RESIDUE/code/GHIJ/small_counterexamples.py
python3 RESIDUE/code/GHIJ/marked_curve_lifts.py
python3 RESIDUE/code/GHIJ/finite_poset_direct_image.py --max 5 > RESIDUE/code/GHIJ/finite_poset_direct_image_max5.log
```

`code/root/finite_categories.py` is an imported exact helper. The document
metadata utility `code/BC/update_register.py` updates the B/C working register
and historical audit; its outputs are the corresponding files in `sections/`.

The finite-poset direct-image program tests all maps between representatives,
without quotienting maps by isomorphism. The relative-path catalogue tests
fixed alternating words of lengths 2, 4, and 6. It does **not** enumerate the
full category of all word shapes of length at most six. Neither the complete
pseudo-action search in A(6) nor the monoid/presheaf search in F(2) was
performed. No object-bounded exhaustive enumeration of all finite categories
with unbounded arrow counts is claimed.

Universal assertions are proved in the paper. Passing a finite suite is not
used as a universal pullback, localization, or homotopy theorem.

## Provenance and final checks

The original prompt and archive hashes, and verification of all 431 background
manifest members, are in `code/root/input_provenance.json`. To reproduce that
input audit, place the original uploads in the adjacent `upload/` directory
and their extraction in the adjacent `background/` directory, then run
`python3 RESIDUE/code/root/input_manifest_audit.py`.

From inside `RESIDUE`, the following programs render page contact sheets,
validate the package, and create the ZIP in the parent directory:

```sh
python3 code/root/pdf_quality.py
python3 code/root/package.py
```

Page images are checked visually in addition to text, font, and build-log
checks. The visual-inspection record is in `code/root/pdf_visual_audit.json`.
The checksum manifest and ZIP can be regenerated; rebuilding outputs changes
their checksums and requires regenerating the manifest.
