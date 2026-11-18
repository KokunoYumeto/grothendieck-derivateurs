# C-delta free-monoid investigation: root notes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. These are working routes, not claimed solutions.

## 1. A positive version of the free-group diagram need not suffice

D.4 proves that its free-group diagram has source H2=Z and free group colimit. Even if compatible positive monoid cones were constructed in all those groups, one would still have to calculate the **monoid** colimit. Its classifying space could retain the nonzero H2 that group completion kills. Thus positivity alone does not refute the monoid comparison. This distinction was communicated to both investigating agents.

## 2. Attempt to turn arbitrary free abelian maps into positive maps

The module Q in R17 is objectwise free of finite rank, with transition matrices that may have negative entries in a chosen basis. A tempting stabilization is E_A=Q_A⊕Z, with maps f⊕N_f where N_f is a rapidly growing multiplicative size weight. One would choose unimodular simplicial cones containing the invariant scalar axis in their interiors, so scalar expansion dominates the signed matrix.

There is an elementary obstruction to the simplest integral form. Suppose h:E→Z is the primitive quotient, v is its chosen splitting with h(v)=1, and a basis b_1,...,b_d has h(b_i)>0 and puts v in the interior of its nonnegative cone. Then v=Σ n_i b_i with every n_i a positive integer, so 1=h(v)=Σ n_i h(b_i)≥d. Thus this is impossible for d>1. This rules out that proposed cone choice, not every possible positive stabilization.

Using a rational interior axis introduces a different problem. With axis (v_A,k) in Q_A⊕Z, an extension preserving axes up to scalar N_f would have the form

    (q,t) ↦ (f(q) + t (N_f v_B − f(v_A))/k, N_f t).

It is integral only if N_f v_B ≡ f(v_A) modulo k. Arbitrarily increasing N_f does not impose this vector congruence. A compatible family of residue vectors, or a different lattice construction, would be needed; none has been established. Passing to rational vector spaces would no longer give the free abelian groups that are abelianizations of free monoids.

## 3. First-return loop monoids are positive but change the group

A functor of pointed free directed categories does induce homomorphisms between their first-return loop monoids: a loop decomposes uniquely at its visits to the base vertex. Those monoids are free, and transitions are positive word substitutions. This offers a canonical positive construction, but it does not recover the fundamental group of the whole graph.

For the graph with vertices x,v and edges a:x→v, b:v→x, c:v→v, the first-return loops at x are exactly a c^n b, n≥0. Any loop is a unique concatenation of such words. Hence the loop monoid has a countably infinite free basis, while the connected underlying graph has three edges and two vertices, so its fundamental group is free of rank2. The inclusion of the one-object loop category is therefore not a weak equivalence. A replacement argument would have to address this discrepancy explicitly.

## 4. Remaining promising route

For a total index A, hocolim_A X→colim_A X is a weak equivalence for every simplicial-set diagram X. Applying this to the nerves of the fixed-object translation categories reduces the comparison to the passage from their simplicial colimit to their categorical colimit. Condition I provides commuting squares for spans and may give common refinements of contextual positive-word substitutions. Parallel refinements still require the full all-action totality hypothesis. The other threads are investigating a planar substitution-forest model and a positive presentation, respectively. Neither reduction alone proves the required comparison.

## 5. Injectivization, saturation, and the limits of the orbit route

For any action L on C_delta, define x~y at a when some arrow a→b identifies them. Condition I combines two witnesses from a, so this is an equivalence relation. The same amalgamation combines finitely many witnesses, proving that this injectivization commutes with finite products. For a monoid diagram, multiplication is therefore well defined after injectivization. Filtered union over finite closed subsets of the Fraïssé limit and fixed points of G_a also commute with finite products. Thus the R17 action reduction can be applied degreewise to the nerve of a monoid diagram.

The saturated object is a continuous G-monoid S; it is a filtered colimit of the original free monoids along actual inclusions of finite closed structures. The candidate comparison becomes the simplicial orbit map `(NS)/G → N(S_G)`, where S_G means **monoid coinvariants**, not just the orbit set. A proof would have to compare these two different quotients. The filtered-colimit monoid is cancellative, conical and equidivisible, by the corresponding finite existential/Horn properties in free monoids. It need not have an N-valued length. An element can be a proper prefix of its translate: an interval-subdivision example under order automorphisms already has that phenomenon. Therefore a proof based on preservation of discrete length or equality of supports of a product is invalid.

The tower thread subsequently proved a different, irrational rank-two positive stabilization, recorded in `D_positive_stabilization.md`. This repairs the matrix-positivity attempt but **does not produce a strict word-substitution functor**. Moreover even a positive functor with T₁(M_ab)≠0 would not alone disprove q_M: the colimit monoid may have the same nonzero H₂. Knowing only that its group completion is free does not establish that its classifying space is aspherical.

## 6. Further exact searches and inspected sources, 03:05–03:07 UTC

Queries actually run:

- `"free monoids" "homotopy colimit" filtered`
- `"equidivisible" "classifying space" monoid`
- `nerve free categories colimit categorical realization weak equivalence substitutions`
- `"Homotopy theory of monoids and derived localization" arxiv`
- `"Simplicial monoids and Segal categories" Bergner arxiv`

Chuang–Holstein–Lazarev, arXiv:1810.00373v3, primary PDF, was opened at §§2.3–2.5, Proposition 4.1, Corollary 5.1 and Theorem 5.2 with the relevant proofs. Its equivalence of relative categories preserves derived constructions, but says nothing that identifies the required ordinary FreeMon colimit with that derived construction. This route has therefore not removed the comparison problem.

Bergner, *Simplicial monoids and Segal categories*, primary author PDF, was opened at Definitions 1.1–1.5 and the free-monoid/Segal localization argument in Proposition 4.2, Lemma 4.6 and Proposition 4.7. The separate three-page correction arXiv:0806.1767 was opened in full: the original Proposition 3.12 proposed a nonadjoint pair, and the corrected rigidification uses the strictly local algebraic-theory formulation. Neither the uncorrected adjunction nor a false claim that arbitrary colimits commute with products is used. A precise cofibrancy or forest-coherence comparison would still be needed for C_delta.

The source records are `D_root_attempt_refs.bib`. These failed applications are recorded as failed applications, not as flaws in the corrected cited theorems.

## 7. A concrete obstruction to an unrestricted positive-basis theorem

Let F=F(a,b), and mark the three elements a,b,c with

    c=(ab)a(ab)^(-1)=a b a b^(-1) a^(-1).

There is no embedding of F into any free group that sends all three marked
elements to positive words in one free basis. Indeed let A,B,C be the positive
images. Conjugacy gives equal abelianization for A and C, hence equal word
length. The positive-word equality `(AB)A=C(AB)` then has first |A| letters A
on the left and C on the right. Thus C=A. Cancelling the initial A gives BA=AB,
contradicting injectivity because a and b do not commute in F(a,b).

The coordinate presentation `<a,b,c | c=(ab)a(ab)^(-1)>` is free of rank two by
eliminating c, and all three marked elements have positive value under the
character a↦1,b↦1. They are individually primitive. Consequently neither
freeness of the coordinate group, individual primitivity, nor a common positive
character is enough for simultaneous positivity, even after embedding into a
larger free group. This is a proved obstruction to a proposed general lifting
method, not a C_delta counterexample. It may be absent from the special
closed-support configurations of R17; that is being checked separately.

`code/D_root_obstruction_checks.py` checks the finite presentation by exact word
reduction and enumerates all nonempty binary positive A,B of lengths at most
five. In every case the displayed conjugate is positive precisely when A and B
commute, as the general prefix argument proves without a finite bound.

## 8. Delooping a derived monoid colimit is a weaker target

Panov--Ray--Vogt, arXiv:math/0202081v1, was opened at Propositions
7.10--7.11, Theorem 7.12 with its proof, and Propositions 7.14--7.15
with their proofs. Theorem 7.12 identifies the based homotopy colimit
of classifying spaces with the classifying space of the homotopy
colimit of topological monoids. Its proof uses Fiedorowicz's free-
product theorem. Proposition 7.15 supplies the natural square with
ordinary colimits, but does not prove that the lower comparison is
an equivalence. Thus demanding contractibility of every component of
a proposed forest model for the derived monoid colimit may be a
stronger condition than the requested delooped comparison. The
source supplies no missing total-index theorem.

Queries actually run for this investigation:

- `"colimits" "free monoids" "aspherical"`
- `"quasi-filtered" monoids`
- `"totally aspherical" monoids colimits`
- `"free monoids" "non-erasing" pullbacks homotopy`
- `Panov Ray Vogt Colimits Stanley Reisner Algebras Loop Spaces arxiv`

Several hits use "totally aspherical" for a different test-category
condition involving a diagonal. None of those statements was silently
substituted for Chapter XII's all-action definition.

An uncompleted alternative is the generic subdivision factorization
of a free-monoid homomorphism: replace each occurrence in each image
word by a fresh letter, then map the fresh letters to target letters.
The first map has planar forest geometry, and the second is a basis
map. A proof using this factorization would have to construct it
functorially over all chains and control the identifications of new
intermediate vertices by cut-set actions. Individual factorizations
do not by themselves give a strict diagram or the desired comparison.

## 9. Audits of the subsequent reductions

The complete note `D_free_limit_criterion.md` was read by the root
thread. Its product-compatible injectivization and saturation proof
uses the two separate set colimits of M and M squared to identify
the monoid presentations; it does not assume siftedness. The free-
limit criterion and first-return corollary therefore transfer the
canonical comparison in the required direction. They exclude a
family of proposed counterexamples, while leaving general C_delta
diagrams open.

The complete local-free-hull argument in `D_Cdelta_attempts_G.md`
was also read. The distinction between arbitrary submonoids and
intersections of free submonoids is essential: the latter are free
by the stability argument given there. The minimal-rank choice
uses the defect theorem to make a finite free chart inject into the
filtered limit. The resulting replacement is finite free and has
injective monoid transitions; no injectivity of its group-completion
maps is asserted. The finite-support exhaustion uses the finiteness
of C_delta embedding sets and the absence of cancellation in positive
words. This is a substantive reduction of the remaining case, not a
proof of its comparison.

## 10. Structural routes and exact subsequent searches

The root thread independently read the orbitwise signed-lexicographic
cut-order argument in `CD_invariant_cut_orders.md`. The four-region
three-alternative table proves the finite decisive-set intersection
claim. A finite sequence of independently amalgamated nearby copies,
with the leading coordinate monotone, extends the comparison to
arbitrary copies; closure rigidity gives the recursion. The argument
has not yet been turned into a comparison of monoid coinvariants.
The cross-orbit extension is being developed separately and is not
assumed by this audit paragraph.

The intrinsic prefix-tree route remains incomplete. A real positive
length can give strict graph substitutions by unit-speed traversal,
but increasingly fine subdivisions may be dense and a metric quotient
may identify distinct branches. No faithful equivariant real-tree
model follows just from local freeness. A formal ordered length or a
proved cut-space replacement is still required.

The finite-word forest route likewise remains incomplete. Condition I
amalgamates expansions with a common root, but the subcategory of
uniform-stage words is not automatically cofinal: even a basis-map
diagram over Delta_inj distinguishes repetition patterns in the
underlying set colimit that its monoid colimit identifies. Thus a
reduction of mixed-stage words to the action of whole words would
silently assume the very compatibility that needs proof.

Additional queries actually run:

- `"locally free" "monoids" "tree"`
- `"locally free" "monoid" automorphisms`
- `"equidivisible" "homotopy"`
- `"free monoids" "colimit" "homotopy" total`
- `"locally free monoid"`
- `"direct limits" "free monoids"`
- `"free monoids" "aspherical"`
- `"polynomial monads" "homotopy colimits" "Batanin" "De Leger"`
- `"cartesian monad" "exact" "colimits" homotopy`
- `"monoids" "totally aspherical" category`

Only the primary sources separately recorded as opened were used in
the mathematical arguments. Search snippets and unrelated uses of
"locally free" or "totally aspherical" supply no theorem dependency.
