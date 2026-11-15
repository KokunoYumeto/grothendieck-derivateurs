# Literature audit for D.3

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim. This file records actual access, not conclusions inferred from search snippets. Search date: 13 November 2026.

## Requested records

| Source | Access in this run | Exact locations relevant to the task |
|---|---|---|
| Isbell–Mitchell (1973), *Exact colimits*, Bull. AMS79,994–996 | **Opened attached primary PDF; root's theorem audit completed** | Theorems1–3 and Lemma1 were checked. Theorem3 announces the ordinal-injection exact-colimit example; its independent polynomial proof is audited in the current paper. |
| Isbell–Mitchell (1976), *Exact colimits and fixed points*, Trans. AMS220,289–298 | Opened attached primary body and extracted local text | Theorem3.1 (exactness iff components of affine category filtered), Proposition3.3 (I+III), remark p.296 (commutative coefficient rings), Theorem4.1 and Corollaries4.2–4.4 (ordinary equalization exclusions), Proposition4.5 and Corollary4.6 (bounded representables); p.298 asks the fixed-point/exactness question. Root read all §§1–4. |
| Isbell (1968), *A note on exact colimits*, Canad. Math. Bull.11(4),569–572 | **Opened full primary PDF** from Cambridge | The unnumbered theorem in §1, pp.569–570, characterizes exactness by finite additive relations and common successors. The unnumbered theorem in §2, pp.571–572, proves exactness iff filteredness for a monoid. Do not invent theorem numbers; cite by section and page. |
| Isbell (1974), *Exact colimits. I*, Ann. Math.100(3),633–637 | **Not obtained**: Annals bibliographic page and JSTOR record opened; full-body requests failed | No theorem number or content claim assigned to unopened body. Tried exact-title searches, DOI10.2307/1970960, Annals official page, JSTOR stable record, and stable/pdf endpoint. |
| Oberst (1968), *Homology of categories and exactness of direct limits*, Math. Z.107,87–115 | **Not obtained**: publisher metadata opened; body requires subscription; direct content/PDF request failed | No original theorem number asserted. Tried exact title with author, year/volume/pages, DOI10.1007/BF01111023, searches for publicly indexed full text, publisher article and content/PDF endpoint. Husainov Theorem2.7 is opened as a secondary statement, but is not represented as opening Oberst. |
| Adámek–Reiterman (1975), *Fixed points in representations of categories*, Trans. AMS211,239–247 | **Not obtained in this run**: official AMS full PDF and article endpoints failed with403 or internal error | Searched exact title, DOI10.1090/S0002-9947-1975-0376799-X, AMS journal and shorter URL forms; publisher volume contents and bibliographic records are not counted as body access. No content claim assigned. |
| Adámek–Koubek–Reiterman (1981), *Embeddings into categories with fixed points in representations*, Czech. Math. J.31(3),368–389 | **Opened attached primary PDF; construction audit completed for the cited results** | A.4's correction, B.5–B.9, C.1, and the full induction of TheoremC.2 were checked. The finite-tests agent independently inspected (10),(11), C.1's numerical hypotheses, and every C.2 counting step on pp.385–389; the threshold-three weighted extension is detailed in `finite_marked_cycle_audit.md`. This is distinct from proving the still-unresolved infinite-stage H2 persistence. |
| Husainov (2002), *Homological dimension theory of small categories*, J. Math. Sci.110(1),2273–2321 | **Opened English full text in author-uploaded ResearchGate rendering**, plus author-hosted Russian translation | Theorem2.4 (flows modulo internal flows compute first derived colimit); Theorem2.5 (affinization criterion); Theorem2.6 (flatness of a permutation presheaf when all transition maps inject); Theorem2.7 (equivalent exactness formulations, attributed to Oberst); Problem2.5 (fixed-point-property/exactness question). Its Problem2.5 is not a source for the current totality question; in light of AKR1981 the weaker fixed-point equivalence is already false. |
| Gabriel–Ulmer (1971), *Lokal präsentierbare Kategorien*, LNM221 | **Opened full 181-page scan** from Doug Ravenel's university-hosted collection, downloaded locally | §5.2, printed pp.55–56: filteredness iff set colimits commute with finite limits (the alpha variant); §15.2(c), printed p.187: finite cocone zigzag criterion, reducible to two objects; §15.9, pp.190–191: Yoneda completion argument supplies its converse. These are the relevant classical sifted criterion locations. §14.10, pp.177–178, concerns Kan extension preserving specified limits under explicit colimit-commutation assumptions; it does not supply total=>exact. |
| Flatness of the one-element monoid act | **Opened primary Hemelaer–Rogers (2021)** and author manuscript by Valdis Laan | Hemelaer–Rogers Definition1.6 explicitly distinguishes monomorphism-flatness from finite-limit-flatness; Proposition1.8 equates latter with filtering flat functors; Theorem2.32 treats monomorphism preservation by connected components; Theorem2.49 characterizes finite-limit preservation for the one-element act by cofilteredness/right collapsibility, with the reverse variance from our covariant monoid actions. Laan, *On a generalization of strong flatness*, Proposition2.4 and the paragraph following Lemma2.6 distinguish (O) from strong flatness using the one-element act over a nontrivial group. |

## Exact source URLs and local availability

- Isbell1968: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/344EA0110F34F24298FD42E14305F634/S0008439500056836a.pdf/a-note-on-exact-colimits.pdf . Opened web ref `turn6view0`, full§2 also `turn20view2`. Local fetched file: `TOTEX2/sources/Isbell1968.pdf`, HTTP200, 307030 bytes.
- Isbell1974 official record: https://annals.math.princeton.edu/1974/100-3/p05 ; JSTOR https://www.jstor.org/stable/1970960 . Not body access.
- Oberst1968: https://link.springer.com/article/10.1007/BF01111023 . Subscription preview only.
- Adámek–Reiterman1975 attempted official PDF: https://www.ams.org/journals/tran/1975-211-00/S0002-9947-1975-0376799-X/S0002-9947-1975-0376799-X.pdf ; shorter `/tran/...` endpoint also attempted.
- Husainov English author-uploaded text: https://www.researchgate.net/publication/232724279_Homological_dimension_theory_of_small_categories ; relevant complete passages opened (`turn13view2`, `turn13view3`). Russian author translation: https://husainov51.narod.ru/files/rep2rus.pdf . The author publications list identifies this as a Russian translation of the English article.
- Gabriel–Ulmer: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Gabriel-Ulmer.pdf . Local `TOTEX2/sources/gabriel.pdf`, `TOTEX2/sources/GabrielUlmer1971.txt`. Opened web `turn3view0`.
- Hemelaer–Rogers2021: https://link.springer.com/article/10.1007/s10485-020-09620-y . Full publisher HTML opened (`turn17view0`; relevant proof `turn20view1`).
- Laan: https://kodu.ut.ee/~vlaan/condo.pdf . Opened full144-line PDF representation, locally fetched as `TOTEX2/sources/LaanStrongFlat.pdf`, HTTP200, 88952 bytes.
- Goerss–Jardine, *Simplicial Homotopy Theory* (2009reprint): https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf . TheoremI.11.4, SectionIII.4, TheoremIII.4.8 opened to support finite-poset representatives. Local `TOTEX2/sources/GoerssJardine2009.pdf`, HTTP200, 2411067 bytes.

## Mathematical distinctions confirmed

1. The one-element monoid act being flat in the semigroup sense can mean only preservation of monomorphisms by its set tensor functor. It must not be confused with flatness of the constant right ZM-module. The paper's explicit terminology warning rules out that identification.
2. For the one-element act, finite-limit-flatness is precisely the appropriate filteredness condition after reversing variance. This gives no separator because it is already stronger than the totality under investigation.
3. Search hits using 'totally aspherical' often concern Grothendieck test-category terminology in which the diagonal is aspherical. That is a different definition from universal asphericity under ordinary final images in this prompt. No such hit is used as a result about the present class.
4. The type-map description in PRETOT is checked directly in the proof; there is no reliance on a variance-sensitive informal statement.

## Search record for the main question

Exact phrases and combinations queried on the web (two engines, with stronger coverage checks for missing primary sources):

- `totally aspherical exact colimits`
- `totalement asphérique exact`
- `homotopy flat acts category`
- `monoid one-element flat strongly flat trivial act`
- `exact colimits Ramsey`
- `exact colimits ordered graphs`
- `homotopy colimits Ramsey`
- exact titles/authors/DOIs of every requested unprovided source, including exclusions of aggregator domains when searching for primary copies

No opened source in this search proves or refutes the implication from universal contractibility of categories of elements to exactness of abelian colimits. This sentence reports the search result, not a claim that the problem is open in the mathematical literature.

## Follow-up: Ramsey and an additional primary record

- Hubička and Nešetřil, *All those Ramsey classes*, arXiv:1606.07979v4
  (3 September 2019), https://arxiv.org/pdf/1606.07979 , opened full text
  (`turn25view2`, `turn26view1`). The morphism definition at printed p.6
  preserves and reflects relations; Ramsey is defined at printed p.3.
  Corollary 4.3 at printed p.51 explicitly states the Ramsey property for
  finite simple graphs with arbitrary linear order. Theorem 3.21 is the
  broader relational-structure statement. The authored circle-character
  argument in `sections/ordered_graphs.tex` now proves Ramsey implies
  integral exactness (with common successors), so this candidate is exact.
  This exactness implication is our proved deduction, not a theorem
  attributed to the Ramsey source; no priority claim is made. Local source:
  `sources/HubickaNesetril2019.pdf`, fetched successfully with HTTP200.
- A renewed web open of the official Adámek–Reiterman1975 PDF still failed
  with internal error (`turn25view0`).
- Adámek and Reiterman (1976), *Exactness of the set-valued colim*,
  Comment. Math. Univ. Carol.17(1),97–103, found via DML-CZ and its PDF
  opened: https://dml.cz/bitstream/handle/10338.dmlcz/105677/CommentatMathUnivCarol_017-1976-1_8.pdf
  (`turn26view0`, full body `turn34view0`). Proposition I.2(a), pp.97--98,
  characterizes preservation of monomorphisms by Ore squares; I.2(b)
  characterizes equalizer preservation by filtered components; I.2(c)
  characterizes exact set colimits by filteredness (with the usual nonempty
  requirement, forced by preservation of the terminal set). Section II.3,
  p.100, repeats the false fixed-point/exact-Ab-colimit equivalence.
  More precisely, it identifies exact abelian colimits with agreement of
  pairs of endotransformations of each indecomposable set-valued functor,
  and equivalently with a fixed point for each single endotransformation.
  AKR1981 A.4, printed p.370, explicitly corrects the earlier 1975 remark:
  pairwise affine equalization (3*) was confused with simultaneous affine
  equalization for every finite tuple (3). Its counterexample also refutes
  the repeated 1976 II.3 assertion; A.4 does not explicitly cite II.3.
  II.3 must not be used as a valid theorem. The valid I.2 Set-colimit
  characterizations are separate from that false abelian assertion. This is not the
  requested 1975 paper and does not count as opening that paper. Local
  source: `sources/AdamekReiterman1976.pdf`, fetched with HTTP200.

Queries in this follow-up: `Nešetřil Rödl ordered graphs Ramsey theorem
induced embeddings partite construction pdf`; exact 1975 title with PDF.
Further C.1 metric-induction searches used `finite graph convex partial
isometry cyclic amalgamation extension`, `finite extension partial
isometry one partial isometry path cycles metric spaces`, and Solecki's
exact title *Extending partial isometries*. No retrieved theorem was
applied to the prescribed beta gluing; generic existence of an isometric
extension would not prove preservation in that specific construction.

## Follow-up: topos, shape, and constant coefficients

The detailed access record and exact theorem scopes are in
`notes/finite_topos_shape_route.md`. Primary bodies actually inspected are
Volpe (2025), Chough (2021), Blechschmidt (2018), Christensen–Flaten (2025),
Mielke (1993), and Lehner (2026). Lehner's primary PDF was successfully
downloaded after web-reader failures, to `sources/Lehner2026_shape.pdf`,
with extracted text alongside it. Its Theorems 8.9 (p.34) and 9.10 (p.40)
are constant-coefficient shape comparisons; Example 4.4 already applies
to every presheaf infinity-topos. On discrete slices the homology formula
recovers the known permutation-module calculation. It does not assert
exactness for arbitrary abelian diagrams. No inspected theorem in this
follow-up resolves totality implying exactness.

The note also contains a fully proved limitation on a possible injectivity
argument: the module Q with t acting by 2 over Z[t,t^{-1}] has zero positive
Ext from every permutation module, hence zero positive cohomology on every
discrete slice, but is not externally injective. This coefficient object
is not constant and the ambient group category is not total, so it is
explicitly not a counterexample to the main implication.

### Execution records

`code/finite_source_fetch.py`, `code/finite_source_fetch_additional.py`, and `code/finite_source_fetch_followup.py` preserve public download attempts and HTTP failures. An initial inline attempt to import the third-party `requests` module failed because it is unavailable; all actual fetches use Python's standard-library urllib. Source PDFs are research inputs, not new results; they should be omitted from the deliverable ZIP unless separate copyright permissions justify redistribution. The authored proofs and exact citations remain in the paper.

`code/finite_source_fetch_topos.py` and its output record the successful
Lehner download and content hash.
