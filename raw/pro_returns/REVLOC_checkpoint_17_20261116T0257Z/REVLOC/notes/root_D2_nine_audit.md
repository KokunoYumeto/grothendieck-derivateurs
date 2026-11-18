# Independent audit of the nine-skeleton calculation

GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15 November 2026.
Status: mathematical calculation passes; final wording under assembly.

## Primary formulas and finite algebra

Root enumerated all26 degree-nine free double-loop monomials and
checked the11-dimensional fibre basis. The mixed terms and base
labels account for the other15 dimensions. In particular {a,x},
whose second square is R, must not be omitted.

Root visually reread the original CLM ChapterIII Theorem1.3 on
printedpp217--218, in FGH_CLM_114_right.png and FGH_CLM_115_left.png.
For the top operation on c4, the partition(0,2) gives the nonlinear
term {c,Sq2c}=R. For Sq4 only the binomial term i=2 survives,
giving xi a. The correction aR+a²xi a cancels exactly the four
extra coproduct terms of xi c.

Root independently wrote code/D2_fiber_poly_check.py. It constructs
the coproduct dual to the polynomial Serre algebra and computes
Steenrod operations by Cartan. It checks13 polynomial fibre classes
through degree9, their complete coproducts, and39 Sq1/Sq2/Sq4 values.
All assertions pass; output is code/outputs/D2_fiber_poly_check.json.
This certificate does not claim to prove the top-operation, Browder
or homotopy interfaces, which were checked separately.

## A correction discovered during integral normalization

The initial proposed stable group Z4 plus two Z2 summands is
SUPERSEDED. The complete first-Bockstein cycle basis in degree9 is

    UA, N, K1, K5, K2+K3+K4, Pn, Pm+ZA.

The first five have zero second Bockstein. N and the K sum have
actual integral cycles: e1(cc) with the product corrections, and
lambda(a,x)-lambda(b,y), with dx=2y, db=2a and dy=0. For the
other three one has, in T and then after the actual projection to F,

    UA=beta(zu), K1=beta({b,f}+bR), K5=beta{b,k}.

BOTH remaining classes have second Bockstein C=c². The identity
for Pn is [Pn]=[n]+[c][d]. The additional identity is

    Pm+ZA=m+ag+ce+bf,
    beta(bg)=ag+bf,
    [Pm+ZA]=[m]+[c][e].

Since beta2d=beta2e=c, base/fibre separation forces beta2m=beta2n=0
and gives beta2=C in both rows. Root independently confirmed the
correction immediately after the fibrations reviewer identified it.
Thus Z0=Pm+ZA+Pn has zero first and second Bockstein. Because H8F
has exponent at most4, even column corrections give exact zero
integral boundary while retaining Sq2Z0=P+Q and Sq4Z0=z. This
extra relation is essential; a dimension count alone misses it.

## Component calculation

Root independently computed pi8C from the Chang cofiber. It injects
into Z8{nu5}+Z2{eta6²} with image ker((x,y)->2x+4y). Thus it is
Z4 on omega whose quotient is(2nu5,eta6²). The seven-cell maps
kill2omega, since delta eta² has quotient(4nu5,0). The Moore
summand has pi8M4=Z4{i nu5}+Z2{b eta}; the specified order-two
top-eta lift b gives the second summand.

The important remaining relation is kappa eta=omegaBar+b eta.
In C'=C union_delta e7_Q, pi8C'=Z2 omegaBar. A lift kappa' of
degree2Q has Sq2 vector e6 by Adem. Its quotient to
Ceta(bottom5) vee S6 has S6 component eta, so kappa' eta has
nonzero eta² component and equals omegaBar. The normalized
kappa of D.2.19 differs by b and possibly bottom nu, whose eta
composite is zero. This proves the stated relation with the
required earlier normalization, rather than an unspecified lift.

The eight-cells kill b eta,c eta and omegaBar. The other kernel
lift theta lies entirely in C vee S6 plus the P+Q seven-cell;
therefore its double involves only omegaBar and c eta, now killed.
The ENTIRE torsion in pi8L8 is consequently

    Z4{n=alphaBar nu}+Z2{theta}+Z2{lambda eta}.

Theta has Sq2 vector P+Q and Sq4 vector z. The fourth-square
coefficient also follows from Sq2Sq3=Sq5+Sq4Sq1 on the bottom
four-class, using absence of degree-eight cohomology in that cone.
The other detectors are Sq2=R for lambda eta and Sq4=u for
the parity of n.

N and K2+K3+K4 have zero integral boundaries and no theta
component. Their exact attaching maps are lambda eta plus an
odd multiple of n, and lambda eta plus an even multiple of n.
Their difference kills n, then lambda eta. The zero-boundary
Z0 kills theta. This controls every previously hidden torsion
component, including the possible even-nu coefficient.

## The full stable group as a lattice quotient

Once that torsion is killed, no free-lift ambiguity remains. The
integral Hurewicz image of pi8L8 in the eight-cycles is

    L=Z_(2){W,J2}+2Z_(2){C,J1,M-L}.

The kernel of the preceding attaching matrix gives this lattice:
W,J2 are free spheres and C,J1,M-L have order-two attachments.
The complete Bocksteins give the boundary lattice

    B=4Z_(2){C}+2Z_(2){W,J1,J2,M-L}.

Its index agrees with H8F=Z4 plus four Z2 factors; the four
first-Bockstein images fix the order-two generators. Thus

    pi8 Sigma-infinity F=L/B=(Z2)^3,

with injective integral Hurewicz and image generated by2C,W,J2.
The mod-two Hurewicz kernel is exactly the class a with integral
image2C. In particular alphaBar nu and lambda eta vanish stably.

## Ordinary-space exclusion and source consequence

The double-loop unit of the three-connected F has a left inverse.
Its double suspension is five-connected, so pi10 of that double
suspension is stable. Therefore ordinary pi8F injects as a split
subgroup of the computed stable group. No equality is assumed.

The stable kernel class a cannot be an actual sphere. An actual
cone would have a new top mod-two class in degree9 with beta=C
modulo earlier first-Bockstein images. All those earlier images
have fourth square zero. Hence Sq4_* beta_*=Sq5_* takes the top
class to A4. Dually Sq5 on a degree-four class would be nonzero,
contrary to instability. Ordinary mod-two Hurewicz is therefore
injective on pi8F. Stable vanishing of the nu composite is actual.

Root checked the full source nine-cell note, including its explicit
unknown subgroup<2v,w>. The shorter sufficient argument uses
the eight-skeleton quotient decomposition

    D' vee M(Z2,7) vee M(Z4,7) vee C1^8 vee S8.

Choose the correction zero on all factors except D'. Its pi8 is
Z_(2)theta plus Z4v plus Z2w. These generators all map to zero:
v goes to alphaBar nu, w to rho eta², and theta has integral
Hurewicz2H8, hence mod-two Hurewicz zero. Its image is an ACTUAL
class in F, so the injectivity just proved kills it. Therefore
the correction annihilates all pi8 of the quotient and extends
over every nine-cell, regardless of the undetermined coefficients.
Adding the canonical summand available through relative dimension9
gives G9. No dimension10, full-source or nullification conclusion
is inferred.
