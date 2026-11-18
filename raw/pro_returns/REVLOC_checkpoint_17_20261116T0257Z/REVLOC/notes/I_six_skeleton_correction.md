# A finite correction of the low Hopf coefficient

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15.

Status update, 2026-11-15 16:57 UTC: the primitive class
r=b^2+{a,b}+f+ac+a^3 is now proved actually spherical, using the
Akhmetiev--Repovs--Skopenkov framed embedding described in Section 7.
Together with the explicit free-six-sphere choice in Section 8, this
realizes the dangerous low pattern s=1, gamma=0, epsilon=1 on a finite
six-skeleton. Root, the axioms agent, and the fibrations agent have
independently audited the relevant steps. The older unresolved wording
in Sections 4--5 records the preceding stage and is superseded by
Sections 7--8. No extension over the seven-cells or the full infinite
loop space has been proved.

Later update, 17:25 UTC: D.2.18 computes the exact target group and
extends this chosen pattern over the seven-skeleton. D.2.19 computes
the next target group and extends it over the eight-skeleton. The
historical six-dimensional construction below is retained unchanged;
the next live obstruction is the nine-cell calculation in
notes/I_nine_cell_source.md. No full-source map has been constructed.

## 1. Conventions and the canonical nonzero s

Put B=K(F2,2), X=Sigma B, A=QX, Y=Sigma^2B, and T=Omega^2Y.
Let A0=σa, B0=σb, C=σc be the source classes in degrees3,4,5,
where a,b,c are dual to u,v=Sq1u,u^2 in H^*B. For a map into T,
s is the coefficient of a^2 on B0 and gamma is the coefficient of
xi a on C. The canonical map on the second loop stage is

    g2 = Omega^2(eta2 smash id_B) : C2 X -> T.

Its unit restriction g0 has s=gamma=1. The value gamma=1 is proved
in D.2.13. Here is the explicit check of s, which must not be omitted.
Let x be dual to v^2 and X7=σx. The cofiber CP^2 smash B makes the
quadratic once-adjoint image on σ^2x equal to (σb)^2. Its linear part
vanishes, and tensor length three starts in degree9, above this degree8
calculation. The primitive degree-seven target basis is

    xi b, {a,c}, P=g+ae+bc+a^2b, Q=h+ad,

where g,h are dual to u^2v,uw. Their homology suspensions are respectively
bb, ac+ca, σg, σh, which are linearly independent. Thus the primitive
suspension kernel is zero and g0(X7)=xi b. Exact top Nishida gives
Sq3_*(xi b)=a^2, while Sq3_*X7=B0. Therefore g0(B0)=a^2.
The axioms agent independently rechecked this entry.

The exact primary interfaces are Halperin--Lemaire1995, Section3.1
p300 and the proof of Proposition7.4 p309, together with CLM1976,
ChapterIII Theorems1.3--1.4 and3.1--3.2. These are the already opened
sources in D.2.13 and the low E2 audit.

## 2. A six-skeleton of A and its quotient

The map C2X -> A is seven-connected. Indeed Sigma^2X is four-connected;
Freudenthal makes its stabilization unit nine-connected, and looping
twice leaves connectivity seven. Subsequent stages improve this bound.
A relative CW model may therefore be chosen with no new cells below
dimension eight. Its six-skeleton K may be taken from C2X, and g2 gives
an actual map K -> T.

The four-skeleton K4 is the bottom Moore M(Z/2,3). In particular,
H4(K4;Z)=0. The quotient K/K4 has cells only in dimensions five and
six, and is four-connected. Moreover

    H5(K/K4;Z) = H5(K;Z) = H5(A;Z) = H4(B;Z) = Z/4.

The second equality is unaffected by cells of dimension at least seven.
The third uses the configuration filtration/Snaith splitting: all weights
at least two begin in degree six for X. The last follows from the
classical order-four calculation, explicitly identified by Mahowald1964
p1340 as H^5(B;Z)=Z/4, together with the integral universal coefficient
theorem and the finite torsion homology of B.

A four-connected six-dimensional CW complex is determined here by the
degree matrix of its six-cell attachments to a wedge of five-spheres.
Cell slides and Smith normal form therefore give

    K/K4 ~ M(Z/4,5) vee (a finite wedge of six-spheres),

after removing contractible cell pairs. Extra six-sphere summands are
allowed and are not silently discarded in the extension problem.
Projection to the Moore summand sends C to its bottom generator.

The opened primary stable-splitting source is Snaith1974, Theorem1.1
and Section2:
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Snaith-split.pdf

## 3. A four-torsion class that changes gamma

Let u4:S4 -> Y be the bottom map. By Hurewicz, pi4Y=Z/2 and 2u4=0.
Let nu4:S7 -> S4 be the quaternionic Hopf map, with Hopf invariant one.
Set alpha=u4 nu4. The Hopf--Hilton formula gives

    0=(2u4)nu4=2alpha+[u4,u4].

Bilinearity gives 2[u4,u4]=[2u4,u4]=0, so 4alpha=0. The formula can
be obtained directly by decomposing the pinch of nu4 into its two
sphere components and the single Whitehead-product component in
pi7(S4 vee S4); the latter coefficient is its Hopf invariant one.
There are no higher-weight components in this dimension. The quadratic
formula and its composition interpretation are also recorded in Baues1996,
(8.2)(4), (8.4), and Lemma8.5, pp4756--4757:
https://www.maths.ed.ac.uk/~v1ranick/papers/baues2.pdf

The double adjunct alphaBar:S5 -> T has mod-two Hurewicz image xi a.
One direct verification uses the cofiber HP^2 of nu4: its bottom
cohomology generator has nonzero square, so the once-adjoint image is
the square of the degree-three loop generator. Homology suspension
sends xi a to that square and has zero kernel in degree five in
Omega^2S4. Naturality under u4 gives the stated image in T.
This is the same Hopf-invariant/relative Adams--Hilton interface used
for the canonical eta calculation.

Since 4alphaBar=0, alphaBar extends over M(Z/4,5). Compose such an
extension with K -> K/K4 -> M(Z/4,5), and call the result f:K -> T.
It is zero on K4, hence leaves B0 unchanged, and f_*(C)=xi a.
Pointwise addition in the H-group T now gives

    g' = g2|K + f,
    g'_*(B0)=a^2,     g'_*(C)=0.

The source classes B0,C are primitive, so the homology calculation of
the pointwise sum has no cross terms. This proves the finite partial-map
statement. It is not a global correction factoring through a finite
sphere or a finite Moore space.

## 4. Exact boundary of the construction

Extending g' over the seven-cells is unresolved. Its obstruction includes
the image of the eta attachment on the bottom five-cell, hence may involve
alphaBar eta5, equivalently u4 nu4 eta7 in pi8Y. Other components and
choices of images for the six-cells must be retained. No reduction to
this one composition has been proved.

Differences of two extensions over a fixed Moore M(Z/4,5) factor through
a six-sphere. The only mod-two primitive degree-six target class allowed
by Sq2-annihilation and the second Bockstein is

    r=b^2+{a,b}+p3,   p3=f+ac+a^3.

Indeed neither b^2+{a,b} nor p3 is separately Sq2-annihilated; both have
Sq2 image a^2, which cancels in their sum. Thus one may not decide the
dangerous epsilon merely by changing a top-cell extension unless r is
actually in the image of pi6T -> H6T. That spherical-image question is
being checked independently. The general full-map low-table formulas
also use seven-dimensional source relations, so they must not be imposed
on an arbitrary six-skeleton map without their extension hypotheses.

## 5. The linear f class is stably spherical

A blanket stable-Hurewicz exclusion of r is impossible. The ordinary
Hurewicz image of r after two homology suspensions is the class f dual
to u^3 in H6(B;F2). This class is stably spherical.

Take the closed framed six-manifold M=RP^3 x RP^3. Each RP^3 is the
Lie group SO(3), hence parallelizable; their product admits a framing.
Write x,y for the degree-one mod-two generators of its two factors.
Choose the map M -> B classifying xy in H2(M;F2). Then

    <(xy)^3,[M]> = <x^3 y^3,[M]> = 1.

Pontryagin--Thom followed by this label map and the projection to the
reduced suspension spectrum of B gives a stable class in pi6^s(B)
whose Hurewicz pairing with u^3 is one. The reduction from B_+ to B
does not change this positive-degree pairing.

This proves stable realization only. It does not give a codimension-two
framed embedding, nor a lift to pi8(Sigma^2B). The underlying framed
bordism class can be altered by a constant-label framed component without
changing the reduced B class, so the underlying Kervaire/nu^2 component
alone cannot be used as a desuspension obstruction. The actual labeled
metastable/EHP obstruction remains to be computed.

## 6. Huang--Wu source boundary

The primary Huang--Wu paper was opened at
https://arxiv.org/pdf/1706.02916 . Its Theorem1.5/5.5 and Lemma5.4 give
vanishing Toda-indeterminacy and shuffle composites with a filtered
evaluation map. Proposition1.6/6.7 applies to maps in the image of a
specified Cohen-group representation and proves their loops null.
It does not state that every ordinary map C4X -> T belongs to that image.
No application to the remaining arbitrary-map coefficient has therefore
been asserted.

## 7. Positive spherical update: an actual rank-two framing

Akhmetiev--Repovs--Skopenkov, Embedding products of low-dimensional
manifolds into R^m, Topology and its Applications 113 (2001), 7--12,
Theorem 1.1 and its proof on printed page 9, explicitly construct an
embedding (RP^3)^2 x I^2 -> R^8. Restriction to the central slice gives
M=(RP^3)^2 an actual trivial rank-two normal bundle. Its framed
Pontryagin--Thom collapse, followed by the map M -> B classifying xy,
therefore gives an actual map S^8 -> Sigma^2 B. Its mod-two Hurewicz
image is precisely Sigma^2 f: the two degree-six cohomology basis
classes are u^3 and v^2, and their pullbacks evaluate respectively as
x^3y^3 (value one) and x^4y^2+x^2y^4 (zero).

The double adjunct rho:S^6 -> T has primitive Hurewicz image. The
primitive degree-six basis is b^2, k={a,b}, p3=f+ac+a^3. Sq2 sends b^2
and p3 to a^2 and sends k to zero. The second Bockstein sends the E2
classes of b^2 and k to xi a, whereas p3 is a first-Bockstein boundary.
A spherical class is annihilated by both operations, and its double
homology suspension is f. These conditions force its image to be
exactly r=b^2+k+p3. This is an unstable realization, not merely the
stable realization of Section 5.

Primary full text independently opened by all four agents:
https://www.academia.edu/18703053/Embedding_products_of_low_dimensional_manifolds_into
DOI 10.1016/S0166-8641(00)00021-3. The shared bibliography key is
EH5AkhmetievRepovsSkopenkov2001. Full geometric audit and an integration
paragraph are in notes/EH5_degree8_spherical.md and
notes/EH5_degree8_geometry.md.

## 8. Explicit choice realizing the dangerous six-skeleton pattern

Write D=Sigma d and E=Sigma e for the degree-six source classes, and
A0^2 for the weight-two degree-six class. In the quotient K/K4 the
classes D and E both project to the mod-two top class of M(Z/4,5):
their second Bockstein is C. Their difference D+E lifts an integral
free six-cycle. It is independent of the free cycle A0^2. Choose the
Smith-normal-form splitting so the projection q to M(Z/4,5) sends
D,E to its top class and kills the free classes D+E,A0^2. Choose a
free-six-sphere projection l with l(D)=0, l(E)=1, l(A0^2)=0. Additional
free six-spheres can be sent to the basepoint. This free-sphere choice
is explicit; no relation involving the seven-dimensional source
class is used to assert that an arbitrary six-skeleton map has it.

Let alphaBar:S^5 -> T be the four-torsion Hopf class of Section 3,
whose Hurewicz image is xi a. Any extension over M(Z/4,5) sends its
top class to k+t r for t in F2: primitivity, Sq2-annihilation, and
beta2(top)=bottom give exactly these two choices. Composing the
top-cell coaction with rho toggles t, so choose an extension mu with
top image exactly k. Then the map

    G = g2|K + mu q + rho l : K -> T

has the following exact mod-two values:

    G(A0)=0,  G(B0)=a^2,  G(C)=0,
    G(D)=b^2+k,  G(E)=b^2+k+p3=r,  G(A0^2)=0.

Here g2 has values D -> b^2 and E -> k, mu q sends both D,E to k,
and rho l sends only E to r. The relevant source classes are
primitive, so pointwise addition introduces no cross terms. The
canonical map g2 is an E2 map and kills A0, hence also A0^2; both
corrections kill the chosen A0^2 sphere. Thus this is an actual
six-dimensional map with the dangerous low pattern, not just a
compatible linear assignment.

The construction imposes the free-six-sphere value needed for the
full-source low equations, but it does not prove extension across
any seven-cell. The actual seven-cell attaching maps, integral
orders and divisibility of the chosen spherical correction remain
to be analyzed. In particular no nullification survival or collapse
claim follows from this finite-stage realization.
