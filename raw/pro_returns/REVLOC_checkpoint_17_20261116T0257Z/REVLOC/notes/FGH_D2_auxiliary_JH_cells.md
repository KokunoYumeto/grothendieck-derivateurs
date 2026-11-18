# Auxiliary James--Hopf target: proposed finite cell matrix

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. The complete calculation in Sections4--8 has now
independently passed root and the fibrations reader. It is formalized
as D.2.60 in sections/D2_auxiliary_hopf_twelve.tex. Sections1--3 retain
the discovery-stage labels and are superseded by the signed integral
matrix in Section4. The conclusion is survival through the actual
twelve-skeleton only; the cells in dimensions13--15 remain uncomputed.

**02:24 update.** Sections 4--8 supply the missing integral normalization
and a proposed complete survival argument through all twelve-cells.
The quotient detector in Section 6 has independently passed the
fibrations reader. The combined source matrix and resulting conclusion
are submitted for a separate full audit; no numbered result is used
before that audit. Sections 1--3 retain the original working labels.

Put Z=Sigma³(B smash B), B=K(F2,2). Use homology labels a2,b3,c4,
d5 dualw,e5 dualuv,f6 dualu³,x6 dualv². The relevant operations are
beta b=a, beta x=d+e, Sq2c=a, Sq2d=b, Sq2x=c; the other operations
needed below vanish. Tensor labels are ordered; all displayed mod-two
cell names are suppressed Sigma³ shifts.

## Chosen nine-stage

Use B8=ab, e8=ba-ab. Let D9=ac, r9=ca-ac, m9=bb-ac.
The complete nine-stage is C1^9 on (aa,B,D), M2,8 on (e,m), and S9_r.
The Chang generators in pi9 are gamma (h=2D) and delta (Sq2=B).
The Moore-bottom eta has Sq2=e. These, and the free r, form the
complete pi9 of the wedge; there is no mixed Whitehead in this range.

## Ten-cells, with even integral normalization required

Raw ad,ae,da,ea need NOT be integral cycles. For example d(ad)=4ac;
subtracting twice the bc ten-cell makes it a literal zero-boundary
cycle without changing its mod-two label. Make these parity-preserving
corrections first, and use AD,AE,DA,EA below for the corrected cells.
The two remaining boundaries bc,cb are 2D and 2(D+r).
The complete primary/integral data give the proposed attachments

    AD: delta                 AE: 0
    DA: delta+e eta            EA: 0
    BC: gamma+delta+e eta      CB: gamma+2r+delta.

Here Sq2(ad)=ab, Sq2(da)=ba, Sq2(bc)=ba, Sq2(cb)=ab; ae,ea have
zero second square. Row changes isolate delta, e eta, gamma, 2r,
and two zero cells. Thus the proposed actual ten-stage splitting is

    Z10 = Cb9 vee C1^10 vee M2,9_r vee S10_AE vee S10_EA,
    Cb9=C1^9 union_delta e10_Q union_gamma e10_G.

Write V10=DA-AD for the C1^10 top, and Q10=AD for the delta cell.
The Cb9 free pi10 generator kappa has h=2Q, Sq2=D, and can be
normalized to Sq4=0 by adding the bottom nu class v=i7 nu7.
The Sq2 coordinate follows directly from Adem applied to the cone:
Sq2Sq2(a7)=Sq3Sq1(a7), beta(top)=Q and Sq2Q=B8. This is the shifted
same Cblock calculation used in D38. The other pi10 coordinates are
free gamma-prime with h=2V and Sq2=0, delta-prime with Sq2=m9,
r eta9 with Sq2=r9, and the two free ten-sphere inclusions.
Consequently the full pi10 has free rank four and three order-two
coordinates v,delta-prime,r eta9; their Sq4/Sq2 detectors are complete.

## Proposed eleven-cell matrix

The nine mod-two labels are AF,AX,FA,XA,BD,BE,DB,EB,CC.
Their first Bocksteins in the corrected ten-basis are

    0, Q+AE, 0, Q+V+EA, Q, AE, Q+V, EA, 0.

Their Sq2 vectors are

    0, D, 0, D+r, D+m, 0, D+m, 0, r,

and only CC has nonzero Sq4, equal to aa.
Integral Kunneth gives H7(B smash B;Z)=(Z2)^4; hence the incoming
integral eleven-boundary lattice is 2 times the four free ten-cycle
lattice. One must explicitly choose parity-preserving cellular
normalizations realizing the preceding Bockstein vectors before using
the following complete-detector matrix:

    AF: 0
    AX: kappa+2AE
    FA: 0
    XA: kappa+gamma-prime+2EA+r eta9
    BD: kappa+delta-prime
    BE: 2AE
    DB: kappa+gamma-prime+delta-prime
    EB: 2EA
    CC: v+r eta9.

All possible pi10 torsion directions are represented by the three
listed primary detectors. If the integral normalization is confirmed,
ordinary cell slides isolate kappa, v, delta-prime, gamma-prime,
r eta9, 2AE, 2EA and two zero cells. This suggests the splitting

    Z11 = (Cb9 union_kappa e11 union_v e11)
          vee Cb10 vee C1^11 vee (M2,10)^2 vee (S11)^2.

This is a working deduction, not yet used to claim survival through
twelve. The remaining bottom-factor pi11, its free top-degree-two
nu lift, and the full twelve-cell integral attachment lattice must be
computed before asserting that the bottom i7 sigma-prime survives.
In particular a single 2p_aux nu class has nonzero top pinch4nu;
only a combination canceling all top pinches can be an old-bottom
relation. The isolated top-eight comparison does not substitute for
that complete intersection calculation.

## 4. Literal integral normalization and the actual eleven-stage split

Choose the low integral cellular chains of B with

```
db=2a, dc=0, dd=de=4c, dx=2(e-d), df=0.
```

The mod-two labels are the fixed ones above. These choices follow
from H4(B;Z)=Z4, H5(B;Z)=Z2 and the already fixed first and second
Bocksteins; the integral spherical f-class supplies df=0. Odd-unit
normalization and even cell slides preserve the specified mod-two
labels. All tensor-chain signs below use the displayed degrees.

The four literal ten-cycles in Sigma³(B smash B) are

```
AD=ad-2bc,  AE=ae-2bc,
DA=da-2cb,  EA=ea-2cb.
```

The other two ten-cells BC=bc and CB=cb have boundaries 2D and
2(D+r). In this basis the entire eleven-boundary matrix is exactly

```
AF: 0;                  AX: 2(AE-AD);
FA: 0;                  XA: 2(EA-DA);
BD: 2AD;                BE: 2AE;
DB: -2DA;               EB: -2EA;
CC: 0.
```

This directly proves that the image is twice the free ten-cycle
lattice; no inference from the first Bockstein alone is needed.

The ten-stage slides can be chosen explicitly as

```
Q=AD, V=DA-AD, G=BC-DA, H=CB-BC+DA-AD.
```

Their attaching maps are respectively delta, e eta, gamma, 2r.
Thus the ten-stage splitting in Section 2 is an actual splitting.
The only possible attaching components in degree nine are exactly
the free and eta components listed there, so the integral boundary
and Sq2 data determine these maps completely.

With orientations matching the literal chain matrix, the complete
eleven-stage homotopy matrix is

```
AF: 0
AX: -kappa+2AE
FA: 0
XA: -kappa-gamma'+2EA+r eta9
BD: kappa+delta'
BE: 2AE
DB: -kappa-gamma'+delta'
EB: -2EA
CC: v+r eta9.
```

Only the signs of the free components differ from the earlier
mod-two working display. The three torsion coordinates are detected
independently by Sq4 on aa and Sq2 on m,r. There is no additional
primary-invisible component in this degree.

First isolate 2AE and 2EA. The sum of DB and BD isolates -gamma'.
Combining AX with BD and the AE relation isolates delta'. The BD
relation then isolates kappa. The XA relation, after these changes
and the EA relation, isolates r eta9. Finally CC isolates v. The
two zero cells remain zero. Consequently actual cell slides give

```
Z11 ~= J vee Cb10 vee C1^11 vee M2,10 vee M2,10
          vee S11 vee S11,
J = Cb9 union_kappa e11_K union_v e11_N,
Cb9 = C1^9 union_delta e10_Q union_gamma e10_G.
```

This equivalence preserves the specified bottom S7, which lies in J.
All maps used to make the slides are in the ordinary stable range
through dimension eleven; no classification of pi14 by stabilization
is being substituted. In particular there is an actual retraction
of the eleven-stage onto J, fixing its bottom.

## 5. The complete pi11 group of the bottom block

The earlier Cblock calculation gives

```
pi10(Cb9) = Z{kappa} + Z2{v},
0 -> Z2{omega} -> pi11(Cb9) -> Z2{G eta10} -> 0,
kappa eta10=omega.
```

The old omega is the image of the Chang generator t of Section 22.
Indeed the delta-attaching map composed with eta squared is 2t,
so its image after the two ten-cells has order two. The G-eta
coextension is denoted zeta before and after quotienting by omega.
Attaching the kappa eleven-cell kills omega and has no extra free
pi11 lift, because kappa has infinite order. Thus its pi11 is
Z2{zeta}.

The class v=i7 nu7 still has exact order two, detected by Sq4 on
the bottom class. Its eta composite is zero, since nu7 eta10=0.
The cofiber sequence for its eleven-cell therefore gives

```
pi11(J) = Z{p_aux} + Z2{zeta},    h(p_aux)=2N.
```

The pinch image is 2Z because v has order two. This accounts for
every homotopy class in the attaching group, not merely a chosen
free lift. The zeta class has nonzero Sq2 detector on the G10
cohomology class: its pinch on G is eta10.

## 6. An independent quotient detects zeta nu

Collapsing the bottom S7 gives an actual equivalence

```
Cb9/S7 ~= C(eta8) vee M(Z2,9).
```

The Ceta factor is on B8,Q10, and the Moore factor is on D9,G10.
In degree eleven, their groups are respectively Z4{i8 nu8} and
Z4{tilde eta9}. The representative zeta pinches to eta10 on G,
so its Moore component is an odd multiple of tilde eta9.

In the stable-range cofiber sequence for S7 -> Cb9, the connecting
map from the quotient to S8 extends degree two on B8 and eta8 on
D9. It therefore sends the Ceta nu generator to 2nu8. On the
Moore eta coextension it has value +2nu8 or -2nu8, the exact
ordinary Toda bracket <eta8,2,eta9>. Both possible values are
twice an odd multiple of nu8. Exactness forces the coefficient
of the Ceta nu generator in zeta's quotient image to be odd.

After composition with nu11, its Ceta coordinate is therefore
the nonzero class i8 nu8 squared. This bottom nu squared survives
the eta cell: the relevant fourth stable stem which could supply
a boundary is zero. The Moore coordinate has zero nu composite,
since its stable fifth stem is zero.

Passing from Cb9/S7 to J/S7 adds only two eleven-cells. Both spaces
are seven-connected, so pi14 is still in their ordinary stable
range. The possible kernel is the image of pi14(S10 vee S10),
which is zero by the fourth stable stem. Thus the detected
nu-squared coordinate remains nonzero in J/S7. We have proved

```
zeta nu11 has nonzero image in pi14(J/S7).
```

The fibrations reader independently checked this component
calculation, including both connecting coefficients and the
subsequent injection.

## 7. The top-eight lift is exactly four p_aux

There is an actual map C(nu7)->J, taking the bottom to i7 and
the top cell to the N-cell. The unique class v8 in pi11 C(nu7)
with top degree eight exists by the ordinary stable-range cofiber
sequence: pi11S7=0 and nu7 has order eight.

Both 4p_aux and the image of v8 have integral Hurewicz image 8N.
Their difference is therefore a multiple of zeta. But zeta is
detected by Sq2 on G10, whereas both comparison classes have zero
such detector. For 4p_aux this follows from the degree-four map
on the source sphere. For the image of v8 it follows from the
actual cone map and H10 C(nu7)=0. Thus the difference is zero:

```
4p_aux = image(v8) in pi11 J.
```

The ordinary coextension formula, with the singleton bracket
<nu7,8,nu10>=4sigma-prime already audited in Section 21, gives

```
4p_aux nu11 = i7 (4sigma-prime)=0.
```

For the last equality, 2i7=0 and [i7,i7]=0, the latter following
from the H-space sphere S7. Hence the cyclic Hilton correction
vanishes; the order-two bottom kills every even multiple of
sigma-prime. No out-of-range covariant cofiber exact sequence is
used to compute the actual degree-fourteen composite.

## 8. Why no twelve-cell attachment can kill the bottom class

Suppose a composite in pi11J followed by nu11 lies in the old
bottom subgroup generated by i7 sigma-prime. Write its first
factor as m p_aux+epsilon zeta. Pinching the N-cell gives
2m nu11 in pi14S11=Z8{nu11}. Thus m is divisible by four.
Section 7 kills that whole free contribution. If epsilon is odd,
Section 6 gives a nonzero quotient coordinate in J/S7, contrary
to being a bottom class. Therefore epsilon is zero as well.
We have established the exact intersection statement

```
(pi11J) nu11 intersect <i7 sigma-prime> = 0.
```

Retracting Z11 onto J proves the same obstruction to a bottom
relation arising from any collection of twelve-cell attachments
to the actual auxiliary target. Indeed the comparison from the
wedge of attaching S11 spheres to the homotopy fiber is
sixteen-connected by Blakers--Massey (initial connectivities six
and eleven). Hence the entire kernel on old pi14 is the image
of pi14 of that wedge, namely its nu11 composites. Projecting
any putative bottom relation to J contradicts the displayed
intersection statement.

The initial i7 sigma-prime is nonzero of order two at the
nine-stage by the actual Moore/Chang argument in Section 20.
Adding ten-cells preserves old pi14: the same comparison is
fourteen-connected and pi14S9 is the zero fifth stable stem.
Adding eleven-cells preserves it because the comparison is
fifteen-connected and pi14S10 is the zero fourth stable stem.
The intersection argument then preserves it through all
twelve-cells.

**Independently audited conclusion (D.2.60):** the actual
James--Hopf image of alpha sigma-prime remains nonzero of exact
order two through the twelve-skeleton of Sigma³(B smash B).
The thirteen-, fourteen-, and fifteen-cell effects are not
computed here. In particular this does not decide the image
in the full auxiliary space, the value of n, or the full-target
class h.
