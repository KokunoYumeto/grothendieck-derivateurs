INCOMPLETE

# S2COUNT work report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026. No priority is claimed; no mathematical authorship is attributed to any person.

Work began at approximately 05:39 UTC. Checkpoint 01 was saved at 06:39 UTC and checkpoint 02 at 07:39 UTC. The three-hour progress assessment was made at 08:39 UTC; checkpoint 03 is the scheduled third-hour snapshot. The final package follows that assessment and is explicitly incomplete in E2–E4.

## Scope and progress

The full attached prompt is being addressed. Primary effort: settle countability of [BC,S²] on finite categories. The monoid homotopy type, the dimension-two resolutions, and other targets/ind-representations are investigated in parallel.

| Item | Current state | Result or remaining issue |
| --- | --- | --- |
| A1 | Proved and independently checked by program | Ring basis, integral resolution, retraction, explicit cup primitives |
| A2 | Proved | Explicit sphere maps induce a primitive integral basis and a wedge equivalence |
| A3 | Proved | Two-object Karoubi model and Quillen-A comma contractions |
| A4 | Proved | Second example is a wedge of 2^(n−2) spheres in degree n |
| B1 | Proved | R2 checked; return-degree extension and finite-domination case written |
| B2 | Proved | Exactly continuum many maps to S³ and S² |
| B3 | Proved | Six arrows suffice and are necessary; independent complete enumeration through five |
| C1 | Proved | Exact componentwise Postnikov criterion, including arbitrary finite complexes |
| C2 | Proved | Countable locally finite representatives characterized; finite representatives exactly finite groupoid types |
| C3 | Proved | Explicit finite stages with S² colimit; comparison fails injectivity for every stipulated source |
| D | Proved | Specified manuscript pages corrected, with all used R1 and R5 transfer proofs audited |
| E1 | Audited | Complete equation-theorem source and every requested INDLOCAL assertion checked |
| E2 | Undecided | Countable-quotient obstruction or construction |
| E3 | Undecided | Intermediate cardinal bounds |
| E4 | Undecided | Arbitrary rank in dimension two |
| E5 | Proved in the full B.7 scope | Two-dimensional group tests miss S³ at every bound; the S²-only refinement inherits E2–E4 |

## Deliverable and verification policy

Every proved or refuted numbered statement receives a row in `S2COUNT_results.csv`. A conditional statement remains explicitly conditional. Finite computations are independent checks, never substitutes for an all-degree homotopy proof.

The PDF builds with LuaLaTeX. Checkpoint 01 contains the first integrated 32-page version. The initial build had one overfull box of 9.6264 pt in a theorem heading; splitting the heading removed it. That version was rendered throughout, with four contact sheets and full-size pages 8 and 31 visually inspected; its record is `logs/checkpoint_01_pdf_qa.json`.

Checkpoint 02 has 37 pages, 79 result rows, and 27 bibliography entries (18 cited in the paper). Its build has zero overfull boxes, zero undefined references, and zero undefined citations. All pages were rendered and five contact sheets spanning the document inspected. Full page images 35 and 37 were also inspected. Compacting the bibliography removed a nearly empty final page; the affected final sheets were rendered and inspected again. No clipping, overlap, missing glyphs or protruding displays were observed. The structured record is `logs/checkpoint_02_pdf_qa.json`.

The final expanded manuscript has 42 pages, 85 result rows, and 35 bibliography entries (21 cited; 34 entries marked verified and one exploratory entry marked unverified). The latest LuaLaTeX log has zero overfull boxes, zero undefined references, zero undefined citations, and zero missing-character warnings. Every page was rendered; all five contact sheets were inspected, and the final pages 40–42 were also inspected at 120 dpi. A smaller bibliography font removed a nearly empty 43rd page; the affected pages were rendered and inspected again. No clipping, overlap, missing glyphs, or protruding displays were observed. The final visual review, exact PDF hash, and build counts are in `logs/checkpoint_03_pdf_qa.json`. The environment uses a private generated TeX format and Type 1 font map; the reproducible build script changes no system files. The complete overflow history is one initial 9.6264 pt box, repaired before checkpoint 01, and zero in each subsequently delivered PDF.

## Approaches and exact obstacles

Main question settled: write e=x00, a=x10−e, b=x01−e, t=y−e. An integral idempotent decomposition of ZM gives an all-degree projective resolution. For every word w in the nilpotent letters the bar cycle [b|t_w|a] is realized by a sphere obtained as the join of a two-edge circle with zero-spheres. Explicit integral cocycles pair as the identity matrix, proving these spheres induce a primitive homology basis. Their wedge map is a homotopy equivalence by the simply connected homology Whitehead theorem. This gives BM≃∨_{n≥2}S^n and continuum many maps to S² and S³.

Initial countability observation: the ordered-product argument in OWN_RESULTS Proposition 4.1 is valid after pointed cellular choices; coprime degrees suffice. This does not establish that the candidate meets the hypothesis.

The candidate now meets that hypothesis by the explicit wedge equivalence. The integral cup primitives also establish all products without relying on the homotopy identification. All positive Steenrod operations and all ordinary triple Massey products vanish.

The independent C++ enumeration of connected categories through five arrows confirms the exact structural alternatives used in the lower-bound proof. Counts use normalized source--target blocks. The one-object labelled counts are 1, 2, 11, 156 and 4122; the two-object counts at 3, 4 and 5 arrows are 2, 11 and 76; the three-object count at 5 arrows is 6.

E investigation: the uncountable simple locally free group route fails. A nontrivial locally free perfect group cannot be finitely normally generated (Magnus-degree argument); a simple group would be normally generated by any nonidentity element. The known general dimension bound for uncountable locally free groups also does not supply an actual two-dimensional model.

The remaining E2 problem is exact: construct an actual two-dimensional K(G,1) with H₁(G;Z)=0, H₂(G;Z)=Z and no nontrivial countable image, or prove such a group has a nontrivial countable image. The finite-bound construction works, and the audited residual-cardinality theorem rules out every bound at least the continuum. The interval ℵ₀≤μ<2^ℵ₀ remains undecided here; CH reduces it to the single bound ℵ₀ without deciding it. For infinite rank κ, existence is established for μ<κ and nonexistence for μ≥κ^ℵ₀; the interval κ≤μ<κ^ℵ₀ remains undecided. Rank zero admits all bounds. If κ^ℵ₀=κ the answer is exactly μ<κ.

Additional obstruction lemmas have been proved during this investigation. A cyclic cover of an actual two-dimensional classifying space has H₂ free over Q[t,t⁻¹], which prevents an uncountable H₂ rank from being compressed to finite rank by a semidirect-product shift. Also, the pointwise finite normal-generation norm in INDLOCAL A.31 prevents ordinary countable equation compactness: an essential countable subgroup of an ultrapower supplies a countable, finitely solvable but unsolvable equation system. Its exponent rows need not be independent, so this does not supply the nonsingular acyclic extension needed to decide E2. Both proofs and the precise limitation are in Statements E.11–E.12.

The later statements isolate further failures of proposed shortcuts. An integral identity exponent matrix does not imply asphericity: a balanced presentation of the binary icosahedral group gives a finite counterexample (E.13). Klyachko's simplicity theorem blocks proper simple extensions by one unimodular generator–relator pair, and the coefficient-quotient preservation theorem prevents repairing the resulting old normal distinctions by later homology-equivalent attachments (E.14). A small-retract theorem for sparse presentations excludes uncountable Higman-graph constructions with small H₁ and H₂ (E.15).

The finite-rank normal-subgroup restriction is stronger: if N is perfect and normal in a group G with an actual two-dimensional classifying space, and H₂(N;Z)=Z^r for 0<r<∞, then G/N is finite, acts faithfully on H₂(N), and has order dividing r+1 (E.16). For r=1 and G perfect this forces N=G. Passing from a countable homology core to its normal closure cannot be assumed to retain rank one: its disjoint lifts already contribute a copy of Z[G/N]⊗H₂(core). The proof treats arbitrary free cellular ranks without cancelling infinite dimensions. These restrictions do not produce either the group required by E2 or a countable quotient of every candidate.

Statement E.17 advances the countable diagonal beyond the previously audited classes. If a remaining simple group has pointwise finite normal-generation norm N and, for some d≠1, conjugates of elements in the ball N(c)≤2N(d) admit a uniform bound on the N-length of their conjugators, an explicit fixed-ball tree system excludes that group. Its extension is proved to be normally generated by the old coefficient group, homology equivalent to it, and to have an actual two-dimensional aspherical model. It adds only countably many cells. Thus the diagonalized candidate can exclude this further class. A surviving countable simple image must fail that bound for every d≠1; the element c can vary with the requested conjugator bound. No assertion of transport failure within one fixed conjugacy class is made.

The auxiliary Farjoun–Orr–Shelah audit identifies a literal one-pass existence-closure error and gives a finite, independently checked counterexample. The main unique-solvability localization theorem has a repair, described in `notes/CD_E_FDOS_one_pass.md`; it is not rejected. The source does not close the independent-row and asphericity gaps in E2. The complete nonsingular-systems preprint was independently reread by two agents, with the root check completed by 07:08 UTC.

The third-hour additions strengthen the obstructions without closing E2–E4. Statements E.18 and E.18a extend the normal-subgroup restrictions to arbitrary second-homology rank: finite positive rank forces finite quotient, infinite rank bounds the quotient cardinal by that rank, and a perfect normal subgroup gives a faithful action on its nonzero second homology. These facts do not show that a countable homology core has a small normal closure.

The literal Corson–Obraztsov Jónsson presentation has second homology of rank equal to its infinite generating cardinal (E.19). Three relator families have affine exponent vectors and give an explicit independent second-difference cycle for each of that many disjoint factor pairs. The source-specific weak asphericity argument and 108 finite parameter checks are retained. This identifies why that presentation does not furnish rank-one homology; it is not a claim that every Jónsson construction must have the same obstruction.

E.20 proves that every Higman-group homomorphism into the group of increasing, piecewise linear, bi-Lipschitz homeomorphisms of the line with locally finite breakpoints is trivial. Thus the A.28 group, normally generated by images of Higman groups, has no image there. This does not exclude all groups of homeomorphisms of the line, or all left-orderable groups. E.22 proves the corresponding exclusion for automorphism groups of locally finite simplicial trees, using adjacent fixed points and a least-prime orbit argument. Local finiteness is essential; no property-FA assertion for arbitrary trees is made.

E.21 gives a new normally generating quotient obstruction with an exact homology cost. Given a perfect group P with an actual two-dimensional classifying space and a nontrivial epimorphism q:P→E to a countable group, a countable sequence of injective cyclic HNN extensions produces P⊂G, normally generated by P, with H₁(G)=0 and H₂(G)=H₂(P)⊕Z, such that q has no extension to G. The presentation and every HNN endpoint are explicit. Its final HNN tail kills the successive primitive first-homology generators while preserving H₂. The independent additional H₂ class is not removable by later two-dimensional subcomplex attachments. Beginning instead with a first-homology reservoir can defer that cost, but the reservoir vanishes at a countable limit; it does not support the required uncountable iteration at fixed H₂ rank. The earlier fresh-Higman closure is superseded by the normally generating HNN tail; the exact earlier checkpoint passages remain preserved.

The colored-tree investigation gives concrete boundary examples. Countable simple groups can simultaneously contain a prescribed countable subgroup, satisfy a mixed identity, and have pointwise finite but globally unbounded canonical normal-generation norm. Seeded coherent branch swaps yield an explicit exponent-one equation with no solution: it would require a cube root of a single branch three-cycle. Thus these examples fail the unimodular solvability required of a residual A.28 target. The precise countable extraction and source hypotheses are in `notes/A_E_attempts.md`; this is not a classification of every subgroup of the tree automorphism group.

The checked graphical small-cancellation constructions of Brown–Leary allow homology-preserving acyclic-kernel quotients in actual dimension two, but their relevant groups have uncontrolled H₂. Their more homologically finite variants supply actual geometric dimension two only in the stated special case; cohomological dimension two is not substituted for geometric dimension two. The Eilenberg–Ganea preprint found during the search is marked unverified and is not used. Further simple-envelope and strongly bounded constructions likewise add large H₂. The corresponding source scopes and attempted modifications are preserved in the research notes.

The exact next steps would be: (i) convert the essential pure extension into an actual two-dimensional relative homology equivalence, without dependent exponent rows; (ii) prove fixed-ball word coverage or another repeatable diagonal invariant in the unbounded conjugator-transport branch; or (iii) arrange homology-preserving quotient replacements with an actual two-dimensional model at the uncountable limit. None of these bridges has been established. Mere finite solvability, ordinary nondiscrete metrizability, or a list of homology groups is insufficient. These are unsolved proof steps, not claims of independence or proofs that the desired resolution cannot exist.

## Exact unresolved cardinal ranges

Write c=2^ℵ₀ and let κ be the rank of H₂ of the simply connected two-dimensional target. Every such target is homotopy equivalent to a wedge of κ two-spheres.

| Rank κ | Existence proved | Nonexistence proved | Undecided here |
| --- | --- | --- | --- |
| 0 | Every μ | None | None |
| 0<κ<ℵ₀ | Every finite μ | μ≥c | ℵ₀≤μ<c |
| κ≥ℵ₀ | μ<κ | μ≥κ^ℵ₀ | κ≤μ<κ^ℵ₀ |

If κ^ℵ₀=κ, the infinite-rank row is complete: exactly μ<κ. CH makes the finite-positive-rank undecided interval consist of μ=ℵ₀; it does not decide that remaining case. No independence conclusion is claimed. The first unresolved instance is κ=1, μ=ℵ₀. E5 is settled negatively for replacing the full B.7 tests for arbitrary target types, since every map from a two-dimensional classifying space to S³ is null-homotopic. Any S²-only testing improvement requires the strict size window μ<|G|<κ and retains the gaps above.

## Three-hour progress assessment and stopping decision

At 08:39 UTC, the main question and A–D are settled, and all requested E1 audits have complete arguments at the cited locations. E2–E4 remain undecided in the ranges above. The third hour produced actual mathematical advances in the local obstruction theory: E.18–E.22, the normally generating HNN repair, and the exact exclusions of several proposed target families. None supplies the missing homology-preserving block or a universal countable-quotient theorem. By the assessment time, all three investigations independently found no concrete mechanism carrying the current work across that gap; further special-family exclusions would presently be peripheral to the unresolved existence question.

I therefore apply the user's explicit three-hour progress rule and stop the extended investigation here. This is a deliberately incomplete return under that stopping rule, not a claim that E2–E4 have been decided or shown independent. The report begins with INCOMPLETE; every undecided task remains marked in the register. The exact next proof steps, unsuccessful approaches, and smallest undecided instance are preserved. No environment failure or time-limit termination is asserted.

## Exclusions from the package

The user-supplied background archive and its extracted contents are inputs and are excluded from checkpoints and the final deliverable, as requested. Generated notes, scripts, outputs and build logs will be retained.

Full-text copies of public research papers downloaded during the investigation, and text extracted from the supplied Hatcher book, are omitted from delivery. Their exact URLs and verification locations are retained in the bibliography and source manifest. These are reproducible source inputs, not authored proof notes. Checkpoint 01 is the complete first-hour snapshot. Its package manifest lists all omitted source inputs.

Two such source files were inadvertently included in checkpoint 02 and are explicitly omitted from subsequent archives: `notes/E_KlyachkoMikheenkoOlshanskii_v3.pdf` and `notes/E_KlyachkoMikheenkoOlshanskii_v3.txt`. Reason: they are the full public preprint and its extracted text, duplicate source inputs rather than authored work. The exact source URL, version, bibliographic entry, and authored audit notes remain. Their checkpoint hashes and this omission reason are recorded in `logs/checkpoint_content_history.json`. No authored proof, note, script, output, report, or earlier PDF is omitted.

Before later packaging, `code/preserve_checkpoint_history.py` accounts for every file in each earlier checkpoint by content hash. An unchanged file remains at its working path; an exact superseded version is kept under `history/` and indexed in `logs/checkpoint_content_history.json`. The two explicitly listed public-source omissions are recorded with their reasons instead of copied. This preserves earlier authored proof passages, reports, PDFs, and QA images instead of silently replacing them.

## Checkpoint record

- 06:39 UTC: `S2COUNT_checkpoint_01.zip`, complete first-hour snapshot, 32-page PDF, 71 result rows. E2–E4 remain unresolved and research continues.
- 07:39 UTC: `S2COUNT_checkpoint_02.zip`, complete second-hour snapshot, 37-page PDF, 79 result rows. It includes the exact superseded checkpoint-01 files and their content-hash index. E.13–E.17 and E.16a are integrated; later Jónsson and transformation-group investigations remain separately recorded research work. E2–E4 remain unresolved.
- 08:39 UTC: `S2COUNT_checkpoint_03.zip`, complete third-hour snapshot, 42-page PDF, 85 result rows, 35 bibliography entries, and the three-hour assessment above. E.18–E.22 are integrated, with the strengthened normally generating E.21. All authored content from checkpoints 01 and 02 is retained by exact hash; the two public-source omissions are explicitly recorded. The final ZIP additionally preserves the content of this checkpoint and the upload records.
- Final delivery: `S2COUNT_final.zip`. The exact earlier-checkpoint preservation audit is in `logs/final_preservation_check.json`; the script checks every retained file hash and individually lists the two source omissions. The final archive receives a separate CRC and retained-content verification before upload.
