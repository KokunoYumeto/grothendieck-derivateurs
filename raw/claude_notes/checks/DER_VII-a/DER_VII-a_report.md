# Les Dérivateurs VII-a: audit and production report

**Scope:** Chapter VII, manuscript pages 1–57, including the intercalated pages 49′ and 50′. **Status date:** 10 November 2026 (Europe/Berlin). This is the ninth package in the supplied project sequence.

## Completion and contents

The six files required by `FORMAT.md` are complete. The commentary contains 37 substantial blocks: 17 exposition blocks, eight worked-example blocks, four developments, three historical-context blocks, three later-development blocks, and two status blocks. The claim register covers every manuscript page, the intercalated pages, the eight numbered propositions, their corollaries, the intervening definitions and assertions, and the final all-degree nerve construction. The overview gives a continuous account of the installment. All ten cited works have been opened; the bibliography records them as verified and preserves existing cumulative keys where available.

The audit has **177 rows: 173 source items and four explicitly identified commentators' results**. Source proof status is distinguished from completion in the commentary: a source sketch remains `sketched` even when the commentary supplies a full proof. Twelve literal assertions are marked `false`, with counterexamples and repairs. This number includes local numerical or indexing assertions; it does not mean that twelve principal theorems fail. The main classification and nerve-freeness results survive.

The correction register has **101 records**: 18 genuine transcription corrections, two resolved doubtful readings, and 81 retained edition readings. The last group consists of 79 printed slips or omitted conventions and two unchanged editorial `[sic]` annotations. The slips include orthography, grammar, indices, notation, and substantive mathematics. All 56 `% [sic]` tags on 53 source-comment lines have a recorded disposition; compound comments can require more than one correction record. Both `% ??` readings are resolved, and neither requires changing the associated formula.

The archive also contains the compiled reader, its generated TeX, the corrected source transcription, the style and builder, the original transcription and original builder/style for comparison, section contributions, exact patch records, validation results, and all task-specific code used for generation and verification. Large third-party runtime downloads and redundant source-page rasters are omitted; they are reproducible from the scripts and provenance records.

## Source authority and the missing tail

The advertised page range does not match the supplied PDF. That attachment has **37 physical pages: two preliminary pages and edition pages 1–35**. It stops midway through manuscript page 52. The attached TeX continues through **edition page 38 / manuscript page 57**. The prompt's description “edition pages 1–37” is therefore inaccurate for both the PDF and the complete transcription.

To finish the requested audit, the missing tail was checked against the same official electronic edition, version **22 December 2001**, obtained from Georges Maltsiniotis's Chapter VII page:

https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChVII-456.pdf

The official full chapter has 109 physical pages. All 37 physical pages shared with the attachment were compared in two independent ways: extracted text and rendered page images at 72 dpi. Every comparison was identical. Official physical pages **38–40**, corresponding to edition pages **36–38**, were then rendered and visually read to check the transcription's remaining manuscript pages 52–57. Each correction concerning the supplement explicitly names that authority. The full provenance record, including every common-page comparison, is in `qa/source_provenance.json`.

| Source | SHA-256 |
|---|---|
| Supplied 37-page PDF | `29eee17debda34a9a7b69218d7b9ae472958ae4a4f3ed3d46197acbcfaa70a61` |
| Complete official Chapter VII PDF | `1b246f105a72e3558242ef8e23a14e779de4f537080a59e27a2a516a5538e481` |

The comparison was with the electronic edition, not a facsimile of Grothendieck's manuscript. Consequently `edition_slip_kept` means that the defective reading is present in the printed authority; it does not determine whether Grothendieck or the transcribers introduced it. No diplomatic correction beyond that evidence is claimed. The French source is not silently regularized.

The complete transcription was read in three adjoining mathematical ranges, manuscript pages 1–18, 19–38, and 39–57. Every corresponding PDF page was rendered and visually inspected, including arrow directions, underlining, diagrams, indices, footnotes, and the supplementary tail. The two uncertain arrow-label underlines were checked in enlarged crops. The English proofs were then reviewed across ranges, with particular attention to variance, endpoint conventions, the zero-length type, and the relation between structural intervals and critical vertices.

## Mathematical findings

### Intervals, fullness, and reduction

The first construction is a free category on a finite oriented path. Its progression order and categorical order serve different purposes. An interval may be traversed left to right while some generating arrows point right to left. Structural chains are maximal constant-sign runs, and critical vertices are their endpoints. The commentary makes these definitions explicit before discussing intrinsic orientation and reduced shapes.

The principal early repair is Proposition 1(b), manuscript page 5. The edition really says “functor.” The endofunctor of the three-object chain with vertex values `(0,0,2)` fixes both endpoints and is not the identity. The subsequent proof establishes the automorphism statement, which is enough for the classification of orientations. The commentary proves the sharp additional result: an interval has no nonidentity endpoint-fixing endofunctor **if and only if it is reduced**. This proof treats arbitrary functors; it does not assume numerical monotonicity.

Proposition 3, manuscript page 10, uses incoming and outgoing slices as though they exhausted every other vertex. They omit vertices incomparable with the chosen vertex. Its printed global coproduct equality is therefore false. The footnote's no-cross-arrow criterion remains valid. The commentary gives the numerical left/right deletion criterion needed for the next argument and completes Proposition 5 directly. In a full subcategory, consecutive retained vertices are joined exactly when no intervening critical turn has been omitted. This proves both the interval decomposition of components and the connectedness criterion.

The footnote on manuscript page 11 claiming that every interval-shaped subcategory is full also fails. Inside the chain `0→1→2`, retain `0→1` and `0→2` but omit `1→2`. The result is an interval-shaped span and is not full. Fullness remains essential to the intended definition of subinterval.

Other early repairs distinguish arbitrary injective simplices from maximal structural chains, correct the printed object-count/length equality, and treat the endpoint map to a point as a map rather than an embedding. The full faithfulness of an injective simplex is retained; the erroneous maximality correspondence is not used to manufacture a second false theorem.

### Categories of paths and changes of shape

A path of fixed type is a functor `I_tau→X`; its morphisms are natural transformations. The ordinary category of such diagrams and its underlying object set must remain distinct. Two actual transcription errors in this range lost that distinction by using an underlined `Ch` where the edition prints the ordinary symbol. Both were corrected locally.

The commentary gives the identity-path proof of the Yoneda classification of operations natural in `X`, works out composition and insertion of an identity, and supplies the complete split Grothendieck-fibration construction. The three successive categories of types are kept separate: all functors, endpoint-preserving functors, and increasing endpoint-preserving functors. The successive fullness assertions refer to different definitions. They are not inconsistent claims about one fixed category.

No bifibration theorem is attributed to the manuscript. A worked span example shows why a direct-image construction would require additional colimits in `X`; already collapsing the span would require a pushout. The example with a three-object span as coefficient category gives 11 span-shaped diagrams and nine cospan-shaped diagrams. Both functor categories are posets, so they cannot be equivalent. Stable reorientation results apply in a different setting, explained with precise hypotheses and references.

Proposition 7 and its main corollaries are correct. The proof separates nonconstant images of structural runs, crossing of target critical vertices, and additive length budgets. Three printed subsidiary overstatements are repaired: a constant map at a noncritical interior vertex lies in one critical interval, not two; the image of source critical vertices need not fill the ambient integer segment; and intrinsic runs of a preimage can include truncated constant boundary pieces absent from the global-run index. Those additional pieces contribute zero, so the numerical length formula survives.

### Signed transitions, concatenation, and the nerve

For the final category of types, taking transitions reverses arrows. A morphism `f:tau→upsilon` determines a nondecreasing sign-preserving function from the target transitions to the source transitions. Conversely, such a function `h` gives the vertex function

`f(i) = #{j : h(j) ≤ i}`.

The commentary proves that these constructions are inverse, reverse composition, and handle empty words. Thus the final type category is opposite to the category of finite signed linear orders with monotone sign-preserving maps. Proposition 8 is the reduced-target case: the transition map is then injective, and a morphism is a signed subsequence.

This description supplies complete inverse constructions for the outgoing weight-vector classification and the incoming image-and-fibre classification. The printed reconstruction on manuscript page 45 must use the graph whose edges are precisely the collapsed transitions. Its vertex union alone is insufficient: source `+++` with weights `(0,1,0)` has vertex map `(0,0,1,1)`, although every source vertex is incident to some collapsed edge. The point target requires the convention that the critical-image set is the whole image `{0}`. The object-map table on manuscript page 47 requires cumulative jump sums.

Concatenation is the pushout obtained by gluing chosen endpoints. It gives a strict monoidal structure on the final category, and even on the intermediate endpoint-preserving category. It cannot extend with the same object operation to the category allowing all functors. There `+` and `−` are isomorphic, whereas `++` and `−+` are not; tensoring such an isomorphism with `+` would be impossible. This is a genuine obstruction to the printed parenthesis on manuscript page 50.

The signed-order model gives the strict monoidal universal property: the category is freely generated by two counital coassociative comonoids. The one-colour ordinal/comonoid result is classical; the two-colour statement is presented as its explicit adaptation, with a complete proof, rather than as a new homotopy theorem (Aguiar & Mahajan, 2010, Appendix D).

Every nerve degree is a free monoid. A string of composable type maps factors uniquely according to the transitions of its initial word. Each factor is an ordered rooted expansion history; zero-length descendant blocks are allowed. The commentary proves this for every degree and gives the faces and degeneracies. The first face can take one indecomposable to a product or to the unit. Consequently the distinguished degreewise bases do not form a simplicial subset. The two final support and summation index slips are corrected in the commentary without changing the source.

## Developments and their status

Four results are explicitly marked `\ours`, each with a complete proof and a bounded account of the literature checked.

| Result | Content of the proved continuation |
|---|---|
| Reduction adjunctions | The critical-vertex inclusion `j:R→I` has retractions `r_t ⊣ j ⊣ r_s`. The corresponding precomposition adjunctions explain groupoid-valued invariance and failure of full faithfulness for general diagram categories. |
| Sharp endpoint rigidity | Every endpoint-fixing endofunctor is the identity exactly when the interval is reduced, including the point convention. |
| Maximal endpoint evaluation | A shape map admits endpoint evaluation functors natural in every coefficient category exactly when the required comparison arrows to the specified endpoints exist. This maximal class is closed under composition but does not support strict endpoint gluing. |
| Sections of contractions | A retained signed edge subset admits a section exactly when the exterior signs and each interior left/right cut satisfy the stated sign conditions. The number of sections is the product of the available cuts in equal-sign gaps. |

The general ingredients—Yoneda, precomposition adjunctions, Grothendieck constructions, and the ordinal/comonoid description—are attributed. The critical-vertex reduction itself is used explicitly in the later literature. Searches did not locate the exact additional interval formulations and counting criterion in the sources checked. This is a limited negative search result, not a priority claim or an assertion that no such result exists elsewhere. These developments finish useful consequences of the manuscript's definitions.

## Historical and current references

The earlier-package index was read, especially DER_VI-a. The commentary refers back to its discussion of splitting and path completion instead of repeating the foundations. Historical context is tied to the constructions here: SGA 1 for split fibrations; Gabriel–Zisman for ordinary localization; and Dwyer–Kan's 1980 hammock construction, which already predates these notes. No unverified causal claim about Grothendieck's reading or influence is made.

The later comparison is exact at the level of shapes. Marking negative transitions identifies the final type category with Mazel-Gee's zigzag type category (2018, Definition 3.5 and Remark 3.6). Arakawa and Cnossen's August 2026 preprint uses the same boundary-preserving shape category, its Reedy structure, and its critical-vertex reduction (Example 4.12 and Lemma 4.16). The status block distinguishes these finite identifications from the extra weak-equivalence data and homotopical colimits needed for localization mapping spaces.

Mazel-Gee's three-arrow comparison is stated after geometric realization and under its calculus-of-fractions hypothesis, not as an unconditional equivalence of simplicial-space objects. His Rezk-nerve localization theorem is cited separately (2019, Theorem 3.8). The more recent mapping-space comparison is explicitly labelled a preprint result; its strict ordinary endpoint-fibre specialization is supported by Arakawa and Cnossen's Section 4 as well as Theorem 1.9 and Corollary 1.11. This higher-categorical structure is not attributed to the present excerpt.

### Verified locations

| Bibliography key | Passage checked and use |
|---|---|
| `Grothendieck1990VII` | Official Chapter VII, electronic edition of 22 December 2001, including supplemental edition pp. 36–38. |
| `GrothendieckSGA1` | Exposé VI §§8–10, §11(f), Proposition 12.1: split fibrations and functors on their total categories. |
| `GabrielZisman1967` | Chapter I §1.1 and Lemma 1.2: ordinary localization and its universal property. |
| `DwyerKan1980Calculating` | Definition 2.1, Propositions 2.2 and 3.1, §5.5: hammocks, weak-equivalence arrows, and simplicial localization. |
| `Riehl2016` | Author's current second-edition revision, Theorem 2.2.4, Corollary 2.2.8, Proposition 4.3.7: Yoneda and precomposition adjunctions. The cumulative key is retained; the entry identifies the revision and uses `n.d.`. |
| `GrothStovicek2016Trees` | Actual arXiv v3 PDF, Theorem 9.19 and Corollary 9.23, printed pp. 40–41: stable reflection and reorientation. The HTML renderer instead numbers these 9.21 and 9.25, so the reader explicitly qualifies the PDF version. |
| `AguiarMahajan2010` | Appendix D, especially Proposition D.2, pp. 713–716: the ordered-set universal monoid/comonoid calculation. |
| `MazelGee2018Hammocks` | Published paper, Definitions 3.5, 3.9, 3.17, Remark 3.6, Theorem 4.4: shapes, relative zigzags, hammocks, and the realized three-arrow comparison. |
| `MazelGee2019Rezk` | Theorem 3.8: universality of the relative Rezk nerve. |
| `ArakawaCnossen2026` | arXiv v1, 20 August 2026: Definition 1.1, Theorem 1.9, Corollary 1.11, Convention 4.2, Definition 4.3, Theorem 4.7, Proposition 4.8(b), Example 4.12, Lemma 4.16, Corollary 5.7. |

Broken older Riehl and Dwyer–Kan URLs were replaced by working author-hosted or primary-paper copies under the existing keys. Duplicate cumulative entries were not copied into the final bibliography. No unopened work was marked verified. Exact URLs and DOI metadata are in the bibliography and section reports.

## Verification and reproducibility

Mathematical proofs are the basis of the conclusions. Two independent finite enumerations provide additional checks. The first examined all 63 signed intervals of length at most five, 2,730 full subcategories, 321 adjoint vertex cases, and 845 endpoint-fixing endofunctors. It also checked 1,471 monotone type maps among 961 type pairs of length at most four and 2,731 composable pairs with lengths at most three. The second independently enumerated increasing vertex sections for 21,845 contractions of 255 signed words of length at most seven, testing 254,157 candidate sections. Both passed. Neither computation is offered as a proof for arbitrary length.

`code/assemble.py` applies exactly 20 source replacements: 18 verified reading corrections and two uncertainty-comment resolutions. Printed mathematical errors are not altered. Presentation-only changes are recorded separately: English/French language selection, A4 geometry, line-breaking adjustments, and source marginalia. Three exact layout patches remove one unnecessary inherited page break, keep a paired diagram with its introductory sentence, and keep a footnote invocation with its proposition. The footer separation is 40 points. The original transcription remains available for exact comparison.

The builder was changed in three transparent ways. Ties at a shared anchor preserve commentary-file order instead of sorting blocks lexicographically. A separate front page identifies the commentary, source coverage, and AI production. The bibliography starts on a fresh page. The style selects English within commentary blocks, shortens word anchors in visible headings, and supplies PDF bookmarks. These changes preserve the mathematical source and six-file schemas. Safe exact-word anchors are used where a bare page anchor would split a sentence, list, or argument.

<!-- FINAL_BUILD_RECORD -->
The completed reader has **57 pages** and **41 PDF bookmarks**. The overview occupies reader pages **54–56**, and the ten-entry bibliography occupies page **57**. Its PDF is 690,437 bytes, with SHA-256 `f8ebb3d9fafa73d14c1512b083bce7b049001c734d5783b60383e269568a8ed1`. The final LuaLaTeX pass and BibTeX log contain no errors or warnings: there are no unresolved references or citations, missing glyphs, or overfull/underfull boxes. All 37 commentary titles are present as bookmarks. Schema validation confirms the exact CSV headers, 177 unique audit identifiers, 101 correction records, ten verified bibliography entries, balanced commentary environments, and safe source anchors.

Every reader page was rendered at 150 dpi. Three section reviews inspected all pages through contact sheets and full-size page images; the affected pages were inspected again after pagination repairs. A diagram/footer collision found by visual inspection was repaired even though the compiler had not flagged it. The final footer-band candidates on pages 7 and 24 were examined separately and are visibly clear of the page numbers. No text extends beyond a page's media box. The marginal labels for manuscript pages 49′ and 50′, footnotes, diagrams, and bibliography URLs are readable. `qa/visual_review.md` consolidates the individual section records and the final rendered-page checks.

The build record, schema and anchor validation, rendered-page inspection, and checksums are recorded in `qa/final_validation.json`, `qa/deliverable_validation.json`, and `qa/pdf_inspection.json`. The build uses the supplied builder, BibTeX, and repeated LuaLaTeX passes. The environment lacked a usable LuaLaTeX format and some language/font components, so `code/tex_environment.py` provides an optional workspace-local bootstrap; a complete ordinary TeX Live installation does not need it.

An isolated package check copied only the files selected for delivery, then successfully ran assembly, schema validation, `python build_reader.py DER_VII-a`, and inspection of the existing PDF and logs. The regenerated source transcription, commentary blocks, both CSV registers, bibliography, and reader TeX were byte-identical to the final integrated files. The result is recorded in `qa/package_rebuild.json`. This checks the archive's build-input completeness independently of the production workspace; the final PDF itself was compiled and visually checked as described above.
<!-- END_FINAL_BUILD_RECORD -->

For an ordinary TeX Live installation, run these commands from the extracted archive directory:

```bash
python code/assemble.py
python code/validate_deliverables.py
python build_reader.py DER_VII-a
lualatex -interaction=nonstopmode -halt-on-error DER_VII-a_reader.tex
bibtex DER_VII-a_reader
lualatex -interaction=nonstopmode -halt-on-error DER_VII-a_reader.tex
lualatex -interaction=nonstopmode -halt-on-error DER_VII-a_reader.tex
```

The included `code/build_all.py` runs the same process and writes the validation record. It can use the optional local TeX environment when required. The source-provenance comparison needs the supplied PDF and official complete chapter; their hashes identify both exactly. No source-document inspection is required merely to rebuild the delivered reader.

## Limits and questions left by the installment

No doubtful transcription remains unresolved. No modern open conjecture has been invented from an incomplete sentence or boundary convention. The unfinished source-characterization sentence after Proposition 1(a) is retained as unfinished: a unique completion would require orientation data not supplied by the sentence. Footnote 13's underspecified request is answered by a precise nonconstant-image lemma, with the constant case separated.

The promised category-of-fractions construction lies beyond this installment. The commentary states what the present shape calculus establishes and what a later localization comparison must add. It does not claim to audit the remainder of Chapter VII, reproduce the original manuscript, or settle any global derivator question from this fragment. Literature status is limited to the verified works and versions available on the stated date.

## Production credit

The project supplied the following credit: **“AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), edited with Claude (Anthropic).”** It is preserved here as requested project metadata. This session's production record supports GPT-6 Astra authorship of the commentary, mathematical development, cross-review, and integration; no separate Claude editing pass was performed or independently evidenced in this session. The requested project credit therefore does not certify such a pass on this delivered version. No person is attributed authorship of the AI commentary. Grothendieck and the electronic edition's named transcribers retain their respective source credits.

## References

Aguiar, M., & Mahajan, S. (2010). *Monoidal functors, species and Hopf algebras* (CRM Monograph Series, Vol. 29). American Mathematical Society. https://doi.org/10.1090/crmm/029

Arakawa, K., & Cnossen, B. (2026). *Hammock localization via Segal animae* (Version 1) [Preprint]. arXiv. https://arxiv.org/abs/2608.19870v1

Dwyer, W. G., & Kan, D. M. (1980). Calculating simplicial localizations. *Journal of Pure and Applied Algebra, 18*(1), 17–35. https://doi.org/10.1016/0022-4049(80)90113-9

Gabriel, P., & Zisman, M. (1967). *Calculus of fractions and homotopy theory* (Ergebnisse der Mathematik und ihrer Grenzgebiete, Vol. 35). Springer. https://doi.org/10.1007/978-3-642-85844-4

Groth, M., & Šťovíček, J. (2016). Tilting theory for trees via stable homotopy theory. *Journal of Pure and Applied Algebra, 220*(6), 2324–2363. https://doi.org/10.1016/j.jpaa.2015.11.009

Grothendieck, A. (1971). *Revêtements étales et groupe fondamental (SGA 1)* (Lecture Notes in Mathematics, Vol. 224). Springer. https://doi.org/10.1007/BFb0058656

Grothendieck, A. (1990–1991). *Les Dérivateurs, chapitre VII: Catégories de chemins (2)* [Manuscript; electronic edition, December 22, 2001]. https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html

Mazel-Gee, A. (2018). Hammocks and fractions in relative ∞-categories. *Journal of Homotopy and Related Structures, 13*(2), 321–383. https://doi.org/10.1007/s40062-017-0184-0

Mazel-Gee, A. (2019). The universality of the Rezk nerve. *Algebraic & Geometric Topology, 19*(7), 3217–3260. https://doi.org/10.2140/agt.2019.19.3217

Riehl, E. (n.d.). *Category theory in context* [Author's online second-edition revision; first edition published in 2016]. Retrieved November 10, 2026, from https://emilyriehl.github.io/files/context.pdf
