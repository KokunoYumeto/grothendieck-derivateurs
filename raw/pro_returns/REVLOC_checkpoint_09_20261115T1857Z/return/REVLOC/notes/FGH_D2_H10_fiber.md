# Degree-ten fiber homology: basis, primary operations, and the next Bockstein

**Status update, 2026-11-15 18:08 UTC.** The eighteen-dimensional basis and
primary table have been saved for the target calculation, with independent
polynomial certificates and the induced connected-cover table independently
audited by the root and the source agent. The integral order-eight comparison
in Section 5 has now passed the root audit, with the mixed Kunneth correction
explicit below. These are not yet a numbered manuscript claim.
No assertion about injectivity of stabilization on \(\pi_9F\) is made.

## 1. Notation and the ambient count

Continue D.2.18--D.2.20, with
\(B=K(\mathbb F_2,2)\), \(T=\Omega^2\Sigma^2B\), and
\(F=\operatorname{fib}(q:T\to B)\). The section of \(q\) gives
\(T\simeq B\times F\). Write

\[
A=a^2,\quad z=e+ab,\quad u_F=\xi a,\quad
d_6=b^2,\quad e_6=b^2+k,\quad f_6=f+ac+a^3,
\]

where \(k=\{a,b\}\), \(R=\{a,c\}\). The unadorned letters
\(d,e\) remain the degree-five **label** classes, dual to
\(w_B\) and \(u_Bv_B\). In degree seven put

\[
P=g+ae+bc+a^2b,\qquad Q=h+ad.
\]

The degree-eight classes are

\[
W=a^4,\quad C=c^2,\quad L=l+bd,\quad
M=j+ax+be+ab^2,
\quad J_1=\{a,d\},\quad J_2=\{a,e\}+ak,
\quad J_3=\{b,c\}+ak.
\]

All degree-nine symbols refer to the explicit basis in
`FGH_D2_H9_fiber.md` and D.2.20. In particular
\(Z_A=Az\), \(U_A=Au_F\),
\(N=\xi c+aR+Au_F\),
\(K_\Sigma=K_2+K_3+K_4\), and
\(Z_0=P_m+Z_A+P_n\).

The new degree-ten labels \(p,q,r,s\) are respectively dual to
\(u_B^5,u_B^2v_B^2,u_Bv_Bw_B,w_B^2\). The complete degree-ten ambient
basis contains 42 elements. Its twelve indecomposables are

\[
\begin{gathered}
p,q,r,s,\\
\{a,g\},\{a,h\},\{b,f\},\{b,x\},
\{c,d\},\{c,e\},\{b,k\},\{a,R\}.
\end{gathered}
\]

The identities \(\{a,\xi b\}=\{b,k\}\) and
\(\{c,\xi a\}=\{a,R\}\) prevent double counting. The thirty products
are

\[
\begin{gathered}
ai,aj,al,a\{a,d\},a\{a,e\},a\{b,c\},\\
bg,bh,b\xi b,bR,cf,cx,ck,\\
d^2,de,du_F,e^2,eu_F,u_F^2,\\
a^2f,a^2x,a^2k,abd,abe,abu_F,\\
ac^2,b^2c,a^3c,a^2b^2,a^5.
\end{gathered}
\]

The base and mixed summands in \(H_{10}(B\times F)\) have dimensions
\(4+2+4+3+4+7=24\). Consequently \(\dim H_{10}F=18\).

## 2. A complete candidate fiber basis

Six product classes are

\[
D_A=Ad_6,\quad E_A=Ae_6,\quad F_A=Af_6,
\quad Z_2=z^2,\quad ZU=zu_F,\quad U_2=u_F^2.
\]

An additional primitive square is \(D_2=d^2\), using the degree-five
label \(d\). Define

\[
\begin{split}
Q_{10}&=q+cx+aM+bP+abz,\\
P_p&=p+ai+cf+a^2f+ac^2+a^3c+a^5,\\
P_r&=r+al+bh+ed.
\end{split}
\]

The remaining eight primitive classes are

\[
\begin{split}
B_1&=\{a,g\}+a\{a,e\}+ck+bR+Ak,\\
B_2&=\{a,h\}+a\{a,d\},\\
B_3&=\{b,f\}+ck+a\{b,c\}+Ak,\\
B_4&=\{b,x\},\\
B_5&=\{c,d\}+a\{a,d\},\\
B_6&=\{c,e\}+bR+a\{b,c\}+a\{a,e\}+Ak,\\
B_7&=\{b,k\},\qquad B_8=\{a,R\}.
\end{split}
\]

The reduced diagonal of \(Q_{10}\) is \(z\otimes z\).
The classes \(P_p,P_r,D_2,B_1,\ldots,B_8\) are primitive. All these
classes have zero image under \(q_*\); in particular there is no
degree-ten primitive in \(H_*B\). The product classes are visibly
fiber classes. Thus the diagonal criterion for the product splitting
places every displayed class in the fiber factor. Distinct leading
ambient monomials, with the six independent product classes, prove
linear independence. The dimension count then gives completeness.

For clarity, the bracket diagonal calculations are

\[
\begin{split}
\overline\Delta\{a,g\}
 &=a\otimes\{a,e\}+\{a,e\}\otimes a
   +k\otimes c+c\otimes k+b\otimes R+R\otimes b,\\
\overline\Delta\{a,h\}
 &=a\otimes\{a,d\}+\{a,d\}\otimes a,\\
\overline\Delta\{b,f\}
 &=k\otimes c+c\otimes k
   +a\otimes\{b,c\}+\{b,c\}\otimes a,\\
\overline\Delta\{c,d\}
 &=a\otimes\{a,d\}+\{a,d\}\otimes a,\\
\overline\Delta\{c,e\}
 &=b\otimes R+R\otimes b
   +a\otimes(\{b,c\}+\{a,e\})
   +(\{b,c\}+\{a,e\})\otimes a
   +A\otimes k+k\otimes A.
\end{split}
\]

The class \(\{b,x\}\) is primitive because
\(\overline\Delta x=b\otimes b\) and \(\{b,b\}=0\).
The indicated corrections cancel these diagonals exactly.
For the polynomial nonprimitive class one can use the expanded expression

\[
Q_{10}=q+cx+aj+a^2x+abe+a^2b^2+bg+b^2c.
\]

Direct diagonal expansion leaves precisely \(z\otimes z\).

## 3. Primary operation table

All entries are obtained by Cartan and the already audited label tables;
no new top-operation Nishida correction occurs in this degree.

| Class | \(\beta\) | \(\mathrm{Sq}_*^2\) | \(\mathrm{Sq}_*^4\) |
|---|---|---|---|
| \(D_A\) | 0 | \(W\) | 0 |
| \(E_A\) | 0 | \(W\) | 0 |
| \(F_A\) | 0 | \(W\) | 0 |
| \(Z_2\) | 0 | \(W\) | 0 |
| \(ZU\) | \(U_A\) | 0 | 0 |
| \(U_2\) | 0 | 0 | 0 |
| \(D_2\) | 0 | 0 | \(d_6\) |
| \(Q_{10}\) | \(P_m+Z_A+P_n\) | \(M+C+W\) | \(f_6\) |
| \(P_p\) | 0 | \(W\) | \(f_6\) |
| \(P_r\) | 0 | 0 | 0 |
| \(B_1\) | \(K_1\) | \(J_2\) | 0 |
| \(B_2\) | 0 | \(J_2\) | 0 |
| \(B_3\) | \(K_1\) | 0 | 0 |
| \(B_4\) | \(K_\Sigma\) | \(J_1+J_2+J_3\) | \(d_6+e_6\) |
| \(B_5\) | 0 | \(J_1+J_3\) | \(d_6+e_6\) |
| \(B_6\) | 0 | \(J_2\) | 0 |
| \(B_7\) | \(K_5\) | 0 | 0 |
| \(B_8\) | 0 | 0 | 0 |

The label operations used here are

\[
\begin{array}{c|ccc}
 &\beta&\mathrm{Sq}_*^2&\mathrm{Sq}_*^4\\\hline
p&0&0&f\\
q&m+n&j&f\\
r&0&0&0\\
s&t&l&x
\end{array}
\]

For example, \(\mathrm{Sq}^4(u_B^3)=u_B^5+u_B^2v_B^2\), and
\(\mathrm{Sq}^4(v_B^2)=w_B^2\). The first Bockstein on \(Q_{10}\)
has the exact value

\[
\beta Q_{10}=P_m+P_n+Z_A=Z_0.
\]

Thus the essential zero-boundary class used in D.2.20 is, in fact, a
first-Bockstein boundary from degree ten. This is an independent check
on the second-Bockstein correction that changed the stable target group.
The other two operations on this class are

\[
\mathrm{Sq}_*^2Q_{10}=M+C+W,
\qquad \mathrm{Sq}_*^4Q_{10}=f_6.
\]

As checks, \(\mathrm{Sq}_*^5Q_{10}=z\), consistent with its diagonal
\(z\otimes z\), and
\(\mathrm{Sq}_*^2\mathrm{Sq}_*^2Q_{10}=f_6\).

The image of \(\beta:H_{10}F\to H_9F\) is exactly the independent
five-dimensional span

\[
\langle U_A,K_1,K_\Sigma,K_5,Z_0\rangle.
\]

## 4. What follows for the next integral group without a hidden extension

The universal-coefficient sequence and the already proved
\(H_8F\cong\mathbb Z/4\{C\}\oplus(\mathbb Z/2)^4\) give six
cyclic summands in the finite two-primary group \(H_9F\). The rank-five
first Bockstein above identifies five summands of exponent two. On the
second page the degree-nine classes remaining after incoming first
Bocksteins are represented by \(N\) and \(P_n\). The established
\(\beta_2P_n=C\) removes the latter. Therefore there is a single
remaining higher-exponent summand represented modulo two by \(N\).
Its exact exponent is eight by the independently audited higher-Bockstein
comparison below; it is not determined by the primary table alone.

## 5. Integral configuration-chain calculation: an order-eight candidate

The integral chain summand corresponding to \(H_4B\cong\mathbb Z/4\)
has generators \(c\) in degree four and \(d\) in degree five with
\(\partial d=4c\). In the arity-two circle configuration complex put

\[
z_c=e_1(c\otimes c),\quad
v=e_0(c\otimes d-d\otimes c),\quad
h=e_1(c\otimes d),\quad h'=e_1(d\otimes c).
\]

With the usual Koszul signs the exact boundaries are

\[
\partial h=-v-4z_c,\qquad
\partial h'=v-4z_c,
\qquad \partial(h+h')=-8z_c.
\]

Also \(\partial e_0(d\otimes d)=4v\). Thus this two-generator
quadratic chain block has a cyclic order-eight class represented by
\(z_c\). Keeping both mixed-label circle chains is essential: using
only \(e_0(d\otimes d)+4h\) would give a misleading order-sixteen
bound and overlook the displayed order-eight relation.

There is a compatible Browder-chain description. For integral label
chains use

\[
\partial\lambda(s,t)=-\lambda(\partial s,t)
 -(-1)^{|s|}\lambda(s,\partial t).
\]

The even-dimensional self-bracket is twice the top circle class, so
\(\partial\lambda(c,d)=-8z_c\). The corrected degree-ten fiber
class \(B_5=\{c,d\}+a\{a,d\}\) has an integral representative
whose second summand contributes \(-4aR\). Since
\(\partial b=2a\), adding \(2bR\) cancels that contribution.
The resulting boundary is \(-8z_c\). Modulo earlier Bocksteins
\(N\) and \(\xi c\) coincide, because \(aR\) and \(Au_F\) are
first-Bockstein boundaries in the ambient double-loop space.

**Full comparison, independently audited by the root.** Snaith's
Theorem 1.1 gives the integral stable splitting into configuration
weights. In weight two the chain complex is the derived
\(\Sigma_2\)-coinvariant complex
\(C_*(\mathcal C_2(2))\otimes_{\Sigma_2}\widetilde C_*(B)^{\otimes2}\).
The integral free chain complex of \(B\) has a chain retract onto the
elementary Moore summand \((c_4,d_5;\partial d=4c)\): this is ordinary
Smith decomposition of a bounded-below free complex over \(\mathbb Z\).
Its tensor square is equivariant for the signed transposition. The
configuration chains are free over \(\mathbb Z[\Sigma_2]\), so this
chain retract survives passage to the displayed derived tensor product.
No topological Moore-space retraction of \(B\) is being assumed.

For completeness, the entire relevant quadratic block has bases

\[
\begin{array}{c|l}
8&e_0(cc)\\
9&e_0(cd),e_0(dc),z_c=e_1(cc)\\
10&q=e_0(dd),h=e_1(cd),h'=e_1(dc)\\
11&e_1(dd).
\end{array}
\]

The degree-nine cycles have basis \(v=e_0(cd-dc),z_c\).
The three degree-ten boundary columns in this basis are
\((4,0),(-1,-4),(1,-4)\). Their Smith invariants are \(1,8\), so
the degree-nine homology is exactly \(\mathbb Z/8\{z_c\}\).
The final boundary is
\(\partial e_1(dd)=-2q-4h+4h'\), consistent with the preceding
formulas. Thus no unspecified higher cell in this retract can remove
the order-eight class.

The integral class lifting \(N\) has weight-two component \(\xi c\).
Its other displayed summands \(aR\) and \(a^2\xi a\) have order
dividing two, since they have the integral order-two factor \(a\).
Consequently this lift has exact order eight in \(H_9T\).
The actual product splitting \(T\simeq B\times F\) takes its reduction
to the fiber class \(N\). One must include the mixed Kunneth summands
here, rather than only the base summand. The degree-nine base homology
has exponent two; every mixed tensor or Tor summand has exponent at
most four. For example \(H_4B\otimes H_5F\cong\mathbb Z/4\) is a
mixed summand that cannot be ignored. The ordinary integral Kunneth
sequence splits as abelian groups, so the entire complement of
\(H_9F\) has exponent at most four. Consequently projection to \(F\)
retains exact order eight. This proves

\[
H_9F\cong\mathbb Z/8\oplus(\mathbb Z/2)^5.
\]

Naturality then identifies the displayed corrected mixed-label circle
class with \(\beta_3[B_5]=[N]\). The earlier order-sixteen and
comparison uncertainties remain documented above as the path to this
corrected calculation, not as current unresolved assumptions.

Snaith's primary Theorem 1.1 and the filtration-quotient description in
Section 2 were reopened at
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Snaith-split.pdf
(printed pages 577--579).

### Complete third-Bockstein check: the second order-eight relation

**Correction found while completing the next target matrix.** The class
\(B_6\), as well as \(B_5\), has third Bockstein \(N\). The two
relations must both be retained; using only \(B_5\) leaves a spurious
possible hidden extension.

Indeed choose the integral chain decomposition with
\(\partial d=4c\), \(e=d+y\), \(\partial y=0\), and
\(\partial x=2y\), with harmless odd-unit changes if necessary.
The chain retract onto the Moore-four block sends both \(d\) and
\(e\) to \(d\), while it sends every label of degree other than
four or five to zero. Under projection to weight two, followed by this
retract, \(B_5\) and \(B_6\) both map to the mixed-label circle
class \(h+h'\). Their higher-weight corrections disappear. Thus

\[
\beta_3[B_5]=[N],\qquad \beta_3[B_6]=[N].
\]

Here is the exhaustive check for the cover, whose degree-ten first-
Bockstein cycles have basis

\[
Z_2,U_2,T_{10},P_r,B_2,B_5,B_6,B_8,B_1+B_3.
\]

Their projections to the Moore-four quadratic block are respectively

\[
q,\ 0,\ q,\ q,\ 0,\ h+h',\ h+h',\ 0,\ 0,
\qquad q=e_0(dd).
\]

The class \(q\) is already a first-Bockstein boundary: the formula
\(\partial e_1(dd)=-2q-4h+4h'\) gives
\(\beta_1[e_1(dd)]=[q]\). The third differential on the displayed
cycle basis therefore has coefficient one on exactly \(B_5,B_6\)
and coefficient zero on the other seven classes (a class may of course
already represent zero on the third page). No outgoing second
differential can hit \(N\), because projection detects its order-eight
survival. This also proves that \(B_5\) and \(B_6\) survive to the
third page: their projected classes do.

For the original fiber \(F\), the complete degree-ten first-Bockstein
cycle basis is

\[
D_A,E_A,F_A,Z_2,U_2,D_2,P_p,P_r,
B_2,B_5,B_6,B_8,B_1+B_3.
\]

The same projection proves that the only nonzero third differentials
into \(N\) are again the two just displayed. In particular
\(B_6+B_2\) has zero second and fourth squares but nonzero third
Bockstein, while \(B_5+B_6\) has zero third Bockstein. These are
distinct pieces of input for the next cellular matrix.

## 6. Scope and next unstable interface

This note supplies the next homology matrix. It does not make
\(\pi_9F\) stable. The double-loop unit gives a retraction into
\(\Omega^2\Sigma^2F\), but the next stabilization lies at the first
possible quadratic kernel. The Browder self-bracket of the bottom
\(\pi_4F\)-class and its image through the Chang complex must be
handled separately. The other agents own that exact interface and the
source ten-skeleton. An eventual stable relation alone will not be used
as an ordinary nullhomotopy.

### Primary-source interfaces

- Serre, *Cohomologie modulo 2 des complexes d'Eilenberg--Mac Lane*,
  Section 2: the polynomial cohomology and label operations already
  opened and cited in the manuscript.
- Cohen--Lada--May, *The Homology of Iterated Loop Spaces*, Chapter III,
  Theorems 1.2--1.4 and the integral configuration-chain calculation:
  the free double-loop basis, restricted Browder identities, Cartan
  formulas, and integral circle signs. Printed pages 217--218 and 232
  were opened visually earlier in this session.
- D.2.18--D.2.20 supply the complete lower-degree tables and integral
  fiber/base splitting used above.

### Finite polynomial certificate

`code/FGH_H10_poly_check.py` independently checks all coproducts and
twenty-one first/second/fourth-square values for the seven polynomial
classes \(D_A,F_A,Z_2,D_2,Q_{10},P_p,P_r\). It returned `PASS`; the
exact output is `code/outputs/FGH_H10_poly_check.json`. The root's
separately authored degree-ten polynomial certificate also returned
`PASS`. Neither certificate claims to check the Browder formulas,
integral comparison, or any homotopy attachment.
