# DER_VI-c: editorial and mathematical report

## Scope and source authority

This package concerns manuscript pages 138–204 of Chapter VI, together with the final incomplete paragraph of §9. The attached PDF has 43 file pages, whose actual printed labels are **85–127**. The transcription begins one printed page earlier, on page **84**. The prompt's range “87–129” counts the two preliminary PDF pages in the complete chapter and is not the printed pagination. We use manuscript numbers for mathematical references; `pdf_page` in the corrections table means the one-based page of the attached PDF. A supplemental-page entry explicitly identifies the official complete chapter when no attached PDF page exists.

Printed page 84 was inspected in the editors' official complete Chapter VI PDF, file page 86 (zero-based page index 85), version 9 November 2001. It supplies the opening paragraph and manuscript markers 138–139. The square's `\Phi_S(X'/S')` really is printed there; it is an edition slip, not a transcription error. The supplied PDF remains authoritative wherever it covers the transcription.

Manuscript page 170 is explicitly missing in the edition. The final §9 ends with the editors' `[la suite manque]`. Neither lacuna has been reconstructed or passed off as recovered text. Mathematical consequences needed for reading the surviving discussion are supplied in separately marked commentary.

The supplied continuity index ends with DER_VI-a, manuscript page 70. It contains no DER_VI-b entry. We have used all of the supplied index and refer to its named blocks where appropriate; we cannot claim comparison with an unavailable commentary on manuscript pages 71–137.

## Editorial method

The transcription is checked against the attached PDF, with visual inspection for diagrams, indices, doubtful underlining, and arrow styles. Every input `% ??` receives a corrections-table entry. Every input `% [sic]` is checked rather than accepted on the transcriber's authority. The corrections table also records newly identified edition slips. Corrections classified `transcription` are applied to the supplied text; a confirmed erroneous edition reading remains in the source and is explained in the audit and commentary.

The audit separates assertions at the time they occur from their later retractions or repairs. A false start that Grothendieck explicitly retracts is not treated as an unnoticed error. A stated theorem with a proof completed later in this extract is distinguished from an argument requiring a genuinely additional assumption. Historical labels such as “open” are accompanied by a separate present-status note and the exact range of the literature verification.

## Authorship and provenance

The commentary and audit in this delivery are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). The package specification requests the series credit “edited with Claude (Anthropic)”. No Claude editing pass was performed or independently verified in this session; that requested credit is recorded here as supplied editorial metadata, not asserted as an action completed for this delivery. No human is credited as author of the commentary.

## Completed package

The six prescribed editorial files are complete. The interleaved reader contains 37 commentary blocks in all six required categories, approximately 16,500 whitespace-delimited word tokens including formulas. The claims ledger has 226 rows. The correction ledger has 51 rows. The bibliography contains 13 opened and verified works. The compiled reader has 66 pages; the overview occupies pages 63–65, approximately 2.6 pages.

The claims ledger covers the definitions, axiom changes, propositions, conjectures, questions, and substantive footnotes throughout the surviving manuscript pages 138–204. Page 170 has no recoverable assertions. The statement field specifies the mathematical assertion; the gap, repair, and notes fields distinguish the argument written here, subsequent corrections, and the present conclusion. Some historical questions retain `open` as their manuscript status while their repair field gives the modern affirmative answer. Rows B029, B033, and B064 expressly use `proved` for the repaired current implication, and B065 uses `false` for the precise modernly excluded conjecture. Those conventions are explained in their notes; none should be read as saying that an unwritten proof occurs in Grothendieck's text. The commentators' independent results have their own audit rows.

The archive includes the corrected transcription, the unchanged supplied builder, the adapted style, the built reader TeX and PDF, the original supplied materials, the reviewed section fragments, the executed audit/build code, and the verification logs. The reviewed fragments are the authoritative inputs to `code/assemble.py`; the earlier CSV-writing helpers are retained as execution history and are not rerun by the final rebuild command.

## Diplomatic correction results

All five input `% ??` markers have been resolved. Three require changes to the transcription:

| Manuscript page | Attached PDF page | Verified change |
| --- | --- | --- |
| 141 | 2, printed 86 | The curved arrow labelled `i_{X'}` has a solid shaft. |
| 144 | 4, printed 88 | The curved identity arrow has a solid shaft. |
| 155 | 10, printed 94 | `Liss` has one underline. |

The other two doubts require no mathematical change: the marks on manuscript page 185 are overlines on the saturated equivalence classes; the argument of `hot` in the underbrace on page 201 is an ordinary argument, not part of its subscript. The additional `doubt_resolved` record concerns the final printed lacuna. Thus the 51 correction rows comprise three `transcription` records, three `doubt_resolved` records, and 45 `edition_slip_kept` records.

All 28 input `% [sic]` markers were checked and are covered by the ledger. The 45 retained-source records include grammatical and typographical slips, incorrect indices, already bracketed editorial repairs, and mathematical wording that needs clarification. They should not be interpreted as 45 independent false theorems. Among the significant retained readings are the incorrect base in the opening square, the wrong target of `i_X` on page 144, the base index of the pointwise `hot` on page 158, the reversed addition/deletion sentence on page 190, the incorrect central fibre in the diagram on page 191, and the repeated base index at the start of printed page 124.

Only the three verified reading changes are applied to the source body. The five doubt comments now point to the correction ledger. Separate typesetting changes enable English in the commentary, keep the mathematical fonts compatible with LuaLaTeX, and fit the paired diagram before manuscript page 198 within the reading column without changing any label or arrow. `work/source_edits.json` records these changes. The original attachment is retained byte-for-byte under `sources/`.

## Mathematical findings and completed arguments

### Adjunction, products, and the pointwise formula: pages 138–159

The construction of `f_! ⊣ f^*` is sound. The unsuccessful attempt to invert an arbitrary pullback of `i_X` is explicitly replaced by the correct fraction `(i_X)^{-1} pr_1^{Phi(X)}` in the localization over the original base. The commentary supplies both triangle calculations and the naturality needed when the formal reflection argument is passed through localization. Essential surjectivity alone would not justify that passage; the relevant natural transformation descends because precomposition with a localization is fully faithful on functor categories.

The product corollary is false and is retracted by Grothendieck himself. The walking-arrow example is computed on its fibres and comma fibres. It shows why multiplication by a specified category over the base depends on that representative. The valid identity is `f_! f^* = multhot_{S'/S}`. Identification with the internal product needs its own comparison argument.

The comma square on page 157 is lax. Its structural natural transformation, with the presheaf variance used throughout the chapter, gives the standard mate `f'_! q^* → p^* f_!`. The reverse direction displayed in the source is obtained after that mate has been proved invertible. The commentary checks the canonical mate on representatives; it does not substitute an unspecified isomorphism between its source and target.

Theorem 3's Der 2 assertion is withdrawn in footnote 76. Its historical proof remains incomplete. The modern repair is recorded in the p159 block and A050; it applies to every basic localizer. Strong saturation is also a theorem in that setting (Cisinski, 2006, Proposition 4.2.4), so the source's saturation qualifications record its proof stage rather than a further modern axiom.

### Base change and the revised axioms: pages 160–181

The proper/smooth base-change theorem is completed by the direct representative calculation on pages 168–169. This removes the earlier reliance on the then-unproved conservativity assertion. The Hom-set calculation for a `HOT_W`-equivalence is kept distinct from conservativity of every arrow in a localized diagram category.

The audit tracks total, strict-fibrewise, right-fine, left-fine, and relative universally fine equivalences separately. On weak `W`-fibrations the fine tests agree and imply total equivalence. Their converse is the fibre-detection axiom W(4b). The definition of relative universality is taken over the specified base; it is not replaced by an unrelated absolute pullback condition.

The four localized categories and their comparison arrows therefore retain their distinct meanings. In particular, a coarse replacement whose unit is merely a total equivalence does not prove that the fine and coarse theories agree. The action-groupoid example with connected-component equivalences calculates the resulting loss of faithfulness on morphisms, even on perfect objects.

The three minimum classes discussed in this extract all identify with `W_infty` today. For `W'_omega`, basic minimality gives one inclusion and Quillen's Theorem B makes `W_infty` an admissible fibre-detecting candidate for the other. The p172 commentary supplies the short proof and retains the standing axioms in the footnote's minimum. Containment of this minimum does not make an arbitrary larger localizer satisfy W(4b).

### Alternating completion and the reflection repair: pages 182–197

The finite branching example is checked by explicit retractions and natural transformations. Its final emptiness conclusion needs one additional step: after producing an arrow into one maximal fibre, apply the other maximal-fibre test to its target. The resulting comma category is empty. The erroneous central label in the printed diagram is independently confirmed against the PDF and preserved as an edition slip.

For the alternating completion, the commentary proves sequential stability of smoothness and properness through their lifting categories. The relevant objects, arrows, and equations are witnessed at finite stages. The odd and even subsequences are cofinal, and the unit is a total equivalence for arbitrary input and a fibrewise equivalence for weakly fibred input. The induced localization equivalence is proved on morphisms as well as objects by explicit quasi-inverse functors and the two unit isomorphisms.

Modern closure and minimality results remove the extra sequential hypothesis for the standing basic-localizer application. The argument in the commentary gives a common fine replacement in `Parf_omega`. It consequently identifies the fine localizations of all full intermediate subcategories containing that replacement. Applying the restricted fibre-detection test to the replaced morphism, then using the two fine units, also repairs the original W(4b′) implication. This does not make W(4b) true for an arbitrary basic localizer: its restricted test is still a hypothesis.

The omission on page 197 is repaired under the precise two cases of the proposition. Case 1 uses the established reflector `C`. In case 2, `R=Phi_infty` is compared with `C` by the natural isomorphism `(alpha_{RX})^{-1} C(eta_X)`, and the equality of units is proved. Precomposition with `eta_X` is then bijective on maps into the local object `R²X`; naturality yields `eta_{RX}=R(eta_X)`. This is justified cancellation through a universal property, not cancellation of an arrow merely assumed invertible.

The references to “XVI 4.9” in notes 95–96 are located by their statements. In the current electronic Chapter XVI, the relevant replacement and transfer results occur in §4.4, especially Lemma 4.4.9, Corollary 4.4.10, and Theorem 4.4.13.

### Restriction and the last product question: pages 198–204

The restrictions on lateral and locally constant theories are constructed on their appropriate good representatives. Compatibility with the coarse localization is checked separately. The last base-change fragment is kept incomplete. Its expected theorem is proved in commentary with the Cartesian-square hypothesis explicitly added; that hypothesis is not silently attributed to the surviving sentence.

The product question has a positive answer. Under W(1,2,3), if `X→S` is weakly `W`-fibred in the universally stable sense of the chapter, then for every `Y→S` the canonical map

\[
[X\times_S Y]\longrightarrow[X]\times_S[Y]
\]

is invertible. The proof first treats `X=∫F` with all transports in `W`. Over `B=s\Y`, transport along the displayed arrow `s→q(y)` defines a fibrewise `W`-equivalence to `F(s)×B`. A fibre-to-comma adjunction shows that this map is exactly the canonical product comparison followed by a `W`-equivalence. Two-out-of-three proves the comparison itself. The universal fine unit `X→Phi(X)` reduces the general case to this split one. This argument does not assume W(4b). The additional properness or smoothness suspected necessary at the end of page 202 is therefore unnecessary under the stated fibred hypothesis.

## Independently proved developments

Four results are explicitly marked `\ours`, each with a precise statement and complete proof. This marker identifies work supplied by the commentators; it makes no claim of priority.

| Anchor | Result and role |
| --- | --- |
| p155 | For a full inclusion of finite posets, the universal comparison `u_!u^*F→u_!1×F` holds for every space-valued presheaf exactly when the subposet is a lower ideal. Necessity is detected by a representable. |
| p178 | For connected-component equivalences over `BG`, fine localization retains the action, while coarse localization is computed by orbits. Distinct translations of the regular right `G`-set demonstrate nonfaithfulness of the comparison. |
| p192 | A poset with a least object and two distinct maximal objects obstructs properness of the comma completion of every nonempty category over it, for a nondegenerate localizer. |
| p202 | A weakly fibred factor suffices for the canonical product comparison, with arbitrary second factor. |

The supplied proofs were independently checked across the three section reviews. The finite-poset statement is deliberately modest in scope; its proof does not actually need finiteness. The groupoid-base bifibration comparison and the full-sieve pushout calculation are also proved, as elementary explanatory arguments. They are not presented as newly discovered general theories.

## Remaining limits

The ordinary-bifibration fine-localization comparison over an arbitrary base was not established or located in the checked literature, including in the usual nerve-equivalence case. The commentary proves it for groupoid bases. Clarke, Scherer, and Zeilberger (2025, Theorem 1.17) provide a free categorical bifibration, but the fibrewise equivalence of its unit required here was not verified. Lamarche's antecedent path construction has a different weak-equivalence scope. `work/bifibration_status.md` gives the exact missing criterion and the primary-source checks. This is a limit of the present audit, not a declaration that the general question is presently open throughout the literature.

The modern automatic-colimit argument is used with relative W(2). We did not establish its analogue for every weak basic localizer defined using only absolute Theorem A, and we found no verified counterexample that would justify calling that broader assertion false. This distinction does not prevent any of the standing-W applications made in the commentary.

The manuscript's illegible cohomology index on page 190 can be corrected mathematically from the surrounding construction, but the original handwritten index cannot be deciphered from an edition that itself marks it illegible. Likewise, page 170 and the final continuation cannot be recovered from the supplied materials. These textual limits remain visible.

## Primary-reference verification ledger

All entries in the delivered bibliography have `note = {verified}` and a URL or DOI. The following are the exact principal locations opened; theorem numbering is preferred where author preprints and printed editions paginate differently.

| Work | Verified loci | Primary text |
| --- | --- | --- |
| Grothendieck (1983), *Pursuing Stacks*, §69 | Both adjoints to restriction; excerpt pp. 1–2 | [Section 69](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/ps-69.pdf) |
| Grothendieck (1990), Chapter VI | Entire attached extract; supplemental printed p. 84 | [Complete Chapter VI](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChVI-345.pdf) |
| Grothendieck (1990–1991), Chapter XII, I–IV | Axioms on ms. p. 1; Part III, Theorem 3 and Definition 4, ms. pp. 51–52 | [Chapter XII, I–IV](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChXIIa-012.pdf) |
| Grothendieck (1991), Chapter XVI | §4.4, especially 4.4.9–4.4.13; 2019 electronic edition | [Chapter XVI](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/der-ch16.pdf) |
| Cisinski (2003) | Theorem 6.11 and Proposition 6.13 | [Numdam PDF](https://www.numdam.org/article/AMBP_2003__10_2_195_0.pdf) |
| Cisinski (2004) | Definition 1.1.3; Theorems 2.2.11 and 2.3.6 | [Author PDF](https://www.math.univ-toulouse.fr/~dcisinsk/winfax.pdf) |
| Cisinski (2006) | 3.1.30; 3.3.2; 4.1.29; 4.2.3–4.2.7; 4.2.22; 6.4.1; 6.4.17 | [Author PDF](https://www.math.univ-toulouse.fr/~dcisinsk/ast.pdf) |
| Cisinski (2009) | Theorems 1.3, 1.10; Remark 1.11; Corollary 1.28 | [Author PDF](https://www.math.univ-toulouse.fr/~dcisinsk/lcmodcat3.pdf) |
| Maltsiniotis (2005), *Structures d'asphéricité…* | Theorems 1.2, 4.13, 5.4; Proposition 4.3; Example 4.17; Proposition 5.3; Remark 5.5 | [Numdam PDF](https://www.numdam.org/article/AMBP_2005__12_1_1_0.pdf) |
| Groth (2013) | Definition 1.5; Propositions 1.23, 1.24, 1.26, 1.30 | [Publisher PDF](https://msp.org/agt/2013/13-1/agt-v13-n1-p10-s.pdf) |
| Riehl (n.d.), online revision of *Category Theory in Context* | Proposition 4.3.8; Lemma 4.5.11; Definition 4.5.12 | [Author PDF](https://emilyriehl.github.io/files/context.pdf) |
| Clarke, Scherer, and Zeilberger (2025) | Theorem 1.17; Propositions 1.23–1.24; Corollary 2.5; Theorem 2.7 | [Author PDF](https://bryceclarke.github.io/preprints/the-free-bifibration-on-a-functor.pdf) |
| Lamarche (2013), *Path Functors in Cat*, v3 | Theorem 3 and §4, pp. 20–23 | [Author-uploaded full text](https://www.researchgate.net/publication/281566170_Path_Functors_in_Cat) |

The cumulative key `Grothendieck1990XII` names a different part of the chapter, so `Grothendieck1990XIIa` is used for the verified I–IV PDF. The key `Riehl2016` is reused, but its entry specifies the actually opened online revision and uses `n.d.` rather than inventing a revision date. Numbered citations to that work refer to the opened revision. The bibliography does not assert that a source was read merely because it was named in a search result.

## Build and quality checks

The supplied `build_reader.py` is byte-identical to the kit copy. It accepts all six files, all 37 anchors, and all citation keys. The successful sequence was builder, LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX. `code/rebuild.py` reproduces it, and `code/verify.py` records schemas, allowed values, unique claim identifiers, bibliography coverage, preserved source markers, PDF page counts, and final-log checks in `DER_VI-c_validation.json`.

The final LuaLaTeX pass has no errors, undefined citations, missing characters, or overfull boxes. BibTeX has no warnings. The remaining LaTeX messages are automatic movements of marginal source-page labels and three underfull boxes. They were visually checked: there is no clipping or overlap. Representative pages from the beginning, long diagrams, new status material, reflection proof, product proof, overview, and bibliography were inspected. All extracted text spans lie inside their PDF pages.

This environment had the LuaHBTeX engine but lacked its format and some language/font data. The missing data were installed in the task directory without changing system files; `code/bootstrap_tex.py` and `code/run_tex.py` record that setup. A complete normal TeX Live installation can use the ordinary build commands in `README.md`. The archive omits the large downloaded TeX caches and packages but includes their URLs and checksum manifest.

The style changes are limited to a wider A4 reading column, clear English commentary headings, short manuscript anchors in headings, and suitable mathematical font handling. No change to the machine-readable format is proposed. For a future format revision, separate historical and current-status columns would make the chronology even easier to query; the present delivery retains the prescribed schema and records that distinction in its existing repair and notes fields.
