# TOTASPH research and verification report

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.**

The production date is 10 November 2026, the session date. The supplied prompt has additions dated 11 November; those dates are retained as source metadata. “Open” means unresolved in this work, not necessarily open in the published literature.

## 1. Inputs and deliverables

The attached PROMPT(2).md governs the work. We read the background description, manifest, change record, relevant FABLE overview/addendum, manuscript transcriptions, companion audits, primary papers, and the specified CATHOT material. The unversioned archive has 58 files, compared with 52 in v1 and 56 in v2. All shared files have identical SHA-256 digests, and the unversioned archive contains every file in the other versions. The comparison is recorded in research/archive_audit.json and code/root_extract_sources.py.

The paper follows Parts A–H. Every theorem-like statement has a number, stable source label, and one permitted status. The authoritative root-level CSV is generated from the actual statement environments and final LuaLaTeX auxiliary file. It preserves LaTeX mathematics in its statement field and gives final PDF pages and source locations. Subsidiary ledgers are working audit records. The final statement count and status breakdown are in code/root_finalize.out.txt.

The archive contains the complete paper source and included sections, PDF, global CSV, bibliography, report, README, programs and outputs, complete finite-category tables where used, and independent audit records. Original attachment archives, downloaded articles, OCR caches, and TeX caches are excluded. Bibliographic “verified” means that the specified text or record was opened; the note states the exact scope. It does not certify every claim in a source.

## 2. Main mathematical findings and corrections to the leads

**Lead 1 is proved and strengthened.** The one-source collage is the literal simplicial mapping-cone pushout of the actual covariant element projection. Thus its classifying space is the homotopy cofiber even when the base is not contractible. Finality is exactly nonempty connectedness of the element category. If the base is contractible, integral acyclicity is exactly what the single suspension test detects.

For total categories, the action condition is inherited by connected element categories. Cyclic-subgroup coverings then upgrade integral acyclicity to weak contractibility. Consequently total weak-homotopy asphericity and total integral-homology asphericity coincide for categories. Each is equivalent to nonempty connectedness together with weak contractibility of every component of every covariant set-valued element category. This is not transferred automatically to presheaves, whose quantifier tests only actions restricted along their element projection.

The iteration arguments use actual transition functors. Congruence quotients, localizations, and idempotent completion are handled with specified final functors. The paper also characterizes the canonical homotopy-colimit-to-colimit map for arbitrary simplicial-set-valued diagrams.

**Lead 2 is proved without an asphericity hypothesis.** Its subgroup of integer weights is generated over all targets. Directedness, once established, consolidates finitely many witnesses at one target. The proof uses kernel and image sequences for the difference map between linearized representables. It does not call every diagram free on a set projective.

**Lead 3 is proved.** The right-zero monoid has a contractible nerve, is cofiltered and not filtered, and has the specified circle action category and sphere final image. Two cofiber computations prove the all-degree homotopy types. For the entire rectangular-band family \((I\times J)^1\), totality for \(W_\infty\), totality for nonzero \(W_R\), and filteredness are equivalent to \(|J|=1\), while cofilteredness is equivalent to \(|I|=1\). Infinite sets and the empty-band exception are explicitly covered.

**The filteredness half of Lead 4 is false.** The countable category \(\Delta_{\mathrm{inj}}\) of nonempty finite ordinals and increasing injections has exact integral colimits, hence is totally weakly aspherical, but is not filtered. Exactness is proved by a complete polynomial construction of augmentation-one affine cones. Distinct injections from a singleton cannot be equalized by another injection. The category is not sifted: its two-singleton cospan category has three components.

The converse does hold for every category with a weakly terminal object, hence every monoid and every finite-object category. The proof converts affine equalizers into genuine ones using finite invariant signed measures and least-period descent, including negative coefficients.

The literal homology/exactness biconditional is false because exactness does not impose nonemptiness or connectedness. With both hypotheses, exact module colimits imply total homology asphericity. The converse remains unresolved in the stated generality. The exact affine criterion is proved: module colimits are exact precisely when each connected component of the affine linearization is filtered.

Totality also implies preservation of set-diagram monomorphisms, commuting completion of spans, and the fixed-point property for connected representations. These do not resolve additive exactness. Adámek, Koubek, and Reiterman (1981), A.4 and C.2, explicitly correct and refute the fixed-point-to-exactness implication repeated in older sources. We do not claim totality for their counterexample.

**Lead 5 and B035 are false.** On the idempotent monoid \(\{1,e\}\), the three-element presheaf \(\{i,h_1,h_2\}\), with \(e\) constant at \(i\), is total for every fundamental localizer. It is two representables glued along a split subpresheaf. Every ordinary Kan extension has a contractible element category by the same nerve-union calculation. Its own three-object, six-arrow element category has a final image of type \(S^2\), so is not total for \(W_\infty\), nonzero \(W_R\), or \(W_n\), \(n\ge2\). Minimality is asserted only on this fixed base.

For every fundamental localizer, totality of the element category implies totality of the presheaf, with a converse for subterminal presheaves. The universal converse holds for all presheaves exactly when \(S^2\) is \(W\)-aspherical. The genuine filtered-presentation and ind-right-adjoint criteria remain valid but are strictly stronger than totality in the displayed examples.

## 3. Manuscript audit

Full W(7) and W(7 bis) include reflection implications and must not be replaced by forward gluing. The finite acyclic noncontractible category refutes the full axioms for \(W_\infty\). The conditional Proposition 7 is retained with its actual hypothesis. Fixed-coefficient homology equivalences satisfy full gluing. Proposition 8 and 9(a) survive; 9(b), its retraction repair, and the outgoing-fork corollary are false, including under full homological gluing.

C035 is false even for a couniversal weak equivalence: the three-object, seven-arrow example has a relative contraction surviving every pushout, but a disconnected crossing category. It is also discretely flat. A separate four-object, eleven-arrow example is an \(h\)-cofibration but not discretely flat. The literal one-point-complement cofibration recognition claims at ms.111, including tests after every complementary change, are false already for a point included in a two-parallel-arrow category. The narrower couniversal one-point question is separately characterized and linked to the unresolved presheaf question.

Strict and total aspherical **functors** compose for every fundamental localizer. Total dwyérienne **sieves** compose for \(W_\infty\) and nonzero \(W_R\), and strict homological sieves compose. Both sieve composition assertions fail for \(W_0,W_1\), with six-object examples. Fixed-localizer total sieve composition has an exact cosieve-restriction criterion. Higher-truncation finite-object cases are positive; unrestricted cases are not inferred from them.

C048 is completely settled for every fundamental localizer: all sieves work if \(S^2\) is aspherical, and only isomorphisms can belong to a class with the required stability otherwise. The positive branch uses Cisinski (2006), Proposition 9.2.17, printed pp.369–370, and an explicit groupoid inverse for the span-to-pushout comparison. There is no accessibility assumption. The negative branch proves failure of the \(h\)-cofibration property itself, not merely failure of a right adjoint.

C005 is false for the outgoing fork with origin its initial vertex. The actual fixed-origin path category is contractible, its endpoint functor is final, and its composite to the sphere category is final. The proof treats all finite path lengths and the actual interval-morphism convention.

## 4. Transcription and companion corrections

| Location | Correction |
|---|---|
| XII ms.88 | Use \(U'/H'\), the correctly based category of elements. |
| XII ms.89 | The assignment is \(F\mapsto V/F\), not \(F/V\). |
| XII ms.92 | The discrete-fibration clause for \(F'\) on \(V'\) uses \(V'/F'\). |
| XII ms.93 | Use the correctly typed \(\underline{\pi}_0(V/V')\), not its reversal. |
| XII ms.96 | The group pushout uses the subgroup generated by \(\alpha^2\); this is already an editorial correction. |
| XII ms.110,113 | Cobase change uses \(U'\amalg_U X\), with the original \(X\). |
| XII ms.112 | The asserted aspherical restriction is \(i'_0\); the crossing weight is \(i'^*(t')\). |
| Companion B035 | The finite split-idempotent counterexample supersedes the open status. |
| Companion filteredness | The finite/weak-terminal extension holds, but the general conjecture is false. |
| Companion C035/C037/C038 | Absence of an adjoint alone did not answer C035. The couniversal counterexample does; the separate cofibration-recognition clauses are false. |
| Companion interval block | The obstruction strengthens to non-cofibrancy and the complete maximal-class dichotomy. |
| Companion C005 | The endpoint-finality counterexample settles the stated assertion negatively. |
| Historical exactness claim | The 1981 correction prevents use of the false fixed-point criterion or its later repetition as an open-problem authority. |

The truncated homological Theorem A was also tightened in review to require nonempty comma categories explicitly. Vanishing reduced homology in nonnegative degrees alone would admit the empty category. All applications already satisfied nonemptiness, so no later conclusion changed.

## 5. Computations

All finite counterexamples have explicit objects, arrows, units, and compositions. Programs check typing, associativity, functor laws, naturality, adjunctions where used, comma connectedness, and actual pushout relations. Integer homology uses exact matrices and Smith normal form.

| Program family | Principal outputs |
|---|---|
| ag_finite_examples | Fork: 3 objects/5 arrows. Sphere: 4/10, simplex counts \((4,6,4)\), \(H_2=\mathbb Z\). Acyclic noncontractible category: 35/159, counts \((35,124,90)\), plus a finite permutation certificate for nontrivial fundamental group. Cones: 36/195 and 37/231. |
| root_monoid_checks | Right-zero monoid, action category, sphere collage; normalized homology through degree 4; rectangular-band checks through three rows/columns. |
| root_presheaf_checks | Three-object/six-arrow element category; final quotient, sphere functor, composite, all comma categories, and failure of common successors. |
| cd_affine_simplex | Exploratory exact nullspace calculations, retained as bounded evidence. |
| cd_affine_polynomials | Source ordinals \(0,1,2,3\); targets \(0,2,6,14\); \(1,3,29,932\) nonzero terms. Augmentation 1 and every coface identity checked. |
| cd_finite_checks | Discrete two-object exactness, \(C_2\) multiplication/differentials, rational/integral separation, and 351 bounded cospan-stratum checks. |
| f_check | Three- and four-object cofibration examples. Endpoint \(n=2\) pushout: 8 objects/30 arrows, simplex counts \((8,22,30,20,4)\), homology ranks \((1,0,0,1,0)\). The \(n=3\) example has 10/40 and the same reduced \(H_3\). |
| f_low_truncation | Complete six-object target tables, with 15/21 arrows, and all adjunction, transformation, and slice checks. |

The paper's proofs, not bounded computations, establish all-degree and infinite claims. The infinite fence uses an actual uniform displacement bound, with no false compactness or ind-colimit inference. Source retrieval/OCR and artifact-production programs are retained separately with outputs.

## 6. Exact unresolved work

The connected integral implication from totality to exact abelian colimits remains unresolved. Its general nonzero-ring analogue is also retained. For the integral case, all weakly terminal and finite-object categories are settled; the first unhandled cardinality is countable without a weakly terminal object. This is not a claim that every hypothetical counterexample reduces to that size.

Finite-relation quotient actions do not yield a single simultaneous affine equalizer. Free-abelian comonad resolutions do not commute underlying-set functors with colimits; Dold–Kan shifting does not repair that step. Product arguments fail already for injective ordinals. The fixed-point property is insufficient by the verified 1981 example.

The common strict-\(W_\infty\) sieve/presheaf assertion remains unresolved. A counterexample would be a total integral-homology presheaf with acyclic element category and nontrivial perfect fundamental group. Restricted actions do not supply every covering of that element category. The paper proves the equivalence with strict sieve composition, discrete flatness, nonempty cosieve restriction, and the one-point couniversal recognition question. A composition failure can be confined to a classical Dwyer first factor and a one-object extension. General finite bases/presheaves are not settled; no minimum or existence claim is made.

For fixed general localizers, the remaining total-sieve composition issue is the exact cosieve-stability condition stated in the paper. The \(W_0,W_1\) failures and the weak/homological positive cases are established; the branch making \(S^2\) aspherical is analyzed separately. Among higher truncations, \(W_2\) with infinite categories is the first unhandled case. All strict and total functor composition questions and all C048 cases are settled.

## 7. Review and artifact validation

Independent mathematical review checked the action classification, covering argument, affine construction, signed measures, exactness criterion, presheaf example, restricted actions, discrete flatness, paths, interval obstruction, fixed points, and final composition reductions. The appended audit records specify sources and exact transfer checks. This is not external refereeing or a formal proof-assistant certificate.

LuaLaTeX, BibTeX, and latexmk produce the PDF. Missing font packages/maps in the environment were supplied in a private workspace tree without changing global configuration. The source builds normally on complete TeX Live. Final checks cover citations, references, labels, ledger coverage, permitted statuses, page boundaries, and ZIP integrity. Every page is rendered for visual review. Exact counts and results are in the saved build, QA, finalization, and package outputs.

## 8. Detailed source, search, and independent-review records

The following appendices are the contemporaneous subtask records. Later additions in them supersede earlier working-scope remarks; the numbered paper, root CSV, and exact unresolved list above determine the final status. They preserve the actual searches, source locations, mathematical checks, and unsuccessful approaches rather than replacing them with a generic bibliography.

---

## Appendix 1: AG_report.md

### Parts A (audit) and G: verification report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

#### Sources actually read

1. Attached `DER_XIIb-a_text.tex`, XII ms. 75–103: exact W(7)/W(7 bis), Propositions 7–10, all retraction corrections, the path question C005. The primary electronic PDF `Der-ChXIIb-012.pdf` was opened independently and the Proposition 7 passage checked.
2. Attached `DER_XIIb-b_text.tex`, XII ms. 149–150: the deferred one-point corollary and its proof strategy.
3. Attached `DER_VII-a_text.tex`, VII ms. 25–31: actual Grothendieck-construction variance of path morphisms and the corrections restricting type morphisms to increasing endpoint-preserving interval functors.
4. Attached `DER_VII-b_text.tex`, VII §§5–7, especially ms. 59–78: composition, component groupoid, cancellation moves. The primary electronic PDF `Der-ChVII-456.pdf` was opened; its component/localization passage was located. Sections 8–10 were inspected to distinguish component claims from stronger homotopy claims; the proof of C005 uses no unverified perfectness or homotopy-fibre theorem.
5. Companion XIIb-a blocks on ms. 78, 85, 93–103, read as drafts. The explicit fork final image and homology-localizer gluing audit were independently reconstructed. The companion's C005 open status is superseded by the explicit final-image obstruction below.
6. Hatcher's primary full PDF `Algebraic Topology`: Theorem 1.20, Theorem 2.35, Example 2.38 (p. 142), and Corollary 4.33 (p. 367) opened/located. The finite categorical example replaces the companion's existential finite triangulation by explicit face operators and full machine-readable data.
7. The supplied primary proceedings `bass-seattle.pdf` was converted to text and Quillen's §1 Theorem A read, including its expressly stated dual overcategory version.

#### Literature searches

Web searches actually run included `Grothendieck dérivateurs "chemins" "totalement"`, `Grothendieck "Ch(Y" asphérique`, `"Grothendieck" "totalement asphérique" "chemins"`, and `"path categories" "Grothendieck" final functor`. Search coverage was checked with both available engines. The principal relevant primary hits were Grothendieck's manuscript and Maltsiniotis's discussion of the different Pursuing Stacks notion. Most other path-category hits concerned Brown categories of fibrant objects or the left adjoint to the nerve, and were not used. No independent published settlement of the exact XII C005 question was located in these searches. This is a report of the searches, not a priority claim or an assertion that no such publication exists.

#### Mathematical results

C005 is **false**. Let Y be the outgoing fork z→a,z→b and choose y0=z. The fixed-origin path category P(Y,z) has an explicit two-step natural-transformation contraction, hence contractible classifying space. Its endpoint functor q:P→Y is ordinary final. For an object (c ending at w, α:y→w) in y\P, append the retrograde edge w←y. Collapsing that last interval gives a morphism from the resulting fixed-end path to (c,α). Components of the fixed-end path category equal arrows of the groupoid completion, proved by elementary identity/composition/cancellation zigzags in the exact VII definition. The fork has trivial fundamental groupoid, so the comma categories are connected.

There is an explicit final inclusion Y→C with four-object target C and BC≅S². Composing P→Y→C gives an ordinary final outgoing map that violates the defining test of total W∞-asphericity. The same witness works for W_R (R nonzero) and W_n (n≥2). P also fails the common-successor part of filteredness: paths ending at a and b cannot have a common successor, since endpoint evaluation would give a common successor of a,b in Y. None of these arguments assumes total asphericity equals filteredness.

Proposition 7 and its one-point corollary are valid with the stated full W(7 bis). A direct categorical double mapping-cylinder construction proves the missing attachment comparison and then the axiom applies. The construction also proves the one-point collage homotopy-pushout formula with specified comparison maps. Its Quillen-A proof explicitly contracts every overcategory, including the nontrivial overcategory at the attached point.

The one-point converse is false for W∞ without the extra axiom. An explicit finite category A has 35 objects and 159 arrows and realizes a triangulation of Hatcher's acyclic presentation complex. Its fundamental group has a nontrivial A5 representation. Adjoining two distinct final cone points gives a 37-object, 231-arrow category X and a 36-object full sieve U with BU and BX contractible, but U/t≅A is not weakly contractible. This also disproves full W(7 bis) and W(7) for W∞. It is consistent with the companion's audit; the new contribution to the deliverable is complete finite data and independent checks.

Propositions 8 and 9(a) are valid for every fundamental localizer. Proposition 9(b), its proposed retraction repair, and its fork corollary are false. The outgoing fork and its two terminal-object branches prove failure for W∞ and W_R. The normalized-chain exact sequence of a sieve cover proves full W(7) for W_R, so the counterexample respects the conditional axiom in the original statement. The failed proof step is the claim that a categorical retraction of a sieve defines a retraction of its subterminal presheaf and hence survives left Kan extension; it does not.

#### Source corrections and variance checks

- VII ms. 25–31: use increasing, endpoint-preserving maps of intervals, not the initial uncorrected collection of all functors.
- VII ms. 63: the second backtracking cancellation has a natural transformation **from** the backtracking path b←a→b **to** the constant path at b. The attached transcription already carries an editorial correction; our argument uses that corrected direction.
- XII ms. 85 footnote 65 calls the deferred result Corollary 4 of Proposition 15. In the supplied continuation, the result at ms. 149–150 belongs to the corollaries of Theorem 4; Proposition 15 begins later. The paper cites the manuscript location and exact statement rather than propagating that cross-reference.
- Ordinary finality uses y\P, not P/y. The appending construction gives the arrow (c_alpha,id_y)→(c,alpha) in y\P. Every source, target, type map and endpoint component is specified.
- The homotopy equivalence M_U→U in the mapping-cylinder argument is supplied by an adjunction, not an equivalence of categories. The map M→X is a specified weak equivalence proved by Quillen A.
- The 35-object example is a category of simplices with distinct incidence arrows for repeated faces; it is not the poset of simplex names. Collapsing repeated incidence arrows would change the homotopy type.

#### Computations and reproducibility

`code/ag_finite_examples.py` is deterministic and requires Python 3 and SymPy. It enumerates the fork, its S² final image, the 35-object category A, and its one- and two-cone extensions. It checks identity and associativity axioms for every composable triple, the relevant sieve conditions, connectedness of every comma category for the fork inclusion, the full normalized nerve chain complexes, d²=0, and exact Smith normal forms over Z. It also evaluates the A5 relator words and the determinant of the original cellular differential.

Output is saved in `code/ag_finite_examples.output.json`. Complete finite objects, arrows and composition tables, together with the defining face operators, are saved in `code/ag_category_data.json`.

The normalized simplex counts are (3,2) for the fork, (4,6,4) for C, (35,124,90) for A, (36,159,214,90) for its cone, and (37,194,338,180) for its two-cone suspension. The result for C is H0=Z,H1=0,H2=Z; A and both cone constructions have H0=Z and zero higher integral homology. The geometric proof, not homology computation alone, establishes nontrivial π1 for A and contractibility for its suspension.

The first program run completed all mathematical assertions but encountered a JSON serializer TypeError on SymPy's Integer objects. Explicit conversion to Python integers fixed the output serialization; the subsequent complete run passed. No mathematical assertion was relaxed.

#### Remaining questions in this subtask

No question assigned to Part G remains open: its general implication is refuted by the displayed finite Y. The path category is infinite, and the proof applies to all finite-length paths; no inference from bounded enumeration is used. Propositions 7–9 have all been classified with their original axiom qualifications. This subtask makes no claim to settle the general presheaf converse in Part E or the general category characterization in Parts C–D.


#### Independent cross-review of Parts A–E

At the parent's request, the root drafts A.tex and B.tex were read in full. The literal simplicial mapping-cone identification in B:collage is valid: mixed nondegenerate simplices start with exactly one new source, repeated source vertices are precisely the cone-factor degeneracies, and the face deleting the first old vertex acts on the chosen element by the covariant functor. The transfinite iteration is valid because each inclusion is full and a comma category into a fixed earlier stage stabilizes once its source object has appeared; the draft's second proof gives this cleanly. The Karoubi totality converse is valid: multiplying every arrow in a connecting comma zigzag by the target idempotent preserves each triangle and fixes its endpoints. The natural contraction of the Karoubi comma category has component v at an object represented by v, with naturality equation wv=v'.

Part C was then read in full. The integral acyclicity-to-contractibility argument correctly uses all connected coset coverings, including one for every cyclic subgroup of the fundamental group. Its inheritance argument is an actual isomorphism of categories of elements of the disjoint-union functor. The signed-measure monoid lemma remains valid for negative coefficients: each nonzero support point has a nonzero-support predecessor; finiteness then forces every support point onto a periodic orbit. Left multiples of a point of period r inherit period dividing r, and the augmentation-one condition permits prime-divisor descent to period one. The weak-terminal reduction is correctly typed. The affine-polynomial proof was checked at the coordinate-hyperplane compatibility, inclusion–exclusion interpolation, degree recursion, gap encoding, and passage from equalized cofaces to all parallel injections.

Part D's affine exact-colimit criterion was independently checked in both directions over an arbitrary nonzero commutative ring. Exactness gives common successors by preserving intersections of cosieve-supported constant submodules. The finite direct-sum presentation of a zero colimit element gives the affine equalizer t=d_q−Σr(d_t v−d_s)c; its augmentation is one and its multiplication by δ is zero. The group and truncated-localizer arguments also check. One proof-completeness suggestion was sent: replace the uncited nerve/Grothendieck-construction comparison in D:homology-localizer by the explicit bisimplicial set (a_0→…→a_q, f(a_q)→c_0→…→c_p). Its two spectral sequences directly compute H(A) and the slice-homology comparison.

The parent's finite B035 counterexample was independently verified immediately upon receipt. For U the idempotent monoid {1,e}, let Q={e} be the split subpresheaf of the representable R=U(-,*), and put H=R⊔_Q R={i,h_1,h_2}. For every p:U→C, with c=p(*) and d=p(e), p!Q is the subpresheaf {α:b→c | dα=α} of C(-,c). Its category of elements is filtered: every object (b,α) maps to (c,d) by α, and β equalizes any parallel pair ending at (b',β). The two copies of C/c in C/p!H are full sieves with this contractible intersection. Their nerve union is a homotopy pushout of contractible spaces. Thus H is totally W∞-aspherical. Its element category has endomorphisms {1,e} at i and arrows i→h_1,i→h_2, with no common successor of h_1,h_2. The full quotient to the outgoing fork is final, and composing with the four-object sphere target proves failure of totality. This verifies the counterexample for W∞ and every nonzero W_R, independently of the proposed filteredness characterization.

#### Independent cross-review of Parts E and F

The complete current Part E was read, including the restricted-action criterion. Its necessity uses the actual covariant collage on U, so that the actions tested on E=U/H are precisely those factoring through E→U. The new-source values are the components of the resulting two-sided element category. The attachment formula and its integral homology sequence give exactly componentwise acyclicity, not unproved contractibility. For sufficiency, the comma category at (u',c) in U'/p!H is the component labelled c of the element category of u↦U'(u',p(u)) pulled back to E. Homological Theorem A supplies homology, and ordinary finality supplies the fundamental-group quotient. Together these prove the W∞ criterion. The subterminal converse, filtered-presentation criterion, and typed ind-right-adjoint statement also check. A harmless missing backslash in a displayed `quad` was reported to the parent.

Part F was read in full and checked at the level of functors, weights, and natural transformations. The forward gluing proof uses only objectwise invariance for a span, not the invalid reverse W(7 bis) property. For a cover by two cosieves, the comma over an object outside the intersection lies in the unique relevant slice and has a terminal object; over the intersection the three slice-terminal objects are compatible and contract the span. The couniversality criterion uses a Thomason factorization and retracts of classical Dwyer maps, so its reverse direction has the hypotheses needed beyond mere two-out-of-three.

The closure arguments for total categories, total functors, and total sieves are correctly typed. The Grothendieck-construction comparison E_z→X/z has the displayed left-adjoint section and is final. For a composite of sieves, the intermediate nonempty locus is a cosieve, as required. The strict-functor composition proof takes slices in the collage of the extended weights; an arrow to (y,h) retains its actual crossing-arrow label q even if two coend expressions [q,h] represent the same element. Thus its slice really is X'/Q_y. The later homological cosieve-restriction lemma also checks: the first extension produces an initial cone on C/K, the two-valued covariant action produces its double cone, and the second source attachment has homotopy type Σ²B(C/K). Reduced suspension homology gives the stated nonempty connected R-acyclic result for every nonzero R. It does not assert the unproved W∞ version.

The discrete-flatness weight test is exact in both directions. Its necessity uses simplicial collages with unchanged objects; its sufficiency verifies all mapping simplicial sets and essential surjectivity. The total-category sufficient condition uses the bisimplicial replacement degree by degree. The finite B035 weight is discretely flat because its coend is V⊔_{im(d)}V and im(d)→V is a split simplicial monomorphism. The independent h-cofibration-but-not-discretely-flat example gives CK⊔_K CK→* for K a circle. Its relative two-step categorical deformation survives arbitrary pushout because product with [1] preserves colimits. The C035 example's natural transformations were checked on both parallel arrows and on all crossing arrows after an arbitrary base change.

The source `background/papers/2205.02353/Dwyer-pushout-scat.tex` was inspected at the proof of Theorem 1.5. Its generalized statement explicitly applies to discretely flat inclusions, with the comparison from the ordinary simplicial pushout of nerves. Thus the invocation in F:DFh is supported by the supplied primary text; it is not an extrapolation from classical Dwyer inclusions.

For the endpoint product, all weights were independently reconstructed. The u_1 weight is the subterminal presheaf supported on the sphere category C, because the four-vertex source S maps finally to the outgoing fork and that fork maps finally to C. Every later weight is represented by a, and the only transition into u_1 is the canonical representable-to-subterminal map. The retraction sending u_k to a for k≥2 has a natural transformation to the identity with components represented by id_a. This gives the stated S³ pushout for target C with an added terminal point. The sharper S² argument also checks: without that added terminal point, the pushout contracts, while C has type S². Since the original inclusion α is already a weak equivalence, the couniversality criterion detects failure for every W not inverting S², including W₂.

The maximal-class argument has no hidden retract-closure assumption on the proposed class K. A crossing arrow exhibits the initial-vertex inclusion e→[1] as a retract in the arrow category; only the already proved retract closure of W-cofibrations is used after applying the fixed endpoint product. If there is no crossing arrow, a proper full sieve is a coproduct-summand inclusion; applying the endpoint product once creates a crossing arrow. Thus only isomorphisms can occur for the stated localizers. Finally, the W₁ exception correctly uses groupoid completion preserving pushouts and retaining object sets, together with left properness of the folk model structure under object-injective maps. Pushouts of groupoids in categories remain groupoids. This proves the positive C048 answer for W₁, alongside the simpler π₀ argument for W₀.

No substantive mathematical error was found in these current Part E/F arguments. `research/AG_cross_review.csv` records the statement-by-statement audit outcomes; “verified” there means independently checked against the specified proof, not a claim of publication or priority.

#### Final additions and coverage audit

The added infinite-fence example B:fence is correct. Its nerve is the one-dimensional ray, its two maximal vertices violate common successors, and each component of a natural transformation can move an object by at most one edge. A finite zigzag would therefore impose a uniform displacement bound, incompatible with a constant endofunctor. This uses actual transformations on the entire infinite category.

The added B:homotopical-colimits is correct. In bidegree (p,q), the displayed simplicial replacement is the p-nerve of the category of elements of the q-th set-valued diagram. Its augmentation is the canonical component map. The action criterion applies to each row and the bisimplicial diagonal lemma then supplies the specified map to ordinary colimit. The converse uses discrete diagrams and retains the essential nonempty-connected hypothesis on A.

The finite idempotent-base classification E:finite-idempotent-classification is correct. Components of the element category are precisely fibers over the fixed points of the idempotent. With one fixed point, any finite presheaf is either Q itself or a finite union of representables with common split subpresheaf Q. Its arbitrary Kan images give the same contractible union argument. An element set of size one gives the filtered idempotent monoid, size two gives a terminal object, and size at least three gives distinct maximal objects without a common successor. Thus its asserted minimality is only on this specified base, exactly as stated.

The Part H table was compared with all requested rows and the proved section statements. No mathematical status error was found in the then-current table. The integral exactness converse was deliberately left pending while the other agent checked an additional primary source. Two coverage amendments were sent to the parent: record the unresolved strict-dwyérienne-to-discretely-flat implication in H, and explicitly mark total immersion composition for a general localizer as unresolved rather than leaving only the proved cases implicit. The F owner was also asked to state and prove the conditional biconditionals of Théorème 3 and the boundary criterion of its corollary; the cover proof takes only a short additional proposition and was supplied with the request.

The following source slips were verified directly in the attached transcription during this final audit. They supplement the earlier corrections above and should be retained in the consolidated report: XII ms. 88 has U/H' in a category of elements that is over U', so it must be U'/H'; XII ms. 89 labels the right vertical category-of-elements functor F↦F/V instead of F↦V/F; XII ms. 92 factorization clause (a) has V/F' for a presheaf F' on V', so the base must be V'; XII ms. 112 says i' is aspherical where only its restriction i'_0 to the generated cosieve is asserted to be so, and the crossing weight must be i'^*(t') rather than either i^*(t') or i'^*(t). The mathematics in the current sections already uses the corrected typed formulas. These are corrections to the supplied source formulas, not reasons to alter the definitions.

#### Final scope after integration

The later integrated proofs supersede the earlier provisional open lists. Strict and total functors compose for every fundamental localizer. The total-functor argument uses the actual isomorphism of the slice of (gf)/z→Y/z at (y,β) with X/y, followed by the proved restriction theorem for total presheaves. The general total-sieve question is equivalent to nonempty cosieve stability of total categories. The lower-copy construction gives finite six-object counterexamples for both W0 and W1; these were proposed during this audit and independently verified and programmed by the F subtask. For higher truncations the finite-category total-sieve cases are positive.

The narrowed one-point couniversal-recognition question is equivalent to the other four remaining presheaf assertions, by the exact one-point criterion. All five directions and the universal-cover attachment argument were audited. The literal ordinary-cofibration recognition statements C037/C038 are false, as detailed in `AG_general_report.md`. Their counters do not refute the narrower couniversal question.

C048 is completely settled for every fundamental localizer by `F_followup.tex`; its two cases are all sieves versus only isomorphisms, according to whether S2 is aspherical. The primary Cisinski proposition and the explicit groupoid-connector inverse were independently checked. The new `D_general.tex` then completes the entire S2-aspherical branch for category totality, presheaf totality, and sieve composition. Combining it with the finite split-idempotent counterexample gives the complete all-localizer B035 dichotomy.

The two new necessary conditions in `D_followup.tex` also pass audit. Preservation of set-diagram monomorphisms and span amalgamation use total action components and their common successors. The fixed-point argument uses the action-category nerves for the monoid of nonnegative integers and then the cyclic group of the least occurring positive period. Their degreewise colimits are exactly the stated classifying-space nerves, so homotopicality of ordinary colimit supplies the contradictions. The 1981 counterexample is used only to invalidate a fixed-point-to-exactness inference, not asserted to be totally aspherical.

One genuine wording defect found in the final edge-case audit was corrected: the truncated clause of C:homology-A must retain nonemptiness of every comma category. Vanishing reduced homology in nonnegative degrees alone would admit the empty category. All applications already used final functors, so the correction changes no derived result. Combined status headings were normalized to one of the four required statuses. The final core manuscript rows are all represented in H; the unresolved exactness and presheaf implications retain explicit quantifiers and restricted forms of possible counterexamples.

---

## Appendix 2: CD_report.md

### Parts C and D: research record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

#### Sources inspected

- Attached PROMPT(2).md; relevant FABLE overview and companion II-a discussion.
- John R. Isbell, *A note on exact colimits* (1968), full four-page primary article opened at Cambridge, DOI 10.4153/CMB-1968-068-7. Section 1 gives a finite-family linear condition; Section 2 proves the monoid theorem. Its argument was not blindly substituted for the total-asphericity condition.
- Isbell, *Exact colimits, I* (1974): Annals and JSTOR bibliographic pages opened; full body inaccessible. The title, volume, issue, pages, DOI verified, but no theorem number invented and no unavailable proof used.
- A. A. Husainov, *Homological dimension theory of small categories* (2002), author's uploaded full text opened. Section 2.3, Theorem 2.5 states the affine-category criterion and the following paragraph identifies Delta_face as Isbell's nonfiltered exact-colimit example. This supplied a literature lead; the relevant claims are proved independently in the paper.
- Husainov, *On the homology of small categories and asynchronous transition systems* (2004), primary article opened. Section 2 notes the counterexample to Oberst and repeats an unresolved fixed-point/exactness question. The later source audit found that the relevant fixed-point equivalence had already been refuted in 1981; that historical passage is not used as an open-problem source. See CD_followup.md.
- Open Maths, *Derived colimits over a small category* (20 October 2026), sections 4.1–4.8. Page explicitly credits Claude Opus 5.5 and dedicates content to the public domain (CC0). Treated as an untrusted AI mathematical draft. The gap-polynomial interpolation construction was read, independently proved, and checked by exact symbolic arithmetic. No authority or priority claim relies on this page.
- Isbell–Mitchell 1973 and 1976 AMS bodies: attempted direct retrieval, HTTP 403. No invented theorem number. The affine theorem is reproved.

#### Queries

Searched combinations of “Isbell Mitchell exact colimits fixed points”, “Oberst conjecture”, “aff C filtered”, “Delta face exact colimits”, “categories of elements contractible colimit”, and exact article titles. Routine engine coverage was checked with the stronger engine for the principal original-paper searches. No claim of novelty is made.

#### Proof decisions

1. Total W_Z implies all connected categories of elements of covariant Set-valued diagrams are acyclic, using the collage construction. This property is inherited by categories of elements.
2. Covariant coset diagrams model every connected covering. Applying acyclicity to a covering with a cyclic fundamental group proves that every such element-category component is simply connected, hence contractible. Thus total W_Z equals total W_infinity.
3. Exact Ab-colimits imply total W_infinity in the nonempty connected case. The missing connectedness invalidates the literal W_Z assertion in Lead 4, even before discussing its difficult converse.
4. Delta_inj has exact Ab-colimits and is not filtered. Its exactness is proved through explicit affine cones, so the main counterexample does not rest on an inaccessible article or on an unchecked AI source.
5. Lead 2's H_1 formula is correct without an asphericity assumption on the base. Its proof uses two short exact sequences of functors and projectivity of linearized covariant representables.
6. A monoid affine-equalizer condition yields genuine equalizers through invariant signed measures and reduction of finite cycle periods. This also proves filteredness for total categories with a weakly terminal object, including every finite-object category.

#### Programs and outputs

- code/cd_affine_simplex.py and .out: exploratory exact nullspace computations for affine cones, which found target cardinalities 3 and 7 and suggested the subsequent polynomial construction. These bounded searches are evidence only, not the general proof.
- code/cd_affine_polynomials.py and .out: exact integral polynomial construction, validation of augmentation one and equality of all codimension-one faces, with actual injection dictionaries for dimensions through 3. The symbolic induction is the proof for every dimension.

#### Limits

The connected converse from total W_infinity (equivalently total W_Z) to exactness of colim on Ab is not established merely by the action criterion; the proof must not identify free-on-a-set diagrams with projective diagrams. It is retained as an exact unresolved implication in this report, not asserted to be an open problem in the literature without a current verified source.

#### Additional verified background

- Hatcher, *Algebraic Topology*, author's PDF opened; Theorem 1.38 (covering classification), Theorem 2A.1 (first homology as abelianization), and Theorem 4.32 (Hurewicz) verified.
- Lurie, *Higher Topos Theory*, author's PDF opened; Proposition 5.5.6.18 verified for the n-truncation adjunction.
- `cd_finite_checks.py` checks the discrete two-object category, the C2 multiplication law and displayed periodic differentials, and the three comparison strata of Delta_inj cospans on a bounded family (351 comparisons). Full mathematical proofs establish the unbounded claims.
- `cd_make_results.py` generates the C/D statement ledger; its output is attached.

#### Further corrections and scope

- W0-total categories are exactly nonempty connected categories; W1-total categories are exactly those with simply connected classifying spaces. For n>=2, the paper gives an exact action-category criterion and proves filteredness in all weakly terminal and finite-object cases.
- For a finite group G and a nonzero commutative unital ring R, total W_R is equivalent to invertibility of |G| in R. Thus rational and integral totality differ already for C2.
- The zero-ring case is handled separately; every category is then total.
- Delta_inj is not sifted: the cospan category for two singleton ordinals has exactly three components (<,=,>). This directly blocks a proposed Dold–Kan shortcut to the missing converse.
- The manuscript's integral-homology totality and weak-homotopy totality coincide, but no claim is made that an arbitrary homology equivalence preserves totality.
- The verified 1981 primary-source correction and two further necessary conditions are recorded in CD_followup.md and sections/D_followup.tex. In particular, totality implies the representation fixed-point property; that property alone does not imply exact additive colimits. This does not settle the corrected connected necessity.

---

## Appendix 3: CD_followup.md

### Exactness follow-up and source correction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.

#### Verified additions

`sections/D_followup.tex` contains complete proofs of:

1. Total weak-homotopy asphericity implies preservation of monomorphisms by set-valued colimits, and the commuting-completion property for spans.
2. Total weak-homotopy asphericity implies the fixed-point property for every nonempty connected covariant set-valued representation. The proof first rules out aperiodic endomorphisms by the classifying space of the monoid N, then rules out least periods r>1 by BC_r. It uses the already independently audited homotopical ordinary-colimit characterization.

These do not settle the corrected necessity from total asphericity to exact abelian colimits.

#### Primary-source correction

Adámek, Koubek, and Reiterman (1981), *Embeddings into categories with fixed points in representations*, Czechoslovak Mathematical Journal 31(106), 368–389, DOI 10.21136/CMJ.1981.101753, was downloaded from DML-CZ and its complete scan OCRed. The source cache is outside the deliverable directory.

Verified locations: A.4 (p.370) corrects the earlier FPP/exactness identification; Construction C.1 (p.384) and Theorem C.2 (pp.385–389) construct a quasifiltered category whose affine category is not filtered. Consequently Adámek–Reiterman (1976), II.3 (p.100), and the later repetition of an unresolved FPP/exactness question in Husainov cannot establish a present theorem or open-problem claim. The 1976 paper's I.2(a) on monomorphism preservation is separate and consistent with the proved result above.

No total-asphericity claim is made for the 1981 example.

#### Routes checked and exact remaining obstacles

- An action quotient identifying finitely many parallel arrows gives an image subfunctor generated by their differences. Its first-homology vanishing follows already from the pairwise tests and right exactness; this does not produce a single common affine equalizer.
- The free-abelian comonad resolution consists of free-on-set diagrams and is useful for computing derived colimits, but set-valued colimits of its underlying simplicial sets differ from the underlying sets of its abelian colimits.
- Shifting such a resolution using Dold–Kan does not justify interchanging the underlying-set functor with colimit.
- Products cannot repair that step. For Delta_inj, the abelian-valued diagram F([n])=Z{0,...,n} already has distinct tuple strata (e_i,e_i) and (e_i,e_j), i<j, in the set colimit of the square, although their separate coordinates have the same colimit classes.
- All set-linearized diagrams being colimit-acyclic does not, without another argument, imply acyclicity of every module-valued diagram.

The manuscript's precise unresolved connected implication and its general-ring analogue therefore remain unchanged.

#### Reproducibility

`code/cd_followup_sources.py` and `.out` record attempted primary-source retrievals.
`code/cd_ocr_source.py` and `.out` record OCR of the available 1981 scan.
The copyrighted source cache is excluded from the deliverable archive.

---

## Appendix 4: F_report.md

### Part F working report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

#### Sources read

- Grothendieck XII ms. 107--115, attached transcription, including every definition and the exact interval orientation.
- Companion XIIb-a blocks at ms. 100, 107--114; the four-object sphere category and the interval slice calculation were checked mathematically rather than accepted on authority.
- Hackney--Ozornova--Riehl--Rovelli, attached source 2205.02353: Definition 3.4, Example 3.5, Proposition 3.3, Theorems 1.5 and 1.6; surrounding proofs read.
- Batanin--Berger, attached source 1305.0086: Definition 1.1, Lemma 1.3, Proposition 1.6, Corollary 1.9, Lemma 1.10.
- Cisinski (1999), full attached PDF, extracted with `pdftotext -layout` to research/Cisinski1999.txt; definition and correction checked.
- Pavlov, arXiv:2208.02954v4, full web PDF, especially Propositions 2.9, 3.2, 4.1--4.3. This supplies an independently verified related obstruction to cartesian model structures, not the exact endpoint-product result.

#### Searches

Web searches included exact title searches for the HORR and Batanin--Berger papers; `"h-cofibrations" "pushout-product" Cat`; `"discretely flat" "filtered"`; `"Grothendieck" "totalement asphérique" dwyérienne`; and `"Thomason" "pushout product" interval`. Searches located Pavlov's related paper through a secondary pointer, after which only the primary paper was used. No claim of novelty is made for the constructions below.

#### Findings

1. C035 is false even for a 3-object, 7-arrow sieve. The inclusion of a into a category a ⇉ t → s with equal composites is couniversally a categorical homotopy equivalence, but its crossing category at t consists of two discrete objects. This example is also discretely flat.
2. A distinct 4-object example gives a couniversal W-infinity-equivalence sieve that is not discretely flat. Its enriched test uses the inclusion S1→cone(S1), compared with S1→point. The resulting crossing mapping spaces are S2 and point.
3. The interval product in XII ms. 114 fails the h-cofibration property itself, for every n≥2, not only the existence of a right adjoint. An explicit ordinary pushout along a weak equivalence has homotopy type S3.
4. This yields a sharp impossibility: a class of W-infinity-cofibration sieves closed under that endpoint pushout-product contains only isomorphisms. A second pushout, with source of type S2 and contractible target, strengthens the condition to every fundamental localizer in which S2 is not aspherical. This includes all nonzero fixed-coefficient homology localizers and all W_n for n>=2. Closure under arbitrary cobase change is not needed for the impossibility.
5. The literal maximal class meeting the requested two stability conditions in these cases is therefore the isomorphisms. A useful nontrivial replacement must alter the operation, for example by using a homotopy pushout/cofibrant replacement rather than the specified ordinary product inclusion.
6. For W0 and W1, all sieves satisfy C048. The W1 argument uses the fact that groupoid completion preserves pushouts and keeps object injectivity, together with left properness of the folk model structure (explicitly recalled in the verified proof of HORR Theorem 1.6). The supplement F_followup.tex completes the result for every fundamental localizer: all sieves are the maximal class when S2 is W-aspherical, and only isomorphisms are possible otherwise. Its additional source is Cisinski (2006), Proposition 9.2.17, with no accessibility hypothesis; the supplement records the full proof and source verification.
7. Totally dwyérienne sieves compose for W-infinity and every nonzero homology localizer W_R, using the action-category characterization and the actual transition functors in the Grothendieck construction. The later argument in item 14 strengthens total functor composition to every fundamental localizer.
8. Strictly W-aspherical functors compose for every fundamental localizer. The proof uses a collage of the Kan-extended representable restrictions, then Theorem A on its category of elements. No identification of total presheaves with total element categories is assumed.
9. W_R-dwyérienne sieves compose for every nonzero homology localizer W_R. The needed nonempty cosieve-restriction lemma is proved by constructing a category of elements of homotopy type the double suspension of the restricted element category.
10. The finite split-idempotent presheaf from Part E gives a strict-but-not-total dwyérienne sieve which is also discretely flat. The weighted coend is a pushout of two spaces over a simplicial retract.
11. The exact discrete-flatness criterion is now proved: for E=U/H, the weighted coend H tensor_U - preserves objectwise weak equivalences precisely when every component of El_E(L pi), for every covariant L:U→Set, is contractible. Necessity uses the explicit simplicial bar resolution of L, and sufficiency uses the two-sided bisimplicial bar construction. Among such weights, total W-infinity-asphericity is exactly nonempty connectedness of E.
12. The two unresolved strict-class questions are proved equivalent, and equivalent to a third precise statement: every totally integral-homology-aspherical presheaf is totally W-infinity-aspherical. They are also equivalent to preservation of total W-infinity-asphericity by nonempty cosieve restrictions, and to recognition of a couniversal W-infinity-equivalence with a one-object, identity-only complement as W-infinity-dwyérienne. A failure of composition can already be realized with a classical Dwyer first factor and a one-object extension second factor. This is a five-way reduction theorem, not a solution of the equivalent question.
13. The exact conditional versions of Théorème 3(a,b) and Corollaire 2 are stated and proved: under full W(7 bis), i in W iff its cobase change is in W iff the boundary inclusion dotT→T is in W iff i is couniversal; under full W(7), p in W iff q in W. The couniversality equivalence itself does not need these extra gluing axioms.
14. Totally W-aspherical functors compose for every fundamental localizer. For total f and g, the induced f_z:(gf)/z→Y/z has slices canonically X/y, hence is total and therefore strict. Strict pullback preserves the total terminal presheaf of Y/z, proving totality of (gf)/z. This also gives Grothendieck-construction closure for total bases and total fibres for every fundamental localizer.
15. For a fixed fundamental localizer W, total dwyérienne sieve composition is equivalent to closure of total W-aspherical categories under nonempty full cosieves. Necessity uses the lower-copy construction and a one-point terminal extension; sufficiency uses the general Grothendieck-construction result. For W_n with n≥2, total sieve composition holds between finite categories, because the finite boundary categories are filtered by Part D.
16. Both strict and total dwyérienne sieve composition fail for W0 and W1. There are explicit six-object target counterexamples with a classical Dwyer first factor and a total second factor. The examples have 15 and 21 arrows, respectively, and composite boundary respectively a discrete pair and a parallel-arrow circle. Thus universal total-sieve composition for all fundamental localizers is false; it is no longer listed as open.
17. The source's ordinary-cofibration one-point recognition (C037) and complementary-change recognition (C038) are false. The inclusion of one object into the parallel-arrow circle is discretely flat, and every change of its terminal complement remains discretely flat because the source is discrete. Its two-element boundary fails totality for W-infinity, all nonzero W_R, and every W_n. This also refutes the claims under full W(7), by taking nonzero homology coefficients.
18. The narrower one-point couniversal question has an exact criterion: U→U⊔_H{t} is couniversal W-infinity iff H is totally W_Z-aspherical, and is couniversal W_R iff H is totally W_R-aspherical for a nonzero commutative unital ring R. For the first sufficiency, total integral-homology asphericity forces the element-category projection to kill π1, by testing cyclic-subgroup local systems on the base. On universal covers, the cone attachment then adds cones on disjoint copies of an acyclic category, and is a homology equivalence between simply connected CW complexes. The unresolved W-infinity one-point recognition statement is consequently exactly the remaining presheaf question of item 12; its homological analogue is proved.

#### Computations

`code/f_check.py` constructs all finite arrows and compositions explicitly. It checks associativity exhaustively, checks the retraction and natural transformations, computes the actual ordinary interval pushout by coends (union-find on the defining relations), and computes normalized nerve chains with exact integer matrices and Smith normal form. Output is `code/f_check.out`.

The n=2 interval pushout has 8 objects, 30 arrows, nondegenerate simplex counts (8,22,30,20,4), and integral homology ranks (1,0,0,1,0), with every nonzero Smith entry equal to 1. The corresponding n=3 pushout has 10 objects and 40 arrows and the same nonzero reduced homology in degree 3. The proof for all n uses an explicit relative natural deformation retraction; the finite checks are independent corroboration, not an extrapolation from the tested values.

`code/f_low_truncation.py` constructs the two low-truncation composition counterexamples, reusing the finite-category and normalized-homology routines from f_check.py. It checks every composition and associativity equation, both inclusions and their composite as full sieves, the first factor's right adjoint and triangle identities, the deformation of the intermediate category onto an initial cone, and the explicit isomorphism of the composite boundary with the chosen two-object category. Its output `code/f_low_truncation.out` includes complete target arrow and composition tables. The final target counts are (6 objects, 15 arrows, simplex counts (6,9,4)) and (6 objects, 21 arrows, simplex counts (6,15,16,6)); both are contractible by the stated terminal-object proof. The boundary homology ranks are respectively (2) and (1,1), with no torsion. The parallel-arrow category simultaneously verifies the finite category used for C037/C038.

#### Corrections to prior audit

The companion's interval block correctly identifies two incomparable maxima in a slice, but its conclusion can be strengthened: the entire interval inclusion is not an h-cofibration. Its suggestion that a broader class might solve exactly the same stability requirement must be qualified by the impossibility theorem. The companion correctly distinguishes the two different meanings of flatness; the explicit examples above give strict separating cases.

The companion's C037/C038 entries retain the strong gluing framework as a potential justification. The explicit two-object example shows that this does not save the ordinary-cofibration assertions: they fail even for nonzero homology localizers, where full W(7) holds. The one-point couniversal variant must be separated from this false statement; its integral-homology characterization and its precise relation to the remaining presheaf implication are now proved.

#### Final status and precise remaining obstruction

The unresolved assertions are whether every W-infinity-dwyérienne sieve is discretely flat and whether strict W-infinity-dwyérienne sieves compose. The new equivalence theorem shows that these are the same remaining question, equivalent to asking whether a totally W_Z-aspherical presheaf can have an acyclic but non-simply-connected category of elements. Any obstruction must have a nontrivial perfect fundamental group. The covering argument for total categories cannot simply be reused: a covering of a restricted action component need not be another action factoring through U/H→U. The exact discrete-flatness criterion replaces integral acyclicity of these components by their weak contractibility.

Strict and total functor classes compose for every fundamental localizer. Total sieve classes compose for W-infinity/W_R, and strict homological sieve classes compose. Both sieve classes fail composition for W0 and W1. For a fixed localizer, total-sieve composition is characterized exactly by the nonempty-cosieve criterion above; for finite n≥2, the unrestricted total W_n sieve question and the strict W_n sieve question remain unsettled here, while total W_n composition between finite categories is proved. C048 is settled for every fundamental localizer by the supplement's S2 dichotomy. No implication from an unproved total-asphericity/flatness characterization is used in the counterexamples or the interval impossibility.

The final reduced setting is specific rather than a claim about a minimal finite example: one may seek a total W_Z presheaf H with nontrivial fundamental group of U/H. Adjoining an initial object to U and setting the extended weight there to a singleton yields a total W-infinity presheaf, and its restriction back to the cosieve U recovers H. The lower-copy mapping cylinder turns this into the stated composition test. No finite cardinality bound or finite-example existence is asserted.

An independent agent audited the original Part F proofs, the exact DF criterion, and the original four-way equivalence, including the empty-action case, component subpresheaves, cone attachment homology, and the classical right adjoint in the composition reduction. The final scope audit supplied the low-truncation composition counterexamples and the exact one-point couniversality argument, which were independently checked before inclusion. The stable labels for the additions are F:DF-actions, F:remaining-equivalence, F:conditional-theorem3, F:total-functor-general, F:total-sieve-cosieves, F:low-sieve-composition, F:onepoint-cofibration, and F:onepoint-couniversal.

---

## Appendix 5: CD_C048_report.md

### Complete C048 localizer dichotomy

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.

#### Source verification

Cisinski (2006), Astérisque 308, Proposition 9.2.17(a)–(b), printed pp.369–370, explicitly applies to any fundamental localizer W. It identifies inversion of the sphere-category Δ/∂Δ^(n+2) with containment of W_n. Corollary 9.2.15 identifies the homotopy-group convention. The author-hosted PDF was opened on the web; the supplied published PDF was then inspected directly at background/papers/Cisinski_Ast308/smf_ast_308.pdf. The theorem numbers agree; pagination differs between versions. Citation uses published pagination.

The appearance of accessibility later in the proof concerns a particular minimal generated localizer; it is not a hypothesis on the arbitrary W in the proposition.

#### Proved deductions

The supplement sections/F_followup.tex gives an explicit groupoid proof that the Grothendieck-span comparison to an ordinary pushout is a W1-equivalence whenever one leg is injective on objects. Object injectivity makes the connector-based conjugation well defined; faithfulness is not needed, and the other leg may identify objects.

If S2 is W-aspherical, W1 is contained in W. Relative Theorem A supplies invariance of Grothendieck constructions under objectwise W-equivalences; the supplement proves this through the actual slices. Two-out-of-three therefore makes every object-injective functor a W-cofibration.

All full sieves consequently satisfy C048 when S2 is W-aspherical. Combining this with F:interval-impossibility proves the complete dichotomy: the maximal class is all full sieve inclusions when S2 is inverted, and only isomorphisms otherwise. This is a statement about the specified endpoint pushout-product operation, not an additional assertion about strict or total sieve composition.

#### Verification and reproducibility

The paths_audit sibling independently checked the published proposition, both connector functors and their natural isomorphism, the relative-Theorem-A argument, and the resulting dichotomy. Audit passed without a mathematical amendment.

code/cd_cisinski_source.py and its saved output verify the relevant numbered statements in the supplied published source. Extracted copyrighted source text remains outside the deliverable directory.

The supplementary statement ledger is research/CD_C048_results.csv.

---

## Appendix 6: AG_general_report.md

### Final general-localizer supplement

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

#### Scope and dependencies

The root requested this supplement after the complete C048 dichotomy was established. It concerns exactly the fundamental localizers containing W1, equivalently those making S2 aspherical. The source for that equivalence is Cisinski's Astérisque 308, Proposition 9.2.17(a)–(b), printed pages 369–370. The attached primary PDF is `background/papers/Cisinski_Ast308/smf_ast_308.pdf`; its text is `background_text/Cisinski_Ast308.txt`. We independently inspected the printed proposition and Corollary 9.2.15, which fixes the convention for n-equivalences. The proposition explicitly allows every fundamental localizer, with no accessibility restriction.

The independent groupoid-connector audit of F:span-groupoid checked the quasi-inverse on objects and all generating arrows. Object injectivity, rather than faithfulness or fullness, is what makes its conjugation functor well defined. The comparison therefore belongs to W1, and the relative Theorem A proof makes every object-injective map a W-cofibration for the localizers in this branch.

#### Results

`sections/D_general.tex` gives three numbered, Proved statements, with ledger rows in `research/AG_general_results.csv`.

First, total W-asphericity equals ordinary W-asphericity in this branch. An ordinary final functor becomes, after groupoid completion and specified skeletal equivalences, a functor bijective on objects and surjective on each endomorphism group. The pushout of that functor along its source-to-point map is the point. Since it is an object-injective W-cofibration, asphericity of its source passes to its target. The empty-source case is checked separately: finality then forces the target empty.

Second, for a presheaf H, all three conditions are equivalent: H is total, its element category is aspherical, and its element category is total. The proof uses the identity test, the preceding category result, and the already proved universal forward implication. The canonical final comparisons under Kan extension give an alternative direct verification. Empty presheaves satisfy all three conditions exactly when the empty category is W-aspherical. It follows that the strict and total functor classes coincide and that the two Dwyer-type sieve classes coincide.

Third, composition of these sieve classes holds if and only if every nonempty category is W-aspherical. If every nonempty category is aspherical, all full sieves belong to both classes. Conversely, any nonempty category V is a cosieve of its contractible initial cone. The general cosieve criterion for total sieve composition would force V to be total. A category V violating that conclusion yields the explicit lower-copy counterexample with a classical first factor and a terminal-object extension second factor. The already checked W0/W1 examples are finite instances; the present theorem imposes no finiteness assumption.

The supplement deliberately does not identify the coarse localizers by a separate classification theorem. Its exact condition is stated directly and needs no additional literature hypothesis.

The Dwyer subtask independently audited all three supplement proofs after they were written. It checked the object-bijective skeletal groupoid construction, the strict categorical pushout to the point, the empty final-source case, the canonical final comparison for presheaves, and the nonempty-cosieve argument. No mathematical gap was found. These files were then frozen at the root's request.

#### Related final audit corrections

The literal ordinary-cofibration claims C037 and C038 at XII ms. 111 are false, even for nonzero homology localizers satisfying full W(7). The two-object parallel-arrow category, with the source singleton as sieve, is discretely flat by the discrete-source weight test but has a two-point boundary presheaf. Every change of complementary category retains that discrete source and hence remains discretely flat. This corrects the companion's conditional/sketched treatment of those clauses; it does not contradict Proposition 7, whose tests concern membership in W rather than the cofibration condition.

For the narrower couniversal condition with complement isomorphic to the terminal category e, we supplied and independently checked the criterion subsequently written as F:onepoint-couniversal: couniversality for W-infinity is equivalent to total integral-homology asphericity of the boundary presheaf. Its essential step is that such a presheaf's element projection induces the zero map on fundamental groups. Pulling back the ambient coset local system for the cyclic group generated by an image element gives an acyclic covering component surjecting onto that cyclic group, forcing it trivial. Cone attachment then preserves the fundamental group and universal-cover homology. This places the remaining one-point recognition question in the same equivalence class as the outstanding strict-sieve composition and discrete-flatness question.

The phrase “terminal complement” must mean that the full complementary category is isomorphic to e, with one object and only its identity. Merely having a terminal object would include the existing three-object C035 counterexample and is a different assertion.
