# RESIDUE audit report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No priority is claimed.

Register at build: **85 statements** (54 Proved, 7 Known, 13 Open, 11 Refuted); **34 bibliography records**.

## Scope and status

This is a substantive but incomplete answer to the ten-part research request. Each formal result in the paper has a matching register row. `Open` means that this return has not proved or refuted the exact requested statement; it does not assert that the mathematical literature contains no answer. Several broad questions and several specifically requested exhaustive searches remain incomplete. They are retained below and in the paper rather than silently replaced by the smaller completed computations.

The paper is ordered A–J. It distinguishes the literal absolute localizer axioms from the relative package, canonical comparison maps from abstract equivalences, strict categorical pullbacks from homotopy pullbacks, ordinary from infinity-categorical localization, and algebraic curve stacks from coarse moduli spaces. Empty categories, disconnected bases, missing components, and infinite fibres are treated where they enter the results.

## The five leads

| Lead | Disposition | Exact scope and correction |
|---|---|---|
| 1: boundaries characterize intrinsic truncation fibrations | **Proved, D.2** | Requires the stated homotopy-pullback hypothesis. For n≥1, the degree-n boundary is zero; for n=0, the component action is trivial. Empty and disconnected cases are included. |
| 2: equivalence transports cannot model the path family over M | **Proved, A.1–A.3** | Every central-cocycle and orbit step is supplied. The acting object is the simplicial group N(BA), not an ordinary discrete action of A. It does not exclude transports with adjoints that are not categorical equivalences. |
| 3: enough intrinsic fibrations imply every intermediate localization equivalence | **Proved, C.1–C.2** | No functorial factorization, global terminal object, retract closure or strong saturation is added. Cisinski's exact fibration-category approximation theorem is applied with every hypothesis checked. Both ordinary and infinity localizations are covered. |
| 4: proper finite-poset realization computes right Kan extension | **Proved, H.1** | A new barycentric-normalization/proper-base-change argument identifies the canonical mate. The independent numerical checks are recorded in H.7. |
| 5: the marked-point forgetful functor is proper and not smooth in the first nontrivial case | **Proved and extended, H.3–H.6** | The all-genus stack statement is proved for one forgotten mark. The only noncontractible outgoing exit lift is BZ; geometric comparison and base change are stated for actual point fibres and actual closed boundary inclusions. |

## Additional principal results

The absolute Theorem A package does **not** become relative Theorem A after adding retract closure or strong saturation. B.2–B.4 construct a detecting functor on the homotopy category whose inverse-image class is W_infinity together with nonzero-degree maps between circle types. Its aspherical objects remain precisely the weakly contractible types. A degree-two crown covering and its suspension give a finite relative-Theorem-A counterexample. Two independent proof audits and an independent reconstruction of its integral chain cycles found no defect. This is a mathematical conclusion of the included proof, not a priority claim or a statement that a complete contemporary literature search was achieved.

C.3 gives a five-object, sixteen-arrow category with all pullbacks and a strongly saturated weak class satisfying (a) and (b) at every base but failing (c) and the factorization hypothesis. This improves the inherited six-object upper bound outside posets. It does not establish the least possible number of objects. C.4 explains why an object bound alone is not a finite enumeration bound: the one-object cyclic groups give infinitely many inequivalent finite categories with pullbacks. C.5–C.6 directly verify the finite-fence replacement and prove the intermediate perfect-subcategory assertion for every fundamental localizer, including truncation and homology localizers.

D.4 proves that, for every localizer between W_infinity and W_0, the intrinsic maps cannot be the right-lifting class of any class of arrows. The obstruction is failure of closure under a countable product. The proof uses increasingly long finite fences and a uniform zigzag-length obstruction; a finite prefix of the example is not mistaken for its infinite conclusion.

D.5 identifies the derived local-coefficient tests by loop algebras and universal covers. Integral derived coefficients give W_infinity; sets give W_1; groupoids give W_2. D.6 proves that, under the same homotopy-pullback hypothesis as Lead 1, rational local coefficients require only zero boundary π₂B→π₁F. The proposed extra rational vanishing of higher boundaries is false. A completely specified infinite categorical path-fibration model over S³ supplies the counterexample.

D.8 proves that every covering with monodromy through a finite p-group is intrinsic for mod-p homology, including a nontrivial connected regular p-fold covering. D.12 proves the contrasting complete classification for ordinary integral and rational homology: precisely componentwise trivial coverings are intrinsic. Its integral witness attaches a cell with universal-cover differential 2t−1; its rational witness uses a nonzero-degree circle map. These results leave the arbitrary-spectrum classification open.

D.10 reconstructs all eight maps in BISITE B.15, proves all universal entries, and independently checks the finite categories, lifting categories, and fundamental-group presentations. **All 48 scalar entries agree** with the inherited table. D.11 supplies all six requested rows for Loc (7a), (7b), (7c), (7F), and the perfect-to-intrinsic inclusion. The two rational localizers fail (7F); the proof includes their accessibility argument and verifies the local-target hypothesis in Cisinski's obstruction.

F.1–F.4 resolve the named elementary totality candidates. A full subcategory of injective finite ordinals is total exactly when its object set is a singleton or unbounded, and in those cases its integral colimits are exact. Finite sets and injections, and the monoid of injective self-maps of N, are not total. A free category is total exactly when it is filtered. The weakly-terminal case is proved, including nonempty connected finite-object categories. The general countable exact-colimit and universal Cat-colimit converses remain open here.

The Part G interval realization formula is false even for a point represented at zero. This refutes that formula, not the proposed localization equivalence over the line. Cantor-to-point preserves the open-test class but is not a shape submersion. G.5 proves that every product projection, and every map locally of that form on its source, preserves the open-test class; the proof uses rectangular-open homotopy codescent without separation or numerability assumptions. The stable compact-support Verdier theorem is recorded with exact sources, and the pointed-space analogue of that transform is refuted. The larger raw-space recognition problem remains open.

I.1 proves maximality of discrete fibrations among diagonal-closed smooth classes. I.3 supplies the coherent correspondence construction with the span universal property, including its transformation and monoidal parts. A naive specialization of Mann's suitable-decomposition theorem fails its cancellation hypothesis; that failure is explicitly checked and is not presented as a failure of the correspondence formalism itself. The coefficient-dependent universal ambidexterity classifications are proved within this maximal class. J.1 proves relative strict-2-category recognition for ordinary-category bases, using only the established two-dimensional Thomason model structure.

I.9 gives a specified enhanced realization and finite iteration, with exact second-stage formulas. For spectra, both locally constant stages are W_infinity. For D(F_p), the second stage is component bijectivity, integral isomorphisms on pi1 and pi2, and F_p-homology equivalence of the specified 2-connected covers. The proof constructs accessible localizations by a bounded, finite-support witness argument, identifies the constant class exactly by mapping-space tests and Yoneda, and identifies the specified restriction functor through its action monad. It assumes neither finite type nor nilpotence. This chosen localized-space realization does not give functoriality on all bare derivators and all exact morphisms.

## Root computation record

| Program | What it actually checks | Output |
|---|---|---|
| `code/root/finite_categories.py` | Category laws, finite lifting and pullback constructions, connected components, explicit spanning-tree/Tietze presentations | Imported by the D and F verification programs |
| `code/root/verify_D.py` | All eight inherited maps, all their incoming/outgoing lift categories, sphere twist and self-pullback fundamental groups, regular C_p coverings for p=2,3,5,7, finite fence instances | `D_output.json`, `D_stdout.txt`, `tables/D_BISITE_B15.csv` |
| `code/root/verify_F.py` | Complete two-subset action category on FI through cardinality three; its π₁; exact integral polynomial affine cones for n=1,2,3; every corresponding parallel injection; the disconnected two-object scope guard for F.4 | `F_output.json`, `F_stdout.txt` |
| `code/root/verify_coverings.py` | Exact Smith forms for 2P−1 on cycles of lengths 1–12; augmentation-one and determinant identities | `coverings_output.json`, `coverings_stdout.txt` |
| `code/root/assemble.py` | A–J ordering, one register row per statement, permitted status values, citation-key resolution, bibliography consolidation | `assembly_output.json` |
| `code/root/input_manifest_audit.py` | SHA-256 and byte sizes of all 431 background members, plus input archive and prompt provenance | `input_provenance.json` |
| `code/root/build_pdf.py` | LuaLaTeX/BibTeX compilation with a local format/cache fallback when the installed format index is unavailable | `latex_build.log`, `pdf_build.json` |

These are exact finite and symbolic computations where claimed. None establishes an infinite universal preservation property by bounded testing. In particular, the table's intrinsic columns are proved mathematically, not accepted merely because a finite suite of pullbacks passed.

The root polynomial check initially exposed an implementation mistake in hyperplane-coordinate lifting. The code was corrected to use independent coordinates x_i=z_i−z_{i+1}, and all exact restriction and augmentation checks were rerun successfully. The proof contains this coordinate argument explicitly. No failed exploratory output is used as evidence.

The final independent proof audit found a scope omission in the finite-object consequence of F.4. The universal Cat-colimit comparison forces filteredness there only with the nonempty connected hypothesis of Part F(3). A discrete two-object category has the comparison for every diagram but is not filtered. The theorem statement and proof now state the required hypothesis explicitly. The affine-polynomial proof, signed-measure monoid argument, and F.7 spectral-sequence calculation passed the same audit. A separate independent audit of I.9 checked exact accessibility, the specified monad comparison, the second-stage formulas, and finite iteration; no defect was found.

## Document and archive validation

The final LuaLaTeX PDF has 60 pages. Its build exits successfully with no TeX error lines, undefined control sequences, unresolved citations, missing characters, or overfull or underfull boxes. All fonts are embedded. Every page was rendered and visually inspected in contact sheets; critical formulas, tables, references, and the corrected page break were also inspected at page scale. The final-page and font records are retained under `code/root/`.

The supplied minimal TeX runtime lacks the optional OpenType loader `luaotfload-main` and its normal format index. The build script constructs a local format cache and the document uses Type 1 Latin Modern and mathematical fonts. The retained log honestly records the startup font-loader fallback notice. No loader implementation was stubbed and no error line was suppressed. The source also builds with the ordinary LuaLaTeX command on a complete TeX installation.

The final validation program checks the paper/register identity, permitted statuses, bibliography keys, completed numerical counts, the PDF's exact hash against its visual-review record, input provenance, and archive checksums. It does not machine-check the mathematical proofs. The supplied background and transient literature extractions are excluded from the archive; program sources and completed mathematical outputs are included.

## Exact outstanding obligations

| Prompt item | Remaining obligation |
|---|---|
| A(3), A(4), A(5) | The adjoint but non-equivalence transport bifibration over M and the seven-element S³ monoid; decisive fence-completion, reduced-word and bar-resolution constructions; the adjunction/Beck–Chevalley obstruction; general-base existence. A.8 states what each attempt still lacks. |
| A(6) | The complete pseudo-action search on all categories with at most five objects and twelve arrows was **not performed**. The exhaustive monoid enumeration is a different computation. |
| B(5) | Some literal historical assertions are proved or refuted, with an explicit statement-by-statement CSV; the remaining Mayer–Vietoris and other marked entries stay Open. Relative Theorem A does not fix every unrelated typographical qualification. |
| C(3) | The five-object upper bound is proved; no classification excluding every smaller finite category with unbounded arrow count is supplied. No exhaustive all-category search through six objects is claimed. |
| D(3) | The arbitrary-functor rational local-coefficient criterion and the complete mod-p local-coefficient classification, including the sharp-map case, remain Open. |
| D(4) | Complete covering and smooth/proper classifications for arbitrary nonzero spectra remain Open. The integral/rational and finite-p-group results are stated separately. |
| E(1), E(2) | The literal all-word full subcategories of length at most six were not computed. The catalogue computes fixed alternating shapes. The unbounded comparison is proved for the marked three-object chain, not for every four-object relative poset. |
| E general comparison | General J and the literal original all-vertical/ind-stage additive or pointed transfer remain Open; the corrected weak-vertical localized refinements are proved. |
| F(1) | General connected countable totality ⇒ exact integral colimits without a weakly terminal object. The exact gap is equalization of arbitrary affine parallel pairs. |
| F(2) | Total integral-homology-aspherical presheaves ⇒ total weak-homotopy-aspherical presheaves, and composition of the specified dwyérienne sieves. The complete monoid≤6/presheaf≤6 search was not performed. |
| F(3) | The general countable universal Cat-colimit ⇒ filtered converse without a weakly terminal object. |
| G(1)–G(5) | The raw-space/cosheaf equivalence over R and its listed extensions; the dual raw-space realization or impossibility theorem; complete preserving classes and both raw base-change theories. The proposed formula and the proposed shape-submersion equality are refuted, not used to claim these wider statements false. |
| I(2) | The reversible accessible-localizer classification, including the W_Z-to-W_0 interval and the specified non-total case. |
| I(3) | The functorial construction on all bare derivators or its required counterexample, the weakest sufficient enhancement, and iteration in that generality. I.9 proves finite iteration and both second-stage calculations for the specified enhanced localized-space construction. |
| J(1)–J(3) beyond ordinary bases | Recognition over each requested genuine 2-cell base; universal strict-pullback lifting criteria and boundary/comma tests; the lax-comma Der 4 theorem and the complete four-variance table. |

## Reading, sources, and attribution

We read the supplied prompt and manifest, the relevant mathematics and reviews of the seven earlier returns, the relevant manuscript transcriptions and companion blocks, and the primary sources specified in the appended audit logs. Earlier AI papers and reviews were treated as drafts rather than evidence that a claim was true. The background archive is not redistributed in this ZIP; the deliverables contain the new text, programs, outputs, provenance records, and bibliographic references.

For Part D the primary monograph checks include Cisinski (2006), Corollary 4.2.22, Theorem 5.2.15, Propositions 6.1.8 and 6.1.11, Propositions 6.2.3–6.2.4, Section 9.2.1, Corollary 9.2.15, and Lemma 9.4.5. Lurie's *Higher Algebra*, Theorem 4.7.3.5, was opened at the author's source for the monadic loop-algebra comparison. Rivera, Wierstra, and Zeinalian (2021), Theorem 3, was read in the primary arXiv full text. Thomason's original paper was opened, while the corrected model-structure theorem is taken from Cisinski rather than the original false retract assertion about Dwyer maps.

For Part F, the independent proofs are provided in full. Isbell's 1968 publisher PDF was opened, including its affine-combination characterization and monoid theorem. The 1974 *Exact colimits I* publisher record was opened but its full text was not verified. That entry is explicitly marked unverified in the bibliography and no proof depends on its body. Searches included exact-colimit, affine-combination, total-asphericity, injective-ordinal and universal-category-colimit terminology; failure to find a source is not represented as a novelty result.

Every bibliography entry is marked `verified` or `unverified` with the scope of the inspection. A verified entry means that the named primary text or stated part was opened; it does not mean that every theorem in the work was independently reproved. Metadata-only inspection is distinguished from full-text inspection. All specifically requested unattached sources are accounted for in the combined bibliography and appended source registers.

The additional historical corrections, exact passages read, bounded-search exclusions, and full program commands are in the four audit logs appended below. They are part of this report and preserve the difference between an actual counterexample and a missing proof.


---

# Appendix 1: A/E proof and computation audit

# Parts A and E audit log

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.

Read: the attached RESIDUE prompt; PATHS sections B, C_paths, and relevant E; STRATA section E; manuscript conventions. Finalized for integration with the root report.

## Initial verified deductions

Lead 2 has a valid 2-type obstruction. The central-cocycle and Borel argument can also be made precise using a degreewise free action of the simplicial group N(BA), rather than an ordinary discrete A-action. A cleaved opfibration over a one-object category has the same objects as its fibre and can indeed be identified with a twisted category after trivializing its equivalence transports.

The principal strict-bifibration existence problem is not resolved by this obstruction; non-equivalence transports with adjoints fall outside it.

## Completed mathematical results

A.1 proves the higher-boundary obstruction by the categorical autoequivalence 2-group. A.2 verifies every step of Lead 2, including the literal twisted-category isomorphism after choices and the degreewise free simplicial BA-action. A.3 gives the exact lifting criterion for categorical-equivalence transports. A.4 splits the rectangular-band pseudo-action, records the coherence and a four-corner clutching loop, and gives the exact orbit-map criterion for contractible total space. A.5 proves that M is the only non-1-type monoid of order at most five, using a fresh exhaustive enumeration and an elementary proof of the corner-reduction lemma. A.6 reproves the 1-type-base theorem with simplex categories. A.7 excludes finite acyclic fibre categories, where acyclic means no nonidentity endomorphisms or directed cycles, not homologically acyclic.

E.1 gives a uniform closure-operator proof for the [2] example, all alternating lengths, all endpoints. E.2 concludes that the specified J is a weak equivalence for that example and identifies its localization as the walking retraction. The enriched type-poset contraction was checked directly: the first-run contraction fixes endpoints, retains type-map monotonicity, and sends every backward edge to a same-sign string or identity. E.3 contains the complete bounded catalogue of relative posets through four objects. E.4 gives transient S1 homotopy in a finite shape. E.5 proves no single finite all-word cutoff can calculate every four-object case, since the four-point circle with all arrows marked has a loop space with infinitely many components. E.7 constructs the corrected additive refinement for any commutative k and finite-direct-sum-stable W, via finite free modules, algebraic theories, and Day convolution. E.8 constructs the corrected pointed refinement at the localized mapping-space level.

No priority is claimed. The additive argument was found also in a 2023 research discussion (Ramzi's answer to MathOverflow question 445934) in the k=Z case; the technical input used here is Badzioch's primary paper, and the composition construction is written out. The prior PATHS C.9 remains conditional for the literal all-vertical model because its general J is not proved. The literal ind-stage uniformity in C.10 remains unresolved.

## Exact computational scope

1. `monoids.cpp`: complete labeled monoid enumeration for orders 1 through 5 with identity fixed; associativity propagation; quotient by every identity-fixing permutation. Labeled counts: 1, 2, 11, 156, 4122. Isomorphism counts: 1, 2, 7, 35, 228.
2. `monoid_classification.py`: independently rechecks every multiplication table, all associativity equations, canonical labeling, and every idempotent-corner reduction. All 273 types reduce to finite groups except one, the rectangular-band monoid. The terminal reduction counts are 228 trivial, 33 C2, 6 C3, 2 C2 x C2, 2 C4, 1 C5, and 1 M.
3. `path_chain.py`: exact full fixed alternating-shape path posets for [2], W={ids,0->2}, lengths 2,4,6,8,10,12, nine endpoint pairs at each length. Every component has a beat-removal certificate.
4. `chain_closure_check.py`: separately verifies the explicit minimum/maximum and closure-operator formulas for 45 endpoint/length cases and every associativity equation of the walking-retraction category.
5. `relative_posets.py`: exhaustive relative posets through four objects, up to isomorphism, including the empty poset. There are 121 types in all, 120 nonempty. It computes 5313 endpoint rows at fixed alternating lengths 2,4,6. This is not the full subcategory of all word types of length <=6.
6. `verify_certificates.py`: independently checks all 5313 beat-removal certificates; computes integral homology of the six remaining cores by Smith normal forms with integral kernel bases; checks the M cocycle, bar-cycle pairing 1, and the central-extension simplicial action through degree 3.
7. `core_fundamental_groups.py`: constructs exact spanning-tree group presentations for the six non-discrete cores and records each Tietze generator elimination. Four cores give Z; two give the trivial group and are integrally acyclic, hence contractible.
8. `complete_homotopy_table.py`: combines these certificates into `relative_posets_homotopy_table.csv`. Four rows have the homotopy type of S1; every other row has homotopy-discrete nerve. The table gives H0,H1,H2,H3 and pi1.

An exploratory exact-rational calculation on the exceptional chain [3] at lengths 2,4,6,8,10 found Betti vectors in degrees 0..3 of (1,0,0,0), (1,1,0,0), (1,0,0,0), (1,0,0,1), (1,0,0,0). The supporting script and its rerun output are included as `transient_probe.py`; no all-degree assertion at lengths 8 and 10 is inferred from this probe.

## Literature searched and opened

Verified primary full texts: Fiedorowicz (2002), supplied full text and arXiv metadata; Dwyer and Kan (1980), Calculating simplicial localizations, supplied PDF, especially Definition 5.1 and Propositions 2.2 and 5.5; Arakawa and Cnossen (2026), supplied full LaTeX, interval-localization definition and Section 4's Reedy/Grothendieck comparison; Badzioch (2002), primary arXiv PDF, Theorems 1.3 and 6.4; Chacholski and Scherer (2001), institutional PDF, Theorem 26.8, Corollary 26.9 and Theorem 30.5.

The independent online fetch of Arakawa–Cnossen was blocked; verification of its mathematical statements uses the supplied source. Quillen's Higher algebraic K-theory I primary PDF was located at Rochester and EPFL, but both fetches failed in this subtask; its status here is unverified online. The cofinality theorem is independently verified in Chacholski–Scherer. Sweeney's version-2 PDF was located but its fetch failed; none of A.5's exhaustive computation relies on it. Clarke–Scherer–Zeilberger's arXiv record was opened; no homotopical preservation theorem is attributed to that free-bifibration construction. Minichiello–Rivera–Zeinalian's arXiv record was opened; a full PDF at an author URL failed and no theorem from it is used.

Search strings included 'Grothendieck bifibration homotopy equivalences algebraic Kan fibrations free bifibration category weak equivalence', 'category paths arbitrary vertical morphisms localization hammock Grothendieck', 'Fiedorowicz five element monoid classifying space sphere S2', 'Rivera Wierstra Zeinalian 2021 localization necklaces path category', 'arbitrary vertical hammock localization', 'Quillen Higher algebraic K-theory I pdf', and 'localization additive category infinity category enrichment simplicial abelian groups direct sums weak equivalences'. No novelty claim is based on failure to find a source.

## Exact unresolved items

A.3's requested construction or nonexistence theorem for non-equivalence transports over M is not settled. The proposed filtered fence completion lacks a definition with verified endpoint adjoints and fibrewise comparison; reduced-word and bar-resolution candidates have no verified bifibration structure. No claimed verdict on those unspecified completions is substituted for that missing step. The adjunction-unit/counit obstruction and four-square Beck–Chevalley argument are not completed. The seven-element S3 monoid is excluded only for equivalence transports, not all adjoint transports. General-base existence is open. The exhaustive action enumeration on all categories with <=5 objects and <=12 arrows is not performed; the complete base-monoid enumeration must not be confused with it.

E.1's principal J question is settled by a uniform proof and a cofinal alternating computation, but the specific full all-word finite cutoff <=6 was not computed. E.2's complete bounded relative-poset table does not prove the unbounded comparison for all those pairs. No deformation for arbitrary relative categories has been constructed. The additive and pointed refinements are established for the corrected weak-vertical localized hom-spaces; the original full-path transfer remains conditional on J, and the literal ind-stage pointed assertion remains open.

## Exact source-verification record

| Source | Opened and inspected | Precisely used |
|---|---|---|
| Fiedorowicz (2002), *A counterexample to a group completion conjecture of J. C. Moore*, arXiv math/0202260 | Supplied full text; https://arxiv.org/abs/math/0202260 opened | Unnumbered five-element-monoid lemma, printed pp.33–34; own projective-resolution proof and independent enumeration given |
| Dwyer and Kan (1980), *Calculating simplicial localizations*, JPAA 18, 17–35 | Supplied primary PDF, extracted and read; extraction saved as `code/AE/dwyer_kan_read.txt` | Definition5.1 and Propositions2.2,5.5; weak-vertical hammock convention and mapping-space comparison |
| Arakawa and Cnossen (2026), supplied arXiv2608.19870 source | Full supplied `hammock_4.tex` read; independent online fetch unavailable | Interval localization and Section4 Reedy/Grothendieck comparison; no assertion of an independently opened online PDF |
| Badzioch (2002), *Algebraic theories in homotopy theory*, Annals of Mathematics155(3),895–913 | https://arxiv.org/pdf/math/0110101 opened, Theorems1.3 and6.4 read | Rigidification of homotopy product-preserving diagrams; composition is proved separately in E.7 |
| Chachólski and Scherer (2001 preprint), *Homotopy theory of diagrams*, arXiv math/0110316 | https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/ChacholskiSchererMemoirs.pdf opened | Theorem26.8, Corollary26.9 and Theorem30.5: iterated homotopy colimits, Grothendieck nerve, cofinality |
| Quillen (1973), *Higher algebraic K-theory I* | Rochester and EPFL PDFs located; both fetches failed in this subtask | Standard Theorem A is invoked; primary online verification not claimed here; Chachólski–Scherer supplies an independently inspected cofinality theorem |
| Clarke, Scherer, and Zeilberger (2025), arXiv2511.07314 | https://arxiv.org/abs/2511.07314 opened; abstract only | Literature lead for free bifibrations; no preservation theorem used |
| Minichiello, Rivera, and Zeinalian, arXiv2201.03046 | https://arxiv.org/abs/2201.03046 opened; author PDF fetch failed | Literature lead only; no theorem used |
| Sweeney, arXiv2502.05276v2 | Located; PDF fetch failed | Not used for A.5; its enumeration was independently implemented and proved complete |
| Ramzi (2023), answer to MathOverflow445934 | https://mathoverflow.net/questions/445934/when-is-an-infty-categorical-localization-of-an-additive-1-category-enriched/446007 opened | Secondary research lead for k=Z; not the primary technical authority, and no priority claim is made |

The proof of E.2 was re-audited after the initial draft: its first-run contraction fixes both endpoints, acts functorially on transformations, and preserves the requirement on backward arrows. The ordinary type-category and alternating-sequence cofinality arguments are supplied explicitly. E.7 was strengthened to check that the product-preserving reflection of presheaves is monoidal: Day tensor with a representable carries each finite-direct-sum localization generator to another such generator. This supplies the higher composition coherences rather than presuming that objectwise rigidification does so. E.8 only asserts contractibility of choices made through the zero object, not of arbitrary nullhomotopy spaces.

## Parent-requested independent audit of Part F

F.1–F.4 were read adversarially after the A/E work. No substantive error was found. The F.2 integral kernel is generated objectwise by all composites c(a−b), so its finite colimit relation really yields the displayed augmentation-one equalizer after choosing common successors. In F.3 the affine-cone polynomial restrictions agree on adjacent intersections directly and on separated intersections by the exponent-2k induction hypothesis; inclusion–exclusion in the linear difference coordinates preserves integrality and homogeneity. The degree recurrence gives the asserted target. The monoid signed-measure argument in F.4 is valid: invariance forces the finite support to be permuted even for signed coefficients, and mass one forces an orbit length not divisible by any chosen prime divisor of the least period. Suggested explanatory additions were sent to the parent; F.5 remains explicitly Open and is not inferred from F.2.


---

# Appendix 2: B/C proof and historical audit

# RESIDUE Parts B and C: audit log

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No personal attribution or priority claim.

## Confirmed principal result

Lead 3 is true, including infinity-categorical localizations. The missing point is that Cisinski's definition of a category with weak equivalences and fibrations only requires the pullbacks entirely inside the fibrant subcategory; an arbitrary full intermediate subcategory has precisely those pullbacks. Definition 7.4.6, Definition 7.4.12 and Theorem 7.5.18 have been checked in the attached book and at the author's source https://cisinski.app.uni-regensburg.de/CatLR.pdf (accessed 2026-11-11; draft date 2026-07-30, published monograph 2019).

BISITE A.32 and E.12 have been read in full. No error found in the former's general axiom proof or in its finite example; the independent finite checker passes. The six-object example also proves that (a)+(b) do not imply enough intrinsic fibrations.

## Completed mathematical results

The original component-dependent `W†` counterexample is correct, including empty categories and infinitely many components. Its strong saturation is exactly `W0`. This has a short explicit arrow-retract proof; no finite sampling is used to establish the axioms on all categories.

The stronger implication asked in Part B(3) is false. The class `W_circ` consists of weak homotopy equivalences together with nonzero-degree maps between circle homotopy types. It is strongly saturated, hence retract closed. The proof constructs the quotient of the homotopy category by the two-sided ideal of maps factoring through a circle, adjoins formal zero morphisms to handle empty hom-sets, and combines the quotient functor with rational first homology. Its aspherical objects are exactly the contractible homotopy types, so absolute Theorem A holds by Quillen's theorem. The relative axiom fails on the suspension of a double covering of finite crown posets: `C8 → C4` becomes a ten-object-to-six-object map over the three-object span. Its comma comparisons are a degree-two circle map and two maps between contractible cones, while its total map has degree two on `H2(S²; Z)` and is outside `W_circ`. No priority is claimed. The quotient proof is independent of any speculative universal-cover criterion.

The literal Rappel 1 (`W=W°`) and Rappel 1.2 are true. Complete elementary proofs use the cylinder projection and the twisted-arrow category. Proposition 1.3 is true with its ambient category read as `Cat`; the apparent circularity in its backward proof is removed by first applying opposite invariance to `W°`. Rappel 2.3 and the finite-product assertion of Proposition 2.4 do not follow from the printed absolute definition: the product of degree two on the circle with the identity circle gives a torus counterexample for `W_circ`.

Lead 3 is true without functorial factorization, a global terminal object, retract closure, or strong saturation. Every full intermediate subcategory inherits precisely the partial pullback structure required by Cisinski's Definition 7.4.6/7.4.12. Theorem 7.5.18 therefore applies directly inside that subcategory. The result includes ordinary and infinity-categorical localizations, and proves all three fibre axioms (a), (b), and (c).

The six-poset counterexample can be folded into a five-object category with sixteen arrows and all pullbacks. Its slice over `S` is exactly the old six-element lattice; the two distinct atoms of that lattice become two maps from a single object `A`. The specified category has maps `α,β:A→B`, `γ:A→C`, `b:B→S`, `c:C→S`, with `bα=cγ=x` and `bβ=y`, together with an initial object `0`. The weak class consists of identities and `α,β,γ`. The proof and program verify strong saturation, (a), and (b), and disprove (c) and factorization. This gives an upper bound of five for the minimum among all finite categories; it does not establish the minimum.

The needed portion of BISITE B.19 has been independently checked. Prescribed outgoing and incoming endpoint lifts have initial and terminal objects at each finite support stage, with the correct opposite parity choices. Rooted finite fence diagrams contract by repeated leaf deletion, fixing the root. Consequently the full fence replacement is strictly functorial and has a weak coaugmentation. It proves the intermediate-perfect-subcategory comparison for **every** fundamental localizer, including truncation and homology localizers. This does not require perfect maps to be intrinsic for the chosen localizer.

At XII ms.240–241, the stated factorization hypothesis now proves (a), (b), and (c) and both relative pullback identities. Footnote 128's weaker pullbackability assumption suffices. The caution in footnote 130 about all terminal maps being fibrant is unnecessary for these relative statements. The word `cofibrations` in footnote 129 has the wrong variance for the factorization, and two arrows at ms.241 are mistyped; their correct name is `bar p_2`. These are typing corrections derived from the displayed sources and targets, not claims of fresh manuscript-image verification.

## Final historical audit and further counterexamples

Two separate literal corrections survive even after changing the definition to relative Theorem A. In XVI Corollary 2.2, finite-coproduct closure plus filtered-colimit closure implies arbitrary **closure**, not the full two-direction decomposition axiom. The coarse localizer `W_ne` of all maps between nonempty categories and the identity of the empty category is strongly saturated and satisfies relative Theorem A, arbitrary coproduct closure, and filtered-colimit closure; it fails summand restriction. This is Maltsiniotis's Example 1.1.30 in the March 2020 version. B.11 proves every required property directly.

In XVI Lemma 2.5, the stated allowance of an arbitrary arrow class omits an identity hypothesis. On the four-object diamond, `W={a→1,id_1}` is closed under **every** product of its arrows, including nullary products, but localization does not preserve the binary product with `b`. The intended finite localization lemma with identities is proved in B.12. Its arbitrary infinite-product extension with identities remains Open here.

B.16–B.17 supply a second substantive counterexample, `W_nb`. On categories with finitely many connected components it requires an ordinary weak homotopy equivalence; on categories with infinitely many components it requires only a near bijection of component sets, meaning a bijection after deleting finite subsets on both sides. It satisfies every literal moderate-saturation clause, the terminal-object axiom, absolute Theorem A, and finite-coproduct closure. Its aspherical objects remain exactly weakly contractible. The shift of the discrete natural numbers is weak, so component bijectivity fails, yet its localization is nonthin. A fully defined quotient of `Set` by finite-output disagreement, with formal zero morphisms, detects the identity of the natural numbers against a constant endofunctor. This refutes **XVI Proposition 2.7 and XV Proposition 9.9, Lemma 9.10, Proposition 9.12, and Corollary 9.13 as literally stated**. B.17 also proves the corrected versions under relative Theorem A. No retract closure or strong saturation is claimed for `W_nb`.

The formal decomposition equivalences, descent of adjunctions, the intended finite product/coproduct localization lemma, the two adjunctions with discrete sets including infinite sets, and the elementary cube implications of XVI 3.1 are proved. The discrete-set proof does not assume preservation of arbitrary coproducts: a represented functor already inverting the weak arrows keeps its representing hom-sets after localization.

The exact saturation convention was checked at Cisinski 1.4.12 and Maltsiniotis 1.1.1: their FS3 is the split-idempotent clause `ri=1` and `ir∈W` implies `i,r∈W`. It is implied by Grothendieck's stronger moderate clause; it is not closure under arbitrary arrow retracts. Both constructed counterexample classes satisfy the stronger requested literal saturation, so this terminology distinction changes none of the results.

The final register has **25 numbered statements: 13 Proved, 6 Refuted, 4 Known, and 2 Open**. The historical inventory has **36 named rows: 8 Known, 7 Proved, 9 Refuted, and 12 Open**. A mixed row is marked Refuted if one printed clause is false, and Open if its additional conclusion has not been audited; its notes specify the individually settled clauses.

Independent adversarial audits by the other two agents confirmed B.2–B.4 and B.11–B.17. The latter checks included the exact XVI and XV manuscript hypotheses, the finite-output congruence and its inverse-isomorphism criterion, the finite/infinite split in the saturation proof, both discrete-set adjunctions, and the corrected relative-Theorem-A argument.

## Computations

Run `python code/BC/verify_counterexamples.py` from the package directory. The program is self-contained except for SymPy and uses no earlier package code. Its exact output is `code/BC/verification_output.json`.

The successful run reports:

```text
status: PASS
circle degree on H1: 2
suspension degree on H2: 2
fibre counterexample: 5 objects, 16 arrows
pullback cospans checked by universal property: 66
```

For the circle example it checks normalized nerve chain complexes, `d²=0`, integer Smith normal forms of the boundaries, primitive top cycles, and the actual chain maps. It constructs the actual overcomma posets over the three-object span and computes their homology. It also computes fundamental-group presentations from edges, a spanning tree, and triangle relations, recording exact Tietze eliminations. The two crowns give free rank one; the suspensions and cones give trivial groups. The sphere assertions themselves are proved by their explicit cone decomposition, rather than inferred merely from homology.

For `W†`, the program checks all category laws, the projection functor, the comma construction, component labels, isotropy groups, and the finite arrow-retract data. For the five-object fibre counterexample, it checks every composition, every cospan and the uniqueness of its universal pullback mediators, every intrinsic test, all universal-equivalence tests for (b), and the explicit `R,T` weak-natural-transformation certificates for (a).

This is verification of explicit counterexamples. It is **not** an exhaustive search through categories with six objects. The latter family is infinite without an arrow bound, since finite cyclic groups provide infinitely many one-object categories with pullbacks. Every finite category with pullbacks has only monomorphisms, but their automorphism groups still have unbounded order. No claim that a finite search proves a minimum has been made.

The program additionally checks the finite counterexamples to XVI 2.2 and 2.5, including the strict empty pullback of the two point inclusions and the diamond's sixteen binary meets. For `W_nb` it represents functions of the natural numbers by a finite prefix followed by an exact affine tail. Symbolic composition verifies the shift, its near inverse, the finite exceptional sets, and two maps to `{0,1}` becoming equal after precomposition with the shift. This is a certificate about the specified infinite functions, not a claim that a finite sample proves an infinite assertion.

The script `code/BC/update_register.py` regenerates the numbered register from the LaTeX claims and updates the explicit historical statuses. It is metadata maintenance; all mathematical verification is in `verify_counterexamples.py`.

## Literature checked and search record

The attached versions of BISITE A.32, A.10–A.13, E.7–E.12, and B.19 were read. Relevant original transcriptions in XVI and XII ms.215–218, 240–242 were read. The original transcriptions of XVI ms.1–27 and XV §9 were also read in full. The separate `BC_historical_audit.csv` inventories 36 named statements, with precise mixed-clause notes and unresolved entries left `Open`.

Cisinski (2004), *Le localisateur fondamental minimal*, was extracted and its Definition 1.1.3, Remark 1.1.4, and initial closure statements inspected. Its `LF3` is explicitly relative. Cisinski (2006), §§4.2 and 6.1.12–6.1.18, was inspected; 6.1.12 is explicitly the absolute weak-localizer definition. Maltsiniotis's March 2020 book, §1.1, was checked, including Definition 1.1.2 and opposite invariance, which is Proposition 1.1.21 in that version. The attached *Structures d'asphéricité* article was extracted and consulted for its comparison of lifting conditions and fibrations.

The web searches included the exact strings `localisateur fondamental faible`, `localisateurs fondamentaux faibles`, `weak fundamental localizer`, and `weak basic localizer`, together with `example`, `absolute`, `relative`, `Ara`, and `Chiche`. Author and publisher sources were preferred. The particularly relevant historical statements are Maltsiniotis (2012), Remark 1.3, and Cisinski's December 2019 MathOverflow answer to the weak-localizer-example question. Both report no example known to their authors at those dates. This is not presented as proof of absence in all later literature.

Opened primary sources not supplied in the archive:

- Quillen (1973), *Higher algebraic K-theory I*: original scan at `https://people.math.rochester.edu/faculty/doug/otherpapers/Quillen-Higher-I.pdf`, Theorem A at p.93 and twisted-arrow example at p.94; publisher record also checked. **verified**.
- Brown (1973/1974), *Abstract homotopy theory and generalized sheaf cohomology*: author scan `https://pi.math.cornell.edu/~kbrown/scan/1973.0186.pdf`; pages 422–423 visually inspected, including I.1 axioms and factorization lemma. **verified**.
- Kahn–Maltsiniotis (2008), *Structures de dérivabilité*: author preprint `https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/bkgmdef.pdf`; opened, but no theorem from it is used in the proof. **verified** for access, not a claim to have audited its proofs.
- Maltsiniotis (2012), *Carrés exacts homotopiques, et dérivateurs*: author preprint `https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/carhex.pdf`, Remark 1.3 and §1.4. **verified**.
- Cisinski's author-hosted 2019 monograph, currently dated July 30, 2026: Definitions 7.4.6/7.4.12 and Theorem 7.5.18. **verified**.

The editor's *Pursuing Stacks* landing page was opened, but this does not amount to direct verification of §§28–33. That specific requested primary-source check remains incomplete. Search results locating Ara and Chiche's relative localizers were inspected; a complete audit of all their weak-localizer remarks has not been made. These access limits are not hidden behind a blanket `verified` label.

The final near-bijection construction was additionally checked against searches combining the exact weak-localizer terms with `finite`, `connexité`, and `near bijection`; no matching example was located. An initial low-coverage search returned irrelevant results and was repeated with the stronger search service, recovering the primary Maltsiniotis definitions and the dated Cisinski discussion. This is a search record, not a priority or completeness claim.

Cisinski's 2026 author PDF Theorem 4.4.36(ii′), including its explicit restriction to nerves of ordinary categories and its opposite, was checked for the lifting-category criterion used in C.5. Cisinski 2006 Example 4.1.29 and Theorem 6.1.18 were checked for the two-stage localization argument of B.13.

I independently audited the root's D.4, D.6, and D.11. No mathematical defect was found in the countable-product obstruction, the sharp rational boundary criterion, or the fibration-axiom table. I recommended an explicit slice-model realization lemma in D.6 and an explicit accessibility citation for rational local coefficients in D.11. These are requests for proof exposition and source precision, not counterexamples.

## Remaining open work

`B.10` records the uncompleted full statement-by-statement audit of XVI ms.1–27 and XV §9. The inventory CSV explicitly distinguishes 24 settled named assertions from 12 remaining rows. These are XVI's first Corollary 2.8, Lemma 3.2.1, Corollary 3.2.2, Proposition 3.3, Proposition 3.6, Corollary 3.7; and XV Proposition 9.1, Corollary 9.2, Corollary 9.3, the earlier-axiom deduction in Proposition 9.4, Proposition 9.7, and Proposition 9.11. The main formal equivalences in 9.4 are proved; its additional deduction is not silently included. The mathematical questions about literal opposite invariance and strong/retract saturation are settled by the proofs above; the remaining work is the wider source audit, not those implications.

`C.8` records the exact unresolved minimum: exclude or construct a counterexample among finite categories with fewer than five objects, with no bound on arrows. No proof that the five-object example is least has been obtained. A naive finite enumeration by object count cannot provide such a proof.


---

# Appendix 3: G–J proof, source and computation audit

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


---

# Appendix 4: Enhanced second-stage localization audit

# I.9: concrete enhanced second stages

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). This is an independently checked proof of a specified enhanced construction, with no priority claim.

## Result and stage convention

The fragment `I9_agent.tex` proves I.9. Set stage 0 equal to the ordinary constant-coefficient class of the original coefficient category. Stage 1 is its locally constant class. Realize stage 1 by the accessible localization of spaces at exactly that class; stage 2 is the locally constant class of this chosen localized-space coefficient category. This matches the GALOIS E.8/E.10 numbering. It is not an assertion about a unique second coefficient category independent of the chosen realization.

For spectra, stage 1 and stage 2 are both ordinary weak homotopy equivalences. For D(F_p), stage 2 consists exactly of component bijections, integral isomorphisms on pi1 and pi2, and F_p-homology equivalences on the specified 2-connected covers, with no finite-type or nilpotence hypotheses.

## Proof obligations checked

The proof does not infer accessibility merely from two-out-of-three or product stability. It constructs a small generating set for the concrete mod-p first class: every weak simplicial-set map is a sufficiently filtered union of bounded-cardinality weak submaps, obtained by simultaneously adjoining all component/path witnesses, loop-chain lifts of cycles, and source boundaries for target boundaries. Ex-infinity and the based-loop model preserve filtered unions and have finite support in the original complexes. An uncountable regular cardinal controls the countable closure. The same construction with double loops realizes the second class. Strong saturation follows separately from the functor-category characterization and preservation of colimits-to-limits.

Product stability proves finite-product preservation of the reflector. It also proves that mapping spaces between local objects are local, which is used to identify the ordinary constant class with the exact inverted class. Testing constants with source the point supplies the converse by Yoneda.

Evaluation on a connected indexing space is conservative and preserves geometric realizations. The Barr–Beck hypotheses and the action monad are checked explicitly. Necessity for a specified restriction functor uses the adjunction unit on the free object, evaluated at the terminal local space; this is exactly the specified map on localized loop spaces. Sufficiency uses the resulting equivalence of monads. Thus no unspecified Morita equivalence is substituted for a map of loop objects.

The universal cover of the identity component of Omega X is Omega of the 2-connected cover of X. The proof checks this using its homotopy groups and Postnikov fibre sequence. The bar/cobar comparison uses 1-reduced models and a degreewise finite tensor-length filtration. No unproved convergence or finite-type hypothesis is inserted.

The passage between infinity-category restriction and equivalence on the ordinary homotopy categories is also checked: restriction has a Kan-extension adjoint, so its unit and counit detect equivalence in both settings.

## Sources read and verification status

The attached GALOIS E.1, E.7–E.11, G.6, B_accessibility, and definitions in A were read as earlier drafts, not as mathematical authority. They already contain the ring-valued second-stage formula and the localized-space loop-shift construction. Root D.5 and current I.7 were also read to align definitions and scope.

| Primary source | Exact material checked | Status |
|---|---|---|
| Lurie (2017), *Higher Algebra*, https://www.math.ias.edu/~lurie/papers/HA.pdf | Theorem4.7.3.5 at p.685; conservative right adjoint plus preservation of split geometric realizations; surrounding monad comparison discussion | Full primary PDF opened and exact statement read |
| Lurie (2009), *Higher Topos Theory*, https://www.math.ias.edu/~lurie/papers/HTT.pdf | Proposition5.5.4.15 at printed p.482: accessible localization at a small set, with exact equality of strongly generated and inverted classes | Full primary PDF opened and exact statement read |
| Rivera (2022), *Adams’ cobar construction revisited*, https://ems.press/journals/dm/articles/8965824 | Publisher PDF https://ems.press/content/serial-article-files/26673?nt=1; Theorem1 and Proposition7 | Full primary publisher PDF opened and inspected |
| Rivera, Wierstra, and Zeinalian (2022), *The simplicial coalgebra of chains determines homotopy types rationally and one prime at a time*, https://www.diva-portal.org/smash/get/diva2%3A1601126/FULLTEXT01.pdf | Propositions3–4, Definition11, and proof of Theorem41, especially the natural 1-reduced models and comparison of universal-cover loop homology | Full institutional primary text opened and inspected; theorem numbering refers to this manuscript |

Adams (1956), *On the cobar construction*, was located at https://pmc.ncbi.nlm.nih.gov/articles/PMC534237/ but the full-text route returned a browser-verification page. It is not represented as an independently read primary source; Rivera’s fully opened modern proof supplies the comparison used here. Searches for fibrewise Bousfield localization returned additional literature leads; no theorem from those uninspected leads is used.

Search strings included “Bousfield localization spaces preserve fundamental group homology equivalence universal covers fiberwise localization,” “accessible localization spaces locally constant functors stable category loop spaces equivalence,” “Adams 1956 cobar construction simply connected spaces loop space homology primary PDF,” and “Rivera Wierstra Zeinalian 2021 homotopy equivalence fundamental groups chains cobar simply connected.”

## Remaining boundary

The construction chooses localized-space coefficients from specified enhanced first-stage classes. It does not construct an operation on arbitrary bare derivators, prove naturality in all exact morphisms, or identify these localized spaces with a category of higher linear categories. Those parts of I.7 remain Open. No finite computational search is claimed or needed for this theorem.
