# Independent audit of the actual secondary-operation comparison

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Independent audit of the proposed D.2.61 argument.
The full argument passes. This note records the exact promotion gate;
it does not assert a full fourth-suspension extension or solve D.2.4.

## 1. Primary source checked

I directly reopened Baues--Jibladze, *Secondary derived functors and
the Adams spectral sequence*, arXiv:math/0407031v3. Construction(4.1)
and Theorem4.2 define the secondary differential as the difference
of the two coherent tracks. Theorem7.3 and its complete proof on
printed pp19--21 identify it with the actual Adams differential;
the proof retains the fiber lifts and the track-composition lemma.
The source does not by itself identify a chosen Steenrod relation
with the specific scalar functional needed here. That additional
identification is the following direct calculation.

## 2. Exact relation coordinate in a genuine coresolution

Let M=H*(L;F2) and use its nonminimal free bar resolution:

    P0=A tensor M,
    P1=A tensor bar(A) tensor M,
    P2=A tensor bar(A) tensor bar(A) tensor M.

For a=a7, each of Sq1a,Sq6a,Sq8a is zero. The relation

    R=Sq1 Sq8 + Sq2 Sq1 Sq6 + Sq8 Sq1=0

therefore gives the exact Tor/bar cycle

    r=[Sq1|Sq8]a+[Sq2 Sq1|Sq6]a+[Sq8|Sq1]a.

In the free resolution, before tensoring with the augmentation,
its differential is literally

    Sq1[Sq8]a+Sq2 Sq1[Sq6]a+Sq8[Sq1]a.

The other terms vanish because the three inner operations kill a
and the sum of their outer composites is R. The scalar combination
r can be included in a free basis of P2. In the associated actual
GEM-spectrum coresolution L--g0-->A0--d1-->A1--d2-->A2, its coordinate
of d2 is consequently the specified three-operation row.

Write eta0 for the zero track d1g0 and eta1 for the zero track d2d1.
Their genuine secondary coherence is eta1 g0=d2 eta0. Choose any
stable nullhomotopy H of R and regard it as a zero track factoring
the degree-seven coordinate of A0. The difference

    q=eta1,r-H : A0 -> Sigma15 HF2

is an actual stable map. Its pullback g0*q is exactly the R-secondary
value with the inner nullhomotopies supplied by eta0. In particular
q retains the secondary structure of L; it is not permissible to
replace eta1,r by H and discard q.

## 3. Pairing with the actual incoming Adams differential

A primary-annihilated x in H15L represents an Ext0 class and a
map c:S15->A0. Choose c with only its degree-fifteen GEM coordinates
nonconstant. A zero track gamma of d1c exists because x is a cocycle.
The actual Adams track formula, evaluated in the r coordinate, is

    eta1,r c + (Sq8,Sq2 Sq1,Sq1) gamma.

The row uses only the degree8,13,15 coordinates of A1. Their zero
tracks on S15 are unique: pi16 of Sigma8, Sigma13 and Sigma15 HF2
is zero. Thus this row applied to gamma is zero. The bottom
degree-seven coordinate of c is strictly constant, so Hc is also
zero. The remaining value is qc. By the augmentation definition of
c this equals <g0*q,x>. Hence, with no track omitted,

    <r,d2 x> = <Phi_R(a7),x>.

Changing H changes the value by a positive degree-eight primary
operation on a. Changing the inner nullhomotopies changes it by
the row's positive-operation images. Both evaluate to zero on x.
The definite universal-space value may therefore be used in this
identity. The four-term dual Milnor functional is precisely r:

    [xi1|xi1^8]a,
    [xi1^3|xi1^6]a,
    [xi2|xi1^6]a,
    [xi1^8|xi1]a.

Its value on the bottom h0h3 class is one. This is a direct bar
coordinate identification, not a match based only on degree or
the abstract dimension of a universal Ext group.

## 4. The actual universal value evaluates to zero

Set F=hofib(Sq6 rho:K(Z4,7)->K(F2,13)). The mod-four lift of a
gives the Sq1 nullhomotopy, instability gives the Sq8 nullhomotopy,
and the fiber gives the Sq6 nullhomotopy. The resulting phi in H15F
restricts to Sq2 Sq1 i12 on its fiber. Double looping gives an
actual space splitting

    Omega2 F ~= K(Z4,5) times K(F2,10),

since the looped defining operation is Sq6 on a degree-five class.
There are no mixed positive products in degree13. Thus

    sigma2 phi=Sq2 Sq1 z10+eta,
    eta in H13 K(Z4,5).

Serre's generator theorem expresses eta as positive operations on
the two fundamental classes x5,y6 and decomposables. Those two
classes pull back to double cohomology suspensions of the actual
mod-four class and its integral coefficient connecting class on L.

Every primary-annihilated x in H15L has a primitive preimage z in
H13E, E=Omega2L: the double suspension is onto, and the nine product
directions of degrees5+8 and6+7 remove every reduced diagonal.
All their factors are primitive by connectivity, and the different
degrees make the tensor symmetrization injective.

Sq2_*z is primitive and lies in the already proved kernel
<uD,uE6,xi u> of H11E->H13L. The first two products have independent
nonzero reduced diagonals, so only xi u could remain. In the ambient
free E2 homology, a degree-thirteen outer restricted generator is
xi(y6). Its second square has restricted part xi(beta y6), while
no degree-six beta image has the u=xi a coefficient. Labels,
ordinary Hall brackets and products do not create that outer
restricted generator. The actual H11E injection therefore proves
Sq2_*z=0.

The fiber term now pairs to zero. The decomposables in eta pair to
zero on primitive z, and its positive-primary terms pair to zero
on the original primary-annihilated x by suspension naturality.
Consequently every incoming d2 has zero r coordinate.

## 5. Exact consequences and retained scope

The bottom image t of h0h3 is a nonboundary by D.2.58 and r(t)=1.
The preceding calculation excludes every incoming Adams d2; higher
incoming differentials would start in negative filtration. Outgoing
differentials vanish by naturality from the permanent sphere class.
Thus t is permanent. It detects the nonzero stable image of
alpha sigma-prime=alpha(2sigma), so the bottom cyclic Z4 generated
by the stable alpha sigma retains its double. Every nonzero
subgroup of this Z4 contains that double, so the entire bottom
AHSS group survives, including the possible incoming d8.

D.2.54 supplies a theta-detecting class already surviving through
page eight. Its last differential is now zero, and D.2.51 therefore
gives the actual equality h_M l4=0. The exact relation 2h=2q of
D.2.53, together with the nonzero stable q image, gives q=alpha
sigma-prime of exact order two in the actual target.

These conclusions concern the selected Moore composite and the
stable detecting class. They do not construct a corrective map
from the relative finite configuration complex, extend the
dangerous restriction to the full infinite-loop source, or prove
preservation under later nullification cones. Those are distinct
remaining tasks for D.2.4.
