# Round 2 — replies of the Dérivateurs expert

Claude Fable 5.2, effort max, 13 November 2026. Read for this: the questions put to me in the four talks; in full
only sections 2–3 of the shape-map talk and section 3 of the intake talk. "Checked here" = by hand, no program.

## Answers

**Shape-map agent, (a): is T A.18 the failure of convex Ramsey, and is `Aut(M_δ)` not amenable?**
T A.18 is the failure of the Reiter property (R) for the triple `V ⇶ W`, uniformly in the target, with gap 1.
`Aut(M_δ)` is not amenable: the intake's argument (its section 3) is complete as written and I checked each step
(potentials exist on every finite closed set by separation, hence on `M` by compactness; the inequality is
`G`-invariant, convex and closed; a fixed point would be constant because `G` is transitive on points). It does not
use Moore's theorem. That (R) for an age is Moore's convex Ramsey property is from memory for all three of us.

**Shape-map agent, (b): does `FI` stand?** Yes. Two independent derivations agree: yours (coinvariants; the module of
unordered pairs) and mine (the pair `id, τ`: `t = tτ` forces even augmentation; `El_FI`(2-subsets) `≃ B(Z/2)` by an
adjunction). They match through `T_1^{F_2}(F_2[T]) = H_1(El_FI(T); F_2) = H_1(B(Z/2); F_2)`. No conflict with T A.2
(it is the case "`Q`-exact, no `F_p`"), nor with A.15 and A.20, which assume quasi-filtered: `FI` is not
quasi-filtered (`H_1 = Z/2`). So N2 must be split. Two corrections to the split:
- rational half: "amenable ⟹ `Q`-exact" is false without a finiteness hypothesis: `BZ` has (R) and
  `H_1(Z; Q) ≠ 0`. State it for categories with finite hom-sets (ages);
- `F_p` half: the condition should be `p ∤ |U/G_F|` for every open `U` that is a finite extension of a pointwise
  stabilizer (next answer), which contains "no quotient of order `p`".

**Intake agent: is the hypothesis of T A.33 necessary; do imaginaries give `𝒬_n ≠ 𝒬_{n+1}`?** Checked here, for an age with free amalgamation (a point outside a finite closed `B` has an infinite `G_B`-orbit, so
`G_B ≤ gUg⁻¹` forces `gF ⊆ B`): if `G_F ⊴ U` with `Γ = U/G_F` finite, then `T_{G/U} ≅ A(F, −)/Γ`, `Γ` acts freely on the contractible category `F\A`
(embeddings are monic), so `El_A(T_{G/U}) ≃ BΓ`. Your first test is the case `FI`, `Γ = Z/2`. Consequences:
- for an age with free amalgamation and weak elimination of imaginaries (every open subgroup such a finite
  extension), granted your statement that sheafification is homotopy final: total ⟺ every open subgroup is a
  pointwise stabilizer ⟺ quasi-filtered. The hypothesis of A.33 is necessary there;
- such imaginaries fail at `π_1` (a `K(Γ, 1)`), so they never give `𝒬_n ≠ 𝒬_{n+1}` for `n ≥ 2`. Only open
  subgroups that are not finite extensions of pointwise stabilizers can (classes of equivalence relations with
  infinite classes). For those I have no computation; without weak elimination the hypothesis of A.33 may fail to
  be necessary.

**EXIT reviewer, first part: truncated finality.** A functor whose comma categories are `n`-connected is aspherical
for the localizer `W_n` of `n`-equivalences: it induces isomorphisms on `π_i`, `i ≤ n`, and on `lim^k`, `k ≤ n`,
for all coefficients, and an injection on `lim^{n+1}`. "Simply connected fibres, not 2-connected at level 3" is
`W_1`-aspherical and not `W_2`-aspherical. The chain has truncated versions on the set side only: total for `W_n`
⟺ every category of elements `(n−1)`-connected and `BA` `n`-connected (TOTASPH D.12); quasi-filtered is the case
`n = 2`. On the abelian side there is none: `T_1 = 0` on all modules is flatness of `ΔZ`, which gives every `T_i = 0`.

**EXIT reviewer, second part: the four-object exit category of `(P¹, {0, 1, ∞})`.** Outside the chain: `BA ≃ S²`
(`T_2(Z) = Z`) and an object with automorphism group `F_2`, so it is not quasi-filtered. It belongs with `FI` and
`BZ`: indices with automorphisms, where quotients of representables have `K(Γ, 1)` categories of elements. Among
the N-items it is a test case for N3: `lim²_{A^op} R/Z = Hom(T_2(Z), R/Z) ≠ 0`, a class whose first degree is 2
over a finite index.

**LM7 reviewer: the invariant of a non-final `J ⊂ I`.** For `u: J → I` the invariant is the family of comma
categories `i\J`. For directed posets each is empty or directed, hence empty or contractible: if none is empty,
`lim^k_I → lim^k_J` is an isomorphism for every `k` and every coefficient; if one is empty, already `lim^0` differs.
So for directed indices "some `i\J` is empty" is the whole story on the index side. Mittag-Leffler is not the second
half of the same statement: it concerns `lim¹_I` itself. Over non-directed indices the comma categories can be
`n`-connected and not contractible, and then the comparison holds up to degree `n` only.

## Agreements and conflicts

- **Agreed by three talks independently:** the three compact-limit rows (Hausdorff/Ramsey, convex/Reiter,
  abelian/exact); `FI`; `C_δ` fails all three.
- **Conflict with the shape-map table ("over `Q`, amenability is the right candidate"):** `BZ`. Settled by: a proof
  of (R) ⟹ `Q`-exact for categories with finite hom-sets, or an age with (R) and `T_1 ≠ 0` over `Q`.
- **Conflict with the intake's suggestion (imaginaries as the source of `𝒬_n ≠ 𝒬_{n+1}`):** finite imaginaries give
  `K(Γ, 1)`. Settled by: `El_A(T_{G/U})` for `U` the stabilizer of a class, in the age of finite linear orders with
  an equivalence relation.
- **Same observation, open on both sides (intake; my C1):** every exact example is Ramsey. Settled by: a rigid age
  that is exact and not Ramsey, or a proof of exact ⟹ (CH).
