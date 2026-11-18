# Supplementary source record: B, E, and general comparison tools

Audit date: 17 November 2026. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Primary passages inspected

- **Dwyer–Kan, Calculating simplicial localizations (1980): opened.** Primary scan at `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/dwyer-kan-2.pdf`. Proposition 2.2 compares the two localizations; Propositions 3.1 and 3.5 and Corollary 3.6 give the component/natural-transformation/adjunction statements. Section 4, especially Propositions 4.2–4.5, treats the indexing category and proper diagrams; 5.1–5.5 identify fixed-type hammock graphs and their colimit; Section 6 states the additional fraction hypotheses. The all-type conclusion is not silently imposed on an arbitrary fixed type. A guessed UiO route failed before this original was obtained.
- **Chachólski–Scherer, Homotopy theory of diagrams (arXiv math/0110316): opened.** Attached TeX and primary 95-page PDF at `https://arxiv.org/pdf/math/0110316`; Chapter 3's comparison framework, Theorem 24.9 (Fubini), Theorem 26.8 and Corollary 26.9 (Grothendieck constructions), Theorem 30.5 (cofinality), including the proof steps used. These support the named natural homotopy-colimit comparisons in B.4; all comma contractions specific to the present problem are written out.
- **Cegarra–Heredia, Homotopy colimits of 2-functors (arXiv 1504.06114): opened.** The 32-page preprint, Section 4 and Theorem 5.1, at `https://arxiv.org/pdf/1504.06114`. The variance and double-nerve/Grothendieck comparison were checked for B.9. The number 5.1 is explicitly the preprint number.
- **Ara–Maltsiniotis, Vers une structure ... (2014): opened.** Original author PDF `https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/nthom.pdf`, Theorem 6.27, Section 5's nerve conventions, and Proposition 8.14. B.9 uses the established dimension-two case only. The attached 317 source was separately opened at its foundations and Section 7 equation `eq:model-classes`; no higher-dimensional theorem or unexecuted Lean certificate is asserted as independently checked.
- **Hackney–Ozornova–Riehl–Rovelli (arXiv 2205.02353): opened.** Attached source and primary PDF; Definition 3.4, Proposition 3.3, Example 3.5, Proposition 3.6, and Theorem 1.5. This fixes the exact meaning of “discretely flat”; it is not identified with the manuscript's dwyérienne notion.
- **Charney (arXiv math/0610668): opened.** Attached source and primary PDF, Sections 2.6–2.7 and Theorem 2.6. The Salvetti link argument and homology discussion are context for the earlier RAAG tests, not a theorem about FreeMon.
- **Gray–Steinberg (arXiv 1805.03413v3): opened.** In addition to the source audit in `CD_sources.md`, the primary PDF was opened at Theorems 4.5, 4.8, 4.10 and Remark 4.11. These correspond to the source labels recorded there. The false flatness inference from Fiedorowicz Lemma 5.2(a) is not used.
- **Nicholson (arXiv 1905.12018, attached revised source): opened.** Introduction, Theorem A and Corollaries B–C. These are comparison literature concerning dimension two; they are not a proof that every finitely presented superperfect group admits a finite acyclic two-complex. E.5 retains the exact balanced-presentation criterion in dimension two.
- **Higman (1951): body not obtained.** Exact-title/author searches, the OUP record `https://academic.oup.com/jlms/article-abstract/s1-26/1/61/966631`, and the Wiley DOI PDF route `https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/jlms/s1-26.1.61` were tried. The latter returned the abstract/record page. No mathematical assertion is attributed to the unseen body, and it is not needed for E.5.
- **Cisinski's MathOverflow correction (question 516223): opened.** The full primary answer at `https://mathoverflow.net/questions/516223/equivalence-of-cisinskis-proposition-4-3-2-ast%C3%A9risque-308-when-a-bg` confirms the missing hypothesis in (g)⇒(c) of Proposition 4.3.2. We use none of that disputed implication. The short URL first failed; the full indexed URL exposed the question and author answer.
- **Lurie, Higher Topos Theory: opened.** The exact inspected places and the Dold–Kan, Kervaire and Hirschhorn sources are recorded in `BE_sources.md` and `B_interval_sources.md`. In particular, the all-simplex theorem does not validate the false generalized nondegenerate-simplex reduction.

## Additional search topics and access attempts

The initial exact B.2 and E.2 queries are listed in `BE_sources.md`. The additional source-discovery topics and retrieval targets were:

1. `Dwyer Kan Calculating simplicial localizations 1980 pdf`.
2. The Rochester primary scan of *Calculating simplicial localizations*, found by the exact-title search.
3. `Cegarra Heredia homotopy colimits 2 functors Theorem 5.1`.
4. `Ara Maltsiniotis 2 categories Thomason Theorem 6.27`.
5. `Higman A finitely generated infinite simple group 1951 pdf`.
6. `site:academic.oup.com Higman 26 61 1951`.
7. `Cisinski 4.3.2 516223`.
8. `site:github.com/Commutator-IO/grothendieck-project cote 106` and `site:github.com/leanprover-community/mathlib4 44731`.

Queries 1–7 led to the primary routes stated above, except for Higman's unavailable body. Query 8 and direct web-reader directory/raw requests failed to expose the formal files; the public API/raw requests recorded by `code/F_source_fetch.py` succeeded. Their exact URLs, timestamps, hashes, and later pinned-source audit are retained separately. No login, private repository, or access-control bypass was used.

## Scope corrections to the supplied reviews and transcription

The PRETOT review's actual A.4 check concerns a free degeneracy completion and remains valid. Finding F13 merely proposes extending the method to arbitrary finite acyclic simplicial sets. E.1–E.5 confirm that method's classification goal; E.3 refutes the extra functor written in Lead 4(a), not the correctly scoped original A.4.

The phrase at VII ms.112 is expressly about full path categories; its negative conclusion is false in that context, as the already established PATHS/INDLOCAL comparisons show. The “hypothèse d'homotopie” at ms.99 only equates parallel maps up to homotopy. B.10 keeps this distinct from coherent descent and proves the retained component assertion at ms.110. A preliminary checkpoint sentence describing the ms.112 warning as correct without this distinction was corrected during this audit.
