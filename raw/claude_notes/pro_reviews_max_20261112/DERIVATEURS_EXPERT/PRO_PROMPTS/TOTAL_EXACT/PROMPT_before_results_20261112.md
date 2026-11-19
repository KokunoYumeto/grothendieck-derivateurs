# TOTAL_EXACT: is total asphericity the same as exactness of abelian colimits?

Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max), Dérivateurs expert, for GPT-6 Astra (ChatGPT Pro mode).
Follow-up to TOTASPH (return 2). File prefix for the deliverables: `TOTEX`. To attach: the TOTASPH return
(paper, sections C, D, D_followup, E; results CSV), `REVIEW.md` of 12 Nov, `HUNCHES.md` (H1), Grothendieck's
text `DER_II-a` (II ms. 30–36ter) and `DER_XIIb-a` (XII ms. 87–103), Isbell–Mitchell 1973 (Bull. AMS 79, 994–996),
Adámek–Koubek–Reiterman 1981 (Czech. Math. J. 31, 368–389), Isbell–Mitchell 1976 if it can be obtained.

## Where this comes from

Grothendieck (II ms. 36–36ter; XII ms. 88–89, Définition 1) calls a small category `A` *totalement
`W∞`-asphérique* when every category receiving a final functor from `A` is aspherical, and suspects that this
means filtered. TOTASPH proved (checked in the review):

- (C.5) `A` is totally `W∞`-aspherical iff `A` is non-empty, connected and for every `H: A → Set` every connected
  component of the category of elements `El_A(H)` is weakly contractible; equivalently every such component is
  integrally acyclic; equivalently `hocolim_A K → colim_A K` is a weak equivalence for every `K: A → sSet`.
- (C.6, D.4) If `colim_A: Ab^A → Ab` is exact, i.e. (Isbell–Mitchell 1973, Th. 1) the affinization `Aff_Z(A)` has
  filtered components, and `A` is non-empty and connected, then `A` is totally `W∞`-aspherical. Example: `Δ_inj`
  (Isbell–Mitchell, Th. 3), which is not filtered; so Grothendieck's conjecture is false.
- (C.11, D.16, D.17) A totally `W∞`-aspherical category is quasi-filtered in the sense of Adámek–Reiterman: spans
  complete to commutative squares and every parallel pair `a, b: p → q` has an affine equalizer
  (`t ∈ Z[A(q, r)]` of coefficient sum 1 with `ta = tb`).
- (C.13) With a weakly terminal object, total ⇔ filtered.
- (D.7) **Open:** does total imply exact?

So `{Aff_Z-filtered} ⊂ {total} ⊂ {quasi-filtered}`, and the outer classes differ (Adámek–Koubek–Reiterman 1981,
Th. C.2: a quasi-filtered `K*` with three parallel arrows `v_1, v_2, v_3: V → W` that no affine arrow equalizes
simultaneously).

## What the outcome must be

Deliverables: `TOTEX_paper.tex` and PDF (LuaLaTeX), `TOTEX_results.csv` (one row per numbered statement:
`id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`), `TOTEX_references.bib`
(each entry marked opened / not opened), `TOTEX_report.md`, `code/` with every program and its output.

What counts as done, per item of the Parts below: (a) a theorem with a complete proof; or (b) a counterexample
given completely (objects, arrows, composition, verification of every hypothesis), checked by a program when
finite or finitely presented; or (c) if neither is reached: the cases proved, the computations run, and the
obstruction as one exact statement with the smallest undecided instance. "Known" counts only with the derivation
of the statement used here from the cited theorem.

Not acceptable: a survey; "open, see [reference]"; a plan or an outline; a proof that total implies exact which
at any step replaces a set-valued functor `Z[H]` by an arbitrary abelian functor without proof; a claimed
counterexample whose total asphericity is verified only on finitely many functors `H`; an item dropped without a
row.

Finished only when Part A is decided in sense (a) or (b), or every item of Parts B–E has reached (a), (b) or (c).
If the execution environment disconnects: wait and retry for ten minutes, then write every file out in the chat in
full and continue there.

## Parts

**A. The main question.** Prove or refute: for every small non-empty connected category `A`, if every component
of every `El_A(H)` (`H: A → Set`) is integrally acyclic, then every finite family of parallel arrows
`a_0, …, a_k: p → q` of `A` has a simultaneous affine equalizer (by Isbell–Mitchell's Lemma 1 this is equivalent to
`Aff_Z(A)` filtered, given common successors). Either outcome settles D.7.

**B. The first undecided instance: triples.** For `a_0, a_1, a_2: p → q` put `P_x = Z[A(x, −)]`,
`K_i = {t ∈ P_q : t(a_i − a_0) = 0}` (`i = 1, 2`), `K = {(t_1, t_2) : t_1(a_1 − a_0) + t_2(a_2 − a_0) = 0}` and
`H_3 = A(p, −)/(ca_0 ∼ ca_1 ∼ ca_2)`.
1. Prove (the reviewer's computation, to be checked): `H_1(El_A(H_3)) = Z²/aug(K)`,
   `H_2(El_A(H_3)) = ker(colim_A K → Z²)`; a simultaneous affine equalizer exists iff `aug(K_1 ∩ K_2) = Z`; and
   `Z/aug(K_1 ∩ K_2)` is a quotient of `Tor_1^{ZA}(ΔZ, P_q/(K_1 + K_2))`.
2. Decide whether total asphericity of `A` (all `H`, including the categories of elements of categories of
   elements, which are again total by C.3–C.5) forces `aug(K_1 ∩ K_2) = Z`. Use every `H` you need; say which.
3. Compute `H_j(El_A(H))`, `j = 1, 2, 3`, as explicit `Tor` groups for the family of functors `H` presented by one
   generator and finitely many relations `ca_i ∼ ca_j`, and identify the condition on the affine equalizers that
   each vanishing expresses ("coherence" between equalizers of different pairs).

**C. The Adámek–Koubek–Reiterman category.** Take `K*` of their Construction C.1 (and the variant with the
general quasi-filters of their Part B).
1. Decide whether `K*` is totally `W∞`-aspherical. The reviewer's heuristic: adjoining a new maximal object `Z`
   changes `B El` by a cone on `B(old ↓ Z)`; for a freely adjoined quasi-filter this is a circle that is already
   null-homotopic, so `H_2 ≠ 0` appears and is not killed later. Turn this into a proof or find the error:
   compute `H_2(El(h_V/(cv_1 ∼ cv_2)))` on the stages `K_1`, `K_2` by program (the stages are finite), then prove
   the statement for `K*`.
2. If `K*` is not total: find the smallest modification of the construction that makes every `El(H)` acyclic, and
   decide whether it then acquires a simultaneous affine equalizer of `v_1, v_2, v_3`.

**D. Structural routes.** Each to be carried to a theorem or to an exact obstruction.
1. Sifted case: prove that a totally `W∞`-aspherical category that is sifted has exact abelian colimits (the
   forgetful functor `Ab → Set` commutes with sifted colimits, and by B.11 colimits over `A` are homotopical), and
   decide whether the same holds for `1`-sifted replaced by weaker conditions that `Δ_inj` satisfies.
2. Animated abelian groups: for `F: A → Ab` let `G_F(Z^n) = colim^{Set}_A (UF)^n`, a presheaf of sets on finitely
   generated free abelian groups. Prove: if `A` is total then `L_i colim_A F = π_i(L G_F)`, `L` the reflection to
   product-preserving presheaves of spaces. Decide for which presheaves of sets `G` on that category `L G` is
   discrete, and whether every `G_F` is of that kind when `A` is total.
3. Other coefficient rings and the stable statement: prove or refute, for `A` total, that homotopy colimits over
   `A` of Eilenberg–MacLane spectra `HM_a` are again Eilenberg–MacLane (this is exactness), and that homotopy
   colimits over `A` of `n`-truncated spaces are `n`-truncated for `n = 1` (groupoids). Give the exact class of
   shapes for `n = 1` if it differs from `n = 0`.
4. Closure properties: prove that both classes (total; `Aff_Z`-filtered) are closed under final images, finite
   products, Grothendieck op-fibrations with fibres and base in the class, and passage to components of
   categories of elements; find one operation under which the two classes behave differently, or prove there is
   none among: full cosieves, localizations, idempotent completion, filtered colimits of categories along final
   functors.

**E. New examples.** Construct at least three non-filtered totally `W∞`-aspherical categories not equivalent to
`Δ_inj` or to products and final images of it with filtered categories, with proofs (for instance: injections of
finite sets with extra structure; the subdivision category of a filtered category; categories whose hom-sets are
monomials with a substitution law for which an interpolation argument as in TOTASPH C.8–C.9 works). For each,
decide filteredness of `Aff_Z`, siftedness, and whether it has a final functor from or to `Δ_inj`.

**F. Statement of results** against: Grothendieck's question at II ms. 36 and the conjecture of ms. 36ter (what
the correct statement is), TOTASPH D.7, and the literature (Isbell–Mitchell 1973 and 1976; Oberst 1968;
Adámek–Reiterman 1976; Adámek–Koubek–Reiterman 1981; Husainov 2002): for each statement proved, say whether it is
in one of these, with theorem number, after opening the source.

Rules of proof, conventions and the form of the deliverables are those of the common block of the TOTASPH prompt
(variance: presheaves in the manuscript, covariant `H` for `El_A(H)`; "final" = all `b\A` non-empty connected;
every map typed; every counterexample complete and machine-checked; no authority, including this prompt's
"reviewer's computation" lines, which are to be re-proved).
