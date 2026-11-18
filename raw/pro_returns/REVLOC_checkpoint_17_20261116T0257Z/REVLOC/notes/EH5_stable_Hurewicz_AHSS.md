# The degree-fifteen stable Hurewicz obstruction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Research note; the unresolved differentials are explicitly
retained. The counit and primary-operation observations below were independently
matched by `simple_higher`. The compatible Toda representative used in Section 5
was independently checked by all three other agents and is being recorded in
D.2.53. This note does not assert stable sphericity or the vanishing of h.

Put L=Y<7>, E=Omega^2 L. The space L is six-connected and E is four-connected.
All calculations in this note are two-local. The reduced homological AHSS is

    E2_(p,q)=H_p(L;pi_q S) ==> pi^s_(p+q)L,
    d_r:E_r(p,q) -> E_r(p-r,q+r-1).

The d1 differential is the ordinary cellular boundary and is already taken in
passing to E2. There are no local-coefficient complications because L is simply
connected. In the bottom coefficient row there are no incoming differentials.

## 1. Integral suspension preserves the order-eight class

The actual counit factors as

    Sigma^2 E -> Sigma Omega L -> L.

Its first arrow is twelve-connected and its second arrow is thirteen-connected,
by the join-fiber proof in `I_counit_twelve_cells.md`. Thus

    sigma^2:H9(E;Z) -> H11(L;Z)

is an integral isomorphism. In the established D.2.22 normalization,

    H9(E;Z)=Z8{N'} + (Z2)^3,
    h_Z(p)=4N',  h_Z(s)=0.

Consequently the unique L-lift of p has integral Hurewicz image
4 sigma^2 N', nonzero of order two. Its coefficient reduction in
H11(L;Z8) is still nonzero: the canonical tensor summand
H11(L;Z) tensor Z8 injects by the homology universal coefficient sequence.
No identification with a suspended decomposable is legitimate here.

## 2. One extra degree of cohomology-suspension injectivity

Let u5 be the bottom mod-two class of E and a7 its double suspension dual in L.
The degree-ten product u5^2 is nonzero by the full D.2.22 table.

In the reduced bar construction for BE=Omega L, a tensor of length two first
has total degree twelve. The unique possible new class in that degree is
[u5|u5], whose bar d1 is u5^2 and hence is nonzero. Length three begins in
degree eighteen. It follows that

    sigma:H11(E;F2) -> H12(Omega L;F2)

is surjective. In the next bar construction the least homology degree is six;
length-two terms therefore start in total degree fourteen. Hence
H12(Omega L;F2)->H13(L;F2) is also surjective. Dually, the actual double
cohomology suspension is injective in degree thirteen.

The bottom class a7 is the reduction of the mod-four fundamental class, so
Sq1(a7)=0. The operation Sq6(a7) pulls back to Sq6(u5*)=0 by instability,
and the preceding injectivity proves

    Sq6(a7)=0.

The exact degree-nine E operation table has Sq4_* N=u5 and zero fourth square
on every other basis class. Thus the degree-eleven dual of the order-eight
summand is

    n11=Sq4(a7),  and Sq2(n11)=Sq6(a7)+Sq5 Sq1(a7)=0.

This is an actual operation identity in L, not merely an identity after
cohomology suspension. It does not evaluate a secondary operation on n11.

## 3. The old d4 target, with all incoming sources retained

Before the compatible Toda representative is improved in D.2.53, D.2.52 gives
a geometric detecting cycle whose potential d4 is represented by
n red8 h_Z(Et). The containment Et in <p,s> makes that representative either
zero or n times 4 sigma^2 N'. Its correct target is E4_(11,3), not raw
H11(L;Z8).

Since pi4 S=pi5 S=0, this target has no outgoing d2 or d3. Its full quotient is

    E4_(11,3) = H11(L;Z8) / (im d2_(13,2) + im d3_(14,1)),

where the second image is interpreted on E3 and then lifted to the first
quotient. More explicitly,

    E3_(14,1) = ker(Sq2_*:H14(L;F2)->H12(L;F2))
                 / im(Sq2_* red2:H16(L;Z)->H14(L;F2)).

There is no omitted d1, and no other incoming differential before E4.

The row-one d2 is Sq2_*. One direct justification is that it is a stable
degree-two mod-two operation, whose space of possibilities has the single
nonzero generator Sq2; the cone of eta makes it nonzero because eta^2 is
nonzero. Multiplication by eta is an isomorphism from coefficient row one to
row two, and takes eta^2 to eta^3=4nu in row three. Naturality therefore gives

    d2_(p,2) = i4 Sq2_*:H_p(L;F2)->H_(p-2)(L;Z8),
    i4:F2->Z8,  i4(1)=4.

The n11 coordinate has a mod-eight lift: its integral cellular block is the
order-eight N' block, with zero first and second Bocksteins. Choose that lift
lambda_N in H11(L;Z8), evaluating as one on N' and as zero on the other
integral and Tor coordinates. Then

    <lambda_N,i4 Sq2_* x> = 4<n11,Sq2_*x>
                          = 4<Sq2 n11,x> = 0,

whereas <lambda_N,4N'>=4. Thus the specified nonzero 4N' is not in the image
of incoming d2. The incoming secondary d3 is NOT evaluated by this argument.

After D.2.53, this unresolved d3 is no longer needed for the chosen detecting
witness: one can choose Et=0 and use the smaller source in Section 5.

## 4. All possible outgoing edge differentials

For a degree-fifteen integral class the only possible nonzero edge
differentials, before exploiting its particular geometric source, are

    d2: (15,0)->(13,1), coefficient eta;
    d3: (15,0)->(12,2), coefficient eta^2;
    d4: (15,0)->(11,3), coefficient nu in Z8;
    d7: (15,0)->(8,6),  coefficient nu^2;
    d8: (15,0)->(7,7),  coefficient sigma in Z16.

The fifth and sixth stable stems vanish; r>=9 lands below the connectivity of
L. Higher differentials in this list are not identified with primary squares.

## 5. The new chosen witness survives through d7

D.2.53 supplies the actual relation e=u4 Eepsilon'=0, with a compatible
representative Et=0 in D.2.49. D.2.46 therefore supplies an integer n with

    mu delta = n alpha sigma' in pi14 L,
    delta=partial(2c4):S14->M(Z4,7).

Form the actual finite complex

    P=(M(Z4,7) vee S7) union_(i_M delta - n i_7 sigma') e15.

The maps mu and alpha extend to P->L. The same actual cone map and Stiefel
cup comparison as D.2.52 show that the image omega of its top integral cycle
has theta-pairing one. The M(Z4,7) component delta is stably zero by its exact
metastable quadratic boundary definition. Since E^infty sigma'=2sigma up to
an odd orientation unit, there is a filtered stable equivalence, identical on
the old skeleton,

    Sigma^infty P  ~=  Sigma^infty M(Z4,7) vee C(2n sigma:S14->S7).

Thus the top class of P survives every differential before d8; its only
possible edge differential is 2n sigma on the added seven-sphere. Naturality
proves the exact statement

    omega belongs to E8_(15,0)(L),
    d8(omega) = the class of 2n alpha in E8_(7,7)(L).

Here alpha also denotes the bottom generator of H7(L;Z)=Z4, and
H7(L;Z16)=Z4. The displayed raw coefficient has order at most two. It is not
asserted nonzero in the actual E8 target.

This is stronger than primary-operation annihilation: no d2, d3, d4 or d7 can
remove this chosen detecting class. There are no later outgoing differentials
after d8, so omega is stably spherical if and only if this actual E8 class is
zero. This assertion uses the convergent connective AHSS edge map; it does not
select a value of n or of h.

## 6. The exact remaining d8 target and changing the witness

There are no outgoing differentials from (7,7) in this range. Starting with

    E2_(7,7)=H7(L;Z16)=Z4,

the only possible incoming sources before page eight are

    d2: E2_(9,6)=H9(L;F2),
    d5: E5_(12,3),
    d6: E6_(13,2),
    d7: E7_(14,1).

The d3 and d4 sources are zero because pi5 S=pi4 S=0. Every source in this
list must be taken on its specified page, including its earlier incoming and
outgoing differentials. In particular the target is an iterated quotient of
Z4, not an unqualified raw coefficient group. The value of this quotient and
of the remaining differential are not yet computed here.

The first listed differential is in fact zero. Use the unit from the sphere
to the connective image-of-J spectrum j. The opened Bruner--Rognes
Theorem1.2 and Remark1.3 give pi6(j)=0 and an isomorphism
pi7(S)->pi7(j)=Z16 (the four surviving h0-powers on the image of h3).
Naturality of AHSS therefore maps the source H9(L;pi6 S) to zero and maps
the target H7(L;pi7 S) isomorphically to H7(L;pi7 j). The commuting d2
square forces d2_(9,6)=0. No classification of coefficient operations or
surjectivity of integral reduction on H9(L;F2) is assumed.

Consequently the exact remaining quotient before d8 is obtained only from

    d5:E5_(12,3)->Z4,
    d6:E6_(13,2)->the quotient by im d5,
    d7:E7_(14,1)->the quotient by im d5 and im d6.

The image-of-J comparison has not evaluated these three maps. In particular
the presence of an isomorphism on the final coefficient group does not by
itself identify their sources or their images on later pages.

The existence question is not decided merely by a single chosen witness.
Since the bottom-row pages are subgroups of integral homology, write

    H=E8_(15,0)(L),  H0=ker(theta:H->F2).

The constructed omega has theta(omega)=1, so all detecting classes on this
page are omega+H0. With no differentials after d8, the exact existential test
is

    theta detects some stable Hurewicz class
       iff d8(omega) belongs to d8(H0).

This retains the possibility of changing the detecting integral cycle. A
nonzero d8 of one witness alone would not prove h nonzero.

## 7. Opened primary anchors and current scope

* Adams, *Stable Homotopy and Generalised Homology*, Part III Section 7:
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Adams-SHGH-latex2.pdf
  Opened the revised transcription, printed pp257--261: exact couple, dr
  bidegree, E1 cellular boundary, E2 homology and natural convergence. This is
  not represented as a newly opened scan of the 1974 edition.
* Oka1986, Section2 (2.1), printed p149, reopened publisher PDF:
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9BF563A8A92B6BF87DAA39E8DAD092BE/S0013091500017557a.pdf/homotopy-of-the-exceptional-lie-group-g2.pdf
  It explicitly gives eta^2 nonzero and eta^3=12nu integrally, hence 4nu after
  an odd two-local generator change. Existing bibliography key I_Oka1986.
* Strickland's author program https://strickland1.org/toda/Toda.m, reopened:
  the sixth-stem block gives pi9(S3)_(2)=0, attributed to Toda Proposition5.11
  p46; the seventh-stem block gives pi10(S3)_(2)=pi11(S4)_(2)=0, attributed to
  Toda Proposition5.15 p50. These are the exact D.2.53 indeterminacy inputs.
  Original Toda pages were not newly opened.
* Bruner--Rognes, arXiv2105.02601v3, opened pp2--3 and Theorem1.2/Remark1.3:
  https://arxiv.org/pdf/2105.02601 . The connective image-of-J spectrum is
  the fiber of ko -> Sigma^4 ksp lifting psi^3-1. The unit is an isomorphism
  on pi7 and pi6(j)=0. Section 6 uses precisely those two facts to eliminate
  the first possible incoming d2 at (7,7), by naturality. No later j-homology
  calculation is asserted.

The manuscript's D.2.4 remains open. The selected d4 obstruction has been
removed by the actual Toda theorem, not by an unproved AHSS collapse. The
remaining work is the d8 quotient and the image on H0 above.
