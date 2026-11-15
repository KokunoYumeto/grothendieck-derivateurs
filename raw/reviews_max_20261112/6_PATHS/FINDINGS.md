# Findings of the intake of PATHS (package 6 of the Les Dérivateurs series)

Intake by Claude Fable 5.2 (Anthropic), effort high, 12 November 2026 (about 23:30 WEST). The return is by GPT-6 Astra
(OpenAI, ChatGPT Pro mode), 11 November 2026. This intake replaces the review of 11 November, which is void and was
not read. The intake agent could not write its three files (a harness guard blocked it); the main session saved the
texts as the agent gave them. REVIEW.md gives the verdict on each of the 76 statements; IMPLICATIONS.md says what
changes for INDLOCAL, for PRETOT F.16 and for the companion. Findings F2 and F3 are arguments of this intake: nobody
else has read them.

Notation. `M` a small category, `Σ` a wide subcategory. `I_τ` the interval of type `τ`; `Ty` the category of types.
`F_τ(a,b) = Fun_Σ(I_τ, M)_{a,b}`: functors with backward edges in `Σ`, endpoints `a, b`, and ALL natural
transformations that are identities at the two endpoints. `Ch_Σ(M;a,b)` is the fibred Grothendieck construction of
`τ ↦ F_τ(a,b)` over `Ty`: a morphism `(τ,c) → (σ,d)` is a type map `u: τ → σ` with `η: c ⇒ d∘u`. `Ch_Σ^Σ` is the same
with all components of `η` in `Σ` (the Dwyer–Kan hammock model). `J: Ch_Σ^Σ → Ch_Σ` is the inclusion.
`L = L(M,Σ)` is the ∞-categorical localization.

## Mathematics

### F1. PATHS C.P1–C.P3 prove what PRETOT F.16 leaves open. The proof is correct.

Statement proved (C.P3, with A.P2): for every small `M`, every wide `Σ`, all `a, b`, and every sequence of types
`t_0 ← t_1 ← …` such that each type receives a map from some `t_n`, both legs of

    C_∞(t) = colim_n F_{t_n}(a,b)  ←  E_t  →  Ch_Σ(M;a,b)

are weak equivalences (`E_t` the Grothendieck construction of the sequence). PRETOT F.16 has this for groupoids and
for `[1]` only, and names the six-object poset of type `S²` and proper `Σ` as undecided. Both are covered.

This is Grothendieck's question at VII ms. 103 (b) ("Est-elle canoniquement isomorphe à C dans Cat hot, ou dans
Hot ?"), which he answers "en général pas" at ms. 112 and reopens in footnote 24 at ms. 113 ("le problème si
C_∞ ≃ C dans Hot reste entier"). The answer is yes in `Hot`, for every `Σ`.

The proof, as checked:

1. `P(τ,σ)`: the poset of type maps `τ → σ`, with `u ≤ v` iff `u(i) → v(i)` in `I_σ` for all `i`. It is empty or
   contractible (C.P1). The induction on the runs of `σ` was followed (the retraction `R` onto the maps sending the
   first source run to `(0,b,…,b)`, with `1 ⇒ R` or `R ⇒ 1`), and checked by enumeration: all 11,369 non-empty
   `P(τ,σ)` with `|τ| ≤ 7`, `|σ| ≤ 5` collapse to a point (`work/scratch/test_cp1.py`, `.out`).
2. `(u,c) ↦ c∘u` is a functor `P(τ,σ) × F_σ → F_τ`, strictly associative and unital: for `α: u ⇒ v` the component
   `c(α_i)` is a composite of forward arrows and `Σ`-arrows, with identities at the endpoints. This needs the
   interior vertical arrows to be arbitrary; the hammock categories `F_τ^Σ` do not carry this action.
3. Let `𝔗` be the simplicial category with the types as objects and `Hom(τ,σ) = N P(τ,σ)`, and `R` the preorder of
   types (`τ → σ` iff `P(τ,σ) ≠ ∅`). By 1, `𝔗 → R` is bijective on objects and a weak equivalence on every Hom: a
   Dwyer–Kan equivalence. Restriction along it is a Quillen equivalence between the projective model categories of
   simplicial functors to simplicial sets (Dwyer–Kan; Lurie, HTT A.3.3.8). Hence the diagram `τ ↦ N F_τ` on `𝔗^op` is
   weakly equivalent to the pull-back of a diagram `F̄` on `R^op`, and its restriction to `Ty^op` is weakly
   equivalent to `p^*F̄`, `p: Ty^op → R^op`. The return words this step with coherent nerves and Kerodon numbers (not
   opened); the model-category form is the one verified here.
4. `p` is homotopy final: the comma category at `σ` is the opposite of `Ty_σ` (types with a map to `σ`), and
   `τ ↦ σ*τ` has natural maps to the identity and to the constant `σ`. For the sequence, the comma category at `σ`
   is a non-empty upward closed subset of `ℕ`.
5. So `hocolim_ℕ N F_{t_n} → hocolim_{Ty^op} N F_τ` is a weak equivalence; by Thomason's theorem in its fibred form
   this is the nerve of `E_t → Ch_Σ(M;a,b)`. `E_t → C_∞(t)` is A.2 (filtered colimits of categories).

PRETOT's obstruction (no cofinal chain is homotopy initial in `Ty` for all diagrams; `Ty^op` is not filtered) is
correct and is not contradicted: step 3 is special to the path diagram. Grothendieck's sufficient condition at
ms. 112 (`T → T_o` smooth and coaspherical, or proper and aspherical) fails for `Ty`, as he says; what holds for `Ty`
is that its Hom-posets are contractible.

Test on the instance named in F.16 (`work/scratch/test_s2.py`): for the six-object poset `Y` of type `S²`, base
`0⁺`, all arrows marked, `F_{(+−)^k}(0⁺,0⁺)` has 5, 61, 841 objects and Betti numbers (1,0,0,0), (1,1,1,0),
(1,1,1,0) for `k = 1, 2, 3`: connected with `b_1 = 1`, as `ΩS²` requires.

Verified by the same means: E.26 (1), (2) (C.P3) and E.27 for every block containing both signs (C.P4:
`β_P μ = γ(β_P × β_P)`, so the padded operation is strict concatenation transported). For a block with one sign the
sequence is not cofinal and E.27 fails: for the crown `0,2 → 1,3` and `a = b = 0`, `F_{+^n}(0,0)` is one point,
against `ΩS¹ = ℤ`.

### F2. New in this intake: `B Ch_Σ(M;a,b)` is the mapping space of the localization, for every wide `Σ`.

**Theorem.** For every small category `M`, wide subcategory `Σ` and objects `a, b` there is an equivalence
`B Ch_Σ(M;a,b) ≃ Map_{L(M,Σ)}(a,b)`, natural in `a ∈ M^op`, sending the empty path at `b` to the identity. No
two-out-of-three, saturation or calculus of fractions is assumed.

This is what PATHS leaves open as B.8 (with F3), Grothendieck's "Hom externe" (VII §§10–13, IX ms. 1–25), and the
"comparison with the modern mapping space" on which rows IX-037, IX-040, IX-041, IX-072 and others were conditional.

*Proof.* Fix `b`. Presheaves are functors `M^op → 𝒮` (spaces); `h_b = Hom_M(−,b)`. Call a presheaf `Σ`-local if it
inverts `Σ`. The `Σ`-local presheaves are the presheaves on `L`, and `R_b = Map_L(−,b)` is the localization of `h_b`:
it is `Σ`-local and `Map(R_b,Q) → Map(h_b,Q) = Q(b)` is an equivalence for every `Σ`-local `Q`. It suffices to give a
presheaf `X_b` with `X_b(a) ≃ B Ch_Σ(M;a,b)` and a map `h_b → X_b`, and to show (i) `X_b` is `Σ`-local,
(ii) `Map(X_b,Q) → Q(b)` is an equivalence for every `Σ`-local `Q`.

*The presheaf.* For a type `τ` let `F_τ(−,b)` be the category of paths of type `τ` ending at `b` with free origin:
morphisms are natural transformations `η` with `η_n = id_b` and `η_0` arbitrary. Let `s(c) = c_0`, and
`X_b^τ(a) = B(a\s_τ)`, where `a\s_τ` has objects `(c, f: a → c_0)`. This is a strict functor of `a ∈ M^op` and
`τ ∈ Ty^op`. Put `X_b(a) = B(a\s)` for the total category `Ch_Σ(M;−,b) = ∫_{Ty} F_τ(−,b)`. Then:

- `a\s` is the fibred Grothendieck construction over `Ty` of `τ ↦ a\s_τ`, so `X_b = hocolim_{τ ∈ Ty^op} X_b^τ`
  (Thomason), naturally in `a`.
- `a\s_τ → F_τ(−,b)` is the discrete opfibration of `c ↦ Hom(a,c_0)`, so `X_b^τ = hocolim_{c ∈ F_τ(−,b)} h_{c_0}` and
  `Map(X_b^τ,Q) = holim_{c ∈ F_τ(−,b)^op} Q(c_0) =: A_τ`. `X_b^∅ = h_b`.
- `i: Ch_Σ(M;a,b) → a\s`, `c ↦ (c, id_a)`, and `r: (c,f) ↦ (f)*c` (prepend the forward edge `f`) are inverse modulo
  natural transformations (`r i ⇒ 1` by collapsing the identity edge; `i r ⇒ 1` by the morphism `(f)*c → c` with
  components `(f, id, id, …)`). So `X_b(a) ≃ B Ch_Σ(M;a,b)`, and `X_b(f)` is prepending `f`.

*(i).* For `w: a' → a` in `Σ`, prepending the forward edge `w` has the homotopy inverse "prepend the backward edge
`w`": `(a ←w a' →w a)*c ⇒ (a = a = a)*c` and `(a' = a' = a')*c' ⇒ (a' →w a ←w a')*c'`, each with middle component
`w`, natural in `c`, `c'`; the constant edges collapse.

*(ii).* `Map(X_b,Q) = holim_{τ ∈ Ty} A_τ`. Claim: for every type `τ'` and sign `ε`, the map `A_{ετ'} → A_{τ'}` induced
by collapsing the first edge (restriction along `pad: F_{τ'}(−,b) → F_{ετ'}(−,b)`, which prepends an identity edge)
is an equivalence.

- `ε = +`. `trunc: F_{+τ'}(−,b) → F_{τ'}(−,b)` (forget the first vertex) is a Grothendieck opfibration: the
  cocartesian lift of `η': c' → d'` at `(f: c_0 → c'_0; c')` is `(η'_0 f; d')` with first component `id`. Its fibre
  over `c'` is `M/c'_0`. So the right Kan extension of `c ↦ Q(c_0)` along `trunc^op` (a fibration) is computed on
  fibres: `holim_{(M/c'_0)^op} Q = Q(c'_0)`, the value at the initial object `id`, which is `pad(c')`.
- `ε = −`. Now `pad ⊣ trunc`: a morphism `pad(c') → c = (c_0 ←w c_1; …)` has `η_0 = w η_1`. So `trunc^op` is a left
  adjoint, hence initial, and `holim_{F_{−τ'}^op} Y'∘trunc = holim_{F_{τ'}^op} Y'` for `Y'(c') = Q(c'_0)`. Since `Q`
  inverts `Σ`, `Q(w): Q(c_0) → Q(c_1)` is a natural equivalence from `c ↦ Q(c_0)` to `Y'∘trunc`. This gives an
  equivalence `A_{τ'} → A_{−τ'}` whose composite with restriction along `pad` is the identity.

Every `τ → ∅` is a composite of first-edge collapses and `∅` is terminal in `Ty`; so `A` sends every morphism of `Ty`
to an equivalence and is equivalent to the constant diagram `A_∅ = Q(b)`. `B Ty` is contractible, so
`holim_{Ty} A → A_∅ = Map(h_b,Q) = Q(b)` is an equivalence. ∎

The argument shows more: for each single type `τ`, `h_b → X_b^τ` is already a `Σ`-local equivalence; the union over
the types is needed only to make the result `Σ`-local. The arbitrary vertical arrows are used twice (the fibres
`M/c'_0`, the adjunction `pad ⊣ trunc`); with vertical arrows in `Σ` both steps fail at a fixed type, as they must
(`Σ` = identities, `τ = (+,+)`).

Checks. Known cases: `Σ ⊂ Iso(M)` (B.4: discrete `Hom_M(a,b)`); all arrows (path spaces of `BM`). Computations
(`work/scratch/`: pointwise-ordered path posets, collapse of weak points, Betti numbers mod 32003) on the cofinal
sequence `(+−)^k`, which by F1 computes `Ch_Σ`:

| `(M, Σ)` | `L(M,Σ)` | found |
|---|---|---|
| `[2]`, `0 → 2` marked (PATHS's "undecided instance") | walking retraction: every `Map` one point, `Map(1,1)` two | `k = 2..5`, all nine `(a,b)`: the poset (up to 189 objects) collapses to exactly that many points |
| crown, three of four edges marked | `Bℕ`: `Map(0,0) = ℕ` | collapses to 1, 2, 2, 3, 3 points (`k = 1..5`) |
| crown, all marked | `S¹`: `ℤ` | 1, 3, 3, 5, 5 points |
| crown × `[1]`, horizontal arrows and one vertical arrow marked (19 of 24 arrows) | `S¹` | 1, 3, 3, 5 points for all four endpoint pairs (up to 8012 objects) |
| `S²`-poset × `[1]`, horizontal arrows and one vertical arrow marked (41 of 54) | `S²`: `ΩS²` | `k = 2`: cores of 31 elements, `k = 3`: cores of 253 elements, Betti (1,1,1), for all four endpoint pairs; same core sizes and chain counts as the `S²`-poset with all arrows marked |

Not done: a search of the literature for this theorem (PATHS reports a 2020 MathOverflow question on it and no proof
located); a second reading. It should be checked before it is used in a publication.

### F3. Consequence: `J: Ch_Σ^Σ(M;a,b) → Ch_Σ(M;a,b)` is a weak equivalence for every wide `Σ` (PATHS B.8).

`X_b^Σ(a) := B Ch_Σ^Σ(M;a,b)` is functorial in `a ∈ M^op` up to coherent natural transformation (prepending a forward
edge, with identity vertical components), and `J` commutes strictly with prepending and with the empty path. `X_b^Σ`
inverts `Σ` (the argument of (i); the vertical arrow used is `w ∈ Σ`). By Dwyer–Kan (PATHS B.2: the strict,
concatenation-compatible map `ρ` to the hammock localization; the hammock localization is the localization:
Arakawa–Cnossen, Theorem 4.7 and Corollary 1.11) `h_b → X_b^Σ` is the `Σ`-localization of `h_b`. By F2 so is
`h_b → X_b`. A map under `h_b` between two localizations of `h_b` is an equivalence. So `J` is a weak equivalence, and
the map `Q` of PATHS B.6 is one.

State of rigour: F2 is written out in full. In F3 the passage from "functorial up to coherent natural
transformation" to presheaves, and the form of the Dwyer–Kan theorem used (the hammock mapping spaces as a presheaf
on `M` under `h_b`), are standard and not written out.

### F4. PATHS A.8 is no longer open.

A.8 asks for the shapes `A` with `∫_A D → colim^{Cat}_A D` a weak equivalence for all `D: A → Cat`. PRETOT F.6
(reviewed 12 Nov, none wrong) answers it: for `A` non-empty and connected, exactly the filtered categories; in
general, every component filtered. A.7's bounds agree with it.

### F5. No statement of the return was found wrong.

Labels stronger than the proofs:
- B.6 (the map `Q`): the cocone and its compatibility with concatenation are described, not constructed in detail.
  With F2 and F3 the conclusion holds and `Q` is an equivalence.
- D.15 and D.21 (labelled Known, Proved) are formal consequences of Kaledin's Theorem 7.3.1.3, a preprint whose
  Chapters 6–7 its author marks preliminary.
- E.27 is proved for blocks containing both signs; the prompt's "arbitrary block" is false for one-sign blocks (F1).
  The return states the restriction and gives no counterexample.

### F6. Results of the return that other work can cite after this intake (each checked here)

- A.P1: `π_0 Ch_Σ(M;a,b) = Hom_{M[Σ^{-1}]}(a,b)` for every wide `Σ`, with composition.
- A.3: for `u: J → T`, `∫_J F u → ∫_T F` is a weak equivalence for every `F: T^op → Cat` iff every `u/t` is weakly
  contractible. A.4: Grothendieck's hypotheses at VII ms. 99–101 do not suffice (`T = BC_2`; his own example, ms. 109).
- A.5, A.6: `Δ_inj` is totally `W∞`-aspherical and not filtered, and `D([n]) = ℕ^{n+1}` has `colim^{Cat} = Bℕ` (type
  `S¹`) and `H_k(∫D) = ℤ` for all `k`. A.6's polynomial construction was followed; by integer linear algebra, for
  `n = 2` an augmentation-one combination of injections `[2] → [M]` equalizing the cofaces exists for
  `M = 6 = n + d(n,1)` and not for `M = 4, 5` (`work/scratch/test_misc.py`).
- B.4: for `Σ ⊂ Iso(M)`, `Ch_Σ(M;a,b)` is isomorphic in `Cat hot` to the discrete `Hom_M(a,b)`.
- C.P5: for the crown with all arrows marked, `q_L` is a weak equivalence with no inverse modulo natural
  transformations (covering argument; the paths `c_N` reach lifted height `4N`).
- D.2, D.3: the finite category of IX ms. 23 with `W` = identities is rectifiable at every shape; it lacks products.
  D.5: a six-object poset `X` and a weak equivalence `Y → B` of finite categories with `H_{s,s}(B) → H_{s,s}(Y)` not
  onto (own computation: `X^Y` has 198 objects, is connected, `b_1 = 1`; `X^B = X^{[1]}` has 18 objects). D.8:
  intrinsic cofibrations with an initial object give a finite cofibration structure. D.10–D.13, D.16, D.23: the
  separating examples.
- D.K4, D.K5: a small filtered ind-object of `Cat hot` whose functor inverts `W∞` on all small categories factors
  through `Π_1`; the formula `Hom_{M^X[Σ_X^{-1}]}(a_X,b_X) = colim_n π_0 Fun(X, K_n)` of V ms. 44–45, with
  `K_n = F_{t_n}(a,b)` for any cofinal sequence.
- E.2: `Ch(X;x,x)` is a strict monoidal category with `B ≃ Ω_x BX` as `A_∞`-spaces. E.3–E.6: `Ch(X) → X × X` is
  smooth, not proper, not a fibration or opfibration. E.7: the pushout-product of `{0} → [1]` with `{0,2n} → Φ_n` is
  not an intrinsic `W∞`-cofibration for any `n ≥ 1` (a cobase change of type `S³`). E.13: finite set-valued tests
  are not faithful.

## Record

- **F7.** The five programs of the return were rerun with `python -I` in `work/rerun/`: outputs identical to the
  delivered ones (`a_finite_checks`, `b_crown_checks`, `d_finite_checks`, `e_finite_checks`, `b_path_search` at
  lengths 3 and 4; `e_category_tables.json` agrees up to the order of list entries).
- **F8.** Citations: the numbers cited from Arakawa–Cnossen (Definition 1.7, Theorem 1.9, Corollary 1.11, Theorem
  3.26, Theorem 4.7, Proposition 4.8, Lemma 4.16, the remark on the Grothendieck-construction variant) were checked
  against the supplied LaTeX source by label and content. Dwyer–Kan 2.1 and 5.5 are corroborated by that source's
  own citation. Grothendieck's text was read at VII ms. 99–103, 108–115 and IX ms. 21–24. Nothing else was opened.
- **F9.** PRETOT review F17 ("F.16 conflicts with PATHS A.P2/C.P2") is resolved: there is no conflict of mathematics.
  PRETOT did not find the proof; PATHS has it.
- **F10.** `KNOWLEDGE_HANDOFF.md` (section on PATHS) says "The prompt's main question is still open (B.8)" and "which
  shapes compute colimits in `Cat` is open (A.8)". Both are out of date after F2–F4.
