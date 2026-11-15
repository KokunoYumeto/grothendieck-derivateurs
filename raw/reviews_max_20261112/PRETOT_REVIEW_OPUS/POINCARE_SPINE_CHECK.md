# P and the punctured Poincaré sphere

Check by Claude Opus 5.5 (effort max), 12 November 2026, 22:30 WEST, for the PRETOT review (FINDINGS F1).
No sub-agents.

**Question.** Is the presentation complex P of ⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩ (PRETOT Theorem A.5) homotopy
equivalent to Σ(2,3,5) minus an open ball, that is, to its 2-dimensional spine?

**Answer.** Yes. Let K be the 2-skeleton of Poincaré's dodecahedral cell structure on Σ = Σ(2,3,5); Σ minus an
open ball inside the 3-cell deformation retracts onto K. For any isomorphisms ρ_P : π₁(P) → 2I and
ρ_K : π₁(K) → 2I there is a homotopy equivalence h : P → K with ρ_K ∘ π₁(h) ∘ ρ_P⁻¹ = id (a polarised homotopy
equivalence). The proof is Nicholson's Theorem A, applied to two finite 2-complexes with fundamental group 2I and
Euler characteristic 1; its hypotheses hold for 2I (4-periodic cohomology, m_ℍ(2I) = 2). For 2I the cancellation
step inside the proof of Theorem A is Swan's Theorem I.

**What it settles.** F1 left "P ≃ punctured Poincaré sphere" unasserted because equal π₁ and χ do not decide the
homotopy type of a 2-complex in general. For fundamental group 2I they do: every finite 2-complex with π₁ ≅ 2I and
χ = 1 is homotopy equivalent to Σ minus a ball. Where PRETOT A.5 identifies the classifying space of its finite
category with P up to homotopy, that classifying space is therefore a punctured Poincaré sphere up to homotopy. The
general caveat of F1 stays correct: by the "only if" half of Theorem A, for groups with 4-periodic cohomology and
m_ℍ ≥ 3 the Euler characteristic does not determine finite D2 complexes up to polarised homotopy.

**Marks.** [S] verified by opening the source (place given). [C] verified by computation; scripts in
`scratch_poincare_spine/scripts`, outputs in `scratch_poincare_spine/out`, exact arithmetic unless stated.
[A] verified by the argument written here from [S] and [C] items. [NV] not verified. Statements from the sources are
restated in their own notation; direct quotation is limited to one short phrase.

## 1. Nicholson's theorem

Source: J. Nicholson, *On CW-complexes over groups with periodic cohomology*, arXiv:1905.12018v3 (10 May 2021),
local copy `user\Documents\research_maps_20261112\PRETOT_3D_MODULARITY\papers\arXiv_1905.12018.pdf`
(SHA-256 ee867c54…9298506a). The text layer drops symbols such as ≤ and the tildes of T̃, Õ, Ĩ, so the key
statements were read on rendered page images (`scratch_poincare_spine/img/p1_*.png`, `p2_top`, `p16_bp`, `p17_mH`,
`p20_thm7`).

- **Theorem A** (p. 1) [S]. Let G have 4-periodic cohomology. Then finite D2 complexes X with π₁(X) = G are
  "determined up to (polarised) homotopy by their Euler characteristic" if and only if m_ℍ(G) ≤ 2.
- **D_n complex** (p. 1, Wall's definition) [S]: a CW complex K with H_i(K̃) = 0 for i > n and H^{n+1}(K; M) = 0
  for every finitely generated ℤ[π₁(K)]-module M.
- **Polarisation** (p. 2) [S]: each X carries an isomorphism ρ_X : π₁(X) → G; a homotopy equivalence h : X → Y is
  polarised if ρ_Y ∘ π₁(h) ∘ ρ_X⁻¹ = id_G. A polarised homotopy equivalence is in particular a homotopy equivalence.
- **m_ℍ(G)** (p. 1) [S]: the number of copies of ℍ in the Wedderburn decomposition of ℝG. These are the factors
  M₁(ℍ) = ℍ; factors M_n(ℍ) with n ≥ 2 do not count. The paper's own values (p. 17: m_ℍ(T̃) = 1, m_ℍ(Õ) = 2,
  m_ℍ(Ĩ) = 2; pp. 2 and 17: m_ℍ(Q₄ₙ) = ⌊n/2⌋, whose floor brackets the text layer drops and m_ℍ(Q₂₈) = 3 in
  Theorem 8.11 confirms) fit this reading and not a count of all quaternionic factors, which would give 4 for Ĩ
  (§2.3) [S, C].
- **n-periodic cohomology** (§6, p. 16) [S]: the Tate groups Ĥ^i(G; ℤ) are periodic of period n. In §3 the paper
  quotes Swan [Sw60b, Thm 4.1]: G has n-periodic cohomology if and only if there is an exact sequence
  0 → ℤ → P_{n−1} → ⋯ → P₀ → ℤ → 0 with the P_i projective; G has free period n when the P_i can be taken free
  [S for the quotation; Swan 1960 itself not opened, NV].
- **Euler characteristic and grading** (§1.1) [S]: D2(G), the set of polarised homotopy types of finite D2 complexes
  with π₁ = G, is a graph graded by χ(X), with an edge from X to X ∨ S².
- **(G, n)-complexes.** The term does not occur in the paper. The polarised finite 2-complexes form the subgraph
  PHT(G, 2) ⊆ D2(G) (§2) [S]. Every finite 2-complex is a finite D2 complex: its universal cover has no cells above
  dimension 2, and it has no 3-cochains [A].
- **Cancellation** (§1.2) [S]: for a projective ℤG-module P, [P] is the set of nonzero projectives stably
  isomorphic to P, graded by rank; [P] has cancellation if P₁ ⊕ ℤG ≅ P₂ ⊕ ℤG implies P₁ ≅ P₂ for P₁, P₂ ∈ [P].
  Cancellation leaves one module in each rank: two members of equal rank become isomorphic after adding the same
  free module, and the copies of ℤG cancel one at a time [A].
- **How Theorem A is proved** (pp. 3–4 and §7) [S for the statements; proofs NV]. Theorem 2.1: D2(G) ≅ Alg(G, 2) as
  graded trees, for every finitely presented G. Theorem 4.1: for G with 4-periodic cohomology, Alg(G, 2) ≅ [P_G] as
  graded trees, for any P_G with σ₄(G) = [P_G] ∈ C(ℤG)/T_G (Swan finiteness obstruction). Theorem 7.2: for such G,
  [P_G] has cancellation if and only if m_ℍ(G) ≤ 2. With cancellation, D2(G) has one vertex in each grade, which is
  the conclusion of Theorem A.
- **The case G = Ĩ.** Nicholson's Theorem 7.5 (p. 20) [S] quotes Swan [Sw83, Theorem I]. Opened in the original:
  R. G. Swan, *Projective modules over binary polyhedral groups*, J. reine angew. Math. 342 (1983), 66–172; Theorem I
  is on p. 66 (GDZ scan https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0342/00000070; page image in
  `scratch_poincare_spine/downloads/swan_1983_gdz_img/`) [S]. For a binary polyhedral group G, cancellation holds for
  ℤG if and only if G is one of Q₈, Q₁₂, Q₁₆, Q₂₀, T̃, Õ, Ĩ. Swan's "cancellation holds for R" means R ⊕ P ≅ R ⊕ Q
  implies P ≅ Q for all finitely generated projective P, Q (same page) [S]. That is cancellation in every stable
  class, so [P_G] has cancellation for G = Ĩ whatever σ₄(Ĩ) is [A]. Swan's proof was not checked [NV].
- Inputs to the proofs of Theorems 2.1 and 4.1, not opened [NV]: Johnson [Jo03a] (LMS Lecture Note Series 301) and
  [Jo03b]; Browning [Br78] (unpublished; the paper cites [Ham19, Cor. 2.6] for another proof); Swan [Sw60a].

## 2. The hypotheses for 2I

### 2.1 The group

- [C] `char_table_2I.py`: coset enumeration (sympy 1.13.1) gives |⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩| = 120. The 120 icosians
  (±1, ±i, ±j, ±k, ½(±1 ± i ± j ± k), and the even permutations of ½(0, ±1, ±φ⁻¹, ±φ), with φ = (1+√5)/2) are unit
  quaternions closed under multiplication. q_a = (1+√5)/4 + ((√5−1)/4)i + ½j and q_b = ½(1 + i + j + k) satisfy
  q_a⁵ = q_b³ = (q_a q_b)² = −1 and generate all 120. So a ↦ q_a, b ↦ q_b is a surjection between groups of order
  120, hence an isomorphism from π₁(P) onto the icosian group G. This agrees with F1.
- [C] `icosian_is_I120.py`: the rotations v ↦ g v g⁻¹ (g ∈ G, v pure imaginary) preserve the regular dodecahedron
  with vertices (±1, ±1, ±1), (0, ±φ, ±φ⁻¹), (±φ⁻¹, 0, ±φ), (±φ, ±φ⁻¹, 0), and they are 60 distinct rotations. The
  rotation group of a regular dodecahedron has order 60 (Hatcher, *Algebraic Topology*, Example 2.38, p. 142) [S],
  so G, of order 120, is the full preimage in S³ of that rotation group: Hatcher's binary icosahedral group I₁₂₀
  (§1.3, p. 75) [S]. Kirby–Scharlemann (p. 116) call the group ⟨x, y | x³ = y⁵ = (yx)²⟩ the binary icosahedral
  group I* [S]. Nicholson's Ĩ is the binary icosahedral group among the finite non-cyclic subgroups of S³ (p. 16) [S].
  Below, 2I means G.

### 2.2 4-periodic cohomology

- [A] A subgroup of S³ acts freely on S³ by left multiplication (Hatcher §1.3, p. 75) [S]. A free action of a finite
  group on a Hausdorff space is a covering space action (Hatcher §1.3, Exercise 23, stated as an exercise) [S], so
  S³ → S³/2I is a covering with deck group 2I (Hatcher Prop. 1.40) [S]. Kirby–Scharlemann identify S³/I* with the
  dodecahedral space (§3) [S, proof NV]; 2I and I* are preimages of rotation groups of regular dodecahedra centred at
  0, hence conjugate in S³, and conjugate subgroups have homeomorphic quotients [A]. So S³/2I has a finite CW
  structure. Lifting its cells to S³ gives a finite CW structure whose cells 2I permutes freely [standard, NV], and the
  cellular chain complex gives an exact sequence 0 → ℤ → C₃ → C₂ → C₁ → C₀ → ℤ → 0 with the C_i free ℤ[2I]-modules of
  finite rank. The left ℤ is H₃(S³) with trivial action: left multiplication by g is homotopic to the identity along
  a path from 1 to g in S³. By Swan's criterion as quoted in Nicholson §3, 2I has 4-periodic cohomology, with free
  period 4.
- Cross-checks. Nicholson's list of the groups with 4-periodic cohomology (§6, p. 18, Milnor's notation) contains Ĩ
  in family (iii) [S]. [C] The element orders of 2I are 1, 2, 3, 4, 5, 6, 10 (with 1, 1, 20, 30, 24, 20, 24 elements)
  and −1 is the only involution, so the Sylow subgroups are Q₈, C₃ and C₅, as Nicholson's Theorem 6.1 ([CE56,
  Thm 11.6] as quoted) requires for periodic cohomology [S for the quotation; that a non-cyclic group of order 8 with
  one involution is Q₈ is standard, NV].

### 2.3 m_ℍ(2I) = 2

[C] `char_table_2I.py`, exact in ℚ(√5). The characters are χ_{k+1}(g) = U_k(Re g) for k = 0, …, 5 (the symmetric
powers Sym^k V of the natural representation V on ℂ² = ℍ; U_k is the Chebyshev polynomial of the second kind), the
Galois conjugates χ₂′, χ₃′ of χ₂, χ₃ (√5 ↦ −√5), and χ₄′ = χ₂χ₂′. With τ = (1+√5)/2:

| size | order | Re g | χ₁ | χ₂ | χ₃ | χ₄ | χ₅ | χ₆ | χ₂′ | χ₃′ | χ₄′ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 2 | 3 | 4 |
| 1 | 2 | −1 | 1 | −2 | 3 | −4 | 5 | −6 | −2 | 3 | 4 |
| 20 | 3 | −1/2 | 1 | −1 | 0 | 1 | −1 | 0 | −1 | 0 | 1 |
| 30 | 4 | 0 | 1 | 0 | −1 | 0 | 1 | 0 | 0 | −1 | 0 |
| 12 | 5 | (√5−1)/4 | 1 | τ−1 | 1−τ | −1 | 0 | 1 | −τ | τ | −1 |
| 12 | 5 | −(√5+1)/4 | 1 | −τ | τ | −1 | 0 | 1 | τ−1 | 1−τ | −1 |
| 20 | 6 | 1/2 | 1 | 1 | 0 | −1 | −1 | 0 | 1 | 0 | 1 |
| 12 | 10 | (1+√5)/4 | 1 | τ | τ | 1 | 0 | −1 | 1−τ | 1−τ | −1 |
| 12 | 10 | (1−√5)/4 | 1 | 1−τ | 1−τ | 1 | 0 | −1 | τ | τ | −1 |

- The Gram matrix of the nine characters is the identity (exact) and 2I has nine conjugacy classes, so this is the
  complete character table; degrees 1, 2, 3, 4, 5, 6, 2, 3, 4, with squares summing to 120 [C].
- Frobenius–Schur indicators ν(χ) = (1/120) Σ_g χ(g²): ν = +1 for χ₁, χ₃, χ₅, χ₃′, χ₄′ and ν = −1 for χ₂, χ₄, χ₆,
  χ₂′; none has ν = 0 [C]. The quaternionic characters are exactly the four on which −1 acts as −1 [C].
- With the standard dictionary (ν = +1, degree d ↦ M_d(ℝ); ν = −1, degree 2d ↦ M_d(ℍ)):
  ℝ[2I] ≅ ℝ × M₃(ℝ) × M₃(ℝ) × M₄(ℝ) × M₅(ℝ) × ℍ × ℍ × M₂(ℍ) × M₃(ℍ), of total dimension 120. The quaternionic
  factors of degree 2 are those of χ₂ and χ₂′, so m_ℍ(2I) = 2 [C; the Frobenius–Schur theorem and the dictionary are
  standard and were not opened, NV].
- Cross-check that uses neither [C, A]. The inclusion ι : G → ℍ and σ∘ι, where σ applies √5 ↦ −√5 to the coordinates
  (a ring automorphism of the quaternions over ℚ(√5)), are injective homomorphisms into the unit quaternions
  (σ(G) checked: 120 unit elements, closed under multiplication), and both images contain 1, i, j, k. They extend to
  surjective ℝ-algebra maps ℝ[G] → ℍ. A surjection from a product of simple algebras onto ℍ factors through the
  projection onto one factor, which is then ≅ ℍ. If both maps used the same factor they would differ by an
  automorphism of ℍ, and automorphisms of ℍ preserve real parts (Im ℍ = {q : q² ∈ ℝ, q² ≤ 0}); but
  Re ι(q_a) = (1+√5)/4 ≠ (1−√5)/4 = Re σι(q_a). So m_ℍ(2I) ≥ 2. Conversely ℂ[G] = ℝ[G] ⊗_ℝ ℂ and
  ℍ ⊗_ℝ ℂ ≅ M₂(ℂ), so each factor ℍ gives its own irreducible complex character of degree 2; there are exactly two.
  So m_ℍ(2I) ≤ 2.
- Nicholson (p. 17) states m_ℍ(Ĩ) = 2, from tables of real representations, without proof [S]. The computation agrees.

### 2.4 Nothing else is required

Theorem A asks only that G have 4-periodic cohomology and that m_ℍ(G) ≤ 2; the objects compared are finite D2
complexes with fundamental group G [S, p. 1]. 2I is finite and both complexes are finite 2-complexes (§1, §3).

## 3. The spine of Σ minus a ball

Source: R. Kirby and M. Scharlemann, *Eight faces of the Poincaré homology 3-sphere*, in *Geometric Topology*
(Athens, GA, 1977), Academic Press 1979, pp. 113–146. Scan from https://web.math.ucsb.edu/~mgscharl/papers/Poincare.pdf,
copy `scratch_poincare_spine/downloads/kirby_scharlemann/Poincare_ucsb.pdf` (SHA-256 41ab5348…605196ff), read as page
images (`img/ks-*.png`).

- p. 113 [S]: eight descriptions of the Poincaré homology sphere, among them (3) the link of z₁² + z₂³ + z₃⁵ = 0,
  that is Σ(2,3,5), (4) S³/I*, and (5) the dodecahedral space; the paper shows they define the same 3-manifold
  [the proofs: NV].
- p. 117, Description 5 [S]: each face of a regular dodecahedron is identified with the opposite face by pushing it
  through the solid and twisting it by 2π/10 about the axis of the push, in the sense of a right-hand screw; the
  quotient is a 3-manifold, the same as in the other descriptions.
- p. 116 [S]: from the surgery description, π₁ = ⟨a, g | a⁵ = g³ = (ag)²⟩, which is the presentation of P. This
  presentation comes from a 4-dimensional handle picture, not from a spine of Σ, so on its own it does not make P a
  spine; Theorem A closes that gap.
- [A] The quotient D is a CW complex with one 3-cell, the open solid, attached to K = (boundary of the
  dodecahedron)/(face pairings). The pairings send vertices to vertices and edges to edges [C]. Radial projection from
  the centre deforms the dodecahedron minus a small open ball about the centre onto its boundary and fixes the boundary
  pointwise, so it passes to the quotient: Σ minus that open ball deformation retracts onto K.
- [C] `dodecahedral_spine.py` builds the pairings of Description 5 (floating-point geometry, used only to match
  vertices) and finds 5 vertex classes of 4 vertices each, 10 edge classes and 6 faces, so χ(K) = 5 − 10 + 6 = 1. The
  cellular presentation (spanning tree of 4 edges, one relator per face) has 6 generators and 6 relators; coset
  enumeration gives order 120, and the abelianisation matrix has determinant 1. Tietze eliminations
  (x₆ = x₇ = x₅x₈, x₉ = x₅⁻¹, x₄ = x₈x₅) leave the group ⟨s, t | sts⁻¹tst⁻¹, s⁻¹t⁻¹s⁻¹ts²t⟩, of order 120;
  `spine_group_iso.py` finds images of s and t in the icosian group that satisfy both relators and generate it.
  So π₁(K) ≅ 2I.
- [A] χ(K) = 1 also follows from χ(Σ) = 0, since Σ = K ∪ e³.
- So K is a (2I, 2)-complex, a finite connected 2-complex with π₁ ≅ 2I, with χ = 1, and it is homotopy equivalent to
  Σ minus a ball. This is the standard spine from Poincaré's dodecahedral description; no Heegaard splitting is
  needed. The ball is taken inside the 3-cell; that the complement of a tame ball does not depend on the ball is
  standard [NV].

## 4. Conclusion

[A] P and K are finite connected 2-complexes, hence finite D2 complexes (§1), with π₁ ≅ 2I (§2.1, §3) and χ = 1
(P: 1 − 2 + 2; K: 5 − 10 + 6). 2I has 4-periodic cohomology (§2.2) and m_ℍ(2I) = 2 ≤ 2 (§2.3). By Theorem A, for any
choice of polarisations (P, ρ_P) and (K, ρ_K) are polarised homotopy equivalent. Hence P ≃ K ≃ Σ(2,3,5) minus an
open ball. The same argument shows that every finite D2 complex with π₁ ≅ 2I and χ = 1 has this homotopy type.

Not addressed: whether P and K are simple-homotopy equivalent, and whether the two presentations are related by
Andrews–Curtis moves.

## 5. Not verified

- The proofs of Nicholson's Theorems 2.1, 4.1 and 7.2 and their inputs (Johnson [Jo03a, Jo03b], Browning [Br78],
  Swan [Sw60a, Sw60b]); the statements were opened.
- The proof of Swan's Theorem I; the statement was opened.
- Kirby–Scharlemann's proofs that the eight descriptions agree, in particular that the dodecahedral space is a
  3-manifold homeomorphic to Σ(2,3,5) and to S³/I*; the statements were opened.
- The Frobenius–Schur theorem and the dictionary between indicators and Wedderburn factors (standard).
  m_ℍ(2I) = 2 does not depend on them (cross-check in §2.3).
- Standard topology used in §2.2 and §3: cells of a CW complex lift to a covering space; Q₈ is the only non-cyclic
  group of order 8 with a single involution; tame balls in a 3-manifold are unique up to isotopy.
- The identification of P with the realisation of the finite category in PRETOT A.5 (the return's comparison lemma,
  reproduced by the review, F21); not rechecked here.

## Files

- Scripts: `scratch_poincare_spine/scripts/char_table_2I.py`, `icosian_is_I120.py`, `dodecahedral_spine.py`,
  `spine_group_iso.py` (run with `python -I -B`, Python 3.13.9, sympy 1.13.1).
- Outputs: `scratch_poincare_spine/out/*.out`.
- Source text and page images: `scratch_poincare_spine/text/`, `scratch_poincare_spine/img/`; downloads in
  `scratch_poincare_spine/downloads/` (Kirby–Scharlemann scan; Swan 1983 p. 66, OCR text and page image from GDZ).
