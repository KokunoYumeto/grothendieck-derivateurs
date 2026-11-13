# Independent audit of the selected large-target AKR construction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. This is an independent proof audit, not a priority claim. The reviewed statements are in sections/akr_ordered_necklace.tex and sections/akr_large_targets.tex.

## Outcome and scope

The proofs of C:necklace-set-colimit, C:ordered-necklace, C:large-target-convexity, and the assembled C:selected-nontotal pass this independent audit. The conclusion is existence of sufficiently large admissible choices, for every allowed numerical sequence, giving a quasi-filtered category whose binary action has nonzero second homology. The universal quantifier over all admissible choices in Part C.1 is not proved by these statements.

## Strict necklace colimit

For each actual path size \(m\), the displayed visibility table covers all target coordinates. Each fiber has one preimage at every visible index; consecutive-overlap equalities join all those preimages along a cyclic interval. Fixed-point fibers are circles and private-point fibers are singletons. The prescribed target is covered, so its fibers are precisely the equivalence classes of the neighboring relations. This verifies the strict set coequalizer, including the absence of extra target identifications.

## Ordered necklaces

The partial increasing bijection \(f(S)\to g(S)\) extends by finite linear interpolation and slope-one tails to an increasing homeomorphism \(h\) of the real line. Every component of the complement of its fixed set is invariant. Within such a component the iterates move monotonically to one endpoint. Therefore \(h^{2k}g(S)\) eventually lies strictly beyond both finite sets \(f(S)\) and \(g(S)\), in the direction of motion, and this remains true for every larger \(k\).

The prescriptions \(wg=f\) and \(wh^{2k}g=h^{2k}g\) then define a strictly increasing function on their finite joint domain. Prescriptions in distinct complementary components cannot interfere; at fixed points they agree. The interpolated \(w\) exists. The four displayed families of necklace equations for \(a_i=h^i\) and \(a_i=wh^{4k+1-i}\) all hold as actual equalities of functions. Factoring through the strict coequalizer gives \(\rho:Z\to\mathbb R\). Ordering first by \(\rho\) and then within its fibers preserves every source-copy order because \(\rho\alpha_i=a_i\) is injective and increasing.

This argument does not rely on a homotopy-coherent cocone or on a strictification theorem.

## Long-target convexity

The linear-amalgam lemma is valid with the stated strong convention that every shortest path stays in a convex image. Component injectivity makes the component incidence relation of each two-piece gluing a matching. A shortest excursion outside one piece would be a shortest path in the other piece between vertices of the convex overlap, which is impossible. Induction along a chain preserves component injectivity and convexity; the necessary convexity is transitive.

The numerical visibility bound can be checked directly from the table in the necklace lemma. For a nonconstant path with \(m\ge2\) vertices:

- in the first coordinate range, the visibility size is \(2(u+1)\le2m-2\);
- in each middle range it is \(m\le2m-2\);
- in the last range it is \(2(4k-u+1)\le2m-2\).

Private points have visibility size one, bounded by \(2n-2\) because \(n\ge2\). Fixed points are visible everywhere and are omitted from the union used to choose the cut.

A shortest path \(P\) between two vertices in one old component has at most \(D\) edges. Thus its at most \(D+1\) vertices have proper visibility sets with union size at most \((2n-2)(D+1)<s\). Choose a missing index \(r\) and remove the overlap from \(r-1\) to \(r\). Each proper vertex fiber of \(P\) is untouched, and each full circular fiber becomes a connected path. An edge with a proper endpoint fiber avoids the cut. If both endpoints have full visibility, the two-point routing property factors the whole W-arrow through every copy, so its edge fiber is full and also remains connected.

Consequently every vertex and edge of \(P\) has exactly one preimage in the linear amalgam. The cell lifts respect incidence, and the endpoint lifts are the vertices in the selected copy. This supplies a path of the same length in the linear amalgam. Comparing its length with the intrinsic source distance and using linear-amalgam convexity proves that every shortest \(P\) lies in the selected copy. New component injectivity is not assumed in this proof.

## Assembly of the selected construction

The point order and the order on binary graph components are legitimately independent auxiliary orders. Increasing injections rule out nontrivial cycles for both partial transition relations. Choosing a common odd bound \(n\) above both path sizes is essential: the finite third-coordinate experiment showed that a point-path bound need not bound a component path.

The same necklace parameters can meet both orderability thresholds, the convexity threshold, and the original expansion requirement: multiples of the odd integer \(3n\) that are \(1\) modulo \(4\) form an unbounded arithmetic progression.

Taking graph components commutes with the necklace graph colimit because components are the coequalizer of the endpoint maps in sets, and set colimits commute with colimits. Hence the ordered component necklace really is the actual component set of the constructed graph, not an auxiliary approximation.

Composition preserves the three required properties. New same-stage targets have no arrows between them; adding them one at a time introduces no missing incoming factorization. The connected fixed-subgraph criterion gives injectivity of the old cycle colimit, and therefore of the old second homology, for each attachment. Weak sums preserve it directly.

The first-stage calculation is consistent for arbitrary sufficiently large choices: the two binary endpoint pairs contribute one cycle each with augmentation one; pairs involving the third point have private leaf endpoints and give forests. Repeated pairs, identity attachments, and initial weak sums give forests as well. Thus the class \(\kappa_+-\kappa_-\) is initially nonzero and survives every stage. Filtered exactness of abelian groups transfers this persistence to the countable union.

## Verification limits

No finite graph computation is used to prove the selection theorem. Earlier finite computations supplied useful hypotheses to investigate, and the component-path inflation example exposed a necessary distinction, but the present argument is an all-stage induction under selected sufficiently large parameters.
