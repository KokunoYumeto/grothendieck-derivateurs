# Answer to Derivateurs_expert_Q1 (which open subgroups give contractible categories of elements?)

From the Dérivateurs successor (Claude Fable 5.2, effort max), 13 November 2026. Status per part below. All by
hand; checked by nobody else. "T" = TOTAL_EXACT_2. Notation: `A_M` the finite closed subsets of `M` with all
(strong) embeddings; for an open `U ≤ G`, `T_{G/U}(B) = (G/U)^{G_B}`.

## A description that serves all three parts

`El(T_{G/U}) ≃ E_U`, where `E_U` has objects the finite closed `B` with `G_B ≤ U` and arrows `B → C` the maps `u|_B`,
`u ∈ U`, `uB ⊆ C`. (Send `(B, gU)` to `g^{-1}B`; an extension of an arrow is in `U` or not independently of its
choice, because `G_B ≤ U`.) The proof of T A.33 uses, of the free amalgam, only its functoriality: over non-empty
bases for the two comparisons `H → H^inj → T_S`, and over the empty base only to contract `A_M = E_G` itself. So,
with functorial amalgamation over non-empty bases, every action component is some `E_U`.

## Part 1 (the first case): settled, contractible

Age: finite linear orders with an equivalence relation `E`; `U` the stabilizer of a class. `T_{G/U}(B) = B/E` (a class
of `M` is fixed by `G_B` iff it meets `B`), so `El(T_{G/U})` has objects `(B, c)`, `c` a class of `B`, and arrows the
embeddings `f` with `f(c) ⊆ c'`.

- Order independent of `E`: `Φ(B, c) = (B ⊔ {*}, c ⊔ {*})` with `*` above all points of `B` and `* E b ⟺ b ∈ c`. It is
  a functor (`f ⊔ id_*` preserves and reflects `E` because `f` reflects `E`), with natural maps `(B, c) → Φ(B, c)`
  (inclusion) and `({*}, {*}) → Φ(B, c)` (`* ↦ *`). So the identity is homotopic to a constant: `El(T_{G/U})` is
  contractible.
- Classes convex: the same with `*` placed just above the class `c` (embeddings preserve the order of the classes).
  Here the age is Ramsey (Kechris–Pestov–Todorcevic, Corollary 6.8), so every category of elements is
  contractible anyway (T A.6, TOTASPH C.6).

In the independent case the next atom is different: for `U'` the stabilizer of an unordered pair of classes,
`El(T_{G/U'}) ≃ RP^∞`: the ordered pairs of distinct classes give a contractible category (two new points on top,
one in each class) on which `Z/2` acts freely. So that age is not quasi-filtered. In the convex case the classes
are ordered and the swap does not exist.

General statement behind it (a Lead of the prompt, with `π_1(E_U) = U/⟨G_B : G_B ≤ U⟩`): `E_U` is contractible when a
new element can be adjoined functorially to the imaginary that `U` stabilizes; it is a `K(Γ, 1)` when `U` is a finite
extension by `Γ` of a pointwise stabilizer (your reply).

## Part 2: true in the setting of the question; false without the functorial joint embedding

Hypothesis (WEI): every open `U` has a finite closed `F` with `G_F` normal of finite index in `U`.

- quasi-filtered ⟹ every open subgroup is a pointwise stabilizer: `E_U ≃ B(U/G_F)` (`U/G_F` acts freely on the
  contractible `F\A_M`; a point outside a finite closed `B` has an infinite `G_B`-orbit, so the `G_B`-fixed cosets
  are those with `gF ⊆ B`), and quasi-filtered means every action component is simply connected. Needs only strong
  amalgamation.
- every open subgroup a pointwise stabilizer ⟹ total: T A.33, which needs the functorial amalgam over non-empty
  bases and over the empty base.
- total ⟹ quasi-filtered: always.

So for an age with functorial free amalgamation (the setting of the question) and (WEI): quasi-filtered ⟺ total ⟺
every open subgroup is a pointwise stabilizer. Without the functorial joint embedding over the empty base the
middle term drops out: under functorial amalgamation over non-empty bases and "every open subgroup is a `G_F`", the
action components are the `E_{G_F}` (`F ≠ ∅`: initial object) and `E_G = A` itself. Hence

> `A` is total iff `BA` is contractible, and `A ∈ 𝒬_n` iff `BA` is `(n−1)`-connected.

Expected example: the category `C` of T A.11 (a linear order and an independent cyclic order). It has functorial
amalgamation over non-empty bases (in each cyclic gap and each linear gap of the base, one side first) and none over
the empty base; `BC` is simply connected with `H_2 = Z` (T A.11). If every open subgroup of its group is a `G_F`
(not checked; the bridge of T A.30 should go through with positions on a circle), then `C` is quasi-filtered and
not total: a second witness for `{total} ⊊ {quasi-filtered}`; (WEI) holds there and "quasi-filtered ⟺ total" fails.

## Part 3: yes for n = 2; open for n ≥ 3, reduced to the homotopy type of BA

- `n = 2`: for the age of T A.11 and `U = G`, `El(T_{G/G}) = C`, which is 1-connected and not 2-connected
  (`H_2(BC) = Z`; I expect `BC ≃ CP^∞`). This is unconditional given T A.11. It gives `C ∈ 𝒬_2 ∖ 𝒬_3` if the other
  action components are simply connected, which holds if every open subgroup is a `G_F` (previous paragraph).
- Finite extensions of pointwise stabilizers never contribute for `n ≥ 2` (your reply). Stabilizers of classes of
  equivalence relations with infinite classes give contractible `E_U` in the cases of Part 1.
- By the displayed statement, a class with functorial amalgamation over non-empty bases, all open subgroups
  pointwise stabilizers, and `BA` `(n−1)`-connected and not `n`-connected lies in `𝒬_n ∖ 𝒬_{n+1}`. So DER_FOLLOWUP A.3
  becomes, on this route: which homotopy types occur as `BA`? I have no example with `BA` 2-connected and not
  contractible. Two things that do not work: a class with two unrelated sorts has `BA ≃ BA_1 * BA_2`, but the
  objects with non-empty first sort form a cosieve equivalent to `A_1`, an action component; and products of
  cyclic orders give products of `CP^∞`.

In the prompt FRAISSE_EXACT: Lead 7 and Parts B.2, B.3, B.5, B.6 (every statement above is asked there as "prove or
refute"; `n ≥ 3` is B.6).
