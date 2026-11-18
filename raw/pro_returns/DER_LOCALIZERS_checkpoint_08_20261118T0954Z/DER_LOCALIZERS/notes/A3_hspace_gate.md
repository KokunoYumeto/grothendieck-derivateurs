# H-space tests for the primary reversible candidates

This is a proof note extending the accepted A4.5 argument to the generators in A.3. It neither supplies a non-RT witness nor replaces stable membership by sphere-nullity. No main-section or principal-register status is changed by this note.

## H1. A bounded ordinary test becomes unsuspended on sufficiently connected H-spaces

Let A be a connected pointed space with p-primary reduced integral homology. Suppose d≥1, A is (d−1)-connected, and ordinary A-nullification kills every d-connected GEM with p-primary homotopy groups. Put W_A=min Rev(A→*). Then for every d-connected H-space H with p-primary reduced integral homology,

\[
 H\in\mathcal A_{W_A}
 \quad\Longleftrightarrow\quad
 P_A\Sigma^dH\simeq *
 \quad\Longleftrightarrow\quad P_AH\simeq *.
\tag{H1}
\]

The first equivalence is A34.1. The forward implication from ordinary acyclicity to its suspension is formal. For the remaining implication put Z=P_AH.

The cone-attachment construction in Bousfield 1996, immediately after Theorem 1.1, preserves d-connectivity: all attaching domains are nonnegative suspensions of the (d−1)-connected A. For d=1, van Kampen gives simple connectivity. For higher d, van Kampen and the cofiber homology exact sequence preserve vanishing through degree d, then the Hurewicz theorem gives the required connectivity. The same sequence preserves homology over Z[1/p], so Z remains primary. Transfinite homotopy colimits preserve these conclusions. Nullification preserves finite products (Bousfield 1996, proof of Theorem 1.7), so Z is an H-space.

The nullity of Z implies that of every iterated loop space of Z. Thus the unit H→Z and the hypothesis give an equivalence of full mapping spaces

\[
 \operatorname{Map}_*(\Sigma^dZ,Z)
 \simeq\operatorname{Map}_*(Z,\Omega^dZ)
 \simeq\operatorname{Map}_*(H,\Omega^dZ)
 \simeq\operatorname{Map}_*(\Sigma^dH,Z)
 \simeq *.
\]

Suppose inductively that Map_*(Σ^jZ,Z) is contractible for 1≤j≤d. Apply **Bousfield 1996, Key Lemma 1.6, p.35** with V=Σ^{j−1}Z and target Z. Its precise hypotheses hold: V is connected, Z is a connected H-space, and Z is ΣV-null. It identifies Map_*(V,Z) with Map_*(SP^∞V,Z). The Dold–Thom description on the same source page makes SP^∞V a d-connected primary GEM. It is A-acyclic by hypothesis, and Z is A-null, so this last mapping space is contractible. Descending to j=1 proves Map_*(Z,Z) contractible. In particular id_Z is nullhomotopic, so Z is contractible. This proves (H1), with components as well as positive mapping-space homotopy groups controlled.

This argument does not commute P_A with suspension, does not use inverse-limit closure of an acyclic class, and does not require a bound on torsion exponents or a countability assumption.

## H2. Exact null H-space form of the stable-versus-reversible candidate gate

Under the hypotheses of H1, set L_A=loc(Σ^∞A). Then the following are equivalent:

1. W_A is not RT-fixed.
2. There is a noncontractible d-connected primary H-space Z such that Z is A-null and Σ^∞Z belongs to L_A.

The implication from (2) follows immediately from (H1): stable membership puts Z in the RT-aspherical class; A-nullity and noncontractibility prohibit ordinary A-acyclicity, and hence prohibit W_A-asphericity.

Conversely choose a pointed space X in the RT-aspherical class but outside the W_A-aspherical class. Such an X can be taken as the homotopy cofiber of a witnessing categorical map. Since L_A is primary, X has primary reduced integral homology; its reduced H_0 is therefore zero, and X is connected. Put

\[
 H=J(\Sigma^dX)\simeq\Omega\Sigma^{d+1}X.
\]

James's reduced product construction and theorem (the exact original already opened for A4.5) make H a d-connected H-space. Its filtration has successive cofibers (Σ^dX)^{∧r}. Localizing subcategories of spectra are tensor ideals, and are closed under cofibers and homotopy colimits. Thus Σ^∞H belongs to L_A. The same filtration shows that H has primary homology.

The suspension-loop adjunction triangle exhibits Σ^{d+1}X as a homotopy retract of ΣH. Therefore W_A-asphericity of H would, by suspension, retract closure, and repeated reversible desuspension, imply W_A-asphericity of X. It follows that H is not W_A-aspherical. Equation (H1) implies P_AH is noncontractible. Set Z=P_AH. Its connectivity, primary homology and H-space structure were checked in H1. The cone-attachment construction starts from H and attaches cofibers built from nonnegative suspensions of A. Its suspension spectrum therefore remains in L_A throughout, including the transfinite homotopy colimit. This proves (2).

No countability assertion is made about Z. The construction only uses its actual stable membership, not chromatic vanishing or nullity against spheres.

## H3. The specific generators

The exact GEM input is **Bousfield 1997, Lemma 8.13, p.1341**: for n≥2 and a nonzero p-torsion abelian group G, K(G,n) kills every (n−1)-connected generalized polyGEM with p-torsion homotopy groups, with the extra condition π_nY/pπ_nY=0 when G/pG=0.

- For B=K(F_p,2), take d=1. There is no exceptional divisibility condition. Thus min Rev(B) is not RT-fixed if and only if there is a noncontractible simply connected primary B-null H-space Z with Σ^∞Z∈L_p. This replaces the previously proved one-suspension ordinary test by an unsuspended test on this H-space domain.
- For D=K(C_{p^∞},2), take d=2. The exceptional condition is satisfied because a 2-connected GEM has π_2=0. D is 1-connected, as needed for preservation of 2-connectivity. Thus min Rev(D) is not RT-fixed if and only if there is a noncontractible 2-connected primary D-null H-space Z with Σ^∞Z∈J_p. The strict separation J_p⊊L_p from A34.4 remains essential: B itself fails this membership requirement.
- For A_r=QΣ^rB, the exact hypotheses already checked in A34.2 give d=r+1. That argument's killed GEM range and the (r+1)-connectivity of A_r allow the same statement in connectivity d. This is an application, not a new computation of the stable ideal of A_r.

The d=1 case with A=BC_p recovers the ordinary/reversible comparison in A4.5. It does not strengthen A4.6's finite generation hypothesis. The finite Steenrod-algebra generation exclusion is already proved in `sections/A4_hspace_review.tex`, Claim A4.6, from the published Castellana–Crespo–Scherer Theorem 7.2. It is not duplicated here and is not silently applied to A-nullity for B or D.

## Exact checks and source scope

The full statements and indicated proof paragraphs of Bousfield's Key Lemma 1.6 and Lemma 8.13 were reread in the obtained primary PDFs during this deduction. All three inputs have existing bibliography entries: `ABousfield1996`, `ABousfield1997`, and `A4James1955`. The James original and passage to countable CW complexes were independently opened in the accepted A4.5 audit; this note uses the same general reduced-product filtration and equivalence, without a new access claim for that original.

Schematization independently checked the B and D desuspension steps in a message on 2026-11-18 before this full writeup: it identified the two successive applications V=ΣZ and V=Z for D, and verified 2-connectivity through cone attachments. A separate root audit of this full general H1–H2 note has not yet been requested or claimed. The principal existence question A.3 remains open.

The universal application, including single infinite-loop generation and accessibility, is now written in `sections/A34_reduction.tex`, A34.6. Independent root audit was requested after writing; no acceptance is presumed in this note.
