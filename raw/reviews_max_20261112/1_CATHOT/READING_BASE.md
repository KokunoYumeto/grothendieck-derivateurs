# READING_BASE: what was read for the review of CATHOT, and what is relied on

Claude Fable 5.2 (Anthropic), effort max, 12 Nov 2026. Primary texts only; freely accessible copies (arXiv, authors'
pages, Numdam, journals' open pages) or the files supplied in the background package. "Local" paths are under
`pro_reviews_max_20261112/1_CATHOT/work/`. For each source: where it is, what I read, and the statements I rely on
with their hypotheses. "Recent" = dated after mid-2026, outside what I could know from memory. At the end: what I
could not obtain.

## 1. Grothendieck, *Les Dérivateurs* (transcription in the background package)

Local: `background/grothendieck/DER_*/DER_*_text.tex` (AI transcription of the edition of Künzer, Malgoire and
Maltsiniotis; manuscript pages marked `\msp{page N}`). Read in full:
- **V ms. 11–13**: definition of Cat hot, Hom = π₀ Hom(A, B), ind-objects of Cat hot, the ind-morphism of
  composition of paths.
- **V ms. 36–52**: the asserted right adjoint ψ of φ: Cat hot → Hot (ms. 37, with the editors' request for a
  proof); Proposition 1 and its corollary (ms. 37–40); ind-objects and Proposition 2 (ms. 40–42); the "enveloppe de
  Thomason–Kan" (ms. 42–44); K_∞ and finite categories (ms. 44–46); the claims about union maps, the strict
  retraction, the Question (ms. 46–49); Hot₀ and the functor Hot → Hot₀^ ("conservatif", "pleinement fidèle?";
  ms. 51–52).
- **VII ms. 108–136** (C, C_∞, H_T; the flèche C_∞ → C; composition; "Hot → Hot₀^ est conservatif", ms. 121 note 26;
  "Z ↦ Hom_Hot(Y, Z) commute aux limites inductives filtrantes si Y est une catégorie finie", ms. 121; associativity
  and faithfulness, ms. 127; ms. 128; §11, ms. 129–136: the "condition préalable", the 2-sphere example, the map
  hot(Hom(Y, C)) → Hom_Hot(hot Y, hot C), "n'ont aucune tendance à être des catégories de Thomason–Kan") and
  **VII ms. 149–157** (T², the fibration statements 1°–3°).
- **IX ms. 8–13** (the diagram with φ, ψ, lim; composition C⁻ × C⁺ → C) and **IX ms. 22–25** (Σ, Ω, tests ⓐ ⓑ ⓒ,
  "Je doute que ces conditions puissent être satisfaites pour M finie", the path-object construction).
- **Appendix to XII, ms. 1–18** in full (the false Proposition; the two-object category with monoid G; V, Ṽ; Z and
  footnote 7: "il a donc le type d'homotopie de la 2-sphère"; the square and the cofibration counterexample; the
  gluing question).
Not read in full: VII ms. 50′–107 and 137–148 (definitions of types and path categories), used only through the
return's quotations; my verdicts on E.20–E.27 say so.

## 2. The preprint under test (recent)

**O. Ben-Bassat, *On a Conjecture of Fiedorowicz*, arXiv:2610.38760v1, 28 Oct 2026** (19 pp.; unrefereed; only v1
exists on 12 Nov 2026). Local: `lit/benbassat/src/Fiedorowicz2.tex` (arXiv source, sha256 102ceaa7…) and the PDF.
Read in full. Relied on:
- Conjecture 1.1 (Fiedorowicz); Theorems A, B, C (Introduction): Theorem C: "every finite simply connected CW
  complex is homotopy equivalent to BM for a finite aperiodic monoid M".
- Lemma 2.4: if every object of a small category D is a retract of c₀, then B D(c₀, c₀) → BD is a homotopy
  equivalence (proof by Quillen's Theorem A; checked).
- Definition 3.3 (the monoid M(Y, f)), Lemma 3.2, Lemma 3.6, Proposition 4.1, Lemma 4.2, Lemmas 5.1–5.4 (read and
  re-derived as listed in `EMAIL_CLAIMS_CHECK.md` (d)).
- §7: η_M is onto and U(M) is finite for finite M; **Conjecture 7.1**: "Let X be a connected finite CW complex. If
  π₁(X) is finite, then X ≃ BM for some finite monoid M."
- Examples 3.2, 6.1–6.4 (used for my tests; the 1795- and 122-element monoids were not recomputed).

## 3. Sources for the fundamental-group theorem

**H. Miller, *The Sullivan conjecture on maps from classifying spaces*, Ann. of Math. (2) 120 (1984), 39–87.**
Author's page: https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture.pdf (local `lit/miller/`). Read: pp.
39–41 and Section 10 (pp. 84–85) in the page images. Relied on: **Theorem B** (p. 40): "Let X be a finite
dimensional CW complex and G a torsion group. Then any pointed map BG → X induces the trivial map of fundamental
groups." = **Theorem 10.1** (p. 84, "any map"), proved pp. 84–85 by a covering space, Lusternik–Schnirelmann
category and K⁰(BZ_m) = Z[[x]]/((1+x)^m − 1). Theorem A (p. 39; G locally finite, X connected finite-dimensional
CW: map_*(BG, X) weakly contractible) is quoted in the return's D.6 remark and in my H7. Remarks 10.2, 10.3.
**Correction, Ann. of Math. 121 (1985), 605–609**:
https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture-correction.pdf. Read pp. 605–608: two errors (the
unstable-module claim behind the spectral sequence (2.5); "Fact 3.9"), both in the proof of Theorem C of that
paper; Section 10 is not concerned.

**M. F. Atiyah, *Characters and cohomology of finite groups*, Publ. Math. IHES 9 (1961), 23–64.** Numdam:
http://www.numdam.org/item/PMIHES_1961__9__23_0.pdf (local `lit/atiyah/`). Read §6 (6.8)–(6.13), §7 (7.1)–(7.9),
§8 (8.1)–(8.2), pp. 45–48 in the page images. Relied on: **(6.10)** ⋂ I(G)ⁿ = {χ ∈ R(G) : χ(S) = 0 for all S of
prime-power order}; **(6.11)** for a p-group R(G) → R(G)^ is a monomorphism; **(7.2)** α̂: R(G)^ → 𝒦*(B_G) is a
topological isomorphism (𝒦* = inverse limit of K* of the finite skeleta; G finite); **(8.1)** the same, as filtered
groups, for cyclic G.

**A. Hatcher, *Algebraic Topology*** (supplied PDF). Relied on: **Proposition 4C.1** (a simply connected CW complex
with a chosen decomposition of its homology groups is homotopy equivalent to a CW complex with one n-cell per Z
summand of H_n and one n-cell and one (n+1)-cell per finite cyclic summand); Theorem 2C.5 (finite CW ≃ finite
simplicial complex); Proposition 4.15; Theorem 4.57; Examples 3F.7, 3F.9.

## 4. Finite monoids, finite models (several recent)

- **D. Sweeney, *Homotopy types of small semigroups*, arXiv:2502.05276v2 (13 Jun 2026; recent)** and **v1 (Feb
  2025)**. Local `lit/arxiv_2502.05276v*/`. Read v2 §§1–2 (Lemma 2.1: the group completion of a finite semigroup is
  H/⟨⟨sandwich entries⟩⟩ for its minimal ideal M(H; I, J; C), quoting Larisse and Howie–Margolis; Prop. 2.2,
  Cor. 2.3: H_i(BM) = Tor_i^{ZM}(Z, Z); Lemma 2.6, Theorem 2.7: BS ≃ B(eSe) if eSe = eS or Se; Cor. 2.9), §5
  (Examples 5.1–5.3), statement of Theorem 1.1 and Corollaries 1.2–1.4 (joins, suspensions). v1: Example 8.2 (the
  six-element semigroup with BS ≃ S³ and its resolution). Tables 4–5 were *not* relied on: I re-enumerated all
  monoids of order ≤ 6 myself.
- **Z. Fiedorowicz, *A counterexample to a group completion conjecture of J. C. Moore*, AGT 2 (2002), 33–35**
  (arXiv:math/0202260; supplied). The Lemma (pp. 33–34): the five-element monoid and its resolution.
- **A. Martinian, B. Steinberg, arXiv:2511.12657v1 (Nov 2025)**: statement of Theorems A, B only (wedges of Moore
  spaces); not relied on.
- **I. Carcacía-Campos, arXiv:2611.09718v1 (6 Nov 2026; recent)**: Theorem 6.2: "For every n ≥ 1, B C_{Z/2,n} is
  homeomorphic to RPⁿ" (C_{Z/2,2} is the return's R₂). Not relied on (I proved the case n = 2 directly).
- **N. Cianci, M. Ottina, arXiv:1512.06088v1**: Corollary 5.8 ("a finite model of the real projective plane has at
  least 13 points") and Theorem 5.10 (the two 13-point models). Relied on for G.8 and my Proposition 5.1; proofs
  not re-checked.
- **J. Barmak, E. Minian, *Minimal finite models*, arXiv:math/0611156** (supplied): "Any space with the same
  homotopy groups as Sⁿ has at least 2n + 2 points", with uniqueness. Cited by G.7; G.7's own proof is independent
  and I checked it.

## 5. Thomason's model structure, posets, Quillen, homotopy colimits (supplied)

- **R. W. Thomason, *Cat as a closed model category*, Cahiers 21 (1980), 305–324** (Numdam). Theorem 4.9 (model
  structure), Lemma 4.10, Corollary 5.5 (properness), Lemma 5.6, Proposition 5.7 ("every cofibrant category is a
  poset"). Statements read; proofs not re-checked (the retract error for Dwyer maps is corrected by Cisinski, as
  Raptis recalls).
- **G. Raptis, *Homotopy theory of posets*, HHA 12 (2010), 211–230.** Proposition 2.4 (pseudo-Dwyer morphisms;
  c Sd² of a monomorphism is a Dwyer morphism), Theorem 2.6 (model structure on Pos, Quillen equivalent to Cat, with
  the same fibrations and weak equivalences), Proposition 3.4, **Theorem 3.5** (the model category Cat_{I(λ)}: all
  pseudo-Dwyer morphisms between λ-presentable objects as generating cofibrations; every λ-presentable object is
  cofibrant), Remark 3.6, the paragraph on p. 220–221 showing these structures are *not* monoidal, Proposition 4.8
  (the cylinder P × Z₂ with Z₂ = c Sd² Δ¹), Remark 4.9.
- **J. P. May, M. Stephan, I. Zakharevich, *The homotopy theory of equivariant posets*, Cahiers 58 (2017).**
  Lemmas 3.6, 4.7, 4.8 (pushouts of Dwyer G-maps), Proposition 6.2 (a six-element poset of type S² is not
  cofibrant), Proposition 6.4.
- **D. Quillen, *Higher algebraic K-theory I*** (LNM 341): §1, Theorem A and Theorem B.
- **W. Chachólski, J. Scherer, *Homotopy theory of diagrams*, arXiv:math/0110316v1**: Theorem 26.8 and
  Corollary 26.9 (= Thomason's Theorem 1.2: N(Gr_I H) ≃ hocolim_I N(H)).
- **B. Shoikhet, arXiv:1412.0317v4**: only located (Theorem 1.8, Proposition 3.3); not relied on.

## 6. Group theory and cohomology used in Parts B and F

- **M. Palmer, X. Wu, *Embedding groups into acyclic groups*, arXiv:2510.16879v1 (19 Oct 2025)**, Introduction: the
  statements of Kan–Thurston ("every connected CW-complex has the homology of a group") and of [KT76, Prop. 3.3]
  (every group embeds in an acyclic group of the same cardinality, countable if the group is finite).
- **W. Dicks, P. Kropholler, I. Leary, S. Thomas, arXiv:math/0111283v1**: Corollary 6.10(2) (Chen): for an abelian
  torsion group G and a non-zero ring R in which the orders of the elements of G are invertible,
  cd_R G = ℵ-rank(G) + 1. Statement read; relied on for F.12.
- **J. E. Domínguez, C. Segovia, arXiv:2012.02464v2**: Proposition 20 and Corollary 21 (for n ≥ 4, n ≠ 6, 7 the
  generator of the Schur multiplier of A_n is represented by the pair (1 2)(3 4), (1 3)(2 4)). Statement read.
- The HNN embedding theorem, the mitosis construction and the homology of amalgams are used by the return with
  proofs written out (B.5, B.6, B.8); I checked those proofs and did not need the original papers.

## 7. Finite tests (supplied)

- **K. Arlin, J. D. Christensen, *Detecting isomorphisms in the homotopy category*, AGT 23 (2023)** (LaTeX
  supplied): Theorem 2.1 (no set of spaces detects isomorphisms in Hot), Theorem 4.3 (spheres detect equivalences
  through fundamental groupoids of mapping spaces). Statements located; proofs of F.4 and F.9 in the return are
  self-contained and I checked those.
- **K. Arlin, HHA 22 (2020)**; **P. Freyd, *Homotopy is not concrete*** (TAC reprint); **J. Lurie, *Higher Topos
  Theory***, 5.3.3.3, 5.3.5.11, 5.4.2.4, 4.2.4.4 (statements from memory; the supplied PDF was not re-opened).

## 8. Recent results that bear on the field (as required; all claimed, unrefereed unless said)

Read in the user's files `recent_results_20261110/SCOREBOARD.md`, `RECENT_RESULTS.md`, `BRIEF_FOR_PROMPTS.md`
(written by an agent at effort medium: used as pointers only) and `OPENAI_MATH_INVENTORY.md` (all 373 family titles;
full rows for 196, 207, 246–256, 304–321). Then the papers themselves:
- **OpenAI family 317, *Thomason Model Structures in Every Strict Higher Dimension*, 25 Sep 2026** (local copy in
  `recent_results_20261110/papers/`). Read: abstract, Introduction, Theorem 1.1 (for 1 ≤ n ≤ ω, nCat has a proper
  combinatorial model structure with weak equivalences and fibrations detected by Ex² N_n, Quillen equivalent to
  simplicial sets via c_n Sd² ⊣ Ex² N_n), the outline of the proof, §2 conventions, Theorem 5.2 and Propositions
  7.2–7.4, Theorem 7.5 as stated. Claimed; formalized main theorem per its repository note; not checked by me. Use
  here: none in any verdict; it is the n-dimensional frame for hunch H5. For n = 1 it is Thomason's theorem.
- **OpenAI family 312, *The Grothendieck homotopy hypothesis via elementary expansions*, 24 Sep 2026.** Read:
  abstract, Introduction, Theorem 1.1 (Henry's pushout conjecture), the outline, Corollaries 5.1–5.2 as stated.
  Claimed; only the pushout theorem formalized. Use here: its remark that strict ∞-groupoids model only products of
  Eilenberg–Mac Lane spaces among simply connected types (Ara), for H5.
- Families 249 (Eilenberg–Ganea, claimed refuted) and 321 (Wall's D(2), claimed refuted): titles and one-line
  claims only; they concern the gap between cohomological and geometric dimension, which is why Theorem 2.2 of
  `OWN_RESULTS.md` is stated with ordinary homology and proved through simple connectivity, not through a
  dimension count.
- My own search of arXiv on 12 Nov 2026 (API queries "classifying space" + "finite monoid", "Fiedorowicz" + monoid,
  "finite monoids" + "homotopy type", "classifying spaces" + "finite semigroups", and math.AT abstracts with "finite
  monoid" since 2025): the only 2025–2026 items are Sweeney v2, Martinian–Steinberg, Ben-Bassat and
  Carcacía-Campos. No preprint was found that states the refutation of Conjecture 7.1, the characterization of
  finite monoids with finite classifying space, or the ind-version of the envelope question.
- Our own project's claims (required reading, as claims): `french_school_site_20261110/findings/
  2026-11-10_thomason-kan-envelope.md` and the CATHOT entries of `grant_evidence/EVIDENCE.md`. Verdict in
  `REVIEW.md`, section "The Thomason–Kan envelope".

## 9. Not obtained

- **D. McDuff, *On the classifying spaces of discrete monoids*, Topology 18 (1979)**; **D. Kan, W. Thurston,
  Topology 15 (1976)**; **Baumslag–Dyer–Heller, JPAA 16 (1980)**; **Dwyer–Kan (1980)**: in the publisher's open
  archive, which refused automated access (HTTP 403). Kan–Thurston is used in `OWN_RESULTS.md` Theorem 3.1 from
  memory and from the Palmer–Wu summary; this is flagged there. McDuff's Lemma 1 is replaced by a direct proof.
- **Z. Fiedorowicz, Amer. J. Math. 106 (1984)**: paywalled; the copy the return used is on a university course page.
  Not opened; G.3 is therefore "known, statement not verified by me".
- **Higman–Neumann–Neumann 1949**, **Thomason 1979**, **Matumoto–Minami–Sugawara 1984**, **Schur 1911**,
  **Putcha 1998**: not opened; nothing in a verdict depends on them (Putcha only in hunch H2, marked).
- Pursuing Stacks, Maltsiniotis (Astérisque 301) and Cisinski (Astérisque 308): not re-opened for this review; the
  fundamental-localizer facts used (A.2) are proved in the return and checked.
