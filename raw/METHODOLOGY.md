# How the research outputs on *Les Dérivateurs* were made

This is the account of the eight research prompts on Grothendieck's *Les Dérivateurs* whose raw outputs are in this
folder: what each prompt asked and what it attached, which model answered, how each answer was reviewed, and how the
open points of one answer were carried into the next prompt. Every file named here is published in this folder; the
paths are relative to `raw/`.

## The method in brief

1. **Questions.** The critical companion in this repository audits every chapter of the manuscript and lists the
   claims Grothendieck leaves unproved, conjectures or asks. Claude Fable 5.2 read the audited chapters and the raw
   text of some chapters not yet audited, and chose seven questions that a long run of a strong model could settle.
   That reading is [prompts/FABLE_PILOT_OVERVIEW_20261110.md](prompts/FABLE_PILOT_OVERVIEW_20261110.md); the index
   of the prompts, with their order and dependencies, is [prompts/README.md](prompts/README.md).
2. **Prompts.** Each prompt has two halves. The first, specific to the question, states what is to be settled, gives
   "leads" (the prompt author's own inferences, marked as unverified, to be proved or refuted) and divides the work
   into Parts. The second half is common to all prompts, [prompts/_COMMON_BLOCK.md](prompts/_COMMON_BLOCK.md): fixed
   conventions, nine rules of proof (state the full claim, type every map, give every counterexample completely and
   check it by a program when it is finite, keep open what is not settled, search the literature before calling
   anything new) and the deliverables: a paper in LaTeX with its PDF, in which every statement is numbered and
   labelled Proved, Refuted, Known or Open; a register of the statements (`<ID>_results.csv`); a report; a
   bibliography; and every program run, with its output.
3. **Attachments.** Each prompt went with a background zip: our LaTeX transcription of the relevant chapters, the
   companion's files for them, the background papers, and the reading the leads came from. For every prompt,
   `prompts/<name>/ATTACHMENTS.md` lists every file of the zip. Our own files link to where they are published (in
   this repository, or in `prompts/<name>/attached/` when they are not published elsewhere); papers by other authors
   are listed with their citation and address and are not re-published. `prompts/<name>/work/` holds the notes on
   why each item was attached (`BACKGROUND.md`), the zip's manifest (`MANIFEST.tsv`), the record of every change made
   to the prompt after an earlier answer came back (`CHANGES_20261110.md`), and earlier versions.
4. **Runs.** The user pasted each prompt into ChatGPT with its zip, one prompt at a time, and the model was
   GPT-6 Astra in ChatGPT Pro mode throughout. The answers are in `pro_returns/` as returned. The returns record no
   run time; the dates below are those on which each return was received.
5. **Folding in.** As soon as an answer came back, and before it was reviewed, its results were written into the
   prompts not yet sent, as a section headed "After <short name>" with a summary of what the answer claims, marked
   as unverified, and the questions it reopens. Each such step is recorded in
   `reviews/<name>/PROMPT_UPDATES.md`, with the inserted sections and the prompts as they were before in
   `reviews/<name>/fold_in/`.
6. **Review.** Claude Fable 5.2 then reviewed each answer statement by statement. Each review says what was read
   (which statements, which proofs in full), which proofs were followed step by step, which counterexamples and
   counts were reproduced by the reviewer's own programs (`checks_author/` or `checks/`, with their outputs; the
   programs in the answers were not run), which cited sources were opened, and which statements remain unverified.
   Its verdict words are defined at its head. Where a later prompt was still unsent when a review was finished, its
   section was updated to what the review found.
7. **Integration.** The reviewed results were then entered into the critical companion: claim rows updated, new
   commentary blocks with proofs added. [reviews/integration_20261111/INTEGRATION_LOG.md](reviews/integration_20261111/INTEGRATION_LOG.md)
   records every change, item by item, against the list at the end of each review; the scripts and new blocks are
   beside it, and `before/` holds every file as it was. These changes are in the working copy of the companion; they
   are not yet in the companion published in this repository.
8. **Record.** The reviewing sessions kept a running record of the whole series, in the order the answers came in:
   [reviews/KNOWLEDGE_HANDOFF.md](reviews/KNOWLEDGE_HANDOFF.md).

The prompts, reviews, records and scripts are published as they were written, with the user's first name replaced by
"user". The script that built the eighth prompt and its zip is [tools/build_8_RESIDUE.py](tools/build_8_RESIDUE.py);
it assembles `PROMPT.md` from `prompts/8_RESIDUE/work/PROMPT_head.md` and the common block, and the zip from the
manifest. The scripts that inserted the "After" sections are in `reviews/<name>/fold_in/`, and those of the
integration in `reviews/integration_20261111/`.

## Prompt by prompt

### 1. CATHOT: what categories modulo natural transformations can represent

- **Prompt:** [prompts/1_CATHOT/PROMPT.md](prompts/1_CATHOT/PROMPT.md). Asked: that the functor from small categories
  modulo natural transformations (`Cat hot`) to the homotopy category `Hot` has no right adjoint; what objects of
  `Cat hot` represent; finite tests; small models of spheres and projective planes. Attached:
  [prompts/1_CATHOT/ATTACHMENTS.md](prompts/1_CATHOT/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 10 November 2026. 90 statements by its own labels:
  59 Proved, 14 Refuted, 11 Known, 6 Open.
- **Review:** two reviews by Claude Fable 5.2. The first, by the author of the prompt
  ([reviews/1_CATHOT/REVIEW_author.md](reviews/1_CATHOT/REVIEW_author.md)), read all 90 statements, followed
  Parts B and C with their proofs, and checked the small models by its own program (mod-p Betti numbers of the nerves
  of the five- and seven-element monoids for `S²` and `S³`, and of the three-object model of `RP²`). The second,
  independent review ([reviews/1_CATHOT/REVIEW.md](reviews/1_CATHOT/REVIEW.md)) confirmed D.3–D.5, E.1–E.5,
  E.7–E.13, E.15, E.18, E.20–E.25 and F.7–F.13, and reproduced the minimal models by its own enumeration, including
  all 208,672 labelled monoids of order 6 (`reviews/1_CATHOT/checks/`). No statement labelled Proved or Refuted was found false. Open in the answer: D.6, E.6,
  E.17, E.26, E.27, G.17.
- **Path forward:** sections "After CATHOT" in prompts 2 to 6. After the second review: the question of
  rectifiability (prompt 6), a cardinal-controlled Kan–Thurston statement to which E.17 reduces (prompts 4 and 6), a
  caution on ind-objects (prompts 2, 5 and 6, and the Longue Marche prompts on the Teichmüller tower and on Galois
  topoi). E.26 and E.27 were later proved by the answer to prompt 6, and the Kan–Thurston statement, with E.17 for
  small filtered index, by the answer to prompt 4.

### 2. TOTASPH: total asphericity, filtered categories, and Grothendieck's Dwyer-type immersions

- **Prompt:** [prompts/2_TOTAL_ASPHERICITY/PROMPT.md](prompts/2_TOTAL_ASPHERICITY/PROMPT.md). Asked: whether the
  "totally W-aspherical" categories of Chapter XII (every ordinary final image aspherical) are the filtered ones, with
  a collage test, an affine-equalization condition and small monoids as leads, and the claim rows of Chapters II
  and XII that depend on it. Attached: [prompts/2_TOTAL_ASPHERICITY/ATTACHMENTS.md](prompts/2_TOTAL_ASPHERICITY/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 10 November 2026. 107 statements: 84 Proved,
  11 Refuted, 10 Known, 2 Open.
- **Review:** [reviews/2_TOTAL_ASPHERICITY/REVIEW_author.md](reviews/2_TOTAL_ASPHERICITY/REVIEW_author.md), all 107
  statements. Own programs in `reviews/2_TOTAL_ASPHERICITY/checks/` reproduce every count of the answer (the affine
  cones over the injective ordinals, the small examples, the endpoint pushouts). Opened: Cisinski 2006 (9.2.1,
  9.2.15, 9.2.17), Adámek–Koubek–Reiterman 1981, Cisinski 1999 and 2004, Thomason 1980 and the others listed in the
  review. No statement labelled Proved
  or Refuted was found false. The review found that B.11 holds for diagrams of simplicial sets but not for diagrams of
  categories with the colimit taken in `Cat` (a counterexample over the injective ordinals). Open: D.7, F.27.
- **Path forward:** sections "After TOTASPH" in prompts 3 to 6
  ([reviews/2_TOTAL_ASPHERICITY/PROMPT_UPDATES.md](reviews/2_TOTAL_ASPHERICITY/PROMPT_UPDATES.md)); after the review,
  prompt 6 was corrected for B.11.

### 3. POLES: the fibration axiom and the cofibration axiom for fundamental localizers

- **Prompt:** [prompts/3_POLES/PROMPT.md](prompts/3_POLES/PROMPT.md). Asked: the fibration axiom Loc (7) against the
  reversible cofibration axiom Loc (6 b) of Chapters XII and XVI, and Théorème 5.4 of Chapter XVI, which asserts both
  for `W∞`. Attached: [prompts/3_POLES/ATTACHMENTS.md](prompts/3_POLES/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 10 November 2026. 104 statements: 75 Proved,
  14 Refuted, 13 Known, 2 Open.
- **Review:** [reviews/3_POLES/REVIEW_author.md](reviews/3_POLES/REVIEW_author.md): the report and all 104
  statements (38 in full), Parts B and D with their proofs, against the companion's audit of Chapters XII and XVI;
  own program `checks_author/check_poles.py`. Verdicts: Théorème 5.4 of Chapter XVI is false in its Loc (6 b) entry
  only; Loc (6 b) forces `W ⊃ W_Z`. No statement labelled Proved or Refuted was found false. Unverified: Part A,
  C.8–C.10, E.3, E.4, E.7, F.9–F.13, most of Part G, H.7. Open: A.16, F.14.
- **Path forward:** sections "After POLES" in prompts 5, 6 and 7
  ([reviews/3_POLES/PROMPT_UPDATES.md](reviews/3_POLES/PROMPT_UPDATES.md)). Prompt 4 had already been sent; nine
  checks on its answer were listed instead and made in its review. A.16 was later refuted by the answer to prompt 7
  (A.32).

### 4. GALOIS: locally constant coefficients and the localizer they define

- **Prompt:** [prompts/4_GALOIS/PROMPT.md](prompts/4_GALOIS/PROMPT.md). Asked: the localizer of equivalences on
  locally constant coefficients (Chapter I), and a Galois theory relative to a theory of coefficients. Attached:
  [prompts/4_GALOIS/ATTACHMENTS.md](prompts/4_GALOIS/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026. 74 statements: 52 Proved, 7 Refuted,
  10 Known, 5 Open.
- **Review:** [reviews/4_GALOIS/REVIEW_author.md](reviews/4_GALOIS/REVIEW_author.md): the report and all 74
  statements, Parts A and B with their proofs, the proofs of D.3–D.7 and D.12; own program
  `checks_author/check_galois.py`; opened Cisinski 2009 (Theorem 3.6) and the papers of Di Vittorio and Kaledin;
  four apparent slips checked against the printed edition (all four are the edition's text). Verdicts: the localizer
  is a fundamental localizer for every derivator satisfying Der 1–4; Lead 3 is false and is repaired by Thomason
  fibrations; the cardinal-controlled Kan–Thurston statement, and with it E.17 of prompt 1 for small filtered index,
  is proved. No statement labelled Proved or Refuted was found false. Open: B.13, B.14, E.11,
  F.8, G.6.
- **Path forward:** sections "After GALOIS" in prompts 5, 6 and 7 and in the Longue Marche prompt on the Teichmüller
  tower ([reviews/4_GALOIS/PROMPT_UPDATES.md](reviews/4_GALOIS/PROMPT_UPDATES.md)).

### 5. STRATA: small categories as stratified spaces

- **Prompt:** [prompts/5_STRATA/PROMPT.md](prompts/5_STRATA/PROMPT.md). Asked: small categories as stratified spaces
  and coefficients on them as constructible sheaves; the gluing of the appendix to Chapter XII as homotopy links;
  bifibrations; the exit-path category of the moduli space `M̄_{0,n}`. Attached:
  [prompts/5_STRATA/ATTACHMENTS.md](prompts/5_STRATA/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026. 81 statements: 54 Proved, 9 Refuted,
  14 Known, 4 Open.
- **Review:** [reviews/5_STRATA/REVIEW_author.md](reviews/5_STRATA/REVIEW_author.md), all 81 statements; own program
  `checks_author/check_strata.py`; opened Lurie's *Higher Algebra*, *Exodromy*, Aoki, Douteau–Waas, Cisinski 2006,
  Jansen, Kent–Leininger–Schleimer and Fiedorowicz (the arXiv papers are listed in
  [reviews/5_STRATA/SOURCES_OPENED.md](reviews/5_STRATA/SOURCES_OPENED.md)). No statement labelled Proved, Known or
  Refuted was found false. Open: A.6, B.5, B.12, E.11.
- **Path forward:** sections "After STRATA" in prompts 6 and 7 and in the Longue Marche prompt on the Teichmüller
  tower ([reviews/5_STRATA/PROMPT_UPDATES.md](reviews/5_STRATA/PROMPT_UPDATES.md)).

### 6. PATHS: path categories against the simplicial localization

- **Prompt:** [prompts/6_PATHS/PROMPT.md](prompts/6_PATHS/PROMPT.md). Asked: whether Grothendieck's path categories
  (vertical arrows arbitrary) have the homotopy type of the Dwyer–Kan mapping spaces, how they compose, and which
  relative categories carry a homotopy theory of diagrams. Attached:
  [prompts/6_PATHS/ATTACHMENTS.md](prompts/6_PATHS/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026. 76 statements: 40 Proved,
  19 Refuted, 11 Known, 6 Open.
- **Review:** [reviews/6_PATHS/REVIEW_author.md](reviews/6_PATHS/REVIEW_author.md), all 76 statements; own program
  `checks_author/check_paths.py`; opened Cisinski 2006 and 2019, Maltsiniotis 2005, Kaledin, Dwyer–Kan, Meier,
  Rădulescu-Banu, and the manuscript at the pages concerned. No statement labelled Proved, Known or Refuted was found
  false. The prompt's main question remains open (B.8). Open: A.8, B.8, C.9, C.10, D.22, E.11.
- **Path forward:** a section "After PATHS" in prompt 7 ([reviews/6_PATHS/PROMPT_UPDATES.md](reviews/6_PATHS/PROMPT_UPDATES.md)).

### 7. BISITE: the two fine localizations, smooth and proper maps, and the six-operations shape of a derivator

- **Prompt:** [prompts/7_BISITE/PROMPT.md](prompts/7_BISITE/PROMPT.md). Asked: the two fine localizations over a
  base, the duality of smooth and proper maps, and the shape of six operations on a derivator. Attached:
  [prompts/7_BISITE/ATTACHMENTS.md](prompts/7_BISITE/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026. 126 statements: 72 Proved,
  32 Refuted, 18 Known, 4 Open.
- **Review:** [reviews/7_BISITE/REVIEW_author.md](reviews/7_BISITE/REVIEW_author.md), all 126 statements: Parts A
  and B followed in full, eight proofs of Parts C to G followed, about twenty statements checked by hand, 44
  statements unverified (listed in the review); own program `checks_author/check_bisite.py`; no cited source opened.
  No statement labelled Proved, Known or Refuted was found false.
- **The seven answers together:** [reviews/7_BISITE/COMBINED_REVIEW.md](reviews/7_BISITE/COMBINED_REVIEW.md) reads
  the seven answers as one body: 658 statements, 29 of them Open. It aligns their conventions and adds three
  arguments of the reviewer's own, unchecked by anyone else.
- **Path forward:** [reviews/7_BISITE/FOLLOW_UPS.md](reviews/7_BISITE/FOLLOW_UPS.md) writes the open points as ten
  Parts of a new prompt (prompt 8 below) and six inserts for the Longue Marche prompts not yet sent (they will be
  published with their answers). [reviews/7_BISITE/COMPANION_INTEGRATION.md](reviews/7_BISITE/COMPANION_INTEGRATION.md)
  lists 24 items for the companion.

### 8. RESIDUE: what seven packages on *Les Dérivateurs* left undecided

- **Prompt:** [prompts/8_RESIDUE/PROMPT.md](prompts/8_RESIDUE/PROMPT.md), the follow-up prompt: Parts A to J are the
  ten Dérivateurs items of the follow-ups of prompt 7; the reviewer's three combination arguments are its Leads 1
  to 3, and four statements of the answer to prompt 7 that its review left unverified (D.11, F.15–F.17) are Leads 4
  and 5. Built by [tools/build_8_RESIDUE.py](tools/build_8_RESIDUE.py); assembly notes in `prompts/8_RESIDUE/work/`.
  Attached: [prompts/8_RESIDUE/ATTACHMENTS.md](prompts/8_RESIDUE/ATTACHMENTS.md).
- **Model and run:** GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026. 85 statements: 54 Proved,
  11 Refuted, 7 Known, 13 Open.
- **Review:** not yet made. Every statement of this answer is unchecked.
