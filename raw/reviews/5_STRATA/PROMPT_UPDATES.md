# Prompt updates after the STRATA answer

Claude (Fable 5.2), 11 November 2026, about 08:50–09:15 UTC. The answer is by GPT-6 Astra (ChatGPT Pro mode): 81 statements (54 Proved, 14 Known, 9 Refuted, 4 Open). Decided from `STRATA_report.md` and `STRATA_results.csv` (read in full) and all eight section files (read in full, proofs included). The sections "After STRATA" were first written citing the answer as unverified; the review (`REVIEW_author.md`, this folder) was finished the same hour, and its consequences are at the end of this file and already in the prompts.

Scripts and section texts: `fold_in\` (`apply_fold_in.py`, `apply_after_review.py`, `update_readmes.py`, the five `*_section.md`; `before\` has every prompt file as it was before this work).

## The stopped Opus agent

An Opus agent was started on this step at about 08:45 UTC and stopped after a few minutes. Before changing anything I listed every file under the two prompt stacks modified after 03:00 local time (02:00 UTC) on 11 November: there was none. It changed nothing in the Longue Marche prompt folders, in `7_BISITE` or anywhere else in the two stacks, so there was nothing to keep or undo.

## Which prompts are ready to send, in run order

| Order | Prompt | Folder | State |
|---|---|---|---|
| 1 | `6_PATHS` | `derivateurs_companion_20261109\pro_prompts_20261110\6_PATHS\` | Not sent before (confirmed by the user through the coordinator). `PROMPT.md` + `6_PATHS_background.zip` (222 files). Ready. |
| 2 | `7_BISITE` | `derivateurs_companion_20261109\pro_prompts_20261110\7_BISITE\` | `PROMPT.md` + `7_BISITE_background.zip` (278 files). Ready. If the version of 01:48 UTC was sent, that was `PROMPT_v5.md` + `7_BISITE_background_v5.zip`. |
| 3 | `LM3_TEICHMULLER_TOWER` | `longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM3_TEICHMULLER_TOWER\` | `PROMPT.md` + `LM3_TEICHMULLER_TOWER_background.zip` (263 files). Ready, all parts (Part F no longer waits). The folder's own note still applies: better after the 33 open fixes of P011–P040 are merged. |
| not ready | `LM4_FINITE_GROUP_ACTIONS`, `LM5_MULTI_GALOIS_TOPOI` | same stack | Sections added; no zip exists; they wait for the second pass of LM_P06–P10 and LM_P01–P02, as before. |

`LM1_GROUP_SCHEMES` and `LM2_LOOP_EQUATIONS` are untouched by this work (no contact with STRATA); their state is whatever it was.

## Which version is which

| Prompt | Current (with STRATA and the review) | Previous |
|---|---|---|
| `7_BISITE` | `PROMPT.md` (43,381 bytes) + `7_BISITE_background.zip` (278 files, 45,392,706 bytes, SHA-256 `9791011…807da3`) | `PROMPT_v5.md` (31,510 bytes; the prompt as made ready at 01:48 UTC) + `7_BISITE_background_v5.zip` (263 files, 43,725,358 bytes, SHA-256 `9a014c47…96fdb96`): with the companion files of II-b, XI-XIIa, XIIc-b, XIII-a, XIII-b, without STRATA |
| `6_PATHS` | `PROMPT.md` + `6_PATHS_background.zip` (222 files, 47,083,720 bytes, SHA-256 `359048c6…2b594e`) | `6_PATHS_background_v9.zip` (209 files, 46,460,465 bytes); the prompt text before STRATA is `fold_in\before\6_PATHS\PROMPT.md` |
| `LM3_TEICHMULLER_TOWER` | `PROMPT.md` + `LM3_TEICHMULLER_TOWER_background.zip` (263 files, 86,915,777 bytes, SHA-256 `8b4fdb4e…0abfff6`) | `LM3_TEICHMULLER_TOWER_background_v2.zip` (226 files, 84,934,340 bytes); the prompt text before STRATA is `fold_in\before\LM3\PROMPT.md` |

The current `PROMPT.md` of a folder always goes with the unnumbered zip of that folder. Full hashes are on the second line of each `MANIFEST.tsv`.

## Changed: Les Dérivateurs

| Prompt | Why | Zip |
|---|---|---|
| `7_BISITE` | Parts A, B: the lifting-category tests for proper and smooth functors with the converse by universal base change (D.3, D.4), D.7, D.9. Parts B, E: bifibration against `Liss ∩ Prop` against `Fib_W` (E.1, D.5, D.6, E.2–E.4; E.8–E.10, E.11 open); general `W`: G.3–G.5. Part B, the two fine theories: G.1. Part D (Lead 2): the poset dictionary with its hypotheses (A.1, A.2, A.4–A.6, A.12, B.3, B.7) and the difference between Kan extensions and topological direct images (D.5, D.8). Part E: A.9, C.6–C.8. Part F: D.1–D.2 and the moduli example (F.7, F.10–F.14). Part G: A.4–A.5, G.1, G.7, D.8. | rebuilt; previous kept as `7_BISITE_background_v5.zip`; 15 files added: 13 under `STRATA_return/` (report, register, paper PDF and TeX, bibliography, conventions, sections A–G), Jansen's paper, the review |
| `6_PATHS` | Lead 2 and the comparison `J`: exit paths of `|NS|` (A.4, A.12, B.3), the crossing category as homotopy link (C.2), unrestricted paths (C.4). Part D: relative posets present every small category (B.8, B.6, B.7); homotopy categories of diagrams do not glue (C.6, C.7; B.12 open). Parts C, E: the weight test for strict pushouts (C.9–C.11). "After TOTASPH", first item: G.2, A.10, E.3, E.4. Part E: the strict path bifibration over posets (E.5, E.6, E.10; E.7, E.11) against `Ch(X) → X × X`; D.3–D.6, E.1, G.3. | rebuilt; previous kept as `6_PATHS_background_v9.zip`; 13 files added: 12 under `STRATA_return/` (sections A, B, C, D, E, G) and the review |

Nothing from the answer's `code\` or `audit\` folders is in any zip. `MANIFEST.tsv`, `BACKGROUND.md` and `CHANGES_20261110.md` of each folder are updated. `README.md`: rows 5, 6, 7 annotated; new last section with the fate of the four leads of `5_STRATA`.

`5_STRATA` itself: untouched.

## Changed: La Longue Marche

| Prompt | Why | Zip |
|---|---|---|
| `LM3_TEICHMULLER_TOWER` | Part F named STRATA as its input. Section "After STRATA": the category (F.7, F.8; Jansen's theorem, which covers every genus); `n = 4, 5` (F.1–F.6, F.3); his groups in his notation (F.16) and the request to read the definition of the modular topos in the attached transcription of scans 321–330; the functors (F.9, F.12, F.13, F.15), properness (F.10), failure of smoothness (F.11), base change (F.14); F.17; what is left to this prompt; five suggestions for Part F, each marked as an unverified inference of mine (a completion by transporters in the profinite group; the profinite category `Gal(X)` of Barwick–Glasman–Haine as a geometric definition; the action as outer actions compatible with the inertia bimodules and the functors, on levels 4 and 5; the element `t_1t_2^{-1}`; relabelling as a pseudo-action); B.1, B.6, B.10, B.12, C.5–C.6, D.3–D.4. One sentence of Part F edited ("if its output is attached" → it is attached). | rebuilt; previous kept as `LM3_TEICHMULLER_TOWER_background_v2.zip`; 37 files added: 10 under `STRATA_return/` (sections B, C, D, F), the review, `papers/2308.09551/2308.09551v2.pdf` (Jansen, fetched from arXiv), `papers/1807.03281/` (*Exodromy*, 25 files copied from the `5_STRATA` zip); `MANIFEST.tsv`, `ASSEMBLY.md`, `BACKGROUND_ADD.md`, `CHANGES_20261110.md` updated |
| `LM5_MULTI_GALOIS_TOPOI` | Parts B, C: gluing a presheaf topos from an open part, a closed part and the link (C.1–C.4, C.6, C.8); the exit-path category of `P¹` with three points (F.1–F.2, F.8) and two candidate comparisons for `B_{X,U}` (an unverified inference of mine); the forgetful functor and its fibres (F.9–F.11, F.13). Part E: A.1–A.2, B.6, B.10, B.12. | none exists; `BACKGROUND.md` lists the files |
| `LM4_FINITE_GROUP_ACTIONS` | Parts A, C: a group with loops as an EI category (B.1, F.1–F.3, F.13), with an unverified inference of mine on the 2-category of Part C; Parts E, F: his groups of §19 as read in F.16, and F.9. | none exists; `BACKGROUND.md` lists the files |

Not changed: `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS` (searched for strata, exit paths, moduli of curves with boundary, links: no contact). In the Longue Marche prompts no reading or design is called settled and nothing is stated as the user's; the suggestions are labelled as inferences of the author of the prompt. `README.md` of that stack: the LM3 row of the table now says "can run now, all parts"; new last section.

## What the answer says about the leads of `5_STRATA`

- Lead 1: true with hypercompletion, or for posets with finite principal downsets; the unrestricted form is false (A.2). The finite geometric form is A.4.
- Lead 2: true as corrected: EI categories exactly (B.1, B.2); obstruction for non-invertible endomorphisms (B.6, B.7); geometric form proved for finite categories without non-identity endomorphisms and isomorphisms (B.3, B.4), open for general EI categories (B.5).
- Lead 3: true (C.2–C.4), with coefficients (C.6–C.8).
- Lead 4: recollement known (D.1, D.2); the identification of his proper and smooth functors with topological proper maps and submersions is false (D.5, D.6), and the Kan extensions are the topological direct images only in the cases of D.8.
- The patch construction proposed after CATHOT: `B K_λ(Y) ≃ Y` (E.5); it is not a bifibration without a fibrant replacement (E.7); with one, the bifibration question is settled over all posets (E.10) and left open in general (E.11).

## What of STRATA bears on prompts already sent

None of the prompts sent before STRATA is waiting: `1_CATHOT` to `4_GALOIS` are answered and reviewed, `5_STRATA` is this answer. For the record of the integration: STRATA C.3 is a second reading of POLES G.19 (the POLES review left G.19 unverified; it is now followed), G.2 a second proof of TOTASPH B.11, G.5 of POLES E.5, B.11 of the table GALOIS C.15, E.5 an addition to CATHOT D.1.

## After the review (`REVIEW_author.md`, 11 November 2026)

No STRATA statement cited in `6_PATHS`, `7_BISITE`, LM3, LM4, LM5 was found false. Changes the review made to the prompts (already applied, by `fold_in\apply_after_review.py`):

1. The sentence "has checked none … treat them like leads" in each "After STRATA" section is replaced by: the statements have been reviewed, none found false, the review is attached, with the list of what was not verified for that prompt.
2. `7_BISITE` and `6_PATHS`: a sentence that "row VIc-C008" in the STRATA files is row VIc-C022 of the companion's current register (the label came from the first return of chunk VI-c, through the pilot overview, into prompt `5_STRATA`). No prompt of the Longue Marche stack uses the label.
3. `LM3`: Kent–Leininger–Schleimer's Theorem 7.1 is now said to have been opened, and F.11 recomputed.
4. The review is in the three zips as `STRATA_review/REVIEW_author.md`, and listed in the `BACKGROUND.md` of LM4 and LM5. The zips were not sent between the two steps, so no further `_vN` was made.

Followed and found proved, among the statements cited in the prompts: A.1, A.2, A.7–A.10, A.12 (given A.4), B.1, B.2, B.6, B.7, B.9, B.10, C.1–C.4, C.6–C.11, D.3–D.7, D.9, E.1, E.2, E.4–E.10, F.1–F.8, F.11, F.12, F.15–F.17, G.1–G.5. Still unverified among those cited: the coarsening step of A.4 and B.3 (two sources not opened: Haine–Porta–Teyssier 2026; Kerodon 6.3.6.2), A.5, the coefficient extension of D.8, the general-`σ` step of F.10, the geometric halves of F.13–F.14, and the citations of Rivera–Wierstra–Zeinalian, Bakalov–Kirillov, Groth, Haine.

## For the order of running

`6_PATHS`, `7_BISITE`, `LM3_TEICHMULLER_TOWER` can run as they stand. `LM4` and `LM5` still wait for their second passes.
