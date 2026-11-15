# Countable targets and infinite recursive equations

## Checked source scope

Samuel M. Corson, *On homomorphic images of ultraproducts*, arXiv:2503.09228v2 (18 June 2025), primary PDF <https://arxiv.org/pdf/2503.09228>, was read through Section 2. Its Definition 8 calls a group Higman-complete when every system `h_i=w_i(f_i,h_(i+1))`, with one coefficient `f_i` per step, has a solution. Lemma 11 proves that reduced products and nonprincipal ultraproducts have this property by solving finite prefixes coordinatewise. Remark 9 proves preservation under epimorphisms. Proposition 10 and Theorem 17 classify the abelian case via cotorsion. They do not provide a countable envelope for an arbitrary prescribed nonabelian coefficient group.

The one-coefficient definition applies to the reverse commutator systems of A.21 by splitting the step into `y_i=[x_(i+1),a_i]`, `x_i=y_i b_i`. A word with several interlaced coefficients and repeated occurrences of the unknown has not been reduced here to such one-coefficient unary steps. No general reduction from an arbitrary countable relative boundary-isomorphism presentation to a Higman recurrence has been established.

George M. Bergman, *Homomorphisms on infinite direct products of groups, rings and monoids*, final author preprint <https://math.berkeley.edu/~gbergman/papers/prod_gp.pdf>, published Pacific Journal of Mathematics 274 (2015), 451–495, was checked in Sections 4–5. Lemma 11 supplies the countable nonabelian example `Q ⋊ {±1}` that is a retract of its ultrapowers. The elementary extension below gives a countably infinite perfect example, with its exact limitation for the current problem.

## A countably infinite perfect group solving all finitely consistent equation systems

Let `F=A_5` act on

`V={(q_1,...,q_5) in Q^5 : q_1+...+q_5=0}`

by permuting coordinates, and let `B=V ⋊ F`. This group is countably infinite and perfect.

To check perfectness directly, averaging a vector `v in V` over the transitive permutation action gives zero. Thus

`v = (1/|F|) sum_(s in F) (v-sv)`.

Each summand is a commutator contribution, by applying `s` to `v/|F|`. Hence `[V,F]=V`. Since `F` is perfect and is an actual subgroup of the semidirect product, both `V` and `F` lie in `[B,B]`, proving `[B,B]=B`.

For every ultrafilter `U` on every index set `I`, the ultrapower of the finite group `F` is canonically `F`: a finite partition of `I` has a unique cell in the ultrafilter. Therefore there is a canonical isomorphism

`B^I/U = (V^I/U) ⋊ F`.

The ultrapower vector space contains the diagonal copy of `V`. Extend a basis of that diagonal subspace to a basis of the whole `Q`-vector space, obtaining a linear retraction `p:V^I/U -> V`. Average it to

`p_F(w) = (1/|F|) sum_(s in F) s^(-1) p(sw)`.

This remains a retraction onto `V` and is `F`-equivariant. The formula

`(w,s) -> (p_F(w),s)`

is consequently a group homomorphism from the ultrapower to `B`, left inverse to the diagonal embedding.

Now take a countable system of equations with coefficients in `B`, every finite subsystem of which has a solution in `B`. At coordinate `n`, choose a solution to its first `n` equations. These coordinate values solve the full system in a nonprincipal ultrapower, since every particular equation holds eventually. Applying the displayed retraction gives a solution in `B`, with the original coefficients fixed. More generally the same proof works for any set of equations, using an ultrafilter on its finite subsets containing every set of supersets of a fixed finite subset. Thus this group has the full equation-compactness property, and in particular it is Higman-complete: every finite prefix of a reverse recursive system is solved by choosing its last variable freely and evaluating backwards.

This proves that countability and perfectness alone do not exclude Higman-completeness.

The example does not detect the coefficient groups needed for the hardest dimension problem. If `H` is perfect and all its homomorphisms to finite groups are trivial, then every homomorphism `H -> B` is trivial. Indeed its composite with the actual projection `B -> F` vanishes, so its image lies in the abelian normal subgroup `V`; perfectness then kills that image. In particular this construction supplies no embedding of a nontrivial such `H`.

## Exact fiber observation for torsion-free existentially closed targets

Let `w(t)` be a word over a group `Q` with total exponent zero in `t`, and suppose `w(c)=b` in `Q`. In `Q × Z`, every element `(c,k)` solves the same equation with the coefficients embedded diagonally as `(q,0)`: the second coordinate of the evaluated word is its exponent sum times `k`, hence zero. These solutions are distinct. If `Q` is torsion-free, the overgroup is torsion-free as well.

Consequently a group existentially closed among torsion-free groups has infinitely many solutions of each solvable zero-exponent one-variable equation: any finite list of excluded solutions is avoided in the displayed torsion-free overgroup, and the finite equation/inequation condition is realized back in the group. This is a proof of infinite fibers. It is not a proof that the word map has cofinite image, or that an inverse system of its fibers has a compatible infinite solution.

## Remaining exact obstruction

No countable Higman-complete overgroup containing a prescribed nontrivial perfect group with no finite images has been obtained. No theorem in the checked primary sources provides such an overgroup. The finite-prefix solution sets of a general reverse-word system form an inverse system; their nonemptiness, and even infinite individual word-map fibers, have not supplied a compatible infinite sequence in a fixed countable target. The reduced-power construction supplies such sequences in a target of continuum cardinality, while A.24 proves that some natural reduced powers have no smaller nontrivial quotients.

