# DER_XIIb-a: mathematical audit and commentary report

**Commentary, audit, and explicitly marked mathematical developments: GPT-6 Astra (OpenAI, ChatGPT Pro mode).** Completed 10 November 2026. This credit covers the present package only; it does not certify any subsequent assembly or editing by another system or person.

## Scope and deliverables

The audit covers all of the supplied transcription and all 40 leaves of the authoritative edition PDF: *Les Dérivateurs*, Chapter XII, section V, manuscript pages 59–122, edition printed pages 43–82. The excerpt starts with open–closed attachment data and ends at the integration/Kan-extension formula on manuscript page 122. No part of the supplied excerpt was omitted. The announced continuation reducing the general problem to closed immersions lies beyond these pages and is not reported as proved here.

The six main deliverables follow `FORMAT.md`: the commentary blocks, standalone overview, claim register, correction register, scoped bibliography, and this report. The package also contains the assembled reader in TeX and PDF, the corrected transcription used for assembly, the unchanged original transcription, the supplied build script, the adjusted companion style, reproducibility code, and the relevant verification records. The six files are usable independently of the supporting part files; those part files preserve the inputs from which the consolidated files were generated.

There are **36 commentary blocks, 198 claim records, 50 correction or confirmation records, and 17 bibliography entries**. The claim register contains 16 definitions, 2 axioms, 44 propositions, 115 claims, 15 questions, 5 remarks, and 1 conjecture. A record may keep the successive clauses of one assertion together when their hypotheses and proof are inseparable. The source-status counts are 80 proved, 23 sketched, 62 stated, 6 assumed, 11 open, and 16 false. These counts are descriptive, not a quality score for the manuscript. In accordance with `FORMAT.md`, `false` can identify a false inference even where a separately stated conclusion has a valid repair. Conversely, `open` records a question left open in the source; it does not assert that the question is an open research problem today. Present conclusions and qualifications appear in the repair, references, and notes columns.

The commentary follows the original progression, supplies full arguments at the difficult points, and keeps source text and commentary visibly distinct. Four commentary blocks are marked as developments. Their results carry `\ours` and an explicit limitation of the priority claim. The longer examples include actual hom-set descriptions, comma categories, Kan-extension values, or chain calculations, rather than an appeal to a suggestive diagram alone.

## Source comparison and the three page systems

Every source paragraph, displayed formula, diagram, footnote, doubtful reading, and existing `[sic]` flag was compared with the supplied edition. All 40 edition leaves were rendered and visually inspected. The checks were divided into manuscript pages 59–80, 81–102, and 103–122, with shared boundary leaves and the necessary preceding definitions read in both adjoining parts. Independent cross-review then checked the mathematical interfaces: initial versus final variance, the quantifiers in total asphericity, the hypotheses inherited from W(7), and the orientation of the final integration construction.

The authoritative object for this comparison was the **edition PDF**, not a facsimile of Grothendieck's handwriting. An error already present there is therefore described as a source or edition slip; the audit does not assign responsibility between the manuscript and its decipherment without evidence. The earlier-package index and cumulative bibliography were read for continuity. Only that index, rather than the earlier full commentary, was supplied. References to earlier block titles and manuscript pages consequently do not certify an independent re-audit of their full contents.

The attached PDF leaf number is the `pdf_page` field of the correction register. Here it equals the edition's printed page minus 42. Manuscript page labels are independent and sometimes begin inside a formula or sentence. In particular, the inline markers for manuscript pages 70, 89, and 95 are present; they were not treated as missing pages. The following concordance reports the manuscript material occurring on each edition leaf, including continuations.

| PDF leaf | Printed page | Manuscript pages | PDF leaf | Printed page | Manuscript pages |
|---:|---:|:---|---:|---:|:---|
| 1 | 43 | 59–60 | 21 | 63 | 88–89 |
| 2 | 44 | 60–61 | 22 | 64 | 90–91 |
| 3 | 45 | 61–62 | 23 | 65 | 92–93 |
| 4 | 46 | 63–64 | 24 | 66 | 93–95 |
| 5 | 47 | 65–66 | 25 | 67 | 95–97 |
| 6 | 48 | 66–67 | 26 | 68 | 97–98 |
| 7 | 49 | 67–68 | 27 | 69 | 98–99 |
| 8 | 50 | 69–70 | 28 | 70 | 99–101 |
| 9 | 51 | 70–72 | 29 | 71 | 101–103 |
| 10 | 52 | 72–73 | 30 | 72 | 103–104 |
| 11 | 53 | 74–75 | 31 | 73 | 105–106 |
| 12 | 54 | 75 | 32 | 74 | 106–107 |
| 13 | 55 | 75–76 | 33 | 75 | 108–109 |
| 14 | 56 | 76–77 | 34 | 76 | 109–111 |
| 15 | 57 | 78–79 | 35 | 77 | 111–114 |
| 16 | 58 | 79–81 | 36 | 78 | 114–115 |
| 17 | 59 | 81–82 | 37 | 79 | 116–117 |
| 18 | 60 | 82–83 | 38 | 80 | 117–118 |
| 19 | 61 | 84–86 | 39 | 81 | 119–120 |
| 20 | 62 | 86–88 | 40 | 82 | 121–122 |

The page numbers printed at the bottom of the new reader are a fourth, purely navigational pagination. The original manuscript and edition markers remain in its margin. Citations to the mathematical source in the commentary use manuscript pages unless explicitly qualified.

## Transcription decisions

The 50 correction records comprise **48 `edition_slip_kept` records and 2 `doubt_resolved` records**. All 25 original `% [sic]` flags were checked against the edition. The register also records additional mathematical and typographical slips found during the audit. Edition slips remain in the diplomatic body, even when the intended mathematical correction is certain. Examples include the specialization-order orientation on page 59, the unqualified universal-property displays on page 61, several missing primes and misplaced category-of-elements labels, the incorrect map named at the beginning of the page 112 proof, and the missing terminal-presheaf symbol in the page 120 direct-image argument. The two uses of “Proposition 11” are disambiguated by manuscript page rather than silently renumbered.

Both original `% ??` markers are resolved. On manuscript page 98, PDF leaf 27, the editorial bracket is `[la]`, as transcribed. On manuscript page 119, PDF leaf 39, enlarged inspection of the curved lambda arrow, supplemented by inspection of the PDF drawing stream, shows a continuously drawn shaft approximated by many small segments. The transcription's `dashed` option is removed. That is the **only change to the mathematical/linguistic content of the source body**; the two uncertainty comments are replaced with resolved-reference comments. The arrow's exact old and new TikZ commands are in the correction register. The enlarged image and drawing-stream extract are included among the evidence files. Separate layout adjustments reserve room for one deep display, widen one diagram, and move four labels away from crossing strokes; they change no wording, label, vertex, arrow, or formula.

No other source slip has been silently corrected. The original transcription is retained as `source_original.tex`, so the diplomatic decision is reproducible. Layout and language additions are isolated in the preamble, companion style, and the explicit layout replacements in `assemble_package.py`. The source-preservation check reverses those exact layout replacements before comparing content.

## Principal mathematical conclusions

### Collages, gluing, and ordinary pushouts, manuscript pages 59–75

The basic attachment description is correct. A sieve and its complementary cosieve determine a profunctor, and the category is its collage. The commentary specifies the two actions, composition, maps out of the collage, and compatible natural transformations. It also computes the pushout by an ordinary left Kan extension and proves the resulting component formula for the crossing hom-sets. The distinction between the full factorization category and its set of connected components is made explicit because it drives the later homotopical difficulties.

Two corrections are substantive. For the down-set topology used on page 59, the displayed specialization-order formula has its closure relation reversed. A walking-arrow calculation identifies the error. On page 61, the asserted unqualified representability of the induced collage is false; merely adding primes does not repair it. The correct property is a cartesian lifting over the pair of endpoint categories. The commentary gives the pullback formula for hom-sets and functor categories and a counterexample to the printed absolute formula.

The topos comparison is traced to its precise antecedent, SGA 4, Exposé IV, Exercise 9.5.10(a–c), with the surrounding gluing theorem checked (Artin et al., 1972). The converse retains the accessibility assumption on the gluing functor. The reversal of natural transformations between left and right adjoints is recorded instead of suppressing the variance in the category-level equivalence.

### The false reverse gluing principle, manuscript pages 76–80

The main finding is that **Theorem 2 on manuscript page 78 is false as stated for ordinary weak homotopy equivalences**. The forward gluing implication holds: a union of two sieves gives a simplicial union of nerves, and its inclusions are cofibrations. The reverse implication of W(7 bis), and therefore the full symmetric W(7), fail even for finite posets.

The proof uses a connected acyclic noncontractible finite complex. Its two-cell presentation, cellular boundary matrix, and a nontrivial permutation representation are written out. Hatcher's Example 2.38 and finite simplicial replacement theorem supply the classical topological input (Hatcher, 2002). Let A be the face poset of such a finite model, and adjoin two incomparable terminal cone points. The one-cone subcategories U and V are sieves, their intersection is A, and their union X realizes the suspension of BA. Both cones and the suspension are contractible, while BA is not. Thus U→X is a weak equivalence and A→V is not. This directly contradicts the reverse implication; it is not merely an objection to the sketch of proof.

The development following page 79 gives finite counterexamples for every homotopy-truncated class W≤n, using the face poset of the boundary of an (n+1)-simplex and its double cone. It also proves the exact positive result suggested by the source's Mayer–Vietoris argument: full W(7) holds for fixed-coefficient homology equivalences. The proof uses a short exact sequence of normalized chain complexes and its sequence of mapping cones. This separates the valid homological statement from the invalid unstable homotopical converse.

The later discussion of localizers in Chapter XVI, section 3, was checked for context. Its separation of the three gluing implications does not supply a proof of the false assertion for W∞. Subsequent uses of W(7) and W(7 bis) in the present excerpt are therefore retained as conditional statements. An argument made under an additional axiom was not marked false solely because that axiom fails for W∞.

### Ordinary finality and total asphericity, manuscript pages 81–102

The comprehensive factorization on pages 89–93 is correct. Its first map is **ordinary final**: each relevant comma category is one connected component of an original comma category, hence nonempty and connected. It need not be homotopy final. The commentary proves the factorization, recovery of the discrete fibration, and uniqueness with the required compatibility. Kelly's corrected account supplies an exact literature comparison with Street and Walters (Kelly, 1982, §4.7; Street & Walters, 1973). The incoming commas on page 85 instead have the variance conventionally called homotopy initial; that distinction was corrected during independent review.

One development formulates total W-asphericity as the requirement that every ordinary final target of the category be W-aspherical. It proves this criterion, closure under ordinary final images, and the corresponding largest-class characterization. These are direct consequences of comprehensive factorization, with no claim of priority.

The union argument on pages 97–100 fails because ordinary left Kan extension need not preserve the subpresheaf monomorphisms representing the cover. Categorical retractions do not provide the presheaf splittings needed for the proposed repair. The finite outgoing-fork example was reconstructed, then located in Grothendieck's Appendix XII, manuscript pages 10–12, and is attributed there. A final functor from the contractible fork Ψ=(z→a,z→b) lands in a four-object category C with BC≃S². Its exceptional comma category is a connected square. The calculation explicitly exhibits two representatives that become equal after applying a left Kan extension. A separate exact finite-chain computation verifies the nerve dimensions (4 vertices, 6 nonidentity edges, 4 nondegenerate triangles), differential ranks (3 and 3), and rational Betti numbers (1,0,1). The homotopy-type proof is given in the commentary and does not rest on those Betti numbers alone.

A further development tests the retracted assertions **under their actual gluing hypothesis**. For any nonzero commutative ring R, nerve R-homology equivalences form a fundamental localizer satisfying full W(7). The relative Theorem A axiom is proved by a bisimplicial chain resolution and first-quadrant spectral-sequence comparison; W(7) is supplied by the earlier chain argument. In this class the same fork is not totally aspherical, since its final target has H₂(C;R)=R, although its two branches and their intersection have terminal objects and the indicated categorical retractions exist. Thus the conditional union and retraction conclusions themselves fail; their failure is not inferred from W∞, which does not meet their gluing assumption.

The subterminal case of the presheaf/category-of-elements converse is proved. The general converse is left unresolved by this audit. The covering argument leading to the simple-connectivity obstruction on pages 101–102 is completed by explicit transport and a choice-independence argument.

### Good attachments, fibres, and integration, manuscript pages 103–122

The pushout failures on pages 104–107 are verified directly. Their classifying spaces are computed by cone decompositions, culminating in a space of type S³. This proves the asserted failures independently of the disputed one-point converse.

The intrinsic pushout stability of the W-Dwyer boundary-weight condition is correct and follows from transitivity of ordinary Kan extensions. Its stronger category-of-elements version uses the final first factor of the comprehensive factorization. Theorem 3's two biconditionals retain their explicit W(7 bis)/W(7) hypotheses. The source's proof begins by naming the wrong map: the aspherical map is the inclusion into the generated cosieve, with its subscript 0, rather than the whole inclusion. The diplomatic text retains that slip and the commentary supplies the corrected argument.

The inclusion of the ordered set of natural numbers into the category obtained by adding a terminal object is totally W∞-Dwyer and a couniversal weak equivalence, but it has no classical Dwyer right adjoint. For every pushout, its new slice is the category of elements of a filtered colimit of representables; the filteredness and comma-category argument are written out. Since every such pushout is already a weak homotopy equivalence, the example also works for Wℤ, which satisfies full W(7). It therefore answers the stronger classical-Dwyer suggestion negatively even if a standing gluing hypothesis is imposed. The interval pushout-product example is computed separately: the crucial four-object lower slice is contractible but has two incomparable maximal objects and no terminal object.

The proper-terminal-fibre argument is correct under its stated connectivity assumption, or with W₀-properness. The fibre inclusion is W-coaspherical; the connectivity condition makes it ordinary final. The terminal presheaf therefore has terminal direct image, and transitivity proves total asphericity of the total category. The commentary proves the component-colimit formula and constructs the natural transformation requested in footnote 83, including its action on comma objects, morphisms, target-variable maps, and composition in the index.

The final span is integrated with the manuscript's contravariant/fibred convention. The cross-fibre hom-sets and their composition are explicit. Two categorical mapping cylinders retract onto the outer categories, and their nerves form a simplicial union over the middle nerve. This proves the homotopy-pushout description. The fully worked span e←{a,b}→e has ordinary pushout e and integrated classifying space S¹. The concluding localized-diagram formula is placed under the necessary ambient assumptions; no arbitrary class of arrows is silently promoted to a derivator.

## Historical and later comparisons

The later commentary is selective: it follows the actual mathematical questions in these pages rather than attaching a generic history of derivators. The 17-entry bibliography records a URL or DOI and the exact verification scope for every item. Existing cumulative keys are reused. Where a later preprint or corrected online edition was read, that version and its numbering are stated.

The main comparisons are the SGA 4 gluing exercise; comprehensive factorization in Street–Walters, Kelly, and Berger–Kaufmann; the proper/smooth criteria in Maltsiniotis (2005); Thomason's classical Dwyer construction and Cisinski's correction of retract stability; the h-cofibration theory of Batanin and Berger (2017) and Manetti and Meazzini (2019); and the higher-categorical pushout theorem of Hackney et al. (2024). The last comparison distinguishes Dwyer maps, discretely flat inclusions, discretely flat cofibrations, and the manuscript's W-dependent condition. Weak categorical equivalences and weak homotopy equivalences are not identified.

There are two explicit access limitations. The original Street–Walters article's metadata were verified, but its full proof could not be accessed; the theorem and correction of the proof were checked in Kelly's account. Thomason's 1979 metadata were verified, and Theorem 1.2's statement and numbering were checked through Chachólski and Scherer (2001, Corollary 26.9); the original proof was not accessed. The span case used here is independently proved. These limits are recorded in the bibliography itself rather than hidden behind an unqualified “verified” label.

The supplied references to earlier packages are used by block title and manuscript page. The bare cross-reference on manuscript page 75 to “proposition 15, page 158, and its corollaries” does not identify the chapter or repeat its statements. The audit records that limitation and does not invent assertions for an unidentified reference.

## Questions not settled by this audit

The remaining limitations concern exact literature status, rather than unfinished source comparison. The search did not locate a general answer to the converse from totality of a presheaf to totality of its category of elements, beyond the subterminal case proved here. Nor did it locate an exact result settling total asphericity of the particular based-path category in the question on page 103 when its target is weakly contractible; a complete characterization of all sieve h-cofibrations by the manuscript's W-Dwyer weights; or all composition questions for the strict/total variants on pages 109–114. The report does not declare those questions currently open.

Searches checked the relevant primary treatments named above, the Appendix XII example, and the later localizer discussion in Chapter XVI. Several uses of “totally aspherical” in later test-category literature concern a diagonal/product condition rather than the quantified ordinary-image condition of these pages. They cannot be substituted for a result about the latter without a comparison theorem. Each status block and claim record states the narrower conclusion actually supported by the sources inspected.

## Reader, format, and reproducibility decisions

The supplied `build_reader.py` is unchanged. Exact textual anchors are retained for insertion, while the companion style displays only their manuscript-page component in the commentary heading. This avoids printing a long source substring in the margin label. English language selection is local to commentary, overview, and bibliography; the original French remains French. The reader adds A4 geometry with a reserved outer margin, margin-note collision handling, breakable long URLs, microtypographic adjustment, and a small emergency line-breaking allowance. Space reservations and paragraph/list penalties keep headings and proposition introductions with their opening text. A brief title and the requested model credit are added before the source. These are layout additions, not textual emendations.

Visual inspection identified defects that the ordinary TeX log did not flag. The deep boxed formula on manuscript page 72 reached into the footer; a local eight-baseline reservation moves it when necessary. The presheaf/discrete-fibration square on page 89 had a long label touching its endpoint; its columns are widened. Four vertical labels in the cubes on pages 77–78 were partly erased by crossing strokes; their positions are moved toward the beginnings of the same arrows. The overview's internal headings and commentary headings are kept with their first lines. Five missing backslashes in commentary spacing commands were corrected before the final build. The source's mathematical content is preserved by each of these changes.

The build uses the supplied author–year `plainnat`/`natbib` convention. The standalone overview has no section or chapter commands. All commentary kinds, anchors, claim kinds, status values, bibliography keys, and required CSV headers are validated. The six distinct exact-text anchors, used by seven blocks, each match uniquely on their manuscript page. The counterexample to Theorem 2 is anchored directly after its proof sketch, keeping the following remark and its displayed surjectivity condition together. `\ours` occurs only in development blocks.

For a normal TeX Live installation with LuaLaTeX, BibTeX, French and English Babel, fontspec, TikZ, framed, natbib, hyperref, geometry, marginfix, xurl, microtype, and needspace, the build is:

```bash
python3 build_reader.py DER_XIIb-a
lualatex -interaction=nonstopmode -halt-on-error DER_XIIb-a_reader.tex
bibtex DER_XIIb-a_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XIIb-a_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XIIb-a_reader.tex
```

The first LuaLaTeX run creates the auxiliary file needed by BibTeX; the two subsequent runs resolve the bibliography and references. The package already contains the resulting reader, so rebuilding is optional for reading it. To reproduce consolidation from the retained part files, run `python3 assemble_package.py` first. It re-creates the merged blocks, registers, bibliography, and diplomatic source while leaving the overview and report intact.

The working container supplied TeX's package trees but lacked usable generated formats, Lua font-loading components, French language files, and a font map. `bootstrap_tex.py` installs the required runtime components in a local tree from unmodified Debian packages, with the downloaded SHA-256 values recorded in `verification/tex_installation.json`. `build_all.py` creates a writable local cache and format and performs the complete build without modifying the system installation. Large package downloads and generated caches are not required deliverables and are excluded from the archive. The ordinary commands above remain the recommended route on a complete TeX installation.

Final build and visual-verification results are recorded in `verification/final_validation.json` and the accompanying logs. The unmodified supplied validator accepted all 36 blocks and 17 bibliography entries. The initial LuaLaTeX run, BibTeX run, and two subsequent LuaLaTeX runs all exited successfully. The final logs contain **no errors, citation/reference warnings, missing-character messages, overfull boxes, or underfull boxes**. The PDF has **56 pages**. The overview occupies reader pages **52–54**, within the required two-to-five-page span; the bibliography begins on page 54 and ends on page 56. All 17 works appear in it.

All 56 final pages were inspected at layout scale, with individual-page inspection throughout the first complete render and renewed individual inspection of the changed or technically dense regions. The entire final overview and bibliography were inspected individually. The three visual-review records state their exact scope and close every defect identified. A last anchor adjustment affected only pages 16–19, as verified by comparison of rendered-image hashes; those four refreshed pages were then checked individually. The source-preservation, schema, anchor, merge-consistency, citation, page-marker, and glyph checks all pass. The final PDF SHA-256 is `dcd80bd5e1e605c783d15eecde2d0b1017736feb01b6bb45f9e78f01b131b723`.

The package is assembled by `package_delivery.py`. Its ZIP integrity check reads every member and verifies the included per-file SHA-256 manifest. Source comparison and all mathematical conclusions remain distinct from these mechanical checks: the latter establish the completeness and reproducibility of the delivered files, not the truth of a theorem.

The supporting part notes and independent review reports preserve the scope of the individual checks. Temporary review documents, failed intermediate builds, downloaded third-party books and articles, and TeX caches are excluded from the delivery archive.
