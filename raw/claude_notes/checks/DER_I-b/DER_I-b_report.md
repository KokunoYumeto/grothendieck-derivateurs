# DER I-b: textual verification, mathematical audit, and commentary

## Scope and editorial basis

This package treats the supplied continuation of Chapter I of Alexander Grothendieck’s *Les Dérivateurs*, in the electronic edition transcribed by M. Künzer, J. Malgoire, and G. Maltsiniotis. The source comparison, mathematical audit, and commentary cover the whole supplied transcription, including its overlap with the preceding package. The two CSV ledgers distinguish mistakes introduced by the transcription from readings and mathematical slips already present in the edition.

Three page systems must be kept separate:

| Material or numbering system | Actual scope used here |
|---|---|
| Attached excerpt PDF | 38 leaves, carrying printed page numbers 37–74 |
| Prompt’s page range 39–76 | Corresponds to the whole-chapter PDF positions when its two preliminary leaves are counted; these are not the printed running page numbers |
| Supplied LaTeX transcription | Printed pages 34–74, with manuscript markers 60–126 and an opening continuation before the first marker |
| Supplemental source comparison | Printed pages 34–36, checked in the same official electronic edition, whole-chapter PDF leaves 36–38 |
| Earlier-package continuity | Manuscript pages 60–66 already appear in the supplied `index_earlier.md` |
| Manuscript page 114 | Explicitly marked blank in the edition; no mathematical text has been supplied for it |

The attached PDF remains the authority for its own 38 leaves. The three earlier printed pages were checked separately against the editors’ public electronic edition; the corrections ledger labels these supplemental references with `official:` rather than assigning them fictitious attachment page numbers. The edition date, 8 July 2001, agrees. The official edition is identified by `Grothendieck1990Derivateurs` in the bibliography and by its [editorial site](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html).

The overlap is not omitted from the audit. Its definitions and claims are recorded, but the commentary uses a concise continuity block and refers to the earlier block titles instead of repeating their exposition. No claim is made to have reread the complete preceding package from its index alone. The edition’s own editorial insertions, including `[mot illisible]`, remain source readings: the original handwritten manuscript was not independently deciphered in this work.

## Files and final integration record

The six files required by `FORMAT.md` have the following roles:

| Required file | Function |
|---|---|
| `DER_I-b_blocks.tex` | Anchored English commentary, including exposition, context, later results, worked examples, status discussions, and complete developments |
| `DER_I-b_overview.tex` | A standalone account of the argument and its later interpretation, without chapter or section commands |
| `DER_I-b_claims.csv` | The audit of definitions, axioms, propositions, informal claims, questions, conjectures, and substantive footnotes |
| `DER_I-b_corrections.csv` | Transcription corrections, resolved doubtful readings, and confirmed edition slips retained in the source |
| `DER_I-b_references.bib` | Bibliographic entries for cited works, reusing supplied keys and recording verification status |
| `DER_I-b_report.md` | This account of the work, evidence, limitations, and reproduction requirements |

**Final integration record, 9 November 2026.**

- Final commentary blocks: **41, including eight development blocks**.
- Final audit records, excluding header: **275 unique records: 79 proved, 40 sketched, 113 stated, 22 assumed, 9 conjectured, and 12 false**.
- Final correction records, excluding header, with classification counts: **84 records: 5 transcription corrections, 4 resolved doubts, and 75 preserved edition readings or cross-reference ambiguities**.
- Cited bibliography entries and verification counts: **15 entries, all opened and marked verified; no missing citation keys**.
- Final reader length and standalone overview length: **62 reader pages; the overview occupies three pages (reader pages 59–61)**.
- `build_reader.py` validation and command result: **`python build_reader.py DER_I-b` exits 0: 41 blocks, all six kinds, 15 references**.
- LuaLaTeX/BibTeX sequence, final log result, and any residual nonfatal warnings: **LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX all exit 0. The final log has zero TeX errors, undefined citations, missing characters, overfull boxes, underfull boxes, or warnings**.
- Visual inspection coverage and resulting adjustments: **All 62 final pages rendered and inspected. The first 48 were reviewed in contact sheets, with full-page checks of adjusted layouts; pages 49–62 were also independently inspected at full-page size. No remaining clipping, overlap, or unreadable mathematical displays was found. The blank manuscript-page-114 label and the following page-115 label are separated**.
- Exact archive contents and reproduction entry point: **The six required files, the built reader TeX/PDF and bibliography, corrected source and frontmatter, supplied builder and format/continuity material, companion style, audit and calculation code, source evidence, optional TeX support archives, and final build logs are listed individually in `MANIFEST.sha256`. Run `python code/reproduce.py --bootstrap` from the extracted directory; omit `--bootstrap` on a complete TeX installation**.

`code/package_validation.json` records the final schema, count, citation, footnote, source-identity, and PDF checks. `code/render_validation.json` records the SHA-256 digest of the exact PDF inspected, its page count, and its rendered-page validation. `MANIFEST.sha256` covers every other file included in the ZIP; the manifest itself is excluded to avoid a self-referential digest. The packaging script verifies both ZIP integrity and every recorded digest before reporting success.

## How the text was checked

The source was divided into contiguous ranges, with the shared boundary pages read on both sides: manuscript 60–78, 79–101, and 102–126. Every corresponding attached PDF page was visually inspected against the transcription, and the missing printed 34–36 overlap was inspected in the official supplement. The text extraction from the attached PDF was not a reliable basis for reading because its embedded font encoding produced largely unusable characters. Formula and arrow comparisons therefore used rendered page images; selected pages were rerendered at higher resolution when the first image or a small glyph was inadequate.

The checks included quantifiers, variances, subscripts, comma-category orientations, adjunction units and counits, displayed arrows, diagram labels, footnote references, and the edition’s bracketed repairs. Every supplied `% [sic]` location was checked against the edition. All four supplied `% ??` readings were resolved:

| Manuscript location | Doubt | Resolution |
|---|---|---|
| Page 63, Proposition 2 | Typeface of the ending “à gauche” | Recorded from the printed proposition, with the edition’s mixed typography retained |
| Page 88, gluing construction | Subscript on $u_b$ | Plain $b$, not barred $b$ |
| Page 111, footnote 58 | Weight of the numeral in “Der 3” | The numeral 3 is bold with “Der” |
| Page 121, Proposition 9(b) | Dash before “et itou” | A typographic en dash, represented by LaTeX `--` |

The genuine transcription changes are deliberately narrow. They restore an ordinary arrow where an isomorphism arrow had been introduced, restore underlined internal/functor-category Hom notation where it was lost, supply the edition’s explicit footnote number 60, and correct the editorial insertion `[1a]` to `[la]`. Resolving a doubt comment is recorded separately from changing mathematical text. Exact replacement strings were checked to have unique matches before application.

The separate `code/footnote_coverage.csv` accounts for all 36 footnote bodies, numbered 25–60: 28 contain substantive mathematical content, six are cross-references, and two are editorial pointers. Every substantive note is mapped to claim IDs. Footnote 42 receives its own remark: its disconnected-fibre parenthesis does not describe the explicit circle-fibre model at the cited pages, although the surrounding general construction admits disconnected variants. This is retained and explained as a cross-reference ambiguity, not assigned an unqualified false status.

Errors already present in the edition are not silently corrected in the French source. Their intended mathematical repairs appear in the audit and at the relevant reading point. In a corrections row classified `edition_slip_kept`, a suggested replacement is explanatory, not an instruction to alter the source. Some rows repeat the printed reading in `should_read` and explain the repair in `evidence`; other rows state explicitly that the printed wording must be retained. The classification controls the editorial policy in both cases.

## Mathematical audit and principal repairs

### Cofinality, properness, and taking opposites

Theorem 1 on manuscript page 67 has a sound Yoneda proof under the displayed adjoint-existence and pointwise-computation hypotheses. Its use of constant homology to establish cohomological invariance is an adjunction argument, not a missing assumption that cohomology and homology agree. The commentary writes out the comparison and identifies the comma categories controlling its fibres.

Theorem 2’s lifting, fibre, and universal base-change conditions are valid after the source’s variable slips are distinguished from mathematical content. The omitted implications involving the coaspherical tests are supplied. The parenthesis in condition (d'), however, cannot be read as asserting that every coaspherical point inclusion necessarily selects a terminal object for every coefficient theory. A represented derivator of the complete lattice $\{0<1\}$ separates the two assertions. Restricting the test to categories with a terminal object gives the sufficient formulation actually required.

The twisted-arrow construction has the stated slice-category isomorphisms. Both endpoint projections are opfibrations; the edition itself corrects the initial mixed fibration/opfibration wording. Their contractible fibres explain their universal equivalence. A later displayed under-comma symbol reverses the orientation needed in the longer proof; the commentary gives the correct over-comma interpretation relative to the projection to $X^{\mathrm{op}}$. Taking opposites requires the corresponding closure of the allowed diagram domain. Modern comparisons are made with the actual definitions and results of Maltsiniotis (2005), Groth (2013), and Ponto and Shulman (2016), rather than treating “proper” as an ordinary topological condition.

The local-constancy concern in footnote 33 has an elementary answer on categories with an initial or terminal object: the contraction natural transformation, together with pointwise detection, identifies a locally constant object with the constant object at the chosen endpoint. This does not by itself prove the stronger statement for every weakly contractible indexing category. The latter requires the later homotopy-invariance theorem or an explicit axiom.

### The failed universal-equivalence argument

The failed converse in Proposition 2 on pages 79–81 is explicitly retracted in the edition. Its unsupported step applies an invariance assertion for constant coefficients to the generally nonconstant local system $f_*M_X$. The audit does not classify the whole proposition indiscriminately as false: the forward implication survives, and the two universal weak fibration conditions become equivalent under the later local-constancy hypotheses.

The fibrewise comparison theorem of Proposition 3(b) is also valid. Three cohomological arrows in its proof are reversed in the printed source; the correct comparison is $p'_*M_{X'}\to p_*M_X$. Once the direct images are computed on fibres, pointwise detection proves the result. The converse proposed in Proposition 6(b) is false, and the footnote’s proposed exception for a merely $\mathbb{D}$-contractible base is false as well. Complete asphericity controls the relevant local systems; constant-coefficient acyclicity alone does not.

The claimed rescue of the failed implication for all truncated homotopy theories already fails for the standard theory of 0-types. In the represented set-valued derivator, $e\to BC_2$ is a constant-coefficient equivalence. The covering $EC_2\to BC_2$ satisfies the universal weak cohomological and homological conditions, but pulling back to $e$ produces the non-equivalence $C_{2,\mathrm{disc}}\to EC_2$. Restriction of $C_2$-sets also gives a direct failure of full faithfulness. The later footnote about truncated theories is therefore answered separately according to whether its antecedent means an actual nerve weak equivalence or only a coefficient-detected equivalence.

### Monodromy and the finite models

The reflected-circle bundle gives the Klein bottle. The degree-one cohomology of its circle fibres forms a sign local system on the base circle. With a nonzero coefficient ring in which 2 is invertible, the cochain complex of that local system has differential multiplication by $-2$. Its cohomology on the base vanishes, although its stalks do not. The commentary gives both the cellular calculation and the direct-image splitting, translating the manuscript’s explicitly stated degree convention rather than misclassifying its $k[1]$ as a transcription error. The self-pullback restores an invariant degree-two fibre class and has cohomology in degrees 0, 1, 2, and 3. The degree-$n$ covering of the circle gives an additional simple check of the same distinction.

The finite-group construction is checked using exactness of invariants when the group order is invertible. The argument applies to arbitrary complexes by an averaging projection, without assuming an unjustified functorial splitting into cohomology groups. It gives a counterexample with both base and total category coefficient-acyclic and with nonacyclic fibre.

The finite-poset construction on manuscript pages 93–95 needs a further correction. The antipodal involution on $S^2$ and the reflection on $S^1$ each reverse the corresponding positive-degree generator, but their product fixes the degree-three product class. The 52-object total poset therefore has a nonzero top class and is not rationally acyclic. The base remains rationally acyclic, and the fibre inclusion still fails to be an equivalence; the stronger conclusion about the total space does not follow. The preceding printed orbit-category relations also have an incidence error. Both points are proved in the commentary, not repaired by editing the French source. The proposed general conditions on the separate invariant cohomologies are insufficient by themselves: taking the first factor to be a discrete regular group set makes the fibre inclusion an identity.

### The later definitions

The example on manuscript page 102 incorrectly attributes both fibre comparison and transport invariance to properness alone. The proper cosieve $\{1\}\hookrightarrow[1]$ has comma categories empty and terminal, and disproves that wording. Adding the transport condition gives the valid criterion used later in the text.

Propositions 4 and 9 receive a complete proof of the universal local-coefficient characterization. The proof preserves the quantifier over arbitrary locally constant coefficients on every pullback, including coefficients that do not descend from the original total category. The point/terminal-object test recovers transport by the valid cancellation direction for cohomological equivalences. No unrestricted two-out-of-three statement is inserted for that class.

The internal-Hom argument is valid when local internal Homs and the monoidal unit have the stated compatibility with restriction. It identifies cohomological equivalence with 1-completeness and implies homological equivalence. It does not supply essential surjectivity, and it does not identify bare constant-coefficient equivalence with 1-completeness. The word “cohomological” missing on manuscript page 122 is a material source slip, refuted literally by rational trivial and sign representations of $C_2$. The parenthesis in Der 3 (b) similarly writes the stronger locally constant condition where the intended equivalent formulation concerns constants.

The (b)-axioms and (c)-axioms have different antecedents. Modern invariance under a weak equivalence of nerves proves the former; it does not make a weak equivalence detected by an arbitrary fixed coefficient theory preserve all local systems. For spaces, mapping-space Yoneda detects the nerve homotopy type and the local-system invariance theorem supplies the strong lemma Grothendieck postpones. The claims about $\mathrm{HOT}$ are therefore given their modern affirmative status, while the distinctions for rational and truncated coefficients remain visible.

## Complete developments supplied in this companion

The label `\ours` identifies constructions and proofs supplied for this reading. It does not assert novelty. Each development states its hypotheses and supplies a proof, and its literature note says what was checked rather than claiming that no earlier treatment exists.

The principal developments are the following:

1. **Failure of arbitrary base change.** A walking-arrow map into the two-object chaotic groupoid gives an explicit small counterexample to universalizing the first weak fibration condition. A second example uses only the four-object poset $x\to a\leftarrow b\to z$ over $[2]$: all original fibre and comma categories are contractible, but pullback along the long edge leaves a discrete two-point category. The second example applies to the finite-poset domains considered in the manuscript.
2. **Cancellation for a nonempty product base.** Choosing an object of $S$ exhibits the augmentation for $T$ as a retract of the augmentation for $S\times T\to S$. Thus the envisaged product counterexample cannot occur when the base is nonempty. The empty base is treated separately.
3. **The corrected finite 52-object calculation.** The quotient-poset construction, object counts, realizations, signs of the group action, and invariant cohomology are proved completely. Exact rational chains independently check the answer below.
4. **The arbitrary pulled-back coefficient fibre formula.** For a universally weak cohomological fibration, the comparison $(f_*f^*F)_y\to H^*_{\mathbb{D}}(X_y,(F_y)_{X_y})$ is an isomorphism for every $F\in\mathbb{D}(Y)$. The proof takes a left mate and decomposes it over categories of factorizations of arrows $z\to y$. Each summand reduces to a constant-homology equivalence. The proof states the required coproduct and diagram-domain hypotheses. Its dual treats $f_!f^*F$ under the universal weak homological hypothesis, and naturality gives the associated base-change comparison.
5. **Universal equivalences and full faithfulness.** The preceding result implies that a universal $\mathbb{D}$-equivalence induces fully faithful restriction on the whole coefficient category. Both relevant adjunction comparisons are invertible. This answers the expectation on page 84 under the explicitly stated domain hypotheses.
6. **Failure of composition for the final intermediate $\mathbb{D}$-fibrations.** For rational coefficients, take the opfibration over $[1]$ with transport $e\to BC_2$, then the covering given by the regular $C_2$-set. Both maps are $\mathbb{D}$-fibrations, but the composite has transport from two discrete points to a contractible action groupoid; the cohomological comparison is the noninvertible diagonal $\mathbb Q\to\mathbb Q^2$. This settles the requested composition counterexample and explains why the stronger local-coefficient condition is needed.

7. **Failure of composition for the proposed 2-complete class.** For the represented set-valued derivator, a normalized $C_2$-valued cocycle supported on one triangle of the tetrahedral boundary face poset defines a bifibration $E_c\to B$ with fibres $BC_2$ and simply connected total category. Form $Y=\int_{[1]}(e\to B)$ and pull this bifibration back along $Y\to B$ to obtain $X\to Y$. Both $X\to Y$ and $Y\to[1]$ satisfy all the contractible-base tests of manuscript page 122; the first is even a $\mathrm{HOT}$-fibration. Their composite fails the test $\{0\}\to[1]$, whose comparison is $BC_2\to X$ with $X$ simply connected. Restriction includes sets as trivial $C_2$-sets and is fully faithful but not essentially surjective. The complete proof verifies associativity, the fundamental-group presentation, and both universal conditions. All three categories are finite; their automorphisms mean that this is not an example in the domain of finite posets.

A further worked example answers the request for stronger coefficient-relative fibrations beyond ordinary homotopy: the rational opfibration with transport $BC_2\to e$ is cohomological and homological in the complete sense, but is not a $\mathrm{HOT}$-fibration. The proof uses averaging and the behaviour of a local coefficient along cocartesian transport.

The factorization arguments were compared with Groth, Ponto, and Shulman’s homotopy-exactness criterion (2014, Theorem 3.8) and Groth and Šťovíček’s homotopical epimorphism criterion (2016, Theorem 6.10). They are coefficient-relative applications of that method. The local constructions and calculations were also checked against the smooth-functor and locally constant-coefficient treatments cited below. No priority claim is based on a failed search for their exact presentation.

## Exact finite calculation

`b_poset_check.py` enumerates the 26 nonempty faces of the octahedral boundary, takes antipodal orbits, forms the diagonal product with the four-object circle, and verifies that the resulting relations are partial orders. It enumerates every nondegenerate nerve simplex and computes boundary ranks over the rational numbers using exact arithmetic. Its output is recorded in `b_poset_check_results.json`.

| Category | Chain dimensions, starting in degree 0 | Boundary ranks, starting with $d_1$ | Rational Betti numbers |
|---|---|---|---|
| Base $E/C_2$ | (13,36,24) | (12,24) | (1,0,0) |
| Total $(E\times Z)/C_2$ | (52,340,576,288) | (51,289,287) | (1,0,0,1) |

For example, the total-space dimensions give $340-51-289=0$ in degree 1, $576-289-287=0$ in degree 2, and $288-287=1$ in degree 3. The geometric proof explains why the final class survives: it is the product of two anti-invariant generators. The computation corroborates this proof; it is not used as a substitute for a mathematical explanation.

A separate exact check, `b_two_complete_check.py`, verifies the finite category used in the 2-complete counterexample. Its `b_two_complete_check.json` records 14 objects and 100 morphisms for the extension, all 194 cocycle identities and 1,552 labelled associativity tests, and zero failures. It also records an explicit collapse certificate for the tetrahedral boundary order complex after removing the chosen triangle: 23 free-edge/triangle collapses followed by 13 free-vertex/edge collapses reduce it to a point. Every free-face condition is replayed and checked. This independently corroborates the disk presentation used to kill the central fundamental-group generator; the mathematical proof and the universal base-change arguments remain in the commentary.

## Literature and verification

Bibliography keys already supplied in `references_cumulative.bib` are reused for the same works. New keys identify additional works actually needed. The entry note `verified` means that the work was opened during this package’s research; it does not claim verification of every assertion in that work. A stable URL or DOI is supplied for every entry. Exact locators in the commentary identify the version inspected where preprint and published numbering differ.

The most consequential numbering issue concerns Cisinski’s *Locally constant functors*. The published article has **Corollary 3.8** on page 607 for arbitrary derivators and **Theorem 3.13** on page 608 for the derivator of local systems. The arXiv version numbers these **3.7** and **3.12**. The published numbering is the common convention for this package. The model-category invariance result is Theorem 1.3 in both versions. The [published PDF](https://www.math.univ-toulouse.fr/~dcisinsk/lcmodcat3.pdf) was opened and the relevant statements checked.

The primary comparisons include:

| Work | Locations and purpose checked |
|---|---|
| Cisinski (2003), *Images directes cohomologiques dans les catégories de modèles* | Theorem 6.11 and its dual: construction from a model category, including the homotopy derivator used here |
| Cisinski (2004), *Le localisateur fondamental minimal* | Theorem 2.2.11 and the localizer interpretation of nerve weak equivalences |
| Cisinski (2009), *Locally constant functors* | Theorem 1.3, Corollary 3.8, and Theorem 3.13 in the published article |
| Groth (2013), *Derivators, pointed derivators and stable derivators* | Definitions 1.5 and 1.8, and Propositions 1.24 and 1.26, for axiom conventions, strongness, and base-change formalism |
| Groth, Ponto, and Shulman (2014), *Mayer–Vietoris sequences in stable derivators* | Warning 2.2 and Theorem 3.8, for variance and factorization categories controlling exactness |
| Groth and Šťovíček (2016), *Tilting theory for trees via stable homotopy theory* | Theorem 6.10 in the author-hosted arXiv v3 text (November 2015), for homotopical epimorphisms; the author’s publication list independently confirms the 2016 journal metadata |
| Hatcher (2002), *Algebraic topology* | Sections 2.2, 3.G, and 3.H, for cellular chains, transfer, and local coefficients |
| Lurie (2009), *Higher topos theory* | Theorem 2.2.1.2 and Corollary 3.3.3.4, for straightening and the section interpretation of limits |
| Maltsiniotis (2005), *Structures d’asphéricité, foncteurs lisses, et fibrations* | Theorems 1.2, 4.13, and 5.4; Definition 4.1, Proposition 4.3, and Corollary 4.16, including the distinction between weakly smooth and weak cohomological terminology |
| Ponto and Shulman (2016), *The linearity of traces in monoidal categories and bicategories* | Section 5 of the opened arXiv text and the journal record, for the twisted-arrow construction and coends |
| Quillen (1973), *Higher algebraic K-theory: I* | Section 1, Theorem B and its following corollary, for the homotopy-fibre and transport criteria |
| Riehl (2014), *Categorical homotopy theory* | Example 7.2.9, Remark 7.2.10, Section 7.8, and Section 8.5 of the author’s text, for categorical homotopy calculations |

Grothendieck’s *Pursuing Stacks*, Section 69, and the letter to Thomason of 2 April 1991 are used for historical context. In particular, the latter’s pullback-preservation definition explains the formal closure under composition when the same weak-equivalence class is used on both sides. It is not confused with the intermediate coefficient-relative definition whose composition fails here.

The complete bibliographic details and URLs are in `DER_I-b_references.bib`. The report’s references to Hatcher and the later categorical literature do not attribute the specific 52-object correction or the particular composition counterexample to those authors.

## Status conventions and limits

The `proof_status` field distinguishes the source’s proof, sketch, statement, assumption, and conjecture, while `false` identifies an assertion invalid as written. Historical questions are marked `stated`; their current resolution or its limits are recorded in `repair`, `references`, and `notes`. No row uses an unqualified `open` status. Four supplementary records state the general fibre formula, universal full faithfulness, and the two composition counterexamples as `proved`, and the explicitly answered base-change, composition, and arbitrary-coefficient questions point to them. Thus an unresolved issue in the manuscript is not silently described as a current open problem.

The proposed 1-complete and 2-complete variants now have distinct answers in this companion. The manuscript’s phrase “as far as I know” supplies no proof. Under the compatible internal-Hom hypotheses, the 1-complete class coincides with the cohomological class and is closed under composition. The 2-complete class is not closed under composition, even for the represented set-valued derivator on all small categories: the finite categorical construction in claim `Ib-R004` proves this. The failure is essential surjectivity on local systems, while full faithfulness survives. This negative answer is not extended to the 1-complete class without its additional hypotheses, and no literature-wide open-problem or originality claim is made.

Diagram-domain assumptions remain material. The proofs use specified opposites, comma categories, twisted-arrow categories, factorization categories, pullbacks, and disjoint unions. On all small categories these operations are available. For restricted domains, each argument states the necessary closure or retains the manuscript’s conditional formulation. The successful finite-poset examples should not be mistaken for permission to import every unrestricted-domain theorem without checking its hypotheses.

The textual findings identify what is printed in the authoritative electronic edition. Without an independent comparison to the handwritten pages, a source-level slip cannot always be assigned specifically to Grothendieck or to the electronic edition’s transcription. The report therefore uses “edition slip” and “source slip” rather than asserting an unsupported origin.

## Reproduction and small format recommendations

The entry point is `python code/reproduce.py --bootstrap` in the extracted package. On a complete TeX Live installation, omit `--bootstrap`. It reassembles the corrected source and commentary from the preserved fragments, reruns both exact finite calculations, invokes the unchanged supplied `build_reader.py`, and runs LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX. The lower-level `python code/tex_build.py` rebuilds the reader without regenerating the ledgers. Final command output and the diagnostic counts are included in `build/logs/`.

The initial environment had a LuaHBTeX 1.17.0 executable but no usable LuaLaTeX format, font map, Lua font loader, or French language support. The optional bootstrap uses eight included, checksum-verified TeX Live 2023 package archives, creates its format and font map within `build/tex-runtime/`, and writes no system files. It still requires the installed engine, standard LaTeX packages, and the Latin Modern/AMS fonts; the archive is not a complete TeX distribution. No network access is needed for this bootstrap.

Presentation changes are isolated in `code/configure_reader.py` and recorded in `code/presentation_only.diff`. They add English hyphenation for the commentary, a readable page geometry, manuscript/edition margin labels, commentary bookmarks, and working bibliography links. Text-capable mathematical macros avoid compilation errors where the supplied source uses them outside math mode. An invisible node repairs a TikZ label anchored to an empty matrix cell; the intended bold Greek delta uses a proper mathematical glyph; one wide implication diagram is set slightly smaller. Two paragraphs with long monospaced editorial insertions use ragged setting, and the adjacent blank-page-114/page-115 labels are separated. These are rendering changes, not new readings or mathematical emendations. The source before these presentation changes is preserved alongside the original.

The existing six-file contract is sufficient for this package. Four small clarifications would improve later packages without changing the present schema:

1. Distinguish attachment leaf, whole-volume PDF position, printed page, and manuscript page in the package header. The current two-page offset and three-page transcription overlap are easy to obscure otherwise.
2. Specify that `edition_slip_kept` rows are explanatory and must never be applied automatically as source substitutions. The ledger can then retain both the literal reading and the proposed mathematical repair unambiguously.
3. State explicitly that `proof_status` describes the source’s treatment, while present status is recorded in the repair and notes fields. This avoids interpreting a historical question as a currently open problem.
4. Record the inspected version in bibliographic locators when theorem numbering changes between a preprint and the publication. The Cisinski numbering difference in this package is a concrete instance.

The provided builder checks file presence, CSV headers, anchors, block kinds, and citation keys. Mathematical correctness, full audit coverage, source fidelity, and page layout require the separate checks documented here; a successful script exit alone does not certify them.

## Attribution

The commentary and audit are **AI-produced by GPT-6 Astra (OpenAI) for this package**. The supplied brief also requests the credit “edited with Claude (Anthropic).” **No Claude review was performed in this run, so that additional editorial credit cannot be certified as completed work.** No human authorship or editorial responsibility is attributed to the commentators’ text. Grothendieck and the named electronic-edition editors retain their respective credit for the source material.
