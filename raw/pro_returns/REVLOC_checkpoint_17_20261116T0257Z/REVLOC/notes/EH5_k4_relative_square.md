# The finite relative source for the fourth-suspension ambiguity

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Research note after D.2.34.

**Status.** The reduction and integral chain calculation below are exact.
They do not determine the paired coefficient on all maps from the finite
source to the connected-cover target. In particular they do not prove a
fourth-suspension nonextension theorem. The target calculation is assigned
to the axioms agent; this note records the independent source interface.

Put B=K(F2,2), X=Sigma B, Y=Sigma²B and T=Omega²Y. Let
Z'=Y<7> be the six-connected cover, E=Omega²Z', and U=Omega²E.
Thus U is two-connected and is an actual fourfold loop space. Let

    V=U<6>

denote its FIVE-connected cover. Equivalently V=Omega⁴(Y<10>),
where Y<10> is nine-connected. In particular V is a loop space.

## 1. The actual relative difference and its stable range

Suppose g,g0:C4X->U agree up to a specified homotopy on X. Form their
pointwise difference using the H-group U. Its restriction to X is null,
so the pointed cofiber universal property gives an ordinary map

    d:C4X/X -> U.

The source is five-connected: the configuration filtration starts its
non-unit part with two labels from the two-connected space X, hence in
dimension six. The difference consequently lifts uniquely up to homotopy
to V. This is a connected-cover lifting statement, not a multiplicativity
assertion for either original map.

For every finite CW complex K of dimension at most eleven, the map

    [K,V] -> [Sigma∞K,Sigma∞V]

is a bijection. Indeed V is five-connected, so its unit into Omega Sigma V
is eleven-connected and gives surjectivity on these mapping sets. Because
V is a loop space, the unit has an actual homotopy retraction by the loop
counit; it is therefore injective on mapping sets in every dimension.
Finally Sigma V is six-connected, and Sigma K has dimension at most
twelve, so the remaining stabilization is bijective by Freudenthal.
This proof supplies the endpoint degree eleven, where bare Freudenthal
alone would give only surjectivity.

The Snaith splitting is relative to its weight-one inclusion. Consequently
the suspension spectrum of C4X/X is the wedge of the arity-at-least-two
configuration quotients. Let M=M(Z/2,3) be the actual bottom Moore
subcomplex of X. The arity-two summand and M->X give a stable map

    Sigma∞D -> Sigma∞(C4X/X),
    D=D_2^(4)M = S³_+ smash_{C2} (M smash M).

Here the two-point little-four-cubes space is equivariantly equivalent to
the antipodal S³: shrink cubes to their centers and use the normalized
difference of the two centers. This is the usual arity-two configuration
model, not an infinite homotopy-orbit replacement.

Composing with Sigma∞d and using the established mapping bijection gives
an actual map D->V. Its homology on the unique degree-eleven top class
records exactly the change on Q7(B0), where B0 is the top degree-four
Moore class of X. The class Q7(B0) is primitive in H11(C4X): the two label
classes are primitive and the coproduct formulas for the top operation
have no mixed term involving the unit. Therefore the pointwise difference
adds the two homology values on this class, with no convolution correction.

Define mu11 on U to be the pullback under twofold cohomology suspension
of the sum of the independent ambient functionals dual to xi1(k) and
xi1(f) in H13(T). The following is a sufficient exact target test for
rigidity of the paired coefficient:

    For every actual map v:D->V,
    <v*(mu11|V), top11>=0.                         (1)

If (1) holds, every ordinary C4 extension agreeing on the unit has the
same paired coefficient as the canonical one. Unlike a test on spheres
alone, (1) includes the nontrivial Moore-top choices described next.
The converse is not asserted: arbitrary maps D->V need not extend to the
whole relative source.

### Scope repair after the entire-unit linear exclusion

The root's subsequently audited degree-minus-three Steenrod argument
excludes the linear f coefficient for every map Sigma⁵B->Sigma²B;
the independent hand audit is `EH5_k4_linear_audit.md`. Consequently
the conditional finite test can cover all dangerous fourth-suspension
maps, without fixing their entire infinite unit maps, as follows.

For M=M(Z/2,3), the actual Moore Puppe sequence is

    0 -> coker(2:pi4U->pi4U) -> [M,U]
      -> ker(2:pi3U->pi3U) -> 0.

The proved actual groups are pi3U=Z/4{alpha}, pi4U=Z/4{rho}.
The two nonzero group terms displayed are therefore Z/2. For a fixed
bottom map, the nontrivial top action is represented by rho composed
with M->S4; it changes the doubly suspended top homology by
r=b²+k+p3. Thus the bottom bit t and the rho-top bit epsilon determine
the homotopy class of the whole Moore restriction. A putative difference
2rho has already vanished in the cokernel and is not an extra choice.

Every dangerous map has commutator coefficient1. Its exact bottom/top
range is t k+epsilon r. The entire-unit linear exclusion forces
epsilon=0, and hence t=1. Its Moore restriction is therefore homotopic
to the canonical map of D.2.29, with bottom -2alpha and top k.

Restrict a proposed full map A->U to C4M->C4X->A, and compare it with
the canonical free-E4 extension of this same Moore map. The difference
now factors through C4M/M, which is still five-connected. Applying
Section1 to this smaller relative source gives exactly the same D->V
test (1). The value of the canonical top under mu is one; a full
infinite-loop-source extension must give zero, since Q7B becomes the
first Bockstein of Q8B at the sixth stage and neither ambient outer
square is a first-Bockstein boundary. Thus (1), if established, would
exclude ALL dangerous fourth-suspension maps. Higher unit choices
play no role in this reduction.

The missing assertion remains exactly (1). Moore uniqueness does not
prove it, and no vanishing of the paired functional is inferred here.

For completeness the four-element Moore mapping group is actually
elementary abelian. Let m denote the canonical class and e=rho q the
top action. The class e has order two by the displayed cokernel. The
Moore Puppe sequence factors 2 id_M through the top pinch q.
Since pi4(M)=Z/2{i eta3}, its factor is zero or i eta3; either gives

    2m = (2alpha) eta q = 4rho q = 0,

using 2rho=alpha eta from D.2.18. Thus [M,U]=(Z/2)², with
representatives 0,e,m,m+e. This refinement is not needed for uniqueness
of the dangerous restriction; it uses only the low Moore exact
sequence, the opened Oka1986 low sphere stems, and the proved actual
target relation. The stronger identity 2 id_M=i eta q is unnecessary.

## 2. Exact integral chains of D

Use Moore cellular chains a in degree3 and b in degree4, with db=2a.
The antipodal sphere has one free Z[C2]-cell e_i in each degree
0<=i<=3, with differential 1+(-1)^i g. The action on the label tensor
is graded interchange, so

    tau(aa)=-aa, tau(ab)=ba, tau(ba)=ab, tau(bb)=bb.

The total chain group has basis e_i xy, i=0,1,2,3 and x,y in {a,b}.
Its differential is

    d(e_i xy)=e_(i-1)(xy+(-1)^i tau(xy))
              +(-1)^i e_i d(xy),

with the first term absent at i=0. These are the actual cellular chains
of the free-action quotient; the signed product cellular differential
is equivariant. The ranks in degrees6,...,11 are 1,3,4,4,3,1.

Here is an explicit integral cancellation, retained to make the Smith
normal form independently checkable. Abbreviate the generators as

    a0=e0 aa;
    x=e0 ab, y=e0 ba, z=e1 aa;
    t=e0 bb, h=e1 ab, h'=e1 ba, w=e2 aa;
    s=e1 bb, j=e2 ab, j'=e2 ba, v=e3 aa;
    q=e2 bb, r=e3 ab, r'=e3 ba;
    t3=e3 bb.

Their nonzero differentials are

    dx=-2a0, dy=2a0, dz=2a0;
    dt=2x+2y, dh=x-y+2z, dh'=-(x-y+2z);
    ds=-2(h+h'), dj=h+h'-2w, dj'=h+h'+2w, dv=2w;
    dq=2s+2j+2j', dr=j-j'+2v, dr'=-(j-j'+2v);
    dt3=-2(r+r').

Cancel successively the three unit pairs given by h, j, r. In the
resulting quotient chain complex these set

    y=x+2z, h+h'=2w, j'=2v.

The surviving complex is the direct sum of the five two-term complexes

    Z{z7} --2--> Z{a0_6},
    Z{t8} --4--> Z{(x+z)7},
    Z{v9} --2--> Z{w8},
    Z{q10} --2--> Z{(s+2v)9},
    Z{t3_11} --(-2)--> Z{(r+r')10}.

This is a splitting of CHAIN COMPLEXES only. It is not a claim that the
space or its suspension spectrum splits as a wedge of Moore spaces.
In particular Steenrod and secondary attaching information is retained
as a separate issue.

It follows that the nonzero reduced integral homology groups are

| degree | integral homology |
|---|---|
| 6 | Z/2 |
| 7 | Z/4 |
| 8 | Z/2 |
| 9 | Z/2 |
| 10 | Z/2 |

The mod-two homology ranks in degrees6,...,11 are 1,2,2,2,2,1.
The top cell t3 has boundary -2(r+r'), so its first Bockstein is nonzero.
In operation notation this is precisely

    beta Q7(B0)=lambda3(A0,B0),                    (2)

the top-operation correction which cannot be omitted at C4.
Thus the source top class in (1) is not an integral homology cycle.
An argument controlling only actual S11->V variations does not control
all of the changes permitted by the finite source D.

For the target operation comparison, the complete mod-two basis and
first/second/fourth squares are useful. Write

    P6=A²;
    R7=AB, S7=Q4A;
    T8=B², U8=Q5A;
    V9=Q5B, W9=Q6A;
    X10=Q6B, Y10=lambda3(A,B);
    Z11=Q7B.

The nonzero beta values are R,S->P; W->U; X->V; Z->Y.
The nonzero second squares are T,U->P; V->S; X->U; Z->W.
The nonzero fourth squares are X->P and Z->S. All other values
of these three operations on the displayed basis vanish. The top
correction terms in the second/fourth square of Z vanish: the only
positive square of B is Sq1B=A, and the remaining unequal-index
Browder summands contain a zero factor. This uses the printed CLM
top formula on pp217--218, visually reopened for this calculation.
Consequently in cohomology

    Z11* = Sq4 Sq1(P6*) = Sq2 Sq3(P6*),
    Sq5(P6*)=0.

A target expression for the paired functional as Sq4 of a degree-seven
class would therefore not by itself force zero. It can detect the
actual lower relative choices on S7. Likewise an arbitrary integral
cohomology lift is insufficient, since H11(D;Z)=Ext(H10D,Z)=Z/2
and its reduction can detect Z11. These are retained mapping choices,
not vanishing conclusions.

### The degree-ten Bockstein target is an actual spherical class

There is an actual sphere y:S10->D whose mod-two Hurewicz image is
Y10=lambda3(A,B). No assertion about its homotopy order is needed.
Start with the bottom map S3->M and the unit M->C4M. Their generalized
Browder map has domain

    Sigma³(S3 smash M)=M(Z/2,9).

On the bottom S9 its fourfold adjunct is the Whitehead square
[u7,u7] in Sigma⁴M, where u7:S7->Sigma⁴M is the bottom inclusion.
The square is zero: S7 has its octonionic H-space multiplication, so
[iota7,iota7]=0, and Whitehead products are natural. A chosen nullhomotopy
therefore factors the generalized Browder map through the top quotient
S10. Its H10 image is exactly lambda3(A,B), since both Moore labels
are primitive and the bottom-to-top quotient is an isomorphism on the
degree-ten mod-two class.

Compose stably with the Snaith projection C4M->D. The projected class
is unchanged because it has weight two. The finite space D is
five-connected, so pi10D agrees with its stable homotopy group by
Freudenthal. Hence this stable sphere desuspends to an actual S10->D
with the asserted Hurewicz image. The mod-two class is also the reduction
of the nonzero integral H10(D;Z)=Z/2 class, by the coefficient sequence
and beta X10=V9, beta Y10=0.

This spherical fact does not identify the entire stable attaching map
of D's eleven-cell. Its integral degree is twice this H10 class, but
additional torsion components and their nullhomotopies have not been
discarded. In particular it does not turn condition (1) into a test on
spheres alone.

`code/EH5_k4_relative_square.py` independently checks d²=0 and the
integral Smith invariants, using the already retained Smith-decomposition
routine. Its output is `code/outputs/EH5_k4_relative_square.json`.

## 3. Exact limitation of a literal multiplication-deviation copy

D.2.16 exploited a nonzero target Pontryagin square and a forced source
coefficient mismatch. Here the actual degree-four Moore-top class q4 in
U has q4²=0, as proved in Section8 of `EH5_first_cone_suspensions.md`.
Therefore its square has no dual coefficient functional and cannot play
the role of D.2.16's L. Merely repeating that proof with renamed classes
would be invalid.

Furthermore the ordered multiplication deviation on X smash X does not
automatically carry the RP³ coherence encoded by D. The ordered S³ cover
has degree two on the top projective cell. No equivariance or descent of
an arbitrary multiplication deviation is supplied by an ordinary map.
The relative-cofiber argument in Section1 avoids that assumption and
produces the actual finite test (1). Its value remains to be calculated.

## 4. Primary-source audit

Snaith, *A stable decomposition of Omega^n S^n X* (1974), Theorem1.1,
printed p577, and the filtered Theorem3.2, printed p580, were reopened
directly in this session. They give the stable splitting with its
filtration compatibility; the weight-one piece is the unit X.
Existing bibliography key: `Snaith1974`.
<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Snaith-split.pdf>

May, *The Geometry of Iterated Loop Spaces* (1972), Sections4--6, was
reopened at the author's site for the configuration model and its
approximation to iterated loops. Existing key: `May1972`.
<https://www.math.uchicago.edu/~may/BOOKS/geom_iter.pdf>

The endpoint mapping argument is the same split loop-unit/Freudenthal
argument independently audited in D.2.18--D.2.22, now with connectivity
five and source dimension eleven. The top Bockstein convention agrees
with the already opened Cohen--Lada--May, ChapterIII, Theorems1.2--1.4,
and with the explicit integral chains above. No unverified higher
configuration splitting or stable-to-unstable inverse is being used.
