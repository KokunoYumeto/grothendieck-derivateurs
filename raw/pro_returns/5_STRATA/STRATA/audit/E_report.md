# Part E audit record

## Scope and result

Part E contains twelve numbered statements: eight Proved, one Known, two Refuted, and one Open. The full ordinary strict-bifibration assertion of VIc-C008 remains unresolved in this audit. We prove existence for every small poset, more generally every small base with all arrows monic or all arrows epic, every base whose classifying space is a 1-type, and every local system with 1-truncated fibres over any base. There is no remaining poset-base existence gap. We do not describe the unrestricted assertion as a known open problem in the literature.

The distinction that matters is between ordinary cartesian/cocartesian universal arrows and homotopically contractible lifting categories. An ordinary bifibration has adjoint transport, and its transport functors are automatically nerve weak equivalences. Proper-and-smooth functors need not be bifibrations as specified ordinary functors. Part D supplies the finite diamond counterexample; Part E does not duplicate that program.

## Sources opened

The first mathematical source opened for Part E was Denis-Charles Cisinski, *Les préfaisceaux comme modèles des types d'homotopie* (2006), Theorem 5.3.14. Its full PDF was downloaded from the author's site, `https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf`, and pp.230–231 read. Proposition 5.3.13, Corollaries 6.4.8 and 6.4.16, and Theorem 6.4.15 were also read. The model-structure theorem is not a statement about Grothendieck bifibrations.

The supplied Chapter VI-c transcription and companion discussion at ms.186–195 were read, including VIc-C008 and the fork-support obstruction. The supplied Chapter XI §1 transcription (ms.127 onward) and Chapter XVI §4 (especially ms.41–44 and the comparison surrounding Theorem 4.4.13) were read. The CATHOT D.1 proof and its model-structure supplement were read. E.5 proves the additional classifying-space assertion directly using the simplex category.

Bryce Clarke, Gabriel Scherer, and Noam Zeilberger, *The free bifibration on a functor*, arXiv:2511.07314v3 (15 January 2026), was opened at the arXiv abstract and in full PDF. Theorem 1.17 and Propositions 1.23–1.24 were inspected. These give a free ordinary bifibration, a fully faithful unit, and a retraction of underlying categories. They do not state the weak-homotopy comparison needed for the present question. We do not infer that comparison from full faithfulness or a retraction alone.

François Lamarche, *Path functors in Cat*, HAL hal-00831430v3 (19 September 2013), was read through the indexed author manuscript. The direct HAL request returned HTTP 403 and the direct Citeseer PDF request returned HTTP 404; the browser-indexed complete text was available. Section 4 expressly says that its path-based weak equivalences differ from standard categorical nerve weak equivalences. This prevents an unqualified substitution for W∞. The description is a bibliographical boundary, not a claim that no useful comparison can exist.

A. M. Cegarra, *Cohomology of Homotopy Colimits of Simplicial Sets and Small Categories* (2020), was opened on the publisher's site; §3.1, equation (9), identifies the Thomason comparison explicitly. A final targeted search for the original 1979 Thomason paper used both search engines, its exact title, Theorem 1.2, and PDF-oriented queries. The publisher's Cambridge page was opened and verified the journal, 1979 publication year, pages 91–109, and DOI 10.1017/S0305004100055535, but exposed only the extract and references with a “Get access” notice. The publisher content endpoint was unavailable; no accessible primary full paper was found in that targeted search. The original theorem therefore remains honestly marked unverified. The already opened Cegarra formulation, rather than an inaccessible primary page, supplies the checked comparison used here.

Jacob Lurie, *Higher Topos Theory* (2009), was opened in the complete IAS-hosted PDF. Proposition A.2.8.2 gives the injective diagram model structure with objectwise cofibrations and weak equivalences. Proposition A.3.3.2 and Remark A.3.3.4 explicitly verify its simplicial model structure. We give the needed horn-lifting proof directly in E.10. The existing bibliography key FLurieHTT2009 is reused.

Zbigniew Fiedorowicz, *A counterexample to a group completion conjecture of J. C. Moore*, Algebraic & Geometric Topology 2 (2002), 33–35, was opened in full at arXiv math/0202260. Its unnumbered lemma on pp.33–34 identifies the five-element rectangular-band monoid's classifying space with S². The article includes a complete length-two projective resolution; we verify that resolution in E.11 and in the accompanying program.

## Literature searches

Searches used the phrases “Cisinski Les préfaisceaux 5.3.14 bifibration Thomason”, “Grothendieck bifibration homotopy local system every functor weak equivalence replacement”, “category contractible spaces bifibration locally constant functors adjoints”, “algebraic Kan fibrations base change left adjoint”, “free bifibration ordinary category adjoints homotopy equivalence”, “Lamarche Path functors homotopy”, and “Thomason 1979 Homotopy colimits category small categories Theorem 1.2”. Search results were treated as leads; claims used from the free-bifibration and Cisinski sources were read in the primary texts. Further searches used “bifibration injective simplicial”, “injective model structure simplicial A.3.3.2”, and “classifying space rectangular band monoid 2 sphere”; the model-structure and monoid claims were then checked in the primary texts. No priority claim is made for any argument in Part E.

## Computation

The program code/E_finite_checks.py verifies the finite chain examples of E.4, including the ordinary universal lifting property and its loss under the next inclusion. It checks the complete two-object four-arrow groupoid and point-patch obstruction of E.7. It checks the six-element sphere poset, its composition relation, boundary-square-zero identities, simplex counts, and rational homology; E.10 now settles its bifibration existence question affirmatively. Its sphere identification is proved by the join decomposition, not inferred from homology alone.

The same program checks the full multiplication table of the five-element rectangular-band monoid, all associativity and unit equations, every cancellation test, the idempotent right-module projectors, and the exact integral projective resolution used in E.11. The post-tensor chain complex is Z² → Z → Z with differentials (1,1) and zero, giving H₂=Z and no higher positive homology. The paper combines this with simple connectivity and Hurewicz–Whitehead, rather than inferring homotopy type from a finite bar truncation. Its complete output is code/E_finite_checks_output.txt.

The program code/E_make_register.py writes the twelve result-register rows and reports their status counts. Its output is saved separately.

## Corrections and exact boundaries

The added CATHOT patch lead has a positive classifying-space answer: BKλ(Y) is naturally weakly equivalent to Y. The associated raw opfibration does represent the local system, with the stated variance. The proposed adjoint step is false for these raw patch categories: inclusion of one vertex into the contractible two-object groupoid nerve produces postcomposition with neither adjoint. Enlarging the collection of nonempty domains alone cannot fix the strict-over-the-base vertex obstruction. This example does not refute the existence of a different bifibration representative.

E.10 repairs the patch route for all-mono or all-epi bases by replacing the entire diagram first. In presheaf variance, a monomorphism α:s→t makes the representable map h_s→h_t an injective cofibration. Injective fibrancy makes RF_t→RF_s a Kan fibration; locality makes it a trivial Kan fibration. Integrating the opposite patch categories gives the right-adjoint transports required of a Grothendieck fibration. The covariant all-epi argument is dual. The comparison is diagramwise and natural, with a uniform cardinal chosen for any specified small family of replacement models.

The alternating replacement provides a functorial perfect representative and a fibrewise equivalence on weak-fibration input. It does not by filtered-colimit reasoning alone provide ordinary universal lifts. The increasing-chain example demonstrates exactly which universal arrow fails to remain cartesian.

The read transcription of XI ms.131 displays a fibre map with wrong source/target labels: it must be X′_s→X_s for the displayed map X′→X. The type in XVI Lemma 4.4.1 must be p∈F in f=pi, as its later restatement confirms. No new correction to the mathematical content of the companion's strict-bifibration warning is asserted.

## Remaining exact question

E.11 retains unrestricted essential surjectivity outside the affirmative classes and the stronger general fibrewise-localization equivalence from VIc-C008. Its explicit remaining test is the one-object monoid M={1}∪{e_ij : i,j∈{0,1}}, with e_ij e_kl=e_il, and the path local system classified by *→BM≃S², whose fibre has type ΩS². Every nonidentity arrow fails both cancellation properties, so the representable inclusions required by E.10 are unavailable. The precise question is a strict bifibration with that local-system class and weakly contractible total category. One object is minimal for a nonempty base; no minimality among numbers of arrows is claimed.

The former six-element sphere-poset test is settled affirmatively by E.10 and is no longer presented as unresolved.

An algebraic-Kan-fibration attempt was considered: change of base has a plausible algebraic left adjoint, but its preservation of weakly contractible total spaces was not proved. Existing chosen fillers can collide under noninjective base maps, so merely calling the new cells “horn fillings” does not establish that comparison. A proof of that preservation statement, or a suitable homotopy theorem for the free-bifibration unit, would still be required before either route could be used.
