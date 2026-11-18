# The actual two-stage base for the integral target calculation

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. The identification of the six-type below is proved;
the degree-sixteen integral product is not evaluated by that identification.

**16 November 2026 update (D.2.50):** the separate actual canonical-cobar
argument in `I_integral_square_cobar.md` proves that b8 squared is nonzero
of exact order two, and that the half-product detects an integral
fifteen-class of order at least four. The stable-spherical pairing remains
open. Sections4--5 below record the earlier unresolved reduction, retained
for its exact chain/coefficient distinctions; they are superseded only
where they leave the total square undecided.

Put B=K(F2,2), Y=Sigma²B, Z=Y<5>, and L=Y<7>.
The established actual groups are pi4Y=F2, pi5Y=0, pi6Y=F2.
Write U4=Sigma²u2 for the mod-two bottom cohomology class.

## 1. The exact six-type

The only possible six-stage invariant belongs to

    H7(K(F2,4);F2)=<Sq3 u4, Sq2 Sq1 u4>.

It is nonzero. Indeed Y->P6Y induces an isomorphism on homology
through degree six, and H6(Y;F2) has dimension one. If the invariant
were zero, P6Y would be K(F2,4) times K(F2,6), whose degree-six
cohomology has two independent classes, Sq2u4 and the second
factor's fundamental class. This contradicts that isomorphism.

The invariant must pull back to zero on Y. Suspension compatibility
and Serre's calculation for B give

    Sq3 U4=Sigma²Sq3u2=0,
    Sq2 Sq1 U4=Sigma²(Sq2Sq1u2)=Sigma²w5 != 0.

These identify the nonzero invariant uniquely. Consequently

    P6Y = fib(Sq3:K(F2,4)->K(F2,7)).                    (1)

This is a space-level equivalence over K(F2,4), with the standard
nonzero generator of pi6. It uses the actual low groups, not a
guess from a suspended cell matrix.

Since Sq3=Sq1 Sq2, (1) can equivalently be written as the homotopy
pullback of the coefficient fibration

    K(Z4,6) --red2--> K(F2,6) --Sq1--> K(F2,7)

along Sq2:K(F2,4)->K(F2,6). In particular a map into P6Y consists
of the bottom class together with a specified mod-four lift of
its second square, including the compatibility homotopy.

For Y itself, H6(Y;Z)=Z4 and H5(Y;Z)=0, by the established
integral H4(B)=Z4 calculation. Thus the nonzero class
Sq2U4=Sigma²(u2²) has an odd mod-four lift C6 in H6(Y;Z4).
The actual Postnikov projection corresponds to one such lift.
Changing the lift by twice a generator does not change its mod-two
reduction; this choice is not silently discarded when cochain
normalizations are needed later.

## 2. The two actual fiber sequences

The model fixes the actual maps in

    K(F2,3) -> Z -> Y,
    K(F2,5) -> L -> Z.                                (2)

The first is the fiber of the bottom class U4. The second is the
fiber of the fundamental class p6 in H6(Z;F2): Z is five-connected,
pi6Z=F2, so Hurewicz identifies that class. In the coefficient
pullback model, the restriction of C6 to Z is i(p6), where
i:F2->Z4 sends 1 to 2. Indeed the fiber of the pullback over the
basepoint of K(F2,4) is K(F2,6), and its map to K(Z4,6) is exactly
that coefficient inclusion. This also identifies the required
integral normalization without replacing the fiber fundamental
class by an arbitrary lift of a homology class.

Looping (1) gives the familiar two-stage fiber

    Omega P6Y = fib(Sq3:K(F2,3)->K(F2,6))
              = fib(u3²:K(F2,3)->K(F2,6)).              (3)

The equality on the right is the unstable identity Sq3u3=u3².
It must not be read as a product splitting. Looping once more
kills that square as a cohomology class, but any resulting
space-level splitting does not supply the needed coherent
multiplication or integral product data on L.

## 3. A permissible Pontryagin-square normalization

The lift in Section 1 can be chosen to be

    C6 = Sigma² P2(u2) in H6(Y;Z4),

where P2:H2(-;F2)->H4(-;Z4) is the ordinary Pontryagin square.
Its reduction is u2², so P2(u2) is an odd generator of
H4(B;Z4)=Z4 and its double suspension is an odd generator
of H6(Y;Z4). This fixes an actual lift, not only its reduction.
For example the usual integral-cochain definition
U cup U + U cup_1 dU modulo four, for an integral lift U of
u2, makes the reduction property immediate. Only this standard
normalization property is needed here; no suspension formula
for the Pontryagin square is being used to compute a product.

The two odd choices of C6 give equivalent Postnikov projections
over the fixed bottom class. Indeed multiplication by -1 on
K(Z4,6) is an automorphism over K(F2,6), and is the identity on
the coefficient fiber K(F2,6). It induces an automorphism of
the displayed homotopy pullback, fixes both homotopy groups of
P6Y, and exchanges the two odd lifts on Y. Their fibers are
therefore equivalent over Y. Thus using Sigma²P2(u2) is an
allowed normalization of the actual six-type, not a new
assumption on Y. The compatibility homotopy in the pullback is
still part of the map. In this range changing it does not add
an unseen choice: the coefficient reduction map
H5(Y;Z4)->H5(Y;F2) is onto, because H4(Y;Z)=Z2 and H5(Y;Z)=0,
so the preceding term removes that homotopy ambiguity.

The root independently checked the six-type argument. This
normalization does not identify any of the degree-sixteen
multiplicative extensions described next.

### The fundamental a7 as an actual secondary Pontryagin class

There is a second normalization, directly for the degree-seven
class in the transfer calculation. Thomas's Theorem I and
Proposition 6.9 say S(P2)=p and S(p)=0. Hence

    P2(U4)=0 on Y=Sigma²B.

Choose a nullhomotopy, or equivalently a lift

    Y -> fib(P2:K(F2,4)->K(Z4,8))

over the bottom map U4. Passing to fibers over K(F2,4) gives an
actual map a_Z:Z->K(Z4,7). Its restriction to L is the fundamental
coefficient class a7, after choosing the sign of that generator.
Here is a direct test of the coefficient. The generator
alpha=u4 nu4:S7->Y lifts to L. The actual cone map

    HP² = S4 union_(nu4) e8 -> Cone(alpha)

fixes the bottom map u4 and has top-cell degree one. The pulled-back
bottom mod-two class is the reduction of the integral HP² generator;
its Pontryagin square is the mod-four reduction of the integral
square, and evaluates to one on the top cell. The usual defining
relative pairing for the chosen nullhomotopy therefore evaluates
a_Z on alpha as an odd generator of Z4. This is a cone calculation
of the map to the fiber, not an assumed primary formula for a7.

Moreover the restriction to L is independent of the choice of that
nullhomotopy. A different choice adds the pullback of a class in
H7(Y;Z4). Its value on alpha is zero, since alpha factors through
S4 and hence has zero ordinary integral Hurewicz in Y. The space L
is six-connected, H7(L;Z)=Z4 is generated by alpha, and H6L=0;
the coefficient universal-coefficient theorem then says that the
whole pullback class is zero. Thus the transfer class a7 is a
choice-independent secondary Pontryagin class on this actual L.

The primary Thomas source was reopened at
<https://msp.org/pjm/1959/9-3/pjm-v9-n3-p26-p.pdf>:
Theorem I is on pp.897--898 and Proposition 6.9 on p.908.
This identification fixes the class and its integral Bockstein;
it does not yet calculate the integral square of that Bockstein.

The root independently reopened these exact passages and passed the
actual lift, HP2 coefficient test, and choice-independence argument
on 16 November 2026.

## 4. The remaining integral extension

The target class b8=beta4(a7) of I_Hopf_transfer_test.md is an
integral order-four class. Its square has zero mod-two reduction.
The question is whether b8² vanishes integrally or persists as an
even torsion class, and, more specifically, whether its associated
half-product theta pairs with a stable-spherical integral H15 class.

The two Serre sequences (2) give a concrete way to attack this,
but their associated graded groups alone do not determine that
square. Coefficient extensions and multiplicative extensions must
be fixed. In particular a mod-two differential killing the reduction
of an integral class can make the integral class divisible by two;
it need not kill the integral class. Neither the pullback model
(1) nor the square description (3) is being used to suppress this
possibility. No numerical value for b8² or the stable pairing is
asserted in this note.

The primary input for the two mod-two generator computations is
Serre, *Cohomologie modulo 2 des complexes d'Eilenberg--MacLane*,
Section 2, Theorem 2 and the explicit low K(F2,2) generators
(bibliography key I_Serre1953). The exact coefficient-fibration
identity is proved directly by the short exact sequence
0->F2->Z4->F2->0. The low actual homotopy groups and integral
H4(B)=Z4 have already been proved and source-audited in D.2.17--18.

## 5. The actual low Browder comparison and its remaining even term

This is a precise chain-level boundary for the current attempt, not an
evaluation of the square. Let M=M(Z/2,2) be the bottom Moore subspace
of B, let T=Omega²Y, and choose an actual U:S5->C2M->T representing
the integral class xi a and hence alpha=u4 nu4 after double adjunction.
The actual Browder map

    f:Sigma(S5 smash C2M)=Sigma6 C2M -> T

lifts uniquely to E=Omega²L: its source is seven-connected and the
Postnikov quotient T/E has homotopy only below degree five. The same
connectivity gives uniqueness of the homotopies used below.

There are two genuine nullhomotopies. First 4f=0. Its double adjunct
is the generalized Whitehead product of alpha:S7->Y and the evaluation
Sigma²C2M->Y. Their desuspended source factors are S6 and Sigma C2M,
both suspensions, so Arkowitz's bi-additivity theorem applies and
gives 4f=[4alpha,evaluation]=0. Second, the restriction to the actual
U5 sphere in the second factor is zero: its double adjunct is
[alpha,alpha]=alpha_*[iota7,iota7]=0, using the H-space structure on S7.
These statements concern actual maps and homotopies, and do not follow
merely from their homology values.

The integral quadratic configuration chains, independently checked by
the root's exact certificate code/D2_C2_Moore_integral_chain.py, are

    da2=0, db3=2a2, U5=e1(aa),
    H6=e1(ab), J6=e1(ba),
    dH=ab-ba-2U, dJ=ba-ab-2U,
    D6=-H-J, dD=4U,
    V6=bb-H+J, dV=0,
    Z7=e1(bb), dZ=2V.

In particular V=bb+D+2J. The mod-two reduction suppresses the final
2J, but it must be retained in the actual integral comparison. The
finite source has integral homology Z/2 in degree four, Z/4{U} in
degree five, and Z/2{V} in degree six. Its stable six-skeleton is
C_1^6 wedge M(Z4,5), and the seven-cell attaches by gamma_C+i_U eta5;
the fibrations agent is recording that independent finite-source proof.

After one homology suspension the comparison concerns the mixed Moore
cycle z=u6 D7-D7 u6 in Omega L. In the next displayed formula only,
a,b denote the suspended James letters of degrees three and four,
with db=2a, so u maps to a² and D maps to ba-ab. The formal ambient
tensor boundary

    d(aabb-2baab+bbaa)=2z

does not prove that the boundary lifts to Omega L. In the actual
Browder comparison, the omitted even term is represented by
4 sigma{U,J}, with the signs dependent on the chosen displayed
orientation. The identity 4f=0 is not a justification for setting
this expression to zero: J is not a cycle, and a chain homotopy
for 4f contributes its value on dJ. Likewise the separate nullity
of f(U) does not supply a simultaneous relative nullhomotopy.

Thus the exact missing datum is a compatible relative comparison on
this finite quadratic source (or an equivalent actual integral Serre
extension), not another calculation of its primary Steenrod squares.
No order drop for z, integral square vanishing, or James--Hopf image
is inferred from the two nullhomotopies above. The root and source
agent independently checked the scope of the bilinearity and the
S7 Whitehead-square argument.

## 6. The square restricts to zero on the actual Milgram fiber

16 November 2026. This is an exact filtration reduction; it does not
evaluate the remaining mixed Serre extension.

Write H=Omega P6Y. There is an actual fiber sequence

    H -> L -> Y,
    H = fib(v3^2:K(F2,3)->K(F2,6)).

On the K(F2,3) fiber of Z->Y, the actual class a_Z constructed in
Section 3 restricts to Thomas's suspended operation

    p(v3)=2 v3 beta_Z(v3) in H7(K(F2,3);Z4).

Put V4=beta_Z(v3). Directly from integral representatives dv=2V,
the integral connecting class beta4(a_Z) restricts to V4^2: the
representative 2vV has differential 4V^2. Consequently the class
b8=beta4(a7) on L restricts on H to the pullback of V4^2.

This restriction is nonzero, but its square is zero. To see the
second assertion first, on H the class v3^2 is null, and Cartan
gives

    red2(V4^2)=(Sq1 v3)^2=Sq2(v3^2)=0.

The integral coefficient sequence therefore gives V4^2=2z8 on H.
Since V4 has order two, 2V4^2=0, so 4z8=0. It follows that

    (b8|H)^2=4z8^2=(4z8)z8=0.

For nonzeroness, use K(F2,5)->H->K(F2,3). The class V4^2 in
integral degree eight on the base is nonzero because its mod-two
reduction is the nonzero polynomial class (Sq1 v3)^2. No integral
Serre differential can hit it: the fiber has no positive integral
cohomology below degree six, and H7(K(F2,5);Z)=0. The only potential
sources for base degree eight would thus be bidegrees (1,6) and
(0,7), both zero. Hence its pullback to H is nonzero and z8 has
exact order four.

The half can also be expressed by a coefficient lift. The mod-two
class v3 Sq1v3 has first Bockstein (Sq1v3)^2, which is zero on H.
Choose a mod-four lift c7. Then

    2 beta4(c7)=beta_Z(v3 Sq1v3)=V4^2.

Thus z8 may be chosen to be beta4(c7). This specifies its coefficient
origin; the lift c7 is not asserted to extend to L. Indeed, its
possible mixed transgressions in H->L->Y are precisely relevant.

There is also a general elementary square-zero statement useful for
interpreting the reduction. For a fibration over a suspension, the
kernel of restriction of cohomology to the fiber has square zero.
Cover the suspension by its two cones and pull the cover back to
the total space. The two inverse images each retract to a fiber.
A class restricting to zero on a fiber therefore lifts to relative
cohomology with respect to either inverse image. Relative cup
product, using the two different inverse images for the two factors,
lands in the cohomology relative to their union, which is zero.
This proof works with arbitrary constant coefficient rings.

Applied to H->L->Y, it says that b8^2 belongs to a square-zero
restriction ideal. It does NOT imply b8^2=0: b8 itself has the
nonzero restriction just computed. The exact unresolved quantity
is the mixed/base-filtration class represented by b8^2, or its
half-product pairing on the stable-spherical part of integral H15.

## 7. The exact total-degree-eight multiplicative extension

16 November 2026. Independently audited and passed by the root.
This identifies the nonzero class 2b8; it still does not compute b8^2.

First, in the universal path fibration over P=P6Y, the mixed term
E5^(4,4)=F2{u4 tensor V4} supports

    d5(u4 tensor V4)=2B9,
    B9=beta4 P2(u4) in H9(P;Z)=Z4.

There is a short exact reason fixing this coefficient without an
assumed integral product formula. After the independently established
d5(z8)=Sq1u4 tensor V4, the remaining first-column degree-eight
group is <2z8>=Z2. The only possible incoming differentials to base
degree nine are d5 from (4,4) and d9 from that remaining Z2. Since
the universal path total space is contractible, d5 must hit the
unique order-two subgroup <2B9>, and then d9 hits the remaining
quotient. The (4,4) group survives to E5: its only potential earlier
incoming map is d4 from (0,7), which is zero for the reason below.

In fact H7(H;Z)=Z2{beta_Z Sq2 Sq1v3}. This follows directly from
K(F2,5)->H->K(F2,3); the only degree-seven integral class is the
displayed base class, and beta_Z(v3^2)=0. It is the cohomology
suspension of beta_Z Sq2 Sq1u4 in H8(P;Z), so is universally
transgressive. In particular its d4 vanishes.

Pull back to the actual H->L->Y. Since P2(U4)=0, the base class
B9 pulls to zero. Thus d5(U4 tensor V4)=0. No subsequent outgoing
differential from (4,4) is possible, and its only possible incoming
one was the just-excluded d4. It gives a nonzero E-infinity term.
On the other hand the universally transgressive degree-seven fiber
class now has

    d8(beta_Z Sq2 Sq1v3)
      =beta_Z Sq2 Sq1U4
      =Sigma² beta_Z w5 !=0.

This is the entire base H8(Y;Z)=Z2; it has no earlier incoming
differential and hence is killed exactly here. The first-column
term <2z8> survives, either by naturality of d9 and B9|Y=0 or
by the already existing global class b8 with this restriction.

The only three possible total-degree-eight terms were (0,8),
(4,4), and (8,0); the last is killed. Since six-connectivity and
H7(L;Z)=Z4 give H8(L;Z)=Z4{b8}, the resulting filtration is
therefore exactly

    F4 H8(L;Z)=<2b8> = Z2,
    gr4(2b8)=U4 tensor V4,
    H8(L;Z)/F4=<2z8>=Z2,
    F5 H8(L;Z)=0.

In particular the pullback of the entire base H8(Y;Z) is zero.
The class 2b8 is a mixed class, not a base pullback. This distinction
must be retained in any attempt to evaluate b8^2 or its associated
stable-spherical half-product.
