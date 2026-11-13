# PRESHEAF_TOTALITY: totally aspherical presheaves, Grothendieck's Dwyer-type immersions for `W∞`

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix: `PRETOT`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max), Dérivateurs expert; revised the same day so that it starts
from the results now in hand (the draft before this revision: `PROMPT_before_results_20261112.md`). Follow-up to
TOTASPH (return 2), Parts E–G. The files to attach are listed in `ZIP_LIST.tsv`.

## Where this comes from

XII ms. 88–89, Définition 1: a presheaf `H` on `U` is *totalement `W`-asphérique* when the category of elements
`U'/p_!H` is `W`-aspherical for every functor `p: U → U'`. XII ms. 107–114: an open immersion (sieve)
`U ⊂ X` is *`W`-dwyérienne* when every non-empty crossing presheaf `Hom_X(−, t)|U` is totally `W`-aspherical, and
*totalement `W`-dwyérienne* when every non-empty `U/t` is a totally `W`-aspherical category. Grothendieck asks
(ms. 111, Question (a)) whether a sieve that is a couniversal `W`-equivalence is `W`-dwyérienne, doubts
(ms. 113–114) that these classes are stable under composition, and wants (ms. 114) a class of sieves stable under
the operations he needs later.

## Results this prompt builds on (status on 12 Nov 2026)

"TOTASPH" and "POLES" are returns of GPT-6 Astra (effort Pro); "review" is the row-by-row check by Claude Fable
5.2 at effort max (the two `REVIEW.md` files in the zip). None of these is to be proved again as if open. For
each one you use: read the proof at the place given and either confirm the step you rely on in one paragraph of
your own, or give the exact error with a repair or a counterexample.

- **R1 (TOTASPH E.8, F.15, F.20; checked in the review).** For a presheaf `H` with `E = U/H`, `π: E → U`: `H` is
  totally `W_Z`-aspherical iff `E` and every component of every `El_E(L∘π)`, `L: U → Set`, is integrally acyclic;
  the weighted colimit `H ⊗_U −: sSet^U → sSet` is homotopical iff all those components are contractible; a
  one-point attachment `U ⊂ U ∪_H {t}` is a couniversal `W∞`-equivalence iff `H` is totally `W_Z`-aspherical, and
  then `π_1(U/H) → π_1(U)` is trivial.
- **R2 (TOTASPH F.6–F.9; checked, F.7 and F.8 step by step).** Strictly and totally aspherical functors compose
  for every fundamental localizer; totally `W∞`-dwyérienne sieves compose; total sieve composition holds for
  `W∞`, `W_R` and fails for `W_0`, `W_1`.
- **R3 (TOTASPH F.18–F.20; checked).** Question (a) of XII ms. 111 has the answer no for general complements:
  `{a} ⊂ (a ⇉ t → s)` is a couniversal `W∞`-equivalence that is not dwyérienne. For one-point complements the
  question is R5 below.
- **R4 (TOTASPH F.23, F.24; checked).** If `S²` is not `W`-aspherical, the endpoint pushout-product
  `({0} ⊂ [1]) □ ({0, 2n} ⊂ Φ_n)` is not a `W`-cofibration, and a class of sieves made of `W`-cofibrations and
  closed under `− □ j` contains only isomorphisms. So the class asked for at XII ms. 114 does not exist for `W∞`.
- **R5 (TOTASPH F.26, F.27; F.26 checked).** Open, in five equivalent forms: every totally `W_Z`-aspherical
  presheaf is totally `W∞`-aspherical; `W∞`-dwyérienne sieves are discretely flat
  (Hackney–Ozornova–Riehl–Rovelli); `W∞`-dwyérienne sieves compose; total `W∞`-asphericity of presheaves
  restricts to non-empty cosieves; one-point couniversal `W∞`-equivalences are `W∞`-dwyérienne.
- **R6 (reviewer, effort max; review row F.27; not checked by anyone).** R5 is true when `U` is a group, when `H`
  is terminal or subterminal, and whenever `π_1(U/H)` has a non-trivial cyclic quotient visible in `U`. A natural
  candidate fails: for `U = Δ_inj` and `H = K` the acyclic semi-simplicial set with perfect `π_1` of TOTASPH A.12,
  the restricted action `L` = "vertices, all identified from dimension 2 on" gives a category equivalent to the
  vertex–triangle incidence graph, with `H_1 = Z^{28}`; so `K` is not totally `W_Z`-aspherical.
- **R7 (POLES B.2, H.5, H.6 and Cisinski, Astérisque 308, Prop. 9.2.17; checked in the POLES review).** For every
  fundamental localizer in Cisinski's sense, Dwyer immersions are `W`-cofibrations and the forward
  Mayer–Vietoris axioms hold; every sieve is a `W`-cofibration iff `W_1 ⊂ W` iff `S²` is `W`-aspherical; the
  pushout-product fails as in R4.
- **R8 (TOTASPH G.3, G.5; and the reviewer, `FINDINGS.md` F2-11, from Grothendieck's own remarks at XII ms.
  102–103, 112; not checked).** For `Y` simply connected the endpoint functor of `Ch(Y; y_0, −)` is final, so
  `Ch(Y; y_0, −)` totally `W∞`-aspherical ⇒ `Y` totally `W∞`-aspherical.
- **R9 (reviewer, effort max; `RESULT_FILTERED_BY_ONE_TYPES.md`, complete proof; not checked by anyone; no
  literature search).** For a small category `A`: `∫_A D → colim^{Cat}_A D` is a weak equivalence for every
  `D: A → Cat` iff `A` is filtered. The test diagrams in the proof are set-valued ones and, for each parallel
  pair `u, v`, one diagram of right-angled Artin groups of bipartite graphs. (The earlier example
  `A = Δ_inj`, `D([n]) = N^{[n]}`, with `H_q(B∫D) = Z` for all `q` against `B colim D ≃ S¹`, is `FINDINGS.md`
  F2-13: found by the earlier review at effort medium, re-derived at effort max.)

## What the outcome must be

Deliverables: `PRETOT_paper.tex` and PDF, `PRETOT_results.csv` (one row per numbered statement:
`id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`), bibliography with
opened / not opened, `PRETOT_report.md`, `code/` with outputs.

What counts as done per item: (a) a theorem with complete proof; (b) a complete counterexample, machine-checked
when finite; (c) failing both: cases proved, computations run, the obstruction as one exact statement with the
smallest undecided instance. An item that says "check" is done only as: every step confirmed with your own
argument, or the first wrong step with a repair or a counterexample.

Not acceptable: a status report; "open" without your own attack; proving R1–R4 or R7 again in place of the items
below; a counterexample to Part A verified only against finitely many `p` or `L` when the definition quantifies
over all; any use of the covering argument of TOTASPH C.4 for actions that do not factor through
`π: U/H → U` without saying how they are obtained.

Finished only when Part A is decided in sense (a) or (b), or every item of Parts A–F has reached (a), (b) or (c).
On disconnection: retry ten minutes, then write all files out in the chat and continue there.

## Parts

**A. The main question (R5).** Prove or refute: if `H` is a presheaf on a small category `U` such that `U'/p_!H` is
non-empty, connected and integrally acyclic for every `p: U → U'`, then `U/H` is simply connected. By R1 and R6 a
counterexample has perfect `π_1(U/H)` invisible from `U`, and `U` is not a group.
1. Prove it for `U` a monoid, for `U` a poset, for `U` with finitely many arrows, or give a counterexample in the
   first of these classes where it fails.
2. Enlargement: for a totally `W_Z`-aspherical `H` and a cyclic subgroup `C ≤ π_1(U/H)`, construct a functor
   `p: U → U'` and `L': U' → Set` such that some component of `El_{U'/p_!H}(L'π')` is a connected covering of
   (a category weakly equivalent to) `U/H` with group `C`, or prove that no such pair exists for a specified `H`.
3. Search: enumerate presheaves `H` on small monoids and small one-way categories (give the bounds reached) for
   which `U/H` is acyclic with non-trivial `π_1`, and test the criterion R1 on the generating functors `L`
   (quotients of representables). Report the smallest surviving candidates, or a proof that none survives within
   the bounds. (An enumeration of all monoids of order ≤ 6 and all categories with ≤ 7 arrows, with exact
   integral homology of nerves, exists with its programs: `catlib.py`, `enum_monoids.py`, `enum_cats.py` in the
   zip; made by Claude Fable 5.2 at effort max for another review, not checked by a second party. Start from it
   or from your own.)
4. Check the computation of R6 (`H_1 = Z^{28}`), then characterize the semi-simplicial sets `K` that are totally
   `W_Z`-aspherical as presheaves on `Δ_inj`, and the simplicial sets that are so as presheaves on `Δ`.

**B. Consequences in both cases.** If A is true: state and prove the resulting theorems (composition of
`W∞`-dwyérienne sieves; they are discretely flat; exact characterization of one-point couniversal equivalences),
and extend R1 from one-point complements to arbitrary complements: characterize the sieves `U ⊂ X` that are
couniversal `W∞`-equivalences by a condition on the crossing bimodule `Hom_X(u, t)` (R3 shows the pointwise
condition is not it). If A is false: give the counterexample to each of the five forms explicitly, and the exact
classes in between.

**C. Sieve composition for the truncated localizers.** For `W_n`, `n ≥ 2` (TOTASPH F.9, F.27; R7 covers `n ≤ 1`,
where every sieve is a cofibration): decide whether non-empty full cosieves of totally `W_n`-aspherical categories
are totally `W_n`-aspherical without finiteness (first case `W_2`, countable categories), and whether
`W_n`-dwyérienne sieves compose.

**D. The class Grothendieck wanted at XII ms. 114, repaired (starting from R4 and R7).** Construct the largest
class of sieves that is stable under cobase change and under a *modified* endpoint operation (specify it: for
instance the pushout-product followed by a functorial Dwyer replacement, or the product with the subdivided
interval), prove that its members are `W∞`-cofibrations, and prove that it suffices for the use Grothendieck
announces ("pour des applications ultérieures": locate that use in XII §3 and XIII and check it). Decide whether
the class of Dwyer immersions itself (R7) already suffices for that use.

**E. Path categories (starting from R8).** (i) Check R8. Decide the converse; first case `Y = e`, where
`Ch(e; ∗, −)` is the category of interval types of VII §§4–6: is it totally `W∞`-aspherical, is its affinization
filtered, is it filtered? (ii) For which `Y` is the endpoint functor `Ch(Y; y_0, −) → Y` strictly, resp. totally,
`W∞`-aspherical in the sense of XII Définition 2?

**F. `Cat`-valued diagrams (starting from R9).**
1. Check the theorem of `RESULT_FILTERED_BY_ONE_TYPES.md` step by step (naturality of `H_2` of the right-angled
   Artin groups, the fundamental group of the homotopy colimit, the spectral sequence), and search the
   literature for it; say, after opening the source, whether it is there.
2. Smaller classes of test diagrams. For each of the following classes `𝒟`, determine the shapes `A` such that
   `∫_A D → colim_A D` (colimit in the class named) is a weak equivalence for all `D: A → 𝒟`: posets with the
   colimit in posets; posets with the colimit in `Cat`; groupoids; categories with a terminal object; abelian
   groups (the remark in the note: such `A` are total, sifted and have exact abelian colimits; is every such `A`
   filtered?); free monoids.
3. Other localizers: for `W = W_n` and for `W = W_Z`, determine the shapes `A` such that `∫_A D → colim^{Cat}_A D`
   is in `W` for all `D: A → Cat`. (For `W_0` every `A` qualifies; for `W_1` the question is when the
   pseudo-colimit of groupoids is the strict colimit.)
4. Locate in VII §10 (ms. 102–103) and VII §§4–6 each place where a colimit of categories is taken along a
   system of types or of path categories; for each, say whether the shape is filtered, and if it is not, whether
   the statement made there survives.

**G. Statement of results** against XII ms. 94–97, 103, 111, 113–114, XIIapp ms. 13–18, VII §10, II ms. 36ter (the
form of the conjecture that is true by R9), with the exact passage for each.

Rules of proof and conventions: as in the common block of the TOTASPH prompt (`_COMMON_BLOCK.md` in the zip); no
authority: R1–R9 are to be checked where used, R6, R8 and R9 in full.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority.
