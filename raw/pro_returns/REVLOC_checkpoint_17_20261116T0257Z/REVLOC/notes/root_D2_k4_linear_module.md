# The entire fourth-suspension unit has zero linear degree-eight image

15 November 2026, root; research calculation begun about 21:20 UTC.

## Exact scope

For every ordinary pointed map `h: Σ5 B -> Σ2 B`, with
`B=K(F2,2)`, its degree-eight mod-two homology homomorphism is zero.
This excludes the second bottom Moore pattern `r=b²+k+p3` for an
entire unit map. It does not yet exclude the known pure-commutator
unit map or prove extension/nonextension for arbitrary full `QΣB` maps.

## Source-only proof

The cohomology map, with suspensions removed, is an arbitrary linear
map φ of degree minus three on reduced H*(B), commuting with all
Steenrod squares. It is not assumed multiplicative. Write
`u2,v3,w5,t9,s17` for the first Serre generators.
Suppose φ(u³)=v. Since H1(B)=0, φ(u²)=0. The exact identities

1. Sq4(u²)=u4;
2. Sq3(uv)=uv²+vw;
3. Sq2(u³)=u4+uv²;
4. Sq6(v²)=v4;
5. Sq4(vw)=vt+v4;

give successively φ(u4)=0, φ(uv²)=φ(vw)=w, φ(v4)=0,
and φ(vt)=t. Here Sq3 φ(uv)=0 and Sq6 φ(v²)=0 by
instability, without a restriction on those unspecified coefficients.

The remaining exact identities are

6. Sq10(uvw)=u²v²w²;
7. Sq9(ut)=ut²+vs;
8. Sq8(vt)=vs;
9. Sq4(uwt)=ut²+u²v²w².

The first is a top square, while the second and fourth follow by
Cartan; Sq1(t)=w², Sq8(t)=s, Sq9(t)=t², and Sqj(t)=0 for
2<=j<=7 follow from Adem and instability. Since φ(uvw) has
degree7 and φ(ut) has degree8, identities6--8 imply
φ(u²v²w²)=0 and φ(ut²)=φ(vs)=s.
Identity9 would therefore give Sq4 φ(uwt)=s. But φ(uwt)
has degree13, and every degree13 class of H*(B) is decomposable:
the algebra generators have degrees2,3,5,9,17,... . Cartan
preserves the decomposable ideal, whereas s is indecomposable.
This contradiction proves φ(u³)=0. Also
φ(v²)=φ(Sq2u²)=Sq2φ(u²)=0. These two classes are the entire
degree-six cohomology basis of B, proving the homology assertion.

## Computation and independent review

`code/D2_k4_linear_module.py` constructs the Serre polynomial algebra
using Adem reduction on admissible words, then Cartan on monomials.
It allows every coefficient of φ in the range. Gaussian elimination
with exact F2 integers returns a dependency containing precisely
the prescribed u³ coefficient and the nine identities above.
With only φ(u³)=v fixed, the range through degree19 is consistent,
and degree20 is inconsistent. A consistent finite module map is
not asserted to be realized by a map of spaces.

The implementation also checks all applicable Adem relations on
every source monomial through degree20 (1573 checks), including
top-square identities. These are internal algebra checks, not a
replacement for the printed source formulas or the proof above.

Fibrations independently checked every Cartan/Adem identity and
the suspension interface, and confirmed no other fixed coefficient
is used. Further independent reviews are recorded when received.

## Consequence for the remaining relative test

For a full map `Σ4 A -> Y`, `A=QΣB`, the unit spans all degree-eight
source homology. Its attaching homology map in this degree is
therefore zero. In the double adjunct the degree-six primitive image
of the unit B6 is consequently either zero or the pure k class:
the p3 component vanishes, and Sq2 excludes the b² coefficient.

One must still control arbitrary ordinary maps on the quadratic
extended-power part. For a fixed entire unit restriction, compare
with its canonical C4 extension, not just with the specific h0 in
D29. If the relevant target suspension H4U -> H6E is an isomorphism,
the canonical top operation has the same paired coefficient for
every unit with image k. This is the interface to check in applying
the universal relative D -> V test; it is not a proved global
nullification conclusion.


All three parallel readers subsequently passed the nine identities and the ordinary suspension interface. Fibrations also read the complete final TeX; the one noted code-documentation mismatch had already been repaired: the current program fixes only u³->v, with degree19/20 equation counts3124/3785 after including the degree-five equations explicitly. The final degree20 dependency again uses exactly the nine stated identities.

The Moore-only scope repair in `EH5_k4_relative_square.md` was read independently by root: maps M(Z2,3)->U have the short exact Moore sequence with kernel coker(2 on pi4U) and quotient ker(2 on pi3U), both Z2. The bottom bit and rho-top bit classify the four maps. With the linear coefficient excluded, every dangerous map has the same Moore restriction as the canonical one. Restricting to C4M removes any need to identify entire unit maps. The relative D->V paired-functional test, if proved, would therefore cover every dangerous k4 map. It is still unresolved.
