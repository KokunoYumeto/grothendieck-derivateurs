# Audit of Leads 6, 8, 9

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.

## Results

- Lead 6: proved, label `FT:finite-test`. Explicit natural transformation H_u -> H sends [d,f] to H(f)(h_d); induced category-of-elements functor factors v **strictly** through j_u. Sphere maps are represented by functors from face posets after finite subdivision; Ex-infinity argument recorded in `FT:sphere-representatives`. No restricted test on H is substituted for the universal hypothesis.
- Lead 8: true for every **nonzero unital** coefficient ring; literally false if 'any ring' includes the zero ring. Label `FT:ty` gives precise contravariant bijection from endpoint-preserving monotone vertex functions to monotone sign-preserving maps of letters, all empty-word cases, composition, absence of squares and affine equalizers. Stronger explicit obstruction: for H = h_(++)/(ge~gc), H_1(El H; Z)=Z. Thus non-totality is proved directly, not only via a cited quasi-filteredness implication.
- Lead 9(a)–(d): proved, label `FT:minimal-family`. Read IM76 pp.296–298 (Corollary4.3, Proposition4.5) and TOTEX proof of nonempty-cosieve inheritance in full. The global minimality condition is essential for part (d); no reverse arrows, bounded hom sets, or finite-category assumptions are added.

## Code

`finite_ty_verify.py` and `finite_ty_verify.out`: 961 word pairs checked for the variance bijection; 2731 composable pairs checked for composition; 1023 target words through length9; 7937 outgoing arrows checked for the dual certificate; 103033 square candidates ruled out via disjoint supports. Universal proof is independent of finite bounds. The same integral functional certifies the obstruction over every nonzero ring; modulus1 checks the zero-ring exception.

## Read sources for inherited steps

1. PRETOT paper, Definition E.1 (`E:path-definition`), checked: interval categories are free oriented lines; endpoint and monotonicity restrictions are the data used in the explicit letter/vertex bijection. No alternative path-category convention was silently substituted.
2. TOTEX paper, nonempty full cosieves (`D:cosieves`): verified the empty-set extension to A is a covariant functor because no arrow exits a cosieve; its element category agrees exactly with the old one. Connectedness is supplied here directly by condition I applied to maps from p.
3. Isbell–Mitchell1976, Corollary4.3: verified its finite-endomorphism conclusion, derived from Corollary4.2; composing an equalizer of ba_i with b gives equalization of a_i. Proposition4.5 applies to the single connected representable with a uniform finite bound; the quotient construction makes all maps injective and maximal finite cardinality turns them into bijections, where IV's necklace forces triviality.

## Technical note

The name 'comprehensive factorization' in Lead6 does not mean j_u is final in the covariant convention. For D={p}, j_u includes the initial object into p/A and is generally initial, not final. The proof does not claim or use finality of j_u. The strict factorization alone is what is needed.

4. Goerss–Jardine, *Simplicial Homotopy Theory*, 2009 reprint, opened at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf. Theorem I.11.4, Section III.4 pp.183–188 (subdivision/Ex adjunction, last-vertex maps), Theorem III.4.8: the canonical map into Ex-infinity is a weak equivalence and its target is Kan. These supply the precise finite subdivision lemma; finite presentability of the source then factors a map through one finite Ex stage.
