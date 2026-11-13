# Explicit obstruction for independent linear and cyclic orders

Status: this natural rigidification of the cyclic-embedding category is
not total and is not exact, even over the rationals. No assertion that it
is quasi-filtered is made. This disposes of the candidate before it can
be used as a separator for the main question.

## The category

Let C have as objects the nonempty finite sets with both a linear order
and a cyclic order, with no compatibility condition between the two.
Morphisms are injections preserving both structures. Take the small
skeleton whose underlying linearly ordered sets are {1,...,n}.

Every endomorphism is an identity, because it preserves a finite linear
order. This elementary rigidity is not sufficient for totality or
exactness, as the following computations show.

## A four-arrow integral obstruction

Let p be the two-point object and let q have linear order

    1 < 2 < 3 < 4

and cyclic order (1,3,2,4). Write ij:p->q for the increasing injection
with image {i,j}. The cyclic structure on a two-point set is unique, so
these are all morphisms of C.

For any target r, choose a cut of its cyclic order, thereby obtaining a
temporary linear order around the circle. Define chi:C(p,r)->{0,1} by
chi(h)=1 exactly when the first point of the increasing pair h occurs
after its second point in this temporary order. For every g:q->r,

    chi(g12)+chi(g23)+chi(g34)-chi(g14)=1.             (1)

The induced cut on g(q) is one of the four rotations of (1,3,2,4).
Direct evaluation in these four cases proves (1); the complete table
is printed by the accompanying program.

Suppose t=sum_g n_g[g] has integral coefficients, augmentation one, and

    t12=t23=t34=t14.

Applying the integral linear extension of chi to these equal measures
gives the same integer c in each case. Summing (1) with coefficients
n_g then gives

    2c=1,

a contradiction. Thus these four ordinary parallel arrows have no
integral affine post-equalizer, in any target.

## Five arrows rule out exactness over every nonzero coefficient ring

Use instead the five arrows

    12, 23, 13, 24, 14 : p -> q.

The induced cyclic order on {1,2,3} is negative relative to the linear
order, whereas its induced cyclic order on {1,2,4} is positive. Hence
for every g:q->r, with the same cut function as above,

    chi(g12)+chi(g23)-chi(g13)=1,                    (2)
    chi(g12)+chi(g24)-chi(g14)=0.                    (3)

If a coefficient-R affine combination t simultaneously equalizes the
five arrows, all five chi-values of the resulting marginals are some
c in R. Equations (2) and (3), weighted by t, respectively give c=1_R
and c=0_R. This is impossible for any nonzero unital ring R.

The categorical conclusion does not require importing a characterization
of exactness. For this family let

    D:P_q -> P_p^4

be the column of differences from one chosen member, and L=ker D.
The same calculation for an arbitrary t in L gives aug(t)=0_R.
The two short exact sequences through im D therefore identify

    L_1 colim_C(coker D) = R / aug(colim_C L) = R.

In particular integral and rational exactness both fail. All coefficients
0 and 1 in chi are interpreted as central scalars when R is noncommutative;
the calculation itself only uses the underlying additive groups and is
equally valid for left R-module diagrams.

## Totality already fails for the constant one-point diagram

There is also a direct, low-dimensional topological obstruction.

Let X be the semisimplicial set whose n-simplices are cyclic orders on
the linearly ordered set {0,...,n}. A face deletes its indicated point
and relabels in increasing order. The category of simplices of X is
exactly C: its morphisms are increasing injections which pull the
target cyclic order back to the source cyclic order.

The classifying space of a semisimplicial set's category of simplices is
weakly equivalent to its realization. One way to see this is to replace
each simplex by its standard contractible geometric simplex and use
the usual homotopy-colimit model for realization; equivalently it is
the standard subdivision comparison. Thus it suffices to compute
cellular homology of |X|.

There is one 0-simplex, one 1-simplex, and two 2-simplices, corresponding
to the cyclic orders (0,1,2) and (0,2,1). Consequently

    d_1=0,      d_2=(1,1): Z^2 -> Z.

There are six 3-simplices. For each cyclic order on four points, the
alternating sum of its four induced three-point cyclic orders is zero.
This gives the identically zero matrix

    d_3: Z^6 -> Z^2.

All six cases are included in the exact program. Alternatively this is
the familiar alternating cocycle identity for circular orientation.
It follows integrally that

    H_2(BC;Z) = ker(d_2)/im(d_3)
              = Z[(0,1,2)-(0,2,1)].

The unique 1-cell is killed by the degree-one attaching map of either
2-cell, so BC is simply connected. Higher cells cannot change this
fundamental-group calculation, and cells of degree at least four do
not affect the displayed second homology. In particular, BC itself
is not contractible; no nonconstant C-set is needed to refute totality.

This argument does not identify the full homotopy type with CP^infinity,
and it does not identify this rigid category with the ordinary cyclic
category. Neither identification is needed for the proved obstruction.

## Reproducible finite checks

Program: ../code/cyclic_linear_cuts.py

Recorded output: ../code/cyclic_linear_cuts.out

The program uses only standard-library exact integer arithmetic. It
enumerates all four cut positions, all six degree-three cyclic orders,
and checks d^2=0 through degree four. These finite checks verify every
case used by the proofs, rather than extrapolating a finite search to
the infinite category.
