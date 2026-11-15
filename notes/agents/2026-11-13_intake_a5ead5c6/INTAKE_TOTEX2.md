# Intake of TOTAL_EXACT_2 (TOTEX2), 89 rows

Reader: Claude Fable 5.2 (Anthropic), effort high, 13 Nov 2026. Return: GPT-6 Astra (OpenAI, ChatGPT Pro mode),
checkpoint 03 = deliverable (`...\TOTAL_EXACT_2\checkpoints\TOTEX2_checkpoint_03_20261113T1144Z_unzipped\TOTEX2\`).
This is an intake at effort high, not the expert's review. The field expert reads it at effort max.

## Result

- CONSISTENT 89 (74 Proved, 13 Refuted, 2 Known). DOUBT 0. WRONG 0. OPEN 0.
- Of the 89: **47 with the proof read and followed here or recomputed** (basis P or C), **42 at statement level
  only** (basis S: the
  statement, its hypotheses and its place in the dependency chain were read; the proof was not).
- The main theorem A.1 (a total category that is not exact) rests only on A.21, A.24, A.30, A.31, A.32, A.33
  (and A.34, which assembles them). All six were read in full and every step followed. It does not rest on the
  necklace estimate A.22 or on quasi-filteredness A.23 (which also follows from totality), nor on any program.
- Own checks, written and run here (`checks\check_totex2_finite.py`, `.out`): A.4 (matrix, determinant 3, Smith
  form 1,1,1,3), A.9 and A.10 (both certificates: induced paths, augmentation 1, equal marginals), A.11 (`d_2 = (1,1)`,
  `d_3 = 0`; the three cut identities on all 1,904 embeddings into targets of 4 to 6 points), C.6 (15 vertices,
  20 edges, connected, `H_1 = Z^6`). The return's code was not run.

Basis codes: **P** proof read and followed; **S** statement level only; **C** confirmed by own script; **A** rests
on the Adámek–Koubek–Reiterman invariants (10), (11), (c_m) and TOTEX Proposition C.1, taken as stated (not re-read
here); **L** rests on a cited source not opened here; **M** the correspondence with the manuscript was not checked.

## What the main theorem is, in the form I checked it

`C_δ`: finite linearly ordered 3-uniform hypergraphs with `δ(U) = 2|U| − 3|E(U)| > 0` for all non-empty `U`;
arrows: increasing induced embeddings with strictly closed image (`δ(U) > δ(A)` for `A ⊊ U`).

1. A.24 (no affine equalizer of the three point arrows `v_i: V → W`, over any non-zero ring). Arrows `W → X` are
   distinct hyperedges; `r` of them span `v` vertices with `2v > 3r`, so one vertex lies on exactly one of them and
   its coefficient cannot cancel. So `D: R[A(W,−)] → R[A(V,−)]²` is injective at every object; `colim D = 0`;
   `T_1(coker D) = R`. Checked line by line.
2. A.30 (alternating bridge). Circle of `E, D_1, …, D_{2N−1}`, glued over `B` and `C` alternately. Fibres are full
   circles (`F = B ∩ C`) or arcs of at most 3 indices; factors are induced; positivity by cutting one overlap
   (loss at most `2m`) and counting first appearances (at least `s/3`), with `s > 3(δ(E) + 2m)`; the order by linear
   interpolation of coordinates. Checked, including the end identifications through `E`.
3. A.31 `⟨G_B, G_C⟩ = G_{B∩C}` (telescoping along the bridge inside the Fraïssé limit) and A.32 (every open subgroup
   is a pointwise stabilizer `G_F`; minimal support, rigidity of finite orders). Checked.
4. A.33. (i) Non-empty full cosieves of slices `P/A` are contractible (functorial free amalgam with a fixed
   object, two natural transformations). (ii) `H → H^inj` (eventual equality) and (iii) `H^inj → T_S`,
   `T_S(B) = S^{G_B}`, are homotopy final on categories of elements (Quillen A, comma categories = such cosieves).
   (iv) `T_{G/G_F} ≅ A(F, −)` by `Fix(G_B) = B`. Checked. Remark of the reader: (ii) and (iii) are the two steps of
   the associated sheaf for the atomic topology on `A^op`; the theorem says that sheafification
   `[A, Set] → Cont(G)-Set` is a weak equivalence on categories of elements, and that every atom of the atomic
   topos is representable or terminal.

## Table

| Id | Return | Claim (short) | Verdict | Basis | Reason / remark |
|---|---|---|---|---|---|
| A.1 | Refuted | `C_δ` is total; `v_1,v_2,v_3` have no affine equalizer; colim not exact | CONSISTENT | P | assembles A.21, A.24, A.34 |
| A.2 | Proved | exact over `Z` iff exact over `Q` and every `F_p` | CONSISTENT | P | torsion filtration and `M_tf ⊂ Q ⊗ M_tf`; equal bar complexes |
| A.3 | Refuted | `C_δ` non-exact over every non-zero ring; `T_1(Q_R) = R`, pd 1 | CONSISTENT | P | A.24 with coefficients |
| A.4 | Refuted | `Q_a` outside the resolving class of P1 (finite filtered category, `Z/3` torsion) | CONSISTENT | P, C | table, determinant 3 and Smith form recomputed |
| A.5 | Refuted | same over `Q` (object with automorphism group `Z`; eigenvalue −2) | CONSISTENT | P | invariant `ker(T^{2n} − 2^{2n}) = 0` closed under each operation; matrix rechecked by hand |
| A.6 | Proved | morphism Ramsey + common successors ⇒ exact (circle-valued character, `(3k+1)^k` colours) | CONSISTENT | P | `θ ∈ [1/3,1/2]` against a sum of size `< k/(3k+1)` |
| A.7 | Proved | scope remark on finite hom-sets | CONSISTENT | P | a remark, labelled Proved |
| A.8 | Proved | ordered graphs with induced embeddings are exact | CONSISTENT | P, L | Hubička–Nešetřil 2019, Cor. 4.3 not opened here |
| A.9 | Proved | vertex certificate in `r_6` | CONSISTENT | C | recomputed |
| A.10 | Proved | edge certificate in `r_7` | CONSISTENT | C | recomputed |
| A.11 | Refuted | linear + cyclic orders: `H_2(BC) = Z`, a 5-arrow family without equalizer | CONSISTENT | P, C | `d_2`, `d_3` and the cut identities recomputed |
| A.12 | Proved | finite-pattern Ramsey = morphism Ramsey for finite hom-sets | CONSISTENT | P | a definition with a one-line remark |
| A.13 | Proved | non-empty limits of compact Hausdorff `A^op`-diagrams ⇔ finite-pattern Ramsey | CONSISTENT | P | both directions followed (colourings as a compact diagram; simultaneous Ramsey; uniformities) |
| A.14 | Proved | either condition of A.13 ⇒ exact | CONSISTENT | P | A.6 with injectivity of `R/Z` |
| A.15 | Proved | quasi-filtered + fibres of size ≤ N ⇒ non-empty limit | CONSISTENT | P, L | Isbell–Mitchell 1976, Prop. 4.5 (as R5 of the prompt) |
| A.16 | Proved | pinning a coefficient in `Δ_inj` loses a set-colimit relation | CONSISTENT | P | valuation argument |
| A.17 | Refuted | total ⇏ compact-limit / Ramsey condition | CONSISTENT | P | A.34 + A.14 |
| A.18 | Proved | uniform gap: `‖μ_2−μ_1‖_1 + ‖μ_3−μ_1‖_1 ≥ 1` for probability combinations | CONSISTENT | P | layer-cake on the private-incidence count |
| A.19 | Refuted | compact convex `A^op`-diagrams over a total `A` can have empty limit | CONSISTENT | P | separation from A.18 |
| A.20 | Proved | quasi-filtered, `|M(a)| ≤ N` ⇒ `T_1 = 0`; total ⇒ all `T_i = 0` | CONSISTENT | P, L | quotient category with bounded homs is filtered (IM 1976, 4.5) |
| A.21 | Proved | closure calculus, free amalgam, I | CONSISTENT | P | submodularity; each inequality rechecked |
| A.22 | Proved | long necklace is positive, copies closed | CONSISTENT | P, A | estimate followed; visibility intervals taken from C.32 (not read) |
| A.23 | Proved | `C_δ` quasi-filtered | CONSISTENT | P, A | A.22 + C.33; also a consequence of A.34 |
| A.24 | Proved | the triple has no affine equalizer over any ring; `T_1(Q) = R` | CONSISTENT | P | private incidence, see above |
| A.25 | Proved | adjoining a loose path of length 3 keeps `B` closed | CONSISTENT | S | |
| A.26 | Proved | loose cycles of length ≥ 4: positive, atoms closed | CONSISTENT | S | 5-cycle with 3 up and 2 down edges checked by hand (pair equalizer exists) |
| A.27 | Proved | `colim K ≅ Z` for the binary cycle functor; binary `H_2 = 0` in `C_δ` | CONSISTENT | S | implied by A.34 |
| A.28 | Proved | functorial path cone | CONSISTENT | S | |
| A.29 | Proved | `El(H_12)`, `El(H_123)` contractible | CONSISTENT | S | implied by A.34 |
| A.30 | Proved | finite alternating bridge | CONSISTENT | P | see above |
| A.31 | Proved | `⟨G_B, G_C⟩ = G_{B∩C}` | CONSISTENT | P, L | Evans–Hubička–Nešetřil 2019, Th. 2.6 (existence of the limit) not opened; the construction is standard |
| A.32 | Proved | open subgroups are the `G_F` | CONSISTENT | P | |
| A.33 | Proved | open subgroups = `G_F` ⇒ total, for all `H` | CONSISTENT | P | see above; Quillen A in the form `d ↓ u` |
| A.34 | Proved | both predimension categories are total and non-exact over every ring | CONSISTENT | P | |
| B.1 | Refuted | triples: refuted in `C_δ`; three is least | CONSISTENT | P | pairs have equalizers under IV |
| B.2 | Proved | row presentation: `T_1, T_2, T_j` of `Z[H]` through `K` | CONSISTENT | S | = R7 of the prompt, extended to `k` |
| B.3 | Proved | Lead 1 | CONSISTENT | S | |
| B.4 | Proved | Lead 2; needs `aug z = 0` in the Tor formula | CONSISTENT | S | correction of the Lead's wording noted |
| B.5 | Proved | Lead 3 | CONSISTENT | S | the case used in A.24 was checked directly |
| B.6 | Proved | Lead 4, both statements | CONSISTENT | S | |
| B.7 | Proved | Lead 4's last phrase is not an equivalence (`Δ_inj`: `2[a] − [b]` and `[a]`) | CONSISTENT | P | example checked |
| B.8 | Proved | zero class normal form under common successors | CONSISTENT | S | |
| B.9 | Proved | Lead 5 (i), (iii), (iv) | CONSISTENT | S | |
| B.10 | Proved | `[κ]` generates `Z/ε(L)`; no one-term normal form in a separator | CONSISTENT | S | |
| C.1 | Proved | `H_2(El_{K*}(h_V/(cv_1 ∼ cv_2))) ≠ 0` for every admissible choice | CONSISTENT | P, A | = C.28 |
| C.2 | Proved | Lead 7 with its hypothesis | CONSISTENT | S | |
| C.3 | Proved | equalizing precomposition breaks the hypothesis | CONSISTENT | S | |
| C.4 | Proved | `K*`: the triple column is injective over every abelian group | CONSISTENT | S, A | |
| C.5 | Proved | exact cycle-space test for one attachment | CONSISTENT | S | |
| C.6 | Refuted | "the component is a circle" needs monomorphisms | CONSISTENT | C | counts recomputed |
| C.7 | Refuted | free values and split injections do not give `T_1 = 0` (`K*`) | CONSISTENT | S | |
| C.8 | Proved | the same with free groups and free-factor maps over `K*` | CONSISTENT | S | |
| C.9 | Proved | free-factor diagram with free colimit, nerve colimit `H_2 = Z` | CONSISTENT | S | |
| C.10 | Proved | kernel of old → new `colim K` = fixed-endpoint path classes | CONSISTENT | P, A | exact sequence (CF) and both homology sequences followed |
| C.11 | Proved | fixed subsets of two copy maps: at most `2L − 1` | CONSISTENT | S, A | |
| C.12 | Proved | small overlap ⇒ connected equalizer subgraphs | CONSISTENT | S | |
| C.13 | Proved | protected cycles: `F → K` mono, quotient split-free | CONSISTENT | S, A | |
| C.14 | Proved | protected circles meet in ∅, a vertex or an edge | CONSISTENT | S | |
| C.15 | Proved | two-image saturation of protected cycles | CONSISTENT | S | |
| C.16 | Proved | local convexity `(2 − a_m) r ≥ 1` | CONSISTENT | S, A | |
| C.17 | Proved | small-diameter sources are safe | CONSISTENT | S | |
| C.18 | Proved | sources born in `K_1` are safe | CONSISTENT | S | |
| C.19 | Proved | forbidden pair ⇒ factorization | CONSISTENT | P, A | induction on the stage followed |
| C.20 | Proved | Helly for the birth cover (`s ≥ 15n > 3w`) | CONSISTENT | P, A | interval argument followed |
| C.21 | Proved | image intersections are arrow images | CONSISTENT | P | descent followed |
| C.22 | Proved | pointwise equalizer = image of one arrow | CONSISTENT | P | |
| C.23 | Proved | finite certificate for a source | CONSISTENT | P | |
| C.24 | Proved | component injectivity ⇒ zero kernel | CONSISTENT | P | |
| C.25 | Proved | component intersections of size ≥ 2 come from spans | CONSISTENT | P | |
| C.26 | Proved | `L_H ≤ L_U + 1`, no component cycles | CONSISTENT | P | induction on the source followed |
| C.27 | Proved | every arrow injective on `π_0 G_X` | CONSISTENT | P, A | the step "the proof of C.19 with components as the marked pair" is written in one paragraph; I re-ran it and it goes through; the expert should write it out |
| C.28 | Proved | every attachment preserves `colim K`; `κ_+ − κ_−` survives; `K*` not total | CONSISTENT | P, A | |
| C.29 | Proved | fixed sets of convex partial isometries are convex | CONSISTENT | S | |
| C.30 | Proved | warning: generic gluing can fail component injectivity | CONSISTENT | S | |
| C.31 | Refuted | generic connected convex warning (`n=3, s=45, k=11`) | CONSISTENT | S | finite; rests on the return's program (not rerun) |
| C.32 | Proved | repaired target is the strict necklace coequalizer | CONSISTENT | S, A | |
| C.33 | Proved | ordered necklace for large `k` | CONSISTENT | S | |
| C.34 | Proved | scope and effective choice | CONSISTENT | S | |
| C.35 | Refuted | large `k` cannot be dropped (`n=3, k=11`) | CONSISTENT | S | finite; the return's program not rerun |
| C.36 | Proved | convexity for `s > (2n−2)(D+1)` | CONSISTENT | S | |
| C.37 | Proved | selected targets: quasi-filtered, not total | CONSISTENT | S | superseded as a proof by C.28; kept as the explicit example |
| C.38 | Known | sphere classes have finite-poset representatives | CONSISTENT | S, L | |
| C.39 | Proved | Lead 6 (finite test) | CONSISTENT | S | |
| C.40 | Proved | Lead 8: `Ty^op` fails I and IV; `H_1 = Z`; needs a non-zero ring | CONSISTENT | P | the three lines rechecked; agrees with the expert's `ty_check.py` |
| C.41 | Proved | Lead 9 (a)–(d) | CONSISTENT | S | |
| D.1 | Proved | filtered ⊊ exact ⊊ total ⊊ quasi-filtered | CONSISTENT | P | `Δ_inj`; A.34; C.28/C.37 |
| D.2 | Refuted | II ms. 36ter false; sifted ⇏ total (`Δ^op`, the simplicial circle); "exact" does not repair it | CONSISTENT | P, M | mathematics checked; the wording of "Proposition 2.19" at II ms. 36 not compared with `DER_II-a.tex` |
| D.3 | Known | truncations preserved iff the commas of `A → ΠA` are filtered | CONSISTENT | S | TOTEX D.10 |
| D.4 | Proved | typing: `y\X` at II ms. 36; `U'/H'` at XII ms. 88 | CONSISTENT | S, M | already in TOTEX; not compared with the edition |

## Notes for the expert

1. Rows A.7 and A.12 are a remark and a definition carrying the label Proved; C.38 and D.3 are Known.
2. "Three independent audits" (C.28) and "independently audited" (A.34) are audits inside the return's own run.
3. The return states no source for A.31–A.32 in this form. The pattern (free amalgamation gives
   `⟨G_B, G_C⟩ = G_{B∩C}`, hence weak elimination of imaginaries) is standard in model theory; it opened Evans 2002,
   Conant, Marimon 2025 and did not use them. No literature check was made here.
4. Not in the register, in `notes\finite_pd_route.md` §3: over `C_δ` a functor to free groups with free-factor
   transitions whose abelianization is `Q` (so `T_1 = Z` over a total index). Only its first two paragraphs were
   read here. It bears on DER_FOLLOWUP Part D (see `BLOCK_FOR_DER_FOLLOWUP.md`).
5. Not read: `sections\algebra_leads.tex` (B.2–B.10), `akr_links.tex`, `akr_marked_cycles.tex`,
   `akr_protected_intersections.tex`, `akr_local_convexity.tex`, `akr_convexity.tex`, `akr_large_targets.tex`,
   `akr_ordered_necklace.tex`, `akr_beta_fixed_subsets.tex`, `akr_component_necklace.tex`, `finite_tests.tex`
   (except C.40's statement), `statements_sources.tex`, `predimension_binary_cycles.tex`,
   `predimension_functorial_cone.tex`, `freefactor_nerve.tex`, the bibliography, `code\`, `notes\` (one excepted).
