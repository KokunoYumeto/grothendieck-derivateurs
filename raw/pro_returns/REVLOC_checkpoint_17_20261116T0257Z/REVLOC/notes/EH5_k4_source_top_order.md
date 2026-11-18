# The order of the spherical top-boundary class in the finite relative source

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Proved; complete source-order proof independently
audited by root and axioms_derivators. Final TeX: D.2.38,
sections/D2_fourth_source_order.tex. The final QM refinement was also
independently checked by both readers.

Let D=D_2^(4)M(Z/2,3). The exact cellular chains, Steenrod table and
spherical class Y10=lambda3(A,B) are in EH5_k4_relative_square.md.
All homotopy calculations in this note are stable and 2-local. Since
D is five-connected, its ordinary pi10 is the same group.

**Proved claim.** pi10D is (Z/4)² plus Z/2. Every element whose
mod-two Hurewicz image is Y10 has exact order four. In particular the
actual spherical Y10 obtained by the octonionic Whitehead argument
cannot be chosen to have order two. The full top attaching expression
below retains two possible lower torsion coefficients; no value for
those coefficients is asserted.

## 1. Stable cells through degree nine

Use the minimal integral chain coordinates of the preceding note.
Elementary unit cancellations are performed stably, so a new skeleton
here means a finite CW-spectrum model for D. This avoids claiming an
unstable minimal cell structure merely from chain Smith normal form.

In degrees six and seven let P6 be the bottom class, z7=S7=Q4A, and
c7=R7+S7=AB+Q4A. Thus dz7=2P6 and dc7=0. In degree eight use
U8=Q5A and T8'=B²+Q5A. Their boundaries are 0 and 4c7, respectively,
and their second squares are P6 and 0. There are no other stable
attaching possibilities in this range: pi7M(Z/2,6)=Z/2{i eta6} is
detected by the second square. Hence the eight-skeleton is

    D8 = C vee M(Z/4,7),
    C=Cof((2,eta6):S6 vee S7 -> S6).

The C cells are P6,z7,U8. Write i for its bottom inclusion and q for
its quotient onto S7 vee S8. The direct cofiber calculation already
used in D.2.18--D.2.20, shifted up by two, gives

    pi8C=Z_(2){gamma} plus Z/2{delta},
    q gamma=(0,2),   q delta=(eta7,0),
    gamma eta8=0.

The two degree-nine cells are W9=Q6A and V9=Q5B. Their integral
boundaries are 2U8 and 0, and their second squares are 0 and z7.
The Moore-four summand's possible attaching element in degree eight
is i7 eta7 and is detected by the c7 second-square coefficient, which
is zero for both cells. The torsion delta is detected by z7. Therefore
the two attachments are exactly gamma and delta. Set

    Cb=C union_gamma e9_W union_delta e9_V,
    D9=Cb vee M(Z/4,7).

All references to D9 use this stable cell model, including the unit
cancellation across the raw degree-nine/degree-ten chain pair. The
cancelled pair is not silently retained as an extra nine-cell.

## 2. The required Cb component groups

For clarity the component calculation is reproduced from the earlier
Chang-block proof rather than inferred from a group table. The same
cofiber long exact sequence gives

    pi9Cb=Z_(2){kappa} plus Z/2{v},
    h_Z(kappa)=2V9,   v=i nu6.

Normalize kappa to have Sq4 detector zero; adding v changes exactly
that detector. Its Sq2 detector is U8. This follows from the cone
Bockstein of the degree-two V pinch and Adem, exactly as for kappa'
in EH5_pi8_stable_target.md, Section2.

In the next degree, pi10C is Z/4{omega}, with quotient

    q omega=(2nu7,eta8²),      delta eta8²=2omega.

The eta-images of the two nine-cell attachments are gamma eta=0 and
delta eta nonzero. Their eta²-images are 0 and 2omega. Thus

    0 -> Z/2{omegaBar} -> pi10Cb -> Z/2{zetaBar} -> 0,        (3)

where the right-hand generator is eta on the W-cell, i.e. on the
gamma attachment. The extension in (3) need not be split here.

The precise relation needed below is

    kappa eta9=omegaBar.                                   (4)

It can be checked first in C'=C union_delta e9_V. There
pi10C'=Z/2{omegaBar}. A kappa' with top degree two on V has Sq2
detector U8. After collapsing the bottom S6, the U8 component of
kappa' is eta8, hence its further eta has nonzero eta8² component.
It is therefore omegaBar. Passing to Cb preserves the left subgroup
in (3), because gamma eta²=0. The possible normalization change by
v does not alter (4), since nu eta=0.

The quotient generator zetaBar is detected by Sq2 from its attaching
cone's top class to W9: its quotient is the eta map into that nine-cell.
Any representative from the left subgroup has zero such detector.

## 3. The degree-ten attachments, including the hidden coefficient

Write n=i7 nu7 in pi10 M(Z/4,7), of exact order four. The Moore
coextension calculation gives

    pi9 M(Z/4,7)=(Z/2){i7 eta7²} plus (Z/2){tilde eta},
    pi10 M(Z/4,7)=(Z/4){n} plus (Z/2){t},
    t=tilde eta composed eta9.

The top eta lift tilde eta has order two; this is the same Moore-four
coextension used in D.2.19--D.2.22, shifted by two. The relevant
composition identities are

    v eta9=0,        i7 eta7³=4i7 nu7=0.                    (5)

The two ten-cells are X10=Q6B and Y10=lambda3(A,B). Their integral
boundaries are 2V9 and 0. The first has Sq2=U8 and Sq4=P6. Thus its
attaching map has the exact form

    a_X=kappa+v+epsilon i7 eta7²,        epsilon in F2.      (6)

The eta-coextension component in the Moore-four summand is excluded by
the zero T8' coefficient of Sq2. The primary-invisible i eta² term
is retained in (6). For Y, zero boundary and zero second/fourth squares
leave at most the same i eta² component.

The spherical Y10 proved in the preceding note forces its entire
attaching map to be zero. Here is why no X correction can invalidate
that inference. A stable S10->D can be lifted to the ten-skeleton,
since D has only an eleven-cell above it. Its relative degree vector
on the ten-cells is (a,b). The cofiber exact sequence requires

    a a_X + b a_Y=0 in pi9D9.

The free kappa coefficient of a_X is one, whereas a_Y is torsion,
so a=0. Its mod-two Hurewicz Y coefficient is one, so b is odd.
Multiplication by b is invertible on the 2-local torsion subgroup;
therefore a_Y=0. This proves a genuine stable wedge splitting

    D10=R vee S10_y,      R=D9 union_(a_X) e10_X.            (7)

It is the infinite kappa coefficient, not mod-two sphericity alone,
which excludes an X correction in this argument.

## 4. The exact group below the last cell

In the cofiber sequence for (6), the map
pi9S9=Z_(2)->pi9D9 is injective because of its free kappa component.
Hence pi10R is the quotient of pi10D9 by a_X eta9. Equations (4)--(5)
show that this is exactly the quotient by omegaBar, independently of
epsilon. Thus (3) and the Moore group give an exact direct sum

    pi10R = (Z/2){zeta} plus (Z/4){n} plus (Z/2){t}.        (8)

Here zeta is the image of any lift of the right-hand generator in (3).
Its order is now two because the left subgroup has been killed.
The summands in (8) come from the actual Cb and Moore wedge factors
before the X attachment; no new extension is introduced, since the
right-hand kernel term of the cofiber sequence is zero.

## 5. The last attachment and the order-four conclusion

The integral top differential is 2Y10, so the attaching map of the
eleven-cell has form 2y+z for some z in (8). Its Sq2 vector is W9.
The generator zeta has this detector, whereas n and t belong to the
Moore summand and have no W9 component. The map 2y has zero second
square. Therefore the zeta coefficient is one.

The fourth-square vector of the top is z7=S7, with zero coefficient
on c7. The class zeta has no c7 fourth-square component: it is
represented from Cb, where c7 restricts to zero. The class t factors
through eta on S9, so the natural cone Ceta9, which has no degree-seven
cohomology, shows that its c7 fourth-square coefficient is zero.
The class n has c7 fourth-square coefficient one, by the Hopf invariant
of nu. Consequently its coefficient in z is even. We obtain

    a_top=2y+zeta+2d n+e t,       d,e in F2.                 (9)

No value for d or e is needed. Since every torsion term on the right
of (9) has order two, the quotient gives 4y=0. The element 2y is
nonzero: modulo 2pi10R its value has the nonzero zeta coordinate.
Equivalently eliminating zeta from the presentation gives

    pi10D = (Z/4){y'} plus (Z/4){n} plus (Z/2){t},

after replacing y by y+dn and, if desired, changing the order-two
zeta basis by et. Any element with odd Y10 integral Hurewicz coefficient
has the form odd*y plus an element of (8). Its double still has
nonzero zeta coordinate modulo 2pi10R, and its fourth multiple is zero.
Thus every such spherical representative has exact order four.

This calculation retains the lower torsion terms in (9). In particular
the last cell is not being replaced by a pure degree-two attachment,
and no wedge-of-Moore-spaces conclusion is drawn.

## 6. Source audit, dependencies and scope

The raw configuration model and its complete operation table were
checked against the primary Cohen--Lada--May formulas on printed
pp217--218; the chain model and Smith check are retained in the
preceding note. The shifted Chang and Moore cofiber calculations are
the same explicitly proved calculations in D.2.18--D.2.22 and
EH5_pi8_stable_target.md, with the opened Oka1986 Section2 stable
stems and Moore coextension identities. The spherical-Y construction
uses the actual generalized Whitehead/Browder adjunction and the
octonionic H-space multiplication on S7, not a stable guess.

The only unresolved cell coefficients in this note are epsilon in
(6) and d,e in (9). The group and order conclusions do not depend on
their values. They do not decide the image of the paired functional
under maps D->V or the existence of a full fourth-suspension map.

## 7. Exact refinement: the chosen sphere also dies in QM

The homology class Y10 maps to zero in QM. The generalized Browder
Moore map is null there because stabilization kills its generalized
Whitehead adjunct. The Moore Puppe sequence only implies, in general,
that the chosen top-sphere factor has image in 2pi10(QM). In this
specific degree that group is zero, for an independent low-stem reason.

Write M2=Cof(2:S->S). Then pi10QM=pi7M2. Since 2id_M2 is zero on
the bottom sphere, it factors through the pinch q:M2->Sigma S.
The Moore LES gives pi1M2=Z2{i eta}, so the factor is either zero or
i eta; the stronger familiar equality 2id_M2=i eta q is unnecessary.
For x in pi7M2, qx is in pi6S=Z2{nu²}, and eta nu²=0 since eta nu=0.
It follows that 2x=0 for every x. Thus the actual S10->C4M sphere
used before stable projection has zero image in QM.

Primary source directly reopened and p149 rendered on15 November:
Oka1986, Section2 equation(2.1)(e') eta nu=0, and(2.1)(g)
pi6S=Z2{nu²}; publisher URL:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9BF563A8A92B6BF87DAA39E8DAD092BE/S0013091500017557a.pdf/homotopy-of-the-exceptional-lie-group-g2.pdf

This concerns the actual sphere factor S10->C4M->QM. It does not
turn the stable projection C4M->D into a canonical ordinary map
D->QM. Root and axioms_derivators independently passed the exponent
argument; the final TeX uses the weaker factorization proof above
so no additional unquoted Moore identity is needed.

## 8. The possible arity-three sphere component is zero

Set E3=D_3^(4)M. This weight-three summand is eight-connected.
Its complete mod-two homology basis through degree eleven is

    H9:  A³;
    H10: A²B, A Q4A;
    H11: AB², A Q5A, B Q4A.

Completeness follows directly from the free E4 homology basis:
an indecomposable operation has weight a power of two, so every
weight-three class in this range is a product of weight one and
weight two; the first possible weight-three Browder expression
has degree at least twelve. The available weight-two operations
in degrees at most eight are precisely A², AB, B², Q4A, Q5A.
This uses the same opened CLM ChapterIII basis theorem and Nishida
formulas as D.2.29 and D.2.38, with no infinite-product substitution.

Both degree-ten classes have beta=A³. Among the degree-eleven
classes only B Q4A has nonzero beta, equal to A²B+A Q4A. All three
degree-eleven classes have Sq2=A³, by Cartan and the table (38d).
Consequently the stable ten-skeleton is

    M(Z/2,9) vee S10_c,

where c reduces to A²B+A Q4A. Normalize the unique nonzero
eleven-cell integral boundary to 2c using its odd 2-local unit.
The other eleven-cell boundaries are divisible by four and can
be made exactly zero by even cell slides against that cell.
Such slides do not change their mod-two square vectors. The
AB² cell, for example, therefore attaches as the nonzero bottom
i eta9 in pi10 M(Z/2,9)=Z/2, detected by its Sq2. This kills the
only lower torsion; the remaining relation is 2c. Hence

    pi10 E3 = Z/2{c},

and its mod-two Hurewicz map is injective. Higher cells cannot
affect pi10. Axioms_derivators independently audited this entire
low-cell computation, including the even-slide normalization.

Now take the ACTUAL sphere y0:S10->C4M constructed in Section7
and project it stably to the relative quotient C4M/M. Its homology
is pure weight-two Y10, so the arity-three projection has zero
mod-two Hurewicz image, and is zero by the preceding calculation.
Weights at least four are eleven-connected and also contribute
nothing to pi10. Thus, under the relative Snaith splitting, this
actual sphere's relative stable class is solely its weight-two
component y_D in pi10D. In particular y_D has the exact order four
proved above, and the higher-weight caveat is resolved in this
degree by a computation, not by choice of a nullhomotopy within
filtration two.

If f:QM->U is an ordinary map whose restriction to M is the
canonical dangerous Moore map m, compare its restriction to C4M
with the canonical E4 map g4. Their pointwise difference factors
through C4M/M and lifts to the five-connected cover V. In the
finite dimension-eleven range that lift is equivalent to a stable
map. If v2:D->V denotes its weight-two component, the actual
nullity of y0 in QM and the absence of its higher-weight components
give the exact sphere condition

    (v2)_*(y_D)=-(g4)_*(y0) in pi10U=pi10V.

The target value on the right is not computed here. Nor is this a
condition on every arbitrary map D->V. It is a necessary condition
on maps arising from a putative full extension. The unconditional
paired-functional test on all D->V maps remains sufficient.

## 9. Primary identification of the actual sphere before projection

The original sphere y0:S10->C4M fourfold-adjoints to

    y0_tilde:S14->P8(2)=M(Z/2,7).

Morisugi--Mukai2000, Lemmas2.7 and2.8(ii), printed p523
(PDF index8), directly compute

    pi14 P8(2)=Z4{l4} plus Z2{tilde(nu7²)},
    2l4=i8 sigma',     Sigma l4=i9[iota8,iota8].

Here i8:S7->P8 is the bottom inclusion; sigma' in pi14S7 is
the unstable order-eight element. The nu-squared coextension
pinches to nu8² and therefore remains nonzero after stabilization.
The l4 summand stabilizes to zero because its suspension is a
Whitehead square. Thus the exact stable kernel of pi14P8 is
Z4{l4}.

The preceding sections put y0_tilde in this stable kernel. Its
stable projection through C4M to D has order four, so y0_tilde
cannot be an even multiple of l4. Consequently

    y0_tilde=plus or minus l4.

This proves the ACTUAL sphere has order four as well. It does
not merely infer actual order from its stable D projection.
No extra relative-Whitehead coefficient calculation is needed:
the primary group and its exact stable kernel suffice. The paper
also records j*l4=[gamma8,iota7] in the relative Moore pair.

Let h_M:P8->Y be the restriction of the actual generalized
Whitehead unit h0 of D.2.29, and let g4=Omega4 h_M. Its value on
the actual sphere is therefore exactly

    (g4)_*(y0)=plus or minus h_M l4 in pi14Y=pi10U,
    2(h_M l4)=(h_M i8) sigma'=(-2alpha) sigma'.

The target composite h_M l4 has not been evaluated. Bilinearity
of the generalized Browder product shows only that its underlying
Moore-map factor is zero and hence that this value is a double
in pi10U; it does not determine the doubled-sphere ambiguity.

Source audit: the primary J-STAGE PDF was reopened and page523
rendered. Its Lemmas2.7/2.8(ii), full proof, and the preceding
definition V_(2n+1),2=P^(2n) union_(l_n) e^(4n-1) were checked.
URL: https://www.jstage.jst.go.jp/article/jmath1948/52/3/52_3_515/_pdf
Existing bibliography key EH5MorisugiMukai2000 has been updated
with this exact passage. Axioms_derivators independently opened
the same page and checked the stable-kernel identification.

## 10. The target value is a double: a weaker sufficient target test

Write m:M(Z/2,3)->U for the canonical dangerous Moore restriction.
Its bottom is -2alpha, with alpha in pi3U=Z/4 and
alpha eta3=2rho in pi4U=Z/4. The actual Moore Puppe sequence
factors 2id_M through i eta3 q (or through zero); this is within
the stable range of maps M->M. Hence

    2m=(m i) eta3 q=-4rho q=0.

The E4 generalized Browder map on the bottom and the full Moore
restriction is lambda3(-2alpha,m). Bi-additivity gives

    lambda3(-2alpha,m)=-2lambda3(alpha,m)
                     =-lambda3(alpha,2m)=0.

All relevant input desuspensions for the corresponding generalized
Whitehead product, S6 and Sigma3M, are suspensions. Therefore the
precise primary bi-additivity hypothesis is satisfied: Arkowitz1962,
Proposition3.4, printed p14, reopened in the original publisher PDF.
The group structures are identified under the fourfold adjunction.

The chosen top sphere value g4(y0) therefore belongs to 2pi10U
by the actual Moore Puppe sequence. This does NOT assert it is zero;
Section9 identifies it as plus or minus h_M l4 and retains its
genuine doubled-sphere ambiguity.

For a relative difference v2:D->V arising from a full extension,
Section8 now implies

    (v2)_*(y_D) belongs to 2pi10V,
    (v2)_*(Y10)=0 in H10(V;F2).

Here pi10V->pi10U is an isomorphism, so the double lifts as a
double. This restricts the ACTUAL differences under consideration;
it need not hold for an arbitrary map D->V.

Consequently the following target identity would already suffice
for paired-coefficient rigidity of full extensions:

    mu11|V belongs to
       beta H10(V;F2) + Sq3 H8(V;F2) + Sq5 H6(V;F2).       (10)

Indeed beta Z11=Y10, while Sq3_* Z11=Sq5_* Z11=0 by the
complete source table. Every beta term evaluates to zero by the
new fixed-sphere Hurewicz condition, and the other two summands
evaluate to zero directly. This is weaker than the unconditional
test on all D->V maps, whose sufficient primary relation did not
include beta H10. No relation (10) has been proved.

