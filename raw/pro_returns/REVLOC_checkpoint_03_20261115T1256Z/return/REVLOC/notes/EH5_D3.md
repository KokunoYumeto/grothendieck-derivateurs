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

## Degree-one Prüfer candidate: exact reduction, finite part unresolved

Let C=Sigma-infinity B(C_{p^infinity}) and D=Sigma-infinity CP-infinity, both reduced. Then

    loc(C) = loc(D smash S/p).

The homomorphism C_{p^infinity} -> S^1 induces a mod-p equivalence on classifying spaces; the same comparison is explicitly used in Levy2025's first proof of Theorem 1.5. For bounded-below spectra, an F_p-homology equivalence is an S/p-equivalence: its cofiber smashed with S/p has zero integral homology, and stable Hurewicz makes that connective spectrum zero. Thus C/p=D/p. Also C[1/p]=0 because B(C_{p^infinity}) has p-primary reduced integral homology. The cofiber of C -> C[1/p] is Sigma C and is the filtered homotopy colimit of C/p^r. Every C/p^r is built by finitely many extensions from C/p, so loc(C)=loc(C/p)=loc(D/p).

This does not identify the ideal with loc(S/p), and it does not show its finite part is zero. Equal Morava heights or equality of smash-homology Bousfield classes is insufficient for that conclusion. Root checked Bousfield1997 section10.12: B(C_{p^infinity}) is not stable-cohomotopy-acyclic, so the Lee/annihilator-of-the-sphere proof for K(Fp,2) cannot be reused.

Snaith's Bott construction gives a lower bound containing KU/p: writing R=Sigma-infinity_+ CP-infinity and I=D for its augmentation ideal, the Bott element has zero augmentation. Multiplication by Bott factors R -> Sigma^{-2}I -> Sigma^{-2}R. The alternating telescope therefore expresses KU as a homotopy colimit of desuspensions of I, and KU/p lies in loc(D/p). This gives an infinite periodic object, not a nonzero finite spectrum. An opened exposition of the exact Snaith construction is https://math.uchicago.edu/~amathew/snaith.pdf (Theorem1); it is a source lead, not a new manuscript citation. No stable finite-object conclusion from the circle-transfer route has been established.

### Exact scope of the height-one source check, 12:55 UTC

Carmeli, arXiv:2309.12734, Remark 5.4 (opened directly, https://arxiv.org/pdf/2309.12734) states loc(Sigma-infinity B C_p)=loc(S/p), attributing the argument to Burklund's variant of an unpublished Hopkins--Smith proof. Propositions 5.2--5.3 concern K(F_p,n), not B(C_{p^infinity}) or CP-infinity. The remark consequently gives no reverse inclusion loc(S/p) subset loc(D/p). Levy2025's first proof similarly starts with B C_p and then obtains B(C_{p^infinity}) by filtered colimits; its argument does not reverse that step. No checked height-one classification has supplied the missing reverse inclusion or excluded finite objects. This investigation is paused at the exact reduction above; it is not an additional proved example for D.2.

### Superseding the earlier infinite-target candidate status

The earlier paragraph headed "Remaining genuinely infinite target route" records an intermediate research state. Sections D.3.4--D.3.6 now settle those candidate comparisons: every infinite wedge of simply connected mod-p Moore targets has the same arbitrary-source null class as a single such Moore target; on p-primary sources that class agrees with sphere-nullity. The full family of simply connected finite-dimensional targets, with any fixed infinite bound on cardinality or with no cardinality bound, also gives that same class on the p-primary interval (D.3.5). Thus these target variations do not create a chain. The unresolved separator is a p-primary sphere-null space X for which P_{B C_p}(Sigma X) is noncontractible. The finite-join theorem, infinite-loop theorem, and target-family collapse do not decide its existence.
