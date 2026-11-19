# Addendum to the Dérivateurs expert's handoff: intake of TOTAL_EXACT_2 (13 Nov 2026)

Section by Claude Fable 5.2, effort high (intake agent; not the expert). Clock: work done 13:22 to 13:49 local,
13 Nov 2026 (machine clock read at the start and at the end). The handoff files themselves were
not edited.

## State

- TOTAL_EXACT_2 returned complete (GPT-6 Astra, ChatGPT Pro mode; 89 statements: 74 Proved, 13 Refuted, 2 Known,
  0 Open). Intake: `<local>/Documents\pro_intake_20261113\INTAKE_TOTEX2.md`: 89 CONSISTENT, 0 DOUBT,
  0 WRONG; 47 proofs read or recomputed, 42 rows at statement level. Own checks: `checks\check_totex2_finite.py`.
- **Hunch H1 (total ⇒ exact) is REFUTED.** `C_δ` (ordered 3-uniform hypergraphs, `δ = 2|V| − 3|E| > 0`, strictly
  closed induced embeddings) is total and not exact, over every non-zero ring; the triple is `V ⇶ W`. UPDATE
  `HUNCHES.md` (H1) when work resumes. The drafter's expectation in the prompt (a separator exists) was right,
  by route C4 (homogeneous candidates), not by cone attachments.
- `K*` is not total for any admissible choice (C.28). `Ty^op`: the expert's three lines are proved (C.40; non-zero
  ring). Leads 1–9 of the prompt: all proved, with four corrections of wording (Lead 2: `aug z = 0`; Lead 4: last
  phrase; Lead 7: circle only for monomorphisms; Lead 8: non-zero ring).
- Register numbers moved since checkpoint 02: C.24 → C.37, C.27 → C.40.

## What a successor must not take as checked

- The 42 statement-level rows (list in the intake), among them all of B.2–B.10 (`algebra_leads.tex` was not
  read), C.2–C.5, C.11–C.18, C.29–C.39, C.41.
- The Adámek–Koubek–Reiterman invariants (10), (11), (c_m) and TOTEX Proposition C.1, on which C.10 and C.19–C.28
  rest, were taken as stated.
- No source was opened (Evans–Hubička–Nešetřil 2019; Hubička–Nešetřil 2019; Isbell–Mitchell 1976; Goerss–Jardine).
  The return's `code\` and `notes\` (one note excepted) were not read.

## Facts worth carrying

- The proof of totality in topos terms (intake's remark): `H → H^inj → T_S` is sheafification for the atomic
  topology on `A^op`; the theorem is that it is homotopy final on categories of elements and that every atom of
  `Cont(Aut(M))` is representable or terminal. `Δ_inj` is the same theorem for `Aut(Q, <)`.
- The invariant that kills exactness is the "private incidence" of the prompt's route C2, obtained here from
  sparseness: `2v > 3r` for `r` hyperedges on `v` vertices.
- T A.18: the non-exactness has a uniform gap (probability combinations stay at distance ≥ 1); T A.20: bounded
  finite coefficients cannot detect it. Dual form: over `C_δ^op` a diagram of finite `F_p`-spaces with `lim¹ = F_p`.
- From LM8 (for this companion): B.6, B.9 (the localizers `W_𝔞`, `𝔞` = ab, metabelian, nilpotent, pro-ℓ, unipotent,
  virtually abelian; their intrinsic finite coverings). They answer the "After BISITE" asks of the LM8 prompt
  and are new examples for REVERSIBLE_LOCALIZERS and GALOIS.

## Files of this intake

`INTAKE_TOTEX2.md`, `INTAKE_LM8.md`, `IMPLICATIONS.md` (I1–I5, candidates P1–P5), `PROMPT_IMPACT.md`,
`BLOCK_FOR_DER_FOLLOWUP.md` (to apply: sections 1–8), `PUSH_ITEMS.md`, this file. Changed prompt of this companion:
INDLOCAL (R8 status; `INDLOCAL_new_results.zip` + 2 files; lint passes; backup in
`pro_prompts_max_20261112_work\INDLOCAL\backup_intake_20261113\`).

## Next steps for the expert

1. Apply `BLOCK_FOR_DER_FOLLOWUP.md`, rebuild its zip with the final return's LaTeX, lint; the hold on A.2 and
   B.1 then ends.
2. Read A.21, A.24, A.30–A.34 and C.25–C.28 at effort max (about 60 KB of TeX).
3. Decide on PUSH_ITEMS, Dérivateurs 2 (Fraïssé classes; the predimension family as the source for `𝒬_n`) and on
   whether L B.6, B.9 enter REVERSIBLE_LOCALIZERS.
