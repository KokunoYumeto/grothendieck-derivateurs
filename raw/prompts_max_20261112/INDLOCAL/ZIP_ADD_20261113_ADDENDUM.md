# INDLOCAL: addendum to ZIP_ADD_20261113.md (13 November 2026)

Dérivateurs field expert (Claude Fable 5.2, effort max). Written with the Write tool after the context guard
stopped all commands (context at 706k tokens); the two small edits below were prepared and NOT applied.

## State of the upload copy `pro_prompts_max_20261112/INDLOCAL/PROMPT.md`

- The PATHS intake is folded in (R6, R7, R8; Part C with statuses C1–C4 and items C4.1–C4.4; "What is attached";
  rule 5; the header and the task paragraph). Backup of the version before:
  `pro_prompts_max_20261112_work/INDLOCAL/PROMPT_before_paths_intake_20261113.md` (byte-identical copy, checked).
- The closing paragraph was completed to the template's wording ("…extend them as you go, so that an interruption
  loses little.").
- Last lint run, after the last change to the file: `--lint-math` printed `files: 1 failing lint: 0`.
- The script that made the edits: the scratchpad file `indlocal/fold_paths.py` of this session (assert-based
  replacements; it was dry-run on a copy first).

## One more file for `INDLOCAL_new_results.zip`

| Path in zip | Source | Why |
|---|---|---|
| `PATHS_intake/SECOND_READING_F2.md` | `C:/Users/user/Documents/derivateurs_companion_20261109/pro_reviews_max_20261112/6_PATHS/SECOND_READING_F2_20261113.md` | the second reading of F2 (every step followed, no error found; F3 not covered), which R7 of the prompt reports |

## Two edits to the prompt that were not applied (apply them with the zip rebuild, then lint)

1. In R7, replace
   `Second reading (Dérivateurs expert, 13 Nov 2026): F2 followed step by step, no error found;`
   by
   `Second reading (Dérivateurs expert, 13 Nov 2026; ` + "`PATHS_intake/SECOND_READING_F2.md`" + `): F2 followed step by step, no error found;`
2. In "What is attached", in the list of `PATHS_intake/`, after "`IMPLICATIONS.md`," add
   "`SECOND_READING_F2.md`,".

If they are not applied the prompt is still consistent: it reports the second reading without naming the file.

## Correction to ZIP_ADD_20261113.md

`PATHS_intake/scratch/` has 14 files to add (15 in the folder, less the empty `s2cyl_k3.err`); the list was
corrected by a command and says 14.
