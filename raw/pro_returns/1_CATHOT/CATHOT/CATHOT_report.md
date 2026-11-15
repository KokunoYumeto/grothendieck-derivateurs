# CATHOT research and audit report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. Original arguments and computational work in this package are not attributed to any person. Named authors are credited only for the primary literature that is actually cited.

## Scope and proof status

The paper addresses Parts A–G in the requested order. A result marked **Proved** has an argument in the paper; **Refuted** identifies an assertion for which an actual counterexample is supplied; **Known** identifies an imported theorem with an exact inspected source, sometimes followed by a proof of its application; **Open** identifies a statement that this audit has not settled. “Open” does not assert that the literature has no answer. The status of the statement, rather than the tone of its title, governs its interpretation. A Refuted statement may be phrased as “the proposed assertion is false” so that its complete quantified scope remains explicit.

The CSV contains the complete text of every numbered assertion, in TeX notation with whitespace normalized, together with dependencies, source location, manuscript pages, and qualification notes. The bibliography records the version inspected and labels every entry verified or unverified. Reading a paper and checking a theorem's statement is distinguished from independently auditing every step of its proof. In particular, the finite alternating-group multiplier, the relevant rational cohomological dimension theorem, the recent finite-monoid realization theorem, and the published order-five/order-six semigroup classification are explicitly imported ingredients.

## Inputs and source handling

The attached `PROMPT(1).md`, `BACKGROUND(1).md`, and `MANIFEST(1).tsv` were read. The attached background archive was checked against SHA-256 `e91871632a2a856d47e993341ba56763c2bf1f8244a3c3442711ccb2a20a4c39` before extraction. The available Grothendieck text is the supplied AI transcription, not a fresh examination of manuscript images. Consequently a necessary correction to a formula is reported as a correction to the supplied transcription; we do not claim to decide whether the error originated with Grothendieck, the edition, or the transcription.

The relevant manuscript ranges were read using their manuscript-page markers: V ms. 11–13 and 37–52; VII ms. 108–136 and 150–156, with the defining relative path conventions at ms. 65–67 and the all-arrows conventions at 137–148; IX ms. 9–13 and 22–25; and the XII appendix examples named in the prompt. The companion's overview, block commentary, statement ledger, and bibliography in the corresponding III–V, VII-b, VII-c, VIII–X, and XIIapp packages were used as draft claims and search leads. They are not proof authorities. The pilot overview and addendum were consulted for the three proposed leads.

`code/prepare_sources.py` converted the supplied PDFs to searchable text, and its output lists the conversions. The source PDFs and supplied third-party text are not redistributed inside the deliverable archive. Our authored programs, outputs, statements, audit notes, and reference metadata are included. Repeating source-extraction or source-dependent diagnostics requires the supplied background archive, or the exact URLs identified by the fetching scripts and bibliography.

## Root source checks

Thomason (1980), the supplied complete paper *Cat as a closed model category*, was inspected at the model structure, the comparison with simplicial sets, and the cofibrant-poset assertion. The citation uses Theorem 4.9, Corollary 5.5, and Proposition 5.7. The argument does not rely on the false assertion that all Dwyer maps are closed under retracts.

Raptis (2010), *Homotopy theory of posets*, was opened both in the supplied PDF and at the independently retrieved primary PDF. Proposition 2.4 and the pseudo-Dwyer discussion, Theorem 2.6, Theorem 3.5, the product observation at the end of Section 3, Proposition 4.8, and Remark 4.9 were checked. These distinguish three different facts: poset fibrant replacement exists; bounded-source model structures make the bounded sources cofibrant; and the exact cosimplicial resolution for Thomason mapping spaces is `c Sd²(NX × Δ•)`. D.9 records the known model-category route to bounded representability, so D.1 is not presented as an uncited novelty claim.

May, Zakharevich, and Stephan (2017), *The homotopy theory of equivariant posets*, was inspected in the published version, especially Lemma 3.6 and Lemmas 4.7–4.8. The published author order and theorem numbering differ from the author preprint. The bibliography uses the published order; the internal citation key is only an identifier. The pushout description verifies that the free-equivariant horn construction in A.6 introduces no new fixed objects.

Quillen (1973), *Higher algebraic K-theory: I*, was inspected in the supplied proceedings scan at Section 1, Theorems A and B and their opposite formulations. Page numbering in that scan differs from standard journal/book pagination; the final paper therefore cites the section and named theorem, not a misleading scan page.

The original full text of Thomason's 1979 homotopy-colimit paper was not obtained. Its publisher page verified the bibliographic metadata. A complete primary proof of the needed theorem is available in Chachólski and Scherer's *Homotopy theory of diagrams*, arXiv:math/0110316v1, Theorem 26.8 and Corollary 26.9. That author-hosted PDF was opened and those statements and their proof linkage were inspected. The final mathematical uses cite the inspected source; the original Thomason entry is explicitly marked unverified full text.

Dwyer and Kan's *Calculating simplicial localizations* (1980) was opened in its complete primary PDF at the Rochester archive. Section 2, Proposition 2.2, and Proposition 3.1 give the hammock construction and its component category. Their *Function complexes in homotopical algebra* (1980) was opened at Proposition 4.4 and Corollary 4.7, with the resolution comparison in Sections 6–8. Failed attempts at the Oslo mirror are not counted as verification; the Rochester PDFs were successfully inspected.

Lurie's *Higher Topos Theory* was checked, in addition to the finite-generation passages reported in the Part F audit, at Proposition 4.2.4.4 and its surrounding discussion. Its chunk and combinatorial simplicial-model hypotheses are retained. The formula for external Hom in E.9 is conditional on the specified diagram-localization comparison; it is not asserted for an arbitrary small relative category.

The detailed B/C, F, G, and exact-path audit contributions below record the other primary papers opened, exact versions and theorem numbers, failed accesses, and the particular searches performed.

## Decisions on the three leads

**Lead 1 is correct.** There is no right adjoint at all to `Cat hot → Hot`, even without adding full faithfulness as a requirement. The explicit `K(Z/2,2)` obstruction uses the finitary alternating group at a cardinal strictly above the arrow set of the proposed representing category, within the same universe. The passage from finite alternating-group multipliers to the infinite group checks the actual transition maps. Evaluation of `Fun(BG,K)` is an isomorphism of categories, not merely a bijection on objects or connected components. Noninvertible endomorphisms and idempotents in K do not escape the argument, since a group homomorphism into a monoid lands in its units.

The sharper obstruction is proved for every homotopy type that is not a 1-type. Finitary alternating groups alone are not asserted to have the required maps to every target. The alternative acyclic/simple-envelope and amalgamated-double construction produces groups of arbitrarily large prescribed cardinality with the required small-quotient obstruction and a homology equivalence to an arbitrary sphere Sⁿ, n≥2. Postnikov mapping-space comparison into the simply connected universal cover retains essential higher classes, including for disconnected targets and nontrivial fundamental-group actions.

**Lead 2 is correct.** Local categories are exactly categories isomorphic in `Cat hot` to groupoids, and the represented types are exactly 1-types. The canonical unit to fundamental groupoidification is the relevant isomorphism. A nerve having 1-type, or even contractible, is not alone sufficient. The local subcategory is reflective through Π₁, but not coreflective. Its reflector inverts 1-equivalences, a different class from W∞; it does not restore the proposed reflection onto all homotopy types.

**Lead 3 needs its finiteness convention fixed.** The infinity-category of spaces is the Ind-completion of finite CW homotopy types; its compact objects are retracts of such types. A finite category may have a noncompact nerve, so the given inclusion of all finite-category homotopy types is not an Ind presentation. Space-valued restricted Yoneda on that larger full test category is nevertheless fully faithful because it contains the finite CW types. Set-valued testing loses fullness, faithfulness, and conservativity. Coherent height-two tests recover conservativity, but no finite height recovers ordinary fullness or faithfulness for unrestricted sources. For countable CW sources, coherent height-two finite CW tests do recover ordinary map classes. These are separately proved assertions, not different uses of an undefined word “faithful.”

## Corrections to the companion and the manuscript's deductions

The companion's “unproved reflection must remain a hypothesis” is strengthened to a refutation. Its conditional formal propositions remain valid, with typed ind-Hom formulas and explicit use of the unit on ind-objects. One-way descent of an already ind-represented invariant functor is formal and needs no adjoint (A.7). The converse global representability statement is false for every non-1-type.

The companion's “finitely many objects already give a uniform stage” is valid for full inclusions. It does not make a general finite category topologically compact, does not justify replacing derived maps by strict functors, and does not turn a union of local categories into a local category. E.4 supplies finite full stages which are both local and Thomason-fibrant, with a fibrant union, and a shift equal to the identity as an ind-morphism but not even a weak equivalence on the union. Its union is explicitly nonlocal. The genuinely stronger hypothesis that both unions themselves are local must be kept separate, and is treated separately in E.18.

The finite fence counterexample in E.5 refutes strict retraction under localness. It does not have a fibrant retract target and is not used to refute the additional fibrancy variant. For a fibrant target, an actual strict retraction exists in the same ordinary localized homotopy class by the direct path-object lifting argument recorded in E.6. The remaining issue is whether it can be kept in the original `Cat hot` class. This distinction prevents changing the meaning of “Thomason category” in mid-proof.

The two fibrant-target shortcuts in VII ms. 136 are independently false. A fibrant poset model of BC₂ already refutes the unreplaced-source component formula. A separate equivariant horn attachment and semidirect-product construction refutes fibrancy of the functor category. These are different assertions with different counterexamples. A.5 uses the exact model cylinder, rather than silently replacing model homotopy by finite natural-transformation zigzags.

At VII ms. 135 the *absolute* arrow-category map `B Fun([1],C) → Map(B[1],BC)` is always a weak equivalence. Evaluation at the source proves this directly. Its strict endpoint fibre need not be a homotopy fibre: in the terminal fork the arrow set from one outer vertex to the other is empty, but the derived path space is nonempty and contractible. The correction is to that fibre inference, not to the absolute comparison.

The set-valued arguments for associativity, path transport, and T² do not prove the corresponding statements in Hot. The specified canonical all-arrows alternating path model is compared directly with derived endpoint fibres and ordinary path spaces in E.20–E.24; the comparison also checks the actual gluing operation. These positive conclusions do not silently certify every arbitrary relative class, every block, or every cofinal system of path types. The scope audit and precise remaining assertions are included with the path supplement.

The symbol ψ at IX ms. 9 means restricted Yoneda, whereas at V ms. 37 it means the proposed right adjoint. The first exists and fails the proposed detection properties; the second does not exist. Product-preserving forward passage and passage to component categories remain valid. The assertion that only essentially constant ind-objects can have a colimit in Hot is false: the increasing finite discrete sets have the discrete countable set as their ordinary categorical colimit in Hot.

At IX ms. 23 the stated tests alone permit a nontrivial finite pointed relative category: pointed sets with one or two elements, with only identities inverted. This is a five-arrow category. If finite products are additionally required, a finite pointed category is equivalent to a point; the counting proof is given. At IX ms. 24–25 the first arrow in a path-object factorization must be a weak equivalence. A cofibration alone is not enough to compute loops.

The companion's symmetric-group and telescope counterexamples are retained with explicit checks. The telescope remains invisible to finite-category tests for a reason stronger than finite CW compactness: their fundamental groups are finitely generated, so every map to K(Z[1/2],1) factors through a cyclic subgroup. The finite-category sphere examples in XIIapp are upper bounds, not minima. Five- and seven-element monoids improve the S² and S³ bounds. The latter is a six-element *semigroup* with a separate identity adjoined, and hence a seven-arrow monoid.

## Corrections to the supplied transcription

These corrections are mathematical type checks, not claims to have re-read original images. Several are already marked `[sic]` or “plutôt” in the supplied transcription; they are retained rather than silently inherited.

| Location | Supplied formula or wording | Typed correction |
|---|---|---|
| V ms. 38 | `Hom_C(φX,K′)` in the adjunction triangle | The subscript is C′, since both arguments are objects of C′. |
| V ms. 38 | Repeated implication `(i) ⇒ (i)` | The intended implication in that chain is `(i) ⇒ (i′)`. |
| V ms. 39 | The sentence repeats `φ(i)` where both factors are needed | The second factor is `φ(p)`; the concluding label is `(ii′)`. |
| V ms. 40 | `H′: C^op → Set` | The domain is `(C′)^op`. |
| V ms. 40 | Both ind-functor arrows point toward Ind C′ | `Ind ψ` has source Ind C′ and target Ind C. |
| V ms. 41 | `Hom_C(X,K)` and `Hom_C′(φX,φK)` with K an ind-object | These are Hom-sets in Ind C and Ind C′, with constant objects embedded. |
| V ms. 42 | A missing implication between `(i″)` and `(ii′)` | Insert the implication and extend the presheaf to ind-objects by a limit. |
| V ms. 45 | Constant-diagram Hom uses `(a_X,b_Y)` | The second diagram is `b_X`. |
| VII ms. 120–123 | An asserted isomorphism in Hot follows only from the restricted finite-test argument | Without a separate comparison proof, only the restricted presheaf isomorphism is established; the subscript/restriction cannot be discarded. |
| VII ms. 155 | An even/odd endpoint convention in the text is inconsistent with the displayed fence | The endpoint direction must be read from the actual generating arrows; E.21 states both parity cases explicitly. We do not infer which original textual layer introduced the mismatch. |
| IX ms. 23 | “Empty” can be read where the categorical conclusion requires the trivial pointed category | A pointed category has a zero object and cannot be empty. The relevant conclusion is equivalence to the terminal category, and needs the extra product hypothesis. |

## Computations and their logical limits

`a_finite_checks.py` verifies the crown and terminal fork, including all typed compositions and the stated nerve homology. `e_full_filtration.py` verifies the full-filtration formulas through stage three, all composition equations, the shift functor, and all three stagewise natural transformations. The stages have respectively 1, 5, 23, and 119 arrows. These finite checks support but do not replace the uniform proof.

`e_retraction_and_pointed.py` checks the nine-object fence and twelve-object circular fence, the eight-step contraction, all 729 candidate retractions, and the five-arrow pointed category with its identity and associativity equations. No strict retraction is found, in agreement with the independent distance proof. The exact half-fence collar checks and the B/C, F, and G computations are documented in the appended contributions.

The diagnostic `f_sweeney_cup.py` computes exact rational cochain ranks and a cup square for a six-element monoid with homology in infinitely many degrees. It does not identify the full homotopy type and does not settle the cardinality of its map set to S². The order-five/order-six monoid lower bound in G is imported from the identified Sweeney classification, not represented as a locally repeated exhaustive computation.

`editorial_updates.py` records idempotent final source clarifications. `assemble.py` merges the current bibliography and statement metadata and produces this report. `build.py` runs LuaLaTeX, BibTeX, and the final LuaLaTeX passes; its output and the final log are included. `validate_package.py` checks statement/ledger agreement, citation keys, proof-status vocabulary, compilation diagnostics, archive members, and file hashes. These structural checks are not advertised as mechanical verification of the mathematics.

The final paper has 63 A4 pages. All four compilation commands succeeded. The final LuaLaTeX log contains no warnings, overfull or underfull boxes, missing characters, or unresolved citations or references. `render_pdf_qa.py` rendered every page at 90 dpi, generated eight contact sheets, and checked text bounds. Every page was visually inspected in contact sheets; the title, conventions, contents, first assertion, dense crosswalk, finite-test and minimum-size tables, and bibliography were also reviewed individually. Review records are retained in `research/pdf_visual_review_part1.md` and `research/pdf_visual_review_part2.md`.

`f_final_consistency.py` provides a separate read-only cross-check of the assertion register, citation keys, source inputs, and narrative scope. `package.py` selects the deliverables, excludes complete third-party sources and runtime caches, and creates an archive with a SHA-256 content manifest. The final register records 90 assertions and the six Open identifiers listed below.

## Remaining exact questions

The numbered Open assertions in the final paper and CSV are the authoritative list. In particular, they retain the sequential S² finite-test question, the extra-fibrancy strict-retraction question with the *same Cat hot class*, the W∞-invariant small-ind versus groupoid-stage issue, the exact general path-system comparisons not covered by the canonical construction, and the remaining finite-realization and RP²-poset arrow questions. Each states the proved range, the missing implication, attempted approaches, and the smallest unresolved scope reached in this audit. No unproved classification of all infinite-dimensional finite-category or finite-monoid types is claimed.

The finite CW realization statement for finite monoids uses the recent Ben-Bassat preprint as an explicitly cited Known input. Its sufficiency proof is not independently audited in full here. The necessity argument is independent and refutes that preprint's separate finite-fundamental-group conjecture using RP². The report distinguishes this from a claim that the simply connected realization theorem is false.

## Reproduction and deliverable boundaries

Run `python code/assemble.py` and `python code/build.py` from the extracted CATHOT directory with LuaLaTeX, BibTeX, the listed TeX packages, and Python available. The scripts resolve their data paths relative to their own locations. In the sparse authoring environment, the installed engine initially lacked its format, searchable TeX database configuration, Lua font libraries, and font map. `code/setup_lualatex.py` and `code/run_with_tex.py` repaired these in a separate workspace runtime without system writes or relaxed file-write restrictions. The successful build uses the real LuaHBTeX engine, not a substitute renderer. That environment-specific wrapper is optional on a normal TeX Live installation. Prior failure logs and the final successful four-pass build log are retained separately. Exact finite-model programs additionally use SymPy. The exhaustive scope, enumeration counts, and outputs are retained. Source extraction and source diagnostics identify their external inputs; the archive does not redistribute complete third-party papers. The complete final paper is the PDF plus its root TeX file, included section files, and bibliography. The report and machine-readable statement ledger are supplemental audit records.

The literature searches are bounded, documented searches rather than proof of absence from the literature. No priority assertion is made for a formulation not found in those searches.

## Final statement inventory

The assembled paper has 90 numbered statements: 59 Proved, 14 Refuted, 11 Known, 6 Open.

The exact Open statement identifiers are D.6, E.6, E.17, E.26, E.27, G.17.


---

## Parts B and C research and audit report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The section's 17 numbered statements are all recorded in `BC_results.csv`.

### Material inspected

Read the attached prompt, the pilot overview's envelope lead, and the V manuscript passages at ms.37--49 defining and invoking the right adjoint. The prior companion and leads were treated as claims to check, not authorities.

Primary sources opened and relevant passages inspected:

- Higman, Neumann, and Neumann (1949), *Embedding Theorems for Groups*, publisher PDF, Theorems I and II. Theorem II permits simultaneous conjugation of an arbitrary family of isomorphic subgroups while retaining the base group.
- Baumslag, Dyer, and Heller (1980), *The topology of discrete groups*, complete 47-page primary-source PDF at the University of Chicago archive. Inspected Proposition 4.1, Theorem 4.2, Corollary 4.5, Lemmas 5.1--5.4, and Theorem 5.5. The previously missing background paper was found freely available at `https://math.uchicago.edu/~shmuel/lg-readings/Baumslag-Dyer-Heller.pdf`. Theorem 5.5 explicitly states a same-cardinality acyclic embedding for infinite groups.
- Domínguez and Segovia, arXiv:2012.02464v2, *Extending free group action on surfaces*, equation (35), Proposition 20, and Corollary 21. These record the finite alternating-group multiplier and a compatible torus generator. The journal version is entitled *Extending free actions of finite groups on surfaces* (2022); its corresponding numbering is equation (34), Proposition 21, Corollary 22. The paper consistently cites the inspected arXiv numbering.
- Lawson, *An introduction to Bousfield localization*, author PDF dated March 11, 2019, Example 9.2 and Examples 9.5--9.6. Example 9.2 confirms that simply connected spaces are local with respect to integral homology equivalences; the section gives the complete Postnikov mapping-space argument needed here.
- Löh, *A note on bounded-cohomological dimension of discrete groups*, author PDF dated September 8, 2015, Corollary 1.3. This independently records same-cardinality mitotic embeddings. It was useful as a search lead but is not needed in the final proof.
- Palmer and Wu, *Embedding groups into acyclic groups*, arXiv:2510.16879v1, introduction. This supplied current bibliographic cross-checks for Kan--Thurston and BDH; none of its stronger finite-generation theorems is used.

Schur's 1911 article bibliographic record was opened, but its original full text could not be accessed through the available reader. Its bibliography entry is explicitly marked **unverified**. No proof depends on an uninspected theorem number in it. The finite multiplier calculation is instead an explicitly identified **Known** input verified in the Domínguez--Segovia primary research paper. Its upper-bound proof is not independently reproduced; the infinite-cardinal calculation and all required transition maps are proved in full from that finite input.

### Search record and claims of novelty

Searches included `finitary alternating group Schur multiplier infinite set Z/2`, `simple groups prescribed homology`, `simple Kan-Thurston groups homology`, `every group simple group same cardinality`, `acyclic simple every group embed`, `mitotic acyclic Baumslag Dyer Heller`, `Schur multipliers alternating groups n 8 theorem proof pdf`, and `homology equivalence simply connected mapping spaces integral`. Searches about categorical homotopy, natural transformations, local objects, and 1-types did not locate the precise full classification stated here. This is not a novelty claim; the argument is assembled from standard group embeddings, amalgams, Postnikov towers, and the nerve of a groupoid.

The alternating-union construction of a simple acyclic envelope was also encountered in a MathOverflow discussion of arbitrarily large acyclic simple groups. That forum was used only as a search lead and cross-check. The paper proves the observation, the cardinal bounds, and all subsequent consequences independently from the verified primary ingredients.

### Corrections and settled leads

Lead 1 is correct. The cardinal argument must remain within the fixed universe, and the infinite homology calculation requires checking the maps in the directed system, not just the abstract finite Schur multipliers. The section does both. Evaluation `Fun(BG,K) -> K` is a strict category isomorphism under the small-quotient hypothesis, including categories with nontrivial endomorphisms and idempotents.

The argument is strengthened to **every non-1-type**, including arbitrary disconnected types and arbitrary actions of a nontrivial fundamental group. Finitary alternating groups alone were not assumed to provide the required essential maps to spheres. Instead, for each infinite cardinal lambda, simple and acyclic embeddings are alternated to build an acyclic simple group of size lambda containing a prescribed group. Amalgamated doubles of such envelopes, iterated from Z, produce perfect groups G of size lambda with no nontrivial homomorphisms to any smaller group and homology equivalences `BG -> S^n` for every n >= 2. Mapping into simply connected universal covers turns nonzero higher homotopy elements into essential unpointed maps. The resulting groups G need not be simple; the exact small-quotient property requested in the prompt is proved.

Lead 2 is fully settled affirmatively: representable homotopy types are exactly 1-types, and local categories are exactly those isomorphic in Cat hot to groupoids. The canonical groupoidification unit is the relevant isomorphism. Having a 1-type nerve alone is not sufficient: the infinite fence has contractible nerve and is not local.

The local subcategory is reflective, with reflector Pi_1. It is **not coreflective**. The reflector inverts 1-equivalences, a larger class than W_infty, so this does not restore the nonexistent right adjoint to Cat hot -> Hot. The right adjoint asserted at V ms.37 is false, rather than merely unproved. Thomason fibrancy is also insufficient to imply localness; a Thomason fibrant replacement of a category of type S^2 is already a counterexample.

### Computations

`code/bc_checks.py` uses exact permutation operations, rational Clifford algebra, free-product normal forms, and finite graph distances. Its deterministic output is `code/bc_checks_output.json`.

It verifies the fresh-point commutator producing a 3-cycle; verifies that spin lifts of the two Klein-four generators square to -1 and anticommute; checks the simple-envelope word for all 1,360 choices of nonidentity g and arbitrary h in cyclic groups of orders 2 through 16; and verifies finite fence truncations with 3, 5, 9, 17, 33, and 65 objects, with endpoint distances 2, 4, 8, 16, 32, and 64. These finite checks supplement the general proofs and are not presented as proof of an infinite assertion or as a recomputation of the full finite Schur multiplier.

`code/bc_write_metadata.py` produces the 17-row results ledger; its output is retained in `code/bc_write_metadata_output.txt`.

### Remaining questions in Parts B and C

None of the requested classification or representability questions in Parts B and C remains open in this treatment. The proof uses the stated classical finite Schur-multiplier theorem as a Known ingredient. Whether some of the explicit large groups can additionally be required to be simple while retaining the exact sphere-plus type is neither needed nor asserted. The central classification proof does not depend on the alternating-group calculation at all; it also independently refutes the proposed right adjoint.

No transcription correction was needed for the mathematical formulas used from V; the correction is to the asserted adjoint itself.

---

## Part F: source audit, computations, and unresolved questions

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. This is a contribution to the CATHOT package, not a separate publication attributed to any person.

### Read sources

The attached prompt and the relevant companion blocks were read first. From `DER_III-V_blocks.tex` the blocks at V ms. 52 on the finite-support symmetric-group shift and the general obstruction were checked. From `DER_VII-c_blocks.tex` the blocks at ms. 121, 127, and 150 on finite tests, telescopes, and reversal were checked. From `DER_VIII-X_blocks.tex` the block “What the finite tests forget” and the ind-object discussion at IX ms. 9–13 were checked. These are treated as draft claims and are not cited as authorities for mathematics.

The supplied Arlin–Christensen LaTeX source was read in its introduction, Section 2 (including the complete regular-cardinal permutation argument), the statements and explanation of Section 3, and Section 4. The primary arXiv HTML was independently opened, confirming Theorem 2.1, Remark 2.3, and Theorem 4.3. The paper is *Detecting isomorphisms in the homotopy category*, Algebraic & Geometric Topology 23 (2023), 2975–2991, DOI 10.2140/agt.2023.23.2975. The theorem on no privileged transfinite weak colimits is not reproved in Part F, and the full graph-of-groups proof in Section 3 was not read line by line.

The supplied Arlin source was read in the relevant introductory definitions and results and Sections 5–6. Its arXiv HTML, version 4, was opened independently. Exact theorem numbers checked are 19 (strict/simplicial embedding), 29 (bicategorical embedding on all small diagram categories), 35 (spaces and finite diagram conservativity), and 37 (quasicategorical conservativity); the suggested non-fullness construction is explicitly Conjecture 34. This distinction is retained. The journal metadata was checked as Homology, Homotopy and Applications 22(1) (2020), 117–139, DOI 10.4310/HHA.2020.v22.n1.a8. The publisher PDF returned HTTP 403; the supplied source and the arXiv HTML were accessible.

The supplied Hatcher PDF was converted to text and the following passages opened: Theorem 2C.5 (finite CW to finite simplicial complex), Theorem 3.19 (projective-space cohomology), Examples 3F.7 and 3F.9 (inverse limits and the telescope), Theorem 4.57 (including its following paragraph on unpointed classes), and Appendix remarks relevant to finite domination. The author-hosted PDF was opened through web retrieval.

The supplied Lurie HTT PDF was converted to text. Proposition 5.3.3.3 (filtered colimits commute with finite limits), Proposition 5.3.5.11 (the precise Ind criterion), and Lemma 5.4.2.4 (idempotent completion and compact objects) were checked. The author-hosted PDF was independently opened. The supplied text is the April 9, 2017 revision of the book published in 2009.

The supplied Freyd PDF was read at the main theorem on reprint p. 1, the simply connected finite-dimensional refinement on p. 5, and the explanatory footnote on basepoints later in the paper. The TAC-hosted reprint was opened independently. The original 1970 print copy was not opened; citations in this package use the 2004 reprint pagination explicitly.

Nguyen–Raptis–Schrade, *Higher weak (co)limits, adjoint functor theorems, and higher Brown representability*, Documenta Mathematica 27 (2022), 1369–1420, was opened from the publisher. Theorem 4.2.11 and Corollary 4.3.2 were checked to ensure that they were not silently converted into a restricted-Yoneda fullness theorem. They concern representability under exactness assumptions on the full higher category.

Dicks–Kropholler–Leary–Thomas, *Classifying spaces for proper actions of locally finite groups*, Journal of Group Theory 5(4) (2002), 453–480, DOI 10.1515/jgth.2002.016, was opened at its primary arXiv PDF `https://arxiv.org/pdf/math/0111283`. Corollary 6.10(2), printed p.21 of arXiv version 1, establishes the rational cohomological dimension used in F.12 for torsion abelian groups. Theorem 5.4, printed pp.16–17, supplies the more explicit nonzero H²(G;QG) when |G|=aleph_1. The commentary on Conjecture 1.7 and the proof via Theorem 3.10 and Corollary 6.9 were inspected. The exact corollary is a proved abelian-group case, not an appeal to the broader Holt conjecture. The citation key is in `BC_references.bib` because the B/C reviewer supplied this independent extension of Part F.

Matumoto–Minami–Sugawara (1984) remains **unverified**: the Project Euclid landing link was inaccessible and the full-text landing page only yielded an iframe. Its Proposition 4.1 attribution is reported only as confirmed by Arlin–Christensen, Remark 2.3; no proof depends on an unread assertion of that paper.

### Literature searches

Search phrases included “Arlin Christensen Detecting isomorphisms homotopy category 4.3 2023”; “restricted Yoneda finite spaces homotopy n category phantom maps n-faithful Ind completion spaces finite CW”; “homotopy finite complexes full Yoneda”; “higher Brown representability homotopy n-categories”; “spaces restricted Yoneda faithful”; “homotopy 2-category phantom”; “finite complexes unbased natural transformation”; and “Adams representability spaces”. Search results from secondary discussions were used only as leads; mathematical citations are to opened primary sources or the verified supplied primary texts.

No claim of novelty is made for the disjoint-transposition proof of non-fullness (F.3), the shifted phantom-homotopy construction (F.10), the tower comparison (F.11), or the large rational-module constructions (F.12). These exact formulations were not located in the primary sources searched. The proofs, rather than absence of a search hit, carry their mathematical content. Additional F.12 searches included “locally finite group rational cohomological dimension cardinal aleph one,” “locally finite abelian cohomological dimension,” and “Holt conjecture Osofsky Chen.” A MathOverflow discussion served only as a lead to primary group-cohomology literature. Holt's original 1981 PDF was inaccessible; F.12 instead cites the independently opened proof in DKLT.

A side search on finite monoids and projective spaces found the recent primary arXiv paper 2610.38760, *On a Conjecture of Fiedorowicz*. This lead was sent to the parent and the Part G agent. Part F does not rely on that paper.

### Computations

`code/f_checks.py` and `code/f_checks.out` contain all finite computations for Part F. The program checks the shift-conjugacy equation on 5,913 permutations supported on initial sets of sizes 1 through 7. It validates the one-object two-arrow category BC2 (all identity equations and all eight associativity triples) and computes its normalized mod-2 bar boundary through degree 9. The symbolic all-degree proof is in F.1. It also checks several finite truncations of the 2-adic congruences for the telescope cocycle. The output explicitly warns that each finite congruence has solutions; the proof of failure of an integer solution is an infinite argument in F.6.

`code/f_metadata.py` writes the 13-row statement register `research/F_results.csv`; its output is `code/f_metadata.out`. Neither script searches all finite categories, and no such claim is made.

### Corrections and clarifications

Lead 3 is correct after making “finite spaces” mean finite CW homotopy types (or using their retract completion). It is false if read as saying that the given inclusion of *all* finite-category homotopy types exhibits spaces as their Ind-completion. BC2 is a finite category and is not compact. Nevertheless the space-valued restricted Yoneda on all finite-category types is fully faithful, because that larger full testing subcategory contains the finite CW types and is dense.

The companion's finite-support shift proof is valid. It already proves non-faithfulness directly, besides non-conservativity. Thus Freyd's theorem is a stronger independent obstruction rather than a necessary extra argument for the finite-category case. Part F also supplies a direct non-fullness example: locally defined maps from the free group on an uncountable set to the countable finitary symmetric group, using disjoint transpositions.

The companion's telescope example is valid even for finite-category nerves whose CW dimension is infinite. The reason is the finite generation of their fundamental groups and cyclic factorization into Z[1/2], not topological compactness of those nerves. Part F keeps this exact distinction.

The phrase “in the homotopy n-category, finite tests are faithful” is not well typed without saying which dimension of morphisms is meant. F.9 proves conservativity for every n>=2. F.10 disproves faithfulness on the highest retained morphisms, hence full faithfulness of the n-functor, for every finite n. This does not by itself disprove injectivity on ordinary homotopy classes of 1-morphisms. For countable CW source, F.11 actually proves bijectivity on those classes for n>=2 with coherent finite-CW tests. F.12 independently refutes both ordinary fullness and faithfulness without a source-size restriction, using torsion abelian groups with large rational cohomological dimension. It also refutes injectivity on each retained pi_k using correspondingly shifted twisted Eilenberg–Mac Lane targets.

Arlin's strict embedding theorem does not imply bicategorical full faithfulness of finite tests. The difference between strict transformations, pseudonatural transformations, full diagram domains, and finite diagram domains is kept explicit. Conservativity is not an equality test for associativity or T^2=1.

No transcription correction specific to the requested manuscript ranges was established by this contribution; the parent owns the page-by-page manuscript audit.

### Resolution of the finite-height arbitrary-source question

An earlier working draft left F.12 open. The final proof replaces that provisional gap with counterexamples at every finite height. For n>=2, take G=direct sum of aleph_(n-1) copies of C2. DKLT Corollary 6.10(2) gives cd_Q(G)=n. A syzygy M=Omega^n Q in the rational bar resolution gives an explicit U-small coefficient module and a nonzero class in H^n(G;M) by dimension shifting. In the split Borel K(M,n) fibration, the corresponding section and the zero section remain different even as unpointed maps: the zero section makes the base mapping-space monodromy fix the zero component. Over every finite subgroup H, rational averaging makes the section space K(M^H,n), whose (n-1)-truncation is contractible. Finite-category test presheaves of BG are the filtered colimit of those of BH. Since BH itself is a test, the coherent truncated presheaf section space is therefore a homotopy limit of contractible spaces, hence contractible. This proves nonfaithfulness. Replacing n by n+k in the fibre degree supplies the same obstruction on every retained pi_k.

For nonfullness, use G of cardinal aleph_n, nonzero H^(n+1)(G;M), and the fibrewise path fibration between zero and that section of the split K(M,n+1) bundle. The resulting K(M,n) fibration has no actual homotopy section, but its truncated presheaf has a coherent section. Such a transformation cannot lift to a map because maps into a 1-type target are fully faithfully preserved by R_n for n>=2. This last comparison also proves that nonfullness survives restriction from finite-category tests to finite CW tests. The proof explicitly uses truncation of a fibre over an already 1-truncated base; it does not assert that truncation is generally left exact. Source cardinal bounds are aleph_(n-1) for nonfaithfulness and aleph_n for nonfullness. All coefficient modules and total spaces stay in U.

For the manuscript's equations, F.13 supplies the exact conditional tests. Infinity-level coherent finite tests suffice without a source-size restriction. Height two suffices for equality when the source has countable CW homotopy type and the tests include a coherent modification, not just unrelated homotopies. No fixed finite height supplies a general equality test for arbitrary sources, by F.12. A direct path-model proof can still settle a particular equation independently of any testing criterion. The countable-source theorem is consistent with the counterexamples: the first height-two nonfaithful example has aleph_1 cells. The requested general fullness and faithfulness questions in Part F are no longer left open.

F.13 includes literal counterexamples to both identity-testing implications. In the split bundle E, translation T by the nonzero rational cohomology section satisfies R_n T homotopic to the identity, but T² is not homotopic to the identity because it takes the zero section to the nonzero 2-alpha section. The operation m(x,y)=T(x) has coherently associative finite-height tests, while its actual associators are T² pr_1 and T pr_1 and are distinct. Preservation of the needed fibre products is justified over the 1-type base; no general left exactness assertion for truncation is used. These constructions are not assertions that any particular path model has a false identity.

### Independent review of Part D and additional diagnostic

At the parent's request, D.1, D.3, and D.4 were independently checked. No gap was found. In D.1 the resolution `Q_X(x)=N(X/x)` is covariant and projectively cofibrant, and its ordinary colimit is `NX`. The horn attachment count remains bounded by the stated cardinal. The lift `Q_X→A^f` is a lift over the terminal diagram; its composite to Y defines the map g, rather than presupposing a lift over a preassigned g. In D.3 the tagged Grothendieck construction is the finite categorical model of a double mapping cylinder, hence a homotopy coequalizer. In D.4 finite categorical presentations lift through filtered colimits, including all finite natural-transformation data, and local finiteness of the colimit does not require injective stage maps.

The exact tower argument in F.11 was checked again: the fiber of a space E→τ≤mE is m-connected. A homotopy inverse limit of a tower of such fibers is (m−1)-connected, with nonemptiness when m=0. This proves precisely the stated range, not a stronger one.

For the unresolved S² countability question in D.6, Sweeney's six-element monoid from v2 Example 5.2 (five nonidentity elements) was examined. Its source is `research/Sweeney2026v2.txt`, obtained by the Part G agent. The program `code/f_sweeney_cup.py`, with output `code/f_sweeney_cup.out`, validates the 125 semigroup associativity triples and computes the normalized rational bar-cochain matrices through d3. The ranks are 5, 19, and 105; H² is one-dimensional, and the square of an explicit generator is a coboundary. This does not classify the homotopy type. The conjectural wedge-of-spheres identification is not asserted. The known retraction onto the five-element S² monoid makes the H² generator spherical, so an automatic CP∞-style phantom-map argument does not follow. No determination of the cardinality of [BM,S²] resulted from this computation.

---

## Part G research and verification report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. This contribution is `sections/G.tex`, with seventeen numbered statements and a separate statement ledger. The root paper owns the common conventions and bibliography assembly.

### Read

The attached Part G prompt and relevant XIIapp companion blocks were read, in particular the degree-three correction for the two-object category, the three-object/21-arrow example, and the four-object sphere construction. The full supplied Fiedorowicz 2002 LaTeX was read. The Barmak–Minian supplied LaTeX was read around the sphere lower bound and uniqueness theorem. The companion was used as a research lead, not an authority.

The following primary PDFs were opened and retained locally for checking: Fiedorowicz 1984 (Theorems 3.5 and 4.7), Miller 1984 (Theorems A and B), Cianci–Ottina arXiv:1512.06088v1 (Corollary 5.8 and Theorem 5.10), Sweeney arXiv:2502.05276v1 (Example 8.2 with its exact projective resolution), Sweeney version2 June2026 (Theorem2.7 and Tables3–5), Martinian–Steinberg arXiv:2511.12657v1 (Theorems A/B and group-completion discussion), Ben-Bassat arXiv:2610.38760v1 (Theorems A–C, Sections2–5, Conjecture7.1), and Carcacía-Campos arXiv:2611.09718v1 (Theorem6.2 and related orbit construction). `g_fetch_sources.out` records exact URLs, byte sizes and SHA-256 hashes.

The main theorem of the recent Ben-Bassat preprint is reported as **Known (cited recent result)**, not as an independently verified proof of the entire19-page paper. Its finite-fundamental-group Conjecture7.1 is separately refuted by the explicit argument below. The full McDuff1979 paper was not obtained; the unrestricted monoid theorem is cited through the verified independent proof of Fiedorowicz1984, Theorems3.5/4.7. No unverified McDuff theorem number has been invented.

### Mathematical conclusions and corrections

For finite categories, the object/arrow minima are S1=(2,4), S2=(1,5), S3=(1,7), RP2=(3,9). For posets the sphere pairs are (4,8),(6,18),(8,32); RP2 needs13 objects, and its13-object model has49 arrows. The global RP2 poset arrow minimum is only bounded here by28 and49. We explicitly do not promote object-minimality to arrow-minimality.

The five-element rectangular-band monoid realizes S2. The S3 example in Sweeney v1 is a **six-element semigroup**, hence a **seven-element monoid after adjoining identity**. Confusing these conventions would give a false six-arrow monoid upper bound. Both monoids have complete, finite projective resolutions checked in the program, so their full homotopy types are proved, not guessed from a few homology groups.

For a finite monoid M, a maximal subgroup H=eMe in the minimal ideal surjects on U(M)=pi1(BM). Its map to BM is correctly typed through the Karoubi envelope because H→M need not preserve the global identity. Miller1984 TheoremB forces this map to be trivial on pi1 if BM has finite-dimensional CW type. Thus that type must be simply connected. This rules out finite monoid models of both S1 and RP2 and refutes Ben-Bassat2026 Conjecture7.1. The argument does not conflict with that preprint's simply connected realization theorem.

A strongly connected component of a finite category has fundamental group generated by a finite local subgroup. The same Miller argument kills its image when the whole classifying space has finite-dimensional type. Collapsing these components to identities produces an acyclic category of no greater size with the same fundamental group. This statement is only about pi1; no higher homotopy equivalence is claimed. It provides the exact3-object9-arrow lower bound for RP2.

Literal unrestricted-size conventions change object minima: McDuff/Fiedorowicz gives a one-object small monoid model of every connected type, with a countable model for countable CW types. Accordingly all four unrestricted category object minima are1, but the least arrow cardinalities for unrestricted monoids are aleph0,5,7,aleph0. Minimizing objects and arrows is a separate optimization in this convention.

Finite category does not mean finite CW nerve. The group C2 supplies a two-arrow category with classifying space RP-infinity. Conversely, having finite data in each homotopy/simplicial degree is not sufficient for realization by a finite category; G.2 supplies an exact diagonal counterexample.

### Computed

`code/g_finite_models.py` constructs and checks:

- sphere posets S1,S2,S3 with4/8,6/18,8/32 objects/arrows;
- the3-object9-arrow RP2 category with two arrows per increasing pair and addition-mod2 composition;
- its13-object49-arrow face-orbit poset;
- the5- and7-element monoids and complete finite projective resolutions.

It checks all identity and associativity equations. Normalized boundaries use exact integers, F2 ranks use exact integer bit operations, rational ranks use SymPy exact arithmetic, and integral resolution images are checked by Smith diagonal units. The positive sphere identification uses the analytic simply connected homological Whitehead proof; finite-range nerve homology is only a consistency check.

The exhaustive search covers every monoid with at most4 elements and every connected category with at least2 objects and at most6 arrows. Endpoint-count distributions cover every labeling; products vary over every correctly typed target and every associative table is accepted. No quotient by isomorphism is needed for exhaustiveness. Counts for identity-labeled monoids of orders1,2,3,4 are1,2,11,156. Counts for2-object categories with3,4,5,6 arrows are2,11,76,977;3-object counts at5,6 arrows are6,54. Other connected cases in scope are empty.

Ten multi-object tables have F2 Betti vector (1,0,0,1), but exact rational homology is (1,0,0,0) in each. Two are the category join C2*C2, so this is a concrete check that one low-degree coefficient system is insufficient. The output retains all ten composition tables. The final exclusion concerns S3, so these rational checks resolve the concrete ambiguity.

The remaining monoid lower bound through order6 uses Sweeney2026v2 Table5 plus its Theorem2.7 reduction. The local computation does **not** claim to rerun all5/6-element monoids. This external computational dependence is explicit in G.15 and the ledger.

Every authored executable program is included with its output: `g_fetch_sources.py/.out`, `g_finite_models.py/.out/.json`, and `g_write_ledger.py/.out`. Short exploratory shell/Python read commands and a temporary candidate-inspection command were used while developing the programs; the resulting candidate inspection is incorporated into the final `rationally_checked_candidates` output. The code's categorical composition dictionary is explicitly named `composition_first_then`; the monoid constructor converts the usual product convention accordingly.

### Literature searches

Exact-title searches covered Fiedorowicz's finite monoid realization conjecture, Homotopy Types of Small Semigroups, Realizing Wedges of Moore Spaces as Classifying Spaces of Finite Semigroups, Poset Splitting and Minimality of Finite Models, the Sullivan conjecture on maps from classifying spaces, and the October/November2026 preprints. Additional searches used “finite category K(Z,2)”, “finite monoid CP infinity”, “finite monoid real projective plane”, and “finite monoid Sullivan”. Search-engine snippets were followed by actual primary PDFs before a result was used. The signed source bibliography labels each included entry verified and states the opened version and relevant theorem numbers.

### Remains open in this audit

The exact global arrow minimum for an RP2 poset lies in[28,49]. The fact that every13-object model has49 arrows does not exclude a model with14 or more objects and fewer arrows. No exhaustive search over that entire interval was performed.

We do not give an intrinsic characterization of all potentially infinite-dimensional homotopy types realized by finite categories or finite monoids. The finite CW portion is settled; a finite-type counterexample shows why the general case is stricter. As concrete remaining test questions, we do not settle whether K(Z,2) has a finite categorical model or finite monoid model. We do not claim that these are newly posed or that the literature contains no answer.

For the parent's Part D, Sweeney v1 Example8.5/v2 Example5.2 gives a6-element monoid with H_n=Z for every n>=2 and pi1=0. No full homotopy-type identification or uncountability theorem for its maps to S2 was established here; homology alone cannot justify either conclusion.

---

## Audit of the remaining local ind-presentation implication

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim is made.

### Exact manuscript passage

The original transcription `background/grothendieck/DER_III-V/DER_III-V_text.tex` was read from the argument immediately preceding manuscript page 44 through the paragraph on manuscript page 46. At page 44 the asserted envelope comparison is said to be an ind-isomorphism exactly when its associated functor inverts weak equivalences. At page 46 the manuscript restates this as existence of a sequence of Thomason–Kan categories representing the same presheaf. The subsequent assertions about making transition maps full inclusions, the locality of the union, and the uniqueness or weak equivalence of union maps are logically separate.

The smallest original claim is sequential. The more general version for a U-small filtered diagram is recorded separately. The term “local” is interpreted consistently with C.3, hence equivalently as isomorphism in Cathot to a groupoid; it is not silently replaced by Thomason fibrancy.

### Results

The implication from W-infinity invariance to a local ind-presentation was neither proved nor refuted in this audit. E.17 explicitly marks both the sequential and general U-small filtered versions Open. This records the limit of the audit, not a claim that the problem is unknown throughout the literature.

There is an exact proved criterion, supplied by the actual reflection Pi1:Cathot→Gpd and the formal A.4 theorem. A small ind-object has a presentation by local categories if and only if its associated presheaf inverts every unit X→Pi1X, if and only if its canonical ind-unit is invertible. Equivalently the presheaf inverts W1. When this occurs, applying Pi1 to the original diagram provides the required presentation on the same index, so no additional sequential cofinality or strictification assertion is needed.

The precise unproved implication is W-infinity invariance ⇒ invariance under all X→Pi1X. These units need not be weak homotopy equivalences. A.7 proves descent to the presheaf colim_i[-,BK_i] on Hot; it does not identify that varying-target presheaf with a single representable. D.8 excludes a small presentation when the descended presheaf is represented by a non-1-type; applying it separately to a stage would be invalid.

Two positive special cases are proved. If a cofinal subdiagram has all BK_i of 1-type, A.7 and objectwise groupoid comparison prove invertibility of the ind-unit. If the descended presheaf is representable, D.8 forces its representing space to be a 1-type and the ind-object is essentially constant with a groupoid representative.

The U-small index restriction is indispensable for any possible positive theorem. D.7 constructs a V-small, cardinal-unbounded ind-presentation of maps into K(Z/2,2). It cannot have a groupoid ind-presentation, as the canonical map induced by S²→e distinguishes it from every colimit of groupoid representables. This refutes only the enlarged-index variant. E.4's groupoid-like full filtration is likewise not a counterexample to the local-presentation existence question: its stages already satisfy that conclusion, although its union has the asserted failures.

### Searches and limits

The existing proofs in A, B/C, D, and E were reread. Primary-source searches investigated whether a cardinal-controlled relative Kan–Thurston construction with kernels admitting no small quotients could force the missing unit invariance. Search terms included “simple group plus construction every,” “Kan-Thurston simple groups homology,” “simple groups prescribed homology,” “Kan-Thurston no nontrivial quotient,” and “simple group homology of space.” No verified primary theorem establishing the required strengthening was found in this run. Secondary discussions were treated only as leads and are not cited as authority for a mathematical assertion here. Ordinary Kan–Thurston or acyclic-envelope theorems were not strengthened without proof.

No additional higher-homotopy-killing assertion is used in E.17. Such information alone would not establish factorization through a 1-type; in particular a nonzero class CP²→K(Z,4) induces zero on every higher homotopy group but does not factor through the point.

### Independent F.12–F.13 check

The current F.12 and F.13 were read again line by line. No cross-reference or mathematical defect was found. The finite-subgroup filtered-colimit formula uses finite generation of component fundamental groups and finitely many components. Truncation of section spaces is invoked only over mapping spaces into BG, which are 1-types. The zero section fixes its fibre-component under base mapping-space monodromy, justifying the distinction of unpointed classes. The module syzygy and d/n cardinal indices are consistent. The nonsplit fibration has no homotopy section, and the 1-type-target mapping comparison proves that its non-realizable transformation remains non-realizable after restriction to finite CW tests. F.13's translations and associator comparison use only fibre products over this same 1-type base; T²pr1 and Tpr1 are correctly typed and distinguished using T inverse.

No computations or new programs were needed for this formal audit. No root A/D/E source file was edited; `sections/E_ind.tex` is supplied for insertion after the existing E.16 material.

---

## Independent exact-path supplement

### Deliverable

`sections/E_path.tex` contains E.20–E.27. E.20–E.24 give complete proofs for the actual integer-fence eventual-path category, actual even translation, actual left- and right-padding comparisons, and the manuscript's actual left-right concatenation for the canonical block D=(+,-), with Sigma all arrows. E.25 extends actual collar weak equivalences and literal even translation to every admissible Sigma, and proves the resulting relative operation defined and unital. E.26–E.27 retain the precise remaining arbitrary-cofinal-type and arbitrary-block/relative-associativity claims as Open in this audit. It can be input at the end of Part E. Its non-elementary categorical input is Quillen A/B. Shoikhet2016 provides a related finite-stage identity-collar calculation; the half-fence comparison is proved independently. It does not rely on restricted Yoneda conservativity or faithfulness.

### Primary source opened independently

- Boris Shoikhet, *On Evrard's homotopy fibrant replacement of a functor*, arXiv:1412.0317v4, 7 November 2016: https://arxiv.org/pdf/1412.0317 (opened full PDF in web tool, ref turn71view0).
- Exact indexing in Section 2.1, equations (2.2)–(2.5): the unique inclusion m→n is i↦n−m+i, so its transition pads the left end. This was checked, not inferred from the general description of a cocylinder.
- Section 3.2.1, Proposition 3.3, PDF pages 25–26: identity-pair sliding through a finite zigzag. E.23 gives an explicit compatible half-fence version and supplies its continuous realization homotopy independently.
- Theorem 2.8 and Lemma 3.1 were inspected but are **not used**: the draft dependence was removed after an exact indexing audit of the zero-length stage. No identification of the manuscript's colimits with a categorical cocylinder is assumed in the final proof.
- Theorem 1.8 records Quillen B in the under-comma variance used in E.21. The parent also has Quillen's primary 1973 text.
- Journal primary metadata: https://tac.mta.ca/tac/volumes/31/34/31-34abs.html ; volume 31, no.34, pages 989–1015, published 26 October 2016.

### Checks and limits

The finite-support proof distinguishes positive even-even intervals (both endpoints sources) from positive odd-odd intervals (both sinks); the zero-length diagonal is never called a Grothendieck fibration. The lift category at the filtered union is not assumed to have a Cartesian lift. Its weak contractibility is proved by finite diagrams and filtered simplicial colimits.

For smooth+proper ⇒ strict fibre = homotopy fibre, the supplement writes both projections of the category of arrows over a base arrow, the appropriate comma categories, their deformation retractions to lift categories, and the natural transformation giving the Quillen-B base-change condition.

Translation is proved in the localized slice by cancelling the constant-path weak equivalence and then taking derived fibres. The natural strict-fibre comparison identifies the result with the actual translated fibre map. This avoids a possible phantom-map gap in an argument only checking finite stages.

For one-sided models, the final proof uses explicit functors phi_j on the negative half-fence, inserting a pair of duplicate vertices at -j. Consecutive precomposition functors are connected by a natural transformation in the direction of the original fence edge. They become the identity on each finite diagram once the insertion is outside its support. Concatenating their realization homotopies gives a continuous homotopy from right-collar insertion to the identity, stationary near the limiting time on each nerve simplex. Finite diagrams and nullhomotopies in the two-sided model can be shifted into the half-fence; the collar homotopy handles basepoints and makes the half-fence inclusion a weak equivalence. The two-sided derived-fibre theorem then transfers naturally. This proof does not need Shoikhet's strict prefibration assertion or a general homotopy-colimit theorem.

For actual concatenation, the category of composable pairs is treated over X^3. Its constant section is a weak equivalence and its strict fibres are shown to be derived fibres, using the middle-coordinate fibre and then the remaining two coordinates. Cancellation of constants in this localized slice proves compatibility with ordinary path concatenation, and the projection identities identify the comparison on a product fibre as the product of the two single-path comparisons. This is stronger than a bare isomorphism of path-space homotopy types.

No finite counterexample is introduced in the supplement. `code/e_fence_check.py` and its saved output provide a bounded off-by-one/parity audit of the universal formulas: 31 insertion positions on 65 fence vertices on each half-fence, and all 143 walking-arrow half-fence paths of lengths 0,2,4,6,8. The program checks functoriality, component arrows, naturality, endpoint preservation, eventual stationarity, and preservation of the geometric direction of every noncollapsed edge. The general theorem is supplied by the written proof, not inferred from these bounded checks.

### Exact manuscript scope and crosswalk suggestions

- Relative paths and admissibility are defined at VII manuscript pages **65–67** (not page60): backwards arrows lie in Sigma, Sigma contains identities and is closed under composition, and the subcategory is full. The latter is essential: collar homotopy components are not required to lie in Sigma.
- The type category is specified combinatorially at VII ms50'–53; useful length is the number of constant-sign runs, ms75–76. The manuscript's cofinality is for its reachability preorder, ms99–102, and is equivalent to unbounded useful length, ms138. E.26 includes these exact definitions and does not substitute homotopy cofinality of a functor.
- Section12 declares Sigma=all arrows at **ms137**, so all of ms150–156 falls under E.20–E.24's all-arrows scope.
- At **ms145**, t_n=(Delta+Delta−)^{2n} with symmetric collapse delta_p*id*delta_p has support vertices [-2n,2n], exactly the model in E.20.
- At **ms147**, T^p sends a_j to a_{j-p} and likewise shifts the edge indices. Odd p exchanges the two parity models on the **same X**; at ms148 it acts on their disjoint union. Therefore E.22/E.25's formula T²c(j)=c(j−2) is literally the manuscript map. No passage to X^op is part of this particular definition.
- Suggested E.16 row VII108–115: retain E.8 for the ordinary-colimit comparison, add **E.26** for the remaining specified all-type projection. Do not imply that ordinary path-space comparison identifies the original projection to Ch_Sigma automatically.
- Suggested E.16 row VII116–120: **E.23/E.25 prove the concrete collar comparisons; E.26 retains arbitrary left-cofinal type systems and their canonical/transitive comparisons as Open.**
- Suggested E.16 row VII125–127: **E.24 proves the all-arrows canonical alternating-block operation; E.25 gives relative canonical existence/units; E.27 retains relative associativity and arbitrary-block independence with their original quantifiers.**
- Suggested E.16 row VII150: **E.22 and E.25 prove the literal T² statement directly**, including arbitrary admissible relative classes in the canonical model.

The smallest uncovered changes to E.24's hypotheses are already a proper admissible Sigma with D fixed, or the three-letter alternating block (+,-,+) with its specific left/right/symmetric transitions. These are explicit gaps in the current audit, not claimed counterexamples or claims of research-level open problems. E.7/E.9 remain conditional derived replacements and do not decide these raw comparison and composition assertions.
