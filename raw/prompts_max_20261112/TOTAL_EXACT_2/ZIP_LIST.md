# ZIP_LIST for TOTAL_EXACT_2 (for the collector who builds the zip)

Claude Fable 5.2 (effort max), 12 November 2026. Every source path below was checked to exist at 23:40 local time.

Upload folder to create: `user/Documents/derivateurs_companion_20261109/pro_prompts_max_20261112/TOTAL_EXACT_2/`
with two files and no subfolder: `PROMPT.md` (copy of the `PROMPT.md` beside this list) and
`TOTAL_EXACT_2_background.zip`. The prompt names the zip and the paths inside it exactly as in the first column.
`MANIFEST.tsv` goes at the root of the zip (path in zip, origin, bytes, sha256, why), as in the other packages.

Roots used below:
- `ANS` = `user/Documents/longue_marche_pro_pilot_20261104/answers`
- `DER` = `user/Documents/derivateurs_companion_20261109`
- `REV` = `DER/pro_reviews_max_20261112`

| Path in zip | Source | Why |
|---|---|---|
| `TOTEX_return/TOTEX_paper.tex` | `ANS/TOTEX_unzipped/TOTEX_paper.tex` | the return: all statements cited as A.1–F.5 |
| `TOTEX_return/TOTEX_paper.pdf` | `ANS/TOTEX_unzipped/TOTEX_paper.pdf` | the same, typeset |
| `TOTEX_return/TOTEX_results.csv` | `ANS/TOTEX_unzipped/TOTEX_results.csv` | ids and statuses |
| `TOTEX_return/TOTEX_report.md` | `ANS/TOTEX_unzipped/TOTEX_report.md` | what was tried on Part A; the AKR schedules |
| `TOTEX_return/TOTEX_references.bib` | `ANS/TOTEX_unzipped/TOTEX_references.bib` | sources and their access marks |
| `TOTEX_return/code/` (whole tree, 56 files) | `ANS/TOTEX_unzipped/code/` | the AKR stage programs and outputs (R10), `akr_REPRODUCE.md` |
| `TOTEX_REVIEW.md` | `REV/TOTEX_REVIEW_OPUS/REVIEW.md` | the review; section 6 is the state of Part A; F2, F4, F5, F6, F11, F13, F14 |
| `TOTEX_review_code/` (12 files) | `REV/TOTEX_REVIEW_OPUS/indep/` | reviewer's independent AKR construction, down-set homology, triple equalizers (R10, F11) |
| `TOTAL_EXACT_PROMPT.md` | `DER/pro_prompts_max_20261112/TOTAL_EXACT/PROMPT.md` | the prompt TOTEX answered |
| `papers/IsbellMitchell1973.pdf` | `REV/DERIVATEURS_EXPERT/work/lit/IsbellMitchell1973_bull.pdf` | R2, R3 |
| `papers/IsbellMitchell1976.pdf` | `REV/TOTEX_REVIEW_OPUS/papers/IsbellMitchell1976.pdf` | R2, R4, R5; the question at p. 298; TOTEX did not have it |
| `papers/AdamekKoubekReiterman1981.pdf` | `REV/DERIVATEURS_EXPERT/work/lit/AKR1981.pdf` | R10; Part C.1 (scan, no text layer) |
| `TOTASPH/TOTASPH_C.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/C.tex` | proofs of C.5, C.6, C.9–C.13 (R1–R5) |
| `TOTASPH/TOTASPH_D.tex` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/sections/D.tex` | D.4, D.7, D.16–D.18 |
| `TOTASPH/TOTASPH_results.csv` | `DER/pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/TOTASPH_results.csv` | ids |
| `TOTASPH/TOTASPH_REVIEW.md` | `REV/2_TOTAL_ASPHERICITY/REVIEW.md` | the check of R1–R5 |
| `PRETOT/PRETOT_paper.tex` | `ANS/PRETOT_unzipped/PRETOT/PRETOT_paper.tex` | Definition E.1 of `Ty`; F.3, F.6, F.12 (R6, Lead 8) |
| `PRETOT/PRETOT_results.csv` | `ANS/PRETOT_unzipped/PRETOT/PRETOT_results.csv` | ids |
| `PRETOT/PRETOT_REVIEW.md` | `REV/PRETOT_REVIEW_OPUS/REVIEW.md` | the check of E.1, F.3, F.6, F.12 |
| `PRETOT/PRETOT_FINDINGS.md` | `REV/PRETOT_REVIEW_OPUS/FINDINGS.md` | F12 (`Ty^op`) |
| `HUNCHES.md` | `REV/DERIVATEURS_EXPERT/HUNCHES.md` | H1: the class `κ` of Lead 5 |
| `ty_check.py` | `DER/pro_prompts_max_20261112_work/TOTAL_EXACT_2/checks_framer/ty_check.py` | the enumeration behind Lead 8 |
| `ty_check.out` | `DER/pro_prompts_max_20261112_work/TOTAL_EXACT_2/checks_framer/ty_check.out` | its output |
| `DER_II-a.tex` | `DER/pro_prompts_max_20261112_work/TOTAL_EXACT/redacted/DER_II-a.tex` | II ms. 36–36ter; the redacted copy already made for TOTAL_EXACT |
| `DER_XIIb-a.tex` | `DER/corrected_french_20261111/DER_XIIb-a.tex` | XII ms. 88–89, 112–113 |
| `DER_VII-a.tex` | `DER/corrected_french_20261111/DER_VII-a.tex` | VII ms. 25–32 (`Ty`); see the note on redaction |

Notes for the build.
- `DER_VII-a.tex` contains one printed e-mail address (as `DER_II-a.tex` did): replace it by
  `[e-mail address removed]` in the copy that goes into the zip, as the TOTAL_EXACT build did for `DER_II-a.tex`.
- Run the usual privacy scan on the text files. The six Markdown files I looked at (the two reviews, the findings,
  `HUNCHES.md`, the TOTASPH review, `TOTEX_report.md`) do not contain the user's name.
- The three PDFs in `papers/` are binary and were not scanned by me. Isbell–Mitchell 1976 comes from ams.org (open
  access); the other two were in the TOTAL_EXACT zip.
- Not to attach: `REV/TOTEX_REVIEW_OPUS/bg/` and `rerun/` (copies of the TOTAL_EXACT zip and identical reruns);
  Lurie's *Higher Topos Theory*, Adámek–Rosický–Vitale, Cegarra, Charney–Davis, Bojańczyk–Klin–Lasota (the results
  that used them are settled and are cited from TOTEX); `_COMMON_BLOCK.md` (the prompt carries its own rules; the
  common block has the old rule 8).
- Not obtained by anyone on our side and named as such in the prompt: Oberst 1968, Gabriel–Ulmer 1971, Isbell 1968,
  Isbell 1974. If one of them is obtained before the prompt is sent, add it under `papers/` and change the
  paragraph "Not attached" of the prompt.
- Uncompressed total: about 5.2 MB.
