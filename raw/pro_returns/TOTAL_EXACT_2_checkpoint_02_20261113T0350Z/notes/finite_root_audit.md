# Independent audit of the root's arithmetic and source sections

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. This is an independent mathematical audit of `sections/main_question.tex` and `sections/statements_sources.tex`, with the underlying supplied arguments read where the new section abbreviates them. It makes no priority claim and does not decide either the totality-to-exactness question or infinite-stage AKR survival.

## Conclusion

No mathematical error was found in the fieldwise exactness theorem, the known class-diagram reductions, the fixed-positive-truncation argument, the universal-cover classification, the simplicial-circle counterexample, or the stated manuscript typing corrections. The hypotheses used by those proofs match their statements, including the empty and disconnected cases where asserted.

The following are optional clarity improvements rather than corrections to a false argument:

1. In the abbreviated simply connected case for `D:truncation`, say that the constant point diagram makes the base itself an n-type. The supplied full proof explicitly does this; it is needed together with connectivity of the projection to identify its fibres as K(L,n).
2. Cite Isbell–Mitchell (1976), Corollary 4.6, directly for the bounded-hom-set exclusion. Proposition 4.5 supplies the argument immediately before it, so the existing attribution is not false, but Corollary 4.6 is the precise named conclusion.
3. For AKR's Ore condition I, one can spell out that a common successor first moves the two codomains of a span to one object, after which a quasi-filter of the resulting parallel pair supplies a cross relation. Merely saying that every finite diagram occurs at a finite stage would not establish the Ore square without these ingredients; both ingredients are already present in the proof.

## A:fieldwise — arithmetic reduction

The theorem is valid for every small category and needs no totality, connectedness or nonemptiness assumption.

For a diagram of Q-modules or F_p-modules, the direct-sum-and-relations construction of its abelian-group colimit is already a module construction: the relation subgroup is closed under the field's scalar action. Forgetting scalars therefore preserves this colimit and is exact. This proves the easy implication without any base-change assumption.

For the converse, the normalized simplicial replacement over Z and the one over a field are literally the same complex after restriction of scalars. Exactness of the field-valued colimit functor therefore makes every field-valued diagram acyclic for all positive integral derived colimits. No claim that F_p is flat over Z enters here.

The class of acyclic diagrams is closed under arbitrary direct sums, filtered colimits, extensions and kernels of epimorphisms between acyclic diagrams. Each assertion follows from the displayed bar complex and its long exact homology sequence. For a p-primary torsion diagram, the functorial filtration by M[p^n] has F_p-module successive quotients. Taking its union proves acyclicity; the direct sum over primes handles all torsion. For a torsion-free diagram N, the natural injection N → Q⊗N has a torsion cokernel, so the kernel closure proves acyclicity of N. The torsion sequence then proves acyclicity of every diagram.

The conclusion that a counterexample over Z must fail over Q or some F_p is therefore justified. The qualification that the obstructing diagram need not be the literal reduction of the original diagram is necessary and correctly included. The theorem does not decide exactness over any of these fields for total categories.

## D:known-diagram — exact, total and quasi-filtered

The bar complex of Z[H] is the integral nerve-chain complex of the covariant category of elements. Exactness thus gives acyclicity of its components. The dependent-sum action on A really transports every set action on a component E of that element category, so the same acyclicity applies to all such actions on E. This inheritance is the essential point: it is not a replacement of permutation modules by arbitrary modules.

For a cyclic subgroup C of π_1(BE,e), the groupoid action Hom(e,−)/C has connected total space with fundamental group C. Its first homology is C because a cyclic group is already abelian. Acyclicity kills every cyclic subgroup, hence the whole fundamental group. Hurewicz then proves weak contractibility of the connected CW space BE. The order and variance of this argument are correct.

For totality implying common successors, each principal cosieve is nonempty and connected. If two such cosieves are disjoint, the double action gives two copies of BA glued along their disjoint union, whose first reduced homology is Z when BA is contractible. This contradicts totality. Applying common successors in the inherited total category p/A produces commuting Ore squares. The separately audited pair calculation gives the quasi-filter condition IV.

The ordinal-injection proof in the supplied TOTASPH C.8–C.10 was inspected, rather than inferred from the bibliographic announcement. The gap-polynomial formula, integral interpolation on compatible coordinate restrictions, augmentation-one condition and coface-to-arbitrary-injection induction are consistent. The two distinct point inclusions cannot be post-equalized by an injection, so strictness of filtered ⊊ exact follows. The new section correctly says that the body of Isbell (1974) was not obtained.

AKR's common successors and quasi-filters are present at the union because every relevant object or parallel pair is present at some finite stage. Their implication of I and IV is valid. Nonexactness is established by the separate simultaneous-column/private-incidence argument, without assuming that the category is total. Thus the composite strictness does not decide either intermediate inclusion, exactly as stated.

## D:manuscript — the fixed-positive-level test

For a total connected category BA is contractible. For n ≥ 2, the homotopy colimit X_M of K(M,n) is (n−1)-connected. If it is an n-type, its canonical map to K(colim M,n) is a weak equivalence, since it induces the degree-n homology identification. The reduced bar spectral sequence has row n equal to M and row n+1 zero. Its only contribution in total degree n+1 is T_1(M), with no possible nonzero incoming or outgoing differential. The low-homology fact H_{n+1}K(M,n)=0 is valid for arbitrary abelian M, including torsion.

After exactness is proved, naturality of the homology comparison and the split cross summand in degree 2n for K(M⊕N,n) identify colim(M⊗N) with colim M⊗colim N. There is no positive-positive Künneth Tor term in degree 2n, since its two positive indices would have sum 2n−1 and both would be at least n. Evaluation on covariant representables forces the cospan category C_{p,q} to have exactly one component, hence gives siftedness. Inherited totality in that cospan category then gives ordinary equalizers of parallel arrows, proving filteredness.

For n=1, common successors make the group colimit of an abelian diagram abelian. The fundamental-group presentation of the homotopy colimit has no residual base fundamental group because BA is contractible. In total degree two the spectral sequence has a quotient T_1(M), while the edge image is the image of colim Λ²M → Λ²(colim M). Transporting two representatives to a common successor proves that this edge map is surjective, so T_1(M)=0. The cross summand of Λ²(M⊕N) gives the same tensor comparison. These steps do not assume filteredness prematurely.

The Δop example has the correct variance: the covariant category of elements of the simplicial circle H=Δ[1]/∂Δ[1] is opposite to its usual simplex category. Its classifying space is S¹. The cospan category for [m],[n] in Δop is opposite to the simplex category of Δ[m]×Δ[n], which is nonempty and connected. Thus Δop is sifted and not total. This refutes the stated siftedness-to-totality implication, without using a different definition of totality.

## D:truncation — R6 and the categorical universal cover

The definition C_a = El_A Hom_{ΠA}(a,ℓ(−)) has the correct covariant variance. Its transition maps are bijective, and lifting edge paths identifies it with the connected universal covering category of the component of a. A dependent sum of a diagram on a category of elements has exactly the same simplicial replacement as the corresponding diagram on A. Since disjoint unions preserve n-types, the preservation hypothesis therefore descends to C_a.

The full supplied simply connected proof was read. For n ≥ 2, both X_M and BC are n-types: the second statement comes from the constant point diagram. The projection X_M→BC is (n−1)-connected, and hence its fibres are K(L,n). Its section makes it a family of pointed Eilenberg–MacLane spaces. The space of based self-equivalences of K(L,n) has π_i given by reduced cohomology in degrees n−i, which vanishes for i>0, including reduced degree zero. Thus its classifying space is BAut(L), a 1-type. On simply connected BC that classifying map is null, so the family is fibrewise trivial. Relative homology in degree n+1 then vanishes and, by the reduced bar spectral sequence, equals T_1(M).

For n=1, the constant point diagram makes simply connected BC contractible. The double-cosieve action gives a module diagram with π_1 of its homotopy colimit equal to Z, while E²_{1,1}=Z survives to H_2. The only possible incoming differential is from H_3(BC)=0 and there is no outgoing differential. Thus absence of common successors contradicts the one-type hypothesis. The abelian one-type argument can then be applied.

In the converse direction, the pullback of BC_a→BA along hocolim_A X→BA is modeled by hocolim_{C_a} Xπ: a lifted bar chain is determined by the path class to its first object. Filteredness preserves n-types there; covering maps preserve homotopy groups in degrees at least two. Since n ≥ 1, this proves the required truncation downstairs, including components and empty diagrams. The empty indexing category makes both assertions vacuous. No conclusion for n=0 is substituted.

## Manuscript typing and literature precision

For f:X→Y, the finality comma category is y\X, formed using f. The printed y\Y has initial object id_y and would make the condition vacuous. For H′ a presheaf on U′, the typed slice is U′/H′. Reversing the category when turning a presheaf into a covariant action reverses its category of elements and does not change the classifying-space homotopy type. The section accurately restricts its provenance to the supplied transcription, not an independent authoritative-edition collation.

The primary Adámek–Reiterman (1976) PDF was reopened for this audit. Its I.2(a–c), printed pp.97–98, states the valid Set-colimit distinctions. Its II.3, p.100, repeats the false equivalence between exact abelian colimits and the fixed-point property for indecomposable set-valued representations. AKR (1981), A.4, p.370, explicitly corrects the earlier 1975 remark by distinguishing pairwise affine equalization (3*) from finite simultaneous affine equalization (3). The resulting counterexample also refutes the repeated 1976 II.3 assertion. AKR A.4 does not explicitly cite that later II.3, so the access note records this distinction.

## Files actually checked

- `TOTEX2/sections/main_question.tex`.
- `TOTEX2/sections/statements_sources.tex`.
- `background/TOTASPH/TOTASPH_C.tex`, including the polynomial/coface argument.
- `background/TOTEX_return/TOTEX_paper.tex`, the fixed-positive-level and categorical-cover proofs, especially D.5, D.7, D.9 and D.10 in the supplied numbering.
- `TOTEX2/sources/IsbellMitchell1973.txt` and `IsbellMitchell1976.txt`, with the source audits already recorded in `notes/literature.md`.
- `TOTEX2/sources/AdamekReiterman1976.pdf`, I.2 and II.3, read in full text.
- `TOTEX2/code/akr_source_images/page-03.png` and `page-04.png`, printed pp.369–370, including A.4.

No finite computation is used to infer any of the infinite statements audited here.
