# The four-connected cover: homology through degree ten

**Status, 2026-11-15: Sections 1--3 independently audited and passed by
the root and the source agent; the exact order-eight comparison in
Section 4 has also passed the root audit.** Put
\(E=F\langle5\rangle=\operatorname{fib}(p:F\to K(\mathbb F_2,4))\),
where \(p\) represents the fundamental class dual to \(A=a^2\in H_4F\).
The claim below concerns the actual cover and its ordinary mod-two homology.
The proof uses an explicit low-degree Koszul calculation, not the insufficient
claim that injectivity on base cohomology alone collapses the Serre sequence.

The notation for \(F\) is that of D.2.20 and `FGH_D2_H10_fiber.md`.
All undecorated homology and cohomology in Sections 1--4 has coefficients
\(\mathbb F_2\). A superscript star denotes a dual basis vector.

## 1. The base map through degree eleven

Write \(x\in H^4K(\mathbb F_2,4)\). Its polynomial generators through
degree eleven are

\[
x_4=x,\ x_5=Sq^1x,\ x_6=Sq^2x,
\ x_7=Sq^3x,\ y_7=Sq^2Sq^1x,
\ x_8=Sq^3Sq^1x,
\ x_9=Sq^4Sq^1x,
\ x_{10}=Sq^4Sq^2x,
\ x_{11}=Sq^5Sq^2x,\ y_{11}=Sq^4Sq^2Sq^1x.
\]

The images through degree ten are exactly

\[
\begin{array}{c|l}
x_4&A^*\\
x_5&z^*\\
x_6&d_6^*+e_6^*+f_6^*\\
x_7&V^*+P^*\\
y_7&P^*+Q^*\\
x_8&L^*+M^*\\
x_9&P_n^*+P_o^*\\
x_{10}&D_2^*+Q_{10}^*+P_p^*.
\end{array}
\]

The base monomials not listed separately are
\(x_4^2\) in degree eight, \(x_4x_5\) in degree nine, and
\(x_4x_6,x_5^2\) in degree ten. Their images are detected by
\(C\), \(Z_A\), \(D_A,E_A,F_A\), and \(Q_{10}\), respectively.

For the two new degree-eleven generators, two actual primitive fiber
homology classes suffice. Let \(t\in H_9B\) be dual to \(Sq^4w_B\),
and let \(v_{11}\in H_{11}B\) be the label dual to
\(u_BSq^4w_B\). Put

\[
T_{11}=\xi d,\qquad Z_{11}=v_{11}+at.
\]

Both are primitive: \(d\) is a primitive label and
\(\overline\Delta v_{11}=a\otimes t+t\otimes a\).
Both have zero base image because \(H_{11}B\) has no primitive.
The exact operation values are

\[
\beta T_{11}=D_2,\quad Sq_*^4T_{11}=V,
\qquad \beta Z_{11}=0,\quad Sq_*^4Z_{11}=Q.
\]

For the first pair use the CLM top Bockstein formula and top Nishida
formula; \(\beta d=0\), \(Sq_*^2d=b\), and the only surviving
fourth-square term is \(Q^4b=\xi b\). For the second pair use label
Cartan: \(Sq_*^4v_{11}=h\) and \(Sq_*^4t=d\).
Consequently \((x_{11},y_{11})\) evaluate on
\((T_{11},Z_{11})\) as the identity matrix, since
\(x_{11}=Sq^1x_{10}\) and \(y_{11}=Sq^4y_7\).

The remaining degree-eleven base monomials are
\(x_4x_7,x_4y_7,x_5x_6\). They are independently detected by
products \(A\cdot H_7F\) and \(z\cdot H_6F\); every positive
cohomology product vanishes on the two primitive test classes above.
This proves injectivity of \(p^*\) through degree eleven, but the next
section supplies the additional module calculation actually needed.

## 2. Explicit Koszul vanishing, including all low mixed terms

The cohomological Eilenberg--Moore sequence for the simply connected base
has

\[
E_2=\operatorname{Tor}_{H^*K(\mathbb F_2,4)}(H^*F,\mathbb F_2)
\Longrightarrow H^*E.
\]

Use the polynomial Koszul resolution. A generator associated to a base
generator of degree \(j\) has total degree \(j-1\) and its differential
is the corresponding displayed image under \(p^*\). The smallest three
Koszul degrees are \(3,4,5\). Therefore length at least three starts in
total degree twelve. In length two, a positive \(H^*F\)-coefficient
starts in total degree eleven. Thus every length-two term of degree at
most ten has scalar coefficient, and every length-one coefficient has
degree at most seven.

Here is the full rank check for length one. In degrees three through six
the scalar generator images are independent. In degrees seven through
ten the dimensions of the length-one chain groups, of their differential
images, and of the incoming length-two boundaries are respectively

\[
\begin{array}{c|ccc}
\text{total degree}&\dim K_1&\operatorname{rank}(d:K_1\to K_0)
 &\operatorname{rank}(d:K_2\to K_1)\\\hline
7&2&2&0\\
8&4&3&1\\
9&7&6&1\\
10&13&10&3.
\end{array}
\]

For degree seven the images are \(A^{*2}=C^*\) and \(L^*+M^*\).
In degree eight, \(A^*H^5F\) has rank two, while the scalar
\(x_9\)-image is independent; the sole relation is the Koszul
commutativity relation for \(x_4,x_5\).
In degree nine, \(A^*H^6F\) has rank three and
\(z^*H^5F\) has rank two, with disjoint images. The scalar
\(x_{10}\)-image adds one rank, detected on primitive \(D_2\).
The sole relation is the commutativity relation for \(x_4,x_6\).

In degree ten, \(A^*H^7F\) has rank four and \(z^*H^6F\) has
rank three. The product \(u_F^*p^*x_6\) adds one independent rank;
\(z^*p^*x_6\) is already in the second subspace. The two scalar
degree-eleven images add two independent ranks, by the primitive tests
of Section 1. The three relations are exactly the commutativity
relations for \((x_4,x_7),(x_4,y_7),(x_5,x_6)\).

Every product rank just used can be checked on actual homology products:
\(AH_5F,AH_6F,AH_7F,zH_6F,u_FH_6F\), and on \(Q_{10}\) for
\(z^{*2}\). In the ranges used all individual homology factors are
primitive. Distinct degree splittings, and the independent factors in
each fixed splitting, make the stated subspaces disjoint. The sole
degree-ten equal-factor test is
\(\overline\Delta Q_{10}=z\otimes z\).

The length-two differentials are injective in degrees seven through ten:
the scalar wedges are

\[
t_3t_4;\quad t_3t_5;\quad
t_3t_6,t_3t'_6,t_4t_5;\quad
t_3t_7,t_4t_6,t_4t'_6,
\]

and their displayed nonzero independent scalar-generator images make
their differentials independent. This proves that positive Tor vanishes
in total degrees at most ten. Higher base generators begin in degree
twelve and their Koszul degrees are at least eleven, so none was omitted.
The Eilenberg--Moore sequence therefore has only filtration zero in the
range in question, with no possible incoming higher differential.
Its edge map is restriction, giving

\[
H^{\le10}E
\cong
\left(H^*F/(p^*\widetilde H^*K(\mathbb F_2,4))H^*F\right)^{\le10}.
\]

This is an isomorphism with Steenrod operations in every range where
both source and target degrees lie at most ten. Dually, inclusion
\(H_iE\to H_iF\) is injective through degree ten.

## 3. Exact homology image and induced operation table

Use the following cover basis, regarded as classes in \(H_*F\):

\[
\begin{array}{c|l}
5&u_F\\
6&D=d_6+e_6,\quad E_6=d_6+f_6\\
7&S=V+P+Q,\quad R\\
8&W,\quad D_8=L+M,\quad J_1,J_2,J_3\\
9&N,K_1,K_2,K_3,K_4,K_5,P_m,S_9=P_n+P_o\\
10&Z_2,U_2,T_{10}=D_2+P_p,P_r,B_1,\ldots,B_8.
\end{array}
\]

Thus the dimensions in degrees five through ten are
\(1,2,2,5,8,12\). Every class in this displayed range is primitive.
For degree ten this follows directly from the previous fiber coproduct
table: the only nonprimitive classes there are removed by the base ideal.

The nonzero operation values in degrees at most eight are

\[
\begin{gathered}
\beta S=D+E_6,\qquad Sq_*^2S=u_F,\\
Sq_*^2D_8=E_6,\qquad Sq_*^2J_1=Sq_*^2J_3=D,
\qquad\beta J_3=R.
\end{gathered}
\]

All other first, second and fourth squares in these degrees are zero.
The degree-nine table is

| Class | \(\beta\) | \(Sq_*^2\) | \(Sq_*^4\) |
|---|---|---|---|
| \(N\) | 0 | \(R\) | \(u_F\) |
| \(K_1\) | 0 | 0 | 0 |
| \(K_2\) | \(J_1+J_2\) | \(R\) | 0 |
| \(K_3\) | \(J_1\) | 0 | 0 |
| \(K_4\) | \(J_2\) | 0 | 0 |
| \(K_5\) | 0 | 0 | 0 |
| \(P_m\) | \(W\) | 0 | 0 |
| \(S_9\) | \(D_8\) | 0 | 0 |

The degree-ten table is

| Class | \(\beta\) | \(Sq_*^2\) | \(Sq_*^4\) |
|---|---|---|---|
| \(Z_2\) | 0 | \(W\) | 0 |
| \(U_2\) | 0 | 0 | 0 |
| \(T_{10}\) | 0 | \(W\) | \(E_6\) |
| \(P_r\) | 0 | 0 | 0 |
| \(B_1\) | \(K_1\) | \(J_2\) | 0 |
| \(B_2\) | 0 | \(J_2\) | 0 |
| \(B_3\) | \(K_1\) | 0 | 0 |
| \(B_4\) | \(K_2+K_3+K_4\) | \(J_1+J_2+J_3\) | \(D\) |
| \(B_5\) | 0 | \(J_1+J_3\) | \(D\) |
| \(B_6\) | 0 | \(J_2\) | 0 |
| \(B_7\) | \(K_5\) | 0 | 0 |
| \(B_8\) | 0 | 0 | 0 |

## 4. Integral information and exact stability scope

The lower Bocksteins and the universal-coefficient theorem give

\[
H_5(E;\mathbb Z_{(2)})\cong\mathbb Z/4,
\quad H_6(E;\mathbb Z_{(2)})\cong\mathbb Z/2,
\quad H_7(E;\mathbb Z_{(2)})\cong\mathbb Z/2,
\quad H_8(E;\mathbb Z_{(2)})\cong(\mathbb Z/2)^4.
\]

For \(H_9\), three order-two summands are detected by the rank-three
first Bockstein from degree ten. The fourth summand is represented by
\(N\). The exact configuration-chain calculation in
`FGH_D2_H10_fiber.md` proves \(\beta_3[B_5]=[N]\) in the fiber \(F\).
To transfer this to the cover, use the Bockstein sequence itself, not
an unsupported claim that integral homology injects whenever mod-two
homology does. In degree nine the cover's second page is the one-dimensional
span of \([N]\), and its map to the corresponding page for \(F\) is
injective. Its outgoing second differential is zero; an incoming
second differential hitting it would map to one hitting \([N]\) in
\(F\), which is impossible. Thus this injection persists to the third
page. The cover class \([B_5]\) cannot be an earlier boundary or have
a nonzero earlier differential: either possibility would contradict
its image's nonzero third differential in \(F\), using the injection
just identified for a possible second-differential target. Naturality
therefore gives \(\beta_3[B_5]=[N]\) in the cover. Hence exactly

\[
H_9(E;\mathbb Z_{(2)})\cong\mathbb Z/8\oplus(\mathbb Z/2)^3.
\]

The full degree-ten audit is essential: \(\beta_3B_6=N\) as well
as \(\beta_3B_5=N\). On the complete first-Bockstein cycle basis
\(Z_2,U_2,T_{10},P_r,B_2,B_5,B_6,B_8,B_1+B_3\), these are the only
nonzero third differentials into \(N\). The exact Moore-four
configuration-chain projections proving this are recorded in
`FGH_D2_H10_fiber.md`. Thus the two primary operation vectors of
the order-eight boundary must both enter the target component calculation.

The cover is a four-connected loop space, since the Postnikov map is a
loop map. Its unit \(E\to\Omega\Sigma E\) has a retraction and is
nine-connected. It is therefore an isomorphism on \(\pi_9\); the target
\(\pi_{10}\Sigma E\) is already stable because \(\Sigma E\) is
five-connected. Hence

\[
\pi_9F\cong\pi_9E\cong\pi_9\Sigma^\infty E.
\]

This does not assert that \(\pi_9F\to\pi_9\Sigma^\infty F\) is
injective. It computes the same ordinary group using the different,
more connected cover spectrum.

## 5. Source audit

The Eilenberg--Moore convergence interface is stated explicitly in
J. P. May, *The cohomology of principal bundles, homogeneous spaces,
and two-stage Postnikov systems*, Bull. AMS (1968), printed p.334:
simply connected base, finite-type cohomology over a field, and
\(E_2=\operatorname{Tor}_{H^*B}(H^*X,\mathbb F_2)\) converging to
the fiber cohomology. The author's primary PDF was opened at
https://www.math.uchicago.edu/~may/PAPERS/6.pdf .
The polynomial base-generator list is Serre's classical computation.
CLM Chapter III supplies the two top-operation formulas in Section 1.
James 1955 Theorem 1.8 supplies the loop-space retraction.

## 6. A geometric spherical test and its exact limitation

There are actual mod-two spherical lifts of both \(K_5\) and \(K_1\).
Take the bottom Moore map \(M(\mathbb Z/2,2)\to B\to T\), with
mod-two classes \(a,b\), and the sphere
\(\overline\alpha:S^5\to T\), with Hurewicz image \(\xi a\).
The generalized Whitehead product of their double adjoints, followed
by double adjunction, gives an actual map

\[
\Sigma(M(\mathbb Z/2,2)\wedge S^5)
=M(\mathbb Z/2,8)\longrightarrow T.
\]

Its bottom sphere has Hurewicz image
\(\{a,\xi a\}=\{a,\{a,a\}\}=0\). The actual mod-two Hurewicz
injectivity on \(\pi_8T\) proved in D.2.20 makes this restriction
null, so the map factors through the top pinch to \(S^9\). Its
mod-two Hurewicz image is
\(\{b,\xi a\}=K_5\). Also the actual Browder bracket of the
bottom sphere \(a\in\pi_2T\) and \(\rho\in\pi_6T\) has
Hurewicz image

\[
\{a,b^2+k+p_3\}=K_5+K_1.
\]

Subtracting a lift of \(K_5\) gives a mod-two spherical lift of
\(K_1\). These constructions were independently checked by both
other agents.

**Integral boundary.** The top Moore pinch has zero integral homology
in degree nine. Therefore this factorization does not force the
chosen sphere's integral Hurewicz image to be precisely an order-two
\(K_5\)-class: it can contain an undetected \(2N\) component.
The same caution applies to \(K_1\). No individual hidden even-nu
coefficient is removed merely by these mod-two spherical lifts.
The actual bracket \(\{a,\rho\}\) does have order dividing two,
by bilinearity and \(2a=0\). Thus it equates the two possible
even-nu coefficients, but does not determine their common value.
The target component calculation explicitly retains this uncertainty.
