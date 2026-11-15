# The direct Shelah-presentation attempt: an explicit cellular obstruction

Authored source/applicability audit, 14 November 2026. This note proves a statement about a specified presentation **two-complex**. It does not identify its homology with group homology.

## Primary sources and versions

Márk Poór and Assaf Rinot, *A Shelah group in ZFC*, Forum of Mathematics, Pi 13 (2025), DOI <https://doi.org/10.1017/fmp.2025.5>.

The published full text was opened at
<https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/shelah-group-in-zfc/0E6D4386E4C6D64B6B4EF2E1529F5A22>.
The inspected passages are Theorem A, Lemma 3.4, Theorem 5.1, the recursive construction in §5.2, and the full defining-relation verification in Lemma 5.20, especially Claims 5.20.1 and 5.20.2.

The available arXiv PDF <https://arxiv.org/pdf/2305.11155> is the preliminary version of 18 May 2023. Its numbering differs: the pertinent verification is Lemma 5.10. Local downloaded files `D_PoorRinot2025.pdf` and `D_PoorRinot2025.txt` contain this **2023 v1**, despite their download filenames. The argument below uses the published numbering and published full text. The author's direct PDF endpoint returned an access error and was not used as evidence.

## What the cardinal construction supplies

At an uncountable regular cardinal \(\kappa\) covered by Theorem 5.1, the construction produces distinguished generators \(x_\alpha\), \(\alpha<\kappa\), with \(x_\gamma\notin G_\gamma\), and \(G=\bigcup_{\gamma<\kappa}G_\gamma\). Lemma 5.20 proves that every subset \(Z\subseteq G\) of cardinality \(\kappa\) satisfies \(Z^{10120}=G\). In particular, the construction gives such a torsion-free group of cardinality \(\aleph_1\) in ZFC.

Every homomorphism \(f:G\to Q\) with \(|Q|<\kappa\) is trivial. Indeed, \(|G|=|\ker f|\,|\operatorname{im}f|\); hence \(|\ker f|=\kappa\), and the displayed property applied to \(Z=\ker f\) gives \(G=(\ker f)^{10120}\subseteq\ker f\). This is the exact map argument establishing the small-image property.

## The actual relation and its boundary

Lemma 3.4 uses the word
\[
 \rho(u,v)=uv\,u^2v\,u^3v\cdots u^{80}v
\]
and adds relations
\[
 r_\sigma=h_\sigma^{-1}\rho(b_\sigma a_\sigma,b'_\sigma a_\sigma).
\]
Here \(h_\sigma\) belongs to the old amalgamated group. The exponent sums of \(u\) and \(v\) in \(\rho\) are respectively \(3240\) and \(80\). Thus, after choosing finite words for the displayed coefficients in the distinguished generators, the integral cellular boundary of this relation cell is
\[
 \partial_2 r_\sigma
 =-[h_\sigma]+3320[a_\sigma]+3240[b_\sigma]+80[b'_\sigma].
\]
The square brackets in this formula mean exponent vectors of the chosen words in the free abelian cellular one-chains; they do not mean classes in an already formed group abelianization. In particular, the formula remains valid before imposing any other relation.

For \(h_\sigma=1\), choose its coefficient word to be empty. Then \(\partial_2r_\sigma\) is divisible by \(40\), and in particular is zero over \(\mathbb F_2\). This calculation is unaffected by the lengths or overlaps of the finite coefficient words for \(a_\sigma,b_\sigma,b'_\sigma\).

## There are \(\kappa\) such cells at distinct outer stages

For every \(\eta<\kappa\), take the set
\[
 Z_\eta=\{x_\alpha:\eta\leq\alpha<\kappa\}.
\]
It has cardinality \(\kappa\), since each distinguished generator is new at its outer stage. Apply the **proof** of published Lemma 5.20 with \(Z=Z_\eta\) and with its arbitrary target element \(h\) equal to \(1\). That proof chooses an index \(\gamma\) from the index set of \(Z\), so \(\gamma\geq\eta\), and constructs a pair \(\sigma_*\). Claim 5.20.1 and the subsequent verification prove that \(\sigma_*\) lies in the actual defining system \(\Sigma\) at the outer stage \(\gamma\). The evaluation table and Claim 5.20.2 identify its coefficient as
\[
 h_{\sigma_*}=h=1.
\]
The relation used to express \(h\) is therefore one of the relations actually added by the recursion, not merely an arbitrary consequence of the final group presentation.

Consequently the set of outer stages carrying a relation with \(h_\sigma=1\) is unbounded in the regular cardinal \(\kappa\), and has cardinality \(\kappa\). Choose one such defining cell at each of \(\kappa\) distinct outer stages.

## Independent cycles in the direct presentation two-complex

Let \(X\) be the direct cellular realization of the defining presentation, retaining these defining relations as distinct two-cells and expanding their coefficients in the distinguished one-cell generators. More generally, the following conclusion holds in every presentation two-complex containing these cells with these attaching words, even when further defining two-cells have been included. Use the empty coefficient word for each displayed identity \(h_\sigma=1\).

Each of the chosen \(\kappa\) two-cell basis vectors is in
\(\ker(\partial_2:C_2(X;\mathbb F_2)\to C_1(X;\mathbb F_2))\).
Distinct cells are linearly independent in \(C_2\). Since \(X\) has no three-cells,
\[
 H_2(X;\mathbb F_2)=\ker\partial_2,
 \qquad
 \dim_{\mathbb F_2}H_2(X;\mathbb F_2)\geq\kappa.
\]
The native construction has at most \(\kappa\) indexed relation cells, so its direct realization has dimension exactly \(\kappa\) in this formula.

This proves that this direct defining two-complex cannot have the homology of \(S^2\), whose second mod-two homology has dimension one. Attaching further two-cells does not remove these cellular two-cycles. No assertion about \(H_2(G;\mathbb F_2)\), or about the existence of another two-dimensional classifying space for \(G\), follows from this calculation alone. Identifying \(H_2(X)\) with \(H_2(G)\) would require a proof that this particular \(X\) is aspherical; no such proof has been obtained in this audit.

## An additional exact map at each outer successor stage

The outer extension \(G_\gamma\hookrightarrow G_{\gamma+1}\) admits a surjective homomorphism
\[
 q_\gamma:G_{\gamma+1}\longrightarrow\mathbb Z/40
\]
that sends \(G_\gamma\) to zero and \(x_\gamma\) to \(1\). To construct it, start with this map on the cyclic group generated by \(x_\gamma\). At each inner amalgamation \(K*_H L\), use zero on \(K\subseteq G_\gamma\) and the already constructed map on \(L\). These agree on \(H\subseteq G_\gamma\). Every added relation maps to zero: its \(h_\sigma\) term is old, and the two exponent sums of \(\rho\) are divisible by \(40\). The map therefore descends through the defining quotient. Inner limit stages use the compatible union. The result is onto because of its value on \(x_\gamma\).

Thus these outer successor inclusions do not induce surjections on first integral homology, and cannot serve as the homology-equivalence attachments used in A.27–A.28. The maps \(q_\gamma\) are maps from individual stages. They are not claimed to be compatible as \(\gamma\) increases, and no map from the final Shelah group to \(\mathbb Z/40\) is asserted.

## Current outcome

The small-quotient property is verified by an explicit kernel argument. The direct defining presentation two-complex has the wrong second homology, by the independent-cell calculation above. The checked source does not supply a simultaneous repair of this cellular homology and an actual two-dimensional classifying space. The remaining \(W=S^2\), \(\mu=\aleph_0\) problem is unchanged.
