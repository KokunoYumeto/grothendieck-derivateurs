# Independent audit of Parts G–J

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim. The proofs are in `GHIJ_agent.tex`, and primary bibliographic records are in `GHIJ_agent_references.bib`. This is a record of completed and unresolved work, not a claim that every requested research problem has been settled.

## Principal results

The bounded-interval homotopy-colimit formula in G(1) is false: the cosheaf represented by the point at zero acquires nonempty inverse images over every nonempty interval, including `(1,2)`. This refutes the formula only, not the proposed localization equivalence. Every local product projection preserves the open-test class, by rectangle-cover Cech codescent and locality on the source (G.5). The Cantor projection to a point then proves that this preserving class strictly exceeds Volpe's shape submersions. The known stable compact-support Verdier transform is distinguished from a false pointed-space analogue: on the real line the latter kills the nonzero constant `S^0` sheaf.

BISITE D.11 has a second proof by barycentric normalization and nonabelian proper base change, with arbitrary sheaf coefficients and the canonical adjunction mate. An independent program computes both sides for every proper map between posets with at most five objects. The unmodified extension to finite categories fails for the one-object idempotent monoid `{1,e}`, `e²=e`.

For one forgotten mark, all noncontractible outgoing exit lifting categories are `B Z`: the exceptional case is a rational bridge whose image node is smoothed. Incoming exit lifts are contractible, by an algebraic graph-of-groups argument. The exact normalized lift presentation retains all automorphism groups. The proofs extend to all stable `(g,n)`. Geometric direct image agrees with right Kan extension for the moduli stack, actual point fibres and actual closed unions of boundary strata.

The maximum diagonal-stable smooth subclass is precisely the discrete fibrations. Universal ambidexterity within it means isomorphisms for spaces, inclusions of unions of components for pointed spaces, and finite discrete bifibrations for spectra or `D(k)` with any nonzero field. The correspondence functor is constructed with the exact span universal property of Cnossen, Lenz, and Ramzi, including monoidal coherence. Strict-2-category fine recognition is proved for ordinary-category bases, with explicit relative inverses. Genuine 2-cell bases remain unresolved here.

## Every prompt subpart

| Item | Disposition |
|---|---|
| G(1), localization equivalence over `R` | **Open**, G.3. No replacement realization or full-faithfulness proof is supplied. |
| G(1), proposed interval realization | **Refuted**, G.1, already on a represented point cosheaf. |
| G(2), interval, circle, graphs, manifolds, CW complexes and locally compact bases | **Open**, G.3. No extension of the unproved real-line equivalence is asserted. |
| G(2), Cantor set, Hawaiian earring, rationals | **Open** for localization recognition. G.2 concerns a different, pullback-preservation question. |
| G(2), parametrized-space and Lurie comparison | **Known results recorded**, G.4. Shulman's theorem describes locally homotopically constant homotopy sheaves for locally compact CW bases, not all open-inverse-image cosheaves. |
| G(3), dual raw-space realization or general impossibility | **Open**, G.3. Neither requested alternative is established. |
| G(4), equality with shape submersions | **Refuted**, G.2, by Cantor-to-point. |
| G(4), local product projections and shape submersions | **Proved**, G.5, for arbitrary product factors. Open-cover Cech descent handles every open test and glues source charts. |
| G(4), exact full class and dual class | **Open as a full classification**, G.3. G.2 and G.5 establish strict containment of shape submersions. |
| G(5), complementary raw theories and both base-change theorems | **Open**, G.3. G.4 records Lurie's stable theorem and proves the pointed unstable compact-support counterexample. |
| H(1), finite-poset theorem | **Proved**, H.1, using the prompt's proper-base-change alternative. No factorization into elementary maps is asserted. |
| H(1), exhaustive finite computation | **Completed**, H.7: 96,372 proper maps, 5,536,094 stalk/coefficient cases each over `Q` and `F_2`, no discrepancies. |
| H(1), extension to finite categories | **Refuted in its unmodified minimum-object-stratum form**, H.2. Corrected coefficient or exodromy formulations are not excluded. |
| H(2), Jansen/STRATA conventions | **Verified**: exit `C`, entrance `C^op`; Jansen Construction 3.18, Proposition 3.23, Corollary 6.6, Theorem 6.7. |
| H(2), properness and all noncontractible lifts | **Proved**, H.3 and H.5, for all stable `(g,n)`. One forgotten point permits at most one `Z` factor. |
| H(2), `n=4,5` finite calculations | **Completed**, H.4: target mark counts 4 and 5 mean forgetting `5→4` and `6→5`. Finite presentations of the infinite lift categories are supplied. |
| H(2), right Kan/geometric direct image and boundary base change | **Proved in the stated scope**, H.6: moduli stacks, point fibres and actual closed boundary unions. No arbitrary pullback or clutching-normalization identification is claimed. |
| H(3), BISITE B.15 | **Proved by the independent Part D work**, reported in H.8 with dependency D.10: all 48 scalar entries agree. |
| I(1), correspondence coherence | **Proved**, I.3–I.5. The exact extension theorem's hypotheses and monoidal transformation conditions are checked. |
| I(1), maximum diagonal-stable subclass | **Proved**, I.1: discrete fibrations; dually discrete opfibrations. |
| I(1), smooth/étale/proper classification in that subclass | **Proved**, I.2, I.6 and I.8 for spaces, pointed spaces, spectra and `D(k)`. All allowed maps have trivial cohomological smooth/étale twist. |
| I(1), noninvertible prime | **Covered explicitly**, I.8: the finite-set fibre result requires no prime inversion; `BC_p` with `F_p` coefficients fails ambidexterity in the larger class. No classification for all group fibres or all presentable coefficients is claimed. |
| I(2), reversible accessible localizers | **Open**, I.7, including the interval from integral homology equivalences to `W_0` and the specified non-total example. |
| I(3), functorial bare-derivator construction or impossibility | **Open**, I.7. Neither a construction natural in all exact morphisms nor the demanded pair of counterexample derivators is supplied. |
| I(3), weakest enhancement and general iteration | **Open**, I.7, for the requested full generality. I.9 separately proves the chosen enhanced localized-space realization, finite iteration, and both concrete second-stage calculations for spectra and `D(F_p)`. |
| J(1), ordinary-category base | **Proved**, J.1, with the Street-nerve comparison. |
| J(1), walking noninvertible/invertible 2-cell, one-object generator, general base | **Open**, J.2. |
| J(2), universal strict-pullback criterion and boundary/comma tests | **Open**, J.3. |
| J(3), 2-derivator Der 4 and four-variance base change | **Open**, J.3. Absolute Theorem A and duality invariance do not supply this theorem. |

## Verification details

### Local product maps

For an open subset of a product, choose an open rectangle cover. Every finite intersection pulls back to a product of a fixed space and one of the given open-test weak equivalences. Products preserve weak homotopy equivalences. Open-cover Cech homotopy colimits recover arbitrary topological spaces without numerability or separation assumptions: the small-singular-simplex inclusion is a weak equivalence by subdivision, and the cover-index nerve over each small simplex is contractible. This proves the product case. For a locally product map, intersect an arbitrary open with the source charts and apply the same descent argument. The proof is G.5 and uses the verified exact source statements HA Proposition A.3.2 and Lemma A.3.3.

### Finite posets

For a target simplex with positive weights, retaining and renormalizing its lowest-level barycentric coordinates gives a proper map from the actual geometric fibre to the strict lowest-level fibre's realization. Its fibre over a point whose support ends at `p` is a smaller upper-level geometric fibre above `p`. Induction proves weak contractibility. Finite polyhedra satisfy the hypotheses of nonabelian proper base change (Lurie, 2009, Corollary 7.3.1.18) and finite-dimensional hypercompleteness. These yield `A ≃ r_*r^*A` for every sheaf, rather than only an equivalence on constant coefficients.

The normalization preserves minimum labels at every point, including cell boundaries. Thus the restricted coefficient is an actual inverse image with its specialization maps. An independent cellular-descent lemma proves `Γ(|NP|,ν_P^*D) ≃ lim_(P^op)D`: the minimum map from the face poset is initial, with comma categories given by subdivisions of `P_{≥p}`. The proof identifies the specified mate, not merely abstractly equivalent endpoints.

The computation enumerates all maps between representatives of the 88 isomorphism classes of posets of sizes zero through five. It examines 1,349,916 monotone maps. Properness uses explicit simplicial collapses of every relevant lift complex; a homologically acyclic but uncertified case would abort. None occurs. The geometric fibre is computed as a polytopal complex of products of simplices. The product boundary signs are implemented, `d²=0` is checked, and exact ranks use integer/gcd elimination or binary arithmetic. Constant and principal-cosieve coefficients are computed separately. The tests compare cohomology, while H.1 proves the canonical mate.

### Marked curves

After normalizing an exit arrow to `[1]:qσ→η`, outgoing lifts have objects `s⊆σ` with `qs=η`. For `H={d∈Δ_σ:φ(d)∈Δ_η}`, the morphisms from `s` to `t` are `H/Δ_s` when `s⊇t`, and empty otherwise; composition is addition modulo the source subgroup. The triangle equation forces representatives into `Δ_σ`, so no unrecorded component automorphisms survive. The twist map is a basis bijection, deletion of a single bubble coordinate, or addition of two bridge coordinates. The category has an initial object except when the bridge image is smoothed; then it is the one-object group `ker(Z²→Z)=Z`.

Incoming lifts normalize to `{ρ⊇σ:qρ=η}` in reverse inclusion. Cutting along `η` gives vertex surface groups and injective cyclic edge groups. The amalgamated-product/HNN normal-form theorem makes the coset graph a tree. Isotopy extension identifies vertices with single lifts, edges with duplicated-curve lifts, and peripheral disappearing curves with added leaves. Cutting along a prescribed `σ` reduces to this calculation or a pair-of-pants singleton. This replaces the lifted-geodesic argument without claiming that finite enumeration proves all-genus properness.

The geometric comparison separately uses local triviality of normalized smooth families with their marked/node sections, proper base change, naturality of exodromy, and uniqueness of the resulting right adjoints. Orbifold stabilizers are retained in positive genus. A boundary normalization is not substituted for a closed boundary inclusion.

| Calculation | Total | Contractible | `B Z` |
|---|---:|---:|---:|
| Forget 5 marks to 4 | 47 | 44 | 3 |
| Forget 6 marks to 5 | 766 | 696 | 70 |

The stable-split strata counts for 3, 4, 5 and 6 marks are 1, 4, 26 and 236. Counts by codimension are `(1)`, `(1,3)`, `(1,10,15)` and `(1,25,105,105)`. The lift presentations are finite descriptions of infinite categories, not finite group replacements for `Z`. Integral homology through degree three is `(Z,0,0,0)` or `(Z,Z,0,0)`, without torsion. The small-counterexample program additionally checks the idempotent category's laws, zero contraction, action and limit, and enumerates the incoming lifts for the cancellation counterexample in I.4.

## Inherited-proof audit

- **D.11:** complete with its cited cellular-exodromy and hypercompleteness inputs. Its multilevel fibre-cell initiality argument is not used as the second proof.
- **F.10:** the claim is correct with the stated enhancement. Contractible uniqueness describes the mechanism but the written argument does not name the extension theorem that certifies coherent span and monoidal choices. I.3 supplies that theorem. The failed Mann specialization is a warning about a proposed substitute, not an allegation that F.10 explicitly applies A.5.10 that way.
- **F.15:** agrees with Jansen after translating exit to entrance variance; the printed sign slip in Theorem 6.7's second stability inequality is not used.
- **F.16:** the normalized-poset and geodesic-tree proof is complete with the quoted point-pushing identification. H.5 replaces the geodesic step by algebraic normal forms.
- **F.17:** correctly restricts its comparison to point fibres and the stated actual closed boundary inclusions. It does not prove arbitrary geometric pullback compatibility.
- **C.5–C.10:** the absolute two-categorical results do not imply general relative recognition. Only ordinary bases are completed here.

## Primary-source register

“Verified” means the named statements and hypotheses were inspected in the primary text, not that every theorem of the paper was independently re-proved. Every unattached work specifically requested by the prompt is accounted for. Exact BibTeX entries are in the accompanying bibliography.

| Primary source | What was verified |
|---|---|
| Aoki, K. (2022). *Posets for which Verdier duality holds*, arXiv:2202.05312v1. Published in *Selecta Mathematica, 29*(5), Article 78 (2023), DOI `10.1007/s00029-023-00887-2`. https://arxiv.org/pdf/2202.05312 | **Verified:** Theorem A and its Gorenstein-star hypothesis; primary bibliographic metadata. No unstable duality inferred. |
| Volpe, M. (2025). The six operations in topology. *Journal of Topology, 18*(4), e70050. DOI `10.1112/topo.70050`. https://arxiv.org/pdf/2110.10212 | **Verified:** October 2025 version, Definition 3.23's essential local-product condition. |
| Heyer, C., & Mann, L. (2024). *6-Functor formalisms and smooth representations*, arXiv:2410.13038v1. https://arxiv.org/pdf/2410.13038 | **Verified:** §3.3 and Definition 4.6.1, including the recursive diagonal condition. |
| Mann, L. (2022). *A p-adic 6-functor formalism in rigid-analytic geometry*, arXiv:2206.02022. | **Verified in attached TeX:** Appendix A.5, especially suitable decompositions and Proposition A.5.10. |
| Cnossen, B., Lenz, T., & Ramzi, M. (2025). Universality of Barwick's unfurling construction. *International Mathematics Research Notices, 2025*(18), rnaf280. DOI `10.1093/imrn/rnaf280`. https://arxiv.org/pdf/2502.18278 | **Verified:** Corollary 2.6(2), including adjointable transformations. |
| Jansen, M. Ø. (2023). *Moduli stack of stable curves from a stratified homotopy viewpoint*, arXiv:2308.09551v2. https://arxiv.org/pdf/2308.09551 | **Verified:** Construction 3.18, Proposition 3.23, Corollary 6.6, Theorem 6.7, and the sign slip. No journal publication status asserted. |
| Kent, R. P., IV, Leininger, C. J., & Schleimer, S. (2009). Trees and mapping class groups. *Journal für die reine und angewandte Mathematik, 637*, 1–21. DOI `10.1515/CRELLE.2009.087`. https://arxiv.org/pdf/math/0611241 | **Verified:** Sections 2 and 7, especially the point-pushing fibre/coset description. |
| Ara, D., & Maltsiniotis, G. (2014). Vers une structure de catégorie de modèles à la Thomason sur la catégorie des n-catégories strictes. *Advances in Mathematics, 259*, 557–654. DOI `10.1016/j.aim.2014.03.013`. https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/nthom.pdf | **Verified:** Theorem 6.27 and Corollary 6.32 for **2-categories only**. No unrefereed higher-dimensional model claim used. |
| Ara, D., & Maltsiniotis, G. (2018). Un théorème A de Quillen pour les ∞-catégories strictes I: La preuve simpliciale. *Advances in Mathematics, 328*, 446–500. DOI `10.1016/j.aim.2018.01.018`. https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/thmAI.pdf | **Verified:** Theorem 5.2 and Remark 5.3, as an absolute slice theorem. |
| Ara, D., & Maltsiniotis, G. (2022). Comparaison des nerfs n-catégoriques. *Algebraic & Geometric Topology, 22*, 2867–2914. DOI `10.2140/agt.2022.22.2867`. https://arxiv.org/pdf/2010.00266 | **Verified:** Theorem 6.6, invariance under cell dualities. |
| Rijke, E., Shulman, M., & Spitters, B. (2020). Modalities in homotopy type theory. *Logical Methods in Computer Science, 16*(1), 2:1–2:79. DOI `10.23638/LMCS-16(1:2)2020`. https://lmcs.episciences.org/6015/pdf | **Verified:** Theorems 1.54 and 2.19 and Lemma 2.20. Not represented as a proof of I(2) or I(3). |
| Lurie, J. (2009). *Higher topos theory*. Princeton University Press. https://www.math.ias.edu/~lurie/papers/HTT.pdf | **Verified:** Proposition 4.2.4.4 and Corollary 7.3.1.18. |
| Lurie, J. (2017). *Higher algebra*, September 18 version. https://www.math.ias.edu/~lurie/papers/HA.pdf | **Verified:** Proposition A.3.2 and Lemma A.3.3, Theorem 5.5.5.1 and Proposition 5.5.5.10. No raw all-cosheaf realization theorem attributed. |
| Shulman, M. A. (2008). Parametrized spaces model locally constant homotopy sheaves. *Topology and its Applications, 155*(5), 412–432. DOI `10.1016/j.topol.2007.11.001`. https://arxiv.org/abs/0706.2874 | **Verified:** attached source, locally compact CW hypothesis and right Quillen embedding; author metadata. |

## Artifacts

- `code/GHIJ/finite_poset_direct_image.py`, `finite_poset_direct_image_max5.log`, `poset_direct_image_summary_max5.json`, `poset_direct_image_maps_max5.csv`, `poset_representatives_max5.json`.
- `code/GHIJ/marked_curve_lifts.py`, `marked_curve_lifts.csv`, `marked_curve_presentations.json`, `marked_curve_summary.json`, and `boundary_strata_3.json` through `boundary_strata_6.json`.
- `code/GHIJ/small_counterexamples.py` and `small_counterexamples.json`.
- `sections/GHIJ_agent.tex`, `GHIJ_agent_references.bib`, `GHIJ_agent_results.json` and this report.

Open statuses are deliberate limits of this return. Successful finite computation does not turn the unresolved infinite or relative recognition questions into theorems.
