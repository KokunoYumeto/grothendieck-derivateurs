# PATHS Parts A/B and the sequential part of C: source and proof record

This work was produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The text below records the scope actually checked in this session; previous AI answers and reviews were treated as mathematical drafts.

## Files supplied to the main paper

- `sections/A_definitions.tex`: A.P1–A.P2, exact component localization and sequential comparison span.
- `sections/B.tex`: B.1–B.9, the literal inclusion, the restricted hammock comparison, proved cases, the canonical map to localization, and the unresolved general inclusion.
- `sections/C_paths.tex`: C.P1–C.P5, coherent type reparametrization, all E.26/E.27 comparisons, and a finite counterexample to a Cat-hot inverse for q_L.
- `research/B_results.json`: one registry entry for each of these sixteen statements.
- `research/B_references.bib`: only references used by these sections, with current-session reading scope.

## Sources read

The manuscript transcription was read at VII ms.27–57 for type maps and concatenation, VII ms.58–78 for path morphisms, admissible markings and ordinary localization, and the companion's blocks at VII ms.86, 94, 103–109 and 117 for interval-map contractions, parallel type maps, Grothendieck variance and the previous sequential argument. The CATHOT path section and its review were read, including E.20–E.27 and the q_L discussion. CATHOT E.4 was read directly to check the danger of using ind-isomorphisms or merely stagewise unbased homotopies. Its locally conjugate shift obstruction is precisely why the first attempted telescope argument was rejected.

Dwyer–Kan, *Calculating simplicial localizations* (1980), was opened as the supplied full PDF and extracted to text. Definitions 2.1 and 5.1, Propositions 2.2, 3.1 and 5.5, and Definition 6.1/Proposition 6.2 were read. Dwyer–Kan, *Function complexes in homotopical algebra* (1980), was opened as the supplied full PDF; Section 4, including Propositions 4.4–4.5 and Corollary 4.7, was read. These identify the weak-vertical mapping construction; they were not misquoted as a theorem about arbitrary verticals.

Arakawa–Cnossen, *Hammock localization via Segal animae*, arXiv:2608.19870, was read from the supplied LaTeX source: the definition of Zig and the fibre categories, the hammock anima and main theorem, the proof using fixed-shape colimits, the fraction discussion and fibrant-object theorem, the exact simplicial-category comparison, and the Reedy proof. Its arXiv abstract/metadata were independently opened. The exact source numbering is Definition 1.7, Theorem 1.9, Corollary 1.11; Theorem 3.26; Definition 4.3, Theorem 4.7, Proposition 4.8, Lemma 4.16 and Remark 4.18. A script records these counters, including the shared numbered-equation counter. No successful local compilation of this reference was required or claimed.

Chachólski–Scherer, *Homotopy theory of diagrams*, the institutional 2001 preprint, was opened in full through the web reader; Theorem 26.8 and Corollary 26.9 were read as an independent source for the natural Grothendieck homotopy-colimit theorem. Kerodon was opened at tags 01LA, 01JX, 01E7 and 02NX for coherent-nerve mapping spaces, detection of equivalences, restriction on functor categories, and cofinality. The enriched-type proof was independently reviewed by the agent responsible for colimits and KT; its notes are in `research/A_path_audit.md`.

## Decisive conclusions

The restricted Grothendieck construction is the hammock mapping space for every wide marking. The paper gives the actual simplicial reduction map: pull an n-simplex of the fibred total category back to its first type, then reduce the resulting width-n hammock. This is a simplicial map and strictly respects concatenation. The Reedy argument verifies that the ordinary simplicial-set colimit has the correct derived colimit, so the conclusion concerns this specified map, not only an abstract homotopy type.

For markings contained in the isomorphisms, the full all-type path category is actually equivalent to the discrete Hom-set in Cat hot. The uniform zigzag is `id <- pad <- T -> i effect`, where pad appends a positive identity edge and T puts the total effect on that last edge. Prefix composites provide the natural transformation into pad. This corrects the overly compressed “initial factorization object” explanation in Lead 2: a one-edge path is not generally initial in the total all-type category, because its type need not map to the target type.

All three exact targets in CATHOT E.26 are settled for arbitrary wide markings, and E.27 is settled for every block containing both signs. The key extra structure is the category P(tau,sigma) of interval maps and natural transformations. Its classifying space is empty or contractible, and the full path diagram carries an actual enriched action of these categories. The ordinary type category and every preorder-cofinal sequence map homotopy finally to the reachability preorder after this coherent descent. The first finality is checked by an actual comma category, contracted by `sigma*tau -> tau` and `sigma*tau -> sigma`; the second comma is a nonempty upward-closed subset of N. This proves weak equivalence of the specified sequence-to-total map and not merely independence of abstract homotopy types. The resulting canonical comparisons transport strict all-type composition to the manuscript's left/right/symmetric operation.

This does not identify arbitrary-vertical paths with the modern localization mapping space. The restricted diagram does not admit the same type enrichment: components of a natural transformation of interval maps can be forward arrows and need not be marked. Thus the new E.26/E.27 proof is independent of J and does not covertly assume it.

The q_L question in Cat hot is refuted by the four-object crown (two minimal and two maximal points), all arrows marked, endpoints at one minimum. Its universal-cover category is the integer fence. Endpoint-fixed transformations lift and move a fixed evaluated vertex by at most one. A finite zigzag between id and q_L r would therefore bound the distance of every positive-coordinate lifted value uniformly. Null-winding paths going 4N steps out and back contradict this. This is a finite relative-category counterexample, strengthening the initially noticed infinite-fence example. It does not contradict q_L being a weak equivalence.

There is a coherent map Q from the full all-type path space to the localization mapping space. It is constructed by inverting, **as an equivalence of diagrams**, the interval-localization precomposition maps `Fun([number of plus edges], C) -> Fun_relative(I_tau,C)` on endpoint fibres. QJ is the hammock comparison, so J is split monic in Hot. Separate pointwise choices of inverse were not used.

## Computation record

`code/b_path_search.py` constructs the complete category of paths with word length at most L in each chosen finite poset. It retains each type map as part of an arrow and computes every composable pair, so parallel type maps and their relations are not discarded. It computes H0 and H1 over F2 by collapsing a spanning forest and row-reducing all triangle relations.

The family comprises [1], [2], a three-object span, a three-object cospan, and the four-object crown, every composition-closed wide marking, and endpoint pairs (0,0) and (0,n-1). There are 66 cases at L=3 and 66 at L=4. All 132 comparisons have equal H0 and H1. At L=4 the largest examined category has 16,229 nonidentity arrows and 2,525,024 nondegenerate 2-simplices. The complete per-case outputs are `code/b_path_search_L3.jsonl` and `code/b_path_search_L4.jsonl`. No unbounded equivalence or counterexample is inferred from these finite computations.

`code/b_crown_checks.py` verifies the four-object base, unique cover lifts at all residues, all 85 endpoint-fixed paths and 387 endpoint-fixed transformations at parameter length six, and the out-and-back family for N=1,...,8. Sixty-three of the length-six paths have zero winding. Output: `code/b_crown_checks.txt`. The proof in C.P5 handles every N and every prospective inverse functor, beyond the finite checks.

`code/b_reference_audit.py` records the source theorem numbers and summarizes the two finite-search output files. Output: `code/b_reference_audit.txt`.

Commands used for the substantive computations:

```bash
python PATHS/code/b_path_search.py --length 3 > PATHS/code/b_path_search_L3.jsonl
python PATHS/code/b_path_search.py --length 4 > PATHS/code/b_path_search_L4.jsonl
python PATHS/code/b_crown_checks.py > PATHS/code/b_crown_checks.txt
python PATHS/code/b_reference_audit.py > PATHS/code/b_reference_audit.txt
```

## What remains unresolved

B.8 retains the general weak-equivalence assertion for J, separately for an arbitrary wide class, a two-out-of-three class, a saturated class, a homotopy calculus of fractions, a model category, and a category of fibrant objects. There is no verified counterexample and no complete higher-coherence proof in this work. The local sweep of one backward square is explicitly verified: after padding to -+-, the vertical components are `(id,w,w',id)`. Forward squares are handled by equality of composites. Making these sweeps into a compatible replacement for every higher simplex is the remaining step.

The source theorems on short fractions identify the restricted three-arrow category. With two-out-of-three, its vertical maps are automatically marked. This does **not** imply that its inclusion into the full all-type category is a weak equivalence. The distinction is retained even in the model and Brown cases.

The three-object chain with only the long edge marked is a concrete smallest-size case remaining in the tested family that is not covered by the already-invertible/all-arrows results. It is saturated, as witnessed by the walking split retraction, but no claim is made that it is a counterexample or globally minimal among all possible categories.

The stratified interpretation based only on components of Sigma is refuted separately in E.10 of the main paper; this section does not duplicate that result. The finite crown computation does not address a more restrictive Cat-hot invertibility statement for arbitrary chosen finite path-length bounds or for classes of categories satisfying additional uniform contraction hypotheses.

## Literature-search scope

Searches used the exact paper titles above and the phrases “Grothendieck path categories arbitrary natural transformations hammock localization”, “zigzag category natural transformations not weak equivalences simplicial localization”, “hammock vertical arbitrary localization”, and “Dérivateurs hammock”. A MathOverflow discussion from 2020, with a 2024 response, asks essentially the same unrestricted-vertical question and points to three-arrow calculus. It was used as a lead only, not as a primary theorem or proof. No checked source from this search proves the full assertion B.8. “Open” in this paper therefore means not settled in this audit, not a claim about the global state of the literature.
