# Parts C and D work record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. No priority claim. Proof labels are in sections/C.tex and sections/D.tex.

## Established conclusions

**C.1–C.7.** Lead 2 is correct in full generality and at all path lengths. The outgoing Tor quotient has denominator the basis elements γv with vu=1; the incoming quotient has denominator γv. Nonempty target types contribute zero because the two composite supports are disjoint and endpoint values are constant on each composition fiber. This is a proof for the full path category, independent of truncation checks.

Strict = total for every localizer asked. For W_infinity, W_Z and W_n with n≥2, they hold exactly for a connected thin groupoid Y. For W0 and W1 they hold exactly when BY is 1-connected and 2-connected, respectively. Ordinary asphericity requires BY (n+1)-connected for W_n and BY weakly contractible for W_Z or W_infinity. The slice-to-fixed-endpoint comparison is given by appending β and by an intermediate functor appending an identity; this avoids an invalid type map when the old last sign is negative. INDLOCAL C.7 then identifies the slice with the corresponding path space.

The low-localizer argument uses the ordinary finality of the canonical left-Kan-extension element functor and the induced π0 bijection and π1 surjection. REVLOC H.4 and H5.6–H5.8 are explicitly checked in C.tex; the latter is not substituted for strict asphericity.

**D.1–D.5.** Lead 3 is correct: H_(k+1)(B int M)=T_k(M_ab) over total A, π1 is the canonical group colimit, and exact A gives a K(Γ,1) homotopy colimit for any free-monoid or free-group diagram. Universal covers of graph fibers, not injectivity of transition maps, are used. The interval example has monoid presentation <x,y,z | xy=x,y²=y,yz=z>, group completion F(x,z), and H2=0. The convergent rewrite/critical-confluence computation was checked integrally.

The C_delta functor in the prompt is a valid diagram of finitely generated free groups with actual free-factor inclusions. Absolute/relative private-vertex counting proves this; abelianization is Q, T1Q=Z, group colimit is F(u,v), and H2 of the Grothendieck construction is Z. Thus it gives the free-group counterexample expressly allowed in Part D.4. The earlier K* and finite parallel-pair examples do not contradict the exact-index theorem.

**D.6–D.7, decisive additional theorem.** Every nonempty connected exact A passes every FreeMon diagram, with arbitrary word substitutions. For C=colimMon M, the comma */q is int_A D, where D(a) is the translation category of M(a) acting on C. Its objects are literally C for every a, and its transitions fix them. Each D(a) is free on a graph, so H_q=0 for q≥2. Its strict categorical colimit is the regular translation category C//C, which has initial object 1. Since BA is simply connected, one can eliminate the transport copies of ΠA at each fixed c; this proves Π(int D) equivalent to Π(colim D), hence simple connectivity of the comma. Exactness and the homology spectral sequence kill all higher homology. Hurewicz makes the comma contractible, and Quillen A proves q a weak equivalence. Root and the tower thread independently scrutinized the two presentation arguments; the latter wrote notes/D_exact_audit.md.

Consequently **Part D.1 is refuted** by the known exact, nonfiltered category Delta_inj, uniformly over all diagrams. **Part D.3 is true**. The same statement holds for every exact colored-word category W_m. In particular the interval example passes in all degrees, not only degree two.

## Computations performed independently

- code/CD_finite_checks.py: constructs R0 as actual finite-set functions, enumerates paths through length two (25 objects, 585 arrows), verifies all composable path-arrow pairs, both quotient actions, tensor-kernel images exactly Z.e, and the restricted-action integral H1=Z with no torsion. The two action categories have 34 objects and 803/819 arrows. Computes the interval-monoid critical confluences, cocone on all injections through [5], and primitive integral homology matrices.
- code/CD_freefactor_checks.py: checks C.9 Nielsen inverses and its exact primitive H2 kernel Z.(2,-1), group-colimit elimination, and all 39,364 reduced words through length nine for the subgroup-intersection test. Enumerates all 172 positive ordered hypergraphs through five vertices, their 775 closed embeddings, and all actual-edge families; 496 relative families all have a new private vertex. Relation matrices have full row rank. The program uses no supplied program imports.
- Outputs are in code/outputs/CD_finite_checks.out and CD_freefactor_checks.out. Bounded checks supplement the general proofs and are not used to extrapolate them.

## Discarded approaches and remaining extra issue

Before D.6, we tried to realize a five-element rectangular-band monoid (classifying space S²) by interval/circular subdivision diagrams over Delta_inj. Ordinary interval subdivision gives the absorption presentation above; circular subdivision gives further idempotent absorption, not a sphere. The new theorem proves that no nonaspherical target can arise from an exact-index diagram of free monoids, so continuing that counterexample search would be futile.

The C_delta group presentation does not automatically supply free monoids: forgetting a group leaves nontrivial units, and free-factor inclusions do not select compatible positive bases. A single relator has positive realizations (for example u2=a u1 and v1=a v3, or v1=u2 t and v3=u1 t). Across overlapping hyperedges these impose common-prefix/suffix constraints; no functorial simultaneous positive basis has been established. A closed one-edge copy meets another closed subobject in at most one vertex, which may help a future positive-refinement argument, but this observation alone is not a proof. We make no assertion that C_delta passes or fails all FreeMon tests. This additional classification is separate from the counterexample settling D.1 and from the free-group alternative settling D.4.

The exact-index proof cannot be extended to merely total A by dropping exactness: the comma spectral sequence may then contain T_p H_1(D(a)), p>0. Totality kills the derived colimits of permutation modules, not arbitrary H1 modules. Similarly, transporting the vanishing from the source to BC before proving the comparison would be circular. These gaps are explicitly avoided in D.6.
