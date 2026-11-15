# BISITE Parts B and C: research and verification report

## Delivered material

- `sections/B.tex`: B.1–B.22.
- `sections/C.tex`: C.1–C.10.
- `B_results.csv`, `C_results.csv`: the required seven-column registers, with full numbered statements, statuses, dependencies and manuscript pages or inherited claim IDs.
- `BC_references.bib`: ten primary-source entries, each carrying an explicit `verified:` note describing the scope of verification.
- `code/bc_*.py` and their outputs: exact finite category, group presentation, path-monoid and registry checks. The proofs do not infer contractibility from numerical homology.

The two sections contain 32 statements: 18 Proved, 7 Refuted, 5 Known and 2 Open. “Refuted” identifies the proposed assertion being rejected; its text and proof specify the corrected conclusion or counterexample. “Open” means the exact remaining task is not resolved in this manuscript; it is not a claim of priority or of a newly discovered open problem.

## Main conclusions and the variance audit

The presheaf fine test is `s\X -> s\Y`, and the covariant test is `X/s -> Y/s`. Their enhanced localizations for the minimal localizer are respectively `Fun(NS^op, Spaces)` and `Fun(NS, Spaces)`. B.3 gives inverse relative functors, including natural weak-equivalence comparisons, through the simplex category and its last vertex. It proves an equivalence of infinity-localizations; it does not invent a model structure on `Cat/S` for which the ordinary nerve is a Quillen equivalence.

For simplicial sets, the literal strict-slice test works over a quasicategorical base even for arbitrary, nonfibrant total simplicial sets. Over an arbitrary simplicial base one must use the appropriate fibrant replacement of the vertex. B.4 supplies the inner-horn counterexample: over `Lambda^2_1`, the left-anodyne inclusion of vertex 0 into edge 01 pulls back along the literal slice over 2 to the empty-to-point map. B.22 restores the all-base statement using the actual covariant and contravariant structures, and proves the maximal preservation property directly.

The smooth/proper dictionary is fixed by explicit outgoing and incoming lifting categories. Grothendieck-proper equals Cisinski-proper and HTT Lurie-smooth. Grothendieck-smooth is the opposite class. The current Cisinski errata matter: the general quasicategorical fibre-to-comma criterion needs universal base changes, whereas the ordinary-category nerve criterion used here remains valid. The July 31, 2026 errata were opened and checked.

The manuscript's `Wg` at XII ms.222 is the covariant `X/s` class. Its maximal universal raw-pullback-preserving class is exactly `Liss_W`. For presheaf variance the maximal class is `Prop_W`. B.6 proves both, without accessibility, by Maltsiniotis's universal preservation characterization of aspherical functors and the explicit comma/Grothendieck resolution. It does not confuse this stabilizer with the larger transporter of II ms.88–89.

## Complementarity and the coefficient examples

B.9 proves that `Liss_W intersect Prop_W` is contained in the intrinsic universal pullback-preserving class exactly for the minimal localizer and the total class. Accessibility is not assumed. The proof factors arbitrary categorical maps through minimal smooth and proper maps, obtains homotopy-pullback stability, and loops a noncontractible aspherical fibre until disconnected. Pulling back two points in different components then makes the empty category aspherical and forces the total localizer.

The requested tests are handled independently:

- `W0`: the finite regular `C2` covering.
- Every finite truncation `Wn`: an explicit sphere face-poset and its fully specified fence-path category; B.12 gives a finite witness for `W1`.
- Every nonzero spectrum homology localizer: the same three-sheeted free-group action covering and the same endomorphism, with a proof that includes nonconnective spectra.
- Rational locally constant complexes: a finite central `C2` cocycle extension of the tetrahedral-sphere face poset. Its total category is simply connected, while its self-pullback has fundamental group `C2`. The original map is a rational local-system equivalence; its self-pullback is not.

The rational local-system criterion is justified through modules over rational based-loop chains and Rivera–Wierstra–Zeinalian's Theorem 3. This avoids identifying rational homology with invariance of locally constant rational complexes. In particular, coverings preserve `W1` and rational local-system equivalences, so the three-sheeted homology witness is not a witness for those coefficient localizers. The fence path over `BC2` likewise preserves those two classes while failing rational homology preservation.

B.14 proves that cohomological fibrations, with all local coefficients after all base changes, and `W_D^lc`-proper maps have neither containment for nonterminal presentable coefficients. A universal deformation-retraction example gives one direction; a proper cosieve with nonconstant right direct image gives the other. The dual assertion is also proved. B.15 reconstructs all finite maps in GALOIS D.3–D.5 and records the smooth, proper and intrinsic classifications for both requested localizers.

## Path-model audit

The integer-fence construction is specified on objects, arrows, composition, endpoint conditions and parity of the finite-support extensions. B.8 proves the fixed-left contraction and two lifting conditions; B.19 independently proves the full endpoint result and mapping-path factorization. For `[1]`, the endpoint map has no terminal incoming lift and no initial outgoing lift because the transition can be moved arbitrarily far along the fence.

B.20 retains the actual category of finite interval types. It proves smoothness by adjoining the endpoint arrows, factoring through a slice with terminal object and padding source paths with identity edges. Properness fails because the empty type has no endpoint-preserving map to a nonempty type; the fibration claim fails because two distinct type collapses yield two morphisms to any proposed terminal lift. Thus reversing interval words does not reverse the indexing category of types.

B.21 verifies the standard fence obstruction for the five-element rectangular-band monoid. Existence of a different bifibration representative remains open, exactly as stated there. Neither the complementarity proof nor the abstract factorization uses such existence.

## Presheaf and strict higher category boundaries

C.1 gives two completely specified comma-test localizations via categories of elements for any presheaf category. C.2–C.3 show why this does not automatically extend the simplicial pair: for a component-detecting localizer one of these classes contains only isomorphisms, and every presheaf map is elementwise smooth while elementwise properness demands cartesian naturality squares. Even on `A=Delta`, these two candidate localizations are not equivalent. This is a refutation of the specified automatic transport, not a claim that no richer directed structure can be placed on that model.

C.4 states the extra data that suffice: an involutive equivalence preserving the absolute weak class and exchanging the two chosen test classes. Simplicial reversal comes from an automorphism of `Delta`, not from a false identification `Delta=Delta^op`. A test category provides an absolute homotopy theory; it does not select directed slices or an exchange involution.

For strict higher categories, C.5 resolves the exact Theorem A reference and its slice convention. C.6–C.7 prove formal fine duality in every dimension by total cell reversal, and describe the full commuting family of cell dualities. The decisive published source is Ara–Maltsiniotis (2022), Theorem 6.6, with the total-dual slice isomorphism in the proof of Corollary 6.8. These conclusions use no September 2026 model claim.

C.8 records the verified published dimension-two Thomason theorem. C.9 states precisely what an absolute model theorem would imply: the coarse slice of spaces. C.10 leaves the relative Street-nerve comparison and the higher local base-change criterion unresolved. Theorem A and an absolute Quillen equivalence do not by themselves provide those comparisons. The statement names the missing maps and does not simply label all higher-category work open.

## Primary literature and novelty checks

The supplied primary PDFs of Cisinski (2006, 2019), Lurie, Maltsiniotis (2005), and Evrard (1975) were read or extracted at the locations recorded in the bibliography. Online primary checks opened:

- Cisinski's current author errata, especially Theorem 4.4.36.
- Ara–Maltsiniotis, *Un théorème A de Quillen pour les infinity-catégories strictes I: la preuve simpliciale*, Theorem 5.2 and Remark 5.3.
- Ara–Maltsiniotis, *Comparaison des nerfs n-catégoriques*, Sections 6.4–6.8.
- Ara–Maltsiniotis, *Vers une structure de catégorie de modèles à la Thomason…*, Theorem 6.27 and Corollary 6.32.
- Rivera–Wierstra–Zeinalian, *Rational homotopy equivalences and singular chains*, Theorem 3.

Searches included the exact names “Cisinski 4.4.36 proper smooth nerve,” “Maltsiniotis structures asphericite smooth Theorem 1.2,” “Ara Maltsiniotis Theorem A strict infinity categories,” “Comparison n categorical nerves duality,” “Thomason 2 categories Theorem 6.27,” and “Rivera Wierstra Zeinalian rational homotopy Theorem 3.” Author pages, author PDFs, arXiv primary manuscripts and primary journal records were used; search snippets or earlier AI answers are not theorem authorities. Some journal landing pages timed out or rejected XHTML; the corresponding complete author PDFs were successfully opened. No novelty claim is made for any of the deductions or counterexamples.

## Reproduction and exact computational scope

Run from the workspace root:

```
python BISITE/code/bc_counterexamples.py
python BISITE/code/bc_inherited.py
python BISITE/code/bc_paths.py
python BISITE/code/bc_register.py
```

The first program checks finite category laws, the central-extension lifting equations, full nonabelian group presentations, diamond and V examples, simplex intersections and the covering permutations. It produces `bc_counterexamples.out.json`. The inherited-example checker produces `bc_inherited.out.json`; the rectangular-band checker produces `bc_paths.out.json`. `bc_register.py` rebuilds both CSV registers and checks claim IDs, statuses, cited keys and verification flags, producing `bc_register.out.json`.

The exact presentation reductions are elementary Tietze substitutions after a spanning-tree collapse. For `H` all 73 generators are eliminated; for `H x_K H` 172 of 173 generators are eliminated, leaving the order-two relation. There is no probabilistic group recognition or floating-point linear algebra. The proof gives the geometric disk argument as well, so the software is an independent verification rather than the mathematical justification.

`bc_extract.py` records reproducible text extraction of supplied primary PDFs. It requires `pdftotext` and the supplied `background` tree. Its output is an extraction log, not an assertion that every page of each book was used. All other programs use Python's standard library only.

## Cross-review of Parts E and F

The completed E.1–E.9 and F.1–F.14 were read for variance and adjunction scope. The raw-pullback exception in E.2 agrees with the classes proved here. The recognition assumptions in E.3 explicitly carry the required colimit and generator data. The left and right Kan formulas and the mate-based converse in F.2 have the correct presheaf variance. F.10's correspondence construction is consistent with its chosen ordinary categorical base and the 2022 geometric-setup convention; F.12 correctly separates the later diagonal condition and verifies the discrete-fibration repair. No change was requested to those statements. The review did not certify the later moduli-space arguments F.15–F.17.
