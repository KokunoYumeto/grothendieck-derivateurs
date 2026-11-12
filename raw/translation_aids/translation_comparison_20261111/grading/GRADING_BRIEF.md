# Blind grading of the translation comparison (11 Nov 2026)

Several configurations translated the same French into English: five scans of Grothendieck's *La Longue Marche à
travers la théorie de Galois* (our diplomatic transcription, with its marks) and five edition pages of his *Les
Dérivateurs*. One version per work covers only the first page. The versions are anonymous (letters). The choice of
translation route for about 2,700 pages depends on your grading, so fidelity to the French is what counts.

## What you may read

- `user\Documents\translation_comparison_20261111\source\`: the French (`LM.tex`, `DER.tex`; `LM_ref.tex`,
  `DER_ref.tex` are their first pages).
- `...\prompt\`: the brief every translator received (`system_LM.txt`, `system_DER.txt`, with the glossary decisions
  and conventions; `user_*.txt` hold the French as sent).
- `...\blind\`: the versions, `LM_<letter>.tex` and `DER_<letter>.tex`.

Do not open `key\`, `runs\`, `checks\`, `RUNS.md`, `selection\` or anything else in the folder: they name the
configurations. Do not read the other grader's files in `grading\`.

## How to grade

For each work, go through the French sentence by sentence and compare every version at that place. Record every error:
- **meaning**: the English says something the French does not (wrong object, quantifier, direction, negation, scope,
  reference; a hedge such as "il semble que" or "sans doute" made firmer or weaker);
- **omission** or **addition** of content;
- **terminology**: a term other than the brief prescribes, or inconsistent within the version;
- **marks**: a `\deleted`, `\inserted`, `\unsure`, `\illegible`, margin note or comment handled otherwise than the
  brief says (the script checks found every formula unchanged in all but one version; you need not re-check formulas
  symbol by symbol, but do note any you see changed);
- **English**: unidiomatic, ambiguous or unclear English a mathematician would stumble on, meaning intact.

Severity: **major** if a reader would get the mathematics or the author's stance wrong, or lose content; otherwise
**minor**. For each error: version, page anchor, category, severity, the French, the English, the fix.

For each version give a fidelity score and an English score (0–10 each) and two sentences on its character. Then rank
the versions per work (ties allowed) and say whether the differences between the top versions matter to a reader of an
edition. Do not reward length, polish or explanation over fidelity; an added explanation is an error.

## What to write

`grading\GRADE_<your label>.md`: per work, the table of errors, the scores, the ranking, and a short conclusion.
`grading\GRADE_<your label>.json`: `{"LM": {"errors": [...], "scores": {letter: {"fidelity": n, "english": n}},
"ranking": [...]}, "DER": {...}, "conclusion": "..."}`.
