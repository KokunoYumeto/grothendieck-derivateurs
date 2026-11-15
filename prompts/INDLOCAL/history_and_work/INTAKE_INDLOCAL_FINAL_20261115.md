# Intake of the INDLOCAL final return, and consolidation of the unsent Dérivateurs prompts

Claude Fable 5.2, launched at effort high (the intake agent of TOTAL_EXACT_2 and LM8). Work done 14 Nov 2026,
23:18–23:30 UTC by the machine clock. Brief: main session (Claude Opus 5.5 at effort max): a check of sense of the
main results, what is new, and the consolidation of the five unsent prompts in the same pass. No expert step yet;
a joint review comes later.

Return: `pro_prompts_max_20261112_work\INDLOCAL\INDLOCAL_final_20261114T2220Z_unzipped\INDLOCAL\`
(GPT-6 Astra, ChatGPT Pro mode; marked INCOMPLETE). Register: 95 rows: 83 Proved, 6 Refuted, 4 Refuted with
replacement, 1 Verified derivations, 1 Unresolved (A3(iii)-unrestricted). Prompt as sent:
`...\INDLOCAL\PROMPT_as_sent_20261114.md`.

## 1. What this intake is, and what it read

This agent was at 73 % to 85 % of its context during the work, so the reading was kept to the problem's own files.

- Read: the register, all 95 rows (statements; in full for A3(iii), A.11, A.19, A.28, B.3, B.4, B.6–B.9, C.21,
  C.23, C.26, D.17, E.5, and the Part D and E rows); Parts A–E and the task of the prompt as sent; the report's
  lines on A3(iii).
- Proofs read: A.20 in full; D.18 in full, D.19 and D.20 in the passages that carry the argument; B.7 in two
  passages. Everything else is a check of the statement against the prompt, against the rows it depends on and
  against what I know.
- Not read: the proofs of Parts A (except A.20), B (except as said), C and E; D.17's proof; the report beyond the
  A3(iii) lines; `code\`, `logs\`, `research\`; the PDF. No source was opened. The PDF check (overfull boxes,
  rendered pages) was not done.

## 2. Verdicts by Part (sense, not a referee's report)

| Part | What the return says | Sense | Basis and remarks |
|---|---|---|---|
| A (A.1–A.16) | Both proofs of R2 (Kan–Thurston with no small quotients) hold; the kernel `P` can be simple of any cardinality `λ > μ` (A.6); `H_*(P) ≅ H_*(W̃)` is forced (A.7); functorial for injective simplicial maps, and by a replacement for all maps (A.8, A.9); `P ≠ 1` needs `μ < |G|` (A.11); dimension `max(dim W, 3)` for every `μ` (A.16), dimension `dim W` for finite `μ` (A.10) | holds | A.7 and A.11 are immediate; the rest statement level. A.9 corrects the prompt's hope for one functor with simple kernels |
| A (A.19, A.20) | A group with a two-dimensional classifying space and countable `H₁`, `H₂` is residually of cardinality `≤ 2^{ℵ₀}`; so S² has no dimension-two resolution for `μ ≥ 2^{ℵ₀}`; for `⋁_λ S²`, `λ^{ℵ₀} = λ`, exactly `μ < λ` | A.20 follows from A.19 (proof read) | **A.19 rests on a 2026 OpenAI preprint on non-singular systems of equations over groups, unrefereed.** The return says it checked that proof. Nobody on our side has |
| A3(iii) | Undecided: dimension-two resolutions of S² for `ℵ₀ ≤ μ < 2^{ℵ₀}` | OPEN, as the return says | reduced by A.27–A.31 to countable simple quotients satisfying a mixed identity, with a length condition (A.31). Folded into S2COUNT, Part E |
| B (B.1–B.6, B.9) | Both proofs of R3 hold; all invariant small colimits of representables (B.2); `W_n`: ind-groupoids, `W_0`: discrete (B.3); `W_Z`: groupoids with `HZ`-local isotropy (B.4); every `W ⊇ W∞` through `Ho(Grpd)[Π₁(W)⁻¹]` (B.6); enlarged universe (B.5); bounded finite stages are constant (B.9) | holds | B.3 is immediate from R3 (every ind-groupoid depends on `Π₁` only). B.4's class is Bousfield's class of `HZ`-local groups, as I remember its definition (not opened) |
| B.7, B.8 (the prompt's B4) | With stages of at most `μ` arrows, invariance on tests with fewer than `κ` arrows forces an ind-groupoid exactly when `μ⁺ < κ`; below that every homotopy type occurs; the invariant restrictions are classified | holds | the threshold is what A.11 and A.12 give: the test group must have more than `μ` elements and exists with `μ⁺`; it must itself be a test, so `μ⁺ < κ` |
| C (C.1–C.28) | PATHS C.P1–C.P4 confirmed; R7 proved for every wide marking and PATHS B.8 closed (C.7–C.9); one-sign blocks fail (C.6, the four-crown); R8 again (C.11); the exact domain of the path formula (C.20, C.21); exact criteria for invariance (C.14); the manuscript sentences replaced (C.24–C.28), three of them by finite counterexamples | holds at statement level | agrees with the PATHS intake and with TOTAL_EXACT_2 C.40. No proof read |
| D, positive (D.1–D.5, D.7–D.14) | A strict retraction exists in the `Hot` class (D.1), and in the class modulo natural transformations for local or groupoid targets (D.2), for cofibrations finitely presented under their source (D.13), for filtered targets and targets with pushouts or pullbacks (D.14) | holds at statement level | |
| D, the two counterexamples (D.18, D.19; with D.6, D.17, D.20) | `F` = the countable free Thomason-fibrant completion of a point: bifibrant, weakly contractible, identity isolated under natural transformations. Then: a prescribed transformation `a → b` on `{a} → F` extends over no finite fence (D.18); a trivial cofibration `A → B` between countable posets with a retraction up to homotopy and no strict retraction in the class (D.19) | **holds, given D.17** | D.18 and D.19 are short and I followed them. D.17 is the whole content: its mechanism is Stong's (a poset with finite principal ideals and no down beat points admits no `g ≤ id` other than `id`; I checked that half by induction on the ideals). The other half (`g ≥ id`) and the proof of fibrancy were not read |
| E (E.1–E.6) | The expected class (2-types, strict 2-groupoids) is refuted: `B²C₂` is not local (E.1); for strict `n`-categories with strict functors modulo lax transformations, `1 ≤ n ≤ ∞`, the representable types are the 1-types and the invariant ind-objects the ind-groupoids (E.5, E.6) | holds | E.1 checked by hand: there is one strict functor `BC₂ → B²C₂` and `[BC₂, K(C₂, 2)] = H²(C₂; C₂)` has two elements |

Counts by my verdict: no row found wrong; 1 open (A3(iii)); the proof-level reading covers A.20, D.18–D.20 and
E.1 only.

## 3. What is new, and what follows

Against our earlier returns.
- CATHOT E.17 (= R3) stands, with two proofs checked, and is extended to all small colimits, to `W_n`, `W_Z`, every
  larger localizer, bounded tests and the enlarged universe (B.1–B.9).
- CATHOT E.6 (the strict retraction) is **false** in the class modulo natural transformations (D.19), true in
  `Hot` (D.1) and in the finite and local cases (D.2, D.13). Hunch H4 of the CATHOT expert survives as D.2; hunch H5
  ("one dimension up gives 2-types") is refuted (E.1, E.6).
- PATHS B.8 is closed (C.9), R7 is proved (C.7, C.8): the prompt HAMMOCK_FULL named in the war game is no longer
  needed. R8 has a third independent proof (C.11, after the expert's and TOTAL_EXACT_2 C.40). R5 is confirmed (C.27).
- The one row the prompt's hope did not survive in Part A: no acyclic-resolution functor has simple kernels on all
  simply connected inputs (A.9).

Against the literature (from memory; nothing opened).
- The Kan–Thurston theorem and its variants with acyclic or simple groups are classical (Kan–Thurston 1976,
  Baumslag–Dyer–Heller 1980). The form "no homomorphic image of cardinality `≤ μ`" with the cardinal and dimension
  bookkeeping of A.6–A.16 I do not know from the literature. A.19–A.20 (a cardinal obstruction in dimension two)
  would be new; they stand on an unrefereed preprint.
- D.17 is an infinite, Thomason-fibrant counterpart of Stong's cores of finite spaces (Stong 1966;
  Barmak–Minian). That a bifibrant object of Thomason's structure can have `π₀Fun(F, F) → [BF, BF]` non-injective
  (D.6, D.20) I do not know from the literature.
- B.4 connects the invariant ind-objects for `W_Z` with Bousfield's homological localization of groups.

What follows for the companion.
1. V ms. 46 ("factors through `Hot` iff represented by Thomason–Kan categories"): the true statement is the
   theorem on ind-groupoids, now with its exact range: tests of fewer than `κ` arrows see it exactly when
   `μ⁺ < κ` (B.7), and on finite tests the classification is B.8 with B.9.
2. Grothendieck's `Cat hot` (functors modulo natural transformations) is not the homotopy category even on
   bifibrant objects of Thomason's structure (D.6, D.20). Every place of V, VII, IX that argues in `Cat hot` needs
   the localized or the ind-form; C.24–C.28 give the replacements for the sentences the prompt listed.
3. Strict higher categories do not enlarge the class of representable types as long as functors are strict
   (E.5, E.6).
4. A3(iii) is the only undecided row; it is a question of combinatorial group theory about perfect groups of
   geometric dimension two with `H₂ ≅ Z`.

## 4. Consolidation: what was changed in each unsent prompt

Scripts and inserted texts: `...\INDLOCAL\consolidation_20261115\` (`blocks.md`,
`apply_consolidation_20261115.py`, `apply_derf_and_notes_20261115.py`). The first script applied prompts 01–03 and
stopped at DER_FOLLOWUP, whose file has CRLF line ends; the second applied DER_FOLLOWUP with those line ends and
wrote the notes. Backups of each `PROMPT.md` and of each zip touched: `<work folder>\backup_indlocal_intake_20261115\`.
The zips were changed in place (files added; LaTeX, register, report, bibliography; no PDF). The build scripts and
ZIP_LISTs of the prompts do not know the added files: each work folder now has `ZIP_ADD_INDLOCAL_20261115.md`
listing them, to be honoured by any rebuild.

| Prompt | INDLOCAL bears on it through | Change to `PROMPT.md` | Zip | Lint (`--lint-math`) |
|---|---|---|---|---|
| 01_REVERSIBLE_LOCALIZERS | B.3, B.4, B.6 (invariant ind-objects for `W_n`, `W_Z`, every `W ⊇ W∞`): one half of the correspondence asked in Part H.5; D.13, D.16–D.20 (beat points, the isolated identity): Part I; E.1, E.5, E.6: the strict `n`-categories of Part F.3 | new **R13** (results stated; where attached); Part H item 5: a paragraph placing the item on B.3, B.4, B.6 and saying what is left (the way back from local groups to the localizer); Part I: new item 9 (finite fibrant posets; posets with finite principal ideals), "items 1–8" → "1–9" | `REVERSIBLE_LOCALIZERS_new_results.zip`: + `INDLOCAL_return/` (B, B_finite, D, E, main file, register, report, bib): 73 → 81 entries; README extended | passes |
| 02_FINMON | B.8, B.9 (finite tests, bounded finite stages), C.22, C.25, C.26, C.28 (finite categories as tests; the IX tests), D.13 (finite cofibrations): Part F (the manuscript pages) | new **R12**; Part F: a sentence pointing VII ms. 121 and IX ms. 9–13, 23 at those rows, to be checked and built on | `FINMON_new_results.zip`: + `INDLOCAL_return/` (B, B_finite, C_manuscript, D, main file, register, report, bib): 50 → 58 entries; README extended | passes |
| 03_S2COUNT | B.7–B.9 (the threshold; finite tests; bounded stages are constant: so stages for S² are unbounded); **A3(iii)** with A.10, A.13, A.16, A.19, A.20, A.27–A.31 | new **R5**; new **Part E** "The two-dimensional acyclic resolutions of S²" (E1 check A.19, A.20, A.28 and the preprint's theorem; E2 the case `μ = ℵ₀`; E3 the whole interval below the continuum; E4 general simply connected 2-complexes; E5 the consequence for bounded tests) | `S2COUNT_background.zip`: + `INDLOCAL_return/` (all 15 A sections, B, B_finite, main file, register, report, bib): 37 → 58 entries; 21 MANIFEST rows | passes |
| 04_FRAISSE_EXACT | nothing: no INDLOCAL row concerns exactness of abelian colimits or automorphism groups of Fraïssé limits; C.27 (filtered indices) is already among its known results | none | none | passes (unchanged) |
| 05_DER_FOLLOWUP | Part C of INDLOCAL: C.2–C.4 (PATHS C.P1–C.P4 confirmed), C.5–C.6 (one sign), C.7–C.9 (PATHS B.8 closed), C.11 (R12 again), C.21, C.23 (sequences of types; the uniform fibred comparison), C.27, C.24–C.28 | header: "INDLOCAL (unsent) …" replaced by its outcome; new **R18**; Part B: an opening paragraph placing B.2–B.5 on C.21, C.23 and saying what is left (fibred categories over `Ty` that are not path diagrams) | `DER_FOLLOWUP_background.zip`: + `INDLOCAL/return/` (C_paths, C_manuscript, C_relative, C_crown, main file, register, report, bib): 161 → 169 entries; 8 MANIFEST rows | passes |

Where A3(iii) went and why: 03_S2COUNT. It is the prompt about S² and about what small or low-dimensional models
of it can do, it works on the same manuscript pages (V ms. 43–52), it is the smallest of the five, and INDLOCAL's
B.7 (which S2COUNT now carries as R5) is the statement that A3(iii) feeds. DER_FOLLOWUP was the alternative; it is
already the largest prompt and none of its Parts is about groups.

What was taken out as settled: in DER_FOLLOWUP the statement that INDLOCAL "checks" PATHS C.P1–C.P4 (now: done,
not to be redone). No numbered task of the five prompts was fully settled by INDLOCAL; REVERSIBLE_LOCALIZERS H.5
and DER_FOLLOWUP B were narrowed to what is left.

## 5. For whoever continues

- Not done by me: the tally (`MATHS_PROMPTS_TALLY.md` and its script), the agents' registry, STATUS.md, the PDF
  check of `INDLOCAL_paper.pdf`, retiring the superseded checkpoints.
- 01_REVERSIBLE_LOCALIZERS has CRLF line ends; the lines I inserted may be LF. Harmless for the lint; normalized
  if the last check below says so.
- Seen while working, not changed: the last MANIFEST row of `DER_FOLLOWUP_background.zip` shows a source path with
  the user's first name, where other manifests write "user" or `%USERPROFILE%`. A point for the next rebuild if
  that zip is ever published.
- For the joint review: read D.17 (fibrancy and the `g ≥ id` half) and A.19 with the preprint it uses; these two
  carry the two results of the return that would be new.
