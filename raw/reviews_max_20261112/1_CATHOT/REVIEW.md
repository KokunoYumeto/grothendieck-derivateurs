# REVIEW of the return CATHOT (Les Dérivateurs, package 1 of 7)

Reviewer: Claude Fable 5.2 (Anthropic), effort max, 12 Nov 2026. Return: GPT-6 Astra (OpenAI, effort Pro, ChatGPT
Pro mode), 10 Nov 2026: `CATHOT_paper.tex` with `sections/*.tex`, `CATHOT_results.csv` (90 rows), `CATHOT_report.md`,
`research/`, `code/`. Started from nothing; the earlier review was not opened before this file was complete.
Reading done first: `READING_BASE.md`. The return's code was read, not run; my own checks are in `work/code/`.
Companion files: `G6_VERDICT.md`, `EMAIL_CLAIMS_CHECK.md`, `OWN_RESULTS.md` (my proofs), `HUNCHES.md`, `FINDINGS.md`.

## Summary

- **Verdicts on the 90 items: 84 correct, 0 wrong, 0 gap; 6 left unproved by the return** (its own "Open" items).
  Of those six, **E.17 is settled here: it is true** (`OWN_RESULTS.md`, Theorem 3.2); for G.17 the bound is improved
  (34 ≤ a_pos(RP²) ≤ 49) and facts on K(Z, 2) recorded; for E.6 a case is proved; D.6, E.26, E.27 remain open, with
  a reduction for D.6 and hunches H3, H4, H6.
- I found no false statement and no proof that fails. Recorded flaws are of citation or labelling: D.9 attributes to
  Raptis's "product discussion" a left-Quillen statement that the passage does not contain (it proves the opposite
  kind of statement, non-monoidality); the needed fact is true and immediate. G.15 is labelled "Known" from Sweeney's
  tables; my enumeration of all monoids of order ≤ 6 makes it independent of that source. A.5 repeats one sentence.
- Depth of checking is marked per item: **[V]** verified in full by my own argument or computation; **[O]** the
  structure and the key steps checked, no error found, not every line re-derived; **[C]** rests on a cited theorem
  whose statement I located in the source (or, where said, recall from memory).
- New in this review: the settlement of E.17 with a Kan–Thurston theorem without small quotients; the
  characterization "finite ⇔ finite-dimensional ⇔ bounded integral homology" for classifying spaces of finite
  monoids, and Swan's theorem for finite monoids; uniqueness of the smallest models of S¹ and S² and the fact that
  every smallest S³ is a monoid; a criterion for uncountably many maps to S²; a_pos(RP²) ≥ 34.

## The Thomason–Kan envelope (our project's claim; its own verdict)

Claim (`french_school_site_20261110/findings/2026-11-10_thomason-kan-envelope.md`; `grant_evidence/EVIDENCE.md`):
(1) φ: Cat hot → Hot has no right adjoint; (2) X ↦ [BX, Y] is representable on Cat hot exactly for 1-types Y, the
local categories are those isomorphic in Cat hot to groupoids, reflective and not coreflective; (3) a bounded
envelope exists for every size bound; (4) finite tests: fully faithful for space-valued tests, groupoid-valued tests
decide maps from countable sources, no finite height works in general, sets fail; (5) small models (5-element S²,
7-element S³ and none of order 6, 3-object RP²).

**Verdict: correct in all five points.** Full argument:

(1) and (2), negative part. Let K be a U-small category with natural bijections θ_X: π₀Fun(X, K) → [BX, Y], and
suppose some component of Y has π_n ≠ 0 with n ≥ 2. Let λ > |Mor K| be an infinite cardinal. *Groups too large to
act.* If a group G has no non-trivial homomorphism to a group of cardinality < λ, every functor BG → K is constant
on arrows (a functor sends G into the units of an endomorphism monoid), so Fun(BG, K) ≅ K and π₀Fun(BG, K) = π₀K
(B.1). *Such a G with an essential map to Y.* (i) Every group H embeds in a simple group of any cardinality
λ ≥ |H| (HNN extensions making every element a product of conjugates of every other; B.5) and in an acyclic group
of its own cardinality (mitosis; B.6); alternating gives a simple acyclic A ⊃ H with |A| = λ (B.7). (ii) A *_H A
has no non-trivial homomorphism to a smaller group and its classifying space maps to ΣBH by a homology isomorphism
(B.8); starting from Z this gives G_n with BG_n → Sⁿ a homology isomorphism. (iii) A homology isomorphism induces a
bijection on pointed classes of maps into simply connected spaces (Postnikov tower; B.9), so a non-zero
α ∈ π_n(Y) gives an essential BG_n → Sⁿ → Ỹ → Y (B.10). Naturality of θ for BG_n → e then gives a square whose top
is the bijection π₀K → π₀Fun(BG_n, K) and whose bottom π₀Y → [BG_n, Y] is not onto: contradiction (B.11). For
Y = K(Z/2, 2) the finitary alternating group on λ letters does it at once: it is simple of cardinality λ with
H₂ = Z/2 (B.3, B.4). A right adjoint ψ would make ψ(Y) such a K. Each step was checked: B.1–B.11 below.
(2), positive part. For a groupoid G, N Fun(X, G) = Map(NX, NG) and NG is Kan, so π₀Fun(X, G) = [BX, BG] (C.1);
a local K has BK a 1-type and η_K: K → Π₁K is then an isomorphism in Cat hot with inverse given by localness
(C.3); Π₁ is the reflector (C.4); the infinite fence is contractible and not local, and coproducts show there is
no coreflector (C.5).
(3) D.1: the category of contractible simplicial sets of size ≤ λ over a Kan complex Y represents [B−, Y] on
categories with ≤ λ arrows. Also Raptis's Theorem 3.5 (D.9).
(4) F.2–F.3, F.6 (sets fail), F.7–F.8 (space-valued), F.9 (conservative at height two), F.11 (countable sources),
F.10, F.12 (no finite height in general; F.12 rests on a theorem of Chen quoted from Dicks–Kropholler–Leary–Thomas).
(5) G.9–G.11, G.14–G.15, re-proved by my own programs (`EMAIL_CLAIMS_CHECK.md` (g)).

Three additions to the claim. (a) The ind-version is now also settled (Theorem 3.2 of `OWN_RESULTS.md`): a small
ind-object of Cat hot is W∞-invariant exactly when it is an ind-object of groupoids; so V ms. 46 is right when
"Thomason–Kan" means "local", and invariance on all small categories forces 1-truncation of Grothendieck's path
ind-categories. (b) In the findings file, the sentence that the same fact "explains why, in La Longue Marche,
passing to fundamental groups loses nothing for the anabelian homotopy types" is not something this return proves;
it is a remark about another text and should be checked there. (c) "Checked by two independent readers": those
checks were at effort medium; this review replaces them.

---

## Part A (7 items)

**A.1 correct [V].** Whiskering preserves zigzags, so Cat hot is a category; X × [1] → X is in W∞ with two
sections, so any functor inverting W∞ identifies naturally related functors, and Cat → Hot factors through the
quotient Cat → Cat hot (bijective on objects, full); weak equivalences of a model category are saturated, so [f] is
invertible in Hot iff f ∈ W∞.

**A.2 correct [V].** Loc(3) for W∞ is the relative form of Quillen's Theorem A (the Grothendieck constructions of
c ↦ A/c, c ↦ B/c are weakly equivalent to A, B; Thomason's theorem, Chachólski–Scherer 26.9). For any W:
(X × [1])/x = (X/x) × [1] and X/x have terminal objects, so Loc(1)–(3) give X × [1] → X ∈ W.

**A.3 correct [V].** Idempotent-monad algebra: with pη_K = id, naturality gives η_K p = RL(p)η_{RLK} =
RL(p)RL(η_K) = id (η_{RL} = RLη because R is fully faithful). The representability corollary uses R.

**A.4 correct [V].** Hom in Ind is lim colim; Ind L ⊣ Ind R termwise; a limit of bijections is a bijection, which
is the step Grothendieck flags at V ms. 42.

**A.5 correct [C, Known].** Thomason, Theorem 4.9, Corollary 5.5; c Sd² is left Quillen, so c Sd²(NX × Δ¹) is a
good cylinder for the cofibrant QX = c Sd² NX, and [BX, BK] = Hom(QX, RK)/left homotopy. q_X is a weak equivalence
because Sd² NX → N c Sd² NX and Sd² NX → NX are. (One sentence of the proof is printed twice.)

**A.6 correct [V].** (i) A functor from the group C₂ to a poset P is constant on arrows, so π₀Fun(BC₂, P) = π₀P is
one point, while [BC₂, BC₂] has two elements; fibrant poset models exist by Raptis 2.6. (ii) The crown D is not
fibrant (Ex² ND has finitely many edges, π₁ = Z); Q, the free C₂-equivariant fibrant replacement with Q^{C₂} = D,
and E = Q ⋊ C₂ are fibrant (I checked the horn-filling argument: a functor from a horn to BC₂ is isomorphic to the
trivial one, twist, fill in Q, untwist); Fun(BC₂, E) = E ⊔ (D × BC₂) retracts onto D. Refutes both shortcuts of
VII ms. 136 (and Grothendieck's own footnote 29 there was right to doubt).

**A.7 correct [V].** L^* on presheaves is fully faithful for a localization L; Nat(colim h_{LK_i}, F) =
lim F(LK_i) = Nat(H, L^*F) = Nat(H′, F).

## Part B (11 items)

**B.1 correct [V].** A functor from a group lands in units; Aut_K(k) has cardinality ≤ |Mor K|.

**B.2 correct [C, Known].** Schur: the multiplier of A_n is Z/2 for n ≥ 8 (and n = 4, 5); Domínguez–Segovia,
Corollary 21: its generator is the pair (1 2)(3 4), (1 3)(2 4). The spin lifts ½(e_a − e_b)(e_c − e_d) and
½(e_a − e_c)(e_b − e_d) square to −1 and anticommute (I recomputed: the lift of the Klein four-group in the double
cover is Q₈), so the torus class is non-zero and the inclusions are isomorphisms on H₂.

**B.3 correct [V].** Commutator with a 3-cycle on two fresh points: gτg⁻¹τ⁻¹ = (b c d)(a d c) = (a b c)
(recomputed); H₂ as a filtered colimit with the transition maps of B.2.

**B.4 correct [V].** As in the envelope section. This is the refutation of V ms. 37.

**B.5 correct [V].** w = [g, t][g, t²] and wh are cyclically reduced of length 8 (or 6 when hg = 1) in L * ⟨t⟩,
hence of infinite order; the HNN extension s⁻¹ws = wh exists and puts h in the normal closure of g; iterate and take
the union.

**B.6 correct [V].** Mitosis m(H) = HNN(H × H; d, s); k(b, c) = b c^s is a homomorphism, the two inclusions and the
diagonal followed by k are conjugate to j, so (jf)_*z = 2(jf)_*z on the first degree where f_* can be non-zero.

**B.7 correct [V].** Alternating union of B.5 and B.6.

**B.8 correct [V].** Amalgam A *_H A: no small quotients (generated by two simple groups of cardinality λ);
classifying space the double mapping cylinder; Mayer–Vietoris against ΣBH.

**B.9 correct [V].** Standard (simply connected spaces are local for integral homology equivalences); the proof by
Postnikov towers on mapping spaces is right, including the passage to the limit.

**B.10 correct [V].** Lift to the universal cover, B.9, and free = pointed null-homotopy in a simply connected
target.

**B.11 correct [V].** The naturality square for BG → e. Disconnected Y included.

## Part C (6 items)

**C.1 correct [V]. C.2 correct [V]. C.3 correct [V]. C.4 correct [V].** Arguments as in the envelope section. In
C.3 the inverse of [η_K] is obtained from localness at X = Π₁K and checked on both sides.

**C.5 correct [V].** In the infinite fence a natural transformation moves each coordinate by at most one step, so
r ↦ 0 and r ↦ 2r are not connected; in Ho(Grpd) the discrete category on N is the coproduct of points, which a
left adjoint would preserve.

**C.6 correct [V].** Immediate from C.3: a fibrant replacement of a category of type S² is not local.

## Part D (9 items)

**D.1 correct [V].** A functor X → K_λ(Y) is a diagram A of contractible simplicial sets over the constant diagram
Y; it gives * ← A → Y in Ho(sSet^X), that is an element of [NX, Y]. Surjective by Q_X = N(X/−) (cofibrant, colimit
NX). Injective: factor A → A^f → Y_X, lift Q_X → A^f, and connect two maps NX → Y by a simplicial homotopy; all
objects stay of size ≤ λ. |Mor K_λ(Y)| ≤ 2^λ.

**D.2 correct [V].** [BP, S²] = Z is infinite for a poset P of type S² while Fun(P, K) is finite; A_n with
|A_n| > |Mor K| and H²(A_n; Z/2) = Z/2 for the second.

**D.3 correct [V].** The category of elements is filtered: coproducts give upper bounds, and the tagged
Grothendieck construction of A ⇉ B is a finite category realizing the homotopy coequalizer, over which any
b with b∘Bu = b∘Bv extends.

**D.4 correct [O].** Countable filtered categories have cofinal sequences; finite categories are finitely
presentable, so Fun(C, colim K_n) = colim Fun(C, K_n) and π₀ commutes; local finiteness of the colimit checked.

**D.5 correct [V].** H²(BC; Z/2) is finite for finite C.

**D.6 unproved (open in the return; still open).** Is [BC, S²] countable for every finite category C? My
contribution: Proposition 4.1 of `OWN_RESULTS.md` (infinitely many sphere retracts ⇒ uncountable) and hunch H3: the
six-element monoid of Sweeney's Example 5.2 should give uncountably many classes. Evidence computed: S² is a
retract; cup products x₂², x₂x₃ vanish mod 2, 3, 32003. The return's remark that finite groups are no obstruction
(Miller's Theorem A) is right. Prompt: `PRO_PROMPTS/S2COUNT`.

**D.7 correct [O].** The K_λ(Y) are nested full subcategories with compatible θ; for fixed X bijective from
λ ≥ |Mor X| on.

**D.8 correct [V].** For G huge relative to all K_i, π₀K_i → π₀Fun(BG, K_i) is the identity for every i, so any
colimit sends BG → e to a bijection; but [BG, Y] has a non-constant class. (For filtered colimits this also follows
from Theorem 3.2.)

**D.9 correct [V], with a wrong attribution.** The statement is true: Raptis, Theorem 3.5, makes every category
with fewer than μ arrows cofibrant in Cat_{I(μ)}; X ⊔ X → X × Z₂ is a pseudo-Dwyer morphism between μ-presentable
objects (sieve X × {a₀, a₂}, cosieve X × (Z₂ ∖ {a₁}), retraction a_{0/1} ↦ a₀, a_{1/2} ↦ a₂), so X × Z₂ is a good
cylinder, and left homotopy through it is a four-step zigzag of natural transformations. But the sentence "the
product discussion at the end of Section 3 proves that X × − is left Quillen" misreports the source: that passage
(p. 220–221) proves that these model structures are *not* monoidal. The cylinder statement itself is in Raptis's
proof of Proposition 4.8 (for posets; "a similar construction" for Cat), which the return also cites.

## Part E (27 items)

**E.1 correct [V].** Collects A.3–A.7, B.4, C.3, D.1.

**E.2 correct [V].** Finitely many objects land in one full stage; fullness brings arrows and components of
transformations; zigzags are finite.

**E.3 correct [V].** Inductive lifting gives strictly commuting fibrant replacements; the generating trivial
cofibrations have finite domains, so filtered colimits of fibrant categories are fibrant.

**E.4 correct [V].** T_n (objects 0..n, Hom(i, j) = Sym{0..j} for i ≤ j) is isomorphic in Cat hot to BSym{0..n}
(identity-labelled arrows to the object n) and is fibrant (fill in BG_n, send new objects to n); the shift and the
inclusion T_n → T_{n+1} are joined by three transformations because c g c⁻¹ = s(g) for the long cycle c; on
BT ≃ BSym_fin(N) the shift is not onto on π₁. A genuine counterexample to V ms. 47 ("alors u_∞ est forcément un
isomorphisme dans Hot"), with all the hypotheses of ms. 46–47 satisfied.

**E.5 correct [V].** Poset maps between fences do not increase distance; 0 and 8 are at distance 8 in A and 4 in
B; A is contractible in Cat hot by the functors max(i, k).

**E.6 unproved (open in the return; still open), one case added.** Proved in the return: a strict retraction in the
Hot-class of p. Added here: if A is also local, any strict retraction r with [r] = [p] in Hot has [r] = [p] in
Cat hot (C.3). My guess is that E.6 fails in general (hunch H4: the pushout-product needed for a homotopy extension
property of zigzags is not a pseudo-Dwyer morphism).

**E.7 correct [V].** The terminal fork 0 → 1 ← 2 has a terminal object, hence is fibrant (send all new objects of a
horn to it), and 0, 2 are joined by no single arrow: answers the question of V ms. 49 in the negative.
Dwyer–Kan part [C].

**E.8 correct [V].** Thomason's theorem and "filtered hocolim = colim"; compactness of finite CW types; BC₂ shows
that a finite category is not a compact test, against VII ms. 121.

**E.9 correct [O].** Under the stated rectification hypothesis the formula is the end formula for mapping spaces of
constant diagrams (HTT 4.2.4.4 for the hypothesis). The last assertion (small M with invariance on all shapes forces
1-types) follows from D.8, and now in the stronger form of Corollary 3.3 of `OWN_RESULTS.md`.

**E.10 correct [V].** Fun([1], C) ≃ C by the source evaluation; strict fibre Hom(a, b) versus path space.

**E.11 correct [V]** (given F.2, F.6, F.7–F.9, F.13).

**E.12 correct [V].** π₀ commutes with finite products of categories (pad zigzags).

**E.13 correct [V].** [N, Y] = (π₀Y)^N = lim [D_n, Y]; (D_n) is not essentially constant. (It refutes a
parenthesis of IX ms. 10, not a theorem of the text.)

**E.14 correct [V; O for one paragraph].** Pointed sets {0, x} with only identities inverted:
Hom(a_X, b_X) = Hom(a, b)^{π₀X} is invariant, mapping spaces are discrete, Σ = Ω = 0. A finite pointed category with
finite products is trivial (2^r arrows a → b^r). The paragraph identifying the path categories with discrete ones
(functors q, s, R) was read and looks right; I did not re-derive its naturality squares.

**E.15 correct [V].** Standard; the counterexample to "cofibration suffices" (P b = b × b) is right.

**E.16 correct [O].** A table of cross-references; each row checked against the item it cites. The row "V 46" must
now read: true, by Theorem 3.2 of `OWN_RESULTS.md`.

**E.17 unproved in the return; SETTLED HERE: true.** The criterion (E.17a) is correct [V] (A.4 for Π₁ ⊣ j). The
missing implication (E.17c), "H_K inverts W∞ ⇒ H_K inverts every η_X", holds: `OWN_RESULTS.md`, Theorems 3.1 and
3.2. Idea: for each X there is a groupoid 𝒢 = ∐ BG_c with an acyclic map B𝒢 → BX such that every homomorphism from
G_c to a small group factors through π₁; functors from 𝒢 to the K_i are then the same as functors from Π₁X, while
maps from B𝒢 to the BK_i are the same as maps from BX. The groups are built cell by cell from the simple acyclic
groups of B.7 (and the Kan–Thurston theorem for the lifting of attaching maps). Consequence: the invariant small
ind-objects of Cat hot are exactly the ind-groupoids; V ms. 46 is true for "local".

**E.18 correct [V].** One-object test categories BH land in one full stage (E.2); bijections on [BH, −] for all
groups H and on π₀ give an equivalence of 1-types; equality of two maps is assembled in the groupoid Π₁K′.

**E.19 correct [C, Known].** Dwyer–Kan hammock localization (not opened by me; standard): strictly associative
composition, π₀ = localization, composition with arrows of W a weak equivalence; Ex^∞ preserves finite products.

**E.20 correct [V].** Fun(I, X) ≃ X for a finite oriented interval by the retractions min(i, k); filtered colimit.

**E.21 correct [V].** Even-even stages are fibrations over X × X and odd-odd stages opfibrations, so both lift
categories of the union are filtered unions of categories with a terminal (initial) object; then E_b → b∖q is a weak
equivalence by Quillen A (its comma category is the lift category), base changes are weak equivalences through
M_h, and Quillen B applies. I re-derived the three steps.

**E.22 correct [V].** T²j = j and Bj is invertible in Ho(Spc/K²), so B(T²) = id there; derived fibres. This proves
the T² = 1 that VII ms. 149–150 hoped to get from faithfulness of finite tests.

**E.23 correct [O].** q_L S = T⁻² q_L checked; the infinite concatenation of collar homotopies is continuous because
stationary on each simplex; the image argument for homotopy groups re-derived.

**E.24 correct [O].** Cancellation of the constant sections in the localized slices over K² and K³; the fibre
identification by the middle coordinate.

**E.25 correct [O].** The collar functors send edges to edges of the same direction or to identities, so they
preserve Σ-paths; units by cancellation. Associativity is rightly not claimed.

**E.26 unproved (open; still open).** Hunch H6: true for Σ = Mor(X). **E.27 unproved (open; still open).** Same.
Prompt: `PRO_PROMPTS/INDLOCAL`, Part C.

## Part F (13 items)

**F.1 correct [V].** Finite posets ↔ finite complexes; finite 2-skeleton; BC₂ = RP^∞ is not compact (mod 2
cohomology in every degree).

**F.2 correct [V].** The shift s on Sym_fin(N) is conjugation by a long cycle on every finitely generated
subgroup, so Bs acts as the identity on [A, BSym_fin(N)] whenever π₁(A) is finitely generated; s is not onto.
Refutes "conservatif" and "fidèle" of V ms. 52, VII ms. 121 (note 26), 127, 150.

**F.3 correct [V].** The transformation "send basis letters to disjoint transpositions" is natural on tests with
finitely generated π₁ and not induced by a homomorphism from the free group on an uncountable set to a countable
group.

**F.4 correct [V, Known].** Arlin–Christensen, Theorem 2.1; the size argument given is right.

**F.5 correct [C, Known].** Freyd; cited, not re-read beyond locating it.

**F.6 correct [V].** H²(Tel; Z) = Z₂/Z ≠ 0 (the 2-adic computation recomputed: 1 + 4 + 16 + … = −1/3);
finitely generated subgroups of Z[1/2] are cyclic.

**F.7 correct [O].** HTT 5.3.5.11 with compactness of finite complexes and generation under filtered colimits.

**F.8 correct [O].** Right Kan extension along the inclusion of finite CW types; BC₂ not compact.

**F.9 correct [V, Known].** The orbit-set argument for Γ-equivariant homomorphisms is right.

**F.10 correct [V].** π_{n−1}Map(T, K(Z, n+1))₀ = H²(T; Z) ∋ α; the top homotopy group of a mapping space of
(n−1)-truncated presheaves injects into the product over tests.

**F.11 correct [V].** Milnor sequences for τ_{≤m} holim versus holim τ_{≤m}: equal π_k for k < m, onto for k = m.

**F.12 correct [O; C].** Rests on cd_Q(⊕_{ℵ_{d−1}} Z/2) = d (Chen; Dicks–Kropholler–Leary–Thomas, Corollary
6.10(2), statement read). Section spaces over finite subgroups are K(M^H, r) by averaging; the coherent section
space of the truncated presheaf is a limit of contractible spaces. Structure checked; the cardinal bookkeeping not
re-derived.

**F.13 correct [O].** Translation by the section s_α is tested trivially at height n and T² ≠ id.

## Part G (17 items)

**G.1 correct [V].** A finite poset has a finite order complex; a finite complex is homotopy equivalent to a finite
simplicial complex (Hatcher 2C.5), whose face poset has it as barycentric subdivision. A finite category with m
arrows has at most m^r non-degenerate r-simplices; BC₂ = RP^∞ shows the nerve need not be finite-dimensional.

**G.2 correct [V].** Diagonal argument: list the countably many finite categories C_i and put A_i = Z/2 exactly when
π_{i+2}(BC_i) = 0; the product of the K(A_i, i + 2) is simply connected, finite in each simplicial degree, and
differs from every BC_i in π_{i+2}.

**G.3 correct [C, Known].** McDuff's theorem (not opened; from memory: every path-connected space has the weak
homotopy type of BM for a discrete monoid M). The countable reduction is a correct Löwenheim–Skolem argument.

**G.4 correct [V].** `G6_VERDICT.md`. Sharpened: Theorems 2.1–2.2 of `OWN_RESULTS.md`.

**G.5 correct [C], given Theorem C of arXiv:2610.38760v1 (recent, unrefereed).** I read that proof and found no
gap; five numerical tests of Theorem A pass (`work/code/theoremA_test.out`).

**G.6 correct [V].** `G6_VERDICT.md`: Conjecture 7.1 of the preprint is false as stated.

**G.7 correct [V].** A vertex-minimal full subcomplex with H̃_n ≠ 0 has H̃_{n−1}(lk v) ≠ 0 for every vertex; induction
gives ≥ 2n neighbours, no cone point, so ≥ 2n + 2 vertices and ≥ n f₀ edges; the join of n + 1 copies of S⁰ attains
both.

**G.8 correct [C; V for the bound].** 13 points: Cianci–Ottina 5.8, 5.10. The lower bound 28 is right and can be
raised to 34 (`OWN_RESULTS.md`, Proposition 5.1).

**G.9 correct [V]. G.10 correct [V].** Both resolutions verified exactly by my program (`resolution_check.out`),
bar homology agrees through degree 4 and 3.

**G.11 correct [V].** The nerve of R₂ is the octahedron modulo the antipodal map; also checked as a closed surface
with χ = 1 and H₁ = Z/2.

**G.12 correct [V].** For a strongly connected component S and a ∈ S, U(End(a)) → π₁(BS, a) is onto
([u_y]⁻¹[f][u_x] = [v_y u_y]⁻¹[v_y f u_x]); the group at the minimal ideal of End(a) then maps onto π₁(BS) and, by
Miller's Theorem B, trivially to π₁(BC); the quotient D has each arrow represented by one arrow of C.

**G.13 correct [V].** Case analysis for acyclic categories with at most 8 arrows re-derived (three objects need
a, b, c ≥ 2).

**G.14 correct [V].** Reproduced by my own enumeration, with the same counts (2, 11, 76, 977; 6, 54) and the same
ten tables with H₃ = Z/2.

**G.15 correct [V] (the return's label "Known" can be upgraded).** My enumeration of all 208,672 labelled monoids of
order 6 (1,373 classes) and of orders ≤ 5 gives no (0, 0, Z); the list of triples agrees with the one quoted from
Sweeney. Added: with 7 arrows no category with ≥ 2 objects has (0, 0, Z); the smallest S¹ and S² are unique.

**G.16 correct [V].** Follows from G.4, G.7–G.15.

**G.17 unproved (open; partly advanced).** (i) 34 ≤ a_pos(RP²) ≤ 49. (ii) K(Z, 2): a reformulation, the exclusion of
regular monoids (if Putcha's theorem is as I recall), and of all monoids of order ≤ 6 (hunch H2). (iii) The
finite-dimensional part of the classification for finite categories is hunch H1 (Wall's obstruction).

---

## Corrections to the return's wording, sources and labels

1. D.9: wrong attribution to Raptis's product discussion (see D.9).
2. A.5: a sentence printed twice.
3. G.15: "Known" from an external table; it is now proved by an independent enumeration.
4. E.13 is labelled "Refuted" for a parenthetical remark of the manuscript; "the parenthesis is not an equivalence"
   would be more exact.
5. README and report say that the six Open items are open "in this audit". Correct; E.17 is no longer open.
6. The report's bibliography marks Fiedorowicz 1984 as verified from a copy on a university course page; I did not
   use that copy.

## What the return's code is (read, not run)

`a_finite_checks.py`, `e_full_filtration.py`, `e_retraction_and_pointed.py`, `e_fence_check.py` (finite
verifications of the crown, the fork, the filtration T_n through stage 3, the fences, the five-arrow pointed
category); `bc_checks.py` (commutator, Clifford lifts, the word w for cyclic groups, fence distances);
`f_checks.py`, `f_sweeney_cup.py`; `g_finite_models.py` (models and the enumeration for G.14), plus build and
packaging scripts. Each states its scope; none is used as a proof of an infinite statement. Their recorded outputs
agree with my independent computations wherever the two overlap (counts 1, 2, 11, 156; 2, 11, 76, 977; 6, 54; the
ten F₂-ambiguous tables; the homology of P₂, P₃, R₂).
