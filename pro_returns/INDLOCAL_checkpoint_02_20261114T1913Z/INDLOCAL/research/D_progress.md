# Part D working record

## Exact remaining question
For every U-small Thomason-fibrant category A, every Thomason cofibration i:A→B, and every p:B→A with pi connected to id_A by a finite zigzag of natural transformations, must there be a strict retraction r in the same zigzag class as p?

A strict retraction in the same Hot class is verified by the model-path argument below. The remaining requirement is equality in Cat_hot. General lengthened-fence HEP is also undecided.

## Completed arguments
1. Rechecked CATHOT E.6: Fun(Z,A) receives constant-path c:A→Fun(Z,A), a categorical homotopy equivalence; factor endpoint evaluation by trivial cofib j and fibration to A²; both evaluations are trivial fibrations since A fibrant. Lift along i to get r with ri=id and equality in Hot. No inference to Cat_hot has been made.
2. For any sieve i:C→D and target F with terminal object, every fence homotopy on C with initial extension f:D→F extends after one padding step. First replace f(d) by terminal for d outside C, retaining f on C. The transformation f⇒f' is identity on C. Then use the prescribed homotopy on C and terminal elsewhere. All mixed arrows point from C outward.
3. For any pseudo-Dwyer i:C→D, cosieve W, retraction r:W→C, ε:ir⇒id_W identity on C, and target F with initial object, analogous HEP. Replace f by f'=fir on W and initial outside W. The transformation f'⇒f has component fε on W and unique arrows from initial outside. Extend H by Hr on W and initial outside. Cosieve closure ensures no arrows from W outward. Mixed arrows have initial source, so naturality is automatic.
4. For W=D the construction in (3) uses no initial object and gives HEP for every target.
5. Target groupoid: strict retraction naturally isomorphic to p by objectwise conjugation along pi≅id; complete check to write in section.
6. Target local: Hot-level retraction represents the same Cat_hot class because definition of local gives injectivity of π0Fun(B,A)→[BB,BA].

## Approaches explored; exact obstacles
- Product corner inclusion fails pseudo-Dwyer property already for [0]→[1]. Raptis p.221. This does not refute subdivision HEP: the initial three-point fork is fibrant and provides an explicit one-padding extension despite lack of square filler.
- Attempt to infer injectivity π0Fun(B,F)→[BB,BF] from fibrancy is unsupported. CATHOT A.6 equivariant free fibrant completion suggests fixed-point loci of Fun(BG,F) can retain arbitrary nonfibrant posets; cannot assume functor categories fibrant.
- Try use cofibrant-source cylinder B×cSd²Δ1: product preservation of Thomason cofibrations is not proved. Raptis product-corner counterexample and Pavlov 2023 only yield h-cofibration and weak-equivalence facts, not the required lifting property.
- Cell induction: a generating cofib cSd²∂Δn→cSd²Δn is D→K(D), where K(D) has D×[1] and a common lower vertex at the top copy. Simplicial prism filling does not immediately produce an unmodified-source product-fence homotopy; a uniform time subdivision across arbitrary cell dimensions remains the obstacle.
- Equivariant free fibrant completion can preserve fixed poset D in Q^G, but new objects of a Thomason relative cell complex have no new isotropy. A construction with BG factors on new cells therefore fails the cofibration hypothesis.

## Literature opened and checked
- Thomason 1980: supplied PDF, extracted to D_Thomason.txt.
- Cisinski 1999: supplied PDF, extracted to D_Cisinski.txt; Proposition 2 every Thomason cofibration pseudo-Dwyer; Proposition 1 poset source gives poset target and Dwyer.
- Raptis 2010: supplied PDF, D_Raptis.txt; §2 definitions, Proposition 2.4, p.221 corner obstruction, Proposition 4.8 strong mapping-cylinder factorization.
- May–Stephan–Zakharevich 2017 supplied PDF, D_MSZ.txt; §7 fibrant posets and partial model structures; does not classify all fibrant posets.
- Pavlov, The enriched Thomason model structure on 2-categories, arXiv:2208.02954v4, opened https://arxiv.org/pdf/2208.02954, web ref turn23view0. Proposition 3.4 flatness proof checked; Corollary 3.5 asserts weak equivalence only, not cofibration, for acyclic pushout products.
- Meier–Ozornova, Fibrancy of partial model categories, arXiv:1408.2743v1, opened https://arxiv.org/pdf/1408.2743, ref turn30view0. Theorem 2.1 and description K(D) in Remark 4.1 opened; no general HEP asserted.

## Next work
Seek a relative simplicial prism comparison with uniformly bounded fence length, or construct a genuine relative-cell counterexample forcing unbounded lift length. Test the single cSd²Δ1 attachment explicitly before attempting arbitrary-dimensional cells.


## Checkpoint 02: new results D.7–D.13

- D.7: every backward transformation lifts along any full sieve by composing each mixed arrow with the given component.
- D.8: universal strict retraction is exactly equivalent to forward endpoint extension. The collage of h1:C→F is itself fibrant when F is fibrant; the explicit reflector/unit and pushout transfer the endpoint problem to a retraction problem.
- D.9: fixed-endpoint P4 paths into a fibrant F represent Pi1(BF) bijectively. Equal classes admit an exactly eight-edge alternating comparison, given by a verified table in the 25-object poset cSd²Δ2.
- D.10: an arbitrary set of one-cells attached in one stage has full prescribed fence HEP, with length bound 9L. This decides the prompt's requested single attachment to a fibrant circle/sphere poset model affirmatively.
- D.11: relative comparisons of P_n maps have length 4(n+1). A relative simplicial cylinder is C_n=Δ^(n+1) ⊔_W ∂Δ^n, where W=π^(-1)(∂Δ^n) for π identifying n,n+1. The boundary consists of the side facets AND the common end facet V. An initial draft omitted V; independent C-agent audit caught this, and the corrected W formula is now saved. The rank sweep transforms all faces containing n by adding n+1 in decreasing cardinality, then removes n in increasing cardinality, with two comparison steps per rank.
- D.12: a coproduct of cells of dimensions at most N has HEP bound (4N+5)L; finite sequences of bounded-dimensional stages multiply bounds; arrow retracts inherit HEP. The Kan mapping-space horn step and all padding/retract equations were independently checked by C agent.
- D.13: a cofibration finitely presented under its source is a retract of a finite relative cell complex. Finite dependencies close to a finite subcomplex by well-foundedness and König's lemma. Hence every cofibration between finite categories satisfies HEP; no finite-category counterexample exists.

Programs d_prism_probe.py and d_higher_prism_checks.py verify actual lifted flag comparisons, not a quotient surrogate. The latter checks dimensions zero through four (source sizes 1, 5, 25, 149, 1081). All pass. D_results.json includes D.1–D.13 and two explicitly unresolved metadata-only rows, D.U1 and D.U2. D_references.bib includes checked primary sources.

## Exact remaining infinite issue
No proof or counterexample for an arbitrary unbounded relative Thomason cell complex is known in this work. The proved comparison bound grows with dimension, and iterating stages grows the fence further. A global finite fence must be uniform over all cells. An alternate proof could avoid this rank sweep; it has not been obtained.

Potential lower-bound target: free fibrant completion R(K_n) of the finite prescribed product corner. Its old category K_n remains a Dwyer sieve. An old→new←old two-step comparison retracts to the old category via the cosieve right adjoint, but longer comparisons can leave the cosieve through new cell centers. No lower bound stable under all horn attachments has been proved.

A separate possible target, the group-labeled filtration T from CATHOT E.4, was analyzed and does not yield a counterexample by homotopy-injectivity failure: for functors f,g:D→T, a natural isomorphism of their composites into BG_infinity gives a two-step categorical comparison in T. At object x take the maximum of f(x), g(x), and the support of the conjugating permutation; naturality makes that maximum monotone along arrows. Thus the mapping comparison is injective for this target, even though the target is not local.

## Additional source verification
The primary Numdam pages for Thomason and Cisinski were independently opened; the public primary Raptis PDF was opened and Theorem 2.6 located; the authors' MSZ preprint was opened and compared to the supplied published version. Lurie's official HTT PDF Proposition A.2.2.1 was opened for independence of cylinder object, used only in ordinary simplicial sets under the fixed boundary. The reference key CpathsLurieHTT is reused from the existing bibliography.
