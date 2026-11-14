# Audit of nonsingular equation solvability and the fixed target

## Source and exact statement

The primary source is OpenAI, *Nonsingular systems of equations over arbitrary groups*, dated 5 October 2026, 16 pages. The official source was downloaded and the complete PDF was read, twice for the operator and planar arguments.

- Official PDF: <https://github.com/openai/math/blob/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf>.
- Raw official PDF: <https://raw.githubusercontent.com/openai/math/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf>.
- Local copy: `D_nonsingular_2026.pdf`; extracted text: `D_nonsingular_2026.txt`.
- Downloaded file: 383280 bytes; SHA-256 `732c93a33db2c8c7da84a2bc8505ac9e00f7fe345731cf9a4bfe00b82c17cea2`.
- Status: a newly released preprint. The full multirelator theorem is proved in the PDF; the companion one-relator formalization is not being represented as a formalization of this theorem.

Theorem 1 states: for any group `G` and words `w_1,...,w_m` in `G*F(x_1,...,x_n)`, independence over `Q` of the `m` variable-exponent rows implies injectivity of the canonical map

`G -> (G*F(x_1,...,x_n))/<<w_1,...,w_m>>`.

There is no torsion, cardinality, finiteness, or hyperlinearity assumption on `G`. The quotient is the actual solution overgroup; the injection is the canonical coefficient map. Remark 5.1 establishes the same conclusion for arbitrary sets of finite words with linearly independent exponent rows: a kernel witness uses only finitely many relators and variables, to which Theorem 1 applies.

**Audit conclusion.** The complete proof checks. The multiblock unitary theorem was additionally audited independently by the Part C agent. The root agent also read the full primary paper and independently confirmed the trace and planar arguments. The details below record the mathematical checks, rather than treating the theorem's announcement as its proof.

## 1. Simultaneous unitary fixed spaces, pages 3–7

For positive block sizes `k_i`, signed occurrence matrix `B` of full row rank, and maps

`F_j((X_i)) = diag(X_i^s) P_j`,

the theorem produces matrices whose total fixed-space dimension is at least `sum_i k_i`.

1. Sort `k_1>=...>=k_r`. Independent first `t` rows allow columns `j_1,...,j_t` with every leading `t`-minor nonzero: extend the previous independent columns by one. Set `l_(j_t)=k_t`, other `l_j=0`. Every selected column contains some nonzero entry among its first `t` rows, so its total block size is at least `k_t`. Hence all incidence spaces exist. Both `sum l_j=sum k_i` and `sum l_j^2=sum k_i^2` hold exactly.
2. In the fibration `U(d-1)->U(d)->S^(2d-1)`, the rational Serre spectral sequence has only columns `0` and `2d-1`. Its only possible differential vanishes on every exterior generator by degree, and therefore on every product by the derivation rule. This gives compatible generators `e_a` of degree `2a-1`. For primitivity, the difference between multiplication pullback and the two factor classes has positive degree in both factors. Both bidegrees are at most `2d-2`, where restriction to `U(d-1)` is injective. Its restriction vanishes by induction, including the new sphere class whose restriction to the fiber is zero. Thus the generators are primitive. Inversion changes their signs; conjugate coordinate inclusions have the same pullback because inner conjugation in a connected group is homotopic to the identity.
3. The incidence manifold of pairs `(W,L)` with an `l`-plane `L` fixed pointwise by `W in U(d)` is a compact oriented bundle with fiber `U(d-l)` over `Gr_l(C^d)`. Its real codimension in the target is `l^2`. The Poincare dual of its pushed fundamental class has leading exterior term `c e_1...e_l`, where `c` is nonzero. Degree alone makes this the only term with `l` factors and excludes longer terms.
4. To determine that coefficient, intersect with `X -> X direct-sum (-I)` on `U(l)`. There is exactly one incidence pair: `X=I`, with fixed plane the first summand. At that pair, variations of `X`, of the complementary unitary, and of the plane span respectively the upper diagonal, lower diagonal, and off-diagonal skew-Hermitian blocks. For the last part the derivative is `2T`, so the intersection is transverse with multiplicity `+1` or `-1`. This proves the required nonzero coefficient, including the edge cases `l=0,d`.
5. Pullback of each primitive class is `sum_i b_ij e_a^(i)`, with only `k_i>=a` included. In total top degree on `product_i U(k_i)`, a nonzero exterior monomial must use every generator. Thus all shorter terms of the incidence classes vanish in the product. Grouping the remaining terms by degree yields, at each threshold `a`, exactly the nonzero minor with the rows `k_i>=a` and the correspondingly selected columns. Their product is nonzero. Nonzero intersection number forces an actual common incidence point, giving the simultaneous fixed spaces.

No integral cohomology assertion or embeddedness of the incidence image is used. Poincare duality applies to the pushed fundamental homology class; the incidence parameter manifold supplies the intersection calculation.

## 2. Trace and phase, pages 7–10

Let `M` be the commutant of the right translations on `ell^2(G)`. The identity-coordinate vector functional, summed over finitely many matrix coordinates, is a faithful normal trace even when `G` is uncountable. The check uses countable support of each square-summable vector, Cauchy–Schwarz for the convolution sums, and right translates of the identity vector to prove faithfulness. No countable basis or approximation by finite matrices is assumed.

Use the nonnegative fractional-angle function `h` with `h(1)=0`, and define `ell(V)=tau(h(V))`. Faithfulness gives `ell(V)=0` exactly when `V=I`.

The subadditivity proof is valid in this algebra. For `D=h(V)` and `W_u=U exp(2 pi i u D)`, cyclicity of the trace first proves

`d/du tau(f(W_u)) = tau(f'(W_u) D)`

for Laurent polynomials. Absolute summability of the Fourier series and its differentiated series gives the formula for smooth `f`. When `f'<=1`, positivity of

`D^(1/2) (I-f'(W_u)) D^(1/2)`

bounds the derivative by `tau(D)` without requiring commutation. The fractional-angle function is smoothed from the positive-angle side. Those smooth functions have derivative at most one and converge at every point, including the cut at `1`; bounded convergence for the finite spectral measure gives `ell(UV)<=ell(U)+ell(V)`. The direction of smoothing is essential and is correctly implemented.

For a weighted cyclic shift on `a` coordinates, scalar conjugacy by successive `a`th roots of unity makes all root rotations have the same phase trace. Summing their scalar fractional angles and then applying functional calculus gives

`ell(T)=(a-1)/2 + tau(h(C))`,

where `C` is the ordered product of the weights around the cycle. All diagonal entries of `T^a` are conjugate to `C`; this accounts for the normalization exactly.

## 3. Planar boundary obstruction, pages 10–13

Take a connected genus-zero surface of signed relator disks and bands pairing equal variables with opposite traversal signs. Row independence forces positive and negative multiplicities to be equal separately for each relator type. Write these multiplicities as `k_i`, and set `K=sum k_i`, `b=sum N_i k_i`, where `N_i` is the variable-word length. There are `2K` disks, `b` bands, and `2b` slots. For `q` boundary circles, Euler characteristic gives `2-q=2K-b`.

Let `sigma` advance around disks and `theta` pair band ends. Boundary components are the cycles of `sigma theta`; their total lengths sum to `2b`. The graph on these cycles induced by the pairs of `theta` is connected, because `<sigma theta,theta>=<sigma,theta>` is transitive on slots. Therefore any real boundary phases summing to zero can be distributed as slot phases with opposite values at paired ends, using a spanning tree. Loops in the graph cause no problem.

The operator `S` advances around disk slots with inverse coefficient weights; `Theta` crosses bands with their scalar phases and is an involution. A scalar involution `J` mixes positive and negative copies of each relator type using a unitary `X_i`. The opposite corner conventions give `JSJ=S^-1` exactly. Consequently `SJ` is an involution that exchanges the two disk signs, has zero trace, and has phase trace `b/2`.

On coordinates grouped by variable and positive traversal, `JTheta` is a block-unitary map with signed multiplicity matrix `-A`. The fixed-space theorem applies without alteration to the independent rows present in the surface, producing at least `K` fixed directions there. Conjugation by `J` exchanges traversal signs and takes `JTheta` to its inverse, so the full scalar fixed-space dimension is at least `2K`. Inverse pairing of its nonidentity eigenvalues then gives

`ell(JTheta)<=b-K` and `ell(STheta)<=3b/2-K`.

The weighted-cycle formula expresses this same phase trace as a sum over boundary words. Assign phase `-epsilon` to every known trivial boundary and `(q-1)epsilon` to the possibly nontrivial one. The former contribute `1-epsilon`; the latter approaches its unrotated phase from the continuous side of the cut. The cycle-length sum and Euler identity make the limiting constant precisely `3b/2-K`. The upper bound therefore forces the remaining nonnegative phase to vanish. Faithfulness gives that the remaining boundary word is the identity in the original coefficient group.

The argument includes `q=1`: its exceptional scalar phase is then exactly zero. The auxiliary choice of `J` can depend on the phase distribution; the phase bound holds separately for every choice and is all that is needed for the limit.

## 4. Extracting the planar surfaces, pages 13–15

A finite normal-closure expression for a coefficient-group element gives a map from a disk with finitely many holes to the wedge of a presentation space for the coefficient group and the variable circles. Cut arcs labelled by the conjugators give the stated boundary word with the correct inverse orientations; the expression makes it nullhomotopic, so the map exists.

Project to each variable circle and approximate those circle maps by finite piecewise affine maps, fixed on the boundary. Their common uniform error is less than `1/12`. Choose regular levels between `1/3` and `2/3`. Each level is a finite union of disjoint embedded circles and proper arcs; the boundary traversals supply exactly one endpoint per variable occurrence. At such a level the original circle projection is more than `1/4` away from the wedge point, so the original wedge-valued map lies in that particular variable circle. Every other circle projection and the coefficient projection are then constant in a neighborhood. Consequently levels of different variables are disjoint, and thin band neighborhoods of the proper arcs have exactly constant coefficient projection. Discarding the closed level curves removes no slot endpoint.

The induced endpoint signs are opposite by coorientation. Shrinking the variable slots leaves their coefficient labels unchanged. Filling the original holes with signed word disks therefore makes an embedded, possibly disconnected and nested planar disk-band surface of exactly the kind already treated.

Choose a component with minimal exterior Jordan disk. Its interior complementary disks contain no other component and hence no missing word disk, so their coefficient loops already bound. The planar obstruction makes its exterior loop bound as well. Fill it in the coefficient space, preserving the exact boundary loop, and continue outward. A finite number of repetitions fills the original outer loop. This proves coefficient injectivity.

## 5. Explicit fixed target of cardinal at most the continuum

This consequence was obtained independently during the investigation and is used in the Part A dimension obstruction. The reduced-power implementation was proposed by the Part C agent and audited here.

Start with a countable group `H`. Build a countable overgroup `E` solving every finite nonsingular system over itself. At each pass enumerate all finite nonsingular systems with coefficients in the preceding countable stage; there are countably many. Adjoin their solution quotients in that order. The coefficient maps are injective by Theorem 1, so each stage embeds in the next. Repeat for countably many passes. Each system over the final union has only finitely many coefficients and hence was solved in one of the passes. The original `H` embeds in `E` by the actual composite coefficient maps.

Define

`U = E^N / E^(N)`,

where `E^(N)` consists of sequences equal to the identity except at finitely many coordinates. This is a normal subgroup of the product, and the diagonal map `E -> U` is injective: a nonidentity constant sequence never has finite support. There are at most `2^aleph_0` elements in `U`.

Every countable row-independent equation system over `U` has a solution in this same `U`. Choose a sequence representative for each of its countably many coefficients. At coordinate `n`, substitute the coefficient coordinates into the first `n` equations and solve that finite nonsingular system in `E`. Only finitely many variables occur there; assign every unused variable the identity at that coordinate. Each variable now defines a sequence. The value of the `j`th equation is the identity at every coordinate `n>=j`, so it lies in `E^(N)` and becomes the identity in `U`. This proves simultaneous solvability of the full countable system.

It follows by the universal property of relative presentations that every transfinite tower starting at `H`, with countable row-independent relative systems at successor stages and colimits at limits, has a homomorphism to this fixed `U` restricting to the displayed injection of `H`. The target is fixed before the tower is considered. At a successor, substitute the existing homomorphism into the coefficients and use the just-proved solution property; at a limit, use the compatible colimit map. This describes the exact morphism used in the cardinal obstruction.

No assertion that `U` is countable is made. The reduced-power construction gives the bound `2^aleph_0`.

