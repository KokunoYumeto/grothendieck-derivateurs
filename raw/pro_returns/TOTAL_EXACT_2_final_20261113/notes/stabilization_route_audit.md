# Stabilization route: precise formulation, literature scope, and one-pair positivity

Status: proved reformulations and obstructions to particular arguments. No proof
of totality implying exactness, or even joint positive approximate equalizers,
is claimed. This is a separate working note; it does not alter an included
section of the checkpointed paper.

## 1. The unstable statement is a preservation statement about discrete objects

Let A be a small category, put X = Fun(A, Spaces), and let

    Pi : X -> Spaces

be the homotopy-colimit functor. It is left adjoint to the constant-diagram
functor Delta. The latter preserves all limits, so it is the inverse-image
part of an essential geometric morphism. Its usual right adjoint is

    Gamma = lim_A.

These two adjoints of Delta have different roles below.

For a covariant set-valued diagram H, the category-of-elements model gives

    Pi(H) = B El_A(H),
    pi_0 Pi(H) = colim_Set H.

Consequently totality, with the componentwise convention, is exactly:

    Pi carries every 0-truncated object of X to a 0-truncated space.

This statement does not say that Pi preserves products of discrete objects.
For example, the already established exact/total category Delta_inj has a
set-colimit functor which does not preserve all finite products.

There is an equivalent strict simplicial-set formulation. For every
X : A -> sSet, the canonical comparison

    hocolim_A X -> colim_A X

is a weak equivalence if A is total. Indeed, apply totality in each
simplicial degree: hocolim_A X_n is weakly equivalent to the discrete set
colim_A X_n. The diagonal lemma for bisimplicial sets, or geometric
realization of this levelwise equivalence, proves the comparison. Hence
ordinary simplicial-set colimit preserves objectwise weak equivalences.

Conversely, if ordinary simplicial-set colimit preserves all objectwise
weak equivalences, apply it to a projective simplicial replacement of a
set-valued H. The replacement is objectwise weakly equivalent to H and its
colimit computes hocolim_A H. Thus B El_A H is discrete up to weak
equivalence. This proves the converse without assuming siftedness.

## 2. The stabilized statement is exactly the unresolved additive condition

Stabilization gives Sp(X) = Fun(A, Sp), and the stabilized left adjoint is

    Pi_st = hocolim_A : Fun(A, Sp) -> Sp.

For an abelian diagram M, let HM be the objectwise Eilenberg--Mac Lane
spectrum. The standard skeletal filtration of the simplicial replacement
has spectral sequence

    E^2_(p,q) = L_p colim_A (pi_q HM)
              => pi_(p+q) Pi_st(HM).

Only the row q=0 is nonzero. The filtration is connective, so convergence
is not an issue here, and it gives canonical isomorphisms

    pi_i Pi_st(HM) = L_i colim_A M,   i >= 0,
    pi_i Pi_st(HM) = 0,              i < 0.

It follows that the following are equivalent:

1. colim_A on abelian diagrams is exact;
2. Pi_st carries every object of the pointwise heart Ab^A to the heart Ab;
3. Pi_st is t-exact for the pointwise standard t-structures.

Here is the detail for (2) => (3), which avoids a tacit boundedness
assumption. Pi_st always preserves connective spectra, because connective
spectra are closed under colimits. It is an exact functor of stable
categories. If it preserves the heart, it preserves every finite Postnikov
extension of shifted heart objects. A coconnective diagram E is the filtered
colimit, pointwise and therefore in Fun(A, Sp), of its finite-amplitude
connective covers tau_(>=-n) E. Each such cover is a finite Postnikov
extension. Pi_st preserves this filtered colimit, and coconnective spectra
are closed under filtered colimits. Therefore Pi_st preserves coconnective
objects as well. The other implications follow from the displayed
calculation and the usual degree-one criterion for exactness of a
right-exact additive functor.

Thus the proposed general theorem would need to say that, for this
essential geometric morphism, preservation of 0-truncated objects by Pi
forces its stabilized left adjoint to preserve the heart. None of the
statements above supplies that theorem. In particular:

- Pi is not known to preserve the products needed to carry a group object
  or an iterated group object to another such object.
- Stabilization of a left adjoint is not obtained by simply applying it
  levelwise to an Omega-spectrum and declaring the result to remain an
  Omega-spectrum; the necessary limit comparisons are precisely absent.
- Connectivity preservation gives the lower half of t-exactness for free.
  The missing condition excludes new positive homotopy groups in Pi_st(HM).

The symmetric-cocycle calculation in constant_extension_cocycle.md locates
the first possible obstruction: totality kills the category direction in
the relevant double complex, while a character on T_1(M) can remain in the
bar direction. This note therefore refines that obstruction rather than
removing it.

## 3. Why standard infinity-topos dimension results do not give the theorem

The official IAS copy of Lurie's Higher Topos Theory was opened directly.
The relevant numbered statements are:

- Definition 7.2.1.1: homotopy dimension is defined by existence of global
  sections of sufficiently connective objects.
- Definition 7.2.1.6 and Lemma 7.2.1.7: the relative condition tests the
  right adjoint f_* on connective morphisms.
- Example 7.2.1.3: P(C) has homotopy dimension at most zero when C has a
  terminal object.
- Example 7.2.1.9: every presheaf infinity-topos is locally of homotopy
  dimension at most zero.
- Corollary 7.2.2.30 relates that homotopy dimension to cohomological
  dimension. It concerns derived global sections, not the extra left
  adjoint Pi at issue here.

Accordingly, those dimension theorems cannot be substituted for the desired
left-adjoint assertion. There is a small explicit warning example.

Let A have objects 0,1,2, nonidentity arrows

    u:0->1,  v:0->2,  f,g:1->2,

and compositions fu=gu=v. There are no other nonidentity arrows. The
object 0 is initial, so A^op has a terminal object. Hence
Fun(A,Spaces)=P(A^op) has global homotopy dimension at most zero by the
cited example. Nevertheless define

    Q = coker(P_2 -> P_1),     1_2 |-> g-f.

The displayed map is objectwise injective: it is zero-to-zero at 0,
zero-to-Z at 1, and Z -> Z^2 with image generated by g-f at 2.
It is therefore a projective resolution of Q of length one. On colimits
the map is Z -> Z, identically zero, and consequently

    L_1 colim_A Q = Z.

This A is not total: H=A(1,-)/(f~g) has an element category consisting of
two objects joined by two parallel arrows, with classifying space S^1.
The example is not a counterexample to the main conjecture. It shows
concretely that the standard infinity-topos dimension hypothesis has the
wrong adjoint for this problem.

Reference: Lurie, J. (2009). Higher topos theory. Princeton University Press.
Official author-hosted text: https://www.math.ias.edu/~lurie/papers/HTT.pdf
(printed pp. 717--720, 735--736; the numbered statements above are the
unambiguous locators).

## 4. A proved sharper fact about the positive approximation route

Condition I alone gives positive approximate equalizers for one ordinary
parallel pair. Here condition I means every span p->x, p->y can be
completed to a commuting square.

Fix a,b:p->q and n>=1. There are an object r, arrows g_1,...,g_n:q->r,
and vertices u_0,...,u_n:p->r such that

    g_i a = u_(i-1),    g_i b = u_i.

Proof by induction. For n=1 take r=q and g_1=id_q. Given the path at r,
apply condition I to u_n:p->r and a:p->q. Choose h:r->r' and
g:q->r' with h u_n = g a. Postcompose the old path by h and append g.
Repetitions or loops cause no problem; this is a list of edges, not an
assertion that all edges or vertices are distinct.

The finitely supported probability distribution

    t = (1/n) sum_(i=1)^n [g_i]

therefore satisfies

    t b - t a = ([u_n]-[u_0])/n,
    ||t b-t a||_1 <= 2/n.

Equivalently, condition I rules out a family of uniformly bounded vertex
potentials which increases by one fixed positive amount along every
postcomposition of this single pair. Evaluation on the length-n path
would give a total increase n times that amount.

This does not prove the joint Reiter condition in
main_total_specific_attempts.md. For two or more pairs, path gluing in one
coordinate can disturb the other marginal differences. The AKR expansion
counterexample therefore starts at joint control of two pairs, as its two
potential coordinates suggest. No use of totality is hidden in this lemma.

## 5. Audit of the separate fixed-path attachment result

The new file sections/akr_attachment_fixed_paths.tex was independently
read in full, together with its cycle-space criterion and the repaired
path interval formulas. No substantive mathematical error was found.

In particular, the circular cell-fibre equations give
d_(2k+j)=d_(2k-j), hence d_(4k)=d_0 and g d_0=f d_0. The remaining
cancellations make all d_i equal. Thus the kernel of the cell-incidence
map is exactly the diagonal C_*(Fix). In the subsequent two long exact
sequences, the diagonal lift of a fixed-endpoint path sigma maps to the
fixed-component difference [w]-[v]. Summing its components gives
(g-f)sigma with coefficient 2k-(2k-1)=1. This verifies the exact kernel
formula and its sign.

Its remaining limitation is the one stated in that file: component
injectivity of the fixed subgraph has not been proved at every stage,
and a disconnected fixed subgraph does not alone establish that its
corresponding class is nonzero in the old colimit.
