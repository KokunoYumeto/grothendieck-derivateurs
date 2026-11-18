# A34.6: optional finite-loop strengthening

This is a separately checked refinement, not an actual A.3 example or an impossibility proof. It does not assert that one witness can be given all loop structures simultaneously.

## F1. Each prescribed finite loop degree can be imposed

Keep the generator A, its stable ideal L_A, the integer d, and the hypothetical X constructed in A34.6. For every fixed integer m≥1 put

\[
H_m=\Omega^m\Sigma^{m+d}X,\qquad Z_m=P_AH_m.
\]

Then Z_m is a noncontractible d-connected primary A-null **m-fold loop space**, and Σ∞Z_m belongs to L_A. The same generator A works for every m; the spaces Z_m may depend on m.

### Proof

The space Y=Σ^dX is connected. May's approximation Theorems 2.7/6.1 identify C_mY with Ω^mΣ^mY. The little-cubes filtration has quotients

\[
\mathcal C_m(r)_+\wedge_{\Sigma_r}Y^{\wedge r}.
\]

Snaith Theorem 1.1 splits these stably. Each quotient spectrum belongs to loc(Σ∞Y): the coefficient space has free symmetric-group action, so the orbit construction is a homotopy-orbit construction, and a localizing tensor ideal is closed under smash products and homotopy colimits. Thus Σ∞H_m∈L_A. Connectivity of iterated suspension and loops makes H_m d-connected, and integral homology away from p vanishes. Cone attachments in A-nullification preserve this connectivity, primary homology, and stable membership in L_A exactly as in A34.6.

The suspension-loop adjunction triangle displays Σ^{m+d}X as a homotopy retract of Σ^mH_m. If H_m were W_A-aspherical, retract, suspension, and reversible desuspension closure would make X aspherical. Hence H_m is not W_A-aspherical. The H-space comparison A34.6.4 now gives Z_m≠*.

The exact primary source for preserving the loop structure is Bousfield, *Homotopical localizations of spaces* (1997), **Theorem 5.2**, printed p. 1330: for a pointed map f and connected Y, the canonical comparison

\[
L_f\Omega Y\longrightarrow\Omega L_{\Sigma f}Y
\]

is an equivalence. This statement and its preceding construction were reopened in the downloaded original. Taking f=A→* and iterating (all intervening deloopings here are connected) gives the actual equivalence

\[
P_A\Omega^m\Sigma^{m+d}X
\simeq\Omega^mP_{\Sigma^m A}\Sigma^{m+d}X.
\]

This supplies an m-fold delooping of Z_m; no unsupported operadic-coherence inference from product preservation is required.

## Exact access and limits

Theorem 5.2 is stated in the published Bousfield 1997 paper and credits the earlier Bousfield/Dror Farjoun proofs. Its original 1994 proof was not obtained: both web and ordinary HTTPS requests to the AMS PDF returned 403. The 1997 theorem itself is a primary-source statement by the same author, opened locally at `sources/A34_Bousfield_1997.txt` and available in `sources/A34_Bousfield_1997.pdf`. The present result imports that theorem rather than claiming to reprove its original localization argument.

The May and Snaith source scope is precisely that recorded for A34.6: the author-hosted May transcription, Theorems 2.7/6.1 and configuration Theorem 4.8; published Snaith Theorem 1.1 and its filtration. The free finite-m coefficient action and exact stable-ideal membership are explicitly checked above.

There is no passage from the family {Z_m} to a nonzero infinite-loop witness. In particular, a sequential homotopy colimit of A-null spaces need not be A-null, and underlying-space homotopy colimits do not commute with nullification merely because nullification is a reflector.
