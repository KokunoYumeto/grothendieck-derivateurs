# Integration of CATHOT and TOTASPH into the companion (11 November 2026)

Applied by `apply_integration.py` to `checks\DER_<id>\`. Originals: `before\`.

- II-a: new block "Total asphericity is not filteredness" after "A necessary directedness condition"
- II-a: paragraph updated: "The difficult direction is whether this test forces the equalization o..."
- II-a: paragraph updated: "Our literature check did not locate a resolution of the full implicati..."
- II-a: row II-C-003 updated (gap_or_error, repair, references, notes); proof_status now "conjectured"
- II-a: row II-C-010 updated (repair, notes); proof_status now "stated"
- II-a: bibliography entry AdamekKoubekReiterman1981 added
- XIIb-a: new block "A total presheaf whose category of elements is not total" after "Total asphericity tested on final images"
- XIIb-a: new block "The path category over a contractible base need not be total" after "The information lost by taking components"
- XIIb-a: new block "The open questions of this page" after "The later theory of homotopy cofibrations"
- XIIb-a: new block "Composition of aspherical functors and of dwy\'erienne immersions" after "Dwyer attachments and higher categorical pushouts"
- XIIb-a: new block "The endpoint product is not a cofibration" after "Dwyer attachments and higher categorical pushouts"
- XIIb-a: paragraph updated: "This counterexample defeats the proposed pushout method; it does not r..."
- XIIb-a: paragraph updated: "The question about $\underline{\mathrm{Ch}}(Y;y_0,-)$ when $BY$ is con..."
- XIIb-a: paragraph updated: "It supplies no composition theorem for arbitrary strictly or totally $..."
- XIIb-a: row XIIb-a-B035 updated (repair, references, notes); proof_status now "open"
- XIIb-a: row XIIba-C005 updated (gap_or_error, repair, references, notes); proof_status now "open"
- XIIb-a: row XIIba-C035 updated (repair, references, notes); proof_status now "open"
- XIIb-a: row XIIba-C037 updated (proof_status, gap_or_error, repair, references, notes); proof_status now "false"
- XIIb-a: row XIIba-C038 updated (proof_status, gap_or_error, repair, references, notes); proof_status now "false"
- XIIb-a: row XIIba-C045 updated (repair, references, notes); proof_status now "open"
- XIIb-a: row XIIba-C047 updated (repair, references, notes); proof_status now "open"
- XIIb-a: row XIIba-C048 updated (repair, references, notes); proof_status now "open"
- XIIb-a: row XIIbb-A001 updated (repair, references, notes); proof_status now "open"
- XIIb-a: bibliography entry Cisinski2004Minimal added
- XIIb-a: bibliography entry Cisinski2006 added
- III-V: replaced block "The reflection does not exist" (was "The unproved reflection must remain a hypothesis")
- III-V: new block "The same ind-morphism, two different maps of the unions" after "A complete instance of the length obstruction"
- III-V: paragraph updated: "The claim on manuscript p.~47 that a corresponding union map must be a..."
- III-V: paragraph updated: "We have not shown that the target stages or their union are Thomason f..."
- III-V: row V-I026 updated (proof_status, gap_or_error, repair, notes); proof_status now "false"
- III-V: row V-I054 updated (repair+, notes); proof_status now "stated"
- III-V: row V-I059 updated (proof_status, gap_or_error, repair, notes); proof_status now "false"
- III-V: row V-I060 updated (proof_status, gap_or_error, repair, notes); proof_status now "false"
- III-V: row V-I063 updated (gap_or_error, repair, notes); proof_status now "stated"
- VII-c: row VIIc-C004 updated (repair+, notes); proof_status now "open"
- VII-c: row VIIc-C005 updated (repair+, notes); proof_status now "sketched"
- VIII-X: row IX-037 updated (repair, notes); proof_status now "open"

## State after the run

- The chunk readers of II-a, XIIb-a and III-V were rebuilt with `kit\build_reader.py` and compiled (LuaLaTeX, BibTeX, LuaLaTeX twice): no errors, no undefined citations (52, 66 and 74 pages). VII-c and VIII-X had only claim rows changed; their `_reader.tex` was regenerated, not recompiled.
- Not done: the global reader (`kit\build_global_reader.py`, `reader\`) was not rebuilt and nothing was published. `returns\` was not touched.
- Stated in the new commentary without proof, each marked there as not reproduced: the converse of Proposition 8 and the cofibration property of object-injective functors for localizers containing `W_1` (TOTASPH D.19, F.29, F.30); the restriction of a totally `W_R`-aspherical presheaf to a cosieve (F.11); the classification of representable `[B-, Y]` by 1-types (CATHOT B.5-B.11, C.2). Not set in the commentary at all: CATHOT E.18, E.20-E.25 (rows V-I059, V-I063, VIIc-C004, VIIc-C005, IX-037 point to the Pro answer in their notes).
- Arguments in the commentary that are the reviewer's own and were not checked by a second reader: the join argument at XII ms. 111 (row XIIba-C038); part (c) of the proposition at V ms. 49 (row V-I060); the direct proof of exactness over the injective ordinals at II ms. 36 (it replaces the answer's passage through the affine category).
- The overviews (`_overview.tex`) of the five chunks were not revised; II-a, III-V and XIIb-a may still describe as unsettled what the blocks and rows above settle.

# Integration of POLES (11 November 2026)

Applied by `apply_POLES.py` (with `integ_lib.py`). State of each file before this package: `before\POLES\`.

- XVI: block "The least localizer satisfying reverse cube excision" extended (443 words added at its end)
- XVI: new block "Reverse excision excludes the fibration axioms" after "The least localizer satisfying reverse cube excision"
- XVI: block "The weak minimality theorem settles the finer-localizer hopes" extended (79 words added at its end)
- XVI: block "Generalized Thomason models and the role of properness" extended (122 words added at its end)
- XVI: new block "No homology localizer has enough intrinsic fibrations" after "Generalized Thomason models and the role of properness"
- XVI: overview extended (180 words)
- XVI: row XVI-A092 updated (notes+); proof_status now "open"
- XVI: row XVI-A112 updated (notes+); proof_status now "open"
- XVI: row XVI-B099 updated (repair, references, notes+); proof_status now "open"
- XVI: row XVI-C038 updated (repair+, notes); proof_status now "stated"
- XVI: row XVI-C039 updated (notes+); proof_status now "false"
- XVI: row XVI-C040 updated (repair+, notes); proof_status now "conjectured"
- XVI: row XVI-C073 updated (repair, references, notes); proof_status now "open"
- XVI: row XVI-C105 updated (repair, references, notes); proof_status now "open"
- XIIb-a: block "Ordinary covers yield homotopy pushouts, with one direction of excision" extended (180 words added at its end)
- XIIb-a: block "A finite counterexample to the asserted reverse excision" extended (95 words added at its end)
- XIIb-a: block "What survives of the cube principle" extended (98 words added at its end)
- XIIb-a: row XIIba-A-053 updated (repair, references, notes); proof_status now "open"
- XIIb-a: row XIIb-a-B002 updated (notes+); proof_status now "proved"
- XIIb-a: row XIIb-a-B003 updated (notes+); proof_status now "proved"
- XIIb-a: row XIIb-a-B012 updated (notes+); proof_status now "sketched"
- XIIb-a: row XIIb-a-B015 updated (notes+); proof_status now "stated"
- XIIb-b: block "Why converse excision is an additional axiom" extended (229 words added at its end)
- XIIb-b: row XIIbb-A045 updated (repair+, notes+); proof_status now "proved"
- XIIb-b: row XIIb-b-B036 updated (notes+); proof_status now "proved"
- XIIb-b: row XIIbb-C019 updated (notes+); proof_status now "sketched"
- XIIc-a: block "Degree two and the localizer correction" extended (195 words added at its end)
- XIIc-a: row A029 updated (repair+, notes+); proof_status now "false"
- XIIc-b: row XIIcb-C028 updated (notes+); proof_status now "open"

## POLES: the review's list, item by item

- 1 (row XVI-C105; new block at ms.124): done. Block "No homology localizer has enough intrinsic fibrations"; the lemma and Proposition 2 it uses are in the new block at ms.27.
- 2 (block at ms.124 on properness): done by a paragraph at its end. Only the necessity of aspherical generation is proved in the commentary; the equivalence with right properness (POLES E.2) is stated as not checked.
- 3 (row XVI-C073): done. Accessibility of the homology localizers is stated as standard, not proved.
- 4 (row XVI-B099): done; the description of Fib_{W_n} (C.9) is entered as stated and not verified.
- 5 (block at ms.27): done by two results at its end: the single-square form with the cofibre test (proved for weak localizers; the equivalence with the cube forms under (3 bis) is stated, not reproduced), and W_0 as a non-reversible localizer above the integral homology localizer.
- 6 (new block at ms.27): done, "Reverse excision excludes the fibration axioms" (POLES D.3, C.4, H.8, D.2). The inclusion of a non-total reversible localizer in W_0 (Loc 5) is stated and not reproduced.
- 7 (block at ms.87; rows C038, C039, C040): done.
- 8 (optional block on localizing subcategories of spectra): NOT done. The review makes it conditional on a check of F.9, which has not been made.
- 9 (overview of XVI): done, one paragraph.
- 10 (rows XVI-A092, A112): done; A.16 is cited as open in POLES and refuted for the literal axioms by BISITE A.32, literature check not done.
- 11 (row XIIba-A-053; block at ms.76): done; the argument is set in outline in an exposition block, with the pointer to ms.272.
- 12 (blocks at ms.78 and ms.79; rows XIIb-a-B002, B003, B012, B015): done; the Dwyer-map version is stated as not reproduced; no status change.
- 13 (row XIIbb-A045; block at ms.126): done, with a complete proof in the cosieve form of that block.
- 14 (rows XIIb-b-B036, XIIbb-C019): done in the notes only; G.8 is unverified and was not compared with the block at ms.157.
- 15 (row A029 of XIIc-a; block at ms.187): done. POLES E.7 is unverified in the review; the proof in the commentary (cell structure and cup products) was written at the integration: a second reader should check it.
- 16 (row XIIcb-C028): done in the notes only (G.26 unverified). Rows C011, C020, C038: no change, as the review says.

# Integration of GALOIS (11 November 2026)

Applied by `apply_GALOIS.py` (with `integ_lib.py`). State of each file before this package: `before\GALOIS\`.

- I-b: bibliography entry Cisinski2006 added
- I-b: new block "The localizer of locally constant coefficients" after "Sets already detect the missing monodromy"
- I-b: block "Two fibrations whose composite is not a fibration" extended (133 words added at its end)
- I-b: block "The 2-complete variant also fails to compose" extended (189 words added at its end)
- I-b: overview extended (133 words)
- I-b: row I-b-A069 updated (notes+); proof_status now "conjectured"
- I-b: row I-b-B079-03 updated (repair, notes+); proof_status now "false"
- I-b: row I-b-B079-04 updated (repair+, notes+); proof_status now "false"
- I-b: row I-b-B081-04 updated (repair+, notes+); proof_status now "false"
- I-b: row I-b-B084-01 updated (notes+); proof_status now "conjectured"
- I-b: row I-b-B084-06 updated (repair+, notes+); proof_status now "false"
- I-b: row I-b-B084-07 updated (notes+); proof_status now "false"
- I-b: row I-b-B087-05 updated (notes+); proof_status now "false"
- I-b: row I-b-B093-04 updated (notes+); proof_status now "false"
- I-b: row I-b-B093-05 updated (notes+); proof_status now "false"
- I-b: row I-b-B095-01 updated (notes+); proof_status now "false"
- I-b: row I-b-B096-04 updated (notes+); proof_status now "conjectured"
- I-b: row I-b-B097-03 updated (repair, notes+); proof_status now "assumed"
- I-b: row I-b-B098-03 updated (repair, notes+); proof_status now "assumed"
- I-b: row I-b-B100-03 updated (repair+, notes+); proof_status now "assumed"
- I-b: row Ib-C003 updated (notes+); proof_status now "false"
- I-b: row Ib-C018 updated (notes+); proof_status now "sketched"
- I-b: row Ib-C021 updated (notes+); proof_status now "conjectured"
- I-b: row Ib-C026 updated (notes+); proof_status now "conjectured"
- I-b: row Ib-C034 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C036 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C037 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C038 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C039 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C047 updated (notes+); proof_status now "sketched"
- I-b: row Ib-C048 updated (notes+); proof_status now "conjectured"
- I-b: row Ib-C069 updated (notes+); proof_status now "conjectured"
- I-b: row Ib-C082 updated (notes+); proof_status now "false"
- I-b: row Ib-C087 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C088 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C089 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C090 updated (repair, notes); proof_status now "assumed"
- I-b: row Ib-C092 updated (notes+); proof_status now "conjectured"
- I-b: row Ib-C096 updated (notes+); proof_status now "conjectured"
- I-a: block "Equivalence measured by constant coefficients" extended (87 words added at its end)
- I-a: row I-a-L063 updated (notes+); proof_status now "sketched"
- I-a: row I-b-A020 updated (notes+); proof_status now "sketched"
- VIII-X: new block "Five coefficient theories and their classes of equivalences" after "A nonzero coefficient theory that forgets components"
- VIII-X: row X021 updated (repair+, notes+); proof_status now "sketched"
- VIII-X: row X022 updated (notes+); proof_status now "conjectured"
- VIII-X: row X024 updated (repair+, notes+); proof_status now "open"
- VIII-X: row X038 updated (repair+, notes+); proof_status now "conjectured"
- VIII-X: row X042 updated (notes+); proof_status now "open"
- VI-a: block "The locally constant comparison is now a theorem" extended (118 words added at its end)
- XIIc-a: block "Degree two and the localizer correction" extended (96 words added at its end)
- XIIc-a: row A050 updated (notes+); proof_status now "false"
- XIIc-a: row A062 updated (notes+); proof_status now "open"
- XI-XIIa: block "The universal meaning of a Hot-fibration" extended (83 words added at its end)
- XVI: block "A reverse-excision counterexample in every finite degree" extended (86 words added at its end)
- XVI: block "No homology localizer has enough intrinsic fibrations" extended (209 words added at its end)
- XVI: row XVI-C019 updated (repair+, notes+); proof_status now "conjectured"
- XIIapp: row XIIapp-G23 updated (notes+); proof_status now "conjectured"
- III-V: new block "A small ind-object that is homotopy invariant sees only 1-types" after "Fibrancy passes to the union"
- III-V: row V-I052 updated (notes+); proof_status now "proved"
- III-V: row V-I053 updated (notes+); proof_status now "stated"
- III-V: row V-I057 updated (notes+); proof_status now "conjectured"

## GALOIS: the review's list, item by item

- 1 (new block at I ms.99-100): done, "The localizer of locally constant coefficients", with the proof of B.3 in five steps. The compatibility of the mates with units and counits is stated as standard, not written out (as in the review).
- 2 (rows I-b-B097-03, B098-03, B100-03, Ib-C034, C036-C039): done; no status change.
- 3 (rows Ib-C087-C090): done.
- 4 (rows I-b-B079-03, B079-04): done; the alternative "completely D-aspherical test bases" is struck from the repair. D.2 itself is unverified and is cited as such.
- 5 (row I-b-B081-04; block at ms.118): done.
- 6 (block at ms.122): the companion already had the same tetrahedron example with proof. Added three complements (fibrewise detection, the reading of the edition, a shorter computation of the fundamental group). Nothing replaced.
- 7 (row I-b-B084-01; block at ms.84): the companion already had the result with proof ("Universal equivalences give fully faithful restriction"). Row notes only; proof_status stays conjectured (source status), the answer yes is in repair and notes.
- 8 (row I-b-B084-06): done; set in the last paragraph added to the block at ms.118; depends on accessibility (unverified).
- 9 (row I-b-B084-07): done, notes only.
- 10 (row I-b-B096-04): notes only; stays conjectured (D.8 unverified).
- 11 (row I-b-A069): notes only (D.11 unverified).
- 12 (rows Ib-C021, C026, C048, C069, C092, C096): notes only.
- 13 (rows Ib-C018, C047, C082): notes only.
- 14 (rows I-b-B087-05, B093-04, B093-05, B095-01, Ib-C003): notes only, no change of content.
- 15 (overview of I-b): done, one paragraph.
- 16 (I-a block at ms.61; rows I-a-L063, I-b-A020): done.
- 17 (row X021): done. 18 (row X024): done. 19 (rows X038, X042): done. 21 (row X022): done.
- 20 (new block at X ms.5): done, "Five coefficient theories and their classes of equivalences". The table is stated without derivations; the arithmetic criterion (C.9) is proved in the block by an argument written at the integration from the review's indication: a second reader should check it.
- 22 (VI-a): one paragraph added to the status block at ms.40 (not to the blocks at ms.32-38 and 65-69). Rows VIa-141, 146, 148, 160: no change, as the review says.
- 23 (XIIc-a block at ms.187; rows A050, A062): done, with the indices of the table C.15 (the review's sentence has an index slip, recorded in the row notes).
- 24 (XI-XIIa, opening block): done; D.8 and D.1 are entered as stated, not verified.
- 25 (row XVI-C019): done.
- 26 (XVI ms.124): done as a further example at the end of the block "No homology localizer has enough intrinsic fibrations": the case k = Q is proved (the review's own test); the general statement for a ring k is entered as stated (properness half of B.7 unverified).
- 27 (XVI ms.17-prime): done, stated without proof (B.6).
- 28 (XVI block at ms.78): NOT changed: the [sic] on the order relation is the edition's reading and is already marked in the transcription; nothing mathematical to add.
- 29 (row XIIapp-G23): done, notes only.
- 30 (III-V rows V-I052, V-I053, V-I057; new block at V ms.46): done, "A small ind-object that is homotopy invariant sees only 1-types". The Kan-Thurston statement with a cardinal bound (B.10, B.11) is stated and NOT proved in the commentary; the lemma (B.9) and the proposition (B.12) are proved. The last step (isomorphism of ind-objects) is written out at the integration.

# Integration of STRATA (11 November 2026)

Applied by `apply_STRATA.py` (with `integ_lib.py`). State of each file before this package: `before\STRATA\`.

- VI-c: new block "Bifibrations over posets and over bases with cancellation" after "What the bifibration question asks"
- VI-c: block "Why alternating completion works at the limit" extended (129 words added at its end)
- VI-c: overview extended (159 words)
- VI-c: row VIc-C019 updated (notes+); proof_status now "open"
- VI-c: row VIc-C021 updated (notes+); proof_status now "stated"
- VI-c: row VIc-C022 updated (repair, references, notes); proof_status now "open"
- VI-c: row VIc-C023 updated (notes+); proof_status now "stated"
- VI-c: row VIc-C044 updated (repair+, notes+); proof_status now "sketched"
- VI-c: row VIc-C045 updated (repair+, notes+); proof_status now "sketched"
- I-a: bibliography entry BGH2020 added
- I-a: bibliography entry Aoki2023 added
- I-a: block "Support, zero extension, and the exceptional inverse image" extended (111 words added at its end)
- I-a: new block "Ordered sets as stratified spaces: what is proved" after "From derived coefficients to diagram categories"
- I-a: block "Properness as a condition on all lifts" extended (72 words added at its end)
- I-a: row I-a-E024 updated (notes+); proof_status now "false"
- I-a: row I-a-L014 updated (notes+); proof_status now "stated"
- VI-a: block "Path completion and the modern category of local systems" extended (106 words added at its end)
- VI-b: block "The extra structure hidden in a categorical base" extended (104 words added at its end)
- XIIb-a: block "The presheaf case is already present in SGA 4" extended (139 words added at its end)
- XIIapp: bibliography entry CDDouteauWaas2022 added
- XIIapp: block "The open--closed gluing formula" extended (229 words added at its end)
- XIIapp: row XIIapp-G11 updated (notes+); proof_status now "open"
- XIIc-a: bibliography entry Cisinski2006 added
- XIIc-a: block "Degree two and the localizer correction" extended (95 words added at its end)
- XVI: block "Why enough intrinsic fibrations gives B" extended (43 words added at its end)
- XI-XIIa: block "From strict fibres to homotopy fibres" extended (72 words added at its end)

## STRATA: the review's list, item by item

- 1 (row VIc-C022): done; status stays open.
- 2 (new block at VI ms.186): done, "Bifibrations over posets and over bases with cancellation": E.1, E.5, E.6 as lemmas, E.10 with its proof, E.8 and E.9 stated without proof, E.11 with the reviewer's remark on idempotents. Placed after "What the bifibration question asks" (the review names a block "Perfect maps and strict bifibrations", which does not exist under that title).
- 3 (row VIc-C023): done. 4 (rows VIc-C019, C021; block): done; the separating poset is set as x<a,b<c with x over 0 and a,b,c over 1 (the assignment was reconstructed at the integration: fibration, not opfibration, lifting posets with greatest elements).
- 5 (rows VIc-C044, C045; E.4 in the block at ms.194): done.
- 6 (overview of VI-c): done, one paragraph.
- 7 (I-a block at ms.52-54; row I-a-L014): done. Rows I-a-L018 to L023: no change, as the review says.
- 8 (I-a block at ms.2): done; Groth 2013 was NOT opened at the integration; the paragraph says that the statement numbers were not checked.
- 9 (new block at I ms.4): done as a STATUS block without proofs, "Ordered sets as stratified spaces: what is proved" (A.1, A.2, A.4, A.11, D.5, D.7, D.8, B.3, B.4, B.7). The coarsening step (A.4, B.3) is marked as not opened; the extension of D.8 to all proper maps (BISITE D.11) is marked as unverified.
- 10 (row I-a-E024): done. 11 (row Ib-C003): no change needed.
- 12 (VI-a): one paragraph added to the block at ms.69 (B.9, B.10, B.12, A.10). Rows VIa-267, VIb-A006: no change.
- 13 (VI-b, block at ms.83): done (G.1, B.7).
- 14 (row XIIba-A-003): no change needed. 15 and 16 (XIIb-a block at ms.62): done in one paragraph (C.6, C.7, C.8 and the sentence on discrete flatness).
- 17 and 18 (XIIapp block at ms.18; row XIIapp-G11): done (C.2, C.5, C.3). C.4 is already the example of the next block ("Why replacing arrows by all paths changes the answer"); nothing added for it.
- 19 (XII ms.88-89, G.2): no change needed (second proof of a statement already integrated).
- 20 (XIIc-a block at ms.187): done (G.4, G.3 with the translation-groupoid example).
- 21 (XVI): the sentence from E.12 is added to the block at ms.43. The pointer to G.5 at ms.83-85 was NOT added (a third account of a dichotomy the chunk already proves twice).
- 22 (XI-XIIa, block at ms.131): done.

# Integration of PATHS (11 November 2026)

Applied by `apply_PATHS.py` (with `integ_lib.py`). State of each file before this package: `before\PATHS\`.

- VII-b: block "The universal property includes natural transformations" extended (215 words added at its end)
- VII-b: block "The cofinality condition that controls total categories" extended (105 words added at its end)
- VII-b: block "Independence of the sequential homotopy type" extended (155 words added at its end)
- VII-b: row VIIb-C026 updated (repair+, notes+); proof_status now "open"
- VII-c: new block "The padding functors are weak equivalences and are not invertible modulo natural transformations" after "A comparison that fails under the general hypotheses"
- VII-c: block "A properness claim which the empty path disproves" extended (127 words added at its end)
- VII-c: row VIIc-A046 updated (repair, notes); proof_status now "open"
- VII-c: row VIIc-C005 updated (notes+); proof_status now "sketched"
- VII-c: row VIIc-C042 updated (repair+, notes+); proof_status now "false"
- III-V: block "A small ind-object that is homotopy invariant sees only 1-types" extended (74 words added at its end)
- III-V: row V-I066 updated (repair+, notes+); proof_status now "conjectured"
- VIII-X: row IX-037 updated (repair, notes); proof_status now "open"
- VIII-X: row IX-040 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-041 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-044 updated (notes+); proof_status now "open"
- VIII-X: row IX-049 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-052 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-061 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-065 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-070 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-072 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-080 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-081 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-084 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-087 updated (notes+); proof_status now "conjectured"
- VIII-X: row IX-088 updated (notes+); proof_status now "conjectured"
- XIII-a: block "The factorization hypothesis seen on three objects" extended (155 words added at its end)
- XIII-a: row XIIIa-A046 updated (notes+); proof_status now "proved"
- XIIc-a: block "Smoothness and properness depend on a coefficient theory" extended (206 words added at its end)
- XIIc-a: block "An interval with room at both ends" extended (85 words added at its end)
- XIIc-b: block "An interval with room at both ends" extended (85 words added at its end)
- XIIc-a: row C033 updated (repair, references, notes); proof_status now "conjectured"
- XVI: block "No homology localizer has enough intrinsic fibrations" extended (56 words added at its end)
- XVI: row XVI-C105 updated (notes+); proof_status now "open"
- II-a: block "Total asphericity is not filteredness" extended (168 words added at its end)
- VI-c: row VIc-C022 updated (notes+); proof_status now "open"

## PATHS: the review's list, item by item

- 1 (rows VIIc-A046, V-I066; new block at VII ms.121): done, "The padding functors are weak equivalences and are not invertible modulo natural transformations". C.P5 is proved in the block; C.P3 and C.P4 are stated there as followed in outline.
- 2 (row VIIb-C026; VII ms.99-110): done by paragraphs at the end of the blocks at ms.112 (A.2, A.3, A.4) and ms.117 (the categories P(tau, sigma), C.P1-C.P3, stated as followed in outline). No separate new block.
- 3 (rows VIIc-C042, VIIc-C005): done, with a paragraph at the end of the block at ms.157 (E.3 second half, E.4, E.5).
- 4 (block at VII ms.74): done (A.P1, B.3, B.4, B.6, B.8 stated as open).
- 5 (row IX-037): done. proof_status stays "open" (the source's status, as the convention has it); the answer is in repair. The review asks "status to proved": not followed, because C.P4 was followed in outline only and the column records the source.
- 6 (rows IX-080, IX-081, IX-088): done, notes only. 7 (rows IX-040, 041, 072, 044, 049, 052, 061, 065, 070, 084, 087): done, notes only; C.5 as an unverified citation.
- 8 (block at V ms.46): done, one paragraph at the end of the GALOIS block (D.K5).
- 9 (XIII block at ms.10-11; row XIIIa-A046): done, statement without proof (D.8), with D.9.
- 10 (row C033 of XIIc-a; block at ms.225): done; the W_0 and W_n cases are set with their arguments, rational homology and W_E stated as not reproduced.
- 11 (row XVI-C105; block): done; added to the block at ms.124 (the review names the block at ms.87).
- 12 (XII ms.228-234): done, one paragraph in the block "An interval with room at both ends" of XIIc-a and XIIc-b (E.7, n = 1).
- 13 (II-a; XIIb-a): done in II-a (A.2, A.5, A.7, A.8 open) at the end of "Total asphericity is not filteredness". XIIb-a NOT changed: its TOTASPH blocks do not treat colimits in Cat.
- 14 (row VIc-C022): done, notes only.
- Not integrated because unverified in the review and bearing on no row: B.9, D.15, D.21. Not set in the commentary: Part D items D.10-D.17, D.19, D.20 (no item of the review's list asks for them).

# Integration of BISITE (11 November 2026)

Applied by `apply_BISITE.py` (with `integ_lib.py`). State of each file before this package: `before\BISITE\`.

- XIIc-a: new block "Axioms (a) and (b) do not imply (c): a lattice with six elements" after "Intermediate categories and the extra information in a replacement"
- XIIc-a: block "The saturation question has an affirmative answer in Cat" extended (95 words added at its end)
- XIIc-a: new block "Complementarity holds for ordinary weak equivalences only" after "Smoothness and properness depend on a coefficient theory"
- XIIc-a: row B039 updated (notes+); proof_status now "false"
- XIIc-a: row B062 updated (repair, notes); proof_status now "open"
- XIIc-a: row C020 updated (notes+); proof_status now "sketched"
- XIIc-a: row C021 updated (notes+); proof_status now "stated"
- XIIc-a: row C022 updated (repair, notes+); proof_status now "stated"
- XIIc-a: row C023 updated (repair+, notes+); proof_status now "open"
- XIIc-a: row C024 updated (notes+); proof_status now "proved"
- XIIc-a: row C025 updated (notes+); proof_status now "stated"
- XIIc-a: row C026 updated (notes+); proof_status now "stated"
- XIIc-a: row C027 updated (notes+); proof_status now "sketched"
- XIIc-a: row C028 updated (notes+); proof_status now "stated"
- XIIc-a: row C029 updated (notes+); proof_status now "stated"
- XIIc-a: row C030 updated (repair+, notes+); proof_status now "open"
- XIIc-a: row C032 updated (repair+, notes+); proof_status now "conjectured"
- XIIc-a: row C033 updated (repair, references, notes); proof_status now "conjectured"
- XIIc-a: row C034 updated (notes+); proof_status now "stated"
- XIIc-a: row C035 updated (notes+); proof_status now "proved"
- XIIc-a: row C036 updated (notes+); proof_status now "assumed"
- XIIc-a: row C037 updated (notes+); proof_status now "assumed"
- XIIc-a: row C039 updated (repair+, notes+); proof_status now "open"
- XIIc-a: row C040 updated (repair+, notes+); proof_status now "open"
- XIIc-b: block "The factorization axiom and Brown's hypothesis" extended (116 words added at its end)
- XIIc-b: row XIIcb-B004 updated (notes+); proof_status now "conjectured"
- XIIc-b: row XIIcb-B006 updated (notes+); proof_status now "conjectured"
- XIIc-b: row XIIcb-C037 updated (repair+); proof_status now "false"
- XIIc-b: row XIIcb-C038 updated (repair+); proof_status now "false"
- II-b: row IIb-B013 updated (notes+); proof_status now "false"
- II-b: row IIb-B015 updated (notes+); proof_status now "false"
- II-b: row IIb-B050 updated (notes+); proof_status now "false"
- II-b: row IIb-B084 updated (notes+); proof_status now "sketched"
- II-b: row IIb-B085 updated (notes+); proof_status now "sketched"
- II-b: row IIb-B086 updated (notes+); proof_status now "stated"
- II-b: row IIb-B087 updated (notes+); proof_status now "stated"
- II-b: row IIb-B088 updated (repair+, notes+); proof_status now "false"
- II-b: row IIb-B092 updated (repair+, notes+); proof_status now "stated"
- VI-b: row VIb-A071 updated (repair+, notes+); proof_status now "open"
- VI-b: row VIb-R001 updated (notes+); proof_status now "false"
- VI-b: row VIb-A073 updated (notes+); proof_status now "conjectured"
- VI-b: row VIb-A074 updated (notes+); proof_status now "stated"
- VI-b: row VIb-A078 updated (repair+, notes+); proof_status now "open"
- XIII-b: new block "A closed exact structure is a closed model structure" after "Why uniform left structures produce right images"
- XIII-b: block "The proposed noetherian enlargement is actually finite" extended (28 words added at its end)
- XIII-b: row XIIIb-Q047 updated (notes+); proof_status now "proved"
- XIII-b: row XIIIb-Q048 updated (notes+); proof_status now "proved"
- XIII-b: row XIIIb-Q049 updated (notes+); proof_status now "proved"
- XIII-b: row XIIIb-Q073 updated (repair+); proof_status now "open"
- XIII-b: row XIIIb-Q074 updated (notes+); proof_status now "open"
- XIII-b: row XIIIb-Q076 updated (notes+); proof_status now "open"
- XIII-b: row XIIIb-Q077 updated (notes+); proof_status now "stated"
- XIII-b: row XIIIb-Q078 updated (notes+); proof_status now "open"
- XVI: new block "The absolute axiom does not imply the relative one" after "Axioms for equivalences before a choice of model"
- XVI: overview extended (70 words)
- XVI: row XVI-A018 updated (notes+); proof_status now "assumed"
- XVI: row XVI-A019 updated (notes+); proof_status now "stated"
- XVI: row XVI-C105 updated (notes+); proof_status now "open"
- I-b: block "Universal equivalence and the 1-complete test" extended (134 words added at its end)
- I-b: row Ib-C003 updated (notes+); proof_status now "false"
- VI-c: new block "Base change for the two Kan extensions: the exact conditions" after "The final adjunction and the surviving base-change fragment"
- VI-c: row VIc-C022 updated (notes+); proof_status now "open"
- VII-c: row VIIc-C005 updated (notes+); proof_status now "sketched"
- VII-c: row VIIc-C042 updated (notes+); proof_status now "false"

## BISITE: the review's list, item by item

- 1 (row B062; new block at XII ms.218): integrated, "Axioms (a) and (b) do not imply (c): a lattice with six elements", with the full verification.
- 2 (row C023; rows C020-C022; block at ms.222): integrated. The companion already answered C023 yes; a paragraph with the argument for every fundamental localizer is added to the block at ms.223. The status column of C020-C022 is NOT changed to proved (it records the source); the confirmation is in the notes.
- 3 (row C033; new block at ms.225): integrated, "Complementarity holds for ordinary weak equivalences only" (B.9 with proof; examples B.10, B.12; B.11 named). The rational-local-system half of B.12 is stated, not reproduced. Supersedes item 10 of the PATHS list (the PATHS paragraph in the preceding block stays).
- 4 (rows C030, C032): integrated in repair and notes; C.4 as unverified. Row C031 unchanged.
- 5 (rows C024-C029, C034-C037): integrated, notes only (B.1, B.3, B.16, proved in outline). The two corrections named are already in DER_XIIc-a_corrections.csv (lines for ms.222 and ms.223): nothing added.
- 6 (rows C039, C040): integrated; E.5 as unverified. 7 (row B039): integrated, notes only.
- 8 (rows XIIcb-B004, B006; block at ms.240): integrated. 9 (rows XIIcb-C037, C038): integrated. 10: no change needed.
- 11 (rows IIb-B092, B084-B088): integrated in rows; the companion already has the blocks ("When a transporter becomes a stabilizer", "A closed transporter which does not compose"). B092 keeps the source status "stated". Rows B089-B091, B098, B099: agree, not touched. Rows B100-B102: not addressed by the answer.
- 12 (II ms.76-77 formula (5.20): row IIb-B050; ms.65-67 and the cancelled section: rows IIb-B013, B015): integrated, notes only. No separate row was found for the lattice description of ms.65-67; A.30 is recorded in the note of IIb-B013.
- 13 (rows VIb-A071, A074, A078, R001, A073): integrated. The two 2026 manuscripts on strict n-categories and globular infinity-groupoids are not cited in the rows.
- 14 (new block at XIII ms.57): integrated, "A closed exact structure is a closed model structure" (A.27 with proof). The pointer from ms.27-29 was not added.
- 15 (rows XIIIb-Q073, Q074, Q076-Q078, Q047-Q049): integrated; for Q074, Q076-Q078 notes only, flagged as the reviewer's inference. Rows Q070, Q071: agree, not touched.
- 16 (block at XIII ms.45-50; A.23, A.24): DEFERRED: the chunk XIII-a block for these pages was not identified in the time available; no row depends on it.
- 17 (new block at XVI ms.1-3; rows; overview): integrated, "The absolute axiom does not imply the relative one" (A.32). The block and the rows say that the literature check is not done and make no novelty claim.
- 18 (row XVI-C105): integrated, notes only; E.14 as unverified. Nothing added to the blocks.
- 19 (row Ib-C003; I-b blocks): integrated; A.19, A.20 and the statement of B.14 in a paragraph at the end of the block at ms.120; B.14 stated without its examples. A.18 is GALOIS D.3, already there.
- 20 (VI-c, six operations; row VIc-C022): integrated in part: a STATUS block at ms.204 with F.2, F.3, F.8 (F.9 is already in I-a from STRATA D.1). F.4-F.6 and F.10-F.19 DEFERRED (unverified, or waiting for a second reading of F.10). The combined review's partial result on C022 is NOT entered (unchecked by a second reader), as the list asks.
- 21 (rows VIIc-C042, VIIc-C005): notes only; the smoothness proof at ms.164 was not replaced.
- 22 (topological spaces: D.2-D.4): DEFERRED: no row; D.2 is proved in outline only and the neighbouring statements are unverified or uncited.
- 23 (duality on finite bases: G.2, G.3, G.7, G.8): DEFERRED: no row and no manuscript passage; checked by hand in the review, not followed as proofs; G.9, G.12 wait for the source.
- 24 (moduli example F.15-F.17): DEFERRED: unverified.
- Not integrated, as the list says ("Not to integrate yet"): A.15, B.15, C.4-C.9, D.5-D.8, D.10, D.11, D.13, E.4, E.5, E.9, E.10, E.14, F.4-F.7, F.10, F.11, F.13-F.17, G.1, G.4-G.6, G.9, G.10, G.12-G.14. Where a row mentions one of them (C.4, E.5, E.10, E.14) it is marked unverified.
