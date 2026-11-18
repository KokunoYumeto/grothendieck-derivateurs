> Current scope update: the two-sort example in this note remains a pre-monoidal obstruction and C.25 excludes its copower-compatible tensors. A different three-sort construction is now the complete counterexample C.26 in sections/C.tex. The historical failed formulas below do not concern that accepted tensor.

# A complete abelian obstruction before the monoidal hypothesis

**Status: verified algebraic construction, not a counterexample to the manuscript.** No symmetric monoidal tensor with the required unit has been constructed. The example shows that exact bireflectivity, completeness, enough projectives, and canonical normalization on the single scalar unit do not by themselves propagate that normalization to arbitrary free scalar coefficients. It identifies a concrete remaining monoidal construction problem.

## The exact functor

Fix a field k, and put

    E(V) = coker(V → V**),       V* = Hom_k(V,k),

where the displayed map is evaluation. Duality of vector spaces is exact, evaluation is injective, and the kernel/cokernel sequence for a map between the two exact sequences shows that E is exact. It is additive and k-linear. We have E(k)=0, and more generally E(V)=0 for finite-dimensional V.

For an infinite set I and V=k^(I), the functor is nonzero. Identify V*=k^I. Choose a nonzero linear functional on k^I/k^(I), and compose with the quotient. It gives an element of V** that vanishes on every finitely supported element of k^I. A functional coming from evaluation at an element of V is a finite linear combination of coordinate functionals; if it vanishes on all finitely supported elements, all its coefficients are zero. Thus the chosen functional represents a nonzero element of E(V). This uses ordinary vector-space choice, not a cardinality hypothesis or a large-cardinal principle.

## The abelian category

On Vect_k × Vect_k define H(U,V)=(E(V),U) and the square-zero monad T=Id⊕H. Its multiplication, under the natural finite direct-sum identification T²=Id⊕H⊕H⊕H², is

    (x,h_1,h_2,h_12) ↦ (x,h_1+h_2).

The unit is the inclusion of Id. Additivity verifies the monad identities. Let A be its Eilenberg–Moore category. Explicitly an object is

    (U,V,a:U→V,b:E(V)→U),
    a b=0,       b E(a)=0.

A morphism (f,g) satisfies g a=a' f and f b=b' E(g). Kernels and cokernels are formed on the two underlying vector spaces: exactness of E supplies the induced operations and the required relations. Finite sums are likewise componentwise. Coimage-to-image is an isomorphism because it is one on the underlying vector spaces and the forgetful functor reflects isomorphisms. Therefore A is abelian, and its forgetful functor U_A:A→Vect² is exact and faithful.

All small limits exist and are created by the forgetful functor, as can also be checked directly. For example a product has underlying pair (product U_i, product V_i), with b induced by the maps E(product V_i)→E(V_i)→U_i. No preservation of infinite products by E is needed.

The free functor F is left adjoint to U_A and has underlying functor T. It is exact because T is exact. Its free objects are projective: Hom_A(F(W),-) is Hom_Vect²(W,U_A(-)), which is exact. The action map F(U_A X)→X is an epimorphism, with an underlying vector-space section supplied by the monad unit. Thus A has enough projectives.

All small coproducts exist as well, even though T is not assumed accessible. Each X is the coequalizer of the standard two maps F(T U_A X)⇒F(U_A X). For a set of objects X_i, take free objects on the direct sums of the indicated underlying vector spaces and take the cokernel of the difference of the two induced maps. The adjunction and the coequalizer presentation show directly that this object represents the coproduct of the X_i. Abelian cokernels then supply all small colimits. We are not identifying such coproducts with componentwise sums.

## The two scalar adjoints

Define

    kappa(W)=(W,0,0,0),
    phi(U,V,a,b)=coker b,
    psi(U,V,a,b)=ker a.

The morphism equations give actual adjunctions

    phi ⊣ kappa ⊣ psi.

Indeed a map X→kappa(W) is a map U→W annihilating b, whereas a map kappa(W)→X is a map W→U annihilated by a. The inclusion kappa is fully faithful and exact. It preserves all limits because those limits are componentwise on such objects. It preserves all colimits because it is left adjoint to psi. In particular kappa(W) is the actual k-linear copower of the object 1=kappa(k):

    Hom_A(kappa(W),X)=Hom_k(W,Hom_A(1,X)).

Thus this example has exactly the scalar-adjunction properties, not merely a substitute functor called “trivial scalars.”

## Projective resolutions and failure on infinite free coefficients

The free objects on the two sorts are

    P_0(W)=(W,W,id,0),
    P_1(W)=(E(W),W,0,id).

Both are projective for every W. If S_1(W)=(0,W,0,0), there are short exact sequences

    0→S_1(W)→P_0(W)→kappa(W)→0,
    0→kappa(E(W))→P_1(W)→S_1(W)→0.

The first epimorphism has component maps (id,0); the second has component maps (0,id). Iterating the two sequences gives the projective resolution with terms

    P_(2n)=P_0(E^n W),
    P_(2n+1)=P_1(E^n W).

The odd differential is (0,id), and the even differential of positive degree is (id,0), with the evident adjacent arguments. The displayed short exact sequences prove exactness at every degree.

Applying phi yields E^n(W) in each even homological degree 2n and zero in each odd degree; all differentials are zero. Consequently

    L_(2n) phi(kappa W)=E^n(W),
    L_(2n+1) phi(kappa W)=0.

The canonical degree-zero counit is the identity W→W. At W=k every positive group is zero, since E(k)=0. Thus the canonical normalization L phi(1)→k is a quasi-isomorphism. At an infinite-dimensional free W, however, L_2 phi(kappa W)=E(W) is nonzero, so the canonical derived counit fails.

The same construction exhibits failure of AB4 explicitly. Since E(k)=0, the first short exact sequence at W=k has a monomorphism P_1(k)→P_0(k). For W=k^(I), the coproduct of these maps is P_1(W)→P_0(W), because both families are free objects. Its kernel is kappa(E(W)), which is nonzero for I infinite. Thus the failure is an infinite coproduct of copies of one fixed monomorphism, rather than a varying family. The category has a projective generator P_0(k)⊕P_1(k), but it is not small: its Hom functor does not preserve these coproducts. No corollary hypothesis of a set of finitely presented projective generators is being claimed.

## The unresolved monoidal step

We have not equipped A with a symmetric monoidal k-bilinear tensor having unit kappa(k) and with kappa tensor-compatible. A usual graded tensor formula would have to combine b:E(V)→U with an arbitrary scalar factor W; the obvious attempt demands a natural map E(V⊗W)→E(V)⊗W, which has not been supplied. This blocks that formula, not every conceivable monoidal structure. In particular we do not silently assume that k-bilinearity means cocontinuity.

If an appropriate tensor on A were constructed, its nonnegative chain category would offer a direct full-counterexample route. The scalar functor would be kappa(W)[0], its left adjoint phi H_0, and the usual interval D^1(1) would give a degreewise split monomorphism X→D^1(1)⊗X with contractible target. Finite-diagonal projective comparisons identify the corresponding derived scalar functor with the total left-derived phi. The failure of the derived counit above would then prevent its localization from being an equivalence: the derived adjunction descends to the localization at the maps inverted by its left adjoint, and an equivalence there would have an invertible counit. Every assertion in this paragraph remains conditional on the missing tensor; the algebraic category alone does not answer the manuscript's full question.

## Focused prior-art search, 18 November 2026

This is a search record, not a claim of novelty or an exhaustive literature review. The queries below located standard categorical ingredients and related double-dual constructions. None of the results actually read during these searches identified the exact two-sort choice H(U,V)=(V**/V,U) together with the scalar-normalization/copower failure computed above. This limited negative search finding does not establish that the example is new.

Queries used across the two available search engines included: `"double dual" "square-zero" monad abelian`; `"double dual" "enough projectives" "coproducts"`; `"bireflective" "normalization" "coproducts"`; `"abelian category" "double dual" monad`; `"square-zero" "monad" "abelian"`; `"V**/V" functor abelian category`; `"bidual quotient" functor category`; `"double dual" "quotient" "exact functor" vector spaces`; `"square zero monad" additive`; `"monad" "non-exact coproducts"`; `"exact functor" "V^{**}/V"`; `"double dual" "Ab4"`; `"cokernel" "double dual" "exact functor" category`; `"unit" "derived" "coproducts" "bireflective"`; `"double dual" "square-zero monad"`; `"bidual quotient" "abelian"`; `"copowers" "unit" "homological" monoidal`; and `"V^{**}/V" category`. Focused follow-ups searched the titles/authors of the primary sources below. Several exact-phrase queries returned unrelated topological-bidual or enriched-category results; those were not used as evidence for C.24.

1. **Eilenberg–Moore, 1965.** Samuel Eilenberg and John C. Moore, *Adjoint functors and triples*, Illinois J. Math. 9 (1965), 381–398. Opened the complete primary PDF at <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/eilenberg-moore.pdf>. Read Proposition 5.1 and its kernel proof, Proposition 5.2 and its cokernel proof, and Proposition 5.3 on printed pp. 394–395. Proposition 5.3 gives precisely the standard abelianness/exact-forgetful result for an additive cokernel-preserving monad. We also read the ensuing projective-class and canonical-resolution discussion on pp. 395–396 and the examples on pp. 397–398. This supports the standard machinery, not an attribution of the exact E or the normalization failure. Web references: turn716821737view0 and turn416034439view2.

2. **Gao–Külshammer–Kvamme–Psaroudakis, 2024.** *A functorial approach to monomorphism categories II: Indecomposables*, Proc. London Math. Soc. 129(4) (2024), e12640, DOI 10.1112/plms.12640. Opened <https://arxiv.org/pdf/2303.07753>, version 3, dated 5 September 2024. Read Definition 2.2 and Propositions 2.3–2.4 on printed pp. 6–7; Proposition 2.4 attributes the abelian-monad statement to Eilenberg–Moore Proposition 5.3. This is a modern source pointer, not the origin of that result. The paper's free-monad hypotheses elsewhere are not being applied to our square-zero monad. Web references: turn291965639view0, turn787893634view1, turn942123633view0.

3. **Fossum–Griffith–Reiten, 1975.** *Trivial Extensions of Abelian Categories*, Lecture Notes in Mathematics 456, Springer, DOI 10.1007/BFb0065404. Opened the publisher landing page and its full ten-page front matter at <https://link.springer.com/content/pdf/bfm:978-3-540-37487-9/1>. Read the introduction, especially printed pp. vii–viii: it explicitly considers objects f:F(X)→X satisfying fF(f)=0 in an abelian category with an endofunctor F. Thus the general square-zero/trivial-extension construction used here is classical. The Generalities chapter, pp. 3–23, was identified at DOI 10.1007/BFb0065406, but its full text was not obtained: the publisher offers subscription access and a one-page preview. We do not attribute any uninspected theorem or this particular bidual-quotient example to that chapter. Web references: turn716821737view1, turn721350004view0–1.

4. **Kock, 1970.** Anders Kock, *On Double Dualization Monads*, Math. Scand. 27 (1970), 151–165, DOI 10.7146/math.scand.a-10995. The old publisher PDF URL returned HTTP 404 on direct opening. The current publisher metadata opened at <https://journals.msp.org/mscand/article/view/2331>, and the author's scanned PDF opened at <https://tildeweb.au.dk/au76680/DD.pdf>; its extraction had no readable lines. The search-indexed introduction identifies its subject as the double-internal-Hom monad and its relation to algebra structures (Theorem 3.2). That is different from the quotient E=V**/V and the square-zero monad Id⊕H here. We therefore use it only to distinguish related prior art, not as a checked proof of C.24 or of the missing tensor. Web references: turn291965639search8–9, turn787893634view0, turn841225305view0.

Bibliography and check-register additions were made after the parent released the CP05 metadata freeze at 06:55 UTC. The complete elementary proof of C.24 does not depend on a theorem hidden behind these access limitations.

## Tensor formulas examined, all still unsuccessful

The ordinary truncated-cochain tensor on the finite arrow objects suggests P_0(U)⊗P_0(V)=P_0(U⊗V)⊕P_1(U⊗V), P_0(U)⊗P_1(V)=P_1(U⊗V), and P_1(U)⊗P_1(V)=0. There is a canonical strength E(V)⊗W→E(V⊗W) for every k-linear E, so it is tempting to tensor a map beta:P_0(U)→P_1(V) using this strength. The parent checked an interchange obstruction: for the canonical a:P_1(V)→P_0(V), we have a beta=0, but the proposed a⊗id on the split P_0⊗P_0 decomposition has a nonzero identity component on P_1. The proposed composite (a⊗id)(beta⊗id) then retains the strength term. These formulas do not define a bifunctor. This excludes that attempted extension, not every symmetric tensor.

Smart truncation of a two-term cochain tensor changes the finite formulas, but its extension to a nonzero b still requires a map E(V⊗W)→E(V)⊗W for unrestricted scalar W. The available canonical strength has the opposite direction. A noncanonical vector-space splitting does not supply the required functoriality, associativity, and symmetry. No such splitting is asserted.

Another tempting finite formula makes the ideal of the two nonunit indecomposable arrow objects square-zero. Its cocontinuous extension is not immediate: although psi(S_1(k))=0, the actual copower of S_1(k) by W is P_1(W), with psi(P_1(W))=E(W). Consequently formulas that depend only on psi cease to associate after an infinite scalar copower. Again, this is a failed formula, not a proof that no compatible tensor exists.


A focused tensor follow-up searched `"trivial extension" "monoidal" category endofunctor`, `"square-zero" "bimonad"`, and `"monoidal" "double dual" "vector spaces" commutative monad`. It located Feng Qing and Huang Ju, *Two constructions of monoidal categories*, Journal of Shandong University (Natural Science) 51(4) (2016), 30–34, DOI 10.6040/j.issn.1671-9352.0.2015.187. The opened publisher abstract assumes an additive strict monoidal endofunctor. Full text was not obtained: the PDF link returned the same landing page, the public download endpoint had an unsupported content type in web retrieval, and direct retrieval returned HTTP403. Neither its exact notion of trivial extension nor its proof has been checked; this source does not supply the missing tensor. Exact-title, Chinese-title, and DOI searches found no independently readable full text in the results examined.

## Structural tensor obstruction after CP05

The complete proof is integrated as C.25 in `sections/C.tex` after independent root re-proof; `notes/C25_draft.tex` retains the accepted draft. It gives more than a failed formula. For every exact sequence 0→S→D→1→0 in an additive monoidal abelian category, the map Hom(1,S⊗X)→Hom(1,D⊗X) is injective for all X. We factor the difference (p⊗D)−(D⊗p) through S and use this factor to turn a purported kernel element beta into beta p=0. Applied to C.24, scalar-copower compatibility would identify the map with P_1(W)→P_0(W), whose kernel has a nonzero map from1 whenever E(W)≠0. Thus no cocontinuous monoidal tensor with the required unit can exist on this category, even without symmetry. The original manuscript's merely bilinear hypothesis is still weaker; that remaining possibility is not excluded.


## A separated-copower formula fails its canonical associativity

This is one attempted formula only; it does not exclude every merely bilinear tensor. For a vector space W and X in A, let

    R_W(X) = image(W·X → X^{W*}),

where · is the actual scalar copower, the superscript is the k-linear power, and the comparison is induced by all coefficient contractions lambda:W→k. This is an additive bifunctor with R_k(X)=X and R_W(1)=kappa W. Its temptation is that R_W(S)=S_1(W), so it removes the kappa E(W) obstruction in the copower P_1(W).

We check the canonical associativity comparison on X=P_1(Z). Here

    R_W(P_1(Z)) = (B_W, W⊗Z, 0, q_W),
    B_W = image(E(W⊗Z) → Hom_k(W*,E(Z))),

and q_W is the evident quotient map. The lambda component of the displayed map is E(lambda⊗id_Z). Applying R_V again gives first component the image of

    E(V⊗W⊗Z) → Hom_k(V*,Hom_k(W*,E(Z)))

with components E(f⊗g⊗id_Z). To verify this despite the first object not being free, use its epimorphism P_1(W⊗Z)→R_W(P_1(Z)); its kernel is kappa ker(q_W). Taking the V-copower preserves this cokernel. The map from E(V⊗W⊗Z) into the stated power kills that kernel and has the asserted image. The second component remains V⊗W⊗Z, since ordinary vector coefficient contractions are jointly injective.

In contrast, R_(V⊗W)(P_1(Z)) has first component the image of

    E(V⊗W⊗Z) → Hom_k((V⊗W)*,E(Z)).

The natural comparison to the two-step construction restricts along V*⊗W*→(V⊗W)*. It need not be injective. Take V=W=Z=k^(N), and define the infinite-rank bilinear form h by h(e_i,e_j)=delta_ij. Then h is outside F=V*⊗W* inside H=(V⊗W)*. Choose mu in Z** whose class in E(Z) is nonzero. The natural map H⊗Z*→(V⊗W⊗Z)* is injective. On its subspace (F+k h)⊗Z*, define a linear functional ell to be zero on F⊗Z* and to send h⊗z* to mu(z*). These prescriptions agree because F and k h have zero intersection. Extend ell linearly to all of (V⊗W⊗Z)*.

Thus ell belongs to (V⊗W⊗Z)**. Its class in E(V⊗W⊗Z) is killed by every decomposable contraction f⊗g but has h-contraction equal to the nonzero class of mu in E(Z). It therefore gives a nonzero element in the kernel of the canonical associativity comparison above. No alternate, noncanonical associator has been excluded by this calculation; in particular we do not call this a theorem excluding all Vect-actions or all merely bilinear monoidal products.
