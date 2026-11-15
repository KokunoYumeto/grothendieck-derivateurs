# Algebraic audit: Leads 1–5

Status at this checkpoint: every formal claim in Leads 1–5 is proved in `sections/algebra_leads.tex`; the main implication and the triple assertion are not settled by these calculations.

## Statements and sources read

- TOTEX A.1–A.4, B.1–B.4, with the actual normalized-bar/nerve map, the two exact sequences defining row homology, and the distinction between row kernel and intersection kernel.
- TOTASPH C.3–C.6 and C.11–C.13, in the supplied TeX: inherited actions, cyclic covers, the permutation-module comparison, and the common-successor argument.
- Isbell–Mitchell (1976), supplied PDF, text extracted into `sources/IsbellMitchell1976.txt`: §2, Lemma 2.2, Proposition 2.3; §3, Theorem 3.1, Lemma 3.2, Proposition 3.3 and the coefficient remark; §4, Theorem 4.1 and Corollaries 4.2–4.6.
- `HUNCHES.md`, H1: κ is now used explicitly, and the precise obstruction to its disappearance inside the binary cycle subfunctor is proved.

The relied-on statements are re-derived in the proof paragraphs of the LaTeX section; the source readings are not used as blanket authority.

## Completed formal proofs

1. **Lead 1:** the prior surjection is the canonical isomorphism. The proof identifies `colim(K1+K2)` as `Z² / ε(L)(1,−1)` and takes the kernel of addition. The second proposed proof is also correct; its explicit map is `t ↦ [(tz1,0)]`, and the inverse calculation has the required minus sign.
2. **Lead 2:** the one-relator criterion is correct for every category satisfying I, even without connectedness. The Tor formula requires the already stated hypothesis `aug z = 0` and otherwise uses no hypothesis on A. It is derived from two short exact sequences; common successors convert an augmentation image into an equalizer at one object. Empty A is handled explicitly.
3. **Lead 3:** all displayed formulas and the one-relation presentation are correct. The case `k=0` is included. The equality of the row and column cokernels for `k=1` does not extend to larger `k`.
4. **Lead 4:** both affine-equalization assertions are correct. The last phrase about finite products is explanatory, not a new equivalence. Exactness is not equivalent to injectivity of the set-to-abelian comparison or to siftedness. An explicit `Δ_inj` example shows a nontrivial fibre even for an exact category.
5. **Lead 5(ii):** proved in a stronger form with common successors in place of I. Quotient each F(y) by all incoming parallel-arrow differences; the quotient factors through the directed reachability preorder. The filtered-colimit criterion for a zero element yields the asserted finite normal form.
6. **Lead 5(i), (iii), (iv):** correct. κ has zero augmentation vector, hence zero colimit class by the row calculation. An affine annihilator gives the triple equalizer. The map ψ has kernel `(ℓ,−ℓ,ℓ)` and cokernel with `T1 = Z/ε(L)`.
7. **Lead 5 graph and final interpretation:** the integral cycle-group identification is explicit and natural even under noninjective maps. If a triple lacks an affine equalizer, `[κ]` is nonzero already in `colim im ψ`; hence no killing normal form may use only coefficients in `im ψ`, or have jointly affinely equalizable arrow pairs. A “1-cycle of A” must mean a coefficient bar cycle; ordinary `H1(BA)` vanishes for a total category.

## Main-question investigations recorded so far

### P1: augmentation ideals and the resolving class

**Definite obstruction, completely settled:** universal membership of the column module Q_a in the specified resolving class is false, even for a finite filtered category. Every object of that class is objectwise torsion-free. The four-object category in `sections/algebra_p1_obstruction.tex` is filtered because it has a terminal object, but its triple-column module at one old object has cokernel `Z²⊕Z/3`. The category, every composition, associativity, terminal object, all-action totality and the Smith-form certificate are given completely. The finite check in `code/algebra_column_torsion.py` verifies 52 composable pairs and 121 associativity triples. This does not affect P1's alternative of using a different module with the same T1; in this filtered example T1 is zero.

For an arbitrary abelian diagram M, let `R(M)=Z[UM]` be its pointwise group ring and `I(M)=ker(R(M)→Z)`. Totality makes `R(M)` and the constant permutation module acyclic; hence I(M) is acyclic. Tensor powers of I(M) are likewise acyclic, by successively tensoring the split augmentation sequence with permutation modules and using kernels of epimorphisms. Pointwise one has `I(M)/I(M)^2 ≅ M`.

**Exact obstruction:** from `0→I(M)^2→I(M)→M→0`, the needed `T1(M)` is `ker(colim I(M)^2→colim I(M))`. Acyclicity of I(M), its tensor powers, and its generators does not show this map injective. Resolving I(M)^2 by products gives the bar complex and restates the derived-colimit problem; it does not make I(M)^2 a permitted kernel with known acyclic quotient. Rational logarithms only exist after completion, an inverse-limit operation not justified by the resolving-class closure. No flatness conclusion is claimed.

### P2: `z=2c0−c1−c2`

For `z_i=c_i−c_0`, totality supplies the row syzygies and the independent augmentation-one annihilators of each z_i. A common coefficient for the equation `t(z1+z2)=0` is not produced by those row syzygies: they allow separate coefficients t1,t2. Treating `(2c0,c1+c2)` as an ordinary pair in a symmetric-power action fails because their two elements need not be in the same action component; already `Δ_inj` separates diagonal and off-diagonal configurations. Quotienting an action to force connectedness imposes exactly the relation being tested and does not return an annihilator upstairs.

**Current smallest undecided instance:** an affine annihilator for `2c0−c1−c2` in a general total category. No claim that failure to prove this special case refutes it.

### P3: κ normal forms

The strengthened normal form completely explains the passage from homological zero to a finite sum of parallel-arrow differences. The missing step is simultaneous affine equalization of those differences, with coefficients in the full row-cycle module K. IV handles one term. If all terms use the binary-cycle submodule I, they would kill `[κ]` in `colim I`; this is impossible whenever `ε(L)≠Z`. This supplies a rigorous necessary obstruction, not a proof that every possible normal form has one of those two special forms.

### P5: free resolutions, stabilization, and delooping

The square between free abelian simplicial diagrams and underlying simplicial-set colimits commutes. Totality proves homotopicality on free abelian diagrams. A cotriple resolution of an abelian diagram has a contraction after forgetting addition; applying abelian colimit does not preserve that contraction because the extra degeneracy is not additive. Stabilizing levelwise colimits of Eilenberg–Mac Lane spaces can retain positive stable homotopy: those groups are the very Tor groups at issue. Neither argument closes the gap.

### Cayley graph / relation module (parent's suggested variation of P1)

For `P=Z[H]`, `Q=P/K`, form the Cayley graph with vertices Q and labelled edges `(q,h):q→q+[h]`. Its integral cycle module C is the kernel of a morphism between permutation modules, with constant connected-component module; consequently totality makes C colimit-acyclic. Exponent counting gives a natural epimorphism `C→K`. Its kernel consists of commutator relations; this is the abelianized relation module of the free group on H mapping onto Q.

For `K=J=P_r z`, a fixed word spelling z gives a natural lift `P_r→C`, but proving that this lift vanishes on `ann(z)` is an additional identity. The word `2c0−c1−c2` runs through the vertices `0,c0,2c0,c2,0`, and these intermediate configurations need not become one component under ordinary arrows. For a binomial there are only the two edges based at zero, which do come from the same representable component. Filling commutator squares identifies the kernel, but its colimit first homology is exactly `colim J=T1(P/J)`; its vanishing is the missing claim.

A translation-equivariant section cannot be assumed. For H={a,b}, Q=Z with a,b↦1, the graph-cycle module is `⊕_{n∈Z} Z(e_{a,n}−e_{b,n})`; its map to `K=Z(a−b)` sums coefficients. Translation shifts the basis, so there is no finite-support invariant element mapping to 1. This observation obstructs that proposed equivariant splitting, not every possible A-natural section.

## Literature searches for these routes

The web searches used the exact queries:

- `"exact colimits" "homology"`
- `"permutation modules" "flat" "category" colimits`
- `"quasi-filtered" "acyclic" category`
- `"homotopy" "exact colimits"`
- `"totalement asphérique" "exact"`
- `"colim" "permutation modules" flatness`
- `"homotopy colimits" "filtered" "Isbell"`
- `"exact colimits" Ramsey`
- `"affinization" Ramsey category`
- `"quasi-filtered" category homology`
- `"total asphericity" category exact`

No result obtained by this search supplied a theorem settling total⇒exact. The search found primary landing/PDF locations for Isbell (1968) and Isbell (1974); they were passed to the parent, not treated here as opened source bodies. Modern permutation-resolution results for finite groups were not applied to arbitrary categories or to the constant category module without a justified comparison.

Further queries were `"functors" "sets" "preserve weak equivalences" simplicial`, `"colimit" "simplicial sets" "exactness" Isbell Mitchell`, `"homotopical" "colimit functor" "abelian"`, and `"left adjoint" "simplicial" "additivization"`.

These located a primary source that was opened: L. Hubert (2026), *A homotopical Dold–Kan correspondence for Joyal's category Θ and other test categories*, arXiv:2602.09674v1, HTML at <https://arxiv.org/html/2602.09674v1>. §§3–5 were read, in particular Proposition 4.6 and Definition 5.1/Proposition 5.3. Proposition 4.6 gives homological cofinality for arbitrary abelian coefficients by comparing bounded-below complexes of projective presheaves after testing representables. It does not replace the potentially nonflat underived constant module in our problem. Its Example 5.4 uses “totally aspherical” for the diagonal/aspherical-product notion of test-category literature; that is not the present final-image definition. No result of that paper is invoked as deciding the main implication.

## Remaining work

The formal algebraic leads are complete. The general triple assertion and the one-relator annihilator problem remain exact missing implications. Continue with a permutation-module homology witness for the column cokernel, or with a proof that an arbitrary κ normal form can be simplified without assuming affine pair equalization.
