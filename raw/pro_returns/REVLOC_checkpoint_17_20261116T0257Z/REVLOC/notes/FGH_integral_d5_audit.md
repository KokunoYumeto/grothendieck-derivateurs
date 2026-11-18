# Independent audit of the first mixed integral differential

16 November 2026. This records the axioms/derivators agent's audit
of the root's proposed calculation. It proves the stated differential;
it does not evaluate the remaining integral square on L.

Put

    P=P6Y=fib(Sq3:K(F2,4)->K(F2,7)),
    H=Omega P=fib(v3^2:K(F2,3)->K(F2,6)),
    V4=beta_Z(v3),
    L=hofib(Y->P).

All groups below are cohomology groups. There are actual fibrations
`K(F2,5)->H->K(F2,3)` and `K(F2,6)->P->K(F2,4)`.

## 1. The fiber group H8(H;Z)

In total degree eight, the first Serre sequence has just the base
class `V4^2` of order two and the fiber class `beta_Z Sq2(s5)`
of order two. No mixed terms have that total degree. The base
class cannot be hit: possible source bidegrees for its scalar-line
differential are `(1,6)` and `(0,7)`, both zero.

The assertion that the fiber class survives needs more than a
dimension count. A d3 into bidegree `(3,6)` is formally possible
in this pulled-back fibration. Use instead its origin in the
universal path fibration over `K(F2,6)`. There the same class
has no earlier differential and is transgressive, with value
`beta_Z Sq2(u6)`. Naturality of that actual path fibration shows
that all earlier differentials remain zero on its pullback.
The transgression becomes

    beta_Z Sq2(v3^2)=beta_Z((Sq1 v3)^2)=0,

since `Sq1 v3` is the reduction of the integral class V4.
The fiber class is therefore permanent. The two terms give an
extension of Z/2 by Z/2. The nonzero base class has zero mod-two
reduction, because `(Sq1 v3)^2=Sq2(v3^2)=0` on H. It is thus
divisible by two in the integral group. This forces

    H8(H;Z)=Z/4{z8},       2z8=V4^2.

The same low-degree sequence gives `H1..3(H;Z)=0`,
`H4(H;Z)=Z/2{V4}`, and `H5(H;Z)=0`.

## 2. The entire group H9(P;Z)

In total degree nine, the base contributes
`Z/4{B9=beta4 P2(u4)}`. The only other possible term is
the fiber class `beta_Z Sq2(w6)` of order two. It is
transgressive, either by the same universal-path argument or
directly from the degree range. Its value is

    beta_Z Sq2 Sq3(u4)=beta_Z Sq4 Sq1(u4).

Its mod-two reduction is `(Sq1 u4)^2`, which is nonzero in
the polynomial cohomology of `K(F2,4)`. Thus that fiber term
is killed. There are no mixed total-nine terms, and no
differential can hit the base degree-nine class: the possible
sources are `(1,7)` and `(0,8)`, both zero. Consequently

    H9(P;Z)=Z/4{B9}.

This is the full group needed below, not merely a named subgroup.

## 3. The universal path differential

In the path fibration `H->*->P`, integral cohomology suspension
commutes with coefficient Bocksteins. Thomas's actual suspension
formula gives

    sigma(B9)=beta4 p(v3)
             =beta4(2v3 beta_Z v3)=V4^2=2z8.

For the last equality, choose integral representatives with
`dv=2V`. The differential of `2vV` is `4V^2`.
Thus the image of the entire cohomology suspension in degree
eight is exactly `<2z8>`.

In a path fibration the image of cohomology suspension is the
subgroup of transgressive fiber classes. This can also be seen
directly: a transgressive fiber cocycle extends to a cochain
whose differential is pulled back from the base, and the
contractibility of the total path space identifies that
construction with suspension. Hence odd z8 cannot survive
to its scalar-line transgression.

There is only one possible earlier differential on z8.
The base P is three-connected, `H5H=0`, and `H1..3H=0`.
Thus r=2,3,4,6,7,8 give zero targets. At r=5 the target is

    E5^(5,4)=H5(P;Z/2){V4}=F2{Sq1 u4 tensor V4}.

No earlier incoming or outgoing differential removes that
target: the potential incoming terms have base degree one,
two, or fiber degree five, and the earlier outgoing terms
have fiber degree at most three. It follows that

    d5(z8)=Sq1 u4 tensor V4 != 0.

## 4. Pullback to the actual target

The fibration `H->L->Y` is pulled back from the path fibration
along the actual Postnikov projection `Y->P`. Naturality gives

    d5(z8)=Sq1 U4 tensor V4 != 0

there as well. The class `Sq1 U4=Sigma^2 Sq1 u2` is nonzero,
and the same absence of earlier differential terms applies.

This differential prevents a global integral class restricting
to an odd multiple of z8. It does not by itself determine the
square of the global class whose restriction is `2z8`; a
multiplicative or coefficient extension must still be checked.

## Source interface

The actual six-type and its coefficient pullback are recorded
in `I_integral_P6_target.md`, Sections 1--3. The low integral
Eilenberg--MacLane groups and transgressive operations use the
already opened Serre computation. Thomas's Theorem I and
Proposition 6.9 give `S(P2)=p`, and the integral representative
above checks the coefficient Bockstein explicitly. No claim of
a new original-source opening is made in this audit.


## Final independent audits of D.2.48--50 (16 November 2026)

D.2.48 passes in full. In the universal path spectral sequence the
only maps hitting the base Z/4 in degree nine are d5 from (4,4) and
d9 from the surviving Z/2 in (0,8). Acyclicity forces the former
to hit the unique order-two subgroup. The fiber e7 is the suspension
of an actual e8, so its earlier d4 into (4,4) vanishes. Pullback to Y
kills B9 and hence the actual d5 on U4 tensor V4; the actual d8(e7)
kills the whole base H8(Y). The global Z/4 extension therefore puts
2b8 in filtration four and makes the base pullback zero. Rational
acyclicity supplies the implicit zero Hom term in the final UCT use.

Both D.2.49 inputs pass. The complete Ganea six/seven-cell matrix
has pi6(Sigma B)=Z/2, and the first James relative Hopf map makes
suspension injective with image twice alpha. Thus u3 nu-prime=0.
The indexed epsilon-prime bracket is contained in the ordinary
bracket; after postcomposition its zero first map leaves exactly
pi10(Sigma B) composed with nu10 as the full indeterminacy. The
actual suspended composition lifts uniquely through L using S11,
so its integral loop H13 vanishes. The independent actual Moore
comparison and chain identities identify Hur(h) with twice the
intrinsic bottom commutator, proving that double zero.

D.2.50 passes in its final corrected form. For a six-reduced
simplicial model the degree-fourteen canonical cobar nullchain
has only lengths one and two. Its linear part is the desuspension
of an actual integral fifteen-cycle. The functional A tensor B
on the quadratic part has value two modulo four. Its value on
the internal differential of every possible degree pair (7,9),
(8,8), (9,7) is zero modulo four, using dA=4B and dB=0.
The remaining reduced-diagonal term is exactly the Alexander--Whitney
cup product, with the Koszul sign harmless modulo four at value two.
Thus the half-product theta pairs one on an actual integral cycle.
An integral lift would pair zero by torsion, so beta_Z(theta)=b8^2
is nonzero and has exact order two.

The final manuscript explicitly constructs the mod-four lift:
if dE=2B^2 and dJ=B^2+2K, then E-2J modulo four is a cocycle
lifting theta. This shows that the detected integral class has
order at least four. The earlier draft incorrectly attributed
that explicit construction to D.2.45, which only wrote dE=2B^2;
the final two-line addition removes the dependency gap.

The current author-hosted ABFJ PDF puts Lemma 5.4.2 on printed
page 43 (PDF index 42); the D.2.50 locator was corrected accordingly.
The axioms agent independently opened that lemma and the HPST
version-2 passages on printed pages 3 and 5. The latter supply
the natural integral algebra quasi-isomorphism and the exact
linear-plus-reduced-Alexander--Whitney cobar differential. All
three agents and root have completed the relevant full reads.

No argument here makes the integral fifteen-cycle stably spherical.
The stable Hurewicz pairing and the homotopy value of h remain open.
