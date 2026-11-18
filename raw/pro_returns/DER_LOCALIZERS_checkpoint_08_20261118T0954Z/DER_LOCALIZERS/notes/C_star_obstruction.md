# A normalized pointwise example without a countable scalar form or a represented flat-interval approximation

18 November 2026. GPT-6 Astra, inherited effort, agent
`DER_LOCALIZERS/linear_case`.

**Scope.** This construction satisfies the full manuscript hypotheses and the
small-projective-generator hypotheses of the corollary. No flat object, in the
module-category sense, admits a monomorphism from the unit. In particular all
possible interval objects are non-flat, and the presentation-and-factorization
hypothesis of C.27 cannot be supplied for *any* interval in this category. The
underlying k-linear abelian category admits no form over a countable subring,
even after changing the small linear presentation. Thus C.21/C.22 cannot be made
automatic by changing generators.

This is **not a raw-adjoint counterexample**. Its interval is pointwise split,
and a resolving functor has finite evaluation components; C.7 and C.17 already
give the raw conclusion. The construction identifies limitations of two proof
routes. The coordinating agent independently re-proved the complete argument
and accepted it for integration as C.28. No novelty or exhaustive prior-art
claim is made. The main proof uses its shorter Tor2 argument below.

## 1. The scalar ring and the linear star

Let I be an uncountable set and let

\[
 k=\mathbb F_2[e_i\mid i\in I]/(e_i^2-e_i\mid i\in I)
\]

be the free Boolean ring on I. Every element is a polynomial in finitely many
generators. Every assignment of zeroes and ones to the generators determines a
character k -> F_2. We could choose I of cardinality aleph_omega, but the
argument below only requires uncountability.

For each i put

\[
 H_i=k\oplus k e_i x_i,\qquad x_i^2=0.
\]

Thus H_i is a k-algebra with unit 1, augmentation epsilon_i(1)=1,
epsilon_i(x_i)=0, and the additional scalar relation (1-e_i)x_i=0.
The underlying k-module is finitely generated projective. It is a
cocommutative k-bialgebra: 1 is grouplike and

\[
 \Delta(x_i)=x_i\otimes1+1\otimes x_i.
\]

The square-zero relation is preserved because the characteristic is two. The
support relation is preserved because (1-e_i) annihilates both terms after
moving scalar coefficients across the tensor product. The counit is epsilon_i.

Define a small k-linear category A with objects

\[
 u,\quad b_0,\quad b_1,\quad a_i\ (i\in I).
\]

The endomorphism algebras at u,b_0,b_1 are k, and End(a_i)=H_i. There is one
copy of k of morphisms u -> v for every branch v in {b_0,b_1,a_i}; all other
off-diagonal Hom modules are zero. Write g_v for its generator. Composition
with a branch endomorphism h is

\[
 h g_v=\epsilon_v(h)g_v,
\]

where epsilon_v is the identity for b_0,b_1. Scalar composition at u is the
usual one. All Hom modules of A are projective over k. We may pass to the
additive envelope when applying the manuscript's additive-generator
formulation. The original indexing category, not its additive envelope, is
used for pointwise formulas.

Give each k g_v its grouplike coalgebra structure, and each zero Hom module
the zero coalgebra structure. The identity maps and composition are coalgebra
maps: the only nontrivial check is composition with H_i, where the assertion
is the counit identity for epsilon_i. This makes pointwise tensor product on
k-linear presheaves well-defined.

For clarity, an object X of M_0=Fun_k(A^op,Mod k) consists of k-modules X_u,
X_{b_0},X_{b_1}, H_i-modules X_i, and maps

\[
 f_v:X_v\longrightarrow X_u,
 \qquad f_i x_i=0.
\]

The tensor is pointwise over k. At a_i, x_i acts on X_i tensor Y_i as
x_i tensor 1 + 1 tensor x_i. At the trivial branches and u it is the ordinary
tensor of k-modules, with the structure map f_v tensor f_v. The square-zero
and support relations, and f_i x_i=0, are preserved by these formulas. The
usual module associativity, symmetry, and unit isomorphisms are compatible
with all the actions. We obtain a cocontinuous symmetric k-bilinear tensor.

Its unit U has value k at every vertex, all branch maps the identity, and all
x_i acting by zero. Scalar copowers kappa_0(V)=U tensor_k V are constant
presheaves with value V. The object u is initial in the *linear, augmented*
sense A(u,a)=k with covariant reindexing by augmentation. Accordingly,

\[
 \operatorname{Hom}_{M_0}(X,\kappa_0 V)
 =\operatorname{Hom}_k(X_u,V).
\]

Indeed a map into kappa_0 V is determined by its component at u; at a branch
it must be its composite with f_v. This fixes the variance: we use
**contravariant presheaves** on the star. The corresponding constant covariant
functor is representable at u, whereas the unit presheaf need not be flat.

## 2. Add the simplicial direction and verify all manuscript hypotheses

Let M=sM_0, the category of simplicial objects in M_0. Equivalently it is the
category of k-linear presheaves on A tensor_k k[Delta]. It is an abelian module
category with all small limits and colimits, exact products, and a small set
of finitely presented projective representables. Its Hom modules between
these representables are projective over k: they are finite sums of the Hom
modules of A, since every Hom set in Delta is finite. Finite sums and retracts
give the additive generator category required in the corollary.

The tensor on M is pointwise in both indexing variables. The unit is the
constant simplicial object U. Its scalar copower kappa(V) is constant with
value V at every vertex and every simplicial degree. Thus kappa is exact and
preserves all limits. Its left adjoint is

\[
 \varphi(X)=H_0N(X_u),
\]

where N is normalized chains of a simplicial k-module. The adjunction follows
first from evaluation at u as above, then from maps of simplicial modules into
a constant module.

Take F(X)=N(X_u). This is exact and cocontinuous. Each F_n is a retract of the
single evaluation X -> X(u,[n]), by the natural normalized/degenerate
decomposition of simplicial modules. In particular its components are
projective cocontinuous functors. On the representable at (a,[m]), evaluation
at u is k[Delta[m]], since A(u,a)=k. Its normalized chain complex consists of
finite free k-modules, is acyclic in positive degrees, and has H_0=k. Thus F
takes projectives to projective objects of Ch_{>=0}(k), and is a resolving
functor as in C.6. The canonical augmentation on the unit is k[0] -> k[0],
so normalization (c) holds with its actual canonical map.

Let

\[
 L=k[\Delta^1]/k[\{0\}],\qquad J=U\otimes_k L,
\]

and let alpha:U -> J be induced by the vertex 1. In every simplicial degree,
L has a basis of the simplices of Delta^1 other than the constant-zero
simplex; the constant-one simplex is among them. Hence alpha is split as a
k-module inclusion at every vertex and degree. Pointwise tensoring preserves
those splittings, so alpha tensor X is monic for every X.

The pointed interval (Delta^1,0) is simplicially contracted to its basepoint
by the map min:Delta^1 times Delta^1 -> Delta^1. Linearizing and passing to
the quotient gives a simplicial homotopy from zero to the identity of L.
Tensor it with X_u; the parameter acts on the L factor. Normalized chains
send this homotopy to the usual prism chain homotopy. Consequently

\[
 F(J\otimes X)=N(L\otimes X_u)\simeq0
\]

for every X, including degree-zero homology. This verifies the full interval
hypothesis (d). Conditions (a), (b), (c), (d), exact products, and every
corollary smallness/projectivity condition have now been checked.

This example already satisfies the split-image alternative in C.7 for every
chosen projective resolving functor: its components are retracts of sums of
evaluations. It also has the finite evaluation resolving functor F just
displayed, so C.17 applies. All raw adjoints in the corollary therefore work.

## 3. The chosen interval is not flat

Let B be the full subcategory on u,b_0,b_1. A B-presheaf is a diagram
X_{b_0} -> X_u <- X_{b_1}. Write h_v=B(-,v). The constant presheaf U_B has
the projective resolution

\[
 0\longrightarrow h_u\xrightarrow{(1,-1)}h_{b_0}\oplus h_{b_1}
 \longrightarrow U_B\longrightarrow0.
\]

At each branch the last map is the identity; at u it is addition. Its kernel
is precisely the displayed copy of h_u. Let T be the covariant B-module
with T(u)=k and T(b_0)=T(b_1)=0. Applying T tensor_B - gives

\[
 \operatorname{Tor}^B_1(T,U_B)=k\ne0.
\]

Therefore U_B is not flat.

Restriction from A to B takes every representable to a projective: h_u,h_b0,
h_b1 restrict to themselves, and every h_ai restricts to h_u. It preserves
filtered colimits. Evaluation of a simplicial object in degree zero also
preserves filtered colimits and takes a representable at (a,[m]) to
h_a^{oplus(m+1)}. Thus both operations preserve objects presented as filtered
colimits of finitely generated projectives. If J were flat in M, its
degree-zero restriction to B would be flat. But that restriction is U_B,
because L_0=k. This contradicts the Tor calculation. Hence J is not flat.

## 4. No flat object contains the unit

We prove a stronger obstruction to the particular presentation condition in
C.27. Every map from U (the unit of M) to a projective object of M is zero
at (b_0,[n]) for every n. It therefore cannot be monic.

First consider a map into a representable R_(a,[m]). If a differs from b_0,
the target is zero at (b_0,[n]), because A(b_0,a)=0. If a=b_0, the target is
zero at (b_1,[n]). Naturality for u -> b_1 forces the component of the map at
(u,[n]) to be zero, since the source structure map is the identity. Naturality
for u -> b_0 then forces its component at (b_0,[n]) to be zero: the target
structure map from (b_0,[n]) to (u,[n]) is the identity on
k[Hom_Delta([n],[m])].

A map into an arbitrary sum of representables is still zero at this
coordinate, as all its coordinate maps are zero. Every projective is a
retract of such a sum, so the assertion follows for every projective.

If a monomorphism alpha':U -> J' factored through a projective P, the map
U -> P would itself be monic. This is impossible by the preceding paragraph.
Thus no universally monic interval map can be represented at a projective
stage of a filtered presentation.

We can strengthen this to exclude every flat interval, even when its unit map
is not initially known to be represented at a stage. Restrict from A times
Delta to B times Delta. This restriction preserves projectives and filtered
colimits, by the same representable calculation as in Section3. The restricted
unit U_(B times Delta) is finitely presented: the resolution of U_B above,
tensored externally with the representable k[Delta(-,[0])]=k, gives the finite
presentation

\[
 h_{(u,[0])}\longrightarrow
 h_{(b_0,[0])}\oplus h_{(b_1,[0])}
 \longrightarrow U_{B\times\Delta}\longrightarrow0.
\]

The no-projective-monomorphism argument applies just as well to this smaller
category. If U -> Y were monic with Y flat in M, restriction would give a
monomorphism from this finitely presented unit into a filtered colimit of
finitely generated projectives. The map would factor through one projective
stage, and that stage map would be monic because its composite is monic.
This contradicts the no-projective-monomorphism argument. Hence no flat
object of M contains the unit. Every possible interval object is non-flat.
This obstruction already occurs for the finite ordinary star B times Delta;
the Boolean branches are needed for the separate no-countable-form assertion.

## 5. No countable scalar form exists, even after changing presentations

Suppose, for a contradiction, that there were a countable unital subring
s subset k, a small s-linear category D_s, and a k-linear equivalence

\[
 M\simeq\operatorname{Fun}_k((k\otimes_sD_s)^{op},\operatorname{Mod}k).
\]

We do not assume that this equivalence preserves the displayed projective
generators. We do not need purity of s, projectivity of D_s's Hom modules,
or a monoidal scalar form: we will contradict even the abelian equivalence.

Every element of s involves finitely many Boolean generators. Since s is
countable, there is a countable subset I_s of I containing all of their
supports. Define characters chi_0,chi_1:k -> F_2 by

\[
 \chi_0(e_i)=0\quad\hbox{for every }i,\qquad
 \chi_1(e_i)=\begin{cases}0&i\in I_s,\\1&i\notin I_s.\end{cases}
\]

They agree on s. For a k-linear abelian category of modules, its full
subcategory on objects annihilated by ker(chi) is intrinsic: the condition
is that every scalar in the ideal act by zero on the identity of the object.
A k-linear equivalence restricts to an equivalence of these fiber
subcategories. On the proposed right-hand side the two fiber categories are
both modules over the same F_2-linear category F_2 tensor_s D_s, since the
characters agree on s. They would therefore be equivalent.

On the left, the fiber is the category of simplicial modules over A_chi,
obtained by applying chi to all Hom modules of A. At chi_0 every branch
endomorphism algebra is F_2. At chi_1 the branches indexed by I minus I_s
have endomorphism algebra F_2[x]/(x^2), while the other branches have F_2.

We distinguish the two abelian categories by the existence of a simple
object of infinite projective dimension. In Mod(A_chi^op), every simple is
supported at one vertex. If its u-component is nonzero, that component
itself gives a nonzero subobject supported at u, so simplicity forces this
case. Otherwise the structure maps are zero and any nonzero branch gives a
subobject supported at that branch. Each branch algebra has a unique simple
module, namely F_2. At chi_0 the simple at u is projective, and each branch
simple S_v has the projective resolution

\[
 0\longrightarrow h_u\longrightarrow h_v\longrightarrow S_v
 \longrightarrow0.
\]

Every base simple therefore has finite projective dimension.

At chi_1, choose an active branch a_i. Evaluation at that vertex is exact
and takes projectives to projective modules over H=F_2[x]/(x^2): the only
nonzero representable evaluation there is H itself. The simple at a_i
evaluates to F_2. This H-module has infinite projective dimension. Explicitly,
the infinite resolution with every projective term H and every differential
multiplication by x is exact, and applying Hom_H(-,F_2) gives zero
differentials and a nonzero Ext group in every degree. Thus the simple at
a_i already has infinite projective dimension in the base presheaf category.

Dold--Kan is an equivalence of abelian categories between simplicial objects
and nonnegative chain complexes in either base category. The simple objects
of the chain-complex category are precisely spheres S[n], with S a simple
base object. Exact evaluation in degree n takes projective complexes to
projective base objects; hence infinite projective dimension of S forces
infinite projective dimension of S[n]. Conversely if S has finite projective
dimension d, then S[0] and every disk D^n(S) have projective dimension at
most d. The exact sequence

\[
 0\longrightarrow S[n-1]\longrightarrow D^n(S)
 \longrightarrow S[n]\longrightarrow0
\]

inductively gives finite projective dimension, at most d+n, for S[n]. It
follows that the chi_0 fiber has no simple of infinite projective dimension,
whereas the chi_1 fiber has such simples (in fact uncountably many at degree
zero). An equivalence of abelian categories preserves simplicity,
projectivity, and projective dimension. The fibers cannot be equivalent,
contradicting the proposed countable form.

Therefore M has no countable scalar form even up to k-linear abelian
equivalence. In particular it is outside C.22's scalar-form class. A
k-linear ordinary-presheaf category has a form over F_2 obtained by
linearizing the ordinary indexing category over F_2; therefore M is not
equivalent to such a category either, and is outside C.21's ordinary class.
Again, its actual raw adjunctions are already covered by the split-interval
criterion, so this proves no negative assertion about C.raw_gate.

## Computational scope

The two finite algebraic steps admit small checks: the three-vertex star
resolution and the 2-by-2 matrix for multiplication by x in the dual-number
algebra. The infinite projective-dimension assertion uses the exact periodic
resolution and its Hom complex, not a finite numerical truncation. The
no-countable-form assertion uses arbitrary Boolean characters and an
abelian-equivalence invariant, not enumeration of finitely many fibers.

The saved code `code/C_star_obstruction.py` and its `.out` passed all displayed
finite checks. The output records exactness of the three-vertex star complex,
zero Hom spaces from the unit to the three representables, Tor1 dimension one,
and the dual-number differential's square, image/kernel and induced Hom map.

## Shorter intrinsic flat-object proof used in C.28

The coordinating agent supplied and independently checked the following
replacement for the finite-presentation factorization step. The covariant
B-module T has resolution 0 -> h^b0 plus h^b1 -> h^u -> T -> 0. Tensoring with
the unit gives the fold map k squared -> k, hence Tor1(T,U_B)=k and
Tor2(T,-)=0. If U_B embeds into a flat Q, its cokernel sequence injects that
nonzero Tor1 into Tor1(T,Q)=0, a contradiction. Degree-zero restriction from M
to B preserves projectives and filtered colimits, hence flat objects, so no
flat object of M contains the unit. The original finite-presentation proof
above remains a separate check of the same conclusion.

## Focused source search and reading limits, 18 November 2026

Queries used both search systems, with the stronger system verifying primary
coverage: `flat functors small additive category filtered colimits finitely
generated projective modules Crawley Boevey`; `Boolean ring scalar extension
module category simple infinite projective dimension dual numbers`; `constant
representation star quiver flat module embedding projective dimension`;
`William Crawley-Boevey Locally finitely presented additive categories 1994 pdf
1.3 flat`; and `Morphisms determined by objects and flat covers Krause 2015
2014 publication`.

Opened Henning Krause's author preprint, *Morphisms determined by objects and
flat covers*, dated 23 March 2014, at
https://www.math.uni-bielefeld.de/~hkrause/flatcover.pdf . Read the p.5 definition
of flat functors as filtered colimits of representables and Theorem 1.9's
explicit attribution to Crawley--Boevey Section 1.4. Also opened the author's
publication page, verifying Forum Mathematicum 28(3) (2016), 425--435,
DOI 10.1515/forum-2014-0115. This is the standard flat-functor background used
in C.28, not a source for the star calculation or Boolean-fiber argument.

Crawley--Boevey's original *Locally finitely presented additive categories*,
Communications in Algebra 22(5) (1994), 1641--1674, DOI
10.1080/00927879408824927, was identified through its author bibliography and
publisher search metadata. The publisher landing page returned HTTP403 and
the PDF endpoint was inaccessible; the original full text was not obtained
or read. Both source records, with these reading limits, are in
notes/C_references.bib. The focused search did not identify an identical
combined star/non-descent construction in the inspected results; that is not
a novelty assertion or a claim of exhaustive literature coverage.
