# Perfect locally free groups and Higman completeness

## Proved statement and source scope

Every homomorphism from a Higman-complete group to a perfect locally free group is trivial. In particular, a perfect locally free Higman-complete group is trivial. No cardinality assumption is used.

The only non-elementary input is the free-group stable commutator length gap: for a nonidentity element `g` of the commutator subgroup of a free group `F`, `scl_F(g) >= 1/2`. This is the consequence of Duncan–Howie, Theorem 3.3, in *The genus problem for one-relator products of locally indicable groups*, Math. Z. 208 (1991), 225–237, DOI <https://doi.org/10.1007/BF02571522>. The original journal metadata was verified at <https://researchportal.hw.ac.uk/en/publications/the-genus-problem-for-one-relator-products-of-locally-indicable-g/>. A full proof of the exact free-group consequence was read in Danny Calegari, *scl*, Theorem 4.111, printed pp. 131–133, primary author monograph available at <https://www.maths.ed.ac.uk/~v1ranick/papers/scl.pdf>. That proof identifies its dependence on Duncan–Howie pp. 229–233 and proves the numerical gap from a reduced surface diagram, a right order on the torsion-free one-relator quotient, and the resulting cusp count. The original 1991 article itself was not downloaded; the full proof checked is Calegari's stated adaptation.

The definition of Higman-complete used here is the one in Corson, *On homomorphic images of ultraproducts*, arXiv:2503.09228v2, Definition 8: every sequence of equations `x_n=w_n(a_n,x_(n+1))`, with one specified coefficient per equation, has a simultaneous solution. The special words below fall exactly within this definition. Official primary PDF: <https://arxiv.org/pdf/2503.09228>.

## The gap passes to locally free groups

Let `P` be perfect and locally free, and let `g != 1` belong to `P`. For every positive integer `m`, choose a shortest expression

`g^m = product_(j=1)^r [u_j,v_j]`, where `r=cl_P(g^m)`.

The subgroup `F=<g,u_1,v_1,...,u_r,v_r>` is a finitely generated free group. Since `g^m` belongs to `[F,F]` and `F_ab` is torsion-free, the element `g` itself belongs to `[F,F]`. The gap theorem gives `scl_F(g)>=1/2`. Consequently

`cl_P(g^m)=r >= cl_F(g^m) >= m scl_F(g) >= m/2`.

Taking the infimum after dividing by `m` proves `scl_P(g)>=1/2`. Perfectness guarantees that all the commutator lengths in this argument are finite.

## An explicit integral length

Stable commutator length satisfies homogeneity `scl(g^m)=|m| scl(g)`, invariance under inverses, and

`scl(gh) <= scl(g)+scl(h)+1/2`.

For completeness, the last bound has an explicit surface proof. Map a pair of pants to `BP` with boundary classes `g`, `h`, `(gh)^(-1)`. For every odd positive integer `m`, the cyclic cover classified by sending the first two boundary loops to `1 in Z/m` is connected and has one boundary component above each original boundary: the third monodromy is `-2`, which also generates `Z/m`. Its Euler characteristic is `-m`, so its genus is `(m-1)/2`. Cap the first two boundary components by surfaces expressing `g^m` and `h^m` as products of commutators. The resulting surface bounds `(gh)^m` and proves

`cl((gh)^m) <= cl(g^m)+cl(h^m)+(m-1)/2`.

Dividing by `m` and taking the odd subsequence gives the bound. The ordinary subadditivity of commutator length ensures that the limit defining `scl` exists and equals its infimum, so the subsequence has the same limit.

Define

`ell(1)=0`, and `ell(g)=ceil(2 scl_P(g))+1` for `g != 1`.

This is a finite nonnegative integer. It satisfies `ell(g^(-1))=ell(g)`, and is positive away from the identity. If `g`, `h`, and `gh` are all nonidentity, the displayed inequality and `ceil(a+b)<=ceil(a)+ceil(b)` give

`ell(gh) <= ceil(2scl(g)+2scl(h)+1)+1 <= ell(g)+ell(h)`.

The cases containing an identity, or `gh=1`, are immediate. Finally, for `g != 1` and `m>=1`, the gap and homogeneity give

`ell(g^m)=ceil(2m scl(g))+1 >= max(m+1,ell(g))`.

In particular powers of nonidentity elements remain nonidentity. This is a Dudley length, with an explicit formula.

## A fixed recurrence that cannot be solved

Let `a != 1` belong to any group equipped with a length satisfying the preceding inequalities, and put `A=ell(a)`. Consider the single-coefficient recurrence

`x_n = a x_(n+1)^((n+2)^2)`, for `n=0,1,2,...`.

Every finite prefix has a solution: choose the final variable arbitrarily, then evaluate backwards. Nevertheless the full system has no solution.

Indeed, choose `N` so large that `(n+2)^2>A` for every `n>=N`. If `x_n=1` for some `n>=N`, the recurrence says `x_(n+1)^((n+2)^2)=a^(-1)`. The next variable cannot be the identity because `a != 1`, and the power lower bound then gives

`A=ell(a^(-1)) >= (n+2)^2+1 > A`,

a contradiction. Therefore all `x_n` with `n>=N` are nonidentity. The triangle inequality also gives, for each such `n`,

`ell(x_n) >= ell(x_(n+1)^((n+2)^2))-A >= ell(x_(n+1))-A`,

and independently

`ell(x_n) >= (n+2)^2+1-A`.

For any `n>=N`, iterate the first inequality from `N` to `n`, then use the second:

`ell(x_N) >= ell(x_n)-(n-N)A >= (n+2)^2+1-(n-N+1)A`.

The right side tends to infinity. This contradicts finiteness of `ell(x_N)`.

Thus the same exponent sequence `(n+2)^2`, independent of the target length or the coefficient, obstructs every nonidentity `a` in every perfect locally free target.

## The homomorphism conclusion with exact maps

Let `f:C->P` be a homomorphism, where `C` is Higman-complete and `P` is perfect and locally free. If `f(c)=a != 1`, Higman completeness supplies elements `y_n in C` satisfying

`y_n=c y_(n+1)^((n+2)^2)`.

Applying `f` gives a prohibited recurrence in `P`, with `x_n=f(y_n)`. Therefore `f(c)=1` for every `c`, proving that `f` is the trivial homomorphism.

## Exact limitation for the main problem

This result excludes perfect locally free Higman-complete targets, at every cardinality. It also proves that no Higman-complete group can have a nontrivial perfect locally free quotient. It does not exclude countable Higman-complete groups outside the locally free class: research/D_Higman_completion.md constructs a countably infinite perfect example explicitly. It does not produce a countable detecting quotient for an arbitrary uncountable perfect locally free source.

The recurrence has relative ordinary boundary `e_n-(n+2)^2 e_(n+1)`. Its cokernel is the nonzero direct limit of infinite cyclic groups under the indicated multiplications; it is not a relative boundary isomorphism. Thus this obstruction has not been transferred to the nonsingular boundary-isomorphism systems of A.19.
