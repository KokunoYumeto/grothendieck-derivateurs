# GALOIS (return 4): review

Reviewer: Claude Fable 5.2 (effort max), field expert for *Les Dérivateurs*, 12 November 2026.
Return reviewed: `pro_returns_20261110\4_GALOIS\GALOIS\` by GPT-6 Astra (ChatGPT Pro mode): paper (sections
`conventions`, A, B, B_general, B_accessibility, B_loc67, B_KT, C, D, E, F, G), `GALOIS_results.csv` (74 rows:
52 Proved, 10 Known, 7 Refuted, 5 Open by its own labels), report, research files, code.

Read before the return (notes in `DERIVATEURS_EXPERT\GROTHENDIECK_NOTES.md`): Chapter I in full (ms. 1–66 for
return 2; ms. 60–126 now), Chapter X ms. 1–5, XI §1, XVI. Before opening the return I worked out the leads
myself (`DERIVATEURS_EXPERT\work\checks_4\own_thoughts_before_reading.md`); where my independent argument
agrees with the return, the row says so.

Verdict vocabulary: **correct** (I checked the proof, or re-proved the statement, or opened the cited source),
**wrong**, **gap**, **unproved**. Notation: `W_D` constant-coefficient equivalences (Grothendieck's
`D`-équivalences, I ms. 61); `W^coh`, `W^hom` (I ms. 101, 113); `W^1` 1-complete, `W^lc` 2-complete (I ms. 99–100,
113); `LC_D(X)` locally constant coefficients.

## Part A. Axioms, coefficients, the five classes

| Id | Verdict | Argument |
|---|---|---|
| A.1 | correct | These are Grothendieck's definitions: `D`-équivalence (I ms. 61, Déf. 1), cohomological and homological `D`-équivalences (ms. 101, 113), 1-complete and 2-complete (ms. 99, 113), locally constant = all restriction maps `F_{y'} → F_y` invertible (footnote 33, ms. 76). Checked against the text. |
| A.2 | correct | `W^lc ⊂ W^1` by definition; `W^1 ⊂ W^coh ∩ W^hom` by applying full faithfulness to `Hom(q^*M, F)` and `Hom(F, q^*M)` and Yoneda in `D(e)`; each of `W^coh`, `W^hom` is in `W_D` (take `F` constant). This is the diagram of I ms. 113. `W∞ ⊂ W^lc` is Grothendieck's axiom Der 3 b′_2 (ms. 112), which he believed to hold "dans tous les cas à ma connaissance"; the return quotes Cisinski, *Locally constant functors* (2009), Cor. 3.8, for every derivator (source not opened by me; I rely on the citation). So **Der 3 b′_2, and with it a′, b′_1, b″_coh, b″_hom, is a theorem for derivators**, and the "Lemme" of I ms. 109 (HOT-equivalences are 2-complete), which Grothendieck could not prove, holds; footnote 57 ("Est-ce vrai aussi pour les dérivateurs `D_i`?"): yes. |
| A.3 | correct | For `A → e`: `LC_D(e) = D(e)`, so 1-completeness is the bijection (A.1.1). Hence a map to the point is in `W_D` iff it is in `W^1`. This corrects a sentence of the prompt (an acyclic group `A` does not give `BA → e ∈ W_D ∖ W^1`); in my own computation for `D(k)`, `W^1` = maps with `k`-acyclic homotopy fibres, which contains `BA → e`. |
| A.4 | correct | Hom-set arguments: `W_D` and `W^lc` are classes inverted by a functor (constants; `X ↦ LC_D(X)` up to equivalence), hence saturated; `W^1` is closed under composition and retracts and satisfies "`f, gf ∈ W^1 ⇒ g ∈ W^1`". This is Grothendieck's sorite (I ms. 101, Prop. 1). |
| A.5 | correct | `e → BC_2 → e` for set coefficients: the composite and `BC_2 → e` are 1-complete, `e → BC_2` is not (the regular `C_2`-set has 2 equivariant and 4 arbitrary endomaps). So `W^1`, `W^coh`, `W^hom` fail two out of three and are not localizers. I had the same refutation before reading (`* → S¹ → *`). **Lead 1 is false for `W^1`.** |
| A.6 | correct | Cited from Cisinski 2009, Th. 3.13 (not opened by me); the deduction (full faithfulness or equivalence at every shape iff at `e`, by units and counits and Der 2) is right. |
| A.7 | correct | Opposites through the twisted arrow category (Grothendieck's `Φ(X)`, I ms. 72–75); finite products by Fubini; sums by Der 1, with the exception noted for `W_D` (`∅ → e` plus an identity, for the derivator of the lattice `{0 < 1}`). The infinite product `∏ I_n` of alternating intervals is not connected: checked (a zigzag of length `m` moves the `n`-th coordinate by at most `m`). |
| A.8 | correct | For `D` the derivator of a complete and cocomplete ∞-category `𝒞`: `LC_D(A) = Ho Fun(BA, 𝒞)`, and full faithfulness or equivalence of the restriction on homotopy categories is equivalent to the ∞-categorical property, because it is detected by units and counits (or by cotensors with spaces). Same as point 1 of my own analysis. |

## Part B. `W^lc` and `W^1` as localizers

Rows B.1, B.2, B.5, B.8, B.9, B.10 are in `sections\B.tex`; B.3 in `B_general.tex`; B.4 in `B_accessibility.tex`;
B.6, B.7 in `B_loc67.tex`; B.11–B.14 in `B_KT.tex`. (Rows are entered in the order in which I read the files.)

| Id | Verdict | Argument |
|---|---|---|
| B.1 | correct | Absolute Theorem A for `W^lc`, for every derivator: if all `A/b → e` are 2-complete then the transitions `A/b → A/b'` are (two out of three, A.4), so `u_!F` is locally constant for locally constant `F` (pointwise formula and A.2), the unit `F → u^*u_!F` is invertible at `(a, id)` and the counit `u_!u^*G → G` at every `b`; Der 2 concludes. For `W_D` the relative Theorem A follows from the pointwise formula for `β_* p_B^* → α_* p_A^*` at `s`; this is Grothendieck's axiom L 4 for `W_D` (X ms. 4: "C'est OK") with the proof he does not write. |
| B.2 | correct | For `D` the derivator of a complete and cocomplete ∞-category: `BA ≃ hocolim_s B(A/s)` (the projection `∫_S (A/s) → A` has a left adjoint section), so `Fun(BA, 𝒞) = lim_s Fun(B(A/s), 𝒞)`, and an objectwise equivalence of diagrams gives an equivalence of limits; A.8 passes between homotopy categories and ∞-categories. Same as my own argument. So `W^lc` is a fundamental localizer in the enhanced case: **Lead 1 is right for `W^lc`**. |
| B.5 | correct | Loc (4) is A.7; Loc (6 a) because `N A = N A_1 ∪_{N A_0} N A_2` for a cover by two sieves and `Fun(−, 𝒞)` turns the homotopy pushout into a pullback; Loc (8) because nerves commute with filtered colimits; Loc (5) for `W^lc` iff `D(e)` is not trivial (G.1). In the unenhanced case the return uses B.3 and Cisinski, Ast. 308, Cor. 4.2.22 (opened for return 3). I checked the enhanced arguments; the unenhanced ones stand or fall with B.3. |
| B.8 | correct | Cisinski, Ast. 308, Prop. 9.2.17 (opened for return 2): `W_n ⊂ W` iff `Δ/∂Δ^{n+2}` is `W`-aspherical. Applied to `W^lc`. |
| B.9 | correct | For `t: X → Y` with acyclic homotopy fibres, the fold `Y ∪^h_X Y → Y` is an isomorphism on `π_1` (amalgam along a surjection) and on homology with all local coefficients (Mayer–Vietoris; acyclic maps induce isomorphisms with local coefficients, Hausmann–Husemoller, cited), hence a weak equivalence; so the two inclusions of `Y` agree in the homotopy category and `[Y, Z] → [X, Z]` is injective. Checked. |
| B.10 | correct | Simple envelope: for `g ≠ 1`, `h`, the word `w = g t g⁻¹ t⁻¹ g t² g⁻¹ t⁻²` is a product of conjugates of `g^{±1}`, `w` and `wh` have infinite order, and an HNN letter with `s⁻¹ w s = w h` puts `h` in the normal closure of `g`; iterate. Acyclic envelope: mitosis (checked in the review of return 3, B.10 there). Alternating the two and taking the union gives an acyclic simple group of cardinality `λ` containing `H`; a simple group of cardinality `> μ` has only trivial homomorphisms to groups of cardinality `≤ μ`. |

