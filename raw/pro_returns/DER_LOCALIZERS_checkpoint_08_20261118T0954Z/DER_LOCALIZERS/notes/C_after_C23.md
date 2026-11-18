# Research after C.23

Historical starting status: the full general-M and raw-adjoint gates were open. Current update: C.26 now refutes the full general-M theorem; only the separate corollary raw-adjoint gate remains open. This note records investigations after the accepted enough-injectives theorem; none of the route observations below is being counted as closure of a main gate.

## Normalization already propagates through degree one on free coefficients

Let Q be an injective k-module and let U=k^(I). Derived adjunction, projective resolutions in M, and exactness of Hom_k(-,Q) identify

    Hom_k(L_n phi(X),Q) = Ext_M^n(X,kappa Q).

Normalization gives Ext_M^n(1,kappa Q)=0 for n>0. For n=1 this extends to X=coproduct_I 1 without AB4: any extension 0→kappa Q→E→coproduct_I 1→0 pulls back to a split extension on every summand. Choosing the sections and using the universal property of the coproduct gives a section on the entire coproduct. Hence L_1 phi(kappa U)=0, since injective k-modules detect nonzero modules. The canonical degree-zero comparison is also an isomorphism: phi and kappa preserve coproducts, and phi(1)=k canonically. Thus a normalization failure first appearing on an infinite free coefficient would have to occur in degree at least two. We do not extrapolate the splitting argument to higher Yoneda extensions.

If the unit itself is projective in M, this candidate mechanism disappears altogether. Coproducts of projectives are projective, independently of AB4, because their Hom functors are products of exact Hom functors to abelian groups. Thus kappa(k^(I)) is projective; normalization and the ordinary coefficient resolution prove the derived counit on every k-module. In particular a represented-unit Neeman/Day construction cannot fail by this scalar-coefficient mechanism.

## Exact source checks on the coproduct obstruction

We opened Argudín-Monroy, *The Yoneda Ext and arbitrary coproducts in abelian categories*, arXiv:1904.12182v2 (8 September 2020), 20 pages; the published metadata is Glasgow Mathematical Journal64(2)(2022),277–291, DOI10.1017/S0017089521000070. We read Proposition3.11's degree-one injectivity proof, the discussion after Theorem3.13 on printed p14, Corollary3.14, and Theorems4.3–4.4. The paper explicitly distinguishes the always-injective degree-one coproduct comparison from the higher comparison, whose general injectivity it does not claim. Its equivalence with AB4 concerns bijectivity. This supports the scope distinction above, not a present-day claim that the broader question is still unsolved. PDF: https://arxiv.org/pdf/1904.12182 . A local PDF and text copy were saved.

We also opened the current arXiv PDF of Argudín-Monroy–Parra, *Exactness of limits and colimits in abelian categories revisited*, arXiv:2203.15096v2, dated21July2026, 16 pages. We read the Introduction, Corollary10 and its preceding explanation, and §4.1 Proposition13 with its proof. Corollary10 confirms the enough-injectives/AB4 and enough-projectives/AB4* implications used in our direct argument. Proposition13 extends the latter implication to projective effacements. This does not make arbitrary filtered colimits exact or furnish enough injectives from the original interval assumptions. PDF: https://arxiv.org/pdf/2203.15096 .

Finally we opened Psaroudakis–Vitória, *Realisation functors in tilting theory*, arXiv:1511.02677v3 (25July2017), 46 pages; publication Math. Z.288(2018),965–1028, DOI10.1007/s00209-017-1923-y. We read Definition6.8 and Theorem6.9 with its proof on preprint pp32–33. The theorem assumes preservation of products and coproducts by the **derived** embedding, as well as the stated derived-category completeness conditions. It therefore cannot be used to infer derived coproduct preservation merely from the ordinary bireflective scalar embedding. The institutional PDF initially returned an Anubis access-denied page; the arXiv PDF was then opened and saved successfully. PDF: https://arxiv.org/pdf/1511.02677 .

## Search record

Queries submitted in this continuation:

- `"homological embedding" "coproducts" "abelian"`
- `"bireflective" "enough projectives" "derived"`
- `"Ext" "coproducts" "AB4" "vanishing"`
- `"THE YONEDA EXT AND ARBITRARY COPRODUCTS" Monroy`
- `"Realisation functors in tilting theory" authors arxiv`
- `"Ext" "coproducts" "injective" "Argudín"`
- `"Ext" "Ab3" "injective" "n"`
- `"Yoneda Ext" "coproducts" "counterexample"`
- `"Exactness of limits and colimits in abelian categories revisited"`
- `"Ab3" "higher" "Ext" coproducts injective`
- `"coproducts" "Ext" "injectivity" "Argudín"`

Search-result snippets and third-party abstracts were used as locators only. The claims above were checked in opened primary PDFs. The searches did not produce a theorem eliminating the higher relative-coproduct obstruction; this is a limited search result, not a completeness assertion.
