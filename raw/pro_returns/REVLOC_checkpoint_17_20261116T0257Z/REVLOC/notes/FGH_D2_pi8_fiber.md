# Independent audit: the degree-eight group and the seven-cell relation

**Status, 2026-11-15 17:09 UTC.** The calculation below passes the independent
audits of the root and the three mathematical agents. It proves

\[
\pi_8(\Sigma^2K(\mathbb F_2,2))\cong\mathbb Z/4,
\qquad 2\rho=(u_4\nu_4)\eta_7,
\]

where \(\rho\) is any sphere map whose double-loop Hurewicz image is the
class \(r=b^2+\{a,b\}+f+ac+a^3\) constructed in D.2.17. In particular every
such \(\rho\) has order four. This is an exact unstable group calculation,
obtained by moving to a three-connected fiber where the relevant degree is
stable. It does **not** infer an order from the Pontryagin--Thom construction
alone. The calculation cancels the specified seven-cell obstruction; no
extension over all higher cells or nullification conclusion is asserted.

## 1. A three-connected fiber

Put \(B=K(\mathbb F_2,2)\), \(Y=\Sigma^2B\), and \(T=\Omega^2Y\).
The bottom cohomology class gives a map
\(Y\to K(\mathbb F_2,4)\), hence a double-loop H-map

\[
q:T\longrightarrow B.
\]

The ordinary double-suspension unit \(j:B\to T\) is a section: the
composite is the identity on the unique nonzero homotopy group of \(B\).
Let \(F=\operatorname{fib}(q)\). The multiplication of the grouplike
H-space \(T\) gives a weak equivalence

\[
B\times F\longrightarrow T,\qquad(b,f)\longmapsto j(b)\,f.
\]

Only a space section is required; no multiplicativity of \(j\) is used.
An inverse is obtained using \(q\) and multiplication by the inverse of
\(j(q(t))\). The long exact sequence gives that \(F\) is three-connected
and that \(\pi_6F=\pi_6T=\pi_8Y\). Freudenthal identifies \(\pi_6F\)
with its stable value. Cells of dimension eight or more do not affect it.

The spaces in question have finite-type homology and finite two-primary
positive homotopy groups, by the Serre-class theorem applied to \(Y\)
and then to its connected loop spaces and fiber. Thus the low integral
homology groups below contain neither rational nor odd-primary parts.

## 2. Complete low homology of the fiber

Use the labels and operations fixed in D.2.13 and D.2.17. Set

\[
A=a^2,\quad z=e+ab,\quad u=\xi a,
\quad d=b^2,\quad e'=b^2+\{a,b\},\quad f'=p_3=f+ac+a^3.
\]

The following is the entire reduced mod-two homology of \(F\) through
degree seven:

| Degree | Basis | \(\beta=\mathrm{Sq}_*^1\) | \(\mathrm{Sq}_*^2\) |
|---|---|---|---|
| 4 | \(A\) | 0 | 0 |
| 5 | \(z,u\) | \(A,0\) | \(0,0\) |
| 6 | \(d,e',f'\) | \(0,0,0\) | \(A,A,A\) |
| 7 | \(V=\xi b,R=\{a,c\},P,Q\) | \(e',0,f',0\) | \(u,0,z,z\) |

Here

\[
P=g+ae+bc+a^2b,\qquad Q=h+ad,
\]

with \(g,h\) the labels dual to \(u_B^2v_B,u_Bw_B\) in the notation of
the original Eilenberg--Mac Lane cohomology calculation. The subscript
distinguishes those cohomology generators from the homology class \(u=\xi a\).

These are precisely the primitive kernel classes of \(q_*\). For example,
\(u=\xi a\) is spherical by D.2.17, so maps to zero in \(B\); the three
degree-six primitives map to zero under the Eilenberg--Mac Lane addition
law; and \(B\) has no primitive degree-seven homology, since its
cohomology has no indecomposable generator in degree seven. In a tensor
product of connected coalgebras the primitive subspace is the sum of the
primitive subspaces of the two factors. Therefore these classes belong
to the fiber factor, without an unsupported identification of all of
\(\ker q_*\) with that factor.

Completeness follows from the product splitting. The dimensions of
\(H_iT\) for \(i=4,5,6,7\) are \(2,4,6,9\), from the full free
double-loop basis. Subtracting the contributions of \(B\times F\)
gives fiber dimensions \(1,2,3,4\), exactly the displayed list.

The second Bockstein is

\[
\beta_2[d]=[u],\qquad \beta_2[e']=0.
\]

This is the explicit configuration-chain calculation of D.2.17, not a
guess from primary operations. The first Bockstein table, the second
Bockstein, and the integral universal coefficient theorem give

\[
H_4F=\mathbb Z/2,
\qquad H_5F=\mathbb Z/4,
\qquad H_6F=(\mathbb Z/2)^2.
\]

For the last assertion, \(e',f'\) are the two independent first-Bockstein
images in degree six. The remaining mod-two class \(d\) is the Tor
contribution of \(H_5F=\mathbb Z/4\), detected by its second Bockstein.

## 3. The stable six-skeleton

Work in two-local spectra with the suspension spectrum of \(F\). Its
finite low-dimensional cellular model can be made minimal modulo two
by elementary cell slides and cancellation of odd-unit boundary pairs.
This is only a finite-range operation: higher cells may be retained and
their attaching maps adjusted. Consequently the cells through dimension
seven can be indexed by the displayed mod-two homology bases. Equivalently
one may carry out the following argument after adjoining and subsequently
cancelling contractible cell pairs.

The five-skeleton is \(P^5(2)\vee S^5_u\), where \(P^5(2)\) has bottom
four-cell \(A\) and five-cell \(z\) of boundary \(2A\).
The six-cells \(d,e',f'\) all have the \(\eta\)-component into the bottom
four-cell, since each has square \(\mathrm{Sq}_*^2=A\). The integral
boundary of \(d\) is \(4u\); those of \(e',f'\) are zero.
There is no further six-cell attachment component: in this range the
only stable maps to the bottom Moore complex are its bottom \(\eta\),
and the component to \(S^5_u\) is its degree.

Change six-cell basis to

\[
e',\qquad d-e',\qquad r=f'-e'.
\]

Here the last formula is an integral cell-basis choice; its mod-two
reduction is the already specified class \(e'+f'\).

The result is the stable wedge

\[
F^{(6)}\simeq C\vee M(\mathbb Z/4,5)\vee S^6_r,
\qquad C=P^5(2)\cup_{i\eta_4}e^6.
\]

The Moore bottom is the class \(u=\xi a\), represented in \(F\) by
the double adjunct of \(\alpha=u_4\nu_4\).

## 4. The complete stable attaching-map detectors

The complex \(C\) is the cofiber of

\[
(2,\eta):S^4\vee S^5\longrightarrow S^4.
\]

Using \(\pi_1^S=\mathbb Z/2\{\eta\}\),
\(\pi_2^S=\mathbb Z/2\{\eta^2\}\), and \(\eta^2\ne0\), the cofiber
sequence gives an injection

\[
\pi_6C\hookrightarrow
\pi_6(C/S^4)=\mathbb Z/2\{\eta_5\}\oplus\mathbb Z\{\iota_6\}
\]

with image \(\mathbb Z/2\oplus2\mathbb Z\). Thus

\[
\pi_6C=\mathbb Z\{\gamma\}\oplus\mathbb Z/2\{\delta\},
\]

where \(\gamma\) maps to \((0,2)\) and \(\delta\) to \((\eta_5,0)\).
The Hurewicz image of \(\gamma\) is \(2e'\). The quotient to the
five-sphere detects exactly \(\delta\). Therefore the square from the
degree-five class \(z\) into a newly attached seven-cell detects the
\(\delta\)-coefficient of that attaching map.

Similarly,

\[
\pi_6M(\mathbb Z/4,5)=\mathbb Z/2\{i\eta_5\}.
\]

The square from its degree-five bottom \(u\) detects exactly this
coefficient. Finally the last summand has \(\pi_6S^6=\mathbb Z\).
There are no cross summands, since the calculation is stable (or,
unstably, all possible Whitehead products start in higher degree).

It follows that **integral six-dimensional degrees and the two square
coefficients determine every seven-cell attaching map completely**.
No unmeasured secondary component remains.

## 5. Normalizing the integral seven-cell matrix without losing the squares

The six-cycles are freely generated by \(e',f'\), and
\(H_6F=(\mathbb Z/2)^2\). Thus the image of the integral cellular boundary
from degree seven is exactly \(2\mathbb Z\{e',f'\}\).
After dividing that boundary matrix by two it is a surjection onto
\(\mathbb Z^2\). The first Bockstein identifies its reduction modulo
two: \(V\mapsto e'\), \(P\mapsto f'\), and \(Q,R\mapsto0\).

One can choose preimages of \(e'\) and \(f'\) congruent to \(V,P\)
modulo two: an initial lift differs from the desired preimage by an
even vector in \(\mathbb Z^2\), which is corrected by twice a chain
using surjectivity. Likewise the kernel reduces onto the kernel of
the matrix modulo two, since its quotient is free. Hence choose the
zero-boundary seven-cells congruent to \(Q,R\). These changes preserve
every mod-two square coefficient. The integral boundaries are now
exactly \(2e',2f',0,0\).

In the wedge coordinates of Section 3, write \(a_\eta\) for the Moore
bottom \(\eta\)-class and \(\rho_0\) for the last sphere generator.
The complete seven-cell attaching relations, by Section 4 and the
operation table, are

\[
\begin{array}{c|c}
V&\gamma+a_\eta\\
P&\gamma+2\rho_0+\delta\\
Q&\delta\\
R&0.
\end{array}
\]

There is no sign issue in the final order-two relation. Quotienting
\(\mathbb Z\gamma\oplus\mathbb Z/2\delta\oplus
\mathbb Z/2a_\eta\oplus\mathbb Z\rho_0\) by these relations gives

\[
\pi_6F\cong\mathbb Z/4\{\rho_0\},
\qquad 2\rho_0=a_\eta.
\]

The image of \(a_\eta\) in \(T\) is precisely the double adjunct of
\((u_4\nu_4)\eta_7\), since the Moore bottom was represented by the
double adjunct of \(u_4\nu_4\). The double-loop Hurewicz of \(\rho_0\)
is \(r=e'+f'\). Every element with that Hurewicz image is an odd
generator of this cyclic group, so the same doubling relation holds
for the Pontryagin--Thom representative in D.2.17.

## 6. Consequence and boundary

For the seven-skeleton quotient of the source in the independent
source-cell audit, the only nonzero correction obstruction is

\[
\overline\alpha\eta_5+2\rho\in\pi_6T.
\]

The relation just proved makes it zero. The additional zero-boundary
seven-cell represented modulo two by \(A_0B_0+Q^4A_0\) has zero square
from the five-cell and hence has zero correction obstruction.

This establishes the required seven-stage cancellation. It neither
computes the eight-cell and later obstructions nor turns the existing
map into a map on all of \(Q\Sigma B\).

## Sources and audit provenance

* The full homology, coproduct, and Steenrod table is the already opened
  Cohen--Lada--May Chapter III calculation recorded in D.2.13, D.2.16,
  and D.2.17. The exact second Bockstein uses the explicit integral
  configuration chain, with the conventions of III Lemma 3.10, p.232.
* Eilenberg--Mac Lane cohomology and finite two-primary homotopy use the
  already opened Serre computations and Serre-class theorem.
* The elementary stable Chang computation can alternatively use Oka
  (1986), Section 2, equations (2.2)(a)--(b), p.149, directly opened by
  `simple_higher`, for \(2\widetilde\eta=i\eta^2\) and
  \(p\widetilde\eta=\eta\). The cofiber proof above only requires the
  first two stable stems and displays the complete detector map.
* Mukai (2001), saved as `FGH_Mukai2001.pdf`, was opened as a search lead.
  Its main computations concern higher Moore-space groups and are not
  needed in the proof above.

