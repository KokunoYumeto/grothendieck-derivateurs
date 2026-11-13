# FINMON: which homotopy types are classifying spaces of finite monoids and of finite categories

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for your deliverables: `FINMON`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max, CATHOT expert); revised the same day by Claude Fable 5.2
(effort max, Dérivateurs expert) so that it starts from the results now in hand (the draft before this revision:
`PROMPT_before_results_20261112.md`). Checked against the push standard
(`PUSH_STANDARD_AND_AUDIT_20261111.md`): every part asks for a check of a written proof, a proof, a refutation, a
construction or a computation. The attached files are listed in `MANIFEST.tsv` at the root of
`FINMON_background.zip`.

## What is to be settled

In *Les Dérivateurs* Grothendieck introduces the homotopy types of *finite* categories, "types d'homotopie de type
fini (ou de présentation finie?)" (V ms. 51–52), and tests everything on them (VII ms. 121–128, IX ms. 9–13, 23); in
the Appendix to XII (ms. 8–11) he writes down small categories of type S¹ and S². Which homotopy types these are is
not known. For one object the question is Fiedorowicz's (1984). O. Ben-Bassat, *On a Conjecture of Fiedorowicz*,
arXiv:2610.38760v1 (28 Oct 2026), proves that every finite simply connected CW complex is BM for a finite monoid M
(Theorem C) and conjectures:

> **Conjecture 7.1.** Let X be a connected finite CW complex. If π₁(X) is finite, then X ≃ BM for some finite monoid M.

The conjecture is false, and more is known; the list follows. **Your task is to check the written proofs on that
list, and then to carry the classification past them: Parts A–F.** You are not asked for an opinion on the results,
on their wording or on their plausibility; you are asked for confirmations step by step, errors with repairs,
proofs and counterexamples.

## Results this prompt builds on (status on 12 Nov 2026)

"CATHOT" is a return of GPT-6 Astra (effort Pro, ChatGPT Pro mode). "CATHOT expert" and "Dérivateurs expert" are
two agents of Claude Fable 5.2 (Anthropic) at effort max; the second read the first's proofs
(`CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`): a second reading by the same model, not a confirmation by another
system or by a person. None of the results is an authority; none is to be proved again as if open. For each one
you use: read the proof at the place given and either confirm each step with your own argument, or give the
first wrong step with a repair or a counterexample.

- **R1 (CATHOT G.4; checked by Claude Fable 5.2 at effort medium on 11 Nov and at effort max on 12 Nov; complete
  proof in `G6_VERDICT.md`, five steps).** If M is a finite monoid and BM has the homotopy type of a
  finite-dimensional CW complex, then U(M) = π₁(BM) is trivial. Steps: π₁(BM) = U(M) and M → U(M) is onto; the
  group H = eMe at an idempotent e of the minimal ideal surjects onto U(M); the map BH → BM through the Karoubi
  envelope realizes this surjection on π₁; H. Miller, Ann. of Math. 120 (1984), Theorem B (p. 40; proved as
  Theorem 10.1, pp. 84–85): a map from BG, G a torsion group, to a finite-dimensional CW complex is trivial on π₁.
  A second proof of the last step, from Atiyah, Publ. Math. IHES 9 (1961), (6.11), (7.2), (8.1), with no appeal
  to Miller, is written out in the same file.
- **R2 (CATHOT G.6; same checks).** Hence Conjecture 7.1 is false as stated: RP², and every connected
  finite-dimensional complex with non-trivial fundamental group, is not BM for a finite monoid M. (Sent to the
  author of the preprint on 12 Nov 2026.)
- **R3 (CATHOT G.5, given Theorem C of the preprint).** A connected finite CW complex is BM for a finite monoid M
  iff it is simply connected. Status of Theorem C: claimed 2026, unrefereed; the CATHOT expert read its proof in
  full, re-derived Lemmas 2.4, 2.6, 3.2, 4.2 (one of its two cases), 5.2, 5.3, and ran five numerical tests of
  Theorem A (orders 7, 11, 11, 16, 22); no gap found; three results it cites were not opened (Jardine's simplicial
  approximation Cor. 4.8, Geoghegan's cell trading Prop. 4.2.1, Thomason's homotopy colimit theorem).
- **R4 (CATHOT expert; `OWN_RESULTS.md` Theorems 1.1, 1.2; read and found correct by the Dérivateurs expert, given
  Atiyah's statements as quoted).** A map BG → X, G finite, X connected with finite π₁ and H^q(X; Z) = 0 for
  q > n, is trivial on π₁ (Miller's Theorem B with "finite dimension" weakened to a cohomological bound);
  p-local form with Z_(p) coefficients: the image on π₁ has order prime to p.
- **R5 (CATHOT expert; `OWN_RESULTS.md` 2.1–2.5; read and found correct by the Dérivateurs expert).** For a finite
  monoid M: "BM has the homotopy type of a finite complex", "of a finite-dimensional complex" and
  "H_k(M; Z) = 0 for all large k" are equivalent, and each forces U(M) = 1; if a prime p divides |U(M)|, then
  H_k(M; F_p) ≠ 0 for infinitely many k (a Swan theorem for finite monoids); finite cohomological dimension forces
  U(M) = 1; with Theorem C, the homotopy types of finite monoids with bounded homology are exactly the finite
  simply connected complexes.
- **R6 (CATHOT G.11–G.13; re-proved by the CATHOT expert, `EMAIL_CLAIMS_CHECK.md` (g)).** The category R₂ with
  objects 0, 1, 2, Hom(i, j) = Z/2 for i < j, no other non-identity arrows, composition by addition (3 objects,
  9 arrows) has classifying space homeomorphic to RP²; a finite category of type RP² has at least 3 objects and
  at least 9 arrows.
- **R7 (CATHOT expert, by exhaustive enumeration with programs in the zip; `OWN_RESULTS.md` 6.1; not checked by a
  second party beyond 6 arrows, where the earlier review's independent enumeration agrees).** Counting identity
  arrows, the least number of arrows of a category of type S¹, S², S³ is 4, 5, 7; for S¹ only two parallel
  arrows; for S² only the monoid P₂ = {1} ∪ {x_ij : i, j ∈ {0, 1}}, x_ij x_kl = x_il; for S³ every such category
  is a monoid, one of them P₃ = P₂ ∪ {q, r} with x_ij q = x_ij r = x_i0, q x_ij = r x_ij = x_ij, q² = qr = q,
  r² = rq = r. Counts: 1, 2, 11, 156, 4,122, 208,672 monoid structures on {0, …, n−1} with identity 0 for n ≤ 6
  (1, 2, 6, 27, 156, 1,373 classes up to isomorphism and anti-isomorphism); the triples (H₁, H₂, H₃) that occur
  are listed in 6.1 (b), (c); no monoid of order ≤ 6 and no category with at least two objects and at most 7
  arrows has (0, 0, Z). Grothendieck's own S² model (the category Z of XII app. ms. 10–11) has 10 arrows.
  PRETOT A.14 and the review of PRETOT recount the labelled monoids with identity 0 for n ≤ 4 independently: 1, 2, 11, 156.
- **R8 (CATHOT expert; `OWN_RESULTS.md` 5.1; read and found correct by the Dérivateurs expert, given
  Cianci–Ottina, arXiv:1512.06088v1, Cor. 5.8 and Th. 5.10).** A poset of type RP² has at least 34 arrows (pairs
  x ≤ y); CATHOT G.8 had 28; the two 13-point models have 49.
- **R9 (CATHOT expert; `HUNCHES.md` H1, H2, H7: partial facts, not theorems).** (H1) For a finite category C with
  BC finitely dominated, every natural source of projective ZC-modules induces stably free modules over
  Z[π₁(BC)]; a dévissage is missing. (H2) BM ≃ K(Z, 2) iff U(M) = 1 and M ×_u Z has contractible classifying
  space for some 2-cocycle u (stated with a sketch); no monoid of order ≤ 6 has mod-p Betti numbers 0, 1, 0, 1, 0
  in degrees 1–5 (computed); for regular M the algebra QM has finite global dimension (Putcha 1998, quoted from
  memory, not opened). (H7) Theorem C gives an aperiodic M′ with BM′ ≃ BM, with no relation to M.
- **R10 (CATHOT expert; `OWN_RESULTS.md` 4.1, 4.2, read and found correct by the Dérivateurs expert; and
  computations).** If H¹(X; Z) = 0 and Sⁿ is a homotopy retract of X for infinitely many n with π_n(S³) ≠ 0, then
  [X, S²] is uncountable. For the six-element monoid of Sweeney's Example 5.2: U = 1, H_k = Z for k ≥ 2, S² is a
  retract of its classifying space, and the cup products x₂², x₂x₃, x₃x₂ vanish mod 2, 3, 32003.
- **R11 (Dérivateurs expert; `DERIVATEURS_FINDINGS.md` F-G4).** At XII app. ms. 15 Grothendieck's parenthesis
  "dans le cas où W ⊆ W₁, car π₁ ≅ Z" is wrong: the category in question is the Z of ms. 10–11, of type S² (his
  own footnote 7).

- **New since this prompt was drafted (12 Nov 2026): PRESHEAF_TOTALITY, reviewed.** Attached as `FINMON_new_results.zip`: the return PRESHEAF_TOTALITY (`PRETOT_return/`: paper, results, programs; GPT-6 Astra, ChatGPT Pro mode) and its review by Claude Opus 5.5 at effort max (`PRETOT_review/REVIEW.md`, `FINDINGS.md`). The review checked all 54 statements: none wrong; G.3 correct with a gap; A.12, D.4, E.1, F.14 and G.2 known; C.4, E.9, F.10 and F.16 open as stated. Theorem A.5 was recomputed independently: a 52-element act over `End_Δ([2])` whose element category is integrally acyclic with `π₁ ≅ SL(2,5)`, so total `W_ℤ`-asphericity does not imply total `W∞`-asphericity for presheaves. Checked since then (Claude Opus 5.5, effort max; `PRETOT_review/POINCARE_SPINE_CHECK.md`): the 2-complex of A.5 (`π₁ ≅ 2I`, `χ = 1`, presentation `⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩`) is homotopy equivalent to the Poincaré homology sphere `Σ(2,3,5)` minus an open ball, by Nicholson, arXiv:1905.12018, Theorem A, with `m_ℍ(2I) = 2`. F.3 and F.6: a sifted totally aspherical category is filtered, and abelian-group diagrams detect filteredness. Cite its statements by number where they bear here. The unreviewed return PATHS claims what F.16 leaves open: check it before relying on it.

## WHAT THE OUTCOME MUST BE

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

1. **Deliverables.** One ZIP: `FINMON_paper.tex` and its PDF (LuaLaTeX, compiles cleanly); `FINMON_results.csv` with
   one row per numbered statement (`id, statement, status, where_proved, depends_on, manuscript_pages_settled,
   notes`); `FINMON_references.bib` (each entry marked `verified` = you opened it, or `unverified`);
   `FINMON_report.md`; `code/` with every program and its output.
2. **What counts as done, for each numbered item of Parts A–F:** one of
   (a) proved, in its stated form or in its strongest correct form, with a complete proof in the paper;
   (b) refuted by a complete counterexample, checked by a program when finite, with the strongest true statement in
   its place, proved;
   Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack the obstruction, starting from that instance.
   An item that says "check" is done only as: every step of the written proof confirmed with your own argument
   (one paragraph per step in the paper), or the first wrong step with a repair or a counterexample.
   A statement labelled "Known" counts only together with the derivation from the cited theorem, with theorem
   number, and with every hypothesis checked against the case at hand.
3. **Not acceptable:** comments on, or assessments of, the results instead of step-by-step confirmations, proofs
   and counterexamples; proving R1–R8 again from nothing in place of the pushes; a survey or status report;
   "open, see [reference]"; a plan, a sample or an outline; a statement dropped without a row; an exhaustive
   search whose scope is not stated exactly (orders, numbers of objects and arrows, whether up to isomorphism,
   which invariant excluded each candidate).
4. **When the work is finished:** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `FINMON_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.
5. **If the execution environment disconnects:** wait and retry for at least 10 minutes; if it does not come back,
   write every file out in the chat in full, each in its own code block headed by its file name, and continue the
   work in the chat. An answer that only reports the disconnection is not acceptable.

## Parts

**A. The theorem on finite monoids (R1, R4, R5) and its exact strength.** A1. Check R1 in both forms (through
Miller's Theorem B, statement and hypotheses in the attached paper and its 1985 correction; and through Atiyah).
A2. Check R4 and R5 (the skeletal filtration of K-theory under a cohomological bound; the regular
representation; the p-local form). A3. Push past R5: (i) a Quillen-type detection theorem for finite monoids: prove or refute that a class x ∈ H*(M; F_p) of
positive degree is nilpotent iff its restriction along BG → BM (through the Karoubi envelope) is nilpotent for
every subgroup G of every group eMe, e an idempotent; then decide whether every class of positive degree in
H*(M; F_p) is nilpotent when U(M) = 1 (a positive answer excludes K(Z, 2) and K(Z/2, 2) in Part E; first test:
the six classes of monoids of order 6 with H₁ = 0 and H₂ ≠ 0 of `OWN_RESULTS.md` 6.1 (e)); (ii) decide whether U(M) = 1 follows from "H_k(M; Z) is finite for all large
k and of bounded exponent"; (iii) decide whether R4 holds with no condition on π₁(X) (the remark after Theorem 1.2
gives it for residually finite and for linear π₁). A4. Extend the census R7 by your own program to monoids of
order 7 with U(M) ≠ 1 (or as far as you get: state the scope): for each, a projective resolution or the homology
to the degree needed, and the first degrees with non-zero homology at each prime dividing |U(M)|. A5. State and
prove the theorem corresponding to R1 and R5 for finite categories with several objects (which subgroups of which
endomorphism monoids must die in π₁, and what follows for π₁(BC)); decide whether "finite-dimensional" can be
replaced by "bounded integral homology" there (R6 shows that π₁ need not be trivial).

**B. Theorem C of the preprint (R3).** B1. Complete the check of the proof of Theorems A, B, C of
arXiv:2610.38760v1: the steps not yet re-derived are Lemmas 2.1–2.3, 2.5, 3.6, Proposition 4.1, the second case
of Lemma 4.2, Lemmas 5.1, 5.4, and the three cited results named in R3 (state each with its hypotheses, from the
source). For each step write your own argument, or the exact gap with a repair or a counterexample. B2. Implement
Definition 3.3 and compute, by finite projective resolutions and not by a finite range of the bar complex, the
homology of M(Y, f) for: Example 3.2 with both labels; A₂, A₃; M(sk₂N(C₂), *); M(Y_z, f_z) and M(Y_z, *) of
Example 6.3; and one case of your choice with non-trivial holonomy in dimension 2. B3. Decide whether the
1795-element and the 122-element monoids of type CP² are as claimed (recompute the Hopf invariant). B4. Determine
the least order of a finite monoid of type S² ∨ S², S⁴, CP², S² × S², M(Z/2, 2), M(Z/3, 2): for each, prove a lower bound (by enumeration, which R7 has done up to order 6, and by structural arguments beyond it) and an upper bound by an explicit monoid with a complete resolution, until the two bounds meet. B5. Prove or refute (R9, H7): if BM has finite homotopy type, there is a finite aperiodic monoid M′
and a zigzag of monoid homomorphisms between M and M′ inducing homotopy equivalences of classifying spaces.

**C. The small models (R6, R7, R8).** C1. Reproduce R7 by an independent program (state the method, the counts
for every (number of objects, number of arrows), and the invariant that excludes each candidate); report every
disagreement with `OWN_RESULTS.md` 6.1. Then list, up to isomorphism, all categories with 7 arrows of type S³,
and all categories of type RP² with 3 objects and 9 arrows (R6). C2. Find the least numbers of arrows of
categories of type S⁴, S¹ × S¹, S¹ ∨ S¹, RP³, the lens space L(3, 1), CP²: lower bounds proved, upper bounds by
explicit categories verified by program. C3. Check R8; then determine the least number of arrows of a poset of
type RP², or prove the best interval inside [34, 49] you can.

**D. Finite categories with finite-dimensional classifying space (R9, H1).** D1. Prove or refute: if C is a finite
category and BC has the homotopy type of a finite-dimensional CW complex, then BC has the homotopy type of a finite
CW complex. Start from the reduction in `HUNCHES.md` H1: the obstruction is the class of the n-th syzygy of the
constant ZC-module in K̃₀(Z[π₁(BC)]); supply the missing dévissage or a counterexample. D2. Decide it in general; on the way, decide it for categories whose endomorphism monoids are groups, for categories with at most two
objects, and for π₁(BC) of order 2, 23 and for Q₈; a counterexample must be a finite category given by its
composition table, with its finiteness obstruction computed. A test case with finite perfect `π₁`: PRETOT A.3–A.5 give a finite category `M/H` (52 objects, 520 arrows; the degenerate 2-simplices have non-trivial endomorphism monoids containing idempotents) with `B(M/H)` homotopy equivalent to the acyclic 2-complex of `⟨a,b | a⁵b⁻³, b³(ab)⁻²⟩`, `π₁ ≅ SL(2,5)`; its finiteness obstruction vanishes. D3. Determine all finite-dimensional homotopy types
realized by finite categories with two objects.

**E. Infinite-dimensional types (R9, R10).** E1. Prove the reformulation of R9 (H2) for K(Z, 2); then decide
whether K(Z, 2) is BM for a finite monoid M, and whether it is BC for a finite category C; the search starts at
order 7. Prove that no regular finite monoid has infinitely many non-zero rational Betti numbers, with the exact
theorem used, opened. E2. Decide the same for K(Z/2, 2), ΩS³, ΣCP^∞, ⋁_{n≥2} Sⁿ. E3. Identify the homotopy type
of BM for the six-element monoid of Sweeney's Example 5.2, starting from R10: decide whether it is ⋁_{n≥2} Sⁿ
(is the generator of H₃ spherical?); compute its cohomology ring and the Hurewicz image as far as needed.
E4. Check Proposition 4.1 of `OWN_RESULTS.md` and decide whether [BC, S²] is countable for every finite
category C. E5. For every monoid of order ≤ 6 with homology in infinitely many degrees (R7 lists them by
(H₁, H₂, H₃)), identify the homotopy type or state exactly what is known of it.

**F. Back to the manuscript.** For each of V ms. 51–52 (Hot₀), VII ms. 121 (a finite category as a compact test),
VII ms. 128 (finiteness of the computation of the π_i), IX ms. 23 (the doubt about finite M), XII app. ms. 8–11
(the models of S¹ and S²; with R7) and XII app. ms. 15 (R11): write the statement that is true, with its proof or
its reference to R1–R11 and Parts A–E, in the form in which it can be entered at that page.

## Conventions

Categories are small; a finite category has finitely many arrows, identities counted; BC = |NC|; a monoid is a
one-object category and BM its classifying space; U(M) is the universal group. "Type X" means homotopy equivalent
to X. Homology is integral unless a coefficient is written. Keep apart: homeomorphic, homotopy equivalent, the same
homology in a range.

## What is attached

The files of `FINMON_background.zip`, listed with their origins in `MANIFEST.tsv` at its root: the notes named in
R1–R11 (`G6_VERDICT.md`, `EMAIL_CLAIMS_CHECK.md`, `OWN_RESULTS.md`, `HUNCHES.md`, `CATHOT_REVIEW.md`,
`CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`, `DERIVATEURS_FINDINGS.md`) and `CATHOT_FINDINGS.md` (the CATHOT expert's
running list of findings; G1–G5 concern the pages of Part F); the CATHOT paper, its Part G and its results table; the
programs and their outputs (census, mod-p homology, small models, projective resolutions, tests of Theorem A, cup
products); arXiv:2610.38760v1 (PDF and TeX source); Miller 1984 and its 1985 correction; Atiyah 1961; Sweeney,
arXiv:2502.05276v2; Fiedorowicz 2002 (arXiv:math/0202260); Martinian–Steinberg, arXiv:2511.12657v1; Carcacía-Campos,
arXiv:2611.09718v1; Cianci–Ottina, arXiv:1512.06088v1; Barmak–Minian, arXiv:math/0611156; Hatcher, *Algebraic
Topology*; Quillen, *Higher algebraic K-theory I*; Grothendieck's text `DER_III-V.tex`, `DER_VII-c.tex`,
`DER_VIII-X.tex`, `DER_XIIapp.tex` (the French transcription corrected on 11 Nov 2026; AI-made from the edition of
Künzer, Malgoire and Maltsiniotis; where a formula looks wrong, say so and reason from the mathematics). Not attached,
to be obtained by you and marked verified only if opened: Putcha 1998 (J. Algebra 205); Jardine, Geoghegan and
Thomason as cited in the preprint; Fiedorowicz 1984; McDuff 1979.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: which monoid or category, identity arrows counted or not, pointed or
   unpointed, homotopy equivalent or homeomorphic, which coefficients. If you prove a special case, name it as one
   and keep the general statement on your list.
2. Type every map: source, target, the category in which it is a morphism. A homomorphism eMe → M does not preserve
   the identity; say how the map of classifying spaces is defined.
3. Every reduction comes with its comparison map and a proof that the property needed transfers in the direction
   needed. Equal homology in a range is not a homotopy equivalence.
4. A counterexample is given completely (table, verification of every axiom and of the failure) and checked by a
   program whose code and output you attach. One verified counterexample refutes the statement: say "false". An
   invalid proof alone shows a gap, not falsity.
5. No authority: the preprint and the results R1–R11 are all to be checked where you use them. If one is wrong,
   say so and show where.
6. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the
   smallest undecided instance. Never write it up as proved, and never drop it. Known and Open are not end points:
   a Known statement is derived from the cited theorem with the proof of the reduction; an Open statement records
   your own attack.
7. Before calling anything new, search the literature and say what you searched. Never invent a reference.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority. This task is long by design. Work through all parts completely; do not stop at an outline, a
sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `<ID>_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
