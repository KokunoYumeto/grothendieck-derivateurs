# Finite interpolation and finite-image word maps

Author: Part A collaborator. Independently audited by C collaborator, 2026-11-14.

## 1. Exact finite interpolation statement

Let F be a nonabelian simple group. Let c_1,...,c_m be pairwise distinct elements of F, and let d_1,...,d_m be arbitrary elements. There is a one-variable word q(y)∈F*〈y〉 whose total y-exponent is zero and whose evaluations satisfy q(c_i)=d_i for every i.

Let A be the kernel of the exponent homomorphism F*〈y〉→Z. Its evaluation image in F^m contains the diagonal subgroup ΔF and the subgroup

    D_c={(c_i a c_i^{-1})_{i=1}^m : a∈F},

because these are the evaluations of the exponent-zero words a and y a y^{-1}, respectively. We show the subgroup K=〈ΔF,D_c〉 is F^m.

For every pair of coordinates i≠j the projection of K onto F×F is onto each factor. A proper subdirect subgroup of F×F must be the graph of an automorphism: the kernels of its two coordinate projections give normal subgroups of F, so simplicity leaves either the full product or an isomorphism graph. Since K contains the diagonal, that automorphism would have to be the identity. But D_c would then give c_i a c_i^{-1}=c_j a c_j^{-1} for all a, making c_j^{-1}c_i central. The center is trivial and c_i≠c_j, a contradiction. Thus every two-coordinate projection is the full product.

We prove by induction on m that these facts force K=F^m. The case m=2 has just been checked. Its projection to the first m−1 factors is full by induction. Let N=K∩({1}^{m−1}×F). The last-coordinate image of N is normal in F, since K projects onto the last factor; hence it is either F or 1. In the first case K=F^m. In the second, the projection K→F^{m−1} is an isomorphism, and K is the graph of an epimorphism ψ:F^{m−1}→F. Each direct factor has normal image under ψ, and hence image either 1 or F. Images of distinct factors commute. Since F is nonabelian, at most one factor has image F; since ψ is onto, precisely one does. Its restriction is an automorphism, and the resulting two-coordinate projection is a graph, contradicting the preceding paragraph. The induction is complete.

Therefore A evaluates onto F^m. A preimage of (d_i) is the asserted exponent-zero interpolation word. This proves the statement without invoking an unproved interpolation theorem.

## 2. Unimodular closure excludes every nonconstant finite-image word map

Let F be nonabelian simple and suppose every one-variable equation over F with exponent ±1 has a solution in F. Let p(x) be any one-variable word whose evaluation image C=p(F) is finite. Then p is constant as a function on F.

For a contradiction choose t with p(t)≠p(1), and put b=t^{-1}. In particular t≠1 and b≠1. Apply Section 1 to the finite set C, prescribing an exponent-zero word q(y) with

    q(p(1))=b,
    q(c)=1 for every c∈C\{p(1)}.

Set v(x)=q(p(x)). Substitution gives exponent(v)=exponent(q)·exponent(p)=0. Its values lie in {1,b}, while v(1)=b and v(b^{-1})=v(t)=1.

The word u(x)=v(x)x has exponent 1 and no solution to u(x)=1. Indeed a solution would have x=v(x)^{-1}∈{1,b^{-1}}. At the first candidate u(1)=b≠1, and at the second u(b^{-1})=b^{-1}≠1. This contradicts the assumed equation-solving property.

Thus every nonconstant one-variable word map on such F has infinite image. This consequence is stronger than excluding a word with just one exceptional nonidentity value, but it does not rule out constant nested commutator maps. In particular no implication to mixed-identity-freeness has been proved here.
