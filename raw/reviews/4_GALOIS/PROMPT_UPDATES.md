# Prompt updates after the GALOIS answer

Claude (Fable 5.2), 11 November 2026. Decided from `GALOIS_report.md` (read in full) and `GALOIS_results.csv` (all 74 statements read in short form; A.1, B.3, B.7, D.2, E.1, E.10, F.4 in full). When the prompts were edited no proof had been checked; every prompt cites the GALOIS results as unverified. The review (`REVIEW_author.md`, this folder) comes after; its consequences for the prompts will be added at the end of this file.

The coordinator confirmed on 11 November that `5_STRATA` and `6_PATHS` had not been submitted; both were edited and their zips rebuilt.

No lead of prompts 5 to 7 or of the Longue Marche prompts is refuted or settled by GALOIS. One numbered target of `6_PATHS` (CATHOT E.17 with (KT_μ)) is claimed proved in GALOIS B.11–B.12.

## Changed: Les Dérivateurs

| Prompt | Why | Zip |
|---|---|---|
| `5_STRATA` | Part A: locally constant objects as a derivator with both adjoints (A.6) and `LC_D(A) ≃ Ho Fun(BA, 𝒞)` with detection on homotopy categories for a specified restriction (A.8, C.1). Part B: what locally constant coefficients recover of `BS` (F.1–F.3; F.8 open; values C.4, C.7, C.9, C.10, C.13). Part C: relative Theorem A for locally constant coefficients on a bare derivator and its opfibration mechanism (B.3), direct Mayer–Vietoris and filtered colimits (B.5), no reverse (B.6). Parts D, E: the audit of Chapter I's fibrations (D.3–D.6, D.8, D.9, D.12). Part G: `W_{r+1}` and every accessible `W_D^lc` do translate, as equivalences on locally constant sheaves (C.4, E.7, B.4); base change does not (B.7). | rebuilt; previous kept as `5_STRATA_background_v6.zip`; 14 files added under `GALOIS_return/` |
| `6_PATHS` | The target CATHOT E.17 and (KT_μ): claimed proved (B.9–B.12); the prompt now asks to check B.11's induction and B.12, to cite them, and to draw the consequence for Lead 3 without CATHOT D.8's hypothesis. Part D: `W_𝒞^lc` as accessible localizers on `Cat` with a coefficient meaning (B.3, B.4, E.7, C.15; B.13 open); `W_D^1` as a class with descent and without two-out-of-three (A.4, A.5, B.5); detection of a specified restriction (C.1, A.8, E.1). Recent results: what the answer read in Kaledin v3 (F.5, F.6) and Di Vittorio (E.6). Fibrations (D.6, B.7, D.3–D.5, D.8). Infinite products (A.7). | rebuilt; previous kept as `6_PATHS_background_v8.zip`; 16 files added under `GALOIS_return/` |
| `7_BISITE` | Part A: the base-change tests of Chapter I (D.1, D.2), refuted rows (D.3–D.5, D.9, D.12), D.8, three printed slips. Part B: `W_D^lc` as general localizers with a coefficient meaning and the classification of the fibration axioms among them (B.3, B.4, B.7, C.15); a question on cohomological fibrations against `W_D^lc`-proper maps. Caution on two-out-of-three (A.5). Part E: A.6, D.6. Parts E, F: D.7 and the opfibration argument of B.3. G.1, G.2. Verdict "wait" unchanged. | rebuilt; previous kept as `7_BISITE_background_v3.zip`; 13 files added under `GALOIS_return/` |

Each zip has, under `GALOIS_return/`: `GALOIS_report.md`, `GALOIS_results.csv`, `GALOIS_paper.pdf`, `GALOIS_paper.tex` (the macros), `GALOIS_references.bib`, `sections/conventions.tex` and the sections cited (5: A, B, B_general, B_loc67, C, D, E, F; 6: these and B_accessibility, B_KT; 7: A, B, B_general, B_loc67, C, D, G). Nothing from `code\`. `MANIFEST.tsv`, `BACKGROUND.md` and `CHANGES_20261110.md` of each folder are updated. `README.md`: rows 4 and 6 of the table annotated; new last section with the fate of the four leads of `4_GALOIS`.

`4_GALOIS` itself: PROMPT.md and zip untouched; one entry in its CHANGES file.

## Changed: La Longue Marche

| Prompt | Why | Zip |
|---|---|---|
| `LM5_MULTI_GALOIS_TOPOI` | Part E names GALOIS as its input. Section "After GALOIS": the statement for a locally connected topos (F.4; Hoyois 3.13, 3.20: representations of the pro-groupoid, not of the limit group; no claim that `LC` is a topos); level 1 among the levels (C.4, C.15, A.5, F.1, E.5, F.3, F.7; F.8 open); direct van Kampen at all levels, no converse (B.3, B.5, B.6); E.17 claimed proved (B.11–B.12); Kaledin's route (F.5–F.6). | none exists; `BACKGROUND.md` now lists the 13 files to attach |
| `LM3_TEICHMULLER_TOWER` | Part F: what a profinite completion remembers (F.1, F.4); the caution on ind- and pro-objects sharpened (B.12). Part E: the two rational theories (C.13, C.14). | rebuilt; previous kept as `LM3_TEICHMULLER_TOWER_background_v1.zip`; 10 files added under `GALOIS_return/`; `MANIFEST.tsv`, `ASSEMBLY.md`, `BACKGROUND_ADD.md` updated |
| `LM4_FINITE_GROUP_ACTIONS` | Part C: the three conditions on `π_{≤ r+1}` given by locally constant `r`-truncated coefficients (C.4–C.5), as a ladder for his fidelity conditions. | none exists; `BACKGROUND.md` lists the files |

Not changed: `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS` (no contact; whether they were submitted did not need deciding), `LM6`, `LM7`, `LM8`. For LM1 and LM8, GALOIS C.13–C.14 (the rational theory with discrete `π_1` against Toën's schematization) is noted in the Longue Marche README for their revision.

## Corrections the answer makes to what the prompts said

- The "After CATHOT" section of `4_GALOIS` said that `BA → e`, `A` an acyclic group, is not 1-complete. False: for a map to the point the constant and 1-complete conditions are the same condition (A.3). The separating map is `e → BA`. No other prompt repeats the error (searched 5, 6, 7 and LM1–LM8).
- Lead 1 of `4_GALOIS` for `W_D^1` and Lead 3 are refuted (A.5; D.3–D.5, D.12). Prompts 5–7 did not rely on either.
- `6_PATHS`, "Recent results": Kaledin's shapes are posets of finite chain dimension (`Pos`) and the left-bounded ones (`Pos⁺`), not "all posets, or the left-finite ones" as the introduction was summarized; the new section tells the model to correct this from the paper.

## What must be checked in the review before these citations are relied on

In this order: B.3 (the relative Theorem A on a bare derivator: everything in the three prompts leans on `W_D^lc` being a fundamental localizer); A.5; B.11 and B.12 (cited in `6_PATHS`, LM3, LM5); C.4, C.7, C.9, C.13 (values); B.7 against POLES E.2, E.5; D.3–D.5 (finite); D.7; F.4 against Hoyois; F.5 and E.6 against the papers; the nine POLES checks of `3_POLES\PROMPT_UPDATES.md`.

## For the order of running

`5_STRATA` and `6_PATHS` can run as they stand. `7_BISITE` still waits (II-b). `LM5` still waits for the second pass of LM_P01, P02.

## After the review (`REVIEW_author.md`, 11 November 2026)

No GALOIS statement cited in `5_STRATA`, `6_PATHS`, `7_BISITE`, LM3, LM4, LM5 was found false, and no prompt was changed again.

- Followed and found proved, among those cited: A.2–A.5, A.7, A.8 with C.1, B.3 (the whole proof; Cisinski 2009, 3.4–3.13 opened: Theorem 3.6 is for an arbitrary set of arrows), B.5, B.6, B.9–B.12 (the induction of B.11 with its injectivity step, and B.12), C.2, C.4, C.5, C.7, C.9, C.10 (own derivations), D.3–D.7, D.12 (own enumeration for D.3, D.4, D.12: `checks_author\check_galois.py`), E.5, E.7, E.10, F.1–F.3, G.1, G.2. Confirmed in the papers: E.6 (Di Vittorio: HDer 5 is Conjecture 3.2.23) and F.5 (Kaledin: `Pos` is posets of finite chain dimension; Chapters 6–7 "still preliminary" is in the arXiv comments field).
- Still unverified among those cited: B.4 (accessibility), the properness half of B.7, C.11, C.14, D.1, D.2, D.8, D.9, D.11, E.2–E.4, E.8, F.4 (Hoyois not opened), F.6, F.7.
- The nine checks of `3_POLES\PROMPT_UPDATES.md`: no contradiction with POLES in any of them (details in the review).
- `5_STRATA` and `6_PATHS` went out with the "After GALOIS" sections as written; nothing in them needs a correction after the review. The sentence in `6_PATHS` that B.11's injectivity step should be read first can now be read as: it has been followed once and found complete.
