# A full ordered predimension category: the quasi-filtered stage

Status: the quasi-filteredness and nonexactness statements below are proved. **The original totality-open status of this historical note has been superseded:** the independently audited alternating bridge and all-action comparison now prove totality of both categories; see `sections/predimension_stabilizers.tex`, `sections/predimension_totality_reduction.tex`, and Theorem A:predimension-total. The earlier investigation is retained below to show which parts did and did not establish totality on their own. No priority claim is made.

## 1. The category

For a finite simple 3-uniform hypergraph X and a vertex subset U, let

    delta_X(U) = 2|U| - 3|E_X(U)|,

where E_X(U) is the set of hyperedges contained in U. Let C_delta be a small skeleton of the category whose objects are nonempty finite linearly ordered such hypergraphs satisfying delta_X(U)>0 for every nonempty U. A morphism is an increasing induced embedding f:S→T with d-closed image:

    delta_T(U) > delta_T(fS)  whenever fS is properly contained in U⊆T.

Isomorphisms satisfy this condition vacuously. The empty structure may instead be included as an object; all proofs below remain valid. When it is excluded, it is still convenient as a formal amalgamation base.

The term d-closed and the strict predimension condition are used by Evans, Hubička, and Nešetřil (2019, Definition 4.4) for sparse graphs. Their Lemma 4.8 and Remark 4.12 discuss the associated submodular closure calculus. The weighted 3-uniform category here and the necklace estimate below are proved directly; no theorem about its Ramsey property or totality is imported from that paper.

## 2. Closure calculus and free amalgamation

For vertex subsets U,V of one hypergraph, submodularity gives

    delta(U)+delta(V) >= delta(U∪V)+delta(U∩V).

Indeed the vertex contribution is modular, while every edge in U or V is in U∪V, and their common edges are exactly those in U∩V.

If A≤d B and X⊆B, then A∩X≤d X. For A∩X⊊U⊆X, one has U∩A=A∩X and U∪A properly contains A, whence

    delta(U)-delta(A∩X) >= delta(U∪A)-delta(A) > 0.

The relation ≤d is transitive. To see this for A≤d B≤d C and A⊊U⊆C, use the preceding restriction assertion to obtain U∩B≤d U. If U⊆B, use A≤d B. Otherwise delta(U)>delta(U∩B)≥delta(A). Intersections of d-closed subsets are d-closed, by restriction followed by transitivity.

Consequently every finite subset has a least d-closed closure. If S≤d T and F⊆S, then cl_T(F)=cl_S(F), viewed inside S: the left side is contained in the d-closed set S, and restriction and transitivity give both minimality implications.

For d-closed induced inclusions A≤d B,C, form the free hypergraph amalgam D=B∪_A C. The linear orders can be amalgamated by merging the two finite chains separately in each interval determined by A. For every U⊆D,

    delta_D(U)=delta_B(U∩B)+delta_C(U∩C)-delta_A(U∩A).

If U has a vertex in C\A, the last two terms have positive difference, by A∩U≤d C∩U; the first term is nonnegative. If there is no such vertex, U is a subset of B. Thus all nonempty U have positive predimension. For B⊊U⊆D,

    delta_D(U)-delta(B)=delta_C(U∩C)-delta(A)>0.

Therefore B,C≤d D. Free amalgamation proves condition I, and disjoint amalgamation proves common successors and connectedness.

## 3. Repaired necklaces as hypergraph colimits

Let f,g:S⇉T be morphisms. Because they are increasing, the nonfixed components of the partial bijection f(s)↦g(s) are directed paths. Choose n≥2 bounding their numbers of vertices, set w=2n−2, choose k≥n, and put s=4k+1. Use the covered, actual-path-length repaired point target Z and its injections alpha_i:T→Z, as in `sections/akr_ordered_necklace.tex`.

Its precise overlap equations are

    alpha_i lambda_i = alpha_(i+1) mu_i,

with cyclic indices and

    (lambda_i,mu_i)=(g,f)  for 0≤i<2k;
                    (g,g)  for i=2k;
                    (f,g)  for 2k<i<4k;
                    (f,f)  for i=4k.

Each target vertex has a fibre indexed either by the whole index circle (a fixed point) or by a proper cyclic interval of at most w indices (a nonfixed or private point). Each alpha_i is injective, the exact consecutive overlap is the indicated S-image, and the point target is the strict set colimit of this necklace.

Declare the edges of Z to be the union of the images of the edges of the T-copies. Then every alpha_i is induced. In fact, suppose an edge from copy j has all three vertices visible in copy i. Every proper visibility interval is shorter than half the index circle, since w≤2k−2 and s=4k+1. It therefore contains the unique shortest index path between any two of its indices. The shortest path from j to i lies in all three vertex visibility sets. At every consecutive overlap, the edge lies in the S-image. Because the source maps S→T are induced, the edge comes from an edge of S and propagates to the next copy. It consequently occurs in copy i.

This argument also shows that an edge's visibility is exactly the intersection of the visibility sets of its three vertices. It is a connected proper cyclic interval, unless all vertices are fixed, in which case it is the full circle. Thus all point and edge identifications are generated by the consecutive overlaps, and Z is the strict hypergraph colimit of the necklace.

Deleting one overlap yields a linear amalgam L of s copies of T. It is an iterated free amalgam over S, so it is sparse and every T-copy is d-closed in L. Its quotient map q:L→Z restores only the omitted overlap. Each nonfixed vertex fibre in L is a component of its former proper cyclic visibility interval and has at most w indices. Full-circle vertex fibres become connected paths. At most |S| vertex pairs are identified by q.

## 4. The predimension estimate

Choose k also so large that

    s > w (delta(T)+2|S|).                                      (P)

Let U be any subset of the vertices of Z, and let U_tilde=q^{-1}(U) in a cut linear amalgam L. Every edge of Z[U] has a preimage edge in L[U_tilde], and the only vertex identifications are those from the omitted S-overlap. Thus

    delta_Z(U) >= delta_L(U_tilde)-2|S|.                       (1)

More exactly, if d_v and d_e are the numbers of vertex and edge duplications removed by q on these induced substructures, then

    delta_L(U_tilde)-delta_Z(U)=2d_v-3d_e,

where 0≤d_v≤|S| and d_e≥0. Edge identifications help the lower bound; they are not ignored with the wrong sign.

There are two cases.

### Case 1: a copy index is missed

Suppose the union of the proper visibility intervals of the vertices in U misses an index r. Cut the overlap from r−1 to r. No proper vertex fibre of U is severed, and every full-circle fibre becomes a connected path. Hence q is bijective on the vertices above U. The induced edge correspondence is also bijective: edge fibres are connected and, equivalently, a simple edge cannot have two different lifts once all its vertices have unique lifts. Therefore Z[U] and L[U_tilde] are isomorphic.

If U is nonempty, delta_Z(U)>0. If U properly contains some alpha_i(T), its lift properly contains that T-copy in L, so delta_Z(U)>delta(T).

### Case 2: every copy index is covered

Cut at any overlap and label the resulting chain 0,...,s−1. Build L[U_tilde] by adjoining its intersections U_j with the T-copies successively. At step j>0, the new copy meets the preceding linear amalgam in exactly its incoming S-image A_j. Consequently its predimension contribution is

    delta(U_j)-delta(U_j∩A_j).

If U_j has a vertex outside A_j, submodularity and A_j≤d T_j give

    delta(U_j)-delta(U_j∩A_j)
       >= delta(U_j∪A_j)-delta(A_j) >= 1.                    (2)

If U_j is contained in A_j, the contribution is zero. At j=0 the contribution is delta(U_0), which is at least one when U_0 is nonempty.

Let E be the set of chain indices at which at least one nonfixed vertex of U_tilde first appears. For a fixed j∈E, every such newly appearing vertex is visible only among indices j,...,j+w−1. This is because each of its linear visibility intervals has at most w indices. The hypothesis of this case says that every copy index contains a nonfixed U-vertex. The corresponding vertex in L has a first-appearance index in E. Hence the intervals [j,j+w−1], j∈E, cover the s indices, and

    |E| >= ceil(s/w).

Each j∈E contributes at least one in (2), or at the initial step. All other contributions are nonnegative. It follows that

    delta_L(U_tilde) >= ceil(s/w).

Combining this with (1) and (P) gives

    delta_Z(U) >= ceil(s/w)-2|S| > delta(T) > 0.              (3)

The count is by first-appearance *indices*, not by the number of new vertices. Arbitrarily many vertices may first appear at one stage; they still cover only the next w indices. No boundedness of |T| is assumed.

The two cases show that Z is sparse and every alpha_i(T) is d-closed in Z.

## 5. Ordering and the explicit affine equalizer

The eventual ordering proposition in `sections/akr_ordered_necklace.tex` applies to these same point injections. Thus k can additionally be chosen beyond its threshold, so Z admits a linear order making all alpha_i increasing. All alpha_i are now morphisms in C_delta.

The integral affine combination

    t = sum_(i=0)^(2k) alpha_i - sum_(i=2k+1)^(4k) alpha_i

has augmentation one. The overlap equations give

    t g = sum_(i=1)^(2k) alpha_i f
          - sum_(i=2k+1)^(4k-1) alpha_i f
        = t f - alpha_0 f + alpha_(4k) f = t f.

Thus every parallel pair has an integral affine post-equalizer. With condition I and connectedness from free amalgamation, this proves that C_delta is quasi-filtered.

The same proof applies to the full subcategory in which every point and every hyperedge is d-closed: free amalgams and the necklace target are covered by old copies, and transitivity preserves each such d-closed atom. This subclass also contains V and W below. No assertion is made here that totality passes between this subclass and the full category.

## 6. The triple obstruction over every nonzero ring

Let V be the one-point structure and W the ordered three-point structure with its single hyperedge. All three point embeddings v_1,v_2,v_3:V→W are d-closed, because their source predimension is two, while the proper two-point and three-point extensions have predimensions four and three.

For any nonzero unital coefficient ring R, consider

    D:R[C_delta(W,-)] → R[C_delta(V,-)]^2,
    D(g)=(g v_2-g v_1, g v_3-g v_1).

This map is objectwise injective. If a nonzero finitely supported coefficient vector has support r distinct W-morphisms, their images are r distinct hyperedges, since an increasing embedding of the fixed three-point ordered set is determined by its image. Let U be their vertex union, of size v. Positivity gives

    2v > 3|E(U)| >= 3r.

As the total number of incidences in these r hyperedges is 3r, some vertex belongs to exactly one support edge. At its corresponding V-arrow, that coefficient occurs as (−c,−c), (c,0), or (0,c), according to its position in W. It cannot cancel. The V-arrow exists because V→W→X is a composite of d-closed embeddings. This proves injectivity over every R, without a field or domain assumption.

Consequently no nonzero linear combination, and in particular no augmentation-one combination, simultaneously equalizes the three arrows. For Q=coker D, the two representable terms are projective, their colimits are R and R², and the colimit map D is zero. The exact sequence therefore gives

    T_1^{C_delta}(Q) ≅ R.

C_delta is not exact over any nonzero unital ring.

## 7. The then-unresolved issue and useful cautions

At this stage totality had not been proved or refuted. A proof that C_delta was total would turn the preceding all-ring obstruction into a negative answer to A.1. Quasi-filteredness alone did not establish it; the separately selected AKR construction already showed why that implication was unavailable. The later finite-support proof now supplies the required totality theorem.

Raw vertices and raw hyperedges of a general object need not be d-closed. Thus the actions represented by V and W need not contain all raw vertices and edges. The proof of D-injectivity uses only actual W-morphisms and their composite V-morphisms. The atom-closed subclass avoids this particular mismatch, which by itself did not settle totality.

The fixed subset of any parallel pair f,g:S⇉T is d-closed in S. Indeed if F={x:f(x)=g(x)}, closure preservation gives f(cl_S F)=cl_T(fF)=g(cl_S F), so g^{-1}f is an increasing permutation of cl_S F and is the identity. Hence F=cl_S F. This is a closure statement, not a statement that F is connected in the binary graph used for the AKR H_2 argument.

The selected AKR category maps faithfully into this full category when its distinct W-images are regarded as hyperedges. The full category has additional old-target embeddings and additional d-closed amalgams; a nonzero class for the generated AKR subcategory is not thereby nonzero in the full category. In particular, d-closed extensions can add long paths between old vertices. The selected AKR convexity argument does not apply solely from d-closedness.

## Reference

Evans, D. M., Hubička, J., & Nešetřil, J. (2019). Automorphism groups and Ramsey properties of sparse graphs. *Proceedings of the London Mathematical Society, 119*(2), 515–546. https://doi.org/10.1112/plms.12238 (Author manuscript: https://arxiv.org/abs/1801.01165.) Definition 4.4, Lemma 4.8, and Remark 4.12 were inspected in the primary manuscript. The present weighted-hypergraph necklace calculation is not attributed to that paper.
