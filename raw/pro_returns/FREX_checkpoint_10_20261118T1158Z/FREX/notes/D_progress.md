# Part D research ledger

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), subagent predimension. No priority claim.

## Current results

All requested classification parameters are settled by the proofs in sections/D.tex:

- Every ordered C(k,a,b) is total and has (St), (Op).
- If b < (k−1)a, it is not exact over any nonzero ring and its group is non-amenable.
- If b ≥ (k−1)a, it is Ramsey, exact over every ring, with extremely amenable group.
- The unordered Cδ is not exact over any nonzero ring: the 18-point rigid atom constructed from the cubic asymmetric graph gives a second obstruction, despite averaging equalizing the original 3-point hyperedge.
- There is no co-precompact extremely amenable subgroup in the low range; orientation expansions are not precompact over the original limit merely because finite objects have finitely many orientation lifts.
- FE-4: first two clauses true, last clause false. E^2_{1,0} in the proposed Kan spectral sequence survives and must be zero, hence cannot be T1(Q_R)=R.

## Important construction

A finite atom W with a < δ(W) ≤ a|W|/2 and every ≥2-point proper subset of predimension ≥δ(W) exists throughout b<(k−1)a. Explicit cases are cycles, truncated complete hypergraphs, and core/petal hypergraphs. Only its singletons are proper nonempty d-closed subsets. Distinct closed copies meet in at most one point; positivity forces a private vertex among every finite family. This supplies the entire low-range obstruction, including C(2,2,1) and C(3,3,1). Root independently checked the four-case construction.

## Computations

code/D_certificates.py uses only Python standard library, output in code/D_certificates.out. It checked 359 parameter triples with atom size at most 18; 46 larger cases were not enumerated (the proof covers them). It checked the five-edge signed marginal identity and boundary examples. It enumerated every nontrivial cut and every graph automorphism of the explicit cubic 12-vertex graph, and all 262143 nonempty subsets of its 18-vertex ternary atom. It also verifies the eight-base-vertex finite counterexample to the source's shadow-sparsity remark.

## Sources opened and searched

- Supplied predimension_category.tex, predimension_stabilizers.tex, predimension_totality_reduction.tex read in full where used; parameter-dependent estimates independently re-derived.
- Supplied ordered_graphs.tex: full Ramsey-to-integral-equalizer proof read and rechecked.
- EHN arXiv 1705.02379 supplied LaTeX and v3 PDF opened. Theorem 1.3 applies to one unary set-valued function F:A→P(A), with no uniform image bound, so the critical line b=(k−1)a is covered.
- EHN arXiv 1801.01165 supplied LaTeX and v5 PDF opened. Exact numbers: strong-class KPT Theorem 2.13, nonamenability Theorem 3.8, no precompact subgroup argument Theorem 3.16(1), functional Ramsey expansion Theorem 6.7, maximal subgroups Theorem 6.9, functional amenability Theorem 6.10. Remark 3.2 is false as stated; a direct finite counterexample is supplied.
- Web queries: “Hrushovski predimension minimal pair rational coefficient hypergraphs essential minimal pair existence”; “Hrushovski predimension strictly balanced hypergraph delta rational minimal pair”; “exact colimits predimension Fraisse”; “Hrushovski predimension category affine equalizer rational exactness”; EHN exact theorem-number searches. No equivalent all-parameter exactness classification was identified in these searches. This is a search report, not a novelty claim.

## Corrections and boundaries

- Lead 8(a) through (d) are true; 8(e)'s five-edge identity and its positivity/closedness assertions are true, but its proposed exact low-density candidate categories fail exactness by a different finite atom.
- Source EHN Remark 3.2 is false for sparse relations; its graph Theorem 3.8 remains valid. The hypergraph assignment proof avoids the incorrect inference.
- No correction to the read steps of TOTAL_EXACT_2 A.21, A.24, A.30–A.34, or A.6 was needed.
- The exact threshold for equalizing only the original three singleton arrows in all ternary parameters is not required by the Part D classification: the category is nonexact throughout b<2a. Lead 8(e)'s statement that a threshold exists follows from monotonicity in b/a. No numerical value for that additional threshold is claimed.
