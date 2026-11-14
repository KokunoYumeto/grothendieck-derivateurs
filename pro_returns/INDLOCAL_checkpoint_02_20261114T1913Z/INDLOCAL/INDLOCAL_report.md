INCOMPLETE

# INDLOCAL research record

Work started 14 November 2026 at 18:21 UTC. This is a live research record. Each proved statement has an explicit argument and typed comparison maps in the paper. The complete task has not yet been settled.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The attached AI-produced returns are treated as proofs to check. No statement is accepted on the authority of a return or its review.

## Requested task register

| Task | Current state | Proof or active obstruction |
|---|---|---|
| A1 | Proved | A.1--A.3: simultaneous cone construction, injectivity, local coefficients, quotient and perfect kernel |
| A2 | Proved with the cardinal estimate supplied | A.4: each lifting, amalgam, homology and limit step; explicit size control |
| A3(i) | Proved | A.8--A.9: functorial construction, replacement for general simplicial maps and proved limits |
| A3(ii) | Proved | A.6--A.7: the kernel can be simple; its homology is forced by the universal cover |
| A3(iii) | UNDECIDED in unrestricted cardinality | A.10--A.11 prove dimension preservation for finite target bounds and the exact countable-source threshold. A general large, acyclic group of geometric dimension two without small quotients remains under investigation. A.13 proves there is no dimension-only bound even for nonaspherical targets: a wedge of lambda 2-spheres has a dimension-two resolution with every target bound mu < lambda. |
| A4 | Proved | A.2: full derived mapping-space comparison onto the components killing the kernel, including disconnected targets |
| B1 | Proved | B.1 checks both written R3 proofs and their specified unit |
| B2 | Proved | B.2: arbitrary small colimits of groupoid representables |
| B3 | Proved | B.3--B.4 and B.6: truncation, integral homology, and exact algebraic orthogonality for every larger localizer |
| B4 | Proved | B.7--B.8: sharp uniform threshold mu^+ < kappa; full classification of bounded invariant restrictions |
| B5 | Proved | B.5: enlarged-universe invariant ind-objects equal Ind_V(Hot_U) |
| C1 | Proved | C.20--C.22: both D.K5 proofs and exact universal sequence criterion |
| C2 | Proved | C.13--C.17: exact stage criterion, comparison square, suspension and crown examples; finite computations passed |
| C3 | Proved | C.22--C.28: sentence-level replacements, shape audit, R5 proof and complete chain-complex example |
| C4.1 | Proved | C.1--C.4: clamping, strict action, coherent descent, both finality comparisons and composition identity |
| C4.2 | Proved, correcting the premise | One-sign padding and composition remain valid; comparison to the full localization has the exact restrictions stated in C_paths.tex |
| C4.3 | Proved | R7 local-representable proof, both signs, canonical maps, hammock comparison and isomorphism closure |
| C4.4 | Proved | Naturality in both endpoints, concatenation, the specified Q, literature comparison and finite (+,-,+) checks |
| D, strict retraction | UNDECIDED | D.1--D.13: proved for finite relative cell constructions and retracts, with explicit padding bounds. Collage reduction isolates the general forward-endpoint question; unrestricted construction is active. |
| D, lengthened-fence HEP | UNDECIDED | D.3--D.13: proved for the specified smallest example, arbitrary bounded-dimensional cell families in one stage, finite composites and retracts. Remaining obstruction is a uniformly finite fence for an unrestricted construction. |
| E, strict 2-categories | Proved, correcting the proposed answer | E.1--E.6: explicit finite B^2 C2 counterexample; ordinary groupoids give the exact invariant class |
| E, all strict n-categories | Proved | E.2--E.6, for the explicitly fixed normal Gray lax/pseudo convention. Independent audit completed, including the typed Gray cylinder and transformation group. |

## Main findings recorded so far

1. The first R3 proof extends to arbitrary small colimits because the Kan--Thurston comparison is bijective before taking a colimit. Filteredness enters only the second proof's preservation of injections.
2. Among presentations with stages of at most mu arrows, invariance on tests with fewer than kappa arrows forces a global ind-groupoid precisely when mu^+ < kappa. The element-category construction proves sharpness, including kappa = mu^+.
3. One-sign blocks compute ordinary arrows (positive) or reversed marked arrows (negative). Their padding maps are isomorphisms in Cat_hot. The crown calculation concerns the comparison with the full localization.
4. Strict higher-category morphisms have a much more restrictive representability result than the proposed n-groupoid answer: the exact class is ordinary groupoids. The finite strict two-groupoid B^2 C2 already gives a complete counterexample to the proposed two-type criterion.
5. A three-object relative category gives a mapping space BC2 and a globally invariant constant-endpoint presheaf. Thus the fundamental groups of invariant mapping spaces can be nontrivial.
6. The map from transformation homotopy classes into ordinary homotopy classes can fail to be injective even for a Thomason-fibrant target. The proved example is recorded in D.tex. It is not by itself a counterexample to the strict retraction problem.

## Computations

- code/e_strict_two_groupoid.py: all 8 associativity and 16 interchange checks passed; unique strict functor from BC2; two normalized 2-cocycles and one coboundary.
- code/cpaths_checks.py: finite vertex/letter correspondences, compositions, clamping categories, R8 certificate arrows, crown markings and (+,-,+) padding squares checked; detailed counts in its output.
- code/a_finite_checks.py and code/d_finite_checks.py: current finite checks and outputs included.

## Open work and approaches tried

### Unrestricted dimension preservation

The finite-target construction uses a two-dimensional acyclic Higman complex in the dimension-preserving Baumslag--Dyer--Heller realization. A simple-envelope construction gives arbitrary cardinal bounds and can make the kernel simple, but the completed acyclic restoration argument has not yet established the required two-dimensional bound. A strongly connected high-chromatic graph of Higman power relations forces small homomorphisms to vanish; its repeated incoming relations leave degree-two homology, so this attempt does not give the required acyclic group. The next active target is an unrestricted-cardinality acyclic aspherical two-dimensional construction. A.13 gives simple groups of arbitrary cardinal lambda with a two-dimensional classifying space and H2 free of rank lambda, resolving the wedge of lambda 2-spheres. This disproves a bound based only on dimension, but does not settle a fixed S2 at mu = aleph_0.

### Strict retraction and fence extension

The model-category path-object proof constructs a strict retraction with the same ordinary homotopy class. It does not identify the finite-natural-transformation class. The proposed product-corner pseudo-Dwyer argument fails at its adjunction, and that failure is not a proof of non-extension. A fibrant-target noninjectivity example shows why ordinary homotopy-class equality does not finish the argument. A collage reduction now converts a suitable endpoint-extension failure into the requested strict-retraction counterexample; this is one active route. D.9 gives the exact eight-step subdivided-triangle table. D.11 extends it to a 4(n+1)-step comparison relative to the boundary of an n-cell, using a corrected relative cylinder. D.12 gives full prescribed extension for a bounded-dimensional family of cells in one stage and for finite composites and retracts. The bound depends on dimensions and the number of stages. Independent checking found a missing common facet in the first cylinder draft; the gluing subcomplex is now the full inverse image of the boundary, and the proof was rechecked with that correction.

## Checkpoint and typesetting record

Checkpoint 01 records the completed Part B and Part E proofs together with every deliverable and authored work record written so far. A PDF was not included in checkpoint 01: that initial LuaLaTeX build was still being repaired. Checkpoint 02 records completion of Part C and the subsequent proved retraction cases, including a checked PDF. The local Type1-font bootstrap is documented and reproducible in code/build_pdf.py. Checkpoint 02 has 59 pages. The final LuaLaTeX log has 0 overfull horizontal boxes and 0 overfull vertical boxes (before visual review: 0 and 0; after review: 0 and 0), no undefined references or citations, and no LaTeX warnings. Pages 1, 3, 7, 12, 18, 24, 30, 36, 42, 48, 54 and 59 were rendered and visually inspected. No clipping, overlapping text, missing glyphs or protruding displays were observed. The PDF hash and the exact visual-review record are in logs/PDF_QA_PASSED.json in that checkpoint.

Attached source files, extracts of those files, and downloaded third-party source reproductions are excluded. They are reference inputs, not authored deliverables. Authored research notes, all current sections, computations, outputs, build logs and the results table are retained. No mathematical passage from an earlier checkpoint has been omitted. The corrected current source supersedes earlier working wording; earlier build-pass logs are superseded by the clean three-pass LuaLaTeX logs. The checkpoint archives retain their original contents.

The first three-hour progress reassessment is due around 21:21 UTC. Work is currently advancing the main unresolved items.

## Independent audit and source-access record

Part E and the sharp cardinal and bounded-restriction results B.7--B.8 received independent proof audits. The audit confirmed the transformation group law, localization comparisons, equality case of the cardinal threshold, and the relative homotopy-coequalizer map. C.17 gives the specified finite-image/all-functions comparison, so the all-test Hom comparison is not silently assumed.

The original Kan--Thurston 1976 and Maunder 1981 papers remain marked unverified: public publisher and historical PDF links failed or exposed only metadata. No theorem in this manuscript depends on their unexamined text. The primary Baumslag--Dyer--Heller, Hausmann--Husemoller and Leary proofs used in Part A were opened and checked.
