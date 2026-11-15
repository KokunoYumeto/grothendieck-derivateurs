# Stable hyperbolic unitary groups with nontrivial involution are MIF

**Status: proved, 14 November 2026; independently audited.** This is an
authored extension of the proof in `D_skew_linear_MIF.md`. It addresses the
proposed stable hyperbolic-unitary detecting target directly. It asserts no
inheritance of MIF by arbitrary subgroups of the displayed groups.

## 1. Statement and conventions

Let \(D\) be a division ring with an involution \(d\mapsto d^*\) which is not
the identity. Suppose the fixed subfield of its centre contains an infinite
field \(k\) of characteristic different from 2. Let \(\epsilon\in\{1,-1\}\).
On the right \(D\)-space with hyperbolic basis \(e_i,f_i\), put

\[
 h(e_i,f_j)=\delta_{ij},\qquad h(f_i,e_j)=\epsilon\delta_{ij},
 \qquad h(e_i,e_j)=h(f_i,f_j)=0,
\]

and use \(h(ud,ve)=d^*h(u,v)e\). Write \(U_\infty(D,*,\epsilon)\) for the
union of the isometry groups of finite hyperbolic blocks, embedded by the
identity on subsequent pairs. Write \(EU_\infty(D,*,\epsilon)\) for its
elementary hyperbolic unitary subgroup.

For every nontrivial reduced word
\(w\in U_\infty(D,*,\epsilon)*\langle x\rangle\), there exists
\(g\in EU_\infty(D,*,\epsilon)\) with \(w(g)\ne1\). In particular both
displayed groups are mixed-identity-free in one variable.

The statement applies to every division ring of characteristic zero with a
nontrivial involution, by taking \(k=\mathbb Q\). An involution on a
noncommutative division ring cannot be the identity, because an involution
reverses multiplication.

## 2. A diagonal detection lemma for sesquilinear forms

If a sesquilinear form \(B\) on a right \(D\)-space satisfies
\(B(v,v)=0\) for every \(v\), then \(B=0\).

Indeed expansion at \(v+w\) gives \(B(w,v)=-B(v,w)\). Expansion at \(vd+w\)
then gives

\[
 d^*B(v,w)=B(v,w)d\qquad(d\in D).
\]

If some \(z=B(v,w)\) were nonzero, this would give
\(d^*=zdz^{-1}\) for every \(d\). Thus the involution would also be an
automorphism. Comparing its action on a product in the two orders shows that
\(D\) is commutative. In a commutative division ring the displayed inner
automorphism is the identity, contrary to the hypothesis on \(*\).

Consequently, for any nonidentity linear map \(c\) on a finite nondegenerate
block, there is a vector \(v\) in that block with

\[
 h(v,(c-1)v)\ne0.
 \tag{1}
\]

To see this, apply the lemma to \(B(u,v)=h(u,(c-1)v)\). The form \(B\) is
nonzero by nondegeneracy of \(h\) and \(c\ne1\).

## 3. Polynomial elementary isometries detecting paired entries

Fix a finite old hyperbolic block containing the supports of all coefficients
of a word. Add a fresh hyperbolic pair \(e,f\). For a vector \(v\) in the old
block and \(t\in k\), define

\[
 \begin{aligned}
 S_v(t)e&=e+tv-f\,t^2h(v,v)/2,\\
 S_v(t)f&=f,\\
 S_v(t)z&=z-f\,t h(v,z)\qquad(z\text{ in the old block}).
 \end{aligned}
 \tag{2}
\]

The map fixes every other basis vector. Direct substitution into the form
shows that it is an isometry. For example the norm of the first displayed
vector is

\[
 t^2h(v,v)-t^2h(v,v)/2-\epsilon t^2h(v,v)^*/2=0,
\]

and
\(h(S_v(t)z,S_v(t)e)=t(h(z,v)-h(v,z)^*\epsilon)=0\).
The other pairings are unchanged. Direct substitution also gives
\(S_v(s)S_v(t)=S_v(s+t)\); hence its inverse is \(S_v(-t)\).
All matrix entries in (2), and those of its inverse, are polynomials in the
central variable \(t\).

These are elementary unitary isometries. Here is an explicit reduction to
the usual coordinate generators. Express \(v\) as a sum of multiples of
isotropic hyperbolic basis vectors in the old block. For such a single
summand (2) is a coordinate elementary unitary root transformation. For two
summands \(v,w\), the product \(S_v(1)S_w(1)\) differs from \(S_{v+w}(1)\)
only by the long-root transformation \(e\mapsto e+f a\), where

\[
 a=\bigl(h(w,v)-h(v,w)\bigr)/2,
 \qquad a+\epsilon a^*=0.
\]

That long-root transformation is also a coordinate elementary unitary
generator. Induction gives the claimed membership for every \(v\) and \(t\).

Let \(c\) be one of the nonidentity old-block coefficients, extended by the
identity on \(e,f\), and choose \(v\) satisfying (1). The coefficient in row
\(f\), column \(e\) of \(S_v(1)^{-1}cS_v(1)\) is

\[
 h(S_v(1)e,cS_v(1)e)
   =h(v,cv)-h(v,v)
   =h(v,(c-1)v)\ne0.
 \tag{3}
\]

Define the tail isometry \(W\) by \(We=f\), \(Wf=\epsilon e\), fixing the
old block. It commutes with \(c\). Conjugating the family (2) by \(W\) gives
a polynomial elementary family starting at the identity which detects the
opposite paired entry, in row \(e\), column \(f\). Its elementary membership
also follows directly by interchanging the two isotropic tail basis vectors
in the coordinate-generator reduction above; membership of \(W\) itself in
the elementary subgroup is not needed.

## 4. One simultaneous conjugation

For each nonidentity interior coefficient \(c_i\) of the reduced word, take
the two polynomial elementary families just constructed, one for each
paired off-diagonal entry. Form a product of all these families with
independent central parameters:

\[
 S(\mathbf t)=A_1(t_1)\cdots A_r(t_r).
\]

Every relevant entry of \(S(\mathbf t)^{-1}c_iS(\mathbf t)\) is a
\(D\)-valued polynomial. The two paired off-diagonal polynomials are nonzero:
set every parameter except that of its detecting family to zero, and that
parameter to one. Both diagonal-entry polynomials are nonzero as well,
because at \(\mathbf t=0\) both diagonal entries on the fresh pair equal 1.

For each of these finitely many nonzero \(D\)-valued polynomials, choose a
\(k\)-linear functional on the finite-dimensional \(k\)-span of its
coefficients which does not annihilate one nonzero coefficient. The resulting
scalar polynomial is nonzero. Their finite product is nonzero, so over the
infinite field \(k\) there is a common parameter value at which none vanishes.
Fix the resulting elementary isometry \(S\). Then for every \(i\), all four
entries in rows and columns \(e,f\) of \(c_i'=S^{-1}c_iS\) are nonzero.

## 5. An elementary hyperbolic torus

For \(q\in k^\times\), the isometry \(d(q)\) which multiplies \(e\) by \(q\),
\(f\) by \(q^{-1}\), and fixes the other basis vectors belongs to the
elementary subgroup.

For \(\epsilon=-1\), the central elementary matrices of \(SL_2(k)\) on this
pair are elementary isometries, and the standard elementary factorization
of \(\operatorname{diag}(q,q^{-1})\) applies.

For \(\epsilon=1\), choose \(\lambda\ne0\) with \(\lambda^*=-\lambda\);
such a scalar exists because the involution is nontrivial and 2 is invertible.
For a skew-adjoint scalar \(a\) the two matrices

\[
 U(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
 L(a)=\begin{pmatrix}1&0\\a&1\end{pmatrix}
\]

are elementary isometries of the hermitian hyperbolic pair. Both
\(\lambda\) and \(-\lambda^{-1}\) are skew-adjoint. Put

\[
 w(\lambda)=U(\lambda)L(-\lambda^{-1})U(\lambda)
   =\begin{pmatrix}0&\lambda\\-\lambda^{-1}&0\end{pmatrix}.
\]

Since \(q\) is fixed and central, multiplication gives

\[
 w(q\lambda)w(\lambda)^{-1}
    =\operatorname{diag}(q,q^{-1}).
\]

This proves elementary membership in both cases with an explicit morphism.

## 6. The Laurent coefficient which detects the word

Write a nontrivial reduced word involving the variable as

\[
 w(x)=c_0x^{a_1}c_1\cdots c_{m-1}x^{a_m}c_m,
 \qquad a_j\ne0,
\]

where every interior coefficient is nonidentity. A constant nontrivial word
already detects itself. Conjugate by the fixed \(S\) from Section 4 and
substitute the diagonal matrix \(d(t)\), with central indeterminate \(t\).
Let \(L=\sum_j|a_j|\), and set \(\eta_j=e\) for \(a_j>0\) and \(\eta_j=f\)
for \(a_j<0\). In

\[
 d(t)^{a_1}c_1'\cdots c_{m-1}'d(t)^{a_m},
\]

the coefficient of \(t^L\) is exactly

\[
 \left(\prod_{j=1}^{m-1}(c_j')_{\eta_j,\eta_{j+1}}\right)
 E_{\eta_1,\eta_m}.
\]

There is exactly one index path of this degree, since each diagonal factor
has a unique entry of maximal degree \(|a_j|\). Every factor in the displayed
ordered product is nonzero, so their product is nonzero in the division ring.
The invertible outer coefficients \(c_0',c_m'\) do not annihilate this leading
matrix coefficient. The evaluated word is therefore not the constant
identity matrix as a Laurent polynomial.

Choose a nonzero matrix entry of the difference from the identity and a
\(k\)-linear functional detecting one of its coefficients. The resulting
nonzero scalar Laurent polynomial vanishes at only finitely many points of
\(k^\times\). Thus some \(q\in k^\times\) gives

\[
 w(Sd(q)S^{-1})\ne1.
\]

The element \(Sd(q)S^{-1}\) lies in the elementary hyperbolic unitary group,
as required. This completes the proof.

## 7. Exact relevance and primary-source boundary

The proposed whole stable hyperbolic unitary group over a countable
noncommutative division ring with involution is therefore in the MIF target
class already excluded by A.27--A.28. No embedding of the actual Higman-based
homology core in a division ring is used or asserted in this deduction; it
is an obstruction to the proposed whole detecting group itself. No
conclusion about an arbitrary simple subgroup follows merely from its
inclusion in that ambient group.

The primary preprint Bradford--Ersoy--Schneider--Thom, *Mixed identities for
simple locally finite groups*, arXiv:2608.14537,
<https://arxiv.org/pdf/2608.14537>, Theorem 5.16 and Section 5.2.3, treats
finitary symplectic groups over **infinite locally finite commutative fields**.
Those fields have trivial involution in the symplectic form. Its stated
classification does not give a mixed identity over a noncommutative division
ring with involution. The proof above supplies the exact contrary MIF
conclusion for the latter stable hyperbolic-unitary class. The distinction
is witnessed by the diagonal-detection calculation in Section 2: for a
commutative field with identity involution, nonzero alternating bilinear
forms have zero diagonal, so that step does not apply.

This result supplies no fixed countable solver for arbitrary countable
systems with invertible relative exponent matrix. That remains the first
unproved step of the proposed detecting-target route.

## 8. Independent audit record

The C agent read the complete note and checked every pairing in (2), the
additive one-parameter law, the coefficient in (3), the coordinate-root and
long-root factorization, the opposite family's elementary membership, the
finite scalar-polynomial avoidance, both torus factorizations, and the
ordered leading Laurent coefficient over a division ring. The audit found
no gap. The one-variable conclusion is exactly Property 1 used in A.27;
no further change of the target class is required.
