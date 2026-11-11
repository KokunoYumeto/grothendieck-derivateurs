# README updates after STRATA (Claude Fable 5.2, 11 Nov 2026). Run once.
DER = r"C:\Users\user\Documents\derivateurs_companion_20261109\pro_prompts_20261110\README.md"
LMR = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\README.md"
def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s): open(p, "w", encoding="utf-8", newline="\n").write(s)
s = rd(DER)
for old, new in [
    ("| 5 | `5_STRATA` | **Run now**, all parts", "| 5 | `5_STRATA` | **Answered 11 Nov** (81 statements; reviewed: see the last section). Was: **Run now**, all parts"),
    ("| 6 | `6_PATHS` | **Run now**, all parts", "| 6 | `6_PATHS` | **Run now**, all parts (11 Nov, after STRATA: section \"After STRATA\" added, zip rebuilt; not sent before that)"),
    ("| 7 | `7_BISITE` | **Run now** (", "| 7 | `7_BISITE` | **Run now** (11 Nov, after STRATA: section \"After STRATA\" added, zip rebuilt; the version made ready at 01:48 UTC is kept as `PROMPT_v5.md` with `7_BISITE_background_v5.zip`) ("),
]:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
s = s.rstrip("\n") + r"""

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
"""
wr(DER, s + "\n")

s = rd(LMR)
old = "**Parts A–E can run now**, better after the 33 open fixes of P011–P040 are merged. **Part F waits** for the output of the Dérivateurs prompt `5_STRATA`."
assert s.count(old) == 1
s = s.replace(old, "**Can run now, all parts**, better after the 33 open fixes of P011–P040 are merged. Part F no longer waits: the answer to the Dérivateurs prompt `5_STRATA` came back on 11 Nov and is folded in (see the last section).")
s = s.rstrip("\n") + r"""

## 11 November 2026: after the STRATA answer of the Dérivateurs series

The Dérivateurs prompt `5_STRATA` has been answered (GPT-6 Astra, ChatGPT Pro mode; 81 statements: 54 Proved, 14 Known, 9 Refuted, 4 Open) and reviewed by Claude (Fable 5.2): no statement labelled Proved, Known or Refuted was found false. Record: `C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\5_STRATA\PROMPT_UPDATES.md`; review: `REVIEW_author.md` beside it.

- `LM3_TEICHMULLER_TOWER`: section "After STRATA" before "Recent results" (the category `T_{0,n}` and its opposite, the cases `n = 4, 5`, his groups of §19, the forgetful and clutching functors with their properties, and five suggestions for Part F marked as unverified inferences); the sentence of Part F that said "if its output is attached" now says that it is. Zip rebuilt with 37 added files (`STRATA_return/`, `STRATA_review/`, Jansen's paper, *Exodromy*); the previous zip is `LM3_TEICHMULLER_TOWER_background_v2.zip`; `MANIFEST.tsv`, `ASSEMBLY.md`, `BACKGROUND_ADD.md`, `CHANGES_20261110.md` updated. **Ready to send, all parts.**
- `LM4_FINITE_GROUP_ACTIONS`: short section "After STRATA" (a group with loops as a category in which every endomorphism is invertible; his groups of §19). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P06–P10.
- `LM5_MULTI_GALOIS_TOPOI`: section "After STRATA" (gluing a topos from an open part, a closed part and the link; two candidate comparisons for `B_{X,U}`, marked as an unverified inference; the forgetful functor and its fibres). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P01, P02.
- `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS`: unchanged (no contact with STRATA).

No lead of this stack is refuted or settled by STRATA.
"""
wr(LMR, s + "\n")
print("ok")
