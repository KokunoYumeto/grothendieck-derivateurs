# Finiteness constraints on the H-space gate

## Proved exclusion: finite generation as an unstable algebra

Let p be a prime. Suppose H is a simply connected H-space with p-primary reduced integral homology, and suppose Map_*(H,S^n_(p)) is contractible for every n≥2. If H*(H;F_p) is finitely generated **as an algebra over the Steenrod algebra A_p**, then

\[
                         P_{BC_p}H\simeq *.
\]

Consequently a countable H-space separator in A4.5 cannot have this algebraic finiteness property. A noncontractible primary sphere-null BC_p-null H-space Z cannot have it either. This is stronger than excluding ordinary Noetherian mod-p cohomology, but does not exclude all spaces with degreewise finite-dimensional mod-p cohomology.

### Proof

Put Z=P_BCp H. The exact imported theorem is **Castellana–Crespo–Scherer, Deconstructing Hopf spaces, published Theorem 7.2**: for a connected H-space X whose mod-p cohomology is finitely generated as an algebra over A_p, P_BCp X has finite total mod-p cohomology. The theorem does not require that X be p-complete. It gives an N such that H_n(Z;F_p)=0 for n>N.

A4.5 proves that Z is simply connected, primary and sphere-null. The integral-to-mod-p universal coefficient sequence surjects

\[
 H_{k+1}(Z;\mathbb F_p)\twoheadrightarrow
 \operatorname{Tor}_1^{\mathbb Z}(H_k(Z;\mathbb Z),\mathbb F_p)
 =H_k(Z;\mathbb Z)[p].
\]

For k≥N the left side is zero. Every nonzero p-primary torsion group contains an element of order p, so H_k(Z;Z)=0 for k≥N. Thus the integral reduced homology is bounded above. No finite generation of the integral groups is needed; this handles divisible p-primary groups as well.

If the reduced integral homology is nonzero, let d be its highest nonzero degree and set A=H_d(Z;Z). Simple connectivity implies d≥2. The cohomology universal coefficient theorem and the exact sequence

\[
 0\longrightarrow\mathbb Z_{(p)}\longrightarrow\mathbb Q
 \longrightarrow\mathbb Q/\mathbb Z_{(p)}\longrightarrow0
\]

give

\[
 H^{d+1}(Z;\mathbb Z_{(p)})
 \cong\operatorname{Ext}^1(A,\mathbb Z_{(p)})
 \cong\operatorname{Hom}(A,\mathbb Q/\mathbb Z_{(p)})\ne0.
\]

The last nonvanishing follows by mapping a nonzero cyclic subgroup of A into the p-primary Prüfer group Q/Z_(p) and extending the map by injectivity of that divisible group. Hom(A,Q)=0 because A is torsion, and Ext(A,Q)=0 because Q is injective; these justify the middle isomorphism for arbitrary A.

Choose a nonzero class c, hence a pointed map Z→K(Z_(p),d+1), the bottom Postnikov section of S^(d+1)_(p). The universal coefficient theorem also gives H^r(Z;B)=0 for every abelian coefficient group B whenever r>d+1. At each successive stage of the simply connected sphere's Postnikov tower, the obstruction to lifting the chosen map lies in a group H^(k+2)(Z;π_(k+1)S^(d+1)_(p)), with k≥d+1, and hence vanishes. Choose lifts successively in fibration models, including their compatibility. Postnikov convergence yields a map

\[
                           Z\longrightarrow S^{d+1}_{(p)}
\]

whose bottom Postnikov class is c. It is not null, contradicting sphere-nullity. Therefore Z has zero reduced integral homology. Since it is simply connected, the homological Whitehead theorem gives Z≃*, as required.

This proof is the bounded-integral-homology obstruction already recorded in `notes/A4_new_routes.md` §4, applied to the nullification whose mod-p cohomology is controlled by the newly opened theorem.

## What the finiteness theorem does not give

1. **Finite type is insufficient for this deduction.** The hypothesis is finite generation as an unstable algebra, not merely finiteness of each H^n. The published introduction, Theorems 5.3 and 5.5, and Theorem 7.2 keep these conditions distinct. No theorem reducing every countable A4.5 candidate to this finitely generated subfamily has been proved.
2. **No filtration by suitable H-subspaces was established.** Presenting an unstable algebra as a union of finitely generated unstable subalgebras does not realize those subalgebras by H-subspaces that remain primary and sphere-null. Cohomology is contravariant, so even the direction of such a realization would need proof. This is the precise failure of a proposed finite-generation extension.
3. **Local finiteness alone is weaker.** For a BC_p-null H-space with the relevant finite-type hypotheses, the Lannes–Schwartz criterion provides local finiteness as an unstable module. A locally finite unstable module or algebra need not be finite dimensional without finite generation. No comparison with ordinary acyclicity follows from that algebraic observation alone.
4. **The source condition is essential.** Primary simply connected BC_p-null H-spaces can be nontrivial, so primary homology and target nullity alone do not prove the desired contraction. At p=2, take the homotopy fibre F of rationalization S³_(2)→S³_Q≃K(Q,3). Rationalization preserves products, so this is a fibre of H-maps and F is an H-space. The homotopy exact sequence gives π₂F=Q/Z_(2), π₃F=0 and π_kF=π_kS³_(2) for k>3. Serre's finiteness theorem, already opened for A4.4, makes the latter finite 2-groups, so F is simply connected and primary. Both sphere S³_(2) and rational K(Q,3) are BC₂-null; therefore their homotopy fibre is too. It is nontrivial already on π₂. Its map F→S³_(2) is nonnull, for example on π₄=Z/2, so it fails the source condition. This example illustrates why the proof explicitly uses sphere-nullity, rather than an Euler-characteristic argument that would be invalid for divisible integral homology.

## Exact primary-source and access record

**Published original obtained and used:** Castellana, Crespo and Scherer, *Deconstructing Hopf spaces*, Inventiones Mathematicae 167 (2007), 1–18, DOI 10.1007/s00222-006-0518-8. Publisher-layout PDF hosted by an author institution: <https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CCSdeconstructingPublished.pdf>. Opened as `turn530352763view0`; Theorem 7.2 and complete proof were read at `turn611877533view0`. The preceding Lemma 7.1 and the supporting Theorem 6.1 proof using André–Quillen homology were also read, at `turn855521131view0`.

**Earlier author version also opened, not used in place of the final proof:** <https://mat.uab.cat/~natalia/articles/Deconstruct-L9.pdf>, `turn918846788view0`. Its corresponding theorem is numbered 6.4. The published introduction explicitly acknowledges repair of an earlier proof by André–Quillen methods; accordingly the published Theorem 7.2 and its final supporting argument are used here, and the preprint numbering is not cited in the formal result.

**Additional scope source opened:** Castellana–Crespo–Scherer, *On the homotopy groups of p-completed classifying spaces*, author PDF <https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CCSBGcompleted.pdf>, `turn918846788view2`. Introduction and Section 2's Lemma 2.1, Proposition 2.2 and Corollary 2.3 with proofs were read. Their local-finiteness statements address BC_p-null targets or their loops. They do not imply that every sphere-null source in A4.5 is acyclic. This paper is not an input to the proof above.

**Failed access:** the IEC conference PDF <https://publicacions.iec.cat/repository/pdf/00000506/00000006.pdf> timed out (`turn918846788view1`). No theorem from that inaccessible version is used.

**Searches:** `"H-space" "Miller" "nullification"`; `"locally finite" "cohomology" "Miller spaces"`; `"H-spaces" "sphere-null"`; `"locally finite" "cohomology" "maps to spheres"`; `"BZ/p-local" "spheres" "source"`; `"BZ/p-null" "maps" "finite complexes" "H-space"`. The term “Miller space” repeatedly denotes the target condition in these sources, whereas A4.5 also imposes the source condition. No unrestricted vanishing theorem or explicit separator was obtained.

## Completion and an unsuccessful extension route

Costoya–Scherer–Viruel's author original *A torus theorem for homotopy nilpotent groups* was reopened at <https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CostoyaSchererViruel_2015.pdf>, `turn740771061view0`. Section 2, Remark 2.1, distinguishes the actual localization that kills BC_p and inverts all mod-p homology equivalences from the composite `(P_BCp(-))^∧_p`. The latter is not generally idempotent, even for p-good spaces. This source and distinction are already recorded in the A.3 attempt ledger; the present rereading supplies no new result. We do not use the composite as a reflector to close the H-space gate.

A proposed extension from finite Steenrod-algebra generation to mere local finiteness would need to realize the finitely generated subalgebras by suitable H-spaces, or to prove that every relevant BC_p-null H-space is obtainable from finite targets by homotopy limits. Neither assertion was established. Brown–Gitler searches supplied stable realization statements with different variance and do not provide finite unstable targets detecting these sources. The attempted direct opening of Grodal's *The transcendence degree of the mod p cohomology of finite Postnikov systems* at <https://web.math.ku.dk/~jg/papers/postnikov.pdf> timed out (`turn580269907view0`); no theorem from that unopened original is used. These failures leave the unrestricted H-space criterion unresolved.
