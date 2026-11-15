# BISITE research audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026.
No priority is claimed. The work was developed from the attached prompt,
its primary-source archive, targeted primary-literature checks, and
independent proofs and finite computations. Earlier AI-produced packages
are treated as leads, not as authorities.

## Deliverables and status conventions

The paper is BISITE_paper.tex and BISITE_paper.pdf. The complete register is
BISITE_results.csv, with exactly one row per numbered statement and the
requested seven columns. BISITE_references.bib is the unified bibliography;
each entry has an explicit verification note. The sections directory holds
the included LaTeX sources. The code directory holds programs and saved
outputs. The auxiliary part registers and reports are retained so the merge
is reproducible.

“Proved” means a proof is given here under the full hypotheses in the
statement. “Refuted” means a specified assertion is false and an explicit
counterexample is supplied. “Known” means the cited primary theorem and its
actual hypotheses were checked. “Open” records an exact task not settled by
this audit; it does not claim that the task is unresolved in the literature.
C.9 is a proved conditional implication: above dimension two its
model-structure premise is the unrefereed OpenAI claim, named in its
statement and dependency field. It is not an unconditional verification of
that claim. Bibliographic verification of the two OpenAI attachments means
that their documents and claimed statements were read, not that their
proofs or formalizations were certified.

| Part | Proved | Refuted | Known | Open | Total |
|---|---:|---:|---:|---:|---:|
| A | 24 | 10 | 0 | 0 | 34 |
| B | 13 | 5 | 3 | 1 | 22 |
| C | 5 | 2 | 2 | 1 | 10 |
| D | 5 | 3 | 4 | 1 | 13 |
| E | 9 | 4 | 1 | 0 | 14 |
| F | 11 | 3 | 4 | 1 | 19 |
| G | 5 | 5 | 4 | 0 | 14 |
| **Total** | 72 | 32 | 18 | 4 | **126** |


## Main determinations

The manuscript's maximal universal testing class is identified with the
correct smooth or proper class according to comma variance. The minimal
categorical fine theories are the covariant and presheaf diagram
infinity-categories. The simplicial literal-slice recipe needs a
quasicategorical base; its corrected universal version uses the actual
covariant and contravariant model structures at every base.

The complementarity inclusion for the same fundamental localizer holds
exactly for the minimal localizer and the total class, without an
accessibility hypothesis. The truncation, homology, and local-system
examples are distinguished and checked separately. The finite central C2
extension is verified by nonabelian presentation reductions, not by
homology alone.

XIIc B062 is false. A six-element lattice satisfies fibre axioms (a) and
(b) at every base and violates (c), with explicit inverse equivalences
after both ordinary and enhanced localization. Separately, the manuscript's
literal moderately saturated absolute localizer package does not imply
relative Theorem A; a component-sensitive class and a finite groupoid
triangle give a counterexample. Its failure of full arrow-retract closure
is explicitly recorded. These conclusions supersede the temporary Open
drafts from the work process.

The abstract theorem uses explicit enhanced presentation hypotheses,
distinguished from the finite Brown floor. The derivator statements give
the precise base-change, projection and exchange maps and their canonical
mates. The correspondence construction specifies both its enhanced input
and its geometric-setup version. In the diagonally closed discrete-fibration
setup, the stable cohomologically proper maps are exactly finite discrete
bifibrations.

The geometric comparison is proved for every categorically proper map of
finite posets, including nonvertex points of the target realization. The
genus-zero forgetting functor is proper for every n≥3 and is not smooth at
n=4, with a lifting category equivalent to BZ. Its specified direct-image
and boundary comparisons are proved using the actual constructible
categories and canonical mates.

The stable finite-limit formula is a covariant spectral weight acting by a
derived coend. A pointwise twist followed by the same-base colimit is
refuted on the walking arrow. The finite-poset canonical equivalence
criterion, its upper-interval variance, and its geometric Verdier comparison
are stated with the checked Aoki hypotheses. Finite EI categories require
coefficient conditions, and ordinary Verdier duality need not preserve the
coarse minimum stratification.

## Exact remaining tasks

| ID | Remaining assertion | Smallest boundary isolated here |
|---|---|---|
| B.21 | Existence of a different strict Grothendieck bifibration representing the path local system with contractible total category | The five-element rectangular-band monoid; the given fence model's failure is proved, but it does not rule out every alternative |
| C.10 | Relative Street-nerve recognition of both strict higher fine localizations, together with the local lifting and universal Kan base-change criteria | A strict 2-category with a walking noninvertible 2-cell |
| D.12 | General locally compact Hausdorff representation of cosheaves by the unrestricted open-test localization of Top/Y, and a precise dual slice presentation of sheaves | The real line is beyond the proved finite Alexandrov construction |
| F.18 | Extension of the derivator base-change theorem to specified strict higher indexing shapes with coherent mates | Dimension two, where a higher Der 4 and a compatible lax-comma comparison must first be supplied |

Each corresponding paper statement explains the attempted reduction and
the missing comparison. No one of these tasks is silently replaced by its
proved special case.

## Reproducibility and evidence limits

The source-archive inventory and hashes are in code/00_inventory.out.txt.
The extraction programs record the supplied PDFs and text products used.
Reading an extracted section is not a claim to have checked every page of
each monograph. Exact source locations and corrections appear in the
detailed audits below and in the bibliography notes.

The finite certificate programs run with Python's standard library. They
verify complete finite category laws, pullbacks or pushouts where used,
comma categories, permutation actions, explicit localization certificates,
and exact group-presentation or linear-algebra data. In particular,
a_b062_verify.py is independent of the search and rewriting algorithm.
The search exhausted the specified naturally labelled posets through five
objects, recorded no skipped cases, and found the counterexample during a
partial six-object enumeration. No minimality theorem for arbitrary finite
categories is claimed.

The D.11 consistency check covers 50 naturally labelled posets, 1,584
monotone maps to a three-object chain, and 794 comma posets for the retained
proper-lifting cases. Its rational-homology check is distinguished from the
paper's full homotopy-initiality proof. The C2 finite-EI calculation checks
the algebra of the resolution; the paper separately proves the infinite
product-versus-sum conclusion.

The build and final validation programs record compilation, citation and
register consistency, PDF page geometry, and the reproducibility manifest.
The PDF was rendered for visual inspection. Computational checks support
the specified finite certificates and document integrity; this paper is
not a formally verified or refereed mathematical work.



## Part A and XIIc B062: audit report

This work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We attribute no research contribution to a person and claim no priority. Numbered results, hypotheses and proofs are in `sections/A.tex`; the full counterexample answering XIIc B062 is in `sections/E_b062.tex`, E.12. The independent register `A_results.csv` has 34 rows: 24 Proved and 10 Refuted, with no remaining Open statement in Part A. In particular both the fibre-axiom implication and the literal absolute-to-relative localizer implication are refuted by explicit examples.

### Sources actually checked

We read VI ms. 81–84 and XII ms. 207–227 in the supplied LaTeX transcriptions. The supplied archive contains no edition PDF for VI-b or XIIc-a. We subsequently opened the editors' public XIIc edition, dated 30 March 2003, at <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/ps/Der-ChXIIc-30-03-03.pdf>. We compared the extracted text for ms. 207–208, 217–218 and 222–224 and visually inspected the edition images containing ms. 207–208, 217–218 and 222–224. In particular, the weak saturation footnote at ms. 207, the question at ms. 217–218, the strengthened universal definition at ms. 222, and the smooth/proper type mismatch at ms. 223 are present in the edition. We did not independently inspect an edition image for VI ms. 81–84.

We read II §§5–6, ms. 69–89, together with the cancelled §4, ms. 65–68, in the transcription and extracted edition text. The audit includes the domains of the Galois correspondence, formula (5.20), the successive versions of (6.2)–(6.7), Proposition 6.1 and the stabilizer definitions after it. We compared the corresponding companion overview, claim register and commentary blocks. The cancellation is mathematically material: a stabilizer is not an antitone operation on arbitrary input classes, and a mixed transporter need not be composition-closed.

We read XII §7's fibre and finite-diagram arguments, particularly ms. 240–248, and followed the later propositions used in the report, including the cocartesian statements at ms. 273–275. We read XIII §§4–6, ms. 44–76, including the proof of the admissibility theorem at ms. 62–72, against the edition text; the definitions at XIII ms. 7–12 and 27–29 were checked to determine precisely what its closedness and exactness hypotheses mean. We read XVI §4's fibration definitions and implication scheme, with its references to the localizer clauses at XVI ms. 1–3, against the supplied edition. We did not silently identify the historical numbering of derivator axioms with the modern numbering.

We inspected the relevant POLES, GALOIS, PATHS and STRATA claim statements and proofs. They were treated as proposed arguments, not as authorities. The independently reconstructed portions are identified below. The supplied unrefereed 2026 claims about higher categories and globular infinity-groupoids are recorded with the status requested in the prompt; no result in Part A or E.11–E.12 uses them.

The extraction program `code/a_extract_evidence.py` records SHA256 hashes of the supplied edition PDFs and the additional background PDFs from which searchable text was extracted. Extracting a paper is not a claim to have verified every theorem in it. In particular, the Rezk, Maltsiniotis and Cisinski extractions supplied targeted checks and coordination with Part B; the proofs in Part A cite their actual inputs separately.

### The fibre question XIIc B062 is false

The implication from axioms (a) and (b) to the assertion about every full intermediate subcategory is refuted by E.12. The category is the finite poset on six objects with Hasse covers

`0<1, 0<2, 1<3, 2<3, 1<4, 3<5, 4<5`.

There is a unique arrow for each ordered comparable pair, and composition is forced by the order. Weak equivalences are the identities and `1→3`, `1→4`, `2→3`. This is a finite lattice and hence has all finite limits and colimits. Its weak equivalences satisfy two-out-of-three and are strongly saturated, not merely the weak saturation stipulated at XII ms. 207.

The full subcategories of intrinsic fibrations over the six bases are respectively `{0}`, `{0,1}`, `{0,2}`, `{0,3}`, `{0,1,4}`, `{0,3,5}`. E.12 derives every entry by all applicable pullback tests. On these subcategories the restricted weak equivalences are identities, except for `1→4` in the slice over `4`; its three possible base changes are again weak. This proves axiom (b) at all bases.

Axiom (a) is tautological for bases `0,1,2,4`. At base `3`, the relative retraction sending `1,2` to `3` has a weak coaugmentation. At base `5`, the relative retraction `R=(0,3,3,3,3,5)` and the relative endofunctor `T=(0,1,2,3,1,5)` have componentwise weak natural transformations `Id ← T → iR`, with `Ri=Id` on the fibrant chain `{0<3<5}`. These transformations give explicit inverse equivalences after localization. They also prove the premise with infinity-categorical localizations: they become natural equivalences there, so no assumption of discrete higher mapping spaces is being made.

The intermediate full subcategory `{0,3,4,5}` is a four-object diamond. Its only weak arrows are identities, so it localizes to itself. The fibrant three-object chain does not include it essentially surjectively. Its functor to the whole localization is also not full: there is no diamond arrow `3→4`, but the whole localization has the isomorphism represented by `3←1→4`. This verifies failure of each required equivalence in (c).

The example has a terminal object but does not make every terminal map intrinsic. It does not have enough intrinsic fibrations, since `4→5` has no factorization as a weak arrow followed by an intrinsic fibration. These extra properties are not hypotheses of the question at ms. 218. The later addition of terminal-map hypotheses at ms. 240 must not be read back into it. E.11 remains a valid sufficient theorem with enough intrinsic fibrations and a coaugmented slice replacement. A weak natural zigzag through arbitrary objects is insufficient: here its component at `4` passes through `1`, which the intermediate subcategory omits.

Before finding this example, we tried to deduce (c) by factoring the assumed equivalence in (a) through the intermediate localization. That argument fails because the composite being an equivalence imposes no essential-surjectivity or full-faithfulness requirement on each factor. We then proved the sufficient coaugmented replacement statement, searched finite posets and extracted the explicit counterexample. The final status supersedes the temporary Open draft; B062 is not left open.

### Definitions, quantifiers and variance corrections

1. **Literal and adopted localizer axioms.** XVI's literal Loc (1) contains isomorphisms, two-out-of-three, and the two-composite condition `gf,fg∈W ⇒ f,g∈W`; the text calls these together moderate saturation. Retract closure is Loc (1 bis), and strong saturation is Loc (1 ter). The absolute Theorem A clause is Loc (3), and the relative clause is Loc (3 bis). The modern relative package fixed in the paper cannot be substituted silently for the literal absolute one. A.1 proves the forward relative-to-absolute implication; A.32 refutes the converse under precisely the literal moderate saturation hypothesis.

2. **Intrinsic means universal preservation of arrows over the base.** The tests in `Fib_W` are all weak arrows `T′→T` equipped with `T→S`, not only comparisons of chosen fibres and not only maps between contractible bases. Composition and arbitrary pullback closure require no two-out-of-three hypothesis. Retract closure requires the stated retract premise on `W`; it is not supplied by the weak saturation footnote of XII ms. 207 alone. This verifies the formal content of GALOIS D.1.

3. **The universal quantifier in the maximal local class.** The first proposal at XII ms. 222 tests only the indicated base-change functor. Grothendieck immediately strengthens it to test every preliminary base change `T→S`. A.5 uses that second definition and proves closure, idempotence, equality of the resulting fine classes, and maximality among composition- and pullback-closed test classes. The first displayed arrow direction on that page is mistyped: the functor `Cat/S→Cat/S′` requires `S′→S`.

4. **The two fine variances.** In the discussion at XII ms. 222, `W^g` uses `X/s` and corresponds to the covariant fine theory; its maximal preservation class is the smooth class studied in Part B. At XII ms. 224, `W^d` uses `s\X` and corresponds to the presheaf theory, with the proper preservation class. Superscripts copied from a different passage do not determine variance. The source's occurrence of `Liss_W` just before constructing `Prop_W S` at ms. 223 must read `Prop_W`; the edition confirms the mismatch. A sieve and a cosieve cannot be interchanged when testing raw pullback.

5. **Smooth and proper are stabilizers.** The definitions in II ms. 66 and 89 are stabilization of the aspherical class and its dual coaspherical class. They are not the mixed transporters taking these classes merely into `W`. The latter contain the corresponding stabilizers and also `Fib_W`; conflating them changes the mathematical assertion. The inclusion `Liss_W∩Prop_W⊂Fib_W` at XII ms. 225–226 is explicitly proposed with a qualification, not proved there. Its validity is a substantive additional question handled in Part B.

6. **The three weak-equivalence classes.** A.3 proves `W_S^u⊂W_S^L⊂W_S` by actual test functors and identifies where two-out-of-three enters. A full-faithfulness class on coefficients need not have it. The set-coefficient example `e→BC₂→e` in GALOIS is independently verified. Universal weakness in a slice over `S` is distinguished from universal weakness of an arrow with respect to its own codomain.

7. **Raw and derived reindexing.** Postcomposition preserves the fine class for every base map, by pullback stability of the local tests. Raw pullback is proved to preserve it for a map in the test class, or under a separate preservation hypothesis. One cannot deduce an adjunction on localized slices for all base maps merely because postcomposition descends. A.4 proves descent when both members of the original adjunction are relative. A.14 explains the different method using the opposite structural class and universal weak equivalences to construct a pseudofunctor for arbitrary base maps.

8. **The three fibre axioms have different content.** Axiom (a) gives equality of strong saturations of the two restricted weak classes; (b) is equality of the original classes; (c) quantifies over every full intermediate subcategory. Therefore the underbrace at XII ms. 218 saying that the source localization identifies under (a) need not be changed to “under (b)”: (a) already identifies the relevant localizations. The separate clause labelled (c) at ms. 227 concerns adjunctions, not intermediate subcategories.

9. **The literal weak-fibration test in XVI.** “Contractible” in XVI §4 is category-homotopy contractibility: the identity functor is joined to a constant functor by a finite zigzag of natural transformations. Weak contractibility of the nerve follows, but replacing the test family by all categories with weakly contractible nerves requires a separate argument. POLES A.5 makes the category-homotopy distinction correctly. A.15 preserves it and separates intrinsic fibrations, Grothendieck fibrations, weak fibrations and perfect functors, and the reference-localizer variants. The initial Loc (7 F) wording says cofibrations where fibrations are required.

10. **Chapter I's coefficient repair is asymmetric.** The direct-image assumption for constant coefficients pulls a 1-complete equivalence back to a constant-coefficient equivalence. It does not automatically give a 1-complete equivalence. Stability under composition follows for the stronger condition testing every locally constant coefficient after every base change. A.19 reconstructs this argument from the adjunction and base-change maps instead of citing GALOIS D.2 as authority.

### Other independently checked implications and counterexamples

The transporter Galois relation in A.6 uses composition closure on its weak-arrow side and pullback closure on its test-map side. Imposing composition closure on the latter before taking the transporter is incorrect: the explicit four-object chain in A.8 refutes it under precisely the hypotheses of II §6, where `W` is only composition-closed. A.7 proves the exact additional criterion for a closed transporter pair to have a composition-closed right side. A.34 refutes antitonicity for the cancelled stabilizer-only construction.

II §5's polarity identities require closure after taking a join, and distinguish a principal lower set from its generating element. A.29 verifies the corrected formula and evaluates the annihilator example over the two-dimensional vector space over `F₂`. A.30 checks that unions of classes closed under composition and pullback need not compose; intersections do, and joins require closure of the union.

A.11 proves the fibrewise invariance from enough intrinsic fibrations without requiring terminal objects, chosen functorial factorization or strong saturation. A.16–A.17 check the formal POLES A.13–A.14 implication scheme against the actual premises in XVI. The relative mapping-path proof includes the terminal-map assumption and all comparison maps. For transferring a condition involving arrows, objectwise replacements must be assembled into commuting squares; functorial replacement is sufficient. Brown's two original fibre lemmas were opened and read, rather than inferred from a later source.

A.18 independently reconstructs the finite rational-coefficient failure of composition in GALOIS D.3: a map into the specified two-object category and a regular-action covering are each weak rational fibrations, whereas the composite has a two-point strict fibre over a contractible base. The comparison in degree zero is the diagonal `Q→Q²`. All finite categories and pullbacks involved were checked by the attached program. A.20 independently verifies the proper-cosieve counterexample at I ms. 102: the inclusion `{1}→[1]` is proper, but the relevant comma transition is the empty category to the point. This is the error registered as Ib-C003; it is not a claim that proper maps fail the appropriate base-change theorem.

A.21 proves the finite product universal property in the localized fibrant slice by localizing the product/diagonal adjunction. Its pullback assertion uses one intrinsic leg and the explicit replacement comparisons. A.22 preserves the distinction between historical exactness `W=TF∘TC` and the equalities of trivial classes. A.27 then proves that the **additional closedness assumption actually present in XIII ms. 57** forces both equalities, and that `W` is retract-closed. This uses the proof of Riehl's Lemma 11.3.3, reproduced with finite pushouts and lifting only. The resulting model structure is proper when the source's intrinsic-containment clauses are imposed.

Consequently the original uniform closed exact premise of XIII is strong enough to prove more admissibility than a reading using only the intrinsic floor would suggest. A.28 proves that every functor for which the ordinary right Kan extension exists is admissible in that domain: it preserves weak equivalences between fibrant diagrams by Brown's lemma. The derived adjunction and pointwise comma formula are proved with their comparison maps, using Quillen's homotopy-category theorem in its original finite-limit convention. In particular, the theorem for finite posets at XIII ms. 59–61 is settled; it is not left open. The noetherian sober Alexandrov-poset qualification adds no infinite case, as proved independently in A.25. Ordinary right Kan extensions still do not preserve arbitrary objectwise weak equivalences: the finite cospan in A.24 has strict pullback empty before comparison and terminal afterwards. The finite intrinsic floor alone does not imply all-small Kan extensions, as the `FinSet` example in A.26 proves.

A.33 verifies the POLES correction at XII ms. 274 by a complete finite-set example with `W` equal to the isomorphisms: a comparison of two pushout squares has initial and final component isomorphisms but a middle component collapsing a two-element set. The conditions about aspherical initial and final vertices in the stated Corollary 1 hold nevertheless, so that corollary also fails without the extra conservativity premise. The word “cartesian” in Cons 2 at ms. 273 must be “cocartesian”; this is present in the edition, not merely introduced by transcription.

We reviewed the proof of the full right base-change converse in the parent paper against STRATA D.3–D.4. There is no counterexample to STRATA D.4 from the observation that right Kan extension preserves terminal objects: its proof takes the **left adjoint mate** first and then evaluates that left mate on the terminal coefficient. Testing the original right comparison only at the terminal coefficient would be vacuous, but that is not the supplied proof. The precise mate statement is preserved in Part F.

Other transcription or displayed-formula slips recorded during the read are XIII ms. 71's reference to a left adjoint where the right adjoint is intended, the pointwise map at ms. 70 whose target should be `u^*F` rather than repeating the source, and the trivial-fibration equality at ms. 74 which requires `F∩W`, not `F∩C`. The use of finite limits in the admissibility proof is licensed by M0, which supplies both finite limits and finite colimits even where a nearby sentence singles out colimits. These corrections do not change the hypotheses used in A.28.

### The literal absolute-to-relative implication is also false

The focused second pass on A.32 produced a separate counterexample, independently checked by two mathematical derivations and a finite certificate. For arbitrary small categories define `W†` to consist of the functors inducing a bijection on components, with the additional requirement of being a weak homotopy equivalence only when the categories are connected. Thus on categories with two or more components the class tests only the bijection of components; on connected categories it is exactly `W∞`; the empty-to-empty functor is included.

This is a class on **all** small categories, not a finite fragment. Two-out-of-three holds because any two weak maps in a composable triangle force bijections on all three component sets. All three categories then have the same component cardinality, so the remaining test is either vacuous or exactly two-out-of-three for `W∞`. The literal moderate condition holds for the same reason: if both composites `gf` and `fg` are in the class, their component maps being bijections force those of `f` and `g` to be bijections, and in the connected case the corresponding two-composite property of weak homotopy equivalences applies. No full arrow-retract closure is assumed.

The `W†`-aspherical categories are exactly the categories with weakly contractible nerves. The terminal-object axiom follows. Absolute Theorem A for `W†` follows directly from Quillen's Theorem A for `W∞`, whose exact original statement and dual comma formulation were opened and checked. Thus the literal Loc (1,2,3) hold with their actual quantifiers.

Take the one-object base `C=BC₂`; let `E` be the chaotic groupoid on the two elements of `C₂`, with its regular-action functor `E→BC₂`. The projection `u:E×BC₂→E` is a morphism over this base. Globally its source and target are connected; the induced fundamental-group map is `C₂→1`, so `u∉W†`. For the unique base object, the comma category `E/c` has four objects `(x,t)` and two components indexed by `x+t`; each component is chaotic with two objects. The source comma category is `(E/c)×BC₂`. Its projection to `E/c` is a bijection on the two component sets, hence belongs to `W†`. This is exactly the premise of relative Loc (3 bis), while its conclusion fails.

The example is appropriate to the literal saturation convention and does not conceal its boundary. The map `BC₂→e`, which is outside `W†`, is an arrow-category retract of `(BC₂⊔e)→(e⊔e)`, which belongs to `W†`. Thus the class fails full retract closure, although it satisfies the split-retraction clause of modern weak saturation as a consequence of its moderate condition. No assertion about an additionally retract-closed absolute class is inferred from this example.

Our initial draft left this implication unestablished and incorrectly suggested the walking arrow as a first missing test. The latter suggestion is false: whenever the base has a terminal object `t`, the comparison at `t` is already the original functor, since `A/t≅A` and `B/t≅B`. The final proof records that correction. The counterexample uses a one-object base with a nonidentity automorphism instead. It settles the literal question left unestablished in POLES A.16; there is no remaining A.32 Open status.

### Programs and outputs

All mathematical computations below are finite checks or exact symbolic certificates. No floating-point estimate is used as evidence for contractibility, weak equivalence or equivalence of localizations.

| Program | Saved output | What it verifies |
|---|---|---|
| `a_extract_evidence.py` | `a_extract_evidence.out.txt` | Source PDF hashes and reproducible text extraction for edition and targeted primary-source checks. |
| `a_fetch_primary.py` | `a_fetch_primary.out.txt` | Retrieval hash of Brown's author-hosted scan; OCR of the pages containing Part I §4, Lemmas 1–2. |
| `a_finite_audit.py` | `a_finite_audit.out.txt` | All finite examples in A.3, A.8, A.18, A.20, A.24, A.29, A.30, A.33 and A.34, including identities, arrows, composition, pullbacks or pushouts as applicable. |
| `a_b062_search.py` | `a_b062_search_n4.out.json`, `a_b062_search_n5.out.json`, `a_b062_search_n6.out.json` | Search over naturally labelled finite posets with pullbacks and all two-out-of-three weak classes, then exact localization checks by completed path rewriting. |
| `a_b062_verify.py` | `a_b062_verify.out.txt` | Independent certificate for the six-object counterexample; it imports neither the search nor the rewriting implementation. |
| `a_absolute_relative.py` | `a_absolute_relative.out.txt` | All finite groupoid and comma-category data in A.32, their component and automorphism groups, and the full arrow-retract certificate locating the saturation boundary. |
| `a_make_registry.py` | `a_make_registry.out.txt` | Parses all 34 numbered A claims, checks their count and writes the supplied CSV with statuses, dependencies and source locations. |

The search exhausted naturally labelled posets with pullbacks through five objects: respectively 1, 2, 6, 25 and 141 posets for sizes 1 through 5, and respectively 1, 3, 16, 140 and 2005 two-out-of-three classes. It found no counterexample in those ranges and recorded no skipped case. It then found the six-object example during a partial size-six enumeration. These are program-output statements; we do not claim a general minimality theorem for arbitrary finite categories. Completion limits in the search are implemented as skips, never as successful equivalence tests, and the supplied runs have empty skip lists. The hand proof of E.12 is independent of these localization computations. Its separate verifier exhausts every possible intrinsic and universal pullback test and checks the actual natural-transformation certificate establishing (a).

### Primary references and search record

Every entry in `A_references.bib` is marked `verified` and says what was opened. Brown (1973), *Abstract homotopy theory and generalized sheaf cohomology*, Part I §4, Lemmas 1–2, was checked in the author-hosted scan. The printed journal volume is dated December 1973; the author's publication list assigns 1974, so the bibliography records the journal date and explains the discrepancy. Quillen (1967), *Homotopical Algebra*, I.1, Theorem 1 and I.4, Theorem 3, was checked against the publisher record and public re-typesetting; the latter renumbers these results Theorems 1.1 and 1.3. Quillen (1973), *Higher algebraic K-theory: I*, Theorem A and its dual comma formulation, were read in the full original scan at printed p. 93, with the proof beginning at p. 95; its Springer bibliographic record was also opened. Riehl (2014), *Categorical Homotopy Theory*, Lemma 11.3.3, was read in the author-hosted PDF. The proof is included rather than using a citation to conceal the retract-closure step. Hovey's standard model-category formulations were inspected as a cross-check but are not an additional premise in the manuscript argument.

For the B062 question we searched, among other formulations, `localization "intermediate full subcategory" equivalence fibrant`, `Grothendieck "axiome de la fibre homotopique" "218"`, and `relative category "full subcategory" "intermediate" localization counterexample`. The original Grothendieck edition and related localization literature were returned; no matching six-object example was identified in those results. That limited search is not a claim of novelty, and no priority is asserted. We also searched primary-source formulations of Brown's lemma, the finite-limit model-category convention, retract closure from two weak factorization systems, and the noetherian sober Alexandrov condition before using the corresponding arguments.

For the absolute-to-relative question, we additionally checked Cisinski (2006), §6.1.12 and Theorem 6.1.18, in the supplied *Astérisque* 308 text: the former explicitly defines weak fundamental localizers using absolute Theorem A, and the latter proves their minimum is `W∞`; neither identifies every such class with a relative localizer. We opened Maltsiniotis's author-hosted *La théorie de l'homotopie de Grothendieck*, provisional March 2020 version, §§1.1.1–1.1.2, which likewise distinguishes the split-retraction saturation clause and the absolute notion from the relative notion introduced in Chapter 2. Searches included `"localisateur fondamental faible" "connexe"`, `"weak fundamental localizer" "relative"`, and `"localisateur" "composantes connexes" "facteurs directs"`. No identical component-dependent counterexample was located in the returned sources. This is a limited search record, not a novelty claim.

### Remaining scope boundaries

No numbered statement of Part A remains Open. The A.32 counterexample addresses the literal moderate saturation package; its explicitly demonstrated failure of full arrow-retract closure prevents treating it as a counterexample under an additional Loc (1 bis) premise. The E.12 counterexample addresses XII's exact all-base fibre axioms; its failure of enough intrinsic fibrations prevents treating it as a counterexample to the stronger replacement theorem E.11. These are stated limits on the examples, not omitted hypotheses or claims about larger questions.

B062, the literal absolute-to-relative implication, the XIII admissibility theorem under its actual uniform closed exact premises, the transporter composition mistake, the finite counterexamples and the missing conservativity at XII ms. 274 are settled above. Parts B–G maintain their own scope and remaining statements; this audit does not certify every result in an inherited AI-produced package merely because several of its arguments were successfully reconstructed.

## BISITE Parts B and C: research and verification report

### Delivered material

- `sections/B.tex`: B.1–B.22.
- `sections/C.tex`: C.1–C.10.
- `B_results.csv`, `C_results.csv`: the required seven-column registers, with full numbered statements, statuses, dependencies and manuscript pages or inherited claim IDs.
- `BC_references.bib`: ten primary-source entries, each carrying an explicit `verified:` note describing the scope of verification.
- `code/bc_*.py` and their outputs: exact finite category, group presentation, path-monoid and registry checks. The proofs do not infer contractibility from numerical homology.

The two sections contain 32 statements: 18 Proved, 7 Refuted, 5 Known and 2 Open. “Refuted” identifies the proposed assertion being rejected; its text and proof specify the corrected conclusion or counterexample. “Open” means the exact remaining task is not resolved in this manuscript; it is not a claim of priority or of a newly discovered open problem.

### Main conclusions and the variance audit

The presheaf fine test is `s\X -> s\Y`, and the covariant test is `X/s -> Y/s`. Their enhanced localizations for the minimal localizer are respectively `Fun(NS^op, Spaces)` and `Fun(NS, Spaces)`. B.3 gives inverse relative functors, including natural weak-equivalence comparisons, through the simplex category and its last vertex. It proves an equivalence of infinity-localizations; it does not invent a model structure on `Cat/S` for which the ordinary nerve is a Quillen equivalence.

For simplicial sets, the literal strict-slice test works over a quasicategorical base even for arbitrary, nonfibrant total simplicial sets. Over an arbitrary simplicial base one must use the appropriate fibrant replacement of the vertex. B.4 supplies the inner-horn counterexample: over `Lambda^2_1`, the left-anodyne inclusion of vertex 0 into edge 01 pulls back along the literal slice over 2 to the empty-to-point map. B.22 restores the all-base statement using the actual covariant and contravariant structures, and proves the maximal preservation property directly.

The smooth/proper dictionary is fixed by explicit outgoing and incoming lifting categories. Grothendieck-proper equals Cisinski-proper and HTT Lurie-smooth. Grothendieck-smooth is the opposite class. The current Cisinski errata matter: the general quasicategorical fibre-to-comma criterion needs universal base changes, whereas the ordinary-category nerve criterion used here remains valid. The July 31, 2026 errata were opened and checked.

The manuscript's `Wg` at XII ms.222 is the covariant `X/s` class. Its maximal universal raw-pullback-preserving class is exactly `Liss_W`. For presheaf variance the maximal class is `Prop_W`. B.6 proves both, without accessibility, by Maltsiniotis's universal preservation characterization of aspherical functors and the explicit comma/Grothendieck resolution. It does not confuse this stabilizer with the larger transporter of II ms.88–89.

### Complementarity and the coefficient examples

B.9 proves that `Liss_W intersect Prop_W` is contained in the intrinsic universal pullback-preserving class exactly for the minimal localizer and the total class. Accessibility is not assumed. The proof factors arbitrary categorical maps through minimal smooth and proper maps, obtains homotopy-pullback stability, and loops a noncontractible aspherical fibre until disconnected. Pulling back two points in different components then makes the empty category aspherical and forces the total localizer.

The requested tests are handled independently:

- `W0`: the finite regular `C2` covering.
- Every finite truncation `Wn`: an explicit sphere face-poset and its fully specified fence-path category; B.12 gives a finite witness for `W1`.
- Every nonzero spectrum homology localizer: the same three-sheeted free-group action covering and the same endomorphism, with a proof that includes nonconnective spectra.
- Rational locally constant complexes: a finite central `C2` cocycle extension of the tetrahedral-sphere face poset. Its total category is simply connected, while its self-pullback has fundamental group `C2`. The original map is a rational local-system equivalence; its self-pullback is not.

The rational local-system criterion is justified through modules over rational based-loop chains and Rivera–Wierstra–Zeinalian's Theorem 3. This avoids identifying rational homology with invariance of locally constant rational complexes. In particular, coverings preserve `W1` and rational local-system equivalences, so the three-sheeted homology witness is not a witness for those coefficient localizers. The fence path over `BC2` likewise preserves those two classes while failing rational homology preservation.

B.14 proves that cohomological fibrations, with all local coefficients after all base changes, and `W_D^lc`-proper maps have neither containment for nonterminal presentable coefficients. A universal deformation-retraction example gives one direction; a proper cosieve with nonconstant right direct image gives the other. The dual assertion is also proved. B.15 reconstructs all finite maps in GALOIS D.3–D.5 and records the smooth, proper and intrinsic classifications for both requested localizers.

### Path-model audit

The integer-fence construction is specified on objects, arrows, composition, endpoint conditions and parity of the finite-support extensions. B.8 proves the fixed-left contraction and two lifting conditions; B.19 independently proves the full endpoint result and mapping-path factorization. For `[1]`, the endpoint map has no terminal incoming lift and no initial outgoing lift because the transition can be moved arbitrarily far along the fence.

B.20 retains the actual category of finite interval types. It proves smoothness by adjoining the endpoint arrows, factoring through a slice with terminal object and padding source paths with identity edges. Properness fails because the empty type has no endpoint-preserving map to a nonempty type; the fibration claim fails because two distinct type collapses yield two morphisms to any proposed terminal lift. Thus reversing interval words does not reverse the indexing category of types.

B.21 verifies the standard fence obstruction for the five-element rectangular-band monoid. Existence of a different bifibration representative remains open, exactly as stated there. Neither the complementarity proof nor the abstract factorization uses such existence.

### Presheaf and strict higher category boundaries

C.1 gives two completely specified comma-test localizations via categories of elements for any presheaf category. C.2–C.3 show why this does not automatically extend the simplicial pair: for a component-detecting localizer one of these classes contains only isomorphisms, and every presheaf map is elementwise smooth while elementwise properness demands cartesian naturality squares. Even on `A=Delta`, these two candidate localizations are not equivalent. This is a refutation of the specified automatic transport, not a claim that no richer directed structure can be placed on that model.

C.4 states the extra data that suffice: an involutive equivalence preserving the absolute weak class and exchanging the two chosen test classes. Simplicial reversal comes from an automorphism of `Delta`, not from a false identification `Delta=Delta^op`. A test category provides an absolute homotopy theory; it does not select directed slices or an exchange involution.

For strict higher categories, C.5 resolves the exact Theorem A reference and its slice convention. C.6–C.7 prove formal fine duality in every dimension by total cell reversal, and describe the full commuting family of cell dualities. The decisive published source is Ara–Maltsiniotis (2022), Theorem 6.6, with the total-dual slice isomorphism in the proof of Corollary 6.8. These conclusions use no September 2026 model claim.

C.8 records the verified published dimension-two Thomason theorem. C.9 states precisely what an absolute model theorem would imply: the coarse slice of spaces. C.10 leaves the relative Street-nerve comparison and the higher local base-change criterion unresolved. Theorem A and an absolute Quillen equivalence do not by themselves provide those comparisons. The statement names the missing maps and does not simply label all higher-category work open.

### Primary literature and novelty checks

The supplied primary PDFs of Cisinski (2006, 2019), Lurie, Maltsiniotis (2005), and Evrard (1975) were read or extracted at the locations recorded in the bibliography. Online primary checks opened:

- Cisinski's current author errata, especially Theorem 4.4.36.
- Ara–Maltsiniotis, *Un théorème A de Quillen pour les infinity-catégories strictes I: la preuve simpliciale*, Theorem 5.2 and Remark 5.3.
- Ara–Maltsiniotis, *Comparaison des nerfs n-catégoriques*, Sections 6.4–6.8.
- Ara–Maltsiniotis, *Vers une structure de catégorie de modèles à la Thomason…*, Theorem 6.27 and Corollary 6.32.
- Rivera–Wierstra–Zeinalian, *Rational homotopy equivalences and singular chains*, Theorem 3.

Searches included the exact names “Cisinski 4.4.36 proper smooth nerve,” “Maltsiniotis structures asphericite smooth Theorem 1.2,” “Ara Maltsiniotis Theorem A strict infinity categories,” “Comparison n categorical nerves duality,” “Thomason 2 categories Theorem 6.27,” and “Rivera Wierstra Zeinalian rational homotopy Theorem 3.” Author pages, author PDFs, arXiv primary manuscripts and primary journal records were used; search snippets or earlier AI answers are not theorem authorities. Some journal landing pages timed out or rejected XHTML; the corresponding complete author PDFs were successfully opened. No novelty claim is made for any of the deductions or counterexamples.

### Reproduction and exact computational scope

Run from the workspace root:

```
python BISITE/code/bc_counterexamples.py
python BISITE/code/bc_inherited.py
python BISITE/code/bc_paths.py
python BISITE/code/bc_register.py
```

The first program checks finite category laws, the central-extension lifting equations, full nonabelian group presentations, diamond and V examples, simplex intersections and the covering permutations. It produces `bc_counterexamples.out.json`. The inherited-example checker produces `bc_inherited.out.json`; the rectangular-band checker produces `bc_paths.out.json`. `bc_register.py` rebuilds both CSV registers and checks claim IDs, statuses, cited keys and verification flags, producing `bc_register.out.json`.

The exact presentation reductions are elementary Tietze substitutions after a spanning-tree collapse. For `H` all 73 generators are eliminated; for `H x_K H` 172 of 173 generators are eliminated, leaving the order-two relation. There is no probabilistic group recognition or floating-point linear algebra. The proof gives the geometric disk argument as well, so the software is an independent verification rather than the mathematical justification.

`bc_extract.py` records reproducible text extraction of supplied primary PDFs. It requires `pdftotext` and the supplied `background` tree. Its output is an extraction log, not an assertion that every page of each book was used. All other programs use Python's standard library only.

### Cross-review of Parts E and F

The completed E.1–E.9 and F.1–F.14 were read for variance and adjunction scope. The raw-pullback exception in E.2 agrees with the classes proved here. The recognition assumptions in E.3 explicitly carry the required colimit and generator data. The left and right Kan formulas and the mate-based converse in F.2 have the correct presheaf variance. F.10's correspondence construction is consistent with its chosen ordinary categorical base and the 2022 geometric-setup convention; F.12 correctly separates the later diagonal condition and verifies the discrete-fibration repair. No change was requested to those statements. The review did not certify the later moduli-space arguments F.15–F.17.

## BISITE D/G audit report

AI-produced by GPT-6 Astra, OpenAI, ChatGPT Pro mode. No priority is claimed.

### Scope and deliverables

This contribution owns Parts D and G. The finished section files are `sections/D.tex` and `sections/G.tex`. Their registers are `sections/D_results.csv` and `sections/G_results.csv`; every register has the requested seven columns. There are 27 numbered statements: 10 Proved, 8 Known, 8 Refuted, and 1 Open. “Open” means not settled by this audit, not asserted to be an open problem in the literature.

The separately mergeable bibliography is `sections/DG_references.bib`. Every entry contains an explicit `verified` note specifying the source actually inspected and the theorem or section used. There are no entries whose existence or contents were inferred only from a bibliography or search snippet. The Groth–Šťovíček theorem was read in the supplied LaTeX; publication details and printed numbering were independently checked in primary sources.

### Main decisions

#### Topological open tests

D.1 distinguishes the localization of actual spaces over a base from a coefficient category of sheaves. Sending `X -> Y` to the inverse-image homotopy types of opens gives a canonical hypercomplete cosheaf. Its existence alone does not establish that every cosheaf is represented, nor that localization has the required mapping spaces.

D.2 supplies a complete positive theorem for every finite downset Alexandrov base and every discrete base. Its proof gives an ordinary relative adjunction, so it proves full faithfulness after localization as well as essential surjectivity. For a finite poset P, the left functor records the subspaces lying over principal downsets. The right functor gives the disjoint union of diagram values a topology generated by inverse images of opens along its structure maps. The counit at p deformation retracts the part over P≤p onto F(p). The homotopy is a jump only at its final time; continuity is verified on each topology generator. If p≤q, membership is unchanged throughout; if p≰q, the section never meets the generator and its preimage is an open subset times [0,1). These are the two exhaustive cases. The triangle identity gives the unit, and finite open-cover induction promotes principal-open tests to every open.

The result allows non-Hausdorff total spaces. No Hausdorff restriction is silently added to Top. Strict diagram rectification is supplied separately by HTT 4.2.4.4, rather than inferred from an equivalence of the unindexed homotopy theories.

D.4 is an explicit obstruction to identifying geometric proper base change with strict pullback of this open-test class. The map `(0,1] -> [0,1]` is a weak equivalence over every open of `[0,1]`, while its pullback to the proper closed endpoint `{0}` is `empty -> point`. All spaces are locally compact Hausdorff. Thus a six-operation coefficient theorem cannot justify the asserted raw-pullback statement.

D.5 proves strict preservation along maps locally of product form. D.7 gives a precise shape-submersion class with an additional essentiality hypothesis, where the left adjoint to inverse image exists. Its local compactness assumption is the one explicitly imposed before Volpe's Lemma 3.26 and is retained after base change.

D.6 and D.8 state ordinary sheaf proper base change and stable Verdier duality under their exact coefficient hypotheses. In particular the operation defined through proper support is distinguished from the left adjoint to ordinary inverse image: their values on a constant sheaf on the real line differ by a shift.

#### Finite weights and dualities

The main correction to Lead 4 is a variance correction. The canonical weight for a limit of presheaves on S is a covariant spectral diagram on S. The correct formula is a derived coend, proved in G.2 from coherent Yoneda and finite-limit/colimit commutation. It is not pointwise tensoring by a presheaf followed by the ordinary colimit on the same index. G.3 disproves that interpretation for the two-object arrow: a presheaf `(M -> 0)` has limit M but every pointwise-twisted colimit is zero.

G.4 gives composition and transitivity at the level of spectral Kan-extension kernels and explains exactly which Beck–Chevalley mate induces a kernel equivalence. G.5 disproves unqualified restriction invariance of the weight. G.6 supplies a separate contravariant duality on finite spectra or perfect modules, preserving the opposite coefficient ring when necessary.

G.7 demonstrates why “finite EI” is not a coefficient-independent enlargement of “homotopy finite.” For `BC2` in characteristic 2, homotopy fixed points fail a countable coproduct. The proof uses a bounded-above free resolution and explicitly obtains the inclusion of a countable direct sum into a countable product. The finite program verifies the resolution's algebra, while the manuscript proves the infinite step. G.8 supplies a valid positive finite-group class when group order is invertible in the coefficient ring.

The literature search found Aoki's exact criterion, which replaces a broad unresolved-duality discussion by a known classification of the canonical transform. With the paper's presheaf convention, Aoki must be applied to `P opposite`: his strict lower intervals become our strict upper intervals. G.9 accordingly requires every `P>p` to be Gorenstein*. The transform always expresses the limit as a colimit on the opposite base; it is an equivalence precisely under that criterion for spectral coefficients. Its extension to every stable derivator is explained through invertible spectral bimodules, using the canonical spectral action, so no enhancement of the given derivator is assumed.

G.14 separately records the positive reflection-equivalence theorem for oriented trees. These equivalences can exist even when the canonical Frobenius transform is not invertible. The criterion in G.9 is not misrepresented as a classification of all abstract equivalences between diagram categories.

#### Geometric dictionary and Verdier support

G.10 independently verifies the specific STRATA dictionary used by D and G. It proves continuity of the minimum map, gives the explicit lower-cone times upper-cone charts, checks contractibility of strata, and computes the exit category by combining the simplex-face exit calculation, the precise HPT coarsening theorem, and Kerodon's last-vertex localization. The coefficient extension is restricted to the exact compactly assembled or stable presentable classes in HPT Corollary 4.1.15. In particular the arbitrary-presentable-coefficient gap from STRATA is not silently filled.

G.11 computes a very small geometric obstruction: on the closed interval with minimum strata `[0,1)` and `{1}`, the constant sheaf is constructible but its usual Verdier dual has zero stalk at the endpoint and a shifted field at every interior point. It is not constructible for those minimum strata. The calculation is via explicit local relative cochains and does not rely on an unexamined slogan about boundaries.

G.12 gives the correct positive geometric comparison from Aoki Theorem 6.13: pull back to the realization, apply Lurie's sheaf–cosheaf Verdier duality, and push the resulting cosheaf forward to the finite base. Compact Hausdorff realization, the Gorenstein* hypothesis, and full faithfulness of inverse image are all checked. Opposite face posets of finite simplicial complexes give a concrete class where minimum strata are the actual open simplices, making the cellular interpretation literal.

A further proof pass resolved the previously isolated general-proper-map issue. **D.11 now proves the comparison for every categorically proper map of finite posets**, for spaces, spectra, and derived-ring coefficients. If a target point has support chain σ, its geometric fibre is a finite polytopal complex whose cells are the chains κ upstairs mapping onto σ; each cell is a product of open simplices. The cell-poset minimum functor to the opposite of the fibre over the minimum of σ is homotopy initial. Its comma categories are proved contractible by adding the chosen minimum, deleting other first-level vertices, and inducting over the remaining target chain using the proper lifting posets. This proves the needed comparison at every interior simplex point. The canonical counit mate is then checked on stalks, and finite-polyhedron hypercompleteness detects its equivalence. The proof does not assert a stronger exit-category equivalence for the entire fibre.

D.13 supplies a specified dual geometric operation for smooth finite-poset maps on perfect coefficients. Coefficient duality changes a presheaf to a sheaf on the maximum-stratified realization, D.11 applies to the opposite proper functor, and covariant Verdier duality converts geometric proper direct image to cosheaf pushforward. The resulting realization is contravariant and its target subcategory is described explicitly as a Verdier image. It is not misidentified with literal constructible cosheaves for the minimum stratification.

### Precisely unresolved assertion

**D.12.** For a general locally compact Hausdorff base, the canonical functor from the open-test localization of all spaces over the base to cosheaves is not proved to be an equivalence. The first unproved base in the supplied construction is the real line, which has no smallest point neighbourhoods. The proposed “dual localization” of Top/Y also needs an actual specification and representation theorem. Closed-set tests define a different class, as D.4 shows, but do not by themselves prove a sheaf equivalence. The search found no primary theorem establishing this unrestricted representation assertion. These are recorded as missing proofs, not as refutations.

### Source checks

The following primary sources were actually opened, either as attached material, full author/publisher documents, or both. Exact source pointers are retained in the bibliography.

| Source | Exact content checked | Use |
|---|---|---|
| Lurie, *Higher Algebra*, 2017 author PDF | 5.5.5.1, 5.5.5.10; A.3.2, A.3.8, A.3.10; A.6.4, A.6.10, A.9.3 | Open cosheaves, stable Verdier duality, finite exodromy |
| Lurie, *Higher Topos Theory*, supplied 2017 revision of 2009 book | 4.2.4.4, 4.2.4.5, 7.3.1.18, 7.2.3.7, 7.2.1.12 | Diagram rectification, proper base change, finite-polyhedron hypercompleteness |
| Volpe, *The six operations in topology*, 2025 publisher full text | Definition 3.23, condition before Lemma 3.26, Lemmas 3.26–3.27; Section 6.1 and Proposition 6.9 | Shape submersions, support, bicomplete stable coefficients |
| Groth–Shulman, 2017 arXiv v1 and attached LaTeX | Theorems 2.14 and 4.11(iv), Construction 4.8, Lemma 4.10 | Stable weighted-colimit theorem |
| Cisinski–Tabuada, 2011 publisher PDF | Definition A.1 and Theorem A.11, Appendix A.3 | Canonical spectral action without strongness |
| Aoki, 2022 arXiv v1 full PDF | Theorems A, C, D and 6.13; Definition 3.9; Propositions 3.11 and 5.12; Remark 6.14 | Exact canonical finite-poset duality and geometric comparison |
| Haine–Porta–Teyssier, author PDF dated April 26, 2026 | Theorem 3.3.5 and Corollary 4.1.15 | Coarsening and coefficient scope |
| Kerodon, online November 11, 2026 | Proposition 6.3.6.2, including proof | Last-vertex localization |
| Groth–Šťovíček, supplied `tilting2.tex` | Source reflection theorem and tree corollary, printed 9.19 and 9.23 | Universal stable equivalences for trees |

The abstract/source of Jansen's attached paper was extracted as a possible geometric source but is not used to supply an unverified theorem. Ladkani's primary paper was consulted during the search for general opposite-poset equivalences; no result from it is invoked in the finished text. No claim that all finite posets fail to be derived equivalent to their opposites is made.

Representative search directions were “Top/Y localization cosheaves weak equivalences on opens,” “shape submersion smooth base change,” “finite poset Verdier duality,” “stable derivator spectral action no strongness,” and “tilting theory trees Corollary 9.23.” Only primary mathematical sources were used to support the final assertions. This was a targeted search, not a claimed exhaustive literature review.

### Reproducibility

`code/dg_extract_sources.py` extracts the relevant supplied PDFs; its captured output is `code/dg_extract_sources.out.txt`. Extracted working texts live under `research/dg` in the shared workspace and are not a required deliverable.

`code/dg_finite_checks.py` uses only Python's standard library. It outputs `code/dg_finite_checks.out.json` and verifies all its assertions. The output contains complete objects/arrows/composites for the finite posets used, all six candidate fork anti-isomorphisms, the endpoint comma calculations, the arrow-weight values, the C2 multiplication and differential matrices over F2, small order-complex reduced Betti numbers, interval local relative-cochain ranks, and the unstable product counterexample. It makes no claim that finite truncation proves the infinite non-preservation result in G.7.

`code/dg_validate_artifacts.py` checks register/claim identity, status labels, proof delimiters, cited bibliography keys, and explicit verification notes. Its captured output is `code/dg_validate_artifacts.out.txt`.

`code/dg_proper_fibres.py` independently checks the new D.11 construction on all 50 naturally labelled posets with one through four objects. It tests all 1,584 monotone maps to the three-object chain, retains the 152 with beat-contractible outgoing lift posets, and checks rational acyclicity of all 794 minimum-comma posets across 432 nonempty fibre cell posets. The largest tested comma has 15 objects. Its output is `code/dg_proper_fibres.out.json`. This is a finite consistency check of the actual variance and comma construction; the manuscript's induction, not rational homology alone, proves homotopy initiality.

The final compilation and validation are documented in the combined build and validation outputs.

## Parts E and F: hypotheses, operations, and geometric checks

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

### The abstract theorem and the finite intrinsic floor

E.1 proves what the bare universal-test recipe supplies: postcomposition is relative for every base map; raw pullback is relative along the testing class; the slice adjunction descends when both functors are relative. E.2 gives the explicit endpoint obstruction to extending raw pullback to every map. The derived inverse image on a fine localization must therefore be constructed.

E.3 is an enhanced recognition theorem with explicit sufficient hypotheses. The slice localization has a fully faithful small family of compact projective generators, with mapping spaces preserving all small colimits, and postcomposition preserves colimits and takes generators coherently to generators. Restricted Yoneda identifies the localization with a presheaf infinity-category. The proof constructs the inverse through the category of elements, checks the unit on representables, checks the counit by joint conservativity, and identifies postcomposition with left Kan extension. Restriction then has both Kan adjoints. Groupoid completion supplies reflection and coreflection of locally constant diagrams.

These assumptions exceed the finite intrinsic floor. E.7 proves the non-formal Brown axiom from terminal objects, pullbacks, two-out-of-three, and enough intrinsic fibrations: a weak intrinsic fibration remains weak after any pullback, by factoring the base map. The resulting category of fibrant objects supplies finite homotopy limits and finite inverse diagram rectification. Neither all-small diagram rectification nor a fine-site presentation follows. E.3's generator and colimit hypotheses are not attributed to the factorization axiom.

E.4 extends a verified presentation to presentable coefficients and exact comma comparisons. E.5 checks the categorical, simplicial, finite Alexandrov and discrete-base instances. The coarse comparison is separately stated and checked for the minimal localizer. E.6 refutes its extension to all fundamental localizers: over BC2, the regular C2-set and the terminal C2-set are distinct locally constant fine objects, but their representing total categories become equivalent for the component localizer.

E.8 checks the accessible equivalences among enough intrinsic fibrations, aspherical generation, set generation by maps to a point, right properness and nullification. Necessity of aspherical generation does not need accessibility; the passage to a set-generated proper model does. E.14 includes the modality and locally cartesian closed equivalences. Its reverse LCC argument uses space-indexed colimits of points over a local base; it is not asserted for an arbitrary ambient topos. The modality's right class differs from intrinsic fibrations, and its left class can be smaller than the class inverted by the reflector.

E.9 records the actual path-object transfer: universal weakness of source evaluation is needed to deduce weakness of the mapping-path inclusion. The categorical fence model, simplicial Kan replacement and topological path-fibration cases are distinguished. The topological path-fibration assertion does not identify Hurewicz fibrations with geometric proper or shape-submersive maps.

E.10 proves the groupoid test independently of the 2026 claim. For groupoids over a groupoid base, both comma fine theories collapse to the coarse families of 1-types. Arbitrary strict tests can retain presentation data: a one-object inclusion into the walking isomorphism is an equivalence but has an empty strict fibre at the other object.

E.11 gives the sufficient coaugmented replacement hypothesis for every intermediate-subcategory comparison. E.12 settles XIIc B062 by the six-element lattice counterexample in the Part A audit, including enhanced localizations. E.13 gives a coherent-arrow obstruction: the coherent mapping set is Z while the underlying arrow category of the homotopy category has one morphism.

### Derivator operations and corrections to Lead 3

F.1 uses Der 1–4 and the presheaf convention. Pointwise formulas, exact comma squares and mate pasting are distinguished from strongness, pointedness and stability. The printed Groth (2013) Definition 1.5 gives the axioms; Definition 1.10 concerns opposition. The initially considered 1.10 pointer was corrected before delivery.

F.2 proves the two strict Beck–Chevalley theorems. Left base change holds for a smooth vertical or proper horizontal map. Right base change holds with those roles reversed. The converse takes the left adjoint mate of the right comparison and evaluates it on the terminal space; its summands are the lifting categories. This agrees with STRATA D.4. Evaluating the original right comparison on the terminal presheaf would be vacuous, but that is not the supplied proof.

F.3 supplies finite endpoint counterexamples to unrestricted pullback base change and their stable versions. F.4 proves the internal left projection formula for smooth maps or locally constant second coefficient, and the external formula for all maps. F.5 refutes the unrestricted internal formula, even in spaces or spectra. An external separately cocontinuous tensor cannot be confused with internal tensor of two varying diagrams.

F.6 gives precise right projection hypotheses: a globally dualizable coefficient always suffices; for proper maps, preservation of the actual fibre limits also suffices. Stable coefficients with homotopy finite fibres are a positive case. The two-point projection in spaces gives the diagonal from two elements to four and refutes the unrestricted formula.

F.7 spells out closed exchange and the right-adjoint mate of left base change. F.8 explains VI ms.84: base opposition exchanges incoming and outgoing tests, while reversing adjunction directions additionally takes opposite coefficient categories. Base opposition alone is not a coefficient duality over a fixed base. Separate cocontinuity need not survive opposition.

F.9 supplies zero extensions and coherent open–closed sequences with exact sieve/cosieve variance. Strongness is used for the resulting triangulated structure, not for the coherent constructions.

### Correspondence formalisms and version control

F.10 constructs a lax symmetric monoidal correspondence functor from the nerve of ordinary Cat with strict pullbacks and smooth right legs. An enhanced coefficient category is input. The specified Beck–Chevalley mate gives composition, and the common iterated pullback and contractible universal property of Kan adjoints with their units supply higher coherence. External tensor gives the monoidal structure. Mann (2022), Definitions A.5.1, A.5.6 and A.5.7, specify the formalism used.

F.11 distinguishes this terminology from categorical properness. On the allowed Kan class exceptional inverse image is restriction with trivial twist. A categorically proper map need not equate left and right Kan extension: the walking-arrow projection evaluates different endpoints. Finite discrete bifibrations give canonical stable ambidexterity.

F.12 records a material definition change. Heyer–Mann (2024) require diagonal closure; Mann's 2022 Definition A.5.1 does not. The walking-arrow diagonal is not smooth, so the all-smooth setup fails the later convention. Discrete fibrations form a diagonally closed subclass. Neither setup silently replaces strict pullbacks in ordinary Cat by general infinity-categorical pullbacks.

F.19 supplies an exact classification in that smaller setup, for spectra or modules over a nonzero commutative ring: cohomological properness is equivalent to universal Kan ambidexterity and to being a discrete bifibration with pointwise finite fibres. Vertex pullbacks force finiteness by the failure of infinite products to preserve filtered colimits. Arrow pullbacks force each fibre transport to be bijective by an explicit star limit, the fibre of the diagonal M→M^m. The converse identifies the canonical norm with the finite biproduct map. The diagonal's properness is checked before invoking Heyer–Mann Lemma 4.6.4(ii), so the proof does not presume a norm exists for every discrete fibration. Definition 4.6.1 and Lemmas 4.6.3–4.6.4 were additionally opened at printed pp.74–76.

F.13 applies Hörmann (2017), Theorem 6.12, with its actual pre-multiderivator and Der 1–2 hypotheses and its diagram-correspondence base. It is not a formalism on all strict spans with unrestricted Beck–Chevalley. F.14 identifies the Anel–Weinberger calibrations for this particular indexed presheaf category. Its reference is arXiv version 5, dated February 2025, whose numbering was checked; the 2024 journal version is recorded in the bibliographic note.

### The genus-zero forgetting example

F.15 specifies the entrance category as the opposite of Jansen's mapping-class quotient category. Objects, arrows, twist quotient and composition are explicit. Forgetting a mark defines an actual functor: vanishing twists go to the identity and repeated curves have the same image twist. This is checked against the generators of geometric degeneration. The stable range is 2g−2+n>0; the second inequality printed in the attached Theorem 6.7 has a sign slip.

F.16 proves properness of forgetting a mark for every n≥3. A lifting category is first proved equivalent to a reverse-inclusion refinement poset by normalizing the mapping-class representative. That poset is a tree with possible peripheral leaves, using lifted geodesics and the checked Kent–Leininger–Schleimer Theorem 7.1. Cutting along a fixed multicurve reduces to the stable component containing the extra point or to the explicit unstable bubble and bridge cases. Boundary circles count as retained punctures.

For n=4, a three-component chain with the extra mark in the middle has two twists mapping to one downstairs twist. The bad lifting category is a transitive action groupoid with stabilizer ker(Z²→Z), (a,b)↦a+b, hence is BZ. This proves nonsmoothness. The category is infinite; the code checks the exact integral basis change and does not claim to enumerate it.

F.17 proves the geometric direct-image comparison on constructible coefficients. On a small ball in a fixed dual-tree stratum, normalization and isotopies trivialize the universal curve with its strata. Proper base change proves constructibility of direct image. Compactly generated coefficients are handled by finite-limit-preserving functors on compact test objects. Uniqueness of the right adjoint identifies the categorical and topological operations with their units and counits.

Fibre and boundary comparisons are checked separately. A fibre has punctured-sphere components, circle links at marks and two circle links at nodes. Injective peripheral cyclic subgroups make the exit mapping spaces discrete coset sets, identifying the actual fibre category rather than just its total homotopy type. A boundary is a replete full cosieve selected by a label partition. Cutting gives the component-product description, and its inverse image gives the strict categorical square. The comparisons are mates of the same restriction identity. No theorem for every arbitrary geometric pullback is asserted.

F.18 leaves strict higher indexing unresolved. The first new case needs a higher Der 4 and a relative comma comparison respecting the prescribed mate. An absolute Thomason model theorem alone provides neither.

### Primary-source checks and searches

The bibliography identifies each source and version. Principal checks were Cisinski (2006), Theorems 5.2.15 and 6.1.11 and Example 6.1.14; Cisinski (2009), Theorem 3.13; Cisinski (2019), Theorems 7.5.18 and 7.6.17; Rijke–Shulman–Spitters (2020), Theorems 1.34, 1.54, 2.19 and Lemma 2.20; Groth (2013), Definition 1.5, Proposition 3.6, Lemma 3.7, Corollary 3.8 and Theorem 4.16; the exactness and monoidal statements of Groth–Ponto–Shulman; Maltsiniotis (2012), Sections 1–2; the formalism definitions just specified; Jansen (2023), Construction 3.18, Proposition 3.23, Corollary 6.6 and Theorem 6.7; Kent–Leininger–Schleimer (2009), Section 2 and Theorem 7.1; and Keel (1992), pp.546–548.

For Groth–Ponto–Shulman's Mayer–Vietoris paper, PDF numbering was checked: Theorem 3.8 is the sufficient exactness test, Corollary 3.13 is the cofinality consequence, and Theorem 3.16 is the full characterization. A later HTML conversion had different numbering and is not the source of those pointers. The published Kent–Leininger–Schleimer PDF was opened to verify its title, authors, year, pages and DOI in addition to the author preprint used for the theorem.

Targeted searches included “Groth derivator exact squares terminal mate,” “Mayer Vietoris derivators Theorem 3.16,” “Mann A.5.1 geometric setup diagonals,” “Heyer Mann cohomologically smooth,” “Hörmann Theorem 6.12 multiderivator,” “Anel Weinberger Definition 2.3.1,” “nullification locally cartesian closed localization spaces,” “Jansen stable curves forgetful exit category,” and “Kent Leininger Schleimer trees mapping class groups fibre.” Earlier AI packages were checked as leads. These searches imply no novelty claim.

The two OpenAI manuscripts were opened for their titles, dates and claimed statements. Their bibliography's verified notes explicitly mean source identification and statement reading, not certification of proofs or formalizations. Only C.9 above dimension two conditionally uses the first claim. All unconditional conclusions and the groupoid test are independent of both.

### Computations and document validation

The program ef_finite_checks.py enumerates the interval, point, empty category, C2 and walking isomorphism, checking identities and all compositions. It constructs the comma categories for E.2 and E.6, computes finite limits and colimits in the base-change and projection counterexamples, and checks the missing diagonal lift. The twist-kernel calculation uses a determinant-one integral basis change. Output distinguishes symbolic descriptions from finite enumeration.

The program ef_register.py extracts complete E/F statements into the seven-column registry. The assembly program unifies duplicate references, checks used citation keys and verification notes, and matches every full statement to one CSV row. The build program records all LuaLaTeX and BibTeX passes. The preparation program supplies only missing public font-loader dependencies to a local TeX tree and records official CTAN URLs and hashes. Rendering and finite certificates validate the document and the stated computations; they are not a claim of formal machine verification of the complete mathematical paper.
