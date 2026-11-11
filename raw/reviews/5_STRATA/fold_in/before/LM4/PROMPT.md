# LM4_FINITE_GROUP_ACTIONS: finite groups acting on surfaces and on groups with loops (§§12–18, 23–25 bis, 31)

DRAFT, provisional (11 November 2026). Development prompt for Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981). File prefix for your deliverables: `LM4_FINITE_GROUP_ACTIONS`.

## What is to be settled

In §12 Grothendieck convinces himself that, in the anabelian cases, the whole system of groupoids attached to a curve with marked points can be expressed by an *exterior group with loops* ("groupe extérieur à lacets"): the fundamental group `π` with the conjugacy classes of its loop subgroups `L_i`. From there to §31 he studies a finite group `Γ` acting on a surface, or acting exteriorly on `π`, discrete or profinite, with two operations: filling holes ("bouchage") and drilling holes ("forage de trous"). His aim is stated at 140-2 scans 270–271: the 2-functor from topological `Γ`-actions on surfaces to the group-theoretic data should be a 2-equivalence, "i.e. 3-fidèle". What he asks, in his order:

1. Rigidity of the loop structure: centralizers and the centre are trivial, conjugators are unique, `Norm_E(L_i) = E_i`, `Trans_E(L_i^d, L_i) = E_i`, the Hom-categories are discrete (scans 53–54, 62, 69, 84); in the profinite anabelian case "pas prouvé pour le moment dans aucun cas" (scan 118, margin).
2. §15 and §17: critical orbits of splittings; fixed points against classes of sections, "Cette application est-elle bijective ??" (scan 139); the "lemme fondamental" and its expected validity in the two abelian cases; the abandoned theorem "Ultra fort" and the lemma he marks "faux !"; "Ça doit être le seul contre-exemple" (scan 179).
3. The invariant `μ` on elements of finite order (scans 155–160): "J'ignore si cette application μ peut se définir intrinsèquement"; the torus case.
4. Questions c), d), e) of scans 197–198: is `π^Γ = 1` for finite `Γ ⊂ Aut_lac(π)`; a unique maximal section subgroup (his proof, scans 201–203); finitely many classes of lifts. He reduces c) and e) to realizability of cyclic outer actions.
5. Essential surjectivity, "un problème ouvert sur lequel les gens sèchent" (scans 101–102), and the realizability criterion of scan 294: a faithful outer action is realizable if and only if, after drilling holes, it lifts to an admissible action whose extension is a group with loops; the bijection (∗) of scans 289–290; `Π_1^Γ = 1` (288), `H^1(Γ, B^0) = 1` (285); the theorem of scan 304, `π_0(SA_{g,ν}) ≅ SΓ^{!+}` with `(SA_{g,ν})^0` ∞-connected; "Le plus agréable serait que ce soit un homotopisme" (281); the programme of scans 292–293 (cyclic groups first, then dévissage).
6. "Toute extension sans torsion d'un groupe fini par un groupe à lacets est (canoniquement) un groupe à lacets" (scan 353), and the relèvements of §31, with "conjecturer sans vergogne" for the profinite classes of lifts.
7. §25 and §25 bis: the special Teichmüller groups and the case of two groups of operators.

## Leads (unverified; prove or refute each)

- **Lead 1.** Essential surjectivity in the discrete case is the Nielsen realization problem, solved by Kerckhoff (1983); contractibility of the identity components is Earle–Eells and Hamstrom. What Grothendieck states beyond this, and what does not seem to be in the literature as a statement, is the 2-categorical form: an equivalence between the 2-category of surfaces with `Γ`-action (isotopies as 2-arrows) and a 2-category of exterior groups with loops with `Γ`-action.
- **Lead 2.** His "forage" criterion is a form of the Birman–Hilden correspondence together with the theory of Fuchsian and NEC groups; the torsion-free extension statement in the discrete case is the classical theorem that a torsion-free finite extension of a surface group is a surface group (Zieschang; Eckmann–Müller for the closed case), and with loops kept, its relative form.
- **Lead 3.** The profinite counterparts (triviality of centralizers of open subgroups; normalizers of the `L_i`; finite subgroups of the profinite completion and their conjugacy to discrete ones; the profinite realization statement) are partly theorems (Nakamura; Anderson; Bridson–Conder–Reid and others for Fuchsian groups) and partly open; the profinite torsion-free extension statement is, as far as I know, open in general.

## After the first Dérivateurs return (added 11 November 2026)

Package CATHOT of the companion work on *Les Dérivateurs* has been answered (GPT-6 Astra, ChatGPT Pro mode). The statements below are from that answer; those marked *checked* were followed step by step by the author of this prompt. The named sections of that answer are attached.

- **What the group-theoretic side of the 2-functor can see** (CATHOT C.1–C.4, B.11; *checked*). Categories and functors modulo zigzags of natural transformations represent homotopy classes of maps into 1-types and nothing more, and the reflection onto them is the fundamental groupoid. Surfaces of the anabelian types are 1-types, which is why his passage from surfaces to exterior groups with loops loses nothing at the level of objects and arrows; the 2-arrows (isotopies) are where a statement beyond this is needed. In Part C, say exactly which level of the mapping spaces of the homeomorphism groups each of his fidelity conditions concerns ("3-fidèle" in his usage), and where the excluded types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)` fail because the surface, or the identity component of its homeomorphism group, is not a 1-type or not contractible.

### After GALOIS (added 11 November 2026)

Package GALOIS of the companion work on *Les Dérivateurs* (locally constant coefficients) has been answered (GPT-6 Astra, ChatGPT Pro mode). Its statements are cited by their numbers; the author of this prompt has read them in statement only, and the review is not finished: verify what you use. The named section is to be attached under `GALOIS_return/`.

- **A ladder of levels to state the fidelity conditions against (Part C).** GALOIS C.4–C.5: for a map of spaces `v` and coefficients in `r`-truncated spaces (`r = 0`: sets; `r = 1`: groupoids), restriction of locally constant coefficients along `v` is (i) bijective on morphisms between constant coefficients iff `v` is an isomorphism on `π_i` for `i ≤ r`; (ii) fully faithful iff moreover `π_{r+1}(v)` is onto at every base point; (iii) an equivalence iff `π_{r+1}(v)` is an isomorphism. All three inclusions are strict, and the middle class fails two-out-of-three (`* → K(A, r+1) → *`). So "faithful", "fully faithful" and "equivalence" at the level of locally constant `r`-types are three different conditions on `π_{≤ r+1}`. When you say which level of the mapping spaces each of his conditions concerns ("3-fidèle" in his usage), place it on this ladder for `r = 0, 1, 2`, or say why it is not of this form.
- Nothing in the leads of this prompt is refuted or settled by GALOIS.

## Parts

**A. Groups with loops.** Give the definition (discrete and profinite; exterior version), his list of rigidity statements with exact hypotheses, and for each a proof or a citation with the theorem number, the excluded types named. Settle item 1 completely.

**B. The discrete theory, §§15–18.** Every statement and question of items 2–4, in his order: proved, refuted or corrected, with the classical theory of group actions on surfaces as the tool. For `μ` (item 3): decide whether it is intrinsic to the extension, and compute the torus case he begins.

**C. The 2-equivalence.** Define both 2-categories exactly (objects, arrows, 2-arrows; what "3-fidèle" means in his usage), state the 2-functor, and prove or refute that it is a 2-equivalence, first for `Γ = 1`, then for finite `Γ`. Prove the theorem of scan 304 and the realizability criterion of scan 294 in their strongest correct form, and decide the bijection (∗). Say what the homotopy statement of scan 281 should be and prove it.

**D. The profinite theory.** For each statement of Parts A–C say what its profinite counterpart is, in his formulation (§31 and the passages marked "admis dans le contexte profini"), and prove, refute or leave open with the exact obstruction. Item 6 in both settings. Give the smallest undecided instance of profinite realization.

**E. §25, §25 bis.** The special Teichmüller groups and the two-group case: definitions, the statements he makes, their proofs.

**F. What follows.** State the consequences he draws later from this part (in §§26–30 for the discretifications, and in §33 for anti-involutions) as lemmas in the form those sections need, so that packages LM3_TEICHMULLER_TOWER and LM6_POINTS_AS_SECTIONS can cite them.

---

THE TEXT YOU ARE GIVEN
- Grothendieck wrote *La Longue Marche à travers la théorie de Galois* by hand between January and June 1981. It was never prepared for print. What is attached is a transcription of the manuscript made by AI from scans (first pass: GPT-6 Astra, ChatGPT Pro mode; second pass, line by line against the scans: Claude, Anthropic), by package. The manuscript is in four archive files: cote 140-2 (folios 1–292, §§1–37), cote 140-3 (folios 293–650, §§38–49), cote 140-4 (folios 650bis–787, §§50–53) and cote 140-1 (a draft of 37 scans). `\scanpage{n}` marks the scan, `\mspage{n}` his folio number.
- Marks in the transcription: `\unsure{a|b}` a doubtful reading with its alternatives; `\illegible{n}` unread words; `\deleted{…}` struck by the author; `\inserted{…}` added by him; `\margin{…}` a marginal note. A reading is never final. Where your mathematics depends on a doubtful or unread place, say so at that place, work with each alternative that makes sense, and report which one the mathematics supports as evidence for the editors, with the scan number. Do not silently choose, and do not call any reading settled. The scans of the pages that matter are attached: look at them.
- His notation changes as he goes, sometimes within a section ("Notations définitives (?)", §46). Fix yours on the first page with a table giving, for each symbol you use, his symbol and the scan where he introduces it.
- He marks his own doubts ("un peu faux", "ultra-faux", "sauf erreur", "peut-être est-ce tout à fait faux ?", "Théorème (!)"). These are part of the text: a statement he doubts is treated as a question, one he withdraws as withdrawn.

WHAT IS ATTACHED
A zip with: the transcription packages listed in the manifest (the current text of each), the scans of the pages named in this prompt, his table of contents, the checked research notes of those packages (notes by the transcribing models on his conjectures, unproved claims and unpursued implications; drafts, not authority), the background papers, and `OVERVIEW.md` (a reading of the whole manuscript by Claude, from which the leads below come).

RULES OF PROOF (they bind every statement you deliver)
1. State the actual claim with all its data: which group (discrete, profinite, pro-ℓ), which field, which type `(g, ν)`, outer or genuine actions, base points and the choices they involve, which topology, which of his numbered conditions in which version. Do not replace it by a convenient special case; if you prove a special case, name it as one and keep the general statement on your list as open.
2. Type every map: source, target, the category in which it is a morphism, and each property you use (continuous, open, compatible with which outer action, defined up to which inner automorphisms).
3. Every reduction ("we may assume", "pass to an open subgroup", "fill the holes", "replace by a covering") comes with its comparison map and a proof that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: a homomorphism and its class modulo inner automorphisms; an isomorphism and a canonical isomorphism; injective, with open image, bijective; a discrete group and its profinite completion (and say when the completion map is injective); a statement over `Q` and over a finite extension.
5. Check the cases he sets aside or forgets: types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)`; `(0,3)` and `(1,1)` against the general anabelian type; residue characteristics 2 and 3; non-orientable and real cases; trivial and non-trivial centres.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you attach. One verified counterexample refutes the statement: say "false", and then find the strongest true statement in its place. An invalid proof alone shows a gap, not falsity.
7. No authority. His assertions, the notes of the transcribing models, and the leads marked "Lead" below (inferences by Claude from one reading, checked by no one) are all to be proved or refuted. If a lead is wrong, say so plainly.
8. Later work (Belyi, Drinfeld, Ihara, Nakamura, Matsumoto, Tamagawa, Mochizuki, Pop, Hoshi, Boggi and others) is to be used, with exact theorem numbers, wherever it proves or refutes what he asks. The task is to do the mathematics he set out, with everything now available, and to carry it to where it stops; it is not a survey. Never invent a reference; mark each bibliography entry `verified` (you opened it) or `unverified`. Before calling anything new, say what you searched.
9. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the smallest undecided instance.

WHAT TO DELIVER
One ZIP containing:
- `<ID>_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the parts, every statement numbered and labelled Proved / Refuted / Known (with citation) / Open, with complete proofs; each statement that answers a passage of the manuscript cites it by section, folio and scan. English, first person plural, the register of a careful research paper; quote Grothendieck in French where his wording matters, and never write in his voice. This text is meant for a book that reproduces his text and builds it out; how it will be placed there is not decided, so make it readable on its own.
- `<ID>_results.csv`: one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_passages (section; folio; scan), depends_on_doubtful_reading (scan, alternatives), notes`.
- `<ID>_readings.csv`: every place where the mathematics bears on a doubtful reading: `package, scan, the \unsure or \illegible place, what the mathematics supports, how strongly`.
- `<ID>_references.bib`, `<ID>_report.md` (what you read, what you computed, corrections to the leads and to the notes, what remains open), and `code/`.
The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and claim no priority.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go.
