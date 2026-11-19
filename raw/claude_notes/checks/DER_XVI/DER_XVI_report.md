# Chapter XVI, manuscript pages 1–124: audit and commentary

Commentary and mathematical audit by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. This credit applies to the present commentary, registers, overview and report. The French text retains the original author's and electronic editors' credits. No later assembly or editing by another system is certified here.

## Scope and reading conventions

This package covers all 59 leaves of the attached `DER_XVI_pages.pdf`: two preliminary leaves followed by the edition's printed pages 1–57. The manuscript labels run from 1 to 124, with the additional primed labels 13′–18′. There are therefore 130 manuscript-page markers. These are three separate page systems. The corrections register uses **PDF leaves counted from 1**, the claims register and commentary anchors use **manuscript labels**, and the reproduced margin marks also retain the edition's printed pagination. `checks/page_concordance.csv` supplies the correspondence and the original transcription line at each manuscript marker.

All supplied leaves were read. The substantive leaves were rendered and inspected visually, in three contiguous groups, with additional checks of every doubtful or flagged formula and the complicated diagrams. The attached PDF, not a mathematically preferred reconstruction, governs the French reading. The original manuscript page 94 is explicitly marked *manque* in the edition. Its absence is recorded and preserved. The unreadable words at manuscript page 124 remain unreadable; no completion has been invented. These leaves are a packet from Chapter XVI, not a claim to have audited material beyond the supplied endpoint.

The earlier-companion index was read for continuity. Established material on path categories, perfect maps, Brown structures, covering obstructions and derivator conventions is referred to at the relevant earlier manuscript pages. New explanations concentrate on what the present arguments need: their exact hypotheses, the relation among the many fibration classes, and the consequences of later minimality theorems. When an earlier result is decisive for the audit, its source was opened rather than inferred from its title in the index.

The `proof_status` column describes the source's treatment. A conjecture which a later theorem disproves remains `conjectured`; the later answer is recorded in `repair`, `references` and `notes`. A false unrestricted assertion or inference is marked `false`. A sketched proof is not automatically called a gap: routine steps are supplied in the commentary, while genuine missing hypotheses are identified separately. Definitions and independent directions of compound results receive separate rows where that is needed to avoid mixing statuses.

## Principal mathematical findings

### Weak localization is not the relative axiom

Definition 1.1 uses the absolute asphericity axiom Loc (3). The later standard definition of a fundamental localizer uses the relative Loc (3 bis). The commentary maintains this distinction throughout, including the variance of the comma categories and the free split Grothendieck-fibration replacement. Strong saturation and retract closure are also kept separate from the source's initial saturation conditions.

The key later result is **Cisinski (2006, Theorem 6.1.18, pp. 242–243)**: ordinary weak homotopy equivalences form the least *weak* fundamental localizer. Definition 6.1.12 and Proposition 6.1.16 were checked to verify that this theorem applies to the weak axioms actually used here. The pagination is that of the published 418-leaf Astérisque PDF. The earlier 370-leaf author version has different pagination. Consequently the source's minimum `W_omega` equals `W_infty`; the predictions that this minimum is strictly finer, or fails filtered-colimit stability, do not survive that theorem.

This result does not prove that every weak fundamental localizer satisfies the relative axiom. Chiche's 2014 thesis, Remark 2.1.15, explicitly calls the distinction open, and Cisinski's dated answer of 22 December 2019 says that no distinguishing example was known to him. A targeted later search found no resolution. This report records those documented dates and the search limitation; it does not turn the absence of a search result into a theorem about all literature through 2026.

### Localization, products and connectedness

Lemma 2.6, on descending adjunctions, is valid by localizing the unit and counit. The product application needs more care. The literal arbitrary-class formulation of Lemma 2.5 omits identities, and a four-object Boolean-lattice example shows failure even for binary products. Adding identities repairs the finite statement. Infinite products introduce a separate issue: finite words in individual localizations need not have uniformly bounded lengths. This is not used to manufacture a defect in an explicitly finite assertion.

The cited proof of Proposition 2.7 was checked in Chapter XV, §9.12, manuscript page 133 quinquies (PDF leaf 75, printed page 73). Its editors explicitly warn that the finite-product preservation used there is established under Loc (3 bis), not under Loc (1,2,3) alone. The weak-axiom nontriviality criterion and the converse in the first Corollary 2.8 therefore inherit that dependency. The repaired argument is given with its stronger hypothesis. The fibration hypothesis D permits a separate direct proof of the needed connectedness, given below; its consequences do not remain dependent on this general gap.

### Forward and reverse excision

Loc (6a) and Loc (6b) are different conditions. Forward Mayer–Vietoris excision is compatible with ordinary weak homotopy equivalences; the reverse implication is not. Theorem 5.4's blanket inclusion of Loc (6) is therefore false if both halves are meant. Its countable-accessibility assertion survives and is treated separately. The list on manuscript page 87 has the same problem: the literal combination of reverse excision, connectedness and the strong fibration condition is inconsistent. The intended forward-excision version is the one identified with ordinary weak homotopy equivalences.

The commentary supplies a full form of the Brown argument needed by the cofibration calculations and applies its dual carefully to the fibration scheme. It develops the reverse-excision observation further by using categorical suspensions of connected components. Integral homology equivalences form the least weak fundamental localizer satisfying the reverse cube condition (6b). The proof establishes the homological localizer axioms by a double-complex argument and forces each componentwise homology equivalence into any such localizer by a suspension cube. Taking the disjoint union of the entire cubes avoids assuming summand closure of the unknown localizer. Results developed in the commentary are marked `\ours`, with complete proofs and an explicit statement of the literature checked; that marking makes no priority claim.

### The fibration scheme and its hypotheses

Intrinsic `Fib_W`, weakly `W`-fibred maps, locally constant Grothendieck fibrations and perfect maps have different definitions. The audit does not identify them with the fibrations of an arbitrary Quillen model structure. The arrows in the A–B–C–D–F scheme were checked with their stated classes and auxiliary localizer `W_0`.

The abstract assertion B(`F`) ⇒ C(`F`) needs identities in the test class. A one-object class of maps gives a counterexample to the unrestricted wording; every intended geometric class contains the identities, so those applications are unaffected. The infinite-path argument on manuscript page 57 was checked against Chapter VI, manuscript pages 193–195: its unit is universally a `W`-equivalence for the specified weakly `W`-fibred input, not automatically universally a `W_0`-equivalence. Using `W` for that unit and `W_0` for the perfect target repairs the argument needed there. Theorem 4.4.13(4a) prints the weaker F hypothesis for `W_0`, whereas the preceding proof uses Loc (7); the difference is recorded instead of silently replaced.

A finite group example gives a complete failure of composition for locally constant Grothendieck fibrations with respect to connected-component equivalences. A further result characterizes the intrinsic fibrations inside this class by trivial monodromy on the component sets. The proof includes the component-colimit formula and all base changes. An explicit componentwise factorization proves the existence of enough intrinsic fibrations for the connected-component localizer without incorrectly extending the stronger A–D properties to that example. The bold `\mathbf W_0` used for this particular localizer must be distinguished from the arbitrary auxiliary localizer `W_0` in the implication scheme.

Under **Loc (5)**, the source's loop argument and the fibration condition `D_{W_omega}` give `W ⊆ W_infty`; Cisinski's weak minimality gives the reverse inclusion. The other branch also admits a direct repair. If a disconnected category is `W`-aspherical, factor a chosen point through the canonical perfect replacement. Its total space is ordinarily weakly contractible, so it misses another component of the target. Universal pullback then makes the empty category aspherical, which forces every functor into `W`. If `W` is not total, all `W`-aspherical categories are therefore connected and nonempty; the perfect replacement of an arbitrary `W`-map then has connected nonempty fibres, giving Loc (5). This argument does not require the problematic general nontriviality criterion or strong saturation.

It follows that **`D_{W_omega}` allows precisely `W_infty` and the total localizer**. Every one of the eight conditions in the §4 rectangle implies this weakest D condition. In the ordinary case the auxiliary localizer is ordinary as well; in the total case all the tests hold automatically. Thus the eight conditions are equivalent without the sequential-colimit assumption. This later deduction settles the implication questions while keeping the defect in the source's earlier proof of 4.4.13(4a) visible. F remains strictly weaker. The finite truncation localizers `W_n` satisfy F: Cisinski (2006, §9.2.1 and Corollary 9.2.15) identifies them as proper accessible localizers, and Theorem 5.2.15 supplies right proper model structures whose fibrations are intrinsic `W_n`-fibrations.

### Accessibility, finite posets and derivators

The countable enlargement argument is made explicit, including the finite homotopy witnesses and the passage to a cofinal tail needed to choose a representative of a colimit basepoint. The apparent `pi_0` cardinal slip on manuscript page 82 is not an error: Theorem 5.4 expressly uses that symbol for the first infinite cardinal. The `[sic]` suggestion is resolved without changing the formula.

The subdivision example is proved at the level of natural-transformation homotopy. It is kept distinct from homotopy of geometric realizations and from simple homotopy. One drawing in the transcription had silently supplied an edge absent from the edition; that edge is removed from the transcription, while the edition's graphical deficiency is explained in the register.

Chapter I, manuscript page 67, footnote 3, was inspected to establish that the source's Der (1) concerns **finite sums**. Thus §7.6's assertion for relative categories is not rejected by an infinite-product counterexample. The source's contravariant convention also makes the colimit-at-an-initial-object argument in §7.7 correct. The circularity in Corollary 7.7.2, already acknowledged in the printed footnotes, remains a circularity under its exact weak hypotheses.

Cisinski's generalized Thomason theorem (2006, Theorem 5.2.15) supplies a later model-existence result for accessible **relative** fundamental localizers. Left properness is part of that theorem; right properness has an additional properness condition. Model-to-derivator results are cited with their actual hypotheses. They are not used to certify every weak-axiom variant or every prescribed intrinsic fibration class in these exploratory pages.

## Transcription and technical repairs

The input has two doubtful `% ??` lines and 49 comment lines containing `[sic]`; some contain more than one proposed slip. Every flagged place is resolved in the corrections register. The two doubtful arrow labels are decided from the PDF. Mathematical and grammatical slips already printed in the edition remain in the French source, with the intended reading recorded as `edition_slip_kept`. A source error is never corrected merely because its corrected form would make a theorem true.

The exact original transcription is retained as `inputs/DER_XVI_text_original.tex`. The buildable `DER_XVI_text.tex` is produced by `checks/prepare_source.py`, applying unique, asserted text replacements from the audited patch lists. The nonmathematical repairs complete two unterminated diagram macros, encode the summary implication diagram in compilable TikZ, and normalize the six primed page markers to the syntax accepted by the supplied builder. The editorial note about the shifted numbering is retained. English hyphenation for commentary, adequate margins, required TikZ libraries and microtypography are enabled in the preamble.

The supplied `build_reader.py` and `derivateurs_companion.sty` are retained unchanged. The overview is set apart from the original French text, and the commentary is visibly labelled and framed by the kit. Original margin marks continue to distinguish manuscript and edition pagination. One hard page break in the running text is suppressed for reflow because interleaving the commentary otherwise leaves an almost empty page; all words and pagination markers at that boundary remain unchanged. Exact-word anchors keep the two reverse-excision developments with the closing paragraph of §3, before the next section heading.

## Bibliographical checking and unresolved scope

The BibTeX file reuses cumulative keys wherever they exist. Every entry has a URL or DOI and an explicit verification note describing the item and version actually checked. A verification note does not certify every theorem in an entire monograph. The principal sources are Grothendieck's electronic chapters and letter, Brown's original paper, the published Cisinski monograph and papers, and the specific later papers identified beside their uses.

The registers and commentary identify the remaining scope questions individually. These include the weak-to-relative implication, unrestricted weak versions of the nontriviality argument, bare one-sided excision implications, objectwise replacement hypotheses without comparison squares in the B-transfer lemma, and the derivator-detection circle in §7.7.2. An unresolved implication is not called false without a counterexample, and an accessible relative theorem is not substituted for an arbitrary weak one. The infinite variant of the arbitrary-relative-category product lemma is not asserted merely from the finite proof. The stronger conclusions available under D are proved separately, rather than left under the general product-dependency warning.

## Build and validation

The final reader contains **84 pages**. The overview occupies reader pages **78–80**, satisfying the requested two-to-five-page limit; the bibliography begins on page 80. The final merge contains the following material.

| Item | Final count |
|---|---:|
| Audited source assertions | 337 |
| Anchored commentary blocks | 54 |
| Commentary words, whitespace count including mathematical markup | 21,111 |
| Overview words, same counting convention | 1,791 |
| Bibliography entries, each with a verification scope | 27 |
| Correction records | 96 |
| Transcription or encoding corrections | 10 |
| Edition slips retained in the French | 80 |
| Resolved doubts or confirmed readings | 6 |
| Original doubtful comment lines resolved | 2 |
| Original comment lines containing `[sic]` resolved | 49 |
| Distinct manuscript markers checked | 130 |

The commentary comprises 27 exposition blocks, nine worked-example blocks, seven later-development blocks, five blocks of commentators' mathematical development, four status blocks and two historical-context blocks. The five development blocks concern the missing-identity counterexample, homological Theorem A and reversible excision, the least reverse-excision localizer, component monodromy, and the degree spectrum of crown-poset maps. Each has an explicit result, a proof, the required `\ours` marking and a limited statement about the literature checked.

The supplied **`build_reader.py` and `derivateurs_companion.sty` are byte-for-byte unchanged**. The builder, first LuaLaTeX pass, BibTeX, and two further LuaLaTeX passes all completed with exit code zero. The final log contains no undefined citations or references, missing glyphs, TeX errors, or overfull boxes. Its remaining layout diagnostics are 19 repositioned margin notes and 2 underfull lines in a retained typewriter editorial paragraph. Visual inspection found no collision or loss of text at those places. All 44 fonts are embedded outline fonts; no Type 3 bitmap font is used.

All 84 final pages were rendered and inspected through contact sheets. Full-page checks additionally covered the major implication diagrams, the repaired span and square, the polygon drawings, base-change diagrams, the overview and the bibliography. There are no empty pages or text bounding boxes outside the page. The inspection record gives the exact final PDF hash and the pages examined. The original manuscript-page-94 notice, page-124 illegibility marker, and edition slips are preserved.

`checks/validation.json`, `checks/build_summary.json`, `checks/pdf_qa.json`, `checks/visual_review.json` and the complete command logs record these checks. `SHA256SUMS.txt` supplies an integrity manifest for the files in the archive. The archive includes the six requested files, the built reader TeX/PDF, its bibliography, the buildable and original transcriptions, the authoritative attached PDF, the original instructions and earlier-companion references, and the assembly and checking code. No draft reference, checkpoint notice, downloaded research corpus or local TeX distribution is included.
