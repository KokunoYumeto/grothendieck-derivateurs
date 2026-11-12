# PRETOT: research and verification report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Decisive result and completion criterion

**Part A is false, already for a finite monoid.** The paper constructs the ten-element monoid of monotone self-maps of `[2]` and a 52-element right act `H`. Its element category has 52 objects and 520 arrows. The integral module `Z[H]` is a direct summand of `(ZM)^18`, while the element category is integrally acyclic with nontrivial perfect fundamental group. The supplied matrices certify the direct-summand assertion over the integers. This proves the defining total-homology condition for **every** target category and **every** functor out of the monoid, through the two-sided bar calculation and the checked comprehensive-factorization criterion. No bounded list of actions or target functors stands in for that quantifier.

The prompt's explicit completion criterion is met by deciding Part A with a complete, finite, machine-checked counterexample. The additional parts are developed substantially, with exact distinctions between proved results and residual questions. This report does not represent every auxiliary problem in A–G as solved.

The paper's main numbered statement is labelled `A:counterexample`; the CSV gives its final displayed number and PDF page. Labels remain stable if the source is reflowed. Every numbered theorem, proposition, lemma, construction, definition, corollary, and remark has exactly one row in `PRETOT_results.csv`.

## Construction and universal verification

The starting two-dimensional presentation complex is

\[
\langle a,b\mid a^5b^{-3},\ b^3(ab)^{-2}\rangle.
\]

Its cellular differential is `[[5,-2],[-3,1]]`, of determinant `-1`; thus it is integrally acyclic. The permutations `a=(1 4 3 2 5)` and `b=(1 2 3)` satisfy both relators and generate `A5`. This proves nontrivial fundamental group; no assertion about its exact order is needed. Vanishing first homology makes that group perfect. The classical presentation complex is documented in Hatcher (2002, Example 2.38, p. 142); the construction and arithmetic used here are independently checked.

Coning the two attaching polygons produces a semisimplicial set with 3 vertices, 17 edges, and 15 triangles. The exact words, face maps, free degeneracy completion, multiplication table, and all 520 right-action values are included in `main_counterexample_data.json`. Its simplicial completion has 3, 20, and 52 simplices in degrees 0, 1, and 2.

There are specified weak equivalences from the 52-object monoid element category to the 75-object simplex element category over `Delta_<=2`, and from there to the 35-object nondegenerate face category. The second comparison has an actual section and a natural-transformation contraction. For the first, every object is a retract of a degree-two object, and the resulting outgoing comma categories have explicit natural-transformation contractions. These are weak equivalences and specified homotopies, not categorical equivalences.

The normalized free chain complex splits as

\[
S^0(\mathbb Z)\oplus D^1(\mathbb Z)^2\oplus D^2(\mathbb Z)^{15}.
\]

Dold–Kan transports this projective decomposition to simplicial abelian groups. Each disk is a retract of a free representable; after restriction to the endomorphism monoid, each relevant representable is a retract of its regular act. This gives 18 regular summands. The supplied certificate has `S` of size `180 x 52` and `R` of size `52 x 180`, with 3,360 and 226 nonzero entries respectively. Independent integer readers check `RS=I` and both equivariance identities for every monoid element. The two-sided bar identifies all positive restricted-action homology groups with Tor groups, which vanish by projectivity.

## Conclusions by part

### A: main question and subsidiary tests

The negative theorem simultaneously answers the monoid and finite-arrow versions. For every small poset base, a complete positive classification is proved: total integral-homology presheaves are exactly subterminal presheaves supported on a nonempty directed lower subset. These are total for every fundamental localizer.

The R6 group-base assertion is verified: the act must be free and transitive. The subterminal assertion is verified by explicitly extending every action from the supporting sieve by left Kan extension. For arbitrary total integral-homology presheaves, the induced fundamental-group homomorphism into the base is trivial. The relevant local systems are constructed on the base, so this is not an application of the invalid unrestricted covering argument.

For the specified finite counterexample, **no cyclic-cover enlargement as requested in A.2 exists** for any nontrivial cyclic subgroup. Kan extension preserves total homological asphericity, whereas the requested covering component would have nonzero first homology equal to its cyclic fundamental group. Here the subgroup specifies the fundamental group of the covering, not its deck group.

The R6 semisimplicial action has first homology `Z^28`. Its 52-object, 221-arrow category deformation retracts up to natural transformation onto the vertex–triangle incidence category, whose underlying graph has 18 vertices and 45 edges. It is **not equivalent as a category** to that graph category. The action cannot extend over the degeneracy maps of `Delta`; this is why it does not contradict the main construction.

The full simplicial classification is proved: `K` is total for integral homology precisely when `|K|` is acyclic; it is total for weak homotopy precisely when `|K|` is weakly contractible. For bases with a finite height function strictly increased by nonidentity arrows, the total presheaves for integral homology, weak homotopy, or `W_n` with `n>=2` are precisely representables. Consequently a finite-dimensional semisimplicial set is total precisely when it is one standard semisimplex. For unbounded semisimplicial dimension the paper supplies an exact countable family of finite-presentation bar tests, rather than claiming a further structural classification. The complete polynomial proof that `Delta_inj` itself is total but nonfiltered is included.

### B: all five negative consequences

The five assertions in R5 are refuted by explicit related examples, without relying solely on their abstract equivalence:

| Assertion | Counterexample |
|---|---|
| Total homological presheaf implies total weak-homotopy presheaf | The 52-element act over the ten-element monoid |
| Total weak-homotopy presheaves restrict to nonempty cosieves | Initial-cone extension `F` on `M^initial`, restricted back to `M` |
| One-point couniversal equivalences are dwyérienne | `M -> M union_H {t}`; target has 2 objects and 63 arrows |
| Every weak-homotopy dwyérienne sieve is discretely flat | Attachment by `F`; target has 3 objects and 66 arrows |
| Weak-homotopy dwyérienne sieves compose | Explicit `M_0 -> X -> Y`; `X` has 3 objects/32 arrows, `Y` has 4 objects/138 arrows |

For the discretely flat failure, the proof supplies a simplicial replacement of a specific covariant action. Before pushout it is an objectwise weak equivalence of hom spaces; after pushout the new hom space is the non-equivalence `NE -> *`. For composition, the first sieve is classical Dwyer and its right adjoint is given explicitly; the second has a total weight by transitivity of Kan extension; the composite has the original failing weight.

The intermediate classes are characterized by their crossing weights and restricted actions. Classical Dwyer sieves are strictly contained in total weak-homotopy dwyérienne sieves, which are strictly contained in the intersection of dwyérienne and discretely flat sieves. The latter two classes are incomparable, and each is a proper subclass of homotopical-cofibration sieves. Explicit separators and the forward gluing proof are included. A separate complete audit proves the R2 composition results for strict and total functors, and for total weak-homotopy sieves; none is confused with the refuted strict-sieve assertion.

### C and D: truncations and the repaired operation

Strict `W_n`-dwyérienne sieves fail to compose for every `n>=1`, by the same finite example. For total `W_n` categories with `n>=2`, a nonempty full cosieve inherits total `W_(n-1)` asphericity. The exact remaining obstruction is its `H_n`. The paper proves the stronger positive result for preorders and for categories having a weakly terminal object, hence for categories with finitely many objects. A cone-on-a-sphere attempt at the first missing degree is explicitly rejected by a detecting action with first homology `Z`.

For the modified operation `E_r(i)=R(i square j)`, where `R` is the explicit functorial twice-subdivided-boundary-cell replacement, the largest requested class is all homotopical-cofibration sieves. It is equivalently characterized by the formal nerve-pushout comparison for every cobase change. The source of the endpoint operation is preserved exactly, and its target changes by a specified weak equivalence.

The constructions verify the located forward gluing claims in XII §3 and the cylinder/cofiber requirements in XIII. Classical Dwyer maps suffice for the actual constructed maps; the boundary-cell factors also satisfy the Thomason model-structure requirements. It would be wrong to identify **all** classical Dwyer maps with Thomason cofibrations. Their failure of retract closure is verified using Cisinski's finite example. The particular unnamed later application announced at XII manuscript page 114 was not identified in the supplied continuation, and is expressly not claimed to be checked.

### E and F: paths and diagram shapes

R8 is proved by the exact equality of comma components with morphisms in the groupoid completion. For the point, the category of interval types has the empty type as a terminal object, so it and its integral affinization are filtered and it is total. Its opposite is not filtered. The converse to R8 fails already for `Y=[1]` with initial basepoint, by an all-length final map through the fork to the four-object sphere category.

The endpoint functor is **totally** weak-homotopy aspherical exactly when `Y` is a connected thin groupoid, equivalently a category equivalent to the point. The general **strict** endpoint classification remains separate. It is settled for preorders and groupoids. The length-one walking-retraction example is verified universally and finitely; the full path category is not inferred from its truncation. The identity-test comma category in the full example is explicitly contracted, leaving a precise restricted-action condition.

R9 is false as written for arbitrary small shapes: the empty shape and a discrete two-object shape are immediate counterexamples to its claim of filteredness. The first incorrect inference is the assertion that the singleton set test forces the indexing category to be nonempty and connected. It only contracts each component. The repaired theorem is **componentwise filteredness**. Under the nonempty connected hypothesis, the right-angled Artin group proof works. Its edge-orientation naturality, fundamental-group presentation, and convergent spectral sequence are all checked. For the `W_2` argument, the section of the base row explicitly removes the otherwise dangerous differential from `H_3(BA)`.

Complete diagram classifications are proved for all categories, groupoids, posets with colimits in posets or in categories, abelian groups, and terminal-object-valued diagrams with colimits in all categories. Abelian-group tests alone force filteredness, with nonemptiness and connectedness also necessary. For all-category tests, `W_0` allows every shape, `W_1` is exactly the simply-connected-action-component condition, and `W_n` for `n>=2` and integral homology again force filtered components.

Free monoids are treated with explicit colimit conventions. With colimits in all monoids, filteredness suffices and totality is necessary; for basis-preserving maps totality is also sufficient. Arbitrary word substitutions remain unresolved. A literal colimit in the full subcategory of free monoids is different: the doubling sequence of one-generator free monoids has trivial colimit there but homotopy colimit `K(Z[1/2],1)`. The full subcategory of categories with a terminal object is not cocomplete, so the ambient-category result is not silently relabelled as a theorem in that full subcategory.

### G: passage corrections and the bridge theorem

The paper quotes and treats XII manuscript pages 94–97, 103, 111, 113–114; XIIapp 13–18; the relevant constructions in VII §§4–6 and §10; and II manuscript page 36ter. It distinguishes strict from total functors and sieves throughout.

At XIIapp page 15, the displayed four-object category has type `S^2`, not fundamental group `Z`. Its double-cone attachment has type `S^3`. The original particular obstruction therefore detects `W_infinity` and `W_n` for `n>=3`, but not `W_1` or `W_2`. Both full finite nerves are machine checked. This correction does not remove the separate R4 obstruction for `W_2`.

The bridge-category conjecture at XIIapp pages 17–18 is proved for every small category and full sieve. Mixed nerve simplices have a unique crossing and are joins; their midpoint sections form the two-sided bisimplicial bar. This gives the classifying space as a double mapping cylinder. The specified diagonal map to the bridge category is a weak equivalence compatible with both projections, and the two comparison homotopies are identified relative endpoints. Thus the **canonical** integrated-span comparison, not merely an abstract space of the same homotopy type, is a weak equivalence.

In VII, the actual sequential diagram is indexed by `N` and is filtered; cofinality in the associated preorder does not make the chosen chain homotopy final in the full category. A one-object `C2` base with constant point fibres supplies the counterexample to that general inference. The transition direction printed at manuscript page 102 is reversed and is corrected. The manuscript's later withdrawn loop-space objection is not reused as a counterexample. II page 36ter's literal total-implies-filtered conjecture is refuted by the now self-contained `Delta_inj` proof; the true stronger statement uses every category-valued diagram.

## Exact computations and bounds

All arithmetic used to certify the counterexample is integral. No floating-point rank test or empirical inference from a finite nerve truncation is used.

| Program | Scope and recorded output |
|---|---|
| `main_counterexample.py` | All face/action/functor laws; category compositions; comparison maps; full finite face-nerve homology; nontrivial `A5` quotient; projective splitting; R6 action |
| `audit_certificate.py` | Independent JSON-only reconstruction of the action and all certificate identities |
| `independent_projectivity_check.py` | A second independent integer verification of `RS=I` and both equivariance equations |
| `bounded_search.py` | Exhaustive stated monoid and one-way-category bounds; full fundamental-group presentations and exact abelianizations |
| `quotient_action_tests.py` | Every left-regular quotient act of the ten-element monoid; induced tensor splittings |
| `check_truncated_composition.py` | 2,131 composable pairs and 28,204 associativity triples; sieve and right-adjoint conditions |
| `check_sieve_examples.py` | Dwyer retract example; exact finite sphere/cosieve obstruction and action homology |
| `path_checks.py` | Finite path and final-functor witnesses; walking retraction; 209 bounded type precomposition tests |
| `diagram_tests.py` | The finite cellular disk/square tests, integral Smith forms and torsion checks |
| `semisimplicial_affine_checks.py` | Exact gap-polynomial calculations through source degree three, plus auxiliary recursive cases |
| `appendix_gluing_check.py` | Complete finite `S^2` and `S^3` nerves, category axioms, integral homology, fundamental-group relators |

The monoid census exhausts all labelled monoids of orders one through four with a fixed labelled identity, and all right acts on one through three elements: 170 multiplication tables, 6,145 acts, 4,008 connected element categories, and 3,281 connected zero-first-homology cases. Every latter fundamental-group presentation is reduced to the trivial presentation by reversible Tietze eliminations.

The one-way census exhausts skeletal categories with a chosen increasing object order and at most seven arrows including identities, all set values at most two, and total presheaf cardinality at most four. It covers 173 ordered category presentations and 12,890 presheaves. Isomorphic presentations may repeat. Every connected zero-first-homology case has trivial fundamental group by the same exact elimination. Thus no acyclic, non-simply-connected candidate exists within either bound; this exclusion does not require pretending that a monoid nerve is finite-dimensional.

The old supplied census was inspected but its order-six monoid and arbitrary seven-arrow-category searches were not rerun. Identifying opposite monoids is unsuitable for an unqualified right-act census. Homology only through degree three does not establish full acyclicity when the nerve is unbounded. No global minimality claim for the ten-element example is made.

For the actual monoid, all 115,975 set partitions were examined and 25 left-stable equivalence relations retained. Quotient-size counts are `1:1, 2:1, 3:3, 4:7, 5:3, 6:3, 7:5, 8:1, 10:1`. Every induced tensor splitting passes. Vanishing in every positive degree follows from the already verified universal projective module, not from truncating these action nerves.

The affine semisimplicial audit gives target sizes `[0],[2],[6],[14]`, polynomial degrees `0,1,4,11`, and support sizes `1,3,29,932` for sources `[0]` through `[3]`. The proof for all degrees is the explicit induction in the paper.

## Sources read, literature search, and provenance

The attached prompt, common block, manuscript transcriptions at every requested passage, `RESULT_FILTERED_BY_ONE_TYPES.md`, TOTASPH A/C/E/F/G and the relevant F follow-up, the earlier findings and review files, the census programs and saved outputs, the supplied Hackney–Ozornova–Riehl–Rovelli TeX, Thomason's 1980 PDF, Cisinski's 1999 PDF, and the relevant portions of Cisinski's Astérisque 308 were read or inspected for the claims used. The earlier AI-produced reports were treated as drafts requiring mathematical verification. They are not bibliographic authorities.

The bibliography records opened status entry by entry. Primary texts opened include Weibel's Chapter 8, Stacks Project Theorem 14.24.3, Hatcher Example 2.38, Cegarra (2020), Charney's 2006 preprint, Shoikhet's 2016 preprint, Quillen's Section 1, and the supplied Thomason, Cisinski, and Dwyer-pushout sources. Only relevant sections of the longer books were read. Thomason's 1979 article body and Isbell–Mitchell's original exact-colimit article body were not accessible; neither is marked opened on the strength of metadata. Quillen's original university-hosted scan was eventually opened after other mirrors failed.

Searches included `totally aspherical presheaf monoid`, `totalement aspherique Dold`, `presheaf acyclic projective Dold-Kan`, `dwyerienne composition presheaf`, `homotopy colimits filtered groupoids`, `homotopy colimits preserve truncated`, `sifted aspherical category`, `posets colimit weak equivalence filtered`, `Isbell Mitchell Exact colimits 1973`, `category sieve complement homotopy pushout`, and `collage classifying space homotopy pushout`. The modern test-category use of “totally aspherical” is not substituted for the manuscript's universal Kan-extension definition.

Cegarra supplies the Grothendieck-construction comparison and Charney supplies the Salvetti facts; neither opened source states the corrected filtered-shape classification. Shoikhet treats different path constructions and does not establish the universal claims for the exact type category here. The searches did not locate the finite presheaf counterexample or the exact bridge formulation in a primary source. This is an account of the search, not a claim of novelty, priority, or exhaustive absence.

Independent cross-reviews checked the A certificate, the path classification, the C/D variance and model-structure assertions, the RAAG and abelian-diagram arguments, the gap-polynomial construction, and the bridge comparison. This is exact computational checking and mathematical review, not formal proof-assistant verification.

## Residual questions, precise obstruction, and attempted routes

1. **Total truncated cosieve closure.** For `n>=2`, does total `W_n` asphericity of `A` imply `H_n(BV;Z)=0` for every nonempty full cosieve `V`? The first unresolved degree/cardinality in this investigation is `n=2` with countably infinitely many objects. Action connectivity, finite-object cases, weakly terminal cases, and preorders are proved. Doubling along `V` only moves the missing group to degree `n+1`, beyond the hypothesis. The explicit cone-on-`S^2` candidate fails totality.

2. **Strict endpoint classification for arbitrary categories.** For the full walking retraction with `ru=1` and `ur=e!=1`, the identity-test comma category is contractible and the length-one truncation is strictly total by a universal split-gluing proof. The remaining question is whether every component of every action restricted through the full endpoint-weight projection is acyclic. Passing from the truncation to the full path category has no proved totality-preserving comparison. The total endpoint classification itself is complete.

3. **Free-monoid diagrams with arbitrary substitutions and ambient monoid colimits.** Do their universal weak comparisons force filteredness, or can a nonfiltered total shape pass them? The first concrete unresolved shape is `Delta_inj`. Basis maps pass. The RAAG detector has commutation relations and the poset detector has composition relations, so neither is a free-monoid test; replacing either by a free presentation changes the relevant strict colimit. A classification under literal colimits inside `FreeMon` is also not established; the doubling sequence proves it is not the ambient-monoid classification.

4. **Literal terminal-object subcategory convention.** The complete theorem uses colimits in `Cat`. The full category of categories with a terminal object and arbitrary functors has no initial object, hence not all small colimits. The distinct classification requiring existence and correctness of all colimits in that full subcategory remains unproved.

5. **The special VII full path comparison.** It is proved for groupoids and `[1]`; the exact general canonical comparison remains open. The first specified test is the six-object poset with three ranks of two incomparable objects each, and every lower-rank object below every higher-rank object. Filteredness of a selected sequential diagram alone does not prove comparison with the full category. The manuscript's withdrawn loop-space objection is not a counterexample.

6. **Unlocated intended application.** XII page 114's unspecified later use is not identified beyond the explicit XII §3 and XIII applications proved. A use requiring the literal unreplaced endpoint product would remain obstructed by R4.

7. **Scope of the semisimplicial characterization.** The finite-presentation bar criterion is exact in all dimensions; the sharper representability classification is proved in bounded dimension. No additional simple structural classification in unbounded dimension is asserted.

## Reproduction and document checks

`README.md` gives the execution order and dependencies. All mathematical checkers use package-relative paths, write their outputs under `code/outputs`, and use deterministic exact calculations. The final LaTeX is self-contained, including the APA-style reference list; the separate BibTeX file retains machine-readable fields and verification notes.

The paper is compiled with LuaLaTeX. The supplied build helper can bootstrap the installed source-only TeX environment locally when its generated format and font maps are absent. In that case it uses the installed Type 1 Latin Modern and AMS fonts and a clearly named local kernel variant without the unavailable OpenType-loader startup. It does not change the mathematical source or any system file. Standard complete TeX Live installations use their ordinary LuaLaTeX format. The final build report records errors, missing references, and box checks; rendered pages are visually inspected before delivery.

The delivered PDF has 49 pages. The statement ledger contains 54 rows: 39 marked Proved, 10 Refuted, 4 Open, and 1 Known. The assembler verifies a bijection between numbered statements and rows, their printed numbers and PDF start pages, their statuses, and their dependency labels. An independent CSV import preserves all seven columns and every field exactly. The final LuaLaTeX log has no errors, unresolved references or citations, duplicate labels, overfull boxes, or underfull boxes. Contact sheets of all 49 pages and full-size views of selected mathematical pages were inspected for clipping, missing content, and legibility. The four numbered Open entries do not exhaust the finer residual distinctions listed above.
