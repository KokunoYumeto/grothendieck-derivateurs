# POLES: background to put in the zip

Paths are relative to `C:\Users\user\Documents\derivateurs_companion_20261109\`. "(m)" after an arXiv number means the number is from memory: resolve it by the exact title before fetching.

## Grothendieck's text (LaTeX transcription, plus the edition's pages for the unaudited chunks)
- `packages/DER_XI-XIIa/DER_XI-XIIa_text.tex` (XII §§I–IV: characterization of `W∞`, Théorèmes 1–2, the variants of W(4)); also `DER_XI-XIIa_pages.pdf`. Not yet audited.
- `packages/DER_XIIb-a/DER_XIIb-a_text.tex` (XII ms. 59–122: W(7), W(7 bis), Théorème 2 at ms. 78).
- `packages/DER_XIIb-b/DER_XIIb-b_text.tex` (XII ms. 115–169).
- `packages/DER_XIIc-a/DER_XIIc-a_text.tex` (XII ms. 171–234: `a_n, b_n, c_n`; mapping cylinder ms. 228–234).
- `packages/DER_XIIc-b/DER_XIIc-b_text.tex` and `DER_XIIc-b_pages.pdf` (XII ms. 235–272: §7 fibre axioms, §8 "Retour sur les axiomes W(7), W(7 bis)"). Not yet audited.
- `packages/DER_XIIapp/DER_XIIapp_text.tex`.
- `packages/DER_XVI/DER_XVI_text.tex` and `DER_XVI_pages.pdf` (the Loc axioms; §3 Loc (6); §4 Loc (7); §5 Théorème 5.4; §6 Théorème 6.1 and 6.4; §7). Not yet audited.
- `packages/DER_VI-a/DER_VI-a_text.tex` (VI ms. 43–45: new L5) and `packages/DER_VI-c/DER_VI-c_text.tex` (VI ms. 171–187: W(4a), W(4b)).

## Companion (audited chunks only)
For each of `DER_XIIb-a`, `DER_XIIb-b`, `DER_XIIc-a`, `DER_XIIapp`, `DER_VI-a`, `DER_VI-c`: `checks/DER_<id>/DER_<id>_overview.tex`, `_blocks.tex`, `_claims.csv`, `_references.bib`, and `derivateurs_companion.sty`. The blocks that matter most: XIIb-a "A finite counterexample to the asserted reverse excision" (ms. 78), "What the symmetric cube rule can detect" (ms. 79), "Testing the retracted assertions under their stated axiom" (ms. 100); XIIb-b "Why converse excision is an additional axiom" (ms. 126); XIIc-a "Degree two and the localizer correction" (ms. 187), "Conservative gluing is an additional hypothesis" (ms. 228); XIIapp "Acyclic links and a false converse" (ms. 17); VI-a "Why the new fibration axiom selects full homotopy theory" (ms. 45).
Also `FABLE_PILOT_OVERVIEW_20261110.md` (sections 2.2 and the addendum).

## Papers
Localizers and `Cat` as a model for homotopy types
- D.-C. Cisinski, *Le localisateur fondamental minimal*, Cahiers Topologie Géom. Différentielle Catég. 45 (2004). PDF: https://www.numdam.org/item/CTGDC_2004__45_2_109_0/
- D.-C. Cisinski, *Les préfaisceaux comme modèles des types d'homotopie*, Astérisque 308 (2006). PDF: https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf (chapters 1–4 and 6; Théorème 6.4.22 and Remarque 6.4.23 in particular).
- G. Maltsiniotis, *La théorie de l'homotopie de Grothendieck*, Astérisque 301 (2005). PDF: https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/prstnewprov2020.pdf
- G. Maltsiniotis, *Structures d'asphéricité, foncteurs lisses, et fibrations*, Ann. Math. Blaise Pascal 12 (2005). PDF: https://www.numdam.org/article/AMBP_2005__12_1_1_0.pdf
- R. W. Thomason, *Cat as a closed model category*, Cahiers 21 (1980). PDF: https://www.numdam.org/article/CTGDC_1980__21_3_305_0.pdf
- R. W. Thomason, *Homotopy colimits in the category of small categories*, Math. Proc. Cambridge Philos. Soc. 85 (1979) (PDF if freely readable).
- D.-C. Cisinski, *La classe des morphismes de Dwyer n'est pas stable par rétractes*, Cahiers 40 (1999). PDF: https://www.numdam.org/article/CTGDC_1999__40_3_227_0.pdf
- K. S. Brown, *Abstract homotopy theory and generalized sheaf cohomology*, Trans. AMS 186 (1973). PDF: https://pi.math.cornell.edu/~kbrown/scan/1973.0186.pdf
- M. Batanin, C. Berger, *Homotopy theory for algebras over polynomial monads*, arXiv:1305.0086 (h-cofibrations, §1).
- C. Rezk, *Fibrations and homotopy colimits of simplicial sheaves* (sharp maps). PDF: https://rezk.web.illinois.edu/rezk-sharp-maps.pdf
- P. Hackney, V. Ozornova, E. Riehl, M. Rovelli, *Pushouts of Dwyer maps are (∞,1)-categorical*, arXiv:2205.02353 (m).

Localization of spaces and spectra
- A. K. Bousfield, *The localization of spaces with respect to homology*, Topology 14 (1975); *The localization of spectra with respect to homology*, Topology 18 (1979) (Elsevier open archive PDFs).
- A. K. Bousfield, *Homotopical localizations of spaces*, Amer. J. Math. 119 (1997) (PDF if freely readable).
- M. Hovey, J. Palmieri, *The structure of the Bousfield lattice*, arXiv:math/9801103 (m).
- M. Hovey, J. Palmieri, N. Strickland, *Axiomatic stable homotopy theory*, Mem. AMS 610 (1997) (authors' PDF).
- A. J. Berrick, C. Casacuberta, *A universal space for plus-constructions*, Topology 38 (1999) (open archive PDF).
- J.-C. Hausmann, D. Husemoller, *Acyclic maps*, Enseign. Math. 25 (1979) (e-periodica PDF).
- A. Hatcher, *Algebraic Topology* (Example 2.38: an acyclic 2-complex). https://pi.math.cornell.edu/~hatcher/AT/AT.pdf

Left exact localizations and modalities
- J. Lurie, *Higher Topos Theory*, §§6.1.3, 6.2.1–6.2.2, 6.5.2, 7.2.1. https://www.math.ias.edu/~lurie/papers/HTT.pdf
- E. Rijke, M. Shulman, B. Spitters, *Modalities in homotopy type theory*, arXiv:1706.07526.
- M. Anel, G. Biedermann, E. Finster, A. Joyal, *A generalized Blakers–Massey theorem*, arXiv:1703.09050; *Left exact modalities and higher sheaves*, arXiv:2101.02791 (m).

Derivators
- M. Groth, *Derivators, pointed derivators and stable derivators*, arXiv:1112.3840. Local TeX: `C:\Users\user\Documents\Free or receipted\free\arxiv-tex\1112.3840v2\groth_derivators.tex`.
- M. Groth, K. Ponto, M. Shulman, *Mayer–Vietoris sequences in stable derivators*, arXiv:1306.2072.
- M. Groth, M. Shulman, *Generalized stability for abstract homotopy theories*, arXiv:1704.08084.

## Added 11 Nov 2026 (after the CATHOT answer)

- `CATHOT_return/sections/BC.tex` (CATHOT answer)
- `CATHOT_return/research/BC_report.md` (CATHOT answer)
- `CATHOT_return/research/BC_references.bib` (CATHOT answer)
- G. Baumslag, E. Dyer, A. Heller, *The topology of discrete groups*, JPAA 16 (1980): not in the zip (no free copy fetchable; see the end of MANIFEST.tsv); doi:10.1016/0022-4049(80)90040-7
