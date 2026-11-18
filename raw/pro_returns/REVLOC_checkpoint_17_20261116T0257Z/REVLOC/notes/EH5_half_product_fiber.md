# The half-product on the higher cover and the stable connecting map

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Exact reductions only. The stable connecting map,
the full stable Hurewicz image, and the global primary-operation class
of the half-product have not been evaluated.

Write `L=Y<7>`, `L'=Y<10>`, and `P=P_9L`. The established
connectivities are six for `L` and `P`, and nine for `L'`.
The notation `theta` below is the D.2.45 half-product class on `L`.
It is distinct from the D.2.42 secondary square class `Theta` on `L'`.

## 1. A specified predecessor on the fiber

Choose the integral cochains on the Postnikov base representing the
fundamental coefficient class:

\[
 A\in C^7(P;\mathbb Z),\qquad dA=4B,\qquad dB=0.
\]

Their pullbacks to `L` are denoted by the same letters. As in D.2.45,
the actual mod-two product is zero, so choose `C` of degree fourteen
and `E` of degree fifteen with

\[
 dC=A\smile B-2E,\qquad dE=2B\smile B.
\]

Then `theta=[E mod2]`. Use a strict fibration model for
`q:L'→L→P`, with normalized base cochains, so that the restrictions
of `A` and `B` to the actual fiber are literally zero. The class

\[
 k_{14}=[q^*C\bmod2]\in H^{14}(L';\mathbb F_2)
\]

is therefore defined and satisfies

\[
 \tau(k_{14})=x_7y_8,\qquad
 \operatorname{Sq}^1 k_{14}=q^*\theta.
\]

The first formula is the ordinary transgression definition, since
`d(C mod2)` is the pullback of the product of the specified base
classes. The second is the coefficient connecting homomorphism:
`d(q*C)=-2q*E`. There is no mixed Serre term through degree sixteen,
because the least positive base and fiber degrees are seven and ten.
Thus this transgression has no earlier mixed-term indeterminacy.

Changing the compatible nullhomotopy changes `k` and `theta` together;
the displayed relation is asserted for these explicit choices. In
particular it proves that the half-product becomes a first square
on the higher cover. It does **not** show that `theta` is a first
square, or any positive Steenrod operation, on `L` itself. The
nonzero transgression of `k` is exactly why one cannot simply extend
its chosen predecessor over `L`.

The distinction from D.2.42 is essential:

\[
 \tau(k_{14})=x_7y_8,\qquad
 \tau(\Theta_{15})=y_8^2.
\]

The previous proof that `Theta` is outside a specified odd-operation
subspace says nothing by itself about the global positive-operation
class of `theta`.

## 2. The coefficient-lift restriction on possible witnesses

Retain the exact mod-two square nullhomotopy from the transfer note.
Choose an integral `C15` such that

\[
 dC_{15}=B^2+2D_{16}.
\]

Then

\[
 \theta_4=[E-2C_{15}\bmod4],\qquad
 \rho_2\theta_4=\theta,\qquad
 \beta_4\theta_4=-[D_{16}],\qquad
 \beta_{\mathbb Z}\theta=2\beta_4\theta_4
\]

up to the common sign convention for the connecting maps. The last
identity also follows from `[B²]=-2[D16]`.

If an integral fifteen-cycle class `z` has order at most two, its
evaluation under the mod-four class `theta4` lies in `{0,2}`.
Reduction modulo two gives

\[
 \langle\theta,\rho_2 z\rangle=0.
\]

Thus a stable map whose James–Hopf image is `2c` must have an
integral stable Hurewicz image of order at least four. This is a
restriction on the **image** of the stable Hurewicz map; a bound on
the abstract homotopy group alone has not been supplied. The root
and simple-higher agent independently checked this coefficient
argument directly.

## 3. An exact stable cofiber reformulation

Let `C_q` be the homotopy cofiber of the fiber inclusion `L'→L`.
The canonical comparison

\[
 C_q\longrightarrow P
\]

is sixteen-connected. One can obtain this from Blakers–Massey applied
to the defining pushout: `L'→L` is six-connected and `L'→*` is
ten-connected, so the comparison from `L'` to the new homotopy
fiber is fifteen-connected. Comparing the two fiber sequences gives
the stated one-higher connectivity on the bases. This is the exact
Goodwillie II §2, Theorem 2.3 form already opened for D.2.43.

The stable cofiber sequence consequently gives an exact segment

\[
 \pi_{15}^{s}L\longrightarrow\pi_{15}^{s}P
       \xrightarrow{\delta}\pi_{14}^{s}L'.
\]

The replacement of `C_q` by `P` in this segment is justified by the
sixteen-connectivity just proved. It is not a claim that suspension
spectra preserve the entire original homotopy-fiber sequence.

The natural quadratic comparison of D.2.43 gives an isomorphism

\[
 JH_P:\pi_{15}^{s}P\xrightarrow{\cong}
       \pi_{15}D_2P\cong\mathbb Z/8\{c\}\oplus\mathbb Z/2\{u\}.
\]

Indeed `P` is six-connected, and its ordinary homotopy groups in
degrees fourteen and fifteen are zero. These degrees are within
the `3 conn(P)=18` Goodwillie comparison range. The quadratic map
induced by `L→P` is an isomorphism in this degree, as its value is
already fixed by the common low skeleton.

Therefore the remaining exact test can equivalently be written

\[
 \delta\bigl(JH_P^{-1}(2c)\bigr)=0.
\]

Nine-connectivity of `L'` identifies its degree-fourteen ordinary
and stable homotopy groups, but this does not evaluate `delta`.
Without further Postnikov or attaching-map information this is a
reformulation of the original obstruction, not a solution of it.

Finally `q*theta=Sq1(k)` shows directly that the half-product pairing
vanishes on every stable spherical class coming from `L'`. The
positive Steenrod operation is stable, so this assertion does not
require an unstated desuspension of a map. It explains why any
nonzero pairing must occur on the part projecting nontrivially to
the explicitly displayed Postnikov stable group.
