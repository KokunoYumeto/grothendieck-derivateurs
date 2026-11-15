# STRATA research audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No human authorship or priority claim is asserted for this return. Published mathematical results retain their ordinary scholarly attribution.

## Source authority and the delivered record

The authoritative attachment was the unversioned `5_STRATA_background.zip`, SHA-256 `c4cd2af79619d296dadcb3b30b5b1740c8f0e408f538d820a2d0fddb83ac3c09`. Its 372 files and 37,813,282 uncompressed bytes match the supplied manifest. The numbered archives are earlier snapshots. We used the unversioned archive, which includes the GALOIS follow-up material, and read `PROMPT(9).md`, `BACKGROUND(5).md`, the manifest, and `CHANGES_20261110(3).md` to establish that choice. Archive paths were checked before extraction. `code/00_sources.py` and its output reproduce the inventory, hashes, extraction checks and the root PDF text extractions.

The mathematical paper is ordered A–G and contains **81 numbered statements: 54 Proved, 14 Known, nine Refuted, and four Open**. The preliminary variance statement is included in this count. “Open” means unresolved in this audit; it is not an assertion of global mathematical openness. The register has the exact seven requested columns. Each row is checked against the final TeX identifier and status, and its proof location is supplemented with the PDF page after compilation. The paper uses author–date citations and an APA bibliography. Every bibliography entry carries a verification note; the original Thomason (1979) theorem remains explicitly unverified, although its publisher metadata and the comparison in Cegarra (2020) were inspected.

The archive contains the paper source, all included section sources, the LuaLaTeX PDF, the combined bibliography and results CSV, this report, the authored audit fragments used to assemble it, and the programs with their captured outputs. Downloaded third-party papers, the supplied source archive and the temporary TeX runtime are not redistributed. The ordinary mathematical verification scripts do not require those source PDFs. Source-reading scripts explicitly require the separately supplied background directory.

## Root sources read and checked

The transcriptions and companion passages are distinguished from primary literature. A companion assertion is not promoted to a theorem merely because another attached AI return labels it Proved. Part C checks the supplied proof of open–closed gluing and its actual comparison map, as requested, instead of supplying a third proof. The detailed C/D, E and F records below identify every source passage used there.

For A and B, we read the attached Barwick–Glasman–Haine *Exodromy* source, especially Chapter 2 on conservative/layered categories and Chapter 3, Proposition 3.12.11, Example 3.12.15 and Warning 3.12.16. The author PDF dated 21 August 2020 was opened to verify the numbered statements. We opened the full publisher text of Ko Aoki (2023), *Tensor triangular geometry of filtered objects and sheaves*, including Appendix A and Examples A.11–A.13. Its explicit infinite Alexandrov example is reproduced mathematically and its finite join models are computed.

We read the supplied *Higher Algebra* PDF dated 18 September 2017, Appendix A, including A.5.9, A.6.4, A.6.8–A.6.11 and A.9.3; the appendix text was extracted locally for checking. The categorical formulas also use the inspected tensor-product and monadicity statements 4.8.1.17 and 4.7.3.5. We opened the current author version of Haine–Porta–Teyssier, *Exodromy beyond conicality*, dated 26 April 2026, and checked Theorems 3.3.5 and 5.1.7, Lemma 4.1.2, Corollary 4.1.15, Example 5.3.2 and Section 5.6. Their intrinsic exit construction was not silently identified with the raw exit simplicial set. The explicit cone charts in A.4 and B.3 establish the needed conicality. Haine–Porta–Teyssier (2023), *The homotopy-invariance of constructible sheaves*, was also opened, with its coefficient and hypercompletion distinctions retained.

Kerodon Subsection 6.3.6 was opened in full. Proposition 6.3.6.2 is the universally localizing last-vertex theorem used in the finite-poset and finite-acyclic computations; Theorem 6.3.6.1 supplies a genuinely marked poset presentation for an arbitrary category. The elementary roof sketches were not substituted for the full infinity-categorical localization theorem. The Haine stratified homotopy-hypothesis source was read for its conservative-category formulation; it does not on its own prove ordinary sheaf exodromy for every prescribed weak CW realization.

We read Cisinski (2009), *Locally constant functors*, in its supplied published PDF, especially Theorem 3.13 and its indexing convention. We read the supplied GALOIS arguments A.6, A.8, C.1, the coefficient tests in Part C, and the reconstruction qualifications in F.1–F.3 and F.8. B.10–B.11 give the explicit reconstruction and restriction arguments, including the use of cotensors and specified evaluation. Rivera–Wierstra–Zeinalian (2021), *Rational homotopy equivalences and singular chains*, Theorem 3, was opened in the full repository manuscript; its statement includes the actual fundamental-group isomorphism and not merely a rationalized or completed fundamental group.

The supplied Carcacía Campos preprint arXiv:2611.09718v1 was read at Theorem 6.2. B.4 gives an independent homeomorphism proof for its three-object projective-plane category by a free antipodal quotient of the octahedral poset. The proof does not infer a homeomorphism from matching homology.

For G, we read TOTASPH's comprehensive-factorization, category-of-elements and total-asphericity arguments, including B.11 and the relevant part of C. The exact equivalence between totality and homotopical strict colimits is proved in G.2; no assertion that filtered categories are the only such categories is used. We read POLES C.8–C.9 and E.4–E.5. The proof of the two-extreme-localizers assertion is reproduced in G.5, with its perfect-model transfer specified. We opened Cisinski (2006), Proposition 6.2.3, and the exact truncation passages Section 9.2.1 and Corollary 9.2.15 before applying the proper-localizer criterion. GALOIS E.7's accessible-localized-space realization was checked through its Yoneda and product-stability arguments, with Cisinski's Theorems 1.4.3 and 4.2.15 supplying the correspondence.

## Corrections to the proposed dictionary

**Lead 1 requires hypercompletion for arbitrary Alexandrov posets.** With downsets open, the coefficient variance is `Fun(P^op,Spaces)`. This is the category of hypersheaves for every small poset. Ordinary sheaves agree for finite principal downsets, but the unrestricted assertion is false even for interval-locally-finite posets. Aoki's layered example proves the failure through compactness of the terminal object. This distinction does not by itself refute the separate geometric realization clause.

**Raw exit calculations and geometric sheaf exodromy are separate.** A.4 proves the finite minimum-vertex geometric dictionary, including explicit conical charts. A.12 proves the raw exit category is `P^op` for every small poset by compact containment in a finite CW subcomplex and filtered unions. Neither proof licenses ordinary geometric sheaf exodromy for every infinite weak CW realization. For arbitrary presentable coefficients the finite geometric comparison is proved to be fully faithful; the cited results give essential surjectivity in the stated compactly assembled and stable ranges. A.6 retains the remaining clauses explicitly.

**A bare derivator is not automatically a theory of sheaves on a topological site.** Its cellular coefficients, restrictions, pointwise Kan extensions and locally constant reflection are defined by Der 1–4. The geometric comparison requires a specified enhancement and an exodromy theorem. Stable coherent exact sequences and strong stable triangulated recollement are also distinguished. No strongness axiom is inserted into Cisinski's locally constant adjoint theorem.

**Lead 2 is exact for layered categories, not all ordinary categories.** B.1 proves that an ordinary category is conservative over a poset exactly when it is EI. The stratum at an object has the classifying-space type of its automorphism group, and the crossing hom-sets and their composition must remain in the data. B.2 gives the exact abstract stratified-topos dictionary. B.3 proves the literal finite acyclic realization, allowing parallel arrows. B.5 retains the unrestricted EI ordinary-sheaf realization as a separate audit boundary.

**Noninvertible endomorphisms give a Morita-level obstruction.** The atomic objects of a presheaf infinity-category recover idempotent completion. Consequently a category with a noninvertible endomorphism cannot even have an enhanced presheaf category abstractly equivalent to that of a layered exit category. The one-object two-arrow idempotent monoid is a complete minimal counterexample, despite its contractible classifying space. Unmarked subdivision cannot remove this obstruction; marked localization retains the category by requiring specified coefficient arrows to be equivalences.

**The two invariants require their exact extra data.** `BS` determines the locally constant enhanced theory, while the fine enhanced theory determines the Karoubi/Morita class. The point and interval separate these invariants by their numbers of subterminal presheaves. The ordinary homotopy category together with its specified constant-diagram functor recovers `BS` by Yoneda. Enhanced linear coefficients with their evaluation recover the actual loop algebra, rather than only its module category. B.12 retains the missing reconstruction from bare ordinary categories. The coefficient table in B.11 is a theorem about the specified restriction functor, not arbitrary abstract category equivalences.

**Lead 3 needs directed links and coherent gluing.** The crossing category models the homotopy link with its endpoint maps. Its open endpoint is the actual complement of the closed subcomplex, which retracts onto the open indexing category's realization. Ordinary path spaces can change the answer. Finite filtrations retain all flag categories and their composition data. Enhanced constructible coefficients form a lax pullback; passing to homotopy categories before taking the lax pullback loses morphisms. Locally constant enhanced coefficients form the ordinary pullback in `Cat_infinity`. The detailed C/D record gives the finite tests against the supplied TOTASPH examples.

**Lead 4 separates categorical properness, smoothness and ambient operations.** The exact outgoing and incoming lift-category tests determine the manuscript's categorical adjectives. Every finite-poset realization map is topologically proper, which does not imply categorical properness. A proper endpoint cosieve fails the local-constancy/Quillen-B condition. The proper-and-smooth diamond has no opcartesian lift. Intrinsic Kan adjoints need not be ambient topological direct images: the vertex-0 inclusion in the minimum-stratified interval gives a skyscraper that is not constructible. Closed inclusions, finite product projections and the verified moduli maps provide literal geometric classes with their stated coefficient hypotheses.

**The CATHOT patch construction has a positive classifying-space result and a negative raw-adjoint result.** E.5 proves `BK_lambda(Y) ~= Y` naturally. E.6 proves that its integration represents the given local system, and states a sufficient trivial-Kan-fibration transition hypothesis for bifibrancy. E.7 refutes the proposed general adjoint step by a weak equivalence between two contractible Kan complexes. This is a failure of that construction, not a counterexample to VIc-C008.

**Cisinski's perfect replacement does not settle strict bifibrations, but every poset base is affirmative.** Proper-and-smooth functors need only homotopically contractible lifting categories. Strict Grothendieck bifibrations have universal lifting arrows and adjoint transports. The alternating construction retains the former but need not retain the latter through an arbitrary filtered colimit; finite initial chains with growing maxima demonstrate the exact loss. E.8–E.9 extend the affirmative cases to all 1-truncated fibres and all bases with 1-type classifying space. E.10 additionally proves the result for every small category whose arrows are all monomorphisms, or all epimorphisms; this includes every small poset without a dimension restriction. An injective fibrant replacement of the entire locally constant simplicial diagram has trivial-Kan-fibration transitions under these cancellation hypotheses. The patch adjunction then supplies the missing universal lifts. Functoriality is stated on strict models with a uniform size bound for the chosen replacements. E.11 retains the general problem over noncancellative bases.

**The moduli ordinary-category theorem is known, but its variance and strict models matter.** The four-pointed and five-pointed cases are fully specified before the general construction. Jansen's theorem gives the ordinary exit category. Under the manuscript's presheaf convention the coefficient indexing category is its opposite, the entrance/degeneration category. Forgetting is categorically proper for the specified full multicurve model and fails smoothness already at five to four markings. Clutching uses a replete closed cosieve to make a strict proper model; the literal fixed-curve product inclusion is not proper in that strict sense. The Lego comparison retains the mapping class group action, and the open groupoid is distinguished from the full degeneration category and both kinds of groupoid completion.

**Other localizers are not devoid of a coefficient interpretation.** Finite truncation detects locally constant truncated coefficients. Its intrinsic fibration condition is a pullback formula in n-types, not an ordinary-space homotopy-pullback formula. Universal stability of ordinary-space equivalences under all homotopy pullbacks has only the two extreme solutions proved in G.5. Accessible localizations still realize constant-coefficient tests. Total asphericity likewise translates to an exactness condition on indexing, while conically smooth atlases, tubular embeddings, dimensions and dualizing data remain additional geometric structure.

The supplied transcription corrections established here are I ms.54's target of the fibre inclusion, XII ms.59's specialization-order formula under the stated downset topology, XI ms.131's fibre-map source and target, and XVI Lemma 4.4.1's output factor. The report does not describe these as corrections to a handwritten scan that was not inspected. POLES G.8's false reverse integral-smoothness implication is not used. POLES G.6's corrected punctured-category sphere example is not needed in the proof, so it has not been reasserted on the strength of the attachment alone.

## Computations and build checks

`AB_checks.py` gives complete finite categories, identity and associativity checks, normalized nerve boundary matrices, exact rational ranks and integral Smith forms. The R2 category has three objects, nine arrows, normalized simplex counts `(3,6,4)` and first integral homology `Z/2`; its octahedral cover has counts `(6,12,8)` and top homology `Z`. The triangle-boundary face poset has counts `(6,6)` and first homology `Z`. The first four finite Aoki layer models give the expected joins of zero-spheres. The idempotent monoid and its Karoubi hom-sets are verified exactly. The source and target topological identifications still come from the proofs, not from homology tests.

`G_checks.py` constructs and checks the fork, its four-object element-circle category, the one-object C2 base, the two-object translation groupoid and its strict pullback. It verifies every composition and both unique-lift conditions for the groupoid projection. The pullback has two components and the base point one. It also checks the complete four-arrow mixed EI category retained as an open geometric test in B.5; that last computation is not labelled a counterexample.

The C/D, E and F computational records are given in the detailed records below. All mathematical finite checks pass. The verification methods distinguish ordinary category axioms, homotopies supplied by actual natural transformations, integral homology, weak contractibility, and homeomorphism; none is silently substituted for another. A final proof review improved E.10 from a low-dimensional affirmative class to every small poset. The six-object sphere poset is accordingly an affirmative example in the delivered paper. We replaced it as the remaining test by Fiedorowicz's one-object five-arrow rectangular-band monoid, whose classifying space is a sphere. The primary 2002 proof was opened and its multiplication, projective resolution and integral chain calculation were checked explicitly. No minimality in arrow count is asserted.

`assemble.py` builds the requested CSV and bibliography, checks all 81 identifiers and statuses, checks citation-key coverage and verification notes, and inserts page numbers from the final `.aux` file. `build.py` performs the actual LuaLaTeX, BibTeX and repeated LuaLaTeX passes and records the final compilation diagnostics. The minimal environment's missing generated TeX configuration was repaired entirely in a separate workspace directory by `E_texenv.py`; its source, setup output and smoke test are included. The paper itself uses standard packages and can be rebuilt by ordinary LuaLaTeX on a full TeX installation. The final PDF is visually inspected after rendering; its diagnostic and page-inspection records are included with the build outputs.

An initial serialization error in `G_checks.py` was corrected by converting exact SymPy matrix entries to Python integers; no mathematical calculation changed. The first paper compilation exposed an unavailable `longhookrightarrow` macro, which was replaced by the standard `hookrightarrow`. Failed intermediate build logs are retained for transparency alongside the final successful log.

The first complete visual inspection found two stranded headings, at the starts of subsection A.3 and section G, where the following numbered statement's space guard had forced a page break. The final source reserves space before section and subsection headings. Bibliography entries are also kept together to remove a one-line continuation at a page boundary. Title spacing keeps the entire conventions block on the first page as requested. The paper was rebuilt and all pages rendered again after these layout corrections; unchanged rendered pages retain their inspection by exact image comparison.

## Exact unresolved statements

| Identifier | Exact missing conclusion | What is established and where the attempt stops |
|---|---|---|
| A.6 | Essential surjectivity for arbitrary presentable geometric coefficients, and the ordinary geometric sheaf dictionary on every unrestricted infinite weak CW poset realization | A.3 proves arbitrary Alexandrov hypersheaf coefficients; A.4–A.5 prove the stated finite geometric ranges; A.12 computes the raw exit category for every poset. The unsupported step is geometric ordinary-sheaf exodromy outside those hypotheses. The two-element coefficient case outside the cited classes and Aoki's explicit infinite layered realization are retained tests. |
| B.5 | Ordinary constructible sheaves on every prescribed EI minimum-isomorphism-class realization equal the intrinsic diagram theory | B.1–B.3 prove the abstract EI dictionary and the literal finite acyclic case. A groupoid with one stratum is affirmative. The two-object category with automorphism C2 at the source and one arrow to a terminal target is the smallest mixed finite candidate outside the supplied finite proof; no counterexample is asserted. |
| B.12 | Recovery of the fine or coarse invariant from a bare ordinary coefficient category without enhancement, constants or evaluation | B.6 and B.10–B.11 prove recovery with exactly those data. The proof cannot identify the missing mapping spaces, specified constant functor, or evaluation monad from the bare category. No minimal counterexample or literature-wide openness is claimed. |
| E.11 | Every locally constant object over every small category has a strict Grothendieck bifibration representative, functorially and with the claimed fibrewise-localization equivalence | Perfect replacement, patch integration, 1-type fibres, 1-type bases, and all bases with exclusively monic or exclusively epic arrows are proved; in particular every small poset is settled. The remaining test is the one-object monoid `M = {1,e00,e01,e10,e11}`, with `eij ekl = eil` and identity `1`. Its classifying space has type S2, and the specified path local system has fibre `Omega S2` and contractible total space. The representable maps needed by the injective argument fail to be monomorphisms. Raw patch adjoints fail; filtered colimits do not preserve universal arrows; the free-bifibration theorem lacks the needed weak-homotopy comparison. One object is minimal for a nonempty base; no minimum arrow count is claimed. |

## Literature searches and attribution limits

Root searches used exact phrases involving Alexandrov infinity-topoi and hypercompletion, infinite poset sheaves, finite-poset exodromy, coarsening and coefficient exodromy, EI categories and conservative functors, atomic-object Morita reconstruction, last-vertex localization, classifying-space categories with idempotents, and the Rivera–Wierstra–Zeinalian loop-chain theorem. Exact primary statements were opened when routine searches had incomplete coverage. The detailed subrecords list the bifibration, moduli, gluing and base-change searches. No failure to find a theorem is described as evidence of novelty.

The work supplies no profinite completion of the moduli category, arithmetic Galois action, or comparison with the Grothendieck–Teichmüller group. The specified category, its functors and their strict model qualifications are provided as the requested input for that separate task.

## Detailed record for gluing and base change

## STRATA Parts C and D: audit record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No priority is claimed. The supplied companion, POLES, TOTASPH, and GALOIS files are drafts whose specified arguments were checked, rather than authorities from which their assertions were adopted wholesale.

### Deliverables and scope

The mathematical text is in `sections/C.tex` and `sections/D.tex`. The register `audit/CD_results.csv` contains 20 statements: 13 labelled Proved, four Known, and three Refuted. Its columns are exactly those requested in the prompt. The 12 entries in `audit/CD_references.bib` all have explicit verification notes. `code/CD_checks.py` and its captured output give the finite category, naturality, lifting, and homology checks. `code/CD_metadata.py` and its output reproduce the register and verify statement IDs, labels, proof delimiters, citation coverage, and bibliography verification notes.

Every coefficient construction uses presheaf variance, `D(X) = Ho Fun(X^op,C)`. A sieve is a downset/open indexing category. The geometric realization uses the minimum-vertex convention on `NX`, equivalently the last-vertex convention on `N(X^op)` with the opposite stratum order. The statements do not silently replace an arbitrary derivator by an infinity-category enhancement.

### Sources inspected

#### Manuscript and supplied audits

We read the supplied transcription and companion blocks for I ms. 1–9, on support and exceptional adjoints, and I ms. 49–59, on the fibre-comma comparisons and the proper/smooth conditions. We checked the proper-cosieve assertion at Ib-C003 against the literal outgoing-lift definition. We read XII ms. 59–63 for the order/topology convention, the crossing bimodule, and the SGA 4 gluing description; the resulting conclusions are also compared with XII appendix ms. 17–18 and row XIIapp-G11.

The whole proof of POLES G.19 was inspected. We checked its three-fibre Grothendieck-construction category, its functor to `X`, the components and typing of both natural transformations in each comma category, and its empty cases. C.3 records these checks and compares its actual cocone with the homotopy-link evaluation prism. We do not give a third proof of the directed gluing theorem.

We read POLES G.8 to identify the failed reverse integral-smoothness assertion. **No reverse integral-smoothness implication from POLES G.8 is used anywhere in Parts C or D.** Neither reverse excision nor inference of componentwise contractibility from contractibility of a total gluing is used. The categorical proper/smooth tests are instead verified directly from the exact lifting categories.

We read and independently checked TOTASPH F.14, F.18, and F.21. Their roles are sharply separated: F.14 supplies a degreewise crossing-weight criterion to audit; F.18 supplies the seven-arrow couniversal attachment with a disconnected individual crossing category; F.21 supplies the eleven-arrow attachment whose ordinary weighted coend fails to preserve an objectwise equivalence. We proved the universal pushout assertions by relative natural transformations, not by finite enumeration.

GALOIS A.8 and B.3/B.5 provide the previously audited locally constant comparison and abstract-derivator invariance context. C.8 makes its additional enhancement hypothesis explicit. GALOIS D.9's correction to Ib-C003 was independently verified in D.5 by the endpoint cosieve `{1} -> [1]` and its comma transition `empty -> point`.

#### Primary literature

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

### Corrections and distinctions established

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

### Computations and reproducibility

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

### Literature search record

Searches used the titles and exact theorem phrases for Douteau–Waas's homotopy-link comparison, Groth's pointed derivator theorem, and Groth–Ponto–Shulman's homotopy-exactness criterion. Initial routine searches had incomplete coverage, so the exact primary papers were opened and their attached TeX was searched directly. Separate searches concerned finite-limit preservation by geometric realization, coefficient versions of nonabelian proper base change, and Lurie's Corollary 7.3.1.18. These led to the inspected Kerodon, HTT, and Haine passages recorded above. A search for `discretely flat` and `Theorem 1.5` led to the published Hackney–Ozornova–Riehl–Rovelli paper; the primary PDF hosted at Rochester was opened after the publisher PDF endpoint returned no readable lines. We checked the generalized statement in Section 4, not only the narrower theorem in the introduction. A search for infinity-categorical collage/gluing descriptions did not supply an additional result that was used; C.6 is proved directly from Kan extensions and the reconstruction pullback. No novelty assertion is based on failure to find a reference.

### Remaining scope and coordination

No additional C/D claim has been relabelled Proved by omitting a required hypothesis. The unqualified path-space replacement, ordinary-homotopy-category lax gluing, and geometric adjective identifications are refuted, with explicit counterexamples. The general diagrammatic and enhanced statements are proved at their stated scope; the geometric coefficient hypotheses are those of Part A and the sources cited in D.8.

We did not use or assert the possible further strengthening that every categorically proper finite-poset map has ambient constructible direct image equal to its intrinsic right Kan extension. The task's intrinsic theorem is proved for all such maps, its unrestricted ambient reading is already refuted, and D.8 explicitly names the geometric classes for which a literal comparison is proved. Likewise the homotopy-link comparison is not substituted for the additional geometric exodromy question for arbitrary EI spaces. These non-used strengthenings are not prerequisites for any C/D conclusion.

Part E uses D.6 only for the strictness separation between proper-and-smooth maps and Grothendieck bifibrations. Part F was advised to use replete full entrance cosieves for strict closed-boundary representatives: an equivalent but non-replete fixed-object inclusion can fail the exact outgoing-lift test. Questions about the forgetful moduli functor are addressed in Part F, not silently assumed in the base-change theorem.

At the parent's request we also reviewed G.4–G.6. We opened Cisinski (2006), Section 9.2.1, pp.364–365, where the truncation localizer generated by `Delta/partial Delta^{n+2}` is explicitly proved proper, and Corollary 9.2.15, p.369, identifying its equivalences with the stated homotopy-group truncation convention. G.4 was patched to cite those passages and Theorem 5.2.15 before using Proposition 6.2.3. Its level-zero component/lift proof was checked. The loop/fibre argument in G.5 and the constant-coefficient Yoneda argument in G.6 were checked without finding an additional hypothesis gap. The shared Cisinski bibliography entry and the parent report record those G references.

## Detailed record for bifibrations

## Part E audit record

### Scope and result

Part E contains twelve numbered statements: eight Proved, one Known, two Refuted, and one Open. The full ordinary strict-bifibration assertion of VIc-C008 remains unresolved in this audit. We prove existence for every small poset, more generally every small base with all arrows monic or all arrows epic, every base whose classifying space is a 1-type, and every local system with 1-truncated fibres over any base. There is no remaining poset-base existence gap. We do not describe the unrestricted assertion as a known open problem in the literature.

The distinction that matters is between ordinary cartesian/cocartesian universal arrows and homotopically contractible lifting categories. An ordinary bifibration has adjoint transport, and its transport functors are automatically nerve weak equivalences. Proper-and-smooth functors need not be bifibrations as specified ordinary functors. Part D supplies the finite diamond counterexample; Part E does not duplicate that program.

### Sources opened

The first mathematical source opened for Part E was Denis-Charles Cisinski, *Les préfaisceaux comme modèles des types d'homotopie* (2006), Theorem 5.3.14. Its full PDF was downloaded from the author's site, `https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf`, and pp.230–231 read. Proposition 5.3.13, Corollaries 6.4.8 and 6.4.16, and Theorem 6.4.15 were also read. The model-structure theorem is not a statement about Grothendieck bifibrations.

The supplied Chapter VI-c transcription and companion discussion at ms.186–195 were read, including VIc-C008 and the fork-support obstruction. The supplied Chapter XI §1 transcription (ms.127 onward) and Chapter XVI §4 (especially ms.41–44 and the comparison surrounding Theorem 4.4.13) were read. The CATHOT D.1 proof and its model-structure supplement were read. E.5 proves the additional classifying-space assertion directly using the simplex category.

Bryce Clarke, Gabriel Scherer, and Noam Zeilberger, *The free bifibration on a functor*, arXiv:2511.07314v3 (15 January 2026), was opened at the arXiv abstract and in full PDF. Theorem 1.17 and Propositions 1.23–1.24 were inspected. These give a free ordinary bifibration, a fully faithful unit, and a retraction of underlying categories. They do not state the weak-homotopy comparison needed for the present question. We do not infer that comparison from full faithfulness or a retraction alone.

François Lamarche, *Path functors in Cat*, HAL hal-00831430v3 (19 September 2013), was read through the indexed author manuscript. The direct HAL request returned HTTP 403 and the direct Citeseer PDF request returned HTTP 404; the browser-indexed complete text was available. Section 4 expressly says that its path-based weak equivalences differ from standard categorical nerve weak equivalences. This prevents an unqualified substitution for W∞. The description is a bibliographical boundary, not a claim that no useful comparison can exist.

A. M. Cegarra, *Cohomology of Homotopy Colimits of Simplicial Sets and Small Categories* (2020), was opened on the publisher's site; §3.1, equation (9), identifies the Thomason comparison explicitly. A final targeted search for the original 1979 Thomason paper used both search engines, its exact title, Theorem 1.2, and PDF-oriented queries. The publisher's Cambridge page was opened and verified the journal, 1979 publication year, pages 91–109, and DOI 10.1017/S0305004100055535, but exposed only the extract and references with a “Get access” notice. The publisher content endpoint was unavailable; no accessible primary full paper was found in that targeted search. The original theorem therefore remains honestly marked unverified. The already opened Cegarra formulation, rather than an inaccessible primary page, supplies the checked comparison used here.

Jacob Lurie, *Higher Topos Theory* (2009), was opened in the complete IAS-hosted PDF. Proposition A.2.8.2 gives the injective diagram model structure with objectwise cofibrations and weak equivalences. Proposition A.3.3.2 and Remark A.3.3.4 explicitly verify its simplicial model structure. We give the needed horn-lifting proof directly in E.10. The existing bibliography key FLurieHTT2009 is reused.

Zbigniew Fiedorowicz, *A counterexample to a group completion conjecture of J. C. Moore*, Algebraic & Geometric Topology 2 (2002), 33–35, was opened in full at arXiv math/0202260. Its unnumbered lemma on pp.33–34 identifies the five-element rectangular-band monoid's classifying space with S². The article includes a complete length-two projective resolution; we verify that resolution in E.11 and in the accompanying program.

### Literature searches

Searches used the phrases “Cisinski Les préfaisceaux 5.3.14 bifibration Thomason”, “Grothendieck bifibration homotopy local system every functor weak equivalence replacement”, “category contractible spaces bifibration locally constant functors adjoints”, “algebraic Kan fibrations base change left adjoint”, “free bifibration ordinary category adjoints homotopy equivalence”, “Lamarche Path functors homotopy”, and “Thomason 1979 Homotopy colimits category small categories Theorem 1.2”. Search results were treated as leads; claims used from the free-bifibration and Cisinski sources were read in the primary texts. Further searches used “bifibration injective simplicial”, “injective model structure simplicial A.3.3.2”, and “classifying space rectangular band monoid 2 sphere”; the model-structure and monoid claims were then checked in the primary texts. No priority claim is made for any argument in Part E.

### Computation

The program code/E_finite_checks.py verifies the finite chain examples of E.4, including the ordinary universal lifting property and its loss under the next inclusion. It checks the complete two-object four-arrow groupoid and point-patch obstruction of E.7. It checks the six-element sphere poset, its composition relation, boundary-square-zero identities, simplex counts, and rational homology; E.10 now settles its bifibration existence question affirmatively. Its sphere identification is proved by the join decomposition, not inferred from homology alone.

The same program checks the full multiplication table of the five-element rectangular-band monoid, all associativity and unit equations, every cancellation test, the idempotent right-module projectors, and the exact integral projective resolution used in E.11. The post-tensor chain complex is Z² → Z → Z with differentials (1,1) and zero, giving H₂=Z and no higher positive homology. The paper combines this with simple connectivity and Hurewicz–Whitehead, rather than inferring homotopy type from a finite bar truncation. Its complete output is code/E_finite_checks_output.txt.

The program code/E_make_register.py writes the twelve result-register rows and reports their status counts. Its output is saved separately.

### Corrections and exact boundaries

The added CATHOT patch lead has a positive classifying-space answer: BKλ(Y) is naturally weakly equivalent to Y. The associated raw opfibration does represent the local system, with the stated variance. The proposed adjoint step is false for these raw patch categories: inclusion of one vertex into the contractible two-object groupoid nerve produces postcomposition with neither adjoint. Enlarging the collection of nonempty domains alone cannot fix the strict-over-the-base vertex obstruction. This example does not refute the existence of a different bifibration representative.

E.10 repairs the patch route for all-mono or all-epi bases by replacing the entire diagram first. In presheaf variance, a monomorphism α:s→t makes the representable map h_s→h_t an injective cofibration. Injective fibrancy makes RF_t→RF_s a Kan fibration; locality makes it a trivial Kan fibration. Integrating the opposite patch categories gives the right-adjoint transports required of a Grothendieck fibration. The covariant all-epi argument is dual. The comparison is diagramwise and natural, with a uniform cardinal chosen for any specified small family of replacement models.

The alternating replacement provides a functorial perfect representative and a fibrewise equivalence on weak-fibration input. It does not by filtered-colimit reasoning alone provide ordinary universal lifts. The increasing-chain example demonstrates exactly which universal arrow fails to remain cartesian.

The read transcription of XI ms.131 displays a fibre map with wrong source/target labels: it must be X′_s→X_s for the displayed map X′→X. The type in XVI Lemma 4.4.1 must be p∈F in f=pi, as its later restatement confirms. No new correction to the mathematical content of the companion's strict-bifibration warning is asserted.

### Remaining exact question

E.11 retains unrestricted essential surjectivity outside the affirmative classes and the stronger general fibrewise-localization equivalence from VIc-C008. Its explicit remaining test is the one-object monoid M={1}∪{e_ij : i,j∈{0,1}}, with e_ij e_kl=e_il, and the path local system classified by *→BM≃S², whose fibre has type ΩS². Every nonidentity arrow fails both cancellation properties, so the representable inclusions required by E.10 are unavailable. The precise question is a strict bifibration with that local-system class and weakly contractible total category. One object is minimal for a nonempty base; no minimality among numbers of arrows is claimed.

The former six-element sphere-poset test is settled affirmatively by E.10 and is no longer presented as unresolved.

An algebraic-Kan-fibration attempt was considered: change of base has a plausible algebraic left adjoint, but its preservation of weakly contractible total spaces was not proved. Existing chosen fillers can collide under noninjective base maps, so merely calling the new cells “horn fillings” does not establish that comparison. A proof of that preservation statement, or a suitable homotopy theorem for the free-bifibration unit, would still be required before either route could be used.

## Detailed record for the moduli calculation

## Part F audit

The ordinary-category assertion in Part F is known. The decisive additional primary source is Mikala Ørsnes Jansen, *Moduli stack of stable curves from a stratified homotopy viewpoint*, arXiv:2308.09551v2 (2023), Construction 3.18, Proposition 3.23, Corollary 6.6 and Theorem 6.7. Its theorem identifies the **exit infinity-category**, rather than only the ordinary homotopy category or classifying space. The category used with Grothendieck's presheaf convention must be its opposite: `T_{0,n}=C_n^op`. In Jansen's notation `C_n` is `CL_S`; the original Charney–Lee degeneration category is its opposite.

### Sources read

The attached Keel PDF was read in the Introduction and Catalogue, Facts 1–3 (pp. 546–552), for normalization, the universal curve, normal crossings, and the boundary product. The attached Bakalov–Kirillov TeX was read, with the arXiv PDF opened to verify theorem numbering: Main Theorem 4.9 is the genus-zero simple-connectedness assertion, and Main Theorem 4.24 is the arbitrary-genus assertion. The attached Esquisse §2 (printed pp. 9–11) was read for the precise object of the tower and the warning about multiple basepoints.

The attached Longue Marche P021–P024 were searched and the definitions in §19, manuscript p. 102, scans 204–205, were read directly; P034–P036 were searched and the relevant §26 continuation and §27 filling passage, scans 331–350, were read. The supplied P034 extract starts after the actual modular-topos definition. The missing preceding definition was obtained from the publicly available Grothendieck Circle Part Ib transcription: §26, equations (19)–(25), printed pp. 5–6. This is an additional primary source, not a reconstruction of an absent attachment. The retained-marking subgroup and the orientation-preserving subgroup are kept distinct from Grothendieck's full homeomorphism-component groups.

Additional opened primary sources are Fadell–Neuwirth (1962), Theorem 3; Kent–Leininger–Schleimer (2009), §2.1, Lemma 2.1, Theorem 7.1 and §7.1; and Lurie, *Higher Topos Theory*, Corollary 7.3.1.18 and Remark 7.3.1.19. The Hatcher–Lochak–Schneps PDF was opened through local text extraction, but its font encoding produced corrupted text (34,119 unexpected control characters); no mathematical assertion is based on that extraction.

### Corrections and distinctions

1. The requested `T=Exit` together with `HOT(T)=Ho Fun(T^op,Spaces)` needs an opposite. F.8 states the corrected variance.
2. Asphericity of strata is insufficient to prove ordinariness of the exit category: the sphere stratified by one point and its complement has contractible strata but an exit mapping space equivalent to a circle (F.3).
3. The five-pointed category is finite on **isomorphism classes of objects**, with 26 such classes, but has infinitely many arrows. The 81 comparable pairs checked by code belong only to its quotient poset of stratum types; they are not the number of arrows of the exit category.
4. Clutching into a fixed separating curve gives an equivalence onto a full fixed-curve subcategory. Its replete enlargement is the actual cosieve in entrance variance and is proper. The literal fixed-curve inclusion into the full multicurve model is not proper: an isomorphism to a missing isomorphic target object has no exact lift. The distinction is retained because strict properness is not invariant under arbitrary changes of skeleton (F.12).
5. For the exact full multicurve forgetful functor, F.10 proves categorical properness through actual lifting categories. It reduces each category to the reverse-inclusion poset `{rho contains sigma: q(rho)=eta}`. The tree part is the existing Bass–Serre description of Kent–Leininger–Schleimer; peripheral lifts add leaves. The proof handles arbitrary nodal sigma by cutting at sigma and retaining the unique component containing the forgotten puncture. No comparison of inverse limits or pro-objects is used.
6. The forgetful functor is not smooth already for five to four markings. The specified outgoing EXIT lifting groupoid is equivalent to `B Z`; in entrance variance this is the smoothness test (F.11). The counterexample is infinite, so a finite enumeration is not presented as its proof.
7. Proper topological base change and proper categorical base change are both stated, but their identification is asserted only after a comparison between the strict pullback category and the entrance category of the geometric pullback. The topological theorem is stated for pullbacks among locally compact Hausdorff spaces. The categorical theorem applies to all strict pullbacks of the specified proper representatives. Point fibres and pullbacks of replete boundary inclusions have the required geometric comparison, checked explicitly in F.13–F.14. Product exodromy on contractible charts proves preservation of constructibility; uniqueness of the right adjoint identifies direct image with right Kan extension.
8. Coefficient exodromy is stated for compactly generated presentable infinity-categories. A bare derivator provides `D(T)` as categorical coefficients but no automatically defined sheaf theory on an arbitrary topological site. Neither limitation is disguised as a theorem for arbitrary coefficients.
9. The Teichmüller groupoid of the open stratum is the open full subgroupoid of T. The whole EI category has noninvertible degenerations and cannot be identified with that groupoid. Its infinity-groupoid completion is the compactified moduli homotopy type; for four points that is S², not BF₂ (F.17). The comparison with Bakalov–Kirillov retains the mapping class group action on the marking complex: the equivariant path groupoid recovers the mapping class group, whereas the nonequivariant path groupoid is contractible. Remark 4.3 explicitly distinguishes marking moves from homeomorphisms. The composition of the equivariant path groupoid is given in F.17.

### Computations

`code/F_checks.py` enumerates stable split systems for four and five markings, checks all 81 order relations under forgetting 5, and obtains stratum fibre counts `{open:1, divisors:4}` over the open base and `{divisors:2, points:5}` over each boundary base. It checks the simplicial-circle homology used in F.3 and the exact integer exponent kernel of `(r,s) -> r+s` used in F.11. Its complete output is `code/F_checks.txt`.

`code/F_source_audit.py` reproduces the three local PDF text extractions performed while reading the sources and records the damaged HLS extraction. Its output is `code/F_source_audit.txt`.

`code/F_build_catalog.py` rebuilds the seventeen-row results register, verifies its statement identifiers and statuses against the TeX, and checks that its internal dependency graph is acyclic. Its output is `code/F_build_catalog.txt`. The final terminology audit records that `G/H` consists of left cosets `gH`, equivalently the quotient by the right `H`-action; this convention is explicit in F.2 and F.7.

### Literature searches and priority

Searches included `exit path infinity category moduli stable curves Charney Lee Jansen stratified homotopy type`; `moduli M0n aspherical configuration spaces Fadell Neuwirth theorem`; `"exit" "forgetful" "Charney" "proper"`; `"Charney-Lee" "forgetful" fibration`; `"exit" "proper functor" stratified`; `"curve complex" "forgetful map" "tree" Kent Leininger Schleimer`; `"Trees and mapping class groups" Kent Leininger Schleimer arxiv`; and `Grothendieck La Longue Marche Galois 26 topos modulaire M g nu manuscript`.

These searches found the complete ordinary-exit-category theorem and the tree theorem used for forgetting. No exact statement of properness in Grothendieck's category-theoretic sense for the specified Charney–Lee forgetful functor was located. F.10 records a proof of this consequence, with no priority or novelty claim. The explicit coset presentation in low dimensions is a calculation within the known transporter model, not a claim of a new exit-category theorem.

### Scope remaining outside the claims

All seventeen numbered Part F statements are settled within their stated hypotheses; none is labelled Open. This section does not establish a geometric sheaf realization for every abstract derivator, or for arbitrary presentable coefficients without a coefficient exodromy theorem. The former additionally requires a definition of geometric derivator-valued sheaves; Der 1–4 alone do not supply one. It also makes no blanket identification of an arbitrary strict categorical pullback with a geometric pullback. These are explicit limits of scope, not proved universal statements and not claims that the corresponding questions are open in the literature.

The section makes no profinite completion, arithmetic Galois-action, or Grothendieck–Teichmüller comparison claim. Those are the expressly separate LM3 task. The exact category and its chosen functors, including their strict model qualifications, are available in F.7–F.15 for that task to cite. Repeated forgetting is strict on the fixed surface models; relabelling is equipped with the natural isomorphisms arising from comparisons of chosen lifts, without assuming a splitting of the mapping-class extension.

## Reproduction and final artifact verification

The final paper has **54 pages**. Its SHA-256 is
`b6d7bfa2b7b4799dac5603cc75890d009090dacab6de96cb6e2c9d115cce6ef9`. The register contains **81 statements**,
with the status counts `{"Known": 14, "Open": 4, "Proved": 54, "Refuted": 9}`. Every numbered
statement has a location in the compiled PDF. All 24 PDF font
records are embedded. The final LuaLaTeX log contains no compilation errors,
unresolved references or citations, missing characters, overfull boxes or
underfull boxes. Every page was rendered and visually inspected; the exact
hash, page coverage and observations are recorded in
`code/pdf_qa_output.json` and `code/visual_qa_output.json`.

From the extracted `STRATA` directory, the mathematical finite checks are:

```sh
python3 code/AB_checks.py
python3 code/CD_checks.py
python3 code/E_finite_checks.py
python3 code/F_checks.py
python3 code/G_checks.py
```

Python 3 and SymPy supply the exact finite-category, chain-complex and
integer-matrix calculations. The PDF inspection additionally uses Pillow,
pypdf, and the Poppler commands `pdftoppm` and `pdffonts`. All captured
outputs are included. `00_sources.py` and `F_source_audit.py` audit the
separately supplied background, so they require the original attachments;
the mathematical verification programs above do not. Their source paths
and assumptions are explicit in the scripts.

The paper uses standard LuaLaTeX packages, including `fontspec`, the Latin
Modern fonts, the AMS packages, `mathrsfs`, `microtype`, `needspace`,
`hyperref`, and `apacite`. On a complete TeX installation, rebuild the
paper, APA references and paginated CSV with:

```sh
python3 code/build.py
python3 code/pdf_qa.py
```

`build.py` runs the actual LuaLaTeX engine, BibTeX, and two further
LuaLaTeX passes. `code/E_texenv.py` records the workspace repair used
for the minimal environment of this audit; `--local-tex` is an optional
build mode for that repaired environment, not a requirement for a normal
TeX installation. It downloads TeX runtime support, not mathematical
proofs. The separate temporary runtime and rendered inspection images
are not part of the deliverable.

`code/assemble.py` regenerates the bibliography and result register from
the authored section and audit inputs. The scripts `CD_metadata.py`,
`E_make_register.py` and `F_build_catalog.py` retain the corresponding
section metadata sources. `finish_report.py` combines the authored audit
reports and verifies the final inspection record. `package.py` performs
the final consistency checks, writes a file-hash manifest and creates
the single deliverable ZIP. A newly rebuilt PDF should be rendered and
inspected again before regenerating a final visual-inspection record;
the recorded observations concern the exact hash above.

