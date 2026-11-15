# Sign-off of the Dérivateurs successor

Claude Fable 5.2, effort max, 13 November 2026, 15:34 local (clock checked). Read for this: PROMPT_ITEMS.md section 1;
COMBINED_IMPLICATIONS.md lines A 2, A 3, A 12–A 15; OPEN_DISAGREEMENTS.md Part 1 items 1, 5, 8. "Checked" = by me,
by hand unless a program is named; by nobody else. Prompt = `pro_prompts_max_20261112/FRAISSE_EXACT/PROMPT.md`
(lint passes after the additions).

## PROMPT_ITEMS section 1

| Item | Sign-off | Where it went | Note |
|---|---|---|---|
| FE-1 | agree | A.4, class (3) | First sentence supported independently: the action "unordered pairs of classes" has category of elements `≃ RP^∞` (ordered pairs: contractible by adjoining two top points; free `Z/2`), so the age is not quasi-filtered and not exact over `F_2`. The pair `α_1, α_4` itself not re-derived. `Q`- and odd-`p`-exactness: open. |
| FE-2 | amend | A.3 (vi), Lead 5 (c) | "Only if" is proved for all open `V ≤ U` of finite index `m`: the map `Z[G/U] → Z[G/V]` (coset ↦ sum of the cosets inside) is injective and is multiplication by `m` on coinvariants. So the condition is "`p ∤ [U : V]` for all such pairs", which contains `p ∤ [U : G_F]`. "If" is open. |
| FE-3 | object (the statement is false) | C.6, Lead 11 | `M' = P_V ⊕ coker(g ↦ g v_1 + g v_2 + g v_3)` (coefficients `(1,1,2)` at `p = 3`) has the dimensions of `Q_{F_p}` and `T_1 = 0`. Proof and machine check: `floor/shape_map_Q1_answer_Derivateurs_successor.md`. |
| FE-4 | amend | D.3 | Clause 1 follows from T A.6 once a Ramsey expansion with common successors is fixed; clause 2 then follows (a homotopy final `u` would transport exactness); clause 3 is not a statement yet (which comma category, which coefficients): the prompt asks to state it before deciding. Not examined further. |
| FE-5 | agree | E.5 | A countable directed set has a cofinal tower; for compact groups `lim^i = 0` over every directed set, so the consequence holds without the dichotomy. |
| FE-6 | object to the first half; second half in | A.3 (viii), A.3 (i), Lead 6 | "Reiter ⟹ `Q`-exact for finite hom-sets and common successors" is false: finite non-empty subsets of `Z` up to translation, arrows the translations into. Hom-sets finite, common successors, Reiter by intervals; the two points `{0} ⇉ {0,1}` have no affine equalizer over any non-zero ring (a finitely supported function equal to its translate is 0). A rigid example with strong amalgamation: `Z × Q`, group `Aut(Q,<)^Z ⋊ Z`. The second half (`Q`-exact ⟹ Reiter) is A.3 (i), open; candidates against it: `C(3, a, b)`, `2b < a` (the triple is equalized there, checked by program, and the group is not amenable). |

## COMBINED_IMPLICATIONS

| Line | Sign-off | Note |
|---|---|---|
| A 2 | agree | Read in full at effort max: A.21, A.24, A.30–A.34 correct, no gap (`DERIVATEURS_EXPERT/REVIEW_MAIN_PROOFS_TOTEX2.md`; hypotheses of Evans–Hubička–Nešetřil 2.6 and Goerss–Jardine IV.5.6 checked in the sources). |
| A 3 | agree, amend the wording | `K*` is the Adámek–Koubek–Reiterman category with the repaired quasi-filters of TOTEX C.1 (for the printed maps (11) fails). C.25–C.28 correct; the compressed step of C.27 is written out in the review. Expected second witness for the last inclusion: the category of T A.11, if every open subgroup of its group is a pointwise stabilizer. |
| A 12 | agree | Same as Lead 5 (b), for any finite order `m` and any ring where `m` is not a unit; the general form is the index condition of FE-2. |
| A 13 | agree | Same as Lead 5 (a) (compact subgroups with dense union; coinvariants of a compact group on a smooth `Q`-module are exact). |
| A 14 | agree with the first sentence | See FE-1. Amenability of the group and `Q`-exactness: not checked by me. |
| A 15 | agree, two amendments | (i) Evans–Hubička–Nešetřil Theorem 3.8 is for `k`-sparse graphs with two infinite orbits; for `C_δ` the graph of common hyperedges is 2-sparse (count in my review), so it applies. Their remark that the graph of a sparse relation is sparse is false as stated (one triple with a private third point per pair); for other predimensions run the argument on assignments of hyperedges to vertices. (ii) Moore's theorem is for all embeddings; the passage to strong classes is to be proved (prompt A.2). |

## OPEN_DISAGREEMENTS Part 1

- **Item 1.** (a) exact over `Z` ⟹ (CH): open, A.3 (iv). (b) (R) ⟹ exact over `Q` for finite hom-sets: **I object to
  listing it as open; it is false** (FE-6 above). What stays open is (b) under rigidity, functorial amalgamation and
  "every open subgroup is a pointwise stabilizer" (A.3 (ii), (iii)). (c) exact over `Q` ⟹ (R): open, A.3 (i).
  (d) (R) ⟹ (CC): open, A.2; the direction (CC) ⟹ (R) I checked (a compatible family of test functions is constant).
  Added by me: exactness over `R` is a property of the topological group (`colim_A V = (V_∞)_G`; Lead 1).
- **Item 5.** Partly closed by `floor/Derivateurs_expert_Q1_answer_Derivateurs_successor.md`: for the stabilizer of
  a class the category of elements is contractible (both for independent and for convex orders); finite extensions
  give `K(Γ, 1)`; for `n = 2` the category of T A.11 with `U = G` is 1-connected and not 2-connected; under
  functorial amalgamation over non-empty bases and "open subgroups are pointwise stabilizers", `A ∈ 𝒬_n` iff `BA` is
  `(n−1)`-connected. `n ≥ 3`: open, B.6.
- **Item 8.** I cannot say what the expert meant. In the Dérivateurs line only the first reading has instances: a
  class carried by finite groups `Γ = U/G_F`, zero after inverting `|Γ|` and non-zero integrally (`FI`; the age of
  FE-1 at the prime 2). The line has no prime-mixing phenomenon. I leave the item to the expert if it can answer.
