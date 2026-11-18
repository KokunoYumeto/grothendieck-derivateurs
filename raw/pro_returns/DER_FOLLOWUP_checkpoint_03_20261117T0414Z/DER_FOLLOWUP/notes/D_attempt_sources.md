# Primary-source and search record for the final positive-monoid attempts

17 November 2026. This supplements `notes/D_positive_stabilization.md` and the localization/paths threads' attempt notes. No source below is being used to bridge an unproved step of the C_delta FreeMon comparison.

## Lawson–Wallis: the exact length hypothesis

Opened the full primary author-repository PDF:

<https://pure.hw.ac.uk/ws/portalfiles/portal/10624800/SS2.pdf>

M. V. Lawson and A. R. Wallis, *A correspondence between a class of monoids and self-similar group actions II*, International Journal of Algebra and Computation 25(4) (2015), 633–668, DOI `10.1142/S0218196715500137`.

Read §2, Theorem 2.3, Lemma 2.7, Proposition 2.8, and Remark 2.10. Their “Levi monoid” includes a homomorphism to the additive natural numbers whose zero fiber is the units. Theorem 2.3's conclusion that a Levi monoid with trivial units is free uses this discreteness. Remark 2.10 explicitly points to cancellative, equidivisible, unit-free examples without such a length. Consequently the theorem does not apply merely from the equidivisibility and cancellation inherited by a filtered colimit of free monoids. The direct limit `N→N→…` under multiplication by two is already `N[1/2]` and has no nonzero natural-number-valued length.

The portal PDF has a cover sheet: printed paper page 2 is PDF page 3, and printed page 5 containing Remark 2.10 is PDF page 6. A text search for “classifying space” found no such theorem in this source. Bibliography key: `DALawsonWallis2015`.

## Batanin–De Leger: a criterion without the missing totality implication

Opened the primary arXiv v4 PDF:

<https://arxiv.org/pdf/1712.00904>

Confirmed publisher metadata through:

<https://ems.press/journals/jncg/articles/16692>

M. A. Batanin and F. De Leger, *Polynomial monads and delooping of mapping spaces*, Journal of Noncommutative Geometry 13(4) (2019), 1521–1576, DOI `10.4171/JNCG/355`; online publication 21 January 2020. Direct DOI opening failed in the web reader, but the arXiv PDF and official publisher record were obtained normally.

The paths thread inspected classifier definitions and the proofs of Theorems 6.10/6.12, Example 7.1, Proposition 7.4, and Remark 7.5. The tower thread independently opened the statements and proofs around 6.10–7.5. Theorem 6.12 expresses the comparison through contractibility of the appropriate classifier; it does not show that totality of A makes this classifier contractible. Example 7.1 discusses monoid pushouts and invokes a module-flatness condition from Fiedorowicz. That condition was not established for the current C_delta diagrams. Thus this is a useful reformulation, not a solution. Bibliography key: `DABataninDeLeger2019`.

## Positive matrices and potentially positive words

Opened Handelman's official publisher abstract and metadata:

<https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/eventually-positive-matrices-with-rational-eigenvectors/6F27ACDF45B860FC33C27F3A81ADE878>

The article is *Eventually positive matrices with rational eigenvectors*, Ergodic Theory and Dynamical Systems 7(2) (1987), 193–196, DOI `10.1017/S014338570000393X`. The 2008 date on the page is the online-publication date, not the journal year. Full text was not inspected; only its abstract is used for bibliographic context. The proof in `D_positive_stabilization.md` is independent. Key: `DAHandelman1987`.

Opened the primary HTML introduction and potential-positivity discussion in Dinowitz–Koch-Hyde–O'Connor–Olive:

<https://arxiv.org/html/2512.13967v1>

This paper studies words carried to positive words by an automorphism, which makes clear that a positive matrix is only part of the noncommutative issue. No claimed C_delta consequence is extracted. Key: `DADinowitzEtAl2025`.

Also opened the author-maintained free-group problem list and its F34 background:

- <https://shpilrain.ccny.cuny.edu/gworld/problems/probfree.html>
- <https://shpilrain.ccny.cuny.edu/gworld/problems/Back.html>

The background reports that Clark–Goldstein, *Stability of numerical invariants in free groups*, Communications in Algebra 33(11) (2005), 4097–4104, resolved the stability-of-potential-positivity question. The original paper was **not** obtained or inspected, so it is not used as a theorem in our argument. Its DOI and publisher contents record were located, but that is not a proof audit.

O'Connor's 2026 dissertation landing page was opened:

<https://academicworks.cuny.edu/gc_etds/6698/>

The linked PDF returned HTTP 403. No statement beyond the landing page's abstract is attributed to the dissertation.

## Queries

The exact positive-matrix and potential-positivity queries are listed in §5 of `D_positive_stabilization.md`. Additional tree/Levi searches were:

- `"Levi monoid" "tree" automorphism`
- `"equidivisible" "classifying space"`
- `"monoid" "orbit" "equidivisible"`
- `"filtered colimit" "free monoids" "tree"`
- `"equidivisible" "tree" "cancellative"`
- `"equidivisible monoid" "classifying"`
- `"locally free monoid" classifying space colimit`
- `"free monoid" "coinvariants"`
- `site:ems.press "Polynomial monads and delooping" "1521"`
- `"Stability of numerical invariants in free groups" Clark Goldstein pdf`

The search located structural literature, but no theorem establishing the remaining C_delta comparison from totality or the inherited equidivisibility properties.
# Additional saturated-chart source audit (17 November 2026)

- **DABertheEtAl2015 — opened primary body.** Valérie Berthé, Clelia
  De Felice, Francesco Dolce, Julien Leroy, Dominique Perrin,
  Christophe Reutenauer, Giuseppina Rindone, *Acyclic, connected and
  tree sets*, Monatshefte für Mathematik 176(4) (2015), 521–550,
  DOI 10.1007/s00605-014-0721-4. Opened
  https://arxiv.org/pdf/1308.4260 (v6), including §§2.2–2.3,
  Propositions 2.5 and 2.7, and the statements/scope of Theorems
  5.1–5.2 in §5.1. The former propositions describe the connection
  between reversible automata and equality of a positive submonoid
  with its generated subgroup intersected with the ambient free
  monoid. The latter theorem concerns saturation inside a specified
  acyclic language; it is not a general amalgamation theorem.
  Our finite saturated-chart counterexample is proved directly.
  The initial Luxembourg repository PDF open timed out; arXiv then
  opened successfully. Metadata cross-checked against the author
  repository record https://orbi.uliege.be/handle/2268/174949 in
  search results. Web references: turn577965919view0,
  turn395519187view0, turn395519187view1.

Exact new searches:

- `free monoids amalgamation saturated submonoids free groups bifix codes`
- `amalgam free monoids free factor saturated submonoid`
- `"amalgamation" "free monoids" "unitary"`
- `"free monoids" "amalgam" "codes"`
- `"Acyclic, connected and tree sets" arxiv`
- `"amalgam" "bifix" "free"`
- `"free monoids" "amalgamation property"`

Other search hits were not opened or used as mathematical sources.
No general positive-chart amalgamation theorem was found. The direct
counterexample in `D_saturated_amalgam_obstruction.md` shows that
saturation and free-factor hypotheses alone are insufficient.

# Additional invariant-cut-order source

- **DABodirskyBodorMarimon2025 — opened primary body.** Manuel
  Bodirsky, Bertalan Bodor, Paolo Marimon, *Taking model-complete
  cores*, arXiv:2512.21278v1, 24 December 2025. The paths thread
  supplied this exact source; this thread independently reopened
  the institutional PDF and read Lemmas 4.34–4.35 with proofs,
  printed pp.33–35. Exact URL:
  https://fis.tu-dresden.de/portal/files/81089088/2512.21278v1.pdf .
  The arXiv PDF direct open returned DisabledError; the institutional
  PDF succeeded. The result classifies the indicated definable
  orders by signed lexicographic coordinate comparisons. It is
  precedent for the cut-order attempt and supplies no C_delta or
  monoid comparison theorem. Web references: turn290196504view0,
  turn606165394view0, turn606165394view1, turn898284020view0.

