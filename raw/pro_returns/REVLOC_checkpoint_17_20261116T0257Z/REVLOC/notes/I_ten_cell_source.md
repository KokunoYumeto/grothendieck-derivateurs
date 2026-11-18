# The source ten-cell correction: a conditional unit-quotient reduction

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15, 17:54 UTC.

Status: research in progress after the proved D.2.20 nine-skeleton map.
No ten-skeleton map, no extension of the canonical summand, and no
nullification-survival statement is asserted here. The parent is examining
the canonical summand separately. This note concerns only the correction.

## 1. A smaller source for a possible new correction

Keep B=K(F2,2), X=Sigma B, A=QX, and F the 3-connected double-loop
fiber used in D.2.18--D.2.20. Choose the bottom subcomplex
K4=Sigma B^(3)=M(Z/2,3) inside X, and put

    Z=X/K4=Sigma(B/B^(3)).

Thus Z is 4-connected and there is an actual map QX -> QZ induced
by the quotient. The stabilization

    Omega Sigma Z -> QZ

is 10-connected: Sigma Z is 5-connected, its stabilization is
11-connected, and one looping lowers the connectivity by one.
The same statement holds for Omega Sigma(Z^(10)) -> QZ, since
the omitted cells of Z have dimension at least eleven.

Consequently, given an actual based map h:Z^(10)->F, its James
extension to Omega Sigma(Z^(10)) can be pulled back along QX->QZ
over any finite source subcomplex of dimension at most ten.
The relevant homotopy pullback projects 10-connectedly to QX;
obstruction theory gives the lift through dimension ten. F is
a loop space, so the James extension is the standard adjoint
extension, not an assumption that h is an H-map.

This is a conditional reduction of a NEW correction construction.
It does not yet prove that such h exists with the required low
values. It also does not identify the resulting pullback map up
to homotopy with the already chosen G9 correction. Compatibility
through dimension nine requires a specified relative lift and
agreement of the lower maps, rather than mere agreement of their
mod-two homology coefficients. The possible freedom in the old
eight- and nine-cell nullhomotopies must be retained explicitly.

The unit-weight quotient has the same C,D,E lower classes used
by the existing correction. Its desired unit values are

    C -> xi a,
    D -> k=b^2+(b^2+k),
    E -> k+r=b^2+p3,

where r=b^2+k+p3 is the actual spherical class of D.2.17.
The other-weight zero choices of D.2.20 suggest compatibility,
but that suggestion has not been substituted for a relative
homotopy argument.

## 2. The four unit ten-classes and their primary operations

Write H*(B;F2)=F2[u2,v3,w5,t9,...], with

    v=Sq1 u, w=Sq2 v, t=Sq4 w.

The complete degree-nine cohomology basis of B is
u^3 v, u^2 w, v^3, t. Let M,N,O,T denote the suspended dual
classes in degree ten of Z. Retain G,H for the suspended duals
of u^2 v, u w, and I,J,L for the suspended duals of u^4,
u v^2, v w. Direct Cartan and Adem calculations give

    beta O=J+L;        beta M=beta N=beta T=0;
    Sq_*^2 N=G+H;     Sq_*^2 O=G+H;
    Sq_*^2 M=Sq_*^2 T=0;
    Sq_*^4 N=E;       Sq_*^4 O=E;
    Sq_*^4 T=D;       Sq_*^4 M=0.

For example Sq2(u^2v)=u^2w+v^3=Sq2(uw), and
Sq4(uv)=u^2w+v^3, whereas Sq4w=t. Also
Sq_*^3 O=F (F is dual to u^3), and all degree-five-square
coefficients into the bottom C vanish by instability on u^2.
This table does not give a complete attaching matrix in pi9(Z9).
In particular it does not determine secondary coefficients or
the possible first Whitehead-square component.

## 3. The new order-eight integral group

The next integral group is

    H8(B;Z)=Z/8 + Z/2,

so a degree-four boundary normalization would be incorrect here.
The fundamental u is transverse in the Bockstein spectral sequence:
its successive squares give orders 2,4,8. Thus the degree-eight
u^4 survives to a nonzero third Bockstein. In the homological
spectral sequence the corresponding degree-nine class is represented
by the dual to u^3v (equivalently u^2w after the earlier boundaries),
and its third Bockstein hits the dual to u^4.

Opened primary source: Alain Clement, *Integral Cohomology of
2-Local Hopf Spaces with at Most Two Non-Trivial Finite Homotopy
Groups*, Contemporary Mathematics (2005), Proposition 2.4 and the
table on p.5. The table is cohomological: H^9(B;Z)=Z/8+Z/2,
which gives the displayed homology group by integral UCT.

https://serval.unil.ch/resource/serval:BIB_3440F3674944.P001/REF.pdf

The primary paper was opened in full (web reference turn1158view0).
It points to the author's 2002 thesis, *Integral cohomology of finite
Postnikov towers*, for the transverse theorem's proof. The thesis
source is also maintained by its author at

https://github.com/aclemen1/integral-cohomology-of-finite-postnikov-towers

The author's original thesis TeX has now also been retrieved and
read from the two raw GitHub files chap3sect2.tex and chap2sect4.tex.
Local copies are in notes/I_sources/I_Clement2002_chap3sect2.tex
and I_Clement2002_chap2sect4.tex. Section3.2 explicitly gives

    d3(u^4)=u^2(uv+w)=u^3v+u^2w,

and Section2.4 proves the transverse implication using Cartan
divided powers and their pairing with cohomological powers.
The primary paper is saved at notes/I_sources/I_Clement2005.pdf;
its direct university bitstream URL is

https://api.unil.ch/iris/server/api/core/bitstreams/e250b742-47ff-4cc0-a778-03a0ddd52088/content

## 4. A complete zero-Hurewicz fact for the unit ninth skeleton

The following source calculation does NOT require the unknown
even-nu or w coefficients to be chosen. Write Z_i for the unit
quotient's finite skeleton, in the compatible two-local cell model.
The known eight-stage decomposition is

    Z8=D' vee M(Z/2,7)_F.

From the audited nine-source calculation,

    pi8(Z8)=Z_(2){theta} + Z/4{v} + Z/2{w,tau_F},

where theta has integral Hurewicz degree2 on H. The three unit
nine-cell attachments have exact forms

    I:       a0 v + tau_F + e0 w,       a0 odd;
    J: theta + 2a1 v + tau_F + e1 w;
    L: theta + 2a2 v         + e2 w.

Here a0,a1,a2 and e0,e1,e2 retain every previously undetected
component. No value of any e_i or even-nu coefficient is assumed.
The free cellular cycles in degree nine are I and J-L.
For a linear combination a I+b J+c L to vanish in pi8(Z8),
its theta coordinate first forces c=-b. Its tau_F coordinate
then forces a+b to be even. The v coordinate is

    a0 a + 2(a1-a2)b =0 mod4.

Reducing this modulo two forces a even, and then the tau_F
condition forces b even. Substitution gives4|a. Conversely
4|a and2|b annihilate every torsion coordinate, including w.
The stable cofiber sequence for the three attachments therefore
gives the exact integral Hurewicz lattice

    image(pi9^s Z9 -> H9(Z9;Z_(2)))
         =4 Z_(2){I} + 2 Z_(2){J-L}.

The space Z9 is4-connected, so its ordinary ninth homotopy
surjects onto stable ninth homotopy by Freudenthal. In particular
the same zero-mod-two conclusion holds for every ordinary sphere
map, even without using this surjectivity. Thus

    h_F2: pi9(Z9) -> H9(Z9;F2) is identically zero.

The mod-two UCT Tor term from H8(Z9;Z)=Z/2 causes no exception:
the Hurewicz image of an integral sphere map lies in the reduction
of integral H9 and has no component in that Tor term.

This is a proved source input. It would kill all unit ten-cell
images if the ordinary mod-two Hurewicz map of the4-connected
target cover E=F<5> is injective in degree nine. That target
injectivity is NOT assumed here and is being computed separately.

## 5. Why the target cover has no unstable degree-nine ambiguity

Every map Z9->F lifts to E=F<5>, because Z9 is4-connected and
the bottom Postnikov map has target K(Z/2,4). The cover E is a
4-connected loop space. Its single suspension-loop unit

    E -> Omega Sigma E

has a homotopy retraction, and Freudenthal makes it9-connected.
It is consequently an isomorphism on pi9. Since Sigma E is
5-connected, pi10(Sigma E) is stable. Hence

    pi9(E) -> pi9^s(E) is an isomorphism.

This argument concerns the cover E. It does NOT identify
ordinary pi9(F) with its stable counterpart or discard the
possible Browder class in F.

The exact ten-cell extension and compatibility with a fixed
previous G9 remain open. No source ten-cell has yet been declared
harmless solely from a stable calculation in F.

## 6. Relative compatibility for a specified allowed nine-map

The following refines the qualification in Section1. It proves an
exact relative construction for a coordinated choice of the earlier
correction. It does not identify every arbitrary previous G9 with
that choice.

Put C0=A/K4 (this C0 denotes a space, not the unit homology class C).
The stable Snaith splitting, with its unit weight-one summand, gives

    Sigma-infinity C0 = Sigma-infinity Z vee W,

where W is the sum of weights at least two. Use the PROJECTION in
this splitting to define an actual based map

    P:C0 -> QZ.

There is no need to assert that a separately chosen suspension-loop
counit is this projection. The restriction of P to the unit quotient
Z is its stabilization unit. Use compatible relative CW models, so
Z_i is a subcomplex of (C0)_i=Q_i. The map Z9->QZ is9-connected:
Z9->Z is9-connected and Z->QZ is9-connected. Since Q9 has dimension
nine, obstruction theory lifts P|Q9 to a map

    p9:Q9 -> Z9,

relative to the identity on Z9. This is an actual homotopy retraction
of the unit quotient through degree nine, obtained from the given
stable projection. The lift through degree eight is unique up to
relative homotopy, since its homotopy fiber is8-connected.

Choose the unit correction h8:Z8->E by the already proved D' block
construction, zero on its M(Z/2,7)_F summand. It extends to some h9
by the D.2.20 target argument. Define the coordinated correction on
Q9 to be h9 p9. Equivalently, make the previous allowable higher-
weight and ninth-cell choices according to this stable projection.
The six-dimensional values are the original Moore correction on
the unit cells and zero on the weight-two cell; the splitting's
weight-two section chooses the latter cell in the projection kernel.
This specifies a homotopy class of a permitted correction, rather
than identifying maps solely by their homology coefficients.

Now suppose h9 extends to an ACTUAL h10:Z10->E. Let

    j:Omega Sigma Z10 -> QZ

be stabilization; it is10-connected. On Q9 specify the lift
eta_1 p9, where eta_1:Z9->Omega Sigma Z10 is the James unit.
On the unit subcomplex Z10 specify eta_1 itself. These agree on
Z9, and their composites with j agree with P up to the specified
relative homotopies. The homotopy fiber of j is9-connected, so
the lift extends over all remaining relative ten-cells of Q10.
Compose this lift with the James extension of h10 to E. The result
is an actual correction Q10->E whose restriction to Q9 is homotopic,
relative to the lower unit data, to the specified h9 p9.

Thus existence of the unit extension gives a correction with exact
agreement through nine for this coordinated allowed choice. It
does not by itself preserve an unrelated choice of all earlier
nullhomotopies. The canonical summand is still a separate problem.

## 7. The first exact integral qualification in dimension ten

The zero-mod-two-Hurewicz result in Section4 must not be mistaken
for a proof that all target images vanish. The cover calculation
may contain a mod-two-invisible spherical class with integral
Hurewicz4N, where N has order eight in H9(E). The source sphere
whose integral Hurewicz is4I could detect that class: naturality
of Sq4 forces the mod-two N coefficient of h9(I) to be one.

For the ACTUAL unit ten-cell boundaries, the integral image lattice
can be normalized as

    8 Z_(2){I} + 2 Z_(2){e},
    e=J-L+2kI,

with k retained. It is not legitimate to set k=0 merely from the
abstract group H9(Z)=Z/8+Z/2. For example the raw relation
2(J-L)+4I is compatible with that same group. An even slide of
the free ninth cellular cycles produces the stated normalized e
without changing any mod-two label or the spherical lattice in
Section4. The image of e under a partial h9 may still have a
hidden2N component, even when its mod-two image lies in the
first-Bockstein order-two part. Such a component would matter
after multiplication by two.

Similarly, an exponent bound4 on pi9(E) alone does NOT kill the
eight-I attachment. A lift with source Hurewicz8I is twice a lift
with Hurewicz4I, plus a torsion element. Its image could be twice
an order-four target element. The exponent bound only says that
changing the filling of the I nine-cell alters the obstruction
by8x=0; it does not compute the baseline obstruction.

The exact unit-ten images therefore require the target's complete
component calculation and, if necessary, the source's secondary
coefficients. They have not been inferred from the primary table.

Finally, constructing extensions of the canonical and correction
summands separately is sufficient, but is not necessary, for an
extension of their sum G9. If the separate constructions fail,
one must compute the joint ordinary obstruction on a common cell
basis and allow all previously permitted choices. A failure of
either constrained summand is not a nonextension theorem for G9.
