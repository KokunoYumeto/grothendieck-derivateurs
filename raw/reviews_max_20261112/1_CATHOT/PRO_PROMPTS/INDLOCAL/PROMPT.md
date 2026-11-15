# INDLOCAL: which ind-objects of categories up to natural transformation are homotopy invariant

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for your deliverables: `INDLOCAL`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max, CATHOT expert); revised the same day by Claude Fable 5.2
(effort max, Dérivateurs expert) so that it starts from the results now in hand (the draft before this revision:
`PROMPT_before_results_20261112.md`). Kind of prompt: a theorem with two written proofs, to be checked and pushed
further; plus three hunches to prove, refute or develop. The files to attach are listed in `ZIP_LIST.tsv`.

## What is to be settled

In Chapter V of *Les Dérivateurs* (ms. 11–13, 37–52) Grothendieck works in `Cat hot` (small categories, functors
modulo zigzags of natural transformations) and with ind-objects K = (K_n) of it, which ind-represent the functors
X ↦ Hom_{M(X)Σ_X^{-1}}(a_X, b_X) of a localization (V ms. 44–46). He asserts (V ms. 46) that such a functor factors
through Hot if and only if K can be represented by a sequence of "catégories de Thomason–Kan", and builds on this in
VII ms. 108–136 and IX ms. 9–13, 22–25.

**Your task: check the two proofs of the theorem below (R2, R3), and then determine what the theorem leaves: the
exact classes of invariant ind-objects in the neighbouring situations, the consequences at each page of the
manuscript, and the three open items E.6, E.26, E.27 of CATHOT.** A report on the proofs is not the task;
confirmations step by step, errors with repairs, proofs and counterexamples are.

## Results this prompt builds on (status on 12 Nov 2026)

"CATHOT" and "GALOIS" are returns of GPT-6 Astra (effort Pro, ChatGPT Pro mode) to two earlier prompts. "CATHOT
expert" and "Dérivateurs expert" are two agents of Claude Fable 5.2 (Anthropic) at effort max. None of the
results is an authority; none is to be proved again as if open. For each one you use: read the proof at the
place given and either confirm each step with your own argument, or give the first wrong step with a repair or a
counterexample.

- **R1 (CATHOT; checked row by row by the CATHOT expert, `CATHOT_REVIEW.md`).** A category K with
  π₀Fun(X, K) → [BX, BK] bijective for all X ("local") is exactly a category isomorphic in `Cat hot` to a groupoid
  (C.1–C.4); X ↦ [BX, Y] is representable only for 1-types Y; with Thomason-fibrant in place of local the
  statement of V ms. 46 is false (C.6); on finite tests every homotopy type is ind-representable (D.1, D.3); an
  index category that is large in the universe escapes all of this (D.7). Left open there: E.17 (the ind-version),
  E.6, E.26, E.27.
- **R2 (a Kan–Thurston theorem with no small quotients; two independent proofs).** For a connected CW complex W
  and a cardinal μ there are a group G and an acyclic map t: BG → W (isomorphism on homology with every local
  coefficient system), onto on π₁ with perfect kernel P, such that every homomorphism from G to a group of
  cardinality ≤ μ vanishes on P. Hence [W, Y] → [BG, Y] is bijective for every Y whose fundamental groups have
  cardinality ≤ μ.
  Proof 1: `OWN_RESULTS.md`, Theorem 3.1 (CATHOT expert): transfinite induction over the cells; amalgams
  (G_α × A′) *_{H′} A″ with A′, A″ simple acyclic of large cardinality; for cells of dimension ≥ 3 it uses the
  Kan–Thurston theorem on a homotopy pull-back, with a cardinality bound quoted from memory. Read and found
  correct, given that bound, by the Dérivateurs expert (`CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`).
  Proof 2: GALOIS B.10, B.11 (GPT-6 Astra): simplicial cones over a triangulation, each cone group a simple
  acyclic group of cardinality λ > μ; subcomplex injectivity on π₁ by graphs of aspherical spaces; no use of the
  Kan–Thurston theorem and no cardinality bound from the literature. Checked step by step by the Dérivateurs
  expert (`GALOIS_REVIEW.md`, rows B.10, B.11).
- **R3 (E.17 of CATHOT is true; two independent proofs).** Let I be a U-small filtered category and
  K: I → Cat_hot a diagram of U-small categories. If H_K = colim_i π₀Fun(−, K_i) inverts W∞, then it inverts every
  unit η_X: X → Π₁X, and K → (Π₁K_i)_i is an isomorphism in Ind(Cat_hot). So the invariant small ind-objects are
  exactly the ind-objects of groupoids, and an invariant functor sees only Π₁X.
  Proof 1: `OWN_RESULTS.md`, Theorem 3.2 and Corollary 3.3. Proof 2: GALOIS B.12, which uses of acyclic maps only
  that they are epimorphisms of the homotopy category (GALOIS B.9: the fold map Y ∪ʰ_X Y → Y is a weak
  equivalence). Both read by the Dérivateurs expert (same files). The smallness of I is used once (one bound μ for
  all K_i).
- **R4 (CATHOT expert; `HUNCHES.md` H4, H5, H6: partial facts, not theorems).** (H4) E.6 is true when A is local
  and when A is a groupoid; the map (B × {0}) ∪ (A × Z) → B × Z is not a pseudo-Dwyer morphism when the upward
  closure of A in B is larger than A; expectation: E.6 is false in general. (H5) the groups used in R2, seen as
  one-object n-categories, see only the group-like part of a small n-category. (H6) for Σ = Mor(X) every constant
  section X → Fun(I_τ, X) is a weak equivalence compatible with type morphisms; missing: that strict fibres over
  (a, b) are homotopy fibres in the colimit.
- **R5 (Dérivateurs expert; `RESULT_FILTERED_BY_ONE_TYPES.md`; not checked by anyone).** For a small category A:
  ∫_A D → colim^{Cat}_A D is a weak equivalence for every D: A → Cat iff A is filtered. (Used in Part C only.)

## WHAT THE OUTCOME MUST BE

1. **Deliverables.** One ZIP: `INDLOCAL_paper.tex` and PDF (LuaLaTeX, compiles cleanly); `INDLOCAL_results.csv`
   (one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_pages_settled,
   notes`); `INDLOCAL_references.bib` (entries marked `verified` or `unverified`); `INDLOCAL_report.md`; `code/`.
2. **Done, for each numbered item below:** (a) proved, in the stated or the strongest correct form, with a complete
   proof; or (b) refuted by a complete counterexample (checked by program when finite), with the strongest true
   statement in its place, proved; or (c) partly settled, with the cases proved, the computations run, the
   obstruction as an exact statement and the smallest undecided instance. An item that says "check" is done only
   as: every step of the written proof confirmed with your own argument, or the first wrong step with a repair
   or a counterexample. "Known" counts only with the derivation from the cited theorem, hypotheses checked.
3. **Not acceptable:** an assessment of the proofs without step-by-step confirmation or a counterexample; proving
   R1–R3 again from nothing in place of the pushes; a survey; "open, see [reference]"; a plan or outline; a
   statement dropped without a row.
4. **Finished** only when every item meets the bar; otherwise report what is unfinished, item by item.
5. **If the execution environment disconnects:** wait and retry for at least 10 minutes; then write every file out
   in the chat in full, each in its own code block headed by its file name, and continue in the chat.

## Parts

**A. The Kan–Thurston theorem with no small quotients (R2).** A1. Check Proof 2 (the construction of T(L) for
all subcomplexes at once; asphericity and injectivity through V = T(K^{(n−1)}) ∪ T(L); the local-coefficient
comparison; the van Kampen computation of G/N; perfectness; the simple cone groups). A2. Check Proof 1 (the lifting
step; the amalgam; the Mayer–Vietoris comparison; the "no small quotients" induction; limit ordinals), and either
prove the cardinality bound for the Kan–Thurston group that it quotes, with source, or record that Proof 1 depends
on it. A3. Push: (i) make the construction a functor on simplicial complexes and injective simplicial maps
(Proof 2 is natural for inclusions of subcomplexes), and decide what naturality survives for arbitrary simplicial
maps; (ii) decide whether the kernel P can be taken simple, and whether H_*(P) can be prescribed; (iii) decide
whether G can be taken with BG of dimension dim W when W is finite-dimensional (then μ must be bounded: give the
exact relation). A4. Prove that Map(W, Y) → Map(BG, Y) is a weak equivalence onto the components of maps killing
P, for Y not connected and unpointed maps.

**B. The exact scope of R3.** B1. Check both proofs of R3. B2. Decide the same question for arbitrary U-small
colimits of representables (not filtered): which W∞-invariant presheaves on Cat_hot are U-small colimits of
representables? B3. Other localizers. A W-invariant small ind-object, W ⊃ W∞, is an ind-groupoid by R3; determine
which ind-groupoids are W-invariant for W = W_n (functors inducing bijections on π₀ and isomorphisms on π_k for
k ≤ n, all base points), for W = W_Z, and for an arbitrary fundamental localizer W ⊃ W∞; classify the W-invariant
representable presheaves. B4. Bounded tests: for an infinite cardinal κ, classify the ind-objects K of Cat_hot
whose functor is W∞-invariant on categories with fewer than κ arrows (R1: every homotopy type occurs for κ = ℵ₀
and, with large stages, for every κ); give the exact relation between the size of the stages K_i and κ, using the
bound μ of R2. B5. The enlarged-universe version (CATHOT D.7): describe all V-small invariant ind-objects.

**C. The manuscript, page by page.** C1. Prove Grothendieck's formula
Hom_{M(X)Σ_X^{-1}}(a_X, b_X) = colim_n π₀Fun(X, Ch_{n,Σ}(a, b)) (V ms. 44–45) for his path categories, with his
definitions (VII ms. 65–67, 50′–53, 99–102, 138), or give its exact domain of validity. (Corollary 3.3 (b) of
`OWN_RESULTS.md` uses it without proof.) C2. Deduce from R3: for a U-small (M, Σ), if this functor is W∞-invariant
on Cat_U then it depends only on Π₁X; classify the small relative categories for which this happens (necessary and
sufficient conditions on the simplicial localization), with examples where the fundamental groups of the mapping
spaces are not trivial. C3. Rewrite V ms. 46–49, VII ms. 129–132 and IX ms. 22–23 accordingly: for each sentence
that uses "catégorie de Thomason–Kan", the statement that is true, with proof; and for each colimit of categories
taken there along a system, say whether the system is filtered (R5: only then is the colimit in Cat a homotopy
colimit for all diagrams). C4. Prove CATHOT E.26 and E.27 for Σ = Mor(X) (every left-cofinal sequence of types,
every block τ₀, the all-type projection), starting from R4 (H6), or find the first failure; then decide them for a
proper admissible Σ. The smallest instance is the block (+, −, +) with left, right and symmetric padding. A
natural tool is the Dwyer–Kan hammock localization; any comparison you use must be between the specified maps.

**D. The strict retraction (CATHOT E.6; R4, H4).** Let A be Thomason-fibrant, i: A → B a Thomason cofibration,
p: B → A with [p][i] = id_A in Cat_hot. Prove or refute: there is r: B → A with ri = id_A and [r] = [p] in Cat_hot.
Decide the homotopy extension property for zigzags of natural transformations that would imply it: for a
Thomason cofibration A → B and a fence Z, does every functor (B × {0}) ∪ (A × Z) → F into a fibrant F extend over
B × Z′ for some longer fence Z′ → Z? Smallest instance to decide by program or by hand: A a fibrant poset model of
the circle (or of the six-point 2-sphere), B obtained by attaching one copy of c Sd² Δ¹ at two points.

**E. One dimension up (R4, H5).** For strict 2-categories modulo the equivalence relation generated by lax (or
pseudo) natural transformations: prove or refute that X ↦ [N₂X, Y] is representable exactly when Y is a 2-type,
and that the local objects are those equivalent in this sense to 2-groupoids; state and prove the analogue of R3
(the groups of R2, as one-object 2-categories, are the test objects). Then state and attack the case of strict
n-categories (expected answer: the homotopy types of nerves of strict n-groupoids, which for n ≥ 3 are not all
n-types). You may use the Thomason model structure on nCat (OpenAI, *Thomason Model Structures in Every Strict
Higher Dimension*, 25 Sep 2026: claimed, unrefereed, formalized main theorem) only with the words "claimed (OpenAI,
2026, unrefereed)" and after checking the steps you use.

## Conventions

As in CATHOT: a universe U ∈ V; Cat = U-small categories; BX = |NX|; W∞; Hot = Cat[W∞⁻¹]; Cat_hot;
Π₁X = X[Mor(X)⁻¹] with unit η_X; "local" as above; Ind with U-small filtered index categories unless said
otherwise; a sieve is full and closed under sources. Manuscript pages as "V ms. 46".

## What is attached

The files of `ZIP_LIST.tsv`, under the names of its second column (`MANIFEST` in the zip lists every file with
its origin): `OWN_RESULTS.md` (§3; §§1–2 are not part of this task), `HUNCHES.md`, `CATHOT_REVIEW.md`,
`CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`, `GALOIS_REVIEW.md`, `RESULT_FILTERED_BY_ONE_TYPES.md`; the CATHOT paper,
results table, report and Parts D, E; the GALOIS paper, results table and the sections with B.9–B.12 (both
returns are AI-produced by GPT-6 Astra: a colleague's drafts, not authorities); Grothendieck's text `DER_III-V.tex`,
`DER_VII-b.tex`, `DER_VII-c.tex`, `DER_VIII-X.tex` (the French transcription corrected on 11 Nov 2026; AI-made from
the edition of Künzer, Malgoire and Maltsiniotis; where a formula looks wrong, say so and reason from the
mathematics); Thomason 1980; Raptis 2010; May–Stephan–Zakharevich 2017; Quillen 1973; Hausmann–Husemoller 1979;
Palmer–Wu, arXiv:2510.16879v1; Shoikhet, arXiv:1412.0317v4; Chachólski–Scherer, arXiv:math/0110316v1; the OpenAI
manuscript on Thomason structures (Part E). Not attached, to be obtained by you and marked verified only if
opened: Kan–Thurston (Topology 15, 1976), Baumslag–Dyer–Heller (J. Pure Appl. Algebra 16, 1980), Maunder 1981,
Dwyer–Kan (1980).

## Rules of proof

1. State each claim with quantifiers, universe and size conditions, which localizer, pointed or unpointed.
2. Type every map; compositions must type-check; say in which category an isomorphism holds (Cat, Cat_hot,
   Ind(Cat_hot), Hot).
3. Every reduction comes with its comparison map and the proof that the property transfers in the direction used.
4. A counterexample is complete and, when finite, checked by a program you attach. One verified counterexample
   refutes: say "false". An invalid proof shows a gap, not falsity.
5. No authority: Grothendieck's assertions, CATHOT, GALOIS, the attached notes and the hunches are all to be
   checked where you use them. If a written proof is wrong, say so plainly and show where; then find the true
   statement.
6. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the
   smallest undecided instance. Known and Open are not end points.
7. Before calling anything new, search the literature and say what you searched (for R2: Kan–Thurston 1976,
   Baumslag–Dyer–Heller 1980, Maunder 1981, Hausmann 1986, Leary 2013). Never invent a reference.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority. This task is long by design. Work through all parts completely; do not stop at an outline, a
sample or a plan, and do not ask whether to continue. Write the files from the start and extend them as you go.
