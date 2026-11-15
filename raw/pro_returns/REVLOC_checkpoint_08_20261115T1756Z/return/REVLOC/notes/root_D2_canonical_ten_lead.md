# Canonical tenth-stage extension: conditional lead

Root work record, 15 November 2026, 17:53 UTC. This is not a proved
manuscript statement. D.2.20 gives an actual map only through dimension
nine. The following is the next obstruction calculation to verify.

Put B=K(F2,2), X=Sigma B, Y=Sigma^2 B, T=Omega^2 Y, and
X'=X/S^3. The canonical double-loop summand factors through C2X'.
The space X' is 3-connected; its bottom integral homology in degree4
is free. The canonical map on that bottom class is chi in pi4T,
with mod-two Hurewicz image a^2. The comparison C2X' -> QX' is
9-connected, which supplies the already proved canonical extension
through source dimension9.

The expected first relative ten-cell for C2X' -> QX' is the binary
configuration cell on the bottom degree-four generator. Its attaching
map is the Browder self-bracket. Hence the obstruction to extending
this particular E2-map is expected to be lambda(chi,chi) in pi9T.
One way to verify the normalization is the universal bottom-sphere
case: the first James cell of S6 -> Omega S7 attaches by the Whitehead
square; double looping identifies the corresponding Browder bracket.
This comparison, including the relative filtration, still needs a
complete proof before use in the manuscript.

There is a potentially essential distinction after pulling back to X.
Its bottom Moore chain has a in degree3, b in degree4, db=2a. In the
relative arity-two chain complex, write configuration cells e_i,
i>=2. Up to dimension10 the relevant generators include e2aa,
e3aa, e2ab, e2ba, e3ab, e3ba and e2bb. With the usual Koszul signs,
the tentative differential calculation is

    d(e3aa)=-2e2aa,
    d(e2ab)=-2e2aa,
    d(e2ba)= 2e2aa.

For cycle representatives w=t-r and w'=t'+r in degree9, it gives

    d(e3ab)=w'-w,
    d(e2bb)=2(w+w').

Thus the relative H9 in this binary part is Z/4. Pullback of the
degree-ten bottom class from X' may therefore be the Ext generator,
whose obstruction coefficient is lambda(chi,chi) modulo 4*pi9T,
rather than the bracket itself. The relative integral H10 map to the
free bottom H10 for X' can be zero while this cohomology pullback is
nonzero. This is why homology alone cannot decide the extension.

The required remaining checks are: (1) the precise relative
configuration filtration and its orientation; (2) absence of other
weight contributions in this degree; (3) the obstruction coefficient
and its indeterminacy under the existing nine-stage choices; and
(4) the actual bracket and its divisibility by four. Arity-three
relative cells should first occur in degree11, but this is not yet
being used as a theorem.

The target reviewer identified an important invalid shortcut. The
unit F -> Omega^2 Sigma^2 F, for the 3-connected fibre F of T -> B,
is a split map of spaces but need not preserve the given E2-structure.
A Whitehead square in pi11(Sigma^2 F) maps under the loop-counit
retraction to the Browder bracket in pi9F; it need not lie in the
image of that unit. Consequently the Browder bracket cannot simply
be identified with the kernel of stabilization of F, and its stable
image must also be computed.

A separate source approach is being investigated by the source
reviewer: collapse the whole bottom Moore complex, use the
4-connected quotient Z=X/K4, and extend a map on Z by the James
construction. This may give better freedom of higher-weight choices.
Agreement with the already constructed map through dimension9 must
be checked; agreement only on low homology is insufficient.

An exact literature search for pi10(Sigma^2 K(F2,2)) did not locate a
usable primary table. Results about Sigma K(A,1) were not substituted
for the different space at issue. The target computation continues
directly from finite cofiber sequences and opened primary identities.
