# Audit report: Chapter XI and Chapter XII, sections I–IV

**Commentary and mathematical audit: GPT-6 Astra (OpenAI, ChatGPT Pro mode).**

This report concerns the contribution delivered in this package. It does not certify any later assembly or editing with another system.

## Scope and pagination

The entire supplied transcription was read and checked against all 52 leaves of the attached edition PDF. The mathematical text occupies Chapter XI, manuscript pages 127–136, and Chapter XII, manuscript pages 1–58. Chapter XI has two preliminary leaves and six numbered edition pages; Chapter XII has two preliminary leaves and 42 numbered edition pages. The attached package therefore contains XI edition leaves 1–8 and XII edition leaves 1–44, with preliminary leaves included.

The three number systems have been kept separate. The corrections register uses the 1-based leaf number in the combined attachment. The claims register qualifies manuscript pages by chapter. Commentary anchors use the supplied manuscript markers and exact words. The edition's explicit statement that Chapter XI has no manuscript pages 1–126 is retained. The prompt's shorthand “manuscript pages 1–136” must not be read as one uninterrupted sequence.

The contribution index supplied with the kit was consulted to avoid repeating earlier explanations. The reader refers back to earlier discussions of the free fibration, the fork obstruction, and the path-category constructions. Where the present argument depends on material beyond this extract, that material has either been checked at its exact source or explicitly retained as a dependency.

## What the audit establishes

### Chapter XI

The characterization of Hot-fibrations in Theorem 1 is valid. Its universal quantifiers are essential: the degree-zero condition must also apply to locally constant coefficients on a base-changed total category. The comma-category comparisons and the abelian Leray comparison have been expanded without adding unnecessary boundedness assumptions.

The displayed nonabelian obstruction argument is not correct as a general fixed-band exact sequence. The band of a component of the torsor groupoid is determined by automorphisms of the represented torsor and can differ from the printed direct-image group. The commentary supplies a direct countercheck with a transposition subgroup of S3, then replaces the obstruction argument by a complete descent argument for the groupoids of torsors on X/y. Universal H0 supplies full faithfulness, R1 supplies essential surjectivity, and the fibre formula supplies objectwise base-change equivalences. The claimed conclusion survives.

Theorem 2 is valid. Its sufficiency proof receives the missing local torsor-descent explanation. Necessity follows either from homotopy-fibre invariance or from a contractible replacement. An independent replacement is obtained from Thomason's model-category factorization, with strict pullback control supplied by Ex²N and right properness of simplicial sets. This proof does not presuppose the derivator under construction.

### Chapter XII, sections I–II

The minimal-localizer conjecture is resolved by Cisinski's later work. The bibliography distinguishes the 2004 theorem for full fundamental localizers from the 2006 theorem for weak fundamental localizers. The latter is a minimality theorem: it does not assert that every weak fundamental localizer satisfies relative theorem A.

The source's nondegeneracy argument contains the component-restriction gap acknowledged by its own footnote. The development “A fibre criterion that avoids component restriction” gives a complete repair under the weaker absolute theorem-A hypothesis. A missed component produces an empty homotopy fibre. Identified components produce a disconnected aspherical fibre; the diagonal of that fibre into its square again has an empty homotopy fibre. Absolute theorem A then collapses the class to all functors. Combined with the perfect path replacement and the iterated loop argument, this proves the claimed dichotomy under the weakest perfect-fibre test.

The path construction is not justified by assuming that dichotomy. The categorical fixed-type contraction, terminal path type, and explicit lift-category comparisons were checked first in Chapter VII, manuscript pages 152–171, edition pages 95–107. The finite contraction left unwritten there is supplied. These comparisons establish the necessary perfectness for the minimum Wω before the later equality Wω=W∞ is invoked.

The truncation examples are correct after their precise interpretation is restored. The classes Wn satisfy the localizer axioms, but fail the strong fibre tests. The alternative connectivity classes W′n lose two-out-of-three. The group-cokernel formula for the component set of a homotopy fibre is false in degree zero without a pointed-set/orbit interpretation; an explicit S3 action-groupoid example shows the difference. The opening equality inference for a derivator's localizer also needs nondegeneracy, as the terminal derivator demonstrates.

### Chapter XII, section III

The properness and smoothness arguments were checked with their variance and exact localizer hypotheses. Their lift-category criteria, universal base-change assertions, and composition proofs are valid. In particular, the apparent use of Proposition 5 during the proof of composition is not circular: Proposition 5 uses independently established base-change stability.

The proposed edge-only construction of functorial transport on manuscript page 36 is false. The development “An eight-object obstruction to edge transport” provides a finite poset over [2]. Its fibres each have two contractible components, and all six functors [1]→[2] give pullbacks with equivalent endpoint inclusions. The 01 and 12 transports preserve the two component labels, while 02 exchanges them. Thus transport does not compose. The nerve of the total category is exactly an eight-cycle, giving a negative answer to the pseudofibration question on page 40.

The successful eight-condition theorem is justified by adding universal preproperness or prelissity. Its contraction argument has been made explicit through a finite zigzag of families obtained from natural transformations of indexing functors. This proves membership in W directly and does not infer a zigzag of W-maps merely from an abstract isomorphism in the localization. The more general localization argument is read with its actual saturation hypothesis. Cisinski's automatic strong-saturation result applies to the full relative axiom W(2), which Theorem 3 explicitly assumes.

### Chapter XII, section IV

The changing labels of the fibration axioms have been tracked by content. The original proof status of anticipated implications remains distinct from the later classification. The homotopy-colimit comparison is expanded into an adjunction and Yoneda argument, with strict-pullback and integration identifications listed as actual dependencies.

The final Proposition 3 is false under its printed hypotheses. A strictly Cartesian inclusion of split fibrations over [1], from the edge o→a to the fork o→a, o→b, has perfect discrete fibre maps. Its pullback over o→b has fibres e and the empty category, so the total functor is not a pseudofibration. The preceding paragraph mentions additional structural W-fibration hypotheses that the proposition omits.

The development gives a sufficient repair for that preceding fibrewise-perfect situation: structural transports in W, smooth fibrewise W-fibrations, and W(4a) plus W(4b). Its proof controls relative-fibre transport and then the under-comma transitions. The audit does not assert that adding only structural W-fibration hypotheses proves the entire printed proposition. Rezk's later gluing theorem is compared with this issue only under its explicit homotopy-Cartesian square hypothesis; a weak equivalence between total-space models alone does not transfer a strict-pullback property.

## Transcription decisions

Every original uncertainty marker and every original sic marker has been checked against the edition. The marker-to-register concordance is supplied in the audit folder.

There is a genuine arrow error in the supplied transcription on PDF leaf 32, XII manuscript page 27. The identity between the two copies of y1 points left in the edition; the supplied TikZ row had a headless rightward dash. The corrected text restores the printed direction. On PDF leaf 40 the ambiguous a in a0 is text italic, with a mathematical subscript; the corrected text matches the edition's fonts. The two uncertain editorial brackets are regular typewriter, not bold. The three uncertain references on PDF leaf 46 are all a′.

The edition's own slips remain in the French text, including incorrect variable names, arrow directions, misspellings, and already bracketed editorial repairs. Proposed intended readings appear only in the corrections register and commentary. The resolved uncertainty comments are replaced by audit comments. The original attached transcription is preserved in the inputs folder, and the assembly script makes the two substantive transcription changes reproducibly.

## Literature and limits of verification

The bibliography records verification at the level actually reached, including theorem numbers and the version read. Primary sources inspected include Thomason's original article; Quillen's original scan; Cisinski's 2004, 2006, and 2009 texts; Maltsiniotis's 2005 article and 2011 preprint of the 2012 exact-square article; Groth's published 2013 article; Rezk's author preprint; the relevant Chapter VII pages; the introductory portion of Pursuing Stacks §69; and §1 of the 2 April 1991 letter to Thomason.

Giraud (1971) was verified for publisher metadata and contents only. It supplies historical framework for bands and gerbes, not a falsely certified numbered repair theorem. Chapter VII was checked only over the explicitly cited dependency, not in its entirety. The manuscript's recollection of precisely which unpublished Pursuing Stacks arguments used which axioms has not been independently certified. The earlier companion's index was available; the earlier companions themselves were not silently treated as newly verified sources.

The three development blocks contain deductions with complete proofs and bounded statements of the literature examined. No priority claim is made. The finite examples were not located in the inspected treatments; that is not a claim that no equivalent example exists elsewhere. The weak-versus-relative localizer distinction is retained. No assertion that an exact weakened problem is currently open is inferred merely from failure to find a result.

## Reader and reproducibility

The six required files are accompanied by the integrated reader source and PDF, the corrected transcription, the unmodified supplied build script, the companion style, the original format specification, original input transcription, contribution files, verification records, and substantive scripts used in the audit.

The reader uses A4 geometry with room for the original margin page markers, English hyphenation for commentary and overview, and French for the source. The companion style prints only the manuscript page in each commentary header; exact word anchors remain in the machine-readable files. A separate Chapter XII title leaf, space reserved before commentary headings, and deferred placement of marginal notes prevent crowded transitions and overlapping source markers. One five-column source diagram has narrower column spacing. An explicit Latin Modern bold-math alphabet mapping restores the printed bold Delta without changing its mathematical input. These are presentation changes. They do not alter the French mathematical assertions. Bibliographic keys are deduplicated while preserving the precise verification scopes of the reviews.

The local environment contained LuaHBTeX but lacked its usable format, French language files, and several font components. Reproducible workspace-only setup scripts are included. Standard installations can use the supplied build commands directly. The proof checks and final build results are recorded below after integration.

## Final validation

The completed reader has 73 pages. The overview occupies reader pages 69–71, within the requested two-to-five-page range; the bibliography begins on page 71. The six required deliverables are complete.

| Item | Final result |
| --- | --- |
| Commentary | 57 blocks: 38 exposition, 3 later, 9 examples, 1 context, 3 status, 3 development |
| Commentary length | 17,299 whitespace-delimited source tokens; mathematical TeX is included in this reproducible count |
| Claims register | 324 entries: 40 definitions, 26 axioms, 56 propositions, 163 claims, 19 remarks, 11 questions, 9 conjectures |
| Source proof-status register | 124 proved, 35 sketched, 90 stated, 43 assumed, 12 conjectured, 11 open, 9 false |
| Corrections register | 79 records: 72 edition slips retained, 6 doubts resolved, 1 transcription error |
| Original editorial markers | All 28 sic markers and 6 uncertainty markers accounted for; no unresolved uncertainty marker remains |
| Bibliography | 16 distinct keys; 13 reused from the cumulative bibliography and 3 added |
| Required build | Supplied build_reader.py, LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX: all five commands exited successfully |
| Bibliographic checks | No BibTeX warnings; no undefined citation or reference |
| Final typesetting checks | No errors, missing glyphs, overfull boxes, rerun requests, out-of-page text, overlapping margin labels, or Type 3 fonts |
| Visual review | Every page inspected in current-build contact sheets; pages 3, 15, 50, 67, 68, and 71 also inspected at full resolution |

The proof-status counts describe the source's treatment, with modern resolutions and repairs recorded in their own fields. In particular, an entry marked open or conjectured does not assert present-day openness. The nine false entries include specific notation and inference defects as well as false assertions; they do not mean that nine principal theorems fail.

One nonfatal underfull-box diagnostic remains in a preserved typewriter editorial paragraph. It produces no observed clipping, overlap, or lost text. The intermediate margin-label collision was corrected and the final 73-page rendering reviewed again. Intermediate review records are explicitly marked as superseded; the final review records identify the actual PDF by its SHA-256 digest.

Register validation found no duplicate identifiers, malformed rows, invalid statuses, unresolved placeholders, control characters in fields, missing bibliography keys, or bibliography entries without a URL/DOI and verification-scope note. The insertion checks place all 57 commentary blocks outside protected source environments and preserve the corrected source text. The finite examples were checked by the included combinatorial scripts, including exact rational homology and transport-component calculations for the eight-object poset. These computations support the fully written mathematical proofs.

The package includes the build logs, marker concordance, final validation records, reviewed source contributions, visual contact sheets, and SHA-256 file manifest. The original attachments remain available in the inputs folder. The bibliography and downloaded-source manifest give the provenance of external primary sources without redistributing their PDFs.
