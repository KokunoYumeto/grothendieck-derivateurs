# Les Dérivateurs, Chapter II-a: audit and commentary report

## Scope, source, and editorial responsibility

This delivery covers manuscript pages 1–53, including the inserted pages 36bis and 36ter, and edition pages 1–33. The mathematical transcription, its annotations and footnotes, the supplied earlier-package index, and the cumulative bibliography were read. Every substantive definition, numbered result, conjecture, question, proof step, and mathematical footnote in this range was assigned an audit record. The reader stops where the supplied transcription stops, during the proof of Proposition 4.1; the completed proof supplied in the commentary is identified as our completion, rather than attributed to the truncated excerpt.

There is a pagination discrepancy in the attachments. The supplied PDF contains 33 physical pages: two preliminary pages followed by edition pages 1–31. Its LaTeX transcription continues through edition page 33. We obtained the editors’ complete Chapter II PDF, version 8 July 2001, from the [official edition](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChII-234.pdf). Text extraction from each of its first 33 physical pages agrees exactly with the corresponding supplied page. The next two physical pages supply edition pages 32–33. Those pages were rendered and visually checked along with the supplied pages. Accordingly, `pdf_page` values 34–35 in the correction table refer to this explicitly identified continuation of the same edition.

The edition is the authority for readings. The handwritten manuscript was not supplied, so `edition_slip_kept` does not decide whether an error originated with Grothendieck, a decipherer, or an editor. It records that the questionable expression is actually printed in the authoritative edition. We preserve those expressions in the French source and explain their mathematical repair separately. The original uploaded LaTeX is preserved under `original/`; the corrected, compilable transcription is also included.

The required six deliverables are complete. The archive additionally contains the built reader, its source and style, the unchanged supplied builder, the corrected source, and the scripts and data needed to reproduce the assembly and checks.

| Item | Final extent |
|---|---:|
| Commentary blocks | 38 |
| Commentary words, approximately, including mathematical tokens | 13,351 |
| Claims audit records | 245 |
| Correction records | 77 |
| Verified bibliography entries | 18 |
| Built reader pages | 50 |
| Overview pages in the reader | 3 |

The commentary uses the earlier packages only through the supplied index. References to their block titles distinguish continuity from a claim to have reread unavailable full earlier readers. No additional files from prior conversations were accessed.

## How to read the audit

The `proof_status` column describes the treatment in this excerpt, while `repair` and `notes` describe the mathematical resolution and later status. Thus an assertion may be `stated` here but proved in the commentary; a question can be `open` at its point in the manuscript and settled immediately in our discussion. The three rows carrying `open` explicitly explain this local meaning. They must not be read as a list of currently unsolved research problems. Likewise, `false` includes proposed assertions which the edition itself retracts. Counting such rows does not count previously unnoticed errors by Grothendieck.

The audit separates the manuscript’s provisional terminology from its final corrected statements. In particular, ordinary connectedness, nonempty connectedness, weak cofiltering, PS1, PS2, ordinary siftedness, and homotopical contractibility remain distinct. The positive connected-object assertions in the middle portion explicitly concern noninitial connected objects. Directions of comma categories are stated before the cofinality arguments; the later change from predecessor to successor conditions is also made explicit.

There are 11 correction records classed as `transcription`, 1 as `doubt_resolved`, and 65 as `edition_slip_kept`. Several records address a repeated formula or a whole displayed diagram. These are records, not counts of individual glyph changes. The exact replacement manifest separately records each programmatic source replacement and its expected number of matches.

## Principal mathematical conclusions

### Cofinality and the derived weight

For a functor \(u:C'\to C\), the presheaf \(K_u(c)=\pi_0(c\backslash C')\) represents the functor \(F\mapsto\Gamma(C',u^*F)\). Its augmentation to the terminal presheaf gives the precise ordinary cofinality criterion: every indicated comma category must be nonempty and connected. The manuscript’s initial weak cofiltering condition is sufficient but stronger than necessary. The relative problem has two endpoints and is controlled by categories of factorizations, explaining why invariance of global sections does not itself make restriction fully faithful. These identifications agree with SGA 4, Exposé I, §8.1 (Artin et al., 1972).

The abelian cohomological question on manuscript page 5 has an affirmative answer. The commentary constructs a projective bar resolution and proves

\[
(\mathbf L u_! k_{C'})(c)\simeq C_*(N(c\backslash C');k).
\]

Derived adjunction then proves invariance for all complexes of coefficients when the comma nerves are weakly contractible. For a fixed commutative ring, acyclicity with that ring’s coefficients already suffices. The higher categorical cofinality theorem supplies the parallel statement for spaces (Lurie, 2009, Theorem 4.1.3.1). The proof here does not depend on the stronger internal-Hom assertion made later in the manuscript.

That unrestricted internal assertion is false. For the terminal-vertex inclusion \(i:\{1\}\hookrightarrow[1]\), a presheaf is an arrow \(F_1\to F_0\), and

\[
i_!A=(A\xrightarrow{1}A),\qquad i_*A=(A\to *).
\]

The global adjunction holds, but \(\underline{\operatorname{Hom}}(i_!1,F)=F\) need not equal \(i_*i^*F\). The projection comparison has the canonical direction \(u_!(u^*G\otimes H)\to G\otimes u_!H\); its inverse direction is not available before proving invertibility. Frobenius reciprocity is the additional condition, with its sliced form required for local connectedness (Garner & Streicher, 2021, §1).

### Irreducibility, filtering, and the hereditary condition

The topos discussion is reconstructed with the distinctions which the manuscript progressively discovers. Irreducibility of the presheaf topos records common predecessors in the reachability preorder. Local irreducibility records PS1. Equalization of arbitrary parallel arrows is PS2 and is genuinely additional. The parallel-arrow category and a nontrivial one-object groupoid separate these conditions. The four-object example at the boundary of manuscript pages 16–17 is also treated explicitly, rather than lost between the two adjacent discussions.

In Theorem 2.6 the surviving equivalent assertions are (a), (a′), (b), and (d). The generator-slice tests (c), (c′) are weaker, as the edition’s annotations already say. The commentary supplies the omitted generator-component proof in Lemma 2.9 and the successive equalizations in Lemma 2.10. It records the missing connectedness of the base in Corollary 2.8(b). The groupoid answers the first request in Perplexity 2.11. The second requested example cannot exist: if all representable slices are totally 0-connected, those slices also satisfy local irreducibility, and Corollary 2.7 makes them cofiltered.

Ordinary total 0-connectedness of a presheaf topos is ordinary siftedness of the opposite indexing category. It is weaker than the hereditary local condition needed later. The cohomological induction on pages 30–32 must remain within connected, locally totally 0-connected topoi, because it repeatedly passes to connected slices. The commentary gives the contracting homotopy for the augmented Čech complex and proves the homotopical assertion directly: exactness of the component functor carries hypercover matching epimorphisms to boundary-filling maps of simplicial sets. Every resulting component simplicial set is weakly contractible. The reference to Artin and Mazur (1969, §§8–9) concerns the classical hypercover construction; the proof of the assertion needed here is written out.

The vanishing concerns constant coefficients and the classical hypercover homotopy type. It does not eliminate arbitrary sheaf cohomology. The explicit affine-cover computation \(H^1(\mathbf P^1_k,\mathcal O(-2))\cong k\), using Serre’s affine comparison, makes that distinction concrete (Serre, 1955, no. 47, Theorem 4).

The ind-object criterion is proved in both directions: a presheaf is a filtered colimit of representables exactly when its category of elements is filtered. The general statement is SGA 4, Exposé I, Theorem 8.3.3; the directed-poset reindexing is Proposition 8.1.6, explicitly attributed there to Deligne. Left Kan extension then proves the preservation assertion in 2.17. Cisinski’s minimal-localizer theorem strengthens the historical asphericity conclusion under the modern fundamental-localizer axioms, without the extra Loc(8) hypothesis (Cisinski, 2004, Theorem 2.2.11).

### The withdrawn total-asphericity claim

For manuscript page 36 we use \(T(A)\) to mean that every ordinary cofinal functor \(A\to E\) has weakly contractible target nerve. This is the exact universal quantifier on that page. It is not the later diagonal-based definition of total asphericity in Maltsiniotis (2020, §1.7).

The correct part of Proposition 2.19 is preservation of ordinary siftedness under ordinary cofinal images. Its inference to weak contractibility is false and explicitly withdrawn in the edition. We complete the counterexample by adjoining one closed object to \(\Delta\) using the simplicial circle \(H=\Delta[1]/\partial\Delta[1]\). The nerve of the resulting collage has the homotopy type of the mapping cone of \(B(\Delta/H)\to B\Delta\), hence of \(S^2\). The opposite inclusion is ordinary cofinal, so this gives the required explicit failure for \(\Delta^{\mathrm{op}}\).

There is a separate defect in the appeal to Chapter XII: the reflection step used by II 2.20 needs the strong biconditional form of \(W(7\mathrm{bis})\). The source is XII §V.3.4, Corollary 4, printed page 103, manuscript pages 149–150, especially note 104; notes 93–98 at Theorem 4 distinguish the direct gluing theorem from the extra reflection hypothesis (Grothendieck, 1990–1991). That reflection fails for ordinary nerve weak equivalences. The circle computation avoids it completely. The conditional corollary in XII is not classified as an unconditionally false theorem.

Here is the independent obstruction to reflection. A connected finite acyclic noncontractible complex has contractible suspension: van Kampen gives simple connectivity, Mayer–Vietoris gives vanishing reduced homology, and the homology Whitehead theorem applies. Such a complex is supplied by Hatcher’s presentation with relators \(a^5b^{-3}\) and \(b^3(ab)^{-2}\). Its cellular boundary matrix is

\[
\begin{pmatrix}5&-2\\-3&1\end{pmatrix},
\]

of determinant \(-1\), while \(a=(1\,2\,3\,4\,5)\), \(b=(2\,5\,4)\) gives a nontrivial permutation quotient. Replace it by a finite homotopy-equivalent simplicial complex \(K\). The face posets of the two cones on \(K\) form an open cover of the face poset of \(\Sigma K\). Each cone and their union is weakly contractible, while their intersection has the noncontractible homotopy type of \(K\). Thus a weak equivalence from a cone into the union does not reflect to the intersection. The inputs are Hatcher (2002, Example 2.38, Theorem 2C.5, Corollary 4.33); the face-poset argument is given here explicitly.

### Degree zero and recovery of diagrams

The localization in Section 3 is identified with the represented derivator of sets through the adjunction between connected components and discrete categories. The relative localization uses comma components, not only components of the total category. The lifting conditions, arrow tests for universal \(W_0\)-equivalence, and componentwise criterion for strong \(W_0\)-fibrations are proved. The translation covering \(EG\to BG\) distinguishes the weak condition from the strong \(W_0\)-condition; it is not presented as a failure of the corresponding \(W_\infty\)-statement.

The filtering argument in Corollary 3.4(d) and the related footnote requires the right Ore condition, whereas the earlier use of PS1 was left-handed. The correction record preserves the printed terminology and the commentary states the required direction. The fully faithful inclusion \(\{1,2\}\to(0\to1,0\to2)\) supplies a counterexample to a literal left-handed reading: it satisfies the objectwise successor condition, but the comma under 0 has two components.

Footnotes 53 and 55 are treated separately. For locally connected topoi, preservation of noninitial connected objects is the component-preserving asphericity condition; the all-sections condition is coasphericity. For morphisms induced by indexing functors these are initiality and finality, respectively. The higher-degree suggestion is recorded with its coefficient dependence rather than assigned an unspecified universal meaning. Footnote 55's later reference was checked in Chapter XVIII, Lemma 4.9.6.3 and its proof. Eventual lifting of an arrow between image objects after postcomposition is the additional F3 condition. With the target right Ore condition, F1 and F3 imply cofinality; if the functor is faithful, its source satisfies the right Ore condition and is filtered whenever its target is filtered. The commentary gives the two successive lifts explicitly. The faithful filtered case is the cited lemma; our finite synthesis also explains where the weaker Ore hypothesis suffices. The bounded-cardinal version retains its additional simultaneous-lifting hypothesis.

Manuscript page 51 has a coefficient-dependent failure even for an ordered indexing category. Let \(I=[1]\), \(I'=\{1\}\), and let \(\mathcal M\) be a discrete two-object category. Restriction of \(\mathcal M\)-valued diagrams is an equivalence. The slice comparison at 0 is nevertheless \(\varnothing\to *\), and the corresponding comparison in \(\widehat{\mathcal M}\simeq\mathrm{Set}\times\mathrm{Set}\) is

\[
(1,\varnothing)\longrightarrow(1,1),
\]

which is not invertible. Abstract existence of the adjoints does not repair this example. The argument needs the relevant pointwise comma limits, for example completeness of the coefficient category. The independent extension argument for posets is supplied by the monotone retraction onto a principal downset; it does not manufacture missing limits.

Proposition 4.1 is valid after changing the printed coslice criterion in (d′) from cofinal to co-cofinal, that is, initial. Its corrected equivalences are proved using connected nonempty categories of factorizations of every arrow through the indexing functor. The later terminology is lax epimorphism or absolute density (Adámek et al., 2001; Lucatelli Nunes & Sousa, 2022, Theorem 4.1). The homotopical version replaces connectedness by weak contractibility (Groth & Šťovíček, 2016, Theorem 6.10). A quotient of groups gives the worked comparison: the factorization category has the homotopy type of the classifying space of the kernel.

## Developments and the boundary of the status search

Every result offered as our continuation of an unworked calculation is marked `\ours` in a development block, with a statement, proof, and explicit absence of a priority claim. There are four such developments. The point-inclusion criterion gives the exact projection-formula obstruction. The four-object presentation on page 16 has nerve homotopy equivalent to \(\mathbb RP^2\): removing its first object is a categorical deformation retraction, and the remaining category is the orbit of the ordinal sum of three two-point sets under simultaneous interchange. Its nerve realizes to the antipodal quotient of an octahedral sphere. The source’s crossed composition relations are exactly addition modulo two. The literature check did not locate this identification for the particular presentation; the join and antipodal descriptions themselves are classical (Hatcher, 2002, p. 9 and Example 1.43). The independent program confirms rational Betti numbers \((1,0,0)\) and mod-two Betti numbers \((1,1,1)\), consistent with the explicit topological proof.

The common-successor theorem proves

\[
T(A)\Longrightarrow A\ne\varnothing\quad\text{and}\quad
\text{every pair of objects has a common successor}.
\]

It follows that \(T(A)\) is equivalent to filteredness for preorders. The obstruction uses a four-object category with a cofinal three-object subcategory and a displayed integral two-cycle generating \(H_2\cong\mathbb Z\). The independent finite-category program checks composition and associativity, comma connectedness, boundary-square zero, rational Betti numbers, and the nonzero integral cycle. The written proof establishes the integral homology assertion; a numerical computation alone would not establish it.

For arbitrary categories we did not locate a resolution of \(T(A)\Rightarrow A\) filtered under this exact quantifier. The remaining issue is equalization of parallel arrows; the proof does not establish the stronger intermediate siftedness assertion either. Searches used the exact conjectural formulation and English and French combinations of total asphericity, cofinality, and filtering, and checked the treatments of Maltsiniotis, ordinary sifted categories, and lax epimorphisms. Much of the literature uses a different definition of total asphericity. This is a bounded failure to locate a resolution, not a claim that the question is recognized as open across the literature.

The fourth marked development is the finite eventual-lifting synthesis discussed above. Its faithful filtered specialization is explicitly attributed to Chapter XVIII; the weaker Ore formulation is proved here.

The analogous search for the point-evaluation projection criterion used the pointwise Kan-extension treatment of Riehl and the Frobenius discussion of Garner and Streicher, together with exact searches for evaluation, exponentials, and incoming invertible arrows. No matching formulation was located in those checked sources. Elementary proofs and explicit modest framing are preferable here to unsupported novelty claims.

The edition’s own `[mot(s) illisible(s)]` and `[?]` annotations remain. They report uncertainty already present in the edition; the supplied material cannot recover the absent handwriting. They are distinguished from the transcription’s `% ??`, which has been fully resolved.

## Literature opened and extent of verification

Every bibliography entry has a URL or DOI and the required `note = {verified}`. Here “verified” means that the source or its primary bibliographic record was opened. It does not mean that every page of every book was read. Exact theorem references were checked in accessible full text; metadata-only checks are identified below. Existing cumulative keys were retained, including the historical `Riehl2016` key for the current author-hosted second-edition revision.

| Bibliography key | Material actually checked |
|---|---|
| `Grothendieck1990II` | Supplied edition through printed 31, official continuation through printed 33, matching first 33 physical pages, and edition identification. |
| `Grothendieck1990XII` | §V.2.1 strong gluing formulation; §V.3.4, Theorem 4 and Corollary 4, including the qualifying notes. |
| `Grothendieck1990XVIII` | Official edition of 17 December 2025, Lemma 4.9.6.3, printed pages 81–82, and its proofs in §§4.9.6.7–4.9.6.10. |
| `Grothendieck1983` | Editor-hosted *Pursuing Stacks*, §69, especially excerpt pages 1–3 on coherent diagram categories. |
| `SGA4I1972` | Authoritative Orgogozo–Laszlo reedition of Tome I, version 71766d9 of 30 July 2024; Exposé I §2.7, §8.1, Proposition 8.1.6, and Theorem 8.3.3. Original publication metadata also checked. |
| `Heller1988` | Full primary scan; Chapter II §1, Chapter III §2, and Chapter IV tensor/cotensor setting. |
| `Lurie2009HTT` | Author-hosted full PDF; §4.1, Theorem 4.1.3.1 and related results, plus the filtered/sifted-colimit discussion in §§5.3.3 and 5.5.8. |
| `Riehl2016` | Author-hosted second-edition revision; pointwise Kan extensions in §6.2, especially Theorem 6.2.1 and Corollary 6.2.9. The metadata does not falsely identify this revision’s pagination with the first edition. |
| `GarnerStreicher2021` | Author-hosted full draft, §1, and institutional publication metadata; Frobenius versus stable Frobenius and the relation to exponentials. |
| `Cisinski2004Minimal` | Author-hosted scan, Theorem 2.2.11, printed page 136, and Numdam bibliographic record. |
| `Serre1955FAC` | Collège de France scan, no. 47, Theorem 4, printed page 239. The projective-line computation is then supplied explicitly. |
| `Hatcher2002` | Author-hosted full PDF, Example 2.38, printed page 142; Theorem 2C.5, page 182; Corollary 4.33, page 367. |
| `Maltsiniotis2020` | Author-hosted expanded provisional version, Definition 1.7.2, surrounding propositions, Proposition 1.7.14, and relevant later sections. |
| `GrothStovicek2016Trees` | Full author preprint, Theorem 6.10, and the primary arXiv publication record. |
| `NunesSousa2022` | Full author preprint, Theorems 4.1 and 5.6, and publisher metadata. Theorem 4.1 explicitly attributes the ordinary factorization criterion to the 2001 paper. |
| `AdamekElBashirSobralVelebil2001` | Official TAC abstract and metadata. The original PDF repeatedly failed to load; no unchecked theorem number from it is quoted. The precise criterion was checked in the 2022 paper and proved here. |
| `AdamekRosickyVitale2010` | Official TAC abstract and metadata, cross-checked against an author publication list. Full-PDF retrieval failed; no numbered theorem from unread pages is asserted. |
| `ArtinMazur1969` | Publisher record and chapter list, including §§8–9. The full book was not accessed. The commentary supplies the needed hypercover proof itself. |

Full bibliographic details are in `DER_II-a_references.bib` and the reader’s bibliography. The supplied plainnat/natbib format has been retained for compatibility with the build kit.

## Source preparation, build, and visual verification

The source preparation script makes only the verified transcription changes and explicitly documented typesetting repairs. It rejects a replacement if its expected exact match count changes. The mathematical edition slips remain in the source.

The actual reading corrections include a duplicated standalone numeral, the calligraphic topos letter, three wrong TikZ arrow endpoints, missing underlines distinguishing functor categories from Hom sets, the relative-component underline, and the first primed label in Proposition 4.1. That last label is printed `a′`; the transcription’s claim that the edition printed `d′` was itself erroneous and has been removed. The later occurrence of “cofinal” in condition (d′) really is printed and remains.

Two source-code defects also required repair. The supplied document attempted to redefine TeX’s primitive `\def`; mathematical uses now employ its existing `\defeq` command. Bold simplex symbols use `\boldsymbol{\Delta}` instead of a text-font construction which produced a missing Greek glyph under LuaLaTeX. Neither repair changes the displayed mathematical meaning. A single wide naturality diagram is scaled to the text measure. The commentary style displays only the manuscript page number in its heading while retaining the complete exact anchor in the source, and switches locally to English hyphenation. The two opening page markers share one two-line margin box, and commentary headings are kept with the start of their text. The forced line break before the call to note 54 is replaced with a nonbreaking space to retain its connection with the preceding assertion. These repairs address collisions and orphaned elements found by visual inspection. The French text and its page markers remain distinct.

The supplied `build_reader.py` is unchanged. It validates and inserts the final blocks successfully. LuaLaTeX, BibTeX, and two subsequent LuaLaTeX passes complete successfully. The final log has no fatal errors, undefined citations or references, missing characters, or overfull boxes. The remaining notices concern automatic repositioning of margin page markers; these were checked visually for collisions and are recorded in `tools/validation.json`. The final reader was rendered and every page reviewed; dense formula pages and diagrams were additionally inspected at reading resolution. The overview occupies 3 pages, within the required two-to-five-page range.

The environment’s incomplete TeX installation needed a workspace-local LuaLaTeX/French support tree and font maps. These runtime dependencies are not bundled as large binary packages. A bootstrap recipe is included; a normal complete TeX Live installation can run the supplied build script directly. No network access is needed to rebuild once those TeX dependencies are present. The packaged reader PDF can be read without any build environment.

From the archive’s root directory, run:

```sh
python tools/assemble_parts.py
python tools/build_and_verify.py
python tools/check_finite_examples.py
```

The assembly script uses the final audited part data, preserves all stable claim identifiers, prepares the corrected source, and consolidates the bibliography. The build script performs the original builder and TeX sequence and writes its machine-readable verification record. The independent finite examples are supplemental checks of the written mathematics. `tools/finalize_report.py` substitutes final counts and verified page information into this report. The archive includes a SHA-256 manifest for its deliverable files.

## Format observations

The present format works without changing the supplied builder. For a future revision, the anchor parser should recognize manuscript labels such as `36bis`, `36ter`, and inline `\mspin{page 39}`. This delivery instead uses unique exact source phrases within the builder’s existing numeric-page ranges. The exact anchor is useful as machine data but too long for a printed heading; the small style adjustment keeps only the page label visible.

A future audit schema could separate “proof status in the excerpt” from “current mathematical status.” This would avoid making `open` do two jobs. Likewise, separate fields for “source opened” and “theorem passage checked” would make bibliographic verification more expressive. The current files obey the supplied schemas; the qualifications are recorded in their existing `notes` fields and here.

## Credit

AI-produced commentary: **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. The project’s supplied editorial credit is **“edited with Claude (Anthropic)”**. No additional Claude editing was performed during this session; that phrase is recorded as project-supplied credit, not as a claim about work performed here. No human is credited as author of the commentary.
