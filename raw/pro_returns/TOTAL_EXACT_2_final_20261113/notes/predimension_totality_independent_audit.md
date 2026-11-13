# Independent audit of the all-action totality criterion

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026.
Reviewer: the `main_compact_duality` branch. No priority claim.

## Status

**Passed.** I read the complete proof of Proposition A:predimension-stabilizer-criterion in `sections/predimension_totality_reduction.tex`. Its changes of indexing category, both homotopy comparisons, the smooth group action, and the final representable identification are valid. The criterion is conditional only on the displayed open-subgroup hypothesis; that hypothesis is independently supplied by the alternating-bridge argument and its separate finite-branch audit.

The criterion applies to every covariant set-valued diagram, without finite-generation, finite-presentation, injectivity, bounded-cardinality, or definability restrictions. The proof does not identify all A-sets with group actions without comparison: it explicitly changes the action twice and proves that each change preserves the homotopy type of its category of elements.

## 1. The rich limit and the concrete category

The hypotheses needed for the countable strong limit are present: countably many finite isomorphism types and embeddings, restriction and composition of closed embeddings, joint embedding, and free amalgamation. Serving all finite strong extensions in a countable rich sequence gives the extension property over an arbitrary finite closed base. To reduce an arbitrary base to a stage, freely amalgamate the proposed extension with a large enough stage over that base. Back-and-forth then extends any finite closed partial isomorphism to an automorphism.

The category A_M contains **all** strong embeddings between finite closed substructures of M. It is equivalent to the specified small category A. The inclusion-only directed poset used later is a different indexing category, introduced solely to construct S. No claim equates the homotopy type of the all-embedding category with that of the inclusion poset.

Free duplication of a finite closed D over a closed B, followed by extension into M over the first D, proves Fix_M(G_B)=B. It moves any chosen point outside B and works also for B empty. Ordered amalgamation is permitted because the class accepts every extension of the two factor orders.

## 2. Contractibility of slice cosieves

In the slice P/A, free amalgamation with one fixed object P→Z gives a functor. The order rule—X-side before Z-side in each gap of P—is respected by every slice arrow, because an increasing injection fixing P preserves each gap and cannot send an extra point into P. For an arrow X→Y over P, the map between the two amalgams is a closed embedding: its target is the free amalgam of Y and the source over X.

The two factor inclusions are natural transformations from the identity and the constant Z functor. If the chosen Z belongs to a full cosieve, every target amalgam belongs to that cosieve. Hence the cosieve's nerve is contractible. Tagged construction followed by transport along an equivalence correctly handles the lack of a functorial choice of embeddings into the one fixed limit M.

The same construction over the empty formal base contracts BA itself. It does not require that the empty object belong to the chosen category.

## 3. Eventual equality and the first comparison

For H arbitrary, h∼h' at a means that one future arrow from a identifies them. Condition I makes this relation transitive: use a commuting square for the two witnessing arrows. The same square argument makes it natural. Its quotient H^inj has injective transitions, because an equality after u and one additional witness gives a witness before u by composition.

The comparison El H→El H^inj has the correct comma orientation. For b=(a,[h]), write D=b↓El(q). Its objects are triples (x,k,f:a→x) with [k]=[H(f)h]. The functor J:a/A→D sends f to (x,H(f)h,f).

For d=(x,k,f), an object of d↓J is determined by a single arrow g:x→y satisfying

    H(g)k=H(gf)h.

The target a-arrow is forced to be gf. A morphism is exactly further postcomposition in x/A. Thus this comma is literally the full cosieve of equality witnesses, not merely a related graph or a set of witnesses. It is nonempty by the definition of the quotient relation and contractible by the slice lemma. Quillen A makes J a weak equivalence, so D is weakly contractible because a/A has an initial object. A second application of Quillen A proves the desired comparison for El(q).

No ordinary finality assertion is substituted for a homotopy-finality assertion; both comma calculations are explicit.

## 4. The group action from an injective diagram

For H with injective transitions, the inclusion-only poset of finite closed substructures is directed, and its set colimit S contains each H(B) injectively. The formula

    g·i_B(h)=i_(gB)(H(g|B)h)

is independent of the representative: put any two representatives in a common closed finite stage and use naturality of g on its inclusions. Functoriality gives the group law. G_B fixes i_B(h), so every point stabilizer is open and S is a continuous discrete G-set.

For T_S(B)=S^{G_B}, an embedding f:B→C extends to an automorphism g. If g' is another extension, g^{-1}g' fixes B pointwise, so g' differs on the right by an element fixing s. Thus g·s is independent of the extension. Since G_C≤G_(gB), the image lies in the required fixed-point set. Products of extensions show functoriality.

The inclusion H→T_S is natural for arbitrary embeddings, not only inclusions: the value H(f)h at C and H(g|B)h at gB have the same image in S under the inclusion gB⊆C.

## 5. Saturation and the second comparison

For (a,s) in El T_S, an object in (a,s)↓El(i) consists of f:a→b and h∈H(b) with i_b(h)=T_S(f)s. Injectivity makes h unique. Morphisms in this comma are therefore exactly those in the full cosieve of eligible f in a/A; naturality ensures eligibility is preserved by postcomposition.

The cosieve is nonempty. Represent s by an element of H(c), take a finite closed b containing a∪c, and use the inclusion a→b. The identity automorphism extends this inclusion, so T_S carries s to itself, now represented in H(b). Contractibility of the cosieve and Quillen A yield BEl H≃BEl T_S.

The use of a common stage here is legitimate even when a and c intersect: no disjointness or amalgamation inside M is required, only that their finite union lie in some later closed stage.

## 6. Open stabilizers give representables

For an orbit G/G_F, a coset gG_F is fixed by G_B exactly when

    G_B ≤ gG_Fg^{-1}=G_(gF).

By Fix_M(G_B)=B, this is equivalent to gF⊆B. Restricting the closed inclusion gF≤dM gives a closed embedding F→B. Every such embedding extends to an automorphism, and two extensions give the same coset precisely when they agree on F. This establishes a natural isomorphism T_(G/G_F)≅A_M(F,−), with postcomposition in the required covariant direction.

If F is empty, this is the constant singleton action; its element category is the already contractible A_M. Otherwise its element category has the initial object (F,id). Orbit decomposition commutes with taking fixed subsets because all action maps preserve the individual orbits. Hence each component of El T_S is contractible.

The two weak equivalences preserve components and their weak homotopy groups. This proves totality for arbitrary H. Empty actions cause no problem: their categories of elements have no components. Nerve realizations are CW complexes, so the weak-contractibility formulation is sufficient for the stated definition of totality.

## Conclusion of the audit

There is no unproved finite-support assumption inside the comparison proof: its sole group-theoretic hypothesis is displayed and supplied separately. There is also no use of a Ramsey theorem, positive averaging, a Boolean-colimit claim, weak elimination of imaginaries, or a homotopy-coherent-to-strict conversion.

Together with the independently audited open-subgroup classification, this criterion proves totality of both explicit predimension categories. The private-incidence column calculation remains a different module and gives T_1(Q)=R for every nonzero unital coefficient ring. The binary/triple row-action contractions do not identify that column cokernel with a permutation module.
