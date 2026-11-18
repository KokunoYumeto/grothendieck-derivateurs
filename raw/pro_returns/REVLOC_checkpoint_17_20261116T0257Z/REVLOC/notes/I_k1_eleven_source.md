# The once-suspended eleven-cell test: a Moore coextension and the p coset

GPT-6 Astra, 2026-11-15; updated 20:18 UTC.

**Current status.** D.2.31 has determined the D.2.22 common extension
bit to be zero. Consequently Section 6 proves the nonextension
asserted in D.2.32 for its precisely specified coordinated map on
R9, for every choice of ten-cell fillings. Root and axioms have
independently passed the full mathematics and final TeX. The earlier
conditional discussion is retained below as calculation history;
its common bit is no longer unresolved. This does not classify other
lower maps that are zero on K6 (notably a different J-Moore-top
choice), or maps nonzero on K6. It does not assert a full-source
nonextension or first-cone survival. Section 7 isolates the actual
source quotient controlling the other J-top choice; its target Toda
value remains under investigation.

The notation A=Q Sigma B, B=K(F2,2), W=Omega Z and F=Omega W
is as in D.2.28--D.2.30. The discussion concerns the particular
D.2.30 branch which is zero on the six-skeleton. Arbitrary maps
can have a nonzero image of C5 in pi5W and are not reduced to this
branch by anything proved below.

## 1. The actual stable range for this finite problem

Put R_i=K_i/K_6. The chosen D.2.30 map is exactly zero on K6,
so factors through R10. The source is six-connected. Since its
degree-five cohomology vanishes, it lifts to the five-connected
cover W' of W. Write E=Omega W'; this is exactly the
four-connected target cover used in D.2.22.

The evaluation Sigma E->W' is eleven-connected: its homotopy
fiber is the join E*E, which is ten-connected. Hence its lifting
property covers source relative dimensions through eleven.
Also Sigma E is five-connected, so pi10(Sigma E) is stable.
All attaching maps of the six-connected R11 are in the stable
range. Thus this is an actual finite stable mapping problem;
relative choices through dimension ten can be carried along.

There is a further available lift to the six-connected cover
V=fib(W'->K(Z/4,6)), since H6(R;Z/4)=0. This observation does
not by itself compute the low cells of V, and no property of
their Hurewicz map is inferred from it.

## 2. The complete relevant nine-stage source splitting

Collapse K6 in the already audited D.2.19--D.2.20 source tables.
The eight-skeleton is a wedge of

    M(Z/2,7)_F, M(Z/4,7)_J, S7_X, S7_R,
    S8_H, S8_P, S8_N,

where R=Q4A0, J=A0B0+R, P=A0C5 and N=Q5A0. The top cell
of M(Z/4,7)_J is B0^2-P. All lower torsion components denoted
v,w in the former Q8 table disappear on collapsing K6.
The full nine-cell attaching table is therefore

    I9: eta F,                 J9: 2H+eta F,
    L9: 2H,                    AD: eta J+eta R,
    AE: 0,                     BC: 2P+eta J+eta R,
    Q6A0: 2N,                  Q5B0: eta R,
    A0^3: 0.                                           (1)

There is no remaining undetected component: in this range the
only components are the free degrees on the eight-spheres and
the eta classes on the seven-dimensional bottom cells. These
are exactly the integral boundary and Sq2 detectors. In
particular the old even-nu ambiguity lived below K6 and cannot
survive this quotient.

Cell slides give the stable, and hence ordinary, wedge factors

    Jblock = M(Z/4,7)_J union_(i eta) e9_U,
                  U=AD-Q5B0;
    Pblock = M(Z/2,8)_P, top cell BC-AD;
    Rblock = S7_R union_eta e9_(Q5B0);
    Fblock = M(Z/2,7)_F union_(i eta) e9_I;
    M(Z/2,8)_H, M(Z/2,8)_N, S7_X,
    S9_(J9-I9-L9), S9_AE, S9_(A0^3).                   (2)

For one coordinated nine-map, set every factor other than
Jblock and Pblock to zero. On Jblock use the Moore extension
of rho and the standard nullhomotopy of rho eta supplied by
the target c-eight-cell of D.2.22. On Pblock use the actual
target R-Moore block. This has exactly the D.2.30 eight-stage
values: P maps to lambda, N to zero, and the J-Moore top has
zero mod-two Hurewicz. No unrelated choice of all ninth-cell
fillings is silently identified with this coordinated one.

Choose integral unit chains with

    dB0=2A0,  dD6=4C5,  dE6=-4C5,
    dX7=2(D6+E6).

These are the elementary chain summands already used in the
source Bockstein calculations. Pontryagin multiplication gives
the exact cycle and boundary

    K10=A0X7+B0D6+B0E6,       dK10=0,
    d(B0X7)=2K10.                                     (3)

For example d(A0X7)=-2AD-2AE, d(B0D6)=2AD+4BC,
and d(B0E6)=2AE-4BC. A cellular chain comparison carries
these identities to the finite model. Since the displayed
mod-two class is nonzero, a parity-preserving two-local cell
basis can retain K10 as a primitive cycle coordinate and the
degree-eleven relation with boundary 2K10. This does not say
that K10 is a spherical class before its own cell is attached.

In these raw product-chain formulas, AD is not itself an integral
cycle: d(AD)=-4P and d(BC)=2P. The normalized nine-cycle labels
used in (1)--(2) are AD'=AD+2BC and AE'=AE-2BC. Thus
d(BD)=2AD', d(BE)=2AE', and d(AX)=-2(AD'+AE'). They have
the same mod-two labels, and the exact K10/BX identities are
unchanged. This explicitly separates the integral cell slides
from the original Pontryagin product chains.

Its primary operation is

    Sq2_* K10=P+B0^2.                                 (4)

In (2), this vector is exactly the top class of M(Z/4,7)_J;
the two P components cancel. Its integral ninth-cell degrees
are zero, because K10 is an integral cycle.

The cofiber sequence for Jblock=C_4^9 gives

    pi9(Jblock)=Z_(2){gamma} + Z/2{delta},

where gamma has top degree two on U and delta is the image
of the Moore eta-coextension S9->M(Z/4,7). The latter is
detected by Sq2 from the Moore top into its attaching cone.
The former's integral degree is detected independently.
Thus the attaching map of the K10 coordinate projects to
exactly delta, not gamma+delta. Its projection to Pblock
is zero, since pi9(Pblock) is generated by the bottom eta
and the P coefficient in (4) is zero. All other source
factors in (2) have been assigned the zero map. This is
the full component check for the chosen lower map.

## 3. Exact image of the Moore eta-coextension

Desuspend the target once, so the notation agrees with
D.2.22. Its lower block is

    D0=cofib([[4,eta],[0,2]]:S5 vee S6 -> S5 vee S6).

Let alpha be its bottom five-sphere and rho the six-sphere.
Then 2rho=-alpha eta and pi7D0 has basis b,c of order two,
where c=rho eta. In pi8D0 put n=alpha nu; it has order four.
The target eight-skeleton L8 kills both b and c.

Let mu:M(Z/4,6)->D0 extend rho. Let

    f:M(Z/2,6)->M(Z/4,6)

be the Moore map of bottom degree two and top degree one.
Let tilde_eta2:S8->M(Z/2,6) be an eta-coextension and set
tilde_eta4=f tilde_eta2. Both its pinch and its order are
the standard ones: pinch tilde_eta4=eta, and it has order
two. Other choices differ by bottom eta^2.

The maps mu f and -alpha bar_eta agree on the bottom
six-sphere, since 2rho=-alpha eta. Their difference factors
through the top S7 and hence is an element of pi7D0.
After composing with tilde_eta2 the difference belongs to
<b eta,c eta>. The exact stable Toda bracket gives

    bar_eta tilde_eta2 in {2nu,6nu}.

Both values have image 2n, because n has order four. Hence

    mu tilde_eta4 = 2n modulo <b eta,c eta>,
    mu tilde_eta4 = 2n in pi8L8.                       (5)

The choice ambiguity bottom eta^2 contributes rho eta^2,
which is c eta and also dies in L8. Thus (5) includes all
coextension and Moore-extension indeterminacies. This is
not a guessed Toda-bracket inclusion: it is a direct
comparison of two actual extensions through M(Z/2,6).

Opened primary sources:

* Brayton Gray, *Periodicity, compositions and EHP sequences*,
  Contemporary Mathematics 617 (2014), Section 2, printed p191.
  The extension/coextension construction is written there,
  followed by nu'={eta,2,eta} and its stable value 2nu.
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/gray4.pdf
* Pengcheng Li, *The homotopy classification of based maps between
  A_n^2-complexes*, arXiv:2008.03049v3 (2024), equations (3.1),
  (3.2), pp6--7, gives the Moore eta extensions/coextensions and
  the bottom/top degrees of f. Proposition 4.1 and Table 3, p10,
  explicitly give the Chang group and the generator delta used
  in Section 2. Its cofiber proof is also elementary as above.
  https://arxiv.org/pdf/2008.03049
* Daniel Isaksen, *Stable stems*, Table 23, printed p117, records
  the motivic bracket with the same displayed values {2nu,6nu}.
  Its complex realization is a compatible check, not a substitute
  for the direct classical argument supplied by Gray above.
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/isaksen-stable.pdf

The primary passages were opened in full through the web reader,
and the axioms agent independently audited the proof of (5).

## 4. What the integral filling forces, and its genuine indeterminacy

Equations (2)--(5) show that the K10 attaching composite for
the coordinated lower map is the suspension of 2n in L8.
The chosen nine-map lands in Sigma L8: the Jblock uses D0
and the c-cell, and Pblock uses the R-Moore factor. Therefore
the homotopy identifying the composite with 2n is also in
Sigma L8 and introduces no top-ten homology coordinate.
In the target L9 of D.2.22, the normalized cell N' attaches
by n. A reference filling uses two copies of that cell and
has integral Hurewicz coordinate 2N'. Its difference from
any other filling is an actual element of pi10W=pi9E.

The source relation in (3) consequently has obstruction
whose integral Hurewicz is 4N'. In the D.2.22 presentation
it is initially p or p+s; the sole integral-Hurewicz-zero
direction is s=rho nu. The actual cone detector distinguishes
these two possibilities, as follows.

For the coordinated nine-map the exact cohomology pullbacks
are q7=alpha3 beta4 and ell9=alpha3 delta6, where
delta6=Sq2 beta4. The R8 pullback contains the additional
class dual to B0^2, but that class has zero first Bockstein
and hence does not change ell9=Sq2 q7+Sq1 r8. The source
Cartan identities are

    Sq4(alpha beta)=gamma delta+beta X,
    Sq2(alpha delta)=gamma delta+beta X,

where gamma=Sq2 alpha and X=Sq3 beta. The cross term
Sq1(alpha) Sq1(delta)=beta X in the second formula must
be retained. Thus Sq4 q7+Sq2 ell9 vanishes on the whole A.

Let omega be the actual composite of the BX attachment
with g10. In Cone(omega), theta7 and lambda9 have unique
extensions, since the new cell has dimension eleven.
The value of Sq4 theta7+Sq2 lambda9 on its top cell is
zero for normalized p and one for s. For p this is the
zero-primary-detector normalization of D.2.22; for s it is
the suspended rho-nu detector of D.2.23. The evaluation
through Sigma E is valid in this range by Section 1.
Explicitly, throughout this comparison p is the lift with
h_Z(p)=4N' and Psi(p)=0. These two conditions fix the possible
s ambiguity. If one begins with an integral lift not yet
normalized by the detector, add s when necessary. This does
not silently change a common extension bit: if 2x=p is
nonzero, additivity gives Psi(p)=Psi(2x)=0 already; when the
common bit is zero the doubling relations are unchanged.

The actual cone map R10 union e11_BX -> Cone(omega) has
relative top degree one. Its pulled-back lower classes are
the restrictions of q7 and ell9 on the full source. Their
displayed sum of squares is zero. The new source eleven-cell
is a nonzero mod-two cohomology coordinate, since its boundary
is 2K10 in the chosen cellular-minimal model. Therefore the
top detector value of omega is zero. This rules out the s
addition and proves that the reference filling has obstruction
exactly p. It is an actual cone calculation, not an inference
that every mod-two invisible element is p.

The independent unavoidable filling indeterminacy is

    obstruction modulo 2 pi10W.                        (6)

Indeed changing the K10 filling by z changes the relation
2K10 by 2z; it does not change the already fixed lower map.
D.2.22 retains

    2p=2s=0, 2x=a p, 2y=b p,
    h(x)=K1-2aN', h(y)=K5-2bN'.                        (7)

Thus the phrase 'N coefficient two modulo four for every
filling' would be false when a or b is one. Adding x or y
then changes that coefficient while introducing the allowed
order-two homology direction. In exactly that case p lies
in 2 pi10W. The actual Browder representative of K1+K5
has order at most two, so the target agent has further
deduced a=b; the common bit remains unresolved at the time
of this note.

Consequently this calculation isolates precisely the p coset,
with its s coefficient zero and the full doubling ambiguity.
It does not yet prove a nonextension of every D.2.30 map,
does not handle the other branch which is nonzero on K6,
and does not construct a full A->W map. Those distinctions
are part of the current mathematical conclusion.

## 5. Auxiliary integral-chain certificate

The authored script code/I_k1_extended_power.py computes the
standard free C2-resolution tensored with the signed square
of a Moore chain complex, verifies d^2=0 over the integers,
and checks the Smith decomposition together with both basis
matrices. Its result is code/outputs/I_k1_extended_power.json.
It gives H7(D2 M(Z/2,3))=Z/4 and all its degree8--13 groups
of exponent two, while H11(D2 M(Z/4,5))=Z/8. The scope is
integral homology of these stable Snaith summands only.
It does not compute an unstable attaching map or replace
the component and Toda arguments above.

## 6. All seven integral degree-ten cycles and all eleven-cell couplings

This section fixes the coordinated R9 map of Section 2 throughout.
It does not enlarge the claim to maps nonzero on K6. The result
before determining the target bit is an exact conditional statement:
this fixed map has an extension through dimension eleven if and
only if the common bit in (7) is one.

To avoid collisions with the source eight-classes, use lower-case
m,n,o,t for the four unit ten-classes dual to u^3v,u^2w,v^3,t9.
The full mod-two degree-ten source basis is

    AR, Q6B, Q7A, A^2B, AF, AX, BD, BE, C^2, m,n,o,t.

Its complete nonzero first Bocksteins are

    beta(AR)=beta(A^2B)=A^3,
    beta(Q6B)=Q5B,
    beta(AX)=AD+AE,
    beta(BD)=AD, beta(BE)=AE,
    beta(o)=J9+L9.                                    (8)

All other values are zero. The image rank is five. Define

    K1=AR+A^2B,  K2=C^2,   K3=Q7A,   K4=AF,
    K5=m+n,      K6=t,     K7=AX+BD+BE.                 (9)

The following table lists the entire degree-eleven basis, not
only its primitive part, and every first Bockstein:

| Eleven-class | First Bockstein |
|---|---|
| BR | K1 |
| A Q5A | 0 |
| Q6C | K2 |
| Q7B | 0 |
| Q8A | K3 |
| A^2 C | 0 |
| AG | K4 |
| AH | 0 |
| AB^2 | 0 |
| CD | 0 |
| CE | 0 |
| BF | K4 |
| BX | K7 |
| unit dual to u^5 | 0 |
| unit dual to u^2v^2 | K5 |
| unit dual to uvw | 0 |
| unit dual to w^2 | K6 |

Thus eight basis generators have nonzero first Bockstein,
with AG and BF sharing their image, and the image rank is
seven. Cartan proves the product entries. The three Dyer
entries use beta Q^s=(s-1)Q^(s-1) in the free source, with
Q5C=C^2. The unit entries follow from
Sq1(u^3v)=Sq1(u^2w)=u^2v^2 and Sq1t9=w^2.
These are operations on the source itself, not operations
that an arbitrary ordinary map is assumed to preserve.

This also determines the exact integral group. The source
is of finite type with finite two-primary reduced integral
homology in each positive degree. The established group
H8A=(Z/2)^3 and dim H9(A;F2)=9 give six cyclic summands
in H9A by UCT. The dimension13 in degree ten then gives
seven cyclic summands in H10A. Rank seven for the first
Bockstein from degree eleven means that all seven have
order exactly two. Therefore

    H10(A;Z_(2))=(Z/2)^7.                              (10)

There is no unmeasured higher-exponent summand in (10).
As an independent check, the sole degree-ten E2 survivor
not in the span of (9) is the unit class represented by
m or n; its third Bockstein hits the unit ninth class
dual to u^4, exactly the known Z/8 in H9A. This is a Tor
partner of the preceding group, not an order-eight H10
class.

The integral cycle lattice H10(R10;Z_(2)) is free of rank
seven. Its reductions are precisely the independent classes
in (9), which are already integral reductions because they
are first-Bockstein images. Choose cycle representatives
lifting them; modulo odd units they form a lattice basis.
For K7 use the exact product-chain cycle in (3). The image
of the integral eleven-boundary is exactly twice this
lattice by (10). Consequently parity-preserving two-local
cell operations put seven eleven-cell boundaries in the
form 2K1,...,2K7, and make every other eleven-cell boundary
zero. The BX relation can be retained as the 2K7 coordinate.
The repeated AG/BF relation becomes their zero-boundary
difference. Even cell additions removing higher multiples
do not change any mod-two operation used in the cone test.
This is the integral normalization; reducing the cellular
boundary modulo two alone would not suffice.

For completeness, the entire second-square table of the
seven cycle classes is

    Sq2 K1=Sq2 K2=Sq2 K3=Sq2 K4=Sq2 K6=0,
    Sq2 K5=G8+H8,
    Sq2 K7=P+B0^2.                                    (11)

Thus only K7 has a nonzero coefficient on the J-Moore top
in the splitting (2). None has a Pblock-bottom coefficient.
All seven have integral ninth-cell degree zero, being cycles.
The cofiber computation of Section 2 now shows that the
attaching composites for K1,...,K6 are zero already in
Sigma L8, whereas K7 has composite 2n. This uses the full
source splitting: the only nonzero target factors are
Jblock and Pblock; all other projections are sent to zero.
Cross Whitehead terms cannot intervene, since the source
bottom dimension is seven and they start in dimension13,
above the attaching group pi9 under consideration.

Choose reference fillings of K1,...,K6 inside Sigma L8.
They contribute no target degree-ten homology. Use the
reference 2N' filling for K7. Since the chosen R9 map
already lands in Sigma L8, all these are coordinated
actual fillings of the same lower map.

For a normalized eleven-cell with boundary 2Ki, its
integral-Hurewicz obstruction is therefore zero if i<7
and 4N' if i=7. A zero-boundary eleven-cell also has
integral-Hurewicz obstruction zero. The actual suspended
Psi cone test of Section 4 applies to every cell: the
fixed lower pullbacks q7 and ell9 extend as the same
classes on the whole source, and their sum of squares
vanishes identically. Thus every obstruction has zero
Psi detector. By the exact target kernel of D.2.22,
all reference obstructions vanish except the 2K7/BX
coordinate, whose value is exactly p.

Changing the K7 ten-cell filling by z in pi10W changes
that one obstruction by 2z. It changes none of the other
normalized eleven-cell obstructions, because their
integral degree on K7 is zero. This is the actual cell
coaction law. It is linear in this range; a potential
Whitehead term involving the new ten-sphere would begin
strictly above dimension ten. In particular there is
no hidden coupling that spoils the correction if p is
twice an element of pi10W.

If the common bit is one, add x (or y) to the K7 filling;
then 2x=p and all eleven-cell obstructions vanish. If
the common bit is zero, pi10W is elementary abelian and
no change of any ten-cell filling can remove the BX
obstruction p. The chosen lower R9 map then has no
extension over R11. These are both statements about
the precisely fixed lower map; they do not classify
ordinary maps with different nonzero data on K6.

## 7. The other J-Moore top: an actual quotient and an exact Toda value

This section is a new source comparison, independent of any proposed
normalization of the target R-eta nullhomotopy. It varies only the
J-Moore top of the fixed lower map and keeps the other factors of
(2) fixed. The target computation of the resulting Toda value is a
separate obligation, presently owned by the fibrations agent.

There is an actual quotient map

    q_M:R9 -> S8

which on Jblock collapses its bottom seven-sphere and its eta
nine-cell, and projects to its Moore top eight-sphere. It is zero
on every other wedge factor. Indeed the nine-cell attaches into
the bottom seven-sphere, so after that sphere is collapsed the
quotient is S8 vee S9; projection to S8 gives the stated map.
The other J-top choice is the pointwise loop-space sum

    g9' = g9 + lambda q_M,

where lambda generates pi8W. This comparison uses the actual
H-group structure of W; it is not an assertion about arbitrary
maps preserving multiplication.

Let Ceta8=S8 union_eta8 e10. The exact cofiber sequence gives

    pi9(Ceta8)=0,
    pi10(Ceta8)=Z_(2){gamma},  h_Z(gamma)=2[top10].       (12)

For the second assertion, the preceding map
pi10(S9)->pi10(S8) is multiplication by eta and is an isomorphism
because eta squared generates the second stable stem. Therefore
pi10(Ceta8) injects into pi10(S10)=Z_(2), with image 2Z_(2).
There is no torsion ambiguity in (12). The entire calculation is
in the ordinary stable range of this seven-connected complex.

Compose q_M with S8->Ceta8. Since pi9(Ceta8)=0 it extends over
all ten-cells of R10. For the seven integral cycle coordinates
Ki in (9), their projected attaching maps are zero except
q_M(attachment K7)=eta8, by the complete second-square table (11).
A filling in Ceta8 consequently has even relative top degree
for i<7 and odd degree for i=7. Changing a ten-cell filling by
multiples of gamma changes that degree by even integers. With
the parity-preserving integral cycle basis used in Section 6,
choose the degrees to be 0 for i<7 and 1 for i=7. Denote this
actual extension by q_tilde:R10->Ceta8.

The normalized BX attachment has integral boundary exactly
2K7. Its composite with q_tilde has top degree two. By (12)
that composite is exactly gamma, with no undetected component.
Every other normalized eleven-cell has zero top degree and
hence zero composite in pi10(Ceta8). Thus this quotient comparison
also records all eleven-cell couplings: it changes only the BX
obstruction, not an unspecified selection of other relations.

The target relation lambda eta8=0 supplies an actual extension
lambda_bar:Ceta8->W. The composite lambda_bar q_tilde gives an
extension of the lower difference lambda q_M. Its sole possible
eleven-cell obstruction is

    lambda_bar gamma in <lambda,eta,2> subset pi10W.    (13)

Here gamma is the actual coextension of degree two across eta,
so (13) is the defining extension/coextension model of the Toda
bracket. Its full indeterminacy is

    lambda pi10(S8) + 2 pi10W
      = <lambda eta squared> + 2 pi10W = 0.            (14)

The first summand vanishes because lambda eta=0, and the second
vanishes by D.2.31. Thus (13) is a singleton independent of the
choice of lambda_bar and the ten-cell fillings. Since W is an
H-group, taking the pointwise sum with the D.2.32 reference map
adds the attaching composites in pi10W. The BX obstruction for
this specific altered lower map is therefore exactly

    p + <lambda,eta,2>.                                (15)

No four-cell subcomplex of the original source has been assumed.
The construction is an actual quotient comparison using its
complete R9 splitting and the normalized boundary d(BX)=2K7.

The cone detector on the bracket in (13) is automatically zero.
There is an actual map

    Ceta8 union_gamma e11 -> Cone(lambda_bar gamma)

of relative top degree one. The source has no degree-seven or
degree-nine cohomology. Hence the pullbacks of the uniquely
extended theta7 and lambda9 are both zero. Its mod-two top class
is nonzero, because the integral top boundary has degree two.
Consequently

    Psi(<lambda,eta,2>)=0.                              (16)

This rules out an s component without choosing the target
normalization of its R-eta attaching map. It does not identify
the integral-Hurewicz component, which is the remaining target
question. In particular (15) must not be replaced by p without
a computation of the actual bracket.

## 8. Component audit for arbitrary lower maps that kill K6

Root and axioms independently passed this strengthened reduction
at 20:26 UTC. It is not included in D.2.32. It concerns maps on R9,
not the branches
with nonzero data on K6. The conclusion below is only the integral
Hurewicz direction of the BX obstruction; an arbitrary such lower
map may have additional s-valued obstructions.

Suppose a lower map g9:R9->W has the epsilon-one degree-seven
pattern required of a putative full map by D.2.28. Then its value
on J has odd rho coefficient. Its values on the other seven-cells
need not be zero; in particular the unit or Q4A values may be even
multiples of rho, and no assumption is made on the J-Moore top.

Every such map lifts to W', then to Sigma E, by the ranges in
Section 1. The finite target comparison Sigma L8->Sigma E is
nine-connected, so a nine-dimensional source lifts through it.
The comparison is actual: both spaces are five-connected in the
cell realization range in use. No global minimal target CW model
is needed. In this lower target, rho eta is already null
because the c-cell belongs to L8. Thus rho eta squared is also
zero there.

Here is the complete projection of the K7 ten-attachment to
all ten factors of the source splitting (2):

| Source factor | Possible pi9 components | K7 projection and reason |
|---|---|---|
| Jblock | free gamma; Moore coextension delta | delta: degree on U is zero; Sq2 from its Moore top is one |
| Pblock=M2,8 | bottom eta | zero: the two P coordinates cancel in P+B² |
| Rblock=S7 cup_eta e9 | free gamma of top degree two | zero: K7 has zero ninth-cell degree |
| Fblock=M2,7 cup_(i eta) e9 | free gamma; torsion detected by Sq2 from its Moore top | zero: both the ninth degree and this Sq2 coefficient vanish |
| M2,8_H | bottom eta | zero: the H coefficient of Sq2 K7 is zero |
| M2,8_N | bottom eta | zero: the N coefficient is zero |
| S7_X | eta squared | its target image is zero already in Sigma L8, because every pi7 target value is a multiple of rho |
| each of the three S9 factors | integer degree | zero: K7 is an integral cycle |

There are no cross Whitehead terms: every factor is at least
six-connected and such terms begin in dimension thirteen, above
pi9. The zero entries use the full elementary cofiber groups,
not just an incomplete list of operations. For example, the
free component in a Chang factor is detected by twice its top
nine-cell, while its only torsion coordinate is detected by the
second square from the Moore top. The S7_X coordinate is retained
rather than incorrectly declared zero by primary operations.

On the J factor, any odd multiple of the reference Moore map
sends delta to 2n in pi9(Sigma L8), by Section 3: multiplying
2n by an odd integer leaves it unchanged since n has order four.
Two extensions with the same bottom differ by the unique class
lambda on the Moore top. This is the exact choice represented
by q_M in Section 7; it is not forced by the earlier primary
relations. Different choices on its nine-cell do not change the
image of K7, since K7 has degree zero on that cell.

The preceding component check shows that every other factor's
contribution to K7 is null already in Sigma L8. Such a contribution
can therefore be filled with no target degree-ten homology. Any
remaining ten-cell fillings exist by the D.2.30 cone-square
argument: R9 has H5=0, every source attaching Hurewicz is zero,
and the sole possible w9 obstruction is excluded by its actual
square cone. Their choices cannot change the BX integral
Hurewicz term, because its exact boundary is 2K7 and changes
of a K7 filling give twice an element of pi10W, now zero.

Consequently, modulo the integral-Hurewicz kernel <s>, every
zero-K6 epsilon-one lower map has BX obstruction

    p                for one J-top choice,
    p+<lambda,eta,2>  for the other.                    (17)

The cone detector in Section 7 makes the bracket's s coefficient
zero, but this paragraph does not assert that all the other lower
choices have zero s detector. It is enough that the p direction
in (17) is controlled. If the actual bracket is zero, no map in
this entire zero-K6 epsilon-one branch can extend over dimension
eleven. If it equals p, the coordinated top-toggle map of Section 7
has all its eleven-cell obstructions zero and gives an actual
extension through dimension eleven. Neither alternative has yet
been selected here. Maps nonzero on K6 require the separate unit
and Cblock analysis under way in the axioms agent's notes.
