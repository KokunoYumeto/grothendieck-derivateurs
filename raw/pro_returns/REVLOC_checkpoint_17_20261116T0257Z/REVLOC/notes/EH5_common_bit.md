# The common extension bit in D.2.22

**Status, 15 November 2026, 20:02 UTC: the common bit is zero.**
Section 4 gives an actual order-two representative of K5, using the
opened Chen--Wu spherical commutator and a triple Samelson map.
Root and both other mathematical agents have independently passed
the full proof, including the final TeX. Sections 1--3 retain
the earlier reduction and the failed particular-coextension route,
so the distinction between that failure and the successful new
representative remains explicit.

## 1. Exact question and actual representative

Use the presentation of D.2.22,

    pi9T = <p,x,y,s | 2p=2s=0, 2x=a p, 2y=b p>,

with integral Hurewicz h(p)=4N, where N has order eight, and
h(s)=0. The mod-two Hurewicz values of x,y are K1,K5. The actual
bracket of the order-two bottom element a in pi2T with rho in
pi6T has order at most two and mod-two Hurewicz K1+K5. Hence a=b.

Let m:M(Z/2,2)->B->T be the bottom Moore map and let
alpha:S5->T be the order-four class with Hurewicz xi1(a). The
actual generalized Browder map

    lambda1(m,alpha): M(Z/2,8)->T

has null restriction to its bottom sphere: its Hurewicz is
{a,xi1(a)}=0, and D.2.20 gives injectivity of the actual mod-two
Hurewicz map in degree eight. Factoring through the top quotient
gives kappa:S9->T with mod-two Hurewicz K5. The desired bit is
exactly the value of 2kappa, either zero or p. Different choices
of this factor differ by 2pi9T; their doubles agree since
4pi9T=0. The existence of this Moore factorization alone does
not make kappa order two.

After double adjunction, the map is the generalized Whitehead
product

    [m_tilde:M(Z/2,4)->Y, u4 nu4:S7->Y]:M(Z/2,10)->Y.

Its bottom [u4,u4 nu4] is zero in Y. The question is the double
of its chosen sphere coextension S11->Y, with all changes of
bottom nullhomotopy retained.

## 2. Opened primary Moore calculation and its exact limitation

Juno Mukai, *Generators of some homotopy groups of the mod 2
Moore space of dimension 3 or 5*, Kyushu Journal of Mathematics
55 (2001), 63--73, primary publisher PDF:

https://www.jstage.jst.go.jp/article/kyushujm/55/1/55_1_63/_pdf

The full relevant pages were opened as images. Theorem 1,
printed p.63, makes pi11(P5(2)) an elementary two-group. It
would settle the desired double if the sphere coextension
could be chosen through P5(2). However equation (5.5), printed
p.71, gives

    [i5,i5 nu4] = i5 nu4 nu7 + a_tilde (tilde_nu4 nu7),
    a_tilde even.

The i5 nu4 nu7 component is nonzero, independently of the
even coefficient. Thus the required bottom Whitehead product
does not vanish in P5(2). Its vanishing in Y uses additional
cells, whose nullhomotopy may contribute precisely the
unknown secondary term. No order conclusion is imported
from Mukai's abstract group table.

## 3. Relation to the once-suspended source test

The separate source calculation in I_k1_eleven_source.md
identifies, for its coordinated lower map, an eleven-cell
obstruction with integral Hurewicz 4N. Before its independent
primary detector is applied it is p or p+s. Changes of the
relevant ten-cell filling change it by 2pi9T. Consequently
the p part can be removed by that variation exactly when
the common bit is one. This does not cover every lower map
or the branch nonzero on the six-skeleton.

Ordinary mod-four homology of the Moore--Whitehead map does
not decide the bit: the class 4N reduces to zero with those
coefficients. A secondary operation detecting the even-nu
attachment, or an actual controlled nullhomotopy in Y, is
still required by that particular approach. The following different
order-two representative settles the bit directly.

## 4. An actual order-two representative from a spherical commutator

Let M=M(Z/2,3)=P4(2), with mod-two classes u3,v4. The suspension
of the bottom Moore map M(Z/2,2)->B gives j:M->X=Sigma B,
with j_*(u)=sigma(a) and j_*(v)=sigma(b). We may work two-locally;
all target homotopy groups in the degrees used are two-primary.

Chen--Wu, Proposition 2.1, printed pp.3249--3250, supplies an
actual map

    alpha:S7 -> M smash M,    alpha_*(iota7)=uv+vu.

Let E_M:M->Omega Sigma M be the James unit and let

    S3=[[E_M,E_M],E_M]: M smash M smash M -> Omega Sigma M

be its actual triple Samelson product. Since M is a suspension,
its two homology generators are primitive. Therefore S3 acts
on the threefold tensor product by the iterated commutator
beta3(xyz)=[[x,y],z]. Consider the composite

    M smash S7 --id smash alpha--> M smash M smash M
      --S3--> Omega Sigma M --Omega Sigma j--> Omega Y.       (4)

The source is M(Z/2,10), whose bottom S10 represents the
order-two generator of pi10 by the ordinary Hurewicz theorem.
Restricting (4) to that sphere gives an actual order-at-most-two
class in pi10 Omega Y, equivalently a class gamma in pi9T.
Its Hurewicz class in Omega Y is exactly

    beta3(uuv+uvu)=uuv+vuu
      -> (sigma a)^2(sigma b)+(sigma b)(sigma a)^2.             (5)

The computation is over F2: beta3(uuv)=0 and
beta3(uvu)=uuv+vuu. In particular (5) is nonzero.

By D.2.22, for either values of its retained bits, the image
of the actual mod-two Hurewicz homomorphism pi9T->H9T is
contained in, and spans, <K1,K5>. This follows directly from
its complete presentation and integral Hurewicz lattice:
h(p)=4N reduces to zero, h(s)=0, while x,y reduce to K1,K5.
The ordinary homology suspension sigma:H9T->H10 Omega Y has

    sigma(K1)=(sigma a)(sigma f)+(sigma f)(sigma a),
    sigma(K5)=(sigma a)^2(sigma b)+(sigma b)(sigma a)^2.         (6)

Indeed homology suspension annihilates the product correction
in K1={a,f}+aR and takes an E2 Browder bracket to the E1
commutator. The two expressions in (6) are independent in
the tensor algebra H_*(Omega Sigma X;F2): they have distinct
word lengths and nonzero monomials. Naturality of Hurewicz
under adjunction and (5) therefore force

    h_F2(gamma)=K5,       2gamma=0.                            (7)

In the D.2.22 presentation, every element with mod-two
Hurewicz K5 is y plus a combination of p,s and even multiples
of x,y. Those additional terms have double zero, because
4pi9T=0. Thus 2gamma=bp. Since p is nonzero, (7) gives b=0.
The previously proved equality a=b gives a=0 as well. Hence

    pi9T = (Z/2)^4.                                         (8)

In particular 2pi9T=0. The integral Hurewicz kernel remains
the nonzero order-two class s=rho nu6; it is not suppressed
by this argument. The degree-eleven source obstruction with
integral Hurewicz 4N cannot be removed by changing a ten-cell
filling through doubling. Its complete nonextension scope
still depends on the independently audited source calculation.

This construction does not assert that the particular
Moore--Whitehead factorization of Section 1 already lifts
through P5(2). It supplies a different actual sphere with the
same mod-two Hurewicz image, which is enough to determine the
intrinsic bit by the complete target presentation.

### Primary source interface for Section 4

Chen, Weidong, and Jie Wu, *Decomposition of loop spaces and
periodic problem on pi_**, Algebraic & Geometric Topology 13
(2013), 3245--3260, DOI 10.2140/agt.2013.13.3245:

https://msp.org/agt/2013/13-6/agt-v13-n6-p08-p.pdf

Proposition 2.1 and its full proof, pp.3249--3250, were reopened
directly on 15 November 2026. The actual spherical map is also
used in D.1.8. The construction of the triple Samelson map is
the ordinary generalized Whitehead adjunction; Wu's *On
combinatorial calculations for the James--Hopf maps*, Section 1
and Section 4, explicitly writes S3 in this form:

https://arxiv.org/pdf/math/9510209

The argument needs no loop-space retraction, no unsuspended
Lie telescope identification, and no claim that an arbitrary
ordinary map preserves Dyer--Lashof operations.
