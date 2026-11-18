# Independent audit of the once-suspended eleven-cell reduction

15 November 2026, 19:55 UTC. Axioms-agent audit of
`I_k1_eleven_source.md`. The complete reduction passes. It is not a
nonextension theorem; the common D.2.22 bit is retained.

**Update, 20:06 UTC.** The historical qualification in the preceding
paragraph is superseded by the independently checked D.2.31: the
common bit is zero and the actual target group is elementary abelian.
The complete seven-cycle argument in Section 6 of the source note also
passes the independent audit below. Consequently the precisely fixed
coordinated nine-stage map has no extension through dimension eleven.
Maps with different lower-skeleton data are not covered.

## Source components and the reference filling

After collapsing K6, the source is six-connected. Cross Whitehead
terms first occur in dimension thirteen and cannot add an unmeasured
component to the degree-nine attaching map. The Chang block C4^9 has
pi9 = Z_(2){gamma} direct-sum Z/2{delta}. Integral top degree detects
gamma; Sq2 from the Moore top detects delta. The integral cycle K10
has zero degree boundary and Sq2 equal to P+B0^2, exactly the Moore
top after the prescribed slide. Thus its Chang projection is delta.
Its P-Moore projection is zero. All other factors have been assigned
the zero map. This is a complete component check for this coordinated
choice, not for every map realizing epsilon=1.

The exact integral chain identities dD=4C, dE=-4C, dX=2(D+E),
dB=2A give K=AX+BD+BE and d(BX)=2K. Both mod-two coordinates are
nonzero, so the corresponding primitive cycle and relation can be
retained by parity-preserving two-local basis changes.

The chosen nine-stage map lands in Sigma L8: the J block uses the
D0 Moore extension and the target c-cell, and the P block uses the
R-Moore factor. Therefore the homotopy identifying K's image with
2n introduces no target top-ten homology. Filling by two copies of
N' gives integral obstruction 4N' on BX. Its inverse image in the
actual target group is p or p+s, since the exact integral Hurewicz
kernel is Z/2{s}. Changing this filling changes the obstruction by
2*pi10(W), and this ambiguity must not be discarded.

## Moore coextension calculation

For f:M2,6 -> M4,6 with bottom degree two and top degree one,
mu f and -alpha bar_eta agree on the bottom. Their difference
factors through the top seven-sphere and is a combination of b,c.
Precomposing tilde_eta2 changes the value only by b eta,c eta.
The exact Toda set <eta,2,eta>={2nu,6nu} has identical image 2n
because n has order four. The alternative choice of tilde_eta4
adds bottom eta^2; its image is rho eta^2=c eta. Both indeterminacies
die in L8. Thus mu tilde_eta4=2n there, with no omitted coefficient.

## The remaining s coefficient is zero for this coordinated map

The suspended relation is Psi=Sq4 theta7+Sq2 lambda9=0 on W.
The cone detector of p is zero by its prescribed normalization;
the detector of s=rho nu is one (Sq4 top=r=e+f, Sq2 top=0).
The source identities give

    Sq4_*(BX)=AB,
    Sq2_*(BX)=AD+AE+BC.

For the coordinated lower map, theta7 evaluates one on AB,
and lambda9=J1* evaluates respectively 1,0,0 on AD,AE,BC.
The last three values follow directly from the target c-cell and
R-Moore choices: AD maps to J1+(L+M), AE to zero, and BC to
J3+(L+M). Consequently Psi evaluates 1+1=0 on this actual
source cone. The reference obstruction is therefore p, not p+s.
Equivalently the pulled-back classes are alpha3 beta4 and
alpha3 delta6, and their displayed Steenrod relation holds in
H*(A); the cone comparison uses their actual restrictions.

The final obstruction is the precise coset [p] in
pi10(W)/2*pi10(W). If the common bit a=b is zero, this coset
is nonzero. If the bit is one, p is twice x (and twice y), so
the coset vanishes. Neither value of that bit is selected by
this audit. The other lower-map branches and all full-source
extension questions remain outside this conclusion.

## Complete cycle lattice and every eleven-cell coupling

The full degree-ten and degree-eleven mod-two source bases have
dimensions 13 and 17. Their first Bockstein ranks are 5 and 7. The
seven independent latter images are the Ki listed in Section 6 of
the source note. Cartan and Nishida give all the displayed entries;
in particular AG and BF share their image, so there are eight
nonzero input columns, not nine. The established H8(A;Z)=(Z/2)^3
and UCT give six cyclic summands in H9 and seven in H10. Rank seven
for beta from degree eleven proves H10(A;Z)=(Z/2)^7 exactly.

The kernel of the integral degree-ten differential is a saturated
free submodule of the degree-ten cellular chains. Its seven
independent reductions Ki therefore lift to a two-local lattice
basis. The exact chain K7=AX+BD+BE can be retained. The integral
eleven-boundary lattice is twice this cycle lattice, so BX may be
kept as the relation 2K7 while the other relations are normalized
to 2Ki or zero by parity-preserving cell operations.

The Sq2 table detects every torsion component on the two source
summands assigned nonzero maps. K5 has only the F-Moore-top
coordinate, whose whole factor is assigned zero. K7 alone has
the J-Moore-top coordinate. No Ki has a P-block coordinate.
All free ninth-cell degrees are zero because the Ki are integral
cycles. Thus K1,...,K6 have zero composite already in Sigma L8;
K7 has composite 2n there. Cross Whitehead components start in
dimension thirteen and cannot occur in this attaching group.

Reference fillings for the first six cycles remain inside Sigma L8,
which has no degree-ten homology. The K7 filling uses 2N'. The
reference eleven-obstruction therefore has integral Hurewicz zero
on every normalized coordinate except BX, where it is 4N'. The
same actual Psi cone calculation kills the sole possible s term on
every coordinate. Although the degree-seven class on the quotient
R may have a relative ambiguity from K6, H11(R11) -> H11(K11)
is an isomorphism. Hence the identity verified on the full source
still determines every top detector value in this quotient.

Changing a ten-cell filling by z changes an eleven-obstruction by
its integer cellular degree times z. This is the actual cell-coaction
law; a Whitehead term involving the new ten-sphere starts too high.
After the boundary normalization, only changing K7 can affect BX,
and its effect is 2z. Thus there is no missing coupling. D.2.31 now
gives 2*pi10(W)=0, so the nonzero reference p cannot be removed.

## Independent audit of the new order-two K5 sphere

The published Chen--Wu Proposition 2.1, printed pp.3249--3250,
was reopened directly at
https://msp.org/agt/2013/13-6/agt-v13-n6-p08-p.pdf . Its proof and
the left-nested computation on p.3251 were read. For M=M(Z/2,3),
the actual alpha:S7 -> M smash M has Hurewicz uv+vu. Compose
id smash alpha with the left-nested triple Samelson map into
Omega Sigma M and then Omega Y. The source M smash S7 is
M(Z/2,10), whose bottom S10 has exact order two. The image has
once-adjoint Hurewicz beta3(uuv+uvu)=uuv+vuu.

D.2.22's entire mod-two spherical image is span(K1,K5). Its
homology suspensions are the independent tensor words af+fa and
aab+baa. Hence the constructed actual sphere has Hurewicz K5,
not K5 plus an undetermined K1 component. Doubling an element
with that Hurewicz gives b*p, with p nonzero. Its order two forces
b=0; the previously proved a=b then gives both coefficients zero.
All dimensions, actual adjunctions, and the presentation's p,s/even
generator ambiguities have been checked. No Lie-telescope
factorization or assumed H-map property is used.
