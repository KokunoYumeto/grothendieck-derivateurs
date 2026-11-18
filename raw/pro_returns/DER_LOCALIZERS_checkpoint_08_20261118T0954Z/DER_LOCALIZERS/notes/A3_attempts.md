# A.3: independent routes and exact remaining gates

Author: GPT-6 Astra, child agent `intervals`; 18 November 2026. This is an attack log, not a claim that A.3 or A.4 has been decided. The Part B and A.5 deliverables are separate and complete.

## 1. The decision and the strongest established reduction

The question is whether a reversible fundamental localizer can fail to be fixed by `RT` while its stable part contains no nonzero finite spectrum. The strongest universal reduction is now A34.5–A34.6, independently accepted by root and schematization. It is equivalent to the existence of one primary infinite-loop generator `A=QΣ³V` with no nonzero finite spectra in `L_A=loc(Σ∞A)`, together with a noncontractible sufficiently connected primary **A-null H-space** `Z` for which `Σ∞Z∈L_A`. The precise connectivity bound is `d=n−1` when the first nonzero homology group `G=H_nA` has `G/pG≠0`, and `d=n` in the divisible-bottom case. The associated reversible closure is accessible. For every prescribed finite loop degree m the same generator can be used with an m-fold loop witness Z_m; no single infinite-loop witness or limiting inference is asserted. The small supporting family consists of actual aspherical CW spaces in a fixed universe, and no uniform size or accessibility rank is asserted.

The arithmetic first step remains valid for every reversible `W`: `W_p=W∩R(loc(S/p))` has `T(W_p)=Γ_pT(W)`, and `W` is RT-fixed exactly when all primary intersections are. The normal form has not produced an actual generator–separator pair. The following gate remains a separate sufficient route through one chosen ideal. Put

\[
B=K(\mathbb F_p,2),\qquad L_p=\operatorname{loc}(\Sigma^\infty B).
\]

The return already gives a nonzero `L_p` with zero finite part and an accessible reversible realization. For the particular realization `minRev(B)`, the exact remaining test is

\[
\Sigma^\infty X\in L_p,
\qquad P_B(\Sigma X)\not\simeq *.
\tag{G1}
\]

This is an equivalence for failure of fixedness of that particular localizer, not an equivalence for the existential question over every possible stable part. Its source is the complete argument in REVLOC `sections/D_nullification.tex`, D.2.7: Bousfield 1996 Theorem 3.3 gives the one-suspension reduction, and Bousfield 1997 Lemma 8.13 says that `B` kills the required simply connected primary GEMs. The extra divisibility qualification in Lemma 8.13 must be retained for divisible generators.

**Full proof promoted into the present return.** `sections/A34_reduction.tex`, A34.1–A34.2, now gives the complete proof of the equality `A_minRev(B)={X:P_B(ΣX)=*}`, together with the `BCp∨V` and `A_r` versions. Both original Bousfield theorem statements and their proofs were opened and rechecked in this run. The crucial step is that `P_B(Σ²X)=*` forces primary homology and hence connectedness of `X`; the primary GEM `SP∞ΣX` is then killed by Bousfield 1997 Lemma 8.13, and Bousfield 1996 Theorem 3.3 identifies the nullity of `ΣX` with that of `Σ²X∨SP∞ΣX`. Thus the once-suspended acyclic class is desuspension closed. Cofiber rotation gives its third cofiber implication, and the nullification cone construction plus reversible desuspension gives both minimality inclusions. Root independently audited this proof against the two primary sources and approved it. Ordinary failure `P_BX≠*` alone is not used as an exclusion from the reversible closure.

A related, sufficient gate uses

\[
A_r=Q\Sigma^r B,\qquad W_r=\min\operatorname{Rev}(A_r),\quad r\geq0.
\]

REVLOC D.2.9 proves that these have the same stable part `L_p`. A counterexample would follow from

\[
P_{A_r}(\Sigma^{r+1}B)\not\simeq *
\tag{G2}
\]

for one `r`. The old long obstruction calculation concerns a particular instance of this gate. This independent attack has not supplied its full-source extension, and does not use a finite skeleton calculation as a substitute.

## 2. Finite-dimensional targets, including arbitrarily large ones: excluded

**Attempt.** Extend the finite-target Miller obstruction from REVLOC D.2.10 to infinite-cell but finite-dimensional targets, hoping to separate a space in `R(L_p)` from its smallest reversible realization.

**Primary inputs opened.** Haynes Miller, *The Sullivan conjecture on maps from classifying spaces*, Annals 120 (1984), the author PDF, Theorems A and A′. These cover locally finite groups and the stated finite Postnikov generalization against connected finite-dimensional CW targets. Jeffrey Strom, *Finite-dimensional spaces in resolving classes*, Fund. Math. 217 (2012), 171–188, DOI `10.4064/fm217-2-3`: Theorem 1; Proposition 4(b); Proposition 6; Corollary 12(a),(b). Also Strom, *Miller spaces and spherical resolvability of finite complexes*, Fund. Math. 178 (2003), 97–108, DOI `10.4064/fm178-2-1`, opened from the publisher: Corollary 11 and Theorem 10.

**Exact exclusion.** REVLOC D.3.5 already proves, at `p=2`, that sphere-null primary spaces map trivially into every simply connected finite-dimensional CW target, with no restriction on the cardinality of the source or target. Its full proof was read. It first proves the countable-source result by pro-zero inverse towers, Hilton–Milnor, and Strom Corollary 12. It then uses the countable enlargement theorem G.7, whose full proof was also read, to remove source cardinal bounds. The argument is not merely the finite-type theorem from Strom. Replacing the finite coefficient field in G.7 and the arithmetic square by their `p` versions gives the identical argument at any prime; the literal attached D.3.5 statement is at `2`.

Consequently finite targets, finite-dimensional targets of infinite cardinality, and arbitrary wedges of simply connected spheres do not solve (G1). Arbitrary wedges of spheres are explicitly dealt with inside the proof, even when their dimensions are unbounded. No new cardinal parameter is obtained by enlarging these families.

**What is still outside this exclusion.** Infinite-dimensional targets with genuinely unbounded complexity are not automatically covered. In particular a wedge of finite complexes whose cone lengths are unbounded is not finite-dimensional; the theorem must not be extended to every such wedge without proof.

## 3. Pure infinite-loop substitutions: excluded in the stated range

**Attempt.** Replace the unknown `X` by `Ω∞E` for a connective spectrum in `L_p`, or use an infinite-loop target to detect (G1).

**Exact input.** REVLOC D.2.9 was read in full. It uses Bousfield 1996 Theorem 2.6, not a claim that ordinary unstable nullification is stable. If `C` is `n`-connective, has primary integral homology and nonzero bottom mod-`p` homology, then

\[
E\in\operatorname{loc}(C)\cap\mathrm{Sp}_{\geq n}
\implies P_C^{\mathrm{Sp}} E\simeq0.
\]

For `C=Σ∞A`, Bousfield Theorem 2.10 identifies the corresponding infinite-loop-space nullification. Thus the proposed infinite-loop sources in the required connectivity range are already ordinarily `A`-acyclic. This rules out that direct source construction.

In the notation of Levy 2025, Definition 1.4 and Lemma 2.3, let `⟨C⟩^s` denote the smallest spectral class closed under colimits and extensions and containing `C`. The same checked argument in fact gives the exact equalities

\[
\langle\Sigma^\infty B\rangle^s=L_p\cap\mathrm{Sp}_{\geq2},
\qquad
\langle\Sigma^\infty A_r\rangle^s=L_p\cap\mathrm{Sp}_{\geq r+2}.
\tag{G3}
\]

The forward inclusions follow because each right side is closed under colimits and extensions. The reverse inclusions are D.2.9, together with Levy Lemma 2.3 identifying spectral-nullification acyclics with this connective closure. Thus a higher version of the connective-closure input is already available in the precise range required. Replacing the right side with **all** sufficiently connective primary spectra would be false: it would put a shifted nonzero finite Moore spectrum in `L_p`. Equation (G3) does not provide a passage from arbitrary spaces to infinite-loop spaces that preserves the non-nullification condition in (G1).

An infinite-loop target equipped with the full stable right-orthogonality condition also cannot detect the gap, by suspension-spectrum adjunction. A target that is merely `A`-null is not silently identified with a full stable right orthogonal: negative shifts and connectivity matter.

**Inverse-limit obstruction.** A Goodwillie/Postnikov approach has acyclic infinite-loop layers but still requires passage through an inverse limit. Acyclic classes are closed under the required homotopy colimits, not under arbitrary homotopy inverse limits. A finite primary Moore space supplies the familiar warning: its finite primary Postnikov stages are killed by the Eilenberg–Mac Lane generator in the appropriate connected range, while the Moore space itself is a nonzero finite Miller-local target. Thus increasingly connected convergence alone does not supply the missing preservation theorem.

## 4. Higher divisible Eilenberg–Mac Lane generators: comparison refined by A34.4

**Attempt.** Replace `K(Fp,2)` by `K(C_{p∞},n)`, hoping that different ordinary nullities have the same stable part with no finite spectra.

**Exact exclusions and subsequent refinement.** REVLOC D.2.14–D.2.15 show that degree-one Prüfer generators already have stable ideal `loc(S/p)`, which contains a nonzero finite spectrum. They cannot answer A.3. The degree-two equality was open at checkpoint 05; the subsequently proved A34.4 refutes it by an actual smash-homology detector. See (M10) below. Matching Morava-height vanishing patterns would not establish equality of actual localizing subcategories.

Bousfield 1997 Lemma 8.13 includes the extra condition `π_nX/pπ_nX=0` when the generator group is divisible. Deleting this condition would give a false shortcut. A34.4 calculates a nonzero suspended nullification for the degree-two Prüfer generator, but its separating space is outside that generator's stable ideal. Thus it does not give (G1), (G2), or an A.3 witness.

## 5. Stable ideals with zero finite part need suspension-spectrum generators

**Attempt.** Choose `loc(HFp)` or an ideal of positive periodic telescope spectra merely because it has no finite objects, then seek a reversible realization inside it.

**Precise obstruction.** Stable parts here are generated by suspension spectra of aspherical spaces. An arbitrary stable ideal with no finite spectra need not occur as a nonzero stable part.

For the ideal generated by `HFp`, the obstruction is rigorous. Hopkins–Ravenel, *Suspension Spectra are Harmonic*, author preprint dated 3 June 1992, Theorem 8, says that suspension spectra are harmonic. Proposition 11 says that `HFp` is dissonant; the localizing subcategory it generates remains dissonant. A spectrum that is both harmonic and dissonant is zero. Therefore

\[
\operatorname{loc}(H\mathbb F_p)
\cap\{\text{suspension spectra}\}=\{0\}.
\]

This is an exclusion of this particular construction, not a statement that every stable ideal with no finite part is dissonant. In particular it does not exclude `L_p`.

For an ideal generated by positive periodic telescopes, the proposed connective realization also has a separate elementary obstruction: such telescopes are integral-homology acyclic, whereas a nonzero bounded-below integral-homology-acyclic spectrum contradicts the first nonzero homotopy group's stable Hurewicz isomorphism. This statement applies to the indicated telescope-generated homology-acyclic ideal, not to every telescope-related localization category.

## 6. Phantom and same-type constructions: no witness obtained

**Attempt.** Find spaces with the same stable type but different nullification, or detect the gap with phantom maps into an infinite-dimensional target.

Actual maps between connected spaces inducing equivalences of suspension spectra do not supply a shortcut: they induce integral homology equivalences, their suspensions are weak equivalences, and every reversible fundamental localizer already inverts them. An abstract stable equivalence without such an unstable map is a different matter, but no applicable pair was constructed.

J. Daniel Christensen's MIT thesis, *Ideals in triangulated categories: phantoms, ghosts and skeleta*, §6.3, Lemma 6.9 and Proposition 6.10, was opened and read. It constructs a nonzero superphantom out of `HFp`. The theorem concerns stable maps that vanish on every desuspended suspension-spectrum test. It does not itself construct the required space `X`, and the harmonicity obstruction in §5 prevents treating `HFp` itself as a nonzero suspension-spectrum generator.

There is a concrete remaining infinite-dimensional target program. Given finite subcomplexes `X_i` exhausting a space, the telescope cofiber sequence yields a universal phantom into `Σ∨_i X_i`. Such a target can escape finite-dimensional target theorems. To solve (G1) by this program, one must prove that the target is `B`-null while the proposed map out of `ΣX` survives; to solve (G2), prove it is `A_r`-null and the map from `Σ^{r+1}B` survives. Nullity of each finite summand does not imply nullity of their infinite wedge. No uniform tower bound establishing the first requirement has been found. Consequently this is a precise open gate, not a counterexample.

### A concrete essential phantom, with a complete proof

The nonzero-map half of this program can be proved. Suppose `X` is a connected countable CW complex, `X_i` is an exhaustion by finite pointed subcomplexes, and the reduced suspension spectrum `E=Σ∞X` is nonzero and satisfies

\[
[E,F]=0\quad\text{for every finite spectrum }F.
\tag{P1}
\]

Here is an actual space-level construction, with no subtraction on an unstable wedge. Choose the exhaustion maps cellular and form the **reduced mapping telescope** `T`: take the ordinary mapping telescope and collapse its basepoint ray. This ray is a contractible CW subcomplex, so `T≃X`. The integer-level stage slices form the CW subcomplex `A=∨_i X_i` of `T`. On collapsing `A`, each cylinder `X_i×[i,i+1]` has both ends and its basepoint interval collapsed, and hence becomes `ΣX_i`. Consequently there is an actual pointed cofibration and quotient identification

\[
\bigvee_iX_i\longrightarrow T\longrightarrow T/A
   \cong\bigvee_i\Sigma X_i.
\]

Its quotient map is zero on every stage. Any phantom map out of `X` is null on each `X_i`, so choosing these based nullhomotopies supplies a nullhomotopy on their wedge and the cofiber universal property gives a factorization through the quotient. Under `T≃X`, this is the universal phantom

\[
\delta:X\longrightarrow Z_X:=\bigvee_i\Sigma X_i.
\tag{P2}
\]

Its restriction to each finite subcomplex is null. After applying the suspension-spectrum functor, the cylinder boundary is `s−1` on the wedge of stage spectra; changing its overall sign gives the standard telescope triangle below. Thus the quotient map really is its boundary, up to that harmless sign:

\[
W\xrightarrow{1-s}W\longrightarrow E
 \xrightarrow{\Sigma^\infty\delta}\Sigma W,
\qquad W=\bigvee_i\Sigma^\infty X_i.
\]

**Claim.** `Σ∞δ` is nonzero, and hence `δ` is essential.

**Proof.** If the boundary were zero, the triangle would split and there would be maps `i:E→W` and `r:W→E` with `ri=id_E`. Let `e=ir`. For every projection `q_j:W→Σ∞X_j`, (P1) gives `q_ji=0`; therefore every matrix entry `q_jeι_k` is zero. Each source `Σ∞X_k` is compact, so `eι_k` factors through a finite subwedge of `W`. A finite wedge is a biproduct in spectra, and its projections detect its maps; hence `eι_k=0`. The coproduct universal property gives `e=0`, and then `id_E=re i=0`, contrary to `E≠0`. This proves the claim.

Apply this to `X=Σ^{r+1}K(Fp,2)`, using the stable Miller theorem (Lee, as reproved in Allen Yuan, *The sphere of semiadditive height 1*, arXiv:2208.12844, Corollary 1.4.1). It produces an explicit target of the form

\[
Z_X=\bigvee_i\Sigma^{r+2}B_i,
\]

where the `B_i` are finite subcomplexes exhausting `B`. This target has infinitely many bottom-dimensional cells and no bound on dimension. Each individual finite summand is invisible to the Miller source, but the whole wedge is not. The construction is compatible with, and explains the necessity of, the dimensional hypotheses in §2.

The **remaining gate is exactly** `Map_*(A_r,Z_X)≃*`; no such assertion is proved here. In the original `B`-nullification test, using a suspension of `B` itself as source cannot work, because that source is already `B`-acyclic. For the `A_r` test, stable essentiality of the phantom does not imply its survival after `P_{A_r}`: applying nullification can kill its stable class. This is the precise reason that the displayed essential phantom alone does not decide A.3.

### Every map into this wedge is phantom; the exact tower to compute

There is a further precise reduction. Let `Z_r=∨_iΣ^{r+2}B_i`, as above, and choose a finite CW exhaustion `(A_r)_n` of `A_r`. For every `t≥0`, **every** map `f:Σ^tA_r→Z_r` is phantom. To prove this, restrict to a finite subcomplex of the source. Its compact image lies in a finite subwedge `Z_J`. Let `q_J:Z_r→Z_J` be the projection. Since `Σ∞Σ^tA_r∈L_p`, REVLOC D.2.10 gives `Map_*(Σ^tA_r,Z_J)≃*`: the target is a finite simply connected complex. Thus `q_Jf` is null, and its restriction is precisely the chosen restriction of `f`, regarded in `Z_J`. Including `Z_J` back into `Z_r` proves the assertion. This does not claim that the full wedge is a finite-dimensional target.

Consequently the remaining nullity gate is equivalent to the following explicitly countable inverse-system condition:

\[
\text{for every }t\geq0,\qquad
\lim_n^{1}[\Sigma^{t+1}(A_r)_n,Z_r]_* = *.
\tag{P3}
\]

The identification is the Milnor exact sequence for the mapping tower of a sequential CW exhaustion. Each displayed group is countable, because the source is finite and the target is a countable CW complex. Hence (P3) is equivalent to the Mittag–Leffler condition for each of these group towers. In fact it is equivalent to their being **pro-zero**. Every actual map from each suspension of `A_r` is phantom, so surjectivity onto the inverse limit in the same Milnor sequence makes that inverse limit trivial. For a countable Mittag–Leffler tower, its eventual images are reached by the inverse limit; those images must therefore be trivial. Conversely pro-zero plainly implies (P3).

This reduction locates exactly the missing uniformity: for every `t` and finite source stage `n`, one needs a later stage `m` such that **every** map `Σ^{t+1}(A_r)_m→Z_r` restricts trivially to stage `n`, uniformly over the arbitrarily large finite target subwedges through which such a map factors. Finite-target Miller nullity gives no such uniform `m` as the target subwedge grows.

The opened original Gray–McGibbon, *Universal phantom maps*, Topology **32** (1993), 371–394, §1 and Theorem 1, supplies exactly the telescope quotient above. Its Example 4.1 and proof give vanishing of phantoms from torsion-homology sources into targets with finitely generated homotopy groups. Applied in our countable finite-type source setting, that theorem excludes a finite-type replacement of the target in this phantom program. It does **not** establish (P3): `H_{r+4}(Z_r;Z)` already has infinitely many `Fp` summands, so `Z_r` is not of finite type. We use only the countable inverse-tower form of the Mittag–Leffler criterion; no uncountable inverse-limit assertion is needed here.

### A necessary finite-type target test for the wedge program

The pro-zero condition has a useful consequence which prevents the infinite wedge from hiding a simpler missing test. Put `Y_r=Σ^{r+2}B`, so `Y_r=colim_iΣ^{r+2}B_i`. Then

\[
\operatorname{Map}_*(A_r,Z_r)\simeq *
\quad\Longrightarrow\quad
\operatorname{Map}_*(A_r,\Omega Y_r)\simeq *.
\tag{P4}
\]

Here is a direct proof. Fix `s≥1` and a map `f:Σ^s A_r→Y_r`. For a finite source stage `n`, choose the later stage `m` given by pro-zero of `[Σ^s(A_r)_j,Z_r]`. The restriction of `f` to stage `m` has finite image and therefore factors through some `Σ^{r+2}B_i`. Include this factor as the `i`th summand of `Z_r`. Its restriction to stage `n` is null by pro-zero; retracting to that summand shows that the original restriction of `f` is null in `Y_r`. Thus `f` is phantom. Its source has torsion integral homology, and its target is a simply connected space of finite type, so Gray–McGibbon Example 4.1 makes `f` null. This holds for every `s≥1`, which is precisely (P4), including the components of the pointed mapping space into `ΩY_r`.

The loop-suspension unit `Σ^{r+1}B→ΩΣ^{r+2}B` is essential: it is an isomorphism on the first nonzero homotopy group by Freudenthal, and that group is `Fp`. Consequently a proof of the left-hand side of (P4) would automatically furnish the simpler finite-type separating target `ΩΣ^{r+2}B`. Neither side of (P4) has been proved. This is a necessary-condition reduction, not a claim that the looped suspension is `A_r`-null and not an inference from its being of finite type.

### Additional primary checks on the phantom program

Iriye's original *Stable suspension order of universal phantom maps and some stably indecomposable loop spaces*, J. Math. Soc. Japan **59** (2007), 97–112, was obtained from the publisher's J-STAGE PDF. Its Theorem 1.1 and proof, Corollary 1.2 and proof, and the definitions in §1 were read. Corollary 1.2 gives infinite **strong stable suspension order** for the universal phantom out of the nontrivial finite Postnikov space `B=K(Fp,2)`. Suspending its telescope construction preserves that spectrum-level order, so it confirms and strengthens the stable essentiality used above. The paper carefully distinguishes the colimit of finite-suspension homotopy sets from maps of suspension spectra; the natural comparison need not be injective. Neither notion by itself supplies the missing `A_r`-nullity of `Z_r`. Its Theorem 2.1 gives a stable splitting criterion, not a nullification computation. The separately identified Iriye 2000 *Universal phantom maps out of loop spaces* original remains unobtained: the apparent publisher PDF redirects to its abstract/access page.

Schwass's original *On phantom maps into co-H-spaces*, Algebraic & Geometric Topology **17** (2017), 847–867, §2.1.1, Corollary 2.1 and Theorem 2.2, supplies the countable mapping-tower formulation and the exact countable Mittag–Leffler criterion used in (P3). Its results on phantom targets in §1 and its rational comparisons in §2.1.2 retain finite-type target hypotheses. They do not give `A_r`-nullity of the infinitely repeated low-dimensional torsion in `Z_r`.

Kihara's original *Groups of homotopy classes of phantom maps*, Algebraic & Geometric Topology **18** (2018), 583–612, was opened and downloaded. Theorem A, Definitions 2.1 and 2.2's ambient category, and the classes `A,B,A',B'` preceding Proposition 2.5 were inspected. In particular, the calculations with infinite-loop domains are in `CW^op × N`, where `N` consists of **nilpotent spaces of finite type**. The target class `B` consists of nilpotent finite complexes, classifying spaces of compact Lie groups, and their iterated loop spaces; it does not include the wedge `Z_r`. Kihara's *Phantom maps and rational homotopy* (2021), Theorems 1.2 and 1.4, has the same target category `N`, even though its domain restriction is broader. Both its author preprint and the published repository PDF were obtained after an earlier repository 429 response. Thus these sources genuinely go beyond finite-dimensional targets, but the finite-type condition still prevents their application to (P3). No finite-type replacement of `Z_r` can detect the torsion-homology source by an essential phantom, by Gray–McGibbon Example 4.1.

For an independent primary discussion of this universal phantom target, McGibbon–Møller, *Connected covers and Neisendorfer’s localization theorem*, §1, Question 6 and its subsequent discussion, explicitly use the target `∨ΣX_i`; their criterion is cited to their reference [11]. Their discussion was opened. The argument above avoids needing that criterion.

## 7. A.4 and size arguments: limits of the current attack

The new A.5 finite-support class is not a fundamental localizer in the relative-Theorem-A sense and is not a shortcut to a reversible fundamental example. Taking its fundamental/reversible closure changes the class.

Ohkawa-style set results concern smash-Bousfield equivalence classes. They do not automatically imply that all localizing kernels, or all reversible localizers with one fixed stable part, form a set. A uniform accessibility rank for the latter collection has not been proved. Conversely, proper-class families of ordinary unstable nullity classes cannot simply be declared distinct after reversible closure or after imposing a fixed stable part.

For the primary interval in A.4, Levy's *The spectral Sullivan conjecture*, arXiv:2510.00262v1, Theorems 1.5 and 3.2 (opened), strengthen the infinite-loop input. They do not by themselves produce a strict intermediate reversible localizer. Root is auditing the exact consequences of this source separately.

### 7.1. Neisendorfer localization and stabilization fibres: an excluded source family

**Attempt.** Use the fibre `F` of the infinite suspension `K→QK`, where `K` is finite and simply connected with torsion `π2K`, to retain an unstable map into a finite target while removing its stable class.

**Opened result and exact exclusion.** McGibbon–Møller, *Connected covers and Neisendorfer’s localization theorem*, Fund. Math. **152** (1997), 211–230, Theorem 7.2, states `(P_BCp F)^∧p≃K^∧p`. Its Theorem 7.1 and proof make clear that this is the natural comparison induced by `F→K`. Thus, when `K^∧p` is noncontractible, the map `F→K` is essential: a null map could not become that equivalence. On the other hand its suspension-spectrum map is zero, since it becomes zero after the unit `Σ∞K→Σ∞QK`, and that unit has the counit as a retraction. This is a real unstable/stable difference, but it is not the required one. By the rechecked REVLOC D.2.10, an essential map from `F` to the finite simply connected `K` implies

\[
F(\Sigma^\infty F,\mathbb S)\ne0.
\]

Consequently `Σ∞F` is not in `L_p`, which has zero sphere-valued dual on every object. The tempting stabilization-fibre candidate therefore fails the stable-membership half of (G1). The analogous connected-cover construction is excluded in the same way whenever the comparison to the finite target is essential.

**Access distinction.** McGibbon’s separate original, *Infinite loop spaces and Neisendorfer localization*, Proc. AMS **125** (1997), 309–313, DOI `10.1090/S0002-9939-97-03744-1`, was identified but **not obtained**: both the publisher PDF and abstract page returned HTTP 403, including an ordinary direct download of the PDF. The theorem above is explicitly stated in the opened paper coauthored by McGibbon; the proof of the infinite-loop input in the separate original was not read. This is recorded as an access gap, not hidden behind its abstract.

The opened Costoya–Scherer–Viruel author manuscript, *A Torus Theorem for homotopy nilpotent groups*, §2, Remark 2.1, independently makes the functor distinction precise. Their idempotent `L` is localization at `BCp→*` together with a universal mod-p homology equivalence. Nullification followed by p-completion computes it in their stated special cases; in general the two operations must be iterated. Their use of McGibbon therefore cannot be silently substituted for the ordinary uncompleted `P_A` in (G1) or (G2). The stronger ordinary primary infinite-loop acyclicity already available from Bousfield/Levy still does not evaluate the general unstable gate.

## 7.2. A distinct converse-Miller attack and an explicit false separator

We investigated whether a source invisible to spheres or to nilpotent finite complexes, with p-primary reduced integral homology, must already belong to the reversible class generated by `BCp`. Here a **Miller source** means a space `X` with `Map_*(X,K)≃*` for every nilpotent finite complex `K`. This is Strom's convention. It is not the convention in the introduction of Castellana–Crespo–Scherer, *On the homotopy groups of p-completed classifying spaces*, where a “Miller space” is a **target** `Y` satisfying `Map_*(BCp,Y)≃*`. Confusing these directions would turn the desired conclusion into an unrelated source theorem. Nor does “finite” mean every finite complex without a fundamental-group restriction: the example below is finite and has an essential identity map.

There is an explicit counterexample to the **ordinary**, unsuspended converse. It does not decide A.4. Let `A` be the exact Higman presentation complex already proved noncontractible and integrally acyclic in D.5:

\[
\pi_1A=\langle a,b,c,d\mid
a^{-1}bab^{-2},\ b^{-1}cbc^{-2},\ c^{-1}dcd^{-2},\ d^{-1}ada^{-2}\rangle.
\]

There is one vertex, four one-cells and four two-cells. The boundary matrix in D.5 has determinant `−1`; hence its reduced cellular complex is contractible. The amalgam normal-form proof in D.5 proves `π1A≠1` without assuming asphericity. We read that proof and the contraction argument reused in A2.8. No new unverified group-theoretic example is required here.

**Why `A` is a Miller source.** The group `π1A` is perfect. Its image under any homomorphism to a nilpotent group is both perfect and nilpotent, hence trivial. A based map from `A` to a nilpotent finite `K` therefore lifts to the simply connected universal cover of `K`. Since `A` is two-dimensional, its homotopy classes of maps into a simply connected target are classified by `H^2(A;π2K)`, which is zero: the displayed integral cellular contraction works with every abelian coefficient group. Thus `[A,K]_*=*`. Also `ΣA` is simply connected and integrally acyclic, hence contractible by Hurewicz and Whitehead. All higher homotopy groups of `Map_*(A,K)` vanish for this reason. This proves the full mapping-space assertion, not only its set of components.

**Why ordinary nullification misses this source.** Since `A` is finite-dimensional, Miller's Theorem A makes `A` a `BCp`-null target. Consequently `P_BCp A≃A≠*`. Now put `X=A∨BCp`. The product formula for pointed mapping spaces makes `X` a Miller source, and

\[
\widetilde H_*(X;\mathbb Z)\cong
\widetilde H_*(BC_p;\mathbb Z),\qquad
P_{BC_p}X\simeq A\ne *.
\]

The nullification assertion follows directly from its universal property: the collapse `A∨BCp→A` is a `BCp`-equivalence, and `A` is already null. Thus the example has **nonzero** p-primary homology; it is not merely the degenerate homologically zero case.

**Exact reason it fails the reversible gate.** We have `ΣX≃ΣBCp`, because `ΣA≃*`. Ordinary `BCp`-acyclic spaces are closed under pointed homotopy colimits and hence suspension. Therefore

\[
P_{BC_p}(\Sigma X)\simeq *.
\tag{M1}
\]

The exact criterion A34.1 puts `X` inside `Rev(BCp)`. Equivalently, the collapse `X→BCp` is an integral-homology equivalence, and every reversible fundamental localizer already contains `W_Z`. The ordinary counterexample is erased for the precise structural reason required by A.4.

**Source distinction.** The same finite acyclic-source idea appears in Strom's original preprint *Miller Spaces and Spherical Resolvability of Finite Complexes*, the unnumbered Example on p. 3 after Corollary 3. Its PDF's character extraction is garbled, so that page was opened as an image and read. The example is absent from the published 2003 article; we do not attribute it to a nonexistent example number there. The explicit model and the complete proof above use D.5 and the already opened Miller theorem. This is an exclusion of a proposed route, not a new decision of A.4 or a priority claim.

## 7.3. Completed classifying spaces and the limits of source recognition

The finite-group completion family is also excluded, this time by an exact ordinary nullification calculation. The **published original** of Flores, *Nullification and cellularization of classifying spaces of finite groups*, Trans. AMS **359** (2007), 1791–1816, was opened through the author's linked copy. Proposition 3.14, pp. 1804–1805, states

\[
P_{BC_p}\bigl((BG)^\wedge_p\bigr)\simeq *
\qquad\text{for every finite group }G.
\tag{M2}
\]

The proof was read. It first handles the simply connected p-completed classifying space by mapping into the universal cover of an arbitrary null target and its arithmetic comparison. For general `G`, the covering associated to the maximal p-perfect normal subgroup has a simply connected fibre of the preceding kind and a finite p-group base; both are `BCp`-acyclic, so their extension is acyclic. The same proposition separately proves `((P_BCp BG)^∧p)≃*`; these two differently ordered assertions must not be conflated. Formula (M2) is already stronger than the suspended vanishing needed for reversible membership.

The later Castellana–Flores author preprint *Homotopy idempotent functors on classifying spaces*, arXiv:1210.7772, Proposition 5.2 and Remark 3.15, gives another route: for finite `G`, `P_BCp((BG)^∧p)≃((BG)^∧p)_Q≃*`. Both passages and the proof of Proposition 5.2 were opened. The preprint's Theorem 4.1 is printed with different completion typography in its introduction and main statement, and the proof of Proposition 4.11 contains an unqualified acyclicity phrase for p-compact toral classifying spaces where the surrounding argument is about mod-p comparison. We have not repaired those passages by assumption. The finite-group exclusion (M2) uses Flores's published Proposition 3.14, so it is independent of those editorial issues. The published final Castellana–Flores PDF was requested from the AMS; its exact access outcome is recorded in the retrieval output and source ledger.

Strom's published 2012 Theorem 2 supplies a useful **sufficient source criterion**: for a finite-type CW complex with `H̃^*(X;Z[1/p])=0`, reduced `H^*(X;Fp)` and injectivity of `H^*(X;Fp)⊗J(n)` for every `n≥0` imply nullity of the indicated odd-sphere mapping spaces. Theorem 1 then gives nullity for simply connected finite-dimensional targets. The theorem and its finite-type hypotheses were read. It is not a converse, does not assert that all Miller sources have injective cohomology, and does not construct them cellularly from `BCp`. Likewise the published 2003 Corollary 11 recognizes the source property by mapping to spheres; its resolving-class theorems construct **targets** from spheres by limits and fibrations. Neither theorem identifies the class of Miller sources with the acyclic class generated by `BCp`.

The currently missing implication in this distinct route is therefore still precise: one would need either a proof that every p-primary Miller source has `P_BCp(ΣX)≃*`, or a specified source for which that suspended nullification is noncontractible. Ordinary nonacyclicity is insufficient, as (M1) verifies concretely. No general converse cellular-generation theorem was located and proved in this run. The absence of such a theorem from the searched sources is not a claim that none exists in the literature.

### Further exact exclusions in this route

Dwyer–Wilkerson's original *Spaces of null homotopic maps*, Astérisque **191** (1990), 97–108, was obtained and its Theorems 1.1–1.3 and 3.2 were read. The first two keep a locally finite group as source and concern the **constant component** of the mapping space into a simply connected p-complete target. Theorem 1.2 assumes finite-type mod-p cohomology and locally finite indecomposables. It does not assert that all components vanish, nor that these targets are Miller sources. Theorem 3.2's converse at `p=2` is a converse between target cohomology and this constant-component assertion; it is not the converse needed for A.4. These precise restrictions prevent two tempting reversals of the result.

Flores–Muro's *Torsion homology and cellular approximation*, author preprint arXiv:1707.07654v2, §5, Propositions 5.3–5.4, gives a different source family with nontrivial ordinary `BCp`-nullification: the classifying space of the two-generator free Burnside group of prime exponent `p>665`. The same section explicitly records a nonzero countably generated free abelian Schur multiplier. It therefore fails the required p-primary **homology** premise, despite its fundamental group having exponent p. The underlying Schur-multiplier computation is quoted there from Olshanskii, whose original was not opened in this run; no independent group-theoretic proof is claimed. No source-Miller property for these Burnside groups has been proved here either.

The same paper's Proposition 4.8 proves group cellularity for the first Grigorchuk group and the Gupta–Sidki group, using their Schur multipliers. It does not establish cellularity or acyclicity of their **classifying spaces**, much less the simultaneous source-Miller and suspended nonacyclicity properties required here. The paper itself leaves a related amenable p-torsion classifying-space acyclicity question open immediately before that proposition. We do not transfer group-colimit constructions through `B` as if they were homotopy-colimit constructions of spaces.

### A Moore-smash reduction for the new smash-generator route

**M3 (proved, under the stated accessibility hypothesis).** Let `W` be an accessible reversible fundamental localizer, let `Y` be a connected space with p-primary reduced integral homology, and let `M=M(Fp,1)` be the cofiber of the degree-p map of the circle. Then

\[
Y\text{ is }W\text{-aspherical}
\quad\Longleftrightarrow\quad
M\wedge Y\text{ is }W\text{-aspherical}.
\tag{M3}
\]

Here all spaces may be represented by pointed CW complexes; the smash products and telescope are derived. For the forward implication, the aspherical class of `W` is closed under pointed homotopy colimits and hence under smash product with a fixed pointed space. For the converse, there is a cofiber sequence

\[
\Sigma Y\xrightarrow{p\wedge1_Y}\Sigma Y
\longrightarrow M\wedge Y.
\]

Reversibility's cofiber criterion makes the first map a `W`-equivalence. Form its sequential homotopy telescope `T`. Accessibility gives the required homotopy-colimit closure, so the canonical map `ΣY→T` is a `W`-equivalence: compare the constant diagram on the first stage with the telescope diagram using the iterates of the displayed map. Reduced integral homology commutes with this telescope, and its transition homomorphisms are multiplication by p. Thus

\[
\widetilde H_*(T;\mathbb Z)
=\widetilde H_*(\Sigma Y;\mathbb Z)[1/p]=0.
\]

Every reversible fundamental localizer contains the integral-homology localizer, so `T` is `W`-aspherical. Hence `ΣY` is `W`-aspherical, and reversible suspension reflection makes `Y` aspherical. The self-map used here is the degree-p map on the **circle factor** of `S^1∧Y`. It is not identified with the suspension of an H-space p-power map on `Y`; those are distinct assertions.

Apply (M3) to `C=BCp`, `B=K(Fp,2)`, and `A=C∧B`. The proposed witness `X=M∧B` lies outside `minRev(A)` if and only if `B` itself does. Thus the exact proposed separation is

\[
B\notin\mathcal A_{\min\operatorname{Rev}(BC_p\wedge B)}.
\tag{G4}
\]

The stable tensor-ideal comparison in the root's proposal does not decide (G4). Bousfield 1997 §4.5 was opened: it supplies the nullity order, its obvious finite smash operation, and the composition relation for ordered nullifications. It does **not** there assert a smash-cancellation or smash-idempotence theorem. Bousfield 1996 Theorems 3.4–3.5 classify the indicated finite-complex nullities; neither theorem applies directly to the infinite complexes `BCp` and `B`. The candidate was subsequently excluded by A34.3 below; the Moore-smash reduction itself is not an A.3 decision.

### The smash-generator candidate is excluded (A34.3)

The full independent proof is now `sections/A34_reduction.tex`, **A34.3**. A subsequent complete read found that the supplied REVLOC **D.2.37** already proves the same exclusion, and **D.2.39** proves its generalization to every `C∈Rev(BCp)`. The new proof uses the published stabilization-cofiber estimate rather than the original algebraic-theory/Segal argument. This is a re-proof of that background result, not an unresolved-row refinement. It proves

\[
\min\operatorname{Rev}(BC_p\wedge K(\mathbb F_p,2))
=\min\operatorname{Rev}(K(\mathbb F_p,2)),
\qquad P_{BC_p\wedge B}(\Sigma^2B)\simeq *.
\]

The new primary input is Chachólski–Farjoun–Flores–Scherer, *Cellular properties of nilpotent spaces*, published Geometry & Topology **19** (2015), Propositions 3.1(1),(2) and 3.4(11), read in the published original. They imply that `B` is `ΣBCp`-cellular, that `B∧B` is `Σ(BCp∧B)`-cellular, and that the cofiber of `Z→ΩⁿΣⁿZ` is `Z∧Z`-cellular for every connected `Z`. Taking a sequential homotopy colimit preserves this cellularity and gives the cofiber of `Z→QZ`; no inverse-limit closure is assumed. Thus the cofiber `K` of `ΣB→QΣB` is `A`-cellular for `A=BCp∧B`.

The proof supplies the stable tensor-ideal comparison explicitly: Levy Theorem 1.5 gives `loc(Σ∞BCp)=loc(S/p)`; smash with `Σ∞B`, and use the cofibers of multiplication by `p^m` and the telescope whose homology is localized at p. It then reproves the needed connective spectral-nullification consequence of Bousfield 1996 Theorem 2.6 in degree 3, with the exact lower and upper connectivity bounds. Theorem 2.10 consequently gives `P_A(QΣB)=*`. In the rotated cofiber sequence `QΣB→K→Σ²B`, the first two terms are ordinarily A-acyclic; hence so is the third. Reversible desuspension puts B in the class generated by A. The other inclusion is smash closure.

This excludes the proposed `M(Fp,1)∧B` witness. It is **not** substantive stopping-rule movement: none of the requested open A.3/A.4 decisions has changed. REVLOC D.2.39 also proves the accessibility-free form of (M3), by expressing `Σ²Y` as the telescope of the cofibers of iterated degree-p maps, each built from `M∧Y`. Both its proof and D.2.37 were read in full in this run. The next distinct question is whether the stabilization-cofiber argument can control the square `B∧B` inside the classes generated by `QΣ^rB`; that inclusion has not been assumed.

### The remaining square test for the free infinite-loop candidates

The complete D.2.1–D.2.61 exclusion index and the report's current D.2 gate were read before further variants were pursued. In particular D.2.37/D.2.39 already exclude all the indicated `BCp` smash constructions, D.2.11 excludes the realized periodic Lie targets, D.2.35 excludes fixed finite Postnikov invariants as a general cone-preservation argument, and D.3.8 gives the countable family classification for primary infinite-loop presentations. No stronger conclusion is inferred from these index summaries than from the cited proved statements.

**M4 (proved equivalence, not a decision).** Put `A_r=QΣ^rB` and `W_r=minRev(A_r)` as before. Then

\[
 B\in\mathcal A_{W_r}
 \quad\Longleftrightarrow\quad
 B\wedge B\in\mathcal A_{W_r}
 \quad\Longleftrightarrow\quad
 P_{A_r}\bigl(\Sigma^{r+1}(B\wedge B)\bigr)\simeq *.
\tag{M4}
\]

The first forward implication is smash closure. Conversely set `Z=Σ^rB`. The cofiber of `Z→QZ=A_r` is `Z∧Z=Σ^{2r}(B∧B)`-cellular by the homotopy-colimit version of CFFS2015 Proposition 3.4 proved in A34.3. If `B∧B` is `W_r`-aspherical, that cofiber is aspherical; since its middle term `A_r` is aspherical, reversible cofiber reflection makes `Z` aspherical, and suspension reflection makes `B` aspherical. The last equivalence is the exact bounded-suspension formula A34.2, applied to `B∧B`. For `r=0`, `B` is already a retract of `QB`; the unresolved cases start at `r=1`.

This test does not supply the square inclusion. The facts that `Σ∞(B∧B)∈L_p` and that every finite Postnikov stage of a sufficiently suspended square is ordinarily `A_r`-acyclic do not imply the displayed vanishing. Passing from those stages to their inverse limit would repeat the established convergence gap. The Snaith splitting also gives stable summands, not an ordinary retraction from `A_r` to a suspension of the square. The earlier D.2.12 obstruction to an unstable retraction of the stabilization unit cannot by itself rule out a construction through arbitrarily many nullification cones.

The same cofiber argument gives a useful conditional filter for further proposed generators. If `W` already kills all sufficiently connected infinite-loop spaces from `L_p`, and `Σ∞X∈L_p`, then `X∧X∈A_W` implies `X∈A_W`: choose a sufficiently large `s`, kill `QΣ^sX`, and apply the cofiber estimate to `Σ^sX`. Here the infinite-loop premise must actually be established, for example by the supported-primary spectral argument; it is not an axiom asserted for arbitrary localizers. Iterating shows that, under that premise, any positive smash power of such an `X` can be aspherical only if `X` is. This observation filters proposed variants but supplies no separating space.

### Suspended finite-group targets do not separate the square gate

**M5 (auxiliary exclusion, proved).** Let `X` be a pointed space such that `F(Σ∞X,S)=0` as a mapping spectrum. For every finite group `G` and every integer `s≥1`,

\[
\operatorname{Map}_*(X,\Sigma^s BG)\simeq *.
\tag{M5}
\]

In particular this applies to every `Σ∞X∈L_p`. These targets are generally infinite-dimensional. The assertion uses their special finite-group structure, not a dimension estimate. It also applies to any homotopy limit of these targets, since a pointed mapping-space functor preserves homotopy limits.

Here is a complete reduction to the already checked inputs of REVLOC D.2.10. Put `C=coloc(S)`, the full stable subcategory closed under retracts and small homotopy limits generated by the sphere. D.2.10 proves that `Σ∞BH_+∈C` for every finite group `H`, using the completed Segal theorem, tom Dieck splitting, finite transfer and the arithmetic comparison. Its proof, including the integral passage from the finitely many prime completions, was re-read in full. A genuine finite `H`-spectrum has a finite equivariant cell construction, up to retract, from orbit cells. Consequently its homotopy-orbit spectrum belongs to `C`: an orbit cell gives a shift of `Σ∞BJ_+` for a subgroup `J≤H`, and finite cofibers and retracts remain in `C`.

For `Y=Σ^sBG`, the spectrum underlying the nth Goodwillie layer of the identity is

\[
V_n=\bigl(\partial_n I\wedge
       (\Sigma^\infty Y)^{\wedge n}\bigr)_{h\Sigma_n}.
\]

Write `K=G^n⋊Σ_n` for the finite wreath-product group. The natural splitting `Σ∞BG_+≃S∨Σ∞BG` shows that the reduced n-fold smash is a **Σ_n-equivariant** retract of the n-fold smash with disjoint basepoints: the summand in which every factor is reduced is invariant under all permutations. This is an equivariant retract of spectra, not an asserted unstable splitting. Also `(BG_+)^{∧n}=(B(G^n))_+`, with the permutation action. After accounting for the permutation of the `S^s` factors, the unreduced version of `V_n` is

\[
\bigl(\operatorname{inf}^{K}_{\Sigma_n}
       (\partial_n I\wedge S^{s\rho_n})\bigr)_{hK},
\]

where `ρ_n` is the real permutation representation and inflation is along `K→Σ_n`. This identification is the iterated homotopy-orbit formula for the semidirect product; the normal subgroup `G^n` acts trivially on the inflated spectrum. The partition-complex model makes `∂_nI` a genuine finite `Σ_n`-spectrum. Smashing with the representation sphere and inflating along the finite quotient preserve genuine finiteness: each orbit cell inflates to the corresponding finite `K`-orbit cell. The preceding paragraph therefore puts the unreduced orbit spectrum, and its equivariant retract `V_n`, in `C`.

Since `F(Σ∞X,-)` vanishes throughout `C`, adjunction gives `Map_*(X,D_nI(Y))≃*` for every n. Induction up the fibre sequences of the Goodwillie tower gives the same assertion for `P_nI(Y)`. The space `Y` is simply connected because `BG` is connected and `s≥1`; the identity tower therefore converges. Mapping out of `X` preserves its homotopy limit, proving (M5). The only Goodwillie inputs are precisely the layer formula, the finite partition-complex model, and convergence on simply connected spaces already cited and checked in D.2.10. For this new use the primary texts were also opened: Arone–Mahowald 1999 Theorem 2.1 and its finite partition model; Goodwillie 1992 Example 4.3 and proof; Goodwillie 2003 Theorem 1.13 and convergence proof, Proposition 1.18, and §8 pp. 704–705. The Segal input was opened in Bergsaker–Rognes arXiv v2 Theorem 1.1 with its hypotheses and the sphere identification in the introduction; Carlsson 1992 §2(B), §2(D) and Corollary 2.3 were opened for transfer and splitting. Exact access records and bibliography entries are in the companion files.

This excludes a proposed route through suspended finite-group classifying spaces. It does **not** apply by replacing `BG` with the realization `K(Fp,2)`: the relevant realization is an infinite homotopy colimit, while `C` has not been shown closed under such colimits. It does not establish ordinary `A_r`-nullity of the universal-phantom target or of `Σ^{r+1}B`, and it changes none of the requested A.3/A.4 decisions.

### Further source checks on the nonlinear reconstruction

The full statement and proof of D.2.12 were re-read. At `p=2`, every map `ΣA_r→Σ^{r+1}B` has zero bottom mod-2 homology, whereas the suspended stabilization unit is an isomorphism there. Thus even a one-suspension retraction cannot be extracted from the Snaith stable summand. The distinction is exact: the theorem excludes the retraction and controls the first cone attachment; it does not prove that the complete mapping space is contractible or control all subsequent nullification cones. No suspension splitting has been substituted for the missing square membership in (M4).

Gray's published *EHP Spectra and Periodicity. I: Geometric Constructions*, §4, p. 607, was opened as a separate check on this possible shortcut. Its discussion reports Kirley's no-finite-suspension splitting result at the prime 2 and contrasts a conjectural odd-primary double-loop splitting. The Kirley thesis itself was not obtained, and none of that reported theorem is used as a new premise here. The explicit supplied D.2.12 proof suffices for the rejected one-suspension shortcut.

The published abstract of Castellana–Gavira-Romero, *Cellular approximations of infinite loop spaces* (2015), and the repository abstract of Gavira-Romero's 2014 thesis were located. The publisher original and thesis PDF were not obtained: direct repository access presented an access-denied page, and the independent handle resolver returned HTTP 403. The thesis abstract concerns cellularization by `BC_{p^m}`, the Prüfer classifying space, and their products, for spaces satisfying a stated completed `ΣBCp`-acyclicity premise. An abstract with that premise is not a theorem reconstructing `B∧B` from `QΣ^rB`; no such implication is assumed.

Lee's 1992 paper on stable maps from Eilenberg–Mac Lane spaces to classifying spaces remains an exploratory lead for which only indexed metadata or excerpts were obtained. The initial access failure for Chachólski–Dwyer–Intermont's `v_*`-torsion paper was subsequently resolved: the author-uploaded manuscript dated 28 July 2004 was opened as a PDF through ResearchGate. Its exact statements and the limitations of this route are recorded below under (M9). The earlier failed download remains in the chronological ledger; it is no longer the current source-access status. The finite-group target exclusion (M5) continues to use the supplied D.2.10 proof and the independently opened original inputs stated above.

### Nonuniform stabilization: elementary constructions that still collapse

**M6 (auxiliary exclusions, proved).** Failure of a uniform finite suspension bound is not by itself a separator. Let `(X_i,Y_i)` be any small family of pointed pairs such that for each `i` there is a finite integer `n_i` and a pointed equivalence `Σ^{n_i}X_i≃Σ^{n_i}Y_i`. The integers need not be bounded. For every reversible aspherical class `A`, suspension reflection gives `X_i∈A` if and only if `Y_i∈A`. Since a wedge is aspherical precisely when each of its summands is aspherical (homotopy-colimit closure in one direction, pointed retractions in the other),

\[
\bigvee_iX_i\in A\quad\Longleftrightarrow\quad\bigvee_iY_i\in A.
\tag{M6a}
\]

Thus assembling finite-suspension comparisons with unbounded bounds by a wedge does not distinguish the classes, even if no simultaneous finite-suspension comparison has been supplied.

Likewise let `f:X→X` be an actual pointed self-map of a connected CW complex. If `Σ∞f=0`, the standard telescope triangle shows `Σ∞Tel(f)=0`: its first map is `1−s`, and the shift `s` is null. In particular the telescope is integrally acyclic and is killed by every reversible fundamental localizer. If instead `Σ∞f` is an equivalence, then `f` is an integral-homology equivalence, and so is `X→Tel(f)`. This map again belongs to every reversible fundamental localizer. The same argument applies to a sequential diagram of actual stable-equivalence maps. These two commonplace telescope constructions therefore do not exploit the sought distinction between a stable map and a map realizable after one uniform finite suspension.

None of these observations identifies an abstract map of suspension spectra with an actual map of spaces. An abstract stable comparison that lacks a uniform unstable realization remains a possible source of a different construction, but no comparison with the needed nullification behavior has been constructed here.

### Twisted fibrations: the finite-fibre route and a failed infinite-dimensional example

**M7 (auxiliary exclusions, proved).** Put `B=K(Fp,2)` and write `G=ΩB≃BCp`, using a topological group model. If a fibration over `B` has finite-dimensional CW fibre `F`, its monodromy action of `G` is trivial. Levy's original Corollary 3.8 states that an action of an infinite-loop space with torsion positive homotopy groups on a finite-dimensional space factors through its component group. We read the preceding Theorem 3.7 and the action proof: the endomorphism space of the fibre is null for `∨_qBCq`, and the cartesian-monoidal localization gives factorization as an `E_1` action, not merely as a map of underlying spaces. Here `G` is connected, so its component group is trivial. The fibration is therefore fibre-homotopy equivalent over `B` to the product. The homotopy cofiber of its fibre inclusion has the pointed form

\[
\operatorname{Cof}(F\longrightarrow B\times F)
\simeq B\wedge F_+.
\tag{M7a}
\]

This is already in the reversible aspherical class generated by `B`, by smash closure. No finite-dimensional twisting construction of this form gives the desired separator. The result concerns dimension, not the number of cells.

An explicit infinite-dimensional trial shows what still needs to be controlled. Let `F=Σ^uG` be the unreduced suspension with the left translation action on the equator and with both poles fixed. Forgetting the action, the based space `F` is equivalent to `ΣBCp`. Each equivariant cone contracts to its fixed pole, and the equator has contractible homotopy quotient. Taking homotopy quotients of this equivariant pushout gives

\[
E=F_{hG}\simeq BG\vee BG=B\vee B,
\qquad E\longrightarrow BG=B
\text{ the fold map}.
\tag{M7b}
\]

Its homotopy fibre is `ΣG`, also seen directly by pulling the wedge pushout back over `B`: its three fibres are `*←G→*`. This exhibits a nontrivial action on an infinite-dimensional fibre which is `B`-null by (M5). It does not give a candidate for (G1). Indeed `Σ∞E∈L_p`, whereas `Σ∞F∉L_p`: Levy Theorem 1.5 gives `loc(Σ∞F)=loc(S/p)`, which contains a nonzero finite spectrum. If the cofiber of `F→E` had suspension spectrum in `L_p`, the stable cofiber triangle would put `Σ∞F` in `L_p`, a contradiction. Thus the exact trial fails the stable-membership premise.

The still-unproved variation would need an infinite-dimensional action whose stable local system is trivial, together with a proof that its relative cofiber survives the relevant suspended nullification. Stable triviality alone would put that relative cofiber stably in the ideal generated by `B`, but it is not a construction of the required action and is not evidence for its unstable survival. This remains an exploratory gate, not an A.3 or A.4 decision.

### The higher Prüfer candidate: checkpoint-05 comparison gaps

**M8 (proved limited conclusions at checkpoint 05; refined by A34.4 and M10).** Put `D=K(C_{p^∞},2)` and `J_p=loc(Σ∞D)`. The ordinary `B=K(Fp,2)`-acyclic class contains `D`. Indeed the short exact sequences building `Z/p^n` give finite fibration extensions of `B`, and the filtered homotopy colimit of `K(Z/p^n,2)` along subgroup inclusions is `D`. Ordinary acyclic classes are closed under those extensions and homotopy colimits. Consequently

\[
0\ne J_p\subseteq L_p,\qquad J_p\cap\mathrm{Sp}^{\mathrm{fin}}=0.
\tag{M8a}
\]

Nonvanishing follows already from `H_2(D;Z)=C_{p^∞}`. The finite-spectrum assertion follows from `J_p⊂L_p` and A.3's checked sphere-dual argument; it does not require the reverse inclusion.

The space `B` is ordinarily `D`-null: the homotopy groups of `Map_*(D,B)` are the reduced groups `H^{2-i}(D;Fp)` for `0≤i≤2`, all zero. In particular `H²(D;Fp)=Hom(C_{p^∞},Fp)=0`. This distinguishes ordinary nullity but does not distinguish reversible closures. Bousfield 1997 Lemma 8.13, including its divisible-group qualification, says that `D` kills all 2-connected p-primary GEMs: their `π₂` is zero, so the extra requirement is satisfied. The already proved A34.1 therefore gives the exact comparison

\[
\mathcal A_{\min\operatorname{Rev}(D\to *)}
=\{X:P_D(\Sigma^2X)\simeq *\}.
\tag{M8b}
\]

Thus the relevant test on `B` is `P_DΣ²B`, not `P_DB=B`. Its value had not been established at checkpoint 05; A34.4 now proves it is noncontractible. The fibration `B→D\xrightarrow{p}D` alone does not settle it: reversible cofiber closure is not closure under taking the fibre of a map between two aspherical spaces.

The checkpoint-05 attempt to assert `J_p=L_p` had two distinct gaps. The equality is now refuted by A34.4, but both cautions remain valid objections to those attempted shortcuts.

1. **Homological comparison.** Bousfield 1997 Lemmas 10.3–10.4 distinguish the exceptional case at mod-p transitional dimension 2 in which `(E/p)_*K(Z,3)=0`. In that case the divisibility of `π₂D` permits `D` to be acyclic although `B` is not. The source explicitly reports that no spectrum satisfying Lemma 10.4 was known there. Targeted searches before checkpoint 05 found no later resolution; that was only a report of those searches. A34.4 subsequently constructs a spectrum killing `D` but detecting `B`, directly from the cyclotomic-completion counterexample. Its proof does not invoke the classification of exceptional spectra in Lemma 10.4. The acyclicity-level examples in Theorem 10.5 never justified omitting the exception.
2. **Cohomological comparison.** Even agreement of all such smash-homology acyclicities would not by itself prove equality of actual localizing subcategories. A right-orthogonal detector has the form `F(Σ∞D,R)=0` for an arbitrary spectrum `R`. The conversion of cohomological equivalences to homological ones in Bousfield 1997 §2.6 assumes that every group `π_k(R/p)` is finite, for each prime p. No argument reduces an arbitrary detector here to spectra satisfying that hypothesis. The two issues must therefore be kept separate.

The degree-one Prüfer calculation in supplied D.2.14–D.2.15 was reread and does not provide a higher-degree cancellation theorem. It has stable ideal `loc(S/p)`, containing a nonzero finite spectrum. Also, because `D` is already ordinarily `B`-acyclic, adjoining `D` to the generator `B` cannot enlarge `min Rev(B)` and hence cannot by itself produce a strict intermediate element above it in A.4. No requested row is resolved by (M8).

### Further primary-source checks on periodicity and genus

**M9 (route exclusions and source-access corrections).** Chachólski–Dwyer–Intermont's author manuscript was opened in full as a primary PDF. Definitions 1.1–1.9 and Theorem 1.10 use thickness with respect to **fibration** sequences. The realization theorem 1.14 assumes connected degreewise `v_*`-torsion spaces and abelian fundamental groups. Its proof, the adjoining results of §7, the polyGEM discussion in §5, and Theorems 6.1–6.2 with their indicated proofs were read. These hypotheses do not identify the paper's classes with the reversible cofiber-closed classes required here, and no such transfer has been used. The author name is Michele Intermont; the exploratory bibliography has been corrected. Ordinary local PDF retrieval still returned HTTP 403, but the original author manuscript itself was read through the web tool.

Bousfield's *On the telescopic homotopy theory of spaces* (2001), Theorems 6.5–6.6, 6.11 and the proofs in §§6.10–6.11, was obtained and read. Theorem 6.11 constructs, from failure of the height-n stable telescope conjecture, a sufficiently connected infinite-loop space `Y` with zero reduced `E(n)`-homology and nonzero `v_n`-periodic homotopy. The precise construction is `Y=(Ω∞M_n^fE)⟨j⟩`, `j>d_n`. Burklund–Hahn–Levy–Schlank arXiv:2310.17459v1 was subsequently downloaded: Theorem A and the final proof of Theorem 6.25 establish the requisite failure at every prime and height `n≥2`. The full internal proof chain of that 101-page preprint has not been independently re-proved here.

This supplies actual periodic examples but does not give the desired A.4 intermediate element. The construction is p-local and its rationalization is zero: `M_n^fE` is the fibre of `L_n^fE→L_{n-1}^fE`, whose two rationalizations agree for `n≥1`. Thus the connected infinite-loop space `Y` has p-primary homotopy groups. Levy's already opened Theorem 3.2 makes it ordinarily `BCp`-acyclic. Adjoining it to `BCp` therefore does not enlarge that reversible class. Nor has its suspension spectrum been shown to generate an ideal with no nonzero finite spectra; vanishing of `E(n)` alone would not prove that property. This excludes the proposed immediate application, not every possible use of the stable telescope counterexamples.

Møller–Scherer, *Localization genus* (2017), was also obtained and read at Proposition 1.1 and its proof, the precise quoted Neisendorfer theorem 5.1, Proposition 5.2, and Theorem 5.4 with their proofs. Its Postnikov and completion genera provide possible sources of nonuniform comparisons, but the checked statements do not exhibit an actual pair having the same suspension spectrum and different reversible asphericity with zero finite stable part. The finite-type and connectivity assumptions have not been discarded. Powers and simultaneous products from a fixed set are handled by the separately proved A4.3; their bounded representative argument is not being duplicated or counted again here.

Root independently re-proved (M5)–(M7), reopened their listed primary inputs, and accepted these auxiliary exclusions. Its exact check events are in `notes/A3_root_checks.tsv`. They do not change the A.3 or A.4 status.

### A strict stable separation for the higher Prüfer candidate

**M10 (proved as A34.4; not a resolution of A.3).** For every prime `p`, set `B=K(Fp,2)` and `D=K(C_{p^∞},2)` as in (M8). Then

\[
0\ne J_p\subsetneq L_p,
\qquad
\min\operatorname{Rev}(D\to*)\subsetneq
\min\operatorname{Rev}(B\to*),
\qquad
P_D\Sigma^kB\not\simeq *\quad(k\ge0).
\tag{M10a}
\]

The full proof, with all maps and hypotheses, is Claim A34.4 in `sections/A34_reduction.tex`. Here is its source and detector chain. Work internally in `C=Sp_T(2)`, with tensor `U⊗_CV=L_T(2)(U∧V)`; do not identify this with ordinary smash. CSY *Ambidexterity in chromatic homotopy theory* arXiv v3 Theorem 5.3.1 and *Ambidexterity and Height* v2 Theorem 4.4.5 give infinite semiadditivity of height 2. Write `R_r=1[ω_(p^r)^(2)]` and `R_∞=colim^C R_r`, using Definitions 4.7 and 4.10 of CSY *Chromatic cyclotomic extensions*, arXiv v2.

Take the `BP⟨1⟩` and the `Z`-action specified in BHLS Convention 5.1 and Theorem 5.4. Theorem 6.25 at `n=1,k=0` gives the actual non-equivalence

\[
c:L_{T(2)}K(BP\langle1\rangle^{h\mathbb Z})
\longrightarrow
\bigl(L_{T(2)}K(BP\langle1\rangle)\bigr)^{h\mathbb Z}.
\]

It is the cyclotomic-completion map. BHLS §1.1 identifies this as `R_∞`-localization, so its fibre `F` is nonzero and `F⊗_CR_∞=0`. CSY Proposition 4.11's proof, before the comparison with `B³Z_p`, splits the actual multiplication-by-`p` map on `1[D]` as projection with complementary summand `R_∞`. It follows that `p` is an equivalence on `F⊗_C1[D]`. Set the **ordinary spectrum** `E_p=T(2)∧F`. Then `p` is an ordinary equivalence on `E_p∧Σ∞_+D`. The telescope of multiplication by `p` on `D` is contractible, because every element of the Prüfer group is killed by a power of `p`. Hence `E_p∧Σ∞D=0`.

CSY Proposition 4.5 with `r=1` identifies `L_T(2)Σ∞B` with `R_1`, and Proposition 4.9(2) makes `R_1` faithful in `C`. Thus `E_p∧Σ∞B≠0`. The kernel of ordinary smash with `E_p` is a localizing subcategory, so this is an actual strict separation of `J_p` from `L_p`, not merely a comparison of chromatic profiles. It also detects every suspension of `B`, proving all the nonvanishing nullifications in (M10a). The detector `E_p` is a spectrum; no ring structure is asserted or used.

The four originals were opened and downloaded; precise versioned locators and access qualifications are in `notes/A3_source_ledger.tsv`. BHLS Theorem 6.25 and its final proof, §1.1, Convention 5.1 and Theorem 5.4 were read; the full internal proof chain of the 101-page manuscript is not represented as independently re-proved. The precise localizing-ideal conclusion was not located verbatim in the portions opened; it is the deduction proved here from those inputs. This is not a priority claim. Root's independent prior-art search additionally identified Barkan–Heuts–Shi arXiv:2604.10867 and Ravenel's 2026 `gjm-cyc-ext.pdf`; that source review is handled by root and is not silently claimed completed in this note.

Root independently accepted A34.4 after reading CSY Propositions 4.5, 4.9 and 4.11, the height theorem 4.4.5, and BHLS §1.1 and Theorems 5.4 and 6.25, and after re-proving the ordinary-smash and telescope steps. The accepted conclusion remains auxiliary, with no principal-question status upgrade.

The remaining A.3 requirement for the new generator is still

\[
\Sigma^\infty X\in J_p,
\qquad P_D\Sigma^2X\not\simeq *.
\tag{M10b}
\]

The space `B` satisfies the second condition and fails the first. A strict stable comparison therefore does not make `min Rev(D)` non-RT, and it does not create two different reversible localizers with the same stable part. No requested principal row or stopping-rule movement is claimed.

### A universal reduction to one prime

**M11 (proved in A34.5; independently accepted by root).** For every reversible fundamental localizer `W`, with no accessibility premise, set `W_p=W∩R(loc(S/p))` and `W_Q=W∩R(loc(HQ))`. Claim A34.5 proves

\[
T(W_p)=\Gamma_pT(W)=T(W)\cap\operatorname{loc}(S/p),
\qquad
W=\bigvee\bigl(\{W_Q\}\cup\{W_p\}_p\bigr),
\]

and `W_Q` is either `W_Z` or `R(loc(HQ))`. It follows that `W` is RT-fixed if and only if every `W_p` is RT-fixed. Hence A.3 is equivalent to the case of a single prime-primary stable part. This is a reduction of the principal existential problem; the reduced problem remains open.

The key space-level calculation uses `Z=Σ³X`, even when `X` is disconnected. Write `G_p(Z)=fib(Z→Z[1/p])` and `F(Z)=fib(Z→Z_Q)`. These fibers are simply connected. Pinch followed by fold gives actual self-maps of the suspension `Z` whose maps on reduced homology are integer multiplication; their telescopes realize the required arithmetic localizations. Their suspension spectra are exactly the corresponding stable localizations. Ganea's theorem makes the two fibrations actual cofiber sequences: the comparison fibers are `G_p(Z)*ΩZ[1/p]` and `F(Z)*ΩZ_Q`, and the joins are contractible by integral Künneth and the disjoint primary/rational supports. Finally the **canonical** maps `G_p(Z)→F(Z)` give a wedge equivalence, because their suspension spectra give `∨_p Γ_pΣ∞Z≃Γ_torΣ∞Z`, and both spaces are simply connected. No full product of primary localizations is used.

These facts establish the pointwise membership test

\[
X\in\mathcal A_W
\iff
Z_Q\in\mathcal A_W\ \text{and}\ G_p(Z)\in\mathcal A_W\text{ for every }p.
\]

Given a hypothetical original witness `g∈RT(W)\W`, take `X=C(g)`. The rational term is aspherical, so at least one of the named spaces `G_p(Σ³C(g))` is not. Its simplex-category collapse is a conditional witness for `W_p`, and its suspension spectrum is in `T(W_p)`. Zero finite part passes to this subcategory. This transfers an assumed witness; it is not an actual unconditional witness for A.3.

**Exact source correction.** The published author PDF of May–Ponto has two incorrect sentences on printed p.128 immediately before Proposition 6.6.4, and root checked visually that they are not extraction errors. A suspension pinch `δ:Z→Z∨Z` has each projection composed with `δ` equal to the identity. The fold composed with `δ` represents twice the identity, not the identity as the printed co-H definition states. Also copowers do not act by the same scalar on every unstable homotopy group: a degree-`r` map of `S²` acts by `r²` on `π₃(S²)≅Z`. A34.5 uses neither sentence. The telescope conclusion needed here follows independently from the action on **reduced homology**, simple connectivity, and the fully opened Theorems 6.1.1–6.1.2. The unchanged valid conclusion of Proposition 6.6.4 is cited with this correction made explicit. Chataur–Scherer's published Proposition 3.4 and its indicated proofs through Proposition 2.3 and Corollary 3.3 were opened in full; no abstract or unverified general fiber-closure assertion is substituted.

### The integral degree-three candidate and two supporting calculations

**M12 (auxiliary arithmetic calculation; no separate A.3 decision).** Let `A=K(Z,3)` and `D_p=K(C_{p^∞},2)`. The exact coefficient sequence `0→Z→Z[1/p]→C_{p^∞}→0` gives

\[
D_p\longrightarrow A\longrightarrow K(\mathbb Z[1/p],3).
\]

This is also a homotopy cofiber sequence. Indeed the Ganea comparison fiber is `D_p* K(Z[1/p],2)`, and its reduced homology vanishes by Künneth because the first factor has p-primary homology and the second has `Z[1/p]`-module homology. The join is simply connected. The base is the telescope of multiplication by `p` on the Eilenberg–Mac Lane space `A`, so it is aspherical for `min Rev(A)`. Reversibility therefore gives `D_p∈A_minRev(A)` for every prime. Likewise `K(Q,3)` is a telescope of `A`. The rationalization fibration

\[
K(\mathbb Q/\mathbb Z,2)\longrightarrow A\longrightarrow K(\mathbb Q,3)
\]

is a cofiber sequence by the same support calculation. The torsion fiber is the wedge of its primary factors: the canonical wedge map `∨_p D_p→K(Q/Z,2)` is an integral homology equivalence between simply connected spaces, by the finite-product Künneth calculation and passage through the weak product. Consequently

\[
\min\operatorname{Rev}(A)
=\bigvee\bigl(\{\min\operatorname{Rev}(K(\mathbb Q,3))\}
\cup\{\min\operatorname{Rev}(D_p)\}_p\bigr),
\]

and

\[
\operatorname{loc}(\Sigma^\infty A)
=\operatorname{loc}\bigl(H\mathbb Q,\{\Sigma^\infty D_p\}_p\bigr).
\]

The second equality follows either by taking suspension spectra in these cofiber constructions or by the arithmetic localization argument. For the latter comparison, the reduced suspension spectrum of `K(Z[1/p],3)` is p-invertible: multiplication by p is an integral homology isomorphism of that bounded-below spectrum, hence an equivalence by stable Hurewicz. The induced map `(Σ∞A)[1/p]→Σ∞K(Z[1/p],3)` is likewise an integral homology isomorphism between bounded-below spectra and hence an equivalence. The rational spectrum `HQ` is present because the rational homology of `A` is nonzero and rational spectra split by their graded rational homotopy groups. Smashing with `S/p` gives precisely `J_p`: it kills the rational generator and all other primary generators, while `loc((Σ∞D_p)/p)=J_p` by the primary reconstruction proved next. Thus a finite spectrum in `loc(Σ∞A)` has zero smash with every `S/p`, because A34.4 places each `J_p` in a zero-finite-part ideal. Such a finite spectrum is rational and hence zero (its finitely generated homology groups would be uniquely divisible by every prime). This mixed ideal is nonzero and has no nonzero finite spectra. Its proposed new generator does not separate from the previously considered rational and Prüfer generators: the unstable inclusion is proved, not left as a p-completion assumption. No fixedness verdict for it is claimed by this paragraph.

For completeness, the bounded-below Moore transfer originally requested for this route has a short direct proof. Put `M=S/p`. In the Moore triangle `S --p→ S --i→ M --q→ ΣS`, the endomorphism `p_M` factors as `a q`, because `p_M i=0`, while `q p_M=0` by the next triangle map. Hence `p_M²=0`, including at `p=2`. If a bounded-below spectrum `C` is `HF_p`-acyclic and `Y=M∧C` were nonzero, choose its first nonzero homotopy group `π_nY`. Stable Hurewicz gives `H_n(Y;Fp)=π_nY/pπ_nY`. This is nonzero: `p²π_nY=0` and `π_nY=pπ_nY` would force it to vanish. But `HF_p∧Y=0`, a contradiction. Thus every bounded-below `HF_p`-equivalence is an `S/p`-equivalence. No claim for arbitrary unbounded spectra is made.

Finally, for any spectrum `E` with `E[1/p]=0`, the objects `E/p^n` are built by finite extensions of `E/p`, and their telescope, with maps induced by the squares having identity on the source and multiplication by `p` on the target, is the cofiber of `E→E[1/p]`, namely `ΣE`. Hence `loc(E)=loc(E/p)`. This is the primary reconstruction used above. The cofiber sequence already proves the Prüfer inclusion directly, so the Moore transfer is a verified supporting lemma rather than a hidden substitute for an unstable argument.

## 8. Source access and reproducibility

A compact claim-by-claim access ledger is `notes/A3_source_ledger.tsv`; the associated exploratory bibliography is `notes/A3_attempt_references.bib`. These distinguish theorem statements actually opened from the McGibbon original whose publisher access failed. Exact numbered reductions and their independent check events have separate metadata in `notes/A34_reduction_results.csv` and `notes/A34_reduction_checks.tsv`.

Opened primary URLs:

- Miller 1984: `https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture.pdf`.
- Strom 2012: `https://www.impan.pl/shop/en/publication/transaction/download/product/88690`.
- Strom 2003: `https://www.impan.pl/shop/publication/transaction/download/product/88494`. The earlier copy from Paris had garbled extraction; the publisher copy resolves that access issue.
- Hopkins–Ravenel: `https://www.sas.rochester.edu/mth/sites/doug-ravenel/mypapers/harm.pdf`.
- Christensen thesis: `https://math.mit.edu/~hrm/thesis/christensen-thesis.pdf`.
- Bousfield 1996: `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf`.
- Levy 2025: `https://arxiv.org/pdf/2510.00262`.
- Allen Yuan 2022: `https://arxiv.org/pdf/2208.12844`.
- McGibbon–Møller: `https://bibliotekanauki.pl/articles/1205441.pdf`.
- Bousfield 1997: `https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf`.
- Costoya–Scherer–Viruel: `https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CostoyaSchererViruel_2015.pdf`.
- Strom finite-acyclic-source preprint: `https://www.math.univ-paris13.fr/~schwartz/FIMFA/MillerSpaces.pdf` (p. 3 read visually).
- Flores published 2007 original: `https://630d8d70-6fa8-4ac2-a19f-246ebe964ec3.filesusr.com/ugd/b82155_12a8f6e62ec34c9fbcd8b8ca25d7547a.pdf`.
- Castellana–Flores author preprint: `https://arxiv.org/pdf/1210.7772`.
- Castellana–Crespo–Scherer: `https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CCSBGcompleted.pdf`.
- Dwyer–Wilkerson published original: `https://www.numdam.org/item/AST_1990__191__97_0.pdf`.
- Flores–Muro author preprint: `https://arxiv.org/pdf/1707.07654`.
- Chachólski–Dwyer–Intermont author manuscript: `https://www.researchgate.net/profile/W-Dwyer/publication/227315003_n-torsion_spaces_and_thick_classes/links/53e112af0cf2235f352728a4/n-torsion-spaces-and-thick-classes.pdf`.
- Bousfield 2001: `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-telescopic.pdf`.
- Burklund–Hahn–Levy–Schlank v1: `https://arxiv.org/pdf/2310.17459`.
- Carmeli–Schlank–Yanovski, *Ambidexterity in chromatic homotopy theory*, v3: `https://arxiv.org/pdf/1811.02057`.
- Carmeli–Schlank–Yanovski, *Ambidexterity and Height*, v2: `https://arxiv.org/pdf/2007.13089`.
- Carmeli–Schlank–Yanovski, *Chromatic cyclotomic extensions*, v2: `https://arxiv.org/pdf/2103.02471`.
- May–Ponto, author-hosted final proof PDF: `https://math.uchicago.edu/~may/PAPERS/116.pdf`.
- Chataur–Scherer, published original: `https://ems.press/content/serial-article-files/43077`.
- Marcum, published original used as a discovery cross-check for Ganea: `https://msp.org/pjm/1981/95-1/pjm-v95-n1-p12-s.pdf`.
- Møller–Scherer 2017: `https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/MollerScherer_LocGenus_PubMat2016.pdf.pdf`.

Local reads include the complete proofs of REVLOC D.2.7–D.2.9, D.3.5 and G.7, and the indicated Prüfer/CP-infinity comparisons. Primary numerical claims in this note are theorem numbers, not numerical experiments. There is no certificate program purporting to decide an infinite nullification calculation.

Searches included these literal query families:

- `Bousfield nullification K Z p 2 acyclic suspension stable acyclic Eilenberg Mac Lane spaces`
- `Bousfield K(Z/p,2) nullification suspension acyclic class stable homotopy`
- `Miller spaces stable cohomotopy infinite wedge spheres nullification`
- `stable Sullivan conjecture infinite wedge spheres Eilenberg Mac Lane space phantom maps`
- `Strom Miller spaces spherical resolvability finite complexes pdf infinite wedge`
- `Miller spaces finite dimensional spheres arbitrary wedges phantom map spaces`
- `"same suspension spectrum" "nullification"`
- `"stably equivalent" "acyclic classes" spaces`
- `"suspension spectrum" "nullity" "Bousfield"`
- `nullity classes spaces proper class set Ohkawa nullification`
- `acyclic classes spaces set Bousfield nullity classes proper class`
- `retract cofiber closed classes spaces Ohkawa theorem set localizations`
- `"Miller spaces" "acyclic"`, `"Miller space" "nullification"`, `"Miller spaces" converse BZ`
- `"same n-type" "nullification"`, `"same n-type" "acyclic"`, `"same n-type" "suspension spectrum"`
- `"phantom" "nullity classes"`
- `"phantom maps" "wedge" "rationally trivial"`
- `"Suspension spectra are harmonic" Hopkins Ravenel pdf`
- `"nullification" "infinite loop" "suspension"`, `"QX" "nullification"`
- `"infinite loop spaces" "co-H-spaces" maps`, `"BZ/p" "suspension" "null" phantom`
- `"Stable suspension order" Iriye pdf`, `"Universal phantom maps" "loop spaces" Iriye pdf`
- `"phantom maps" "infinite loop spaces" McGibbon torsion`, `"universal phantom" "nullification"`
- `"Groups of homotopy classes of phantom maps" pdf`, `"Phantom maps and rational homotopy" Kihara pdf`
- `"Miller spaces" "acyclic"`, `"Miller space" "cellular"`, `"Miller spaces" "converse"`
- `"Sullivan conjecture" "converse" nullification`, `"Miller spaces" "nullification"`, `"spheres" "BZ/p-acyclic"`
- `"Miller" "spherical" "cellular" homotopy`, `"contractible" "mapping spaces" "cellular" "converse" Sullivan`
- `"nullification" "p-completion" "finite group" contractible`, `"BZ/p" "BG" "acyclic" completion`
- `"Homotopy idempotent functors on classifying spaces" pdf`, `"Nullification and cellularization of classifying spaces of finite groups" pdf`
- `"Classifying spaces with injective mod p cohomology" Henn`, `"reduced injective" "spaces" Lannes Schwartz realization`
- `"Miller spaces" "Higman"`, `"Miller space" "simply connected"`, `"sphere codes" Strom nullification`
- `"BZ/p-acyclic" "fibre"`, `"BZ/p-acyclic" "loop"`, `"nullification" "stabilization" "BZ/p"`
- `Grigorchuk group "Sullivan" "maps"`, `Grigorchuk "nullification"`, `"Miller" "torsion groups" homotopy`
- `"Bousfield" "nullity" "smash"`, `"nullity" "smash products"`, `"Localization and periodicity in unstable homotopy theory" pdf`
- `"loop space" "smash" "nullity"`, `"acyclic" "smash" "loop space" Farjoun`, `"QΣ" "nullification"`
- `"nullification" "infinite loop spaces" suspension`, `"nullity" "QX"`, `"cellular" "QX" "smash"`
- `"Cellular approximations of infinite loop spaces" pdf`, `"v*-torsion spaces" "thick classes" pdf`
- `"Cellular approximations of infinite loop spaces" theorem`, `"Castellana" "Gavira" "Theorem" "infinite loop"`
- `"maps from" "infinite loop spaces" "suspensions"`, `"infinite loop spaces" "co-H-spaces" homotopy`
- `"On stable maps from Eilenberg-MacLane spaces to classifying spaces"`, `"Snaith splitting" "one suspension"`
- `"Snaith splitting" "desuspend" suspension`, `"Bousfield" "Theorem 9.10" nullity`
- `"infinite loop spaces" "co-H-spaces" maps null`, `"maps" "infinite loop space" "suspension" null homotopic`
- `"Miller spaces" "suspensions" infinite dimensional`, `"QX" "suspension" "phantom maps"`
- `"infinite loop spaces" "suspensions" "maps" nullity`, `"On phantom maps into suspension spaces"`
- `"phantom fibrations" "stable"`, `"stably trivial" "fibration" "phantom"`, `"phantom" "BAut" "fibrations"`
- `"infinite dimensional" "stably trivial" homotopy fibration`, `"phantom" "fibre homotopy"`, `"phantom fibrations"`, `"phantom" "stably trivial" bundles`
- `"acyclic classes" "desuspension"`, `"nullity" "stably equivalent" spaces`, `"nullification" "same suspension spectrum"`
- `"spaces" "cofibre sequences" "thick classes" nullification`, `"stable nullification" "spaces"`, `"nullity" "suspension spectra" Bousfield`
- `Chacholski Dwyer Intermont v torsion spaces thick classes pdf dwyer`, `"v*-torsion" "pdf"`, `"v∗-TORSION" Chacholski`, `"Dwyer" "Intermont" "thick" pdf`
- `Burklund Hahn Levy Schlank telescope conjecture counterexamples arxiv theorem`, `"K-theoretic counterexamples" "Theorem" telescope`
- `"Bousfield" "Prüfer" "classes"`, `"Eilenberg-MacLane" "localizing subcategory"`, `"Bousfield class" "K(Z" "infinity"`
- `"Bousfield" "transitional dimension"`, `"acyclicity level" spectrum`, `"acyclicity" "K(Z" Bousfield spectrum`
- `"nullification" "Prüfer" "Eilenberg"`, `"nullity" "K(Z" "divisible"`, `"Eilenberg-MacLane" "acyclicity" "Prüfer"`
- `"K(Zp" "nullification"`, `"Prüfer" "nullity"`, `"Eilenberg-MacLane" "nullity classes"`
- `"Miller spaces" "products"`, `"nullification" "infinite products"`, `"Prüfer" "nullification" suspension`
- `"Eilenberg-MacLane" "suspensions" "maps" nullification`, `"Eilenberg-Mac Lane" "suspension" "phantom"`
- `Ganea theorem homotopy fibre cofiber fiber join loop space`, `"cofiber" "localization" "homotopy fiber" nilpotent`, `"homotopy fiber" "F" "join" "Ganea" theorem`
- `Chataur Scherer "Fiberwise localization and the cube theorem" 81 2006`, `May Ponto More Concise Algebraic Topology 6.1.1 localization homology pdf`

No unlocated theorem from these searches has been promoted to a proof. The current result of this independent attack is the exact exclusions and gates above; the existential decision A.3, the strict intermediate-element decision A.4, and the fixed-stable-part set question remain open in this work.

## M13. The chromatic-hole proposal is excluded, without deciding A.3

A proposed primary suspension spectrum with nonzero K(m)-homology but zero K(n)-homology for some 1≤m<n cannot occur. Bousfield, *On K(n)-equivalences of spaces* (1999), Theorem1.1, proves the implication for arbitrary spaces; no finite-type hypothesis is needed. Theorem1.4 makes simultaneous vanishing at all positive heights equivalent to mod-p acyclicity. These constraints exclude this candidate construction, not the normal-form gate: neither chromatic type nor its tail determines the entire localizing subcategory. The already proved strict J_p⊊L_p comparison remains a warning against that substitution. No new A.3 existence or impossibility conclusion follows.

Primary author manuscript: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/AKB-K(n).pdf. The five-page text, including Theorems1.1–1.4, Lemma2.6, Theorem2.7 and Section2 proofs, was opened and downloaded as `sources/A3_Bousfield_1999_Kn.pdf`. Earlier Kuhn–Lloyd introductory references were discovery aids only.

### Additional post-checkpoint06 source scope

Barkan–Heuts–Shi2026, https://arxiv.org/pdf/2604.10867: the actual statements of Theorems1.13–1.14, Theorem3.12, Theorem3.18, and Theorem4.1 were read, together with the Section4.3 proof of Theorem1.13. Its cited earlier lemmas were not all independently reconstructed. The connected loop-localization comparison is cited from Bousfield1997Theorem5.2 in A34.6, whose exact statement was separately reopened. No separator is inferred from this paper's title, abstract, or general periodic comparison.

Additional literal search families in this block:

- `"K(n)-acyclic" "periodic" "spaces"`; `"acyclic" "v_n-periodic" "homology"`; `"v1" "homology" "acyclic" "unstable"`
- `"On periodic homotopy and homology equivalences of spaces"`; `"Shi" "homological and homotopical" localisation`
- `"K(n -1)" "acyclic space" Kuhn`; `"H-space" "K-theory" "acyclic"`; `"H-spaces" "K(1)" "nullification"`; `"H-space" "K(Z/p,2)" null`
- `"bousfield" "1994" "periodicity" "pdf" -site:scispace.com -site:academia.edu -site:researchgate.net -site:portal.mardi4nfdi.de`; `"Homotopy localization nearly preserves" "pdf" Farjoun Smith`
- `May geometry iterated loop spaces approximation theorem 2.7 pdf`
- `"suspension spectrum" "localizing" "finite" cohomotopy`; `"localizing subcategory" "sphere" "orthogonal" spectra finite`; `"Miller spaces" "stable cohomotopy" localizing`
- `spaces "K(n)" "K(n-1)" "acyclic"`; `"chromatic" "acyclic" "spaces" Bousfield`
- `Aguade Smith On mod p torus theorem John Hubbuck 1986 pdf`; `"On the mod p torus theorem"`
- `Bousfield On K(n) equivalences of spaces 1999 pdf theorem all spaces`; `Bousfield On K(n)-equivalences of spaces 1999 85 89`
- `"k(1)" "space" "localizing" spectrum`; `"Morava" "spaces" "localizing subcategory" infinite`; `"suspension spectra" "chromatic type" "localizing"`

The Aguade–Smith original and the 1994 Bousfield original were not obtained through these attempts; their exact access outcomes are recorded in the source ledger. No unlocated theorem is used.
