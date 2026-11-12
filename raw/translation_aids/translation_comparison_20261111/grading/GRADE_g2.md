# Blind grading of the translation comparison: grader g2

Read: `source\LM.tex`, `source\LM_ref.tex`, `source\DER.tex`, `source\DER_ref.tex`, the files of `prompt\` and the versions in `blind\`; nothing else. Each French sentence was compared with all eight versions at that place; a script compared the skeleton of every version (formulas, marks with their nesting and bars, \text, comments, blank lines, page anchors) with the French. The one-page versions (LM C, DER D) were graded on that page. The one-page version is C in LM and D in DER, so a letter need not name the same configuration in both works.

## 1. La Longue Marche, scans 483-487 (ms. pp. 245-247)

Versions LM_A to LM_H; C covers scan 483 only.

### Errors

| # | Ver. | Anchor | Category | Severity | French | English | Fix |
|---|---|---|---|---|---|---|---|
| 1 | A | scan 485 | English | minor | ``` une action effective, relevant une action extérieure admissible ``` | ``` an effective action, lifting an admissible outer action ``` | ``` an actual action, lifting an admissible outer action ``` In English an "effective action" is a faithful one; here he means the true action, as against the outer action it lifts. |
| 2 | B | scan 485 | English | minor | ``` une action effective ``` | ``` an effective action ``` | ``` an actual action ``` In English an "effective action" is a faithful one; here he means the true action, as against the outer action it lifts. |
| 3 | B | scan 486 | meaning | minor | ``` on voit que l'arithmétisation de $\pi''$ \unsure{déduite} de celle de $\pi'$ par ``passage au quotient'', soit celle \unsure{induite} par $\pi$ ``` | ``` we see that the arithmetization of $\pi''$ \unsure{deduced} from that of $\pi'$ by ``passage to the quotient'', is the one \unsure{induced} by $\pi$ ``` | ``` ..., be the one \unsure{induced} by $\pi$ ``` His subjunctive marks a requirement, not an observation; the loose construction is to be kept. |
| 4 | B | scan 487 | marks | minor | ``` \unsure{mettons\|mettant} à part ``` | ``` \unsure{let us set apart\|setting apart} ``` | ``` \unsure{let us set\|setting} apart ``` The doubt covers the verb only. |
| 5 | B | scan 487 | terminology | minor | ``` une \deleted{\unsure{une}} partie $I'\subset I(\pi)$ ``` | ``` a \deleted{\unsure{a}} part $I'\subset I(\pi)$ ``` | ``` a \deleted{\unsure{a}} subset $I'\subset I(\pi)$ ``` |
| 6 | B | scan 487 | English | minor | ``` dans cette optique conjecturale ``` | ``` in this conjectural optic ``` | ``` in this conjectural perspective ``` |
| 7 | D | scan 483 | marks | minor | ``` (1)\qquad 1\longrightarrow\pi\longrightarrow\mathcal E\longrightarrow\Gamma^{+}\longrightarrow1\qquad\text{ou} ``` | ``` ...\qquad\text{ou} (left in French) ``` | ``` ...\qquad\text{or} ``` French wording inside \text is to be translated. |
| 8 | D | scan 483 | marks | minor | ``` $\unsure{\mathrm{Centre}}(\pi)=1$ ``` | ``` $\unsure{\mathrm{Center}}(\pi)=1$ ``` | ``` $\unsure{\mathrm{Centre}}(\pi)=1$ (formula copied unchanged) ``` The one changed formula: notation is unified later, in both languages. |
| 9 | D | scan 483 | marks | minor | ``` dans les \deleted{\illegible{1}} données \unsure{$\mathcal E$} ``` | ``` into the data \unsure{$\mathcal E$} ``` | ``` into the \deleted{\illegible{1}} data \unsure{$\mathcal E$} ``` The struck-out illegible word is lost. |
| 10 | D | scan 483 | meaning | minor | ``` On se borne aux courbes ``` | ``` I restrict to ``` | ``` We restrict ourselves to ``` He writes "on" here and "je" elsewhere; the reference changes. |
| 11 | D | scan 483/484 | marks | minor | ``` respecte \margin{482} \scanpage{484} nécessairement la structure à lacets ``` | ``` necessarily respects \margin{482} \scanpage{484} the loop structure ``` | ``` respects \margin{482} \scanpage{484} necessarily the loop structure ``` The word is moved from scan 484 to scan 483. |
| 12 | D | scan 484 | marks | minor | ``` il \unsure{sera} clair ``` | ``` it will be clear ``` | ``` it \unsure{will be} clear ``` The transcriber's doubt is dropped. |
| 13 | D | scan 485 | English | minor | ``` une action effective ``` | ``` an effective action ``` | ``` an actual action ``` In English an "effective action" is a faithful one; here he means the true action, as against the outer action it lifts. |
| 14 | D | scan 485 | omission | minor | ``` que si $U$ est donnée par une action ext. ..., que les classes de conj. ... \unsure{proviennent} bien toutes de ``` | ``` that if $U$ is given by an outer action ..., the conjugacy classes ... all \unsure{come} from ``` | ``` that if $U$ is given by an outer action ..., that the conjugacy classes ... do all \unsure{come} from ``` The doubled "que" is smoothed away and the emphatic "bien" dropped. |
| 15 | D | scan 485 | terminology | minor | ``` points de $U$ rat/$K$ ``` | ``` points of $U$ rat/$K$ ``` | ``` points of $U$ rational/$K$ ``` Abbreviations are to be written out. |
| 16 | D | scan 486 | meaning | minor | ``` on voit que l'arithmétisation de $\pi''$ ... soit celle \unsure{induite} par $\pi$ ``` | ``` one sees that the arithmetization of $\pi''$ ... is the one \unsure{induced} by $\pi$ ``` | ``` ..., be the one \unsure{induced} by $\pi$ ``` His subjunctive marks a requirement, not an observation. |
| 17 | D | scan 486 | omission | minor | ``` non seulement ils commutent à $\Gamma$, mais encore qu'ils sont dans $N(\pi)$ ``` | ``` not only do they commute with $\Gamma$, but moreover they are in $N(\pi)$ ``` | ``` not only do they commute with $\Gamma$, but moreover that they are in $N(\pi)$ ``` The doubled "que" is smoothed away. |
| 18 | D | scan 486 | marks | minor | ``` \inserted{En fait, \unsure{on va\|on se} décrire une prédiscrétification \unsure{orient.} \uline{stricte}} \deleted{\illegible{3} \unsure{point de base}} bien déterminée de $\pi$ ``` | ``` \inserted{In fact, \unsure{we are going to\|we} describe a well-determined \uline{strict} \unsure{oriented} prediscretification} \deleted{\illegible{3} \unsure{base point}} of $\pi$ ``` | ``` \inserted{In fact, \unsure{we are going to\|we} describe a \uline{strict} \unsure{oriented} prediscretification} \deleted{\illegible{3} \unsure{base point}} well determined of $\pi$ ``` Words of the original line are moved into the interlinear insertion. |
| 19 | D | scan 487 | marks | minor | ``` dont on \unsure{fixe} déjà ``` | ``` for which we \unsure{already fix} ``` | ``` for which we already \unsure{fix} ``` The doubt is widened to "already". |
| 20 | D | scan 487 | terminology | minor | ``` \inserted{et une arithmét. \unsure{a}} ``` | ``` \inserted{and an arithmet. \unsure{a}} ``` | ``` \inserted{and an arithmetization \unsure{a}} ``` Abbreviations are to be written out. |
| 21 | D | scan 487 | terminology | minor | ``` une \deleted{\unsure{une}} partie $I'\subset I(\pi)$ ``` | ``` a \deleted{\unsure{a}} part $I'\subset I(\pi)$ ``` | ``` a \deleted{\unsure{a}} subset $I'\subset I(\pi)$ ``` |
| 22 | D | scan 487 | marks | minor | ``` les \inserted{$\Gamma^{\natural}$-}pts \unsure{du\|de} $\pi$ ``` | ``` the \inserted{$\Gamma^{\natural}$-}points of $\pi$ ``` | ``` the \inserted{$\Gamma^{\natural}$-}points \unsure{of the\|of} $\pi$ ``` The two-reading doubt is dropped. |
| 23 | E | scan 485 | English | minor | ``` une action effective ``` | ``` an effective action ``` | ``` an actual action ``` In English an "effective action" is a faithful one; here he means the true action, as against the outer action it lifts. |
| 24 | E | scan 485 | English | minor | ``` de cette action \unsure{proviennent} bien toutes de points de $U$ ``` | ``` of this action do \unsure{come} all of them from points of $U$ ``` | ``` of this action do all \unsure{come} from points of $U$ ``` |
| 25 | F | scan 483/484 | marks | minor | ``` respecte \margin{482} \scanpage{484} nécessairement la structure à lacets ``` | ``` necessarily respects \margin{482} \scanpage{484} the loop structure ``` | ``` respects \margin{482} \scanpage{484} necessarily the loop structure ``` The word is moved from scan 484 to scan 483. |
| 26 | F | scan 485 | English | minor | ``` de cette action \unsure{proviennent} bien toutes de ``` | ``` of this action \unsure{do come} all from ``` | ``` of this action do all \unsure{come} from ``` Also keeps the doubt on the verb alone. |
| 27 | G | scan 485 | English | minor | ``` une action effective ``` | ``` an effective action ``` | ``` an actual action ``` In English an "effective action" is a faithful one; here he means the true action, as against the outer action it lifts. |
| 28 | G | scan 486 | English | minor | ``` il est sous-entendu que \deleted{\illegible{1}} non seulement ils commutent à $\Gamma$ ``` | ``` it is understood that \deleted{\illegible{1}} not only they commute with $\Gamma$ ``` | ``` it is understood that \deleted{\illegible{1}} not only do they commute with $\Gamma$ ``` |
| 29 | H | scan 484 | English | minor | ``` on prend un \unsure{sous-groupe\|ss-groupe} \inserted{ouvert} $\mathcal E'$ ``` | ``` we take a \unsure{subgroup\|subgroup} \inserted{open} $\mathcal E'$ ``` | ``` we take an \inserted{open} \unsure{subgroup\|subgroup} $\mathcal E'$ ``` Keeping the French position of the insertion gives non-English word order. |
| 30 | H | scan 486 | English | minor | ``` les \unsure{hom} \inserted{``admissibles''} des $\Gamma$-groupes ext. ``admissibles'' ``` | ``` the \unsure{homomorphisms} \inserted{``admissible''} of the ``admissible'' outer $\Gamma$-groups ``` | ``` the \inserted{``admissible''} \unsure{homomorphisms} of the ``admissible'' outer $\Gamma$-groups ``` Same cause as at scan 484. |

Checked and not counted:

- An inserted adjective moved before its noun (``` an \inserted{open} \unsure{subgroup|subgroup} ```, ``` the \inserted{``admissible''} \unsure{homomorphisms} ```, ``` the \inserted{(outer)} automorphisms ```): English order, the same word marked; accepted.
- The French line-break hyphen "sous-/extensions" kept as "sub-/extensions" (A, D, E) or joined: both accepted.
- "geometrically" for "géom." (an adverb here), "we"/"one" for "on", "the image by u", "In this point of view", "the simplest criterion, is that", "left invariant" for "invariées", and the readings ``` \unsure{on va|on se} ``` as "we are going to|we" or "... |we ourselves": accepted.
- D's ``` \unsure{of|of} ``` for ``` \unsure{de|du} ``` before $\pi'$, and B's "that is well determined" inside the struck-out paragraph: accepted.
- Formula and mark skeletons were compared by script: apart from the cases in the table, every version keeps every formula, mark, nesting, bar, blank line and anchor of the French.

### Scores

| Ver. | Fidelity | English | Major | Minor | Character |
|---|---|---|---|---|---|
| A | 9.5 | 8.5 | 0 | 1 | Complete, literal and careful: every mark stays where it stands, and his loose syntax is kept (the doubled "that", the subjunctive "be the one induced"). Its one slip is the calque "effective action", which an English reader may take for "faithful action". |
| B | 8.5 | 8 | 0 | 5 | Complete and generally faithful, with every mark present and his abbreviations written out. It turns the subjunctive "soit" into "is", widens one \unsure to take in "apart", and has three calques ("effective action", "a part I'", "conjectural optic"). |
| C (page 1 only) | 9.5 | 8.5 | 0 | 0 | Covers scan 483 only; there it is error-free, keeps every mark, and even keeps the French order of the qualifiers ("curves geometrically connected (for convenience), anabelian"). One page says nothing about the dense deleted and inserted passages of scans 485-487. |
| D | 6 | 7 | 0 | 16 | Fluent but the least careful version: it drops three marks (a \deleted{\illegible{1}} and two \unsure), moves words across the scan-484 anchor and into an insertion, widens an \unsure, changes \mathrm{Centre} to \mathrm{Center} and leaves \text{ou} in French. It also smooths what the brief says to keep (the doubled "que", the subjunctive "soit", the emphatic "bien"), turns "on" into "I" once, and leaves "rat" and "arithmet." unexpanded. |
| E | 9.5 | 8 | 0 | 2 | Complete and faithful, every mark in place, subjunctives and doubled "that" kept. Two English stumbles: "effective action" and "do come all of them from". |
| F | 9 | 8.5 | 0 | 2 | Faithful and the most idiomatic of the full versions ("an actual action", "rid ourselves", "This does not thereby mean"), all marks kept. It moves "necessarily" back across the scan-484 anchor and has one awkward "do come all from". |
| G | 9.5 | 8 | 0 | 2 | Complete and faithful, every mark in place, the emphatic "bien" well rendered ("indeed all come"). Two English stumbles: "effective action" and "not only they commute". |
| H | 9.5 | 8 | 0 | 2 | The most literal about marks: every mark stays exactly where it stands in the French, and it gets "an actual action" right. The cost is two non-English word orders where an insertion follows its noun (a subgroup "open" E', the homomorphisms "admissible" of the ...). |

Scan 483 alone: A, B, C, E, G and H have no errors there; D has five (errors 7-11), F one (error 25).

### Ranking

Fidelity first, then English; (fidelity / English).

- 1=: A (9.5 / 8.5); C (9.5 / 8.5, page 1 only)
- 3=: E (9.5 / 8); G (9.5 / 8); H (9.5 / 8)
- 6: F (9 / 8.5)
- 7: B (8.5 / 8)
- 8: D (6 / 7)

### Conclusion

No version makes a major error on these pages, and the differences among A, E, F, G and H do not matter to a reader of an edition: each has one or two minor slips (a calque, an awkward order, one word displaced across a page anchor) that a copy-edit catches, and all keep the deletions, insertions, doubts and his loose syntax. B is a step down (a smoothed subjunctive, a widened doubt, three calques). D is the only version whose errors would mislead a reader about the manuscript: it loses and displaces marks, changes a formula and smooths his syntax. Five of the seven full versions write "effective action" for "action effective"; only F and H write "actual action".

## 2. Les Dérivateurs, ch. XVIII, printed pp. 1-5 (ms. pp. 50-60)

Versions DER_A to DER_H; D covers printed page 1 only.

### Errors

| # | Ver. | Anchor | Category | Severity | French | English | Fix |
|---|---|---|---|---|---|---|---|
| 1 | A | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux de procéder comme dans le cas des topos ``` | ``` It is no doubt judicious to proceed as in the case of topoi ``` | ``` It is probably judicious to proceed as in the case of topoi ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 2 | B | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux ``` | ``` It is no doubt wise ``` | ``` It is probably wise ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 3 | B | p. 4 (ms. p. 57) | English | minor | ``` Visiblement, il y a quelque chose de non trivial à démontrer ! ``` | ``` Visibly, there is something nontrivial to prove! ``` | ``` Evidently, there is something nontrivial to prove! ``` |
| 4 | C | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux ``` | ``` It is doubtless judicious ``` | ``` It is probably judicious ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 5 | C | p. 2 (ms. p. 53) | meaning | minor | ``` un pseudo-topos produit [(4.1.4)] qui ait les propriétés d'un 2-produit ``` | ``` a product pseudo-topos [(4.1.4)] which has the properties of a 2-product ``` | ``` which would have the properties of a 2-product ``` His subjunctive states what he wants; the footnote says the result is not a 2-product. |
| 6 | E | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux ``` | ``` It is no doubt judicious ``` | ``` It is probably judicious ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 7 | E | p. 2 (ms. p. 54) | English | minor | ``` l'accent dans le $\uHom^{!'}$ ``` | ``` the accent in the $\uHom^{!'}$ ``` | ``` the prime in the $\uHom^{!'}$ ``` |
| 8 | E | p. 4 (ms. p. 57) | English | minor | ``` Visiblement, il y a ``` | ``` Visibly, there is ``` | ``` Evidently, there is ``` |
| 9 | F | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux ``` | ``` It is no doubt judicious ``` | ``` It is probably judicious ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 10 | F | p. 2 (ms. p. 53) | addition | minor | ``` ce qui équivaut à $f_*$ une équivalence ``` | ``` which amounts to $f_*$ being an equivalence ``` | ``` which is equivalent to $f_*$ an equivalence ``` The elliptic French is completed. |
| 11 | F | p. 2 (ms. p. 53) | meaning | minor | ``` qui ait les propriétés d'un 2-produit ``` | ``` which has the properties of a 2-product ``` | ``` which would have the properties of a 2-product ``` His subjunctive states what he wants; the footnote says the result is not a 2-product. |
| 12 | F | p. 4 (ms. p. 57) | English | minor | ``` Visiblement, il y a ``` | ``` Visibly, there is ``` | ``` Evidently, there is ``` |
| 13 | G | p. 1 (ms. p. 50) | English | minor | ``` (surtout du type exactitude) ``` | ``` (mostly of the type exactness) ``` | ``` (mostly of the exactness type) ``` |
| 14 | G | p. 1 (ms. p. 51), footnote | meaning | minor | ``` $\mathcal{M}$ s'interprète bel et bien comme les “faisceaux” sur cette catégorie $\mathcal{M}$ d'ouverts ``` | ``` $\mathcal{M}$ is interpreted quite literally as the ``sheaves'' on this category $\mathcal{M}$ of open sets ``` | ``` $\mathcal{M}$ is indeed interpreted as the ``sheaves'' on this category $\mathcal{M}$ of open sets ``` "Bel et bien" means indeed/really; his quotation marks show the sense is not literal. |
| 15 | G | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux ``` | ``` It is no doubt judicious ``` | ``` It is probably judicious ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 16 | G | p. 2 (ms. p. 53) | addition | minor | ``` de deux foncteurs adjoints $(f^*,f_*)$ ... ce qui équivaut à $f_*$ une équivalence, ou $\alpha$ et $\beta$ des isomorphismes ``` | ``` consisting of two adjoint functors $(f^*,f_*)$ ... which is equivalent to $f_*$ being an equivalence, or $\alpha$ and $\beta$ being isomorphisms ``` | ``` of two adjoint functors $(f^*,f_*)$ ... which is equivalent to $f_*$ an equivalence, or $\alpha$ and $\beta$ isomorphisms ``` The elliptic French is completed in three places. |
| 17 | G | p. 2 (ms. p. 53) | meaning | minor | ``` qui ait les propriétés d'un 2-produit ``` | ``` which has the properties of a 2-product ``` | ``` which would have the properties of a 2-product ``` His subjunctive states what he wants; the footnote says the result is not a 2-product. |
| 18 | G | p. 2 (ms. p. 53) | terminology | minor | ``` l'indice ! (resp. l'exposant !) ``` | ``` the index ! (resp. the exponent !) ``` | ``` the subscript ! (resp. the superscript !) ``` |
| 19 | G | p. 4 (ms. p. 57) | marks | minor | ``` Il est clair, \texttt{[en]} outre, ``` | ``` It is clear, \texttt{[moreover]}, ``` | ``` It is clear, \texttt{[in]} addition, ``` The editors supplied only "en"; the bracket now claims the whole adverb. |
| 20 | G | p. 4 (ms. p. 57) | omission | minor | ``` Il faut d'ailleurs trouver aussi une petite sous-catégorie strictement génératrice. ``` | ``` We must also find a small strictly generating subcategory. ``` | ``` Besides, we must also find a small strictly generating subcategory. ``` |
| 21 | G | p. 4 (ms. p. 57) | English | minor | ``` Visiblement, il y a ``` | ``` Visibly, there is ``` | ``` Evidently, there is ``` |
| 22 | G | p. 4-5 (ms. pp. 58-59) | marks | minor | ``` \overset{\text{pl. fid.}}{\lhook\joinrel\relbar\joinrel\relbar\joinrel\longrightarrow} in (4.2.3), (4.2.5) and the unnumbered display after (4.2.5) ``` | ``` \text{pl. fid.} left in French (three times) ``` | ``` \text{f.f.} (or \text{fully faithful}) ``` French wording inside \text is to be translated. |
| 23 | G | p. 5 (ms. p. 60) | marks | minor | ``` (4.2.7): "\text{\scriptsize pleinement fidèle}" (three arrow labels) ``` | ``` left in French (three times) ``` | ``` "\text{\scriptsize fully faithful}" ``` French wording inside \text is to be translated. |
| 24 | H | p. 1 (ms. pp. 51 and 52) | English | minor | ``` $\mathcal{M}^\circ$ est également un pseudo-topos; si $\mathcal{M}^\circ$ est également une catégorie pseudo-topos ``` | ``` $\mathcal{M}^\circ$ is equally a pseudo-topos; if $\mathcal{M}^\circ$ is equally a pseudo-topos category ``` | ``` $\mathcal{M}^\circ$ is also a pseudo-topos; if $\mathcal{M}^\circ$ is also a pseudo-topos category ``` False friend, twice. |
| 25 | H | p. 2 (ms. p. 52) | meaning | minor | ``` Il est sans doute judicieux ``` | ``` It is no doubt judicious ``` | ``` It is probably judicious ``` "Sans doute" is a hedge (probably); "no doubt"/"doubtless" can be read as "certainly". |
| 26 | H | p. 2 (ms. p. 54) | English | minor | ``` l'accent dans le $\uHom^{!'}$ ``` | ``` the accent in the $\uHom^{!'}$ ``` | ``` the prime in the $\uHom^{!'}$ ``` |
| 27 | H | p. 4 (ms. p. 57) | English | minor | ``` Visiblement, il y a ``` | ``` Visibly, there is ``` | ``` Evidently, there is ``` |

Checked and not counted:

- "Paratopos" or "Paratopoi" in the section title, "Pseudo-topos" or "Pseudo-topoi" in 4.1: the French plural is invariable; either reading accepted.
- The misprint "par forcément" rendered "not necessarily" (all), the [sic] "adjoint à droite" kept as "right adjoint" (all), the undefined ``` \mathcal{Q} ``` kept (all): correct handling.
- "second member", "make precise", "formed of", "the functor restriction to", "well and truly", "f.f."/"f. f."/"fully faith."/"f. faithful" for "pl. fid.", and ``` \textit{strictly generating} ``` moved before its noun (B, C, G): accepted.
- Formula and macro skeletons were compared by script: no DER version changed a formula; G's \text labels are unchanged only because they were not translated.

### Scores

| Ver. | Fidelity | English | Major | Minor | Character |
|---|---|---|---|---|---|
| A | 9.5 | 9 | 0 | 1 | The most accurate and idiomatic version: it keeps the editors' brackets, the [sic] "right adjoint", the redundant "in addition ... in addition", the elliptic "`f_*` an equivalence" and the subjunctive "which would have", with apt English ("the prime", "the right-hand side", "Evidently"). Its one slip, shared by every full version, is "no doubt" for the hedge "sans doute". |
| B | 9.5 | 8.5 | 0 | 2 | Accurate and complete in natural English ("I claim that", "the prime"), with the ellipses and subjunctives kept. Two slips: "no doubt" for "sans doute" and "Visibly" for "Visiblement". |
| C | 9 | 9 | 0 | 2 | Complete and well written ("Clearly", "the prime", "[in] addition"). It turns the subjunctive "qui ait les propriétés d'un 2-produit" into "which has the properties", which the footnote then contradicts, and writes "doubtless" for "sans doute". |
| D (page 1 only) | 9.5 | 9 | 0 | 0 | Covers printed page 1 only; there it is error-free, keeping the misprint "par forcément" as "not necessarily" under its comment, the unclosed parenthesis and the doubled "moreover ... moreover". One page says nothing about the diagrams, labels and editors' additions of pages 2-5. |
| E | 9.5 | 8 | 0 | 3 | Faithful and complete, subjunctives kept ("which should have", "be in"). Its English has calques: "the accent" for the prime and "Visibly", besides "no doubt". |
| F | 8.5 | 8.5 | 0 | 4 | Complete, with a neat "[more]over" for the editors' "[en] outre". It completes one ellipsis ("`f_*` being an equivalence"), turns "qui ait" into "which has", and has "Visibly" and "no doubt". |
| G | 7 | 7.5 | 0 | 11 | The weakest DER version: it leaves "pl. fid." and "pleinement fidèle" in French inside \text in four displays, brackets the whole "moreover" as an editors' addition, drops "d'ailleurs", completes ellipses and turns "qui ait" into "which has". It adds calques ("the index ! (resp. the exponent !)", "of the type exactness") and "quite literally" for "bel et bien". |
| H | 9.5 | 7.5 | 0 | 4 | Faithful in content, subjunctives kept. Its English is the most stilted ("equally" for "également" twice, "the accent", "Visibly", "One must besides also find"). |

Printed page 1 alone: A, B, C, D, E and F have no errors there; G has two (errors 13-14), H one (error 24).

### Ranking

Fidelity first, then English; (fidelity / English).

- 1=: A (9.5 / 9); D (9.5 / 9, page 1 only)
- 3: B (9.5 / 8.5)
- 4: E (9.5 / 8)
- 5: H (9.5 / 7.5)
- 6: C (9 / 9)
- 7: F (8.5 / 8.5)
- 8: G (7 / 7.5)

### Conclusion

No version makes a major error. A and B are equivalent for a reader of an edition, with E and H close behind (English calques only: "the accent", "Visibly", "equally"). C, F and G turn the subjunctive "qui ait les propriétés d'un 2-produit" into "which has", which the footnote corrects for the reader; F and G also complete his ellipses. G is the only version that needs repair: French left inside \text in four displays, an editors' bracket widened, a word dropped. Every full version renders "sans doute" as "no doubt" or "doubtless", and five of seven write "Visibly" for "Visiblement".

## 3. Conclusion

No version makes a major error: all keep the mathematics and the page structure, and only LM D (three marks dropped, words moved across an anchor and into an insertion, \mathrm{Centre} changed, \text{ou} left in French) and DER G (French left in \text labels, an editors' bracket widened) mishandle formulas, marks or brackets in more than one place. The top versions (LM: A, then E, G and H, then F; DER: A and B, then E and H; the one-page versions LM C and DER D are clean on their page) differ by one or two minor slips each, calques such as "effective action", "Visibly" and "the accent" or a smoothed subjunctive, which do not matter to a reader of an edition and fall to a light copy-edit. Only LM D (lost and displaced marks, smoothed syntax) and DER G (untranslated labels, completed ellipses, a dropped word) would need real repair, and the slips shared by most versions ("no doubt" for "sans doute", "effective action" for "action effective") are worth adding to the briefs.
