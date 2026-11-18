**Historical status update, 20:08 UTC:** the conditional relative calculation below was proved in D.2.21, the target bound/kernel in D.2.22, and the canonical square was proved zero in D.2.23. D.2.31 later refines the target group to an elementary abelian two-group. The earlier tentative claims are retained as the research record, with their corrections below.

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

## Refined finite proposition under audit, 18:04 UTC

The coefficient-four calculation can now be made exact. This section
replaces the earlier tentative signs. Its finite integral algebra is
proved below and machine-checked in D2_canonical_relative_chain.py;
the relative-CW comparison and Whitehead normalization have been sent
to the source and target reviewers respectively.

Use the relative binary configuration complex for C2X -> QX, with
the circle cells e0,e1 removed. Through dimension10 its bases are

    degree8: q=e2aa;
    degree9: r=e3aa, t=e2ab, t'=e2ba;
    degree10: e4aa, s=e3ab, s'=e3ba, v=e2bb, e2ac, e2ca.

Here |a|=3, |b|=4, |c|=5, db=2a and dc=0. Configuration
boundaries alternate tau-1 and1+tau, with the Koszul permutation
action; the total tensor differential gives

    d9(r)=-2q, d9(t)=-2q, d9(t')=2q;
    d10(s)=2r-t+t', d10(s')=-2r+t-t', d10(v)=2t+2t';
    d10(e4aa)=d10(e2ac)=d10(e2ca)=0.

The integral kernel of d9 has saturated basis w=t-r,w'=t'+r.
The nonzero boundary columns in that basis are (-1,1), (1,-1)
and(2,2). Their Smith form is diag(1,4), so the relative H9 of
this range is Z/4. This uses the entire degree10 boundary matrix,
not just a rational kernel or the e2bb column.

Let theta in an arbitrary abelian group M be the sole obstruction
coefficient on v; suppose the other degree10 cells initially have
zero obstruction. Changing the three nine-cell fillings by R,T,T'
changes the coefficients on s and v by

    ds=2R-T+T',       dv=2T+2T'.

The exact identity dv-2ds=4(T-R) proves that all coefficients can
be killed if and only if theta lies in4M. Conversely theta=4m is
realized by R=0,T=T'=m, with a sign change if needed to cancel
rather than reproduce the obstruction. The equation holds over
every abelian coefficient group, including groups with2-torsion.

For the intended topology, X'=X/S3 has bottom free generator b4.
The first relative cell for C2X' -> QX' is e2bb in dimension10,
with integral boundary2e1bb. Its homotopy boundary should be the
Browder self-bracket, equivalently the Whitehead square of the
bottom S6 after double adjunction. Under the specified canonical
map it becomes theta=lambda(chi,chi) in pi9T. Pullback to X kills
every displayed cell with an a-label, so gives precisely the
obstruction vector used above.

The range check to verify is that weights at least3 in the relative
free-configuration filtration have cells of dimension at least11:
three positive labels have minimum dimension9 and the relative
configuration cells begin in dimension2. The binary complex is
therefore the complete relative cell model through dimension10.
May's configuration construction and its label filtration provide
the proposed topological model; stable Snaith splitting alone would
not establish the ordinary attaching statement.

### Essential qualification on choices

This criterion fixes the canonical map on C2X and its selected
extension through the relative eight-cells. It varies the nine-cell
fillings. It is not yet a criterion allowing arbitrary changes on
the eight-cells: those changes can act through secondary attaching
components and must not be silently discarded. Nor is it a criterion
for the sum with the separate correction if that correction itself
has a nonzero tenth-stage obstruction. The target bracket and its
four-divisibility remain uncomputed.

### Correct target antecedent

The preliminary Moore-coextension route has been withdrawn. The
actual double adjunct of chi has integral Hurewicz image2c in the
order-four H6(Y) group. In the low Chang model it is the image of
the free lift gamma, whereas the Moore torsion coextension is killed
by the two seven-cell attachments. Thus the required square is the
image of[gamma,gamma]; the opened Morisugi--Mukai theorem about a
different Moore square cannot be applied to it. The independent
source and target checks of this correction are recorded in
EH5_next_browder_square.md.
