# An actual spherical change of the fourth-suspension coefficient

15 November 2026, 19:33 UTC. Research note. The actual sphere and the
relative eleven-skeleton indeterminacy below are proved. Extension of the
modified choice over all of `C_4 X`, or over `QX`, remains undecided.

Put `B=K(F_2,2)`, `X=Sigma B`, `Y=Sigma^2 B`, and
`T=Omega^2 Y`. All homology in this note is mod two unless marked
otherwise. Retain the established classes

\[
 k=\{a,b\},\qquad p_3=f+ac+a^3,\qquad
 r=b^2+k+p_3\in H_6T.
\]

D.2.17--D.2.18 construct an actual element
`rho:S^6 -> T` with Hurewicz image `r`; its homotopy order is four.
Write `rhoTilde:S^8 -> Y` for its double adjunct. The construction of
the sphere below needs the existence and Hurewicz value, not the order.

## 1. The actual sphere

Let `sigma_8:S^15 -> S^8` be the octonionic Hopf map, of Hopf invariant
one. Form the actual composite

\[
 S^{15}\xrightarrow{\sigma_8}S^8
       \xrightarrow{\widetilde\rho}Y.
 \tag{1}
\]

Its double adjunct `s:S^13 -> T` has Hurewicz image

\[
 h(s)=\xi_1(r)\in H_{13}T.
 \tag{2}
\]

Here is the exact Hopf-invariant interface. The once-adjoint of
`sigma_8` has Hurewicz image `z_7^2` in the James tensor algebra
`H_*(Omega S^8)=T(z_7)`: the coefficient of this quadratic word is
the Hopf invariant, as follows equivalently by applying the quadratic
Adams--Hilton differential/cup-product identification to its mapping
cone. The group `H_13(Omega^2 S^8)` is one-dimensional on
`xi_1 z_6`. Homology suspension sends this generator to `z_7^2`.
Consequently the double adjunct of `sigma_8` has image `xi_1 z_6`.
The map `Omega^2 rhoTilde` is an actual double-loop map, so it preserves
the top operation and sends `z_6` to `r`. This proves (2).

No Dyer--Lashof compatibility is being imposed on an arbitrary map
from `C_4X`; it is used only for the specified double-loop map in
this construction.

## 2. The coefficient detected by D.2.29

Let `ell` denote the coefficient of the independent outer restricted
square `xi_1 k` in the free `E_2` polynomial basis of `H_13 T`.
Then

\[
 \ell\bigl(\xi_1r\bigr)=1.
 \tag{3}
\]

Indeed, top additivity gives

\[
 \xi_1r=\xi_1(b^2+k)+\xi_1p_3+\{b^2+k,p_3\}.
\]

The top Cartan identity gives `xi_1(b^2)=0`: the two identical
product terms cancel in characteristic two and the possible bracket
term contains `{b,b}=0`. Also `{b^2,k}=0` by the derivation law.
Thus `xi_1(b^2+k)=xi_1k`.
The expression `xi_1p_3` uses only the labels `a,c,f`, and therefore
cannot contain the independent Hall word involving `b`, followed by
an outer restricted square. The last summand has an outer ordinary
bracket; the restricted-Lie reduction identity retains ordinary Hall
words and products and cannot produce an outer `xi_1k`. This proves
(3) in the complete basis, not only after homology suspension.

In particular, the fact that `xi_1 k` itself is not a first-Bockstein
boundary does not make its coefficient zero on spherical classes.
The spherical class in (2) is a combination with coefficient one;
this note does not assert that `xi_1 k` alone is spherical.

## 3. What this changes on an actual relative skeleton

Let `U=Omega^4Y`, and take the fourfold adjunct of (1),

\[
 \psi:S^{11}\longrightarrow U.
\]

Its twofold homology suspension satisfies

\[
 \ell\bigl(\sigma^2 h(\psi)\bigr)=1.
 \tag{4}
\]

Replace the unit `X -> C_4X` by a relative CW model and let
`K=X union (relative cells of dimension at most 11)`. Start with the
restriction of the canonical map `g_4:C_4X -> U` of D.2.29.
The class `Q^7 B_0` has nonzero image in `H_11(C_4X,X)`:
the free `E_4` basis separates this weight-two operation from the
weight-one unit image. It is represented in `K`, and its relative
cellular cycle has some odd coefficient on an eleven-cell.

Change the filling of that eleven-cell, relative its boundary, by
the actual element `psi in pi_11 U`. This produces an actual map
`K -> U`, unchanged on `X` and on every relative cell of dimension
at most ten. The standard cell-pinch coaction shows that its value
on the chosen homology cycle changes by `h(psi)`. Therefore the
coefficient in (4), applied to `Q^7B_0`, toggles. The change is
ordinary and cellular; no multiplicativity is assumed.

This is a full indeterminacy at the relative eleven-skeleton.
It does not construct a map on the entire `C_4X`. The changed
eleven-cell fillings can have new obstructions on the twelve-cells
and beyond. In particular the top Bockstein of `Q^7 B_0` in the
finite `E_4` source contains its Browder correction; that higher
attachment is not removed by this construction. Any all-choices
nonextension theorem must control these higher compatibility
conditions, rather than assume that the D.2.29 coefficient is
already fixed by the unit or by lower-cell data.

## 4. Primary-source audit and dependencies

* Hatcher, *Algebraic Topology*, Example 4.47, printed pp.378--379,
  explicitly constructs the octonionic Hopf bundle. Section 4.B,
  printed p.427, gives the Hopf-invariant-one statement from the
  cohomology of the octonionic projective plane. Both exact passages
  were opened on the author's site on 15 November 2026:
  <https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf> and
  <https://pi.math.cornell.edu/~Hatcher/AT/ATch4.4.pdf>.
  Existing bibliography key: `FGHHatcher2002`.
* Cohen--Lada--May, *The Homology of Iterated Loop Spaces*, Chapter
  III, Theorems 1.2--1.4, printed pp.216--219, supplies the top
  additivity, Cartan, restricted-bracket and homology-suspension
  identities; Theorems 3.1--3.2 supplies the free `E_2` basis. The
  primary scan and the rendered pp.217--218 are already retained
  in the source audit. Existing key: `I_CohenLadaMay1976`.
* The quadratic Adams--Hilton/cup-product interface is the same
  opened Halperin--Lemaire Section 3.1 used in D.2.26; no new
  comparison theorem is assumed.
* Actual `rho` and its Hurewicz value are D.2.17--D.2.18. The
  canonical obstruction whose indeterminacy is analyzed is D.2.29.

Root independently found the same composite (1). This note records
the finite-skeleton consequence and its precise unresolved boundary.

## 5. The paired coefficient and the cancelled higher-Bockstein lead

The same spherical change has coefficient one on the independent outer
restricted square `xi_1 f`, because `p_3=f+ac+a^3`. Thus its outer-square
coefficient vector `(xi_1k,xi_1f)` is `(1,1)`, whereas the canonical
value of D.2.29 is `(1,0)`. Every full extension would make both
coordinates zero, since neither independent outer square can be a
first-Bockstein boundary. The sum of those coordinates is therefore a
better candidate invariant, but its rigidity is not proved here.

The tempting second-Bockstein test does not establish that rigidity.
Already in T, the proposed value `{k,xi_1a}` is a first-Bockstein boundary:

    beta {b,{a,k}} = {a,{a,k}} = {k,xi_1a}.

The fibrations agent subsequently constructed the relevant boundary
inside the actual four-connected cover E, using a universal mixed
Browder source. Taking two more adjoints through its seven-connected
mixed fiber also supplies the corresponding boundary in U=Omega²E.
The exact universal construction and source audit are retained in the
fibrations note; axioms independently checked both connectivity ranges
and the equality with the internal E4 bracket via the common fourfold
Whitehead adjunct. Thus no nonzero higher-Bockstein value is being
asserted either before or after these homology suspensions.

## 6. The connected-cover cup test and its exact remaining boundary

15 November 2026. The mod-two product calculation below has been
independently audited by the fibrations agent. It is a further test of
the paired coefficient, not a proof that the coefficient is rigid.
Write E=Omega²Z′ for the four-connected cover of F, with Z′ the
six-connected cover of Y, and W′=Omega Z′. The established low cover
basis is

    H5E=<u>, H6E=<D,E6>, H7E=<S,R>,
    D=k, E6=b²+p3, S=xi b+P+Q.

The low suspension maps identify these with the generators in degrees
7,8,9 of Z′, respectively. Their once-suspended images in the James
tensor algebra H_*(Omega Y) are

    u6 -> aa,
    D7 -> ab+ba,
    E7 -> f,
    S8 -> bb+g+h,
    R8 -> ac+ca.

Here the letters on the right are suspended labels; their degrees are
3,4,5,7,8 as appropriate. The eight ordered products of total degree
fourteen are

    uS, Su, uR, Ru, D², DE, ED, E².

Their target images are linearly independent. Successive distinguishing
words may be taken as aa g, g aa, aaac, caaa, abab, abf, fab, ff.
Thus there is no relation among these products in H14(W′).

In a minimal mod-two Adams--Hilton model of the six-connected space
Z′, the bottom generators have degree six. A generator of degree
fifteen has differential of degree fourteen, so its only possible
terms have word length two and degree splittings 6+8 or 7+7. The
eight products just listed exhaust them; word length three starts in
degree eighteen. Their independence therefore makes the quadratic
differential zero. The usual quadratic differential/reduced-diagonal
identity shows that all cup products

    H7(Z′;F2) H9(Z′;F2),  H8(Z′;F2) H8(Z′;F2)

vanish in H16(Z′;F2). This calculation uses the complete low basis,
not an assumption that the connected cover is a co-H-space.

The integral class relevant to the paired coefficient is

    x8=beta_4(u7),  red_2(x8)=D8*+E8*.

It has order four. Its square reduces to zero by the preceding
calculation, but this DOES NOT prove x8²=0 integrally. The exact
low integral AH pattern explains the possible problem. In suitable
coordinates it has generators u6,d7,r7,s8 with

    d(d7)=4u6,  d(r7)=0,  d(s8)=2r7.

Then d(d7²)=4(u6 d7-d7 u6). An additional generator v14 with
d(v14)=2(u6 d7-d7 u6) permits the integral cycle d7²-2v14.
Such a correction is compatible with the actual mixed Browder
Bockstein boundary of Section 5. Consequently one cannot discard
even integral square terms just because the mod-two quadratic
products are independent. This paragraph describes the unresolved
possibility; it does not assert that this integral square is nonzero
in the actual target.

Every sphere S15->Z′ lifts to the seven-connected cover Z″, since
the removed Postnikov stage is K(Z/4,7). The class x8 restricts to
zero on Z″. Its bottom quadratic Hopf contribution is therefore the
already known diagonal xi(r). There can still be a linear H15(Z″)
contribution to the pulled-back paired functional. Neither its
integral Hurewicz image nor the integral lift of that functional has
been determined here. This is the precise remaining interface in
this connected-cover approach.
