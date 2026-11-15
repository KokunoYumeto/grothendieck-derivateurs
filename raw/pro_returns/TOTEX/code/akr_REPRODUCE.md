# AKR computation protocol

The formulas and repaired construction are in Part C of `../TOTEX_paper.tex` and the accompanying PDF. Run the commands below from the `code/` directory. The source is the attached Adámek–Koubek–Reiterman (1981) PDF, pp. 377–380 and 383–388. The program uses only the Python standard library. JSON output is written next to the program; ordinary output can be redirected as below. All category and nerve generators are reconstructed by the program, so no opaque certificate data are needed.

```sh
python akr_stages.py --partial-k2 > akr_stages.out
python akr_stages.py --triple --verify-field > akr_stages_triple.out
python akr_stages.py --critical-k3 > akr_stages_critical.out
python akr_stages.py --literal-common-n --partial-k2 > akr_stages_literal.out
python akr_stages.py --literal-common-n --triple > akr_stages_triple_literal.out
python akr_component_checks.py > akr_component_checks.out
```

The repaired commands verify properties (9), (10), and (11) for every quasi-filter constructed. The literal-common-n commands deliberately implement the printed common-n restriction and record each failure of (11); those commands are diagnostics for the source error and are not C.1/(11) certificates. They are valid substages of general Part B.9, whose B.7–B.8 induction uses the verified quasi-filter identities and property (9), but not (11). The paper derives this scope from the opened source and proves that the recorded class death is real for that general variant. The signed neighbour quasi-filter identities are checked in both modes.

Every finite category is generated as concrete injections, with arrows represented by complete function tuples and composition by tuple substitution. The program verifies injectivity and closure under every composable pair. Associativity follows pointwise from function composition. For H=hV/(v1~v2), or the three-relation quotient selected by --triple, it constructs the exact quotient functor and every nondegenerate simplex of its category of elements. It checks d²=0 and computes homology by integral unit-entry chain contractions. If any nonunit boundary remains, it is reported instead of silently treating rational Betti numbers as integral homology. The --verify-field calculation is a separate sparse column elimination over F_101 and was run for the triple diagram at K0 and K1.

The s=45 stage K1 includes all eleven ordered parallel pairs of K0, including equal pairs, and all four ordered object pairs. It has seventeen objects and 1263 arrows. The selected s=153 K2 calculation is one attachment, not the full second stage. Its schedule is a0=2, a1=8/5, a2=128/85.

The --critical-k3 calculation has a different continuation: after K1 it adds only the sum of the two circular-link targets at stage two and then a cross-sum quasi-filter at stage three. It uses a2=(8/5)(64/65) and a3=a2(32/33), so s=297 is allowed. It must not be combined with the a2=128/85 schedule of the selected s=153 K2 attachment. Both are substages of allowed completed infinite constructions. Neither is the full K2 or full K3.

The component check exhausts all 1263 arrows and 91783 ordered parallel pairs of repaired K1. All H transition maps are injective and no induced pair graph on H-components has a nontrivial directed cycle. This is finite evidence only; no assertion about all later stages or all functors H follows from it.

## Recorded groups

- Repaired Hpair, K0: H0=Z, H1=Z.
- Repaired Hpair, K1: H0=Z, H1=0, H2=Z.
- Repaired Hpair, selected K2 substage: H0=Z, H1=0, H2=Z, H3=0; relative homology zero.
- Repaired Htriple, K0: H0=Z, H1=Z².
- Repaired Htriple, K1: H0=Z, H1=0, H2=Z⁴.
- Repaired Hpair, selected critical K3 substage: H0=Z, H1=0, H2=Z, H3=H4=0; relative homology zero at the sum attachment and final quasi-filter attachment.
- Literal common-n diagnostic, Hpair K1: H2=Z³, with twelve recorded failures of (11).
- Literal common-n diagnostic, selected Hpair K2 substage: H2=Z², H3=Z, with fourteen cumulative failures of (11). Its old H2 has rank-one kernel, but this is not evidence of a death in the repaired C.1 construction.
- Literal common-n diagnostic, Htriple K1: H2=Z¹⁰, with twelve failures of (11).

The paper proves that the repaired K1 H2 class injects into the full K2 without enumerating all second-stage objects. Its fate in the full K3 and eventual union remains undecided. Over that repaired first stage, the injection also holds for arbitrary Part B.9 second-stage targets. For the separately specified common-n Part B.9 continuation, the complete second-stage group and eventual homology remain undecided.
