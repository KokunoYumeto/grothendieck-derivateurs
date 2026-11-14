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
| A3(iii) | Unrestricted dimension-two existence REFUTED; exact frontier still UNDECIDED | A.14--A.16 prove dimension preservation for every d >= 3 and every cardinal mu. Dimensions <=1 use identities; A.10 settles dimension two for finite mu. A.19--A.20 exclude W=S2 for every mu >= continuum and give the exact threshold mu<lambda for W=vee_lambda S2 when infinite lambda^aleph0=lambda. The interval aleph0 <= mu < continuum remains undecided for S2, starting at mu=aleph0 and allowing an uncountable G. |
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
| D, strict retraction | Refuted by a complete counterexample | The countable rigid fibrant-poset construction and its explicit collage in Part D give a Thomason trivial cofibration i:A->B with A fibrant and [p][i]=id in Cat_hot, but no strict retraction in the prescribed Cat_hot class. D.1 proves that a strict retraction in the prescribed ordinary homotopy class always exists. |
| D, lengthened-fence HEP | Refuted by a complete counterexample | The cofibrant and fibrant, weakly contractible poset F of Part D has isolated identity in Fun(F,F). The cofibration {a}->F and an arrow a->z prohibit any finite-fence extension of id_F. D.10--D.14 give the proved positive cases, including the requested single one-cell attachment and every finite cofibration. |
| E, strict 2-categories | Proved, correcting the proposed answer | E.1--E.6: explicit finite B^2 C2 counterexample; ordinary groupoids give the exact invariant class |
| E, all strict n-categories | Proved | E.2--E.6, for the explicitly fixed normal Gray lax/pseudo convention. Independent audit completed, including the typed Gray cylinder and transformation group. |

## Main findings recorded so far

1. The first R3 proof extends to arbitrary small colimits because the Kan--Thurston comparison is bijective before taking a colimit. Filteredness enters only the second proof's preservation of injections.
2. Among presentations with stages of at most mu arrows, invariance on tests with fewer than kappa arrows forces a global ind-groupoid precisely when mu^+ < kappa. The element-category construction proves sharpness, including kappa = mu^+.
3. One-sign blocks compute ordinary arrows (positive) or reversed marked arrows (negative). Their padding maps are isomorphisms in Cat_hot. The crown calculation concerns the comparison with the full localization.
4. Strict higher-category morphisms have a much more restrictive representability result than the proposed n-groupoid answer: the exact class is ordinary groupoids. The finite strict two-groupoid B^2 C2 already gives a complete counterexample to the proposed two-type criterion.
5. A three-object relative category gives a mapping space BC2 and a globally invariant constant-endpoint presheaf. Thus the fundamental groups of invariant mapping spaces can be nontrivial.
6. The map from transformation homotopy classes into ordinary homotopy classes fails to be injective even when source and target are cofibrant, fibrant and weakly contractible. Part D constructs such a countable poset with isolated identity and converts it, by explicit functors, into the requested strict-retraction counterexample.
7. Arbitrary cardinal bounds are compatible with dimension preservation in every dimension at least three. A.14 rechecks the surface blocks of Bartholdi--Mikhailov; A.15 constructs arbitrarily large simple acyclic groups with three-dimensional classifying models; A.16 proves the equivariant relative construction with all local coefficients. Thus the suggested dimension-only bound on mu is false even for the fixed target S3.
8. A.19 proves a residual-cardinality bound for every group with an actual two-dimensional classifying space: each nonidentity element survives in a quotient of size at most nu^aleph0, where nu=max(aleph0, generator cardinal of H1, rank H2). A.20 applies it to refute a dimension-two R2 resolution of S2 at every bound at least the continuum. For a wedge of lambda two-spheres with infinite lambda^aleph0=lambda, the exact existence threshold is mu<lambda.

## Computations

- code/e_strict_two_groupoid.py: all 8 associativity and 16 interchange checks passed; unique strict functor from BC2; two normalized 2-cocycles and one coboundary.
- code/cpaths_checks.py: finite vertex/letter correspondences, compositions, clamping categories, R8 certificate arrows, crown markings and (+,-,+) padding squares checked; detailed counts in its output.
- code/a_finite_checks.py and code/d_finite_checks.py: current finite checks and outputs included.

## Open work and approaches tried

### Dimension two: the remaining cardinal interval

This is the only requested item still undecided as an exact frontier. Unrestricted dimension preservation in dimension two is now refuted: A.20 gives the fixed counterexample W=S2 at every mu at least the continuum. A.10 proves the dimension-two construction for every finite mu. For this fixed target the remaining interval is aleph0 <= mu < continuum, with the first undecided instance mu=aleph0 and an uncountable source group permitted. The counterexample is complete, but it does not settle that remaining exact relation.

The new obstruction A.19 starts with a small aspherical subcomplex Y of an actual two-dimensional BG, containing a chosen nontrivial element and inducing ordinary homology isomorphisms. Its relative cellular boundary is an actual isomorphism between free abelian groups. Closing under full relator supports and the inverse boundary supports decomposes the relative presentation into countable blocks. The finite nonsingular-system theorem of OpenAI (5 October 2026, unrefereed) constructs a small coefficient group E solving every finite nonsingular system. The explicit reduced power E^N/E^(N) then solves every countable independent-row system: at coordinate n solve the first n equations, so each equation holds eventually. Compatible presentation maps give the detecting quotient of size at most nu^aleph0. The source theorem's complete 16-page proof was read independently by all four agents; the incidence, trace-length and planar-band arguments were checked. The companion Lean verification covers an earlier one-relator theorem, not this complete multi-equation result. The detailed source audits are in research/D_nonsingular_audit.md and research/Cpaths_nonsingular_audit.md.

A.20 combines this bound with A.13 to give an exact threshold for every W=vee_lambda S2 with infinite lambda^aleph0=lambda: existence holds precisely for mu<lambda. This supplies exact instances beyond the fixed finite-rank target without claiming that the remaining interval for S2 is settled.

The surface-block construction supplies dimension at most max(dim W,3) for every cardinal bound. Its equivariant proof retains H2 of the universal cover, including torsion, as an actual direct summand and removes the extra free summand without creating H3. Thus every target dimension at least three is settled without a cardinal restriction.

The failed dimension-two routes now have explicit obstructions. A strongly connected high-chromatic graph of Higman power relations forces small homomorphisms to vanish, but repeated incoming relations leave degree-two homology. A.17 proves that retaining exactly one predecessor per generator gives countable retracts detecting every nonidentity element. A.18 proves that every transfinite tower of layered unimodular one-generator/one-relator extensions maps nontrivially to one fixed countable group. A perfect locally free group cannot have a finite normal generating set, by the complete formal-series argument in research/D_normal_frattini.md; thus a locally free normal-Frattini cover of a nonabelian simple group is excluded.

A single positive-genus surface block killing an old H2 class creates new H2: its H1 kernel has rank at least the genus, by the symplectic cup-product pairing. The finite replacement construction has a two-dimensional model, but its infinite sequence has only a proved three-dimensional telescope model. Free products of countable acyclic groups retain factor quotients. Universal central extensions do not supply the required geometric-dimension bound. A.21 proves that reverse commutator towers, despite giving actual two-dimensional homology extensions, all map to a fixed countable torsion-free two-conjugacy-class group. A.23 proves the exact congruence extension property for every two-dimensional homology-equivalence inclusion: every quotient of the coefficient group injects into the corresponding pushout. In particular a simple final group requires each nontrivial homology core to be simple already. A.24 proves that a reduced power of the particular two-conjugacy-class target has minimum nontrivial quotient cardinality exactly the continuum, so it cannot be compressed to a countable detecting quotient. Its explicit Z^m subgroups rule out finite geometric dimension, so it is not a dimension-two construction. A.25 constructs a fixed countable coefficient-preserving target for every homology-equivalence presentation whose relators use at most two new variables, each with nonzero exponent sum. Its graph argument covers arbitrary valence and rules out the anchored Camm word pattern under the actual small-homology dimension-two hypotheses. General countable nonlinear systems and Camm-style balanced amalgams with large free vertex groups remain under active investigation. Every unproved step remains an active obstruction, not an asserted theorem.

### Strict retraction and fence extension: completed

Start from a point and, at every finite stage, attach a fresh copy of every generating Thomason horn along every map into that stage. The union F is a countable, cofibrant and fibrant, weakly contractible poset. Every principal lower set is finite, and no point has a greatest strict predecessor. For every strict pair x<z, a fresh one-horn supplies y>=x such that y and z have no common upper bound; later Dwyer inclusions preserve this incompatibility. A map g<=id would move a minimal point and create a greatest strict predecessor. A map g>=id moving x to z would make g(y) a common upper bound. Thus id is isolated under natural transformations, proving that no finite fence can extend the prescribed move of the original point a along a->z.

Adjoin an object c below precisely the upper set of z, with reflector q(c)=z and q|F=id. This collage A is fibrant by the explicit horn-lifting construction. Glue a second copy of F to A by c=a. The resulting inclusion i:A->B is a Thomason trivial cofibration. The map p restricts to the identity on the second F and sends c to a on A; the two transformations through the reflector give [p][i]=id_A. A strict retraction in [p] would produce an endofunctor of F homotopic to id that moves a to z, contradicting isolation. Two independent audits checked the horn pushouts, noninjective attaching maps, lower sets, branching, and the collage maps.

The positive statements are retained: the model-category path-object proof gives a strict retraction in the same ordinary homotopy class; finite cofibrations and finite-stage bounded-dimensional cell constructions have the full prescribed fence extension property. D.9 supplies the eight-step triangle table, D.11 the 4(n+1)-step relative comparison, and D.12 the explicit extension bounds. An earlier missing common facet in the relative cylinder was corrected and the proof independently rechecked. The final counterexample requires an infinite construction and rules out every finite padding length.

## Checkpoint and typesetting record

Checkpoint 01 records the completed Part B and Part E proofs together with every deliverable and authored work record written so far. A PDF was not included in checkpoint 01: that initial LuaLaTeX build was still being repaired. Checkpoint 02 records completion of Part C and the subsequent proved retraction cases, including a checked PDF. The local Type1-font bootstrap is documented and reproducible in code/build_pdf.py. Checkpoint 02 has 59 pages. The final LuaLaTeX log has 0 overfull horizontal boxes and 0 overfull vertical boxes (before visual review: 0 and 0; after review: 0 and 0), no undefined references or citations, and no LaTeX warnings. Pages 1, 3, 7, 12, 18, 24, 30, 36, 42, 48, 54 and 59 were rendered and visually inspected. No clipping, overlapping text, missing glyphs or protruding displays were observed. The PDF hash and the exact visual-review record are in logs/PDF_QA_PASSED.json in that checkpoint.

Checkpoint 03 records completion of Part D and the dimension-three advance A.14--A.16. It contains 80 registered statements and a 69-page PDF. Before visual review there were 0 overfull horizontal boxes and 0 overfull vertical boxes; after review the counts remain 0 and 0. A fourth LuaLaTeX pass cleared the cross-reference rerun warning. The final log has no LaTeX warnings and no undefined references or citations. Pages 1, 4, 9, 12, 14, 15, 16, 17, 22, 29, 36, 43, 50, 58, 59, 60, 61, 62, 63, 66 and 69 were rendered and visually inspected, including every new dimension and retraction proof page. No clipping, overlapping text, missing glyphs or protruding displays were observed. The hash and page list are recorded in logs/PDF_QA_PASSED.json.

Checkpoint 04 records the residual-cardinality obstruction A.19, the exact family A.20, and the construction obstructions A.17--A.18 and A.21--A.25. It contains 89 registered statements and an 83-page PDF. All three final LuaLaTeX passes completed; the final log has 0 overfull horizontal boxes, 0 overfull vertical boxes, no warnings and no undefined references or citations. The before/after overflow counts are 0/0 in both directions. Pages 1, 4, 10, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 42, 50, 57, 62, 65, 71, 76, 80, 82, 83 were rendered and visually inspected. The initial 84-page candidate left two bibliography lines on its last page; the bibliography typography was adjusted and the changed pages rerendered. No clipping, overlap, missing glyphs or protruding displays were observed. The PDF hash and page list are in logs/PDF_QA_PASSED.json. The generated stale bibliography and missing Euler font-map entry were repaired during preflight; their failed logs remain as records and are superseded by the clean final build.

The stable results-row ID A3(iii)-unrestricted is retained from checkpoint 03. Its updated statement records that A.20 refutes unrestricted dimension-two existence while the interval aleph0 <= mu < continuum for S2 remains undecided. No prior statement has been dropped.

Attached source files, extracts of those files, and downloaded third-party source reproductions are excluded. They are reference inputs, not authored deliverables. Authored research notes, all current sections, computations, outputs, build logs and the results table are retained. No mathematical passage from an earlier checkpoint has been omitted. The corrected current source supersedes earlier working wording; earlier build-pass logs are superseded by the clean three-pass LuaLaTeX logs. The checkpoint archives retain their original contents.

In checkpoint 03 the four-pass logs supersede the earlier three-pass logs. The earlier PDF, results table, bibliography, report, snapshot and PDF-QA record are superseded by their updated versions with the same filenames. The checkpoint-02 renderings logs/rendered/page_03.png, page_07.png, page_18.png, page_24.png, page_30.png, page_42.png, page_48.png and page_54.png are superseded by the newly rendered page sample; their page numbers described the former 59-page layout. No authored proof, research note, computation or program from checkpoints 01 or 02 is omitted. The exact path comparison is retained in logs/checkpoint_contents_diff.json.

The first three-hour progress reassessment is due around 21:21 UTC. Work is currently advancing the main unresolved items.

## Independent audit and source-access record

Part E and the sharp cardinal and bounded-restriction results B.7--B.8 received independent proof audits. The audit confirmed the transformation group law, localization comparisons, equality case of the cardinal threshold, and the relative homotopy-coequalizer map. C.17 gives the specified finite-image/all-functions comparison, so the all-test Hom comparison is not silently assumed.

Independent checks of A.21 confirmed the finite-prefix cell cancellations, actual two-dimensional union, and the recursive solution with constant-map resets. Root also checked the formal-series proof A.22, the quotient and base-change maps A.23, and the support-ideal and ultrapower proof A.24.

A.25 was checked independently by all four agents: the graph classification, rational functional excluding ungrounded trees, finite nonsingular cycle equations, arbitrary-valence recursion, and the countable-core consequence all pass.

The full independent audits of A.19 confirmed its small core, exact cellular matrix, countable support closures, reduced-power solution, and compatible transfinite homomorphisms. A.20 uses that actual detecting map to contradict the requested kernel condition.

The original Kan--Thurston 1976 and Maunder 1981 papers remain marked unverified: public publisher and historical PDF links failed or exposed only metadata. No theorem in this manuscript depends on their unexamined text. The primary Baumslag--Dyer--Heller, Hausmann--Husemoller and Leary proofs used in Part A were opened and checked.

Checkpoint 04 path supersession: logs/latex_pass_4.out; logs/rendered/contact_1.png; logs/rendered/contact_2.png; logs/rendered/contact_3.png; logs/rendered/contact_4.png; logs/rendered/page_09.png; logs/rendered/page_12.png; logs/rendered/page_15.png; logs/rendered/page_16.png; logs/rendered/page_17.png; logs/rendered/page_43.png; logs/rendered/page_58.png; logs/rendered/page_59.png; logs/rendered/page_60.png; logs/rendered/page_61.png; logs/rendered/page_63.png; logs/rendered/page_66.png; logs/rendered/page_69.png. These are prior rendering/build records with their replacement and reason listed in logs/checkpoint_contents_diff.json. No authored mathematical passage was removed.
