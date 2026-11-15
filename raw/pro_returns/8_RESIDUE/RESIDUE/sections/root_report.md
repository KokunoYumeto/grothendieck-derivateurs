# RESIDUE audit report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No priority is claimed.

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
