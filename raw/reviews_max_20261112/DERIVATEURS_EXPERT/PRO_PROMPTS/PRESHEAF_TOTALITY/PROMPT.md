# PRESHEAF_TOTALITY: totally aspherical presheaves, Grothendieck's Dwyer-type immersions for `W∞`

Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max), Dérivateurs expert, for GPT-6 Astra (ChatGPT Pro mode).
Follow-up to TOTASPH (return 2), Parts E–G. File prefix: `PRETOT`. To attach: TOTASPH sections E, F, F_followup, G
and results CSV; `REVIEW.md` of 12 Nov; `HUNCHES.md` (H3); Grothendieck's text `DER_XIIb-a` (XII ms. 87–114),
`DER_XIIapp` (ms. 10–18), `DER_VII-a`, `DER_VII-b` (the path categories); Hackney–Ozornova–Riehl–Rovelli
(arXiv:2205.02353); Cisinski 1999 and 2006 as in the TOTASPH zip.

## Where this comes from

XII ms. 88–89, Définition 1: a presheaf `H` on `U` is *totalement `W`-asphérique* when the category of elements
`U'/p_!H` is `W`-aspherical for every functor `p: U → U'`. XII ms. 107–114: an open immersion (sieve)
`U ⊂ X` is *`W`-dwyérienne* when every non-empty crossing presheaf `Hom_X(−, t)|U` is totally `W`-aspherical, and
*totalement `W`-dwyérienne* when every non-empty `U/t` is a totally `W`-aspherical category. Grothendieck asks
(ms. 111, Question (a)) whether a sieve that is a couniversal `W`-equivalence is `W`-dwyérienne, and doubts
(ms. 113–114) that these classes are stable under composition.

TOTASPH settled most of it (checked in the review): for a presheaf `H` with `E = U/H`, `π: E → U`:
`H` is totally `W_Z`-aspherical iff `E` and every component of every `El_E(L∘π)`, `L: U → Set`, is integrally
acyclic (E.8); the weighted colimit `H ⊗_U −: sSet^U → sSet` is homotopical iff all those components are
contractible (F.15); a one-point attachment `U ⊂ U ∪_H {t}` is a couniversal `W∞`-equivalence iff `H` is totally
`W_Z`-aspherical (F.20); strictly and totally aspherical functors compose for every fundamental localizer (F.7,
F.8); totally `W∞`-dwyérienne sieves compose (F.6). **Open (F.26–F.27), five equivalent forms:** every totally
`W_Z`-aspherical presheaf is totally `W∞`-aspherical; `W∞`-dwyérienne sieves are discretely flat;
`W∞`-dwyérienne sieves compose; total `W∞`-asphericity of presheaves restricts to non-empty cosieves; one-point
couniversal `W∞`-equivalences are `W∞`-dwyérienne.

## What the outcome must be

Deliverables: `PRETOT_paper.tex` and PDF, `PRETOT_results.csv` (one row per numbered statement), bibliography with
opened / not opened, `PRETOT_report.md`, `code/` with outputs.

What counts as done per item: (a) a theorem with complete proof; (b) a complete counterexample, machine-checked
when finite; (c) failing both: cases proved, computations run, the obstruction as one exact statement with the
smallest undecided instance.

Not acceptable: a status report; "open" without your own attack; a counterexample to Part A verified only against
finitely many `p` or `L` when the definition quantifies over all; any use of the covering argument of TOTASPH C.4
for actions that do not factor through `π: U/H → U` without saying how they are obtained.

Finished only when Part A is decided in sense (a) or (b), or every item of Parts A–E has reached (a), (b) or (c).
On disconnection: retry ten minutes, then write all files out in the chat and continue there.

## Parts

**A. The main question.** Prove or refute: if `H` is a presheaf on a small category `U` such that `U'/p_!H` is
non-empty, connected and integrally acyclic for every `p: U → U'`, then `U/H` is simply connected.
Known: true for `H` terminal or subterminal, and for `U` a group; `π_1(U/H) → π_1(U)` is always trivial (F.20), so
a counterexample has perfect `π_1(U/H)` invisible from `U`.
1. Prove it for `U` a monoid, for `U` a poset, for `U` with finitely many arrows, or give a counterexample in the
   first of these classes where it fails.
2. Enlargement: for a totally `W_Z`-aspherical `H` and a cyclic subgroup `C ≤ π_1(U/H)`, construct a functor
   `p: U → U'` and `L': U' → Set` such that some component of `El_{U'/p_!H}(L'π')` is a connected covering of
   (a category weakly equivalent to) `U/H` with group `C`, or prove that no such pair exists for a specified `H`.
3. Search: enumerate presheaves `H` on small monoids and small one-way categories (give the bounds reached) for
   which `U/H` is acyclic with non-trivial `π_1`, and test the restricted-action criterion E.8 on the generating
   functors `L` (quotients of representables). Report the smallest surviving candidates, or a proof that none
   survives within the bounds.
4. The reviewer's test case, to be reproduced and extended: `U = Δ_inj`, `H = K` an acyclic two-dimensional
   semi-simplicial set with perfect `π_1` (TOTASPH A.12); the functor `L` = "vertices, all identified in
   dimensions ≥ 2" gives `El_{U/H}(Lπ)` equivalent to the vertex–triangle incidence graph, so `K` is not totally
   `W_Z`-aspherical. Characterize the semi-simplicial sets `K` that are totally `W_Z`-aspherical as presheaves on
   `Δ_inj`, and the simplicial sets that are so as presheaves on `Δ`.

**B. Consequences in both cases.** If A is true: state and prove the resulting theorems (composition of
`W∞`-dwyérienne sieves; they are discretely flat; exact characterization of one-point couniversal equivalences),
and extend F.20 from one-point complements to arbitrary complements: characterize the sieves `U ⊂ X` that are
couniversal `W∞`-equivalences by a condition on the crossing bimodule `Hom_X(u, t)`. If A is false: give the
counterexample to each of the five forms explicitly, and the exact classes in between.

**C. Sieve composition for the truncated localizers.** For `W_n`, `n ≥ 2` (TOTASPH F.9, F.27): decide whether
non-empty full cosieves of totally `W_n`-aspherical categories are totally `W_n`-aspherical without finiteness
(first case `W_2`, countable categories), and whether `W_n`-dwyérienne sieves compose.

**D. The class Grothendieck wanted at XII ms. 114, repaired.** TOTASPH F.23–F.24: for `W∞` no class of sieve
`W`-cofibrations is stable under the ordinary pushout-product with `{0, 2n} ⊂ Φ_n`. Construct the largest class of
sieves that is stable under cobase change and under a *modified* endpoint operation (specify it: for instance the
pushout-product followed by a functorial Dwyer replacement, or the product with the subdivided interval), prove
that its members are `W∞`-cofibrations, and prove that it suffices for the use Grothendieck announces ("pour des
applications ultérieures": locate that use in XII §3 and XIII and check it).

**E. Path categories.** (i) For `Y` simply connected, TOTASPH G.3 gives: `Ch(Y; y_0, −)` totally
`W∞`-aspherical ⇒ `Y` totally `W∞`-aspherical. Decide the converse; first case `Y = e`, where `Ch(e; ∗, −)` is the
category of interval types of VII §§4–6: is it totally `W∞`-aspherical, is its affinization filtered, is it
filtered? (ii) For which `Y` is the endpoint functor `Ch(Y; y_0, −) → Y` strictly, resp. totally,
`W∞`-aspherical in the sense of XII Définition 2?

**F. `Cat`-valued diagrams.** TOTASPH B.11 concerns simplicial sets. For `D: A → Cat` and the colimit in `Cat`,
the map `∫D → colim_Cat D` can fail to be a weak equivalence over a totally aspherical `A` (example: `A = Δ_inj`,
`D([n]) = N^{[n]}`; to be re-proved). Characterize the small categories `A` such that `∫D → colim_Cat D` is in
`W∞` for every `D: A → Cat`; prove that filtered categories have the property and decide whether any non-filtered
category has it. This is the question behind VII §10 (ms. 102–103).

**G. Statement of results** against XII ms. 94–97, 103, 111, 113–114, XIIapp ms. 13–18, VII §10, with the exact
passage for each.

Rules of proof and conventions: as in the common block of the TOTASPH prompt.
