# Part D: rectification audit and results

## Scope and deliverables

This part addresses Part D of the prompt, including the POLES, GALOIS, STRATA and Kaledin additions. The separate `D_kt.tex` contribution handles `(KT_mu)` and CATHOT E.17; neither is reproved here. The manuscript contribution is `sections/D.tex`, with 23 numbered results. `D_results.json` has a matching record for every result, and `D_references.bib` records the inspected source versions. The executable finite checks are `code/d_finite_checks.py`, with saved output `code/d_finite_checks.txt`.

The distinction between a relative category, its infinity-localization, the localization of its ordinary strict functor categories, and coherent functor infinity-categories is maintained throughout. Covariant shapes are used for the canonical comparison `R_A`; Kaledin's contravariant convention is stated separately. Universe bounds are part of every infinite-shape assertion. An ordinary finite category with nonidentity endomorphisms can have infinitely many nondegenerate nerve simplices, so it is not silently covered by a finite-direct rectification theorem.

## Principal corrections and positive results

### The finite example does not fail rectification or enhancement

The two-object, five-arrow pointed category E at IX manuscript page 23 has a zero object 0, another object x, and End(x)={1,z} with z squared equal to z. With weak equivalences the identities, it rectifies every shape. Degree by degree, `Fun(NA,NE)=N Fun(A,E)`; ordinary localization does nothing. Its loop objects are the trivial pointed mapping objects, represented by 0 in both variables. Kaledin Example 7.2.1.16 says that the represented family K(E) is enhanced for every ordinary E, without requiring finite limits.

Consequently the prompt's requested failed rectification or failed enhancement axiom for this example does not exist. The actual obstruction is that x times x is absent: Hom(x,x) has two elements, and neither possible object has four maps from x. More generally a finite category with every finite product is a preorder; a pointed such category is equivalent to the terminal category. Results D.2–D.3 settle this correction, and the complete typed composition table and all 34 associativity triples are checked by the program.

### Enough intrinsic cofibrations with an initial object are sufficient for finite posets

D.8 proves all CF1–CF4 directly. Composition and cobase stability of intrinsic cofibrations follow by identifying iterated pushouts. The nontrivial step is cobase stability of a trivial intrinsic cofibration. Factor the proposed base change as an intrinsic cofibration followed by W; the first change is weak because the factor is intrinsic, the intermediate comparison is weak because the base-changed original map is intrinsic, and two out of three supplies the final comparison.

Cisinski's canonical infinity-localization theorem, Theorem 7.6.17 in the attached book version, now applies to every finite direct category, including every finite poset and every span. This proves that no finite-poset counterexample satisfying the additional initial-object hypothesis can exist.

The conventions are audited rather than merged. Rădulescu-Banu's CF1–CF4 allow noncofibrant objects. Szumiło's attached convention additionally requires every object cofibrant and two out of six. Lenz's ABC convention has CF5 and CF6, including arbitrary permitted coproducts and countable composites. The four-element diamond with W consisting of identities and the two maps out of the least element has enough intrinsic cofibrations but two noncofibrant objects. Finite sets with isomorphisms satisfy the finite hypotheses but have neither a countable coproduct of singletons nor the indicated increasing sequential colimit. Thus no infinite ABC axiom is being smuggled into D.8. The two-out-of-six strengthening itself has not been separately derived from the intrinsic hypotheses; no claim that it fails in the diamond is made.

### All cubes are insufficient

Let P be the six-element face poset of a triangle boundary, with every arrow weak. For any shape with an initial object, evaluation at that object is a nerve homotopy equivalence from its strict functor category to P, and the coherent target has the same property. Hence every cube rectifies. At the finite poset P itself, strict endofunctors have degree -1, 0 or 1, whereas coherent endomaps of its circle realization have every integer degree. Degree two is missing. The exhaustive enumeration finds exactly 234 monotone maps: 3 of degree -1, 228 of degree 0, and 3 of degree 1. D.10 refutes the proposed cubical criterion.

### Finite posets do not suffice for BZ; BK fibrancy is independent of all-shape rectification

Finite simplicial sets, with monomorphisms and weak homotopy equivalences, form a finite cofibration category. Mapping cylinders give finite factorizations. Thus they rectify every finite direct shape by Cisinski, without invoking the infinite ABC theorem. A strict BZ action is an actual simplicial automorphism of a finite simplicial set, so has finite order. The coherent action on a wedge of two circles given by the Nielsen self-equivalence has first-homology matrix [[1,1],[0,1]], of infinite order. An equivalence of coherent actions would conjugate monodromy and cannot identify these orders. This proves the requested finite-poset versus BZ example.

The opposite relative category is a fibration category and therefore is fibrant in the usual BK structure by Meier Theorem 4.13. It still fails at BZ. The non-opposite cofibration category is covered by Meier's conjugate BK structure, not automatically the same structure.

Conversely the nine-vertex fence 0<1>2<3>4<5>6<7>8, with all arrows weak, has a fixed eight-step natural-transformation contraction. This contracts every strict functor category, even at infinite shapes, so every R_A is an equivalence. But the zeroth level of its BK nerve is Ex squared of NF. Its edges are monotone maps from the five-vertex fence. There are edges 0 to 4 and 4 to 8, and no edge 0 to 8, yielding an unfillable inner two-horn. D.11–D.12 prove both all-shape nonimplications. They do not settle whether BK fibrancy alone gives finite-poset or finite-category rectification; that narrower target is explicitly Open in D.22.

### Relative poset presentations do not give naive diagram rectification

D.13 gives two constructions. The finite circle poset P maps to the ordinary group category BZ by labeling one incidence edge with a generator and the others with zero. This is an infinity-localization, but every strict BZ diagram in P is constant and has trivial monodromy. The coherent target has components indexed by integers.

For a finite target and finite test shape, the explicit countable poset Q consists of orbits of nonempty finite signed subsets of N times {+,-}, with at most one sign per index, under simultaneous sign reversal. Order is inclusion after sign alignment. Its nerve is the quotient of the barycentric subdivision of the infinite join of S0's, hence has type RP infinity. Normalize each representative by making its least-index sign positive; send an order relation to the unique aligning sign. This defines Q to BC2 and presents BC2 by inverting every arrow. Yet strict BC2 diagrams in a poset are constant, and the canonical comparison misses the identity homomorphism C2 to C2. The full multiplication law and both homomorphisms of C2 are checked. Kerodon Theorem 6.3.6.1 supplies the general presentation theorem, but is not used as an unsupported assertion of strict rectification.

## Kaledin comparison, with body-level verification

The attached paper is arXiv:2409.17489v3, dated 23 February 2026, 602 pages. The arXiv record says Chapters 6 and 7 are preliminary. It is treated as a preprint theorem, not asserted to have been refereed or independently reconstructed in full.

The following body passages were read: Definitions 2.1.5.3–2.1.5.4; Definitions 7.1.1.1–7.1.1.2 and 7.1.1.9; Definition 7.1.4.6; Definitions 7.2.1.1, 7.2.1.3, 7.2.1.4 and 7.2.2.1; Example 7.2.1.16; Proposition 7.2.3.7 and its proof; Lemma 7.2.4.1; Lemma 7.3.1.1 and its expansion formulas; Theorem 7.3.1.3 and its proof; Corollaries 7.3.1.5–7.3.1.6.

The shape correction is material. `Pos` consists of finite-chain-dimensional posets, not finite posets. `Pos+` consists of left-bounded posets, while `Pos+-` consists of left-finite posets. An infinite discrete set belongs to all three. The lower-case `pos` is the finite-poset category. The uncountable regular bound in the representation theorem is retained.

The axioms concern the family jointly: conservative point evaluations, the specified reflexive adjunction, fullness and essential surjectivity of the arrow comparison, arbitrary permitted disjoint-union additivity, semiexactness, and the prescribed excision/cylinder/semicontinuity squares. The extension proposition starts with a **good** family on left-finite posets; it does not extend arbitrary finite-poset data. Lemma 7.2.4.1 identifies its model-category extension with the naive larger family only with the stated completeness assumption.

D.15 resolves the representing-object question. A fibrewise localization map `ell:K(M) -> D` has fully faithful precomposition on cartesian functors and their modifications. This follows from ordinary localization in each fibre, including uniqueness of descended natural transformations and of restriction coherences. Enhanced functors in Definition 7.2.2.1 are precisely cartesian functors; they are not required to preserve Kan extensions. Represent D as K(X). The map ell represents f:NM to X, which inverts W. Factor it as gq through C=L(M,W). The canonical comparison D to K(C) is cartesian, so represents h:X to C. Then hf=q, giving hg=id by the localization universal property. Moreover K(g)theta ell=ell, and full faithfulness of precomposition with ell gives K(g)theta=id. Kaledin's homotopy-detection clause gives gh=id. Thus theta is the specified equivalence, and X is C. The reverse implication follows by transporting the axioms from the coherent family. The result is labeled Known, as a formal consequence of the cited preprint theorem; no independent novelty claim is made.

D.16 supplies an actual failed axiom and an actual admissible infinite shape. For P with all arrows weak and I countably infinite discrete, the additivity functor Pi1 B(P^I) to the product of Pi1 BP is not full. A finite zigzag in P^I gives a uniformly bounded sequence of winding numbers, whereas the product has the unbounded sequence (n). This locates failure at Kaledin Definition 7.1.4.6. Since I is already left-finite, the extension theorem cannot retain all naive left-finite values for this example. The finite E example fails no axiom at all.

D.21 proves a corresponding infinity-level upgrade when R_(A times J) is known for **all** Kaledin Pos shapes J: apply the same recognition argument to the relative category M^A. The finite-J version suggested in the prompt is not established by this argument; it is explicitly left Open with the missing enhancement/comparison step identified.

## The later Grothendieck conditions

Direct manuscript text, not only the companion audit, was read for XIII manuscript pages 7–12 and 50–59; XVII pages 39–40 and the finite Reedy discussion through page 50; XIX pages 33–38 and Question 3.14 at page 48.

XIII's M0 supplies finite limits and colimits. M2, M-prime and M-double-prime give both intrinsic factorizations, so finite-direct rectification follows already before the additional exactness hypothesis. “Exact weak Quillen” means W=TF composed with TC; it is not silently replaced by TC=C intersect W or TF=F intersect W. “Quillenisable” does not by itself imply large colimit completeness: the manuscript expressly considers small and noncocomplete examples.

XVII's Cof0–Cof3 are the finite precofibration axioms with an initial object and with the required pushouts. They therefore give canonical finite-direct rectification. The Brown lemma is correctly restricted to the category of cofibrant objects at XVII page 40. The stronger ambient reading at XIX page 35 is not used without properness C contained in intrinsic Cof_W.

XIX's full Cof4 includes small filtered-colimit existence and transfinite closure of C and its trivial subclass. Together with the finite axioms this gives CF5 by forming a well-ordered coproduct one summand at a time, and CF6 directly. Lenz then supplies all-relative-universe rectification and the left Kan extensions sought in Question 3.14. No functorial factorization or generating set is needed for that deduction. For intrinsic cofibrations, filtered-colimit stability of W makes the transfinite closure argument direct. Functorial factorization alone in XIX Corollary 3.3 does not supply the omitted infinite colimits.

## Localizers and the two-out-of-three warning

D.18 verifies accessible fundamental localizers using Cisinski 2006 Theorem 5.2.15: the Thomason model structure exists and is left proper without a right-properness assumption. Enough intrinsic fibrations is stronger. The Brown direction gives W=W_asph, and Theorem 6.1.11 identifies aspherical generation with properness; the same book connects this to model right properness. Raw Cat is not pointed, so the pointed tests are applied in its pointed model category rather than misusing the unpointed category.

D.23 checks the claimed asymmetry for every nonzero homology spectrum, including nonconnective spectra. Any E-aspherical space A is connected and has no nonzero homomorphism pi1(A) to Z, since such a map would split S1 off A and split Sigma E off zero. Thus every free-group classifying space BF is null for all E-aspherical A. Take the free-group endomorphism alpha(x)=x, alpha(y)=yxyx^-1y^-1. Its stable graph map is the identity exponent-sum matrix, so it is an E-equivalence for every E. Its image is not the full free group: sending x,y to the transpositions (12),(13) in S3 sends both alpha generators to (12). The mapping-space localizer V_(BF) contains every E-aspherical-to-point generator but excludes alpha; otherwise precomposition on self maps would give a homotopy inverse. Hence W_E is not aspherically generated and cannot have enough intrinsic fibrations. This proof does **not** infer failure of properness merely by pulling an acyclic-map equivalence back along a W_infinity path fibration; that shortcut is invalid.

D.19 retains two out of three as an explicit hypothesis where used. The fully faithful restriction class W_Set^1 fails it on e to BC2 to e. Trivial-action restriction is fully faithful; forgetful restriction on the regular C2-set sees four functions but only two equivariant functions. This does not prevent forming the ordinary localization, but does prevent invoking the cofib/fib axioms on descent alone.

## Source versions and exact citations

| Source | Passages actually inspected | Qualification |
|---|---|---|
| Cisinski (2003), *Images directes cohomologiques...*, AMBP 10(2), 195–244 | Attached PDF; Theorem 6.11; official metadata | The model-category right derivator theorem, with its limit hypotheses |
| Cisinski (2010), *Catégories dérivables*, BSMF 138(3), 317–393 | Definition 1.1, Theorems 1.30 and 2.21, Corollaries 3.20 and 6.21 | Finite derivable theory distinguished from homotopical completeness |
| Cisinski (2019), *Higher Categories and Homotopical Algebra* | Definition 7.4.12; complete statement and proof of Theorem 7.6.17; Theorem 7.9.8 and Remark 7.9.7 | Attached author PDF is actually dated 30 July 2026; theorem numbering refers to that inspected version. Published 2019 metadata verified separately |
| Lenz (2018), AGT 18(6), 3601–3646 | Attached TeX and published PDF; Definition 1.5, Warning 1.7, Theorem 3.33, Corollaries 4.5–4.6 | Not Definition 1.2/Warning 1.4; CF5–CF6 are part of the hypothesis |
| Rădulescu-Banu (2009), arXiv math/0610009v4 | Attached source; Definition 1.1.1, finite/infinite axiom distinctions, saturation discussion | Preprint, revised 8 February 2009 |
| Szumiło (2014), arXiv 1411.0303v1 | Attached Section 1.1, C0–C5 | Exact attached title retained; not silently replaced with one of the later related articles |
| Meier (2016), AGT 16(6), 3271–3300 | Attached source and published PDF; Example 2.5, Definition 2.6, Theorems 4.10 and 4.13, Corollary 4.15 | Main fibrancy theorem is 4.13, not 4.9; distinguish the conjugate structure |
| Kaledin (2026), arXiv 2409.17489v3 | Body passages listed above | Chapters 6–7 preliminary; theorem used with this status |
| Kerodon, tag 02MD | Theorem 6.3.6.1 and proof opened online | General localization presentation, not strict diagram rectification |
| Cisinski (2006), Astérisque 308 | Primary book PDF; Theorems 5.2.15 and 6.1.11, Example 6.1.14 | The accessible-localizer model theorem does not assume right properness |
| Arlin (2020), HHA 22(1), 117–139 | Official title/DOI metadata; arXiv v4 body, Theorems 19,29,37 | Published title differs from earlier arXiv title; author previously Carlson; strict and pseudonatural conclusions distinguished |
| Fuentes-Keuthan, Kędziorek, Rovelli (2019), TAC 34(39), 1220–1245 | Official journal metadata; arXiv PDF Definition 2.8 and Theorems 2.16,3.1,3.4 | Journal PDF fetch timed out; arXiv primary body supplied the numbered passages and is explicitly identified |

No unverified reference is used as substantive support. “Verified” here means source and cited passage were inspected, not that an entire external monograph has been independently reproved. The bibliography notes record version discrepancies and failed fetches. Extracted text under `research/d_text/` is an intermediate local aid and need not be included in the delivered package; the attached source books should not be redistributed as newly authored deliverables.

## Finite computation audit

The pure Python program has no dependencies. It checks E's composition and zero object; exhaustively enumerates W classes and intrinsic cofibrations on three small lattices; checks C2 laws and all endofunctions of its regular set; enumerates all 234 monotone P endomaps and their degree; enumerates all five-fence maps into the nine-fence to detect the missing edge; checks every endpoint retraction; verifies the eight-triangle suspension 2-cycle used for the finite test-(b) failure, including zero boundary and the absence of 3-simplices; checks the Nielsen power formula for n=1 through 100 while the proof supplies the induction; and checks the full S3 multiplication table, all 216 associativity triples, and the two subgroup sizes in D.23.

Finite verification does not stand in for an infinite argument. The infinite-order Nielsen conclusion is proved by its general power formula. The Kaledin additivity failure is proved by a uniform finite-zigzag length bound. The countable poset Q is defined and its classifying-space calculation proved mathematically. All finite base categories have complete relations or composition formulas in the text and complete relevant output in the code file.

## Exact unresolved targets

D.22 leaves six explicitly bounded gaps rather than a blanket failure label: intrinsic finite-only/cardinal-only recognition; finite-poset-product upgrade of a canonical homotopy-category comparison to infinity-level equivalence; BK fibrancy as a sufficient condition for the finite-only shape classes; enough intrinsic cofibrations without an initial object; the exact bounded Cat-hot formulation of IX test (b) and the path-object implication (c) to (b) without Part B's missing comparison; and the unrestricted derivator assertion for nonaccessible fundamental localizers. The sufficient model/ABC/Cisinski conditions, cube counterexample, finite-poset versus BZ separation, relative-poset counterexample, and all-Pos Kaledin recognition do not logically fill these remaining gaps. “Open” records what this package has not settled and does not claim a comprehensive negative literature result.

## Assembly notes

The section uses only standard LaTeX mathematics, `amsmath`, `amssymb`, `amsthm`, `natbib` commands, and the parent `result` environment. It introduces no custom macros and contains no top-level section command; the main manuscript owns the A–E sections. All numbered statements have matching JSON rows. Part D does not require fontspec or any interactive output.
