# Root audit and finite source for the remaining half-product

15 November 2026, 23:53 UTC. This is a research reduction, not a
solution of D.2.4 and not a numerical evaluation of x8 squared.

## The actual six-type and coefficient normalization

Root read the entire note I_integral_P6_target.md, including its
new Pontryagin-square normalization. The two possible degree-seven
base classes are Sq3u4 and Sq2Sq1u4. Pullback kills the former and
not the latter; the invariant cannot be zero because that would
give two independent H6 classes in the six-type whereas Y has one.
Thus P6Y is the fiber of Sq3. The coefficient pullback description
follows from Sq3=Sq1Sq2 and the exact coefficient fibration.

Sigma²P2(u2) is an odd mod-four lift of Sq2U4. Any such lift gives
a map to the pullback inducing the identity on pi4 and pi6, so
is a permissible Postnikov projection. Multiplication by minus one
on K(Z4,6) fixes its mod-two base and coefficient fiber and exchanges
the two odd lifts. Finally H5(Y;Z4)->H5(Y;F2) is onto by UCT:
H4Y=Z2 and H5Y=0, and the induced map on Ext is the quotient
Z4/2Z4 -> F2. Hence the relevant compatibility-homotopy ambiguity
is removed by that preceding term. This passes without fixing a
high-dimensional multiplicative extension.

## The half-product on the higher cover

Root read all of EH5_half_product_fiber.md. In a strict fibration
model the normalized base cochains A7,B8 restrict literally to
zero. The chosen C14 with dC=AB−2E therefore gives k14 on L',
with transgression xy and Sq1(k14)=q*theta. The first nonzero mixed
base/fiber degree is17, so there is no earlier mixed term in this
range. The transgression xy is nonzero; k14 cannot be silently
extended to L. No global Steenrod decomposition follows.

The lift theta4=[E−2C15 mod4] has d(E−2C15)=−4D16 when
B²+2D16=dC15. Thus theta evaluates to zero on every integral
class of order at most two. The necessary stable-Hurewicz witness
has order at least four. This is an image condition, not a claim
about all of pi15 stable or all of H15.

The cofiber comparison L/L' -> P9L is16-connected: the two maps
out of L' have connectivities6 and10, giving a15-cartesian square
by Blakers–Massey, followed by the fiber comparison. It therefore
supplies the stated stable exact segment through degree15. Its
connecting map remains the original uncomputed obstruction.

## A concrete finite source for the integral chain comparison

Let M=M(Z2,2), and use the quadratic weight D2^(2)M of C2M.
Its integral chains have aa in degree4; ab,ba,U=e1aa in5;
bb,H=e1ab,J=e1ba in6; and Z=e1bb in7, with db=2a.
The free C2 resolution through dimension one gives

    dH=ab−ba−2U,  dJ=ba−ab−2U,
    d(bb)=2ab−2ba, dZ=2bb−2H+2J.

Put D=−H−J and V=bb−H+J. Then dD=4U, dV=0,
dZ=2V, and V=bb+D+2J. The explicit integral changes of basis
in code/D2_C2_Moore_integral_chain.py have determinant plus or
minus one and cancel one unit pair. They give integral homology
Z2 in degree4, Z4{U} in5, and Z2{V} in6. The exact certificate
passes. The first run passed all matrix assertions but failed to
serialize SymPy integers; conversion to native integers fixed that
output-only issue. No mathematical assertion was changed.

These chain summands are not a stable wedge splitting. The stable
eta attachments remain necessary data. The actual Browder map
Sigma(S5 smash C2M)->T, using the actual class U:S5->T, has source
starting in degree8 and therefore lifts uniquely to the connected
cover E=Omega²L. Its suspended U coordinate is the self-Whitehead
product of alpha:S7->Y, hence zero because S7 is an H-space.
The D coordinate is the candidate mixed commutator in Omega L.
The V=bb+D+2J identity exposes the remaining even correction;
J is not a cycle, so neither an ambient tensor boundary nor a
nullhomotopy of four times the whole map can be used without
tracking the induced homotopy on dJ. The fibrations and simple
agents are computing that genuine stable source comparison.

## Additional actual-map constraint

The actual Browder lift is annihilated by four. After two adjunctions
it is [alpha,e]:Sigma(S6 smash Sigma C2M)=Sigma8C2M ->Y, where
e:Sigma²C2M->Y is evaluation. Both desuspended factors S6 and
Sigma C2M are suspensions, so the opened Arkowitz1962 Proposition3.4
gives bilinearity. Thus four times the map is [4alpha,e]=0. The
source starts in degree8, so maps and homotopies into the lower
Postnikov base of T vanish; this nullhomotopy class lifts to E.
Both simple and axioms independently checked the exact source
and group-law interface. This still does not set4f(J) to zero
chainwise, since a chain homotopy contributes on dJ.


## 16 November 2026: secondary Pontryagin normalization audit

The root read the new normalization in I_integral_P6_target.md and
reopened Thomas, Pacific J. Math.9(1959), pp.897--898 Theorem I,
the proof in Section5, and Proposition6.9/p.908. The latter proof
uses the product formula and the one-dimensional suspension class
to show S(p)=0. Hence S²(P2)=0, so P2(U4)=0 for the actual bottom
class U4=Sigma²u2 on Y=Sigma²B. A chosen nullhomotopy gives an
actual lift to fib(P2:K(F2,4)->K(Z4,8)), and passing to fibers
over K(F2,4) gives a_Z:Z->K(Z4,7).

To identify its restriction on L, use alpha=u4 nu4. The actual
map of mapping cones HP²=C(nu4)->C(alpha) has relative top-cell
degree one. Its bottom class pulls back to the reduction of the
integral degree-four generator; the Pontryagin square pulls back
to that integral square modulo four and has top-cell value one.
Thus the defining relative obstruction evaluates a_Z on alpha
as an odd generator of Z4. Changing the initial nullhomotopy adds
a pullback from H7(Y;Z4). Since alpha factors through S4 its
ordinary integral Hurewicz in Y is zero, so this added class
evaluates as zero. On the six-connected L, H7(L;Z)=Z4 is
generated by alpha and H6L=0; coefficient UCT therefore makes
the entire restriction of the ambiguity zero. The normalization
is valid and independent of that choice, up to the orientation
of the named generator.

This does not compute the integral square of beta4(a7). No
Pontryagin-square suspension identity is being interpreted as
vanishing of that higher integral product.

Primary source opened by the root:
https://msp.org/pjm/1959/9-3/pjm-v9-n3-p26-p.pdf
