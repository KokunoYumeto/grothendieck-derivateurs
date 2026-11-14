# Independent attack on the remaining two-dimensional case

## Exact instance being investigated

The remaining fixed-target instance asks for a group `G` with a
two-dimensional classifying CW complex, `H_1(G;Z)=0`,
`H_2(G;Z)=Z`, and no nontrivial homomorphism to a countable group.
The following observations are proved. They do not decide existence of
such a group.

## Countable aspherical homology cores

**Proved statement.** Let `X` be a connected aspherical CW complex of
dimension at most two. Suppose `H_1(X;Z)=0` and `H_2(X;Z)` is countable.
Every countable subcomplex of `X` lies in a connected countable
subcomplex `Y` such that the actual inclusion `Y -> X` induces an
injective homomorphism on fundamental groups and an isomorphism on
integral homology in every degree. The complex `Y` is aspherical.
The collection of all such subcomplexes is directed under inclusion
and has union `X`.

**Proof.** Enlarge the initial subcomplex by countably many cellular
paths to make it connected and contain a fixed basepoint. As `X` is
two-dimensional, its second cellular homology is the kernel of
`d_2:C_2(X;Z)->C_1(X;Z)`. Choose cycles representing all elements of
its countable second homology and add their finite cellular supports.
This gives a connected countable subcomplex `Y_0` whose map to `X`
is onto on second homology.

Given `Y_n`, its fundamental group is countable. For each element in
the kernel of `pi_1(Y_n)->pi_1(X)`, choose one nullhomotopy disk in
`X` and add a finite subcomplex containing its image. Also choose,
for every element of the countable group `H_1(Y_n;Z)`, a cellular
one-cycle representing it and a finite cellular two-chain in `X`
whose boundary is that cycle. Add the supports of those chains.
Connect the resulting subcomplex using countably many paths when
needed. The result `Y_{n+1}` is again countable. Set
`Y=union_{n<omega}Y_n`.

Every loop in `Y` lies in a finite subcomplex and hence in some
`Y_n`. If it becomes null in `X`, its homotopy class was explicitly
killed at the next stage. Thus `pi_1(Y)->pi_1(X)` is injective.
The chosen two-chains likewise give `H_1(Y;Z)=0`. For any inclusion
of two-dimensional CW complexes, the induced map on second
cellular homology is injective, because the inclusion of cellular
two-chains is injective and there are no cellular three-boundaries.
It follows that `H_2(Y;Z)->H_2(X;Z)` is an isomorphism. Connectedness
and dimension settle the other ordinary homology groups.

The universal cover of `Y` is the component over `Y` in the
universal cover of `X`, because of the proved injection on
fundamental groups. It is therefore a subcomplex of a contractible
two-dimensional CW complex. Its second homology vanishes by the
same injectivity of cellular two-cycles. It is simply connected,
and it has no homology above degree two. Hurewicz and Whitehead
therefore make it contractible. This proves asphericity.

For directedness, apply the construction to the union of any two
such countable subcomplexes. Every cell of `X` belongs to a finite
subcomplex, so applying the construction to that subcomplex proves
the union assertion. This completes the proof.

For the homology-sphere instance, this gives a directed union of
countable subgroups with two-dimensional classifying models and
`H_1=0,H_2=Z`, with the specified inclusion maps inducing the
homology isomorphisms. No retraction or quotient map has been
constructed by this argument.

## Exponent-sum matrix route: exact unsolved step

After collapsing a maximal tree in the one-skeleton, ordinary cellular
homology gives a surjection `C_2 -> C_1` with kernel `H_2(X;Z)`.
For the sphere instance the kernel has rank one. The surjection
splits as a map of free abelian groups. This is an assertion about
abelian cellular chains. It does not supply a homomorphism of the
fundamental groups associated to an abelian basis change.

In the acyclic case, the column-finite exponent-sum matrix is an
isomorphism with a column-finite inverse. Matching independent
relation columns to distinct supporting generators suggests a
countable coloring of the resulting finite-outdegree dependency
graph. Even with such a coloring, identifying generators can
create new van Kampen diagrams. A proof that some selected
nonidentity element remains nonidentity in the resulting countable
presentation has not been obtained. No countable-quotient theorem
is inferred from the matrix calculation.

## Surface replacement: why the finite cancellation does not finish the limit

The A agent checked the finite replacement in Bartholdi--Mikhailov
Section 5.3. A zero-exponent-sum relator is represented by a surface;
after attaching its surface block, the old relator disk can be
cancelled against the cylinder three-cell. This gives a new
two-dimensional model and an embedding of the old group. The
models do not remain nested CW subcomplexes, and their mapping
telescope has dimension three.

An additional module check rules out one proposed shortcut. For a
surface block `b:Sigma -> M` with `M` replaced by a two-dimensional
spine and `b_*[Sigma]=0`, the image of the cellular fundamental
two-cycle in `C_2(M;Z)` is exactly zero: it is a two-cycle, it
represents zero homology, and `C_3(M;Z)=0`. Consequently every
coefficient of its lifted cellular image has augmentation zero.
There is no augmentation-one coordinate from which to infer a
split rank-one inclusion in the group-ring chain module. This
does not determine the telescope's geometric dimension; it
identifies the failed proposed splitting argument.

## Primary literature checked independently in this phase

* A. J. Berrick, *The acyclic group dichotomy*, arXiv:1006.4009,
  Section 2, including the actual grope construction and Proposition
  2.3. The displayed maps run from a locally free acyclic group to a
  prescribed perfect group. They provide no reverse map and impose
  no restriction on the small quotients of the source. The explicit
  free-product version has projections to its countable factors.
* Tsunekazu Nishinaka, *Uncountable locally free groups and their
  group rings*, arXiv:1601.00295, Theorem 1.1. The theorem constructs
  a free subgroup of the same cardinality as the locally free group.
  The specified morphism is an embedding; no quotient conclusion
  is used here.
* Nicholas G. Vlamis, *Three perfect mapping class groups*,
  New York J. Math. 27 (2021), 468--474,
  https://nyjm.albany.edu/j/2021/27-18v.pdf, Theorem 1.1 and the
  argument for Corollary 1.3. These supply no-countable-quotient
  examples and their perfectness, but no two-dimensional
  classifying-space statement. They do not settle the dimension
  requirement under investigation.

Searches also tested combinations of uncountable groups, small
Schur multiplier, geometric or cohomological dimension two,
countable quotients, balanced presentations, locally free groups,
and residual countability. No general quotient theorem satisfying
the hypotheses above was found or asserted.

## Forester--Rourke route settled as A.18

The complete proved statement is now in `sections/A_equations.tex`,
with metadata in `Cpaths_Aequations_results.json`. A nontrivial
countable torsion-free group `H` embeds into a countable torsion-free
`U` solving every one-variable equation of exponent sum plus or minus
one. The construction preserves ordinary integral homology and raises
a specified classifying-space dimension only to its maximum with two.
Every transfinite tower of these extensions beginning at `H` maps to
this fixed `U`, with injective restriction on `H`. Thus it has a
specified nontrivial countable image at every tower cardinality.

The primary inputs are Forester--Rourke's *The adjunction problem over
torsion-free groups* (PNAS 102 (2005), 12670--12671, Theorem 1 and
Proposition 1), whose complete author PDF was read, and *Diagrams and
the second homotopy group* (CAG 13 (2005), 801--820), whose Sections
1--3 were read through the root-shape reduction, diagram cancellations,
Lemma 3.1, and the inclusion-induced extension-of-scalars map of
Proposition 3.3. The source theorem requires layering. An arbitrary
invertible exponent matrix does not satisfy that hypothesis merely
because its underlying abelian chain map is invertible.

The D agent independently derived and audited the same countable-target
construction, including the arbitrary-dimensional classifying-space
argument. Its one suggested wording correction (sphere dimensions at
least two in the union argument) has been incorporated.

## A.19: a proved continuum bound

Claim A.19 in `sections/A_cardinal_obstruction.tex` now proves a
uniform detecting-quotient bound. For an actual two-dimensional
classifying space, put
`nu=max(aleph_0,d(H_1(G;Z)),rank H_2(G;Z))`. Every nonidentity
element survives in a quotient of cardinality at most `nu^(aleph_0)`.
For countable homology this is the continuum. The finite-system
input is the October 2026 nonsingular-equation preprint, whose
complete proof has been checked across the root, A, and D agents,
with my independent check of Theorem 2 recorded in
`Cpaths_nonsingular_audit.md`. The proof constructs the actual
quotient maps; it uses no model-theoretic saturation assertion.

The D agent and the root independently checked the complete A.19
manuscript. The D agent's precision about actual attaching supports
was incorporated: `W(r)` consists of the relative one-cell interiors
meeting the attaching image, including traversals absent from a
simplified word. The residual question at a countable quotient
bound, and more generally in `aleph_0 <= mu < 2^(aleph_0)`, is not
decided by A.19.

## Further simple-envelope and amalgam checks

The complete official PDF of Fournier-Facio--Sun,
*Dimensions of finitely generated simple groups and their subgroups*,
arXiv:2503.01987v3, was reopened. I read Theorem 4.1, Remark 4.5,
and Theorem 5.1 and its proof. The cited bibliography entry already
exists as `A_FournierFacioSun2025`.

Remark 4.5 proves that the groups produced by that construction have
infinite-dimensional second rational homology. In the specialization
where every input has geometric dimension at most two, there is a
direct verification independent of any homology-preservation slogan.
After `n` forcing rounds, take the subcomplex with the initial two
loops, the selected one-skeleta of the `L_i`, and just the forcing
two-cells described in that remark. If those one-skeleta add `r_i`
loops, the corresponding forcing steps add `r_i+2` disks. The
subcomplex has one vertex, `2+sum_i r_i` one-cells, and
`sum_i(r_i+2)` two-cells. The kernel of its ordinary cellular
boundary therefore has rational dimension at least `2n-2`.
This subcomplex sits in the actual final two-dimensional classifying
complex, so its second homology injects by inclusion of two-cycles.
Letting `n` grow proves infinite-dimensional `H_2`. Hence these
specific simple-envelope maps cannot supply acyclic simple blocks,
or homology-isomorphism extensions of a fixed core, for the proposed
common-core amalgam route.

The primary paper Jens Harlander, *Embeddings into efficient groups*,
Proc. Edinburgh Math. Soc. 40 (1997), 317--324,
DOI `10.1017/S0013091500023750`, was opened at its publisher PDF.
The main theorem and Corollaries 1--2 with proofs were read. The
dimension-two corollary uses `Z/n * Z/n` factors and states virtual
cohomological dimension two; it does not give the acyclic,
torsion-free, simple block needed here. The higher-dimensional
variant uses `Z^3`. No stronger geometric-dimension or homology
claim is inferred from this source.

The primary Burger--Mozes 1997 announcement was also opened and its
construction through the square-complex description read. It
produces a countable collection indexed by finite valencies and
finite covers; that particular collection does not itself provide
the continuum of distinct blocks needed in the proposed counting
argument. No general nonexistence statement about simple acyclic
two-dimensional groups is inferred.

For a free amalgam `F_p *_C F_q`, the actual Mayer--Vietoris map
identifies `H_2` with the kernel of
`C_ab -> Z^p direct_sum Z^q`, since both vertex groups are free.
Thus an infinitely generated free edge group and finite vertex
ranks force infinite-rank `H_2`. This is the precise obstruction
to using the ordinary finite-vertex-rank Camm pattern unchanged.
The parent and A agent are investigating genuinely infinite vertex
ranks, where the two abelianization maps could jointly form an
isomorphism. No simplicity or no-small-image conclusion has been
proved for that modification.

## A.25: the anchored sparse amalgam route is refuted

The graph analysis of the infinite-rank variant now gives a proved
result, Claim A.25 in `sections/A_sparse_systems.tex`. Over a group
`H` of size at most an infinite cardinal `nu`, fix a group `E_H` of
size at most `nu` solving all finite nonsingular systems. A relative
presentation with integral exponent map an isomorphism maps to this
fixed `E_H`, extending the embedding of `H`, whenever each full
relator word involves at most two new variables and every occurring
new variable has nonzero exponent sum.

The actual exponent graph has only grounded trees and nonsingular
unicyclic components. Two cycles/grounds would give finitely many
columns outnumbering their supporting vertices; an ungrounded tree
would give a nonzero rational functional annihilating all columns.
Solve each ground or cycle in `E_H`, then solve the one-variable
equations outward by finite graph distance. This works at arbitrary
valence and cardinality and constructs the required homomorphism.

For an actual two-dimensional classifying model with countable
first and second homology, a countable homology core can contain
all fixed anchors, any countable exceptional relators, and a
chosen nonidentity element. A.25 then supplies a countable quotient
detecting that element. Thus the direct anchored Camm pattern
`a^n p_alpha^u = b^m q_beta^v`, with `u,v` nonzero, cannot produce
the required no-countable-image example under the stated small
homology hypothesis. The full-word requirement is essential:
zero-exponent occurrences and words with three or more new variables
are outside the proved criterion. The D agent checked the graph
argument, and the A agent audited the complete manuscript without
requesting corrections.


