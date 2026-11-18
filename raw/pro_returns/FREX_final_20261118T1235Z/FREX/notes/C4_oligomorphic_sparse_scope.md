# An oligomorphic scope check for the rational gate

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
Recorded 18 November 2026, 09:58 UTC. This is a fully specified auxiliary
example, not a resolution of A.3(iii) or of total C.4. Its group is
nonamenable.

## Class and opened source

Put delta(X)=2|X|-|E(X)| for finite simple graphs, and
F(x)=log(1+5x). Let K_F consist of finite graphs X satisfying
delta(U)>=F(|U|) for every U subset X, expanded by an arbitrary linear
order. Maps are increasing induced embeddings with strictly d-closed
image: A<=_d X means delta(A)<delta(U) for every A proper subset U
subseteq X. Include the empty structure for amalgamation and use the
nonempty objects as the index category.

The complete primary source was reopened:
Evans--Hubicka--Nesetril, *Automorphism groups and Ramsey properties of
sparse graphs*, arXiv:1801.01165v5 (16 January 2019),
https://arxiv.org/pdf/1801.01165 . Definition 4.13, Theorem 4.14 and
Example 4.15 are on printed pages 26--27. The full free-amalgamation
proof in Example 4.15 was read. Retrieval references in this run:
turn103092261view0 and turn286489452view0. The local supplied source is
background/arxiv/1801.01165/SparseRamsey-arxiv4.tex; the PDF numbering
was checked independently rather than inferred from source labels.

Here F is increasing and unbounded, F(0)=0, and its decreasing
derivative 5/(1+5x) is at most 1/x for x>0. Thus Example 4.15 applies.
The independent order amalgamates by putting the first side before
the second side in each gap of the base, exactly as in D:closure.
This gives (S), (Rig), (SA), (FA), and (FA-empty).

## Oligomorphicity

Submodularity gives the same strict-closure intersection calculus as
D:closure. If C is the closure of a finite A, then delta(C)<=delta(A),
and hence

    |C| <= (exp(2|A|)-1)/5.

For completeness, delta(C)<=delta(A) follows by choosing a largest
superset of A that minimizes delta among all its supersets in a finite
strong ambient object. That largest minimizer is d-closed; minimality
of C and d-closedness of C force it to equal C. The bound is uniform
in the ambient object. There are only finitely many ordered graph
types of bounded size, so strong homogeneity gives finitely many
orbits on each finite tuple power. This is also precisely the
argument of Theorem 4.14 and Remarks 2.8 of the opened source.

## Totality and stabilizers

The circular bridge from D:total still works with the added F-bound.
Use its notation B,C<=D, E containing the two copies of D,
m=max(|B|,|C|), and s even circle factors. Choose s sufficiently large
that the order interpolation requirements hold and

    ceil(s/3)-2m > max(delta(E), F((s-1)|D|+|E|)).

This is possible since the left side is linear in s and the second
term on the right is logarithmic. For a subset whose proper vertex
visibility intervals miss a factor, cut at that factor. Its vertices
and edges lift uniquely into a linear free amalgam in K_F, so the
F-bound follows. If the intervals cover the circle, the integer
predimension increment argument of D:total gives
delta(U)>=ceil(s/3)-2m; the total number of quotient vertices is at
most (s-1)|D|+|E|, so this is greater than F(|U|). The same inequality
is greater than delta(E) and proves that every original factor is
strong. All other incidence and order parts of that bridge are
unchanged, because the strong relation is the same strict
predimension relation.

Consequently the bridge proves (St). Free amalgamation gives the
fixed-point identity Fix(G_B)=B for finite strong B. The minimal
support argument, rigidity, and intersections then prove (Op),
exactly as in D:total. Its action-component reduction, using the
already checked functorial amalgams including the empty base, proves
totality. No assertion about arbitrary free amalgamation classes is
used here: the logarithmic circle estimate is the extra check.

## Failure of exactness over every nonzero ring

The ordered triangle W is in K_F: its nonempty induced subgraphs
have predimensions 2,3,3, which exceed log6,log11,log16 respectively.
Its singletons are strong, while no two-element subset is strong.
Two distinct strong copies of W in an object therefore intersect in
at most one vertex. For r such copies, their 3r distinct edges and
the positivity of the induced vertex union give 2v>3r. If every
union vertex were in two copies, incidence counting would give
3r>=2v, a contradiction. Thus some vertex belongs to only one copy.

The same private-vertex proof as D:nonexact shows that

    R[Emb(W,X)] -> R[Emb(V,X)]^2,
    [g] |-> ([gv2]-[gv1], [gv3]-[gv1])

is injective for every X and every nonzero unital ring R. On
colimits the map is zero from R to R^2. Its cokernel therefore has
T_1 isomorphic to R. In particular this oligomorphic, total example
is not rationally exact and not exact over any prime field.

## Amenability and scope

Every singleton is strong in every object: any proper extension has
at least two vertices and integer predimension at least
ceil(log11)=3, whereas a singleton has predimension 2. Strong edges
exist and have infinitely many images over either endpoint by free
amalgamation. The graph is 2-sparse. The opened EHN Theorem 3.8, or
the orientation probability argument already checked in D:amenability,
therefore proves nonamenability, including after the independent
order expansion.

Thus oligomorphicity, even with totality and all of the named
amalgamation/stabilizer hypotheses, does not by itself imply rational
exactness. This does not decide the amenable case: the example fails
the amenability hypothesis. It also has no bearing on the implication
from all-prime exactness under totality, since it fails every prime.
No new main-row movement is claimed for this scope check.
