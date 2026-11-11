# Part C research and verification report

## Scope and principal corrections

We computed all five classes for the derivators of sets, groupoids, truncated spaces, spaces, unbounded derived modules over every associative unital ring, spectra, and E-local spectra. Statements C.1–C.15 in `sections/C.tex` contain the proofs and exact hypotheses. All results using coherent local systems are explicitly restricted to infinity-category enhancements. We do not infer them for arbitrary prederivators or derivators merely by passing to homotopy categories.

The key enhancement observation C.1 is that a restriction functor commutes with cotensors by arbitrary small spaces. Full faithfulness of its homotopy-category functor therefore tests all mapping spaces, not only their component sets. C.2 uses point-inclusion Kan extensions to prove equality of the cohomological, homological, and 1-complete classes for these coefficients. The resulting class has coefficient-acyclic homotopy fibers. It is not a fundamental localizer: C.5 and C.12 give explicit failures of two-out-of-three.

The CATHOT afterword in the supplied prompt incorrectly asserts that an integrally acyclic group A gives BA→* outside the 1-complete class. For every prederivator whatsoever, the constant and 1-complete definitions coincide for a map with point target. Thus BA→* belongs to the 1-complete class and lies outside the 2-complete class when coefficients detect pi1. The reverse point map *→BA is the constant equivalence outside the 1-complete class. C.8 states this correction independently of enhancement. The supplied CATHOT B.6 mitosis argument was read and checked; its construction and homology induction are valid. Root Part B incorporates it as B.10.

For D(k), C.7 proves the exact three levels: ordinary k-homology, k-acyclic homotopy fibers, and pi0/pi1 plus universal-cover k-homology. It treats noncommutative rings by integral chain models followed by scalar extension, rather than silently supposing that Mod_k has a symmetric tensor product. The zero ring yields the terminal coefficient theory and all maps. C.9 further proves that Wlc_D(k) equals ordinary weak equivalences precisely when no rational prime is invertible in the nonzero ring k.

For E-local spectra, C.11 gives the exact generalized-homology description using based loops at the 2-complete level. We do not silently replace loop E-homology by E-homology of universal covers for arbitrary nonconnective E. The explicit Morava K(n) result is strict containment of ordinary weak equivalences, using a degree-ell sphere map with ell different from the defining prime. This answers the requested “as far as you can” case without making an unverified chromatic simplification.

The rational class is already known as pi1-rational or fiberwise-rational homotopy equivalence; it must not be claimed new. The directly relevant primary result is Rivera–Wierstra–Zeinalian (2021), Theorem 3, a source absent from the supplied bibliography. The GHT finite-type algebraic model and Toën schematization were compared with their actual statements, rather than their abstracts alone. The implication to schematization is strict by the uncountable acyclic simple-group example in C.14.

The attached Toën source has an implication reversed in the prose immediately following Definition 3.1.1: it says an O-equivalence is a P-equivalence. Lemma 3.3.2, the proof following it, and the example BC2→* over Q show the correct implication is P-equivalence ⇒ O-equivalence. No Grothendieck transcription correction is needed in Part C.

## Sources actually read

- Grothendieck `DER_I-b_text.tex`, ms.99–101, 106, 113 and surrounding definitions. The point-target issue is visible directly in the ms.99 definition.
- Supplied CATHOT `sections/BC.tex`, especially B.6, B.7 and their proof text. The checked C.1–C.4 reflector result is cited as the prompt instructs, not reproduced.
- Supplied Lurie `HA.pdf`, extracted to text; Theorem 4.7.3.5 and its hypotheses checked. The application to evaluation includes proof of conservativity, colimit preservation, the monad, and functoriality.
- Supplied Schwede–Shipley source, Theorem 5.1.6, also cross-checked against the publisher's full text at https://doi.org/10.1016/S0040-9383(02)00006-X.
- Supplied Hatcher PDF, Corollary 4.33 and its relative-Hurewicz proof.
- Supplied Toën final April 2006 source, Definition 3.1.1, Lemma 3.3.2, Theorem 3.3.4, Corollaries 3.3.7–3.3.9, and the examples in Section 3.4. A parser independently checked the theorem numbering.
- Rivera–Zeinalian (2018), publisher PDF https://msp.org/agt/2018/18-7/agt-v18-n7-p02-p.pdf, Corollary 9.2, Remark 9.3, and the introduction's precise warning about quasi-isomorphisms and cobar equivalences.
- Rivera–Wierstra–Zeinalian (2021), published PDF opened through https://pure.mpg.de/pubman/item/item_3337679_6/component/file_3403111/Rivera-Wierstra-Zeinalian_Rational%2Bhomotopy%2Bequivalences%2Band%2Bsingular%2Bchains_2021.pdf, especially Theorem 3. A later repeat fetch returned 403; the first successful fetch supplied the theorem and publication metadata. DOI: https://doi.org/10.2140/agt.2021.21.1535.
- Gómez-Tato–Halperin–Tanré (2000), author-uploaded complete article at https://www.researchgate.net/publication/253067640_Rational_homotopy_theory_for_non-simply_connected_spaces. Checked Definition 6.1, Theorems 5.10, 5.11, 6.2 and 6.4, their hypotheses, and adjacent proofs. The AMS PDF returned 403. The author upload identifies the correct DOI 10.1090/S0002-9947-99-02463-0 on its front matter. This is a primary author-supplied copy, not a secondary summary.
- Pascaleff–Pavia–Sibilla, author PDF https://jpascale.web.illinois.edu/papers/Local_systems.pdf, introduction, Theorem A, and categorical theorem listings; forwarded to the higher-reconstruction subtask because its actual content is relevant to Part E. No theorem from its unexamined later sections is used in Part C.

Every Part C bibliography entry is marked verified with the exact access basis. No inaccessible source is used as proof. No priority claim is made.

## Literature searches

Searches included the exact titles of GHT, “local systems chain complexes modules chains based loop space infinity category theorem”, “Adams cobar construction 1956 simply connected theorem”, “cobar quasi-isomorphism simply connected Rivera Zeinalian”, the exact Schwede–Shipley title with “5.1.6”, “Toën Champs affines Selecta 2006 DOI”, and “Bousfield localization spectra homology”. These searches uncovered RWZ (2021) and Pascaleff–Pavia–Sibilla. The arithmetic detection assertion C.9 is supplied with a proof from derived tensor products and field detection; we make no novelty claim for it.

## Computations and supplied code

`code/verify_coefficient_examples.py` verifies the finite permutation quotient of the acyclic presentation complex K, the unimodular cellular boundary, the C2 category axioms, and the failure of fullness of the underlying-set functor on the regular two-point action. It reports a quotient of order 60 and a determinant of 1. Its output is `code/verify_coefficient_examples.out`. The finite computation does not substitute for the proof of all-degree acyclicity: that proof is the two-dimensional cellular chain computation with no higher cells.

`code/verify_toen_numbering.py` parses section/subsection and theorem counters from the supplied source. Its output records Definition 3.3.1, Lemma 3.3.2, Corollary 3.3.3, Theorem 3.3.4, Lemma 3.3.5, and Corollaries 3.3.6–3.3.9. Output is supplied.

`code/make_C_register.py` constructs the 15 result records and its output is supplied. PDF-to-text reads of HA, HTT, and Hatcher were used for searching, with `pdftotext -layout`; these source-derived scratch text files are not independent deliverables and need not be included in the final archive.

## Exact limits

Part C has no unresolved requested example among the asserted coefficient classes. C.11 deliberately stops at an exact E-homology condition on based loop spaces for general E, which is a complete test but not a closed-form ordinary-homotopy-group classification. No statement claims that an arbitrary derivator admits the coherent enhancement used in C.1–C.3. Reconstruction from a bare ordinary category and ordinary fiber functors, which is a separate problem from C.1's detection of a specified restriction, is handled in Part F rather than inferred here.
