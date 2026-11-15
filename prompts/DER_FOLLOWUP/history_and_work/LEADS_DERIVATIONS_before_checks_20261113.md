# Derivations behind Leads 1, 2, 3 and 5 of the prompt DER_FOLLOWUP

Claude Fable 5.2 (Anthropic), effort max, 13 November 2026. Written while drafting the prompt. Nobody else has read
these arguments and no program has checked them. They are inferences to be proved or refuted, not results. Notation
as in the prompt.

## Lead 1: the cone on a member of `𝒬_n`

`𝒬_n` (`n ≥ 2`): non-empty connected categories all of whose action components are `(n−1)`-connected.

(a) Let `E ∈ 𝒬_n`, `L: E → Set`, `D` a component of `El_E(L)`, and `K: D → Set`. Then `El_D(K)` is the category of
elements over `E` of `a ↦ ∐_{l ∈ L(a), (a,l) ∈ D} K(a, l)`. So the action components of `D` are action components
of `E`, and `D ∈ 𝒬_n`.

(b) Let `E ∈ 𝒬_n` and `E^◁ = E ∪ {0}`, `0` initial. `B(E^◁)` is contractible. Let `L': E^◁ → Set` and
`L = L'|_E`. Each `l ∈ L'(0)` gives a section `s_l: E → El_E(L)`, `x ↦ (x, L'(0 → x)l)`. Its image lies in one
component `D` (`E` is connected), is closed under targets in `D`, and is a full subcategory isomorphic to `E`. In
`El_{E^◁}(L')` the object `(0, l)` has exactly one arrow to each object of `s_l(E)`, no arrow to any other object,
and receives only its identity. So a component of `El_{E^◁}(L')` is either a component `D` of `El_E(L)`, or such a
`D` with one new source for each `l` in a subset of `L'(0)`, and its nerve is `N(D)` with a cone on each
`N(s_l(E)) ≅ N(E)`: a chain that contains `(0, l)` begins with it and continues inside `s_l(E)`. Homotopy pushout
of `BD ← ∐_l BE → ∐_l pt`. `BD` and `BE` are `(n−1)`-connected (`E` is its own action component for `L = pt`). Van
Kampen gives simple connectivity, and `H_q(BD) → H_q(new) → ⊕ H̃_{q−1}(BE)` gives `H_q(new) = 0` for
`1 ≤ q ≤ n − 1`. So every action component of `E^◁` is `(n−1)`-connected and `B(E^◁)` is `n`-connected: by
TOTASPH D.12, `E^◁` is total for `W_n`. `E` is a cosieve of `E^◁` (arrows out of objects of `E` stay in `E`).

(c) If `E ∈ 𝒬_n` has `H_n(BE) ≠ 0`, then `A = E^◁`, `V = E` contradicts the implication of PRETOT C.4 for this `n`.
Conversely a counterexample `(A, V)` has `V ∈ 𝒬_n` (PRETOT C.2) and `H_n(BV) ≠ 0`. So the implication for `n` holds
iff `H_n(BE) = 0` for all `E ∈ 𝒬_n`. If that holds and `E ∈ 𝒬_n`, each action component `D` of `E` is in `𝒬_n`
by (a), so `H_n(BD) = 0` and `D`, being simply connected and `(n−1)`-connected, is `n`-connected: `E ∈ 𝒬_{n+1}`.
Conversely if `𝒬_n = 𝒬_{n+1}` then `BE` is `n`-connected for `E ∈ 𝒬_n`. So: implication for `n` ⟺
`𝒬_n = 𝒬_{n+1}`. All `n ≥ 2` together: `𝒬_2 = 𝒬_∞`, that is, quasi-filtered (R3) = total (R1).

(d) R14 gives a quasi-filtered `A` and `H = h_V/(bv_1 ∼ bv_2)` with `H_2(B El_A(H)) ≠ 0`. `E = El_A(H)` is connected
(a quotient of a representable) and lies in `𝒬_2` by (a). So `E^◁` is total for `W_2` and its cosieve `E` is not.

## Lead 2: strict end-point functors

Setting. `P = P(Y, y_0)`, `q: P → Y`, `z ∈ Y`, `H = Y(q(−), z)` (a presheaf on `P`; for `k: x → x'` in `P`,
`H(k)γ = γ ∘ q(k)`). For objects `p, d` of `P` and `f, g: p → d` put `L = P(p, −)/(kf ∼ kg)`, `k` running over the
arrows out of `d`. Then `Z[L] = coker(δ)`, `δ: Z[P(d, −)] → Z[P(p, −)]`, `k ↦ kf − kg`. Let `K = ker δ`.
With `0 → K → Z[P(d,−)] → im δ → 0` and `0 → im δ → Z[P(p,−)] → Z[L] → 0` and PRETOT A.1:

`H_1(El_{P/H}(Lπ)) = Tor_1^{ZP}(Z[H], Z[L]) = ker( Z[H(d)]/N → Z[H(p)] )`, the map induced by `H(f) − H(g)`,

where `N` is the image of `Z[H] ⊗ K → Z[H(d)]`: the span of the elements `γ·t = Σ n_i γ∘q(k_i)` for objects `x`,
`γ ∈ H(x)` and `t = Σ n_i k_i ∈ Z[P(d, x)]` with `tf = tg`. If `q(f) = q(g)` then `H(f) = H(g)` and
`H_1 = Z[H(d)]/N`.

First pair. `u: y_0 → z`. `d = ((+), y_0 →u z)`, `p = ((++), y_0 →id y_0 →u z)`.
`f = (φ_f, η)`: `φ_f` has vertex map `(0, 1, 1)`, `η = (id, u, id_z)`. `g = (φ_g, η')`: vertex map `(0, 0, 1)`,
`η' = (id, id, id_z)`. Naturality: for `f`, edge 1: `u∘id = u∘id`; edge 2: `id_z∘u = id_z∘u`. For `g`, edge 1:
`id = id`; edge 2: `u∘id = id_z∘u`. Both have `q = id_z`, so `H_1 = Z[Y(z, z)]/N`.
- `x` of non-empty type of length `m`: every `k: d → x` has vertex map `(0, m)`, so `kf` has `(0, m, m)` and
  `k'g` has `(0, 0, m)`: never equal. If `tf = tg` then both sides vanish; grouping the `k_i` by the value
  `φ = k_i f`, each group has coefficient sum `0`, and `q(k_i) = q(k_i f) = q(φ)` is constant on a group; so
  `γ·t = 0`.
- `x = o`: an arrow `d → o` is a `v: z → y_0` with `vu = id`; `k_v f = k_v g` (components `(id, id, v)` both). So
  `N` is spanned by the `γ∘v`, `γ ∈ H(o) = Y(y_0, z)`, `vu = id`.

Hence `H_1 = Z[Y(z, z)] / span{γv}`. The span is spanned by basis elements; the quotient is zero iff every
endomorphism of `z` is some `γv`. In particular `id_z = γv` with `vu = id`: `v` has a left and a right inverse, so
`u = v^{-1}` is invertible. For `R_0`: `Y(0, z) = {u}`, `Y(z, 0) = {r}`, `span = Z·e`, `H_1 ≅ Z`.

Second pair. `v: z → y_0`. `d' = ((−), y_0 ←v z)`, `p' = ((−−), y_0 ←v z ←id z)`, `f'` over `(0, 1, 1)` with
components `(id, id_z, id_z)`, `g'` over `(0, 0, 1)` with components `(id, v, id_z)`; both have `q = id_z`. For
`x` of non-empty type the same disjointness holds. There is exactly one arrow `k: d' → o` (component `v`), and
`kf' = kg'`. So `H_1 = Z[Y(z, z)]/span{γv : γ ∈ Y(y_0, z)}`, zero only if `id_z = γv`. By the first pair `γ` is
invertible, so `v` is.

Conclusion. If `H` is totally `W_Z`-aspherical for every `z` (or totally `W_n`-aspherical, `n ≥ 2`: PRETOT C.1
needs `H_1` of the restricted actions), every arrow out of `y_0` and every arrow into `y_0` is invertible. Then,
as in PRETOT E.6, every arrow of the component of `y_0` is invertible (transport along the isomorphisms already
found), `|Y(y_0, y)| ≤ 1` (PRETOT E.7), and `Y` is connected because no weight is empty. So `Y` is a connected thin
groupoid; the converse is PRETOT E.6. Not treated: `W_1`, `W_0`.

The splitting for `R_0`. `o` is terminal in `P(R_0, 0)`, the element `u ∈ H(o)` gives `P(−, o) → H`, split by
`H → pt = P(−, o)`. The complement is `q^*S`, `S(z) = Z·(id_z − e)`, `S(0) = 0`. `Tor_i(Z[P(−, o)], Z[L]) = 0` for
`i > 0` (each component of `El_P(L)` has a terminal object). So `H` is totally `W_Z`-aspherical iff
`Tor_i^{ZP}(q^*S, Z[L]) = 0` for all `i ≥ 1` and all `L`.

## Lead 3: free monoids over exact shapes

`A` total, `M: A → FreeMon`, `M(a)` free on `S_a`. `BM(a)` is the wedge of circles on `S_a`, naturally equivalent
to `BM(a)^{gp}` (PRETOT F.9). `B∫_A M ≃ hocolim_A BM(a)`. Bousfield–Kan: `E²_{p,q} = L_p colim_A H_q(BM(a))`,
`H_0 = Z` (and `BA` is contractible), `H_1 = M_ab(a)`, `H_q = 0` above. So `H_{k+1}(B∫_A M) = T_k(M_ab)`.
`BA` simply connected gives `π_1 = colim^{Grp}_A M^{gp} = Γ`. The homotopy fibre of `hocolim_A BM(a) → BΓ` is
`hocolim_A` of the `Γ`-coverings `Γ ×_{M(a)^{gp}} E`, whose homology is `Z[Γ/im]` in degree 0, `H_1(M(a)^{gp}; ZΓ)`
in degree 1 and `0` above. If `A` is exact, `L_p colim_A = 0` for `p ≥ 1`, so the fibre has homology
`colim_A` of these, zero in degrees `≥ 2`; it is the universal covering, so it is simply connected, hence
contractible. So `B∫_A M ≃ K(Γ, 1)`. Group completion is a left adjoint: `(colim^{Mon}_A M)^{gp} = Γ`. So
`q_M ∈ W∞` iff `BC → K(C^{gp}, 1)` is a weak equivalence, `C = colim^{Mon}_A M`.

The example. Intervals `I_n = {−∞} ∪ [n] ∪ {+∞}` with `n + 2` edges; an increasing injection `[m] → [n]` extends
to the end points, and an edge goes to the product of the edges between the images of its end points. In the
colimit monoid all first edges become one element `x`, all last edges `z`, all interior edges `y`; subdividing
gives `x = xy`, `y = yy`, `z = yz`. So `C = ⟨x, y, z | xy = x, y² = y, yz = z⟩` (not checked that no further
relation holds). The rewriting system `xy → x`, `yy → y`, `yz → z` is terminating and confluent (critical pairs
`xyy, yyy, yyz, xyz`). Over `Z`: `∂_2` sends each rule to `y`; `∂_3(xyy) = [xy] − [yy]`, `∂_3(yyy) = 0`,
`∂_3(yyz) = [yy] − [yz]`, `∂_3(xyz) = [xy] − [yz]`; so `H_1 = Z²` and `H_2 = 0`.

## Lead 5: the conditions on `F: Ty^op → Cat`

(b) `E_t` is the union of the full subcategories `E_t^{(n)}` on the indices `≤ n`; `E_t^{(n)}` is fibred over a
chain with initial object `t_n`, so `F(t_n) → E_t^{(n)}` has a right adjoint and is a homotopy equivalence.
`∫_{Ty} F` is the union of the `∫_{t_n↑} F` (`t_n↑ ⊂ t_{n+1}↑`, and every type lies in some `t_n↑`). The functor
`E_t → ∫_{Ty} F` maps `E_t^{(n)}` into `∫_{t_n↑} F`. So `B E_t → B∫_{Ty} F` is the sequential homotopy colimit of
the maps `BF(t_n) → B∫_{t_n↑} F`. (LOC) makes each of them a weak equivalence.

(a), sketch. A strict 2-functor on `𝕋y` sends comparable type maps to functors joined by a natural
transformation, hence to homotopic maps of nerves; since every `P(τ, σ)` is empty or contractible (PATHS C.P1), the
homotopy-coherent diagram of nerves factors through `R^op`. (DESC) ⟹ (LOC) needs: `(r↑)^op → (R_{≥ r})^op` is
homotopy final, that is, for `r ≤ s` the full subcategory of the types between `r` and `s` is weakly contractible
(Part B.4); then `∫_{r↑} F ≃ hocolim_{(R_{≥r})^op} Y = Y(r)`.

Presheaves of sets. A strict 2-functor with discrete values sends comparable type maps to the same map, and
`P(τ, σ)` is connected; so (2F) for a presheaf of sets `S` means that `S` factors through `R`. The representable
presheaf of `(+)` does not satisfy (𝒟) (PRETOT F.12: the maps `(0,0,0,1)` and `(0,1,1,1)` from `(+−+)` to `(+)` are
equalized by no map into `(+−+)`).
