# Chapter XVIII-a: audit and mathematical commentary

**Commentary and audit produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).**

Completed 10 November 2026. This report concerns the supplied extract of Alexander Grothendieck's *Les Dérivateurs*, Chapter XVIII, manuscript pages 50–138. It credits the present AI-produced work only; it makes no attestation about subsequent assembly or editing.

## Scope and coverage

We read the full supplied transcription, checked its mathematics against the edition, and inspected every leaf of the authoritative 45-leaf PDF. The first two leaves are preliminary material; the mathematical text occupies edition printed pages 1–43. The manuscript has 89 consecutive page labels, 50–138. The PDF, printed, manuscript, and new reader page numbers are separate systems. In the supplied PDF, a numbered edition page occurs at PDF leaf equal to its printed number plus two. All correction records use PDF leaves, as required.

The working ranges overlap at the PDF leaves on which a manuscript range changes. The assembled registers contain one record for each audited assertion or subsidiary inference, rather than duplicate rows for those overlapping images.

| Manuscript range | Authoritative PDF leaves | Edition printed pages | Claim records | Principal material |
|---|---:|---:|---:|---|
| 50–64 | 3–10 | 1–8 | 41 | Pseudo-topoi, adjoints, tensor product, density, presheaf extension |
| 65–90 | 10–23 | 8–21 | 132 | Tensor representability, accessibility, first filtration, restricted ind-objects, common presentations |
| 91–115 | 23–35 | 21–33 | 71 | Comma adjunctions, coproducts, cocompleteness, universal property, cardinal estimates |
| 116–138 | 35–45 | 33–43 | 74 | Intrinsic filtration, diagram presentability, bounded presentations, descent and retracts |

The delivery contains all six prescribed files, the assembled reader source and PDF, the prepared transcription, the unchanged supplied transcription and authoritative PDF, and the code and small data files needed to reproduce the assembly and checks. The final reader has **74 pages**. Its overview occupies **three pages**, contains no sectioning command, and is readable independently of the commentary. There are **41 commentary blocks**, approximately **19,437 whitespace-delimited word tokens including LaTeX**, **318 claim records**, **73 collation records**, and **13 bibliography entries**. Formula tokens make the word count only an approximate measure of prose length.

The supplied `index_earlier.md` was checked for continuity. It contains no previous commentary on this portion of Chapter XVIII. The reader refers to the pertinent earlier blocks on diagram categories, coefficient categories, and the distinction between a formal ind-object and a realized colimit. We have not repeated a general introduction to derivators or attributed later homotopical results to these specifically ordinary categorical arguments.

## Textual collation and preservation

All **25 supplied `% [sic]` markers** were checked against the rendered edition. Both supplied **`% ??` markers** were resolved. Additional formulas, arrow directions, subscripts, indexing categories, numbering, and doubtful grammatical readings were inspected when their meaning affected the argument. Enlarged crops were used for ambiguous colimit signs, the supposed extra Hom subscript on manuscript page 67, and the readings on pages 86 and 88.

The register has **65 `edition_slip_kept` records** and **8 `doubt_resolved` records**. It has no record classified `transcription`. One of the doubt resolutions does entail a typographic alteration: on manuscript page 99, PDF leaf 27, **“existent” is upright**, whereas the supplied transcription placed it inside the italic proposition text. The prepared transcription moves the closing italic brace before that word. The other originally flagged doubt, the line-broken “bi-contrafoncteurs” on manuscript page 55, is resolved by retaining the supplied diplomatic reading.

These counts do not mean that 65 mathematical theorems are false. Collation records include grammar, duplicated numbering, variance errors, wrong ambient categories, and false intermediate inferences. A single flawed theorem can have several textual manifestations, and a valid theorem can have a flawed proof. The register preserves these distinctions.

No mathematical edition slip has been silently repaired in the French text. In particular, the projective-limit sign and opposite-category superscript in Lemma 4.3.2, the unrestricted restriction assertion in the proof of 4.4.16, the reversed evaluation-adjoint formula in Lemma 4.5.8, and the assertions disputed in 4.5.13–4.5.16 remain as supplied. The commentary states the intended or corrected versions. Three initial suspicions were rejected after closer inspection: the first Hom calculation on page 67 has no extra subscript after the colimit; page 86 really says type J; and page 88 really includes the cardinal after “grande devant.” Their correct transcriptions are retained.

The supplied source's paired footnotes 45 and 46 were checked against PDF leaf 38. Their printed numbering is correct. The reader disables footnote hyperlinks to avoid duplicate destinations produced by the manual paired-footnote construction; ordinary citations and URLs remain linked. The source-body comparison in `checks/verify_assembly.py` proves that, after stripping comments, the sole body change is the verified typographic adjustment to “existent.” Reader-only preamble changes and updated uncertainty comments are shown in `checks/source_changes.diff`.

## Meaning of the claims register

The register follows the source's treatment of each assertion. Its `proof_status` counts are 141 `proved`, 33 `sketched`, 95 `stated`, 6 `conjectured`, 2 `open`, and 41 `false`. The last category means that the assertion or inference **as written** is false. It includes literal variance mistakes and unsuccessful proof steps; it is not a verdict that 41 main results of the chapter fail. A question subsequently answered in the commentary keeps its original source status, with the answer in `repair` and `notes`. Likewise, a modern proof supplied here does not convert a source sketch into a source proof.

The two `open` rows record questions in the manuscript. They do **not** certify that the corresponding questions are open in the current literature. The register uses all seven permitted assertion kinds and does not add an unofficial status vocabulary. Exact citations and qualifications appear in the repair and reference fields, with fuller proofs in the anchored commentary.

One convention is essential throughout. For an infinite cardinal \(\pi\), “grand devant \(\pi\)” means filtered for diagrams with at most \(\pi\) arrows, hence **\(\pi^+\)-filtered** in the modern regular-cardinal terminology. The objects called \(\pi\)-accessible in these pages are therefore \(\pi^+\)-presentable. The cocomplete accessible coefficient categories under discussion are locally presentable categories. These translations are stated before the detailed arguments, and no inaccessible-cardinal or continuum hypothesis is imported into proofs that do not need one.

## Main mathematical conclusions

### Pseudo-topoi and the tensor problem

The opening adjoint and representability assertions are read through the dual special adjoint functor theorem, with the hypotheses and variance made explicit (Artin et al., 1972, Exposé I, §§7–8). A pseudo-topos need not be accessible by definition. The comparison between its small dense generating family and modern local presentability is a later theorem, not an assumption added to the opening paragraphs.

The actual bicategorical product of pseudo-topoi, when morphisms are represented by cocontinuous inverse-image functors, has coefficient category \(\mathcal M\times\mathcal N\). The proposed separately cocontinuous tensor represents a different universal property. The commentary proves this distinction by decomposing \((m,n)\) as \((m,0)\amalg(0,n)\), and explains why the tensor can nevertheless agree with the product for Grothendieck topoi and geometric morphisms. That latter comparison is supported by Pitts (1985, Theorem 2.3), rather than inferred from terminology.

The dense-presheaf construction establishes local smallness and reconstruction of continuous extensions. It does not by itself produce the reflector. The missing completeness hypothesis in the general extension assertion on page 61 is exposed by the finite-set example. The naive product of two representable presheaves is separately continuous only when both representing objects are terminal, because preservation of the empty colimit is already decisive. The reader gives a complete calculation of \(\mathbf{Ab}\boxtimes\mathbf{Ab}\simeq\mathbf{Ab}\), identifying the external tensor with the ordinary tensor product over \(\mathbb Z\).

Lemma 4.3.2 is false in the generic form printed: completeness is substituted for the cocompleteness used by its proof. The opposite of the category of ordinals in the fixed universe supplies a counterexample to that lemma. This does not disprove Proposition 4.3.1(b′⇒c), whose particular tensor embedding has additional hypotheses. For accessible factors, we supply a complete positive construction: reduce the continuity conditions to orthogonality to a set of presheaf maps, then alternately adjoin extensions and identify extensions agreeing on their domains. A regular presentability bound controls the transfinite construction. This yields the reflector, accessible generators, and elementary tensors. Kelly (1982, §6.5) supplies the ordinary enriched background; Lurie (2017, §4.8.1) supplies a carefully delimited higher-categorical comparison.

### Accessibility and restricted ind-completions

The structural conclusion behind Theorem 4.3.6 is valid. Starting with a small dense family of presentable probes, we construct a small subcategory closed under the appropriate bounded colimits and prove directly that the ambient category is its restricted ind-completion. The proof includes the size calculation, filteredness of each canonical slice, and the ind-object Hom formula. It avoids the abandoned numerical proof on pages 72–76.

The early cardinal-filtration proof uses an unestablished directed-hull estimate and an SGA 4 covering-family bound without its universal-epimorphic and pullbackability hypotheses. The commentary identifies the precise missing steps without treating the failure of that proof as a counterexample to its intended structural theorem. The proposed indexing poset on page 76 does fail in the elementary finite-set example given in the reader.

The restricted ind-completion is cocomplete and has the stated universal property. We give complete arguments for the omitted comma adjunction, products of filtered indexing categories, the required coproducts, filtered closure, and extension of functors. The assertion that restriction is fully faithful on **all** functors is false; restriction is fully faithful on the functors preserving the relevant density presentations, which is the version the universal-property argument needs (Artin et al., 1972, Exposé I, Proposition 7.8).

The question on manuscript page 94 has a negative answer under the stated hypotheses. Take \(C\) to be the countable sets, let \(F(c)\) be the finite-image maps \(c\to\mathbb Z\), and equip \(F\) with translation by \(\mathbb Z\). It is an ordinary ind-object with an action, but any equivariant representable stage must be empty; the proposed evaluation is not final. The source of the failure is the difference between ordinary filteredness and the stronger filteredness relevant to the existing countable colimits. Henry's (2025) exact diagram-category comparison is cited with the hypotheses and version-specific numbering actually checked.

### Intrinsic cardinal filtration and bounded presentations

The presentability layer \(\mathcal M_\pi\) and the pointwise presheaf-size layer \(\mathrm{Filt}^{\pi}\) differ. For sets tested by sets of size at most \(\pi_0\), the conditions are respectively \(|X|\leq\pi\) and \(|X|^{\pi_0}\leq\pi\). The correct comparison is

\[
\mathrm{Filt}^{\pi}\subseteq\mathcal M_\pi
\subseteq\mathrm{Filt}^{\pi^{\pi_0}}.
\]

The fixed-point condition \(\pi^{\pi_0}=\pi\) gives equality. The canonical intrinsic filtration and the quantitative bound \((\pi')^\pi\) survive the repairs. The proof of the diagram-presentability criterion uses the corrected right adjoint to evaluation and the natural-transformation equalizer; it does not allege a spurious generating-family gap, since “generating” in the invoked SGA convention is conservative.

The purported equivalence between the two triples in Proposition 4.5.13 is false. With countable sets as generators and \(\pi=\beth_\omega\), a set of size \(\pi\) has a \(\pi\)-sized singleton coproduct presentation, while no family of at most \(\pi\) countable subsets is cofinal among all its countable subsets. The proof is an explicit diagonal argument, independent of the continuum hypothesis.

The positive bounded-presentation statement is stronger than the warning at the end of page 138 suggests. If \(D_\pi\) denotes one-step colimits of \(C\)-diagrams with at most \(\pi\) arrows, then

\[
D_\pi=\mathcal M_\pi\qquad(\pi\geq\pi_0).
\]

The reader gives a complete flattening proof: maps from the generators factor through bounded pieces of a target presentation; adjoining the corresponding cones and coequalizer relations preserves the cardinal bound; coproducts and splitting of idempotents finish the argument. No additional exactness condition A), B), or C) is used. The general presentation result is known. Barton's (2019) authored proof and discussion locate its earlier attribution and explain the difficulty with an originally cited justification. The supplied proof is a direct repair in the present setting, without a claim of priority.

### Universality, strict epimorphisms, and the closing assertions

Footnote 50 now has a precise affirmative repair. If \(C\) also has pullbacks, then ordinary filtered colimits in \(\operatorname{Ind}_{\pi_0^+}(C)\) are universal if and only if the filtered colimits in \(C\) indexed by categories with at most \(\pi_0\) arrows are universal in \(C\). No terminal object in \(C\) and no colimits of the larger bound \(\pi\) are required. The proof simultaneously approximates the whole cocone and base-change arrow, then uses the \(\pi_0^+\)-directed family of filtered subcategories of a general index category. The unqualified printed phrase is underspecified when pullbacks in \(C\) have not been assumed; the proved statement explicitly supplies this hypothesis.

Lemma 4.5.14 misses retract closure. Factoring an identity through a stage gives a retract of that stage, and the reader supplies a counterexample to the abstract membership inference. In the intended application, bounded-colimit closure provides the retract closure that is needed.

The group example on page 135 is repaired by replacing the Cartesian-product axes with \(C_2,C_2\to C_2*C_2\), then pulling back along the infinite cyclic subgroup generated by the alternating word. The resulting family is not epimorphic. This establishes C)⇏B), while the displayed product-group family in the source is not strict epimorphic even before base change.

Corollary 4.5.16 is false as printed. The complete counterexample uses sets with a countably-ary relation. All colimits are universal, strict epimorphic families are universal, and the category has the required restricted ind-presentation. For \(|S|=\beth_\omega\), the identity-carried universal epimorphism

\[
(S,\varnothing)\longrightarrow(S,S^{\mathbb N})
\]

has a source in the bounded presentation layer and a target outside it. The excess lies in the number of relations, invisible to an underlying surjection. Every ambient hypothesis is checked in the development block, so this is a counterexample to the statement, not merely to its proof. Requiring the outer family to be **universally strict epimorphic** repairs the corollary by composition of canonical covers (Artin et al., 1972, Exposé II, §§2.5–2.6).

## Verification limits and literature status

Two assertions remain unsettled by this audit in the manuscript's full generality. First, the defective generic Lemma 4.3.2 does not settle whether the additional structure of the particular tensor embedding proves Proposition 4.3.1(b′⇒c) for arbitrary pseudo-topoi. The accessible case is proved here. Second, the proposed implication B)⇒C), from universality of strict epimorphic families to universality of ordinary filtered colimits, has no certified general proof or counterexample in this package. Searches through the relevant SGA passages, tensor and presentability sources, and material on familially regular categories and quasitoposes did not establish it. The relation-category counterexample satisfies both B) and C) and therefore does not decide this implication.

Neither item is advertised as a literature-established open problem. A limited search that fails to find a resolution does not establish global novelty or current openness. The footnote-50 theorem above resolves a specified version under an added pullback hypothesis; it does not remove that qualification from the source statement. The later Section 4.6 is mentioned only where the source itself points forward, and has not been certified by an audit of this extract.

Development blocks use `\ours` for the formulations and complete proofs developed in this audit, with an explicit disclaimer of priority. Known general theorems retain their literature attribution. No priority claim is made for the terminal-subcategory repair, the directed-hull counterexample, the bounded-presentation proof, the footnote-50 reduction, or the relational counterexample. The work is a mathematical audit with independent cross-checks of its most delicate proofs, not a proof-assistant formalization.

## Sources and exact verification scope

All thirteen bibliography entries have a URL or DOI and a scoped `verified:` note. Existing cumulative keys were reused. Verification of a statement is distinguished from verification of a complete proof or of metadata only. Author–date citations in the prose use the supplied reader's `natbib` workflow; the unmodified builder selects its bibliography style.

| Source | What was checked and how it is used |
|---|---|
| Grothendieck, Chapter XVIII (1990–1991; supplied 2025 edition) | All 45 supplied PDF leaves, formulas, footnotes and flagged readings for manuscript pages 50–138. |
| Artin, Grothendieck, and Verdier (1972), SGA 4 I | Retypesetting dated 30 July 2024. Exposé I: Definition 7.1 and 7.1.1; Propositions 7.2(i), 7.6, 7.8; 7.12–7.13; 8.1.3(b), 8.1.6, 8.7.3, 8.9.5(b), 8.12.7–8.12.9; 9.8–9.9, 9.12–9.13, 9.16 and Lemma 9.16.2, 9.17–9.18. Exposé II: 2.5–2.6. Internal numbering is used. |
| Grothendieck, letter to Thomason (1991) | Opening paragraph, printed page 2: Chapter XVIII and SGA 4 I.9; the following page's pointer to *Pursuing Stacks* §69 is reported as a pointer, not a separate audit of that text. |
| Grothendieck, Chapter XIX (1990–1991; 2019 edition) | Theorem 2.6, hypotheses and conclusions on manuscript pages 25–26, including footnotes 10–13. |
| Kelly (1982; corrected TAC reprint, 2023) | §§5.10–5.11 and 6.5, especially Theorem 5.38, Propositions 5.39–5.41 and equation (6.24); hypotheses of Theorem 5.32 and Theorem 6.5. |
| Pitts (1985) | Proposition 1.5, Definition 2.2, Theorem 2.3 and proof, printed pages 47–52. |
| Freyd (1966) | Publisher metadata and indexed primary text on page 95. The publisher download was inaccessible; the full proof was not verified. The abelian calculation is proved independently. |
| Adámek and Rosický (1994) | Publisher's Chapter 1 description and metadata, including Definition 1.17 and Theorem 1.20. The full book proof was not accessible in the consulted excerpt. |
| Adámek, Koubek, and Velebil (2000) | Published scan, Theorem 3.1 and proof, pages 535–537, for the uncountable product/filteredness comparison. |
| Henry (2025) | Theorems 1.2 and 1.3, Corollary 2.2 and §2.2 proof in arXiv:2307.06664v2, 9 October 2024. Published metadata checked; publisher PDF inaccessible. The cited numbering belongs to this preprint version. |
| Lurie (2017) | *Higher Algebra*, version 18 September 2017, §4.8.1, especially Proposition 4.8.1.15, Lemma 4.8.1.16, Proposition 4.8.1.17 and Examples 4.8.1.19–4.8.1.20. |
| Riehl (n.d.; online second-edition revision) | Proposition 6.1.5, Theorem 6.2.1 and Corollary 6.2.9 in the author's online revision consulted 10 November 2026. The cumulative key `Riehl2016` is retained, but first-edition pagination is not claimed. |
| Barton (2019) | Complete authored MathOverflow proof, including its two lemmas and use of the fat small object argument; accompanying discussion of the earlier attribution and defective cited justification. |

Full bibliographic metadata and links are in `DER_XVIII-a_references.bib`. These narrowly stated verification notes deliberately avoid implying that every page of a book, or a publisher's inaccessible final version, was checked.

## Assembly, build, and visual verification

The supplied `build_reader.py` and `derivateurs_companion.sty` are unchanged. The builder validates all 41 block kinds and anchors and all thirteen reference entries. The independent verifier checks unique claim IDs, the two CSV schemas, allowed category values, the one permitted source-body alteration, all 27 original flags, bibliography-key uniqueness, overview structure, and the placement of commentary outside open environments, displays, and brace groups. These last checks prevent an anchor from inadvertently inserting a commentary frame inside a footnote or diagram.

The prepared source adds an academic cover, A4 geometry, English language support for the commentary, microtypographic adjustment, URL line breaking, and `marginfix` for the two marginal page systems. An initial render revealed a collision between the printed-page and manuscript-page labels; the final render separates them. The original source body and equation numbering are preserved. No modifications to the package's commentary environment or assembly logic were required.

The final build runs the supplied builder, a LuaLaTeX seed pass, BibTeX, and two subsequent LuaLaTeX passes. The final logs have no compilation errors, undefined citations, missing-character messages, overfull or underfull boxes, duplicate destinations, or remaining margin warnings. All required fonts are embedded. We inspected an all-page contact sheet and enlarged pages containing dense formulas, source diagrams, long commentary proofs, marginal labels, the overview, and the bibliography. A PDF geometry check found no text spans outside the page bounds. These checks address layout and assembly; they do not replace the mathematical proofs.

The execution environment's system TeX installation lacked usable configuration and some runtime packages. The optional `checks/setup_tex_runtime.py` and `checks/tex_environment.py` supply a project-local runtime without changing system files or relaxing TeX's output restrictions. Official TeX Live package URLs and SHA-256 hashes are recorded. A complete TeX Live installation can build the reader directly with the standard commands in `README.md`; the temporary caches and installed runtime tree are not part of the ZIP.

`checks/verification.json`, `checks/pdf_validation.json`, `checks/build_manifest.json`, the final build logs, the source diff, and the package manifest record the reproducible checks. The registers and commentary fragments used by the assembler are included under `work/`; final content is in the six prescribed files at the package root.

## Proposals for future reader and format maintenance

The present format is sufficient for this package. Three modest improvements would reduce ambiguity in later chunks. A stable row identifier in the correction register would make it easier to link several source markers to one collation decision. A separate optional field for present-day disposition would make the distinction from source `proof_status` machine-readable without changing its meaning. Finally, the builder could reject anchors inside balanced LaTeX groups and environments, using the kind of conservative insertion check supplied here, and the reader style could include collision-aware marginal labels by default.

No such schema changes were applied to the six required deliverables. Duplicate source equation numbers and headings remain diplomatic readings; the commentary identifies them by page and context. The exact supplied build format therefore remains usable for the later companion assembly.
