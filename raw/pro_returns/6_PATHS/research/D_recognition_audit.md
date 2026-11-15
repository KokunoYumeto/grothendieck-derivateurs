# Independent risk audit of D.13 and D.15

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), within this collaboration; no priority is claimed. This audit read the current `sections/D.tex`, especially D.13–D.15, and the extracted Kaledin v3 text at Definition 7.2.2.1, Lemma 7.3.1.1 with formulas (7.3.1.7)–(7.3.1.8), Example 7.3.1.2, and Theorem 7.3.1.3 with its proof. No optional additional literature search was undertaken.

**Conclusion:** both arguments are sound as stated, with Kaledin's representation theorem retained as an explicitly identified preprint dependency. No mathematical correction is required. The localization argument really identifies the represented infinity-category with L(M,W) and proves that the canonical comparisons are equivalences; it does not merely show that the family represents some unrelated category.

## 1. The precise categorical content of Kaledin's theorem

Definition 7.2.2.1 says that an enhanced functor is a functor cartesian over the designated shape category, and its morphisms are morphisms over that category. It imposes no preservation of homotopy Kan extensions. Consequently both the pointwise localization map and the canonical comparison map in D.15 are admissible enhanced functors once the source and target families satisfy the enhancement axioms.

Theorem 7.3.1.3 has each clause needed in D.15: representation of the family, representation of every enhanced functor between the represented families by a map of complete fibrant Segal spaces, and detection of homotopy of those maps by isomorphism of enhanced functors. The theorem supplies these statements both on Pos and on Pos⁺ in the senses fixed in D.14. D.15 does not replace either shape category by finite posets. Its restricted theorem still requires all the allowed infinite finite-dimensional posets.

The identification of K(X)_J with the homotopy category of J^op-diagrams is compatible with the expansion description used in Lemma 7.3.1.1. The core records the fundamental groupoid of the derived diagram space; applying the expansion to the values on J×[n] recovers arrows and composition, hence the entire homotopy category of diagrams rather than only its core. For an ordinary category M, this returns the ordinary category Fun(J^op,M). There is therefore no change of the represented input hidden in the notation K(M).

## 2. Descent of cartesian functors and their transformations

The pointwise localization step is genuinely two-categorical. Let A be a category-valued family, let S_J be a class of arrows in each fibre A_J preserved by restriction, and let D_J=A_J[S_J⁻¹]. For cartesian functors F,G:D→E, precomposition with ℓ:A→D is fully faithful on transformations over the base.

To check this directly, choose the ordinary formal-word localization, which keeps the objects of A_J. A transformation α:Fℓ→Gℓ supplies its component at every object of D_J. Naturality for an original arrow is given. If s is inverted, naturality for s⁻¹ follows from the square for s by multiplying by the images of s⁻¹ on the appropriate sides. Naturality for each word follows by composition. Thus the extension on each fibre is unique.

A cartesian functor is equivalently a pseudonatural transformation of the corresponding category-valued pseudofunctors. Its coherence for a restriction u* is an invertible natural transformation between two functors out of the source fibre. The same localization argument descends that transformation uniquely. An equation between two such coherence composites can be tested after precomposition with ℓ, because that precomposition is faithful. Hence identity and composition coherence survive. A modification between cartesian functors has its restriction-compatibility equation descended in the same way.

Equivalently, every arrow of the Grothendieck construction factors as a vertical arrow followed by a chosen cartesian lift. The localization preserves the chosen cartesian lifts, while all additional vertical arrows are finite words in the old vertical arrows and their marked inverses. The preceding naturality checks therefore cover all arrows of the total category, not merely arrows within a fibre.

If the original transformation is invertible, its inverse descends too, and the two composite identities are detected before localization. Thus a natural isomorphism after precomposition lifts to a natural isomorphism, not just to an arbitrary transformation. This is the exact strength required for the second inverse in D.15. There is no interchange of an infinite product with π₀ and no unbounded-zigzag issue in this argument: the transformations under discussion are actual natural transformations with all their components.

## 3. Identification of the represented infinity-category

Fix an enhanced equivalence e:D≃K(X). Suppressing e in notation, as the TeX does, is harmless; keeping it explicit gives the following diagrammatic argument.

The enhanced functor eℓ:K(M)→K(X) is represented by f:NM→X. For every w in W, its value in the point fibre D_pt is invertible. A natural isomorphism K(f)≅eℓ therefore implies that f(w) is invertible in Ho(X), equivalently that f sends w to an equivalence of X. With C=L(M,W) and q:NM→C, the infinity-localization universal property supplies g:C→X and a natural equivalence gq≃f.

The canonical comparisons θ_J:D_J→Ho Fun(NJ^op,C) commute with every restriction. Indeed a pointwise W-map becomes a pointwise equivalence of coherent diagrams; pointwise equivalences are exactly equivalences in the functor infinity-category. This constructs a cartesian functor θ:D→K(C). The representation theorem gives h:X→C with K(h)e≅θ. Its composite with ℓ is the canonical K(q), so the theorem's homotopy-detection clause gives hf≃q.

It follows that hgq≃q. Precomposition with q is fully faithful on infinity-functor categories, with essential image the functors inverting W. Applying it to the two functors hg,id_C:C→C lifts this equivalence uniquely to hg≃id_C. This use of the localization universal property is in its correct source variance.

For the other inverse, the natural equivalence gq≃f gives an isomorphism

\[
K(g)\theta\ell\cong e\ell.
\]

The fully faithful localization descent from §2 gives K(g)θ≅e. Combining this with K(h)e≅θ shows K(gh)e≅e. Cancel the enhanced equivalence e to get K(gh)≅id_K(X). Kaledin's final homotopy-detection clause then yields gh≃id_X. Thus g and h are mutually inverse equivalences.

Crucially, h represents θ itself. Hence it is the specified comparison θ_J, not an unrelated equivalence of the source and target categories, that is proved to be an equivalence. No essential step requires an arbitrary natural transformation between enhanced functors to come from a higher transformation: the theorem is used only to represent functors and to detect isomorphisms between their represented composites, exactly as stated.

Conversely, pointwise equivalence of the canonical comparison functors, together with their restriction compatibility, is a cartesian equivalence of families. Enhancement axioms are invariant under this equivalence. The coherent family K(C) has those axioms by Lemma 7.3.1.1, proving the converse. The smallness and compatible-universe conditions in D.14–D.15 must remain; no enlargement or restriction of the test-shape universe has been silently used.

## 4. The explicit face-orbit presentation in D.13

Let K be the infinite join of copies of S⁰. Its faces are the nonempty finite sets F of signed natural numbers containing at most one sign at each index. Simultaneous sign reversal has no fixed face and cannot stabilize any simplex setwise. Its action on the realization is free as well: a fixed point would have invariant barycentric support, which would require both signs at an index.

The orbit relation in D.13 defines a genuine partial order. Reflexivity is immediate. If εF⊆G and δG⊆H, then δεF⊆H, proving transitivity. Mutual comparability implies equal finite cardinalities, so the inclusions are equalities up to sign and the two orbits coincide, proving antisymmetry.

For F nonempty, there cannot be two aligning signs with both F⊆G and −F⊆G: select an index occurring in F and use the fact that G contains at most one sign there. This uniqueness proves that a chain of face orbits lifts uniquely after one representative has been chosen. It also applies to repeated vertices in degenerate chains. Therefore the identification

\[
NQ=N(\operatorname{Face}K)/C_2
\]

is an isomorphism of simplicial sets, with faces and degeneracies respected.

The finite joins are spheres in increasing dimensions. A map from a compact sphere into the CW union lies in a finite subcomplex and hence in one finite join. It becomes nullhomotopic in a sufficiently larger join. Thus K is weakly contractible, and CW Whitehead makes it contractible. BFace(K) is its barycentric subdivision and has the same type. Its free C₂ quotient is consequently a K(C₂,1), as claimed.

Choose the representative with plus sign at the least index. The sign ε for an order relation [F]≤[G] is uniquely characterized by εF⊆G. For composable relations the signs multiply, so the stated q:Q→BC₂ is an actual functor. The associated cover has the two face representatives over each orbit, and its arrows are the inclusions after sign alignment. It is exactly Face(K)→Q. Thus q classifies a connected contractible universal cover and induces an isomorphism on π₁; both classifying spaces are aspherical. It exhibits BC₂ as the infinity-groupoid completion of Q. Since all arrows are marked, this is precisely the asserted infinity-localization presentation.

For a strict functor BC₂→Q, every group element must act by an automorphism of one object of the poset, hence by its identity. Natural transformations between these constant diagrams are exactly the order arrows of Q. Thus Q^{BC₂}≅Q as categories, including their arrows. Its localization is connected. In contrast, the coherent functor groupoid Fun(BC₂,BC₂) has two components: its objects are the trivial and identity homomorphisms; since C₂ is abelian, no conjugation identifies them. Both components have automorphism group C₂, which is consistent with, and stronger than, the components calculation used in the text. The canonical comparison lands in the trivial-homomorphism component, so it is not essentially surjective.

The first example in D.13 separately gives a finite presenting poset, using the six-element circle poset and target BZ. The second example gives a finite target and finite testing category, using the countable orbit poset Q. The text does not incorrectly claim that Q itself is finite, and neither example confuses the universal property of functors out of a localization with localization of strict functors into its presentation.

## 5. Residual qualifications

- The recognition statement remains conditional on the full stated Kaledin axioms and his v3 representation theorem. Its preliminary-preprint status is accurately recorded in D.14.
- It does not recognize enhancement from the point fibre, finite posets alone, or the manuscript's weaker component-valued tests.
- The abstract equivalence e:D≃K(X) is fixed during the argument. Restoring it explicitly, as above, verifies all types; suppressing it in the TeX is conventional and introduces no logical gap.
- No extra saturation or two-out-of-three assumption is needed for the two localization universal properties used in the proof.

No further correction or numerical experiment is required for these two statements.
