# The exact low-cobar test for a simultaneous first attachment

**Status, 2026-11-15, 18:41 UTC.** The algebraic and cochain criteria below
are proved. They do not assert that every first nullification attachment
passes the criterion. In particular the fourth-suspension calculation
currently remains open, and the earlier proposed ratio between its Hopf
and linear coefficients was corrected by the fibrations agent. No
iteration or nullification-survival conclusion is made here.

All (co)homology in this note has coefficients in the field F_2. Spaces
and wedges are small CW spaces; there is no finite-type hypothesis in the
conclusions. Put

    B = K(F_2,2),   X = Sigma B,   Y = Sigma X = Sigma^2 B,
    A = QX,        T = Omega^2 Y.

The old loop-homology letters a,b in this note have degrees 3,4 in
H_*(Omega Y). Thus they are the homology suspensions of the degree-2 and
degree-3 B-labels called a,b in the double-loop calculations. Write

    kappa = ab+ba in H_7(Omega Y).

The old cohomology classes are u in H^4(Y) and v=Sq^1 u in H^5(Y).
The same letters u,v used for their unsuspended B-classes in other notes
are shifted here; all degrees are stated explicitly to remove that
ambiguity.

## 1. The exact low-cobar injection

For every 3-connected CW space C, define

    W(C) = (H_4 C tensor H_5 C) direct-sum
           (H_5 C tensor H_4 C).

Let Delta_9 be the reduced homology diagonal H_9 C -> W(C). These are
all its possible reduced components in degree nine, by 3-connectivity.
There is a natural injective map

    W(C) / image(Delta_9)  -->  H_7(Omega C).                 (1)

Its map before taking the quotient is the Pontryagin product of the
canonical desuspensions H_4 C = H_3(Omega C) and
H_5 C = H_4(Omega C). In particular this is a statement about the actual
product in loop homology, not just an associated graded group with a
possible extension left undecided.

### Proof

First take C of finite type. A minimal Adams--Hilton model over F_2 is
(T(V),d), where V=s^{-1} H~_*(C), every generator has degree at least
three, d has no linear part, and its quadratic part is the desuspension
of the reduced homology diagonal. These precise properties are stated
in Halperin--Lemaire, Section 3.1, printed p.300.

All products V_3 V_4 and V_4 V_3 are cycles. In degree seven they are
exactly the length-two words; words of length at least three start in
degree nine. A degree-eight chain is a sum of a generator in V_8 and
length-two words. Each letter in a length-two word of degree eight has
degree at most five and has zero differential, since any decomposable
differential has degree at least six. Consequently its differential is
zero. The differential of V_8 has degree seven and is exactly its
quadratic part: no word of length at least three can occur there.
It is Delta_9, after desuspension. Thus the intersection of all
boundaries with V_3 V_4 + V_4 V_3 is precisely image(Delta_9).
This proves (1). The definition by the actual Pontryagin product proves
its naturality, independently of choices of minimal model.

For arbitrary C choose a CW model with no positive-dimensional cells
below dimension four, and write it as the filtered union of its finite
subcomplexes. All those subcomplexes are 3-connected. Homology, tensor
products over a field, the diagonal, and its image/cokernel commute with
this filtered union. Loop-space homology does also: a finite singular
cycle, a finite chain bounding it, and their adjoints use compact
parameter spaces and therefore factor through a finite CW subcomplex.
Taking the filtered colimit of the natural injective maps (1) proves
the assertion without a cardinality restriction. This argument also
explains why the finite-type convention in the cited source causes no
gap here.

## 2. Exact criterion and a useful sufficient cup-product test

Let h:S -> Y be a pointed map from a 2-connected CW space, and let
C=Y union_h CS. Suppose h_* is zero in homology degrees four and five,
as it is for every first A-attachment in the present problem. Then C is
3-connected and the old H_4(Y),H_5(Y) inject into those of C. Denote
their images by a_4,b_5. Naturality in (1) gives the exact criterion

    kappa survives in H_7(Omega C)
    iff a_4 tensor b_5 + b_5 tensor a_4
         is not in image(Delta_9).                          (2)

This remains the exact criterion when new low homology is created.
Testing just one coefficient of a general vector in image(Delta_9)
is then insufficient: a relation may identify the old commutator with
another nonzero commutator rather than kill it.

Choose any lift alpha in H^4(C) of u. Then beta=Sq^1 alpha is a lift of
v. If

    alpha beta = alpha Sq^1 alpha = 0 in H^9(C),             (3)

the functional alpha tensor beta annihilates image(Delta_9), but has
value one on the old tensor in (2). Therefore (3) implies survival.
If H_4(C),H_5(C) are precisely the one-dimensional old groups, (3)
is also necessary: cocommutativity makes every Delta_9 image a multiple
of that tensor. This particular simplification applies to wedges of
attachments Sigma^k A -> Y with every k>=2, because their sources have
no homology in degrees three and four.

The product in (3) does not depend on the chosen lift. More generally,
the image of the connecting map H^{j-1}(S)->H^j(C) annihilates positive
cohomology of C. To see this directly, use the ordinary coaction

    C -> C wedge Sigma S.

Projection to the first summand is homotopic to the identity, and
pullback from the second summand is the connecting map. A product of
positive-dimensional classes supported on the two different wedge
summands is zero. Pulling it back proves the annihilator statement.
The difference of two lifts is a connecting-image class. Thus all
products of lifts of fixed positive-dimensional classes from Y agree.
This is a statement about lifts in one fixed cone; it does not remove
the simultaneous-attachment issue below.

## 3. An exact cochain formula, valid also for unsuspended sources

Fix cocycles a in C^4(Y), b in C^5(Y) representing u,v, and choose
c in C^8(Y) with

    dc = a cup b.                                          (4)

Such c exists because Y is a suspension. For h:S->Y with h^*u=h^*v=0,
choose p in C^3(S) with dp=h^*a. Set

    theta_h = [h^*c - p cup h^*b] in H^8(S).                (5)

In characteristic two the minus sign equals plus; it is retained to
show the differential cancellation. Formula (4) and the Leibniz rule
show that (5) is a cocycle. If p is changed by a closed 3-cochain z,
the change is z cup h^*b. Since h^*b is exact, this is exact. Hence
theta_h is independent of p. Changing c by a closed 8-cochain changes
theta_h by h^* of its cohomology class. The same a,b,c will always be
used for every attaching map in a simultaneous collection.

Let delta:H^8(S)->H^9(C) be the cofiber connecting map. For arbitrary
lifts alpha,beta of u,v, respectively, the exact identity is

    alpha beta = delta(theta_h).                           (6)

Here is a direct proof using the actual singular cup product. Work in
a mapping-cylinder cone model with an open cover U,V, where U retracts
to Y, V is contractible, and W=U intersection V is a collar S times
an interval. The retraction r_U can be chosen so that its restriction
to that collar is h after projection to S. The small singular-chain
complex C_*(U)+C_*(V) includes quasi-isomorphically in C_*(C), by
ordinary subdivision. Its dual retains the actual Alexander--Whitney
cup: all faces of a simplex contained in one cover member remain in
that member. There is a short exact sequence of cochain complexes

    0 -> C^*small(C) -> C^*(U) direct-sum C^*(V)
                       -> C^*(W) -> 0,                    (6a)

with the last arrow the difference of restrictions. Surjectivity is
literal: a functional on the singular simplices in W extends to those
in U. This is the ordinary Mayer--Vietoris cochain sequence.

Choose cocycles representing alpha,beta that restrict on U exactly to
r_U^*a,r_U^*b. Such representatives exist: starting with arbitrary
cocycles with the prescribed restricted cohomology classes, extend
the correcting cochains from U to the small-chain complex and subtract
their coboundaries. On V the first cocycle is dP for a 3-cochain P,
since V is contractible. The actual cup product alpha cup beta has
primitive r_U^*c on U and primitive P cup beta on V, by the Leibniz
rule. Their difference on W is therefore the representative in (6a)
whose connecting class is alpha beta. Pull back along a fixed collar
section i:S->W and set p=i^*P. Then dp=h^*a and that difference pulls
back exactly to h^*c-p cup h^*b. This proves (6). No multiplication on
an abstract mapping-cone DGA, strict-unit assertion, or omission of
a cup-i correction is involved: all products above are restrictions
of the same actual singular Alexander--Whitney product.

Taking beta=Sq^1 alpha is permitted, since that is one of the lifts of
v and the product is independent of the lift, as proved above.

## 4. Simultaneous attachments require one common factor

Let S be the small wedge of spaces S_i, and h the map specified by
h_i:S_i->Y. Assume every h_i is zero on H_4 and H_5. Then

    H_8(S) = direct-sum_i H_8(S_i),
    H^8(S) = product_i H^8(S_i).

With the fixed common a,b,c of (4), the class in (5) is the tuple
theta=(theta_{h_i})_i. By (6) and the cofiber exact sequence,

    alpha Sq^1 alpha = 0 in H^9(C)
    iff theta is in image[ h^*:H^8(Y)->H^8(S) ].             (7)

Equivalently, there must exist ONE linear functional
ell:H_8(Y)->F_2 such that, simultaneously for every i,

    theta_{h_i}(z) = ell((h_i)_* z)
    for all z in H_8(S_i).                                 (8)

Equivalently again, the functional theta on the direct sum must vanish
on the whole kernel of h_*:H_8(S)->H_8(Y), including all finite-support
cancellations between different summands. These equivalences use the
universal coefficient isomorphism over a field and extension of a
functional from a vector subspace. They require no finite-dimensional
or countability hypothesis.

It is not enough that each theta_{h_i} separately belongs to
image((h_i)^*:H^8Y->H^8S_i). That permits a different functional ell_i
for every i. The target primitive c in (4) is common, so those separate
normalizations cannot be made independently in the common cone.
For example, in pure linear algebra take two one-dimensional source
groups with generators z_1,z_2 mapping to the same nonzero f in
H_8(Y), but with theta(z_1)=1 and theta(z_2)=0. Both individual kernels
are zero, whereas z_1+z_2 is in the simultaneous kernel and has theta
value one. This is an illustration of the exact obstruction; no claim
that these two matrices are realized by actual A-attachments is made.

## 5. Suspended sources: the once-adjoint gives the exact common factor

Suppose now every S_i=Sigma R_i, where R_i is 2-connected, and every
h_i induces zero homology in degrees four, five, and six. This includes
all maps Sigma^k A->Y with k>=1 by D.2.12. Write

    bar h_i:R_i -> Omega Y

for the ordinary adjunct. The Bott--Samelson/James identification is

    H_*(Omega Y) = T(V),  V = H~_*(X),  |V|>=3,
    H_7(Omega Y) = V_7 direct-sum F_2{ab,ba},
    V_7 = H_8(Y).

The images of H_3(R_i),H_4(R_i),H_5(R_i) under bar h_i are zero:
in these degrees the homology suspension is an isomorphism onto
H_4(Y),H_5(Y),H_6(Y), respectively. All V-letters are primitive
because X itself is a suspension. Coalgebra naturality therefore
forces the ab and ba coefficients of bar h_i(z), z in H_7(R_i),
to agree: the only potentially nonzero reduced target coproduct in
that degree has bidegrees (3,4) and (4,3), and both source factors map
to zero. Thus define actual functionals L_i by

    (bar h_i)_*(z) = (h_i)_*(sigma z) + L_i(sigma z) kappa,
    L_i:H_8(S_i)->F_2.                                    (9)

The first term in (9) is placed in the fixed James word-length-one
summand V_7. This fixes the normalization for all maps at once.

For the simultaneous cone the following is now an exact, necessary
and sufficient criterion:

    kappa survives in H_7(Omega C)
    iff L=(L_i)_i vanishes on ker[h_*:H_8S->H_8Y]
    iff L_i = ell (h_i)_* for ONE ell in H^8(Y).            (10)

### Direct Adams--Hilton proof of (10)

The opened proof of Halperin--Lemaire, Proposition 7.4, printed p.309,
gives the relative model for the cone of a map whose source is an
AH-suspension. Here both Y and S are suspensions. With
W=H~_*(wedge_i R_i), it is

    AH(C) = (T(V direct-sum sW), D),
    D|V=0,   D(sw)=(bar h)_*(w) in T(V).                   (11)

This is the actual loop-chain model. It is not necessary to assume
that the algebraic quotient by the displayed boundaries is a model
in all degrees: the following degree calculation uses (11) itself.

The old V-generators have degrees at least three; the new sW-generators
have degrees at least four. The differentials of new generators of
degrees four, five and six are zero by the low homology assumptions
and the absence of decomposable words in the respective output degrees
three, four and five. Every length-two chain of degree eight has only
such letters (or old letters with zero differential), so its
differential is zero. A new generator of degree seven cannot occur
in a decomposable chain of degree eight, since the other letter would
have to have degree one. Words of length at least three have degree
at least nine. Consequently all degree-seven boundaries are exactly
the images D(sW_7), and these are precisely (9).

The old kappa is a cycle. It is a boundary if and only if a finite
linear combination of the vectors (9) has zero V_7 component and
nonzero kappa component. This is exactly the negation of (10).
The argument remains valid even when k=1 creates new H_5(C) classes:
possible mixed old/new degree-seven words are cycles, and no
degree-eight decomposable chain can create an additional boundary.

For infinite wedges and non-finite-type spaces use filtered finite
subpairs in the cone construction. A finite set of source cycles and
a potential boundary uses only finitely many cells and finitely many
wedge summands. Enlarge the finite target subcomplex to contain the
finitely many chains witnessing the assumed low homology vanishing.
Thus the finite-type relative models prove the same degree-seven
criterion for every finite witness. Filtered passage then proves
(10) as stated. Equivalently, the cellwise construction of (11) is
compatible with these filtered unions.

Formulas (7) and (10) are compatible. Indeed for the whole suspended
source wedge and any z in ker h_*, a lift of z to H_9(C) has quadratic
diagonal given by (9), by the quadratic-differential assertion in
Section 3.1 of the primary source. Pairing with alpha tensor beta
gives L(z). Formula (6) and the connecting pairing give theta(z).
Hence theta-L vanishes on the whole ker h_*, and thus is the pullback
of one common H^8(Y) class. The cochain normalization can consequently
differ from the fixed James normalization only by that common
pullback, which does not change the common-factor condition.
For an unsuspended k=0 source, use the cochain criterion (7) or the
full tensor criterion (2); do not use (11) without proving that its
AH-suspension hypothesis holds.

## 6. Current scope of the attachment calculations

* k=2: D.2.24 proves L_i=0 on the entire input, not merely on an
  individual homology kernel. Its possible linear f image does not
  affect this exact zero statement.
* k=3 and k=5: the fibrations agent has separate exact-zero proofs.
* k>=6: H_8(Sigma^k A)=0, so the relevant input is absent.
* k=0,1: owned by the axioms agent; no completed elimination is used
  in this note.
* k=4: the corrected low top image in T is t k + epsilon r, with
  k={a,b} in double-loop degree six and r=b^2+k+p_3. Its once-adjoint
  commutator coefficient is t+epsilon and its linear f coefficient
  is epsilon. The provisional formula t b^2+epsilon r was false.
  In particular t=1,epsilon=0 would already be individually dangerous;
  neither its realization nor its exclusion is asserted here.

Even exact vanishing for every first attachment would establish only
a first-cone invariant. The loop homology, Steenrod operations, and
available source restrictions change after that cone. No unchanged
operation table, automatic second-cone persistence, or nonzero final
nullification follows from this note.

## 7. Primary-source audit

Halperin, Stephen, and Jean-Michel Lemaire, *The fibre of a cell
attachment*, Proceedings of the Edinburgh Mathematical Society 38
(1995), 295--311, DOI 10.1017/S001309150001909X; existing bibliography
key `FGHHalperinLemaire1995`.

Primary full text opened directly on 2026-11-15:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/51067699B6F3ADA6EAFB4AFFA43A3F85/S001309150001909Xa.pdf/fibre_of_a_cell_attachment.pdf

Exact passages checked: the ground-field/finite-type convention on
printed p.295; Section 3.1 on p.300 (minimal tensor model, linear
homology identification, quadratic differential, and cell attachment);
the suspension assertion on p.301; and the complete proof of
Proposition 7.4 on p.309 (relative cone model for an AH-suspension
source). The paper explicitly treats arbitrary characteristic,
including characteristic two. Its finite-type convention is addressed
by the filtered arguments above. Web references from this agent are
turn1190view0 and turn1191view0. No characteristic-zero Lie model is
being substituted for this associative mod-two argument.

The cochain and common-factor proofs in Sections 3--4 are written
out here; they invoke only ordinary cofiber/Mayer--Vietoris cochains,
Leibniz, the coaction, and linear algebra. The exact first-stage
geometry and source degrees, not a spectral-sequence convergence
guess, give the required conclusion.

## 8. Exact universal normalization of the secondary cup class

**Added 18:50 UTC.** This identifies the class required by the
axioms agent's delooping calculation; it does not prove its pullback
along every attaching map is zero.

Let q:Z->Y be the homotopy fiber of the map u:Y->K(F_2,4), in a
path-space model over Y. The previous low homotopy calculation gives
pi_4(Y)=Z/2 with u inducing an isomorphism, and pi_5(Y)=0. Thus Z is
5-connected. Moreover Omega²Z is the fiber F of
Omega²Y->K(F_2,2), with exactly the inclusion used in D.2.18--D.2.24.

Keep the single fixed cochains a4,b5,c8 of (4). Choose p3 on Z with
dp3=q^*a4 and define the actual class

    Theta = [q^*c8-p3 cup q^*b5] in H^8(Z).                (12)

Here q^*b5 is exact as well. The proof of (5) shows that (12) is
independent of p3. For any h:S->Y with h^*u=0, choose a lift
h~:S->Z using a nullhomotopy of u h. In the path-space fiber model
q h~=h strictly. Pulling back (12) and using (5) gives

    theta_h = h~^* Theta.                                 (13)

The right side is independent of the lift: either lift supplies
one of the permissible p3 cochains in (5), whose class was proved
independent. Thus this is an ordinary universal cohomology class,
not a family of secondary operations with separately chosen values.

Double cohomology suspension H^8Z -> H^6F is an isomorphism. One
may see this without an uncertain spectral-sequence range: Omega Z
is 4-connected, and the minimal AH generators for Z start in degree
five, so the degree-seven homology of Omega Z is precisely H_8Z.
The minimal AH generators for Omega Z start in degree four, so the
degree-six homology of F is precisely H_7(Omega Z). In each case
both decomposables and their possible incoming differentials lie
strictly above the degree in question. Dualizing over F_2 gives the
stated isomorphism, in fact with the natural homology suspensions.

Let epsilon:Sigma²F->Z be the ordinary double-loop counit. Its
composite h=q epsilon has double adjunct the inclusion F->T.
On H_6F use the established basis

    d6=b²,  e6=b²+{a,b},  f6=p3=f+ac+a³.

Once homology-suspending this inclusion sends these classes to
0,kappa,the linear f-letter, respectively. Therefore, for h,

    L_h(d6)=0, L_h(e6)=1, L_h(f6)=0,
    h_*(d6)=h_*(e6)=0, h_*(f6)=f in H_8Y.                (14)

The source is a double suspension; its only possible degree-six
homology image also vanishes, since homology suspension kills the
product A4=a² in H_4F. Thus all hypotheses of Section 5 apply.
The exact equality theta_h-L_h in image(h^*) now gives

    sigma² Theta = e6^* + lambda f6^*                   (15)

for some lambda in F_2. The other old degree-eight Y-class pulls
back to zero. Choose an old class f^* in H^8Y dual to the indicated
f homology label, and replace the ONE common primitive c8 by
c8+lambda f^*. This changes Theta by lambda q^*f^* and removes
the last term of (15). Since double suspension is an isomorphism,
the normalized Theta is exactly the unique class called theta8
in Section 4 of FGH_D2_first_cone_low_suspensions.md.

This establishes that that delooped e6^* class is the universal
secondary cup functional for all first attachments simultaneously.
It uses the exact coefficient equality of Section 5, not merely
an equivalence between two vanishing tests. A proof that its
pullback to every suspension of A vanishes is still required.
