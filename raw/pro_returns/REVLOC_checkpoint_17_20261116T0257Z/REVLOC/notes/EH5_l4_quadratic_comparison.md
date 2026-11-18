# The exact metastable comparison for the Moore attaching class

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. The comparison and finite-layer calculation have
independent root and simple_higher audits. Section 5 is a finite-model strengthening independently audited by
root and simple_higher; it is not a statement about the complete target
cover.

## 1. Primary comparison, action, and connectivity

For a based space \(X\), write

\[
 \mathbb D_2X=(\Sigma^\infty X\wedge\Sigma^\infty X)_{hC_2}.
\]

The interchange is the ordinary symmetric-monoidal interchange. The
second derivative of the identity is \(S^{-1}\) with **trivial** \(C_2\)
action, rather than a sign twist. This is explicit in Goodwillie,
*Calculus III: Taylor Series*, Section 8, printed p.704:
<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/goodwillie-calc3.pdf>.
The author PDF was opened directly, including the cross-effect argument
and its symmetry statement. Existing bibliography key: FGHGoodwillie2003.

Behrens, *The Goodwillie tower and the EHP sequence*, Theorem 4.2.1,
printed p.37 in the opened author version, gives the natural fiber sequence

\[
 P_2\operatorname{Id}(X)\longrightarrow QX
       \xrightarrow{JH} \Omega^\infty\mathbb D_2X.
 \tag{1}
\]

Here \(JH\) is adjoint to the weight-two projection in the Snaith
splitting of \(\Sigma^\infty QX\). The sentence immediately following
the theorem identifies \(\pi_tX\to\pi_tP_2\operatorname{Id}(X)\)
as an isomorphism for \(t\leq3\operatorname{conn}(X)\).
The monograph works two-locally throughout; no finite-type hypothesis
is imposed in this statement. The exact opened PDF is
<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Behrens-EHP.pdf>.
The author version has PDF index47 for printed p.37. Do not substitute
the unrelated early 2005 preprint, which carries a warning about its
claims.

For the six-connected spaces used here, (1) therefore gives the natural
exact sequence

\[
 \pi_{15}^{s}X\xrightarrow{JH_*}\pi_{15}\mathbb D_2X
 \xrightarrow{\partial_X}\pi_{14}X
 \longrightarrow\pi_{14}^{s}X.
 \tag{2}
\]

Both degrees14 and15 are below the stated comparison bound18. Thus
there is no appeal to an unsupported convergence or an unstable-to-stable
identification outside its range.

## 2. The source lift is unique

Put \(M_q=M(\mathbb Z/q,7)\). The complete finite-spectrum calculation
in `notes/I_quadratic_Moore_layer.md` has been independently read here.
It proves

\[
 \pi_{15}\mathbb D_2M_2=\mathbb Z/4\{c_2\}.
 \tag{3}
\]

Morisugi--Mukai, Lemmas2.7 and2.8(ii), printed p.523, give

\[
 \pi_{14}M_2=\mathbb Z/4\{l_4\}\oplus
             \mathbb Z/2\{\widetilde{\nu_7^2}\}.
\]

The first summand is the exact stable kernel: the suspension of \(l_4\)
is a bottom-cell Whitehead square, and the other summand pinches to a
class with nonzero stable image. D.2.41 gives the complete primary-source
audit and identifies the actual sphere under consideration with
\(\pm l_4\).

Exactness of (2) and equality of the two finite orders imply that

\[
 \partial_{M_2}:\pi_{15}\mathbb D_2M_2
     \xrightarrow{\cong}\ker(\pi_{14}M_2\to\pi_{14}^sM_2)
 \tag{4}
\]

is an isomorphism. In particular the source James--Hopf homomorphism
is zero, and the lift of \(l_4\) is the unique generator up to the
sign convention for \(l_4\). There is no arbitrary choice of a lift
whose target image might differ by an unrecorded source connecting class.

## 3. The exact target layer and the map

The actual target \(Z'=Y\langle7\rangle\) is six-connected. Its stable
nine-skeleton, from (D.2.22t2) suspended twice, is

\[
 K\vee S^9_R,\qquad
 K=(M_4\vee S^8_r)\cup_{i\eta_7+2r}e^9_s.
 \tag{5}
\]

The specified Moore map \(h_M:M_2\to Z'\) is the bottom-two/top-one
comparison \(c_{2,4}:M_2\to M_4\subset K\), up to the fixed orientation.
This uses the pure-\(k\) restriction already isolated in D.2.36/D.2.41.
Since all relevant spaces are six-connected and these source complexes
have dimension at most9, the stable cell model and its specified map
are realized uniquely as ordinary maps in this range.

The independently audited finite-spectrum proof gives

\[
 \pi_{15}\mathbb D_2Z'
   =\pi_{15}\mathbb D_2K
   =\mathbb Z/8\{c\}\oplus\mathbb Z/2\{u\},\qquad
 (\mathbb D_2h_M)_*c_2=2c.
 \tag{6}
\]

Decisive points in that proof are the integral cycle
\(c_q=e_0ab+(q/2)e_1aa\), the relation \(2q c_q=0\), and the intrinsic
sixteen-cell of \(\mathbb D_2S^7\), whose second square kills the only
possible Hurewicz-kernel class \(P\eta\). The target's additional
sixteen-cell attaches by \(P\eta+2u\), hence imposes exactly (2u=0).
Thus no eta term has been erased merely because ordinary homology
does not detect it.

The free \(S^9_R\) contributes a summand beginning in degree16 and does
not alter \(\pi_{15}\). Any cell of (Z') above degree9 first contributes
to its quadratic spectrum in degree17, because the other factor starts
in degree7. This proves the target truncation specifically for the
quadratic group, not for the domain of \(JH_*\).

## 4. The remaining exact unstable problem

Naturality of (2)--(6) gives

\[
 h_Ml_4=\partial_{Z'}(\pm2c),\qquad
 h_Ml_4=0\quad\Longleftrightarrow\quad
 2c\in\operatorname{im}\left(
  JH_*:\pi_{15}^sZ'\to\mathbb Z/8\{c\}\oplus\mathbb Z/2\{u\}
 \right).
 \tag{7}
\]

This is the remaining calculation. A nonzero, even injective, map on
the quadratic layers does not prove that the actual unstable composite
is nonzero. Conversely, proving that the specified element (2c) is
a target James--Hopf image proves that composite is zero. The domain
\(\pi_{15}^sZ'\) and its James--Hopf homomorphism can depend on target
cells through dimension16, which the layer truncation did not retain.

## 5. A finite-model strengthening: the James--Hopf image of K has exponent two

**Lemma, independently audited by root and simple_higher.** For the actual finite
space \(K\) in (5),

\[
 2\operatorname{im}(JH_*:\pi_{15}^sK\to\pi_{15}\mathbb D_2K)=0.
 \tag{8}
\]

Consequently (2c), of order four, is not in this finite-model image.
Thus the Moore composite is nonzero in \(\pi_{14}K\), although it may
still become zero in the full (Z'). No equality of the two images
is inferred.

Here is the complete exact-sequence argument. First

\[
 \pi_{15}\mathbb D_2S^7=0.
 \tag{9}
\]

Its integral fifteenth homology is zero, and the intrinsic sixteen-cell
kills the sole bottom-eta possibility, exactly as in the layer proof.
By naturality every bottom-sphere class in the stable groups below has
zero James--Hopf image.

For \(a\in\pi_{15}^sM_4\), the Moore cofiber sequence gives

\[
 q_*a=4j\sigma\in
   \ker(4:\pi_7^s\mathbb S\to\pi_7^s\mathbb S),
 \qquad \pi_7^s\mathbb S_{(2)}=\mathbb Z/16\{\sigma\}.
\]

There is \(b\in\pi_{15}^sM_2\) with \(q_*b=8j\sigma\), again by the
Moore exact sequence. Since \(c_{2,4}\) has top degree one,

\[
 2a-(c_{2,4})_*b\in\operatorname{im}
       (\pi_{15}^sS^7\to\pi_{15}^sM_4).
 \tag{10}
\]

The source James--Hopf map is zero by (4), and the difference in (10)
has zero James--Hopf image by (9). Therefore

\[
 2JH_*(a)=0\qquad(a\in\pi_{15}^sM_4).
 \tag{11}
\]

Next collapse the bottom \(S^7\subset K\). The actual quotient and
the stable connecting map are

\[
 K/S^7\simeq S^8_b\vee M(\mathbb Z/2,8)_r,
 \qquad
 \delta=(4,\eta_8 q):S^8_b\vee M(\mathbb Z/2,8)_r\to S^8.
 \tag{12}
\]

The degree-four component comes from the Moore-four cell. The other
component is zero on the \(r\)-bottom and has top value \(\eta_8\),
so it factors precisely through the pinch \(q:M(2,8)\to S^9\).
This records the eta part of the original nine-cell; it is not discarded.

The existing D.2.38 stable-Moore argument gives

\[
 \pi_{15}^sM(\mathbb Z/2,8)=\pi_7(\mathbb S/2),
 \qquad2\pi_7(\mathbb S/2)=0.
 \tag{13}
\]

Explicitly, \(2x=i\eta qx\), while \(qx\in\pi_6^s\mathbb S\)
is a multiple of \(\nu^2\) and \(\eta\nu^2=0\). These are the
same opened primary low-stem identities used in D.2.38; no table for
an unstable mod-four group is being assumed.

For \(x\in\pi_{15}^sK\), write its quotient image as \((a,\xi)\).
By (12), \(4a+\eta q\xi=0\). The second term vanishes because
\(q\xi\in\mathbb Z/2\{\nu^2\}\) and \(\eta\nu^2=0\). Hence
\(a=4j\sigma\), and an old class from \(\pi_{15}^sM_4\) has exactly
this \(S^8_b\)-coordinate and zero \(M(2,8)_r\)-coordinate.
Subtract such a class. The remaining quotient coordinate \((0,\xi)\)
has order at most two by (13), so twice the remaining class comes
from \(\pi_{15}^sS^7\) by the cofiber exact sequence. Its James--Hopf
image is zero by (9). Combining with (11) proves (8).

All terms in this proof are stable homotopy groups of the displayed
finite spaces, and naturality is used only for actual maps (the bottom
inclusions and the Moore comparison). It proves that the higher cells
of (Z'), rather than merely the elementary Chang relation in its
nine-skeleton, would have to supply a James--Hopf image killing (2c).

## 6. Strengthening: the finite-model James--Hopf map is zero

**Proved; independently audited by root and simple_higher.**
In fact
\[
 JH_*:\pi_{15}^{s}K\longrightarrow\pi_{15}D_2K,\qquad JH_*=0
 \tag{14}
\]
Therefore the quadratic boundary is injective and
\(\partial_K(2c)\) has exact order four. This still concerns the
finite \(K\), not its image in the complete \(Z'\).

### 6.1. Actual low-unit boundaries

Let \(L=M_4\) or \(K\), put \(B=L/S^7\), and let
\(F=\operatorname{hofib}(L\to B)\). In the homotopy pushout square
with initial vertex \(S^7\), both \(S^7\to L\) and \(S^7\to *\)
are seven-connected. Thus Blakers--Massey gives a thirteen-connected
map \(i:S^7\to F\). The exact primary theorem opened for this use
is Goodwillie, *Calculus II*, Section2 p.309 and Theorem2.3 p.310:
<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/goodwillie-calc2.pdf>.
It gives the bound \(7+7-1=13\) for the cocartesian square.

In both cases \(B=\Sigma B'\) and \(\dim B'\le8\). Consequently
the actual boundary \(\Omega B\to F\), restricted to the suspension
unit \(B'\to\Omega B\), factors uniquely through \(i\). Its factor
is determined by stabilization, since maps from dimension at most
eight into \(S^7\) are in the stable range. Compare with
\[
 F\longrightarrow\operatorname{hofib}(QL\to QB)\simeq QS^7.
\]
The natural map of fiber sequences identifies the stabilized factor
with the desuspension of the stable cofiber connecting map. Thus the
actual factors are
\[
 \begin{array}{c|c|c}
 L&B'&B'\longrightarrow S^7\\ \hline
 M_4&S^7&4\iota_7\\
 K&S^7_b\vee M(2,7)_r&(4\iota_7,\eta_7q).
 \end{array}
 \tag{15}
\]
The second row desuspends the already computed matrix
\((4,\eta_8q)\). This is an actual fibration-boundary calculation;
it does not assume an unstable covariant cofiber exact sequence.

### 6.2. Vanishing for the old Moore-four classes

Morisugi--Mukai, printed p.515, states
\[
 \pi_{14}S^7_{(2)}=\mathbb Z/8\{\sigma'\},\qquad
 [\iota_8,\iota_8]=\pm(2\sigma_8-E\sigma').
 \tag{16}
\]
Therefore \(E^\infty\sigma'=2\sigma\), up to sign. The actual
class \(2E\sigma'\in\pi_{15}S^8\) has stable image \(4\sigma\).
The first row of (15) gives its fibration boundary as
\[
 i\bigl((4\iota_7)\circ2\sigma'\bigr)=8i\sigma'=0.
 \tag{17}
\]
The degree-four action here is genuinely additive: \(S^7\) is an
H-space, so its degree-four map induces multiplication by four on
homotopy groups. Equivalently, the Hilton correction vanishes since
\([\iota_7,\iota_7]=0\); the Hilton formula is Lemma1.1 in the same
Morisugi--Mukai paper. There is no omitted unstable quadratic term.

The actual fibration exact sequence supplies a class
\(\widehat a\in\pi_{15}M_4\) with pinch \(2E\sigma'\).
Its stabilization has zero James--Hopf image and stable pinch
\(4\sigma\). An arbitrary stable class of \(M_4\) pinches to
\(4j\sigma\); subtracting \(j\widehat a\) leaves a bottom-sphere
class, also with zero James--Hopf image by (9). Hence
\[
 JH_*:\pi_{15}^{s}M_4\longrightarrow\pi_{15}D_2M_4
 \quad\text{is zero}.
 \tag{18}
\]

### 6.3. The remaining \(\nu^2\)-coextension lifts actually

The stable Moore exact sequence and (13) show that
\(\pi_{15}^{s}M(2,8)=\pi_7(\mathbb S/2)\) is generated by a
bottom \(\sigma\)-class and a lift of \(\nu^2\). Choose the actual
class from Morisugi--Mukai, Lemma2.8(ii), p.523:
\[
 t:S^{14}\longrightarrow M(2,7),\qquad qt=\nu_8^2.
 \tag{19}
\]
Its suspension \(\xi=Et:S^{15}\to M(2,8)\subset B\) has the
required stable pinch. The second row of (15) computes its actual
fibration boundary:
\[
 \partial\xi=i\eta_7qt=i\eta_7\nu_8^2=0.
 \tag{20}
\]
The first composite \(\eta_7\nu_8\) belongs to
\(\pi_{11}S^7\), already the zero fourth stable stem. Thus \(\xi\)
has an actual lift to \(\pi_{15}K\), whose stabilization has zero
James--Hopf image. The other quotient generator is covered by the
actual bottom-\(r\) map \(r\sigma_8:S^{15}\to K\).

Finally any stable class in \(\pi_{15}^{s}K\) has quotient
coordinates \((4j\sigma,\xi')\). Subtract an old Moore-four lift,
the bottom-\(r\) class, and the actual lift from (20), according
to these coordinates. The remainder comes from \(S^7\). All
four kinds of summands have zero James--Hopf image, proving (14).
For the final bottom remainder it suffices that \(JH_{S^7}=0\);
no separate unstabilization claim is used.

The exact order-four conclusion follows from the natural exact
sequence (2). It persists through the additional free nine-sphere
and through ten- and eleven-cells by the same argument as in the
final paragraph of D.2.43. The first possible killing image in the
full target still comes from dimension twelve or higher.
