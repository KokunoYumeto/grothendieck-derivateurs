# TOTAL_EXACT: is total asphericity the same as exactness of abelian colimits?

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for the deliverables: `TOTEX`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max), Dérivateurs expert; revised the same day so that it starts
from the results now in hand (the draft before this revision: `PROMPT_before_results_20261112.md`). Follow-up to
TOTASPH (return 2). The attached files are listed in `MANIFEST.tsv` at the root of `TOTAL_EXACT_background.zip`.

Attached in that zip, besides the files named below: the return TOTASPH (paper, results table, report, the TeX of
Parts C and D, the prompt it answered); Isbell–Mitchell 1973 and Adámek–Koubek–Reiterman 1981; three of the sources
named in D.1 (Adámek–Rosický–Vitale 2010 on sifted colimits, `AdamekRosickyVitale2010_sifted.pdf`; Lurie, *Higher
Topos Theory*, `Lurie_HTT.pdf`; Cegarra 2020 on homotopy colimits of small categories, `Cegarra2020_hocolim.pdf`);
Grothendieck's text in `DER_II-a.tex` (II ms. 1–53) and `DER_XIIb-a.tex` (XII ms. 59–122): the French transcription
corrected on 11 Nov 2026, AI-made from the edition of Künzer, Malgoire and Maltsiniotis, manuscript pages marked
`\msp{page N}`; where a formula looks wrong, say so and reason from the mathematics. Of `_COMMON_BLOCK.md` only the
conventions, the rules of proof and the form of the deliverables apply; its paragraph "WHAT IS ATTACHED" describes the
zip of an earlier prompt. The Open Maths lesson of R3 is not attached; it is online at
https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/derived-colimits-over-a-small-category.html,
and the construction R3 uses is written out in TOTASPH C.9, C.10 (`TOTASPH_C.tex`).

Also attached since this prompt was drafted: the return PRESHEAF_TOTALITY (`PRETOT_return/`: paper, results table, report, bibliography, programs and finite certificates; GPT-6 Astra, ChatGPT Pro mode, 12 November 2026; not yet reviewed). Its statements are claims: check what you use. Those that bear on this prompt: Theorem A.5 (a 52-element right act `H` over the 10-element monoid `End_Δ([2])` such that `U'/p_!H` is nonempty, connected and integrally acyclic for every `p: M → U'`, while `π₁B(M/H)` is nontrivial and perfect: total `W_ℤ`-asphericity does not imply total `W∞`-asphericity); Theorems B.2–B.4 (separating examples between Dwyer, totally dwyérienne, dwyérienne, discretely flat and homotopical-cofibration sieves); its §5 (the diagram-shape theorem corrected to componentwise filteredness, with a table of test classes including abelian groups with colimits in `Ab`); and its reading of II ms. 36ter (totality does not imply filteredness). Where they bear on R1–R6 above, say so at that row, and build on them or refute them.

## Where this comes from

Grothendieck (II ms. 36–36ter; XII ms. 88–89, Définition 1) calls a small category `A` *totalement
`W∞`-asphérique* when every category receiving a final functor from `A` is aspherical, and suspects that this
means filtered. The question of this prompt is what the class of totally aspherical categories is.

## Results this prompt builds on (status on 12 Nov 2026)

"TOTASPH" is the return of GPT-6 Astra (effort Pro) to the earlier prompt; "review" is the row-by-row check of it
by Claude Fable 5.2 at effort max (`2_TOTAL_ASPHERICITY_REVIEW.md` in the zip). None of these is to be proved
again as if open. For each one you use: read the proof at the place given and either confirm the step you rely on
in one paragraph of your own, or give the exact error with a repair or a counterexample.

- **R1 (TOTASPH C.5; checked in the review).** `A` is totally `W∞`-aspherical iff `A` is non-empty, connected and
  every component of every category of elements `El_A(H)`, `H: A → Set`, is weakly contractible; equivalently
  integrally acyclic; equivalently `hocolim_A K → colim_A K` is a weak equivalence for every `K: A → sSet`.
  Consequence used below: `L_k colim_A Z[H] = 0` for `k > 0` and every `H`.
- **R2 (TOTASPH C.6, D.4; checked).** If `colim_A: Ab^A → Ab` is exact (Isbell–Mitchell 1973, Th. 1: the
  components of the affinization `Aff_Z(A)` are filtered) and `A` is non-empty and connected, then `A` is totally
  `W∞`-aspherical.
- **R3 (known: Isbell–Mitchell, Bull. AMS 79 (1973), Th. 3, opened by the reviewer; re-proved in TOTASPH C.9,
  C.10 by the interpolation construction of our Open Maths lesson "Derived colimits over a small
  category" of 20 Oct 2026, whose address is in `TOTASPH_CD_report.md`).** `Aff_Z(Δ_inj)` is filtered and
  `Δ_inj` is not filtered. So Grothendieck's conjecture of II ms. 36ter is false.
- **R4 (TOTASPH C.11, D.16, D.17; checked; Adámek–Koubek–Reiterman 1981, Theorem [1], opened).** Total ⇒
  quasi-filtered: spans complete to commutative squares, and every parallel pair `a, b: p → q` has an affine
  equalizer (`t ∈ Z[A(q, r)]` of coefficient sum 1 with `ta = tb`). So
  `{Aff_Z-filtered} ⊂ {total} ⊂ {quasi-filtered}`, and the outer classes differ (their Th. C.2: the category `K*`).
- **R5 (TOTASPH C.13; checked).** With a weakly terminal object (in particular for monoids and for finite
  categories) total ⇔ filtered. **So no finite category and no monoid separates the classes; do not search
  there.** (The census of all monoids of order ≤ 6 and all categories with ≤ 7 arrows made for another review is
  therefore of no use here.)
- **R6 (TOTASPH D.7).** Open in the return: does total imply exact?
- **R7 (reviewer, Claude Fable 5.2, effort max; in the review, row D.7 (c), and `HUNCHES.md` H1; not checked by
  anyone).** For `a_0, a_1, a_2: p → q` put `P_x = Z[A(x, −)]`, `K_i = {t ∈ P_q : t(a_i − a_0) = 0}`. A
  simultaneous affine equalizer exists iff `aug(K_1 ∩ K_2) = Z`, and `Z/aug(K_1 ∩ K_2)` is a quotient of
  `Tor_1^{ZA}(ΔZ, P_q/(K_1 + K_2))`. For a presented `H`, `H_1(El_A(H))` is (cycles of the presentation
  graph)/(augmentations of syzygies), and quasi-filteredness makes it vanish for all `H`; so the first condition
  of totality beyond quasi-filteredness is the vanishing of the groups `H_2(El_A(H))`.
- **R8 (reviewer, effort max; `RESULT_FILTERED_BY_ONE_TYPES.md`, complete proof; not checked by anyone; no
  literature search).** `A` is filtered iff `A` is totally `W∞`-aspherical and `hocolim_A BM(a)` is 1-truncated
  for every `M: A → Grp`; iff `∫_A D → colim^{Cat}_A D` is a weak equivalence for every `D: A → Cat`. Remark of
  the same note: if `A` is total and `hocolim_A K(M(a), 1)` is 1-truncated for every `M: A → Ab`, then `colim_A`
  is exact on `Ab^A` and `A` is sifted. So
  `{filtered} = {total, and 1-types preserved} ⊊ {Aff_Z-filtered} ⊂ {total} ⊂ {quasi-filtered}`,
  and Grothendieck's conjecture is true one level up. What stays open is the middle inclusion (R6) and the
  abelian form of R8.
- **R9 (reviewer; `FINDINGS.md` F2-6; one-line proofs from R1, not checked).** Total categories are closed under
  final images (Grothendieck, XII ms. 112), finite products, Grothendieck op-fibrations with total fibres over a
  total base, and passage to components of categories of elements; the first three also preserve exactness of
  abelian colimits.
- **R10 (reviewer; a heuristic, not a proof; review row D.7 (d)).** Adjoining a new maximal object `Z` changes
  `B El` by a cone on `B(old ↓ Z)`; for a freely adjoined quasi-filter of a pair this is a circle that is already
  null-homotopic, so `H_2 ≠ 0` appears. Expectation: `K*` is not total.

## What the outcome must be

Deliverables: `TOTEX_paper.tex` and PDF (LuaLaTeX), `TOTEX_results.csv` (one row per numbered statement:
`id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`), `TOTEX_references.bib`
(each entry marked opened / not opened), `TOTEX_report.md`, `code/` with every program and its output.

What counts as done, per item of the Parts below: (a) a theorem with a complete proof; or (b) a counterexample
given completely (objects, arrows, composition, verification of every hypothesis), checked by a program when
finite or finitely presented; or (c) if neither is reached: the cases proved, the computations run, and the
obstruction as one exact statement with the smallest undecided instance. An item that says "check" is done only
as: every step confirmed with your own argument, or the first wrong step with a repair or a counterexample.
"Known" counts only with the derivation of the statement used here from the cited theorem.

Not acceptable: a survey; "open, see [reference]"; a plan or an outline; proving R1–R5 again in place of the
items below; a proof that total implies exact which at any step replaces a set-valued functor `Z[H]` by an
arbitrary abelian functor without proof; a claimed counterexample whose total asphericity is verified only on
finitely many functors `H`; an item dropped without a row.

Finished only when Part A is decided in sense (a) or (b), or every item of Parts B–F has reached (a), (b) or (c).
If the execution environment disconnects: wait and retry for ten minutes, then write every file out in the chat in
full and continue there.

## Parts

**A. The main question (R6).** Prove or refute: for every small non-empty connected category `A`, if every
component of every `El_A(H)` (`H: A → Set`) is integrally acyclic, then every finite family of parallel arrows
`a_0, …, a_k: p → q` of `A` has a simultaneous affine equalizer (by Isbell–Mitchell's Lemma 1 this is equivalent to
`Aff_Z(A)` filtered, given common successors). Either outcome settles TOTASPH D.7. By R5 a counterexample has
infinitely many objects and no weakly terminal object; by R8 it is not filtered but may be sifted.

**B. Triples, starting from R7.**
1. Check R7 (both formulas). Then compute, for `H_3 = A(p, −)/(ca_0 ∼ ca_1 ∼ ca_2)`, the groups
   `H_1(El_A(H_3))` and `H_2(El_A(H_3))` in terms of `K = {(t_1, t_2) : t_1(a_1 − a_0) + t_2(a_2 − a_0) = 0}`
   (expected: `Z²/aug(K)` and `ker(colim_A K → Z²)`), with proof.
2. Decide whether total asphericity of `A` (all `H`, including the categories of elements of categories of
   elements, which are again total by R9) forces `aug(K_1 ∩ K_2) = Z`. Use every `H` you need; say which.
3. Compute `H_j(El_A(H))`, `j = 1, 2, 3`, as explicit `Tor` groups for the functors `H` presented by one
   generator and finitely many relations `ca_i ∼ ca_j`, and identify the condition on the affine equalizers that
   each vanishing expresses.

**C. The Adámek–Koubek–Reiterman category, starting from R10.** Take `K*` of their Construction C.1 (and the
variant with the general quasi-filters of their Part B).
1. Turn R10 into a proof that `K*` is not totally `W∞`-aspherical, or find the error and decide the question
   otherwise: compute `H_2(El(h_V/(cv_1 ∼ cv_2)))` on the stages `K_1`, `K_2` by program (the stages are finite),
   then prove the statement for `K*`.
2. If `K*` is not total: find the smallest modification of the construction that makes every `El(H)` acyclic, and
   decide whether it then acquires a simultaneous affine equalizer of `v_1, v_2, v_3`.

**D. Between filtered and exact, starting from R8.**
1. Check the theorem of `RESULT_FILTERED_BY_ONE_TYPES.md` (the naturality of `H_2` of the right-angled Artin
   groups in the diagram, the fundamental group of the homotopy colimit, the spectral sequence) and its abelian
   remark. Search the literature for it (Gabriel–Ulmer; Adámek–Rosický–Vitale on sifted colimits; Lurie, HTT
   5.3; work on homotopy colimits in `Cat`) and say, after opening the source, whether it is there.
2. Prove or refute: a sifted totally `W∞`-aspherical category is filtered. (Then abelian diagrams suffice in
   R8.) If refuted, give the category completely and decide whether its abelian colimits are exact.
3. Prove or refute: if `A` is total and `hocolim_A K(M(a), n)` is `n`-truncated for every `M: A → Ab` and one
   fixed `n ≥ 2`, then `A` is filtered; and determine, for each `n ≥ 0`, the class `𝒯_n` of shapes over which
   homotopy colimits preserve `n`-truncated spaces (`𝒯_0` = total by R1; `𝒯_0 ∩ 𝒯_1` = filtered by R8; every
   group `BG` is in `𝒯_n` for `n ≥ 1` and not in `𝒯_0`). Is `𝒯_n ⊂ 𝒯_{n+1}` for `n ≥ 1`?
4. The stable form of the main question: for `A` total, prove or refute that the homotopy colimit over `A` of
   Eilenberg–MacLane spectra `HM(a)` is Eilenberg–MacLane for every `M: A → Ab` (this is exactness), and decide
   it for `M` with values in `F_p`-vector spaces and in `Q`-vector spaces separately.
5. Animated abelian groups: for `F: A → Ab` let `G_F(Z^n) = colim^{Set}_A (UF)^n`, a presheaf of sets on finitely
   generated free abelian groups. Prove: if `A` is total then `L_i colim_A F = π_i(L G_F)`, `L` the reflection to
   product-preserving presheaves of spaces. Decide for which presheaves of sets `G` on that category `L G` is
   discrete, and whether every `G_F` is of that kind when `A` is total.
6. Starting from R9: find one operation under which the classes "total" and "`Aff_Z`-filtered" behave
   differently, or prove there is none among: full cosieves, localizations, idempotent completion, filtered
   colimits of categories along final functors.

**E. New examples.** Construct at least three non-filtered totally `W∞`-aspherical categories not equivalent to
`Δ_inj` or to products and final images of it with filtered categories, with proofs (for instance: injections of
finite sets with extra structure; the subdivision category of a filtered category; categories whose hom-sets are
monomials with a substitution law for which the interpolation argument of R3 works). For each, decide
filteredness of `Aff_Z`, siftedness, and whether it has a final functor from or to `Δ_inj`. By R8 none of them
preserves 1-types: exhibit for each a diagram of groups whose homotopy colimit is not 1-truncated.

**F. Statement of results** against: Grothendieck's question at II ms. 36 and the conjecture of ms. 36ter (the
correct statement, with R8), TOTASPH D.7, and the literature (Isbell–Mitchell 1973 and 1976; Oberst 1968;
Adámek–Reiterman 1976; Adámek–Koubek–Reiterman 1981; Husainov 2002): for each statement proved, say whether it is
in one of these, with theorem number, after opening the source.

Rules of proof, conventions and the form of the deliverables are those of the common block of the TOTASPH prompt
(`_COMMON_BLOCK.md` in the zip; variance: presheaves in the manuscript, covariant `H` for `El_A(H)`; "final" = all
`b\A` non-empty connected; every map typed; every counterexample complete and machine-checked; no authority: the
results R1–R10 are to be checked where used, R7, R8 and R10 in full).

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority.
