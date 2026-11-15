INCOMPLETE

# REVLOC research report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15 November 2026. No priority is claimed. This is an active research checkpoint, not a completed return.

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
| D.2 | Every thick finite subcategory occurs. Every nonzero torsion thick subcategory and the full finite category have accessible non-RT-fixed realizations. D.2.7 gives exact bounded-suspension ordinary-nullification tests; D.2.8 proves finite primary generators are RT-fixed; D.2.9 constructs a descending chain with common nonzero stable part and zero finite part, and computes its adjacent ordinary nullifications. | **Open:** zero finite thick part with nonfixedness. For `B = K(Fp,2)` and `A1 = Q Sigma B`, the concrete remaining test is whether `P_A1(Sigma^2 B)` is noncontractible. No strictness of the descending chain is asserted. Rational stable parts cannot provide a separator. |
| D.3 | No largest non-total reversible localizer. Every nonzero finite primary addition to the lower endpoint reaches the upper endpoint. Single Moore targets, all infinite identical Moore wedges, and all bounded-cardinality finite-dimensional target families give the same sphere-test interval element (D.3.3--D.3.6). | **Open:** set size at fixed stable part; whether the projective-space interval has more than two elements. In particular, strictness of the common sphere-test class over the lower endpoint remains unproved. |
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

## Computations

The programs in `code/` save exact data and assertions in `code/outputs/`:

- `CD_finite_checks.py`: all objects, arrows, composites and associativity checks for the 35-object/159-arrow acyclic category and the 16-object/68-arrow braid presentation category; integer boundary Smith forms; complete order-120 coset table and explicit generating matrices in `SL2(F5)`.
- `FGH_literal_axioms.py`: the finite degree-two sphere and Grothendieck-construction witness to failure of relative A.
- `EH5_fence_counterexample.py`, `EH5_trefoil.py`, `EH5_group_witnesses.py`: strict-fibre and coefficient/group counterexamples.
- `I_finite_checks.py`, `I_torsion_witness.py`, `I_fibrancy_checks.py`: beat cores, simple-collapse data, a nonzero Whitehead-torsion unit and finite attachment data, and the finite tree obstruction to fibrancy.
- `I_lie_moore.py`: two independent exact eleven-letter commutator computations; both generator matrices have raw counts `[[3125,3125],[3039,2460]]` and reduction `[[1,1],[1,0]]` modulo two.

The exact theorem statements explain which conclusions are mathematical proofs and which finite portions the programs certify.

## Approaches rejected or still under test

The following tempting shortcuts have been explicitly rejected: a space-level Kahn–Priddy section need not be an infinite-loop section; generator-nullity need not imply map-locality; stable membership need not imply unstable asphericity; a set of target spaces does not automatically yield an accessible localization; ordinary and strong resolving classes differ; a compactness proof in the homotopy arrow category cannot silently replace it by the arrow category of the homotopy category; full stable part does not imply totality; properness of a model category alone supplies the intrinsic fibration axiom, not an unproved higher analogue of every categorical fibration axiom.

For active approaches, failures and next steps see `notes/main_worklog.md`, `notes/FGH_report.md`, `notes/EH5_report.md`, and `notes/I_progress.md` as well as the open paragraphs in the manuscript. These are retained as work records and may be superseded by later proved sections.

The most recent direct attacks on D.2 and D.3 are recorded as follows. The classes generated by `Q Sigma^r K(Fp,2)` have an exact adjacent-nullification calculation, but the comparison of their reversible closures still requires a genuinely unstable test. Finite-type suspended Eilenberg--Mac Lane targets have no phantom maps from the indicated finite-type sources, but this does not prove that all actual maps vanish. Infinite products of suspended Eilenberg--Mac Lane spaces have not been shown to retain the required stable part; closure of a localizing category under such products cannot be assumed. For the degree-one Prüfer candidate, the stable ideal reduces to `loc(Sigma^infty CP^infty smash S/p)`; it has not been shown to contain a finite spectrum or to have zero finite part. None of these failed or incomplete approaches is counted as a separator.

## Typesetting and reproducibility

The LuaLaTeX installation had no generated format and no luaotfload module. A format was generated locally from the installed LaTeX sources; the manuscript uses Latin Modern Type 1 fonts with LuaLaTeX. `tools/build_pdf.py` records every compilation pass and the bibliography run. The first completed build is 68 pages. Its build log reports zero overfull boxes (therefore zero exceeding 2 pt), zero missing characters, and no undefined citations. The first successful layout pass also had zero overfull boxes; the before/after overflow counts are 0/0. Pages 1, 20, 40, 60 and 68 were rendered and visually inspected; margins, displayed mathematics, headings, citations and bibliography are legible with no clipping. No overflow pages required a separate inspection.

The second-hour build is 97 pages. Its final log again records zero overfull boxes, zero overflows exceeding 2 pt, zero missing characters, and no undefined citations; the before/after overflow counts are 0/0. The final-layout sample was rendered and inspected at pages 1, 23, 25, 26, 29, 37, 59, 72, 88 and 97, covering the new Moore proof and matrix, the stable-part reductions, the unit-fiber criterion, accessibility proofs, the manuscript comparison table and the bibliography. All are legible with no clipping. The intermediate 93-page version was also inspected at pages 20, 33, 68 and 83. No overflow page needed a separate repair.

The third-hour build is 111 pages. The preceding 110-page layout had two overfull boxes, of approximately 104 pt and 4.8 pt, both in D.3.5. The long equality was split into aligned lines, and the prose line was rewritten. The final build has zero overfull boxes, zero exceeding 2 pt, zero missing characters, and no undefined citations: before/after overflow counts are 2/0. Pages 30, 32, 33, 34, 35, 38, 39, 40, 41, 43, 44 and 111 of the final PDF have been rendered and visually inspected, including both repaired layout regions, the new nullification proofs, the unstable Moore tower and the bibliography. All are legible without clipping. The earlier spread across the unchanged parts of the document remains recorded above.

`tools/assemble.py` merges the owned bibliography fragments and records into the requested top-level files. `tools/source_crosswalk.py` regenerates the per-statement literature comparison. There are currently 98 numbered statements. Every bibliography entry records whether its primary text was opened and the theorem numbers used.

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
