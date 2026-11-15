# Handoff of the Dérivateurs field expert (successor), 13 November 2026

Claude Fable 5.2 (Anthropic), effort max. Written about 00:45 local on 13 November 2026 (last clock reading
00:32; no command could be run after that). The context guard stopped me at 706k tokens, above the coordinator's
bound of 640k: my own running estimate was far too low (I believed I was near 370k). A successor should ask the
harness for the figure instead of estimating.

Start here, then read `pro_reviews_20261110/KNOWLEDGE_HANDOFF.md` (its last section, "After TOTEX", is mine) and
`KNOWLEDGE_HANDOFF.md` of this folder (the expert in reserve).

## Done, task 1 (12 Nov, late): TOTEX shape and the prompt TOTAL_EXACT_2

- `derivateurs_companion_20261109/GLOBAL_SHAPE_AFTER_TOTEX_20261112.md`.
- `pro_prompts_max_20261112_work/TOTAL_EXACT_2/PROMPT.md`, `ZIP_LIST.md`, `checks_framer/ty_check.py` (+ `.out`).
  Packaged by the main session on 13 Nov 00:08 (`pro_prompts_max_20261112/TOTAL_EXACT_2/`). Lint: failing 0.

## Done, task 2 step 1 (13 Nov): PATHS intake folded into INDLOCAL

- Upload copy edited: `pro_prompts_max_20261112/INDLOCAL/PROMPT.md`. Backup:
  `pro_prompts_max_20261112_work/INDLOCAL/PROMPT_before_paths_intake_20261113.md`. Lint after the last change:
  `files: 1 failing lint: 0`.
- What changed: header and task paragraph; R1 and R4 cross-references; the PRETOT bullet (F.16 closed); new
  **R6** (PATHS statements verified by the intake: A.P1, C.P1–C.P5, A.2–A.4, D.K4, D.K5, D.1, D.5; open B.8,
  B.6 with a gap), **R7** (the intake's F2–F3 as a theorem with one written proof, to be checked), **R8** (`Ty^op`
  is not totally aspherical); "Not acceptable" names R6–R8; Part C rewritten with a status for each of C1–C4 and
  the items C4.1 (check C.P1–C.P4), C4.2 (one-sign blocks: E.27 fails there; the crown), C4.3 (check F2 step by
  step, write out F3), C4.4 (push R7: naturality in `b`, composition, the map `Q` of B.6, literature); "What is
  attached"; rule 5; the closing paragraph completed to the template's wording.
- `pro_prompts_max_20261112_work/INDLOCAL/ZIP_ADD_20261113.md` (files for `INDLOCAL_new_results.zip`) and
  `ZIP_ADD_20261113_ADDENDUM.md` (one more file and two one-line prompt edits that I prepared and could not
  apply; the prompt is consistent without them).
- `pro_reviews_max_20261112/6_PATHS/SECOND_READING_F2_20261113.md`: my second reading of F2. Every step followed;
  no error found. For the sign `+` the functor `trunc` is left adjoint to `pad`, so that step needs no hypothesis
  on `Q`. F3 was read in outline only: its two unwritten steps are unchecked. No literature search.

## Not done: task 2 step 2, the Dérivateurs follow-up prompt (DER_FOLLOWUP)

The coordinator's condition (context under 600k after step 1) was not met. Nothing was written under
`pro_prompts_max_20261112_work/DER_FOLLOWUP/`. Notes for whoever drafts it (template:
`claude_tools/prompt_lessons_20261112/PROMPT_TEMPLATE_PUSH.md`; lint `--lint-math`; model on
`TOTAL_EXACT_2/PROMPT.md`):

- Items asked for: PRETOT C.4, E.9, F.10; PRETOT A.5 for `End_Δ([n])`; `Ty^op`.
- I have NOT read the statements and proofs of PRETOT C.4, E.9, F.10, A.5 in the paper, only the review's lines:
  C.4 "n ≥ 2, A totally W_n-aspherical, V ⊂ A a non-empty full cosieve ⇒ H_n(BV) = 0? first case n = 2, countably
  many objects, no weakly terminal object" (review §3 and F15); E.9 "P(R,0) → R: the identity test is
  contractible, the remaining condition is the restricted-action acyclicity"; F.10 "Δ_inj with word
  substitutions"; F13 "the method of A.5 should extend to End_Δ([n]) and any finite acyclic K (not checked beyond
  n = 2)". Read `longue_marche_pro_pilot_20261104/answers/PRETOT_unzipped/PRETOT/PRETOT_paper.tex` at these
  numbers and `pro_reviews_max_20261112/PRETOT_REVIEW_OPUS/REVIEW.md` before framing.
- `Ty^op`: the question "is `Ty^op` totally aspherical" is answered no (R8 of INDLOCAL = Lead 8 of TOTAL_EXACT_2;
  mine, checked by nobody else). In the follow-up it becomes: check the three lines; then determine for which
  presheaves of categories on `Ty` the comparison `C_∞ → C` is a weak equivalence. Known: PATHS A.3 (exact
  condition uniform in the fibration), PATHS C.P1–C.P3 (the path diagrams, through the contractible posets of
  type maps). My suggestion, unchecked: the diagrams for which it holds are those on which the strict 2-category
  of types of C.P1 acts; state it as a Lead. Also: the wide subcategory of injective letter maps of `Ty^op` is
  `W_2` (exact, total: TOTEX E.2), and the preorder reflection of `Ty^op` is directed.
- Results to carry as R-items: TOTASPH C.5, C.11–C.13; PRETOT A.2, A.5, A.10, B.2–B.4, F.1–F.6; TOTEX D.4, D.7,
  D.9–D.10, D.21–D.26, E.2–E.6; PATHS A.2–A.4, C.P1–C.P3; the review's corrections (Isbell–Mitchell 1976).
- Do not duplicate TOTAL_EXACT_2 (total ⇒ exact; `K*`) or INDLOCAL Part C.

## Mathematics of mine that nobody else has checked (all are Leads or R-items in the two prompts)

1. `Ty^op` fails span completion: `e = (1,3)`, `c = (1,1)`: `(++) → (+−+)`; `g(1) < g(2) < g(3)` for every
   `g: (+−+) → σ`.
2. For every category: a family `a_0..a_k: p → q` has an affine equalizer iff `Tor_1(ΔZ, coker(P_q → P_p^k)) = 0`
   (given common successors); the permutation module is the cokernel of the transposed map.
3. If `κ = (ρ_1 − ρ_3, ρ_3 − ρ_2)` is annihilated by one affine arrow, the triple has an equalizer.
4. Totality is a finite test (comprehensive factorization of functors from finite posets).
5. Cones over diagrams whose strict colimit of representables is the homotopy colimit kill no class above the
   dimension of the diagram (so quasi-filters never kill `H_2`); the hypothesis fails where an arrow equalizes
   the pair.
6. The second reading of F2 (above).

## Records that are out of date (not corrected by me)

- `HUNCHES.md` of this folder: H1 (now framed by TOTAL_EXACT_2), H3 (refuted by PRETOT A.5), H7 (proved, PRETOT
  F.3 = TOTEX D.4).
- `pro_reviews_20261110/KNOWLEDGE_HANDOFF.md`, section on PATHS: "main question still open (B.8)" and "A.8 open"
  (intake F10); and the PRETOT review's "Open after the review" list (F.16 is closed).
- `GLOBAL_SHAPE_AFTER_PRETOT_20261112.md` §2 item 2 says "`Ty^op` first": closed by item 1 above.
