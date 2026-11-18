# Independent audit of D.2.42

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Full mathematical audit passed.

Read `FGH_D2_k4_relative_target.md`, Sections 8--9, and the final
`sections/D2_fourth_secondary.tex`. This is a fresh check of the actual
relative class and its nonmembership in the proposed odd-operation
span, not a claim that a finite source realizes its nonzero value.

## Actual class and common normalization

The eight degree-fourteen products in the old loop target have the
independent tensor words listed in D.2.42f. The old loop generators
start in degree six, so cubic terms start in degree eighteen. This
excludes a quadratic boundary among those eight words and proves the
needed degree-sixteen cup products vanish, including the square of
the specified class y8.

The singular-cochain formula

    Theta15 = [q*c15 - P7 cup q*y8],
    dc15=y8 cup y8, dP7=q*y8,

is closed. Changing P changes its class by zero, while changing c by
a cocycle changes Theta by the restriction of that one cocycle. This
is the actual Mayer--Vietoris cochain construction already proved in
D.2.26, not an abstract cone algebra.

For epsilon:Sigma4 V -> Z', new Adams--Hilton generators start in
degree ten. Thus no old/new term occurs in differential degree
fourteen (their least degree is sixteen). On the kernel of the map
on H15, cancellation of the linear part leaves precisely the old
quadratic coordinates. The source once adjunct is a suspension map,
so its image is primitive: the DE and ED coefficients agree and
cancel when paired with y8 tensor y8. The D² and E² coefficients
give the paired functional.

The suspension indices were checked explicitly. The original ambient
functional is on H13(Omega²Y); mu11 is its twice-pulled-back
cohomology suspension on U. Three homology suspensions from V take
degree eleven to degree fourteen in Omega Z'. The final suspension
takes xi1(k) and xi1(f) to (ab+ba)² and f². It is not a second
suspension of those squares, which would vanish. The independent
Hall/restricted-square basis gives exactly the claimed two
coordinates. Consequently equality on the kernel permits one common
linear-functional extension in H15(Z'), and hence one common choice
of c15. Fourfold cohomology suspension from the nine-connected cover
is an isomorphism in all degrees used here, since the last loop
space starts in degree six and its first product degree is twelve.

## Shifted Postnikov computation

I checked all three odd-degree input lists in the note. Through the
needed range, the five nonzero transgressions of the s9 family are

    s9 -> Sq3 x7,
    Sq2 s9 -> Sq5 x7,
    Sq4 s9 -> Sq5 Sq2 x7,
    Sq6 s9 -> Sq6 Sq3 x7,
    Sq4 Sq2 s9 -> Sq7 Sq2 x7.

Adem and Sq1 x=0 give the displayed values; the last also uses
Sq9 x7=0. These are distinct polynomial generators, so their
successive quotients introduce no annihilator cycles. The surviving
s-generators in degrees twelve and fourteen do not contribute a new
class in input degrees eleven, thirteen, or fifteen. There are no
mixed products with them in that range.

The complete operation checks on the stated spanning lists are:

* beta in degree fifteen gives x Sq2 x, or the killed Sq7 Sq2 x.
* Sq3 in degree thirteen gives zero or that same killed class.
* Sq5 in degree eleven gives zero or that same killed class.
* The separate K(F2,9) factor contributes only Sq7 t and Sq5 Sq2 t.

The square y8² is a distinct base polynomial monomial and survives.
The apparent additional possible bidegree-(7,8) source xr for a d9
into total degree sixteen is permanent because r is an actual class;
it is not a missing differential. I suggested saying “only possible
nonzero sources” in the final text's sentence about the two
degree-fifteen fiber generators, solely for this literal precision.

## Unambiguous transgression and conclusion

For L' -> L -> P9L, the base begins in degree seven and the fiber
in degree ten. For a fiber class of degree j between ten and
fifteen, every differential before d_(j+1) has zero target.
Moreover a mixed source hitting the scalar base line would have
target total degree at least eighteen. Thus the transgression in
this range lands in the full H^(j+1)(P9L), with no earlier scalar-line
quotient or unspecified indeterminacy. The ordinary Steenrod
transgression identities apply to all three operations used.

In a strict fiber model the chosen base y8 restricts literally to
zero. Taking P7=0 then identifies the transgression of Theta with
y8². The common change by a total-space cocycle has zero
transgression. Therefore membership of Theta in beta/Sq3/Sq5 of
the indicated lower fiber groups would put y8² in the computed
three-dimensional operation span on P9L, which is impossible.

This proves the nonzero class and the negative operation-criterion
result exactly as stated in D.2.42. It does not calculate the image
of stable maps from the finite eleven-dimensional source, does not
resolve its remaining secondary/integral attachments, and does not
establish a full fourth-suspension extension or nonextension.
