# Grothendieck, *Les Dérivateurs*: LaTeX transcription and critical companion

*Les Dérivateurs* is a manuscript of 1,976 pages that Alexander Grothendieck wrote between October 1990 and the first
half of 1991. It is devoted to the foundations of homotopy theory: it is centred on the notion of a derivator, several
chapters study the homotopy theory of the category of small categories and various notions of model category, and the
long penultimate chapter founds the theory of accessible categories. M. Künzer, J. Malgoire and G. Maltsiniotis
deciphered the manuscript and published an electronic edition of it (twenty-two chapter files and a table of contents,
1,176 typeset pages), freely available at

<https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>

That edition is published as PDF only. This repository holds three things built on Grothendieck's text as read in
it: the transcription, the critical companion and an English translation.

**The editors' own writing is not reproduced here.** Their notes (the corrections, comments and queries they set in
typewriter type between square brackets), the preface of each chapter file, the afterword of Chapter XIV, their table
of contents, and the running heads and footers of their pages are their work, and they are left out of every file of
this repository, in French and in English. Read them in the edition. Where a note of theirs supplies a missing word or
corrects a slip, the text here is the text as the edition prints it, without the note. (Until 15 November 2026 this
repository reproduced those notes; that version and its history have been replaced by this one.)

## Whose work this is

*Les Dérivateurs* was deciphered and transcribed by M. Künzer, J. Malgoire and G. Maltsiniotis, who published it as an
electronic edition: <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>. Their edition is the
basis of everything here: our LaTeX follows their text page by page, and our English translation was made from their
French. We did not decipher the manuscript; they did. Their notes, prefaces, postface and page furniture are their own
writing and are not reproduced here; read them in their edition. What their notes point out, and our attempts to answer
the questions they raise, will be listed in our own words in `EDITORS_INSIGHTS_AND_OUR_ANSWERS.md`.

## How this was made: AI's failure modes, and what we do about them

Everything here was produced by AI. Transcribing a typeset edition and translating it fail in known ways, and a reader
is right to expect them. The method is built against each of them, and we report what the checks measured.

**How each layer was made**
- **Transcription:** Claude Opus 5.5 at effort high (Anthropic Message Batches API), from images of the edition's
  pages, not from its PDF text: one request per five pages (243 requests, one per file of `transcription/`), each page
  sent whole and as three overlapping strips at 300 dpi. Each five-page file is a complete LaTeX document and is
  compiled on its own.
- **Check of the transcription:** each of the 32 parts of the companion was checked against the edition's pages by
  GPT-6 Astra (ChatGPT Pro mode), which returned the corrected text with a table of corrections
  (`companion/checks/DER_<part>/DER_<part>_corrections.csv`). Claude Opus 5.5 at effort max then decided every change
  the returned texts made but the tables did not list, each against the edition's page (`transcription/DECISIONS.md`).
- **Companion:** the commentary, the register of claims and the bibliography are by GPT-6 Astra (ChatGPT Pro mode).
- **English:** GPT-6.1 Sol at reasoning effort max (OpenAI API, Flex), five pages per request, with a glossary of
  Grothendieck's terms (171 entries); every answer was checked by scripts against its French, then the whole was
  compared with the French paragraph by paragraph and sentence by sentence (`en/README.md`).

**The failure modes, and what we do about each**
- **A plausible word in place of the printed one.** The transcription prompt asks for the printed text and a `% ??`
  comment wherever a reading is in doubt. The check by GPT-6 Astra (ChatGPT Pro mode) found 134 transcription errors
  in the 1,171 pages (about one in nine pages) and resolved 122 doubtful readings; all are corrected and listed in the
  parts' tables. 20 `% ??` marks remain in the source, each a place to read against the edition.
- **Dropped symbols, lines or diagram arrows.** Each page is sent whole and in three overlapping strips, so that no
  line falls between two images; the check compares every page of the text with the edition's page, formulas and
  diagrams included. In the English, scripts compared every formula with the French: 46,016 of the 46,072 are
  identical, and the other 56 are listed with the reason in `en/checks/FORMULAS_NOT_IDENTICAL.md` (47 differ only in
  a translated word inside the formula).
- **Silent corrections of the edition.** A model tends to correct what looks like a slip. Our rule is the opposite:
  slips of the edition are kept as printed and flagged `% [sic]` in the source (895 flags); the companion's tables
  list 1,878 such slips, kept. The checking model's own changes were not taken on trust: of the 435 changes its
  returned texts made without listing them, Claude Opus 5.5 at effort max kept 69 that match the edition and 130
  layout-only repairs, undid 9 that were wrong and 227 layout additions, and overruled five of the listed corrections
  against the edition's pages (`transcription/DECISIONS.md`). The editors' own corrections, which stood in their
  notes, are not applied: the text is as the edition prints it.
- **Notation drifting between packages.** Each five-page file carries the macro definitions of its own pages, so a
  sign is defined where it is used; ten corrections of macro definitions were checked against the pages and eight
  applied. In the English, formulas are copied character for character from the French, and the glossary fixes one
  English term for each of Grothendieck's terms: 9,752 of 9,759 page entries carry the glossary's English, and the
  other 7 are checked misfires of the script, each waived with its reason.
- **A translation that smooths or "improves" the mathematics.** The prompt asks for Grothendieck's own register and
  forbids any change to formulas; the formula check above enforces it, and the page anchors, labels and footnote marks
  are checked to stand as in the French. What scripts cannot judge is the English prose itself: it has not had a second
  reading as a whole.
- **Dropped sentences.** The whole translation was compared with the French for anything missing, cut short or left in
  French: the 7,267 paragraphs and 884 footnotes have their English one for one (14,698 French sentences, 14,736
  English), and each of the 145 places the comparison flagged was read against the French; none is a missing passage.
  The comparison was tested by deleting text from the English at random: it found all 197 deleted sentences and 249
  of 411 deleted clauses, so a short clause dropped from a long sentence can escape it.
- **Work lost or cut short.** Every request, answer and fix is kept: the prompts as sent (`en/prompt/`), the answers
  (`en/runs/out/`), the 41 fixes with their reasons (`en/checks/FIXES.jsonl`), and each part's returned text before
  the decisions (`companion/checks/DER_<part>/DER_<part>_text_pro.tex`).

The edition's pages are public on the editors' site, so every reading here can be checked against them. Corrections are
welcome as GitHub issues.

## 1. The LaTeX transcription (complete)

A LaTeX transcription of Grothendieck's text in the whole edition: every page of the nineteen chapters (Chapter XII
in four files, as in the edition). The manuscript's page numbers are kept in brackets in the margin ([page 12]); where
the edition marks a page of the manuscript as blank, missing, struck through or numbered twice, a word of ours says so
([page 68: blank]). The edition's printed page numbers are in the margin (p. 12). Slips of the edition are kept as
printed and marked `% [sic]` in the source; doubtful readings are marked `% ??`, and where the check of the companion
resolved a doubt, the comment gives the resolution.

The transcription carries the corrections found in checking each of the companion's parts: the transcription
errors and the resolved doubtful readings that each part's table of corrections lists, and the other changes of the
checked text that agree with the edition's pages. The decisions on those other changes, one per change with the page,
the reason and the text before and after, are in `transcription/DECISIONS.md` and `transcription/DECISIONS.json`;
`DECISIONS.md` also gives the check of the ten corrections that change the definition of a macro, eight of which are
applied (in Chapters I, II, VI and XIX). Not applied: five listed corrections that the check against the edition's
pages overruled (two in Chapter XVII, one each in Chapters II, VII and XVI). On pages that two parts both contain, the
transcription follows the earlier part.

- PDF: **[LesDerivateurs_transcription.pdf](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/latest/download/LesDerivateurs_transcription.pdf)**
  (896 pages)
- Source: `transcription/`, one folder per edition file, one file per five pages
  (`transcription/Der-ChI-234/Der-ChI-234_p001-005.tex`, ...). Each of these files is a complete LaTeX document.
  `transcription/LesDerivateurs_transcription.tex` sets them all in one book.

The edition files and the versions transcribed (the version is printed at the foot of each page of the edition):

| Edition file | Contents | Version |
|---|---|---|
| `Der-ChI-234` | Chapitre I. Généralités sur les (pré)dérivateurs | 8 juillet 2001 |
| `Der-ChII-234` | Chapitre II. Cofinalité (à droite et à gauche) (préliminaire à la cofinalité cohomologique) | 8 juillet 2001 |
| `Der-ChIII-567` | Chapitre III. Hom externes dans les dérivateurs | 2 février 2002 |
| `Der-ChIV-567` | Chapitre IV. Diagrammes substantiels | 2 février 2002 |
| `Der-ChV-234` | Chapitre V. Catégories de chemins et localisation | 9 septembre 2001 |
| `Der-ChVI-345` | Chapitre VI. HOT | 9 novembre 2001 |
| `Der-ChVII-456` | Chapitre VII. Catégories de chemins (2) | 22 décembre 2001 |
| `Der-ChVIII-567` | Chapitre VIII. 1-types d'homotopie relatifs : leur intégration... | 2 février 2002 |
| `Der-ChIX-678` | Chapitre IX. Retour sur les catégories de fractions MW⁻¹, comparaison avec Quillen | 12 mars 2002 |
| `Der-ChX-789` | Chapitre X. Comparaison de Cat avec Δ^ | 9 avril 2002 |
| `Der-ChXI-890` | Chapitre XI. Hot-fibrations, foncteurs propres et foncteurs lisses etc. (dans Cat) | 28 mai 2002 |
| `Der-ChXIIa-012` | Chapitre XII. Caractérisation de W∞ ..., sections 1–4 | 7 décembre 2002 |
| `Der-ChXIIb-012` | Chapitre XII, section 5 | 7 décembre 2002 |
| `Der-ChXIIc-30-03-03` | Chapitre XII, section 6 | 30 mars 2003 |
| `Der-ChXIIapp-19-06-03` | Appendice au chapitre XII | 20 juin 2003 |
| `Der-ChXIII-25-01-04` | Chapitre XIII. Catégories de modèles (1) | 25 janvier 2004 |
| `Der-ChXIV-07-10-10` | Chapitre XIV. Carrés h-cartésiens et h-cocartésiens | 7 octobre 2010 |
| `Der-ChXV-05-11-10` | Chapitre XV. Théorèmes de factorisation (Modèles (2)) | 5 novembre 2010 |
| `der-ch16` | Chapitre XVI. Les localiseurs fondamentaux | 18 mars 2019 |
| `der-ch17` | Chapitre XVII. Catégories à fibrations et à cofibrations (Modèles (3)) | 9 février 2019 |
| `der-ch18` | Chapitre XVIII. Catégories et ensembles accessibles | 17 décembre 2025 |
| `der-ch19` | Chapitre XIX. Modèles (4) | 11 février 2019 |

The files are named as on the editors' page; the editors ask that links point to their page, not to the files, whose
names change with each version.

**Compiling.** 240 of the 242 files compile without LaTeX errors. In two files LuaLaTeX reports one error each (in a
diagram and a footnote); the PDF is still produced, and these places should be read against the edition:
Chapter XII section 6 pp. 61–64; Chapter XV pp. 31–35 (pages of the edition's files). Six files carry
LaTeX-only changes that leave the text as read: in Chapter II pp. 26–30 and Chapter VII pp. 76–80 a macro is renamed
(`\def` to `\defeq`, `\No` to `\Nop`) because TeX or French babel already uses the name; in Chapter VII pp. 106–109 a
TikZ style uses `-` instead of the tikz-cd key `no head`; in Chapter XII appendix pp. 6–10, Chapter XV pp. 46–50 and
Chapter XVII pp. 1–5 a diagram inside a footnote or an italic passage uses `ampersand replacement=\&`. Where a
corrected page uses a macro or a package that its file did not have, the file's preamble has gained that definition or
package (seventeen files). In fourteen files the preamble has the corrected macro definition or package option of a
table row (`transcription/DECISIONS.md`), and fifteen files load `lmodern`, without which LuaLaTeX has no glyph for
the bold capital Greek letters and accented letters that their formulas set in a math alphabet; the master file loads
it too.

## 2. The critical companion (complete)

A reading of the text with an English commentary set into Grothendieck's French at the places it concerns, marked by
a vertical rule. The commentary explains the definitions and arguments, gives the mathematical context and the later
literature, works out examples, and states the present status of each question; where the text leaves a proof to be
given or a claim is false, it gives the proof or a counterexample, marked as the commentators' own and with no claim of
priority. Each part also has

- a register of claims: every definition, axiom, proposition, claim, conjecture and question of the text, with the
  status the text gives it: proved, sketched, stated, assumed, conjectured, false (the assertion, or the inference as
  written, is false) or open;
- a table of corrections to the transcription: transcription errors, doubtful readings resolved, and slips of the
  edition kept as printed;
- a bibliography with links.

The companion sets the corrected text of the pages it covers. These corrections are listed in each part's
`corrections.csv`, and the transcription in `transcription/` carries them too (section 1).

- PDF: **[LesDerivateurs_companion.pdf](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/latest/download/LesDerivateurs_companion.pdf)**
  (1,865 pages: the text and commentary, the register of claims, the corrections, the bibliography)

The companion has all 32 of its parts. It covers:

| Chapter | Covered |
|---|---|
| I | whole chapter (parts I-a, I-b) |
| II | whole chapter (parts II-a, II-b) |
| III, IV, V | whole chapters (part III-V) |
| VI | whole chapter (parts VI-a, VI-b, VI-c) |
| VII | whole chapter (parts VII-a, VII-b, VII-c) |
| VIII, IX, X | whole chapters (part VIII-X) |
| XI | whole chapter (part XI-XIIa) |
| XII, sections 1–4 | whole sections (part XI-XIIa) |
| XII, section 5 | whole section (parts XIIb-a, XIIb-b) |
| XII, section 6 | whole section (parts XIIc-a, XIIc-b) |
| XII, appendix | whole appendix (part XIIapp) |
| XIII | whole chapter (parts XIII-a, XIII-b) |
| XIV | whole chapter (part XIV) |
| XV | whole chapter (parts XV-a, XV-b) |
| XVI | whole chapter (part XVI) |
| XVII | whole chapter (parts XVII-a, XVII-b) |
| XVIII | whole chapter (parts XVIII-a to XVIII-e) |
| XIX | whole chapter (part XIX) |

Source: `companion/`

- `companion/checks/DER_<part>/`: for each part, the text with its anchors (`_text.tex`), the commentary blocks
  (`_blocks.tex`), the overview (`_overview.tex`), the register of claims (`_claims.csv`), the corrections
  (`_corrections.csv`) and the bibliography (`_references.bib`); in seventeen parts also `_text_pro.tex`, the text
  before the decisions of `transcription/DECISIONS.md` undid some of the returned changes (the returned text; in I-b
  and VII-a with three readings fixed in the review of the overlaps);
- `companion/reader/`: the book, `LesDerivateurs_companion.tex`, with its bibliography and the per-part files it
  inputs (`parts/`), all written by `kit/build_global_reader.py`; `OVERLAPS.md` explains how pages that two
  consecutive parts both contain are set once in the book. Seven such pairs, which involve the parts added in
  this release (Chapters II, XV, XVII and XVIII), are not merged yet: the book sets their pages in both parts.

## 3. The English translation

[`en/`](en/README.md): the whole of *Les Dérivateurs* in English, AI-translated by GPT-6.1 Sol (OpenAI API, reasoning
effort max) from the transcription, with the checks of every page against the French and a comparison of the whole for
completeness; the editors' writing is taken out of it as out of the French (`en/README.md`). The book:
**[LesDerivateurs_English.pdf](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/latest/download/LesDerivateurs_English.pdf)**
(894 pages).

## Raw research outputs

[`raw/`](raw/README.md) holds raw research outputs, not edited for publication: the answers of GPT-6 Astra (ChatGPT
Pro mode) to eight research prompts on open questions of the manuscript, their reviews by Claude Fable 5.2 (Anthropic; the reviews of 10–11 Nov 2026 at effort high or medium, those from 12 Nov at effort max), the prompts
with everything they attached, and [how this was done](raw/METHODOLOGY.md).

Readers (French and English, each diplomatic, corrected with apparatus, and plain reading text) and the companion with
an appendix of new results, built by GPT-6 Astra (ChatGPT Pro mode) on 12 Nov 2026, not yet reviewed:
[`raw/pro_returns/DER_READERS_20261112/`](raw/pro_returns/DER_READERS_20261112/README.md).

The editors' writing is taken out of the raw records too (15 Nov 2026): the prompts with their attachments, the
answers, the readers and their records, the check records. Records that quoted it now say where it stood ("[editors'
note, not reproduced]"); hashes, offsets and counts that the records give for the texts as they were no longer match
the files.

## Building

Both books need LuaLaTeX (TeX Live 2025 or later, with `fontspec`, `babel-french`, `tikz-cd`, `luacode`); the companion
also needs BibTeX and Python 3.

```
# the transcription (from the repository root)
python -I kit/build_transcription_master.py --pdf
#   or by hand: cd transcription; lualatex LesDerivateurs_transcription.tex (three runs)

# the companion
for d in companion/checks/DER_*; do python -I kit/build_reader.py "$(basename "$d")" "$d"; done
python -I kit/build_global_reader.py --pdf
```

`kit/build_reader.py` sets the commentary blocks of a part into its text at their anchors and checks the part's files;
`kit/build_global_reader.py` assembles the book (LuaLaTeX, BibTeX, LuaLaTeX until the cross-references settle);
`kit/derivateurs_companion.sty` is the style of the commentary. A single five-page transcription file compiles on its
own with `lualatex`.

## Weigh in

AI models are following up the mathematical leads in this material. Claude Fable 5.2 and Claude Opus 5.5 (effort max)
read the texts, check the results and write the next questions; GPT-6 Astra (ChatGPT Pro mode) proves and computes.
The results are published here as they come in.

If you work on these topics and want something taken into account (a reference, a known result, an error, an
objection, a direction worth pursuing or one to drop), please open an [issue](../../issues). Issues are read and go
into the next round of work, with credit to you.

## Credits

- **Author:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991).
- **Edition transcribed:** the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis (Universités de
  Montpellier II et Paris VII), <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>, in the
  versions listed above. The deciphering of the manuscript and its edition are theirs. Their notes, prefaces,
  afterword, table of contents and page furniture are their own writing and are not reproduced here.
- **Transcription:** AI-transcribed by Claude Opus 5.5 at effort high (Anthropic, Message Batches API).
- **Companion:** commentary AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checked and integrated by Claude
  Opus 5.5 (Anthropic). The register of claims and the corrections are produced the same way.
- **Commentary from reviewed answers:** eight commentary blocks in parts II-a, III-V and XIIb-a, seven paragraphs of
  other blocks there, nineteen rows of the register of claims (II-a, III-V, VII-c, VIII-X, XIIb-a) and three
  bibliography entries are AI-produced by Claude Fable 5.2 (Anthropic; the reviews of 10–11 Nov 2026 at effort high or medium, those from 12 Nov at effort max), from answers of GPT-6 Astra (OpenAI, ChatGPT
  Pro mode) that it reviewed; each of these rows names the answer and the reviewer.
- **Corrections in the transcription:** the corrections of the companion (above); the corrections of macro
  definitions and the changes of the checked texts that their tables do not list were compared with the edition's
  pages by Claude Opus 5.5 at effort max (Anthropic) (`transcription/DECISIONS.md`).
- **English translation:** AI-translated by GPT-6.1 Sol (OpenAI API, reasoning effort max) from the transcription;
  glossary by Claude Fable 5.2 at effort medium and Claude Opus 5.5 at effort max, prompt, checks, fixes, the comparison for completeness and the
  book by Claude Opus 5.5 at effort max (Anthropic) (`en/README.md`).
- **Raw research outputs** (`raw/`): the answers AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); the reviews
  by Claude Fable 5.2 (Anthropic; the reviews of 10–11 Nov 2026 at effort high or medium, those from 12 Nov at effort max).

## Rights

The rights in Grothendieck's text belong to his heirs. This edition is published for educational, non-profit purposes,
and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open
a GitHub issue and we will take it down.

Our French transcription follows the electronic edition of *Les Dérivateurs* by M. Künzer, J. Malgoire and
G. Maltsiniotis, and our English translation was made from it. We based our work on their edition because it is careful
and accurate: a spot check of four pages against the manuscript scans of the Montpellier archive, by Claude Opus 5.5 at
effort high, found it a faithful edition of the final text of the manuscript. A faithful transcription reproduces the
author's text, and the rights in that text are the author's heirs'. What is the editors' own work, their notes,
prefaces and postface, is not reproduced here; it can be read in their edition. Like theirs, our edition is meant to
make Grothendieck's manuscript available and readable to those who study his mathematics; ours adds an English
translation. If the editors nonetheless want us to stop basing our text on theirs, we will, and replace it with a
transcription made from the manuscript scans alone.

Our transcription, translation, corrections and typesetting were produced by AI. They have no human author and, in our understanding, are not protected by copyright; where any right of ours exists nonetheless, it is dedicated to the public domain under CC0 1.0. All of this work reproduces or translates Grothendieck's text, whose rights belong to his heirs, so nothing here licenses or authorizes any reproduction, translation or other use of his work.

**Prompts and method.** The prompts, templates, scripts and working method published here are dedicated to the public domain under CC0 1.0. If you want to do similar work, use them freely; we claim no rights in them.

See also [RIGHTS_NOTICE.md](RIGHTS_NOTICE.md) (with the French text).

## Rights considerations

**Grothendieck's texts.** The rights belong to his heirs; his texts are protected until the end of 2084. The University
of Montpellier publishes the scans of his mathematical papers (https://grothendieck.umontpellier.fr/archives-grothendieck/) with his heirs' agreement. We hold no licence
from his heirs and claim no rights in his texts.

**Grothendieck's declaration of 3 January 2010.** He declared that he did not intend to publish or republish any of his texts, or translations of them, and that any edition made without his agreement in the past, or in the future during his lifetime, was illicit in his eyes. Since his death in 2014 the decision lies with his heirs, who have agreed to the University of Montpellier's online publication of his mathematical papers. We publish on that basis.

**Earlier editions and transcriptions.** Others have edited or transcribed parts of these papers before us:
- *Les Dérivateurs*: the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis (https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html);
- *La Longue Marche à travers la théorie de Galois*: tome 1, edited by J. Malgoire (Université Montpellier II, 1995),
  and the transcriptions by M. Carmona with M. Künzer (https://agrothendieck.github.io/);
- *Pursuing Stacks*: M. Carmona's transcription (https://arxiv.org/abs/2111.01000), which he dedicated to the public domain under CC0, and
  G. Maltsiniotis's edition *À la poursuite des champs*, vol. I (SMF, 2022);
- the transcriptions of the Centre for Grothendieckian Studies (https://csg.igrothendieck.org/), which states that it publishes them with the
  consent of the rights holders.

Apart from that statement, none of these says it holds a licence from the heirs, and a transcription gives its maker no
rights in the author's text. We do the same work with AI for the whole archive: to make all of it available as editable
LaTeX, with translations, and as a second reading beside the existing ones. This is no claim of priority or
superiority, and no claim to rights we do not hold. If the editors of an earlier edition would rather we took down what
we based on their work, so that theirs stands alone, we will do so as a courtesy.

**Works with an authorized edition.** Where a work has an edition published with the rights holders' authorization, as
*Récoltes et Semailles* has (Gallimard, 2022), we do not reproduce or translate it; at most we write our own commentary
on its mathematics.

**Texts by others.** We transcribe or translate other people's texts only where the rights holders, or the institution
that holds the texts, have made them publicly available for study. Examples are Daniel Quillen's notebooks, which the
Clay Mathematics Institute has digitized and made available to the mathematical community (https://www.claymath.org/online-resources/quillen-notebooks/), and the Séminaire
Bourbaki exposés and Bourbaki drafts that Grothendieck reused or kept among his own notes, which the University
publishes as part of his papers. This is our good-faith reading, not a claim of rights. If you hold rights in any of
this and object, please open a GitHub issue and we will take it down.

