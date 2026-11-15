# Independent audit of the all-action stabilizer criterion

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026.
Independent reviewer: `finite_tests_literature`. No priority claim.

**Passed.** After separately approving the finite alternating bridge,
I read the full proof of `A:predimension-stabilizer-criterion` in
`sections/predimension_totality_reduction.tex`. This is an additional
independent check, separate from the audit by `main_compact_duality`.
I found no missing hypothesis or gap in the following steps.

1. **Concrete indexing and the rich limit.** The indexing category has
   all closed embeddings, not just the inclusions used to form the
   directed union. Richness and homogeneity follow from countability,
   joint embedding, closed-subobject restriction, and free amalgamation.
   A finite extension over an arbitrary finite closed subset is served
   by first amalgamating it with a stage containing that subset.
   In the point-and-edge-closed version, every raw atom of the limit is
   closed: it lies in a closed stage where it is closed, and transitivity
   applies. Consequently the finite closed substructures used in A_M
   belong to the stipulated subcategory as well. The equivalence A_M≃A
   keeps all morphisms and induces equivalences of element categories.

2. **Fixed points of a pointwise stabilizer.** For x outside closed B,
   two copies of a closed D containing B and x can be freely amalgamated
   over B, embedded over the original D, and interchanged by a partial
   isomorphism extending to an automorphism. This moves x while fixing
   B. It proves `Fix_M(G_B)=B`, including the empty-base case.

3. **Functorial contraction of slice cosieves.** In each order interval
   determined by P, placing the X-side points before the fixed Z-side
   points is preserved by every increasing embedding fixing P. Such
   an embedding cannot send a point outside P into P. The map on free
   amalgams is induced, and its image is closed because the target
   is the free amalgam of Y and the source over the closed X-image.
   The identity and constant natural transformations therefore exist
   as stated. Transport through a category equivalence does not need
   a functorial choice of embeddings into the limit. Full cosieves are
   closed under isomorphism, so that transport preserves the desired
   contraction. The analogous disjoint-union construction contracts
   BA_M.

4. **The eventual-equality quotient.** Condition I combines witnesses
   both for transitivity of `h~h'` and for preservation under any
   outgoing map. If two quotient elements become equal after u, the
   witness after u composes with u, proving injectivity of the quotient
   transitions. Thus this step really applies to every original action,
   without an unmentioned monomorphism assumption.

5. **The first homotopy-final comparison.** In the comma category
   D=`(a,[h]) downarrow El(q)`, an object of `d downarrow J` is uniquely
   specified by an arrow g from x satisfying `H(g)k=H(gf)h`: its target
   slice arrow must be gf. Morphisms are exactly the corresponding
   postcompositions. This is the full nonempty cosieve claimed in the
   proof. Quillen's Theorem A applies in the displayed direction;
   a/A_M has an initial object. A second application proves that
   El(q) is a weak equivalence, not merely a bijection on components.

6. **The saturation.** The inclusion-only poset of finite closed
   substructures is directed. For an injective action, its colimit S
   contains each H(B) injectively. The G-action is well-defined after
   passing to a common closed superset, and G_B fixes every element
   coming from H(B). Hence S is a continuous discrete G-set.
   For `T_S(B)=S^{G_B}`, two automorphism extensions of a closed
   embedding differ on the right by G_B, giving independence of the
   chosen extension. Its image lies in the appropriate fixed subset.
   Extending composites proves functoriality, and the original H maps
   naturally and injectively into T_S.

7. **The second homotopy-final comparison.** In
   `(a,s) downarrow El(i)`, the element of H(b) is uniquely determined
   by the slice arrow f because i_b is injective. The same injectivity
   shows that every slice morphism between the allowed objects is an
   element-category morphism. Thus this comma category is precisely
   a full cosieve. It is nonempty by taking a closed b containing a
   and a finite support c for s; the identity automorphism extends the
   inclusion a→b. The slice contraction and Theorem A prove the second
   weak equivalence.

8. **Open stabilizers and representables.** An orbit with stabilizer
   G_F is G/G_F. A coset gG_F is fixed by G_B exactly when G_B fixes
   gF pointwise, which is equivalent to `gF subset B` by the already
   proved fixed-point identity. Since gF is closed in M, its inclusion
   in B is closed; conversely every closed embedding F→B extends to
   an automorphism. This gives the stated natural representable
   identification. For F empty the action is constant one, whose
   element category is the separately contracted A_M. Orbit
   decomposition commutes with taking fixed subsets, so the saturated
   element category is a disjoint union of these contractible pieces.

The two weak equivalences transfer contractibility of components back
to every covariant A-set. Combined with the separately audited
open-subgroup classification, this proves totality of both ordered
strict-predimension categories. Their previously proved injective
column presentation has nonzero derived colimit, so this combined
argument gives a total nonexact category. This conclusion uses the
general proofs; no enumeration of finite targets is being used to
infer the all-action statement.
