# The source ten-cell correction: a conditional unit-quotient reduction

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15, 17:54 UTC.

Status: research in progress after the proved D.2.20 nine-skeleton map.
No ten-skeleton map, no extension of the canonical summand, and no
nullification-survival statement is asserted here. The parent is examining
the canonical summand separately. This note concerns only the correction.

## 1. A smaller source for a possible new correction

Keep B=K(F2,2), X=Sigma B, A=QX, and F the 3-connected double-loop
fiber used in D.2.18--D.2.20. Choose the bottom subcomplex
K4=Sigma B^(3)=M(Z/2,3) inside X, and put

    Z=X/K4=Sigma(B/B^(3)).

Thus Z is 4-connected and there is an actual map QX -> QZ induced
by the quotient. The stabilization

    Omega Sigma Z -> QZ

is 10-connected: Sigma Z is 5-connected, its stabilization is
11-connected, and one looping lowers the connectivity by one.
The same statement holds for Omega Sigma(Z^(10)) -> QZ, since
the omitted cells of Z have dimension at least eleven.

Consequently, given an actual based map h:Z^(10)->F, its James
extension to Omega Sigma(Z^(10)) can be pulled back along QX->QZ
over any finite source subcomplex of dimension at most ten.
The relevant homotopy pullback projects 10-connectedly to QX;
obstruction theory gives the lift through dimension ten. F is
a loop space, so the James extension is the standard adjoint
extension, not an assumption that h is an H-map.

This is a conditional reduction of a NEW correction construction.
It does not yet prove that such h exists with the required low
values. It also does not identify the resulting pullback map up
to homotopy with the already chosen G9 correction. Compatibility
through dimension nine requires a specified relative lift and
agreement of the lower maps, rather than mere agreement of their
mod-two homology coefficients. The possible freedom in the old
eight- and nine-cell nullhomotopies must be retained explicitly.

The unit-weight quotient has the same C,D,E lower classes used
by the existing correction. Its desired unit values are

    C -> xi a,
    D -> k=b^2+(b^2+k),
    E -> k+r=b^2+p3,

where r=b^2+k+p3 is the actual spherical class of D.2.17.
The other-weight zero choices of D.2.20 suggest compatibility,
but that suggestion has not been substituted for a relative
homotopy argument.

## 2. The four unit ten-classes and their primary operations

Write H*(B;F2)=F2[u2,v3,w5,t9,...], with

    v=Sq1 u, w=Sq2 v, t=Sq4 w.

The complete degree-nine cohomology basis of B is
u^3 v, u^2 w, v^3, t. Let M,N,O,T denote the suspended dual
classes in degree ten of Z. Retain G,H for the suspended duals
of u^2 v, u w, and I,J,L for the suspended duals of u^4,
u v^2, v w. Direct Cartan and Adem calculations give

    beta O=J+L;        beta M=beta N=beta T=0;
    Sq_*^2 N=G+H;     Sq_*^2 O=G+H;
    Sq_*^2 M=Sq_*^2 T=0;
    Sq_*^4 N=E;       Sq_*^4 O=E;
    Sq_*^4 T=D;       Sq_*^4 M=0.

For example Sq2(u^2v)=u^2w+v^3=Sq2(uw), and
Sq4(uv)=u^2w+v^3, whereas Sq4w=t. Also
Sq_*^3 O=F (F is dual to u^3), and all degree-five-square
coefficients into the bottom C vanish by instability on u^2.
This table does not give a complete attaching matrix in pi9(Z9).
In particular it does not determine secondary coefficients or
the possible first Whitehead-square component.

## 3. The new order-eight integral group

The next integral group is

    H8(B;Z)=Z/8 + Z/2,

so a degree-four boundary normalization would be incorrect here.
The fundamental u is transverse in the Bockstein spectral sequence:
its successive squares give orders 2,4,8. Thus the degree-eight
u^4 survives to a nonzero third Bockstein. In the homological
spectral sequence the corresponding degree-nine class is represented
by the dual to u^3v (equivalently u^2w after the earlier boundaries),
and its third Bockstein hits the dual to u^4.

Opened primary source: Alain Clement, *Integral Cohomology of
2-Local Hopf Spaces with at Most Two Non-Trivial Finite Homotopy
Groups*, Contemporary Mathematics (2005), Proposition 2.4 and the
table on p.5. The table is cohomological: H^9(B;Z)=Z/8+Z/2,
which gives the displayed homology group by integral UCT.

https://serval.unil.ch/resource/serval:BIB_3440F3674944.P001/REF.pdf

The primary paper was opened in full (web reference turn1158view0).
It points to the author's 2002 thesis, *Integral cohomology of finite
Postnikov towers*, for the transverse theorem's proof. The thesis
source is also maintained by its author at

https://github.com/aclemen1/integral-cohomology-of-finite-postnikov-towers

The exact integral ten-cell normalization and the compatibility
of the proposed new correction with the earlier chosen nine-map
remain to be checked. No source ten-cell has yet been declared
harmless solely from a stable target calculation.
