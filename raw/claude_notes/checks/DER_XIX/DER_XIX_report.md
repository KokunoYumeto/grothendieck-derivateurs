# Chapter XIX: audit and commentary report

## Authorship and scope

The commentary, audit, and supplementary mathematical arguments were produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. Grothendieck's text remains attributable to him. The electronic edition was deciphered and transcribed by M. Künzer and edited by M. Künzer, J. Malgoire, and G. Maltsiniotis. No subsequent assembly or editing with Claude (Anthropic) is certified by this delivery.

The supplied PDF is the authority for readings. It contains 28 leaves: the title and editorial preliminary leaves, then printed pages 1–26, covering manuscript pages 1–50. The audit is divided for checking into manuscript pages 1–18, 19–32, and 33–50, with the arguments at their boundaries reconciled. The PDF was extracted for searching and rendered for visual comparison; the glyph decisions are based on the rendered edition, not on extracted text alone.

The six deliverables use the exact filenames and column schemas specified in FORMAT.md. The corrected transcription is supplied as an additional build input. Transcription corrections are applied there; edition slips are preserved and explained. Ordinary layout changes to the reader are documented separately from readings.

## Continuity material

The supplied `index_earlier.md` ends at DER_VII-a. It does not contain the indices or audits of the intervening packages through Chapter XVIII. We therefore make no claim to have checked non-repetition against unavailable commentary. Where an earlier listed block directly covers an issue, the commentary refers to its package and title. In particular, the infinite-product localization warning uses the listed DER_VI-b block at manuscript page 132, “The uniform bound in an infinite product is a real obstruction.” Mathematical dependencies on the later chapters are checked against the relevant original electronic chapters where needed; they are not attributed to unseen companion blocks.

## Principles of the mathematical audit

The `proof_status` field records the treatment in the source. It does not promote a source conjecture to `proved` because later literature proves a suitably stated form, or demote a correct sketch because its details are not repeated. Later theorems, counterexamples, qualifications, and complete repairs are recorded in `repair`, `references`, and `notes`, and developed in the commentary. A false inference is distinguished from an intended theorem that remains correct after repair.

Three distinctions control the reading. A mutually lifting-closed pair need not admit factorizations. Generation under filtered colimits is different from generation under pushouts, transfinite compositions, and retracts. Finally, existence of homotopy Kan extensions is different from existence of projective or injective model structures on every strict diagram category. Conflating any two of these assertions would introduce errors into the audit itself.

Grothendieck's individually accessible objects are not silently replaced by local presentability of the ambient category. The modern locally presentable form of Question 1.11 is identified explicitly as such. His Q-saturated class in Question 3.15 is not silently replaced by a class equal to its double lifting orthogonal. Universes are fixed throughout the smallness statements and the ordinal example.

## Principal findings

The opening identification of separate double-orthogonal closedness with mutual determination of an orthogonal pair is too strong before factorization. The pair consisting twice of the isomorphisms supplies a counterexample. Proposition 1.3 provides the retract argument that repairs the identification for factorizing pairs. The componentwise equality in (1.14) also needs the ability to isolate coordinates, supplied by identities in the left class and automatic in the closed-pair applications.

The uncertainty about retracts of cellular arrows on manuscript pages 4–5 has a general positive answer in a cocomplete category. The commentary gives a compatible transfinite retraction construction and credits Makkai–Rosický, Lemma 2.2. For Question 1.11, Lurie's Lemma A.2.8.3 proves the locally presentable case, but the particular suggested generators fail for nontrivial group actions. The commentary's constant-generator criterion develops this failure with a complete proof and limited novelty framing.

The projective and injective theorems survive several local source slips. These include the missing T in the displayed formula for projective cofibrations, the variance error in (1.13.2), the projective-limit arrow in the cardinal-stage condition (2.6.1d), and an unjustified equality with cofree arrows in the proof of Theorem 2.9. Each is treated locally. The recognition argument in Chapter XV, §7 uses two-out-of-three in an essential way and must not be replaced by the explicitly withdrawn, more general assertion in §6.

Cisinski's Theorem 6.11 and its dual rule out the requested failure of homotopy Kan extensions in the bicomplete modern Quillen case. The bounded-complex example is retained, with an explicit periodic resolution over F2[C2] and an adjunction obstruction using shifts. The discussion also distinguishes Brown's excision on cofibrant objects from the ambient, universally pushout-stable class of W-cofibrations used elsewhere in the manuscript.

The coreflective-localization proposal in Example 3.12 cannot destroy completeness or cocompleteness of a bicomplete ambient category. The ordinal category answers Question 3.13, with the conservative-generator convention of SGA 4 stated explicitly. A rational ordered category cut at an irrational real gives a mutually lifting-closed pair without factorization, while leaving the additional cocompleteness condition separate.

For Question 3.15, the 2026 presheaf classification by Cox, Feigert, Kamsma, Mazari-Armida, and Rosický supplies a non-generation theorem for pure monomorphisms of directed multigraphs. The commentary proves accessibility of the **full arrow subcategory**, using countable closure under witnesses, and separately verifies stability under arbitrary filtered colimits and the required saturation operations. This matches the older filtered-colimit-envelope convention. A small Q-generating subset would imply cofibrant generation by the small object argument, contradicting the classification. The literature's non-generation theorem is credited to its authors; the detailed translation is distinguished from that theorem.

Proposition 3.5 needs a qualification if its first equality is read with an arbitrary presentation Φ={}^⊥Ψ. The commentary gives a finite arrow-diagram counterexample. Taking the canonical Ψ=Φ^⊥ repairs the statement, and the source explicitly does this in (3.5.2). The register separates the false unrestricted reading from the valid canonical statement. The adjacent conjecture (3.5.3) is proved for its noetherian-poset case with the needed colimits explicit: attach relative latching maps through their one-object free diagrams and verify transfinite closure by a fixed-boundary chain. This gives a presentation by a class of cells, without asserting small generation. Ordinary Reedy precedent is cited to Riehl and Verity (2014), and the ordinal-poset argument is proved directly.

The implicit lemma in Proposition 3.7 is valid. A pushout, a Cof₃ factorization, and a lift against an acyclic cofibration prove (C∩W)^⊥∩W⊆C^⊥. Thus the retract argument does not need a second factorization or retract closure of W. The printed Cof₄ reference and the misnamed diagonal are local source slips.

Question 3.14 has two different answers. The cofibration assertion follows from modern ABC cofibration theory: Cof₄ supplies the coproduct and sequential-colimit hypotheses (Rădulescu-Banu, 2009, Lemma 1.6.2 and Theorem 10.3.2; Cisinski, 2010, Corollary 6.21 and its dual). The broader localizer request has a finite counterexample. Localizing the Boolean lattice P({1,2,3}) at {1}→{1,2} yields a seven-object skeleton lacking the join of {2},{3} and the meet of {1,3},{2,3}. Its diagonal into its square has neither adjoint. The complete proof verifies the categorical localization, strong saturation, accessibility, and filtered-colimit stability. An exhaustive finite calculation independently checks the relation and all relevant joins and meets.

Other worked examples include the classifying space of a group as a derived colimit, the finite 3→2 diagram distinguishing a right lifting class from a cofree image, a special model structure on sets that is not very special, and a finite Cat pushout that changes a sphere into a contractible groupoid. These examples are proved in full, not used as unexplained illustrations.

## Reading repairs and source preservation

All **11 original doubt markers** and all **23 original “sic” markers** are accounted for. The marker-by-marker review in parts/a_full_corrections_review.md identifies original lines, manuscript and printed pages, PDF leaves, and correction rows. Its final update incorporates the additional Proposition 3.5 correction. The audit arrangements and independent cross-checks do not imply external human peer review.

The corrected source applies **16 token or macro replacements**:

| Location | Applied repair | Number |
|---|---|---:|
| Right Q-closure macro, PDF leaf 3 | Horizontal bar in place of a negation sign | 1 macro definition |
| Left Q-closure marks, leaves 11–14 | Tilde in place of breve | 10 |
| Formula (2.1.4a), leaf 12 | Full heads with transverse factorization stroke | 2 |
| First arrow of Theorem 2.6(1), leaf 18 | Restore factorization stroke | 1 |
| Formula (3.10.1), leaf 26 | Full heads with transverse factorization stroke | 2 |

The harpoon in Proposition 3.7 is retained. Enlarged inspection confirms lower-left and upper-right half-heads, matching the effective original macro. An initially reversed reading was caught and corrected before integration. Every original edition-slip comment remains in the corrected transcription; resolved doubt comments point to the register.

The mathematical mistakes and slips belong in the commentary and correction register, not in a silently amended source. In particular, the missing T, the limit-direction sign, the cofree-image equality, and the newly qualified Proposition 3.5 formula remain as printed.

## Verification scope and limits

The exact weaker ambient generality of Question 1.11 is not settled by the sources checked. Lurie's locally presentable theorem is not presented as covering every historical special category. Likewise, the unrestricted class equality in Question 3.6 is not declared settled by the later existence theorem for Kan extensions.

The final request for a nonfactorizing mutually closed pair in a special ambient category remains separate from the rational-cut example. Neither pure-monomorphism non-generation nor the finite-localizer construction automatically answers that stronger request. These are limits of this audit, not assertions that the corresponding questions are currently open in the literature.

No priority claim is made for the constant-generator characterization, the finite cofree-image example, the Boolean localization, or the detailed translation of pure-monomorphism non-generation. Each development records the literature checked. For the finite Boolean example, targeted searches did not establish an attribution for that exact presentation. They did identify Zhang's September 2026 preprint on localization and (co)products. Only its primary metadata and abstract could be retrieved; no numbered example was checked, and no assertion is made that it lacks the same construction. The bibliography records this limitation.

Taylor (1999, Example 5.7.10) is cited for an earlier nonfactorizing prefactorization system. The author's HTML omits its diagram; the statement and surrounding explanation, rather than the individual arrows, are the verified antecedent. Rezk's example is cited with the checked arXiv numbering only. Brown's undated group-cohomology notes are cited without inventing a publication date.

The bibliography consolidates duplicate records and reuses cumulative keys. Verification notes specify the inspected passages and versions; a reference is not represented as read in full when only stated passages were checked. The original Chapter XIII, XV, and XVIII dependencies were checked at the locations specified in their entries. The audit identifies later proofs of Anderson's claimed conclusions without validating his criticized historical proof.

## Reproduction and reader layout

The supplied build_reader.py is unchanged. Reader-only layout preparation removes two redundant hard page breaks within the chapter while retaining the two preliminary leaves and all printed-page markers. The style provides readable margins, a visible commentary bar, English commentary and bibliography, breakable URLs, separate commentary credit, and manuscript-page labels without reproducing long anchor phrases. These are presentation changes, not reading changes.

With Python 3, LuaLaTeX, BibTeX, and the packages named by the source and style installed, run from the extracted archive directory:

~~~bash
python3 rebuild.py
~~~

This reapplies only the verified transcription patches, runs the unchanged supplied builder, prepares the reader layout, runs LuaLaTeX once, runs BibTeX, and then runs LuaLaTeX twice more. The six final deliverables are the authoritative integration inputs; regeneration of intermediate range files is unnecessary.

The build image lacked generated TeX format and font-map files. The helper tex_environment.py records the workspace-local fallback and leaves an ordinary working TeX installation unchanged. The optional install_tex_dependencies.py records the package-repair procedure used in the image. It is unnecessary with a complete TeX Live installation. No system-wide TeX files were modified.

The finite mathematical check has no external Python dependencies:

~~~bash
python3 parts/b_validate_boolean_localizer.py
~~~

For apparatus validation and page renders, install PyMuPDF and Pillow and run:

~~~bash
python3 verify_reader.py
~~~

That verifier checks source-page coverage, record identities, exact anchors, bibliography keys and verification notes, original marker preservation, compiled title coverage, page-boundary geometry, overview length, and final build logs. It renders every page and creates contact sheets for visual inspection. The mathematical proofs and visual review remain distinct from these automated checks.

## Verification and build record

Final verification was completed on 10 November 2026. The assembled reader has **53 pages**, including a **three-page overview** beginning on reader page 48. The references begin on page 50. All 34 commentary titles occur in the compiled PDF, and every manuscript page from 1 through 50 is represented in the claim register.

| Component | Final count |
|---|---:|
| Claim-register records | 269 |
| Correction-register records | 52 |
| Commentary blocks | 34 |
| Bibliography entries | 23 |
| Approximate commentary words | 15,739 |
| Approximate overview words | 1,575 |

The correction records comprise 10 doubt-resolution records, six transcription-repair records, and 36 retained-edition records. These are record categories, not counts of independent mathematical errors. One record can cover several repeated glyphs or markers; all 11 original doubt markers and all 23 original sic markers are accounted for.

The supplied builder completed successfully. BibTeX and the final LuaLaTeX pass completed with no warnings or errors; the final log contains no overfull boxes, underfull boxes, or missing-glyph diagnostics. Automated checks found no text outside the safe physical-page rectangle and no replacement characters in the extracted PDF text. Every rendered page was inspected in the final contact sheets, with full-page inspection of selected dense mathematical passages. No clipping, collisions, or unintentional blank pages remained.

The independent finite-localizer program passed all assertions. It checked all 256 subsets of the eight-object lattice, all 64 composable pairs for two-out-of-three, and all 64 endpoint pairs in the localization normal form. It verified strong saturation, the seven-object skeleton, and the unique missing join and meet pairs described above. These finite checks support the worked example; they do not substitute for the categorical and accessibility arguments given in the commentary.

The archive includes the six requested files, the compiled reader TEX/PDF and bibliography output, the corrected transcription, original attached inputs, the unchanged builder and companion style, reconstruction and verification scripts, final build logs, source-reading evidence, and final contact sheets. The supplied builder's SHA-256 is 43d2999d64c4fd667a6432f04d7c86155f2f31fd5b51d6b95bf386ca37a96bec, identical to the version in the original kit. Intermediate range files and cross-check notes are included for provenance; rebuilding uses the final integrated deliverables. A machine-readable SHA-256 manifest records the packaged files. Workspace caches and obsolete preliminary builds are omitted.
