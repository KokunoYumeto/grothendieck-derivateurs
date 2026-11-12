Every statement holds.

(Two wording points for a revision, neither a failure: in (a) "is BM" means "is homotopy equivalent to BM", as the conjecture has it; in (g) "smallest" means fewest arrows, identities counted, and this is now proved by exhaustive enumeration. Claim (d) rests on Theorem C of the preprint, which is unrefereed; I read its proof in full and found no gap.)

# Check of the e-mail of 12 Nov 2026 on Conjecture 7.1 of arXiv:2610.38760v1

Checker: Claude Fable 5.2 (Anthropic), effort max, 12 Nov 2026. Started from nothing: no earlier review was opened.
What I read first, in the primary texts (exact locations in `READING_BASE.md`):

- O. Ben-Bassat, *On a Conjecture of Fiedorowicz*, arXiv:2610.38760v1 (28 Oct 2026; recent, unrefereed), the whole TeX source and the PDF (19 pp.).
- H. Miller, *The Sullivan conjecture on maps from classifying spaces*, Ann. of Math. (2) 120 (1984), 39–87: Introduction (Theorems A–D, pp. 39–41) and Section 10 (pp. 84–85), from the author's page; and the *Correction*, Ann. of Math. 121 (1985), 605–609.
- M. F. Atiyah, *Characters and cohomology of finite groups*, Publ. Math. IHES 9 (1961), 23–64 (Numdam): §6 (6.10)–(6.13), §7 (7.1)–(7.9), §8 (8.1).
- D. Sweeney, *Homotopy types of small semigroups*, arXiv:2502.05276v2 (13 Jun 2026; recent): §§1–2, 5.
- Z. Fiedorowicz, *A counterexample to a group completion conjecture of J. C. Moore*, AGT 2 (2002), 33–35.
- Grothendieck, *Les Dérivateurs*: V ms. 11–13 and 37–52; VII ms. 108–136 and 149–156; IX ms. 8–13 and 22–25; the Appendix to XII (ms. 1–18), in the transcription of the background package.

My programs and their outputs are in `work/code/` (`catlib.py`, `models_check.py`, `resolution_check.py`, `enum_monoids.py`, `enum_cats.py`, `theoremA_test.py`, and the `.out`/`.json` files). I did not run the return's code.

Notation. M is a finite monoid, BM = |N M| its classifying space, U(M) its universal group with η: M → U(M). "≃" is homotopy equivalence.

---

## (a) Conjecture 7.1 as stated in v1 is what the e-mail says it is. **Holds.**

Text of v1 (TeX source, lines 1282–1285; PDF p. 17, numbered 7.1 because Section 7 is "The finite fundamental-group question" and the conjecture is its first numbered statement):

> **Conjecture 7.1.** Let X be a connected finite CW complex. If π₁(X) is finite, then X ≃ BM for some finite monoid M.

The e-mail: "every connected finite CW complex with finite fundamental group is BM for a finite monoid M". Same quantifiers, same hypotheses, same conclusion. The one difference is "is BM" for "X ≃ BM": the preprint fixes "≃" as homotopy equivalence (§2, Conventions), and the e-mail's own argument is about homotopy type ("has the homotopy type of a finite-dimensional CW complex"), so the statement refuted is the one in v1. In a revision or a reply, write "is homotopy equivalent to BM".

The other references of the e-mail to the preprint are also exact: Lemma 2.4 is the retract lemma (every object a retract of c₀ ⇒ B D(c₀, c₀) ≃ B D); j_e: B(eMe) → BM is defined in the Introduction as the span B(eMe) → B Kar(M) ← BM with the second map an equivalence by Lemma 2.4; §7 proves that η_M is onto and U(M) finite; only v1 exists on arXiv today (abstract page fetched 12 Nov 2026).

## (b) RP² is a counterexample. **Holds.**

RP² is a connected finite CW complex (three cells) with π₁ = Z/2, finite. If RP² ≃ BM with M finite, then BM has the homotopy type of a finite-dimensional CW complex, so U(M) = 1 by (c); but U(M) = π₁(BM) ≅ π₁(RP²) = Z/2. Contradiction. The same argument excludes every connected finite-dimensional CW complex with non-trivial fundamental group (RPⁿ for n ≥ 2, lens spaces, S¹, surfaces, …).

## (c) A finite monoid whose classifying space has the homotopy type of a finite-dimensional CW complex has trivial universal group. **Holds.** Full proof:

**Step 0 (standard facts).** (i) π₁(BM) ≅ U(M): N M is a reduced simplicial set, so π₁ has one generator [m] for each m ≠ 1 and one relation [m₁][m₂] = [m₁m₂] for each 2-simplex; this is the presentation of U(M), and the loop of m is η(m). (ii) η is onto and U(M) is finite: for a ∈ M there are r < s with aʳ = aˢ, so η(a)^{s−r} = 1 and η(a)⁻¹ = η(a^{s−r−1}); every word in the η(a)^{±1} is therefore η of an element of M (this is §7 of the preprint).

**Step 1 (H = eMe is a group and η|H is onto).** Let K be the intersection of all two-sided ideals of M; it is a two-sided ideal, non-empty because it contains every product of one element from each ideal. Some power of an element of K is idempotent; call it e, and put H = eMe, a finite monoid with identity e. For x ∈ H we have x ∈ K, and MxM is a two-sided ideal inside K, so MxM = K ∋ e: e = axb with a, b ∈ M. Since x = exe, e = e·axb·e = (eae)·x·(ebe), so uxv = e in H with u = eae, v = ebe. In a finite monoid a left-invertible element is invertible (left multiplication by it is injective, hence bijective). So xv is invertible with inverse u, then x·(vu) = e, and by the same argument on the right x is invertible. Hence H is a finite group. η(e) is an idempotent of a group, so η(e) = 1 and η(eme) = η(m); η|H: H → U(M) is a group homomorphism (it sends the identity e to 1), and it is onto because η is.

**Step 2 (a map BH → BM inducing η|H on π₁).** Kar(M) has the idempotents of M as objects and Hom(f, g) = gMf. Its full subcategory on the object 1 is M, on the object e it is H. The arrows r = e ∈ Hom(1, e) = eM and s = e ∈ Hom(e, 1) = Me satisfy r∘s = e = id_e, so e is a retract of 1 (likewise every object), and j: M → Kar(M) induces a homotopy equivalence on classifying spaces (Lemma 2.4 of the preprint; its proof by Quillen's Theorem A is correct: the comma category j/f is a retract of j/1, which has a terminal object). In the fundamental groupoid of B Kar(M), [r][s] = 1, so [s] = [r]⁻¹, and for h ∈ H the loop [h] at e is carried by the path [r] to the loop [s][h][r] = [s∘h∘r] = [ehe] = [h] at 1, where now h is read in M = End(1). Under π₁(BM) = U(M) this is η(h). So the composite BH → B Kar(M) ←≃ BM induces η|H: H → U(M) on fundamental groups (up to the inner automorphism that a change of base path introduces), a surjection by Step 1.

**Step 3 (the topological input).** *Proposition.* Let G be a finite group and X a connected CW complex of finite dimension d. Every map f: BG → X is trivial on π₁.

This is Miller's Theorem B for finite G (statement and hypotheses checked under (e)). A complete proof, by Miller's own route but with Atiyah's theorem quoted exactly:

Write φ = f_*: G → π₁(X) and suppose φ ≠ 1. Some g ∈ G has φ(g) ≠ 1; g is a product of commuting elements of prime-power order (its primary components, which are powers of g), so some element c of p-power order has φ(c) ≠ 1. Let C = ⟨c⟩, a cyclic p-group, and N = φ(C), a cyclic p-group ≠ 1. Let X′ → X be the connected covering with π₁(X′) = N; X′ is a CW complex of dimension d, and f|BC lifts to f′: BC → X′ with f′_* = φ|C: C → N, onto. Choose a character ψ: N → C^× of order p and let L be the flat line bundle X̃ ×_N C_ψ on X′. Then f′^*L is the line bundle on BC of the character χ = ψ∘φ|C, which has order exactly p because φ|C is onto N.

In K⁰(X′) the class x = [L] − 1 restricts to 0 on the 0-skeleton. The skeletal filtration F^q = ker(K⁰(X′) → K⁰(X′^{(q−1)})) is multiplicative (F^a F^b ⊂ F^{a+b}, by cellular approximation of the diagonal) and F^{d+1} = 0 since X′ has dimension d. So x^{d+1} = 0. (Miller says the same through Lusternik–Schnirelmann category.) Pulling back, (χ − 1)^{d+1} goes to 0 in K⁰ of every finite skeleton of BC, that is, α((χ − 1)^{d+1}) = 0 in 𝒦⁰(B_C) = lim K⁰(B_C^{(n)}), where α: R(C) → 𝒦⁰(B_C) is Atiyah's homomorphism. By Atiyah's Proposition (8.1) (cyclic groups; or Theorem (7.2) in general) α̂: R(C)^ → 𝒦*(B_C) is an isomorphism, and by Proposition (6.11) R(C) → R(C)^ is injective for a p-group. Hence (χ − 1)^{d+1} = 0 in R(C). But R(C) is a ring of functions on C, and at a generator c of C the character (χ − 1)^{d+1} takes the value (ζ − 1)^{d+1} ≠ 0, ζ = χ(c) a primitive p-th root of unity. Contradiction. ∎

**Step 4 (conclusion).** Let k: BM → Z be a homotopy equivalence with Z a finite-dimensional CW complex; Z is connected because BM is. Choose a homotopy inverse of Bj (both spaces are CW complexes). The composite BH → B Kar(M) → BM → Z is trivial on π₁ by Step 3 and onto on π₁ by Step 2. So π₁(Z) = 1, that is, U(M) = 1. ∎

Remarks. (1) Nothing but Step 3 is more than a page of elementary algebra. (2) The statement can be sharpened; see "Beyond the e-mail" below.

## (d) Among connected finite CW complexes the ones realized by finite monoids are exactly the simply connected ones, given Theorem C. **Holds, given Theorem C; Theorem C does give the simply connected case.**

Theorem C of v1 (TeX lines 189–193): "Conjecture 1.1 holds. More strongly, every finite simply connected CW complex is homotopy equivalent to BM for a finite aperiodic monoid M", with "simply connected" defined in the Introduction as path connected with trivial fundamental group. So: if X is a finite simply connected CW complex, X ≃ BM with M finite (Theorem C); if X is a connected finite CW complex and X ≃ BM with M finite, then π₁(X) = U(M) = 1 by (c). The two classes coincide. The e-mail's wording "would be exactly" and "makes your Theorem C the complete answer" (for finite complexes) is accurate.

What I checked of Theorem C itself, since (d) stands on it. I read the whole proof.
- Lemma 2.4 (retracts), Lemma 2.6 (truncated category of simplices: the comma category retracts onto the factorizations with surjective first map, which has a terminal object by Eilenberg–Zilber), Lemma 3.2 (normal forms in the category with the adjoined retraction), Lemma 4.2 for the object •_L (the comma category retracts onto a category built from Q_L, which has a terminal object), Lemma 5.2 (aperiodicity is preserved: (y, l, i)^r = (y, l c^{r−1}, i) with c = hol_i(y) l), Lemma 5.3 (reduction to one vertex: the two horn fillings and their labels, e y e = e for y ∈ {a, 1} with e = a^r), and the induction over cells: I re-derived each and found them correct.
- Lemma 2.5 (collage = homotopy pushout) is the standard description of the cograph of a profunctor; its proof through Thomason's homotopy colimit theorem and Quillen's Theorem A reads correctly.
- Not opened by me, used as cited: Jardine, *Simplicial approximation*, Cor. 4.8; Geoghegan, *Topological methods in group theory*, Prop. 4.2.1 (cell trading); Thomason 1979, Theorem 1.2.
- Consistency tests of Theorem A by my own program (`theoremA_test.py`; mod-p Betti numbers and low integral homology of the bar complex of M(Y, f) built from Definition 3.3): Example 3.2 with f = f_g (order 11): H₁ = 0, H₂ = Z, mod-2 Betti numbers 0, 1, 1 in degrees 1–3, as for RP^∞/RP¹; with f = f_1 (order 11): 1, 2, 1 mod 2 and 0, 1, 0 mod 3, as for BC₂ ∨ S²; A₂ (order 7): the homology of S² through degree 3; A₃ (order 16): Betti numbers 0, 0, 1 mod 2 and mod 3; M(sk₂ N(C₂), *) (order 22): Betti numbers 0, 1 mod 2 and 0, 0 mod 3, as for ΣRP². All agree with Theorem A. These are tests, not a proof.
I found no gap. The preprint is recent (28 Oct 2026) and unrefereed, so (d) should be stated as conditional on it, as the e-mail does.

## (e) Proof steps 1, 2 and 3 as written. **Each holds.**

**Step 1 of the e-mail.** "H is a finite group": proved in (c) Step 1 (it is also the classical fact that for an idempotent e of the minimal ideal, eMe is the maximal subgroup at e; cf. Sweeney's Lemma 2.1, quoting Larisse and Howie–Margolis, where the group completion of a finite semigroup is computed as a quotient of that group). "H → U(M) = π₁(BM) is onto, because η(e) = 1 and η(eme) = η(m) for the universal homomorphism η, which is onto as in your §7": correct as written; U(M) = π₁(BM) is McDuff's Lemma 1, proved above in two lines.

**Step 2 of the e-mail.** Correct as written, with the conventions Hom(f, g) = gMf of the preprint: r = e: 1 → e, s = e: e → 1, r∘s = id_e, and s∘h∘r = ehe = h in End(1) = M, so the loop [s][h][r] at 1 is the class of h. Lemma 2.4 is the right reference for BM ≃ B Kar(M).

**Step 3 of the e-mail.** The quotation of Miller is exact. Ann. of Math. 120 (1984), p. 40:

> **Theorem B.** Let X be a finite dimensional CW complex and G a torsion group. Then any pointed map BG → X induces the trivial map of fundamental groups.

It is restated as Theorem 10.1 on p. 84 ("any map BG → X") and proved on pp. 84–85; p. 41: "Theorem B is an exercise in covering spaces and K-theory; it is carried out in Section 10." Standing conventions (p. 40): classifying spaces are CW complexes and base points are vertices. Hypotheses against the case used: G = H is finite, hence a torsion group; X = Z is a finite-dimensional CW complex by assumption (connectedness is not required by the theorem); the map is the composite BH → B Kar(M) → BM → Z, defined after choosing a homotopy inverse, and can be taken cellular, hence pointed at vertices; in any case 10.1 does not ask for pointedness. So the theorem covers the case. "Being both trivial and onto, it forces π₁(Z) = 1": correct.

On Miller's proof: I checked it. With σ ∈ G of order mn mapped to an element of order m > 1, the map Bh: BZ_{mn} → BZ_m factors through a finite-dimensional covering space, so the image of x_m = ξ_m − 1 ∈ K̃⁰(BZ_m) in K⁰(BZ_{mn}) = Z[[x]]/((1+x)^{mn} − 1) would be nilpotent; it is (1+x)ⁿ − 1, which is not nilpotent: for a prime p | m let p^c be the exact power of p in mn and ζ a primitive p^c-th root of unity; x ↦ ζ − 1 defines a continuous ring map to Z_p[ζ], a domain, under which (1+x)ⁿ − 1 ↦ ζⁿ − 1 ≠ 0 because p^c ∤ n. The 1985 Correction concerns two errors elsewhere (the unstable-module statement behind the spectral sequence (2.5), and "Fact 3.9"), both in the proof of Theorem C of that paper; it does not touch Section 10.

## (f) The Atiyah route. **Holds.**

Publ. Math. IHES 9 (1961): Theorem (7.2), p. 46: "α̂: R(G)^ → 𝒦*(B_G) is a topological isomorphism", where 𝒦*(X) = lim K*(Xⁿ) over the finite skeleta and R(G)^ is the I(G)-adic completion; Proposition (6.11), p. 45: "If G is a p-group then R(G) → R(G)^ is a monomorphism" (from (6.10): the kernel in general is the set of characters vanishing on all elements of prime-power order). For a cyclic p-group C and a character χ of order p, χ − 1 is not nilpotent in R(C) (its value at a generator is ζ − 1 ≠ 0), so by (6.11) and (7.2) its image in K⁰ of BC is not nilpotent. "While it would be pulled back from a finite-dimensional complex": yes, in the situation of Step 3, after the two reductions spelled out in (c) Step 3 (pass to a cyclic p-subgroup C on which the map on π₁ is non-trivial, and to the covering X′ whose fundamental group is the image of C); the pulled-back class is [L] − 1 for a flat line bundle L on X′, and it is nilpotent because X′ has finite dimension. For cyclic groups Atiyah's (8.1) already gives the isomorphism, so the full completion theorem is not needed. The sentence in the e-mail is compressed but correct.

## (g) The finite models. **Each holds; "smallest" is now proved, by exhaustive enumeration with my own code.**

**(g1) A three-object, nine-arrow category of type RP².** R₂: objects 0, 1, 2; Hom(i, j) = Z/2 for i < j, empty for i > j, only identities as endomorphisms; composition Hom(1,2) × Hom(0,1) → Hom(0,2) is addition. Nine arrows. No non-identity composite is an identity, so the non-degenerate simplices of the nerve are closed under faces: 3 vertices, 6 edges (i < j, a), 4 triangles (a, b) with edges a, b, a + b, nothing above. Every edge lies in exactly two triangles and every vertex link is one 4-cycle (program), so BR₂ is a closed connected surface with Euler characteristic 3 − 6 + 4 = 1 and H₁ = Z/2: it is RP². Equivalently it is the quotient of the octahedron S⁰ * S⁰ * S⁰ by the antipodal map: (i, ε) ↦ i on vertices, ε_i ε_j on edges. BR₂ is homeomorphic to RP², not only homotopy equivalent.

**(g2) "…which shows the obstruction is to having one object."** Correct: by (c) no finite monoid has type RP², and R₂ is a finite category of that type. Sharper (return G.12–G.13, which I re-proved): a finite category of type RP² has at least three objects and at least nine arrows, so R₂ is smallest in both senses. The proof passes to the quotient that collapses each strongly connected component; its fundamental group is unchanged because every component maps trivially on π₁ by Miller's theorem, and an acyclic category with non-free fundamental group needs three objects with at least two arrows between each pair. For at most 7 arrows I also confirmed by enumeration that no category with at least two objects has (H₁, H₂, H₃) = (Z/2, 0, 0).

**(g3) The smallest finite categories of types S¹, S², S³.** Size = number of arrows, identities included.
- *Enumeration.* All monoids of order n ≤ 6, labelled with the identity fixed: 1, 2, 11, 156, 4,122, 208,672 tables; 1, 2, 6, 27, 156, 1,373 classes up to isomorphism and anti-isomorphism (the known counts). All connected categories with k ≥ 2 objects and N ≤ 7 arrows, as labelled tables with the arrows sorted by (source, target): (N, k) = (3,2): 2; (4,2): 11; (5,2): 76; (5,3): 6; (6,2): 977; (6,3): 54; (7,2): 22,798; (7,3): 498; (7,4): 32. For each, exact integral H₁, H₂, H₃ of the nerve from the normalized chain complex (Smith normal forms). The code was validated on S¹, S², RP², BC₂ and on group homology (C_k, C₂², S₃).
- *S¹.* No category with ≤ 3 arrows has H₁ = Z. With 4 arrows exactly the two labellings of the parallel pair 0 ⇉ 1 have (H₁, H₂, H₃) = (Z, 0, 0); its nerve is a circle. So the smallest category of type S¹ is the parallel pair (2 objects, 4 arrows), and it is unique. One object is impossible (U(M) is finite).
- *S².* No category with ≤ 4 arrows has H₂ = Z. With 5 arrows the only ones with (0, Z, 0) are the monoids isomorphic to P₂ = {1} ∪ {x_ij : i, j ∈ {0,1}}, x_ij x_kl = x_il (one class; no category with 2 or 3 objects). BP₂ ≃ S²: every element is idempotent, so U(P₂) = 1, and the left-module complex 0 → Rx₀₀ ⊕ Rx₀₁ → R → Rx₀₀ → Z → 0 (R = Z[P₂]; maps (a, b) ↦ a + b, c ↦ c(x₁₀ − x₀₀), augmentation) is a resolution by projectives (exactness verified over Z by ranks and saturation, `resolution_check.py`); tensoring gives Z² → Z → Z with maps (1 1) and 0, the homology of S²; Hurewicz and Whitehead finish. This is Fiedorowicz's monoid (AGT 2 (2002), Lemma, pp. 33–34). So the smallest category of type S² is this five-element monoid, unique up to isomorphism.
- *S³.* No monoid of order ≤ 6 and no category with ≥ 2 objects and ≤ 7 arrows has (H₁, H₂, H₃) = (0, 0, Z) (the triples that occur for monoids of order 6 are (0,0,0), (0,Z,0), (0,Z,Z), (0,Z,Z/2), (0,Z/2,0), (Z/k,0,Z/k) for k = 2,…,6, (Z/2,0,Z/6), ((Z/2)², Z/2, (Z/2)³)). So a category of type S³ has at least 7 arrows, and one with exactly 7 arrows is a monoid. P₃ = P₂ ∪ {q, r} with x_ij q = x_ij r = x_i0, q x_ij = r x_ij = x_ij, q² = qr = q, r² = rq = r is a monoid of order 7 (associativity checked), all of whose elements are idempotent, and 0 → Rx₀₁ ⊕ Rq → Rx₀₀ ⊕ R → Rq → Rx₀₀ → Z → 0 with maps (c, d) ↦ (0, c + d), (a, b) ↦ a + b(r − q), c ↦ c(x₁₀ − x₀₀) is a projective resolution (verified exactly); tensoring gives Z² → Z² → Z → Z with matrices ((0,0),(1,1)), (1 0), (0): the homology of S³. Hence BP₃ ≃ S³. The bar complex gives the same groups through degree 3 (independent check). This is Sweeney's six-element semigroup (v1, Example 8.2, as the return cites it) with an identity adjoined.

**(g4) "For S² and S³ these are monoids, with five and seven elements."** Correct, in the strong sense: every category of type S² with 5 arrows and every category of type S³ with 7 arrows is a monoid.

## Beyond the e-mail (my own additions; proofs in `OWN_RESULTS.md`)

1. Finite dimension can be replaced by bounded integral homology: if H_k(M; Z) = 0 for all large k, then U(M) = 1. Hence for a finite monoid M: BM has the homotopy type of a finite complex ⇔ of a finite-dimensional complex ⇔ H_*(M; Z) is bounded; and a finite monoid with U(M) ≠ 1 has non-zero integral homology in infinitely many degrees (Swan's theorem for groups, extended to monoids).
2. Every connected finite-dimensional complex with non-trivial π₁ is a counterexample to Conjecture 7.1, not only RP².
3. Not settled, and worth a line to the author: whether a finite *category* with finite-dimensional classifying space always has the homotopy type of a finite complex (Wall's obstruction), and whether K(Z, 2) is the classifying space of a finite monoid.

## A caution on wording for the reply to the author

- Say "homotopy equivalent to BM".
- Theorem B of Miller is stated for torsion groups and finite-dimensional CW complexes; "finite-dimensional" refers to an actual CW complex in the homotopy type, which is the hypothesis of (c).
- "Smallest" refers to the number of arrows; for RP² the three-object category is smallest in objects and in arrows.
