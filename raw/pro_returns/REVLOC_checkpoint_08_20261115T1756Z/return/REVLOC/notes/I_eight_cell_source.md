# The exact source eight-cell matrix

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15.

Status update, 17:25 UTC: the full source calculation has passed root
and axioms-agent independent review and is integrated with the target
calculation in D.2.19. The two target composites are individually zero,
so the chosen map extends over the eight-skeleton. The note retains
the reduction below to make every interface reviewable. No full-source
extension is asserted; the live nine-cell problem is recorded in
notes/I_nine_cell_source.md.

## 1. The seven-dimensional quotient and its entire pi7

Let K_i be the chosen finite skeleta of A=Q Sigma K(F2,2), with
K4=M(Z2,3), and put Q_i=K_i/K4. The seven-stage result gives

    Q7 = D vee M(Z2,6)_z vee S7_F vee S7_J,
    D = cofib( [[4,eta5],[0,2]] : S5 vee S6 -> S5 vee S6 ).

Here D contains the bottom c5, the degree-four Moore top d6=D,
the free six-cell e6=D+E, and the seven-cell x attached by
i eta5+2e. The second Moore factor has bottom z=A0². The two
free seven-spheres are F=Sigma f and J=A0B0+Q^4A0 modulo two.
Extra auxiliary cells may be retained and cancelled in pairs;
they do not introduce an undetected attachment component.

There is a completely detected group

    pi7(Q7) = Z{F,J} + (Z2){tau_d,tau_e,tau_z}.

To prove this without assuming a Moore-group extension, collapse
the bottom five-sphere of D. The quotient is

    D/S5 = S6_d vee M(Z2,6)_e.

The map pi7(S5)->pi7(D) is zero: its eta² generator is
(i eta5+2e) eta6, since 2 eta6=0. Thus the quotient injects
pi7(D) into pi7(S6 vee M(Z2,6))=(Z2)^2. Its connecting map to
pi6(S5) is zero on both generators. On the S6_d summand the
connecting map is degree four, which kills eta. On the Moore
factor the connecting map is eta6 composed with the top pinch;
the generator i eta6 lies on the bottom and its pinch is zero.
Hence that injection is an isomorphism.

Choose any coextension

    zeta:S7 -> M(Z4,5),  pinch zeta = eta6.

It exists by the Moore cofiber sequence. Its image in D is the
unique class tau_d mapping to the eta generator on S6_d. The
choice ambiguity is i eta², already zero in D. Set tau_e=e eta6,
and tau_z=z eta6. The three classes are detected exactly by Sq²
from the three degree-six cohomology classes d^vee,e^vee,z^vee.
The free components are the integral degrees on F,J. All spaces
here are four-connected and the relevant dimension is seven,
so the stable calculation is also the actual unstable one.
There is no Whitehead component in this range.

## 2. The complete mod-two degree-eight list

Write g,h for the B-labels dual to u²v,uw. The entire ordinary
degree-eight homology of A has basis

    G8=Sigma g, H8=Sigma h, A0 C, B0², Q^5 A0.

No nonprimitive product is omitted: A0C is the degree3+5
product, B0² is the degree4+4 product, and Q^5A0 is the new
arity-two class. All arities at least three begin in degree9.
The first Bocksteins are

    beta G8=F,  beta H8=beta(A0 C)=beta(B0²)=beta Q^5A0=0.

The complete Sq_*² table into H6(A) is

    G8 -> E=d+e,
    H8 -> E=d+e,
    A0 C -> z,
    B0² -> z,
    Q^5 A0 -> z.

For the unit entries, Sq²w=0 and Sq²(uv)=u²v+uw. Cartan gives
Sq_*²(A0C)=A0 Sq_*²C=A0² and
Sq_*²(B0²)=(beta B0)²=A0². The stable Nishida relation gives

    Sq_*² Q^5 A0 = binom(3,2) Q^3 A0 = A0²,

since beta A0=0. These are the exact CLM conventions already
opened for the preceding source computations.

## 3. The integral weight-two chain and the order-four seven-cycle

The integral weight-one group in degree7 is H6(B;Z)=Z2.
Indeed its mod-two rank after subtracting the Tor contribution
of H5(B;Z)=Z2 is one, and beta g=f is nonzero, forcing
exponent two. It is represented by F=Sigma f.

For the weight-two group, take the bottom Moore chain of X:

    a in degree3, b in degree4, db=2a.

Use the free E(Sigma2) cellular generators e_i with
de1=(tau−1)e0 and de2=(1+tau)e1. Permuting labels has the
Koszul sign: tau(aa)=−aa and tau(ab)=ba. Define

    x=e0(aa),
    r1=e1(aa),  t=e0(ab),  t'=e0(ba),
    h=e1(ab),  q=e0(bb).

The degree-six generator is x. In degree seven,

    dr1=−2x,  dt=−2x,  dt'=2x.

Thus w=t−r1 and w'=t'+r1 freely generate the cycles. In
degree eight,

    dh=t'−t+2r1=w'−w,
    dq=2(t+t')=2(w+w'),
    d(e2(aa))=0.

The other mixed e1(ba) has the opposite boundary. All cells
using a higher label in degree eight are cycles and do not
alter H7. Hence the weight-two H7 is

    Z{w,w'} / (w'−w, 2(w+w')) = Z/4{w}.

The mod-two reduction of w is exactly

    J=A0B0+Q^4A0.

Moreover

    d(q−2h)=4w.

The reduction of q is B0². This corrected integral representative
therefore proves the exact second Bockstein

    beta2[B0²]=[J] != 0.

The correction by 2h is essential: dq itself is not divisible
by four. Both A0C and Q^5A0 have integral cycle representatives,
so their second Bocksteins vanish. The unit class H8 has zero
second-Bockstein component on J by the configuration-weight
splitting. Consequently

    H7(A;Z) = Z2{F} + Z4{J}.

This uses the Snaith splitting only for the direct-sum and
weight separation. The actual exponent and beta2 coefficient
are given by the explicit chain calculation above.

## 4. Integral normalization and all eight-cell attachments

After cancelling unit pairs, the degree-seven cycles of Q7
are generated by the free spheres F,J. The determined integral
homology makes the image of the degree-eight boundary the
index-eight sublattice generated by 2F and4J. The first and
second Bocksteins specify its filtered mod-two normal form:
G8 is the degree-two relation and B0² is the degree-four
relation. One can choose integral lifts preserving all mod-two
labels so their boundaries are exactly 2F and4J, while H8,
A0C,Q^5A0 have zero integral degree boundary.

Here is the normalization point that must not be silently
replaced by an arbitrary Smith basis. A term 4mJ in the
boundary of G8 is removed by replacing the free generator F
by F+2mJ, which has the same mod-two class. Terms 4mF in the
boundary of B0² are removed by even multiples of G8. A
zero-first-Bockstein cell has an even F coefficient, and
zero second Bockstein on J makes its remaining J coefficient
an even multiple of the degree-four relation. Thus even
cell combinations eliminate those remaining boundaries
without changing any mod-two Sq² coefficient. Odd rescalings
are harmless in the two-local calculation. This gives the
claimed normal form with the displayed operation table intact.

Since the integral degrees and the three Sq² coefficients
detect every element of pi7(Q7), the complete eight-cell
attaching table is, with compatible orientation choices,

    G8       : 2F + tau_d + tau_e,
    H8       : tau_d + tau_e,
    B0²      : 4J + tau_z,
    A0 C     : tau_z,
    Q^5 A0   : tau_z.

Any extra zero-mod-two cellular pairs have already been
cancelled. If instead they are retained, their incidences
are invertible two-locally and impose no additional condition
on maps to the two-local target T.

## 5. The single new target equality for the chosen correction

The correction used in D.2.18 has bottom alphaBar on the
degree-four Moore bottom, Moore extension mu whose top image
is k, value rho on the free six-sphere e, and zero on z.
It may be chosen zero on the free seven-spheres F,J. Therefore

    tau_d |-> mu zeta,
    tau_e |-> rho eta6,
    tau_z |-> 0.

The generator tau_d can be represented inside M(Z4,5), and
tau_e inside S6_e, so these values do not depend on the
chosen nullhomotopy filling the seven-cell i eta5+2e.
Every eight-cell condition is consequently satisfied if
and only if

    mu zeta + rho eta6 = 0 in pi7(T).

This is the explicit source-side condition sent to the target
agent. Changing zeta by i eta² does not change mu zeta:
alphaBar eta²=2rho eta6=0, using D.2.18 and2eta6=0.
No conclusion about dimensions nine and higher follows from
the eight-cell matrix.

To turn an extended correction into an actual map on A8, the
canonical summand must also be extended: g2 is originally
defined only on C2X. This extension is available through source
relative dimension nine, by the precise D.2.13 construction.
Let X'=X/S3, which is three-connected, and choose
hbar:Sigma²X'->Y extending h0 through the quotient. The map
C2X'->QX' is nine-connected. Its homotopy pullback along
QX->QX' is therefore nine-connected over QX, receives the
canonical lift of C2X, and maps to T by Omega²hbar. The lift
extends over relative cells through dimension nine. Adding an
extended correction on Q8 to this canonical extension gives
an actual map on A8, with the D.2.17 coefficients unchanged.
This uses the unsuspended pullback directly and does not
assume that suspension preserves a homotopy fiber sequence.

## 6. Opened primary inputs

The homology labels, ordinary products and Nishida operations
use Serre1953 Section2 nos8--9 and CLM1976 ChapterIII
Theorems1.2--1.4 and3.1--3.2. The cellular E(Sigma2)
conventions are those of the proof of CLM III Lemma3.10,
printed p232; the odd-degree mixed-label calculation is
written out above. The configuration-weight splitting is
Snaith1974 Theorem1.1 and Section2. The only stable stems
needed for the complete source attachment detectors are
eta, eta² and2eta=0, also recorded in opened Oka1986
Section2 equation(2.1), p149.
