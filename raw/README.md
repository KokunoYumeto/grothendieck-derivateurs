# Raw research outputs on *Les Dérivateurs*

This folder holds raw research outputs, not edited for publication: the answers of GPT-6 Astra (ChatGPT Pro mode)
to eight research prompts on Grothendieck's *Les Dérivateurs*, the reviews of those answers by Claude Fable 5.2, the
prompts with the full list of what was attached to each, the working files that carried the results from one prompt
to the next, and the scripts that built the prompts. [METHODOLOGY.md](METHODOLOGY.md) explains how it was done, return
by return.

- Each paper in `pro_returns/` is AI-produced by GPT-6 Astra (ChatGPT Pro mode). The date of each return is given
  below.
- The reviews in `reviews/` are by Claude Fable 5.2.
- The labels Proved, Refuted, Known and Open are the model's own. The reviews give the verdicts checked so far;
  statements the reviews do not cover are unchecked.
- No priority or novelty is claimed.
- The programs in the returns (the `code/` folders and the other program files) are published as returned, with
  their data and outputs; we have not run them. The reviewers' own programs are in `checks_author/` and `checks/`
  beside each review, with their outputs.
- In these copies the first name of the user who ran the project is replaced by "user", local paths included, and
  e-mail addresses are replaced by "[e-mail address removed]". Nothing else in the files is changed. LaTeX auxiliary
  files, Python caches and compiled binaries are not included. The background zips are not uploaded as zips: their
  contents are listed file by file in `prompts/<name>/ATTACHMENTS.md`, with a link to each of our own files and the
  citation and address of each paper by other authors, which is not re-published here.

To the extent that we hold any rights in these AI-produced texts, they are dedicated to the public domain under CC0 1.0.

## Folders

Dates are those on which the return was received (UTC).

| Folder | What it is | Date | Reviewed |
|---|---|---|---|
| `pro_returns/1_CATHOT/` | Answer to prompt 1: what categories modulo natural transformations can represent | 10 Nov 2026 | yes, twice, and item G.6 a third time (`reviews/1_CATHOT/`) |
| `pro_returns/2_TOTAL_ASPHERICITY/` | Answer to prompt 2: total asphericity, filtered categories, Dwyer-type immersions | 10 Nov 2026 | yes (`reviews/2_TOTAL_ASPHERICITY/`) |
| `pro_returns/3_POLES/` | Answer to prompt 3: the fibration axiom and the cofibration axiom for fundamental localizers | 10 Nov 2026 | yes (`reviews/3_POLES/`) |
| `pro_returns/4_GALOIS/` | Answer to prompt 4: locally constant coefficients and the localizer they define | 11 Nov 2026 | yes (`reviews/4_GALOIS/`) |
| `pro_returns/5_STRATA/` | Answer to prompt 5: small categories as stratified spaces | 11 Nov 2026 | yes (`reviews/5_STRATA/`) |
| `pro_returns/6_PATHS/` | Answer to prompt 6: path categories against the simplicial localization | 11 Nov 2026 | yes (`reviews/6_PATHS/`) |
| `pro_returns/7_BISITE/` | Answer to prompt 7: the two fine localizations, smooth and proper maps, six operations | 11 Nov 2026 | yes (`reviews/7_BISITE/`) |
| `pro_returns/8_RESIDUE/` | Answer to prompt 8: what the first seven answers left undecided | 11 Nov 2026 | not yet |
| `pro_returns/PRETOT/` | Answer to PRESHEAF_TOTALITY (second series): totally aspherical presheaves, Dwyer-type immersions for `W∞` | 12 Nov 2026 | yes (`reviews_max_20261112/PRETOT_REVIEW_OPUS/`) |
| `pro_returns/TOTEX/` | Answer to TOTAL_EXACT (second series): total asphericity against exactness of abelian colimits | 12 Nov 2026 | yes (`reviews_max_20261112/TOTEX_REVIEW_OPUS/`) |
| `pro_returns/TOTAL_EXACT_2_checkpoint_01_20261113T0116Z/` | First checkpoint of the run of TOTAL_EXACT_2, as the model packaged it while still working (not a finished return): the draft paper with its source, the report, the results CSV and the code with its outputs. Raw; nothing in it is checked | 13 Nov 2026 | not yet |
| `pro_returns/DER_READERS_20261112/` | The readers build: six books (French and English; diplomatic, corrected with apparatus, plain reading text) from one annotated master per language, the companion rebuilt with an appendix of new results, and the build records, by GPT-6 Astra (ChatGPT Pro mode); its own README gives our check | 12 Nov 2026 | checked (compilation, privacy, credits, samples); not reviewed |
| `reviews/<name>/` | The review of each answer: `REVIEW_author.md` (and for prompt 1 also `REVIEW.md`, an independent second review, and `REVIEW_G6.md`, a check of item G.6 against the conjecture it refutes; the draft note to the author that it mentions is not included), the reviewer's programs, `PROMPT_UPDATES.md` (what the answer changed in the prompts not yet sent) and `fold_in/` (the inserted sections, with the prompts as they were before) | 10–11 Nov 2026 | — |
| `reviews/7_BISITE/` | Also `COMBINED_REVIEW.md` (the seven answers read together), `FOLLOW_UPS.md` (the open points written as new prompt parts) and `COMPANION_INTEGRATION.md` (what goes into the companion) | 11 Nov 2026 | — |
| `reviews/KNOWLEDGE_HANDOFF.md` | The running record kept by the reviewing sessions, in the order the answers came in | 10–12 Nov 2026 | — |
| `reviews/integration_20261111/` | Working files of the integration of the reviewed results into the critical companion: log, scripts, new commentary blocks, the files as they were before, build logs | 11 Nov 2026 | — |
| `prompts/` | The eight prompts (`<name>/PROMPT.md`), the shared second half of every prompt (`_COMMON_BLOCK.md`), the index of the series (`README.md`), the reading of the companion the prompts came from (`FABLE_PILOT_OVERVIEW_20261110.md`), and for each prompt `ATTACHMENTS.md`, `attached/` (our own attached files not published elsewhere in this repository) and `work/` (background notes, manifest, the record of changes, earlier versions) | 10–11 Nov 2026 | — |
| `tools/` | The script that built prompt 8 and its background zip | 11 Nov 2026 | — |
| `reviews_max_20261112/` | The effort-max reviews and expert files of 12 November: CATHOT, TOTASPH, POLES, GALOIS, the Dérivateurs expert (with `GLOBAL_SHAPE_AFTER_PRETOT_20261112.md` and `GLOBAL_SHAPE_AFTER_TOTEX_20261112.md`, the shape of the companion after each return), the reviews of PRETOT and TOTEX by Claude Opus 5.5, and the intake of PATHS by Claude Fable 5.2 (effort high), each with its own README where it has one | 12 Nov 2026 | — |
| `prompts_max_20261112/` | The second series of prompts, with its own README | 12 Nov 2026 | — |
| `research_maps_20261112/PRETOT_3D_MODULARITY/` | A map from PRETOT Theorem A.5 to Ẑ invariants, 3d modularity, umbral moonshine, the Leech lattice and the Albert algebra (`MAP.md`, Claude Fable 5.2, effort high), and the earlier sketch it supersedes (`TRIAGE.md`); the papers it cites are not included | 12 Nov 2026 | — |
| `translation_aids/` | The glossary (terms, notation, typesetting) and the comparison of translation models for the English *Dérivateurs* and *Longue Marche*, with their own README; the one copy, linked from the repository of *La Longue Marche* | 10–11 Nov 2026 | — |
