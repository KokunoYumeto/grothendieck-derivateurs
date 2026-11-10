# Grothendieck, *Les Dérivateurs*: LaTeX transcription and critical companion

*Les Dérivateurs* is a manuscript of 1,976 pages that Alexander Grothendieck wrote between October 1990 and the first
half of 1991. It is devoted to the foundations of homotopy theory: it is centred on the notion of a derivator, several
chapters study the homotopy theory of the category of small categories and various notions of model category, and the
long penultimate chapter founds the theory of accessible categories. M. Künzer, J. Malgoire and G. Maltsiniotis
deciphered the manuscript and published an electronic edition of it (twenty-two chapter files and a table of contents,
1,176 typeset pages), freely available at

<https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>

That edition is published as PDF only. This repository holds two things built on it.

## 1. The LaTeX transcription (complete)

A LaTeX transcription of the whole edition: the table of contents and every page of the nineteen chapters (Chapter XII
in four files, as in the edition). It follows the edition's layout and conventions: the manuscript's page numbers and
the editors' notes in typewriter type between square brackets, the edition's printed page numbers in the margin, the
running heads and footers as TeX comments. Slips of the edition are kept as printed and marked `% [sic]` in the
source; doubtful readings are marked `% ??`.

- PDF: **[LesDerivateurs_transcription.pdf](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/latest/download/LesDerivateurs_transcription.pdf)**
  (934 pages)
- Source: `transcription/`, one folder per edition file, one file per five pages
  (`transcription/Der-ChI-234/Der-ChI-234_p001-005.tex`, ...). Each of these files is a complete LaTeX document.
  `transcription/LesDerivateurs_transcription.tex` sets them all in one book.

The edition files and the versions transcribed (the version is printed at the foot of each page of the edition):

| Edition file | Contents | Version |
|---|---|---|
| `dertbmt` | Table des matières | |
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

**Compiling.** 232 of the 243 files compile without LaTeX errors. In eleven files LuaLaTeX reports errors, mostly
commutative diagrams with an arrow to a cell that does not exist and unbalanced braces in displays; the PDF is still
produced, and these places should be read against the edition: Chapter I pp. 51–55; Chapter II pp. 16–20;
Chapter VII pp. 101–105; Chapter XII section 6 pp. 61–64; Chapter XIV p. 11; Chapter XV pp. 31–35 and 46–50;
Chapter XVI pp. 36–40; Chapter XVII pp. 21–25; Chapter XVIII pp. 121–125 and 176–180 (pages of the edition's files).
Six files carry LaTeX-only changes that leave the text as read: in Chapter II pp. 26–30 and Chapter VII pp. 76–80 a
macro is renamed (`\def` to `\defeq`, `\No` to `\Nop`) because TeX or French babel already uses the name; in
Chapter VII pp. 106–109 a TikZ style uses `-` instead of the tikz-cd key `no head`; in Chapter XII appendix pp. 6–10,
Chapter XV pp. 46–50 and Chapter XVII pp. 1–5 a diagram inside a footnote or an italic passage uses
`ampersand replacement=\&`.

## 2. The critical companion (in progress)

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
`corrections.csv`; the files in `transcription/` are the transcription before them.

- PDF: **[LesDerivateurs_companion.pdf](https://github.com/KokunoYumeto/grothendieck-derivateurs/releases/latest/download/LesDerivateurs_companion.pdf)**
  (857 pages: the text and commentary, the register of claims, the corrections, the bibliography)

The companion now covers:

| Chapter | Covered |
|---|---|
| I | whole chapter (parts I-a, I-b) |
| II | pages 1–35 of the 65 of the edition file (part II-a) |
| III, IV, V | whole chapters (part III-V) |
| VI | whole chapter (parts VI-a, VI-b, VI-c) |
| VII | whole chapter (parts VII-a, VII-b, VII-c) |
| VIII, IX, X | whole chapters (part VIII-X) |
| XII, section 5 | whole section (parts XIIb-a, XIIb-b) |
| XII, section 6 | pages 1–35 of the 64 of the edition file (part XIIc-a) |
| XII, appendix | whole appendix (part XIIapp) |

In progress: the rest of Chapter II; Chapter XI; Chapter XII, sections 1–4 and the rest of section 6; Chapters XIII to
XIX. The table of contents of the companion lists these parts as not yet included.

Source: `companion/`

- `companion/checks/DER_<part>/`: for each part, the text with its anchors (`_text.tex`), the commentary blocks
  (`_blocks.tex`), the overview (`_overview.tex`), the register of claims (`_claims.csv`), the corrections
  (`_corrections.csv`) and the bibliography (`_references.bib`);
- `companion/reader/`: the book, `LesDerivateurs_companion.tex`, with its bibliography and the per-part files it
  inputs (`parts/`), all written by `kit/build_global_reader.py`; `OVERLAPS.md` explains how pages that two
  consecutive parts both contain are set once in the book.

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

## Credits

- **Author:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991).
- **Edition transcribed:** the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis (Universités de
  Montpellier II et Paris VII), <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>, in the
  versions listed above. The deciphering of the manuscript, its edition and the editors' notes are theirs.
- **Transcription:** AI-transcribed (Claude Opus 5.5, Anthropic).
- **Companion:** commentary AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checked and integrated by Claude
  Opus 5.5 (Anthropic). The register of claims and the corrections are produced the same way.

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.

See also [RIGHTS_NOTICE.md](RIGHTS_NOTICE.md) (with the French text).
