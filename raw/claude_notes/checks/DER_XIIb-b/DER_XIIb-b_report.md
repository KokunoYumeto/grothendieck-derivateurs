# Les Dérivateurs, XII.5, part 2: audit and commentary report

**Commentary and audit produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 10 November 2026.** This credit concerns the present work. It does not attribute the commentary to a person or certify any subsequent assembly or editing with Claude or another system.

## Delivery and scope

The package contains the six files required by `FORMAT.md`, the assembled `DER_XIIb-b_reader.tex` and its PDF, the corrected buildable source, and the code used for assembly, mathematical checks, source repair, rendering, and validation. The supplied `build_reader.py` is included unchanged. The reader has 54 pages. Its overview occupies three pages, including the last page shared with the beginning of the bibliography.

| Component | Completed content |
| --- | --- |
| Commentary | 28 blocks: exposition, context, later developments, examples, status, and development |
| Audit register | 156 entries: 154 source assertions and two separately identified commentary propositions |
| Correction register | 34 entries: 30 edition slips retained, three doubtful readings resolved, and one broken transcription macro repaired |
| Bibliography | 13 entries, each with a URL or DOI and a specific verification note |
| Source markers | All 55 manuscript-page markers preserved |
| Source annotations | All 13 existing `% [sic]` comments preserved; all three `% ??` comments resolved |
| Reader build | Supplied builder, LuaLaTeX, BibTeX, and two further LuaLaTeX passes completed successfully |

The attached PDF is the reading authority. All 37 leaves were inspected as images, with enlarged inspection of the doubtful curved arrows. They carry edition printed pages 78–114 and manuscript pages 115–169, together with the opening continuation from manuscript page 114. The printed page number, manuscript number, and attached-PDF leaf are different systems. `review/page_map.csv` records the PDF leaves, printed numbers, and manuscript-page starts. A manuscript page can span two PDF leaves; that table records starts, not exclusive ranges.

The LaTeX transcription was read throughout. The source comparison was divided across leaves 1–13, 14–27, and 27–37, with the boundary text read in context. The audit of the cube corollary beginning on manuscript page 132 and ending on page 133 appears once, as `XIIb-b-B001`. The original attached TeX and PDF are retained in `inputs/`. The supplied text itself notes the absence of a manuscript page 170; this package ends at 169 and makes no claim to audit an unavailable continuation.

The editors' complete Chapter XIIb PDF was additionally consulted for the antecedent definitions of W(7 bis), W(7), and total asphericity on manuscript pages 75–78 and 88–89. This contextual reading is identified separately from the audit of the attached leaves. The statement earlier in the chapter that W∞ satisfies full W(7) lies outside the attached range; its failure is discussed because it changes how the present conditional results can be applied.

## Continuity with earlier packages

The supplied `index_earlier.md` ends at DER_VII-a. It contains no preceding XII package. We therefore cannot certify that the overlap with XIIb-a has already been commented on, or that no duplication with that unavailable commentary exists. We did not invent such coverage.

Where the supplied index does give relevant earlier material, the historical block refers to its actual titles: DER_VI-b, “Integration and the geometry of a family”, and DER_VI-c, “Integration and the geometry of coefficients”. The new discussion concerns the use of integration for gluing, the precise transition arrows, the comparison map, and the excision hypotheses. Cross-references within this package use the final titles of actual blocks.

## Mathematical results and repairs

### Proper families and total asphericity

The component formula and its presheaf version are valid with the connectedness hypothesis made explicit: W₀-properness is sufficient, and W-properness suffices under W(5). The commentary proves the colimit-of-components formula directly from its generators and relations, then checks naturality in the object of the target category. The mate requested in footnote 83 is represented by the functor

\[
(x,a:y\to p_i x)\longmapsto(\alpha_*x,\lambda_xa).
\]

The proof checks morphisms, variance, naturality, and composition. The terminal-base-object argument then proves Proposition 11 and its product corollary. This is an ordinary left Kan extension of set-valued presheaves, so the proof cannot be replaced by an assertion about the homotopy type of the total category.

A marked development proves the distinction is essential: **total W∞-asphericity in this chapter's sense is not invariant under weak homotopy equivalence**. The finite disk-to-sphere construction described below gives a functor whose relevant comma categories are all connected. After taking opposites, the left Kan extension of the terminal presheaf becomes terminal on a category with two-sphere classifying space. The domain is nevertheless contractible. The terminal category itself is totally aspherical because the corresponding Kan extensions are representables.

### Integration and excision

The smooth integral is described by objects, every mixed Hom-set, and composition. Its functor-out universal property includes noninvertible natural transformations. The comparison map for a strict cocone is then defined on arrows, including its identity values on the chosen cartesian transitions. This supplies the construction requested in footnote 87.

The two full closed pieces of the smooth integral form a strict pullback and pushout. Their outer-fibre inclusions have explicit right adjoints. The nerve of this closed cover gives a complete proof of the homotopy-pushout calculation needed for the span. The proper integral is written out with the reverse mixed-arrow convention and the corresponding left adjoints. These proofs keep the lax square separate from its strict closed-cover replacement.

**The full W(7 bis) and W(7) are stronger than ordinary weak-homotopy gluing.** The conditional propositions in the source remain valid. The failure occurs when their converse implications are applied to W∞ after omitting, or incorrectly claiming, the strong hypothesis.

The commentary proves that reverse closed-cover excision forces every connected integrally acyclic category to be W-aspherical. For W∞ this is false. A finite presentation complex has cellular boundary matrix

\[
\begin{pmatrix}1&-1&-1\\-1&2&-1\\-1&-1&4\end{pmatrix}
\]

of determinant −1 and a nontrivial permutation quotient of its fundamental group. It is acyclic and noncontractible. A finite simplicial replacement supplies a finite face poset. Adjoining two initial vertices gives two contractible closed cones with contractible union but noncontractible intersection. The proof uses the standard suspension, Hurewicz, and Whitehead arguments; the specific matrix and permutation representation are independently checked in `partA_math_checks.py`. Hatcher (2002, Example 2.38, Theorem 2C.5, and Corollary 4.33) was checked for the supporting topological constructions and implications.

For integral homology equivalences, the normalized nerve chains of a closed cover form a short exact sequence. Its homology sequence proves all three implications of the homological cube assertion. This identifies the valid content of the five-lemma intuition and the exact extra step that fails for weak homotopy equivalences. The commentary does not relabel Proposition 13 or its correctly qualified corollaries as false.

### Opposites and the four comparison maps

The chosen convention for Σ is given explicitly, including both projections and their split-fibration description. The asphericity proof checks slices, not just the existence of weakly contractible object fibres. Applying Σ to diagrams and then integrating yields the claimed comparisons in the localized diagram category.

The deferred coherence check on manuscript page 143 is completed. If η is the natural comparison with the objectwise opposite operation, then η on the opposite diagram is its inverse. Naturality identifies the two routes around the four-comparison square. Writing proper integration as opposite–smooth integration–opposite identifies its direct edge with the opposite of the inverse smooth edge. Cancellation then proves route independence and transitivity, including for the expanded indexing diagrams and arbitrary small shapes. This proof is marked as a commentators' development, without a priority claim.

The indexing category Γ is a free diamond followed by a cocone vertex. Its two paths are identified only after composition to the cocone target. The manuscript's parenthetical identification with an ordered square is therefore false, as its footnotes already recognize. Optional central inclusions are additional generators; natural transformations are not imposed as false equalities in the ordinary indexing category.

### A finite answer to manuscript pages 145–146

The requested phenomenon is proved affirmatively for W∞, even with a sieve leg. A seven-triangle collapsible disk maps simplicially to the boundary of a tetrahedron. Let E and S be their nonempty face posets. Every comma category E/s is nonempty and connected, while E/{n} is a circle. Adjoin an initial object to S and form a mapping-cylinder poset B containing E as a sieve. An explicit adjunction makes B contractible.

The categorical pushout P = B ⨿ₑ e has two incomparable minimal objects below S. Its nerve is the join of a two-point set with the subdivided tetrahedral boundary, hence its classifying space is S³. The proof verifies the categorical universal property: the mixed arrows from the collapsed object to s are exactly π₀(E/s). It does not substitute a topological quotient for the categorical pushout.

E has 25 objects, S has 14, B has 40, and P has 16. All three categories of the original span B ← E → e have contractible nerves, so its smooth integral is contractible. Its comparison to P is not in W∞, whereas the composite with P → e is. The twelve elementary collapses, all fourteen connected comma categories, and the rational Betti numbers (1,0,0,1) of NP are checked in `check_finite_rescue.py`. The geometric join proof establishes the full homotopy type independently of that rational calculation.

Both this construction and the coherence completion received an independent second mathematical reading. The bounded literature check included the Dwyer-map results of Thomason and Cisinski and the pushout comparison of Hackney et al. (2024, using the explicitly identified arXiv v3 theorem numbering). We did not find this particular finite construction in the sources checked. This is not a claim of novelty or of an exhaustive search.

### Smoothness and the last gluing theorem

The commentary proves the two slice and strict-fibre identifications in Theorem 4 on objects, Hom-sets, identities, and composition. The direct local-smoothness argument uses a split fibration over the contractible fork with aspherical fibres. This repairs the noncommuting diamond noted in footnote 107 and removes W(7 bis) from the forward direction. A direct contraction likewise removes that hypothesis from the open-cover corollaries. The reverse implication concerning the middle map still uses strong reflection.

The sentence after Corollary 6 drops necessary outer smoothness assumptions. An explicit finite-poset example gives a central lifting category consisting of a contractible three-object fork and an isolated point. W(5) prevents its asphericity although the central and second outer maps are smooth. The conditional corollary itself remains valid with its stated outer hypotheses.

Proposition 15 is proved through the presheaves of arrows crossing from a sieve to its complement. The comparison is a left Kan extension; fixing one crossing arrow identifies its fibre with the connected components of the corresponding factorization category. The proof includes the functor-out universal property and both directions of the criterion. A two-object example shows why the condition on crossing arrows cannot be omitted.

For categories of elements, the formula

\[
N(X/F)_n=\coprod_{x_0\to\cdots\to x_n}F(x_n)
\]

proves preservation of colimits. The relative functor into Cat/X preserves all small limits as well. This stronger known statement is credited to Cisinski (2006, Proposition 3.2.12 and Corollary 3.2.13), and the commentary gives its explicit adjunction and a direct proof. It is not marked as original. The proof of Theorem 5 also verifies complement arrows, since a bijection of complementary object sets would not by itself establish a categorical isomorphism.

The positive homotopy-pushout clause of Theorem 5 holds for every fundamental localizer: the nerve square is a simplicial pushout along a monomorphism, and W∞ is contained in every fundamental localizer. The final reflection equivalences retain strong W(7 bis). Accessibility and a suitable local test category are needed for the later presheaf model-structure theorem (Cisinski, 2006, Theorem 1.4.3 and Corollary 4.2.18). The case X = e gives a complete factorization obstruction to inferring such a model structure from attachment stability alone.

## False statements versus source sketches

The `proof_status` column records the source's treatment. There are 85 `proved`, 44 `stated`, 13 `sketched`, five `assumed`, four `false`, three `conjectured`, and two `open` entries. Two `proved` rows are explicitly labelled commentary propositions rather than source assertions. A status such as `open` at the place where a question is asked does not mean open today: the equivalence of smooth and proper integration is answered later in the same source.

| Audit entry | Problem as written | Repair |
| --- | --- | --- |
| XIIb-b-B014, ms. 139 | Γ is identified with the ordered square plus an initial vertex | Retain the free diamond and impose equality only after composition to the added cocone vertex |
| XIIbb-C009, ms. 155 | Cartesian arrows in the smooth integral are printed in the reverse direction | Use αᵢ(x₀) → x₀; keep the printed source reading |
| XIIbb-C013, ms. 156 | A noncommuting integral diamond is used as a strict cocartesian square | Use the fibred argument of footnote 107 for preservation, and the strict closed-piece replacement for reflection |
| XIIbb-C021, ms. 157 | Local smoothness at the central stratum is asserted without the outer hypotheses | Retain both outer smoothness assumptions; the commentary gives a finite counterexample otherwise |

The register also records smaller source slips, absent proof details, inherited hypotheses, and later strengthening. A true conditional assertion is not assigned `false` merely because W∞ does not satisfy its extra axiom.

## Reading corrections and source preservation

The two questionable curved arrows, λₐ on attached leaf 4 and λ₂ on leaf 11, are solid. Their tiny contiguous segments are a feature of the original PDF curve rendering. They are visibly distinct from the truly dotted i₀ arrow on leaf 11. The two `dashed` TikZ options have therefore been removed. Footnote 107 on leaf 31 really contains two unlabelled arrows from a common source; no vertex label was lost. All three uncertainty comments are replaced by resolved comments.

The global `\intdiag` definition in the supplied TeX is truncated and has no closing body. It has been restored as a three-argument macro producing the integral sign and its two-legged diagram. This is a preamble repair, recorded as a transcription correction spanning its uses, rather than a reading change to any printed sentence.

The 30 edition-slip records include all 13 existing `[sic]` comments, the editors' bracketed repairs, the reversed cartesian arrows, and the reversed complement arrows in both corollaries of Proposition 15. The edition's erroneous words, arrows, and bracketed annotations remain in the source. The correction register explains their intended readings without applying them silently.

`source_patch.diff` discloses every source-file modification. In addition to the two arrow-style corrections and the macro restoration, it contains layout and compatibility changes: A4 margins with room for the source labels, English language support for commentary, French punctuation spacing, microtypography, a current-babel compatibility definition, separation of the two inline diagrams on manuscript page 145, and a smaller font for the long typewriter editorial note on page 166. Two corollary openings are protected against separation from their diagrams. The comparison diagrams on manuscript pages 140 and 145 have additional horizontal space so that their labels remain clear of adjacent objects and parentheses. The wording and mathematical content of those reflowed passages are unchanged. `repair_source.py` reproduces this patch from the original transcription.

The companion style adds the credit page, short manuscript labels in block headings, English hyphenation within commentary, and space protection before a heading. The original style is retained in `inputs/derivateurs_companion_original.sty`. The supplied builder is unchanged.

## Literature verification and limits

Every bibliography entry contains a concrete `verified:` note describing the passage or metadata actually checked. Existing cumulative keys are reused. The two duplicated Maltsiniotis entries from the section drafts were merged, retaining both checked scopes. Generic inherited verification notes were not copied into the final bibliography.

The historical discussion uses Grothendieck's *Pursuing Stacks*, §69, and his letter to Thomason of 2 April 1991, §§1–2. The modern comparison uses Groth (2013, Definition 3.9 and Proposition 3.13) and Lurie (2009, Corollary 3.3.4.3, Warning 3.3.4.4, and Proposition 3.3.4.5). The latter is explicitly interpreted with inversion of Cartesian transport edges; the total category is not identified with a Cat∞ colimit before that operation. The classifying-space statement and the categorical statement are kept distinct.

The original 1979 Thomason proof was not accessible through the publisher during this work. Its metadata were verified, and its theorem statement and number were checked through Cegarra's primary independent treatment (2020, §§1 and 3, equation 9 and Theorem 3). The span case used here is proved directly in the commentary. The final bibliography states this limitation rather than certifying an unread proof.

The opening request for an enlarged cofibration class closed under the stated interval pushout-product operation remains unsettled here in full generality. We prove the indicated Dwyer-map failure and document the later retract correction, but do not claim that those facts settle the requested closure property. This is the limit of the present audit, not a declaration that the question remains open in contemporary research. No exact preceding XII commentary was supplied, and no exhaustive literature search or priority determination is claimed.

## Reproduction and validation

On a complete TeX Live installation, run from the archive's top-level directory:

```sh
python3 build_reader.py DER_XIIb-b
lualatex -interaction=nonstopmode -halt-on-error DER_XIIb-b_reader.tex
bibtex DER_XIIb-b_reader
lualatex -interaction=nonstopmode -halt-on-error DER_XIIb-b_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_XIIb-b_reader.tex
```

The build environment used for this delivery lacked LuaLaTeX support files, its format, and a usable font-map configuration. `bootstrap_tex.py` and `build_local.py` supply those components in a local TEXMF tree; no system installation was modified. The dependency archive URLs and SHA-256 hashes are recorded in `review/tex-downloads.json`. These support scripts are for reproducing this restricted environment; an ordinary complete TeX Live installation needs only the commands above.

The supplied builder validates the six files, anchors, enumerations, unique IDs, and citation keys. `validate_deliverables.py` additionally checks preserved manuscript markers and `[sic]` comments, all three resolved doubts, specific bibliography notes, final build logs, overview length, and PDF text bounds. The final build has **zero TeX errors, zero overfull boxes, zero missing glyphs, zero undefined citations or references, and no BibTeX warnings**. The remaining log advisories are babel-french's notice about its supported legacy list implementation and automatic repositioning of seven margin labels. The PDF is rendered for visual inspection; those advisories are not omitted from the saved validation record.

`review/validation.json`, the final builder/BibTeX/LuaLaTeX logs, the finite-computation results, and the source patch are included. Rendered page images are review intermediates; the deliverable is the PDF itself. The independent section notes and drafting scripts are retained in `audit_parts/` for traceability. They are working provenance, not additional requested companion files.

All 54 reader pages were inspected in rendered form, using page sheets and individual pages for dense formulas, diagrams, footnotes, and the bibliography. The final layout pass resolved two corollary openings separated from their diagrams and two crowded comparison labels; the affected page ranges were rendered and checked again. The manuscript and printed-page labels remain legible, including the automatically moved labels. No clipping, missing mathematical symbols, diagram-label collisions, or unresolved heading orphans were found in the final inspection. `review/visual_review.json` records the review ranges and the final PDF digest.
