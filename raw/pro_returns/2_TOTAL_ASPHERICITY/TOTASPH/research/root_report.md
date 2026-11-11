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

