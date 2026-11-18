# The connected fibre and the seven-cell relation

GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15 November 2026.

Status at 17:06 UTC: proposed complete calculation, under independent
audit by both axioms and fibrations reviewers. The Chang component
detectors have passed both reviews; the full fibre basis and integral
normalization are receiving a final check. No global extension is claimed.

Update at 17:12 UTC: both independent full audits passed, including the
fibre dimensions, every operation used, the integral normalization and
the absence of a hidden attaching component. The final argument is
being integrated as D.2.18. Use the stable finite-range cancellation
described below, rather than requiring an unstable minimal CW model.

## 1. A three-connected fibre

Put B=K(F2,2), Y=Sigma^2 B and T=Omega^2Y. The fundamental class
Sigma^2u defines Y->K(F2,4); looping twice gives the H-map q:T->B.
The suspension-loop unit j:B->T is a space section, since qj represents
u. If F is the homotopy fibre, multiplication gives an equivalence
B times F -> T, (b,f) |-> j(b)f. The section need not preserve
multiplication. Thus integral and mod-two homology split by Kunneth.
The bottom homology calculation makes F three-connected. Equivalently
it is the three-connected cover of T.

All primitive classes below map trivially under q. The labels in B in
degrees four through seven have no primitive ambiguity that changes
the following fibre table. In these degrees F is three-connected,
so all of its homology is primitive. Its complete mod-two bases are:

| Degree | Fibre basis |
|---|---|
| 4 | A=a^2 |
| 5 | Z=e+ab, U=xi a |
| 6 | b^2, k={a,b}, p=f+ac+a^3 |
| 7 | V=xi b, R={a,c}, P=g+ae+bc+a^2b, Q=h+ad |

Here g,h are the unit labels dual to u^2v and uw. In counting ambient
H7(T), one must include the nonprimitive product a xi a; omission
would give an incorrect fibre dimension.

The exact operations needed are

    beta Z=A,  beta V=b^2+k,  beta P=p,  beta Q=beta R=0,
    Sq2 b^2=Sq2 p=A,  Sq2 k=0,
    Sq2 V=U,  Sq2 P=Sq2 Q=Z,  Sq2 R=0,
    beta2[b^2]=[U].

Thus H4(F;Z)=Z/2, H5(F;Z)=Z/4 and H6(F;Z)=(Z/2)^2.
The finite-type primary torsion condition excludes rational and odd
primary summands. The nonzero first Bocksteins identify the two
order-two summands in degree six, and the nonzero second Bockstein
identifies the order-four summand in degree five.

## 2. The actual six-skeleton

For the group calculation work with the suspension spectrum of a finite
eight-skeleton of F, localized at two. Cancel adjacent sphere cells
whose cellular incidence is odd, hence a unit in Z_(2). This is stable
cell cancellation of an equivalence and preserves the mod-two labels.
Include the eight-cells at this step to remove extra seven-cells killed
by unit incidences. The remaining cell counts through seven equal the
listed mod-two dimensions. Discarding the eight-cells then does not
affect pi6. Freudenthal identifies pi6F with this stable group.

Choose integral cellular bases a4, z5, u5, d6, e6, f6, with

    dz=2a, du=0, dd=4u, de=df=0.

Modulo two the degree-six labels are

    d=b^2, e=b^2+k, f=p.

Every one of d,e,f has Sq2 image A. The five-skeleton is
P^5(2) vee S^5_u. Its pi5 has exactly the degree on S5 and the
bottom eta of P^5(2), so these operations specify all six-cell
attaching maps:

    d: i eta4 + 4u,   e: i eta4,   f: i eta4.

Slide d over e and f over e. The six-skeleton becomes

    C vee M(Z/4,5) vee S6_r,
    C=cofib((2,eta4):S4 vee S5 -> S4),
    r=e+f=b^2+k+p  (mod two).

All possible extra integral unit pairs may be cancelled, and extra
free six-cells are excluded by the already determined mod-two ranks.

## 3. Exact stable Chang group and component detectors

Every six-dimensional homotopy group here is in the stable range,
since these spaces are three-connected. The stable cofiber sequence
for C gives

    pi6(S4 vee S5) -> pi6(S4) -> pi6(C)
       -> pi6(S5 vee S6) -> pi6(S5).

The first map is onto: the eta on the S5 summand carries eta5 to the
nonzero eta4 eta5. The last map sends (epsilon eta5,n) to n eta5.
Consequently the middle quotient map identifies pi6(C) with

    (Z/2){(eta5,0)} plus 2Z{(0,iota6)}.

Write delta and gamma for the respective elements, so gamma has
integral Hurewicz image 2e and projects trivially to S5. Thus

    pi6(C)=Z gamma plus (Z/2) delta.

This derivation uses only pi1^S=Z/2{eta} and the nonzero eta^2;
it does not need an unproved extension in a Moore homotopy group.
Also pi6(M(Z/4,5))=Z/2{t}, where t is bottom eta. Hence

    pi6(F6)=Z gamma plus (Z/2) delta plus (Z/2)t plus Z rho.

An attaching map S6->F6 is determined completely by its integral
degrees on the free H6 generators and the Sq2 values from the two
degree-five classes: Z detects delta and U detects t. This follows
from the displayed injective Chang quotient and the usual cofiber
Sq2 detector of eta. There are no Whitehead terms in this dimension.

## 4. Seven-cell relations and the resulting group

Integral boundaries and the Sq2 table above give the following exact
attaching elements, up to harmless orientation signs:

    V: gamma+t,
    P: gamma+2rho+delta,
    Q: delta,
    R: 0.

The first two boundaries are 2e and 2f=2(e+r). The Sq2 values
distinguish all remaining two-torsion coefficients. Thus

    pi6(F) = (Z/4){rho},
    t=2rho.

Higher cells do not alter pi6. Under F->T, the bottom U class is
represented by the double adjunct of u4 nu4, whose order is four and
whose Hurewicz image is xi a. Therefore t is its eta composite:

    2rho = (u4 nu4)^hat eta5,
    equivalently 2rho^hat = u4 nu4 eta7 in pi8(Y).

Every element with mod-two Hurewicz image r is an odd generator of
this Z/4, so has the same double. In particular the geometric PT
representative from RP3 times RP3 has the required relation.

## 5. Exact intended application

The independently analyzed quotient of the source seven-skeleton by
its bottom Moore four-skeleton has the attaching maps
i eta5+2e and 2z, with possible free seven-spheres. The correction
on its Moore bottom and its e sphere therefore extends precisely
when the relation in Section 4 holds. This would extend the dangerous
six-skeleton pattern to the seven-skeleton. It would not extend it
over the eight-cells or to Q Sigma B. That full-source extension and
the ordinary nullification remain separate undecided steps.
