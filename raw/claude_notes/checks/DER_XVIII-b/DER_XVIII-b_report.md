# Chapter XVIII-b: audit and commentary report

The commentary and audit were produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. This report concerns the present work only; it does not certify any subsequent assembly or editing by another system or a human editor.

## Scope and source authority

We read the supplied transcription throughout and checked the complete attached 45-leaf PDF. The excerpt runs from the unmarked tail of manuscript p. 126 through manuscript p. 228, beginning inside Proposition 4.5.13 and ending inside the proof numbered 4.9.6.7. Its numbered manuscript markers are 127–228; the opening tail must not be mistaken for a complete p. 127. The edition's printed pages are 39–83. The corresponding leaves of the editors' complete Chapter XVIII PDF are 41–85. Thus attached leaf n is printed page n+38 and complete-chapter PDF leaf n+40. These three systems are kept separate in the registers.

The attached PDF is the authority for transcription decisions. We also consulted the editors' complete Chapter XVIII PDF to recover standing hypotheses or examine explicit forward references, particularly 4.11.7 and 4.15.10–11. Those later passages are identified as later evidence, not as proofs contained in this excerpt. We read all footnotes and annotations in the assigned range. The terminal proof continues outside the package; a commentary block supplies the relevant completed argument and labels the boundary explicitly.

The supplied `index_earlier.md` contains no entry for XVIII-a. Consequently comparison with an earlier commentary on the opening overlap could not be certified. We checked the opening mathematics and provided the necessary local explanations, without inventing earlier block references. The earlier index and cumulative bibliography are included among the input materials for reproducibility.

## Mathematical findings and repairs

The audit distinguishes a false assertion, a missing hypothesis, a proof that stops short of its conclusion, and a question whose exact present status was not established by the literature checked. The `proof_status` field records the source treatment according to FORMAT.md; present resolutions and qualifications appear in `repair`, `references`, and `notes`.

### The cocomplete argument, 4.5–4.6

The core closure and reconstruction arguments are valid after their hypotheses are made explicit. A filtered presentation of a presentable object produces a retract of one stage. Lemma 4.5.14 omits the retract-closure hypothesis for its unrestricted converse; a complete counterexample in sets is given. The later application to a subcategory closed under the appropriate colimits is valid, because idempotents split there by coequalizers.

The coordinate inclusions into a product of groups are not a strict epimorphic family in the proposed special case. A free-product example repairs the intended distinction between strict epimorphy and universal epimorphy. Corollary 4.5.16 invokes universal strict epimorphic descent with a weaker printed hypothesis; its strengthened version is proved. The full passage to case C of 4.5.13 is not established by the displayed cover argument. We do not supply a counterexample under all its standing hypotheses and do not label that conclusion false.

The essential-smallness construction in 4.6.1 survives independently of its numerical morphism bound. The numerical assertion in 4.6.1.1(2), inherited by 4.6.1.2, is false: a variety with arbitrarily many binary idempotent operations has a one-arrow full subcategory on its free one-generator algebra, while the binary coproduct introduces arbitrarily many arrows from that generator. This supplies the concrete defect anticipated by the author's footnotes 56–57. An infinite normalization also repairs the elementary pi1=1 edge case in 4.6.2, but its proposed general numerical proof is not thereby established.

The fully faithful completion functor in SGA 4, I, 9.18 does not by itself force its original objects to be presentable; the rigid real ring gives the stated counterexample. Evaluation of presheaves proves the needed assertion in the actual Ind application. The unrestricted wording of 4.6.3(3)c/c' omits the colimit hypotheses on the small category which its proof later restores. The discrete two-object category disproves the omitted-hypothesis version.

Footnote 59 is answered negatively at every specified infinite cardinal by a sheaf topos on a co-small topology. The proof shows that no noninitial sheaf is presentable at the proposed rank, although filtered colimits are exact and a small dense category exists. Pointed sets supply a further fully checked example of all six conditions in 4.6.7. Examples in groups and commutative rings separate the conditions on monomorphisms.

### Bounded presentations and generalized filtrations, 4.7

The unconditional pointwise-size implication in 4.7.1 is false below the size of C. A terminal presheaf on a sufficiently long ordinal has singleton values but fails presentability at the chosen smaller cardinal. Adding the cardinal bound on C repairs that implication.

The retract-removal and bounded iteration questions have a positive answer in the literature checked. Chen (2021), Corollaries 4.13 and 4.15, proves the relevant bounded closure results, the latter explicitly relating them to Makkai–Paré, Proposition 2.3.11. We give a complete elementary retract proof preserving the arrow count, and do not mark that known result as our own. At the initial level the correct category is Kar(C), not necessarily C; the two-element idempotent monoid provides the precise endpoint example.

The transfinite construction of a filtered subcategory is completed by retaining old arrows and adjoining cone legs as well as objects. Its cardinal bound is maintained. The generalized filtration discussion explicitly uses repaired versions of the two erroneous bounds in 4.7.7. Even with these repairs, the bare filtered-slice criterion in 4.7.12 does not imply realization equivalence: an explicit filtration of sets is a counterexample. Density or the canonical-colimit property is required. With usefulness defined by realization equivalence, every useful cardinal satisfies the manuscript's quantitative regularity condition. A complete bounded cofinal-poset argument is included to respect its requirement of ordered indexing sets.

The literal proposed uniform initial exponent in footnote 78 is disproved in sets. The less drastic sharpening in footnote 79 is a different question, and its exact general bounds were not settled by the sources inspected. The commentary does not present them as a recognized currently open problem. Modern results on the accessibility spectrum are distinguished from presentability ranks and internal sizes of individual objects. Following the example in Vasey, Remark 3.7 and Example 3.8, we give a complete proof that the single category of nonempty aleph1-directed posets is aleph1-accessible but fails theta-plus accessibility for every singular theta greater than aleph1 of countable cofinality. This supplies unbounded nonuseful manuscript cardinals and answers both 4.8.6(1) and the nonuseful part of 4.8.6(4), with aleph-omega as a first explicit failure.

### Recognition and diagrams, 4.8–4.9

The enlargement of a dense subcategory in 4.8.2–3 is valid; the author's initial doubt is withdrawn later in the source, and we do not perpetuate it. The description of compact objects by idempotent completion is also valid. The retraction-versus-cofinality example is worked out without confusing failure of cofinality of that functor with failure of a bounded presentation to exist.

SGA 4, I, 8.13.2(b), says **prorepresentable**, so the first assertion of 4.8.11 is false as printed. Locally constant maps from the Cantor space give an accessible finite-limit-preserving, nonrepresentable functor. The all-small-limit version repairs the intended representability argument. The bounded finite-limit assertion in 4.8.12 is proved directly using finite acyclic strictification; it does not require the false general claim that every finite diagram can be realized at stages.

Footnote 91's converse is false. The self-dual category of sets and partial injections is accessible and not essentially small. Heunen's treatment is cited, and a full direct proof establishes that its lambda-presentable objects are precisely the sets of cardinality below lambda. This does not affect the theorem on essentially small accessible categories.

The exact equality endpoint of 4.8.13 is not established here or by the checked continuation. The later manuscript, 4.15.10–11, proves a strict size inequality and calls it a weaker version. Tendas's checked continuity bounds are also strict. These results suffice for the stated small-category corollary, but are not evidence for the unchecked endpoint.

The diagram obstruction in 4.9.4 is supplied at every infinite filtering bound by a transfinite adaptation of SGA 4, I, Exercise 8.8.8. A nontrivial involution on an ind-object cannot be carried by any stage. The argument keeps the stronger filteredness condition, rather than using an ordinary countable filtered example at the wrong rank. The corrected coherence construction and the faithful cofinality criterion are proved with their hypotheses stated. The printed alternative b' in 4.9.6.3 lacks a comma-category condition and is false even for the empty category mapping to the terminal category. Products of filtered categories behave as asserted under the ambient choice convention; a separate fence example explains why arbitrary products of connected categories need not be connected.

## Supplied developments and attribution

The blocks marked `development` contain the explicit local counterexamples or extensions supplied in this audit: the omitted retract-closure counterexample, the numerical Hom-bound counterexample, the fixed-rank sheaf-topos example, the filtered-slice counterexample, the literal exponent obstruction, the transfinite involution construction, and the product-of-fences calculation. Each marked result has a full proof and a statement of the literature comparison made. These markings identify supplied arguments, not claims of priority. Standard retract principles and the known bounded closure theorem are cited and left unmarked.

## Bibliographic verification

Every bibliography entry records the exact verification scope. The primary texts directly inspected include the supplied edition and relevant later portions of the official chapter; SGA 4, Tome 1, digital edition 71766d9 of 30 July 2024; the specified passages in Lurie's 949-page online Higher Topos Theory; Chen's 15-page author-hosted preprint and its journal metadata; the revised Heunen preprint; Tendas's published article; the stated arXiv versions of Vasey and of Lieberman–Rosický–Vasey; and the primary scan containing Tôhoku Theorem 1.10.1.

Gabriel–Ulmer and Makkai–Paré were checked bibliographically through publisher records. The original proof of Makkai–Paré 2.3.11 was not retrieved; its content and attribution were checked through Chen's explicit statement and proof. For Adámek–Rosický, the publisher excerpt identifies Theorems 1.20 and 1.46, but their full book proofs were not available in that excerpt. The notes say so. A later theorem is not represented as having been read merely because its metadata or an abstract was available. Existing cumulative keys have been reused wherever present.

## Transcription and build record

The final counts, exact transcription changes, compilation results, and visual checks are appended after integration. Edition slips are kept in the working source. The two prose languages are set separately: French for the edition, English for commentary and overview. Changes to page geometry, display fitting and margin labels are layout changes only and are documented separately from transcription corrections.

The six required files follow the schemas supplied in FORMAT.md. `build_reader.py` is retained from the kit and is run as requested. The package also contains the built reader TeX and PDF, the working source, the companion style, the original inputs needed to reproduce the assembly, and the local assembly/verification code. No claimed mathematical result is inferred from a successful TeX build.
