# Finite unstable-algebra generation is excluded for the L_p H-space gate

## FG1. Statement

Let p be prime and let A be a primary generator with the connectivity and GEM-killing hypotheses in A34.6. Let Z be a d-connected primary H-space which is A-null and is sphere-null in the sense used in A4.6. If H*(Z;F_p) is finitely generated as an algebra over the Steenrod algebra, then Z is contractible.

In particular, a nonzero H-space separator for A=K(F_p,2), with Σ∞Z∈L_p, cannot have this finiteness property. More generally it excludes the A34.6 witnesses for any A whose stable ideal is already known to be left orthogonal to the sphere spectrum. It does **not** assert that having no finite spectrum in L_A alone implies this orthogonality.

## Proof

A4.6 applies to the primary sphere-null H-space Z and gives P_BCp Z≃*. The published Castellana–Crespo–Scherer *Deconstructing Hopf spaces*, Lemma7.1 and Theorem5.5, identify the actual homotopy fibre of Z→P_BCp Z as a p-torsion H-Postnikov piece. Lemma7.1 supplies a finite Krull-filtration stage and the finite-type Lannes-T hypotheses from finite generation of the unstable algebra. Theorem5.5 gives only finitely many nonzero homotopy groups, each a finite direct sum of cyclic p-groups and Prüfer groups. Since the base is contractible, Z itself is that Postnikov piece. No p-completion replacement is made in this step.

The d-connectivity and primary homotopy place Z in the range killed by A: the precise Bousfield1997 Lemma8.13 argument from A34.6 handles both the nondivisible bottom group and its extra-degree divisible exception. Thus P_AZ≃*. But Z is A-null, so Z≃P_AZ≃*.

For the particular stable ideal L_p=loc(Σ∞K(F_p,2)), the already rechecked stable-Miller argument in REVLOC D2_stable_miller.tex gives sphere-nullity from Σ∞Z∈L_p. The proof never claims that P_BCp Z remains in L_p; it only needs sphere-nullity during that auxiliary nullification and the resulting Postnikov description.

## Source and check scope

The publisher-layout original at https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CCSdeconstructingPublished.pdf was reopened. Read Theorem5.4 and proof, Theorem5.5, Lemma7.1 and proof, Theorems7.2–7.3 and proof (printed pp.10–11,15–16). Existing bibliography key: A4CCSDeconstruct2007; no duplicate is added. Schematization independently reopened these exact statements and confirmed the argument and its fibre identification. The earlier preprint numbering is not used.

This is an exclusion of an additional concrete witness class. It decides neither unrestricted A.3 nor the L_p gate. Finite type alone is not excluded.

## FG2. Universal exclusion after requiring two loop structures

**Scoped corollary of the A34.6 normal form, independently accepted by root and schematization and integrated in A34.6.** Let A,d satisfy the general hypotheses of A34.6.4, with d≥1. Suppose Z is a d-connected primary A-null space which is the loop space of a connected H-space. If H*(Z;F_p) is finitely generated as an unstable algebra, then Z≃*. In particular, every nonzero witness Z_m in the normal form with m≥2 has mod-p cohomology that is not finitely generated as an unstable algebra. The same assertion applies to the actual double-loop representatives constructed there. There is no sphere-nullity hypothesis and no inference that zero finite stable part implies sphere orthogonality.

### Full proof

Write Z≃ΩU for a connected H-space U and put Y=P_BCp Z. Bousfield1997 Theorem5.2 gives the actual equivalence

\[
Y\simeq\Omega P_{\Sigma BC_p}U.
\]

Nullification preserves finite products, so P_{ΣBCp}U is again a connected H-space. Consequently Y is itself the loop space of an H-space, with the required coherences furnished by this delooping. The cone construction of P_BCp preserves simple connectivity because BCp is connected: starting from the simply connected Z, the cones on its nonnegative suspensions introduce no one-dimensional cells. It preserves reduced homology over Z[1/p], because BCp is primary. Therefore Y is simply connected and has p-primary reduced integral homology.

By CCS published Theorem7.2, Y has finite total mod-p cohomology. Hemmi, *Higher homotopy commutativity of H-spaces and the mod p torus theorem* (1991), Theorems1.1 and2.2, applies for every prime: a loop space on an H-space is a quasi-C_infinity space, and a simply connected quasi-C_p space with finite mod-p cohomology has zero reduced mod-p cohomology. Thus H~*(Y;F_p)=0. This application uses the actual theorem with a finite **cohomology** hypothesis, not a finite-CW assumption and not a p-completed substitute.

For each k, the homological universal coefficient sequence surjects H_(k+1)(Y;F_p) onto H_k(Y;Z)[p]. Every nonzero p-primary torsion abelian group has an element of order p, including the divisible case. Hence all reduced integral homology groups of Y vanish. Simple connectivity and the homological Whitehead theorem give Y≃*.

CCS Lemma7.1 supplies an integer r with QH*(Z;F_p) in the rth Krull stage and the finite-type hypotheses for all relevant Lannes-T functors. Their Theorem5.5 identifies the **actual fibre** of Z→P_BCp Z as a p-torsion H-Postnikov piece with only finitely many nonzero homotopy groups. Since Y≃*, Z itself is that Postnikov piece. Its d-connectivity means all of its nonzero Eilenberg–Mac Lane stages are d-connected primary GEMs. A kills each such stage by hypothesis, and finite fibre-extension closure of ordinary A-acyclicity makes P_AZ≃*. The assumed A-nullity now gives Z≃P_AZ≃*, as claimed.

### Source audit

Hemmi's published original was opened and downloaded from https://msp.org/pjm/1991/149-1/pjm-v149-n1-p05-p.pdf. Theorems1.1 and2.2, the proof of Theorem1.1 in Section4, and the proof of Theorem2.2 in Section5 were read; Section4's exterior-algebra and primitive-class argument was followed through its stated supporting lemmas. This records a primary theorem import, not an independent reconstruction of every older secondary-operation result on which Hemmi relies. Local file: `sources/A3_Hemmi_1991.pdf`.

Aguadé–Smith, *On the mod p torus theorem of John Hubbuck*, Math. Z.191(1986),325–326, DOI10.1007/BF01164037, was located as the original odd-prime precursor. Springer provided a subscription landing page; the Geodesic/Mathdoc scan request returned502. That original was not obtained and is not used as a separate premise. Hemmi proves the stated all-prime strengthening and explicitly identifies the odd-prime loop-on-H specialization.

The corollary belongs to the same normal-form refinement as A34.6. It supplies no actual nonzero separator, no impossibility theorem without the algebraic finiteness assumption, and no additional stopping-rule movement beyond the hour's already established reduction.
