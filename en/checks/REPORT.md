# Run report

## Batches (GPT-6.1 Sol, reasoning effort max, OpenAI Responses API, Flex tier)

| batch | requests | translated | refused by Flex | edition pages translated | tokens in | tokens out (reasoning) | minutes |
|---|---|---|---|---|---|---|---|
| b01-pilot | 5 | 5 | 0 | 25 | 24,466 | 85,994 (68,008) | 19.4 |
| b02 | 60 | 60 | 2 | 294 | 344,947 | 1,184,421 (923,851) | 67.3 |
| b03 | 60 | 38 | 106 | 180 | 201,869 | 692,632 (540,164) | 27.6 |
| b04 | 75 | 71 | 232 | 343 | 399,592 | 1,310,781 (1,007,550) | 196.4 |
| b05 | 65 | 65 | 0 | 316 | 442,571 | 1,388,593 (1,033,911) | 12.7 |
| b06 | 4 | 4 | 0 | 18 | 25,105 | 85,192 (66,552) | 7.2 |
| all | 269 | 243 | | 1176 | 1,438,550 | 4,747,613 (3,640,036) | |

Edition pages translated (each unit counted once): 1176 of 1176; units 243 of 243; units translated twice (re-run after a check): 0; not translated: 0.


## Checks of the raw output, as it came back

243 units checked: 221 pass, 22 fail.
- French left: 20 units
- glossary: 3 units
- formulas identical (or up to spacing): 46019 of 46072; changed only in the wording of text-mode boxes: 45; moved: 7; glossary entry-pages with the English form: 9749 of 9759

## Checks of the English units (raw output plus fixes)

243 units checked: 243 pass, 0 fail.
- formulas identical (or up to spacing): 46016 of 46072; changed only in the wording of text-mode boxes: 47; moved: 7; glossary entry-pages with the English form: 9752 of 9759

## Fixes (checks/FIXES.jsonl)

41 fixes in 33 units:
- Der-ChV-234_p031-034: 'canulars' (his word for a blunder; 'un très gros canular' is 'a very big blunder' in Der-ChI-234_p036-040): 'hoaxes' misreads it
- Der-ChVII-456_p006-010: French left in a formula: 'réd' (réduit) is 'red' in the English, as the macros \red and \cardred print it (common_dt.MACRO_EN)
- Der-ChXIIa-012_p026-030: French left in a formula: 'dans' in an \textit box inside a display, translated
- Der-ChVII-456_p031-035: French left in a formula: 'réd' (réduit) is 'red' in the English, as the macros \red and \cardred print it (common_dt.MACRO_EN)
- Der-ChIX-678_p001-005: French left in a formula: 'dans' in an \textit box
- der-ch16_p011-015: French left in a formula: 'dans' in an \textit box
- Der-ChXV-05-11-10_p006-010: French left in a formula: 'et' in an \textit box ('\text{with}' before it was translated)
- Der-ChXV-05-11-10_p011-015: French left in a formula: 'avec' in an \textit box
- Der-ChXV-05-11-10_p011-015: French left in a formula: 'avec' in \textit boxes
- Der-ChXV-05-11-10_p011-015: French left in a formula: 'si' in \textit boxes
- Der-ChXV-05-11-10_p011-015: French left in a formula: 'd'où' in an \textit box
- Der-ChXV-05-11-10_p066-070: French left in a formula: 'pour tout' in an \textit box
- der-ch16_p006-010: French left in a formula: 'déf' over the equality sign is 'def', as the macro \defeq prints it (common_dt.MACRO_EN)
- Der-ChXIIb-012_p041-045: French left in a formula: 'non commutatif!' in a \shortstack of a diagram
- Der-ChXV-05-11-10_p001-005: French left in a formula: a \parbox of the display left in French; 'limite inductive' is 'direct limit' (glossary)
- Der-ChX-789_p001-005: glossary: 'W-équivalence universelle' is 'universal W-equivalence' (the italics kept on the adjective)
- Der-ChX-789_p001-005: glossary: 'fibrations cohomologiques (resp. homologiques) faibles' are 'weak cohomological (resp. homological) fibrations' (the italics kept on the adjective)
- der-ch17_p011-015: French left in a formula: 'déf' over the equality sign is 'def', as the macro \defeq prints it (common_dt.MACRO_EN)
- der-ch18_p016-020: French left in a formula: 'dans' in an \textit box
- der-ch18_p036-040: French left in a formula: 'réd' (réduit) is 'red' in the English, as the macros \red and \cardred print it (common_dt.MACRO_EN)
- der-ch18_p066-070: French left in a formula: 'avec' in an \textit box
- der-ch18_p071-075: French left in a formula: 'réd' (réduit) is 'red' in the English, as the macros \red and \cardred print it (common_dt.MACRO_EN)
- der-ch18_p091-095: French left in a formula: 'réd' (réduit) is 'red' in the English, as the macros \red and \cardred print it (common_dt.MACRO_EN)
- der-ch18_p091-095: French left in a formula: 'déf' over the equality sign is 'def', as the macro \defeq prints it (common_dt.MACRO_EN)
- der-ch18_p101-105: French left in a formula: 'si' in an \textit box
- der-ch18_p131-135: French left in a formula: 'déf' over the equality sign is 'def', as the macro \defeq prints it (common_dt.MACRO_EN)
- der-ch18_p186-190: French left in a formula: 'si' in \textit boxes
- der-ch18_p186-190: French left in a formula: 'grande devant' in an \textit box; 'grand devant' is 'large relative to' (glossary)
- der-ch18_p191-195: glossary: topos, plural topoi (his English), so paratopoi, as in the table of contents (dertbmt) and in der-ch18_p101-105
- Der-ChI-234_p021-025: the French writes the prefix in lower case here (hot-équivalence; once 'hot équivalence'); the English follows the French, as the glossary's 'Hot-equivalence' renders Grothendieck's 'Hot-équivalence' (completeness check of 12 Nov, COMPLETENESS_20261112.csv)
- Der-ChI-234_p026-030: the French writes the prefix in lower case here (hot-équivalence; once 'hot équivalence'); the English follows the French, as the glossary's 'Hot-equivalence' renders Grothendieck's 'Hot-équivalence' (completeness check of 12 Nov, COMPLETENESS_20261112.csv)
- Der-ChI-234_p031-035: the French writes the prefix in lower case here (hot-équivalence; once 'hot équivalence'); the English follows the French, as the glossary's 'Hot-equivalence' renders Grothendieck's 'Hot-équivalence' (completeness check of 12 Nov, COMPLETENESS_20261112.csv)
- Der-ChII-234_p001-005: the French writes the prefix in lower case here (hot-équivalence; once 'hot équivalence'); the English follows the French, as the glossary's 'Hot-equivalence' renders Grothendieck's 'Hot-équivalence' (completeness check of 12 Nov, COMPLETENESS_20261112.csv)
- der-ch16_p041-045: French left in a formula: 'connexe' in the \textit subscript of Cat (edition page 43), translated as in the \text subscripts of the same unit ('0-connected')
- Der-ChXIIb-012_p056-060: French left in a footnote: 'W(7 bis faible)' is the weak form of W(7 bis), as the other two footnotes of the unit put it ('weak form', 'W(7 bis) in weak form')
- Der-ChXIII-25-01-04_p066-066: bibliography: the title of a published work stays in its language (Verdier's thesis, Astérisque 239), as the English titles of the list and the journal names stay as they are
- Der-ChXIII-25-01-04_p066-066: bibliography: the title of SGA 4 and the name of the seminar stay in French (the published title)
- Der-ChXIIc-30-03-03_p061-064: LaTeX error of the transcription (the same in its French book): the diagram's baseline names the empty cell (2,1), which has no node; the baseline is now the cell of T_1 (2,2), the same row; no text changes
- Der-ChI-234_p026-030: the label of the dashed arrow in the diagram of edition page 27 (French 'cas de hot-équivalence costricte'): the French writes the prefix in lower case, as in the prose of this unit (fixed by the regex fix of 12 Nov, which does not reach formulas)
- Der-ChXIIc-30-03-03_p036-040: the edition hyphenates 'immersion' across the end of its page 154 ('une imm-' / 'ersion ouverte de Dwyer'); the translation gave 'an imm-' / 'open ersion of Dwyer', which reads as a broken word; now 'an open Dwyer imm-' / 'ersion', the glossary's 'open Dwyer immersion' cut at the same place (the reader joins the two halves)
- Der-ChXIIc-30-03-03_p041-045: the edition hyphenates 'immersion' across the end of its page 154 ('une imm-' / 'ersion ouverte de Dwyer'); the translation gave 'an imm-' / 'open ersion of Dwyer', which reads as a broken word; now 'an open Dwyer imm-' / 'ersion', the glossary's 'open Dwyer immersion' cut at the same place (the reader joins the two halves)

## Waivers (checks/WAIVERS.jsonl: a check that misfired on a correct translation)

13 waivers in 12 units:
- Der-ChVI-345_p031-035, glossary entry 'fibration gauche, fibration droite', page 30: the French pattern matches 'en mettant les fibrations à droite, pas à gauche' (where to draw them in the diagram); the English 'putting the fibrations on the right, not on the left' is correct
- Der-ChVI-345_p021-025, glossary entry 'catégorie fibrée, cofibrée', page 19: 'fibrés scindés' names the four categories Fibsc, Cofibsc, Fibsc_0, Cofibsc_0 (fibered and cofibered); 'split fibrations' covers both and is kept
- Der-ChII-234_p061-065, formulas: 1 changed, 0 missing, 0 added: the tikzcd diagram of edition page 60: only the wording of a tabular cell differs ('cela n'implique \textit{·} $X$ cofiltrante' -> 'this does \textit{·} imply $X$ cofiltering', English word order around the illegible word); every math piece is unchanged
- Der-ChXIV-07-10-10_p006-010, glossary entry 'catégorie de modèles', page 7: Quillen's notion ('une catégorie de modèles fermée de Quillen'): 'model category', as the glossary's note keeps it for Quillen's notion
- Der-ChXIV-07-10-10_p006-010, glossary entry 'catégorie de modèles', page 8: Quillen's notion ('la catégorie de modèles des espaces topologiques pointés', '... des complexes d'une catégorie abélienne'): 'model category', as the glossary's note keeps it for Quillen's notion
- der-ch16_p001-005, glossary entry 'W-équivalence fine, grossière, complète, locale, colocale', page 2: the French pattern fires on 'localement' ('une §-équivalence localement sur §'); the English 'a §-equivalence locally over §' is right
- Der-ChXV-05-11-10_p051-055, French left: 0 sentences, 1 formula boxes, 0 elisions: 'Mon' in the \parbox of (7.2.6) is the class of monomorphisms (notation; \Mon elsewhere), as in the French, not the French word
- Der-ChXV-05-11-10_p016-020, formulas: 1 changed, 0 missing, 0 added: edition page 22: the inline formula with two tabulars under \underbrace is cut into fragments by the checks' pairing of $ signs; the tabular wording is translated ('à isomorphisme près' -> 'up to isomorphism'), every math piece unchanged (checked by hand)
- der-ch18_p181-185, French left: 0 sentences, 1 formula boxes, 0 elisions: '\underline{\text{Ép}}' is notation (the category of epimorphisms; the macro \uEp prints it in der-ch18_p146-150), kept as in the French like Fl and Ob
- Der-ChXV-05-11-10_p026-030, glossary entry 'catégorie de modèles', page 25: Quillen's notion ('la définition des catégories de modèles de Quillen clos'): 'Quillen's closed model categories', as the glossary's note keeps 'model category' for Quillen's notion
- der-ch19_p001-005, glossary entry 'flèche', page 1: 'le demi-sommet de flèche' is 'the half-arrowhead'; the pattern \barrows?\b does not match inside 'arrowhead'
- Der-ChXIIc-30-03-03_p061-064, formulas: 1 changed, 0 missing, 0 added: the one changed formula is the LaTeX fix of 12 Nov (checks/FIXES.jsonl): the tikz-cd baseline named the empty cell (2,1), which has no node and stops the compilation, in the French book as well; it now names the cell of T_1 (2,2) in the same row; the printed diagram and its text are unchanged
- Der-ChXIII-25-01-04_p066-066, French left: 1 sentences, 0 formula boxes, 0 elisions: bibliography: the titles of published works stay in their language (Verdier's thesis 'Des catégories dérivées des catégories abéliennes'; SGA 4 'Théorie des Topos et Cohomologie Étale des Schémas', Séminaire de Géométrie Algébrique du Bois-Marie), as the journal names (Cahiers de Topologie et Géométrie Différentielle, Astérisque) do
