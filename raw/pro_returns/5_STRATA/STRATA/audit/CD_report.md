# STRATA Parts C and D: audit record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No priority is claimed. The supplied companion, POLES, TOTASPH, and GALOIS files are drafts whose specified arguments were checked, rather than authorities from which their assertions were adopted wholesale.

## Deliverables and scope

The mathematical text is in `sections/C.tex` and `sections/D.tex`. The register `audit/CD_results.csv` contains 20 statements: 13 labelled Proved, four Known, and three Refuted. Its columns are exactly those requested in the prompt. The 12 entries in `audit/CD_references.bib` all have explicit verification notes. `code/CD_checks.py` and its captured output give the finite category, naturality, lifting, and homology checks. `code/CD_metadata.py` and its output reproduce the register and verify statement IDs, labels, proof delimiters, citation coverage, and bibliography verification notes.

Every coefficient construction uses presheaf variance, `D(X) = Ho Fun(X^op,C)`. A sieve is a downset/open indexing category. The geometric realization uses the minimum-vertex convention on `NX`, equivalently the last-vertex convention on `N(X^op)` with the opposite stratum order. The statements do not silently replace an arbitrary derivator by an infinity-category enhancement.

## Sources inspected

### Manuscript and supplied audits

We read the supplied transcription and companion blocks for I ms. 1–9, on support and exceptional adjoints, and I ms. 49–59, on the fibre-comma comparisons and the proper/smooth conditions. We checked the proper-cosieve assertion at Ib-C003 against the literal outgoing-lift definition. We read XII ms. 59–63 for the order/topology convention, the crossing bimodule, and the SGA 4 gluing description; the resulting conclusions are also compared with XII appendix ms. 17–18 and row XIIapp-G11.

The whole proof of POLES G.19 was inspected. We checked its three-fibre Grothendieck-construction category, its functor to `X`, the components and typing of both natural transformations in each comma category, and its empty cases. C.3 records these checks and compares its actual cocone with the homotopy-link evaluation prism. We do not give a third proof of the directed gluing theorem.

We read POLES G.8 to identify the failed reverse integral-smoothness assertion. **No reverse integral-smoothness implication from POLES G.8 is used anywhere in Parts C or D.** Neither reverse excision nor inference of componentwise contractibility from contractibility of a total gluing is used. The categorical proper/smooth tests are instead verified directly from the exact lifting categories.

We read and independently checked TOTASPH F.14, F.18, and F.21. Their roles are sharply separated: F.14 supplies a degreewise crossing-weight criterion to audit; F.18 supplies the seven-arrow couniversal attachment with a disconnected individual crossing category; F.21 supplies the eleven-arrow attachment whose ordinary weighted coend fails to preserve an objectwise equivalence. We proved the universal pushout assertions by relative natural transformations, not by finite enumeration.

GALOIS A.8 and B.3/B.5 provide the previously audited locally constant comparison and abstract-derivator invariance context. C.8 makes its additional enhancement hypothesis explicit. GALOIS D.9's correction to Ib-C003 was independently verified in D.5 by the endpoint cosieve `{1} -> [1]` and its comma transition `empty -> point`.

### Primary literature

| Source | Exact inspected passage | Use |
|---|---|---|
| Douteau and Waas, *From homotopy links to stratified homotopy theories*, arXiv:2112.02394v2, 29 December 2022 | Theorem 6.1; Example 2.30 | The actual simplicial-link-to-geometric-holink weak equivalence, including generalized flags; the boundary-triangle versus triangle warning |
| Quinn (1988), *Homotopically stratified sets* | Sections 2.1, 2.4, 3.1 | Original homotopy-link terminology and the additional metric, tameness, and fibration hypotheses |
| SGA 4, Exposé IV | Theorem 9.5.4; Exercise 9.5.10 | Ordinary gluing of topoi; comparison with the independently proved enhanced lax pullback |
| Groth (2013), *Derivators, pointed derivators and stable derivators*, inspected arXiv v2 numbering | Proposition 3.6; Lemma 3.7; Corollary 3.8; Theorem 4.16; Example 4.25 | Extension by zero and its exceptional adjoints; stable strong triangulation and recollement |
| Groth, Ponto, and Shulman (2014), *Mayer–Vietoris sequences in stable derivators*, inspected arXiv v2 | Theorems 3.8, 3.16, 6.1 | Homotopy exactness/cofinality for all derivators and stable coherent sequences |
| Maltsiniotis (2005), *Structures d'asphéricité, foncteurs lisses, et fibrations* | Definition 1.1; Theorem 1.2 | Smoothness and its universal base-change formulations, with the proper dual and variance checked |
| Lurie, *Higher Topos Theory* | Corollary 7.3.1.18 and proof | Nonabelian proper base change on locally compact Hausdorff spaces |
| Haine, *From nonabelian basechange to basechange with coefficients*, arXiv:2108.03545v3 | Corollary 3.2; Proposition 3.8; Subexample 3.15 | Extension of the geometric proper-base-change statement to the stated compactly generated or stable presentable coefficient class |
| Kerodon | Theorem 3.6.2.1, Tag 013D | Realization preserves limits on underlying sets; in the finite-poset application compactness and Hausdorffness upgrade the comparison to a homeomorphism |
| Hackney, Ozornova, Riehl, and Rovelli (2024), *Pushouts of Dwyer maps are (infinity,1)-categorical* | Definition 3.4; Proposition 3.6; generalized Theorem 1.5 in Section 4, p.2180 | The missing implication from discrete flatness to homotopical cofibration, with the stated faithful/object-injective hypothesis supplied by being a sieve |

The Douteau–Waas numbering is the inspected preprint numbering. The example is **2.30**, not 2.42. The publication listing subsequently found for Mémoires de la Société Mathématique de France 189 (2026) is not substituted for the numbering of the version actually read.

The generalized-link theorem is a statement in the Douteau/Henriques stratified homotopy theory. It is not used as a theorem identifying all constructible sheaves on arbitrary EI realizations. Any geometric exodromy assertion still has the hypotheses stated in Parts A and B.

## Corrections and distinctions established

1. **Crossing category versus path space.** `E` is the category of crossing arrows and commuting squares. Its opposite nerve is exactly the simplicial mapping space from the stratified 1-simplex into `N(X^op)`. The realized comparison preserves the endpoint data. Unrestricted paths cannot replace this object: two parallel arrows already give two crossing components but infinitely many ordinary path components.

2. **The actual open stratum.** The subcomplex `BA` is generally not open in `BX`. The complementary open stratum is `BX minus BB`. C.2 gives the explicit barycentric strong deformation retraction onto `BA`, compatible with the strata. Statements about literal open restriction use this open complement.

3. **Finite filtrations retain coherence.** At each stage one uses all arrows from the accumulated earlier sieve to the new layer. Generalized links are indexed by complete flags and their ladder categories. Pairwise link homotopy types without their face/composition data do not determine the result. Strict fibre products of link categories are promoted to spatial homotopy products only in the specified groupoidal-layer case.

4. **The enhanced coefficient gluing functor.** The correct lax pullback consists of `FA`, `FB`, and a coherent arrow `FB -> i^*j_*FA`. The functor `i^*j_*` is identified with `t_*s^*` by an explicit adjunction `r:E/b -> A/b` left adjoint to its fully faithful section. The whole span, its endpoint maps, and its natural-transformation data are used; the space `BE` alone is insufficient.

5. **Homotopy categories cannot be substituted before gluing.** C.7 gives a mapping-set counterexample over `[1]`. The coherent arrow category has an integer family of maps between the two specified arrows, while the ordinary arrow category of `Ho Spaces` has one. Enhanced locally constant gluing is a pullback in `Cat_infinity`, followed by `Ho` if desired. For a bare derivator, the pointwise Kan extensions and support/recollement conclusions are retained; an ordinary comma construction is not asserted to reconstruct all coefficients.

6. **Pointed, stable, and strong are separate hypotheses.** D.1 requires Der 1–4 and a zero object. D.2 constructs the particular coherent square by extension by zero on explicitly defined sieve/cosieve subcategories of `X times [1]^2`; no arbitrary incoherent-square lifting is assumed. Coherent fibre/cofiber assertions make sense in the pointed case. Stability supplies exact sequences in the stable sense. Canonical triangulated recollement is asserted only with the additional strongness hypothesis. The abelian short exact sequence in the source is not read as a short exact sequence of spaces.

7. **Proper is outgoing; smooth is incoming.** In the manuscript's presheaf variance, a poset map is proper precisely when every exact outgoing lift poset is weakly contractible; smoothness uses incoming lifts. This gives necessary and sufficient combinatorial tests. Contractibility is not replaced by connectedness or by rational acyclicity. Right base change uses proper vertical maps or smooth base-change maps; left base change has the dual orientation. The converse is tested on fibre squares and the terminal coefficient, which gives an actual map onto a discrete representable.

8. **Finite realizations do not turn the categorical adjectives into their geometric counterparts.** Every continuous map between finite-poset realizations is topologically proper. Endpoint inclusions nevertheless distinguish categorical properness and smoothness. The proper endpoint cosieve also refutes the implication from categorical properness to Quillen-B transport or correct homotopy fibres. The four-object diamond is both proper and smooth but has no opcartesian lift over `0 -> 1` and is not a topological fibre bundle.

9. **Strict cartesian lifts need the full factorization test.** During final review we restricted the greatest/least-exact-lift-poset argument in D.6 and its program to the actual base `[1]`. For longer bases those extrema alone need only give precartesian/preopcartesian lifts. The diamond's stated properties remain valid because there are no further base factorizations to test. The program rejects any base other than `[1]` before applying that shortened strict-lift criterion.

10. **Intrinsic and ambient operations differ.** The finite-poset dictionary transports restriction, its adjoints, and their specified mates. It does not identify arbitrary intrinsic Kan extensions with topological direct image along the map of realizations. The inclusion of vertex `0` into `[1]` sends a two-point coefficient intrinsically to a constant diagram, while ambient direct image is a skyscraper that is not constructible for the minimum-vertex stratification. D.8 gives literal ambient comparisons for closed cosieves and finite product projections, with the coefficient hypotheses required by the inspected proper-base-change sources. An intrinsic left adjoint is not automatically a compact-support operation.

11. **Supplied transcription corrections.** At I ms.54, the target of the fibre inclusion for smoothness must be `y_0\\X`, not `y_0\\Y`. At XII ms.59, downsets being open implies that `x <= y` gives `y in closure{x}`. The reverse formula printed there conflicts both with that open-set convention and with the later upward-closure description in the same paragraph. These are mathematical corrections to the supplied transcription; the original manuscript scan was not inspected.

## Computations and reproducibility

From the `STRATA` directory, run:

```sh
python3 code/CD_checks.py > code/CD_checks_output.txt
python3 code/CD_metadata.py > code/CD_metadata_output.txt
```

The finite-category routine constructs every object, arrow, identity and composition. It checks the typing of all composable pairs, both identity laws, and every associativity triple. For the seven-arrow and eleven-arrow examples it also checks the endofunctors and every naturality equation used by the relative contractions. Crossing categories are generated from their commuting-square definition.

The normalized-nerve and finite-simplicial-complex routines compute boundary matrices, check that successive boundaries compose to zero, and record rational Betti numbers and the nonzero Smith diagonal entries of the integer boundary matrices. The relevant outputs are:

| Example | Nondegenerate chain ranks | Betti numbers |
|---|---:|---:|
| Two parallel arrows | `(2,2)` | `(1,1)` |
| Seven-arrow attachment | `(3,4,2)` | `(1,0,0)` |
| Eleven-arrow attachment | `(4,7,6,2)` | `(1,0,0,0)` |
| Boundary triangle | `(3,3)` | `(1,1)` |
| Filled triangle | `(3,3,1)` | `(1,0,0)` |
| Double cone on the circle | `(5,9,6)` | `(1,0,1)` |
| Four-object diamond | `(4,5,2)` | `(1,0,0)` |

All nonzero reported Smith entries are one. The circle/sphere conclusions also have the explicit geometric descriptions in the proofs; no claim of weak contractibility is deduced merely from homology. For the proper/smooth examples, each nonempty lifting category has a printed initial or terminal object providing its contraction. The endpoint and diamond results `(proper,smooth,fibration,opfibration)` are respectively `(False,True,True,False)`, `(True,False,False,True)`, and `(True,True,True,False)`. The empty-source example gives four true values vacuously. The failed endpoint base-change limit cardinalities are computed as two and one. The downset closures in `[1]` are printed as `{0:[0,1],1:[1]}`. The captured output ends with `ALL CHECKS PASSED`.

The computation supplements the proofs. It does not establish a universal pushout property from finitely many inputs, decide contractibility from vanishing homology, or certify arbitrary proper/smooth maps by sampling.

## Literature search record

Searches used the titles and exact theorem phrases for Douteau–Waas's homotopy-link comparison, Groth's pointed derivator theorem, and Groth–Ponto–Shulman's homotopy-exactness criterion. Initial routine searches had incomplete coverage, so the exact primary papers were opened and their attached TeX was searched directly. Separate searches concerned finite-limit preservation by geometric realization, coefficient versions of nonabelian proper base change, and Lurie's Corollary 7.3.1.18. These led to the inspected Kerodon, HTT, and Haine passages recorded above. A search for `discretely flat` and `Theorem 1.5` led to the published Hackney–Ozornova–Riehl–Rovelli paper; the primary PDF hosted at Rochester was opened after the publisher PDF endpoint returned no readable lines. We checked the generalized statement in Section 4, not only the narrower theorem in the introduction. A search for infinity-categorical collage/gluing descriptions did not supply an additional result that was used; C.6 is proved directly from Kan extensions and the reconstruction pullback. No novelty assertion is based on failure to find a reference.

## Remaining scope and coordination

No additional C/D claim has been relabelled Proved by omitting a required hypothesis. The unqualified path-space replacement, ordinary-homotopy-category lax gluing, and geometric adjective identifications are refuted, with explicit counterexamples. The general diagrammatic and enhanced statements are proved at their stated scope; the geometric coefficient hypotheses are those of Part A and the sources cited in D.8.

We did not use or assert the possible further strengthening that every categorically proper finite-poset map has ambient constructible direct image equal to its intrinsic right Kan extension. The task's intrinsic theorem is proved for all such maps, its unrestricted ambient reading is already refuted, and D.8 explicitly names the geometric classes for which a literal comparison is proved. Likewise the homotopy-link comparison is not substituted for the additional geometric exodromy question for arbitrary EI spaces. These non-used strengthenings are not prerequisites for any C/D conclusion.

Part E uses D.6 only for the strictness separation between proper-and-smooth maps and Grothendieck bifibrations. Part F was advised to use replete full entrance cosieves for strict closed-boundary representatives: an equivalent but non-replete fixed-object inclusion can fail the exact outgoing-lift test. Questions about the forgetful moduli functor are addressed in Part F, not silently assumed in the base-change theorem.

At the parent's request we also reviewed G.4–G.6. We opened Cisinski (2006), Section 9.2.1, pp.364–365, where the truncation localizer generated by `Delta/partial Delta^{n+2}` is explicitly proved proper, and Corollary 9.2.15, p.369, identifying its equivalences with the stated homotopy-group truncation convention. G.4 was patched to cite those passages and Theorem 5.2.15 before using Proposition 6.2.3. Its level-zero component/lift proof was checked. The loop/fibre argument in G.5 and the constant-coefficient Yoneda argument in G.6 were checked without finding an additional hypothesis gap. The shared Cisinski bibliography entry and the parent report record those G references.
