# POLES research, proof audit, and verification report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. “Open” means unresolved in this audit unless an item explicitly identifies the published status of an external conjecture. The paper and ledger distinguish a false statement from an invalid proof of a statement that has another proof.

## Source selection and scope

The authoritative request is the attached `PROMPT(4).md`, together with its CATHOT and TOTASPH additions. The unversioned `3_POLES_background.zip` is the fullest attached bundle: it contains 89 entries, including both returns. The `_v1` bundle contains 77 entries and `_v2` contains 80. The unversioned bundle was therefore selected and extracted into an isolated source directory. The user's source files were not modified. The supplied additions bear 11 November 2026 dates; this audit was performed in the environment dated 10 November 2026. The source dates were retained as evidence, rather than silently corrected.

The original transcriptions, the companion's claim tables and commentary, and the earlier AI returns were treated as independent objects of review. The companion is not cited as mathematical authority. In particular, the whole relevant XIIc-b transcription was read through manuscript p. 275, beyond the p. 272 endpoint described in the request. The suspect new statements on pp. 273–274 were checked against the attached edition PDF, so their diagnosis is not based solely on an AI transcription.

The fixed convention is the modern **relative** Theorem A definition of a fundamental localizer. The printed Chapter XVI calls this Loc (3 bis), whereas its literal Loc (3) is the absolute Theorem A. Part A preserves that difference. Strong saturation and full arrow-retract closure are consequences in the modern convention, by Cisinski (2006, Proposition 4.2.4), and are not silently inserted into an argument using only the weaker historical definition. The unresolved implication between those two historical axiom packages is A.16.

The historical **minimum** is nevertheless settled separately: Cisinski (2006, Definition 6.1.12 and Theorem 6.1.18) proves that W_infinity is the least weak fundamental localizer even with only absolute Theorem A. The literal XVI cancellation axiom implies his weak retraction axiom. Hence the historical W_omega also equals W_infinity; A.19 records this verified result. It does not imply that every weak localizer satisfies relative Theorem A.

The mathematical paper follows Parts A–H. Every numbered claim has exactly one row in `POLES_results.csv`, with the requested seven columns. Entries preserve the exact TeX statement text, so qualifiers, quantifiers, and formulas are not lost in a short paraphrase. A claim's dependency column records the explicitly referenced internal claims; its location and notes record manuscript pages, companion rows, or the lead being settled. The source paragraphs following each claim contain the proof, cited external theorem, counterexample, or exact outstanding obligation.

The final integrated ledger contains **104 numbered statements: 75 Proved, 14 Refuted, 13 Known, and 2 Open**. The two Open statements are A.16 and F.14; the latter contains two distinct obligations, so there are three exact unresolved questions. The bibliography has 25 verified entries, and the editorial check found no missing internal claim targets or citation keys. G.26 was closed during the final independent proof review and is counted among the proved statements.

## Disposition of the six leads

| Lead | Disposition in the fixed convention | Exact qualification |
| --- | --- | --- |
| 1 | Proved in B.5. | Reverse excision, its single-square version, Loc (6 C), and detection by a categorical homotopy cofiber are equivalent. Forward gluing and enough Dwyer cofibrations are already available. The cofiber is based at its cone vertex. |
| 2 | Proved in B.6. | Every reversible fundamental localizer contains integral homology equivalences. Empty sources are treated separately, and arbitrarily many components are permitted. Loc (6 a) is not an additional independent hypothesis. |
| 3 | Proved with the connectivity correction in D.1–D.3. | W_Z is the least reversible localizer, and W_infinity fails the reverse axiom. There is **no** class satisfying Loc (5), the weakest perfect-fibration axiom, and reverse excision. The total class is the unique joint solution only after Loc (5) is omitted. |
| 4 | Proved with the definition distinguished in D.4. | The unconstrained stability intersection is total with full Loc (6), and is W_infinity with only Loc (6 a). If containment inside W_infinity is imposed simultaneously, the full reading has no solution. |
| 5 | Proved with the precise dictionary in E.2–E.6. | The strongest and weakest perfect-fibration formulations correspond to left exactness when an accessible reflector exists. Loc (7 F) instead corresponds to nullification/modality and local cartesian reflection; it is strictly weaker. |
| 6 | Refuted as an inverse bijection in F.7. | The Galois connection, exact fixed objects, image description, and fibers are proved in F.1–F.6. Zero and a nonzero stable localizing subcategory can induce the same W_Z. The additional surjectivity claim that every accessible reversible localizer is RT-fixed is retained as an exact open obligation in F.14. |

The upper-interval wording also requires correction: containing W_Z is necessary for reverse excision but is not sufficient. W_0 contains W_Z and fails the cofiber criterion, as B.13 shows. Thus the reversible localizers have a least member without forming an upward-closed interval in the full localizer poset.

## Root proof work and source checks

The categorical cofiber in B.3 is an actual small category, not an unnamed representative in a localization. It has the two layers of the mapping category and a specified cone point; its crossing hom sets and compositions are written explicitly. A commutative square of functors induces a specified functor on these categories. The two sieve pieces have the appropriate adjunction contractions, which identifies the canonical maps with the homotopy-pushout comparison. For an empty source its value is the target disjoint union the cone point; for an empty source and target it is the point.

B.2 proves objectwise invariance of Grothendieck constructions directly from relative Theorem A, with the evaluation/inclusion adjunction typed over each indexing object. Its span proof uses a cover by two categorical mapping layers, inclusions of nerves as simplicial subcomplexes, and specified retractions. The general nerve comparison used elsewhere was additionally checked in Chachólski and Scherer (2001, Theorem 26.8 and Corollary 26.9, preprint p. 63), which identifies Thomason's original homotopy-colimit theorem. No literal equality between a general Grothendieck-construction nerve and a simplicial replacement is asserted.

B.4 uses exactly the alternating interval and endpoint product of XII ms. 228–234. The free endpoint inclusion is a classical Dwyer map. Thomason (1980, Proposition 4.3 and Lemma 5.3(1)) supplies the pushout and composition facts. The false retract assertion in Lemma 5.3(3) is expressly not used. The resulting factorization is enough for intrinsic cofibrations for every modern fundamental localizer, regardless of reverse excision.

The cube proof in B.5 preserves the cone basepoints. The cofibers are first formed in pointed spaces; the forgetful functor creates the pushouts indexed by the contractible span category. For the third cube clause, the map from the wedge to the actual pushout is induced by the **section** from the point to the initial cofiber, not by a map in the opposite direction. The wedge summands are retracts. This supplies the exact transfer omitted by an unqualified “replace the intersection by a point” phrase.

G.26 completes the corresponding **abstract** argument under the original factorization-only hypotheses. The decisive preliminary lemma proves invariance of ordinary pushouts under objectwise weak equivalences when the corresponding first legs are intrinsic cofibrations; the other legs need not be cofibrations. Finite Reedy replacements are then built under a fixed initial vertex, using only pushouts, the intrinsic cofibration/weak-equivalence factorizations, and the relative preservation lemma A.9. A single replacement of the square-times-span diagram gives compatible cofiber comparisons and both iterated colimits. The constant terminal-object row is handled by the one-leg lemma using its identity legs, so the proof does not assume that the terminal object is cofibrant. Common refinements compare the choices by specified weak-equivalence maps. This proof was independently checked, including the latching-colimit maps and the passage to the actual pointed cofibers. The former G.26 residual obligation is therefore discharged; it does not repair the separately refuted Cartesian Cons 2 or the unconditional third cube clause.

The double-cofiber argument in B.6 includes H_0 and empty cases. A homology isomorphism induces a bijection on the actual set of components, including infinite sets. Its cofiber is connected and acyclic; its suspension is simply connected and acyclic. Hurewicz and Whitehead then supply weak contractibility. Two applications of the cofiber criterion give membership in W. D.1 independently verifies the relative Theorem A for integral homology by the first-quadrant homology spectral sequence and proves all three cube clauses by short exact sequences of ordinary nerve-chain complexes. This does not infer the minimality statement from a sample of examples.

For the group alternative, the original Baumslag–Dyer–Heller paper was located and opened, despite the attached manifest's lack of a full local copy. Proposition 4.1, Theorem 4.2, Lemma 5.4 and Theorem 5.5 were checked. B.10 gives the actual mitosis presentation and a field-homology proof, followed by integral universal coefficients. The stronger claim about acyclic **simple** overgroups is unused, so no conclusion is made from that unneeded CATHOT claim. B.12 verifies the amalgam claim by the tree of classifying spaces and its specified quotient to a suspension; it also notes that only the ambient group, rather than the subgroup, must be acyclic.

For the finite acyclic category, Hatcher (2002, Example 2.38) was checked against the supplied complete textbook. The categorical construction and the presentation/permutation proof were redone. The covering argument in H.3 was checked against Theorem 1.38; first homology versus abelianization against Theorem 2A.1; the contractibility arguments against Theorem 4.32 and Corollary 4.33. The proofs only use the stated consequences and do not equate acyclicity with contractibility without the simple-connectivity hypothesis.

The suggestion about simple homotopy was checked against the four-page Lurie (2014) lecture on Whitehead torsion, particularly Definition 2, Example 3 and Definition 17. D.5 distinguishes the geometric expansion/collapse structure from an ordinary localization of all finite complexes and cellular maps. Such an unrestricted localization already identifies homotopic maps and makes every homotopy equivalence invertible, so it does not retain the finer simple type. The finite-poset observation at XVI ms. 95 survives, as D.6 proves without contradicting minimality.

## Checks of the requested TOTASPH inputs

B.9 proves the one-object collage formula in both variances, with the same actual simplex data and a specified realization comparison. The one-point-complement test requires that the complementary object have only its identity endomorphism. Its full reverse hypothesis is retained.

H.2 proves the final-image criterion directly from the presheaf Kan-extension formula. H.3 then proves that total W_infinity-asphericity and total W_Z-asphericity coincide. The argument uses every covariant set-valued category of elements and inherits this property to each of its components. The categorical coverings associated with cyclic subgroups of the fundamental group force those subgroups to vanish. Hurewicz supplies the remaining higher homotopy conclusion. This argument is stronger than simply observing that one acyclic object has trivial homology; it explains why the quantifier over all final images changes the result.

H.4 verifies that above W_1 total asphericity is plain asphericity. It uses the ordinary-final functor's surjection on fundamental groups, the specified groupoid-completion comparisons, and an actual pushout of a bijective-on-objects, surjective-on-arrows groupoid functor. H.5 proves the precise converse threshold: every full sieve is a W-cofibration if and only if W contains W_1. Its necessity is the explicit four-object S^2 category and its collapse to the arrow category.

H.6 verifies the endpoint pushout-product obstruction uniformly for every n >= 2. It computes the **ordinary categorical** pushout by its coend relations and exhibits an actual retraction and natural transformation. The categorical collapse of an S^2-type category to a contractible category is the obstruction; an auxiliary cone variant gives the literal failure to preserve a weak equivalence, with output of type S^3. The uniform proof and the finite computations are separated. The final no-nontrivial-class argument uses both arrow retractions and the modern retract closure of W, rather than pretending that the defining preservation property by itself implies retract closure under only two-out-of-three assumptions.

H.7 concerns the precise **unpointed** HOT_W of the request. Its initial and terminal objects remain the empty category and point after localization, by the descending constant-functor natural transformations. Pointedness forces the empty-to-point functor into W by strong saturation, and then forces totality. Conversely the total localizer gives the terminal derivator. Stable spectral detection of equivalences does not by itself make this unpointed derivator stable.

H.8 strengthens the separation: every **nontotal** reversible localizer preserves connected components and fails even Loc (7 F), without accessibility. If a W-map misses or merges components, its aspherical cofiber has S^0 or S^1 as a homotopy retract, contrary to D.3. Consequently every W-aspherical space has no nontrivial fundamental-group homomorphism to Z, and BF_2 is null for all those spaces. The direct fundamental localizer detected by mapping into BF_2 then contradicts the universal free-group homology equivalence if (7 F) is assumed. This argument does not construct a localization at a proper class and was independently checked. The term “nontotal” is used to avoid confusing a strict subclass of all functors with Cisinski's model-theoretic term “proper localizer.”

## Root computations and their limits

| Program | What was checked | Saved output |
| --- | --- | --- |
| `finite_examples.py` | Complete categories, compositions, identities, associativity, sieve inclusions, Dwyer right-adjoint hom-set bijections, integral Smith invariants, and the nontrivial A5 quotient. | `finite_examples_output.json`, `finite_examples_output.txt`, `finite_category_data.json`. |
| `sieve_pushouts.py` | Actual categorical coend pushouts; independence of composite representatives; functors, retractions and natural transformations; integral chain invariants for n = 2,3. | `sieve_pushouts_output.json`, `.txt`, and `sieve_pushouts_data.json`. |
| `poset_subdivision.py` | All 456 monotone maps from the six-object triangle-boundary face poset to its twelve-object chain poset, with degree zero for every map. | `poset_subdivision_output.json` and `.txt`. |
| `free_by_cyclic.py` | An auxiliary free-by-cyclic group certificate: explicit free-group automorphism and inverse, abelianization matrix, determinant, and nontrivial commutator. | `free_by_cyclic_output.json` and `.txt`. |
| `extract_sources.py` | Text extraction of the supplied Hatcher, minimal-localizer, and Thomason PDFs for theorem verification. | `extract_sources_output.txt`; full copyrighted extracts are omitted from the delivered archive. |
| `assemble_deliverables.py` | One-to-one numbered-claim/CSV correspondence, statuses, all explicit cross-references, citation keys, bibliography deduplication, and verification labels. | `assemble_deliverables_output.txt` and `verification/editorial_checks.json`. |
| `assemble_report.py` | Integration of the root and three section reports, preserving search records and exact unresolved obligations. | `assemble_report_output.txt`. |
| `verify_pdf.py` | All 104 claim headings, embedded fonts, reference markers, page-edge text bounds, and rendering of all 71 pages. | `verify_pdf_output.txt`, `verification/pdf_qa_summary.json`, and the separate visual review record. |
| `build_archive.py` | Packaging the authored deliverables, code, and outputs while omitting full source extracts and temporary rendering files. | Final archive verification records. |

The finite acyclic example has 35 objects and 159 arrows, with normalized nerve-chain ranks (35,124,90), H_0 = Z, and no positive integral homology. Its nontrivial fundamental group is certified independently by two permutations satisfying the presentation relators. The two-cone category has 37 objects and 231 arrows; its contractibility is proved topologically, not inferred from the program's homology output. The genuine Dwyer cylinder and its cofiber have respective sizes (141,1149) and (107,867).

For the endpoint pushout-product, at n = 2 the first pushout has 7 objects and 25 arrows and contracts by an explicit functor and natural transformation; the auxiliary two-cone pushout has 8 objects and 30 arrows and type S^3. At n = 3 the corresponding sizes are (9,35) and (10,40). The all-n statement follows from the coend and retraction proof; no infinite family is claimed to have been exhaustively executed by a finite computation.

The auxiliary free-by-cyclic computation was carried out during the search for a homological fibration counterexample. The paper uses the simpler free-group endomorphism independently checked in Part F instead. The auxiliary program and its output are retained because they were run. An initial JSON-writing error after successful symbolic calculations in the finite-example program was corrected by converting exact integer objects for serialization; the final saved run completed all checks. This was an output-encoding correction, not a change to the example or its mathematical certificate.

## Literature search record

In addition to the searches recorded in the appended section reports, root searches used the exact or combined phrases “Cisinski Le localisateur fondamental minimal theorem 2.2.11 2004”, “Baumslag Dyer Heller topology discrete groups mitotic Proposition 4.1 Theorem 4.2 1980”, “Grothendieck localizer homology mapping cone converse Mayer Vietoris axiom W(7)”, “Grothendieck localisateur W7 homologie cofibre W infinity axiom”, “simple homotopy equivalence Whitehead torsion finite CW complexes Cohen course simple homotopy theory PDF”, and “Thomason Homotopy colimits of small categories 1979 Theorem 1.2 pdf”. Primary author or publisher sources were used for cited technical assertions. The scanned Cohen text was located, but no unverified theorem from it is used. The publisher record verified the metadata for Thomason's 1979 paper; the full proof version actually checked for the nerve comparison is the Chachólski–Scherer preprint cited in the bibliography.

All bibliography entries state what was opened. “Verified” records source inspection and the identified theorem numbers; it does not certify the entire cited work or assert independent proofs of its every foundational result. The manuscript and the supplied companion are not treated as exceptions to the proof audit. Searches are reported to delimit what was checked, not to support a priority claim.

## Exact unresolved obligations

**A.16:** Does the literal historical Loc (1,2,3), with only absolute Theorem A, imply the relative Theorem A? The attempted transfer would require objectwise equivalences of Grothendieck constructions to transfer under that weaker package; its absolute comma test does not establish this step. A first nonterminal relative test base is [1]. No modern result in the paper requires resolving this historical equivalence, because the prompt explicitly fixes the relative convention.

**F.14, first obligation:** For every accessible reversible fundamental localizer W, does membership of D(Bg) in the stable localizing category generated by D(Bu), u in W, imply g in W? This is the exact RT-fixedness assertion. The paper proves it for every displayed stable-detectable example, including W_E and their intersections, but does not infer it from conservative suspension alone. Arbitrary stable generation with desuspensions and infinite constructions is the unproved transfer. Berger–Ratković's stable embedding result requires fully faithful suspension and therefore does not fill this gap.

**F.14, second obligation:** In all spectra, is loc(HF_p) the kernel of smash with some spectrum? Equivalently, does it equal the specific minimal homological kernel defined by a(HF_p)? The full paper distinguishes this exact verification question from the known existence of a set-generated localization functor. The published example of a non-Bousfield localizing category that was verified lives in the HF_p-local ambient category, so it was not imported into all spectra. The 2026 paper checked in the follow-up concerns a different retract conjecture. No claim that the concrete question is newly open is made.

These are the remaining proof obligations, not silently accepted results. The six-lead bijection is already decisively false by the separate noninjectivity example, irrespective of either F.14 obligation. Parts C and E use the explicitly permitted lower-and-upper-bounds alternative for homological intrinsic fibrations; they do not claim a simpler exhaustive equality description.

## Build, package, and visual verification

On a standard complete TeX Live installation, build from the `POLES` directory with `python code/build_lualatex.py --system-tex`, or run LuaLaTeX, BibTeX, and LuaLaTeX twice on `POLES_paper`. The accompanying build script records the complete transcript and a machine-readable warning summary. The workspace-specific repair path and the exact public TeX dependencies are documented in the Part F report below; they are unnecessary on a complete installation.

The final editorial counts, compilation results, PDF dimensions, font checks, page-render checks, and archive integrity results are recorded in `verification/` and `code/`. These checks validate typesetting and internal consistency; they do not replace mathematical proofs. The paper, bibliography, ledger, and all program outputs are included together in the single archive. Full supplied papers and intermediate full-text extracts are not redistributed.

The final PDF has **71 A4 pages** and **638,865 bytes**. LuaLaTeX, BibTeX, and two subsequent LuaLaTeX passes completed with no unresolved references or citations, missing characters, box warnings, or backend warnings. All 71 pages were rendered and visually inspected; the detailed review is `verification/visual_review.md`. Every claim heading is present, all fonts are embedded, and the page-edge text checks passed. The archive builder verifies required files, path safety, member CRCs, and the SHA-256 digests of every payload file; its manifest omits only its own digest to avoid self-reference.

## Detailed section reports

The following reports retain the direct-source audit, exact theorem references, computations, correction lists, and search limits of the parallel section reviews. They supplement the integrated conclusions above.

## Parts A and G: source, proof, and computation report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. Statements labelled Open are exact obligations left unresolved in this audit, not assertions that the questions are newly open in the literature.

### Scope and source handling

The authoritative task is `upload/PROMPT(4).md`, including the CATHOT and TOTASPH additions. Parts A and G use the original transcriptions in `sources/grothendieck/DER_XIIb-a`, `DER_XIIb-b`, `DER_XIIc-a`, `DER_XIIc-b`, `DER_XIIapp`, and `DER_XVI`, with the relevant earlier XII and VI definitions consulted for variance and the abstract relative-category conventions. The companion claim tables, commentary and overview files were used as an index of assertions to check, not as proof. The relevant CATHOT and TOTASPH claims were compared with the independent proofs and computations in the other parts of this paper.

The entire relevant end of XIIc-b was inspected through manuscript p. 275. This matters because the request's main endpoint is p. 272, but the following pages contain the abstract theorem, the literal Cartesian `Cons 2`, and its corollaries. The suspect word on p. 273 and the missing conservativity premise in part 3° on p. 274 were checked against the attached edition PDF, not only the AI transcription. Both are in that edition. They are therefore described as printed mathematical errors, without attributing their origin to the original handwritten manuscript or to the modern editors.

The source inventory program records explicit occurrences of reverse-excision labels and related words. Its 119 lexical hits are a navigation aid. Exhaustiveness of the mathematical register is based on the page-by-page examination and the proofs in G.1–G.25, not on the proposition that a keyword search finds every implicit dependency. G.26 supplies a separate complete proof at the original abstract factorization-only level, rather than presenting the modern Cat result as a proof for an arbitrary relative category.

The A/G contribution has 45 numbered statements: A.1–A.19 and G.1–G.26, comprising 24 Proved, 10 Refuted, 10 Known, and one Open. `AG_results.json` preserves their complete statement text, including quantifiers and qualifications. The final assembly converts this intermediate ledger into the requested integrated CSV. The local bibliography was supplied as `AG_references.bib`; the assembly deduplicates its Cisinski entry to the canonical key `RootCisinski2006`.

### The historical convention and the separately settled minimum

The prompt explicitly requests relative Theorem A. The literal Chapter XVI calls the absolute comma-category test Loc (3), and the relative statement Loc (3 bis). A.1 preserves that distinction. Cisinski's modern Definition 3.3.2 and Proposition 4.2.4 apply to the relative convention; the latter supplies strong saturation and arrow-retract closure. They are not silently applied to every historical weak localizer.

There is, however, a separate theorem which resolves the historical minimum itself. Cisinski (2006, §1.4.12) defines weak saturation by identities, two out of three and the split-retract cancellation rule `ri=id`, `ir∈W` implies `i∈W`. His §6.1.12, pp. 240–241, defines a **weak fundamental localizer** using that rule, terminal categories, and absolute Theorem A. Literal XVI Loc (1)(c), which tests both composites `gf` and `fg`, implies his split-retract rule. Cisinski's Theorem 6.1.18, pp. 242–243, then proves that W_infinity is the minimum among weak fundamental localizers. It follows that the literal historical W_omega is also W_infinity. A.19 supplies this precise comparison, without accessibility and without claiming that every weak fundamental localizer is modern.

The proof of the external theorem was read through its five steps. It obtains asphericity of horn attachments and their transfinite composites, proves all weakly contractible spaces aspherical, and uses Proposition 6.1.16 with the proper Thomason model and Brown's lemma to pass from aspherical objects to all ordinary weak equivalences. Its target W is only a weak fundamental localizer. This is why the historical minimum can be settled even while the general absolute-to-relative implication remains unproved here.

### Part A: exact axioms and proof repairs

A.2–A.7 give the literal data for XII W(7), W(7 bis), XVI Loc (6a,b,c), (6′a,b), (6A), (6A′), (6B), (6C), (4), (5), (7a,b,c), reference (7D_V), (7F), (8), (8 bis), and (9). They distinguish strict base change, ordinary Grothendieck fibrations, weak fibrations and perfect maps. A Grothendieck fibration is not assumed to be an intrinsic W-fibration. The labels are not silently transported between chapters: XII W(7) includes the third cube clause, whereas XVI explicitly omits it from Loc (6) after footnote 13. The opposite-category sieve/cosieve translation is also separated from passing to a dual derivator.

A.8 gives a complete typed proof of the Brown lemma used at XVI 3.2.1. The argument first proves the elementary functor lemma, applies it in the relative category under a fixed object, and then treats the retraction of a trivial cofibration by an explicit pushout diagram. Every comparison map and its direction is supplied. It does not assume that Dwyer maps are closed under retracts, or that the localizer is strongly saturated. Brown's original scanned paper was opened at §4, Lemmas 1–2, pp. 428–429. The proof is used in its dual cofibration form.

A.9 proves the couniversal-equivalence and relative cobase-change statements from enough intrinsic cofibrations. Its dual gives the corresponding universal-equivalence theorem for enough intrinsic fibrations. A.10 gives the exact two degenerate cubes proving the easy implications. A.11–A.12 verify the remaining modern cofibration implications, with the Dwyer cylinder and the precise comparisons supplied by Part B. This repairs footnote 136 without presupposing the desired reverse cube theorem.

In the third cube-clause argument, the four homotopy cofibers retain their cone points. The map from the homotopy wedge to the original pushout uses the specified **section** `e→Z_0`; it cannot be obtained by keeping both outside vertices fixed and merely reversing the asphericity map `Z_0→e`. The section is a W-map by two out of three. The wedge summands are retracts after localization. This corrects a potential direction error and makes the object-retract premise explicit.

A.13–A.15 separate the formal fibration arrows from the extra hypotheses printed in the source. Composition closure and functorial replacement over the base are stated where they are used. The printed summary 4.4.13 uses (7F) for the reference localizer where its earlier argument 4.4.6 had used Loc (7); those are not reported as the same proof. A.17 verifies all eight formulations in the modern convention by the stronger result of E.4–E.5, without accessibility. A.18 gives the accompanying coproduct implications, including empty summands and arbitrary small families.

The source heading after 4.4.15 is literally **4.16**, not 4.4.16. That printed label is retained. The first wording of (7F) uses “cofibrations” where the definition and all following formulas require fibrations; A.6 explicitly identifies this variance error. The finite coproduct and accessibility claims are also kept distinct: Loc (8) means all filtered colimits, and the source's countable-cardinality convention is not modern finite accessibility.

### Part G: consequences and corrections

The exact locations and dispositions are collected in G.25. The following table records the substantive corrections and their proof mechanisms.

| Locations | Finding and proof |
| --- | --- |
| XII ms. 75–80 | The formal implication W(7)⇒W(7 bis) is correct. Theorem 2, asserting W_infinity satisfies full W(7), is false. The checked finite acyclic category A and its two cones refute both reverse edge cancellation and the reverse cube clauses. |
| XII ms. 76–77 and companion XIIba-A-053 | The object statement “intersection and union aspherical imply both pieces aspherical” is true for every modern W, using a specified point in the intersection, forward gluing and strong saturation. It does not imply the failed map-level Loc (6c). The empty-intersection case is included. |
| XII ms. 81–85, 108–109, 227–228 | Reverse cancellation fails even along a genuine classical Dwyer map. The actual alternating-interval cylinder in B.4–B.8 gives that stronger counterexample. The one-point-complement converse is false without its full reverse premise, and valid with that premise. |
| XII ms. 97–100 | The total-asphericity gluing proof has a separate failure, which persists for nonzero homology localizers satisfying full W(7). A four-object, ten-arrow category of type S² has a contractible ordinary-final fork. The claimed preservation of monomorphisms by the relevant left Kan operation is also false. |
| XII ms. 104–107; appendix ms. 15–16 | The suspension construction used to disprove cofibrancy survives by a different proof when its input is simply connected. In the appendix, the punctured category V′_0 is S², not S¹, and its double cone is S³. The later attachment uses a **trivial closed Dwyer** inclusion; forward pushout and two out of three repair the claimed equivalence transfer. There is no need for general reverse cancellation there. |
| XII ms. 125–135 | The integral models, forward cube statements, and closed-cover comparisons survive for every modern W. Their reverse clauses require the full reverse hypothesis and fail for W_infinity. Footnote 85 correctly removes reverse hypotheses from the forward implications. |
| XII ms. 146–157 | The reverse smoothness implication is false for W_infinity without full W(7 bis). A complete 110-object, 1051-arrow smooth integral is smooth although its middle structural functor is not. All exceptional lifting categories are explicitly computed. The forward theorem and the conditional reverse theorem are retained. |
| XII ms. 168–169 | For presheaves, the formula `N(X/F)_n = disjoint_union_(x_0→…→x_n) F(x_n)` proves that the element-category nerve preserves the pushout and its monomorphism leg. Thus the homotopy-pushout conclusion and forward implications survive. The converses fail on the simplex categories of the two cones of NA. |
| XII ms. 111, companion XIIba-C037–038 | A sieve cofibration with one-point complement need not have the proposed total-aspherical boundary weight, even for homology localizers. The two-parallel-arrow category gives the counterexample. A universal proof covers every small change of complementary category, rather than a finite sample. This does not settle the separate narrower question about **trivial** cofibrations by the same example. |
| XII ms. 114–115, 228–234 | The actual cylinder uses the product of the endpoint inclusion with the source, followed by pushout. It remains valid. The desired endpoint pushout-product stability is a different claim and fails, as H.6 proves uniformly for n≥2. |
| XII ms. 234–239 | Proposition 17 and pasting Proposition 18 are true. The latter cancels homotopy-pushout **squares**, rather than reflecting weak equivalences across a pushout. Only the forward direction of the source's auxiliary biconditional is needed. |
| XII ms. 240–261 | The fibre and homotopy-Cartesian formalism uses enough fibrations and the stated terminal-map premise, not reverse cofibration excision. In Cat, terminal maps are intrinsic fibrations by product stability. Footnote 130 correctly identifies the additional abstract premise. |
| XII ms. 262–264 | Proposition 20 is true in the modern convention by specified cofibration replacement and integral comparisons. The displayed comparison labelled lambda points opposite to the functor induced by the displayed replacement; reversing that arrow repairs the typing. |
| XII ms. 265–267 | The introductory citation reverses what Proposition 6 actually proved at p. 78. Footnote 136 identifies a real missing comparison, now supplied by Brown gluing and the functorial Dwyer construction. The cone criterion itself still uses reverse excision. |
| XII ms. 268–272 | The square-of-cofibres lemma is true in modern Cat by interchange of pointed homotopy colimits. The claim that the whole reduction has used only the forward half is false: it already invoked equivalence detection by cofibres at p. 267 and again in the deployment argument. |
| XII ms. 273 | Literal Cartesian Cons 2 is false even for W_Z. The empty pullback of the two distinct endpoint objects of [1] has the other three vertices contractible and its initial legs are intrinsic cofibrations. Replacing Cartesian by cocartesian gives the intended implication under conservativity. The word is present in the edition PDF. |
| XII ms. 274 | Theorem 3° and the asserted equivalence in Corollary 1 are false as printed. A strict finite cube has f_0 and f_3 weak equivalences but f_1 not, while satisfying enough cofibrations, the terminal-object premise and retract closure. The edition PDF confirms that the missing conservativity premise is not merely lost in the transcription. |
| XII ms. 272–275 | The corrected theorem and Corollary 2 are proved both in modern Cat and at the original arbitrary-relative-category factorization level in G.26. Conservativity and the literal object-retract hypothesis are retained where needed; the terminal object need not be cofibrant or fibrant. |
| XII appendix ms. 17–18 | The open/closed gluing conjecture is proved by an explicit Grothendieck construction P and a contraction of every P/x. All five types of arrows and both natural transformations are typed. The extra reverse tests proposed there are false for W_infinity. Empty U, V and crossing-arrow categories are included. |
| XVI §§3–4, ms. 16′–70 | The conditional reverse implication diagram is correct in the modern convention. Brown's missing proof and the forward cofibration premises are supplied. The fibration argument has no reverse-cofibration dependency. The W_0 counterexample in the source is correct and separates (7F) from both the reverse axiom and the perfect-fibration axiom. |
| XVI §5, ms. 71–83 | The full list in Theorem 5.4 is false because it includes Loc (6b). The accessibility conclusion and the other listed axioms survive. A countable finite-witness extension argument gives the source's countable-subcategory property without reverse excision; the modern model theorem independently gives accessibility. The unfinished general hypothesis in Lemma 5.5(b) is not filled in silently. |
| XVI §6, ms. 83–97 | The fibration theorem and its lemma/corollary use no reverse cofibration axiom. The full proposed stability intersection is total; imposing containment inside W_infinity simultaneously leaves no solution. With forward Loc (6a) only, its minimum is W_infinity. The separate literal historical minimum is also W_infinity by A.19. |
| XVI §7, ms. 98–123, especially 119–120 | The remark that Loc (6b) is unused in obtaining HOT_W as a derivator is correct for every accessible modern W. Cisinski's Theorem 5.2.15 supplies the actual combinatorial model on Cat, and Groth's Proposition 1.36 supplies its strong derivator. Neither enough intrinsic fibrations nor the fibration axiom is required. |

The standing finite counterexample is accompanied throughout by the one-object acyclic-group alternative verified in Part B. Its use does not depend on finiteness and introduces no nonidentity idempotents. The categorical descriptions of the relevant cone and comma categories are literal, not merely homotopy-type comparisons.

### The abstract finite calculus in G.26

The concern in XII footnote 138 can be resolved for the precise finite operations used in the theorem. No global initial object of M is needed. The proof works under a fixed object T, the value at the least vertex of the actual finite diagram; the undercategory has an initial object and pushouts, and therefore finite colimits. Its forgetful functor creates the connected colimits used for the spans and product diagrams. No conclusion about arbitrary absolute finite homotopy colimits in M is made.

The elementary gluing lemma is stronger than the usual two-cofibration-leg form: for an objectwise W-map of spans, one pair of corresponding cofibration legs suffices. Its proof changes the initial vertex along its W-map, then applies A.9 to the comparison of cofibrant objects under the new base. This explicitly handles the other leg to a terminal object without any cofibrancy assumption on that object.

Finite Reedy replacement factors each actual latching map `L_jQ→D_j`. A common refinement of two replacements is built from their pointwise coproduct under T, using the relative latching map `P_j ⊔_(L_jP) L_jR→D_j`. All comparison maps to the given diagram are objectwise in W; two out of three and finite gluing make their colimit comparisons W. A separate root-rectification formula `Q_i*=Q_i ⊔_(Q_0) D_0` proves that a row whose initial object changed still computes the original span's homotopy pushout.

Fixed rows are not incorrectly called downward closed in the product. The proof identifies their latching colimits with colimits over the corresponding downward closures, using the terminal coordinate to give an actual ordinary-colimit isomorphism. Inclusion of a downward-closed subposet adds the original latching cofibrations one at a time. This proves both row/column cofibrancy and cofibrancy of the partial-colimit diagrams. Ordinary Fubini then becomes a comparison of valid compatible homotopy-pushout models, with no pushout-product axiom.

For the square-of-cofibres lemma the full diagram is `I×J`, where I is the four-vertex square and J is the three-vertex span. Its columns are X, Y and the constant terminal object. The terminal column's initial-span pushout maps to e by a W-map because its comparison to the constant identity-leg span satisfies the one-leg gluing lemma. This proves the terminal comparison explicitly instead of assuming that T→e is cofibrant. The row cofibers of the Reedy replacement are then compared to the **actual** cofibers `Y_i ⊔_(X_i) e`, by the same one-leg lemma. For arbitrary vertical maps, the entire cube is first replaced on `I×[1]` so that its vertical maps are cofibrations; membership in W transfers by the actual natural comparison maps and two out of three.

Finally, the original abstract retract premise is used at its stated strength. After replacing the initial legs of an aspherical-intersection/union square, push out along `Z_0→e`. The resulting wedge has its two branches as actual retracts in M, obtained by terminal collapse of the other branch. The proof does not infer closure under retracts in the localization from the weaker printed hypothesis. This completes theorem parts 1°–2° and Corollary 2 with the corrected cocartesian Cons 2, while leaving the independently refuted unconditional part 3° and Corollary 1 false. The full finite argument was independently checked before G.26 was changed from a provisional Open entry to Proved.

### Computations and reproducibility

All finite categories are given by complete object, arrow and composition data. The scripts check source and target compatibility, identities, all composable pairs and triples, and the asserted functors. Homology is computed from normalized nerve chains with exact integer matrices and Smith invariants. Weak contractibility is never inferred from the computed vanishing of homology alone; the required simple connectivity or explicit contraction is proved in the paper.

| Program | Data and checks | Saved outputs |
| --- | --- | --- |
| `ag_source_inventory.py` | Explicit reverse-excision markers in the supplied XII/XVI transcriptions, with source line and current manuscript page. | `ag_source_inventory.out`; `verification/ag_source_inventory.json`. |
| `ag_audit_examples.py` | Four-object S² category, ordinary-final fork and comma categories; six-object S³ double cone; 110-object reverse-smoothness integral and all three exceptional lifting categories. | `ag_audit_examples.out`, `ag_audit_examples_data.json`. |
| `ag_small_checks.py` | Literal Cartesian Cons 2 counterexample; every inclusion, sieve cover and commuting face in the strict G.17 cube; the two-parallel-arrow boundary example. | `ag_small_checks.out`, `ag_small_checks_data.json`. |
| `ag_appendix_square.py` | The original appendix attachment for n=m=2, the closed Dwyer adjoint, the full categorical pushout, and its homology. | `ag_appendix_square.out`, `ag_appendix_square_data.json`. |
| `ag_extract_references.py` | Reproduces primary PDF extraction and the Brown p. 428 / XII pp. 273–274 page images used for source checks. | `ag_extract_references.out`; intermediate copyrighted extracts and images are excluded from the final package. |
| `ag_finalize.py` | Complete A/G statement extraction, statuses, dependencies, locations, sequential numbering and display/proof delimiter checks. | `ag_finalize.out`, `research/AG_results.json`. |

The four-object counterexample has normalized chain ranks (4,6,4), with H_0=Z and H_2=Z. Its fork has three objects and five arrows and is contractible. The double cone has six objects, twenty arrows, chain ranks (6,14,16,8), and H_3=Z as its only positive homology. The reverse-smoothness integral has 110 objects and 1051 arrows; its central lifting category has 107 objects and 867 arrows and is the verified integral model of the acyclic suspension. The two outer lifting categories each have 36 objects and 195 arrows.

For the original appendix square with n=m=2, X=Phi_2×Phi_2 has 25 objects and 81 arrows. The pushed-out category X′ has 27 objects and 94 arrows, with normalized chain ranks (27,67,48,8) and H_3=Z as its only positive homology. The closed-Dwyer left adjoint is computed on the generated sieve {0,1,2}² by the coordinate rule 0↦0, 1↦1, 2↦1. The symbolic proof explains why the result is S³; the finite program checks the category and integer chain invariants independently.

All final saved runs completed successfully. The first version of the ledger checker counted the TeX row-spacing sequence `\\[3pt]` as a display opener; its delimiter regular expression was corrected to ignore a preceding backslash. This was an editorial checker issue, not a missing mathematical display or a change to the proof. The full LuaLaTeX build separately caught one genuinely missing display terminator in A.13; it was repaired. The typesetting pass also braced the literal TikZ cell `[1]`, split a long equivalence display, allowed breaks in the eight-condition list, and made the audit-register columns ragged right. These changes do not alter mathematical statements.

### Verified literature and search record

The mathematical citations used for this contribution are primary sources. Cisinski's complete Astérisque PDF was opened at Definition 3.3.2, Proposition 4.2.4, Theorem 5.2.15, §1.4.12, §6.1.12, Propositions 6.1.15–6.1.16 and Theorem 6.1.18. The small 1999 Dwyer paper and its NUMDAM bibliographic record were opened; the paper is used only for the failure of retract closure of the **classical Dwyer class**, not for failure of retract closure of intrinsic cofibrations. Brown's scan was inspected visually at its relevant lemmas. Groth's supplied TeX and arXiv v2 PDF were opened at Theorem 1.34, Lemmas 1.35–1.37 and Proposition 1.36. The latter directly proves the combinatorial-model derivator statement; no broader theorem is needed.

The following queries or close combined forms were issued during this work:

1. “Brown abstract homotopy theory 1973 gluing lemma category cofibrant objects cofibrations lemma 1.1”.
2. “Brown lemma cofibration category all objects cofibrant gluing lemma proof”.
3. “site.numdam.org Cisinski Le localisateur fondamental minimal 2004 2.2.11”.
4. “site.numdam.org La classe des morphismes de Dwyer”.
5. “site.math.cornell.edu Abstract homotopy theory and generalized sheaf cohomology”.
6. “Moritz Groth Derivators pointed derivators stable derivators 2013 1411 1494 1.36”. The initial page guess in this search was wrong; the primary record gives **313–374**, which is the bibliography's value.
7. “category sieve cosieve complementary homotopy pushout arrow category nerve gluing”.
8. “Grothendieck Les Derivateurs chapitre XII 273 carrés cocartésiens conservatifs”.
9. “Cisinski fundamental localizer Brown lemma homotopically cocartesian 5.1.3”.

The last search surfaced a secondary mention of the weak-localizer theorem. That mention was used only to locate Cisinski's primary §6.1.12 and Theorem 6.1.18, which were then read directly. No result is accepted on the secondary snippet's authority.

Primary URLs opened or whose supplied full primary contents were inspected are:

- https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf — supplied complete primary PDF, with the theorem locations listed above.
- https://www.numdam.org/item/CTGDC_1999__40_3_227_0/ — primary record and supplied complete article.
- https://pi.math.cornell.edu/~kbrown/publications.html — author bibliographic record.
- https://pi.math.cornell.edu/~kbrown/scan/1973.0186.pdf — complete primary scan. Its title page dates volume 186 to December 1973; the author list catalogs it as 1974. The bibliography uses the printed volume date and records the discrepancy.
- https://arxiv.org/abs/1112.3840 and https://arxiv.org/pdf/1112.3840 — author primary record and v2 PDF, alongside the supplied TeX. The published paper is Algebraic & Geometric Topology 13(1), 313–374, DOI 10.2140/agt.2013.13.313.
- The manuscript transcriptions and edition PDFs were provided in the attached workspace and read locally. The web search also located the original edition index at https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html and the XIIc PDF at https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChXIIc-30-03-03.pdf; no additional uninspected result from those search hits is used.

Two attempted metadata opens were unsuccessful: the AMS article landing page returned HTTP 403, and the MSP XHTML landing page was unsupported by the reader. Neither is treated as a verified full-text source. The corresponding bibliographic information was checked through the accessible primary author records and paper scans instead. The exact AMS DOI was not inserted on the basis of the failed fetch.

### Independent cross-review of Part H

H.2–H.7 were read critically after their full proofs were written. The variance of the final-image criterion and the covariant set-valued category-of-elements argument is consistent. The cyclic-subgroup covering argument in H.3 does establish the equality of the two notions of total asphericity; it does not confuse acyclicity of one category with contractibility of every relevant category of elements. H.4's fundamental-group surjectivity argument and groupoid pushout apply in the required direction.

The H.6 coend presentation, its functorial retraction and its natural transformation were checked for both the first interval stage and the uniform n≥2 case. The only needed clarification was that passage from an intrinsic cofibration to its arrow retract uses retract closure of W, supplied by B.1; it does not follow merely from the definition under an arbitrary two-out-of-three class. The authoring agent incorporated that premise. H.7 now also gives the descending natural transformations from the empty constant functor and to the terminal constant functor, so the initial/terminal claim in the localized unpointed category is explicit. No change in the claimed results was needed.

### Exact remaining obligations

**A.16.** Does the literal historical package Loc (1,2,3), with absolute Theorem A, imply relative Theorem A? The transfer attempted here would need objectwise weak equivalences of Grothendieck constructions to belong to the same weak localizer. The absolute comma-asphericity test does not by itself establish that step as written. A first nonterminal relative test base is [1], since over the terminal category the relative statement is tautological. No general implication or counterexample is asserted. The historical minimum is **not** left open: A.19 settles W_omega=W_infinity by the separate weak-localizer theorem. All modern conclusions in A–H use the relative convention expressly required by the prompt.

The sole remaining A/G obligation is the historical absolute-to-relative comparison in A.16. The original abstract factorization-only issue is resolved by G.26, with the finite least-vertex scope and every comparison specified above. The settled modern accessible derivator theorem and the fixed-convention localizer classification do not depend on A.16.

## Parts C and E: verification and corrections

This contribution was produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). It claims no priority. The mathematical deliverables are `sections/C.tex` and `sections/E.tex`, with 18 numbered claims. The exact claim statements and audit metadata are in `research/CE_results.json`. The bibliography fragment is `research/CE_references.bib`; every entry in that fragment is marked verified because the primary text was opened.

### Scope and conventions

All statements about a fundamental localizer use the paper's modern relative-Theorem-A convention. The comparison with the manuscript's weaker literal Loc (1)–(3) is kept in Part A, and is not silently assumed here. Categories and spaces are small in the fixed universe. A larger universe is used for classes of maps where necessary. Accessibility is explicitly imposed whenever the argument constructs a reflective localization of spaces or invokes a set-generated model structure for the given localizer. The classification under the weakest perfect-fibration axiom, E.4–E.5, does not impose accessibility on that localizer.

For a spectrum E the homology convention is the **unreduced** spectrum `E smash Sigma^infinity(BX)_+`. This is essential for Loc (5), for empty categories, and for coproducts. E may be nonconnective, and E = 0 is included. Coefficient rings are arbitrary unital rings, not assumed commutative; their additive Eilenberg–MacLane spectra suffice, so none of the proofs uses commutativity. The finite truncation localizers include n = 0.

### Primary texts read

The relevant sections of the supplied transcription of XVI were read with particular attention to manuscript pp. 17′, 27–45, 68–70, 83, 89–91, and 119–121, and footnote 36. The statements of Loc (7), the relative-reference form `7D_V`, and Loc (7F) were coordinated with the direct axiom audit in Part A. The questions about truncation and generalized homology in pp. 91 and 119–121 are answered by C.5–C.10. The definitions and arguments for `a_n`, `b_n`, and `c_n` were read in XII, manuscript pp. 178–187, including footnotes 116 and 117 and the final assertion on p. 187. The omitted range in the displayed definition of `c_n` is reconstructed as `0 <= i <= n`; the surrounding proof explicitly confirms this range.

Cisinski's complete *Astérisque* 308 PDF was opened and the following exact results were checked:

| Location | Use |
| --- | --- |
| Theorem 4.2.15 and Remark 4.2.16 | Correspondence between fundamental and simplicial localizers, with accessibility. |
| Theorem 5.2.15 | Left proper Thomason models and the equivalence of right properness with properness of the localizer. |
| Definition 5.3.1; Proposition 5.3.4 | The strict-fiber/comma definitions of proper and smooth functors and the interval criterion. |
| Corollary 5.3.6; Proposition 5.3.8 and duals | Base-change and composition closure of proper and smooth functors. |
| Theorem 5.3.14 | Factorization with strongly proper and smooth Thomason bifibrations. E.4 applies it only to the accessible minimal localizer. |
| Proposition 6.1.8 | Accessibility and properness of the localizer generated by all aspherical objects of an accessible localizer. |
| Theorem 6.1.11 | Properness if and only if accessible aspherical generation, equivalently generation by a set of categories to be trivialized. |
| Definition 6.1.13; Example 6.1.14 | The intrinsic weak-fibration definition and the inclusion of Thomason fibrations when the localizer is proper. |
| Proposition 6.2.3 | Intrinsic weak fibrations if and only if every strict base-change square is homotopy cartesian, under properness. |
| Corollary 6.4.8; Propositions 6.4.10 and 6.4.14 | Proper plus smooth implies local constancy; the finite-ordinal test detects universal weak-homotopy pullback behavior. |
| Section 9.2, especially 9.2.1, Corollary 9.2.15 and Proposition 9.2.17 | Truncation localizers, properness, and the generator of type `S^(n+1)`, with its correct index shift. |
| Theorem 9.4.2; Corollary 9.4.3 | Accessible localizers from generalized homology theories. |
| Proposition 9.4.6; Scholium 9.4.7 | Previously stated nonproperness for rational and integral homology, and the relation with plus construction. These special cases were not extrapolated without proof. |

The supplied TeX and the published PDF of Rijke–Shulman–Spitters (2020) were opened. The exact statements used are Theorem 2.19 (nullification is a modality), Lemma 2.20 (an accessible localization which is modal has a nullification presentation), Theorems 1.34, 1.53, and 1.54 (equivalence and uniqueness of the stable orthogonal factorization-system formulation), Theorem 3.1 (left-exact modalities), Theorem 3.8, and Corollary 3.9 with its explicit warning that finite truncation is not left exact. The published numbering, rather than an assumed preprint numbering, was used.

The supplied TeX and primary publication record of Anel–Biedermann–Finster–Joyal's *A generalized Blakers–Massey theorem* were opened. Its modality definition is in **Section 3.4**, and the connected–truncated example is given there. The separate *Left-exact localizations of infinity-topoi I: Higher sheaves* text and publication record were opened for the congruence terminology. Macpherson's 2021 preprint, version 2, was opened; Propositions 3.1 and 3.3, Definition 3.9, and Corollary 4.1 were checked. Its orthogonality-defined model-infinity-category fibrations are not identified with the maximal intrinsic class of functors in Cat used here.

### Main corrections and conclusions

#### The ten axiom columns

For nonzero E, every generalized homology localizer satisfies Loc (4), (5), (6a), (6b), (6c), (8), and (9), and fails Loc (7), even the weakest `7D_Winfinity`, and Loc (7F). For every finite n >= 0, truncation satisfies Loc (4), (5), (6a), (7F), (8), and (9), and fails (6b), (6c), (7), and the weakest (7D). The zero theory is the total class and fails only the connectedness column (5). C.7 displays the complete table, with W0 repeated explicitly.

The nonzero-spectrum proof of connectedness uses a nonzero element of some homotopy group of E and the split point summand in each component's unreduced E-homology. It therefore applies without a connectivity or boundedness hypothesis on E. Finite strings in the nerve and finite sphere/homotopy data prove the filtered-colimit assertions, including the unrestricted filtered-colimit version rather than just sequential colimits.

#### Why generalized homology never has enough intrinsic fibrations

C.4 proves that any E-aspherical connected space has no nonzero homomorphism of its fundamental group to Z. Otherwise S1 is a homotopy retract and Sigma E is a retract of zero. Every subgroup of a free group is free, so every map of that fundamental group to a free group is trivial. Hence free-group classifying spaces are null for **every** E-aspherical object.

C.5 uses the explicit endomorphism of the free group on x,y with `x |-> x` and `y |-> y x y x^-1 y^-1`. It induces the identity matrix on the stable suspension spectrum of the graph, and hence is an E-equivalence for every E, but it is not surjective. The finite S3 witness and all its group calculations were independently checked in Part F. This map cannot be inverted by the nullification generated by E-aspherical objects because its source and target are already local there. The Brown argument in E.2 shows that Loc (7F) would force exactly that aspherical generation. This proves failure of (7F) for **every nonzero spectrum**, not merely for ordinary homology or selected coefficients.

C.6 also gives a direct perfect-functor counterexample with complete objects, arrows, composition, and projection formula. Its strict fiber has the cosets of the nonsurjective free-group image as its connected components. C.10 gives a second useful witness: the action-groupoid covering on three letters is perfect, but pullback along the same endomorphism changes the orbit decomposition from one orbit to two.

#### Intrinsic fibration classes and the exact bounds supplied

C.8 gives an equality description of `Fib_W0`: each strict fiber has exactly one connected component for each component of the total category above the relevant base component, and every base arrow has a lift in each such component. This includes empty inverse images and nontrivial endomorphisms.

C.9 gives an equality description of `Fib_Wn` by the canonical comparison from a truncated strict pullback to the pullback of the three truncated nerves, for **every** base change. The proof verifies the canonical map using right properness and the relative Brown lemma. It agrees with Cisinski's Proposition 6.2.3.

For generalized homology, C.10 supplies the bounds requested as an alternative to an equality classification. The lower class contains all product projections, component inclusions, their closure under composition, pullback and retracts, and the functors with simplicially E-sharp nerves. The explicit upper class `Q_E` requires an E-equivalence from each vertex fiber to the pullback over every finite ordinal mapping to the base. The covering witness lies in `Q_E` and outside `Fib_WE` for every nonzero E, proving that the upper inclusion is strict. For each fixed base, accessibility also reduces the defining test to a set of bounded-cardinality maps. No finite decision algorithm, or false equality between this upper class and intrinsic fibrations, is claimed.

#### The exactness dictionary

E.2 proves `7F <=> aspherical generation <=> set nullification <=> right proper localization`, with the accessibility qualification on the equivalences requiring a set presentation. The necessity `7F => aspherical generation` does not need accessibility. The proof explicitly establishes universal stability of a trivial intrinsic fibration before applying Brown's lemma.

E.3 proves the corresponding equivalence with modality, locally cartesian reflection, and local cartesian closedness of the local infinity-category. The last converse is justified specifically for a reflective subcategory of **spaces**: every object over a local base is a colimit of its diagram of points, its slice reflection is the colimit of that same diagram in the local slice, and an LCC pullback functor preserves that colimit. No preservation of colimits by the inclusion, or preservation of limits by the reflector, is assumed. The nullification-presentation proof takes a homotopy limit over the entire base space; replacing it by a product over a set of points would discard monodromy.

E.4 proves that the weakest perfect-fibration clause is equivalent to arbitrary homotopy-pullback stability of equivalences. The proof verifies all transfers: a perfect categorical replacement using Cisinski's model for Winfinity; strict-fiber/comma comparisons and finite-ordinal tests; and the natural category-of-simplices comparison for arbitrary diagrams of spaces. No accessible reflector for the original W is used.

E.5 then gives exactly two classes under this axiom, Winfinity and the total class, even without accessibility. An aspherical noncontractible fiber can be looped until it is disconnected; pulling back two points in different components forces the empty space to be aspherical, and product stability forces the total class. Loc (5) removes that class. E.6 identifies the same property with left exactness when the accessible reflector exists. Thus Lead 5 is valid with the stronger `7D` interpretation and homotopy pullbacks, but not with `7F` substituted for it. Finite truncation is the explicit counterexample to that substitution.

The right class of the modality is also distinguished from the intrinsic Cat fibration class. Every terminal projection in Cat is intrinsic, whereas the right-class terminal projections of the modality have local sources. The left class of the modality is distinguished from its larger class of reflective equivalences.

#### XII's three truncation classes

E.7 proves the full local-coefficient implications, not just their simply connected special case. Constant-group degree-one cohomology identifies the fundamental groups by a Yoneda-type argument modulo conjugacy. Injective modules over the common group ring then identify the homology maps of universal covers; relative Hurewicz proves the final connectivity implication.

Two manuscript assertions are false as stated. First, `b2 = c2`, so the expectation that each implication is strict fails at n = 2. For n >= 3, the wedge-to-product map `S2 wedge S^(n-1) -> S2 times S^(n-1)` proves strictness, because it kills a nonzero Whitehead product while preserving the specified cohomology groups. Second, `a_n` does not define the localizer of n-types: `* -> K(Z,n+1) -> *` violates two out of three for `a_n`. The actual localizer is `b_n`, and `a_n` is its universal subclass and the left class of the truncation modality.

### Computations

`code/ce_sphere_cover.py` and `code/ce_sphere_cover_output.json` are a deterministic, dependency-free certificate for C.3 at n = 0,1,2,3. The program constructs the finite poset categories, tests all identities and composable pairs/triples, checks every full-sieve and cover condition, checks all functors and commutative faces of both cubes, constructs the nerve's integral boundaries and verifies `d^2 = 0`, and computes Betti numbers over F2 by exact bit arithmetic. The suspension categories have respectively `(objects, arrows)` equal to `(4,8)`, `(8,26)`, `(16,80)`, and `(32,242)`. Their Betti numbers are those of S1, S2, S3, and S4. The proof of integral homotopy type is the exact simplex-boundary face-poset and suspension identification, not an inference from mod-two homology.

`code/ce_truncation_cochains.py` and its JSON output check the finite cellular examples in E.7 at n = 3,...,8. They retain distinct generators when their dimensions agree, verify cellular cohomology ranks and the coefficient-independent restriction isomorphism through degree n, verify the ring identities, and compute the top cross cup product as 1. The Whitehead attaching-map argument remains the explicit topological proof in the paper; the code does not claim to compute general unstable homotopy groups.

The S3 multiplication and orbit computations used in C.5, C.6, and C.10 are supplied by `code/f_free_group_witness.py` and its complete output, with the mathematical construction in F.8. The categorical endpoint pushout-product computation is owned by H.6, not duplicated here.

`code/ce_export_results.py` extracts the exact balanced-brace claim statements from the two TeX sections and combines them with the hand-written audit metadata. Its output records all 18 IDs. Re-running it refreshes `research/CE_results.json`.

### Literature searches and limits of the contribution

Internet searches included combinations of “Cisinski localisateur propre homologie”, “homology localization right proper”, “generalized homology localization proper”, “nullification modality locally cartesian localization”, “locally indicable acyclic free group”, “homology localization trefoil”, and “free-by-cyclic homology equivalence”. These searches led to the primary sources above and were used to check publication metadata and theorem numbers. No exact source for the all-nonzero-spectrum obstruction C.4–C.5 was located in those searches; the paper gives its proof and makes no priority claim. The existence of the familiar rational and integral special cases was verified directly in Cisinski.

No unresolved assertion is promoted to a theorem in Parts C and E. The homological intrinsic-fibration problem is answered by explicit lower and upper bounds, the alternative expressly allowed by the prompt, and by an exact set-sized test; an exhaustive simpler equality classification is not asserted. The unrelated historical comparison of absolute and relative Theorem A remains explicitly separated in Part A. No assertion about an arbitrary ambient infinity-topos is inferred from the dense-point argument special to spaces.

## Part F: sources, proofs, computations, corrections, and open obligations

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

### Sources actually read

The original Chapter XVI transcription was read for Loc (1), (1 bis), (1 ter), Proposition 3.3, and the following discussion. Chapter XII ms. 76 and the corresponding companion row XIIba-A-053 were read directly. The attached complete author TeX of Hovey–Palmieri, *The structure of the Bousfield lattice*, was read in Sections 2, 7, and 9. The attached Berrick–Casacuberta PDF was converted to text and read, especially Theorems 3.3 and 4.3. Hausmann–Husemoller, *Acyclic maps*, was inspected for the distinction between acyclic fibers, twisted homology equivalences, and ordinary homology equivalences; the paper's introduction and first sections were read, but no unverified theorem number is used from it. Cisinski's Astérisque 308 PDF was searched and the exact statements of Definition 3.3.2, Sorites 3.3.8, Proposition 4.2.4, Theorem 4.2.15, and Theorem 9.4.2 were read.

Primary sources additionally opened on the web:

- Tyler Lawson, author PDF dated 11 March 2019, `https://www-users.cse.umn.edu/~tlawson/papers/bousfield.pdf`, especially Example 9.20.
- Casacuberta–Gutiérrez–Rosický, `https://www.ub.edu/topologia/casacuberta/articles/cgr.pdf`, Theorems 3.7 and 3.9, Proposition 3.8, Section 4.
- Wolcott, `https://msp.org/pjm/2015/276-2/pjm-v276-n2-p14-p.pdf`, Propositions 6.2 and 6.4 and the paragraph following 6.4.
- Hovey–Palmieri–Strickland, `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/axiomatic.pdf`, Theorems 2.3.2 and 3.2.2 and the following discussion.
- Hovey–Palmieri arXiv record `https://arxiv.org/abs/math/9801103`, the author's research listing, and the AMS listing for publication metadata.
- Berger–Ratković, `https://math.univ-cotedazur.fr/u/cberger/Gabriel-Morita.pdf`, Definition 2.1, Propositions 2.3–2.8, Remark 2.9; the author's publication list verifies *Applied Categorical Structures*, 27(1), 23–54 (2019), DOI 10.1007/s10485-018-9539-x.
- Pützstück, *Tensor-Nilpotence and the Size of the Bousfield Lattice*, `https://arxiv.org/pdf/2608.06104`, v1 of 6 August 2026. The complete seven-page PDF was downloaded and read after the browser PDF endpoint failed. Theorem 1.1, Corollary 1.2, and Theorem 1.4 concern tensor-nilpotence, Hovey–Palmieri's retract conjecture (3.12), and the cardinality of the Bousfield lattice. They do not settle the distinct localizing-subcategory conjecture (9.1). No claim from a machine-generated review of that paper is used.

Every entry in F_references.bib is marked verified, with the specific material opened. “Verified” is not a claim that every result in the cited source was independently re-proved.

### Searches

Searches were run on 10 November 2026 for combinations of “Bousfield integral homology Morava K theory smash HZ acyclic spectrum,” “localizing subcategories spectra generated bounded below spectra,” “stable acyclic classes spaces suspension localization,” “homotopical localization spaces cofiber homological,” “nullity classes stable,” “localizing subcategory not a Bousfield class spectra,” “Hovey Palmieri Conjecture 9.1,” and specific searches for loc(HFp), loc(I), and loc(HZ). The searches located the author and publisher sources listed above. Secondary snippets were used as leads only, not as authority for mathematical claims. No novelty claim is made for the free-group endomorphism certificate or the Galois formulation.

### Mathematical corrections

Lead 6 is false as a bijection with **all** localizing subcategories, even with accessibility. Both zero and the nonzero HZ-acyclic spectra induce exactly W_Z on maps of spaces. An even more explicit set-generated example is loc(K(n)) for any prime and n>0: it is nonzero, lies in the HZ-acyclic spectra, and has no nonzero connective object. Every cofiber probed by a map of spaces is connective. This is a failure of injectivity, independent of any unresolved converse about the image.

The correct Galois connection is T(W)=loc{cofib(Σ∞_+Bu):u∈W} and R(L)={u:cofib(Σ∞_+Bu)∈L}. The stable fixed objects are exactly L=loc(L∩D), where D is the class of reduced suspension spectra of pointed spaces. Fibers are determined exactly by intersection with D. The unstable fixed objects are the stable-detectable classes W=RT(W). The two operators give inverse order isomorphisms on these fixed objects. This is the precise image description established here; it is not silently expanded to all reversible localizers.

The expression Σ∞cofiber(g) must mean the reduced suspension spectrum with the specified cone vertex. Adding another disjoint basepoint would give the wrong zero test.

The universal plus construction and W_Z have the same aspherical spaces but different equivalences. The explicit endomorphism α of F2, x↦x and y↦yxyx⁻¹y⁻¹, is a homology equivalence but not surjective. Both copies of BF2 are plus-local. Its cofiber is acyclic and therefore plus-aspherical. Thus aspherical-object equality does not imply map-class equality, and plus localization does not satisfy reverse excision. Nullification at any individual acyclic space is also strictly below W_Z and fails reverse excision.

Row XIIba-A-053 is affirmative in the modern relative-Theorem-A convention fixed by the prompt. Cisinski Proposition 4.2.4 supplies arrow-retract closure automatically. A direct Grothendieck-construction argument makes the two pieces retracts of an aspherical homotopy wedge. Reverse excision is not used. This does not claim that the same proof follows from the manuscript's weaker absolute Loc (3) without the relative axiom.

Wolcott's example of a non-Bousfield localizing subcategory lives in the HFp-local category. It cannot be imported unchanged into the entire stable homotopy category; the author explicitly flags this distinction after Proposition 6.4.

### Computation

`code/f_free_group_witness.py` defines every arrow and composition of the one-object category BS3, verifies closure, all 216 associativity triples, identities, and inverses, then checks two distinct homomorphisms F2→S3 with equal composites with α. It verifies α's abelianization matrix is the identity. It also computes the orbits of the action used in Part C: the original action is transitive, whereas the pullback action along α has orbits {1,2} and {3}. Full output is in `code/f_free_group_witness_output.json`.

`code/f_finalize_section.py` performs only idempotent ordering of the separately authored Part F blocks; its output records the statement order. It makes no mathematical inference.

### Exact remaining obligations

F.14 retains the implication “accessible and reversible cofiber detection ⇒ W=RT(W)” as unresolved in this audit. The obstruction in the attempted proof is that closure under finite unstable suspensions and cofibers does not by itself justify transfer of arbitrary stable localizing constructions back to maps of spaces. The Galois formulas remain valid without that implication; Lead 6 is already refuted by the independent noninjectivity example.

F.14 also explicitly retains the test whether loc(HFp), in the category of all spectra, is the kernel of smash with some spectrum. This is an unresolved verification here, not a claim to establish its current research status. The published Hovey–Palmieri Conjecture 9.1 and Proposition 9.2 were checked; no theorem was found in the performed searches that settles the full replacement of arbitrary localizing kernels by homological Bousfield classes. Existence of a localization for a set-generated localizing subcategory is kept separate from homological representability.

The focused follow-up checked exact phrases involving “localizing subcategory,” “HFp,” “HF_p,” “Hovey–Palmieri Conjecture 9.1,” and “Bousfield classes,” including recent coverage. It found Pützstück's 2026 paper and checked its full text as described above. The test is sharpened using the elementary argument in Hovey–Palmieri Proposition 9.2: loc(HFp) is homologically representable if and only if it equals the a(HFp)-acyclic spectra, where a(HFp) is a wedge representing all Bousfield classes annihilating HFp. This is the smallest homological kernel containing HFp, so the precise remaining issue is an equality of two specified subcategories.

For the other F.14 obligation, Berger–Ratković's terminology makes the failed implication particularly clear. Their “excisive” hypothesis is conservative suspension and yields the cofiber diagram lemmas; their stable embedding statement in Remark 2.9 requires *fully faithful* suspension. One cannot substitute the former hypothesis for the latter. The citation is incorporated in F.14; it narrows the exact gap rather than concealing it behind a general stabilization reference.

### LuaLaTeX verification

The supplied TeX installation contained the package trees and LuaHBTeX executable but lacked lookup databases, generated formats/configuration, Lua font-loading dependencies, and Pagella. `code/f_tex_runtime.py` repairs this only inside `tmp/tex`, using an explicit list of five public CTAN packages with SHA-256 hashes in `code/f_tex_dependencies.json`. It preserves HOME and the system installation and retains TeX's restricted write policy, authorizing font-cache writes through the workspace-specific TEXMFOUTPUT. The format output is in `code/f_tex_format_output.txt`. `code/f_check_latex.py` compiled the standalone Part F with LuaLaTeX/BibTeX and two convergence passes; the initial verified version produced a nine-page PDF with no overfull or underfull boxes, missing characters, or unresolved citations. Links to Part B are naturally absent from that standalone wrapper. `code/build_lualatex.py` supplies the same reproducible four-pass build for the integrated paper.

The definitive integrated build, including A.19, the proved G.26 with its finite Reedy construction, H.8, all final Part F additions, the canonical merged bibliography, and the final PDF metadata, completed successfully: 71 pages and 638,865 bytes. The final log contains no LaTeX/package warnings, missing characters, underfull or overfull boxes, or PDF backend warnings. The complete transcript and machine-readable summary are `code/build_lualatex_output.txt` and `code/build_lualatex_summary.json`. The compilation required only typographical corrections to the shared operator macros, A's display line breaking, and G's TikZ cell, table/filename wrapping, and proof subheading commands; no mathematical content was changed by the build repair.
