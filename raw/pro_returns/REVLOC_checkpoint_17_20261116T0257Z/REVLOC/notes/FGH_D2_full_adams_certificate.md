# Extending the bottom-sigma certificate to the full target

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026, 02:10 UTC. Exact geometric and algebraic argument,
independently checked with the source and root agents. This proves a
nonboundary in the full target's Adams E2 term. It does **not** remove
the possible incoming Adams d2 from filtration zero.

Use `L=Y<7>`, `E=Omega^2 L`, and the classes of D.2.57:

```
a=a7, S=Sq2 a, N=Sq4 a, Z=Sq4 Sq2 a.
```

Let Phi be the eleven-term cobar-two functional in D.2.57. Its
definition can be read without choosing a full homology basis: the
six displayed algebra tensor pairs in its A row are paired with a,
the four in its S row with S, and the last pair with Z.

## 1. Exactly what the new cobar columns require

At internal degree sixteen, C2 uses homology only through degree
fourteen, and C3 only through thirteen. C1 can additionally use
degree fifteen. Every such new column is `[xi1]m`, with m in H15L.
Among the eleven supported tensor types, only

```
[xi1|xi1^8] paired with a,
[xi1|xi1^2] paired with Z
```

can occur in the differential of this column. Hence

```
Phi(d([xi1]m)) = <Sq8 a + Sq2 Z,m> = <Sq2 Z,m>.
```

The last equality is the actual instability relation `Sq8 a7=0`.
Write `V15=Sq2 Z`. Adem and the proved `Sq1 a=Sq3 a=0` give

```
V15=Sq6 Sq2 a=Sq4 Sq4 a=Sq6 S=Sq4 N.
```

No assertion that V vanishes follows from the fourteen-stage data.

## 2. An actual class ell14 and the identity V=Sq1 ell

In the free E2 homology of T, let lambda be the coefficient functional
of the ordinary two-letter Hall bracket `{d5,x6}`, where d is the
label dual to w5 and x the label dual to v3 squared. Restrict lambda
to H12E. It annihilates every generator of the D.2.56 double-suspension
kernel:

```
uS, uR, D^2, D E6, E6^2, {u,D}, {u,E6}.
```

The first five are Pontryagin products. The last two have ordinary
Lie components involving a,b,c,f and of different word length; neither
has the two-label word d,x. Thus lambda descends to an actual class
`ell14 in H14(L;F2)`.

There is an exact identity of functionals on all of H13T:

```
lambda beta = coefficient of the outer restricted generator xi(x6).
```

Indeed the top Bockstein gives

```
beta xi(x) = {x,beta x} = {x,d+e}.
```

Its d,x coefficient is one. The other degree-six restricted inputs
are f and `{a,b}`; both have zero Bockstein. Products cannot contribute
an ordinary indecomposable bracket. An ordinary Hall word of length
at least three cannot contribute a two-label word. For an ordinary
two-label bracket, a contribution to d,x would require either a label
with Bockstein x, which does not exist because Sq1(v squared)=0, or
the source bracket x,x, since x is the only label whose Bockstein
contains d. The latter bracket is zero. These exhaust the free basis.

The same outer coefficient is the double-suspension pullback of V.
Indeed Z is the coefficient functional of xi(d), and the top even
formula shows that the only restricted input contributing xi(d) to
Sq2 is xi(x), since beta x=d+e. Ordinary labels, brackets and products
cannot create such an outer restricted indecomposable.

It remains to justify that equality after double cohomology suspension
implies equality on L in degree fifteen. The following short bar
argument does this without computing all of H13E or assuming a new
Eilenberg--Moore edge isomorphism.

## 3. Double suspension is onto in homology degree fifteen

In the first bar construction `BE=Omega L`, all factors have degree
at least five. There are no length-three terms in the relevant range.
Apart from filtration one, total degree fourteen has precisely the
three length-two cycles with shuffle-leading terms

```
u|S+S|u,   u|R+R|u,   D|E6+E6|D.
```

The low products are independent as already checked in D.2.56.
These three cycles are realized by actual Pontryagin products in
Omega L. Consequently every class in H14(Omega L), modulo products,
is an actual homology suspension of a class of H13E.

In the second bar construction, total degree fifteen could additionally
have length-two terms from degree six times degree seven. Their
differential is the four ordered products

```
(sigma u)(sigma D), (sigma D)(sigma u),
(sigma u)(sigma E6), (sigma E6)(sigma u).
```

They have rank four, including the two independent lower commutator
directions proved in D.2.56. Thus this length-two kernel is zero.
There is no length-three term. It follows that

```
sigma^2 : H13E -> H15L
```

is onto. Double cohomology suspension in degree fifteen is therefore
injective. Combining this with Section 2 proves the actual identity

```
Sq2 Z13 = Sq1 ell14                              (1)
```

on L. The argument uses actual bar constructions and maps throughout.
It does not rely on the provisional full degree-fifteen matrix.

## 4. The extended full-target functional

Define Psi on the full C^(2,16)(H_*L) by adding to Phi the term

```
Psi([xi1|xi1]m14) = <ell14,m14>.
```

More precisely Psi is the sum of Phi and this last functional; the
supports are disjoint. This addition cannot affect an old incoming
column. An internal coproduct term retains its module degree, and a
coaction term decreases it. The only old column with module degree
fourteen has algebra factor xi1 squared, whose reduced coproduct is
zero; it cannot yield the required first factor xi1. Columns of lower
module degree cannot reach degree fourteen.

On each new `[xi1]m15` column, the added term evaluates to
`<Sq1 ell,m15>`, exactly cancelling the old value `<Sq2 Z,m15>`
by (1). Thus Psi annihilates **every** incoming cobar-one column for
the full target. No module degree beyond fifteen can occur in C1.
The original bottom cycle `[xi1|xi1^8]a7` is still paired to one.
Therefore

```
image(h0 h3) is nonzero in Ext_A^(2,16)(H^*L,F2).   (2)
```

This is a full-target E2 nonboundary, not merely a truncated-module
calculation. The conclusion requires neither the full H15 dimension
nor a choice of a basis in that group.

## 5. Exact remaining Adams ambiguity

Naturality from the permanent sphere class still prevents the class
in (2) from supporting an outgoing differential. For the full target,
however, the possible incoming differential

```
d2 : Ext_A^(0,15)(H^*L,F2) -> Ext_A^(2,16)(H^*L,F2)
```

is no longer excluded by dimension. All higher incoming sources have
negative filtration. Thus this one Adams d2 is the remaining
permanence question for this particular bottom detector. No vanishing
of it, no stable Hurewicz realization of the half-product class, and
no value of the actual h is claimed here.

Equation (1) also implies that V pairs to zero on every reduction of
an integral H15 class, since it is the reduction of the integral
Bockstein of ell. This is compatible with the possible filtration-zero
source above; it is not a computation of its secondary differential.

The existing note `root_degree14_independence.md` supplies independent
degree-fourteen base tests for a complete E13 edge calculation. Those
tests can support a full numerical H15 table, but the proof of
(1)--(2) intentionally does not need that additional enumeration.
