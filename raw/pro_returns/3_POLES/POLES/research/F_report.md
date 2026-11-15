# Part F: sources, proofs, computations, corrections, and open obligations

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Sources actually read

The original Chapter XVI transcription was read for Loc (1), (1 bis), (1 ter), Proposition 3.3, and the following discussion. Chapter XII ms. 76 and the corresponding companion row XIIba-A-053 were read directly. The attached complete author TeX of Hovey–Palmieri, *The structure of the Bousfield lattice*, was read in Sections 2, 7, and 9. The attached Berrick–Casacuberta PDF was converted to text and read, especially Theorems 3.3 and 4.3. Hausmann–Husemoller, *Acyclic maps*, was inspected for the distinction between acyclic fibers, twisted homology equivalences, and ordinary homology equivalences; the paper's introduction and first sections were read, but no unverified theorem number is used from it. Cisinski's Astérisque 308 PDF was searched and the exact statements of Definition 3.3.2, Sorites 3.3.8, Proposition 4.2.4, Theorem 4.2.15, and Theorem 9.4.2 were read.

Primary sources additionally opened on the web:

- Tyler Lawson, author PDF dated 11 March 2019, `https://www-users.cse.umn.edu/~tlawson/papers/bousfield.pdf`, especially Example 9.20.
- Casacuberta–Gutiérrez–Rosický, `https://www.ub.edu/topologia/casacuberta/articles/cgr.pdf`, Theorems 3.7 and 3.9, Proposition 3.8, Section 4.
- Wolcott, `https://msp.org/pjm/2015/276-2/pjm-v276-n2-p14-p.pdf`, Propositions 6.2 and 6.4 and the paragraph following 6.4.
- Hovey–Palmieri–Strickland, `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/axiomatic.pdf`, Theorems 2.3.2 and 3.2.2 and the following discussion.
- Hovey–Palmieri arXiv record `https://arxiv.org/abs/math/9801103`, the author's research listing, and the AMS listing for publication metadata.
- Berger–Ratković, `https://math.univ-cotedazur.fr/u/cberger/Gabriel-Morita.pdf`, Definition 2.1, Propositions 2.3–2.8, Remark 2.9; the author's publication list verifies *Applied Categorical Structures*, 27(1), 23–54 (2019), DOI 10.1007/s10485-018-9539-x.
- Pützstück, *Tensor-Nilpotence and the Size of the Bousfield Lattice*, `https://arxiv.org/pdf/2608.06104`, v1 of 6 August 2026. The complete seven-page PDF was downloaded and read after the browser PDF endpoint failed. Theorem 1.1, Corollary 1.2, and Theorem 1.4 concern tensor-nilpotence, Hovey–Palmieri's retract conjecture (3.12), and the cardinality of the Bousfield lattice. They do not settle the distinct localizing-subcategory conjecture (9.1). No claim from a machine-generated review of that paper is used.

Every entry in F_references.bib is marked verified, with the specific material opened. “Verified” is not a claim that every result in the cited source was independently re-proved.

## Searches

Searches were run on 10 November 2026 for combinations of “Bousfield integral homology Morava K theory smash HZ acyclic spectrum,” “localizing subcategories spectra generated bounded below spectra,” “stable acyclic classes spaces suspension localization,” “homotopical localization spaces cofiber homological,” “nullity classes stable,” “localizing subcategory not a Bousfield class spectra,” “Hovey Palmieri Conjecture 9.1,” and specific searches for loc(HFp), loc(I), and loc(HZ). The searches located the author and publisher sources listed above. Secondary snippets were used as leads only, not as authority for mathematical claims. No novelty claim is made for the free-group endomorphism certificate or the Galois formulation.

## Mathematical corrections

Lead 6 is false as a bijection with **all** localizing subcategories, even with accessibility. Both zero and the nonzero HZ-acyclic spectra induce exactly W_Z on maps of spaces. An even more explicit set-generated example is loc(K(n)) for any prime and n>0: it is nonzero, lies in the HZ-acyclic spectra, and has no nonzero connective object. Every cofiber probed by a map of spaces is connective. This is a failure of injectivity, independent of any unresolved converse about the image.

The correct Galois connection is T(W)=loc{cofib(Σ∞_+Bu):u∈W} and R(L)={u:cofib(Σ∞_+Bu)∈L}. The stable fixed objects are exactly L=loc(L∩D), where D is the class of reduced suspension spectra of pointed spaces. Fibers are determined exactly by intersection with D. The unstable fixed objects are the stable-detectable classes W=RT(W). The two operators give inverse order isomorphisms on these fixed objects. This is the precise image description established here; it is not silently expanded to all reversible localizers.

The expression Σ∞cofiber(g) must mean the reduced suspension spectrum with the specified cone vertex. Adding another disjoint basepoint would give the wrong zero test.

The universal plus construction and W_Z have the same aspherical spaces but different equivalences. The explicit endomorphism α of F2, x↦x and y↦yxyx⁻¹y⁻¹, is a homology equivalence but not surjective. Both copies of BF2 are plus-local. Its cofiber is acyclic and therefore plus-aspherical. Thus aspherical-object equality does not imply map-class equality, and plus localization does not satisfy reverse excision. Nullification at any individual acyclic space is also strictly below W_Z and fails reverse excision.

Row XIIba-A-053 is affirmative in the modern relative-Theorem-A convention fixed by the prompt. Cisinski Proposition 4.2.4 supplies arrow-retract closure automatically. A direct Grothendieck-construction argument makes the two pieces retracts of an aspherical homotopy wedge. Reverse excision is not used. This does not claim that the same proof follows from the manuscript's weaker absolute Loc (3) without the relative axiom.

Wolcott's example of a non-Bousfield localizing subcategory lives in the HFp-local category. It cannot be imported unchanged into the entire stable homotopy category; the author explicitly flags this distinction after Proposition 6.4.

## Computation

`code/f_free_group_witness.py` defines every arrow and composition of the one-object category BS3, verifies closure, all 216 associativity triples, identities, and inverses, then checks two distinct homomorphisms F2→S3 with equal composites with α. It verifies α's abelianization matrix is the identity. It also computes the orbits of the action used in Part C: the original action is transitive, whereas the pullback action along α has orbits {1,2} and {3}. Full output is in `code/f_free_group_witness_output.json`.

`code/f_finalize_section.py` performs only idempotent ordering of the separately authored Part F blocks; its output records the statement order. It makes no mathematical inference.

## Exact remaining obligations

F.14 retains the implication “accessible and reversible cofiber detection ⇒ W=RT(W)” as unresolved in this audit. The obstruction in the attempted proof is that closure under finite unstable suspensions and cofibers does not by itself justify transfer of arbitrary stable localizing constructions back to maps of spaces. The Galois formulas remain valid without that implication; Lead 6 is already refuted by the independent noninjectivity example.

F.14 also explicitly retains the test whether loc(HFp), in the category of all spectra, is the kernel of smash with some spectrum. This is an unresolved verification here, not a claim to establish its current research status. The published Hovey–Palmieri Conjecture 9.1 and Proposition 9.2 were checked; no theorem was found in the performed searches that settles the full replacement of arbitrary localizing kernels by homological Bousfield classes. Existence of a localization for a set-generated localizing subcategory is kept separate from homological representability.

The focused follow-up checked exact phrases involving “localizing subcategory,” “HFp,” “HF_p,” “Hovey–Palmieri Conjecture 9.1,” and “Bousfield classes,” including recent coverage. It found Pützstück's 2026 paper and checked its full text as described above. The test is sharpened using the elementary argument in Hovey–Palmieri Proposition 9.2: loc(HFp) is homologically representable if and only if it equals the a(HFp)-acyclic spectra, where a(HFp) is a wedge representing all Bousfield classes annihilating HFp. This is the smallest homological kernel containing HFp, so the precise remaining issue is an equality of two specified subcategories.

For the other F.14 obligation, Berger–Ratković's terminology makes the failed implication particularly clear. Their “excisive” hypothesis is conservative suspension and yields the cofiber diagram lemmas; their stable embedding statement in Remark 2.9 requires *fully faithful* suspension. One cannot substitute the former hypothesis for the latter. The citation is incorporated in F.14; it narrows the exact gap rather than concealing it behind a general stabilization reference.

## LuaLaTeX verification

The supplied TeX installation contained the package trees and LuaHBTeX executable but lacked lookup databases, generated formats/configuration, Lua font-loading dependencies, and Pagella. `code/f_tex_runtime.py` repairs this only inside `tmp/tex`, using an explicit list of five public CTAN packages with SHA-256 hashes in `code/f_tex_dependencies.json`. It preserves HOME and the system installation and retains TeX's restricted write policy, authorizing font-cache writes through the workspace-specific TEXMFOUTPUT. The format output is in `code/f_tex_format_output.txt`. `code/f_check_latex.py` compiled the standalone Part F with LuaLaTeX/BibTeX and two convergence passes; the initial verified version produced a nine-page PDF with no overfull or underfull boxes, missing characters, or unresolved citations. Links to Part B are naturally absent from that standalone wrapper. `code/build_lualatex.py` supplies the same reproducible four-pass build for the integrated paper.

The definitive integrated build, including A.19, the proved G.26 with its finite Reedy construction, H.8, all final Part F additions, the canonical merged bibliography, and the final PDF metadata, completed successfully: 71 pages and 638,865 bytes. The final log contains no LaTeX/package warnings, missing characters, underfull or overfull boxes, or PDF backend warnings. The complete transcript and machine-readable summary are `code/build_lualatex_output.txt` and `code/build_lualatex_summary.json`. The compilation required only typographical corrections to the shared operator macros, A's display line breaking, and G's TikZ cell, table/filename wrapping, and proof subheading commands; no mathematical content was changed by the build repair.
