INCOMPLETE

# REVLOC research report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15–16 November 2026. No priority is claimed. This is an active research checkpoint, not a completed return.

## Main result reached

Parts A and B establish, in ZFC, an accessible reversible fundamental localizer that is not of the form `R(L)`. The proof treats the bounded-subcomplex construction, its homotopy-colimit and three cofiber cases, and the explicit alternating enlargement needed for desuspension. A stronger consequence is proved: the smallest reversible fundamental localizer containing any small set of maps is accessible. In particular the reversible closure of `BZ/2 -> *` is accessible and not `RT`-fixed.

The sphere-null construction and its odd-prime repair have been derived from opened primary sources, including the space-level Kahn–Priddy section. No infinite-loop section is assumed. The stable identity `loc(Sigma^infty BZ/p) = loc(S/p)` is proved at every prime. A further compactness argument now proves that the **full sphere-null localizer itself is accessible in ZFC**, by identifying its null class with its countably bounded subclass (G.6–G.7).

## Item-by-item status at this checkpoint

“Open” below means the requested item is still being attacked; a proved partial result does not complete it. Exact numbered statements are in `REVLOC_results.csv` and the corresponding manuscript sections.

| Requested item | State reached | Remaining obligation / next attack |
|---|---|---|
| A.1–A.3 | Proved: EHP desuspension including dimension two; retracts, relative Theorem A and cofiber criterion; stable projective-space identity. | Final source and layout verification. |
| A.4 | Proved after replacing the even-sphere odd-prime lead by Toda's odd spheres and truncated James constructions. | Final cross-check of all-prime statement. |
| B | Proved: accessible reversible nonstable example; small reversible closures are accessible. Independently checked by two parallel readers. | Final adversarial check of cardinal bookkeeping. |
| C, class and listed aspherical spaces | Proved: exact closure description; all listed tests decided, including `Q(Sigma^m RP2)`. | None for these tests. |
| C, local objects | Proved: every localized or completed simply connected finite target is local (C.8–C.9). The connected finite-pi1 bounded-cohomology assertion is refuted by the finite acyclic binary-icosahedral complex. | Completed finite-target locality uses a convergent loop–suspension resolution, after a separate loop-target argument. |
| D, proposed classification | Refuted as worded: acyclic nullification has a desuspension-closed null class but is not reversible. | The obstruction is the failure of object nullity to determine map locality; D.0 supplies an explicit homology-equivalence counterexample. |
| D.1 | Complete: integral and localized spheres fail; `K(G,1)` works only for trivial `G`; `BU` works; a finite H-space works exactly when it is weakly contractible. Among the usual prime Moore targets `M(Z/p,n)`, with `n >= 1`, the single-target null class is desuspension-closed exactly when `(p,n) != (2,1)`. | D.1.7 proves the simply connected odd-primary case. D.1.8 supplies a geometric mod-2 Lie-telescope retraction and an exact finite certificate. D.1.9 handles cyclic fundamental groups and gives the explicit RP2 counterexample. Independent review passed. |
| D.2 | Every thick finite subcategory occurs. Every nonzero torsion thick subcategory and the full finite category have accessible non-RT-fixed realizations. D.2.7 gives exact bounded-suspension ordinary-nullification tests; D.2.8 proves finite primary generators are RT-fixed; D.2.9 constructs a descending chain with common nonzero stable part and zero finite part, and computes its adjacent ordinary nullifications. D.2.10 excludes finite simply connected separating targets. D.2.11 excludes every realized unstable K(2)-local target, using countable colimit generation by trivial periodic Lie algebras. D.2.12 obstructs an unstable retraction of the suspended stabilization unit at p=2 for every positive suspension index and proves that the first three mod-two homology groups survive the first simultaneous nullification cone attachment. | **Open:** zero finite thick part with nonfixedness. For `B = K(Fp,2)` and `A1 = Q Sigma B`, the concrete remaining test is whether `P_A1(Sigma^2 B)` is noncontractible. No strictness of the descending chain is asserted. The retraction obstruction alone does not determine successive nullification attachments. Rational stable parts cannot provide a separator. D.2.37 proves the primary GEM tensor collapse, and D.2.39 strengthens it: for every C already in Rev(BZ/p), smashing C with BZ/p leaves Rev(C) unchanged. Thus no such tensor factor supplies the proposed separator. D.2.17--D.2.20 construct the dangerous pattern through dimension nine, and D.2.24 now proves that no map with that pattern extends through the unit ten-skeleton. D.2.21--D.2.23 compute the exact target and separately extend the canonical summand through relative dimension ten. D.2.26 gives the exact simultaneous-cone criterion, and D.2.27 proves uniform vanishing with one common normalization for every mixture of suspension exponents 0,2,3 and at least5. D.2.28 reduces exponent1 to the single product coefficient alpha3 beta4, and D.2.30 realizes it by an actual ordinary map through the ten-skeleton. D.2.31 determines the actual target group as (Z/2)^4, and D.2.32 proves that every ten-cell filling of one explicitly fixed nine-stage map fails at the eleven-skeleton. D.2.33 now treats every full ordinary exponent1 map: its quadratic eleven-stage test exists by a limited target stabilization, the nonzero bottom-six branch is excluded, and every remaining lower choice forces the singleton bracket <lambda,eta,2> to equal p and forces the nonreference Moore top. D.2.34 now computes that exact bracket as zero by an actual lower cone and Hurewicz-injectivity argument. Thus every full ordinary exponent1 map has zero normalized functional, and the simultaneous first-cone result holds for every mixture of all exponents except4. D.2.29 realizes a dangerous exponent4 map on the entire unit but obstructs extension of its fixed canonical C4 choice to C6. D.2.36 now excludes the second bottom Moore pattern for every entire unit map, by nine explicit Steenrod identities through source degree20. Every full exponent4 map is zero on degree-eight linear homology, leaving only the pure commutator pattern. D.2.38 now determines the finite relative source group as (Z/4)^2 plus Z/2 and proves exact order four for every sphere representing its specified Browder boundary. D.2.41 identifies the actual sphere as the Stiefel attaching map up to sign and forces its relative full-extension image to be a double, weakening the sufficient connected-cover operation test. D.2.40 identifies the exact target five-type and proves that the paired functional does not descend from it, eliminating pure Postnikov descent as a shortcut. D.2.42 now constructs its actual secondary class on the connected cover, proves the restriction is nonzero, and refutes the proposed odd-operation criterion. D.2.43 computes the exact quadratic map and reduces the target composite h_M l4 to whether 2c lies in the stable James–Hopf image. It proves exact order four through the target eleven-skeleton. D.2.44 reduces the actual universal composite to two bottom-sphere components and shows why suspension does not separate them. D.2.46 now chooses a bottom remainder before passing to the Moore target; its sphere suspension is zero, reducing the composite to one cyclic generator q with4q=0 and2h=2q. Their actual values are determined later in D.2.61. D.2.45 strengthens nonvanishing through every target skeleton of dimension fourteen: transfer has kernel <4c>, so a target with H15=0 cannot kill the boundary of2c. Only the actual fifteen-cells can first kill it; the full question is determined on that skeleton. The necessary mod-four pairing is the pairing of a half-product class theta on stable integral Hurewicz classes, with beta_Z(theta)=x8 squared. D.2.47 now computes the actual six-type fiber, its integral group H^8(H;Z)=Z/4, the restriction b8|H=2z8, and the nonzero mixed differential d5(z8)=Sq1(U4) tensor V4. D.2.48 determines the full degree-eight filtration: 2b8 has exact filtration four with associated class U4 tensor V4, while the degree-eight base pullback is zero. D.2.49 now proves the actual lifted universal composite has zero integral loop Hurewicz image and therefore kills the intrinsic doubled integral commutator. D.2.50 converts that exact chain nullhomotopy into an integral fifteen-cycle with mod-four cup coefficient two. The integral square b8 squared is consequently nonzero of exact order two, and the half-product detects a torsion integral homology class of order at least four. D.2.51 now removes the independent quadratic coordinate and proves an exact existential equivalence: the homotopy composite vanishes if and only if theta detects a stable integral Hurewicz class. The possible James--Hopf images give exactly the three remaining orders four, two and one. D.2.52 constructs an actual finite-cone integral detecting cycle whose mod-two reduction is annihilated by every positive Steenrod operation; hence theta is not in the entire positive-operation image. D.2.53 now proves the actual epsilon-prime target term zero by selecting the compatible Toda factor and evaluating its entire suspended bracket as the singleton zero. Thus the sole remaining target generator is alpha sigma-prime. D.2.54 proves that a chosen detecting cycle survives all stable AHSS differentials before d8, whose value is2n times the bottom generator in a quotient of Z4. Only incoming d5,d6,d7 can change that quotient; the potential d2 is zero by comparison with the connective image-of-J spectrum. The exact existence criterion also allows changing the detecting cycle by the theta-zero subgroup. D.2.55 now proves the incoming d5 zero by controlling every actual twelve-cell nu composite, including the doubled N-lift and the even Q-coordinate correction; the full bottom Z4 injects through that stage. Only incoming d6 and d7 remain. D.2.56 extends the actual cover edge quotient through degree12 and computes H13(L;F2) and H14(L;F2) as explicit double-suspension quotients of dimensions17 and25. The two reversed loop-space products supply essential Browder relations in degree14. D.2.57 now completes that test: the actual four-class cyclic submodule, an explicit thirteen-column cobar certificate, and finite-skeleton Adams permanence prove both incoming d6 and d7 zero. The final stable AHSS target is exactly Z4. Only the specified d8 and its theta-zero source-changing image remain in the exact criterion. D.2.58 extends the bottom Adams nonboundary to the full space: Sq2 Z13=Sq1 ell14 and one additional functional term cancel every degree15 cobar column. D.2.59 computes H15(L;F2) with dimension33 and its seven-dimensional primary-annihilator space, proves integral lifts of all seven classes, and fixes the half-product values as1,1,0,0,0,0,0 by six explicit integral double suspensions. D.2.60 independently proves that the actual auxiliary James--Hopf bottom sigma-prime survives every cell through dimension12 with exact order two; its cells in dimensions13--15 are not evaluated. D.2.61 now settles the actual remaining Adams comparison: a controlled universal secondary operation has zero pairing on every possible primary source, and an explicit coherent bar/GEM track proof identifies this pairing with Adams d2. The bottom h0h3 is permanent. Its nonzero stable double forces the whole bottom Z4 to survive, so the last stable AHSS d8 is zero. The detecting integral class is stably spherical; the actual composite h_Ml4 is zero, while alpha sigma-prime has exact order two. Thus this specific Moore obstruction cannot exclude a full extension. The next finite test concerns a relative correction on D/y_D with paired functional one and an exact sphere-null condition. Arbitrary ordinary extension and persistence through all later cones remain open. D.2.35 proves that every finite Postnikov section of the target is A1-acyclic; consequently fixed finite Postnikov data cannot alone give a universal invariant closed under all cone attachments and transfinite colimits. D.2.13 and D.2.16 exclude every ordinary fourth-stage extension of the proposed Hopf attachment, and force the specified Hopf coefficient to vanish for every map. The implication for arbitrary first-cone cup products and later nullification stages is still being tested. D.2.14--D.2.15 exclude the degree-one Prüfer candidate at every prime by proving its stable ideal is the full primary ideal. |
| D.3 | No largest non-total reversible localizer. Every nonzero finite primary addition to the lower endpoint reaches the upper endpoint. Single Moore targets, all infinite identical Moore wedges, and all bounded-cardinality finite-dimensional target families give the same sphere-test interval element (D.3.3--D.3.6). D.3.7 gives a countable universal generating list for all connected polyGEM-generated reversible localizers. D.3.8 gives at most countably many connected p-primary infinite-loop-generated localizers at a fixed stable part. | **Open:** set size at fixed stable part; whether the projective-space interval has more than two elements. In particular, strictness of the common sphere-test class over the lower endpoint remains unproved. |
| E.1 | Refuted: a four-object fence satisfies both proposed hypotheses but is not an intrinsic fibration. | Strongest repaired simplex criterion proved in E.3–E.4. |
| E.2 | Proved: coefficient systems are hypercentral, allowing transfinite central filtrations. Uniform finite nilpotence is too restrictive, already over the circle. | Final review of the telescope necessity proof. |
| E.3 | Trefoil calculation and properness/unit-fibre equivalence checked. E.8 gives an exact bounded catalogue and coherent obstruction criterion using maps between localization-unit fibres; it also realizes an actual strict Cat factorization. E.8.1 gives explicit boundary cases. | The criterion is an enumerative obstruction test, not a claimed simpler condition using only the two original unit fibres. Independent review passed. |
| E.4 | Morava-K and KU locally constant localizers proved nonproper. The KU witness uses `(Q S5)_(p)` and the explicit negative homotopy groups of the height-one localized sphere. | Source interfaces and witness independently reviewed. |
| F.1 | Refuted: explicit saturated class has absolute A, Loc (8),(9), but neither relative A nor forward sieve gluing. Base `[1]` cannot be a counterexample. F.1.1 proves that (6′a) together with (8) forces relative A; (9) is unnecessary. | The corrected implication resolves XVI Corollary 7.7.2 and its footnote 56. |
| F.2 | Proved: the single reverse square already forces integral homology equivalences, including disconnected sources. | None beyond final verification. |
| F.3 | Set-generated/combinatorial correspondence proved. Literal unrestricted claim refuted in a universe with no measurable cardinal, by an actual Bousfield–Friedlander model localization. Under the stated class form of VP it holds. Transport and properness consequences proved. | Final proof/interface review; no automatic accessibility assumed. |
| G.1 | Strong stable derivator formula proved from the canonical spectrum action. Every accessible W is the constant-coefficient localizer of HOT_W. | None beyond final verification. |
| G.2 | Suspension is conservative, neither faithful nor full. G.6–G.7 prove in ZFC that the full sphere-null class is accessible and therefore has the required small-universe localization and derivator. | The compactness proof explicitly constructs degreewise compact models of completed sphere targets. |
| H.1–H.4 | Proved: products, accessibility under class-form VP, nonaccessible locally constant example with no measurable cardinal, classification for represented derivators. | Final universe and source checks. |
| H.5 | Literal proposed correspondence and Loc (6b) expectation refuted; corrected group tests and all-functor fibration criterion proved. Accessibility of the rational-unipotent case is positive under the stated VP hypothesis and negative when the indexing universe contains no measurable cardinal (H5.9). The other listed cases have explicit generating constructions. | All six cases are decided with the necessary set-theoretic qualification. The rational-unipotent obstruction was independently reviewed. |
| I.1–I.8 | All proved or refuted with strongest replacement statements and finite witnesses. The supplied 317 and 312 interfaces were audited against opened primary sources. | Final independent reading of the higher-category audit. |
| I.9 | Stronger finite theorem proved: every connected finite Thomason-fibrant poset is categorically contractible. Infinite identity-isolation criterion and finite-principal-ideal qualifications written. | Final check of the precise infinite core statement and INDLOCAL audit. |
| J | Consolidated manuscript-page and literature comparison is in Part J; `REVLOC_source_crosswalk.csv` gives one row for every numbered statement. | The Farjoun book is honestly marked partly opened: only the two specified chapter previews were accessible. No claim is made about unread portions. New claims will be added to the crosswalk as they are integrated. |

## Proof audits and independent checks

The attached AI-produced results are treated as proposed proofs, not authorities. Each used interface is checked in the relevant section. The finite binary-icosahedral witness was rebuilt independently rather than accepted from PRETOT. The strict higher-category transfer has a step-by-step audit, and the distinction between a strict categorical globe and a coherator globe is kept explicit.

Two independent readers reviewed the bounded-subcomplex accessibility proof. The nonaccessible derivator construction was independently checked, including its monadic restriction argument and bounded cochain obstruction. The new unrestricted model-localization counterexample was checked against the corrected primary statement of Stanculescu Theorem 1.1; its radical is idempotent because reduced groups are closed under extensions, which supplies the required pullback property.

Subsequent independent reviews covered the finite-target locality proof, the full sphere-class compactness argument, the KU nonproperness witness, the rational-unipotent reduced-product obstruction, the bounded factorization criterion, and the forward-gluing implication to relative Theorem A. The odd-prime Moore proof was checked against the original CMN propositions, including the printed connectivity ranges; its bottom-dimensional case is supplied explicitly rather than inferred from a theorem outside its stated range.

The mod-2 Moore proof was independently checked at its geometric interfaces: the spherical two-letter class, the three-letter projection, the eleven-letter Lie projector, the comultiplication used to obtain a map to a wedge, and the convergent unlooping argument for arbitrary sources. Two distinct expansions give the same integral count matrices and their invertible mod-2 reductions. The cyclic-fundamental-group proof uses the suspension unit and the universal cover; Strom's Corollary 12(a) was opened and checked specifically to avoid importing a finite-type hypothesis on the mapping source.

The target-family collapse results were independently checked as well. D.3.4 uses actual finite Lie retracts and uniform pro-zero towers of finitely many Hilton--Milnor factor types, followed by G.7 compact shrinking. D.3.6 recovers completed spheres from the unstable higher-exponent Moore tower through finite Postnikov pro-spaces; the Isaksen fibrancy and completion statements were opened and checked directly, and the higher-exponent cellular cofiber matrix was verified. These results eliminate the proposed cardinal and Moore-target distinctions without asserting a strict intermediate class.

The third-hour stable-part results were reviewed at their nonlinear interfaces. D.2.7 uses Bousfield's exact suspension/nullification identity, not an interchange of stabilization and nullification. D.2.9 uses the connective truncation of successive spectral nullifications to control all components of the mapping space; it does not interchange maps with an infinite colimit. D.3.3 uses a finite Goodwillie stage of an odd-dimensional localized sphere, the checked periodic-localization comparison, and Levy's ordinary nullity theorem for torsion infinite loop spaces. It makes no claim that the Goodwillie tower converges on a Moore space. D.3.5 explicitly controls both inverse limits and derived inverse limits, then passes from countable sources to arbitrary sources.

The fourth-hour size results were independently reviewed. D.3.7 reduces arbitrary abelian Eilenberg--Mac Lane generators to a countable arithmetic list and extends to connected polyGEMs through the opened acyclic-class comparison. The proof treats degree-one rational cofibers, nonseparated Ext-complete groups, genuine bar quotients, and the distinction between completed free modules and abstract free modules. D.3.8 combines D.2.9 with the exact ordinary space--spectrum nullification comparison to identify every connected p-primary infinite-loop-generated class from its stable part, lowest degree and divisibility flag. The divisible case is proved separately using the general stable-GEM error theorem, a one-degree-larger bound, and a two-stage comparison. Its final Postnikov step puts the relevant Eilenberg--Mac Lane spectrum in the stable part before taking the connected cover. Neither result settles the general fixed-stable-part size question.

D.2.11 has passed an independent complete review. Its product closure uses diagrams augmented by an initial zero, retaining the extra product value. A fibre sequence is realized by the action bar of the loop of its base on its fibre, checked through the conservative forgetful functor. Simultaneous induction over every nonnegative loop of a finite weight truncation yields a countable generating family. Thus no join axiom or unproved fibre/base extension property of a nullification kernel is needed. The ordinary-space consequence checks lower chromatic acyclicity and connectivity before using the fully faithful periodic model. Hovey--Strickland dualizability and the exact Ravenel--Wilson rank calculation supply a local-unit retract; the prime-two proof uses rank-one coevaluation and does not assume commutative Morava K-theory. The proof does not exchange ordinary nullification with periodic localization or an inverse limit.

## Computations

The programs in `code/` save exact data and assertions in `code/outputs/` or the explicitly named `outputs/` files:

- `CD_finite_checks.py`: all objects, arrows, composites and associativity checks for the 35-object/159-arrow acyclic category and the 16-object/68-arrow braid presentation category; integer boundary Smith forms; complete order-120 coset table and explicit generating matrices in `SL2(F5)`.
- `FGH_literal_axioms.py`: the finite degree-two sphere and Grothendieck-construction witness to failure of relative A.
- `EH5_fence_counterexample.py`, `EH5_trefoil.py`, `EH5_group_witnesses.py`: strict-fibre and coefficient/group counterexamples.
- `I_finite_checks.py`, `I_torsion_witness.py`, `I_fibrancy_checks.py`: beat cores, simple-collapse data, a nonzero Whitehead-torsion unit and finite attachment data, and the finite tree obstruction to fibrancy.
- `I_lie_moore.py`: two independent exact eleven-letter commutator computations; both generator matrices have raw counts `[[3125,3125],[3039,2460]]` and reduction `[[1,1],[1,0]]` modulo two.
- `D2_fiber_poly_check.py`: an independent calculation of 13 polynomial fibre classes through degree nine, their full reduced coproducts and 39 Steenrod-operation values. This certifies the finite polynomial algebra only; the top-operation, Browder and homotopy interfaces are proved and audited separately.
- `D2_fiber_degree10_poly.py` and `FGH_H10_poly_check.py`: two separately written degree-ten polynomial checks, each passing seven classes, their full coproducts and 21 primary operation values. These verify part of the next working homology table; they certify no tenth-stage homotopy extension or integral exponent.

The exact theorem statements explain which conclusions are mathematical proofs and which finite portions the programs certify.

## Approaches rejected or still under test

The following tempting shortcuts have been explicitly rejected: a space-level Kahn–Priddy section need not be an infinite-loop section; generator-nullity need not imply map-locality; stable membership need not imply unstable asphericity; a set of target spaces does not automatically yield an accessible localization; ordinary and strong resolving classes differ; a compactness proof in the homotopy arrow category cannot silently replace it by the arrow category of the homotopy category; full stable part does not imply totality; properness of a model category alone supplies the intrinsic fibration axiom, not an unproved higher analogue of every categorical fibration axiom.

For active approaches, failures and next steps see `notes/main_worklog.md`, `notes/FGH_report.md`, `notes/EH5_report.md`, and `notes/I_progress.md` as well as the open paragraphs in the manuscript. These are retained as work records and may be superseded by later proved sections.

The most recent direct attacks on D.2 and D.3 are recorded as follows. The classes generated by `Q Sigma^r K(Fp,2)` have an exact adjacent-nullification calculation, but the comparison of their reversible closures still requires a genuinely unstable test. Finite-type suspended Eilenberg--Mac Lane targets have no phantom maps from the indicated finite-type sources, but this does not prove that all actual maps vanish. Infinite products of suspended Eilenberg--Mac Lane spaces have not been shown to retain the required stable part; closure of a localizing category under such products cannot be assumed. For the degree-one Prüfer candidate, D.2.14--D.2.15 prove that `loc(Sigma^infty CP^infty smash S/p)` is the full p-primary ideal at every prime. The E1 coefficient-ring detector, the bottom circle-transfer calculation and a finite module endomorphism ring remove the prime-two obstruction. This rules out the degree-one Prüfer candidate for zero finite stable part. None of the excluded approaches is counted as a separator.

## Typesetting and reproducibility

The LuaLaTeX installation had no generated format and no luaotfload module. A format was generated locally from the installed LaTeX sources; the manuscript uses Latin Modern Type 1 fonts with LuaLaTeX. `tools/build_pdf.py` records every compilation pass and the bibliography run. The first completed build is 68 pages. Its build log reports zero overfull boxes (therefore zero exceeding 2 pt), zero missing characters, and no undefined citations. The first successful layout pass also had zero overfull boxes; the before/after overflow counts are 0/0. Pages 1, 20, 40, 60 and 68 were rendered and visually inspected; margins, displayed mathematics, headings, citations and bibliography are legible with no clipping. No overflow pages required a separate inspection.

The second-hour build is 97 pages. Its final log again records zero overfull boxes, zero overflows exceeding 2 pt, zero missing characters, and no undefined citations; the before/after overflow counts are 0/0. The final-layout sample was rendered and inspected at pages 1, 23, 25, 26, 29, 37, 59, 72, 88 and 97, covering the new Moore proof and matrix, the stable-part reductions, the unit-fiber criterion, accessibility proofs, the manuscript comparison table and the bibliography. All are legible with no clipping. The intermediate 93-page version was also inspected at pages 20, 33, 68 and 83. No overflow page needed a separate repair.

The third-hour build is 111 pages. The preceding 110-page layout had two overfull boxes, of approximately 104 pt and 4.8 pt, both in D.3.5. The long equality was split into aligned lines, and the prose line was rewritten. The final build has zero overfull boxes, zero exceeding 2 pt, zero missing characters, and no undefined citations: before/after overflow counts are 2/0. Pages 30, 32, 33, 34, 35, 38, 39, 40, 41, 43, 44 and 111 of the final PDF have been rendered and visually inspected, including both repaired layout regions, the new nullification proofs, the unstable Moore tower and the bibliography. All are legible without clipping. The earlier spread across the unchanged parts of the document remains recorded above.

The intermediate fourth-hour build is 115 pages, after adding D.3.7. It has zero overfull boxes, zero exceeding 2 pt, zero missing characters, and no undefined citations: before/after overflow counts are 0/0. Pages 44, 45, 46, 47, 48 and 115 were rendered and visually inspected, covering the entire new proof and the bibliography; all are legible without clipping. The subsequent 117-page supported-case build also had no overflows, missing characters or undefined citations; pages 48, 49, 50 and 117 were rendered and inspected. The strengthened D.3.8 build is 118 pages, with zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (before/after overflow counts 0/0). Pages 48, 49, 50 and 118 of that build were rendered and visually inspected, covering the complete revised proof and the bibliography; all are legible without clipping.

`tools/assemble.py` merges the owned bibliography fragments and records into the requested top-level files. `tools/source_crosswalk.py` regenerates the per-statement literature comparison. The current assembled register has 152 numbered statements. Every bibliography entry records whether its primary text was opened and the theorem numbers used.

## Timing, checkpoints, and omissions

Work began at approximately 09:57 UTC (10:57 Europe/Berlin). The first checkpoint is due at 10:57 UTC; subsequent checkpoints are due hourly. The first three-hour assessment is due at 12:57 UTC. Current work is advancing the main question and open items.

### First three-hour progress assessment — 12:56 UTC

The work is advancing the remaining requested classification questions. In the third hour, D.2.7–D.2.9 established exact nullification reductions and a common-stable-part chain; D.3.3–D.3.6 ruled out finite additions and identified three infinite-target candidate families. These results constrain the unresolved items themselves. Accordingly work continues under the user's progress rule. The next assessment is due at approximately 13:57 UTC. The current attacks are the nonlinear `P_A1(Sigma^2 B)` test, the strictness of the sphere-test class in the projective-space interval, and whether the rigid-group proper-class construction survives reversible closure.

Each checkpoint contains every current deliverable, program, exact output, proof note and build log. Attached archives and their extracted source texts are excluded, as requested. Downloaded reference PDFs and their extracted reproductions are not included as original work; bibliography URLs identify those sources. No authored proof passage has been discarded. Any future removal or replacement will be identified here.

### Checkpoint 01 — 15 November 2026, 10:57 UTC

The first hourly archive is `REVLOC_checkpoint_01.zip`. It contains the complete authored working tree at this time, including the 68-page visually checked PDF, build logs, exact finite outputs and current unresolved-item records. It excludes only attached material and unmodified downloaded reference reproductions identified above. Work continues; this is not the final return.

### Checkpoint 02 — 15 November 2026, 11:57 UTC

The second hourly archive is `REVLOC_checkpoint_02.zip`. It contains the full current authored tree, including the 97-page verified PDF, all 91 result rows, the per-statement source crosswalk, the eleven-letter Moore certificate, the research notes and build records. The remaining main open items are D.2.4 and the two questions retained in D.3.2. Work continues; this is not the final return.

### Checkpoint 03 — 15 November 2026, 12:57 UTC

The third hourly archive is `REVLOC_checkpoint_03.zip`. It contains the full authored tree, including the 111-page verified PDF, all 98 result rows, the updated source crosswalk and bibliography, every finite certificate, all research notes and the first three-hour progress assessment. The main question in Part B is proved, while D.2.4 and the two questions retained in D.3.2 remain open. The first progress assessment calls for continuing on those questions. This is not the final return.

### Revisions since checkpoint 01

The earlier open-status paragraphs for C finite targets, D finite H-spaces, E factorability, G full sphere-class accessibility, and H5 rational-unipotent accessibility have been superseded by C.9, D.1.6, E.8, G.6–G.7 and H5.9 respectively. Their unsuccessful approaches remain in the research notes and in the immutable first checkpoint. D.1.7–D.1.9 replace the open Moore paragraph with its full classification. The old table entries have been replaced here because they no longer describe the mathematical state, not because their former gaps were ignored. Part J and the source crosswalk are new. No original finite certificate or proof log has been removed.

### Revisions since checkpoint 02

D.2.7–D.2.9 add the bounded-suspension nullification formula, finite-primary RT-fixedness, and the common-stable-part chain with its adjacent nullifications. D.3.3–D.3.6 eliminate finite-primary additions and identify the Moore-target, large-wedge and finite-dimensional-target candidates with the same sphere-test interval class. The earlier possibility that varying those target cardinalities might yield different interval elements is superseded by these proofs. It remains in the work notes as the route that was tested. The corresponding result rows, source crosswalk entries and bibliography opening records have been added. No authored proof passage or finite certificate has been omitted.

### Revisions since checkpoint 03

D.3.7 adds a countable universal list for all connected polyGEM-generated reversible localizers. D.3.8 adds at most countably many connected p-primary infinite-loop-generated localizers at a fixed stable part, with explicit formulas for both bottom-divisibility cases. The earlier supported-only proof of D.3.8 is retained in `notes/FGH_D3_infinite_loop_supported_history.md`. These results replace the rigid-abelian proper-class lead and the divisible-bottom gap as active approaches; the general set-size question remains open. No earlier authored proof passage or certificate has been removed.


D.2.10 adds the full stable-to-unstable finite-target theorem. Its proof first places finite-group classifying spectra and their prime localizations in the colocalizing subcategory generated by the sphere, using the completed Segal theorem, tom Dieck splitting, Sylow transfer and an arithmetic pullback. The genuinely finite partition-complex models then put every relevant Goodwillie layer in that subcategory. Convergence of the identity tower proves the mapping-space statement for arbitrary sources. Root opened all primary interfaces; two independent readers found no gap. This rules out sphere/finite-target separation for the zero-finite-part candidate, while leaving its RT-fixedness open.


### Four-hour assessment — 15 November 2026, approximately 13:57 UTC

Continue. The fourth hour has advanced the requested classification questions directly. D.3.7 and D.3.8 give explicit set-size bounds for broad generator families at fixed stable part, including the previously untreated divisible-bottom case. D.2.10 proves a new obstruction to finite-target separation for the zero-finite-part candidate. The spectral Lie investigation has reduced a proposed periodic separator to a precise joint-detection/join-axiom issue, with the additional axiom recorded rather than silently assumed. These are changes to the mathematical state of the open items, not peripheral exposition. The next progress assessment is due about 14:57 UTC.

The direct next steps are the ordinary-nullification test in D.2.9, the join condition for nullification at all trivial K(2)-local Lie algebras, and product constructions whose stable p-torsion membership is controlled. The general fixed-stable-part set-size question, zero finite thick part with nonfixedness, and a third element of the projective-space interval remain open.

### Checkpoint 04 — 15 November 2026, 13:57 UTC

The fourth hourly archive is `REVLOC_checkpoint_04.zip`. It contains the full authored tree: the 120-page verified PDF, 101 numbered result rows, the updated source crosswalk and bibliography, all finite certificates, all research notes, and both timed progress assessments. The final build has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (before/after overflow counts 0/0). Root rendered and visually inspected pages 34, 35, 36 and 120, covering all of D.2.10 and the final bibliography page; previous builds have the distributed samples recorded above. All inspected material is legible without clipping. No previous authored file or proof passage has been dropped; original downloaded reference reproductions remain excluded from the archive.

### Revisions since checkpoint 04

D.2.11 closes the categorical gap recorded at the fourth-hour assessment and rules out all unstable K(2)-local separating targets for the zero-finite chain. It gives an explicit countable family of trivial algebras rather than supposing a localization at a proper class. Earlier attempts through a join axiom remain in `notes/I_periodic_lie.md`; they are superseded by the action-bar proof. The direct ordinary-nullification barriers, including the failure of inverse-limit interchange and the inapplicable finite-Krull hypotheses, are recorded in `notes/FGH_D2_direct_nullification_obstruction.md`. Products of Postnikov approximations, abelian Moore targets, and the Prüfer stable-ideal dichotomy are recorded in `notes/EH5_D3.md`. These restrictions do not settle D.2.4 or D.3.2.

The new build has 125 pages and 102 numbered result rows. A first build stopped at two unescaped mathematical subscripts in the new bibliography; the corrected successful build has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (overflow counts before/after 0/0). The failed log is retained as `build/D2_11_bibliography_failure.log`. Root rendered and visually inspected pages 36--40, 117, 122 and 125, covering the complete new proof and its new bibliography entries. All are legible without clipping. The prior distributed samples remain recorded above.

D.2.12 adds a direct unstable obstruction for every r at least one, at the prime two: no map from the suspension of `Q Sigma^r K(F2,2)` to `Sigma^(r+1) K(F2,2)` is nonzero on bottom homology. The first odd-r proof used a Nishida relation; it remains in `notes/I_unstable_obstruction.md`. The stronger final proof uses only the low Serre cohomology groups, the James tensor algebra, Steenrod naturality and the coproduct. It permits arbitrary maps and higher-weight corrections. Root and two independent readers checked the coefficient contradiction, including the exceptional possible quadratic term when r=1. This refutes an unstable lift of the stable retraction but does not identify ordinary nullification with a single retraction test; D.2.4 remains open.

The build incorporating D.2.12 has 127 pages and 103 numbered statements. Its final log has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (before/after overflow counts 0/0). Root rendered and visually inspected pages 40--42, 124, 126 and 127, covering the complete new proof, its transition from D.2.11, and the James and Serre bibliography entries. All inspected pages are legible without clipping. These checks supplement the distributed samples of the preceding builds.


The first-cone corollary to D.2.12 strengthens the map calculation: every map from any nonnegative suspension of A_r into Sigma^(r+1)B is zero in the target's first three mod-two homology degrees. For the unsuspended source, Sq² followed by Sq¹ gives a separate contradiction after restriction along Sigma^r B -> A_r; higher suspensions are treated by the original theorem and connectivity. The cofiber sequence proves injections for any first small simultaneous wedge of attachments, as well as injection on the bottom integral Z/2. The first possible image not excluded is the class dual to uv in degree r+6. No map realizing it has been constructed. A later attachment could alter the loop-space tensor algebra; a possible new cup product/Hopf invariant is the exact next obstruction.

The final fifth-hour build has **128 pages and 103 numbered statements**. Its final log has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (before/after overflow counts 0/0). Root rendered and visually inspected pages 42, 43, 44 and 128, covering the complete first-cone corollary, its neighboring statements and the final bibliography. All are legible without clipping; the 127-page and prior distributed samples remain recorded above.

### Five-hour assessment — 15 November 2026, approximately 14:57 UTC

Continue on the direct zero-finite-part test. This hour proved D.2.11, which excludes every realized unstable K(2)-local separating target, and D.2.12 with its first-cone corollary, which identifies an unstable obstruction and proves actual first-stage homology survival. These advance the remaining requested D.2.4 problem. They do not establish survival through the full nullification. The D.3 H-space source-family search is now stalled and is not being extended merely to accumulate exclusions.

The next direct steps are to determine whether an actual A_r-attachment can create the cup product/Hopf invariant that kills the relevant loop commutator, whether a periodic comparison holds on the restricted suspension-spectrum ideal I_p, and whether an actual circle-transfer/Thom construction settles the finite part of the Prüfer ideal. Broad unsupported localization-commutation assertions have been disproved or explicitly withheld. The next timed assessment is due approximately 15:57 UTC. If these efforts then amount only to peripheral detail, the user's stopping rule will be applied.

### Checkpoint 05 — 15 November 2026, 14:57 UTC

The fifth hourly archive is `REVLOC_checkpoint_05.zip`. It contains the complete authored tree, the verified 128-page PDF, 103 result rows, all bibliography fragments and source comparisons, all finite certificates, all research notes including the generic periodic-reflection counterexample, and the timed assessments. No previous authored file or proof passage is omitted. Earlier failed proof routes and the odd-suspension-only obstruction remain in their notes with their superseding arguments identified. Original reference reproductions remain excluded as requested. This is an incomplete research checkpoint, not the final return.

### Research since checkpoint 05

The next attachment problem is now concrete. For `B=K(F2,2)`, the actual map `eta_2 smash B : Sigma^3 B -> Sigma^2 B` is homology-zero but stably essential. Its cone is `CP^2 smash B`, where the product of the old degree-four and degree-five classes is nonzero. It therefore demonstrates exactly how a later cone could destroy the loop commutator used in D.2.12. It is not yet a permitted attachment: the missing map is its extension to `Sigma^2 Q Sigma B`.

`notes/I_eta_attachment.md` proves that this extension exists if and only if it exists at every finite stabilization stage. All relevant target homotopy groups are finite, so finite-skeletal mapping sets are finite and the phantom derived-limit term vanishes. Compactness then removes any purely infinite compatibility obstruction. A negative answer must already have a finite stage and finite relative-subcomplex witness. The first two stabilization stages admit compatible extensions. After killing the bottom source sphere and using an 11-connected pullback, the canonical extension also passes every relative cell through dimension eleven. The first remaining possible cellular obstruction lies in dimension twelve. The note computes the relevant quotient-bottom class in `pi_6(Sigma^2 B)=Z/2`; no order-four Hurewicz detection can be inferred from it. None of these finite-range statements asserts a full extension or nonextension.

`notes/FGH_D2_E2_eta_extension.md` checks the twice-adjoint primary homology calculation, including the reduced J-action and the top-operation Browder correction. The first candidate Steenrod contradictions cancel. Higher-weight primitive corrections remain available for ordinary space maps, which are not required to preserve double-loop multiplication or Dyer–Lashof operations. `notes/FGH_D2_first_attachment_hopf.md` records the cone/cobar boundary and its exact relation to first-stage homology survival.

The Prüfer alternative has also been reduced precisely: `J_p=loc(Sigma-infinity CP-infinity smash S/p)` is proper in `loc(S/p)` if and only if there is a nonzero derived-p-complete E-infinity ring whose reduced CP-infinity cohomology vanishes in every degree. `notes/EH5_Pruefer_transfer.md` proves this using the local unit and derived completion. The circle transfer, its first loop, and the Moore-smashed versions do not provide the needed sections. Neither complex-orientation base change nor an Eilenberg–Moore comparison is automatic for the hypothetical ring; the exact coherent-action and convergence issues are recorded. This equivalence does not decide which side holds.

The D.3 literature note now includes the opened August 2026 preprints of Pützstück and Barthel–Castellana–Heard–Sanders–Zou. The former gives the precise cardinality of smash-homology Bousfield classes. The latter explicitly distinguishes that result from the general cohomological set-size problem. These results do not settle the fixed-stable-part reversible question. The opened locations and scope checks are retained in `notes/root_late_source_checks.md` and the bibliography.


D.2.13 is now integrated. The canonical double-adjoint Hopf extension does not extend even as an ordinary map from the second to the fourth stabilization stage. A complete degree-thirteen target-basis calculation gives a Steenrod--Bockstein coefficient obstruction, with the top Browder correction retained and then shown Bockstein-zero. The same calculation rules out every H-map extension to the infinite stabilization. It does not rule out an arbitrary extension: that map would have to change the coefficient of the square of a degree-five class. The positive range through relative dimension eleven and the all-choices finite-detection theorem are included in the same statement. Root and an independent reader checked the entire proof. A coherent symmetric binary cross-effect cannot be inferred merely from an E2 multiplication, so that possible shortcut has been rejected explicitly.

### Six-hour assessment — 15 November 2026, approximately 15:57 UTC

Continue. This hour produced a finite obstruction to a concrete attachment that could otherwise defeat the first-stage nullification invariant: D.2.13 proves the canonical extension fails at the fourth stabilization stage and identifies the precise nonmultiplicative correction required of any replacement. It also proves that the unrestricted extension problem has a finite-stage witness if negative. Independently, the Prüfer candidate has now been resolved at every odd prime by a new Thom-orientation argument, independently audited and saved in `notes/EH5_Pruefer_odd.md`; its manuscript integration is next. Both changes advance the requested D.2 and D.3 candidate analysis directly.

The next attacks are realization of the necessary ordinary-map correction, the prime-two eta obstruction in the Prüfer local-unit criterion, and use of these outcomes to settle an actual zero-finite-part nonfixedness example or strict interval inclusion. The broad fixed-stable-part set-size question remains open. The next timed assessment is due about 16:57 UTC. The current return remains INCOMPLETE.


### Checkpoint 06 — 15 November 2026, approximately 15:57 UTC

The sixth hourly archive is `REVLOC_checkpoint_06.zip`. It contains the full authored tree, the 133-page verified PDF, 104 numbered result rows, the updated source crosswalk and bibliography, all finite certificates, and every authored research note including the newly proved odd-primary Prüfer result awaiting manuscript integration. The new D.2.13 proof and its adjacent text were rendered and visually inspected on pages43--47; page133 was also checked. All are legible without clipping. The successful build has zero overfull boxes, zero exceeding2pt, zero missing characters and no undefined citations (overflow counts0/0). An intermediate unescaped filename in a bibliography note was repaired; its failed log is retained as `build/D2_13_bibliography_failure.log`. Original reference scans and crops are excluded; no authored proof or failed approach is omitted. This is an incomplete research checkpoint, not the final return.


### Research since checkpoint 06

D.2.14--D.2.15 are integrated. Reduced complex projective space generates the entire stable category: `loc(Sigma-infinity CP-infinity)=Sp`. The proof first detects every nonzero E1 coefficient ring using a genuine Thom orientation. At two, the bottom reduced circle transfer is an odd multiple of nu; its vanishing makes eta act trivially on the finite module `R smash Ceta`. Applying the detector to that module's endomorphism ring removes the eta obstruction. Derived completion and the local monoidal unit give actual localizing generation. Consequently the Prüfer suspension-spectrum ideal is `loc(S/p)` for every prime, so this candidate has the full finite primary part. No general equivalence between smash Bousfield order and localizing membership is assumed.

D.2.16 settles the arbitrary-choice extension issue left by D.2.13. Every ordinary map `C4(Sigma B) -> Omega2 Sigma2 B`, for `B=K(F2,2)`, has zero coefficient on the specified top double-loop generator. An actual multiplication-deviation map from the double-suspended smash supplies the obstruction, without an H-map or coherent symmetric-factorization assumption. The complete source calculation has nine basis vectors: all 512 coefficient vectors were checked, and the unique candidate after the first two constraints violates the third. The Python source and exact JSON certificate are retained. In particular, `eta2 smash B` cannot extend even to the fourth stabilization stage, for any choices.

These are direct advances on the remaining D.2.4 investigation. They do not yet prove that `P_A1(Sigma2 B)` is noncontractible. A common Browder-bracket coefficient on two degree-six source labels remains possible in an arbitrary first attachment; the new Hopf obstruction excludes unequal coefficients, not the common coefficient. That coefficient and its effect on the old cup product are the next concrete test. The fixed-stable-part set-size and strict projective-interval questions remain open.


The combined D.2.14--D.2.16 build has 142 pages and 107 numbered statements (91 Proved, 12 Refuted, 2 Open, and two separately qualified refutations). The successful LuaLaTeX/BibTeX build has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations; before/after overflow counts are 0/0. Root rendered and visually inspected pages 47--55, 137, 139 and 142, covering the complete three new proofs, their transitions, the historical comparison and the relevant bibliography pages. All inspected pages are legible without clipping. The earlier 136-page odd-prime-only build also had zero overflows and citation/font errors; its rendering files are retained, but the full visual check is the later 142-page version just listed.

The residual first-attachment calculation has since been narrowed by an explicit integral configuration-chain computation of the second Bockstein. Root and both algebra reviewers checked the corrected chain representative and its signs. The remaining potentially dangerous pattern requires the degree-four source class to map to `a^2`, together with a specified common bracket term in degree six. These coefficients satisfy the primary relations checked so far; no realizing map or universal vanishing theorem has been obtained. The exact chain calculation, the remaining coefficients and the scope of the conclusion are recorded in `notes/I_first_cone_low.md` and `notes/FGH_D2_first_attachment_hopf.md`. This refinement is not counted as a solution of D.2.4.

At the seventh-hour assessment, the finite realizability step has advanced further. The opened Akhmetiev--Repovš--Skopenkov Theorem 1.1 and its proof give a smooth embedding of `(RP3 × RP3) × I²` into `R8`. Pontryagin--Thom collapse, labelled by the product of the two degree-one classes, realizes the exact remaining spherical primitive in the double-loop target. The construction was independently checked by root and all three reviewers. It supplies the top-cell choice needed in the six-skeleton correction; it supplies no extension over the seven-cells or over the full infinite-loop source. The complete geometric proof is in `notes/EH5_degree8_spherical.md`, with the finite correction in the adjoining research notes. Integration as D.2.17 is planned after checkpoint 07. These are direct advances on D.2.4, so work continues under the hourly progress rule; the next assessment is due at 17:57 UTC.

The Prüfer unstable comparison has plateaued at its exact nullification test. The Thom and orbit calculations do not decide that test, and broad searching along that route has stopped. Its owner has joined the finite extension calculation. At this assessment the rebuild had 142 pages and 107 rows, with zero overfull boxes, missing characters or undefined citations; final bibliography pages 131, 136 and 142 were additionally rendered and visually checked.

### Further direct progress, 17:22 UTC

D.2.17 and D.2.18 are integrated, giving 109 numbered statements and a 150-page manuscript. The framed product construction realizes the exact degree-six primitive and produces the six-skeleton correction. The next theorem computes the full group `pi_8(Sigma^2 K(F2,2)) = Z/4`, including the precise relation `2 rho = u_4 nu_4 eta_7`, and uses that relation to extend the correction over the seven-skeleton. The proof computes a three-connected fibre and all components of its finite stable attaching maps; independent reviewers checked the integral normalization and the component detectors. These results do not supply a map on the full source or a value of its ordinary nullification.

At 17:22 the next eight-cell calculation was under audit. It treated both the target homotopy group and the additional source cells, including the extension of the canonical map beyond the original double-loop stage. Its completed integration is recorded below. D.2.4 and D.3.2 remain Open.

The 150-page build has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations; before/after overflow counts are 0/0. Pages 54--62 and 150 were rendered and visually inspected, covering both new proofs, their transitions and the changed bibliography. All inspected pages are legible without clipping. The earlier inspection spread over the unchanged parts remains recorded above.

### Eight-skeleton extension completed, 17:29 UTC

D.2.19 is now integrated and independently audited. It computes `pi_9(Sigma^2 K(F2,2)) = Z/2`, with Hurewicz generator `{a,c}`, and proves that the Moore-top eta composite and `rho eta` both vanish. The source calculation retains every degree-eight product and uses an explicit integral configuration chain to determine the order-four boundary. It constructs an actual eight-skeleton map after separately extending the canonical summand through relative dimension nine. Two-local cell normalization is explicitly distinguished from an integral minimal-cell claim. Root's complete independent audit is `notes/root_D2_eight_audit.md`.

The new build has 157 pages and 110 numbered statements: 94 Proved, 12 Refuted, two Open, and two refutations with the qualifications printed in their status fields. There are zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations; before/after overflow counts are 0/0. Pages 62--68 and 157 were rendered and visually inspected, covering the complete new proof, transitions and final bibliography continuation. All inspected material is legible without clipping.

At that point the next unresolved step was the nine-skeleton. The completed calculation is recorded next. No finite-stage result is being counted as a solution of the full-source or ordinary-nullification problem.

### Nine-skeleton extension completed, 17:53 UTC

D.2.20 is now integrated. It computes the full stable group in the next target degree and proves that the ordinary mod-two Hurewicz map on `pi8 F` is injective. A second Bockstein on `Pm+ZA`, initially missed in the working calculation, is essential: the corrected stable answer is `(Z/2)^3`, not the provisional `Z/4 + (Z/2)^2`. The erroneous preliminary route is retained and explicitly superseded in the audit notes. The proof accounts for every torsion attaching component, then excludes the sole stable mod-two Hurewicz-kernel class from ordinary spheres by a Steenrod instability argument. It does not identify the ordinary and stable homotopy groups.

The source quotient splits so that the correction is supported on one factor. The entire eighth homotopy group of that factor has zero ordinary mod-two Hurewicz image. Naturality and the target injectivity therefore kill all nine-cell attaching maps, including the components invisible to primary operation tables. This constructs an actual map on the nine-skeleton with the previously specified low values. The longer preliminary source calculation remains in `notes/I_D2_20_source_full_history.tex`; the shorter complete argument is in the manuscript. Root's independent audits are `notes/root_D2_eight_audit.md` and `notes/root_D2_nine_audit.md`.

The current manuscript has **164 pages and 111 numbered statements: 95 Proved, 12 Refuted, two Open, and two separately qualified refutations**. The successful build has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations; before/after overflow counts are 0/0. Pages 68--76 and 164 were rendered and visually inspected, covering the entire new proof, its transition and the final bibliography. They are legible without clipping. Earlier distributed inspections cover the unchanged material.

The next exact issue is extension through dimension ten. The canonical summand has a possible Browder self-bracket obstruction, and pullback over the bottom Moore complex may make divisibility by four the relevant condition. The source correction and the target homotopy group are being computed independently. This is a conditional research lead, documented in `notes/root_D2_canonical_ten_lead.md`, not a claimed extension or nonextension. D.2.4 and D.3.2 remain Open.

### Eight-hour assessment — 15 November 2026, approximately 17:57 UTC

Continue. This hour completed D.2.17--D.2.20: it realized the previously undecided primitive geometrically, computed the target attaching groups and relations in the next two degrees, and constructed an actual ordinary map through the nine-skeleton. These directly advance the finite realizability obstruction in the remaining D.2.4 test. They are not a proof that the complete infinite-loop source maps with these values, and they do not decide ordinary nullification.

The next target degree now has a concrete alternative to an unsafe stabilization assertion: pass to the four-connected cover of the double-loop fibre, whose first possible Whitehead-product suspension kernel vanishes because it is an H-space. Its homology and stable attaching components are the next calculation. The source correction has a separate James-construction reduction, with relative compatibility explicitly still required. Root is checking the canonical relative ten-cell and its modulo-four obstruction. A tempting appeal to the Moore-coextension Whitehead square was rejected after identifying the wrong antecedent: the actual target generator has integral Hurewicz image twice the order-four generator. This correction is recorded in `notes/EH5_next_browder_square.md`; no numbered theorem depends on the rejected identification.

The next assessment is due about 18:57 UTC. If the work has then shifted to detail that no longer advances an open item, the user's stopping rule will be applied. Both D.2.4 and D.3.2 remain Open, and this report remains INCOMPLETE.

### Checkpoint 08 — 15 November 2026, approximately 17:57 UTC

The eighth hourly archive is `REVLOC_checkpoint_08.zip`. It contains the entire authored tree, the verified 164-page PDF, 111 result rows, assembled bibliography and all fragments, source crosswalk, all finite certificates and outputs, and every authored research note and log. The new degree-ten notes are explicitly conditional; rejected routes and the longer superseded ninth-stage source proof are retained with their status. Original source reproductions remain excluded as requested. The final rebuild after a bibliography correction again has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations. The changed bibliography page 161 was also rendered and visually inspected and is legible without clipping. No earlier checkpoint is replaced, renamed or deleted.

### Exact tenth-stage criterion, 18:24 UTC

D.2.21 is integrated and has passed two independent complete reviews. With the canonical relative eight-stage choice fixed, extension through dimension ten is equivalent to four-divisibility of the actual Browder square. The proof computes every relative cell in the range and every integral boundary, including the bottom Moore differential. The first James cell fixes the Whitehead-square normalization; there is no extra factor of two. The result is explicitly restricted to the canonical summand and the stated choices.

The new build has **165 pages and 112 numbered statements**: 96 Proved, 12 Refuted, two Open and two separately qualified refutations. It has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations; before/after overflow counts are 0/0. Root rendered and visually inspected pages 76, 77 and 165, covering the complete new proof and final bibliography. All are legible without clipping. The relative integer matrix and its exact modulo-four cochain identity pass `code/D2_canonical_relative_chain.py`.

The next target calculation has now also passed three independent full audits and is being integrated as D.2.22. It uses the four-connected cover, the complete degree-ten homology table, an explicit low-degree Koszul calculation, and both nonzero third Bocksteins. Its conclusions are exponent at most four, one order-two integral-Hurewicz-kernel generator represented by `rho nu`, and zero eta composites from the preceding homotopy group. It does not identify the actual Browder square with that generator. The correction's unit ten-cell maps and the combined extension remain unresolved; an abstract group exponent or mod-two spherical lift alone does not settle them.


### Dimension-ten obstruction completed, approximately 18:40 UTC

D.2.22--D.2.24 are integrated. The actual tenth-stage target has exponent at most four, integral Hurewicz kernel generated by the nonzero order-two class `rho nu`, and zero eta composites from the preceding group. The proof uses the actual four-connected cover, a complete eighteen-class degree-ten homology table, an explicit low Koszul calculation, both essential third Bocksteins, and the full stable attaching-component presentation. The unresolved common even-nu bit affects the abstract group alternative but not any stated conclusion.

The exact primary cohomology relation `Sq4(e6 dual) + Sq2(J1 dual) = 0` has two consequences. First, its cone value distinguishes the actual canonical Browder square from `rho nu` and proves that this square vanishes. The canonical summand therefore extends through relative dimension ten. Second, on the unit ten-class the same relation forces the dangerous bracket coefficient to vanish for **every** ordinary map `Sigma K(F2,2) -> Omega2 Sigma2 K(F2,2)`. The pattern realized through dimension nine cannot extend over the unit ten-skeleton, for any earlier choices. This is an obstruction to the combined pattern, fully compatible with the separate canonical extension.

The full-source corollary removes the k=2 commutator functional from the first-attachment test. Other suspension exponents and simultaneous attachments are being analyzed. Individual-cone safety is insufficient: linear images from different attachments can cancel, so a common factorization or exact vanishing is required. Persistence through later nullification cones is a separate unresolved issue. D.2.4 and D.3.2 remain Open.

The manuscript now has **178 pages and 115 numbered statements: 99 Proved, 12 Refuted, two Open, and two separately qualified refutations**. The first new layout had one display protruding by 43.25752 pt and invalid multi-column split alignments; these were repaired and the failed logs retained. The successful build has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations. Overflow counts before/after the repairs are 1/0 (over 2 pt: 1/0). Root rendered and visually inspected pages 77--89 and 178, covering all three new proofs and their transitions; all are legible without clipping. Bibliography pages 170 and 174 were also inspected. Earlier distributed inspections cover unchanged parts.

`notes/root_D2_ten_audit.md` records the independent mathematical and primary-source audit. The new exact certificate `code/D2_ten_exact_certificate.py` passes the integral Smith-form and chain identities, eighteen cohomology-relation evaluations, four source Cartan tests, and all four parameter cases of the target presentation, including 1,024 group-addition/Hurewicz checks. Its stated scope excludes the geometric inputs, which are proved in the manuscript.


### Uniform first-cone progress, approximately 18:55 UTC

D.2.25--D.2.27 are integrated. The full commutator functionals vanish for suspension exponents three and all exponents at least five. D.2.26 gives an exact quadratic criterion for a simultaneous cone, using actual loop homology and genuine singular-cup cochains; it proves precisely why a common target functional is required. D.2.27 then proves that the unsuspended functional is identically zero with one fixed normalization. Its proof lifts the operation relation to the five-connected fiber, identifies the universal secondary cup class, and gives five explicit source witnesses whose fourth squares span all degree-eight homology while their second squares vanish. This is uniform over every map and every small simultaneous unsuspended family.

The new build has **184 pages and 118 numbered statements: 102 Proved, 12 Refuted, two Open, and two separately qualified refutations**. It has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (overflow counts before/after0/0). Root rendered and visually inspected pages89--95 and184, including every new proof and the final bibliography. A mistyped text command in D.2.26e was noticed visually and repaired. Bibliography pages177,178,181 were also rendered and read; the complete changed Clément, Halperin--Lemaire and May entries are legible and unclipped. The final correction was rebuilt with the same zero-error counts, and page91 was rendered and visually rechecked before the checkpoint; the text command is now correct.

The exact source program `code/D2_Qsource_primary.py` independently enumerates the complete polynomial/Dyer--Lashof basis through degree12, applies Cartan and Nishida, and checks the Bockstein-square and dual Adem identities. It computes the full image of Sq4 on the kernel of Sq2 in source degrees3--8. Its degree-eight rank is five, agreeing with all five hand witnesses. The program's scope is a primary-operation constraint; no realization theorem is inferred from it.

Exponents one and four remain in the first-cone test. The fourth-exponent provisional Moore-top calculation used the wrong basis element; the corrected formula and withdrawn route are retained in `notes/EH5_first_cone_suspensions.md`. No numbered claim relies on that mistake. Persistence through later cones remains unresolved, as does D.3.2.


### Nine-hour assessment — 15 November 2026, approximately 18:57 UTC

Continue. The hour completed D.2.21--D.2.27. It computed the actual tenth-stage target, proved the canonical Browder square vanishes, and independently proved that the dangerous ordinary-map pattern cannot extend through the unit ten-skeleton. It then established the exact simultaneous-cone criterion, eliminated further suspended commutator functionals, and proved uniform vanishing for every unsuspended attachment with one common secondary-cup normalization. These are direct advances on the concrete remaining D.2.4 test. They do not determine the final nullification.

The next specific tasks are the exponent-one and exponent-four first attachments, the common normalization for mixed suspension families, and an invariant that can survive later cone stages. A corrected fourth-exponent Moore interface remains only a restriction; its realization or exclusion is not asserted. The exponent-one primary relation now leaves two specified coefficients. The fixed-stable-part cardinality and strict projective interval problem D.3.2 remains Open. The next timed assessment is due approximately19:57UTC. The report remains INCOMPLETE.

### Checkpoint 09 — 15 November 2026, approximately 18:57 UTC

The ninth hourly archive is `REVLOC_checkpoint_09.zip`. It contains the complete authored tree, verified 184-page PDF, 118-row result register, assembled bibliography and all fragments, source crosswalk, all finite certificates and outputs, and every authored note and log. The new exact source program and the full independent audits are included. Rejected and superseded routes are retained with their status; original supplied/reference reproductions remain excluded as requested. No earlier checkpoint is replaced, renamed or deleted. The final build has zero overfull boxes, zero exceeding2pt, zero missing characters and no undefined citations. The new mathematical pages and changed bibliography pages were rendered and read as recorded above. This is an incomplete research checkpoint, not the final return.


### Once-suspended reduction and a fourth-stage boundary, approximately19:25UTC

D.2.28 and D.2.29 are integrated, and the mixed-family addition to
D.2.27 has passed full independent review. The same secondary-cup
normalization now handles every simultaneous mixture of suspension
exponents0,2,3 and at least5. The once-suspended functional vanishes
on the entire unit and on its Dyer--Lashof generator; only the
product coefficient alpha3 beta4 remains. Its algebraic compatibility
is shown explicitly, without asserting that a map realizes it.

The fourth-suspension generalized Whitehead map exists on the entire
unit and has a cone with nonzero old cup product. Its canonical
extensions throughC4 are actual iterated counits. The fixed canonical
C4 extension cannot extend toC6: a source first-Bockstein identity
would make the independent restricted square xi(k) a boundary in
the actual double-loop target, which the complete free-E2 basis
excludes. AtC5 a top-operation Browder correction remains, so no
C5 claim is made. Agreement only on the unit does not fix theC4
restriction, and such arbitrary extensions remain open.

The successful build has **188pages and120numbered statements:
104Proved,12Refuted,twoOpen,andtwo separately qualified refutations**.
It has zero overfull boxes, zero exceeding2pt, zero missing characters
and no undefined citations; before/after overflow counts are0/0.
Root rendered and visually inspected pages93,95--99,176,and188,
covering the mixed-family claim and proof, both complete new proofs,
the new Arkowitz bibliography entry, and the final bibliography page.
All inspected material is legible without clipping. Earlier distributed
checks cover the unchanged sections. Root independently opened the
Arkowitz publisher PDF, including its general-space mapping-cylinder
qualification, and recorded the full mathematical audits in
notes/root_D2_ten_audit.md.

A proposed square detector for the fourth-exponent all-choices problem
has been ruled out by an actual degree-eleven cover class: it forces
the relevant Moore-top homology square to vanish after two loops.
The proof is retained in notes/EH5_first_cone_suspensions.md Sections7--8.
A suggested higher-Bockstein nonsphericity argument also fails:
its alleged target is already a first-Bockstein boundary. These
negative tests are not counted as vanishing theorems for all maps.
D.2.4 andD.3.2 remain Open, and this report remains INCOMPLETE.

### Actual once-suspended realization through dimension ten, approximately 19:50 UTC

D.2.30 is integrated and has passed independent mathematical review.
It constructs an actual ordinary map from the ten-skeleton of
`Q Sigma K(F2,2)` to the once-looped five-connected fiber, with the
remaining secondary-cup coefficient equal to `alpha3 beta4`.
The construction uses the actual Moore and Chang summands of the
eight-skeleton, a coordinated choice of their top-cell extensions,
and the complete target Hurewicz calculation. Every ninth attachment
extends by injectivity of the relevant Hurewicz map. The only possible
tenth obstruction is excluded by an actual cone-square calculation,
using the vanishing pullback of the bottom degree-five class.

This is a finite realization theorem. It does not extend the map
over the eleven-skeleton or the full infinite-loop source, and it
does not assert a nonzero old cup product in a finite cone without
the additional factorization test. The next integral calculation
has been reduced to a specified Moore coextension and a target
obstruction modulo twice the homotopy group. A retained common
extension coefficient in D.2.22 can change that quotient; no value
for it is assumed and no eleven-stage nonextension is claimed.

The fourth-suspension route has a second precise limitation. An
actual spherical variation changes the two tested restricted-square
coefficients simultaneously. The proposed higher-Bockstein detector
does not distinguish all such variations: a universal mixed-fiber
construction gives the relevant first-Bockstein boundary internally
in the connected cover and before two homology suspensions. The
full proof is retained in `notes/EH5_xik_Bockstein.md`, with an
independent root audit. This does not settle the arbitrary ordinary
extension problem or propagation through later nullification cones.

The successful build has **190 pages and 121 numbered statements:
105 Proved, 12 Refuted, two Open, and two separately qualified
refutations**. It has zero overfull boxes, zero exceeding 2 pt,
zero missing characters and no undefined citations; overflow
counts before/after are 0/0. Root rendered and visually inspected
pages 99--101, 184 and 190, covering the complete new proof,
its transition, the changed Hatcher bibliography entry, and the
final bibliography page. All inspected material is legible without
clipping. Earlier distributed checks cover the unchanged pages.
D.2.4 and D.3.2 remain Open, and this report remains INCOMPLETE.


### Ten-hour assessment — 15 November 2026, approximately 19:57 UTC

Continue. This hour proved the mixed-family extension of D.2.27
and completed D.2.28--D.2.30. The once-suspended first-cone test
now has only one coefficient, and that coefficient is realized by
an actual map through dimension ten. The fourth-suspension test
has an actual entire-unit example but a proved obstruction to
extending its fixed canonical C4 choice through C6. These results
directly change the remaining D.2.4 analysis; they are not only
additional detail about completed parts.

The next eleven-cell test has also been reduced to an exact Moore
coextension and a class modulo twice the target homotopy group.
The primary cone detector removes a separate ambiguity, while one
retained integral extension coefficient remains decisive. Determining
that coefficient, treating the other once-suspended lower branch,
and resolving arbitrary fourth-suspension extensions are concrete
next tasks. The full later-cone propagation obligation is still open.
D.3.2 has not been decided; a nonrepresentable-homology cardinality
route was rejected because its null classes fail the required wedge
closure, as recorded in the root note.

Both D.2.4 and D.3.2 remain Open. The next timed assessment is due
approximately 20:57 UTC. If the work then ceases to advance either
open item, the user's stopping rule will be applied without asking
whether to continue. This report remains INCOMPLETE.

### Checkpoint 10 — 15 November 2026, approximately 19:57 UTC

The tenth hourly archive is `REVLOC_checkpoint_10.zip`. It contains
the complete authored tree, verified 190-page PDF, 121-row register,
assembled bibliography and all fragments, source crosswalk, every
finite certificate and its output, and all authored notes and logs.
The new once-suspended finite realization, canonical fourth-stage
obstruction, mixed-fiber cancellation audit, and conditional
integral eleven-cell notes are included. Rejected and superseded
routes retain explicit status. Original supplied/reference
reproductions remain excluded as requested. No previous checkpoint
is replaced, renamed or deleted. The final build has zero overfull
boxes, zero exceeding 2 pt, zero missing characters and no undefined
citations. The new proof and changed bibliography pages were
rendered and read as recorded above. This is an incomplete research
checkpoint, not the final return.


### Exact target group and the eleventh-stage boundary, approximately 20:21 UTC

D.2.31 resolves the retained integral extension coefficient by an
actual geometric construction. The spherical commutator of a
mod-two Moore smash product feeds a left-nested triple Samelson
map. Its bottom Moore sphere has order two, and its James tensor
word identifies its double-adjoint Hurewicz image uniquely. This
forces both retained coefficients to be zero and gives the actual
homotopy group `(Z/2)^4`. The nonzero order-two integral Hurewicz
kernel is retained. The older expression “exponent four” denotes
the earlier bound dividing four, not an element of exact order
four in this now fully computed group.

D.2.32 proves nonextension at the eleven-skeleton for every
ten-cell filling of the specified coordinated nine-stage map.
The complete source calculation accounts for thirteen degree-ten
classes, seventeen degree-eleven classes, and seven independent
integral order-two cycles. An actual Moore eta-coextension maps
to twice the target nu class; the exact integral source boundary
doubles its filling. The cone detector removes the separate
Hurewicz-kernel ambiguity. The elementary target group makes every
doubling change zero, leaving one unavoidable nonzero obstruction.

The scope is explicit: the nine-stage map is fixed, including its
Moore-top choice. Other lower maps that also vanish on K6 are not
excluded, and maps nonzero on K6 are not excluded. A different
Moore top changes the obstruction by one precisely identified
Toda bracket. Its cone detector is zero, so only the integral
p direction remains possible. This secondary operation and the
remaining lower-branch components are the next actual calculations.
No full-source vanishing or later-cone persistence is claimed.

The independent certificate `code/D2_once_eleven_certificate.py`
uses the existing full Cartan/Nishida enumerator to check both
complete bases, every listed first Bockstein, their ranks five
and seven, independence of all seven cycles, and their complete
second-square table. It passes. The script expressly does not
certify geometric attaching maps or replace the Toda proof.

The successful manuscript build has **196 pages and 123 numbered
statements: 107 Proved, 12 Refuted, two Open, and two separately
qualified refutations**. It has zero overfull boxes, zero exceeding
2 pt, zero missing characters and no undefined citations; overflow
counts before/after are 0/0. Root rendered and visually inspected
pages 86, 101--106, 189, 191--192 and 195--196. These include both
complete new proofs, the changed forward reference, both new
bibliography entries and their continuation, and the final pages.
All inspected material is legible without clipping. The bibliography
currently carries the final two lines onto page 196; this is a
legible continuation, not a missing passage. The next substantive
build will be checked again. Earlier inspections cover the unchanged
sections. D.2.4 and D.3.2 remain Open; this report remains INCOMPLETE.


### All-choice once-suspended reduction, approximately 20:44 UTC

D.2.33 is integrated and has passed independent complete reviews by
root and the source agent. A relative James-filtration calculation
uses the already proved bottom Whitehead-square vanishing to show
injectivity in the one target homotopy group needed for the
obstruction. The stable Snaith quadratic summand of any full
ordinary map consequently supplies an actual eleven-stage test.
This does not replace unrestricted ordinary mapping sets by stable
ones, and the unit summand is separated only by that finite lifting
argument.

The complete quadratic nine-stage has four actual factors. Its
nonzero bottom-six value is ruled out: the C-squared ten-cycle
attaches by the unique bottom nu class, and the signed arity-two
chain gives the exact next boundary twice that cycle. A bottom
value twice alpha therefore forces integral Hurewicz four times
the order-eight target generator, independently of every filling
and of the Moore-top toggle. The remaining bottom value is zero.
For all surviving lower choices, the BX obstruction modulo the
one-dimensional integral-Hurewicz kernel is p plus the Moore-top
choice times the singleton bracket <lambda,eta,2>. This bracket
is zero or p. Nonzero epsilon therefore requires its value p and
the nonreference top. Its actual value remains an open calculation;
it is distinct from the two attachment coefficients resolved in
D.2.31. The companion bracket with the last two entries reversed
is nonzero but cannot be substituted for it.

The independent source certificate now also checks the quadratic
basis dimensions 3,5,7,9 in degrees8--11, the Bockstein ranks2,3,4,
and the two fourth-square values used to identify the exact
attachments. All assertions pass. The next source certificate
computes degree12 and13 operations and integral H11 = Z8 plus
four Z2 summands, H12 = eight Z2 summands. This is retained as
research data, not a further nonextension theorem: the additional
nine-cell target filling and its possible next Toda operation
remain explicit.

The current successful build has **199 pages and 124 numbered
statements: 108 Proved, 12 Refuted, two Open, and two qualified
refutations**. It has zero overfull boxes, zero exceeding2pt,
zero missing characters and no undefined citations; before/after
overflow counts are0/0. Root rendered and visually read pages
106--110 and198--199, covering the entire new proof, its transitions,
and the final bibliography. All are legible and unclipped; the
previous two-line bibliography tail has reflowed onto a full final
page. Earlier inspections cover unchanged proof material.
D.2.4 and D.3.2 remain Open. No off-hour archive was created;
checkpoint11 and the next progress assessment remain due20:57UTC.


### The once-suspended Toda obstruction is resolved, approximately 20:52 UTC

D.2.34 proves **<lambda,eta,2> = {0}**, and D.2.33 therefore
excludes the nonzero normalized functional for every full ordinary
once-suspended map. This supersedes the remaining-bracket status
recorded in the 20:44 entry. The earlier lower-branch reduction
and exact nonzero reference obstruction are both needed for the
uniform conclusion.

The key is an actual antecedent, not a change of stable basis.
The generator lambda in pi9Y equals the eta2-smash-B map composed
with the suspension of the actual sphere rho in pi8Y. This equality
is detected by the complete degree-eight James tensor calculation;
no tensor-length-three term can occur in that degree. In the
lower double-loop target, rho extends over Ceta6. Its degree-two
coextension has zero mod-two Hurewicz. The actual ordinary
Hurewicz injection proved in D.2.20 kills the resulting composite.
Explicit suspension, counit and adjunction maps carry this zero
representative into the remaining Toda bracket. Its full
indeterminacy is already zero, so its value is exactly zero.
Root and both other agents independently passed every interface,
and all three independent audit notes are retained.

The single normalization of D.2.27--D.2.28 is unchanged. By the
common-factor criterion of D.2.26, the first-cone functional now
vanishes for arbitrary simultaneous mixtures of exponents
0,1,2,3 and every exponent at least5. The remaining first-cone
case is exponent4. Even complete first-cone vanishing would still
require a proof of persistence through later nullification cones;
that separate obligation is being attacked directly. D.2.4 is
therefore still Open, as is D.3.2. The conditional twelve-cell
branch notes are marked superseded for the excluded exponent1
case; their finite calculations are retained with their original
limited scope.


The post-D.2.34 build has **201 pages and 125 numbered statements:
109 Proved, 12 Refuted, two Open, and two qualified refutations**.
The final log records zero overfull boxes, zero exceeding 2 pt,
zero missing characters and no undefined citations (before/after
0/0). Root rendered and read pages 107, 110--112 and 201 of this
version: the changed forward reference, the entire new proof,
its transition and the bibliography tail are legible and unclipped.
The final two bibliography lines continue on page 201; no text
is omitted. The unchanged material retains its earlier visual QA.


### Eleven-hour progress assessment — approximately 20:57 UTC

**Continue under the user's stopping rule.** This hour advances an
unresolved requested item directly. D.2.31 determines the actual
obstruction group; D.2.32 proves the fixed-map eleven-stage
nonextension; D.2.33 treats all lower choices; D.2.34 evaluates
the last Toda bracket and rules out every nonzero exponent-one
functional. The first-cone proof now covers every simultaneous
mixture except exponent4. These are decisions of the outstanding
mathematical obstacles, not peripheral exposition.

The next attacks are specific: classify the allowed exponent4
relative changes after its known paired spherical variation;
determine the integral-square or relative-Moore obstruction in
the six-connected cover; and identify a stagewise invariant strong
enough to survive all later cone attachments. The bare low-degree
cohomology conditions are already known to be insufficient for
an arbitrary target, so that shortcut is not being assumed.
D.3.2 remains unresolved with the prior exclusions retained.
The next timed assessment and checkpoint are due approximately
21:57 UTC. The two Open rows and this report's INCOMPLETE heading
remain unchanged.

### Checkpoint 11 — 15 November 2026, approximately 20:57 UTC

The eleventh hourly archive is `REVLOC_checkpoint_11.zip`. It
contains the complete authored tree, verified 201-page PDF,
125-row register, assembled bibliography and all fragments,
source crosswalk, exact certificates and outputs, and every
authored note and build log. It includes all four new proved
statements and the independent audits of the decisive Toda
vanishing. Historical conditional calculations are retained with
explicit superseding status. Original supplied/reference
reproductions remain excluded as requested. Prior archives are
not replaced, renamed or deleted. This is an incomplete research
checkpoint, not the final return.


## 21:19 UTC — D.2.35 and the remaining fourth-suspension scope

D.2.35 is integrated and independently reviewed. Every finite Postnikov section of Y is ordinarily A1-acyclic, by the opened symmetric-product comparison and Bousfield's exact polyGEM acyclicity lemma. This rules out a universal preservation argument depending on any one fixed finite Postnikov range. It does not assert that a finite Postnikov section occurs along the particular construction beginning at Y.

The successful build has **202 pages and 126 numbered statements: 110 Proved, 12 Refuted, two Open, and two separately qualified refutations**. There are zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (overflow counts before/after 0/0). Root rendered and read pages 111--113 and 202, covering the complete new statement, its proof and transition, and the final bibliography page. All are legible without clipping.

The fourth-suspension relative source has been reduced to the genuine projective extended square of the bottom Moore space, with an exact integral chain certificate. This reduction is not a solution: it treats maps agreeing on one entire unit restriction. The bottom Moore data also permit a second pattern, with both the commutator and the linear f coefficient nonzero. No realization or exclusion of that entire unit pattern is established. Nor does a spherical rigidity assertion control its nonintegral-cycle Moore top. These qualifications are retained in the research notes. The all-except-four first-cone theorem remains unchanged, and neither open item is promoted.


## 21:31 UTC — D.2.36 excludes the second fourth-suspension pattern

The exact Steenrod-module computation found an obstruction in degree20, and it has been extracted as a nine-identity hand proof. Every degree-minus-three module map on reduced H*(K(F2,2)) sends u³ and v² to zero. Applied to an arbitrary ordinary map Σ5B->Σ2B, this proves that its degree-eight homology image is zero. Since the unit spans H8 of Σ4A1, the conclusion also applies to every full fourth-suspension map. The only dangerous primitive image left is the pure commutator k. No ordinary multiplicativity is assumed. All three parallel readers independently passed the identities and topological interface; two also read the final TeX.

The source program leaves every other coefficient free. Through degree19 its exact module problem is consistent; in degree20 Gaussian elimination gives precisely the nine-identity contradiction used in the proof. All applicable Adem relations on source monomials through degree20 were checked (1573 checks). The program certifies the finite source algebra, not a homotopy realization.

The successful build has **203 pages and 127 numbered statements: 111 Proved, 12 Refuted, two Open, and two separately qualified refutations**. It has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (overflow counts before/after0/0). Root rendered and visually read pages113--115 and203, including the entire new proof, its transition and the final bibliography. All are legible without clipping.

The remaining k4 relative test now has the correct universal scope. The bottom Moore restriction of every dangerous map is homotopic to the canonical restriction, by the exact Moore Puppe sequence and D.2.36. Restriction to C4 of this Moore space then gives the genuine finite projective extended-square test. Higher choices on the entire unit do not prevent this reduction. Its paired target functional has not yet been proved to vanish on every actual map from that finite source. This and later-cone preservation remain unresolved.


## 21:55 UTC — D.2.37 integrated and the finite source order audited

D.2.37 proves, for every prime p and n at least one, that the ordinary nullification of Sigma²K(Fp,n) by BZ/p smash K(Fp,n) is contractible. Hence the two generators have the same reversible closure. The proof uses the fat-wedge filtration, an all-components mapping-space equivalence into a loop-group target, and Badzioch's rigidification theorem. The original unlooped component gap is recorded and repaired in the expanded note. Root opened and read the relevant definitions, theorem statements and the full rigidification proof; root and an independent reader passed the saved TeX.

The successful build has **205 pages and 128 numbered statements: 112 Proved, 12 Refuted, two Open, and two separately qualified refutations**. Its final log has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (overflow counts before/after 0/0). Root rendered and read pages114--116,193,205, covering the complete new proof, its transitions, the new Badzioch entry and the bibliography tail. All are legible without clipping. The bibliography now has105 entries.

The finite projective extended-square source for the remaining exponent4 test has also been calculated in the fully written research note `notes/EH5_k4_source_top_order.md`. Root and a second independent reader passed its complete cell, homotopy-group and attaching-map argument. Its degree-ten homotopy group is (Z/4)^2 plus Z/2, and every spherical lift of the specified mod-two Browder class has order exactly four. The stable cell splitting retains all undetermined attaching bits; it does not infer a homotopy wedge splitting from a cellular Smith form. The numbered manuscript statement is still being prepared at this checkpoint. No vanishing of the target paired functional is claimed.

### Twelve-hour progress assessment — approximately 21:57 UTC

**Continue under the user's stopping rule.** Three new integrated theorems directly decide obstacles to D.2.4: the finite-Postnikov invariant barrier (D.2.35), the complete exclusion of the second exponent4 unit pattern (D.2.36), and the failure of the proposed primary tensor separator (D.2.37). The audited finite-source order calculation is a further direct advance on the remaining exponent4 obstruction. These are substantive proof decisions on an unresolved requested item.

The next attacks are to integrate that exact source calculation, compute or constrain the paired target functional on actual maps from this finite source, and determine whether a preserved obstruction survives later nullification cones. The separate fixed-stable-part size and interval questions in D.3.2 remain open. The next timed assessment and checkpoint are due approximately22:57 UTC. The two Open rows and the report's INCOMPLETE heading remain unchanged.

### Checkpoint12 — 15 November2026, approximately21:57 UTC

The twelfth hourly archive is `REVLOC_checkpoint_12.zip`. It contains the complete authored tree, the verified205-page PDF,128-row register,105-entry bibliography and all owned fragments, the per-statement source crosswalk, all exact certificates and outputs, and every authored note and build log. This includes the audited source-order research note and any standalone manuscript draft completed before archiving; such a draft is not yet part of the verified PDF or numbered register. Superseded calculations and rejected approaches remain with their stated limitations. Original supplied/reference reproductions remain excluded as requested. Earlier archives are never replaced, renamed or deleted. This is an incomplete research checkpoint, not the final return.


## 22:03 UTC — D.2.38 integrated with complete stable cell proof

The finite source-order theorem is now integrated as D.2.38. It retains the three primary-invisible attachment coefficients and proves the same group and exact-order conclusion for every value, rather than selecting a convenient splitting. The actual sphere factor maps to zero in QM by a separate exponent-two calculation in pi7(S/2); this does not infer an ordinary D-to-QM map from the stable weight projection. Root read the entire final TeX, including that refinement and the integral-lift coordinate clarification. Independent review of the complete note passed before integration.

The successful build has **209 pages and129 numbered statements:113 Proved,12 Refuted,two Open,and two separately qualified refutations**. It has zero overfull boxes, zero exceeding2pt, zero missing characters and no undefined citations (overflow counts before/after0/0). Root rendered and read pages116--120 and209, covering the full theorem and proof, both transitions and the bibliography tail. All are legible without clipping. The paired target functional and the actual global nullification remain open.


## 22:13 UTC — D.2.39 proves the general tensor collapse

For every connected ordinary BZ/p-acyclic C, D.2.39 proves that BZ/p smash C kills Sigma²(M(Z/p,1) smash C) and Sigma4C by ordinary nullification. Thus BZ/p smash C, M(Z/p,1) smash C, and C generate the same reversible class. The bounded-suspension criterion D.2.7 extends the equality to every C already in Rev(BZ/p). This eliminates the entire proposed tensor strategy within that class. It does not supply the missing inclusion of B, or BZ/p smash B, in Rev(QSigma B).

The general argument replaces the vector-space theory of D.2.37 by Segal's very special Gamma-space construction. All mapping components are included. Its spectral nullification telescope uses separate bounds on a fiber and its suspension to control the limit, without compactness of Sigma-infinity BZ/p. An elementary cofiber telescope for the degree-p circle map smashed with C then recovers Sigma²C from the Moore smash. Root and the axioms reader independently passed the complete final proof; root opened and read the primary Segal construction and proof as well as the exact Bousfield spectral comparison. The separate root audit is retained.

The successful build has **212 pages and130 numbered statements:114 Proved,12 Refuted,two Open,and two separately qualified refutations**, with106 bibliography entries. The final log has zero overfull boxes, zero exceeding2pt, zero missing characters and no undefined citations (overflow counts before/after0/0). Root rendered and read pages119--122,210,212, covering the complete new theorem, its transitions, the new Segal and expanded Serre entries and the bibliography tail. All are legible without clipping. Both requested open items retain their status.


## 22:23 UTC — D.2.40 integrated and verified

The actual fourth-loop target has space five-type fib(i Sq2 rho: K(Z/4,3) -> K(Z/4,5)) times K(F2,5). Integral UCT and the nonzero eta action determine the first invariant; the nonzero actual Hurewicz image of the next generator forces the second invariant to vanish. The full low Serre calculation proves that its degree-eleven cohomology is spanned by products and positive squares, while the canonical primitive A-annihilated Q7q4 has paired value one. The paired functional therefore does not descend from this five-type. This eliminates pure Postnikov descent as a shortcut; it does not decide its restriction to the connected cover or the full extension.

Root checked the complete TeX proof and reopened/read Serre's exact primary passages, including the higher-coefficient transgression and its inductive proof. The printed page locators were corrected: no7 pp201--203, no11/Theorem4 pp204--205, no14--15 pp207--209, Theorems8--9 p209. See notes/root_D40_audit.md.

The successful build has **214 pages and 131 numbered statements: 115 Proved, 12 Refuted, two Open, and two separately qualified refutations**, with 106 printed bibliography entries. The final log has zero overfull boxes, zero exceeding 2 pt, zero missing characters and no undefined citations (overflow counts before/after 0/0). Root rendered and read pages122--125 and214, covering the complete new proof, its transitions and the bibliography tail. All are legible without clipping.


## 22:33 UTC — D.2.41 integrated and visually verified

D.2.41 identifies the actual source sphere as plus or minus the Stiefel attaching map l4, after ruling out its possible weight-three component by an injective Hurewicz calculation. Every relative difference arising from a full fourth-stage extension sends this sphere to a double in pi10V. The first Bockstein can therefore be included in the sufficient target-operation test. The target membership and the actual composite h_M l4 remain unproved. Root and the independent reader checked the complete final TeX and reopened the exact Morisugi--Mukai and Arkowitz passages. Their audits are notes/root_D41_audit.md and notes/I_D41_audit.md.

The successful build has **217 pages and 132 numbered statements: 116 Proved, 12 Refuted, two Open, and two separately qualified refutations**, with 107 printed bibliography entries. Final log: zero overfull boxes, zero exceeding 2pt, zero missing characters, no undefined citations; overflow counts before/after 0/0. Root rendered and read pages124--127,214,217, covering the new proof, transitions, newly printed primary entry and bibliography tail. All are legible without clipping.

The current direct attacks are the actual secondary square class on Y<10> and the quadratic stabilization kernel containing h_M l4. The former is now identified by an actual universal cochain construction (root audit passed), but its beta/Sq3/Sq5 expression is not computed. The latter requires both a low quadratic-power map and its connecting-map quotient; a nonzero class in the quadratic layer alone does not determine its image in the actual target.


## 22:56 UTC — D.2.42 and strengthened D.2.43 integrated

D.2.42 constructs the actual secondary square class on the nine-connected cover and fixes one common normalization whose fourfold cohomology suspension is the paired functional. Its exact transgression is the independent square y8^2 in the nine-type. The complete low-degree spanning calculation proves that the restriction is nonzero and lies outside Sq1 H10 + Sq3 H8 + Sq5 H6. The sufficient operation criterion of D.2.41 is therefore false. No finite-source realization or full extension follows.

D.2.43 computes the actual quadratic source Z4, target Z8 plus Z2, and map sending its generator to2c. The natural metastable boundary identifies h_M l4 with the boundary of plus or minus2c. It vanishes exactly when2c belongs to the full-target stable James–Hopf image. An actual pinch-fiber calculation, using Blakers–Massey and the suspended sigma-prime and nu-squared lifts, proves that this homomorphism is zero for the finite nine-model. The composite has exact order four there and through all ten- and eleven-cell attachments. Target cells from dimension twelve onward remain an actual unresolved calculation.

Both final proofs and the finite quadratic input passed root and independent full-text audits. Root reopened the exact Behrens, Goodwillie, Morisugi–Mukai, Serre and Arkowitz interfaces, with the additional low stable stems already checked in Oka. The final LuaLaTeX/BibTeX build has **225 pages and134 numbered statements:118 Proved,12 Refuted,two Open,and two separately qualified refutations**, with108 printed bibliography entries. The final log has zero overfull boxes, zero exceeding2pt, zero missing characters and no undefined citations; before/after overflow counts0/0. Root rendered and visually read the complete new proof pages127–135 and the changed bibliography entries and tail; all are legible without clipping. The strengthened final pages were checked after build completion.

New research notes isolate three concrete next calculations, without upgrading their conclusions: the actual twelve-cell attachments under the counit, the integral Tor/James–Hopf transfer test, and the universal Moore-space Whitehead composite. The twelve-cell list retains all free p,q,x,y contributions; an earlier informal suggestion that onlyp mattered is explicitly withdrawn. The all-degree primary Steenrod/primitive-coalgebra route is closed by the existing stable-counit solution, now spelled out in FGH_D2_primary_module_boundary.md.


## 22:57 UTC — thirteen-hour progress assessment

Continue under the user's stopping rule. This hour proved D.2.38--D.2.43, including the exact source order, the general tensor-collapse exclusion, the target Postnikov and secondary-class calculations, the actual source-sphere constraint, and the exact quadratic/James–Hopf reduction with order-four survival through the target eleven-skeleton. These results directly change the remaining D.2.4 calculation; they are not peripheral polishing. Main B is proved, while D.2.4 and D.3.2 remain Open. The current manuscript is225pages with134rows (118Proved,12Refuted,2Open,2qualified) and108bibliographyentries. Compile and visual checks passed as recorded above.

The next three independent attacks are concrete: the actual higher target attachments through dimension15, the integral mod-four diagonal/transfer condition, and the universal Moore-space Whitehead composite using the precise pinch-fiber cell model. No proposed secondary identity is still treated as plausible after D.2.42 refuted it. No global nullification conclusion is drawn from the finite computations. The next assessment and hourly checkpoint are due at23:57UTC. This checkpoint retains the INCOMPLETE status and every authored deliverable, note, certificate, source audit, script and log.


## 23:36 UTC — D.2.44 and D.2.45 integrated and visually verified

D.2.44 reduces the actual universal Moore composite to the bottom
sphere, using the exact third cell of the pinch fiber and a required
Hilton correction checked by graded Jacobi. Its target image belongs
to the span of alpha sigma-prime and u4 E epsilon-prime, the second
of order at most two. Both universal bottom images suspend to zero
separately, so suspension does not determine their coefficients.
The complete proof and opened primary passages passed independent
full-text audits.

D.2.45 proves survival of the actual obstruction through every target
skeleton of dimension fourteen. The integral quadratic transfer has
kernel <4c>, whereas the obstruction is the boundary of2c. Only the
actual fifteen-cells can first kill it, and the full-target question
is already determined on the fifteen-skeleton. A half-product class
theta gives the exact necessary mod-four pairing and satisfies
beta_Z(theta)=x8 squared. The integral square and the pairing on the
stable Hurewicz image remain uncomputed; no full extension or global
nullification conclusion follows. The independent transfer certificate
passed its integral chain checks, all16 elements and256 addition pairs.

The final build has **232 pages and136 numbered statements:120 Proved,
12 Refuted,two Open,and two separately qualified refutations**, with
113 printed bibliography entries. The first build had two overfull
boxes, one exceeding2pt (maximum14.60222pt). Both were repaired.
The final LuaLaTeX/BibTeX log has zero overfull boxes, zero exceeding2pt,
zero missing characters and no undefined citations. Root rendered
and visually read pages135–141,226,228,229,231,232 after the final
build. All new proofs, their transitions, the changed bibliography
entries and the tail are legible without clipping.

A further audited research note sharpens Mukai's congruence for the
Whitehead square of the Moore eta coextension: the retained tau5
coefficient is even and its image has order two, hence contributes
zero. The coextension term consequently maps to zero in Y. This does
not yet evaluate either coefficient of the composite in D.2.44.
The independent Stiefel mapping-cone proof of D.2.45's survival bound
and the exact low Postnikov model under investigation are retained
as research notes. The next hourly assessment/checkpoint remains
23:57UTC; no checkpoint is made between the scheduled hours.


Archive exclusion correction before checkpoint14: the three files
notes/FGH_Mukai2001-01.png, -02.png and -03.png are unmodified
renderings of an original reference scan. They are excluded from
checkpoint14 and later packages, as are the downloaded source PDF
and the other identified reference reproductions. They were
inadvertently present in checkpoint13; that immutable archive is
not changed. The mathematical source locators, proof notes, audits,
and all authored material are retained. This is an exclusion of
reproduced source images, not removal of a proof passage.


## 23:57 UTC — fourteen-hour progress assessment

**Continue under the user's stopping rule.** This hour proved and
integrated D.2.44 and D.2.45. The actual universal composite is reduced
to bottom-sphere coefficients with its missing Hilton correction
explicitly repaired. The actual obstruction survives every target
skeleton through dimension fourteen, and the full problem is determined
on the fifteen-skeleton. Its necessary integral transfer/half-product
test is now exact. These are direct advances on the unresolved D.2.4,
not detail away from the requested questions. Main B remains proved;
D.2.4 and D.3.2 remain Open.

The verified manuscript has232pages and136rows:120 Proved,12 Refuted,
two Open, and two separately qualified refutations. Its printed
bibliography has113entries; the assembled bibliography also preserves
opened note-only sources. The final compile and visual checks are
recorded above and have zero remaining overfull boxes, missing
characters or undefined citations.

The auxiliary Moore coextension comparison has been fully evaluated:
it gives exactly an already known target-zero relation and is no longer
being pursued as an independent separator. The actual higher-cover
half-product, its mod-four lift, and the restriction to integral classes
of order at least four are recorded with their scopes. A new exact
finite source certificate identifies the integral chains of the binary
C2 Moore layer; the genuine eta-attached cell model is separately
retained, and no chain decomposition is called a stable wedge splitting.
The remaining even correction in its actual connected-cover map has
not been suppressed.

A further direct refinement has just been proved in the universal
Moore note, Section13: a bottom-sphere remainder can be chosen before
passing to the Moore space, and its actual sphere suspension is zero.
The complete sphere table then reduces the previous two target
coefficients to a single cyclic generator q=alpha sigma-prime plus
u4 E epsilon-prime, with h_Ml4 in <q> and2h_Ml4=2q. It is not yet
integrated in the verified PDF or numbered register at this checkpoint.
The generator's full-target value and the remaining order-two choice
are still uncomputed. Its final proof is retained for the next
independent review and integration.

The next attacks are the actual map from the finite binary source,
including its even chain correction and order-four nullhomotopy
coherence; the integral target square and stable Hurewicz image; and
the remaining one-parameter Moore composite. The exact low Postnikov
model and the permissible Pontryagin-square normalization are saved,
without a guessed multiplicative extension. The next assessment and
checkpoint are due at00:57UTC on16 November2026.

### Checkpoint14 — 15 November2026, approximately23:57 UTC

The fourteenth hourly archive is REVLOC_checkpoint_14.zip. It contains
the complete authored tree, verified232-page PDF,136-row register,
assembled bibliography and all fragments, source crosswalk, every exact
certificate and output, and every authored research note, audit, script
and log. The new cyclic-span refinement is included as a research note,
not as an unbuilt numbered statement. Superseded and rejected routes
remain with their exact limitations. Original supplied/reference
reproductions are excluded, including the three Mukai scan renderings
identified in the explicit exclusion correction above. No earlier
checkpoint is overwritten, renamed or deleted. This is an incomplete
research checkpoint, not the final return.


## 16 November 2026, 00:18 UTC — D.2.46 integrated and checked

D.2.46 is now integrated after the two-parameter result and the
integral transfer test. It proves h_Ml4 lies in the cyclic subgroup
generated by q=alpha sigma-prime+u4 E epsilon-prime, with4q=0
and2h_Ml4=2q. The sphere suspension is tested before passing to
the Moore space; this is stronger than the previous test after
that passage. Both independent reviews and the root audit passed.
The order of q and the residual choice when its double vanishes
remain uncomputed. D.2.4 and D.3.2 stay Open.

The integrated manuscript has233pages and137rows:121 Proved,
12 Refuted,2 Open and2 separately qualified refutations. Its
printed bibliography has113entries. Before and after this addition
the final build has0 overfull boxes (and0 exceeding2pt),0 missing
characters and no undefined citations. Root rendered and viewed
all D.2.46 pages and transitions (140--143), bibliography page227,
and changed bibliography/tail pages232--233. No clipping, overlap
or equation-number collision was found.

A separate exact computation now proves three actual degree-fourteen
fiber cohomology classes independent: (V*+P*)², (P*+Q*)², and
Sq6 Sq3 Sq1 A4*. Three classes defined by the actual retraction
T->F give the matrix [[1,1,0],[0,1,1],[0,0,1]]. The full hand
proof, two independent reviews, and a passing finite certificate
are saved. This removes one cancellation possibility in the
actual cover spectral sequence; mixed/product transgressions
and integral extensions are still being checked. The actual
a7 secondary Pontryagin normalization has also passed root
source and cone-map audit. No integral square value is inferred.


## 16 November 2026, 00:44 UTC — D.2.47 and D.2.48 integrated and checked

The actual integral half-class calculation and the complete low Serre
filtration are now numbered and integrated. D.2.47 proves that the
fiber group in degree eight is cyclic of order four, the restriction
of b8 is twice a generator z8, and the odd generator has the nonzero
mixed d5. D.2.48 proves that 2b8 has exact filtration four and
associated class U4 tensor V4. A different transgression kills the
entire base degree-eight class. Every possible competing differential
in this range is treated; the universal path fibration fixes the
coefficient of the mixed differential. Three independent readers and
the root passed these proofs. The integral square b8 squared is
not evaluated by either result. Both requested open rows remain Open.

The integrated manuscript has237pages and139rows:123 Proved,
12 Refuted,2 Open and2 separately qualified refutations. Its printed
bibliography has113entries. The first D.2.47 build stopped on an
unescaped underscore in a newly expanded bibliography note; the title
was written in words and BibTeX regenerated. The D.2.48 build had
one overfull display of23.07457pt, repaired by splitting the low-group
display. The final build has0 overfull boxes,0 exceeding2pt,0 missing
characters and no undefined citations: before/after overflow counts
for the final addition are1/0. Root rendered and visually inspected
pages142--147 and235--237, covering both complete new proofs, the
previous overflow, section transitions and the changed bibliography.
All are legible without clipping, overlap or equation-number collision.

The intrinsic integral James commutator calculation is saved in
notes/EH5_C2_Moore_quadratic.md Section7. Its literal chain identities
show that the doubled commutator is independent of all bottom-cycle
and top-nullchain choices; the actual Moore comparison identifies
it with the loop Hurewicz image of h_M l4. The opened current
Zhu--Pan primary statements fix the odd relative-Hurewicz coefficient.
This identity by itself asserts no vanishing. A separate suspended
Toda-bracket factorization is under final audit and will be recorded
with its precise scope when checked.


## 16 November 2026, 00:54 UTC — the integral square is decided

D.2.49 and D.2.50 are now integrated and independently checked.
The actual epsilon-prime term factors through an eleven-sphere,
with the full Toda-bracket indeterminacy retained. Unique lifts
to the connected cover make its integral loop Hurewicz image zero;
the other cyclic summand factors through a seven-sphere and has
the same vanishing. The actual universal obstruction therefore
has zero integral loop Hurewicz. Its comparison with the doubled
James commutator is exact and independent of all chain choices.

The next deduction settles the previously unevaluated integral
square. A six-reduced simplicial model and the canonical integral
cobar algebra turn the doubled-commutator nullchain into an
integral fifteen-cycle. Its reduced Alexander--Whitney diagonal
has the specified mod-four cup coefficient two. Thus the
half-product theta pairs one with its integral reduction and
cannot lift integrally. It follows that b8 squared is nonzero
of exact order two. The explicit mod-four lift of theta shows
that the detecting integral homology class has order at least
four. All three readers passed the root's coefficient argument
and the completed TeX, with the primary model and cobar
interfaces opened directly. No stable sphericity of that class
is inferred. D.2.4 and D.3.2 remain Open.

The final manuscript has243pages and141numbered statements:
125 Proved,12 Refuted,2 Open,2 separately qualified refutations.
The printed bibliography has117entries. Both compilation runs
for the addition have0 overfull boxes,0 exceeding2pt,0 missing
characters and no undefined citations (before/after0/0). Root
rendered and viewed every new proof page and its transitions
(pages146--151), the new bibliography entries on227 and235,
and the changed tail242--243. After revising two stale note-only
bibliography descriptions, root rebuilt and rerendered/reviewed
235 and242--243. The output remains legible without clipping,
overlap or equation-number collision. All preceding authored
proofs and superseded routes are retained with their scopes.


## 00:56 UTC — fifteen-hour progress assessment

**Continue under the user's stopping rule.** This hour integrated
D.2.46--D.2.50 and settled the actual integral square: it is
nonzero of exact order two. The full low Serre filtration,
the suspended Toda-bracket factorization, the exact doubled
loop-commutator identity, and the canonical-cobar cup evaluation
are direct advances on D.2.4. The work is not confined to detail
away from the requested questions. Main B remains proved;
D.2.4 and D.3.2 remain Open.

The verified manuscript has243pages and141rows:125 Proved,
12 Refuted,2 Open,2 separately qualified refutations. There are
117printed references, with all newly used primary interfaces
opened. Final build and visual checks have zero remaining
overflows, missing characters or undefined citations. Every
new proof page and all changed bibliography entries have been
rendered and read.

The next direct obligations are the stable Hurewicz image in
degree fifteen and the actual cyclic homotopy obstruction.
The nonzero half-product pairing now exists on integral homology,
but its witness is not known to be stably spherical. The positive
Steenrod-operation test reduces to the coupled Sq2/Sq4 equation
recorded in the new root frontier note; the Sq1-only possibility
is excluded by the now nonzero integral Bockstein. A separate
actual suspended-nu image reduction is being audited in the
universal Moore note. No homotopy vanishing or full ordinary
cone-extension claim is inferred. The next assessment/checkpoint
is due01:57UTC.

### Checkpoint15 — 16 November2026, approximately00:57UTC

The fifteenth hourly archive is REVLOC_checkpoint_15.zip. It
holds the full authored tree, verified243-page PDF,141-row
register, assembled bibliography and fragments, source crosswalk,
every finite certificate and output, all authored notes, audits,
reports, scripts and logs. Original supplied/source reproductions
remain excluded by the recorded rules; no earlier checkpoint is
overwritten, renamed or deleted. This is an incomplete research
checkpoint, not the final return.


## 01:15 UTC — D.2.51 and D.2.52 integrated and visually verified

The full mod-two diagonal now forces every actual James--Hopf value
into the cyclic subgroup generated by2c. The half-product pairing
detects2c or6c; an odd multiple of a stable sphere changes6c to2c.
Thus existence of a stable-spherical detector is exactly equivalent
to vanishing of the actual homotopy obstruction. The three possible
image subgroups give orders4,2,1; none has been selected. This is
D.2.51, including its sixteen-element exact algebra certificate.

D.2.52 constructs a finite fifteen-dimensional cone mapping to L
whose top integral class detects theta. Its actual cofiber map to
a wedge of three cones computes the mixed coefficient two by the
Stiefel comparison. All positive Steenrod operations annihilate
the resulting mod-two class: the first two vanish in the source,
the fourth maps through a sphere with zero mod-two Hurewicz, and
the eighth vanishes by instability. Thus theta lies outside the
entire positive-operation image in degree15. This closes the
primary-operation test without asserting stable sphericity.

Root read both final proofs; the independent full-proof audits
passed. D.2.45 retains its pointwise ambiguity and now gives exact
forward references to D.2.50--51. The resulting PDF has246pages
and143rows:127 Proved,12 Refuted,2 Open,2 separately qualified
refutations, with117printed references. The build has0 overfull
boxes,0 exceeding2pt,0 missing characters and no undefined citations
(before/after0/0). Root rendered and visually read138--140,150--154
and246; all are legible without clipping or equation-number overlap.
The full audit is notes/root_D51_D52_audit.md.

The next actual stable obstruction is being checked in the sphere
AHSS. The double counit is12-connected, so H9(Omega²L;Z) maps
isomorphically to H11(L;Z); the order-two class4N' therefore remains
nonzero integrally. Its raw nu-row coefficient is not yet a proved
surviving differential: the incoming d2/d3 quotient and the actual
suspended Toda coefficient must still be computed. The original
requested D.2.4 and D.3.2 remain Open. The next scheduled assessment
and checkpoint remain01:57UTC.


## 01:24 UTC — D.2.53 integrated and visually verified

The actual epsilon-prime target term is zero. D.2.53 selects the
cone extension and coextension realizing the specified epsilon-prime,
so its factor t lies in the correct ordinary Toda bracket before
suspension. The suspended bracket contains zero by last-entry
degree-two naturality and the actual exponent-two target group. Its
full indeterminacy is zero. This eliminates the term, with every
nullhomotopy choice needed for the chosen factor tracked explicitly.
It does not assert that every arbitrary factor of the earlier
nu composite has zero suspension. The remaining generator is exactly
alpha sigma-prime, with its value and order still unknown.

Root and both independent readers passed the complete final proof.
Root reopened the author program's sixth/seventh-stem tables and
verified all stated two-primary zeros. The bibliography records the
exact Toda attributions without claiming that the original book
pages were opened. The detailed audit is notes/root_D53_audit.md.

The verified PDF has248pages and144rows:128 Proved,12 Refuted,
2 Open,2 separately qualified refutations, with117printed references.
The build has0 overfull boxes,0 exceeding2pt,0 missing characters
and no undefined citations (before/after0/0). Root rendered and
visually read154--156 and246--248, covering the entire new proof,
its transitions, the expanded source note and the bibliography tail.
All are legible without clipping or equation-number collision.

This zero removes the earlier possible nu-row obstruction for a
chosen half-product detecting cycle. The new actual finite source
has only a twice-sigma stable top attachment. Consequently its top
class survives through d7. The precise d8 quotient, including three
possible incoming differentials and the freedom to change the
detecting cycle, is the next direct calculation on D.2.4.


## 01:33 UTC — D.2.54 integrated and visually verified

The chosen half-product detecting cycle now survives every stable
AHSS differential through d7. Its only possible outgoing differential
is d8, whose exact raw coefficient is2n times the bottom generator
in H7(L;Z16)=Z4. The true target is its page-eight quotient.
The connective image-of-J comparison kills the incoming d2; zero
fourth/fifth sphere stems eliminate incoming d3/d4. Only incoming
d5,d6,d7 remain, with their actual earlier-page source conditions
retained. No one of those maps is asserted zero without proof.

The exact criterion also accounts for changing the integral cycle.
Let H0 be the theta-zero subgroup of E8_(15,0). The original
homotopy obstruction vanishes exactly when the displayed d8 value
belongs to d8(H0). A proper quotient of the target Z4 would already
suffice. A nonzero obstruction requires the full Z4 target, odd n
and zero d8 on H0. These are unresolved necessary conditions, not
a selection of a case. This is the new proved D.2.54.

Root and the independent reader passed the complete actual-source,
filtered-cofiber, page-group and convergence proof. Root opened the
exact Adams cellular construction and Bruner--Rognes image-of-J
calculation directly. Their bibliography entries specify the exact
text versions and interfaces used. The audit is notes/root_D54_audit.md.

The verified PDF has250pages and145rows:129 Proved,12 Refuted,
2 Open,2 separately qualified refutations, with119printed references.
The build has0 overfull boxes,0 exceeding2pt,0 missing characters
and no undefined citations (before/after0/0). Root rendered and
visually read156--158,233--234,238,249--250, covering the entire new
proof and transition, both new source notes, and the bibliography
tail. All are legible without clipping or equation-number collision.

The next computation is extending the actual cover data into the
source degrees of d6/d7, while checking the actual nu composites of
the twelve-cell attachments governing d5. The auxiliary James--Hopf
image survives through its own eleven-skeleton; its twelve--fifteen
attachments still require calculation. These are research notes,
not additional claims of global nonvanishing.


## 01:52 UTC — D.2.55 and D.2.56 integrated and visually verified

The incoming fifth differential at the final sigma target is zero. The
proof fixes the actual doubled N-lift by the entire injective torsion
detector matrix, evaluates its cone composite, and retains the possible
even N term in the Q-cell normalization. Every twelve-cell nu image is
then included. Independent top-cell projections and the original lower
quotient prove that their span has zero intersection with the bottom Z4.
This stronger stage-injection statement implies the actual page-five
vanishing without replacing its source by raw homology. Only incoming
d6 and d7 remain before the final d8 target.

The new cover calculation proves base-map injectivity through degree13
using exact Newton primitives and a full fiber-coaction test. Freeness
over the image Hopf algebra, followed by a bounded minimal-resolution
argument, gives the actual edge quotient through degree12. Two actual
bar filtrations then give H13(L;F2) of dimension17 and H14(L;F2) of
dimension25, with complete double-suspension kernels. An initial
unintegrated count27 omitted the two reversed loop-space products.
Independent review caught this, and the two additional Browder relations
are present in the final theorem and its proof. The exact polynomial
and integer-series certificate was rerun and passed.

Root and the independent readers passed the complete final proofs. Root
opened the exact Milnor--Moore and Madsen--Milgram primary passages and
rechecked the CLM suspension formulas in the already downloaded scan.
The audits are notes/root_D55_audit.md and notes/root_D56_audit.md.

The verified PDF has256pages and147rows:131 Proved,12 Refuted,
2 Open,2 separately qualified refutations, with121printed references.
The final build has0 overfull boxes,0 exceeding2pt,0 missing characters
and no undefined citations. The first build stopped at an unmatched
TeX brace in the new bracket display; it was corrected and the full
build rerun. Root rendered and visually read158--163,250,252,255--256,
covering both entire new proofs, their transitions, both new reference
entries, the expanded Strickland source note and the bibliography tail.
All are legible without clipping or equation-number collision.

The next exact test is the image of the sphere Adams class h0h3 in
Ext^{2,16} of the fourteen-stage. A nonzero class would survive by
naturality and the absence of H15 in that finite stage, forcing both
remaining incoming differentials zero. This conditional argument has
been independently checked; the actual Steenrod comodule and finite
boundary matrix are now being computed. The auxiliary James--Hopf route
also has a new actual Chang-space nu-composite zero, recorded with its
remaining coupled higher-cell ambiguity. Neither route is claimed to
have evaluated the final homotopy obstruction.


### Sixteenth-hour progress assessment — 16 November 2026, 01:57 UTC

Continue under the user's rule. This hour proved D.2.51--D.2.56,
which directly reduce the remaining D.2.4 obstruction: exact stable
Hurewicz detection, primary undetectability, zero epsilon-prime term,
an exact final d8 criterion, zero incoming d5, and the complete next
two ordinary homology source groups. These are advances on the open
requested item itself. The main accessibility question B remains
proved. The two requested rows D.2.4 and D.3.2 remain Open.

At this checkpoint the new 71-class Steenrod input has produced a
positive finite Adams boundary test: the proposed bottom h0h3 class
is a nonboundary, with an explicit dual functional and Ext dimension18.
The generic engine has passed root review and exact self-tests. The
actual geometric input is undergoing independent full review and is
NOT promoted to a theorem in this archive. The certificate may reduce
to a four-dimensional cyclic cohomology submodule; that simplification
is also under review. Next steps are to finish the operation-model
audit, prove the finite-stage Adams implication with exact sources,
and then attack the final d8/source-changing problem. A parallel actual
James--Hopf calculation retains its explicit higher-cell boundary.

Checkpoint16 contains the verified256-page PDF,147 numbered rows,
121 printed references, every authored note, program, output and build
log currently saved. Its six new numbered statements were fully
reviewed and visually verified before archiving. Candidate code and
its pending topological interface remain distinguished in the notes.
Raw downloaded references and attachment reproductions remain excluded
under the established archive rule. The next progress assessment and
checkpoint are due at approximately02:57UTC.

## 02:11 UTC — D.2.57 integrated and visually verified

The new theorem proves both remaining incoming stable AHSS maps d6
and d7 zero, so the target of the final d8 is exactly Z4. Its proof
uses the actual four-class cyclic Steenrod submodule in degrees
7,9,11,13, including an explicit primitive Newton correction detecting
the last class. Restriction to an ordinary finite fourteen-skeleton
gives the required comodule quotient without a minimal-CW assumption.
The complete thirteen incoming cobar columns and the eleven-term dual
functional are printed. Sphere naturality, the zero degree15 source
and connective Adams convergence prove survival of the specified
doubled sigma. Root and both independent mathematical readers passed
the entire geometric, algebraic and convergence argument.

The rebuilt PDF has260pages and148numbered rows:132 Proved,
12 Refuted,2 Open and2 separately qualified refutations, with
122 printed references. The new Milnor reference and the expanded exact Adams opening record are
included. The build log has zero overfull boxes, zero missing
characters and no undefined citations. Root rendered and visually
read all four proof pages163--166, including both complete tables;
there is no clipping or equation-tag collision.

The original requested D.2.4 and D.3.2 rows remain Open. A subsequent
full-target extension now has an independently checked symbolic
certificate: the extra operation Sq2 Z13 is Sq1 of an actual class
ell14, permitting one extra functional term. Its full-target Adams
consequence still allows an incoming d2 from filtration zero, unlike
the finite-skeleton theorem. That extension is being drafted
separately; neither the final stable d8 nor h has been evaluated.

## D.2.58 integrated after the full-target audit

The symbolic extension is now a proved numbered result. Its actual
degree14 class ell is detected by an explicit primitive cover class;
the top Bockstein gives Sq1 ell=Sq2 Z on all of L. A short two-bar
argument proves the required degree15 cohomology-suspension injectivity
without assuming a new cover edge range. Adding the single
[xi1|xi1] ell term to the finite certificate annihilates every full
cobar-one column. This proves the full-target h0h3 Ext class nonzero,
while explicitly retaining its possible incoming Adams d2. The
geometric hand normalization also passes the independent166-column
matrix check. Root and both independent mathematical readers passed
all parts of the proof.

The rebuilt PDF has262pages,149numbered rows and122printed references:
133 Proved,12 Refuted,2 Open and2 separately qualified refutations.
The build again has zero overfull boxes, no missing characters and
no undefined citations. Root rendered and visually read166--168,
covering the entire new claim and proof; all displays and file paths
fit, and there are no tag collisions. The two original open items
remain Open. The next concrete work concerns the seven potential
filtration-zero sources, their integral Bocksteins, and the actual
secondary differential, with an independent unstable James--Hopf
calculation continuing in parallel.


## D.2.60 integration and visual verification — 16 November, 02:40 UTC

The actual auxiliary James--Hopf survival theorem has passed root review
and has been integrated with its exact source comparison. The rebuilt
PDF has265pages,150numbered rows and123printed references:134Proved,
12Refuted,2Open and2qualified refutations. The build log records zero
overfull boxes, zero over2pt, zero missing characters and no undefined
citations. Root rendered and actually viewed pages168--171, including
both attaching matrices, the quotient calculation and the final kernel
argument. All are legible and free of clipping or equation-tag collisions.
The first statement starts at the foot of page168 and continues normally
on169. The original D.2.4 and D.3.2 remain Open.


## D.2.59 and D.2.61 integration and visual verification — 16 November

The integral-source theorem and the full secondary-operation calculation
have passed independent review. D.2.59 proves dimensions47 and33 for the
next cover and target homology groups, the seven-dimensional primary
space, and integral lifts of every primary class. Six explicit integral
double suspensions give its half-product kernel. D.2.61 proves the exact
bar-cycle/Adams differential pairing using coherent GEM tracks and the
actual universal secondary representative. It closes the specified
Moore obstruction: h_Ml4=0 and alpha sigma-prime has exact order2.
These results do not settle D.2.4 or D.3.2.

The rebuilt manuscript has272pages,152numbered rows and125printed
references:136Proved,12Refuted,2Open and2qualified refutations. The
first build had one overfull display,108.65695pt wide, in the new
double-bar quotient. Splitting that display gave zero overfull boxes,
zero over2pt, zero missing characters and no undefined citations.
The initial page image is retained. Root rendered and actually viewed
pages168--172 and175--178 of the corrected build, covering every new
proof page and the repaired display. They are legible, with no clipping
or equation-tag collisions. The explicit bar-resolution realization
and the source-dependent track term are printed in full.

A current-status paragraph now precedes the long obstruction calculation
so that earlier intermediate statements are read with the endpoint
proved in D.2.61. All earlier notes, failed attempts and finite certificates
are retained. The original two Open rows remain Open.


Root additionally rendered and viewed the current-status paragraph on
page30 and the two new source entries on pages254 and257. They also
fit cleanly. The exact Serre locator in D.2.61 is corrected to printed
pp204--205 (Theorem4 on205), verified again against the opened original
scan; the earlier off-by-one working-note locator is corrected.


## Seventeen-hour assessment — 16 November 2026, 02:57 UTC

The main Parts A/B result remains proved. The original requested rows
D.2.4 and D.3.2 remain Open; this checkpoint is INCOMPLETE.

The last hour made direct progress on the active D.2.4 construction.
D.2.57 and D.2.58 removed the lower stable differentials and established
the full-target Adams class. D.2.59 completed the seven-dimensional
primary source calculation and all integral lifts. D.2.60 proved actual
auxiliary survival through every twelve-cell. D.2.61 then closed the
remaining secondary-operation comparison, proved the whole final stable
d8 zero, and determined the actual Moore composite h_Ml4=0 and the
related sphere composite to have exact order two. The known detecting
integral cycle is now proved stably spherical. The comparison is backed
by opened primary proofs, an explicit coherent-track derivation, a
four-term certificate against all166 incoming columns, and independent
full-proof audits. This is a substantive completion of the particular
homotopy calculation, not a resolution of the original localizer item.

The next concrete test has changed accordingly. A possible finite
relative correction must factor through the actual quotient Q=D/y_D.
The saved source calculation gives an order-two top attachment, a free
integral top class and only even spherical Hurewicz image. A compatible
integral cochain calculation reduces vanishing of its target functional
on all integral classes to the restriction of one specified order-four
class D16 to Y<10>, equivalently its membership in the image from the
actual nine-type. The value of that restriction and the realization of
a detecting class by a Q-map are still unproved. The newly stable
θ-detecting sphere does not itself supply that map. Those exact limits
are retained in the working notes.

The progress condition is met: the active obstruction was evaluated,
and the next finite obligation is explicit. Work therefore continues
on that obligation. Arbitrary full-source extension, persistence through
all nullification stages, the zero-finite-part nonfixed example and the
fixed-stable-part interval/set-size question are not declared finished.

Checkpoint17 contains the verified272-page manuscript,152statement
rows,125printed references, all authored code, finite certificates,
source audits, notes and build/visual logs through this hour. Counts are
136Proved,12Refuted,2Open and2qualified refutations. The final build has
zero overfull boxes and no missing characters or undefined citations.
Original attached materials and third-party scans remain excluded by
the documented checkpoint rule; no authored work is omitted.
