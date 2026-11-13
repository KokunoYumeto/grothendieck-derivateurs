# TOTAL_EXACT_2: does total asphericity imply exactness of abelian colimits?

To be settled: whether a small category all of whose categories of elements have contractible components has an
exact colimit functor on diagrams of abelian groups. Either answer fixes the correct form of Grothendieck's
statement at II ms. 36ter.

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for the deliverables: `TOTEX2`.
Drafted on 12 Nov 2026 by Claude Fable 5.2 (effort max), Dérivateurs expert, from the return TOTEX (GPT-6 Astra,
ChatGPT Pro mode, 12 Nov 2026; 58 statements) and its review by Claude Opus 5.5 (effort max, 12 Nov 2026; none of
the 58 found wrong; the main question not decided). Follow-up to the prompt TOTAL_EXACT.

## What is attached

One file, `TOTAL_EXACT_2_background.zip`; `MANIFEST.tsv` at its root lists every file with its origin.
- `TOTEX_return/`: the return TOTEX (paper as TeX and PDF, results table, report, bibliography, `code/` with every
  program and output). Its statements are cited below by their numbers, A.1 to F.5.
- `TOTEX_REVIEW.md`: the review, statement by statement, with its section 6 "The state of Part A";
  `TOTEX_review_code/`: the reviewer's own programs and outputs (the Adámek–Koubek–Reiterman stages rebuilt from
  the paper's formulas, the homology of the down-sets, the search for triple equalizers at every computed stage).
- `TOTAL_EXACT_PROMPT.md`: the prompt that TOTEX answered.
- `papers/`: Isbell–Mitchell, *Exact colimits*, Bull. AMS 79 (1973); Isbell–Mitchell, *Exact colimits and fixed
  points*, Trans. AMS 220 (1976) (TOTEX could not obtain it; the reviewer read it in full); Adámek–Koubek–Reiterman,
  Czech. Math. J. 31 (1981) (a scan without text layer).
- `TOTASPH/`: sections C and D of the earlier return TOTASPH (the proofs behind R1, R2, R4, R5), its results table
  and its review. `PRETOT/`: paper (TeX) and results table of the return PRESHEAF_TOTALITY (Definition E.1 of `Ty`;
  F.3, F.6, F.12) with its review and findings.
- `HUNCHES.md` (the expert's H1, where the class `κ` of Lead 5 comes from); `ty_check.py`, `ty_check.out` (the
  enumeration behind Lead 8).
- `DER_II-a.tex` (II ms. 1–53), `DER_XIIb-a.tex` (XII ms. 59–122), `DER_VII-a.tex` (VII ms. 1–57): Grothendieck's
  text, the French transcription corrected on 11 Nov 2026, AI-made from the edition of Künzer, Malgoire and
  Maltsiniotis; manuscript pages are marked `\msp{page N}`. The edition is the authority; where a formula looks
  wrong, say so and reason from the mathematics.

Not attached, and opened by nobody on our side: Oberst, Math. Z. 107 (1968) 87–115; Gabriel–Ulmer, LNM 221 (1971);
Isbell, Canad. Math. Bull. 11 (1968) 569–572; Isbell, Ann. of Math. 100 (1974) 633–637. Adámek–Reiterman, Trans.
AMS 211 (1975) 239–247, is open access at ams.org.

## Where this comes from

Grothendieck (II ms. 36–36ter; XII ms. 88–89, Définition 1) calls a small category `A` *totalement
`W∞`-asphérique* when every category receiving a final functor from `A` is aspherical, and conjectures at II
ms. 36ter that such a category is filtered. That is false (`Δ_inj`: Isbell–Mitchell 1973). What is established is
`{filtered} ⊊ {exact} ⊂ {total} ⊂ {quasi-filtered}`, and the two outer classes of the last three differ
(Adámek–Koubek–Reiterman 1981). In 1976 Isbell and Mitchell asked (p. 298) for "a category with the fixed point
property whose affinization is not filtered"; the question of this prompt is theirs with total asphericity in place
of the fixed point property. TOTEX left it undecided.

## Results this prompt builds on (status on 12 Nov 2026)

**Notation and conventions used from here on (keep them).**

- Categories are small. `BA = |NA|`. `W∞`: functors whose nerve is a weak homotopy equivalence. For `u: A → B`,
  `b\A` has objects `(a, b → u(a))`; `u` is *final* when every `b\A` is non-empty and connected.
- An *`A`-set* is a functor `H: A → Set` (covariant); `El_A(H)` has objects `(a, h)`, `h ∈ H(a)`, and arrows
  `f: (a, h) → (a', h')` with `H(f)h = h'`. The manuscript uses presheaves; translate the variance at each place.
- *Total* means: `A` is non-empty, connected, and every component of every `El_A(H)` is weakly contractible (R1).
  *Exact* means: `colim_A: Ab^A → Ab` is exact.
- `P_x = Z[A(x, −)]`; `ΔZ` is the constant right `ZA`-module; `T_i(F) = Tor_i^{ZA}(ΔZ, F) = L_i colim_A F` for
  `F: A → Ab`; `F` is *colim-acyclic* when `T_i(F) = 0` for all `i > 0`. `aug` sums coefficients. For a subfunctor
  `K ⊂ P_q`, `ε(K) ⊂ Z` is the image of `colim_A K → colim_A P_q = Z` (elements at different objects may have to be
  combined). An *affine arrow* `x → y` is an element of `Z[A(x, y)]` with `aug = 1`; they form `Aff_Z(A)`. An
  *affine equalizer* of `a_0, …, a_k: p → q` is an affine `t: q → r` with `ta_i = ta_0` for all `i`.
- Conditions of Isbell–Mitchell 1976, §2, for an `A`-set `X` (and for `A`, meaning all representables): I (any two
  elements `x ∈ X(c)`, `x' ∈ X(c')` have arrows with `βx = β'x'`; for `A`: every span completes to a commutative
  square); II (every pair in `X(c)` is equalized by an arrow); III (every finite family in `X(c)` by an affine
  arrow); IV (every pair by an affine arrow); V (the necklace form of IV). *Quasi-filtered*: I and IV.
- A *separator* is a total category that is not exact, with a finite family of parallel arrows that has no affine
  equalizer.

**The results.** None of these is to be proved again as if open. For each one you use: read the proof at the
place given and confirm the step you rely on in a paragraph of your own, or give the exact error with a repair or a
counterexample. "Checked" means: by the review of Claude Opus 5.5 (effort max), which followed the proof in full
unless said otherwise.

- **R1 (TOTASPH C.5; TOTEX A.1; checked).** For `A` non-empty and connected the following are equivalent: every
  category receiving a final functor from `A` is aspherical; every component of every `El_A(H)` is weakly
  contractible; every such component is integrally acyclic; `hocolim_A X → colim_A X` is a weak equivalence for
  every `X: A → sSet`. Hence `Z[H]` is colim-acyclic for every `A`-set `H`, and so are `R[H]` for a commutative
  ring `R`, direct sums, summands and filtered colimits of such functors (TOTEX D.13). Standard: colim-acyclic
  functors are closed under extensions and kernels of epimorphisms. (The presheaf example PRETOT A.5 concerns
  restricted actions and does not bear on categories: TOTEX A.6.)
- **R2 (known: Isbell–Mitchell 1973, Th. 1, Lemma 1; 1976, Th. 3.1, Prop. 3.3; TOTASPH C.6; TOTEX A.2).** For `A`
  non-empty connected: exact ⟺ `ΔZ` is flat ⟺ `Aff_Z(A)` is filtered ⟺ I and III ⟺ I and every pair of affine
  arrows has an affine equalizer. Exact ⟹ total. For a commutative ring `R ≠ 0` the same holds with `Aff_R` and
  `(R-Mod)^A` (Isbell–Mitchell 1976, Remark p. 296; this is TOTEX D.14, proved there without the citation because
  the paper was not obtained).
- **R3 (known: Isbell–Mitchell 1973, Th. 3, with the proof in Isbell 1974, opened by nobody here; TOTASPH C.9–C.10;
  TOTEX A.3, E.1–E.6, checked).** `Δ_inj` (non-empty finite ordinals, increasing injections) and the coloured-word
  categories `W_m` (finite words in `m` letters, strictly increasing colour-preserving maps; TOTEX E.1) are exact,
  hence total, and are neither filtered nor sifted; `W_2, W_3, W_4` are pairwise inequivalent and are not final
  images of `Δ_inj^r × I`, `I` filtered (TOTEX E.5, new).
- **R4 (TOTASPH C.11; Adámek–Koubek–Reiterman 1981, Theorem [1]; Isbell–Mitchell 1976, Lemmas 2.1, 2.2, Prop. 2.3;
  TOTEX A.4, B.5, B.6; checked).** Total ⟹ quasi-filtered. With I and IV for `A`, every connected `A`-set satisfies
  I and IV: two elements `x, x' ∈ X(q)` of a connected `X` have an affine `t` with `tx = tx'` in `Z[X]`. In a
  quasi-filtered category every component of every `El_A(H)` is simply connected. So the first condition of
  totality beyond quasi-filteredness is `H_2(El_A(H)) = 0`.
- **R5 (known: Isbell–Mitchell 1976, Th. 4.1, Cor. 4.3, Cor. 4.4, Prop. 4.5, Cor. 4.6).** Under I and IV: a
  category with a weakly terminal object is filtered (Cor. 4.4; this is TOTASPH C.13 = TOTEX A.5, which both
  returns label "Proved" without the citation; Th. 4.1 is the minimal-period argument of TOTASPH C.13); every finite
  family of endomorphisms of an object is equalized by an arrow, and if `A(q, p) ≠ ∅` every finite family in
  `A(p, q)` is equalized by an arrow (Cor. 4.3); if `sup_X |A(p, X)| < ∞`, every finite family of parallel arrows
  out of `p` is equalized by an arrow (Prop. 4.5, due to Adámek–Reiterman). **So no finite category, no monoid and
  no category with a weakly terminal object is a separator; do not search there.**
- **R6 (TOTEX D.4 = PRETOT F.3; TOTEX D.5 = PRETOT F.6, which TOTEX does not credit; TOTEX D.7, D.9, D.10, new; all
  checked).** A sifted total category is filtered (the criterion for siftedness is Gabriel–Ulmer's and Lair's,
  quoted from Adámek–Rosický–Vitale 2010, Remark 1.1). A total category in which `hocolim_A K(M(a), n)` is
  `n`-truncated for all `M: A → Ab` and one `n ≥ 1` is filtered. For `n ≥ 1`, homotopy colimits over `A` preserve
  `n`-types iff every comma category `a ↓ (A → ΠA)` of the groupoid completion is filtered. So a separator is not
  sifted and preserves no positive truncation level.
- **R7 (TOTEX B.1–B.4; checked).** For `a_0, a_1, a_2: p → q` put `z_i = a_i − a_0`,
  `K_i = {t ∈ P_q : tz_i = 0}`, `K = {(t_1, t_2) ∈ P_q² : t_1z_1 + t_2z_2 = 0}`,
  `H_3 = A(p, −)/(ca_0 ∼ ca_1 ∼ ca_2)`. With common successors, the triple has an affine equalizer iff
  `ε(K_1 ∩ K_2) = Z`, and `T_1(P_q/(K_1 + K_2))` maps onto `(ε(K_1) ∩ ε(K_2))/ε(K_1 ∩ K_2)`. Further
  (with `ε²: colim K → Z²` the two augmentations) `H_1(El H_3) = Z²/ε²(colim K)`, `H_2(El H_3) = ker(colim K →
  Z²)`, `H_j(El H_3) = T_{j−2}(K)` for `j ≥ 3`, and the
  analogous formulas for any finite graph of relations `ca_v ∼ ca_w`. For total `A` therefore `colim K ≅ Z²`,
  `T_i(K) = 0`, and (review, 6.2) `colim K_i ≅ Z`, `T_i(K_i) = 0` (`i ≥ 1`). `K` is a kernel in `P_q²`; it is not
  `K_1 ∩ K_2`.
- **R8 (TOTEX D.12, D.15, D.17–D.19; checked).** `π_i hocolim_A HM = T_i(M)`; for total `A` and one `n ≥ 2`,
  `H_{n+1}(hocolim_A K(M, n); Z) = T_1(M)`; `T_i(F) = π_i(LG_F)` for the presheaf of sets
  `G_F(Z^n) = colim^{Set}_A (UF)^n` and `L` the reflection to animated abelian groups; a rational affine equalizer
  is an integral simultaneous annihilator of non-zero augmentation, and an `F_p`-affine equalizer is an integral
  `t` with `t(a_i − a_0) ∈ pZ[A(p, r)]` and `aug t ≢ 0 mod p`. These are reformulations: none of them decided the
  question.
- **R9 (TOTEX D.21–D.26; checked, followed and not recomputed).** Total and exact are each preserved by final
  images, finite products, opfibrations with total (exact) base and fibres, passage to components of categories of
  elements, non-empty full cosieves, localization, idempotent completion, and filtered colimits along final
  functors. So none of these operations produces a separator from exact categories.
- **R10 (Adámek–Koubek–Reiterman 1981, Constructions B.5–B.9, C.1, Theorem C.2; TOTEX C.1–C.5, checked and
  recomputed by independent code; reviewer's computation F11).** The category `K*` (objects finite sets, arrows
  injections; `K_0 = (V ⇶ W)`, `V` one point, `W` three points, `v_1, v_2, v_3` the three points; then, stage by
  stage, a fresh quasi-filter target for each ordered parallel pair and a disjoint sum for each ordered pair of
  objects) is quasi-filtered, and `v_1, v_2, v_3` have no affine equalizer, even rationally (any `r` distinct maps
  `W → X` cover more than `3r/2` points, while an equalizer supported on `r` maps forces at most `3r/2`). The
  source has two sign misprints in Lemma B.5 (c), (d), a wrong summand in B.6, and a false claim that (9)–(11)
  survive domain–range restriction ((11) fails on a two-point path); TOTEX Proposition C.1 repairs the
  construction (each path with its actual number of vertices, one common `k`) and Theorem C.2 is not affected. For
  the repaired first stage (17 objects, 1,263 arrows; `s = 45`, `k = 11`, `n = 3`, `a_0 = 2`, `a_1 = 8/5`):
  `H_*(El(h_V/(cv_1 ∼ cv_2))) = (Z, 0, Z)` and `H_*(El(h_V/(cv_1 ∼ cv_2 ∼ cv_3))) = (Z, 0, Z⁴)`; the first `H_2`
  class injects into `H_2` of every second stage (C.3) and survives one selected second-stage and one selected
  third-stage attachment (C.4). In the variant with the literal common-`n` maps (it violates (11) and is a valid
  instance of the general construction B.9 only) a selected attachment kills a class: `Z³ → Z²` with kernel `Z`.
  The cone-attachment sequence (C.5): adjoining new maximal objects attaches a cone on each old comma link `L_h`,
  with `⊕H_2(L_h) → H_2(E_old) → H_2(E_new) → ⊕H_1(L_h) → H_1(E_old)` exact. Reviewer (F11): at no object of any
  computed stage, repaired or literal, do `v_1, v_2, v_3` have an affine equalizer over `Q`, `F_2` or `F_3`. **Not
  settled:** whether `K*` is total (TOTEX C.6). The reviewer read the proof of Theorem C.2 only up to the start of
  its induction on (c_m), (d_m).
- **R11 (corrections of the review to TOTEX, besides the credits in R2, R5, R6).** (i) The proof for `Δ_inj` is
  Isbell 1974; TOTEX cites only the 1973 announcement. (ii) TOTEX D.3 is the check of the expert's note and of
  PRETOT F.4. (iii) TOTEX C.7 (adjoining a terminal object gives a filtered category) is trivial and does not
  answer the item it was filed under (the smallest change of `K*` that makes it total, and whether the triple then
  acquires an equalizer): that item was not addressed. (iv) The triple is the smallest instance left open, but the
  main question does not reduce to triples: after equalizing `a_0, a_1, a_2` by an affine `t`, the next step is to
  equalize the affine pair `(ta_0, ta_3)`. (v) TOTEX does not use the class `κ` of the expert's H1 (Lead 5).
  (vi) Sources still unopened: Oberst 1968 and Gabriel–Ulmer 1971 (needed before any statement of novelty for
  TOTEX D.7, D.9–D.10, E.2–E.6), Isbell 1968, Isbell 1974.

## Leads

Each is an inference of the model named, checked by nobody else; each is to be proved or refuted in full. Expected
answer for every one of them: true.

- **Lead 1 (Claude Opus 5.5, review F2; derived a second way by the drafter).** For total `A` the surjection of R7
  is an isomorphism `T_1(P_q/(K_1 + K_2)) ≅ Z/ε(K_1 ∩ K_2)`. Second derivation: with `J_i = P_q z_i ⊂ P_p` and
  `D = {(tz_1, tz_2) : t ∈ P_q}`, one has `P_q/(K_1 + K_2) ≅ (J_1 ⊕ J_2)/D`, `D ≅ P_q/(K_1 ∩ K_2)`, and
  `J_i = ker(P_p → Z[A(p, −)/(ca_0 ∼ ca_i)])` is colim-acyclic with `colim J_i = 0`.
- **Lead 2 (Claude Opus 5.5, review F4).** For `A` satisfying I: `A` is exact iff for all `p, r` every
  `z ∈ Z[A(p, r)]` with `aug z = 0` has an affine left annihilator; and `T_1(P_p/P_r z) ≅ Z/ε(ann z)`. Totality
  gives the binomials `z = c − c'`. A proof for all triples does not formally give quadruples (R11 (iv)).
- **Lead 3 (drafter).** For every small category `A` (no hypothesis) and every family `a_0, …, a_k: p → q` let
  `d^T: P_q → P_p^k`, `t ↦ (t(a_i − a_0))_i`, `Q_a = coker d^T`, `L = ker d^T = K_1 ∩ … ∩ K_k`. Then
  `T_1(Q_a) ≅ Z/ε(L)`, `T_2(Q_a) ≅ ker(colim L → Z)`, `T_i(Q_a) ≅ T_{i−2}(L)` for `i ≥ 3`; with common successors
  the family has an affine equalizer iff `T_1(Q_a) = 0`. The permutation module `Z[A(p, −)/(ca_0 ∼ … ∼ ca_k)]` is the
  cokernel of the transposed map `d: P_q^k → P_p`. So totality says that the cokernel of the row `(z_1, …, z_k)`
  is colim-acyclic, and exactness asks the same for the cokernel of the column; for `k = 1` they are the same
  module. `Q_a` is the module with generators `x_1, …, x_k` at `p` and the single relation `Σ_i (a_i − a_0)x_i = 0`
  at `q`.
- **Lead 4 (drafter, from Isbell–Mitchell 1976, Prop. 2.3).** In a quasi-filtered category: for every `M: A → Ab`
  and `α, β ∈ M(q)` with the same class in `colim^{Set}_A UM` there is an affine `t: q → s` with `tα = tβ` in
  `M(s)`. And `A` is exact iff the same holds for all `α, β ∈ M(q)` with the same class in `colim^{Ab}_A M` (the
  case `M = P_p`, `α, β` affine arrows, is condition II for `Aff_Z(A)`). So for total `A` the content of the main
  question is the fibres of `colim^{Set}_A UM → colim^{Ab}_A M`, that is, the failure of `colim^{Set}_A` to commute
  with finite products.
- **Lead 5 (drafter; the class is the expert's, `HUNCHES.md` H1).** Let `ρ_1, ρ_2, ρ_3 ∈ P_q(s)` be affine
  equalizers of `(a_0, a_1)`, `(a_0, a_2)`, `(a_1, a_2)` and `κ = (ρ_1 − ρ_3, ρ_3 − ρ_2)`. (i) `κ ∈ K(s)` and
  `ε²(κ) = 0`, so for total `A` the class of `κ` in `colim K` is zero. (ii) In a connected category satisfying I, an
  element
  `κ ∈ F(s)` of a functor `F: A → Ab` has class zero in `colim_A F` iff there are an arrow `u: s → y`, finitely
  many pairs of parallel arrows `e_j, e'_j: x_j ⇉ y` and elements `k_j ∈ F(x_j)` with
  `uκ = Σ_j (e_j − e'_j)k_j`. (iii) If `tκ = 0` for an affine `t`, then `tρ_1 = tρ_2 = tρ_3` is an affine
  equalizer of the triple; this happens when the pairs `(e_j, e'_j)` of (ii) have a common affine equalizer, in
  particular when one term is enough. (iv) With `K_3 = {t : t(a_2 − a_1) = 0}` and
  `ψ: K_1 ⊕ K_2 ⊕ K_3 → K`, `ψ(k_1, k_2, k_3) = (k_1 − k_3, k_2 + k_3)`: `ker ψ ≅ K_1 ∩ K_2`, and for total `A`,
  `T_1(K/im ψ) ≅ Z/ε(K_1 ∩ K_2)`. Here `K(x)` is the cycle space of the bipartite graph on `A(q, x) ⊔ A(p, x)` with
  an edge from `g` to `ga_i` for each `g` and `i`, and `im ψ` is the sum of the cycle spaces of its three subgraphs
  with two of the three kinds of edges. So in a separator the null-homology of `κ` passes through cycles that mix
  the three kinds of edges, carried around a 1-cycle of `A`.
- **Lead 6 (drafter).** A finite test. For a functor `u: D → A` let `H_u(a) = π_0(u ↓ a)` (objects of `u ↓ a`:
  `(d, u(d) → a)`) and `j_u: D → El_A(H_u)`, `d ↦ (u(d), [d, id])` (the comprehensive factorization of `u`). A
  non-empty connected `A` is total iff `Bj_u` is null-homotopic on each component for every finite poset `D` and
  every `u`; it is enough to take for `D` the face posets of triangulated spheres. (Any `v: D → El_A(H)` factors
  through `j_{πv}`.)
- **Lead 7 (drafter; its use for `K*` is the "link lemma" of the review, F14).** Let `A'` be `A` with one new object
  `Z`, `A'(−, Z) = R` a presheaf on `A`, `A'(Z, Z) = {1}`, no arrows from `Z` to old objects. For `H': A' → Set`
  and `h ∈ H'(Z)` the comma link `L_h` is a union of components of the two-sided category of elements
  `El(R, H'|A)` (objects `(x, r ∈ R(x), k ∈ H'(x))`). If `R = colim_{d ∈ D̃} A(−, ũ(d))` for a functor `ũ: D̃ → A`
  such that every component of every comma category `x ↓ ũ` is weakly contractible, then `El_{D̃}(ũ^*H') →
  El(R, H'|A)` is a weak equivalence; so every link has the homology of a category of dimension at most
  `dim N(D̃)`, and `H_j(El_A(H'|A)) → H_j(El_{A'}(H'))` is injective for `j > dim N(D̃)`. Consequence: cones over
  diagrams of dimension 1 (quasi-filters) and of dimension 0 (sums) never kill a class of degree 2. The hypothesis
  fails for the quasi-filter of a pair `f, g: T → S` at an object `x` with an arrow `c: x → T` such that `fc = gc`
  (the component is a circle); this occurs in `K_2` (the pair `α_0, α_{4k}` of a first-stage quasi-filter and
  `c = v_1`), and those links have to be treated by the cover by the slices over `(S, h_i)` and (9)–(11).
- **Lead 8 (drafter; `ty_check.py`).** `Ty^op` is not total and not exact. In Grothendieck's category `Ty` of
  interval types (VII ms. 25–32; PRETOT E.1), `Ty(τ, ρ)` is the set of weakly increasing sign-preserving maps from
  the letters of `ρ` to the letters of `τ`; so `Ty^op` is the category of finite words in `+, −` with these maps,
  and `W_2` is its subcategory of injective maps. The two arrows `e = (1, 3)` and `c = (1, 1)` from `(++)` to
  `(+−+)` in `Ty^op` have no completion to a commutative square and no affine equalizer over any ring (for
  `g: (+−+) → σ`, `g(1) < g(2) < g(3)`, so `ge` is injective and `gc` is constant). So `Ty^op` fails I and IV, and
  the candidate "`Ty^op`" of the review (section 6.4) is closed.
- **Lead 9 (Claude Opus 5.5, review F5, F6; (d) drafter).** Let `A` be a separator and `a_0, …, a_k: p → q` a
  family without affine equalizer, with `k` the least number for which `A` has such a family. Then: (a) `A(q, p) = ∅`
  (R5);
  (b) `sup_X |A(p, X)| = ∞` (R5); (c) the full cosieve of objects receiving an arrow from `p` is again a separator,
  so `p` may be taken weakly initial (R9); (d) for every arrow `g: q → x` the arrows `ga_0, …, ga_k` are pairwise
  distinct.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (objects, arrows, composition, the verification of every hypothesis and of the
failure; checked by a program when finite or finitely presented) and the strongest true statement proved in its
place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the
obstruction as an exact statement and the smallest undecided instance are the state of an item you are still
working on: record them as you go, then attack the obstruction, starting from that instance. "Known" counts only
with the derivation of the statement used here from the cited theorem, after opening the source.

For the main question in particular. A proof must hold for every total `A`. A refutation is one category given
completely, with a proof that every component of every `El_A(H)` is weakly contractible for **all** `H: A → Set`,
and a named finite family with a proof that it has no affine equalizer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1–R11 again in place of
the items; a proof of the main implication that at any step replaces a permutation module `Z[H]` by an arbitrary
functor to `Ab` without proof, or that uses siftedness, a weakly terminal object, bounded hom-sets or an arrow
`q → p` without naming the hypothesis; a proof for triples presented as a proof for all finite families; a claimed
separator whose total asphericity is verified only on finitely many `H`, only in homology of low degree, or only on
finite stages of an infinite construction; a statement about `K*` proved only for selected attachments; a step that
replaces a claim by a convenient special case without naming it.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `TOTEX2_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The main question.**
1. Prove or refute: every small non-empty connected category `A` in which every component of every `El_A(H)`,
   `H: A → Set`, is weakly contractible satisfies III, that is, every finite family of parallel arrows
   `a_0, …, a_k: p → q` has an affine equalizer. (By R2 this is exactness of `colim_A` on `Ab^A`; by R1 the
   hypothesis is total `W∞`-asphericity.)
2. Prove or refute the same implication with coefficients: for `R = Q`, and for `R = F_p` for each prime `p`, a
   total `A` has exact colimits on `(R-Mod)^A`. (If A.1 is proved, this follows from TOTEX D.12.)

We have no expectation that we trust. The expert's hunch H1 was that the implication holds: every known total
category that is not filtered is exact, and every known proof of totality passes through exactness. The drafter of
this prompt expects a separator: Lead 6 turns totality into a list of filling tasks which a construction can serve
one at a time, as Adámek, Koubek and Reiterman did for pairs, and F11 of the review shows attachments that kill
`H_2` classes without creating an equalizer of the triple. Neither is evidence.

Approaches to A.1. These are not items; they are the routes known to us, in the order we would take them. Record
the state of each one you try.
- *Proof side.* (P1) Show `T_1(Q_a) = 0` for the module `Q_a` of Lead 3 by placing `Q_a`, or a module with the
  same `T_1`, in the smallest class that contains the permutation modules and is closed under extensions, kernels of
  epimorphisms, direct sums, summands, filtered colimits and `− ⊗ Z[H]`; every member of that class is colim-acyclic
  over every total category. Totality of `A × A`, of the components of `El_A(H_3)` and of iterated categories of
  elements, of cosieves, localizations and idempotent completions supplies further permutation modules (R9).
  (P2) The one-relator form (Lead 2), first for `z = 2c_0 − c_1 − c_2`, then by induction on the support of `z`.
  (P3) The class `κ` (Lead 5): from the relation `uκ = Σ_j (e_j − e'_j)k_j` produce an affine `t` with `tκ = 0`, or
  an element of `K_1 ∩ K_2` of augmentation 1 by another route; or read off from the relations what a separator
  must look like. (P4) Dual certificates (review, 6.5): there is no rational equalizer of the triple at `r` iff
  there are functions `φ_1, φ_2` from `A(p, r)` to the rationals with `φ_1(ca_1) − φ_1(ca_0) + φ_2(ca_2) −
  φ_2(ca_0) = 1` for all `c: q → r`;
  such potentials pull back along arrows, and a compatible family on all of `p\A` is impossible; show that
  totality forces a compatible family. (P5) The stable forms of R8 and Lead 4: `T_i(M)` is the stable homotopy of
  the `Γ`-set `n ↦ colim^{Set}_A (UM)^n`.
- *Counterexample side.* (C1) Settle `K*` first (Part C.1): it fixes the calculus of links. (C2) Build a
  separator by attaching cones. By Lead 6 the tasks are the finite spheres `u: D → A` with `Bj_u` not
  null-homotopic; by Lead 7 a class of degree `n` can only be killed by a cone over a diagram of dimension at least
  `n`, or over one whose strict colimit of representables is not its homotopy colimit. A "higher quasi-filter" for
  `u` is a new object with a cocone over `ũ: D̃ → A`, where `D̃ → El_A(H_u)` carries a class mapping to the class of
  the sphere and no cocone over `D` itself is created. The invariant to keep is a private incidence: if for every
  object `x` every non-empty finite set `S` of arrows `q → x` has an arrow `c: p → x` equal to `ga_i` for exactly
  one `(g, i) ∈ S × {0, …, k}`, then the family has no affine equalizer over any non-zero ring (the coefficient of
  `g` would vanish); the bound of R10 is the case `k = 2` by counting. By Lead 5 (iii) the class `κ` must die
  without being annihilated by one affine arrow. Two fillings related by an arrow create no new class: if
  `(α_i: S → Z)` and `(α'_i: S → Z')` are quasi-filters of one pair and `θ: Z → Z'` has `θα_i = α'_i`, their two
  discs are homologous. (C3) The general construction B.9: the literal attachments kill classes and keep the
  triple unequalized at the computed stages; decide what remains of the inequalities (c_m), (d_m) there. (C4) Homogeneous
  candidates: the categories of embeddings of amalgamation classes of rigid finite structures (finite linearly
  ordered graphs with order-preserving induced embeddings; ordered triangle-free graphs; other Ramsey classes).
  They satisfy I by amalgamation, all arrows are monic, there is no weakly terminal object, and hom-sets are
  unbounded. For ordered graphs the two edges of the induced path `x < y < z` have an affine equalizer made of two
  induced increasing paths with 5 and 4 edges and the same end edges (one hand computation of the drafter; nothing
  else is known to us about these categories). (C5) By R5 a finite computation can only be a piece of an infinite
  construction; every candidate has to pass Lead 9.

**B. Triples.**
1. Prove or refute: in every total category every triple of parallel arrows has an affine equalizer;
   equivalently (Lead 3) `T_1(coker(P_q → P_p ⊕ P_p, t ↦ (t(a_1 − a_0), t(a_2 − a_0)))) = 0`. This is the open
   statement B.7 of TOTEX. It is decided by A.1 except when A.1 is refuted only by larger families; then decide it.
2. Prove or refute each of Leads 1 to 5, in full.

**C. The Adámek–Koubek–Reiterman category and the tools for a separator.**
1. Prove or refute: for the repaired Construction C.1 (TOTEX Proposition C.1), for every admissible choice of
   the sequence `(a_m)` and of the targets, `K*` is not total; precisely, `H_2(El_{K*}(h_V/(cv_1 ∼ cv_2))) ≠ 0`.
   Expected: true, by
   showing that every link of every new object has vanishing `H_2` (Lead 7 where its hypothesis holds, the cover by
   slices and (9)–(11) elsewhere), so that the class of R10 never dies. If instead `K*` is total for some choice,
   it is a separator: then check the proof of Theorem C.2 in full, and A.1 is refuted. This closes TOTEX C.6.
2. Prove or refute each of Leads 6 to 9, in full.

**D. Statement of results.**
1. The diagram of classes of non-empty connected small categories, `{filtered} ⊊ {exact} ⊂ {total} ⊂
   {quasi-filtered}`, with each of the two right-hand inclusions decided: an equality with its proof, or strict
   with its example.
2. The corrected statements for II ms. 36–36ter and XII ms. 88–89 that follow, with what TOTEX already proved
   (R6) and the manuscript readings it corrected (II ms. 36: `y\X` for the printed `y\Y`; XII ms. 88: `U'/H'`).
3. The literature record: for Isbell–Mitchell 1973 and 1976, Isbell 1968 and 1974, Oberst 1968, Adámek–Reiterman
   1975, Adámek–Koubek–Reiterman 1981, Husainov 2002, Gabriel–Ulmer 1971, and the literature on flatness
   properties of acts over monoids (the one-element act), one line each: opened, with the numbers of the theorems
   that contain or come closest to each statement you prove; or not obtained, with what you tried. Say nothing
   about the content of a source you did not open. Say what you searched for the main question itself.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: quantifiers, size conditions, variance, which coefficients, which
   numbered condition in which version. Do not replace it by a convenient special case. If you prove a special
   case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property
   you use (natural in which variable, linear, a map of `A`-sets or only of modules). Compositions must
   type-check; an element of a colimit is a finite sum of classes of elements at possibly different objects.
3. Every reduction ("we may assume", "replace by") comes with its comparison map and a proof that the exact
   property needed transfers in the direction needed. Passing to a nerve, a cosieve, a component, a stage of a
   union, a field of coefficients or a homotopy category transfers nothing by itself.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories; weak equivalence of
   a specified map; an isomorphism on homology. An abstract isomorphism is not the canonical map.
5. Check the edge cases in scope: empty categories, several components, `A`-sets on which arrows act
   non-injectively, categories with idempotents or endomorphisms, arrows `q → p`, infinite families.
6. A counterexample is given completely and, when finite or finitely presented, checked by a program whose code
   and output you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone
   shows a gap, not falsity; keep the two apart.
7. No authority. Grothendieck's assertions, the returns TOTASPH, PRETOT and TOTEX, their reviews, the results R1–R11
   and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full. If one is
   wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails,
   and you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

## What to deliver

One ZIP containing:
- `TOTEX2_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Refuted / Known (with citation), with complete proofs; English, first
  person plural; quote Grothendieck in French where his wording matters.
- `TOTEX2_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `TOTEX2_references.bib`: each entry marked opened / not opened.
- `TOTEX2_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted,
  with the statement number); then what you read, what you computed, every correction to R1–R11, to the Leads, to
  the reviews and to the transcription.
- `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

If the execution environment disconnects: wait and retry for ten minutes; then write every file out in the chat in full, each in its own code block, and continue the remaining parts in the chat until every part is written.

**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `<ID>_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
