# READMEs of the two prompt stacks after the PATHS answer. Claude Fable 5.2, 11 Nov 2026. Run once.
DER = "C:/Users/user/Documents/derivateurs_companion_20261109/pro_prompts_20261110/README.md"
LM = "C:/Users/user/Documents/longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111/README.md"
BS = chr(92)


def rd(p):
    return open(p, encoding="utf-8").read()


def wr(p, s):
    open(p, "w", encoding="utf-8", newline="\n").write(s)


s = rd(DER)
assert "after the PATHS answer" not in s
old6 = "| 6 | `6_PATHS` | **Run now**, all parts"
old7 = "| 7 | `7_BISITE` | **Run now** ("
assert s.count(old6) == 1 and s.count(old7) == 1
s = s.replace(old6, "| 6 | `6_PATHS` | **Answered 11 Nov** (76 statements; folded into `7_BISITE`; review pending: see the last section). Was: **Run now**, all parts")
s = s.replace(old7, "| 7 | `7_BISITE` | **Run now** (11 Nov, after PATHS: section \"After PATHS\" added, zip rebuilt, 295 files; the previous zip is `_work" + BS + "7_BISITE_background_v6.zip`) (")
if not s.endswith("\n"):
    s += "\n"
s += """
## 11 November 2026: after the PATHS answer

`6_PATHS` has been answered (GPT-6 Astra, ChatGPT Pro mode; 76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open). The record of what was folded in is `..{b}pro_reviews_20261110{b}6_PATHS{b}PROMPT_UPDATES.md` (Claude Fable 5.2); the review will be `REVIEW_author.md` beside it. Until then the answer is cited as unverified.

`7_BISITE` got a section "After PATHS", a CHANGES entry and a rebuilt zip (`PATHS_return/`, and eight files that `6_PATHS` carried: CATHOT's path section and review, chunk VII-c); two stale sentences that still called II-b, XII §7 and XIII unaudited were corrected. Top level of the folder: `PROMPT.md` and `7_BISITE_background.zip`; everything else is in `_work{b}`. It can be sent as it stands. All seven prompts of this series are now answered or ready.

The leads of `6_PATHS`, as its answer has them (not yet reviewed):

- Lead 1 (weak vertical arrows give the hammock localization): known, with the comparison map made explicit (B.2). Whether Grothendieck's categories with arbitrary vertical arrows have the same type is **open** (B.8): the inclusion is split injective in `Hot` (B.6), an equivalence when `Σ` consists of isomorphisms or of all arrows (B.4), and no counterexample was found in 132 finite cases (B.9).
- Lead 2 (`Σ` = isomorphisms): true; the explanation given in the lead (an initial object) is not sufficient and is replaced (B.4).
- CATHOT E.26 and E.27 (the sequential models against the total category; composition): proved for arbitrary `Σ` (C.P3, C.P4), so row IX-037 holds for the raw construction in `Hot`; the stronger statement modulo natural transformations is false (C.P5, a four-object example).
- Lead 3 (rectifiability; the tests (a), (b), (c) of IX ms. 22–23): its last clause is false: the finite example of IX ms. 23 rectifies every shape and what it lacks is a product (D.2, D.3). Sufficient conditions (D.7, D.8, D.17, D.18), separating examples (D.9–D.13), the comparison with Kaledin (D.14–D.16, D.21); six questions left open (D.22).
- The reviewer's example after TOTASPH (total asphericity does not make colimits in `Cat` correct; the injective ordinals) is confirmed (A.5, A.6); the exact class of shapes is open (A.8).
- Part E: `Ch(X) → X × X` is smooth, not proper, not a bifibration (E.3); the eventual model is smooth and proper, not a bifibration (E.4); a functorial factorization through it (E.5); the bifibration question of STRATA E.11 stays open (E.6, E.11); smooth and proper maps for `W∞` do not preserve a larger `W` under base change (E.9).
""".format(b=BS)
wr(DER, s)

t = rd(LM)
assert "after the PATHS answer" not in t
if not t.endswith("\n"):
    t += "\n"
t += """
## 11 November 2026: after the PATHS answer of the Dérivateurs series

The Dérivateurs prompt `6_PATHS` has been answered (GPT-6 Astra, ChatGPT Pro mode; 76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open); under review by Claude (Fable 5.2), so cited as unverified. Record: `C:{b}Users{b}user{b}Documents{b}derivateurs_companion_20261109{b}pro_reviews_20261110{b}6_PATHS{b}PROMPT_UPDATES.md`.

- `LM4_FINITE_GROUP_ACTIONS`: short section "After PATHS" before the Parts (strict against homotopy-coherent actions, PATHS D.1, D.4, D.11, D.13; a reading of the essential-surjectivity problem in three layers, marked as an unverified inference). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P06–P10.
- `LM5_MULTI_GALOIS_TOPOI`: section "After PATHS" before the Parts (a second proof of GALOIS B.11–B.12; finite tests do not determine a morphism of classifying topoi, PATHS E.13, with an unverified inference on profinite completions; the shapes of Kaledin's theorem; filtered colimits of categories). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P01, P02.
- `LM3_TEICHMULLER_TOWER`: not edited (it was being sent). What of PATHS bears on its answer is listed in the record above.
- `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS`: unchanged (no contact with PATHS).

No lead of this stack is refuted or settled by PATHS; the run-now-or-wait table is unchanged.
""".format(b=BS)
wr(LM, t)
print("ok")
