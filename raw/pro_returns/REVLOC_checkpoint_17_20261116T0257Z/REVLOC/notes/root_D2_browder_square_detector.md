# The actual Browder square: a cone detector

Root calculation, 15 November 2026, approximately18:28 UTC.
Submitted to all three independent reviewers. This record is not yet
a numbered manuscript claim. The tentative conclusion is that the
actual square vanishes, not merely that it is stably zero.

## 1. Verified target input

Let F be the3-connected double-loop fibre, E=F<5> its4-connected
double-loop cover, and chi in pi4F the bottom element. The fully
audited component calculation gives

    ker(pi9E -> H9(E;Z_(2))) = Z/2{s},
    s=rho nu6 !=0,   4pi9E=0.

The cover map gives pi9E=pi9F=pi9T. Its integral H9 map is
injective here: H9E=Z8+Z2^3, the mod-two H9 map is injective,
and the order-eight generator N maps to an odd multiple of the
unique order-eight generator of H9F. A kernel therefore cannot
occur in2Z8N, nor in the mod-two quotient.

On a cone of a homology-zero element of pi9E, the residual s is
detected by the functional operation

    Sq4(D*+r*) + Sq2(J1*).

Its value is1 on s. The full component proof, including why the
functional vanishes on every existing ten-cell, is in
EH5_pi9_cover_components.md. Here D=d6+e6 and r=e6+f6.

## 2. The detector extends from E to F

The complete eighteen-row H10F operation table gives the exact
cohomology relation

    Psi_F = Sq4(e6*) + Sq2(J1*) = 0 in H10(F;F2).

This is checked on every row. B4 and B5 have both evaluations1,
which cancel. All other rows have both evaluations0. In particular
D2 has Sq4=d6 and Pp,Q10 have Sq4=f6, so none has an e6 coefficient.

Restriction of e6* to E has value1 on both D and r. Restriction of
J1* is the J1 dual vector in the cover basis. Consequently Psi_F
restricts to the displayed s detector. Because Psi_F is already
zero on F, its cone value is independent of adding an old H10F
class to a chosen new top homology class.

## 3. The actual Browder cone and its new top class

Use the actual E2 extension of chi,

    C2S4 = Omega²S6 -> F.

The inclusion C2S4 -> C3S4 is9-connected and its first relative
cell has dimension10, attached by the Browder square of the bottom
class. Its normalization is the double-loop of the first James
twelve-cell, hence one copy of[ iota6,iota6 ], with no extra factor2.
Form the homotopy pushout with that first relative ten-skeleton.
It is the ordinary cofiber C_lambda=F union_lambda e10, where
lambda=lambda1(chi,chi).

In the source, write x4 for the bottom homology class. The class
Q6x4 in H10(C3S4;F2) has coefficient1 on the relative ten-cell.
The first-relative-ten-stage source has the same H8 and H6 as the
full source, and Q6x4 is already represented there. The Nishida
formula and the vanishing positive operations of a sphere give

    Sq_*²(Q6x4) = binom(4,2) Q4x4 = 0,
    Sq_*⁴(Q6x4) = 0.

The second equality also follows from H6(C3S4)=0. Any top-operation
Browder correction involves a positive operation on x4 and vanishes.
Thus its image v10 in H10(C_lambda;F2), with relative coefficient1,
has zero second and fourth squares. The first Bockstein causes no
missing relative generator: mod-two the first attaching boundary is
zero, and beta(Q6x4)=Q5x4 maps to xi(a²)=0 by top Cartan. Even
without that latter equality, the mod-two top cycle itself exists.

It follows that Psi_F evaluates to0 on v10. The operation is zero
on the old H10F as well, so its functional cone value on lambda is0.

## 4. Integral Hurewicz normalization must be retained

One cannot replace h_Z(chi) by a². The correct integral class is

    h_Z(chi)=a²-2c.

Indeed q:T->K(Z2,2) is an E2 map. In the base the Pontryagin
product of the bottom order-two class with itself is2c. This can
be derived from K(Z,2)=CP-infinity -> K(Z2,2): the degree-four
integral generator maps to an odd generator of Z4 because u²
pulls back nontrivially, and the CP-infinity product has coefficient2
by the primitive coproduct of its integral degree-two class.
Choose the orientation of c accordingly. The unique fibre generator
with the required mod-two reduction is therefore a²-2c.

Integral Browder derivation gives

    {a²-2c,a²-2c}=4{c,c}=8 xi(c)=0.

The terms containing a vanish because2a=0, and the exact order-eight
circle calculation gives8xi(c)=0. Thus the actual lambda has zero
integral Hurewicz image. By the integral injectivity of H9E->H9F,
its lift to pi9E lies in{0,s}.

## 5. The proposed conclusion

The cofiber map C_lambda(E)->C_lambda(F) is induced by E->F and the
identity of the attaching sphere. It preserves the relative top
generator. Naturality therefore identifies the cover functional
value with the zero value computed in Section3. Since its value
on s is1, lambda cannot be s. It follows that

    lambda1(chi,chi)=0 in pi9F,
    equivalently[widehat-chi,widehat-chi]=0 in pi11Y.

This would settle the canonical tenth-stage criterion of D.2.21.
It does not by itself extend the independent correction or their
sum through every ten-cell, and it does not settle D.2.4.
