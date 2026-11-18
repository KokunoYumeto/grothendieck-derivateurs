# Degree-fifteen source space and the integral-lift distinction

**Status update, 2026-11-16 02:49 UTC.** The geometric edge and bar
calculation and the complete primary matrices have passed independent
review. The integral-lift questions recorded below are now resolved by
`I_integral_browder_lifts.md`: all seven primary directions lift in L,
and the exact theta-zero six-space lifts by integral double suspension.
D.2.59 contains the combined proof. The earlier uncertainty statements
in Sections 3--5 are retained as the history of what the primary
calculation alone could prove; they are superseded by that actual-map
and tensor/Tor construction, not by an inference from beta1 alone.

## 1. The Eilenberg--Moore edge through degree thirteen

The three previously audited tests in
`root_degree14_independence.md` are exactly the three new primitive
directions in H14 K(F2,4):

```
(Sq3 x4)^2, (Sq2 Sq1 x4)^2, Sq6 Sq3 Sq1 x4.
```

There are no other new primitive directions: the Serre generator in
degree14 is the admissible word (6,3,1), and the two squares come from
the two degree-seven generators. On the actual fiber tests

```
r_*([v²][u⁴]), r_*([u²][w²]), r_*([w][t]),
```

their pairing matrix is

```
1 1 0
0 1 1
0 0 1.
```

This is the complete independent hand calculation in the cited root
note, not a new inference from a dimension count. Together with D56
it proves p* injective through degree14. A least-degree element of
the kernel is primitive, so this suffices for full injectivity in
that range.

In the same bounded Hopf-freeness argument as D56, the first possible
kernel degree is now15. The minimal-resolution generators in
homological degree s>0 have internal degree at least
`15+4(s-1)`, and positive Tor has total degree at least
`14+3(s-1)`. Thus the actual E edge is valid through degree13.
The Hilbert quotient, previously only a formal coefficient there,
therefore gives

```
dim H13(E;F2)=47.
```

## 2. The exact next two-bar quotient

Use u5,D6,E6,S7,R7 as in D56. The nine products in H13E are

```
u H8E  (five directions),
D S, D R, E6 S, E6 R.
```

They are independent: their reduced diagonals have independent
components in bidegrees (5,8) and (6,7). All participating low
classes are primitive, and no equal-factor square occurs here.

In the first bar construction, total degree14 has a filtration-one
quotient of dimension47-9=38, together with the three independent
filtration-two cycles

```
u|S+S|u, u|R+R|u, D|E6+E6|D.
```

No length-three term can enter this degree. Thus H14(Omega L) has
dimension41. For the next bar construction, the four length-two
terms in total degree15 have factors of degrees6 and7; their
ordered-product differentials are independent by D56, so no new
filtration-two class survives.

The products removed from H14(Omega L) are the eight ordered products
with factor degrees (6,8), (8,6), and (7,7). Their three leading
filtration-two terms are precisely the three cycles just displayed.
The five remaining independent filtration-one directions are

```
{u,S}, {u,R}, {D,E6}, xi(D), xi(E6).
```

This uses the actual homology-suspension identities of CLM III.1.4:
the difference of two reversed ordered products is the suspension
of the Browder bracket, and the square is the suspension of the
top operation. The three brackets are independent modulo the nine
Pontryagin products. Their indecomposable ordinary-Lie terms can be
distinguished respectively by the label multisets (a,a,g)/(a,a,h),
(a,a,a,c), and (a,b,f). The two top-operation terms have independent
outer restricted components xi({a,b}) and xi(f), absent from the
ordinary brackets. Thus all five are independent.

Consequently actual double homology suspension gives

```
H15 L = H13 E /
 < u H8E, D S,D R,E6 S,E6 R,
   {u,S},{u,R},{D,E6},xi(D),xi(E6) >,
dim H15 L = 47-14 = 33.
```

Every assertion here is in ordinary mod-two homology. The filtration
arguments also prove surjectivity of double suspension in degree15
without the dimension computation or the extended edge assumption,
as used separately in D58.

## 3. Exact finite primary calculation

`code/I_E2_primary_15.py` is a snapshot extension of the independently
audited degree12 engine. The only structural changes are the extra
degree, the two degree13 base generators, and the fourteen displayed
bar-kernel directions. It gives the complete actual operation
matrices once Sections 1--2 are accepted. Its output is
`code/outputs/I_L15_primary.json`.

All ambient Hopf identities, retraction/operation compatibilities,
16,449 Adem instances and the complete geometric kernel stability
checks pass. The independent Milnor converter also passes its
coassociativity and cobar checks; see
`outputs/EH5_L15_Milnor_coaction.json` and
`outputs/EH5_L15_bottom_sigma_cobar.json`.

The combined Sq_*^1,2,4 map out of H15L has rank26. Sq_*^8 is zero
by instability on the degree-seven cohomology input. Therefore
the actual positive-operation annihilator, equivalently
Ext_A^(0,15)(H*L,F2), has dimension7.

The new positive-operation class is

```
V15=Sq2 Z13=Sq4 N11=Sq6 S9.
```

It is nonzero and is the functional of the outer xi([v²]) term.
In the output it is supported on L15_32. The independently proved
identity V15=Sq1 ell14 is retained; ell is the coefficient of
{d5,x6} on H12E, with x dual to v². Thus this nonzero class is the
reduction of an integral Bockstein and annihilates every integral
homology reduction. No arbitrary mod-two primary cycle is thereby
shown to lift integrally.

## 4. The seven primary cycles and the first exact integral warning

The seven vectors are saved, with full E representatives, in
`outputs/I_L15_primary_cycles.json`. Their coordinates in the
degree15 output basis are

```
K1 = L15_05,
K2 = L15_08,
K3 = L15_06+L15_10,
K4 = L15_06+L15_12,
K5 = L15_15,
K6 = L15_06+L15_07+L15_11+L15_13+L15_18+L15_19,
K7 = L15_30.
```

A compact choice for the first two E representatives is

```
K1={a,B7},   K2={a,B3},
beta K1={u,D},   beta K2={u,E6}.
```

Here B3 and B7 are the established degree-ten primitive fiber/cover
classes; the earlier output representative of K2 differs from this
one by the killed product D R. The two displayed Bocksteins are
nonzero in E and vanish only after the double-bar quotient. The
other five chosen representatives have beta zero already in E.
These are exact first-Bockstein statements. In particular a claim
that the latter five have integral lifts would require checking
higher Bocksteins, which has not yet been done.

## 5. A rigorous restriction on the theta-detecting integral classes

The class theta15 of D50 satisfies beta_Z(theta)=b8^2. Double
cohomology suspension kills the product b8^2. Hence sigma²theta has
an integral cohomology lift on E. Since E is rationally acyclic of
finite type, H13(E;Z_(2)) is torsion, and this integral lift pairs
zero with every integral H13E class. It follows that

```
theta vanishes on im(H13(E;Z_(2)) -> H15(L;Z_(2))).
```

Thus the theta-detecting integral class from D50/D52 cannot itself
be an integral double suspension. This is compatible with, and
explains the importance of, the mod-two surjectivity in Section 2.
The actual failure of integral lifting, especially for K1 and K2
after correcting their ordered-product commutator boundaries, is
the remaining Bockstein problem. Neither the seven-dimensional
primary count nor the full-L Ext^(2,16) nonboundary certificate
determines the remaining incoming Adams d2.
