# Block for DER_FOLLOWUP: resolution of the items held for TOTAL_EXACT_2

Claude Fable 5.2 (effort high), intake of 13 Nov 2026. For the Dérivateurs expert to apply (the intake does not
edit DER_FOLLOWUP). Source: `INTAKE_TOTEX2.md`. Numbers are those of the final register of TOTAL_EXACT_2
(89 statements); the checkpoint 02 numbers quoted in the prompt changed: **C.24 (checkpoint 02) is now C.37;
C.27 (checkpoint 02) is now C.40.**

Status of what is used: C.40 and the chain C.10, C.19–C.28 were read with their proofs in the intake (C.27, C.28
with the Adámek–Koubek–Reiterman invariants (10), (11), (c_m) taken as stated); C.37 at statement level; the main
theorem A.1 with the proofs of A.21, A.24, A.30–A.34 read in full. No error found. Reviewed by nobody else.

## 1. Header (line 15, "Related prompts")

Replace "TOTAL_EXACT_2 (total ⇒ exact; the Adámek–Koubek–Reiterman category `K*`) is still running; its items
below marked **[TOTAL_EXACT_2]** are also asked there." by:

> TOTAL_EXACT_2 (total ⇒ exact; the Adámek–Koubek–Reiterman category `K*`) returned complete on 13 Nov 2026
> (GPT-6 Astra, ChatGPT Pro mode; 89 statements, none open; intake by Claude Fable 5.2, effort high: no error
> found; not reviewed further). It refutes total ⇒ exact (R17) and settles the two items that were marked
> [TOTAL_EXACT_2]: see R12, R14 and Parts A.2, B.

## 2. R12 (`Ty^op`): status

Replace "statement C.27 of checkpoint 02 of TOTAL_EXACT_2, read by nobody on our side" by "proved as statement
C.40 of TOTAL_EXACT_2 (`TOTAL_EXACT_2/sections/finite_tests.tex`, label `FT:ty`; the intake rechecked the three
lines)". Add after "is not total and not exact": "(no affine equalizer over any non-zero ring; over the zero ring
the statement is void)".

## 3. R14 (quasi-filtered, not total): status and statement

Replace R14 by:

> **R14 (TOTAL_EXACT_2 C.28, C.37, D.1; C.28 read with its proof in the intake).** For **every** admissible choice
> in the repaired Adámek–Koubek–Reiterman construction, every attachment preserves the colimit of the binary cycle
> functor, and `H_2(B El_{K*}(h_V/(cv_1 ∼ cv_2)); Z) ≠ 0` (C.28; the proof is a simultaneous induction showing that
> every arrow is injective on the components of the binary graphs, C.25–C.27, with the exact kernel formula
> C.10). C.37 is the earlier proof for selected large targets and specifies one category completely. So
> `{total} ⊊ {quasi-filtered}`, and with R17 `{filtered} ⊊ {exact} ⊊ {total} ⊊ {quasi-filtered}` (D.1).

## 4. New result R17 (the main theorem of TOTAL_EXACT_2)

Add:

> **R17 (TOTAL_EXACT_2 A.1, A.24, A.30–A.34, A.6, A.13, A.20; the proofs of A.21, A.24, A.30–A.34 read in full in
> the intake).** Let `C_δ` be the category of finite linearly ordered 3-uniform hypergraphs with
> `δ(U) = 2|U| − 3|E(U)| > 0` for every non-empty `U`, with increasing induced embeddings whose image `A` satisfies
> `δ(U) > δ(A)` for all `U ⊋ A`. Then `C_δ` is total (every component of every `El(H)` is weakly contractible) and
> not exact: the three point arrows `V → W` into the one-edge object have no affine equalizer over any non-zero
> ring, and `T_1(coker(P_W → P_V²)) = R`. The proof of totality: (i) for finite closed `B, C` in the Fraïssé limit
> `M`, `⟨G_B, G_C⟩ = G_{B∩C}` (a finite alternating amalgam), hence every open subgroup of `G = Aut(M)` is a
> pointwise stabilizer `G_F`; (ii) for every `H`, the maps `H → H^inj → T_S`, `T_S(B) = S^{G_B}`, are homotopy final
> on categories of elements (non-empty full cosieves of slices are contractible by a functorial free amalgam);
> (iii) `T_{G/G_F} ≅ A(F, −)`. Also: a category with common successors and the morphism Ramsey property is exact
> (A.6; ordered graphs, A.8); non-empty limits of all compact Hausdorff `A^op`-diagrams are equivalent to the
> finite-pattern Ramsey property (A.13) and fail for `C_δ` (A.17, A.19); over a quasi-filtered category
> `T_1(M) = 0` when `|M(a)| ≤ N` for one `N` (A.20).

## 5. Part A.2

Replace item 2 by (as the note in `ZIP_LIST.md` foresaw):

> 2. The implication of PRETOT C.4 fails for `n = 2`, by Lead 1 (c) and R14. Read the proofs of TOTAL_EXACT_2
>    C.10, C.19–C.28 (`sections/akr_attachment_fixed_paths.tex`, `akr_birth_cover_descent.tex`,
>    `akr_universal_components.tex`) in full, confirm each step with your own argument or give the exact error with
>    a repair; in the proof of C.27 write out the step that reruns C.19 with components as the marked pair. Then
>    write out the counterexample of Lead 1 (d): the category `E^◁`, its cosieve, and both verifications.

In Lead 1 (d) replace "With R14 it fails" / "(d) is conditional on R14: the drafter read …" by the status
"(d) rests on R14, now TOTAL_EXACT_2 C.28".

## 6. Part B.1

Delete item B.1 (settled: R12 is TOTAL_EXACT_2 C.40) and renumber, or keep the number with the text:

> 1. Settled: R12 is TOTAL_EXACT_2 C.40. Check its proof (`finite_tests.tex`, `FT:ty`) before using R12 in B.2–B.5
>    and report any error.

## 7. Part D.1 (a consequence the hold did not foresee)

`ZIP_LIST.md` says: "Part D.1 only meets it in the case of a total shape that is not exact, which exists only if
its Part A.1 is refuted." It is refuted: `C_δ` is such a shape. Two additions for the expert to weigh:

- In D.1, after "whether or not `A` is exact", name the test case: "the total category `C_δ` of R17, which is not
  exact, is the first case to settle".
- A lead from the return's notes, not a register row and read only in its first paragraphs by the intake
  (`notes/finite_pd_route.md` §3): over `C_δ` the functor `X ↦ ⟨u_x, v_x (x: V → X) | u_{ev_2} u_{ev_1}^{-1}
  v_{ev_3} v_{ev_1}^{-1} (e: W → X)⟩` takes values in finitely generated free groups (private-vertex Tietze
  elimination), its transitions are free-factor inclusions, and its abelianization is the module `Q` of R17 with
  `T_1 = Z`. Ask: prove or refute this, and decide whether it gives `M: C_δ → FreeMon` (or free groups) with
  `q_M ∉ W∞`. TOTAL_EXACT_2 C.8 is the same construction over the quasi-filtered `K*`, and C.9 a finite diagram of
  free-factor inclusions with free colimit whose nerve colimit has `H_2 = Z`: both bear on Lead 3.

## 8. Attachments

Replace `TOTAL_EXACT_2/checkpoint02/` in the zip by the final return's LaTeX: `TOTEX2_paper.tex`, `sections/`
(all 34 files, 330 KB), `TOTEX2_results.csv`, `TOTEX2_report.md`, `TOTEX2_references.bib`, and
`notes/finite_pd_route.md`; no PDF. Source folder:
`pro_prompts_max_20261112_work\TOTAL_EXACT_2\checkpoints\TOTEX2_checkpoint_03_20261113T1144Z_unzipped\TOTEX2\`.
Update the lines of the prompt that name checkpoint 02 (lines 30, 160, 176, 314, 402, 420 of the current file)
and run `--lint-math`.

## 9. What does not change

Part A.3 (`𝒬_n ≠ 𝒬_{n+1}`, `n ≥ 3`), Parts B.2–B.5, C, E. A suggestion for A.3, from the intake (unchecked): the
method of R17 applies to other predimensions `δ = a|V| − b|E|` on `k`-uniform hypergraphs; whether some of them
give categories whose categories of elements are `(n−1)`-connected and not `n`-connected is a natural first place
to look for the separation at `n ≥ 3` (see PUSH_ITEMS, Dérivateurs 2).
