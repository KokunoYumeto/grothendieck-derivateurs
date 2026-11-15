# PATHS research and verification report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No priority is claimed. “Proved” means that a proof is supplied or a supplied proof has been independently checked and reconstructed here; it does not mean that the result is new. “Open” means that this investigation has not settled the precise statement, not that the statement is known to be open throughout the literature.

## Deliverables and scope

The paper contains 76 numbered statements: 40 Proved, 19 Refuted, 11 Known, and 6 Open. The six Open statements contain individually specified subquestions, particularly D.22. The accompanying CSV has exactly one record per numbered statement, with the status checked against the TeX source. The bibliography contains 32 distinct entries after citation aliases are consolidated; every entry is marked verified or unverified, with actual source and version scope recorded. No unverified citation supplies a mathematical step. The appendix gives the disposition of every manuscript row and added numbered target requested in the prompt.

The central unrestricted-vertical inclusion problem is **not settled in full**. B.8 explicitly retains the general question, including two-out-of-three, saturation, calculus-of-fractions, model-category and Brown-category variants beyond the proved special cases. The package therefore does not claim an unconditional identification of Grothendieck’s arbitrary-vertical path category with the modern localization mapping space. This limit governs the literal pointed, Quillen and broad linear transfers. The sequential comparison results do not have this dependence: their proofs use a separate enriched-indexing argument.

## Source corpus and verification

The operative task is the attached `PROMPT(20261111-091225).md`. The selected cumulative source is the unversioned `6_PATHS_background.zip`, containing 222 files. It is the final, largest supplied cumulative package, rather than one of the earlier numbered snapshots. Its SHA-256 is `359048c67c05ce4bacde40e49a913e5f99e84f4f0dd65d1f9524ca4cb02b594e`. The supplied manifest, archive contents, and all extracted files were checked byte for byte by `code/source_integrity.py`; the complete result is `code/source_integrity_output.json`. The verification found no source-content discrepancy. The manifest also has nonfile notes interspersed with cumulative additions; these notes were retained separately from the 222 file records.

We read the relevant manuscript transcriptions in Chapters V, VII and IX, and the later axiom passages in XIII, XVII and XIX, together with the exact companion claim rows. The detailed logs below give manuscript page ranges and primary theorem numbers. CATHOT, TOTASPH, POLES, GALOIS and STRATA, and their supplied reviews, were treated as drafts requiring verification. Their status labels were not treated as evidence of correctness. In particular the GALOIS B.11 subcomplex-injectivity induction, GALOIS B.12 reduction, CATHOT E.20–E.25, the companion’s run-clamping argument at VII ms.86, and TOTASPH G.1–G.6 were checked before use.

Primary texts were opened for Dwyer–Kan, Quillen, Cisinski, Rădulescu-Banu, Szumiło, Lenz, Meier, Kaledin, Arlin, Fuentes-Keuthan–Kędziorek–Rovelli, Arakawa–Cnossen, Keller, Dugger–Shipley, Groth, Maltsiniotis, Fiedorowicz and the Kan–Thurston ingredients listed in the bibliography. Author-maintained Kerodon and Stacks Project pages were opened for the exact coherent-nerve, cofinality, subdivision and Dold–Kan statements used. Attached source versions are not silently identified with later published theorem numbering. The Kaledin result is explicitly a preprint theorem in version 3, whose Chapters 6 and 7 are marked preliminary. The Cisinski book numbering follows the attached author revision dated 30 July 2026; the book’s publication year is 2019.

Full copyrighted source extractions and attempted compilation of an attached reference were temporary reading aids. They are not redistributed in the result ZIP. The source archive remains the user-supplied evidence; the result ZIP contains our paper, verification notes, programs and outputs.

## Corrections and distinctions established

### Path constructions, reindexing and localization

Lead 1 correctly singles out weak vertical arrows as the hammock construction. B.2 specifies the actual simplicial reduction map and proves that it respects composition and units strictly. Its proof distinguishes the ordinary colimit in simplicial sets from a colimit in categories and checks the Reedy hypotheses needed for that colimit to compute a homotopy colimit. Allowing arbitrary vertical arrows is a separate change. Even saturated markings do not make the inclusion an isomorphism of categories; `[1]` with identity marking already refutes that assertion. The higher weak-equivalence claim remains B.8.

Lead 2 is true, with a stronger conclusion for the full category: when every marked arrow is already invertible, the full all-type category has a uniform categorical-homotopy contraction onto the discrete ordinary Hom-set. The parenthetical initial-object explanation is inadequate for the total all-type category, since the necessary type map need not exist. B.4 supplies the explicit uniform zigzag instead.

All three targets CATHOT E.26(1), (2), (3) are proved, for arbitrary wide markings, by C.P1–C.P3. The nonempty categories of type maps and endpoint-fixed transformations are contractible. They act coherently on the full path fibres. This coherent action descends to the reachability preorder, and both the ordinary type category and a preorder-cofinal sequence have the required homotopy-final maps to that preorder. This proves the weak equivalence of the specified sequential-to-total functor. It does not infer that equivalence from an ind-isomorphism or from unrelated pairwise homotopies.

CATHOT E.27 follows in C.P4 for every cofinal block containing both signs. The original CATHOT E.27 and VII ms.125 explicitly assume that the number of sign-runs is at least two, equivalently that the block contains both signs. C.P4 therefore covers the full original arbitrary-block target; the exclusion of one-sign blocks is not an added restriction. The canonical comparisons transport literal concatenation to the manuscript’s left/right/symmetric operation and prove its associativity and units in Hot. Thus IX-037 is settled for the raw construction without assuming B.8. Higher identification with the localization multiplication retains the appropriate comparison hypothesis; in the all-arrows case B.2 supplies it.

The stronger Cat hot assertion is false. C.P5 uses the four-object crown, all arrows marked, and a lift to the integer fence to show that the actual `q_L` has no inverse modulo a finite zigzag of natural transformations. A hypothetical inverse gives a uniform displacement bound; the explicit out-and-back paths violate it. The same `q_L` is a weak equivalence. A.9 independently verifies the six-face circle/subdivision example: all 456 reverse monotone maps have degree zero while the last-element map has degree one.

The component localization theorem uses only inversion of backward horizontal arrows. It never inverts an arbitrary vertical component. This observation is also required for the all-small-shape ind-representation in D.K5. B.6 constructs a coherent map from the full path space to the localization mapping space and proves that the inclusion is split monic in Hot. It does not prove the absence of extra higher homotopy on the full side.

The separate faithfulness question in VIIc-C004 is false. E.13 independently checks CATHOT F.2: shifting the finitary symmetric group on the natural numbers gives a nonsurjective endomorphism that is conjugation on the image of every finitely generated group. Its classifying-space map differs from the identity but induces the identity on all homotopy-class sets tested by finite categories. This disposes of the proposed set-valued inference while retaining the independently proved equality of the particular translation map with the identity. The counterexample category is infinite, and no finite truncation is substituted for its universal quantifier.

### Total categories and ordinary colimits

The comparison in VII ms.99–110 is a specified span through the sequential Grothendieck construction, not a generally available direct functor from the all-type total category to its sequential colimit. A.2 proves the filtered total-to-Cat-colimit comparison without assumptions that the transition functors are embeddings. A.3 gives the exact uniform condition on a base functor: the appropriate comma categories must be contractible. Preorder cofinality alone is insufficient; the constant terminal diagram over `BC2` is a complete counterexample. The manuscript already notices that obstruction, so we do not present it as a new correction to Grothendieck.

The proposed `Delta_inj` counterexample is correct. Its ordinary Cat colimit has type `S1`; its Grothendieck total has integral homology `Z` in every degree. Positive-degree homology diagrams are projective representables, which supplies the homotopy-colimit calculation directly. A.6 independently verifies total asphericity and exactness of abelian-group colimits, establishing the separating premise. The exact class of universally correct Cat-colimit shapes is left in A.8, with proved filtered lower and totally-aspherical upper bounds. No assertion for simplicial-set colimits is silently transferred through the nerve to Cat colimits.

### Pointed and additive claims

The pointed unit is `S0` for smash composition. The one-point Cartesian unit would select the zero map, which cannot act as identity when identity and zero differ. A pointed simplicial model category supplies strict zero absorption, Kan mapping spaces on cofibrant-fibrant objects, smash composition and the required units. Quillen’s comparison is an equivalence of fundamental groupoids, with the specified vertices and basepoint paths retained; it is not a literal equality of chosen constructions.

Mapping-space loop and suspension identities follow from enhanced homotopy pullbacks and pushouts. Representability of the groups `pi1` alone does not imply them: the pointed infinity-category on `*`, `S0` and `K(Z,2)` has trivial `pi1` mapping functors, but its nontrivial `K(Z,1)` loop space defeats the proposed stronger identity. For complexes over a commutative ring, C.8 constructs the requested objects in `D^{<=0}(k)` using fixed dg-projective replacements, good truncation and derived tensor, with grading signs and units included. General additive markings closed under finite direct sums do not automatically supply the additive-resolution hypotheses used in the checked enrichment literature. C.9 and C.10 retain the exact broader linear and literal pointed-ind targets.

### Diagram tests, rectification and enhancement

The final clause of Lead 3 is false. The finite two-object, five-arrow pointed category at IX ms.23, with identity weak equivalences, rectifies every shape and satisfies Kaledin’s enhancement axioms. There is no failed enhancement axiom to assign to it. Its deficiency is finite completeness: it has no product of the nonzero object with itself. It therefore cannot serve as a counterexample to rectification or enhancement. D.2–D.3 establish the correct diagnosis.

Rectifiability on a specified class of shapes implies the constant-diagram form of test (b), by the natural formula `H_ab(A)=[BA,Map(a,b)]`. The reading of the other formulation that merely asks for a weakly equivalent Thomason-fibrant category is vacuous and not equivalent to that test. D.5 gives a failure between finite shapes, replacing the earlier infinite test by a finite category with two parallel arrows. The more precise Cat hot/localness formulation and the full necessity assertion from the literal path version of (c) remain in D.22. Pointedness, the two possible representability directions in (a), and size bounds are stated explicitly.

Enough intrinsic cofibrations, with an initial object and the stated pushouts and two-out-of-three hypotheses, imply the finite precofibration axioms and rectification at every finite direct category. This rules out the requested finite-poset counterexample under those assumptions. It does not force every object to be cofibrant, two-out-of-six by convention, or the infinite ABC axioms. A complete four-element diamond example and the finite-set example distinguish these requirements. The version without an initial object remains separate.

Rectification at every cube is insufficient: the six-element circle poset misses degree two at its own finite shape. Finite simplicial sets rectify finite posets but fail at `BZ`, because strict finite automorphisms have finite order and the coherent Nielsen action does not. The opposite is Barwick–Kan fibrant and still fails at `BZ`. Conversely a nine-vertex fence rectifies every shape but is not Barwick–Kan fibrant. These results do not settle the narrower finite-only sufficiency of Barwick–Kan fibrancy. Relative poset presentations are also insufficient: the paper gives both a finite poset presenting `BZ` and an explicit countable poset presenting `BC2` that fails already at the finite shape `BC2`.

Kaledin’s actual `Pos` is finite chain dimension, not finite cardinality, and its infinite discrete shapes matter. D.15 shows, using the cited preprint theorem and a full pointwise-localization argument, that an enhanced naive family represents the actual localization `L(M,W)`. The statement is labelled Known, with that dependence retained. The circle example fails the named additivity axiom on the countable discrete poset: finite zigzags give uniformly bounded winding sequences, while the product contains unbounded sequences. This poset is already left-finite, so extension cannot fix that naive family while preserving its left-finite values.

The later manuscript cofibration and Quillen axioms give finite rectification under their finite hypotheses; the full transfinite axiom supplies the infinite ABC operations. Functorial factorization alone is not substituted for infinite colimits. Accessible fundamental localizers give rectifiable diagram theories on Cat through the left proper Thomason model, without requiring right properness. Intrinsic fibrations are more restrictive. D.23 verifies that every nonzero homology localizer fails to have enough of them, using free-group nullity and the explicit nonsurjective self-map with identity homology matrix. It does not confuse this result with a failure of pullback along an arbitrary Winfty-good path map.

### The small-index obstruction

D.K1–D.K5 independently verify the GALOIS argument rather than assume it. Acyclic maps are epimorphisms in unpointed Hot. Groups admit simple acyclic envelopes with the required cardinal control. The Kan–Thurston construction has the disputed subcomplex-injectivity induction, its local-coefficient comparison and its kernel description checked. This establishes `(KT_mu)` and CATHOT E.17 for a nonempty small filtered index in the same universe, with the specified groupoid-completion unit an ind-isomorphism on the original index category. It applies to the manuscript’s countable path system. Bounded test classes do not support the resulting all-small-shape one-type obstruction.

### Endpoint functors, intervals and stratification

The two endpoint models must be distinguished. The all-type functor is smooth but need not be proper, a fibration or an opfibration; the empty type already gives the outgoing-lift obstruction for `[1]`. Reversing paths does not reverse the base of the fibred Grothendieck construction, so the proposed duality shortcut is invalid. The eventual alternating model is both smooth and proper, yet still lacks strict Cartesian/coCartesian lifts. Its two lifting properties give the functorial mapping-path factorization and the exact homotopy fibres in E.5.

For the five-element rectangular-band monoid of type `S2`, the standard eventual path model is neither a strict fibration nor an opfibration. This does not refute the existence of another strict bifibration; E.11 retains STRATA’s exact target. The interval pushout-product fails for every `n>=1`, including the shortest block: the specified weak equivalence cobase-changes to a map from a contractible category to one of type `S3`. This extends the tested range of the inherited example without a priority claim. Products and concatenation used by the loop model require no pushout-product theorem. Finite interval cotensors have the correct total type but can have the wrong strict endpoint fibres.

Winfty smoothness and properness do not imply universal pullback preservation for an arbitrary larger localizer; the rational `BC2` example displays the distinction. Components of the marked subcategory do not by themselves define the proposed stratification: the two-element idempotent monoid with identity marking has contractible classifying space but a two-point localization endomorphism space. Finally the fixed-origin category of paths can be contractible without being filtered or totally aspherical, as verified in the finite fork/sphere example.

## Transcription and version corrections

At VII ms.66 the backward arrows must be said to lie in Sigma, rather than in X; the supplied transcription already marks this correction. We preserve it and do not claim to have discovered a new transcription error. The notation “full subcategory” at VII ms.65–67 concerns arbitrary vertical transformations and is decisive for the two constructions. We found no additional source-byte discrepancy. Several source interpretations, rather than transcriptions, require correction: a direct total-to-colimit map is not generally present; all-type properness does not follow from path reversal; Thomason fibrancy is not Cat hot localness; Kaledin’s shape categories are not finite posets; and the finite IX example does not fail rectification. Exact theorem numbers, inspected versions, and failed source fetches replaced by primary versions are recorded in the detailed logs below.

## Computations and their limits

All mathematical programs and their recorded outputs are included under `code/`. The finite path search covers 132 complete truncation comparisons, with no discrepancy in `H0` or `H1` over `F2`; it proves no stabilization theorem. At length four its largest category has 16,229 nonidentity arrows and 2,525,024 nondegenerate two-simplices. The crown program checks the covering rule and all endpoint-fixed ladders at parameter length six, while the proof supplies the unbounded displacement obstruction.

The poset enumerations give 456 subdivision-reverse maps of degree zero and 234 circle endofunctors with degree counts 3, 228, 3 at -1, 0, 1. The finite pointed category, diamond intrinsic-cofibration class, nine-fence horn, six-object suspension cycle, cyclic-group action and `S3` witness are completely specified and checked. The endpoint checks cover 543 `[1]` paths through length six. Rectangular-band associativity checks all 125 triples. The interval-pushout program constructs complete category tables, verifies all associativity equations, computes normalized-chain ranks over the rationals and confirms the sphere and suspension homology for `n=1,2,3`. The analytic proof, not these truncations, proves the full integer-indexed family. An independent rerun reproduced the Part E tables and ranks.

`code/README.md` gives commands, dependencies and source-dependent audit requirements. `code/assemble_package.py` verifies status agreement, one row per statement, bibliography keys and statement references. `code/build_paper.py` records the LuaLaTeX/BibTeX command outputs. PDF layout and final build diagnostics are recorded under `audit/`. The optional local-runtime switch creates a format inside the package for this container’s Type 1 font configuration and never modifies the system TeX installation; ordinary TeX Live installations can use the standard command without that switch.

## Exact remaining targets

A.8 asks for the exact class of shapes for which every ordinary Cat colimit has the homotopy type of the Grothendieck total. The residual scope is infinite shapes without a weakly terminal object; the proved bounds are stated in A.7. B.8 is the literal unrestricted-vertical inclusion problem, separately at the six hypotheses recorded there; the local grid sweep has been proved, but a coherent replacement on all simplices has not. The saturated three-object chain with only its long edge marked is a smallest-size remaining example within the tested family, not a claimed globally minimal counterexample.

C.9 retains the arbitrary additive relative-category enhancement proposal without the stronger dg or additive-resolution hypotheses. C.10 retains literal pointed and pointed-ind refinements, including absorbing zero coherences and the compatibility of specified comparisons. E.11 retains existence of another strict bifibration over the rectangular-band base; failure of the standard models is insufficient to settle it.

D.22 itemizes finite-poset-only, finite-category-only and cardinal-only recognition; the finite-product-test mapping-space upgrade; finite-shape sufficiency of Barwick–Kan fibrancy; intrinsic cofibrations without an initial object; the exact bounded Cat hot formulation of (b) and the raw-path implication (c) to (b); and unrestricted derivators for nonaccessible fundamental localizers. For targets without a chosen finite instance, no unsupported “smallest” counterexample is asserted. The preceding counterexamples and sufficient conditions do not supply the missing classification. The literature searches and the precise steps that remain unproved are given in the detailed records that follow.

## Detailed evidence records

The following records are included in this report so that the report is complete without opening its subsidiary files. Independent audit notes are also retained separately in `research/`.


## Detailed record: total categories and the small-index obstruction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. Statements labelled Proved are proved in this package, including independent verification of supplied arguments; that label does not assert novelty.

### Material read

We read the supplied prompt in its current version, the Chapter VII transcription at ms. 99–110, the relevant VII-b companion claim VIIb-C026 and commentary, and Chapter V at ms. 41–50 with special attention to the exact countable indexing and variance at ms. 44–45. We also read TOTASPH sections C and D, specifically the category-of-elements criterion, the affine-cone construction for Delta_inj, exactness of module colimits, and the weakly-terminal case; POLES D.6; GALOIS B.9–B.10 in sections/B.tex and the complete B.11–B.12 proofs in sections/B_KT.tex. The latter were not treated as authority.

The independent verification of GALOIS B.11 began with its subcomplex-injectivity induction. The intermediate pushout V in formula B.11.3 has injective edge groups on both sides for reasons already available at that point of the induction; the missing-simplex attachments then preserve those injections. This resolves the particular gap identified in the prompt. We also checked the local-coefficient skeletal induction, the description of the kernel as the normal closure of cone groups, the uniform cardinal bound, the acyclic epimorphism argument, and the left-Kan-extension argument in B.12. We found no error in these steps. D.K1–D.K5 give the full checked proofs and their application to V.

Primary bodies opened in this run are Cegarra (2020), Section 3, equation (9), Theorem 3 and proof; Higman, Neumann, and Neumann (1949), Theorems I–II; Baumslag, Dyer, and Heller (1980), the amalgamation statement before Proposition 1.1, Lemma 2.4, Proposition 4.1, Theorem 4.2 and Corollary 4.5; Hausmann and Husemoller (1979), Definition/Proposition 1.2 and Propositions 1.3–1.4; Hatcher (2002), Theorem 2C.5 and proof; Buchholtz, de Jong, and Rijke (2025), Theorem 2.9 and Definition 6.8 with proof; and Lurie's author-maintained Kerodon, Example 7.2.3.3, for the exact Quillen-A statement. The exact URLs and verification scopes are in A_references.bib. Original Thomason (1979) metadata were opened, but its body was not obtained; the paper cites the exact restatement and specified comparison in Cegarra Section 3.1. Cegarra's independent Theorem 3 proves stronger cohomology preservation; it is not described as a separate proof of the full homotopy-equivalence theorem. Initial attempts to open two scans of Quillen's original paper failed, so the Part A bibliography cites the opened author-maintained treatment. In the later CE audit, the relocated original Quillen scan was retrieved successfully, and Theorems A and B and the corollary to B were checked; its URL is recorded in CE_independent_audit.md. We did not use Maunder's paper as a proof or assert anything about its unchecked injectivity step.

### Computation

The command `python PATHS/code/a_finite_checks.py` was run from the workspace root, with output saved as `PATHS/code/a_finite_checks_output.json`. The implementation uses only Python's standard library. `code/a_build_register.py` generates the explicit result-register metadata and has its own output log.

It constructs the six-face triangle-boundary poset and its twelve-chain subdivision, verifies the order axioms, enumerates all monotone maps by every possible vertex image and compatible edge image, and computes winding numbers on the explicitly oriented nerve cycles. It finds exactly 456 reverse maps, all degree zero; the last-element map has degree one. It also checks the complete multiplication table of C2 and its normalized-nerve chain differential, giving H1 = Z/2. These are complete finite checks of the finite counterexamples A.4 and A.9.

The Delta_inj part checks every injection and 966 composition pairs through [5], verifies that the two [0] to [1] inclusions cannot be equalized within that truncation, identifies the ordered exterior bases with representable bases, and computes the colimit relations in exterior degrees 1 through 6. Every nonzero degree has free colimit rank one. These finite checks are not presented as evidence that truncations have stabilized: the all-degree infinite result in A.5 follows analytically from projectivity of the representable homology modules and the hocolimit spectral sequence.

### Corrections and clarifications

The proposed Delta_inj counterexample is correct. Its verification can be shortened materially: full exactness of all abelian-group colimits is unnecessary for that homology calculation, because each positive-degree homology diagram is representable and hence projective. We nevertheless rechecked the inherited proof of Delta_inj's total asphericity and included its integral affine-cone construction in A.6, since that premise is needed to separate the two classes of shapes.

The comparison at VII ms.108 is a span `C <- C_u -> C_infinity`. The universally valid sequential weak equivalence is the right-hand arrow. An isomorphism `C_infinity -> C` in Hot is obtained when the left-hand arrow is a weak equivalence; there is no generally specified direct functor `C -> C_infinity`. A.3 gives an exact condition uniform over all strict fibred diagrams: the base functor u must be homotopy initial, meaning every u/t is weakly contractible. Cofinality only in the associated preorder does not suffice even under the manuscript's parallel-reindexing homotopy condition. The manuscript itself already notices this at ms.109, so we do not call that observation a correction to the manuscript.

The finite POLES D.6 example checks exactly as stated. It establishes a distinction between Hot and Cat hot but does not decide the particular geometric comparison q_L. D.K4 verifies the small-index statement of CATHOT E.17 with the same index category. Its application to the path sequence requires all-small-shape invariance in the same universe. The result does not impose a one-type restriction on mapping spaces of a model category tested only on shapes small relative to that larger category.

### Remaining open statements in this contribution

A.8 leaves the exact class of shapes A for which every Cat-valued diagram has a correct ordinary Cat colimit unresolved. We prove the filtered lower bound and the strictly larger totally-aspherical upper bound with a separating example. This fulfills the prompt's alternative of bounds from both sides; we do not assert that the exact classification is open in the literature. The attached TOTASPH argument identifies the finite-object and weakly-terminal scopes with filteredness; the first residual scope has infinitely many objects and no weakly terminal object. Exact necessity for a particular fibred diagram, or for the restricted class satisfying the manuscript's homotopy hypothesis, is not confused with the universal equivalence in A.3.

### Literature searches

Searches included the exact titles of Baumslag–Dyer–Heller and Hausmann–Husemoller; `Embedding theorems for groups Higman pdf`; `homotopy colimit ordinary colimit categories filtered`; `colimits Cat homotopy filtered all diagrams`; and `totally aspherical sifted`. We opened primary papers behind the usable results and did not rely on search snippets or MathOverflow answers. The broad shape searches did not locate an exact classification sufficient to close A.8. The literature uses “totally aspherical” with other conventions, including a diagonal-asphericity condition; we used only the final-image convention specified by this prompt and did not identify those notions.


## Detailed record: localization and coherent path comparison

This work was produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The text below records the scope actually checked in this session; previous AI answers and reviews were treated as mathematical drafts.

### Files supplied to the main paper

- `sections/A_definitions.tex`: A.P1–A.P2, exact component localization and sequential comparison span.
- `sections/B.tex`: B.1–B.9, the literal inclusion, the restricted hammock comparison, proved cases, the canonical map to localization, and the unresolved general inclusion.
- `sections/C_paths.tex`: C.P1–C.P5, coherent type reparametrization, all E.26/E.27 comparisons, and a finite counterexample to a Cat-hot inverse for q_L.
- `research/B_results.json`: one registry entry for each of these sixteen statements.
- `research/B_references.bib`: only references used by these sections, with current-session reading scope.

### Sources read

The manuscript transcription was read at VII ms.27–57 for type maps and concatenation, VII ms.58–78 for path morphisms, admissible markings and ordinary localization, and the companion's blocks at VII ms.86, 94, 103–109 and 117 for interval-map contractions, parallel type maps, Grothendieck variance and the previous sequential argument. The CATHOT path section and its review were read, including E.20–E.27 and the q_L discussion. CATHOT E.4 was read directly to check the danger of using ind-isomorphisms or merely stagewise unbased homotopies. Its locally conjugate shift obstruction is precisely why the first attempted telescope argument was rejected.

Dwyer–Kan, *Calculating simplicial localizations* (1980), was opened as the supplied full PDF and extracted to text. Definitions 2.1 and 5.1, Propositions 2.2, 3.1 and 5.5, and Definition 6.1/Proposition 6.2 were read. Dwyer–Kan, *Function complexes in homotopical algebra* (1980), was opened as the supplied full PDF; Section 4, including Propositions 4.4–4.5 and Corollary 4.7, was read. These identify the weak-vertical mapping construction; they were not misquoted as a theorem about arbitrary verticals.

Arakawa–Cnossen, *Hammock localization via Segal animae*, arXiv:2608.19870, was read from the supplied LaTeX source: the definition of Zig and the fibre categories, the hammock anima and main theorem, the proof using fixed-shape colimits, the fraction discussion and fibrant-object theorem, the exact simplicial-category comparison, and the Reedy proof. Its arXiv abstract/metadata were independently opened. The exact source numbering is Definition 1.7, Theorem 1.9, Corollary 1.11; Theorem 3.26; Definition 4.3, Theorem 4.7, Proposition 4.8, Lemma 4.16 and Remark 4.18. A script records these counters, including the shared numbered-equation counter. No successful local compilation of this reference was required or claimed.

Chachólski–Scherer, *Homotopy theory of diagrams*, the institutional 2001 preprint, was opened in full through the web reader; Theorem 26.8 and Corollary 26.9 were read as an independent source for the natural Grothendieck homotopy-colimit theorem. Kerodon was opened at tags 01LA, 01JX, 01E7 and 02NX for coherent-nerve mapping spaces, detection of equivalences, restriction on functor categories, and cofinality. The enriched-type proof was independently reviewed by the agent responsible for colimits and KT; its notes are in `research/A_path_audit.md`.

### Decisive conclusions

The restricted Grothendieck construction is the hammock mapping space for every wide marking. The paper gives the actual simplicial reduction map: pull an n-simplex of the fibred total category back to its first type, then reduce the resulting width-n hammock. This is a simplicial map and strictly respects concatenation. The Reedy argument verifies that the ordinary simplicial-set colimit has the correct derived colimit, so the conclusion concerns this specified map, not only an abstract homotopy type.

For markings contained in the isomorphisms, the full all-type path category is actually equivalent to the discrete Hom-set in Cat hot. The uniform zigzag is `id <- pad <- T -> i effect`, where pad appends a positive identity edge and T puts the total effect on that last edge. Prefix composites provide the natural transformation into pad. This corrects the overly compressed “initial factorization object” explanation in Lead 2: a one-edge path is not generally initial in the total all-type category, because its type need not map to the target type.

All three exact targets in CATHOT E.26 are settled for arbitrary wide markings, and E.27 is settled for every block containing both signs. The key extra structure is the category P(tau,sigma) of interval maps and natural transformations. Its classifying space is empty or contractible, and the full path diagram carries an actual enriched action of these categories. The ordinary type category and every preorder-cofinal sequence map homotopy finally to the reachability preorder after this coherent descent. The first finality is checked by an actual comma category, contracted by `sigma*tau -> tau` and `sigma*tau -> sigma`; the second comma is a nonempty upward-closed subset of N. This proves weak equivalence of the specified sequence-to-total map and not merely independence of abstract homotopy types. The resulting canonical comparisons transport strict all-type composition to the manuscript's left/right/symmetric operation.

This does not identify arbitrary-vertical paths with the modern localization mapping space. The restricted diagram does not admit the same type enrichment: components of a natural transformation of interval maps can be forward arrows and need not be marked. Thus the new E.26/E.27 proof is independent of J and does not covertly assume it.

The q_L question in Cat hot is refuted by the four-object crown (two minimal and two maximal points), all arrows marked, endpoints at one minimum. Its universal-cover category is the integer fence. Endpoint-fixed transformations lift and move a fixed evaluated vertex by at most one. A finite zigzag between id and q_L r would therefore bound the distance of every positive-coordinate lifted value uniformly. Null-winding paths going 4N steps out and back contradict this. This is a finite relative-category counterexample, strengthening the initially noticed infinite-fence example. It does not contradict q_L being a weak equivalence.

There is a coherent map Q from the full all-type path space to the localization mapping space. It is constructed by inverting, **as an equivalence of diagrams**, the interval-localization precomposition maps `Fun([number of plus edges], C) -> Fun_relative(I_tau,C)` on endpoint fibres. QJ is the hammock comparison, so J is split monic in Hot. Separate pointwise choices of inverse were not used.

### Computation record

`code/b_path_search.py` constructs the complete category of paths with word length at most L in each chosen finite poset. It retains each type map as part of an arrow and computes every composable pair, so parallel type maps and their relations are not discarded. It computes H0 and H1 over F2 by collapsing a spanning forest and row-reducing all triangle relations.

The family comprises [1], [2], a three-object span, a three-object cospan, and the four-object crown, every composition-closed wide marking, and endpoint pairs (0,0) and (0,n-1). There are 66 cases at L=3 and 66 at L=4. All 132 comparisons have equal H0 and H1. At L=4 the largest examined category has 16,229 nonidentity arrows and 2,525,024 nondegenerate 2-simplices. The complete per-case outputs are `code/b_path_search_L3.jsonl` and `code/b_path_search_L4.jsonl`. No unbounded equivalence or counterexample is inferred from these finite computations.

`code/b_crown_checks.py` verifies the four-object base, unique cover lifts at all residues, all 85 endpoint-fixed paths and 387 endpoint-fixed transformations at parameter length six, and the out-and-back family for N=1,...,8. Sixty-three of the length-six paths have zero winding. Output: `code/b_crown_checks.txt`. The proof in C.P5 handles every N and every prospective inverse functor, beyond the finite checks.

`code/b_reference_audit.py` records the source theorem numbers and summarizes the two finite-search output files. Output: `code/b_reference_audit.txt`.

Commands used for the substantive computations:

```bash
python PATHS/code/b_path_search.py --length 3 > PATHS/code/b_path_search_L3.jsonl
python PATHS/code/b_path_search.py --length 4 > PATHS/code/b_path_search_L4.jsonl
python PATHS/code/b_crown_checks.py > PATHS/code/b_crown_checks.txt
python PATHS/code/b_reference_audit.py > PATHS/code/b_reference_audit.txt
```

### What remains unresolved

B.8 retains the general weak-equivalence assertion for J, separately for an arbitrary wide class, a two-out-of-three class, a saturated class, a homotopy calculus of fractions, a model category, and a category of fibrant objects. There is no verified counterexample and no complete higher-coherence proof in this work. The local sweep of one backward square is explicitly verified: after padding to -+-, the vertical components are `(id,w,w',id)`. Forward squares are handled by equality of composites. Making these sweeps into a compatible replacement for every higher simplex is the remaining step.

The source theorems on short fractions identify the restricted three-arrow category. With two-out-of-three, its vertical maps are automatically marked. This does **not** imply that its inclusion into the full all-type category is a weak equivalence. The distinction is retained even in the model and Brown cases.

The three-object chain with only the long edge marked is a concrete smallest-size case remaining in the tested family that is not covered by the already-invertible/all-arrows results. It is saturated, as witnessed by the walking split retraction, but no claim is made that it is a counterexample or globally minimal among all possible categories.

The stratified interpretation based only on components of Sigma is refuted separately in E.10 of the main paper; this section does not duplicate that result. The finite crown computation does not address a more restrictive Cat-hot invertibility statement for arbitrary chosen finite path-length bounds or for classes of categories satisfying additional uniform contraction hypotheses.

### Literature-search scope

Searches used the exact paper titles above and the phrases “Grothendieck path categories arbitrary natural transformations hammock localization”, “zigzag category natural transformations not weak equivalences simplicial localization”, “hammock vertical arbitrary localization”, and “Dérivateurs hammock”. A MathOverflow discussion from 2020, with a 2024 response, asks essentially the same unrestricted-vertical question and points to three-arrow calculus. It was used as a lead only, not as a primary theorem or proof. No checked source from this search proves the full assertion B.8. “Open” in this paper therefore means not settled in this audit, not a claim about the global state of the literature.


## Detailed record: rectification and enhancement

### Scope and deliverables

This part addresses Part D of the prompt, including the POLES, GALOIS, STRATA and Kaledin additions. The separate `D_kt.tex` contribution handles `(KT_mu)` and CATHOT E.17; neither is reproved here. The manuscript contribution is `sections/D.tex`, with 23 numbered results. `D_results.json` has a matching record for every result, and `D_references.bib` records the inspected source versions. The executable finite checks are `code/d_finite_checks.py`, with saved output `code/d_finite_checks.txt`.

The distinction between a relative category, its infinity-localization, the localization of its ordinary strict functor categories, and coherent functor infinity-categories is maintained throughout. Covariant shapes are used for the canonical comparison `R_A`; Kaledin's contravariant convention is stated separately. Universe bounds are part of every infinite-shape assertion. An ordinary finite category with nonidentity endomorphisms can have infinitely many nondegenerate nerve simplices, so it is not silently covered by a finite-direct rectification theorem.

### Principal corrections and positive results

#### The finite example does not fail rectification or enhancement

The two-object, five-arrow pointed category E at IX manuscript page 23 has a zero object 0, another object x, and End(x)={1,z} with z squared equal to z. With weak equivalences the identities, it rectifies every shape. Degree by degree, `Fun(NA,NE)=N Fun(A,E)`; ordinary localization does nothing. Its loop objects are the trivial pointed mapping objects, represented by 0 in both variables. Kaledin Example 7.2.1.16 says that the represented family K(E) is enhanced for every ordinary E, without requiring finite limits.

Consequently the prompt's requested failed rectification or failed enhancement axiom for this example does not exist. The actual obstruction is that x times x is absent: Hom(x,x) has two elements, and neither possible object has four maps from x. More generally a finite category with every finite product is a preorder; a pointed such category is equivalent to the terminal category. Results D.2–D.3 settle this correction, and the complete typed composition table and all 34 associativity triples are checked by the program.

#### Enough intrinsic cofibrations with an initial object are sufficient for finite posets

D.8 proves all CF1–CF4 directly. Composition and cobase stability of intrinsic cofibrations follow by identifying iterated pushouts. The nontrivial step is cobase stability of a trivial intrinsic cofibration. Factor the proposed base change as an intrinsic cofibration followed by W; the first change is weak because the factor is intrinsic, the intermediate comparison is weak because the base-changed original map is intrinsic, and two out of three supplies the final comparison.

Cisinski's canonical infinity-localization theorem, Theorem 7.6.17 in the attached book version, now applies to every finite direct category, including every finite poset and every span. This proves that no finite-poset counterexample satisfying the additional initial-object hypothesis can exist.

The conventions are audited rather than merged. Rădulescu-Banu's CF1–CF4 allow noncofibrant objects. Szumiło's attached convention additionally requires every object cofibrant and two out of six. Lenz's ABC convention has CF5 and CF6, including arbitrary permitted coproducts and countable composites. The four-element diamond with W consisting of identities and the two maps out of the least element has enough intrinsic cofibrations but two noncofibrant objects. Finite sets with isomorphisms satisfy the finite hypotheses but have neither a countable coproduct of singletons nor the indicated increasing sequential colimit. Thus no infinite ABC axiom is being smuggled into D.8. The two-out-of-six strengthening itself has not been separately derived from the intrinsic hypotheses; no claim that it fails in the diamond is made.

#### All cubes are insufficient

Let P be the six-element face poset of a triangle boundary, with every arrow weak. For any shape with an initial object, evaluation at that object is a nerve homotopy equivalence from its strict functor category to P, and the coherent target has the same property. Hence every cube rectifies. At the finite poset P itself, strict endofunctors have degree -1, 0 or 1, whereas coherent endomaps of its circle realization have every integer degree. Degree two is missing. The exhaustive enumeration finds exactly 234 monotone maps: 3 of degree -1, 228 of degree 0, and 3 of degree 1. D.10 refutes the proposed cubical criterion.

#### Finite posets do not suffice for BZ; BK fibrancy is independent of all-shape rectification

Finite simplicial sets, with monomorphisms and weak homotopy equivalences, form a finite cofibration category. Mapping cylinders give finite factorizations. Thus they rectify every finite direct shape by Cisinski, without invoking the infinite ABC theorem. A strict BZ action is an actual simplicial automorphism of a finite simplicial set, so has finite order. The coherent action on a wedge of two circles given by the Nielsen self-equivalence has first-homology matrix [[1,1],[0,1]], of infinite order. An equivalence of coherent actions would conjugate monodromy and cannot identify these orders. This proves the requested finite-poset versus BZ example.

The opposite relative category is a fibration category and therefore is fibrant in the usual BK structure by Meier Theorem 4.13. It still fails at BZ. The non-opposite cofibration category is covered by Meier's conjugate BK structure, not automatically the same structure.

Conversely the nine-vertex fence 0<1>2<3>4<5>6<7>8, with all arrows weak, has a fixed eight-step natural-transformation contraction. This contracts every strict functor category, even at infinite shapes, so every R_A is an equivalence. But the zeroth level of its BK nerve is Ex squared of NF. Its edges are monotone maps from the five-vertex fence. There are edges 0 to 4 and 4 to 8, and no edge 0 to 8, yielding an unfillable inner two-horn. D.11–D.12 prove both all-shape nonimplications. They do not settle whether BK fibrancy alone gives finite-poset or finite-category rectification; that narrower target is explicitly Open in D.22.

#### Relative poset presentations do not give naive diagram rectification

D.13 gives two constructions. The finite circle poset P maps to the ordinary group category BZ by labeling one incidence edge with a generator and the others with zero. This is an infinity-localization, but every strict BZ diagram in P is constant and has trivial monodromy. The coherent target has components indexed by integers.

For a finite target and finite test shape, the explicit countable poset Q consists of orbits of nonempty finite signed subsets of N times {+,-}, with at most one sign per index, under simultaneous sign reversal. Order is inclusion after sign alignment. Its nerve is the quotient of the barycentric subdivision of the infinite join of S0's, hence has type RP infinity. Normalize each representative by making its least-index sign positive; send an order relation to the unique aligning sign. This defines Q to BC2 and presents BC2 by inverting every arrow. Yet strict BC2 diagrams in a poset are constant, and the canonical comparison misses the identity homomorphism C2 to C2. The full multiplication law and both homomorphisms of C2 are checked. Kerodon Theorem 6.3.6.1 supplies the general presentation theorem, but is not used as an unsupported assertion of strict rectification.

### Kaledin comparison, with body-level verification

The attached paper is arXiv:2409.17489v3, dated 23 February 2026, 602 pages. The arXiv record says Chapters 6 and 7 are preliminary. It is treated as a preprint theorem, not asserted to have been refereed or independently reconstructed in full.

The following body passages were read: Definitions 2.1.5.3–2.1.5.4; Definitions 7.1.1.1–7.1.1.2 and 7.1.1.9; Definition 7.1.4.6; Definitions 7.2.1.1, 7.2.1.3, 7.2.1.4 and 7.2.2.1; Example 7.2.1.16; Proposition 7.2.3.7 and its proof; Lemma 7.2.4.1; Lemma 7.3.1.1 and its expansion formulas; Theorem 7.3.1.3 and its proof; Corollaries 7.3.1.5–7.3.1.6.

The shape correction is material. `Pos` consists of finite-chain-dimensional posets, not finite posets. `Pos+` consists of left-bounded posets, while `Pos+-` consists of left-finite posets. An infinite discrete set belongs to all three. The lower-case `pos` is the finite-poset category. The uncountable regular bound in the representation theorem is retained.

The axioms concern the family jointly: conservative point evaluations, the specified reflexive adjunction, fullness and essential surjectivity of the arrow comparison, arbitrary permitted disjoint-union additivity, semiexactness, and the prescribed excision/cylinder/semicontinuity squares. The extension proposition starts with a **good** family on left-finite posets; it does not extend arbitrary finite-poset data. Lemma 7.2.4.1 identifies its model-category extension with the naive larger family only with the stated completeness assumption.

D.15 resolves the representing-object question. A fibrewise localization map `ell:K(M) -> D` has fully faithful precomposition on cartesian functors and their modifications. This follows from ordinary localization in each fibre, including uniqueness of descended natural transformations and of restriction coherences. Enhanced functors in Definition 7.2.2.1 are precisely cartesian functors; they are not required to preserve Kan extensions. Represent D as K(X). The map ell represents f:NM to X, which inverts W. Factor it as gq through C=L(M,W). The canonical comparison D to K(C) is cartesian, so represents h:X to C. Then hf=q, giving hg=id by the localization universal property. Moreover K(g)theta ell=ell, and full faithfulness of precomposition with ell gives K(g)theta=id. Kaledin's homotopy-detection clause gives gh=id. Thus theta is the specified equivalence, and X is C. The reverse implication follows by transporting the axioms from the coherent family. The result is labeled Known, as a formal consequence of the cited preprint theorem; no independent novelty claim is made.

D.16 supplies an actual failed axiom and an actual admissible infinite shape. For P with all arrows weak and I countably infinite discrete, the additivity functor Pi1 B(P^I) to the product of Pi1 BP is not full. A finite zigzag in P^I gives a uniformly bounded sequence of winding numbers, whereas the product has the unbounded sequence (n). This locates failure at Kaledin Definition 7.1.4.6. Since I is already left-finite, the extension theorem cannot retain all naive left-finite values for this example. The finite E example fails no axiom at all.

D.21 proves a corresponding infinity-level upgrade when R_(A times J) is known for **all** Kaledin Pos shapes J: apply the same recognition argument to the relative category M^A. The finite-J version suggested in the prompt is not established by this argument; it is explicitly left Open with the missing enhancement/comparison step identified.

### The later Grothendieck conditions

Direct manuscript text, not only the companion audit, was read for XIII manuscript pages 7–12 and 50–59; XVII pages 39–40 and the finite Reedy discussion through page 50; XIX pages 33–38 and Question 3.14 at page 48.

XIII's M0 supplies finite limits and colimits. M2, M-prime and M-double-prime give both intrinsic factorizations, so finite-direct rectification follows already before the additional exactness hypothesis. “Exact weak Quillen” means W=TF composed with TC; it is not silently replaced by TC=C intersect W or TF=F intersect W. “Quillenisable” does not by itself imply large colimit completeness: the manuscript expressly considers small and noncocomplete examples.

XVII's Cof0–Cof3 are the finite precofibration axioms with an initial object and with the required pushouts. They therefore give canonical finite-direct rectification. The Brown lemma is correctly restricted to the category of cofibrant objects at XVII page 40. The stronger ambient reading at XIX page 35 is not used without properness C contained in intrinsic Cof_W.

XIX's full Cof4 includes small filtered-colimit existence and transfinite closure of C and its trivial subclass. Together with the finite axioms this gives CF5 by forming a well-ordered coproduct one summand at a time, and CF6 directly. Lenz then supplies all-relative-universe rectification and the left Kan extensions sought in Question 3.14. No functorial factorization or generating set is needed for that deduction. For intrinsic cofibrations, filtered-colimit stability of W makes the transfinite closure argument direct. Functorial factorization alone in XIX Corollary 3.3 does not supply the omitted infinite colimits.

### Localizers and the two-out-of-three warning

D.18 verifies accessible fundamental localizers using Cisinski 2006 Theorem 5.2.15: the Thomason model structure exists and is left proper without a right-properness assumption. Enough intrinsic fibrations is stronger. The Brown direction gives W=W_asph, and Theorem 6.1.11 identifies aspherical generation with properness; the same book connects this to model right properness. Raw Cat is not pointed, so the pointed tests are applied in its pointed model category rather than misusing the unpointed category.

D.23 checks the claimed asymmetry for every nonzero homology spectrum, including nonconnective spectra. Any E-aspherical space A is connected and has no nonzero homomorphism pi1(A) to Z, since such a map would split S1 off A and split Sigma E off zero. Thus every free-group classifying space BF is null for all E-aspherical A. Take the free-group endomorphism alpha(x)=x, alpha(y)=yxyx^-1y^-1. Its stable graph map is the identity exponent-sum matrix, so it is an E-equivalence for every E. Its image is not the full free group: sending x,y to the transpositions (12),(13) in S3 sends both alpha generators to (12). The mapping-space localizer V_(BF) contains every E-aspherical-to-point generator but excludes alpha; otherwise precomposition on self maps would give a homotopy inverse. Hence W_E is not aspherically generated and cannot have enough intrinsic fibrations. This proof does **not** infer failure of properness merely by pulling an acyclic-map equivalence back along a W_infinity path fibration; that shortcut is invalid.

D.19 retains two out of three as an explicit hypothesis where used. The fully faithful restriction class W_Set^1 fails it on e to BC2 to e. Trivial-action restriction is fully faithful; forgetful restriction on the regular C2-set sees four functions but only two equivariant functions. This does not prevent forming the ordinary localization, but does prevent invoking the cofib/fib axioms on descent alone.

### Source versions and exact citations

| Source | Passages actually inspected | Qualification |
|---|---|---|
| Cisinski (2003), *Images directes cohomologiques...*, AMBP 10(2), 195–244 | Attached PDF; Theorem 6.11; official metadata | The model-category right derivator theorem, with its limit hypotheses |
| Cisinski (2010), *Catégories dérivables*, BSMF 138(3), 317–393 | Definition 1.1, Theorems 1.30 and 2.21, Corollaries 3.20 and 6.21 | Finite derivable theory distinguished from homotopical completeness |
| Cisinski (2019), *Higher Categories and Homotopical Algebra* | Definition 7.4.12; complete statement and proof of Theorem 7.6.17; Theorem 7.9.8 and Remark 7.9.7 | Attached author PDF is actually dated 30 July 2026; theorem numbering refers to that inspected version. Published 2019 metadata verified separately |
| Lenz (2018), AGT 18(6), 3601–3646 | Attached TeX and published PDF; Definition 1.5, Warning 1.7, Theorem 3.33, Corollaries 4.5–4.6 | Not Definition 1.2/Warning 1.4; CF5–CF6 are part of the hypothesis |
| Rădulescu-Banu (2009), arXiv math/0610009v4 | Attached source; Definition 1.1.1, finite/infinite axiom distinctions, saturation discussion | Preprint, revised 8 February 2009 |
| Szumiło (2014), arXiv 1411.0303v1 | Attached Section 1.1, C0–C5 | Exact attached title retained; not silently replaced with one of the later related articles |
| Meier (2016), AGT 16(6), 3271–3300 | Attached source and published PDF; Example 2.5, Definition 2.6, Theorems 4.10 and 4.13, Corollary 4.15 | Main fibrancy theorem is 4.13, not 4.9; distinguish the conjugate structure |
| Kaledin (2026), arXiv 2409.17489v3 | Body passages listed above | Chapters 6–7 preliminary; theorem used with this status |
| Kerodon, tag 02MD | Theorem 6.3.6.1 and proof opened online | General localization presentation, not strict diagram rectification |
| Cisinski (2006), Astérisque 308 | Primary book PDF; Theorems 5.2.15 and 6.1.11, Example 6.1.14 | The accessible-localizer model theorem does not assume right properness |
| Arlin (2020), HHA 22(1), 117–139 | Official title/DOI metadata; arXiv v4 body, Theorems 19,29,37 | Published title differs from earlier arXiv title; author previously Carlson; strict and pseudonatural conclusions distinguished |
| Fuentes-Keuthan, Kędziorek, Rovelli (2019), TAC 34(39), 1220–1245 | Official journal metadata; arXiv PDF Definition 2.8 and Theorems 2.16,3.1,3.4 | Journal PDF fetch timed out; arXiv primary body supplied the numbered passages and is explicitly identified |

No unverified reference is used as substantive support. “Verified” here means source and cited passage were inspected, not that an entire external monograph has been independently reproved. The bibliography notes record version discrepancies and failed fetches. Extracted text under `research/d_text/` is an intermediate local aid and need not be included in the delivered package; the attached source books should not be redistributed as newly authored deliverables.

### Finite computation audit

The pure Python program has no dependencies. It checks E's composition and zero object; exhaustively enumerates W classes and intrinsic cofibrations on three small lattices; checks C2 laws and all endofunctions of its regular set; enumerates all 234 monotone P endomaps and their degree; enumerates all five-fence maps into the nine-fence to detect the missing edge; checks every endpoint retraction; verifies the eight-triangle suspension 2-cycle used for the finite test-(b) failure, including zero boundary and the absence of 3-simplices; checks the Nielsen power formula for n=1 through 100 while the proof supplies the induction; and checks the full S3 multiplication table, all 216 associativity triples, and the two subgroup sizes in D.23.

Finite verification does not stand in for an infinite argument. The infinite-order Nielsen conclusion is proved by its general power formula. The Kaledin additivity failure is proved by a uniform finite-zigzag length bound. The countable poset Q is defined and its classifying-space calculation proved mathematically. All finite base categories have complete relations or composition formulas in the text and complete relevant output in the code file.

### Exact unresolved targets

D.22 leaves six explicitly bounded gaps rather than a blanket failure label: intrinsic finite-only/cardinal-only recognition; finite-poset-product upgrade of a canonical homotopy-category comparison to infinity-level equivalence; BK fibrancy as a sufficient condition for the finite-only shape classes; enough intrinsic cofibrations without an initial object; the exact bounded Cat-hot formulation of IX test (b) and the path-object implication (c) to (b) without Part B's missing comparison; and the unrestricted derivator assertion for nonaccessible fundamental localizers. The sufficient model/ABC/Cisinski conditions, cube counterexample, finite-poset versus BZ separation, relative-poset counterexample, and all-Pos Kaledin recognition do not logically fill these remaining gaps. “Open” records what this package has not settled and does not claim a comprehensive negative literature result.

### Assembly notes

The section uses only standard LaTeX mathematics, `amsmath`, `amssymb`, `amsthm`, `natbib` commands, and the parent `result` environment. It introduces no custom macros and contains no top-level section command; the main manuscript owns the A–E sections. All numbered statements have matching JSON rows. Part D does not require fontspec or any interactive output.
