# INDLOCAL: which ind-objects of categories up to natural transformation are homotopy invariant

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for your deliverables: `INDLOCAL`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max, CATHOT expert); revised the same day by Claude Fable 5.2
(effort max, Dérivateurs expert) so that it starts from the results now in hand (the draft before this revision:
`PROMPT_before_results_20261112.md`); revised again on 13 Nov 2026 by the Dérivateurs expert after the intake of
the return PATHS (R6, R7, R8 and Part C; the version before: `PROMPT_before_paths_intake_20261113.md`). Kind of
prompt: two theorems with written proofs (R2 and R3, two proofs each; R7, one proof), to be checked and pushed
further; plus hunches to prove, refute or develop. The attached files are listed in `MANIFEST.tsv` at the root of
each of the two background zips and in `README_NEW_RESULTS.md` of the third zip.

## What is to be settled

In Chapter V of *Les Dérivateurs* (ms. 11–13, 37–52) Grothendieck works in `Cat hot` (small categories, functors
modulo zigzags of natural transformations) and with ind-objects K = (K_n) of it, which ind-represent the functors
X ↦ Hom_{M(X)Σ_X^{-1}}(a_X, b_X) of a localization (V ms. 44–46). He asserts (V ms. 46) that such a functor factors
through Hot if and only if K can be represented by a sequence of "catégories de Thomason–Kan", and builds on this in
VII ms. 108–136 and IX ms. 9–13, 22–25.

**Your task: check the two proofs of the theorem below (R2, R3) and the proof of the theorem R7, and then
determine what they leave: the exact classes of invariant ind-objects in the neighbouring situations, the
consequences at each page of the manuscript, the open item E.6 of CATHOT, and what remains of its items E.26 and
E.27, which the return PATHS has proved since (R6).** A report on the proofs is not the task;
confirmations step by step, errors with repairs, proofs and counterexamples are.

## Results this prompt builds on (status on 12 Nov 2026)

"CATHOT", "GALOIS", "PATHS" and "PRESHEAF_TOTALITY" (PRETOT) are returns of GPT-6 Astra (effort Pro, ChatGPT Pro
mode) to earlier prompts. "CATHOT
expert" and "Dérivateurs expert" are two agents of Claude Fable 5.2 (Anthropic) at effort max. None of the
results is an authority; none is to be proved again as if open. For each one you use: read the proof at the
place given and either confirm each step with your own argument, or give the first wrong step with a repair or a
counterexample.

- **R1 (CATHOT; checked row by row by the CATHOT expert, `CATHOT_REVIEW.md`).** A category K with
  π₀Fun(X, K) → [BX, BK] bijective for all X ("local") is exactly a category isomorphic in `Cat hot` to a groupoid
  (C.1–C.4); X ↦ [BX, Y] is representable only for 1-types Y; with Thomason-fibrant in place of local the
  statement of V ms. 46 is false (C.6); on finite tests every homotopy type is ind-representable (D.1, D.3); an
  index category that is large in the universe escapes all of this (D.7). Left open there: E.17 (the ind-version;
  now R3), E.6, E.26 and E.27 (the last two now R6).
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
  (a, b) are homotopy fibres in the colimit (H6 is superseded for Part C4 by R6).
- **R5 (Dérivateurs expert, `RESULT_FILTERED_BY_ONE_TYPES.md`; checked and corrected in PRETOT F.1, F.4 (GPT-6 Astra)
  and in the review of PRETOT).** For a small category `A`: `∫_A D → colim^{Cat}_A D` is a weak equivalence for every
  `D: A → Cat` iff every connected component of `A` is filtered (as first stated, "iff `A` is filtered", it fails for
  the empty category and the discrete category on two objects); for non-empty connected `A`, iff `A` is filtered.
  Abelian groups with colimits in Ab already detect filteredness (PRETOT F.6). (Used in Part C only.)

- **New since this prompt was drafted (12 Nov 2026): PRESHEAF_TOTALITY, reviewed.** Attached as `INDLOCAL_new_results.zip`: the return PRESHEAF_TOTALITY (`PRETOT_return/`: paper, results, programs; GPT-6 Astra, ChatGPT Pro mode) and its review by Claude Opus 5.5 at effort max (`PRETOT_review/REVIEW.md`, `FINDINGS.md`). The review checked all 54 statements: none wrong; G.3 correct with a gap; A.12, D.4, E.1, F.14 and G.2 known; C.4, E.9, F.10 and F.16 open as stated. Theorem A.5 was recomputed independently: a 52-element act over `End_Δ([2])` whose element category is integrally acyclic with `π₁ ≅ SL(2,5)`, so total `W_ℤ`-asphericity does not imply total `W∞`-asphericity for presheaves. Checked since then (Claude Opus 5.5, effort max; `PRETOT_review/POINCARE_SPINE_CHECK.md`): the 2-complex of A.5 (`π₁ ≅ 2I`, `χ = 1`, presentation `⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩`) is homotopy equivalent to the Poincaré homology sphere `Σ(2,3,5)` minus an open ball, by Nicholson, arXiv:1905.12018, Theorem A, with `m_ℍ(2I) = 2`. F.3 and F.6: a sifted totally aspherical category is filtered, and abelian-group diagrams detect filteredness. Cite its statements by number where they bear here. F.16 is closed since by the return PATHS (R6).

- **R6 (the return PATHS; GPT-6 Astra, ChatGPT Pro mode, 11 Nov 2026; intake of 12 Nov 2026 by Claude Fable 5.2 at
  effort high: all 76 statements, none found wrong, C.P1–C.P4 followed step by step; `PATHS_intake/REVIEW.md`,
  `PATHS_intake/FINDINGS.md` F1).** Notation: `M` a small category, `Σ` a wide subcategory; `F_τ(a, b)` the category
  of functors `I_τ → M` with backward edges in `Σ` and endpoints `a, b`, with all natural transformations that are
  identities at the two endpoints (the interior vertical arrows are arbitrary); `Ch_Σ(M; a, b)` the fibred
  Grothendieck construction of `τ ↦ F_τ(a, b)` over `Ty`; `Ch^Σ_Σ(M; a, b)` the same with all vertical components in
  `Σ` (the Dwyer–Kan hammock model); `J: Ch^Σ_Σ → Ch_Σ` the inclusion. Verified statements:
  - A.P1: `π₀Ch_Σ(M; a, b) = Hom_{M[Σ⁻¹]}(a, b)`, compatibly with concatenation.
  - C.P1: the poset `P(τ, σ)` of type maps `τ → σ` (ordered by pointwise arrows of `I_σ`) is empty or
    contractible; these posets make `Ty` a strict 2-category, which acts strictly on the categories `F_τ(a, b)`.
  - C.P2: the diagram `τ ↦ BF_τ(a, b)` on `Ty^op` descends coherently to the reachability preorder of types, and
    over that preorder `Ty^op` is homotopy final, as is every sequence of types `t_0 ← t_1 ← …` such that each
    type receives a map from some `t_n`.
  - C.P3: for every such sequence both legs of `C_∞(t) ← E_t → Ch_Σ(M; a, b)` are weak equivalences; a strictly
    commuting map of sequences induces a weak equivalence; the comparisons are canonical and transitive in Hot.
    This is CATHOT E.26 (1)–(3) for every wide `Σ`. It closes PRETOT F.16 and answers Grothendieck's question at
    VII ms. 103 (b), which he answers "en général pas" at ms. 112 and reopens in footnote 24 at ms. 113:
    `C_∞ ≃ C` in Hot for `T = Ty`, `C = Ch_Σ(X; a, b)`.
  - C.P4: for a block `τ₀` containing both signs the padding maps `q_L`, `q_R` are weak equivalences, and the
    operation `κ(q_L⁻¹ × q_R⁻¹)` is associative, unital and independent of the block in Hot: it is strict
    concatenation transported. This is CATHOT E.27. For a block with one sign it fails (intake, F1; the return
    states the restriction and gives no counterexample): the powers of the block are not cofinal, and for the
    crown `0, 2 → 1, 3` with all arrows marked and `a = b = 0` the category `F_{+ⁿ}(0, 0)` is one point, against
    `ΩS¹ = Z`.
  - C.P5: for the same crown `q_L` is a weak equivalence with no inverse in `Cat_hot`.
  - A.2 (= PRETOT F.13): over a filtered index the Grothendieck construction maps to the colimit in Cat by a weak
    equivalence. A.3: for `u: J → T`, `∫_J Fu → ∫_T F` is a weak equivalence for every `F: T^op → Cat` iff every
    `u/t` is weakly contractible. A.4 (= PRETOT F.14): the hypotheses of VII ms. 99–101 do not suffice (`T = BC₂`;
    Grothendieck's own example at ms. 109).
  - D.K4 (= GALOIS B.12, Proof 2 of R3). D.K5: the formula of V ms. 44–45,
    `Hom_{M^X[Σ_X⁻¹]}(a_X, b_X) = colim_n π₀Fun(X, K_n)` with `K_n = F_{t_n}(a, b)` for any cofinal sequence. D.1:
    read as "isomorphic in Hot to a Thomason-fibrant category", the condition "homotope à une catégorie de
    Thomason–Kan" holds for every small category and is no criterion. D.5: the invariance of
    `X ↦ Hom_{M^X[Σ_X⁻¹]}(a_X, b_X)` under weak equivalences can fail between finite categories.
  - Left open in the return: B.8 (is `J` a weak equivalence?). B.6 describes a map from `B Ch_Σ(M; a, b)` to the
    mapping space of the localization and does not construct it in detail. For both see R7.
- **R7 (the path categories with arbitrary vertical arrows are the mapping spaces of the localization; one written
  proof, by Claude Fable 5.2 at effort high in the intake of PATHS: `PATHS_intake/FINDINGS.md`, F2 and F3).** For
  every small category `M`, wide subcategory `Σ` and objects `a, b` there is an equivalence
  `B Ch_Σ(M; a, b) ≃ Map_{L(M,Σ)}(a, b)`, natural in `a ∈ M^op`, sending the empty path at `b` to the identity;
  `L(M, Σ)` is the ∞-categorical localization, and no two-out-of-three, saturation or calculus of fractions is
  assumed. Consequence (F3): `J` is a weak equivalence for every wide `Σ`; that is PATHS B.8.
  The proof of F2 is written out in full. With `h_b = Hom_M(−, b)` and `s` the origin functor on the paths ending
  at `b` with free origin, it defines the presheaf of spaces `X_b(a) = B(a ↓ s)` on `M` with a map `h_b → X_b`,
  shows `X_b(a) ≃ B Ch_Σ(M; a, b)`, and proves (i) `X_b` inverts `Σ` (prepending the backward edge `w` is inverse
  to prepending the forward edge `w`), and (ii) for every presheaf of spaces `Q` that inverts `Σ`,
  `Map(X_b, Q) → Q(b)` is an equivalence: `Map(X_b, Q) = holim_{τ ∈ Ty} A_τ` with
  `A_τ = holim_{c ∈ F_τ(−, b)^op} Q(c_0)`; collapsing the first edge induces an equivalence `A_{ετ'} → A_{τ'}` for
  each sign `ε` (for `+`: forgetting the first vertex is an opfibration with fibres `M/c'_0`; for `−`: padding is
  left adjoint to it and `Q(w)` is invertible); and `Ty` has a terminal object. F3 leaves two steps unwritten (the
  passage from "functorial up to coherent natural transformation" to a presheaf for `Ch^Σ_Σ`; the form of the
  Dwyer–Kan theorem used, with Arakawa–Cnossen, Theorem 4.7 and Corollary 1.11).
  Second reading (Dérivateurs expert, 13 Nov 2026; `PATHS_intake/SECOND_READING_F2.md`): F2 followed step by step, no error found; one remark: for the
  sign `+`, forgetting the first vertex is also left adjoint to padding, so restriction along padding is an
  equivalence for every diagram, and the hypothesis on `Q` is used for the sign `−` only. F3 read in outline; its
  two unwritten steps were not checked. The intake's computations on five relative categories agree with the
  theorem (`PATHS_intake/scratch/`). No search of the literature has been made (the return PATHS reports a
  MathOverflow question of 2020 and no proof located).
- **R8 (`Ty^op` is not totally aspherical; Dérivateurs expert, 12 Nov 2026; a proof in three lines and an
  enumeration, `ty_check.py`; read by nobody else).** For words `τ, ρ` in `+, −`, `Hom_Ty(τ, ρ)` is the set of
  weakly increasing sign-preserving maps from the letters of `ρ` to the letters of `τ` (PRETOT E.1). Let
  `e, c: (+−+) → (++)` in `Ty` be given by the letter maps `(1, 3)` and `(1, 1)`. There are no type `σ` and
  `g, h: σ → (+−+)` with `eg = ch`: the letter map of `g` is strictly increasing (`g(1) < g(2) < g(3)`, the signs
  alternate), so that of `eg` is injective, and that of `ch` is constant. So in `Ty^op` the span
  `(+−+) ← (++) → (+−+)` has no completion to a commutative square, while a totally `W∞`-aspherical category
  completes every span (TOTASPH C.11, checked; `TOTASPH_C.tex`). The same computation shows that the pair has no
  affine equalizer, and that the presheaf of sets `σ ↦ Hom_Ty(σ, (++))/(eg ∼ cg)` on `Ty` has a category of
  elements with `H₁ = Z`. So over the shape `Ty^op` not even colimits of sets are homotopy colimits for all
  diagrams: nothing about `Ch(X) → Ty` follows from properties of the shape, and what PATHS proves is special to
  the path diagram (C.P1).

## WHAT THE OUTCOME MUST BE

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

1. **Deliverables.** One ZIP: `INDLOCAL_paper.tex` and PDF (LuaLaTeX, compiles cleanly); `INDLOCAL_results.csv`
   (one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_pages_settled,
   notes`); `INDLOCAL_references.bib` (entries marked `verified` or `unverified`); `INDLOCAL_report.md`; `code/`.
2. **Done, for each numbered item below:** (a) proved, in the stated or the strongest correct form, with a complete
   proof; or (b) refuted by a complete counterexample (checked by program when finite), with the strongest true
   statement in its place, proved. Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack the obstruction, starting from that instance. An item that says "check" is done only
   as: every step of the written proof confirmed with your own argument, or the first wrong step with a repair
   or a counterexample. "Known" counts only with the derivation from the cited theorem, hypotheses checked.
3. **Not acceptable:** an assessment of the proofs without step-by-step confirmation or a counterexample; proving
   R1–R3 or the statements of R6 again from nothing in place of the pushes; accepting R7, R8 or a statement of R6
   without confirming the steps you use; a survey; "open, see [reference]"; a plan or outline; a
   statement dropped without a row.
4. **Finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `INDLOCAL_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.
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

**C. The manuscript, page by page (statuses after the intake of PATHS: R6, R7, R8).**

C1 (status: the formula is proved in PATHS D.K5, verified in the intake, for `K_n = F_{t_n}(a, b)` with arbitrary
vertical arrows and any cofinal sequence of types). Check D.K5, both proofs (by words and commutative ladders; by
C.P3 applied to `(M^X, Σ_X)` with the identification of its fixed-type path categories with `Fun(X, K_n)`). Then
determine the exact domain of validity of Grothendieck's formula
Hom_{M(X)Σ_X^{-1}}(a_X, b_X) = colim_n π₀Fun(X, Ch_{n,Σ}(a, b)) (V ms. 44–45) for his own path categories and
indexing (VII ms. 65–67, 50′–53, 99–102, 138): for which sequences of types, which Σ and which X it holds, with
proof, and a counterexample outside that domain. (Corollary 3.3 (b) of `OWN_RESULTS.md` uses it without proof.)

C2 (status: the first half is PATHS D.K4 and D.K5, verified). Check: for a U-small (M, Σ), if the functor of C1
is W∞-invariant on Cat_U then it depends only on Π₁X. Then classify the small relative categories for which this
happens: necessary and sufficient conditions on the mapping spaces of the localization L(M, Σ) and on the
comparison functors `M^X[Σ_X⁻¹] → Ho Fun(X, L(M, Σ))`, with examples where the fundamental groups of the mapping
spaces are not trivial. By R7 the mapping spaces are `B Ch_Σ(M; a, b)` for every (M, Σ), with no comparison
hypothesis; rely on that only once C4.3 has confirmed R7.

C3 (status: for VII §§4–6 and §10 the true statements are known, from PRETOT F.12–F.15 and PATHS A.2–A.4, C.P3,
C.P4, all reviewed; the rewriting is to do). Rewrite V ms. 46–49, VII ms. 129–132 and IX ms. 22–23: for each
sentence that uses "catégorie de Thomason–Kan", the statement that is true, with proof (verified inputs: PATHS
D.1, D.5, D.K4, D.K5); and for each colimit of categories taken there along a system, say whether the system is
filtered (R5: only then is the colimit in Cat a homotopy colimit for all diagrams). For VII §§4–6 and §10
(ms. 26–32, 48–58, 99–115) write the true statements out, each with its proof or with its citation checked, from
these inputs: `Ch(X)` is fibred over `Ty`, so the relevant shape is `Ty^op`, which is not filtered (PRETOT F.12)
and not totally aspherical (R8), while `Ty` has the empty type as terminal object (PRETOT E.4); `C_{N°} → C_∞` is
always a weak equivalence (PRETOT F.13 = PATHS A.2); the transition displayed at ms. 102 is reversed (it is
`C_{t_{n−1}} → C_{t_n}`); cofinality in the associated preorder does not suffice for a general fibration (PATHS
A.4 = PRETOT F.14; Grothendieck's own example at ms. 109), and the condition that is exact and uniform in the
fibration is PATHS A.3; for `C = Ch_Σ(X; a, b)` over `Ty` the arrow `C_∞ → C` is an isomorphism in Hot, canonical
and independent of the sequence (PATHS C.P3), so the "conviction" of ms. 112 is wrong, the correction in footnote
24 is right, and the arrow marked "en général pas un isomorphisme" in the diagram of ms. 114 is one for the path
categories; his sufficient condition at ms. 112 (`T → T_o` smooth and coaspherical, or proper and aspherical)
fails for `Ty`, as he says, and the property of `Ty` that is used instead is C.P1; a composition
`C_∞(a, b) × C_∞(b, c) → C_∞(a, c)` exists in Hot, canonical, associative and unital (PATHS C.P4, for blocks with
both signs), which answers ms. 111 and 115. Check R8 (the three lines and the enumeration), and determine what it
changes at each place of VII where a property of the shape `Ty` or `Ty^op` is used or hoped for (ms. 109–110: "Il
n'est pas dit, certes, que Ty ne satisfasse pas à ces conditions draconiennes").

C4 (status: CATHOT E.26 and E.27 are proved for every wide Σ in PATHS C.P3 and C.P4, verified in the intake; E.27
holds for blocks containing both signs and fails for blocks with one sign; the comparison with the simplicial
localization, left open in PATHS B.8, has the written proof R7).
C4.1. Check PATHS C.P1–C.P4 step by step: the contraction of `P(τ, σ)` by clamping runs; the strict action
`P(τ, σ) × F_σ → F_τ` and the place where it needs arbitrary interior vertical arrows; the descent to the
reachability preorder (in the model-category form of the intake, FINDINGS F1 step 3, and in the form with coherent
nerves of the return); the two finality statements with their comma categories; the identity
`β_P μ = γ(β_P × β_P)`.
C4.2. Blocks with one sign: prove that their powers are not cofinal, check the crown example of R6, and determine
for every one-sign block and every wide Σ which of the assertions of VII ms. 125–127 hold and which fail.
C4.3. Check the proof of R7 (F2), each step with your own argument: the presheaves that invert Σ are the presheaves
on L(M, Σ), and `Map_L(−, b)` is the localization of `h_b`; the Thomason step and its naturality in `a`; the
functors `i` and `r`; (i); (ii) for each of the two signs; the conclusion from the terminal object of `Ty`; the
naturality in `a` and the image of the empty path; the by-product that for each single type `τ` the map
`h_b → X_b^τ` is already an equivalence after localization. Then F3: write out its two unwritten steps, or find
the error, so that PATHS B.8 is proved or refuted.
C4.4. Push R7. Prove or refute: the equivalences `B Ch_Σ(M; a, b) ≃ Map_{L(M,Σ)}(a, b)` are natural in `b` and
compatible with composition (concatenation of paths on one side, composition in L(M, Σ) on the other; for blocks
with both signs, the operation of C.P4). Determine the map `Q` of PATHS B.6 in these terms and prove or refute that it
is an equivalence. Search the literature for R7 (Dwyer–Kan 1980; Low–Mazel-Gee, arXiv:1409.8192; Mazel-Gee,
arXiv:1510.03961; Arakawa–Cnossen, arXiv:2608.19870; the treatments of the calculus of fractions for
∞-categories) and say, after opening each, whether the statement or a special case of it is there.
The smallest instance for hand checks is the block (+, −, +) with left, right and symmetric padding. Any
comparison you use must be between the specified maps.

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

The files of `INDLOCAL_background_1.zip` and `INDLOCAL_background_2.zip` (the second holds only Hausmann–Husemoller
1979), listed with their origins in `MANIFEST.tsv` at the root of each: `OWN_RESULTS.md` (§3; §§1–2 are not part of
this task), `HUNCHES.md`, `CATHOT_REVIEW.md`, `CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`, `GALOIS_REVIEW.md`,
`RESULT_FILTERED_BY_ONE_TYPES.md`; the CATHOT paper, results table, report and Parts B, C, D, E; the GALOIS paper,
results table, conventions and the sections with B.9–B.12 (both returns are AI-produced by GPT-6 Astra: a colleague's
drafts, not authorities); Grothendieck's text `DER_III-V.tex`, `DER_VII-b.tex`, `DER_VII-c.tex`, `DER_VIII-X.tex` (the
French transcription corrected on 11 Nov 2026; AI-made from the edition of Künzer, Malgoire and Maltsiniotis; where a
formula looks wrong, say so and reason from the mathematics); Thomason 1980; Cisinski 1999 (Dwyer and pseudo-Dwyer
morphisms, Part D); Raptis 2010; May–Stephan–Zakharevich 2017; Quillen 1973; Hausmann–Husemoller 1979; Palmer–Wu,
arXiv:2510.16879v1; Shoikhet, arXiv:1412.0317v4; Chachólski–Scherer, arXiv:math/0110316v1; the OpenAI manuscript on
Thomason structures (Part E). Not attached, to be obtained by you and marked verified only if opened: Kan–Thurston
(Topology 15, 1976), Baumslag–Dyer–Heller (J. Pure Appl. Algebra 16, 1980), Maunder 1981.

In `INDLOCAL_new_results.zip` (listed in its `README_NEW_RESULTS.md`): the return PRESHEAF_TOTALITY and its review
(`PRETOT_return/`, `PRETOT_review/`); and, added on 13 Nov 2026: `PATHS_return/` (the return PATHS: paper,
sections, results table, report, bibliography, programs and outputs); `PATHS_intake/` (`REVIEW.md`, `FINDINGS.md`
with F1–F10, `IMPLICATIONS.md`, `SECOND_READING_F2.md`, and `scratch/` with the intake's own programs and outputs); `PATHS_papers/`
(Arakawa–Cnossen, *Hammock localization via Segal animae*, arXiv:2608.19870, LaTeX; Dwyer–Kan 1980, *Simplicial
localizations of categories*, *Calculating simplicial localizations* and *Function complexes in homotopical
algebra*; Low–Mazel-Gee, arXiv:1409.8192; Mazel-Gee, arXiv:1510.03961); `ty_check.py` and `ty_check.out` (R8);
`TOTASPH_C.tex` (TOTASPH C.5 and C.11, used in R8); `DER_VII-a.tex` (VII ms. 1–57: the pages on `Ty`).

## Rules of proof

1. State each claim with quantifiers, universe and size conditions, which localizer, pointed or unpointed.
2. Type every map; compositions must type-check; say in which category an isomorphism holds (Cat, Cat_hot,
   Ind(Cat_hot), Hot).
3. Every reduction comes with its comparison map and the proof that the property transfers in the direction used.
4. A counterexample is complete and, when finite, checked by a program you attach. One verified counterexample
   refutes: say "false". An invalid proof shows a gap, not falsity.
5. No authority: Grothendieck's assertions, CATHOT, GALOIS, PATHS, PRETOT, their reviews and intakes, the attached
   notes, R7, R8 and the hunches are all to be checked where you use them. If a written proof is wrong, say so plainly and show where; then find the true
   statement.
6. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the
   smallest undecided instance. Known and Open are not end points.
7. Before calling anything new, search the literature and say what you searched (for R2: Kan–Thurston 1976,
   Baumslag–Dyer–Heller 1980, Maunder 1981, Hausmann 1986, Leary 2013). Never invent a reference.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority. This task is long by design. Work through all parts completely; do not stop at an outline, a
sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an interruption loses little.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `<ID>_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
