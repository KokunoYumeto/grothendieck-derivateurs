# ZIP_LIST for DER_FOLLOWUP

Claude Fable 5.2 (effort max), 13 November 2026. `build_zip_20261113.py` (beside this list) reads the table, stages
the files, writes `MANIFEST.tsv` (path in zip, origin, bytes, sha256, why) and builds the upload folder
`<local>/Documents/derivateurs_companion_20261109/pro_prompts_max_20261112/DER_FOLLOWUP/` with two files and
no subfolder: `PROMPT.md` and `DER_FOLLOWUP_background.zip`. The prompt names the paths of the first column.

The zip carries LaTeX, not PDFs: every return and every arXiv paper is attached as TeX source, and the PDFs of the
returns are left out. The only PDFs are the two Isbell–Mitchell papers (journal scans; no source exists).

Roots:
- `ANS` = `<local>/Documents/longue_marche_pro_pilot_20261104/answers`
- `DER` = `<local>/Documents/derivateurs_companion_20261109`
- `REV` = `DER/pro_reviews_max_20261112`
- `CK2` = `DER/pro_prompts_max_20261112_work/TOTAL_EXACT_2/checkpoints/TOTEX2_checkpoint_02_20261113T0350Z_unzipped/TOTEX2`
- `FREE` = `<local>/Documents/Free or receipted/free/arxiv-eprints-der-20261113` (fetched on 13 Nov 2026 from
  `https://arxiv.org/e-print/<id>`; unpacked by `unpack_eprints_20261113.py`)

| Path in zip | Source | Why |
|---|---|---|
| `PRETOT_return/PRETOT_paper.tex` | `ANS/PRETOT_unzipped/PRETOT/PRETOT_paper.tex` | the return PRETOT: A.1–A.5, A.10 (R8), B.2–B.4 (R9), C.1–C.4 (R2, Part A), E.1–E.9 (R10, Part C), F.1–F.12 (R7, R11, Part D) |
| `PRETOT_return/PRETOT_results.csv` | `ANS/PRETOT_unzipped/PRETOT/PRETOT_results.csv` | ids and statuses |
| `PRETOT_return/PRETOT_report.md` | `ANS/PRETOT_unzipped/PRETOT/PRETOT_report.md` | what PRETOT tried on C.4, E.9, F.10 |
| `PRETOT_return/PRETOT_references.bib` | `ANS/PRETOT_unzipped/PRETOT/PRETOT_references.bib` | its sources and access marks |
| `PRETOT_return/code/` | `ANS/PRETOT_unzipped/PRETOT/code/` | programs and certificates of A.5 (model for Part E), path checks (E.8) |
| `PRETOT_REVIEW.md` | `REV/PRETOT_REVIEW_OPUS/REVIEW.md` | the review of PRETOT (statuses of R7–R11, R15) |
| `PRETOT_FINDINGS.md` | `REV/PRETOT_REVIEW_OPUS/FINDINGS.md` | F12, F13 (Lead 4), F15 |
| `TOTEX_return/TOTEX_paper.tex` | `ANS/TOTEX_unzipped/TOTEX_paper.tex` | D.4, D.7, D.9–D.10, D.21–D.26, E.1–E.6 (R5, R6, R7) |
| `TOTEX_return/TOTEX_results.csv` | `ANS/TOTEX_unzipped/TOTEX_results.csv` | ids and statuses |
| `TOTEX_return/TOTEX_report.md` | `ANS/TOTEX_unzipped/TOTEX_report.md` | report of TOTEX |
| `TOTEX_return/TOTEX_references.bib` | `ANS/TOTEX_unzipped/TOTEX_references.bib` | its sources and access marks |
| `TOTEX_REVIEW.md` | `REV/TOTEX_REVIEW_OPUS/REVIEW.md` | the review of TOTEX; the credits to Isbell–Mitchell 1976 (R3, R4, R15) |
| `TOTASPH/TOTASPH_C.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/C.tex` | C.5, C.11–C.13 (R1, R3, R4) |
| `TOTASPH/TOTASPH_D.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/D.tex` | D.12, D.13 (R2, R4) |
| `TOTASPH/TOTASPH_D_followup.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/D_followup.tex` | continuation of Part D |
| `TOTASPH/TOTASPH_D_general.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/D_general.tex` | continuation of Part D |
| `TOTASPH/TOTASPH_F.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/F.tex` | F.9 (sieves and cosieves, R2), F.15 |
| `TOTASPH/TOTASPH_F_followup.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/F_followup.tex` | continuation of Part F |
| `TOTASPH/TOTASPH_results.csv` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/TOTASPH_results.csv` | ids and statuses |
| `TOTASPH/TOTASPH_REVIEW.md` | `REV/2_TOTAL_ASPHERICITY/REVIEW.md` | the check of R1–R4 |
| `PATHS_return/PATHS_paper.tex` | `DER/pro_returns_20261110/6_PATHS/PATHS_paper.tex` | the return PATHS (main file) |
| `PATHS_return/sections/` | `DER/pro_returns_20261110/6_PATHS/sections/` | A.2–A.4, C.P1–C.P3 with proofs (R13, Part B) |
| `PATHS_return/PATHS_results.csv` | `DER/pro_returns_20261110/6_PATHS/PATHS_results.csv` | ids and statuses |
| `PATHS_return/PATHS_references.bib` | `DER/pro_returns_20261110/6_PATHS/PATHS_references.bib` | its sources and access marks |
| `PATHS_intake/REVIEW.md` | `REV/6_PATHS/REVIEW.md` | the intake review of PATHS (R13) |
| `PATHS_intake/FINDINGS.md` | `REV/6_PATHS/FINDINGS.md` | F1 (the check of C.P1–C.P4), F2–F3 |
| `PATHS_intake/SECOND_READING_F2.md` | `REV/6_PATHS/SECOND_READING_F2_20261113.md` | the expert's second reading |
| `TOTAL_EXACT_2/PROMPT.md` | `DER/pro_prompts_max_20261112/TOTAL_EXACT_2/PROMPT.md` | the running prompt: what is not to be done again here |
| `TOTAL_EXACT_2/checkpoint02/TOTEX2_results.csv` | `CK2/TOTEX2_results.csv` | 62 statements of the unfinished run (R12: C.27; R14: C.24, D.1) |
| `TOTAL_EXACT_2/checkpoint02/TOTEX2_report.md` | `CK2/TOTEX2_report.md` | its report at the checkpoint |
| `TOTAL_EXACT_2/checkpoint02/TOTEX2_paper.tex` | `CK2/TOTEX2_paper.tex` | main file of its paper |
| `TOTAL_EXACT_2/checkpoint02/TOTEX2_references.bib` | `CK2/TOTEX2_references.bib` | its sources |
| `TOTAL_EXACT_2/checkpoint02/sections/` | `CK2/sections/` | the proofs: `akr_*.tex` (C.24, for Part A.2), `finite_tests.tex` (C.26, C.27), `statements_sources.tex` (D.1) |
| `LEADS_DERIVATIONS.md` | `DER/pro_prompts_max_20261112_work/DER_FOLLOWUP/LEADS_DERIVATIONS.md` | the drafter's derivations for Leads 1, 2, 3, 5 |
| `ty_check.py` | `DER/pro_prompts_max_20261112_work/TOTAL_EXACT_2/checks_framer/ty_check.py` | the enumeration behind R12 |
| `ty_check.out` | `DER/pro_prompts_max_20261112_work/TOTAL_EXACT_2/checks_framer/ty_check.out` | its output |
| `arxiv/1412.0317_Shoikhet/` | `FREE/1412.0317/src/` | Evrard's path-category factorization of a functor: the literature PRETOT opened for E.9 (Part C); its bibliography gives Evrard 1975 (R16) |
| `arxiv/2205.02353_HackneyOzornovaRiehlRovelli/` | `FREE/2205.02353/src/` | the definition labelled `discretely flat` (R9; Part A.4) |
| `arxiv/math0610668_Charney/` | `FREE/math_0610668/src/` | the Salvetti complex of a right-angled Artin group: the detector of PRETOT F.4 (R7; Part D) |
| `arxiv/1905.12018_Nicholson/` | `FREE/1905.12018/src/` | finite 2-complexes with fundamental group of periodic cohomology: the homotopy type of the example of A.5 (PRETOT_FINDINGS F1; Part E) |
| `arxiv/math0110316_ChacholskiScherer/` | `FREE/math_0110316/src/` | Thomason's theorem and cofinality for homotopy colimits, as used in PATHS C.P3 (Part B) |
| `arxiv/1805.03413_GraySteinberg/` | `FREE/1805.03413/src/` | amalgamated free products of monoids and their classifying spaces; the remark that Lemma 5.2 (a) of Fiedorowicz 1984 does not hold (R16; Part D) |
| `checks_drafter/lead2_walking_retraction.py` | `DER/pro_prompts_max_20261112_work/DER_FOLLOWUP/checks_drafter/lead2_walking_retraction.py` | the program behind Lead 2 |
| `checks_drafter/lead2_walking_retraction.out` | `DER/pro_prompts_max_20261112_work/DER_FOLLOWUP/checks_drafter/lead2_walking_retraction.out` | its output |
| `papers/IsbellMitchell1973.pdf` | `REV/DERIVATEURS_EXPERT/work/lit/IsbellMitchell1973_bull.pdf` | R6; journal scan, no source exists |
| `papers/IsbellMitchell1976.pdf` | `REV/TOTEX_REVIEW_OPUS/papers/IsbellMitchell1976.pdf` | R3, R4, R15; journal scan, no source exists |
| `DER_II-a.tex` | `DER/pro_prompts_max_20261112_work/TOTAL_EXACT/redacted/DER_II-a.tex` | II ms. 36–36ter; the redacted copy made for TOTAL_EXACT |
| `DER_VII-a.tex` | `DER/corrected_french_20261111/DER_VII-a.tex` | VII ms. 25–32 (`Ty`) |
| `DER_VII-b.tex` | `DER/corrected_french_20261111/DER_VII-b.tex` | VII ms. 99–115 (`C_∞ → C`) |
| `DER_XIIb-a.tex` | `DER/corrected_french_20261111/DER_XIIb-a.tex` | XII ms. 88–89, 93–97, 101–103, 109–114 |

## Items that TOTAL_EXACT_2 may settle (for the user's decision when to send)

TOTAL_EXACT_2 is still running. Two items of the prompt are marked `[TOTAL_EXACT_2]`:
- **Part A.2** (PRETOT C.4 for `n = 2`). By Lead 1 it is the question whether a quasi-filtered category with
  `H_2 ≠ 0` exists: Parts C.1 and D.1 of TOTAL_EXACT_2. Its checkpoint 02 already states this (C.24, D.1).
- **Part B.1** (the three lines on `Ty^op`). It is Lead 8 of TOTAL_EXACT_2; its checkpoint 02 lists it as proved
  (C.27, for non-zero rings).

When TOTAL_EXACT_2 has returned and its statements C.24 and C.27 are reviewed: change R12 and R14 to the reviewed
status, delete Part B.1, and replace Part A.2 by "write out the counterexample of Lead 1 (d)". If C.24 does not
survive, Part A.2 stays as it is. Part A.3 (`n ≥ 3`), Parts B.2–B.5, C, D, E do not depend on TOTAL_EXACT_2; Part
D.1 only meets it in the case of a total shape that is not exact, which exists only if its Part A.1 is refuted.

## Notes

- Not attached: the PDFs of the returns (TeX attached); the AKR scan (it belongs to TOTAL_EXACT_2); the programs of
  TOTEX and of the checkpoint (the AKR stages; not needed for these items); `HUNCHES.md` (out of date: H3, H7).
- The closing paragraph has "Take the time the work needs." (the clock sentence was replaced on 13 Nov by
  `claude_tools/prompt_lessons_20261112/clock_line_20261113.py`, here and in the template).
- Second pass of 13 Nov (`patch_prompt_20261113.py`): R16 (literature), a status line under each Lead, Lead 5
  corrected, the program for Lead 2 attached. Backups: `PROMPT_before_lead_checks_20261113.md`,
  `LEADS_DERIVATIONS_before_checks_20261113.md`, `ZIP_LIST_before_checks_20261113.md`.
- Privacy: the build replaces the user's first name by [the user's words, omitted] in text files and removes printed e-mail addresses
  from the `DER_*.tex` files. The arXiv sources keep their authors' published addresses.
