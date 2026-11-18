# Sources and search log, Parts C–D

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026. No priority claim. “Opened” describes access to the body, and does not mean independent external peer review. The proof dependencies and the steps checked are stated in C.tex and D.tex.

## Attached earlier returns: bodies opened and used steps followed

- PRETOT_return/PRETOT_paper.tex: A.1 two-sided bar/Tor identification; C.1 restricted-action criterion for truncated localizers; B.4 final-image/comprehensive-factorization implication from total to strict; E.3–E.8, especially necessary tests, total endpoint classification, strict groupoid/preorder cases and the walking-retraction truncation; F.1–F.9 action calculus, RAAG/poset/abelian detectors and free-monoid bounds. The Tor variance, cosieve-double homology, and free-monoid graph input are rechecked in our proofs. The RAAG and diamond-poset detectors do not take values in free monoids, so they were not imported as free-monoid tests.
- LEADS_DERIVATIONS.md: Leads 2 and 3 read in full. The full-path kernel calculation and all spectral-sequence statements were rederived. The hand interval-monoid colimit and degree-two homology were independently proved and checked by code.
- checks_drafter/lead2_walking_retraction.py: read in full, including representable quotient, mixed-variance element category, nerve differential and tensor-kernel routines. It computes the stated bounded problem. Our program imports none of it.
- INDLOCAL/return/sections/C_paths.tex, C.7: read in full, including the forward and backward deletion/padding adjunctions, their opposite initiality directions, and the localized-representable universal property. Used for the all-arrows-marked path-space comparison. We separately construct the slice-to-fixed-endpoint zigzag in C.6.
- REVLOC/sections/H14.tex, H.4: read in full. Verified the faithful regular permutation action on a product, coset projection detecting lack of fullness, and detection of components. REVLOC/sections/H5.tex, H5.6–H5.8: read in full; checked the double-coset component formula, fiber-product isotropy, image of the π2 boundary, and the component caveat for localizers containing W1. H5.6 is an intrinsic-fibration criterion, not a strict-asphericity criterion.
- TOTAL_EXACT_2/return/notes/finite_pd_route.md, §§1–4: read in full. The proposed C_delta presentations have free values and actual free-factor maps by absolute/relative private-vertex elimination. Their abelianization gives exactly Q and T1Q=Z. This supplies the free-group alternative in D.4; compatible positive monoid bases are not asserted.
- TOTAL_EXACT_2/return/sections/freefactor_nerve.tex: read in full. Independently checked the finite parallel-pair example, both Nielsen inverses, the surviving b-block proof, group colimit, and integral H2 kernel. Its index is not total or exact, so it does not contradict Lead 3.
- TOTAL_EXACT_2/return/sections/akr_links.tex, C.8 proof: verified the corresponding absolute/relative private-vertex elimination over K* and its nonzero T1. This does not contradict the exact-index theorem.
- TOTAL_EXACT_2/return/sections/predimension_category.tex (closure calculus), predimension_binary_cycles.tex (the matrix), predimension_functorial_cone.tex, predimension_totality_reduction.tex, predimension_stabilizers.tex: read the relevant closure and matrix arguments and the latter three complete proofs. Checked how strict predimension yields a new private vertex, the finite alternating-amalgam stabilizer identity, minimal supports, functorial free-amalgam contraction of slice cosieves, saturation, and reduction of every action component to a representable. D.4 contains the requested paragraph checking R17 at the exact step used.
- TOTASPH/TOTASPH_C.tex, C.8–C.10: read the normalized affine-cone proof in full. The coordinate-hyperplane interpolation, gap-polynomial identity, augmentation-one condition, and coface-to-all-injections induction check out. This verifies the exactness of Delta_inj used for the counterexample.
- TOTEX_return/TOTEX_paper.tex, E.2: read in full. The lift i ↦ m f(i−1)+w_i respects colors and preserves the affine equalization identities. This verifies exactness of all W_m used in D.7.
- papers/IsbellMitchell1973.pdf: primary paper read in full; Theorem 1, Lemma 1, and Theorem 3 are the precise published affine/exactness inputs. Its proofs are announced/sketched; the complete supplied polynomial proof is also checked. DOI 10.1090/S0002-9904-1973-13296-3. The text extraction is notes/CD_IsbellMitchell1973.txt.

## Primary external literature opened

1. Marcel Evrard, *Fibrations de petites catégories*, Bulletin SMF 103 (1975), 241–265. [Primary PDF](https://www.numdam.org/article/BSMF_1975__103__241_0.pdf), DOI 10.24033/bsmf.1804. Opened the path-category definitions, the categorical homotopy-group comparison, the fibration discussion, and Theorems A and B (§V, printed pp. 261–265). This is nearest path-fibration literature; it does not state the strict endpoint classification proved here. Web refs include turn21view0, turn61view0.
2. Boris Shoikhet, *On Evrard’s homotopy fibrant replacement of a functor*, Theory and Applications of Categories 31 (2016), 989–1015; arXiv:1412.0317. Attached TeX opened: §2.1, Proposition 2.7, Theorem 2.8, the replacement definition and Proposition 2.10/Theorem 2.11, and §3's adjoint/base-change/shift arguments. The endpoint compositions and the two natural transformations were followed; this ordinary homotopy-fibrant replacement does not imply strict asphericity in XII Definition 2. We do not treat text inside the TeX's commented-out alternative proof as its published proof.
3. Zbigniew Fiedorowicz, *Classifying Spaces of Topological Monoids and Categories*, Amer. J. Math. 106 (1984), 301–350. [Primary PDF](https://www.uio.no/studier/emner/matnat/math/MAT9580/gamle-undervisningsressurser/varen-2018/documents/fiedorowicz-classifying-spaces-of-topological-monoids-and-categories-amer-j-math-1984.pdf), DOI 10.2307/2374307. Proposition 4.4 and its proof were read: the two-sided bar is the universal group-cover, giving the Tor test for monoid asphericity. The adjacent amalgamation discussion was inspected but not used. The claim depending on Lemma 5.2(a) cannot be imported, because Gray–Steinberg give a counterexample. Web refs turn33view1, turn34view1, turn35view0.
4. Robert Gray and Benjamin Steinberg, *Topological finiteness properties of monoids, Part 2*, arXiv:1805.03413. Attached TeX opened at the Bass–Serre freeness and flatness results (labels t:bass.serre.free, t:bass.serre.flat, t:amalg.cd) and the counterexample to Fiedorowicz Lemma 5.2(a), approximately source lines 1188–1432. The flatness hypotheses are substantive. None is silently applied to an arbitrary diagram in FreeMon.
5. Oliver Urs Lenz, *The classifying space of a monoid*, MSc thesis, Leiden/Padova, 20 December 2011. [Author PDF](https://cwi.ugent.be/~oulenz/publications/lenz-2011-classifying.pdf). Proposition 4.4.1 and Corollary 4.4.6 read, including the free-monoid cover-tree argument. Used only for this proved free-monoid fact; the thesis's speculative final section is not used. Web refs turn33view0, turn34view3, turn61view1.
6. Dimitri Ara, Albert Burroni, Yves Guiraud, Philippe Malbos, François Métayer and Samuel Mimram, *Polygraphs: From Rewriting to Higher Categories*, LMS Lecture Note Series 495, Cambridge University Press, 2025, DOI 10.1017/9781009498968. [Author PDF](https://webusers.imj-prg.fr/~yves.guiraud/articles/polybook.pdf). Read Theorem 7.3.5 (critical confluences form a coherent completion), Propositions 9.2.3 and 9.3.2 with their normalization/contraction proofs, and the partial-resolution statement 9.3.7. Applied only through degree three to the explicit terminating three-rule presentation. Publisher page opened to verify year, series, DOI and authors. Web refs turn55view0, turn55view1, turn56view0, turn60view1.
7. Zbigniew Fiedorowicz, *A counterexample to a group completion conjecture of J. C. Moore*, Algebraic and Geometric Topology 2 (2002), 33–35, DOI 10.2140/agt.2002.2.33. [Primary article](https://www.maths.tcd.ie/EMIS/journals/UW/agt/ftp/main/2002/agt-2s3.pdf) opened in full. Its five-element rectangular-band lemma informed a discarded attempt to build a Delta_inj diagram. The exact-index theorem shows such a diagram cannot exist. This article is not a dependency for the main conclusions. Web ref turn60view0.

## Original body not obtained

Dusa McDuff, *On the classifying spaces of discrete monoids*, Topology 18 (1979), 313–320, DOI 10.1016/0040-9383(79)90022-3. The [Celebratio record and abstract](https://celebratio.org/McDuff_D/article/412/) were opened (turn21view1, turn23view0, turn59search2). The DOI link redirected to Elsevier and returned a nonretryable retrieval error. Repeated exact-title/PDF searches did not produce the original body. No proof here relies on the unavailable paper; Fiedorowicz's primary papers were opened separately.

## Search log and outcome

All searches below were run on 17 November 2026 using the available web search, with stronger primary-source verification where a routine search did not give the needed coverage.

- `"colimits" "free monoids" "filtered"`
- `"semicosimplicial" "monoid"`
- `"cosimplicial" "free monoids"`
- `"exact colimits" "monoids" classifying`
- `"free monoids" "colimit" homotopy`
- `"cosimplicial" "free monoid" classifying`
- `"exact colimits" "free monoids"`
- `"free categories" "exact" "colimits" homology`
- `"classifying spaces" "free monoids" colimit`
- `"semicosimplicial" "monoids"`
- `"exact colimits" "monoids"`
- `"free monoids" "homotopy" "colimits"`
- `"free categories" "homotopy colimit" exact`
- `"On the classifying spaces of discrete monoids" McDuff pdf`
- `McDuff 1979 classifying spaces discrete monoids pdf topology 313 320`
- `"On the classifying spaces of discrete monoids" filetype:pdf`
- `"A counterexample to a group completion conjecture" Fiedorowicz pdf`
- `"Fibrations de petites catégories" Evrard 1975 pdf`
- `"strictement asphérique" "chemins"`
- `"strictly aspherical" "path" category`
- `"Fibrations de petites catégories" "Evrard" "strict"`

No exact statement of the full strict endpoint classification or of the exact-index/free-monoid theorem D.6 was located. D.6 is proved directly here by the fixed-object translation-category argument, not attributed to any of these search hits. This search outcome is not a claim of novelty. Search-result excerpts and discussion-site pointers served discovery only; technical dependencies are the opened primary material listed above.
