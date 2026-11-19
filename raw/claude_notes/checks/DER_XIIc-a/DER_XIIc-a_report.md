# DER_XIIc-a: consolidated textual and mathematical audit

**Commentary, mathematical audit, and report by GPT-6 Astra (OpenAI, ChatGPT Pro mode).** This credit applies to the present work and does not certify subsequent editing or assembly by another model. Audit date: 10 November 2026.

## 1. Scope, authority, and coverage

This package treats Alexander Grothendieck’s *Les Dérivateurs*, Chapter XII, section VI, manuscript pages **171–234**. The authoritative source is the attached 35-leaf PDF, corresponding to edition pages **115–149**, from the electronic edition transcribed by M. Künzer, J. Malgoire, and G. Maltsiniotis, version 30 March 2003. The accompanying LaTeX transcription was checked against that PDF throughout. Every source leaf was rendered and visually inspected; text extraction supplemented the visual examination of formulas, diagrams, footnotes, and doubtful readings. The attachment covers the entire assigned extract, so no missing source leaves required supplementation.

Three numbering systems remain distinct: attached PDF leaves, edition pages, and manuscript pages. The reader’s own pagination is independent. Manuscript anchors determine commentary placement; edition and manuscript labels identify the historical text without requiring the reader to reconstruct its original page breaks.

The integrated files contain **36 commentary blocks, 191 claim-register entries, 46 correction-register entries, and 23 bibliographic references**. The blocks comprise 18 expositions, seven developments, three worked-example discussions, three contextual discussions, four accounts of later work, and one status discussion. Eight individual results carry the `\ours` marker. The claim register covers all 64 manuscript page labels and includes definitions, axioms, propositions, intermediate arguments, conjectures, and questions. Its identifiers are unique.

The supplied earlier-companion index ends with **Chapter VII-a**. It establishes continuity with earlier discussions, especially Chapter VI, but supplies no evidence that this part of Chapter XII has already been covered. Repeated manuscript page numbers in different chapters are not treated as overlapping material. References to earlier commentary are distinguished from passages of Grothendieck independently consulted for this audit.

## 2. Textual decisions and the meaning of the registers

The correction register contains **one transcription correction, 41 retained edition slips, and four resolved doubts**. All **24 existing `[sic]` flags and both existing `% ??` flags** are accounted for. Only the verified transcription discrepancy changes a mathematical source reading: in footnote 114, attached PDF leaf 3, the assignment is printed as `$(X,x) \mapsto \Omega(X,x)$`, not with `\longrightarrow`. Edition slips remain in the French text and receive explanations separately.

The four doubt records preserve the editors’ `[mot illisible]` on manuscript p. 206; identify the exponent in the p. 223 underbrace as a literal digit zero; resolve the line-end division of *cocartésiens*; and confirm both biconditionals in the continuation of footnote 124. The illegible manuscript word cannot be recovered from the supplied edition. Mathematical interpretation of the intended notation does not justify substituting an unsupported reading. Preliminary suspicions about two other small letterforms were rejected after enlarged inspection and were not entered as corrections.

The claim register separates the source’s presentation from the present assessment. Its `proof_status` field follows the supplied format: `open` records a question left open in the source, while `repair`, `references`, and `notes` describe what is proved here, settled later, or still unestablished under the exact hypotheses. Thus the 17 entries labelled `open` are **not** a list of 17 contemporary open problems. Similarly, nine entries labelled `false` include failed inferences and a mistaken label, not nine independent failed theories:

| Manuscript locus | Assertion or inference as written | Assessment and repair |
|---|---|---|
| p. 172, Theorem 1 | Finite-stage cohomology and homotopy comparisons are equivalent | The converse fails in degree three. |
| p. 172, footnote 112 | The converse may already fail in degree two without simple connectivity | The degree-two converse holds with all permitted local coefficients. |
| pp. 176–177 | The inductive lemma supplies the same converse | The degree-three counterexample also satisfies its lower hypotheses. |
| p. 179 | Every implication in the corrected chain is strict | The middle implication is an equivalence for degree two. |
| p. 187 | The fibre-connectivity class defines the localizer of finite homotopy types | It fails two-out-of-three; use homotopy isomorphisms through the specified degree, or take saturation. |
| p. 201 | Common refinements establish filteredness | They do not establish equalization of parallel arrows; contractibility provides the needed conclusion. |
| p. 204 | The one-object category of an arbitrary group is monoidal | The group must be abelian; the infinite cyclic group supplies the intended example. |
| p. 205 | The functor labelled `(*)` is an equivalence | The intended equivalence is labelled `(**)`. |
| p. 208, footnote 120 | Intrinsic fibrations are retract closed under the stated minimal assumptions | A finite-set counterexample disproves this; retract closure of the weak equivalences repairs it. |

## 3. Homotopy, cohomology, and the loop criterion

The initial descriptions of $W_0$ and $W_1$ are justified explicitly. Constant coefficients detect components; locally constant systems encode transport through the fundamental groupoid. The apparently weak degree-one test is sufficient because sections of every group action detect surjectivity of the fundamental-group map, while surjectivity on constant nonabelian $H^1$ detects injectivity. The coefficient groups must be allowed to vary. Abelian degree-one cohomology alone would not exclude a nontrivial perfect group.

The first failure of the withdrawn Theorem 1 is exhibited by

$$S^2=\mathbf{CP}^1\longrightarrow\mathbf{CP}^{\infty}=K(\mathbf Z,2).$$

For every abelian coefficient group, this map is a cohomology isomorphism through degree three, whereas its map on $\pi_3$ is $\mathbf Z\to0$. Both spaces are simply connected, so the permitted local systems introduce no additional obstruction. This also disproves the proposed inductive lemma (Hatcher, 2002, Examples 4.50–4.51).

The degree-two assertion requires the opposite conclusion. After identifying the fundamental groups with $\pi$, the local coefficient module $\operatorname{Hom}_{\mathbf Z}(\mathbf Z[\pi],\mathbf Q/\mathbf Z)$ detects the second homology of the universal cover by exact faithful duality. The natural Hurewicz isomorphism then detects $\pi_2$. Consequently $b_2$ and $c_2$ are equivalent without a simple-connectivity hypothesis. The proof supplies the left-module action explicitly, so the noncommutativity of the group ring causes no ambiguity (Hatcher, 2002, §3H and Theorem 4.32; The Stacks Project Authors, 2026, Tags 01D8 and 08WE).

The corrected chain

$$a_n\Longrightarrow b_n\Longrightarrow c_n\Longrightarrow a_{n-1}$$

is valid. The commentary completes the twisted-coefficient evaluation map using equivariant cocycles and Hurewicz images, proving additivity, naturality, and equivariance and identifying the relevant spectral-sequence edge map. The converse tests the first possible nonzero homotopy module of the fibre against itself. At degree two, the homotopy exact sequence first proves that the fibre’s fundamental group is abelian. The required degree-one Hurewicz identification is therefore legitimate.

The abandoned universal-cover comparison is also completed. Smart truncation gives a finite-range comparison for derived invariants without an assumption in the next degree. Covering-chain groups are free over $\mathbf Z[\pi]$, so their cochain terms are products of coinduced modules and are acyclic for invariants. Derived invariants therefore compute the required local-coefficient cohomology. Monodromy is retained throughout; the untwisted statement in Hatcher’s spectral-sequence notes is used only for indexing and filtration, alongside Serre’s construction of the fibre-cohomology local system (Serre, 1951, Chapter II, §8, Proposition 6; Hatcher, 2004, Theorem 1.14).

The p. 187 localizer claim fails because maps with $n$-connected fibres do not satisfy two-out-of-three. The composite $*\to K(A,n+1)\to *$, with $A\ne0$, gives the counterexample. The correct weak-equivalence class is $b_n$, detected by Postnikov truncation. Its relation to the author’s intuition is precise: saturation of $a_n$ gives $b_n$, since Postnikov maps have $n$-connected fibres (Lurie, 2009, Proposition 5.5.6.18).

Theorem 2 and its loop-asphericity corollary survive. The reverse induction at its degree-two endpoint uses the abelianness of $\pi_1\Omega X$, supplied by the Eckmann–Hilton argument. Pointed transport is constructed through arrow categories, and multiplication in a group-like loop space justifies transport from the unit component to every component. These proofs concern classifying spaces or CW/singular homotopy types; they do not assert an unconditional comparison with ordinary sheaf cohomology on arbitrary pathological spaces.

## 4. Canonical replacements and intrinsic fibrations

A weak coaugmentation $1\to C$ makes the replacement functor preserve and reflect weak equivalences by two-out-of-three. Two replacements have the normalized comparison $[i'_X][i_X]^{-1}$ after localization. The common-refinement construction gives exactly that comparison, and the specified units force its cocycle identity. Ordered insertion of units proves all six ternary compatibility identities by the interchange law.

The category of coaugmented replacements is contractible whenever it is nonempty: fixing $R$ supplies natural transformations $1\to(-)R\leftarrow\operatorname{const}_R$. This is an application of the nerve homotopy induced by a natural transformation (Quillen, 1973, §1, Proposition 2). Finite nonempty ordered sets with injections and concatenation demonstrate why such common targets need not imply filteredness. The audit does not infer that the actual replacement category is nonfiltered. The localization equivalence is proved separately, with the agreement of total and fibrewise weak equivalences on permitted representatives stated as an additional necessary input.

A complete cochain-complex example factors a map into a homotopy equivalence followed by a degreewise surjection, verifies the differential and contracting homotopy, and identifies its strict fibre with the shifted mapping cone. Multiplication by $m$ on $\mathbf Z[0]$ has zero ordinary kernel but a homotopy fibre with $H^1=\mathbf Z/m\mathbf Z$. This illustrates the information retained by replacement (Brown, 1973, Part I, §1, Example 3).

The intrinsic $W$-fibrations are sharp maps in the model-category terminology. Composition and pullback stability are formal. Retract stability requires more: on finite sets, maps preserving cardinal parity satisfy the literal assumptions, but a map with fibre sizes $(1,3)$ is an intrinsic fibration and its retract with fibre sizes $(1,2)$ is not. Rezk’s right-properness hypotheses are retained when relating sharp maps to ordinary fibrations and homotopy-cartesian pullbacks (Rezk, 1998, §2, Propositions 2.2 and 2.7).

Axiom a transports arbitrary base change through the equivalence of localized slices and identifies the strong saturations of the two weak-equivalence classes. If $W$ is strongly saturated, it implies axiom b. An explicit functorial coaugmented replacement proves the intermediate-full-subcategory assertion c. **The bare implication from a and b to c is not established here**, and is not announced as a contemporary open problem. The subsequent manuscript argument at pp. 240–241 adds factorization and a qualification about fibrancy over a terminal object. Brown’s and Cisinski’s results supply sufficient structures, not a proof that those structures follow from a and b alone (Cisinski, 2010, Definition 1.1, Proposition 1.8, Theorem 2.21).

## 5. Relative tests, smoothness, and gluing

The comma-category tests retain their variance: $X/s\to Y/s$ defines the local class, while under-categories define its counterpart. Opposite categories exchange these constructions while also reversing the base. The degree-two circle endomorphism over the free monoid illustrates their directional content: its total homotopy type has fundamental group $\langle a,t\mid tat^{-1}=a^2\rangle$, while its derived fibre over the circle is $K(\mathbf Z[1/2],1)$ rather than the original $K(\mathbf Z,1)$.

The universal enlargement of admissible base changes is proved maximal and idempotent, with pullback stability and unchanged relative equivalences. The statement assumes invariance under isomorphisms of arrows, making pullback choices immaterial. For Grothendieck’s local class in categories, the enlargement equals the class of $W$-smooth functors: testing arrows to terminal slice objects converts universal preservation into Maltsiniotis’s aspherical-functor criterion (Maltsiniotis, 2005, Theorem 1.2(c)). Postcomposition descends for every base map; when raw pullback is homotopical, the ordinary slice adjunction descends too. No automatic adjunction for an indirectly constructed inverse image is asserted. Smooth/proper complementarity depends on the coefficient theory and its base-change transformations (Anel & Weinberger, 2024, Definition 9 and Proposition 10).

The long categorical interval gives the required two-endpoint Dwyer inclusion for $n\ge2$; the shorter interval fails for an explicit adjoint obstruction. The mapping cylinder, its functoriality, its Dwyer first factor, and its weak-equivalence retraction are verified. An eight-vertex example computes the cofiber of $S^0\to *$ as a circle. Proposition 16 follows by factorization and forward gluing. The deferred pasting argument is completed for every fundamental localizer using objectwise invariance of integration, explicit homotopy-final comparisons, and Cisinski’s minimal-localizer theorem.

Footnote 124 requires a separate qualification. Its biconditionals assume conservative axioms W(7 bis) and W(7); these converse implications are not properties of ordinary weak homotopy equivalences. A finite acyclic noncontractible complex, its two cones, and its suspension produce a counterexample by face posets, even with Dwyer inclusions and an open-sieve cover. The conditional footnote is not falsely classified merely because its extra axioms fail in that example. Forward preservation still proves the mapping-cylinder and gluing results. Original Dwyer maps are also distinguished from Thomason cofibrations in light of Cisinski’s retract correction (Thomason, 1980, §4; Cisinski, 1999). Later infinity-categorical preservation strengthens forward gluing, not the rejected converse (Hackney et al., 2024, Theorems 1.5–1.6 in arXiv v3).

## 6. Literature limits and attribution

Each of the 23 bibliography entries contains a URL or DOI and an extent-specific verification note. Published and preprint numbering are distinguished: Groth’s pasting proposition is cited as published Proposition 3.13, whereas Hackney and collaborators are cited explicitly by arXiv v3 numbering. Groth’s published proposition leaves its proof to the reader; the present commentary supplies one.

**Thomason’s original 1979 proof of Theorem 1.2 was not inspected.** Publication metadata and the precise theorem statement and attribution were checked, the latter against Rubin’s *Elmendorf constructions for G-categories and G-posets* (2020, §2.3, Theorem 2.6, manuscript dated 30 December 2020). That supporting work has its own bibliography entry. The bibliography records this limitation rather than claiming direct verification of the original proof.

The searches were targeted to the manuscript’s questions and their mathematical dependencies, not exhaustive priority surveys. The eight marked results are supplied proofs or applications: pointed transport, finite-range descent, the degree-two converse, saturation of the fibre class, the parity retract counterexample, universal saturation of test classes, descent of postcomposition, and the acyclic face-poset construction. Their `[ours]` labels identify work provided for this commentary and make no claim of historical novelty.

## 7. Reproducibility and verification

The expected package root contains the six prescribed files—`DER_XIIc-a_blocks.tex`, `_overview.tex`, `_claims.csv`, `_corrections.csv`, `_references.bib`, and `_report.md`—together with the prepared `_text.tex`, generated `_reader.tex`, compiled `_reader.pdf`, `build_reader.py`, `derivateurs_companion.sty`, and `FORMAT.md`. Original inputs are retained under `inputs/`, including `DER_XIIc-a_text_original.tex` and the authoritative PDF; executable preparation, assembly, rebuilding, and validation scripts are under `code/`. Part registers and their generators retain the provenance needed to repeat structural validation. Verification summaries and logs belong under `verification/` in the delivered layout; the working layout uses `work/qa/`.

On a complete TeX Live installation, run:

```bash
python code/rebuild.py
python code/validate_package.py
```

The rebuild prepares the transcription, invokes `build_reader.py DER_XIIc-a`, then runs LuaLaTeX, BibTeX, and two further LuaLaTeX passes. `code/source_repairs.json` records the sole transcription replacement separately from typography. The optional `--local-tex` switch supplies the scoped TeX-data workaround used where LuaTeX support and French language data are missing; it changes no system installation. It requires the indicated Debian downloads and is unnecessary with a complete installation.

The supplied assembly script and commentary style are unchanged. Reader typography is configured separately in `code/prepare_reader_source.py`: A4 margins, English and French hyphenation, explicit font maps, distinct manuscript and edition margin labels, a cover, and readable table and bibliography alignment. `code/layout_repairs.json` records the source-body layout changes separately: removal of one forced page break that orphaned two displays, spacing and routing changes in three source diagrams, and restoration of the source’s two emphasis marks to the left margin. No node, map, mathematical label, or historical reading is emended by these layout changes. Footnote hyperlinks are disabled because the faithfully retained unnumbered continuation of footnote 124 otherwise creates a duplicate hyperlink destination; the footnote text and numbering remain intact. The original audit flags remain available as locators, with their resolutions in the correction register.

The recorded build completed all six commands successfully. Its final log contains **zero LaTeX errors, undefined references or citations, missing characters, overfull boxes, and underfull boxes**. Structural validation confirms source fidelity against the documented transformations, coverage of every manuscript page and original annotation, unique claim and bibliography identifiers, and the counts reported above. These checks establish reproducibility and internal consistency; they do not replace the mathematical arguments or visual inspection.

The final reader has **55 physical PDF pages**. Its overview occupies **three pages**, beginning on physical page 50; the bibliography begins on page 52, after the overview concludes on that shared page. Every source leaf and every reader page received visual inspection. The final review checked all-page contact sheets, individual full-size pages for the complete first assembled reader, and the changed diagrams and surrounding page boundaries again after repair. The coordinating review additionally checked the cover, the entire reflowed reader, and the overview and bibliography. No unresolved clipping, overlapping labels, missing glyphs, or ambiguous source/commentary boundaries remain.

Two benign LaTeX margin-placement warnings remain for the first two numbered pages: the page-label margin notes were moved by LaTeX and are visually clear. There are no unresolved typesetting or bibliographic build diagnostics. The completed rendering inventory reports no text at the physical clipping boundary. The auxiliary logs, annotation-to-register mapping, finite-example checks, and checksums are included as verification records. Verification completed on **10 November 2026**.

