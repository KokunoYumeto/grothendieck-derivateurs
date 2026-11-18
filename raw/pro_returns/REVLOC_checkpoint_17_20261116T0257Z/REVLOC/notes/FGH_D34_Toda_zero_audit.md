# Independent audit of the remaining once-suspended Toda bracket

15 November 2026, 20:50 UTC. The fibrations and axioms agents independently
reached the same cone argument. This note records the exact ordinary-map
interfaces; the assigned manuscript owner will supply the numbered result.

Put B=K(F2,2), Y=Sigma²B and T=Omega²Y. Let rho:S6->T be the
class of D.2.18, and write rhoY:S8->Y for its double adjunct. Let
h0=eta2 smash id_B:Sigma Y->Y. The class lambdaY in pi9Y is the
double adjunct of the R-detected generator of pi7T.

## 1. The actual representative of lambda

The ordinary map

    h0 Sigma(rhoY):S9 -> Y

is lambdaY. Indeed, rhoY has mod-two Hurewicz image Sigma²f. The
once-adjoint h0':Y->Omega Y sends this class to ac+ca. This is the
exact low quadratic Adams--Hilton calculation already proved in the
eta-extension note: the cofiber is CP² smash B, its reduced diagonal
gives ac+ca, the linear part vanishes, and tensor words of length three
begin in degree nine, above the degree-eight calculation. The once
adjunct of h0 Sigma(rhoY) therefore has this nonzero Hurewicz image.
D.2.19 gives pi9Y=Z/2, whose generator is detected by the same image
sigma(R)=ac+ca. Thus the equality is of actual homotopy classes.

## 2. The lower Toda bracket has a null representative

D.2.19 proves the actual equality rho eta6=0. Choose an ordinary
extension

    rhoBar:Ceta6=S6 union_eta6 e8 -> T.

Since eta6 has order two, choose a coextension of degree two,

    Gamma:S8 -> Ceta6,
    pinch Gamma = 2:S8->S8.

Equivalently Gamma is the usual representative used to define
<rho,eta6,2>. The group H8(Ceta6;F2) has only its top-cell generator,
and pinch is an isomorphism on it. Therefore Gamma has ZERO mod-two
Hurewicz image. Naturality gives h2(rhoBar Gamma)=0. D.2.20 proves
that the ACTUAL Hurewicz homomorphism pi8T->H8(T;F2) is injective.
Consequently

    rhoBar Gamma = 0 in pi8T.

This proves that the lower bracket contains zero. No generalized
metastable identification, stable lift of an arbitrary map, or
unproved Hurewicz statement is involved.

## 3. Carry the chosen null representative to the desired bracket

Take two adjoints of the chosen extension and coextension. The source
cone is literally Sigma²Ceta6=Ceta8, and Sigma²Gamma still has top
pinch degree two. Their composite is the double adjunct of the null
map above. Hence it gives a zero representative of

    <rhoY,eta8,2> subset pi10Y.

Suspend these specified maps ONCE and postcompose the extension with
h0. Its bottom restriction is h0 Sigma(rhoY)=lambdaY, and the resulting
composite is still null. This constructs a zero representative of

    <lambdaY,eta9,2> subset pi11Y.

All source cones here are sufficiently connected to lift uniquely
through Z=fib(Y->K(F2,4)); adjunction identifies this with the
bracket Delta=<lambda,eta8,2> subset pi10W, W=Omega Z, used in D.2.33.
The full indeterminacy is already proved zero in D.2.33:

    lambda pi10S8 + 2 pi10W
      = <lambda eta8²> + 2 pi10W = 0.

Thus Delta is exactly zero, not merely a bracket containing zero with
uncontrolled additional values. D.2.33 then rules out epsilon=1 for
every full once-suspended attachment.

## Scope and source audit

The new calculation uses only the exact earlier results D.2.19,
D.2.20, D.2.31, D.2.33 and the low eta-map calculation already sourced
to the opened Halperin--Lemaire quadratic cone model. All cone,
adjunction and Toda constructions in the argument are explicit.
It settles the once-suspended coefficient; it does not settle the
fourth-suspension coefficient or propagation through later cones.

The axioms agent reread the saved statements and the exact
indeterminacy in the manuscript on 15 November 2026 before recording
this pass. The fibrations agent reached the same inner-cone proof
independently, without relying on this note.
