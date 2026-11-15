# TOTEX: the effort-max review of 12 November 2026

Review by Claude Opus 5.5 (Anthropic), effort max, of the return TOTAL_EXACT (TOTEX) of GPT-6 Astra (ChatGPT Pro
mode), 12 November 2026. The return is in [`../../pro_returns/TOTEX/`](../../pro_returns/TOTEX/), the prompt in
[`../../prompts_max_20261112/TOTAL_EXACT/PROMPT.md`](../../prompts_max_20261112/TOTAL_EXACT/PROMPT.md).

- `REVIEW.md`: the verdict on each of the 58 statements, the sources opened, the computations.
- `indep/`: the reviewer's own programs, written from the paper without importing the return's code, with their outputs
  (§5 of the review).
- `rerun/`: the rerun of the return's 14 programs. `rerun/out/` holds the outputs and `COMPARISON.txt`, `RUNLOG.txt`;
  `rerun/tools/` the scripts that ran and compared them. `rerun/code/` holds only the files the rerun wrote that
  differ in content from the return's (the programs themselves are the return's, in `../../pro_returns/TOTEX/code/`);
  the review's `rerun/shipped/`, a copy of the return's shipped outputs, is not repeated here.

Not included:

- the papers by other authors that the reviewer downloaded or read (`papers/` and the scans in `bg/` of the working
  folder): Bojańczyk–Klin–Lasota 2014 (arXiv:1402.0897), Charney–Davis 1995 (author's PDF), Isbell–Mitchell 1976
  (*Exact colimits and fixed points*, Trans. AMS 220), Isbell–Mitchell 1973, Adámek–Koubek–Reiterman 1981,
  Adámek–Rosický–Vitale 2010, Cegarra 2020, Lurie's *Higher Topos Theory*, with their extracted text and page
  renderings. The review cites each at the place used.
- the rest of `bg/`: the background extracted from the prompt's zip (the transcription chunks DER_II-a and DER_XIIb-a,
  the expert's FINDINGS and HUNCHES, the PRETOT paper, two sections of TOTASPH, the review of TOTASPH), all of which
  are published elsewhere in this repository.

In these copies the first name of the user who ran the project is replaced by "user", local paths included. Not
checked by a person; no priority claimed.
