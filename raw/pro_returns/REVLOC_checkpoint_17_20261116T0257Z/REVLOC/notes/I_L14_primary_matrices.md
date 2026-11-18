# Exact primary matrices through degree fourteen

**Status, 2026-11-16 01:56 UTC.** The full finite model and output are saved
in `code/I_E2_primary.py` and `code/outputs/I_L14_primary.json`.
The independent Milnor-conversion/cobar engine of the fibrations agent
passes its pairing, coassociativity and differential-square checks, and
finds the bottom `h0 h3` class nonboundary.  The topological input is under
final independent audit; this note does not yet promote the Adams
consequence to a numbered statement.

## 1. Ambient algebra and operations

Let `T=Omega^2 Sigma^2 B`, `B=K(F2,2)`. Through degree twelve, the Serre
cohomology algebra of B uses only u2,v3,w5,t9. The label [m] denotes the
homology class dual to the indicated cohomology monomial. Its diagonal is
the sum of all monomial factorizations of m. Homology Steenrod operations
on labels are dual to Cartan and

```
Sq1 u=v, Sq2 u=u^2;
Sq2 v=w, Sq3 v=v^2;
Sq1 w=v^2, Sq4 w=t, Sq5 w=w^2;
Sq1 t=w^2.
```

Only these values can contribute in the stated range.

The free E2 homology theorem identifies H*T with the commutative
Pontryagin polynomial algebra on the free restricted Lie algebra on
the degree-shifted positive label space. Ordinary Lyndon brackets are
expanded in the free associative algebra; restricted powers are squares
in that associative algebra. The external Pontryagin product is kept
separate. This prevents confusing a restricted square with a Pontryagin
square. The bracket has degree one, and `xi(x)` has degree `2|x|+1`.

The exact characteristic-two CLM formulas used are

```
{xy,z}=x{y,z}+{x,z}y;
xi(x+y)=xi(x)+xi(y)+{x,y};
xi(xy)=xi(x)y^2+x^2xi(y)+xy{x,y};
Sq_*^r{x,y}=sum_{i+j=r}{Sq_*^i x,Sq_*^j y};
Sq_*^(2k)xi(x)=xi(Sq_*^k x)
                 +sum_{i<j,i+j=2k}{Sq_*^i x,Sq_*^j x};
Sq_*^(2k+1)xi(x)=(|x| mod2)(Sq_*^k x)^2
                 +sum_{i<j,i+j=2k+1}{Sq_*^i x,Sq_*^j x}.
```

These are the p=2, n=1 specializations of CLM, Chapter III,
Theorems 1.2 and 1.3. The original scan was reopened and rendered at
printed pp.216--219, especially the internal Cartan formula on p.217
and the explicit Bockstein formula on p.218. The coproduct uses the
external Cartan formula

```
xi(x tensor y)=xi(x) tensor y^2+x^2 tensor xi(y),
```

together with the additive bracket correction. The tensor bracket is
`{x tensor y,z tensor w}={x,z} tensor yw+xz tensor {y,w}`.

## 2. The actual fiber projection

The map q:T->B is an E2 map and has the unit section j:B->T.
It sends labels to the corresponding B homology labels and sends every
bracket to zero. It also sends all positive restricted-power generators
through degree twelve to zero. Indeed their diagonals, by induction and
the divided-power multiplication in H*B, show that each image is
primitive. Primitive H*B occurs here only in degrees2,3,5,9. The degree5
class xi[u] has zero second homology square, whereas the unique primitive
degree5 B class has second square [v], so its image is zero. The only
further possible case is xi[u^2] in degree9. Its fourth homology square is xi[u],
whereas the unique primitive degree9 B class has fourth square [w],
so this image is also zero. All remaining cases have no primitive B
class in their degree. Thus q on a Pontryagin monomial of labels is the
usual divided-power product, and a nonlinear Lie factor makes it zero.

Use the actual T group inverse to retract onto the fiber F:

```
r_*(x)=sum x' S_T(j_*q_*x''),  Delta(x)=sum x' tensor x''.
```

The antipode here is the antipode in H*T. It is **not** j applied to the
antipode in H*B, because the section j is not an H-map. Its value on a
label is computed recursively from the label diagonal. The image of r
is H*F under the actual product splitting T~=B x F. The code checks
r^2=r and compatibility with every homology Sq in the required range.

## 3. The actual E edge, then the two bar quotients

For p:F->K(F2,4), the bottom cohomology functional is dual to a^2 in
H4F. The images of all polynomial Serre generators of the base through
degree twelve are obtained by composing that functional with the
homology Steenrod operations. A vector z in H_nF belongs to H_nE
precisely when contraction of Delta(z) by each such positive base
generator is zero. This is exactly the dual of annihilating the ideal
`p*(H^+K(F2,4)) H*F`, not merely the kernel of the base homology map.
D.2.56 proves that this quotient is the actual E edge through degree12.

The resulting ambient/fiber/cover dimensions agree with the separately
proved Hilbert series:

```
degree: 0 1 2 3 4 5 6 7 8 9 10 11 12
T:      1 0 1 1 2 4 6 9 16 26 42 69 112
F:      1 0 0 0 1 2 3 4 7 11 18 30 49
E:      1 0 0 0 0 1 2 2 5 8 12 20 32
```

The actual double-suspension quotient is unchanged below E degree10.
In degrees10,11,12 its kernels are respectively

```
<u^2>,
<uD,uE6,xi(u)>,
<uS,uR,D^2,D E6,E6^2,{u,D},{u,E6}>.
```

Here the notation is that of D.2.56. The last two bracket directions
are essential: Omega L is only E1, so reversing its two products adds
those independent Browder terms. Quotienting gives L dimensions
`1,2,2,5,8,11,17,25` in degrees7,...,14. The output lists an explicit
ambient E representative of every basis vector, so no implicit choice
of a high-degree class enters the matrices.

## 4. Exact checks and independent conversion

The program checks all ambient coproducts for coassociativity; all
Steenrod/coproduct compatibilities; all retraction/Steenrod
compatibilities; 8,973 instances of the Adem relations; and stability
of every displayed bar-kernel generator under the operations. All
checks pass. The output has 71 classes and matrices for Sq_*^1,2,4.
Sq_*^8 has zero image in this range because the target has no positive
homology below degree7.

The independent engine `EH5_bottom_sigma_cobar.py` converts these
matrices to the **left** Milnor coaction, with standard coproduct
`Delta xi_n=sum xi_(n-i)^(2^i) tensor xi_i`. It checks redundant
Steenrod words, the full coaction identity and the normalized-cobar
differential square. Its certificate is
`outputs/EH5_L14_bottom_sigma_cobar.json`, with converted coaction
`outputs/EH5_L14_Milnor_coaction.json`. The conditional output is
that the bottom class representing h0 h3 is nonboundary in
Ext^(2,16), whose dimension is18. The finite calculation alone does
not assert the final stable-homotopy consequence; the actual input
and Adams permanence interfaces require the independent audit.

## 5. A four-dimensional cyclic submodule: hand proof

The full matrices are not needed for the decisive Ext class. Let a7 be
the bottom cohomology class of L. Through degree14 its Steenrod cyclic
submodule has the four nonzero basis elements

```
a7,
S9=Sq2 a7,
N11=Sq4 a7,
Z13=Sq4 Sq2 a7.
```

Their only nonzero positive operations in this range are the three
displayed defining ones. Here is a direct topological verification.

Under the injective cohomology double-suspension map, a7 is the dual
functional of the outer restricted generator xi(a2) in H5E. The
functionals S9,N11,Z13 detect, respectively, the outer generators
xi(b3), xi(c4), xi(d5), where d is the label dual to w5. The even
Nishida formulas give these identifications: the only relevant linear
label squares are Sq1 b=a, Sq2 c=a, and Sq2 d=b. The other possible
degree-five inputs are the label e5 and xi(a2); their second squares
are zero. Thus no additional outer generator contributes to Z13.

All odd homology squares of a free E2 basis class have zero coefficient
on any outer restricted generator. For a restricted generator, the
odd top Nishida formula consists of Pontryagin products and brackets.
The brackets of restricted Lie words are ordinary Lie words, by the
restricted adjoint identity; they have no restricted-power component.
For a label, ordinary Hall word, or Pontryagin product, the same
statement follows respectively from label naturality, bracket Cartan,
or product Cartan. Consequently Sq1 of a7,S9,N11,Z13 is zero.

Adem gives Sq2 S9=Sq3 Sq1 a7=0 and
Sq2 N11=Sq6 a7+Sq5 Sq1 a7=0. The last vanishing also follows directly
from the even top Nishida formula, since no degree-five input has a
third homology square equal to a2; alternatively it is the already
proved degree13 double-suspension/instability lemma. Every other
operation through degree14 is zero by Adem, the preceding odd-square
vanishings, or instability.

The first three classes are nonzero by the established low E tables.
For the last, define the primitive Newton class P_(4v) to be the
coefficient of u_B^4 v_B in
`G^{-1} v_B (partial G/partial v_B)`. Put

```
w11=xi(d5)+Z11+P_(4v),     Z11=[u_B t_B]+a[t_B].
```

All three summands are primitive fiber classes. The only polynomial
base generators in cohomology degree11 are x11=Sq5 Sq2 x4 and
y11=Sq4 Sq2 Sq1 x4. Their pairing vectors on the three summands are
respectively (1,0), (0,1), and (1,1). The last pair follows from
`beta P_(4v)=P_p` and `Sq4_* P_(4v)=P`, using the already established
degree-ten Newton class P_p and degree-seven class P. Thus w11
annihilates both degree-eleven base generators. Primitivity annihilates
every positive cohomology product, so the exact D56 edge places w11
in H11E. Finally

```
Sq4_* w11=xi(b3)+P+Q=S,
Sq2_* S=xi(a2).
```

It follows that Z13 pairs one with the actual double suspension of
w11. In the full output this witness is exactly L13_15.

The dual four-dimensional quotient comodule therefore has reduced
left coaction

```
psi(s9)=xi1^2 tensor a7,
psi(n11)=xi1^4 tensor a7,
psi(z13)=xi1^4 tensor s9+xi2^2 tensor a7.
```

This small quotient already detects the bottom h0 h3 Ext class by the
independent eleven-term functional certificate. Its existence is now
justified without relying on the full high-dimensional operation
enumeration. The full matrices remain useful for independent checks
and later calculations.
