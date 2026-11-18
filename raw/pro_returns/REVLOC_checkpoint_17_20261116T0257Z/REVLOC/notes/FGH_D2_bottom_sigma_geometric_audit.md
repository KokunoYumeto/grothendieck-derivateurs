# Independent audit of the bottom-sigma Adams detector

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. **Complete independent audit: PASS.**

This note audits the actual topological input, the small algebraic
certificate, and the finite-skeleton Adams implication. It does not
evaluate the later incoming eighth differential or the full-target
class `h`. The complete operation engine remains an independent check;
the decisive proof uses only four cohomology classes and thirteen
cobar-one columns.

## 1. Actual retraction, not a formal Hopf quotient

Write `T=Omega^2 Sigma^2 B`, with `B=K(F2,2)`, and let
`q:T->B` be the double-loop map with its unit section `j:B->T`.
The fiber is F. Translation in the actual loop-group model gives

```
r(t)=t (j q(t))^(-1),
r_*(x)=sum x' S_T(j_*q_*x''),   Delta(x)=sum x' tensor x''.
```

Here `S_T` is the antipode in the homology of T. The section is not an
H-map, so replacing this by `j_* S_B` would be wrong. The recursion used
in `I_E2_primary.py` is exactly the connected-Hopf antipode recursion
on the image of each label. The map r takes values in the actual fiber
and restricts to the identity there; its image is therefore precisely
the included homology of F. No preservation of Pontryagin products by
r is assumed.

The code's other input, that q kills restricted generators through
degree twelve, has a direct range proof. It kills Browder brackets
because its target is an infinite loop space. By the diagonal formula,
the images of the relevant restricted generators are primitive once
the lower cases have vanished. Primitive homology of B in this range
occurs only in degrees 2, 3, 5, 9. The possible degree-five image of
`xi a` is excluded by `Sq2_* xi a=0`, since the primitive label d5 has
`Sq2_* d=b`. The possible degree-nine image of `xi c` is excluded by
`Sq4_* xi c=xi a`, since the primitive label t9 has `Sq4_* t=d`.
The degree-seven and degree-eleven images have no primitive targets.
The iterated restriction of `xi a` vanishes by naturality. These are
all restricted generators needed through twelve. This is a range
argument, not a claim that all Dyer--Lashof operations on B vanish.

Products of labels map by the divided-power multiplication in H_*B,
dual to the primitiveness of its polynomial Serre cohomology generators.
Thus the binary-carry test in `q_monomial` is also exact.

## 2. The cover edge and its implemented contractions

For `p:F->K(F2,4)`, the bottom cohomology functional is dual to the
fiber class `a^2`. Its Steenrod descendants give all polynomial base
generators through degree twelve. Their admissible operation lists are

```
(), (1), (2), (3), (2,1), (3,1), (4,1), (4,2),
(5,2), (4,2,1), (5,2,1).
```

For such a base generator f and an arbitrary cohomology class g of F,

```
<p*(f) g,z> = <p*(f) tensor g, Delta_F z>.
```

Consequently simultaneous vanishing of the left contractions by these
generators is precisely annihilation of the whole ideal
`p*(H^+ K(F2,4)) H^*F`. Products of base generators require no additional
test: one factor is already among the generators, and the other factors
are absorbed into g. The ambient extension of each functional by r is
legitimate, because the diagonal of an actual fiber class lies in
H_*F tensor H_*F. D.2.56 identifies this annihilator with the actual
image of H_*E through twelve. It is stronger than merely taking the
kernel of p_*.

The bounded Hopf-freeness argument and all degree-thirteen primitive
tests in D.2.56 were independently read. They justify the edge in this
range without global injectivity of p* or an unproved collapse of the
entire Eilenberg--Moore sequence.

## 3. Exact CLM formulas and the two bar quotients

The author scan of Cohen--Lada--May, Chapter III, printed pp.217--218,
was reopened visually in this audit. The internal Cartan term is
`xy{x,y}`. With `xi=xi_1`, the top Nishida relation specializes to

```
Sq_*^(2k) xi(x) = xi(Sq_*^k x)
                 + sum_(i<j, i+j=2k) {Sq_*^i x,Sq_*^j x},
Sq_*^(2k+1) xi(x) = (|x| mod2)(Sq_*^k x)^2
                 + sum_(i<j, i+j=2k+1) {Sq_*^i x,Sq_*^j x}.
```

Indeed, in the ordinary term of the printed formula only excess one
or zero can remain in an E2 space: these are the top restriction and
the Pontryagin square. Their coefficients are respectively one and
`|x| mod2`. The displayed nonlinear partitions are exactly the distinct
pairs `i<j`. This verifies the engine's formulas, including the parity
factor, rather than inferring them from its Adem checks.

The actual double-suspension kernels used in the code are

```
E degree10: <u^2>,
E degree11: <uD,uE6,xi u>,
E degree12: <uS,uR,D^2,D E6,E6^2,{u,D},{u,E6}>.
```

For the first bar, E has no positive homology below five, so length
three begins in total degree eighteen. The only extra length-two
cycles relevant here are `u|D+D|u` and `u|E6+E6|u`. For the second bar,
Omega L has no positive homology below six, and length three begins
in degree twenty-one. Its four ordered degree-thirteen products have
rank four: two shuffle-leading directions and the two distinct lower
commutators `sigma{u,D}` and `sigma{u,E6}`. The latter must not be
discarded by treating Omega L as E2. They are independent modulo the
five products in E degree twelve. Thus the corrected degree-fourteen
dimension is 25, and the implementation uses precisely the actual
quotient. No higher bar differential can enter these degrees.

## 4. Hand identification of the four-class submodule

The full proof in `I_L14_primary_matrices.md`, Section 5, was checked
independently. The cyclic cohomology module through fourteen has basis

```
a7, S9=Sq2 a7, N11=Sq4 a7, Z13=Sq4 Sq2 a7.
```

Under injective double cohomology suspension these are the coefficient
functionals of the outer restricted generators `xi a`, `xi b`,
`xi c`, `xi d`, respectively. Odd homology squares cannot contribute
such a coefficient: the odd top formula gives only products and
brackets; a bracket of restricted words reduces, by the restricted
adjoint identity, to ordinary Lie words. Label and product Cartan laws
likewise cannot create an outer restricted indecomposable.

Thus all four first squares vanish. Adem gives `Sq2 S=0`; also
`Sq2 N=Sq6 a+Sq5 Sq1 a=0`. For the direct last check, no degree-five
restricted input has third homology square equal to the label a.
All remaining square-power generator actions in the range are zero
except the three defining arrows. This proves closure as an actual
Steenrod submodule, not just equality of dimensions.

The nonzero witness for Z is

```
w11=xi d + ([u_B t_B]+a[t_B]) + P_(4v),
```

where `P_(4v)` is the coefficient of `u_B^4 v_B` in the logarithmic
derivative of the group-like label series with respect to v_B.
All three terms are primitive fiber classes. Their pairings with the
two degree-eleven polynomial base generators
`Sq5 Sq2 x4, Sq4 Sq2 Sq1 x4` are, in order,

```
(1,0), (0,1), (1,1).
```

For example, `Sq5_* xi d=b^2` and `Sq2_* b^2=a^2` give the first
entry. `Sq4_* xi d=xi b`, followed by Sq2 and Sq1, gives zero for
its second entry. Cartan gives `Sq4_* Z11=Q` and
`Sq4_* P_(4v)=P`. The Newton class's fifth square is the primitive
polynomial class with leading label f, whose second square is a^2.
These give the other two vectors. Their sum is zero; primitivity
annihilates the decomposable base ideal as well. The exact edge places
w11 in E, and `Sq4_* w11=S`, `Sq2_* S=u`. Its double suspension
therefore detects Z13 nontrivially.

## 5. Independent thirteen-column check

Dualizing this four-class inclusion gives the left comodule N with

```
psi_red(s)=xi1^2 tensor a,
psi_red(n)=xi1^4 tensor a,
psi_red(z)=xi1^4 tensor s+xi2^2 tensor a.
```

The eleven-term functional in `EH5_bottom_sigma_four_class.md` was
checked by multiplying the Milnor coproducts, independently of the
row-reduction code. On the thirteen incoming columns, the numbers
of supported terms are exactly

```
a columns: 2,2,2,2,2;
s columns: 2,2,2,4;
n columns: 0,0;
z columns: 0,2.
```

All are even, while the functional takes value one on
`[xi1|xi1^8] a`. That element is a cycle because both algebra factors
are primitive and a has zero reduced coaction. This proves it is not
a boundary in the complete small complex. Naturality of the quotient
then proves that the antecedent bottom class in the actual skeleton's
cobar complex is not a boundary either.

## 6. Finite-skeleton interface and Adams permanence

There is also a formulation avoiding any separate minimal stable-CW
existence theorem. Choose an ordinary finite fourteen-skeleton P14
of the existing finite-type CW model of L, retaining its bottom sphere.
Restriction from L is an isomorphism in cohomology through degree
thirteen and injective in degree fourteen. Hence the four-class
submodule above injects into H^*(P14). Operations landing above
fourteen are zero on this skeleton. Dualizing yields the required
actual comodule quotient H_*(P14)->N, even if P14 has additional
degree-fourteen homology. One does not need to identify its entire
comodule with the truncation of H_*L.

The sphere element 2sigma is detected by h0h3 in filtration two.
Its image is the nonboundary class just proved. Inductively it cannot
support an Adams differential, by naturality from the permanent sphere
class. It cannot be hit: the only possible incoming differential is
d2 from Ext^(0,15), zero since H15(P14)=0; all later potential sources
have negative filtration. Finite-spectrum convergence therefore makes
the stable image of 2alpha-sigma nonzero in P14.

D.2.55 has already identified the bottom surviving group through the
twelve-stage as Z4. Every nonzero subgroup of Z4 contains its doubled
generator. Its survival through the fourteen-stage proves that both
incoming stable AHSS differentials d6 and d7 are zero. Thus the
bottom term on the eighth page remains exactly Z4. This conclusion
does not determine the source-changing eighth differential, the
stable half-product pairing, or the actual full-target class h.

Source interface: the exact primary CLM scans used here are the
already excluded local images of printed pp.217--218, from
<https://www.math.uchicago.edu/~may/BOOKS/homo_iter.pdf>.
The Milnor coproduct and the sphere Adams detector are the primary
interfaces recorded by the root and fibrations agents in their
corresponding source audits. The thirteen-column algebra above is
fully reproduced in the authored certificate note.
