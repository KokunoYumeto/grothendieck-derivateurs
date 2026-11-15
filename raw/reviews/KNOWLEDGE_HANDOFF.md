# Knowledge handoff (Claude, Fable 5.2; written 11 November 2026 because the session's context is large)

For a successor who continues the Pro-mode prompt work on Les Dérivateurs and La Longue Marche.

## Files that carry the state
- `..\FABLE_PILOT_OVERVIEW_20261110.md` with its addendum: my reading of the 15 audited chunks of Les Dérivateurs and of the raw text of XII §8, XVI §§3, 5–7.
- `..\pro_prompts_20261110\` : seven prompts, numbered in running order (1_CATHOT submitted and returned; 2_TOTAL_ASPHERICITY, 3_POLES, 4_GALOIS, 5_STRATA, 6_PATHS, 7_BISITE), each with PROMPT.md, BACKGROUND.md, and since 11 Nov a CHANGES_20261110.md where edited. `_COMMON_BLOCK.md` is the shared second half (conventions, rules of proof, deliverables).
- `1_CATHOT\REVIEW_author.md` (this folder): verdicts on the returned answer; `checks_author\` my own homology check.
- Longue Marche: `user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\` (OVERVIEW.md, README.md, LM4_FINITE_GROUP_ACTIONS–P168). Read `PLAN_RECORD.md` there before touching anything: never label a reading or a design "settled", never restate the 30 statements of its section 5 as the user's, no rights remarks.

## What each Dérivateurs prompt is for
1. CATHOT: no right adjoint to `Cat hot → Hot`; what categories modulo natural transformations represent; finite tests; small models. Returned; see the review.
2. TOTASPH: is "totally W-aspherical" (every ordinary final image aspherical; XII ms. 88) the same as filtered. Tools: the collage test (adjoin one object with `Hom(x,a) = H(a)`; the new category is the homotopy cofibre of `B El(H) → BA`), the affine-equalization condition, the monoid `{1,e,f}`, `xy = y`. Decides rows II-C-003, XIIb-a-B035, XIIba-C005/C035/C045/C047/C048.
3. POLES: fibration axiom Loc (7) (only `W∞`, by his XVI 6.1 plus Cisinski) against the reversible cofibration axiom Loc (6 b) / W(7 bis) (equivalent to "g in W iff cofibre aspherical", his XII ms. 266–267; my inference: forces `W ⊃ W_Z`). XVI Théorème 5.4 asserts both for `W∞`: false if the inference holds. Unverified.
4. GALOIS: the localizer `W_D^lc` of equivalences on locally constant coefficients (I ms. 99–100), a Galois theory relative to the coefficient theory. Values expected: sets `W_1`, `D(Z)` `W∞`, `D(Q)` rational with `π_1`.
5. STRATA: small categories as stratified spaces; the XII-appendix gluing as homotopy links; bifibrations (row VIc-C008); the exit-path category of `M̄_{0,n}` (feeds LM3_TEICHMULLER_TOWER Part F).
6. PATHS: `Ch_Σ(M;a,b)` (vertical arrows arbitrary) against the hammock localization (vertical in `Σ`); composition; which relative categories are "rectifiable".
7. BISITE: the two fine localizations over a base for `(M, W, 𝓛)`, smooth/proper duality, six-operations shape. Waits for II-b, XI-XIIa, XIIc-b, XIII.

## Settled by CATHOT (as I judged it)
Proved: no right adjoint; representable types are exactly 1-types; local categories are those isomorphic in `Cat hot` to groupoids; reflection `Π_1`, not coreflective; bounded envelope `K_λ(Y)` (contractible simplicial sets over `Y` of size at most `λ`); space-valued finite tests fully faithful (finite CW types, not all finite-category nerves, are the compact generators); the diagonal argument G.2. Consistent with my homology check: the 5-element monoid for `S²`, the 7-element one for `S³`, 3 objects and 9 arrows for `RP²`. Unverified by me: Part E beyond E.1, F.10–F.12, the minima in the table, the citations "Ben-Bassat" and Carcacía-Campos Theorem 6.2. Open: D.6, E.6, E.17, E.26, E.27, G.17.

## Open in my own leads
The three starting arguments of prompts 2 and 3 are unchecked by anyone else. The Longue Marche overview rests on the table of contents, the coordinator's global pass and the board card, not on a line reading of the checked texts; NOTES_B and NOTES_C are unread; LM8_LIE_APPROXIMATIONS must be rewritten when cote 140-4 scans 172–280 are second-passed.

## Added after the second review of CATHOT (11 November 2026)

The independent review (`1_CATHOT\REVIEW.md`) confirms more than mine: D.3–D.5, E.1–E.5, E.7–E.13, E.15, E.18, E.20–E.25, F.7–F.13, and the minimal models by its own enumeration. New points folded into the prompts: (1) rectifiability and test (b) only make sense on shapes bounded relative to `M` (prompt 6, Lead 3 and Part D); (2) E.17 reduces to a cardinal-controlled Kan–Thurston statement (KT_μ), now a target in prompts 4 and 6; (3) an isomorphism of ind-objects modulo natural transformations says nothing about the unions (E.4), a caution added to prompts 2, 5, 6 and to LM3_TEICHMULLER_TOWER, LM5_MULTI_GALOIS_TOPOI; (4) G.5 rests on an unrefereed preprint (Ben-Bassat, arXiv:2610.38760) and G.4 refutes a conjecture of that preprint. Each changed folder has the details in `CHANGES_20261110.md`. Prompts 3 and 7 were not changed by the second review.

## TOTASPH (prompt 2) is back: state on 11 November 2026, for the successor

Return: `pro_returns_20261110\2_TOTAL_ASPHERICITY\TOTASPH\` (107 statements: 84 Proved, 11 Refuted, 10 Known, 2 Open). Do not run its code.

Done by me (step 1 of the coordinator's request): prompts 3_POLES, 4_GALOIS, 5_STRATA, 6_PATHS each got a section "After TOTASPH" before their Parts, a CHANGES entry and a rebuilt zip (previous kept as `_vN`); `2_TOTAL_ASPHERICITY\PROMPT_UPDATES.md` in this folder lists why. 7_BISITE unchanged. I read the report's sections 2, 3, 4, 6 and all statements in short form; I checked no proof. The prompts cite TOTASPH as unverified.

NOT done: step 2 (`2_TOTAL_ASPHERICITY\REVIEW_author.md`) and step 3 (integration into the companion of CATHOT and TOTASPH: rows V-I026, V-I054, V-I059, V-I063, V-I060, VIIc-C004/C005, IX-037, and the TOTASPH rows).

What the answer says about my leads (prompt 2):
- Lead 1 (collage test) proved and strengthened: the one-object collage is a literal mapping cone (B.1, B.2). Lead 2 (affine equalization, `H_1 = Z/g`) proved (B.4). Lead 3 (monoid `{1,e,f}`) proved, with the whole rectangular-band family (B.5, B.6).
- Lead 4 is FALSE in general: C.7–C.10 claim that the category of non-empty finite ordinals and increasing injections has exact colimits of abelian groups, hence is totally `W∞`-aspherical, and is not filtered. True with a weakly terminal object (C.13: monoids, finitely many objects). So audit row II-C-003 would be: false in general, true for preorders (companion), monoids and finite-object categories. The `W_Z` half: exact colimits (with non-empty, connected) imply total asphericity (C.6, D.5); the converse is open (D.7). C.5: total `W∞`- and total `W_Z`-asphericity coincide.
- Lead 5 and row XIIb-a-B035 FALSE: E.3, a three-element presheaf on the monoid `{1,e}`, total for every localizer, whose category of elements (3 objects, 6 arrows) has a final image of type `S²`.
- Rows: C035 false (F.18), C045/C047: functors compose for every localizer (F.8), total sieves compose for `W∞` and `W_R` (F.6), fail for `W_0`, `W_1` (F.10); strict `W∞` sieves open (F.27); C048 settled by a dichotomy (F.24, F.31: only isomorphisms unless `S²` is `W`-aspherical, i.e. `W ⊃ W_1`, F.28); C005 false (G.5).

What to check first in the review, in this order: (1) C.7–C.9, the exactness of colimits over injective ordinals (the affine cone construction with polynomials); my one hand check: for the two maps `[0] ⇉ [1]` the combination `(0<1) + (1<2) − (0<2)` of maps `[1] → [2]` has weight 1 and equalizes them, so the first affine condition holds. (2) C.3–C.4 (acyclic for all categories of elements implies contractible, by coverings) and C.6. (3) E.3 by direct enumeration (small). (4) F.23 (the pushout-product with the endpoints of `Φ_n` is not a `W∞`-cofibration): it bears on prompt 3. (5) B.6 and F.10 by enumeration. The citation "Adámek, Koubek, Reiterman (1981), A.4 and C.2" and "Cisinski 2006, Proposition 9.2.17" must be opened.

## TOTASPH reviewed; integration in progress (successor session, 11 November 2026)

Done:
- `2_TOTAL_ASPHERICITY\REVIEW_author.md`: all 107 statements. No statement labelled Proved or Refuted was found false; no gap found. Open: D.7 (total ⇒ exact colimits of abelian groups) and F.27 (is a totally `W_Z`-aspherical presheaf totally `W∞`-aspherical; equivalently do `W∞`-dwyérienne sieves compose). Own checks in `2_TOTAL_ASPHERICITY\checks\` (`fincat.py` and four `check_*.py` with `.out`): they reproduce every count of the answer. Opened: Cisinski 2006, 9.2.1, 9.2.15, 9.2.17; AKR 1981, A.4, A.5, C.1, C.2 (A.5 attributes the exactness example of the injective ordinals to Isbell–Mitchell); Cisinski 1999, Proposition 2; Cisinski 2004, 2.2.11; HORR generalized Theorem 1.5; Thomason 1980, Proposition 4.2.
- A finding of the review that is not in the answer: B.11 is about diagrams of simplicial sets. For diagrams of categories with the colimit in `Cat`, total asphericity is not sufficient: over `Δ_inj`, `D([n])` = free commutative monoid on `[n]`; `colim_Cat D = N` (type `S¹`), while `H_k(hocolim) = colim Λ^k Z^{n+1} = Z` for all `k`. Unchecked by anyone else.
- Prompt `6_PATHS` corrected for this (first item of "After TOTASPH"; CHANGES entry; zip rebuilt with the review and `sections\D.tex`; previous zip `6_PATHS_background_v4.zip`). Prompts 3, 4, 5, 7 unchanged: every TOTASPH statement they cite is proved. `2_TOTAL_ASPHERICITY\PROMPT_UPDATES.md` has the record.

Integration into the companion (`checks\DER_<id>\`; originals of every file touched are in `integration_20261111\before\`):
- Working files in `integration_20261111\`: `new_<chunk>.tex` (new commentary blocks, each preceded by a line `%%BLOCK after="<title of an existing block>"`), `apply_integration.py` (inserts the blocks, replaces outdated paragraphs, updates the claim rows, adds bibliography entries), `INTEGRATION_LOG.md` (what was changed, row by row).
- Conventions used: `proof_status` becomes `false` for a claim the source asserts and that is refuted; for the source's questions and conjectures it stays and the answer goes in `repair`; `notes` names the Pro answer (GPT-6 Astra, ChatGPT Pro mode), its statement numbers, and the checker (Claude, Fable 5.2, with the review file). New blocks are `development` blocks with proofs, marked `\ours`; they do not name the Pro packages.
- See `INTEGRATION_LOG.md` for where the work stopped.

State at the end of this session: review complete; prompt `6_PATHS` corrected; integration applied to the claim rows II-C-003, II-C-010, XIIb-a-B035, XIIba-C005, C035, C037, C038, C045, C047, C048, XIIbb-A001, V-I026, V-I054, V-I059, V-I060, V-I063, VIIc-C004, VIIc-C005, IX-037, with eight commentary blocks (one in II-a, five in XIIb-a, two in III-V). Left for a successor: rebuild the global reader and publish when the coordinator asks; revise the overviews of II-a, III-V, XIIb-a; have a second reader follow TOTASPH F.7 and the three reviewer's arguments listed in `INTEGRATION_LOG.md`; row XIIba-A-053 and row VIIb-C026 are untouched (prompts 3 and 6).

## Recent results (added 10 Nov 2026, late, by the coordinator)
Read `user\Documents\recent_results_20261110\BRIEF_FOR_PROMPTS.md` (two pages; sections per workstream)
before framing or reviewing any prompt; details and sources in `RECENT_RESULTS.md` beside it. For Les Dérivateurs and
Pursuing Stacks the relevant items are the claimed homotopy hypothesis (OpenAI family 312, restricted to coherators in
the Ara-Henry convention; only Henry's pushout conjecture in Lean) and Thomason model structures on strict
n-categories (family 317, main theorem in Lean). All OpenAI items are AI-produced, unrefereed manuscripts: cite them
with exactly that status. The user (10 Nov): make "the Fable agents ... that frame the prompts" aware of such results.

## POLES (prompt 3) is back and reviewed (successor session, 11 November 2026)

Return: `pro_returns_20261110\3_POLES\POLES\` (104 statements: 75 Proved, 14 Refuted, 13 Known, 2 Open). Do not run its code.

Done:
- `3_POLES\PROMPT_UPDATES.md`: prompts `5_STRATA`, `6_PATHS`, `7_BISITE` each got a section "After POLES", a CHANGES entry and a rebuilt zip (`POLES_return/`; previous zips kept as `_v5`, `_v7`, `_v2`). `4_GALOIS` had been submitted before POLES returned and was not touched: PROMPT_UPDATES.md has the list of checks to make on its answer (Part B's Loc axioms first). LM1, LM2: nothing bears. README: new last section.
- `3_POLES\REVIEW_author.md` with `checks_author\check_poles.py` and `.out`. Verdicts: XVI Théorème 5.4 false in its Loc (6 b) entry only; Loc (6 b) / W(7 bis) forces `W ⊃ W_Z` (proved; also proved independently in the companion's XVI block at ms. 27); `W_Z` is the least such localizer, but the reversible localizers are not all those above `W_Z` (`W_0` is not one), a non-total one lies strictly between `W_Z` and `W_0`, makes no sphere aspherical and never has enough intrinsic fibrations; `W̃∞` does not exist inside `W∞` under his reading of Loc (6), is `Fl(Cat)` without the bound, and is `W∞` with (6 a). New against the companion: no homology localizer `W_E`, `E ≠ 0`, satisfies Loc (7 F) (row XVI-C105); row XIIba-A-053 answered yes. Lead 6 (bijection with localizing subcategories of spectra) is false.
- No statement labelled Proved or Refuted was found false. Unverified: Part A, C.8–C.10, E.3, E.4, E.7, F.9–F.13, most of Part G (G.26 above all), H.7. Open in the answer: A.16, F.14.

NOT done: integration into the companion. The review ends with the list (16 items: XVI rows C105, C073, B099, C038–C040, A092, A112 and blocks at ms. 27, 87, 124; XIIb-a row A-053 and blocks at ms. 76, 78, 79; XIIb-b row A045, B036, C019; XIIc-a row A029; XIIc-b row C028). The companion's XVI and XII audits already contain the main verdicts, so the integration is small.

## GALOIS (prompt 4) is back: step 1 done, review not started (successor session, 11 November 2026)

Return: `pro_returns_20261110/4_GALOIS/GALOIS/` (74 statements: 52 Proved, 10 Known, 7 Refuted, 5 Open). Do not run its code.

Done (step 1): `4_GALOIS/PROMPT_UPDATES.md`. Prompts `5_STRATA`, `6_PATHS` (both confirmed not submitted by the coordinator), `7_BISITE` each got a section "After GALOIS", a CHANGES entry and a rebuilt zip (`GALOIS_return/`; previous zips `_v6`, `_v8`, `_v3`). Longue Marche: `LM5_MULTI_GALOIS_TOPOI` (section; BACKGROUND.md), `LM3_TEICHMULLER_TOWER` (section; zip rebuilt, previous `_v1`), `LM4_FINITE_GROUP_ACTIONS` (short section); LM1, LM2, LM6–LM8 untouched. Both READMEs have a new last section. Everything is cited as unverified: I read the report and the statements, no proof.

What the answer says about my leads: `W_D^lc` is a fundamental localizer for every Der 1–4 derivator (B.3); `W_D^1` is not (A.5: two-out-of-three fails for sets; it has the relative Theorem A); values as expected (Part C); Lead 3 refuted (D.3–D.5, D.12), repaired by Thomason fibrations (D.6); tower built for sets and rationally (E.5, E.8–E.10), general raising open (E.11, G.6). My "After CATHOT" sentence that `BA → e` is not 1-complete was wrong (A.3).

NOT done: step 2, `4_GALOIS/REVIEW_author.md` with `checks_author/`: verdicts on B.3, A.5, Part C, Part D, the tower and reconstruction; the nine POLES checks of `3_POLES/PROMPT_UPDATES.md`; the four slips against the edition's pages (I ms. 93, XVI ms. 78, "cofibrations" in Loc (7 F), "que je sache!" at I ms. 122); Di Vittorio and Kaledin against the papers in the 4_GALOIS zip; the list of companion blocks and rows to change. The order of checks is at the end of `4_GALOIS/PROMPT_UPDATES.md`.

## GALOIS reviewed (same session, 11 November 2026)

`4_GALOIS/REVIEW_author.md` with `checks_author/check_galois.py` and `.out`. `5_STRATA` and `6_PATHS` were sent by the user with their "After GALOIS" sections.

Verdicts: `W_D^lc` is a fundamental localizer for every Der 1–4 derivator on all small categories (B.3, followed in full; Cisinski 2009, Theorem 3.6 is for arbitrary sets of arrows, opened); `W_D^1` is not (two-out-of-three fails for sets) but has the relative Theorem A; the values of Part C hold (own derivations, including the arithmetic criterion: `W_{D(k)}^lc = W∞` iff no prime is invertible in `k`); Lead 3 is false (D.3–D.5, D.12; own enumeration) and the repair is by Thomason fibrations (D.6); D.7 proved (row I-b-B084-01 answered yes); the rational tower and the set tower hold (E.5, E.10); (KT_μ) and CATHOT E.17 for small filtered index are proved (B.9–B.12, followed in full). No statement labelled Proved or Refuted was found false. The nine POLES checks: no contradiction. The four slips (I ms. 93, XVI ms. 78, "cofibrations" at XVI ms. 39 F), "que je sache!" at I ms. 122) are all the edition's printed text; our transcription is faithful and already marks the first two with `[sic]`. Di Vittorio and Kaledin: the answer's qualifications are right.

Unverified: B.1, B.2, B.4 (accessibility; D.6, D.11, E.7, E.10 lean on it), B.8, the properness half of B.7, C.11, C.14, D.2, D.8–D.11, E.2, E.3, E.9, F.4–F.6, G.3–G.5. Open in the answer: B.13, B.14, E.11, F.8, G.6.

NOT done: integration into the companion. The review ends with the list (30 items: I-b rows and blocks at ms. 84, 99–100, 118, 122; I-a; VIII-X rows X021, X024, X038, X042 and a block at X:5; VI-a; XIIc-a; XI-XIIa; XVI rows C019 and blocks at ms. 27, 78, 124; XIIapp-G23; III-V rows V-I052, V-I053).

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

## Folder convention for the prompt folders (user, 11 Nov 2026, about 10:35 UTC; replaces the `_work/` subfolder convention of 10:15 UTC)

The user uploads every file of a prompt folder to ChatGPT, and no subfolder can be uploaded. So each prompt folder holds ONLY its upload files, `PROMPT.md` and `<name>_background.zip`, and never a subfolder. Everything else lives in a parallel work tree, by prompt name:
- Dérivateurs: `user/Documents/derivateurs_companion_20261109/pro_prompts_20261110_work/<name>/` (BACKGROUND.md, CHANGES_*.md, MANIFEST.tsv, earlier prompts, earlier zips `_vN`); the series-level downloads are `pro_prompts_20261110_work/_downloads/`.
- La Longue Marche: `user/Documents/longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/<name>/`. LM4 to LM8, not ready, are entirely there, PROMPT.md included: edit their PROMPT.md there. Their upload folders stay empty until a zip is built; then PROMPT.md and the zip are copied into the upload folder.
- A rebuild writes the new zip and PROMPT.md into the upload folder and the previous zip to the work folder as `<name>_background_vN.zip` (for `7_BISITE` the next is `_v7`).
The READMEs of the two stacks stay at the top of `pro_prompts_20261110/` and `pro_prompts_draft_20261111/`. Records written before 10:35 UTC say `_work/` for what is now the work tree.

## PATHS (prompt 6) is back, folded in and reviewed (Claude Fable 5.2, 11 November 2026, 10:40 UTC)

Return: `pro_returns_20261110/6_PATHS/` (GPT-6 Astra, ChatGPT Pro mode; 76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open). Do not run its code.

Done:
- Step 1, `6_PATHS/PROMPT_UPDATES.md`: `7_BISITE` got a section "After PATHS" (Part B: E.9 and the complementarity `Liss ∩ Prop ⊂ Fib_W`; Parts B, E: E.3–E.8; Part E: D.8, D.9, D.17, D.18, D.23, what needs an enhancement, E.7), two stale sentences on audited chunks corrected, zip rebuilt at 10:26 UTC (295 files, SHA-256 `1a0a4777…`; previous zip `pro_prompts_20261110_work/7_BISITE/7_BISITE_background_v6.zip`). `LM4_FINITE_GROUP_ACTIONS` and `LM5_MULTI_GALOIS_TOPOI` got short sections (no zips). `LM3_TEICHMULLER_TOWER` not edited (it was being sent). Both READMEs have a last section.
- Step 2, `6_PATHS/REVIEW_author.md` with `checks_author/check_paths.py` and `.out`: all 76 statements. No statement labelled Proved, Known or Refuted was found false. Opened: Cisinski 2006 (5.3.1–5.3.7, 4.2.19), Maltsiniotis 2005 (1.1, 1.2), Cisinski 2019 (7.4.12, 7.6.17), Kaledin v3 (2.1.5.3–4, 7.1.4.6, 7.2.1.3–4, 7.2.1.16), Dwyer–Kan (3.1, 5.5, 6.2), Meier, Rădulescu-Banu (CF1–CF6), and the manuscript at VII ms. 65–67, IX ms. 22–23, XIII ms. 7–10, XVII ms. 39, XIX ms. 33.
- After the review the sections of LM4 and LM5 say "reviewed, none found false". `7_BISITE` was not rebuilt after the review (nothing it cites changed; the user may have sent it; which version went out is not known to me). It still words PATHS as "review not finished".

What changed in the picture:
- **The prompt's main question is still open** (B.8): do the path categories with arbitrary vertical arrows (Grothendieck's) have the type of the Dwyer–Kan mapping spaces. Proved: the inclusion `J` of the weak-vertical categories is split injective in `Hot` and bijective on components (B.6), an equivalence for `Σ ⊂ Iso` and for `Σ` = all arrows (B.4). First undecided case: `0 < 1 < 2` with `0 → 2` marked.
- **CATHOT E.26, E.27 are proved** for every admissible `Σ` (C.P1–C.P4, by an action of the categories of maps of types, which are empty or contractible): row IX-037 is settled in `Hot`; the same comparison is not invertible modulo natural transformations (C.P5, four objects): rows VIIc-A046, V-I066.
- **My Lead 3 was wrong in its last clause**: the finite category of IX ms. 23 is rectifiable at every shape and lacks only a product (D.2, D.3). Lead 2 is true with another proof (B.4).
- **Intrinsic cofibrations**: a factorization through `Cof_W` with an initial object, pushouts and two-out-of-three is a finite cofibration structure (D.8; its key step is Grothendieck's XIII ms. 10, Corollaire 1); separating examples D.9–D.13; Kaledin's shapes are posets of finite chain dimension, not finite posets (D.14).
- **`Liss ∩ Prop ⊂ Fib_W` (XII ms. 225–226, row XIIc-a C033)**: true for `W∞`, false for `W_0`, `W_n`, rational homology and every homology localizer (PATHS E.9, STRATA G.3, POLES C.10, with Cisinski 2006, 5.3.1 and 4.2.19; the `W_n` case is mine and unchecked).
- The `Δ_inj` example of my TOTASPH review is confirmed (A.5); which shapes compute colimits in `Cat` is open (A.8).
- The handoff's cross-checks: PATHS E.3–E.6 against STRATA D.6, E.1, E.10–E.11, and PATHS D.13, D.20 against STRATA B.8, C.7: consistent; STRATA E.11 stays open.

Unverified: B.9 (the finite search), C.5, D.15 and D.21 (they rest on Kaledin's preprint theorem 7.3.1.3), the cited numbers in Arakawa–Cnossen, Kerodon, Lenz, Chachólski–Scherer, Groth, Keller, Quillen and the group-theory sources of D.K2, the coherent-nerve step of C.P2, the cocone of B.6, `(N_ξ F)_0 = Ex² NF` in D.12. Open in the answer: A.8, B.8, C.9, C.10, D.22, E.11.

NOT done: integration into the companion. The review ends with the list (14 items: VII rows VIIc-A046, C005, C042, VIIb-C026, V-I066 and blocks at ms. 65–74, 99–110, 121–124; IX rows 037, 040, 041, 044, 049, 052, 061, 065, 070, 072, 080, 081, 084, 087, 088; V ms. 44–46; XIII ms. 10; XIIc-a C033; XVI-C105 and the block at ms. 87; XII ms. 228–234; the TOTASPH block on colimits; VIc-C022). The integrations of POLES (16 items), GALOIS (30) and STRATA (22) are also still to do. All seven Dérivateurs prompts are now answered or ready; when `7_BISITE` returns, check its answer on `Liss ∩ Prop ⊂ Fib_W` against the section "The inference in `7_BISITE`" of the PATHS review.

Added at 13:34 UTC (coordinator's message): `7_BISITE` has been sent and its answer is back (BISITE.zip); `LM3_TEICHMULLER_TOWER` has returned too. Do not rebuild `7_BISITE`. The review of the BISITE return is a separate step; start it from the last section of `6_PATHS/PROMPT_UPDATES.md`.

## BISITE (prompt 7) is back and reviewed; the seven returns read together (Claude Fable 5.2, 11 November 2026, 14:01 UTC)

Return: `pro_returns_20261110/7_BISITE/` (GPT-6 Astra, ChatGPT Pro mode; 126 statements: 72 Proved, 32 Refuted, 18 Known, 4 Open). Do not run its code. Which version of the prompt was sent is still not recorded here; the return answers the "After PATHS" items, so it was the 53,976-byte version.

Files written, all in `pro_reviews_20261110/7_BISITE/`:
- `REVIEW_author.md` with `checks_author/check_bisite.py` and `.out`: all 126 statements. **No statement labelled Proved, Known or Refuted was found false.** Parts A and B followed in full; in Parts C–G eight proofs followed (D.2, E.3, E.6, E.11, E.12, F.2, F.19, G.2) and about twenty statements checked by hand; **44 statements unverified** (the list is in the review; D.11, F.10, F.15–F.17, B.15 are the ones that matter). No cited source was opened in this review.
- `COMBINED_REVIEW.md`: the seven returns together (658 statements; 29 Open).
- `FOLLOW_UPS.md`: six inserts for the unsent Longue Marche prompts (L1, L2 → LM5; L3, L6 → LM4; L4 → LM6; L5 → LM7 and LM8) and ten Parts of a new Dérivateurs prompt (working name `8_RESIDUE`, D1–D10), each as text to insert, to the push standard. The LM prompts were not edited: another agent folds the inserts in.
- `COMPANION_INTEGRATION.md`: 24 items.

What BISITE settles:
- **Part B as expected, and more.** `W∞`-smooth and proper ⇒ `W`-smooth and proper; `Liss_W ∩ Prop_W ⊂ Fib_W` holds **exactly for `W∞` and the class of all functors** (B.9, no accessibility; followed). The `W_n` case that the PATHS review added is confirmed (B.9, B.10, same example). New: a finite bifibration (central `C_2`-extension of the face poset of the tetrahedron boundary, 100 arrows) that is not in `Fib_{W_1}` nor in `Fib` of the rational local-system localizer (B.12, reproduced through `H¹(F_2)`); coverings are in both (B.13).
- **Row XIIc B062: no** (E.12, a six-element lattice; reproduced). True with a coaugmented replacement (E.11); with "enough intrinsic fibrations" alone: open (FOLLOW_UPS D3).
- **Row XIIc-a C023: yes**, `𝓛^ = Liss_W` for every fundamental localizer (B.6, followed).
- **POLES A.16: no** (A.32): Grothendieck's literal Loc (1), (2), (3) (Définition 1.1 of XVI) do not imply Loc (3 bis); the class `W†` (bijective on `π_0`, a weak equivalence when the source is connected) and a triangle of finite groupoids over `BC_2`. `W†` is not retract-closed. It is a weak fundamental localizer in the sense of Maltsiniotis and Cisinski; whether such an example is in the literature is not checked: check before saying anything public.
- The two fine localizations are `Fun(NS^op, Spaces)` (tests `s\X`, proper maps) and `Fun(NS, Spaces)` (tests `X/s`, his `W^g`, smooth maps) (B.1, B.3); literal slices fail over non-fibrant simplicial bases (B.4).
- XIII ms. 57–72 holds under its hypotheses (A.27, A.28); spaces over a finite Alexandrov base are cosheaves (D.2); pullback along a proper map does not preserve open-test equivalences (D.4); the dualizing weight is covariant and acts by a coend (G.2, G.3).
- Leads: Lead 1 true with qualifications, Lead 2 proved only for finite Alexandrov bases, Lead 3 true with hypotheses on the projection formula, Lead 4 false as a pointwise twist.

From the combination (arguments of mine, unchecked by anyone else; in `COMBINED_REVIEW.md` section 3):
- A smooth and proper `p` is in `Fib_{W_n}` iff `π_{n+1}(B) → π_n(F)` vanishes; it explains every example of the returns.
- **No bifibration with invertible transition functors represents the path local system over the five-element monoid** (STRATA E.11 = PATHS E.11 = BISITE B.21): such a bifibration is a central 2-cocycle twist, and a contractible total category would make the fibre a 1-type. What remains: idempotent left adjoints that are weak equivalences and not equivalences.
- B062 with enough intrinsic fibrations should hold by an approximation argument (not written out).

Corrections to earlier records: the handoff's sentence under STRATA that Kan extensions are topological direct images "only for closed inclusions and product projections" is too strong (BISITE D.11 claims all proper maps of finite posets; unverified). "The `W_n` case is mine and unchecked" (PATHS section): now checked. POLES A.16 "open": refuted for the literal axioms.

Conventions to keep straight (COMBINED_REVIEW section 2): Grothendieck-proper = Cisinski-proper = Lurie-smooth; `W`-smooth is a stabilizer, not a transporter; all returns use Loc (3 bis); three different "rational" localizers; `V^{(n)}` (Street nerve) against `W_n` (truncation).

NOT done: integration of BISITE (24 items) and of POLES, GALOIS, STRATA, PATHS; a second reading of D.11, F.10, F.15–F.17, B.15 and of my three combination arguments; opening the citations of BISITE (Cisinski 2019 with the errata of July 2026, Aoki, Volpe, Heyer–Mann, Mann, Rivera–Wierstra–Zeinalian, Ara–Maltsiniotis); the literature check for A.32; building the prompt `8_RESIDUE` from FOLLOW_UPS section II (it needs the common block, a background zip and the push-standard clauses 9 and 10).

## Prompt 8_RESIDUE drafted and packaged (Claude Fable 5.2, 11 November 2026, 14:07 UTC)

At the coordinator's request: `pro_prompts_20261110/8_RESIDUE/` holds `PROMPT.md` (35,727 bytes; Parts A to J = items D1 to D10 of `7_BISITE/FOLLOW_UPS.md`, with the three combination arguments as Leads 1 to 3 and BISITE D.11, F.15 to F.17 as Leads 4 and 5) and `8_RESIDUE_background.zip` (431 files plus `MANIFEST.tsv`, 44,408,713 bytes, SHA-256 `67716a21…a823a9b5`). Work files: `pro_prompts_20261110_work/8_RESIDUE/` (`PROMPT_head.md`, `build_8_RESIDUE.py`, `MANIFEST.tsv`, `ASSEMBLY.md`, `ASSEMBLY_NOTES_20261111.md`; a rebuild overwrites `ASSEMBLY.md`, the notes copy keeps what was left out and why). Edit `PROMPT_head.md` and rerun the script; never edit `PROMPT.md` directly. Not sent. The stack README has no row for it yet. L1 to L6 are with the agent revising the Longue Marche prompts.

## CATHOT G.6 against Ben-Bassat's Conjecture 7.1: checked (Claude Fable 5.2, 11 November 2026, 23:42 UTC)

`1_CATHOT/REVIEW_G6.md`. The item is G.6, deduced from G.4 (where this file says above "G.4 refutes a conjecture of that preprint", read "G.6, by G.4"). Verdict: the refutation is correct. No finite monoid has classifying space of the type of `RP²` or of any connected finite-dimensional CW complex with non-trivial `π_1`; the proof is written out in full there, given one classical theorem, with two independent choices (Miller 1984, Theorem A; or Atiyah 1961 on `K(BG)`, a route added by the reviewer). Conjecture 7.1 was read in the PDF (v1, 28 October 2026): it is about monoids and `RP²` satisfies its hypotheses. Nothing in the public raw copy needs to change. Not opened: Miller, Atiyah, McDuff (stated from memory); a later version of the preprint was not looked for. Nobody was contacted; contact with the author is the user's decision.

## La Longue Marche: separate handoff (pointer added 11 November 2026, 23:50 UTC)

The state of the Longue Marche prompts, the reviews of the LM3 and LM2 returns, what is established, the reviewer's own results and errors, and the open items are in `user/Documents/longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/KNOWLEDGE_HANDOFF_LM.md` (Claude, Fable 5.2).

Added 11 November 2026, 23:59 UTC: both theorems behind G.6 were read in their texts (Miller 1984: Theorem B, p. 40 = Theorem 10.1, pp. 84–85, is exactly the step; the return's citation is right; Atiyah 1961: (6.11) p. 45, (7.2) p. 46, §2 p. 28). arXiv has only v1 of 2610.38760. `1_CATHOT/REVIEW_G6.md` updated; `1_CATHOT/DRAFT_NOTE_TO_AUTHOR.md` is a draft for the user, not sent.

## Update, 12 November 2026 (main session, from the PATHS intake by Claude Fable 5.2 at effort high)

The section on PATHS above summarizes the void medium-effort review of 11 November. Out of date there: "The prompt's
main question is still open (B.8)" and "which shapes compute colimits in Cat is open (A.8)". A.8 is answered by
PRETOT F.6 (filtered components). B.8 has a proof by the intake itself (FINDINGS F2-F3 in
pro_reviews_max_20261112\6_PATHS\: B Ch_Sigma(M;a,b) = Map_{L(M,Sigma)}(a,b) for every wide Sigma), unverified by
anyone else. PRETOT F.16 is closed by PATHS C.P1-C.P3 (verified step by step).

## After TOTEX: shape and the prompt TOTAL_EXACT_2 (successor expert, Claude Fable 5.2, effort max, 12 November 2026, 23:41 local, clock checked)

Return TOTEX (GPT-6 Astra, ChatGPT Pro mode): `longue_marche_pro_pilot_20261104/answers/TOTEX_unzipped/`; review by Claude Opus 5.5 (effort max): `pro_reviews_max_20261112/TOTEX_REVIEW_OPUS/REVIEW.md` (58 statements, none wrong; total => exact not decided).

Written by me:
- `GLOBAL_SHAPE_AFTER_TOTEX_20261112.md` (2,928 characters): what TOTEX settles at II ms. 36-36ter and XII ms. 88-89, what remains, the order of pushes.
- `pro_prompts_max_20261112_work/TOTAL_EXACT_2/PROMPT.md` (push template of `claude_tools/prompt_lessons_20261112/`; lint `--lint-math`: failing 0), `ZIP_LIST.md` (26 rows; all sources exist), `checks_framer/ty_check.py` with output. Not packaged, not sent. Deliverable prefix `TOTEX2`.

In the prompt: R1-R11 (TOTEX results with status and the review's corrections), nine Leads, Parts A (main question; coefficients Q and F_p), B (triples), C (K* not total; tools), D (class diagram, manuscript statements, literature record).

Mine, checked by nobody else (all are Leads of the prompt):
- `Ty^op` is not total: the span `(+-+) <- (++) -> (+-+)` (embedding; both letters to the first +) has no completion, and that pair has no affine equalizer over any ring. `Ty(tau, rho)` = weakly increasing sign-preserving maps from the letters of rho to the letters of tau (enumerated for words of length <= 4). The candidate "Ty^op first" of GLOBAL_SHAPE_AFTER_PRETOT is closed.
- For every category, a family a_0..a_k: p -> q has an affine equalizer iff Tor_1 vanishes on coker(P_q -> P_p^k, t -> (t(a_i - a_0))); the permutation module of the family is the cokernel of the transposed map. For pairs the two coincide.
- If the class kappa of H1 is annihilated by one affine arrow, the triple has an equalizer; in a connected category with span completion a class is zero in a colimit iff u.kappa = sum (e_j - e'_j) k_j for parallel pairs e_j, e'_j.
- Totality is a finite test: for every functor u from a finite poset D, D -> El_A(pi_0(u/-)) is null-homotopic.
- Adjoining an object by a cocone over a diagram whose strict colimit of representables is its homotopy colimit kills no class above the dimension of the diagram. Quasi-filters have dimension 1: the reason to expect K* not total. The hypothesis fails when an arrow equalizes the pair (first case: the pair alpha_0, alpha_4k and v_1 in K_2).
- A separator's failing family of least size has g a_i pairwise distinct for every g.

Not done by me: the proofs of TOTEX Parts D-F were not read (statements only, through the review); the AKR scan was not opened; Oberst 1968, Gabriel-Ulmer 1971, Isbell 1968 and 1974 are still unopened by anyone; the hand computation for ordered graphs in approach C4 of the prompt (two induced increasing paths with 5 and 4 edges) is unchecked.
