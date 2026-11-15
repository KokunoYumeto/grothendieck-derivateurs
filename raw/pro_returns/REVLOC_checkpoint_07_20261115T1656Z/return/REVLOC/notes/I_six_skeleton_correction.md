# A finite correction of the low Hopf coefficient

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15.

Status: the finite six-skeleton construction below was independently
checked by root and the axioms agent. It proves a finite partial-map
statement only. It does not produce a map on the full infinite loop
space, does not select the dangerous epsilon coefficient, and does not
settle the seven-cell obstruction.

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
