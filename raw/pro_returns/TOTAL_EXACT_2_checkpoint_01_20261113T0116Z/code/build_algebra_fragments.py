"""Write the Part B index and interruption-report fragment from verified results."""
from pathlib import Path
import csv

base = Path(__file__).resolve().parents[1]
work = base / 'work'
rows = [
    ['B.1', 'Every triple of ordinary parallel arrows in every total category has an affine equalizer.', 'Open', 'part_b.tex, label B:triple', 'B.4 (B:lead3)', '', 'Unresolved; this row belongs only to an explicitly INCOMPLETE record. Exact remaining group: T_1(Q_a)=Z/epsilon(L).'],
    ['B.2', 'Lead 1: under totality the R7 surjection T_1(P_q/(K_1+K_2)) to Z/epsilon(K_1 intersection K_2) is a canonical isomorphism.', 'Proved', 'part_b.tex, label B:lead1', 'R1, checked R7, long exact sequences', '', 'Includes the explicit natural alternative quotient isomorphism and acyclicity with zero colimit of J_i.'],
    ['B.3', 'Lead 2: under I exactness is equivalent to affine left annihilation of every augmentation-zero integral arrow combination; the stated one-relation Tor formula needs no hypothesis on A.', 'Proved', 'part_b.tex, label B:lead2', 'IsbellMitchell1976 Theorem 3.1, componentwise common successors', '', 'Includes empty/disconnected categories, zero combinations and empty homsets. Does not infer arbitrary finite families from triples.'],
    ['B.4', 'Lead 3: for arbitrary small A the column module Q_a has the stated canonical derived-colimit groups; with common successors T_1(Q_a)=0 exactly detects an affine equalizer.', 'Proved', 'part_b.tex, label B:lead3', 'Representable projectivity, two long exact sequences', '', 'Includes k=0 and distinguishes the permutation row cokernel from the column cokernel.'],
    ['B.5', 'Lead 4: quasi-filteredness supplies affine equalization for equality in the set colimit; under I exactness is equivalent to affine equalization for equality in the abelian colimit.', 'Proved', 'part_b.tex, label B:lead4', 'IsbellMitchell1976 Lemma 2.2 and Theorem 3.1; direct verification of Proposition 2.3 instance', '', 'The final informal sentence is given its precise fibrewise interpretation in B.6.'],
    ['B.6', 'The canonical set-to-abelian colimit map is surjective under connectedness and common successors; exactness does not imply its injectivity or finite-product preservation of set colimits.', 'Proved / stronger readings refuted', 'part_b.tex, label B:lead4-qualification', 'B.5, checked R3', '', 'Explicit Delta_inj coefficient-pattern counterexample; check_delta_patterns.py and .out supplement the arbitrary-target proof.'],
    ['B.7', 'Lead 5(i)-(iv): the kappa identity, finite parallel-difference normal form, affine-annihilation consequence, kernel of psi and mixed-cycle Tor quotient all hold with the specified hypotheses.', 'Proved', 'part_b.tex, label B:lead5', 'B.2, checked R4 and R7, direct-sum colimit presentation', '', 'One-term sufficiency requires IV, available for total A; graph interpretation uses a multigraph and allows noninjective maps.'],
    ['B.8', 'The mixed-cycle quotient C has the same positive derived-group formulas as Q_a, and its distinguished Tor class maps to kappa; its cycle is a bar cycle with coefficients in C.', 'Proved', 'part_b.tex, label B:mixed-cycle', 'B.7', '', 'No isomorphism C=Q_a and no nonzero ordinary H_1(BA) class are asserted.']
]
path = work / 'algebra_results_fragment.csv'
with path.open('w', newline='') as stream:
    writer = csv.writer(stream)
    writer.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes'])
    writer.writerows(rows)
report = '''# Part B report fragment

This fragment is for an **INCOMPLETE** report. The main triple implication remains undecided; the algebraic checks do not finish Part B as a whole.

| Requested item | Status | Statement labels |
|---|---|---|
| B.1: every triple in every total category has an affine equalizer | Open | B:triple; precise obstruction B:lead3 |
| B.2: Leads 1–5 | Proved in their quantified algebraic form; informal closing language qualified | B:lead1 through B:lead5; B:lead4-qualification; B:mixed-cycle |
| Lead 1 | Proved | B:lead1 |
| Lead 2 | Proved | B:lead2 |
| Lead 3 | Proved | B:lead3 |
| Lead 4 | Proved quantified assertions; stronger interpretations refuted | B:lead4; B:lead4-qualification |
| Lead 5(i) | Proved | B:lead5(i) |
| Lead 5(ii) | Proved | B:lead5(ii) |
| Lead 5(iii) | Proved, with IV stated for its one-term consequence | B:lead5(iii) |
| Lead 5(iv) | Proved; coefficient-cycle interpretation made precise | B:lead5(iv); B:mixed-cycle |

## Verification and source record

The algebra agent read the complete attached prompt, the relevant TOTEX A/B/D proofs, TOTASPH C and the affine criterion in TOTASPH D, and the supplied Isbell–Mitchell (1976) PDF. The source statements used are Lemma 2.2 and Proposition 2.3 on p. 293, Theorem 3.1 on pp. 294–295, Proposition 3.3 on p. 295, the coefficient remark on p. 296, and the explicit finite-bound formulations on pp. 297–298. The needed instance of Proposition 2.3 is proved directly rather than relying on its reader-verification sentence.

R1 is used only through the literal identification of the permutation-module bar complex with the nerve chains of a category of elements. R2 is used with filtered **components** of the affine category. R4 is used with ordinary-span completion and pair affine equalization. R7's row and column kernels are kept separate throughout. No correction to those checked mathematical statements was found in this branch.

## Corrections and qualifications

- Lead 4's precise content concerns affine equalization inside fibres of the canonical set-colimit-to-abelian-colimit map. Exactness does not mean that this map is injective, and does not mean that set colimits preserve finite products. The exact category Delta_inj refutes both stronger readings.
- Lead 5(iii)'s one-term conclusion uses an affine equalizer of that one parallel pair. Condition IV supplies it for quasi-filtered and total categories; condition I alone would not supply it.
- Lead 5's final cycle must carry coefficients in C=K/im psi. It is not a nonzero ordinary class in H_1(BA;Z), which vanishes for total A.
- The mixed-cycle quotient has the same positive derived-group formulas as the column module, but this does not prove the modules isomorphic or their T_1 zero.

## Computation

`code/check_delta_patterns.py` and its output verify an explicit affine equalizer for alpha=(1,1,-1) and beta=(1,0,0), while checking invariance of ordered nonzero coefficient patterns under every increasing injection into target sizes three through nine. The proof for arbitrary target size is the elementary zero-insertion argument. The computation is not used to infer an infinite statement from finite cases.

## Main-question routes explored in this branch

| Route | What was proved or checked | Exact obstruction or failure | Next mathematical step |
|---|---|---|---|
| P1, resolving tensor closure | The resolving class generated by permutation modules is stable under tensoring with a permutation module. Augmentation ideals I(M) and their tensor powers belong to it. | I(M)^2 is an image of I(M) tensor I(M), and acyclicity of the source does not imply acyclicity of its image. | Construct a valid resolving-class presentation of this image or of the special column module. |
| P1, three-colour graph and Cech cover | The cycle quotient C has all positive derived groups identified with the corresponding formulas for Q_a. A cover by two-colour subgraphs gives a length-two permutation complex with homology L in degree two and C in degree one. | Its colimit complex retains the same Z/epsilon(L) obstruction. It does not supply a vanishing. | Find an additional structural constraint on C forced by totality, rather than assuming C has a natural permutation basis. |
| P2, one-relator form | The exact one-relator criterion and its Tor formula are proved. | Totality gives binomials but not an arbitrary augmentation-zero combination. | Settle the first trinomial 2c_0-c_1-c_2, keeping ordinary and affine arrows distinct. |
| P3, kappa | Its zero class in colim K has a finite parallel-difference normal form, and simultaneous affine equalization of those pairs would annihilate it. | IV handles one term, not an arbitrary finite family of terms. | Prove a reduction of these special K-valued relations to one term or supply simultaneous equalization independently. |
| P5, free abelian resolution | All free resolution terms are permutation modules. | The extra degeneracy is only set-valued and does not induce an abelian-colimit contraction; the relevant counit face is not the needed free linearization. | Produce an actual linear contraction or a separate derived comparison. |
| P5, Eilenberg–Mac Lane stabilization | It identifies the possible T_1 class in stable homology. | Totality does not supply the requisite truncation preservation; Delta_inj forbids assuming it. | Establish a weaker stable vanishing statement without a product or truncation assumption. |
| Parent's G_F element-category reduction | The common-successor construction gives joint representatives, and the proposed comma comparison was checked. | Shear arguments need equality of joint tuple classes, not merely coordinate classes. | Prove additive-reflection discreteness while allowing the known failure of finite-product preservation. |
| Coefficient detection | The parent's theorem exact over Z iff exact over Q and every F_p was independently audited and verified. | It does not settle any field implication. | Prove or refute one of the field cases or establish all of them uniformly. |
| C4, Ramsey candidates | The literature agent's circle-valued dual-certificate proof of I plus local Ramsey implies integral exactness was independently checked. | This excludes Ramsey candidates; it does not show totality implies Ramsey. | Use the exclusion in the candidate search, or prove a weaker property of total categories sufficient for the same dual argument. |

The smallest unresolved instance in this branch remains an ordinary triple in an arbitrary total category, equivalently whether Z/epsilon(K_1 intersection K_2) vanishes. There is no claimed separator and no claimed proof of its impossibility.

## Supplementary search record

The six queries were: `"acts" "homologically flat" monoid`; `"monoid" "permutation modules" "flat"`; `"Z-flat" acts monoid linearization`; `monoid acts linearization flat modules homology permutation flatness`; `"homological" "flatness" "acts"`; and `"permutation modules" "Tor" "flat" monoids`. No theorem detecting linearized-module flatness from all permutation-module Tor tests was obtained. No content of an unopened source is asserted.

## Files contributed

`work/part_b.tex`, `work/algebra_leads.md`, `work/algebra_results_fragment.csv`, this report fragment, `code/check_delta_patterns.py`, `code/check_delta_patterns.out`, `code/build_algebra_fragments.py`, and its output. The work files retain the detailed reasoning and failed approaches; none is silently omitted or represented as settled mathematics.
'''
(work / 'algebra_report_fragment.md').write_text(report)
print(f'Wrote {len(rows)} statement rows to {path.relative_to(base)}')
print('Wrote work/algebra_report_fragment.md')
