# OWN_RESULTS: statements proved in this review, with full proofs

Author of this file: Claude Fable 5.2 (Anthropic), effort max, 12 Nov 2026, during the review of the return CATHOT
(GPT-6 Astra, OpenAI, effort Pro, ChatGPT Pro mode). Nothing here has been checked by anyone else. Each result says
what it uses from the return (with my verdict on that item, see `REVIEW.md`) and from the literature (exact
locations in `READING_BASE.md`). No priority is claimed; "new" below means: not in the return, and not found by me in
the sources I read. Prompts asking GPT-6 Astra to check and push these results: `PRO_PROMPTS/`.

Conventions as in the return: a universe U; small categories; BX = |NX|; W∞; Hot; Cat_hot with
Hom(X, K) = π₀Fun(X, K); Π₁X the groupoid obtained by inverting all arrows of X, η_X: X → Π₁X. For a monoid M,
U(M) is its universal group. [A, Y] is the set of free homotopy classes.

Contents: 1. Maps from BG under a cohomological bound. 2. Finite monoids: finite, finite-dimensional and bounded
homology coincide. 3. A Kan–Thurston theorem with no small quotients, and the settlement of E.17 (V ms. 44–46).
4. A criterion for uncountably many maps to S² (towards D.6). 5. A better lower bound for posets of type RP².
6. The census of small categories.

---

## 1. Maps from classifying spaces of finite groups under a cohomological bound

**Theorem 1.1.** Let X be a connected CW complex with finite fundamental group π, and suppose H^q(X; Z) = 0 for all
q > n. Let G be a finite group and f: BG → X a map. Then f_*: G → π is trivial.

**Theorem 1.2 (p-local form).** Let X be a connected CW complex with finite fundamental group π, p a prime, and
suppose H^q(X; Z_(p)) = 0 for all q > n. Then for every finite group G and every map f: BG → X, the order of the
image of f_*: G → π is prime to p.

Miller's Theorem B (Ann. of Math. 120 (1984), p. 40) has "X finite-dimensional" as hypothesis and no condition on
π₁(X). Here the dimension hypothesis is weakened to a bound on ordinary cohomology with constant coefficients, at the
price of assuming π₁(X) finite (residually finite, or linear over C, is enough for 1.1; see the remark at the end).
The proof is Miller's and Atiyah's, with the covering-space step replaced by the regular representation.

*K-theory used.* K⁰(Y) = [Y, Z × BU] for CW complexes Y; it is a ring, contravariant in Y. For a CW complex Y put
F^q(Y) = ker(K⁰(Y) → K⁰(Y^{(q−1)})).
(K1) F^a · F^b ⊂ F^{a+b}. Proof: if x ∈ F^a, y ∈ F^b, lift them to x̃ ∈ K⁰(Y, Y^{(a−1)}), ỹ ∈ K⁰(Y, Y^{(b−1)}); the
external product x̃ ⊠ ỹ lies in K⁰(Y × Y, Y^{(a−1)} × Y ∪ Y × Y^{(b−1)}), and the (a+b−1)-skeleton of Y × Y is
contained in Y^{(a−1)} × Y ∪ Y × Y^{(b−1)}; a cellular approximation Δ′ of the diagonal maps Y^{(a+b−1)} into it,
so (xy)|Y^{(a+b−1)} = Δ′^*(x ⊠ y)|… = 0.
(K2) If H^q(Y; Z) = 0 for all q > n, then F^q(Y) = F^{q+1}(Y) for all q > n; hence F^{n+1}(Y) = ⋂_q F^q(Y).
Proof: let x ∈ F^q, q > n. Then x|Y^{(q)} comes from a class c ∈ K⁰(Y^{(q)}, Y^{(q−1)}) = C^q(Y; K̃⁰(S^q)), the
cellular cochains with coefficients Z (q even) or 0 (q odd). Since x|Y^{(q)} extends over Y^{(q+1)}, the image of c
in K¹(Y^{(q+1)}, Y^{(q)}) vanishes; that image is the cellular coboundary δc. So c is a cocycle, hence (H^q = 0) a
coboundary c = δb with b ∈ K^{−1}(Y^{(q−1)}, Y^{(q−2)}), and the image of δb in K⁰(Y^{(q)}) is zero because
K^{−1}(Y^{(q−1)}) → K⁰(Y^{(q)}, Y^{(q−1)}) → K⁰(Y^{(q)}) is exact. So x|Y^{(q)} = 0, that is x ∈ F^{q+1}.
(K3) A cellular map g: Y′ → Y satisfies g^*F^q(Y) ⊂ F^q(Y′).
(K1)–(K3) hold verbatim for the p-localized theory K_(p) (represented by the p-localization of the spectrum KU,
coefficients Z_(p) in even degrees), with H^q(−; Z_(p)) in (K2); and K⁰_(p)(Y) = K⁰(Y) ⊗ Z_(p) for finite Y.

*Atiyah's theorem used* (Publ. Math. IHES 9 (1961)). For a finite group G let 𝒦⁰(B_G) = lim_m K⁰(B_G^{(m)}) over
the finite skeleta of a model of BG with finite skeleta, and α: R(G) → 𝒦⁰(B_G) the map sending a representation to
its associated bundle. (7.2): α induces an isomorphism of the I(G)-adic completion R(G)^ onto 𝒦*(B_G). (6.10): the
kernel of R(G) → R(G)^ is the set of virtual characters vanishing on all elements of prime-power order; (6.11): it
is zero for a p-group. Two models of BG with finite skeleta are related by cellular homotopy equivalences, so "α(θ)
restricts to zero on every finite skeleton" does not depend on the model.

*Proof of 1.1.* Make f cellular; BG = |NG| has finite skeleta. Let ρ: π → GL_d(C) be the regular representation
(d = |π|), V = X̃ ×_π C^d the flat bundle on X, v = [V] − d ∈ K⁰(X). Since X is connected, v ∈ F¹(X); by (K1),
v^{n+1} ∈ F^{n+1}(X) = ⋂_q F^q(X) by (K2). By (K3), f^*(v^{n+1}) restricts to zero on every skeleton of BG. Now
f^*V is the flat bundle of the representation ρ∘φ of G, φ = f_*; so α((ρφ − d)^{n+1}) = 0 in 𝒦⁰(B_G). By (7.2) and
(6.10) the virtual character (χ_{ρφ} − d)^{n+1} vanishes at every g ∈ G of prime-power order: χ_ρ(φ(g)) = d. The
regular character takes the value d only at 1, so φ(g) = 1 for every g of prime-power order. Every element of a
finite group is a product of elements of prime-power order (its primary components). Hence φ = 1. ∎

*Proof of 1.2.* Suppose p divides |φ(G)|. Take u ∈ φ(G) of order p and g with φ(g) = u; if g has order p^a m with
p ∤ m (a ≥ 1) and mm′ ≡ 1 mod p^a, then c = g^{mm′} has p-power order and φ(c) = u. Put C = ⟨c⟩ and restrict f to
BC (cellular; take for BC the infinite lens space, whose odd skeleta are lens spaces L^{2j+1}). As above, with
K_(p): the image of v^{n+1} in K⁰_(p)(X) lies in ⋂_q F^q, so α((ρφ|C − d)^{n+1}) goes to zero in
K⁰(L^{2j+1}) ⊗ Z_(p) for all j. The group K̃⁰(L^{2j+1}) is a finite p-group (Atiyah–Hirzebruch: H̃^{even}(L^{2j+1}; Z)
consists of copies of Z/|C|), so K⁰(L^{2j+1}) → K⁰(L^{2j+1}) ⊗ Z_(p) is injective. Hence α((ρφ|C − d)^{n+1}) = 0
in 𝒦⁰(B_C), and by (7.2), (6.11) (C is a p-group; for cyclic groups Atiyah's (8.1) suffices) (ρφ|C − d)^{n+1} = 0
in R(C). Its value at c is (χ_ρ(u) − d)^{n+1} = (−d)^{n+1} ≠ 0. Contradiction. ∎

*Remark.* In 1.1 the regular representation can be replaced by any finite-dimensional complex representation ρ of
π₁(X), finite or not: the same proof gives ρ(f_*(g)) = 1 for all g ∈ G (a matrix of finite order with trace equal
to its size is the identity). So for arbitrary π₁(X) the image f_*(G) lies in the intersection of the kernels of
all finite-dimensional complex representations, and f_* is trivial if π₁(X) is residually finite or linear.

## 2. Finite monoids: finite type, finite dimension and bounded homology coincide

Let M be a finite monoid. Facts used, all proved in `G6_VERDICT.md`: π₁(BM) = U(M); η: M → U(M) is onto; for an
idempotent e of the minimal ideal, H = eMe is a finite group and there is a map j_e: BH → BM (through the Karoubi
envelope) inducing the surjection η|H on π₁. Also H_k(BM; Z) = Tor_k^{ZM}(Z, Z) is finitely generated for every k
(the bar complex is finitely generated in each degree).

**Theorem 2.1.** If H_k(M; Z) = 0 for all large k, then U(M) = 1. More precisely, if a prime p divides |U(M)|,
then H_k(M; F_p) ≠ 0 for infinitely many k.

*Proof.* If H_k(M; Z) = 0 for k ≥ n, then H^q(BM; Z) = Hom(H_q, Z) ⊕ Ext(H_{q−1}, Z) = 0 for q > n. π₁(BM) = U(M)
is finite. Theorem 1.1 applied to j_e: BH → BM says η|H is trivial; it is onto; so U(M) = 1. For the second
statement: if H_k(M; F_p) = 0 for all k ≥ k₀, then H_k(M; Z) ⊗ F_p = 0 and Tor(H_{k−1}(M; Z), F_p) = 0 for k ≥ k₀,
so the finitely generated groups H_k(M; Z) have zero localization at p for k ≥ k₀, and H^q(BM; Z_(p)) = 0 for
q > k₀. Theorem 1.2 applied to j_e gives p ∤ |η(H)| = |U(M)|. ∎

**Theorem 2.2.** For a finite monoid M the following are equivalent:
(i) BM has the homotopy type of a finite CW complex;
(ii) BM has the homotopy type of a finite-dimensional CW complex;
(iii) H_k(M; Z) = 0 for all large k.
If they hold, U(M) = 1 and BM is simply connected.

*Proof.* (i) ⇒ (ii) ⇒ (iii) are clear. (iii) ⇒ (i): by 2.1, BM is simply connected; its homology groups are
finitely generated and vanish above some degree n; by Hatcher, *Algebraic Topology*, Proposition 4C.1, a simply
connected CW complex with finitely generated homology is homotopy equivalent to a CW complex with one k-cell for
each Z summand of H_k and one k-cell and one (k+1)-cell for each finite cyclic summand of H_k: a finite complex of
dimension ≤ n + 1. ∎

**Corollary 2.3 (Swan's theorem for finite monoids).** A finite monoid with U(M) ≠ 1 has H_k(M; Z) ≠ 0 for
infinitely many k; if p divides |U(M)|, then H_k(M; F_p) ≠ 0 for infinitely many k. (For a finite group this is
Swan's theorem.)

**Corollary 2.4.** If the trivial left (or right) ZM-module Z has a projective resolution of finite length (M has
finite left or right cohomological dimension), then U(M) = 1 and BM has the homotopy type of a finite simply
connected CW complex.

**Corollary 2.5 (with Theorem C of arXiv:2610.38760v1; recent, unrefereed).** The homotopy types of the classifying
spaces of finite monoids with bounded integral homology are exactly the homotopy types of finite simply connected
CW complexes.

Comments. (a) This sharpens G.4 of the return (finite dimension ⇒ U(M) = 1), and it is what refutes Conjecture 7.1
of the preprint. (b) Among monoids of order ≤ 6 (my enumeration) the classes with H₁ ≠ 0 all show the torsion
pattern of 2.3 in degrees ≤ 3. (c) 2.2 fails for finite categories with several objects: BC₂ ⊔ pt aside, a finite
poset of type RP² is finite-dimensional with π₁ = Z/2; what survives for categories is G.12 of the return, and the
question H1 of `HUNCHES.md`.

## 3. A Kan–Thurston theorem without small quotients, and the settlement of E.17

The return leaves open (E.17): if a sequence K = (K_n) in Cat_hot has a W∞-invariant presheaf
H_K = colim_n π₀Fun(−, K_n), is K isomorphic in Ind(Cat_hot) to a sequence of groupoids? It reduces this to (E.17c):
H_K inverts every η_X: X → Π₁X. The answer is yes.

Input from the return (verified): B.7 (for every group H and every infinite cardinal λ ≥ |H| there is a non-abelian
simple, integrally acyclic group A ⊃ H with |A| = λ); A.4 and A.7; C.1, C.4; (E.17a).
Input from the literature: the Kan–Thurston theorem (D. M. Kan, W. P. Thurston, *Every connected space has the
homology of a K(π,1)*, Topology 15 (1976), 253–258): for every connected CW complex E there are a group T and a map
BT → E inducing isomorphisms on homology with every local coefficient system on E (an *acyclic* map); T can be taken
of cardinality at most max(ℵ₀, number of cells of E). I could not open the paper (the publisher's open archive
refused automated access); the statement is quoted from memory and agrees with the summary in Palmer–Wu,
arXiv:2510.16879v1, Introduction. It is used only in the successor step for cells of dimension ≥ 3 below.
Standard facts on acyclic maps (Hausmann–Husemoller): the homotopy fibre of an acyclic map is acyclic; acyclic maps
are stable under homotopy pull-back and composition; an acyclic map f: A → B of connected CW complexes is onto on π₁
with perfect kernel N, and for every space Y, f^*: [B, Y] → [A, Y] is injective with image the classes of maps g
with π₁(g)(N) = 1.

**Theorem 3.1.** Let W be a connected CW complex with one 0-cell, π = π₁(W), and λ an infinite cardinal not less
than the number of cells of W. There are a group G with |G| ≤ λ and a map t: BG → W such that
(i) t is acyclic (an isomorphism on homology with every local coefficient system on W); in particular
τ = π₁(t): G → π is onto;
(ii) every homomorphism from G to a group of cardinality < λ factors through τ.
Consequently, for every space Y all of whose fundamental groups have cardinality < λ, t^*: [W, Y] → [BG, Y] is a
bijection.

*Proof.* Enumerate the cells of dimension ≥ 2 by an ordinal, in non-decreasing order of dimension:
W₁ = W^{(1)}, W_{α+1} = W_α ∪_{a_α} e^{m_α+1} with a_α: S^{m_α} → W_α, m_α ≥ 1, unions at limit ordinals. We build
groups G_α, injective homomorphisms G_α → G_β (α < β) and maps t_α: BG_α → W_α, with t_β|BG_α = t_α, satisfying (i)
and (ii) for (G_α, W_α), with τ_α = π₁(t_α): G_α → π_α = π₁(W_α).

*Start.* G₁ is the free group on the 1-cells and t₁: BG₁ → W₁ a homotopy equivalence; (ii) is empty.

*Successor step.* Let a = a_α: S^m → W_α. Claim: there are a group H′, an acyclic map q: BH′ → S^m and a
homomorphism u: H′ → G_α with t_α∘Bu ≃ a∘q. For m = 1: H′ = Z, q = id, u(1) = g with τ_α(g) the class of the loop a
(τ_α is onto). For m ≥ 2: let E be the homotopy pull-back of S^m → W_α ← BG_α; E → S^m is acyclic and E is
connected; by Kan–Thurston choose H′ and an acyclic map BH′ → E; q is the composite to S^m, and the composite
BH′ → E → BG_α is homotopic to Bu for a homomorphism u. In both cases |H′| ≤ λ. By B.7 choose simple acyclic groups
A′, A″ of cardinality λ and embeddings i′: H′ → A′, i″: H′ → A″. Put P = G_α × A′ and v = (u, i′): H′ → P, which is
injective, and

  G_{α+1} = P *_{H′} A″  (amalgamated along v and i″).

P and A″ embed in the amalgam, so G_α → G_{α+1}, g ↦ (g, 1), is injective, and BG_{α+1} is the double mapping
cylinder of BP ← BH′ → BA″. Define t_{α+1} on it by t_α∘pr₁ on BP, by the cone of q on the mapping cylinder of
BH′ → BA″ (BA″ going to the centre of the new cell), and by the chosen homotopy t_α∘Bu ≃ a∘q on the other
cylinder; then t_{α+1}|BG_α = t_α. *Acyclicity:* for a local system L on W_{α+1} compare the Mayer–Vietoris
sequences of the two double mapping cylinders. On BP: H_*(G_α × A′; L) = H_*(G_α; L) because A′ is acyclic and acts
trivially on L (Lyndon–Hochschild–Serre), and t_α is acyclic. On BH′: q is acyclic. On BA″: L is constant on the
cell and A″ is acyclic. The five lemma gives (i). *No small quotients:* let ρ: G_{α+1} → Λ with |Λ| < λ. ρ is
trivial on A″ and on 1 × A′ (simple groups of cardinality λ). For h ∈ H′, v(h) = (u(h), 1)(1, i′(h)) is identified
with i″(h) ∈ A″, so ρ(u(h), 1) = 1. By (ii) for G_α, ρ|G_α = ρ̄∘τ_α, and ρ̄ kills τ_α(u(H′)), which is trivial for
m ≥ 2 and is the cyclic subgroup generated by the class of the attaching loop for m = 1. By van Kampen ρ̄ factors
through π_{α+1} = π₁(W_{α+1}). Since G_{α+1} is generated by G_α, A′, A″, and τ_{α+1} is trivial on A′ and A″ and
equals G_α → π_α → π_{α+1} on G_α, ρ factors through τ_{α+1}.

*Limit step.* G_γ = ⋃ G_α, t_γ = ⋃ t_α. Homology with local coefficients commutes with these unions, and a
homomorphism from G_γ to Λ factors through colim π_α = π_γ.

*The consequence.* Let N = ker τ. A map g: BG → Y induces G → π₁(Y, g(*)), which factors through τ by (ii); so
every class in [BG, Y] kills N, and the universal property of the acyclic map t gives the bijection. ∎

**Theorem 3.2 (E.17 is true).** Let I be a U-small filtered category and K: I → Cat_hot a diagram of U-small
categories. Suppose H_K(X) = colim_i π₀Fun(X, K_i) sends every functor in W∞ between U-small categories to a
bijection. Then H_K sends every unit η_X: X → Π₁X to a bijection; equivalently (E.17a) the canonical morphism
K → (Π₁K_i)_{i∈I} is an isomorphism in Ind(Cat_hot). So a U-small ind-object of Cat_hot is W∞-invariant if and only
if it is isomorphic to an ind-object of groupoids, and then H_K(X) = colim_i [BX, BΠ₁K_i] depends only on Π₁X.

*Proof.* Let μ be an infinite cardinal with |Mor K_i| ≤ μ for all i. Let H′(Y) = colim_i [Y, BK_i] on Hot. By A.7
the canonical map c_X: H_K(X) → H′(BX) is a bijection for every U-small X, naturally in X.
Fix X. Choose a base object in each component c of X, let π_c be the fundamental group there, and let λ > μ be an
infinite cardinal not less than the number of cells of BX. By 3.1 (applied to a model of the component BX_c with one
0-cell) choose groups G_c, surjections p_c: G_c → π_c and acyclic maps t_c: BG_c → BX_c inducing p_c, such that
every homomorphism from G_c to a group of cardinality < λ factors through p_c. Let 𝒢 = ∐_c BG_c and 𝒫 = ∐_c Bπ_c,
with p: 𝒢 → 𝒫 and the equivalence of groupoids ε: 𝒫 → Π₁X.
(a) p^*: Fun(𝒫, K_i) → Fun(𝒢, K_i) is an isomorphism of categories for every i: a functor 𝒢 → K_i is a family of
objects k_c with homomorphisms G_c → Aut(k_c), and |Aut(k_c)| ≤ μ < λ, so these factor uniquely through p_c; a
natural transformation is a family of arrows satisfying conditions that are the same for G_c and for its quotient
π_c. Hence H_K(p) is a bijection, and so is H′(Bp) (c is natural).
(b) t = ∐ t_c: B𝒢 → BX induces bijections [BX, BK_i] → [B𝒢, BK_i] for every i, by the last statement of 3.1 (the
fundamental groups of BK_i have cardinality ≤ μ). Hence H′(t) is a bijection.
(c) Bη_X∘t = Bε∘Bp in Hot: both are maps from B𝒢 into the classifying space of a groupoid inducing the same functor
on fundamental groupoids up to isomorphism, and C.1 applies.
So H′(t)∘H′(Bη_X) = H′(Bp)∘H′(Bε) is a bijection and H′(t) is a bijection; therefore H′(Bη_X) is a bijection, and
by naturality of c so is H_K(η_X). The rest is (E.17a), that is, A.4 for the reflection Π₁ ⊣ j of C.4. ∎

**Corollary 3.3 (what this says about V ms. 44–46, VII ms. 129–132, IX ms. 22–23).**
(a) Grothendieck's sentence at V ms. 46, "cela équivaut à la condition qu'il puisse se représenter par un système
inductif sur N formé de catégories de Thomason–Kan", is a theorem when "catégorie de Thomason–Kan" is read as
"local category" (C.3): a sequence (K_n) has a W∞-invariant functor exactly when it is ind-isomorphic to the
sequence of groupoids (Π₁K_n). With "Thomason-fibrant" it is false (C.6).
(b) Consequently an invariant functor only sees fundamental groupoids: H(X) = H(Π₁X). For the path ind-categories
H(a, b) = (Ch_{n,Σ}(a, b))_n of a U-small (M, Σ), the "condition préalable" of VII ms. 129–132 and test (b) of IX
ms. 22, imposed on all of Cat_U, forces Hom_{M(Y)Σ_Y^{-1}}(a_Y, b_Y) to depend only on Π₁Y; in particular it equals
Hom_{MΣ^{-1}}(a, b) for every simply connected Y. (This uses Grothendieck's description of these Hom-sets as
colim_n π₀Fun(Y, Ch_{n,Σ}(a, b)), V ms. 45, which I did not re-derive.) So for small (M, Σ) the condition can hold
only when the derived mapping spaces are, as ind-objects, 1-types: a precise form of his remark that the condition
"n'est pratiquement jamais satisfaite" (VII ms. 132) and of his doubt at IX ms. 23.
(c) The filtered case of D.8 of the return (the functor [B−, Y] is a U-small filtered colimit of representables
only if Y is a 1-type) follows: if [B−, Y] = H_K, then by 3.2 the map [P₁Y′, Y] → [Y′, Y] is bijective for all Y′;
for Y′ = Y the identity of Y factors through Y → P₁Y, so Y is a retract in Hot of a 1-type, hence a 1-type.
(d) The size restriction on I is necessary (D.7 of the return).

*Where an error could hide.* In the successor step of 3.1 (the construction of t_{α+1} and the Mayer–Vietoris
comparison with local coefficients), and in the cardinality claim for the Kan–Thurston group. The use of
Kan–Thurston is confined to cells of dimension ≥ 3.

*Provenance, added after the comparison with the earlier review.* The reduction of E.17 to a Kan–Thurston statement
without small quotients was also written down in the earlier review of this return (Claude Fable 5.2, effort
medium, 10 Nov 2026: `pro_reviews_20261110/1_CATHOT/REVIEW.md`, "A reduction for E.17", statement (KT_μ)), which I
opened only after finishing my own review; it expected the statement to follow from Maunder's proof of the
Kan–Thurston theorem and did not prove it. Its deduction of E.17 from (KT_μ) uses only that acyclic maps are
epimorphisms in the homotopy category, which is enough. Theorem 3.1 above is a proof of (KT_μ).

## 4. A criterion for uncountably many maps to S² (towards D.6)

**Proposition 4.1.** Let X be a connected CW complex with H¹(X; Z) = 0. Suppose that for infinitely many n with
π_n(S³) ≠ 0 the sphere Sⁿ is a homotopy retract of X: there are maps s_n: Sⁿ → X and f_n: X → Sⁿ with f_n∘s_n of
degree ±1. Then [X, S³] and [X, S²] are uncountable.

(π_n(S³) ≠ 0 for n = 2p, p prime, by Serre: the p-primary component of π_{2p}(S³) is Z/p.)

*Proof.* Let N be the set of such n. Take f_n and s_n cellular for the cell structure of Sⁿ with one 0-cell and
one n-cell; then f_n(X^{(n−1)}) is the base point. Choose pointed maps a_n: Sⁿ → S³ representing non-zero classes,
with base point 1 ∈ S³ = SU(2), and put g_n = a_n∘f_n. For A ⊂ N define g_A(x) = ∏_{n∈A} g_n(x), the product in
increasing order in the group S³; on X^{(k)} only the factors with n ≤ k differ from 1, so g_A is continuous. Let
A ≠ A′ and n = min(A △ A′), say n ∈ A. On X^{(n)}: g_A = h·g_n and g_{A′} = h, with h the product of the common
factors of index < n. If g_A ≃ g_{A′}, then h·g_n ≃ h on X^{(n)}, hence g_n|X^{(n)} is null-homotopic
(multiply pointwise by h⁻¹), hence g_n∘s_n = a_n∘f_n∘s_n is null-homotopic; but it represents ± the class of a_n
(free and pointed classes agree in S³). So A ↦ [g_A] is injective on the subsets of N. For S²: the Hopf map
S³ → S² is a principal S¹-bundle, so two maps X → S³ with homotopic images in S² differ, after a homotopy, by a
map X → S¹, which is null-homotopic because H¹(X; Z) = 0; thus [X, S³] → [X, S²] is injective. ∎

**Corollary 4.2.** If a finite category C has BC ≃ ⋁_{n≥2} Sⁿ, or more generally has S^{2p} as a homotopy retract
for infinitely many primes p, and H¹(BC; Z) = 0, then [BC, S²] is uncountable, and by D.4 of the return the functor
X ↦ [BX, S²] on finite categories is not ind-representable by a sequence of finite categories. Whether such a C
exists is hunch H3 of `HUNCHES.md` (candidate: the six-element monoid of Sweeney's Example 5.2).

## 5. Posets of type RP²: at least 34 arrows

The return (G.8) proves 28 ≤ a_pos(RP²) ≤ 49 for the least number of arrows (pairs x ≤ y) of a poset whose order
complex has the homotopy type of RP².

**Proposition 5.1.** a_pos(RP²) ≥ 34.

*Proof.* Let P be such a poset with the least number of arrows; it is finite. As in G.8, its comparability graph
has no vertex of degree ≤ 1 (a vertex with one neighbour is a beat point and can be removed), and P has at least 13
points (Cianci–Ottina, arXiv:1512.06088v1, Corollary 5.8). If P has exactly 13 points it has 49 arrows (their
Theorem 5.10). Otherwise f₀ ≥ 14. The order complex Δ is a flag complex with H̃₂(Δ; F₂) ≠ 0. By the argument of
G.7 over F₂ (take a full subcomplex L minimal with H̃₂(L; F₂) ≠ 0; Mayer–Vietoris gives H̃₁(lk_L v; F₂) ≠ 0 for
each vertex v of L, and links in flag complexes are flag), every vertex of L has at least 4 neighbours in L and L
has at least 6 vertices. Summing degrees: 2f₁ ≥ 4|L| + 2(f₀ − |L|), so f₁ ≥ f₀ + |L| ≥ f₀ + 6, and the number of
arrows is f₀ + f₁ ≥ 2f₀ + 6 ≥ 34. ∎

## 6. The census of small categories (computational; my own programs in `work/code/`)

**Statement 6.1.** (a) The numbers of monoid structures on {0, …, n−1} with identity 0 are 1, 2, 11, 156, 4,122,
208,672 for n = 1, …, 6, in 1, 2, 6, 27, 156, 1,373 classes up to isomorphism and anti-isomorphism.
(b) The triples (H₁, H₂, H₃) of BM that occur for monoids of order 6 are (0,0,0) [1,159 classes], (0,Z,0) [2],
(0,Z,Z) [1], (0,Z,Z/2) [2], (0,Z/2,0) [1], (Z/2,0,Z/2) [172], (Z/3,0,Z/3) [22], (Z/4,0,Z/4) [6], (Z/5,0,Z/5) [1],
(Z/6,0,Z/6) [1], (Z/2,0,Z/6) [1], ((Z/2)²,Z/2,(Z/2)³) [5]; for order 5: (0,0,0) [126], (0,Z,0) [1, the monoid P₂],
(Z/2,0,Z/2) [22], (Z/3,0,Z/3) [4], (Z/4,0,Z/4) [1], (Z/5,0,Z/5) [1], ((Z/2)²,Z/2,(Z/2)³) [1].
(c) Connected categories with k ≥ 2 objects and N arrows, as labelled tables with arrows sorted by (source,
target): N = 3: 2; N = 4: 11; N = 5: 76 + 6 (k = 2, 3); N = 6: 977 + 54; N = 7: 22,798 + 498 + 32 (k = 2, 3, 4).
None has (H₁, H₂, H₃) = (0, 0, Z); none with N ≤ 5 has H₂ = Z; exactly the two labellings of the parallel pair
have (Z, 0, 0) with N = 4; none with N ≤ 7 has (Z/2, 0, 0).
(d) Hence: the categories of type S¹, S², S³ with the fewest arrows have 4, 5, 7 arrows; for S¹ it is the parallel
pair, for S² the monoid P₂ (unique up to isomorphism), and for S³ every such category is a monoid of order 7
(P₃ is one).
(e) The six classes of monoids of order 6 with H₁ = 0 and H₂ ≠ 0 have mod-p Betti numbers in degrees 1–5 as listed
in `work/code/higher_homology_order6.out`; none has the Betti numbers of CP^∞ (0,1,0,1,0).

Method: backtracking over composition tables with associativity checks (`catlib.py`), canonical forms under
relabelling and transposition, exact Smith normal forms of the normalized nerve boundaries (python-flint). Checks
of the method: the counts in (a) are the known ones; group homology of C_k, C₂², S₃; the nerves of the parallel
pair, of Grothendieck's category Z of XII app. ms. 10–11 (homology of S²), of R₂ (RP²), of P₂ and P₃.
