# Irrational stabilization of positive matrix diagrams

Working note, GPT-6 Astra, 17 November 2026. The lemmas in Sections 1–3 are proved below. They concern free **commutative** monoids / nonnegative matrices. They do not claim a strict free noncommutative monoid lift or settle the remaining C_delta comparison.

## 1. A unimodular cone with an irrational axis

Let

\[
 T=\begin{pmatrix}1&1\\1&2\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z),
 \quad\varphi=(1+\sqrt5)/2,
 \quad\lambda=\varphi^2,
 \quad v=(1,\varphi)^t.
\]

The matrix is symmetric, with eigenvalues `lambda>1` and `lambda^{-1}<1`, and both its Perron vector `v` and left eigenfunctional `ell=v^t` have positive coordinates. Extend `v` by zero and `ell` by zero on the last r coordinates of `L_r=Z^2⊕Z^r`.

**Lemma 1 (proved).** For every finite r there is a unimodular basis `B_r` of `L_r` for which every coordinate of `v` is strictly positive and `ell` is strictly positive on every basis element.

**Proof.** Initially use `b_1=e_1,b_2=e_2`, with active coordinates `c_1=1,c_2=varphi`. Suppose a basis has already been constructed for `L_s`, every coordinate of `v` is positive, and `ell` is positive on every basis element. Its two distinguished active coordinates remain integer combinations of `1,varphi` with a unimodular coefficient matrix. In particular they are positive and unequal. Let `i,j` be the active indices with `c_i<c_j`, and adjoin the next standard free generator `f`, on which `ell(f)=0`. Replace and append basis elements by

\[
 b_i'=b_i-f,\qquad b_j'=b_j,\qquad b_{new}=f+b_j.
\]

All other basis elements are unchanged. This is an integral basis: recover `f=b_new−b_j`, and then `b_i=b_i'+b_new−b_j`. Its determinant is one up to the chosen ordering. The old contribution `c_i b_i+c_j b_j` becomes

\[
 c_i b_i'+(c_j-c_i)b_j+c_i b_{new}.
\]

Thus all new coordinates remain positive. The values of `ell` on the changed basis elements are respectively `ell(b_i)`, `ell(b_j)`, and `ell(b_j)`, also positive. Keep the original two indices as the active pair. Their coefficient update is one subtractive Euclidean step. Integer independence of `1,varphi` prevents equality or zero at any finite stage, so the construction continues for every finite r. This proves the lemma. ∎

This is precisely where a rational primitive axis can fail: the subtractive algorithm then eventually reaches zero or equal active coordinates. An irrational rank-two axis avoids that obstruction while every basis change remains integral and unimodular. No rational rounding or congruence argument is needed.

## 2. Functorial positive stabilization over a locally finite direct category

Call a small category A *finite below in degree* here if it has a degree into N, every nonidentity arrow strictly raises degree, and every object has only finitely many incoming nonidentity arrows. The last hypothesis can be weakened to finiteness of the finite collection of maps actually needing domination at each step; the stated form suffices for C_delta on a skeleton.

**Lemma 2 (proved).** Let A be finite below in degree, and let `F:A→Ab` be a diagram of finite-rank free abelian groups. Then there is a diagram `H:A→Ab` with chosen finite bases such that:

- every nonidentity transition matrix of H is strictly positive integral;
- `H` is naturally isomorphic to `F⊕constant(Z^2)`;
- if every transition of F is an injective primitive embedding, the same is true of H.

In particular H is the group completion of a strict diagram of finite free commutative monoids.

**Proof.** Choose any integral basis of each F(X), put `r_X=rank F(X)`, and form `L_X=Z^2⊕F(X)`. Apply Lemma 1 to get a basis matrix `B_X` of `L_X`. Use the same `T,v,ell,lambda` in its auxiliary rank-two summand.

For a fixed map `f:X→Y` and an integer n, consider

\[
 A_f(n)=B_Y^{-1}
       \begin{pmatrix}T^n&0\\0&F(f)\end{pmatrix}B_X.
\]

As `n→∞`,

\[
 \lambda^{-n}A_f(n)\longrightarrow
 \frac{(B_Y^{-1}v_Y)(\ell_X B_X)}{\ell(v)}.
\]

Every entry of the limiting outer-product matrix is strictly positive by Lemma 1. Consequently there is an integer threshold `k_f` such that every entry of `A_f(n)` is strictly positive for every `n≥k_f`. This is an actual eventual statement, not a test at selected exponents. Integrality follows from `B_X,B_Y,T` being unimodular and `F(f)` integral.

Choose integers `N_X` by increasing degree so that

\[
 N_Y-N_X\geq k_f\quad\text{for every nonidentity }f:X\to Y.
\]

There are only finitely many constraints when choosing `N_Y`; one may also impose `N_Y>N_X`. Define

\[
 H(f)=B_Y^{-1}
       \begin{pmatrix}T^{N_Y-N_X}&0\\0&F(f)\end{pmatrix}B_X.
\]

These matrices compose exactly because the exponents telescope and F is a functor. Identities give identity matrices. Hence H is a strict positive-matrix diagram. Before changing bases it is the direct sum of F with the auxiliary rank-two diagram whose maps are `T^{N_Y-N_X}`. The latter is naturally isomorphic to the constant diagram through `T^{-N_X}` at X; these inverse powers are integral because T is unimodular. This proves the claimed natural decomposition. The assertion about primitive embeddings follows by the same direct-sum and basis-change argument. Restricting nonnegative matrices to `N^{r_X+2}` gives the free-commutative-monoid diagram. ∎

### Application to C_delta

On the skeleton of C_delta, degree is the number of vertices. A nonidentity increasing embedding strictly raises this degree. Every target has only finitely many subsets and increasing embeddings from skeletal sources, so the finiteness condition holds. R17's Q has finite free values by the private-vertex integral elimination, and its transitions are primitive injections by the relative version of the same proof. Therefore Lemma 2 applies to Q.

**Corollary 3 (proved).** There is a strict diagram H of finite free abelian groups over the total category C_delta, with strictly positive integer matrices on every nonidentity arrow and primitive injective transitions, for which

\[
 T_1^{\mathcal C_\delta}(H)=\mathbb Z.
\]

Indeed `H≅Q⊕Z^2`, R17 gives `T_1Q=Z`, and totality makes the constant rank-two summand acyclic in positive degrees. Thus totality does **not** annihilate higher derived colimits merely because all transition matrices are nonnegative, even with injective primitive maps. Any prospective theorem for abelianizations of free noncommutative monoid diagrams must use their coherent word substitutions and not only matrix positivity.

The conclusion is not that this H is the abelianization of a strict FreeMon diagram. Constructing that lift is a separate problem.

## 3. Why strict word lifts are additional data

Even a finite direct category can have a positive-matrix diagram without a compatible free-monoid lift in the specified bases. Let its nonidentity generators be

`f:0→1`, `g,h:1→2`, with the relation `gf=hf`.

Put ranks `1,2,2`, let `f(1)=(1,1)`, let g be the identity matrix, and let h interchange the two coordinates. The matrix relation holds. In a free-monoid lift, g and h are forced to preserve and interchange the two letters, respectively, whereas f must send its generator to either `ab` or `ba`. Neither word is fixed by interchanging its letters. Thus no lift exists.

This example even has a lift to free groups by free-factor inclusions. Send f's generator to `ab`, let g be the identity map, and set

\[
 h(a)=aba^{-1},\qquad h(b)=a.
\]

Then `h(ab)=ab`, h is an automorphism, and its abelianization is the coordinate transposition. Hence the existence of a free-group lift does not by itself solve the positive-word coherence problem. The example is a logical obstruction to a general lifting inference, not a counterexample over C_delta.

The independently run program `code/D_positive_checks.py` exhausts both possible positive words with Parikh vector `(1,1)`, checks their two composites, and verifies the displayed free-group lift and its inverse by exact word reduction. Its output is `code/outputs/D_positive_checks.json`. It also verifies the exact Nielsen-basis identities in the next section. These are exhaustive checks for this finite example; they do not claim a finite search establishes a universal C_delta assertion.

## 4. An exact nonabelian lift of the first stabilization step

There is nevertheless a useful elementary positive substitution behind the first cone splitting. On the free group with basis a,b,g, define

\[
 \tau(a)=ba,\qquad\tau(b)=bab,\qquad\tau(g)=g.
\]

The first two images form a free basis, and the abelianized matrix on a,b is T. In the new free basis

\[
 x=ag^{-1},\qquad y=b,\qquad z=gb,
\]

the same automorphism is the positive substitution

\[
 x\mapsto yx,\qquad y\mapsto yxz,\qquad z\mapsto zxz.
\]

These identities are exact in the free group and the basis change is integral at the abelianized level. This realizes Lemma 1's first step without losing word order. It does **not** yet provide compatible further splittings or a positive realization of arbitrary transition maps `G(f)`. In particular, positivity of the Perron coordinates alone does not eliminate negative letters inside arbitrary words in the fixed free factor.

## 5. Literature queries and current boundary

Searches on 17 November 2026:

- `"positive matrices" "derived colimits"`
- `"free monoids" "total" "colimits" homology`
- `"eventually positive" "integer" "conjugate" matrix Perron basis`
- `"free group" "positive basis" stabilization automorphism`
- `free group finite set simultaneously positive basis stably positive automorphism`
- `"free group" "potentially positive"`
- `"positive automorphism" "free factor" fixed subgroup primitive`
- `"Handelman" "non-commensurability" eigenvectors positive`

The search located David Handelman's *Eventually positive matrices with rational eigenvectors*, whose publisher abstract describes earlier integer-conjugacy results under noncommensurability assumptions and extends them to a rational-eigenvector setting. Our elementary rank-two proof above is self-contained and no particular theorem from an unopened full text is used. It also located the Miasnikov–Shpilrain problem list F34 on potential and stable potential positivity in free groups, and Siobhan O'Connor's dissertation *Algorithmic Problems in Automorphic Orbits of Free Groups*. These identify the genuine additional free-group positivity issue; they are not invoked as a solution to the present diagram problem.

As of this note, the strict FreeMon realization of Q (or its positive stabilization) and the universal FreeMon passage theorem for C_delta remain unresolved. Even a realization with nonzero `T_1` would still require a computation of the monoid-colimit target before concluding failure of the comparison map.
