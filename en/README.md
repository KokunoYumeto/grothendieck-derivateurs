# *Les Dérivateurs* in English

Alexander Grothendieck, *Les Dérivateurs* (1990–1991), **AI-translated** into English by GPT-6.1 Sol (OpenAI API,
reasoning effort max) from our French LaTeX transcription in this repository (`transcription/`, release
[v2026-11-11b](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/tag/v2026-11-11b)), which is
**AI-transcribed** by Claude Opus 5.5 from the edition of M. Künzer, J. Malgoire and G. Maltsiniotis.

- PDF: [LesDerivateurs_translation.pdf](LesDerivateurs_translation.pdf) (933 pages), also attached to the release
  [en-2026-11-11](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/tag/en-2026-11-11).
- Source: one folder per edition file and one file per five pages, as in `transcription/`
  (`en/Der-ChI-234/Der-ChI-234_p001-005.tex`, ...); each file is a complete LaTeX document.
  `LesDerivateurs_translation.tex` sets all 243 of them in one book, with the transcription's loader
  `derivateurs_parts.lua`; compile it with LuaLaTeX, three runs.

## How it was made

Each five-page file of the French was sent as one request (243 requests translated, in six batches on 11 November
2026). The prompt is in `prompt/`: the template and the parts for *Les Dérivateurs*, and the exact system and user
message of every request (`prompt/system/`, `prompt/user/`). It asks for a faithful English in Grothendieck's voice
and register, with his own English of *Pursuing Stacks* as the model, American spelling; formulas copied character
for character (only French words in text boxes translated); every macro, page anchor and comment line kept; and the
terms of the glossary that occur on the request's pages. The glossary (`glossary/`: 171 terms for *Les Dérivateurs*,
with the notation and typesetting tables and the files they are built from) was made before the translation by Claude
Fable 5.2 and Claude Opus 5.5. Each answer as it came back is in `runs/out/`. Scripts checked every answer against
its French (below); 29 fixes were made to the answers, each recorded with its place and reason in
[checks/FIXES.jsonl](checks/FIXES.jsonl), and the English units here are the answers with those fixes. The scripts
that prepared the requests, ran them, checked, fixed and built the book are in `scripts/`;
[checks/REPORT.md](checks/REPORT.md) gives the batches and the check and fix counts.

## What the checks test, and what they cannot

The checks are scripts that compare each English file with its French file. All 243 files pass.

- **Formulas:** 46,017 of the 46,072 formulas are identical to the French. The other 55 are listed in
  [checks/FORMULAS_NOT_IDENTICAL.md](checks/FORMULAS_NOT_IDENTICAL.md): in 47 only the wording of a text box inside the
  formula differs (it is translated; every mathematical piece is unchanged), 7 are the same formula moved, and 1 is a
  fragment cut by the checks' pairing of `$` signs, checked by hand.
- **Structure:** the 3,198 page anchors are in order; comment lines, macros, equation tags, footnote marks and the
  labels of axioms (Der 1, Loc (6 b), ...) are as in the French; no control sequence is added.
- **No French left:** in the running text and in the text boxes of formulas and diagrams.
- **Glossary:** 9,752 of 9,759 page-entries carry the glossary's English; the other 7 are misfires of the check on a
  correct translation, each waived with its reason in [checks/WAIVERS.jsonl](checks/WAIVERS.jsonl).
- **Paragraph lengths** against the French, and British spellings.

**The quality of the English prose is not machine-checked.** The checks establish that formulas, structure and terms
came through and that no French is left; they do not judge the English. The choice of model rests on a blind grading
of eight configurations translating the same pages; no second reading of the whole English has been made.

## LaTeX errors

The book compiles with three LaTeX errors. They are the transcription's own: the French book of the transcription has
the same three, in the same files.

1. `\mathllap` is used without the package `mathtools` in `Der-ChXIV-07-10-10_p011-011`.
2. A `#` error from the footnote macro (`\@makefntext`) of the preamble of `Der-ChXV-05-11-10_p031-035`, as the book's
   loader reads it.
3. An arrow to an empty cell of a `tikz-cd` diagram (no node `tikz@f@769-2-1`) in `Der-ChXIIc-30-03-03_p061-064`.

When they are fixed in the transcription, the same fixes will be made here.

## Open point

Where the French writes the prefix "hot-" in lower case, in 16 places of Chapters I and II, the English has "Hot-",
the glossary's form. These will be changed to follow the French.

## In this copy

The e-mail address of G. Maltsiniotis, printed at the head of each edition file, is replaced by
"[e-mail address removed]", here and in the PDF, which is built from these files. In the scripts, the first name of
the user who ran the project is replaced by "user" in local paths. The figures of what the runs cost are withheld from
this copy: the billed columns of `checks/REPORT.md`, the price, budget and cap figures in `scripts/run.py` and
`scripts/cmp/run.py`, and the run records of each request.

## Credits

- **Author:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991).
- **Edition:** M. Künzer, J. Malgoire and G. Maltsiniotis (Universités de Montpellier II et Paris VII),
  <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>. The deciphering of the manuscript, its
  edition and the editors' notes are theirs.
- **Transcription** (the French translated here): AI-transcribed by Claude Opus 5.5 (Anthropic); its corrections from
  the critical companion are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode) and checked by Claude Opus 5.5.
- **Translation:** AI-translated by GPT-6.1 Sol (OpenAI API, reasoning effort max).
- **Glossary, prompt, checks, fixes and build:** Claude Opus 5.5 (Anthropic); the glossary also by Claude Fable 5.2
  (Anthropic).

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights,
in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain
under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.
