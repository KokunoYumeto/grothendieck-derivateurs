| Prompt item | Outcome | Statements / record |
|---|---|---|
| A.1 | Proved; Lead1(a)–(c) | A.1–A.2 |
| A.2 | Proved; explicit repaired K* cone | A.15 |
| A.3 | Proved; strict at every n≥3, also n=2 | A.3–A.8 |
| A.4 | Proved for every fundamental localizer; exact intermediate criterion | A.10–A.14 |
| A.5 | Cosieve closure and composition refuted for every finite n≥2; all inclusions decided | A.9 |
| B.1 | Known; compressed R12 proof audited | B.1 |
| B.2 | Classification proved; D₁⇒D refuted; strict 2-category version proved | B.4; B.7; B.9 |
| B.3 | Every implication decided, including within set presheaves | B.3; B.5–B.8 |
| B.4 | Proved for every bounded reachability interval | B.2 |
| B.5 | Corrected manuscript statements proved | B.10 |
| C.1 | Proved; integral obstructions checked independently | C.1–C.3 |
| C.2 | Complete classification proved | C.4 |
| C.3 | Low localizers and represented derivators classified; arbitrary-derivator W7 proved | C.5–C.8 |
| C.4 | Ordinary, strict and total endpoint classes determined | C.7 |
| D.1 | Principal filteredness assertion refuted; requested C_delta FreeMon subcase still under investigation, with proved reductions and an invariant-length criterion | D.6–D.10; notes/D_Cdelta_attempts_*.md |
| D.2 | Lead3 formulas and hand computation proved | D.1–D.3 |
| D.3 | Proved for every FreeMon diagram on Δ_inj | D.6–D.7 |
| D.4 | Free-group alternative proved; earlier examples audited | D.4–D.5 |
| E.1 | Lead4(a) false as stated; corrected comparison and (b),(c) proved | E.1–E.4 |
| E.2 | Groups determined for every n, finite and arbitrary acts | E.5 |
| F.1 | Corrected manuscript ledger proved | F.1–F.3 |
| F.2 | Source access, exact inspected statements and search record supplied | Bibliography; source ledger below |
| G.1 | Both assertions refuted for Wtilde itself | G.1–G.3 |
| G.2 | General weak-axiom assertions refuted; each Wtilde case decided; repairs proved | G.4–G.10 |
| G.3 | Both implications proved; immediate direction and manuscript passage identified | G.6 |
| G.4 | General infinite lemma refuted; fractions and model cases proved | G.11–G.14 |
| Lead1 | (a)–(d) proved | A.1–A.2; A.15 |
| Lead2 | All formulas and classification proved | C.1–C.4 |
| Lead3 | All clauses proved, with stronger exact-index theorem | D.1–D.7 |
| Lead4 | (a) refuted as written; corrected comparison and (b)–(d) proved | E.1–E.5 |
| Lead5 | (a)–(c) proved with precise coherent interpretation; suggested converse refuted | B.2–B.8 |
| Lead6 | Proved for every fundamental localizer | A.10–A.14 |

# DER_FOLLOWUP report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. No priority is claimed. This is a working return: the table above distinguishes the proved/refuted statements from the explicitly requested C_delta free-monoid case that remains under investigation. The numbered register certifies individual statements; its statuses do not assert that every requested subcase is finished.

## Mathematical outcomes and their scope

### A. Every level of the tower is different

For each n≥2, A.3–A.8 define the category A_n(F₂) of finite linearly ordered sets carrying an n-cocycle, with increasing cocycle-preserving injections. Its classifying space is K(F₂,n). The proof controls **every component of every set-valued action**, through injectivization, the Fraïssé limit, finite supports, and the pointwise-stabilizer description. Each component is contractible or has the homotopy type of the base. Thus A_n(F₂) belongs to Q_n and not to Q_(n+1). The proof includes a specified integral n-cycle and a mod-two evaluation equal to one; it is not inferred from the finite computations.

Writing T_n for total W_n-asphericity, A.9 gives the strictly interleaved chain T₁ ⊋ Q₂ ⊋ T₂ ⊋ Q₃ ⊋ T₃ ⊋ …, with totality as the intersection. Initial cones on the named witnesses are total for W_n but have nonempty cosieves that are not. Consequently totally W_n-dwyérienne sieves fail to compose for every finite n≥2. A.15 separately gives the requested K* witness at n=2, including the deterministic choice of its attachment data and the audit of the surviving binary-cycle class.

Lead 6 is proved for every fundamental localizer, without an accessibility hypothesis: a nonempty category A is total for W exactly when BA is W-aspherical and every component of every action has W-aspherical unreduced suspension. A.10–A.11 give the collage, homotopy-colimit, wedge, and retract comparisons used in both directions. A.12–A.14 characterize precisely when the suspension condition lies strictly between adjacent Q_n classes, including arbitrary localizers. The general realization theorem uses simplex categories of connected Kan complexes and controls connected covers, so the criterion is an equivalence rather than a necessary condition alone.

### B. The all-sequence condition has an exact classification

The three local conditions are equivalent: (2F) ⇔ (DESC) ⇔ (LOC). They imply the all-sequence property D, which implies D₁. Both final converses are false, already for presheaves of sets. B.6 supplies D without LOC; B.7 supplies D₁ without D. B.8 records every implication and gives the specialization to set-valued diagrams.

B.4 gives the necessary and sufficient condition for an arbitrary Cat-valued diagram. Extend it by filtered colimits over finite suborders to countable colored orders with unbounded alternation. Then D holds exactly when all maps of this extension are weak equivalences; equivalently the two maps in the canonical span Fω(L) → Fω(L+J) ← Fω(J) are weak equivalences for every such L and a fixed alternating J. The proof identifies these particular comparison maps and their canonical roofs. It does not replace the requested comparison by an abstract isomorphism of homotopy types.

The bounded reachability interval theorem B.2 supplies the missing local coherence input. Its proof identifies a finite moment body and treats the boundary/complement comparison through relative simplex categories. B.9 establishes the comparison as weak equivalences of strict 2-categories in the dimension-two convention used by 317, using the opened primary results on the relevant nerves. No Lean compilation of 317 was run here.

The manuscript discussion keeps three hypotheses separate. Full path diagrams are the positive case already settled in PATHS/INDLOCAL. Merely asking parallel type maps to induce homotopic maps is weaker than coherent descent; this suffices for the indicated π₀ assertion, but no stronger theorem is silently transferred to it. The discrete counterexamples in B.6–B.7 are not asserted to satisfy that extra homotopy hypothesis. B.10 corrects the negative phrase at VII ms.112 in its actual full-path context and retains the legitimate failure for arbitrary fibred diagrams.

### C. Strict endpoint functors and derivator coefficients

C.1–C.3 prove the two integral obstruction formulas of Lead 2 for paths of every length. For the walking retraction the quotient is Z, generated by the identity at z modulo the idempotent ur; independent integer calculations on the specified finite path categories confirm the formula. These computations support, but do not replace, the arbitrary-length proof.

For W∞, W_Z, and W_n with n≥2, the endpoint functor of the full based path category is strictly aspherical exactly when its target is a connected thin groupoid; strict and total asphericity coincide for these endpoint functors. The low truncations are different: for W₀ and W₁, strict and total endpoint asphericity require respectively 1- and 2-connectivity of BY. Ordinary asphericity requires (n+1)-connectivity for W_n; for W∞ or W_Z it requires weak contractibility of BY. C.6 gives the actual slice-to-path-space comparisons behind this distinction.

C.7 also checks the represented-derivator classifications used from REVLOC and the scope of its group-fibration test. C.8 proves the requested open-sieve half of W7 for an arbitrary derivator satisfying Der1–Der4. The proof uses the right projectors, their fibrewise Kan-extension formulas and base-change maps, and the unit/counit criterion at the fixed derivator. An independent audit confirms that it does not replace the hypothesis by equivalence on all shifted derivators or require strongness.

### D. The general filteredness assertion is false; one named subcase remains

D.6 proves that **every nonempty connected exact category passes every free-monoid comparison**, with colimit taken in Mon and arbitrary word substitutions as transition maps. The proof applies Theorem A to the translation comma categories. The local categories are free categories with a fixed object set; exactness kills the higher derived-colimit terms, and the colimit translation category has an initial object. Its fundamental group and integral homology are both controlled, giving contractible comma categories. This is stronger than a statement restricted to basis maps.

Therefore Δ_inj is the explicit nonfiltered counterexample requested in the principal assertion of Part D.1. In particular every colimit monoid of a free-monoid diagram over Δ_inj has aspherical classifying space. The interval diagram in Lead 3 has presentation ⟨x,y,z | xy=x, y²=y, yz=z⟩; its group completion is free on x,z. D.3 checks its presentation and H₂ calculation, and D.6 supplies full asphericity.

Lead 3's homology and fundamental-group formulas are proved with the stated totality hypothesis, and free-group diagrams over exact categories all pass. Over the total nonexact C_delta, D.4 proves that the proposed presentation gives finitely generated free groups, that its maps are free-factor inclusions, and that its abelianization is Q with T₁(Q)=Z. Its group colimit is F(u,v), so the specified comparison fails in H₂. This completes the free-group alternative explicitly allowed in Part D.4. The free-factor examples from TOTAL_EXACT_2 C.8 and C.9 are audited separately; neither contradicts the exact-index theorem.

The prompt additionally asks that the free-monoid test over C_delta itself be settled. A free-group basis chosen separately at each object does not supply a functor to FreeMon. That specific all-diagrams question remains under attack and is recorded without a positive or negative verdict. Its current precise obstruction, unsuccessful routes, and next step are in the C_delta attempt logs. Neither the Δ_inj refutation nor the free-group alternative is used to conceal this extra requested case.

The subsequent investigation made two precise reductions of this case.
D.8 proves that the comparison succeeds whenever the filtered-limit monoid
over the actual finite closed substructures of the Fraïssé limit is free.
Its proof compares the original and saturated diagrams in every simplicial
degree and compares their ordinary monoid presentations. In particular,
all the proposed first-return kernels of maps from basis-map free monoids
to group diagrams pass the test, even if the group maps are noninjective.
D.9 reduces the universal C_delta question to finite-rank free-monoid
diagrams with injective transitions. The reduction uses the word defect
theorem to construct finite free charts in any filtered limit, the stability
criterion to make their finite free hulls intrinsic, and stabilizers to make
the replacement strictly functorial. Both reductions transfer the canonical
comparison, not merely an abstract homotopy type. They leave the injective,
potentially nonfree-limit case unresolved.

D.10 supplies a further sufficient condition: a strictly positive,
G-invariant additive real length on the filtered-limit monoid forces the
comparison to succeed and forces every higher derived colimit of the
abelianization to vanish. Such a length makes every fixed submonoid closed
under factors. Finite free charts then give a distributive support filtration
of the translation graph-chain modules; its quotients are sums of
representable modules with arbitrary constant coefficients. This proves
the required acyclicity and contracts the comparison comma. It also proves
that the specific based positive-matrix stabilization constructed in the
attempt notes has no strict FreeMon lift: its positive invariant functional
would contradict its nonzero T₁. This excludes that candidate construction
globally. The theorem assumes the length condition; it is not asserted for
all diagrams, and does not settle the remaining case.

### E. All acts over End_Δ([n])

Every right M_n-act is uniquely represented, up to isomorphism, by K_n for an n-skeletal simplicial set K; finite acts correspond to finitely many nondegenerate simplices. E.1 proves this through the explicit idempotent completion and skeletal extension. E.2 proves B(M_n/K_n) ≃ |K| for every K of dimension at most n, including infinite K.

Lead 4(a)'s further reduction to a category of nondegenerate simplices is false for arbitrary K when n≥2. For Δ[2]/∂Δ[2], that proposed category has two objects and three parallel nonidentity arrows, with H₁=Z², whereas the realization is S². This does not invalidate PRETOT A.4, whose actual hypothesis is free degeneracy completion. The corrected all-simplex comparison is enough for the requested classification.

The act K_n is totally W_Z-aspherical exactly when |K| is acyclic, equivalently when Z[K_n] is projective and |K| is nonempty and connected. It is totally W∞-aspherical exactly when |K| is weakly contractible. E.4 proves both statements with the restricted-action Tor formula; arbitrary actions on M_n/H are not substituted for restricted actions.

The possible fundamental groups are fully determined. For finite acts, n=1 gives only the trivial group; n=2 gives precisely groups with a finite balanced presentation and trivial abelianization, equivalently fundamental groups of finite acyclic two-complexes; n≥3 gives precisely finitely presented superperfect groups. Without finiteness, n=2 gives groups with a presentation whose exponent-sum map between the free abelian groups on relators and generators is an isomorphism; n≥3 gives all small superperfect groups. The construction remains in the required dimension, including at n=2, by the face-poset mapping-cylinder realization in E.5.

### F. The corrected manuscript statements

F.1 gives filtered ⊊ exact ⊊ total ⊊ quasi-filtered, with Δ_inj, C_delta and the specified K* as successive witnesses. F.2 gives a particularly small answer to XII ms.93–97: the five-element M₁-act of the two-edge interval is totally W∞-aspherical, but its category of elements fails even Q₂. A doubled action along its two-edge cosieve has H₁=Z. The forward implication from a total element category to a total presheaf holds for every fundamental localizer.

F.3 records the manuscript locations and their exact corrected statements. It also writes out the coend/collage argument for strict composition of functors, the slice argument for total composition, and an independent reconstruction of the finite strict-sieve composition counterexample from PRETOT. These are distinct composition assertions. The published sources used in the paper, unavailable named sources, supplied AI returns, and exact inspected theorem numbers are listed in the source ledger below.

### G. The literal weak localization axioms are insufficient

G.1 checks all four conditions defining Wtilde, maps the axiom numbering to the literal Chapter XVI axioms, proves Loc(1), proves strong saturation, and identifies its aspherical objects as the weakly contractible categories. The finite relative-Theorem-A witness is reconstructed independently. Wtilde satisfies Loc(1)–(3), (8), and (9), but fails the relative axiom and forward gluing.

For Wtilde itself, products fail, the localization functor fails to preserve finite products, and the required homotopy left Kan adjoint for a span does not exist. The latter assertion is an adjunction obstruction, not merely a failure of a particular proposed formula. The rational mapping-cone invariant forces an impossible divisibility condition on the image in H₃. G.8 gives the complete contradiction.

Propositions 9.11 and 9.12 and Corollary 9.13 do hold for Wtilde; the corollary's premise is vacuous in the relevant branch. They fail under Loc(1)–(3) in general, as shown by the separately defined Wsharp, which permits merging two circle components while preserving total H₁. G.6 proves the strongest unconditional implication diagram. Retract closure restores the three propositions; Loc(8) supplies it. Loc(6′a) together with Loc(8) restores relative Theorem A, product stability, preservation, and all the homotopy left Kan extensions. Wtilde already has Loc(8), so that axiom by itself does not repair its failures.

For Proposition 9.12, (c)⇒(c′) is immediate. The reverse implication is proved in contrapositive form through the quotient category on XV ms.133 ter–quater. The edition's note at ms.133 bis reverses these affirmative directions. The displayed map h=(f₀,f₁) at ms.133 quinquies has target Y, not the mistyped target. Both corrections are justified in G.6 with the maps typed explicitly.

Finite products after localization are preserved when identities belong to W and W is stable under those products. The unrestricted infinite-product assertion is false. G.12 constructs the free countable-product completion of an alternating zigzag category; every individual factor has the required localized arrow, but any single zigzag has a uniform finite length, preventing a morphism to the product tuple. G.13 and G.14 prove the repairs with a calculus of fractions and for model-category weak equivalences, respectively.

## Audit of earlier returns, reviews, and external formalization

| Input | Step checked and outcome |
|---|---|
| R1–R2 | The action criterion, cyclic-cover argument, restricted-action distinction, cone inheritance, and cosieve/composition reduction are followed where used in A, D, E and F. No error found at those steps. |
| R3–R4 | The affine-equalizer and weakly-terminal arguments are checked against Isbell–Mitchell; the historical citation is restored. The infinite cocycle witnesses do not evade a finite obstruction by truncating the claim. |
| R5–R6 | The closure operations actually used and the exact-to-total argument are audited. The affine-cone proof for Δ_inj and colored words is recorded in D.7. No assertion about the inaccessible Isbell 1974 body is made. |
| R7 | The stronger group/RAAG tests are kept separate from free-group and FreeMon tests. D.2 and D.6 explain why the latter do not detect filteredness. |
| R8 | The Tor comparison, simplicial projectivity argument, and actual free-degeneracy hypothesis are checked. The false extrapolation lies in Lead 4(a), not in PRETOT A.4. |
| R9 | Strict and total functor composition are audited in F.3. The finite strict-sieve counterexample is independently reconstructed; total W∞-sieve composition and finite-truncation failures are distinguished. |
| R10 | Ordinary, strict, total, and bounded-path endpoint statements are kept separate. Lead 2 closes the full-path question; the truncated walking-retraction positive statement is not transferred to all paths. |
| R11 | The basis-map result and its necessity are retained with their limited scope. D.6 supplies a new proof for arbitrary monoid homomorphisms over exact indices. |
| R12 | The compressed coefficient argument is written out over every nonzero ring. The injective/constant letter-map obstruction and the finite relation presentation are independently checked. |
| R13 and R18 | PATHS' descent and INDLOCAL C.21/C.23 are read and audited before use. One-sign exceptions and the uniform-comma criterion are retained. Their positive path results are not reannounced as unresolved. |
| R14 | The corrected K* construction and the C.27 rerun with component markings are followed in full. A.15 records the specific choices and the nonzero H₂ survivor. |
| R15 | The relevant historical attributions are restored. POLES and the separately mentioned XII appendix were not supplied; no uninspected body is used to certify their claims. The full source ledger records the limits. |
| R16 | Original bodies were opened where obtainable. Fiedorowicz's and Gray–Steinberg's exact hypotheses are kept; no unconditional amalgam theorem is substituted. The unavailable McDuff and Higman bodies are not mathematical inputs. |
| R17 | The finite-support/stabilizer and action-reduction proof of totality, and the T₁(Q) calculation of nonexactness, are audited in D.4. No correction is needed at the steps used. |
| 317 | The n=2 nerve convention used here is checked against the supplied source and opened primary papers. This return makes no claim to have run its Lean development. |
| R19, cote104 | The pinned public Lean source is read. The criterion includes skeletalness and identity endomorphisms; monicity alone is insufficient. Mathlib PR44731 was closed unmerged, so it is not reported as an accepted Mathlib theorem. |
| R19, cote105 | C.8 supplies the full arbitrary-derivator proof independently; `notes/C8_independent_audit.md` records the separate audit. |
| R19, cote106 | The pinned source gives localization morphisms as π₀ of the specified span category under its actual C1–C3/cofibrancy hypotheses. This is not silently strengthened to an ordinary Ore calculus or one-step common refinement. |
| R19, cotes114/118 | The invalid reverse implications and the unqualified (g)⇒(c) are not used. The author's primary MathOverflow correction was opened. |
| R20 | The expert's affirmative implication direction at XV 133 bis is confirmed. The finite-product statement is retained under its actual hypotheses; the infinite statement is refuted in G.12. |
| R21 | REVLOC F.1 and F.1.1 are checked with the literal axiom numbering and new finite computations; the used represented-derivator and group-fibration claims are audited. Unused S2COUNT and REVLOC assertions are not claimed reverified merely because their registers were attached. |

The historical Adámek–Reiterman 1976 theorem II.3 is opened and recorded but is **not used as an unconditional exactness equivalence**: that reading conflicts with the independently audited total nonexact example. Likewise, a catalogue page or abstract never counts here as opening a mathematical body. The prompt's statement that the Adámek–Koubek–Reiterman 1981 paper was in the package does not match the attached manifest; the unsuccessful retrieval route is recorded explicitly.

The public R19 audit is pinned to commit `08e7d549678e7434e4d21d95a2cefa8e74fd2acf`. Its fetched sources, metadata, hashes, and the exact inspected definitions are retained in `notes/R19_public_sources/` and `notes/F_R19_audit.md`. Reading a Lean proof is distinguished from executing it: no local Lean build was performed in this return. The source project's stated AI attribution is recorded as stated, without guessing an effort setting or assigning the present work to a human author.

## Independent computations

| Program | Certificate and checks |
|---|---|
| `A_cocycle_checks.py` | Moore complexes for p=2,3 and degrees 2–6; 162 three-piece cohomology checks; 270 anchored amalgams over F₂,F₃,F₅; integral cycles ξ₂,…,ξ₆ with zero boundary and nonzero mod-two evaluation; barycentric flag counts 12,48,240,1440,10080. |
| `B_type_checks.py` | 88,735 and 187,917 functor-law checks for the two set diagrams; 511 R12 target words and 2,561 injectivity checks; 2,283 relation images; amalgam and naturality checks for the D₁/D separator. |
| `CD_finite_checks.py` | Walking-retraction paths through length two: 25 objects, 585 arrows and 13,776 compositional checks. The two restricted-action categories have 34 objects and 803/819 arrows; exact integer computations give H₁=Z and the expected quotient span Z·e. |
| `CD_freefactor_checks.py` | Interval-monoid critical overlaps, 434 edge images, and the degree-two homology certificate; 39,364 reduced-word checks for the finite C.9 example; 172 small predimension hypergraphs, 775 closed embeddings and private-vertex/free-factor certificates. |
| `E_acts_checks.py` | Truncated simplicial functor laws, M₂ multiplication and act data; the two-object, five-arrow nondegenerate-simplex counterexample with H₁=Z², compared with the S² realization. |
| `F_five_act.py` | Complete M₁ and five-element act; its 5-object, 15-arrow element category and the 8-object, 28-arrow doubled action; an integral Smith certificate giving H₁=Z. |
| `F_strict_composition_check.py` | Independent 52-element act reconstruction; unimodular relator matrix; nontrivial 60-element permutation quotient; 32-arrow and 138-arrow collages; both sieves, the right adjoint, 2,131 pairs and 28,204 triples. |
| `G_finite_witnesses.py` | Degree-two and degree-one sphere maps on 50- and 26-object face posets; the 77→53-object relative-A failure; the 400→208-object product with H₃ multiplication by two; the span-adjoint obstruction; the 12→11-object Wsharp component merge. |
| `G_zigzag_bound.py` | 29,660 finite tuple-morphism checks supporting the uniform-length obstruction in the infinite-product example. |

Every program's output is retained under `code/outputs/`. Finite enumeration verifies the explicit algebra and certificates; all universal quantifiers are proved in the paper. Search/fetch scripts, manifest checks, bibliography/register assemblers, build scripts, and their outputs are also included. The reproducibility guide distinguishes mathematical checks that run from this package alone from source-audit scripts that require the supplied background or network access.

The ongoing C_delta investigation also has explicit attempt certificates:
`D_positive_checks.py` checks the positive-matrix diamond with no strict word lift
in its specified bases, the free-group lift, and the Nielsen splitting;
`CD_ratio_chart_obstruction.py` checks the finite positive hypergraph obstruction
to the proposed ratio chart; `CD_band_levi.py` checks all equal-product quadruples
in the five-element rectangular band; and `D_root_obstruction_checks.py` checks
the finite graph showing why first-return loop monoids do not recover the whole
graph's fundamental group, and the positive-conjugation obstruction;
`D_saturated_amalgam_check.py` checks a span of saturated positive free-factor
embeddings with no nonerasing free-monoid cocone. The finite suffix-chart
search is retained in `CD_suffix_length_search.py`: its successful finite
charts do not supply a simultaneous strict functor on all closed embeddings.
These rule out particular shortcuts. None is reported
as a decision of the remaining C_delta comparison.

## Literature access and searches

The following ledger gives one entry for every bibliography source, with opened/not-opened status and exact inspected theorem numbers or failed access attempts. The detailed query logs are `notes/A_sources.md`, `notes/BE_sources.md`, `notes/B_interval_sources.md`, `notes/CD_sources.md`, `notes/G_sources.md`, `notes/F_A_source_ledger.md`, and `notes/F_B_general_source_ledger.md`. These cover the specifically requested searches for A.3, B.2, C.2, D.1, E.2, G.1, G.2 and G.4. Failure to find an earlier statement is not a priority claim.

Current register: **65 numbered statements**, with 6 Known, 49 Proved, 10 Refuted. Bibliography: **92 entries**, 78 opened at the recorded passages and 14 whose body was not obtained.

# Consolidated primary and supplied-source ledger

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Audit date: 17 November 2026. No priority is claimed. “Opened” means the mathematical body at the specified passages was inspected; an abstract, catalogue record, or inherited access claim is not counted. Exact attempts and proof audits are retained in the section source logs.

| Source key | Source | Access and closest inspected statements |
|---|---|---|
| `Cisinski2006` | Cisinski, Denis-Charles, *Les prefaisceaux comme modeles des types d'homotopie* (2006) [primary route](https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf) | Opened: Definition 3.3.2, Sorites 3.3.8, especially (7), and Proposition 3.3.16. The section records these localizer facts with a reference for proofs; Claim A.10 supplies the direct special-case proof needed here, without an accessibility assumption. Part G additionally opened Definitions 1.4.1 and 1.4.12, Proposition 3.4.25, Proposition 4.2.4, Definition 4.2.11, Theorem 4.2.15, Remark 4.2.16, and Theorem 6.1.18 with its proof. |
| `GoerssJardine1999` | Goerss, Paul G. and Jardine, John F., *Simplicial Homotopy Theory* (1999) [primary route](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf) | Opened in the reprint PDF: Proposition I.5.2 and Corollary I.5.3(2), printed pp. 21--22; Theorem III.2.1, Proposition III.2.2, Corollary III.2.3, and the discussion and Corollary III.2.7, printed pp. 146--153. Used for the mapping-space fibration and normalized homotopy-group calculation; explicit cocycle and horn constructions are supplied in this paper. |
| `CampionYeAEC2020` | Campion, Tim and Ye, Jinhe, *Homotopy Types of Abstract Elementary Classes* (2020) [primary route](https://arxiv.org/pdf/1909.07965) | Opened: arXiv v2, 18 May 2020; Theorem 3.6, Corollary 3.7, Remark 3.8, and Examples 4.1--4.3. These realize prescribed base homotopy types with amalgamation; they are context, not a substitute for the all-action assertions proved here. |
| `CampionYeHigher2026` | Campion, Tim and Ye, Jinhe, *Non-trivial higher homotopy of first-order theories* (2026) [primary route](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/nontrivial-higher-homotopy-of-firstorder-theories/30EF8141591F08DF334EE40E5F51BD38) | Primary full text opened: Introduction; Section 1 through Corollary 1.14 and Section 2 through Corollary 2.8. Published online 11 January 2024; issue dated March 2026. The K(Z,2) result is background, not an input to the all-level construction. |
| `EvansHubickaKonecnyNesetril2020` | Evans, David M. and Hubi\v cka, Jan and Kone\v cny, Mat\v ej and Ne\v set\v ril, Jaroslav, *EPPA for two-graphs and antipodal metric spaces* (2020) [primary route](https://arxiv.org/pdf/1812.11157) | Opened: arXiv v2, introduction and definitions, Section 7 including Proposition 7.1 and Corollary 7.2 with proofs. The degree-two F2 cocycle structures are the ordered two-graphs defined there. No EPPA, Ramsey, or imaginary-elimination theorem from this source is assumed in the proof. |
| `CDLenz2011` | Lenz, Oliver Urs, *The classifying space of a monoid* (2011) [primary route](https://cwi.ugent.be/~oulenz/publications/lenz-2011-classifying.pdf) | 20 December 2011. Opened author PDF; Proposition 4.4.1 and Corollary 4.4.6 read for free-monoid group completion |
| `CDPolygraphs2025` | Ara, Dimitri and Burroni, Albert and Guiraud, Yves and Malbos, Philippe and Metayer, Fran\ccois and Mimram, Samuel, *Polygraphs: From Rewriting to Higher Categories* (2025) [primary route](https://webusers.imj-prg.fr/~yves.guiraud/articles/polybook.pdf) | Author PDF opened; Theorem 7.3.5, Propositions 9.2.3 and 9.3.2 read at the steps used |
| `IsbellMitchell1973` | Isbell, John R. and Mitchell, Barry, *Exact colimits* (1973) | Attached primary PDF read in full; Theorems 1 and 3 and Lemma 1 used. Full proofs are only sketched in this announcement; the supplied explicit affine-cone proof was also checked |
| `CDFiedorowicz1984` | Fiedorowicz, Zbigniew, *Classifying Spaces of Topological Monoids and Categories* (1984) [primary route](https://www.uio.no/studier/emner/matnat/math/MAT9580/gamle-undervisningsressurser/varen-2018/documents/fiedorowicz-classifying-spaces-of-topological-monoids-and-categories-amer-j-math-1984.pdf) | Primary PDF opened; Proposition 4.4 and its proof read. The amalgamation claim relying on Lemma 5.2(a) is not used, in view of Gray--Steinberg's counterexample |
| `CDEvrard1975` | Evrard, Marcel, *Fibrations de petites categories* (1975) [primary route](https://www.numdam.org/article/BSMF_1975__103__241_0.pdf) | Primary PDF opened; path replacement and Theorems A and B inspected as nearest literature. Not a source for the strict endpoint classification |
| `CDFiedorowicz2002` | Fiedorowicz, Zbigniew, *A counterexample to a group completion conjecture of J. C. Moore* (2002) [primary route](https://www.maths.tcd.ie/EMIS/journals/UW/agt/ftp/main/2002/agt-2s3.pdf) | Primary article opened in full; the five-element rectangular-band lemma informed a discarded counterexample route, not a proof dependency |
| `CDMcDuff1979` | McDuff, Dusa, *On the classifying spaces of discrete monoids* (1979) [primary route](https://celebratio.org/McDuff_D/article/412/) | Bibliographic record and abstract opened at Celebratio Mathematica; original article body not obtained despite searches and DOI attempt. No proof depends on it |
| `CDShoikhet2016` | Shoikhet, Boris, *On Evrard's homotopy fibrant replacement of a functor* (2016) [primary route](https://arxiv.org/abs/1412.0317) | Attached primary source read in Sections 2 and 3 at the path replacement, shift and base-change steps. This is a homotopy-fibration construction, not the strict endpoint criterion |
| `CDCisinski2009` | Cisinski, Denis-Charles, *Locally constant functors* (2009) [primary route](https://www.math.univ-toulouse.fr/~dcisinsk/lcmodcat3.pdf) | Primary author PDF opened; Section 3, especially Theorem 3.6, Corollary 3.8, Lemma 3.9, Proposition 3.10 and Theorem 3.13, read with proofs. The proof extends the projector argument from all arrows to an arbitrary specified subcategory |
| `CDCisinski2008` | Cisinski, Denis-Charles, *Proprietes universelles et extensions de Kan derivees* (2008) [primary route](https://www.math.univ-toulouse.fr/~dcisinsk/puhot.pdf) | Primary author PDF opened; Definitions 0.1--0.2, Propositions 2.4 and 3.12, Theorem 3.24 and Corollary 3.26 inspected to verify the Der 1--4 hypotheses and the variance of Kan extensions. No strongness axiom is assumed |
| `GMaltsiniotis2020` | Maltsiniotis, Georges, *La theorie de l'homotopie de Grothendieck* (2020) [primary route](https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/prstnewprov2020.pdf) | Opened: provisional version, March 2020; Section 3.1, especially Proposition 3.1.2, Theorem 3.1.4, Lemma 3.1.5, and Theorem 3.1.7. The hypothesis is strengthened from weak to fundamental localizer before Lemma 3.1.5. Used in G.10. |
| `GQuillen1973` | Quillen, Daniel, *Higher algebraic $K$-theory. I* (1973) [primary route](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf) | Opened: Section 1, Proposition 2 and corollaries (adjoints and contractibility), Proposition 3 (filtered colimits), Theorem A and its two comma orientations. Used for the absolute axiom in G.1 and G.4. |
| `GMathlibFiniteProducts` | Mathlib contributors, *Mathlib.CategoryTheory.Localization.FiniteProducts* (2026) [primary route](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Localization/FiniteProducts.html) | Opened on 17 November 2026: theorem preservesProductsOfShape and the explicit Finite hypothesis. Literature record for G.11; no Lean execution claimed. |
| `GDERXV` | Grothendieck, Alexander, *Les Derivateurs, Chapter XV, attached transcription* | Opened: manuscript pages 116--137, including Propositions 9.11--9.12, Corollary 9.13, Section 10.1, and the edition notes. Attached file DER_XV-b.tex. |
| `GDERXVI` | Grothendieck, Alexander, *Les Derivateurs, Chapter XVI, attached transcription* | Opened: manuscript pages 1--16, the axiom and size sections, and passages of pages 99--118 on products, homotopy Kan extensions, and gluing. Attached file DER_XVI.tex. |
| `GR20` | Claude Fable 5.2 (Anthropic), *The Derivateurs field expert's answers XV.8, XV.9, XVI.1--XVI.3* (2026) | Opened in full: attached R20_expert_XV_XVI.md, 15 November 2026, AI-produced, effort max, previously unreviewed. Its direction correction is confirmed; its open weak-localizer and infinite-product questions are settled in G.3--G.14. |
| `GREVLOC` | GPT-6 Astra (OpenAI, ChatGPT Pro mode), *REVLOC, Part F: The literal axioms* (2026) | Opened: attached sections/F12.tex, F.1 and F.1.1 read in full and independently checked in G.1--G.2 and G.9. REVERSIBLE_LOCALIZERS checkpoint 17, AI-produced, previously unrefereed; no human authorship attributed. |
| `GZhang2026` | Zhang, Chencheng, *Gabriel--Zisman Localizations, Products, Coproducts, and Product Categories* (2026) | Primary abstract retrieved; full text not obtained. Tried arXiv abstract, HTML, PDF, export.arxiv PDF, and ar5iv; disabled or inaccessible. No numbered theorem or proof from this source is used; G.12 is proved independently. |
| `GCisinskiMO2019` | Cisinski, Denis-Charles, *Answer to ``Example of a weak basic localizer which is not a basic localizer''* (2019) [primary route](https://mathoverflow.net/questions/348949/example-of-a-weak-basic-localizer-which-is-not-a-basic-localizer/348953) | Opened primary answer, posted 22 December 2019 and updated 26 December 2019. Search-context record only; no result of the present part is inferred from it. |
| `Kervaire1969` | Kervaire, Michel A., *Smooth homology spheres and their fundamental groups* (1969) [primary route](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kervsmoo.pdf) | Opened: original article, Theorem 1 and its use of the Hopf exact sequence. Comparison only; the dimension-three complex construction is proved in E.5. |
| `StacksDK` | The Stacks Project Authors, *The Dold--Kan Correspondence* (2026) [primary route](https://stacks.math.columbia.edu/tag/019D) | Opened: Tag 019D, Theorem 14.24.3 and the explicit inverse construction. |
| `StacksTruncated` | The Stacks Project Authors, *Truncated simplicial objects* (2026) [primary route](https://stacks.math.columbia.edu/tag/017Z) | Opened: Tag 017Z, Definition 14.12.1. Its skeleton notation denotes restriction; our full simplicial skeleton is stated separately. |
| `LurieHTT` | Lurie, Jacob, *Higher Topos Theory* (2009) [primary route](https://people.math.harvard.edu/~lurie/papers/HTT.pdf) | Opened: original author PDF, Theorem 4.1.3.1, Corollary 4.1.3.3, Proposition 4.2.3.14, and Proposition A.3.3.2. Proposition 4.2.3.14 concerns all simplices and does not justify the false nondegenerate-simplex reduction in Lead 4(a). |
| `BCegarraHeredia2015` | Cegarra, Antonio M. and Heredia, Benjamin A., *Homotopy colimits of 2-functors* (2015) [primary route](https://arxiv.org/pdf/1504.06114) | Opened: the 32-page preprint, Theorem 5.1 and the covariant/contravariant Grothendieck constructions in Section 4. Theorem numbering cited is that of this opened version. |
| `BAraMaltsiniotis2014` | Ara, Dimitri and Maltsiniotis, Georges, *Vers une structure de categorie de modeles a la Thomason sur la categorie des n-categories strictes* (2014) [primary route](https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/nthom.pdf) | Opened: Theorem 6.27, Section 5 nerve conventions, and Proposition 8.14. Used only in dimension two, where the proper combinatorial Thomason structure is established. |
| `BHirschhorn2003` | Hirschhorn, Philip S., *Model Categories and Their Localizations* (2003) [primary route](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pshmain.pdf) | Opened: Definition 15.1.16, Example 15.1.19, Proposition 15.10.4(1) and its proof, Theorem 15.10.8(2), Theorem 19.9.1(1), and Theorem 19.4.2(1). These supply the exact Reedy comparison used in the relative simplex-complement lemma for B.4. |
| `FAIsbell1968` | Isbell, John R., *A Note on Exact Colimits* (1968) [primary route](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/344EA0110F34F24298FD42E14305F634/S0008439500056836a.pdf/a-note-on-exact-colimits.pdf) | Opened: complete primary PDF; unnumbered theorems of Sections 1 and 2, pp. 569--572. Current-run audit. |
| `FAIsbell1974` | Isbell, John, *Exact Colimits. I* (1974) [primary route](https://annals.math.princeton.edu/1974/100-3/p05) | Body not obtained: Annals and JSTOR records opened, exact-title searches and JSTOR PDF request attempted; the latter was inaccessible or returned a non-PDF access page. No mathematical-content claim or theorem number is asserted. |
| `FAIsbellMitchell1976` | Isbell, John and Mitchell, Barry, *Exact Colimits and Fixed Points* (1976) | Opened: complete attached primary scan; Proposition 1.1, Lemmas 2.1--2.2, Proposition 2.3, Theorem 3.1, Lemma 3.2, Proposition 3.3, Theorem 4.1, Corollaries 4.2--4.4, Proposition 4.5, Corollary 4.6, and added-in-proof paragraph inspected. |
| `FAOberst1968` | Oberst, Ulrich, *Homology of Categories and Exactness of Direct Limits* (1968) [primary route](https://link.springer.com/article/10.1007/BF01111023) | Body not obtained: publisher record opened; PDF endpoint redirects to subscription record; exact-title and author searches tried. No mathematical-content claim or theorem number asserted. |
| `FAAdamekKoubekReiterman1981` | Adamek, Ji\v ri and Koubek, Vaclav and Reiterman, Jan, *Embeddings into Categories with Fixed Points in Representations* (1981) [primary route](https://dml.cz/handle/10338.dmlcz/101753) | Not opened: body not obtained in an inspectable form in this run. DML-CZ and EuDML records opened; PDF reader returned cover text only; canonical and public alternate download routes failed with HTTP 503 or access/timeout errors. No original theorem number or content claim is asserted. Repaired construction is audited from the attached TOTAL_EXACT_2 source instead. |
| `FAAdamekReiterman1976` | Adamek, Ji\v ri and Reiterman, Jan, *Exactness of the Set-Valued Colim* (1976) [primary route](https://dml.cz/bitstream/handle/10338.dmlcz/105677/CommentatMathUnivCarol_017-1976-1_8.pdf) | Opened: complete primary mathematical text through indexed DML-CZ PDF; I.2, I.4, II.2, II.3, III.1--III.2, IV.1--IV.2 inspected. The printed equivalence in II.3 is not used. Direct PDF download was unavailable. |
| `FACisinski1999` | Cisinski, Denis-Charles, *La classe des morphismes de Dwyer n'est pas stable par retractes* (1999) [primary route](https://www.numdam.org/item/CTGDC_1999__40_3_227_0.pdf) | Opened: complete primary Numdam PDF; Lemma 1 and finite counterexample pp. 228--229, Lemmas 2--4 and Propositions 1--2 pp. 230--231 inspected. |
| `FDwyerKan1980` | Dwyer, William G. and Kan, Daniel M., *Calculating simplicial localizations* (1980) [primary route](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/dwyer-kan-2.pdf) | Opened: primary scan, Proposition 2.2; Propositions 3.1, 3.5 and Corollary 3.6; Section 4, especially Propositions 4.2--4.5; definitions and Propositions 5.1--5.5; Section 6's fraction conditions. The fixed-type/all-type distinction is preserved. |
| `FChacholskiScherer2001` | Chacholski, Wojciech and Scherer, Jerome, *Homotopy theory of diagrams* (2001) [primary route](https://arxiv.org/pdf/math/0110316) | Opened: attached source and primary PDF; Chapter 3, Theorem 24.9 (Fubini), Theorem 26.8 and Corollary 26.9 (Grothendieck construction), Theorem 30.5 (cofinality), at the statements and proof steps used. |
| `FCharney2006` | Charney, Ruth, *An introduction to right-angled Artin groups* (2006) [primary route](https://arxiv.org/pdf/math/0610668) | Opened: attached source and primary PDF, Sections 2.6--2.7, Theorem 2.6 and the link/Salvetti argument. Context for the already established RAAG detector; not imported as a free-monoid theorem. |
| `FHackneyEtAl2022` | Hackney, Philip and Ozornova, Viktoriya and Riehl, Emily and Rovelli, Martina, *Pushouts of Dwyer maps are $(∞,1)$-categorical* (2022) [primary route](https://arxiv.org/pdf/2205.02353) | Opened: attached source and primary PDF, Definition 3.4 (discretely flat), Proposition 3.3, Example 3.5, Proposition 3.6 and Theorem 1.5. Used to keep the sieve terminology distinct. |
| `FGraySteinberg2018` | Gray, Robert D. and Steinberg, Benjamin, *Topological finiteness properties of monoids, Part 2* (2018) [primary route](https://arxiv.org/abs/1805.03413) | Opened: attached primary TeX and arXiv v3 PDF; Theorems 4.5, 4.8, 4.10 (source labels t:bass.serre.free, t:amalg.cd, t:bass.serre.flat), and Remark 4.11's explicit counterexample to Fiedorowicz Lemma 5.2(a). No arbitrary-diagram flatness is assumed. |
| `FNicholson2019` | Nicholson, John, *On CW-complexes over groups with periodic cohomology* (2019) [primary route](https://arxiv.org/abs/1905.12018) | Opened: attached revised primary TeX, Introduction, Theorem A and Corollaries B--C. Comparison context for the dimension-two boundary; not used to identify all superperfect groups with groups of finite acyclic two-complexes. |
| `FHigman1951` | Higman, Graham, *A finitely generated infinite simple group* (1951) [primary route](https://academic.oup.com/jlms/article-abstract/s1-26/1/61/966631) | Not opened: original mathematical body not obtained. Exact-title primary search, OUP record, and Wiley DOI/PDF endpoint tried; records only. No assertion about the paper's mathematical content is used. |
| `FCisinskiMO2026` | Cisinski, Denis-Charles, *Answer concerning Proposition 4.3.2 of Asterisque 308* (2026) [primary route](https://mathoverflow.net/questions/516223/) | Opened: primary author answer dated 21 October 2026 to the question on A=BG. Confirms that (g) implies (c) needs an extra hypothesis. The disputed implication is not used anywhere in this paper. |
| `FPRETOT` | GPT-6 Astra (OpenAI, ChatGPT Pro mode), *PRETOT: attached mathematical return* (2026) | Opened: A.1--A.5, B.2--B.4, C.1--C.4, E.1--E.9, F.1--F.16 and the specifically used auxiliary passages. Each dependency is rederived at its point of use or in the attached audit notes. AI-produced; the original free-degeneracy hypothesis in A.4 is retained. |
| `FPRETOTReview` | Claude Opus 5.5 (Anthropic, effort max), *PRETOT review and findings* (2026) | Opened: attached review, its audit of A.1--A.5 and path/totality results, and findings F12, F13, F15--F19. F13 suggests the general act method, rather than asserting the false nondegenerate-simplex functor of Lead 4(a). No review is treated as a proof substitute. |
| `FTOTASPH` | AI-produced return; attribution as recorded in the supplied package, *TOTASPH: attached Parts C, D, F and follow-ups* (2026) | Opened: C.4--C.13, D.2, D.12--D.13 and D.19, and F.9 at the precise steps used. The affine contraction, action-cover argument, totality criteria and sieve-composition reduction were followed and are audited in the present proof notes. |
| `FTOTASPHReview` | Claude Fable 5.2 (Anthropic, effort max), *TOTASPH: attached expert review* (2026) | Opened: cited C/D/F findings and source corrections. Used as an audit guide; mathematical dependencies are checked against the supplied proofs. |
| `FTOTEX` | AI-produced return; attribution as recorded in the supplied package, *TOTEX: attached mathematical return* (2026) | Opened: the used affine/action criteria; D.4--D.10 and D.21--D.26; E.1--E.6, especially the colored-word affine lifting in E.2. Dependencies are audited in A, C, D and F and the source notes. |
| `FTOTEXReview` | Claude Opus 5.5 (Anthropic, effort max), *TOTEX: attached review* (2026) | Opened: the cited checks and literature corrections. Not used in place of the proof in the return. |
| `FPATHS` | AI-produced return; attribution as recorded in the supplied package, *PATHS: attached mathematical return* (2026) | Opened: A.2--A.4 and C.P1--C.P4, including the type hom-poset contraction, strict action, coherent descent, and finality comparisons. The used steps are rechecked in B.1, B.3 and B.9. |
| `FPATHSReview` | Claude Fable 5.2 (Anthropic, effort high), *PATHS: attached intake and findings F1--F3* (2026) | Opened: review and the supplied second reading of F2 at the path-comparison steps. Proofs in PATHS and INDLOCAL are checked separately. |
| `FTOTEX2` | GPT-6 Astra (OpenAI, ChatGPT Pro mode), *TOTAL_EXACT_2: attached final return* (2026) | Opened: C.10 and C.19--C.28, C.32--C.37, C.40 (FT:ty); A.21, A.24, A.30--A.34 and the nonexactness calculation; the free-factor and finite-projective-dimension notes. The repaired AKR survivor and the all-action C-delta reduction are audited explicitly. AI-produced, previously unrefereed except for the identified supplied readings. |
| `FTOTEX2Review` | Claude Fable 5.2 (Anthropic, effort max), *Referee reading of the main proofs of TOTAL_EXACT_2* (2026) | Opened: attached REVIEW_MAIN_PROOFS_TOTEX2.md, including the expanded actual-arrow routing argument in Section 4 for C.27. Checked against the proof, without replacing actual arrows by component maps. |
| `FINDLOCAL` | GPT-6 Astra (OpenAI, ChatGPT Pro mode), *INDLOCAL: attached return, Part C* (2026) | Opened: C.2--C.9, C.11, C.21, C.23 and the relative/crown comparisons at the used steps. B.1 audits the required C.21 and C.23; C.6 audits C.7's all-arrows-marked mapping-space theorem. AI-produced. |
| `FLeads` | Claude Fable 5.2 (Anthropic), *DER_FOLLOWUP: lead derivations and drafter's checks* (2026) | Opened: attached LEADS_DERIVATIONS.md, Leads 1, 2, 3 and 5; the walking-retraction program and output. All six prompt Leads are independently proved or refuted in the present paper. |
| `FOpenAI317` | OpenAI, AI-produced; model and effort unspecified in the attachment, *317: attached manuscript on Thomason model structures* (2026) | Opened: foundations section and Section 7, equation eq:model-classes. Only the dimension-two weak-equivalence convention is used, verified against Ara--Maltsiniotis Theorem 6.27 and the Street-nerve convention. No Lean certificate was executed here. |
| `FREVLOCH` | GPT-6 Astra (OpenAI, ChatGPT Pro mode), *REVERSIBLE_LOCALIZERS, checkpoint 17: Parts H and H5* (2026) | Opened: attached H14.tex, H.2--H.4, and H5.tex, H5.6--H5.8. The represented-derivator detection, double-coset test and variance of the projector construction are checked in C.7--C.8 and the independent audit. |
| `FS2COUNT` | GPT-6 Astra (OpenAI, ChatGPT Pro mode), *S2COUNT: attached results register* (2026) | Opened: attached CSV register, including CD:boundedtests, E:A19, E:A20 and B:main. Proof bodies were not supplied. None of these results is a mathematical dependency of the present paper. |
| `FDERII` | Grothendieck, Alexander, *Les Derivateurs, Chapter II* | Opened: attached transcription at manuscript 36 ter and surrounding conventions. The Kunzer--Malgoire--Maltsiniotis edition is the authority; F.1 gives the corrected hierarchy. |
| `FDERVII` | Grothendieck, Alexander, *Les Derivateurs, Chapter VII* | Opened: attached transcriptions, manuscript 25--32, 90--115, especially 99--103, 109--110, 112--114. The hypothesis at 99 is equality up to homotopy, not coherent descent. Edition notes are credited where used. |
| `FDERXII` | Grothendieck, Alexander, *Les Derivateurs, Chapter XII* | Opened: attached transcription, manuscript 88--89, 93--97, 101--103, 109--114. Definitions, Proposition 8, the endpoint questions, and the composition question are checked at their literal scope. |
| `FEdition` | Kunzer, Matthias and Malgoire, Jean and Maltsiniotis, Georges, *Edition of Grothendieck's Les Derivateurs* [primary route](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html) | Opened: edition landing page and the edition's notes preserved in the supplied chapter transcriptions. The note at XV manuscript 133 bis reverses the affirmative implication directions; G.6 verifies the correction. No new statement here is attributed to the editors. |
| `FPOLES` | AI-produced source mentioned in the prompt, *POLES: unavailable earlier return* (2026) | Not opened: this body is not among the attached files. The supplied manifest and available paths were checked; no mathematical conclusion is imported from it. |
| `FFREX` | AI-produced source mentioned in the prompt, *FRAISSE_EXACT: unavailable related return* (2026) | Not opened: no FREX return is among the attached files. The manifest and available paths were checked. The all-action realization used here is proved independently in A.3--A.7 and A.13. |
| `FINDLOCALIntake` | Claude Fable 5.2 (Anthropic, effort high), *INDLOCAL: intake mentioned in the prompt* (2026) | Not opened: its separate body is not attached. The actual INDLOCAL Part C proof sources are attached and were read instead. |
| `FDERXIIApp` | Grothendieck, Alexander, *Les Derivateurs, Chapter XII appendix* | Not opened: the appendix body cited by R15 is not in the attached Chapter XII excerpt. The manifest and excerpt limits were checked. Its footnote is not used as a mathematical input here. |
| `FR19Hua104` | Hua, Michel and contributors, *Folder104.lean: Categories of Models and Well-Founded Directness* (2026) [primary route](https://github.com/Commutator-IO/grothendieck-project/blob/08e7d549678e7434e4d21d95a2cefa8e74fd2acf/lean/Grothendieck/Folder104.lean) | Opened: commit 08e7d549678e7434e4d21d95a2cefa8e74fd2acf; declarations reedyDirecte, wf_of_degre, entiers_relatifs_non_directe, and deltaInjReedy. Source and relevant proof dependency inspected 17 November 2026; no local Lean execution claimed |
| `FR19Hua106` | Hua, Michel and contributors, *Folder106.lean: Cofibration Categories, Brown Factorization, and Rectified Spans* (2026) [primary route](https://github.com/Commutator-IO/grothendieck-project/blob/08e7d549678e7434e4d21d95a2cefa8e74fd2acf/lean/Grothendieck/Folder106.lean) | Opened: commit 08e7d549678e7434e4d21d95a2cefa8e74fd2acf; namespace Grothendieck.Folder106.CategorieACofibrations, declarations qFunctor_iso, fidele, plein, and critere. Complete source inspected 17 November 2026; no local Lean execution claimed |
| `FR19HuaReedy` | Hua, Michel, *SemiSimplexCategoryReedy.lean: Local Direct-Category Proofs* (2026) [primary route](https://github.com/Commutator-IO/grothendieck-project/blob/08e7d549678e7434e4d21d95a2cefa8e74fd2acf/lean/Grothendieck/Upstream/SemiSimplexCategoryReedy.lean) | Opened: commit 08e7d549678e7434e4d21d95a2cefa8e74fd2acf; inspected proof of HomotopicalAlgebra.ReedyStructure.ofWellFounded and wellFounded. These local declarations are not evidence that Mathlib PR 44731 was merged |
| `FR19HuaPR44731` | Hua, Michel, *Direct Categories via Well-Foundedness* (2026) [primary route](https://github.com/leanprover-community/mathlib4/pull/44731) | Opened: metadata and proposed source. PR opened and closed unmerged on 11 October 2026; proposed commit a38dc275ef15bfa207bd9cb3ac0f18fce7725c7c. Public metadata, review comments, reported post-build declaration audit, and proposed Direct.lean inspected 17 November 2026 |
| `FR19ProjectProvenance` | Hua, Michel and contributors, *Grothendieck Project: Readme, Lean Appendix, and Build Provenance* (2026) [primary route](https://github.com/Commutator-IO/grothendieck-project/tree/08e7d549678e7434e4d21d95a2cefa8e74fd2acf) | Opened: commit 08e7d549678e7434e4d21d95a2cefa8e74fd2acf. README, RIGHTS, LICENSE, Lean README, toolchain, Lake configuration, and CI workflow inspected 17 November 2026. Configuration records Lean 4.35.0-rc4 and Mathlib commit 715a03a90adf491de40fbec8b456c179a623435f |
| `DALawsonWallis2015` | Lawson, Mark V. and Wallis, Alistair R., *A Correspondence between a Class of Monoids and Self-Similar Group Actions II* (2015) [primary route](https://pure.hw.ac.uk/ws/portalfiles/portal/10624800/SS2.pdf) | Primary author-repository PDF opened 17 November 2026. Section 2, Theorem 2.3, Lemma 2.7, Proposition 2.8, and Remark 2.10 inspected. Levi monoids here require a natural-number-valued length with zero fiber the units; this hypothesis does not follow for a filtered colimit of free monoids. Attempt source only, not a proof of the unresolved free-monoid comparison |
| `DABataninDeLeger2019` | Batanin, Michael A. and De Leger, Florian, *Polynomial Monads and Delooping of Mapping Spaces* (2019) [primary route](https://arxiv.org/pdf/1712.00904) | ArXiv version 4 opened 17 November 2026; publisher metadata gives online publication 21 January 2020. Theorems 6.10 and 6.12, Example 7.1, Proposition 7.4, and Remark 7.5 inspected. Classifier contractibility is a comparison criterion, but no implication from totality of the indexing category was obtained; the flatness hypothesis in Example 7.1 was not verified for the present diagrams. Attempt source only |
| `DAHandelman1987` | Handelman, David, *Eventually Positive Matrices with Rational Eigenvectors* (1987) [primary route](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/eventually-positive-matrices-with-rational-eigenvectors/6F27ACDF45B860FC33C27F3A81ADE878) | Body not obtained; publisher abstract and metadata opened 17 November 2026. Context for eventual positivity under integral changes of basis. The rank-two irrational stabilization in the working notes has its own elementary proof and does not invoke an uninspected theorem from this paper |
| `DADinowitzEtAl2025` | Dinowitz, Emma and Koch-Hyde, Lucy and O'Connor, Siobhan and Olive, Eamonn, *Growth and Language Complexity of Potentially Positive Elements in Free Groups* (2025) [primary route](https://arxiv.org/html/2512.13967v1) | Version 1, 16 December 2025; primary HTML introduction and relevant potential-positivity discussion opened 17 November 2026. Context only: no theorem from this source is used to infer a positive basis or a strict free-monoid diagram over the predimension category |
| `DAShpilrainProblems` | Shpilrain, Vladimir, *Free Groups: Problem F34 and Its Background* [primary route](https://shpilrain.ccny.cuny.edu/gworld/problems/probfree.html) | Problem F34 and its linked background at https://shpilrain.ccny.cuny.edu/gworld/problems/Back.html opened 17 November 2026. This is a discovery source for potential and stable potential positivity; the theorem it attributes to Clark--Goldstein is not used as an independently audited proof |
| `DAClarkGoldstein2005` | Clark, Aaron and Goldstein, Richard, *Stability of Numerical Invariants in Free Groups* (2005) [primary route](https://www.tandfonline.com/doi/abs/10.1080/00927870500261405) | Body not obtained; exact-title and author PDF searches on 17 November 2026 located the publisher contents record and citations in the opened author problem-list background and arXiv:2512.13967. No theorem from the uninspected original is used in the present argument |
| `DAOConnor2026` | O'Connor, Siobhan B., *Algorithmic Problems in Automorphic Orbits of Free Groups* (2026) [primary route](https://academicworks.cuny.edu/gc_etds/6698/) | Body not obtained; official dissertation landing page and abstract opened 17 November 2026. Its linked viewcontent.cgi PDF returned HTTP 403. No statement beyond the landing-page metadata and abstract is attributed to this dissertation |
| `DABertheEtAl2015` | Berthe, Valerie and De Felice, Clelia and Dolce, Francesco and Leroy, Julien and Perrin, Dominique and Reutenauer, Christophe and Rindone, Giuseppina, *Acyclic, connected and tree sets* (2015) [primary route](https://arxiv.org/pdf/1308.4260) | Opened primary arXiv v6 full text; read Sections 2.2--2.3, especially Propositions 2.5 and 2.7 on reversible automata and saturated positive submonoids, and the statements and scope of Theorems 5.1--5.2 in Section 5.1. Relevant terminology for the independently proved saturated-chart obstruction; no general amalgamation theorem or C-delta comparison conclusion is taken from this source. The initial Luxembourg PDF attempt timed out; the arXiv PDF opened successfully. |
| `DABodirskyBodorMarimon2025` | Bodirsky, Manuel and Bodor, Bertalan and Marimon, Paolo, *Taking model-complete cores* (2025) [primary route](https://fis.tu-dresden.de/portal/files/81089088/2512.21278v1.pdf) | Opened primary v1 PDF: Lemmas 4.34--4.35 and their full proofs, printed pages 33--35, concerning signed lexicographic classification of definable orders on increasing rational tuples. Closest-source context for the invariant-cut-order attempt, not a theorem about C-delta or monoid comparisons. The arXiv PDF direct open was disabled; the institutional PDF opened successfully. |
| `ChuangHolsteinLazarev2021` | Joe Chuang and Julian Holstein and Andrey Lazarev, *Homotopy theory of monoids and derived localization* (2021) [primary route](https://arxiv.org/pdf/1810.00373) | Opened: primary arXiv v3, 29 September 2021; Section 2.3--2.5 definitions, Proposition 4.1, Corollary 5.1 and Theorem 5.2 with its proof inspected in the C-delta attempt. The equivalence of relative categories does not identify an ordinary colimit with the specified homotopy colimit. No missing comparison theorem is inferred from it. |
| `Bergner2007Monoids` | Julia E. Bergner, *Simplicial monoids and Segal categories* (2007) [primary route](https://math.ucr.edu/~jbergner/SimpMonSubmit.pdf) | Opened: primary author PDF; Definitions 1.1--1.5, Proposition 4.2, Lemma 4.6, Proposition 4.7 and the accompanying homotopy-colimit discussion inspected. The later 2008 correction was also opened; the uncorrected Proposition 3.12 is not used. This source does not settle the C-delta comparison. |
| `Bergner2008Correction` | Julia E. Bergner, *Correction to ``Simplicial monoids and Segal categories''* (2008) [primary route](https://arxiv.org/pdf/0806.1767) | Opened in full: the three-page correction, Propositions 1--2 and 5--6, Definition 3 and Lemma 4. The original proposed adjoint pair did not preserve coproducts; the corrected rigidification adjunction is not treated as a theorem on arbitrary ordinary colimits of free monoids. |
| `PanovRayVogt2002` | Taras Panov and Nigel Ray and Rainer Vogt, *Colimits, Stanley--Reisner algebras, and loop spaces* (2002) [primary route](https://arxiv.org/pdf/math/0202081) | Opened: primary arXiv v1, Propositions 7.10--7.11, Theorem 7.12 and its proof, and Propositions 7.14--7.15 with their proofs. Theorem 7.12 compares the classifying space of a homotopy colimit of well-pointed topological monoids with the based homotopy colimit of their classifying spaces. Proposition 7.15 gives a comparison square with ordinary colimits; it does not assert that its lower map is an equivalence. Published in Progress in Mathematics 215 (2004), pp. 261--291. |
| `DGHolub2003` | Holub, \v St\v epan, *Binary equality sets are generated by two words* (2003) [primary route](https://www.karlin.mff.cuni.cz/~holub/soubory/freshidea.pdf) | Opened: revised author version, Section 3, Lemma 3; the nonerasing hypothesis is explicit in this corrected version |
| `DGCastiglioneFiciRestivo2019` | Castiglione, Giuseppa and Fici, Gabriele and Restivo, Antonio, *On Sets of Words of Rank Two* (2019) [primary route](https://arxiv.org/html/1810.02182v2) | Opened: version 2, 7 June 2019; Section 2, Theorems 2.1 and 2.2, and the preceding free-intersection/free-hull statement inspected |
| `DGCarpiDAlessandro2014` | Carpi, Arturo and D'Alessandro, Flavio, *\v Cerny-like problems for finite sets of words* (2014) [primary route](https://ceur-ws.org/Vol-1231/proceedings.pdf) | Opened: Theorem 1, p.84, the stability characterization of free submonoids |
| `DGBerstelKarhumaki2003Unread` | Berstel, Jean and Karhumaki, Juhani, *Combinatorics on Words---A Tutorial* (2003) [primary route](https://www-igm.univ-mlv.fr/~berstel/Articles/2003TutorialCoWdec03.pdf) | Not opened: search-located author revision of the Bulletin EATCS 79 article. Two PDF opens failed, with timeout and HTTP 502. Retained solely in the attempt ledger, not a proof citation |
| `DGBataninBerger2017` | Batanin, Michael A. and Berger, Clemens, *Homotopy theory for algebras over polynomial monads* (2017) [primary route](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/batanin-berger.pdf) | Opened: primary paper in an institutional mirror, Theorems 5.14--5.15, Remark 5.16, Theorem 8.2 with proof, Remark 8.3, and Corollary 8.4. Used only in the investigation ledger, not to assert the unresolved total-index comparison |

## Search ledgers by requested problem

| Prompt item | Exact-query and source-audit record |
|---|---|
| A.3 | `notes/A_sources.md`; historical checks in `notes/F_A_source_ledger.md`. Cocycle Fraïssé structures, all-action realization, higher homotopy of theories, and open-stabilizer support were searched. |
| B.2 | `notes/BE_sources.md`, `notes/B_interval_sources.md`, and `notes/F_B_general_source_ledger.md`. Searched homotopy colimits over colored words, cofinal sequences, type descent, and fixed-type/all-type hammocks. |
| C.2 | `notes/CD_sources.md`. Searched strict asphericity of path endpoints, Evrard replacements, and ordinary versus strict path-fibration tests. |
| D.1 | `notes/CD_sources.md` and the C-delta attempt logs. Searched free-monoid colimits over exact or semicosimplicial indices, classifying spaces, amalgams, and positive-word diagrams. |
| E.2 | `notes/BE_sources.md`; independent proof audit in `notes/E_independent_audit.md`. Searched superperfect groups, acyclic complexes in dimensions two and three, truncated simplicial acts, and Kervaire. |
| G.1 and G.2 | `notes/G_sources.md`. Searched weak basic localizers, finite products, homotopy Kan adjoints, and the exact Cisinski theorem chain. |
| G.4 | `notes/G_sources.md`. Searched localization and infinite products, calculus of fractions, and Zhang's exact 2026 title; unavailable full text is recorded without theorem-level claims. |

The bibliography distinguishes repeated editions or separately audited parts. A citation here is not a claim of formal verification: the present independent programs and the externally reported Lean checks are identified separately.

## Typesetting and visual inspection

The first G standalone build had one 50.8849pt overflow from an unbreakable Mathlib module name; the first combined check had one 62.95pt overflow from a bibliography URL. Both were corrected in source with break opportunities. These are **two distinct initial defects**; repeated appearances in intermediate logs are not counted as new defects.

The current master build, `20261117T041116.166781Z`, has 74 pages, 0 overfull boxes, 0 boxes over 2pt, and 0 recorded warnings. All 4 compilation commands returned zero. Full logs and exact commands are retained in `build/master_runs/20261117T041116.166781Z`.

The visual review covers 37 pages: current master pages 1, 3, 8, 13, 18, 23, 28, 34, 39, 42–52, 56, 60, 64, 68, and 71–74; G standalone pages 1, 7, 11, 13, 14; and the earlier combined check pages 1, 30, 55, 59. The current 28-page master sample includes every page of D.8–D.10. Changed pages were viewed after the 04:11 rebuild; unchanged page images retain the preceding actual review. New proof page49 was additionally viewed at full rendered size, as were D.8–D.9 pages45 and47 in their preceding identical renders. The formerly overflowing module-name and bibliography-URL passages are now on master pages68 and73 and were included. The nine historical sample images are byte-identical to their previously reviewed renders. No clipping, overlap or visual overflow was observed. Page images, contact sheets, exact PDF hashes and the review record are retained in `build/visual_qa/` and `code/outputs/pdf_visual_qa.json`. External primary-source PDFs and the bundled TeX manual are immutable source/runtime evidence, not newly typeset papers.

## Checkpoints and preservation

Session start: **2026-11-17 01:14:17 UTC**. Hourly checkpoint archives use new names and are never overwritten, renamed or removed. Attached inputs are excluded. The final/current work directory contains the source files, report, register, bibliography, all proof notes, exact programs and outputs, source-access records, and build logs.

The preservation audit checks 759 entries from 2 prior checkpoint archive(s). 94 superseded versions are retained byte for byte under `history/`; unchanged files remain at their active paths. **No prior file is intentionally omitted.** The complete per-file source, retained path, SHA-256 and supersession reason are in `history/preservation_manifest.csv`. Older drafts are historical records; the master paper and current report give the current mathematical claims.

## Requested progress assessments

### Three-hour assessment, 17 November 2026, 04:13 UTC

**Decision: continue.** The last hour has advanced the remaining main
question, rather than only improving exposition or source metadata.

- D.8 proves passage when the Fraïssé filtered-limit monoid is free,
  excluding every proposed first-return kernel construction.
- D.9 reduces the universal question to finite-rank diagrams with
  injective word substitutions, with both canonical comparison maps proved.
- D.10 proves passage under an invariant positive length and proves a
  global obstruction to the based positive-matrix lifting route. The
  support-filtration proof has received independent audits.
- The signed-lexicographic cut-order argument and its cross-orbit extension
  give structural information about the remaining moving-cut case. Their
  missing connection to the global monoid comparison is stated explicitly.

The unrestricted C_delta FreeMon comparison is still unresolved. The
continuation is justified by these proved restrictions and the active
cut-space argument, not by treating the conditional results as a complete
answer. The next requested progress assessment is at about 05:14 UTC.

