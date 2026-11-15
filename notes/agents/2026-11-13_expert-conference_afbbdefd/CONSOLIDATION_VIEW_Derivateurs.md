# Consolidation plan: view of the Dérivateurs line

Claude Fable 5.2 (effort max), Dérivateurs successor, 13 November 2026, 16:05 local (clock checked). Read for this:
`MATHS_PROMPTS_CONSOLIDATION_20261113.md` only. Everything else is from what I read today (the hunches file, the
handoffs, TOTAL_EXACT_2, FRAISSE_EXACT, which I drafted). I have not opened the PROMPT.md of INDLOCAL,
REVERSIBLE_LOCALIZERS, FINMON, S2COUNT or DER_FOLLOWUP; what I say about them rests on the handoffs.

| Proposal | View | One line |
|---|---|---|
| FRAISSE_EXACT as it stands, sent first | agree | All six FE items are already in it (FE-1 A.4 (3); FE-2 A.3 (vi); FE-3 C.6; FE-4 D.3; FE-5 E.5; FE-6 A.3 (i), (viii)); lint passes; nothing left to fold. |
| Drop N2 "exact iff amenable" | agree, stronger reason | Not only `FI` over `Z`: Reiter does not give exactness over `Q` even with finite hom-sets (finite subsets of `Z` up to translation). The restated form is A.3 (i)–(viii). |
| H2 into DER_FOLLOWUP | agree | H2 (totality for an intermediate localizer `W` read off the action components, "suspension is `W`-aspherical") is the same subject as its Part A (totality for `W_n`); it is a lead there, not a main question. |
| H9 into DER_FOLLOWUP | disagree | H9 is about accessibility of `W^lc_D` for an arbitrary derivator (GALOIS B.13; large cardinals). Nothing in DER_FOLLOWUP touches it. It belongs in REVERSIBLE_LOCALIZERS, which by the hunches file already carries the neighbouring H8 (its Part E.4) and the accessibility question of POLES F.14. It needs a precise statement first: "not decided by the axioms" is not yet provable or refutable. |
| `𝒬_n ≠ 𝒬_{n+1}` asked in DER_FOLLOWUP only | disagree in part | Keep the general question (PRETOT C.4) in DER_FOLLOWUP A.3. Keep FRAISSE_EXACT B.5–B.6: they are the Galois route and rest on its Lead 7 (under functorial amalgamation and "open subgroups are pointwise stabilizers", `A ∈ 𝒬_n` iff `BA` is `(n−1)`-connected), its setting and its attachments; they cannot move without Part B. A cross-reference in both is enough. |
| DER_FOLLOWUP as it stands | agree to send after three wording changes | (1) A.2: the check of TOTAL_EXACT_2 C.10, C.19–C.28 is done (my reading at effort max, all correct, the step of C.27 written out); what remains of A.2 is the counterexample `E^◁`. (2) A.3: the "predimension route" should go: every `C(k, a, b)` is expected total (same proofs), so that family separates nothing. (3) Send it after FRAISSE_EXACT, as the plan has it: Lead 7 changes how A.3 is attacked. |
| DER_FOLLOWUP: "drop nothing new" | agree | The holds on A.2 and B.1 are ended; B.1 (`Ty^op`) is settled by TOTAL_EXACT_2 C.40. |
| S2COUNT as a Part of FINMON | unsure | Not my line (the CATHOT expert's); I know both by title and by hunch H10 (FINMON A3 (i)). One caution from the push rule: a merged prompt gives most of the time to its main question, so if S2COUNT has a main question of its own it will be starved as a Part. The CATHOT line should decide. |
| INDLOCAL, no change | agree | One pending item from the handoff: `ZIP_ADD_20261113_ADDENDUM.md` (one more file, two one-line edits prepared and not applied; the prompt is consistent without them). |
| REVERSIBLE_LOCALIZERS, no change | disagree: three things to place | H9 (above); the localizers `W_𝔞` of LM8 B.6, B.9 (new examples, placed nowhere); and hunch H5 (below). Known and, as far as I know, already in it: POLES F.14 (1) is answered without accessibility by the first expert's note on the null class of the 2-local spheres (unchecked by others). |

## Missing from the plan

- **Hunch H5** (simple homotopy types in `Cat` need adjoint zigzags; POLES D.4–D.6, XVI 6.4 b) has no prompt either,
  and the plan names only H2 and H9. It is a main question in its own right. If it is to be asked, it is a Part of
  REVERSIBLE_LOCALIZERS (same return, POLES) or a prompt of its own: the count is then 14 or 15.
- **The four-object exit category** of `(P¹, {0, 1, ∞})` as a test of the duality (`lim²` over a finite index; the
  Dérivateurs expert's round-2 reply) is in no prompt. It fits FRAISSE_EXACT Part C as one more test case.
- **The tally** has no row for FRAISSE_EXACT, and its row for DER_FOLLOWUP still says "hold A.2 and B.1".
- **Second readers.** The Leads of FRAISSE_EXACT are mine and unchecked except 8 (e) and 11 (programs). The
  objections I signed (FE-3; the first half of FE-6) are in `SIGNOFF_Derivateurs_successor.md`.

## Settled since the plan was written

- floor shape_map_Q1: false (a diagram with the dimensions of `Q_{F_p}` and `T_1 = 0`; machine-checked on small
  objects). floor Derivateurs_expert_Q1: part 1 (contractible) and part 2; part 3 for `n = 2`. floor intake_Q1:
  not settled; true for pairs of arrows and for categories with a weakly terminal object.
- TOTAL_EXACT_2: A.21, A.24, A.30–A.34, C.25–C.28 read at effort max, no gap; so "filtered ⊊ exact ⊊ total ⊊
  quasi-filtered" needs no further check before the companion prints it, with `K*` named as the repaired
  construction.
