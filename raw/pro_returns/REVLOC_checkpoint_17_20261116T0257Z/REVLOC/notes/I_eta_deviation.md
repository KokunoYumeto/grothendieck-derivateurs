# The binary deviation obstructs the actual Hopf extension

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15.

Status: proved as D.2.16. Root and the axioms agent independently checked
the exact target identities, the actual-map deviation, and the complete
finite source calculation. Root also verified the nine-dimensional source
calculation by exhaustive enumeration in `code/D2_deviation_check.py`. This concerns this particular attachment only. It does
not assert that the bottom class survives arbitrary later nullification
attachments.

## 1. Statement and conventions

Let

\[
 B=K(\mathbb F_2,2),\quad X=\Sigma B,\quad Y=\Sigma^2B,
 \quad T=\Omega^2Y,\quad C_mX=\Omega^m\Sigma^mX.
\]

Let \(h_0=\eta_2\wedge\mathrm{id}_B:\Sigma^2X\to Y\), and let
\(g_0:X\to T\) be its double adjunct. The conclusion is:

> There is no ordinary pointed map \(G:C_4X\to T\) whose restriction
> along the stabilization unit \(j_4:X\to C_4X\) is \(g_0\).
> Consequently \(h_0\) does not extend to \(\Sigma^2C_4X\), or to
> \(\Sigma^2QX\), even when all choices of the preceding extensions
> are allowed.

All homology and cohomology in this note has coefficients \(\mathbb F_2\).
Write \(\beta=\operatorname{Sq}_*^1\) on homology and use ordinary
\(\operatorname{Sq}^i\) on cohomology. Cup products and tensor products
are kept distinct.

Serre's polynomial cohomology calculation gives generators

\[
 u_2,\quad v_3=\operatorname{Sq}^1u,\quad
 w_5=\operatorname{Sq}^2v,\quad
 t_9=\operatorname{Sq}^4w.
\]

In the required range,

\[
\operatorname{Sq}^1v=0,\quad \operatorname{Sq}^1w=v^2,\quad
\operatorname{Sq}^2w=0,\quad
\operatorname{Sq}^2(u^2)=v^2,\quad
\operatorname{Sq}^4(u^2)=u^4.
\]

The class \(t\) is a nonzero independent polynomial generator.
The exact primary source is Serre, *Cohomologie modulo 2 des complexes
d'Eilenberg--MacLane*, Section 2, nos.8--9, pp.203--204; the Steenrod
relations and Cartan formulas are those already audited in D.2.12.

## 2. Homology notation and input from D.2.13

Let \(a,b,c,d,e,f,x\) be the homology labels in \(\widetilde H_*B\)
dual respectively to \(u,v,u^2,w,uv,u^3,v^2\), in degrees
\(2,3,4,5,5,6,6\). Also denote their unit images in \(H_*T\) by these
letters. Write \(\xi=\xi_1\) for the top \(E_2\) operation, of degree
\(2|z|+1\), and \(\{z,z'\}\) for the degree-one Browder bracket.

Put \(C=\sigma c\in H_5X\). D.2.13 proves

\[
 g_{0*}(C)=\xi a.
 \tag{1}
\]

Its cone/Adams--Hilton proof and the degree-five primitive-kernel
argument do not assume that \(g_0\) is multiplicative.

D.2.13 also supplies the following coefficient assertion for **every**
ordinary map \(G:C_4X\to T\):

\[
 [ (\xi a)^2 ]\,G_*(C^2)=0.
 \tag{2}
\]

Here the brackets denote selection of a polynomial-basis coefficient.
For reference, in \(H_*C_4X\) the exact top Nishida formula is

\[
 \operatorname{Sq}_*^2\xi_3C=Q^6C+\lambda_3(C,\sigma a),\qquad
 \beta\operatorname{Sq}_*^2\xi_3C=C^2.
\]

The Browder term has zero Bockstein, because both inputs do. In the
target the coefficient of \((\xi a)^2\) in
\(\beta\operatorname{Sq}_*^2H_{13}T\) is zero. This gives (2) solely by
Steenrod naturality. The class \(C^2\) is the Pontryagin square in
\(H_*C_4X\).

## 3. Four exact target cohomology relations

Choose the following cohomology classes by their dual polynomial-basis
functionals:

\[
 U\in H^5T\text{ dual to }\xi a,\quad
 V\in H^7T\text{ dual to }\xi b,\quad
 W\in H^9T\text{ dual to }\xi c,
\]

\[
 L\in H^{10}T\text{ dual to }(\xi a)^2,\qquad
 L_b\in H^{14}T\text{ dual to }(\xi b)^2.
\]

The required identities are

\[
 \operatorname{Sq}^2L=UV,\qquad
 \operatorname{Sq}^4L=L_b+UW,\qquad
 \operatorname{Sq}^2L_b=0,\qquad
 \operatorname{Sq}^2\operatorname{Sq}^1L=0.
 \tag{3}
\]

The last is exactly the coefficient identity in D.2.13. Here is a
complete coefficient check for the other three.

The free \(E_2\) homology theorem gives a polynomial algebra on the
free restricted degree-one Lie basis on the labels. Top generators
\(\xi z\) all have odd degree. Steenrod images of labels remain labels;
Steenrod images of bracket expressions remain in the bracket ideal.
Moreover Steenrod operations cannot turn a positive-degree factor into
a nonzero scalar. Therefore a pure two-factor polynomial coefficient
in an even-degree Steenrod image can come only from an initial product
of two Lie generators. There is no top generator of that even input
degree.

The top Nishida formula gives

\[
 \operatorname{Sq}_*^2\xi b=\xi a,\qquad
 \operatorname{Sq}_*^2\xi c=\{c,a\},\qquad
 \operatorname{Sq}_*^4\xi c=\xi a.
 \tag{4}
\]

For the last equality, \(\beta c=0\),
\(\operatorname{Sq}_*^2c=a\), and
\(\operatorname{Sq}_*^3c=\operatorname{Sq}_*^4c=0\).
The surviving ordinary term is \(Q^3a=\xi a\); all Browder terms in
that formula vanish.

There is no degree-six Bockstein preimage of the indecomposable
\(\xi a\). The full degree-six basis is

\[
 f,x,ac,b^2,a^3,\{a,b\},
\]

with Bockstein images \(0,d+e,0,0,0,0\). There is likewise no
Bockstein preimage of the indecomposable \(\xi b\) in degree eight:
even-degree indecomposables are labels or bracket expressions, whose
Bocksteins cannot become a pure top generator, while products remain
decomposable.

It follows that the coefficient of \((\xi a)^2\) in
\(\operatorname{Sq}_*^2\) of a degree-twelve class is exactly the
coefficient of \(\xi a\cdot\xi b\) in that class. The possible
Bockstein cross terms would require a degree-six Bockstein preimage
of \(\xi a\), which does not exist. This functional is the cup
product \(UV\). Indeed the relevant reduced-coproduct coefficient
\(\xi a\otimes\xi b\) occurs precisely on the product
\(\xi a\cdot\xi b\): there is no top generator in degree twelve,
labels have only label coproducts, and bracket terms retain a bracket
in any such coproduct component. Thus the first identity in (3) is exact.

Similarly, the coefficient of \((\xi a)^2\) in
\(\operatorname{Sq}_*^4\) of a degree-fourteen class is exactly the
sum of the coefficients of \((\xi b)^2\) and
\(\xi a\cdot\xi c\). Equation (4) gives these two contributions;
the partitions \(1+3\) require the absent degree-six Bockstein
preimage. The cup product \(UW\) detects precisely the second
product coefficient. In particular, the nonprimitive coproduct of
\(\xi c\) does not create an additional \(\xi a\otimes\xi c\)
coefficient in this degree: a single generator with such a component
would have even degree fourteen, and neither a label nor a bracket
expression has that component. A product producing two indecomposable
factors must be the indicated two-factor product. This proves the
second identity.

Finally, a degree-sixteen class could have a nonzero
\((\xi b)^2\) coefficient after \(\operatorname{Sq}_*^2\) only through
a degree-nine square-operation preimage of \(\xi b\) or a degree-eight
Bockstein preimage. The latter was excluded above. The only degree-nine
pure top generator is \(\xi c\), whose square-operation image in (4)
is a bracket, not \(\xi b\). Products and the remaining generators
cannot supply an indecomposable preimage. This proves
\(\operatorname{Sq}^2L_b=0\).

These computations use Cohen--Lada--May, Chapter III, Theorems 1.2--1.4
(the top formulas on printed pp.217--218), Theorems 3.1--3.2 and
Lemma 3.8. They were checked against the original scan, including
its Browder corrections.

## 4. The deviation is an actual map from the smash product

Suppose an ordinary \(G:C_4X\to T\) restricts to \(g_0\). Let
\(\mu_4\) and \(\mu_T\) be the loop multiplications. On \(X\times X\)
consider

\[
 F=G\mu_4(j_4\times j_4),\qquad
 H=\mu_T(g_0\times g_0).
\]

They agree up to a specified pointed homotopy on \(X\vee X\).
The pointwise product of \(F\) with the pointwise inverse of \(H\)
is therefore null on that wedge. Choose the nullhomotopy. The pointed
cofiber universal property gives an actual map

\[
 \delta:X\wedge X\simeq\Sigma^2(B\wedge B)\longrightarrow T.
 \tag{5}
\]

A loop-group model can be used if strict inverses are desired; the
construction requires only the ordinary H-group structure on the
double-loop target. It does not use coherent symmetry, a factorization
through \(D_2X\), or multiplicativity of \(G\).

The class \(C\) is primitive. On the cross class \(C\otimes C\),
the homology of the pointwise difference is computed by convolution.
The two cross terms are both \((\xi a)^2\), and cancel over
\(\mathbb F_2\). The antipode fixes \(\xi a\) and its square, since
\(\xi a\) is primitive. Consequently

\[
 [ (\xi a)^2 ]\,\delta_*(C\otimes C)
 = [ (\xi a)^2 ]\,G_*(C^2)+1=1
 \tag{6}
\]

by (1)--(2). Changing the chosen nullhomotopy on the wedge does not
affect this cross-homology calculation: the cofiber quotient induces
an isomorphism on the Kunneth cross summand, and its connecting map
has zero homology there.

## 5. The finite Steenrod calculation on the smash source

Let \(z\in\widetilde H^8(B\wedge B)\) be the double desuspension of
\(\delta^*L\). By (6), its coefficient of \(u^2\otimes u^2\) is one.
Every positive cup product on \(X\wedge X\) is zero, since it is a
double suspension. Pulling back (3) therefore gives

\[
 \operatorname{Sq}^2z=0,\qquad
 \operatorname{Sq}^2\operatorname{Sq}^1z=0,\qquad
 \operatorname{Sq}^2\operatorname{Sq}^4z=0.
 \tag{7}
\]

For the last equality first pull back
\(\operatorname{Sq}^4L=L_b+UW\); the product vanishes, and then
\(\operatorname{Sq}^2L_b=0\) applies. Steenrod operations commute
with the two cohomology suspensions.

The complete degree-eight basis of \(\widetilde H^*(B\wedge B)\) is

\[
\begin{array}{lll}
 u\otimes u^3,&u\otimes v^2,&v\otimes w,\\
 v\otimes uv,&u^2\otimes u^2,&w\otimes v,\\
 uv\otimes v,&u^3\otimes u,&v^2\otimes u.
\end{array}
\]

Cartan gives

\[
 \ker(\operatorname{Sq}^2\text{ in degree }8)
 =\operatorname{span}\{z_0,z_1\},
\]

where

\[
 z_0=u^2\otimes u^2+u\otimes v^2+v^2\otimes u,
 \qquad z_1=v\otimes w+w\otimes v.
\]

For an explicit check, the coefficient of \(u\otimes u^4\) forces
the coefficient of \(u\otimes u^3\) to vanish, and symmetrically
for \(u^3\otimes u\). The unique \(w\otimes uv\) and
\(uv\otimes w\) terms force the coefficients of \(v\otimes uv\)
and \(uv\otimes v\) to vanish. The remaining square-operation
images force the three coefficients in \(z_0\) to agree and the
two in \(z_1\) to agree. Thus the asserted kernel is exact.

Moreover

\[
 \operatorname{Sq}^1z_0=\operatorname{Sq}^1z_1
      =v\otimes v^2+v^2\otimes v,
\]

and

\[
 \operatorname{Sq}^2\operatorname{Sq}^1z_0
 =\operatorname{Sq}^2\operatorname{Sq}^1z_1
 =w\otimes v^2+v^2\otimes w\ne0.
\]

The first two conditions of (7), with the required coefficient one,
therefore force

\[
 z=z_0+z_1,
 \qquad \operatorname{Sq}^1z=0.
 \tag{8}
\]

The Adem relation
\(\operatorname{Sq}^2\operatorname{Sq}^4
 =\operatorname{Sq}^6+\operatorname{Sq}^5\operatorname{Sq}^1\)
now gives

\[
 \operatorname{Sq}^2\operatorname{Sq}^4z
       =\operatorname{Sq}^6z\ne0.
\]

Indeed the coefficient of \(w\otimes t\), with
\(t=\operatorname{Sq}^4w\), is one. It comes from
\(\operatorname{Sq}^2v\otimes\operatorname{Sq}^4w\) on the term
\(v\otimes w\); none of the other four terms in (8) can contribute
that basis element. This contradicts the third condition of (7).

Thus no map (5) with coefficient (6) exists. It follows that the
assumed ordinary fourth-stage extension \(G\) does not exist.

## Scope

This proves nonextension of one explicit, stably essential and
homology-zero Hopf attachment at a finite stabilization stage. It
improves the canonical-only obstruction of D.2.13. It neither asserts
that every potentially dangerous attachment has this form nor proves
nontriviality of the full nullification \(P_{Q\Sigma B}(\Sigma^2B)\).


## Strengthening: no map can have the specified Hopf coefficient

The proof in `sections/D2_eta_nonextension.tex` establishes the stronger
statement that **every** ordinary pointed map G:C4 X -> T has zero
coefficient of xi a on G_*(C), with no prescribed restriction to X.
Indeed put g=G j4 and y=G_*(C). The latter is primitive. Form the actual
multiplication deviation of G mu4(j4 x j4) and muT(g x g) on X x X,
then descend it to X smash X by a chosen nullhomotopy on the wedge.
On C tensor C its L coefficient is

    L(G_*(C^2)) + L(y^2).

The two cross terms cancel, and the antipode fixes primitive y and y^2.
The first summand is zero by D.2.13. Since target homology is polynomial,
the second is exactly the xi a coefficient of y. If it were one, the
same finite cohomology contradiction above applies. Thus that coefficient
vanishes for every G. The eta nonextension follows from its required value
g0_*(C)=xi a. No H-map assumption, coherent symmetric deviation, or
homotopy-orbit factorization is used.

This does not by itself classify other attachment coefficients or prove
persistence after an arbitrary nullification stage. Those implications
require separate examination.
