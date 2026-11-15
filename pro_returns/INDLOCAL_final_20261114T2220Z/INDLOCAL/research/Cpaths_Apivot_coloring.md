# Independent exponent rows and a countable support coloring

Author: C/path collaborator, 2026-11-14.

This records the root collaborator's pivot argument after an independent
check. The conclusion is a coloring of the actual variable supports. No
group homomorphism is inferred from that coloring.

## Exact statement

Let `S` be a set of variables and `R` a set of finite words in
`H * F(S)`, for an arbitrary coefficient group `H`. For `r in R`, let
`W(r)` be the finite set of variables which actually occur in the chosen
word, including occurrences whose total exponent is zero. Let
`a_r in Q^(S)` be its exponent-sum vector. Suppose that the vectors
`(a_r)_(r in R)` are linearly independent over `Q`.

There is a coloring `c:S -> N` such that for every `r` with
`|W(r)| >= 2`, the restriction of `c` to `W(r)` is not constant.
More precisely, there is an injective assignment of pivot variables
`p:R -> S`, with `a_r(p(r)) != 0`, and the coloring may be chosen so
that

\[
 c(p(r))\ne c(s)\qquad
 (r\in R,\ s\in W(r)\setminus\{p(r)\}).
 \tag{1}
\]

All sets may have arbitrary cardinality. No local finiteness of the
incidence relation between words and variables is assumed.

## 1. An injective pivot assignment

Write `N(r)=supp(a_r)`, a nonempty finite subset of `W(r)`. For a
finite subset `T` of `R`, the independent vectors `(a_r)_(r in T)`
belong to the vector space with basis `union_(r in T) N(r)`. Therefore

\[
 \left|\bigcup_{r\in T}N(r)\right|\ge |T|.
 \tag{2}
\]

Finite Hall matching gives distinct representatives in `N(r)` for
every finite family. To pass to the whole family, form the product
`P=product_(r in R) N(r)`, with each finite factor discrete. For each
pair of distinct indices `r,t`, impose the closed condition that the
two chosen representatives differ. Every finite collection of these
conditions involves only finitely many indices and is satisfiable by
the finite matching just proved. Compactness of the product gives a
point satisfying all the conditions. Its coordinates define the
required injection `p`.

## 2. A graph with finite outdegree

For each `r`, draw a directed edge from `p(r)` to each element of
`W(r) \ {p(r)}`. Forget multiple edges and their directions to obtain
a simple undirected graph `Gamma` on `S`. Retain the directed
description for counting.

Because `p` is injective, a variable is the pivot of at most one word.
Consequently its number `d(s)` of outgoing neighbors is finite.
There is no bound on the number of incoming neighbors. Partition

\[
 S=\coprod_{n\ge0} S_n,
 \qquad S_n=\{s:d(s)=n\}.
 \tag{3}
\]

If `V` is a finite subset of `S_n`, each edge of the graph induced
on `V` is witnessed by an outgoing edge whose tail lies in `V`.
It follows that

\[
 |E(\Gamma[V])|\le n|V|.
 \tag{4}
\]

The same estimate holds for every subset of `V`. Thus every nonempty
induced subgraph of `Gamma[V]` has a vertex of degree at most `2n`,
by its average degree. Repeatedly remove such a vertex and then
color in the reverse order. This constructs a proper coloring of
`Gamma[V]` using `2n+1` colors.

Apply the same finite-product compactness argument to the assignments
`S_n -> {0,...,2n}` and the closed conditions that endpoints of an
edge have distinct colors. Every finite set of conditions is
satisfied by the preceding finite graph argument. We obtain a
proper coloring `c_n` of the entire induced graph on `S_n`.

Use disjoint palettes for the different classes:

\[
 c(s)=(n,c_n(s))\quad(s\in S_n).
 \tag{5}
\]

The union of these finite palettes is countable, so choose a
bijection with a subset of `N`. Edges within `S_n` have different
colors by construction; edges between different classes have
different first coordinates. Hence (5) properly colors all of
`Gamma`. Each edge from a pivot to another variable of its full
word support gives (1), proving the statement.

## 3. The exact limit of this conclusion

The result prevents a proof that every countable assignment of
colors makes an entire word support monochromatic: (1) is a
specified counter-assignment for every system with independent
exponent rows. It includes variables with zero total exponent,
because the graph uses `W(r)`, rather than only `N(r)`.

It does not supply solutions of the word equations. For an explicit
check, take the single word `r=xy^(-1)`. Its exponent vector is
nonzero, and a coloring satisfying (1) assigns different colors
`i,j` to `x,y`. The induced homomorphism
`F(x,y) -> F(t_0,t_1,...)` sends the relator to
`t_i t_j^(-1)`, a nonempty freely reduced word. Thus this particular
map does not factor through the quotient by `r`. A solution target
and the actual factorization have to be constructed separately.

The argument above is self-contained apart from finite Hall
matching and compactness of products of finite discrete spaces;
the applications of both were specified explicitly. Its independent
audit checks the finite neighbor inequality, the infinite matching,
the finite-outdegree count, the color bound, and the use of full
word supports.
