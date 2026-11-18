# The universal Moore-space composition behind the k4 test

Status: 2026-11-16, after checkpoint 14. Sections 1--8 support
D.2.44; Section 13 is the sharper cyclic-span result of D.2.46.
The initially omitted Hopf--Hilton correction is included and shown
to vanish below. The actual target generator q and its double have
not been evaluated. The intervening Lemma 5.3 and coextension
calculations retain their exact scopes; Sections 14--15 record the
primary-composition boundary and one new Moore-four nu-composite.

## 1. The actual universal map and its exact double

Write \(P_n=M(\mathbb Z/2,n-1)\), with bottom inclusion
\(i_n:S^{n-1}\to P_n\). Let \(j:P_5\to Y=\Sigma^2K(\mathbb F_2,2)\)
be the bottom Moore map. Naturality of the generalized Whitehead product
gives an actual factorization

\[
w=[i_5,\mathrm{id}_{P_5}]:
\Sigma(S^3\wedge P_4)=P_8\longrightarrow P_5,
\qquad h_M=jw.
\]

This uses the same generalized-Whitehead convention as D.2.29 and
D.2.41. In particular \(w i_8=i_5[\iota_4,\iota_4]\).

Morisugi--Mukai, Lemma 2.8(ii), printed p.523, gives

\[
\pi_{14}P_8=
\mathbb Z/4\{l_4\}\oplus\mathbb Z/2\{\widetilde{\nu_7^2}\},
\qquad 2l_4=i_8\sigma'.
\]

Consequently the universal and target doubles are exactly

\[
2(wl_4)=i_5\bigl([\iota_4,\iota_4]\sigma'\bigr),
\qquad
2(h_Ml_4)=u_4\bigl([\iota_4,\iota_4]\sigma'\bigr).
\]

These identities use postcomposition on homotopy groups, which is a
homomorphism. They do not distribute precomposition over a sum of
maps without checking its Hopf--Hilton correction. The established
target convention rewrites the second identity as
\((-2\alpha)\sigma'\), as in D.2.41. Neither this identity nor
the source order four determines the value of the composite.

The suspension of \(w\) is null because it is a generalized
Whitehead product. Thus \(wl_4\) is in the actual suspension kernel
of \(\pi_{14}P_5\). This observation does not identify that kernel
with the metastable quadratic kernel: \(P_5\) is only
three-connected, and degree fourteen is outside that comparison range.

## 2. What the already opened Moore-space sources provide

The original Morisugi--Mukai PDF was reopened, with Lemma 2.8 on
printed p.523 inspected visually:

<https://www.jstage.jst.go.jp/article/jmath1948/52/3/52_3_515/_pdf>.

Its Lemma 1.2, printed p.517, gives the James relative exact sequence
only for \(r\leq3n-4\). For \(P_5\) this is \(r\leq11\).
It therefore cannot be used without further work to calculate
\(\pi_{14}(P_5,S^4)\) or the universal composite above.

The existing local scan `FGH_Mukai2001.pdf`, *Generators of some
homotopy groups of the mod 2 Moore space of dimension 3 or 5*,
Kyushu J. Math. 55 (2001), 63--73, was checked again at printed
pp.63--65. Its Theorem 1.2 lists \(\pi_{10},\ldots,\pi_{13}\)
of \(P_5\), not \(\pi_{14}P_5\). In particular it is not an
already available table evaluating the requested composition.

## 3. A concrete three-cell fiber route

Let \(F_5\) be the homotopy fiber of the pinch
\(P_5\to S^5\). Its cells begin in dimensions \(4,8,12,16\),
and its two-cell skeleton is

\[
F_5^{(2)}=S^4\cup_{2[\iota_4,\iota_4]}e^8.
\]

Since the pinch kills the bottom inclusion, it kills the generalized
product \(w\). Thus \(w\) lifts to \(F_5\), and cellular
approximation puts a chosen lift in \(F_5^{(2)}\). Its composite
with \(l_4\) can be studied in the three-cell skeleton
\(F_5^{(3)}\): the next cell has dimension sixteen, so that
\(\pi_{14}F_5^{(3)}\to\pi_{14}F_5\) is an isomorphism.
Passing from the fiber to \(P_5\) must still quotient by the
actual connecting image from \(\pi_{15}S^5\); nonzero in the
fiber alone is not sufficient.

A current primary source addresses exactly this missing third cell:

Juxin Yang, Fengchun Lei, Jie Wu, *A “Periodicity” Phenomenon for
Attaching Maps of Suspended Two-Cell Complexes*,
arXiv:2509.21444v8, 17 October 2026:
<https://arxiv.org/pdf/2509.21444>.

Theorem 1.1 / Theorem 8.6.1, printed pp.3 and 40, determine the
third-cell attachment up to an explicitly retained subgroup
\(I\circ\Sigma^{2n+k+2}f\). Here one takes
\(n=3,k=0,f=2\iota_3\), so the third cell is in dimension
twelve and the formula is a main degree-two term modulo \(2I\).
The mod-two cup hypothesis holds for the Moore source.

Theorem 9.1, printed p.43, also applies to degree fourteen under
its extended-range hypothesis: the relevant suspension is
\(\pi_{13}S^7\to\pi_{14}S^8\), which is injective on the
\(\nu^2\) group. It supplies a finite computational framework;
it does not itself state the value of \(wl_4\). The component
of the specified lift and the connecting homomorphism still require
an actual calculation.

The version matters. Indexed excerpts from the older 2025 version
state an equality with the main third-cell term. The opened v8
explicitly includes the indeterminacy \(2I\). That term must not
be discarded in a computation of this composition.

## 4. The actual third cell has no two-primary ambiguity

The original Mukai paper gives a stronger, exact answer in this
particular example than the general 2026 theorem. Lemma 4.1(iii),
printed p.69, states

\[
\pi_{11}A_5=\mathbb Z\{\tau_5\}
 \oplus\mathbb Z/4\{\widetilde{2\nu_7}\}
 \oplus\mathbb Z/15\{i\phi\},
\qquad j_*\tau_5=3[\gamma_8,\iota_4].
\]

Here \(A_5=S^4\cup_{2[\iota_4,\iota_4]}e^8\), \(j\)
is the map to its relative homotopy group, and \(\gamma_8\)
is the characteristic relative eight-cell. Lemma 5.1(i), printed
p.70, proves

\[
\theta_5=2\tau_5+a i\phi,\qquad
\phi\in\pi_{11}S^4\cong\mathbb Z/15.
\]

Consequently, at the prime two the actual three-cell fiber is

\[
B_5=A_5\cup_{2\tau_5}e^{12}.
\]

The proof explicitly excludes a component in
\(\mathbb Z/4\{\widetilde{2\nu_7}\}\): its suspension would
give a nonzero multiple of \(2\nu_9\), whereas the actual fiber
attachment suspends to zero. Thus this is an exact normalization,
not a choice to discard the \(2I\) indeterminacy in the general
theorem. Printed pp.69--72 were visually inspected in the original
scan on 15 November 2026:

<https://www.jstage.jst.go.jp/article/kyushujm/55/1/55_1_63/_pdf>.

## 5. A relative Jacobi reduction, including the Hilton correction

**Audit history and repair.** The parent identified a gap in the original
comparison in this section. Although the two maps differ through
the pinch and \(p_8l_4=0\), precomposition by \(l_4\) is not
additive on the mapping group. A mixed Hopf--Hilton correction can
occur in dimension fourteen. The first draft omitted it. The explicit
Hilton--Milnor range and Jacobi calculation below now show that this
correction is zero; the original shortcut is not used.

Choose the map of cofibers

\[
c:P_8\longrightarrow A_5
\]

induced by the commutative square with top map
\(2:S^7\to S^7\), bottom attachment
\(2[\iota_4,\iota_4]:S^7\to S^4\), left map the identity,
and right map \([\iota_4,\iota_4]\). Thus \(c\) has
bottom map \([\iota_4,\iota_4]\) and relative top degree one.
Its composite into \(P_5\) and the actual generalized Whitehead
map \(w\) agree on the bottom sphere. The Moore Puppe sequence
therefore says that they differ by a map through the pinch
\(p_8:P_8\to S^8\).

The same Morisugi--Mukai Lemma 2.8(ii) gives
\(j_*l_4=[\gamma_8,\iota_7]\). Applying the pinch kills the
absolute bottom entry, so \(p_8l_4=0\). This does **not** by
itself imply \(wl_4=(A_5\to P_5)cl_4\): the possible mixed
correction involves the bottom map \(i_5[\iota_4,\iota_4]\)
and the top-sphere difference \(h:S^8\to P_5\).

Here is the required correction calculation. Write \(P_8=\Sigma P_7\)
and apply Hilton--Milnor to
\(\Omega\Sigma(P_7\vee P_7)\) through degree fourteen.
The singleton factors give the two ordinary composites; the only
other possible factor is \(\Sigma(P_7\wedge P_7)\), whose
bottom cell is in degree thirteen. Factors of word length three
start in degree nineteen and cannot contribute. Since the second
map is \(hp_8\), the mixed factor further maps through

\[
\Sigma(P_7\wedge S^7)\simeq P_{15}.
\]

Its degree-fourteen homotopy group is its bottom
\(\mathbb Z/2\), by Hurewicz. Thus the entire possible mixed
correction is \(\epsilon[\alpha,h]\), where
\(\alpha=i_5[\iota_4,\iota_4]=[u,u]\), \(u=i_5\),
and \(\epsilon\in\mathbb F_2\). Naturality of the generalized
Whitehead map identifies the bottom representative with exactly
this ordinary Whitehead product. There is no additional top-top
term in degree fourteen, and the higher Hilton factors are outside
the range just stated.

The shifted degree of \(u\) is three, hence odd. The graded
Jacobi identity and bilinearity give

\[
[[u,u],h]=\pm2[u,[u,h]]
 =\pm[2u,[u,h]]=0,
\]

because \(2u=0\) in the actual bottom Moore homotopy group.
Consequently all the Hilton correction terms vanish and the needed
equality is valid:

\[
wl_4=(A_5\longrightarrow P_5)cl_4.
\]

Naturality of the relative Whitehead product gives

\[
j_*(cl_4)=[\gamma_8,[\iota_4,\iota_4]].
\]

Only one relative class occurs in the next identity. The mixed
relative Whitehead module satisfies the Jacobi derivation law.
Its shifted degrees here are \(7\) for \(\gamma_8\) and
\(3\) for \(\iota_4\); the two Jacobi terms have the same
sign. Hence, up to the common orientation convention,

\[
[\gamma_8,[\iota_4,\iota_4]]
 =2[[\gamma_8,\iota_4],\iota_4],
\qquad
3j_*(cl_4)=j_*[2\tau_5,\iota_4].
\]

For a primary source, I. M. James, *Products between homotopy
groups*, Compositio Math. 23 (1971), 329--345, §4, printed
p.337, equations (4.1)--(4.2), proves the mixed relative Samelson
Jacobi law. The usual loop-group model of a CW pair identifies
this with the relative Whitehead module law used here. This is
not a bracket of two arbitrary relative classes and has no
metastable range restriction. The original displayed equations
were visually checked:

<https://www.numdam.org/item/CM_1971__23_3_329_0.pdf>.

In \(B_5\), the absolute class \(2\tau_5\) is zero by the
actual twelve-cell attachment. Thus the image of
\(3j_*(cl_4)\) in \(\pi_{14}(B_5,S^4)\) is zero. Since
three is invertible at the prime two, exactness of the pair gives

\[
wl_4=(A_5\longrightarrow P_5)cl_4\in
\operatorname{im}\bigl(i_{5*}:\pi_{14}S^4_{(2)}
 \longrightarrow\pi_{14}P_{5,(2)}\bigr).
\]

This reduces the actual universal composite to a bottom-sphere
element. It does not determine the element or its image in \(Y\).
The parent supplied the essential correction-vanishing observation;
the explicit range/factorization and both Jacobi parity calculations
were independently checked by this author. The fibrations agent
independently checked the relative Jacobi step.

## 6. Boundary of the present check

No opened primary formula in this check evaluates
\([i_5,\mathrm{id}]l_4\) or its image under \(j\).
The universal factorization, its double, the exact three-cell fiber,
and the bottom-sphere reduction for the actual generalized Whitehead
map are rigorous. The value of the remaining bottom-sphere class
is a further computation, not a claimed solution. In particular the exact
remaining James--Hopf image problem of D.2.43 is unchanged.

## 7. The exact sphere table and the suspension-test boundary

The primary table, also displayed in Kachi--Mukai (2000), printed
p.92, is

\[
\pi_{14}S^4_{(2)}=
 \mathbb Z/8\{\nu_4\sigma'\}\oplus
 \mathbb Z/4\{E\epsilon'\}\oplus
 \mathbb Z/2\{\eta_4\mu_5\}.
\]

The author's note by N. P. Strickland, *A Mathematica representation
of some unstable homotopy groups of spheres*, Proposition 7,
printed p.7, explicitly states this table and the suspension formulas

\[
 E(\nu_4\sigma')=\pm E^2\epsilon'
   =2\nu_5\sigma_8,
 \qquad E(\eta_4\mu_5)=\eta_5\mu_6.
\]

Proposition 13, printed pp.8--9, proves
\((E\nu')\sigma'=2E\epsilon'\). The generic
Hopf-composite formula mentioned in that note has an explicit warning;
this particular proof does not require its unqualified version.
The factor \(E\nu'\) is a suspension. For \(\nu_4\sigma'\)
one may first suspend the Hopf formula and use injectivity of
\(E:\pi_{14}S^7\to\pi_{15}S^8\); both \(\sigma'\)
and \(E\sigma'\) have order eight. The correction is
\(\nu_7\nu_{10}\eta_{13}=0\). The fibrations agent's complete
independent source audit is `EH5_pi14S4_primary_audit.md`.

Original author sources opened on 15 November 2026:

- <https://strickland1.org/toda/toda.pdf>, Propositions 7 and 13.
- <https://strickland1.org/toda/Toda.m>, the relation
  \([\iota_5,\iota_5]=\nu_5\eta_8\), attributed there
  to Toda, equations (5.10). The original Toda page has not been
  opened in this check.

The known actual relations \(u_4\eta_4=0\),
\(\alpha=u_4\nu_4\), \(4\alpha=0\), and
\([u_4,u_4]=-2\alpha\) imply

\[
 u_4E\nu'=2\alpha-[u_4,u_4]=4\alpha=0,
 \qquad 2u_4E\epsilon'=u_4(E\nu')\sigma'=0.
\]

Thus the target composite belongs to the subgroup generated by
\(\alpha\sigma'\) and the at-most-order-two class
\(u_4E\epsilon'\). Neither coefficient has been determined.
In particular, killing the \(\eta_4\mu_5\) term does not
evaluate the remaining two terms.

There is also an exact reason that suspension-zero cannot separate
these two coefficients. Let \(i_6:S^5\to P_6\) be the bottom
inclusion. The degree-two composite calculation gives

\[
 (2\iota_5)\nu_5\sigma_8
 =\nu_5(2\iota_8)\sigma_8
 =2\nu_5\sigma_8+[\nu_5,\nu_5].
\]

The first equality uses that \(\nu_5\) is a suspension. For
the second, the Hopf invariant of \(\sigma_8\) is one and
there are no higher Hilton terms in its dimension. Naturality gives

\[
 [\nu_5,\nu_5]
 =\pm[\iota_5,\iota_5]\,\Sigma(\nu_4\wedge\nu_4)
 =\pm\nu_5\eta_8\nu_9\nu_{12}=0,
\]

since \(\eta_8\nu_9\) lies in the zero stable fourth stem.
Since \(i_6(2\iota_5)=0\), it follows that

\[
 i_6(2\nu_5\sigma_8)=0,
 \qquad E(i_5\nu_4\sigma')=E(i_5E\epsilon')=0.
\]

Both candidate bottom images therefore suspend to zero separately.
The already known \(E(wl_4)=0\) imposes no relation between
their coefficients. This calculation keeps the sphere representative
separate from its image in the Moore space; it does not replace
\(E(i_5\delta)=0\) by the stronger and unjustified assertion
\(E\delta=0\).

## 8. Manuscript and final independent audit

D.2.44 is saved in `sections/D2_universal_moore.tex` and registered
with the sole FGH row. It states three separate proved assertions:
the actual bottom-image reduction, the two-term target span, and
the exact failure of the suspension test to choose a coefficient.
It makes no claim about the numerical composite or full extension.
The parent independently read the repaired Hilton/Jacobi note and
opened the original Mukai and James passages. The simple-higher agent
read the full final TeX and independently checked the suspension
indices and the stable-fourth-stem vanishing. The fibrations agent
independently opened the Strickland statements and their required
Hopf-formula qualification; its source audit is retained separately.

## 9. Removing the tau ambiguity in Mukai's Lemma 5.3

Checked at 23:34 UTC on 15 November 2026. This is a further exact
calculation, independently passed by the fibrations agent. It does
not evaluate the bottom representative in Section 5.

Write \(v=\widetilde\eta_4:S^6\to P_5\) and
\(z=\widetilde{2\nu_7}\in\pi_{11}A_5\), with the normalization
of Mukai, Lemma 4.1(iii). The original Lemma 5.3, printed p.71,
states

\[
 [v,v]\equiv i_*z\pmod {i_*\tau_5}.
\]

Here \(i:A_5\to P_5\) is the pinch-fiber map. Its image
\(i_*\tau_5\) has order two: the actual twelve-cell kills
\(2\tau_5\), and the homology computation below shows that
its image is nonzero. We prove that the displayed congruence is
the exact equality

\[
 [v,v]=i_*z. \tag{9.1}
\]

Use the integral Adams--Hilton model

\[
 \mathcal A(A_5)=T(a_3,c_7),\qquad da=0,\quad dc=4a^2.
\]

Indeed, the loop Hurewicz image of \([\iota_4,\iota_4]\)
is \([a,a]=2a^2\), so the attachment \(2[\iota_4,\iota_4]\)
has image \(4a^2\). In degree ten the only words are
\(ac,ca\), with differentials \(-4a^3,4a^3\); there are
no degree-eleven words. Therefore

\[
 H_{10}(\Omega A_5;\mathbb Z)=\mathbb Z\{ac+ca\}. \tag{9.2}
\]

The relative chain quotient by \(T(a)\) has the two independent
degree-ten classes \(ac,ca\). The relative Samelson Hurewicz
image of \([\gamma_8,\iota_4]\) is \(ca+ac\), since
the loop degrees seven and three are both odd. Thus the exact
relative normalization \(j_*\tau_5=3[\gamma_8,\iota_4]\)
forces

\[
 h_{\mathbb Z}(\tau_5)=\pm3(ac+ca).
\]

The sign depends only on the common cell orientation and is
irrelevant after reduction modulo two. The torsion class \(z\)
has zero integral Hurewicz image by (9.2), and hence also zero
mod-two Hurewicz image. This last implication is applied to a
spherical class, so it follows directly by naturality of
coefficient reduction; it does not assert that all mod-two
homology comes from integral homology.

Now \(P_5=\Sigma P_4\), so
\(H_*(\Omega P_5;\mathbb F_2)=T(a_3,b_4)\). The image of
\(c\) is \(ab+ba\). To check this without an implicit
choice of the top nullhomotopy, compare the map of cofibers
\(P_8\to A_5\to P_5\) with the actual generalized
Whitehead map \(w\). They differ through an actual
\(h:S^8\to P_5\). The top homology class of the adjunct
of \(w\) is \(ab+ba\). Mukai's Lemma 4.2, printed p.69,
gives

\[
 \pi_8P_5=\mathbb Z/2\{\widetilde\eta_4\eta_6^2\}
  \oplus\mathbb Z/2\{i_5\nu_4\eta_7\}.
\]

Both generators have zero once-loop Hurewicz image in degree
seven. For the first, the final \(\eta_6^2\) is a suspension
and the adjunct factors through \(S^5\); for the second,
\(\eta_7\) is a suspension and the adjunct factors through
\(S^6\). Consequently the top-sphere ambiguity cannot alter
the degree-seven homology image. It follows that

\[
 h_{\mathbb F_2}(i_*\tau_5)
 =a(ab+ba)+(ab+ba)a=a^2b+ba^2\ne0. \tag{9.3}
\]

On the other hand, the adjunct of \(v\) has degree-five
Hurewicz image zero because \(H_5\Omega P_5=0\). The
Hurewicz image of its Samelson square is consequently zero.
In the congruence of Lemma 5.3 the \(i_*z\) term also has
zero Hurewicz image, while the possible \(i_*\tau_5\)
term has the nonzero image (9.3). Its integer coefficient must
therefore be even. Since the actual twelve-cell gives
\(2i_*\tau_5=0\), its contribution is zero, proving (9.1).

Finally, the actual Moore coextension \(v\) maps to zero in
\(Y\). The low Chang calculation retained in
`EH5_next_browder_square.md`, Section 1, gives
\(\pi_6Y=\mathbb Z/2\) with injective integral Hurewicz
image \(2c\in H_6Y=\mathbb Z/4\); the Moore coextension
has zero ordinary integral Hurewicz image and is killed by the
two seven-cells. Naturality of (9.1) therefore gives

\[
 j_*i_*\widetilde{2\nu_7}=0\in\pi_{11}Y. \tag{9.4}
\]

This does not identify \(cl_4\) with a composition involving
\(\widetilde{2\nu_7}\). In particular, a vanishing pinch
after composing the coextension with \(\nu_{11}\) does not
by itself put that composite in the bottom-sphere image: mixed
relative terms are present in this dimension. No such inference
is used here.

### Exact source interface for the integral chain calculation

The original Mukai scan was visually reopened at printed p.71
for Lemma 5.3; pp.69--70 give the group, relative coefficient,
and actual twelve-cell already checked above. The integral
Adams--Hilton construction and attaching-map Hurewicz rule were
also directly opened in the primary paper of K. Hess, P.-E.
Parent, J. Scott, and A. Tonks, *A canonical enriched Adams--Hilton
model for simplicial sets*, arXiv:math/0408216v2, Introduction,
printed pp.1--2:
<https://arxiv.org/pdf/math/0408216>.
That passage uses a free graded **integral** module, states the
skeletal quasi-isomorphisms, and identifies each differential
with the Hurewicz class of the attaching adjunct. Its warning
about choices of map models is respected by the explicit
\(\pi_8P_5\) comparison above. The original 1956
Adams--Hilton paper itself has not been opened in this check.

The parent independently reopened Mukai pp.69 and 71 and passed
the sharpening, explicitly checking the even-coefficient step
against the actual relation \(2i_*\tau_5=0\).

## 10. The nu-composite is a bottom image, with its coefficient retained

There is a valid additional argument for the composite that the
zero-pinch observation at the end of Section 9 did not establish.
Mukai's proof of Lemma 4.1(ii), printed p.69, explicitly gives

\[
 \pi_{11}(A_5,S^4)_{(2)}
 =\mathbb Z_{(2)}\{[\gamma_8,\iota_4]\}
   \oplus\mathbb Z/8\{\widehat\nu_7\}.
\]

The canonical relative composition \(\gamma_8\nu_8\)
generates the torsion summand, up to an odd unit. To see that it
has no unnoticed free component, identify this relative group
with \(\pi_{10}\operatorname{hofib}(S^4\to A_5)\).
The characteristic relative cell is an actual
\(S^7\to\operatorname{hofib}(S^4\to A_5)\). Its
postcomposition homomorphism sends \(\nu_7\), of order eight,
to the class in question. The pinch of that class is \(\nu_8\),
also of order eight. Thus its order is exactly eight and it is
a torsion generator in the displayed direct sum.

The coextension \(z=\widetilde{2\nu_7}\) has order four,
so \(j_*z\) is torsion. Its pinch is \(2\nu_8\), and
the pinch is injective on the displayed relative torsion
summand. With matching normalization,

\[
 j_*z=2\gamma_8\nu_8.
\]

Now compose with \(\nu_{11}\). In the homotopy-fiber model
this is ordinary precomposition with \(\nu_{10}\), and

\[
 2\nu_7\nu_{10}=0\in\pi_{13}S^7_{(2)}.
\]

This is the standard order-two \(\nu^2\) class; the
suspension in this degree is an isomorphism because the
Whitehead square of \(S^7\) is zero. Hence

\[
 j_*(z\nu_{11})=0,\qquad
 z\nu_{11}\in\operatorname{im}\bigl(
  \pi_{14}S^4_{(2)}\longrightarrow\pi_{14}A_5\bigr). \tag{10.1}
\]

The argument uses the entire relative torsion summand and the
actual homotopy-fiber composition. It therefore controls the
mixed relative terms that a zero pinch alone would miss. The
fibrations agent independently checked this exact interface.

Combining (10.1) with (9.4) gives a bottom-sphere relation that
vanishes in \(Y\). It does not yet evaluate its coefficients
in \(\nu_4\sigma',E\epsilon',\eta_4\mu_5\), nor compare
that representative with the different bottom class producing
\(wl_4\). Those are the remaining concrete composition
questions; no identification between them is asserted.

## 11. Exact evaluation of the coextension-nu comparison

The remaining coefficient in (10.1) can be evaluated. This
calculation was independently passed by the fibrations agent;
it closes the coextension comparison without determining the
different class \(wl_4\).

All groups in this section are localized at two. The cone
definition of the Toda bracket identifies a bottom
representative of \(z\nu_{11}\), up to the common sign,
with an element of

\[
 \{2\omega_4,2\nu_7,\nu_{10}\}\subseteq\pi_{14}S^4.
 \tag{11.1}
\]

Here the chosen coextension \(z\in\{i,2\omega_4,2\nu_7\}\)
uses the same nullhomotopy of \((2\omega_4)(2\nu_7)\).
The other nullhomotopy is that of \(2\nu_7\nu_{10}=0\).
Equivalently, choose the extension of \(2\omega_4\) over
\(C(2\nu_7)\) and compose it with the coextension of
\(\nu_{10}\). The two mapping-cone constructions give the
usual coextension-composition identity after the inclusion
\(S^4\to A_5\). Its ordinary indeterminacy is

\[
 (2\omega_4)\pi_{14}S^7+
             (\pi_{11}S^4)\nu_{11}
       =(2\omega_4)\pi_{14}S^7,
\]

since \(\pi_{11}S^4_{(2)}=0\). The inclusion into \(A_5\)
kills this indeterminacy by the defining cell attachment.

First calculate the smaller bracket

\[
 \{4\iota_7,2\nu_7,\nu_{10}\}
                 =\langle4\sigma'\rangle. \tag{11.2}
\]

The bracket \(\{4\iota_3,\nu',\nu_6\}\) is defined:
\(4\nu'=0\) at two, and \(\nu'\nu_6\) is in
\(\pi_9S^3_{(2)}=0\). The degree-four map acts as
multiplication by four here because \(S^3\) is an H-space;
this is not an unverified distributivity assertion.
Its Toda bracket lies in \(\pi_{10}S^3_{(2)}=0\).
Suspend four times and use \(E^4\nu'=2\nu_7\).
Thus the bracket in (11.2) contains zero. Its indeterminacy is
\(4\pi_{14}S^7+(\pi_{11}S^7)\nu_{11}
=\langle4\sigma'\rangle\), since \(\pi_{11}S^7=0\).
This proves (11.2), not merely a stable version of it.

To carry out the first-variable sum with compatible choices,
put

\[
 C=C(2\nu_7)=\Sigma C(2\nu_6),
 \qquad \varphi:S^{14}\longrightarrow C
\]

for a coextension of \(\nu_{10}\). Extend \(4\iota_7\)
to \(F_0:C\to S^7\). By (11.2) choose the one common
\(\varphi\) so that \(F_0\varphi=0\).
Also extend \(E\nu'\) to \(F_1:C\to S^4\). This
extension exists because \((E\nu')\nu_7=0\). The defining
Toda bracket for \(\epsilon'\), suspended once, gives

\[
 F_1\varphi\in E\epsilon'
                       +\langle2E\epsilon'\rangle.
\]

Indeed its indeterminacy is
\((E\nu')\pi_{14}S^7+(\pi_{11}S^4)\nu_{11}
=\langle(E\nu')\sigma'\rangle
=\langle2E\epsilon'\rangle\).
This statement holds for the same \(\varphi\) that made
\(F_0\varphi=0\); changing the shared nullhomotopy only
changes the indicated coset. Consequently
\(-2F_1\varphi=-2E\epsilon'\).

Define \(F=\nu_4F_0-2F_1:C\to S^4\), using the
co-H structure of \(C\). Its bottom map is
\(4\nu_4-2E\nu'=2\omega_4\). The precomposition
by \(\varphi\) again requires a Hilton check. The
desuspended cone has cells six and ten, so its only mixed
Hilton factor through degree fourteen is the bottom
\(S^{13}\); the next mixed cells have dimension seventeen.
Thus the mixed correction is a multiple of

\[
 [4\nu_4,-2E\nu']\eta_{13}
                 =-8[\nu_4,E\nu']\eta_{13}=0.
\]

For the self-correction in doubling \(F_1\), one has
\([E\nu',E\nu']=(E\nu')_*[\iota_7,\iota_7]=0\),
since \(S^7\) is an H-space. There are no higher terms in
this dimension. It follows, with these actual choices, that

\[
 F\varphi=-2E\epsilon',\qquad
 z\nu_{11}=i_*(\pm2E\epsilon')\in\pi_{14}A_5.
 \tag{11.3}
\]

The sign is immaterial because \(2E\epsilon'\) has order
two. Thus the bottom relation supplied by this coextension
comparison is precisely one already killed in \(Y\):
\(2u_4E\epsilon'=0\). It supplies no new relation on
\(\alpha\sigma'\) and does not choose the coefficients
of the universal composite in D.2.44.

For the exact low sphere groups used in the desuspension,
Toda's original *Topology of Standard Path Spaces and Homotopy
Theory. I*, Proc. Japan Acad. 29 (1953), 299--304,
Proposition 3 on printed p.303, was opened and visually
checked on 15 November 2026:
<https://www.jstage.jst.go.jp/article/pjab1945/29/7/29_7_299/_pdf/-char/en>.
It gives \(\pi_9S^3=\mathbb Z/3\) and
\(\pi_{10}S^3=\mathbb Z/15\). The same zero two-primary
groups and the relation \(\nu'\nu_6=0\) appear in the
opened Strickland author program. The defining bracket for
\(\epsilon'\) is explicitly stated on printed p.4 of
Strickland's note, with the original Toda Chapter VI(iv)
locator; that book chapter has not been opened here.

There is one further exact simplification of Section 1's
double relation. For \(\alpha:S^7\to Y\),
\([\alpha,\alpha]=\alpha_*[\iota_7,\iota_7]=0\).
The Hilton formula through degree fourteen therefore makes
precomposition by \(\sigma'\) additive on the cyclic
subgroup generated by \(\alpha\). Accordingly

\[
 2(h_Ml_4)=(-2\alpha)\sigma'=-2(\alpha\sigma').
\]

This is now justified, but neither side has been evaluated
in the full target.

## 12. Remaining coefficient search: exact source boundary

Status at 23:52 UTC, 15 November 2026. The coextension--nu
comparison in Section 11 is closed. The current question is the
coefficient of the different actual map
\([i_5,\mathrm{id}_{P_5}]l_4\), after the bottom-image reduction
of D.2.44. Neither the double relation nor suspension-zero chooses
that coefficient.

A targeted primary-source search did not locate an opened table or
component formula for \(\pi_{14}P_5\). In particular, the original
contents of Jie Wu's 2003 *Homotopy Theory of the Suspensions of the
Projective Plane*, Memoirs AMS 162, no.769, were opened at
<https://www.gbv.de/dms/goettingen/356720632.pdf>. Chapter 5 advertises
the groups \(\pi_{n+r}(\Sigma^n\mathbb RP^2)\) for \(r\leq8\),
and its P5 subsection starts on printed p.67. That advertised range
does not include \(\pi_{14}P_5\). The body of that subsection was
not opened, so this is a scope check, not a claim that the book
contains no further relevant statement. The opened Mukai 2001
tables, Oka 1988 relative calculations, and the modern relative
James-construction computational framework likewise supply no
already evaluated coefficient for this map.

The general mixed relative Jacobi identity has already been used
with its full legitimate consequence: it places the map in the
bottom sphere image after the actual twelve-cell attachment. A
stronger conclusion would need a choice-compatible secondary
identity for the bottom remainder, or an explicit component
calculation in \(\pi_{14}P_5\). It cannot be obtained by treating
the relative Jacobi equality as an absolute equality, nor by
discarding the coherent Hilton term on the two-Moore smash.

No new numerical value or vanishing assertion is added by this
source search. The still available exact target description is
the two-component span in D.2.44, together with
\(2(h_Ml_4)=-2(\alpha\sigma')\); the full-target integral
fifteen-cell test is recorded separately in D.2.45.

## 13. A stronger sphere-kernel constraint before passing to P5

This argument improves Section 12's boundary; it does not infer a
sphere suspension from suspension in P5. The parent independently
checked the before-P5 interface on 15 November 2026.

Retain the actual map \(c:P_8\to A_5\), bottom \(\omega_4\),
and the relative identity already proved in Section 5. In the pair
\((A_5,S^4)\), it gives

\[
 j_*\bigl(3cl_4-2[\tau_5,i_4]\bigr)=0.
\]

Consequently there is an actual sphere class
\(\delta_0\in\pi_{14}S^4_{(2)}\) such that

\[
 i_*\delta_0=3cl_4-2[\tau_5,i_4]\in\pi_{14}A_5.
 \tag{13.1}
\]

The suspension of each term on the right is zero. This is immediate
for the Whitehead product. For the other term, the restriction of
\(\Sigma c:P_9\to\Sigma A_5\) to its bottom sphere is
\(E\omega_4=0\). The actual Moore cofibration therefore makes
\(\Sigma c\) factor through the pinch \(p_9:P_9\to S^9\).
Morisugi--Mukai's exact formula is
\(El_4=i_9[\iota_8,\iota_8]\), whose composite with that pinch
is zero. Thus \(E(cl_4)=0\). Moreover
\(\Sigma A_5\simeq S^5\vee S^9\), because its attaching map
is \(E(2\omega_4)=0\). The inclusion of the bottom S5 has a
retraction. Suspending (13.1) and applying that retraction proves

\[
 E\delta_0=0\quad\hbox{in }\pi_{15}S^5_{(2)}.
 \tag{13.2}
\]

This is the essential improvement over suspension in P5. The
subsequent actual twelve-cell kills \(2\tau_5\); hence after
mapping to P5,

\[
 3wl_4=i_{5*}\delta_0.
 \tag{13.3}
\]

The exact sphere kernel is already stated and proved in
Strickland, Proposition 7, printed p.7, reopened and visually
checked on 15 November 2026:
<https://strickland1.org/toda/toda.pdf>. Its proof reproduces
Toda Theorem 7.3 and Equations 7.10, 7.16:

\[
\begin{aligned}
 \pi_{14}S^4_{(2)}
   &=\mathbb Z/8\{a=\nu_4\sigma'\}
     \oplus\mathbb Z/4\{b=E\epsilon'\}
     \oplus\mathbb Z/2\{c=\eta_4\mu_5\},\\
 \pi_{15}S^5_{(2)}
   &=\mathbb Z/8\{d=\nu_5\sigma_8\}
     \oplus\mathbb Z/2\{e=\eta_5\mu_6\},\\
 E a&=2d,\qquad E b=\varepsilon\,2d,\qquad E c=e,
 \qquad \varepsilon\in\{1,-1\}.
\end{aligned}
\]

Thus a class \(ma+nb+tc\) is in the kernel precisely when
\(t=0\) and \(m+\varepsilon n\equiv0\pmod4\). The kernel
is the cyclic order-eight subgroup generated by
\(a-\varepsilon b\). Equations (13.2)--(13.3), and the fact
that multiplication by three is invertible on a two-primary group,
therefore prove the sharper one-parameter conclusion

\[
 wl_4\in
 \bigl\langle i_{5*}(\nu_4\sigma'-\varepsilon E\epsilon')\bigr\rangle,
 \qquad
 h_Ml_4\in
 \bigl\langle\alpha\sigma'-\varepsilon u_4E\epsilon'\bigr\rangle.
 \tag{13.4}
\]

No assertion that its coefficient is odd is made. Such an inference
from the double relation would require the additional nonvanishing
of \(2i_{5*}(\nu_4\sigma')\), which has not been established.
Nor does (13.4) evaluate the generator's image in the full target Y.

There is a precise final target formulation. Write
\(e=u_4E\epsilon'\), so \(2e=0\), and put
\(q=\alpha\sigma'+e\). The sign in (13.4) is immaterial in
Y. Since \([\alpha,\alpha]=0\), the already checked cyclic
Hilton argument also gives \(4(\alpha\sigma')=(4\alpha)\sigma'=0\).
Thus \(q\) has order dividing four, and the conclusions are

\[
 h_Ml_4\in\langle q\rangle,\qquad 2(h_Ml_4)=2q.
 \tag{13.5}
\]

If q has order four, the composite is q or minus q. If q has
order at most two, the remaining possibilities are zero and q.
This conditional distinction retains the unresolved full-target
coefficient and does not assert oddness when the double vanishes.

## 14. The exact limit of the three primary annihilator relations

Status: 16 November 2026. This is a calculation of a specified
composition quotient, not a calculation of the complete kernel of
the bottom map into Y. It makes precise why the already proved
relations `2u4=0`, `u4 eta4=0`, and `u4 E nu'=0` alone have not
evaluated q or its double.

Write

\[
 G=\pi_{14}S^4_{(2)}
   =\mathbb Z/8\{a=\nu_4\sigma'\}
     \oplus\mathbb Z/4\{b=E\epsilon'\}
     \oplus\mathbb Z/2\{c=\eta_4\mu_5\},
\]

and let R be the sum of the images in G of postcomposition by
`2 iota4`, `eta4`, and `E nu'`, from the appropriately dimensioned
sphere groups. Then

\[
 R=\langle4a,2b,c\rangle,
 \qquad G/R\cong\mathbb Z/4\{\bar a\}
                 \oplus\mathbb Z/2\{\bar b\}.          \tag{14.1}
\]

Here are the full composition checks. The classical sphere table
gives `pi14 S5` generated by `eta5 epsilon6`, `mu5`, and
`nu5 nu8 nu11`. Their composites with eta4 are respectively
`2b`, `c`, and zero. The last equality follows from
`eta4 nu5=(E nu') eta7` and `eta7 nu8=0`, the latter lying
in the stable fourth stem. Also `pi14 S7=Z/8{sigma'}` and
`(E nu') sigma'=2b`.

For the degree-two map the Hopf--Hilton formula first gives

\[
 (2\iota_4)\nu_4=4\nu_4-E\nu'.
\]

On composing with sigma', the possible mixed Hilton term is
four times a class obtained by precomposition with eta13,
so it is zero. The self terms vanish because both left
factors have source S7 and `[iota7,iota7]=0`. Consequently

\[
 (2\iota_4)_*a=4a-2b,
 \qquad (2\iota_4)_*b=2b.                            \tag{14.2}
\]

The second equality uses the fact that b is a suspension.
For completeness, no extra generator can come from c:
its image has order at most two, and its suspension is
`(2 iota5)_*(eta5 mu6)=0`. The exact kernel in Section 13
therefore puts that image in the subgroup generated by 4a.
Thus the degree-two image is exactly `<4a,2b>`, proving
(14.1). In particular the class `a+b` still has order four
in this quotient, and its double is still nonzero there.

All three image subgroups are killed by the actual bottom
map `u4:S4->Y`. However (14.1) does not say that its kernel
has no additional elements. Such elements can be supplied
by the higher attaching maps and their compatible
nullhomotopies. Therefore this quotient rules out only a
deduction by the three stated primary composition
relations. It does not prove that q or 2q survives in Y.

The additional source table was checked in Strickland's
author program, <https://strickland1.org/toda/Toda.m>, in
the block `pi_(n+9)(S^n)` for `pi14 S5`, which explicitly
attributes it to Toda Theorem 7.2, p.61. The eta composites
and their Toda locators are in the same opened program;
`(E nu') sigma'=2E epsilon'` is proved in the opened
Proposition 13 of the accompanying author note. This is
note-only use of that primary implementation, with no
claim that the original Toda book page was opened.

There is also a useful actual Hurewicz boundary. The lift
of alpha to `L=Y<7>` gives a once-adjoint of
`alpha sigma'` which factors through `Omega S7`.
James's tensor calculation has its generator in degree
six, so `H13(Omega S7;Z)=0`. Thus the integral once-loop
Hurewicz of `alpha sigma'` is zero. The once-loop
Hurewicz of q is exactly that of the unique lift of
`e=u4 E epsilon'` and has order at most two. Section 17 now
proves that this image is zero by an actual factorization through
S11. Neither argument decides either homotopy class.

## 15. One exact nu-composite in the first possible order-dropping stage

This is a new consequence for the Moore-four target of D.2.43,
not a reopening of Section 11's closed coextension in A5.
Put `M4=M(Z/4,7)=S7 union_4 e8`, with bottom inclusion i and
pinch p. Its unique class

\[
 m_4\in\pi_{11}M_4,\qquad pm_4=2\nu_8,
\]

satisfies

\[
                         m_4\nu_{11}=0.              \tag{15.1}
\]

Indeed the relevant groups are in the stable range, and the
Moore exact sequence has `pi11 S7=0` and
`ker(4:pi11 S8->pi10 S7)=<2nu8>`. Thus m4 is uniquely
the coextension of `2nu7` over the degree-four cone. The
choice-level cone formula identifies its composite with
`nu11=E nu10` as a bottom image of the bracket

\[
              \{4\iota_7,2\nu_7,\nu_{10}\}
                    =\langle4\sigma'\rangle.
\]

The equality is the bracket calculation already proved with
its full indeterminacy in Section 11: a fourfold suspension
of the zero bracket in the two-primary group `pi10 S3`
supplies zero, and the indeterminacy is generated by
`4sigma'`. The bottom map of M4 kills that generator:
`i(4sigma')=i((4iota7)sigma')=0`, because S7 is an H-space
and its degree-four action on this homotopy group is
ordinary multiplication. This proves (15.1), independently
of the sign used to define the coextension.

This removes one previously unresolved entry from a possible
calculation of the actual twelve-cell contributions to the
James--Hopf image. It does not determine that entire image.
In the low nine-cell complex K, a class s0 with `2s0=m4`
therefore satisfies `2(s0 nu11)=0`; its composite itself
has not been evaluated. The complete eleven-stage target
also has independent free lifts. Their composites with nu
may contain secondary terms that the primary cell matrix
does not fix. In particular (15.1) alone does not show that
the twelve-cells leave `partial(4c)` nonzero, and hence
does not evaluate `2q` in the full target.

The cone formula and its dimension shifts were independently
checked by the fibrations agent and this author on 16 November
2026. Its proof uses the already opened sources and exact
bracket audit of Section 11, not a new unverified table.

## 16. An actual desuspension of 2alpha, with the remaining composition retained

This gives an alternative description of the double in D.2.46,
but does not evaluate it. Put `X0=Sigma B`. The Ganea evaluation
fibration already used in `FGH_D2_E2_eta_extension.md`, Section 7,
is

    G=Sigma(B smash B) -> X0 -> K(F2,3).

It identifies `pi6 X0` with `pi6 G`. The latter group can be
computed without a hidden attaching-map assumption. In the
usual low mod-two homology notation for B, the degrees five,
six, and seven of G have bases

    aa;        ab,ba;        ac,ca,bb.

The first Bocksteins are `beta(ab)=beta(ba)=aa` and
`beta(bb)=ab+ba`, while the second homology square takes
each of ac, ca, bb to aa. Choose integral six-coordinates
`B6=ab`, with boundary `2aa`, and `C6=ba-ab`, with zero
boundary. The six-skeleton is `M(Z/2,5) wedge S6_C` and

    pi6(G6)=Z/2{bottom eta5} plus Z{C6}.

The two actual integral cycles ac and ca give seven-cells
with zero C6 degree and nonzero Sq2 detector, so each attaches
by exactly the bottom eta. The bb cell has integral degree
`+/-2C6` and the same eta detector. These are all possible
components, since this homotopy group is in the stable range.
Consequently

    pi6 G = Z/2{beta0},
    pi6 G -> H6(G;Z) is an isomorphism.

Transport beta0 to X0 by the Ganea map. In the first James
pair `(JX0,X0)`, relative Hurewicz gives

    pi6(JX0,X0)=H6(JX0,X0;Z)
               =H3(X0;Z) tensor H3(X0;Z)=Z/2.

The class alpha in `pi6 JX0=pi7 Y=Z/4{alpha}` hits its
nonzero element: the Hopf-invariant-one representative
`u4 nu4` has the bottom square as its once-loop homology
image. Exactness therefore gives

    E beta0=2alpha,
    2q=(E beta0) sigma'.                              (16.1)

The relative pair and the complete low cell calculation were
independently checked by the fibrations agent. Equation (16.1)
is an actual unstable identity. It is not a vanishing proof:
sigma' is not being replaced by a suspension with the same
coefficient, and no compatibility of an additional
nullhomotopy has been asserted. In particular this does not
identify the composite with an already zero stable class.

## 17. The actual suspended-nu factorization and vanishing loop Hurewicz

Status: 16 November 2026. This section supports D.2.49. The
factorization and every Toda indeterminacy were independently
checked by the root and fibrations agents; the source agent also
completed a full final read of both D.2.49 inputs and passed them.
It evaluates an actual
integral loop-Hurewicz image, not the homotopy class q or h.

Write `u3:S3->X0=Sigma B`, so `E u3=u4`. Section 16 proves that

    E: pi6(X0)=Z/2 -> pi7(Y)=Z/4{alpha}

is injective, with image generated by `2alpha`. The already
proved actual relation `u4 E nu'=0` therefore implies

    u3 nu'=0.                                           (17.1)

The source input is exact, including its indexing. Strickland's
author note, Section 2.5 on printed p.4 and Proposition 2 on p.6,
states that epsilon-prime is the unique element of
`{nu',2nu6,nu9}_3`, attributing this to Toda Section VI(iv).
The author program explains that the indexed representation is
`{nu',E^3 nu',E^3 nu6}_3`, so it lies in the ordinary bracket
`{nu',2nu6,nu9}`. Both sources were reopened directly:

<https://strickland1.org/toda/toda.pdf>

<https://strickland1.org/toda/Toda.m>.

The program's indexed-bracket convention and full indeterminacy
are in the block beginning with its explanation of TodaBracket;
the epsilon-prime declaration explicitly names Section VI(iv).
The PDF's Proposition 2 independently uses the same
zero-first-entry naturality argument. The original Toda book
page was not opened; this source boundary is retained.

Postcomposition with u3, followed by (17.1), now gives

    u3 epsilon' in {0,2nu6,nu9}
                  = pi10(X0) composed with nu10.         (17.2)

This equality does not choose compatible nullhomotopies by fiat.
The ordinary bracket with zero first map contains zero. Its
first indeterminacy summand is zero composed with pi13(S6),
and its full remaining summand is `[S10,X0] composed with
Sigma nu9`. These are all choices. Consequently there is an
actual `t:S10->X0` with `u3 epsilon'=t nu10`, and suspension
gives the actual factorization

    e=u4 E epsilon'=(E t) nu11 in pi14(Y).                (17.3)

All pi_j(L)->pi_j(Y) for j>6 are isomorphisms, where
`L=Y<7>`. Hence Et and its homotopies have unique lifts through
L, and (17.3) gives the unique lift of e. Its once-adjoint
factors through Omega S11. The lift of alpha sigma-prime
similarly has once-adjoint factoring through Omega S7. James's
integral tensor calculation has generators in degrees ten and
six, respectively, so both have zero H13. Therefore

    Hur_Z adj(e_L)=Hur_Z adj(alpha_L sigma')=0,
    Hur_Z adj(q_L)=Hur_Z adj(h_M l4)_L=0.                 (17.4)

The last equality uses the exact cyclic containment D.2.46.
The high-dimensional sphere factor is essential. The obvious
factorization of e through S4 only implies zero Hurewicz in
Omega Y: u4 does not lift to L, and injectivity of
H13(Omega L)->H13(Omega Y) has not been assumed.

The fibrations agent independently proved the exact comparison
in `EH5_C2_Moore_quadratic.md`, Section 7:

    2[ab-ba]=Hur_Z adj(h_M l4)_L,
    |a|=6, |b|=7, db=4a.                               (17.5)

It retains the actual Moore-four extension and its top-sphere
coaction, the odd integral Hurewicz normalization of the
quadratic generator, and both literal chain identities proving
independence after doubling. Combining (17.4)--(17.5) proves
`2[ab-ba]=0` in the actual integral loop homology. The expanded
proof is the input `sections/D2_even_commutator.tex` inside
D.2.49. It does not specify a compatible higher relation on a
chosen chain bounding this double. In particular neither the
integral cohomology square b8^2 nor h itself is claimed zero.

Final checkpoint-15 scope update: D.2.50 subsequently proves that
the integral cohomology square b8^2 is nonzero of exact order two,
using the canonical cobar model and the doubled-commutator boundary.
The actual homotopy class h, the cyclic generator q, and the required
pairing on the stable Hurewicz image remain unevaluated.


## 18. The remaining suspended nu-image has only two named directions

Status: 16 November 2026. The fibrations agent supplied this exact
refinement and the axioms agent checked it against the full final
D.2.31 and D.2.22 presentations. It does not evaluate either
remaining nu-composite.

Use the actual basis from D.2.31:

    pi11(Y)=pi9(T)=(Z/2){p,s,x,y},
    h_F2(p)=h_F2(s)=0,
    h_F2(x)=K1, h_F2(y)=K5,
    s=rho_Y nu8.

The once-loop Hurewicz images of x and y are respectively

    (sigma a)(sigma f)+(sigma f)(sigma a),
    (sigma a)^2(sigma b)+(sigma b)(sigma a)^2.

They are nonzero and independent, with tensor lengths two and
three in H*(Omega Sigma X0;F2). The once-adjoint of any actual
suspension Et, t:S10->X0, is James-unit composed with t.
Its image has tensor length one. Intersecting this length-one
subspace with the displayed complete spherical image gives zero.
Consequently

    E pi10(X0) is contained in <p,s>.                    (18.1)

This is only containment; no surjectivity onto the two-dimensional
kernel is being claimed. It uses the complete actual D.2.31
Hurewicz image, not a generalized EHP sequence outside its range.
Combining (18.1) with the actual factorization in Section 17 gives

    e in <p nu11, rho_Y nu8 nu11>.                       (18.2)

Both directions have zero integral once-loop Hurewicz for the
high-sphere factor reason already used in D.2.49. Their actual
homotopy values, and the coefficient selected by the Toda choices,
remain unknown. Neither (18.1) nor (18.2) sets q or its double
zero, nor proves that either survives.

## 19. The compatible suspended factor is zero: D.2.53

**Status: proved; root, fibrations and source agent independently passed the full choice-level argument.** This improves Section 18 for the particular epsilon-prime factor without computing either abstract nu-composite separately.

The essential extra information is that the factor t can be selected from a second Toda bracket. It is not legitimate to impose this condition on every factorization satisfying u3 epsilon-prime = t nu10.

Choose the extension and coextension that realize the specified epsilon-prime in the ordinary bracket containing its indexed definition:

    C=C(2nu6)=S6 union_(2nu6)e10,
    bar(nu-prime):C -> S3,
    tilde(nu9):S13 -> C,
    bar(nu-prime) tilde(nu9)=epsilon-prime,
    pinch tilde(nu9)=nu10.

The already proved actual nullhomotopy u3 nu-prime=0 supplies a pinch factor t with

    u3 bar(nu-prime) = t pinch,
    t in {u3,nu-prime,2nu6},
    u3 epsilon-prime = ±t nu10.

The bracket assertion records the two compatible nullhomotopies: the chosen nullhomotopy of nu-prime times2nu6 defining the extension and the chosen nullhomotopy of u3 nu-prime. Gluing their common face is precisely the ordinary extension–coextension Toda construction. Equivalently, the standard cone square proves the associativity inclusion with these fixed compatible choices. No arbitrary Puppe factor is silently identified with this bracket value.

Suspending that same cone diagram gives

    Et in B2={u4,E nu-prime,2nu7} contained in pi11Y.

The smaller bracket B1={u4,E nu-prime,nu7} is defined: u4 E nu-prime=0, and

    E nu-prime nu7=E(nu-prime nu6)=0

because the two-primary group pi9S3 is zero. Last-entry precomposition by degree two gives

    B1 composed with2id_S11 is contained in B2.

D.2.31 proves that pi11Y has exponent two, so B2 contains zero. Its full ordinary indeterminacy is

    u4 pi11S4 + pi8Y composed with2nu8.

The first term vanishes since pi11S4 at2 is zero. For every gamma:S8->Y, the second term is literally

    gamma(2nu8)=gamma nu8 (2id_S11)=2(gamma nu8)=0.

This is right precomposition on a sphere and uses no left-additivity hypothesis in the gamma variable. Thus B2 is the singleton zero and the compatible selected factor satisfies Et=0. In particular

    e=u4 E epsilon-prime = (Et)nu11 = 0 in pi14Y.

The unique lift to L=Y<7> is also zero. D.2.46 now reads

    q=alpha sigma-prime,
    4q=0, h in <q>, 2h=2q.

No value or order of this remaining alpha sigma-prime is selected. If it has order4, h=±q; otherwise h may be0 orq.

### Primary opening audit

Reopened the author's original program at <https://strickland1.org/toda/Toda.m>, rather than inferring the sphere vanishings from memory. The current web rendering lists the sixth-stem reference at lines2635–2636 (Toda Proposition5.11, p46) and pi9S3=0 at lines2640–2641. The seventh-stem reference is at lines2650–2651 (Toda Proposition5.15, p50), followed by pi10S3=0 and pi11S4=0 at lines2653–2654. These are two-primary tables. The local previously downloaded program has different line numbering, so the named blocks and literal groups are the stable locators.

The last vanishing also follows independently from the Hopf fibration S3->S7->S4, since pi11S7=pi4-stable=0 and pi10S3 at2 is zero. The indexed epsilon-prime convention and its inclusion in the ordinary bracket were already reopened for D.2.49 in the author note Section2.5 p4 and the program's declaration, attributed to Toda SectionVI(iv). The original Toda book pages remain unopened. The bracket naturality and selected-factor identification above are proved directly by the actual cone diagrams rather than being imported from an unopened formula.

### Independent audit and manuscript

Fibrations independently passed the complete choice-level proof, then reopened all three author-program group entries. The source agent independently checked the glued-nullhomotopy square and emphasized that only a compatible selected factor is being classified. Root checked the dimensions, full indeterminacy, degree-two naturality and target exponent.

The full claim is in `sections/D2_epsilon_term_zero.tex`, D.2.53a–l, with one FGH record. This is a new exact target value, not completion of the fourth-suspension problem.

## 20. The actual James–Hopf image and its low-stage survival

This is a note-only finite-stage reduction. It does not assert that the full auxiliary target preserves the class.

Let X0=Sigma B and put Z=Sigma(X0 smash X0)=Sigma^3(B smash B). Let H denote the actual second James–Hopf operation on homotopy groups of Sigma X0. Its naturality with respect to suspension maps gives the exact formula

    H(alpha sigma-prime)=u7 sigma-prime in pi14 Z,
    u7=Sigma(u3 smash u3):S7 -> Z.                 (20.1)

Indeed alpha sigma-prime = (Sigma u3)(nu4 sigma-prime). The exact sphere value H(nu4 sigma-prime)=sigma-prime is explicitly displayed in Strickland Proposition13, printed p9. Its safe use was already checked for D.2.44: the left suspension/naturality interface and the injectivity of suspension on pi14S7 remove the warning about an unrestricted generic Hopf-composition formula. Equation (20.1) does not treat sigma-prime itself as a co-H map, or substitute H(alpha) sigma-prime for a generic composite without justification.

### The actual low target

Twice suspend the complete Ganea low-cell matrix used in D.2.49. It gives a chosen actual nine-skeleton

    Z9 = C_1^9 wedge M(Z2,8) wedge S9,

under its bottom S7. The relevant Chang summand is

    C_1^9 = M(Z2,7) union_(i7 eta7)e9.             (20.2)

In detail, before the two suspensions the six-stage is M(Z2,5) wedge S6, and its three seven-cells attach by i eta5, i eta5, and i eta5+2 on the free six-sphere. Invertible cell slides leave i eta5, zero, and twice the free sphere, yielding the stated wedge after two suspensions. There are no unrecorded seven-cell components because the relevant pi6 is exactly Z2{i eta5} plus the free sphere line.

The inclusion M(Z2,7)->C_1^9 is injective on pi14. Here is the complete borderline argument, rather than an extrapolation of stable range. Put f=i7 eta7:S8->M(Z2,7), and let F be the homotopy fiber of the pinch C_1^9->S9. The relative James model and its second stage are

    F=J(M_f,S8),
    J2 = M(Z2,7) union_[id,f] Cone(M(Z2,7) smash S7).

These are Jin–Zhu, Lemma2.1(i),(iii), printed p4, reopened directly at <https://arxiv.org/pdf/2402.11226>. The two new cells have dimensions15 and16. The only fifteen-cell attaching map is

    [i7,i7 eta7] = i7[identity7,identity7] eta13 = 0,

because S7 is an H-space. The Moore top contributes at dimension16, which cannot change pi14. All later relative-James word lengths begin in dimension23. Hence pi14(M2,7)->pi14(F) is an isomorphism.

The remaining boundary from pi15S9 is also zero. The suspension pi14S8->pi15S9 is onto (indeed both are the stable sixth stem), and Lemma2.3 of the same source identifies the boundary of a suspension with f on its desuspension. Its only possible value is

    i7 eta7 nu8^2 = 0.

The sphere composite eta7 nu8^2 has zero stable image because eta nu^2=0, while pi14S7=Z8{sigma-prime} stabilizes injectively by sigma-prime -> 2sigma in Z16. Thus it is already zero before applying i7. Equivalently, the hypotheses of Jin–Zhu Lemma2.5, printed p5, hold and its exact sequence proves the claimed injection.

Morisugi–Mukai's exact Moore relation i7 sigma-prime=2l4 has order two. Consequently the class on the right of (20.1), at the chosen nine-stage, is nonzero of exact order two. Retraction onto the Chang summand makes the other wedge factors harmless at that stage.

### Remaining boundary

This proves survival only in Z9. For later ten- and eleven-cells the same relative James range has no mixed terms in degree14 and the relevant sphere stems pi5^s and pi4^s vanish, so those dimensions cannot kill a pre-existing pi14 class. Twelve- through fifteen-cells can contribute actual nu, eta-squared, eta, or direct attaching relations. No complete calculation of those contributions for the full Sigma^3(B smash B) has been made. In particular, the stable vanishing of u7 sigma-prime is not a proof of its actual vanishing, and its low-stage survival is not a proof of full-target survival.

The exact new primary inputs opened for this note are Jin–Zhu Lemma2.1 and Lemma2.3–2.5, printed pp4–5, plus the already audited Strickland Proposition13 and Morisugi–Mukai Moore relation. No new manuscript number is assigned to this boundary calculation.

## 21. The doubled N-lift has zero actual nu composite

Status: 16 November 2026, independently passed by root and the fibrations agent. It is used as a lemma in the complete incoming-fifth-differential calculation, whose final note was independently passed by the axioms agent. This is a calculation in the chosen finite eleven-stage, not the tautological consequence of the later relation 2p=0 in the full target.

Let P11 be the actual six-connected realization of the twice-shifted nine-skeleton L9 of D.2.22. The lower shifted cell attachments have dimensions at most eleven and their attaching groups are in the ordinary stable range, so this is an ordinary finite complex mapping to L=Y<7>. Write alpha:S7->P11 for its bottom Moore-four map. Orient the N-prime eleven-cell so that its attaching map is alpha nu7. The chosen class p0 in pi11(P11) has integral Hurewicz 4N-prime and zero second- and fourth-square detectors, as in D.2.22t12. The conclusion is

    (2p0) nu11 = 0 in pi14(P11).                    (21.1)

No assertion that p0 nu11 itself vanishes is made.

### Exact source bracket without a K-local substitution

The author's original Strickland program explicitly declares sigma-triple-prime to be the unique ordinary bracket {nu5,8 identity8,nu8}, attributing it to Toda Lemma5.13. The same program gives

    E sigma-triple-prime = 2sigma-double-prime,
    E sigma-double-prime = 2sigma-prime,

attributing both to Toda Lemma5.14. These declarations were reopened directly at <https://strickland1.org/toda/Toda.m>: current web lines807–819 and1482–1489. The author's PDF, Section2.5 on printed p4, gives the same ordinary bracket and the generators and suspension normalization. The original Toda book remains unopened.

Twice suspending the actual cone choices puts 4sigma-prime in

    {nu7,8 identity10,nu10} contained in pi14S7.

Its full ordinary indeterminacy is

    nu7 pi14S10 + pi11S7 nu11 = 0,

because both intervening groups are the fourth stable stem. Consequently this bracket is the singleton {4sigma-prime}. This direct unstable source proof does not replace an ordinary sphere bracket with a K-local one.

### The top-eight cone lift is exactly twice p0

Let Cnu=S7 union_nu7 e11. Its bottom map and the N-prime characteristic cell give an actual map j:Cnu->P11, with bottom alpha and top degree one on N-prime. The ordinary group pi11(Cnu) is in the stable range; its pinch image in pi11S11 is 8Z, and pi11S7=0. Hence there is a unique class v8 with top degree eight. It is the actual coextension of 8 identity10 across nu7.

Both 2p0 and jv8 have integral Hurewicz 8N-prime. Their difference therefore lies in the complete torsion subgroup V of pi11(P11). D.2.22t9–t12, shifted twice, identify V as an elementary abelian group of rank five and show that its combined second- and fourth-square mapping-cone detectors are injective. The detectors of 2p0 vanish by the degree-two cone map. The detectors of jv8 also vanish: Cnu has no mod-two cohomology in degrees eight or ten, and naturality of the actual map of cones reduces the degree-twelve Sq4 and Sq2 pairings to those zero groups. The detector is additive here because pi11 of these six-connected complexes is already stable. Therefore the difference has zero detector and is zero:

    2p0 = jv8 in pi11(P11).                         (21.2)

This uses the complete torsion detector in P11, not an unsupported comparison of two coextensions modulo an unknown old-cell class. In particular, it is unnecessary to choose or discard an m4 remainder. Any other lift with the same integral Hurewicz differs by V, so its double is the same.

### Actual composition in degree fourteen

The ordinary mapping-cone formula gives

    v8 nu11 = i7 {nu7,8 identity10,nu10}
             = i7(4sigma-prime) in pi14(Cnu),

up to the harmless overall convention sign. This is an actual cone calculation in degree fourteen, not a stabilization inference in that degree. Composing (21.2) with the suspension nu11 now gives

    (2p0)nu11 = alpha(4sigma-prime) = 4(alpha sigma-prime)=0.

The last equality is valid in P11 itself. The Moore-four cell makes 4alpha=0 there, while every Whitehead product [alpha,alpha] is zero because it is the image of [identity7,identity7] and S7 is an H-space. Thus the cyclic Hilton correction to precomposition by sigma-prime vanishes, exactly as in D.2.46. This proves (21.1) before any twelve-cell imposing 2p is attached.

The calculation may constrain the incoming d5 relation in the stable Hurewicz analysis. It does not decide alpha sigma-prime, its double, the actual h, or the required stable half-product pairing.

## 22. The auxiliary Chang component has zero actual nu composite

Status: exact finite-component calculation, independently passed in full by the fibrations agent and submitted to root on 16 November 2026. This addresses the Chang summand of the auxiliary James--Hopf target in Section 20. It does not classify the new coextensions created by that target's ten- and eleven-cells.

Write

    C9 = C_1^9 = cofib((2 identity7,eta7):S7 vee S8 -> S7).

The stable cofiber sequence, used only in the ordinary stable range pi11, identifies pi11(C9) with the kernel

    Z8{nu7} plus Z2{eta8²} -> Z8{nu7},
    (x,y) -> 2x+4y.

It is cyclic of order four. Its generator t is characterized, up to the orientation convention, by pinch(t)=(2nu8,eta9²). Then

    t nu11 = 0 in the ACTUAL pi14(C9).                (22.1)

Here is the complete one-desuspension argument. Put

    C8=cofib(a0),
    a0=(2 identity6,eta6):S6 vee S7 -> S6,
    b0=(2nu6,eta7²)^T:S9 -> S6 vee S7.

The wedge has no mixed Whitehead term in the degree of b0. The two actual zero composites needed for the cone construction are

    a0 b0 = 4nu6+eta6³ = 8nu6 = 0,
    b0 nu9 = (2nu6 nu9,eta7² nu9)^T = 0.

The identities eta6³=4nu6 and eta8 nu9=0 are in the usual stable sphere ranges. The remaining identity 2nu6 nu9=0 is NOT being inferred from generic Freudenthal stability: pi12S6 is outside that generic range. It is the actual sphere calculation pi12S6=Z2{nu6 nu9}, explicitly tabulated in Strickland's author program, sixth-stem block (current lines2635--2645), with the order rule at lines1095--1104; both are attributed there to Toda Proposition5.11, p46. These passages were reopened directly on 16 November2026. In the first equality nu6 is a suspension, so the degree-two action on 2nu6 is genuinely additive; no Hopf correction is omitted.

Choose an actual coextension t0:S10->C8 of b0 across a0. Its suspension has the required pinch and hence is t: pi11(C9)->pi11(S8 vee S9) is injective, because pi11S7=0 and the cofiber calculation in that range is stable. The ordinary cone construction, using the displayed nullhomotopy b0 nu9=0, gives

    t0 nu10 = i6 delta for some delta in pi13S6.

This is the standard extension--coextension Toda construction itself, not a claim of an unrestricted covariant cofiber exact sequence in degree thirteen. Now pi13S6=Z4{sigma-double-prime} and E sigma-double-prime=2sigma-prime. Suspending the chosen cone equality therefore gives

    t nu11 in i7 <2sigma-prime>.

Every class in this last subgroup is zero. The bottom i7 has order two, and [i7,i7]=i7[identity7,identity7]=0 since S7 is an H-space; hence the cyclic Hilton correction vanishes and i7(2sigma-prime)=2(i7 sigma-prime)=0. This proves (22.1). The same proof also gives zero for the nu composite of every element of pi11(C9).

### Opened source interface and precise boundary

The exact sphere group and suspension pi13S6=Z4{sigma-double-prime}, E sigma-double-prime=2sigma-prime were reopened in Strickland's author PDF Section2.5 p4 and original program, suspension block1487--1489; the lower stable stem relations are the already opened Oka Section2 formulas. The actual cone argument above is explicitly given, so no unverified matrix Toda numerical value is needed.

For comparison, Yang--Miyauchi--Mukai, *An unstable approach to the May--Lawrence matrix Toda bracket and the 2nd James--Hopf invariant*, arXiv:2310.18014v9 (4 July2024), Theorem1.2 p2 and Definition3.1/Proposition3.2 pp4--5, were opened directly at <https://arxiv.org/pdf/2310.18014>. Their indexed H-formula gives the same zero Hopf invariant for this bracket, but that machinery is not needed for (22.1). The general matrix suggestion from the initial literature lead is not being treated as an evaluated target relation.

Section20 proves the bottom u7 sigma-prime survives the auxiliary target through dimension eleven. Equation (22.1) shows that a twelve-cell attaching map lying in this original Chang component cannot kill it by its nu composite. A full statement for every twelve-cell would still require the complete pi11 of the auxiliary eleven-stage, including the coextensions created by its ten- and eleven-cells. That matrix has not been computed, and no full-target nonvanishing or nullity follows here.
