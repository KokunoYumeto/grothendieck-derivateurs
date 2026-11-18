# Parts C and D: proof and verification record

Prepared by the targets/ind-representability agent for the S2COUNT return.
The work is AI-produced by GPT-6 Astra (OpenAI); no priority is claimed.
All proofs intended for the deliverable are in `sections/CD_agent.tex`.
Root owns the main paper, final register, bibliography merge, and packaging.

## Completed requested items

| Item | Result | Main labels |
|---|---|---|
| C1: named targets | Countable for S1, K(Z,n), K(Z/p,n), and BG for finite or countable G; finite values for K(Z/p,n) and finite G. Every Sn with n≥2 and CP2 has continuum many classes on the six-arrow witness. | `CD:targetlist` |
| C1: general finite CW Y | Exact criterion: each component is a Postnikov piece, meaning only finitely many higher homotopy groups are nonzero. The six-arrow wedge detects every failure of this criterion. No unsupported reduction to asphericity with arbitrary π1 is made. | `CD:wedgecriterion`, `CD:countabletargets` |
| C2: single countable locally finite representative | Exact characterization for arbitrary homotopy types, including targets with uncountable fundamental group: countably many components, componentwise finite Postnikov height, and countable free mapping-class sets from finite connected CW complexes. Equivalent to a finite-CW-test equivalence from a countable componentwise Postnikov CW complex. | `CD:alltargets`, `CD:sequential` |
| C2: finite representative | Exactly finite disjoint unions of BG for finite groups G. Any finite representing category is isomorphic in Cat_hot to a finite groupoid. A finite CW target qualifies exactly when its components are contractible. | `CD:finiterepresentative` |
| C3 | For every finite C with uncountable [BC,S2], there is an actual sequence of finite categories J_n with B colim J_n ≃ S2 for which the comparison fails injectivity. More generally this works whenever H_*(BC;Z) is unbounded. | `CD:boundedhomology`, `CD:spread`, `CD:comparisonfailure` |
| C3: direction of failure | If the colimit has finite CW type the comparison is always surjective, for every source. If all stages also have finite CW type it is bijective for every source. Thus finite poset stages cannot realize the sphere-colimit failure. | `CD:surjectivity` |
| D | Exact corrections at all requested manuscript pages, including an explicit countable non-equivalence invisible to every finite-category set-valued test. | `CD:manuscript`, `CD:largegroups` |

## Critical distinctions preserved in the proofs

1. A finite category need not have finite CW classifying space. Its nerve has finitely many cells in each degree. For a target that is an n-type, restriction to the (n+1)-skeleton of any CW source gives a bijection of free homotopy classes. This finite skeleton is the exact comparison that transfers finite-CW information to finite-category tests; there is no unrestricted inference between those test domains.
2. Infinite products of higher homotopy groups need not have countable orbit classes merely from a countable-looking presentation. The wedge proof uses the support of zero/nonzero coordinates, which is invariant under every π1 action. It supplies continuum many free classes even for uncountable π1.
3. An arbitrary target with countable finite-test values need not have countable π1. The inclusion A_fin(N)→A_fin(Λ) for any infinite Λ is invisible on all finite-category tests by finite support and parity correction. The shift A_fin(N)→A_fin(N) yields the countable nonconservative map used in Part D.
4. The finite representative theorem first obtains an actual weak equivalence BK→Y. This uses finite-poset simplicial approximation and a generating-tuple argument proving that a finite-CW-test equivalence with finitely generated source π1 is a weak equivalence. Without the finite-generation condition that argument is false, as the preceding shift example shows.
5. The remaining finite-representative obstruction is quantitative: for E_r=(C_p)^r and top nonzero higher group A=π_NY, the constant-fibre components in Map(BE_r,Y) give at least p^{binom(r,N)} classes before quotienting by [BE_r,ΩP_{N−1}Y]. The denominator has logarithmic growth of degree at most max(1,N−2), while actual functors BE_r→K number at most |Ob K|·|Mor K|^r. This excludes every N≥2.
6. The S2 countability theorem under bounded integral homology does not confuse an injection of Hopf lift classes with a bound on all classes. Each c1 fibre of [X,S2] is a transitive [X,SU2] orbit, proved by an explicit unitary line-bundle isomorphism and its determinant-one extension.

## Verification of the supplied results actually used

### R1, CATHOT D.2–D.6 and E.8

Read the supplied `CATHOT_D.tex` and `CATHOT_E.tex` at the specified claims.

- D.3: Checked its category of elements, object, coproduct, tagged two-arrow Grothendieck construction, equalization natural transformations, homotopy extension over its realized double mapping cylinder, and the exact density map. The finite span comparison has a direct proof in the C3 construction by categorical mapping cylinders and cofibration gluing.
- D.4: Checked countability of the element category, the cofinal-sequence construction with a diagonal enumeration of comma requirements, and strictification of adjacent transition classes. Functors, transformations, equalities and finite zigzags into the colimit all lift to stages. Crucially, endpoint equalities of a finite generating family must first be made true at a stage; only then do all composable words lift and prove local finiteness.
- D.5: The finite degree-two normalized cochain argument is correct. It works for every finite coefficient group in every degree and for Z with countability in place of finiteness.
- D.2: Its S2 obstruction from a finite sphere poset and [S2,S2]=Z is immediate and correct. The conclusion for K(Z/2,2) is independently confirmed by the complete finite-representative theorem. Its special case can also be proved directly from the lower bound |H2((C2)^r;F2)|≥2^{binom(r,2)} against at most o·m^r functors. Thus the original alternating-group multiplier calculation is not an input to any result here; its extra numerical equality is not being certified from memory.
- D.6 is settled negatively by the explicit six-arrow wedge, not retained as an open assertion.
- E.8: Checked the actual categorical colimit comparison by proving each comma category over a colimit object is filtered. Checked objectwise invariance and compact-source mapping comparison using the finite-data properties of nerve and Ex∞. The exact finite posets c Sd² sk_r N(BC2) were checked against Thomason's Lemma 5.6 and Fritsch–Latch's original twice-subdivision comparison, including the latter's proof. The identity BC2 cannot factor through any stage by unbounded mod-2 cohomology. See `CD:E8`.

### R4, OWN_RESULTS §§1–2

Read the supplied proof, including the K-theory filtration calculations, not just Theorem 2.2.

- Relative products give F^aF^b⊂F^{a+b}. The skeletal pair/triple exact sequences identify the first cellular coboundary; H^q=0 therefore gives F^q=F^{q+1}. This is valid for infinite CW complexes and asserts vanishing only on all skeleta, not vanishing of a possible phantom K-class.
- The regular-representation argument uses precisely Atiyah's completed skeletal group and kernel calculation. The original Propositions 6.10–6.11 and Theorem 7.2 have the stated meaning. The cyclic proof of Proposition 8.1 was also read and supplies the portion needed for the p-local refinement. Odd lens skeleta have reduced K0 finite p-primary, so localization is injective there.
- The universal group of a finite monoid is finite and its map is onto, by eventual periodic powers. For an idempotent e of the minimal ideal, eMe is a group and surjects onto U(M). The map B(eMe)→BM is justified via idempotent completion; the comma category at e contracts by the transformation a:a→e. This directly checks the categorical map, not only the abstract group quotient.
- Bounded homology plus finite generation gives bounded cohomology. The regular-representation result makes U(M)=1. Hatcher 4C.1 gives finite CW type. The mod-p version follows by localization and the same argument. Corollaries 2.3 and 2.4 follow as written.
- OWN_RESULTS 2.5 additionally depends on the separate recent finite-monoid realization theorem. That additional theorem is not needed in these sections and is not included in this audit.
- The finitely dominated assertion is proved directly: a homotopy retraction onto X makes [X,S2] inject into the countable [A,S2] for finite A.
- A stronger theorem proved here applies to every finite category: bounded integral homology implies countability into S2 and S3. Its proof uses the finite CW model of the suspension and the SU2 action on each c1 fibre. This supplies the hypothesis needed in C3 without relying on one-object semigroup structure.

### R5, INDLOCAL B.7–B.9 and its A.1–A.3 inputs

Read the original `INDLOCAL_return/sections/B.tex` and `A.tex` at all these claims.

- B.9: The finite skeleton of types of at most m arrows has finitely many morphisms. The colimit presheaf has finite values and finite filtered element category. A cocone splits it as an idempotent representable; fully faithful Ind inclusion is checked by the limit–colimit Hom formula. An idempotent homotopy class has a strictly idempotent representative power because the monoid of endofunctors is finite. Its fixed objects and arrows split it and preserve the bound m. See `CD:uniformfinite`.
- B.8: The fence giving a finite zigzag is kept as a genuine finite free indexing category. Its two end arrows go to the B vertex and carry u,v. Collapsing the fence gives a relative weak equivalence with the tagged double cylinder, and transfers the extension through an invariant presheaf. Conversely the two finite conditions give exactly the three filteredness conditions for the element category. For uncountable κ, each individual replacement has size max(ℵ0,λ)<κ; no regularity assumption on κ is introduced.
- A.1: Independently checked the infinite-order words w and wh used in the simple envelope (cyclic lengths 8 and 8 or 6), all HNN embeddings, and normal generation. In the acyclic envelope the field Künneth diagonal has only its two axis terms after killing lower homology, and conjugacy gives a=2a. Iteration and field universal coefficients yield integral acyclicity. Alternating cofinal simple and acyclic stages gives both properties without changing the cardinal.
- A.2: The pushout Y∪_X^hW has the same π1 as Y if the map kills ker π1t; local Mayer–Vietoris gives universal-cover homology equivalence and Whitehead gives the extension. The fold W∪_X^hW→W proves injectivity. This confirms the exact mapping-class statement used in B.7. The original full mapping-space enhancement is consistent: every fibre has equivalence diagonal and is empty or contractible.
- A.3: Checked the compatible simplicial homological-cone construction, the asphericity induction, the stronger subcomplex π1-injectivity induction through the stated intermediate space V, the relative local-homology comparison, the quotient by the cone groups in dimensions 2 and ≥3, perfectness and normal generation of the kernel, and the cardinal bound. No two-dimensional resolution theorem is used in this construction.
- B.7: The bounded localization equivalence preserves all maps and homotopies because Kan replacement stays within the same infinite cardinal. The descent/Yoneda comparison needs and has all K_i in that bounded category. Actions of the resolution group on objects of K_j factor through the π1 quotient since each automorphism group has size at most μ; natural transformations factor too. The acyclic mapping comparison gives bijectivity on each unit. The ind-Hom limit yields the inverse to the canonical global unit; orthogonality of the target ind-groupoid proves the other inverse identity. The converse uses the small element category on all categories of size≤μ and the finite sphere-poset test for K(Z/2,2). The equality κ=μ+ is included. Full proof: `CD:acycliccomparison` and `CD:boundedtests`.

## Source checks and pagination

The seven entries in `CD_references.bib` are marked verified and record precise theorem locations. They must be merged into the root bibliography.

- Serre 1953 here means **Cohomologie modulo 2 des complexes d'Eilenberg–MacLane**, Commentarii Math. Helv. 27, 198–232, not the different Annals paper of the same year. Theorem 10 is on printed p.217, proof pp.217–219, sphere corollary p.219. An earlier working citation 216–218 was corrected after noticing that PDF text extraction attached the preceding page footer to the next page's text.
- The mod-2 Serre theorem suffices for spheres and CP2. The simply connected finite-Postnikov remark uses Casacuberta's Theorem 1.1 and its proof, avoiding an unsupported all-primes extension of the particular mod-2 theorem being cited.
- Hatcher Proposition 4C.1 was checked directly in the supplied original, pp.429–430: one generator cell for each cyclic homology summand, with a relator cell in the next degree for each finite cyclic summand. This is stronger and more precise than merely citing a finite-type theorem.
- Kan 1957 was opened at the original proofs of the Ex∞ and subdivision results. They justify finite-domain maps/homotopies factoring at a finite Ex stage, and last-vertex maps of finite posets.
- Casacuberta's introduction distinguishes finite-dimensional rational Postnikov examples from the stronger finite-complex question with arbitrary fundamental group. No claim that this latter question is presently open is used as an answer to C1; our exact support criterion is proved directly.
- The recent arXiv item 2611.09718 on finite acyclic categorical approximations surfaced during searching. No priority is claimed for the level-spreading P_n construction; no theorem from that item is an input here.

## Finite computation and reproducibility

Run `python3 code/CD_finite_telescope.py` from the package root. The output is in `code/CD_finite_telescope.out`.

For n=0,...,5 the script constructs P_n(M), its mapping-cone category K_n, and the sphere-wedged category J_n, for the six-element M and the five-element sphere monoid Q. It exhaustively verifies all identities and composable associativity triples, every transition functor, all comparison functors, and the retractions. J_n has 32,46,66,92,124,162 arrows. It is an independent check of the actual finite categorical data; topology in all degrees is supplied by the proof, not extrapolated from the output.

## Independent check of Part A's sphere topology

Read the current `A_agent.tex`, especially `lem:Mr-spheres` and the proof of `thm:Mr-wedge`.
The bigon circle joined with n−1 zero-spheres is S^n with 2^n top simplices. Colors 0 and 1 flip bit 1; color i≥2 flips bit i. These exactly match the bar-face deletions and adjacent products, and all selected adjacent products equal e. Facet agreement therefore gives all lower face identifications. The join fundamental chain has coefficients (−1)^{sum bits}. Wedge continuity uses the CW weak topology. Together with the integral primitive pairing and the proved homology ranks, the map is a homology equivalence between simply connected CW spaces. No sphere-topology gap was found.

## Packaging note

`notes/CD_Hatcher_text.txt` is only a duplicate text extraction of an attached source. It should be omitted from the final ZIP and checkpoints under the user's instruction to leave supplied scans and sources out; its source is the attached `Hatcher_AT.pdf`. All original proof work is retained in this note, the TeX section, bibliography notes, code, and outputs.

## Additional Part E work after the C--D merge

The new proof in `sections/CD_E_normal_subgroup.tex` was independently audited
by the root and the group-resolutions agent and is being incorporated as
Statement E.16. If G has an actual two-dimensional classifying space and
N is a perfect normal subgroup with H2(N;Z)=Z^r, where 0<r<infinity, then
G/N is finite of order dividing r+1, and acts faithfully on H2(N;Z).
The proof handles arbitrary ranks of the cellular free modules explicitly.
At r=0 it proves only cd_Z(G/N)<=2, with no unsupported geometric-dimension
conclusion. This is a proved restriction; E2--E4 are not settled by it.

For an actual two-dimensional subcomplex homology core Y in X, with
H=pi1(Y), N the normal closure of H in G=pi1(X), and Q=G/N, the N-cover
contains disjoint lifts Y times Q. Their second homology injects into
H2(N) because there are no three-boundaries. Consequently H2(N) contains
Z[Q] tensor H2(Y) and its rank is at least |Q| times rank H2(Y). The
actual-subcomplex hypothesis is essential; arbitrary subgroup maps do
not have this homology-injectivity property.

`notes/CD_E_FDOS_one_pass.md` records a narrowly scoped source audit:
the literal one-pass group in Farjoun--Orr--Shelah Section 3.1 cannot be
used as an existence-only Gamma closure. Its main unique-localization
conclusion can be repaired after the uniqueness quotient. The independent
120-element word-map check is in `code/CD_E_FDOS_one_pass_check.py` and
its output. The earlier binary icosahedral asphericity counterexample is
also checked in `code/CD_E_identity_matrix_counterexample.py`.

The locally free route remains incomplete. The author-hosted primary
addenda at https://mat.uab.cat/~dicks/DKLT.html explicitly distinguish
arbitrary locally free groups from groups with a proved two-dimensional
classifying model. In Berrick--Casacuberta's original
https://www.ub.edu/topologia/casacuberta/articles/berc2.pdf, Lemma 4.1
supplies countable locally free perfect groups; the following sequential
telescope argument applies to those countable groups. Their universal
group is a free product of such groups and consequently does have an
actual two-dimensional wedge model. Proposition 5.2's broader use of
two-dimensionality gives no additional arbitrary-cardinality argument.
Every nontrivial word in that universal free product survives a retraction
to finitely many countable factors, so it cannot itself have the required
absence of countable images. Nishinaka's original five-page proof
(arXiv:1601.00295) was read in full; it constructs large free subgroups,
and supplies neither a quotient nor a retraction theorem. The harmonic
archipelago is also unsuitable as stated, since it has Q as a quotient
(Conner--Hojka--Meilstrup, arXiv:1410.8389); its wild two-dimensional
topological realization is not an actual CW classifying model.
