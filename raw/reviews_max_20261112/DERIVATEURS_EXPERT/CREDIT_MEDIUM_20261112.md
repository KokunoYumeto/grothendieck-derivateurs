# Credit for the effort-medium and effort-high Fable work: evidence per entry (12 November 2026)

Asked by the user on 12 Nov 2026: give Claude Fable 5.2 at effort medium credit where it found things first, because a
result found at medium matters to people who cannot pay for max; and (addition) check the 10 Nov files, some at effort
high, for who first stated or proved the U(M) argument, the answer to Conjecture 7.1, and the step "BM
finite-dimensional ⇒ U(M) = 1". Traced by Claude Opus 5.5 (subagent; its effort setting was not given to it), by grep
over the review, prompt and return files and over the agents' transcripts. Paths are relative to
`C:\Users\user\Documents\derivateurs_companion_20261109\` unless they start otherwise.

## Who wrote what, and at which effort

Effort read from the agents' transcripts (`"effort"` field of every turn) under
`C:\Users\user\.claude\projects\C--Users-user-Documents\`; dates from the files' own headers and the transcripts'
timestamps (UTC).

| File | Agent (transcript) | Model, effort | Date |
|---|---|---|---|
| `pro_prompts_20261110/1_CATHOT/PROMPT.md` (written as `3_CATHOT`), also the POLES prompt | `329fb1e6…/subagents/agent-a83fb615cfe40b3ff` ("Fable pilot: Dérivateurs whole picture") | Claude Fable 5.2, **high** (421 turns, all "high") | 10 Nov, 16:41 UTC |
| `pro_reviews_20261110/1_CATHOT/REVIEW_author.md` | same agent a83fb615cfe40b3ff | Fable 5.2, **high** | 10 Nov, written 18:55 UTC |
| `pro_reviews_20261110/1_CATHOT/REVIEW.md` and `checks/` | `329fb1e6…/subagents/agent-a7b3c0a70067aaf7e` ("Fable review of the CATHOT answer") | Fable 5.2, **medium** | 10 Nov, 18:44–19:10 UTC (header: "10 November 2026") |
| `pro_reviews_20261110/2_TOTAL_ASPHERICITY/REVIEW_author.md` | `329fb1e6…/subagents/agent-ae41699c8244b12b8` ("Fable successor: TOTASPH review") | Fable 5.2, **medium** | 10 Nov, 21:13–21:56 UTC (header: "10–11 November 2026") |
| `pro_reviews_20261110/4_GALOIS/REVIEW_author.md` | `329fb1e6…/subagents/agent-a477d182d2ac42002` ("Integrate the GALOIS answer") | Fable 5.2, **medium** | 11 Nov, written 00:47 UTC |
| `pro_reviews_20261110/1_CATHOT/REVIEW_G6.md`, `DRAFT_NOTE_TO_AUTHOR.md` | `fbe1d313…/subagents/agent-ac003b3dbb4b890ee` ("Fable reviews BISITE and all seven", resumed) | Fable 5.2, **medium** | 11 Nov, 23:40–23:58 UTC (header line 3) |
| `pro_reviews_max_20261112/…` | the 12 Nov experts | Fable 5.2, **max** | 12 Nov |

Note on dates: the user's message speaks of the medium agents "of 11 Nov"; the CATHOT and TOTASPH medium reviews are in
fact of 10 Nov (headers and transcripts), REVIEW_G6 and the GALOIS review of 11 Nov. The credits use the exact dates.

## The three questions of the addition

1. **The universal-group argument** (the maximal subgroup H = eMe of the minimal ideal maps onto U(M) = π₁(BM); the
   map BH → BM through the Karoubi envelope; Miller's Theorem B makes it trivial on π₁ when BM is finite-dimensional).
   First stated and proved by **GPT-6 Astra** in the CATHOT return: `pro_returns_20261110/1_CATHOT/CATHOT/CATHOT_results.csv`
   line 78 (G.4, "Karoubi-envelope map from finite maximal subgroup surjects on fundamental group"), `CATHOT_report.md`
   line 261, `sections/G.tex`. Fable at medium checked it on 10 Nov (`REVIEW.md` line 97, "I checked the Karoubi-envelope
   step and the surjection") and on 11 Nov wrote out the one step the return only asserted, the computation of the map
   on π₁ (`REVIEW_G6.md` line 28, Step 3; line 42: "Step 3's computation on π₁ is only asserted in the return … it is
   written out above and is right"). Fable at high (10 Nov) marked G.4 "unverified" (`REVIEW_author.md` line 57).
2. **The answer to Conjecture 7.1** (RP² is not BM). First stated and proved by **GPT-6 Astra** (G.6,
   `CATHOT_results.csv` line 80, "Refuted … RP2 counterexample"; `sections/G.tex` line 72: "this refutes Conjecture 7.1"),
   in answer to Part G (i) of the prompt ("which are nerves of finite monoids", `pro_prompts_20261110/1_CATHOT/PROMPT.md`
   line 35), written by **Fable at high**, 10 Nov. Checked by Fable at medium on 10 Nov (`REVIEW.md` line 99: "proved …
   G.4 refutes it for every finite complex with non-trivial finite π₁"); completed and checked against the published texts
   of Miller and Atiyah, with a second proof through Atiyah's theorem, and the conjecture and arXiv version verified, by
   Fable at medium on 11 Nov (`REVIEW_G6.md` lines 3–51; route (b) line 34). That file and `DRAFT_NOTE_TO_AUTHOR.md` are
   what the e-mail to the author of 12 Nov was built on (RUNBOOK_20261110.md line 940). Re-checked from scratch by Fable
   at max, 12 Nov (`pro_reviews_max_20261112/1_CATHOT/G6_VERDICT.md`, `EMAIL_CLAIMS_CHECK.md`).
3. **The step "BM finite-dimensional ⇒ U(M) = 1"** is G.4 itself: GPT-6 Astra, as in 1.
4. **"That whole envelope thing."** If this means the Thomason–Kan envelope of Chapter V (published finding
   `FINDINGS/2026-11-10_thomason-kan-envelope.md`): its non-existence was **Fable at high**'s Lead 1, with a sketch of
   the proof (`PROMPT.md` line 17: "`ψ` does not exist … Let `G` be the finitary alternating group …"), and the
   1-type classification was its conjecture (Lead 2, line 18); GPT-6 Astra gave the complete proofs (B.1–B.4, C);
   Fable at high confirmed "Lead 1 is confirmed and the argument is complete" (`REVIEW_author.md`), Fable at medium
   checked it and statements 3–5 (`REVIEW.md`). The published page said only "Claude Fable 5.2"; it now names the
   efforts (commit 38b5740).

## Per entry of NEW_RESULTS.md

### 1. Finite monoids: finite type ⇔ finite dimension ⇔ bounded homology; U(M) trivial

- Evidence. Medium: did **not** state the equivalence, bounded homology, finite type or any corollary (grep for "bounded",
  "finite type", "infinitely many degrees", "Swan", "cohomological dimension" in `pro_reviews_20261110/`: no such
  statement). It proved, by checking and completing the return's proof, only the implication "BM of finite-dimensional
  type ⇒ U(M) = 1" (G.4, GPT-6 Astra's). It came near in method: its route (b) (`REVIEW_G6.md` line 34, 11 Nov) is the
  K-theory argument (flat bundle, skeletal filtration of K⁰, Atiyah (7.2), (6.11)) that OWN_RESULTS §1 (12 Nov) uses with
  "finite dimension" replaced by "cohomology vanishing above n" ("The proof is Miller's and Atiyah's, with the
  covering-space step replaced by the regular representation", `OWN_RESULTS.md` line 32); and it noted that ordinary
  cohomology alone does not give the step (`REVIEW_G6.md` line 43). Max: `pro_reviews_max_20261112/1_CATHOT/FINDINGS.md`
  F2–F3 (lines 19–33), `OWN_RESULTS.md` §§1–2; its own comparison says "No sharpening of G.4 … new here" (line 142).
- Old credit: Proved by "Claude Fable 5.2, effort max, 12 Nov 2026".
- New credit: equivalences and corollaries, Claude Fable 5.2 (effort max), 12 Nov 2026; the finite-dimensional case is
  G.4 of the return (GPT-6 Astra); its K-theoretic proof through Atiyah, the route §§1–2 extend, first written for this
  problem by Claude Fable 5.2 (effort medium), 11 Nov 2026; the medium review did not state the general statement.
  Same in the published README note (commit 38b5740).

### 2. Miller's Theorem B under a cohomological bound

- Evidence: not in the medium or high files (the medium's remark at `REVIEW_G6.md` line 43 is about ordinary cohomology
  not sufficing, not this statement). Max: `OWN_RESULTS.md` §1, FINDINGS F11.
- Credit unchanged: Claude Fable 5.2, effort max.

### 3. Kan–Thurston without small quotients; E.17

- Evidence. Medium, 10 Nov: `pro_reviews_20261110/1_CATHOT/REVIEW.md` lines 112–120, "A reduction for E.17": statement
  (KT_μ), the proof of E.17 from it, and the expected route via Maunder ("I have not checked Maunder's induction"); line
  72 "I expect the answer yes". The reduction went into the GALOIS prompt (`pro_prompts_20261110/4_GALOIS/PROMPT.md`
  lines 37–41, (KT_μ) verbatim). GPT-6 Astra proved (KT_μ) and E.17 for small filtered index categories in the GALOIS
  return (`pro_returns_20261110/4_GALOIS/GALOIS/GALOIS_results.csv` lines 19–21, B.10–B.12, Proved; B.11 cites "CATHOT
  E17 missing KT_mu"; B.12: "the small-index version of CATHOT E.17 is settled"), on file 11 Nov. Medium, 11 Nov
  00:47 UTC: `pro_reviews_20261110/4_GALOIS/REVIEW_author.md` §7 (line 72 ff.) "followed in full" B.11, including the
  step it had left unchecked. Max, 12 Nov: `OWN_RESULTS.md` §3 by a different construction; line 233–235 credits the
  medium reduction; DERIVATEURS_EXPERT FINDINGS F4-5 (line 258): "Two proofs by two systems".
- Old credit: Proved by "Claude Fable 5.2, effort max (the reduction also in the earlier review, effort medium)"; Checked
  by "not yet; the Kan–Thurston cardinality bound was quoted from memory".
- New credit: reduction first found by Claude Fable 5.2 (effort medium), 10 Nov 2026; (KT_μ) and E.17 first proved by
  GPT-6 Astra (effort Pro), GALOIS B.10–B.12, 11 Nov 2026; re-proved independently by Claude Fable 5.2 (effort max),
  12 Nov 2026. Checked by: GALOIS B.11–B.12 followed in full by Claude Fable 5.2 (effort medium), 11 Nov, and read by the
  expert at effort max, 12 Nov; OWN_RESULTS §3 not yet.
- This also corrects a gap beyond the medium question: NEW_RESULTS had not named the GALOIS return's proof.

### 4. Uncountably many maps to S²

- Evidence: medium came near but did not state it. `REVIEW.md` line 52 (10 Nov), on D.6: "a finite category or monoid
  whose nerve has the type of CP^∞ would give uncountably many classes (phantom maps to S³, composed with the Hopf map)";
  a different, conditional route. Max FINDINGS line 134 calls that remark correct and line 150 lists "the criterion for
  uncountably many maps to S²" as not in the earlier review.
- Credit unchanged.

### 5. Posets of type RP²: at least 34 arrows

- Evidence: medium has only the return's interval [28, 49] (`REVIEW.md` line 101). Max line 150: not there.
- Credit unchanged.

### 6. Census of small categories

- Evidence. Question: CATHOT prompt Part G (ii) (line 35), Fable high, 10 Nov. Return: G.14 (Proved), G.15 (minima
  (2,4), (1,5), (1,7); "Known", monoid orders 5–6 from Sweeney's tables), `CATHOT_results.csv` lines 88–89. Medium,
  10 Nov: `REVIEW.md` line 13 (own enumeration of all categories with at most 6 arrows), line 107 (G.14 reproduced; "At
  5 arrows exactly the six labellings of P_2 have the homology of S²"), line 108 (G.15 "proved, by my enumeration in place
  of the answer's citation": all 4,122 monoids of order 5 and 208,672 of order 6), line 165 (the minima table), line 186.
  Programs: `pro_reviews_20261110/1_CATHOT/checks/enum_small_categories.py`, `enum_monoids.py` and outputs (10 Nov
  19:53–20:09 local). Max FINDINGS lines 127–128 and 144–145: the same counts; the medium did not do 7-arrow categories
  with several objects and did not state uniqueness of the smallest S¹ and S².
- Old credit: "Claude Fable 5.2, effort max (exhaustive enumeration)".
- New credit: question by Claude Fable 5.2 (effort high), 10 Nov; minima from the return (GPT-6 Astra); first proved
  without the Sweeney citation by Claude Fable 5.2 (effort medium), 10 Nov, which also found that only P₂ has the
  homology of S² at 5 arrows (uniqueness follows with G.9; not stated there); re-proved by Claude Fable 5.2 (effort max),
  12 Nov, which is first for S¹ uniqueness, the stated S² uniqueness, every smallest S³ a monoid, and the 10 arrows of
  Grothendieck's model.

### 7. A reversible fundamental localizer not detected by spectra

- Evidence: not in medium or high files; max DERIVATEURS_EXPERT FINDINGS F3-11 (line 200). Credit unchanged.

### 8. XII Théorème 2 (ms. 78) false for W∞

- Evidence. First appearance found: the companion's commentary returns on XII (GPT-6 Astra, ChatGPT Pro mode, per
  `METHODOLOGY.md` line 8): `returns/DER_XIIb-a/DER_XIIb-a_overview.tex` line 37 ("Theorem 2 on manuscript p. 78 asserts
  … A complete counterexample …") and `returns/DER_XIIb-b/audit_parts/partA_claims.csv` line 46 (XIIbb-A045: "W_infty does
  not satisfy full W(7 bis) or full W(7)"); files dated 10 Nov 15:57 local. The POLES prompt (Fable high, 10 Nov) cites it
  as "The companion's audit found that Théorème 2 of XII ms. 78 … is false" (`pro_prompts_20261110/3_POLES/PROMPT.md`
  line 12). TOTASPH return A.13 (GPT-6 Astra; `pro_returns_20261110/2_TOTAL_ASPHERICITY/TOTASPH/TOTASPH_results.csv`
  line 14, Refuted). Medium, 10–11 Nov: `pro_reviews_20261110/2_TOTAL_ASPHERICITY/REVIEW_author.md` line 51 (A.13
  proved; 37 objects, 231 arrows reproduced) and line 14 (its program). Max: DERIVATEURS_EXPERT FINDINGS F-G1 (line 9),
  found from Grothendieck's text.
- Old credit: Proved by "Claude Fable 5.2, effort max (also TOTASPH A.13 of the return)"; Checked by "Pro return + expert
  agree".
- New credit: first in the commentary on XII and in TOTASPH A.13 (GPT-6 Astra); found again independently by Claude
  Fable 5.2 (effort max), 12 Nov. Checked by: Claude Fable 5.2 (effort medium), 10–11 Nov (A.13, category recomputed);
  Pro return + expert at max agree. Not a medium first; the medium contributed the check.

### 9. W_Z and W_k fail Loc (7 F): direct proof

- Evidence: max FINDINGS F3-5 (line 172); the comparison (line 228) lists it as missed by the medium POLES review.
  Credit unchanged.

### 10. Y simply connected, Ch(Y; y₀, −) total ⇒ Y total

- Evidence: max FINDINGS F2-11 (line 70); line 127–128: not in the medium TOTASPH review. Credit unchanged.

### 11. Δ_inj against II ms. 36ter

- Evidence. Medium, 10–11 Nov: `pro_reviews_20261110/2_TOTAL_ASPHERICITY/REVIEW_author.md` line 28 (C.7–C.10 proved, the
  chain written out), line 12 (C.8–C.9 recomputed by its own program, "3, 29 and 932 non-zero coefficients"), lines
  64–65 (C.1–C.10 proved; "the exactness fact is Isbell–Mitchell's (AKR 1981, A.5)"). Max FINDINGS lines 96–100 agree
  and add that the medium did not open Isbell–Mitchell 1973.
- Old credit: Checked by "Claude Fable 5.2, effort max".
- New credit: Checked by Claude Fable 5.2 (effort medium), 10–11 Nov, then Claude Fable 5.2 (effort max), 12 Nov.
  Proved-by unchanged (GPT-6 Astra; the Open Maths lesson).

### 12. Counterexample to Conjecture 7.1

- Evidence: see questions 1–3 above.
- Old credit: Proved by "GPT-6 Astra (effort Pro)"; Checked by "Claude Fable 5.2 (effort medium, 11 Nov; again at effort
  max, 12 Nov)".
- New credit: Proved by GPT-6 Astra (effort Pro), G.4 and G.6, answering Part G (i) of the prompt set by Claude Fable 5.2
  (effort high), 10 Nov. Checked by Claude Fable 5.2 (effort medium), 10 Nov; completed (the π₁ step written out, a second
  proof through Atiyah) and checked against the published texts by Claude Fable 5.2 (effort medium), 11 Nov; re-checked
  by Claude Fable 5.2 (effort max), 12 Nov.

## Where the credit was changed

- `NEW_RESULTS.md`: entries 1, 3, 6, 8, 11, 12, and a sentence in the preamble.
- github.com/KokunoYumeto/grothendieck-derivateurs, commit 38b5740 (on top of 565b12c; pulled, committed, pushed, no
  force): `raw/reviews_max_20261112/1_CATHOT/README.md` ("Additional finding" status list) and
  `FINDINGS/2026-11-10_thomason-kan-envelope.md` (Status: efforts of the question-setter and of the two readers).
- `C:\Users\user\Documents\pro_admin_readers_20261112_work\03_DERIVATEURS_READERS\CREDIT_CORRECTION_20261112.md`:
  to apply to the readers' return; the sent zip is unchanged.
- Not changed: the companion appendix (does not exist yet; it is to be built from NEW_RESULTS by the readers' return),
  and the medium review files themselves.
