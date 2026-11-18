# The low quadratic layer of the mod-two to mod-four Moore comparison

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Finite stable calculation; the final unstable boundary
in the target is explicitly left to the James--Hopf image computation.
The full calculation was independently read and passed by
`fibrations_groups`, including the integral signs, the eta-kernel
argument, and the one-new-factor attachment without an extra factor
of two.
Root independently read and passed the full proof, including the
derived symmetric-monoidal integral chains, natural coefficient two,
stable nine-skeleton truncation, and the exact remaining James--Hopf
image obligation. The finite-layer proof is now supplied as the inner
proof file `sections/D2_quadratic_cells.tex` for D.2.43; its parent
claim and record are owned by `fibrations_groups`.

## 1. Result and exact scope

Write

\[
 D_2E=(E\wedge E)_{hC_2},\qquad L_2E=\Sigma^{-1}D_2E.
\]

The involution is the usual interchange of the two factors. There is
no additional sign representation in this formula. All spectra and
homotopy groups below are two-local. Let

\[
 M_q=M(\mathbb Z/q,7),\qquad
 K=(M_4\vee S^8_r)\cup_{i\eta_7+2r}e^9_s.
\]

Here and below a stable cell model is intended. This is precisely the
twice-suspended model in (D.2.22t2); it is not the shorter, unshifted
approximation appearing at an earlier stage of the manuscript.
Let \(m_0:M_2\to M_4\subset K\) have bottom degree two and top degree one.
Then

\[
 \pi_{14}L_2M_2=\pi_{15}D_2M_2\cong\mathbb Z/4,
 \qquad
 \pi_{14}L_2K=\pi_{15}D_2K
       \cong\mathbb Z/8\{c\}\oplus\mathbb Z/2\{u\},
 \tag{1}
\]

and, with the integral cycle coordinates fixed below,

\[
 (L_2m_0)_*(1)=2c.
 \tag{2}
\]

In particular the quadratic map is injective on this cyclic source.
The eta part of the nine-cell attachment is retained in the proof:
its quadratic cross attachment is \(P\eta+2u\). The class \(P\eta\)
has already been killed by the intrinsic two-cell-over-bottom part
of \(D_2S^7\), so this attachment imposes \(2u=0\), without killing
\(2c\).

Adding a free nine-sphere to \(K\), or adding stable cells in dimensions
at least ten, does not alter these groups or this map. A new cell of
dimension ten first has a cross term with the bottom seven-cell in
dimension seventeen. A free nine-sphere contributes a new free
sixteen-cell whose attaching map is zero. None changes \(\pi_{15}\).

**Scope.** Equation (2) is a calculation in the quadratic spectrum.
It does not assert that the actual composition \(h_Ml_4\) is nonzero.
The latter is the image of \(2c\) under the target boundary, and can
vanish if \(2c\) is in the target James--Hopf image. Section 6 states
the precise remaining test.

## 2. Integral chains for one Moore spectrum

Give \(M_q\) integral label chains \(a_7,b_8\) with
\(\partial b=q a\), where \(q\) is even. Use the free resolution
of the trivial right \(\mathbb Z[C_2]\)-module with cells \(e_i\),
and the convention

\[
 \partial(e_i xy)=e_{i-1}\bigl(xy+(-1)^i\tau(xy)\bigr)
                   +(-1)^ie_i\partial(xy).
 \tag{3}
\]

The Koszul actions are
\(\tau(aa)=-aa\), \(\tau(ab)=ba\), and \(\tau(bb)=bb\).
Through degree sixteen the relevant cells are

\[
\begin{array}{c|l}
14&P=e_0aa\\
15&x=e_0ab,\quad y=e_0ba,\quad z=e_1aa\\
16&T=e_0bb,\quad h=e_1ab,\quad h'=e_1ba,\quad U=e_2aa.
\end{array}
\]

Their boundaries are

\[
\begin{split}
 \partial x&=-qP,&\partial y&=qP,&\partial z&=2P,\\
 \partial T&=q(x+y),&\partial h&=x-y+qz,
       &\partial h'&=-\partial h,\qquad\partial U=0.
\end{split}
\tag{4}
\]

The unit incidence in \(\partial h\) eliminates \(y\) and \(h\),
giving \(y=x+qz\). Put

\[
 c_q=x+(q/2)z.
\]

This is an integral cycle, and the remaining degree-sixteen boundary
is \(\partial T=2q c_q\). Consequently

\[
 H_{14}(D_2M_q;\mathbb Z)=\mathbb Z/2\{P\},\qquad
 H_{15}(D_2M_q;\mathbb Z)=\mathbb Z/(2q)\{c_q\}.
 \tag{5}
\]

The chain computation is valid for spectra, including a spectrum with
nontrivial eta attaching data: extension of scalars to \(H\mathbb Z\)
is symmetric monoidal, so the integral homology of the homotopy-orbit
square is the derived coinvariant tensor complex. It does not by itself
compute stable homotopy. The following separate eta check supplies
that missing information.

## 3. The eta attachment and the Hurewicz isomorphism

The bottom-sphere inclusion gives \(D_2S^7\to D_2M_q\). The first
three cells of \(D_2S^7\) are \(P_{14},z_{15},U_{16}\), with
\(\partial z=2P\) and \(\partial U=0\). Moreover

\[
 \operatorname{Sq}_*^2 U=P.
 \tag{6}
\]

For example, in the notation of Behrens, Section 1.4, these cells have
mod-two homology names \(Q^7a,Q^8a,Q^9a\). His displayed Nishida
relation gives
\(\operatorname{Sq}_*^2Q^9a=\binom{7}{2}Q^7a=Q^7a\).
Equivalently, \(D_2S^7\) is the Thom spectrum of
\(\mathbb R^7\oplus7\gamma\) over \(\mathbb RP^\infty\), and
the second Stiefel--Whitney coefficient is \(\binom72=1\pmod2\).

The fifteen-skeleton is \(M(\mathbb Z/2,14)\). Its fifteenth
stable homotopy group is generated by the bottom \(\eta\), of order
two. The square (6) says precisely that \(U\) attaches by this
generator. Thus the intrinsic sixteen-cell kills \(P\eta\).
This remains true after mapping into \(D_2M_q\) or \(D_2K\).

Here is a convenient way to exclude every other possible homotopy
extension in the degree being computed. If \(E\) is fourteen-connective
and \(H_{14}E=\mathbb Z/2\{P\}\), then the fiber of
\(E\to H\mathbb Z\wedge E\) is \(E\wedge\tau_{\ge1}\mathbb S\).
Its lowest possible group is

\[
 \pi_{15}(E\wedge\tau_{\ge1}\mathbb S)
       =H_{14}(E)\otimes\pi_1\mathbb S=\mathbb Z/2.
\]

The corresponding map into \(\pi_{15}E\) is the bottom eta action.
Therefore the stable Hurewicz map in degree fifteen is surjective,
and its only possible kernel is generated by \(P\eta\). Since (6)
kills that generator, it is an isomorphism for every spectrum used
here. In particular

\[
 \pi_{15}D_2M_q\xrightarrow{\ \cong\ }H_{15}(D_2M_q;\mathbb Z)
         =\mathbb Z/(2q)\{c_q\}.
 \tag{7}
\]

One can instead use stable unit cancellation in (4): the relevant
sixteen-skeleton has a Chang summand with attaching matrix
\((2,\eta_{14})\), together with a Moore \(2q\) summand with bottom
dimension fifteen. Any eta term on the latter top cell is absorbed
by \(U\). Equation (7) is the part of that description needed here.

## 4. The bottom-two/top-one comparison and the extra target cell

The comparison \(m_0:M_2\to M_4\) acts on integral label chains by
\(a\mapsto2a\), \(b\mapsto b\). Accordingly

\[
 x\longmapsto2x,\qquad z\longmapsto4z,
 \qquad c_2=x+z\longmapsto2x+4z=2c_4.
 \tag{8}
\]

Naturality of the isomorphism (7) proves that the map on fifteenth
stable homotopy is \(\mathbb Z/4\to\mathbb Z/8\), \(1\mapsto2\).

Set \(K_8=M_4\vee S^8_r\). Distributing the two smash factors
before taking homotopy orbits gives the exact splitting

\[
 D_2K_8\simeq D_2M_4\vee(M_4\wedge S^8_r)\vee D_2S^8_r.
 \tag{9}
\]

The middle summand is \(M(\mathbb Z/4,15)\), with bottom class
\(u=ar\). The last summand starts in dimension sixteen. Hence

\[
 \pi_{15}D_2K_8=\mathbb Z/8\{c_4\}\oplus\mathbb Z/4\{u\}.
 \tag{10}
\]

To attach the nine-cell of \(K\), filter the two-fold smash by the
number of factors in the newly attached cell. The one-new-factor
quotient is \(K_8\wedge S^9\); the two-new-factor quotient is
\(D_2S^9\), which starts in dimension eighteen. In dimensions at
most sixteen the first quotient has exactly one cell, \(as\) in
dimension sixteen. Its attaching map is the orbit image of

\[
 a\wedge(i\eta_7+2r),
\]

and therefore equals \(P\eta+2u\) in \(\pi_{15}D_2K_8\).
There is no extra factor of two on \(P\eta\): the off-diagonal
cross term is an induced free \(C_2\)-orbit, and taking its homotopy
orbits leaves one copy. This is the same cross-term identification
as in (9).

Section 3 proves \(P\eta=0\), so this cell imposes exactly \(2u=0\).
All further cells have dimension at least seventeen and do not alter
\(\pi_{15}\). Equations (1)--(2) follow. The eta attachment was
included and checked, rather than suppressed because it is invisible
in integral cellular homology.

## 5. Why the truncation and map are enough for the layer

The actual target cover has bottom cell in dimension seven. Replacing
its suspension spectrum by its stable nine-skeleton changes it by
cells of dimension at least ten. In the square filtration, a term
with one such new cell has dimension at least seventeen; a term with
two new cells has dimension at least twenty. Homotopy orbits add
only nonnegative cell dimensions. Thus the comparison of quadratic
spectra is an isomorphism on \(\pi_{15}\).

The extra free \(S^9_R\) in the complete nine-skeleton contributes
\(M_4\wedge S^9_R\), whose first cell has dimension sixteen with
zero attaching map, and higher-dimensional terms. It has no
fifteenth homotopy group, so it changes neither (1) nor (2).

For the specified Moore restriction, the stable map into this
nine-skeleton is exactly \(m_0\) followed by inclusion. No choice
of a stable top-cell lift is silently changed in (8). If a different
Moore restriction is used, its cross-coordinate contribution has to
be computed separately; the present result concerns the pure-k
restriction fixed in D.2.41 and the companion target notes.

## 6. The exact remaining unstable test

Behrens, Theorem 4.2.1 (printed p.37), gives the natural fiber sequence

\[
 P_2\operatorname{Id}(X)\longrightarrow QX
          \xrightarrow{JH}QD_2\Sigma^\infty X.
 \tag{11}
\]

The text immediately after the theorem states that
\(\pi_tX\to\pi_tP_2\operatorname{Id}(X)\) is an isomorphism for
\(t\le3\operatorname{conn}(X)\). Thus a six-connected space has
the natural exact sequence

\[
 \pi_{15}^sX\xrightarrow{JH_*}\pi_{15}D_2\Sigma^\infty X
       \xrightarrow{\partial_X}\pi_{14}X
       \longrightarrow\pi_{14}^sX.
 \tag{12}
\]

For \(X=M_2\), Morisugi--Mukai, Lemmas 2.7--2.8 on printed p.523,
and the explicit pinch of their second summand show that the stable
kernel is \(\mathbb Z/4\{l_4\}\). The source group in (12) after
\(JH_*\) is also \(\mathbb Z/4\), by (7). Hence its boundary onto
that stable kernel is an isomorphism. There is a unique generator
\(\widetilde l_4\), up to the chosen sign of \(l_4\), with
\(\partial_{M_2}\widetilde l_4=l_4\).

Let \(Z'\) be the actual six-connected target cover, with the
specified map \(h_M:M_2\to Z'\). Naturality now gives the completely
specified formula

\[
 h_Ml_4=\partial_{Z'}(\pm2c),\qquad
 h_Ml_4=0\ \Longleftrightarrow\
       2c\in\operatorname{im}\bigl(JH_*:\pi_{15}^sZ'
                   \to\mathbb Z/8\{c\}\oplus\mathbb Z/2\{u\}\bigr).
 \tag{13}
\]

The sign has no effect on the membership test. Determining the
right-hand James--Hopf image is a distinct target computation; this
note neither sets it to zero nor assumes it is determined by the
nine-skeleton. In contrast to the quadratic target group, its domain
can depend on cells through dimension sixteen.

## 7. Primary-source audit

* Mark Behrens, *The Goodwillie tower and the EHP sequence*, author-hosted
  primary PDF:
  <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Behrens-EHP.pdf>.
  Opened Section 1.4, Lemma 1.4.1 and the displayed Nishida relation,
  printed p.4/PDF p.14; and Section 4.2, Theorem 4.2.1 and the following
  metastable comparison, printed p.37/PDF p.47. The source supplies
  exactly the ordinary interchange convention and the range in (11)--(12).
* Cohen--Lada--May, *The Homology of Iterated Loop Spaces*, Chapter I,
  Theorem 1.1(9), printed p.6, and Chapter III, Lemma 3.10 and its
  integral-resolution proof, printed p.232, are also the already opened
  primary sources for the Nishida and integral-cell conventions. The
  author-hosted PDF is
  <https://www.math.uchicago.edu/~may/BOOKS/homo_iter.pdf>.
  The scan/text is retained under `notes/I_sources/`; the latest web
  reopen exceeded the service's content-length limit, so that reopen
  is not claimed successful. The existing local primary text was read.
* Morisugi--Mukai, *Lifting to mod 2 Moore spaces*, J. Math. Soc. Japan
  52 (2000), 515--533, Lemmas 2.7--2.8, printed p.523:
  <https://www.jstage.jst.go.jp/article/jmath1948/52/3/52_3_515/_pdf>.
  This was opened in the D.2.41 audit, including the order-four
  Stiefel attaching class and the nonzero stable pinch of the other
  summand. No table for a different mod-four Moore space is substituted.

The chain reduction, the eta-kernel argument, the map (8), and the
cross-attachment filtration are proved in this note. They do not rely
on a quoted extended-power Moore-space decomposition.
