## Exact remaining questions and attempted approaches

### A.3(iii): amenability and rational exactness

The unresolved assertion is the full quantified statement from the prompt: in setting (S), assume (Rig), (FA), (FA-empty), and (Op), and assume that the topological automorphism group is amenable. Must its smooth rational coinvariant functor, equivalently the category colimit functor over Q, be exact? We have neither a proof nor a counterexample satisfying all these hypotheses.

A.23 proves the assertion when the universal minimal flow is metrizable. A.30 proves that a counterexample must contain a finite affine-relation map whose cyclic image has unit quotient filling norm on a sequence converging to zero in the ambient l1 norm. The missing step is a boundedness or closed-range statement for that particular image; an arbitrary invariant algebraic functional is not automatically bounded or positive.

| Approach | What was established | Exact remaining issue or reason for exclusion |
|---|---|---|
| Sparse predimension examples | The complete parameter dichotomy in D separates the low and high ranges. | The low range is nonamenable and nonexact over every nonzero ring; the high range is Ramsey and integrally exact. Neither range refutes the rational implication. |
| Independently ordered posets | Integer Euler-characteristic weights give exactness over every ring; a finite probability obstruction gives nonamenability. | This refutes the reverse implication, not the unresolved amenability-to-Q implication. |
| Independently ordered binary vector spaces | Totality, all named structural hypotheses, amenability, and failure over F2 were proved. A.31--A.33 then prove Q-exactness by an exact auxiliary basis category and a finite simplex-code average. | This is a separator for integral exactness, not a counterexample to A.3(iii). |
| Averaging on a precompact Ramsey expansion | The natural signed-averaging section is proved; positive real averaging plus scalar descent gives the conditional rational theorem. | An arbitrary amenable group in the question need not be known to have such an expansion. |
| Smooth duality, finite length, and representation theorems | The precise scopes of Evans, Yang--Bojanczyk--Klin, Rovinsky, Li, Harman--Snowden, and the locally compact filling-norm results were checked. | Their additional Ramsey, approximation, transitivity, measure-algebra, or compact-open assumptions cannot be dropped. Finite length alone does not make the relevant algebraic functional bounded. |
| Exact open subgroups and a Cech complex | The terms can be expressed using coinvariants for intersections of open subgroups. | The coefficient maps form a nonconstant cosheaf; totality of the underlying orbit complex does not establish exactness of that coefficient complex. No local-to-global theorem was proved. |
| Probability Boolean algebras and rational linear constructions | Several possible constructions and natural-order averages were examined and scoped in the notes. | The necessary Ramsey/amenability/strong-support hypotheses are not all established. Infinite rational-span imaginaries obstruct the naive finite-support bridge. These are not counterexamples. |

There is no certified smallest finite counterexample: this is an all-target exactness question. The remaining class must lie outside the proved metrizable-flow case and must exhibit the specific distortion above. The next substantive step would be to prove the required undistortion under the stated hypotheses, or to construct one total amenable action with a genuinely unbounded invariant affine-relation functional.

### C.4 under totality: all prime fields versus Q

The general implication is false: A_2(Q) is exact over every Fp and not over Q. The unresolved restriction asks whether this can happen for a total category, with or without finite hom-sets. No such total counterexample is produced here.

A counterexample cannot have a weakly terminal object. Its persistent obstruction must involve a genuine finite family beyond the integral pair equalizers supplied by totality. The familywise saturation criterion C.15 shows that its torsion defect cannot have bounded exponent; the integral Noetherian hypotheses stated there are sufficient but are not assumed in general.

| Approach | Established outcome |
|---|---|
| Finite and divisible cocycle coefficients | The full field profile is proved. The all-prime/rational separator remains nontotal. |
| Changing the strong presentation or adding fixed points | Totality is a topological-group invariant. A fixed-point cone does not remove the action on the old cosieve. Dense-image and ordinary-final projections also prevent the proposed repairs. |
| Primitive expansions and contractible Kan targets | A contractible Kan simplex category is Ramsey. A nonsplit acyclic chain complex alone therefore does not give a nonexact index. |
| Increasing-degree and arbitrary filtered Kan totalizations | C.22--C.25 prove integral exactness whenever the resulting base is weakly contractible. The rational-vector version also covers rationally acyclic filtered bases. |
| Grothendieck assemblies over an exact base | C.26--C.27 exclude the coefficient-pushforward construction and then arbitrary connected Kan simplex fibers with arbitrary transition functors: totality forces integral exactness. |
| Ordinary category ultraproducts | C.28 gives fixed three-arrow obstructions in all degrees. C.29 proves unbounded support requirements for shift-window equalizers, so the ordinary ultraproducts, and the specified retained-family subcategories, fail exactness and totality. |
| Finite ordered coproduct completion | Rejected because joint tuples, not merely component marginals, determine embeddings; condition I already fails. |
| Exceptional finite matrices inside C_delta | C.30 verifies a target with a normalized F2 witness and no rational witness there. A complete bridge argument supplies a later integral witness, so the local effect does not persist. |
| Fixed finite edge-voltage covers | C.31 supplies one nine-vertex obstruction with compatible strong sections into every such cover and every composition. Every filtered sequence of these covers remains nonexact over every nonzero ring. |
| More general characteristic-selective endofunctors | No construction was obtained. A different gadget would need to preserve a rational obstruction while killing every modular finite family; a transfer with augmentation p alone proves neither requirement. |

The next substantive step would be a totality theorem controlling the unbounded torsion saturation, or a construction outside these excluded families together with all-family modular witnesses and a persistent rational obstruction. The known nontotal example is not relabelled as a total one.

### G.1--G.2: free monoids

The specified gap diagram and all lexicographic embedding-gap diagrams pass. Uniformly bounded ranks and positive invariant length are also settled in the stated scopes. The still undecided C_delta case can be restricted to finite-rank free monoids at each object, injective transitions, unbounded rank overall, and a smooth locally free saturation monoid. Neither a global counterexample nor universal passage has been proved.

For the Abelianized derived-colimit question, G.30--G.33 supply the strongest universal reduction: if X is the orbit nerve of the locally free monoid and Y the quotient of its canonical cut tree, then H2(X) is exactly the kernel of the displayed transgression from H2(Y) to the sum of the locally cyclic cut stabilizers; for degrees at least three the homology of X and Y agrees. G.40--G.41 permit all smooth bounded cuts without changing this model. G.42 proves that finitely many vertex orbits have a contractible finite-orbit hull closed under rooted meets and canonical path turns; G.43 constrains monotone cuts to a common initial signed flag. Neither result supplies the stabilizer coherence needed to replace the universal homology test by a smaller proved criterion. The injectivity of the transgression and the required higher vanishing remain unproved. The monoid comparison has the additional ordinary-colimit and product-coherence issue.

| Approach | Established outcome and limitation |
|---|---|
| Original DF group relator with positive factors | G.19--G.20 exclude every global positive realization, including arbitrary rectangle factorizations. The explicitly checked finite rectangles do not extend by that argument. |
| Twisted four-factor relator | A complete finite V,W,X11 realization exists, with exact ranks, incidence relations, and the required factor chains. G.23--G.24 force identical signed lexicographic flags in any nonconstant global realization. The surviving same-flag case has no global construction or exclusion. |
| An eight-word stabilization | The recorded specific buffered cycle is excluded by the same global chain/sign argument. Arbitrary cancellation patterns are not covered by that exclusion. |
| Direct natural-order fiber word lift | A finite crossing-partition certificate rules out the indicated basis-specific lift. It is not a theorem forbidding every possible change of basis or enlargement. |
| Positive integral matrices | G.38 realizes nonzero rational derived colimit with strictly positive transition matrices. This does not give a functor to free monoids; ordered substitutions must satisfy the actual word compositions. |
| Free-group or bifix amalgamation | G.39 gives a counterexample even with group-isomorphism maps and identical positive abelian cones. Positive-saturation variants were tested separately; no applicable general amalgamation theorem was obtained. |
| Fixed groups and affine stabilizers | G.27 disproves both naive fixed-group-completion shortcuts. G.28 proves central splitting, while G.29 disproves the stronger bounded-cut conjugacy shortcut. |
| Vanishing of quotient-tree H2 or injection of cut groups | G.34 refutes both shortcuts by an explicit finite-rank diagram for which all positive Abelian derived colimits vanish but H2(Y) and the transgression are nonzero. |
| Finite support cells and graphification | G.35--G.36 describe comparisons by raw order and equality. G.42 removes the suspected support blowup for canonical rooted meets: each meet is supported by one input, and finitely many vertex orbits have a finite-orbit turn/meet hull. This does not imply finitely many tuple orbits or control arbitrary products. |
| Finite tree templates | G.42 encloses strict finite direct diagrams of translations in contractible finite-orbit hulls over one open subgroup. G.43 classifies monotone cuts between two support lex chains. Quotient-face representatives may commute only up to stabilizer elements; no strictification, simultaneous branching template, or product-compatible exact cover has been proved. |
| Nonsimplicial tree and monad results | The exact hypotheses were checked. Tree existence and locally cyclic stabilizers do not by themselves supply an equivariant edge complex; the classifier or relative-coherence hypothesis remains additional. |

The next substantive step would be an actual filling theorem for the remaining quotient-tree kernel, or a globally compatible free-monoid realization in the surviving twisted case. A proof for the Abelianized row alone would still need to be connected to the ordinary monoid comparison. The broader class F is group invariant in setting (S), inherits the proved action/final-functor operations, and lies between exact and total categories; which inclusions are strict remains undecided here.

### F.1: remaining source access

The original bodies of Isbell's 1974 *Exact colimits. I* and McDuff's 1979 *On the classifying spaces of discrete monoids* were not recovered. Official metadata, the cited bibliography records, and the reproduced McDuff abstract were opened; they are not recorded as proof checks. Oberst's original 1968 article was recovered and checked at the used theorem numbers. No mathematical argument in the manuscript relies on an unchecked claim from either missing body. Completing this part requires the original body or an authorized complete primary copy, not another secondary citation.
