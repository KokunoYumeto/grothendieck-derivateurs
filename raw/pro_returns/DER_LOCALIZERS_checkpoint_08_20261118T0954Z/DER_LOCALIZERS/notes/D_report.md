# Part D and Lead 2: outcome

| Item | Outcome | Statements |
|---|---|---|
| D.1, proposed finite-dimensional target-cohomology class | Refuted over every field; it fails two-out-of-three already on a finite one-object category | D.1 |
| Exact repair and choice of derived category | Proved: coherent perfect local systems, with equivalence rather than mere full faithfulness | D.2 |
| Fundamental-localizer axioms for repaired class | Proved, including relative Theorem A for all small categories | D.3 |
| Exact maps inverted by schematization | Known with derivation, all fields, connected pointed components | D.4 |
| Comparison with GALOIS Wlc and W1 | Proved, all strict inclusions and both noninclusions, every field | D.5–D.6 |
| Reverse excision | Refuted, including arbitrary-span square and cube forms, every field | D.7 |
| Localization as an endofunctor of spaces via derived global sections | Refuted in general; correct stack-localization interpretation and restricted positive theorem stated | D.8 |
| Field/basepoint/component hypotheses | Proved necessity of actual missing data; no characteristic-zero/algebraic-closure assumption needed for corrected criterion | D.9 |
| Cote 133/006–008 and PS110 | Checked; neither states D.1 | D.10 |
| Lead 2 | Refuted as stated by D.1; repaired conclusion proved in D.2–D.4 | D.1–D.4 |

## What was read

- The current prompt and its exact Part D formulation, R9, R11 and Lead 2.
- Attached Toën source `literature/arxiv/math_0012219/math_0012219.tex`: 1.5, 2.5, 3.1–3.4, especially Definition 3.1.1; Lemma 3.3.2; Corollary 3.3.3; Theorem 3.3.4; Corollaries 3.3.6–3.3.9. The source's proof and author's PDF were both opened.
- Attached KPT source `literature/arxiv/math_0107129/math_0107129.tex`: introduction and §§1.1, 1.4. Author's PDF independently opened. Exact closest statements: Definition 1.1.6, Theorem 1.1.7, Proposition 1.1.8, Theorem 1.4.1 and Corollary 1.4.2.
- GALOIS sections A, B, B_general, and C; the proof portions actually reused are A.1–A.3, C.2, C.7, C.13, C.14. B.10's cardinal construction was read but was not used: D.5 gives a smaller uniform presentation-complex example.
- Cote 133 scans 006, 007, 008 and `pursuing_stacks/ps6.tex` §110 (pp. 443–444).
- Chachólski–Scherer, *Homotopy theory of diagrams*: Theorem 26.8, Corollary 26.9 and §38. The original Thomason 1979 full paper was not obtained; the independent primary proof is used instead.
- Nica, *Linear groups—Malcev's theorem and Selberg's lemma*, arXiv:1306.2385: unnumbered Malcev theorem p. 1; Lemma 3.2(iii),(iv), proof of Theorem 3.1 on p. 7.
- Baker, *The conjugacy problem for Higman's group*, arXiv:1902.06037: introductory amalgam decomposition and §1 Lemma 4.
- Rivera–Wierstra–Zeinalian, *Rational homotopy equivalences and singular chains*, arXiv:1906.03655v2: Theorem 3.
- Lurie, *Higher Topos Theory*, §§3.3.3–3.3.4 was opened as an alternate route; it is not needed in the final Part D proof.
- Cegarra, *Cohomology of Homotopy Colimits of Simplicial Sets and Small Categories*, publisher metadata/search text were accessible, but the PDF returned HTTP 429; no final argument uses this source. The institutional handle also failed in the browsing tool.

## Searches performed for D.1 and Lead 2

1. “Bertrand Toen Champs affines 3.3.2 3.3.4 schematisation local systems P equivalences”; “Katzarkov Pantev Toen Schematic homotopy types non abelian Hodge theory schematization theorem finite dimensional local systems”. These located author PDFs and publisher texts, while the attached sources gave exact conditions.
2. “schematization functor localization not localization global sections fully faithful rational field”. The decisive correction instead comes directly from the distinction in Toën §§2.5 and 3.3, and the explicit calculation in D.8.
3. “Thomason Homotopy colimits in category of small categories theorem 1.2 pdf”, followed by exact-title searches and Cambridge access-page opening. Original full text not obtained. Opened Chachólski–Scherer at the parent's identified URL and verified covariance from §38.
4. “Higman group acyclic finite dimensional representations no finite quotients aspherical presentation theorem pdf”; “Higman group acyclic four generators four relations proof aspherical”. We used the finite presentation *complex*, so did not need an unverified asphericity assertion.
5. “Nica linear groups Malcev theorem Selberg lemma 2013 pdf theorem 1.1”; “Higman 1951 A finitely generated infinite simple group pdf”. Nica and Baker were opened; the original Higman 1951 paper was not needed or used.
6. “Rivera Wierstra Zeinalian 2021 Theorem 3 pi1 rational equivalences chains coalgebra”. Opened the actual theorem in arXiv:1906.03655v2.

No priority is claimed. The finite-cohomology/schematization criterion is already explicit in Toën Lemma 3.3.2. The elementary finite-group counterexample identifies the condition missing from this prompt's proposed correction.

## Computation

`code/D_verify_examples.py` and its complete `.out` file check:

- All identities and all composable associativity triples in BC2 and BC3 and their one- and two-cone categories.
- The sieve conditions for the two-cone counterexample.
- Normalized nerve boundaries and `d²=0`, and exact rational/modular homology through degree 4 for four coefficient choices. All-degree vanishing is separately proved by averaging and Mayer–Vietoris; the finite calculation is not an unbounded certificate.
- The regular representation invariant subspace dimensions, using exact row reduction.
- All relator exponent sums of the Higman presentation complex, its unimodular cellular boundary determinant, and the affine-transformation identity for the Baumslag–Solitar factors.
- The elementary cellular homology calculation for S².

All checks passed. The finite category reverse counterexample has exactly 3 objects and 6 arrows when char(k)≠2, and 3 objects and 7 arrows in characteristic 2.

## Corrections and rechecks

- **Part D.1 / Lead 2:** false even after adding all cohomological degrees unless essential surjectivity of finite-dimensional local systems is also required. It is not enough to appeal to a comma spectral sequence, because two-out-of-three already fails.
- **R11:** confirmed. The ordinary category of local systems, and even its ordinary bounded derived category, do not detect S². The correct category is coherent perfect local systems inside all derived local systems, componentwise the thick subcategory generated by ordinary finite-dimensional local systems.
- **R9 / GALOIS C.7:** rechecked the used fibre-counit and loop-algebra tests, including the fact that the specified map of group algebras forces an actual group isomorphism. No claim that W1 is a localizer is made.
- **R9 / GALOIS C.13:** confirmed using the opened Rivera–Wierstra–Zeinalian Theorem 3; discrete π1 is retained in the fibrewise rational theory.
- **R9 / GALOIS C.14:** confirmed: Wlc is strictly contained in schematization equivalences. D.5 strengthens the example to a single finite presentation complex valid over every field. The earlier cardinal group construction is not needed for this use.
- **Toën source:** the sentence immediately after Definition 3.1.1 says O-equivalence implies P-equivalence. Its direction is reversed, as already noted by GALOIS C.14. The correct direction is P⇒O, consistent with Lemma 3.2.1 and Corollary 3.3.8 and refuted in the written opposite direction by BCℓ→*.
- **Cote 133/006–008:** the prompt's amended caution is correct: these pages discuss Witt groups, hyperbolic forms and λ-formulas; they do not formulate a localizer of finite-dimensional local systems.
- **PS110:** discrete retention of π1 in one proposed schematization construction is not a statement that Toën's full schematization retains it. D.4–D.6 keep these two tests separate.

## Scope

Part D and Lead 2 are settled in the refutation-and-exact-repair sense. We do not claim that schematization is a reflective endofunctor of spaces or that every schematic homotopy type arises by localization of a space. D.8 refutes the unrestricted global-sections formulation. We do not assert Toën's field theorem for arbitrary nonfield coefficient rings.
