# Pro-mode prompts from the Fable overview of Les Dérivateurs

Written by Claude (Fable 5.2), 10 November 2026, for GPT-6 Astra (ChatGPT Pro mode); packages assembled by Claude
(Opus 5.5). **The folders are numbered in the order to run them.** Each folder holds:

- `PROMPT.md`: the prompt, complete, to paste as it is;
- `<folder>_background.zip`: the attachment (Grothendieck's chunks, the companion files, the papers);
- `MANIFEST.tsv`: every file in the zip with its source and SHA-256; at the end, the papers that could not be fetched
  automatically (publishers that refuse scripts), with their links, to add by hand if wanted;
- `BACKGROUND.md`: the list the zip was built from.

## Order, and what can run now

| # | Folder | Verdict | Depends on |
|---|---|---|---|
| 1 | `1_CATHOT` | **Run now.** | Only audited chunks (III-V, VII-b, VII-c, VIII-X, XIIapp). |
| 2 | `2_TOTAL_ASPHERICITY` | **Run now.** | Audited chunks (II-a, XIIb-a, XIIb-b, XIIapp). II-b (§7 on cofiltering morphisms) is attached raw and is marginal. |
| 3 | `3_POLES` | **Run now, before the second pass of XII and XVI**, or with it. | Uses the raw transcription of XI-XIIa, XIIc-b and XVI, which are not audited. The mathematics (Parts B–F) does not depend on them; Parts A and G audit those pages themselves. Its outcome changes how XVI §§3, 5, 6 must be commented (Théorème 5.4 as stated is false if the lead holds), so it is better to have it before those chunks are finalized than after. The `_pages.pdf` of the three unaudited chunks are in the zip so that readings can be checked. |
| 4 | `4_GALOIS` | **Answered 11 Nov** (74 statements; Lead 3 refuted, Lead 1 refuted for `W_D^1`: see the last section). Was: **Run now**, all parts (11 Nov: XI-XIIa and XVI are audited now; their companion files are in the zip). | Audited chunks (I-a, I-b, VIII-X, XIIc-a, XIIapp, VI-a). Part D ends with a comparison with Chapter XI §1 (in XI-XIIa, unaudited) and Part B with the Loc axioms of XVI (unaudited): both are attached raw; re-check those two comparisons when XI-XIIa and XVI are back. |
| 5 | `5_STRATA` | **Answered 11 Nov** (81 statements; reviewed: see the last section). Was: **Run now**, all parts (11 Nov: XI-XIIa and XVI are audited now; both are in the zip for Part E). | Audited chunks (I-a, I-b, VI-a/b/c, VIII-X, XIIb-a, XIIb-b, XIIapp). Part E (bifibrations) should be compared with Chapter XI §1 and XVI §4 when they are back. Part F (the moduli test case) needs nothing from the manuscript. |
| 6 | `6_PATHS` | **Answered 11 Nov** (76 statements; folded into `7_BISITE`; review pending: see the last section). Was: **Run now**, all parts (11 Nov, after STRATA: section "After STRATA" added, zip rebuilt; not sent before that) (11 Nov: its numbered target CATHOT E.17 is claimed settled by GALOIS B.11–B.12, unverified; the prompt asks to check and cite) (11 Nov: XIII-a/b, XVII-a/b and XIX are audited now; their companion files are in the zip, so D.4 no longer waits). | Parts A–C, E use audited chunks (III-V, VII, VIII-X, XIIc-a). Part D.4 compares with Grothendieck's own conditions in XIII, XVII, XIX (unaudited, about 250 pages). Either run now with those attached raw and treat D.4 as provisional, or run after XIII, XVII-a/b, XIX are back. If only one run is wanted, wait. |
| 7 | `7_BISITE` | **Run now** (11 Nov, after PATHS: section "After PATHS" added, zip rebuilt, 295 files; the previous zip is `..\pro_prompts_20261110_work\7_BISITE\7_BISITE_background_v6.zip`) (11 Nov, after STRATA: section "After STRATA" added, zip rebuilt; the version made ready at 01:48 UTC is kept as `PROMPT_v5.md` with `7_BISITE_background_v5.zip`) (11 Nov: II-b, XI-XIIa, XIIc-b, XIII-a and XIII-b are audited; their companion files are in the zip; the rest of this row is the earlier reasoning). | Its subject is continued by Grothendieck himself in II-b (§§5–6), XII §7 (in XIIc-b), XI-XIIa (§III) and XIII (§§4–6), none audited. Running it now would make Pro mode audit about 200 unaudited pages inside a research prompt, and risks redoing what he did. Run when II-b, XI-XIIa, XIIc-b, XIII-a, XIII-b are back and checked; then replace "not yet audited" in Part A by the companion files. |

Prompts 1 and 2 are the cheapest to verify afterwards (short decisive arguments, finite counterexamples with code).
Before spending Pro runs on 1, 2 and 3, a second reader can check the three short arguments they start from in an hour
(the non-existence argument in 1, the collage test and the three-element monoid in 2, the homology-equivalence argument
in 3); if one of them fails, the prompt's lead section should say so first.

All leads in the prompts are inferences from one reading. Each prompt tells the model so and asks for proof or
refutation.

## The prompts

1. **CATHOT** (`1_CATHOT`): the Thomason–Kan envelope. Settles whether `Cat hot → Hot` has a right adjoint (lead: no),
   which homotopy types are representable on categories modulo natural transformations, the corrected statements at
   every place the manuscript uses the envelope, the exact positive form of the finite-test idea, and a first table of
   minimal category models of spheres.
2. **TOTASPH** (`2_TOTAL_ASPHERICITY`): is total asphericity the same as being filtered. Settles audit rows II-C-003,
   XIIb-a-B035, XIIba-C005, C035, C045, C047, C048, XIIbb-A001 and the characterization of Grothendieck's Dwyer-type
   immersions.
3. **POLES** (`3_POLES`): the fibration axiom Loc (7) against the reversible cofibration axiom Loc (6 b) / W(7 bis).
   Settles which fundamental localizers satisfy which; whether `W_Z` is the least localizer with the reversible axiom;
   the fate of XVI Théorème 5.4 and of the conjectured `W̃∞`; the correspondence with localizing subcategories of
   spectra; every statement of XII and XVI that used the reverse half.
4. **GALOIS** (`4_GALOIS`): the localizer `W_D^lc` of maps inducing equivalences on locally constant coefficients.
   Settles whether it is a fundamental localizer, its value for sets, `n`-types, `D(Z)`, `D(Q)`, `D(F_p)`, spectra; the
   repaired fibration theory of Chapter I; the tower obtained by iterating; the reconstruction statement.
5. **STRATA** (`5_STRATA`): the dictionary between coefficients on a small category and constructible sheaves on a
   stratified space, the gluing conjecture of the appendix to XII as homotopy-link gluing, recollement and base change,
   strict bifibrations (row VIc-C008), and the exit-path category of `M̄_{0,n}` as a test case from the Esquisse.
6. **PATHS** (`6_PATHS`): Grothendieck's path categories against the Dwyer–Kan mapping spaces for a general `Σ`, with
   composition, pointed and linear versions (eleven conditional audit rows), and an intrinsic criterion for a relative
   category to carry a homotopy theory of diagrams.
7. **BISITE** (`7_BISITE`): the two fine localizations over a base for a general `(M, W, 𝓛)`, the smooth/proper duality
   in simplicial sets, presheaf categories and topological spaces, an abstract theorem with his axioms, the
   six-operations shape of a derivator, and duality on finite bases for stable derivators.

Not turned into prompts: overview 3.3 (a mechanical check of the "stated" rows; a script task, not a Pro task) and the
stable direction of I ms. 29 and Chapter XIV (wait for XIV to be audited; the literature has it).

## What changed in the findings

The seven chunks VII-b, VII-c, VIII-X, XIIapp, XIIb-a, XIIb-b, XIIc-a were already in `checks/` at the first read and are
covered by the overview; they change nothing. What does change it is the raw text of the unaudited chunks that the
prompts needed (XII §8 in XIIc-b; XVI §§3, 5, 6, 7; XI-XIIa §I; II-b §6). The corrections are in the addendum at the end
of `..\FABLE_PILOT_OVERVIEW_20261110.md`; in short:

1. The reformulation "under W(7 bis), `g ∈ W` iff the mapping cone of `g` is `W`-aspherical" is Grothendieck's own
   (XII ms. 266–267), and he calls the reverse half "inhabituelle" (ms. 270). The rigidity of the fibration axiom is
   also his (XII Théorème 1, XVI Théorème 6.1 and Corollaire 6.3), completed by Cisinski's minimality theorem. What
   remains an unverified inference is the consequence: the reverse half forces `W ⊃ W_Z`.
2. The false statement survives to the end: XVI Théorème 5.4 (ms. 79) asserts that `W∞` satisfies all the axioms
   including Loc (6), which he reads as Loc (6 a, b). But he also observes (XVI ms. 119–120) that Loc (6 b) plays no part
   in showing `HOT_W` is a derivator, so the damage is confined to the statements listed in prompt 3 (POLES), Part G.
3. New consequence: his conjectured localizer `W̃∞ ⊊ W∞` of "simple homotopy types" (XVI ms. 87–92) would be all of
   `Fl(Cat)` under his own reading of Loc (6).
4. XVI §3 does build a theory of homotopy cofibres (Loc (6 A), via K. S. Brown's lemma), so "a cofibre theory" leaves
   the list of directions not taken.
5. II-b §6 is a Galois connection between classes of weak equivalences and classes of base-change maps. It bears on
   prompt 7 (BISITE), not on the localizer `W_D^lc`; the remark in overview 3.2 that it "may already contain part of
   this" is withdrawn.

`_COMMON_BLOCK.md` is the shared second half of every prompt (conventions, rules of proof, deliverables); it is already
appended to each `PROMPT.md` and is kept only so that a change can be made in one place. `_downloads\` holds the papers
the zips were built from.

## 11 November 2026: kept in step with the Longue Marche prompts

A second stack of draft prompts exists for La Longue Marche: `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\` (LM4_FINITE_GROUP_ACTIONS to LM5_MULTI_GALOIS_TOPOI; its README has the table of overlaps). Two prompts here were edited so that the two stacks divide the work, and only these:

- `5_STRATA\PROMPT.md`, Part F: new item (iv). It uses Grothendieck's definitions of the Teichmüller tower from La Longue Marche §19 and §§26–27, and leaves the profinite completion, the Galois action and the comparison with the Grothendieck–Teichmüller group to LM3_TEICHMULLER_TOWER (Part F), which starts from this prompt's output. `5_STRATA\BACKGROUND.md` lists the added files (LM_P021–P024, LM_P034–P036, the author's table of contents).
- `4_GALOIS\PROMPT.md`, Part F: one sentence. The reconstruction theorem is to be stated so that it specializes to a locally connected topos; the theory of multi-Galois topoi (La Longue Marche §§1–4) is left to LM5_MULTI_GALOIS_TOPOI. `4_GALOIS\BACKGROUND.md` lists the added files (LM_P01–P02; pilot packages, not yet second-passed).

The zips `5_STRATA_background.zip` and `4_GALOIS_background.zip` were built before these edits: add the listed Longue Marche files and update `MANIFEST.tsv` before those two prompts are run. `1_CATHOT` (already submitted) and the other four prompts are unchanged.

## 11 November 2026: after the CATHOT answer

`1_CATHOT` has been answered; the author's review is `..\pro_reviews_20261110\1_CATHOT\REVIEW_author.md`. Prompts 2 to 6 each got a section "After CATHOT" before their Parts, and a `CHANGES_20261110.md` in their folder saying what changed and which parts of the CATHOT answer must be added to the zip. `7_BISITE` is unchanged. The order and the verdicts of the table above are unchanged: no lead of prompts 2 to 7 was refuted or settled by CATHOT; `6_PATHS` became smaller (the all-arrows case is cited, and CATHOT's open statements E.26 and E.27 are its numbered targets). (Updated 10 Nov, late: 4_GALOIS, 6_PATHS and 7_BISITE now carry a dated section "Recent results (state: 10 Nov 2026)"; 3_POLES and 5_STRATA unchanged; see each folder's CHANGES_20261110.md.)

## 11 November 2026: after the POLES answer

`3_POLES` has been answered (104 statements); the record of what was folded in is `..\pro_reviews_20261110\3_POLES\PROMPT_UPDATES.md`, the review `..\pro_reviews_20261110\3_POLES\REVIEW_author.md`. `5_STRATA`, `6_PATHS` and `7_BISITE` each got a section "After POLES" and a rebuilt zip (`POLES_return/`); `4_GALOIS` had already been submitted and is unchanged: the checks to make on its answer are listed in PROMPT_UPDATES.md. The table above is unchanged: no lead of prompts 4 to 7 is refuted or settled by POLES.

The leads of `3_POLES` itself, as its answer has them: the cofibre criterion (Lead 1), "`W ⊃ W_Z`" (Lead 2) and "`W_Z` is the least localizer with the reversible axiom" (Lead 3) proved, with two corrections (the localizers with the reversible axiom are not all the localizers above `W_Z`: `W_0` is not one; with Loc (5) no localizer has both the fibration and the reversible axiom); XVI Théorème 5.4 false in its Loc (6 b) part only; the stability intersection `W̃∞` equal to the class of all functors under his reading of Loc (6) (Lead 4); Lead 5 true for Loc (7) and false for Loc (7 F); Lead 6 (a bijection with localizing subcategories of spectra) refuted, a Galois connection remaining. Items 1 to 3 of "What changed in the findings" above are thereby confirmed, subject to the review.

## 11 November 2026: after the GALOIS answer

`4_GALOIS` has been answered (74 statements: 52 Proved, 10 Known, 7 Refuted, 5 Open); the record of what was folded in is `..\pro_reviews_20261110\4_GALOIS\PROMPT_UPDATES.md`; the review will be `..\pro_reviews_20261110\4_GALOIS\REVIEW_author.md`. `5_STRATA`, `6_PATHS` and `7_BISITE` each got a section "After GALOIS" and a rebuilt zip (`GALOIS_return/`; previous zips kept as `_v6`, `_v8`, `_v3`). No lead of prompts 5 to 7 is refuted or settled by GALOIS; one numbered target of `6_PATHS` (CATHOT E.17, with the cardinal-controlled Kan–Thurston statement) is claimed proved there (B.11–B.12) and is now to be checked and cited. The verdicts of the table are otherwise unchanged.

The leads of `4_GALOIS` itself, as its answer has them (unverified until the review):

- Lead 1: the chain of inclusions proved (A.2); `W_D^lc` is a fundamental localizer for every derivator with Der 1–4, with no enhancement (B.3), and is accessible for presentable coefficients (B.4; open for a bare derivator, B.13). **Refuted for `W_D^1`:** the 1-complete class fails two-out-of-three already for sets (A.5), although it satisfies the relative Theorem A.
- Lead 2 (values): proved (C.4–C.15): sets `W_0`, `W_1`; `r`-types `W_r`, `W_{r+1}`; spaces, `D(Z)` and spectra `W∞`; `D(Q)` the `π_1`-rational equivalences (known: Rivera–Wierstra–Zeinalian 2021). A correction to the "After CATHOT" section of the prompt: for a map to the point the constant and the 1-complete conditions coincide (A.3), so `BA → e` with `A` acyclic is 1-complete; the separating map is `e → BA`.
- Lead 3: **refuted** (D.3–D.5, D.12): replacing equivalences by 2-complete or 1-complete ones throughout does not repair I ms. 79–84; composition and fibre detection still fail for the weak notions. The repair is by the Thomason fibrations of the accessible localizer `W_D^lc` (D.6), and for spaces all notions coincide (D.8).
- Lead 4 (tower): realized for sets (E.5) and for `D(Q)` as an explicit tower of ordinary derivators with intersection `W∞` (E.8–E.10); a functorial raising operation on arbitrary derivators and the identification with higher linear categories are open (E.11, G.6).

## 11 November 2026: after the STRATA answer

`5_STRATA` has been answered (GPT-6 Astra, ChatGPT Pro mode; 81 statements: 54 Proved, 14 Known, 9 Refuted, 4 Open). Record of what was folded in: `..\pro_reviews_20261110\5_STRATA\PROMPT_UPDATES.md`; review: `..\pro_reviews_20261110\5_STRATA\REVIEW_author.md` (Claude, Fable 5.2): no statement labelled Proved, Known or Refuted was found false.

`6_PATHS` and `7_BISITE` each got a section "After STRATA", a CHANGES entry and a rebuilt zip (`STRATA_return/`, `STRATA_review/`; previous zips kept as `6_PATHS_background_v9.zip` and `7_BISITE_background_v5.zip`). Both can be sent as they stand: the current `PROMPT.md` goes with the unnumbered zip of its folder. For `7_BISITE`, in case the version of 01:48 UTC was already sent: that version is `PROMPT_v5.md` with `7_BISITE_background_v5.zip`; the current one differs from it by the section "After STRATA" and 15 added files.

The leads of `5_STRATA` itself, as its answer has them and as the review found them:

- Lead 1 (posets): true with two corrections. `Fun(P^op, 𝒮)` is the ∞-topos of hypercomplete sheaves on `P` with downsets open (A.1); without hypercompletion it fails for some infinite posets (A.2; Aoki's example) and holds when principal downsets are finite. For finite `P` it is the constructible sheaves on `|NP|` for the least-vertex stratification (A.4; one step rests on sources the review did not open).
- Lead 2 (general categories): the categories that are stratified homotopy types are exactly those in which every endomorphism is invertible (B.1, B.2); a non-invertible endomorphism is an obstruction that no subdivision removes (B.6, B.7); the geometric dictionary is proved for finite categories without non-identity endomorphisms and isomorphisms (B.3; `R_2` is `RP²` with its flag stratification, B.4) and open for general EI categories (B.5).
- Lead 3 (links): true: the category of crossing arrows is the homotopy link (C.2), the gluing formula is the link gluing (C.3), unrestricted paths give a different answer (C.4); coefficients glue by a lax pullback, which cannot be formed on homotopy categories (C.6, C.7).
- Lead 4: the recollement is known (D.1, D.2). **The second half is false as stated:** proper and smooth functors are characterized by lifting categories (D.3, D.4) and are not the proper maps or submersions of realizations (D.5, D.6); the Kan extensions are the topological direct images for closed inclusions and product projections, not in general (D.8).
- Part E (the bifibration question; the prompt and the answer call it "row VIc-C008", in the current companion register it is row VIc-C022): **new result:** yes over every poset, and over every base whose arrows are all monomorphisms or all epimorphisms (E.10); yes for 1-truncated values and for bases with 1-truncated classifying space (E.8, E.9); open in general, first undecided base the five-element monoid `{1, e_{ij}}` of type `S²` (E.11). The construction by contractible patches proposed after CATHOT has the right classifying space (E.5) and fails without a fibrant replacement (E.7).
- Part F: the exit-path category of `M̄_{0,n}` is the Charney–Lee category (known: Jansen, arXiv:2308.09551); `n = 4, 5` written out; forgetting a point is proper and not smooth (F.10, F.11). This is the input of `LM3_TEICHMULLER_TOWER`, Part F, which no longer waits.


## 11 November 2026: after the PATHS answer

`6_PATHS` has been answered (GPT-6 Astra, ChatGPT Pro mode; 76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open). The record of what was folded in is `..\pro_reviews_20261110\6_PATHS\PROMPT_UPDATES.md` (Claude Fable 5.2); the review is `REVIEW_author.md` beside it (no statement labelled Proved, Known or Refuted found false; the inference in the first item of "After PATHS" in `7_BISITE` checked and right). `7_BISITE` still words the answer as not yet reviewed; it was not rebuilt after the review, because nothing it cites changed and it may have been sent.

`7_BISITE` got a section "After PATHS", a CHANGES entry and a rebuilt zip (`PATHS_return/`, and eight files that `6_PATHS` carried: CATHOT's path section and review, chunk VII-c); two stale sentences that still called II-b, XII §7 and XIII unaudited were corrected. The folder holds `PROMPT.md` and `7_BISITE_background.zip` only; everything else is in `..\pro_prompts_20261110_work\7_BISITE\`. It can be sent as it stands. All seven prompts of this series are now answered or ready.

The leads of `6_PATHS`, as its answer has them (not yet reviewed):

- Lead 1 (weak vertical arrows give the hammock localization): known, with the comparison map made explicit (B.2). Whether Grothendieck's categories with arbitrary vertical arrows have the same type is **open** (B.8): the inclusion is split injective in `Hot` (B.6), an equivalence when `Σ` consists of isomorphisms or of all arrows (B.4), and no counterexample was found in 132 finite cases (B.9).
- Lead 2 (`Σ` = isomorphisms): true; the explanation given in the lead (an initial object) is not sufficient and is replaced (B.4).
- CATHOT E.26 and E.27 (the sequential models against the total category; composition): proved for arbitrary `Σ` (C.P3, C.P4), so row IX-037 holds for the raw construction in `Hot`; the stronger statement modulo natural transformations is false (C.P5, a four-object example).
- Lead 3 (rectifiability; the tests (a), (b), (c) of IX ms. 22–23): its last clause is false: the finite example of IX ms. 23 rectifies every shape and what it lacks is a product (D.2, D.3). Sufficient conditions (D.7, D.8, D.17, D.18), separating examples (D.9–D.13), the comparison with Kaledin (D.14–D.16, D.21); six questions left open (D.22).
- The reviewer's example after TOTASPH (total asphericity does not make colimits in `Cat` correct; the injective ordinals) is confirmed (A.5, A.6); the exact class of shapes is open (A.8).
- Part E: `Ch(X) → X × X` is smooth, not proper, not a bifibration (E.3); the eventual model is smooth and proper, not a bifibration (E.4); a functorial factorization through it (E.5); the bifibration question of STRATA E.11 stays open (E.6, E.11); smooth and proper maps for `W∞` do not preserve a larger `W` under base change (E.9).
