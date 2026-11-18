# Part A sources and searches

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim. Searches and openings below occurred on 2026-11-17. A search hit is distinguished from an opened primary body. The prose in the paper identifies which facts are established inputs and which are proved in this return.

## Attached sources opened and mathematical steps audited

- `TOTASPH/TOTASPH_C.tex`: action inheritance, cyclic-cover argument, unrestricted action characterization, exactness sufficiency, directedness/affine-equalizer lemma, and the finite/weak-terminal restriction. The inherited action is the explicit dependent sum; this is retained in A.1. The cyclic-cover argument is used in A.12 and A.14.
- `TOTASPH/TOTASPH_D.tex`: truncated criterion D.12 followed in full, including the comma spectral sequence and finality surjection on pi_1. A.1 gives the own-word audit of both directions at the point of use. The low-degree base criterion is used only to identify T_1.
- `TOTASPH/TOTASPH_F.tex` and the corresponding PRETOT composition discussion: the cosieve criterion for composition. A.2 supplies the actual lower-copy category and verifies the boundary for the failing composite, as well as the other implication using the relevant Grothendieck construction.
- `PRETOT_return` C.1–C.4: restricted-action and cosieve formulations checked with their stated variance. No restricted-action statement is substituted for an arbitrary-action statement.
- `TOTEX_return/TOTEX_paper.tex`, A.1, A.4, B.5, B.6: the H_1/quasi-filtered equivalence used in A.2 and A.15. In B.5 the affine equalizer is partitioned by target labels before terms are moved to a common successor; loops reduce by condition I and fill by the augmentation-one nerve-chain combination. B.6 then applies this to cyclic covers. A.2 includes an own-word audit. This use does not assume exactness on arbitrary abelian coefficient diagrams.
- `TOTAL_EXACT_2/return/sections/predimension_totality_reduction.tex`: read in full when designing A.7. The explicit quotient to injective transitions, the two homotopy-final comma comparisons, the directed-union action on the rich limit, and the orbit fixed-point formula were each checked. Their required nonempty-cosieve contractions and exact open-subgroup description are proved independently for the cocycle and Kan classes.
- `TOTAL_EXACT_2/return/sections/finite_tests.tex`: finite-sphere tests followed through `FT:finite-test`; used to evaluate an initial attachment route, not needed by the final tower construction. `FT:ty` is not a Part A input.
- `TOTAL_EXACT_2/return/sections/akr_links.tex`: attachment cycle test `C:attachment-cycle-test`, including its pushout/kernel calculation, and the binary relation-resolution formula. Used in the R14 audit and to assess attachment routes; not used to infer an unproved persistence principle.
- `TOTAL_EXACT_2/return/sections/akr_attachment_fixed_paths.tex`: exact fixed-path kernel C.10 read in full. The fixed-component condition makes precisely the displayed generators of the old-cycle kernel vanish.
- `TOTAL_EXACT_2/return/sections/akr_birth_cover_descent.tex`: C.19–C.24 read in full, including forbidden-pair routing, Helly, intersections, and the pointwise-equalizer image assertion. The latter is an actual arrow image and not merely a union of component images.
- `TOTAL_EXACT_2/return/sections/akr_universal_components.tex`: C.25–C.28 read in full. The induction compares actual factorizations, component paths, and point paths; A.15 records the step and its role in survival.
- `reviews/REVIEW_MAIN_PROOFS_TOTEX2.md`, Section 4: expanded C.27 component-routing proof read in full. Component information locates overlaps; the older hypothesis then factors actual arrows. This distinction is essential and is explicitly preserved in the audit.
- `TOTAL_EXACT_2/return/sections/akr_component_necklace.tex`: exact injectivity threshold and proof read. Its C.1 specialization agrees with the path bound used in the universal induction.
- `TOTAL_EXACT_2/return/sections/akr_beta_fixed_subsets.tex`: actual-path beta formulas and fixed-subset discussion read. The invalid arbitrary restriction of a global beta formula is not used.
- `TOTAL_EXACT_2/return/sections/akr_ordered_necklace.tex`: strict necklace set-colimit C.32 and orderability C.33–C.34 read in full, including the increasing homeomorphism construction and termination of the finite search.
- `TOTAL_EXACT_2/return/sections/akr_large_targets.tex`: C.36–C.37 read in full, including the deterministic algorithm and its final cycle calculation. The selected instance is the named K* in A.15.
- `TOTAL_EXACT_2/return/sections/construction_scope.tex`: universal-versus-selected-target scope verified. The final audit uses universal R14 survival; the selected construction makes one particular category completely specified.
- `LEADS_DERIVATIONS.md`, Lead 1(a)–(d): read in full. None of these leads was treated as an axiom; A.1–A.2 prove them.
- `DER_XIIb-a.tex`, manuscript pp. 109–114, especially 113–114: definitions and composition doubt reread. The final correction distinguishes totally dwyerienne sieve composition at finite n from the already positive composition result for strictly/totally aspherical functors. No editorial correction is used without attribution; the displayed pushout editorial corrections at pp. 112–113 are not needed in the proof.

## Primary literature opened

### Cisinski, *Les préfaisceaux comme modèles des types d'homotopie* (Astérisque 308, 2006)

URL: https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf

Opened Definition 3.3.2, Sorites 3.3.8, and Proposition 3.3.16. In particular (7) gives opposite invariance and 3.3.16 gives the fibrewise equivalence statement. Section 3.3 explicitly says that it records results without proofs and refers to Maltsiniotis [96]; the bibliography note says so. A.10 supplies a direct proof of the Grothendieck-construction form used, via its adjoint comma retractions and relative Theorem A. It assumes no accessibility. Relevant retrieval refs for root: `turn37view1`, `turn37view2`, `turn70view2`, `turn73view0`, `turn73view1`.

### Goerss–Jardine, *Simplicial Homotopy Theory* (1999; opened reprint PDF)

URL: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf

Opened Theorem III.2.1, Proposition III.2.2, Corollary III.2.3 (Dold–Kan), and the discussion and Corollary III.2.7 identifying homotopy groups with normalized homology. A.4 computes its normalized complex explicitly and notes the reversed ordinal convention. Also opened Proposition I.5.2 and Corollary I.5.3(2), with the pushout-product proof of the mapping-space fibration; this is the precise strict-extension input in A.13. Relevant refs: `turn54view0`, `turn54view1`, `turn57view0`, `turn57view1`, `turn68view0`.

### Campion–Ye, *Homotopy Types of Abstract Elementary Classes*

URL: https://arxiv.org/pdf/1909.07965 (v2, 18 May 2020)

Opened introductory material, Fact 1.2, the definitions and proof of Theorem 3.6, Corollary 3.7, Remark 3.8, and Examples 4.1–4.3. The small-category Yoneda inclusion is a weak equivalence because its comma over an admissible presheaf has contractible elements; the construction supplies amalgamation. This is a nearby realization result, not a proof of the required all-action property. A.13 gives that additional property independently for Delta_inj/K. No priority inference is made. Journal metadata: JPAA 225 (2021), no. 5, article 106461; DOI 10.1016/j.jpaa.2020.106461. The bibliography uses the opened arXiv v2. Relevant refs: `turn10view1`, `turn12view0`, `turn12view1`, `turn70view0`, `turn71view1`. Experimental HTML opening failed; the PDF was available.

### Campion–Ye, *Non-trivial higher homotopy of first-order theories*

URL: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/nontrivial-higher-homotopy-of-firstorder-theories/30EF8141591F08DF334EE40E5F51BD38

Opened the primary full text: introduction, finite cyclic and paracyclic definitions, Lemmas 1.9 and 1.11 with proofs, Corollaries 1.12–1.14, the functorial densification construction in Section 2, and Corollaries 2.7–2.8. The paper computes K(Z,2) for cyclic-order categories and dense cyclic-order models. This supplies historical context only. The site's mathematical reference cross-links are shifted in some rendered labels; theorem numbers and actual bibliography entries were read rather than inferred from those links. Publication: online 11 January 2024; JSL 91 (2026), no. 1, pp. 230–236; DOI 10.1017/jsl.2024.3. Relevant refs: `turn66view0`, `turn67view1`–`turn67view3`, `turn68view1`, `turn70view3`, `turn70view4`, `turn71view0`, `turn72view0`.

### Evans–Hubička–Konečný–Nešetřil, *EPPA for two-graphs and antipodal metric spaces*

URL: https://arxiv.org/pdf/1812.11157 (v2, 11 September 2019)

Opened the introduction and the two-graph/switching definitions, plus Section 7 and the proofs of Proposition 7.1 and Corollary 7.2. The ordered r=2, F_2 cocycle structures are exactly their ordered two-graphs. Corollary 7.2 says the ordered class is not Ramsey; this agrees with the present higher-homotopy behavior. No EPPA or imaginary-elimination result is assumed here. Proc. AMS 148 (2020), 1901–1915, DOI 10.1090/proc/14872. Relevant refs: `turn65view0`, `turn66view2`, `turn70view1`.

### Additional records and searches, not used as proof

- Faber, *Homogeneous models and their toposes of supported sets*: primary Cambridge repository record opened, https://www.repository.cam.ac.uk/items/fcee8a47-42ab-46c8-b1af-cdde66bbf9c3. The repository says the thesis file is embargoed; only abstract and metadata were read. Author page also found. No theorem from the thesis is used.
- Brenner–Hubička–Konečný, *EPPA for Reducts of the Random Graph*, arXiv:2610.39760: recent search hit only, not opened; its claimed later EPPA resolution is not used.
- Curtis, *Simplicial Homotopy Theory*: a primary PDF search hit was found, but the proof body was not opened. Goerss–Jardine supplied the precise needed result instead.
- Kerodon normalized-Moore search hits, Konečný's thesis, and a homogeneous-structures survey: search leads only, not proof inputs.
- The original AKR article's metadata is available in the supplied bibliographies. This branch relies on the repaired construction and audited supplied proof, not on an assertion that it independently reopened the original 1981 scan. Its corrected formulas are explicitly identified in A.15.

## Search query log

The following queries were issued with the web-search service. Initial routine queries used the second engine; primary-source verification and coverage gaps used the first engine. No negative search is offered as evidence of novelty.

1. `"category" "quasi-filtered" homology higher connected category of elements`
2. `"classifying spaces" "first-order theories" homotopy types embeddings`
3. `"atomic" "topos" "higher homotopy" category of models`
4. `"Homotopy Types of Abstract Elementary Classes" Campion Cousins Ye`
5. `Cisinski localisateur fondamental construction Grothendieck equivalences foncteurs asphériques sommes`
6. `"homotopy" "atomic topos" shape`
7. `"higher" "homotopy" "Fraïssé" category`
8. `"classifying space" "contractible" "category of simplices" injections Kan`
9. `"quasi-filtered" "higher" homology`
10. `"higher homotopy" "atomic" topos`
11. `"quasi-filtered" categories homology Isbell Mitchell`
12. `"semisimplicial" "Kan" "filtered" category simplices`
13. `"finite" "cocycles" "Fraisse" "classifying"`
14. `"n-cocycles" "Fraïssé"`
15. `"two-graphs" "weak elimination of imaginaries"`
16. `"simplicial abelian group" "normalized" "homotopy" Kerodon`
17. `"random two-graph" "imaginaries"`
18. `"generic" "cocycles" "homogeneous" model theory`
19. `"ordered" "two-graphs" "Ramsey"`
20. `"Eilenberg-Mac Lane" "Fraïssé"`
21. `"Kan complex" "quasi-filtered"`
22. `"category of simplices" "actions" "Kan" category`
23. `"two-graphs" "EPPA" arxiv`
24. `"Fraïssé" "simplicial" "homotopy"`
25. `"Homogeneous models and their toposes of supported sets"`
26. `"quasi-filtered" "Kan"`
27. `"EPPA for two-graphs and antipodal metric spaces"`

Within opened sources, `find` queries included “Moore complex”, “Dold-Kan”, “function complex”, “Proposition 3.3.16”, “Sorites 3.3.8”, “Corollary 7.2”, “Corollary 1.14”, “Corollary 2.7”, “Theorem 2.8” (the source has Corollary 2.8), “Published online”, and “Volume 91”. Direct openings of the primary URLs above supplied the corresponding bodies.

## Independent mathematical audits in this run

Root read the full cocycle argument A.3–A.9 and the Lead 6 proof, checking the explicit primitive, the three-piece circle nerve, finite order interpolation, action reduction, and specified fold map. Root subsequently read A.13–A.14 in full and checked the horn-filler naturality, strict Kan extension, semilinear subgroup dichotomy, and directed-component argument. The separate note `D_exact_audit.md` records this branch's independent audit of the sibling's exact-index free-monoid theorem.

The final source fragments have no unproved Part A assertion. The universal claims are established by proofs; bounded programs check formulas and signs only.
