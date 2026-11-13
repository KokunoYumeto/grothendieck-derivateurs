# Finite fillings, compactness, and a disk ultraproduct obstruction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. No priority claim. This is a research note, not an added numbered result in the compiled paper. The disk construction and the conditional extension criteria below are proved. No total nonexact category is constructed here.

## 1. The logical distinction in Lead 6

For a fixed finite face poset D of a triangulated sphere and a functor u:D→A, Lead 6 tests whether the canonical map

    Bj_u : BD → B El_A(H_u),       H_u(a)=π_0(u↓a),

is null-homotopic. Any particular null-homotopy has a finite certificate: a finite subdivision and simplicial homotopy or ball filling, finitely many objects and arrows of A, and finitely many zigzags certifying the equalities of the relevant components of u↓a. The completeness of this description follows by the same finite simplicial approximation used in Lead 6, applied to a null-homotopy relative to its finite boundary. Each equality of two component classes is witnessed by a finite zigzag.

There is no bound in Lead 6 on the size of that certificate. Consequently its direct logical form is

    ∀u [Functor_D(u) ⇒ ⋁_{τ∈Cert(D)} ∃w E_τ(u,w)],

where Cert(D) is a countable set of finite certificate templates. For a fixed template τ, E_τ is a finite conjunction of typing and composition equations. The displayed countable disjunction is an L_{ω_1,ω} formula, not one first-order formula. We have not proved that an equivalent first-order formulation cannot exist; the point is that the supplied Lead 6 formulation does not give one automatically.

In particular, producing an n-total nonexact category for every finite n does not by itself justify a first-order compactness or ultraproduct argument. Even at a fixed dimension, certificate sizes can tend to infinity. Adding a sort of coded finite lists does not remove this issue unless actual standard finiteness is independently guaranteed: first-order compactness can produce nonstandard list lengths, which do not define finite simplicial chains or ordinary finite null-homotopies.

### The nonexactness side really is a first-order scheme

Use the usual two-sorted language of categories, with distinguished objects p,q and distinguished arrows a_0,a_1,a_2:p→q. For every standard finite integer tuple (c_1,…,c_m) with sum 1, require that no common-target arrows h_1,…,h_m:q→x satisfy

    Σ_j c_j h_j a_0 = Σ_j c_j h_j a_1 = Σ_j c_j h_j a_2

in the free abelian group on A(p,x). Each displayed equality is first-order expressible. For example, partition the 2m labeled terms of a difference into blocks whose signed coefficient sums are zero. There are finitely many such partitions. The equality holds exactly when at least one such partition has all composites within each block equal. Distinct blocks need not be required to have different values: merging zero-sum blocks still gives zero sums. This is a finite disjunction of finite conjunctions of ordinary arrow equalities.

Negating simultaneous equality gives a universal first-order sentence for that coefficient tuple. The collection over all tuples is exactly the assertion that the distinguished triple has no integral affine equalizer. Repeated h_j and negative coefficients cause no problem. This confirms the asymmetry: the obstruction is a first-order scheme, while the unbounded filling alternative is an infinitary disjunction.

## 2. An explicit ultraproduct of contractible finite posets with nonzero H_1

The following auxiliary example concerns classifying-space contractibility. It is not a sequence of total categories, and it is not a counterexample to totality implying exactness.

### 2.1 The disks and their fixed outer boundary

For each integer N≥0, let K_N have vertices

    v_{i,j}   (0≤i≤N, j∈Z/3),       c.

Its oriented triangles are, for 0≤i<N and j∈Z/3,

    A_{i,j} = [v_{i,j}, v_{i,j+1}, v_{i+1,j+1}],
    B_{i,j} = [v_{i,j}, v_{i+1,j+1}, v_{i+1,j}],

and, for j∈Z/3,

    T_j = [v_{N,j}, v_{N,j+1}, c].

Include every face of these triangles and no additional simplices. Realize the three vertices at each fixed i as concentric homothetic triangles, with decreasing positive radii, and realize c at their common center. Each annular trapezoid is divided along its displayed diagonal. Thus K_N is a triangulated closed disk, with N triangular annuli and a central triangular fan. Its outer boundary is the same three-edge cycle for every N:

    v_{0,0} → v_{0,1} → v_{0,2} → v_{0,0}.

The numbers of vertices, edges, and triangles of K_N are respectively

    3N+4,       9N+6,       6N+3.

Indeed, its edges consist of 3(N+1) ring edges, 3N radial edges, 3N annular diagonals, and 3 edges to c.

Let P_N be the poset of nonempty faces of K_N, ordered by inclusion. Its nerve is the barycentric subdivision Sd K_N. In particular BP_N is a disk and is contractible. The numbers of nondegenerate simplices of NP_N in dimensions 0,1,2 are

    18N+13,       54N+30,       36N+18.                    (1)

The first number counts all nonempty faces of K_N. The second counts the 2(9N+6) vertex-edge flags, 3(6N+3) vertex-triangle flags, and 3(6N+3) edge-triangle flags. The last counts the six maximal flags in each original triangle. There are no nondegenerate simplices of higher dimension.

Let D be the fixed face poset of the outer three-edge circle. Write

    x_j = {v_{0,j}},          e_j = {v_{0,j},v_{0,j+1}}.

The inclusions D→P_N give the six-edge integral 1-cycle

    z_N = Σ_{j∈Z/3} ( [x_j<e_j] − [x_{j+1}<e_j] ).       (2)

Its boundary is zero by telescoping. The domain D, the six terms, and their coefficients are independent of N.

### 2.2 The unique filling uses every barycentric triangle

For an oriented triangle t=[a_0,a_1,a_2] in the displayed list, define its barycentric subdivision chain by

    s(t) = Σ_{π∈S_3} sign(π)
           [ {a_{π(0)}} < {a_{π(0)},a_{π(1)}} < {a_0,a_1,a_2} ].

Let b_N be the sum of s(t) over all A_{i,j}, B_{i,j}, and T_j. This is an integral 2-chain with exactly 36N+18 distinct terms, every coefficient being +1 or −1. Directly applying the alternating face differential shows that subdivision commutes with boundary. In the original oriented triangle sum, each annular diagonal, radial edge, inner ring edge, and edge to c cancels with its other incident triangle. The remaining edges are the oriented outer boundary. Consequently

    ∂b_N = z_N.                                           (3)

We now prove uniqueness over Z, not merely minimality among positive fillings. The graph whose vertices are barycentric triangles and whose edges join triangles sharing an edge is connected. Within each original triangle, its six barycentric triangles form a connected cycle in that adjacency graph. Across each original interior edge the two subdivisions have adjacent triangles. The original triangle adjacency graph is connected: B_{i,j} is adjacent to A_{i,j}; for i>0, A_{i,j} is adjacent across its outer ring edge to B_{i−1,j}; and T_j is adjacent to B_{N−1,j} when N>0. At N=0 the three central fan triangles are mutually connected along edges to c.

Now let d be an integral 2-cycle. Give every barycentric triangle the coherent orientation inherited from the disk. At an interior edge the two incident triangle orientations are opposite, so the coefficient of that edge in ∂d forces their coefficients in d to agree. At an outer boundary edge only one triangle is incident, so its coefficient in d must be zero. Connectedness of the adjacency graph propagates zero to every triangle. Therefore

    ker(∂_2:C_2(NP_N;Z)→C_1(NP_N;Z)) = 0.               (4)

It follows from (3)–(4) that b_N is the only integral filling of z_N. Hence every filling has exactly 36N+18 nonzero 2-simplex coefficients and has ℓ^1 norm 36N+18. In particular, a bound on the boundary length gives no bound on the filling support in this family.

### 2.3 Transfer to a nonprincipal ultraproduct

Let U be a nonprincipal ultrafilter on the nonnegative integers and form the ordinary model-theoretic ultraproduct poset

    P = ∏_U P_N.

For sequences of faces f_N and g_N, the order relation is

    [f_N]≤[g_N]  ⇔  {N:f_N⊆g_N}∈U.

There are no strict chains of four objects, since there are none in any factor. A nondegenerate finite simplex of NP is represented, on a set in U, by nondegenerate simplices of the same dimension in NP_N. This follows directly from the finitely many order and inequality conditions defining the simplex. The fixed boundary objects x_j,e_j define a functor D→P and a 1-cycle z by formula (2).

Suppose z=∂b for an ordinary integral 2-chain

    b = Σ_{r=1}^m n_r σ_r

in NP, with standard finite m and integer coefficients n_r. Choose coordinate representatives for the finitely many vertices occurring in the σ_r. Each σ_r then gives a strict 2-simplex σ_{r,N} for N in a set in U. Intersect these finitely many sets.

The equality ∂b=z involves only the finitely many edge terms of these simplices and the six fixed boundary edges. For every pair of these terms, their equality or inequality in P is represented by a set in U. Intersect this further finite collection of sets. On the resulting set E∈U, the equality partition of all edge terms is identical to the equality partition in P. Their integer coefficients are the fixed standard integers n_r and ±1. Therefore, for every N∈E,

    ∂(Σ_{r=1}^m n_r σ_{r,N}) = z_N.

After combining any repeated simplices, the filling on the left has support at most m. But E also meets the cofinite set where 36N+18>m. This contradicts uniqueness and the support count established above. Hence z is not a boundary, and

    H_1(BP;Z) ≠ 0.                                       (5)

The image of D lies in one component of BP, so one connected component already has nonzero H_1. Each BP_N is contractible. The proof uses only finite equality transfer and cofinite membership in U; it does not transfer an unbounded existential assertion about chains.

No P_N is being asserted to be total. In fact its face poset has a common face mapping to two distinct maximal triangles, which have no common upper bound, so it fails the Ore-square condition necessary for totality. The example therefore blocks a general compactness inference about unbounded filling witnesses without deciding whether totality itself is closed under any ultraproduct construction.

### 2.4 Exact program and certificate output

`code/finite_ultraproduct_disks.py` constructs precisely the displayed disks. It writes `code/finite_ultraproduct_disks_certificates.json`, then reloads and replays that file against freshly constructed integer boundary matrices. For N=0,1,2,3,8,32 it checks:

- the simplex counts in (1);
- the six-term cycle (2) and the exact integral boundary equality (3);
- one unit pivot for every 2-simplex, obtained by elementary free-edge collapses;
- a subsequent sequence of free-vertex collapses of the remaining graph to one vertex.

The free-edge replay proves injectivity of ∂_2 integrally for each checked instance. The complete collapse is a homotopy certificate, so the checks do not confuse acyclicity with contractibility. Together with (3), they certify the exact unique filling support and norm in each instance.

The results in `code/finite_ultraproduct_disks.out` are:

| N | Nerve vertices | Nerve edges | Nerve triangles = unique filling support | Rank ∂_1 | Rank ∂_2 |
|---:|---:|---:|---:|---:|---:|
| 0 | 13 | 30 | 18 | 12 | 18 |
| 1 | 31 | 84 | 54 | 30 | 54 |
| 2 | 49 | 138 | 90 | 48 | 90 |
| 3 | 67 | 192 | 126 | 66 | 126 |
| 8 | 157 | 462 | 306 | 156 | 306 |
| 32 | 589 | 1758 | 1170 | 588 | 1170 |

All boundary and collapse replays passed. The certificate file has 31,298 bytes and SHA-256

    72ab1f4618f0e5851896ff01d96c95f65ba7a06344d802ad39cd529cf30b9811

These are six exact finite checks of an explicitly prescribed family, not a finite-category search and not the proof of the all-N or ultraproduct assertions. Sections 2.1–2.3 give those proofs.

## 3. What would make a compactness argument valid

A sufficient strengthened hypothesis would choose, for every sphere face poset D, a finite collection of allowable certificate templates T_D, and establish finite satisfiability of the following first-order theory:

1. the category axioms, the distinguished triple, and, if desired, the assertion that p is weakly initial, ensuring connectedness;
2. the universal nonexistence-of-affine-equalizer scheme from §1;
3. for each D, the sentence

       ∀u [Functor_D(u) ⇒ ⋁_{τ∈T_D} ∃w E_τ(u,w)].

Now each disjunction is finite. First-order compactness gives a model of all the sentences. Every sphere task has a standard finite filling template, so Lead 6 makes that model total, and the universal scheme keeps the triple nonexact. This is a valid conditional argument. The unproved input is finite satisfiability for one globally coherent assignment D↦T_D. Choosing templates afresh for each finite fragment does not automatically provide that assignment.

Equivalently, a size-bound formulation would require a uniform standard bound on filling-certificate complexity for each fixed D throughout the relevant family of models. There are only finitely many combinatorial certificate types of bounded complexity for fixed D. Merely fixing the sphere dimension does not impose this stronger bound.

## 4. A directed extension principle avoids the uniformity issue

Here is a precise sufficient attachment principle. Let K be a class of countable categories with fixed p,q,a_0,a_1,a_2, containing an initial category A_0. Assume:

1. every category in K has p weakly initial and has no affine equalizer of the distinguished triple;
2. K is closed under countable increasing unions along category embeddings;
3. for every A∈K and every finite sphere task u:D→A, there is a countable extension A⊆B in K in which the induced j_u has a finite null-homotopy certificate.

Then a countable total nonexact category exists.

To prove this, enumerate all sphere tasks in A_0 and serve them successively using (3), taking the increasing union to obtain A_1. This is countable and belongs to K by (2). Repeat, serving all tasks in A_m to obtain A_{m+1}, and take A_∞=⋃_m A_m. Every finite sphere functor into A_∞ lands in some A_m and is filled in A_{m+1}. Under an inclusion i:A→B, the map

    π_0(u↓a) → π_0(iu↓i(a)),       [d,f] ↦ [d,i(f)],

induces the required functor of element categories and carries j_u to j_{iu}; hence a certificate remains a certificate at later stages. Lead 6 proves totality of A_∞. Any putative affine equalizer has finite support and therefore lies at some earlier stage, contradicting (1).

Universal private-incidence assertions are compatible with (2): any finite configuration in the union occurs at one stage, and embeddings preserve both equality and inequality. Thus the outstanding issue is exactly (3), a relative attachment lemma. This argument allows certificate sizes to vary arbitrarily between tasks. It does not need an ultraproduct or a uniform filling bound.

## 5. Why attaching strict cones overshoots the task

The most direct attachment does not preserve the AKR type of noncollision invariant. Fix parallel arrows a,b:p→q. Let D again be the face poset of a triangular circle, with vertices d_0,d_1,d_2 and edges e_{01},e_{12},e_{20}. Map d_0 to p and every other object to q. Send

    d_0→e_{01} to a,       d_0→e_{20} to b,

and all four other incidence arrows to 1_q. A strict cocone on this functor has one common component h:q→z at all its q-valued objects, because of the identity incidences. Its p-component must simultaneously be ha and hb. Thus the cocone forces

    ha = hb.

In the AKR setting, taking a=v_1 and b=v_2 contradicts the maintained injectivity of each W-arrow on its distinguished points. More generally, supplying strict cones for all these circle diagrams supplies ordinary equalizers for all parallel pairs. With common successors this is filteredness and implies exactness. Consequently a relative construction must fill the map in El_A(H_u) by a genuine finite homotopy pattern, rather than replace every task by a strict cocone in A.

This is a concrete obstruction to the simplest small-object attachment. It does not rule out more flexible sphere attachments preserving the private-incidence scheme.

## 6. Primary literature checked in this follow-up

No opened primary theorem here supplies the missing relative attachment lemma or detects exactness from all set-action homology. Three precise nearby results help delimit the route.

**Barthel–Schlank–Stapleton (2020).** The publisher body of *Chromatic homotopy theory is asymptotically algebraic* was opened. Definition 3.1 defines categorical ultraproducts by a filtered colimit of products. Remark 3.8 explains the fibrancy condition under which ordinary model-level ultraproducts compute homotopical ones. Lemma 3.9 applies this to quasicategories. Nerves of ordinary categories are quasicategories, but need not be Kan complexes; applying their groupoid completion is an additional operation. Thus these statements do not contradict §2 or make contractibility of each ordinary nerve pass to its ordinary ultraproduct. Proposition 3.7 explicitly assumes contractibility of the entire categorical product, not merely of its individual factors. Primary body: https://link.springer.com/article/10.1007/s00222-019-00943-9 . Web reader only; no local copy downloaded in this follow-up.

**Assadi (1990).** The primary MPI preprint *Permutation complexes and modular representation theory*, MPI/90-46, was opened. Definition 1.1, printed p.3, distinguishes a permutation complex from an arbitrary complex of permutation modules: boundaries must respect the submodules generated by subgroup-fixed basis points. Problem 3.1, printed p.20, asks which modules occur as the sole homology of a bounded complex with this additional structure. This is an extra realization requirement, not an automatic property of a projective resolution. Theorems later in that section have finite-group and additional spectral-sequence hypotheses. No such theorem is applied to arbitrary small categories here. Primary PDF: https://archive.mpim-bonn.mpg.de/id/eprint/2986/1/preprint_1990_46.pdf . Read in web reader; no local copy downloaded here.

**Nguyen–Raptis–Schrade (2022).** The primary journal PDF of *Higher weak (co)limits, adjoint functor theorems, and higher Brown representability* was opened. Definition 2.1.5 and Proposition 2.1.6 concern higher weak colimits through connectivity of cone-category mapping spaces. Remark 2.1.10 states that in an n-category, weak colimits of order at least n are actual colimits. For ordinary categories this is therefore much stronger than the present filling condition; it is not an n-totality theorem of the needed kind. Primary PDF: https://ems.press/content/serial-article-files/26680 . Read in web reader; no local copy downloaded here.

Queries, using both available search engines, included:

- `"higher" "fixed point" "categories" Reiterman`
- `"homological dimension" "permutation" "categories"`
- `"homotopically flat" "category" sets`
- `"n-filtered" categories homology`
- `"small categories" "homotopical dimension"`
- `"permutation modules" "flatness"`
- `"categories" "higher fixed point properties"`
- `"quasi-filtered" "homology"`
- `"permutation modules" "relative homological algebra"`
- `"homology" "set-valued functors" "dimension"`
- `"categories" "n-connected" "colimits" exact`
- `"ultraproduct" "contractible" "simplicial"`

Hits about differential-graded K-flatness, number-indexed filtrations, and diagonal/test-category total asphericity were not used as statements about the manuscript's totality. The failed search is not a claim that the mathematical problem is open in the literature.

## References

Assadi, A. H. (1990). *Permutation complexes and modular representation theory* (MPI/90-46) [Preprint]. Max-Planck-Institut für Mathematik. https://archive.mpim-bonn.mpg.de/id/eprint/2986/1/preprint_1990_46.pdf

Barthel, T., Schlank, T. M., & Stapleton, N. (2020). Chromatic homotopy theory is asymptotically algebraic. *Inventiones Mathematicae, 220*, 737–845. https://doi.org/10.1007/s00222-019-00943-9

Nguyen, H. K., Raptis, G., & Schrade, C. (2022). Higher weak (co)limits, adjoint functor theorems, and higher Brown representability. *Documenta Mathematica, 27*, 1369–1420. https://ems.press/content/serial-article-files/26680
