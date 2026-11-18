# Continued Part C attack after C.20

**Status at 2026-11-18 04:52 UTC: INCOMPLETE.** This is a working research note. It does not modify the checkpoint03 main section or promote either C.raw_gate or C.general_M. The integrated C.1–C.20 proofs remain authoritative.

## Constraints from the actual adjunction

In the corollary, each scalar module T(a)=phi(h_a) is not only projective but finitely generated projective. Indeed kappa is a left adjoint as well as a right adjoint, so it preserves filtered colimits. Evaluation at a preserves them in the module category. The identity kappa(U)(a)=Hom_k(T(a),U) therefore shows that Hom_k(T(a),−) preserves filtered colimits, so T(a) is finitely presented; exactness of kappa already gives projectivity. This is an objectwise assertion. It does not show that T, as a module over the small additive category, has a finite-component projective resolution, or is of type FP-infinity. The arbitrary-sum obstruction C.20 has not been realized with these adjunction and monoidal constraints.

A slightly weaker additional hypothesis than the scalar-copower compatibility used in C.14 suffices for purity: right exactness of the internal tensor product in each variable. For a finitely presented k-module U, choose a finite presentation k^r→k^s→U→0. Exactness/cocontinuity of kappa and right exactness of tensor give

    (kappa U) tensor X = coker(X^r→X^s) = U tensor_k X.

Applying exact cocontinuous F gives the corresponding identity with U tensor_k F(X). The interval monomorphism for X tensor kappa(U) then proves that U tensor_k F(alpha tensor X) is monic. Finitely presented U suffice to detect purity. This is a conditional refinement only: we have not read “k-bilinear” in the manuscript as asserting right exactness or cocontinuity without justification. It has not been inserted in the frozen main section.

## Attempts to realize C.20 as the raw-adjoint obstruction

1. Ordinary nonnegative chain complexes, their diagram categories, and ordinary simplicial/cubical constructions have split interval maps after projective evaluation. The already proved C.7 excludes them. Merely adding a large contractible summand to a resolving functor does not evade this.

2. We examined Day-convolution presheaves on a small monoidal subcategory of projective connective complexes. If the chosen interval comes from an ordinary contractible complex with a graded retraction of its unit inclusion, the induced retraction is natural in the tensor variable. Splitting a projective source complex into spheres and disks then gives split evaluation maps. This model again falls into C.7; it is not a realization of the generic exact functor in C.20. Restricting morphisms or using a nonrepresentable, nonsplit interval could change the conclusion, but no full construction has yet been made.

3. Categories of ordinary representations of a group, or of a cocommutative Hopf algebra with the ordinary tensor product, cannot supply the required interval at all. Let I be an injective cogenerator of k-modules. For a nonzero representation J, the ordinary k-module Hom_k(J,I) has the contragredient action, and evaluation J tensor Hom_k(J,I)→I is equivariant and nonzero. The degree-zero nullity required by (d), together with phi left adjoint to the trivial-action functor, would force that evaluation to be zero. Since alpha embeds the nonzero unit into J, this is a contradiction. Thus an acyclic group with unusual cohomological dimension does not by itself solve the problem. Bialgebras or monoids without an antipode escape this particular argument, but none satisfying all conditions has been constructed.

4. One-object bialgebra/module categories would make the problem concrete: an augmented k-projective bialgebra B, trivial module k with Tor_B(k,k)=k, and an interval J with k→J universally tensor-monic and Tor_B(k,J tensor X)=0 for all X. The projective functor resolution is a right-B resolution of k. The elementary candidates fail: an absorbing idempotent makes the relevant coinvariant functor exact (incompatible with the interval), groups have the evaluation obstruction, and standard chain-category models have split intervals. This is a research route, not an existence result.

5. We considered contramodule and linearly compact constructions for the general-M question. In naive opposite-module or profinite-dual examples, the scalar-copower functor does not preserve products, so assumption (a) fails. Standard t-adic contramodules with unit killed by t have a nonzero Tor_1 of the unit, violating (c). No assertion that those examples refute the theorem is made.

## The completeness route

Enough projectives and existing products give exact products: one tests a product of epimorphisms against every projective and uses exactness of products of module groups. This supplies AB4-star, not AB4. C.18 already disproves the inference of AB4 even with complete, cocomplete, cocontinuously monoidal data satisfying all four hypotheses. We found no argument that these hypotheses produce an exact cocontinuous resolving F in general, and did not assume one.

A search located Weibel's printed Corollary 2.6.11, whose displayed proof uses a coproduct of projective resolutions. The author-hosted scan was downloaded and the printed statement/proof at p.55 read. We do not use this paragraph to erase the exact-coproduct issue: the direct-sum resolution step must be justified for the category at hand, and the complete counterexample C.18 shows why this matters. The official corrections landing page was opened, but its linked second-edition errata PDF was inaccessible in web retrieval and returned404 on direct retrieval. No erratum is reported as read. The C.13 and C.15 proofs retain their own explicit hypotheses and do not depend on this potentially misleading search result.

### Newly inspected sources, integrated in the bibliography after checkpoint03

- Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics38, Cambridge University Press,1994. Public institutional PDF: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/weibel-homv2.pdf . Web open rejected its18,616,592-byte size; direct download succeeded. Saved as sources/Weibel_1994.pdf and .txt. Read only the relevant printed p.55 Corollary2.6.11 paragraph and immediate context for this route; no whole-book reading is claimed.
- Official correction landing page https://sites.math.rutgers.edu/~weibel/Hbook-corrections.html opened. Linked second-edition correction PDF https://sites.math.rutgers.edu/~weibel/papers-dir/Hbook.errors.edition2.pdf not obtained (web inaccessible; direct404). This is a failed retrieval, not an opened source of a correction.

### Searches submitted

`"complete abelian category" "enough projectives" "coproducts"`; `"abelian category" "products" "enough projectives" "cocomplete"`; `"exact functors" "resolution" "cocontinuous" abelian`; `"pure submodule" "projective" "finitely generated" direct summand`; `"complete" "not cocomplete" "enough projectives"`; `Weibel "2.6.11" error exact coproducts`; `site:sites.math.rutgers.edu Weibel errata 2.6.11`; `"abelian category" "complete" "solution set" "coproduct"`; `"complete abelian" "well-powered" cocomplete`; `"homological test" "ring" category`; `"linear" "integrator" "Grothendieck" abelian`; `"Pursuing Stacks" "Lemme 3" linear`; `"test categories" "pure" "modules"`.

Search results on forums, repost sites, and generated summaries were used only as possible source locators, not as theorem evidence. No new published theorem from those snippets was imported into the proof.


### Source handoff after checkpoint03

We opened Positselski, Homological full-and-faithfulness of comodule inclusion and contramodule forgetful functors, Glasgow Mathematical Journal68(2026),86–119, DOI10.1017/S001708952500014X: the full34-page publisher PDF, Introduction and Theorem1.1, including the infinite-dimensional trivial-contramodule discussion on printed p.88. The coordinating agent independently opened it, is pursuing the general-M route, and owns its bibliography record Positselski2026CRoot in notes/C_root_references.bib. We did not create a duplicate. The contramodule tensor structure must itself be constructed; the coordinating agent opened Johnston2026 §2.3 for the warning that it is not automatically inherited from ordinary modules. That source is recorded by the coordinating agent, not treated as read by this child.

The Numdam metadata/abstract for Positselski, Contramodules, Confluentes Mathematici13(2)(2021),93–182, DOI10.5802/cml.78, was opened at https://numdam.org/articles/10.5802/cml.78/ . Only the abstract and bibliographic page were read in this continuation; no theorem from its full text is invoked.

Additional submitted searches: `contramodules "homological epimorphism" "discrete"`; `contramodules "derived" "fully faithful" "coproducts"`; `"bireflective" "abelian category" "homological"`; and `"Ext" "coproduct" "AB4" "injective" monomorphism`.

We reread Hubert2025 §§2.7.2–2.7.10 and2.8.11–2.8.12 from the opened local thesis. Its complex-valued internal-Hom right adjoint is homotopical objectwise, while the raw right adjoint of the problem is its degree-zero cycle object. Replacing the latter by the former would lose exactly the gate under investigation. The thesis's finite-type duality warning is consistent with C.16–C.20; it is not evidence that arbitrary infinite sums admit the same dualization.


### Excluded Neeman/Day candidate: the proposed interval is not universally monic

Status: an excluded construction, not a counterexample to the manuscript's theorem and not a new closed main-result row. The following argument is conditional on the proposed Day tensor actually descending to the indicated exact functor category and preserving its colimits. The coordinating agent independently re-proved the argument on 2026-11-18 before this note was saved.

Put k=Z_(p), J=Z_p, and let alpha:k→J be the usual inclusion. The proposed construction takes a small full k-linear subcategory S of k-modules containing k, J, their tensor powers, and the specified small coproducts, and an exact full category Ex(S^op,Ab) of functors sending those coproducts to products. Write h_T=Hom_k(-,T)|S. We assume the properties used in the proposal: representables are projective, the relevant pointwise cokernels remain in Ex, and a cocontinuous Day tensor satisfies h_T tensor h_U = h_(T tensor_k U). This identity then also holds on retracts. The unit is h_k and the proposed interval map is h_alpha:h_k→h_J. Even under these favorable assumptions, h_alpha tensor X fails to be monic for a specific X.

Let C=J/k and q:J→C. We first check directly that C is a nonzero Q-vector space. It is torsionfree: if p^n z belongs to k for z in J, its p-adic valuation shows that z belongs to k; primes different from p act invertibly. It is p-divisible: for z in J choose an integer a congruent to z modulo p, and the class of (z-a)/p maps to the class of z. Thus every nonzero integer acts invertibly on C. The quotient is nonzero because k is countable and J is not. Moreover Hom_k(C,J)=0: the image of each element under any such map would belong to the intersection of all p^n J, which is zero.

The map delta:J→J tensor_k J defined by delta(z)=1 tensor z-z tensor 1 vanishes on k. It therefore factors as delta_bar:C→J tensor_k J. We have the exact identity

    (id_J tensor q) delta_bar = alpha_C,
    alpha_C:C→J tensor_k C,   c↦1 tensor c.

The inclusion k→J is faithfully flat (equivalently for this argument, it is pure, since C is torsionfree over the PID k), so alpha_C is injective. The target J tensor_k C is a Q-vector space, and alpha_C is Q-linear. Choose a Q-linear retraction r:J tensor_k C→C of alpha_C. Then r(id_J tensor q) retracts delta_bar. In particular C is a direct summand of J tensor_k J. This conclusion does not require a cotorsion theorem or a splitting of J→C.

Although C need not have been chosen as an object of S, h_C is consequently a retract of the projective representable h_(J tensor_k J). Thus h_C belongs to Ex and is projective. Yoneda on the Karoubi envelope gives

    Hom_Ex(h_C,h_J)=Hom_k(C,J)=0,
    Hom_Ex(h_C,h_C)=End_k(C).

Define X=coker(h_q:h_J→h_C), formed pointwise in Ex as assumed. Since h_C is projective, the quotient map pi:h_C→X is nonzero: applying Hom_Ex(h_C,-) identifies its class with id_C in End_k(C), and no morphism from h_C to h_J can account for that class.

Cocontinuity of the proposed tensor, together with the representable identity and its compatibility with retracts, identifies

    h_J tensor X = coker(h_(J tensor_k J) → h_(J tensor_k C)),

where the displayed map is induced by id_J tensor q. The composite of pi with the proposed map alpha_X:X→h_J tensor X is induced by alpha_C. The identity above shows that it factors through h_(J tensor_k J), by delta_bar. It is therefore zero in that cokernel. A monomorphism alpha_X would imply pi=0, a contradiction. Hence alpha_X is not monic.

This rules out the specific interval h_k→h_Zp in the proposed Day/Ex construction, even after all missing Day-descent properties are granted. Neeman's failure of exact sequential colimits by itself still does not give a category satisfying the full interval axiom. The coordinating agent owns the opened Neeman2002 source record and the independent proof-check event; this note records the algebraic exclusion only.
