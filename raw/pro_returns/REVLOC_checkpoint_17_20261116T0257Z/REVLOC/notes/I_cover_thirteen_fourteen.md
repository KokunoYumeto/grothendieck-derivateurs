# Actual cover homology in degrees thirteen and fourteen

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Candidate complete proof; submitted for independent audit.
This computes ordinary mod-two groups and suspension quotients. It does not
identify any higher stable AHSS differential or an unstable attaching map.

Use B=K(F2,2), T=Omega²Sigma²B, F=fib(T->B), and
E=F<5>=Omega²L, L=Y<7>. The previously audited cover note establishes
the edge quotient through degree ten. The extension below supplies the
new range without assuming a collapse from base injectivity alone.

## 1. Bounded Hopf-freeness lemma

Let A=H*K(F2,4), C=H*F, and A'=im(p*:A->C). The fundamental
Postnikov map p:F->K(F2,4) is a loop map (indeed the double loop of
the degree-six Postnikov map of the five-connected cover of Y).
Thus A' is a connected Hopf subalgebra of C. The cup multiplication
in C is commutative. Milnor--Moore Proposition 4.9 therefore gives
a graded free A'-module decomposition of C.

Suppose ker(p*) has no element in degrees at most 13. A minimal
graded A-free resolution of A' has its first positive generators
in internal degree at least 14. Every subsequent differential has
entries in the positive-degree ideal of A, whose least degree is
four. Thus

    Tor_s^A(A',F2)_t = 0 for s>0 and t<14+4(s-1).

Consequently positive Tor has total degree t-s at least
13+3(s-1). Since C is a direct sum of nonnegative shifts of A',
the same lower bound applies to Tor_s^A(C,F2). This also follows
from change of rings and the A'-flatness of C. The Eilenberg--Moore
sequence therefore has no positive filtration in total degrees at
most twelve, nor a differential entering that range. Its edge map gives

    H^{<=12}E = (C / p*(A^{>0}) C)^{<=12}.                 (1)

In particular H_iE->H_iF is injective through twelve, compatibly
with all operations whose input and output lie in this range.
This lemma does not require p* to be globally injective.

**Opened primary source.** Milnor and Moore, *On the Structure of Hopf
Algebras*, Ann. Math. 81 (1965), 211--264, Proposition 4.9 and the
following paragraph, printed pp229--230. The preceding Theorem 4.4
contains the freeness proof. Opened/read original primary PDF:
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Milnor-Moore.pdf .
Normality is automatic here because C has commutative multiplication;
all vector-space splitting hypotheses hold over F2.

## 2. Exact new injectivity tests

The existing note `FGH_D2_four_connected_cover.md` proves injectivity
through degree eleven. Since p* is a Hopf map, any element of least
degree in its kernel would be primitive. All Serre polynomial
generators of A are primitive, and its other primitives are their
iterated squares. The only new primitive directions in degrees
twelve and thirteen are

    degree12: (Sq²x4)²,  Sq5 Sq2 Sq1 x4;
    degree13: Sq6 Sq3 x4, Sq6 Sq2 Sq1 x4.                 (2)

Let u2,v3,w5,t9 denote the polynomial Serre cohomology generators
of B. Write [m] for the corresponding homology label in T. The
formal series F=sum_m [m] m is group-like, so every coefficient of
F^{-1} t (partial F/partial t), or its w analogue, is primitive.
This supplies the following Newton polynomials without a choice of
a retraction T->F:

    Z11 = [ut]+[u][t];
    Z12 = [vt]+[v][t];
    Z13a = coefficient of u^4 w in F^{-1}w(partial F/partial w);
    Z13b = coefficient of u²t in F^{-1}t(partial F/partial t).

They are primitive in H*T. The homology of B has no primitive in
degrees 11,12,13, so all four lie in the fiber factor H*F. The
primitive splitting of H*(B x F) justifies this last assertion;
one is not identifying the entire kernel of T->B with the fiber.

Cartan and Serre's operations give the exact values

    beta Z12=Z11,   Sq6_* Z13a=P7,   Sq6_* Z13b=Q7,       (3)

where P7,Q7 are the previously fixed primitive polynomial classes.
For clarity, the linear-label coefficients in the latter two tests
come from

    Sq6(u²v)=u^4w,       Sq6(uw)=v w²+u²t.

The remaining terms are fixed by primitivity; polynomial primitive
degree-seven homology has basis P7,Q7. Equivalently the complete
polynomials and operation calculations are verified in the finite
certificate below. The existing degree-eleven test has
<p*Sq4 Sq2 Sq1 x4,Z11>=1. Thus Z12 detects the second direction
of degree twelve. It has zero pairing with every positive cup product.

For the first direction in degree twelve take [v²]². Its reduced
coproduct is [v]² tensor [v]². Both [v]² and [v²]² have zero image
under q:T->B, by the divided-power multiplication in H*B. Thus its
FULL right coaction (id tensor q*)Delta is exactly [v²]² tensor1.
Under the actual coalgebra splitting H*T=H*B tensor H*F, the
coinvariants of this right H*B coaction are precisely 1 tensor H*F:
applying the B-counit on the first tensor factor to the coinvariant
identity eliminates every positive B-coordinate. This proves fiber
inclusion, rather than inferring it from q*=0 alone. The class
evaluates to one on (p*Sq²x4)², because
Sq²_*([v]²)=a². The two degree-twelve tests are independent.

In degree thirteen, (p*Sq3 x4,p*Sq2 Sq1 x4) evaluate on (P7,Q7)
as (1,0) and (1,1), respectively. Equation (3) therefore gives
an invertible two-by-two matrix for (2). No least-degree kernel
element can occur through thirteen. This proves the hypothesis
of Section 1 and hence (1).

## 3. Dimensions and the relevant low products

The CLM free restricted-Lie description gives the Hilbert series
of H*T. Divide it by H*B using the actual space splitting B x F,
and then by H*K4 through degree twelve using (1). The resulting
dimensions are

| degree | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H_i(E;F2) | 1 | 2 | 2 | 5 | 8 | 12 | 20 | 32 |

The last two dimensions of F are 30 and 49. An exact independent
integer-series certificate is `code/I_cover_extension.py` with
output `code/outputs/I_cover_extension.json`. It also checks all
four Newton coproducts and the three new operation identities.
Its formal quotient coefficient in degree thirteen is NOT claimed
to equal H13E; the proved edge range ends at twelve.

Use the existing cover classes

    u=u5=xi a, D=D6={a,b}, E6=b²+p3,
    S=S7=xi b+P7+Q7, R=R7={a,c}.

The products uD,uE6 in degree eleven are independent. The five
products uS,uR,D²,DE6,E6² in degree twelve are independent.
This can be checked in the polynomial free-E2 homology of T:
u,D,R are distinct free generators, S has the distinct xi b term,
and E6 has a distinct linear label f term. These triangular
expressions generate a polynomial subalgebra. Also xi u in degree
eleven is a distinct polynomial generator, independent of uD,uE6.

## 4. Two actual bar constructions

The first bar construction has BE=Omega L. Its E1 complex is the
algebraic bar construction on the actual Pontryagin homology of E.
The second is B(Omega L)=L. The field-coefficient bar filtration
and its actual homology-suspension edge are the ones opened in
Madsen--Milgram, Chapter1 Theorem1.5 and footnote, printed p7:
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/madmil.pdf .

At total degree twelve in BE, the only length-two term is u|u.
Its d1 is nonzero u². There is no length at least three below
degree eighteen. The length-one group H11E is quotiented by the
two products uD,uE6 from the length-two terms in total degree
thirteen. Therefore

    H12(Omega L) = H11E / <uD,uE6>,                     (4)

of dimension eighteen. All its classes are actual suspensions.
In the next bar construction, the sole length-two term in total
degree fourteen is sigma u | sigma u. Its d1 is (sigma u)².
CLM's exact top-operation suspension formula identifies this
nonzero class with sigma(xi u). Thus

    H13L = H11E / <uD,uE6,xi u>,   dim=17.               (5)

No other bar filtration or incoming differential occurs in this
range, by the same degree bounds.

For total degree thirteen in BE, the length-one quotient is

    H12E / <uS,uR,D²,DE6,E6²>,                         (6)

of dimension twenty-seven. There are additionally the two
length-two cycles u|D+D|u and u|E6+E6|u. They survive this first
bar sequence: their outgoing differential is already zero and
there is no length-three incoming term in this range. Their
leading terms are exactly the products
(sigma u)(sigma D) and (sigma u)(sigma E6) in Omega L, by the
shuffle formula on the bar filtration. Crucially, Omega L is only
an E1 space: the two reversed products must also be retained.
Their differences from the indicated products are the actual
commutators

    sigma{u,D},  sigma{u,E6},

by the CLM formula relating homology suspension and Browder
operations. These have filtration one and are independent there.
Indeed {u,D}={xi a,{a,b}} has the nonzero ordinary free-Lie
indecomposable [a,[a,[a,b]]]. The indecomposable part of {u,E6}
has the distinct word [a,[a,f]], where f is the degree-six linear
label. Their distinct arities/linear labels show independence,
and neither is in the five-dimensional product subspace (6).
Thus the FOUR products in Omega L have rank four: two independent
shuffle-leading terms and two independent lower commutators.
They are all killed by the second bar differential. The only
other length-two term relevant to total degree fourteen in the
second bar construction is sigma u | sigma u, already killed
as above. Consequently double homology suspension is onto and

    H14L = H12E / <uS,uR,D²,DE6,E6²,{u,D},{u,E6}>,
    dim H14L = 25.                                      (7)

Equations (5),(7) are canonical suspension-quotient descriptions:
the displayed products and xi u are killed by actual homology
suspension, and the dimension calculation proves the indicated
kernels are complete. Steenrod and first-Bockstein operations on
these quotients are inherited from the actual E2 homology of E.
This does not replace a calculation of higher Bocksteins, nor does
it identify a secondary stable differential with a primary square.

## 5. Exact scope for the d8 target problem

The raw mod-two homology spaces supplying the potential incoming
d6 and d7 to E8_(7,7) now have dimensions 17 and 25, with (5),(7)
giving explicit quotients in the already concrete T homology.
Their actual page-six/page-seven subquotients still require the
earlier sphere-AHSS differentials. No assertion about those
subquotients, their higher operations, or theta-zero source-changing
cycles is made by this note.

**Audit correction, 01:43 UTC.** The axioms agent caught that the
first version retained only the two shuffle-leading products of
Omega L. Its multiplication is not assumed commutative. Including
both reversed products supplies the two Browder directions in (7)
and changes the proposed H14 dimension from 27 to 25. The earlier
number is superseded; no manuscript claim used it. The root also
requested the explicit coaction argument for [v²]² above.
