# Ramsey categories have exact integral colimits

Working proof by GPT-6 Astra, 13 November 2026. No priority claim. This is a sufficient condition, not a proof that every total category satisfies it.

## Proposition

Let A be a small category with common successors of every finite family of objects. Suppose that A has the following finite-family Ramsey property: for every finite family a_0,...,a_k:p→q and every integer N≥2 there is an object r such that for every coloring χ:A(p,r)→{1,...,N} there is b:q→r with χ(ba_0)=...=χ(ba_k). Then every finite family of parallel arrows has an integral affine equalizer (condition III). If A additionally satisfies Isbell–Mitchell condition I, then its abelian colimit functor is exact.

This hypothesis follows from the usual categorical Ramsey property, which asks that bA(p,q), rather than just the named finite subset, be monochromatic. No finiteness assumption on A(p,r) is needed in the argument.

## Proof

The case k=0 is immediate, so take k≥1. For each object r define the homomorphism of abelian groups

\[
D_r:\mathbb Z[A(q,r)]\longrightarrow \mathbb Z[A(p,r)]^k,
\qquad t\longmapsto(t(a_i-a_0))_{i=1}^k.
\]

Put

\[
E=\sum_{r\in\operatorname{Ob}A}\operatorname{aug}(\ker D_r)\subseteq\mathbb Z.
\]

We first check that E=Z is equivalent to an affine equalizer. The reverse implication is immediate. For the forward implication, write 1 as a finite sum of augmentations of elements t_j∈ker D_{r_j}; negative integer coefficients may be absorbed into the t_j. Choose a common successor s of the finitely many r_j and ordinary arrows u_j:r_j→s. The integral linear combination t=Σ_j u_jt_j belongs to ker D_s and has augmentation1. Thus t is an integral affine equalizer. This use of common successors is the only place where elements at different target objects are combined.

Suppose for contradiction that no affine equalizer exists. Then E=dZ is a proper ideal of Z, with d=0 or d≥2. Let T=R/Z, given its usual translation-invariant circle metric. Choose a nonzero c∈T with dc=0 when d≥2 (for example c=1/d modZ); when d=0 choose any nonzero c. Consequently ec=0 for every e∈E.

For every object r, the formula

\[
\lambda_r(D_rt)=\operatorname{aug}(t)c
\]

defines a homomorphism λ_r:imD_r→T: if D_rt=D_rt', then t−t'∈kerD_r and its augmentation lies in E. The circle group is divisible, hence injective as a Z-module. Therefore λ_r extends to a homomorphism

\[
\widetilde\lambda_r:\mathbb Z[A(p,r)]^k\longrightarrow T.
\]

Writing the restriction to the i-th summand as the linear extension of a function φ_i^r:A(p,r)→T, we obtain, for every b:q→r,

\[
\sum_{i=1}^k\bigl(\phi_i^r(ba_i)-\phi_i^r(ba_0)\bigr)=c.\tag{1}
\]

Let η=dist_T(c,0)>0 and choose δ>0 with kδ<η. By compactness, T^k has a finite partition into N≥2 cells such that two points in one cell have distance less than δ in each coordinate. Choose r supplied by the finite-family Ramsey property for this N, and form the functions φ_i^r just constructed at this r. Color h:p→r by the cell containing (φ_1^r(h),...,φ_k^r(h)). There is b:q→r for which ba_0,...,ba_k all have the same color. Thus every difference φ_i^r(ba_i)−φ_i^r(ba_0) has distance less than δ from0. By the triangle inequality the left side of (1) has distance less than kδ<η from0, contradicting (1). Hence E=Z and condition III holds.

When I holds, exactness follows from Isbell–Mitchell (1976), Proposition3.3. In a nonempty connected category, I already supplies common successors: along a connecting zigzag, repeatedly complete spans to commutative squares. The proposition therefore applies to a nonempty connected category satisfying I and the stated finite-family Ramsey property. ∎

## Consequences for candidate C4

1. The skeleton of the category of nonempty finite linearly ordered graphs, with order-preserving induced embeddings, is nonempty, connected and satisfies I. To amalgamate a span, take the union over its common induced subgraph, put no new graph edges between the two new parts, and extend the two compatible finite linear orders to one order. Every finite family has a common successor by disjoint ordered union. Its usual categorical Ramsey property is the ordered graph instance of the Nešetřil–Rödl theorem. The proposition shows integral exactness, hence totality by R2. It is not filtered: two distinct embeddings of the one-vertex graph into a two-vertex graph remain distinct after every embedding.
2. Exactly the same conclusions hold for finite linearly ordered triangle-free graphs. The free amalgam adds no edges between new parts, so introduces no new triangle. Its structural Ramsey theorem therefore gives integral exactness. The same two one-vertex embeddings prove nonfilteredness.
3. More generally, any rigid finite-structure Ramsey class with amalgamation and joint embedding, with all embeddings as morphisms, is exact by the proposition. Thus the Ramsey classes proposed in C4 are excluded as separators; no assertion about arbitrary non-Ramsey homogeneous classes follows.

Because the proof is integral, the resulting categories are exact over every commutative coefficient ring, using the usual tensoring of an integral affine equalizer (or the coefficient version of Isbell–Mitchell1976, p296).

## Opened primary sources and exact scopes

- Mašulović, *A new proof of the Nešetřil–Rödl theorem*, arXiv:1703.04685v6, corrected version dated2June2026: Definition2.1 states the categorical Ramsey property; Example2.1 gives it for ordered uniform hypergraphs, including graphs. Section4 contains a proof for all finite ordered relational structures. The introduction explicitly says that the paper does not prove the forbidden-substructure version, so it is not being used alone for triangle-free graphs. FullPDF: https://arxiv.org/pdf/1703.04685 . Webref turn30view0.
- Hubička, *Big Ramsey degrees using parameter spaces*, arXiv:2009.00967v5 (2025), Theorem15 and complete §5.1 proof pp14–17 opened/read: all finite ordered triangle-free graphs have the embedding Ramsey property. FullPDF https://arxiv.org/pdf/2009.00967 . Webrefs turn34view0,turn35view0. The proof encodes all one-types, represents every subembedding by a parameter word, and applies its finite parameter-word theorem.
- Hubička and Nešetřil, *All those Ramsey classes*, Adv.Math356(2019),106791, arXiv:1606.07979v4: Theorem3.21, Definition4.1, Corollaries4.2–4.3 and their proofs read. Cor4.2: ordered free amalgamation classes of relational structures are Ramsey; Cor4.3 explicitly includes ordered simple graphs. FullPDF https://arxiv.org/pdf/1606.07979 . Webrefs turn34view1,turn36view1. Minimal forbidden structures are irreducible because otherwise ordered free amalgamation contradicts minimality.

## Relation to the main question

The general implication total⇒exact is not established by this argument. Totality has not been shown to imply the finite-family Ramsey property. The proof does, however, close the particular Ramsey candidate route C4 without testing only finitely many A-sets or making a permutation-module-to-arbitrary-module transfer.
