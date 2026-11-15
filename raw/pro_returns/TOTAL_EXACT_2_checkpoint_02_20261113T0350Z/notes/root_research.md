# Research log

Initial literature searches: "totally aspherical" "exact" category colimits; "exact colimits" "fixed point" total aspherical; "colimits" "acyclic" "permutation" flat categories.

The complete outcome table, proof-side and construction-side route records, source-access table, and precise unresolved steps are maintained in `TOTEX2_report.md`. This note supplements that record; it does not claim a solution.

## Subsequent searches

Additional queries included:

- `"colimits" "permutation" "exact" category aspherical`
- `"quasi-filtered" "homology"`
- `"fixed point property" "affinization" category`
- `category Ramsey property compact Hausdorff functor inverse limit exact colimits`
- `"Ramsey" "integral" "affine" category exact`
- `"totalement asphérique" "exact"`
- `"totalement asphériques" filtrantes`
- `"catégorie" "totalement" "asphérique" "filtrante"`
- `"exact colimits" "acyclic" category`
- `"homotopically flat" "colimit" category`
- `"category" "all set-valued" "acyclic"`
- `"exact colimits" "homology" Isbell Mitchell`
- `"homotopy colimit" "ordinary colimit" "every diagram" "filtered"`
- `"category" "permutation modules" "flat" colimit`
- `"Ramsey" "exact colimits"`
- `"integer" "convex Ramsey property"`
- `"amenability" "exact colimits"`
- `"On the homology of small categories" pdf Husainov`

The French and English total-asphericity searches mostly returned the distinct diagonal/test-category notion; those results are not substituted for the present definition. A publisher-hosted full PDF of Husainov (2004), *On the homology of small categories and asynchronous transition systems*, was opened at https://archive.intlpress.com/site/pub/files/_fulltext/journals/hha/2004/0006/0001/HHA-2004-0006-0001-a022.pdf . Its introduction and Section 2, especially printed p.446, discuss the fixed-point/exact-colimit problem with a weaker hypothesis; this passage does not supply the missing totality implication. The earlier ETH mirror returned 404. The English author-uploaded Husainov (2002) text was reopened at Theorems 2.5–2.7 to check their variance and hypotheses.

## Additional proof routes examined after the compact-convex obstruction

1. **Augmentation ideals over Q or F_p.** For an abelian diagram M, the group algebra of the underlying additive group is a permutation module. Its augmentation ideal I is acyclic under totality, as are tensor powers of I obtained as kernels using products of the underlying set action. The desired linear diagram is I/I². The multiplication map I⊗I→I² is not known to have acyclic kernel; replacing its image by its source would assume the missing result. Rational logarithms land in completed group algebras and require infinite products/completion, neither of which belongs to the proved resolving closure. Finite scalar dilations do not provide a natural finite-support logarithm or a natural permutation summand.
2. **Mac Lane cubical or stable free resolutions.** Their free terms can be built from powers of the underlying set, and totality gives termwise colimit acyclicity. The colimit of the resolution nevertheless computes the unresolved derived additive colimit. Totality does not by itself identify its degree-zero algebraic reflection with a homotopy-preserving functor. The fact that some cubical face maps are maps of sets does not make the entire augmented resolution a contractible simplicial set diagram.
3. **Torsor encoding of a module inclusion.** For M↪N and P=N/M, the map of element categories for UN→UP has fibres carrying M-torsors. The transition maps of those fibres need not be bijections. Thus this is not a covering-space comparison to which contractibility of the base can be applied. Replacing the fibre diagram by a local system is an unjustified step.
4. **Generic graph realizations of free diagrams.** A linear map between free abelian groups can be realized by a graph map sending an edge to an edge path, but it need not be induced by a map of graph edge sets. Functorial subdivision or passage to Cayley graphs introduces additional cycle modules; no acyclicity transfer back to the original module has been proved.

These are failed reductions or exact unresolved steps, not counterexamples to the main implication. The new compact-convex theorem and the Boolean coefficient-pinning example are complete counterexamples to the auxiliary statements they explicitly name.

## Selected large-target breakthrough and its remaining quantifier

The exact fixed-path attachment formula made it possible to prove a selected infinite construction. We maintain separate linear orders on actual points and on binary graph components, and strong geodesic convexity of all arrow-image components. A strict necklace-colimit calculation and real-line homeomorphisms show that every sufficiently large repaired necklace can carry the required two orders. A short-path cut argument gives convexity whenever s>(2n−2)(D+1). The fixed interval of a convex increasing pair is connected, so the attachment kernel vanishes. Every admissible a-sequence permits a sufficiently large choice at each finite stage; one deterministic least-choice construction is given. Its first-stage H2 generator survives in the countable union. This proves total strictly contained in quasi-filtered. It is not a proof of the universal-choice statement C.1 and does not decide total versus exact.

The universal case is still being attacked through fixed-set geometry. Point-transition length and component-transition length cannot be identified: an exact mixed-branch computation exhibits lengths two and three respectively. The selected proof allows an independently enlarged common bound. A generic connected convex-graph search and potential long-cycle examples test whether the extra diameter bound is dispensable; only configurations actually realizable by C.1 could refute its assertion.

## Further main-question routes

The model-category stabilization argument was examined again. Under totality and I, ordinary colimit of simplicial sets preserves objectwise weak equivalences and monomorphisms, and its pointed version commutes with suspension. Its stabilization nevertheless computes a spectral colimit, not the ordinary abelian colimit on the heart. The latter identification is exactly the unresolved t-exactness condition; being left Quillen does not supply it.

A sharper possible criterion is vanishing of H2 of every category of elements under I and IV. The attempted encoding would have to turn the column obstruction into the second homology of a genuine A-set. Presenting an arbitrary module by a diagram of group presentations or Cayley graphs does not yet do this. A free group can be replaced individually by a graph, but those replacements need not be natural; the finite free-factor nerve example shows the danger without the totality hypothesis.

Additional exact-title and phrase searches included `"exact colimits" "second"`, `"fixed point property" categories "homology"`, `"permutation modules" "constant" "injective" category`, `"W. T. Spears" "colimit"`, `"When is colimit exact" pdf`, and the Oberst title with `pdf`. They produced the already opened Isbell 1968 body, metadata for the still unopened Isbell 1974 paper, and references to other work; no result was inferred from an unopened body. Searches for total asphericity again returned the distinct test-category diagonal notion, which is not used here.
