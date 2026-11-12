# TOTASPH (return 2): review at effort max

Reviewer: Claude Fable 5.2 (Anthropic), effort max, 12 Nov 2026. Return reviewed: GPT-6 Astra (OpenAI, ChatGPT
Pro mode), `pro_returns_20261110\2_TOTAL_ASPHERICITY\TOTASPH\` (107 numbered statements; its own labels: 84 Proved,
11 Refuted, 10 Known, 2 Open).

Read before reviewing: Grothendieck II ms. 1–53 (II-a in full) and the statements of II §7; XII ms. 59–169
(XIIb-a, XIIb-b in full); the appendix to XII (ms. 1–18, in full); I ms. 1–66. Literature opened for this review is
listed in `..\DERIVATEURS_EXPERT\READING_BASE.md`, §1. No earlier review was consulted.

Verdict vocabulary: **correct** (the statement is true and the return's argument proves it, or I supply the
proof); **gap** (true as far as I can see, but the return's argument is incomplete at the place named); **wrong**
(false, or the label is wrong); **unproved** (neither the return nor I have a proof). Each verdict carries my own
argument or an exact citation that I opened. "Known to Grothendieck" means the manuscript already has the
statement or the example, with location.

Conventions as in the return: `W` a fundamental localizer in the sense of Cisinski 2004, Déf. 1.1.3 (LF1–LF3;
checked in the source); `T_W(A)`: `A` totally `W`-aspherical (XII ms. 88–89, Définition 1); "final" = Grothendieck's
"cofinal" (II Déf. 3.3: all `b\A` 0-connected).

## Part A. Definitions and the formal theory (A.1–A.16)

| Item | Verdict | Argument |
|---|---|---|
| A.1 (definition of fundamental localizer; "Known") | correct | Agrees word for word with Cisinski, *Le localisateur fondamental minimal* (Cahiers 45 (2004)), 1.1.1 (FS1–FS3) and Déf. 1.1.3 (LF1–LF3); I opened the paper. It is XII's W(1), W(2 bis), W(3). |
| A.2 (Définitions 1, 2 and the Dwyer-type notions) | correct | Compared with XII ms. 88–89 and ms. 109–110: `H` total iff every `U'/p_!H` is `W`-aspherical; strict = the presheaves `Hom(f−, y)`, total = the categories `X/y`; dwyérienne = `U → Ū` strict. The variance (presheaves; `U/H` a discrete fibration) is the manuscript's. |
| A.3 (comprehensive factorization `A → B/P_f → B`, `P_f(b) = π_0(b\A) = f_!1_A`) | correct | Own check: a morphism `(b, c) → q_f(a)` in `B/P_f` is `β: b → fa` with `[a, β] = c`, so `(b, c)\A` is the component `c` of `b\A`: non-empty, connected. Uniqueness: for `E = B/Q` and `q` final, `f_!1 = r_!q_!1 = r_!1_E = Q`. This is the factorization Grothendieck describes at XII ms. 91–93 ("il doit être facile"). |
| A.4 (`T_W(A)` ⇔ every final image of `A` is `W`-aspherical; stable under final images) | correct | Immediate from A.3 and composition of final functors. Equivalent to the reformulation in Grothendieck's question at II ms. 36. |
| A.5 (`U/H → U'/p_!H` is final; total presheaves are stable under `p_!`) | correct | `π_!1_{U/H} = H` since `u\(U/H)` is a disjoint union over `H(u)` of categories with initial objects. This is Prop. 8 and the Lemma of XII ms. 112. |
| A.6 (final image of a filtered category is filtered) | correct | The equalizing step is right: connect `(a, vs)` and `(a, vt)` in `b\A` by a zigzag and take a cocone. It is II Cor. 3.4 c) of the manuscript. |
| A.7 (filtered ⇒ total for every fundamental localizer; "Known") | correct | `W∞ ⊂ W` by Cisinski 2004, Théorème 2.2.11 (opened: "Les ∞-équivalences forment le localisateur fondamental minimal"); filtered categories have contractible nerve (Quillen 1973, §1, Cor. 2 to Prop. 3). **Sharpening of the manuscript:** II Cor. 2.16–2.17 assume the limit axiom Loc (8); it is not needed. |
| A.8 (invariances) | correct | Equivalences of categories are final in both directions; the rest are quantifier checks. Non-invariance under `W∞`-equivalence: `Ψ → e` (see A.16). |
| A.9 (W(7 bis), W(7) as stated in XII) | correct | Matches XII ms. 75–77. |
| A.10 (one-point attachment: `BX ≃ hocolim(BU ← B(U/H) → pt)`, with an explicit model `M → X`) | correct | I re-derived the two comma categories: `M/u` has the terminal object `(u, id)`; in `M/t` the off-diagonal triples retract onto the `U`-layer, and the remaining category `N` (two copies of `E`, a cylinder, and a cone point) has `Id ⇐ R ⇒ const_t`. Standard collage formula; it is the case `X_1 = e` of Grothendieck's gluing question at XIIapp ms. 17–18. |
| A.11 (Prop. 7 and the Corollary of XII ms. 85 under the full W(7 bis)) | correct | Follows from A.10 and W(7 bis) applied to the cover `M = M_U ∪ M_t`. Grothendieck's own footnotes 104–105 (XII ms. 149, 151) already say the strong form is needed. |
| A.12 (a 35-object, 159-arrow category `A`, acyclic, `π_1 ≠ 1`) | correct | Own check of the data: 3 + 17 + 15 simplices; arrows 35 + 34 + 45 + 45 = 159; nerve ranks (35, 124, 90). `d_2 = [[5, −2], [−3, 1]]`, determinant −1 (exponent sums of `a⁵b⁻³` and `b³(ab)⁻²`). In `A_5`: `a = (1 4 3 2 5)`, `b = (1 2 3)`, `ab = (1 5)(3 4)` (I composed them), so both relators die and `a ≠ 1`. Hatcher's Example 2.38 is the binary icosahedral presentation. |
| A.13 (**`W∞` satisfies neither W(7 bis) nor W(7)**; the one-point converse fails) | correct | `X = A ⋆ {u, t}`: `U = A ∪ {u}`, `V = A ∪ {t}` are sieves with contractible nerves, `BX = ΣBA` is contractible (simply connected and acyclic), `U ∩ V = A` is not. I had found the same counterexample independently while reading XII ms. 78. **This refutes XII Théorème 2 (ms. 78)** as stated; only the direct halves hold. Consequence I add: in II ms. 36ter (Contre-exemple 2.20) the step "`i ∈ W∞` ⇒ `X/H` aspherical" is not available; one gets only that `X/H` is connected and acyclic. The counterexample 2.20 survives (take `H` connected with `ΣB(Δ/H)` not contractible). |
| A.14 (`W_R` satisfies W(7) and W(7 bis)) | correct | For a cover by two sieves every chain of arrows lies in the piece containing its last object, so Mayer–Vietoris is a short exact sequence of normalized chain complexes; cones and the five lemma. |
| A.15 (Prop. 8 and 9 (a)) | correct | As in the manuscript (XII ms. 93, 97); `f_!1_V = B(−, f(v_0))` for `v_0` final. |
| A.16 (Prop. 9 (b), its "rectification" and the fork corollary are false, also for `W_R`) | correct; known to Grothendieck | The final functor `Ψ → C` with `BC ≅ S²` is Grothendieck's own `Ψ → Z` of XIIapp ms. 10–12 (same six-arrow category; his footnote 7 gives the type `S²`), and his footnotes at XII ms. 97–100 already mark 9 (b), Cor. 1 and Cor. 2 "Faux". What the return adds: the failure persists under the full W(7 bis) (for `W_R`, `R ≠ 0`), and the precise failing step (a retraction of categories is not a map of subterminal presheaves; `j_!` does not preserve the monomorphism `Ψ(−, z) → Ψ(−, a)`). Both additions are right. |

## Part B. Collages, the three leads, final-image tests (B.1–B.11)

| Item | Verdict | Argument |
|---|---|---|
| B.1 (Lead 1: `A → A_K` final iff `El_A(K)` non-empty connected; `N(A_K) ≅ NA ⊔_{NE} (Δ⁰ ⋆ NE)`) | correct; known to Grothendieck in the dual form | Own check of the isomorphism of simplicial sets: a simplex not in `NA` is `x → … → x → a_0 → … → a_n`, i.e. a simplex of the cone on `NE`, with the face deleting the last `x` equal to `Nπ`. The test itself is Grothendieck's Contre-exemple 2.20 (II ms. 36bis–36ter: adjoin a closed final point by a presheaf `H`); the prompt's "Lead 1" did not say so. |
| B.2 (if `BA ≃ pt` and `E` connected: `B(A_K) ≃ ΣBE`, contractible iff `E` acyclic) | correct | Suspension of a connected complex is simply connected; Hurewicz. This is the precise replacement for the step of II ms. 36ter that quotes XII Th. 4 Cor. 4. |
| B.3 (iteration of collages, transfinite) | correct | A.4; at limits, `b\A` is already the comma category at the stage where `b` appears. |
| B.4 (Lead 2: `H_1(El_A(H); Z) ≅ Z/I` for `H = h_p/(ca ∼ cb)`) | correct | I re-derived it: with `d: P_q → P_p`, `c ↦ ca − cb`, `J = im d`, `K = ker d`: `L_1colim Z[H] ≅ colim J` because `colim J → colim P_p` vanishes, and `colim J = coker(colim K → Z)`, whose image is generated by the augmentations of the syzygies. |
| B.5 (Lead 3: `M = {1, e, f}`, `uv = v`; `B El_M(K) ≃ S¹`, `B(M_K) ≃ S²`) | correct | Checked by hand: `me = e` for all `m` gives `const ⇒ id`, so `BM ≃ pt`; no `c` with `ce = cf`; `El_M(K)` is the collage of `M` at `i` with the constant two-point functor, whose category of elements is `M ⊔ M`; two applications of B.1. |
| B.6 (bands `(I × J)¹`: filtered ⇔ total ⇔ `|J| = 1`) | correct | `c·(i, j) = (c_1, j)`: two elements are equalized by left multiplication iff they have the same second coordinate (and `c·1 = c·(i, j)` for `c = (c_1, j)`). For `|J| ≥ 2` the surjection onto `{1, e, f}` is a homomorphism for `uv = v`, and a surjective monoid homomorphism is final. |
| B.7 (congruence quotients, localizations, `A → Kar(A)` are final) | correct | Each comma category has an object mapping to all others (`(b, id)`; for `Kar`: `(a, e)` via `v = ve`); for localizations a zigzag read off a word. |
| B.8 (`T_W(A) ⇔ T_W(Kar A)`) | correct | Checked the two steps: `Kar(f)` is final when `f` is (compose a connecting zigzag in `b\A` with `d` on the right), and `B → Kar(B)` has comma categories with a cone from a constant functor to the identity, so it is in `W∞ ⊂ W`. |
| B.9 (remark on what the tests force) | correct | Summary of B.7–B.8. |
| B.10 (infinite fence: contractible, not total) | correct | 1 and 3 have no common successor; C.11 (verified below) then excludes totality. The statement about zigzags of natural transformations is CATHOT C.5; not re-checked by me beyond the distance argument given, which is sound. |
| B.11 (for `A` non-empty connected: `T_{W∞}(A)` ⇔ `hocolim_A K → colim_A K` is a weak equivalence for every `K: A → sSet`) | correct | Levelwise this is C.5 (4) for the functors `K_q`; diagonal lemma. Conversely take `K` discrete. **This is the conceptual content of total asphericity:** ordinary colimits over `A` of simplicial sets are homotopy colimits. Scope: simplicial sets and their colimit in `sSet`. For `Cat`-valued diagrams and the colimit in `Cat` the statement fails (`D([n]) = N^{[n]}` over `Δ_inj`: `colim_Cat D = N`, of type `S¹`, while `H_q(B∫D) = Z` for all `q`); this caveat is from the earlier review and I re-derived it (FINDINGS F2-13). |

## Part C. The main theorem (C.1–C.14)

| Item | Verdict | Argument |
|---|---|---|
| C.1 (properties `P_R(A)`, `P_∞(A)`: every component of every `El_A(H)`, `H: A → Set`, is `R`-acyclic, resp. weakly contractible) | correct (a definition) | — |
| C.2 (homological Theorem A in the final variance, with a range) | correct | Standard spectral sequence of the bisimplicial set of strings `b_0 → … → b_p → f(a_0), a_0 → … → a_q`; rows are the homology of the `b\A`. |
| C.3 (components of `El_A(H)` inherit `P_R`, `P_∞`) | correct | `El_E(K) ≅ El_A(L)` with `L(a) = ⊔_{h ∈ H_E(a)} K(a, h)`; checked. |
| C.4 (a connected `E` with `P_Z` is weakly contractible) | correct | The covering of `BE` with group a cyclic subgroup `K ≤ π_1` is `El_E(H_K)` for `H_K(e) = Hom_{ΠE}(e_0, e)/K`; `P_Z` gives `K = K_ab = H_1 = 0`. Then acyclic and simply connected. |
| C.5 (**characterization: `T_{W∞}(A)` ⇔ `T_{W_Z}(A)` ⇔ `A` non-empty, connected, `P_Z` ⇔ … `P_∞`**) | correct | I followed all four implications. (2) ⇒ (3): the collage of a connected `El_A(H)` is a final image, and the cofibre sequence of B.1 kills its reduced homology; (3) ⇒ (4) by C.3 and C.4; (4) ⇒ (1): for `f` final each `b\A = El_A(Hom(b, f−))` is contractible, Quillen's Theorem A. Before reading the return I had only the direction (4) ⇒ (1) and acyclicity in (1) ⇒ (3); the covering trick of C.4 is what makes the criterion exact. |
| C.6 (`colim_A` exact on `Ab^A`, `A` non-empty connected ⇒ `T_{W∞}(A)`) | correct | `colim_{El_A H} F = colim_A Σ_H F` with `Σ_H` exact; `L_j colim_E Z = H_j(BE)`. |
| C.7 (definition of `Δ_inj`) | correct | — |
| C.8 (interpolation on coordinate hyperplanes) | correct | Verified the inclusion–exclusion: `ρ_j(C) = ρ_j(F_j)` because the terms `S` and `S ∪ {j}` cancel. |
| C.9 (affine cones in `Δ_inj`: `t ∈ Z[Hom([n], [M])]` of augmentation 1 with `th = th'` for all parallel `h, h'`; `M = 2^{n+1} − 2`) | correct, but **known**: Isbell–Mitchell, *Exact colimits*, Bull. AMS 79 (1973) 994–996, Theorem 3 ("aff Δ is filtered"), with the same size `2^{n+1} − 1` of the target | I verified the return's proof line by line (gap monomials: `P_{tδ^i} = y_i D_i(P_t)`; the compatibility `D_{j−1}(F_i) = D_i(F_j)` in both cases; value 1 at the all-ones point; degree `k(2^{n+1} − n − 2)`), and the case `n = 1` by hand: `t = (1,2) − (0,2) + (0,1)`, `tδ⁰ = tδ¹ = [1]`. I also opened the 1973 note (free at ams.org), which the return did not: it states the theorem and sketches a different, combinatorial proof. The label "Proved" should read "Known (Isbell–Mitchell 1973, Th. 3); independent proof". |
| C.10 (**`Δ_inj` is totally `W∞`-aspherical, has exact abelian colimits, is not filtered; Lead 4 and row II-C-003 refuted**; labelled "Refuted") | correct | `Aff_Z(Δ_inj)` filtered ⇒ `colim` exact: I checked this direction directly (`colim_A F = colim_{Aff A} F̃`, since `x − (Σ n_c c)x = Σ n_c (x − cx)`); it is the "if" part of Isbell–Mitchell's Theorem 1. Then C.6. Not filtered: `d⁰, d¹: [0] → [1]` are never equalized. **So the conjecture Grothendieck states at II ms. 36ter is false, and the counterexample is the Isbell–Mitchell category of 1973**; what is new is the identification of total asphericity (C.5) that makes the old example apply. Independent evidence of mine: for several explicit `H` on `Δ_inj` I computed `El(H)` by hand before reading the proof (subfunctors and quotients of `h^0`, `h^1`; all components came out contractible). |
| C.11 (total ⇒ non-empty, common successors, affine equalizers of parallel pairs) | correct | The double of `A` along `U_a ⊔ U_b` has `H_1 ≠ 0` by Mayer–Vietoris when the two cosieves are disjoint; the rest is B.4 with `I = Z`. |
| C.12 (monoids: if for all `x, a` some `t` of augmentation 1 has `tx = txa`, then `M` is filtered) | correct | Checked the measure argument: an invariant finitely supported signed measure of a self-map lives on cycles and is constant on them, so its mass is a combination of cycle lengths; minimal-period descent by a prime; then `zya = zy = zyb`. This is the argument of Isbell 1968 / Isbell–Mitchell 1973, Theorem 2, under a weaker hypothesis. |
| C.13 (**with a weakly terminal object — in particular monoids, finitely many objects, finite categories — total ⇔ filtered**) | correct | From C.11 and C.12; the passage from the monoid `End(q)` to all parallel pairs is right (`z c_i = z` for the finitely many `c_i` in the support). Parallels Isbell–Mitchell 1973, Corollary 1 (exact + weak terminal ⇒ filtered), here from totality alone. |
| C.14 (`Δ_inj` is not sifted) | correct | Cospans `[0] → [n] ← [0]` have three components (`<`, `=`, `>`). |

## Part D. Other localizers (D.1–D.21)

| Item | Verdict | Argument |
|---|---|---|
| D.1 (`W_R` is a fundamental localizer) | correct | Relative Theorem A by the two spectral sequences of the bisimplicial set of strings `a_0 → … → a_q, f(a_q) → c_0 → … → c_p`; standard. |
| D.2 (`T_{W_R}(A)` ⇔ `A` non-empty, connected, `P_R(A)`; `T_{W_Z} = T_{W∞}`) | correct | Same proof as C.5 with C.2 in place of Theorem A. |
| D.3 (`Aff_R(A)`) | correct (definition) | Isbell–Mitchell's "affinization" for `R = Z`. |
| D.4 (`colim_A` exact on `R-Mod^A` ⇔ the components of `Aff_R(A)` are filtered) | correct; **known** for `R = Z`: Isbell–Mitchell 1973, Theorem 1 | I checked both directions of the return's proof. "If": `colim_A F = colim_{Aff A} F̄`. "Only if": common successors from `colim(R_a ∩ R_b) = R`; for parallel affine `α, β` the class of `δ = α − β` in `colim I` vanishes, and pushing the witnessing relation to a common successor gives `t = d_q − Σ r_{jl}(d_{t_j}v_j − d_{s_j})c_{jl}` of augmentation 1 with `tδ = 0`. The 1973 note proves the same through purity; the return's direct argument is self-contained and right. |
| D.5 (exact `R`-module colimits, `A` non-empty connected ⇒ `T_{W_R}(A)`) | correct | As C.6. |
| D.6 (the "literal" `W_Z` half of Lead 4 fails for disconnected or empty `A`; "Refuted") | correct | Two points with identities: exact colimit, not acyclic. A defect of the lead's wording only. |
| D.7 (**Open**: does `T_{W∞}(A)`, `A` connected, imply exactness of `colim_A` on `Ab^A`, i.e. `Aff_Z(A)` filtered?) | unproved; the status "Open" is right, and I could not close it | My attack. (a) Placement: `Aff_Z`-filtered ⇒ total ⇒ quasi-filtered, where "quasi-filtered" (Adámek–Reiterman) = spans complete (D.16) + every parallel *pair* has an affine equalizer (C.11); by Adámek–Reiterman 1976 / Adámek–Koubek–Reiterman 1981, Theorem [1] (p. 369, opened) quasi-filtered ⇔ every connected `H: A → Set` has the fixed-point property (the return's D.17). So the question is where totality sits between the Isbell–Mitchell class and the Adámek–Reiterman class, which are different (D.18). (b) With a weakly terminal object all three coincide with "filtered" (C.13 uses only quasi-filteredness). (c) Reduction: by Isbell–Mitchell's Lemma 1 it suffices to equalize finite families of ordinary parallel arrows; for a triple `a_0, a_1, a_2: p → q` with `K_i = {t : t(a_i − a_0) = 0}` I get that a simultaneous affine equalizer exists iff `aug(K_1 ∩ K_2) = Z`, and that `Z/aug(K_1 ∩ K_2)` is a quotient of `Tor_1(ΔZ, P_q/(K_1 + K_2))`; totality gives `Tor_j(ΔZ, Z[H]) = 0` only for permutation modules `Z[H]`, and `P_q/(K_1 + K_2)` is not one. (d) Evidence that totality is much stronger than quasi-filteredness: when a new maximal object `Z` is adjoined, `B El` changes by a cone on `B(old ↓ Z)`; for a freely adjoined quasi-filter of a pair of arrows `W ⇉ X` into an already contractible stage, `(old ↓ Z)` is a necklace of contractible pieces, a circle, so a 2-sphere is created. Hence the free construction `K*` of Adámek–Koubek–Reiterman (Part C) is very unlikely to be total, and it does not decide D.7. My hunch (recorded as H1 in `HUNCHES.md`): total ⇔ `Aff_Z`-filtered. |
| D.8 (groups: `T_{W_R}(G)` ⇔ every subgroup is `R`-acyclic; finite `G`: ⇔ `|G| ∈ R^×`) | correct | Components of `El` of a `G`-set are the orbit groupoids ≃ stabilizers; `H_1(C_p; R) = R/p`. |
| D.9 (`W_n`) | correct | Standard; the localizers of `n`-equivalences. |
| D.10 (a final functor is bijective on `π_0` and surjective on `π_1`) | correct; known to Grothendieck | XII ms. 101 (coverings pull back fully faithfully along a functor with 0-connected `y\X`). |
| D.11 (`T_{W_0}`: non-empty connected; `T_{W_1}`: simply connected) | correct | D.10. Answers the prompt's "for `W_0` the notion is elementary". |
| D.12 (`n ≥ 2`: `T_{W_n}(A)` ⇔ `BA` `n`-connected and every component of every `El_A(H)` `(n−1)`-connected) | correct | Checked: necessity by the cofibre sequence of the collage, inheritance (C.3) and the cyclic-cover argument (needs `n − 1 ≥ 1`); sufficiency by C.2 with `d = n`, D.10 and Hurewicz. |
| D.13 (`n ≥ 2`, weakly terminal object: `T_{W_n}` ⇔ filtered; false for `n = 1`) | correct | C.11–C.13 use only `H_1 = 0` of connected categories of elements. So for finite categories "totally 2-connected" already means filtered. Relevant to Grothendieck's footnote 42 at II ms. 36 ("c'est 2-connexe qu'il faut lire"): with 2-connected in place of aspherical his conjecture is true for categories with a weakly terminal object and (by C.10 and D.12) false in general. |
| D.14 (monotone in `W`; `T_{W∞}` is not invariant under weak equivalence) | correct | `{1, e, f} → e`. |
| D.15 (zero ring) | correct | Trivial. |
| D.16 (`T_{W∞}(A)` ⇒ `colim_A: Set^A → Set` preserves monomorphisms; spans complete to commutative squares) | correct | Common successors inside the (total) component of `El_A(H)`; `El_A(K)` is a cosieve in `El_A(H)`. **Settles half of Grothendieck's second Question at II ms. 36** ("`X` totalement `W∞`-asphérique ⟹ `X°` totalement 0-connexe? Ou du moins implique PS 1′?"): PS 1′ holds (C.11), and even PS 1 in its dual form (D.16); `X°` totally 0-connected (= `X` sifted) fails for `Δ_inj` (C.14). The return does not point this out. |
| D.17 (fixed points: for `A` total and `El_A(H)` connected, every natural endomorphism of `H` fixes an element) | correct | Checked: without periodic points `colim_A` of the nerves of the `N`-actions is `BN ≃ S¹` while the quotients have colimit a point, contradicting B.11; then the least period `r` gives `BC_r ≃ pt`. This is the fixed-point property of Adámek–Reiterman; by their Theorem [1] it is equivalent to quasi-filteredness. |
| D.18 (the fixed-point condition does not imply exactness; "Known") | correct | I opened Adámek–Koubek–Reiterman, Czech. Math. J. 31 (1981) 368–389 (dml.cz): §A.4, p. 370, corrects the remark of Adámek–Reiterman 1976; Construction C.1 and Theorem C.2, pp. 384–385: `K*` is quasi-filtered and no affine `ρ` has `ρv_1 = ρv_2 = ρv_3`. The return's citation is exact. |
| D.19 (`W_1 ⊂ W` ⇒ `T_W(A)` ⇔ `A` is `W`-aspherical) | correct | Final functors are surjective on `π_1`; the argument reduces to the pushout of a surjection of skeletal groupoids along `S → e`, which is `e`, and uses F.30 (object-injective functors are `W`-cofibrations when `W_1 ⊂ W`), checked in Part F. |
| D.20 (`W_1 ⊂ W`: `H` total ⇔ `U/H` `W`-aspherical ⇔ `T_W(U/H)`; the strict and total notions coincide) | correct | Follows from D.19 and A.5. |
| D.21 (`W_1 ⊂ W`: Dwyer-type sieves closed under composition ⇔ every non-empty category is `W`-aspherical) | correct | D.19, D.20 and the lower-copy construction of F.9. |

## Part E. Presheaves (E.1–E.8)

| Item | Verdict | Argument |
|---|---|---|
| E.1 (`T_W(U/H)` ⇒ `H` total; converse for subterminal `H`) | correct; known to Grothendieck | Prop. 8 and the remark at XII ms. 96. The pushout of a sieve along any functor is a sieve (XII Prop. 5), so `D_f = U'/p_!H`. |
| E.2 (for an idempotent `d` on `c`, `Q_d = {α : dα = α}` is a split subpresheaf of `C(−, c)` and `C/Q_d` is filtered) | correct | `(c, d)` is weakly terminal in `C/Q_d` and `β: (w, β) → (c, d)` equalizes any parallel pair into `(w, β)`. |
| E.3 (**row B035 refuted**: on the monoid `{1, e}`, `H = R ⊔_Q R = {i, h_1, h_2}` is totally `W∞`-aspherical and `U/H` is not) | correct | Checked: `Q` is the image of the idempotent endomorphism `x ↦ ex` of the representable `R`, so for every `p` one gets `p_!H = C(−, c) ⊔_{Q_d} C(−, c)`; its category of elements is two copies of `C/c` (terminal objects) glued along the filtered `C/Q_d`: contractible. `U/H` has objects `i, h_1, h_2`, an idempotent on `i` and arrows `i → h_j`; `h_1, h_2` have no common successor, and `U/H → Ψ → Z` is final onto a category of type `S²`. This is the example Grothendieck could not find (XII ms. 96–97: "je me vois mal construire un exemple"). |
| E.4 (classification on the base `{1, e}`) | correct | `H(e)` is an idempotent map; one fixed point is forced by connectedness; the gluing argument of E.3 iterates. With two elements the non-fixed one is terminal in `U/H`. |
| E.5 ("`H` total ⇒ `U/H` total" holds for all `U, H` iff `S²` is `W`-aspherical) | correct | "Only if": E.3 gives `U/H → Z` final with `Z ≃ S²`. "If": `S²` aspherical ⇒ `W_1 ⊂ W` (F.28–F.29, checked below) and then D.19–D.20. |
| E.6 (`U/H` filtered ⇔ `H` is a filtered colimit of representables; sufficient for totality) | correct; known | SGA 4 I 8; II Cor. 2.18 of the manuscript. |
| E.7 (Lead 5 refuted: ind-right adjoint ⇔ all `U/x` filtered; dwyérienne sieves need not have one) | correct | The two counterexamples are right: `{1, e}` with crossing presheaf `H` of E.3 (strictly, not totally dwyérienne), and `Δ_inj ⊂ Δ_inj^▷` (totally dwyérienne, crossing category total and not filtered). |
| E.8 (restricted-action criterion: `H` is totally `W_R`-aspherical iff `E = U/H` is `R`-acyclic and every component of `El_E(L∘π)`, `L: U → Set`, is `R`-acyclic; for `W∞`: `BE` contractible and those components `Z`-acyclic) | correct | Necessity: the collage `U → U_L` gives `(p_!H)(x) = π_0 El_E(Lπ)` and the category of elements is `E` with cones on the components. Sufficiency: for any `p`, the comma categories of the final `E → U'/p_!H` are components of `El_E(L_{u'}π)`, `L_{u'} = Hom(u', p−)`; C.2; for `W∞` also D.10. In other words: `H ⊗^h_U L → H ⊗_U L` is a homology equivalence for all `L`. |

## Part F. Dwyer-type immersions (F.1–F.31)

| Item | Verdict | Argument |
|---|---|---|
| F.1 (definitions; W-cofibration = h-cofibration of Batanin–Berger for the class `W`) | correct | Matches XII ms. 109–110. Batanin–Berger's Definition 1.1 not re-opened by me; the identification is by definition (pushout functor preserves weak equivalences). |
| F.2 (both dwyérienne classes are stable under cobase change; **every `W`-dwyérienne sieve is a `W`-cofibration, for every fundamental localizer**; `p ∈ W ⇒ q ∈ W`, `i ∈ W ⇒ i' ∈ W`) | correct; sharpens the manuscript | Grothendieck's Corollaire 1 (XII ms. 108) assumes W(7). The return needs only forward gluing: `C → C̄` is `W`-aspherical (LF3), `X ⊔_U C = C̄ ∪ T` over `Ṫ` is a cover by two cosieves, and a map of such covers that is in `W` on the three pieces is in `W` (Grothendieck's own Th. 4 Cor. 3, which by his footnote needs no extra axiom; fibrewise equivalences of integrals, Cisinski 2004, 1.1.13). I checked each step. |
| F.3 (couniversal `W`-equivalence ⇔ `W`-cofibration and in `W`; closure properties) | correct | "⇐" uses Thomason's factorization `p = wj` and Cisinski 1999, Proposition 2 ("toute cofibration de Cat est un rétracte d'un morphisme de Dwyer"; opened), then two-out-of-three. Grothendieck has only "⇒" (ms. 110). |
| F.4 (Théorème 3 (a), (b) and Corollaire 2 under W(7 bis), W(7)) | correct | As in the manuscript; holds for `W_R` (A.14), not for `W∞` (A.13). |
| F.5 (for `W∞`, `W_R`: components of discrete opfibrations over a total category, non-empty cosieves of it, and integrals of total categories over a total base are total) | correct | From C.5/D.2. A non-empty cosieve is connected by common successors (C.11), and it is a category of elements of an indicator functor. |
| F.6 (**totally `W`-aspherical functors and totally `W`-dwyérienne sieves compose, for `W∞` and `W_R`**; rows C045, C047, total half) | correct | Functors: `∫_{Y/z} X/y → X/z` has a left adjoint section, so it is final. Sieves: the cosieve `S_y ⊂ X/y` of objects with non-empty `U/x` and the same integral. Checked. Answers Grothendieck's doubt at XII ms. 113–114 positively for the total notions. |
| F.7 (**for every fundamental localizer: `f` strictly `W`-aspherical ⇒ `f^*` preserves total presheaves; strictly `W`-aspherical functors compose**) | correct | Checked the collage argument: `Z = X' ∪ Y` with `Hom(x', y) = Q_y(x')`, `F = j_!H`, `F|X' = p_!f^*H`; the sieve `X'/K → Z/F` has slices `X'/Q_y` (aspherical) or with terminal object, so it is in `W` by LF3. |
| F.8 (for every `W`: totally `W`-aspherical functors compose; integrals of total categories over a total base are total) | correct | `f_z: X/z → Y/z` has comma categories `X/y`, so it is total, hence strict, and F.7 applies to the terminal presheaf of `Y/z`. For integrals, `D(b) → E/b` is a right adjoint, hence final. |
| F.9 (totally `W`-dwyérienne sieves compose ⇔ non-empty cosieves of totally `W`-aspherical categories are totally `W`-aspherical; finite case for `W_n`, `n ≥ 2`) | correct | The lower-copy construction (`V_0 ⊂ X = A ∪ V_0` classical Dwyer, `A → X` a right adjoint hence final, then adjoin a terminal object) is right; I checked the boundary categories of the composite. |
| F.10 (for `W_0`, `W_1` neither dwyérienne class of sieves is closed under composition; "Refuted") | correct | `V` = two points, resp. two parallel arrows; `B = V^◁` is contractible, hence total for `W_0`, `W_1` (D.11); the composite has boundary category `V`. Six objects. So C045 is false for general `W`. |
| F.11 (`W_R`: restriction of a total presheaf to a cosieve, if non-empty, is total) | correct | Checked the double collage: `q: U → C^◁`, `F = q_!H` with `F(0) = pt`, then the functor `L` with two points at 0: the result has the type of `Σ²B(C/K)`. |
| F.12 (`W_R`-dwyérienne sieves compose) | correct | F.11 and F.7. |
| F.13 (discretely flat functors; "Known") | correct | Hackney–Ozornova–Riehl–Rovelli, arXiv:2205.02353, Definition `discretely flat` (opened in the TeX source: pushout along `c_*I` preserves Bergner weak equivalences; cofibration = injective on objects; inclusion = also faithful). |
| F.14 (a sieve is discretely flat iff every `H_t ⊗_U −: sSet^U → sSet` preserves objectwise weak equivalences; totally `W∞`-dwyérienne ⇒ discretely flat; discrete source ⇒ discretely flat) | correct | Hom-objects of the simplicial pushout are the coends; necessity through the simplicial collage `C_K`. The middle claim is B.11 for `A = U/H_t`. |
| F.15 (`H ⊗_U −` homotopical ⇔ every component of every `El_E(Lπ)` is contractible; then `H` total ⇔ `E` non-empty connected) | correct | Two-sided bar construction, as B.11. |
| F.16 (strictly but not totally dwyérienne, and discretely flat: `{1, e}` with `H` of E.3) | correct | `H ⊗_U L = V ⊔_{im d} V` with `im d` a retract of `V`. |
| F.17 (discretely flat ⇒ `W`-cofibration for every `W`; "Known") | correct | The comparison `NX ⊔_{NU} NC → N(X ⊔_U C)` is a weak categorical equivalence for discretely flat cofibrations (HORR, main theorem in its generalized form; the source states it "holds generally for discretely flat cofibrations"; I read the statement, not the proof). For a discrete source I also checked it directly from the gluing formula. |
| F.18 (**row C035 refuted**: `a ⇉ t → s` with `γα = γβ`; `{a} ⊂ X` is a couniversal `W∞`-equivalence and not `W`-dwyérienne) | correct | I re-derived the pushout `P` and the two natural transformations `id_P ⇒ F ⇐ jr` (naturality at `(f, α)` is `γ(f, α) = f`). `U/t` is two points. So the answer to Grothendieck's Question (a) at XII ms. 111 is no, for `W∞`, `W_R`, `W_n`. |
| F.19 (the assertions of XII ms. 111 for a mere `W`-cofibration with `T ≅ e`, and "il s'ensuit tout au moins ceci…", are false; "Refuted") | correct | `{a} ⊂ (a ⇉ t)`: a sieve with discrete source is a `W`-cofibration for every `W` and stays one after every change of the complement, and its crossing presheaf has two elements. Grothendieck's sentence is right for *trivial* cofibrations under the strong W(7 bis) (Corollary of ms. 85) and wrong as he continues it for cofibrations; the return's reading is fair. Holds also for `W_R`, which satisfies W(7). |
| F.20 (one-point attachment: couniversal `W∞`-equivalence ⇔ `H` totally `W_Z`-aspherical; same for `W_R`) | correct | Checked: `π_1(E) → π_1(C)` is trivial for a totally `W_Z`-aspherical presheaf (the covering with cyclic group `K ⊂ im φ` is a restricted action, E.8), then van Kampen and the universal cover. This is the correct form, for `W∞`, of the Corollary of XII ms. 85 in its couniversal version. |
| F.21 (a 4-object sieve that is a couniversal `W∞`-equivalence and not discretely flat) | correct | `U = [1]`; `H_t ⊗ L = CK ⊔_K CK ≃ S²` against `H_t ⊗ M = pt`. |
| F.22 (`N ⊂ N^▷` is totally `W`-dwyérienne, not a Dwyer map) | correct | `N` is filtered without terminal object. |
| F.23 (**the endpoint pushout-product `({0} ⊂ [1]) □ ({0, 2n} ⊂ Φ_n)` is not a `W`-cofibration when `S²` is not `W`-aspherical**; "Refuted") | correct | I followed the computation: `p: A → D = Z^▷` contractible to contractible; the crossing presheaf at `u_1` pushes forward, through the final functors `S → Ψ → Z`, to the subterminal presheaf supported on `Z`; so `Q ≃ Z ⋆ {s, u_1} ≃ S³`; and with `p_0: A → Z` the cobase change `Z → Q_0` goes from `S²` to a contractible category, which (F.3) excludes couniversality when `S²` is not `W`-aspherical. This is the same phenomenon as Grothendieck's Proposition of XIIapp ms. 13 (the boundary of `Φ_n × Φ_m` is not a `W`-cofibration), one dimension lower and with the proof made independent of the strong axiom. |
| F.24 (**C048 = XIIbb-A001**: if `S²` is not `W`-aspherical, a class of sieves made of `W`-cofibrations and closed under `− □ j` contains only isomorphisms) | correct | A sieve with a crossing arrow has `e → [1]` as a retract; retracts of `W`-cofibrations are `W`-cofibrations (F.3) and `□ j` preserves retracts; a sieve without crossing arrows acquires one after `□ j`. So the class Grothendieck asks for at XII ms. 114 does not exist for `W∞`. |
| F.25 (for `W_0` every functor, for `W_1` every object-injective functor, is a `W`-cofibration) | correct | `π_0` and groupoid completion are left adjoints; left properness of the folk structure for groupoids. |
| F.26 (five equivalent forms of the remaining question: `W∞`-dwyérienne ⇒ discretely flat; composition of `W∞`-dwyérienne sieves; totally `W_Z`-aspherical presheaf ⇒ totally `W∞`-aspherical; restriction to cosieves; one-point couniversal recognition) | correct | I checked 1 ⇔ 3 (the presheaf `F` on `V^◁`; components `D_c` as presheaves `H'_c` on `El_U(L)`), 3 ⇒ 4 ⇒ 2 ⇒ 4 ⇒ 3 and 5 ⇔ 3 (F.20). |
| F.27 (**Open**: is every totally `W_Z`-aspherical presheaf totally `W∞`-aspherical, i.e. must `U/H` be simply connected?) | unproved; the status "Open" is right | My attack: (a) true when `U` is a group (all subgroups of the stabilizer must be acyclic), when `H` is subterminal or terminal (C.5), and whenever `π_1(U/H)` is abelian or has a non-trivial cyclic quotient visible in `U`; an obstruction needs `π_1(U/H)` perfect and mapping trivially to `π_1(U)` (F.20). (b) A natural candidate fails: for `U = Δ_inj` and `H = K` the acyclic semi-simplicial set of A.12, `U/H` is the category of simplices of `K`, but the restricted action `L = h^{[0]}` with all points identified for `n ≥ 2` gives a category equivalent to the vertex–triangle incidence graph, with `H_1 = Z^{28}`; so `K` is not totally `W_Z`-aspherical. (c) What is missing is a way to realize the universal covering of `U/H` by restricted actions after enlarging `U`. Recorded as hunch H3. |

| F.28 (`Δ/∂Δ^{n+2}` is `W`-aspherical ⇔ `W_n ⊂ W`; "Known") | correct | Cisinski, Astérisque 308 (2006), Proposition 9.2.17 (a) ⇔ (b), and Corollaire 9.2.15 for the convention; opened in the copy of the prompt's zip, pp. 369–370. No accessibility hypothesis there. |
| F.29 (for `i: A → B` injective on objects, `∫(B ← A → C) → B ⊔_A C` is in `W_1`) | correct | I followed the construction of `r: Π(B ⊔_A C) → Π(∫)` (objects of `i(A)` moved to the `C`-copy by `θ = v u^{-1}`) and the natural isomorphism `id ⇒ r Π(q)`. It is van Kampen for categories. |
| F.30 (`S²` `W`-aspherical ⇒ every object-injective functor is a `W`-cofibration) | correct | F.28, F.29 and fibrewise invariance of integrals. This is what D.19–D.21 quote; those three rows of Part D are therefore **correct** without reservation. |
| F.31 (**C048, complete dichotomy**: all sieves if `S²` is `W`-aspherical, only isomorphisms otherwise) | correct | F.24 and F.30. |

## Part G. The fixed-origin path category (G.1–G.6)

Reading note: of Chapter VII I read only the definition (VII ms. 24–26: `Ty`, `CH_X: Ty° → Cat`,
`τ ↦ Hom(I_τ, X)`, with footnote 7 restricting to endpoint-compatible maps) and Grothendieck's use of it at XII
ms. 101–103. Chapter VII will be read in full for PATHS; if the definition of the morphisms of intervals in VII
§§5–7 differs from G.1 in a way that matters, this part must be revisited (noted in the handoff).

| Item | Verdict | Argument |
|---|---|---|
| G.1 (definition of `P(Y, y_0) = Ch(Y; y_0, −)`, endpoint functor `q`) | correct as far as checked | Agrees with VII ms. 24–26 (fibred category over `Ty` of the functor `τ ↦ Hom(I_τ, Y)`; morphisms `(φ, η: c ⇒ dφ)`). The restriction to non-decreasing maps (VII §§5–7) not yet checked against the text. |
| G.2 (`π_0 Ch(Y; a, b) ≅ Hom_{ΠY}(a, b)`) | correct | The relations of the groupoid completion are realized by path morphisms (collapse, composition, the two cancellation moves with components `(id, u, id)`). |
| G.3 (`BY` simply connected ⇒ `q` is final) | correct; known to Grothendieck | XII ms. 102–103 (the `y\X` are 0-connected iff `Y` is 1-connected). The return's direct argument (append `α` as a retrograde edge) avoids his appeal to "`f` est `W∞`-parfait". |
| G.4 (`y_0` initial ⇒ `P(Y, y_0)` contractible) | correct | `const ⇐ R ⇒ id` with `R` = constant path of the same type. |
| G.5 (**row C005 refuted**: `Y = Ψ`, `y_0 = z`) | correct; essentially in the manuscript | Since `q` is final (G.3), `T(P(Y, y_0)) ⇒ T(Y)` by stability under final images (the Lemma of XII ms. 112). Grothendieck himself notes that `Ψ` is aspherical and not totally aspherical (footnote to Prop. 10, XII ms. 103; XIIapp ms. 10–12). So his own remarks already answer his question of ms. 103; the return makes it explicit. The general statement I add: **for `Y` simply connected, `Ch(Y; y_0, −)` totally `W∞`-aspherical implies `Y` totally `W∞`-aspherical.** The converse (is `Ch(Y; y_0, −)` total when `Y` is, e.g. for `Y = e`, the category of types?) is not treated; follow-up. |
| G.6 (`P(Ψ, z)` is not filtered) | correct | `r` and `s` have no common successor, since `q` would give arrows from `a` and `b` to a common object of `Ψ`. |

## Part H (disposition table)

The table of H restates the results above against the audit rows; each line agrees with the statement it cites.
My own disposition of the rows named in the prompt:

| Row | Answer | Where | New relative to Grothendieck? |
|---|---|---|---|
| II-C-003 (II ms. 36: total ⇒ filtered?) | No in general (`Δ_inj`); yes with a weakly terminal object (monoids, finite categories). Exact characterization: C.5. | C.5, C.10, C.13 | Yes. The counterexample is Isbell–Mitchell's (1973); the bridge to total asphericity is new. |
| second Question of II ms. 36 (`X°` totally 0-connected? PS 1′?) | PS 1′ yes (also span completion); totally 0-connected no. | C.11, C.14, D.16 (my reading; the return does not name the question) | Yes. |
| XIIb-a-B035 (XII ms. 94–97: `H` total ⇒ `U/H` total?) | No (three-element presheaf on `{1, e}`), unless `S²` is `W`-aspherical. | E.3, E.5 | Yes. |
| XIIba-C005 (XII ms. 103) | No (`Y = Ψ`). | G.5 | Follows from his own remarks. |
| XIIba-C035 (XII ms. 111, Question (a)) | No: a couniversal `W∞`-equivalence need not be dwyérienne (`a ⇉ t → s`). For one-point complements: couniversal ⇔ crossing presheaf totally `W_Z`-aspherical; whether that is totally `W∞`-aspherical is open (F.27). | F.18–F.20 | Yes. |
| XIIba-C045 (composition of dwyérienne sieves) | Total: yes for `W∞`, `W_R`; no for `W_0`, `W_1`. Strict: yes for `W_R`; no for `W_0`, `W_1`; open for `W∞` (equivalent to F.27). | F.6, F.9, F.10, F.12, F.26 | Yes. |
| XIIba-C047 (composition of strictly / totally aspherical functors) | Yes, both, for every fundamental localizer. | F.7, F.8 | Yes. |
| XIIba-C048 = XIIbb-A001 (XII ms. 114) | No such class for `W∞` (only isomorphisms); all sieves when `S²` is `W`-aspherical. | F.23, F.24, F.31 | Yes; his XIIapp ms. 13 Proposition is the first instance. |
| XII Théorème 2 (ms. 78), Corollary of ms. 85, Th. 4 Cor. 4–5 | False for `W∞`; true for `W_R`. | A.11, A.13, A.14 | Yes (not in the prompt's list; subject of POLES). |

## Summary

Counts (107 items): **correct 104; unproved 2** (D.7, F.27: the return's two "Open" statements; I could not
close either, my attacks are in the rows); **wrong 0; gap 0**; plus 1 item (G.1) "correct as far as checked"
pending the reading of Chapter VII, counted among the 104. Label corrections: C.9 (and the core of C.10) is a known
theorem (Isbell–Mitchell 1973, Th. 3) re-proved independently; B.1, E.1, G.3, G.5 and A.16 are in the manuscript.
No statement labelled Proved, Refuted or Known by the return was found false.

Main points for the companion and for follow-up:

1. Total `W∞`-asphericity of a category means: ordinary colimits over it of (simplicial) sets are homotopy
   colimits (C.5, B.11). It is implied by exactness of abelian colimits (Isbell–Mitchell class) and implies
   quasi-filteredness (Adámek–Reiterman class); with a weakly terminal object all coincide with "filtered".
2. Grothendieck's conjecture of II ms. 36ter is false (`Δ_inj`), true for finite categories and monoids.
3. Two open problems of the same nature remain: D.7 (is total = exact?) and F.27 (does integral totality of a
   presheaf force simple connectivity of its category of elements?). Hunches H1 and H3.
4. For `W∞` the Dwyer-type programme of XII §2.4 has this outcome: dwyérienne sieves are `W`-cofibrations without
   any extra axiom; the converse fails; total ones compose; the class asked for at ms. 114 does not exist.

## Report, results CSV, research files and code

- `TOTASPH_results.csv`: the id-to-statement mapping was checked by script against the section labels (107 rows,
  in section order, statuses 84 Proved / 11 Refuted / 10 Known / 2 Open); the rows restate the section statements,
  and the `notes` add only scope remarks. Every id has a verdict above.
- `TOTASPH_report.md`, §§1–8 (read in full): consistent with the sections; no claim there goes beyond a numbered
  statement. Its §4 lists corrections to the transcription of XII: ms. 88 (`U'/H'`, not `U/H'`), ms. 89
  (`F ↦ V/F`, not `F/V`), ms. 92 (`V'/F'`), ms. 93 (`π_0(V/V')`), ms. 110 and 113 (`U' ⊔_U X`), ms. 112. I compared
  them with `corrected_french_20261111\DER_XIIb-a.tex`: ms. 92, 93, 110, 113 are already marked `[sic]` there; **ms. 88
  ("`U'/t' ≃ U/H'`") and ms. 89 (the label "`F ↦ F/V`" in the diagram) are not marked** and should be recorded as
  slips (of the manuscript or the edition; to be checked on the PDF). Its §6 states the two open items exactly as
  D.7 and F.27, plus: total sieve composition for a fixed general localizer (the cosieve criterion F.9), with
  `W_2` on infinite categories as first unhandled case.
- Report appendices 1–6 (= `research\AG_report.md`, `CD_report.md`, `CD_followup.md`, `F_report.md`,
  `CD_C048_report.md`, `AG_general_report.md`): read. They are the working records of the run's sub-tasks and agree
  with the sections. Two facts from them matter for attribution: (i) the run could not open Isbell–Mitchell
  1973/1976 (HTTP 403) and found the gap-polynomial construction of C.9 in the Open Maths lesson "Derived
  colimits over a small category" (20 Oct 2026, AI-written, CC0), which it then re-proved; (ii) it opened
  Hackney–Ozornova–Riehl–Rovelli (Def. 3.4, Th. 1.5, 1.6), Batanin–Berger (Def. 1.1, Lemma 1.10), Cisinski 1999
  and Cisinski 2006 in the attached copies. The unsuccessful routes it lists for D.7 (free-abelian comonad
  resolution; products; fixed points) are the ones I also tried.
- `research\root_report.md` is an earlier copy of the report (same sections 1–4). `TOTASPH_references.bib`: read; it
  marks Isbell–Mitchell 1973 and 1976, Isbell 1974 and Street–Walters 1973 as unverified (not opened by the run);
  I opened the 1973 note. The research ledgers (csv/json) restate the results rows; not read line by line.
- Code (read, not run): `cd_affine_polynomials.py` and its output (the construction of C.8–C.9 for n ≤ 3: targets
  0, 2, 6, 14; 1, 3, 29, 932 terms), `cd_affine_simplex.py` and output (exploratory null-space search: witnesses
  exist exactly from target cardinalities 3 and 7), outputs `cd_finite_checks.out`, `f_check.out` (head).
  Not read: `ag_finite_examples.py`, `root_monoid_checks.py`, `root_presheaf_checks.py`, `f_check.py`,
  `f_low_truncation.py` and the build/QA scripts. Nothing in the code is used as support for a verdict.
- Own checks (`..\DERIVATEURS_EXPERT\work\checks_2\check_affine_cone_and_sphere.py`, run 12 Nov): the 29-term
  combination printed for n = 2 has augmentation 1 and equalizes the three cofaces `[1] → [2]` and the three maps
  `[0] → [2]`; the 4-object category `Z` has nerve with simplex counts (4, 6, 4) and `H_0 = Z`, `H_1 = 0`,
  `H_2` of rank 1. By hand: the n = 1 cone `t = (1,2) − (0,2) + (0,1)`; the permutation identities and the
  counts of A.12.
