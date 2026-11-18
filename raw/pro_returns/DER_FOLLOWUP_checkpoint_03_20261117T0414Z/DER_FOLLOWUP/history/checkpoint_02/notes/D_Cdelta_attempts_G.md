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
