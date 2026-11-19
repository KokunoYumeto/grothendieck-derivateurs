# Les Dérivateurs, Chapters III–V: report on the audit and companion

**Edition audited:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991), electronic edition deciphered and transcribed by M. Künzer, J. Malgoire, and G. Maltsiniotis, as supplied in `DER_III-V_pages.pdf`. **Verification date:** 9 November 2026. The supplied PDF, rather than a silently corrected mathematical reconstruction, governs every transcription decision.

## Scope and navigation

The audit covers the whole supplied extract. Its 53 PDF pages include six title or editorial pages and 47 pages of mathematical text. Manuscript pagination restarts between chapters; a bare manuscript page number is therefore insufficient for Chapters III and V.

| Chapter | Physical PDF pages containing mathematics | Edition pages containing mathematics | Manuscript pages |
| --- | --- | --- | --- |
| III | 3–10 | 1–8 | 1–12 |
| IV | 13–19 | 1–7 | 73–83 |
| V | 22–53 | 1–32 | 1–52; page 32 is marked blank |

The absence of manuscript pages IV.1–72 is stated by the edition. It is not a lacuna introduced by this package. The claims table uses chapter-qualified locations, and the reader's commentary headings display the chapter and manuscript page. Its PDF bookmarks identify the chapters, every commentary block, the overview, and the bibliography.

The six files prescribed by `FORMAT.md` are complete. The ZIP also supplies the corrected transcription, the assembled reader and its compiled PDF, the build tools, machine-readable validation, source and tool patches, the original supplied transcription and PDF, and the authoring scripts. The standalone overview is included in the reader after the annotated text. The earlier-package index was read for continuity: references to those discussions replace repetitions of their treatments of diagram localization and the loss of coherence under the underlying-diagram functor.

The package contains **249 audited assertions**, **134 correction and adjudication records**, **45 commentary blocks** (about 17,610 whitespace-delimited words, including formula markup), and **22 bibliography entries**. The overview occupies **3 compiled pages**, within the required two-to-five-page range. The complete reader has **72 pages**.

| Audit component | Count |
| --- | ---: |
| Chapter III assertions | 52 |
| Chapter IV assertions | 38 |
| Chapter V assertions | 159 |
| Transcription repair records | 14 |
| Edition readings or slips retained | 114 |
| Doubt adjudications | 6 |

All four original `% ??` flags and all 39 original `% [sic]` flags are accounted for. Two additional doubt-adjudication rows confirm the edition's own bracketed uncertainties without claiming to decipher the unattached manuscript. A correction record can group several occurrences of the same notational error; the source patch, rather than the record count, gives the exact individual changes.

## What the audit columns mean

The `proof_status` column records the status of the assertion in the supplied pages. A repair supplied in the commentary does not retroactively turn a manuscript sketch into a proof in the historical source. The `repair`, `references`, and `notes` columns distinguish our completed arguments, the edition's own interventions, and later theorems. A printed false statement corrected a few lines later is recorded locally with that correction; it is not counted as a surviving defect of the chapter's final conclusion. Conversely, a proposed application of a correct formal proposition is not certified when its extra hypothesis has not been established.

The correction table makes the corresponding textual distinction. `transcription` restores the PDF's reading or a dependency necessary to typeset the supplied transcription. `edition_slip_kept` records a reading that the PDF itself prints; the French source preserves it, including editorial brackets. `doubt_resolved` adjudicates a supplied uncertainty flag. Each row cites a physical PDF page and enough local evidence to find the reading. The archived original and unified patch make every actual source change inspectable. The original upload uses CRLF line endings; its bytes are retained, and an additional LF-normalized copy is the explicit base of the unified patch.

## Principal mathematical conclusions

### Chapter III: actions, external Hom, and boundedness

The tensor–cotensor adjunction follows from the two Kan-extension adjunctions, but homotopy invariance in the indexing category and representability of the external Hom require further arguments. The commentary separates an action of spaces from a closed enrichment and identifies the modern descent and universal-property results. In *Propriétés universelles et extensions de Kan dérivées*, Cisinski's Proposition 3.7 and Corollary 3.10 give the localizer argument directly; Theorem 3.24 and Corollary 3.26 give the universal property of the derivator of spaces. Groth and Shulman's later account distinguishes the action from stronger enrichment data.

For derived categories, the worked calculation uses cohomological grading and the good truncation of derived Hom. The resulting mapping-space identity is

\[
\pi_n\operatorname{Map}(M,N)=\operatorname{Hom}_{D(k)}(M,N[-n])\qquad(n\geq0),
\]

at the zero map. The sign and the degree-zero kernel in the truncation are essential. The unreduced circle tensor is \(M\oplus M[1]\); suspension is its reduced summand. Grothendieck himself returns to the pointed correction at the end of the chapter, and the audit credits that repair.

The proposed enhancement with values in \(D^-(\mathbf Z)\) has a real boundedness limitation for arbitrary coefficients. Over the dual numbers \(k=F[\varepsilon]/(\varepsilon^2)\), the residue field \(F\) has nonzero \(\operatorname{Ext}^n_k(F,F)\) in every nonnegative degree. The complete resolution and calculation are included. This is a concrete obstruction to the unrestricted bounded-above target, without calling into question the unbounded derived-Hom construction.

### Chapter IV: coherent squares and adjunction maps

The loop construction is explained through successive fully faithful Kan extensions, with the existence and uniqueness assertions stated in their proper essential-image form. A coherent square carries information that an ordinary commutative square in the fundamental category need not determine.

For a functor \(f:I\to J\), the collage with mixed arrows \(\operatorname{Hom}_J(f(i),j)\) identifies a presheaf on the collage with a map \(f^*G\to F\). The commentary completes the indexing construction that realizes the relevant units and counits coherently. It gives the comparison functors, computes the pointwise Kan extensions with the correct opposite comma categories, and checks the adjunction identities. These canonical lifts concern the specified adjunction maps; they do not assert a canonical coherent lift of every arbitrary arrow in a homotopy category.

### Chapter V: localization by paths

The path theorem is proved with strict endpoint fibres: transformations must be the identity at each endpoint. A full subcategory on paths with the right endpoint objects would be a different construction. The manuscript's switch to even indices repairs the parity problem in concatenation. The quotient, composition, denominator inversion, and cancellation arguments are made explicit, including the degenerate zero-length cases. The hypotheses do not require an Ore condition or composition closure of the original class of denominators.

The main development proves the stronger form of the interval lemma proposed on manuscript page V.26. If the target is any finite oriented path and a restriction has been prescribed, the category of extensions is either empty or categorically contractible. Numerical minimum and maximum are functors on the path; combining them with one chosen extension produces an explicit finite zigzag from the identity endofunctor to a constant endofunctor, through transformations that fix the prescribed restriction. The proof also covers equal-endpoint fibres needed for cancellation. The result is marked `\ours` to identify responsibility for this proof. The relevant min–max-ordering literature was checked, and no priority claim is made.

### Chapter V: diagram parameters, ind-objects, and the final questions

For a variable diagram shape \(X\), the finite length of a path must be bounded uniformly over all objects of \(X\). This is the mathematical reason for the ind-object and the exclamation-mark notation. The resulting formula is an ordinary-localization theorem:

\[
\operatorname{Hom}_{\mathcal M^X[\Sigma_X^{-1}]}(a_X,b_X)
\cong\varinjlim_n\pi_0\operatorname{Fun}(X,K_n).
\]

It does not by itself identify the nerve of the ordinary union with a derived mapping space. The commentary proves the ind-Yoneda calculation, the formal reflective-localization propositions, and the required passage from tests on ordinary objects to tests on ind-objects. Descent of ind-representability itself needs no reflective-localization hypothesis: left Kan extension along the opposite of a localization carries representables to representables and preserves their filtered colimits. Once the presheaf descends, the images of its representing stages ind-represent that descended presheaf. The argument is given in full. A separate bar-resolution calculation for simplicial sets and cyclic-group cohomology explains a model case in which the external Hom is an actual homotopy type.

Several finite-stage issues can be settled directly. For a filtered union of full subcategories, a functor out of a category with finitely many objects factors through one stage, irrespective of how many arrows the source has. The corresponding statement on connected components extends to sources with finitely many isomorphism classes of objects. An infinite alternating fence demonstrates that stagewise categorical homotopies may have unbounded minimal length and therefore fail to assemble into a global finite zigzag. The same fence clarifies the restricted-Yoneda aside on pages V.45–46: uniqueness within the subcategory of finite-type objects does not imply uniqueness among arbitrary objects of categorical homotopy theory.

The one-arrow question on page V.49 has a negative answer even with a Thomason-fibrant target. The category \(0\to1\leftarrow2\) is fibrant, as follows directly by lifting subdivided horns using its terminal object. Its two outer vertices are homotopic but have no arrow between them in either direction. The full proof identifies the precise lifting criterion used; it is separate from the stronger filtered-diagram questions.

The final finite-test question has a definitive negative answer. Let \(G\) be the finite-support permutation group of \(\mathbf N\), and let \(s:G\to G\) shift the support one place while fixing zero. The map \(Bs\) is not an equivalence, but every map into \(BG\) from a finite category's nerve uses only finitely many supports and sees the shift as an inner conjugation. Thus \(Bs\) induces the identity on every proposed test. This proves failure of both conservativity and faithfulness. The example is the classical case attributed to Matumoto, Minami, and Sugawara (1984, Proposition 4.1); the attribution is verified through Arlin and Christensen (2023, Remark 2.3). Their Theorem 2.1 proves the stronger assertion that no set of unpointed spaces jointly reflects isomorphisms. Their Theorem 4.3 explains why retaining mapping groupoids changes the conclusion.

## What is not certified

The strict composition functor requested at V.12–13 on Grothendieck's precise eventual path category, with its symmetric end-padding convention, is not constructed in the supplied pages and was not located in the consulted sources. The comparison with finite-stage concatenation additionally requires bounded target-stage factorization on each source stage. The composition on connected components is proved. Strict composition in a different path or hammock presentation does not by itself supply the functor requested for this fixed category. No nonexistence result is asserted.

The claimed fully faithful right adjoint to \(\mathrm{Cat\,hot}\to\mathrm{Hot}\), questioned by the edition at V.37, was not established in this audit and was not located in a primary source proving precisely the asserted quotient-category adjunction. Thomason fibrant replacement alone does not supply the proposed universal property for actual functors out of every source category modulo finite zigzags. The formal Propositions 1 and 2 remain valid under their stated reflective-localization hypothesis; applying them through this particular reflection remains conditional. This is a limit of verification, not a declaration that a known mathematical problem is open.

The raw union-map assertion at V.47 and the strictification questions at V.48–49 are recorded with their exact hypotheses. An isomorphism of ind-objects in a homotopy category need not carry coherent choices of the stagewise homotopies. The explicit fence example resolves the length obstruction without settling the stronger version in which all target stages are additionally Thomason fibrant. Verified replacement constructions and levelwise weak-equivalence statements are distinguished from these stronger conclusions.

Nor does the ordinary path-localization calculation establish, in arbitrary relative categories, a weak equivalence between the nerve of Grothendieck's specific unbounded path category and a Dwyer–Kan mapping space. The latter has a verified construction and its own comparison theorems. Any proposed identification with the former still needs hypotheses and a proof. Likewise, an action of homotopy types on a derivator alone is not a proof of closed enrichment or of the representability of every external Hom contemplated in Chapter III.

## Literature verification

Bibliography keys already present in the supplied cumulative file have been reused. The cumulative file itself contains repeated keys; the new bibliography includes one entry per key and only the works used in this package. Each entry has a DOI or URL and the exact `verified` or `unverified` note required by the format. An opened bibliographic record verifies metadata; a theorem citation requires inspection of the corresponding text. The reference-verification notes supplied with the authoring fragments record the extent of those checks.

The references with full-text checks include the cited passages of Cisinski, Groth, Groth–Shulman, Thomason, Dwyer–Kan, Riehl, and Arlin–Christensen, as well as the relevant foundational and historical sources identified in the bibliography. The original Matumoto–Minami–Sugawara article was not opened successfully and is explicitly marked `unverified`; its attribution is supported by the opened Arlin–Christensen paper, and the needed counterexample is proved independently in full. A bounded search that did not locate a result is never presented as evidence that nobody has proved it.

## Reader and format repairs

The supplied builder indexed a manuscript page by its first occurrence. This would place Chapter V comments on Chapter III pages with the same number. The revised builder retains every occurrence, requires a unique exact phrase for repeated page numbers, and rejects an ambiguous bare-page anchor. It also recognizes the marker for the blank manuscript page V.32 and preserves input order when several blocks share an insertion point. The original minimum twenty-character requirement for phrase anchors is enforced. No validation gate has been disabled.

The source and commentary are set in French and English respectively. Commentary headings show the chapter and page without printing the long machine anchor. Bookmarks provide navigable block titles. Chapter title sheets start on fresh pages. Two isolated hard breaks at the start of edition page 2 are relaxed in the annotated reader so that the inserted discussion flows without leaving an unnecessary half-empty page; the source-page markers remain. The TikZ brace-decoration library omitted by the supplied transcription is loaded, and the original source is retained alongside a unified patch. The bibliography is set ragged right to avoid stretched lines around long URLs. Additional typographical adjustments are documented in the final build section below.

The build tools can be run with an ordinary LuaLaTeX, BibTeX, and Python installation. The included environment-recovery script documents how missing LuaLaTeX data were supplied locally in this execution environment; the large runtime packages are not part of the deliverable. The mathematical results were checked by explicit argument and independent review of the central constructions. They have not been formalized in a proof assistant.

### Final build and visual verification

`python build_reader.py DER_III-V` and the additional integrity validator both pass. BibTeX completes without warnings. Two successive LuaLaTeX runs after BibTeX complete with no errors, undefined citations, missing characters, or overfull boxes. The overview is within its specified page range. Every page was rendered; the full set of contact sheets and the pages containing dense formulas, long diagrams, repeated manuscript markers, the overview, and references were visually inspected. Text bounds are inside the page on every page.

The remaining routine TeX messages concern automatic movement of marginal source-page labels and one mildly loose line in an English paragraph (`Underfull \hbox`, badness 1189). Their final layout was inspected. They do not indicate missing text or unresolved references. Page-marker text is set ragged right to avoid stretched short lines, and a harmless empty group prevents amsmath from mistaking an opening homotopy-class bracket for an optional alignment argument. No mathematical formula was altered to achieve the layout.

The archive includes the final BibTeX and LuaLaTeX logs, `validation.json`, and the geometry report. The supplied PDF and original transcription are archived unchanged; SHA-256 hashes of the final deliverable files are recorded in `support/SHA256SUMS.txt`. Rebuilding uses the root `rebuild.sh` or the commands documented in that script.

## Credit

The commentary was AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). The supplied project credit also says “edited with Claude (Anthropic).” That phrase is preserved here as the project's supplied credit; no separate Claude editorial pass is documented for this delivery. No human author is attributed to the new commentary. Grothendieck is the author of the source text, and the named electronic-edition transcribers retain their source-edition credit.

## Commentary index

This index follows the compiled reader and can be used when continuing the companion in a later package.

| Chapter and manuscript page | Kind | Title | Reader page |
| --- | --- | --- | ---: |
| III.1 | exposition | Spaces acting on coefficients | 3 |
| III.4 | status | The descent theorem and its domain | 5 |
| III.5 | examples | What the circle actually gives | 6 |
| III.6 | exposition | Associativity and exactness from product squares | 7 |
| III.8 | later | External Hom as a derived mapping space | 9 |
| III.10 | exposition | What the Yoneda calculation proves | 10 |
| III.11 | examples | Integral chains and the truncation of derived Hom | 12 |
| III.12 | status | Keeping all degrees of the mapping complex | 13 |
| IV.73 | context | Why the skeleton is insufficient | 16 |
| IV.75 | exposition | Constructing the loop square without choosing homotopies | 17 |
| IV.79 | exposition | The collage records a relative morphism | 20 |
| IV.82 | exposition | The missing Kan extension comparison | 22 |
| IV.83 | development | Completing both coherent adjunction arrows | 23 |
| IV.83 | examples | A diagonal and its two projections | 24 |
| V.1 | exposition | A path remembers the arrows that will be inverted | 27 |
| V.3 | exposition | The pro-interval and the eventually constant diagram | 29 |
| V.5 | examples | Fixing the endpoints also fixes the vertical arrows | 30 |
| V.6 | exposition | Why a commutative ladder gives equality after localization | 32 |
| V.8 | context | Localization without a short-fraction hypothesis | 33 |
| V.12 | status | What composition in an ind-category actually asserts | 35 |
| V.14 | exposition | Even indices and reparametrization relative to the ends | 36 |
| V.17 | exposition | A contraction is determined by the edges it erases | 38 |
| V.21 | exposition | Sliding an even block gives a natural transformation | 40 |
| V.22 | examples | A denominator set need not be closed under composition | 42 |
| V.23 | examples | Two ordinary arrows and one comparison diagram | 43 |
| V.25 | development | Contracting relative functor categories into an interval | 44 |
| V.27 | examples | Cancellation uses the same endpoint twice | 46 |
| V.27 | exposition | Completing the universal property | 47 |
| V.27 | later | From components of path categories to mapping spaces | 47 |
| V.28 | exposition | The parameter is a diagram shape | 48 |
| V.30 | exposition | Why the exclamation mark is necessary | 50 |
| V.33 | exposition | The precise meaning of ind-representation | 51 |
| V.35 | exposition | Two homotopy invariance questions | 53 |
| V.36 | examples | An external Hom that is an ordinary homotopy type | 54 |
| V.37 | status | The unproved reflection must remain a hypothesis | 55 |
| V.39 | exposition | A retract of a local object is local | 57 |
| V.42 | exposition | Why the argument passes to ind-objects | 59 |
| V.43 | later | What Thomason replacement supplies | 60 |
| V.45 | development | Finitely many objects already give a uniform stage | 62 |
| V.46 | exposition | Fibrancy passes to the union | 63 |
| V.49 | development | A complete instance of the length obstruction | 64 |
| V.49 | examples | Fibrancy does not reduce every homotopy to one arrow | 65 |
| V.51 | later | What a canonical mapping space requires | 66 |
| V.52 | examples | Finite unbased tests miss a symmetric-group shift | 66 |
| V.52 | status | The modern scope of the final obstruction | 67 |

