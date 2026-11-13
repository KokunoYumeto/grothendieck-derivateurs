# What the universal H2 condition gives for graph diagrams

Status: proved graph reformulations and a restricted vanishing result.
The implication from these conditions to exactness is not proved.
In particular no pointwise choice of a free-group basis is being
treated as a natural choice.

Throughout, A is nonempty, connected, and quasi-filtered. Thus

    T_1(Z[H]) = 0

for every covariant A-set H. A directed multigraph means sets E,V
with endpoint maps E->V; loops and multiple edges are allowed.
Morphisms send vertices to vertices and edges to edges, preserving
endpoints. A diagram of such graphs consequently has honest A-sets
of vertices and edges.

## 1. An exact graph reformulation of the universal H2 hypothesis

The following conditions are equivalent:

(a) H_2(B El_A H;Z)=0 for every A-set H.

(b) For every covariant diagram of directed multigraphs G, the natural map

    colim_A Z_1(G_a;Z) -> Z_1(colim_A G_a;Z)

is an isomorphism.

Here colimit on the right is the strict graph colimit, computed on
vertex and edge sets, and Z_1 is the integral cycle group. Because a
graph has no two-cells, Z_1 is also its first homology group.

Proof of (a) => (b). Write V,E for the vertex and edge A-sets and C
for the A-set of graph components. Let I be the image of the incidence
map d:Z[E]->Z[V] and K its kernel. There are exact sequences

    0 -> I -> Z[V] -> Z[C] -> 0,
    0 -> K -> Z[E] -> I -> 0.

Since T_1(Z[C])=0, colim I embeds in colim Z[V]. Since
T_2(Z[C])=0 and T_1(Z[V])=0, the first sequence gives T_1(I)=0.
The second sequence therefore makes colim K embed in colim Z[E],
with image exactly the kernel of colim d. Free abelian groups commute
with set colimits, so this kernel is Z_1(colim G), as asserted.

Surjectivity of the comparison already follows from quasi-filteredness:
T_1(Z[C])=0 makes colim I embed in colim Z[V], and right exactness of
the second sequence gives the required image. The additional H2
hypothesis is what gives injectivity.

Proof of (b) => (a). Every A-set H has a graph presentation with vertex
and edge A-sets free on representables. Explicitly set

    V = coproduct over (a,h in H(a)) of A(a,-),
    E = coproduct over (f:a->b,h in H(a)) of A(b,-).

At x, the edge in the summand (f,h), represented by u:b->x, has
endpoints

    (a,h,uf),    (b,H(f)h,u).

The component quotient is canonically H: both endpoints evaluate to
H(uf)h, and each vertex (a,h,u) is connected by its u-edge to
(x,H(u)h,id_x). The abelian vertex and edge modules are sums of
representables and hence projective. Splitting the displayed graph
sequence through I therefore gives

    T_2(Z[H]) = ker(colim K -> colim Z[E]).

Under (b), colim K is identified with a subgroup of colim Z[E], so
this kernel is zero. The bar/element-category identification proves
(a).

This equivalence is stronger than checking the one row graph attached
to one finite family: it quantifies over all functorial graph diagrams.
It still does not identify a general column cokernel with a graph
cycle module.

## 2. Pointed connected graph diagrams have acyclic cycles in degree one

Assume the equivalent conditions above. Let G be objectwise connected
and possess a natural chosen vertex. Its augmentation Z[V]->constant Z
then has a natural splitting. Hence I=ker(Z[V]->constant Z) is a
direct summand of Z[V]. In particular T_2(I)=0. Applying derived
colimits to

    0 -> Z_1(G) -> Z[E] -> I -> 0

now gives

    T_1(Z_1(G)) = 0,

because T_2(I)=0 and T_1(Z[E])=0. This uses only the universal H2
condition, not totality in higher degrees.

Consequently, if a based free-group diagram admits a natural diagram
of based one-dimensional simplicial models whose maps are simplicial
on cells, its abelianization satisfies this degree-one vanishing.
An objectwise homotopy equivalence to such a model has to be natural.
Maps collapsing a chosen edge to the basepoint can also be accommodated
by reduced permutation modules; their acyclicity follows from the
split constant basepoint summand.

## 3. A useful spectral-sequence refinement

For any based, objectwise connected space diagram Y, the simplicial
replacement chain complex splits naturally as the direct sum of
the base chain complex C_*(A;Z) and its reduced fibre-chain complex.
The splitting comes from the natural basepoint and augmentation.
Thus differentials from the q=0 row to the positive fibre-homology
rows vanish; they cannot absorb a class in T_1(H_1(Y)).

In particular, for a diagram of free groups G, the only nonzero
positive homology row of BG is H_1(BG)=G_ab. The splitting and the
two-row spectral sequence give

    H_2(hocolim_A BG;Z)
        = H_2(BA;Z) direct-sum T_1(G_ab).

Under the universal H2 hypothesis the first summand vanishes, so
T_1(G_ab) is exactly the second homology of that homotopy colimit.
No T_3(constant Z)=0 assumption is needed for this conclusion.

For general abelian M the same splitting removes the apparent incoming
T_3(constant Z) differential from the symmetric-cocycle discussion;
the remaining degree-two fibre-homology contribution still has to be
accounted for. The stronger survival observation does not itself make
T_1(M) vanish.

## 4. Why pointwise free groups and free-factor maps are insufficient input

The nerve BG is natural, but it is not one-dimensional. A free basis
chosen separately at each object produces roses and maps of their
fundamental groups. A transition sends a basis element to a word, so
the corresponding rose map sends an edge to a path, not to one edge.
Furthermore, choosing reduced word representatives does not make
composition of the resulting graph maps literally agree: reduction
of backtracking paths supplies homotopies, not the missing strict
cellular identities.

Thus two requirements must be distinguished:

1. a natural group-valued functor with pointwise free values;
2. a natural graph-valued functor whose edge and vertex sets are A-sets,
   together with natural objectwise classifying-space equivalences.

Free-factor embeddings do not, just by definition, supply the second
structure. Independent relative free-factor decompositions do not
choose coherent bases or coherent one-dimensional simplicial models.
The quasi-filtered AKR free-factor diagram shows that its abelianization
need not be acyclic under quasi-filteredness alone. It does not by
itself disprove existence of a natural graph model: the graph-cycle
vanishing theorem above also uses the universal H2 hypothesis.
The present note gives no counterexample to natural graph modelling
under that stronger hypothesis; obtaining or replacing such a model
is the precise additional issue in this route.

For a free-group presentation one can construct natural universal
covers or Schreier graphs, but these introduce underlying group-element
A-sets and relation modules. Passing from their graph cycle modules to
the desired abelianization requires a coinvariant operation. That
operation is not a set colimit and is not removed by the graph theorem
above. Similarly, a constant-group augmentation gives natural
intermediate covers, but a pointwise free kernel is again a free-group
diagram without the asserted natural graph model.

## Current conclusion

The universal H2 condition precisely controls graph-cycle comparison
and suffices for degree-one acyclicity of based connected graph-cycle
modules. These are verified consequences. No construction here puts
the general simultaneous-equalizer column module into that class,
and no implication to exactness is claimed.
