# Les Dérivateurs, Chapter XIII, part b: audit report

**Commentary and audit: GPT-6 Astra (OpenAI, ChatGPT Pro mode).**  
**Date:** 10 November 2026.

This report describes the work in this package. It does not attribute the commentary to a person or certify any later assembly or editing by Claude or another system.

## 1. Scope and method

The authority for the transcription is the supplied 36-leaf PDF, the electronic edition of 25 January 2004 transcribed and edited by M. Künzer, J. Malgoire, and G. Maltsiniotis. The extract contains the end of manuscript page 50, manuscript pages 51–98, and the edition's indices, axiom list, glossary, and bibliography. Page 78 is marked cancelled. The extract's printed pages are 29–64. The prompt's chapter-file leaves 31–66 count the two preliminary leaves of the full chapter. These are three different numbering systems.

Every supplied PDF leaf was rendered with Poppler and visually inspected; the 1,351-line uploaded TeX transcription was compared with it. Higher resolution crops resolved the relevant star/asterisk, footnote punctuation, and superscript questions. The diagrams on manuscript pages 62–64, 67–70, and 91 were compared arrow by arrow. Text extraction assisted navigation but did not decide ambiguous readings. The authority is the supplied electronic edition, not an independently inspected handwritten manuscript. A retained printed problem is therefore called `edition_slip_kept` without deciding whether it originated with Grothendieck or the editors.

The mathematical audit treats all assertions in §§5–7, the opening overlap, and the appendix definitions and axioms. The notation and terminology indices were checked as finding aids. Their references to earlier manuscript pages outside this extract were not certified against unseen pages. The attached `index_earlier.md` contains packages only through Chapter VII; it supplies no commentary for the immediately preceding part of Chapter XIII. No unavailable earlier commentary was reconstructed or treated as checked. Invocations of the earlier §§3–4 of this chapter are identified as such in the claims register.

The complete transcription is covered by the attached PDF, including the apparatus. No missing source page had to be supplied from a different edition. The official complete chapter and edition landing page were consulted for bibliographic and chronological checks.

## 2. Deliverables and editorial policy

The package contains all six files required by `FORMAT.md`, the generated reader TeX and PDF, the corrected transcription, the supplied builder, the documented reader style, and reproduction code.

| Required file | Content |
|---|---|
| `DER_XIII-b_blocks.tex` | 32 anchored English commentary blocks, using all six permitted kinds |
| `DER_XIII-b_overview.tex` | Standalone account of the argument, later developments, counterexamples, and remaining qualifications |
| `DER_XIII-b_claims.csv` | 197 entries: 90 for §§5–6, 70 for §7, and 37 for the appendix |
| `DER_XIII-b_corrections.csv` | 42 entries: 5 transcription repairs, 36 retained printed slips or discrepancies, and 1 resolved doubt |
| `DER_XIII-b_references.bib` | 20 references, with cumulative keys reused and verification scopes stated |
| `DER_XIII-b_report.md` | This report |

The audit's `proof_status` field follows the supplied specification: it records the source's treatment. A historical question may therefore be `open` in that column while its `repair` and `notes` give a later theorem or a proof in this commentary. Conversely, `false` identifies the assertion or inference as actually written, even if the intended conclusion has a correct proof elsewhere. This convention is essential to interpreting the register.

No mathematical source slip has been silently corrected in the French text. Five transcription rows repair footnote encoding: numeric manuscript notes 28–45, explicit note numbers 43–45, and a separate symbolic counter for glossary notes. The sixth exact patch resolves the doubtful comment without changing the diagram geometry. Loading English as well as French in Babel is a documented presentation adjustment. The original transcription and exact patch list are supplied for comparison.

All eighteen supplied `[sic]` markers were checked and retained as printed. The sole `% ??` concerns the interrupted vertical sides of the lifting diagram on manuscript page 63. The PDF confirms the proposed reading: these are the component arrows from A₀ to X₀ and A₂ to X₂, partly obscured by displaced B labels. The register resolves the doubt and the commentary explains the three lifting problems.

## 3. Quillen structures and derived images

### Closedness and exactness settle admissibility

The terminology is not normalized by fiat. A “category of models” at the start of this text has finite limits and colimits and a two-out-of-three class; weak Quillen structures, closedness, exactness, and properness are additional conditions. The definition of quillenisability in §5 does not include closedness.

For the uniform closed exact structures of §6, however, the retract argument proves TC = C ∩ W and TF = F ∩ W. The commentary gives the graph-factorization proof of the dual Ken Brown lemma with its actual hypotheses. Restriction preserves the objectwise cofibrations and trivial cofibrations, so its ordinary right adjoint preserves trivial fibrations and therefore weak equivalences between fibrant diagrams. Every existing ordinary right Kan extension is admissible under these uniform hypotheses. This answers the product, tower, group, and truncated-simplex questions within their stated scope. It requires no accessibility theorem and does not create a missing ordinary limit (Hovey, 1999, Lemmas 1.1.9 and 1.1.12).

The pointwise homotopy formula needs an additional compatibility: restriction to the comma category must preserve the chosen fibrant diagrams. The commentary proves this using the fiberwise-coproduct left adjoint for a discrete fibration, with the necessary coproducts stated. Finite-poset fibers have at most one element, so the source's finite hypotheses suffice there. The derived-adjunction block supplies both inverse Hom comparisons, including the type-corrected intermediate map. Base change along a discrete fibration is proved by an explicit isomorphism of comma categories. The two endpoint inclusions into [1] give a counterexample to unrestricted pullback base change: the pullback is empty, while the two derived values are k[0] and zero.

### The finite gluing proof is valid

The two-open-cover induction and the three lifting problems for the pullback shape are sound. The matching-object calculation explains why an arbitrary finite poset needs more than fibrancy of individual vertices and edges. A diamond of complexes with a nonsurjective diagonal matching map gives an explicit example. A separate cone calculation computes a homotopy pullback, verifies its differential and contraction, and proves invariance under componentwise quasi-isomorphisms.

The noetherian induction is also valid, but its claimed enlargement is vacuous for posets: a noetherian sober Alexandrov space is finite. The commentary proves this using the order-theoretic sobriety criterion and quasi-compactness of open subsets. This corrects the scope of the proposed generalization, not the proof of admissibility.

### Bounded and unbounded complexes

For infinite shapes, a diagram of bounded-below complexes need not have one bound valid at every object. The commentary proves that the product of the shifted fields k[n], n ≥ 0, cannot exist in D⁺(k), by testing its proposed universal property on the shifts themselves. A filtered system of finite partial sums verifies the footnote warning about filtered-colimit closure. These examples identify the missing justification in the all-diagram bounded claim without falsely claiming to disprove quillenisability itself.

For Grothendieck abelian coefficients, K-injective resolutions answer the unbounded right-image question. The Hom-complex adjunction shows that an exact restriction functor's right adjoint preserves K-injectivity. Beke's injective model structure on unbounded complexes and the combinatorial diagram-model theorem give both homotopy Kan extensions on all small shapes (Beke, 2000, Proposition 3.13; Groth, 2013, Theorem 1.28 and Proposition 1.30). No enough-projectives assumption is imposed on this result. The 2023 algebraic derivator treatment cited in the overview is separately identified as assuming enough projectives.

The historical context is specific. Joyal's letter begun on 11 April 1984 discusses Heller's diagram structures and states an unbounded Grothendieck-category model theorem in its continuation. Spaltenstein's resolution results appeared in 1988, before the manuscript. The commentary distinguishes the source's broad, unstable “triangulated” language from a Verdier triangulation: stability and strength supply the later triangulated structure. Cisinski's locally constant diagram theorem is cited in its proved model-category scope.

Worked examples include an acyclic inverse system whose ordinary inverse limit has H² = Zₚ/Z, and the periodic resolution for the trivial module over k[Cₚ] in characteristic p. The latter calculates all relevant Ext and Tor groups and shows that unbounded operations can exist while failing to preserve boundedness. The full simplex subcategory on [0] and [1] is distinguished from the walking arrow: its two objects and seven morphisms make its ordinary limit a finite-limit operation.

## 4. Cardinal filtrations

### Cardinal bookkeeping and valid constructions

“Grand devant π” means π⁺-directed in the modern regular-cardinal convention. An SGA π-accessible object corresponds to π⁺-presentability. Membership in a filtration stage is not automatically this Hom-preservation property. The commentary separates them and identifies each use of presentability.

The unrestricted assertion that GCH gives (π′)^π = π′ for every π′ > π is false at singular π′ with cofinality at most π. König's diagonal argument supplies the obstruction. The corrected GCH statement needs π < cf(π′), while the displayed power-of-two choice works without GCH. The original enlargement lemma is immediate under its stated directedness hypothesis; its transfinite proof establishes the useful weaker-ambient variant isolated by the editors. Both arguments and their cardinal bounds are supplied.

The adapted-presentation constructions are proved by cocone calculations. The bounded meaning of strict filtration comes from manuscript footnote 41. The glossary omits this bound. Its literal unrestricted closure, combined with the presentation axiom, would force every stage to equal the entire category.

### The same-rank three-way conjecture is false

Two complete counterexamples use E = P(ω₁), ordered by inclusion, with the ordinary cardinality filtration and π = ℵ₀. All filtration axioms, including the bound on presentation indices, are checked. Objects in the π-stage have the required π⁺-presentability. A product with Set gives a large ambient-category variant, also checked.

First, take M to consist of countable successor initial segments together with ω₁. It satisfies aπ: these are exactly the countably directed unions from its countable part. The continuous diagram of nonzero countable limit initial segments is perfectly adapted, has colimit ω₁, and has no M-stage. Thus aπ does not imply bπ. This example also satisfies cπ.

Second, take M to consist of finite subsets together with ω₁. It is strictly generated by its finite part, its relevant canonical slices are ordinarily filtered, and it is closed under countably directed unions. Thus cπ holds. A countably directed family of finite subsets has finite union: otherwise countably many chosen elements and one upper bound for their finite carriers contradict finiteness. Consequently ω₁ is not generated by such a family, and aπ fails. Ordinary filteredness cannot replace the stronger directedness in aπ.

These are marked commentator developments. Targeted literature checks did not locate these exact examples in the inspected sources; no priority claim is made.

### Canonical slices and a corrected size bound

Under the presentability hypothesis explicitly assumed in Lemma 2, the canonical slice of small M-objects over X is π⁺-filtered and has canonical colimit X. The proof factors maps through the presentation and equalizes at most π compatibility equations at a later stage. This resolves the editorial concern on manuscript page 92 under that hypothesis. A flattening argument then proves the required colimit closure.

The unqualified closure assertion called Lemma 1 is not established by that conditional proof. The audit records this limit without declaring the assertion false or claiming it is an open problem in the current literature.

The bound on the image category on manuscript page 93 is insufficient. The filtered category of injections of standard finite sets into an uncountable set has a countable image category but that uncountable set as its colimit. The repair bounds indexing morphisms and uses small non-full filtered subcategories; the closure and cardinality arguments are included.

Grothendieck's eventual proof of bπ ⇒ aπ on manuscript pages 96–97 is valid without presentability. His earlier immediate application of bπ to an arbitrary presentation is invalid and is explicitly retracted in footnote 42. The audit attributes that repair to the source.

### Conditional completion at the successor rank

The final Lemma 3 stops before a complete statement and is left as a fragment. A separate development theorem proves aπ ⇒ bπ⁺ under a strict filtration, repleteness of M, π⁺-presentability of every object of Filt^π(E), and π⁺⁺-presentability of every object of Filt^(π⁺)(E).

The proof reblocks an M-presentation using small π⁺-directed subposets, then compares it with an arbitrary perfectly adapted successor-rank presentation by an alternating ladder of length π⁺. Factorization, eventual equality, colimit maps, and both inverse equations are explicit. Both presentability levels are used; CH is not assumed. Independent review checked the equations and both uses of presentability.

The literature comparison covers SGA 4 I §9, selected Chapter XVIII developments, Lurie's cofinal-poset and rank-enlargement results, and smooth-filtration comparison in Lieberman, Rosický, and Vasey. Smooth-filtration club agreement does not apply to the discontinuous successor presentation in the first counterexample. Chapter XVIII's accessible-inclusion and canonical-slice criteria do not assert this fragment's universal-presentation condition bπ. The completed theorem follows the manuscript's idea without claiming to reproduce missing text or establish priority.

## 5. Literature verification

Every bibliography entry has a URL or DOI and an explicit verification note. Cumulative keys are reused. Publisher metadata is not presented as proof verification. The bibliography distinguishes author-version numbering from published pagination, including Raptis–Rosický Proposition 2.2 in author version 2 versus Proposition 2.3 in the journal.

| Source | Portions checked |
|---|---|
| Artin, Grothendieck, and Verdier (1972), SGA 4 I | 9.1–9.3, 9.12, 9.13.1, 9.14–9.18, 9.24; central proofs in 9.14 and 9.16; electronic edition dated 30 July 2024 |
| Grothendieck, Chapter XIII | All supplied pages and apparatus; official edition metadata |
| Grothendieck, Chapter XVIII | Selected §4.13 definitions and results; Lemma 4.16.7.11 with proof, ms. 488–490; edition dated 17 December 2025 |
| Grothendieck's Thomason letter (1991) | Opening discussion and §§1–2, electronic pp. 2–6 |
| Joyal's letter (1984) | Diagram structures and derived images on p. 3; Theorem 2 on p. 10; editorial chronology |
| Hovey (1999) | Retract, Brown, and derived-adjunction lemmas and proofs; products, small object argument, and Reedy structure in the 213-page author PDF |
| Groth (2013) | Definition 1.12; Theorem 1.28; Lemmas 1.29 and 1.31; Proposition 1.30 and proof; stable derivator theorem statements |
| Cisinski (2009) | Definitions 1.1–1.2; Theorem 1.3; Corollary 3.11; Theorem 3.13; not the entire proof |
| Spaltenstein (1988) | Definitions and Theorems C and D; Theorem 4.5; Proposition 6.7 in the original article |
| Serpé (2003) | Metadata and abstract; existence theorem independently checked through Stacks and Beke |
| Stacks Project, Tag 079P | Statement and transfinite-construction proof of the general K-injective theorem |
| Beke (2000) | Theorem 1.7; Propositions 3.10 and 3.13, including the latter proof; Corollary 3.14 in the author version |
| Lurie (2009) | Proposition 5.3.1.18 and proof; Proposition 5.4.2.2 proof; Lemma 5.4.2.8; Proposition 5.4.2.9; Remark 5.4.2.10 |
| Lieberman, Rosický, and Vasey (2020) | Author version 3, definitions and §8, especially Lemma 8.4 and club agreement, through Theorem 8.8 |
| Raptis and Rosický (2015) | Author-version Proposition 2.2 and pseudopullback argument; Theorem 4.2 statement; Corollary 5.1 proof; published numbering |
| Adámek and Rosický (1994) | Metadata and publisher Chapter 2 summary stating Definition 2.1 and Theorem 2.26; full book proofs unavailable |
| Makkai and Paré (1989) | Metadata and publisher description; historical orientation only |
| Quillen (1967) | Publisher metadata; the source's precise p. I.2 reference was not independently inspected |
| Lindenhovius (2014) | Version 2, Definition B.1 and Proposition B.5 with proof; order convention reversed explicitly |
| Alonso Tarrío, Álvarez Díaz, and Jeremías López (2023) | Version 3, standing hypothesis 1.1, §§2.6–2.10, Theorem 3.4; publication metadata |

These checks do not claim that each cited book or article was read in full. Targeted searches for accessible subcategories, club comparison, continuous filtrations, perfectly adapted presentations, and cardinal filtrations supplied the modern comparisons. Failure to locate an exact formulation is not evidence that it is absent from all literature. Full bibliographic data, links, and version-specific notes are in the BibTeX file and reader bibliography.

## 6. Retained discrepancies and limits

The retained mathematical source slips include the colimit symbol in a finite-limit argument (ms. 59), the mis-typed Hom target (70), two reversals of left and right adjoint (71), TF = F ∩ C (74), the factor named f instead of p (75), the GCH assertion (77), an inverse-limit sign in an inductive construction (85), the indexing-functor label (91), “values in X” instead of E (92), a target C instead of I (93), and the unprimed bπ after cardinal enlargement (97). Orthographic issues are distinguished in their evidence and assigned no mathematical significance.

The glossary's strict-filtration omission and its use of “well adapted” for a perfectly adapted representation are recorded independently. Repeated definitions are not duplicated unnecessarily in the main register. The edition's bibliography includes Verdier's 1996 publication; this is editorial apparatus, not evidence of a future publication cited by the 1990–1991 manuscript.

The final fragment is not completed by conjectural transcription. Quillenisability without closedness, the unqualified closure lemma without presentability, and antecedent results outside the supplied pages are not promoted to proved theorems. Exact current conclusions and their qualifications appear at the relevant anchors and in the register.

## 7. Construction and reproducibility

The supplied `build_reader.py` is unchanged. It validates schemas, enumerations, unique identifiers, block kinds, unique anchors, citation keys, and placement of `\ours`. The assembly helper merges audited components and sorts blocks by their actual insertion paragraph; it does not alter the French body. The final fragment uses an exact-word anchor because a bare page-98 anchor would include the following editorial apparatus.

Documented style adjustments provide A4 geometry, room for source margin labels, English inside commentary, compact manuscript-page labels, PDF bookmarks, and a title page with the required credit. Microtypography improves line breaking. Commentary headings reserve space for their opening text; index entries use compact paragraph gaps; explicit glossary bullet headings stay with their explanations. Proper names and Roman chapter numerals are protected from BibTeX case conversion. The overview and complete bibliography follow the interleaved text, as in the supplied builder. The original style and the adjustment script are included. `FORMAT.md` is unchanged.

The environment's LuaHBTeX executable was present, but format/database paths were broken and runtime packages were missing. A workspace-local repair installed genuine CTAN packages, generated the LuaLaTeX format, loaded language data, and built a font map. No engine was substituted and no package was stubbed. The bootstrap script, dependency archives, SHA-256 manifest, and wrapper are supplied. A complete ordinary TeX Live installation needs only the standard build commands.

The build sequence is the supplied Python builder, one LuaLaTeX pass, BibTeX, and two further LuaLaTeX passes. Both the corrected transcription and the full interleaved reader were compiled with genuine LuaLaTeX. The accompanying build-verification file records final logs, page counts, machine checks, and visual inspection. Compilation errors and unresolved citations were resolved before delivery.

A useful future format extension would separate `source_status` from `current_status`, and distinguish author slips from editorial slips when handwritten evidence is available. This package follows the existing schema and does not invent that evidence.

## 8. Page correspondence

**Attached PDF leaf + 28 = printed page. Attached PDF leaf + 30 = full chapter PDF leaf.** Manuscript markers are independent.

| Attached leaf | Printed page | Manuscript span or apparatus |
|---:|---:|---|
| 1 | 29 | End of 50; 51; beginning of 52 |
| 2 | 30 | 52–54 |
| 3 | 31 | 54–56 |
| 4 | 32 | 56–57 |
| 5 | 33 | 58–60 |
| 6 | 34 | 60–62 |
| 7 | 35 | 62–63 |
| 8 | 36 | 64–65 |
| 9 | 37 | 65–67 |
| 10 | 38 | 68–69 |
| 11 | 39 | 69–71 |
| 12 | 40 | 72–73 |
| 13 | 41 | 74–75 |
| 14 | 42 | 76–77 |
| 15 | 43 | Cancelled-page-78 marker; 79–80 |
| 16 | 44 | 80–81 |
| 17 | 45 | 82–83 |
| 18 | 46 | 84–85 |
| 19 | 47 | 86–88 |
| 20 | 48 | 88–90 |
| 21 | 49 | 91–92 |
| 22 | 50 | 93–94 |
| 23 | 51 | 95–96 |
| 24 | 52 | 97–98; final fragment |
| 25–26 | 53–54 | Notation index |
| 27–28 | 55–56 | Terminological index |
| 29 | 57 | Axiom list |
| 30 | 58 | Glossary §§1–2 |
| 31 | 59 | Glossary §2, diagrams |
| 32 | 60 | Glossary §§2–3 |
| 33 | 61 | Glossary §§3, 5, 6 |
| 34 | 62 | Glossary §§6–7 |
| 35 | 63 | Glossary §7, conclusion |
| 36 | 64 | Edition's bibliography |
