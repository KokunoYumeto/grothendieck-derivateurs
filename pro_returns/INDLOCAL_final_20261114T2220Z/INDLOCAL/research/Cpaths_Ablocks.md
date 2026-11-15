# Countable blocks in an integral cellular isomorphism

The first results below are self-contained algebraic and cellular statements.
The final reduced-power lemma uses the explicitly stated finite-solution
property of its input group; the application using the verified nonsingular
theorem is proved in `sections/A_cardinal_obstruction.tex`, Claim A.19.

## Relative presentation filtration

Let \(Y\subset X\) be a connected one-vertex CW pair of dimension at
most two. Write \(S\) for the oriented one-cells of \(X-Y\), \(R\) for
its two-cells, and choose a finite word \(w_r\) in
\(\pi_1(Y)*F(S)\) for each attaching loop. Suppose the actual relative
cellular boundary
\[
 \delta:\mathbb Z^{(R)}\longrightarrow\mathbb Z^{(S)}
\]
is an isomorphism.

Then there is a continuous ordinal-indexed filtration
\[
 Y=X_0\subset X_1\subset\cdots\subset X_\tau=X
\]
by actual CW subcomplexes such that each successor pair
\((X_{\alpha+1},X_\alpha)\) has at most countably many cells and its
relative integral cellular boundary in degrees two and one is an
isomorphism. The presentation of \(\pi_1(X_{\alpha+1})\) over
\(\pi_1(X_\alpha)\) uses exactly the new generators and the old
attaching words read with coefficients in \(\pi_1(X_\alpha)\).
No injectivity of \(\pi_1(X_\alpha)\to\pi_1(X_{\alpha+1})\) is required
for this presentation or for the filtration assertion.

### Proof

For \(r\in R\), let \(W(r)\subset S\) be the full set of relative
one-cells whose interiors meet the attaching image of \(r\). Choose the word \(w_r\)
within that finite supporting subgraph. Thus \(W(r)\) contains all
letters occurring in \(w_r\), including letters with exponent sum
zero, and also any additional traversals of the actual attaching
map that disappear in the chosen word.
For \(s\in S\), let \(I(s)\subset R\) be the support of
\(\delta^{-1}(s)\). Both sets are finite.

Call a pair \((S',R')\) closed when
\[
 r\in R'\Longrightarrow W(r)\subset S',
 \qquad
 s\in S'\Longrightarrow I(s)\subset R'.
\]
The first condition says that the selected cells, together with \(Y\),
form an actual subcomplex. It also gives
\(\delta(\mathbb Z^{(R')})\subset\mathbb Z^{(S')}\).
The second gives the reverse containment under \(\delta^{-1}\).
The restrictions of \(\delta\) and \(\delta^{-1}\) are inverse
isomorphisms on the selected summands.

Starting with a closed pair, adding any countable set of cells and
then applying \(W\) and \(I\) alternately for countably many rounds
produces another closed pair differing from the first by at most
countably many cells. Only finite supports are added at each use
of \(W\) or \(I\). The union of any increasing chain of closed pairs
is closed.

Well-order \(S\amalg R\). Begin with the empty closed pair. At a
successor stage add the first cell not already present and close as
above. At limit stages take unions. This process exhausts all cells
at an ordinal of cardinality at most \(|S\amalg R|\), apart from the
trivial empty case. Let \(X_\alpha\) be the subcomplex selected by
the closed pair at stage \(\alpha\).

For closed pairs \((S_\alpha,R_\alpha)\subset
(S_{\alpha+1},R_{\alpha+1})\), the two isomorphisms
\(\delta\) and \(\delta^{-1}\) preserve both the older and the newer
summands. They consequently induce inverse isomorphisms
\[
 \mathbb Z^{(R_{\alpha+1}\setminus R_\alpha)}
 \ \longleftrightarrow\
 \mathbb Z^{(S_{\alpha+1}\setminus S_\alpha)}.
\]
The forward map is precisely the relative cellular boundary of
\((X_{\alpha+1},X_\alpha)\). This proves the assertion. Van Kampen
gives the displayed relative presentations, and its CW union form
identifies the group at each limit with the group colimit. \(\square\)

## Finite systems completed to unimodular systems

Let \(\delta:\mathbb Z^{(R)}\to\mathbb Z^{(S)}\) be an isomorphism,
with each basis column finitely supported. Fix a finite subset
\(R_f\subset R\), and a finite set \(S_f\subset S\) containing the
supports of its columns. The columns
\(\{\delta(r):r\in R_f\}\) can be completed to a basis of
\(\mathbb Z^{(S_f)}\).

### Proof

The subgroup \(P=\delta(\mathbb Z^{(R_f)})\) is a direct summand of
\(\mathbb Z^{(S)}\), since \(\delta\) is an isomorphism and
\(\mathbb Z^{(R_f)}\) is a coordinate summand. Its quotient is
isomorphic to the free abelian group \(\mathbb Z^{(R\setminus R_f)}\).
The inclusion
\[
 \mathbb Z^{(S_f)}/P
       \longrightarrow \mathbb Z^{(S)}/P
\]
is injective. Its target is free abelian, so its source is free
abelian; it is finitely generated because \(S_f\) is finite.
The exact sequence
\[
 0\longrightarrow P\longrightarrow\mathbb Z^{(S_f)}
       \longrightarrow\mathbb Z^{(S_f)}/P\longrightarrow0
\]
therefore splits. Choose lifts of a basis of the last group.
Together with the displayed basis of \(P\), these lifts form the
required basis. \(\square\)

Apply this to a finite family of actual relators in one countable
successor block of the preceding filtration. Let \(S_f\) contain
all letters in those relators, including zero-exponent letters.
The extra basis columns can be realized by finite words in these
same variables: after ordering \(S_f=\{s_1,\dots,s_m\}\), realize a
column \((a_1,\dots,a_m)\) by \(s_1^{a_1}\cdots s_m^{a_m}\).
Appending those words to the selected finite relators produces a
square exponent-sum matrix of determinant \(1\) or \(-1\).
The original finite system is literally a subsystem of this
completed finite system. This constructs the precise comparison
of systems; it asserts neither existence nor uniqueness of their
solutions.

## Obtaining the one-vertex relative problem from a homology sphere

Let \(X=BG\) be a connected two-dimensional classifying CW complex
with \(H_1(X;\mathbb Z)=0\) and countable \(H_2(X;\mathbb Z)\).
The proved countable-core construction in
\`Cpaths_A3_obstruction.md\` supplies a countable connected
aspherical subcomplex \(Y\subset X\), injective on fundamental
groups and inducing every ordinary integral homology isomorphism.

Choose a maximal tree in \(Y^{(1)}\) and extend it to a maximal
tree in \(X^{(1)}\). Collapse the latter tree. The quotient maps
on \(X\) and on \(Y\) are homotopy equivalences, and the image of
\(Y\) remains a countable connected subcomplex. The new pair is
one-vertex. Its relative cellular chain complex is concentrated
in degrees one and two, and its relative integral homology is
zero. Therefore its actual boundary \(\delta\) is an isomorphism.
The two preceding proved statements apply to this specified pair.

## Explicit reduced-power solution target

Let `E` be any group in which every finite system with rationally
independent exponent rows has a solution. Set
`U = E^N / E^(N)`, where `E^(N)` is the subgroup of finite-support
sequences. This subgroup is normal because coordinatewise conjugation
preserves support. The diagonal homomorphism `E -> U` is injective:
a nonidentity constant sequence never has finite support.

Every countable system over `U` with rationally independent exponent
rows has a simultaneous solution in `U`. Choose a representative
sequence in `E` for each of its countably many coefficients. At
coordinate `n`, solve the first `n` equations over `E` with these
coordinate coefficients, giving unused variables the value one.
These are finite nonsingular systems because all exponent entries
remain unchanged under coefficient specialization. For each variable,
take the sequence of chosen coordinate values. Equation `i` evaluates
to one at every coordinate `n >= i`; its value has finite support and
therefore becomes one in `U`. This constructs all solution elements
and verifies all equations. The argument also covers finite systems
by using all equations from some coordinate onward.

For infinite `nu` and `|E| <= nu`, this construction has
`|U| <= nu^(aleph_0)`. No compactness, elementary extension, or
saturation theorem is used.

Claim A.19 applies the verified finite nonsingular-system theorem to
construct such an `E` containing a prescribed group `H` of size at
most `nu`: at each of countably many passes, enumerate all at most
`nu` finite nonsingular systems over the old group and adjoin their
universal solution groups successively. The source theorem gives
injectivity at every adjoining step. Every finite coefficient set in
the final union occurred during one pass, so all the specified finite
systems have solutions there.

