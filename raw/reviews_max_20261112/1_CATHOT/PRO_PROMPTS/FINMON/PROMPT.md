# FINMON: which homotopy types are classifying spaces of finite monoids and of finite categories

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for your deliverables: `FINMON`.
Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max); checked against the push standard
(`PUSH_STANDARD_AND_AUDIT_20261111.md`): every part asks for a proof, a refutation, a construction or a computation.

## What is to be settled

In *Les Dérivateurs* Grothendieck introduces the homotopy types of *finite* categories, "types d'homotopie de type
fini (ou de présentation finie?)" (V ms. 51–52), and tests everything on them (VII ms. 121–128, IX ms. 9–13, 23); in
the Appendix to XII (ms. 8–11) he writes down small categories of type S¹ and S². Which homotopy types these are is
not known. For one object the question is Fiedorowicz's (1984). O. Ben-Bassat, *On a Conjecture of Fiedorowicz*,
arXiv:2610.38760v1 (28 Oct 2026), proves that every finite simply connected CW complex is BM for a finite monoid M
(Theorem C) and conjectures:

> **Conjecture 7.1.** Let X be a connected finite CW complex. If π₁(X) is finite, then X ≃ BM for some finite monoid M.

Four claims about this are on the table. **Your task is to prove or refute each of them independently, and then to
carry the classification as far as it goes.** You are not asked for an opinion on the claims, on their wording or on
their plausibility; you are asked for proofs and counterexamples.

## The four claims (state each with all its data, then prove or refute it)

- **(b)** RP² is not homotopy equivalent to BM for any finite monoid M. (So Conjecture 7.1 is false as stated.)
- **(c)** If M is a finite monoid and BM has the homotopy type of a finite-dimensional CW complex, then the universal
  group U(M) = π₁(BM) is trivial.
- **(d)** A connected finite CW complex is homotopy equivalent to BM for some finite monoid M if and only if it is
  simply connected. (The "if" is Theorem C of the preprint: its proof is part of what you check.)
- **(g)** Small models. (g1) The category with objects 0, 1, 2, Hom(i, j) = Z/2 for i < j, no other non-identity
  arrows, composition by addition (3 objects, 9 arrows) has classifying space of type RP². (g2) Counting identity
  arrows, the least number of arrows of a category of type S¹, S², S³ is 4, 5, 7; for S¹ it is attained only by two
  parallel arrows; for S² only by the monoid P₂ = {1} ∪ {x_ij : i, j ∈ {0, 1}}, x_ij x_kl = x_il; for S³ every
  category with 7 arrows of that type is a monoid, one of them being P₃ = P₂ ∪ {q, r} with x_ij q = x_ij r = x_i0,
  q x_ij = r x_ij = x_ij, q² = qr = q, r² = rq = r. (g3) A finite category of type RP² has at least 3 objects and at
  least 9 arrows.

## Leads (unverified; prove or refute each; none is an authority)

- **Lead 1.** (c) follows from: the group H = eMe at an idempotent e of the minimal ideal of M surjects onto U(M);
  the map BH → BM through the Karoubi envelope realizes this surjection on π₁; and H. Miller, Ann. of Math. 120
  (1984), Theorem B (p. 40; proved as Theorem 10.1, pp. 84–85): a map from BG, G a torsion group, to a
  finite-dimensional CW complex is trivial on π₁. Check the statement and its hypotheses in the attached paper.
- **Lead 2.** The same step from Atiyah, Publ. Math. IHES 9 (1961), (6.10), (6.11), (7.2), (8.1), with no appeal to
  Miller.
- **Lead 3 (sharpening).** For a finite monoid M: "BM has the homotopy type of a finite complex", "of a
  finite-dimensional complex" and "H_k(M; Z) = 0 for all large k" are equivalent, and each forces U(M) = 1; if a
  prime p divides |U(M)|, then H_k(M; F_p) ≠ 0 for infinitely many k. Suggested route: the regular representation of
  U(M) as a flat bundle on BM and the skeletal filtration of K-theory.
- **Lead 4.** Counts to reproduce by your own program: 1, 2, 11, 156, 4,122, 208,672 monoid structures on
  {0, …, n−1} with identity 0 for n ≤ 6 (1, 2, 6, 27, 156, 1,373 classes up to isomorphism and anti-isomorphism);
  no monoid of order ≤ 6 and no category with at least two objects and at most 7 arrows has
  (H₁, H₂, H₃) = (0, 0, Z).
- **Lead 5.** A finite category with finite-dimensional classifying space has the homotopy type of a finite complex
  (Wall's obstruction vanishes): open; see Part D.

## WHAT THE OUTCOME MUST BE

1. **Deliverables.** One ZIP: `FINMON_paper.tex` and its PDF (LuaLaTeX, compiles cleanly); `FINMON_results.csv` with
   one row per numbered statement (`id, statement, status, where_proved, depends_on, manuscript_pages_settled,
   notes`); `FINMON_references.bib` (each entry marked `verified` = you opened it, or `unverified`);
   `FINMON_report.md`; `code/` with every program and its output.
2. **What counts as done, for each statement of Parts A–F and for each of (b), (c), (d), (g):** one of
   (a) proved, in its stated form or in its strongest correct form, with a complete proof in the paper;
   (b) refuted by a complete counterexample, checked by a program when finite, with the strongest true statement in
   its place, proved;
   (c) partly settled: the cases proved, the computations run, and the obstruction stated exactly, with the smallest
   undecided instance and what you tried.
   A statement labelled "Known" counts only together with the derivation from the cited theorem, with theorem
   number, and with every hypothesis checked against the case at hand.
3. **Not acceptable:** comments on, or assessments of, the claims instead of proofs; a survey or status report;
   "open, see [reference]"; a plan, a sample or an outline; a summary of what would be done; a statement dropped
   without a row; an exhaustive search whose scope is not stated exactly (orders, numbers of objects and arrows,
   whether up to isomorphism, which invariant excluded each candidate).
4. **When the work is finished:** only when every numbered item of the Parts meets the bar of 2. Anything short of
   it is reported in `FINMON_report.md` as unfinished, item by item.
5. **If the execution environment disconnects:** wait and retry for at least 10 minutes; if it does not come back,
   write every file out in the chat in full, each in its own code block headed by its file name, and continue the
   work in the chat. An answer that only reports the disconnection is not acceptable.

## Parts

**A. Claim (c) and its exact strength.** A1. Prove or refute (c), from the attached primary texts, with every step:
the minimal ideal, the group eMe, the surjection onto U(M), the typing of BH → BM, and the topological theorem with
its hypotheses checked. A2. Give a second complete proof of the topological step that does not use Miller's paper.
A3. Prove or refute each statement of Lead 3. If it is true, decide whether "integral homology bounded" can be
weakened to "H_k(M; F_p) = 0 for large k for one prime p" (conclusion: p ∤ |U(M)|) and to rational homology
(construct a finite monoid with U(M) ≠ 1 and H_k(M; Q) = 0 for k > 0, or prove there is none). A4. Search by
program for a counterexample to (c) and to Lead 3 among all monoids of order ≤ 7 (or as far as you get: state the
scope): for each monoid with U(M) ≠ 1 compute a projective resolution or the homology to the degree needed and
record the first degrees with non-zero homology. A5. State and prove the corresponding theorem for finite
categories with several objects (which subgroups of which endomorphism monoids must die in π₁, and what follows for
π₁(BC)); decide whether "finite-dimensional" can be replaced by "bounded integral homology" there.

**B. Claims (b), (d) and Theorem C of the preprint.** B1. Deduce (b) and the "only if" of (d). B2. Check the proof of
Theorems A, B, C of arXiv:2610.38760v1 line by line (Lemmas 2.1–2.6, 3.2, 3.6, Proposition 4.1, Lemma 4.2 in both
of its cases, Lemmas 5.1–5.4); for each step write "correct" with your own argument, or the exact gap with a repair
or a counterexample. B3. Implement Definition 3.3 and compute, by finite projective resolutions and not by a finite
range of the bar complex, the homology of M(Y, f) for: Example 3.2 with both labels; A₂, A₃; M(sk₂N(C₂), *);
M(Y_z, f_z) and M(Y_z, *) of Example 6.3; and one case of your choice with non-trivial holonomy in dimension 2.
B4. Decide whether the 1795-element and the 122-element monoids of type CP² are as claimed (recompute the Hopf
invariant). B5. Determine the least order of a finite monoid of type S² ∨ S², S⁴, CP², S² × S², M(Z/2, 2),
M(Z/3, 2): prove lower bounds by enumeration as far as feasible and upper bounds by explicit monoids with complete
resolutions. B6. Prove or refute: if BM has finite homotopy type, there is a finite aperiodic monoid M′ and a
zigzag of monoid homomorphisms between M and M′ inducing homotopy equivalences of classifying spaces.

**C. Claim (g): the small models.** C1. Prove (g1) (homeomorphism type, not only homology). C2. By your own
exhaustive enumeration (state the method, the counts for every (number of objects, number of arrows), and the
invariant that excludes each candidate) prove or refute (g2); list, up to isomorphism, all categories with 7 arrows
of type S³. C3. Prove or refute (g3) and list all categories of type RP² with 3 objects and 9 arrows. C4. Find the
least numbers of arrows of categories of type S⁴, S¹ × S¹, S¹ ∨ S¹, RP³, the lens space L(3, 1), CP²: lower bounds
proved, upper bounds by explicit categories verified by program. C5. For posets of type RP² the least number of
arrows (pairs x ≤ y) is at most 49 (the two 13-point models of Cianci–Ottina), and lower bounds 28 and 34 have
been claimed by degree counts in the comparability graph (unverified): determine the number, or prove the best
interval you can.

**D. Finite categories with finite-dimensional classifying space (Lead 5).** D1. Prove or refute: if C is a finite
category and BC has the homotopy type of a finite-dimensional CW complex, then BC has the homotopy type of a finite
CW complex. Reduce it to a statement about the class of the n-th syzygy of the constant ZC-module in
K₀(Z[π₁(BC)]) and decide that statement. D2. If you cannot decide it in general, decide it for categories whose
endomorphism monoids are groups, for categories with at most two objects, and for π₁(BC) of order 2, 23 and for
Q₈; a counterexample must be a finite category given by its composition table, with its finiteness obstruction
computed. D3. Determine all finite-dimensional homotopy types realized by finite categories with two objects.

**E. Infinite-dimensional types.** E1. Decide whether K(Z, 2) is BM for a finite monoid M, and whether it is BC for
a finite category C. Use the reformulation: BM ≃ K(Z, 2) iff U(M) = 1 and M ×_u Z has contractible classifying
space for some 2-cocycle u (prove it first). Prove that no regular finite monoid has infinitely many non-zero
rational Betti numbers, with the exact theorem used. E2. Decide the same for K(Z/2, 2), ΩS³, ΣCP^∞, ⋁_{n≥2} Sⁿ.
E3. Identify the homotopy type of BM for the six-element monoid of Sweeney's Example 5.2 (attached; H_k = Z for all
k ≥ 2): decide whether it is ⋁_{n≥2} Sⁿ; compute its cohomology ring and the Hurewicz image as far as needed.
E4. Decide whether [BC, S²] is countable for every finite category C. E5. For every monoid of order ≤ 6 with
homology in infinitely many degrees, identify the homotopy type or state exactly what is known of it.

**F. Back to the manuscript.** For each of V ms. 51–52 (Hot₀), VII ms. 121 (a finite category as a compact test),
VII ms. 128 (finiteness of the computation of the π_i), IX ms. 23 (the doubt about finite M), XII app. ms. 8–11
(the models of S¹ and S²): write the statement that is true, with its proof or its reference to Parts A–E, in the
form in which it can be entered at that page.

## Conventions

Categories are small; a finite category has finitely many arrows, identities counted; BC = |NC|; a monoid is a
one-object category and BM its classifying space; U(M) is the universal group. "Type X" means homotopy equivalent
to X. Homology is integral unless a coefficient is written. Keep apart: homeomorphic, homotopy equivalent, the same
homology in a range.

## What is attached

`Fiedorowicz2.tex` and the PDF (arXiv:2610.38760v1); Miller 1984 and its 1985 correction (author's page); Atiyah
1961 (Numdam); Sweeney, arXiv:2502.05276v2; Fiedorowicz 2002 (arXiv:math/0202260); Martinian–Steinberg,
arXiv:2511.12657v1; Carcacía-Campos, arXiv:2611.09718v1; Cianci–Ottina, arXiv:1512.06088v1; Barmak–Minian,
arXiv:math/0611156; Hatcher, *Algebraic Topology*; Quillen, *Higher algebraic K-theory I*; the transcription of
Grothendieck's text `DER_III-V_text.tex`, `DER_VII-c_text.tex`, `DER_VIII-X_text.tex`, `DER_XIIapp_text.tex`
(AI-made from the edition of Künzer, Malgoire and Maltsiniotis; where a formula looks wrong, say so and reason from
the mathematics). `MANIFEST` lists every file with its origin. (Local copies: `work/lit/` and `work/background/` of
`pro_reviews_max_20261112/1_CATHOT/`.)

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
5. No authority: the preprint, the four claims and the leads are all to be proved or refuted. If a lead is wrong,
   say so and show where.
6. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the
   smallest undecided instance. Never write it up as proved, and never drop it. Known and Open are not end points:
   a Known statement is derived from the cited theorem with the proof of the reduction; an Open statement records
   your own attack.
7. Before calling anything new, search the literature and say what you searched. Never invent a reference.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority. This task is long by design. Work through all parts completely; do not stop at an outline, a
sample or a plan, and do not ask whether to continue. Write the files from the start and extend them as you go.
