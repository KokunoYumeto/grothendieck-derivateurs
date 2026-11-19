# Les Dérivateurs, VII-c — audit and commentary report

## Scope and completion

The audit covers the complete supplied passage, **manuscript pages 108–171**. Every supplied PDF leaf was read and visually compared with the transcription, including formulas, diagrams, indices, footnotes, editorial brackets and the seven doubtful readings. The package contains **38 commentary blocks**, **265 claim records**, **59 correction records**, and **20 bibliography entries**. The built reader has **57 pages**; its standalone overview occupies **3 pages**.

Three pagination systems remain distinct. The attachment contains 39 leaves, numbered 1–39 in the correction register. Their printed edition pages are 69–107. The task identifies the corresponding leaves of the complete editors’ file as 71–109, counting preliminary leaves. Manuscript markers run from 108 to 171. `support/coverage.md` supplies the complete leaf map and a crosswalk for every original editorial flag. The marker for manuscript page 114 occurs at the end of leaf 3 although its body begins on leaf 4; the same distinction applies to manuscript page 168 at the boundary of leaves 36 and 37.

The PDF edition controlled every reading. Mathematical plausibility was not used to substitute an emendation for what the edition prints. The corrected transcription and its unchanged original are both supplied. Printed mathematical errors are explained in the commentary and register, not silently rewritten in the source.

The continuity index was read throughout. It contains the earlier Chapter V and VI discussions relevant to finite tests, ind-representation and monodromy, and VII-a through manuscript page 57. It contains no VII-b commentary. We refer to the available earlier blocks, but do not certify an overlap check against unavailable VII-b material. The indexed symmetric-group example here adds the strict fibred realization needed for the hypotheses of this passage.

For antecedent definitions we consulted the complete Chapter VII, manuscript pages 28–31 and 99–107, and Chapter V, manuscript pages 45 and 51–52. These settle the definition of a type map, the exact general fibred hypotheses, and the source’s meaning of “finite category.” They do not enlarge the transcription-audit coverage claimed above.

## Mathematical findings

### The geometric path comparison and its multiplication

The main positive conclusion survives. In the all-arrows situation, the canonical span

\[
\operatorname{Ch}(X;a,b)\ \longleftarrow\
C_{\mathbf N^{\mathrm{op}}}(a,b)\ \longrightarrow\
\operatorname{Ch}_{\infty}(X;a,b)
\]

consists of weak equivalences. The commentary proves this for the specified models rather than inferring it from finite unbased tests.

The opening block gives a comma-category proof that a sequential fibred Grothendieck construction maps by a weak equivalence to its filtered colimit. It applies to each fixed-endpoint diagram, without a faithfulness hypothesis on the transitions. The explicit truncations `j ↦ min(j,k)` then contract a finite oriented interval relative to its initial endpoint. This fills the constant-path lemma promised in the manuscript and left unwritten at page 170.

For eventual alternating paths, two cofinal families of positive-length supports have opposite endpoint parities. One gives incoming Cartesian lifts and the other outgoing coCartesian lifts. Filtered colimits of their lift categories prove smoothness and properness. The zero-length diagonal is explicitly excluded from the fixed-stage fibration assertion. Padding need not preserve Cartesian arrows: contractibility of the categories of choices suffices.

For the all-types category, the incoming-lift contraction proves smoothness. Whiskering by endpoint arrows gives transport between strict fibres; the two explicit backtracking cancellation diagrams make it invertible up to categorical homotopy. Collapse maps identify it with transport between under-comma categories. Quillen’s Theorem B therefore makes strict endpoint fibres homotopy fibres (Quillen, 1973, §1; Maltsiniotis, 2005, Theorem 1.2). The intermediary’s fibrewise comparison with eventual paths transfers that property to it. Its total equivalence with the all-types category then proves the other fibrewise comparison.

A separate development proves compatibility with ordinary path concatenation. It treats the category of composable pairs over `X³`, proves its strict-fibre theorem, and cancels the constant-path sections in the localized slice category. The two projections identify its fibre comparison with the product of the individual comparisons. Consequently the equivalence on loops preserves multiplication and units in `Hot`, not merely the underlying homotopy type.

Even translation is also the identity in `Hot`, including on every fixed-endpoint category. Asymmetric finite-stage padding realizes `T⁻²`; its collapse gives a natural transformation after passage to the all-types category. Cancelling the repaired comparisons proves the identity.

### False intermediate assertions and their repairs

The general change-of-sequence assertion in pages 117–123 is false under the hypotheses actually stated. The counterexample uses `T = FIᵒᵖ`, fibre `B S_n`, and extension of permutations along injections by the identity on the complement. Parallel injections induce naturally isomorphic functors. The base has the required cofiltered, countably coinitial preorder and an associative disjoint-union operation with terminal unit and natural projections. Nevertheless a morphism of cofinal sequences induces the nonsurjective shift of the finitary symmetric group on the ordinary colimit, although its ind-object comparison is an isomorphism. This disproves the general assertion while leaving the later geometric theorem intact.

The category of cofinal sequences is contractible whenever a bifunctor with two natural projections and one cofinal sequence exist. The commentary gives the explicit contraction. Unique comparisons follow for a diagram already known to send all arrows to isomorphisms; that premise is retained.

The statement that `Ty → Ty_o` fails even the connectedness lifting tests is verified directly. The alternating interval `0 → 1 ← 2 → 3` has precisely two endpoint-preserving monotone maps to `0 → 1`, while both endomorphism monoids are trivial. Because the preorder retains the same objects, both relevant lift categories are discrete two-point categories.

The properness assertions for `Ch(X)` and `C_(Nᵒᵖ)` are false. For `X = [1]`, the empty path at 0 has no outgoing lift of `(id_0, 0 → 1)`. In the all-types category a map from the empty type must still have empty target; in the sequential category an arrow out of stage 0 cannot reach a positive stage. Both outgoing lift categories are empty. Opposing a total Grothendieck construction also reverses its base; reversing paths inside its fibres does not do that.

The sequential padding formula on page 168 has an independent defect: it produces `1_D * δ_(m,n) * 1_D`, not the required `δ_(m+1,n+1)`. The proposed slice object need not exist. Smoothness is true by a replacement argument: the lift category is fibred over a tail of `Nᵒᵖ`, with contractible positive-stage fibres and an explicitly handled empty or singleton zero-stage fibre. The section called “asphérique” on page 166 is only a weak equivalence; empty over-comma categories above positive stages disprove the stronger wording.

### Finite tests and external Hom

The source defines “finite category” by finite object and arrow sets. Its nerve need not be homotopy finite. `B(Z/2)` and the skeleta of infinite real projective space disprove the compactness inference. Restricting to homotopy-finite tests repairs that inference by changing the test category; it is not presented as the original convention. The elementary finite-presentation calculation in `Cat hot` remains valid.

An explicit telescope of degree-two maps of circles gives an essential map to `K(Z,2)` that vanishes on every finite stage. Its cellular cocycle `(1,0,1,0,…)` cannot be a coboundary, since that would force an integer to equal `−1/3` in the 2-adic integers. It is invisible even to nerves of all finite categories: their finitely generated fundamental groups have cyclic image in `Z[1/2]`. The associated ind-object map is therefore not an epimorphism. The cohomological tools are classical (Hatcher, 2002, §3F and Theorem 4.57). For conservativity the commentary refers to the earlier example and to Arlin and Christensen (2023, Theorem 2.1).

The six-object suspension of the four-object circle poset corrects the bounded-degree explanation on pages 133–134. A natural-transformation loop evaluates to the fundamental class of the two-sphere; repeated concatenation realizes every integer degree with the same four-arrow parameter. Localization of strict diagrams nevertheless really does fail parameter invariance: restriction along the circle poset’s weak equivalence to `B Z` maps a trivial automorphism group to one containing an infinite cyclic subgroup. The intended concern is justified by a different proof.

The absolute arrow-category comparison for parameter `[1]` is always a weak equivalence. Its strict endpoint fibres can fail to be path spaces. For arbitrary parameters, a Thomason-fibrant target still need not make the functor category a derived mapping space: a fibrant poset model of `B(Z/2)` gives a counterexample on components (Raptis, 2010, Theorem 2.6).

The separate closure assertion about fibrancy of `Fun(Y,C)` is also false. A complete development constructs an underlying fibrant `C₂`-poset `Q` whose fixed subposet is a nonfibrant finite crown `D`, by attaching free orbits of horn cells. The transport category `E = Q ⋊ C₂` is fibrant: group labels on each contractible subdivided horn can be trivialized, extended using fibrancy of `Q`, and restored. There is an exact decomposition

\[
\operatorname{Fun}(B C_2,E)\cong E\amalg(D\times B C_2).
\]

The nonfibrant `D` is a categorical retract of this functor category, which therefore is not fibrant. The fixed-point check uses the explicit Dwyer-map pushout descriptions of May, Zakharevich, and Stephan (2017, Lemmas 4.7–4.8). This settles the assertion directly; non-cartesianness alone would not have done so.

The mapping-path replacement is not generally a Thomason factorization. Its constant-path inclusion can fail to be a sieve and hence fail to be a Thomason cofibration. Taking the target to be terminal makes `bar f` equal to `X′ → e`; nonfibrant `X′` disproves universal Thomason fibrancy. The eventual-path replacement remains smooth and proper and computes homotopy fibres. Its triviality criterion follows from two-out-of-three and the homotopy-fibre theorem.

## Corrections and editorial decisions

The register contains 49 `edition_slip_kept`, three `transcription`, and seven `doubt_resolved` records. Every original `[sic]` flag is covered. The three definite transcription corrections restore the printed misspelling **composititon**, the missing underline on `Ch` in the finite-support membership display, and the solid curved `bar f` arrow on manuscript page 170. Resolving the doubts also restores the ordinary functor-category underbrace on page 136 and the projective-system underlines on page 143. The remaining doubtful typography is confirmed as transcribed.

The composite tilde on manuscript page 164 stays in its printed trailing position. The register explains conventional notation without silently normalizing the source. Wrong primes, inconsistent exponents, grammatical slips and invalid mathematical annotations printed in the edition likewise remain in the transcription, with their implications explained separately.

Typesetting repairs are distinguished from emendations. They provide explicit empty TikZ nodes where vertical arrows target blank cells, define the source’s zigzag style, resolve the French ordinal macro’s collision with the source’s `No`, and preserve the normal mathematical font encoding under `fontspec`. Two wide displays are scaled only enough to fit the text width. A long monospaced editorial note is set one size smaller. Marginal page labels have explicit struts and separation to prevent collisions at page starts. Formulas, labels and retained printed errors are unchanged.

The supplied builder and companion style are unchanged. The layout extension switches commentary and overview to English hyphenation, retains French for the source, and displays the manuscript page rather than the entire anchor-matching substring in commentary headings.

## Reference verification and credit

Every bibliography entry has a URL or DOI and a `verified:` note giving the precise scope checked. Established cumulative keys are reused. Principal theorems and the specific proof steps used were read in primary sources: Quillen A/B, the asphericity criteria, poset model structures, diagram-comparison propositions and equivariant pushout lemmas were checked directly.

Version distinctions are explicit. Stevenson is cited by Theorem 21 of arXiv version 2; Shoikhet’s numbering refers to arXiv:1412.0317v4. May, Zakharevich, and Stephan are cited in published author order, using published Lemma 4.8, numbered 4.9 in the author preprint. The Thomason (1979) entry is limited to verified publisher metadata; the fibred convention was checked in Shoikhet and the required comparison is proved here.

The historical references are specifically connected to this passage: derived diagram categories and SGA 5 in *Pursuing Stacks*, §69, and unbounded paths in the letter to Thomason of 2 April 1991. Comparisons with simplicial localization, locally constant diagrams and coherent diagrams retain the hypotheses needed to present strict diagrams by a homotopically adequate model.

Developments marked `ours` are proofs supplied in this commentary. Each states which literature was checked and where the particular application or correction was not located. No priority is claimed. Independent internal review checked the new counterexamples, transport variances, fibre comparison, translation and multiplication compatibility. This is not external peer review.

**Credit:** commentary, audit, mathematical developments and this package’s assembly were AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. No later editorial step is certified, and the commentary is not attributed to any person.

## Limits retained

The full conditional assertion on page 129, with its extra locality hypothesis on the ind-object `H`, is not disproved merely by failure of the preceding finite-category compactness argument. The audit marks the inference as invalid while keeping that stronger conditional separate.

The stronger question whether the particular geometric padding comparisons are invertible already in `Cat hot`, or admit the desired actual inverse functors, is not settled by the general `FIᵒᵖ` example or the weak equivalences proved here. A definitive theorem for that exact stronger question was not located in the checked sources. This is a limit of the audit, not a declaration of an open research problem today.

The completed geometric comparison, transport and multiplication results concern the all-arrows situation of sections 12–13. Extension to every admissible relative pair `(X,Σ)` requires its own hypotheses. Multiplication compatibility is proved in the homotopy category; no further claim of an equivalence of coherently multiplicative models is made.

## Build and inspection

`build_reader.py DER_VII-c` validates anchors, the six file schemas, register values, unique claim identifiers and bibliography membership of every commentary and overview citation. LuaLaTeX, BibTeX and two further LuaLaTeX passes complete successfully. The build was also checked using an independently bootstrapped local runtime. All package source files were scanned for invalid control characters.

The final log contains no compilation errors, unresolved citations, missing glyphs, overfull boxes or underfull boxes. Page-bound checks find no text outside the paper. Every reader page was rendered and visually inspected; wide diagrams, the repaired arrow, bibliography, block boundaries and overview received additional checks. Ordinary margin-label placement notices and the French package’s legacy-list advisory concern layout compatibility, not unresolved mathematical or typesetting errors.

`support/validation.json` records final counts and automated checks; `support/build_logs/` contains the successful logs. The bootstrap reproduces the minimal environment’s local LuaLaTeX repair from bundled, checksum-verified CTAN archives. The integration script assembles the archived fragments and applies documented changes only. The inspection script reproduces page renderings and bounding checks. The supplied attachments were not overwritten.
