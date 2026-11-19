# DER_XVIII-e — mathematical audit and commentary

**Credit:** AI-produced commentary, audit, proofs and reader preparation by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. No human authorship is attributed. This report does not certify any subsequent assembly or editing by Claude or by another editor.

## Scope and authority

The complete supplied transcription and all 41 leaves of the attached edition PDF were read. The PDF is the authority for readings. Its leaves 1–41 correspond to edition printed pages 159–199 and to leaves 161–201 of the complete editors’ chapter file. The main manuscript runs from 419 to 492, including 476 bis; the appended note restarts at manuscript page 1 and ends at 19. There are 94 manuscript-page markers. The page correspondence is supplied in `qa/page_map.csv`.

The initial fragment completes the proof of 4.14.24. The audit continues through 4.14.25; all of 4.15, including the section-category, fibration and small-category arguments; all of 4.16, including its conjectures, marginal retractions, questions and open–closed propositions; the notice that 4.17 contains no text; and the complete appended note on ultraproducts of fields. Definitions, subsidiary claims, counterexamples, questions and editorially recorded changes of mind have separate audit rows where their mathematical status differs. The register’s `proof_status` follows FORMAT: it records the source’s treatment, with `false` for an assertion or inference false as written. Present conclusions are stated separately in `repair` and `notes`.

Every relevant PDF leaf was rendered and visually inspected. Mathematically suspicious formulas were checked against the PDF before assigning an error to the source. The independent inventory verifies all 55 original `[sic]` flags and all four `% ??` flags: 59 of 59 are represented. The two flags on original line 1743 are counted separately. Additional unflagged edition slips have also been recorded. `qa/flag_coverage.csv` gives the explicit correspondence rather than an unreliable fuzzy-text match; its JSON summary distinguishes this documentary check from the substantive mathematical audit.

No mathematical discrepancy between the supplied transcription and the supplied edition was found in the inspected passages. Numerous mathematically incorrect formulas are already present in the edition. They remain in the French text. The sole machine-marker normalization changes `476 bis` to `476bis` so that the unmodified builder recognizes the page; this is recorded as a mechanical transcription correction. The four uncertainty comments are replaced by the verified reading without changing their formulas. Any additional typesetting-only changes required by the integrated build are enumerated in `qa/source_edits.json` and do not emend an edition slip.

The supplied `index_earlier.md` ends at `DER_XIIapp` and contains no earlier Chapter XVIII entries. We therefore could not compare against unavailable XVIII-a–XVIII-d commentary or certify nonduplication of those overlaps. The supplied mathematics is nevertheless audited throughout. We refer to earlier material only when it is actually present in the supplied text or index; no missing commentary is invented.

## Conventions which affect the conclusions

Grothendieck’s indexing categories *grand devant* an infinite cardinal π are modern π⁺-filtered categories: the source permits diagrams with **at most** π arrows. His π-ultrafilters are correspondingly π⁺-complete ultrafilters. Every comparison with regular-cardinal accessibility and large-cardinal compactness states this successor shift.

“Accessible in M” means accessible and accessibly embedded in M. Abstract accessibility alone would not justify the inverse-image arguments. Full subcategories are taken replete when essential images are involved. “Open” and “closed” mean sieve and cosieve. They do not introduce a topology on an object space. Strict pullbacks are not replaced by pseudopullbacks without an isomorphism-lifting argument. The results depending on the appendix’s universe assumption also require an infinite field k with |k| at least the stated ultrafilter cutoff π₀.

## Principal results and repairs

### Gluing and total categories, manuscript 419–440

Corollary 4.14.25(1) omits the existence of the relevant filtered colimits in the closed fibre. The disjoint union of a point with the one-object unsplit-idempotent category `{1,p}` satisfies the printed mixed-Hom condition but lacks those colimits. The corrected two-fibre criterion is proved.

The numerical conclusion in 4.15.2(c), and consequently (d), fails under the printed rank assumptions. The commentary gives a complete example with π₀ = ℵ₀, π₁ = π = 2^ℵ₀ and mixed Hom functor `Set(P_{≤π} A, B)`. A set of size π is presentable in the fibre but fails the required presentability test in the collage. The repair is to choose the initial rank at least as large as all transition-functor ranks before making the subsequent enlargement. The existential theorem 4.15.1 remains valid.

Categories of sections are explicitly constructed with products, inserters and equifiers, including their equations. Proposition 4.15.6 is proved for both fibrations and opfibrations over a small Karoubian base. The proofs establish colimit existence and both directions of the Hom-colimit comparison. A final index is treated before the constant-idempotent argument; one cannot introduce identity transitions by multiplying the index after normalization and continue calling every strict transition p.

### Small categories and projectors, manuscript 441–463

The essential-constancy criterion is proved with correctly typed compositions, coherent splittings, and an explicit upper-slice finality argument. The thinning to a single projector is final as a functor; it need not be a full subcategory of the old index. The transfinite growth argument includes limit stages and the injectivity needed to retain newly added elements.

The literal condition `=1` on a whole tail in 4.15.9(b) is false even for the group of order two. A naturally constant group-valued diagram can have arbitrarily late nonidentity transition arrows. Eventual invertibility, followed by trivialization or a suitable cofinal subsystem, is the correct invariant assertion. A logically separate reduction constructs a quotient of a **submonoid**, whereas the theorem’s wording quantifies only over quotients of the original endomorphism monoid. The proof supplies a sufficient subquotient criterion, not that sharper equivalence.

The substantive strict-bound theorem survives: when π exceeds the total morphism cardinal of C, `Ind_π(C)` is its Karoubi envelope. Both the source’s counting argument and an independent presheaf proof are supplied. The equality boundary is proved under a stricter local Hom bound and for two-sided cancellative endomorphism monoids. The completely unrestricted equality boundary is not settled here; we do not label it a recognized open problem on the basis of a bounded search.

### Images, density and existing colimits, manuscript 464–473

The double-dual functor `X ↦ J^(I^X)`, with its double-precomposition action, fails accessibility at every regular rank when both coefficient sets have at least two elements. The worked proof constructs a functional with no bounded support.

At a common strong accessibility rank κ, the full κ-filtered-colimit closure of the image of an accessible functor is the embedded `Ind_κ` completion of the full category on its κ-presentable image objects. The commentary proves this by the Hom limit–colimit formula. The category of generators must contain exactly those image representatives; arbitrary extra compact objects would spoil minimality.

Under the appendix’s universe hypothesis, these closures need not eventually stabilize. The forgetful functor from pointed k-algebras supplies the covariant example. A separate construction using the contravariant functor `E ↦ k^E` supplies the contravariant example, including the necessary zero-algebra exception for the empty product. Accessibility of an individual fixed contravariant closure is not inferred from either argument.

The stronger density question at p.471 also has a conditional counterexample. Inside the presheaf category on finite free k-algebras, take the cosieve with no map to the nerve of k and adjoin all retracts of representables. The resulting category has a small dense family of presentable objects and sufficiently filtered colimits, but remains nonaccessible. The size calculation and the argument recovering accessibility of the forbidden cosieve from a hypothetical presentation are given in full. This addresses the hypothesis which the manuscript’s initial counterexample did not preserve.

Isbell’s category of partial bijections refutes all three smallness assertions in 4.16.4 without additional set-theoretic assumptions. Its filtered colimits, finite presentability, self-duality, and the full faithfulness of the restricted nerve at a two-element set are proved explicitly. The historical attribution is checked in Avery and Leinster’s Example 8.7; the original Isbell article is not represented as directly inspected.

The assertion that all *existing* colimit cocones form an accessible subcategory fails under the appendix hypothesis. We construct a finitely accessible collage by adjoining an object `*` to k-algebras with `Hom(A,*) = Hom_k(A,k)`. A specified square with vertices `k, A×k, *, *` is a pushout exactly when A has no k-point. Pulling back a hypothetical accessible pushout class would make the nonaccessible no-point cosieve accessible. This gives a complete counterexample for 4.16.5. The positive theorem when all diagrams of the fixed shape have colimits remains valid. The separate implication from an accessible pushout class to accessibility of epimorphisms is also verified.

### Relative accessibility, manuscript 473–476 bis

The Q and Q′ finite-test assertion of 4.16.6.1 is proved. The first test supplies a colimit after splitting the recurrent base idempotent; the second supplies the factorization and eventual equality required for presentability. Common strong ranks are chosen for a small family of tests and fibre inclusions.

Condition b′ of 4.16.6.2 is false for arbitrary functors. The functor from a point selecting one object of the walking isomorphism passes every arrow test. Its strict pullback along the walking split idempotent is the unsplit monoid `{1,p}`, hence is not accessible. A nonidentity projector in a test base may map to an identity in C. The unrestricted Q and Q′ tests must therefore be retained.

For a small Karoubian C, the intended universal strict-base-change property is proved equivalent to: E is accessible, `E → C` is accessible, and `E → C` is an isofibration. Necessity uses splitting of the projector `(1_x,p)` in a walking-retract pullback. Sufficiency identifies strict pullbacks with accessible iso-comma categories. Both projections are accessible. This answers 4.16.6.4 and the intended small-base version of 4.16.6.5. The proposed definition for a general nonsmall base is kept separate.

### Cosieves, long sequences and fields, manuscript 477–492

The small-union criterion, the small weakly initial family criterion, and the no-forward-morphism construction are justified without assuming an unbounded global choice of representatives. An accessible category over `V_θ` has a skeleton of size at most θ; this is the bound needed for the transfinite construction. The canonical slice of presentables over x proves 4.16.7.8–12 and repairs the edition’s omitted or incorrect slice denominators. In particular, a cosieve is accessible precisely when its complementary sieve is closed under sufficiently filtered colimits.

The field-only question at p.485 has an exact universe-relative answer. For `U=V_κ`, there is a κ-long sequence of fields with no homomorphism from an earlier to a later term **if and only if κ is not a Vopěnka cardinal**, where all external subsets of `V_κ` are allowed as families. The proof uses Morleyization and an explicit bipartite incidence graph with two odd-cycle tags at each typed vertex. Every induced graph embedding then yields an elementary embedding. The cardinal-preserving fully faithful graph-to-field functor gives characteristic-zero fields with no maps between any distinct terms. At a Vopěnka boundary the reverse implication follows by thinning to increasing cardinalities. The field sequence exists in the first inaccessible universe. This is a deduction supplied in the commentary, not a claim that the original k-algebra argument already answered the question.

### Appendix, manuscript 1–19

The reduced-product quotient, its field criterion, and the ultrafilter–maximal-ideal correspondence are proved, including the order and variance conventions. For infinite k, triviality of an ultrapower is equivalent to |k|⁺-completeness of its ultrafilter. A nonprincipal sufficiently complete ultrafilter yields a measurable cardinal above the cutoff; the inaccessibility argument is included. Proposition 4’s universe hypothesis holds exactly when the measurable cardinals below the inaccessible boundary are bounded. The proposed cutoff outside all smaller universes works when it exists; it need not exist if smaller inaccessible cardinals are cofinal.

The main-text open–closed criterion completes the implication abandoned in appendix Proposition 4(b). A direct proof also settles the final suggested construction. For every infinite π ≥ |k| ≥ π₀, the reduced power

`A = k^(π⁺) / {f : |supp(f)| ≤ π}`

has no k-point under that hypothesis, but every subalgebra B of size at most π has one. Choose representatives of B and evaluate outside the union of the at most π exceptional supports on which algebra identities fail. Thus no eventual small-obstruction bound exists under the stated assumption.

For every infinite field, without that universe assumption, the localization `k[x_j : j<|k|⁺][(x_i−x_j)^−1 : i≠j]` disproves the proposed bound π = |k|. This does not rule out larger bounds in other universes. A sufficiently large `L_(|k|⁺),ω`-compact cardinal, in particular a sufficiently large strongly compact cardinal, restores a uniform obstruction bound by a complete-ultrafilter argument. For finite fields the ordinary ultrafilter lemma gives a finitely generated obstruction. No exact weakest large-cardinal equivalence for the fixed-field problem is claimed.

## Literature, provenance and limits

The bibliography reuses supplied keys where available. Every entry has a URL or DOI and a verification note identifying the version and the actual scope inspected. Original proofs, statements, indirect attributions and metadata-only checks are distinguished. The main primary sources are SGA 4 I; the author-hosted Ching–Riehl appendix; Paré–Rosický’s preprint; Tendas’s published paper; Lurie’s author-hosted book; Avery–Leinster’s published example; the published Bourke–Lack HTML passages; Keisler’s author manuscript; Brooke-Taylor–Rosický’s accepted manuscript; the graph-to-field paper; and Brooke-Taylor’s Vopěnka preprint.

The original Makkai–Paré book proofs were not available for direct inspection. The relevant theorem formulations and attributions are checked through the stated primary papers. Bird–Kelly–Power–Street is used for historical context on the basis of its metadata and abstract. Stone and Ulam have metadata-only verification and no unverified theorem numbers; their particular consequences used here are proved in full. Isbell’s attribution is indirect through Avery–Leinster. Bourke–Lack numbering refers to the published version, whose Examples 4.8 and Remark 4.9 differ from arXiv v2. The graph-to-field argument’s use at arbitrary cardinality includes the finite-support explanation needed for its real-specialization proof.

All mathematical developments marked `\ours` are complete deductions or constructions for this commentary, accompanied by the literature scope checked. No priority claim is made. The archive does not claim a complete survey of all literature through the current date. In particular, the unrestricted small-category equality boundary, accessibility of each fixed contravariant closure, and the exact weakest compactness principle for the fixed-field obstruction problem remain outside the conclusions established here.

## Reproduction and verification

The six requested files are at the archive root, with the generated reader source and PDF, corrected machine transcription, and the unmodified kit builder and style. Source attachments needed to repeat the documentary audit are under `source/`; generation, assembly and validation scripts and their small input parts are under `code/`. Intermediate renderings and downloaded TeX packages are omitted. No proprietary or inaccessible library is needed to read the completed PDF.

On a working TeX Live installation with LuaLaTeX, French and English Babel, fontspec, TikZ-cd, framed, natbib, marginfix and needspace, run from the extracted archive directory:

```bash
python build_reader.py DER_XVIII-e
lualatex -interaction=nonstopmode -halt-on-error DER_XVIII-e_reader.tex
bibtex DER_XVIII-e_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XVIII-e_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XVIII-e_reader.tex
```

The supplied environment had LuaLaTeX binaries and a substantial read-only TeX tree but broken configuration links and missing LuaTeX/French support. `code/recover_tex.py` records the workspace-only recovery, exact Debian package URLs and SHA256 checks. It is an optional environment-specific repair, not a general installation script. A normal TeX installation should use the commands above directly. Portable instructions are included with the code.

The final integrated build and visual checks are recorded below after compilation. The format change proposed for future kits is narrow: normalize spaced `bis` page markers in the builder itself, and permit an explicit source-versus-commentary language configuration. Neither requires silently repairing the edition’s mathematics. The supplied builder and style are retained unchanged in this deliverable.

## Final integrated build record

The completed reader has **103 pages**. Its overview occupies reader pages **96–99**, four pages including the last page shared with the bibliography. The bibliography begins on page 99 and ends on page 103. The final build uses the supplied `build_reader.py` and `derivateurs_companion.sty` without modification.

| Checked item | Final result |
|---|---|
| Commentary | 48 blocks in all six permitted kinds; approximately 20,200 whitespace-delimited TeX words |
| Developments | 12 development blocks containing 14 result markers `\ours` |
| Claims register | 222 rows, with unique identifiers and the required columns |
| Corrections register | 135 rows: 129 retained edition slips, 5 resolved doubts, 1 machine-marker normalization |
| Original flags | All 55 `[sic]` and all 4 `% ??` flags covered; 59/59 |
| Page inventory | All 41 PDF leaves and all 94 manuscript markers agree with the transcription |
| Bibliography | 17 cited keys, 17 rendered entries, each with a verification note and URL or DOI |
| Final LuaLaTeX diagnostics | No errors, warnings, missing glyphs, unresolved citations/references, overfull boxes or underfull boxes |
| BibTeX diagnostics | No warning or error |
| PDF geometry | No off-page text and no overlapping marginal page labels detected |
| Visual inspection | Every final reader page, 1–103, rendered and inspected |

The final reader's SHA256 is
`46def361c445c040eb7016e3f8c444db2186139feba860c7b087421a86e14798`.
The final reader TeX source's SHA256 is
`4579e6b3fec8372d75e6c8479708747b4ce8016a605dc0313c93c8ddd29f7412`.

Three final visual records cover pages 1–34, 35–68 and 69–103 respectively, all against this exact PDF hash. They supersede the earlier 102-page snapshot reviews, which are retained only as historical QA records. The final checks specifically include the commentary-heading repair on pages 26–27, the complete pushout diagram and proof continuation on pages 57–58, the Q and Q′ diagrams on page 59, the appendix formulas, and the complete overview and bibliography. No required visual correction remained.

The build repairs preserve the source's mathematical readings. They retain the original math-font encodings through fontspec's `no-math` option, place the degree sign of a condition label in a text-font box, replace one invalid nested AMS display by a labelled text row, fit four wide displays using the kit's existing macro, reduce one diagram's column spacing, prevent marginal-label collisions, reserve space for a commentary heading and its opening lines, and set the bibliography in English. The exact substitutions are recorded in `qa/source_edits.json`; the original attachment is separately preserved under `source/`.

The archive's source-only reconstruction was run in a separate directory. All six required files, the prepared transcription and the generated reader TeX were reproduced byte for byte; the comparison is recorded in `qa/reproduction.json`. The final compilation products and diagnostic logs are retained. `bash build.sh` repeats assembly, the supplied builder, LuaLaTeX, BibTeX, two further LuaLaTeX passes, source-flag inventory and structural verification. The SHA256 manifest and ZIP content checks cover the packaged files.

These checks establish documentary coverage, reproducible assembly, citation resolution and a clean rendered reader. They do not constitute a machine-checked proof of the mathematics. The mathematical conclusions, their hypotheses and the limits of the literature checks are stated in the commentary and in this report.
