# The two-primary four-sphere group and the suspended epsilon relation

Status: exact primary-author statements opened and checked on 2026-11-15.
This is a source audit for the universal Moore-composition calculation;
it does not evaluate that composition.

## Sources and precise locations

Neil P. Strickland, *A Mathematica representation of some unstable
homotopy groups of spheres*, author PDF:
<https://strickland1.org/toda/toda.pdf>.

* Proposition 7, printed page 7, displays
  `pi_14(S^4)_(2) = Z/8{nu_4 sigma'} + Z/4{E epsilon'}
  + Z/2{eta_4 mu_5}`.  The source explicitly attributes the group
  and orders to Toda, Theorem 7.3.
* Proposition 13, printed pages 8--9, proves
  `(E nu') sigma' = 2 E epsilon'`.
* Proposition 7 also records that both `nu_4 sigma'` and `E epsilon'`
  suspend to `2 nu_5 sigma_8`, up to the stated sign convention;
  `eta_4 mu_5` suspends to `eta_5 mu_6`.
* The author's companion source file
  <https://strickland1.org/toda/Toda.m>, relation beginning at line 1855,
  explicitly gives
  `eta_4 eta_5 epsilon_6 = 2 E epsilon'`, by suspending
  `eta_3 eta_4 epsilon_5 = 2 epsilon'` from Toda, Lemma 6.6.

The original page of Toda's book has not been opened in this audit.
Consequently the exact locator is recorded as a source attribution
within the opened author note/code, not as an independently opened
copy of Toda.

## Audit of the Hopf step in Proposition 13

The note warns on printed page 2 that a general composite formula for
the James--Hopf invariant has a problematic published proof.  The
warning must not be omitted when importing an arbitrary consequence
from its code.  In the present calculation the problem can be avoided.

The formula is valid if either input is a suspension, and is valid
after one suspension in general, as explicitly stated there.  Thus
it applies directly to `(E nu') sigma'`.  For `nu_4 sigma'`, its
possible quadratic correction is `nu_7 nu_10 eta_13`, which is zero
because `nu_10 eta_13=0` in the stable fourth stem.  Moreover suspension
is injective on `pi_14(S^7)_(2)=Z/8{sigma'}`: `E sigma'` still has order
eight (Toda Lemma 5.14, also the opened Morisugi--Mukai 2000 introductory
notation and Strickland's table).  The suspended version of the formula
therefore suffices to give `H(nu_4 sigma')=sigma'` exactly.  The other
Hopf values used in Proposition 13 are `H(E epsilon')=0` and
`H((E nu') sigma')=0`.

For completeness, if
`x=(E nu') sigma'=a eta_4 mu_5+b E epsilon'+c nu_4 sigma'`,
suspension gives `a=0` and `2(b+c)=4 mod 8`.  The Hopf invariant then
gives `c=0 mod 8`, so `b=2 mod 4`.  Hence the desired relation is
independent of the harmless sign conventions, since `2 E epsilon'`
has order two.

## An actual bottom-map consequence used by the team

Let `u_4:S^4 -> Y=Sigma^2 K(F_2,2)` be the bottom map and
`alpha=u_4 nu_4`, whose exact order four was proved in D.2.18.
Since `2u_4=0`, the Hilton addition formula gives

`0=(2u_4)nu_4=2alpha+[u_4,u_4]`.

Using `omega_4=[iota_4,iota_4]=2nu_4-E nu'`, with the compatible
standard sign choice, gives

`u_4 E nu'=2alpha-[u_4,u_4]=4alpha=0`.

The same conclusion holds under the usual opposite sign conventions.
This is an actual unstable null composite.  It neither evaluates
`u_4 nu_4 sigma'` nor shows that an arbitrary element in the image of
`pi_14(S^4) -> pi_14(Y)` is zero.
