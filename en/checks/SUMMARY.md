# Check results of the English units

243 of 243 units checked; 243 pass, 0 fail. Per unit: `checks/units/<unit>.md`; all figures: `CHECKS.json`.

## Checks waived (false alarms on a correct translation; checks/WAIVERS.jsonl)

- Der-ChVI-345_p021-025: glossary, missing: catégorie fibrée, cofibrée (page 19, 1 in the French) (waived: 'fibrés scindés' names the four categories Fibsc, Cofibsc, Fibsc_0, Cofibsc_0 (fibered and cofibered); 'split fibrations' covers both and is kept)
- Der-ChVI-345_p031-035: glossary, missing: fibration gauche, fibration droite (page 30, 1 in the French) (waived: the French pattern matches 'en mettant les fibrations à droite, pas à gauche' (where to draw them in the diagram); the English 'putting the fibrations on the right, not on the left' is correct)
- Der-ChXIV-07-10-10_p006-010: glossary, missing: catégorie de modèles (page 7, 3 in the French) (waived: Quillen's notion ('une catégorie de modèles fermée de Quillen'): 'model category', as the glossary's note keeps it for Quillen's notion); glossary, missing: catégorie de modèles (page 8, 2 in the French) (waived: Quillen's notion ('la catégorie de modèles des espaces topologiques pointés', '... des complexes d'une catégorie abélienne'): 'model category', as the glossary's note keeps it for Quillen's notion)
- Der-ChXV-05-11-10_p016-020: formulas: 1 changed, 0 missing, 0 added (waived: edition page 22: the inline formula with two tabulars under \underbrace is cut into fragments by the checks' pairing of $ signs; the tabular wording is translated ('à isomorphisme près' -> 'up to isomorphism'), every math piece unchanged (checked by hand))
- Der-ChXV-05-11-10_p026-030: glossary, missing: catégorie de modèles (page 25, 1 in the French) (waived: Quillen's notion ('la définition des catégories de modèles de Quillen clos'): 'Quillen's closed model categories', as the glossary's note keeps 'model category' for Quillen's notion)
- Der-ChXV-05-11-10_p051-055: French left: 0 sentences, 1 formula boxes, 0 elisions (waived: 'Mon' in the \parbox of (7.2.6) is the class of monomorphisms (notation; \Mon elsewhere), as in the French, not the French word)
- der-ch16_p001-005: glossary, missing: W-équivalence fine, grossière, complète, locale, colocale (page 2, 1 in the French) (waived: the French pattern fires on 'localement' ('une §-équivalence localement sur §'); the English 'a §-equivalence locally over §' is right)
- der-ch18_p181-185: French left: 0 sentences, 1 formula boxes, 0 elisions (waived: '\underline{\text{Ép}}' is notation (the category of epimorphisms; the macro \uEp prints it in der-ch18_p146-150), kept as in the French like Fl and Ob)
- der-ch19_p001-005: glossary, missing: flèche (page 1, 1 in the French) (waived: 'le demi-sommet de flèche' is 'the half-arrowhead'; the pattern \barrows?\b does not match inside 'arrowhead')

## Totals over the checked units

formulas identical (or up to spacing) 46017 of 46072, changed only in the wording of text-mode boxes 47, moved 7; page anchors 3198; glossary entry-pages with the English form 9752 of 9759; units with points to review 81
