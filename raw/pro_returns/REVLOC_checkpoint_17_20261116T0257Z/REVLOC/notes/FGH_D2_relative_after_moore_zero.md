# The finite relative source after the Moore composite vanishes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Research reduction following D.2.61.
The source calculation below is exact and was independently read and
passed by the fibrations agent. The target evaluation on this source
remains to be computed; no full extension is constructed.

## 1. The new exact constraint

Retain D.2.38--D.2.42 notation:

    M=M(Z2,3), D=D2^(4)M, U=Omega4 L,
    V=U<6>=Omega4(L<10>),
    y_D:S10 -> D,
    mu11 in H11(V;F2).

D.2.41 identifies the value of the relative correction on the actual
sphere y_D with minus h_M l4. D.2.61 now proves that this value is zero.
Therefore every correction arising from an ordinary full extension
must satisfy

    v_D y_D=0 in pi10 V.

This is stronger than the earlier statement that it is a double, or
that its mod-two Hurewicz vanishes. Choosing an actual nullhomotopy
gives a factorization through the actual cofiber

    Q=Cof(y_D:S10 -> D).

Conversely every map Q->V restricts to a map D->V satisfying this
one sphere constraint. This converse concerns only the finite sphere
constraint, not extendability to the entire relative source.

## 2. The complete finite quotient model

D.2.38 provides an actual ten-stage (or its equivalent stable model,
uniquely realized in the required attaching degrees)

    D10=R vee S10_y,
    pi10 R=Z2{zeta} + Z4{n} + Z2{t},

and its final eleven-cell attaches by

    2y+zeta+2d n+e t,       d,e in F2.

Here R has dimension ten and H10(R;Z_(2))=0. Its degree-ten X cell
has nonzero integral boundary; this also follows directly from the
literal D.2.38 chain reduction. The actual y_D need not equal the
initial free sphere inclusion. Since D is obtained from D10 by one
eleven-cell, y_D lifts to pi10D10. Its free y coefficient is odd:
its mod-two Hurewicz is exactly Y10. Write a lift as o y+w, with
o an odd unit and w in pi10R.

Replace the free sphere coordinate by o y+w. This is an actual
equivalence under R: the relevant pi10 groups of five-connected
spaces are in the stable range, and the map is an integral localized
homology equivalence. Rescale the final cell by the same odd unit.
The attaching map becomes

    2y_D + tau,
    tau=zeta+2d' n+e' t.                         (1)

Only the even n coefficient can change under the doubled torsion
correction; retaining d',e' avoids fixing an unproved normalization.
The coefficient of zeta stays odd and hence is one. All terms of tau
have order at most two and its zeta coordinate is nonzero. Thus tau
has exact order two in pi10R, independently of the remaining bits.

To form Q, attach a second eleven-cell along y_D and cancel that
cell with the free ten-sphere. Equivalently, collapse the contractible
mapping cone of the new sphere inclusion. This yields the actual
homotopy type

    Q ~= R union_tau e11,       |tau|=2.          (2)

The original eleven-cell maps with mod-two top degree one to the
remaining cell. This is not a claim that tau is zero, nor a replacement
of (2) by a wedge with a free eleven-sphere.

## 3. Integral homology and the unspherical top

The lower integral homology is unchanged from D:

    H6Q=Z2, H7Q=Z4, H8Q=Z2, H9Q=Z2,
    H10Q=0, H11Q=Z_(2).

One can also read the last two groups from the cofiber sequence for
y_D: its integral H10 image is the generator of H10D=Z2. The map
H11Q -> H10S10 has image 2Z_(2).

In the model (2), the top pinch H11Q -> H11S11 is an isomorphism.
The stable cofiber sequence gives sphere pinch image

    im(pi11^sQ -> pi11^sS11)=2Z_(2),

because tau has exact order two. Ordinary pi11Q surjects onto the
stable group by Freudenthal at the endpoint for a five-connected
space. Consequently the integral Hurewicz image of actual S11 maps
in H11Q is exactly 2Z_(2). In particular no actual sphere represents
the mod-two top class. This is the first remaining coherence in the
finite quotient; the vanishing of h did not remove it.

In degree ten, where ordinary stabilization is an isomorphism,

    pi10Q = pi10R/<tau> = Z4{n} + Z2{t}.

All these classes have zero integral Hurewicz, because H10Q=0.

The source operations are those of D.2.38 with Y10 removed:
the top z11 has beta z11=0,

    Sq2_*z11=W9,       Sq4_*z11=S7,
    Sq3_*z11=Sq5_*z11=0.

The lower Bocksteins and square operations are unchanged. Thus the
top has become an integral cycle, but it remains a non-spherical
class with two nonzero primary descendants.

## 4. Exact remaining target question

Because V is a five-connected loop space, the endpoint mapping
argument of D.2.41 identifies actual and stable maps from Q (and R)
to V. The precise contravariant cofiber sequence is

    [Sigma R,V] -> pi11V -> [Q,V] -> [R,V]
                                            --tau*--> pi10V.       (3)

The finite paired-coefficient correction exists precisely when
there is a map F:Q->V with

    <F*mu11,z11>=1.                              (4)

If a lower map R->V kills tau, its extensions form the orbit under
pi11V, with the first map of (3) recording the identification of
nullhomotopy choices. Changing an extension changes (4) by the
spherical mu evaluation. Neither that spherical evaluation nor the
initial top value of an arbitrary tau-null lower map is computed
by h_Ml4=0.

The original fixed canonical C4M map still has paired value one
and still fails its C6 extension by D.2.29: beta Q8B0=Q7B0 in C6,
whereas the two target outer-square coefficients are not first-
Bockstein boundaries. For an arbitrary extension, a correction
must therefore realize (4) before this degree-twelve source test
can be passed. The new theorem removes the specified pi10 sphere
obstruction and leaves the exact order-two coextension (2).

Even a solution of (4) would only pass this finite necessary test.
It would not ensure that F extends over the weight-three and higher
parts of C4M/M, over further stages toward QM, over the full source
Q Sigma B, or through later nullification cones. Those distinctions
remain part of D.2.4.

## 5. Why the new stable detecting sphere is not already a correction

The complementary target calculation is saved in
notes/EH5_k4_quotient_target.md. It proves that the map

    pi15 D2L -> [Sigma4 Q,D2L]

induced by the top pinch is injective. In its cofiber sequence the
preceding homomorphism is induced by Sigma5 tau. Any map
Sigma5 R->D2L factors through its last two cell factors; their possible
degree-fifteen precompositions are bottom eta terms, killed by the
intrinsic Thom sixteen-cell in D2L. This is the exact reason for that
injection, rather than a claim that Q has a spherical top.

Consequently a stable sphere f:S15->QL with JH(f)=2c, as now supplied
by D.2.61, still has nonzero James--Hopf obstruction after precomposition
with Sigma4 Q->S15. It cannot simply be desuspended into the required
actual correction. A different construction would have to use a
nonzero lower map on Sigma4 R and its coherent extension. That lower
map is not eliminated by H10R=0: H9R=Z2 supplies a possible Tor
coordinate in degree fourteen for the quadratic target.

The source and target reductions together identify the remaining
problem more narrowly without claiming either existence or
nonexistence in (4).

## 6. Current target tests, not conclusions

The exact source model suggests testing whether an attempted top
coefficient forces f(tau) to be the now known nonzero order-two class
q=alpha sigma-prime in pi10V. This has not been proved. A prerequisite
is to determine the actual Hurewicz of q in V, equivalently in the
nine-connected cover L'. Every tau in (1) has zero integral and mod-two
Hurewicz, since H10R=0 and its sphere cannot hit the Tor coordinate.
Thus a nonzero Hurewicz of q upstairs would rule out this particular
mechanism. The known zero Hurewicz in L or Omega L does not settle
the connected-cover value.

Independently, the source agent is testing whether the actual class
mu has an integral lift. Such a lift would force (4) to vanish:
H11Q is integral free, whereas V is rationally acyclic, so every
integral cohomology evaluation on the image of that generator is zero.
The exact proposed coefficient criterion is beta_Z(mu)=0, expressed
after four suspensions as the pullback of the order-four half-square
class D16 to L'. Its value is still under investigation. Neither
the new stable theta class nor h=0 alone proves this integral lift.
