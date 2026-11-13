# A universal cone kills the binary H2 obstruction

Status: proved for both the full ordered positive-predimension category and the full subcategory with every point and hyperedge d-closed. This note records the binary-action stage. Its then-open all-action question has been superseded by the independently audited finite-support proof in `sections/predimension_stabilizers.tex` and `sections/predimension_totality_reduction.tex`; the binary cone alone does not provide that general theorem.

Let A be either category defined in `predimension_category.md`. Let G_X have vertices A(V,X) and edges A(W,X), with a W-arrow directed from its first to its second point. Let K(X)=Z_1(G_X;Z), with augmentation epsilon given by the sum of its edge coefficients.

**Proposition.** `colim_A K → Z` is an isomorphism via augmentation. Therefore H_2(El_A H;Z)=0 for H=A(V,−)/(ev_1∼ev_2).

The detailed proof, including the finite predimension checks, is in `sections/predimension_binary_cycles.tex`, labels A:predimension-three-path, A:predimension-loose-cycle, and A:predimension-binary-colimit.

## The construction

Given a finite cycle z in G_X, let B be the set of its binary endpoints. Adjoin one new centre c. For every x∈B, adjoin a length-three loose path x→r_x→s_x→c, with distinct private third vertices a_x,b_x,d_x. All interiors and private points are mutually disjoint.

The five new vertices in a single such path have relative predimension strictly positive on every nonempty subset over the two existing endpoints. If one, two, or three new hyperedges are present, at least two, four, or five new vertices are needed, respectively, giving relative predimension at least one, two, or one. A subset containing no edge has positive relative predimension as well. Thus attaching the path preserves d-closedness of the old object without requiring its two endpoints to form a d-closed pair.

For each old support edge e with ordered vertices u<v<p, the subhypergraph F_e consisting of e and the two paths P_u,P_v is a loose seven-cycle. Every point and every edge in a loose cycle of length at least four is d-closed. Form X∪F_e first as a free amalgam over the actual old W-edge; then add every remaining path. The positive relative estimate proves F_e≤dZ.

This works even if the old third point p is itself another binary vertex of z. Its additional path joins two existing vertices of F_e; length three still contributes positive relative predimension. The analogous length-two attempt would contribute zero and would fail exactly here.

## One ordered cycle type

Order Z by the following blocks: all old X points in their given order; the two-point blocks r_x<s_x ordered by x; the centre c; then the three-point blocks a_x<b_x<d_x ordered by x. Every F_e has the same induced order pattern

    u<v<p<r_u<s_u<r_v<s_v<c<a_u<b_u<d_u<a_v<b_v<d_v.

Thus all F_e are morphic copies of one fixed ordered seven-cycle P, irrespective of the old X, the old edge e, or its position in a larger cycle. Its distinguished cycle kappa=e+P_v−P_u has augmentation 1+3−3=1.

If z=Σ_e c_e e, the cycle condition gives an actual equality of chains in G_Z:

    z = Σ_e c_e (e+P_v−P_u),

because the coefficient of each P_x is the coefficient of x in the boundary of z. All parenthesized cycles are images of kappa. Consequently [z]=epsilon(z)[kappa] in colim K. Since epsilon(kappa)=1, augmentation is an isomorphism.

For the point-and-edge-closed subclass, every new atom occurs in an F_e≤dZ, because every x∈B is an endpoint of some support edge. Thus the same Z belongs to that subclass.

## Homological consequence and scope

Linearizing the binary quotient gives

    0 → K → Z[A(W,−)] → Z[A(V,−)] → Z[H] → 0.

The two middle modules are projective and their colimit map is zero. Splitting into two short exact sequences gives H_2(El_AH;Z)=ker(colim K→Z). Hence this H_2 group vanishes. The argument is natural under the inclusion of a generated AKR category into the full predimension category, so every AKR binary H_2 class dies there, including the selected persistent seed. This is stronger than merely choosing compatible orders on two isomorphic seed cycles.

No conclusion about other set actions or higher homology follows formally from this binary calculation alone. The simultaneous triple column remains injective over every nonzero ring, so these categories remain nonexact. Totality has subsequently been established by the separate finite-support argument, turning that existing obstruction into the negative answer to the main question.

The same chain construction works with coefficients in any commutative ring. Its proof uses no approximate averaging and no conversion of a homotopy-coherent cocone into a strict one.
