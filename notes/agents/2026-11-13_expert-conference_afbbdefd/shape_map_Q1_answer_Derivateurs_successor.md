# Answer to shape_map_Q1 (do objectwise sizes determine the class over C_δ?)

From the Dérivateurs successor (Claude Fable 5.2, effort max), 13 November 2026. Status: settled, by hand, with a machine check of the injectivity on small objects; checked by
nobody else. "T" = TOTAL_EXACT_2; the proof of T A.24 used below was read in full by me today
(`REVIEW_MAIN_PROOFS_TOTEX2.md`).

## Answer

**No.** The statement is false already in the first case: there is `M'` with the same objectwise dimensions as
`Q_{F_p} = coker(D)` and `T_1(M') = 0`.

## The example

Work over a field `k` (in particular `F_p`). `A = C_δ`, `V` the point, `W` the single hyperedge, `v_1, v_2, v_3: V → W`,
`P_V = k[A(V, −)]`, `P_W = k[A(W, −)]`.

- `D: P_W → P_V²`, `g ↦ (g v_2 − g v_1, g v_3 − g v_1)`, `Q = coker D`. T A.24: `D` is objectwise injective and
  `T_1(Q) = k`. So `dim Q(X) = 2|A(V, X)| − |A(W, X)|`.
- Choose `α, β, γ ∈ k^×` with `α + β + γ ≠ 0`: `(1, 1, 1)` if the characteristic is not 3, `(1, 1, 2)` if it is 3
  (for `F_2`: `(1, 1, 1)`, sum 1). Put `D'': P_W → P_V`, `g ↦ α g v_1 + β g v_2 + γ g v_3`, and `M'' = coker D''`.
- `D''` is objectwise injective. Proof: let `z = Σ c_g g ≠ 0` in `k[A(W, X)]`. The arrows `g` of its support are
  distinct hyperedges of `X`; by positivity (`2v > 3r` for `r` hyperedges on `v` vertices) some vertex `x` lies on
  exactly one of them, `x = g_0 v_i`. The coefficient of the basis element `x ∈ A(V, X)` in `D''(z)` is
  `c_{g_0} κ_i` with `κ = (α, β, γ)`, non-zero. (The same private vertex as in T A.24.)
- `T_1(M'') = 0`. Proof: `0 → P_W → P_V → M'' → 0` is a projective resolution, `colim P_W = colim P_V = k`, and
  `colim D''` is multiplication by the augmentation `α + β + γ ≠ 0`, injective. So
  `T_1(M'') = ker(colim D'') = 0` (and `colim M'' = 0`).
- `M' = P_V ⊕ M''`. Then `dim M'(X) = |A(V, X)| + (|A(V, X)| − |A(W, X)|) = dim Q(X)` for every object `X`,
  `T_1(M') = 0`, `T_1(Q) = k`.

Dually (`lim^i_{A^op} Hom(M, k) = Hom(T_i(M), k)`): `F = Hom(Q, F_p)` and `F' = Hom(M', F_p)` are diagrams of
finite-dimensional `F_p`-spaces on `C_δ^op` with `dim F(X) = dim F'(X)` for all `X`, `lim^1 F = F_p`, `lim^1 F' = 0`.

## What it says

Both `Q` and `M'` are cokernels of objectwise injective maps `P_W → P_V²` (for `M'` the map `(D'', 0)`). `T_1` of such
a cokernel is the kernel of the induced map `k → k²` on colimits, which is given by the augmentations of the two
components of the column: `(0, 0)` for `D`, `(α + β + γ, 0)` for `(D'', 0)`. So over `C_δ` the class is read from the
image of the column in the colimit, not from any count of dimensions: (S-b) holds on the colimit side, as the
determinant-line reading predicted. Over `Z` the same `M''` with `(1, 1, 1)` has `T_1 = 0` and `colim M'' = Z/3`.

Machine check (my own program, `derivateurs_companion_20261109/pro_prompts_max_20261112_work/FRAISSE_EXACT/checks_drafter/lead11_check.py`, output beside it): at all 31,178 labelled objects of `C_δ` with at most 7 points, `D` and `D''` are injective over `F_2`, `F_3` and `F_5`, so the two dimension functions agree there. The proof above covers every object.

In the prompt FRAISSE_EXACT this is Lead 11 and Part C.6 (to be checked by GPT-6 Astra with the dual diagrams and
the cocycle written out).
