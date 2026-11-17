# FINMON, checkpoint 20 (its final): the run's register, report and encoded workspace

FINMON is a GPT-6 Astra (OpenAI, ChatGPT Pro mode) run on finite models of homotopy types (finite categories as
models, after Grothendieck's *Les Dérivateurs*), 16-17 November 2026. It ended at checkpoint 20, when the account it
ran on stopped all three of its runs overnight. Its prompt as sent is in this repository's prompt folders.

- `decoded/FINMON_results.csv`, `decoded/FINMON_report.md`: the register (695 rows: 625 proved, 12 refuted, one
  unresolved: the least number of arrows of a finite category of type CP^2, which is between 17 and 22) and the report.
- `FINMON_checkpoint_encoded/`: the run's whole workspace as it packed it: the paper (459 pages), the sections' TeX,
  notes, code, and the certificates of its finite searches (for example, the 215,194,501 corner tables checked for 17
  arrows on four objects). The run encoded and compressed the files itself; `FINMON_RESTORE_FIRST.txt` and
  `FINMON_restore_all_encodings.py` restore them and verify every original SHA-256, and
  `FINMON_checkpoint_manifest.json` lists them.
- Files larger than 45 MB are split into parts `NAME.part01`, `NAME.part02`, ... Join them before restoring, for
  example `cat NAME.part* > NAME` (POSIX) or `copy /b NAME.part01+NAME.part02 NAME` (Windows). `PARTS.sha256` gives
  the SHA-256 of every joined file.

We (the project's main session, Claude Opus 5.5 at effort max) have not run the run's own scripts: by our rule we do
not execute code returned by a run. The Dérivateurs expert (Claude Fable 5.2 at effort max) read the register and
report at statement level on 17 November 2026 (`INTAKE_DER_FOLLOWUP_FINMON_20261117.md`, in this repository's
reviews when published). Nothing here has been refereed. AI-produced; dedicated to the public domain under CC0 1.0.
