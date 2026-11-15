# Independent exact-path supplement

## Deliverable

`sections/E_path.tex` contains E.20–E.27. E.20–E.24 give complete proofs for the actual integer-fence eventual-path category, actual even translation, actual left- and right-padding comparisons, and the manuscript's actual left-right concatenation for the canonical block D=(+,-), with Sigma all arrows. E.25 extends actual collar weak equivalences and literal even translation to every admissible Sigma, and proves the resulting relative operation defined and unital. E.26–E.27 retain the precise remaining arbitrary-cofinal-type and arbitrary-block/relative-associativity claims as Open in this audit. It can be input at the end of Part E. Its non-elementary categorical input is Quillen A/B. Shoikhet2016 provides a related finite-stage identity-collar calculation; the half-fence comparison is proved independently. It does not rely on restricted Yoneda conservativity or faithfulness.

## Primary source opened independently

- Boris Shoikhet, *On Evrard's homotopy fibrant replacement of a functor*, arXiv:1412.0317v4, 7 November 2016: https://arxiv.org/pdf/1412.0317 (opened full PDF in web tool, ref turn71view0).
- Exact indexing in Section 2.1, equations (2.2)–(2.5): the unique inclusion m→n is i↦n−m+i, so its transition pads the left end. This was checked, not inferred from the general description of a cocylinder.
- Section 3.2.1, Proposition 3.3, PDF pages 25–26: identity-pair sliding through a finite zigzag. E.23 gives an explicit compatible half-fence version and supplies its continuous realization homotopy independently.
- Theorem 2.8 and Lemma 3.1 were inspected but are **not used**: the draft dependence was removed after an exact indexing audit of the zero-length stage. No identification of the manuscript's colimits with a categorical cocylinder is assumed in the final proof.
- Theorem 1.8 records Quillen B in the under-comma variance used in E.21. The parent also has Quillen's primary 1973 text.
- Journal primary metadata: https://tac.mta.ca/tac/volumes/31/34/31-34abs.html ; volume 31, no.34, pages 989–1015, published 26 October 2016.

## Checks and limits

The finite-support proof distinguishes positive even-even intervals (both endpoints sources) from positive odd-odd intervals (both sinks); the zero-length diagonal is never called a Grothendieck fibration. The lift category at the filtered union is not assumed to have a Cartesian lift. Its weak contractibility is proved by finite diagrams and filtered simplicial colimits.

For smooth+proper ⇒ strict fibre = homotopy fibre, the supplement writes both projections of the category of arrows over a base arrow, the appropriate comma categories, their deformation retractions to lift categories, and the natural transformation giving the Quillen-B base-change condition.

Translation is proved in the localized slice by cancelling the constant-path weak equivalence and then taking derived fibres. The natural strict-fibre comparison identifies the result with the actual translated fibre map. This avoids a possible phantom-map gap in an argument only checking finite stages.

For one-sided models, the final proof uses explicit functors phi_j on the negative half-fence, inserting a pair of duplicate vertices at -j. Consecutive precomposition functors are connected by a natural transformation in the direction of the original fence edge. They become the identity on each finite diagram once the insertion is outside its support. Concatenating their realization homotopies gives a continuous homotopy from right-collar insertion to the identity, stationary near the limiting time on each nerve simplex. Finite diagrams and nullhomotopies in the two-sided model can be shifted into the half-fence; the collar homotopy handles basepoints and makes the half-fence inclusion a weak equivalence. The two-sided derived-fibre theorem then transfers naturally. This proof does not need Shoikhet's strict prefibration assertion or a general homotopy-colimit theorem.

For actual concatenation, the category of composable pairs is treated over X^3. Its constant section is a weak equivalence and its strict fibres are shown to be derived fibres, using the middle-coordinate fibre and then the remaining two coordinates. Cancellation of constants in this localized slice proves compatibility with ordinary path concatenation, and the projection identities identify the comparison on a product fibre as the product of the two single-path comparisons. This is stronger than a bare isomorphism of path-space homotopy types.

No finite counterexample is introduced in the supplement. `code/e_fence_check.py` and its saved output provide a bounded off-by-one/parity audit of the universal formulas: 31 insertion positions on 65 fence vertices on each half-fence, and all 143 walking-arrow half-fence paths of lengths 0,2,4,6,8. The program checks functoriality, component arrows, naturality, endpoint preservation, eventual stationarity, and preservation of the geometric direction of every noncollapsed edge. The general theorem is supplied by the written proof, not inferred from these bounded checks.

## Exact manuscript scope and crosswalk suggestions

- Relative paths and admissibility are defined at VII manuscript pages **65–67** (not page60): backwards arrows lie in Sigma, Sigma contains identities and is closed under composition, and the subcategory is full. The latter is essential: collar homotopy components are not required to lie in Sigma.
- The type category is specified combinatorially at VII ms50'–53; useful length is the number of constant-sign runs, ms75–76. The manuscript's cofinality is for its reachability preorder, ms99–102, and is equivalent to unbounded useful length, ms138. E.26 includes these exact definitions and does not substitute homotopy cofinality of a functor.
- Section12 declares Sigma=all arrows at **ms137**, so all of ms150–156 falls under E.20–E.24's all-arrows scope.
- At **ms145**, t_n=(Delta+Delta−)^{2n} with symmetric collapse delta_p*id*delta_p has support vertices [-2n,2n], exactly the model in E.20.
- At **ms147**, T^p sends a_j to a_{j-p} and likewise shifts the edge indices. Odd p exchanges the two parity models on the **same X**; at ms148 it acts on their disjoint union. Therefore E.22/E.25's formula T²c(j)=c(j−2) is literally the manuscript map. No passage to X^op is part of this particular definition.
- Suggested E.16 row VII108–115: retain E.8 for the ordinary-colimit comparison, add **E.26** for the remaining specified all-type projection. Do not imply that ordinary path-space comparison identifies the original projection to Ch_Sigma automatically.
- Suggested E.16 row VII116–120: **E.23/E.25 prove the concrete collar comparisons; E.26 retains arbitrary left-cofinal type systems and their canonical/transitive comparisons as Open.**
- Suggested E.16 row VII125–127: **E.24 proves the all-arrows canonical alternating-block operation; E.25 gives relative canonical existence/units; E.27 retains relative associativity and arbitrary-block independence with their original quantifiers.**
- Suggested E.16 row VII150: **E.22 and E.25 prove the literal T² statement directly**, including arbitrary admissible relative classes in the canonical model.

The smallest uncovered changes to E.24's hypotheses are already a proper admissible Sigma with D fixed, or the three-letter alternating block (+,-,+) with its specific left/right/symmetric transitions. These are explicit gaps in the current audit, not claimed counterexamples or claims of research-level open problems. E.7/E.9 remain conditional derived replacements and do not decide these raw comparison and composition assertions.
