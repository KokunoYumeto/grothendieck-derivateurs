# Complete degree-nine fiber homology and the remaining target composites

**Status, 2026-11-15: the complete calculation has passed the root and
all three independent agent audits and is integrated in D.2.20.**
Both \(\overline\alpha\nu_5\) and \(\lambda\eta_7\) vanish. The corrected
stable group is \((\mathbb Z/2)^3\), and the actual mod-two Hurewicz map
on \(\pi_8F\) is injective. Together with the source calculation this
gives an ordinary nine-skeleton extension. The derivation below retains
the intermediate uncertainty and the correction of the earlier proposed
order-four stable summand; no full-source extension is asserted.

Keep the notation of D.2.18--D.2.19. Thus
\(A=a^2\in H_4F\), \(z=e+ab\), \(u_F=\xi a\),
\(k=\{a,b\}\), \(R=\{a,c\}\),
\(P=g+ae+bc+a^2b\), and \(Q=h+ad\).
The degree-eight fiber classes are

\[
W=a^4,\ C=c^2,\ L=l+bd,\ M=j+ax+be+ab^2,
\ J_1=\{a,d\},\ J_2=\{a,e\}+ak,\ J_3=\{b,c\}+ak.
\]

## 1. Entire degree-nine basis

Let \(m,n,o,t\in H_9B\) be dual to
\(u_B^3v_B,u_B^2w_B,v_B^3,\mathrm{Sq}^4w_B\), respectively.
The entire free double-loop basis of \(H_9T\) has 26 elements:

\[
\begin{gathered}
m,n,o,t,\\
ag,ah,a\xi b,aR,bf,bx,bk,cd,ce,c\xi a,
a^2d,a^2e,a^2\xi a,abc,b^3,a^3b,\\
\{a,f\},\{a,x\},\{b,d\},\{b,e\},\{a,k\},\xi c.
\end{gathered}
\]

The restricted Browder identity identifies \(\{b,\xi a\}\) with
\(\{a,k\}\); it is not an additional generator. The mixed terms in
\(H_9(B\times F)\) have dimensions \(2,2,3,4\), and the base has
dimension four. Therefore \(\dim H_9F=26-15=11\).

A complete fiber basis is

\[
\begin{split}
Z_A&=Az,&U_A&=Au_F,\\
N&=\xi c+aR+Au_F,\\
K_1&=\{a,f\}+aR,&
K_2&=\{a,x\}+bk,\\
K_3&=\{b,d\},&
K_4&=\{b,e\}+bk,&K_5&=\{a,k\},\\
P_m&=m+ag+ce+a^2e+bf+a^3b,\\
P_n&=n+ah+cd+a^2d,\\
P_o&=o+bx+b^3.
\end{split}
\]

The first two are products of primitive fiber classes. All other
displayed classes are primitive. For the top-operation term,
the exact diagonal is

\[
\overline\Delta(\xi c)=
u_F\otimes A+A\otimes u_F+R\otimes a+a\otimes R.
\]

This follows by applying top-operation additivity and Cartan to
\(\Delta c=c\otimes1+1\otimes c+a\otimes a\). Adding \(aR+Au_F\)
cancels precisely these four terms. The other primitive corrections
follow directly from the label diagonal. For example
\(\overline\Delta\{a,x\}=k\otimes b+b\otimes k\), canceled by \(bk\).
The polynomial primitive \(P_m\) can also be checked as the
\(u_B^3v_B\)-coefficient of the logarithmic derivative of the
group-like label series; the displayed finite formula suffices to
check it directly, without invoking logarithms in characteristic two.

All these classes map to zero under \(q_*\). In degree nine the only
primitive in \(H_*B\) is the label \(t\), so the polynomial and
Browder expressions have zero image immediately. For \(N\), the
fourth-square calculation below gives \(\mathrm{Sq}_*^4N=u_F\).
Since \(q_*u_F=0\), whereas \(\mathrm{Sq}_*^4t=d\ne0\), its possible
\(t\)-coefficient also vanishes. Thus the primitive classes are in
the fiber factor, and the product classes plainly are as well.
The dimension count proves completeness.

## 2. Exact first, second, and fourth squares

The operation table is

| Class | \(\beta\) | \(\mathrm{Sq}_*^2\) | \(\mathrm{Sq}_*^4\) |
|---|---|---|---|
| \(Z_A\) | \(W\) | 0 | 0 |
| \(U_A\) | 0 | 0 | 0 |
| \(N\) | 0 | \(R\) | \(u_F\) |
| \(K_1\) | 0 | 0 | 0 |
| \(K_2\) | \(J_1+J_2\) | \(R\) | 0 |
| \(K_3\) | \(J_1\) | 0 | 0 |
| \(K_4\) | \(J_2\) | 0 | 0 |
| \(K_5\) | 0 | 0 | 0 |
| \(P_m\) | \(W\) | 0 | 0 |
| \(P_n\) | 0 | \(P+Q\) | \(z\) |
| \(P_o\) | \(L+M\) | \(P+Q\) | \(z\) |

The top-operation correction in the \(N\)-row must not be omitted.
For \(c\) of degree four and the top double-loop operation
\(\xi c=Q^5c\), CLM's top Nishida formula gives

\[
\mathrm{Sq}_*^2(\xi c)
=Q^3c+Q^4\beta c+\{c,\mathrm{Sq}_*^2c\}
=\{c,a\}=R.
\]

The first term is zero by instability and \(\beta c=0\).
For the fourth square only the \(i=2\) binomial term remains:

\[
\mathrm{Sq}_*^4(\xi c)=Q^3(\mathrm{Sq}_*^2c)
=Q^3a=\xi a.
\]

The possible top Browder corrections are zero, since
\(\beta c=\mathrm{Sq}_*^3c=\mathrm{Sq}_*^4c=0\).
The added terms \(aR+Au_F\) have zero second and fourth squares.

For the polynomial rows, the needed label formulas are

\[
\begin{split}
\beta m&=\beta n=0,&\beta o&=j+l,\\
\mathrm{Sq}_*^2m&=0,&
\mathrm{Sq}_*^2n&=\mathrm{Sq}_*^2o=g+h,\\
\mathrm{Sq}_*^4m&=0,&
\mathrm{Sq}_*^4n&=\mathrm{Sq}_*^4o=e.
\end{split}
\]

They are dual to Cartan on the polynomial Serre generators. For
example \(\mathrm{Sq}^2(u_B^2v_B)=v_B^3+u_B^2w_B\), the same
formula holds for \(\mathrm{Sq}^2(u_Bw_B)\), and
\(\mathrm{Sq}^4(u_Bv_B)=u_B^2w_B+v_B^3\).
Cartan then gives

\[
\begin{split}
\beta P_m&=af+af+a^4=W,\\
\beta P_o&=j+l+ax+b(d+e)+ab^2=L+M,\\
\mathrm{Sq}_*^2P_n&=\mathrm{Sq}_*^2P_o=P+Q,\\
\mathrm{Sq}_*^4P_n&=\mathrm{Sq}_*^4P_o=e+ab=z.
\end{split}
\]

The bracket formulas use the Cartan rule for the Browder bracket.
For instance \(\beta K_2=J_1+J_2\),
\(\mathrm{Sq}_*^2K_2=\{a,c\}=R\), and the other listed
bracket second and fourth squares vanish.

## 3. An exact second Bockstein and H_8(F;Z)

The first-Bockstein images from degree nine span
\(W,J_1,J_2,L+M\). In degree eight the first-Bockstein cycles
are generated by these four classes and \(C=c^2\). Thus the
degree-eight second page is one-dimensional on \([C]\).

There is a precise second Bockstein

\[
\beta_2[P_n]=[C]\ne0.
\]

There is also a second, essential relation:

\[
\beta_2[P_m+Z_A]=[C].
\]

Indeed \(P_m+Z_A=m+ag+ce+bf\), while
\(\beta(bg)=ag+bf\). Thus its second-page class is
\([m]+[c][e]\). The relation \(\beta x=d+e\) gives
\([e]=[d]\), so \(\beta_2[e]=[c]\). The same base/fiber
separation argument as below forces \(\beta_2[m]=0\) and proves
the displayed equality. Omitting this second relation incorrectly
leaves an order-four summand in the later stable homotopy calculation.

Here is an argument retaining the base/fiber distinction. On the
second page for \(T\), \([a]=0\), since \(\beta b=a\). Therefore

\[
[P_n]=[n]+[c][d].
\]

The unit \(B\to T\) preserves the known second Bockstein
\(\beta_2[d]=[c]\) of \(H_4B=\mathbb Z/4\). Since the Bockstein
spectral sequence is multiplicative for the Pontryagin product,
\(\beta_2([c][d])=[c]^2=[C]\).
The term \(\beta_2[n]\) lies in the base factor, because \(n\)
is a unit label. On the other hand \(P_n\) and \(C\) are fiber
classes. The splitting \(T\simeq B\times F\) splits the Bockstein
spectral sequence as a tensor product over \(\mathbb F_2\), so the
positive-degree base and fiber factors have zero intersection.
It follows that \(\beta_2[n]=0\) and the displayed equality holds.
This also proves that \([P_n]\) is not a first-Bockstein boundary.

Together with the universal coefficient theorem and
\(H_7F=(\mathbb Z/2)^2\), this gives

\[
H_8F\cong\mathbb Z/4\oplus(\mathbb Z/2)^4.
\]

For completeness, the entire first-Bockstein cycle space in degree
nine has basis

\[
U_A,N,K_1,K_5,K_2+K_3+K_4,P_n,P_m+Z_A.
\]

The second Bockstein vanishes on the first five. The classes
\(N\) and \(K_2+K_3+K_4\) have the explicit integral cycle lifts
in Section 5. The other three are already first-Bockstein boundaries:
\(U_A=\beta(zu_F)\),
\(K_1=\beta(\{b,f\}+bR)\), and
\(K_5=\beta\{b,k\}\), followed when necessary by the actual
projection from \(T\) to \(F\). The last two basis classes both
have second Bockstein \(C\). This is a complete filtered boundary
calculation, rather than a single sufficient nonzero differential.

## 4. The actual remaining composites

**Historical boundary, now resolved by D.2.20.** The component calculation
in `EH5_pi8_stable_target.md` supplies the missing exact group and proves
both composites below zero. The discussion records why primary parity
alone was insufficient before that calculation.

The target component-group calculation is owned by `fibrations_groups`.
The source ninth-stage audit identifies two priorities:

1. the exact value of \(\overline\alpha\nu_5\), including its possible
   undetected even multiple;
2. the image of a free source class with integral Hurewicz twice the
   relevant eight-cell, modulo changes by twice a target class.

The operation combination

\[
K_2+K_3+K_4
\]

has zero first Bockstein, second square \(R\), and fourth square
zero. The class \(N\) has the same second square and fourth square
\(u_F\). Their sum therefore isolates the primary \(\nu\)-coefficient
on the Moore bottom. This is useful input, but **is not a proof that
the full order-four \(\nu\)-class vanishes** until the exact target
component group and all remaining detectors are supplied.

The stable comparison also needs care. The double-loop counit makes
\(\pi_8F\to\pi_8\Sigma^\infty F\) injective. The independent James-pair
calculation of `fibrations_groups` gives a further quadratic
\(\mathbb Z/2\) summand in the stable group; it must not be treated as
an actual unstable sphere map. Injectivity is sufficient for a
genuine stable zero test, but not for lifting every stable element.

## 5. Two genuine integral cycles

Both \(N\) and \(K_2+K_3+K_4\) have integral cycle representatives,
so they may be chosen as zero-integral-boundary nine-cells in a
parity-preserving minimal stable model. This is stronger than merely
asserting that their second Bocksteins vanish.

Choose integral label chains \(a_2,b_3,c_4,y_5,x_6\) with
\(db=2a\), \(dc=dy=0\), and \(dx=2y\), where the reduction of
\(y\) is \(d+e\). The exact coefficient two follows from the already
computed cyclic group \(H_5B=\mathbb Z/2\); labels may be normalized
by even chain changes. For a degree-one Browder chain operation,

\[
d\lambda(s,t)=-\lambda(ds,t)-(-1)^{|s|}\lambda(s,dt).
\]

It follows that
\(\lambda(a,x)-\lambda(b,y)\) is an integral cycle. Its reduction is
exactly \(K_2+K_3+K_4\), since the two \(bk\) corrections cancel.

Since \(c\) is an integral cycle of even degree, the arity-two
configuration chain \(e_1(c\otimes c)\) is an integral cycle.
The remaining terms of \(N\), namely \(aR\) and \(a^2\xi a\), are
also products of integral cycles. This gives an integral cycle
lifting \(N\) in \(T\). Apply the actual space projection
\(T\simeq B\times F\to F\) to these cycles. Their mod-two classes
are unchanged, because the displayed classes lie in the fiber
factor. Thus both are integral fiber cycles.

The target component-group calculation must still check other
torsion components. Once its asserted residual group
\(\mathbb Z/4\{\overline\alpha\nu\}\oplus
\mathbb Z/2\{\vartheta\}\oplus\mathbb Z/2\{\lambda\eta\}\)
is verified with \(\vartheta\) detected by \(P+Q\), these two
zero-boundary relations have no \(\vartheta\)-component. Their
operation vectors then give an odd determinant on the
\(\overline\alpha\nu,\lambda\eta\) pair even without separately
identifying the even \(\nu\)-coefficients. That final component group
has now passed the independent audits and the odd-determinant argument
is included in D.2.20.

## 6. Historical split-divisibility interface, and the corrected stronger route

**Update after the complete second-Bockstein audit.** The following
conditional argument was prepared for the initial group proposal.
The extra relation \(P_m+Z_A+P_n\) has zero first and second
Bocksteins and operation vector \((P+Q,z)\). Since \(H_8F\) has
exponent at most four, filtered integral normalization makes it a
zero-boundary nine-cell. It kills the remaining component
\(\vartheta\), after the \(\nu\) and \(\lambda\eta\) components
are removed. The \(P_n\) relation then kills \(2a_0\).
The corrected stable-group proposal is therefore \((\mathbb Z/2)^3\),
with one-dimensional mod-two Hurewicz kernel generated by \(a_0\).
The same \(\mathrm{Sq}^5\) instability excludes that nonzero kernel
class from actual sphere maps, giving actual Hurewicz injectivity.
The complete stable matrix has now passed all independent audits and
the stronger corrected calculation is included in D.2.20. The
conditional argument below remains valid but is no longer needed.

The following implication is exact and independent of a choice of
quadratic complement. Suppose the pending stable calculation gives

\[
L=\pi_8\Sigma^\infty F=\mathbb Z/4\{a_0\}\oplus(\mathbb Z/2)^2,
\qquad \ker(h_{\mathbb F_2}:L\to H_8F)=\langle a_0\rangle,
\]

and the stable cone of an odd multiple of \(a_0\) has nonzero
\(\mathrm{Sq}^5\) from its degree-four class to the new degree-nine
cell. Let \(I=\pi_8F\). The double-loop counit gives a split injection
\(I\hookrightarrow L\): \(F\to C_2F\) is split, and
\(C_2F\to QF\) is nine-connected, hence an isomorphism on \(\pi_8\).
Write \(r:L\to I\) for the group retraction.

An odd multiple of \(a_0\) cannot be an actual sphere map into \(F\),
because its ordinary mapping cone would violate instability of
\(\mathrm{Sq}^5\) on a degree-four cohomology class. Hence an actual
mod-two-Hurewicz-zero element is either zero or \(2a_0\). In the
latter case it is automatically an element of \(I\), and

\[
2a_0=r(2a_0)=2r(a_0)\in2I.
\]

Thus \(\ker(h_{\mathbb F_2}:I\to H_8F)=2I\). This is exactly the
divisibility needed to alter the remaining eight-cell nullhomotopy
in the source calculation. It requires neither a full computation
of \(I\) nor a chosen realization of every stable class.

## Opened primary formulas

CLM Chapter III, Theorem 1.3(2)--(5), printed pp.217--218, was visually
reopened from `FGH_CLM_114_right.png` and `FGH_CLM_115_left.png` during
this calculation. In particular the top Nishida correction for
\(n=1,q=4,r=2\) is exactly the partition \((0,2)\), hence
\(\{c,\mathrm{Sq}_*^2c\}\), with coefficient one. For \(r=4\) the
only nonzero binomial term is \(i=2\), and both possible nonlinear
partitions have a zero factor. The same pages give top-operation
additivity, internal Cartan, the formula for \(\beta\xi\), and
\(\lambda_n(x,\xi_ny)=\operatorname{ad}_n^2(y)(x)\), used in the
full basis and diagonal calculation.

