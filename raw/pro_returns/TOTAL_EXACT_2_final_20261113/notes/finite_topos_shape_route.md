# Topos/shape route to totality implying exactness

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. No priority claim. This note records primary-source access and a precise failed inference; it does not decide Part A.

## Status and variance

No opened primary theorem in this search establishes that preservation of discrete objects by the shape adjoint forces exactness of its abelian left adjoint. No counterexample satisfying the actual totality hypothesis was found. The sources below distinguish the relevant adjoints and make several tempting substitutions invalid.

For a small category \(A\), put
\[
\mathcal E=\operatorname{Set}^{A},\qquad
\mathcal X=\operatorname{Fun}(NA,\mathcal S).
\]
The site underlying the presheaf notation is \(A^{op}\), so this convention retains the problem's covariant actions. Constant diagrams have left adjoints \(\Pi_0=\operatorname{colim}_A\) on sets and \(\Pi_\infty=\operatorname{colim}_A\) on spaces. The latter is a homotopy colimit. For a discrete diagram \(H\),
\[
\Pi_\infty H\simeq B\operatorname{El}_A H.
\]
Thus totality says that \(\Pi_\infty H\) is discrete for every such \(H\), with its components identified with \(\Pi_0H\).

This is stronger than the existence of the shape adjoint. It does not assert that \(\Pi_0\) preserves binary products. A theorem imposing siftedness or cohesive product preservation would not settle the stated problem; the known exact example involving ordinal injections prevents that substitution.

## Opened primary sources

### Volpe: essential morphisms and extension of coefficients

Volpe (2025), *The six operations in topology*, was opened in full at the publisher. Relevant statements are Corollary 2.25, Proposition 3.13, Definition 3.14, Example 3.16(ii)–(iii), Lemma 3.18, and Corollary 3.21.

Definition 3.14 calls a geometric morphism essential when its inverse image has a left adjoint. Over spaces, Example 3.16(ii) identifies this with local contractibility. Example 3.16(iii) transports the adjunction by tensoring presentable categories. Corollary 2.25 identifies this tensor operation with coefficient-valued sheaves.

These statements construct the stable left adjoint but assert no preservation of the abelian heart. Every presheaf \(\infty\)-topos already has the essential adjunction, independently of totality. The remaining issue is precisely degree-zero preservation of its extension to derived abelian coefficients.

Primary URL: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/topo.70050

### Chough: what shape computes

Chough (2021), *Topological types of algebraic stacks*, was read in the author's 36-page manuscript, especially §2.4, manuscript pp. 18–19. Proposition 2.4.2 identifies the connected components of the topological type with those obtained from the connected-components functor. Theorem 2.4.5 compares maps into constant Eilenberg–Mac Lane objects, and Proposition 2.4.10 compares the associated constant-coefficient cohomology.

These comparisons apply to constant coefficients on slices; they do not replace arbitrary abelian objects by constants. The apparently stronger Proposition 2.4.13 has the additional hypothesis, stated in §2.4.12, that the relevant left adjoint preserves finite limits. That hypothesis is not available here.

Author manuscript: https://cgp.ibs.re.kr/~chough/chough_toptypes.pdf

Publisher metadata: https://academic.oup.com/imrn/article/2021/10/7799/5424979

### Blechschmidt: internal and external injectivity

Blechschmidt (2018), *Flabby and injective objects in toposes*, was opened as the 17-page arXiv PDF. Theorem 3.8, PDF p. 10, gives external injectivity implying internal injectivity. Its converse requires a localic topos and the stated metatheoretic choice assumption. The following paragraph extends this to modules when there is a natural numbers object. Scholium 3.10 likewise requires a localic topos to turn flabby extension objects into global extensions.

The presheaf topos in the main problem is not assumed localic. Therefore this theorem does not turn a possible internal splitting argument into the required global additive splitting. Mere divisibility of a constant group also does not supply that missing global extension property.

Primary PDF: https://arxiv.org/pdf/1810.12708

The MPI PDF URL was found but its web-reader response had unsupported application/octet-stream content; the arXiv body was successfully read instead.

### Christensen and Flaten: sheaf Ext is not ordinary Ext

Christensen and Flaten (2025), *Ext groups in homotopy type theory*, was opened in the journal PDF. Definition 3.3.1 distinguishes external from internal injectivity. The paragraph following it, printed p. 51, explicitly gives the trivial \(\mathbb Z/2\)-action on \(\mathbb Q/\mathbb Z\) as internally injective but not externally injective. Theorem 3.3.14 identifies the internal Ext construction with sheaf Ext when sets cover. Corollary 3.3.16 additionally requires the global-sections functor to preserve epimorphisms before its global points recover ordinary Ext; Remark 3.3.17 gives the local-to-global spectral sequence.

The extra condition concerns the right adjoint \(\Gamma\), not the connected-components left adjoint \(\Pi\). Substituting it for totality would change the question.

Primary PDF: https://www.dml.cz/bitstream/handle/10338.dmlcz/153491/HigherStructures_009-2025-2_2.pdf

### Mielke: a different homology theory

Mielke (1993), *Topos based homology theory*, was opened in the DML-CZ PDF. Corollary 2.5 concerns triviality of homology theories defined relative to specified interval/disjoint-relation homotopy structures in a De Morgan topos. Theorem 3.6 constructs singular homology from a sufficiently tight cosimplicial object.

The input homology theory and homotopy structure differ from the derived abelian connected-components functor in the present question. This result cannot be cited as vanishing of \(L_i\Pi^{ab}\).

Primary PDF: https://www.dml.cz/bitstream/handle/10338.dmlcz/118612/CommentatMathUnivCarolRetro_34-1993-3_18.pdf

### Lehner: the homology comparison is for constant coefficients

Lehner (2026), *Shape theory of infinity-topoi: Inverse limits, products, and (co)homology*, was downloaded from the primary arXiv PDF after the web-reader endpoints failed. The PDF is version 1, dated 18 August 2026. The local files are `sources/Lehner2026_shape.pdf` and `sources/Lehner2026_shape.txt`. Sections 4, 8, and 9.1–9.3 were inspected, including the complete proofs of the comparison theorems cited here.

Definition 4.3 and Example 4.4, printed p. 14, define local contractibility by existence of the shape left adjoint and assert it for every presheaf infinity-topos. Example 4.6 includes every slice of such a topos. Proposition 4.7 lists equivalent conditions; none requires the shape of a discrete object to be discrete. Thus local contractibility alone is weaker than the main hypothesis.

Definitions 8.6 and 9.6, printed pp. 33 and 38, define coefficient-valued cohomology and homology using a single object \(E\) of a presentable coefficient category \(\mathcal D\). Theorem 8.9, printed p. 34, identifies cohomology with \(E^{\Pi_\infty\mathcal X}\) for locally contractible \(\mathcal X\). Theorem 9.10, printed p. 40, identifies homology with
\[
H_\bullet(\mathcal X,E)\simeq
\Pi_\infty(\mathcal X)\otimes E.
\]
Here \(E\) is a constant coefficient object on the topos. It is not an arbitrary object of \(\operatorname{Fun}(A,D(\mathbb Z))\). The proof transports the essential adjunction through the functor category of colimit-preserving cosheaves; it supplies no extra assertion about preservation of a heart.

Applying Theorem 9.10 with \(E=H\mathbb Z\) to \(\mathcal X/H\), for a discrete \(H:A\to\operatorname{Set}\), yields precisely the familiar permutation-module calculation
\[
H_\bullet(\mathcal X/H,H\mathbb Z)
\simeq C_*(B\operatorname{El}_A H;\mathbb Z)
\simeq \mathbf L\operatorname{colim}_A\mathbb Z[H].
\]
The last equivalence follows directly by identifying the simplicial replacement chains: an \(n\)-simplex is a composable length-\(n\) string in \(A\) together with an element of \(H\) at its initial object. Under totality, the higher homology groups in this display vanish. Passing from these permutation modules to every abelian diagram is still the missing step. Consequently the theorem confirms the existing reduction without solving it.

Theorem 9.21, printed p. 43, gives the same constant-coefficient formula for compact topoi and compactly assembled stable coefficient categories. Its different compactness hypothesis does not turn the statement into one about arbitrary coefficients, and no compactness of our presheaf topos is assumed.

Primary PDF: https://arxiv.org/pdf/2608.17525 . The reproducible download record is `code/finite_source_fetch_topos.py` and its output.

## A precise obstruction to an unrestricted slice-acyclicity argument

The following elementary example rules out one general inference that might otherwise be inserted between the shape comparison and abelian injectivity:

> A coefficient object can have zero positive cohomology on every discrete slice, and have a divisible underlying group, without being externally injective.

Let \(G=\mathbb Z\), let
\[
R=\mathbb Z[t,t^{-1}],
\]
and give \(D=\mathbb Q\) the \(R\)-module structure in which \(t\) acts by multiplication by \(2\). For every \(G\)-set \(H\), one has
\[
\operatorname{Ext}^{r}_{R}(\mathbb Z[H],D)=0
\qquad(r>0).
\]

Here is a direct proof covering arbitrary, not merely finite, \(H\). Decompose \(H\) into orbits. A free orbit has permutation module \(R\), which is projective. An orbit with stabilizer \(n\mathbb Z\), \(n\ge1\), has permutation module \(R/(t^n-1)\) and a free resolution
\[
0\longrightarrow R\xrightarrow{t^n-1}R
\longrightarrow R/(t^n-1)\longrightarrow0.
\]
Applying \(\operatorname{Hom}_R(-,D)\) gives multiplication by the nonzero rational integer \(2^n-1\), an automorphism of \(\mathbb Q\). Thus the first Ext group vanishes and there are no higher groups. Taking the direct sum of these orbit resolutions gives a projective resolution for \(\mathbb Z[H]\); applying Hom gives products of the corresponding exact complexes, and products of abelian groups are exact. This proves the displayed vanishing for every \(H\).

Under the usual slice/orbit identification, this is the vanishing of all positive cohomology of the pullback of \(D\) to every slice \((G\text{-}\operatorname{Set})/H\).

Nevertheless \(D\) is not injective. The ideal
\[
J=(t-2)R
\]
is isomorphic to \(R\), because \(R\) is a domain. The map
\[
\varphi:J\longrightarrow D,\qquad
\varphi((t-2)r)=r(2)
\]
is well-defined and \(R\)-linear; Laurent evaluation lands in \(\mathbb Z[1/2]\subseteq\mathbb Q\). It sends \(t-2\) to \(1\). Any \(R\)-linear map \(R\to D\), however, sends \(t-2\) to zero because \(t\) acts on \(D\) as \(2\). Consequently \(\varphi\) cannot extend across \(J\hookrightarrow R\).

This is not a counterexample to totality implying exactness: \(D\) is not a constant coefficient object, and \(BG\) is not contractible. The example establishes only that the all-slices cohomology test cannot be promoted to external injectivity by an unrestricted topos theorem. An argument for the main problem must use the special constantness of the coefficient object or another additional structure.

No finite experiment is used in this example.

## Access failures and uninspected leads

Initial web-reader attempts for Lehner's primary abstract, PDF, versioned PDF, and HTML returned disabled access; export/ar5iv variants were inaccessible and the university author page timed out. A subsequent ordinary public PDF download succeeded, and the body was read as described above. Theorem snippets reproduced by third-party pages were never used as verified source claims.

Harting's 1983 papers were encountered through precise citations in the opened Blechschmidt and Christensen–Flaten papers. Their original bodies were not opened in this search; no additional assertion is attributed directly to them.

Searches also returned recent automatically generated lecture sites. Their search previews were not accepted as primary literature. Results using “totally aspherical” in the test-category/diagonal sense were excluded, since that notion differs from the manuscript's definition.

Lehner's primary PDF and extracted text are saved in the workspace. The other URLs above identify bodies actually opened in the web reader; they have not been downloaded by this follow-up. The present note distinguishes those two access modes.

## Search record

Searches included the following exact strings or their displayed conjunctions, using both available engines:

- topos "locally connected" "homology" "left adjoint"
- topos "shape" "slices" "discrete" "locally contractible"
- "connected components" "abelian" "topos" exact
- "locally connected" "acyclic" topos homology
- "locally contractible" topos "abelian"
- "left adjoint" "abelian objects" "locally connected"
- "homological dimension" "locally connected" topos
- "discrete shape" topos homology
- "0-truncated" "left adjoint" "homology" topos
- "injective" "constant sheaf" "locally connected" topos
- "Locally injective abelian groups in a topos" pdf
- "Flabby and injective objects in toposes" arxiv
- "topos" "acyclic slices"
- "colimit" "abelian" "homotopy invariant" exact
- catégorie "totalement asphérique" "exact"
- "dimension homologique" "colimite" catégorie
- "colimit" "discrete" "topos" "homology" exact
- "homotopy colimits" "sets" "exactness" categories
- "acyclic" "injective" "permutation modules" constant category

## References

Blechschmidt, I. (2018). *Flabby and injective objects in toposes* [Preprint]. arXiv. https://arxiv.org/abs/1810.12708

Chough, C.-Y. (2021). Topological types of algebraic stacks. *International Mathematics Research Notices, 2021*(10), 7799–7849. https://doi.org/10.1093/imrn/rnz065

Christensen, J. D., & Flaten, J. G. T. (2025). Ext groups in homotopy type theory. *Higher Structures, 9*(2), 17–61. https://doi.org/10.21136/HS.2025.09

Lehner, G. (2026). *Shape theory of infinity-topoi: Inverse limits, products, and (co)homology* (Version 1) [Preprint]. arXiv. https://arxiv.org/abs/2608.17525

Mielke, M. V. (1993). Topos based homology theory. *Commentationes Mathematicae Universitatis Carolinae, 34*(3), 549–565. https://www.dml.cz/handle/10338.dmlcz/118612

Volpe, M. (2025). The six operations in topology. *Journal of Topology, 18*(4), e70050. https://doi.org/10.1112/topo.70050
