# *Les Dérivateurs*: six readers, French and English, each in three forms, and an appendix of new results

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Three ZIP files are attached. Each has
`MANIFEST.tsv` at its root (path in the zip, original path, bytes, SHA-256, role); read the manifests first.

## What this is for

Grothendieck's *Les Dérivateurs* (1990–91) was edited by M. Künzer, J. Malgoire and G. Maltsiniotis. That edition is
the text, and our transcription of it is in LaTeX:
- 243 units of five edition pages each, 1,176 edition pages in all;
- an English translation (GPT-6.1 Sol, effort max);
- a companion book, with tables of corrections for every part.

What is missing is the readers: finished books, one per form and language, that carry every correction and say
exactly what was changed. One further piece is missing too: an appendix to the companion that collects the results
proved along the way that we did not find in the literature. You build both, by script and diff. The French and
English texts are about a million tokens each, so do not read them whole: work from the records, and look at the text
wherever a decision needs it.

## The six readers

Build one book per form and language, each a single LaTeX file that compiles with LuaLaTeX:

| File | Language | Form |
|---|---|---|
| `DER_FR_diplomatique.tex` | French | **Diplomatic**: the edition as printed, its slips kept (the `% [sic]` places), the editors' notes kept and marked as theirs, the edition's and the manuscript's page numbers marked |
| `DER_FR_corrige_apparat.tex` | French | **Corrected, with apparatus**: the slips of the edition corrected; every place where it differs from the print is marked, and the apparatus gives the printed reading, the correction and its source; the editors' notes kept and marked as theirs |
| `DER_FR_texte_de_lecture.tex` | French | **Plain reading text**: the corrected text with no apparatus and none of the editors' notes. The only exception is a neutral sign where text is missing or illegible. The page numbers are in the margin only, and a short preface says what was left out |
| `DER_EN_diplomatic.tex` | English | **Diplomatic**: the English as published, which follows the French as printed |
| `DER_EN_corrected_apparatus.tex` | English | **Corrected, with apparatus**: the same corrections, wherever they change the English |
| `DER_EN_reading.tex` | English | **Plain reading text**: as for the French |

**Build all three forms of a language from one annotated master.** Mark every place where the print and the
corrected text differ, for instance with a macro `\var{printed reading}{corrected reading}{source id}`, and generate
the three forms from that master by switching the macro. The forms then cannot drift apart.

## Sources of record

- **French** (ZIP 1, `transcription/`): the 243 units at commit f42cfdd (release v2026-11-11b). Also there are the
  23 edition-file masters, the book master `LesDerivateurs_transcription.tex` with its Lua loader, and
  `DECISIONS.md`/`.json` (435 hunks; the 10 macro corrections; the 5 listed corrections overruled against the edition).
  The text carries these layers:
  - editors' notes `\texttt{[...]}` (818);
  - manuscript page anchors `\msp{...}` (2,266);
  - edition page anchors `\printedpage` (1,419);
  - footnotes (1,432);
  - slips of the edition kept as printed, `% [sic]` (899);
  - doubtful readings, `% ??` (20).
- **Corrections** (ZIP 1):
  - `companion_corrections/DER_<part>_corrections.csv` (2,135 rows; columns pdf_page, place, transcription_reads,
    should_read, kind, evidence).
    - The rows of kind `transcription` (134) and `doubt_resolved` (122) are already carried into the transcription,
      except the 5 overruled ones.
    - **The 1,879 rows of kind `edition_slip_kept` are the corrections of the corrected forms.**
  - `corrected_french_20261111/`: the 32 corrected parts from which the corrections were carried into the
    transcription. It is input, not the source of record.
- **English** (ZIP 2): `translation/`, the 243 English units (with the 41 fixes of `checks/FIXES.jsonl` applied). Also
  in ZIP 2:
  - `reader/LesDerivateurs_English.tex` (910 pages, 0 LaTeX errors);
  - `checks/` (FIXES, WAIVERS, REPORT, FORMULAS_NOT_IDENTICAL, completeness flags) and `COMPLETENESS_20261112.csv`
    (50 gaps: 26 fixed, 24 kept);
  - `scripts/` (build_reader.py, assemble.py, common_dt.py: the English units' own macro changes).
- **Companion and new results** (ZIP 3):
  - `companion/reader/`: the companion book at f42cfdd, with its 32 parts, `.bib` and `OVERLAPS.md`.
  - `companion/kit/`: its build scripts and style.
  - `NEW_RESULTS.md` and the proof files it cites (`pro_reviews_max_20261112/…`, `pro_returns_cited/…`).
  - `conventions/`: `GLOSSARY_DER.csv` (171 entries), `NOTATION_DER.csv` (26) and `TYPESETTING.csv`.

## Rules

1. **The editors' text is theirs.** Künzer, Malgoire and Maltsiniotis made the edition.
   - Their notes stay in the diplomatic and corrected forms, marked as theirs and distinct from our apparatus. Never
     reword them and never present them as ours.
   - The plain reading text leaves them out, except a neutral sign where text is missing or illegible, and its
     preface says so.
   - About 17 of their notes report passages Grothendieck struck out ("barré", "biffé", "rayé"). The struck words
     themselves are mostly not transcribed. The plain text drops these notes too, and keeps everything else.
2. **Corrections.**
   - **Apply every `edition_slip_kept` row in the corrected French**, each with an apparatus entry. Merge rows that
     repeat a place across parts.
   - Where two rows disagree, or where a correction is plainly wrong on the text, decide with a reason and record it in
     `CORRECTIONS_DECIDED.tsv`. A correction you reject stays out of the text and goes into that table.
   - The English corrected form applies the same corrections wherever they change the English.
   - Fix the three known LaTeX errors in every form:
     - XIIc p. 61–64 (a tikz-cd arrow to an empty cell; the English unit has the fix);
     - XIV p. 11 (`\mathllap` without mathtools);
     - XV p. 31–35 (a `#` error in the footnote macro).
3. **Terms and notation.** Keep Grothendieck's and the edition's notation in every form.
   - Check the English against `GLOSSARY_DER.csv`, `NOTATION_DER.csv` and `TYPESETTING.csv` (made by Claude Fable 5.2
     on 10 Nov), and apply them where the English departs from them.
   - Where you judge an entry wrong, do not apply it. List it in `GLOSSARY_FLAGGED.tsv` with your reason and the
     rendering you propose.
   - Record every English change in the change log.
4. **The companion** is the repository's book at f42cfdd, as shipped. Changes made on 11 Nov from an earlier review
   folder are superseded and are not in the upload; do not look for them.
5. **The appendix of new results.** Write `appendix_new_results.tex`, a chapter for the companion titled "Results
   proved along the way that we did not find in the literature". It has one section per entry of `NEW_RESULTS.md`
   (12 entries). Each section gives:
   - the statement, exactly;
   - the proof, taken from the cited file and edited for reading but not changed in substance;
   - where it bears on the manuscript, with the pages;
   - who proved it and who checked it, as NEW_RESULTS gives them;
   - one paragraph of your own reading: whether the proof as written is complete, and where it has a gap. Label it as
     GPT-6 Astra's reading; it is not the separate peer review that will follow.

   Open the chapter with NEW_RESULTS's own framing: no priority is claimed, our search was limited, and readers who
   know a reference are asked to tell us. End it with the list of statements found to be known, with their
   references. The reviews at effort max of the returns STRATA, PATHS, BISITE and RESIDUE do not exist yet. Nothing
   from those returns enters the appendix beyond what NEW_RESULTS lists. Add the `\input` of the appendix to the
   companion master, and rebuild the companion book.
6. **Credit and rights.** Each reader's front matter carries:
   - Grothendieck as author;
   - the Künzer–Malgoire–Maltsiniotis edition as the edition transcribed;
   - every credit the repository README gives (`repo/README.md`, `repo/RIGHTS_NOTICE.md`);
   - for the English, "translated by GPT-6.1 Sol (OpenAI, effort max)";
   - the wording "AI-transcribed", "AI-translated" and "AI-produced corrections", never "AI-assisted";
   - this rights statement, in the reader's language: "The rights in the original work belong to its author or the
     author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation,
     corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for
     educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and
     object to its publication here, please open a GitHub issue and we will take it down."

   Credit this build to GPT-6 Astra (OpenAI, ChatGPT Pro mode).
7. **Privacy.** The editors' e-mail addresses were replaced by `[e-mail address removed]`; keep it so. Some records
   contain local file paths with a personal name. Never copy a local path into a reader or a log; refer to files by
   their path inside the ZIP.

## What to deliver

Deliver three ZIPs: `DER_READERS_FR.zip`, `DER_READERS_EN.zip` and `DER_READERS_RECORDS.zip`. Together they hold:

- the six reader `.tex` files and the two annotated masters, with their PDFs if they compile (leave a PDF out only
  if a ZIP would exceed about 100 MB, and say so);
- `appendix_new_results.tex`, the companion master with its `\input`, and the rebuilt companion PDF;
- `CHANGES_FR.tsv`: every difference between the corrected French reader and the transcription at f42cfdd. Columns:
  page, place, before, after, source (correction row id, or your decision id);
- `CHANGES_EN.tsv`: every difference between the corrected English reader and the published English;
- `CORRECTIONS_DECIDED.tsv` and `GLOSSARY_FLAGGED.tsv`;
- `APPARATUS_COUNTS.md`: per chapter and form, the number of apparatus entries by kind;
- `README.md`: what each file is, how each form was made, all the counts, and the compile status of each book with
  its errors and warnings;
- your build scripts, with their outputs.

## When it is done

**Each item is done when:**
- **A reader** compiles without errors and carries every correction applied (check this by script against the
  correction tables and report the counts). Its page anchors agree with the transcription's.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected forms, and none for
  anything else.
- **The appendix** has all 12 entries with statement, proof, bearing, provenance and your reading, and the companion
  builds with it.

**Not acceptable:**
- a reader that drops, summarizes or paraphrases any part of the text;
- a correction applied in one form and missing from another;
- an apparatus entry without a source;
- the editors' notes altered or presented as ours;
- an appendix entry whose statement differs from its source without a note saying so;
- a claim of priority;
- local paths or e-mail addresses in any output.

**The task is finished** when the six readers, the appendix with the rebuilt companion, and every file listed above
are in the three ZIPs.

## Working method

- Start from the manifests, then the correction tables and the decisions. Build the annotated masters by script,
  generate the forms, compile, and check the counts. Then write the appendix.
- After each finished reader, save a checkpoint ZIP of everything so far to the user's Library, or wherever files
  survive the loss of the execution environment, named `DER_READERS_checkpoint_<n>.zip`. Save the final ZIPs there
  too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an
  interruption loses little.

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for at least ten minutes. If it does
not come back, write the work out in the chat as text:
- the appendix in full;
- the tables and the README so far;
- your build scripts in full, so that the readers can be rebuilt from the attached sources;
- which readers were finished and where their checkpoints are.

Put each file in full in its own code block headed by its file name. An answer that only reports the failure or asks
for the files again is not acceptable.
