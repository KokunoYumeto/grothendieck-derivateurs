# RESIDUE Parts B and C: audit log

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No personal attribution or priority claim.

## Confirmed principal result

Lead 3 is true, including infinity-categorical localizations. The missing point is that Cisinski's definition of a category with weak equivalences and fibrations only requires the pullbacks entirely inside the fibrant subcategory; an arbitrary full intermediate subcategory has precisely those pullbacks. Definition 7.4.6, Definition 7.4.12 and Theorem 7.5.18 have been checked in the attached book and at the author's source https://cisinski.app.uni-regensburg.de/CatLR.pdf (accessed 2026-11-11; draft date 2026-07-30, published monograph 2019).

BISITE A.32 and E.12 have been read in full. No error found in the former's general axiom proof or in its finite example; the independent finite checker passes. The six-object example also proves that (a)+(b) do not imply enough intrinsic fibrations.

## Completed mathematical results

The original component-dependent `W†` counterexample is correct, including empty categories and infinitely many components. Its strong saturation is exactly `W0`. This has a short explicit arrow-retract proof; no finite sampling is used to establish the axioms on all categories.

The stronger implication asked in Part B(3) is false. The class `W_circ` consists of weak homotopy equivalences together with nonzero-degree maps between circle homotopy types. It is strongly saturated, hence retract closed. The proof constructs the quotient of the homotopy category by the two-sided ideal of maps factoring through a circle, adjoins formal zero morphisms to handle empty hom-sets, and combines the quotient functor with rational first homology. Its aspherical objects are exactly the contractible homotopy types, so absolute Theorem A holds by Quillen's theorem. The relative axiom fails on the suspension of a double covering of finite crown posets: `C8 → C4` becomes a ten-object-to-six-object map over the three-object span. Its comma comparisons are a degree-two circle map and two maps between contractible cones, while its total map has degree two on `H2(S²; Z)` and is outside `W_circ`. No priority is claimed. The quotient proof is independent of any speculative universal-cover criterion.

The literal Rappel 1 (`W=W°`) and Rappel 1.2 are true. Complete elementary proofs use the cylinder projection and the twisted-arrow category. Proposition 1.3 is true with its ambient category read as `Cat`; the apparent circularity in its backward proof is removed by first applying opposite invariance to `W°`. Rappel 2.3 and the finite-product assertion of Proposition 2.4 do not follow from the printed absolute definition: the product of degree two on the circle with the identity circle gives a torus counterexample for `W_circ`.

Lead 3 is true without functorial factorization, a global terminal object, retract closure, or strong saturation. Every full intermediate subcategory inherits precisely the partial pullback structure required by Cisinski's Definition 7.4.6/7.4.12. Theorem 7.5.18 therefore applies directly inside that subcategory. The result includes ordinary and infinity-categorical localizations, and proves all three fibre axioms (a), (b), and (c).

The six-poset counterexample can be folded into a five-object category with sixteen arrows and all pullbacks. Its slice over `S` is exactly the old six-element lattice; the two distinct atoms of that lattice become two maps from a single object `A`. The specified category has maps `α,β:A→B`, `γ:A→C`, `b:B→S`, `c:C→S`, with `bα=cγ=x` and `bβ=y`, together with an initial object `0`. The weak class consists of identities and `α,β,γ`. The proof and program verify strong saturation, (a), and (b), and disprove (c) and factorization. This gives an upper bound of five for the minimum among all finite categories; it does not establish the minimum.

The needed portion of BISITE B.19 has been independently checked. Prescribed outgoing and incoming endpoint lifts have initial and terminal objects at each finite support stage, with the correct opposite parity choices. Rooted finite fence diagrams contract by repeated leaf deletion, fixing the root. Consequently the full fence replacement is strictly functorial and has a weak coaugmentation. It proves the intermediate-perfect-subcategory comparison for **every** fundamental localizer, including truncation and homology localizers. This does not require perfect maps to be intrinsic for the chosen localizer.

At XII ms.240–241, the stated factorization hypothesis now proves (a), (b), and (c) and both relative pullback identities. Footnote 128's weaker pullbackability assumption suffices. The caution in footnote 130 about all terminal maps being fibrant is unnecessary for these relative statements. The word `cofibrations` in footnote 129 has the wrong variance for the factorization, and two arrows at ms.241 are mistyped; their correct name is `bar p_2`. These are typing corrections derived from the displayed sources and targets, not claims of fresh manuscript-image verification.

## Final historical audit and further counterexamples

Two separate literal corrections survive even after changing the definition to relative Theorem A. In XVI Corollary 2.2, finite-coproduct closure plus filtered-colimit closure implies arbitrary **closure**, not the full two-direction decomposition axiom. The coarse localizer `W_ne` of all maps between nonempty categories and the identity of the empty category is strongly saturated and satisfies relative Theorem A, arbitrary coproduct closure, and filtered-colimit closure; it fails summand restriction. This is Maltsiniotis's Example 1.1.30 in the March 2020 version. B.11 proves every required property directly.

In XVI Lemma 2.5, the stated allowance of an arbitrary arrow class omits an identity hypothesis. On the four-object diamond, `W={a→1,id_1}` is closed under **every** product of its arrows, including nullary products, but localization does not preserve the binary product with `b`. The intended finite localization lemma with identities is proved in B.12. Its arbitrary infinite-product extension with identities remains Open here.

B.16–B.17 supply a second substantive counterexample, `W_nb`. On categories with finitely many connected components it requires an ordinary weak homotopy equivalence; on categories with infinitely many components it requires only a near bijection of component sets, meaning a bijection after deleting finite subsets on both sides. It satisfies every literal moderate-saturation clause, the terminal-object axiom, absolute Theorem A, and finite-coproduct closure. Its aspherical objects remain exactly weakly contractible. The shift of the discrete natural numbers is weak, so component bijectivity fails, yet its localization is nonthin. A fully defined quotient of `Set` by finite-output disagreement, with formal zero morphisms, detects the identity of the natural numbers against a constant endofunctor. This refutes **XVI Proposition 2.7 and XV Proposition 9.9, Lemma 9.10, Proposition 9.12, and Corollary 9.13 as literally stated**. B.17 also proves the corrected versions under relative Theorem A. No retract closure or strong saturation is claimed for `W_nb`.

The formal decomposition equivalences, descent of adjunctions, the intended finite product/coproduct localization lemma, the two adjunctions with discrete sets including infinite sets, and the elementary cube implications of XVI 3.1 are proved. The discrete-set proof does not assume preservation of arbitrary coproducts: a represented functor already inverting the weak arrows keeps its representing hom-sets after localization.

The exact saturation convention was checked at Cisinski 1.4.12 and Maltsiniotis 1.1.1: their FS3 is the split-idempotent clause `ri=1` and `ir∈W` implies `i,r∈W`. It is implied by Grothendieck's stronger moderate clause; it is not closure under arbitrary arrow retracts. Both constructed counterexample classes satisfy the stronger requested literal saturation, so this terminology distinction changes none of the results.

The final register has **25 numbered statements: 13 Proved, 6 Refuted, 4 Known, and 2 Open**. The historical inventory has **36 named rows: 8 Known, 7 Proved, 9 Refuted, and 12 Open**. A mixed row is marked Refuted if one printed clause is false, and Open if its additional conclusion has not been audited; its notes specify the individually settled clauses.

Independent adversarial audits by the other two agents confirmed B.2–B.4 and B.11–B.17. The latter checks included the exact XVI and XV manuscript hypotheses, the finite-output congruence and its inverse-isomorphism criterion, the finite/infinite split in the saturation proof, both discrete-set adjunctions, and the corrected relative-Theorem-A argument.

## Computations

Run `python code/BC/verify_counterexamples.py` from the package directory. The program is self-contained except for SymPy and uses no earlier package code. Its exact output is `code/BC/verification_output.json`.

The successful run reports:

```text
status: PASS
circle degree on H1: 2
suspension degree on H2: 2
fibre counterexample: 5 objects, 16 arrows
pullback cospans checked by universal property: 66
```

For the circle example it checks normalized nerve chain complexes, `d²=0`, integer Smith normal forms of the boundaries, primitive top cycles, and the actual chain maps. It constructs the actual overcomma posets over the three-object span and computes their homology. It also computes fundamental-group presentations from edges, a spanning tree, and triangle relations, recording exact Tietze eliminations. The two crowns give free rank one; the suspensions and cones give trivial groups. The sphere assertions themselves are proved by their explicit cone decomposition, rather than inferred merely from homology.

For `W†`, the program checks all category laws, the projection functor, the comma construction, component labels, isotropy groups, and the finite arrow-retract data. For the five-object fibre counterexample, it checks every composition, every cospan and the uniqueness of its universal pullback mediators, every intrinsic test, all universal-equivalence tests for (b), and the explicit `R,T` weak-natural-transformation certificates for (a).

This is verification of explicit counterexamples. It is **not** an exhaustive search through categories with six objects. The latter family is infinite without an arrow bound, since finite cyclic groups provide infinitely many one-object categories with pullbacks. Every finite category with pullbacks has only monomorphisms, but their automorphism groups still have unbounded order. No claim that a finite search proves a minimum has been made.

The program additionally checks the finite counterexamples to XVI 2.2 and 2.5, including the strict empty pullback of the two point inclusions and the diamond's sixteen binary meets. For `W_nb` it represents functions of the natural numbers by a finite prefix followed by an exact affine tail. Symbolic composition verifies the shift, its near inverse, the finite exceptional sets, and two maps to `{0,1}` becoming equal after precomposition with the shift. This is a certificate about the specified infinite functions, not a claim that a finite sample proves an infinite assertion.

The script `code/BC/update_register.py` regenerates the numbered register from the LaTeX claims and updates the explicit historical statuses. It is metadata maintenance; all mathematical verification is in `verify_counterexamples.py`.

## Literature checked and search record

The attached versions of BISITE A.32, A.10–A.13, E.7–E.12, and B.19 were read. Relevant original transcriptions in XVI and XII ms.215–218, 240–242 were read. The original transcriptions of XVI ms.1–27 and XV §9 were also read in full. The separate `BC_historical_audit.csv` inventories 36 named statements, with precise mixed-clause notes and unresolved entries left `Open`.

Cisinski (2004), *Le localisateur fondamental minimal*, was extracted and its Definition 1.1.3, Remark 1.1.4, and initial closure statements inspected. Its `LF3` is explicitly relative. Cisinski (2006), §§4.2 and 6.1.12–6.1.18, was inspected; 6.1.12 is explicitly the absolute weak-localizer definition. Maltsiniotis's March 2020 book, §1.1, was checked, including Definition 1.1.2 and opposite invariance, which is Proposition 1.1.21 in that version. The attached *Structures d'asphéricité* article was extracted and consulted for its comparison of lifting conditions and fibrations.

The web searches included the exact strings `localisateur fondamental faible`, `localisateurs fondamentaux faibles`, `weak fundamental localizer`, and `weak basic localizer`, together with `example`, `absolute`, `relative`, `Ara`, and `Chiche`. Author and publisher sources were preferred. The particularly relevant historical statements are Maltsiniotis (2012), Remark 1.3, and Cisinski's December 2019 MathOverflow answer to the weak-localizer-example question. Both report no example known to their authors at those dates. This is not presented as proof of absence in all later literature.

Opened primary sources not supplied in the archive:

- Quillen (1973), *Higher algebraic K-theory I*: original scan at `https://people.math.rochester.edu/faculty/doug/otherpapers/Quillen-Higher-I.pdf`, Theorem A at p.93 and twisted-arrow example at p.94; publisher record also checked. **verified**.
- Brown (1973/1974), *Abstract homotopy theory and generalized sheaf cohomology*: author scan `https://pi.math.cornell.edu/~kbrown/scan/1973.0186.pdf`; pages 422–423 visually inspected, including I.1 axioms and factorization lemma. **verified**.
- Kahn–Maltsiniotis (2008), *Structures de dérivabilité*: author preprint `https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/bkgmdef.pdf`; opened, but no theorem from it is used in the proof. **verified** for access, not a claim to have audited its proofs.
- Maltsiniotis (2012), *Carrés exacts homotopiques, et dérivateurs*: author preprint `https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/carhex.pdf`, Remark 1.3 and §1.4. **verified**.
- Cisinski's author-hosted 2019 monograph, currently dated July 30, 2026: Definitions 7.4.6/7.4.12 and Theorem 7.5.18. **verified**.

The editor's *Pursuing Stacks* landing page was opened, but this does not amount to direct verification of §§28–33. That specific requested primary-source check remains incomplete. Search results locating Ara and Chiche's relative localizers were inspected; a complete audit of all their weak-localizer remarks has not been made. These access limits are not hidden behind a blanket `verified` label.

The final near-bijection construction was additionally checked against searches combining the exact weak-localizer terms with `finite`, `connexité`, and `near bijection`; no matching example was located. An initial low-coverage search returned irrelevant results and was repeated with the stronger search service, recovering the primary Maltsiniotis definitions and the dated Cisinski discussion. This is a search record, not a priority or completeness claim.

Cisinski's 2026 author PDF Theorem 4.4.36(ii′), including its explicit restriction to nerves of ordinary categories and its opposite, was checked for the lifting-category criterion used in C.5. Cisinski 2006 Example 4.1.29 and Theorem 6.1.18 were checked for the two-stage localization argument of B.13.

I independently audited the root's D.4, D.6, and D.11. No mathematical defect was found in the countable-product obstruction, the sharp rational boundary criterion, or the fibration-axiom table. I recommended an explicit slice-model realization lemma in D.6 and an explicit accessibility citation for rational local coefficients in D.11. These are requests for proof exposition and source precision, not counterexamples.

## Remaining open work

`B.10` records the uncompleted full statement-by-statement audit of XVI ms.1–27 and XV §9. The inventory CSV explicitly distinguishes 24 settled named assertions from 12 remaining rows. These are XVI's first Corollary 2.8, Lemma 3.2.1, Corollary 3.2.2, Proposition 3.3, Proposition 3.6, Corollary 3.7; and XV Proposition 9.1, Corollary 9.2, Corollary 9.3, the earlier-axiom deduction in Proposition 9.4, Proposition 9.7, and Proposition 9.11. The main formal equivalences in 9.4 are proved; its additional deduction is not silently included. The mathematical questions about literal opposite invariance and strong/retract saturation are settled by the proofs above; the remaining work is the wider source audit, not those implications.

`C.8` records the exact unresolved minimum: exclude or construct a counterexample among finite categories with fewer than five objects, with no bound on arrows. No proof that the five-object example is least has been obtained. A naive finite enumeration by object count cannot provide such a proof.
