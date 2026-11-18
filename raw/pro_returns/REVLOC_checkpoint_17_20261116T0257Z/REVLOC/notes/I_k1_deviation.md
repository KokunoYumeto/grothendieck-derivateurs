# The remaining once-suspended coefficient: exact finite constraints

**Status, 2026-11-15.** Research note. The first-cone criterion D.2.26,
the globally normalized secondary cup class of D.2.27, and the
once-suspended reduction of D.2.28 are proved. The remaining coefficient
epsilon below is not proved to vanish or to be globally realizable.
This note records actual finite tests and separates them from an
unproved equivariant extension of a multiplication deviation.

**Positive finite-stage update, 19:30 UTC.** The root and source agent
independently obtained an actual map on the source ten-skeleton with
epsilon=1. The complete construction is in Section 6. This replaces
the earlier conditional existence qualification for the particular
coordinated choice made there. It does not construct a map on the
full source, and the integral eleven-cell obstruction remains open.

Put B=K(F_2,2), X=Sigma B, A=QX, Y=Sigma²B,
Z=fib(Y->K(F_2,4)), W=Omega Z, and F=Omega W.
Thus W is four-connected and F is three-connected. Use the common
normalization of D.2.27. For any h:Sigma A->Y, a lift to Z has adjunct
g:A->W. D.2.28 leaves precisely

    g^*theta7 = epsilon alpha3 beta4,
    beta4=Sq1 alpha3.                                    (1)

All (co)homology in Sections 1--3 is over F_2.

## 1. The actual binary deviation and what its first tests permit

The target W is a loop space. Form the ordinary H-group difference of
g after source multiplication and the product of its two restrictions.
Its restriction to the source wedge is null, with the specified unit
nullhomotopies, so the cofiber universal property gives an actual map

    delta_g:A smash A -> W.

This uses only an H-group model and the actual difference construction
already used in D.2.16. It does not assert that g is an H-map or that
delta_g has an equivariant extension to E(Sigma_2).

The class theta7 is primitive for multiplication of W, simply because
positive cohomology of W starts in degree five. The classes alpha3,
beta4 are primitive for multiplication of A. Consequently

    delta_g^*theta7
       = epsilon(alpha3 tensor beta4+beta4 tensor alpha3).
                                                               (2)

On X smash X=Sigma²(B smash B), this is
epsilon sigma²(u tensor v+v tensor u), with v=Sq1u. It is the
Bockstein of epsilon sigma²(u tensor u). In particular it evaluates
to zero on the symmetric integral bottom smash-Moore cycle ab+ba.
Thus a spherical test on that cycle does not detect epsilon.

The full source-primary relations do not remove (1). Put
gamma5=Sq2 alpha3 and delta6=Sq2 beta4. The strengthened relation
from D.2.28 is compatible with

    q7=alpha3 beta4,   r8=alpha3 gamma5,
    lambda9=alpha3 delta6.

Indeed Sq1 q7=0, and
Sq2 Sq1(alpha3 gamma5)=Sq4(alpha3 beta4).
The exact relation lambda9=Sq2 q7+Sq1 r8 also holds. These are actual
products in H^*A, so requiring the deviation of r8 to be the reduced
coproduct of a source cohomology class does not by itself add an
obstruction.

There is even an actual bottom finite-smash realization. Let
M=M(Z/2,3). Its integral cellular generators a3,b4 satisfy db=2a.
The chains of M smash M are

    d(ab)=-2aa,   d(ba)=2aa,   d(bb)=2(ab+ba).

After the integral basis change, the space has the stable cell model

    (M(Z/2,6) wedge S7_e) union_(i eta6,2) e8,             (3)

where e corresponds to ab+ba. The eta component is detected by
Sq2 of the bottom cohomology class, since its Cartan cross term is
the top bb class. The model is realized ordinarily in this range:
the source is five-connected and the attaching dimension is seven.

The corrected k4 Moore map, obtained by restricting the actual
Browder map lambda(a,j):Sigma³B->Omega²Y, lifts to F. Its adjoint
M(Z/2,6)->W has bottom 2alpha in pi6W=Z/4 and top theta7 coefficient
one. Take value zero on the free S7 in (3). The last attachment maps
to (2alpha)eta6=4rho=0, because alpha eta6=2rho in pi7W=Z/4.
It therefore extends across (3), with the desired symmetric
Bockstein functional (2). This proves only compatibility on this
finite smash. The source is not the full extended power D2(M),
and no coherent equivariant extension is inferred.

## 2. Exact low homology branches for an ordinary g:A->W

Let A0,B0,C5,D6,E6,F7,X7 be the usual unit labels and put
R7=Q4 A0. In H_7W use the homology suspensions of the F basis

    d=b²,   e=b²+{a,b},   f=p3,

and use R8 for the suspension of R={a,c}. Here all three d,e,f
have second square equal to the bottom H5W class; all have zero
first Bockstein. The degree-eight W classes are V8,R8,P8,Q8, with

    beta V8=e, beta P8=f, beta R8=beta Q8=0,
    Sq2 V8=u6, Sq2 P8=Sq2 Q8=z6, Sq2 R8=0.

The source identity beta R7=A0² immediately gives g_*(A0²)=0.
First Bockstein and the unit H8 relation beta H8=0, Sq2 H8=E6
then force g_*D6=g_*E6=0: beta permits only the u6 coordinate,
whereas a beta-cycle in H8W has second square in the independent
z6 line. This is an ordinary naturality argument.

Suppose epsilon=1 in (1). The theta coefficient and Sq2 then give

    g_*(A0B0)=t d+e+(1+t)f,
    g_*R7=t' (d+f),                                     (4)

for t,t' in F_2. These are not interchangeable choices of basis:
the first vector is k=d+e if t=1, and r=e+f if t=0.

The exact source calculation D.2.19v gives

    beta2[B0²]=[R7+A0B0].

The image of B0² under g is a multiple of R8, by its zero first
Bockstein and zero second square after mapping. But R8 is a first
Bockstein boundary in W (beta J3=R8). On the second Bockstein
page in degree seven, only the d coordinate survives: e and f
are the first Bockstein boundaries displayed above. Naturality
therefore forces t'=t. The two possible branches are exactly

    (g_*R7,g_*(A0B0)) = (0,e+f) or (d+f,d+e).            (5)

This records a necessary condition, not a realization of either
branch on the full A. In particular the r branch cannot silently
be selected when studying the next AC/AD/BC cellular block.

## 3. The Hurewicz kernel after delooping is real

D.2.20 alone proves injectivity of pi8F into H8F; it does not
classify the actual image. The later proof D.2.22t19 supplies
the additional actual statement: pi8F=pi8T=(Z/2)^2, represented
by the W8=A4² and J2 eight-spheres. This follows there from the
four-connected cover E and its complete eight/nine-cell sequences.

Adjunction identifies pi9W with this group. Homology suspension
kills the Pontryagin product W8=A4² and retains J2. The same
path-spectral-sequence calculation used in D.2.27 identifies
H9W with H8F modulo the W8 line. Therefore

    ker[pi9W -> H9(W;F_2)] = Z/2{w9},                   (6)

where w9 is the adjoint of the actual W8 sphere. Thus the
injectivity statement for F must not be transported to W.

## 4. A cup-square detector repairs the tenth-cell extension test

Let a5 be the bottom cohomology class of W. The actual cone of w9
has a unique extension aHat5 of a5, and

    aHat5² is its nonzero relative top class in H10.       (7)

This is a direct Adams--Hilton calculation. The adjoint of w9 has
Hurewicz A4² in H8(Omega W)=H8F. In a minimal AH model for W,
the bottom degree-four generator A4 is a cycle. The cell-attachment
formula of Halperin--Lemaire, Section 3.1, p300, adds a degree-nine
generator with differential representing A4². Changing this new
generator by an old chain makes its differential exactly A4².
It has no linear part, and its quadratic part is the new reduced
diagonal. Thus the square of aHat5 evaluates to one on the new
ten-cell. The square a5² in W itself is zero: otherwise the same
quadratic-diagonal calculation would make A4² a boundary in H8F,
contrary to its nonzero established value. Hence (7) is exactly
the relative top class, with no old summand ambiguity.

Here is the precise extension consequence. Work in a finite two-local
CW model of the required source range in which odd-unit cellular
pairs have been cancelled, so the cellular differential modulo two
vanishes through dimension ten. This condition is essential when
talking about an arbitrary map of a chosen skeleton. Let K9 be its
nine-skeleton and K10 its ten-skeleton, and suppose the bottom
cohomology pullback of a given g9:K9->W extends from a class on A.
This holds for the source models here because inclusion of the
nine-skeleton is an isomorphism in degree five. Every ten-cell
attaching map has zero mod-two Hurewicz in K9, so its composite
with g9 belongs to the two-element group in (6).

If that composite were w9, the actual map of cell-attachment cones

    K9 union e10 -> Cone(w9)

would pull the relative top class back with degree one. Its pullback
of aHat5 is the restriction of the degree-five class on A. Every
positive cohomology square in A is zero, so its square is zero
already on K9 union e10. This contradicts (7), because the new
ten-cell is a nonzero mod-two cohomology coordinate in the chosen
model. Thus the obstruction is zero. Treating cells separately,
or their relative coordinates, proves the same conclusion for a
small simultaneous set of ten-cells.

One may instead factor through Q=A/A4, since W is four-connected.
The quotient maps H5Q and H10Q isomorphically to the corresponding
groups of A; hence the relevant degree-five square is still zero.
Odd-unit cancellation is made in the actual two-local cellular
model, not by replacing an unstable attaching map with an
unjustified stable matrix. Retaining a cancelled pair gives an
equivalent relative extension problem. A change of source skeleton
must be carried along explicitly: this does not claim that every
map on an arbitrary unminimized nine-skeleton extends.

The result is a conditional positive finite-stage statement: once
such a g9 has been constructed, these tenth-cell obstructions vanish.
It does not construct g9, remove a possible eleven-cell rho-nu
obstruction, or construct a map on the full source A. Root and
axioms independently checked the actual-cone detector argument.

## 5. The next tensor block is relative

The integral formal block on A0C5,A0D6,B0C5,B0D6 has

    d(A0D6)=-4(A0C5),   d(B0C5)=2(A0C5),
    z=A0D6+2B0C5,       d(B0D6)=2z.

It is not an absolute smash of subspaces M(Z/2,3) and M(Z/4,5)
inside A. The C5 class has Sq2 C5=A0, so is not a spherical
Moore bottom in the actual A. It becomes one only after collapsing
A4. In an actual deviation source the C-cell attaches through
id smash eta into the preceding bottom smash-Moore block. Those
lower attachments must be retained; in particular z need not be
spherical. This is the remaining concrete relative-cell problem,
not a shortcut to an already established obstruction.

The full mod-two constraints in this block can nevertheless be
derived, without selecting a branch in (5). Write D9=L9+M9 for
the suspension of the target combination L8+M8. Under epsilon=1,
the strengthened relation of D.2.28 forces

    g_*(A0C5)=R8,      g_*(Q5A0)=0.                      (8)

Here are direct witnesses for the R8 coefficients, avoiding a
computer-only assertion. The degree-eleven source BX satisfies

    Sq4_*(B0X7)=A0B0,
    beta Sq2_*(B0X7)=A0C5.

Indeed Sq2(BX)=AD+AE+BC and only the last has Bockstein AC.
The source Q8A0 satisfies

    Sq4_*Q8A0=Q4A0,   beta Sq2_*Q8A0=Q5A0,

by Nishida. Pairing the relation Sq4 q7+Sq2 beta r8=0 gives
the required R8 coefficients 1 and 0. The complete target
degree-eight basis, with beta and Sq2 as in Section 2, then
turns those coefficients into the full vector equations (8).

The suspended target degree-nine basis is

    C9,L9,M9,J1,J2,J3.

The product W8 disappears under homology suspension. Its operations
are inherited from the full F table:

    beta L9=beta M9=Q8, beta J3=R8,
    Sq2 L9=d, Sq2 M9=f,
    Sq2 J1=Sq2 J3=d+e,
    Sq4 C9=the bottom H5W class,

and all other entries needed here are zero. On the source,

    beta(AD)=0,      beta(BC)=AC,
    Sq2(AD)=Sq2(BC)=AB,
    Sq4(AD)=Sq4(BC)=0.

The cohomological identity lambda9=Sq2 theta7+beta R8,
pulled to the source, makes the J1 coefficient on AD equal to
one and that on BC equal to zero: after (8), the mixed product
part of the pulled-back lambda is precisely alpha3 delta6.
Equivalently this follows by pairing that identity directly
with AD and BC. The displayed target table now yields

    g_*(AD)=J1+(1+t)D9+j J2,
    g_*(BC)=J3+(1+t)D9+j'J2,                            (9)

with independent still-undetermined j,j' in F_2. For example,
beta(AD)=0 forces the L,M coefficients to agree and the J3
coefficient to vanish. Its J1 coefficient is one, so matching
Sq2 with t d+e+(1+t)f gives their common coefficient 1+t.
The BC calculation is identical except that beta(BC)=R8 forces
its J3 coefficient to be one and its J1 coefficient is zero.

Thus the previously suggested vectors J1+D9 and J3+D9 are the
t=0 branch, not universally forced values. Both t branches
remain consistent with the complete primary table in this block.
The BD ten-cell has zero mod-two cellular boundary, so Section 4
removes its remaining actual obstruction once a compatible g9
has been chosen. The next possible obstruction is an actual
eleven-cell obstruction in pi10W=pi9F. Its integral-Hurewicz-zero
part is the nonzero rho-nu class of D.2.22; its mod-two kernel
also includes the direction with integral Hurewicz 4N in the
order-eight target homology group. A compatible primary table
does not determine a possible integral 2N filling coefficient.
Neither of those subsequent choices is settled by (8)--(9).

## 6. An actual epsilon-one map through the ten-skeleton

This is a positive existence statement for one coordinated finite-stage
choice. Use the actual two-local cell model of Q=A/A4 established in
D.2.19--D.2.20, with the odd-unit pairs cancelled in a finite range
containing dimension eleven. The cancellation is performed on the
actual localized CW approximation. Thus its mod-two cellular
differential is zero in the relevant dimensions. The target W is
two-local, so such localization and cellular approximation preserve
the mapping problem. The source quotient is four-connected.

The proved eight-stage wedge decomposition is

    Q8 = D' wedge M(Z/2,7)_F wedge M(Z/4,7)_J
           wedge C1^8_z wedge S8_s,                     (10)

where D' is the unit block, J is the seven-sphere with mod-two
label R7+A0B0, C1^8_z is the cofiber of (2,eta6) into the
six-sphere, and s has integral label Q5A0-A0C5. All equivalences
and cell slides in (10) are actual in this range: maps involving
four-connected targets and source dimension at most eight are in
the stable range. Equivalently one can use the actual cell slides
of the existing D.2.19 construction.

The target facts needed here are all already proved:

    pi7W=Z/4{rho}, h_mod2(rho)=r=e7+f7;
    pi8W=Z/2{lambda}, h_mod2(lambda)=R8;
    pi9W=(Z/2)^2, ker h_mod2=Z/2{w9}.                  (11)

The first two are the adjoints of D.2.18--D.2.19; the last uses
the additional actual image computation D.2.22t19, not D.2.20
alone. The class w9 is detected by the cup square in its actual
cone, as proved in Section 4.

Set the map equal to zero on D' and M(Z/2,7)_F. Send the bottom
of M(Z/4,7)_J to rho. Its top extension exists since 4rho=0.
Any such extension sends the top mod-two eight-class into the
R8 line: first Bockstein and Sq2 both vanish on that class,
and the complete H8W table has simultaneous kernel precisely
the R8 line. Changing the extension by the actual sphere lambda
toggles that coefficient. Choose the extension with top image zero.

On C1^8_z take the lower six- and seven-skeleton to zero and
map the top eight-cell, by its pinch, to lambda. This is an
actual map since all its lower attaching data have zero image.
Send s to -lambda. Together these choices define an actual g8.
In the original source labels they give

    g8(R7)=0,      g8(A0B0)=r,
    g8(A0C5)=R8,   g8(Q5A0)=0,   g8(B0^2)=R8.           (12)

The last identity uses the precise cell slide B0^2-A0C5 that
produced the top cell of M(Z/4,7)_J. The unit block maps to
zero. Consequently the degree-seven pullback is exactly

    g8^*theta7=alpha3 beta4.

Every source nine-cell has zero mod-two cellular boundary. Its
attaching map therefore has zero mod-two Hurewicz in Q8, and
so does its composite with g8. The middle equality of (11)
makes the target Hurewicz injective in this degree. Every such
composite is null. Choose nullhomotopies to obtain an actual g9.
No compatibility condition between these independent cell
extensions is missing: their domains attach to the fixed Q8.

For each ten-cell the same mod-two argument puts its composite
with g9 in {0,w9}. If the value were w9, the actual map of cones
would pull the nonzero square of the bottom class in Cone(w9)
to a nonzero relative ten-class. Here the pullback of that bottom
class is already zero on Q9, since g8 was zero on D'. It also
vanishes on the source one-cell extension, as attaching a ten-cell
does not affect degree-five cohomology. This contradicts the
cone square. Thus every ten-cell obstruction is zero, and any
choice of the ninth-cell fillings extends to some actual g10.

The resulting actual map Q10->W, and its composite from a
corresponding finite ten-skeleton of A, has epsilon=1. The low
values in (12) and the branch t=0 are retained. A cellular map
from any initial finite-type model to this localized minimal
model transports the finite-stage example while preserving its
low cohomology statement; no identification of unrelated
skeleton-level homotopy classes is claimed.

This construction proves that the remaining coefficient cannot
be excluded by an obstruction below dimension eleven. It does
not say that every other g9 has the same cohomology pullbacks,
nor that arbitrary eleven-cell choices are harmless. The next
target pi10W has the nonzero rho-nu integral-Hurewicz kernel and
the 4N direction described at the end of Section 5. Those are
separate actual extension tests.

The root independently supplied the same g8 construction; the
source agent checked its ordinary range, top-cell choices and
the complete nine/ten extension argument. The axioms agent has
independently checked the actual-cone square detector.
