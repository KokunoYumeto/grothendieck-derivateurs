# Four times the actual high Browder map

15 November 2026. This is the exact map-level interface requested
for `root_half_product_source.md`; it supplies no chainwise
conclusion about its noncycle J.

Put M=M(Z/2,2), R=C2M, and let t:R→T=Omega²Y be the actual
free-double-loop extension of the bottom Moore map. Let
u:S5→T represent the class whose double adjunct alpha:S7→Y
has order four. The actual Browder map is

    f = lambda_1(u,t): Sigma(S5 smash R) = Sigma6 R → T.

Its twofold adjunct is the generalized Whitehead product

    F = [alpha,e]: Sigma(S6 smash Sigma R) = Sigma8 R → Y,

where e:Sigma²R→Y is the double-loop evaluation followed by
the original Moore map. The two desuspensions S6 and Sigma R
are themselves suspensions. Therefore the actual generalized
Whitehead product is biadditive on these mapping groups, and

    4F = [4alpha,e] = 0.

The adjunction is a group isomorphism, so 4f=0. No assumption
that an arbitrary ordinary map preserves Browder operations is
used: f is the specified actual Browder construction.

The source Sigma6R is seven-connected. Since E=T<5>→T is the
connected-cover map with a four-type base, Map(Sigma6R,E)→
Map(Sigma6R,T) is an equivalence of based mapping spaces.
Consequently the unique lift of f to E is also annihilated by
four as an actual homotopy class of maps.

Primary source: Arkowitz, *The generalized Whitehead product*,
Pacific J. Math.12(1962), Proposition3.4, printed p.14;
Proposition1.2, printed p.9, gives the group-isomorphism
adjunction. Both statements were reopened directly at
https://msp.org/pjm/1962/12-1/pjm-v12-n1-p02-p.pdf.
The source is already registered as EH5Arkowitz1962.

This result gives a nullhomotopy of the multiple of the entire
map. It does not specify its restriction to the attaching data
of the integral chain J. In particular, J is not a cycle, so
one must retain the nullhomotopy on dJ before converting this
map-level exponent statement into a bound on the residual
even chain correction.

There is a geometric way to choose such a nullhomotopy. Let
N=M(Z/4,5), and choose the actual Moore-four extension
mu:N→T of u used in D.2.17--D.2.18, whose mod-two top image
can be normalized to k. Naturality of the actual Browder
construction extends f to

    lambda_1(mu,t): Sigma(N smash R) → T.

Its source is again seven-connected, so it lifts uniquely to E.
This extension supplies a chosen nullhomotopy of four times f
on the bottom N-cell, coherently over the whole R factor. It
does not remove the remaining relative chain term: if the top
integral N-chain has boundary four times its bottom, the
boundary of top tensor J contains both four(bottom tensor J)
and top tensor dJ. The latter term must be evaluated under
this actual extension before any assertion about the even
correction follows.
