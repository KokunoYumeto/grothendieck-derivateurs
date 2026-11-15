# Hunches (Dérivateurs expert, Claude Fable 5.2, effort max)

A hunch is something I suspect and cannot prove. Each entry: the statement, where it comes from in Grothendieck's
text and in the returns, my reasons, what would decide it, and the draft prompt folder under `PRO_PROMPTS\`.

## H1. Total asphericity is exactness of abelian colimits

**Statement.** For a small non-empty connected category `A` the following are equivalent:
(i) `A` is totally `W∞`-aspherical (XII ms. 88–89, Définition 1: every category receiving a final functor from `A`
is aspherical); (ii) `colim_A: Ab^A → Ab` is exact, i.e. (Isbell–Mitchell 1973, Th. 1) the affinization `Aff_Z(A)`
is filtered. Known: (ii) ⇒ (i) (TOTASPH C.6, checked). Open: (i) ⇒ (ii) (TOTASPH D.7).

**Where it bears on Grothendieck.** II ms. 36–36ter: he suspects "totalement `W∞`-asphérique ⟹ filtrante". That
is false (`Δ_inj`, TOTASPH C.10 = the Isbell–Mitchell example). H1 would be the correct form of his conjecture:
total asphericity = filteredness *after affinization*.

**Reasons.**
1. The three classes: `Aff_Z`-filtered ⊂ total ⊂ quasi-filtered (Adámek–Reiterman: spans complete and every
   parallel pair has an affine equalizer; ⇔ fixed-point property for connected set-valued functors). With a weakly
   terminal object all three equal "filtered".
2. Totality means `H_j(El_A(H)) = 0` for all `j ≥ 1` and all `H: A → Set` (TOTASPH C.5). Quasi-filteredness is
   exactly the part `j = 1` (my computation: `H_1(El_A(H))` = cycles of a presentation graph modulo augmentations of
   syzygies, and span completion plus pairwise affine equalizers realize every simple cycle). The conditions for
   `j ≥ 2` look like coherence conditions between different affine equalizers: for three parallel arrows
   `a_0, a_1, a_2` with affine equalizers `ρ_1, ρ_2, ρ_3` of the three pairs, the syzygy
   `κ = (ρ_1 − ρ_3, ρ_3 − ρ_2)` has augmentation 0 and its class in `colim K` is an element of
   `H_2(El_A(h_p/(a_0 ∼ a_1 ∼ a_2)))`: a 2-sphere made of the three "discs".
3. Free constructions do not give totality: adjoining a new maximal object `Z` changes `B El` by a cone on
   `B(old ↓ Z)`, and for a freely adjoined quasi-filter this is a circle that is already null-homotopic, so a
   2-sphere appears. So the Adámek–Koubek–Reiterman category `K*` (quasi-filtered, not `Aff`-filtered) is very
   probably not total, and no example separating total from `Aff`-filtered is in sight. Every known proof of
   totality goes through `Aff`-filteredness.
4. What I could reduce it to: a simultaneous affine equalizer of `a_0, a_1, a_2` exists iff
   `aug(K_1 ∩ K_2) = Z` (`K_i = {t ∈ Z[A(q, −)] : t(a_i − a_0) = 0}`), and `Z/aug(K_1 ∩ K_2)` is a quotient of
   `Tor_1^{ZA}(ΔZ, P_q/(K_1 + K_2))`. Totality gives vanishing of `Tor` only on permutation modules `Z[H]`.

**Against.** The implication "pairs ⇒ triples" has no formal reason; `Δ_inj` satisfies both for the special reason
that one polynomial identity equalizes all cofaces at once. A counterexample would have to be a category with
infinitely many objects, no weakly terminal object, not a preorder.

**What would decide it.** Either a proof that `H_2(El_A(H)) = 0` for the functors
`H = h_p/(ca_0 ∼ ca_1 ∼ ca_2)` and their iterates forces `aug(K_1 ∩ K_2) = Z`; or an explicit `A` (for instance a
modification of `Δ_inj`, hom-sets = monomials with other composition rules, or a quotient of `K*`) with all
`El_A(H)` contractible and a triple without simultaneous affine equalizer. A first computation: `H_2` of
`El(h_V/(cv_1 ∼ cv_2))` at the second stage `K_2` of the Adámek–Koubek–Reiterman construction.

Draft prompt: `PRO_PROMPTS\TOTAL_EXACT\PROMPT.md` (written 12 Nov).

## H2. Total asphericity for an intermediate localizer is governed by its "connectivity profile"

**Statement.** For a fundamental localizer `W` with `W∞ ⊂ W`, `T_W(A)` holds iff `A` is `W`-aspherical and every
component of every `El_A(H)` is "one step less `W`-aspherical", in the sense that its suspension is
`W`-aspherical. (For `W∞`, `W_Z`, `W_R`, `W_n` this is TOTASPH C.5, D.2, D.12; for `W ⊃ W_1` it degenerates to D.19.)
The return proves the cases one by one; a uniform statement in terms of the class `{X : ΣX is W-aspherical}` is
not in the return. Status: to be examined when Part F (the dichotomy on `W ⊃ W_1`) has been read.

## H3. Integral totality of a presheaf forces simple connectivity (TOTASPH F.27)

**Statement.** Let `H` be a presheaf on a small category `U` such that for every functor `p: U → U'` the category
of elements `U'/p_!H` is non-empty, connected and integrally acyclic (`H` totally `W_Z`-aspherical). Then `U/H`
is simply connected, hence `H` is totally `W∞`-aspherical. Equivalent forms (TOTASPH F.26, checked): every
`W∞`-dwyérienne sieve is discretely flat (Hackney–Ozornova–Riehl–Rovelli); `W∞`-dwyérienne sieves compose; a
one-point attachment that is a couniversal `W∞`-equivalence is `W∞`-dwyérienne (the exact form of Grothendieck's
Question (a), XII ms. 111, for `T = e`).

**Reasons for.** For categories (`H` terminal) it is true by the covering trick (C.4). For groups `U = G` it is
true (all subgroups of a stabilizer must be acyclic). The restricted actions `L∘π`, `L: U → Set`, are numerous:
for `U = Δ_inj` and `H` an acyclic semi-simplicial set with perfect `π_1`, the action "vertices, all identified
from dimension 2 on" already produces `H_1 = Z^{28}` (my computation). `π_1(U/H) → π_1(U)` is always trivial
(F.20), so an obstruction is a perfect group invisible from `U`.

**Reasons against.** The covering trick needs actions on `U/H` that do not factor through `U`; nothing forces
them to exist. A counterexample would be a discrete fibration `E → U` with `E` acyclic, `π_1(E)` perfect, and
`H ⊗^h_U L` homology-discrete for every `L: U → Set`.

**What would decide it.** Either a construction, for a given total-`W_Z` presheaf, of an enlargement `p: U → U'`
and `L'` on `U'` whose restricted action on `U'/p_!H` contains a non-trivial cyclic covering; or a counterexample
found by search among small `U` (monoids with a few elements, small posets with several arrows) with `H` such that
`U/H` is the category of simplices of an acyclic complex.

Draft prompt: `PRO_PROMPTS\PRESHEAF_TOTALITY\PROMPT.md` (written 12 Nov).


## H4. The reversible localizers are the desuspension-closed null classes (partly a result now)

**Origin.** POLES F.14 (1): is every accessible fundamental localizer with Loc (6 b) of the form
`R(L) = {g : Σ^∞ C(g) ∈ L}`? XII ms. 75–78, 265–275; XVI §3.

**What is proved** (`RESULT_REVERSIBLE_NOT_STABLE.md`): no, if accessibility is dropped: `W_S` (null class of the
2-local spheres). Also, for every reversible `W` with aspherical class `A`: `A` is closed under contractible
homotopy colimits, two out of three in cofibre sequences, (de)suspension, `− ∧ Y`, extended powers `D_j`,
`Ω^n Σ^n` and `Q` (May–Milgram filtration with quotients `D_{n,j}`; conversely `Σ^n Y` is a retract of
`Σ^n Ω^n Σ^n Y`, so `Y ∈ A ⇔ Ω^n Σ^n Y ∈ A`), and under "`F ∈ A`, `B` connected ⇒ (`E ∈ A ⇔ B ∈ A`)" for fibre
sequences; if `K(T, 1) ∈ A` then all `K(T, n) ∈ A` and all finite Postnikov pieces with such groups. On finite
complexes `A` is a thick subcategory of finite spectra (stable maps and idempotents of finite complexes are
realized after finitely many suspensions).

**Hunches that remain.**
(a) The accessible form is also false: `𝔑^κ` of the note is accessible and reversible. Reason: Löwenheim–Skolem
arguments of this kind work for nullity classes; the only new step, desuspension, passes by the alternating
chain. Against: none known.
(b) The smallest reversible localizer containing `RP^∞ → e` is strictly smaller than `W_S` and has no simple
description; its local objects should be the `HZ`-local spaces `Z` that admit "EHP resolutions to all orders"
by `RP^∞`-null spaces.
(c) **Classification conjecture.** The accessible reversible localizers are exactly the `W_𝒵` for sets `𝒵` of
pointed spaces closed under the following: for every `Z ∈ 𝒵` the null class of `𝒵` is contained in the null
class of some family of loop spaces `ΩZ'`, `Z' ∈ 𝒵`, through which `Z` is resolved. I cannot make this precise.
(d) Every reversible localizer satisfies: `T(W)` restricted to finite spectra is a thick subcategory, hence
(Hopkins–Smith) determined by a type function `p ↦ n_p ∈ {0, 1, …, ∞}`; **hunch: only `n_p ∈ {1, ∞}` (and the
rational case) can occur for `W ≠ Fl(Cat)`**, because a finite complex of type `≥ 2` in `A` forces, by smashing
and cofibre sequences, a Moore space… (to be examined: is a type-2 complex `V(1)`-like in `A` possible without
`M(Z/p)` in `A`? For `W_E` with `E = K(1)`-type theories it is: `K(1)_*`-acyclic finite complexes are those of
type `≥ 2`. So the hunch as stated is false for `W_{K(1)}`; the right statement is that every Hopkins–Smith
class occurs.) Kept as a record of a wrong first guess.

Draft prompt: `PRO_PROMPTS\REVERSIBLE_LOCALIZERS\PROMPT.md`.

## H5. Simple homotopy types in Cat need 2-categorical data, not a localizer

**Origin.** XVI 6.4 b)–6.5 (ms. 87–96): Grothendieck hopes for a localizer `W̃∞ ⊊ W∞` whose `Hot` carries
Whitehead torsion; then retracts; then observes (ms. 95) that `sd(I)` and `I` are not homotopic in Cat for the
hexagon. POLES D.4–D.6: no localizer can do it.

**Hunch.** The relation "connected by a zigzag of functors having adjoints" (or: of Dwyer immersions that are
adjunction-retracts, the categorical elementary expansions) on finite posets is exactly simple homotopy
equivalence of the nerves, and Whitehead torsion is an invariant of the homotopy type in `Cat hot` (functors
modulo zigzags of natural transformations) restricted to finite posets. Reasons: a functor with an adjoint
between finite posets induces a collapse of nerves (a closure operator on a finite poset gives a simplicial
collapse: standard in poset topology, "dismantlability"); `sd(I) → I` is a simple homotopy equivalence although
it has no categorical homotopy inverse (D.6), so the right relation is generated by adjoint pairs, not by
`Cat hot`-isomorphisms. This would give Grothendieck's "opérations élémentaires à la Whitehead dans Cat"
(ms. 88–89) a precise form. It touches the envelope finding of the project (categories up to natural
transformation give the 1-types): `Cat hot` is too coarse in one direction and too fine in another.

**What would decide it.** A proof that two finite posets have simple-homotopy-equivalent nerves iff they are
connected by a zigzag of order-preserving maps each having a left or right adjoint; the known results on
"strong homotopy types" of finite spaces (Barmak–Minian) say that adjoint-zigzags give strong collapses, which
are finer than simple homotopy; so the correct generating class has to be larger (e.g. include `sd(I) → I`,
or all Dwyer immersions `U → X` with `U → X` in `W∞` and finite complement). To be worked out.

## H6. `Fib_{W_Z}` is the class of functors with "homologically nilpotent" local systems

**Origin.** POLES C.10 gives only bounds for `Fib_{W_E}`. XVI §4.

**Hunch.** A functor `p: E → B` is in `Fib_{W_Z}` iff (i) `E_b → E/b` and `E/b → E/b'` are integral homology
isomorphisms (it is a homology fibration), and (ii) for every homology isomorphism `u: Y' → Y` over `B`,
`H_*(Y'; u^*ℋ_q) → H_*(Y; ℋ_q)` is an isomorphism for the local systems `ℋ_q = H_q(E/−)`. Condition (ii)
holds when `π_1` acts nilpotently on each `ℋ_q` and fails for the permutation system `Z[t, t^{-1}]` over `S¹`
(trefoil) and for the three-sheeted covering of POLES C.10. Necessity of (i) and sufficiency of (i) + (ii) are
immediate from the spectral sequence of `E ×_B Y → Y`; necessity of (ii) is the question (the spectral sequence
could have cancelling differentials). If true, `Fib_{W_Z}` has an intrinsic description and the failure of
(7 F) is explained: an acyclic total space over `S¹` needs the non-nilpotent system `Z[t, t^{-1}]`.

## H7. Sifted and totally aspherical implies filtered (added 12 Nov, 16:45)

**Origin.** `RESULT_FILTERED_BY_ONE_TYPES.md`: filtered = total + homotopy colimits of `BM(a)`, `M: A → Grp`, are
1-truncated. With abelian `M` only, the same argument gives: exact abelian colimits and sifted.
**Hunch.** A sifted totally `W∞`-aspherical category is filtered; so abelian test diagrams suffice.
**Reasons.** Siftedness gives commutation with finite products of sets, totality gives affine equalizers of
parallel pairs; an affine equalizer `Σ n_i c_i` of `u, v` is a finite pattern of equalities `c_i u = c_j v`,
`c_i u = c_j u`, and connectedness of the categories of cospans should let one merge the `c_i` step by step.
**Against.** I could not carry out the merging; `Δ_inj` is no test (it is not sifted).
**Smallest undecided instance.** A category with finite coproducts and no weakly terminal object.
Prompts: TOTAL_EXACT Part D.2, PRESHEAF_TOTALITY Part F.2.

## H8. `W^lc_D` is proper only when it is a truncation-type localizer (added 12 Nov)

**Origin.** GALOIS B.7, B.14; my criterion (FINDINGS F4-4).
**Hunch.** For `D` the derivator of `E`-local spectra or of `D(k)`: `W^lc_D` has Loc (7 F) iff `W^lc_D = W∞`.
**Reasons.** True for all `D(k)` (B.7) and, granted Bousfield, false-proper for `K(n)`; the localization is
`X ↦ B L_E ΩX`, and `L_E` restricted to connected loop spaces contains a completion (`Z → Z_p` on `π_1`) or a
rationalization whenever it is not the identity, which is never a nullification.
**Smallest undecided instance.** `E = KU`: is the fibre of `ΩS³ → L_{KU} ΩS³` `KU_*`-acyclic?
Prompt: REVERSIBLE_LOCALIZERS Part E.4 (the `KU` case only).

## H9. Accessibility of `W^lc_D` for an arbitrary derivator is not decided by the derivator axioms (added 12 Nov)

**Origin.** GALOIS B.13. **Reasons.** A product of a class of derivators is a derivator with values in `CAT_V`,
and its `W^lc` is the intersection; Casacuberta–Scevenels–Smith tie localization with respect to a proper class
of maps to large cardinals; under Vopěnka the answer is yes (Cisinski 4.2.17). **Against.** The coefficient
theories at hand (`D(k)`, `L_E Sp`) give only a set of localizers (Ohkawa), so no counterexample is in sight.
No prompt yet.

## H10. Positive-degree cohomology of a finite monoid with trivial universal group is nilpotent (added 12 Nov)

**Origin.** The CATHOT expert's results (finite monoids with bounded homology are the finite simply connected
complexes) and its open question whether `K(Z, 2)` is `BM` for a finite `M`.
**Hunch.** If `M` is a finite monoid with `U(M) = 1`, every class of positive degree in `H*(M; F_p)` is
nilpotent; more generally a class is nilpotent iff its restrictions to the subgroups of the groups `eMe` are.
This would exclude `K(Z, 2)` and `K(Z/2, 2)`.
**Reasons.** Quillen's theorem for groups; all computed examples (Theorem C models are finite complexes; in
Sweeney's Example 5.2 the cup products computed by the CATHOT expert vanish).
**Against.** For `U(M) = 1` the maps `BG → BM`, `G ⊂ eMe`, are null on `π_1` but I have no proof that they are
null-homotopic or nilpotent in cohomology when `BM` is infinite-dimensional.
Prompt: FINMON Part A3 (i).

## Status of the earlier hunches after 12 Nov, 16:45

H1 (total = exact): open; now framed by filtered ⊊ `Aff_Z`-filtered ⊂ total (TOTAL_EXACT). H2 (connectivity
profile for intermediate localizers): no prompt of mine; not examined further. H3: PRESHEAF_TOTALITY Part A.
H4: REVERSIBLE_LOCALIZERS Parts B–D. H5 (simple homotopy types in Cat): no prompt of mine. H6: REVERSIBLE_LOCALIZERS
Part E.1–E.2.
