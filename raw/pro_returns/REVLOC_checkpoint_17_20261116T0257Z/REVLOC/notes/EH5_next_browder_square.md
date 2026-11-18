# The next actual Browder square: exact Moore interface

Status at 15 November 2026: MOORE ANTECEDENT CORRECTED after an
independent low-cell audit. The actual nonzero pi6(Y) element is the
image of the free Chang lift gamma, with integral Hurewicz image 2c.
The Moore coextension is killed. The square and its divisibility
remain undecided; the opened Moore theorem below is not applicable
to that actual square.
This note makes no claim of a ten-skeleton extension.

Put B=K(F2,2), Y=Sigma²B, T=Omega²Y, and let F be the three-connected
double-loop fiber used in D.2.18--D.2.20. Let chi in pi4(F)=Z2 be the
nonzero bottom element, with mod-two Hurewicz image A4=a². Its double
adjunct is the nonzero delta in pi6(Y)=Z2. The actual homotopy Browder
square lambda(chi,chi) corresponds to the Whitehead square
[delta,delta] in pi11(Y). Its mod-two Hurewicz image is zero because
the homology Browder derivation sends {a²,a²} to zero.

## 1. The primary Moore-space theorem

Opened directly:

K. Morisugi and J. Mukai, *Lifting to mod 2 Moore spaces*, Journal of
the Mathematical Society of Japan 52(3) (2000), 515--533,
https://www.jstage.jst.go.jp/article/jmath1948/52/3/52_3_515/_pdf .

Theorem 4.1(i), printed p.529 (PDF p.15), says that
tilde-eta_(n-1) composed with [iota_(n+1),iota_(n+1)] has order four
when n is odd. The proof explicitly includes n=3 and n=5; it cites
J. Wu's 1995 Rochester thesis for those two cases. The theorem itself
is an opened primary research source. The thesis has not been opened.
The added correction on the final page concerns Lemma 3.1, not the
n=5 assertion quoted here.

For n=5 this is exactly

    [tilde-eta4,tilde-eta4] in pi11(P5(2)), of order four,

where P5(2)=S4 union_2 e5 and tilde-eta4:S6 -> P5(2) is the usual
Moore coextension, with 2 tilde-eta4=i4 eta4². An earlier version of
this working note incorrectly identified its image with the canonical
nonzero delta in pi6(Y). The independently checked low cells show
that this Moore image is killed. In fact C1^6 has pi6=Z gamma plus Z2 delta_M, with
h_Z(gamma)=2c and h_Z(delta_M)=0. The two seven-cells of Y have
second Bockstein c and different second-square detectors. With the
fixed notation d dual to Sq2 Sq1 u and e dual to u Sq1 u, their
attachments are 2gamma+delta_M and 2gamma, respectively. The base
operation table gives Sq2_*d=b and Sq2_*e=0, detecting their torsion
components. They kill delta_M and leave gamma modulo two. Higher
cells do not change pi6. This precise normal form was independently
checked by the axioms agent. Therefore the Moore theorem is a source
check only, not an evaluation of the required square.

The canonical delta has order two by the already proved low-stem
calculation, so its Whitehead square has order at most two by
bilinearity. Its vanishing and four-divisibility are not decided.

An independent opened recent computation is Z. Zhu, *The unstable
homotopy groups of 2-cell complexes*, arXiv:2410.20416v2,
https://arxiv.org/pdf/2410.20416 , Section 5, printed p.35,
the pi11(P5(2^r)) calculation and equation (31). For r=1 it gives
pi11(P5(2))=Z2+Z2+Z4. Its cited original is again Wu's Theorem 5.10.
No abstract-group argument is substituted for the actual image map.

## 2. Why the previously safe stabilization argument stops here

The double unit F -> Omega² Sigma²F has a left inverse because F is
a double-loop space. It is a map of spaces; it is not automatically
a map respecting the given double-loop multiplication or Browder
operation. Consequently one cannot identify lambda(chi,chi) with
the stable kernel merely by applying this split unit.

Sigma²F is five-connected. Its first possible unstable kernel in
degree eleven is controlled by the first relative James group
H6(Sigma²F) tensor H6(Sigma²F)=Z2 and the corresponding bottom
Whitehead square. The double-loop counit sends that universal square
to lambda(chi,chi), but membership of the universal square in the
image of the split unit is a separate condition. Thus neither
stable injectivity in degree nine nor stable vanishing of the actual
Browder square has been asserted.

## 3. Current geometric and algebraic tests

Root has isolated the first arity-two relative cell of
C2(X/S3) -> Q(X/S3), with X=Sigma B. Its expected boundary is the
bottom Browder self-bracket. This source-cell identification and the
pullback to the original X are being audited independently. On the
original source the resulting obstruction may be the square modulo
4 pi9(T), rather than the square itself. Therefore both its vanishing
and its four-divisibility remain explicit questions here.

The next target-side test is the free Chang lift through

    gamma:S6 -> C1^6=P5(2) union_(i4 eta4) e6 -> Y.

The relative James construction gives a concrete route to its square;
one must retain the secondary attaching map, not just the order of
the source group. A possible smash-square shortcut would require
computing the actual coextension smash square before applying the
generalized Whitehead product. The opened Zhu--Pan preprint
arXiv:1606.00624, Theorem 1.1, shows that C1^5 smash C1^5 is
indecomposable. It does not compute that particular smash-square map
or prove its vanishing, and no such inference is made.

## 4. Completed preceding stage

D.2.20 is independently audited and integrated: pi8(Sigma-infinity F)
is (Z2)^3, its integral Hurewicz image is <2C,W,J2>, and the sole
stable mod-two Hurewicz-kernel element is excluded from actual pi8F
by Sq5 instability. Thus actual pi8F has injective mod-two Hurewicz,
the two specified torsion composites vanish, and the corrected map
extends through the ninth skeleton. The complete proof is in
EH5_pi8_stable_target.md and sections/D2_nine_target.tex; source and
homology inputs are owned by the other two agents. This finite-stage
result does not settle the full extension requested in Part D.2.
