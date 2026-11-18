# Independent audit of the eight-skeleton calculation

GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15 November 2026,
17:24 UTC. Status: mathematical target and source notes pass;
the combined manuscript wording is being assembled.

Update at17:29UTC: the complete combined TeX has passed root's
reading and is integrated as D.2.19. The source quotient's normal
form and free coefficients are explicitly two-local. The build has
157pages, zero overflows or citation/font errors, and its complete
new pages62--68 plus the final bibliography continuation were
rendered and visually checked.

## Exact target comparison

The three-connected fibre F is itself a double loop space. Write it
as Omega Z. The loop of the suspension counit is a retraction of
F -> Omega Sigma F by the adjunction triangle identity. Freudenthal
gives surjectivity on pi7, and the retraction supplies injectivity.
The next suspension is in the ordinary stable range. Therefore
pi7F equals its stable group. This argument does not extend the
stable comparison to pi8F; that is a new interface in the next stage.

Root opened the original James1955 scan, Theorem1.8 on printedp173,
which states the corresponding reduced-product retraction for an
h-space. The paper's proof can use the explicit adjunction identity,
so no unproved associative extension of an arbitrary H-space map is
being substituted here.

## Complete target homology and operations

Root independently enumerated all16 degree-eight monomials in the
free double-loop homology. They consist of three labels, eight
ordinary products, two products with the earlier operation/bracket
classes, and three new brackets. The apparent additional bracket
{a,xi a} is zero by the restricted-Lie identity. Subtraction of the
base and mixed product terms leaves exactly seven fibre classes.

For L=l+bd, the two reduced diagonals cancel. For
M=j+ax+be+ab², the diagonal of j contributes a tensor x and b
tensor e and their reversals; the other three terms cancel these
and the remaining ab tensor b and a tensor b² terms. The brackets
J2 and J3 acquire exactly the a tensor k correction cancelled by ak.
Only C=c² is nonprimitive, with reduced diagonal A tensor A.
Its base coaction is still trivial because q(A)=0. This verifies
membership in the actual fibre factor, including the nonprimitive
class, rather than just membership in the kernel of q on homology.

The cohomology identities beta(uw)=vw+uv² and
Sq2(u³)=u4+uv² give the two label Bocksteins and second squares.
Cartan then gives

    beta L=beta M=Q, beta J3=R,
    Sq2 L=d, Sq2 M=f, Sq2 J1=Sq2 J3=d+e.

All other displayed first and second operations vanish. The fourth
square is the cup-square detector of the degree-four class: it is
one exactly on C, from its reduced diagonal, and zero on the six
primitives. No operation component is left inferred from dimension
alone.

## Exact component groups

Root checked the independent Moore/Chang exact-sequence derivation.
For C, pi7 is Z2 on bottom nu plus Z2 on delta eta. The eta action
on the distinguished gamma is zero. One verification uses the
factorization of eta on the eta cofiber through its top quotient:
gamma has top degree2, and the bottom degree2 map is null in C.
The manuscript's equivalent cone-square verification is also valid:
the cone map from C(eta:S7->S6) preserves the new top class but
kills degree-four cohomology, forcing the nu detector to vanish.
This is compatible with the earlier fixed quotient image (0,2)
of gamma and does not silently replace gamma by gamma+delta.

For the mod-four Moore summand, the map from the mod-two Moore
spectrum with bottom degree2 and top degree1 gives a top-eta lift
of order2. Root reopened Oka1986, original publisher PDF, Section2
equations(2.1)--(2.2) on printedp149. The exact used formulas are
pi1S=Z2 eta, pi2S=Z2 eta², pi3S=Z24 nu, eta³=12nu,
p etaTilde=eta and2 etaTilde=i eta². Their two-local forms give
all the component groups and the specified order-two lift.

The eta images of the four seven-cell attachments kill precisely
the two components a and h. The degree-six kernel is free on2Q,R,
so pi7L7 is Z_(2)^2 plus Z2^3, with free lifts kappa,lambda and
torsion generators v,b,c. The only bottom-nu class v has order2.
Thus Sq4 measures its entire coefficient; no invisible even-nu
term remains.

The two other torsion square vectors are d+e and e+f. Adem forces
the square vector of kappa to have odd coordinate sum, so adding
b,c makes it d. Adding v then makes its fourth square zero.
The representative2lambda factors through a Moore cone on the
free R sphere and has zero second/fourth squares. Integral degrees
plus these three torsion detectors determine every eight-cell
attaching element. The first Bocksteins and universal coefficient
theorem give H7F=Z2^2; parity-preserving integral normalization
therefore gives the exact seven relations

    0, v, kappa, kappa+b+c, b, 0, 2lambda+b.

Their cokernel is Z2 lambda. In particular both rho eta and every
allowed Moore-top eta composite vanish. The generator has Hurewicz
image R. Higher cells cannot change pi7 of the stable spectrum.

## Actual source attachments and the canonical summand

Root independently checked pi7 of the source quotient. Collapsing
its bottom five-sphere kills the only possible eta² kernel and
identifies the two Chang-like components with the two eta classes
in the quotient. The other Moore summand contributes its bottom
eta. Together with the two free seven-spheres this gives exactly
Z² plus Z2³, completely measured by integral degrees and three
second-square coefficients. The source is four-connected, so this
is an actual unstable calculation in dimension7.

The odd-degree arity-two integral chain is correct: the transposition
on aa has sign minus, dr1=dt=-2x and dt'=2x, while
dh=w'-w and dq=2(w+w'). Thus H7 of this weight is Z4 and
d(q-2h)=4w. This proves beta2[B0²]=J, with the corrected
representative; it does not incorrectly divide dq by4. The other
two weight-two degree-eight basis classes have integral cycle
representatives. The weight-one beta gives the independent Z2
summand generated by F.

The integral normal form preserves all mod-two labels. A possible
4mJ term in dG8 is absorbed by F->F+2mJ. After that change, even
source combinations eliminate all unwanted F and J degrees in
the other columns. The exact first and second Bocksteins identify
which columns have degrees2 and4. The five attaching maps are

    2F+tau_d+tau_e, tau_d+tau_e,
    4J+tau_z, tau_z, tau_z.

The chosen correction is zero on the two free seven-spheres and
on z. Its only condition is mu zeta+rho eta=0, already proved on
the target side. The values of tau_d,tau_e are represented in the
old six-skeleton, so they do not depend on a seven-cell filling.

Finally, g2 initially lives on C2X. It must not be treated as a
map on all of QX. The quotient X'=X/S3 is three-connected;
pi5Y=0, already proved by Freudenthal in D.2.13, makes h0 vanish
on the collapsed bottom and supplies hbar:Sigma²X'->Y. The map
C2X'->QX' is nine-connected. Its homotopy pullback over QX
receives the specified C2X lift, and composition with Omega²hbar
recovers g2. Relative obstruction theory extends that lift through
dimension9. Adding this canonical extension to the quotient
correction therefore gives an actual map on the eight-skeleton.

No map on the full infinite source and no ordinary-nullification
value follows from this finite calculation. The next source stage
and the genuinely unstable pi8F interface remain to be studied.
