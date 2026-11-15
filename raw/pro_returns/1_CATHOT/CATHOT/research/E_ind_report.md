# Audit of the remaining local ind-presentation implication

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim is made.

## Exact manuscript passage

The original transcription `background/grothendieck/DER_III-V/DER_III-V_text.tex` was read from the argument immediately preceding manuscript page 44 through the paragraph on manuscript page 46. At page 44 the asserted envelope comparison is said to be an ind-isomorphism exactly when its associated functor inverts weak equivalences. At page 46 the manuscript restates this as existence of a sequence of Thomason–Kan categories representing the same presheaf. The subsequent assertions about making transition maps full inclusions, the locality of the union, and the uniqueness or weak equivalence of union maps are logically separate.

The smallest original claim is sequential. The more general version for a U-small filtered diagram is recorded separately. The term “local” is interpreted consistently with C.3, hence equivalently as isomorphism in Cathot to a groupoid; it is not silently replaced by Thomason fibrancy.

## Results

The implication from W-infinity invariance to a local ind-presentation was neither proved nor refuted in this audit. E.17 explicitly marks both the sequential and general U-small filtered versions Open. This records the limit of the audit, not a claim that the problem is unknown throughout the literature.

There is an exact proved criterion, supplied by the actual reflection Pi1:Cathot→Gpd and the formal A.4 theorem. A small ind-object has a presentation by local categories if and only if its associated presheaf inverts every unit X→Pi1X, if and only if its canonical ind-unit is invertible. Equivalently the presheaf inverts W1. When this occurs, applying Pi1 to the original diagram provides the required presentation on the same index, so no additional sequential cofinality or strictification assertion is needed.

The precise unproved implication is W-infinity invariance ⇒ invariance under all X→Pi1X. These units need not be weak homotopy equivalences. A.7 proves descent to the presheaf colim_i[-,BK_i] on Hot; it does not identify that varying-target presheaf with a single representable. D.8 excludes a small presentation when the descended presheaf is represented by a non-1-type; applying it separately to a stage would be invalid.

Two positive special cases are proved. If a cofinal subdiagram has all BK_i of 1-type, A.7 and objectwise groupoid comparison prove invertibility of the ind-unit. If the descended presheaf is representable, D.8 forces its representing space to be a 1-type and the ind-object is essentially constant with a groupoid representative.

The U-small index restriction is indispensable for any possible positive theorem. D.7 constructs a V-small, cardinal-unbounded ind-presentation of maps into K(Z/2,2). It cannot have a groupoid ind-presentation, as the canonical map induced by S²→e distinguishes it from every colimit of groupoid representables. This refutes only the enlarged-index variant. E.4's groupoid-like full filtration is likewise not a counterexample to the local-presentation existence question: its stages already satisfy that conclusion, although its union has the asserted failures.

## Searches and limits

The existing proofs in A, B/C, D, and E were reread. Primary-source searches investigated whether a cardinal-controlled relative Kan–Thurston construction with kernels admitting no small quotients could force the missing unit invariance. Search terms included “simple group plus construction every,” “Kan-Thurston simple groups homology,” “simple groups prescribed homology,” “Kan-Thurston no nontrivial quotient,” and “simple group homology of space.” No verified primary theorem establishing the required strengthening was found in this run. Secondary discussions were treated only as leads and are not cited as authority for a mathematical assertion here. Ordinary Kan–Thurston or acyclic-envelope theorems were not strengthened without proof.

No additional higher-homotopy-killing assertion is used in E.17. Such information alone would not establish factorization through a 1-type; in particular a nonzero class CP²→K(Z,4) induces zero on every higher homotopy group but does not factor through the point.

## Independent F.12–F.13 check

The current F.12 and F.13 were read again line by line. No cross-reference or mathematical defect was found. The finite-subgroup filtered-colimit formula uses finite generation of component fundamental groups and finitely many components. Truncation of section spaces is invoked only over mapping spaces into BG, which are 1-types. The zero section fixes its fibre-component under base mapping-space monodromy, justifying the distinction of unpointed classes. The module syzygy and d/n cardinal indices are consistent. The nonsplit fibration has no homotopy section, and the 1-type-target mapping comparison proves that its non-realizable transformation remains non-realizable after restriction to finite CW tests. F.13's translations and associator comparison use only fibre products over this same 1-type base; T²pr1 and Tpr1 are correctly typed and distinguished using T inverse.

No computations or new programs were needed for this formal audit. No root A/D/E source file was edited; `sections/E_ind.tex` is supplied for insertion after the existing E.16 material.
