# Independent audit of the enriched type-category comparison

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). This is an independent verification within the present collaboration, not an assertion of priority. The source argument at VII ms. 83–93, the companion's run-by-run contraction at ms. 86, and the relevant localization arguments at VII ms. 64–74 and 116–117 were read directly. The audit conclusion is **positive for the stated nerve weak-equivalence comparisons**. It does not prove invertibility in Cat hot.

## 1. Exact categories and enrichment

A type is a finite signed word, including the empty word. Its interval category has numbered vertices and generating arrows oriented according to the signs; it is a finite poset. Ty has nondecreasing, endpoint-preserving interval functors as arrows. Let P(τ,σ) have those same arrows as objects and all endpoint-identity natural transformations as morphisms. Horizontal composition and whiskering make these P into the hom-categories of a strict Cat-enriched category with the objects of Ty.

For a relative category (M,Σ), with Σ a wide subcategory, let Fτ be the full category of Σ-paths of type τ with fixed endpoints a,b, with arbitrary vertical natural transformations and identity endpoint components. There is an actual functor

\[
P(\tau,\sigma)\times F_\sigma\longrightarrow F_\tau.
\]

On objects it is precomposition. On arrows it is the usual horizontal composition of natural transformations. A backward source edge under a type map becomes an identity or a composite of backward target edges. The wide-subcategory assumption on Σ is precisely what makes this preserve the object condition. A parameter transformation may map under a path functor to an arbitrary arrow of M, so allowing arbitrary verticals is essential. The same construction does not automatically preserve a restriction that all vertical components lie in Σ.

Associativity, units, and endpoint identities hold strictly before realization. Thus this is substantially more information than a choice of unrelated pairwise homotopies between parallel pullback functors.

## 2. Check of the mapping-category contraction

The manuscript proves connectedness and explicitly doubts that its quickest map is terminal. The companion supplies an additional construction, which was checked here rather than accepted as authority.

If the target is empty, P is terminal. If the initial signs disagree, every admissible map is constant on the first source run; deleting that run gives an isomorphism of mapping categories. In the matching-sign case, let the first source and target runs have lengths a,b. The map h(j)=max(j,b) is a functor of the target interval: it collapses the first run and fixes all later generating edges. Define

\[
(RF)(0)=0,\qquad (RF)(i)=h(F(i))\quad (i>0).
\]

The first source run cannot cross the first target turn. Therefore RF maps its first edge across the entire first target run and the remaining edges of that source run to identities. It is again a nondecreasing endpoint-preserving functor. Applying h to natural-transformation components away from vertex zero defines an endofunctor R of P. Naturality holds because the target interval is thin.

There is a natural transformation id→R for an initially positive target run and R→id for an initially negative run. The components over both endpoints are identities. The image Q consists of maps with prescribed prefix 0,b,…,b; R restricts to the identity on Q. Deleting the first source and target runs identifies Q with the analogous mapping category for a target with one fewer run. Restriction and extension are inverse on morphisms because all removed components are forced identities. Induction gives a finite zigzag of natural transformations from id_P to a constant functor. Consequently BP is contractible whenever P is nonempty. This proof handles target/source length zero and forced initial deletions.

The contraction need not be natural in the ordered pair (τ,σ). Such extra naturality is not required below: the projection from the whole enriched category to the reachability preorder is already an actual enriched functor.

## 3. A precise model for descent to the preorder

Let R be the reachability preorder on types: its hom-set is a singleton exactly when P(τ,σ) is nonempty. Work in compactly generated spaces, where geometric realization of simplicial sets preserves finite products by its natural product homeomorphism. Applying B to the enriched composition and to the action above gives a topological category with hom-spaces BP and a strictly enriched contravariant diagram of spaces BFτ. Taking singular complexes of the mapping spaces produces a locally Kan simplicial category T. The inclusion of the discrete set of type maps into its mapping space gives a genuine simplicial functor from the discretely enriched ordinary category Ty to T.

The projection T→R is identity on objects and is a weak equivalence on every mapping space: both sides are empty together, and otherwise the source is contractible and the target a point. Its homotopy-coherent nerve is therefore an equivalence of infinity-categories. For the contravariant argument one can apply this directly to the swapped-hom simplicial category T^op→R^op, avoiding any need to assert strict commutation of a nerve construction with opposition.

The enriched action yields an infinity-functor on the coherent nerve of T^op with values in spaces. Restriction along the equivalence to NR^op is an equivalence of functor infinity-categories. Hence there exists G:NR^op→Spaces and an equivalence of diagrams

\[
BF\simeq q^*G\quad\text{on }N\mathrm{Ty}^{\mathrm{op}},
\]

where q:Ty^op→R^op is the ordinary reachability quotient. This is an equivalence of coherent diagrams, not just objectwise equivalences or equality in the ordinary homotopy category. Existence is enough; no canonical strict representative G is needed.

The standard facts used here were checked in Lurie's author-maintained Kerodon: §4.6.7, especially Theorem 4.6.7.5 and the stated locally Kan hypothesis; Theorem 4.8.4.1; and Proposition 4.5.4.8. The actual argument requires the equivalence on functor categories, which the last proposition explicitly supplies. The construction of a spaces-valued enriched diagram may use the topological category of CW spaces and compactly generated mapping spaces; the BFτ are CW realizations.

## 4. Cofinality and its variance

For σ in R^op, the under-comma category σ/q is the opposite of the full subcategory

\[
\mathrm{Ty}_\sigma=\{\tau:\mathrm{Ty}(\tau,\sigma)\ne\varnothing\}.
\]

There is no extra choice of a type map in this comma category because its arrow σ→qτ lies in the preorder R^op. This distinction is decisive: the ordinary comma of a sequence directly over Ty has much more data and is not being asserted contractible.

The functor H(τ)=σ*τ of Ty_σ is well-defined. The projection collapsing the τ block gives Hτ→σ, so Hτ remains supported. The projection collapsing the σ block gives Hτ→τ. On an arrow f, Hf=idσ*f. Both projections are natural, giving H→id and H→constσ, and therefore contracting B Ty_σ. This checks q's homotopy-finality in exactly the variance needed for colimits over Ty^op.

Let t:N^op→Ty be any strict sequence cofinal in the reachability preorder. For v=qt^op:N→R^op, the category σ/v is the full subposet

\[
\{n:\mathrm{Ty}(t_n,\sigma)\ne\varnothing\}\subseteq\mathbb N.
\]

It is nonempty by cofinality and upward closed because t_{n'}→t_n for n'≥n. It has a least element and hence contractible nerve. Thus v is homotopy final. The comma criterion was checked in Kerodon, Theorem 7.2.3.1; its right-cofinal convention is the colimit convention used here.

## 5. Why the specified comparison map is a weak equivalence

Using the equivalence BF≃q*G, the natural maps to colim_Rop G give a commuting triangle in spaces

\[
\operatorname{colim}_{\mathbb N}BF_{t_n}
\longrightarrow
\operatorname{colim}_{\mathrm{Ty}^{\mathrm{op}}}BF
\longrightarrow
\operatorname{colim}_{R^{\mathrm{op}}}G.
\]

The right-hand map and the composite are equivalences by the two finality results. Therefore the first, specified map is an equivalence. Naturality of the chosen equivalence of diagrams makes this triangle commute; the argument does not compare three unrelated abstract homotopy types.

Thomason's natural comparison identifies the middle space with the nerve realization of the fibred total category and the left space with that of its pullback along t. For the fibred convention this follows by taking opposites in the usual opfibrational theorem and using the natural realization homeomorphism reversing a nerve. Accordingly the map just proved equivalent is the actual functor from the sequential fibred total to the all-type fibred total. The sequential total-to-Cat-colimit functor is separately a weak equivalence by A.2.

These arguments endorse the nerve/Hot portions of the proposed E26 comparison. They supply compatible comparison maps for strict sequence maps because all operations used to identify the actual functors are natural. They do not, by themselves, prove a Cat hot inverse for the total-to-colimit functor or for other weak equivalences.

For products and concatenations, the proof still needs the actual block maps to be specified and their diagrams checked. If those are strict natural transformations of the stated sequence diagrams, the preceding naturality supplies the desired Hot identities. No implication from pairwise homotopies alone to coherent associativity is being asserted in this audit.

## 6. Independent check of D.K5's localization formula

The use of arbitrary vertical arrows in the path fibres does not invalidate the ordinary localization formula. For a commuting ladder, write its vertical components α_i. A forward square gives α_{i+1}f_i=g_iα_i. A backward square gives g_iα_{i+1}=α_if_i with f_i,g_i in Σ. After inverting those horizontal arrows, the latter becomes α_{i+1}f_i^{-1}=g_i^{-1}α_i. Telescoping along the word and using identity endpoint components proves equality of the represented localization morphisms. No vertical component is inverted in this calculation.

Conversely, composition of consecutive equal-sign arrows is a type-reparametrization, and identities are inserted or removed by collapses. The cancellation of w followed by w^{-1} is realized by the path a→b←a: the constant path at a maps to it by middle component w. The other cancellation is realized by the analogous −+ path with a transformation from that backtrack to the constant path. These are valid relative paths and endpoint-fixed transformations. The defining relations of ordinary localization are therefore generated by the type changes and path transformations used in the total path category.

For every small X there is a literal exponential isomorphism

\[
F_\tau(M^X,\Sigma_X;a_X,b_X)
\cong\operatorname{Fun}(X,F_\tau(M,\Sigma;a,b)),
\]

including morphisms and all type reindexings. A localization word in M^X has a single finite type for the entire X diagram. Its equality proof is finite in the presentation of that category, irrespective of the cardinality of X. Applying the sequence-to-total comparison above to (M^X,Σ_X), then taking π₀ and using the filtered sequential comparison A.2, gives exactly

\[
\operatorname{Hom}_{M^X[\Sigma_X^{-1}]}(a_X,b_X)
\cong\operatorname{colim}_{n}\pi_0\operatorname{Fun}(X,F_{t_n}).
\]

This independently endorses the ind-representability input in D.K5, for full path fibres and a cofinal type sequence. It does not replace a full path fibre by the narrower weak-vertical zigzag category J and does not assert that exponentiation preserves its sequential ordinary colimit.

## Checked web references

- Lurie, J. (2026). *Kerodon*. §4.6.7, [tag 01LA](https://kerodon.net/tag/01LA). Full page opened; local-Kan and mapping-space comparison statements checked.
- Lurie, J. (2026). *Kerodon*. Theorem 4.8.4.1, [tag 01JX](https://kerodon.net/tag/01JX). Full statement and proof opened.
- Lurie, J. (2026). *Kerodon*. Proposition 4.5.4.8, [tag 01E7](https://kerodon.net/tag/01E7). Full statement and proof opened; functor-category equivalence is clause (3).
- Lurie, J. (2026). *Kerodon*. Theorem 7.2.3.1, [tag 02NX](https://kerodon.net/tag/02NX). Full section opened; comma variance and cofinality criterion checked.
- Cegarra, A. M. (2020). Cohomology of homotopy colimits of simplicial sets and small categories. *Mathematics, 8*(6), 981. [https://doi.org/10.3390/math8060981](https://doi.org/10.3390/math8060981). Section 3, equation (9), Theorem 3 and proof opened earlier in this run for the natural Grothendieck/homotopy-colimit comparison.
