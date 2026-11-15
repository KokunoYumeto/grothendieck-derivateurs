
## STRATA (prompt 5) is back, folded in and reviewed (successor session, Claude Fable 5.2, 11 November 2026)

Return: `pro_returns_20261110/5_STRATA/STRATA/` (GPT-6 Astra, ChatGPT Pro mode; 81 statements: 54 Proved, 14 Known, 9 Refuted, 4 Open). Do not run its code.

Done:
- Step 1, `5_STRATA/PROMPT_UPDATES.md`: sections "After STRATA" in `6_PATHS` and `7_BISITE` (zips rebuilt; previous `6_PATHS_background_v9.zip`, `7_BISITE_background_v5.zip`; the 01:48 UTC version of the BISITE prompt is kept as `7_BISITE/PROMPT_v5.md`), in `LM3_TEICHMULLER_TOWER` (zip rebuilt, previous `_v2`; Part F no longer waits; Jansen's paper and *Exodromy* added), and short ones in `LM4_FINITE_GROUP_ACTIONS` and `LM5_MULTI_GALOIS_TOPOI` (no zips). Both READMEs have a new last section. The stopped Opus agent had changed no file. `6_PATHS` had not been sent (confirmed by the user). Ready to send: `6_PATHS`, `7_BISITE`, `LM3_TEICHMULLER_TOWER`.
- Step 2, `5_STRATA/REVIEW_author.md` with `checks_author/check_strata.py` and `.out`: all 81 statements. No statement labelled Proved, Known or Refuted was found false. Opened: Lurie HA A.5.5–A.6.10, A.9.3; *Exodromy* ch. 3; Aoki A.11–A.13; Douteau–Waas (the link theorem); Cisinski 2006 at nine numbers; Jansen 3.18, 3.19, 3.23, 6.6, 6.7; Kent–Leininger–Schleimer 7.1; Fiedorowicz. Downloads are in `5_STRATA/sources_opened/`.
- After the review the prompt sections say "reviewed, none found false" with what was not verified, and the review is in the three zips (`STRATA_review/`).

What changed in the picture:
- Lead 1 holds with hypercompletion (or finite principal downsets); Lead 2 holds for EI categories exactly, with an obstruction for non-invertible endomorphisms; Lead 3 holds (crossing arrows = homotopy link); the second half of Lead 4 is false (his proper and smooth functors are lifting-category conditions, not proper maps or submersions of realizations; Kan extensions are topological direct images only for closed inclusions and product projections).
- New against the companion: the bifibration question holds over every poset and every base with only monomorphisms or only epimorphisms (E.10, followed in full), and for 1-truncated values or bases; open in general (E.11: the five-element monoid of type `S²`). My remark: with idempotents in the base no strict diagram with fibration transitions can work (a surjective idempotent is the identity), so a pseudo-action is needed.
- **The row label:** the bifibration question is row VIc-C022 (ms. 186) in the current companion; "VIc-C008" (in the pilot overview 2.3 C, in prompt `5_STRATA`, and throughout the STRATA files) is the numbering of the first return.
- Part F: the exit-path category of `M̄_{0,n}` is the Charney–Lee category (Jansen 2023; every genus); forgetting a point is proper and not smooth. The profinite completion, the Galois action and `GT̂` are LM3 Part F; my five suggestions there are unverified inferences.
- STRATA C.3 follows POLES G.19 step by step (I did too): G.19 is no longer "unverified".

Unverified: the coarsening step of A.4, A.12, B.3 (Haine–Porta–Teyssier 2026 and Kerodon 6.3.6.2 not opened), A.5, the coefficient extension of D.8, the general-`σ` step of F.10, the geometric halves of F.13–F.14, D.2's cube, and the citations of Rivera–Wierstra–Zeinalian, Bakalov–Kirillov, Groth, Haine. Open in the answer: A.6, B.5, B.12, E.11.

NOT done: integration into the companion. The review ends with the list (22 items: VI-c rows C022, C023, C044, C045 and a new block at ms. 186; I-a blocks at ms. 1–9, 53–54 and a new block with the poset dictionary; VI-a/b; XIIb-a block at ms. 62; XIIapp block at ms. 18 and row G11; XIIc-a ms. 187; XVI; XI-XIIa). The integrations of POLES (16 items) and GALOIS (30 items) are also still to do. When `6_PATHS` returns: check its answer on `Ch(X) → X × X` against STRATA D.6, E.1, E.10–E.11, and its Part D against C.7 and B.8.
