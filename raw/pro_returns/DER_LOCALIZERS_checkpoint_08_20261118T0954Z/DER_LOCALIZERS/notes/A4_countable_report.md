# A.4 countable-source comparison: rechecked background

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 18 November 2026.

## Status and provenance

The candidate countable-enlargement theorem found during this research block is already contained in the supplied REVLOC G.7. It is **not** recorded as new movement of the A.4 research gate. We read REVLOC G.6 and G.7 in full. Their `Nul` is exactly this return's `Nul_2`; no weakening or change of target family is involved. The independent compact-Brownian proof in A4.2 rechecks the part needed for the primary intersection `W_*`. The exact countable-separator corollary is now explicit, but it is a consequence of that existing background theorem.

The new section is `sections/A4_countable_review.tex`; its single statement id is **A4.2**. It proves accessibility of `W_*` and gives the countable form of the same ordinary-nullification test. Neither the existence of a third element nor the full-fibre set-size question has changed status.

## Primary source and exact compactness input

Opened Dennis Sullivan, *Genetics of homotopy theory and the Adams conjecture*, Annals 100 (1974), 1–79, at the primary scanned paper hosted at `https://math.univ-cotedazur.fr/~cazanave/Gdt/ImJ/Sullivan.pdf`.

- Printed pp. 34–37: completion is a represented inverse limit of compact Brownian functors; Property I identifies maps from an arbitrary CW source with the inverse limit over finite subcomplexes; Example II applies this to targets with finite homotopy groups.
- Printed pp. 39–41: the completion indexing category is filtering in the inverse-system direction; bounded Postnikov targets give the same represented completion. The latter is a comparison of represented functors, not an unproved categorical cofinality statement.
- Printed pp. 44–48: Theorem 3.1 and its proof identify completed homotopy groups under the finite-generation hypotheses used for spheres.
- Printed p. 49, Property iii and footnote: the countable-type condition gives a countable inverse system. Finite spheres meet it. The mapping-set inverse-limit formulas are explicitly repeated there.
- Printed p. 52: the construction and propositions extend to completion at one prime.
- Printed pp. 56–57: arithmetic reconstruction. The section also independently verifies the sphere's arithmetic square by the exact ring sequence, so no arbitrary-source completion assertion is needed.

Web-opening refs from this block: `turn273714090view0`, `turn372501910view0`, `turn146879076view0`, `turn146879076view1`, `turn306472097view0`. These are opening-ledger identifiers, not citations meant to appear in the TeX bibliography.

## Exact inverse-limit safeguard

For a finite subcomplex K and a finite completion coordinate T_j, nullity of X into the completed sphere does **not** imply `[X,T_j]=*`. The proof never uses that implication. It uses the finite-set compactness conclusion that there are a finite larger L and later t such that the image `[Sigma^s L,T_t] -> [Sigma^s K,T_j]` is singleton. The later coordinate may depend on K, j, n, and s. Countably many such requirements can be imposed while enlarging a countable complex.

Formula A4.2.2 is an identity of represented ordinary homotopy functors valid on arbitrary CW sources. This handles phantom components directly. There is no appeal to a generally false interchange of `pi_0` with a homotopy inverse limit.

## Audit of supplied G.6 and G.7

G.6's squaring map is on `Omega S^n_(2)`, so it multiplies every homotopy group by two; it is not a degree-two sphere map. For odd n, the only infinite homotopy group is `Z_(2)` in degree n−1. The tower's derived limit is `Z_2/Z_(2)`, a nonzero rational vector space. Its one-dimensional rational summand makes `K(Q,d)` local for all d by varying odd n and looping. The rational-cohomology comparison then forces rational acyclicity. The arithmetic square identifies the original and completed null tests on such sources. All-component assertions are retained.

G.7 constructs a strict simplicial compact metrizable Kan model by the Bousfield–Kan cosimplicial resolution. The supplied Reedy-fibrancy verification uses linear codegeneracies and cofaces other than the outer unit; its correction `c + d^{j+1}(a_j-s^j c)` fixes the next matching equation while preserving the previous ones. The matching maps are split surjections of simplicial abelian groups. Totalization therefore gives the required Kan model. Its levels are closed subsets of countable products of finite sets.

The bounded-extension proof then works with actual simplicial maps and compact Hausdorff spaces of assignments. Closed extension-image sets have the finite intersection property; a countable basis for the countable source lets one choose countably many witnesses. A map from the final union extends globally by another nested compactness argument and is consequently nullhomotopic. This directly treats phantom maps and does not assume the singular complex of a countable CW complex is countable. The separate cellular cycle-boundary enlargement handles rational acyclicity. No fault was found in these steps.

The Sullivan proof in A4.2 is independent of the strict-model construction and supplies the stronger primary coefficient condition by adding `Z[1/2]` boundary witnesses. The latter modification is formal because `Z[1/2]` is countable and acyclicity is a finite-support condition.

## Other sources opened during the abandoned novelty check

These sources were inspected for the compactness/countability route but are not needed in A4.2:

- Lurie, *DAG XIII: Rational and p-adic Homotopy Theory*, `https://people.math.harvard.edu/~lurie/papers/DAG-XIII.pdf`: Sections 3.1–3.3, especially the definition of p-profinite spaces, Theorem 3.3.3, Proposition 3.3.10, and Notation 3.3.14. It supplies related pro-space/materialization comparisons but no countability statement was imported.
- Quick, *Some remarks on profinite completion of spaces*, arXiv:1104.4659v2, `https://arxiv.org/pdf/1104.4659`: introduction and the finite-type comparison discussion. It confirms the distinction between Artin–Mazur pro-objects and Sullivan realization; no theorem from it is used in the proof.
- Adams, *Localisation and Completion*, Proposition 6.4: found only as a search lead; the PDF itself was not opened. No assertion in A4.2 depends on this unopened item.

## Next research direction

After recording this recheck, return to a distinct A.4 construction or classification route. Do not count the countable corollary, repackaging of G.7, or its source verification as a newly smaller obstacle under the user's stopping rule.
