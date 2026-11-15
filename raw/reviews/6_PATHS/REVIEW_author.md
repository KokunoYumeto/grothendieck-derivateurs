# PATHS: review by the author of the prompt

Claude (Fable 5.2, Anthropic), 11 November 2026 (written about 10:30–10:40 UTC). Review of the answer of GPT-6 Astra (ChatGPT Pro mode) to prompt `6_PATHS` (76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open), read against the three leads of the prompt, the numbered targets carried from CATHOT, TOTASPH, POLES, GALOIS and STRATA, and the companion's audit of Chapters V, VII, IX, XIII, XVII and XIX.

## What I read and checked

Read: `PATHS_report.md` and `PATHS_results.csv` in full; `sections/00_conventions.tex`, `A_definitions.tex`, `A_colimits.tex`, `B.tex`, `C_paths.tex`, `C.tex`, `D.tex`, `D_kt.tex`, `E.tex`, `F_audit.tex` in full, proofs included. Nothing in `code/` was opened or run; `audit/` and `research/` were not read (the report reproduces the research records).

Opened (sources on which statements rest):
- Cisinski, *Les préfaisceaux comme modèles des types d'homotopie*: 5.3.1 (definition of `W`-proper and `W`-smooth by `W`-coasphericity of `A_b → A/b`, respectively `W`-asphericity of `A_b → b\A`), Exemple 5.3.2 (every prefibration is smooth and every precofibration proper, for every `W`), Proposition 5.3.4 (the lifting-category criterion (d)), Corollaires 5.3.6, 5.3.7, Corollaire 4.2.19 (the minimal fundamental localizer is `W∞`).
- Maltsiniotis, *Structures d'asphéricité, foncteurs lisses, et fibrations*, Définition 1.1, Théorème 1.2 (`u` is `W`-smooth iff every `A_b → b\A` is `W`-aspherical iff base change along `u` preserves `W`-aspherical functors), and the remark that the notions depend only on the class of `W`-aspherical categories.
- Cisinski, *Higher categories and homotopical algebra* (the copy in the prompt's zip): Definition 7.4.12, Theorem 7.6.17 (for an ∞-category with weak equivalences and fibrations and a finite direct `I`, the localization of the diagrams is the diagrams in the localization), Theorem 7.9.8 (statement only).
- Kaledin, arXiv:2409.17489v3: Definition 2.1.5.3 (`Pos` is partially ordered sets of finite chain dimension), 2.1.5.4 (left-finite, left-bounded; `Pos^+`), Definition 7.1.4.6 (additivity: an equivalence onto the product, for every map to a discrete set), Definitions 7.2.1.3, 7.2.1.4, Example 7.2.1.16 (`K(E)` is an enhanced category for every category `E`). Theorem 7.3.1.3 located, not followed.
- Dwyer–Kan, *Calculating simplicial localizations*: Propositions 3.1, 5.5, 6.2 (statements).
- Meier, *Fibration categories are fibrant relative categories* (arXiv source): the definition of `N_ξ`, the description of `ξ[n]` by chains of subsets, the theorem that every fibration category is Barwick–Kan fibrant (statement; published numbering not checked).
- Arakawa–Cnossen, arXiv:2608.19870 (source in the zip): the Reedy structure on the category of zigzag types and the sentence identifying the hammock mapping space with the nerve of a Grothendieck construction (located; the proofs were not followed).
- Rădulescu-Banu, arXiv:math/0610009: the axioms CF1–CF6 and the definition of a precofibration category (CF1–CF4).
- The transcription: VII ms. 65–67 (the fibred category `Ch_Σ(X)` over the types, a full subcategory; the correction "dans `Σ`"); IX ms. 22–23 (tests (a), (b), (c)); XIII ms. 7–10 (M 0 to M 4, M′, M″, Proposition 3, Corollaire 1, Proposition 4); XVII ms. 39 (Cof 0–3); XIX ms. 33 (Cof 0–4), Question 3.14. The companion's rows VIIc-A046, C004, C005, C042, C045; IX-037, 080, 081, 088; XIIc-a C030–C039; XIX-C099; XIIIa-A046.

Not opened: Kerodon at the tags cited (4.6.7, 4.8.4.1, 4.5.4.8, 7.2.3.1, 7.2.3.3, 6.3.6.1); Chachólski–Scherer 26.8–26.9; Lenz 2018; Szumiło; Quillen 1967; Dwyer–Kan, *Function complexes*; Keller 2006; Dugger–Shipley 2007; Groth 2013 at the numbers cited; Arlin 2020; Fuentes-Keuthan–Kędziorek–Rovelli; Higman–Neumann–Neumann; Baumslag–Dyer–Heller; Hausmann–Husemoller; Cegarra 2020; Shoikhet 2016; Fiedorowicz 2002 (opened in the STRATA review).

Own checks: `checks_author/check_paths.py`, output `check_paths.out`, written from the statements with my own code (finite categories with explicit composition, normalized nerve, exact rational ranks).
1. A.9, D.10: the face poset `P` of the boundary of a triangle has 234 monotone self-maps, of degrees −1, 0, 1 in numbers 3, 228, 3; there are 456 monotone maps `P → sd P`, all of degree 0; the last-element map `sd P → P` has degree 1.
2. D.9: for the diamond with `W` = identities and the two maps out of `0`: two-out-of-three holds, the intrinsic cofibrations are the identities and the three maps into `1`, every map factors as required, and the cofibrant objects are `0` and `1` only.
3. D.12: among the monotone maps of the five-vertex fence to the nine-vertex fence there are ones with ends (0, 4) and (4, 8) and none with ends (0, 8).
4. D.2, D.3: the category `E`: 34 associativity triples; `|Hom(x, 0)| = 1`, `|Hom(x, x)| = 2`, so no object has the four maps from `x` that `x × x` needs.
5. D.5: `BY` and `BB` are circles, `BX` has the homology of `S²`, the cycle `γ` goes to `f − g`; `X^Y` has 198 objects and `X^B` 18.
6. D.19: 4 endofunctions of the regular `C_2`-set, 2 equivariant. D.23: in `S_3` the images of `α(x)`, `α(y)` are both `(12)`; the subgroups have 2 and 6 elements.
7. E.6: the five-element monoid is associative, no product with `e_{00}` is the unit; rational Betti numbers 1, 0, 1, 0, 0 through degree 4.
8. E.7 for `n = 1`, E.12: the category `C` (34 triples; Betti 1, 0, 1); the fork is final in `C` (comma categories with 4, 3, 1, 1 objects, each connected); the pushout `Q` built from the coend formula has 6 objects and 20 arrows, 104 associativity triples, crossing sets of 1, 1, 1, 1, 0 elements, and Betti numbers 1, 0, 0, 1, while `D`, `P_1`, `A_1` are acyclic.
All counts agree with those the answer reports.

Verdict words: **proved** (I followed the argument step by step and found it complete, given the named inputs); **proved in outline** (I followed the argument and found no gap, but it uses ∞-categorical or cited machinery that I did not unfold); **known** (a citation; opened unless said otherwise); **unverified**; **false**.

## Summary

No statement labelled Proved, Known or Refuted was found false, and I found no gap in a proof I followed. The central question of the prompt is not answered: whether Grothendieck's path categories with arbitrary vertical arrows have the type of the mapping spaces of the localization (B.8) is left open, with a retraction (B.6), two extreme cases (B.4) and no counterexample in 132 small cases (B.9, not reproduced by me).

What the answer adds that was not known to us:
- **CATHOT E.26 and E.27 are theorems** (C.P1–C.P4), for every admissible `Σ`: the sequential models, the total category over all types and the one-sided and two-sided paddings are compared by weak equivalences of specified functors, and the composition is associative and unital in `Hot`. The proof replaces the ind-object argument (which CATHOT E.4 shows cannot work) by an action of the categories of maps of types, which are empty or contractible. Row IX-037 is settled for the raw construction.
- **The comparison is not invertible modulo natural transformations** (C.P5; four objects): rows VIIc-A046 and V-I066 are answered no in `Cat hot` and yes in `Hot`.
- **My Lead 3 was wrong in its last clause** (D.2, D.3): the finite category of IX ms. 23 is rectifiable at every shape; what it lacks is the product `x × x`.
- **`Cof_W` with a factorization is already a finite cofibration structure** (D.8), with limits of this (D.9), separating examples for the proposed finite tests (D.10–D.13) and the exact shapes of Kaledin's axioms (D.14–D.16).
- **The asymmetry between cofibrations and fibrations for localizers of `Cat`** is proved without accessibility in one direction (inside D.18) and for every non-zero spectrum (D.23).
- The example found in the TOTASPH review (colimits in `Cat` over the injective ordinals) is confirmed by a shorter argument (A.5).

Points where the answer needs a remark, none an error in a statement:
1. D.8's one non-formal step is Grothendieck's own: XIII ms. 10, Corollaire 1 (`Cof_W ∩ W = W^{univ}` when both factorizations exist, with a footnote that only `TC, TF ⊂ W` is used). The answer proves it from one factorization and cites POLES A.9, not XIII; the companion has it as row XIIIa-A046 (proved). D.17 (3), on Question 3.14 of XIX, agrees with what the companion already says at row XIX-C099.
2. E.3's first half (no outgoing lift from the empty path) is the companion's own correction at row VIIc-C042; the second half (not a Grothendieck fibration either) is new.
3. "Known" for D.15 means: a formal consequence of a theorem of a preprint whose Chapters 6–7 its author marks preliminary. I opened the definitions and the example, not the theorem.
4. B.2 is labelled Known; the composition-compatible map `ρ` from the fibred category to the hammock complex is written out there and rests on Arakawa–Cnossen (2026 preprint) for the Reedy step. I followed the definition of `ρ` and did not check the cited numbers beyond locating them.

## The checks the handoff asked for

**The answer on `Ch(X) → X × X` against STRATA D.6, E.1, E.10–E.11.** Consistent.
- STRATA E.1 (a bifibration is proper and smooth, with adjoint transitions) and PATHS E.3 (`Ch(X) → X × X` is smooth and not proper for `X = [1]`): hence not a bifibration, which E.3 also proves directly on both sides. I followed both halves with the conventions of VII ms. 65–67 (a morphism of paths lies over a map of types `τ → τ'` and is a morphism `c → f^*c'`): a map out of the empty type is to the empty type, so the empty path at `0` has no outgoing lift over `(1_0, w)`; and for a candidate terminal incoming lift `c` of type `τ` the path "constant at `0` on a first copy of `τ`, then `c`" has two different morphisms to `c`, over the two collapses `ττ → τ`.
- STRATA D.6 (proper and smooth does not imply bifibration: a four-element poset over `[1]`) and PATHS E.4 (`𝒫(X) → X × X` is proper and smooth and, for `X = [1]`, neither a fibration nor an opfibration): a second separating example, by the mechanism of STRATA E.4 (filtered unions keep contractibility of lifting categories and lose universal arrows). Followed for `[1]`.
- STRATA E.10 (over a poset every locally constant object is represented by a strict bifibration): no conflict; E.10 is an existence statement, and over the contractible base `[1] × [1]` the path local system is represented by a product projection, not by either path functor.
- STRATA E.11 (open over the five-element monoid): PATHS E.6 shows that the two path functors are not the missing bifibration (followed: the delayed-step lifts and the fact that no product with `e_{00}` is the unit, checked), and E.11 keeps the question open. My remark in the STRATA section of the handoff (with idempotents in the base a strict diagram with fibration transitions cannot work) agrees with the "remaining step" named in PATHS E.11.
- PATHS E.5 (functorial factorization through `A ×_X 𝒫(X)`) agrees with STRATA E.2 (the same factorization taken from Cisinski 2006, 5.3.14). The step "every base change of `σ` is a weak equivalence" also follows at once from Cisinski 5.3.7 (a proper functor with aspherical fibres is universally a weak equivalence).

**Part D against STRATA C.7 and B.8.** Consistent.
- STRATA B.8 (every small category is the localization of a relative poset) and PATHS D.13 (such a presentation does not make the strict diagram categories right: `P` presents the category of `Z`, an explicit countable poset `Q` presents that of `C_2`, and strict diagrams of those shapes in a poset are constant): B.8 concerns the localization only; D.13 is the limit of its use. Followed.
- STRATA C.7 (homotopy categories of diagrams do not glue; `Z` classes against one for `X = [1]`) and PATHS D.20 (the same numbers for maps from `S⁰ → *` to `* → S¹` in `Ho Fun([1], 𝒮)` against `Fun([1], Ho 𝒮)`): the same computation, recomputed (the fibre of the diagonal `S¹ → S¹ × S¹`).
- PATHS E.10 (a relative category can keep a non-invertible endomorphism after localization; the monoid `{1, e}` with identities marked) agrees with STRATA B.7.

**The inference in `7_BISITE`, Part B** (checked first, at the coordinator's request). Right. Cisinski 2006, 5.3.1 defines `W`-proper (respectively `W`-smooth) by: every `A_b → A/b` is `W`-coaspherical (every `A_b → b\A` is `W`-aspherical); a `W∞`-aspherical functor is `W`-aspherical for every fundamental localizer `W`, because `W∞ ⊂ W` (Corollaire 4.2.19: `W∞` is the minimal fundamental localizer). So `W∞`-proper implies `W`-proper and `W∞`-smooth implies `W`-smooth, for every `W`; Maltsiniotis 2005, Théorème 1.2 gives the same with the base-change formulation, and Exemple 5.3.2 gives it for prefibrations and precofibrations with no reference to `W∞`. Consequently, with `Liss` and `Prop` the `W`-smooth and `W`-proper functors:
- for `W` = rational homology equivalences, the path functor `q` of PATHS E.9 is in `Liss ∩ Prop` and not in `Fib_W`;
- for `W_0`, the two-object contractible groupoid over `C_2` (STRATA G.3), a bifibration, is in `Liss ∩ Prop` and not in `Fib_{W_0}`;
- for `W_E`, `E` a non-zero spectrum, the three-sheeted covering of POLES C.10, a discrete bifibration, is in `Liss ∩ Prop` and not in `Fib_{W_E}`;
- for `W_n`, `n ≥ 1` (my addition, checked by no one else): take a finite category `X` of the type of `S^{n+1}` and `q: 𝒫(X; x, −) → X`; `e → X` is in `W_n`, and its pullback along `q` is the inclusion of the fibre, of type `ΩS^{n+1}`, in a contractible category, which is not in `W_n` since `π_n ΩS^{n+1} = Z`.
So the inclusion `Liss ∩ Prop ⊂ Fib_W` that Grothendieck proposes "perhaps" at XII ms. 225–226 (row XIIc-a C033) holds for `W∞` (Cisinski 2006, 6.4.8, 6.4.16; STRATA E.2) and fails for `W_0`, every `W_n`, rational homology and every homology localizer, when the three classes are taken for the same `W`. The item in `7_BISITE` states the inference as unverified and asks the model to decide; it is correct as written and needs no change.

## Verdicts, statement by statement

### Part A (definitions; total categories and colimits)

| Id | Label | Verdict |
|---|---|---|
| A.P1 | Proved | **Proved.** The universal property of the ordinary localization, with no vertical arrow inverted. |
| A.P2 | Proved | **Proved**, given A.2 and C.P3. |
| A.1 | Proved | **Proved** (definitions; the span of VII ms. 108). |
| A.2 | Proved | **Proved.** The comma categories of the comparison are filtered; Theorem A. |
| A.3 | Proved | **Proved.** Both directions followed; necessity uses the representable presheaves. |
| A.4 | Refuted | **Proved** (the constant diagram over the category of `C_2`). The manuscript sees this at VII ms. 109. |
| A.5 | Refuted | **Proved.** Followed in full: the colimit in `Cat` is the free monoid on one generator; `H_k` of the stages is the representable module at `[k − 1]`, so the homotopy colimit has `H_k = Z` for all `k`. This is the example of my TOTASPH review, with a shorter proof (projectivity of representables in place of exactness of all colimits). |
| A.6 | Proved | **Proved, with one part not redone:** the polynomial construction of the equalizing combination was followed in the TOTASPH review (C.7–C.9) and read here without recomputation; the passage from exact colimits to total asphericity was followed. |
| A.7 | Proved | **Proved.** |
| A.8 | Open | Open. The residual case (infinitely many objects, no weakly terminal object) is correctly delimited by TOTASPH C.13. |
| A.9 | Proved | **Proved**; counts reproduced (check 1). |

### Part B (the comparison with the hammock localization)

| Id | Label | Verdict |
|---|---|---|
| B.1 | Proved | **Proved.** The definitions agree with VII ms. 65–67. |
| B.2 | Known | **Known, proved in outline.** Dwyer–Kan 5.5 opened; the map `ρ` followed; the Reedy step and the numbers in Arakawa–Cnossen not verified. |
| B.3 | Refuted | **Proved.** |
| B.4 | Proved | **Proved.** Followed in full: the zigzag `1 ⇐ pad ⇐ T ⇒ ie`, including naturality of the prefix effects across backward squares (it uses that the backward arrows are isomorphisms). The correction to the parenthesis of my Lead 2 is right. |
| B.5 | Known | **Known** (Dwyer–Kan 6.2 opened at the statement). The remark on two-out-of-three is immediate. |
| B.6 | Proved | **Proved in outline.** The localization of the interval at its backward edges and the naturality in the type are clear; the assembly into a coherent cocone and its compatibility with concatenation were read, not unfolded. |
| B.7 | Proved | **Proved** (the three squares checked). |
| B.8 | Open | Open. See "What is left". |
| B.9 | Proved | **Unverified** (a computation; I did not write a second program for it). It supports nothing else. |

### Part C (types, sequential comparisons, composition, pointed and linear versions)

| Id | Label | Verdict |
|---|---|---|
| C.P1 | Proved | **Proved.** The run-clamping contraction followed, with the induction on the runs of the target. |
| C.P2 | Proved | **Proved in outline.** The strict action `P(τ, σ) × F_σ → F_τ` and the two comma-category computations (the contraction `σ * τ` of the types that map to `σ`; an upward closed subset of `N`) were followed. The passage through the homotopy-coherent nerve uses the cited standard facts, not opened. |
| C.P3 | Proved | **Proved in outline**, given C.P2. This settles CATHOT E.26 (1)–(3). |
| C.P4 | Proved | **Proved in outline**, given C.P3. This settles CATHOT E.27 and row IX-037. |
| C.P5 | Refuted | **Proved.** Followed in full: lifts to the integer fence move a vertex by at most one per natural transformation, and the out-and-back paths have unbounded excursions. |
| C.1 | Proved | **Proved.** |
| C.2 | Known | **Known** (Dwyer–Kan 2.1, 3.1 opened; 3.3 not). |
| C.3 | Proved | **Proved.** |
| C.4 | Proved | **Proved**; the identification with derived mapping spaces is by citation, not opened. |
| C.5 | Known | **Unverified citation** (Quillen; not opened). The qualification on base points is right. |
| C.6 | Proved | **Proved** for pointed ∞-categories; the derivator half is by citation (Groth 2013), not opened. |
| C.7 | Refuted | **Proved** (the three mapping spaces recomputed). |
| C.8 | Proved | **Proved** (lax monoidality of the truncation; the citations of Keller and of the Stacks project not opened). |
| C.9 | Open | Open. |
| C.10 | Open | Open. |

### Part D (tests, rectification, enhancement, Kan–Thurston)

| Id | Label | Verdict |
|---|---|---|
| D.1 | Proved | **Proved**; the reading of IX ms. 22–23 checked against the text. |
| D.2 | Refuted | **Proved.** `Fun(NA, NE) = N Fun(A, E)` and `W` = identities. The clause of my Lead 3 is false. |
| D.3 | Proved | **Proved**; check 4. |
| D.4 | Proved | **Proved.** |
| D.5 | Refuted | **Proved.** Followed: `X^B = X^{[1]}` has trivial fundamental group, and the loop (D.5.1) has degree one on the torus `BY × S¹`; check 5. |
| D.6 | Proved | **Proved.** |
| D.7 | Known | **Known**: Cisinski 2019, 7.4.12 and 7.6.17 opened and as cited; Lenz, Cisinski 7.9.8 (hypotheses), Cisinski 2003, 2010 not followed. |
| D.8 | Proved | **Proved.** Followed in full. With Cisinski's Definition 7.4.12 (dual) the needed input is even less than CF1–CF4. See remark 1 of the summary: the key step is XIII ms. 10, Corollaire 1. |
| D.9 | Refuted | **Proved**; check 2. |
| D.10 | Refuted | **Proved**; check 1. |
| D.11 | Proved | **Proved**; that the opposite is Barwick–Kan fibrant is by Meier's theorem (statement opened). |
| D.12 | Refuted | **Proved, with the part named unverified:** that level 0 of `N_ξ` is `Ex² N` when all arrows are weak was checked against Meier's definition of `ξ` only at the level of the description of `ξ[n]`; check 3. |
| D.13 | Refuted | **Proved** (both examples followed; Kerodon 6.3.6.1 not opened and not needed for the examples). |
| D.14 | Known | **Known**: the shape classes and Definitions opened and as cited; Proposition 7.2.3.7 and Lemma 7.2.4.1 not opened. |
| D.15 | Known | **Unverified** beyond its logic: the argument is formal given Kaledin's Theorem 7.3.1.3 and Lemma 7.3.1.1, which I did not follow (preprint). |
| D.16 | Proved | **Proved** (bounded zigzags; additivity asks an equivalence, Definition 7.1.4.6 opened). |
| D.17 | Proved | **Proved**; (1), (2) checked against XVII ms. 39, XIX ms. 33, XIII ms. 7–10; (3), (4) read once. |
| D.18 | Known | **Known, and the converse argument proved:** enough intrinsic fibrations give `W = W^{asph}` by Brown's factorization (followed; no accessibility). |
| D.19 | Refuted | **Proved** (GALOIS A.5); check 6. |
| D.20 | Known | **Proved** for the example; the two references not opened. |
| D.21 | Proved | **Unverified** (depends on D.15). |
| D.22 | Open | Open (six items). |
| D.23 | Proved | **Proved.** Followed in full: an `E`-aspherical space has no non-zero homomorphism from `π_1` to `Z`; `V_{BF}` contains the aspherical generators and not `Bα`; check 6. |
| D.K1 | Proved | **Proved** (as GALOIS B.9, followed in the GALOIS review). |
| D.K2 | Proved | **Proved, citations unverified** (HNN and mitosis; as in the GALOIS review). |
| D.K3 | Proved | **Proved** (as GALOIS B.11; the subcomplex-injectivity step is written out here and I followed it). |
| D.K4 | Proved | **Proved** (as GALOIS B.12). |
| D.K5 | Proved | **Proved.** The universe remark is the one made after the second review of CATHOT. |

### Part E (what the path construction supplies)

| Id | Label | Verdict |
|---|---|---|
| E.1 | Known | **Known**: CATHOT E.20–E.25, followed in the two CATHOT reviews; not redone. |
| E.2 | Proved | **Proved**, given E.1 and B.2. |
| E.3 | Refuted | **Proved** (both halves followed; smoothness is the companion's proof at VII ms. 164). |
| E.4 | Refuted | **Proved** for `[1]`; smoothness and properness are E.1. |
| E.5 | Proved | **Proved**, given E.1. |
| E.6 | Refuted | **Proved**; check 7. |
| E.7 | Refuted | **Proved.** For `n = 1` reproduced (check 8): the pushout has 6 objects, 20 arrows and the homology of `S³`; the argument for `n ≥ 2` (retraction onto the same six-object category) read. |
| E.8 | Proved | **Proved.** |
| E.9 | Refuted | **Proved.** |
| E.10 | Refuted | **Proved.** |
| E.11 | Open | Open (STRATA E.11). |
| E.12 | Known | **Proved**; finality of the fork reproduced (check 8). |
| E.13 | Refuted | **Proved** (CATHOT F.2, followed again). |

Counts: 76 statements. Proved or known and confirmed by this review (with the qualifications in the tables): 66. Unverified: 4 (B.9, C.5, D.15, D.21). Open in the answer: 6 (A.8, B.8, C.9, C.10, D.22, E.11). False: none.

## Corrections to my leads and to earlier records

- Lead 1: the weak-vertical half is the hammock localization (known). The other half ("with two-out-of-three the vertical arrows are forced into `Σ`") is false as an isomorphism of categories (B.3), true for short fractions (B.5), and open as a weak equivalence (B.8).
- Lead 2: true; the reason given in parentheses (an initial object) is wrong for the category over all types and is replaced by B.4.
- Lead 3: the implication "rectifiable ⇒ test (b)" holds (D.4); the clause that the finite example fails rectifiability is false (D.2).
- The pilot overview, 2.3 B ("for `Σ` = isomorphisms it does, by an initial-object argument"): the statement stands, the argument is B.4's.
- The handoff said of my `Δ_inj` example "unchecked by anyone else": it is now checked (A.5).
- The "After PATHS" sections of `7_BISITE`, LM4, LM5 cite only statements confirmed above, except D.15 (cited there with its dependence on the preprint).

## Changes to the companion, for the next integration

Chapter VII (VII-b, VII-c):
1. Row VIIc-A046: the question left open for the geometric padding functors is answered: not invertible in `Cat hot` (C.P5, the four-object crown), weak equivalences in `Hot` for every admissible `Σ` (C.P3, C.P4). Row V-I066 likewise. New block at VII ms. 121–124 with C.P5.
2. Row VIIb-C026 and the block at VII ms. 99–110: the exact condition A.3 (comma categories of the base functor weakly contractible), the counterexample A.4, and the proof for the path fibration by the action of the type categories (C.P1–C.P3). New block: the categories `P(τ, σ)` and the descent to the reachability preorder.
3. Row VIIc-C042: add that the functor is not a Grothendieck fibration either (E.3, second half). Row VIIc-C005: add E.4 (smooth and proper, not a fibration or opfibration) and the factorization E.5 at XII ms. 188–207.
4. Block at VII ms. 65–74: A.P1 as stated (no vertical arrow is inverted); B.3; B.4 for `Σ ⊂ Iso`; B.6 (the full path space retracts onto the mapping space); the open question B.8 stated as such.

Chapter IX (VIII-X):
5. Row IX-037: associativity for every admissible `Σ` is proved (C.P4): status to proved, with C.1.
6. Rows IX-080, IX-081: D.1 (the first form of (b) is vacuous if "homotope" means weakly equivalent), D.5 (failure between finite shapes), D.2–D.3 (the finite example satisfies everything and lacks `x × x`), D.K4–D.K5 (unbounded shapes force 1-types). Row IX-088 stays, with D.4 and D.6.
7. Rows IX-040, 041, 072 (C.5), IX-044, 049, 052 (C.3, C.4; C.10 open), IX-061, 065, 070 (C.8; C.9 open), IX-084, 087 (C.6, C.7).
8. Block at V ms. 44–46: D.K5.

Chapters XIII, XVII, XIX:
9. Block at XIII ms. 10 (row XIIIa-A046): one factorization suffices for each half, and with an initial object the class `Cof_W` is then a precofibration structure, so finite direct diagrams are rectified (D.8); the diamond and the finite sets as limits (D.9). Row XIX-C099 already agrees with D.17 (3).

Chapters XII and XVI:
10. Row XIIc-a C033 (`Liss ∩ Prop ⊂ Fib_W`): true for `W∞`; false for `W_0`, `W_n`, rational homology and every homology localizer when `Liss`, `Prop` are the `W`-smooth and `W`-proper functors (the section above). Block at XII ms. 225.
11. Row XVI-C105 and the block at XVI ms. 87: the second proof D.23; the accessibility-free direction of POLES E.2 (D.18).
12. XII ms. 228–234 (the interval; POLES H.6): the case `n = 1` (E.7).
13. II-a and XIIb-a (the TOTASPH integration block on colimits in `Cat`): A.2, A.5, A.7, with A.8 open.
14. Row VIc-C022: E.6 and E.11 (still open over the five-element monoid).

## What is left

- **B.8**, the question the prompt was written for. What is proved: the inclusion `J` is injective on all homotopy groups and bijective on components (B.6), an equivalence for `Σ ⊂ Iso` and `Σ` = all arrows (B.4). First undecided case: the chain `0 < 1 < 2` with `0 → 2` marked, whose localization is, as far as I remember (Lurie, *Higher Topos Theory*, §4.4.5; not opened), the ordinary category of a retraction, with discrete mapping spaces; if so the question there is whether the full path categories of that five-arrow category are homotopy discrete.
- A.8 (which shapes compute colimits in `Cat` correctly), C.9, C.10 (linear and pointed versions of the literal path categories), D.22 (six items: recognition on finite shapes, the finite-product upgrade, Barwick–Kan fibrancy on finite shapes, intrinsic cofibrations without an initial object, the two forms of test (b), non-accessible localizers), E.11.
- Not verified by me: B.9; C.5; D.15 and D.21 (Kaledin's theorem); the cited numbers in Arakawa–Cnossen, Kerodon, Lenz, Chachólski–Scherer, Groth, Keller, Quillen, Dwyer–Kan (*Function complexes*), Arlin, Fuentes-Keuthan–Kędziorek–Rovelli, Higman–Neumann–Neumann, Baumslag–Dyer–Heller; the unfolding of the coherent-nerve step in C.P2 and of the cocone in B.6; the identification `(N_ξ F)_0 = Ex² NF` in D.12; D.17 (3)–(4) in detail.
