# An exact mixed integral differential for the actual six-type fiber

Root calculation, 16 November 2026, 00:27--00:30 UTC.
The simple/higher agent independently checked the complete argument.
Throughout this note H^n means cohomology, and an omitted coefficient
group in a cohomology group is the integers.

## 1. Spaces and the specified class

Put Y=Sigma²K(F2,2), P=P6Y, and L=Y<7>. The actual six-type,
already audited in I_integral_P6_target.md, is

    P=fib(Sq3:K(F2,4)->K(F2,7)).

Consequently H=Omega P fits into the actual sequence H->L->Y,
and H=fib(v3²:K(F2,3)->K(F2,6)). The sequence H->L->Y is the
pullback of the path fibration of P along its actual Postnikov map.
The integral degree-eight transfer class is x=beta4(a7). By the
audited secondary Pontryagin normalization, its restriction to H is

    x|H=V4²,   V4=beta_Z(v3).

This follows by suspending P2 to Thomas's p: on K(F2,3),
a7 restricts to 2 v3 V4 modulo four. For an integral lift v with
dv=2V, the representative 2vV has differential 4V².

## 2. The complete integral group H^8(H)

Use the integral Serre sequence of K(F2,5)->H->K(F2,3).
In total degree eight its only nonzero E2 pieces are

    (8,0): Z2{V4²},
    (0,8): Z2{beta_Z Sq2(s5)}.

There are no mixed pieces: the base is two-connected and the
fiber's first positive integral cohomology is in degree six.
The base class cannot be hit; the only potential incoming sources
are (1,6) and (0,7), both zero. The fiber class is transgressive
by naturality from the universal path fibration and compatibility
with the stable operation beta_Z Sq2. In particular the
dimensionally possible earlier d3 into (3,6) is zero by this
universal-path naturality. Its transgression is

    beta_Z Sq2(v3²)=beta_Z((Sq1v3)²)=0,

because Sq1v3 is the reduction of the integral class V4. Thus
the second piece also survives. This yields an extension of Z2
by Z2, with the first copy represented by the nonzero V4².

The relation v3²=0 on H gives

    red2(V4²)=(Sq1v3)²=Sq2(v3²)=0.

Integral coefficient exactness gives 2z8=V4². Since the right
side is nonzero and killed by two, z8 has exact order four.
It follows that the whole group is H^8(H)=Z4{z8}, and

    (x|H)²=(2z8)²=4z8²=0.

Also H^3(H)=H^5(H)=0 and H^4(H)=Z2{V4}; these follow at once
from the same sequence below its first positive fiber group.

## 3. The complete integral group H^9(P)

Use K(F2,6)->P->K(F2,4), with mod-two transgression
w6 |-> Sq3(u4). The base has

    H^9(K(F2,4))=Z4{B9=beta4 P2(u4)}.

This class survives: there are no incoming sources in total
degree eight with positive fiber degree. The only additional
degree-nine E2 piece is the fiber class
beta_Z Sq2(w6) of order two. Its transgression is

    beta_Z Sq2 Sq3(u4)=beta_Z Sq4 Sq1(u4).

Here Sq2 Sq3=Sq5+Sq4 Sq1, and Sq5(u4)=0 by instability.
This integral target is nonzero, since its mod-two reduction is

    Sq1 Sq4 Sq1(u4)=Sq5 Sq1(u4)=(Sq1u4)² != 0.

No earlier differential kills this target: the possible earlier
incoming positive-fiber sources have zero base degree one or two,
or have a zero integral fiber group. The lower fundamental fiber
class beta_Z(w6) has transgression beta_Z Sq3(u4)=0, since
Sq3=Sq1 Sq2 and beta_Z Sq1=0. Therefore the degree-nine fiber
piece dies, and

    H^9(P)=Z4{B9}.

## 4. The path fibration forces a nonzero d5

In the path fibration H->PP->P, ordinary cohomology suspension
satisfies

    sigma(B9)=beta4 S(P2)(v3)
             =beta4 p(v3)=V4²=2z8.

Thomas's Theorem I gives the equality S(P2)=p. Consequently
the image of H^9(P)->H^8(H) is exactly the subgroup 2Z4.
For a path fibration the transgressive subgroup is precisely
the image of this cohomology suspension: this is also immediate
from the relative definition of transgression for the pair
(PP,H), using the contractibility of PP. Thus z8 is not
transgressive.

The only differential earlier than d9 that can leave z8 is

    d5:E5^(0,8)=Z4 -> E5^(5,4)=F2{Sq1u4 tensor V4}.

Indeed the base starts in degree four; the candidate d4 target
uses H^5(H)=0, the d6 target uses H^3(H)=0, and d7,d8 use
H^2(H)=H^1(H)=0. There is no incoming differential to column zero.
The stated target has not changed on the earlier pages. Since
z8 cannot be transgressive, this d5 must be nonzero, so

    d5(z8)=Sq1u4 tensor V4.

Naturality pulls this exact differential back to the actual
sequence H->L->Y:

    d5(z8)=Sq1U4 tensor V4 != 0.

The last inequality uses U4=Sigma²u2 and Sq1U4=Sigma²v3 != 0.
There are no earlier differentials into or out of (5,4) that
could suppress this target, by the same connectivity and low
integral fiber groups. In particular the half-class fails before
any scalar degree-nine transgression; it does not extend to L.
The class 2z8 does extend, as the specified class x does.

## 5. Low Eilenberg--Mac Lane groups used above

These small integral groups can be derived from Serre's opened
mod-two polynomial theorem, coefficient exactness, and P2;
they do not require an unexamined integral table.

For K(F2,3), write v3, b4=Sq1v, c5=Sq2v,
d6=Sq2Sq1v, e7=Sq3Sq1v. Through degree eight the first Bockstein
pairs are v->b, c->v², d->e, and vb->b². The other degree-eight
monomial vc has Bockstein bc+v³, so it is not a cycle. These
give H^3=H^5=0, H^4=Z2{beta v}, and H^8=Z2{(beta v)²};
there is no higher Bockstein source in degree seven or eight.

For K(F2,5), the positive integral groups relevant here are
H^6=Z2{beta s}, H^7=0, H^8=Z2{beta Sq2s}. They follow from
the pairs s->Sq1s, Sq2s->Sq3s, and
Sq2Sq1s->Sq3Sq1s. The analogous calculation for K(F2,6)
gives H^7=Z2{beta w}, H^8=0, H^9=Z2{beta Sq2w}.

For K(F2,4), put a5=Sq1u, b6=Sq2u, c7=Sq3u,
d7=Sq2Sq1u, e8=Sq3Sq1u, and f9=Sq4Sq1u. The relevant
first-Bockstein pairs are u->a, b->c, d->e, while
beta(ua)=beta(f)=a². Its E2 terms in degrees eight and nine
are respectively the single classes u² and ua+f.

For completeness the usual integral cup_1 definition of P2
with dU=2A gives

    red2 beta4 P2(u)=u Sq1u+Sq4 Sq1u=ua+f.

To check this, use the representative U cup U+U cup_1 dU
modulo four. Expanding its coboundary with the cup_1 identity,
dividing by four, and reducing modulo two leaves U A+A cup_1 A.
The second term represents Sq4(Sq1u). The second Bockstein of u² is therefore the nonzero class
ua+f, with both groups one-dimensional. This identifies the
order-four integral class beta4 P2(u), and gives
exactly H^9(K(F2,4))=Z4 and no further summands. These are
finite consequences of the specified cochain formula and Serre
generators; no general integral-cohomology comparison is assumed.

## Scope

The new result identifies the first actual mixed differential
for the half-class, and proves that x² has zero restriction to H.
It does not assert that x² is zero on L, nor that a surviving
mixed class is stably spherical. The remaining calculation must
retain this differential and its multiplicative/coefficient
extensions. The three independent degree-fourteen tests in
root_degree14_independence.md are a separate input to that task.

## Independent reviews

The simple/higher, axioms/derivators and fibrations/groups agents
independently passed the complete mixed-differential argument.
The first two explicitly checked the possible earlier d3 on the
K(F2,5) fiber class and its vanishing by universal-path naturality.
All three checked that the entire H9(P;Z), rather than merely a
subgroup, has the stated suspension image.
