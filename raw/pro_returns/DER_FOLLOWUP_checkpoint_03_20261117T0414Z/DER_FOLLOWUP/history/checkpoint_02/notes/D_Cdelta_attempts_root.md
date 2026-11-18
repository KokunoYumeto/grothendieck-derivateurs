# C-delta free-monoid investigation: root notes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. These are working routes, not claimed solutions.

## 1. A positive version of the free-group diagram need not suffice

D.4 proves that its free-group diagram has source H2=Z and free group colimit. Even if compatible positive monoid cones were constructed in all those groups, one would still have to calculate the **monoid** colimit. Its classifying space could retain the nonzero H2 that group completion kills. Thus positivity alone does not refute the monoid comparison. This distinction was communicated to both investigating agents.

## 2. Attempt to turn arbitrary free abelian maps into positive maps

The module Q in R17 is objectwise free of finite rank, with transition matrices that may have negative entries in a chosen basis. A tempting stabilization is E_A=Q_A⊕Z, with maps f⊕N_f where N_f is a rapidly growing multiplicative size weight. One would choose unimodular simplicial cones containing the invariant scalar axis in their interiors, so scalar expansion dominates the signed matrix.

There is an elementary obstruction to the simplest integral form. Suppose h:E→Z is the primitive quotient, v is its chosen splitting with h(v)=1, and a basis b_1,...,b_d has h(b_i)>0 and puts v in the interior of its nonnegative cone. Then v=Σ n_i b_i with every n_i a positive integer, so 1=h(v)=Σ n_i h(b_i)≥d. Thus this is impossible for d>1. This rules out that proposed cone choice, not every possible positive stabilization.

Using a rational interior axis introduces a different problem. With axis (v_A,k) in Q_A⊕Z, an extension preserving axes up to scalar N_f would have the form

    (q,t) ↦ (f(q) + t (N_f v_B − f(v_A))/k, N_f t).

It is integral only if N_f v_B ≡ f(v_A) modulo k. Arbitrarily increasing N_f does not impose this vector congruence. A compatible family of residue vectors, or a different lattice construction, would be needed; none has been established. Passing to rational vector spaces would no longer give the free abelian groups that are abelianizations of free monoids.

## 3. First-return loop monoids are positive but change the group

A functor of pointed free directed categories does induce homomorphisms between their first-return loop monoids: a loop decomposes uniquely at its visits to the base vertex. Those monoids are free, and transitions are positive word substitutions. This offers a canonical positive construction, but it does not recover the fundamental group of the whole graph.

For the graph with vertices x,v and edges a:x→v, b:v→x, c:v→v, the first-return loops at x are exactly a c^n b, n≥0. Any loop is a unique concatenation of such words. Hence the loop monoid has a countably infinite free basis, while the connected underlying graph has three edges and two vertices, so its fundamental group is free of rank2. The inclusion of the one-object loop category is therefore not a weak equivalence. A replacement argument would have to address this discrepancy explicitly.

## 4. Remaining promising route

For a total index A, hocolim_A X→colim_A X is a weak equivalence for every simplicial-set diagram X. Applying this to the nerves of the fixed-object translation categories reduces the comparison to the passage from their simplicial colimit to their categorical colimit. Condition I provides commuting squares for spans and may give common refinements of contextual positive-word substitutions. Parallel refinements still require the full all-action totality hypothesis. The other threads are investigating a planar substitution-forest model and a positive presentation, respectively. Neither reduction alone proves the required comparison.

## 5. Injectivization, saturation, and the limits of the orbit route

For any action L on C_delta, define x~y at a when some arrow a→b identifies them. Condition I combines two witnesses from a, so this is an equivalence relation. The same amalgamation combines finitely many witnesses, proving that this injectivization commutes with finite products. For a monoid diagram, multiplication is therefore well defined after injectivization. Filtered union over finite closed subsets of the Fraïssé limit and fixed points of G_a also commute with finite products. Thus the R17 action reduction can be applied degreewise to the nerve of a monoid diagram.

The saturated object is a continuous G-monoid S; it is a filtered colimit of the original free monoids along actual inclusions of finite closed structures. The candidate comparison becomes the simplicial orbit map `(NS)/G → N(S_G)`, where S_G means **monoid coinvariants**, not just the orbit set. A proof would have to compare these two different quotients. The filtered-colimit monoid is cancellative, conical and equidivisible, by the corresponding finite existential/Horn properties in free monoids. It need not have an N-valued length. An element can be a proper prefix of its translate: an interval-subdivision example under order automorphisms already has that phenomenon. Therefore a proof based on preservation of discrete length or equality of supports of a product is invalid.

The tower thread subsequently proved a different, irrational rank-two positive stabilization, recorded in `D_positive_stabilization.md`. This repairs the matrix-positivity attempt but **does not produce a strict word-substitution functor**. Moreover even a positive functor with T₁(M_ab)≠0 would not alone disprove q_M: the colimit monoid may have the same nonzero H₂. Knowing only that its group completion is free does not establish that its classifying space is aspherical.

## 6. Further exact searches and inspected sources, 03:05–03:07 UTC

Queries actually run:

- `"free monoids" "homotopy colimit" filtered`
- `"equidivisible" "classifying space" monoid`
- `nerve free categories colimit categorical realization weak equivalence substitutions`
- `"Homotopy theory of monoids and derived localization" arxiv`
- `"Simplicial monoids and Segal categories" Bergner arxiv`

Chuang–Holstein–Lazarev, arXiv:1810.00373v3, primary PDF, was opened at §§2.3–2.5, Proposition 4.1, Corollary 5.1 and Theorem 5.2 with the relevant proofs. Its equivalence of relative categories preserves derived constructions, but says nothing that identifies the required ordinary FreeMon colimit with that derived construction. This route has therefore not removed the comparison problem.

Bergner, *Simplicial monoids and Segal categories*, primary author PDF, was opened at Definitions 1.1–1.5 and the free-monoid/Segal localization argument in Proposition 4.2, Lemma 4.6 and Proposition 4.7. The separate three-page correction arXiv:0806.1767 was opened in full: the original Proposition 3.12 proposed a nonadjoint pair, and the corrected rigidification uses the strictly local algebraic-theory formulation. Neither the uncorrected adjunction nor a false claim that arbitrary colimits commute with products is used. A precise cofibrancy or forest-coherence comparison would still be needed for C_delta.

The source records are `D_root_attempt_refs.bib`. These failed applications are recorded as failed applications, not as flaws in the corrected cited theorems.
