# FRAISSE_EXACT: exact colimits, total asphericity and amenability for categories of embeddings

To be settled: for the category `A` of strong embeddings of a Fraïssé class with limit `M` and group `G = Aut(M)`,
the exact relation between exactness of `colim_A` on abelian groups, amenability and extreme amenability of `G`, and
the Ramsey and convex Ramsey properties; the general theorem behind the totality of the predimension category `C_δ`
and its converse; exactness of colimits as a statement about limits of compact diagrams; the whole predimension
family `a|V| − b|E|`; and the three ways in which a limit of solvable problems can fail to be solvable.

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for the deliverables: `FREX`.
Drafted on 13 Nov 2026 by Claude Fable 5.2 (Anthropic, effort max), field expert of the Dérivateurs line, from the
return TOTAL_EXACT_2 (GPT-6 Astra, ChatGPT Pro mode, 13 Nov 2026; 89 statements, none open), its intake by Claude
Fable 5.2 at effort high and the drafter's referee reading at effort max of its main proofs (A.21, A.24, A.30–A.34,
C.25–C.28: no gap, no error; attached). Three questions and two corrections from the field experts' conference of
13 Nov 2026 are folded in (Leads 5 (c), 6, 7, 10, 11; Parts A.3 (vi)–(viii), B.3, B.5, B.6, C.4, C.6).

Related prompts. TOTAL_EXACT_2 is closed: `filtered ⊊ exact ⊊ total ⊊ quasi-filtered` (R1). DER_FOLLOWUP (ready,
unsent) asks for the tower `𝒬_n` of truncated totality, the fibred categories over the interval types, strictly
aspherical end-point functors, free monoids as test diagrams, and for a second check of TOTAL_EXACT_2 C.10, C.19–C.28;
none of that is to be done here. Part B.5 below treats one category only and feeds that prompt.

## What is attached

`FRAISSE_EXACT_background.zip` (LaTeX and text; the only PDFs are the two notes of Isbell and Mitchell, for which no
source exists; `MANIFEST.tsv` lists every file with its origin):

- `TOTAL_EXACT_2/`: the final return: `TOTEX2_paper.tex`, `sections/` (34 files), `TOTEX2_results.csv` (the
  register, 89 rows), `TOTEX2_references.bib`, `TOTEX2_report.md`. Cited below as "T" with the register numbers.
  The sections used most: `predimension_category.tex` (T A.21–A.24), `predimension_stabilizers.tex` (T A.30–A.32),
  `predimension_totality_reduction.tex` (T A.33–A.34), `ordered_graphs.tex` (T A.6–A.10), `compact_duality.tex`
  (T A.12–A.17), `compact_convex.tex` (T A.18–A.19), `uniform_finite_coefficients.tex` (T A.20),
  `cyclic_linear_orders.tex` (T A.11), `main_question.tex` (T A.1–A.3).
- `reviews/REVIEW_MAIN_PROOFS_TOTEX2.md`: the referee reading (what was checked, step by step, and what was not);
  `reviews/INTAKE_TOTEX2.md`: the intake, one line per row of the register with the basis of its verdict.
- `TOTASPH/TOTASPH_C.tex`: proofs of TOTASPH C.5 (the action criterion for totality) and C.6 (exact ⟹ total).
- `arxiv/`: LaTeX sources of Evans–Hubička–Nešetřil, *Automorphism groups and Ramsey properties of sparse graphs*
  (`1801.01165`); Kechris–Pestov–Todorcevic (`math_0305241`); Moore, *Amenability and Ramsey theory* (`1106.3127`);
  Evans–Hubička–Nešetřil, *Ramsey properties and extending partial automorphisms* (`1705.02379`);
  Hubička–Nešetřil, *All those Ramsey classes* (`1606.07979`); Angel–Kechris–Lyons (`1208.2389`); Caramello,
  *Fraïssé's construction from a topos-theoretic perspective* (`0805.2778`); Conant, *An axiomatic approach to free
  amalgamation* (`1505.00762`); Evans–Ghadernezhad–Tent (`1312.3430`).
- `papers/IsbellMitchell1973.pdf`, `papers/IsbellMitchell1976.pdf`.
- `DER_II-a.tex` (II ms. 36–36ter) and `DER_XIIb-a.tex` (XII ms. 88–89): the transcription of the manuscript pages
  this work bears on. The transcription is AI-made; the scans are the authority. Where a formula looks wrong, say
  so and reason from the mathematics.

Not attached, to be found and opened by you where used: Kechris–Rosendal 2007 (Proposition 6.4), Nguyen Van Thé 2013,
Kechris–Sokić 2012, Zucker 2016, Tsankov 2012, Oberst 1968, Isbell 1974, Hrushovski 1993, Macpherson–Tent 2011.

## Where this comes from

- II ms. 36–36ter: Grothendieck suspects that a totally `W∞`-aspherical category is filtered. XII ms. 88–89
  (Définition 1) defines total asphericity. The returns TOTASPH, TOTEX and TOTAL_EXACT_2 replace the conjecture by
  the chain of R1, with every inclusion strict.
- The separator between total and exact, `C_δ`, came from a homogeneous structure: its totality is a statement about
  the open subgroups of `Aut(M)`, and its non-exactness has a uniform gap for probability measures (T A.18), which is
  the language of amenability. This prompt asks for the theorems behind these two observations.

## Results this prompt builds on (status on 13 Nov 2026)

**Notation and conventions used from here on (keep them).**

- Categories are small. `BA = |NA|`. An *action* on `A` is a functor `L: A → Set`; `El_A(L)` has objects `(a, l)`,
  `l ∈ L(a)`, and arrows `f: (a, l) → (b, L(f)l)`. `A` is *total* when it is non-empty and connected and every
  connected component of every `El_A(L)` is weakly contractible (this is total `W∞`-asphericity: TOTASPH C.5).
- Condition I: every span completes to a commutative square. An *affine equalizer* of `a_0, …, a_k: p → q` over a
  ring `R` is `t ∈ R[A(q, r)]` of augmentation 1 with `t a_0 = ⋯ = t a_k`. Condition IV: every parallel pair has an
  affine equalizer over `Z`. *Quasi-filtered*: non-empty, connected, I and IV. *Exact over `R`*:
  `colim_A: (R-Mod)^A → R-Mod` is exact; *exact* means over `Z`. `T_i = L_i colim_A`. `P_p = Z[A(p, −)]`.
- **Setting (S).** `(𝒦, ≤)` is a strong class in the sense of Evans–Hubička–Nešetřil 2019, Definition 2.1: a class of
  finite structures in a countable language, closed under isomorphism, with a class of *strong* embeddings that
  contains the isomorphisms, is closed under composition and satisfies (*): `A ≤ C`, `A ⊆ B ⊆ C`, `B ∈ 𝒦` imply
  `A ≤ B`. It has countably many isomorphism types, joint embedding and amalgamation for strong embeddings. `A` is a
  skeleton of the category of non-empty members of `𝒦` with the strong embeddings. `M` is the Fraïssé limit (their
  Theorem 2.6), `G = Aut(M)` with the topology of pointwise convergence. A finite `F ⊆ M` is *strong* when `F ≤ M`;
  `G_F` is its pointwise stabilizer and `G_{{F}}` its setwise stabilizer. `A_M` is the category of non-empty finite
  strong subsets of `M` with all strong embeddings between them; it is equivalent to `A`. A `G`-set or `R[G]`-module
  is *smooth* when every element has an open stabilizer.
- Hypotheses that may be added to (S), always named when used. **(Rig)**: every member of `𝒦` has only the identity
  automorphism. **(SA)**: amalgams can be chosen with the two images meeting exactly in the base. **(FA)**
  (functorial amalgamation over non-empty bases): for non-empty `P` with strong `P ≤ X` and `P ≤ Z` there is an
  amalgam `X ⊗_P Z ∈ 𝒦`, with strong embeddings of `X` and `Z` whose images meet exactly in `P`, such that for every
  strong `u: X → Y` over `P` the map `X ⊗_P Z → Y ⊗_P Z` (`u` on `X`, the identity on `Z`) is a strong embedding,
  compatibly with composition. **(FA∅)** (functorial joint embedding): the same over the empty base. **(St)**:
  `⟨G_B, G_C⟩ = G_{B∩C}` for all finite strong `B, C ⊆ M`. **(Op)**: every open subgroup of `G` is `G_F` for a finite
  strong `F ⊆ M` (`F = ∅` allowed). **(WEI)**: every open subgroup `U` of `G` has a finite strong `F ⊆ M` with `G_F`
  normal of finite index in `U`. **(Fin)**: no open subgroup of `G` has a proper open subgroup of finite index.
- *Ramsey* (for a category `A` with finite hom-sets): the morphism Ramsey property of T A.6: for `p, q` and `c` there
  is `r` such that every colouring `A(p, r) → {1, …, c}` is constant on `g ∘ A(p, q)` for some `g: q → r`.
  *Finite-pattern Ramsey*: T A.12. *EPPA*: Evans–Hubička–Nešetřil 2019, the definition before their
  Kechris–Rosendal theorem (every strong partial automorphism of `X` extends to an automorphism of some `Y ≥ X`).
- **Three fixed-point properties of a small category `A`.** (CH): every diagram `A^op → CompHaus` of non-empty
  compact Hausdorff spaces has a non-empty limit. (CC): every diagram on `A^op` of non-empty compact convex subsets
  of locally convex spaces, with continuous affine transition maps, has a non-empty limit. (CT): every *torsor
  diagram* on `A^op` has a non-empty limit, where a torsor diagram is a diagram `K: A^op → CompAb` of compact
  Hausdorff abelian groups and continuous homomorphisms together with a diagram `T: A^op → CompHaus` and continuous
  simply transitive actions `K(a) × T(a) → T(a)` for which every transition map of `T` is equivariant along that of
  `K`. (CT)_p and (CT)_Q: the same with every `K(a)` a profinite `F_p`-vector space, respectively the Pontryagin
  dual of a `Q`-vector space.
- **(Re)** (Reiter condition for `A`): for all objects `p, q` with `A(p, q)` finite and every `ε > 0` there are `r`
  and a finitely supported probability measure `ν` on `A(q, r)` with `‖ν a − ν a'‖_1 ≤ ε` for all `a, a' ∈ A(p, q)`,
  where `ν a` is the image measure on `A(p, r)`.
- **The predimension family.** For integers `k ≥ 2`, `a, b ≥ 1`: `δ(U) = a|U| − b|E(U)|` on finite `k`-uniform
  hypergraphs (`E(U)` the hyperedges inside `U`); `B' ≤_d B` when `δ(U) > δ(B')` for all `B' ⊊ U ⊆ B`; `C(k, a, b)` is
  a skeleton of the category of non-empty finite linearly ordered `k`-uniform hypergraphs with `δ(U) > 0` for every
  non-empty `U`, with the increasing induced embeddings of `d`-closed image. `C_δ = C(3, 2, 3)`. `V` is the point,
  `W` the single hyperedge, `v_1, …, v_k: V → W` its points (arrows when `b < (k−1)a`).

**The results.** None of these is to be proved again as if open. For each one you use: read the proof at the place
named, confirm the step you rely on with your own argument, or give the exact error with a repair.

**R1 (TOTAL_EXACT_2 D.1 with TOTASPH C.5, C.6; checked).** Among non-empty connected small categories,
`{filtered} ⊊ {exact} ⊊ {total} ⊊ {quasi-filtered}`, with witnesses `Δ_inj` (finite ordinals and increasing
injections), `C_δ`, and the Adámek–Koubek–Reiterman category with repaired quasi-filters. Status: the proofs behind
the middle and the last separation (T A.21, A.24, A.30–A.34; T C.10, C.19–C.28) were read in full by the intake and
again by the drafter; no gap found.

**R2 (Isbell–Mitchell 1973, Theorem 1 and Lemma 1; 1976; as used in T A.6, T C.41).** For non-empty `A` in which any
two objects have a common successor: `colim_A` is exact over `R` iff every finite family of parallel arrows has an
affine equalizer over `R`. (An affine arrow that equalizes the ordinary arrows in the supports of two affine arrows
equalizes these.) Status: 1973 opened by the first expert; 1976 opened by the return.

**R3 (T A.1, A.24, A.34; proofs read in full twice).** `C_δ` is total. For every non-zero ring `R` the map
`D: R[A(W, −)] → R[A(V, −)]²`, `g ↦ (g v_2 − g v_1, g v_3 − g v_1)`, is objectwise injective (among `r` hyperedges on `v`
vertices, `2v > 3r`, so one vertex lies on exactly one of them), `colim D = 0`, and `T_1(coker D) ≅ R`: the triple
`v_1, v_2, v_3` has no affine equalizer over `R`.

**R4 (T A.30–A.33; proofs read in full twice).** For `C_δ`: (St) holds, by a finite alternating amalgam on a long
circle (A.30, A.31); hence (Op) (A.32: a minimal `B` with `G_B ≤ U`, and rigidity). And (A.33): for every action `H`,
the maps `H → H^inj → T_S`, with `H^inj` the quotient by "equal after some arrow", `S = colim` of `H^inj` over the
finite strong subsets of `M` with inclusions, and `T_S(B) = S^{G_B}`, induce weak equivalences on categories of
elements (Quillen's Theorem A; the comma categories are non-empty full cosieves of slices `P/A_M`, contractible by
`X ↦ X ∪_P Z`); `T_{G/G_F} ≅ A_M(F, −)` by `Fix_M(G_B) = B`; so (Op) gives totality. The proof of A.33 uses of `C_δ`
only: the existence and homogeneity of `M`, I, the functorial free amalgam with the order "`X`-side before `Z`-side in
each gap of `P`" over non-empty `P` (for the two comparisons) and over the empty base (only to contract `A_M`
itself, the category of elements of the orbit `G/G`), and (Op).

**R5 (T A.6, A.8; intake: proof read).** A category with finite hom-sets, common successors and the Ramsey property
is exact: for `a_0, …, a_k: p → q`, every `r` that is Ramsey for `p, q` and `(3k+1)^k` colours carries an integral affine
equalizer. Finite ordered graphs with induced embeddings are exact (Hubička–Nešetřil 2019, Corollary 4.3, not opened
by us).

**R6 (T A.12–A.14; intake: proof read).** For non-empty `A` with common successors: (CH) holds iff `A` is
finite-pattern Ramsey; either implies exactness.

**R7 (T A.15, A.20; intake: proof read; Isbell–Mitchell 1976, Proposition 4.5).** Over a quasi-filtered `A`: every
`A^op`-diagram of non-empty finite sets with `|X(a)| ≤ N` for one `N` has a non-empty limit, and `T_1(M) = 0` when
`|M(a)| ≤ N` for one `N`; over a total `A`, then `T_i(M) = 0` for all `i > 0`.

**R8 (T A.18, A.19; intake: proof read).** For `C_δ` and every finitely supported probability measure `μ` on
`A(W, X)`: `‖μ v_2 − μ v_1‖_1 + ‖μ v_3 − μ v_1‖_1 ≥ 1`. Hence (Re) fails for `C_δ`, and (CC) fails for `C_δ` (a diagram of
finite-dimensional compact convex sets with empty limit).

**R9 (T A.2, A.3; intake: proof read).** `colim_A` is exact over `Z` iff it is exact over `Q` and over every `F_p`.
`C_δ` is not exact over any non-zero ring.

**R10 (T A.11; intake: proof read, cut identities recomputed).** For the category `C` of non-empty finite sets with
a linear order and an independent cyclic order (cyclic orders on one or two points unique) and the injections
preserving both: `BC` is simply connected, `H_2(BC; Z) ≅ Z`, and a five-arrow family has no affine equalizer over any
non-zero commutative ring.

**R11 (duality; two lines, checked by the drafter).** For `M: A → Ab`, with `M^∨ = Hom(M, R/Z): A^op → CompAb`:
`lim^i_{A^op} M^∨ ≅ Hom(T_i(M), R/Z)` as abstract groups, `lim^i` being computed on the underlying diagram of abstract
groups (apply the exact functor `Hom(−, R/Z)` to the bar complex).

**R12 (statements read by the drafter in the attached LaTeX sources; proofs not read, except the third).**
(i) Kechris–Pestov–Todorcevic, as formulated in Evans–Hubička–Nešetřil 2019 (subsection "The KPT correspondence",
citing KPT Theorem 4.8 and Nguyen Van Thé): for an amalgamation class `(𝒦, ≤)` of finite rigid structures, `G` is
extremely amenable iff `(𝒦, ≤)` is a Ramsey class. KPT Corollary 6.8: the finite linear orders with a convex
equivalence relation form a Ramsey class, with limit `(Q², E, <_lex)`.
(ii) Moore 2013, the theorem listing the forms of the convex Ramsey property: for a Fraïssé structure `X` (all
embeddings), `Aut(X)` is amenable iff for all `A', B'` in the age, `ε > 0` and `n` there is `C'` such that for all
`f_1, …, f_n: Emb(A', C') → [0, 1]` some finitely supported probability measure `β` on `Emb(B', C')` has
`|f_i(α) − f_i(α')| ≤ ε` for all convex combinations `α, α'` of the `β ∘ a`, `a ∈ Emb(A', B')`.
(iii) Evans–Hubička–Nešetřil 2019, Theorem 3.8 (proof read): if a topological group acts continuously by
automorphisms on a `k`-sparse graph (`|R^B| ≤ k|B|` for finite `B`) and there are adjacent `a, b` with the `G_a`-orbit
of `b` and the `G_b`-orbit of `a` both infinite, the group is not amenable. Their Kechris–Rosendal theorem: EPPA
implies that `G` has compact subgroups `G_1 ⊆ G_2 ⊆ ⋯` with dense union, and is amenable. Their theorem in the
subsection "Amenable subgroups": for a free amalgamation class with all embeddings (relations and partial
functions), `G` is amenable.

## Leads

Inferences by Claude Fable 5.2 (Anthropic), the drafter. None was checked by anyone else or by a program. Each is to
be proved or refuted in full; the expected answer is stated plainly, and a wrong Lead is to be called wrong.

**Lead 1 (exactness is a property of the group).** In setting (S), for `V: A_M → R-Mod` let `V_∞ = colim V(B)` over
the finite strong subsets with inclusions; `G` acts on it by `g · i_B(v) = i_{gB}(V(g|_B)v)`, and `V_∞` is smooth. Then
`colim_A V ≅ (V_∞)_G` (coinvariants), naturally: every arrow of `A_M` is an inclusion after the restriction of an
automorphism. Every smooth `N` is `V_∞` for `V(B) = N^{G_B}`. Hence: `colim_A` is exact over `R` iff `N' → N` injective
implies `N'_G → N_G` injective, for smooth `R[G]`-modules. Expected: true as stated. Consequences expected: for a
discrete group `G` this is local finiteness when `R = Q`; if `Γ ≤ G` is dense then `N_G = N_Γ` for smooth `N`.

**Lead 2 (amenability as a fixed-point property of `A`).** In setting (S) with finite hom-sets: `G` is amenable iff
(Re) holds for `A` iff (CC) holds for `A`. Derivation of the first equivalence for classes with all embeddings: Moore's
theorem (R12 (ii)), then von Neumann's minimax theorem for the bilinear pairing between probability measures `β` on
`Emb(B', C')` and families `(f_{a,a'})` of functions with values in `[−1, 1]` weighted by a probability vector on the
pairs `(a, a')`; the passage to strong classes is by cofinality of the strong subsets. The second: as T A.13 is to
Ramsey, by compactness and separation. Expected: true.

**Lead 3 (exactness as a fixed-point property of `A`).** For every small `A`: `colim_A` is exact over `Z` iff
`lim_{A^op}` preserves surjections between diagrams of compact abelian groups iff (CT). Derivation: R11; a surjection
`X → Y` of compact diagrams and a point `y ∈ lim Y` give the torsor diagram of fibres under the kernel; a torsor
diagram `T` under `K` has the class `[T(f)t_b − t_a] ∈ lim^1 K` of any choice of points, zero iff `T` has a point in the
limit. The same over `F_p` with (CT)_p and over `Q` with (CT)_Q. Expected: true. So (CH) ⟹ (CC) and (CH) ⟹ (CT), and
the main question of Part A is the relation between (CC) and (CT). The three rows (CH) and Ramsey, (CC) and Reiter, (CT) and
exact were reached independently in three talks of the experts' conference of 13 Nov 2026; no proof of the convex row
was written there.

**Lead 4 (`Aut(M)` for `C_δ` is not amenable; two routes).** (a) The graph on `M` joining two points of a common
hyperedge is 2-sparse: for finite `B`, the hyperedges inside `B` and one further hyperedge for each remaining adjacent
pair, `t` of them, give with their third vertices `t < 2|B| − 3|E(B)|` by positivity. A copy `W ≤_d M` has `d`-closed
points, and the `G_a`-orbit of `b` is infinite for `{a, b, c} = W` (free amalgams of copies of `W` over `a`). Apply
R12 (iii). (b) R8 and Lead 2. (c) Directly: the potentials that certify R8 on the finite strong sets give, by
compactness, a non-empty compact convex `G`-space without a fixed point (argument of the intake, checked by the
previous expert, not re-checked by the drafter). Expected: true by each route.

**Lead 5 (two mechanisms for exactness, and two obstructions).** (a) If `G` has compact subgroups
`G_1 ⊆ G_2 ⊆ ⋯` with dense union (for instance under EPPA), `colim_A` is exact over `Q`: for smooth `N`, `N_G` is the
colimit of the `N_{G_n}`, and coinvariants of a compact group on a smooth `Q`-module are exact (finite orbits,
averaging). (b) If some member of `𝒦` has an automorphism `σ ≠ id` of finite order `m`, the pair `(id, σ)` has no
affine equalizer over a ring in which `m` is not invertible (an equalizer is constant on the free `σ`-orbits of
`A(X, r)`), so `A` is not exact over `Z`, not quasi-filtered and not total. (c) If `V ≤ U` are open subgroups with
`[U : V] = m` finite, the map `Z[G/U] → Z[G/V]` sending a coset of `U` to the sum of the `m` cosets of `V` in it is an
injection of smooth modules which induces multiplication by `m` on coinvariants; so exactness over `F_p` implies
`p ∤ [U : V]` for all such pairs, and exactness over every `F_p` implies (Fin). This contains the condition
"`p ∤ |U/G_F|`" of the conference reply of the previous expert. Expected: all three true. Example for (a), (b), (c):
finite graphs with all embeddings (EPPA by Hrushovski 1992): exact over `Q`, not over any `F_p`, not total.

**Lead 6 (amenable does not imply exact).** (a) `M = (Z; d_k)_{k ∈ Z}` with `d_k(x, y) ⟺ y − x = k`: homogeneous,
`G = Z` discrete, amenable; `A` = non-empty finite subsets of `Z` up to translation with translation embeddings;
the two points `V ⇉ {0, 1}` have no affine equalizer over any non-zero ring (a finitely supported function on `Z`
equal to its translate is zero). Here (SA) fails and `A` is not total. (b) `M = Z × Q` with the equivalence relation
"same first coordinate", the order of `Q` inside each class, and the relations `d_k` between classes:
`G = Aut(Q, <)^Z ⋊ Z` is amenable, the structures are rigid, (SA) holds, and the two points of two consecutive classes
have no affine equalizer over any non-zero ring; `G` has the open normal subgroup `Aut(Q, <)^Z`, which is not a `G_F`,
so (Op) fails, and `A` is not quasi-filtered. Expected: both correct. Both categories have finite hom-sets and (Re),
so a finiteness hypothesis on the hom-sets (proposed at the experts' conference of 13 Nov, where the example was the
one-object category of the group `Z`) does not rescue "amenable implies exact over `Q`". The implication from
amenability to exactness can hold only under hypotheses that exclude these, which is A.3 (ii), (iii).

**Lead 7 (totality in terms of the open subgroups).** In setting (S), for an open subgroup `U ≤ G` let `E_U` be the
category whose objects are the finite strong `B ⊆ M` with `G_B ≤ U` and whose arrows `B → C` are the maps `u|_B`,
`u ∈ U`, `uB ⊆ C`. Then `El_{A_M}(T_{G/U}) ≃ E_U` (send `(B, gU)` to `g^{-1}B`). If (FA) holds, the two comparisons of
R4 hold for every action, and: `A` is total iff `E_U` is weakly contractible for every open `U`; `A` is in `𝒬_n`
(every action component `(n−1)`-connected) iff every `E_U` is `(n−1)`-connected. Also
`π_1(E_U) ≅ U/⟨G_B : G_B ≤ U⟩` (the poset of objects is directed, and `E_U` is its transport category for `U` with the
loops of the `G_B` killed). Under (Rig) and (St) every open `U` is a `G_F` and `E_U` has an initial object for `F ≠ ∅`,
while `E_G = A_M`. So under (FA) and (Op) every action component is weakly contractible or weakly equivalent to `A`:
`A` is total iff `BA` is weakly contractible (which (FA∅) gives), and `A ∈ 𝒬_n` iff `BA` is `(n−1)`-connected. If
`G_F` is normal of finite index in `U`, then `E_U ≃ B(U/G_F)` (`U/G_F` acts freely on the contractible `F\A_M`; reply
of the previous expert at the conference). Expected: all true. Three consequences, each expected true:
(a) **the converse of T A.33 is false**: the finite linear orders with a convex equivalence relation (R12 (i)) are
Ramsey, hence exact (R5) and total (R1), (FA) and (FA∅) hold, and the stabilizer of an equivalence class of
`(Q², E, <_lex)` is open and is not a `G_F` (a `G_F` with `F` meeting the class fixes a point of it; a `G_F` with `F`
outside the class moves the class); for the stabilizer `U` of a class, with or without convexity of the order,
`E_U` is contractible directly (adjoin to the distinguished class a new point, placed just above the class when
classes are convex and above the whole structure when the order is independent of the relation: a functor with
natural maps from the identity and from a constant);
(b) under (SA), (WEI) and quasi-filteredness, (Op) holds (`π_1(E_U) = U/G_F` must vanish); so under (FA), (FA∅) and
(WEI): quasi-filtered iff total iff (Op);
(c) the category `C` of R10 has (FA) (in each cyclic gap and each linear gap of a non-empty base, the `X`-side
first) and not (FA∅); if (Op) holds for it, `C` is quasi-filtered and not total, with the single non-contractible
action component `C` itself (`BC` simply connected, `H_2 = Z`; expected `BC ≃ CP^∞`). That would be a second witness
for the last inclusion of R1, a counterexample to (b) without (FA∅), and the case `n = 2` of the question whether
some `E_U` is `(n−1)`-connected and not `n`-connected.

**Lead 8 (the predimension family).** (a) The proofs of T A.21 and A.30–A.34 use only submodularity, integrality
and positivity of `δ` (the loss at the cut becomes `a·m`, the bound `s > 3(δ(E) + a·m)`). Expected: `C(k, a, b)` is
total for all `k ≥ 2`, `a, b ≥ 1`; so the family contains no category that is quasi-filtered and not total.
(b) For `k ≥ 3` and `ak/2 ≤ b < (k−1)a`: the `v_i` are arrows, and among `r` hyperedges on `v` vertices `av > br`, so
if every vertex lay on two of them, `kr ≥ 2v > 2br/a`, against `2b ≥ ak`; hence a private vertex,
`g ↦ (g v_i − g v_1)_{i ≥ 2}` is objectwise injective and `C(k, a, b)` is not exact over any non-zero ring. For `b ≥ ka`
there are no hyperedges and `C(k, a, b) = Δ_inj`. (c) For `b < (k−1)a`, `Aut(M)` is not amenable: run the argument
of R12 (iii) on the compact space of assignments of every hyperedge of `M` to one of its vertices with at most
`⌈a/b⌉` hyperedges assigned to each vertex (non-empty by Hall's theorem, since `|E(B)| < (a/b)|B|`); for an invariant
measure, some vertex `x` of a copy of `W` has the copy assigned to it with probability `p > 0`, and the `G_x`-orbit of
the copy is infinite. For `a(k−2) < b` the graph of Lead 4 (a) is itself sparse and R12 (iii) applies as stated; for
`b ≤ a(k−2)` it is not (a complete graph on `B` is realized by hyperedges with private further vertices), so the
remark after the definition of sparse graphs in Evans–Hubička–Nešetřil 2019, that the graph of a sparse relation is
sparse, fails as stated, and the hypergraph form is needed.
(d) In the unordered class of `C_δ` the triple `v_1, v_2, v_3` is equalized over `Q` by the sum of the six labellings
of one hyperedge divided by 6; the order is what makes T A.24 work.
(e) For `k = 3` and `2b < a` the obstruction of R3 disappears: on the object with points `1 < 2 < 3 < 4 < 5` and the
five hyperedges `123, 234, 345, 124, 245` (positive iff `a > b`; each hyperedge is `d`-closed iff `a > 2b`, the binding
sets being `{1,2,3,4}`, `{2,3,4,5}` and the whole object), the combination `t = [123] + [234] + [345] − [124] − [245]`
has augmentation 1 and `t v_1 = t v_2 = t v_3 = [3]`. A support in which every vertex lies on exactly two hyperedges
cannot work (each vertex would have the same position in its two hyperedges with opposite coefficients, and the
augmentation would be 0), so between `2b < a` and `2b ≥ 3a` there is a threshold for this triple that the drafter
did not compute. Since `Aut(M)` is not amenable for all `b < 2a` (c), the categories `C(3, a, b)` with `2b < a` (first
`C(3, 3, 1)`) are the natural candidates for an exact category with a non-amenable group, that is, for refuting
A.3 (i). Not decided by the drafter: exactness for `b < ak/2` (first cases `C(2, 2, 1)`, `C(3, 3, 1)`) and for
`(k−1)a ≤ b < ka` (first cases `C(2, 1, 1)`, `C(3, 1, 2)`).

**Lead 9 (the three regimes).** Let `d: X → Y` be a morphism of `A^op`-diagrams of Hausdorff topological abelian
groups and `y ∈ lim Y` *levelwise solvable*: `y_a ∈ d_a(X(a))` for every `a`. (1) If `A^op` is a tower (index `N`)
and the transition maps of `X` are surjective, then `y` lies in the closure of `d(lim X)` in `lim Y`, and the
obstruction to solving `y` is its class in `lim^1 ker(d_n)`; for compact groups it vanishes. (2) For compact groups
and a general index: every levelwise solvable `y` is solvable, for all `d`, iff `colim_A` is exact (Lead 3); for
compact groups `d(lim X)` is closed, so over a non-exact index there is a levelwise solvable `y` outside the closure
of the image. (3) So an obstruction that is not in `closure(im d)/im d` needs a non-exact index or a failure of the
hypotheses of (1). Model cases: `d_n: Z → Z/2^n` over `N` (limit `Z → Z_2`, obstruction `Z_2/Z`, in the closure);
the dual of R3 over `C_δ^op` (compact, uniform gap, obstruction `F_p`, not in the closure). Expected: true.

**Lead 10 (exactness over every `F_p` against exactness over `Q`).** Let `A` have common successors and, for a finite
parallel family `a_0, …, a_k: p → q`, let `D_r(t) = (t a_i − t a_0)_i` on `Z[A(q, r)]` and let `I ⊆ Z` be the ideal of
the augmentations of the `t ∈ ker D_r`, over all `r`. (a) For a family of two arrows, `D_r` is the incidence matrix of
a directed graph, hence totally unimodular: an affine equalizer over one `F_p` at `r` gives a rational one at `r`, and
affine equalizers over every `F_p` give `I = Z`. (b) At one target `r`, the primes `p` for which an `F_p`-affine
equalizer exists without a rational one divide the torsion of `coker D_r`; so in a category with a weakly terminal
object, exact over every `F_p` implies exact over `Q`. (c) If `colim_A` is exact over every `F_p`, then torsion
diagrams are acyclic, `T_i(M)` is a `Q`-vector space for every objectwise torsion-free `M` and `i ≥ 1` (multiplication
by `p` in `0 → M → M → M/p → 0`), and `Z/I` embeds in a `Q`-vector space for every family: `I = 0` or `I = Z`. So under
this hypothesis exact over `Q` and exact over `Z` are the same. (d) Hence a counterexample to "exact over every `F_p`
implies exact over `Q`" needs a family of three or more arrows with `I = 0` for which the saturations
`Sat(r) = {s ∈ Q[A(q, r)] : D_r(s) integral}` have `colim_A Sat ≅ Q` through the augmentation and the torsion of the
cokernels has colimit `Q/Z`: every prime power is a denominator at some target and no target sees infinitely many
primes. Expected: (a)–(d) true. The implication itself is not decided by the drafter.

**Lead 11 (objectwise dimensions do not determine `T_1`).** Over `C_δ` and a field `k`, take `α, β, γ ∈ k^×` with
`α + β + γ ≠ 0` (`(1, 1, 1)`, or `(1, 1, 2)` in characteristic 3) and `D'': k[A(W, −)] → k[A(V, −)]`,
`g ↦ α g v_1 + β g v_2 + γ g v_3`. By the private vertex of R3, `D''` is objectwise injective; `colim D''` is
multiplication by `α + β + γ`; so `T_1(coker D'') = 0`. Then `M' = k[A(V, −)] ⊕ coker D''` has
`dim M'(X) = 2|A(V, X)| − |A(W, X)| = dim (coker D)(X)` for every object `X`, with `T_1(M') = 0` and
`T_1(coker D) = k`. Dually: two diagrams of finite-dimensional spaces on `C_δ^op` with equal dimensions at every
object and `lim^1` of dimensions 0 and 1. Expected: true; the class is carried by the image of the column in the
colimit (its vector of augmentations), not by sizes.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (the class, its strong embeddings, the verification of every hypothesis and of the
failure; checked by a program when finite or finitely presented) and the strongest true statement proved in its
place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the
obstruction as an exact statement and the smallest undecided instance are the state of an item you are still
working on: record them as you go, then attack the obstruction, starting from that instance. "Known" counts only
with the derivation of the statement used here from the cited theorem, after opening the source. An item that
begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is the whole
answer.

For Part A in particular. An implication between exactness and amenability is proved for every class of the stated
setting, or refuted by one class given completely: its language, members and strong embeddings; the proofs of joint
embedding and amalgamation and of each added hypothesis ((Rig), (SA), (FA), (FA∅), (St), (Op), (WEI), (Fin)) that the
item names; the
proof of amenability or of non-amenability of `G`; and the proof of exactness (an affine equalizer for every finite
family, over the ring named) or of non-exactness (a named family, with the proof that no target carries an affine
equalizer).

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1–R12 again in place of
the items; exactness claimed from equalizers of pairs only, of one family only, or over `Q` when the item says `Z`;
amenability or the Ramsey property quoted for a class of all embeddings and used for a strong class without the
passage being proved; a statement about all classes of setting (S) proved only for free amalgamation classes, only
for finite relational languages or only for `ω`-categorical limits, without saying so; totality claimed from finitely
many actions or from homology only; a limit statement about all compact diagrams proved only for finite or only for
profinite ones; a step that replaces a claim by a convenient special case without naming it.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `FREX_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Exactness against amenability and the Ramsey properties. The main question is A.3.**

1. Prove or refute Lead 1. Then decide whether totality of `A` is determined by the topological group `G`: prove it,
   or give two classes with isomorphic topological groups `Aut(M)`, one with a total category and one without.
2. Prove or refute Lead 2, with the exact form of Moore's theorem for strong classes that you use, and prove or
   refute, for setting (S) with (Rig) and finite hom-sets: (CH) for `A` iff `A` is Ramsey iff `G` is extremely
   amenable.
3. For setting (S), prove or refute each of the following.
   (i) If `colim_A` is exact over `Q`, then `G` is amenable (second half of the conference item FE-6).
   (ii) If (Rig), (FA), (FA∅) and (Op) hold and `G` is amenable, then `colim_A` is exact over `Z`.
   (iii) If (Rig), (FA), (FA∅) and (Op) hold and `G` is amenable, then `colim_A` is exact over `Q`.
   (iv) If (Rig) holds and `colim_A` is exact over `Z`, then `G` is extremely amenable (every exact example known to
   us is Ramsey).
   (v) For every small category: (CT) implies (CC); and (CC) together with totality implies (CT).
   (vi) If `colim_A` is exact over `F_p`, then `p ∤ [U : V]` for all open `V ≤ U` of finite index (Lead 5 (c)); and if
   `colim_A` is exact over `Q` and `p ∤ [U : V]` for all such pairs, then `colim_A` is exact over `F_p` (conference
   item FE-2, stated for all pairs of open subgroups).
   (vii) If `colim_A` is exact over `Q` and (Fin) holds, then `colim_A` is exact over `Z`.
   (viii) For every small category with finite hom-sets and common successors: (Re) implies exact over `Q`.
   Expected: false, by Lead 6 (first half of the conference item FE-6).
   What is proved already: Ramsey implies exact over `Z` (R5); the Leads 5, 6 and 10; for `C_δ` exactness fails
   over every ring (R3) and amenability fails (Lead 4), so `C_δ` decides none of (i)–(iv); the categories of
   Lead 8 (e) are the candidates against (i) and (iv). For each of (i)–(viii) that is false, state and prove the
   strongest true statement in its place, so that at the end the relation between "exact over `Z`", "exact over
   `Q`", "exact over `F_p`", "amenable", "extremely amenable" in setting (S), and its dependence on (Rig), (FA),
   (FA∅), (Op), (Fin), is a list of proved implications and of counterexamples with no pair left undecided.
4. Decide, with proofs, for each of the following classes: totality; exactness over `Z`, over `Q` and over `F_2`;
   amenability and extreme amenability of `G`; (St); (Op). (1) `C_δ` (what remains is Lead 4). (2) Finite linear
   orders with a convex equivalence relation. (3) Finite sets with an equivalence relation and an independent linear
   order; for it prove or refute the conference item FE-1 (no second reader): with `b` two inequivalent points
   `x < y`, `c` the structure `x_1 < y_1 < x_2 < y_2` with `x_1 ~ x_2` and `y_1 ~ y_2`, and `α_1 = (x_1, y_1)`,
   `α_4 = (y_1, x_2): b → c`, no `β ∈ R[A(c, d)]` of augmentation 1 has `βα_1 = βα_4` when 2 is not a unit of `R`
   (a parity argument; it agrees with the `RP^∞` of B.3 (c)), and the category is exact over `Q` and over `F_p`
   for every odd `p` (a sketch only). (4) Finite partial orders with an independent linear order. (5) The category of R10. (6) Finite graphs
   with all embeddings. (7) `C(2, 2, 1)` and `C(3, 3, 1)`. (8) The two classes of Lead 6.
5. Prove or refute Lead 5 and Lead 6.

**B. Totality of categories of embeddings.**

1. Prove in setting (S): (FA), (FA∅) and (Op) imply that `A` is total. Say exactly which properties of `(𝒦, ≤)`
   the proof of T A.33 uses, and prove each of them from (S), (FA), (FA∅), (Op) or add it to the hypotheses by name.
2. Prove or refute Lead 7: the equivalence `El(T_{G/U}) ≃ E_U`; the criteria for totality and for `𝒬_n` under (FA);
   the formula for `π_1(E_U)`; that under (FA) and (Op) every action component is weakly contractible or weakly
   equivalent to `A`; the equivalence `E_U ≃ B(U/G_F)` for `G_F` normal of finite index in `U`.
3. Prove or refute: in setting (S) with (FA) and (FA∅), if `A` is total then (Op) holds. Expected: false
   (Lead 7 (a)). Then prove or refute: (a) in setting (S), `A` total implies (Rig), and implies that every open
   subgroup is generated by the subgroups `G_B` (`B` finite strong) that it contains; (b) Lead 7 (b): under (FA),
   (FA∅) and (WEI), quasi-filtered iff total iff (Op); and decide the same statement without (FA∅) (expected: false,
   Lead 7 (c)); (c) for the classes (2), (3), (5) of A.4 and for `C_δ` determine all open subgroups and the homotopy
   type of every `E_U`, in particular for the open subgroups that are not finite extensions of pointwise
   stabilizers (expected: for the stabilizer of an equivalence class, contractible; for the stabilizer of an
   unordered pair of classes in the class (3), `RP^∞`, so that this class is not quasi-filtered).
4. Prove or refute, for a strong class with free amalgamation (Evans–Hubička–Nešetřil 2019, Remarks 2.7) expanded
   by all linear orders: (St) and (Op) hold. Lead: for classes with all embeddings no estimate is needed (a set of
   points that are pairwise in a common relation lies in one factor of a long cyclic amalgam, by the Helly property
   of short arcs), and the result is then weak elimination of imaginaries (Conant 2017, attached); for strong
   classes the cyclic amalgam must be shown to stay in the class, as T A.30 does for `C_δ`. Give the exact
   hypothesis under which the alternating bridge of T A.30 exists.
5. For the category `C` of R10: prove or refute (St) and (Op); decide whether it is quasi-filtered; determine the
   homotopy type of `BC` (expected: that of `CP^∞`); determine the least `n` for which some action component of `C`
   is not `(n−1)`-connected, with the action (expected: `n = 3`, the component `C` itself; Lead 7 (c)).
6. Prove or refute: for every `n ≥ 2` there are a class in setting (S) and an open subgroup `U` of its group such
   that `E_U` is `(n−1)`-connected and not `n`-connected. Prove or refute: for every `n ≥ 2` there is a class in
   setting (S) with (Rig), (FA) and (Op) whose category `A` has `BA` `(n−1)`-connected and not `n`-connected; by
   Lead 7 such an `A` lies in `𝒬_n` and not in `𝒬_{n+1}`. What is known: `n = 2` is expected from `C`; open subgroups
   that are finite extensions of pointwise stabilizers give `K(Γ, 1)` and never contribute; the stabilizer of an
   equivalence class gives a contractible `E_U`. Lead (drafter, unchecked): a class with two unrelated sorts has
   `BA ≃ BA_1 * BA_2` (join), but the objects whose first sort is non-empty form a cosieve, hence an action
   component, weakly equivalent to `A_1`; so joins of sorts do not raise the connectivity of all action components,
   and (FA) fails for them over bases that are empty in one sort.

**C. Exact colimits as limits of compact diagrams.**

1. Prove R11 with all identifications named, and its versions over `F_p` (profinite `F_p`-vector spaces) and over `Q`.
2. Prove or refute Lead 3, for `Z`, for each `F_p` and for `Q`.
3. Prove or refute: `colim_A` is exact over `F_p` iff every torsor diagram on `A^op` under finite `F_p`-vector spaces
   has a non-empty limit. Lead: true when `A` has finite hom-sets (`T_1` commutes with filtered colimits and every
   functor is the union of its finitely generated subfunctors). Decide it for all small `A`.
4. Let (P) be: `lim^1_{A^op}` vanishes on all diagrams of profinite abelian groups. Prove or refute: (P) iff
   `colim_A` is exact over every `F_p`. Then prove or refute: **if `A` has common successors and finite hom-sets and
   `colim_A` is exact over `F_p` for every prime `p`, then `colim_A` is exact over `Q`** (equivalently: if `lim^1`
   vanishes on all profinite abelian diagrams on `A^op`, it vanishes on all compact abelian ones; a counterexample
   would have, for a finite family, integral `t_n` at targets `r_n` with `t_n(a_i − a_0) ∈ N_n Z[A(p, r_n)]`,
   `aug t_n ≡ 1 mod N_n`, every prime dividing some `N_n`, and no rational affine equalizer at any target). Prove or
   refute Lead 10 (a)–(d) on the way. Decide the statement also without finiteness of the hom-sets, for total
   categories, and in setting (S) with (Rig); and prove or refute "(P) implies total". The converse fails: finite
   sets and injections are exact over `Q` and over no `F_p` (Lead 5).
5. Over `C_δ^op`: write the diagram `X ↦ Hom(coker D_X, F_p)` of finite `F_p`-vector spaces of R3, the torsor
   diagram under it that has no point, and prove `lim^1 ≅ F_p` from the cocycle; the same for `Hom(coker D_X, R/Z)`
   with `lim^1 ≅ R/Z`. Then prove or refute: a non-empty connected category with I is quasi-filtered iff every
   `A^op`-diagram of non-empty finite sets of bounded size has a non-empty limit (R7 is one direction).
6. Prove or refute (conference item FE-3): if `F, F'` are diagrams of finite-dimensional `F_p`-vector spaces on `C_δ^op` with
   `dim F(X) = dim F'(X)` for every object `X`, then `lim^1 F` and `lim^1 F'` have the same dimension. Expected:
   false, by Lead 11; check it, write the two dual diagrams and the cocycle of the non-zero class, and then
   determine `T_1(coker D)` for every objectwise injective map `D` between finite sums of representables in terms
   of the matrix of augmentations of `D`.

**D. The predimension family `C(k, a, b)`, all integers `k ≥ 2`, `a, b ≥ 1`.**

1. Prove or refute Lead 8 (a) by going through every step of T A.21 and T A.30–A.34 for general `(k, a, b)`.
2. Determine, for every `(k, a, b)`, whether `C(k, a, b)` is exact over `Z`, over `Q`, over each `F_p`. Lead 8 (b)
   gives the range `k ≥ 3`, `ak/2 ≤ b < (k−1)a` (not exact) and the range `b ≥ ka` (`Δ_inj`); prove or refute them and
   settle the ranges `b < ak/2` and `(k−1)a ≤ b < ka`.
3. Determine, for every `(k, a, b)`, whether `Aut(M)` is amenable and whether it is extremely amenable; prove or
   refute Lead 8 (c); where a precompact Ramsey expansion is known (orientations: Evans–Hubička–Nešetřil 2019),
   say which statement gives it and what it implies here. Conference item FE-4 (a speculation; decide it clause
   by clause): for a Ramsey expansion class `A*` of `C_δ` (orientations with their closures and a free order) with
   forgetful functor `u: A* → C_δ`: `colim_{A*}` is exact over `Z` (R5); `u` is not homotopy final (it would
   transport exactness); and `T_1(Q_R) ≅ R` is the image of the first homology of the comma categories of `u`
   under an edge map of the spectral sequence `L_p colim_{C_δ} ∘ L_q u_! ⟹ L_{p+q} colim_{A*}`. State the last
   clause precisely (the comma categories `u/X` of `u_!`, the coefficients) before deciding it.
4. Compare with A.3: every `(k, a, b)` with `b < (k−1)a` for which `C(k, a, b)` is exact over `Q` refutes A.3 (i); say
   for each whether this happens.
5. Prove or refute Lead 8 (d), and decide exactness over `Q` of the category of the unordered class of `C_δ`.

**E. The three regimes.**

1. Prove or refute Lead 9 (1), with the exact hypotheses (complete metric groups; surjective or dense transition
   maps), and identify the image of `lim^1 ker(d_n)` in `coker(d)` with `closure(im d)/im d` or give the exact
   difference.
2. Prove or refute Lead 9 (2) and (3).
3. Decide whether (1) extends from towers to all directed index sets, countable and uncountable, and give the
   counterexample completely where it fails.
4. Place the two model cases of Lead 9 and the diagram of C.5 in the statement, with the operator `d`, the gap at
   each level and in the limit, and the obstruction group.
5. Prove (conference item FE-5): over a countable directed set, `lim^1` of a diagram of countable abelian groups
   is zero or uncountable (for towers: Gray 1966, to be opened); and `lim^i`, `i ≥ 1`, vanishes on diagrams of
   compact groups over every directed set. Hence a non-zero finite `lim^1` on a diagram of finite groups occurs
   only over a non-directed index.

**F. Literature and the statement for the companion.**

1. For each of the following, open the source and give the exact statement with its number, or say that the
   statement is not there: (St), (Op) and weak elimination of imaginaries for free amalgamation classes and for
   Hrushovski constructions (Conant 2017; Evans–Ghadernezhad–Tent 2016; Macpherson–Tent 2011); amenability, unique
   ergodicity and EPPA (Kechris–Rosendal 2007; Angel–Kechris–Lyons 2014; Kechris–Sokić 2012; Zucker 2016); the
   topos of a Fraïssé class (Caramello 2008); smooth representations of `Aut(M)` and their coinvariants (Tsankov
   2012 and what you find); exact colimits (Oberst 1968; Isbell 1974; Isbell–Mitchell 1973, 1976). Say for Leads 1,
   3 and 7 and for A.3 whether the statement or an equivalent one is in the literature, with what you searched.
2. State as theorems, in the form the companion to *Les Dérivateurs* can print at II ms. 36ter: the chain of R1 with
   its witnesses, and beside it the table of the classes of A.4 and of Part D with the columns filtered, exact over
   `Z`, exact over `Q`, total, quasi-filtered, Ramsey, `G` amenable, each entry with the number of the statement that
   proves it.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: quantifiers, the ring of coefficients, variance, which hypotheses of
   the list (Rig), (SA), (FA), (FA∅), (St), (Op), (WEI), (Fin) are assumed. Do not replace it by a convenient special case. If you prove a
   special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property
   you use (strong or only an embedding; natural in which variable; continuous for which topology; equivariant for
   which group). Compositions must type-check; an element of a colimit is a finite sum of classes of elements at
   possibly different objects.
3. Every reduction ("we may assume", "replace by") comes with its comparison map and a proof that the exact
   property needed transfers in the direction needed. Passing to a skeleton, to `A_M`, to a cofinal family of strong
   subsets, to a dense subgroup, to a reduct or an expansion, to a dual diagram or to a finite stage transfers
   nothing by itself.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories; weak equivalence of
   a specified map; isomorphism of topological groups and of abstract groups; a limit in compact spaces and a
   limit of underlying sets.
5. Check the edge cases in scope: the empty structure and the empty base of an amalgam; classes with and without
   rigidity; infinite hom-sets; infinite languages; limits that are not `ω`-categorical; the zero ring; `F_2`;
   uncountable index sets in Part E.
6. A counterexample is given completely and, when finite or finitely presented, checked by a program whose code
   and output you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone
   shows a gap, not falsity; keep the two apart.
7. No authority. Grothendieck's assertions, the return TOTAL_EXACT_2, its intake and referee reading, the results
   R1–R12, the cited papers and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the
   Leads in full. If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails,
   and you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

## What to deliver

One ZIP containing:
- `FREX_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Refuted / Known (with citation), with complete proofs; English, first
  person plural; quote Grothendieck in French where his wording matters.
- `FREX_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `FREX_references.bib`: each entry marked opened / not opened.
- `FREX_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed, every correction to R1–R12, to the Leads, to the
  return TOTAL_EXACT_2, to its referee reading and to the transcription.
- `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

If the execution environment disconnects: wait and retry for ten minutes; then write every file out in the chat in full, each in its own code block, and continue the remaining parts in the chat until every part is written.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `FREX_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
