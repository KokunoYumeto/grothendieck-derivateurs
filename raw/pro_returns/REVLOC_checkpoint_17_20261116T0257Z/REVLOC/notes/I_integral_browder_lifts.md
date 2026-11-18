# Actual normalized Browder maps and integral lifts of the seven sources

**Status, 2026-11-16, 02:49 UTC.** Root has independently passed the
actual normalized map, all prescribed integral chains, and the six image
formulas, and reran the complete finite source script. The core result
is formalized as D.2.59 in `sections/D2_integral_primary_sources.tex`. The raw Browder operation
on nonprimitive homology labels is deliberately not used as the map
formula.

## 1. The actual reduced map

Let T=Omega²Y, with a loop-group model and its E2 structure. The
fundamental circle of the binary E2 operation gives a loop of maps
T x T -> T, based at the multiplication mu. Translate this loop to
the identity map by multiplying pointwise by mu inverse. More explicitly,
work in a topological-group model of T and adjust the basepoint binary
operation to its multiplication. On either axis the circle of operations
is a loop of unary operations, and the unary little-cubes space is
contractible. Its based contraction, followed by the homotopy extension
property for the wedge inclusion, makes the translated map constant on
the wedge without changing its homology. It is also constant at the
circle basepoint. Thus it factors through the actual reduced map

```
N : Sigma(T smash T) -> T.
```

Equivalently it is the double adjoint of the generalized Whitehead
product of the two evaluation maps Sigma²T->Y. This description
supplies an ordinary based map, independently of an operad model.
The defining circle action on homology is the CLM Browder operation.
The diagonal and group inverse give its reduced-map formula

```
N_*(x tensor y) = sum {x',y'} S_T(x'' y''),
Delta x=sum x' tensor x'', Delta y=sum y' tensor y''.
```

This follows directly by applying homology to the circle action
times mu inverse: the inverse factor is independent of the circle,
so only the summand with the circle fundamental class in the action
factor contributes. The antipode is that of T, not that of B.
For primitive inputs this is the usual Browder bracket. For a label
c with reduced diagonal a tensor a it is, for primitive y,
`N(c,y)={c,y}+a{a,y}`. These corrections are essential.

Apply the map to j:B->T and E->T, or to two copies of j. The sources
Sigma(B smash E) and Sigma(B smash B) are respectively seven- and
four-connected. Since E is the four-connected cover of T, both maps
have unique based lifts to E. Double suspension followed by the
counit therefore gives actual maps

```
Sigma³(B smash E) -> L,
Sigma³(B smash B) -> L.
```

Every integral source cycle maps to an integral double suspension.
By Section 5 of `I_cover_fifteen.md`, theta vanishes on every such
image.

## 2. The exact low integral inputs

Keep all labels and cover classes from D18--D22. The following
mod-two classes are reductions of integral cycles:

* In B: a2 of order2, c4 of order4, d5+e5 of order2, and h7.
  For the last, beta of the label [v_B w_B] in degree8 is h7,
  so h7 is the reduction of its integral Bockstein and has an
  order-two representative.
* In E: J1,J2 in degree8; and P_r, B2, B1+B3, B5+B6 in degree10.

Here is the exact justification of the E assertion. H7(E;Z)=Z2,
so every degree-eight first-Bockstein cycle lifts integrally: the
integral connecting image has order two and reduction is injective
on H7. For degree ten, the proved group is
`H9(E;Z)=Z8{N'} plus (Z2)^3`. A beta1-zero class can have integral
connecting image only 0 or 4N'. Its third homological Bockstein
is nonzero exactly in the latter case. The complete D22 table gives
beta3 B5=beta3 B6=N and zero on P_r,B2,B1+B3. Thus the displayed
four degree-ten combinations have zero integral connecting image.
No general beta1-to-integral-lift inference is being made.

Choose integral chains and cycles with the following literal
boundaries (signs can be changed by orienting a top chain):

```
in B: d b~=2 a~,   d d~=4 c~,   d l~=2 h~;
in E: d B5~=8 N~,  d B4~=2 Ksum~.
```

Their reductions are respectively b,d,[v_Bw_B],B5,B4. The first
two follow from the established bottom Moore and second-Bockstein
classes. The third is the definition of the integral Bockstein of
the degree-eight label. The last two are precisely the established
third and first Bockstein statements; Ksum=K2+K3+K4 in degree9.
Changing an integral representative or a nullchain adds integral
tensor cycles, which are retained in the constructions below.

## 3. Three explicit Tor cycles

The following are actual integral cycles in the indicated smash
product chain complexes; their mod-two reductions are as stated:

```
tau(a,N) = 4 b~ tensor N~ - a~ tensor B5~,
    reduction a tensor B5 in B smash E;

tau(a,Ksum) = b~ tensor Ksum~ - a~ tensor B4~,
    reduction b tensor Ksum + a tensor B4 in B smash E;

tau(c,h) = d~ tensor h~ - 2 c~ tensor l~,
    reduction d tensor h in B smash B.
```

The boundaries cancel literally: 8aN-8aN, 2aKsum-2aKsum,
and 4ch-4ch. The displayed degrees of the first factors are even
where needed, so these signs agree with the tensor differential.
These chains prove the required lifts; a Kunneth splitting or an
abstract existence of a Tor summand is not being substituted for
the prescribed mod-two coordinate.

## 4. Six exact image formulas

Let K1,...,K7 be the primary basis in `I_cover_fifteen.md` and
`outputs/I_L15_primary_cycles.json`. All expressions in the next
table are source mod-two reductions of the indicated integral
tensor/Tor cycles. Applying the actual lifted N and then double
homology suspension gives:

| Integral source | Image |
|---|---|
| a tensor P_r | K5 |
| a tensor (B1+B3+B2) | K1+K2 |
| a tensor B2 + c tensor J2 | K4 |
| a tensor (B2+B5+B6) + tau(a,N) | K3 |
| a tensor B2 + c tensor J1 + tau(a,Ksum) | K6 |
| (d+e) tensor h + tau(c,h) | K7 |

The first five rows use B smash E and the last uses B smash B.
For the fourth row, its reduction simplifies to a tensor (B2+B6).
For the last row, it simplifies to e tensor h; this reduction need
not itself be a tensor product of integral cycles.

Here are useful individual coordinate identities that completely
fix the table relative to the saved L15 basis:

```
N(a,P_r)=L15_15;
N(a,B2)=L15_06;
N(a,B1+B3)=L15_05+L15_06+L15_08;
N(a,B5+B6)=L15_09+L15_10;
N(a,B5)=L15_09;
N(c,J1)=L15_11; N(c,J2)=L15_12;
N(b,Ksum)+N(a,B4)=L15_07+L15_13+L15_18+L15_19;
N(d+e,h)=L15_28+L15_30;
N(d,h)=L15_28.
```

Each equality is obtained by the stated coproduct/antipode formula
and the fourteen explicit double-bar relations of
`I_cover_fifteen.md`. The exact calculation is
`code/I_integral_browder_sources.py`; it checks membership in the
actual E edge before taking the quotient, so no nonexistent fiber
class is used. The six image directions are independent by their
displayed coordinates.

## 5. All seven lift, and theta is now normalized on the source space

The six-dimensional subspace

```
U=<K1+K2,K3,K4,K5,K6,K7>
```

therefore consists of reductions of integral double suspensions,
and theta vanishes on it. D52 supplies an integral primary class
omega with theta(omega)=1. Its reduction lies in the seven-dimensional
primary space and is outside U. Consequently the reductions of
integral H15(L;Z_(2)) contain the entire primary space. In this basis
the exact theta values are

```
theta(K1)=theta(K2)=1,
theta(K3)=...=theta(K7)=0.
```

This determines which primary classes lift integrally: all seven do.
It does not assert that K1 or K2 lifts to an integral class of E;
indeed neither can be an integral double suspension, because theta
evaluates to one on each. Their lift in L follows by combining the
known omega with the six explicitly constructed integral classes.

## 6. Source primitivity for possible Adams naturality

Integral lift alone is insufficient for an Adams Ext0 source.
This additional question was checked separately. In
H12(B smash E;F2), the integral-reduction subspace has dimension22
(15 tensor directions and seven explicit Tor directions). Its
positive-Steenrod annihilator has dimension13, and its image under
the lifted N spans exactly

```
<K1+K2,K3,K4,K5,K6>.
```

For example a tensor (B2+B6) is primary on the source, using
Sq2 B2=Sq2 B6=J2 and the other required vanishings. The full exact
source Cartan check and all preimages are in
`outputs/I_browder_source_lifts.json`.

For B smash B the corresponding source computation has dimension19
of integral reductions and four primary directions; its image is
only <K5>. In particular the last row giving K7 is not primary on
that source. See `outputs/I_BB_integral_source_lifts.json`.
This limitation is retained and is not replaced by a claim that
every integral source cycle is a primary cycle. The separate
universal-secondary argument is responsible for any further
Adams conclusion.
