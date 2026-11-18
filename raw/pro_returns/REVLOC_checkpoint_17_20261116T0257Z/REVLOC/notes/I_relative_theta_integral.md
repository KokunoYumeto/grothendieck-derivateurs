# The relative square class and the integral half-product

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026, 02:55 UTC. Research note; no value of the remaining
restriction class and no corrective-map realization is asserted.

## 1. The compatible representatives

Put L=Y<7>, L'=Y<10>, q:L'->L and V=Omega^4 L'. Use the one
common square-nullhomotopy normalization of D.2.42. The exact cochain
calculation in I_Hopf_transfer_test.md Section6 gives integral cochains

    dA7=4B8,
    dE15=2B8^2,
    dC15=B8^2+2D16,
    dP7=q*B8,

with D16 a cocycle and C15 reducing to the normalized square
nullhomotopy. Then

    theta4=[E15-2C15 mod4],
    Theta15=[q*C15-P7 cup q*B8 mod2],
    I15=q*E15-2P7 cup q*B8

satisfy the literal identities

    dI15=0,
    q*theta4=red4[I15]-i(Theta15),
    beta_Z(Theta15)=q*[D16]=-q*beta4(theta4),

where i:F2->Z4 sends1 to2. The products are singular products in
the displayed order. No graded-commutative chain replacement is used.
Changing the normalized square nullhomotopy by a cocycle ell changes
Theta by q*ell and theta4 by -i(ell); the identity remains valid and
I15 is unchanged. Thus the restriction datum below must always use
the D42-normalized representatives, not an independently chosen half.

By D50, 2[D16]=-b8^2 is nonzero of order two. Consequently [D16]
has exact order four. Since q*b8=0, q*[D16] has order at most two.
This is a stronger exponent statement than simply knowing that
beta_Z(Theta) is a two-torsion class.

## 2. The suspension range is sufficient for the Bockstein test

The actual evaluation epsilon:Sigma^4V->L' is16-connected.
Indeed the first counit Sigma Omega(Omega^3L')->Omega^3L'
is13-connected: Omega^3L' is6-connected and the counit fiber is
Omega(Omega^3L') * Omega(Omega^3L'). Suspending this map three
times makes it16-connected. The next three counits have successively
higher connectivity. Thus the composite has the stated bound.

It follows that fourfold cohomology suspension is an isomorphism
in degree15 and injective in degree16, also for integral 2-local
coefficients. Naturality and D42's exact normalization give

    mu11= sigma*4 Theta15,
    beta_Z(mu11)=sigma*4(q*[D16]),
    beta_Z(mu11)=0 iff q*[D16]=0.                 (1)

Therefore mu has an integral cohomology lift exactly when the
specific order-at-most-two restriction q*[D16] vanishes. Since V
is rationally acyclic of finite type, an integral cohomology lift
pairs zero with all integral H11(V;Z_(2)) classes.
Conversely the universal coefficient argument used in D45 applies
here as well: mu pairs zero on every integral H11V class exactly
when its integral Bockstein is zero. Thus (1) is an exact criterion
for target integral-homology detection. It is not a realization
criterion for maps from the prescribed finite source.

## 3. Why the source sphere condition makes this relevant

Let D=D_2^(4)M(Z2,3), and let y_D:S10->D be the actual order-four
sphere from D38/D41. Its integral Hurewicz image is the nonzero
generator of H10(D;Z)=Z2, since its mod-two Hurewicz image is Y10.
Also H11(D;Z)=0. For Q=Cof(y_D), the integral homology exact
sequence therefore gives

    H11(Q;Z)=Z,  H10(Q;Z)=0,

and the map from H11Q to the new relative eleven-cell has image
2Z. The mod-two exact sequence gives an isomorphism
H11(D;F2)->H11(Q;F2), taking the old Z11 to the reduction of a
generator gamma11 of integral H11Q. This may also be seen in chains:
the old top differential is2Y, the new eleven-cell has boundaryY,
and their difference Z-2e_new is an integral cycle with reductionZ.

After D61, the prescribed relative sphere value is zero. Any actual
relative choice v:D->V satisfying v y_D=0 therefore extends across
Q, with the chosen nullhomotopy, and

    <v*mu,Z11>=<bar(v)*mu,red2 gamma11>.

Thus q*[D16]=0 would exclude every required value-one correction,
not merely a particular choice. If q*[D16] is nonzero, an integral
target class detected by mu exists, but it need not be the image
of gamma11 under any map Q->V. The finite attaching constraints
remain a separate task.

## 4. The exact coefficient evaluation on integral target cycles

Because [I15] is torsion, it pairs zero with every integral cycle.
For z' in H15(L';Z_(2)) the compatible identity consequently gives

    <q*theta4,red4 z'>=-2<Theta15,red2 z'> in Z4.   (2)

The mod-two pullback q*theta alone gives no such detector: it is the
reduction of [I15] and pairs zero with every integral cycle.
Here its stronger membership in Sq1 H14(L';F2) needs an actual
exponent argument, not merely the existence of that integral lift.
Let C14 be the original half-product cochain, so dC14=A7 B8-2E15.
Because H7(L';Z_(2))=0, choose R6 with dR6=q*A7-4P7. Then

    K14=q*C14-R6 cup q*B8,
    dK14=-2(q*E15-2P7 cup q*B8)=-2I15.

Thus 2[I15]=0 and q*theta=Sq1[K14 mod2]. This also follows
from i(q*theta)=q*(a7 cup red4 b8)=0, since q*a7=0, but the
displayed chain proof records the exact compatible representative.
The value in (2) retains the coefficient-two information lost by
that reduction. It is unchanged under the joint D42 normalization,
provided theta4 is changed along with Theta as in Section1.

No value of q*[D16], no integral lift of mu, and no actual map
Q->V with value one is proved by this note. The next exact target
calculation is the restriction of the particular half-square
class [D16] to L', or equivalently beta_Z(mu11).

## 5. The finite Postnikov-base reformulation

In L'->L->P9L, base positive degrees start at7 and fiber positive
degrees at10. Hence the first mixed Serre term has total degree17.
The degree16 kernel of restriction to the fiber is therefore
exactly the image of H16(P9L;Z_(2)). Equivalently,

    q*[D16]=0 iff [D16] is in im(H16(P9L;Z_(2))->H16L).

This is a finite integral base-image problem. It cannot be decided
by halving the base square: its mod-two reduction y8^2 is nonzero
on P9L by D42, so that base square is not itself twice an integral
class. On L its image is twice D16 and has order two. The unknown
is whether some other class of the full coupled P9L has image D16,
including its possible higher coefficient extensions.

Root independently derived this same edge-image criterion. The
fibrations and axioms readers independently confirmed the integral
top-cycle consequence for Q. None inferred a value of q*[D16].
