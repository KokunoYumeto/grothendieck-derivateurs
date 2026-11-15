# Complete C048 localizer dichotomy

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.

## Source verification

Cisinski (2006), Astérisque 308, Proposition 9.2.17(a)–(b), printed pp.369–370, explicitly applies to any fundamental localizer W. It identifies inversion of the sphere-category Δ/∂Δ^(n+2) with containment of W_n. Corollary 9.2.15 identifies the homotopy-group convention. The author-hosted PDF was opened on the web; the supplied published PDF was then inspected directly at background/papers/Cisinski_Ast308/smf_ast_308.pdf. The theorem numbers agree; pagination differs between versions. Citation uses published pagination.

The appearance of accessibility later in the proof concerns a particular minimal generated localizer; it is not a hypothesis on the arbitrary W in the proposition.

## Proved deductions

The supplement sections/F_followup.tex gives an explicit groupoid proof that the Grothendieck-span comparison to an ordinary pushout is a W1-equivalence whenever one leg is injective on objects. Object injectivity makes the connector-based conjugation well defined; faithfulness is not needed, and the other leg may identify objects.

If S2 is W-aspherical, W1 is contained in W. Relative Theorem A supplies invariance of Grothendieck constructions under objectwise W-equivalences; the supplement proves this through the actual slices. Two-out-of-three therefore makes every object-injective functor a W-cofibration.

All full sieves consequently satisfy C048 when S2 is W-aspherical. Combining this with F:interval-impossibility proves the complete dichotomy: the maximal class is all full sieve inclusions when S2 is inverted, and only isomorphisms otherwise. This is a statement about the specified endpoint pushout-product operation, not an additional assertion about strict or total sieve composition.

## Verification and reproducibility

The paths_audit sibling independently checked the published proposition, both connector functors and their natural isomorphism, the relative-Theorem-A argument, and the resulting dichotomy. Audit passed without a mathematical amendment.

code/cd_cisinski_source.py and its saved output verify the relevant numbered statements in the supplied published source. Extracted copyrighted source text remains outside the deliverable directory.

The supplementary statement ledger is research/CD_C048_results.csv.
