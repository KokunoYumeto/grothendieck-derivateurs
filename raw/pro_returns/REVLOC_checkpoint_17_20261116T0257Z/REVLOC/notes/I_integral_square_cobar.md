# The doubled loop commutator forces the nonzero integral square

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026, 00:50 UTC. Complete proof is in
`sections/D2_integral_square_nonzero.tex`, claim D.2.50.

## Exact conclusion

For L=Y<7>, the specified integral class b8=beta4(a7) satisfies
0 != b8^2 in H16(L;Z), of exact order two. There is an integral
fifteen-cycle w with

    <a7 cup red4 b8,w mod4> = 2,
    <theta,w mod2> = 1.

Its homology class is torsion of order at least four. The proof
does not make it stable-spherical. Thus this decides the total
integral square, while the stable-spherical diagonal test and
the actual homotopy class h_M l4 remain open.

## Why the canonical model removes the previous gap

The preceding caution that the nullchain for 2z might carry
an unevaluated degree-sixteen extension was too weak. Its
word-length-one part is itself an integral fifteen-cycle,
and the canonical cobar differential reads its mixed cup
coefficient directly. This does not assume a minimal integral
Adams--Hilton model or replace integral chains by mod-two data.

Use a six-reduced simplicial model K of L and normalized integral
chains C with Alexander--Whitney coproduct. Every positive chain
degree is at least seven. The canonical cobar model is

    Omega C=T(s^-1 Cbar),
    d1=-s^-1 d_C s,
    d2=(s^-1 tensor s^-1) Delta_bar s.

It is a multiplicative integral model of the actual loop space.
Pick integral cochains dA7=4B8, A mod4=a7, [B]=b8. Pick a bottom
generator cycle x7 and y8 with d_C y=4x. Then A(x) is odd and
B(y)=A(x). Both chains have zero reduced coproduct by degree.
Set u=s^-1x, v=-s^-1y, so dv=4u. D49 and the independence of
the doubled commutator give dW14=2(uv-vu).

Only lengths one and two are possible in W. Write W=s^-1w+W2.
The length-one equation says d_Cw=0. On length two of cobar
degree thirteen use lambda=A tensor B, in unshifted bidegree
(7,8), zero otherwise. Then

    lambda(2(uv-vu))=-2 A(x)^2=2 modulo4.

The possible unshifted pairs in W2 are (7,9),(8,8),(9,7).
Their d1 contributions to lambda are respectively zero by dB=0,
divisible by4 by dA=4B, and zero by degree. The Koszul sign of
the first factor of degree seven gives

    lambda(d2(s^-1w))=-<A cup B,w>.

The exact AW cup coefficient is therefore two modulo four.
D45 identifies this with twice the theta evaluation. Its integral
Bockstein is b8^2. If that Bockstein were zero, theta would have
an integral lift, necessarily torsion by finite type and rational
acyclicity of L; such a lift evaluates zero on integral cycles.
This contradicts the displayed evaluation. The Bockstein has
order two, proving the exact square order.

The existing theta4 lift forces theta to annihilate H15(L;Z)[2],
so the detected integral class has order at least four. No stable
Hurewicz surjectivity is used or inferred.

## Primary source audit

1. Anel--Biedermann--Finster--Joyal, *Left-exact localizations of
   infinity-topoi I: Higher sheaves*, author version at
   https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/ABFJ.pdf.
   Opened and read the proof of Lemma5.4.2, printed p43 (PDF page43): every
   n-connected space has an n-reduced simplicial model. Publication
   metadata verified at the publisher: Advances in Mathematics400
   (2022), article108268, DOI10.1016/j.aim.2022.108268. The opened
   author-version locator is stated explicitly in the manuscript.

2. Hess--Parent--Scott--Tonks, *A canonical enriched Adams--Hilton
   model for simplicial sets*, arXiv:math/0408216v2,7 September2005,
   https://arxiv.org/pdf/math/0408216. Opened and read printed p3,
   giving the natural integral chain-algebra quasi-isomorphism
   Omega C(K)->C(GK), and printed p5, giving the exact cobar
   differential and normalized-chain definitions. These are the
   canonical-chain interfaces used above. Existing bibliography
   key FGHHessParentScottTonks2005 is reused.

Root, fibrations, axioms, and this agent independently checked all
degree pairs, the coefficient-four divisibility and the actual cup
identification. The full final TeX is undergoing the usual assembly audit.
