# Actual two-dimensional inclusions with simple final group

Author: Part A collaborator. Checked 2026-11-14, 20:38 UTC.

## Primary source and exact input

Anton A. Klyachko, *The Kervaire–Laudenbach conjecture and presentations of simple groups*, Algebra and Logic **44** (2005), 219–242, DOI <https://doi.org/10.1007/s10469-005-0023-y>. Primary author preprint: <https://arxiv.org/pdf/math/0409146>, opened as `turn351view0`; local copies are `A_Klyachko2005.pdf` and `A_Klyachko2005.txt`.

The Main Theorem says that, for a torsion-free coefficient group H, the group E presented by one extra generator t and one extra relator w is nonabelian simple precisely when H is nonabelian simple and w is conjugate in H*<t> to t^ε h, with ε=1 or −1 and h∈H.

The complete twenty-page preprint was read. The audit checked its normal-form reduction, coefficient injection, added-relator argument, collision schedules, and both final cases. The comotion weights cancel to Euler characteristic; the planar edge bound gives Lemma 17. Lemmas 20–23 then produce a nontrivial added relator whose quotient still contains the coefficients, proving nonsimplicity. The final coefficient choice follows because a group whose squares lie in one cyclic subgroup is metabelian. No gap was found in these implications. This is a source-proof audit, not a formal verification.

## Proved one-pair consequence, with the comparison map

Let Y⊂X be connected actual CW complexes, each of dimension at most two. Suppose the pair has one relative one-cell and one relative two-cell, after collapsing compatible maximal trees, and suppose π₁(Y)=H is torsion-free. Write the canonical relative presentation as

\[
\pi_1(X)=E=(H*\langle t\rangle)/\langle\!\langle w\rangle\!\rangle.
\]

Assume E is nonabelian simple. Klyachko's Main Theorem gives h∈H and ε∈{1,−1} with w conjugate to t^ε h. Conjugate relators have the same normal closure. Define

\[
q:H*\langle t\rangle\longrightarrow H,
\qquad q|_H=1_H,
\qquad q(t)=
\begin{cases}h^{-1}&\epsilon=1,\\h&\epsilon=-1.\end{cases}
\]

The word t^ε h maps to 1, so q descends to \bar q:E→H. The composite H→E→H is the identity. Conversely, the defining relation in E says that t equals the displayed element of H. Hence the composite E→H→E fixes H and t, which generate E, and is the identity. The canonical H→E is therefore an isomorphism, with inverse \bar q.

When Y and X are classifying spaces, their inclusion is consequently a homotopy equivalence: it induces an isomorphism on π₁ and both spaces have zero higher homotopy groups. The proof uses the specified inclusion map; it does not replace it by an unrelated equivalence between models.

For a homology-equivalence pair with these relative cell counts, the relative cellular boundary is multiplication by ε=±1. Thus its exponent hypothesis follows directly from the pair, although the cited Main Theorem already covers arbitrary w.

## Proved transfinite one-pair consequence

Let (X_α)_{α≤θ} be a continuous increasing family of connected actual two-dimensional CW complexes. Suppose X₀ is aspherical, every successor adds one one-cell and one two-cell with exponent ±1 in the new generator, and every X_α is aspherical. At a limit ordinal take the actual CW union. Assume the final group G=π₁(X_θ) is nonabelian simple and π₁(X₀)≠1.

For α≤β, the inclusion X_α⊂X_β is an ordinary homology isomorphism. At successors this follows from the relative cellular complex Z→Z with boundary ±1. At limits cellular chains are directed unions, so the statement persists. Claim A.23 therefore gives an injection

\[
i_{\alpha,\theta}:H_\alpha=\pi_1(X_\alpha)\hookrightarrow G
\]

and the exact identity

\[
\langle\!\langle N\rangle\!\rangle_G\cap i_{\alpha,\theta}(H_\alpha)
=i_{\alpha,\theta}(N)
\qquad(N\triangleleft H_\alpha).
\]

Every H_α is nontrivial because it contains the embedded H₀. Simplicity of G and this identity show that every H_α is simple. Every H_α is torsion-free: its classifying space has dimension at most two, and restriction to a subgroup of prime order would give a two-dimensional classifying space for that finite cyclic group, contrary to its nonzero homology in arbitrarily high odd degrees.

Apply the one-pair result above to X_α⊂X_{α+1}. Its canonical homomorphism i_{α,α+1} is an isomorphism. At a limit ordinal β, van Kampen identifies H_β with the colimit of the actual inclusions H_α→H_γ. A directed system whose structure maps are isomorphisms has colimit canonically isomorphic to any initial term: the inverses to i_{0,α} are compatible and induce the inverse of i_{0,β}. Transfinite induction therefore proves that i_{0,θ}:H₀→G is an isomorphism.

Thus such a tower with simple final group cannot properly enlarge its initial group. This conclusion includes arbitrary set-sized ordinals and arbitrary cardinalities of H₀. It is a consequence about the canonical structure homomorphisms, not about their cardinalities alone.

## Exact boundary of this result

An arbitrary relative exponent isomorphism need not permit a successive ordering in which each new relator uses only one new generator. The argument above uses that ordering at every successor. It supplies no reduction of a multi-variable simultaneous attachment to one-pair attachments. The unresolved construction is an actual two-dimensional homology-equivalence inclusion of distinct simple groups obtained by simultaneous interacting relations, or a construction with no nontrivial countable images that does not require simplicity. No such inclusion or construction has been established here.

## A countable core that closes all finite solution witnesses

There is a further proved obstruction for finite simultaneous attachments inside a specified large simple group.

Let X be an actual two-dimensional classifying CW complex, with G=π₁(X), and suppose H₁(X;Z) and H₂(X;Z) are countable. Fix any countable collection of cells and any nonidentity g∈G. The countable homology-core construction of A.19 can be strengthened to give a countable connected subcomplex Y⊂X containing those cells and a loop for g, with the following properties:

1. The inclusion is an ordinary integral homology isomorphism and injective on π₁; Y is aspherical.
2. Put H=π₁(Y), identified with its image in G. Every finite system of group equations with coefficients in H that has a solution in G has a solution in H.

Here is the explicit closure construction. Start with the countable subcomplex used in A.19. At each stage apply its homology and π₁ closure, retaining a countable subcomplex whose fundamental group embeds in G. There are only countably many finite systems of equations over this countable subgroup. For each system that has a solution in G, choose one solution tuple, choose loops in X representing its finitely many entries, and include the finitely many cells meeting those loops. The union of these additions is countable. Apply the homology/π₁ closure again and repeat for ω stages. The resulting actual union Y has property 1 by the same chain and compactness arguments as A.19. Each finite coefficient list lies in one stage; the next witness stage contains a solution tuple for its system. This proves property 2. No decidability or effective procedure is asserted: the choices are set-theoretic existence choices within the given G.

Now suppose G is nonabelian simple. Then H is nonabelian simple by A.23, since H contains g. Let Y⊂Z⊂X be an intermediate connected subcomplex obtained from Y by finitely many one-cells and finitely many two-cells, with Y→Z an ordinary homology isomorphism. Then Z→X is also an ordinary homology isomorphism. A.23 gives injections H→K=π₁(Z)→G and makes K simple.

Write the actual finite relative presentation

\[
K=(H*F(s_1,\ldots,s_m))/\langle\!\langle w_1,\ldots,w_r\rangle\!\rangle.
\]

Its finite relator system has a solution in G: use the elements represented by the relative one-cells. Property 2 gives elements a₁,…,a_m∈H satisfying the same relators. The homomorphism H*F(S)→H that fixes H and sends s_i to a_i kills all w_j, so descends to r:K→H with r∘i=1_H. It is nontrivial, hence injective because K is simple. It is onto because it fixes H. Therefore r and the given inclusion i:H→K are inverse isomorphisms. In particular Y→Z is a homotopy equivalence of the specified aspherical models.

This proves that every proper extension of this particular countable core, inside X and through a homology-equivalent two-dimensional subcomplex, must require infinitely many relative cells. It excludes finite simultaneous blocks for this selected core, without claiming that every finite balanced relative presentation over an arbitrary simple coefficient group is trivial.

The same reasoning has an exact transfinite form. Suppose a continuous chain of intermediate subcomplexes starts at this Y, ends at X, and at each successor adds finitely many one- and two-cells while preserving ordinary homology. Every stage maps by a homology isomorphism to X, hence its nontrivial group is simple by A.23. Inductively its group is the same embedded H. Each finite next relative system is then a system over this original H, realized in G, so property 2 supplies a retraction and simplicity makes the next group equal H as well. At limits take the colimit of the already identical embedded subgroups. Thus G=H. An uncountable simple G as above cannot admit such a filtration from the chosen Y.


