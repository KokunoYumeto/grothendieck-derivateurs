# Independent C_delta / free-monoid investigation (localization thread)

AI-produced by GPT-6 Astra, 17 November 2026. This is a working record,
not an assertion that the remaining question is settled.

## Scope and already established input

Read `sections/D.tex` D.1--D.7, `notes/CD_work.md`, and the exact prompt
items D.1--D.4. The general filteredness implication is already refuted
by the exact nonfiltered category Delta_inj, uniformly over every free-
monoid diagram. D.4 supplies the requested free-group alternative over
C_delta. The remaining explicit question is whether C_delta itself
passes every free-monoid comparison or admits a failing such diagram.

The comparison comma is K = int_A D with D(a) the free category on the
directed graph of generator transitions on the common vertex set C,
where C is the monoid colimit. Its ordinary categorical colimit is the
regular translation category of C, with initial object 1. For every
total A, K is simply connected by the fixed-object transport argument.
Exactness is used separately in D.6 to kill T_p^A H_1(D(a)); it cannot
simply be deleted from that proof.

## Route 1: direct extension from totality

Totality implies that for every simplicial-set diagram X on A, the
canonical hocolim_A X -> colim_A X is a weak equivalence: apply the
contractibility of the components of element categories in each
simplicial degree, then use diagonal invariance of bisimplicial sets.
Applying this to N D reduces the comma problem to

    colim_A N D(a) -> N(colim_A^Cat D(a)).

The latter map is not formally an isomorphism and is exactly where new
cross-stage compositions and their relations enter. Total categories
need not be sifted; this prevents an argument based on commuting set
colimits with finite products.

For example, over Delta_inj take the free monoid on the vertices [n].
The monoid colimit is the free monoid on one letter. The set colimit of
the underlying monoids still distinguishes increasing, decreasing, and
equal two-letter vertex patterns. Thus representations of a fixed
colimit monoid element need not form a connected element category.
One cannot contract K merely by choosing one representation of each c.

The word-cut idea communicated by the paths_monoids thread is valid at
its current stage: over El_A(U M), send (a,w) to the ordinal of cuts of
w; word substitutions act by cumulative substituted lengths, including
erasures. This defines a strict functor to finite filtered categories,
and its Grothendieck construction has total components. A comparison
from this construction to the comma K still needs a finality or
contractible-fibre argument; individual word components are insufficient.

## Route 2: positive bases for the group obstruction

The point generators satisfy

    u_b u_a^{-1} = v_a v_c^{-1}

for each ordered edge a<b<c. A single edge has the positive realization
u_b=t u_a and v_a=t v_c. It is incorrect to assume that all edge ratios
t can simultaneously be positive in a common free basis.

More generally, if all four displayed point words are positive, Levi
cancellation only forces a factorization

    u_b=p r,  u_a=q r,  v_a=p s,  v_c=q s,

with positive words p,q,r,s; the ratio is p q^{-1}. Neither p nor q
has to be empty. Therefore an impossibility argument which assumes
every ratio itself positive would not settle the actual question.

A natural stronger ansatz is false already on five vertices. Let
X={1<2<3<4<5} have edges (1,3,4) and (1,2,5). Both edge copies are
strictly closed: each has predimension 3, an extension by one new vertex
has predimension 5, and the full union has predimension 4. All nonempty
induced subobjects have positive predimension. The two equations for
globally nested increasing U-prefixes and decreasing V-suffixes would be

    U_3-U_1 = V_1-V_4,
    U_2-U_1 = V_1-V_5.

Strict U order makes the first left side larger; strict decreasing V
order makes the first right side smaller. This is impossible. Both
threads found this example independently. It refutes only that global
ordered-interval strategy, not arbitrary positive bases.

Introducing separate prefix/suffix letters and imposing their equality
edgewise gives a functorial free monoid on equivalence classes of letters,
but then every transition is a basis map. Its abelianization is a
permutation module, so totality kills all its higher derived colimits;
it does not retain the nonexactness witness Q. This loses precisely the
obstruction one is trying to preserve.

## Status

No counterexample or universal passage theorem has yet been obtained.
Continue at the positive-word subdivision / comma comparison step, or
find a different free-monoid diagram over C_delta whose target homotopy
type can be computed independently.

## Route 3: a precise positive-forest refinement lemma

For chosen free bases S_a, define W(M) as the strict monoidal category
whose objects are finite words of tagged letters (a,s), s in S_a.
Its generating arrows replace (a,s) by the tagged positive word
M(f)(s) at b for f:a→b. Impose the identity and composition relations
of A (composition means applying the same next map to every child
letter), together with interchange of substitutions in disjoint word
positions. Thus arrows are finite planar substitution forests modulo
these specified relations. The component monoid is exactly colim Mon M.

If A satisfies condition I, every such forest can be completed by
further substitutions at its leaves to a one-level uniform substitution
on each root. To prove this, take the finite A-labelled rooted tree of
objects and arrows occurring under a root. Every finite rooted tree
diagram in a category with span-completing commuting squares has a
commuting cocone: adjoin one branch at a time, amalgamating its arrow
with the existing map out of the attachment vertex, and postcompose
the previous cocone. At each node the resulting cocone maps agree with
the substitutions on every child. The defining composition relations
then collapse the entire completed tree to the root's one arrow.
Do this separately for the finitely many roots.

Consequently any two forests with the same source word have a strictly
commuting common completion: flatten each forest, then complete the
two maps out of each root by condition I. Thus W(M) also satisfies
condition I. This is a genuine category-level refinement result, not
just an equality of words in the monoid colimit.

It does not prove that the components of W(M) are contractible. In a
parallel pair of forests, the leaves of the common target are assigned
to possibly different ordered blocks of roots. Gluing the forests
along their common leaves need not leave a rooted A-tree. Hence the
preceding commuting-cocone argument does not give a single common
postcomposition equalizing the pair, nor a homotopy filling of all
higher diagrams. Transferring totality of A to W(M) remains the
specific missing assertion. One must also state and verify the exact
delooping/classifier comparison with hocolim_A BM before using W(M)
to conclude the requested theorem.

The condition-I hypothesis matters. For the span of free monoids
N --(×2)→ N and N→1, the ordinary simplicial pushout of nerves is
the homotopy cofiber of the degree-two circle map, whereas the monoid
pushout is the group Z/2. Their classifying spaces are respectively
the two-dimensional Moore space M(Z/2,1) and K(Z/2,1), so they differ.
A commuting square completing this span in a diagram of free monoids
would force the surviving generator to map to the empty word, since
its square maps to the empty word. Thus this counterexample does not
extend formally to an index satisfying condition I.

## Further cautions

A functorial construction which replaces letters by all prefixes and
suffixes, followed only by equality identifications of those new letters,
is a basis-map diagram and loses the nonexactness witness. Interval-gap
constructions have the same limitation in homology: their edge module
fits into the natural exact sequence

    0 -> Z[gaps] -> Z[S plus two endpoints] -> Z -> 0,

so it is derived-colimit-acyclic over a total index. This explains why
ordinary ordered interval subdivision alone does not reproduce Q.

The stronger unsupported claim that all submonoids of free monoids have
aspherical classifying spaces is false; it must not be used to repair
an injectivization argument. A primary MathOverflow answer opened below
gives an explicit eight-generator, four-relation submonoid with a
two-sphere summand. We have not used that source as a theorem in the
paper or as a step toward the still-unsolved comparison.

## Computation and source/search record

`code/D_Cdelta_attempts_G.py` independently verifies all positive
predimensions and both strict-closed edge embeddings in the five-vertex
counterexample. Its exact row-difference certificate is
(U3-U2)+(V4-V5)=0. Output is
`code/outputs/D_Cdelta_attempts_G.json`; the scope is explicitly limited
to the ordered-prefix ansatz.

Searches:

- `"total category" "free monoid" homotopy colimit`
- `"free monoids" "homotopy colimit"`
- `"total categories" monoids colimits`
- `"totally aspherical" monoids`
- `"free monoids" "colimits" "homotopy"`
- `"localisateur" "monoïdes libres"`
- `"submonoid" "free monoid" "classifying space"`
- `"submonoids of free monoids" "homological"`
- `"submonoid" "free monoid" "universal group"`
- `"homotopy colimits" "free algebras" monoids discrete`
- `"free monoids" "homotopy sifted"`
- `"polynomial monads" "homotopy colimits" classifier`

Opened primary sources:

- George M. Bergman, *On monoids, 2-firs, and semifirs*, author preprint
  https://math.berkeley.edu/~gbergman/papers/submonoid.pdf . Opened
  introduction, Section 2 conditions (3)--(7), and the search-exposed
  Example 20 context. This gives terminology for rigidity and the limits
  of identifying a universal group with a chosen ambient free group.
  It supplies no C_delta comparison theorem. Web ref turn118view1.
- Denis T, primary answer at
  https://mathoverflow.net/questions/122221/is-there-a-discrete-monoid-m-injecting-into-its-group-completion-g-for-which-b/516114 .
  Read the complete answer, including its explicit presentation,
  claimed Brown-rewriting calculation, and its disclosure of partial
  LLM assistance. The associated Brown paper was not opened in this
  thread and no theorem from it is asserted as a paper dependency.
  Web ref turn118view0.
- Batanin--De Leger's polynomial-monad paper was located in search and
  handed to the paths_monoids thread for its own primary-source read;
  this thread has not read that paper. Their message reports that
  Theorems 6.10/6.12 and Remark 7.5 formalize the classifier comparison
  but do not supply the needed totality-to-contractibility assertion.

No new statement about C_delta passing or failing all FreeMon tests
has been proved by these attempts.

## Focused ordered-factorization coherence reduction

Let E=El_A(U M). For n>=1, an n-fold factorization of w in the free
monoid M(a) is uniquely a weakly increasing (n-1)-tuple of cuts in
[0,|w|]. A homomorphism M(f) sends cuts by cumulative substituted
lengths, so these finite cut posets form a strict covariant functor
K_n:E→Cat. Each K_n(a,w) is a nonempty finite filtered poset.
Consequently int_E K_n has contractible components (indeed total
components by the Grothendieck stability result used elsewhere).
Keeping only transport arrows, with no movement of cuts, gives exactly
El_A(M^n) over E via multiplication.

Inside W(M), all cut choices for the same tagged word concatenate to
literally the same object. A vertical cut slide therefore maps to its
identity, and a transport maps to the uniform substitution of the whole
word. This checks the strict functor from the cut construction to W(M).
It does not account for contextual substitutions on factors at different
stages. The needed additional coherence statement must show that these
ordered-cut constructions, together with products of genuine A-action
categories, supply all higher relations between contextual forests.

There is a concrete distinction between local and global label data.
Fix the finite A-labelled sources and internal data of a forest. Its
target-refinement categories, defined by finitely many commuting
equations preserved by postcomposition, are categories of elements of
covariant Set functors on A or a finite product A^k. Each of their
components is contractible. One cannot simply assert that the entire
category A^T of varying tree labels is total: an internal vertex is
simultaneously the target and source of arrows, so variation has both
variances. Nor can one ignore distinct components of the refinement
category: in C_delta these can record different overlap and induced-
amalgam types. A successful tree/associahedral proof must show that tree
contractions and cut slides glue the relevant components contractibly
over the actual comparison fibre.

The tower thread has meanwhile constructed a positive-integer-matrix
stabilization of Q preserving T1=Z. Therefore an argument claiming that
arbitrary positive matrix coefficient diagrams are acyclic over a total
category is unavailable. Actual ordered word substitutions, including
their strict compositional coherence, are essential.

One instructive nonabelian check of their first stabilization is as
follows. In F(a,b,g), put x=a g^{-1}, y=b, z=g b. The automorphism
tau(a)=ba, tau(b)=bab, tau(g)=g becomes

    tau(x)=yx, tau(y)=yxz, tau(z)=zxz.

It is positive in this basis. Nevertheless a=x z y^{-1} satisfies
tau^n(a)=tau^n(x) z y^{-1} for every n, and is never a positive word,
even though its abelian coordinates eventually become positive.
Choosing source auxiliary basis A=ab,B=b repairs this first inclusion:
A=xz,B=y, with tau(A)=B A^2 and tau(B)=B A. This realizes the first
split as a genuine cut of a positive auxiliary word. It supplies no
proof for arbitrary further free-group transition words; those would
have to preserve compatible cut configurations. Both observations
were communicated to the tower thread.

## Unit-component rigidity of the forest category (03:20 UTC)

The component of the empty word in W(M) has the empty word as a
terminal object. Indeed, in any category satisfying condition I,
objects in the same connected component admit a common successor:
induct along a connecting zigzag, completing each outward fork by a
commuting square. The empty word has no nonidentity outgoing arrows
in W(M), because it has no letters to substitute. Hence a common
successor of a word w and the empty word must be the empty word
itself. This supplies an erasure forest w -> empty for every word
representing 1 in C=colim Mon M. If two such erasure forests exist,
condition I completes them by arrows out of the empty word; these
arrows must both be identities, so the two forests agree.

In particular every equality w=1 in the monoid colimit can be
witnessed by a purely forward erasure, and this witness is unique in
the forest category with its specified composition/interchange
relations. This does not prove the desired comparison: nonidentity
components and their contextual gluing are still uncontrolled.
Contractibility of the unit component alone is insufficient for a
general topological monoid to be homotopy-discrete after delooping.

Two algebraic consequences of the same refinement are rigorous.

1. C is conical: if ab=1, concatenate tagged representatives of a and
   b. Its unique erasing forest splits over the two subwords, so both
   factors represent 1. Thus C has no nontrivial one-sided units.
2. C is equidivisible: if ab=cd, their concatenated representatives
   have a common forward target word Z. The two root-block partitions
   give Z=PQ=RS, where [P]=a, [Q]=b, [R]=c, [S]=d. Comparison of the
   two cuts in the free word Z gives either P=RT and S=TQ, or R=PT
   and Q=TS. Taking classes yields either a=ct and d=tb, or c=at
   and b=td. This is the equidivisibility property suggested
   independently by the paths_monoids thread.

Neither conclusion supplies asphericity: conical equidivisible monoids
can have nonzero higher homology, as the rectangular-band example
discussed in the other thread illustrates.

The overlap graph of two interval partitions of a word is a forest:
scan the linearly ordered cuts; adding a new nonempty overlap interval
introduces one new block vertex unless it begins a new component.
This observation was reached independently in both threads. It helps
with label amalgamation when the two copies of the source blocks are
kept distinct. For a parallel pair of forests their source roots are
also identified. Those identifications can reintroduce cycles; for
example the partitions [1,2]|[3] and [1]|[2,3] have such an additional
identification pattern. Thus the interval-overlap observation alone
does not prove that parallel forests have equalizing postcompositions
or contractible spaces of higher coherences.

## Reduction to nonerasing word substitutions (03:33 UTC)

The unit-component argument gives a useful exact reduction of the
remaining question. For each a let E_a be the set of basis letters of
M(a) whose image in C is 1, and let M'(a) be the free monoid on the
complementary basis. Define p_a:M(a)->M'(a) by deleting E_a. If s is
in E_a then every letter of M(f)(s) is in E_b, since its product has
class 1 and C is conical. Thus there is a unique strict induced
diagram M', with p:M->M' natural. If s is outside E_a, its image under
M'(f) cannot be empty, because otherwise its C-class would be 1.
Hence every substitution in M' is nonerasing.

Each s in E_a can be erased by a single arrow f:a->b. Indeed, its
erasure forest exists by the terminal-empty-word lemma. Complete its
finite A-labelled root tree to a cocone. Even an erased final branch
retains its target A-object; the uniform composition relation gives
M(f)(s)=empty at the common cocone object. Condition I combines
finitely many such arrows with the same source, so any finite subset
of E_a can be erased simultaneously by one arrow.

For each n>=0 the induced map

    colim_A M(a)^n -> colim_A M'(a)^n

is a bijection. It is surjective because each p_a is. For injectivity,
the additional relations imposed by the deletion quotient already
hold in the original set colimit: a finite tuple of words and its
deleted tuple have equal images under one arrow erasing all the E_a
letters appearing in those words. Equivalently, lift a finite zigzag
of equalities in the M' diagram and insert these actual equality
witnesses at its vertices. This works simultaneously in all n
coordinates. The resulting bijections respect all nerve faces and
degeneracies, so colim_A N M -> colim_A N M' is an isomorphism of
simplicial sets. Also colim Mon M'=C, since every deleted letter was
already equal to 1 in the monoid colimit.

For a total index A, the canonical homotopy-colimit-to-simplicial-
colimit comparisons are weak equivalences. Therefore

    hocolim_A B M(a) -> hocolim_A B M'(a)

is a weak equivalence, and the free-monoid comparison for M passes
if and only if the one for M' passes. Thus one may assume throughout
the unresolved C_delta analysis that all substitutions are nonerasing.
In particular root-cut maps in a substitution forest are then strictly
increasing, with no collapsed intervals.

This does not justify an injectivity assumption. Quotienting a free
monoid by eventual equality of positive words need not leave a free
monoid (for instance the image generated by a^2 and a^3 has a
nontrivial relation). Injectivization remains useful in the Fraisse
limit reduction, where the value is a filtered colimit of free
monoids, but cannot simply be substituted for objectwise freeness.

Additional searches, with no exact comparison theorem found:

- `"free algebras" "aspherical"`
- `"cartesian monad" "colimits" "free" "homotopy"`
- `"monoids" "totalement" "aspherique"`
- `"strongly regular" "homotopy" "colimits"`
- `"cartesian monad" "aspherical"`
- `"totalement aspherique" "monoides"`
- `"free monoids" "derived colimits"`
- `"free monoids" "Riguet"`
- `"totally aspherical" "monads"`
- `"equidivisible" "classifying space"`

Search additionally located the official-journal page for *Infinity-
Operads as Analytic Monads* (IMRN 2022, 12516ff), but that paper was
not opened or used as a proof dependency in this thread.

## Coincidence monoids and finite free hulls (03:43 UTC)

Primary source read: Stepan Holub, *Binary equality sets are generated
by two words*, revised author PDF
https://www.karlin.mff.cuni.cz/~holub/soubory/freshidea.pdf . Read
Section 3, especially Lemma 3 on PDF page 8 (printed page 9): the
coincidence monoid of two nonerasing morphisms is free on its minimal
coincidence pairs, a bifix code. The proof is the ordered-common-cut
decomposition. The statement is elementary for arbitrary alphabets:
for g:U*->T* and h:V*->T*, scan the common image of a pair (u,v), and
cut at every position that is simultaneously a g-letter boundary and
an h-letter boundary. This is a unique factorization into indecomposable
coincidence pairs. Nonerasing is needed to make these boundaries
strictly increasing. Thus nonerasing morphisms of free monoids admit
free pullbacks. Web ref turn505117074view1.

Primary source read: Giuseppa Castiglione, Gabriele Fici, Antonio
Restivo, *On Sets of Words of Rank Two*, arXiv:1810.02182v2,
https://arxiv.org/html/1810.02182v2 . Read Section 2, Theorems 2.1 and
2.2, and the preceding free-intersection/free-hull statement. These
give the defect theorem: a finite non-code of r words is contained
in a free submonoid of rank at most r-1; its minimal free hull has
rank at most r. This is only used below as a standard input to a new
reduction, not as a solution of the C_delta comparison. Web ref
turn926867163view0. Direct PDF/html opens initially failed; following
the experimental HTML link from the opened abstract succeeded.

Primary source read for the stability criterion: Arturo Carpi and
Flavio D'Alessandro, *Cerny-like problems for finite sets of words*,
ICTCS 2014 proceedings, pp. 81--92, Theorem 1 on p.84 (PDF page90),
https://ceur-ws.org/Vol-1231/proceedings.pdf . A submonoid of a free
monoid is free exactly when it is stable: if n_2=u n_1 and n_4=n_3 u
with all four n_i in the submonoid, then u also lies in it. Web refs
turn196701463view0 / turn250291324view0. The Berstel tutorial at
https://www-igm.univ-mlv.fr/~berstel/Articles/2003TutorialCoWdec03.pdf
was located, but both attempts to open it failed (timeout, then502),
so it is not recorded as read.

### Lemma: a filtered colimit of free monoids is locally free

Here 'locally free' means every finite subset is contained in a finite
rank free submonoid, rather than that every finitely generated
submonoid is free (the latter is false). Let S=colim_i F_i be a
filtered colimit of free monoids and lift a finite subset X of S to
some F_i. Consider all later stages j and finite rank free submonoids
H_j of F_j containing that image of X. Such submonoids exist, and
their ranks are nonnegative integers; choose a pair (j,H_j) of least
possible rank r. If any later transition were noninjective on H_j,
the images of its r free generators would satisfy a nontrivial word
equation. If an image is empty or two images coincide, first remove
empty entries or duplicate entries; there are then fewer than r
generators and the same conclusion follows directly from the free-
hull rank bound. Otherwise the r distinct nonempty images form a
non-code, and the defect theorem applies. In either case it puts
their images, hence the image
of X, in a free submonoid of rank less than r at that later stage,
a contradiction. Therefore H_j embeds in the filtered colimit S.
Its image is the required finite free submonoid containing X.
If X is contained in {1}, the trivial rank-zero monoid is already
the required chart and hull.

Filtered colimits of free monoids are cancellative and conical:
each finite equality witnessing a failure of cancellation or a
nontrivial one-sided inverse would already be witnessed at a free
stage. They are also equidivisible, by the same finite-witness
argument applied to the two alternatives of Levi's lemma.

### Lemma: canonical finite free hull inside S

Let S be cancellative and conical and suppose every finite subset
lies in a free submonoid. For finite X subset S choose a finite rank
free submonoid H containing X, and let F_H(X) be the ordinary free
hull inside H. This is independent of H and is the least free
submonoid of S containing X.

To verify the key intersection step, let N be any free submonoid of
S. The submonoid N intersect H is stable inside H. Indeed suppose
u lies in H and n_2=u n_1, n_4=n_3 u with all n_i in N intersect H.
The equality n_3 n_2=n_4 n_1 in free N has a Levi factorization.
Either n_4=n_3 t and n_2=t n_1, in which case ambient cancellation
gives t=u, or n_3=n_4 t, in which case ambient cancellation gives
u t=1 and conicality gives u=1. In both cases u is in N. Thus the
stability criterion makes N intersect H free. It contains X, so
F_H(X) is contained in N. Conversely F_H(X) itself is a free
submonoid of S containing X. This proves the asserted minimality
and independence. The defect theorem bounds its rank by |X|.

Write this canonical submonoid as F_S(X). Every automorphism of S
that fixes X pointwise fixes F_S(X) pointwise. Minimality first shows
that the automorphism preserves the hull. It therefore permutes the
unique free basis of that hull. Every basis letter appears in some
word of X (otherwise deleting that letter gives a smaller free
submonoid containing X). Since the words of X are fixed and free
factorizations are unique, every such basis letter is fixed.

### Application: injective free replacement over C_delta

This application uses the established Fraisse/orbit description from
R17 and the parent thread's product-compatible reduction. First
suppose every M(B) has finite rank. Form the smooth G-monoid S by
the filtered colimit over actual finite closed substructures B of the
Fraisse limit. Put

    N(B)=F_S(image of the free basis of M(B)).

Each N(B) is finite free. For a closed inclusion B subset D, minimality
gives N(B) subset N(D). For an actual embedding f:B->D, extend f to
an automorphism g of the Fraisse limit and restrict g on S. It sends
N(B) into N(D). Different extensions differ by an element fixing B;
such an element fixes image M(B), hence its free hull pointwise, so
the resulting map is independent of the extension. The same fact
makes composition strictly functorial. All transitions are injective,
and there is a natural map M->N.

The filtered union of the N(B)'s is exactly S: it contains every
original image M(B), and each N(B) is already a submonoid of S.
Hence M and N have the same smooth G-monoid and the same monoid
coinvariant C. In each finite simplicial degree, their set colimits
are both S^n/G (filtered colimits commute with finite products).
Thus colim_A Nerve(M)->colim_A Nerve(N) is a simplicial isomorphism.
Since C_delta is total, the natural homotopy-colimit map is a weak
equivalence. The comparison question for M is therefore equivalent
to the comparison question for N.

The finite-rank restriction can be removed by filtered union. Choose
finitely many tagged basis letters (B_i,s_i) of M. At object D take
the union of the supports of M(f)(s_i) for all f:B_i->D. This is a
finite set because the embedding sets are finite. It defines a free
subdiagram: under a further g:D->E, every letter in the image of an
included basis letter also occurs in M(gf)(s_i), because substitutions
are positive and cannot cancel letters. These finite-rank
subdiagrams form a filtered union equal to M. Both sides of q_M and
their comparison commute with this filtered union (nerves use finite
powers and weak homotopy equivalences are stable under filtered
simplicial colimits). Therefore it suffices to test finite-rank M.

Subject only to the already-proved R17 orbit identification, this
reduces the explicit C_delta question to diagrams of finite rank
free monoids with injective, and hence nonerasing, transition maps.
It does not settle the comparison. In particular such monomorphisms
need not induce injective maps of free-group completions: the code
{aa,ab,ba,bb} gives a free rank-four submonoid of the rank-two free
monoid, but its group completion map has a nontrivial kernel.
Writing the four free generators as x,y,z,w in that order, the
nontrivial reduced word x z^{-1} w y^{-1} maps to the identity.

Additional searches for this stage:

- `"colimits" "free categories" "classifying spaces"`
- `"free categories" "homotopy colimit"`
- `"Squier" "diagram" "category" "homotopy colimit"`
- `"Ore condition" "classifying space" monoid`
- `"calculus of fractions" "aspherical" category`
- `"right reversible" monoid "classifying"`
- `"free hull" "monoid" "rank" defect`
- `"Schutzenberger" "stable" "submonoid" free`
- `"filtered colimit" "free monoids" "locally"`
- `"On k-Maximal Submonoids" arxiv`
- `"free hull" "Defect Theorem" site:arxiv.org`
- `"2003TutorialCoWdec03"`
- `"Combinatorics on Words" "A Tutorial" Berstel Karhumaki 2003`
- `"Binary equality sets are generated by two words" "259"`

Ore/aspherical search hits were not used as theorem dependencies.
Full cancellation/fraction conditions cannot be assumed for W(M):
even a constant rank-one M has length-one subcategory equal to A,
and C_delta embeddings are monic but not epic. Two distinct embeddings
may agree after restriction to a smaller closed source and cannot be
equalized by postcomposing another embedding. Any successful Ore
argument must replace this strict cancellation by a proved homotopy
version using totality.

## Polynomial-monad classifier audit (03:55 UTC)

Opened Batanin--Berger, *Homotopy theory for algebras over polynomial
monads*, TAC32(6) (2017),148--253, primary paper in Rochester's
institutional mirror:
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/batanin-berger.pdf .
Read Theorems5.14--5.15 and Remark5.16, and Theorem8.2 with its
bar-resolution proof, Remark8.3, and Corollary8.4. Web refs
turn457722139view0, turn597795444view0--2. The official TAC PDF
open timed out; the MPG copy returned403. These failed attempts
preceded the successful mirror read. The exact bibliography entry
is DGBataninBerger2017 in D_Cdelta_references_G.bib.

Theorem8.2 identifies a derived left adjoint of polynomial-monad
algebras with a homotopy colimit over the internal algebra classifier.
Its proof identifies the relevant bar resolution with a Bousfield--
Kan simplicial replacement. This supplies a precise framework, but
does not assert that the decorated classifier for a diagram indexed
by an arbitrary total category has contractible components. Tameness
concerns the different classifier of semifree algebra extensions.

For the monad encoding A-diagrams of monoids and its map to the
free-monoid monad, classifier objects are words of A-objects; arrows
merge ordered blocks using A-arrows and multiply their decorations.
The decoration at a word of objects is the product of the corresponding
monoids. Objectwise free multiplication reduces words to their basis
letters, returning the global substitution-forest coherence problem.
Consequently the paper has not been used to declare that problem
solved or to claim the same conclusion for free groups.

Additional queries:

- `"polynomial monads" "total" "classifier"`
- `"tame" "polynomial monads" "colimits" "free"`
- `"cartesian monad" "total category"`

The finite-hull reduction in this note was independently audited by
both other mathematical threads and promoted to paper ClaimD.9 in
sections/D_reductions.tex. The empty-image/duplicate-image and
rank-zero edge cases are included there. Its isolated LuaLaTeX first
pass had no overfull boxes; full bibliography passes are retained in
build/D_reductions_check*.

The root integration subsequently built D.8 and D.9 in the master
paper with no warnings or overflows. At the root's request, the
superseded isolated test PDF build/D_reductions_check.pdf was removed;
its TeX source, bibliography files, and all compilation logs remain.
No additional PDF deliverable was created.

## Pure bifix does not by itself remove group folds

Let H be the submonoid of free(a,b,c,d) generated by

    x=ab, y=ac, z=db, w=dc.

The four length-two words form a bifix code, so H is free of rank4.
Its words are exactly ((a|d)(b|c))*. It is both left and right
unitary, since removing an accepted prefix or suffix leaves an
alternating word starting in {a,d} and ending in {b,c}. It is pure:
if v^k is accepted and |v| is odd, two adjacent copies would create
a forbidden pair from {a,d} at their seam; hence |v| is even and
v itself is accepted. Nevertheless x z^{-1} w y^{-1} is a
nontrivial reduced free-group word and has identity image.

This strengthens the fold warning but does not assert that H is a
saturated fixed submonoid. In a free ambient monoid, fixing the four
displayed words by automorphisms fixes all four letters, so that
particular realization cannot be a full fixed submonoid of an
automorphism group. Actual saturation may therefore impose stronger
constraints than purity and biunitarity alone.

The existing independent program code/D_Cdelta_attempts_G.py now
verifies both this exact reduced-word kernel and the even-binary-code
kernel used in paper D.9. For the pure-bifix example it computes the
entire six-element transformation monoid of the three-state DFA for
((a|d)(b|c))*; all transformations satisfy the return and preimage
conditions proving purity and unitarity for all words. This is a
finite exact certificate, not a bounded word search. The existing
JSON output has been updated and every assertion passed.

## Independent audit of the invariant positive length theorem

At the 04:06 UTC request of the tower agent, independently checked
all seven steps of notes/D_invariant_length_theorem.md. The proof
is sound with the following interpretation and clarifications.

1. Invariance and strict positivity of the real length imply that
   an automorphism fixing a product fixes each factor: compare its
   two prefix factorizations using equidivisibility, and apply length
   to the leftover factor. Consequently each fixed monoid S_F is
   factor-closed, and its intersection with a finite free chart H
   is free on a subset of the basis of H.
2. The inclusions of chart edge-chain modules indexed by those
   subsets form a natural transformation of J-diagrams. Filtered
   exactness therefore embeds E_F into E even when individual
   chart transition maps have kernels. No injectivity of the maps
   on free groups, graph homology, or chart chains is assumed.
3. Finite sums and intersections of the chart basis submodules
   commute with filtered colimits. Together with the stabilizer
   identity <G_F,G_D>=G_(F intersection D), this proves the displayed
   distributivity identity. It is an identity of EDGE modules;
   analogous distributivity for cycle submodules would be false.
4. For a support B of size n, its intersection with all lower
   supports and all other n-point supports is exactly the sum of
   its proper closed support submodules. This verifies the direct
   sum formula for each graded piece. Closed embeddings of a
   rigid finite ordered B into F are precisely its copies as
   closed subsets. Extensions to G induce well-defined maps on
   V_B because G_B fixes E_B pointwise. Thus the graded piece is
   indeed a direct sum of representables tensored with V_B.
   Arbitrary abelian coefficient groups cause no flatness issue:
   the representable bar complex contracts with those coefficients.
5. Put K=im(E_F -> Z[C]). From 0 -> K -> Z[C] -> Z[pi_0] -> 0,
   vanishing of the two outer higher derived colimits implies
   T_i K=0 for i>0. From 0 -> H_1 -> E -> K -> 0, the same argument
   gives T_i H_1=0 for i>0. The homology spectral sequence then
   kills every total degree at least two. D.6 supplies connectivity
   and simple connectivity, so Hurewicz and Whitehead finish the
   comparison-comma argument.
6. In Step 7, "abelianization" must mean the UNIVERSAL ABELIAN
   GROUP (S_F^gp)_ab, not the commutative-monoid quotient. With
   this conventional meaning, the edge module for one vertex is
   exactly that group, filtered colimits preserve it, and D.1/D.8
   yield T_i(M_ab)=0 for i>0.
7. A strict word lift of the specified based positive-matrix
   stabilization would inherit the displayed natural positive
   real length. This remains strictly positive on every nonunit
   of the filtered limit and is G-invariant. Its T_1=Z therefore
   contradicts the theorem. The conclusion is only nonexistence
   of a lift in those specified bases with that positive functional;
   it does not settle the unrestricted C_delta FreeMon question.

The audit and the sole terminology correction were sent to the
root and tower agents before the 04:14 UTC checkpoint. This is a
proof audit rather than a computational claim; no additional code,
PDF, or external factual source was required.
