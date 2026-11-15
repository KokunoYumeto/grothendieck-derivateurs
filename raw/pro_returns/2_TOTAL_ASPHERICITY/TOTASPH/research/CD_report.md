# Parts C and D: research record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Sources inspected

- Attached PROMPT(2).md; relevant FABLE overview and companion II-a discussion.
- John R. Isbell, *A note on exact colimits* (1968), full four-page primary article opened at Cambridge, DOI 10.4153/CMB-1968-068-7. Section 1 gives a finite-family linear condition; Section 2 proves the monoid theorem. Its argument was not blindly substituted for the total-asphericity condition.
- Isbell, *Exact colimits, I* (1974): Annals and JSTOR bibliographic pages opened; full body inaccessible. The title, volume, issue, pages, DOI verified, but no theorem number invented and no unavailable proof used.
- A. A. Husainov, *Homological dimension theory of small categories* (2002), author's uploaded full text opened. Section 2.3, Theorem 2.5 states the affine-category criterion and the following paragraph identifies Delta_face as Isbell's nonfiltered exact-colimit example. This supplied a literature lead; the relevant claims are proved independently in the paper.
- Husainov, *On the homology of small categories and asynchronous transition systems* (2004), primary article opened. Section 2 notes the counterexample to Oberst and repeats an unresolved fixed-point/exactness question. The later source audit found that the relevant fixed-point equivalence had already been refuted in 1981; that historical passage is not used as an open-problem source. See CD_followup.md.
- Open Maths, *Derived colimits over a small category* (20 October 2026), sections 4.1–4.8. Page explicitly credits Claude Opus 5.5 and dedicates content to the public domain (CC0). Treated as an untrusted AI mathematical draft. The gap-polynomial interpolation construction was read, independently proved, and checked by exact symbolic arithmetic. No authority or priority claim relies on this page.
- Isbell–Mitchell 1973 and 1976 AMS bodies: attempted direct retrieval, HTTP 403. No invented theorem number. The affine theorem is reproved.

## Queries

Searched combinations of “Isbell Mitchell exact colimits fixed points”, “Oberst conjecture”, “aff C filtered”, “Delta face exact colimits”, “categories of elements contractible colimit”, and exact article titles. Routine engine coverage was checked with the stronger engine for the principal original-paper searches. No claim of novelty is made.

## Proof decisions

1. Total W_Z implies all connected categories of elements of covariant Set-valued diagrams are acyclic, using the collage construction. This property is inherited by categories of elements.
2. Covariant coset diagrams model every connected covering. Applying acyclicity to a covering with a cyclic fundamental group proves that every such element-category component is simply connected, hence contractible. Thus total W_Z equals total W_infinity.
3. Exact Ab-colimits imply total W_infinity in the nonempty connected case. The missing connectedness invalidates the literal W_Z assertion in Lead 4, even before discussing its difficult converse.
4. Delta_inj has exact Ab-colimits and is not filtered. Its exactness is proved through explicit affine cones, so the main counterexample does not rest on an inaccessible article or on an unchecked AI source.
5. Lead 2's H_1 formula is correct without an asphericity assumption on the base. Its proof uses two short exact sequences of functors and projectivity of linearized covariant representables.
6. A monoid affine-equalizer condition yields genuine equalizers through invariant signed measures and reduction of finite cycle periods. This also proves filteredness for total categories with a weakly terminal object, including every finite-object category.

## Programs and outputs

- code/cd_affine_simplex.py and .out: exploratory exact nullspace computations for affine cones, which found target cardinalities 3 and 7 and suggested the subsequent polynomial construction. These bounded searches are evidence only, not the general proof.
- code/cd_affine_polynomials.py and .out: exact integral polynomial construction, validation of augmentation one and equality of all codimension-one faces, with actual injection dictionaries for dimensions through 3. The symbolic induction is the proof for every dimension.

## Limits

The connected converse from total W_infinity (equivalently total W_Z) to exactness of colim on Ab is not established merely by the action criterion; the proof must not identify free-on-a-set diagrams with projective diagrams. It is retained as an exact unresolved implication in this report, not asserted to be an open problem in the literature without a current verified source.

## Additional verified background

- Hatcher, *Algebraic Topology*, author's PDF opened; Theorem 1.38 (covering classification), Theorem 2A.1 (first homology as abelianization), and Theorem 4.32 (Hurewicz) verified.
- Lurie, *Higher Topos Theory*, author's PDF opened; Proposition 5.5.6.18 verified for the n-truncation adjunction.
- `cd_finite_checks.py` checks the discrete two-object category, the C2 multiplication law and displayed periodic differentials, and the three comparison strata of Delta_inj cospans on a bounded family (351 comparisons). Full mathematical proofs establish the unbounded claims.
- `cd_make_results.py` generates the C/D statement ledger; its output is attached.

## Further corrections and scope

- W0-total categories are exactly nonempty connected categories; W1-total categories are exactly those with simply connected classifying spaces. For n>=2, the paper gives an exact action-category criterion and proves filteredness in all weakly terminal and finite-object cases.
- For a finite group G and a nonzero commutative unital ring R, total W_R is equivalent to invertibility of |G| in R. Thus rational and integral totality differ already for C2.
- The zero-ring case is handled separately; every category is then total.
- Delta_inj is not sifted: the cospan category for two singleton ordinals has exactly three components (<,=,>). This directly blocks a proposed Dold–Kan shortcut to the missing converse.
- The manuscript's integral-homology totality and weak-homotopy totality coincide, but no claim is made that an arbitrary homology equivalence preserves totality.
- The verified 1981 primary-source correction and two further necessary conditions are recorded in CD_followup.md and sections/D_followup.tex. In particular, totality implies the representation fixed-point property; that property alone does not imply exact additive colimits. This does not settle the corrected connected necessity.
