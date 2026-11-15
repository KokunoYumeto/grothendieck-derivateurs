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
