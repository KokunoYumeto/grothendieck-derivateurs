# TRIAGE: PRETOT Theorem A.5 against the Ẑ / 3d modularity / umbral moonshine programme

Written 2026-11-12 21:40 WEST by Claude (Fable 5.2, effort high), as step 0 before any full map.

## Verdict

**Not worth mapping in full. No note to the Ẑ researchers.**
The intersection is the group 2I and the Poincaré sphere, and nothing more: no transfer of method, and no
invariant on the category side that can see Ẑ or the false/mock distinction. One small remark is worth keeping
for the PRETOT companion (link 1 below); it is a remark about the counterexample, not about Ẑ.

## What this rests on

Read: PRETOT_paper.pdf pp. 4-7 (Construction A.3, Lemma A.4, Theorem A.5 with proof) and the head of the PRETOT
README. Nothing else.

Not read: every paper of the programme. Each statement about the programme below is **from memory and
unverified**; none carries a section number, because I opened none of them. Six arXiv PDFs were downloaded to
`papers\` before the order changed and are unopened: 1809.10148 (3d Modularity), 1701.06567
(Gukov-Pei-Putrov-Vafa), 1307.5793 (Cheng-Duncan-Harvey, Niemeier lattices), 1503.01472 (Duncan-Griffin-Ono),
1412.8191 (Duncan-Harvey, E8³), 1905.12018 (Nicholson). The Lawrence-Zagier download failed (404 at the MPIM
address) and the error page was removed.

## The sketch: what a link would have to look like

**What (a) is.** A finite category M/H (52 objects, 520 arrows) whose classifying space is homotopy equivalent
to the presentation complex P of ⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩. The proof uses three properties of P: it is a finite
2-complex, it is acyclic (det ∂₂ = −1), and π₁(P) ≠ 1 (a surjection onto A₅). It does not use which perfect
group appears. P is Hatcher's textbook acyclic complex (Example 2.38, cited by the return). Any finite acyclic
2-complex with nontrivial π₁ would give the same theorem by the same construction. So 2I enters (a) through the
choice of example, not through the mathematics of total asphericity.

**What (b) uses.** Ẑ_a(M; q) is an invariant of a closed *oriented* 3-manifold M with a spin^c-type label a,
computed from a negative definite plumbing graph. For Σ(2,3,5) that graph is the E8 tree, eight vertices. From
memory: for Σ(2,3,5) the result is a false theta function whose radial limits give the WRT invariants
(Lawrence-Zagier); for −Σ(2,3,5) the 3d Modularity paper relates it to Ramanujan's order-5 mock theta function
χ₀; and the E8³ case of umbral moonshine (lambency 30+6,10,15) has, as I recall, H₁ = q^(−1/120)(2χ₀(q) − 4)
and H₇ = 2q^(71/120)χ₁(q). The task said to check that last point and not assume it; it is **not checked**.

**Where the two could meet, and why they do not.**

1. *The space.* P and the punctured Poincaré sphere Σ° are both finite 2-complexes (Σ° up to homotopy, via a
   spine) with π₁ ≅ 2I and Euler characteristic 1. Whether P ≃ Σ° is a question in the homotopy classification
   of 2-complexes. From memory, Nicholson (arXiv:1905.12018) proves that for a group G with 4-periodic
   cohomology, finite 2-complexes with π₁ ≅ G are determined up to homotopy by their Euler characteristic if
   and only if G has at most two one-dimensional quaternionic representations. By my count 2I has exactly two
   (the two Galois-conjugate 2-dimensional representations; the 4- and 6-dimensional ones give M₂(ℍ) and
   M₃(ℍ)). That would give P ≃ Σ°. **Status: unknown to me until that theorem statement and the count are
   checked**; this is a recollection, not a reference I opened. It also needs π₁(P) ≅ 2I, which the reviewer is
   verifying.
   Even if true, this tells the Ẑ researchers nothing: they have Σ(2,3,5) itself.

2. *Orientation.* Σ(2,3,5) and −Σ(2,3,5) are the same topological space with two orientations, so they have the
   same punctured space and the same spine. Every invariant of the homotopy type of B(M/H) therefore takes the
   same value on both. The false/mock distinction is exactly the distinction between the two orientations.
   **So no invariant of the finite category that factors through its classifying space can see it.** This is a
   proof and needs no reading. The category side has no substitute: B(C) and B(C^op) are homeomorphic, and the
   orientation of Σ is the sign of the fundamental class, which lives on the 3-cell that P does not have.

3. *What the category can see.* Only what factors through π₁ = 2I: the set of flat connections (for SL(2,ℂ),
   the trivial one and two irreducible ones) and counts of homomorphisms to finite groups (untwisted
   Dijkgraaf-Witten). It cannot see their Chern-Simons values (from memory −1/120 and −49/120 mod 1; these
   change sign with orientation), nor WRT, nor Ẑ, all of which need the fundamental class.

4. *Method transfer.* (a)'s method realizes a finite 2-complex as the element category of a finite act over
   End_Δ([2]). Speculation: with a 3-cell added and End_Δ([3]) one would get a finite category modelling
   Σ(2,3,5) itself. The programme has no use for it: finite combinatorial models of Σ(2,3,5) already exist
   (triangulations, whose face posets are finite categories; the E8 plumbing graph, which is what Ẑ is computed
   from), and Ẑ is not defined from a triangulation or a category. I know of no state-sum formula for Ẑ. The
   state-sum invariant that is defined from spines, Turaev-Viro, equals |WRT|² and is blind to orientation.

5. *Umbral moonshine.* The link E8³ ↔ χ₀, χ₁ ↔ −Σ(2,3,5), if it holds as I recall, runs through the E8 root
   system, i.e. through McKay's correspondence for 2I. That is a link between 2I and the programme. It passes
   through nothing in (a): the category M/H knows 2I only as a fundamental group.

## How interesting, and why

Not interesting for the programme. The shared objects are real (the group, the presentation, the manifold), but
(a) reaches them by picking the standard textbook acyclic complex, and the one structure the programme's results
turn on, the orientation, is provably invisible on the category side (point 2). Because the sketch came out this
way, I did no targeted reading, as instructed.

## The one thing worth keeping

For the PRETOT companion, not for a note to anyone: the remark "the classifying space of M/H is homotopy
equivalent to the punctured Poincaré homology sphere", if point 1 checks out. Cost to check: the statement of
Nicholson's main theorem and the list of groups it covers, plus Hatcher Example 2.38 for the group; about 10k
tokens. It makes the counterexample easier to describe; it is not a new result.

## What the full map would cost

About 50-60k tokens of reading: 3d Modularity (introduction and the Σ(2,3,5) section, ~25k), Cheng-Duncan-Harvey
on the E8³ mock thetas (~5k), Lawrence-Zagier (~10k, and a working source for the PDF), Nicholson (~8k),
Hatcher p. 142 (~2k). Expected outcome: the same verdict, with section numbers attached.
