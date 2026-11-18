# First-cone exponents zero and one: exact reductions and remaining boundary

Status update: 15 November 2026, 19:47 UTC. Section 6 completes the
exponent-zero vanishing with one common normalization; this is D.2.27,
including simultaneous mixtures with exponents two/three/at least five.
Section 7 gives D.2.28: the exponent-one full-source functional has only
the coefficient epsilon alpha3 beta4 left. D.2.30 constructs an actual
epsilon-one map through the source ten-skeleton, but its full extension
remains undecided. The older boundaries below are retained to make the
proof development reviewable. D.2.24 settles exponent two; D.2.25 settles
exponent three and every exponent at least five. Exponent four has the
fixed-canonical result D.2.29 and the actual spherical indeterminacy in
FGH_D2_k4_spherical_indeterminacy.md; no all-choices result follows.

Write B=K(F2,2), X=Sigma B, A=QX, Y=Sigma²B. Coefficients are F2
unless explicitly marked integral. In this note L=Omega Y is the ONCE
looped space; it must not be confused with T=Omega²Y.

## 1. Compatible lifts do not create a choice ambiguity

For every mapping cone C_f of f:S->Y, the image of the connecting map

    delta:H^{*-1}(S)->H^*(C_f)

annihilates all positive-dimensional reduced cohomology of C_f. One
proof uses the standard cone-pinch coaction

    C_f -> C_f wedge Sigma S.

Its first projection is homotopic to the identity, and its second
projection is the cone quotient. Pull back a mixed product from the
wedge, where that mixed product is zero. In particular products of
two connecting-image classes are zero as well.

Consequently, if alpha4 on Y extends to C_f, the product

    alphaHat Sq1(alphaHat)

is independent of the chosen compatible lift alphaHat. Replacing it
by alphaHat+delta(u) changes Sq1(alphaHat) by delta(Sq1 u), and all
three additional products vanish by the preceding argument. This
applies to a small simultaneous wedge of attachments as a single S.

This removes lift dependence, NOT the product itself. In particular,
cup-zero on every individual cone does not imply cup-zero on the
simultaneous cone. The latter requires one common old H8(Y) class to
account for the entire tuple of relative Hopf functionals. The exact
cochain formulation is being written in I_low_cobar_first_cone.md.

## 2. An exact once-loop relation

The James--Bott--Samelson tensor algebra is

    H_*(L)=T(V), V=H~_*(Sigma B),

and every letter is primitive. Use lowercase letters a3,b4,c5 and
capital D6,E6,F7,X7,G8,H8,I9,J9,L9 for the suspended base labels.
The underlying B labels are those used throughout D.2.17--D.2.25.
Let K7 be the cohomology functional dual to the WORD ab (zero on
every other tensor word and every linear label), and let P9 be dual
to the word aD. Then there is an identity in the FULL cohomology:

    Sq4 K7 + Sq2 P9 = 0 in H11(L).                    (1)

Indeed the words of length two in degree eleven are

    aG,aH,Ga,Ha,bF,bX,Fb,Xb,cD,cE,Dc,Ec.

Cartan and the base table show that the coefficient of ab in Sq4
is one exactly on bX,cD. The coefficient of aD in Sq2 is likewise
one exactly on bX,cD. Positive squares preserve tensor-word length,
so linear labels and words of length at least three contribute to
neither functional. This proves (1) without a primitive-only or
untested-complement qualification.

The required base identities are beta b=a, Sq2 c=a, beta X=D+E,
Sq2 X=c, Sq3 X=b, Sq2 D=b, Sq2 E=0. They follow from Serre's
opened polynomial algebra F2[u2,v3,w5,t9,...], v=Sq1u,w=Sq2v,
and Cartan. No map is assumed to preserve products or Dyer--Lashof
operations merely because its source and target are H-spaces.

## 3. What (1) presently proves for exponent one

For h:Sigma A->Y, take the once-adjoint phi:A->L. D.2.12 forces
zero images in degrees three, four and five. All relevant images
through degree seven are therefore primitive. Naturality of beta,
Sq2 and the exact second Bockstein gives

    phi(D)=phi(E)=0,       phi(A0²)=0,
    coefficient_[a,b] phi(F)=0.

Here A0 is the bottom degree-three class of A, and [a,b]=ab+ba.
For clarity, before using beta2 one obtains

    phi(D)=phi(E)=x E+y a².

The unit H8 has beta H8=0 and Sq2 H8=E. In the primitive target
degree-eight basis G,H,[a,c],b², the only beta-preimages of the
commutator are b². A beta-cycle cannot contain b², hence y=0.
The unit G8 satisfies beta G8=F and Sq2 G8=E, which then excludes
a commutator coefficient in phi(F). Finally beta2[D]=C5 in A,
whereas beta2[E]=c5 in L; phi(C5)=0 forces x=0.

The three still-unexcluded commutator coefficients occur on

    X7, R7=Q4 A0, and A0 B0.

Relation (1) links these to higher primitive coefficients but does
not yet make them zero. For example, on the unit class dual to w²,
it gives

    coefficient_[a,b] phi(X7)
      = coefficient_[a,D] phi(L9).

On Q8 A0, ordinary Nishida in the E-infinity SOURCE gives

    coefficient_[a,b] phi(Q4 A0)
      = coefficient_[a,D] phi(Q6 A0).

These are source identities followed by natural Steenrod operations;
they do not assert Dyer--Lashof naturality of phi.

For the product coefficient, (1) on A0 H8 gives zero [a,D]
coefficient in phi(A0 E6). Meanwhile beta(A0 X7)=A0(D6+E6),
so the remaining coefficient is the coefficient of [a,X]+[b,D]
in phi(A0 X7). The current primitive/primary calculations do not
exclude that coefficient. No exponent-one vanishing follows yet.

## 4. A rigorous twofold delooping of the Psi relation

Put Z=fib(Y->K(F2,4)), where the map represents the bottom class
alpha4. Since pi4Y=Z2 and pi5Y=0, Z is five-connected. Let
W=Omega Z, so W is four-connected and Omega W=F, the
three-connected fiber used in D.2.18--D.2.25.

There are unique classes theta8 in H8(Z) and lambda10 in H10(Z)
whose twofold cohomology suspensions are respectively e6* and J1*.
Here e6=b²+{a,b}, J1={a,d}, and the stars mean the specified
dual basis functionals, not arbitrary lifts.

The low path-fibration proof is explicit. For the path fibration
F->PW->W, the only differential before transgression out of H8F
is

    d5:H8F -> H5W tensor H4F.

The action of Omega W on the path fibration identifies its dual
with multiplication of the transgressed bottom class by the bottom
fiber class: the bottom tensor maps to the Pontryagin product
A4²=W8. Thus ker d5 is exactly the W8-annihilator. The targets of
d6,d7,d8 vanish by connectivity. The d9 transgression identifies
this kernel with H9W, since no earlier mixed differential enters
that base group. J1* annihilates W8 and hence lifts uniquely.
In the path fibration W->PZ->Z, the cohomology suspension
H10Z->H9W is an isomorphism: its first possible mixed total degree
is eleven. The lower e6* lift is in the ordinary isomorphism range
of both suspensions.

The kernel of the double cohomology suspension

    H12Z -> H11W -> H10F

is exactly the span of the square of the bottom class v6 in H6Z.
For the first path fibration, the only mixed source which can
enter H12Z before its transgression is bidegree (6,5), and its
image is H6Z·H6Z. For the second, the only such sources into
H11W are (6,4) and (5,5), whose images lie in H5W·H6W.
Cohomology suspension kills decomposables, so these descriptions
give the exact kernels. Its image in H11W is primitive for the
loop multiplication. All H5W and H6W classes are primitive by
connectivity. On their mixed products the reduced coproduct is

    x5 y6 |-> x5 tensor y6 + y6 tensor x5,

which is injective on the mixed-product subspace because the two
bidegrees differ. Thus that second decomposable kernel has zero
intersection with the first suspension image. Finally H6Z is
one-dimensional, so the first decomposable kernel is specifically
a square, rather than an arbitrary mixed product.

The proved full-fiber identity Psi_F=Sq4 e6*+Sq2 J1*=0 therefore
implies the actual relation

    Sq4 theta8 + Sq2 lambda10 = epsilon v6² in H12Z, (2)

for some epsilon in F2. Its value is unnecessary when pulling back
along a map A->Z: H_*(Q Sigma B) is polynomial on primitive
generators, so all positive-dimensional cup squares in H*A are
zero. Thus the pulled-back right side of (2) vanishes.

No assertion is yet made that theta8 is precisely the chosen
secondary cup functional for every cone. That identification must
track the lift A->Z and the common nullhomotopy on Y. Nor has (2)
yet forced theta8 to pull back to zero. These are the actual
remaining exponent-zero issues, and the initial tensor model must
not be silently assumed to survive subsequent attachments.

## 5. Exact scope

The algebraic relation (1), compatible-lift independence, and low
delooping statement (2) are proved reductions. The simultaneous
first-cone theorem and persistence through iterated nullification
remain open. A later proof must either produce one common relative
cup cocycle or prove the full commutator functional identically zero;
separate cone-by-cone choices are insufficient.

## 6. Completed exponent-zero argument with explicit witnesses

The identification left open in Section 4 is now proved using
D.2.26j. Write q:Z->Y, fix the SAME cocycles a4,b5,c8 on Y with
dc=a cup b, and choose P3 on Z with dP=q*a. Then

    Theta8=[q*c-P cup q*b] in H8Z.

Every map h:A->Y has a fiber-model lift h~:A->Z, and its exact
cochain Hopf functional is h~*Theta. Changing that lift or P does
not change this class: the change is a closed degree-three class
times the exact pullback of b. Evaluate Theta along the counit
epsilon:Sigma²F->Z. Its once-adjunct into Omega Y has images

    d6 |-> 0,   e6 |-> ab+ba,   f6 |-> the linear f label.

The exact per-vector AH/MV comparison D.2.26j therefore says
sigma²Theta=e6*+lambda f6*. The image of sigma²q*:H8Y->H6F is
exactly span(f6*). Changing c by that ONE old H8Y class normalizes
Theta to theta8 of Section 4. The isomorphism sigma²:H8Z->H6F
shows equality on Z, rather than merely equality on the evaluation
map. This fixes the common normalization once for every h.

For every lift h~, equation (2) now gives

    Sq4(h~*theta8)+Sq2(h~*lambda10)=0 in H12A,              (3)

because its right side is a positive cup square in H*A. The image
of Sq4_* on ker(Sq2_*:H12A->H10A) is ALL of H8A. Here are five
explicit witnesses, independently checked by Cartan and Nishida.
The H8A basis is

    Q5 A0, A0 C5, H8, G8, B0²,

where A0=Sigma a2, B0=Sigma b3, C5=Sigma c4,
G8=Sigma(dual u²v), H8=Sigma(dual uw). In the following list each
source has degree twelve and has zero second square:

* Q7 C5 has fourth square Q5 A0. Nishida has only the t=2 term,
  since beta C5=0 and Sq2 C5=A0. Its second-square leading
  coefficient is binomial(5,2)=0 modulo two.
* A0(I9+J9), with I9=Sigma(dual u4), J9=Sigma(dual uv²), has
  fourth square A0 C5. Both I9 and J9 have second square F7,
  so their sum has zero second square.
* The unit class Sigma(dual u t) has fourth square H8 and second
  square zero. Here t=Sq4w. Cartan gives Sq4(uw)=u t, while
  no degree-nine monomial has second square containing u t.
* The SUM of unit classes Sigma(dual u4 v)+Sigma(dual u3 w)
  has fourth square G8 and second square zero. Precisely,
  Sq4(u²v)=u4v+v²w and
  Sq2(u³v)=u4v+uv³+u³w; the two indicated coefficients have
  identical second-square images and only the first has a G8
  fourth-square coefficient.
* D6² has fourth square B0² and second square zero, since
  beta D6=0 and Sq2 D6=B0.

For the two unit witnesses, the complete degree-nine cohomology
basis is u³v,u²w,v³,t. Their second squares are respectively

    u4v+uv³+u³w,   v²w,   v²w,   0.

The complete degree-seven basis is u²v,uw, with fourth squares
u4v+v²w and u t. Thus there are no omitted unit coefficients.
The E-infinity source formulas above are legitimate Nishida
identities inside A; no arbitrary h is assumed to preserve Q.

Pairing (3) with each witness forces h~*theta8 to vanish on the
displayed entire H8A basis. Hence theta_h=0 for EVERY ordinary
h:A->Y, with the one fixed c8 normalization. A small simultaneous
wedge of such attachments has the zero tuple of Hopf functionals,
so the common-factor issue is resolved for that whole exponent-zero
family. This does not settle exponent one or four, and it does not
assert that the relation survives subsequent cone stages.

Root independently computed the same full source rank in
code/D2_Qsource_primary.py, checking the primitive polynomial and
Dyer--Lashof basis through degree twelve plus beta² and Adem. The
five hand witnesses above give a standalone proof of the particular
surjectivity assertion used here.

## 7. A further exact relation kills the entire exponent-one unit part

Put W=Omega Z and write theta7=sigma(theta8), lambda9=sigma(lambda10).
Let R8* be the unique cohomology lift of the functional dual to
R7={a,c} in F. In this range cohomology suspension H8W->H7F is
an isomorphism, and H9W->H8F is injective. The complete low F table
gives

    Sq2(e6*)=J1*+J3*,      Sq1(R7*)=J3*.

Consequently there is an exact identity on W:

    lambda9 = Sq2(theta7)+Sq1(R8*).                       (4)

Suspending (2) once kills its square term. Substituting (4) and
using Sq2 Sq2=Sq3 Sq1 gives the actual relation

    (Sq4+Sq3 Sq1)(theta7)+Sq2 Sq1(R8*)=0 in H11W.        (5)

This argument does not model H11W by its indecomposable quotient;
the kernel/product issues in that degree are bypassed completely
by the already proved delooped relation.

For ANY ordinary pointed map g:Sigma B->W, write

    g*theta7 = a Sigma(u³)+b Sigma(v²),
    g*R8* = c Sigma(u²v)+d Sigma(uw).

The complete Cartan calculations are

    (Sq4+Sq3 Sq1)(u³)=u5,
    (Sq4+Sq3 Sq1)(v²)=w²,
    Sq2 Sq1(u²v)=0,
    Sq2 Sq1(uw)=w²+u²v².

For the first identity, Sq4u³=u5+u²v², while
Sq3 Sq1u³=Sq3(u²v)=u²v². The last uses
Sq1(uw)=vw+uv² and Sq2(vw+uv²)=w²+u²v².
Pulling back (5) yields

    a Sigma(u5)+(b+d) Sigma(w²)+d Sigma(u²v²)=0.

The three displayed monomials are linearly independent. Therefore
a=b=d=0. In particular g*theta7=0 on the ENTIRE unit Sigma B,
without requiring an extension to A first.

For a full map g:A->W, the four-dimensional H7A has basis
Q4 A0, A0 B0, Sigma(dual u³), Sigma(dual v²).
The unit result kills the latter two coefficients. The source
class Q6 C5 has Sq2=0 and Sq4=Q4 A0 by Nishida, so the suspended
Psi relation kills the first coefficient as well. Thus the exact
remaining possibility is

    g*theta7 = epsilon alpha3 beta4,
    alpha3=Sigma u, beta4=Sigma v=Sq1 alpha3.             (6)

This is a reduction, NOT an exponent-one vanishing theorem.
The module calculation in code/FGH_k1_primary_module.py first
found this constraint and retains a certificate, but (4)--(6)
give the complete hand proof of the new unit vanishing.

An earlier exploratory beta argument must not be reused:
Sq1(J1*) is NOT zero, because beta K3=J1 in H9F. Thus there
is no claim that Sq1 lambda9 is just a bottom-square ambiguity.
The exact identity (4), which uses beta R7*=J3*, is the valid
replacement.

For completeness, the binary-deviation test alone still permits
the residual epsilon in (6). On X smash X=Sigma²(B smash B),
the induced theta class has the symmetric form

    epsilon Sigma²(u tensor v+v tensor u).

Equation (5) admits the R8 pullback

    epsilon Sigma²(u tensor u²+u² tensor u).

Indeed its first square followed by its second square equals
the fourth square of the preceding symmetric class. This is
only algebraic compatibility and is not a realization assertion.
