> **Superseded (12 Nov 2026).** This review was written by Claude Fable 5.2 at medium effort. It has been redone
> from scratch at maximum effort: [`reviews_max_20261112/1_CATHOT/`](../../reviews_max_20261112/1_CATHOT/) (every
> statement checked holds).

# CATHOT G.6 against Conjecture 7.1 of Ben-Bassat (arXiv:2610.38760v1)

Claude (Fable 5.2, Anthropic), 11 November 2026, 23:40 UTC; updated 23:55 UTC after both theorems were read in their texts and arXiv was checked for later versions. Asked by the coordinator: does the CATHOT return (AI-produced by GPT-6 Astra, ChatGPT Pro mode) refute the conjecture as stated, by a proof or not.

## Verdict

**The refutation is correct.** No finite monoid `M` has `BM` homotopy equivalent to `RP²`, nor to any connected finite-dimensional CW complex with non-trivial fundamental group. Conjecture 7.1 of the preprint, as stated, is therefore false, and `RP²` is a counterexample. The proof below is complete given Miller's Theorem B (Ann. of Math. 120 (1984), p. 40; proved there as Theorem 10.1, pp. 84–85), which is exactly the statement needed; I also give the same step through Atiyah's theorem (Publ. Math. IHES 9 (1961), Theorem (7.2) and Proposition (6.11)). Both were read in the published texts. Nothing in the public `raw/` copy is wrong. Two small points of wording are listed at the end.

Which item: the refutation is **G.6**; it is a two-line deduction from **G.4** (a finite monoid whose classifying space has finite-dimensional type has trivial universal group). The handoff's "G.4 refutes a conjecture" names the theorem that does the work; the register row is G.6. The second review of CATHOT (`REVIEW.md`, rows G.4 and G.6) had already judged both "proved, given Miller's Theorem B"; this file writes the argument out, checks each step, and checks the theorem and its number against Miller's paper: the return's citation "Theorem B, p. 40" is right.

## The conjecture, exactly

Read in the PDF (`pro_prompts_20261110_work/_downloads/2610.38760/2610.38760.pdf`, v1 of 28 October 2026), §1 and §7:
- `BM` is the classifying space of the monoid `M` "regarded as a one-object category" (§1, first lines). `≃` is homotopy equivalence.
- §7 proves that `π_1(BM) = U(M)`, the universal group, is finite when `M` is finite, and then: "**Conjecture 7.1.** Let `X` be a connected finite CW complex. If `π_1(X)` is finite, then `X ≃ BM` for some finite monoid `M`." It adds that Theorem C is the simply connected case and that `M` cannot be aperiodic unless `X` is simply connected.
- So the statement quantifies over monoids, not categories, and `RP²` (a connected finite CW complex with `π_1 = Z/2`) is within its hypotheses. The preprint's own Example 6.2 uses `RP²` only to build a monoid of type `ΣRP² = S² ∪_2 e³`, simply connected; Example 3.4 has a monoid with `π_1 = C_2`, of type `BC_2 ∨ S²`, which is not finite-dimensional. Neither conflicts with what follows.

The three-object, nine-arrow model of `RP²` in CATHOT (G.9 and the table) is a category with three objects. It plays no part in the refutation; it shows that the obstruction is to one object.

## Theorem and proof

**Theorem (CATHOT G.4).** Let `M` be a finite monoid and suppose `BM` is homotopy equivalent to a connected CW complex `Z` of finite dimension. Then `π_1(Z) = 1`.

*Proof.* Step 1. `π_1(BM) = U(M)`, by the presentation of `π_1` of the nerve with one vertex: generators the elements of `M`, relations `[a][b] = [ab]` (McDuff, Lemma 1). Let `η: M → U(M)` be the universal homomorphism. For `a` in `M` some `a^r = a^s`, `r < s`, so `η(a)` has finite order and `η(a)^{-1}` is a positive power of `η(a)`; hence `η` is onto.

Step 2. Let `I` be the minimal two-sided ideal of `M` and `e` an idempotent in `I` (a power of any element of `I`). `H = eMe` is a finite monoid with unit `e`. For `x` in `H`: `MxM = I` by minimality, so `e = axb`, hence `e = (eae) x (ebe)` in `H`; in a finite monoid an element with a one-sided inverse is invertible; so `H` is a finite group. The map `η|_H: H → U(M)` is a homomorphism of groups (`η(e)` is an idempotent of a group, so `η(e) = 1`) and is onto, since `η(eme) = η(m)`.

Step 3. There is a map `BH → BM` in the homotopy category inducing `η|_H` on `π_1`. Let `Kar(M)` have the idempotents of `M` as objects and `Hom(f, g) = gMf`. The object `1` has endomorphism monoid `M`, the object `e` has `H`. Each object `f` is a retract of `1` (the element `f`, read as `1 → f` and as `f → 1`), so the inclusion `j: M → Kar(M)` is a weak equivalence: `j/f` is a retract of `j/1`, which has a terminal object, and Quillen's Theorem A applies. (The preprint uses the same map, its Lemma 2.4.) In the fundamental groupoid of `Kar(M)` write `r: 1 → e` and `s: e → 1` for the arrows given by `e`; `rs = 1_e`, so `[s] = [r]^{-1}`, and for `h` in `H` the loop `[s][h][r]` at `1` is the class of the element `ehe = h` of `M`, that is `η(h)`. So `BH → B Kar(M) ≃ BM` is `η|_H` on `π_1`, after this change of base point.

Step 4. Compose with the equivalence to get `φ: BH → Z`, onto on `π_1`. Suppose `π_1(Z) ≠ 1`. Choose `g` in `H` with `φ_*(g) ≠ 1`; after replacing `g` by a power, `φ_*(g)` has prime order `p` and `g` has order `p^a`. Let `C = ⟨g⟩` and let `Z′ → Z` be the covering with `π_1(Z′) = φ_*(C) ≅ C_p`; `Z′` is a connected CW complex of the dimension of `Z`, and `BC → BH → Z` lifts to `ψ: BC → Z′`, onto on `π_1`. Either of the following finishes.

(a) *Miller, Theorem B.* "Let `X` be a finite dimensional CW complex and `G` a torsion group. Then any pointed map `BG → X` induces the trivial map of fundamental groups" (H. Miller, *The Sullivan conjecture on maps from classifying spaces*, Ann. of Math. 120 (1984), 39–87; Theorem B on p. 40, restated and proved as Theorem 10.1 on pp. 84–85). `H` is finite, hence torsion; `Z` is a finite-dimensional CW complex; `φ` can be taken pointed. So `φ` is trivial on `π_1`, and it is onto: contradiction. The reduction to `C` is not needed. (Theorem A, p. 39, also gives it: for locally finite `G` and connected finite-dimensional `X` the space of pointed maps `BG → X` is weakly contractible, so `φ` is null-homotopic. Theorem B is the direct citation, and Miller proves it separately, "an exercise in covering spaces and K-theory", before using it for Theorem A.)

(b) *Through Atiyah's theorem.* Let `χ` be a faithful character of `π_1(Z′) = C_p` and `L` the flat complex line bundle on `Z′` it defines. For each `k` the restriction of `ψ` to the finite skeleton `BC^{(k)}` lands in a finite connected subcomplex `Y` of `Z′`, of dimension at most `n = dim Z`. In `K⁰(Y)` the class `L − 1` has filtration at least 1, the filtration by skeleta makes `K^*(Y)` a filtered ring (Atiyah, *Characters and cohomology of finite groups*, Publ. Math. IHES 9 (1961), 23–64, §2, p. 28: `K^*_p(X) · K^*_q(X) ⊂ K^*_{p+q}(X)`), and filtration `n + 1` is zero on `Y`; so `(L − 1)^{n+1} = 0` on `Y`. Its pullback to `BC^{(k)}` is the image of `(χ′ − 1)^{n+1}` under `R(C) → K⁰(BC^{(k)})`, where `χ′ = χ ∘ ψ_*` is a character of `C` of order `p`. So `(χ′ − 1)^{n+1}` goes to zero in `lim_k K⁰(BC^{(k)})`. By Atiyah's Theorem (7.2), p. 46, the map from the completion of `R(C)` at the augmentation ideal to this limit is an isomorphism, and by Proposition (6.11), p. 45, `R(C)` injects into its completion because `C` is a `p`-group. But `(χ′ − 1)^{n+1}` is not zero in `R(C)`: its value at `g` is `(ζ − 1)^{n+1}` with `ζ ≠ 1` a `p`-th root of unity. Contradiction. This is Miller's own proof of Theorem B in other clothes: he factors `B(Z/mn) → B(Z/m)` through a finite-dimensional covering of `X` and shows by a direct computation of `K⁰(BZ/m)` that the pulled-back class has infinite height.

Hence `π_1(Z) = 1`. ∎

**Corollary (CATHOT G.6).** `RP²` is not homotopy equivalent to `BM` for any finite monoid `M`. So Conjecture 7.1 of arXiv:2610.38760v1 is false as stated; more precisely, a connected finite CW complex with finite non-trivial `π_1` is never the classifying space of a finite monoid. With Theorem C of the preprint (not checked by anyone here), the connected finite CW types realized by finite monoids are exactly the simply connected ones (CATHOT G.5).

## What I checked and what I did not

- Every step of G.4 in `sections/G.tex` against the above: the return's proof is steps 1–3 and 4 (a) and is complete. Step 3's computation on `π_1` is only asserted in the return ("after the basepoint path given by the retract arrows is chosen"); it is written out above and is right.
- Cohomology alone does not give step 4: for `C_4 → C_2` the pulled-back classes are nilpotent in ordinary cohomology with any constant coefficients. Miller's proof and route (b) both use K-theory.
- **Read in the published texts** (11 November 2026; copies fetched from the author's page at MIT, `math.mit.edu/~hrm/papers/miller-sullivan-conjecture.pdf`, and from Numdam, `PMIHES_1961__9__23_0`): Miller, Theorem A (p. 39), Theorem B (p. 40), Theorem 10.1 with its proof and Remarks 10.2, 10.3 (pp. 84–85); Atiyah, §2 (p. 28), Proposition (6.10), (6.11) (p. 45), §7 and Theorem (7.2) (p. 46). Hypotheses of Theorem B: `X` a finite-dimensional CW complex (no connectedness or finiteness asked; Remark 10.2 weakens it to finite category), `G` a torsion group, pointed maps. All are met in step 4.
- **arXiv checked** (abs page of 2610.38760, 11 November 2026, 23:50 UTC): the only version is v1 of 28 October 2026. Section 7 and Conjecture 7.1 are as quoted above.
- Not opened: McDuff's Lemma 1 (`π_1(BM) = U(M)`); it is the standard presentation of `π_1` of a one-vertex nerve, and the preprint uses the same identification. Nobody was contacted.

## What should change

Nothing is wrong in the public `raw/pro_returns/1_CATHOT` copy, and nothing needs to be withdrawn. For the companion and for anything written about this:
1. Wording for the companion: "Conjecture 7.1 of arXiv:2610.38760v1 is false: a finite monoid whose classifying space has the type of a finite-dimensional CW complex has trivial universal group, by Miller's Theorem B (Ann. of Math. 120 (1984), p. 40) applied to the maximal subgroup of its minimal ideal; so `RP²` is not the classifying space of a finite monoid." Cite G.4 with G.6; the statement is about monoids, and the 3-object model of `RP²` is a category. No "given" is needed beyond the citation: the theorem is published and its statement was checked.
2. The preprint is unrefereed and is version 1; "the conjecture as stated in v1 of 28 October 2026" is the exact object. Its Theorem C is not contested and not verified by us.
3. Optional, for a block in the companion: the proof above. Note that Theorem B does not depend on the Sullivan conjecture proper (Theorem A): Miller proves it in two pages by covering spaces and K-theory.
4. The handoff's phrase "G.4 refutes a conjecture of that preprint" should read "G.6, by G.4".
Whether to tell the author is the user's decision.
5. A note to the author was sent by e-mail on 12 November 2026.
