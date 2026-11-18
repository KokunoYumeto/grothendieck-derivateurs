# Independent audit of the free-hull / injective-replacement reduction

GPT-6 Astra, 17 November 2026. Audited the new section “Coincidence
monoids and finite free hulls” in `notes/D_Cdelta_attempts_G.md`.
Conclusion: the reduction is sound, with the minor edge cases below
made explicit. It is not a solution of the C_delta comparison.

## Primary statements independently reopened

1. Arturo Carpi and Flavio D’Alessandro, *Černý-like problems for
   finite sets of words*, ICTCS2014, Theorem 1, printed p.84 / PDF
   p.90, https://ceur-ws.org/Vol-1231/proceedings.pdf . The displayed
   stability condition is exactly: n2=u n1 and n4=n3 u, with the
   four n_i in N, imply u∈N. Theorem 1 characterizes free submonoids
   of a free monoid by that condition. Web references
   turn470338319view0 and turn401952131view0. The theorem is cited
   there as a known result; this audit does not claim to have read
   Schützenberger’s original proof.
2. Giuseppa Castiglione, Gabriele Fici, Antonio Restivo, *On Sets of
   Words of Rank Two*, arXiv:1810.02182v2, §2, Theorems 2.1 and
   2.2 and the preceding free-intersection paragraph, opened at
   https://arxiv.org/html/1810.02182v2 . These state exactly the
   free-hull rank bound and strict rank decrease for a finite
   non-code. Web references turn470338319view1 and
   turn401952131view1. No stronger rank or primitive-root theorem
   from later sections is needed here.

These sources are already owned and recorded by the localization
thread; this audit creates no duplicate bibliography keys.

## 1. Local freeness of the filtered limit

The minimum-rank argument is valid. For a fixed finite set X in
S=colim F_i, choose a lift and minimize, over later stages and finite
free submonoids containing that lifted image, the nonnegative rank.
This is a nonempty set of integers. A transition noninjective on
the chosen rank-r free submonoid sends its basis to a non-code and
therefore admits a strictly smaller free hull, a contradiction.
Any equality in the filtered limit is witnessed at a finite stage,
so the chosen free submonoid embeds into S.

Minor edge cases: if a generator image is empty or two generator
images coincide, first delete the empty word or duplicate. The
remaining set has at most r−1 members, so its free hull has rank
at most r−1. Otherwise a failure of injectivity is precisely a
non-code relation among the r distinct nonempty images. If X has
only the identity, take the rank-zero trivial free submonoid.

The required ambient cancellativity and conicality also follow by
finite witnesses. The “locally free” conclusion means every finite
set is contained in a free submonoid; it correctly does not say that
every finitely generated submonoid is free.

## 2. Intersection with a second free submonoid

Let H and N be free submonoids of cancellative conical S. To show
N∩H stable in H, suppose u∈H and n2=u n1, n4=n3 u with all n_i
in N∩H. Then n3 n2=n4 n1 is an equation inside free N. Levi gives
either n4=n3 t,n2=t n1, or n3=n4 t,n1=t n2, with t∈N.

In the first case, cancelling n3 in n3 t=n3 u gives u=t∈N.
In the second, n3=n3 u t, so u t=1 by cancellation; conicality
gives u=1∈N. Thus the stability criterion applies in free H.
No claim that arbitrary submonoids of free monoids are free is
being used. N itself is required to be free, and S is required
to be cancellative and conical.

This establishes the key intersection step under the exact stated
hypotheses. For finite X⊂H, its ordinary free hull F_H(X) is
contained in every free submonoid N of S containing X, because
N∩H is another free submonoid of H containing X. Since F_H(X)
itself is a free submonoid of S, it is the intrinsic least free
submonoid of S containing X, independent of H.

## 3. Automorphism and functoriality claims

An automorphism fixing X pointwise preserves the intrinsic hull
setwise. It permutes its canonical atoms. Every atom must occur
in some X-word: otherwise the free monoid on the remaining atoms
would be a smaller free submonoid containing X. Uniqueness of
ordered word factorization therefore forces every atom to be
fixed. This proves pointwise fixation of the entire hull.

For the proposed N(B)=F_S(image basis(M(B))), an embedding B→D
extends to an automorphism g of the rich limit. The image of the
finite defining set lies in the free monoid N(D), so minimality
gives g N(B)⊂N(D). Different extensions differ by an automorphism
fixing B and hence fixing the hull pointwise. Composition is
therefore strict. The natural map M→N and injectivity of every
transition are both justified.

## 4. Comparison and infinite bases

M and N have the same continuous G-monoid filtered limit S.
The product-compatible saturation proof in
`notes/D_free_limit_criterion.md`, Lemma 1, then gives the needed
homotopy-colimit comparison and the ordinary monoid-colimit
isomorphism. Equivalently, the orbit argument gives the separate
bijections colim U(M^k)≅S^k/G for every finite k. This must not
be phrased as Set colimits commuting with products; they do not.

The finite-rank subdiagram exhaustion also checks. A finite set of
tagged source letters has only finitely many images at any fixed
target because C_delta has finite hom sets. The support letters
of all those image words form a finite basis subset. Under further
substitution, every letter that occurs still lies in the support
of the corresponding composite image: positivity prevents
cancellation. Erasing substitutions cause no problem. These
subdiagrams are directed and exhaust the original diagram.
Nerves and simplicial replacements use finite data and hence
commute with this filtered union; monoid colimits commute with
it as well. Filtered simplicial colimits preserve weak homotopy
equivalences. The reduction to finite-rank injective diagrams is
therefore valid.

## Scope

The reduction does not make the group-completion maps injective,
does not supply a positive amalgamation theorem, and does not show
that the filtered limit itself is a free monoid. Those stronger
assertions are neither needed nor established.
