# MAP: PRETOT Theorem A.5 ↔ Ẑ invariants, 3d modularity, umbral moonshine, Leech, the Albert algebra

Written 2026-11-12 22:27 WEST by Claude (Fable 5.2, effort high). TRIAGE.md in this folder was a sketch from
memory and is superseded.

**Purpose.** A map along which a future result on either side can be carried to the other: each link is an
exact statement with its number, an exact construction, and the scope of what is proved. Papers were not read
end to end; each statement used was located in the source and read with its hypotheses.

**Flags.** **[opened]** = I read the statement in the source. **[fetched]** = statement numbers reported by a
fetch tool from the paper's HTML or abstract page. **[memory]** = not checked against a source.
**Speculation** is marked. Status of a link: **checked**, **fails** (with proof and scope), or **open** (with
what a check takes).

## 0. Sources

PDFs in `papers\`.

| Short | Reference | Statements read |
|---|---|---|
| PRETOT | PRETOT_paper.pdf (GPT-6 Astra, ChatGPT Pro mode, 12 Nov 2026) | Thm A.2, Constr. A.3, Lemma A.4, Thm A.5, with proofs |
| LZ | Lawrence, Zagier, Asian J. Math. 3 (1999) 93-108 | §1; §3 (11), Thm 1-2; §5 (19); §6 Thm 3 |
| GPPV | Gukov, Pei, Putrov, Vafa, arXiv:1701.06567v2 | abstract; §2.4; fn. 20 (2.34); (3.142)-(3.146), Remarks; App. C (C.1)-(C.2) |
| 3dM | Cheng, Chun, Ferrari, Gukov, Harrison, *3d Modularity*, arXiv:1809.10148v2 | (1.1)-(1.3); §2 intro; (4.29)-(4.33); Table 3; (6.2)-(6.3), fn. 18; §6.6 Table 12, (6.72); §7 intro; (7.16)-(7.18); §7.5 Table 13; §9 |
| 3dMR | Cheng, Coman, Kucharski, Passaro, Sgroi, *3d Modularity Revisited*, arXiv:2403.14920v3 (Nov 2025) | abstract; (1.5), Conj. 1; §3.2; §5.3.1 (5.8)-(5.12); §6 |
| HJNP | Harichurn, Jagadale, Noshchenko, Passaro, arXiv:2508.10087v3, SIGMA 22 (2026) 090 | abstract; §1; Thm 1.2; Table 1 |
| CDH | Cheng, Duncan, Harvey, *Umbral Moonshine and the Niemeier Lattices*, arXiv:1307.5793 | §1; §2.2 end; §2.4; §2.5 Table 4; (4.12); (5.54)-(5.55) |
| DH | Duncan, Harvey, arXiv:1412.8191 | (1.2)-(1.3); Thm 1.2 |
| DGO | Duncan, Griffin, Ono, arXiv:1503.01472v2 | Thm 1.1; §1 |
| OS | Ozsváth, Szabó, *Absolutely graded Floer homologies and intersection forms for four-manifolds with boundary*, arXiv:math/0110170 | Thm 1.2, 1.3, 1.10, 1.11; Prop. 4.2 (9); §8.1 |
| Wilson | R. A. Wilson, *Octonions and the Leech lattice*, J. Algebra 322 (2009) 2186-2190, author version | §1, §2 opening, §3 definition |
| S6-W | the user's workbench, `math\research\s6_recent_results_main\canonical_S6_snapshot\supporting_materials\workbench\research\es_niemeier_wilson_cyclic.tex` | (wcl:eq:Wilson-definition), Thm wcl:thm:Leech, Thm wcl:thm:fixed-coinvariant |
| S6-F | `workbench_review_20261112\FINDINGS.md` | F31, F32, the "Interest 2" list |
| AJK | Akhmechet, Johnson, Krushkal, arXiv:2109.14139, J. reine angew. Math. 796 (2023) | §3.2, Def. 3.4-3.5, Thm 1.1, 1.2, 3.1, Rem. 3.3 **[fetched]** |
| CS22 | Cheng, Sgroi, *Cone vertex algebras, mock theta functions, and umbral moonshine modules*, arXiv:2203.03052 | abstract **[fetched]** |
| CCPS | Cheng, Coman, Passaro, Sgroi, *Quantum modular Ẑ^G-invariants*, SIGMA 20 (2024) 018, arXiv:2304.03934 | abstract **[fetched]** |
| GPP | Gukov, Park, Putrov, *Cobordism invariants from BPS q-series*, arXiv:2009.11874 | abstract **[fetched]** |
| Carrega | arXiv:1510.08687 | abstract **[fetched]** |

Not read: Nicholson, arXiv:1905.12018 (an Opus agent is checking it; its file
`derivateurs_companion_20261109\pro_reviews_max_20261112\PRETOT_REVIEW_OPUS\POINCARE_SPINE_CHECK.md` did not
exist at the time of writing). Not found free: Elkies, Gross, *The exceptional cone and the Leech lattice*,
IMRN 1996 no. 14, 665-698 (citation confirmed from Wilson's reference [13] and a web search; text not opened).
The board card `braindump_board\cards\moonshine-exceptional-series.md` was read first.

## 1. The main line

Albert algebra → Leech lattice → umbral moonshine → 3d modularity → Ramanujan's mock thetas → Σ(2,3,5) and
2I → PRETOT's category. One row per link.

| # | Link | Statement as found | Where | Status |
|---|---|---|---|---|
| L1a | octonions → Leech | The Leech lattice is the set of triples (x, y, z) of octonions with x, y, z ∈ L, the pair sums in Ls̄, x+y+z ∈ Ls, norm ½(xx̄+yȳ+zz̄); L is a copy of E8 in the Coxeter-Dickson integral octonions. "A 3-dimensional octonionic Leech lattice." | Wilson §3 **[opened]**; the same definition, with the bars, in S6-W (wcl:eq:Wilson-definition) **[opened]** | checked |
| L1b | the same, proved in the user's workbench | Λ_W "is an even unimodular rank-24 lattice of minimum norm 4"; under the cyclic permutation of the three octonion coordinates the fixed lattice has Gram matrix 3·G₈ and the coinvariant lattice is A₂ ⊗ E8, both of determinant 3⁸ | S6-W, Thm wcl:thm:Leech, Thm wcl:thm:fixed-coinvariant **[opened]** | checked (in the workbench, with its program) |
| L1c | Albert algebra → Leech | "In the Albert algebra c_W is realized by conjugation with the real permutation matrix for (1 3 2)": the three octonion coordinates are the off-diagonal entries of a 3×3 Hermitian octonionic matrix | S6-W, text before Thm wcl:thm:fixed-coinvariant **[opened]** | checked for the cyclic symmetry only |
| L1d | Albert algebra → Leech, Elkies-Gross | An integral structure on the exceptional Jordan algebra over the integral octonions, giving the Leech lattice | Elkies-Gross 1996 **[not opened]**; a search snippet of their 2001 Duke paper says the 1996 paper "described an integral structure (J, E)" on the algebra | open: obtain the paper; then compare its lattice with Wilson's conditions in L1a |
| L2a | Leech → the Niemeier family | "The Leech lattice is the unique even, unimodular and positive-definite lattice of rank 24 with no root vectors … while the other 23 … all have root systems of the full rank 24", labelled by root systems with one Coxeter number | CDH §1 **[opened]** | checked |
| L2b | Niemeier family → umbral moonshine | "This relation associates one case of umbral moonshine to each of the 23 Niemeier lattices" | CDH §1 **[opened]** | checked |
| L2c | how Leech sits over the 23 | Deep holes of the Leech lattice correspond to Niemeier root systems, "and all Niemeier root systems arise in this way"; "from each Niemeier lattice one can obtain a different 'holy' construction of the Leech lattice"; the umbral groups relate to "the stabilisers of deep holes in the Leech lattice" (Glauberman); the Frame shapes of the cases are Frame shapes of elements of Co₀ = Aut(Leech) | CDH §2.2 end, §2.4, acknowledgments **[opened]** | checked as statements; the deep-hole sentence was read in part |
| L2d | Leech itself → Conway and Monster moonshine | Aut(Leech) is the double cover of Co₁, which "plays a crucial role in the construction of the Monster" | Wilson §1 **[opened]** | checked as far as stated; "Leech carries Conway moonshine" **[memory]** |
| L3a | umbral E8³ → Ramanujan | For lambency 30+6,10,15: H_{1A,1} = q^(−1/120)(2χ₀(q) − 4), H_{1A,7} = 2q^(71/120)χ₁(q), with χ₀ = Σ qⁿ/(q^(n+1);q)_n, χ₁ = Σ qⁿ/(q^(n+1);q)_(n+1) | CDH (5.54)-(5.55); proved in DH Thm 1.2 with (1.2); module: DGO Thm 1.1 **[opened]** | checked (theorem) |
| L3b | umbral E8³ → 3d modularity, false side | The shadow S^{E8}_r = S_{30,1}+S_{30,11}+S_{30,19}+S_{30,29}; the false theta θ̃_{30,1}+θ̃_{30,11}+θ̃_{30,19}+θ̃_{30,29} "plays the role of homological blocks for Σ(2,3,5)"; both carry the label 30+6,10,15 | CDH (4.12); 3dM (7.16), Table 3, Table 13 **[opened]** | checked |
| L3c | umbral E8³ → 3d modularity, mock side | Ẑ(−Σ(2,3,5)) ≃ H₁^{30+6,10,15} ≃ χ₀ and the defect invariant ≃ χ₁, "assuming Conjecture 3 is correct"; the general statement is the false-mock Conjecture 1 | 3dM (7.17)-(7.18), §7 intro ("we propose"); 3dMR §3.2, (5.12), Conj. 1 **[opened]** | open on the Ẑ side: Ẑ is "rigorously defined for negative definite plumbed 3-manifolds" only, and the two proposals for the other orientation "are incompatible in general" (HJNP abstract, Thm 1.2) |
| L3d | same authors | M. Cheng is an author of CDH, 3dM, 3dMR, CS22, CCPS | author lists **[opened]** | checked |
| L4a | Ramanujan → Σ(2,3,5) | The radial limit of 1 − A(q)/2 at a root of unity is the WRT invariant of Σ(2,3,5); Ramanujan's fifth-order Φ(q) at 1/q is expressed by A₊, A₋ with A₊+A₋ = A (Zwegers) | LZ Thm 1; §5 (19) **[opened]** | checked (theorem); LZ do not read 1/q as orientation reversal |
| L4b | Σ(2,3,5) → 2I | Σ(2,3,5) is "the quotient of S³ by the icosahedral group" | LZ §1 p. 95 **[opened]** | checked |
| L4c | 2I → PRETOT | B(M/H) ≃ P, the presentation complex of ⟨a, b ∣ a⁵b⁻³, b³(ab)⁻²⟩; P is acyclic; π₁(P) maps onto A₅ | PRETOT Lemma A.4, Thm A.5 **[opened]** | checked up to π₁ ≠ 1; π₁ ≅ 2I is ours, under review |
| L4d | P → Σ(2,3,5) minus a ball | homotopy equivalence | none | open: **unknown to me**; with the Opus agent |

A second route from 2I to Leech, found in Wilson §1 **[opened]**: "a 3-dimensional quaternionic version, known
as the icosian Leech lattice … based on the ring of icosians discovered by Hamilton, which is an algebra whose
norm 1 elements form a copy of the H₄ root system". The 120 unit icosians form the group 2I **[memory]**. So
the fundamental group of PRETOT's complex generates a ring over which the Leech lattice is a rank-3 module,
parallel to Wilson's rank 3 over the octonions. Status: open; Wilson's references [15, 1] not opened.

## 2. The chirality tower ("D+1")

Three stages. For each: how it is reached from PRETOT, and what carries the orientation.

### Stage 1, dimension 2: the 2-complex P and the category M/H

- *Reached:* it is PRETOT's object.
- *Orientation:* none. **Fails**, with proof: Σ(2,3,5) and −Σ(2,3,5) are one space with two orientations, so
  they have one punctured space; P is acyclic, so no constant-coefficient homology class exists on it; and
  B(C) ≅ B(C^op). *Scope:* invariants of the homotopy type of B(M/H), and homology of P. Nothing is said here
  about stages 2 and 3.

### Stage 2, dimension 3: Σ(2,3,5) with its 3-cell and fundamental class

- *Reached:* by PRETOT's construction one dimension up. The proof of Lemma A.4 uses i_n : [n] → [2],
  r_n : [2] → [n], r_n(j) = min(j, n), r_n i_n = id, and the epi-mono factorization in Δ; all exist with 3 in
  place of 2. So for a finite 3-dimensional semisimplicial model K of Σ(2,3,5), the act K₃ over End_Δ([3])
  (35 elements) has element category weakly equivalent to Σ(2,3,5). **Checked** by inspection of the proof;
  not run. **Open:** a small model and its counts (a triangulation and a script, 15-20k tokens).
- *Orientation is carried by* a generator of H₃ ≅ ℤ. What then distinguishes the two generators:

| Invariant | Value on Σ(2,3,5), as the boundary of the negative definite E8 plumbing | Under reversal | Source | Computable from (category, generator)? |
|---|---|---|---|---|
| Chern-Simons values of the two non-abelian flat connections | −1/120, −49/120 mod 1 | sign change; HJNP Table 1 lists [49/120], [1/120] | 3dM Table 12, (6.72), Table 13 **[opened]**, my arithmetic | Speculation: yes, from π₁ and the fundamental class by group cohomology of 2I **[memory]**. Open: do it. |
| Casson invariant λ | −1 | sign change **[memory]** | OS Thm 1.3 (normalization) **[opened]** | open |
| Heegaard Floer correction term d | 2 | d(−Σ(2,3,5)) = −2; d(Y) = −d(−Y) | OS §8.1; Prop. 4.2 (9) **[opened]** | Open: Heegaard Floer homology is defined from a Heegaard diagram, so through a Heegaard structure on P (5.2 ii) |
| Frøyshov's h | not read | sign change **[memory]** | OS call their Thm 1.11 "an analogue of a theorem of Frøyshov" **[opened]**; Frøyshov's paper not opened | open |
| Rokhlin μ = σ/8 mod 2 | 1 **[memory]** | none: μ takes values in ℤ/2, and −1 = 1 | **[memory]** | μ does not point in a direction. It records that the filling has signature ±8. *Scope:* this is a remark on μ only. |
| WRT | W(ξ) of LZ | WRT(M; k) = WRT(−M; −k) | 3dMR (1.5) **[opened]** | through a state sum, see 5.3 |

- *The programme at this stage:* GPPV fn. 20, (2.34): Ẑ_a(q) ↔ Ẑ_a(q⁻¹) under reversal, and the index I(q),
  "unlike Ẑ_a(q), is insensitive to the orientation" **[opened]**. AJK Thm 3.1 and Rem. 3.3 relate lattice
  cohomology to HF⁺(−Y) and to d-invariants **[fetched]**; GPP derive homology-cobordism invariants from the
  q-series **[fetched]**. So Ẑ and d already meet in the literature, on negative definite plumbings.

### Stage 3, dimension 4: the filling, where the false/mock data are defined

- *The statement:* Ẑ is computed from a plumbing tree Γ with matrix M, as a principal-value integral with
  factor (z_v − 1/z_v)^(2 − deg v) against the theta function of the lattice (ℤ^L, −M); "well-defined only if M
  is negative definite, i.e. M₃(Γ) is a link of a normal singularity, with Γ being a resolution graph".
  GPPV (3.145)-(3.146), Remark 2 **[opened]**. For Σ(2,3,5): the −E8 plumbing, 3dM fn. 18 **[opened]**. The
  lattice in the formula is H₂ of the 4-dimensional filling.
- *Why it points one way.* **Checked**, one step from memory: −Σ(2,3,5) bounds no negative definite smooth
  4-manifold. Proof: OS Thm 1.11 gives ξ² + rk H² ≤ 4d(Y) for every characteristic vector ξ of a negative
  definite X bounding Y; with Y = −Σ(2,3,5), d = −2 (OS §8.1), so ξ² + rk ≤ −8 for all characteristic ξ; but
  every negative definite unimodular form of rank n has a characteristic vector with ξ² ≥ −n (Elkies
  **[memory]**). For Σ(2,3,5) itself and the E8 filling the inequality is an equality: 0 + 8 = 4·2.
  The programme says the same in its own terms: "the orientation reversal operation does not preserve the
  weakly negative property of the plumbing graph" (3dMR §1, after (1.5)) **[opened]**.
- *Consequence for the pair.* The false side is the side with a definite filling: its Ẑ is an Eichler
  integral of a theta function of a definite lattice (3dM (7.16)). The other side has no such filling, and
  its proposed Ẑ is written with "indefinite lattice theta functions" (3dMR §5.3.1, Conj. 5) **[opened]**.
  So the false/mock split is the definite/indefinite split of the available 4-dimensional fillings. This is
  the precise form of "the Poincaré sphere points in one direction".
- *Reached from PRETOT:* not through P. The spine of the plumbing is one 2-sphere per vertex of the E8 tree,
  meeting according to the edges **[memory, standard]**: simply connected, H₂ = ℤ⁸, while P is acyclic with
  π₁ = 2I. The two meet only through Σ = boundary of the plumbing and P ~ Σ minus a ball. The algebraic way
  from the category to the E8 tree is McKay (5.5). **Open:** a finite category for the plumbing spine with
  the weights as added structure (5.4).
- *Anomaly inflow in the programme's words:* "anomalies … require 2d degrees of freedom to be present on the
  boundary in order to compensate the anomaly of a 3d bulk theory" (3dM §2 intro) **[opened]**; Ẑ is "the
  half-index of the three-dimensional theory … obtained by compactifying the M5 brane theory on the closed
  three-manifold" (3dMR abstract) **[opened]**; the system is "a 6d fivebrane theory on M₃ times a 2-disk"
  (GPPV abstract) **[opened]**. The 2+1-dimensional E8 phase (K-matrix the E8 Cartan matrix, chiral central
  charge 8, boundary character E₄/η⁸ = j^(1/3)) is **[memory]**; no statement read links it to the plumbing
  lattice of Ẑ. **Open**, speculation: the −E8 plumbing lattice of stage 3 and the K-matrix lattice of the E8
  phase are the same lattice, and θ_{E8} = E₄ would be the common theta function.

## 3. Further statements used below

**F1.** PRETOT Thm A.2 **[opened]**: a simplicial set K is totally W_ℤ-aspherical iff |K| is acyclic iff K is
connected, nonempty and ℤ[K] is projective; it is totally W_∞-aspherical iff |K| is weakly contractible.

**F2.** 3dM (1.1)-(1.3) **[opened]**: Ẑ is labelled by Tor H₁(M, ℤ)/ℤ₂ (abelian flat connections), "written
here for G = SU(2)"; the S-matrix "only depends on basic topological invariants … such as H₁(M₃, ℤ)" with its
linking form. §6.6: for integral homology spheres "there is only one q-series invariant", and the
representation on abelian flat connections is trivial. (4.30), (4.33): the Chern-Simons values of non-abelian
flat connections are read from the modular data.

**F3.** GPPV §2.4 **[opened]**: an approach by triangulations is "especially attractive due to its
combinatorial nature"; making it see reducible flat connections "has not been done and presents a nice and
tractable problem for future work" (2017). App. C (C.1)-(C.2): TV(M) = |Z_CS(M)|², and for homology spheres
TV(M, q) = Ẑ₀(M, q)Ẑ₀(M, q⁻¹) = the index of T[M].

**F4.** CDH §2.5 **[opened]**: McKay's correspondence "relates finite subgroups of SU(2) to the extended Dynkin
diagrams of ADE type by associating irreducible representations of the finite groups to nodes", explained "in
terms of resolutions of simple singularities ℂ²/G". Table 4: X = A₂¹², A₃⁸, A₄⁶, A₅⁴D₄, … at ℓ = 3, 4, 5, 6, …;
at ℓ = 3 the umbral group is 2.M₁₂, the SU(2) subgroup is 2.Alt₅, the diagram is extended E8. The umbral
group of E8³ is Sym₃ (§2.4 table; DH (1.3)).

**F5.** 3dM §9 **[opened]**: "One natural question is whether there is a relation between our setup and the
moonshine finite groups." 3dMR §6 **[opened]**: all statements "should have counterparts for other ADE gauge
groups different from SU(2)"; "it would be very illuminating to have a map going directly from the VOA
relevant for M₃ to the VOA relevant for −M₃".

**F6.** AJK §3.2, Def. 3.4-3.5 **[fetched]**: a weight function χ_k on ℤ^s is extended to the cubes of ℝ^s; S_j
is the subcomplex with χ_k ≤ j; the graded root has the connected components of the S_j as vertices and
inclusions as edges. Thm 1.1: with Laurent-polynomial weights it is an invariant of the plumbed 3-manifold
with spin^c structure. Thm 1.2: a two-variable series equal to Ẑ at t = 1. Negative definite plumbings only.

**F7.** S6-F, F32 **[opened]**: in the user's workbench, three Leech neighbours of N(A₅⁴D₄) are cycled by an
order-3 Weyl element; their common sublattice J has determinant 81; a reader found J has exactly eight
unimodular overlattices, six Leech and two A₂¹². Status there: proved in the workbench and recomputed;
novelty not established.

## 4. The dictionary: PRETOT's objects and their counterparts

| PRETOT object | Counterpart | Construction joining them | Status |
|---|---|---|---|
| The category M/H (52 objects, 520 arrows) | The homotopy type of Σ(2,3,5) minus a ball; the flat bundles on Σ(2,3,5) | Classifying space and π₁; or directly: functors M/H → Vect inverting every arrow are the representations of π₁ | **checked:** Lemma A.4, Thm A.5. **open:** L4c, L4d |
| The act H over End_Δ([2]) | A presentation of the manifold of triangulation type. The programme's presentations that carry Ẑ are plumbing trees up to Kirby moves (GPPV Remark 3) and surgery, Σ(2,3,5) = S³₋₁(left-handed trefoil) (3dMR (5.8)) | H is a 2-truncated simplicial set with its degeneracies (Constr. A.3) | **checked** that Ẑ has no triangulation formula in GPPV (F3). **open:** whether one has appeared since; Park arXiv:2106.03942, Gukov-Manolescu arXiv:1904.06057 |
| P and π₁ = 2I | (a) the two non-abelian flat connections = the two components χ₀, χ₁ | non-trivial homomorphisms 2I → SU(2) up to conjugacy: two **[memory]** | **checked** on the programme's side three ways: 3dM Table 12 (count 2); Table 13, σ = {1, 7}; DGO §1, I^X = {1, 7}. **fails:** the Chern-Simons values are not functions of π₁ (they change sign with orientation). **open:** which representation is r = 1 and which r = 7 |
| | (b) the E8 tree | McKay (5.5) | see 5.5 |
| | (c) the Leech lattice | the icosian ring (§1, last paragraph) | open |
| Acyclicity of P | Σ(2,3,5) is an integral homology sphere: one label a = 0, trivial S-matrix | F2 | checked |
| Total W_ℤ- versus W_∞-asphericity | Abelian versus non-abelian flat connections | F1 and F2: W_ℤ sees what H₁ sees, which fixes the labels and the S-matrix; W_∞ sees π₁, where the q-series content lives | **checked:** by F1 every punctured Brieskorn sphere of 3dM Table 12, triangulated, is totally W_ℤ-aspherical and not totally W_∞-aspherical; the compression to a finite monoid act uses only finiteness and dimension 2. **fails:** "the proofs single out 2I" (they use acyclicity, det ∂₂ = −1, a map onto A₅). **checked, one step from memory:** 2I is the smallest finite group possible: π₁ of an acyclic space is perfect with H₂(π₁) = 0 (Hopf), and the only perfect group of order < 120 is A₅, with H₂ = ℤ/2 **[memory]** |
| Grothendieck's setting: a test category and a localizer | A kind of presentation, moves, and a function invariant under the moves: plumbing trees with Kirby/Neumann moves (GPPV Remark 3; AJK Thm 1.1) | a presheaf is a presentation; the localizer says which presentations are the same | **checked:** Ẑ is proved invariant by moves ("A priori this is not obvious", GPPV Remark 3). **fails:** Ẑ does not factor through the W_∞-localization of presheaves modelling the punctured manifold (stage 1). **open:** AJK's sublevel sets S_j (F6) are cubical complexes, so small categories up to homotopy, and the graded root is the diagram j ↦ π₀(S_j); this is where homotopy types of small categories already enter the construction of Ẑ. To check in AJK §§3-5, 7: whether the weights are functions of the diagram j ↦ S_j alone (20k tokens) |

## 5. Bridges and constructions that could carry more

### 5.1 A 3-cell and End_Δ([3])

Stage 2 of §2. Checked by inspection; a model is open.

### 5.2 Structure on a category that carries an orientation

- **(i) A fundamental class** on a 3-dimensional model: §2, stage 2.
- **(ii) A Heegaard structure on P.** Open. If ⟨a, b ∣ a⁵b⁻³, b³(ab)⁻²⟩ comes from a genus-2 Heegaard diagram
  of Σ(2,3,5), then P is an embedded spine and the cyclic order in which the relator curves meet the
  meridians determines the oriented manifold; the mirror diagram gives −Σ. That order is combinatorial data
  addable to the cell structure behind M/H, and Heegaard Floer invariants (d of stage 2) are defined from
  such a diagram. To check: planarity of the Whitehead graph of the two relators, or Kirby-Scharlemann,
  *Eight faces of the Poincaré homology 3-sphere* **[memory]**; 10-15k tokens.
- **(iii) Weights or gleams** on the 4-dimensional spine: 5.3, 5.4.

### 5.3 State sums from spines or categories

- **Checked:** F3 (C.2): an unoriented state sum (Turaev-Viro) gives Ẑ₀(q)Ẑ₀(q⁻¹), the product of the two
  sides at roots of unity, and not each factor.
- **Checked at abstract level:** Turaev's shadow formula computes the SU(2) invariant of a closed oriented
  3-manifold from a shadow (Carrega **[fetched]**), a 2-polyhedron with half-integer gleams **[search
  snippet]**: an orientation-sensitive state sum on a decorated 2-complex.
- **Fails:** Turaev-Viro on B(M/H). The state sum needs a triangulation or a special spine **[search
  snippet; Turaev-Viro 1992 not opened]**, which is more than a homotopy type. *Scope:* the homotopy type;
  the embedded case is 5.2 (ii).
- **Open:** with a special spine, Turaev-Viro at small levels against LZ's table of W(ξ) (LZ §2) would test
  (C.2) on Σ(2,3,5); 20-40k tokens and code. A state sum for Ẑ itself: F3.

### 5.4 Plumbing graphs as categories

- **Checked:** the input of Ẑ is a tree with integer weights, i.e. the lattice (ℤ^L, M) with its tree
  structure (GPPV (3.142)-(3.146)); H₁ = Coker M with linking form (a, M⁻¹b) (GPPV (3.143)-(3.144)).
- **Fails:** the homotopy type of the plumbing spine determines Ẑ. Proof: it is a wedge of L 2-spheres for
  every tree with L vertices and all weights, and Ẑ depends on M. *Scope:* the spine without its weights.
- **Open, speculation:** PRETOT's construction applied to the plumbing spine gives a finite category fibred
  over the face poset of the E8 tree; the weights would be a bilinear form on its H₂. AJK's sublevel sets
  (F6) are the existing construction closest to this.

### 5.5 McKay and E8

The chain: M/H → π₁ = 2I → the irreducible representations of 2I and tensoring with a faithful
2-dimensional one → the extended E8 diagram → drop the trivial node, weight −2 on each vertex → the −E8
plumbing tree → Ẑ by GPPV (3.145) → the false theta of 3dM (7.16).

- **Checked:** F4 (McKay, resolutions of ℂ²/G; 2.Alt₅ ↔ extended E8); GPPV Remark 2 (Γ is the resolution graph
  of the singularity whose link is M₃); 3dM fn. 18; 3dM (7.16). The first arrows are algebraic and start from
  the category (§4, row 1), so the E8 tree is computable from M/H without a 3-manifold in between.
- **Where the orientation enters:** at the sign of the weights, after leaving the category. This agrees with
  stage 1 and stage 3.
- **Fails:** "2I is the umbral group of the case carrying χ₀, χ₁". The E8³ umbral group is Sym₃; 2.Alt₅ is
  attached to ℓ = 3, X = A₂¹² (F4). *Scope:* the umbral groups as CDH define them.
- **Checked, the user's research:** by F7 the lattice J of the user's workbench has two overlattices of type
  A₂¹², the ℓ = 3 Niemeier lattice, whose SU(2) subgroup in CDH Table 4 is 2.Alt₅ = 2I with diagram E8; the
  user's marked lattice N(A₅⁴D₄) is the ℓ = 6 entry of the same table. So the user's Niemeier work and
  PRETOT's group meet in CDH Table 4.
- **[memory], not checked:** McKay's observation on the Monster's 2A involutions and the extended E8 diagram;
  θ_{E8} = E₄; j = E₄³/Δ, where E₄³ is the theta function of the lattice E8³ (it has 3·240 = 720 roots, the
  coefficient of q in E₄³); j^(1/3) = E₄/η⁸. If these hold as recalled, the lattice E8³ carries both the
  J-function (theta function over Δ) and the fifth-order mock thetas (its umbral form, L3a).
- **Open:** F5's question. For E8³ the finite groups in play are Sym₃ and 2I. Also open: whether DH's vertex
  algebra for E8³ is the cone vertex algebra that 3dMR attaches to −Σ(2,3,5). CS22 gives cone vertex algebra
  modules for lambencies 8, 12, 16 **[fetched]**, not 30+6,10,15. To check: DH §2 against 3dMR §4; 15k tokens.

### 5.6 Deligne's exceptional series

- **From the card:** dim g = 2(h∨+1)(5h∨−6)/(h∨+6), eight members A₁ … E8 (Deligne 1996; not opened). My
  arithmetic: h∨ = 2 gives 3; h∨ = 30 gives 248.
- **Checked:** in the programme the two ends of the series appear in different roles. The gauge group is
  G = SU(2), type A₁ (3dM (1.1): "written here for G = SU(2)"); E8 enters as the geometry of the manifold
  (plumbing tree, McKay). So "E8" in Ẑ(Σ(2,3,5)) is not the gauge group.
- **Checked at abstract level:** the gauge group is a parameter the programme varies: CCPS treat SU(3) and
  prove a conjecture for integral homology spheres **[fetched]**; 3dMR §6 asks for all ADE groups (F5).
- **Open:** Ẑ^G(Σ(2,3,5)) for G along the series, and whether its data depend on G through h∨ alone, which is
  what "dimension as a parameter" would mean here. No statement read addresses it.

### 5.7 Octonions

- **Checked:** the Coxeter-Dickson integral octonions are "an algebra whose norm 1 elements form a copy of the
  E8" root system (Wilson §1-2), and they give the Leech lattice in rank 3 (L1a). The quaternionic Leech lattice has symmetry a double cover of G₂(4)
  (Wilson §1) **[opened]**.
- **[memory]:** G₂ = Aut 𝕆; G₂ as the stabilizer of a generic 3-form on ℝ⁷; the associator 3-form; the magic
  square; S⁶ = G₂/SU(3).
- **Open:** a statement joining G₂ or the 3-form to Ẑ or to PRETOT. None was found in what was read. The
  nearest checked facts are L1a-L1c.

### 5.8 The user's S6 research

Statements located (the two preprints named on the card input the workbench modules):

- L1b, L1c (Wilson's Leech lattice in the triality space; the Albert-algebra realization of the cycle; the
  coinvariant lattice A₂ ⊗ E8).
- F7 (the lattice J; six Leech and two A₂¹² overlattices).
- `niemeier_umbral_shadow.tex`: the umbral shadow of X = A₅⁴D₄ after CDH, "a direct coefficient map from the
  actual shadow matrix" to a Fricke-type function **[section headings and two lines opened]**.
- S6-F, "Interest 2" list: "The isometry N ⊗ ℝ → 𝕆³ is a choice … so ℤ/12 is not an invariant" **[opened]**.
- `koide_arithmetic_preprint.tex`: no occurrence of E8, Leech, Niemeier, icosahedral, G₂, octonion (searched).
  S6-F F31 calls the Koide count a "side lane; no mathematical link" to the S6 object.

Where they attach to this map: at L1 (Albert, octonions → Leech), at L2 (Leech neighbours of a Niemeier
lattice), and at CDH Table 4 (5.5). **Open:** the E8³ analogue of the user's shadow computation for A₅⁴D₄;
it would place the shadow of L3b in the user's own framework.

## 6. Transport: what moves along which link

- **A result on fundamental localizers between W_∞ and W_ℤ** moves along §4 (asphericity row) to a statement
  about which flat connections an invariant of that strength can see on a homology sphere. Speculation: a
  localizer sensitive to local systems in a fixed group would detect exactly the two connections of L3.
- **A rigorous definition of Ẑ for positive definite plumbings** (the open side of L3c) moves along stage 3 →
  stage 2 to a requirement on any oriented category model of Σ(2,3,5): its invariants at the generator −[Σ]
  must reproduce χ₀, χ₁ data, starting with the Chern-Simons values.
- **A triangulation or state-sum definition of Ẑ** (F3) moves to a function on finite acts over End_Δ([3])
  with a chosen generator of H₃ (5.1), invariant under the corresponding moves.
- **A vertex algebra map between the M₃ and −M₃ sides** (F5) moves along L3 to a relation between DH's E8³
  module and the logarithmic algebra of 3dM Table 3 for Σ(2,3,5).
- **A result on the Leech lattice over the octonions or the icosians** (L1, §1 last paragraph) moves along L2
  only through the deep-hole correspondence L2c; for E8³ that is the deep hole of type E8³.
- **From PRETOT outward:** Theorem A.2 gives, for every integral homology sphere in the programme's tables,
  a finite monoid act that separates W_ℤ from W_∞. Any invariant the programme defines combinatorially on
  such acts would be an invariant strictly finer than total W_ℤ-asphericity.

## 7. For the PRETOT companion

With their flags: every punctured integral homology 3-sphere with π₁ ≠ 1 is a counterexample by Theorem A.2
(§4); 2I is the smallest finite fundamental group such a counterexample can have (§4, one step from memory);
the E8 diagram is computable from M/H through McKay (5.5); the identification of B(M/H) with the punctured
Poincaré sphere awaits the Nicholson check (L4d).

## 8. Open items, in order of cost

1. L4c, L4d: the group and the homotopy type (in progress elsewhere).
2. Stage 2: the Chern-Simons values from (π₁, fundamental class) for 2I. Small computation.
3. 5.2 (ii): is the presentation geometric. 10-15k tokens.
4. 5.5: DH's vertex algebra against 3dMR's cone vertex algebra for −Σ(2,3,5). 15k tokens.
5. 5.1: an explicit act over End_Δ([3]). 15-20k tokens and a script.
6. §4 last row: AJK's weights as functions of a diagram of categories. 20k tokens.
7. F3: a state-sum definition of Ẑ since 2017. 20k tokens.
8. L1d: Elkies-Gross, once a copy is at hand. §1 last paragraph: the icosian Leech lattice (Wilson's [15, 1]).
9. 5.6, 5.7: no statement found yet; these need a first source before they can be costed.

## Update, 12 November 2026 (main session, Claude Opus 5.5)

L4c and L4d are checked: `derivateurs_companion_20261109\pro_reviews_max_20261112\PRETOT_REVIEW_OPUS\POINCARE_SPINE_CHECK.md`
(Claude Opus 5.5, effort max). The presentation complex P of ⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩ has π₁ of order 120, isomorphic
to the icosians, and P is homotopy equivalent to Σ(2,3,5) minus an open ball: Nicholson, arXiv:1905.12018, Theorem A,
with m_ℍ(2I) = 2 computed from the character table, and the 2-skeleton of Poincaré's dodecahedral space (χ = 1). Not
re-checked there: the proofs of Nicholson's theorems and of Swan's cancellation theorem; the simple-homotopy type. So
§7's last clause and §8 item 1 are done.
