# The next target group: pi_9 of Sigma^2 K(F2,2)

**Status, 2026-11-15, current-session audit: proved calculation, independently checked
by `fibrations_groups`; awaiting manuscript assembly.** With the notation
of D.2.18,

\[
\pi_7F=\pi_7T=\pi_9Y\cong\mathbb Z/2,
\qquad \rho\eta_6=0,
\qquad \mu\widetilde\eta_6=0.
\]

Here \(\mu:M(\mathbb Z/4,5)\to F\) is the Moore extension used for the
six- and seven-stage correction, and \(\widetilde\eta_6:S^7\to
M(\mathbb Z/4,5)\) is any lift of \(\eta_6\) under the top-cell pinch.
The generator has Hurewicz image \(R=\{a,c\}\). The two displayed zero
composites settle the specific next source obstruction computed by
`simple_higher`. They do not by themselves give a full infinite-source
extension or a nullification result.

## 1. Why this degree is still stable

The fiber \(F\) is a double loop space: it is \(\Omega^2\) of the fiber
of \(Y\to K(\mathbb F_2,4)\). Write \(F=\Omega Z\). The triangle identity
for suspension and loops makes

\[
\Omega\epsilon_Z:\Omega\Sigma F\longrightarrow F
\]

a left inverse of the unit \(F\to\Omega\Sigma F\). The latter is
therefore injective on every homotopy group. Since \(F\) is
three-connected, Freudenthal makes it surjective on \(\pi_7\).
Thus \(\pi_7F=\pi_8\Sigma F\), and \(\Sigma F\) is four-connected,
so the latter group is already stable.

This argument handles possible torsion terms in the first unstable
kernel without assuming that a list of Whitehead products is exhaustive.
James (1955), Theorem 1.8, printed p.173, gives the same retraction in
terms of the reduced product. The primary scan was opened directly at
`https://webhomes.maths.ed.ac.uk/~v1ranick/papers/jamesred.pdf`.

## 2. The complete degree-eight fiber homology

Continue to write \(A=a^2\), \(z=e+ab\), \(u=\xi a\),
\(d=b^2\), \(e'=b^2+k\), \(f'=p_3\), with \(k=\{a,b\}\).
Let \(i,j,l\in H_8B\) be dual to \(u_B^4,u_Bv_B^2,v_Bw_B\).
The full free double-loop basis of \(H_8T\) consists of the following
sixteen monomials:

\[
i,j,l,\ af,ax,bd,be,c^2,a^2c,ab^2,a^4,
b\xi a,ak,\{a,d\},\{a,e\},\{b,c\}.
\]

There is no additional top-operation term in even degree eight.
The restricted Browder relation gives \(\{a,\xi a\}=0\), and brackets
on identical inputs vanish. These are the free restricted-Gerstenhaber
conventions of the already opened CLM Chapter III basis theorem.

The splitting \(T\simeq B\times F\) subtracts contributions of dimensions
\(3\) from \(H_8B\), \(1\) from \(H_4B\otimes H_4F\), \(2\) from
\(H_3B\otimes H_5F\), and \(3\) from \(H_2B\otimes H_6F\). Therefore
\(\dim H_8F=16-9=7\). A complete basis is

\[
\begin{split}
W&=a^4,\qquad C=c^2,\qquad L=l+bd,\\
M&=j+ax+be+ab^2,\\
J_1&=\{a,d\},\qquad
J_2=\{a,e\}+ak,\qquad
J_3=\{b,c\}+ak.
\end{split}
\]

All except \(C\) are primitive. Directly,
\(\overline\Delta C=A\otimes A\). Each lies in the fiber factor:
the primitive classes have zero image in \(B\), whose degree-eight
homology has no primitives; and \(q_*C=0\), with coaction
\((q_*\otimes1)\Delta C=1\otimes C\), proves the assertion for \(C\).

The complete relevant operation table is

| Class | \(\beta\) | \(\mathrm{Sq}_*^2\) | \(\mathrm{Sq}_*^4\) |
|---|---|---|---|
| \(W\) | 0 | 0 | 0 |
| \(C\) | 0 | 0 | \(A\) |
| \(L\) | \(Q\) | \(d\) | 0 |
| \(M\) | \(Q\) | \(f'\) | 0 |
| \(J_1\) | 0 | \(d+e'\) | 0 |
| \(J_2\) | 0 | 0 | 0 |
| \(J_3\) | \(R\) | \(d+e'\) | 0 |

Here \(Q=h+ad\) and \(R=\{a,c\}\) are the degree-seven fiber classes
of D.2.18. Some checks fixing every coefficient are as follows:

\[
\begin{split}
\beta(u_Bw_B)&=v_Bw_B+u_Bv_B^2,\\
\mathrm{Sq}^2(u_B^3)&=u_B^4+u_Bv_B^2,\\
\beta L&=h+ad=Q,\\
\beta M&=h+a(d+e)+ae=Q,\\
\mathrm{Sq}_*^2L&=b^2=d,\\
\mathrm{Sq}_*^2M&=f+ac+a^3=f',\\
\mathrm{Sq}_*^2\{a,d\}&=k=d+e',\\
\mathrm{Sq}_*^2\{b,c\}&=k=d+e'.
\end{split}
\]

Cartan gives the remaining entries. The square in the last column is
dual to the cup square of the degree-four cohomology class. It vanishes
on every primitive and equals one on \(C\), since its reduced diagonal
is \(A\otimes A\). Thus its coefficient is also checked independently
of a label-operation calculation.

The integral universal coefficient theorem, \(H_6F=(\mathbb Z/2)^2\),
and the two independent first-Bockstein images \(Q,R\) give

\[
H_7F=(\mathbb Z/2)^2.
\]

## 3. The stable seven-skeleton group

Use the stable cells of D.2.18. For this calculation take a finite
approximation through dimension nine before cancelling odd-unit
boundary pairs; this removes extraneous eight-cells as well. Denote
the resulting stable seven-skeleton by \(L_7\). Its six-skeleton is

\[
L_6=C_1^6\vee M(\mathbb Z/4,5)\vee S^6_\rho,
\]

and its seven-cell attachments are

\[
V:\gamma+t,\quad P:\gamma+2\rho+\delta,\quad
Q:\delta,\quad R:0.
\]

We first calculate the needed \(\eta\)-composites in \(L_6\).
The same Chang cofiber sequence as D.2.18, now using
\(\pi_3^S{}_{(2)}=\mathbb Z/8\{\nu\}\), gives

\[
0\longrightarrow\mathbb Z/2\{v=i\nu\}
\longrightarrow\pi_7C_1^6
\longrightarrow\mathbb Z/2\{\eta_5^2\}
\longrightarrow0.
\]

The class \(\delta\eta_6\) maps nontrivially to the last group and has
order two, so the sequence splits. The class \(\gamma\eta_6\) maps to
zero in that quotient and hence is either zero or \(v\). It is zero:
the coefficient of \(\mathrm{Sq}^4\) from the bottom four-class into
the cone of a map \(S^7\to C_1^6\) detects \(v\), using the cofiber of
\(\nu\). This coefficient vanishes for \(\gamma\eta_6\), since the
map factors through \(S^6\). The induced map from the cone of
\(\eta_6\) kills the degree-four class and preserves the new top
degree-eight class. Consequently

\[
\gamma\eta_6=0.
\]

For the Moore summand,

\[
\pi_7M(\mathbb Z/4,5)
=\mathbb Z/2\{t\eta_6\}\oplus\mathbb Z/2\{b\},
\]

where the top pinch sends \(b\) to \(\eta_6\). To see that its lift
has order two, use the cofiber map from the mod-two Moore spectrum
to the mod-four Moore spectrum that is degree two on bottom cells
and degree one on top cells. Oka (1986), Section 2, (2.2)(a)--(b),
p.149, gives \(2\widetilde\eta=i\eta^2\) in the mod-two Moore spectrum;
its image is \(2i\eta^2=0\) in the mod-four spectrum. The two classes
are independent by the top pinch. The primary page was opened
directly, including (2.1) for the first three stable stems.

Let \(c=\rho\eta_6\) in the sphere summand. The maps induced by the
seven-cell attachments on the preceding \(\eta\)-groups kill precisely
\(t\eta_6\) and \(\delta\eta_6\). The kernel of their map on
\(\pi_6\) is freely generated by twice the \(Q\)-cell and the
\(R\)-cell. Therefore the cofiber exact sequence gives

\[
\pi_7L_7=
\mathbb Z_{(2)}\{\kappa\}\oplus
\mathbb Z_{(2)}\{\lambda\}\oplus
(\mathbb Z/2)\{v,b,c\}.
\]

The Hurewicz images of \(\kappa,\lambda\) are \(2Q,R\), respectively.
The free extension splits as a group; choices of the two lifts will
be fixed by operation detectors below.

## 4. Complete operation detectors in this group

For a map with zero mod-two Hurewicz, its cone has a new top
degree-eight class. The coefficients of \(\mathrm{Sq}^2\) from the
three degree-six classes and \(\mathrm{Sq}^4\) from the bottom class
are additive invariants in the stable category, by the cone
naturality for the stable pinch map. The relevant torsion classes have

\[
\begin{array}{c|c|c}
 &\mathrm{Sq}_*^2&\mathrm{Sq}_*^4\\\hline
v&0&A\\
b&d+e'&0\\
c&e'+f'&0.
\end{array}
\]

For \(b\), collapse the Moore bottom; the top \(\eta\)-coextension is
then detected by its top six-class \(d-e'\), whose reduction is
\(d+e'\). For \(c\), use the sphere six-class \(f'-e'\). Both maps
factor through complexes with no degree-four cohomology, so their
fourth-square coefficient is zero. The coefficient for \(v\) is the
Hopf-invariant-one coefficient, and its second-square coefficients
vanish by comparison with the cone on the bottom sphere map.

For \(\kappa\), the top Bockstein is \(Q\). The Adem identity
\(\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^3\mathrm{Sq}^1\), together
with \(\mathrm{Sq}_*^2Q=z\) and \(\beta z=A\), implies that the sum
of its three second-square coefficients is odd. Adding \(b,c\)
therefore makes its second-square vector exactly \(d\). Adding \(v\)
then makes its fourth-square coefficient zero. Fix this choice of
\(\kappa\).

The element \(2\lambda\) has zero second- and fourth-square
coefficients: it factors through degree two on \(S^7\), and comparison
with the mod-two Moore cone in dimensions seven and eight kills the
degree-six and degree-four classes while preserving the top class.

Thus the integral coefficients of \(\kappa\) and \(\lambda\), together
with the displayed square coefficients, determine every possible
eight-cell attachment. There is no unmeasured even multiple of \(\nu\):
the only surviving bottom \(\nu\)-component is \(v\) of order two,
and its fourth square detects it.

## 5. The eight-cell matrix and its cokernel

The integral seven-cycles are freely generated by \(Q,R\).
Since \(H_7F=(\mathbb Z/2)^2\), the eight-cell boundary image is
exactly \(2\mathbb Z_{(2)}\{Q,R\}\). The same parity-preserving
normalization as D.2.18 makes the boundaries of \(L,M,J_3\)
equal to \(2Q,2Q,2R\), respectively, and all other boundaries zero.
It preserves the operation table in Section 2.

The complete attaching table is then

\[
\begin{array}{c|c}
W&0\\
C&v\\
L&\kappa\\
M&\kappa+b+c\\
J_1&b\\
J_2&0\\
J_3&2\lambda+b.
\end{array}
\]

Its cokernel is \(\mathbb Z/2\{\lambda\}\). Since the stable and
unstable groups agree in this degree, this proves

\[
\pi_9Y=\pi_7F=\mathbb Z/2,
\qquad h(\lambda)=R,
\qquad \rho\eta_6=c=0.
\]

The inclusion of the Moore summand sends its top \(\eta\)-lift to
\(b=0\). Any other Moore extension with the same bottom differs by
an element of \(\pi_6F\) followed by the top pinch. Composing the
difference with a top \(\eta\)-lift gives a multiple of
\(\rho\eta_6=0\). Thus the actual Moore extension used in D.2.17
also satisfies \(\mu\widetilde\eta_6=0\), independently of its
allowed top-cell choice.

## Audit scope

The complete homology basis, coproduct membership, Cartan/Nishida
coefficients, Chang and Moore exact sequences, and all operation
detectors were checked independently against `fibrations_groups`.
The source eight-cell calculation is owned separately by `simple_higher`.
Only after its full ordinary extension interface is checked should
the target calculation be used to assert an eight-skeleton extension.

