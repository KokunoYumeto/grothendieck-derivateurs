# The concrete Hopf attachment: finite obstruction reduction

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15, 15:30 UTC.

This note concerns an actual attachment relevant to D.2.12. It does **not** establish an extension or a nonextension, and does not establish survival through a second nullification stage. The compactness argument below was independently checked by the axioms agent.

## The precise extension problem

Put

\[
B=K(\mathbb F_2,2),\qquad X=\Sigma B,\qquad A=QX,\qquad
Y=\Sigma^2B,\qquad U=\Sigma^2X=\Sigma^3B.
\]

Let \(j:X\to QX\) be the stabilization unit and let

\[
h_0=\eta_2\wedge\mathrm{id}_B:U\longrightarrow Y,
\]

where \(\eta_2:S^3\to S^2\) is the Hopf map. The question is whether there is a pointed map

\[
h:\Sigma^2QX\longrightarrow Y,
\qquad h\circ\Sigma^2j\simeq h_0.
\tag{1}
\]

The cofiber of \(h_0\) is \(\mathbb CP^2\wedge B\). If \(x\) denotes the degree-two class of \(\mathbb CP^2\), and \(u,v=\operatorname{Sq}^1u\) are the classes of degrees two and three in \(B\), then the old classes \(xu,xv\) have nonzero product \(x^2uv\). Thus this map illustrates concretely how a homology-zero attachment can destroy the commutator obstruction used in D.2.12. It is not yet an attachment with source a suspension of \(A\); that is exactly what (1) asks.

## 1. The map is stably essential

The mod-two homology map of \(h_0\) is zero in every degree, since the homology map of \(\eta_2\) is zero. Nevertheless \(\Sigma^\infty h_0\ne0\).

Indeed the unique nonzero bottom cohomology class of its cofiber has degree four and is \(xu\). The Cartan formula gives

\[
\operatorname{Sq}^3(xu)=x^2\operatorname{Sq}^1u=x^2v\ne0.
\tag{2}
\]

Here \(\operatorname{Sq}^2x=x^2\), \(\operatorname{Sq}^1x=0\), and \(\operatorname{Sq}^3u=0\). If \(\Sigma^\infty h_0\) were zero, its cofiber would split, compatibly with the map from \(Y\), as

\[
\Sigma^2\Sigma^\infty B\ \vee\ \Sigma^4\Sigma^\infty B.
\]

The second summand begins in degree six. The unique class in degree four would therefore have \(\operatorname{Sq}^3=0\), contradicting (2). This also prevents treating the problem as a phantom extension of a null stable class.

The only cohomology input is Serre's explicit computation of \(H^*K(\mathbb F_2,2)\), already opened for D.2.12: *Cohomologie modulo 2 des complexes d'Eilenberg--MacLane*, §1 nos.2.1--2.4 and §2 nos.8--9, especially printed pp.199,203--204:

<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf>.

## 2. Compatible extensions through the first two stabilization stages

Write

\[
C_mX=\Omega^m\Sigma^mX,\qquad S_m=\Sigma^2C_mX.
\]

There are stabilization maps \(C_mX\to C_{m+1}X\), and \(\operatorname{hocolim}_m C_mX\simeq QX\). For \(0\le m\le2\), the suspension--loop counit supplies a map

\[
r_m=\Sigma^{2-m}\varepsilon^{(m)}_{\Sigma^mX}:
\Sigma^2\Omega^m\Sigma^mX\longrightarrow\Sigma^2X=U.
\tag{3}
\]

Here \(\varepsilon^{(m)}:\Sigma^m\Omega^m\to\mathrm{id}\) is the iterated counit, and \(r_0=\mathrm{id}\). The triangle identity gives \(r_m\Sigma^2j_m\simeq\mathrm{id}_U\), where \(j_m:X\to C_mX\) is the unit. Consequently

\[
h_m=h_0r_m:S_m\longrightarrow Y
\tag{4}
\]

extends \(h_0\) for \(m=1,2\).

These two choices are compatible under stabilization. This follows from naturality of the counit and its triangle identity. For example, in the comparison from \(m=1\) to \(m=2\), naturality moves the map \(\Sigma X\to\Omega\Sigma^2X\) across the inner counit; the composite of its suspension with the outer counit is the identity of \(\Sigma^2X\). Thus the resulting composite is precisely \(\Sigma\varepsilon_{\Sigma X}=r_1\).

No analogous unsuspended counit is available from (3) once \(m>2\). This failure of the construction is not evidence that a different extension does not exist.

## 3. Finiteness needed for compactness

Every integral homology group of \(B\) in positive degree is a finite 2-group. One can obtain this directly from the bar construction, or from Serre's class theorem for Eilenberg--MacLane spaces. Suspension preserves this property. The simply connected spaces \(\Sigma^mX\) and \(Y\) therefore have finite 2-primary homotopy groups in every degree.

The exact primary reference opened here is Serre, *Groupes d'homotopie et classes de groupes abéliens*, Ann. Math. 58 (1953), 258--294:

<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Classes.pdf>.

Chapter I, §6.4 (p.265) verifies the Serre-class hypotheses for finite groups supported at a given collection of primes. Chapter II, Proposition 8 (p.271) gives the homology assertion for Eilenberg--MacLane spaces. Chapter III, Theorem 1 and its proof, followed by Corollaries 1--2 (pp.272--274), give the homotopy assertion used above. The theorem's proof through the connected-cover tower and the displayed corollaries were opened and read.

In particular \(C_mX\) has finite homotopy groups in each degree and is 2-connected. These spaces, \(U\), \(S_m\), and \(\Sigma^2QX\) admit countable CW models of finite type. For the compactness argument it would suffice to use countable CW exhaustions by finite subcomplexes; a finite-dimensional source is not being assumed.

For a finite pointed CW complex \(K\), the set \([K,Y]_*\) is finite. To see this, replace \(Y\) by the Postnikov section through \(\dim K\), then use its finite sequence of obstruction groups, which are cohomology groups of \(K\) with finite coefficients. The same argument, applied to \(S^1\times K\) relative to the fixed copy of \(K\), makes \(\pi_1\operatorname{Map}_*(K,Y)\) finite at every component. The possible twisting in a nonconstant mapping component does not change finiteness.

If \(K=\bigcup_sK_s\) is a countable CW exhaustion by finite subcomplexes, then

\[
[K,Y]_*\ \cong\ \varprojlim_s[K_s,Y]_*.
\tag{5}
\]

Surjectivity is the usual mapping-tower/Milnor argument. The kernel over each compatible component is a \(\varprojlim^1\) of the finite groups \(\pi_1\operatorname{Map}_*(K_s,Y)\). Each such tower is Mittag--Leffler, because its images in a fixed finite group form a descending sequence of subgroups. Its \(\varprojlim^1\) is therefore trivial. This proves injectivity as well as surjectivity in (5). Equivalently, one may realize compatible maps and homotopies directly on the mapping telescope. This is the same finite-target phantom argument used in D.3.4; it does not require an infinite weak product to be a product.

Giving the finite sets on the right of (5) their discrete topology makes \([K,Y]_*\) compact and Hausdorff. It is a profinite set. A map of countable CW sources induces a continuous map on these sets: each finite source subcomplex maps, after cellular approximation, into a finite target subcomplex, so every finite coordinate factors through a finite coordinate. The topology is independent of the chosen finite exhaustion by the same argument.

## 4. No purely infinite compatibility obstruction

Define

\[
E_m=\{[f]\in[S_m,Y]_*:f\Sigma^2j_m\simeq h_0\}.
\tag{6}
\]

By (5), this is a closed subset of a compact Hausdorff profinite set. Indeed it is the inverse image of the singleton \([h_0]\) under the continuous restriction map to \([U,Y]_*\). The stabilization maps give continuous maps \(E_{m+1}\to E_m\).

Suppose every \(E_m\) is nonempty. Then

\[
\varprojlim_mE_m\ne\varnothing.
\tag{7}
\]

This does not require the bonding maps to be surjective. In the product of the nonempty compact spaces \(E_m\), the compatibility conditions are closed and have the finite intersection property: to satisfy finitely many of them, choose a point at the largest index involved and take its images at lower indices. Compactness gives (7).

Choose a compatible family in (7). The usual Milnor surjection

\[
[\operatorname{hocolim}_mS_m,Y]_*\longrightarrow
\varprojlim_m[S_m,Y]_*
\]

realizes that family by an actual map. Since suspension commutes with this homotopy colimit, its source is \(\Sigma^2QX\). Its restriction to \(U=S_0\) is \(h_0\), so it solves (1).

We have proved the exact equivalence:

> The Hopf attachment extends across \(\Sigma^2X\to\Sigma^2QX\) if and only if it extends across every finite stabilization stage \(\Sigma^2X\to S_m\).

Because (4) handles \(m=1,2\), a negative answer must already appear at a finite stage \(m\ge3\). There cannot be an obstruction consisting solely of failure to choose compatible infinitely many stage extensions.

There is also a finite-subpair detection statement. Replace \(U\to S_m\) by its mapping-cylinder CW pair. Exhaust that countable pair by finite subpairs and impose the fixed restriction \(h_0\) on each. Relative mapping classes form finite sets, by the same Postnikov obstruction argument. If every finite subpair admits an extension, compactness and the mapping-tower argument give an extension on the entire pair. Thus nonextension at a fixed \(m\) is witnessed on a finite relative subcomplex. This formulation avoids treating a mere homotopy map of CW spaces as a literal subcomplex inclusion.

## 5. An initial connectivity bound

The space \(X=\Sigma B\) is 2-connected, so \(\Sigma^mX\) is \((m+2)\)-connected. Freudenthal makes

\[
\Sigma^mX\longrightarrow Q\Sigma^mX
\]

\((2m+5)\)-connected. Looping \(m\) times gives an \((m+5)\)-connected map \(C_mX\to QX\), and suspending twice gives an \((m+7)\)-connected map

\[
S_m\longrightarrow\Sigma^2QX.
\tag{8}
\]

In particular \(S_2\to\Sigma^2QX\) is 9-connected. A relative CW approximation may therefore be chosen with no cells of dimension at most nine. The explicitly constructed \(h_2\) has already dealt with this range. Its first possible cellular extension obstruction is on a relative 10-cell and lies in \(\pi_9(Y)\). A map representing the full extension may restrict to a different member of \(E_2\); failure of this particular \(h_2\) would not by itself show \(E_3=\varnothing\).

The argument in Section 7 below improves this bound for this specific \(h_0\): the obstructions on relative 10- and 11-cells both vanish.

## 6. Stable and periodic calculations still required

There is always a stable extension: compose the suspension-spectrum/infinite-loop counit

\[
\Sigma^2\Sigma^\infty QX\longrightarrow\Sigma^2\Sigma^\infty X
\]

with \(\Sigma^\infty h_0\). A general unstable extension need not stabilize to this canonical choice. It can differ by any stable map which is zero on the weight-one summand of the Snaith splitting. Thus nonrealizability of this one stable map would not rule out all solutions of (1).

For the double adjunct, periodic Lie theory supplies a necessary factorization of the map induced by \(h_0\):

\[
M(\Sigma B)\longrightarrow
\operatorname{triv}(L_{T(2)}\Sigma^\infty\Sigma B)
\longrightarrow\Omega^2M(\Sigma^2B).
\]

The first arrow is the image of the ordinary unit. At this low connectivity it has not been identified with the unit of stabilization internal to the periodic category. Indeed \(M(B)=0\), while \(L_{K(2)}\Sigma^\infty B\ne0\), so commuting ordinary suspension spectra through \(M\) would be false without additional hypotheses. The actual Lie algebra of \(M(\Sigma^2B)\), and the particular map induced by \(\eta_2\wedge B\), have not been calculated. Being a suspension does not justify replacing this target by a free spectral Lie algebra. Nor have loops of a spectral Lie algebra been identified with a trivial algebra.

The one-adjunction James--Hopf/cohomology test does not give a contradiction: projecting source homology to the stable weight-one part and using the actual homology map on \(\Sigma^3B\) gives a compatible primary Steenrod/coalgebra map. A genuine nonextension proof must control further unstable structure, or calculate a finite-stage relative obstruction while allowing all choices of the preceding extension. The finite-stage compactness result makes such a calculation sufficient in principle; no such obstruction has yet been proved nonzero.

## 7. The canonical extension passes relative dimensions ten and eleven

This is a positive improvement of the initial bound, with no claim about higher cells.

First,

\[
\pi_5(Y)=0.
\tag{9}
\]

Indeed the unit \(B\to\Omega\Sigma B\) is 3-connected, since \(B\) is 1-connected. The next unit \(\Sigma B\to\Omega\Sigma^2B\) is 5-connected, so its loop is 4-connected. Thus the composite

\[
B\longrightarrow\Omega^2\Sigma^2B
\]

is 3-connected and is surjective on \(\pi_3\). Its source has \(\pi_3(B)=0\), proving (9).

Choose a CW model of \(X=\Sigma B\) with a single bottom 3-cell, and write \(i:S^3\to X\) for its inclusion. The bottom \(H_3(X;\mathbb Z)=\mathbb Z/2\) is generated by this cell. Set

\[
X'=X/S^3,\qquad q:X\longrightarrow X'.
\]

The quotient is 3-connected. For example the cofiber homology sequence gives \(\widetilde H_i(X';\mathbb Z)=0\) for \(i\le3\); it is simply connected, so Hurewicz gives the assertion. This can equally be checked by its CW structure.

Equation (9) makes \(h_0\Sigma^2i:S^5\to Y\) null. Choose such a nullhomotopy. The cofiber universal property supplies a map

\[
g:\Sigma^2X'\longrightarrow Y,
\qquad g\Sigma^2q\simeq h_0.
\tag{10}
\]

Apply the construction (3) to \(X'\), and define

\[
h_2'=g\varepsilon^{(2)}_{\Sigma^2X'}:
\Sigma^2\Omega^2\Sigma^2X'\longrightarrow Y.
\]

Because \(X'\) is 3-connected, Freudenthal now gives an 11-connected stabilization map

\[
t':\Sigma^2\Omega^2\Sigma^2X'\longrightarrow\Sigma^2QX'.
\tag{11}
\]

Take the homotopy pullback

\[
P=(\Sigma^2QX)\mathbin{\times^h_{\Sigma^2QX'}}
       (\Sigma^2\Omega^2\Sigma^2X'),
\tag{12}
\]

using \(\Sigma^2Qq\) and \(t'\). The projection \(p:P\to\Sigma^2QX\) is 11-connected, because homotopy pullback preserves the homotopy fibers and their connectivity. Naturality of stabilization gives a lift

\[
\widetilde t:S_2=\Sigma^2\Omega^2\Sigma^2X\longrightarrow P
\]

of the usual map \(S_2\to\Sigma^2QX\). Define \(\widetilde h:P\to Y\) by the second projection followed by \(h_2'\). Naturality of the counit and (10) give

\[
\widetilde h\widetilde t
\simeq g\varepsilon^{(2)}_{\Sigma^2X'}\Sigma^2\Omega^2\Sigma^2q
\simeq g\Sigma^2q\varepsilon^{(2)}_{\Sigma^2X}
\simeq h_0\varepsilon^{(2)}_{\Sigma^2X}=h_2.
\tag{13}
\]

Replace \(p\) by a fibration, retaining the specified lift of \(S_2\). Its homotopy fiber is 10-connected. In any relative CW approximation of \(S_2\to\Sigma^2QX\), the map to \(\Sigma^2QX\) therefore lifts to \(P\) over every relative cell of dimension at most eleven: the obstruction for a cell of dimension \(d\) lies in \(\pi_{d-1}\) of that fiber, which is zero for \(d\le11\). Composing the lift with \(\widetilde h\) proves that the chosen canonical \(h_2\) extends through relative dimension eleven.

The same conclusion applies to the corresponding relative skeleta of \(S_2\to S_m\) for every \(m\ge3\), by pulling the construction back again. In particular neither the first weight-two E3 cell in dimension ten nor any relative cell in dimension eleven gives a nonzero obstruction for this canonical choice. The first still-possible obstruction is on a relative 12-cell, in \(\pi_{11}(Y)\). This is a lower bound on where an obstruction can occur; it is not a calculation of that group or a proof that an obstruction there is nonzero.


## 8. The next spherical class has order two, not four

There is a useful correction to the tentative dimension-twelve test. In fact

\[
\pi_6(Y)\cong\mathbb Z/2.
\tag{14}
\]

Here is a source-checked computation. The unit of connective real K-theory
\(\mathbb S\to ko\) is an isomorphism on homotopy in degrees zero, one and two,
and is surjective in degree three. Its cofiber therefore has no homotopy in
degrees below four. Since \(\Sigma^\infty B\) has no homotopy in degrees below
two, smashing this cofiber with \(\Sigma^\infty B\) gives a spectrum with no
homotopy below degree six. The cofiber exact sequence gives

\[
\pi_4^s(B)\cong\widetilde{ko}_4(B).
\]

Davis's computation gives \(\widetilde{ko}_4(B)=\mathbb Z/2\). The exact opened
primary source is Donald M. Davis, *The connective KO theory of the
Eilenberg--MacLane space K(Z/2,2)*, manuscript dated 19 February 2025:

<https://www.lehigh.edu/~dmd1/109p.pdf>.

Theorem 1.3, printed p.4, decomposes the reduced groups into the indicated
modules and an omitted trivial module. Figure 2.1, p.5, was rendered and
visually read; the degree-four part of its first module is one copy of
\(\mathbb Z/2\). Section 11, p.58, gives the explicit derivation and states
that this first module has only the two copies of \(\mathbb Z/2\), in degrees
two and four. Section 10, p.52, computes the omitted trivial module's
Poincare series, whose first term is degree six. All other modules in the
displayed decomposition start above degree four. The familiar low-degree
coefficient classes of \(ko\), including the nonzero images of \(\eta\) and
\(\eta^2\), are also displayed in Figure 3.2, p.9.

Finally, since \(Y\) is 3-connected, Freudenthal identifies \(\pi_6(Y)\)
with its stable group \(\pi_6^s(Y)=\pi_4^s(B)\), proving (14).

The bottom Moore subcomplex of \(X\) is \(M(\mathbb Z/2,3)\). Its image after
quotienting the bottom sphere is the bottom sphere \(S^4\to X'\). Let
\(\alpha:S^6\to Y\) be the restriction of the map \(g\) in (10) to its
double suspension. Then \(\alpha\) is the nonzero element of (14), and is
independent of the chosen nullhomotopy on the bottom \(S^5\).

For completeness, the restriction of \(h_0\) to the double suspension of
that Moore subcomplex, namely \(M(\mathbb Z/2,5)\), is nonzero. Its cofiber
has the unique bottom mod-two cohomology class in degree four, and its
\(\operatorname{Sq}^3\) is nonzero. This follows by comparing the cofiber
with \(\mathbb CP^2\wedge M(\mathbb Z/2,2)\): pullback of the class and its
operation is respectively \(xu\) and \(x^2v\ne0\). A null attachment would
split this cofiber as \(Y\vee\Sigma M(\mathbb Z/2,5)\); its unique bottom
class would come from \(Y\), where its \(\operatorname{Sq}^3\) is zero.
This is a contradiction. Applying pointed mapping classes into \(Y\) to

\[
S^5\xrightarrow{2}S^5\longrightarrow M(\mathbb Z/2,5)
\longrightarrow S^6\xrightarrow{2}S^6
\]

and using \(\pi_5(Y)=0\) and (14) shows that
\([M(\mathbb Z/2,5),Y]_*\) is exactly \(\mathbb Z/2\), with its nonzero
class induced by \(\alpha\). Changes of the chosen bottom nullhomotopy
alter \(\alpha\) by an element of \(2\pi_6(Y)=0\).

The ordinary mod-two Hurewicz image of \(\alpha\) is **zero**. The quotient
\(M(\mathbb Z/2,5)\to S^6\) induces an isomorphism on degree-six mod-two
homology, whereas \(h_0\) induces zero on all mod-two homology. In particular
one must not identify \(\alpha\) with a spherical mod-two class dual to
\(u^2\). A potentially nonzero double-loop Hurewicz image is a different
question and is compatible with this zero ordinary Hurewicz image.

Consequently, the proposed integral/mod-four test using an order-four
class representing \(\alpha\) does not apply. Its Whitehead square
\([\alpha,\alpha]\in\pi_{11}(Y)\) has not been computed here. Even a
nonzero value would first obstruct the specified counit extension on the
bottom free double-loop subspace; it would not by itself exclude all
choices of an extension on \(S_2\). An arbitrary map out of that space
need not preserve its Browder operation. The required control of those
choices remains a separate, unresolved step.


## 9. Why the quotient's first universal obstruction is not yet the answer

Two independent precautions are necessary at relative dimension twelve.
First, the low twice-adjoint calculation is now checked separately in
`FGH_D2_E2_eta_extension.md`: the double-loop Hurewicz image of the class
\(\alpha\) is the Pontryagin square \(a^2\), where \(a\) is the degree-two
bottom class of \(B\subset\Omega^2Y\). The Browder derivation identity gives
\(\lambda_1(a^2,a^2)=0\) over \(\mathbb F_2\). Thus ordinary mod-two
Browder homology does not detect \([\alpha,\alpha]\). Together with (14),
this excludes both of the proposed immediate homology detectors; it does
not prove that the Whitehead square is zero.

Second, the bottom sphere of \(X'\) has no spherical lift to the original
infinite-loop source. Indeed the same low-degree comparison with \(ko\)
and Davis's first-module computation give

\[
\pi_4(A)=\pi_3^s(B)=0,\qquad \pi_4(X')\cong\mathbb Z.
\tag{15}
\]

The nonzero mod-two homology map in degree four under \(Qq\) is compatible
with (15): it is the familiar Moore-quotient phenomenon, with the source
class arising from the \(\operatorname{Tor}\) term on its integral
\(H_3=\mathbb Z/2\). The quotient map
\(M(\mathbb Z/2,3)\to S^4\) itself is the elementary model for this
behavior. It has nonzero degree-four mod-two homology but zero map from
its finite \(\pi_4\) into \(\pi_4(S^4)=\mathbb Z\).

Consequently, even a computation of a nonzero first universal obstruction
for the bottom \(S^4\) in \(X'\) must still be pulled back through the
actual map \(\Sigma^2Qq\) in (12). Its survival on that pullback, with all
choices over the preceding relative cells allowed, has not been proved.
This is an additional issue to the failure of a canonical counit choice
to control every possible extension on \(S_2\).

The established conclusion remains: dimensions at most eleven admit the
specified extension; nonextension, if true, occurs at a finite stage and
on a finite relative subpair; the first remaining candidate is dimension
twelve. Neither an extension on all of \(\Sigma^2QX\) nor a nonzero
all-choices obstruction is currently established.


## 10. A finite failure of the canonical choice is now proved

The later calculation, fully written in `sections/D2_hopf_extension.tex`
as D.2.13 by the axioms agent, changes the status of the canonical
extension. It does **not** settle the arbitrary extension question.
I read that complete proof independently, checked the target's free
\(E_2\) coefficient basis, and visually checked the exact source formula
in Cohen--Lada--May, Chapter III, Theorem 1.3, printed pp.217--218.

Write \(C=\sigma c\) in degree five, with
\(c\in H_4B\) dual to \(u^2\), and \(A_0=\sigma a\) in degree three.
The prescribed map has \(g_0(C)=\xi_1a\). At the fourth loop stage,
\(\xi_3C=Q^8C\) is the top operation and its correct formula is

\[
\operatorname{Sq}_*^2\xi_3C
 =Q^6C+\lambda_3(C,A_0).
\]

The coefficient of the first term is
\(\binom{6}{2}=15=1\pmod2\). The possible term \(Q^7\beta C\)
is zero. Because \(\beta C=\beta A_0=0\), the Browder term has
zero Bockstein. Therefore

\[
\beta\operatorname{Sq}_*^2\xi_3C=C^2.
\]

In the target \(T=\Omega^2Y\), let \(\lambda\) select the coefficient
of \((\xi_1a)^2\). The free \(E_2\) basis and its exact top-operation
relations give \(\lambda\beta\operatorname{Sq}_*^2=0\) on
\(H_{13}T\). Thus every ordinary map \(G:C_4X\to T\) has
\(\lambda G(C^2)=0\). The prescribed double-loop map
\(g_2=\Omega^2h_0\) instead has
\(g_2(C^2)=(\xi_1a)^2\), since it is multiplicative.
Consequently the canonical \(h_2\) does not extend to \(S_4\).
The same coefficient identity proves that a full ordinary extension,
if it exists, must fail to preserve this Pontryagin square; no H-map
extension is possible.

This is consistent with the positive range through relative dimension
eleven. The necessary primitive correction in homology degree ten is
not ruled out for an arbitrary map: a polynomial coalgebra on a
primitive class has its powers \(C^{2^j}\) as independent primitive
coalgebra generators (Lucas's binomial identity identifies it, as a
coalgebra, with the tensor product of the two-dimensional primitive
coalgebras on those powers). Hence ordinary coalgebra naturality alone
does not force the image of \(C^2\) from the image of \(C\).

A proposed further argument via the binary multiplication deviation
would require a coherently symmetric factorization through the full
homotopy-orbit square \(D_2A\). An arbitrary map into an \(E_2\)-space
does not supply that \(EC_2\)-coherence. The finite commutativity
parameter and the full homotopy-orbit square cannot be interchanged.
No such factorization has been established here. This is the precise
gap in using the same \(\beta\operatorname{Sq}^2\) calculation to forbid
the primitive correction for every ordinary map.


## 11. An explicit primitive correction in the ordinary-map problem

The nonprimitive labels in the double-loop target provide additional
primitive classes. This is a concrete reason that the tensor argument
of D.2.12 does not transfer unchanged to this target. It does not solve
the required correction involving \((\xi_1a)^2\).

For \(i\ge1\), let \(c_i\in H_{2i}B\subset H_{2i}T\) be dual to
\(u^i\), and put \(c_0=1\), \(c_1=a\). These are labels, not
Pontryagin powers. Their coalgebra and Steenrod formulas are

\[
\Delta c_k=\sum_{i+j=k}c_i\otimes c_j,\qquad
\beta c_k=0,\qquad
\operatorname{Sq}_*^2c_k=(k-1\bmod2)c_{k-1}.
\]

The coproduct is dual to multiplication of the powers of \(u\).
The operation formula follows from Cartan and
\(\operatorname{Sq}^2u=u^2\): the coefficient of \(u^k\) in
\(\operatorname{Sq}^2(u^{k-1})\) is \(k-1\). No monomial involving
another Serre generator can acquire a pure power of \(u\) under this
operation. The assertions in \(T\) follow by naturality of its unit
map from \(B\).

Introduce the formal group-like series
\(H(t)=\sum_{k\ge0}c_kt^k\). Every coefficient of
\(tH'(t)H(t)^{-1}\) is primitive: apply the coproduct, differentiate
\(\Delta H=H\otimes H\), and multiply by its inverse. The coefficient
of \(t^5\) is the explicit degree-ten class

\[
 p_5=a^5+a^3c_2+a c_2^2+c_2c_3+a^2c_3+a c_4+c_5.
\]

It is primitive and satisfies

\[
\beta p_5=0,\qquad \operatorname{Sq}_*^2p_5=a^4.
\]

For the second identity, the term \(a^3c_2\) contributes \(a^4\),
the two terms \(c_2c_3\) and \(a c_4\) each contribute \(a c_3\),
and the other terms contribute zero. The latter two cancel.

Moreover \(p_5\) maps to zero under the double-loop evaluation
\(T\to B\). That map is multiplicative. On the pure-label part of
\(H_*B\), multiplication is the divided-power multiplication
\(c_ic_j=\binom{i+j}{i}c_{i+j}\), dual to the primitive fundamental
cohomology class \(u\) for the abelian H-space \(B\). Under this
multiplication the only surviving two terms in \(p_5\) are
\(a c_4=c_5\) and \(c_5\), which cancel.

Thus the kernel of evaluation on homology already contains
an explicit primitive correction with a nonzero prescribed
\(\operatorname{Sq}_*^2\)-image. In particular, a proposed argument
using \(\operatorname{Sq}_*^2(BD)=B^2\) to force preservation of the
square of the degree-four source label must account for this
correction. It cannot infer the answer merely from the coproduct of
\(BD\). The independent top-operation coefficient obstruction in
D.2.13 is unaffected, since \(p_5\) has no \(\xi\)-generator coefficient.


## 12. Resolution of this particular extension problem

The previously open all-choices extension in this historical note is now
excluded by D.2.16, proved in `sections/D2_eta_nonextension.tex` and
`notes/I_eta_deviation.md`. Every ordinary map C4(Sigma B) -> Omega^2
Sigma^2B has zero coefficient of xi a on the source class sigma c.
The prescribed Hopf map has that coefficient one. Thus there is no
extension even at stage four, and hence no extension to Sigma^2 Q Sigma B.
Root and the axioms agent independently checked the exact target
cohomology identities, actual multiplication-deviation map, and finite
source Steenrod contradiction. The canonical stage-two extension and
relative-dimension-eleven extension recorded above remain valid.

The ordinary nullification question remains open: this excludes one
particular dangerous attachment and a specified coefficient for all maps,
not every possible subsequent attachment.
