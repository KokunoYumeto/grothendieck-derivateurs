# Part A work record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claim.

## Current mathematical outcome

All requested Part A conclusions have proofs in the three source fragments below. The original main tower proof is independent of the later general Kan-complex extension. Root independently audited A.3–A.9 and the Lead 6 fold argument and found no gap. Root subsequently read A.13–A.14 in full and confirmed the horn-filler, semilinear-stabilizer, and directed-component arguments.

- `sections/A.tex`, claims A.1–A.12: Lead 1; explicit cocycle categories separating every Q_n from Q_(n+1), n>=2; consequences for total W_n categories and sieve composition; Lead 6 for every fundamental localizer, with no accessibility assumption; adjacent-interval localizer criterion and explicit rational/torsion intermediates.
- `sections/A_general_kan.tex`, claims A.13–A.14: realization of every connected homotopy type by a category whose arbitrary action components are contractible or connected covers; an exact classification of all localizers producing a condition strictly between adjacent Q levels, using ordinary covers and suspension-null spaces, with no categorical-action quantifier. The interval group criterion becomes necessary and sufficient for arbitrary small groups.
- `sections/A_Kstar.tex`, claim A.15: the explicitly requested old K* cone witness of A.2 and Lead 1(d), including the deterministic stage prescription and an audit of the exact R14 steps used.

## Main construction and all-action proof

For n>=2 and countable abelian Lambda, let A_n(Lambda) have objects finite nonempty ordered sets with an n-cocycle on the full simplex, and increasing injections preserving the cocycle. It is Delta_inj/K(Lambda,n), including degenerate simplices. The normalized Moore complex is Lambda[n], and the overcomma of Delta_inj/K -> Delta/K contracts by prepending a vertex labelled zero. Thus the base is K(Lambda,n).

Nonempty-base amalgamation is genuinely functorial. Anchor at p=min(P). The primitive s_p c is natural under maps fixing p. On X amalg_P Z use the primitive from each side and zero on genuinely mixed tuples, then take its coboundary. In each P-gap put X-side before Z-side. The resulting functor gives id -> T <- const_Z and contracts every nonempty cosieve in P/A.

The Fraisse limit has Fix(G_B)=B and the algebraic subgroup identity <G_B,G_C>=G_(B intersection C), not just a density assertion. The finite coset-graph proof uses three prescribed simplices whose union has nerve contractible or S^1. Degree n>=2 cocycles extend across that union. Finite interpolation of ordered coordinates supplies intermediate B-copies with overlapping neighboring gaps. The prescribed existing B0 union B1 is treated as one full simplex, even when B0 and B1 overlap beyond D. Minimal finite supports and finite-order rigidity then classify every open subgroup as a pointwise stabilizer, including all imaginary stabilizers.

For arbitrary set actions, first quotient pairs eventually identified by an outgoing arrow. Both the quotient comparison and saturation into fixed-point actions T_S(B)=S^(G_B) are homotopy final; every relevant comma is a nonempty cosieve in a nonempty-base slice. All comparisons are over A. Orbits with nonempty finite support give representables and contractible element categories. Empty support gives the constant singleton and A itself. This controls arbitrary infinite actions with noninjective transition maps.

Therefore A_n(F_2) lies in Q_n minus Q_(n+1), and H_n of its base is F_2. A named integral cycle is xi_n=Sd_#(t-0), the signed face-flag sum of the nonzero and zero n-simplices. Proper faces cancel. The last-vertex F_2 cocycle evaluates one, since only the increasing permutation has strictly increasing successive maxima. Thus the cycle is nonzero and Hurewicz identifies its order as two.

## Lead 1 and consequences

Composing discrete opfibrations gives action inheritance. Every action component of an initial cone E^triangleleft consists of an action component D of E with cones attached along section copies of E. Mayer–Vietoris and van Kampen prove the required connectivity. Thus E in Q_n implies its initial cone is W_n-total.

Cosieve closure, vanishing H_n on every Q_n category, equality Q_n=Q_(n+1), and composition of totally W_n-dwyerienne sieves are equivalent. The lower-copy construction gives explicit failing pairs of sieves once a cosieve witness is given. Using A_n(F_2), every one of these proposed finite-level closure/composition statements is false. All inclusions in T_1 > Q_2 > T_2 > Q_3 > T_3 > ... are strict, with the explicit base/cone witnesses; the intersection is the total class.

## Lead 6: completed arbitrary-localizer proof

The category-valued homotopy-colimit lemma is proved directly from relative Theorem A. For covariant F, (int F)/i -> F(i) has an adjoint section; objectwise W-equivalences therefore induce W-equivalences of Grothendieck constructions. Opposite invariance gives the fibred version. Simplex-category comparisons transfer this to specified homotopy pushouts, without accessible localization.

Necessity uses the collage A_D, whose nerve is the homotopy pushout BA <- BD -> *. The inclusion A->A_D is final. Collapsing BA gives Sigma BD in W.

For sufficiency, the fibred Grothendieck construction of b\\A is weakly equivalent to A **over B up to the stated natural transformation**, so the suspension projection gives the specified fold BB union^h_BA BB -> BB in W. The map of spans goes from BB <- * -> BB into BB <- BA -> BB, using a section *->BA of the W-equivalence BA->*. This direction preserves the original Bf. Hence the wedge fold is W. Both wedge sections are W, and the map killing one summand and fixing the other yields a constant self-map of BB in W. The map BB->* is a retract of this constant map. This proves Lead 6 for every W>=W_infty.

## General Kan realization and unrestricted A.4

For a connected Kan K, A(K)=Delta_inj/K has a functorial nonempty-base amalgam after fixing one filler for each horn of K. For a mixed tuple T not containing anchor p, fill the horn on p union T missing T; the p-containing proper faces have already been defined. This defines both p union T and T and is natural under embeddings because the same horn data invoke the same fixed filler.

A nullhomotopic map from a finite subcomplex L of a simplex extends literally: Map(simplex,K)->Map(L,K) is a Kan fibration, so its image is a union of components and contains the constant maps. This handles the circle-nerve step for simply connected K. The previous finite-support and arbitrary-action proof then works for every countable simply connected K.

For countable connected K use its universal cover Ktilde and the semilinear automorphism group Ghat of the rich limit. The exact sequence 1->G->Ghat->pi_1 K->1 has discrete quotient. For open U, U intersection G=G_F. If F is nonempty, U preserves F; linear-order rigidity and free deck action on vertex labels force U=G_F. Empty F gives inverse images of subgroups of pi_1 K. Nonempty supports yield representables; empty supports yield covering actions. The regular covering action is explicitly equivalent to A(Ktilde), identifying monodromy.

For arbitrary small K, use its filtered union of countable connected Kan subcomplexes. For an arbitrary action fix a base object and the component D_i containing it at each stage. Their union is the global component D even when other components merge. Projection on pi_1 remains injective because any nullhomotopy enters one later stage. If D has any nonzero homotopy class, choose a representative at a stage; at every later stage it survives, so those stages must be of covering type. Their higher homotopy isomorphisms pass to the union. Thus D is weakly equivalent over K to a connected cover, or is weakly contractible.

Define H_W to be connected homotopy types X such that every connected cover X_H has W-aspherical suspension. The categorical suspension condition lies strictly between Q_(n+1) and Q_n iff {n-connected types} is a proper subclass of H_W and H_W is a proper subclass of {(n-1)-connected types}. This is an exact criterion for arbitrary W stated solely in ordinary homotopy theory. For W_(n+1) subset W subset W_n, it reduces to: the abelian groups Lambda with K(Lambda,n+1) W-null contain a nonzero group and omit a nonzero group. The rational truncated-homology intersection supplies a strict example at every n.

## Earlier K* witness and audit

Read the exact attachment kernel C.10, point birth-cover routing/equalizer descent C.19–C.24, simultaneous component induction C.25–C.28, the review's expanded C.27 routing step, and the selected C.37 construction. Also read the strict necklace-colimit and long-necklace orderability proofs C.32–C.34 to specify the deterministic object. The proof source explicitly distinguishes actual-arrow factorizations from component-map equalities. The preserved first-stage class is kappa_+ - kappa_-, of augmentation zero. Filtered nerve-chain unions justify survival. E is connected because it is a quotient-representable action category; quasi-filteredness plus action inheritance gives E in Q_2. The initial cone is W_2-total and its old full cosieve E has nonzero H_2.

## Programs and independent checks

`code/A_cocycle_checks.py` and `code/outputs/A_cocycle_checks.out` contain all bounded computations used in this branch:

- normalized Moore dimensions for r=2,...,6 in several degrees over F_2,F_3;
- 162 cohomology checks of three-piece extension domains;
- 270 anchored-amalgam restriction, naturality, and cocycle checks over F_2,F_3,F_5;
- integer boundaries and mod-two evaluations of xi_2,...,xi_6;
- the three-object finite-poset witness for T_1 minus Q_2.

The output expressly says these are checks of formulas, not a finite test for the universal all-action theorem.

`notes/D_exact_audit.md` contains an independent audit of the sibling's theorem that every exact index passes every free-monoid diagram. The constant object set of its translation categories is the essential feature; the groupoid proof eliminates transport arrows by a reversible presentation argument. No gap found.

## Routes tried and not used as proof

- General abstract-elementary-class realization literature gives arbitrary base homotopy types but does not supply the required all-action conclusion. It motivated the construction, but is not substituted for the proof.
- Joins and ordinary products do not raise the minimum all-action connectivity because the old factors remain action components/cosieves. No proof relies on these routes.
- A direct positive monoid lift of the C_delta free-group diagram works for one hyperedge by introducing w_e, but overlapping edges give competing positive factorizations. No claim about a free-monoid diagram over C_delta is made in this branch. The sibling's separate free-group obstruction satisfies the stated free-group alternative of D.4; the first-case free-monoid question remains with that branch/root.
