# Remaining raw-adjoint investigations after checkpoint 06

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 18 November 2026. No result below is a counterexample to C.raw_gate. The main gate remains C.10.

## R1. What the corollary already forces at the unit

Write the corollary category as Mod(M), let U be its tensor unit, and evaluate the scalar copower at a generator a. Then kappa(V)(a)=U(a) tensor_k V. Exactness and product preservation of kappa force U(a) to be a finitely generated projective k-module. This is the finite unit-coordinate fact used in C.22, not a new theorem.

Here is an elementary check. Product preservation for the family indexed by all elements of U(a), applied to copies of k, expresses the universal tuple of those elements as a finite sum of elementary tensors. Hence U(a) is finitely generated. Choose a finite free surjection k^n -> U(a), with kernel K. Flatness of U(a) makes K tensor k^I -> (k^I)^n injective. Comparing kernels with the product of the original sequence, and using product preservation for U(a), gives K tensor k^I = K^I. The same universal-tuple argument makes K finitely generated. Thus U(a) is finitely presented and flat, hence projective. This conclusion is pointwise; it does not make U finitely presented or projective as an M-module.

## R2. Why witnesswise scalar descent has not closed the gate

A homology cycle in F G K has finite outer tensor/bar support, but each coefficient of G K is a full chain map Q(a) -> K. It may have values on arbitrarily many generators in all degrees. Restricting Q and the coefficient ring to countable data retains the visible finite cycle, but changes the full Hom functor. New chain maps over the smaller data can provide a boundary that is not a boundary in the original problem. A selected Hom sort in a downward elementary substructure need not be the entire Hom over the smaller category.

Even if a selected bar subcomplex splits as a complex of coefficient modules, objectwise extensions of the new Hom maps do not automatically preserve all the naturality and tensor relations appearing in a boundary. No globally natural comparison from the complete descended coinduction to the original coinduction has been constructed. Therefore the finite support of an outer cycle is not by itself a reduction to C.22. The linear agent independently identified the same obstruction.

## R3. The interval-extension argument and its precise missing step

For a contractible complex K with projective components, the counit F G K -> K would make G K a retract of J tensor G K if it extended across the monomorphism F(alpha tensor G K). The extension is valid for injective coefficient disks, and under the separately proved pure-injective and finite-dimension hypotheses. A contractible complex with projective components need not be injective in the abelian category of complexes. Its contraction is not an extension theorem across arbitrary monomorphisms. Thus contractibility alone supplies no missing extension, and the underlying localization equivalence does not identify the raw right adjoint with its derived replacement.

A possible finite-unit variant remains incomplete. If U is finitely presented projective as an M-module, alpha lifts along a projective epimorphism P -> J and the lift factors through a finite coproduct P_fin of representables. The resulting u:U -> P_fin remains monic after tensoring with any X, since alpha tensor X factors through it. For a cocontinuous tensor, the induced maps from representable right-M coefficient modules are pure. If the receiving coefficient modules were projective, the finite presented pure submodules would split. The original hypotheses do not establish that projectivity, and P_fin is not established to be phi-acyclic. Accordingly this argument is not an interval replacement.

## R4. Standard possible counterexample categories do not provide one

Ordinary presheaf categories with pointwise tensor are already excluded by C.21. Standard chain-module categories, differential graded module constructions with the ordinary disk interval, and analogous constructions with an evaluationwise split disk are excluded by C.7 or C.17. Changing their tensor while retaining the same scalar functor does not change a raw-adjoint conclusion already proved using a good resolving functor.

A representation category of a cocommutative Hopf k-algebra H with its ordinary diagonal tensor cannot satisfy the interval hypothesis at all when k is nonzero. Its scalar functor is the trivial-module functor and phi is coinvariants. The usual Hopf isomorphism identifies J tensor_k H (diagonal action) with a free H-module induced from the underlying k-module of J; one may use the symmetry and the isomorphism h tensor j -> sum h_(1) tensor h_(2)j, whose inverse uses the antipode. Consequently phi(J tensor H) is the underlying k-module of J. Hypothesis (d) would make this zero, while alpha:k -> J is monic. This contradiction excludes the ordinary Hopf-representation attempt. It does not cover non-Hopf bialgebras, non-pointwise tensors, or arbitrary linear categories.

## R5. A limited observation on the repair of C.26

Suppose in addition that the internal tensor is cocontinuous and that the canonical derived counit is normalized on every scalar module, rather than only on k. Put S(X)=coker(alpha tensor X). Then S preserves coproducts and the short exact sequence X -> J tensor X -> S(X) gives Lphi S(X)=Lphi X[1]. For a sequence V_n of scalar modules define M_infinity as the coproduct of S^n kappa(V_n). Its tail starting at N is S^N of another object, hence has no derived phi-homology below N. Splitting M_infinity into a finite head and that tail therefore gives H_n Lphi(M_infinity)=V_n. Over a field every connective complex is isomorphic in the derived category to the sum of its homology groups in their degrees, so this proves essential surjectivity in that extra-normalization, cocontinuous, field scope without AB4.

This does not prove full faithfulness, does not settle the raw adjoint, and does not assert that the all-scalar normalization condition by itself repairs the unrestricted theorem. It is retained as a possible route toward the strongest repair, rather than counted as progress on an open principal row.

## R6. Accepted conditional flat-interval argument

C.27 proves a valid extension of the split-inclusion method when the tensor and unit are explicitly pointwise, J is a filtered colimit of finitely generated projective M-modules P_i, and alpha factors through one stage. Reindexing by the filtered undercategory gives compatible maps alpha_i. Each alpha_i tensor X is monic because its composite with the map to J tensor X is monic. On a scalar copower this proves that k to P_i(a) is pure. Since P_i(a) is k-projective, its image of 1 has finitely many coordinates in a free summand; their ideal must be the unit ideal by purity after tensoring with its quotient. A finite-coordinate functional therefore splits it.

The coordinate splittings need not be natural in a. They still split every degree of F(alpha_i tensor X), because F_n is a retract of a sum of evaluations. For split acyclic projective K, the counit F G K to K extends across this degreewise split inclusion. Adjunction gives a retraction of G K to P_i tensor G K at each individual stage. The retractions need not be compatible. For a homology class z of F G K, its image dies in the filtered colimit F(J tensor G K); exactness of filtered colimits puts that death at one later stage. The retraction at that later stage then makes z zero. This is the full C.10 raw test.

The proof assumes a filtered projective presentation of J and an actual stage factorization of alpha; these are not deduced from the manuscript. Finite presentation of the unit is only a sufficient condition for the factorization. The arbitrary tensor and arbitrary interval cases remain unresolved. We have not exhibited an instance satisfying these extra assumptions but outside every earlier sufficient class, so this conditional theorem is not separately claimed as strict principal movement in the stopping ledger.

## Source search and scope

Queries submitted in this block included `Grothendieck linear case interval derived functor`, `exact adjunction counit chain complexes localization`, `test category linear derived Grothendieck`, `Grothendieck k-lineaire intervalle Dold Kan`, and `categories test lineaires`. They returned the already recorded Hubert thesis and 2026 preprint, together with irrelevant linear-logic and general localization sources. We reopened the primary 2025 thesis at https://arxiv.org/pdf/2505.08321 and reread its warning 2.5.17 and comparison Proposition 2.7.10. The comparison in the latter concerns the complex-valued right adjoint; it does not identify its degree-zero raw truncation with a derived functor. No result was imported from search snippets or secondary summaries.
