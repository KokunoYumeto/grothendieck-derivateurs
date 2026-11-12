## Entry 1

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


## Entry 2

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

## Entry 3

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


## Entry 4

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


## Entry 5

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

## Entry 6

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

## Entry 7

## 1. Statement

Notation as in POLES: a fundamental localizer is a class `W` of functors satisfying identities, two out of three,
the retraction rule, the terminal-object axiom and the relative Theorem A. `W` is *reversible* when it satisfies
Loc (6′ b) (XVI ms. 17′; W(7 bis) "⇐" of XII ms. 76), equivalently (POLES B.5) when `g ∈ W ⇔ C(g)` is
`W`-aspherical, `C(g)` the unreduced homotopy cofibre of `Bg`, pointed at the cone point. For a localizing
subcategory `L` of `Ho(Sp)`, `R(L) = {g : Σ^∞ C(g) ∈ L}` (POLES F.2), and `T(W) = loc{Σ^∞ C(g) : g ∈ W}`.

Let `S_n` denote the 2-localization of the sphere `S^n`, and let

    𝔑 = { pointed spaces X : Map_*(X, S_n) is weakly contractible for every n ≥ 2 },
    W_S = { functors g : C(g) ∈ 𝔑 }.

**Theorem.** (a) `W_S` is a fundamental localizer, it is reversible (so it satisfies Loc (6 a, b, c), W(7),
W(7 bis)), and it is not `Fl(Cat)`. (b) `RP^∞ → e` is in `W_S` and `RP² → e` is not. (c) Every reversible
fundamental localizer `W` that contains `RP^∞ → e` has `Σ^∞ RP² ∈ T(W)`, so `RP² → e ∈ RT(W)`. Hence
`W_S ≠ RT(W_S)`: `W_S` is not of the form `R(L)`, and in particular is not a homology localizer `W_E`.
The same holds for every reversible localizer between the one generated by `RP^∞ → e` and `W_S`.

So the reversible cofibration axiom of Grothendieck does not force a localizer to be "stable" or homological.

## 2. The class 𝔑 is closed under desuspension

**Lemma 1.** If `ΣX ∈ 𝔑` then `X ∈ 𝔑`.

*Proof.* James: for every `n ≥ 1` there is, after localization at 2, a fibre sequence
`S^n → ΩS^{n+1} → ΩS^{2n+1}` (`E` followed by the Hopf–James invariant `H`); so for `n ≥ 2` a fibre sequence

    Ω² S_{2n+1} --P--> S_n --E--> Ω S_{n+1}.

Let `φ: X → S_n` be pointed. `Eφ` is adjoint to a map `ΣX → S_{n+1}`, which is null because
`Map_*(ΣX, S_{n+1})` is weakly contractible. So `φ ≃ Pψ` with `ψ: X → Ω² S_{2n+1}`, and `ψ` is adjoint to an
element of `π_1(Map_*(ΣX, S_{2n+1}), const) = 0`. So `φ` is null: `π_0 Map_*(X, S_n) = *`. For `j ≥ 1`,
`π_j(Map_*(X, S_n), const) = π_{j−1}(Map_*(ΣX, S_n), const) = 0`. ∎

**Lemma 2.** (i) `𝔑` is closed under pointed homotopy colimits and retracts and contains the contractible
spaces. (ii) For a cofibre sequence `X → Y → C` of pointed spaces, if two of `X, Y, C` are in `𝔑`, so is the
third. (iii) `X ∈ 𝔑 ⇔ ΣX ∈ 𝔑`. (iv) If `X ∈ 𝔑` then `X ∧ Y_+ ∈ 𝔑` and, if also `Y ∈ 𝔑`, `X × Y ∈ 𝔑`.

*Proof.* (i) `Map_*(hocolim X_i, Z) = holim Map_*(X_i, Z)`. (ii) Use the fibre sequences
`Map_*(C, Z) → Map_*(Y, Z) → Map_*(X, Z)` and `Map_*(ΣX, Z) → Map_*(C, Z) → Map_*(Y, Z)`, with
`Map_*(ΣX, Z) = Ω Map_*(X, Z)`: `X, C ∈ 𝔑 ⇒ Y ∈ 𝔑`; `X, Y ∈ 𝔑 ⇒ C ∈ 𝔑`; `Y, C ∈ 𝔑 ⇒ ΣX ∈ 𝔑` (from
`C → ΣX → ΣY`), and then `X ∈ 𝔑` by Lemma 1. (iii) `ΣX` is the cofibre of `X → *`; Lemma 1.
(iv) `Map_*(X ∧ Y_+, Z) = Map(Y, Map_*(X, Z))`; then `Y → X × Y → X ∧ Y_+`. ∎

## 3. `W_S` is a reversible fundamental localizer

For `f: X → Y`, `g: Y → Z` there is a cofibre sequence `C(f) → C(gf) → C(g)` whose connecting map is
`C(g) → ΣY → ΣC(f)`.

- Identities: `C(id)` is a cone. Two out of three: Lemma 2 (ii).
- Retraction rule. Let `ri = id_X`, `ir ∈ W_S`, `D = C(i)`. From `C(i) → C(ri) ≃ * → C(r)`: `C(r) ≃ ΣD`. In
  `C(r) → C(ir) → C(i) --δ--> ΣC(r)` the map `δ` factors through the connecting map `∂: C(i) → ΣX` of `i`, and
  `∂ ≃ (Σr)(Σi)∂ ≃ *` because `(Σi)∂ ≃ *`. So `ΣC(ir) ≃ Σ²D ∨ ΣD`. As `C(ir) ∈ 𝔑`, the retract `ΣD` is in `𝔑`,
  so `D ∈ 𝔑` (Lemma 1): `i ∈ W_S`, and `r ∈ W_S` by two out of three.
- A category with a terminal object has contractible nerve.
- Relative Theorem A. For `u: A → B` over `C` with all `u/c ∈ W_S`: `BA ≃ hocolim_c B(A/c)`,
  `BB ≃ hocolim_c B(B/c)` naturally, and `C(Bu)` is the pointed homotopy colimit over `C` of the `C(B(u/c))`
  (the unpointed one, with the section `BC` of cone points collapsed). Lemma 2 (i).
- Reversible: `X → e ∈ W_S ⇔ ΣX ∈ 𝔑 ⇔ X ∈ 𝔑` (Lemma 2 (iii)); so the `W_S`-aspherical categories are those
  with nerve in `𝔑` (for any base point), and `g ∈ W_S ⇔ C(g) ∈ 𝔑 ⇔ C(g)` is `W_S`-aspherical. By POLES B.5
  this is Loc (6 b), and Loc (6 c), W(7) follow.
- `S² → e ∉ W_S` (the identity of `S_2`), so `W_S ≠ Fl(Cat)`. Acyclic spaces are in `𝔑` (the `S_n` are simply
  connected, hence `HZ`-local), in accordance with `W_Z ⊂ W_S` (POLES B.6).

## 4. `RP^∞`, `RP²`, and the stable side

(b) Miller's theorem (the Sullivan conjecture): `Map_*(BG, K)` is weakly contractible for `G` finite and `K` a
finite complex; for `K = S^n` and the 2-localization `S_n` use the arithmetic square (`RP^∞` is rationally
acyclic and maps from `BZ/2` into a simply connected space see only its 2-completion). So `RP^∞ ∈ 𝔑`. On the
other hand `[RP², S_2] = H²(RP²; Z_(2)) = Z/2 ≠ 0`, so `RP² ∉ 𝔑`.

(c) Let `W` be reversible with `RP^∞ → e ∈ W`, `A` its class of aspherical pointed spaces, `L = T(W)`. Then
`Σ^∞ A ⊂ L`, `L` is a tensor ideal (POLES F.13), and:
1. `Σ^∞ K(Z/2, n) ∈ L` for all `n`: `K(Z/2, n+1)` is the bar construction of `K(Z/2, n)`, a pointed homotopy
   colimit of finite products, and `Σ^∞(X × Y) = Σ^∞X ∨ Σ^∞Y ∨ Σ^∞(X ∧ Y)`. Hence
   `HZ/2 = colim_n Σ^{−n} Σ^∞ K(Z/2, n) ∈ L`.
2. Snaith: `Σ^∞ Q(RP^∞) ≃ ⋁_j Σ^∞ D_j(RP^∞)`, and `Σ^∞ D_j X = (Σ^∞ X)^{∧ j}_{hΣ_j} ∈ L`. Kahn–Priddy: the
   2-localization of `Q_0 S⁰` is a retract, as a space, of `Q(RP^∞)`. So `Σ^∞ (Q_0 S⁰)_(2) ∈ L`. Its iterated
   bar constructions are the spaces of the spectrum `τ_{≥1} S_(2)`; as in 1, `τ_{≥1} S_(2) ∈ L`.
3. Smashing `τ_{≥1} S_(2) → S_(2) → HZ_(2)` with the Moore spectrum: `(τ_{≥1} S_(2))/2 → S/2 → HZ/2`. So
   `S/2 ∈ L`, i.e. `Σ^∞ RP² ∈ L`, and `RP² → e ∈ R(L) = RT(W)`.
Applied to `W = W_S`: `RP² → e ∈ RT(W_S) ∖ W_S`. ∎

Remark. Step (c) shows `loc(Σ^∞ RP^∞) = loc(S/2)`, the 2-torsion spectra; so `RT` of the reversible localizer
generated by `RP^∞ → e` is the localizer of `Z[1/2]`-homology equivalences.



## Entry 8

F-G1 (mine). **XII Théorème 2 (ms. 78), "`W∞` satisfait à W(7)", is false**, and so is the reverse half of
  W(7 bis) for `W∞`: `X = A ⋆ {t, s}` with `A` connected, acyclic, not aspherical. Grothendieck did not write the
  verification ("je devrais sans doute réparer cette omission"). Everything in XII that uses "W(7 bis) forme forte"
  (his own footnotes 104, 105 mark these places: Th. 4 Cor. 4 and 5; also the Corollary of ms. 85, Prop. 7, and
  the uses at ms. 105, XIIapp ms. 7 and 15) holds for homology localizers and not for `W∞`. (Also in TOTASPH A.13;
  it is the starting point of POLES.)

Own check of the data: 3 + 17 + 15 simplices; arrows 35 + 34 + 45 + 45 = 159; nerve ranks (35, 124, 90). `d_2 = [[5, −2], [−3, 1]]`, determinant −1 (exponent sums of `a⁵b⁻³` and `b³(ab)⁻²`). In `A_5`: `a = (1 4 3 2 5)`, `b = (1 2 3)`, `ab = (1 5)(3 4)` (I composed them), so both relators die and `a ≠ 1`. Hatcher's Example 2.38 is the binary icosahedral presentation.

`X = A ⋆ {u, t}`: `U = A ∪ {u}`, `V = A ∪ {t}` are sieves with contractible nerves, `BX = ΣBA` is contractible (simply connected and acyclic), `U ∩ V = A` is not. I had found the same counterexample independently while reading XII ms. 78. **This refutes XII Théorème 2 (ms. 78)** as stated; only the direct halves hold. Consequence I add: in II ms. 36ter (Contre-exemple 2.20) the step "`i ∈ W∞` ⇒ `X/H` aspherical" is not available; one gets only that `X/H` is connected and acyclic. The counterexample 2.20 survives (take `H` connected with `ΣB(Δ/H)` not contractible).

## Entry 9

**F3-5 (mine). Direct proof that `W_Z` and `W_k` fail (7 F)** (trefoil complement over a base of type `S¹`;
  the Alexander module appears in `H_1` of the base change). Independent of Cisinski's properness theory.

**Independent confirmation for `W_Z` and `W_k`, `k` a field** (my argument before reading, `work\checks_3\own_thoughts_before_reading.md` item 7, not using E.2): if `e → E → S` with `BS ≃ S¹`, `E` acyclic and `p ∈ Fib_W`, the local system `s ↦ H_0(E/s)` must be `Z[t, t⁻¹]`, and base change along a functor `Y' → S` realizing the map from the trefoil complement to `S¹` gives `H_1(E ×_S Y') ↠ Z[t, t⁻¹]/(t² − t + 1) ≠ 0`, although `E ×_S Y' → E` should be a homology isomorphism. This answers XVI 7.5 (ms. 105): **Loc (6 a, 8, 9) does not imply Loc (7 F)**; and it answers the wish of XVI ms. 124 ("regarder quelques exemples (équivalences homologiques ou cohomologiques, `W_n`) … si Loc (7 F) est satisfait").

## Entry 10

F2-11 (mine). C005 (XII ms. 103) follows from Grothendieck's own remarks: the endpoint functor of
  `Ch(Y; y_0, −)` is final when `Y` is 1-connected (ms. 102–103), totality passes to final images (Lemma, ms. 112),
  and `Ψ` is aspherical and not total (his footnote at ms. 103). General form: for `Y` simply connected,
  `Ch(Y; y_0, −)` total ⇒ `Y` total. Open: the converse, starting with `Y = e` (the category of interval types).

## Entry 11

\subsection{An intrinsic criterion and the failure of Lead 4}

\begin{definition}[Proved: the action criterion]\label{C:action-definition}
Let $R$ be a nonzero commutative ring with identity. We write $\mathcal P_R(A)$ for the following property of a small category $A$: for every covariant functor $H:A\to\Set$, each connected component $E$ of the category of elements $\operatorname{El}_A(H)$ is $R$-acyclic, meaning that $H_0(BE;R)=R$ and $H_j(BE;R)=0$ for $j>0$. No condition is imposed on the empty category of elements. We write $\mathcal P_\infty(A)$ when every such component is weakly contractible. These definitions use covariant, rather than presheaf, categories of elements: an arrow $(a,h)\to(a',h')$ is an arrow $v:a\to a'$ with $H(v)(h)=h'$.
\end{definition}

\begin{lemma}[Proved: homological Theorem A in the final variance]\label{C:homology-A}
Let $f:A\to B$ be a functor. If every $b\backslash A$ is nonempty and $R$-acyclic, then $Bf:BA\to BB$ induces an isomorphism on homology with coefficients in $R$. More generally, if every $b\backslash A$ is nonempty and its reduced $R$-homology vanishes in degrees $0,\ldots,d-1$, for an integer $d\geq1$, then $Bf$ induces isomorphisms in degrees less than $d$ and an epimorphism in degree $d$.
\end{lemma}
\begin{proof}
We use the bisimplicial set whose $(p,q)$-simplices are strings
\[
 b_0\longrightarrow\cdots\longrightarrow b_p
 \longrightarrow f(a_0),\qquad
 a_0\longrightarrow\cdots\longrightarrow a_q.
\]
The forgetful map to $NA$ is a weak equivalence after diagonal realization: for a fixed string in $A$, the remaining simplicial direction is the nerve of $B/f(a_0)$, which has terminal object $\id_{f(a_0)}$. The other projection is to $NB$. Taking normalized $R$-chains in both directions and filtering by $p$ gives the spectral sequence of this projection. Its row in degree $q=0$ is the chain complex of $NB$, because each comma category is connected; the rows in degrees $1,\ldots,d-1$ vanish after taking vertical homology. The first possible additional row has degree $d$. Thus the projection induces isomorphisms below degree $d$ and an epimorphism in degree $d$. The first-quadrant filtration is finite in each total degree, so it converges without a boundedness or finiteness assumption on the categories. If all positive rows vanish, it induces isomorphisms in every degree. The two projections commute with the canonical map $Bf$ up to the homotopy supplied by the displayed arrow $b_p\to f(a_0)$; consequently the comparison just computed is the map induced by $f$.
\end{proof}

\begin{lemma}[Proved: inheritance by categories of elements]\label{C:inherit-elements}
If $A$ satisfies $\mathcal P_R$, then every connected component $E$ of $\operatorname{El}_A(H)$, for every $H:A\to\Set$, also satisfies $\mathcal P_R$. The corresponding assertion holds for $\mathcal P_\infty$.
\end{lemma}
\begin{proof}
The elements lying in $E$ define a subfunctor $H_E\subseteq H$, because arrows preserve connected components. Let $K:E\to\Set$ be any covariant functor. Define
\[
 L(a)=\coprod_{h\in H_E(a)}K(a,h).
\]
For an arrow $v:a\to a'$ in $A$, its restriction to the summand indexed by $h$ is the map $K(v):K(a,h)\to K(a',H(v)h)$, landing in the indicated summand of $L(a')$. This defines a covariant functor $L:A\to\Set$. The map
\[
 ((a,h),k)\longmapsto (a,(h,k))
\]
is an isomorphism of categories $\operatorname{El}_E(K)\cong\operatorname{El}_A(L)$, including their specified arrows. Its connected components therefore have the required property.
\end{proof}

\begin{lemma}[Proved: integral acyclicity detects every cyclic subgroup]\label{C:cyclic-covers}
Suppose that a connected, nonempty small category $E$ satisfies $\mathcal P_{\mathbb Z}$. Then $BE$ is weakly contractible. Consequently $\mathcal P_{\mathbb Z}(A)$ and $\mathcal P_\infty(A)$ are equivalent for every small category $A$.
\end{lemma}
\begin{proof}
The constant singleton functor on $E$ shows that $BE$ is integrally acyclic. Fix an object $e_0$ and let $\Pi E$ be the groupoid obtained by inverting all arrows of $E$. The usual edge-path presentation of the fundamental group identifies $\operatorname{Aut}_{\Pi E}(e_0)$ with $G=\pi_1(BE,e_0)$. For any subgroup $K\leq G$, define
\[
 H_K(e)=\operatorname{Hom}_{\Pi E}(e_0,e)/K,
\]
where $K$ acts by precomposition, and an arrow $v:e\to e'$ acts by postcomposition with its image in $\Pi E$. All these maps are bijections. The projection $\operatorname{El}_E(H_K)\to E$ is therefore a categorical covering: each arrow has a unique lift with either a prescribed source or a prescribed target. On nerves this gives the usual covering of $BE$ whose monodromy is the transitive coset action of $G$. It is connected, and its fundamental group, at the lift represented by $\id_{e_0}$, is precisely $K$. The covering classification is also recorded in \citet[Theorem~1.38]{Hatcher2002}. These assertions follow directly here by lifting the edge-path presentation; a loop lifts to a loop exactly when its class belongs to $K$.

Take $K$ to be the cyclic subgroup generated by an arbitrary element of $G$. The hypothesis gives
\[
 0=H_1\bigl(B\operatorname{El}_E(H_K);\mathbb Z\bigr)
   =K_{\mathrm{ab}}=K.
\]
The identification of first homology with abelianization is \citet[Theorem~2A.1]{Hatcher2002}. Thus $G$ is trivial. A simply connected acyclic CW complex is weakly contractible: if a first nonzero homotopy group existed, the Hurewicz theorem would identify it with a nonzero homology group \citep[Theorem~4.32]{Hatcher2002}. A nerve realization is a CW complex, so this applies to $BE$.

For general $A$ satisfying $\mathcal P_{\mathbb Z}$, apply Lemma~\ref{C:inherit-elements} and the preceding argument to each component $E$ of each category of elements. The converse follows from homotopy invariance of integral homology.
\end{proof}

\begin{theorem}[Proved: characterization of total asphericity]\label{C:classification}
For every small category $A$, the following conditions are equivalent:
\begin{enumerate}
\item $A$ is totally $\Winfty$-aspherical in the sense of XII, Definition~1.
\item $A$ is totally $W_{\mathbb Z}$-aspherical.
\item $A$ is nonempty and connected, and satisfies $\mathcal P_{\mathbb Z}$.
\item $A$ is nonempty and connected, and satisfies $\mathcal P_\infty$.
\end{enumerate}
In particular, this is a criterion in terms of all covariant set-valued diagrams on $A$, involving no quantification over target categories or final functors. Moreover every connected component of every $\operatorname{El}_A(H)$ is itself totally $\Winfty$-aspherical whenever $A$ is totally $\Winfty$-aspherical.
\end{theorem}
\begin{proof}
The implication (1)$\Rightarrow$(2) follows because a weak homotopy equivalence induces an integral homology isomorphism. Assume (2). The identity functor is final, so $A$ is integrally acyclic and hence nonempty and connected. For any connected nonempty category of elements, the collage of Part~B is a final image of $A$. Its homotopy-pushout description gives the homology exact sequence
\[
 \cdots\to\widetilde H_{j+1}(BA_H;\mathbb Z)
 \to\widetilde H_j(B\operatorname{El}_A H;\mathbb Z)
 \to\widetilde H_j(BA;\mathbb Z)\to\cdots.
\]
Both outside terms vanish. For a component of an arbitrary $H$, first replace $H$ by its component subfunctor. This proves (3). Lemma~\ref{C:cyclic-covers} proves (3)$\Rightarrow$(4).

Assume (4), and let $f:A\to B$ be any ordinary final functor. For $b\in B$, the category $b\backslash A$ is the category of elements of the covariant functor $a\mapsto\operatorname{Hom}_B(b,f(a))$. It is connected and nonempty by finality, and therefore weakly contractible by the hypothesis. Quillen's Theorem~A \citep[Section~1, Theorem~A]{Quillen1973} implies that the specified map $Bf$ is a weak homotopy equivalence. The constant singleton functor in (4) makes $BA$ weakly contractible. Thus $BB$ is weakly contractible, proving (1) by the comprehensive-factorization criterion. The final assertion follows from Lemma~\ref{C:inherit-elements} and (4).
\end{proof}

\begin{proposition}[Proved: exact integral colimits are sufficient]\label{C:exact-sufficient}
Let $A$ be nonempty and connected. If $\colim_A:\Ab^A\to\Ab$ is exact, then $A$ is totally $\Winfty$-aspherical.
\end{proposition}
\begin{proof}
For $H:A\to\Set$, define $\Sigma_H:\Ab^{\operatorname{El}_A(H)}\to\Ab^A$ by
\[
 (\Sigma_HF)(a)=\bigoplus_{h\in H(a)}F(a,h),
\]
with the transition maps specified in the proof of Lemma~\ref{C:inherit-elements}. It is exact because direct sums of abelian groups are exact. The universal property of a cocone gives the canonical natural isomorphism
\[
 \colim_{\operatorname{El}_A(H)}F
   \cong\colim_A\Sigma_HF.
\]
Thus the colimit functor on each category of elements is exact, and the same is true on any one of its components, by extending diagrams by zero on the other components. The bar resolution computing derived colimits identifies
$L_j\colim_E\underline{\mathbb Z}$ with $H_j(BE;\mathbb Z)$: its term in degree $j$ is the free abelian group on strings of $j$ composable arrows of $E$, and its differential is the alternating sum of the nerve faces. Exactness therefore makes every component $E$ integrally acyclic. Now apply Theorem~\ref{C:classification}.
\end{proof}

\subsection{An explicit nonfiltered totally aspherical category}

\begin{definition}[Proved: the category of injective ordinals]\label{C:delta-definition}
Let $\Delta_{\mathrm{inj}}$ have objects $[n]=\{0,\ldots,n\}$ for $n\geq0$, and all strictly increasing functions as arrows, with ordinary composition of functions. This is a countable small category. In the next construction $\mathbb Z[S]$ denotes the free abelian group on a set $S$, and the augmentation of a finite linear combination of arrows is the sum of its coefficients.
\end{definition}

The exact-colimit example is attributed to \citet{Isbell1974Exact} in \citet[Section~2.3, after Theorem~2.5]{Husainov2002Dimension}; its bibliographic record was verified, but the original article's body was not available in this run. We do not use that unavailable body as a proof. The following explicit verification uses polynomial interpolation. A CC0 AI-authored exposition containing the construction was found during the literature search \citep[Section~4]{OpenMaths2026Derived}; we independently verify its algebraic identities here and by the accompanying program \texttt{cd\_affine\_polynomials.py}. Its provenance is recorded in the report, and it is not used as an authority.

\begin{lemma}[Proved: interpolation on coordinate hyperplanes]\label{C:interpolation}
Let $F_0,\ldots,F_n$ be polynomials in $\mathbb Z[x_0,\ldots,x_n,u]$ such that $F_i-F_j\in(x_i,x_j)$ for every pair $i,j$. There exists $C$ in this polynomial ring with $C-F_i\in(x_i)$ for every $i$. If all $F_i$ are homogeneous of the same degree, $C$ can be chosen homogeneous of that degree.
\end{lemma}
\begin{proof}
For a subset $S\subseteq\{0,\ldots,n\}$ let $\rho_S$ set $x_i=0$ for $i\in S$. For $S\ne\varnothing$, the value $\Phi_S=\rho_S(F_i)$ is independent of the choice of $i\in S$: the difference of two choices belongs to $(x_i,x_j)$ and is killed by $\rho_S$. Set
\[
 C=\sum_{\varnothing\ne S\subseteq\{0,\ldots,n\}}
       (-1)^{|S|+1}\Phi_S.
\]
Modulo $(x_j)$ the terms indexed by $S$ and $S\cup\{j\}$ cancel whenever $j\notin S$ and $S\ne\varnothing$. The remaining term is $\Phi_{\{j\}}$, congruent to $F_j$. All substitutions preserve homogeneity.
\end{proof}

\begin{lemma}[Proved: normalized affine cones]\label{C:affine-cones}
For every $n\geq0$ there are an integer $M\geq n$ and
\[
 t\in\mathbb Z[\operatorname{Hom}_{\Delta_{\mathrm{inj}}}([n],[M])]
\]
of augmentation $1$ such that $th=th'$ whenever $h,h':[m]\to[n]$ are parallel arrows. Here composition is extended bilinearly in the free preadditive category. For $n\geq1$ one can take $M=2^{n+1}-2$.
\end{lemma}
\begin{proof}
We prove a polynomial assertion simultaneously for all integers $k\geq1$. For variables $z_0,\ldots,z_{n+1}$, let $D_i$ identify $z_i$ and $z_{i+1}$ and relabel the remaining variables in order as $y_0,\ldots,y_n$. We claim that there is a homogeneous integral polynomial $C_{n,k}$ with value $1$ when all variables are $1$, such that $y_i^kD_i(C_{n,k})$ is independent of $i$.

For $n=0$, use $C_{0,k}=1$. Assume the assertion for $n-1$ and all $k$. Let $Q=C_{n-1,2k}$, expressed in the variables $y_0,\ldots,y_n$, and prescribe
\[
 D_i(C_{n,k})=F_i:=Q\prod_{l\ne i}y_l^k.
\]
These prescriptions agree on every pairwise intersection of the hyperplanes $z_i=z_{i+1}$. Indeed, for $i<j$, one must check $D_{j-1}(F_i)=D_i(F_j)$. If $j=i+1$, both omitted-variable products become $\prod_lw_l^k$ and the images of $Q$ agree. If $j\geq i+2$, put $p=i$, $q=j-1$. The two expressions are respectively
\[
 w_q^{2k}D_q(Q)\prod_{l\ne p,q}w_l^k,
 \qquad
 w_p^{2k}D_p(Q)\prod_{l\ne p,q}w_l^k,
\]
and are equal by induction. Choose homogeneous polynomial lifts of the $F_i$. The change of coordinates
$x_i=z_i-z_{i+1}$, $u=z_{n+1}$ is invertible over $\mathbb Z$; the kernels of the $D_i$ are the coordinate ideals $(x_i)$. Lemma~\ref{C:interpolation} therefore supplies $C_{n,k}$. It has value $1$ at the all-ones point, and the required common expression is $Q\prod_l y_l^k$. Its degree satisfies
\[
 d(n,k)=d(n-1,2k)+nk=k(2^{n+1}-n-2).
\]

For an injection $g:[n]\to[M]$, let its gaps be
\[
 e_0=g(0),\quad e_i=g(i)-g(i-1)-1\ (1\leq i\leq n),
 \quad e_{n+1}=M-g(n).
\]
This gives a bijection between injections and monomials of degree $M-n$ in $z_0,\ldots,z_{n+1}$. Extend it linearly, writing $P_t$ for the polynomial of an arrow combination $t$. If $\delta^i:[n-1]\to[n]$ omits $i$, deleting $g(i)$ merges two gaps and the deleted point; hence
\[
 P_{t\delta^i}=y_iD_i(P_t).
\]
Take $P_t=C_{n,1}$ and $M=n+d(n,1)$. Its augmentation is $1$, and all $t\delta^i$ agree.

We finally check that this equalizes every parallel pair, rather than just the cofaces. If their common value is $s$, the relation
$\delta^{b+1}\delta^a=\delta^a\delta^b$ for $a\leq b$ gives $s\delta^a=s\delta^b$. Induction on $n$ therefore shows that $s$ equalizes all parallel injections into $[n-1]$. Every proper injection into $[n]$ factors through a coface; factoring two such injections proves $th=th'$. The identity is the only injection $[n]\to[n]$. The case $n=0$ is immediate.
\end{proof}

\begin{theorem}[Refuted: total asphericity need not imply filteredness]\label{C:counterexample}
The category $\Delta_{\mathrm{inj}}$ is totally $\Winfty$-aspherical and has exact colimits of abelian-group-valued diagrams, but is not filtered. Consequently Lead~4 for $\Winfty$ and manuscript row II-C-003 have a negative answer for arbitrary small categories.
\end{theorem}
\begin{proof}
The affine category $\operatorname{Aff}_{\mathbb Z}(\Delta_{\mathrm{inj}})$, defined and analyzed in Theorem~\ref{D:affine-exactness}, has the same objects and all integral arrow combinations of augmentation $1$. Any two objects map to a common larger ordinal. Given two parallel affine arrows $\alpha,\beta:[m]\to[n]$, Lemma~\ref{C:affine-cones} provides $t$ for which $th$ is independent of the ordinary injection $h:[m]\to[n]$. Since the coefficients of both $\alpha$ and $\beta$ sum to $1$, we get $t\alpha=t\beta$. Thus the affine category is filtered. Theorem~\ref{D:affine-exactness} proves exactness of integral colimits. The original category is nonempty and connected, so Proposition~\ref{C:exact-sufficient} proves total $\Winfty$-asphericity.

There are two distinct injections $a,b:[0]\to[1]$, taking $0$ to $0$ and $1$ respectively. Every arrow $c:[1]\to[n]$ is injective, so $ca\ne cb$. Hence this parallel pair has no equalizer by postcomposition, and the category is not filtered. This verifies every hypothesis and the failure in a completely specified countable category; no finite-to-infinite inference is involved.
\end{proof}



I verified the return's proof line by line (gap monomials: `P_{tδ^i} = y_i D_i(P_t)`; the compatibility `D_{j−1}(F_i) = D_i(F_j)` in both cases; value 1 at the all-ones point; degree `k(2^{n+1} − n − 2)`), and the case `n = 1` by hand: `t = (1,2) − (0,2) + (0,1)`, `tδ⁰ = tδ¹ = [1]`. I also opened the 1973 note (free at ams.org), which the return did not: it states the theorem and sketches a different, combinatorial proof. The label "Proved" should read "Known (Isbell–Mitchell 1973, Th. 3); independent proof".

`Aff_Z(Δ_inj)` filtered ⇒ `colim` exact: I checked this direction directly (`colim_A F = colim_{Aff A} F̃`, since `x − (Σ n_c c)x = Σ n_c (x − cx)`); it is the "if" part of Isbell–Mitchell's Theorem 1. Then C.6. Not filtered: `d⁰, d¹: [0] → [1]` are never equalized. **So the conjecture Grothendieck states at II ms. 36ter is false, and the counterexample is the Isbell–Mitchell category of 1973**; what is new is the identification of total asphericity (C.5) that makes the old example apply. Independent evidence of mine: for several explicit `H` on `Δ_inj` I computed `El(H)` by hand before reading the proof (subfunctors and quotients of `h^0`, `h^1`; all components came out contractible).

## Entry 12

\begin{claim}{G.4}{Proved}{A finite monoid cannot have a nonsimply connected finite-dimensional type}
Let $M$ be a finite monoid. Its universal group $U(M)=\pi_1(BM)$ is finite. If $BM$ is homotopy equivalent to a finite-dimensional CW complex, then $U(M)=1$. In particular neither $S^1$ nor $\mathbb{RP}^2$ is the classifying-space type of a finite monoid.
\end{claim}
\begin{proof}
Let $\eta:M\to U(M)$ be the universal homomorphism. For $a\in M$, finiteness gives $a^r=a^s$ for some $r<s$, so $\eta(a)^{s-r}=1$. Every inverse of a generator is therefore a nonnegative power of that generator. It follows that every word in the generators and their inverses equals $\eta(m)$ for some $m\in M$. Thus $\eta$ is surjective, and $U(M)$ is finite. The identification with $\pi_1(BM)$ follows directly from the edge-and-triangle presentation: the generators are the nonidentity elements and the relations are $[a][b]=[ab]$.

Choose an idempotent $e$ in the minimal nonempty two-sided ideal $I$ of $M$. Such an ideal exists by finiteness, and a sufficiently large power of any of its elements is idempotent. We verify that $H=eMe$, with identity $e$, is a group. For $x\in eMe$, minimality gives $MxM=I$, so $e=axb$ for some $a,b\in M$. Multiplying by $e$ at both ends yields
\[
                    e=(eae)x(ebe)
\]
in the finite monoid $eMe$. In any finite monoid a product is invertible only if each factor is invertible: a right inverse makes right multiplication injective, hence surjective, and gives a two-sided inverse; the dual argument treats a left inverse. Thus $x$ is invertible. The group $H$ is finite, and the homomorphism $H\to U(M)$ is surjective since $\eta(eme)=\eta(m)$.

There is a canonical morphism $BH\to BM$ in $\Hot$ even though the inclusion $H\subset M$ sends $1_H$ to $e$, not necessarily to $1_M$. To type this map, let $\operatorname{Kar}(M)$ be the category of idempotents of $M$ with
\[
       \Hom_{\operatorname{Kar}(M)}(f,g)=gMf.
\]
The full one-object subcategory at $1_M$ is $M$ and the full one-object subcategory at $e$ is $H$. Every object is a retract of $1_M$. The inclusion $j:M\to\operatorname{Kar}(M)$ is a weak equivalence: for each object $f$, the comma category $j/f$ is a retract of $j/1_M$, which has a terminal object. A retract of a contractible space is contractible, and Quillen's Theorem A applies. Hence the typed morphism is
\[
          BH\longrightarrow B\operatorname{Kar}(M)
                     \xleftarrow[\simeq]{Bj} BM.
\]
It induces the surjection $H\to U(M)$ on fundamental groups, after the basepoint path given by the retract arrows is chosen.

Suppose $h:BM\to Z$ is a homotopy equivalence with $Z$ a connected finite-dimensional CW complex. Miller's theorem states that every map from the classifying space of a torsion group to $Z$ induces the zero map on fundamental groups \citep[Theorem B, p.~40]{Miller1984}. Apply it to the composite $BH\to BM\xrightarrow{h}Z$. Its map on fundamental groups is both zero and surjective. Consequently $\pi_1(Z)=U(M)=1$. Notice that this step uses the precise fundamental-group theorem, with no assumption that $Z$ was simply connected.
\end{proof}

\begin{claim}{G.6}{Refuted}{Finite fundamental group is not sufficient for finite monoids}
The assertion that every connected finite CW complex with finite fundamental group is the classifying space of a finite monoid is false.
\end{claim}
\begin{proof}
Take $\mathbb{RP}^2$, whose fundamental group is $\Z/2$. G.4 excludes any finite monoid realization. In particular this refutes Conjecture 7.1 in the verified version of \citet{BenBassat2026}; it does not refute that paper's simply connected Theorem C. The explicit finite categorical and poset models below verify that the obstruction concerns the one-object restriction.
\end{proof}

**The proof of step 4, so that nothing is taken on authority.** Let f: BG → X with G finite, X a connected CW complex of dimension d, and suppose f_* = φ is non-trivial on π₁. Pick c ∈ G of prime-power order pᵏ with φ(c) ≠ 1 (a primary component of an element not in the kernel), C = ⟨c⟩, N = φ(C) ≠ 1, X′ → X the covering with π₁(X′) = N, f′: BC → X′ the lift, ψ a character of N of order p, L the flat line bundle of ψ on X′. Then f′^*L is the line bundle of χ = ψ∘φ|C on BC, and χ has order p. In K⁰(X′), ([L] − 1)^{d+1} = 0, because the skeletal filtration is multiplicative and X′ has dimension d (Miller argues with Lusternik–Schnirelmann category). So (χ − 1)^{d+1} restricts to zero in K⁰ of every finite skeleton of BC. By Atiyah, *Characters and cohomology of finite groups*, Publ. Math. IHES 9 (1961), Proposition (8.1) for cyclic groups (or Theorem (7.2), p. 46: α̂: R(G)^ → 𝒦*(B_G) is a topological isomorphism) and Proposition (6.11), p. 45 (for a p-group R(G) → R(G)^ is a monomorphism), (χ − 1)^{d+1} = 0 in R(C). But its value at c is (ζ − 1)^{d+1} ≠ 0 with ζ a primitive p-th root of unity. Contradiction. (Miller's own computation: K⁰(BZ_{mn}) = Z[[x]]/((1+x)^{mn} − 1) and the image (1+x)ⁿ − 1 of x_m is not nilpotent; I verified this by mapping x to ζ − 1 in Z_p[ζ] for ζ of order p^c, p^c the exact power of a prime p | m in mn.)