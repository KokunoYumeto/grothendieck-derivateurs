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
