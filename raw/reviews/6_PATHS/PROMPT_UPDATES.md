# Prompt updates after the PATHS answer

Claude (Fable 5.2), 11 November 2026, about 10:20–10:30 UTC. The answer is by GPT-6 Astra (ChatGPT Pro mode), to prompt `6_PATHS` as sent at about 09:12 UTC with STRATA folded in: 76 statements (40 Proved, 19 Refuted, 11 Known, 6 Open). Return: `pro_returns_20261110/6_PATHS/`. Nothing from its `code/` folder was run.

Decided from: `PATHS_report.md` and `PATHS_results.csv` (read in full), `sections/E.tex` (read in full, proofs included), `sections/D.tex` for D.8, D.9, D.17, D.18, D.19, D.23 (statements and proofs), `sections/00_conventions.tex`, the start of `sections/A_definitions.tex`. Followed step by step: D.8 (the cobase-change step CF3) and E.9. No cited source opened. The review (`REVIEW_author.md`, this folder) is not written yet: the prompts cite PATHS as unverified.

Scripts and section texts: `fold_in/` (`apply_fold_in.py`, `update_readmes.py`, `BISITE_section.md`, `LM4_section.md`, `LM5_section.md`; `before/` has every file as it was before this work).

## Does PATHS bear on `7_BISITE`? Yes

| Part of `7_BISITE` | What of PATHS |
|---|---|
| B (`Liss ∩ Prop ⊂ Fib_W`, ms. 225–226; general `W`) | E.9: the path functor over the group `C_2` is `W∞`-smooth and proper and its base change does not preserve rational homology equivalences. With one inference of mine (marked unverified in the prompt: a `W∞`-smooth and proper functor is `W`-smooth and proper for every fundamental localizer `W`, because `W∞ ⊂ W`), the inclusion fails for rational homology, for `W_0` (STRATA G.3) and for every homology localizer (the covering of POLES C.10), which would answer the question the section "After POLES" asked. The prompt asks to decide it. |
| B, E (bifibration against `Liss ∩ Prop`) | E.3 (`Ch(X) → X × X`: smooth, not proper, not a bifibration; the path-reversal argument at VII ms. 161–166 is wrong), E.4 (the eventual model: smooth and proper, not a bifibration), E.6 with E.11 open, E.5 (functorial factorization into a weak equivalence and a smooth proper functor with strict fibres the homotopy fibres), E.8 (the cotensor has wrong strict fibres). |
| E (the abstract theorem) | D.8, D.9 (enough intrinsic cofibrations, an initial object, pushouts and two-out-of-three give the finite precofibration axioms and rectification at finite direct shapes; not more), D.17 (what XIII, XVII, XIX give), D.18 (accessible localizers; the Brown argument for enough intrinsic fibrations), D.23 (homology localizers); D.10, D.13, D.15, D.16, D.20 (what needs an enhancement); E.7 (intervals). |
| A (XIII §§4–6) | D.17 as a reading of XIII ms. 7–12, 50–59 to check. |

Not put into `7_BISITE`: Parts A–C of PATHS (colimits in `Cat`, the hammock comparison, composition, pointed and linear versions), D.K1–D.K5, D.19 (the same example as GALOIS A.5, already in "After GALOIS"), E.10, E.12, E.13.

## Which version of each prompt is which

| Prompt | Current (with PATHS) | Previous |
|---|---|---|
| `7_BISITE` | `PROMPT.md` (53,976 bytes) + `7_BISITE_background.zip` (295 files, 46,315,195 bytes, SHA-256 `1a0a4777…328c8aad`) | the prompt of 09:08 UTC (43,381 bytes; with STRATA and its review): `pro_reviews_20261110/6_PATHS/fold_in/before/7_BISITE/PROMPT.md`, with `_work/7_BISITE_background_v6.zip` (278 files, 45,392,706 bytes, SHA-256 `97910110…8d807da3`). Before that: `_work/PROMPT_v5.md` with `_work/7_BISITE_background_v5.zip` (01:48 UTC, without STRATA). |
| `LM4_FINITE_GROUP_ACTIONS` | `PROMPT.md` (21,608 bytes), section "After PATHS" before the Parts. No zip. | `fold_in/before/LM4/PROMPT.md` (18,554 bytes) |
| `LM5_MULTI_GALOIS_TOPOI` | `PROMPT.md` (30,355 bytes), section "After PATHS" before the Parts. No zip. | `fold_in/before/LM5/PROMPT.md` (26,187 bytes) |

The top level of `7_BISITE` holds `PROMPT.md` and `7_BISITE_background.zip` only; `BACKGROUND.md`, `CHANGES_20261110.md`, `MANIFEST.tsv` (full hashes on its second line and per file) and the earlier zips are in `_work/`.

## Changed: `7_BISITE`

- Section "After PATHS" inserted before "Recent results" (six items; text in `fold_in/BISITE_section.md`).
- Two stale sentences corrected. The second paragraph said of II §§5–6, XII §7, XIII §§4–6 "None of those three is audited yet", and Part A ended "II-b, XII §7 and XIII are not audited, so there you audit as you go", although the same Part A says they are audited and their companion files have been in the zip since about 02:00 UTC. Both now say the audits are attached. If the prompt of 09:08 UTC had been sent, the model would have had both statements.
- Zip: 17 files added. Nine under `PATHS_return/`: `PATHS_report.md`, `PATHS_results.csv`, `PATHS_paper.pdf`, `PATHS_paper.tex`, `PATHS_references.bib`, `sections/00_conventions.tex`, `sections/A_definitions.tex`, `sections/D.tex`, `sections/E.tex`. Eight copied from the zip of `6_PATHS` (hashes checked against its manifest), because PATHS Part E rests on them: `CATHOT_return/sections/E_path.tex`, `CATHOT_review/REVIEW.md`, `grothendieck/DER_VII-c/DER_VII-c_text.tex`, and the five companion files of DER_VII-c. Nothing from `code/`, `audit/` or `research/`.
- `_work/MANIFEST.tsv`, `_work/BACKGROUND.md`, `_work/CHANGES_20261110.md` updated. `README.md` of the stack: rows 6 and 7 annotated, new last section.

## Changed: La Longue Marche (no zips exist for these two; they still wait for their second passes)

| Prompt | What was added | Why |
|---|---|---|
| `LM4_FINITE_GROUP_ACTIONS` | Section "After PATHS": PATHS D.1, D.4, D.11, D.13 (strict diagrams against homotopy-coherent ones; a strict action of `Z` on a finite model has finite order), and an inference of mine, marked unverified: his essential-surjectivity problem in three layers (outer action to coherent action on the homotopy type, with the obstruction in `H³(Γ; Z(π))` for a centre; coherent action to a strict action on some model; strict action on the surface, which is Kerckhoff for finite `Γ`). | Part C (the 2-equivalence; items 5 and 6). |
| `LM5_MULTI_GALOIS_TOPOI` | Section "After PATHS": D.K1–D.K5 as a second proof of GALOIS B.11–B.12 (the item "After GALOIS" said the Kan–Thurston step was unchecked; it has since been followed in the GALOIS review too) and C.P5; E.13 (two maps of classifying spaces that agree on all finite tests), with an inference of mine, marked unverified, for classifying topoi and profinite completions; the shapes of Kaledin's theorem (D.14–D.16) for the item "A second route"; A.2, A.5–A.7 (filtered colimits of categories). | §3 (pro-variants), Parts A, C, E. |

`BACKGROUND.md` and `CHANGES_20261110.md` of both folders have the entries; the stack's `README.md` has a new last section. In both prompts no reading or design is called settled, nothing is stated as the user's, and the inferences are labelled as the prompt author's. The layout of these two folders was left as it is (working files beside `PROMPT.md`): no zip is built yet; the `_work/` convention is to be applied when the zips are built.

Not changed: `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS` (no contact found: searched the prompts for paths, hammocks, rectification, localization). For `LM6` when it is revised: PATHS E.1, E.2, E.5 (the path fibration without base points, as a functor to `X × X`) is the Dérivateurs form of "points as sections".

## Not edited: `LM3_TEICHMULLER_TOWER` (being sent). What of PATHS bears on it

To use when its answer is reviewed, and in a later revision:

- Part F (a profinite completion of the exit-path category as a pro-object of finite categories): E.13 (maps into a 1-type that agree on every finite test and differ), D.K4–D.K5 and C.P5 (ind-objects of categories modulo natural transformations: what invariance gives, and a weak equivalence with no inverse of that kind).
- The "After STRATA" suggestions on relative categories: E.10 (a relative localization can keep non-invertible endomorphisms, an exit-path category cannot: the monoid `{1, e}`), D.13 (a relative poset can present a category and have the wrong strict diagram categories).
- Nothing in LM3 cites a PATHS statement, and nothing found in PATHS contradicts a statement of LM3.

## Prompts already sent (1–6): what of PATHS bears on them, for the integration

- `1_CATHOT`: E.26 and E.27 (open there) are proved (C.P3, C.P4); the invertibility of `q_L` modulo natural transformations is refuted (C.P5); E.20–E.25 rechecked (E.1); F.2 rechecked (E.13); E.17 and (KT_μ) reproved (D.K1–D.K5).
- `2_TOTAL_ASPHERICITY`: C.7–C.10 rechecked (A.6); G.1–G.6 rechecked (E.12); the example I found in the TOTASPH review (over the injective ordinals the colimit in `Cat` of free commutative monoids is wrong), until now checked by no one else, is confirmed with a shorter argument (A.5); the exact class of shapes is open (A.8).
- `3_POLES`: D.6 rechecked by enumeration (A.9); H.6 extended to `n = 1` (E.7); C.4–C.5 reproved for every non-zero spectrum (D.23); the direction "enough intrinsic fibrations ⇒ generated by maps `A → e`" of E.2 proved without accessibility (inside D.18); A.8–A.9, G.26 used and partly reproved (D.8).
- `4_GALOIS`: B.9–B.12 reproved (D.K1–D.K5); A.5 (D.19); the Kaledin statements F.5–F.6 made precise (D.14–D.16, D.21).
- `5_STRATA`: E.11 stays open: the two path functors are not bifibrations over the five-element monoid (E.6, E.11); B.8 does not give rectification (D.13); C.7 again (D.20); E.2 with explicit functors (E.5).
- `6_PATHS` itself: Lead 1 known in its weak-vertical form (B.2), the comparison `J` open (B.8) with B.4, B.6, B.7, B.9; Lead 2 true, its parenthetical reason replaced (B.4); the last clause of Lead 3 false (D.2, D.3).

## For Phase 2 (the review): first checks

1. E.3–E.5 and E.9 (cited in `7_BISITE`): E.3's direction of type maps against VII ms. 65–67 and the companion block at ms. 164; E.5's use of CATHOT E.21. Against STRATA D.6, E.1, E.10–E.11, as the handoff asks.
2. My inference in `7_BISITE` (monotonicity of smooth and proper in `W`): open Maltsiniotis 2005 and Cisinski 2006 §5.3; if it is wrong, the first item of "After PATHS" must be edited and the zip rebuilt.
3. D.8, D.9, D.17 against XIII, XVII, XIX; D.18's Brown argument; D.23.
4. Part D against STRATA C.7 and B.8 (D.13, D.20).
5. C.P1–C.P5, B.4, B.6; A.5 against my own example; D.K1–D.K5 against the GALOIS review.

## Folder convention changed after this file was written (user, 11 November 2026, about 10:35 UTC)

A prompt folder now holds only its upload files, `PROMPT.md` and the current zip, with no subfolder. What this file calls `_work/` of `7_BISITE` is now `pro_prompts_20261110_work/7_BISITE/` (BACKGROUND.md, CHANGES_20261110.md, MANIFEST.tsv, PROMPT_v5.md, the zips `_v1` to `_v6`). The Longue Marche prompts that are not ready (LM4 to LM8) are entirely in `longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/<name>/`, PROMPT.md included; their upload folders are empty until a zip is built. The files were moved by the coordinator; their contents are as described above.

## After the review (`REVIEW_author.md`, 11 November 2026, about 10:40 UTC)

1. **The inference in `7_BISITE`, Part B, is right.** Cisinski 2006, 5.3.1 defines `W`-proper and `W`-smooth by `W`-(co)asphericity of the fibre-to-comma functors, 5.3.4 (d) is the lifting-category criterion, 4.2.19 says `W∞` is the minimal fundamental localizer, and Maltsiniotis 2005, Théorème 1.2 is the same characterization; Exemple 5.3.2 gives prefibrations and precofibrations directly for every `W`. So a `W∞`-smooth and proper functor is `W`-smooth and proper for every `W`, and `Liss ∩ Prop ⊂ Fib_W` (XII ms. 225–226; row XIIc-a C033) fails for `W_0`, rational homology and every homology localizer; I add `W_n`, `n ≥ 1`, by the path functor over a category of the type of `S^{n+1}` (checked by no one else). It holds for `W∞`.
2. **No PATHS statement labelled Proved, Known or Refuted was found false**, so no prompt cites anything false. `7_BISITE` was **not rebuilt**: its upload set is still `PROMPT.md` (53,976 bytes) + `7_BISITE_background.zip` (295 files, SHA-256 `1a0a4777…328c8aad`), built at about 10:26 UTC. Whether the user sent that version or the one before it (43,381 bytes, zip of 278 files, now `pro_prompts_20261110_work/7_BISITE/7_BISITE_background_v6.zip`) is not known to me. The current prompt still says of PATHS "the review is not finished" and marks the Part B inference "unverified"; both are now out of date in the safe direction. If it has not been sent and a rebuild is wanted: replace those two phrases, add this review as `PATHS_review/REVIEW_author.md`, previous zip to `pro_prompts_20261110_work/7_BISITE/7_BISITE_background_v7.zip`.
3. `LM4_FINITE_GROUP_ACTIONS` and `LM5_MULTI_GALOIS_TOPOI` (work tree, not sent): the sentence on the state of the review now says that the statements were reviewed, none found false, with what was followed and what was not (D.15 rests on Kaledin's preprint theorem); BACKGROUND.md lists the review. Script: `fold_in/apply_after_review.py`.
4. Among the statements cited in the prompts: followed and found proved: A.2, A.5, C.P5, D.4, D.8, D.9, D.10, D.11, D.13, D.16, D.17 (1)–(2), D.18's converse, D.20's example, D.23, D.K1–D.K5, E.3–E.9, E.13; known and opened: D.14, D.18; not verified: D.15 (and the Reedy step behind B.2, on which E.2 leans).

## `7_BISITE` has been sent and answered (coordinator, 11 November 2026; noted at 13:34 UTC)

`7_BISITE` was sent and its answer is back; `LM3_TEICHMULLER_TOWER` has returned too. Which of the two versions of `7_BISITE` went out is not recorded here (see point 2 of the section above); the coordinator's record of the sending decides. `7_BISITE` is not to be rebuilt any more. For the review of the BISITE answer: the Part B inference of "After PATHS" is right (section "The inference in `7_BISITE`, Part B" of `REVIEW_author.md`), so the expected answer on `Liss ∩ Prop ⊂ Fib_W` is: true for `W∞`, false for `W_0`, `W_n`, rational homology and the homology localizers, when the three classes are taken for the same `W`; and no PATHS statement cited in the prompt was found false (D.15 is unverified: it rests on Kaledin's preprint theorem).
