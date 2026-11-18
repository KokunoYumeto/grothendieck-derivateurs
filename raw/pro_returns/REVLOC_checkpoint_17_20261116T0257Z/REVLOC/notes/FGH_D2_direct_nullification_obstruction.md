# Direct ordinary-nullification test: exact obstructions

This note records the renewed D.2.9 separator search after D.2.10. It adds
no claimed separator and no manuscript result row.

Let B=K(F_p,2), I_p=loc Σ∞B, A_r=QΣ^rB, and
Y_r=Σ^{r+1}B. The outstanding test is

\[
P_{A_r}Y_r\stackrel{?}{\ne}*.
\]

The bounded-suspension reduction in D.2.7 makes this a possible way to
separate the reversible closure from its fixed stable part. D.2.10 rules
out using finite simply connected targets or their p-localizations.

## 1. Primary stable cohomology operations do not obstruct the stable map

For connected X, Snaith gives a stable retraction of the unit summand
Σ∞X→Σ∞QX. Taking X=Σ^rB and suspending once gives a stable retraction

\[
\Sigma^\infty Y_r
\longrightarrow\Sigma^\infty\Sigma A_r
\longrightarrow\Sigma^\infty Y_r.
\]

Thus the desired bottom-degree map from ΣA_r to Y_r has a perfectly
consistent stable model. In particular every generalized cohomology
theory, and the entire primary Steenrod-module structure, admits the
induced retraction. An obstruction to realizing this particular map must
use additional unstable structure. D.2.12 now supplies such an obstruction
at p=2: after looping the target, the homology coproduct and the first two
Steenrod squares are incompatible with any bottom-degree isomorphism.
A failure to
realize the stable retraction would itself still be weaker than proving
that the ordinary nullification P_{A_r}Y_r is nontrivial.

## 2. All finite Goodwillie stages are ordinarily A_r-acyclic

Put n=r+2; A_r has its first nonzero reduced mod-p homology in degree n.
The k-th identity-tower layer of Y_r is Ω∞E_k, where

\[
E_k=(\partial_kI\wedge(\Sigma^\infty Y_r)^{\wedge k})_{h\Sigma_k}.
\]

The derivative is (1−k)-connective and Σ∞Y_r is (n+1)-connective.
Therefore E_k is at least kn+1-connective. Since I_p is a localizing
tensor ideal, E_k belongs to I_p. D.2.9, using the exact Bousfield
space/spectrum nullification comparison, implies

\[
P_{A_r}(\Omega^\infty E_k)=*.
\]

Induction through the fibre sequences of the identity tower, using the
valid fibre-and-base-to-total direction of ordinary acyclicity, gives

\[
P_{A_r}(P_k^{\mathrm G}Y_r)=*
\qquad\text{for every finite }k.
\]

The identity tower converges because Y_r is simply connected. However,
ordinary nullification need not preserve its inverse limit. This is the
remaining exact interface; there is no justified exchange of these two
operations in the current argument.

## 3. A directly matching counterexample to the missing exchange

Let M be a noncontractible finite simply connected p-primary Moore
space, and use ordinary BZ/p-nullification. Every layer of its identity
tower is a connected p-primary infinite-loop space. Levy's Theorem 3.2
makes each layer BZ/p-acyclic, and the same finite induction gives

\[
P_{B\mathbb Z/p}(P_k^{\mathrm G}M)=*
\quad\text{for all finite }k.
\]

But Miller's theorem makes M itself BZ/p-null, so

\[
P_{B\mathbb Z/p}M\simeq M\ne *.
\]

Thus even the actual convergent identity tower, with connectivity of its
layers tending to infinity, cannot support the desired interchange.
Merely obtaining stronger finite-stage vanishing does not resolve the
test for Y_r.

## 4. No additional periodic or phantom shortcut is being asserted

A finite-stage Hopf-invariant calculation might obstruct a specific
unstable retraction, but the calculation in section 2 shows why it is
insufficient by itself for the nullification problem. Likewise, the
existence of a stable retraction is not an unstable retraction.

The alternative search for a same-Postnikov-types example currently has
no concrete candidate: finite p-homotopy groups eliminate the obvious
inverse-limit ambiguity, and pure GEM models have split restriction
towers. An infinite-rank non-GEM example would require a specific source
and a computable ordinary nullification before it could be used.

The spectral Lie search is handled independently by simple_higher. Its
subsequent colimit-generation proof is recorded in D.2.11; my independent
audit passed the weakly contractible-colimit product argument, the
effective-zero action bar, the simultaneous induction over all loops of
the finite weight tower, and generation by free spheres. Heuts's finite
weight theorem explicitly includes every integer sphere shift. This
supersedes the earlier unproved proposal to realize the weight tower in
ordinary spaces. In particular it does not assume that K(n)-local
spectra have p-primary homotopy groups.

## 5. Gaudens--Schwartz: the exact hypothesis does not apply

Opened the published article, rather than relying on the earlier
preprint:

- G. Gaudens and L. Schwartz, *Applications depuis K(Z/p,2) et une
  conjecture de N. Kuhn*, Ann. Inst. Fourier 63 (2013), 763--772,
  DOI 10.5802/aif.2776,
  https://www.numdam.org/item/10.5802/aif.2776.pdf.
- N. T. Cuong, G. Gaudens, G. Powell and L. Schwartz, *On non-realization
  results and conjectures of N. Kuhn*, Fund. Math. 234 (2016), 139--161,
  DOI 10.4064/fm95-10-2015,
  https://www.impan.pl/shop/en/publication/transaction/download/product/91443.

The 2013 paper, Corollary 2.3, Lemma 2.4 and section 3.3, obtains
increasing connectivity of mapping spaces from smash powers of BZ/p by
combining a nilpotence bound with a finite Krull-filtration bound. It
uses that estimate to extend a specially constructed map from
Sigma^s BZ/p across Sigma^(s-1) K(F_p,2), contradicting a nilpotent-
filtration obstruction.

For the present target Y_r, that finite Krull hypothesis fails at its
first nonzero nilpotent layer. The unstable module H^*K(F_p,2) is reduced
and lies in no finite Krull stage (2013 paper, p. 765 and section 2.3;
the reduced-module statement at odd primes is detailed in the 2016
paper, Proposition 5.6). Consequently

\[
R_{r+1}\widetilde H^*(Y_r;\mathbb F_p)
=\widetilde H^*(K(\mathbb F_p,2);\mathbb F_p)
\]

has infinite Krull degree. Since Y_r is a suspension, its reduced
cohomology has zero products and equals its module of indecomposables.
Thus the profile functions w and q from the 2016 paper are already
infinite at r+1. Neither the bounds in its Theorem 1.4 nor the finite
degree hypothesis in Theorem 1.5 supply the required obstruction.

This source check does not rule out an adaptation using additional
information about the nullification process. It does rule out importing
the existing extension/connectivity argument for Y_r without a new
estimate. No computation of P_{A_r}Y_r is obtained here.

## 6. A concrete bottom-class collapse criterion at the prime two

Opened G. Powell, *Endomorphisms of H^*(K(V,n);F_2) in the category of
unstable modules*, Math. Z. 254 (2006), 55--115, Corollary 3 (primary
preprint, pp. 2--3):
https://math.univ-angers.fr/~powell/documents/2005/indec.pdf.
It proves that the suspension spectrum of K(F_2,n) is atomic.

Consequently, at p=2, suppose that an ordinary map

\[
g:\Sigma A_r\longrightarrow Y_r
\]

induces an isomorphism in the bottom nonzero reduced mod-2 homology
degree r+3. Compose it with the suspended stabilization unit
j:Y_r→ΣA_r. Since j is an isomorphism in this degree, the stable
self-map Σ∞(gj) of Σ∞Y_r is an equivalence by atomicity. The spaces
involved are simply connected and p-primary, so gj is an ordinary
homotopy equivalence. Replacing g by (gj)^{-1}g makes Y_r a retract
of ΣA_r. It follows that Y_r is ordinarily A_r-acyclic, giving
P_{A_r}Y_r≃*.

This is only a sufficient criterion. D.2.12 now proves that no ordinary
map g with that property exists for any r>=1, including arbitrary
higher-weight corrections to the canonical stable retraction. The
converse implication from nullification-acyclicity to such a single
bottom-class map has not been proved.

## 7. A proved unstable obstruction, without a nullification conclusion

The complete proof is in `sections/D2_unstable_obstruction.tex`, authored
by simple_higher after the joint calculation and independent reviews.
It proves, for B=K(F_2,2) and every r>=1,

\[
\widetilde H_{r+3}(g;\mathbb F_2)=0
\quad\text{for every }g:\Sigma Q\Sigma^rB\longrightarrow\Sigma^{r+1}B.
\]

Put X=Sigma^r B and n=r+2. The adjunct has target
H_*(Omega Sigma X)=T(V), where V=H~_*(X) consists of primitive
generators. Serre's low-degree calculation supplies a,b,d in V of
degrees n,n+1,n+3 with

\[
Sq_*^1b=a,\qquad Sq_*^2b=0,\qquad Sq_*^1d=0,\qquad Sq_*^2d=b.
\]

Every c in V_(n+2) has Sq_*^1 c=0. In the homotopy-commutative
source QX, the images of b,d are primitive and satisfy
Sq_*^2(bd)=b^2 and Sq_*^1(b^2)=0. If an adjunct f hits a, it
also hits b. Coproduct naturality on bd, projected to target tensor
length (1,1), forces the coefficient of bb in f_*(b^2) to be one.
But Sq_*^1(bb)=ab+ba, whereas the only other length-two terms in
that degree, ac and ca, have zero Sq_*^1. Steenrod operations preserve
word length, so no cancellation is possible. This contradicts naturality
of Sq_*^1. No H-map hypothesis on f is used.

The original odd-r argument used a primitive Dyer--Lashof class and the
Nishida relation. The b,d calculation extended it to even r; the final
source-commutativity simplification removes the Dyer--Lashof operation
and covers all r uniformly. The earlier argument and primary-source
checks are preserved in `notes/I_unstable_obstruction.md`.

Primary low-degree check: Serre, *Cohomologie modulo 2 des complexes
d'Eilenberg--MacLane*, Comment. Math. Helv. 27 (1953), Theorem 2,
section 2 no. 8, p. 203, and the explicit example in no. 9, p. 204:
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf.
These give H^2=<u>, H^3=<Sq^1u>, H^4=<u^2>,
H^5=<u Sq^1u,Sq^2Sq^1u>. The suspension and Cartan identities are
section 1 nos. 2.2--2.3, p. 199. This primary PDF and its p. 204 image
were opened directly. The saved final proof was independently audited
in full after writing.

This conclusion concerns individual maps from Sigma A_r. It does not
show that Map_*(A_r,Y_r) is contractible, and it does not show that
P_(A_r)Y_r is nontrivial. In particular, no argument currently controls
the new bottom-degree classes and later relations introduced by a
transfinite nullification construction.

## 8. The two precise gaps in propagating the obstruction

First, the contradiction uses that the loop target still has the tensor
Hopf algebra T(V). An attachment could in principle kill the class
ab+ba before a later map kills a. Its vanishing would remove the last
step of the coefficient contradiction. No actual A_r-acyclic attaching
source hitting ab+ba has been constructed; the elementary Samelson map
X smash X -> Omega Sigma X is insufficient because X smash X has not
been proved A_r-acyclic. Conversely, no invariant preserving ab+ba
through all A_r-attachments has been established.

Second, even a successful calculation performed directly on the loop
target would need its nullification index checked. Bousfield1997,
Theorem 5.2, opened again directly at
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf,
gives, for connected Y,

\[
P_A\Omega Y\simeq\Omega P_{\Sigma A}Y.
\]

It does not identify P_A Omega Y with Omega P_A Y. Therefore the
uncomputed comparison from Sigma A-nullification to A-nullification
cannot be omitted if a loop-space calculation is to settle the original
P_(A_r)Y_r question.

## Sources

All sources used in sections 1–3 are already opened and recorded in the
manuscript bibliography: the Snaith splitting; Bousfield ULP Theorem 2.10
and Proposition 3.1; Goodwillie Calculus III Theorem 1.13; Arone–Mahowald
Theorem 2.1; Levy2025 Theorem 3.2; Miller's theorem in the form checked in
Part A. No new theorem from a secondary source is imported.
