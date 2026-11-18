# Countable H-space gate for A.4

**Date:** 2026-11-18. **Author/checker:** GPT-6 Astra; inherited effort not reported by runtime; DER_LOCALIZERS/schematization.

**Status:** Complete argument submitted for independent parent audit. This note does not declare a principal question solved and makes no priority claim. It sharpens the existing countable gate by both restricting its quantified domain and replacing suspended ordinary nullification by ordinary nullification on that domain.

## 1. Ordinary and reversible acyclicity agree on simply connected primary H-spaces

Fix a prime p, write C=BC_p and P=P_C, and let H be a simply connected pointed H-space with p-primary reduced integral homology. Then

\[
 P(\Sigma H)\simeq *\quad\Longleftrightarrow\quad PH\simeq *.
 \tag{H1}
\]

By the already independently checked A34.2, this is equivalently

\[
 H\in\mathcal A_{\min\operatorname{Rev}(BC_p)}
 \quad\Longleftrightarrow\quad PH\simeq *.
 \tag{H2}
\]

The reverse implication in (H1) is closure of an ordinary nullification-acyclic class under pointed homotopy colimits, in particular suspension. We prove the other implication without assuming that P commutes with suspension.

Put Z=PH. The nullification construction of Bousfield 1996, Theorem 1.1 and its following paragraph (printed p.34), successively attaches mapping cones on maps from C and its nonnegative suspensions and takes a suitable transfinite homotopy colimit. Every such attaching domain is connected and has zero reduced homology over Z[1/p]. Attaching its cone to a simply connected space preserves simple connectivity by van Kampen. It also preserves homology with Z[1/p] coefficients by the cofiber homology sequence. These assertions persist through the transfinite homotopy colimit and replacement by a CW model. Consequently Z is simply connected and still has p-primary reduced integral homology. There is no hypothesis of a bounded torsion exponent or a bound on the number of cells.

Nullification preserves finite products, as explicitly used in the proof of Bousfield 1996, Theorem 1.7 (printed p.35). Apply P to the multiplication of H, use the canonical equivalence P(H×H)≃PH×PH, and transfer its unit homotopies. Thus Z is an H-space. Associativity beyond that required for an H-space is unnecessary.

The target Z is C-null. Hence ΩZ is C-null too: pointed mapping spaces commute with the homotopy limit defining loops. The mapping-space universal property of H→PH therefore gives

\[
\begin{aligned}
 \operatorname{Map}_*(\Sigma Z,Z)
 &\simeq \operatorname{Map}_*(Z,\Omega Z)\\
 &\simeq \operatorname{Map}_*(H,\Omega Z)\\
 &\simeq \operatorname{Map}_*(\Sigma H,Z)
 \simeq *.
\end{aligned}
\tag{H3}
\]

The final equality uses the hypothesis PΣH≃* and C-nullity of Z. These are equivalences of entire pointed mapping spaces, including their components; no assertion is made that PΣH≃ΣPH.

Now use **Bousfield 1996, Key Lemma 1.6**, with its connected source V equal to Z and its connected H-space target also equal to Z. The lemma states: if V is connected and the connected H-space T is ΣV-null, then inclusion into the infinite symmetric product induces an equivalence

\[
 \operatorname{Map}_*(SP^\infty V,T)
 \xrightarrow{\simeq}
 \operatorname{Map}_*(V,T).
 \tag{H4}
\]

Equation (H3) checks precisely the ΣV-null hypothesis here. Consequently id_Z extends up to pointed homotopy along Z→SP∞Z. In other words, Z is a homotopy retract of SP∞Z.

The Dold–Thom description on the same source page identifies SP∞Z as a GEM with homotopy groups H_n(Z;Z). It is simply connected and primary. A34.2, using Bousfield 1997 Lemma 8.13 and the bar construction of K(F_p,2), proves that every such GEM is ordinarily C-acyclic. Ordinary acyclic classes are closed under retracts, so Z is C-acyclic. It is already C-null. Thus its localization unit is an equivalence and PZ≃*, forcing Z≃*. This proves (H1) and (H2).

## 2. The exact countable H-space gate

At p=2 put

\[
 W_0=\min\operatorname{Rev}(BC_2\to *),\qquad
 W_*=W_S\cap W_{\mathbb Z[1/2]}.
\]

The following statements are equivalent:

1. W_0=W_*.
2. PH≃* for every countable simply connected H-space H with 2-primary reduced integral homology and Map_*(H,S^n_(2))≃* for every n≥2.
3. The same assertion holds when H is restricted to reduced products J(ΣX), where X is a countable connected primary sphere-null pointed CW complex.

For (1)⇒(2), every indicated H is W_*-aspherical. Equality puts it in W_0, and (H2) gives ordinary P-acyclicity. The implication (2)⇒(3) uses the explicit construction and properties below. For (3)⇒(1), start with any countable source X in the previous gate A4.2 and let

\[
 A=\Sigma X,\qquad H=J(A)\simeq\Omega\Sigma A=\Omega\Sigma^2X.
 \tag{H5}
\]

Here J is the reduced product of James 1955. Theorem 5.6, printed p.183, and its proof on pp.184–187 establish its equivalence to ΩΣA for connected countable CW complexes. Section 1 describes its multiplication and its cell structure. All hypotheses hold: A is a countable, simply connected, pointed CW complex.

The transfers required by (H5) are as follows.

* **Countability and H-structure.** Its cells are represented by finite words of cells of A. There are countably many such words. Concatenation gives the reduced product its H-space multiplication. Thus this construction retains a countable CW model before any nullification is performed.
* **Simple connectivity.** Σ²X is 2-connected because X is connected. Hence ΩΣ²X is simply connected, and so is J(A).
* **Primary sphere-nullity.** The James filtration has J_0(A)=*, J_1(A)=A, and cofibration quotients J_r(A)/J_(r−1)(A)≅A^∧r. The W_*-aspherical class is closed under suspension, smash with pointed spaces, cofiber extensions, and pointed homotopy colimits. It contains X and therefore A, every A^∧r, every J_r(A), and their sequential homotopy colimit J(A). Thus H is primary and sphere-null. This argument uses actual unstable cofiber sequences; it does not transport an inverse limit through stabilization or invoke a suspension splitting.
* **Retention of a separator.** By the suspension–loop adjunction triangle, the composite

  \[
    \Sigma A\xrightarrow{\Sigma\eta_A}
    \Sigma\Omega\Sigma A\xrightarrow{\epsilon_{\Sigma A}}
    \Sigma A
  \]

  is homotopic to the identity. Thus Σ²X=ΣA is a homotopy retract of ΣH. If H is W_0-aspherical, suspension and retract closure put Σ²X in that class, and reversible desuspension twice puts X in it. Contrapositively, X outside W_0 gives H outside W_0. By (H2), this is equivalent to PH noncontractible.

If (3) holds, PH≃* puts every such H in W_0. The retraction just proved puts every countable X in A4.2 in W_0. A4.2 then gives W_*=W_0. This proves all equivalences. In particular strictness of W_0⊂W_* is equivalent to existence of a **countable simply connected primary sphere-null H-space whose ordinary BC_2-nullification is noncontractible**.

No countability assertion about PH is used. The retained countability is that of H=J(ΣX).

## 3. The restricted domain is proper

The old countable domain contains ΣBC_p. This space is countable, simply connected and primary. It is sphere-null because BC_p is sphere-null by the Sullivan theorem, and the sphere-null reversible class is closed under suspension.

It admits no H-space structure. To see this over F_p, choose nonzero classes a∈H²(ΣBC_p;F_p) and b∈H³(ΣBC_p;F_p). Both groups are nonzero, since the reduced suspension isomorphism identifies them with H¹(BC_p;F_p) and H²(BC_p;F_p), respectively. H¹(ΣBC_p;F_p)=0. If a unital multiplication existed, its pullback on cohomology would therefore make both a and b primitive: the only possible positive-degree decompositions of their degrees involve H¹, which vanishes. All products in positive-degree reduced cohomology of a suspension are zero, so ab=0. But the multiplication pullback is a ring homomorphism, and hence would give

\[
 0=\mu^*(ab)=a\otimes b+(-1)^{2\cdot3}b\otimes a.
 \tag{H6}
\]

The two summands are nonzero and lie in distinct Künneth bidegrees (2,3) and (3,2), a contradiction over every F_p, including p=2. The degreewise mod-p cohomology of ΣBC_p is finite, so the needed Künneth decomposition is valid without a completion issue.

Thus the new test quantifies over a proper subclass of the previous countable source domain, even after restricting the old domain to simply connected spaces. The example ΣBC_p itself belongs to W_0; it establishes strictness of the quantified domain, not a separator.

## 4. Nullifying the H-space also preserves the source conditions

This supplies an additional, possibly uncountable formulation; it is not substituted for the countable gate above. If H is a primary sphere-null H-space, its nullification Z=PH is still simply connected, primary and an H-space by section 1. Every sphere target S used in the test is C-null, and so is Ω^jS for each j≥0. For all such j,

\[
 \operatorname{Map}_*(\Sigma^jZ,S)
 \simeq\operatorname{Map}_*(Z,\Omega^jS)
 \simeq\operatorname{Map}_*(H,\Omega^jS)
 \simeq\operatorname{Map}_*(\Sigma^jH,S)
 \simeq *.
 \tag{H7}
\]

The sphere targets are C-null by the already rechecked Sullivan theorem and its primary localized/completed comparison in A4.2. Thus this argument checks all positive suspensions as well as components. A separator yields a noncontractible simply connected primary H-space Z that is sphere-null as a source and C-null as a target. Conversely any such Z lies outside W_0 by (H2), since PZ≃Z is not contractible. This auxiliary equivalence does not supply a countable CW model for Z or an example of such a space.

## 5. Exact progress and remaining question

The loop–suspension replacement alone would be a normal-form observation valid for many reversible predicates. The additional input here is (H1): it removes the one initial suspension from the ordinary-nullification test **on the H-space domain**, by a mapping-space argument and the symmetric-product retraction. Combined with the countable replacement, it eliminates from the universal test all countable non-H-spaces, while requiring no cardinal enlargement or nullification of a suspension on the surviving test objects. Section 3 verifies that the eliminated subfamily is nonempty.

This is an exact restriction of the existing gate. It does **not** decide whether every surviving H-space is BC_2-acyclic, exhibit a separator, produce a third interval element, or bound the full fibre. The proper-subclass statement concerns the domain of a logically equivalent quantified criterion; it does not assert a strict inclusion between the hypothetical sets of counterexamples, or a priority claim. The parent controls whether the combined restriction and ordinary-versus-reversible comparison meet the stated stopping-rule definition of movement.

## 6. Primary source-opening ledger

* **Bousfield 1996, original opened and reread:** A. K. Bousfield, *Unstable localization and periodicity*, Progress in Mathematics 136, pp.33–50. Author-hosted original <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf>, reference `turn739374038view0`. Printed p.34: Theorem 1.1 and cone-attachment description. Printed p.35: Key Lemma 1.6, its proof referencing [11, Cor.6.9], the Dold–Thom GEM display, and proof of Theorem 1.7 explicitly stating finite-product preservation. The actual Key Lemma statement is transcribed mathematically in (H4). The earlier [11] Corollary 6.9 is not independently opened in this block; the cited 1996 primary theorem itself is the imported result. Existing bibliography key `ABousfield1996` is reused.
* **Bousfield 1997, prior opened original rechecked locally:** *Homotopical localizations of spaces*, Lemma 8.13 and the independently proved A34.2. Existing key `ABousfield1997`. The proof uses exactly the simply connected arbitrary-primary-GEM case, with no finite-rank or bounded-exponent assumption.
* **James 1955, original opened:** I. M. James, *Reduced product spaces*, Annals of Mathematics (2) 62(1), pp.170–197. Original <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/jamesred.pdf>, references `turn581607883view0`, `turn652962587view0`, `turn652962587view1`. Section 1's CW construction and natural multiplication inspected; Theorem 5.6 on printed p.183 and proof on pp.184–187 read, including the passage from finite subcomplexes to countable CW complexes. No full suspension splitting is needed.
* **Prior-art scope:** Parent independently opened the same two key originals and searched for the exact H-space/Miller/nullification gate. No exact prior theorem asserting the displayed countable gate was located. This is an access/search report, not a novelty claim.
