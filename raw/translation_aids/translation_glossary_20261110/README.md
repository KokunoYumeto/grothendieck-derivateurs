# Terminology, notation and typesetting for the English *Les Dérivateurs* and *La Longue Marche*

Made by Claude (Fable 5.2, subagent) on 10 Nov 2026, at the user's request of that day: "one of these agents should
just be asked normalize terminology ... That gives a nice little word list. And the normalization will also sort of
normalizing typesetting, normalizing everything." Nothing is translated here and no source file was changed. These
tables fix the words and forms; the translation comes later, in batches, with the glossary in every request.

## The files

| File | Rows | What it is |
|---|---|---|
| `GLOSSARY_DER.csv` | 171 | French term, the variants found with counts, the English, its source, a note |
| `GLOSSARY_LM.csv` | 116 | the same for La Longue Marche, with his abbreviations at the end |
| `NOTATION_DER.csv` | 26 | notation that varies between chapters of the edition, and one form for the English |
| `NOTATION_LM.csv` | 28 | his notation where it varies for one object, and one form for the English |
| `TYPESETTING.csv` | 26 (10 DER, 16 LM) | one written form encoded in several ways by our transcription; unified in both languages |
| `scripts\` | | the inventory scripts and the decision files the CSVs are built from |
| `inventory\` | | the n-gram, alphabet, operator-name, symbol and macro inventories, the search lists and their outputs |

The CSVs are built by script from the decision files (`scripts\entries_DER.txt`, `entries_LM.txt`,
`notation_DER.txt`, `notation_LM.txt`, `typesetting.txt`): every count in them is what the regular expression in
the decision file found, so a changed decision is one edited line and a rerun
(`python -I build_glossary.py DER`, `python -I build_tables.py`).

## What was counted

| | Les Dérivateurs | La Longue Marche |
|---|---|---|
| Source | `derivateurs_opus_pilot_20261109\out_all\<chapter>\*.tex` | per package the first of `second_pass\LM_<KEY>_checked_fixed.tex`, `_checked.tex`, `answers\fixed`, `answers\unzipped`, `answers` |
| Files | 233 (22 chapters) | 116 packages: 27 checked and fixed, 70 checked, 9 fixed first pass, 7 first pass (cote 140-1 and four of 140-4), 3 pilot (P01, P02, P04) |
| Characters | 3,209,572 | 3,003,369 (with the location comments) |
| Page markers | 1,126 printed pages | 1,588 scans |
| n-gram groups (1 to 3 words, outside formulas) | 24,509 | 23,095 |

In the n-gram inventories, spelling, accent, hyphen, number and gender variants are grouped under one key
(`inventory\DER_ngrams.csv`, `LM_ngrams.csv`). A formula inside a compound is shown as `§` ("§-asphérique" is
"$W$-asphérique"). Each of the 233 Dérivateurs files has its own preamble; the macros are expanded before counting.
The Longue Marche counts include the printed university forms on whose backs he wrote (the words "Montpellier",
"CNRS" and the like, 179 times); they are not in the glossary.

## English sources, in the order of authority given

1. **Grothendieck's own English: *Pursuing Stacks*.** Local TeX of the Scrivener edition
   (`pursuing_stacks_expert_20261110\src\ps1.tex` to `ps7.tex`, CC0). "PS §n (k)" is section n of that edition and
   k occurrences. 102 of the 170 Dérivateurs entries and 13 of the Longue Marche entries rest on it.
2. **The English *Sketch of a Programme*** (the translation of the Esquisse in *Geometric Galois Actions 1*), read at
   https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseEng.pdf. "Sketch p. n" is the book page
   (pdf page + 236). 32 Longue Marche entries.
3. **Our own editions**: ega-en (`ega_scan_check_20261101\ega-en\tex`) and the English SGA 3
   (`rights_cc0_20261025\sga-en\sources\native\SGA3`). 3 and 18 entries.
4. **The literature**: Cisinski, *Higher Categories and Homotopical Algebra* (2019),
   https://cisinski.app.uni-regensburg.de/CatLR.pdf ("Cis19 p. n", printed page), and the nLab pages named in the
   entries. Used where PS has no word (prederivator, accessible, transfinite composition) and to record the modern
   term beside his.
5. **"ours"**: no source found; a literal or calqued form. 62 Dérivateurs entries and 46 Longue Marche entries, most
   of them his coinages (quillénisable, paratopos, discrétification, topos multigaloisien).

Not found in a freely accessible form: Schneps's article "Grothendieck's 'Long March through Galois theory'"
(Cambridge, behind a paywall), which may name the Longue Marche notions in English. The English SGA 1 and SGA 4
trees of the sga-en clone were not searched (the search found only a few of their files).

## What was decided, and why

- **His own words in English stay his.** localiseur fondamental is "basic localizer" (PS, 78 times; he glosses it so
  himself in Les Dérivateurs VI, p. 1: "localisateur fondamental (basic localiser)"); modérément saturé is "mildly
  saturated" (his own gloss in Ch. XVI); asphérique "aspheric", homotopisme "homotopism", modélisateur "modelizer",
  crible "sieve", objet final "final object" (192 times; "terminal object" never), topos "topoi" in the plural,
  semi-simplicial "semi-simplicial", scholie "scholie".
- **His coinages are kept, and a later standard term is recorded beside them, never substituted**: cofinal (with
  "final functor"), somme amalgamée "amalgamated sum" (with "push-out"), homotopiquement cartésien "homotopically
  cartesian" (with "homotopy Cartesian"), grand devant π "large relative to π" (with "π-filtered", not checked in a source), fibration
  gauche "left fibration" (the literature uses that name for another notion), contrafoncteur "contrafunctor".
- **Two words are kept apart where English would merge them**: catégorie de modèles (a pair (M, W)) is "category
  of models", Quillen's notion stays "model category"; couple de Quillen is "Quillen couple", because "Quillen pair"
  means an adjunction; sous-groupe invariant "invariant subgroup" and sous-groupe distingué "normal subgroup";
  opération "operation" and action "action"; commutant "commutant" and centralisateur "centralizer".
- **Spelling: American, in both works**, because his own English is (PS: fiber 174 against fibre 10, fibered 52
  against fibred 0, -ize throughout). The Sketch translation and our EGA-en are British.
- **Notation of Les Dérivateurs**: the edition was typed over ten years and its chapters differ (Ch. I: blackboard
  D, sans serif HOT, short arrows, blackboard Z; the others: bold D, roman HOT, long arrows, bold Z). This was
  checked on three page images (Ch. I p. 51; Ch. II pp. 3 and 9; Ch. XIIb, pdf page 53). The English gets one form for each;
  the French keeps the print.
- **Typesetting**: the one certain transcriber's inconsistency in Les Dérivateurs is the calligraphic X, typed
  `\mathcal{X}` 187 times and `\mathscr{X}` 182 times in alternating five-page batches; the print has one letter.
  The rest is `\mathrm` against `\operatorname` for the same operator, `\tilde` against `\widetilde`, quotation
  marks typed in four ways, and 233 preambles that define the same macro names differently.
- **La Longue Marche**: his abbreviations (hom, isom, autom, ss-groupe, ssi, tt, pts, the m with a bar for "même")
  are listed with their English; the proposal is to write them out. Equation numbers are typed `\tag{n}` 1,256
  times and `(n)\qquad` 1,400 times: one form.

## Open questions for the user (all decided on 10 Nov; see Decisions below)

1. **limite inductive / projective.** His English has "direct limit" (114) and "inverse limit" (81); our EGA-en
   has "inductive limit" (182) and "projective limit" (119), and the English SGA 3 has both pairs. The glossary
   follows the rule (his own English wins) and gives "direct limit", "inverse limit". This makes the new editions
   differ from EGA-en. Keep it so, or follow EGA-en?
2. **Spelling.** American for both works, as proposed, or British as in EGA-en and the Sketch (fibre,
   neighbourhood, centre)? Our English SGA 3 mixes the two (fiber 796, fibre 296).
3. **groupe à lacets** (129). Proposed "group with loops", "loop structure", "loop relation". "Loop group" is
   shorter but in English means the group of loops in a group. No freely accessible English source names the notion.
4. **extérieurement** (35) and **groupe extérieur** (67). Proposed "outerly" and "outer group", on the Sketch's
   "outer action". The alternative for the adverb is a phrase ("by outer automorphisms").
5. **The letter of the derivator.** Bold D (15 chapters of the edition) is proposed; the literature and Ch. I have
   blackboard D.
6. **(Cat), (Hot), (Sets) in parentheses.** Proposed for the English because *Pursuing Stacks* writes them so; the
   edition mostly prints Cat, Hot, Ens without. And should (Ens) become (Sets), as he does in English?
7. **Opposite category**: `^o` in chapters II to XI, `^\circ` from XII on (486 against 781). Proposed `^\circ`.
   The print of II to XI was not checked: if it has a small circle there too, this is a typesetting matter and
   the French is unified as well.
8. **Sl, Gl or SL, GL** in La Longue Marche (512 and 356 against 65 and 48). Proposed: his Sl, Gl.
9. **Two readings that only the scans can settle**, each once for the whole manuscript: the exponent read as
   `\natural` or `\sharp` (683 doubt marks), and the script capital read as Fraktur S, calligraphic G or
   calligraphic S (35 doubt marks for calligraphic G against Fraktur S alone; at least two different objects). Other frequent pairs: ξ or ζ (210), ν or v
   (112), ω or w (80), P or p (344). List: `inventory\LM_unsure_symbol_pairs.csv`. Until then the English copies
   both readings.
10. **His abbreviations in the English Longue Marche**: written out (proposed), or kept short as he writes?
    The same for his underlining: italic in the English (proposed), or underlined as in the transcription?
11. **Register.** bordélique "messy", canulé "botched", itou "likewise", fourbi kept in French with a gloss, AQT
    kept with the editors' gloss. Say if the coarser or the plainer word is wanted.
12. **scholie.** "scholie" as he writes in English, or "Scholium" as in our English SGA 3 (32)?
13. **Inclusion signs in Les Dérivateurs**: `\subset` in some chapters, `\subseteq` in others (975 against 261),
    same meaning. Left as printed. Unify in the English?

## Limits

- The inventories were read, with samples; the two texts were not read through. A term that occurs fewer than
  three times and is not hyphenated may be missing.
- The corrections of the Pro audits of Les Dérivateurs are not yet applied, and 19 Longue Marche packages have no
  second pass: counts will move a little.
- Page images were looked at for four questions only (the letter D, the calligraphic X, the arrows, bold Z). Every
  other statement about "the print" rests on the pattern of the counts by chapter.
- Sources named "ours" are proposals, to be changed by editing one line of the decision file.

## Decisions, 10 Nov 2026

The user, 10 Nov: "please don't fucking ask me to make decisions like that ... You make them. You know more about this
than I do." Decided by Claude on the evidence above; each is one line in `scripts/`, and the tables are rebuilt.

1. Limits: "direct / inverse limit", his English (PS §5); our EGA-en keeps "inductive / projective".
2. Spelling: American in both works, as his English is; EGA-en and the Sketch stay British.
3. Groupe à lacets: "group with loops" ("loop group" means something else).
4. Groupe extérieur: "outer group"; extérieurement: no coined adverb, an English phrase in context ("acts by outer
   automorphisms", "commute as outer actions").
5. The derivator: blackboard D in the English, as in Ch. I and the literature; to check against the manuscript scans
   (cotes 157-160) when they are downloaded.
6. (Cat), (Hot), (Sets) in parentheses as in PS; (Ens) becomes (Sets).
7. Opposite category: ^{\circ} throughout the English.
8. SL, GL in the English; the French keeps his Sl, Gl.
9. The exponent read as natural or sharp, and the script capital read as Fraktur S or calligraphic G/S: PENDING, to be
   settled on the scans on 11 Nov, once for the whole manuscript; a script then resolves the doubt marks.
10. His abbreviations written out in the English; "ssi" becomes "iff" (his English). His underlining stays \uline in
    the English, italic in a reading view; underlined symbols stay underlined.
11. Register: bordélique "messy", canulé "botched", fourbi kept in italics with the gloss "(gear)" at first use, AQT
    kept with the editors' gloss.
12. "scholie" and "theorem-scholie", his English (PS §86); our SGA 3 keeps "Scholium".
13. Inclusion: \subset throughout the English; the French keeps the print.

## Decisions, 11 Nov 2026 (from the blind grading of the translation comparison)

- "action effective", where it is opposed to "action extérieure" (La Longue Marche, e.g. scan 485): **actual action**.
  In English an "effective action" is a faithful one. Elsewhere, where he means a faithful action, keep "effective".
- "sans doute": **probably** (his hedge), not "no doubt" or "doubtless".
- Both are entered in the decision files (`entries_LM.txt`: "action effective", "sans doute"; `entries_DER.txt`: "sans
  doute"; "action effective" does not occur in Les Dérivateurs) and the two glossaries were rebuilt on 11 Nov
  (`build_glossary.py`): the only change is the three new rows (DER 171 entries, LM 116). The files before the change
  are kept in `derivateurs_translation_20261111\glossary_before_20261111\`.
- The translation route chosen on this comparison: GPT-6.1 Sol, reasoning effort max (OpenAI Flex), with this
  glossary in the prompt (`translation_comparison_20261111/RUNS.md`, last section).
