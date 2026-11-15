INCOMPLETE

# INDLOCAL research record

Work started 14 November 2026 at 18:21 UTC. This is a live research record. Each proved statement has an explicit argument and typed comparison maps in the paper. The complete task has not yet been settled.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The attached AI-produced returns are treated as proofs to check. No statement is accepted on the authority of a return or its review.

## Requested task register

| Task | Current state | Proof or active obstruction |
|---|---|---|
| A1 | Proved | A.1--A.4: simultaneous cone construction, injectivity, local coefficients, quotient and perfect kernel |
| A2 | Proved with the cardinal estimate supplied | A.5: each lifting, amalgam, homology and limit step; explicit size control |
| A3(i) | Proved | A.6: functorial construction and precise comparison for general simplicial maps |
| A3(ii) | Proved | A.7--A.9: the kernel can be simple; its homology is forced by the universal cover |
| A3(iii) | UNDECIDED in unrestricted cardinality | A.10--A.11 prove dimension preservation for finite target bounds and the exact countable-source threshold. A general large, acyclic group of geometric dimension two without small quotients remains under investigation. Finite dimension alone is not a cardinality bound. |
| A4 | Proved | Full derived mapping-space comparison onto the components killing the kernel, including disconnected targets |
| B1 | Proved | B.1 checks both written R3 proofs and their specified unit |
| B2 | Proved | B.2: arbitrary small colimits of groupoid representables |
| B3 | Proved | B.3--B.4 and B.6: truncation, integral homology, and exact algebraic orthogonality for every larger localizer |
| B4 | Proved | B.7--B.8: sharp uniform threshold mu^+ < kappa; full classification of bounded invariant restrictions |
| B5 | Proved | B.5: enlarged-universe invariant ind-objects equal Ind_V(Hot_U) |
| C1 | Proof written; integration in progress | Both D.K5 proofs and exact universal sequence criterion in C_manuscript.tex |
| C2 | Proved; finite checks being extended | C.13--C.16: exact stage factorization criterion, mapping-space comparison square, suspension example |
| C3 | In progress | Page-by-page replacement and index-shape audit in C_manuscript.tex; chain-complex example being checked |
| C4.1 | Proved | C.1--C.4: clamping, strict action, coherent descent, both finality comparisons and composition identity |
| C4.2 | Proved, correcting the premise | One-sign padding and composition remain valid; comparison to the full localization has the exact restrictions stated in C_paths.tex |
| C4.3 | Proved | R7 local-representable proof, both signs, canonical maps, hammock comparison and isomorphism closure |
| C4.4 | Proved | Naturality in both endpoints, concatenation, the specified Q, literature comparison and finite (+,-,+) checks |
| D, strict retraction | UNDECIDED | Hot-class retraction exists. Equality in Cat_hot is the active obstruction. Collage construction reduces a fence-endpoint extension failure to a genuine fibrant-source counterexample. |
| D, lengthened-fence HEP | UNDECIDED | Proved for terminal targets, certain initial-target cases and upward closure equal to B. Failure of the product corner to be pseudo-Dwyer alone does not decide extension. |
| E, strict 2-categories | Proved, correcting the proposed answer | E.1--E.6: explicit finite B^2 C2 counterexample; ordinary groupoids give the exact invariant class |
| E, all strict n-categories | Proved | E.2--E.6, for the explicitly fixed normal Gray lax/pseudo convention. Independent audit pending. |

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

The finite-target construction uses a two-dimensional acyclic Higman complex in the dimension-preserving Baumslag--Dyer--Heller realization. A simple-envelope construction gives arbitrary cardinal bounds and can make the kernel simple, but its acyclic restoration currently uses three-dimensional cells. A strongly connected high-chromatic graph of Higman power relations forces small homomorphisms to vanish; its repeated incoming relations leave degree-two homology, so this attempt does not give the required acyclic group. The next active target is an unrestricted-cardinality acyclic aspherical two-dimensional construction.

### Strict retraction and fence extension

The model-category path-object proof constructs a strict retraction with the same ordinary homotopy class. It does not identify the finite-natural-transformation class. The proposed product-corner pseudo-Dwyer argument fails at its adjunction, and that failure is not a proof of non-extension. A fibrant-target noninjectivity example shows why ordinary homotopy-class equality does not finish the argument. A collage reduction now converts a suitable endpoint-extension failure into the requested strict-retraction counterexample; this is the active route.

## Checkpoint and typesetting record

Checkpoint 01 records the completed Part B and Part E proofs together with every deliverable and authored work record written so far. A PDF is not included in this first checkpoint: the LuaLaTeX build is being repaired before a first typeset version is exposed. The local Type1-font bootstrap is documented and reproducible in code/build_pdf.py. Final overflow counts and visual inspection will be recorded after a successful build.

Attached source files, extracts of those files, and downloaded third-party source reproductions are excluded. They are reference inputs, not authored deliverables. Authored research notes, all current sections, computations, outputs, build logs and the results table are retained. No authored passage from an earlier checkpoint has yet been removed.

The first three-hour progress reassessment is due around 21:21 UTC. Work is currently advancing the main unresolved items.
