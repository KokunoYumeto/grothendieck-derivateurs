# Status update — 18 November 2026, 04:25 UTC

The gate described below has been settled: A2.12 refutes constant-to-LC and constant-to-arbitrary by a labelled augmented-complex category; A2.13 proves LC-to-arbitrary by the five-object split-coproduct reconstruction. The following is retained as the earlier research draft, not as a current open claim.

# Unpointed restricted-coefficient draft — 18 November 2026, 03:53 UTC

Not integrated into the proved section. A2.10 is independently audited and integrated; the arguments below are the current next reduction.

## Candidate proved reduction: the pointed envelope has the full half-axiom

Assume constant Der6prime for D. The coherent tree comparison of A2.10 supplies d_M:M→M⊔M⊔M with h d=i1, v d=i2, naturally in every shifted coefficient. For N=(s:1→M) in E=D_*, compose with the canonical map to the pointed triple wedge N∨N∨N. Naturality at s and the fold identity make this a coherent pointed map. Its two fold equations persist. Collapsing the middle pointed summand gives a natural counital comultiplication in E; the A2.10 proof gives additive E(I) in every shift. This does not assume restricted tests pass to arbitrary pointed coefficients.

Point the unpointed constant free-circle square at its selected first edge, using s at its two vertices. The section on the span extends coherently to the pushout because the span has contractible nerve. U creates pushouts and pullbacks, so the lifted square in E is bicartesian. Its root is canonically N∨F(M): the underlying pushout M⊔_1(1⊔M) is M⊔M. Its two fold maps become [id,epsilon_N]:N⊕F(M)→N. The triangular matrix [[id,-epsilon_N],[0,id]] splits this span into the constant N-span and 0←F(M)→0. Exactly the one-arrow strongness argument of A2.10 makes this coherent. Thus F(M)→Omega Sigma F(M) is an isomorphism.

Every N is a retract of F(M), without a stability premise, once E is additive. The cofiber square F1 --F(s)→F(M), 0→N exists as in A2.4, and F(s) has retraction F(!). For an additive strong derivator, a split mono i:A→B with cofiber p:B→C splits its cofiber sequence: id_B-i r kills i, hence cofiber exactness gives q:C→B with q p=id_B-i r. The map Hom(C,T)→Hom(B,T) is injective because the preceding map Hom(Sigma B,T)→Hom(Sigma A,T) is surjective (Sigma i has retraction). Consequently p q=id_C and r q=0, uniquely; q is natural for coherent split cofiber sequences. Thus N is a retract of F(M), and naturality of the suspension unit implies it is an isomorphism for every N. A2.10's cof³ and pasting argument proves all pushouts in E are pullbacks.

## Remaining gate

Transfer this implication back from E to D. Neither conservativity of F nor preservation/reflection of pullbacks by F has yet been proved under the restricted hypothesis. The square X→1⊔X over 1→1⊔1 is a pushout, but its cartesianness is exactly a nonconstant instance, so assuming it is circular. A possible affine embedding K(X)=(F(X)→F1) into a genuine derived slice would suffice if fully faithful and cocontinuous, but a bare derivator slice must not be replaced by an ordinary slice or coherent-arrow fiber; A2.6's counterexample remains applicable.

## Literature check / failed overreach

Johnstone, Affine categories and naturally Malcev categories, JPAA61(3) (1989), 251–256, DOI10.1016/0022-4049(89)90075-3, search-accessible primary abstract states that natural Malcev structure implies additive pointed objects but does not imply an affine slice presentation. Publisher opening returned403; full text not obtained. Bourn–Rodelo, Cohomology without projectives, primary Numdam PDF https://www.numdam.org/article/CTGDC_2007__48_2_104_0.pdf opened at section1.1, pp106–107, gives the natural-operation and pointed-additivity facts. Bourn, Abelian groupoids and non pointed additive categories, https://www-lmpa.univ-littoral.fr/publications/articles/lmpa332.pdf opened; its introduction emphasizes distinctions among naturally Malcev, protomodular, and essentially affine categories. No affine conclusion is imported from these weaker notions. The full cartesian tree comparison is stronger than existence of its induced cooperation and may be needed to close the gate.
