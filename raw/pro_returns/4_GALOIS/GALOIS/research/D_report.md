# Part D research and audit report

Prepared by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Sources actually opened

We read the supplied prompt, all 275 rows of `DER_I-b_claims.csv` for selecting the requested statuses, and the manuscript and companion passages at I ms. 76–85, 93–100, 102–126. We inspected the opening Chapter XI companion treatment of the intrinsic HOT-fibration criterion, its comma-category argument, the nonabelian coefficient issue, and its comparison with model fibrations. The original French text at ms. 122 says “ne pas être stable par composition (que je sache!)”; the qualification is treated as a question, not a proof.

Primary results checked are Cisinski (2009), published PDF, Theorem 1.3, Corollary 3.8, and the surrounding definitions; Cisinski (2006), Theorem 5.2.15 and Definition 5.2.16; Quillen (1973), original scan, Section 1 Theorem B and its corollary; and Rezk (1998), author's preprint, Section 2, especially Propositions 2.2 and 2.7. The accessible-localizer model structure is only left proper without an additional properness hypothesis. The slice right Quillen proof of fibre detection does not need right properness.

The 2026 web searches used the exact queries “Charles Rezk Fibrations and homotopy colimits of simplicial sheaves sharp maps Proposition 2.7” and “Cisinski locally constant functors Corollary 3.8 Theorem 1.3 2009”. We opened the author's Rezk PDF, the published Cisinski PDF and the Quillen scan. Search engine crawl dates were not interpreted as publication dates. These searches checked the source assertions, not novelty of the finite counterexamples. The latter are developments of the attached companion and are not claimed to be new.

## Mathematical corrections

The repaired weak-fibration argument has an asymmetric conclusion: a 1-complete input produces a constant-coefficient equivalence upstairs. It does not prove that the upstairs map is 1- or 2-complete. Full local-coefficient direct-image control produces the composable cohomological class. In an enhanced complete coefficient theory, Part C identifies this with the 1-complete class.

The rational composition counterexample on I ms. 118 is valid. Its intermediate category has two objects and five arrows; its total category has four objects and ten arrows. The fibre change from two discrete points to the regular C2 action groupoid changes degree-zero rational cohomology.

The finite 2-complete composition counterexample on I ms. 122 is also valid. Its nonzero normalized C2 cocycle on a barycentrically subdivided sphere has genuinely nontrivial coherence even though every individual transport is the identity on C2. The associated total category is simply connected. It is not enough to check its first homology, so the verifier also performs explicit Tietze eliminations on a complete fundamental group presentation.

A stronger consequence of that construction is that total Wlc-equivalence between genuine HOT-fibrations need not be Wlc-equivalence on fibres, even over a completely Set-aspherical base. This refutes blanket Lead 3, including its proposed replacement of the base-asphericity qualification. A second finite example, Groth(BC2→*) over [1] with its section, shows that total-to-fibre detection also fails for arbitrary universal W1-preserving fibrations. This does not contradict W1 detection for genuine HOT structural fibrations: the latter follows from the homotopy-fibre criterion in Part C.

The precise positive replacement is available for an accessible Wlc fundamental localizer: use its associated Thomason model fibrations. Base change and composition follow from lifting properties. A map of such fibrations over a common base is a weak equivalence between fibrant objects of the slice; pulling back to a point is right Quillen, hence preserves that weak equivalence. This does not identify all these model fibrations with sharp maps or silently assume right properness.

Universal constant equivalences do imply full faithfulness on the entire derivator category, under the stated all-small-shapes axioms. D.7 supplies the full factorization-category mate argument, not only the constant or locally constant special case.

Other corrections retained and checked: bundle classification does not produce unique isomorphisms; E=G discrete in the quotient recipe makes the fibre inclusion the identity; the S2-antipodal/S1-reflection quotient retains a rational class in degree three; the six-object orbit relations compose by multiplying endpoint signs; a proper cosieve can have an empty-to-point comma transition; and compatible internal Homs do not turn a constant equivalence into a fully faithful restriction. The last assertion requires the adjective cohomological and the actual monoidal unit. The printed invariant-to-invariant arrow on I ms. 93 is ill-typed as the intended nonisomorphism and must target the full cohomology.

## Computations and outputs

`code/D_verify_finite.py` constructs all category laws in the two composition counterexamples, verifies all unit and associativity axioms, checks the normalized cocycle on 194 quadruples, and reduces complete fundamental group presentations. It checks 1,552 associative triples for the 14-object gerbe and 2,064 for the 15-object enlarged total. Tietze elimination removes all 73 and 87 generators, respectively; the fibre retains the presentation <t | t²>. Its output is `code/D_verify_finite.out`.

`code/D_verify_more.py` checks the reversed-transport category, its fundamental-group presentation, the six-object sphere and four-object circle, corrected orbit composites, and rational homology of the 12-object orbit-product category. Its chain dimensions are (12,60,96,48), its boundary ranks (11,49,47), and its rational Betti vector (1,0,0,1). Its output is `code/D_verify_more.out`.

`code/D_verify_remaining.py` verifies the nonidentity sheet-swap automorphism, the regular quotient isomorphism to Z, the comma counts (0,1) for the proper cosieve, and the trivial-to-sign rational Hom calculation. Its output is `code/D_verify_remaining.out`.

`code/D_build_audit.py` selects exactly the 21 source rows with status false or conjectured whose first manuscript page lies in 76–126. It requires exact equality between the selected IDs and the disposition table, so no requested row can silently disappear. Its output is `code/D_build_audit.out`; the complete table is `research/D_audit.csv`.

The computational checks supplement the mathematical proofs. A failed initial syntax parse of the first verifier was corrected before it was run successfully; no failed mathematical check was suppressed. The finite proofs themselves are independent of the software.

## General gluing resolved

D.11 is now Proved for every Der1--4 derivator. B.3 establishes relative Theorem A and hence the fundamental-localizer property of Wlc without enhancement. The fundamental sublocalizer generated by the cosieve inclusion X1→X is accessible; its simplicial model structure makes the nerve inclusion a trivial cofibration, whose pushout is again trivial. Thus X→X amalgam_X1 X belongs to Wlc. The W1 gluing statement follows from B.5 direct excision. No accessibility assumption on the whole Wlc class is needed. The former arbitrary-derivator descent gap is resolved; the result still concerns the specified fork and does not assert universal stability of every original weak fibration condition.
