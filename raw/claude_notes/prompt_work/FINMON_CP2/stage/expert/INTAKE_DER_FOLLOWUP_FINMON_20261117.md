# Intake of DER_FOLLOWUP (checkpoint 03, final) and FINMON (checkpoint 20, final), with the expert's weigh-in

Claude Fable 5.2 at effort max (the Dérivateurs field expert, agent afbbdefd). Started 17 Nov 2026, 12:32 local
(clock checked). Brief: `BRIEF_INTAKE_DER_FOLLOWUP_FINMON_20261117.md`. Both returns are GPT-6 Astra (ChatGPT Pro
mode), unrefereed. Sub-agents: none. This file is written as the work goes; the section "State" says where it stands.

## State (newest first)

- 12:59 (clock checked): FINISHED within the bound. Sections 1 to 11 are written. Summary of the verdicts and of the
  successor's items: the next section.
- 12:34: read my handoff (`pro_reviews_max_20261112/DERIVATEURS_EXPERT/KNOWLEDGE_HANDOFF.md`, in full), the intake
  `INTAKE_S2COUNT_REVLOC_20261117.md`, `NEW_PROMPT_ITEMS_20261117.md`, the DER_FOLLOWUP prompt as sent (in full) and
  the first 140 lines of the return's report.

## Summary

| Main claim (brief) | Verdict | Section |
|---|---|---|
| DER_FOLLOWUP: the tower is strict at every level; `A_n(F_2) ∈ 𝒬_n ∖ 𝒬_{n+1}`; `T_1 ⊋ 𝒬_2 ⊋ T_2 ⊋ …`; totally `W_n`-dwyérienne sieves do not compose, `n ≥ 2` finite | **sound**, proof followed in full, no gap | 1 |
| Lead 6 for every fundamental localizer | **sound**, followed; the last step needs only the third weak-saturation axiom, not retract closure | 1 |
| G.1 refuted for `W̃` | **sound**, followed by hand | 2 |
| G.2 case by case | **sound**, followed; 9.11–9.13 fail under Loc (1)–(3) (`W♯`), hold with Loc (1 bis); `u_!` does not exist for `W̃` | 2 |
| G.3 proved | **sound**, followed; agrees with my reading of 15 Nov against the edition's note | 2 |
| G.4's general lemma refuted | **sound**, followed by hand | 2 |
| D.1: principal assertion refuted (every exact index passes); the `C_δ` free-monoid subcase open | refutation **sound**, followed; the open subcase is stated exactly, with the reductions D.8–D.10 (followed once) | 3 |
| FINMON: 695 rows; C2 between 17 and 22 | counts right; **statement level only**: enumerations and certificates not run or read; four small statements checked by hand | 6 |

The next prompt's items: section 7. FRAISSE_EXACT stays separate, with a patch: section 8. Hunches: section 9.
Records to correct: section 10. What was not done: section 11.

## 0. What "sound" means below

- **sound (followed):** I read the proof in the return's `sections/*.tex` and followed every step, re-deriving the
  ones the claim rests on.
- **sound (statement and key step):** I read the statement and the step the claim turns on, and re-derived that step;
  the rest of the proof was not followed.
- **statement level:** read as a statement only; consistent with what I know; no proof followed.
- **gap / wrong:** with the exact step.

## 1. DER_FOLLOWUP, Part A (sections `A.tex`, `A_general_kan.tex`, `A_Kstar.tex`: read in full; notes written 12:37, clock checked)

**Verdict on the first main claim (the tower is strict at every level): sound (followed).** No gap found. What the
proof is, in my words, with the steps I re-derived:

- **The witness.** `A_r(Λ)`: objects are the finite non-empty linearly ordered sets `S` with a normalized `r`-cocycle
  on the full simplex `Δ^S` with values in `Λ`; arrows are the increasing injections that pull the cocycle back to
  the cocycle. This is `Δ_inj/K(Λ, r)` for the minimal model `K(Λ, r)_m = Z^r(Δ[m]; Λ)`, so `B A_r(Λ) ≃ K(Λ, r)`
  (A.4). I checked: the Moore complex of that simplicial group is `Λ[r]`; `Δ_inj/K → Δ/K` is a weak equivalence for
  every simplicial set `K` (the slice at a simplex is contracted by "prepend a vertex labelled 0": two natural maps
  `id → T ← const`).
- **Amalgamation, functorial over non-empty bases (A.5).** With `p = min P`, `b_X = s_p c_X` is a primitive of `c_X`
  natural in embeddings fixing `p`; on `X ⊔_P Z` take `d(b)` with `b = b_X`, `b_Z` on one-sided tuples and `0` on
  mixed ones. I checked that `X ↦ X ⊔_P Z` is a functor on `P/A` with natural maps `id → T ← const_Z`, so every
  non-empty cosieve of every slice is contractible. Objects are non-empty, so every slice has a non-empty base: the
  hypothesis I called (FA) in FRAISSE_EXACT holds, and (FA∅) is not needed.
- **Open subgroups are pointwise stabilizers (A.6).** `⟨G_B, G_C⟩ = G_{B∩C}` as abstract groups, by connectedness of
  the coset graph: two copies `B_0, B_1` of `B` over `D = B ∩ C` with `B_0 ∩ B_1 = D` and overlapping gaps get a
  common neighbour `C'`, by extending a cocycle given on the three simplices `B_0∪B_1`, `B_0∪C'`, `B_1∪C'`. Their
  union has the homotopy type of the nerve of the cover: a filled triangle when `D ≠ ∅`, **a circle when `D = ∅`**,
  and `H^r(S¹) = 0` needs `r ≥ 2`. This is the one place where `r ≥ 2` enters (for `r = 1` the statement is false,
  as it must be: `A_1(Λ)` has the covers of `BΛ` as action components). General pairs: a finite chain of
  intermediate copies by interpolation in the dense order. Then the minimal-`F` argument gives `U = G_F`, using
  that an order-preserving permutation of a finite chain is the identity. Followed in full.
- **All actions (A.7).** `El L → El L^inj → El T_S` are weak equivalences over `A` (each by Theorem A twice, the
  slices being non-empty cosieves), `S` is a union of orbits `G/G_F`, and `T_{G/G_F} = A(F, −)` for `F ≠ ∅` (uses
  `Fix(G_B) = B`), the constant point for `F = ∅`. So **every action component is weakly contractible or projects to
  `A` by a weak equivalence**, for all actions, infinite ones and non-injective ones included. This is exactly the
  statement of my Lead 7 in the unsent FRAISSE_EXACT (under (FA) and (Op), `A ∈ 𝒬_n` iff `BA` is `(n−1)`-connected)
  and route (ii) of this prompt's Part A.3; the return proves it for this class directly, as the prompt required.
- **Conclusion (A.8, A.9).** `A_n(F_2) ∈ 𝒬_n ∖ 𝒬_{n+1}` for every `n ≥ 2` (`H_n = F_2`). With my Lead 1 (A.1, A.2:
  re-derived, including the Mayer–Vietoris step with infinitely many cones glued along overlapping sections):
  `T_1 ⊋ 𝒬_2 ⊋ T_2 ⊋ 𝒬_3 ⊋ …`, witnesses `A_n(F_2)` for `𝒬_n ∖ T_n` and its initial cone for `T_n ∖ 𝒬_{n+1}`, the
  span poset for `T_1 ∖ 𝒬_2`; non-empty cosieves of `W_n`-total categories are not `W_n`-total and totally
  `W_n`-dwyérienne sieves do not compose, for every finite `n ≥ 2` (the two sieves `V_0 ⊂ X ⊂ X^▷` of A.2, checked).
- **What is new against the prompt's expectations.** The separator did not come from stage constructions (the route
  the prompt listed first) but from the Galois route. `n = 2` now has three witnesses: the repaired `K*` (A.15, an
  audit of TOTAL_EXACT_2 C.28, which I refereed on 13 Nov), `A_2(F_2)`, and `A_2(Z)`.

**The realization theorem A.13: sound (statement and key steps; the semilinear group `Ĝ` followed once, not
re-derived).** For every non-empty connected Kan complex `K`: `B(Δ_inj/K) ≃ |K|`, and the action components of
`Δ_inj/K` are, up to weak equivalence over `|K|`, the point and **all connected covers of `K`**, nothing else. So
`Δ_inj/K ∈ 𝒬_n` iff `K` is `(n−1)`-connected, and `Δ_inj/K` is total iff `K` is weakly contractible. Steps I
checked: the amalgam by chosen horn fillers at the anchor `p` is strictly functorial (the horn met is the same map,
hence the same chosen filler; outer horns occur, which is why `K` must be Kan); the strict extension of a
null-homotopic map from a finite subcomplex (`Map(Δ^U, K) → Map(L, K)` is a Kan fibration, so its image is a union
of components); the passage from countable to arbitrary `K` by a filtered union with `π_1`-injectivity.
Consequence worth stating in the companion: **membership in `𝒬_n` puts no condition on the homotopy type of `BA`
beyond `(n−1)`-connectivity**, and every action component of a category can be made to be a cover of it.

**Verdict on the second main claim (Lead 6 for every fundamental localizer): sound (followed).** A.10, A.11.
- Necessity: for an action component `D`, the collage `A_D` (one new source `v` with `Hom(v, a) = L_D(a)`) receives
  a final functor from `A` (the comma at `v` is `D`), its nerve is the mapping cone of `BD → BA`, and replacing `BA`
  by a point is a `W`-equivalence of homotopy pushouts (A.10: objectwise `W`-equivalences of `Cat`-valued diagrams
  give `W`-equivalences of Grothendieck constructions, by the relative Theorem A; no accessibility). So `ΣBD` is
  `W`-aspherical.
- Sufficiency: for a final `f: A → B`, the fibred category over `B` with fibres `S(b∖A)` models the fold
  `BB ⊔^h_{BA} BB → BB` and has `W`-aspherical fibres, so the fold is in `W`; with `BA → *` in `W` the wedge fold
  `BB ∨ BB → BB` is in `W`; then `BB → *` follows. **One remark:** the return ends with "retract closure". Closure of
  `W` under retracts of arrows is not an axiom of a fundamental localizer; it is not needed. The last step is the
  third weak-saturation axiom itself: with `i = b_0: * → BB` and `r: BB → *`, `ri = id` and `ir` is the constant map,
  which is in `W`, so `r ∈ W`. (For the record, retract closure does hold for every fundamental localizer, as a
  union of accessible ones, which are strongly saturated: Cisinski, Astérisque 308, quoted from memory.) Not a gap.
- A.12 (statement and key step): `S_{W_n} = 𝒬_n`; in an interval `W_{n+1} ⊆ W ⊆ W_n` the suspension condition is
  "`A ∈ 𝒬_n` and `K(H_n(BD), n+1)` is `W`-aspherical for every action component `D`"; `W_n ∩ W_{Q, ≤ n+1}` is a
  fundamental localizer (I checked the truncated relative Theorem A by the comma spectral sequence) and gives the
  condition "every `H_n(BD)` is torsion", strictly between, with witnesses `A_n(F_2)` and `A_n(Z)`. A.14 (formal
  from A.11–A.13): statement level.

## 2. DER_FOLLOWUP, Part G (section `G.tex`: read in full; notes written 12:41, clock checked)

Numbering. "Loc" is Chapter XVI's unless marked XV. I checked the literal XVI Loc (1) in our transcription
(`der-ch16_p001-005.tex`): (a) isomorphisms, (b) two out of three, (c) `gf, fg ∈ W ⟹ f, g ∈ W`; "stable par
facteurs directs" is Loc (1 bis) and strong saturation is Loc (1 ter). The return's ledger agrees. Its translation
between the two chapters: XVI Loc (5) (components preserved) is XV Loc (8); XVI Loc (8) (filtered colimits) is
XV Loc (7); XVI Loc (4) (arbitrary sums detected) is XV Loc (5 bis). **In the companion every "Loc (8)" must say
which chapter.**

**Verdict on "G.1 refuted for W̃": sound (followed, by hand; no program of mine).**
- `W̃` (REVLOC F.1): `u ∈ W̃` iff `Π_1(Bu)` is an equivalence, `H_q(Bu; Z)` is an isomorphism for `q ≥ 3`, and
  `H_2(Bu; Q)` and `tors H_2(Bu; Z)` are isomorphisms. It is the class inverted by a family of functors, so it is
  strongly saturated; its aspherical categories are the weakly contractible ones (simply connected, `H_2` torsion
  with no torsion), so Loc (2) and Loc (3) are Quillen's Theorem A. It satisfies Loc (1 ter), (2), (3), (4), (5),
  (8), (9).
- The point of the class: **a degree-two map of 2-spheres is in `W̃`**. `f: P → Q` is the map of face posets of the
  suspension of the octagon onto the suspension of the square (50 and 26 objects). Over the span `1 ← 0 → 2` the
  map of Grothendieck constructions `S → T` of `(Q ←f P → e) → (Q ←id Q → e)` has all three slices in `W̃`, and
  `BS` is the cofibre of a degree-two map: a Moore space with `H_2 = Z/2`, while `BT` is contractible. So `S → T`
  fails the torsion test: Loc (3 bis) fails; the same square refutes Loc (6′ a). 77 and 53 objects, as REVLOC said.
- Products: `f × id_B` for `B` the face poset of a square (a circle) is multiplication by 2 on
  `H_3(S² × S¹) = Z`, so it is not in `W̃`; and since `W̃` is strongly saturated, `Cat → Hot_W̃` does not preserve
  this binary product. Both assertions of the prompt's G.1 fail for one strongly saturated class.

**Verdict on "G.2 decided case by case": sound (followed).**
- For `W̃` itself 9.11 and 9.12 hold in all their conditions and 9.13 is vacuous (`π_0` factors through `Hot_W̃`).
- Under Loc (1)–(3) alone all three fail, by the class `W♯` (G.4): split each category into the components with
  `H_1 = 0` and the others; `u ∈ W♯` iff `u` respects the split, is a weak equivalence on the first parts, and for
  each target component of the second kind the sum of the `H_1` of the components over it maps isomorphically.
  I checked two out of three in its three forms and Loc (1)(c), that the aspherical objects are the weakly
  contractible categories, and the example: two disjoint triangles mapping onto their wedge is in `W♯` and merges
  two components, while `H_1` factors through `Hot_{W♯}`, which therefore has infinitely many isomorphism classes.
  So in 9.12 the conditions (c), (c′), (c″), (d) hold and (a), (b) fail; 9.13 fails; in 9.11 (b) holds and (a), (c)
  fail. `W♯` is not stable under retracts (`{0,1} → e` is a retract of the example).
- The repair (G.7; followed, and simplified): Loc (1)–(3) **plus stability under retracts (Loc (1 bis))** give the
  dichotomy "`W ⊆ W_0` or `W` contains every functor between non-empty categories", hence 9.11–9.13, with no
  product stability. The steps: a `u ∈ W` that is not injective (or not surjective) on `π_0` has `{0,1} → e` as a
  retract after adding a whisker; then `A × {0,1} → A` is in `W` by the absolute Theorem A, and the two sections
  give `ar ∈ W` for a point `a` of `A`, so `A` is aspherical. The return quotes Cisinski's Theorem 6.1.18
  (`W_∞` is the least weak fundamental localizer; I confirmed the statement in my text extraction of Astérisque
  308) for "adding a whisker is in `W`"; that needs less: a functor with an adjoint is in `W` by Loc (2), (3) and
  two out of three. XVI Loc (8) implies retract stability (the colimit of `b → b → …` along the idempotent).
  **This answers the question I left open in entry XV.9 of the editors' file: 9.11–9.13 do not hold for a weak
  localizer; they hold as soon as `W` is stable under retracts, and Grothendieck's product argument is not needed.**
- `u_!` (G.8; followed): for `W̃` the constant-diagram functor `Hot_W̃ → HOT_W̃(I)`, `I` the opposite of the span,
  has **no left adjoint**: an adjoint would give `β: L D(Q) → ΣQ` with `β L(a) = bβ`, `a` an automorphism and `b` of
  degree 2 on `H_3`, so `H_3(β) = 0`, against the rational cone invariant `T`, on which the canonical cocone is an
  isomorphism. This is a non-existence proof, not the failure of a formula. So 10.1, 1° fails under Loc (1)–(3),
  even with Loc (1 ter), (8), (9).
- What restores everything (G.9 = REVLOC F.1.1, G.10): Loc (1)–(3) with Loc (6′ a) and Loc (8) give a fundamental
  localizer in Cisinski's sense (through his `Δ`-localizers; Proposition 3.4.25 and Theorem 4.2.15, both confirmed
  in the extraction as cited), hence Loc (3 bis), products and all `u_!`. Statement and key step.

**Verdict on "G.3 proved": sound (followed); it agrees with my reading of 15 Nov (entry XV.8).** For every `W` with
Loc (1)–(3): `(a) ⟹ (b) ⟹ (c) ⟺ (c′) ⟺ (c″)` and `(a) ⟹ (d) ⟹ (c′)`. `(c) ⟹ (c′)` is immediate, as
Grothendieck wrote; `(c′) ⟹ (c)` is the contrapositive proved through the quotient category at ms. 133 ter–quater.
The edition's note at ms. 133 bis has the two directions exchanged for the conditions as printed; its location of
the argument is right. So entry XV.8 now rests on two derivations made independently by two models (mine by hand;
GPT-6 Astra, ChatGPT Pro mode). The return adds one correction of the text: at ms. 133 quinquies the map
`h = (f_0, f_1)` has source `X ⊔ X` and **target `Y`**; to be compared with the scan and the edition before it goes
into the transcription.

**Verdict on "G.4's general lemma refuted": sound (followed, by hand).** `𝓜` = the free completion under countable
products of the zigzag poset `0 → 1 ← 2 → 3 ← …` (objects: finite or countable tuples of integers; a map `x → y` is
a function `φ` of index sets backwards with arrows `x_{φ(j)} → y_j`); `W` = the maps with `φ` bijective. `W` contains
the isomorphisms, has two out of three and is stable under countable products. Every forward map and every inverted
map moves each label by at most one, and the empty tuple cannot be left, so every object joined to `(0)` by a
zigzag is bounded; `(n)_{n ∈ N}` is not; yet every `(n)` is isomorphic to `(0)` in `𝓜W⁻¹`. So
`Hom((0), ∏(n)) = ∅ ≠ ∏ Hom((0), (n))`. **This settles what I left open in entry XVI.3** (the editors' doubt about
infinite products in XVI Lemma 2.5 is justified by a counterexample). Finite products (G.11), a calculus of
fractions (G.13) and model categories (G.14): as I answered in XVI.3; statement level.

## 3. DER_FOLLOWUP, Part D (sections `D.tex`, `D_free_limit.tex`, `D_reductions.tex`, `D_invariant_length.tex`: read in full; notes written 12:43, clock checked)

**The principal assertion of D.1 (PRETOT F.10) is refuted: sound (followed).** D.6: over every non-empty connected
**exact** `A`, `q_M: ∫_A M → B(colim^{Mon} M)` is a weak equivalence for every `M: A → FreeMon`, with arbitrary word
substitutions as transition maps. So `Δ_inj` (and each `W_m`) passes the test and is not filtered (D.7), and every
colimit monoid of free monoids over an exact index has an aspherical classifying space (the prompt's D.3: true).
The proof, which I followed step by step:
- the one comma category of `q_M` is `∫_A D`, where `D(a)` is the translation category of `M(a)` acting on the set
  `C = colim^{Mon} M` (same object set at every `a`, identity-on-objects transitions);
- each `D(a)` is free on a graph, so `H_q(BD(a)) = 0` for `q ≥ 2`;
- `colim^{Cat}_A D` is the translation category of `C` on itself, which has an initial object (I checked the
  presentation argument: each defining relation of `C` can be applied at every vertex, because both sides have the
  same endpoint);
- for diagrams with a fixed object set over a simply connected `A`, `Π(∫_A D) ≃ Π(colim D)`: trivial here;
- the spectral sequence `T_p(H_q(BD(−))) ⟹ H_{p+q}(B∫_A D)` has only the corner left, because `A` is exact.
  Simply connected and acyclic, hence weakly contractible; Theorem A.
This also proves my Lead 3 (D.1, D.2: `H_{k+1}(B∫_A M) = T_k(M_ab)` over total `A`; a `K(Γ, 1)` over exact `A`), and
its hand example is right (D.3: `C = ⟨x, y, z | xy = x, y² = y, yz = z⟩`, `H_2 = 0`, and now `BC ≃ K(F(x, z), 1)`).

**D.4 (free groups over `C_δ`): sound (statement and key steps).** The private-vertex elimination gives finitely
generated free groups and free-factor inclusions; `T_1(Q) = Z`; the group colimit is `F(u, v)`; so the comparison
for this diagram of free groups fails in `H_2`. Free groups with colimit in `Grp` therefore separate exact from
total at `C_δ`, while by D.2 they cannot separate filtered from exact.

**What is open, exactly (the return says so itself; no verdict is hidden).** Whether **every** `M: C_δ → FreeMon`
has `q_M ∈ W_∞`. State reached, each step followed once and not re-derived:
- D.8: `M → T_S`, `T_S(B) = S^{G_B}`, `S = colim` of `M` over the inclusions of finite closed substructures, induces
  a weak equivalence of homotopy colimits and an isomorphism of monoid colimits; **if `S` is free, `q_M` passes**;
  the first-return kernels of maps `F(X) → K` to a diagram of groups always pass.
- D.9: it is enough to treat **finite-rank free monoids with injective transitions** (free hulls in the filtered
  colimit, by the defect theorem and the stability criterion for free submonoids; the hull is canonical, so the
  replacement is strictly functorial).
- D.10: **a strictly positive `G`-invariant additive length on `S` forces `q_M ∈ W_∞` and `T_i(M_ab) = 0` for
  `i > 0`.** So a failing `M` needs an `S` on which `G` scales lengths; in particular the positive-matrix diagram
  with `T_1 = Z` of the return's note has no strict lift to words in its given bases.
- My own remark (by hand, read by nobody): in rank one nothing can fail. A functor `A → (N_{>0}, ×)` on a category
  with `BA` simply connected is a coboundary `ψ(D)/ψ(B)`, isomorphism-invariant, so `G` acts trivially on `S` and
  the length exists. A counterexample must use the order of letters.
- So the class `𝓕` of categories passing every free-monoid test satisfies `exact ⊆ 𝓕 ⊆ total`, both inclusions are
  not both equalities (`C_δ`), and **`C_δ ∈ 𝓕` or not decides which one is strict at the only total non-exact
  category we know.** This is a question of ours; no sentence of the manuscript waits on it.

## 4. DER_FOLLOWUP, Parts B, C, E, F (notes written 12:46, clock checked)

Read: `B.tex` and `B_interval_proof.tex` in full; `C.tex` lines 1–330 (C.1–C.7; the proof of C.7 and C.8 not read);
`E.tex` E.2–E.4 statements and the proofs of E.2, E.3; `F.tex` in full. None of these is among the brief's main
claims; verdicts are at the level stated.

- **Part B (statement and key steps; followed once).**
  - B.2 (my item B.4): every bounded interval of the reachability preorder is weakly contractible. The non-empty
    words are `Δ/K` for `K` the nerve of the indiscrete groupoid on `{+, −}`; the interval `s ≤ w ≤ r` is the set
    of simplices of the image `A_r` of an alternating simplex that lie outside a subcomplex `L` of its boundary
    (I checked the two cases `ν(s) = ν(r)` and `ν(s) < ν(r)`); `|A_r|` is a closed ball (step functions with at
    most `n` sign changes, identified with the boundary of a moment body); the simplices of `A` outside `L` have
    the type of `|A| ∖ |L|` (a Reedy argument). A complete and unusual proof; I found no gap on one reading.
  - B.3: (2F) ⟺ (DESC) ⟺ (LOC), the last implication by an explicit strictification `F ← H → p^*G`.
  - B.4: **the exact class.** `F` satisfies (𝒟) iff its extension `F^ω` to countable signed orders with unbounded
    alternation sends every map to a weak equivalence, iff the two maps `F^ω(L) → F^ω(L + J) ← F^ω(J)` are weak
    equivalences for every `L`.
  - B.6, B.7: (𝒟) does not imply (LOC), and (𝒟₁) does not imply (𝒟), already for presheaves of sets, with
    explicit examples. So the expert's suggestion in Lead 5 ("(𝒟) exactly for the diagrams on which `𝕋y` acts") is
    refuted; Lead 5 (a)–(c) are proved.
- **Part C (C.1–C.4 followed; C.5–C.7 statements; C.8 not read).** My Lead 2 is proved for paths of every length:
  the two obstruction groups `Z[Y(z, z)]/⟨γv : vu = 1⟩` and `Z[Y(z, z)]/⟨γv⟩`; for `W_∞`, `W_Z`, `W_n` (`n ≥ 2`) the
  end-point functor of the full path category is strictly aspherical iff totally aspherical iff `Y` is a connected
  thin groupoid. The table C.7 adds: `q` is `W_n`-aspherical iff `BY` is `(n+1)`-connected; for `W_0`, `W_1`
  strict = total = aspherical. So PRETOT E.9 is closed, and remark N6 of the PRETOT review (strict ≠ total for
  path fibrations) holds only for the truncated category `P_{≤1}`.
- **Part E (statement and key steps).** Every right `End_Δ([n])`-act is `K_n` for a unique simplicial set `K` of
  dimension at most `n`; `B(M_n/K_n) ≃ |K|` for all such `K` (E.2). **Lead 4 (a) is corrected (E.3):** the further
  functor to the category of non-degenerate simplices exists only for free degeneracy completions (or `n = 1`);
  for `Δ[2]/∂Δ[2]` that category is a graph with `H_1 = Z²`. The error was in Lead 4 (a) as the review F13 and I
  wrote it; PRETOT A.4 itself is not affected. (b)–(d) stand: the groups are the trivial group (`n = 1`), the
  groups with a finite balanced presentation and trivial abelianization (`n = 2`), the finitely presented
  superperfect groups (`n ≥ 3`).
- **Part F.** F.2 is new and small: over the three-element monoid `End_Δ([1])` the five-element act of the
  two-edge interval is totally `W_∞`-aspherical, and its category of elements fails condition I (the two edges
  have no common successor; checked by hand), so it is not even quasi-filtered.

## 5. What the results settle in Grothendieck's text (task 2)

Pages are manuscript pages. "Settled" means: the return proves it and my verdict above is "sound"; AI-produced,
unrefereed outside this project.

| Place | His claim, question or doubt | What is now known | Where |
|---|---|---|---|
| II ms. 36ter | totally aspherical means filtered (conjecture) | False, and the whole picture: `filtered ⊊ exact ⊊ total ⊊ quasi-filtered = 𝒬_2 ⊋ 𝒬_3 ⊋ …`, `⋂ 𝒬_n = total`; witnesses `Δ_inj`, `C_δ`, repaired `K*`, `A_n(F_2)`. Membership in `𝒬_n` constrains the homotopy type of `BA` only by `(n−1)`-connectivity (A.13) | A.8, A.9, A.13, F.1 |
| II ms. 36ter (our test, PRETOT F.10) | do free monoids detect filteredness? | No: every exact category passes every free-monoid test (`Δ_inj`); the test lies between exact and total | D.6, D.7 |
| XII ms. 88–89, Définition 1 | "totalement `W`-asphérique" | For every fundamental localizer: `A` is total for `W` iff `A` is `W`-aspherical and every action component has a `W`-aspherical suspension | A.11 |
| XII ms. 93–97, Proposition 8 and its converse ("je me vois mal construire un exemple") | does a totally aspherical presheaf have a totally aspherical category of elements? | No, for `W_∞`, `W_Z`, `W_n` (`n ≥ 2`): a five-element act over a three-element monoid. The direct implication holds for every fundamental localizer | F.2, E.4 |
| XII ms. 101–103, Proposition 10 ("J'en doute fort !") | total asphericity of end-point functors of path categories | The classification that decides it (I did not reopen the page today; his sentence is to be quoted from it): aspherical iff `BY` weakly contractible; strictly or totally aspherical only when `Y` is equivalent to the point, so a doubt about total asphericity is right | C.4, C.7 |
| XII ms. 109, Définition 2 | strictly against totally aspherical | They coincide for end-point functors of full path categories (`W_∞`, `W_Z`, `W_n`, `n ≥ 2`) and differ in general (PRETOT B.3) | C.4 |
| XII ms. 113–114 | do the dwyérienne classes compose? ("n'ont pas du tout l'air de l'être") | Strictly and totally aspherical functors compose for every fundamental localizer; totally `W_∞`-dwyérienne sieves compose; `W_∞`-dwyérienne sieves do not; **totally `W_n`-dwyérienne sieves do not, for every finite `n ≥ 2`** | A.9, F.3 |
| VII ms. 103 (b), 109–110, 112–114 | for which fibred categories over the types is `C_∞ → C` an isomorphism in `Hot`? | Exactly those of B.4. Path diagrams always (so "en général pas" at ms. 112 is false in the context where it is written, as PATHS and INDLOCAL had shown); arbitrary fibred categories can fail; one cofinal sequence does not decide; the statement on components at ms. 110 holds | B.4, B.6, B.7, B.10 |
| XV ms. 128–133 quinquies, 9.10–9.13 | "localiseur fondamental sans plus (Loc (1, 2, 3))" suffices | It does not (`W♯`); stability under retracts, Loc (1 bis), suffices, with no use of products. At ms. 133 bis Grothendieck's "(c) ⟹ (c′) trivial" is right and the edition's note has it reversed | G.4–G.7 |
| XV ms. 134–137, 10.1, 1° | `u_!` exists for every fundamental localizer | False under Loc (1)–(3), even with strong saturation: no left adjoint for `W̃`. True with Loc (3 bis); the edition's note there is right | G.8, G.10 |
| XVI ms. 2, footnote 1 | Loc (3 bis) "le plus important des deux" | Confirmed: without it products and `u_!` fail | G.3, G.8 |
| XVI ms. 7–16, Lemma 2.5 | products exist in `𝓜W⁻¹` when `W` is stable under them | True for finite families (`W` containing the identities); false for countable families; true with a calculus of fractions or a model structure. The edition's doubt is justified | G.11–G.14 |
| XVI ms. 118, Corollaire 7.7.2 and footnote 56 ("Loc (3 bis) pas prouvé, probablement faux") | does Loc (6′ a, 8, 9) give Loc (3 bis)? | **Yes** (with Loc (1)–(3), and Loc (9) is not needed): the corollary is right and the footnote's guess is wrong. Without Loc (6′ a) it fails (`W̃`). **The line in `INTAKE_S2COUNT_REVLOC_20261117.md` that REVLOC F.1 "decides his doubt in his favour" should be read this way.** | G.2, G.9 |

## 6. FINMON, checkpoint 20 (notes written 12:55, clock checked)

**What I had and what I read.** The decoded folder holds two files, the report (621 lines) and the register (695
rows). The paper (459 pages) is in the encoded checkpoint as a plain PDF (`FINMON_work/FINMON_paper.pdf`); I
extracted its text with `pdftotext` to my scratchpad and read Section 6 (pages 430–435) and five statements of
Section 1. The sections' TeX, the notes, the code and the certificates (16,248 encoded files, 14 GB) were not
decoded: the decoder is the return's own code, which I do not run. Read: the first 90 lines of the report (the
reviews of hours 18–20), the working report's opening, the passage on the 22-arrow category, and the 53 task rows
of the register with the full row of C2-CP2.

**Register.** 695 rows: 625 Proved, 12 Refuted, 1 Unresolved (C2-CP2), 52 explanatory records, 1 definition, and
four rows with a qualified status (B2, E4, F-VII121, F-XII15). The brief's figures are right. The return's first
line is INCOMPLETE, as the prompt requires.

**Verdict on the main claim (C2: 17 ≤ least number of arrows of a category of type `CP²` ≤ 22): statement level
only. I cannot call it sound and I found nothing against it.**
- The lower bound is a tree of structural theorems closed by exhaustive enumerations with literal certificates
  (for 17 arrows and four objects: 215,194,501 corner tables, 3,911,101 retained records, no survivor; an
  independent checker). None of this was run or read by me. What I checked is the bookkeeping: the object-count
  theorem "no category of type `CP²` with `k` objects and at most `min(21, 2k+7)` arrows" gives at most 4 objects
  at 17 arrows, 5 at 18–19, 6 at 20–21, as the register says; one-object categories need 23 arrows (B4-CP2);
  strongly connected two-object categories are excluded through 22; and the register's own sentence on what is
  left agrees with the brief: **at 17 arrows the remaining families are the linear three-object profiles (154
  frozen profiles, enumeration unfinished) and the nine two-object profiles with a large opposite corner (literal
  gates complete for profiles 0–4, 6, 7; profiles 5 and 8 unfinished).** Nothing is claimed for 18–21 beyond the
  structural theorems.
- The upper bound: two explicit categories with 22 arrows (two objects: an 18-element monoid, three arrows from
  the other object, one identity), each mapped by a functor to a certified 23-element monoid of type `CP²`
  (`sections/C_CP2_upper22.tex`; not read). Checked by the return's two verifiers, not by me.
- The run spent hours 10–20 on this one item. It is an enumeration, and its state cannot be handed to a new run
  except as tables: the certificates are 14 GB.

**Statements I did check, by hand.**
- Proposition 6.6 (V ms. 51–52), the last sentence: the tests `X ↦ ([BC, X])_{C finite}` are neither faithful nor
  conservative. The example is the group `G` of finitary permutations of `N` and the injection `s: G → G` that
  inserts a fixed point. **It is the example of my entry V.10 of 15 Nov**, which the FINMON run cannot have seen
  (it was not attached); the two derivations agree.
- Proposition 6.7 (VII ms. 121): `BC_2 = RP^∞` is not a compact test (the identity does not factor through a
  skeleton, by `H^*(−; F_2)`).
- Proposition 6.9 and Corollary 6.10 (XII appendix ms. 8–11 and 15): the category `Z` of ms. 10–11 (objects
  `0, a, b, c`; two arrows `0 ⇉ a`; `a → b`, `a → c`; the two composites to `b` equal, likewise to `c`; 10 arrows)
  is the union of two cones on the parallel pair along it, so `BZ = S²`: `π_1 = 0`, `π_2 = Z`. So at ms. 15
  "`π_1 ≅ Z`" is wrong, and for `W = W_1` the category is `W`-aspherical; the non-asphericity holds for `W ⊆ W_2`.
- The mechanism of E1–E2 (no finite category has type `K(Z, 2)`, `K(Z/2, 2)`, `ΩS³`): positive-degree rational
  classes are nilpotent because restriction to the maximal subgroups has nilpotent kernel (A3(i)-detection).
  The key step itself was not read.

**Everything else: statement level, by the register.** The rows a reader of the companion should know of, all
unrefereed: D1, D2 (refuted: a finite category with finite-dimensional and not finite classifying space; Wall's
obstruction is realized; the tables have about 10^17 objects and are given by a recursive lookup); D3 (the
finite-dimensional types of two-object categories: finite CW types with free `π_1`); E3 (Sweeney's six-element
monoid is `⋁_{n≥2} Sⁿ`; S2COUNT A.M1 says the same); E4 (`[BC, S²]` can have the cardinality of the continuum;
S2COUNT B:main says the same; both are GPT-6 Astra, ChatGPT Pro mode, so this is two runs of one model);
B4 (least orders of monoids: `S² ∨ S²` 7, `S⁴` 9, `CP²` 23, `S² × S²` 25, `M(Z/2, 2)` 13, `M(Z/3, 2)` 17);
C2 (least numbers of arrows: `S⁴` 9, torus 15, `S¹ ∨ S¹` 5, `RP³` 16, `L(3, 1)` 20); C3 (a poset of type `RP²` needs
49 arrows); A3 (the Quillen-type detection holds; nilpotence of all positive classes when `U(M) = 1` fails:
a six-element monoid); A5 (for finite categories, bounded integral homology kills every endomorphism in `π_1`).

**What FINMON settles in the text (task 2, continued).**

| Place | His claim or question | What is now known | Where |
|---|---|---|---|
| V ms. 51–52 (`Hot_0`) | the types of finite categories as tests | They contain all finite CW types and more (`RP^∞`), not `K(Z, 2)`, `K(Z/2, 2)`, `ΩS³`; as set-valued tests they are neither faithful nor conservative; one-object finite models of finite CW complexes exist exactly for the simply connected ones | Prop. 6.6; A, B, E |
| VII ms. 121 | a finite category as a compact test | False: `BC_2` | Prop. 6.7 |
| VII ms. 128 | the computation of the `π_i` is finite | Homology in a fixed degree is a finite computation; triviality of `π_1` of a finite category is undecidable (Adian) | Prop. 6.8 |
| IX ms. 9–13, 22–23 | the three printed tests | INDLOCAL C.25, C.26 confirmed step by step; a five-arrow non-trivial example passes all three | Prop. 6.4, 6.5 |
| XII app. ms. 8–11 | the small models of `S¹`, `S²` | His 10-arrow category is `S²` (his own footnote 7 is right); least numbers of arrows for `S¹`, `S²`, `S³`: 4, 5, 7 | Prop. 6.9 |
| XII app. ms. 15 | "`π_1 ≅ Z`" for that category, hence not aspherical for `W ⊆ W_1` | Wrong: `π_1 = 0`, `π_2 = Z`; it is `W_1`-aspherical; not aspherical for `W ⊆ W_2` | Cor. 6.10 |

## 7. The next Dérivateurs prompt: its items (task 3; written 12:57, clock checked)

Mathematics only; the procedure is the main session's. Sources of the items: the two returns above;
`NEW_PROMPT_ITEMS_20261117.md` (DER_OPEN_ROWS); `field_experts/FOLLOWUPS_FROM_NOTES_20261117.md` (@4, @8, @270);
`field_experts/GAP_FROM_NOTES_20261117.md` (g6). **I read the entries, not the scans of cotes 105, 133, 134-8, and
not REVLOC's sections D.** Where an item needs a statement from those, it says so; the builder fills it from the
transcription. The order is mine.

**My judgment on the shape.** These items fall into three groups that share no mathematics: localizers (A–D
below), finite models (E), and exactness over Fraïssé classes (the one item DER_FOLLOWUP left open). The third
group is the subject of the unsent 04_FRAISSE_EXACT and goes there (section 8). The first two can share one
prompt, with the localizer question as the main question and the finite models last.

### Part A. Reverse excision and homology localizers (the main question is A.1 with A.2)

- **A.1 (follow-up @4; cote 105, scan 052; open rows POLES F.14 (1), RESIDUE I.7).** Prove or refute: every
  fundamental localizer that satisfies the strengthened reversibility axioms W7 bis and W8 bis of cote 105/052 is
  a homology localizer, that is, `RT`-fixed in the notation of REVLOC Part D (`W = R(T(W))`). A refutation is one
  localizer, with each axiom verified and a proof that it is not `RT`-fixed.
  - What is known: for the plain reverse square axiom (XVI Loc (6 b)) the answer is no. REVLOC D.2.2, D.2.3: every
    non-zero thick subcategory of finite spectra is the finite stable part of a reversible localizer that is not
    `RT`-fixed; and the expert's `RESULT_REVERSIBLE_NOT_STABLE.md` (the null class of the 2-local spheres). Both
    unrefereed. So the question is what the strengthening adds. Our records disagree (NEW_RESULTS 7 against
    NEW_RESULTS 8): the item ends with the one statement that replaces both.
  - To be filled by the builder: the exact text of W7 bis and W8 bis (105/052) and of W(7), W(7 bis) at XII
    ms. 75–78, which `W_∞` fails (TOTASPH: XII Théorème 2 is false).
- **A.2 (follow-up @8 (ii); cote 105/047, 051–052; TOTASPH A.13, BISITE A.33, RESIDUE I.7).** Determine the form
  of the reverse square and cube excision axioms (Der 6, Der 8; W7 bis, W8 bis) that passes to every shifted
  derivator `D_I`. For each hypothesis in Grothendieck's statements: needed or not, with a derivator for which the
  unrepaired axiom holds and fails for some `D_I`. Then answer A.1 for the repaired axiom.
- **A.3 (REVLOC D.2.4).** Decide: is there a reversible fundamental localizer that is not `RT`-fixed and whose
  stable part contains no non-zero finite spectrum? (`NEW_PROMPT_ITEMS_20261117.md`, A1, with its lead: REVLOC's
  rows D.2.10–D.2.61 are one obstruction computation in which the run stalled; a second route is asked for.)
- **A.4 (REVLOC D.3.2).** For `L = loc(S/2)`: the interval between the least reversible localizer containing
  `RP^∞ → e` and the `Z[1/2]`-homology equivalences; does it have more than two elements? (the same file, A2).
- **A.5 (left by DER_FOLLOWUP G.9; XVI ms. 118, Corollaire 7.7.2).** Prove or refute: XVI Loc (1)–(3) and
  Loc (6′ a) imply Loc (3 bis) without Loc (8). Known: with Loc (8), yes (G.9, through Cisinski's
  `Δ`-localizers, where Loc (8) gives the transfinite compositions); with Loc (8) and without Loc (6′ a), no (`W̃`).
  Then the same for Loc (1 ter) in that corollary: which of Loc (8), Loc (9) it needs.

### Part B. Trivial cofibrations (follow-up @8 (i); cote 105/020, 032, 034–040; PATHS D.18, D.22; BISITE A.27, A.28)

- **B.1.** Prove or refute: the class `TC` generated by the interval equals `C ∩ W`, under smallness or
  accessibility hypotheses stated explicitly; give the weakest hypothesis under which it holds and an example
  where it fails without it. (Chapter XIII asks the same of a localizer on a general `𝓜`; REVLOC H.1–H.4 say that
  accessibility of `W^lc_D` holds under Vopěnka's principle and can fail without measurable cardinals.)

### Part C. The linear case (gap item g6; cote 134-8, scans 048–054; Pursuing Stacks §134; GALOIS G.6, RESIDUE I.7)

- **C.1.** Grothendieck's "Thm(?)": for a `k`-linear category `𝓜` with a `k`-bilinear tensor product, enough
  projectives and exact limits, and an interval `α: 1 → J` that stays a monomorphism after tensoring with every
  object and has `L_iφ(J ⊗ x) = 0` for all `i ≥ 0`: prove or refute that the resolving functor `Λ = λ_!` and its
  adjoint `λ^*` induce quasi-inverse equivalences between the localization of `𝓜` and that of chain complexes (the
  counit tests of scan 053, with the "Hypothèse-clef" of 048 and Lemmes 1–3 of 053–054). The statement is to be
  taken from the transcription, hypothesis by hypothesis; where it fails, the least repair.

### Part D. Finite-dimensional local systems and schematization (follow-up @270; cote 133, scans 006–008; Pursuing Stacks §110)

- **D.1.** The war game's H6 is false as written (`S² → *` induces an equivalence on finite-dimensional `k`-local
  systems and `H²(S²; k) = k`). Prove or refute the corrected statement: the maps that induce isomorphisms on
  cohomology with coefficients in every finite-dimensional local system of `k`-vector spaces (equivalently, on the
  derived categories generated by them: say which) form a fundamental localizer, and its localization is Toën's
  schematization. My remark, from memory and unchecked: the localizer axioms should follow from the comma spectral
  sequence with local coefficients, as for homology localizers, and the second half should be Toën's universal
  property of the schematization with respect to these equivalences; the work is to state it with the right
  hypotheses on `k` and on base points, and to find the exact theorem in Toën's *Champs affines* and in
  Katzarkov–Pantev–Toën. The return GALOIS computed the classes `W^lc_D`, `W^1_D` for `D(k)`: compare.

### Part E. Finite models (no passage of the manuscript waits on these)

- **E.1 (FINMON C2-CP2).** Determine the least number of arrows of a finite category of type `CP²`. State: it is
  between 17 and 22; a monoid needs 23; among two-object categories with one trivial corner ("act cones") the
  least is 22; at 17 arrows two families are left (the linear three-object profiles; the two-object profiles with
  a large opposite corner, of which two of nine are unfinished by the report's last review and four by the
  register, frozen earlier); at 18–19 at most five objects, at 20–21 at most six.
  **My view:** this is an enumeration that took ten hours of the last run and whose certificates cannot be
  attached. If it goes into a prompt, it goes last, and the three-hour check will end it. It is better suited to a
  compute job than to a Pro slot; the user decides whether the number is worth one.
- **E.2–E.4 (S2COUNT E:E2, E:E3gap, E:E4gap).** The two-dimensional acyclic resolutions of `S²`, as items B1–B3 of
  `NEW_PROMPT_ITEMS_20261117.md`. Undecided in two runs; closed off for the companion by the stopping rule.

### The item that goes to FRAISSE_EXACT instead (left open by DER_FOLLOWUP D.1)

- **Free monoids over `C_δ`.** Decide whether `q_M ∈ W_∞` for every `M: C_δ → FreeMon`. More generally determine
  the class `𝓕` of non-empty connected categories on which every free-monoid comparison is a weak equivalence:
  `exact ⊆ 𝓕 ⊆ total` (D.6; PRETOT F.9), and decide which inclusion is strict. State reached: D.8 (a free limit
  monoid passes), D.9 (finite rank and injective transitions suffice), D.10 (a positive invariant length forces
  passage and `T_i(M_ab) = 0`). The decisive sub-question, as I see it: **can `T_1(M_ab)` be non-zero for a
  free-monoid diagram over `C_δ`?** By D.10 such a diagram has a limit monoid with a relation `x = (g·x)·w`,
  `w ≠ 1`. Smallest instance with such relations: the gap diagram of Lead 3 pulled back along the forgetful
  functor `C_δ → Δ_inj`; for it `M_ab` is `Z[points] ⊕ Z` and `T_1 = 0` (my computation by hand, unchecked), so
  it does not fail in `H_2`; whether its comparison is a weak equivalence is the first thing to settle.

## 8. Should 04_FRAISSE_EXACT be folded in? No: it stays separate, with a patch

Reasons. (1) It has its own main question (A.3, exactness against amenability and the Ramsey properties), about
thirty items and eleven Leads; a prompt with two main questions gives neither most of the time. (2) It shares no
mathematics with Parts A–D above. (3) It is the natural home of the free-monoid item, which works with the same
objects (`C_δ`, `G = Aut(M)`, the fixed-point functor `B ↦ S^{G_B}`, invariant functionals).

What DER_FOLLOWUP changes in it (I outlined the prompt's Parts again today; I did not reread it in full):
- **B.6 is settled** (A.6–A.8): for every `n ≥ 2` the class of `F_2`-valued `n`-cocycle structures has all open
  subgroups pointwise stabilizers and `BA = K(F_2, n)`. The item becomes "check A.6–A.8 and use them".
- **B.2 (Lead 7) is proved in two families** (A.7; A.13, where the open subgroups that are not pointwise
  stabilizers give exactly the connected covers). The item becomes the general theorem in setting (S), with these
  as the cases to recover.
- **B.5** (the category with a linear and an independent cyclic order): its purpose, a second witness for
  `total ⊊ quasi-filtered`, is met by `A_2(F_2)` and `A_2(Z)`. The return cites Campion–Ye (2020, Theorem 3.6;
  2026, Corollaries 1.13, 1.14, 2.8) for the type `K(Z, 2)` of the cyclic-order class; I did not open them. What
  is left of B.5: (St) and (Op) for that class.
- The results list gains A.11 (Lead 6), D.1, D.2, D.6 (exact indices pass every free-monoid and free-group
  comparison), D.4 (free groups over `C_δ` fail), and the sentence that DER_FOLLOWUP A.3 is no longer open.
- A new Part: the free-monoid item above.

## 9. Hunches (task 4), each with its reason. Mine, unchecked.

1. **`A^op` is an orbit category.** In a Fraïssé class with strong amalgamation, `Hom_A(B, C)` is the set of
   `G`-maps `G/G_C → G/G_B` (because `Fix(G_B) = B`), so `A^op` is the orbit category of `G = Aut(M)` for the
   family of pointwise stabilizers of non-empty finite sets, actions on `A` are coefficient systems of sets, the
   saturation `L ↦ T_S` is the fixed-point system of a `G`-set, `T_k` is Bredon homology for that family, and
   `BA` is the orbit space of the `G`-complex glued from the orbits `G/G_B` (the classifying space of the family
   when a family is closed under subgroups, which this one is not). I checked the identification of the hom-sets
   by hand; the rest is the standard dictionary, from memory. Reason to care: A.7 and A.13 are then statements
   about a family that is not closed under subgroups, and exactness of `colim_A` is "Bredon homological dimension
   zero", for which there is a literature (Lück; Nucinkis and others; from memory) that none of our prompts has
   used. It is the language in which FRAISSE_EXACT A.3 should be asked.
2. **The action spectrum.** Call the set of weak homotopy types of the action components of `A` its action
   spectrum; `𝒬_n` and totality are conditions on it alone. It contains the point when `A` is not empty
   (representable actions) and is closed under connected covers (A.14).
   - For categories that need not be connected the converse is a corollary of A.13 (my remark, by hand): a set of
     connected types that contains the point and is closed under connected covers is the action spectrum of the
     disjoint union of the categories `Δ_inj/Sing X`, `X` in the set.
   - For **connected** categories it is open, and this is the question I would ask: which sets occur? The
     constructions we have add types: the cone of A.1 adds the cofibres of the sections (suspensions of `BE` and
     their wedges), and the punctured product of two cones has the join as its base. First case: is
     `{pt, S², S³}` the action spectrum of a connected category? Reason to expect a restriction: in a Fraïssé
     category the components are the `E_U`, quotients of one space by the open subgroups (hunch 1), so the
     spectrum is a family of "generalized covers" of `BA`; but the repaired `K*` and the cones show that a
     component can carry homology that the base does not.
3. **Free monoids over `C_δ`: no lean.** For passage: every condition the return tried forces it, and the word
   structure (Levi's lemma) kills the abelian candidates. Against: passage over exact indices used exactness
   exactly once, to kill `T_p` of the cycle modules, and over `C_δ` positive diagrams with `T_1 = Z` exist at the
   abelian level; a compatible positive functional is a fixed point of a diagram of compact spaces on `C_δ^op`, and
   `C_δ` fails that property (TOTAL_EXACT_2 A.17, A.19). The sub-question in section 7 decides it.
4. **Chapter XV should be read with Loc (1 bis), Chapter XVI with Loc (3 bis).** Not a hunch any more but a
   consequence of G.4–G.10 that the companion should say in one place: 9.11–9.13 need retract stability and
   nothing else; products and `u_!` need the relative axiom and nothing weaker among the axioms he lists, even
   with strong saturation. His footnote 1 at XVI ms. 2 asks for exactly this exchange.
5. **A.5 above (is Loc (8) needed for Corollaire 7.7.2?).** I expect yes. Reason: forward gluing gives finite cell
   attachments only, and the relative Theorem A over an infinite base needs a transfinite composition; a class
   defined by a condition on finite subcomplexes should separate them. I have no example.

## 10. For the main session: records that these returns change

- `derivateurs_notes_out_20261115/EDITORS_INSIGHTS_AND_OUR_ANSWERS_20261115.md`: entry **XV.8** now has a second
  derivation (G.6); **XV.9** is no longer open (9.11–9.13 fail for a weak localizer and hold with Loc (1 bis):
  G.4–G.7; `u_!` fails: G.8); **XVI.2** is settled (products fail for `W̃`: G.3); **XVI.3** is settled (a
  counterexample for countable products: G.12); **V.10** has an independent confirmation (FINMON Prop. 6.6). The
  closing list "Left open in the answers" of that file is out of date in these four places.
- `INTAKE_S2COUNT_REVLOC_20261117.md`, section 3, row F.1: "decides Grothendieck's doubt … in his favour" is
  misleading. Corollaire 7.7.2 is true as he states it; the footnote's "probablement faux" is wrong; `W̃` shows
  only that Loc (6′ a) cannot be dropped.
- Lead 4 (a) of the DER_FOLLOWUP prompt, and finding F13 of the PRETOT review from which it came, are wrong for
  simplicial sets that are not free degeneracy completions (E.3).
- The transcription at XV ms. 133 quinquies: the target of `h = (f_0, f_1)` should be `Y` (G.6, F.3); to be
  compared with the scan and the edition.
- Timestamps in this file were read from the clock; four that I first wrote ahead of it were corrected.

## 11. Not done

- FINMON: no proof followed outside the four statements named in section 6; the sections, notes, code and
  certificates were not decoded; the two 22-arrow categories were not recomputed.
- DER_FOLLOWUP: the proofs of C.7, C.8, E.1, E.4, E.5 and G.13, G.14 were not read; no program of the return was
  run and none of mine was written (every check above is by hand); the notes, the code and the bibliography
  ledger were not opened; the PDF check (overfull boxes, rendered pages) was not done.
- The scans of cotes 105, 133 and 134-8 and REVLOC's sections D were not read for section 7.
- The registry, STATUS.md and the tally are the main session's.

Claude Fable 5.2 at effort max, 17 November 2026.
