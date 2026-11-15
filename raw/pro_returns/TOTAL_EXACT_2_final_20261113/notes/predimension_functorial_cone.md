# The functorial path cone: full contraction for the two natural point actions

Status: proved. The binary and triple point-quotient categories of elements are contractible, for both the full ordered positive-predimension category and its full point-and-edge-closed subcategory. This historical note records the specific-action contraction. Its remaining totality question has subsequently been resolved by the independently audited finite-support and all-action arguments; the cone proof alone does not imply that general result.

The formal statements and complete proofs are in `sections/predimension_functorial_cone.tex`, labels A:predimension-cone-functor and A:predimension-cone-contracts.

## The functor

For every raw vertex x of X, add a tagged loose path of length three from x to one new centre c_X. The path has two internal binary vertices r_x,s_x and three private third points a_x,b_x,d_x. Order all old points first; then the two-point blocks r_x<s_x in old x-order; then the centre; then the three-point blocks a_x<b_x<d_x in old x-order. Define F(f) by applying f to each old point and each path index and by sending centre to centre.

The tagged formulas are strictly functorial and increasing. The relative delta calculation for a length-three path proves X≤dF(X). For f:X→Y, the intermediate subobject Y∪_X F(X) is a free amalgam, so F(X)≤dY∪_XF(X). The remaining paths, for vertices of Y outside f(X), are positive relative extensions. This proves F(f) d-closed.

There are natural transformations id_A→F (the old inclusion) and const_V→F (the centre). The centre is a d-closed point: first adjoin it disjointly, then add the paths.

For an actual V-arrow x, its point is d-closed in X. Its complete path Q_x is d-closed in F(X): first form the free amalgam of X and Q_x over the closed point x, then adjoin all other paths. Every point and edge in a loose path is d-closed. Thus the path is made of actual W-arrows, even in the full category where other raw vertices might fail to be closed.

If X has all atoms d-closed, this argument applies to every raw x and proves that F(X) does too.

## Contraction

The natural transformations id_A→F←const_V already contract BA. Let H be the binary point quotient, the triple point quotient, or any pointwise quotient of the binary point quotient. For every h∈H(X), the image under the old inclusion X→F(X) is the centre class h_X, because h has an actual point representative and its length-three binary path identifies it with the centre.

Consequently J:X↦(F(X),h_X) is a functor A→El_AH. If p:El_AH→A is projection, the old inclusions give a natural transformation id_El→Jp. The identity of BEl_AH thus factors up to homotopy through the contractible space BA. The element category is nonempty, so it is contractible.

For binary K=ker(Z[A(W,−)]→Z[A(V,−)]), two projective dimension shifts give T_i(K)=H_(i+2)(El_AH_binary)=0 for all i>0. Alternatively e↦e+P_(ev2)−P_(ev1) is a natural map Z[A(W,−)]→F*K; on K it equals K→F*K, so the natural-transformation homotopy and projectivity imply the same derived-colimit vanishing.

This establishes all degrees for these specific actions and explains why the selected AKR binary obstruction disappears in the full category. It does not affect the nonzero T_1 of the simultaneous triple **column** cokernel. The triple point quotient is a different, row-type object; no row/column identification is being used.

## Historical all-action question

The plausible next route is support analysis for arbitrary finitely presented connected A-sets. Each is a quotient of finitely many representables; relations between two embeddings of P can retain their common fixed d-closed substructure. The point cone contracts the special case where the relevant support is empty. A representable itself has its tautological support and an initial element category. Neither observation establishes a functorial reduction of every relation pattern to a single minimal support.

Any use of weak elimination of imaginaries or free-amalgamation model theory had to prove the needed comparison for all A-sets and the relevant element categories. An invariant-subset or orbit description by itself was not a homotopy-equivalence theorem. The subsequent proof supplies an elementary alternating-amalgam support theorem and proves both required comparisons directly; it does not import a weak-elimination theorem.
