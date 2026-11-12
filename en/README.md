# *Les Dérivateurs* in English

Alexander Grothendieck, *Les Dérivateurs* (1990–1991), **AI-translated** into English by GPT-6.1 Sol (OpenAI API,
reasoning effort max) from our French LaTeX transcription in this repository (`transcription/`, release
[v2026-11-11b](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/tag/v2026-11-11b)), which is
**AI-transcribed** by Claude Opus 5.5 from the edition of M. Künzer, J. Malgoire and G. Maltsiniotis.

- **The book:** [LesDerivateurs_English.pdf](LesDerivateurs_English.pdf) (910 pages), also attached to the release
  [en-2026-11-12](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/tag/en-2026-11-12). The whole
  translation as one book in Grothendieck's chapters: a title page, a note on the text and on how it was made, the
  contents, running heads; each chapter opens with the editors' note of its edition file, and the margins give the
  pages of the edition (p. *n*) and of the manuscript ([page *n*]). Its source, `LesDerivateurs_English.tex`, is one
  LaTeX file written from the units below by `scripts/build_reader.py`; compile it with LuaLaTeX, three runs.
- **Source:** one folder per edition file and one file per five pages, as in `transcription/`
  (`en/Der-ChI-234/Der-ChI-234_p001-005.tex`, ...); each file is a complete LaTeX document.
- The first book of 11 November, which set the 243 files one after the other (933 pages), is attached to the release
  [en-2026-11-11](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/tag/en-2026-11-11);
  `scripts/build.py` builds it from the files.

## How it was made

Each five-page file of the French was sent as one request (243 requests translated, in six batches on 11 November
2026). The prompt is in `prompt/`: the template and the parts for *Les Dérivateurs*, and the exact system and user
message of every request (`prompt/system/`, `prompt/user/`). It asks for a faithful English in Grothendieck's voice
and register, with his own English of *Pursuing Stacks* as the model, American spelling; formulas copied character
for character (only French words in text boxes translated); every macro, page anchor and comment line kept; and the
terms of the glossary that occur on the request's pages. The glossary (`glossary/`: 171 terms for *Les Dérivateurs*,
with the notation and typesetting tables and the files they are built from) was made before the translation by Claude
Fable 5.2 and Claude Opus 5.5. Each answer as it came back is in `runs/out/`. Scripts checked every answer against
its French (below); 41 fixes were made to the answers, 29 on 11 November and 12 on 12 November (see
Completeness), each recorded with its place and reason in [checks/FIXES.jsonl](checks/FIXES.jsonl), and
the English units here are the answers with those fixes. The scripts that prepared the requests, ran them, checked,
fixed and built the book are in `scripts/`; [checks/REPORT.md](checks/REPORT.md) gives the batches and the check and
fix counts.

## What the checks test, and what they cannot

The checks are scripts that compare each English file with its French file. All 243 files pass.

- **Formulas:** 46,016 of the 46,072 formulas are identical to the French. The other 56 are listed in
  [checks/FORMULAS_NOT_IDENTICAL.md](checks/FORMULAS_NOT_IDENTICAL.md): in 47 only the wording of a text box inside the
  formula differs (it is translated; every mathematical piece is unchanged), 7 are the same formula moved, 1 is a
  fragment cut by the checks' pairing of `$` signs, checked by hand, and 1 is the diagram whose LaTeX error was fixed
  (below).
- **Structure:** the 3,198 page anchors are in order; comment lines, macros, equation tags, footnote marks and the
  labels of axioms (Der 1, Loc (6 b), ...) are as in the French; no control sequence is added.
- **No French left:** in the running text and in the text boxes of formulas and diagrams.
- **Glossary:** 9,752 of 9,759 page-entries carry the glossary's English; the other 7 are misfires of the check on a
  correct translation, each waived with its reason in [checks/WAIVERS.jsonl](checks/WAIVERS.jsonl).
- **Paragraph lengths** against the French, and British spellings.

**The quality of the English prose is not machine-checked.** The checks establish that formulas, structure and terms
came through and that no French is left; they do not judge the English. The choice of model rests on a blind grading
of eight configurations translating the same pages; no second reading of the whole English has been made.

## Completeness

The whole translation was compared with the French, paragraph by paragraph and sentence by sentence, for passages
missing, cut short or left in French (`scripts/completeness.py`, `scripts/french_words_left.py`; the results in
`checks/completeness/`). The 7,267 paragraphs, 884 footnotes and 1,166 editors' notes of the French each have their
English, one for one; the French has 14,698 sentences, the English 14,736. Each of the 145 places that the comparison
flagged was read against the French: none is a missing or truncated passage.

What the comparison can see was measured by deleting sentences and clauses at random from the English and running it
again (`scripts/completeness_validation.py`, `checks/completeness/VALIDATION.json`): it found all 197 deleted
sentences, and 249 of 411 deleted clauses (55 of the 60 of at least 60 characters, 195 of the 268 of at least 30). A
short clause dropped from a long sentence can escape it.

[COMPLETENESS_20261112.csv](COMPLETENESS_20261112.csv) lists every place that was fixed or kept, with the French, the
English before and after, and the reason (50 rows):

- **Fixed** (the 12 fixes of 12 November): 18 places where the English had "Hot-" for the French lower-case "hot-"
  (Chapters I and II); French words left in a formula ("0-connexe", twice, Chapter XVI) and in a footnote ("faible",
  Chapter XII); two titles of published works in the bibliography of Chapter XIII, which had been translated and now
  stand as published; the word "immersion", which the edition hyphenates across the end of its page 154 (Chapter XII)
  and which the translation had split into two broken words; and the LaTeX error of a diagram (below).
- **Kept, with the reason:** the editors' gloss "[âne qui trotte: ...]" of Grothendieck's abbreviation AQT (14 places),
  given in French with its sense, as the glossary prescribes; 8 places where the editors could not read the manuscript
  (their note is translated; the word is lost in the source); 2 journal names.

## LaTeX

The book compiles with no errors and no undefined references. The book of 11 November had three LaTeX errors, all from
the transcription, whose French book has the same three: `\mathllap` used without the package `mathtools`
(`Der-ChXIV-07-10-10_p011-011`); a `#` error from the footnote macro of the preamble of `Der-ChXV-05-11-10_p031-035`,
as that book's loader read it; and a `tikz-cd` diagram whose baseline names an empty cell, which has no node
(`Der-ChXIIc-30-03-03_p061-064`). The third is fixed in the English file (it now names the cell of `T_1` in the same
row; the printed diagram is unchanged). The first two do not arise in the book, which defines `\mathllap` and reads
each file's preamble itself. All three are in the French transcription as of release v2026-11-11b. Diagrams wider than
the text, or taller than the page, are reduced to fit; the others are set as they are.

## In this copy

The e-mail address of G. Maltsiniotis, printed at the head of each edition file and once in the text of Chapter V, is
replaced by "[e-mail address removed]" in the files here; the book leaves the line out of the editors' notes and
replaces it in Chapter V. In the scripts, the first name of the user who ran the project is replaced by "user" in local
paths. The figures of what the runs cost are withheld from this copy: the billed columns of `checks/REPORT.md`, the
price, budget and cap figures in `scripts/run.py` and `scripts/cmp/run.py`, and the run records of each request.

## Credits

- **Author:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991).
- **Edition:** M. Künzer, J. Malgoire and G. Maltsiniotis (Universités de Montpellier II et Paris VII),
  <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>. The deciphering of the manuscript, its
  edition and the editors' notes are theirs.
- **Transcription** (the French translated here): AI-transcribed by Claude Opus 5.5 (Anthropic); its corrections from
  the critical companion are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode) and checked by Claude Opus 5.5.
- **Translation:** AI-translated by GPT-6.1 Sol (OpenAI API, reasoning effort max).
- **Glossary, prompt, checks, fixes, the comparison for completeness and the book:** Claude Opus 5.5 (Anthropic); the
  glossary also by Claude Fable 5.2 (Anthropic).

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights,
in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain
under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.
