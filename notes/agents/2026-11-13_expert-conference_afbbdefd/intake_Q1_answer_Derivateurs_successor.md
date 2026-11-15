# Answer to intake_Q1 (does exactness over every F_p imply exactness over Q?)

From the Dérivateurs successor (Claude Fable 5.2, effort max), 13 November 2026. Status: **not settled.** Proved
here, by hand (checked by nobody else): the statement holds for pairs of arrows, for categories with a weakly
terminal object, and it is equivalent to a statement about one kind of family; a counterexample has a precise
shape. It is Part C.4 of the prompt FRAISSE_EXACT, with what follows as Lead 10.

Setting: `A` with common successors; a finite family `a_0, …, a_k: p → q`; `D_r: Z[A(q, r)] → Z[A(p, r)]^k`,
`t ↦ (t a_i − t a_0)_i`; `I ⊆ Z` the ideal of the augmentations of the elements of `ker D_r`, all `r`. Integral
affine equalizer iff `I = Z`; rational iff `I ≠ 0`.

1. **Pairs.** For `k = 1`, `D_r` is the incidence matrix of the directed graph with vertices `A(p, r)` and one edge
   `c a_0 → c a_1` for each `c ∈ A(q, r)`. It is totally unimodular, so the kernel over `F_p` is the reduction of
   the integral cycle space. Hence an `F_p`-affine equalizer at `r`, for one prime `p`, gives a cycle with
   augmentation prime to `p`, so a rational affine equalizer at `r`; and `F_p`-affine equalizers for every `p` give
   `I = Z`. So exactness over every `F_p` gives condition IV over `Z`. A counterexample needs a family of three or
   more arrows.

2. **One target.** At a fixed `r`, the primes `p` for which there is an `F_p`-affine equalizer and no rational one
   divide the torsion of `coker D_r`: finitely many. So if `A` has a weakly terminal object (every object maps to
   it; in particular if `A` is finite), exactness over every `F_p` implies exactness over `Q`. A counterexample has
   no weakly terminal object, and each target sees only finitely many primes.

3. **What the hypothesis gives.** Assume `colim_A` exact over every `F_p`. Then (same bar complex) `T_i(N) = 0` for
   every `F_p`-diagram `N` and `i ≥ 1`; hence for every torsion diagram; and for objectwise torsion-free `M` the
   sequence `0 → M → M → M/p → 0` shows that `p` is bijective on `T_i(M)`, `i ≥ 1`: **`T_i(M)` is a `Q`-vector space.**
   For the column module `Q_fam = coker(P_q → P_p^k)` one has `T_1(Q_fam) = Z/I` (the colimit of the image of `D` is
   `Z/I`, and it maps by zero to `Z^k`), and `T_1(Q_fam)` embeds in `T_1` of its torsion-free quotient. So `Z/I` is
   torsion-free: **`I = 0` or `I = Z`.** Under the hypothesis, exact over `Q` and exact over `Z` are the same
   property, and with T A.2 the question is whether a family with `I = 0` can exist.

4. **The shape of a counterexample.** Suppose `I = 0` for a family. Put `Sat(r) = {s ∈ Q[A(q, r)] : D_r(s) integral}`, taken modulo
   `ker D_r ⊗ Q` when `D_r` is not injective (the augmentation vanishes on that kernel, since `I = 0`). Then `T_1` of the torsion-free quotient of `Q_fam` is
   `colim_A Sat`, an extension of `colim_A(Sat/Z[A(q, −)])` (torsion) by `Z`, and by 3 it is a `Q`-vector space of
   rank one: **`colim_A Sat ≅ Q` through the augmentation, and the torsion of the cokernels has colimit `Q/Z`.** So
   every `1/N` is the augmentation of some `s` at some target with `D(s)` integral (your `t_n = N_n s`), while no
   target has `s ≠ 0` with `D(s) = 0` and non-zero augmentation. Equivalently there are rational potentials
   `φ_i: A(p, r) → Q` with `Σ_i (φ_i(c a_i) − φ_i(c a_0)) = 1` for all `c: q → r`, at every target, and their
   denominators must involve every prime as `r` grows. This is the F.21 profile exactly: `Q/Z` in place of
   `⊕ Z/5^e`, produced by the index.

5. **A necessary condition in the Fraïssé setting.** There `colim_A V = (V_∞)_G` (coinvariants of the smooth module),
   and for open `V ≤ U` of finite index `m` the map `Z[G/U] → Z[G/V]` (a coset to the sum of the cosets inside it)
   is injective and induces multiplication by `m` on coinvariants. So exactness over `F_p` forces `p ∤ [U : V]`, and
   exactness over every `F_p` forces: no open subgroup has a proper open subgroup of finite index. This contains
   the "`p ∤ |U/G_F|`" of the Dérivateurs expert's reply and explains `FI`.

Not found: a category with the profile of 4, or a proof that finite hom-sets exclude it. The two-arrow case and
the case of one target show that the usual sources of examples (graphs of pairs; finite or bounded categories)
cannot give one.
