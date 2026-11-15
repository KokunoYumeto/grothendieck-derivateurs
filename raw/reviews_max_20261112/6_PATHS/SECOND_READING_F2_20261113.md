# Second reading of F2 of the PATHS intake (the path categories are the mapping spaces of the localization)

Claude Fable 5.2 (Anthropic), effort max, Dérivateurs field expert, 13 November 2026, 00:40 local (clock checked).
Read: `FINDINGS.md` of this folder, F2 and F3; PATHS `sections/C_paths.tex` (C.P1–C.P5) and the statements A.P1,
A.P2, A.3, A.4, B.1, B.2, B.6, B.8, D.1, D.5, D.K4, D.K5. No program was run. No literature was opened.

**Verdict.** F2: every step followed with an argument of my own; no error found. One step can be shortened (4
below). F3: read in outline; its two unwritten steps are not checked here. A literature search is still to do.

## The statement

`M` a small category, `Σ ⊂ M` a wide subcategory, `b ∈ M`. Claim: there is an equivalence of presheaves of spaces on
`M`, `X_b ≃ Map_{L(M,Σ)}(−, b)`, under `h_b = Hom_M(−, b)`, with `X_b(a) ≃ B Ch_Σ(M; a, b)`.

## The steps, as I checked them

Notation. `F_τ(−, b)`: functors `c: I_τ → M` with backward edges in `Σ` and `c(n) = b`; morphisms are the natural
transformations `η` with `η_n = id_b` (`η_0` and the interior components arbitrary). `s_τ: F_τ(−, b) → M`,
`c ↦ c_0`, `η ↦ η_0`. A type map `u: τ → σ` gives `u^*: F_σ(−, b) → F_τ(−, b)`, `c ↦ c∘u`; it lands in the right
category because a backward edge goes to a string of backward edges or to a vertex and `Σ` is a wide subcategory;
`s_τ u^* = s_σ` strictly, because `u(0) = 0`.

1. *The presheaf.* `X_b(a) = B(a ↓ s)` for `s: ∫_{Ty} F_τ(−, b) → M`, and `X_b^τ(a) = B(a ↓ s_τ)`. Both are strict
   functors of `a ∈ M^op` (precomposition of `f: a → c_0`). `a ↓ s` is literally the fibred Grothendieck
   construction of `τ ↦ a ↓ s_τ`, so `X_b ≃ hocolim_{Ty^op} X_b^τ` objectwise, naturally in `a` (Thomason, fibred
   form, natural for strict maps of diagrams). `a ↓ s_τ → F_τ(−, b)` is the discrete opfibration of
   `c ↦ Hom_M(a, c_0)`, so `X_b^τ ≃ hocolim_{c ∈ F_τ(−, b)} h_{c_0}` and, for every presheaf of spaces `Q` on `M`,
   `Map(X_b^τ, Q) ≃ holim_{c ∈ F_τ(−, b)^op} Q(c_0) =: A_τ`. For the empty type, `X_b^∅ = h_b`.
2. *`X_b(a) ≃ B Ch_Σ(M; a, b)`.* `i(τ, c) = ((τ, c), id_a)`; `r((τ, c), f) = ((+)τ, f*c)`, on morphisms
   `(u, η) ↦ ((+)u, (id_a, η))`, a morphism because `η_0 f = f'`. `r i ⇒ 1` by the first-edge collapse with identity
   components. `i r ⇒ 1` by the first-edge collapse with components `(f, id, id, …)`: the square on the first edge
   reads `id∘f = id∘f`, and the comma condition reads `f∘id_a = f`. Both are natural. So `i`, `r` are inverse
   homotopy equivalences, and `X_b(g)` corresponds to prepending the forward edge `g`.
3. *(i) `X_b` inverts `Σ`.* For `w: a' → a` in `Σ` let `Φ(c) = (w)*c` and `Ψ(c') = (a ←w a')*c'`. The transformation
   `(id_a, w, id_a, id, …): ΨΦ(c) → (a = a = a)*c` has commuting squares (`id_a∘w = id_a∘w` on the backward edge,
   `id_a∘w = id_a∘w` on the forward edge); the transformation `(id_{a'}, w, id_{a'}, id, …): (a' = a' = a')*c' →
   ΦΨ(c')` likewise. Collapsing the identity edges gives zigzags of natural transformations `ΨΦ ≃ 1`, `ΦΨ ≃ 1`.
4. *(ii) For `Q` inverting `Σ`, `Map(X_b, Q) → Q(b)` is an equivalence.* `Map(X_b, Q) ≃ holim_{τ ∈ Ty} A_τ`. Let
   `k: ετ' → τ'` collapse the first edge, `pad = k^*`, and `trunc` forget the first vertex; `trunc∘pad = 1`.
   - `ε = +`. A morphism `η: c → pad(d')` has `η_0 = η_1∘c(e_1)`, so `trunc ⊣ pad`. Hence `pad^op` is a left
     adjoint, so it is homotopy initial, and restriction along `pad` is an equivalence
     `holim_{F_{+τ'}^op} G → holim_{F_{τ'}^op} G∘pad^op` for **every** diagram `G`. (The intake argues by the
     opfibration `trunc` with fibres `M/c'_0`; the two arguments agree. No hypothesis on `Q` is used for `+`.)
   - `ε = −`. A morphism `η: pad(d') → c` has `η_0 = w_c∘η_1` (`w_c: c_1 → c_0` the first edge), so `pad ⊣ trunc`
     and `trunc^op` is a left adjoint: restriction along `trunc` is an equivalence for every diagram on
     `F_{τ'}(−, b)^op`. With `Y'(c') = Q(c'_0)`: `Q(w_c): Q(c_0) → Q(c_1)` is a natural transformation from
     `c ↦ Q(c_0)` to `Y'∘trunc^op` (naturality: `η_0 w_c = w_d η_1`), and an equivalence because `Q` inverts `Σ`.
     This gives an equivalence `Θ: A_{τ'} → A_{−τ'}` with `pad^*∘Θ = 1` (at `pad(c')` the edge is an identity), so
     `pad^* = A(k)` is an equivalence.
   - Every `τ → ∅` is a composite of first-edge collapses, and `∅` is terminal in `Ty`. So `A(τ → ∅)` is an
     equivalence for every `τ`, hence `A(u)` for every `u` (two out of three). `A` factors through the groupoid
     completion of `Ty`, which is contractible; so `holim_{Ty} A → A_∅ = Q(b)` is an equivalence, and this map is
     restriction along `h_b = X_b^∅ → X_b`.
5. *Conclusion.* The presheaves inverting `Σ` are the presheaves on `L(M, Σ)` (universal property of the
   localization), and for such `Q`, `Map(Map_L(−, b), Q) = Q(b) = Map(h_b, Q)`. So `h_b → X_b` and
   `h_b → Map_L(−, b)` are both the reflection of `h_b`, and `X_b ≃ Map_L(−, b)` under `h_b`.

Inputs taken as standard and not re-proved: Thomason's theorem in the fibred form with its naturality; the
criterion that a left adjoint is homotopy initial; the identification of `Σ`-local presheaves with presheaves on the
localization.

## What this reading does not cover

- F3 (the inclusion `J` of the hammock model is a weak equivalence): its two unwritten steps (a presheaf structure
  on `a ↦ B Ch^Σ_Σ(M; a, b)`; the form of the Dwyer–Kan theorem used) are not checked.
- Compatibility of the equivalence with composition and naturality in `b`: not claimed in F2; asked in INDLOCAL
  C4.4.
- The literature. Nothing was searched. The statement must not be called new before that is done.
- The computations of the intake (`work/scratch/`) were not rerun.
