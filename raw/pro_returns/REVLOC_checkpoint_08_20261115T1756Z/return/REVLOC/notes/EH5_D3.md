# D.3: finite chromatic joins and remaining candidates

## Proved finite-join obstruction (15 November 2026, 12:14 UTC)

The following proof has been checked against the opened primary statements. The axioms agent independently checked its formal nullification and cofiber steps. Root can integrate the LaTeX below as D.3.3 (or renumber it).

```latex
\begin{claim}{D.3.3}{Proved}{Every nonzero finite primary addition reaches the upper endpoint}
Fix a prime $p$. Let $V$ be a finite connected pointed complex with
nonzero reduced integral homology, all of it $p$-primary torsion.
Then
\[
 \operatorname{Rev}(B\ZZ/p\vee V)
       =W_{\ZZ[1/p]}=R(\operatorname{loc}(\mathbb S/p)).
 \tag{D.3.3.1}
\]
Consequently a proper intermediate localizer in the projective-space
interval cannot make any nonzero finite $p$-primary complex aspherical.
In particular adding a finite complex of type two, or of any higher
finite chromatic type, cannot produce such an intermediate.
\end{claim}
\begin{proof}
Write $W=\operatorname{Rev}(B\ZZ/p\vee V)$. Its two generators
are $\ZZ[1/p]$-acyclic, so $W\subseteq W_{\ZZ[1/p]}$.
Replacing $V$ by a sufficiently high suspension does not change
$W$, by reversibility. We may therefore suppose that $V$ is a
simply connected suspension. The nonzero finite spectrum
$\Sigma^\infty V$ has some finite $p$-type $n+1\geq1$.
Let $d$ be the lowest degree with $\pi_dV\ne0$, and choose an
odd integer $m\geq3$ with $m-1\geq d$.

Distinguish the ordinary nullification $P_V$ from the Goodwillie
stages $G_s=P_s^{\mathrm{Id}}(S^m_{(p)})$.
The precise periodicity input is
\cite[Theorem~4.1]{EH5AroneMahowald1999}: the natural map
\[
                 S^m_{(p)}\longrightarrow G_{p^n}
 \tag{D.3.3.2}
\]
is a $v_j$-periodic equivalence for every $0\leq j\leq n$,
where $j=0$ means a rational homotopy equivalence.
The nullification comparison is
\cite[Corollary~4.8]{EH5Bousfield2001}, in the arbitrary finite
suspension form explicitly stated in
\cite[Theorem~3.1]{EH5BarthelHeutsMeier2021}: a map of
$d$-connected $p$-local spaces is a $P_V$-equivalence if and
only if it is a $v_j$-equivalence for $0\leq j\leq n$.
All the spaces $G_s$ are $(m-1)$-connected. To check the bound,
the derivative formula in
\cite[Theorem~2.1]{EH5AroneMahowald1999} gives the spectrum of
the $s$th layer as
\[
 E_s=\bigl(\operatorname{Map}_*(\Sigma K_s,
          \Sigma^\infty(S^m_{(p)})^{\wedge s})\bigr)_{h\Sigma_s}.
\]
The finite complex $\Sigma K_s$ has dimension $s-1$, so $E_s$
has no homotopy below $sm-s+1\geq m$. Homotopy orbits preserve
this lower bound. Starting with $G_1=QS^m_{(p)}$ and using
the fiber sequences $\Omega^\infty E_s\to G_s\to G_{s-1}$
proves the assertion by induction. These spaces are $p$-local
as well, by the same induction. Thus (D.3.3.2) is a
$P_V$-equivalence and hence belongs to $W$.

We next remove the finite Goodwillie tower by $B\ZZ/p$
nullification. For $s>1$, the spectrum $E_s$ is rationally
zero, by \cite[Proposition~3.1]{EH5AroneMahowald1999}.
Since it is $p$-local, $E_s[1/p]=0$; and the preceding
connectivity estimate makes it a connected spectrum.
\cite[Theorem~3.2]{EH5Levy2025} therefore gives
\[
                    P_{B\ZZ/p}\Omega^\infty E_s\simeq *.
 \tag{D.3.3.3}
\]
Every projection $G_s\to G_{s-1}$ is consequently a
$P_{B\ZZ/p}$-equivalence. Here only the following elementary
nullification property is used: a fibration with connected
$A$-acyclic fibers is a $P_A$-equivalence. Indeed, mapping its
total space into an $A$-null target is the homotopy limit over
the base of the fiber mapping spaces; the natural maps from
the target to those mapping spaces are equivalences. This
identifies the resulting homotopy limit with the mapping space
from the base. No preservation of periodic homotopy by
$P_{B\ZZ/p}$ is asserted.

The map
\[
                 QS^m_{(p)}\longrightarrow K(\QQ,m)
 \tag{D.3.3.4}
\]
is also a $P_{B\ZZ/p}$-equivalence. Its fiber is the infinite
loop space of
\[
     F=\operatorname{fib}(\Sigma^m\mathbb S_{(p)}
                            \longrightarrow\Sigma^mH\QQ).
\]
The spectrum $F$ satisfies $F[1/p]=0$, and its lowest possible
nonzero homotopy is in degree $m-1\geq2$. Apply Levy's theorem
again. The target $K(\QQ,m)$ is $B\ZZ/p$-null, as is also
immediate from the rational cohomology of $B\ZZ/p$.

Both ordinary nullification-equivalence classes used here are
contained in $W$, since $W$ contains their generating maps.
Combining (D.3.3.2)--(D.3.3.4), we have a natural $W$-equivalence
\[
                         r:S^m_{(p)}\longrightarrow K(\QQ,m).
\]
Naturality for a map $p:S^m_{(p)}\to S^m_{(p)}$ of degree $p$
gives $r p\simeq p r$, with the lower $p$ the multiplication
automorphism of $K(\QQ,m)$. Two out of three therefore puts
the degree-$p$ map of $S^m_{(p)}$ in $W$. Its homotopy cofiber
is the usual finite Moore space $M(\ZZ/p,m)$: the comparison
from the integral degree-$p$ cofiber is an integral homology
equivalence of simply connected spaces. The reversible cofiber
criterion makes this Moore space $W$-aspherical.

Suspension and desuspension now put $M(\ZZ/p,2)$ in the
aspherical class. Its ordinary nullification kills every
simply connected space with $p$-primary homotopy groups, by
\cite[Theorem~7.5]{EH5Bousfield1997}. The Serre-class theorem
identifies these with the simply connected spaces having
$p$-primary reduced integral homology. If $X$ is any connected
space with such homology, its suspension is of this form;
reversibility makes $X$ aspherical as well. These are exactly
the aspherical spaces of $W_{\ZZ[1/p]}$. Applying the cofiber
criterion gives $W_{\ZZ[1/p]}\subseteq W$ and proves (D.3.3.1).
\end{proof}
```

### Source checks for this argument

- Arone–Mahowald, *The Goodwillie tower of the identity functor and the unstable periodic homotopy of spheres*, Invent. Math. 135 (1999), 743–788. Opened author-hosted PDF `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/arone-mahowald.pdf`. Theorem 2.1 is the layer-spectrum formula; after its proof the paper explicitly states that `ΣK_s` has dimension `s−1`. Proposition 3.1 says every layer of index `s>1` on an odd sphere is rationally zero. Theorem 4.1 says `S_(p)→P_{p^n}S_(p)` is a `v_j`-equivalence simultaneously for `0≤j≤n`.
- Bousfield 2001, *On the telescopic homotopy theory of spaces*, §4.3, Theorem 4.7, Corollary 4.8, Lemma 4.10 opened. His `L_n^f` also nullifies the other-prime Moore spaces; Lemma 4.10 removes that difference on already `p`-local simply connected spaces.
- Barthel–Heuts–Meier, *A Whitehead theorem for periodic homotopy groups*, arXiv:1811.04030v2, Theorem 3.1 opened. This restates the exact form for **any** finite suspension `V_{n+1}` and its lowest nonzero homotopy degree `d_{n+1}`. It is not restricted to finite source or target spaces. (The paper's main Whitehead theorem has a finiteness hypothesis, but that is not what is used.)
- Levy, *The spectral Sullivan conjecture*, arXiv:2510.00262, Theorem 3.2 opened. It kills the zero-space of every connected spectrum annihilated by inverting `p`. The proof above uses this statement only with spectra connective in degrees at least two.
- Bousfield 1997, Theorem 7.5 was already opened for E/H.5; its Moore nullification arithmetic gives the last step.

The argument does not use a Goodwillie convergence statement for Moore spaces. That would be invalid: Brantner–Heuts show that the analogous periodic finiteness/convergence statements fail for wedges and Moore spaces. The odd sphere is deliberately the intermediate object.

## Eliminated candidate routes

1. **Adding `Ω^∞E` for a connected `p`-torsion spectrum.** Levy Theorem 3.2 puts this space in the ordinary `B Z/p`-acyclic class already. Thus `Q`-spectrum generators cannot enlarge the minimum. This includes `(Q_0 S^0)_(p)` and connected `p`-torsion covers of periodic infinite-loop spaces, after the precise connectivity adjustment.
2. **Adding a nonzero finite primary complex of higher chromatic type.** D.3.3 above shows that every such addition reaches the upper endpoint.
3. **Adding a stunted projective space by its defining cofiber sequence.** Whenever its finite complement is a nonzero finite primary complex, the preceding theorem forces the upper endpoint. This is not an independent intermediate construction.
4. **Varying the dimension of a finite Moore target.** D.1.7--D.1.8 prove that all simply connected mod-`p` Moore targets have exactly the same null class, for fixed `p`.
5. **Using nonrepresentable homology theories from the generalized Ohkawa construction.** As root noted, the cited theories kill every sufficiently small complex, including `S^1`, while failing to kill a large wedge. Their acyclic classes therefore fail arbitrary pointed homotopy-colimit closure and cannot supply the desired fundamental localizers.

## Remaining genuinely infinite target route

For an infinite cardinal `κ`, let `Y_κ^d=∨_κ P^d(2)`, `d≥3`. It is `B Z/2`-null by Miller because its CW dimension is bounded. The simple-higher agent has checked a desuspension argument for its single-target null class: split the colors into three blocks, take the length-three Hilton–Milnor factor, retain diagonal smash summands, and apply the actual `L_3` Moore retraction to obtain `ΩY_κ^{3d−3}` as a retract of `ΩY_κ^d`. Since `κ+κ=κ`, the higher wedge is two copies of itself. The same two-letter James resolution and finite cone-cube argument as D.1.8 then proves desuspension closure. This avoids treating an infinite weak product as an ordinary product.

**No strictness claim has been proved.** The outstanding question is whether these infinite-wedge target null classes differ on spaces with `2`-primary reduced homology from the class for one finite Moore target, and whether any of them gives a strict enlargement of the minimum. A global Moore-versus-sphere witness outside `loc(S/2)` does not answer this. No assertion that the interval has only two elements is justified by the finite-join theorem.

## Shifted infinite loop generators: an exact comparison, 12:40 UTC

Let `A_r = Omega-infinity Sigma^r(S/p)` for integers r>=1, and let W_r be its smallest reversible localizer. Levy2025 Proposition 3.1 and the proof of Theorem 3.2 give the exact computation

    P_{A_r}(A_s) = tau_{<=r-1}(A_s),      r>s>=1.

Here truncation is the ordinary Postnikov section. To verify it, put C=Sigma-infinity A_r and E=Sigma^s(S/p). C is r-connective and its connective Bousfield class contains Sigma^r(S/p), by Levy Proposition 3.1. Every r-connective p-primary spectrum belongs to the latter connective class (shift the connected-spectrum assertion in the proof of Levy Theorem 3.2). Thus F=tau_{>=r}E is C-acyclic. On the other hand B=tau_{<=r-1}E is C-null by t-structure orthogonality. Bousfield1996 Corollary 2.3 applies to F -> E -> B, since its last term is C-null; it gives P_C E=B. Theorem 2.10 then identifies P_{A_r} Omega-infinity E with Omega-infinity P_C E. Theorems/Corollaries 2.3 and 2.10 were reopened directly in the primary ULP PDF at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf.

In particular

    P_{A_r} A_{r-1} = K(F_p,r-1),
    W_{r-1} = W_r join minRev(K(F_p,r-1)).

The map in the first line is a W_r-equivalence. Also W_r is contained in W_{r-1}, since positive suspension of the generating spectrum shows A_r is ordinarily A_{r-1}-acyclic. These two facts prove both inclusions in the second line by two out of three and minimality.

Every W_r has stable part loc(S/p): the suspension spectrum of A_r is p-primary, and its connective class contains Sigma^r(S/p). W_1=minRev(BZ/p) by Levy Theorem 3.2. Each W_r is consequently a nonfixed reversible localizer with this stable part, since it is contained in W_1 and the finite Moore space is excluded. None of this proves that two W_r differ.

The finite-suspension test D.2.7 applies with k=max(1,r-1), because A_r kills all k-connected p-primary GEMs. Equality W_r=W_1 is therefore equivalent to

    P_{A_r}(Sigma^k BZ/p) = *.

This last test remains unresolved. A reverse bar-construction argument is invalid in general: knowing that B A is acyclic does not make Sigma A acyclic. Nor does the inverse-limit convergence of a Goodwillie tower imply acyclicity from acyclicity of every stage. The candidate is recorded as a reduction, not as a strict chain or a new interval element.

## Degree-one Prüfer candidate: the full primary ideal

**Update after checkpoint06:** D.2.14 proves the odd-primary statement,
and D.2.15 now proves the ideal is loc(S/p) **for every prime**, including
2. In fact reduced Sigma-infinity CP-infinity generates all spectra as a
localizing category. The historical source-audit paragraphs below record
the earlier unresolved state and invalid shortcuts. Complete proofs are
in `sections/D2_Pruefer.tex` and `sections/D2_CPinf.tex`; the final audit
is `notes/EH5_CPinf_detector.md`.

Let C=Sigma-infinity B(C_{p^infinity}) and D=Sigma-infinity CP-infinity, both reduced. Then

    loc(C) = loc(D smash S/p).

The homomorphism C_{p^infinity} -> S^1 induces a mod-p equivalence on classifying spaces; the same comparison is explicitly used in Levy2025's first proof of Theorem 1.5. For bounded-below spectra, an F_p-homology equivalence is an S/p-equivalence: its cofiber smashed with S/p has zero integral homology, and stable Hurewicz makes that connective spectrum zero. Thus C/p=D/p. Also C[1/p]=0 because B(C_{p^infinity}) has p-primary reduced integral homology. The cofiber of C -> C[1/p] is Sigma C and is the filtered homotopy colimit of C/p^r. Every C/p^r is built by finitely many extensions from C/p, so loc(C)=loc(C/p)=loc(D/p).

This does not identify the ideal with loc(S/p), and it does not show its finite part is zero. Equal Morava heights or equality of smash-homology Bousfield classes is insufficient for that conclusion. Root checked Bousfield1997 section10.12: B(C_{p^infinity}) is not stable-cohomotopy-acyclic, so the Lee/annihilator-of-the-sphere proof for K(Fp,2) cannot be reused.

Snaith's Bott construction gives a lower bound containing KU/p: writing R=Sigma-infinity_+ CP-infinity and I=D for its augmentation ideal, the Bott element has zero augmentation. Multiplication by Bott factors R -> Sigma^{-2}I -> Sigma^{-2}R. The alternating telescope therefore expresses KU as a homotopy colimit of desuspensions of I, and KU/p lies in loc(D/p). This gives an infinite periodic object, not a nonzero finite spectrum. An opened exposition of the exact Snaith construction is https://math.uchicago.edu/~amathew/snaith.pdf (Theorem1); it is a source lead, not a new manuscript citation. No stable finite-object conclusion from the circle-transfer route has been established.

### Exact scope of the height-one source check, 12:55 UTC

Carmeli, arXiv:2309.12734, Remark 5.4 (opened directly, https://arxiv.org/pdf/2309.12734) states loc(Sigma-infinity B C_p)=loc(S/p), attributing the argument to Burklund's variant of an unpublished Hopkins--Smith proof. Propositions 5.2--5.3 concern K(F_p,n), not B(C_{p^infinity}) or CP-infinity. The remark consequently gives no reverse inclusion loc(S/p) subset loc(D/p). Levy2025's first proof similarly starts with B C_p and then obtains B(C_{p^infinity}) by filtered colimits; its argument does not reverse that step. No checked height-one classification has supplied the missing reverse inclusion or excluded finite objects. This investigation is paused at the exact reduction above; it is not an additional proved example for D.2.

### Further CP-infinity source audit (14:14 UTC)

The branch was reopened specifically to test the finite thick part, not merely its Morava support. Hovey--Palmieri, *The structure of the Bousfield lattice*, https://arxiv.org/pdf/math/9801103, was opened directly. Their item 8.7 states the smash-Bousfield equality <CP-infinity>=<S>, attributes a proof to Hopkins, and explicitly says that the authors do not know the proof. Their Proposition 9.2 separately makes the equivalence between Bousfield order and localizing-subcategory membership part of their general conjectural picture. Consequently item 8.7 cannot be used to infer S/p in loc(D/p). No original Hopkins--Smith manuscript for *On the Bousfield Class of CP-infinity* was located or opened.

Levy, https://arxiv.org/pdf/2510.00262, Lemmas 2.4--2.5 and the first proof of Theorem 1.5 were reopened in full. The polynomial/free-E-infinity-algebra comparison of Lemma 2.5 uses the vanishing of every B Sigma_n from Lemma 2.4; that vanishing is obtained from B C_p and finite-group extensions. Only after this comparison is established does the double bar construction identify the free degree-two E-infinity algebra with Sigma-infinity-plus CP-infinity. Killing D/p alone does not establish Lemma 2.4, so the proof cannot be reversed by retaining only its final CP-infinity step.

Nishida, *On the S1-Segal conjecture*, Publ. RIMS 19 (1983), 1153--1162, https://www.jstage.jst.go.jp/article/kyotoms1969/19/3/19_3_1153/_pdf/-char/en, was also opened directly. Proposition 3.1 compares the completed stable cohomotopy of B(C_{p^infinity}) and BS1. Proposition 3.2 expresses the completed homotopy of Sigma BS1-plus through an inverse system of circle/cyclic-group transfers; Section 4 then applies finite-group Segal results. These are inverse-limit and dual calculations. Localizing-subcategory closure supplies coproducts and homotopy colimits, so this comparison alone does not place the relevant inverse limit or a finite spectrum in loc(D/p). In particular, one must not replace that inverse limit by a homotopy colimit.

The concrete Thom interface is the cofibration B C_p-plus -> CP-infinity-plus -> Th(L^p), with Th(L)=reduced CP-infinity. Although the mod-p first Chern class of L^p is zero, this does not trivialize its stable spherical fibration. Thus an asserted equivalence Th(L^p)/p = Sigma^2(CP-infinity-plus)/p would require a separate control of the coherent stable J-twist; no such equivalence is proved here. Snaith's Bott telescope remains the checked extraction of KU/p, not of a finite Moore spectrum. Neither a nonzero finite member nor vanishing of the finite thick part has been established.

### The finite part has only two possible values

There is nevertheless a precise additional reduction. Write I=loc(D/p)=loc(Sigma-infinity B(C_{p^infinity})). Then

    loc(T(1),T(2),...,HF_p) subset I subset loc(S/p).

Consequently either I has no nonzero finite spectra, or I=loc(S/p). In particular its finite thick part cannot be a proper higher-type subcategory of the p-primary finite spectra.

For the lower inclusion at heights at least two, use the two-sided simplicial bar quotient of multiplication by p on the simplicial abelian group K(Z,2). Its realization is K(F_p,2): this is the homotopy cofiber in simplicial abelian groups, equivalently the homotopy quotient for translation through the multiplication-by-p map. Its degree-k bar term is a product of k+1 copies of K(Z,2). The reduced suspension spectrum of such a finite product is built from D and its smash powers. Therefore Sigma-infinity K(F_p,2) belongs to loc(D). Smashing this bar construction with S/p places (Sigma-infinity K(F_p,2))/p in I. The former spectrum is p-primary torsion, so the p-power-telescope reconstruction used above places the unsmashed Sigma-infinity K(F_p,2) itself in I. Carmeli2023 Proposition 5.3, reopened directly at https://arxiv.org/pdf/2309.12734, states that loc(Sigma-infinity K(F_p,2)) contains T(n) for every n>=2 and HF_p. This proves those memberships.

For height one, the already checked Snaith telescope puts KU/p in I. To pass from this to T(1) without conflating smash classes and ideals, use Bousfield1979, *The localization of spectra with respect to homology*, Definition 3.7, Proposition 4.2 and Corollary 4.7, all reopened directly at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Bousfield_LocalnSpectraHomol.pdf. Proposition 4.2 identifies the telescope of the Adams self-map of S/p with L_KU(S/p). Corollary 4.7 says that L_KU(S) is KU-nilpotent. By Definition 3.7, that means it is in the thick tensor ideal generated by KU. Smashing the finite construction with S/p therefore puts L_KU(S)/p=L_KU(S/p)=T(1) in the thick tensor ideal generated by KU/p, hence in I. This uses an actual finite construction, not closure under arbitrary inverse limits.

Finally suppose a nonzero finite F lies in I. Since I is contained in loc(S/p), F is p-primary and has some finite chromatic type N>=1. Hopkins--Smith's thick classification identifies its finite thick closure with that of a chosen type-N F(N). Carmeli2023 Section 4 equation (2), deduced there from the elementary telescope/cofiber identity Proposition 2.5, gives

    loc(S/p)=loc(T(1),...,T(N-1),F(N)).

Every displayed generator lies in I. Thus loc(S/p) subset I, proving equality. The reverse direction is immediate because S/p is nonzero finite. The unresolved part of this branch is exactly whether I=loc(S/p), rather than a choice among several finite chromatic types.

### Superseding the earlier infinite-target candidate status

The earlier paragraph headed "Remaining genuinely infinite target route" records an intermediate research state. Sections D.3.4--D.3.6 now settle those candidate comparisons: every infinite wedge of simply connected mod-p Moore targets has the same arbitrary-source null class as a single such Moore target; on p-primary sources that class agrees with sphere-nullity. The full family of simply connected finite-dimensional targets, with any fixed infinite bound on cardinality or with no cardinality bound, also gives that same class on the p-primary interval (D.3.5). Thus these target variations do not create a chain. The unresolved separator is a p-primary sphere-null space X for which P_{B C_p}(Sigma X) is noncontractible. The finite-join theorem, infinite-loop theorem, and target-family collapse do not decide its existence.

## D.3.7 independent audit and the generalized-polyGEM observation

The written proof in sections/D3_abelian.tex was independently reviewed in full. Its Ext completion groups need not be p-adically separated; the proof correctly applies classical completion only after passing to a torsion-free cotorsion quotient. The n=1 rational-kernel edge case is handled uniformly by mod-l Serre equivalences and rational cofibers. Actual bar quotients of length-one free-module resolutions justify the module generation step. No arbitrary-product closure or arbitrary homotopy-fibre two-of-three is used.

There is a further source-supported scope extension, recorded here at root's request rather than added to the manuscript. Bousfield1997, Corollary8.10, says for a nilpotent generalized polyGEM X that A kills X if and only if A kills every K(Gamma_s pi_1X/Gamma_{s+1}pi_1X,1) and K(pi_nX,n), n>=2. Taking A=X, and then taking A to be the wedge of those Eilenberg--Mac Lane factors, identifies their ordinary nullity classes. Therefore D.3.7's countable normal forms also cover arbitrary classes of nilpotent generalized polyGEM generators, with Bousfield's Definition8.1 of generalized polyGEM. The exact primary source was reopened at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf, Corollary8.10 on page1340 and Definition8.1 on page1339. The manuscript already includes the polyGEM/finite-Postnikov extension by the CFFS route.

This does not cover arbitrary infinite Postnikov spaces. Nor does allowing an arbitrary nonnilpotent K(G,1) simplify the remaining problem: Kan--Thurston homology models can encode arbitrary spaces, and all reversible localizers already contain the integral homology equivalences. An additional group property would be required to make that route computationally useful.

## Arbitrary abelian Moore targets: concrete reductions

Write M(A,n) for the simply connected Moore space with reduced integral homology A in degree n, where n>=2. A free abelian presentation of A realizes it with cells only in dimensions n and n+1, regardless of the rank or cardinality of A. All source spaces X in this subsection are connected and have reduced H_*(X;Z[1/p])=0.

### Completion comparison has no finite-type assumption

Miller, *The Sullivan conjecture on maps from classifying spaces* (1984), Theorem1.5, printed page45, was reopened directly at https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture.pdf. Its hypotheses are precisely a connected source W with reduced H_*(W;Z[1/p])=0 and a nilpotent fibrant target Y. It asserts Map_*(W,Y) -> Map_*(W,Y_p-complete) is a weak equivalence. Neither W nor Y is required to be of finite type. The proof uses the general arithmetic square for nilpotent spaces, not a finite-type fracture statement. Thus arbitrary-rank Moore spaces and arbitrary-rank wedges of simply connected spheres are legitimate targets here.

A mod-p homology equivalence of targets induces an equivalence after Bousfield--Kan mod-p completion: the free F_p resolution gives a levelwise equivalence after its first application, and a derived totalization preserves this. Combining with Miller1.5, such an equivalence between nilpotent targets induces an equivalence of the mapping spaces from every X under consideration.

### Torsion-free coefficients

Suppose A is torsion-free. Choose a basis I of A/pA, lift it to A=pi_nM(A,n), and realize those lifts by a map

    wedge_I S^n -> M(A,n).

It is a mod-p homology equivalence: the only positive mod-p homology of the target is A/pA in degree n, since Tor(A,F_p)=0. Therefore it induces an equivalence on mapping spaces from all X under consideration. If A/pA=0, every such mapping space into M(A,n) is contractible. Otherwise the Moore target test is exactly the corresponding wedge-of-spheres test. Consequently the torsion-free group structure introduces no new Ulm/Ext parameters in this primary-source setting. This statement alone does not identify the null class of one sphere target with that of the entire sphere family; the previously proved target-family comparisons should be used only in their stated scope.

### Divisible p-torsion coefficients

For A=(C_{p^infinity})^(I), realize the short exact sequence

    0 -> Z^(I) -> Z[1/p]^(I) -> A -> 0

by taking the homotopy cofiber of wedge_I S^n -> M(Z[1/p]^(I),n). The cofiber is M(A,n), since the first homology homomorphism is injective. The actual Puppe map

    M(A,n) -> wedge_I S^{n+1}

is a mod-p homology equivalence: its preceding target M(Z[1/p]^(I),n) is mod-p acyclic. Miller1.5 again identifies the mapping-space tests on arbitrary primary sources. This construction does not assume an unstable completion formula for the rationalization fiber of an even sphere.

### Reduced unbounded p-torsion coefficients: a finite retract

Every nondivisible abelian p-group A has a nonzero finite cyclic direct summand. Here is an elementary proof, avoiding any smallness or boundedness assumption. Choose a outside pA with the smallest possible order p^r among such elements. The cyclic subgroup H=<a> is pure. Indeed, if p^s a=p^k b with s<min(k,r), then c=a-p^(k-s)b remains outside pA and has order at most p^s, a contradiction. Removing a scalar prime to p reduces every failure of purity to this case.

The image of a in A/p^rA consequently has order p^r. Regard this quotient as an R=Z/p^r-module. The ring R is injective as a module over itself: by Baer's criterion, a map from its ideal p^kR to R extends, since the possible image of p^k is exactly an element annihilated by p^(r-k), hence lies in p^kR. The identity from the embedded R=<a> to R therefore extends to A/p^rA. Composition with the quotient map splits A -> Z/p^r. Thus A=Z/p^r direct-sum A' as asserted.

Realize the homology inclusion and projection by maps of Moore spaces. This is possible using free presentations: a lift of each generator exists by Hurewicz, and each relation is null in pi_n, so the map extends over the relation cells. Their composite on M(Z/p^r,n) induces the identity on homology and hence is a homotopy equivalence by the simply connected homology Whitehead theorem. Adjusting one map by its inverse makes M(Z/p^r,n) a homotopy retract of M(A,n).

It follows that M(A,n)-nullity implies M(Z/p^r,n)-nullity. The converse comparison needed in the interval problem is already supplied at p=2 by D.3.5: a 2-primary sphere-null X maps trivially to every simply connected finite-dimensional target, including the arbitrary-cardinality M(A,n).

### The finite-exponent comparison and conclusion

The needed extension of D.3.6 to all finite exponents has now been checked. Boyde, arXiv:2106.03516v2, Section4, Corollary4.4 and Lemma4.5, opened directly at https://arxiv.org/pdf/2106.03516, states the following exact inputs for q=p^r different from 2: for every d>=3, Omega P^d(q) has Omega(P^a(q) wedge P^b(q)) as a homotopy retract for some a,b>=3, and P^u(q) smash P^v(q) is P^(u+v)(q) wedge P^(u+v-1)(q). These are explicit research-source statements. For the two-primary decomposition, Boyde cites Cohen1989 Lemma2.6, *Applications of loop spaces to some problems in topology*, LMS Lecture Notes139, pp.11--20. The original chapter has been bibliographically identified but not opened: repeated publisher requests failed and the publisher preview stops before this chapter. Thus Cohen1989 is **not marked opened**. The proof below relies on the exact opened Boyde statement, not on a purported inspection of Cohen's original.

Let R_X={Y:Map_*(X,Y) is contractible}; no primary-source or finiteness condition on X is needed in this paragraph. Starting with M(Z/q,n) in R_X also puts its loop space there. Apply the two-summand retract. The Hilton--Milnor word with k occurrences of the first letter and one of the second, followed by the displayed smash splitting, puts Omega P^D(q) in R_X for every

    k(a-2)+b <= D <= k(a-1)+b.

For large k these intervals overlap or are adjacent, so all sufficiently large D occur. The rest of the already proved D.1.7 argument uses only these two inputs: Hilton--Milnor gives looped finite bouquets, increasing connectivity gives looped finite-type bouquets, the convergent James resolution removes the loops, and the Barratt cone cubes lower finite bouquets through every dimension down to three. It does not use the odd-primary coefficient 2 from the earlier part of D.1.7. Hence all P^D(q), D>=3, and the smash/suspension-closed family generated by P^3(q), belong to R_X. For q=2, D.1.8 and D.3.6 already give the corresponding conclusions.

Now repeat D.3.6's finite cone-length argument with q in place of p. The composite P^m(q) -> S^m -> P^(m+1)(q^k) has cofiber P^(m+1)(q^(k+1)): its cellular boundary is [[q^k,1],[0,q]]. Strom's resolving-class Corollary11 applies to the same smash-closed family and puts every P^(m+1)(q^k) in R_X. The tower with exponents p^(rk)=q^k is cofinal in the usual Moore tower. D.3.6's homological pro-space proof therefore identifies its homotopy limit with the p-completed m-sphere, for every m>=2. Closure of R_X under homotopy limits proves

    Map_*(X,M(Z/p^r,n))=*  =>  Map_*(X,(S^m)_p-complete)=*
                              for all m>=2.

This implication holds for every pointed X. Combining it with the finite cyclic retract above, and with D.3.5 in the reverse direction, proves the exact interval conclusion at p=2:

    For every nondivisible abelian 2-group A and every n>=2,
    M(A,n)-nullity on 2-primary connected sources equals sphere-nullity.

In particular, reduced unbounded 2-torsion groups, arbitrary Ulm lengths, and arbitrary cardinalities do not create new target null classes in this interval. This is a target-side result and does not reuse D.3.7's source-side GEM classification. At odd primes the forward completed-sphere implication is proved above; the stated reverse uses only the range of D.3.5 actually established in the manuscript.

## Identical products with finite homotopy groups also collapse

Let Z be a connected pointed space with finite pi_n(Z) for every n>=1, and let I be any small set. Let Part_fin(I) be the filtered poset of finite partitions of I, ordered by refinement. A refinement induces a diagonal map Z^P -> Z^Q. There is a canonical weak equivalence

    hocolim_{P in Part_fin(I)} Z^P  ->  product_I Z.

Indeed, filtered homotopy colimits commute with homotopy groups. On pi_n this map identifies the source with the functions I -> pi_n(Z) having finite image. Since pi_n(Z) is finite, these are all functions, exactly the homotopy group of the product. Both sides are connected. This verifies weak equivalence for arbitrary I; it makes no assumption about continuity of abstract homomorphisms between product groups.

Every ordinary nullification-acyclic class is closed under finite products and pointed homotopy colimits, so if it contains Z it contains every identical power Z^I. Apply this to Z=Sigma BZ/2 and Z=Omega Sigma BZ/2. Their homotopy groups are finite 2-groups: the simply connected finite-type space Sigma BZ/2 has 2-primary reduced homology, so the Serre-class and finite-generation theorems apply; looping shifts its homotopy groups and keeps connectedness. The first space is plainly BZ/2-acyclic. The second is also BZ/2-acyclic by the James construction: each finite James stage is a pushout of a product of BZ/2 along its fat wedge to the preceding stage; the fat wedge is a finite homotopy colimit of lower products. Finite products, these pushouts, and the sequential homotopy colimit all preserve the acyclic class. Therefore neither proposed identical product supplies a strict-interval separator. Varying factors whose homotopy groups or types are unbounded in a fixed degree is not covered by this argument.

### Products of varying finite wedges of Sigma BZ/p

Root supplied a further exact Hilton--Milnor argument, independently checked here. Let Z_i be a finite wedge of copies of Sigma BZ/p, with the number of copies allowed to vary without bound. Then product_i Z_i is still ordinarily BZ/p-acyclic. This includes the attempted example Z_i=wedge_(j<=i) Sigma BZ/2.

Put Y_k=Omega Sigma((BZ/p)^(smash k)). Hilton--Milnor gives

    Omega Z_i = product_(k>=1) Y_k^(a_(i,k)),

where a_(i,k) is the finite number of basic words of length k in the letters of the i-th wedge. The theorem initially supplies a weak product; its factors' connectivities tend to infinity, so the weak product maps by a weak equivalence to the full product. Loops and products commute, and products may be reordered, giving

    Omega(product_i Z_i) = product_(k>=1) Y_k^(kappa_k),
    kappa_k = cardinality of the disjoint union over i of a_(i,k) copies.

For every fixed k, Y_k has finite p-primary homotopy groups in every degree. Indeed Sigma((BZ/p)^(smash k)) is simply connected, has finite-type homology, and has p-primary reduced homology. The Serre theorems therefore apply. Moreover Y_k is ordinarily BZ/p-acyclic: smash products and suspension preserve the acyclic class, and the James construction preserves it by the preceding finite-product/fat-wedge argument. The finite-partition lemma now makes every identical power Y_k^(kappa_k) acyclic.

The connectivity of Y_k is at least k-1, and taking powers preserves this bound. Consequently the remaining product over k is weakly equivalent to the filtered homotopy colimit of its finite subproducts; it too is acyclic. Finally product_i Z_i is simply connected and is the geometric realization of the ordinary bar construction on its connected loop space. Every bar level is a finite product of that acyclic loop space. Closure under pointed homotopy colimits proves product_i Z_i acyclic. This settles the proposed varying-wedge product without guessing a uniform exponent bound for its homotopy groups.

A materially different product candidate would require more than varying multiplicities of these fixed Hilton--Milnor factor types. Merely allowing cyclic groups of unbounded exponent in degree one also fails the primary-endpoint condition: product_i Sigma B(Z/p^i) has H_2=product_i Z/p^i, which contains infinite-order elements.

### Products of Postnikov approximations can contain a finite Moore retract

There is a concrete counterexample to inferring either ordinary acyclicity or sphere-nullity from the factors of a varying product. Take M=M(Z/p,2), a noncontractible finite simply connected Moore space. Every finite Postnikov section P_nM is ordinarily BZ/p-acyclic, since its finitely many homotopy groups are finite p-groups and the successive Eilenberg--Mac Lane fibers are acyclic. Nevertheless

    M is a homotopy retract of product_(n>=1) P_nM.

Here is a precise ordinary-space construction, including the source of the discontinuous maps. Choose a Postnikov tower E_n with Kan fibration transition maps and E_n weakly equivalent to P_nM. Every E_n can be made finite in every simplicial degree. Inductively, a principal Postnikov extension with finite group A=pi_nM is a pullback of the universal principal fibration W K(A,n) -> bar-W K(A,n). The Dold--Kan simplicial group K(A,n) is finite in each degree; the bar and universal-bundle constructions involve only finitely many of its degrees in each fixed simplicial degree. Both are therefore levelwise finite. Pulling back over a levelwise finite Kan E_(n-1) preserves this property, and the transition map is a Kan fibration. The inverse limit L=lim_n E_n computes the homotopy limit and is weakly equivalent to M by Postnikov convergence.

The exact finite-model input was independently source-checked in Barnea--Harpaz--Horel, *Pro-categories in homotopy theory*, Algebraic & Geometric Topology17 (2017), 567--643, https://msp.org/agt/2017/17-1/agt-v17-n1-p17-p.pdf. Lemma7.2.4 and Corollary7.2.6 identify pi-finite spaces with levelwise finite coskeletal minimal Kan models. Lemma7.2.7 and the proof of Proposition7.2.10 give the actual principal pullback construction for the Moore--Postnikov tower. Thus the ultrafilter argument below uses verified finite sets of simplices, not merely finite homotopy groups of an arbitrary model.

Fix a nonprincipal ultrafilter U on the positive integers. For a q-simplex x=(x_n) in product_n E_n and a level m, map x_n down to (E_m)_q for n>=m. This is a sequence in a finite set, so exactly one value occurs on a U-large set. Call this value r_m(x). Discarding finitely many indices has no effect. The transition maps commute with finite-set ultrafilter limits, hence the r_m(x) are compatible. Faces and degeneracies also commute with these limits. Thus r=(r_m) defines an actual simplicial map

    r: product_n E_n -> lim_n E_n=L.

For a compatible tuple from L each relevant sequence is constant, so r is a strict retraction of the canonical diagonal L -> product_n E_n. This proves the displayed homotopy retraction. No compactness assertion about arbitrary abstract homomorphisms is used; the ultrafilter map is exactly a potentially discontinuous ordinary simplicial map.

For each fixed k, pi_k of the product is a product of copies of the one finite p-group pi_kM, with finitely many trivial entries, and hence has bounded p-exponent. The product is simply connected and has p-primary homology by the Serre-class theorem. Thus it does lie in the primary endpoint. But the finite Moore retract makes its reversible closure the full endpoint by D.3.3 (or the Moore arithmetic directly). It is not null for all simply connected p-completed spheres: the reverse implication in D.3.6, applied to this rationally acyclic source, would make its map to M null, contradicting the retract and the nontrivial identity of M. At p=2 this also excludes W_S-nullity by the primary arithmetic comparison. This varying-product family therefore cannot supply the requested strict intermediate either.

### Exact reversible join for every Postnikov product of one finite-homotopy space

The preceding example has a general exact formulation. Let Y be simply connected with every pi_kY a finite p-group. Let I be a small set, choose positive integers n_i, and put Z=product_(i in I) P_(n_i)Y. Then Z still has p-primary homology. If the heights n_i are bounded, Z is ordinarily BZ/p-acyclic. If they are unbounded, then

    minRev(BZ/p wedge Z) = minRev(BZ/p wedge Y).

Thus products of Postnikov approximations do not create new interval joins beyond the underlying Y. In particular, if Y is already ordinarily BZ/p-acyclic, every such product is ordinarily BZ/p-acyclic, regardless of the heights and their multiplicities.

Here are the details. In each fixed degree k, every nonzero pi_k(P_(n_i)Y) is the same finite group pi_kY, so pi_kZ has a fixed finite p-exponent. The Serre-class theorem gives the primary homology assertion. If the heights are bounded by N, Z is a simply connected N-type with p-primary homotopy groups. Its finite principal Postnikov tower has p-primary Eilenberg--Mac Lane fibers, and it is ordinarily BZ/p-acyclic.

Suppose next that the heights are unbounded. The finite Kan tower E_n constructed above models the P_nY. There exists an ultrafilter U on I containing every set {i:n_i>=m}: these sets have the finite intersection property and no common point. For each m, the U-limit of the coordinates E_(n_i) -> E_m, defined on this U-large set, gives the same compatible simplicial retraction from product_i E_(n_i) to lim_m E_m=Y. Thus Y is a homotopy retract of Z, proving one inclusion of reversible joins.

For the converse put W=minRev(BZ/p wedge Y). Let C_n be the connected cover hofib(Y -> P_nY). It fits into the rotated fiber sequence

    Omega P_nY -> C_n -> Y.

The first term is connected, nilpotent, has finitely many nonzero homotopy groups, all p-primary, and hence is ordinarily BZ/p-acyclic. Thus C_n is W-acyclic because Y is. Each C_n still has finite homotopy groups in every degree, so every identical power C_n^J is W-acyclic by the finite-partition lemma. Likewise Y^I is W-acyclic.

The homotopy fiber of the product comparison Y^I -> Z is product_i C_(n_i). Grouping factors by their heights gives product_(n>=1) C_n^(I_n), where I_n={i:n_i=n}. The C_n are n-connected, so this outer product is weakly equivalent to the filtered homotopy colimit of its finite subproducts. It is therefore W-acyclic. A map whose homotopy fibers are W-acyclic belongs to W: its source is the homotopy colimit over its target of those fibers, and homotopy-colimit closure applies to the objectwise maps to a point. Hence Y^I -> Z belongs to W, and Z is W-acyclic. This proves the other inclusion.

If Y is ordinarily BZ/p-acyclic, exactly the same proof works inside that ordinary acyclic class: finite products, pointed homotopy colimits, and fibrations with acyclic fibers suffice. It does not require reversibility. This proves the last assertion. The formula gives no dichotomy for arbitrary unrelated products and no solution of whether some underlying Y yields a proper intermediate; it precisely isolates the information carried by this entire construction.

## Independent audit of D.2.10

The full saved proof in sections/D2_stable_miller.tex was reviewed independently and passed. The decisive sources were directly reopened: Bergsaker--Rognes2023 Theorem1.1 and the introduction's norm-sphere identification; Carlsson1992 Corollary2.3; Arone--Mahowald1999 Theorem2.1; Goodwillie1992 Example4.3 and Goodwillie2003 Theorem1.13.

The completion/function-spectrum interchange uses dualizability of each finite Moore spectrum before taking an inverse limit and hence needs no compactness of BP. The transfer comparison is a mod-p homology equivalence of bounded-below spectra; its cofiber smashed with S/p is integral-homology acyclic and therefore zero by stable Hurewicz. The reduced classifying spectrum's connective AHSS gives finite |G|-primary stable homotopy groups, so its reconstruction from primary completions is valid. The quotient (product_q Z_q)/Z is uniquely divisible, and the rational retract argument uses only products and retracts, not an unproved closure under coproducts.

The partition-complex dual smashed with K^k has an actual genuine finite symmetric-group model; no assertion about arbitrary naive actions on finite spectra is substituted. The localized layer follows by stable p-localization and commutation of homotopy orbits with smashing. The Goodwillie tower converges on every simply connected target, including K_(p), and mapping out of an arbitrary Y preserves that inverse limit. Finally stable sphere annihilation forces connectedness by the split sphere contributed by any additional component. No proof gap was found.
