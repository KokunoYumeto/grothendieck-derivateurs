# Independent adversarial review of the Part D realization route

2026-11-16, approximately 07:00 UTC. This is a proof review of the route in D_finite_realization.md, not a claim that its explicit finite category has already been compiled.

## Confirmed reductions

For Y=K wedge N S^m, the retraction to K splits the relative homotopy sequence. Relative Hurewicz for the (m-1)-connected pair identifies the kernel in degree m with (Z pi)^N. Consequently maps under and over K, interpreted in the derived retractive category, give the indicated matrix group. The section eliminates the possible ambiguity from pi_(m+1)(K); there is no extra uncontrolled pi_m(K) term in the kernel.

The specified homotopy H:r f~r defines a genuine projection from the relative mapping cylinder to K, with the required values on its two ends and on K. Both endpoint inclusions are strict under/over K, and the target inclusion is an underlying homotopy equivalence. Thus this finite roof represents f without using an infinite path object.

The displayed tensor T_A is the fiberwise smash construction. For the wedge coefficient object it has type K wedge N(S^m smash A). Its pushout diagram is functorial for strict retractive maps. Finite category products and finite Grothendieck homotopy colimits implement it once the coefficient diagram is genuinely finite and strict. The projection to K and the section from K pass through these constructions as actual functors if the coefficient data commute strictly.

## Exact finite-diagram condition

The finite-model assertion must concern a finite **direct** diagram, after duplicating occurrences of a coefficient object. It must not assert finite strictification for an arbitrary finite diagram with a self-idempotent or a directed cycle. A direct indexing category has finitely many strings of nonidentity maps, so its cubical/bar strictification uses finitely many cells. An indexing diagram with cycles need not have that property.

All required coefficient maps, homotopies and higher coherence must be present before strictification. Equality of matrices in a homotopy category is not by itself an unlimited coherent diagram. In the current double-cone construction the essential datum appears to be only the chosen nullhomotopy f(1-f)~0, together with finite co-H addition data; a new unnecessary higher coherence should not be introduced by treating the diagram as a strict idempotent action.

Maps of the original finite coefficient spheres are co-H up to homotopy because their degree-m classes form the free Z pi module; their distributivity homotopies are finite coefficient data. These should be retained when tensoring, so that the uniform matrix calculus follows from actual homotopies rather than only equalities of induced homology maps.

## Triangulation condition

Triangulate the finite coefficient data before tensoring with BC. Relative simplicial/PL approximation applies to each finite-domain map and each finite-parameter homotopy, fixing already specified faces. The resulting finite cubical mapping-cylinder/bar pieces are finite polyhedra, and their attaching subpolyhedra admit a common finite subdivision. Face-poset constructions then give finite categories. An assertion that every map between the resulting infinite classifying spaces has a finite representation would be invalid; that assertion is not needed here.

Strict retractions K->Y->K require a small additional check: keep K as a fixed subpolyhedron, approximate the projection relative K, and choose compatible subdivisions of the section and projection. The only feedback relation is r i=id_K. The other coefficient maps should lie in the duplicated direct diagram. This avoids the familiar impossibility of making an arbitrary dynamical self-map simplicial on a single finite triangulation.

## Present conclusion

No algebraic or finite-coherence counterexample to the proposed route was found. Its abstract topological operations have the required finite-domain form. The remaining obligation is to instantiate a finite direct coefficient diagram with all boundary/coherence data, triangulate it by a stated finite algorithm, and compile/check the resulting category table. Until that concrete implementation and its finiteness-obstruction calculation are complete, this review does not certify a counterexample to D1.
