# INDLOCAL: which ind-objects of categories up to natural transformation are homotopy invariant

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for your deliverables: `INDLOCAL`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max). Kind of prompt: a result claimed with a full proof
(attached), to be checked and pushed further; plus three hunches to prove, refute or develop.

## What is to be settled

In Chapter V of *Les Dérivateurs* (ms. 11–13, 37–52) Grothendieck works in `Cat hot` (small categories, functors
modulo zigzags of natural transformations) and with ind-objects K = (K_n) of it, which ind-represent the functors
X ↦ Hom_{M(X)Σ_X^{-1}}(a_X, b_X) of a localization (V ms. 44–46). He asserts (V ms. 46) that such a functor factors
through Hot if and only if K can be represented by a sequence of "catégories de Thomason–Kan", and builds on this in
VII ms. 108–136 and IX ms. 9–13, 22–25. The return CATHOT (attached: its paper and results table) proved that a single
category K with π₀Fun(X, K) → [BX, BK] bijective for all X ("local") is exactly a category isomorphic in `Cat hot` to
a groupoid, that X ↦ [BX, Y] is representable only for 1-types Y, and left the ind-version open (its E.17). The
attached note `OWN_RESULTS.md`, §3, claims to settle it:

> **Theorem 3.1 (claimed).** Let W be a connected CW complex with one 0-cell and λ an infinite cardinal not less
> than its number of cells. There are a group G with |G| ≤ λ and an acyclic map t: BG → W (isomorphism on homology
> with every local coefficient system) such that every homomorphism from G to a group of cardinality < λ factors
> through π₁(t): G → π₁(W). Hence [W, Y] → [BG, Y] is bijective for every Y whose fundamental groups have
> cardinality < λ.
>
> **Theorem 3.2 (claimed).** Let I be a U-small filtered category and K: I → Cat_hot a diagram of U-small categories.
> If H_K = colim_i π₀Fun(−, K_i) inverts W∞, then it inverts every unit η_X: X → Π₁X, and K → (Π₁K_i)_i is an
> isomorphism in Ind(Cat_hot). So the invariant small ind-objects are exactly the ind-objects of groupoids.

**Your task: decide whether these two theorems are true, with complete proofs of your own, and then determine what
they leave: the exact classes of invariant ind-objects in the neighbouring situations, the consequences at each
page of the manuscript, and the three open items E.6, E.26, E.27 of CATHOT.** A report on the attached proof is not
the task; a proof or a counterexample is.

## WHAT THE OUTCOME MUST BE

1. **Deliverables.** One ZIP: `INDLOCAL_paper.tex` and PDF (LuaLaTeX, compiles cleanly); `INDLOCAL_results.csv`
   (one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_pages_settled,
   notes`); `INDLOCAL_references.bib` (entries marked `verified` or `unverified`); `INDLOCAL_report.md`; `code/`.
2. **Done, for each numbered item below:** (a) proved, in the stated or the strongest correct form, with a complete
   proof; or (b) refuted by a complete counterexample (checked by program when finite), with the strongest true
   statement in its place, proved; or (c) partly settled, with the cases proved, the computations run, the
   obstruction as an exact statement and the smallest undecided instance. "Known" counts only with the derivation
   from the cited theorem, hypotheses checked.
3. **Not acceptable:** an assessment of the attached proof without your own proof or counterexample; a survey;
   "open, see [reference]"; a plan or outline; a statement dropped without a row.
4. **Finished** only when every item meets the bar; otherwise report what is unfinished, item by item.
5. **If the execution environment disconnects:** wait and retry for at least 10 minutes; then write every file out
   in the chat in full, each in its own code block headed by its file name, and continue in the chat.

## Parts

**A. Theorem 3.1.** A1. Prove or refute it. Go through the attached proof step by step (the transfinite induction
over cells; the lifting step, which for cells of dimension ≥ 3 uses the Kan–Thurston theorem on a homotopy
pull-back; the amalgam (G_α × A′) *_{H′} A″ with A′, A″ simple acyclic of cardinality λ; the Mayer–Vietoris
comparison with local coefficients; the "no small quotients" induction; limit ordinals; cardinalities) and replace
each step by your own argument or by an exact repair. A2. State the Kan–Thurston theorem you use with its source
and the cardinality bound, and prove the bound. A3. Decide whether the use of Kan–Thurston can be removed (a direct
construction of the lift), and whether G can in addition be taken with H_*(ker π₁(t)) prescribed, or with the
kernel simple. A4. Prove the stated bijection [W, Y] → [BG, Y] in the unpointed form, for Y not connected.

**B. Theorem 3.2 and its exact scope.** B1. Prove or refute it. B2. Decide the same question for arbitrary U-small
colimits of representables (not filtered): which W∞-invariant presheaves on Cat_hot are U-small colimits of
representables? B3. Decide it for the other localizers: for W_n (functors inducing bijections on π₀ and
isomorphisms on π_k for k ≤ n, all base points) and for an arbitrary fundamental localizer W ⊃ W∞, classify the
W-invariant representable presheaves and the W-invariant small ind-objects of Cat_hot. B4. Bounded tests: for an
infinite cardinal κ, classify the ind-objects K of Cat_hot whose functor is W∞-invariant on categories with fewer
than κ arrows (CATHOT D.1, D.3 show that every homotopy type occurs for κ = ℵ₀ and, with large stages, for every
κ); give the exact relation between the size of the stages K_i and κ. B5. The enlarged-universe version (CATHOT
D.7): describe all V-small invariant ind-objects.

**C. The manuscript, page by page.** C1. Prove Grothendieck's formula
Hom_{M(X)Σ_X^{-1}}(a_X, b_X) = colim_n π₀Fun(X, Ch_{n,Σ}(a, b)) (V ms. 44–45) for his path categories, with his
definitions (VII ms. 65–67, 50′–53, 99–102, 138), or give its exact domain of validity. C2. Deduce from B: for a
U-small (M, Σ), if this functor is W∞-invariant on Cat_U then it depends only on Π₁X; classify the small relative
categories for which this happens (necessary and sufficient conditions on the simplicial localization), with
examples where the fundamental groups of the mapping spaces are not trivial. C3. Rewrite V ms. 46–49, VII ms.
129–132 and IX ms. 22–23 accordingly: for each sentence that uses "catégorie de Thomason–Kan", the statement that
is true, with proof. C4. Prove CATHOT E.26 and E.27 for Σ = Mor(X) (every left-cofinal sequence of types, every
block τ₀, the all-type projection), or find the first failure; then decide them for a proper admissible Σ. The
smallest instance is the block (+, −, +) with left, right and symmetric padding. A natural tool is the Dwyer–Kan
hammock localization; any comparison you use must be between the specified maps.

**D. The strict retraction (CATHOT E.6).** Let A be Thomason-fibrant, i: A → B a Thomason cofibration, p: B → A
with [p][i] = id_A in Cat_hot. Prove or refute: there is r: B → A with ri = id_A and [r] = [p] in Cat_hot. It is
true when A is in addition local, and in Hot. Decide the homotopy extension property for zigzags of natural
transformations that would imply it: for a Thomason cofibration A → B and a fence Z, does every functor
(B × {0}) ∪ (A × Z) → F into a fibrant F extend over B × Z′ for some longer fence Z′ → Z? Smallest instance to
decide by program or by hand: A a fibrant poset model of the circle (or of the six-point 2-sphere), B obtained by
attaching one copy of c Sd² Δ¹ at two points.

**E. One dimension up.** For strict 2-categories modulo the equivalence relation generated by lax (or pseudo)
natural transformations: prove or refute that X ↦ [N₂X, Y] is representable exactly when Y is a 2-type, and that the
local objects are those equivalent in this sense to 2-groupoids. Then state and attack the case of strict
n-categories (expected answer: the homotopy types of nerves of strict n-groupoids, which for n ≥ 3 are not all
n-types). You may use the Thomason model structure on nCat (OpenAI, *Thomason Model Structures in Every Strict
Higher Dimension*, 25 Sep 2026: claimed, unrefereed, formalized main theorem) only with the words "claimed (OpenAI,
2026, unrefereed)" and after checking the steps you use.

## Conventions

As in CATHOT: a universe U ∈ V; Cat = U-small categories; BX = |NX|; W∞; Hot = Cat[W∞⁻¹]; Cat_hot;
Π₁X = X[Mor(X)⁻¹] with unit η_X; "local" as above; Ind with U-small filtered index categories unless said
otherwise; a sieve is full and closed under sources. Manuscript pages as "V ms. 46".

## What is attached

`OWN_RESULTS.md` (the claimed proofs: §3; §§1–2 are not part of this task); the CATHOT paper, results table and
report (AI-produced by GPT-6 Astra; a colleague's draft, not an authority); Grothendieck's text `DER_III-V_text.tex`,
`DER_VII-b_text.tex`, `DER_VII-c_text.tex`, `DER_VIII-X_text.tex` (AI transcription of the edition of Künzer,
Malgoire and Maltsiniotis); Thomason 1980; Raptis 2010; May–Stephan–Zakharevich 2017; Quillen 1973;
Palmer–Wu, arXiv:2510.16879v1; Shoikhet, arXiv:1412.0317v4; Chachólski–Scherer, arXiv:math/0110316v1. `MANIFEST`
lists every file with its origin. Not attached, to be obtained by you and marked verified only if opened:
Kan–Thurston (Topology 15, 1976), Baumslag–Dyer–Heller (J. Pure Appl. Algebra 16, 1980), Dwyer–Kan (1980).

## Rules of proof

1. State each claim with quantifiers, universe and size conditions, which localizer, pointed or unpointed.
2. Type every map; compositions must type-check; say in which category an isomorphism holds (Cat, Cat_hot,
   Ind(Cat_hot), Hot).
3. Every reduction comes with its comparison map and the proof that the property transfers in the direction used.
4. A counterexample is complete and, when finite, checked by a program you attach. One verified counterexample
   refutes: say "false". An invalid proof shows a gap, not falsity.
5. No authority: Grothendieck's assertions, CATHOT, the attached note and the hunches are all to be proved or
   refuted. If the attached proof is wrong, say so plainly and show where; then find the true statement.
6. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the
   smallest undecided instance. Known and Open are not end points.
7. Before calling anything new, search the literature and say what you searched. Never invent a reference.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority. This task is long by design. Work through all parts completely; do not stop at an outline, a
sample or a plan, and do not ask whether to continue. Write the files from the start and extend them as you go.
