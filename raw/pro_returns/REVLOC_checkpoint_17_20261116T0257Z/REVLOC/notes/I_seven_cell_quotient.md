# The next exact extension problem after D.2.17

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15, after 17:00 UTC.

Status update, 17:14 UTC: the six-skeleton realization is proved in
D.2.17, and the source quotient calculation below has passed independent
root and axioms-agent review. The independently checked target-fiber
calculation in notes/FGH_D2_pi8_fiber.md and
notes/root_D2_fibre_low_homotopy.md now gives pi8(Y)=Z/4 and
2 betaHat=u4 nu4 eta7 for every representative with the required
Hurewicz image. Thus the displayed seven-cell obstruction vanishes.
The fibrations agent owns the combined D.2.18 statement and proof.
The unresolved boundary has moved to dimension eight and higher;
there is still no map on the full infinite loop source.

## 1. Notation and the finite model

As in D.2.17, B=K(F2,2), X=Sigma B, A=QX, Y=Sigma²B, and
T=Omega²Y. The map C2X -> A is seven-connected, so a relative CW
approximation adds cells only in dimensions at least eight. We may
therefore choose K=A^(7) from C2X. The canonical map g2=Omega²h0 is
defined on K. The correction of D.2.17 is zero on K4=M(Z2,3), and
its extension relative to K4 is a map from Q=K/K4 into T.

The six-skeleton of Q has one Moore factor M(Z4,5), with bottom
five-cell c and top six-cell d, and free six-spheres. On mod-two
homology we choose d=D and e=D+E, and z=A0². Thus E=d+e in these
coordinates. The integral differential has dd=4c and de=dz=0.
Extra cells are retained until their degree-matrix cancellation is
justified below.

## 2. Integral H6(A) and the required degree matrix

The Snaith stable splitting identifies H6(A;Z) with the direct sum
of the weight-one and weight-two terms. Weights at least three start
in degree nine. The first term is H5(B;Z)=Z/2. Here is a direct
exponent check, rather than an assumption of a homology table.

Serre gives dim H5(B;F2)=2 and dim H6(B;F2)=2, while H4(B;Z)=Z/4
by the opened Mahowald calculation. The integral homology of B in
positive degrees is finite two-primary. The universal coefficient
sequence therefore makes H5(B;Z) a cyclic two-group. Its exponent
is two because the first homology Bockstein is nonzero:

    beta(x)=d+e,

where x is dual to v² and d,e are dual to w,uv. This is dual to
Sq¹w=Sq¹(uv)=v². A cyclic summand Z/2^s contributes a nonzero first
Bockstein from its Tor class precisely when s=1. Hence H5(B;Z)=Z/2.

The bottom weight-two group is

    H6(D2X;Z)=H0(Sigma2; H3(X;Z) tensor H3(X;Z))=Z/2.

There is no lower homology term that could contribute another
total-degree-six group or differential in the homotopy-orbit
spectral sequence. The transposition sign on the two degree-three
labels acts trivially on Z/2. Consequently

    H6(A;Z) = Z/2 {e} + Z/2 {z}.

Collapsing K4 does not change H6, and later cells of dimension at
least eight do not change it. Thus the integral seven-cell degree
matrix, on the free six-cycles of Q6, has Smith form with two
entries 2 and all other nonzero entries units. Unit six/seven
pairs can be cancelled. After an integral change of basis we may
take the two essential boundary degrees to be 2e and 2z. Their
mod-two identifications are fixed by the Bockstein calculation in
the next section. Additional seven-cells with zero degree boundary
must still be checked for their eta components.

## 3. The eta components of every seven-cell

The ordinary, not merely primitive, degree-seven mod-two homology
of A has basis

    F=Sigma f, X7=Sigma x, R=Q^4 A0, A0 B0.

The last product must not be omitted. The Bockstein values are

    beta F=0, beta X7=D+E=e,
    beta R=A0²=z, beta(A0 B0)=A0²=z.

Thus we choose the seven-cells x,y corresponding to X7,R for
the two nonzero degree boundaries. The combination A0 B0+R,
and F, have zero degree boundary. Any additional seven-cell
classes killed by later cells also have to be included, but
the square calculation below makes their eta components zero.

The unique degree-five cohomology class of Q is the class C^vee
dual to the Moore bottom c. Stable suspension compatibility and
Cartan give

    Sq²(C^vee) = Sigma(Sq²u²) = Sigma(v²).

Its value is one on X7 and zero on F,R,A0B0. The latter two
vanish also directly: Sq_*²R=0 by the already audited Nishida
identity, and Sq_*²(A0B0)=0 by Cartan. Naturality shows that it
also vanishes on any extra seven-cell cycle mapping to zero in
H7(A;F2).

There are no unrecorded unstable attachment components here.
The space Q6 is four-connected, and

    pi6(Q6) = Z/2 {i eta5} + direct_sum_j Z {sphere_j},

where i:S5 -> M(Z4,5) is the bottom inclusion. The cofiber
sequence of the degree-four map gives pi6 M(Z4,5)=Z/2, generated
by i eta5, and all Whitehead products have dimension at least
nine. The eta component of a seven-cell is detected exactly by
Sq² on the bottom cohomology class of its cone. Therefore the
essential seven-cell attachments are

    x: i eta5 + 2e,
    y: 2z.

Every remaining zero-degree seven-cell has zero eta coefficient,
so it is a freely wedged seven-sphere. This gives the quotient
model

    Q ~ (M(Z4,5) vee S6_e vee S6_z)
          union_(i eta5 + 2e) e7_x union_(2z) e7_y
          vee (a wedge of S7).

The seven-spheres and any cancellable auxiliary pairs are not
being suppressed before their attachment components are checked.

## 4. The resulting concrete homotopy-group equation

Let alphaBar:S5 -> T be the double adjunct of u4 nu4, as in
D.2.17. Its order divides four and its Hurewicz image is xi a.
Choose a Moore extension mu:M(Z4,5)->T with top image k; the
actual spherical r in D.2.17 allows precisely this choice.
Let beta:S6_e -> T have Hurewicz image r, and send S6_z to zero.
In the d,e,z coordinates the correction has

    c -> xi a, d -> k, e -> r, z -> 0.

It therefore gives the required D.2.17 values when added to g2.
For this correction to extend over the displayed quotient Q,
the y and free-seven-sphere attachments impose no condition.
The x attachment imposes exactly

    alphaBar eta5 + 2 beta = 0 in pi6(T)=pi8(Y).

Equivalently, after two adjunctions,

    u4 nu4 eta7 + 2 betaHat = 0 in pi8(Sigma² B),

where betaHat has Hurewicz image Sigma²f. A representative of
r with order two would solve this equation only if the alpha-eta
term vanishes. The framed PT construction alone does not give
the order of betaHat. Conversely, mere two-divisibility of the
alpha-eta term is not sufficient without the required Hurewicz
value of its half. Both qualifications must be retained.

This is an extension criterion for the specified correction
relative to K4. It is not yet a classification of all maps on
the seven-skeleton or a proof that any full A-map exists.

## 5. Primary source interfaces already opened

* Serre1953, Section2 nos8--9, gives the polynomial generators
  u,v,w and the low mod-two dimensions used above.
* Mahowald1964, Section2.3 p1336 and the proof in Section6 p1340,
  gives the Pontryagin-square reduction and the integral Z/4.
* Snaith1974, Theorem1.1 and Section2, supplies the stable
  configuration-weight splitting.
* Cohen--Lada--May1976, ChapterIII Theorems1.2--1.4 and3.1--3.2,
  gives the free loop homology basis and the needed primary
  operations. The extra A0B0 is included before using a CW count.
* Oka1986, Section2 equations(2.1) and(2.2), p149, is an opened
  primary source for eta, eta² and the related Moore relations.
  Bibliography key I_Oka1986; the direct Chang-cofiber argument
  used in the target calculation needs only eta² nonzero.

The degree-matrix and pi6 calculation are elementary in this
connectivity range; their precise use, rather than an assumed
Moore--Chang decomposition of the full source, is given above.
