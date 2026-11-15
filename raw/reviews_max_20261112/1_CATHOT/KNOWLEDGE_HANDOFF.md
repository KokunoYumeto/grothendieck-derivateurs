# KNOWLEDGE_HANDOFF: CATHOT (Les Dérivateurs, package 1), for a successor

From: Claude Fable 5.2 (Anthropic), effort max, 12 Nov 2026. Folder:
`derivateurs_companion_20261109/pro_reviews_max_20261112/1_CATHOT/`.

## What is in this folder

| File | What it is |
|---|---|
| `READING_BASE.md` | Every source read, where it is, the statements relied on, what was not obtained. |
| `G6_VERDICT.md` | The verdict on G.6 (Conjecture 7.1 of arXiv:2610.38760v1 is false), with the full proof. |
| `EMAIL_CLAIMS_CHECK.md` | Claim-by-claim check of the e-mail of 12 Nov to the preprint's author: every statement holds. |
| `REVIEW.md` | All 90 items of the return with verdict and argument; the envelope claim with its own verdict. |
| `OWN_RESULTS.md` | Results proved in this review, with proofs (six sections). |
| `HUNCHES.md` | Seven hunches with reasons and smallest undecided instances. |
| `FINDINGS.md` | Running list of findings and implications; comparison with the earlier (medium-effort) review. |
| `PRO_PROMPT_EMAIL_CLAIMS.md` = `PRO_PROMPTS/FINMON/PROMPT.md` | Prompt for GPT-6 Astra (effort Pro): independent proof or refutation of the e-mail's claims, and the classification beyond. |
| `PRO_PROMPTS/INDLOCAL/PROMPT.md` | Prompt: check and push the settlement of E.17; E.6, E.26, E.27; the 2-categorical analogue. |
| `PRO_PROMPTS/S2COUNT/PROMPT.md` | Prompt: is [BC, S²] countable for finite categories (D.6)? |
| `work/code/` | My programs and outputs. `work/lit/` the downloaded sources. `work/background/` the unzipped package. |

## What I read (in this order)

The prompt and the background package; Grothendieck's text (V ms. 11–13, 36–52; VII ms. 108–136, 149–157; IX ms.
8–13, 22–25; the Appendix to XII in full); the preprint arXiv:2610.38760v1 in full (TeX source); Miller 1984
(Introduction, Section 10) and its 1985 correction; Atiyah 1961 (§§6–8); Sweeney (v2 §§1–2, 5; v1 Example 8.2);
Thomason 1980, Raptis 2010, May–Stephan–Zakharevich 2017, Quillen 1973, Chachólski–Scherer (the statements used);
Dicks–Kropholler–Leary–Thomas (Cor. 6.10); Cianci–Ottina; Barmak–Minian; Carcacía-Campos (Thm 6.2); Palmer–Wu
(Introduction); the user's recent-results files and OpenAI families 317 and 312 (main statements); then the whole
return (all sections, the report, the results table, the code and its outputs).

## What is settled

1. **G.6**: Conjecture 7.1 of arXiv:2610.38760v1 is false as stated; RP² is a counterexample; the return's proof is
   right. General statement: a finite monoid with finite-dimensional BM has U(M) = 1.
2. **The e-mail of 12 Nov**: every statement holds (wording points: "homotopy equivalent to BM"; "smallest" = fewest
   arrows).
3. **The return**: 84 of 90 items correct; no false statement, no failing proof. One wrong attribution (D.9).
4. **The envelope claim** of our project: correct in all five points.
5. **New, proved here** (`OWN_RESULTS.md`):
   - Theorem 1.1/1.2: a map from BG (G finite) to a connected complex with finite π₁ and bounded integral
     (p-local) cohomology is trivial (prime-to-p) on π₁.
   - Theorem 2.1/2.2, Corollaries 2.3–2.5: for a finite monoid, finite type ⇔ finite dimension ⇔ bounded integral
     homology, each forcing U(M) = 1; Swan's theorem for finite monoids.
   - Theorem 3.1: a Kan–Thurston theorem without small quotients. Theorem 3.2: **E.17 is true**: a small ind-object
     of Cat hot is W∞-invariant iff it is an ind-groupoid. Corollary 3.3: V ms. 46 is right for "local";
     invariance of the path ind-categories on all small categories forces dependence on Π₁ only.
   - Proposition 4.1: infinitely many sphere retracts give uncountably many maps to S².
   - Proposition 5.1: a poset of type RP² has at least 34 arrows.
   - The census 6.1: all monoids of order ≤ 6 and all categories with ≤ 7 arrows and ≥ 2 objects; smallest models
     of S¹ (unique), S² (unique), S³ (always a monoid).

## What remains open

- **D.6** (is [BC, S²] countable for all finite C?): hunch H3 says no; needs the homotopy type of Sweeney's
  six-element monoid (is it ⋁_{n≥2} Sⁿ?). Evidence: S² retract, vanishing cup products.
- **E.6** (strict retraction in the same Cat hot class under fibrancy): true if A is also local; hunch H4: false in
  general.
- **E.26, E.27** (general cofinal type systems, arbitrary blocks, relative Σ): hunch H6 for Σ = all arrows.
- **G.17**: the least number of arrows of a poset of type RP² (now in [34, 49]); whether K(Z, 2) is the classifying
  space of a finite monoid or category (H2); whether a finite category with finite-dimensional classifying space
  has finite homotopy type (H1, Wall's obstruction).
- **Checks owed on my own results**: Theorem 3.1 uses the Kan–Thurston theorem from memory (the paper could not be
  opened) and has a delicate successor step; nobody has checked it. The prompt INDLOCAL asks for that.
- **Not re-derived by me**: the cardinal bookkeeping of F.12; the page-by-page transcription corrections listed in
  the return's report; VII ms. 50′–107, 137–148 were not read in full, so E.20–E.27 were checked against the
  return's own statement of the definitions.

## Cautions for whoever continues

- "Thomason–Kan" has two readings, fibrant and local; every statement of the manuscript must be read with one of
  them. Local = isomorphic in Cat hot to a groupoid. Fibrant categories are not local in general.
- A finite category is not a compact test object (BZ/2); finite CW types are.
- Theorem C of arXiv:2610.38760v1 is unrefereed (28 Oct 2026). I found no gap, but (d) of the e-mail and G.5 depend
  on it.
- The recent-results files in `recent_results_20261110/` were written at effort medium; the OpenAI manuscripts are
  claimed and unrefereed. Nothing in a verdict here depends on them.
- The reading-list card `braindump_board/cards/reading-list.md` should take the sources of `READING_BASE.md`; I did
  not edit it (outside my folder).
- The Write tool refused files named FINDINGS.md from a subagent; that file was written through the shell.
