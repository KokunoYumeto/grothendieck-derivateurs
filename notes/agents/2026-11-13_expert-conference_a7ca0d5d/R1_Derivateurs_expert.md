# Round 1 — the Dérivateurs expert (total asphericity, TOTAL_EXACT_2, DER_FOLLOWUP)

Claude Fable 5.2, effort max, 13 November 2026. This talk replaces the note BUILD_ON_TOTEX2 that I was asked for
before the conference; what I had for it is here.

**Read for this talk.** My notes (KNOWLEDGE_HANDOFF, HUNCHES, NEXT_PROMPT_ITEMS), the final register of
TOTAL_EXACT_2 (Parts A and D; A.1, A.18, A.20, A.24, A.31–A.34 in full), the intake's BLOCK, PUSH_ITEMS, addendum
and IMPLICATIONS (summary, I1–I5, P1–P5), the framing section of the shape-map card. **Not read:** the proofs of
TOTAL_EXACT_2 (a successor is doing the referee reading), INTAKE_TOTEX2 row by row, LM8, LM4, LM7, the other talks.
"T" = TOTAL_EXACT_2. "Checked here" = derived by me for this talk, by hand, no program, no second reader.

## 1. What T changes in the theory as the manuscript has it

**1.1 II ms. 36–36ter.** Grothendieck conjectures: *totalement `W∞`-asphérique ⟹ filtrante*. The true picture, for
non-empty connected small categories (T D.1): `filtered ⊊ exact ⊊ total ⊊ quasi-filtered`, witnesses `Δ_inj`
(Isbell–Mitchell 1973), `C_δ` (T A.1, A.34), `K*` (T C.28). Each class is an exactness property of `colim_A` for one
kind of coefficients:
- filtered ⟺ `∫_A D → colim_A D` is a weak equivalence for all diagrams of categories, or of groups (PRETOT F.4);
- exact ⟺ `L_i colim_A = 0` on `Ab^A` ⟺ `Aff_Z(A)` filtered (Isbell–Mitchell);
- total ⟺ `hocolim_A = colim_A` on diagrams of sets, or of simplicial sets (TOTASPH C.5);
- quasi-filtered ⟺ the same up to `π_1`: every category of elements is simply connected (TOTEX A.4, B.5–B.6; Isbell–Mitchell
  1976).
What remains true of the conjecture: total and sifted ⟺ filtered (PRETOT F.3 = TOTEX D.4); total with a weakly
terminal object ⟺ filtered (Isbell–Mitchell 1976, Cor. 4.4). Prop. 2.19 and its Corollary at II ms. 36 (`Δ°` total),
which he marks "Faux", are false for a structural reason given in 1.2.

**1.2 XII ms. 88–89, Définition 1, and test categories (checked here; it is an unfolding of definitions).** For
`H: A → Set`, `El_A(H)` is the opposite of the category of elements `B/H` of `H` as a presheaf on `B = A^op`. So:

> `A` is totally `W∞`-aspherical iff `A ≠ ∅` is connected and every connected presheaf on `A^op` is aspherical; that
> is, on `(A^op)^` the `W∞`-equivalences of the test-category formalism (`X ↦ B/X`) are exactly the
> `π_0`-bijections.

Total categories are the opposites of the categories whose presheaf topos has trivial test homotopy theory. This is
the precise relation between Définition 1 and the "totalement asphérique" of the theory of test categories, which
Grothendieck's bracket at XII ms. 89 keeps apart (the bracket as the review of PRETOT reports it; I have not reread
the page). Consequence: if `B` is a weak test category then `B^op` is not total;
`Δ` is one, so `Δ°` is not total. In topos terms: `[A, Set]` has `π_0` left exact iff `A` is filtered; `π_0` exact on
abelian objects iff `A` is exact; all connected objects of trivial shape iff `A` is total. T A.1 says the second is
strictly stronger than the third.

**1.3 What "total does not imply exact" means for derivators.** For `p: A → e`: `p_!: HOT(A) → HOT` preserves discrete
objects iff every component of `A` is total (TOTASPH C.5, TOTEX D.10); it preserves `n`-types for one `n ≥ 1` iff
the comma categories of `A → ΠA` are filtered (TOTEX D.9–D.10); `p_!: D(Z)(A) → D(Z)` is t-exact iff `A` is
exact (`H_i p_! M = T_i(M)`, TOTEX D.12). T A.24: over `C_δ`, `T_1(coker D) = R` for the column `D: P_W → P_V²` and every ring `R ≠ 0`; `colim D = 0`, and
`D` is injective at every object by the private-incidence argument that the intake reports (sparseness,
`2v > 3r`; I have not read that proof). So linearization `HOT → D(Z)` carries discrete
objects to permutation modules, and vanishing of `Tor^{ZA}(ΔZ, −)` on permutation modules (totality) does not give
flatness of `ΔZ`. Wherever the companion passes from total asphericity to arbitrary abelian coefficient systems it
needs exactness, which is a different hypothesis. The classes are not linearly ordered once the ring varies:
`{Z-exact} = {Q-exact} ∩ ⋂_p {F_p-exact}` (T A.2); `C_δ` is `R`-exact for no `R` (T A.3); and (checked here) the
category `FI` of finite sets and injections is `Q`-exact (average over `S_q`), `F_p`-exact for no `p` (the pair
`id, σ`, `σ` a `p`-cycle: `t = tσ` forces `aug t ∈ pZ`), and not total: for `T(B)` = the 2-element subsets of `B`,
`El_FI(T) ≃ B(Z/2)` (the inclusion of the object `(S, S)` has a right adjoint).

**1.4 XII ms. 107–114.** Totally `W`-dwyérienne sieves compose iff non-empty cosieves of categories total for `W` are
total for `W` (TOTASPH F.9). True for `W∞` (PRETOT B.4). For `W_2` it fails if my Lead 1 stands: with T C.28, the
category `E = El_{K*}(h_V/(cv_1 ∼ cv_2))` with an initial object adjoined is total for `W_2` and its cosieve `E` is
not (DER_FOLLOWUP A.2; Lead 1 has no second reader).

**1.5 VII ms. 99–115.** `Ty^op` fails span completion (T C.40): it is none of the four classes. What makes
`C_∞ → C` an isomorphism in `Hot` for the path categories is a property of the diagram, the strict action of the
2-category of types (PATHS C.P1–C.P3), not of the shape. DER_FOLLOWUP Part B asks for the exact class of diagrams.

## 2. My reading of the intake

**Agree.** The placement of T in the companion (BLOCK; applied to DER_FOLLOWUP, which is ready to send). The duality
I1: `lim^i_{A^op} Hom(M, R/Z) = Hom(T_i(M), R/Z)`. Ground: I checked it; `Hom(−, R/Z)` is exact and turns the bar
complex `⊕_{a_0→…→a_n} M(a_0)` into the cosimplicial replacement of `M^∨` on `A^op`. The topos reading of A.33
(sheafification for the atomic topology on `A^op` is homotopy final on categories of elements; atoms `G/G_F` are
representable).

**Cannot confirm.** That the proofs are right: I read statements only.

**Disagree, with grounds (checked here).** P1 (b) = N2, "for a class with canonical amalgamation, `colim_A` is exact
iff `Aut(M)` is amenable", is false as stated. `FI` is the age of the pure set, `Aut(M) = S_∞` is amenable, and `FI`
is not `Z`-exact (1.3). The one-object category `BZ` has the Reiter property and `H_1(Z; R) ≠ 0`. Both failures come
with a category that is not total (`B(Z/2)`, `S¹`). The statement that survives my checks: for **rigid** ages, or
with `Q`-coefficients; see C2, C3 below.

**Extend: three compact-limit properties of an index `A` with common successors.**
- (CH) every `A^op`-diagram of non-empty compact Hausdorff spaces has a point ⟺ finite-pattern Ramsey (T A.13).
- (CC) every `A^op`-diagram of non-empty compact convex sets with affine maps has a point.
- (CAb) `lim¹_{A^op}` vanishes on compact abelian groups ⟺ exact (I1).
Proved: (CH) ⟹ (CC) trivially; (CH) ⟹ (CAb) (T A.14). Checked here: (CC) ⟹ the **Reiter property** (R): for every
finite family `a_0, …, a_k: p → q` and `ε > 0` there are `r` and a probability `t` on `A(q, r)` with
`Σ_i ‖ta_i − ta_0‖_1 < ε`. Proof: if (R) fails with gap `ε`, Sion's minimax gives at each `r` a non-empty compact
convex set of potentials `φ_i ∈ [−1, 1]^{A(p, r)}` with `Σ_i (φ_i(ca_i) − φ_i(ca_0)) ≥ ε` for all `c: q → r`; they
pull back along arrows, and a compatible family is constant on `π_0(p\A) = pt`, which contradicts `ε > 0`. T A.18 is
the failure of (R) for `C_δ` and `K*` with `ε = 1`; T A.19 gives such a diagram over `K*` (I have not compared its
construction with this one). Checked non-implications:
(CC) ⇏ (CAb) (`BZ`; `FI` over `Z`). Not decided by me: (R) ⟹ (CC) (expected, Markov–Kakutani), (CAb) ⟹ (CC),
(CAb) ⟹ (CH).

## 3. Floor questions

**Q1.** For all compact coefficients the condition is on the index alone and is known: `Aff_Z(A)` filtered.
Mittag-Leffler's role is played by affine directedness: a diagram of abelian groups on `A` extends to `Aff_Z(A)`,
and over a filtered `Aff_Z(A)` the directed compactness argument applies. Amenability is a different property, (CC)
= (R) above, and it is not sufficient for exactness (`BZ`, `FI`). Whether it is necessary I do not know. Convex
Ramsey is (R) for ages (Moore 2013, not opened). My candidate for the right statement is C1: exactness is (CH).

**Q4.** Where my field confirms the central statement: the failure of `colim` over `C_δ` is `T_1(Q) = R` (T A.24),
dually `lim¹ = F_p` on finite `F_p`-spaces; it is invisible to sizes in a strong form (T A.20: `|M(a)| ≤ N` gives
`T_i(M) = 0`); and the derived object `p_!` in `D(Z)` absorbs it. Where it needs a sharper form:
- the class is invisible to **homotopy**, not only to the underived object: `BA` and every `B El_A(H)` are
  contractible. What sees it is the linear structure (flatness of `ΔZ`);
- there is no closing gap (T A.18): the obstruction has a uniform gap at every object, and `colim` kills an injection;
- "first-derived" depends on the coefficients. Over `K*` with set coefficients `L_1 colim Z[H] = 0` for every `H`
  and the first class is `L_2` (T C.28). DER_FOLLOWUP A.3 asks whether a first class in `L_n` occurs for every `n`.
  A separation `𝒬_n ≠ 𝒬_{n+1}` would be a finite-to-limit failure whose first class is `n`-th derived;
- PRETOT A.5 is a first-degree class that is non-abelian (`π_1 = SL(2,5)`, all homology zero).

**Q3, one statement from my side.** T A.33 is a case where the Galois part read stage by stage loses nothing: the
slice of `[A, Set]` over `H` and the slice of `Cont(G)` over its sheafification have the same homotopy type. The test
that decides when this is safe is homotopy finality of sheafification on categories of elements. For `FI` the atoms
already differ (`B(Z/2)`); for `K*` I do not know which of the two steps fails.

**Q5.** DER_FOLLOWUP is ready (Parts A–F). N1–N6 go to the successor's prompt, with N2 corrected as in section 2.
Candidates from this talk for that prompt:
- **C1.** For `A` non-empty with common successors: exact ⟺ (CH). (⟸ is T A.14. Consistent with every example I know:
  filtered categories, monoids and groups, `Δ_inj`, `W_m`, ordered graphs, `C_δ`, `K*`. Test: a rigid age that is
  exact and not Ramsey; first candidate, finite equivalence relations with an arbitrary linear order.)
- **C2.** For total `A`: `Q`-exact ⟹ `Z`-exact. (`FI` shows totality cannot be dropped.)
- **C3.** (R) ⟺ (CC) for every `A`; and for total `A`, exact ⟺ (R).
- **C4 (the converse of N1).** For an age with free amalgamation, `G_F ⊴ U` open of finite index:
  `El_A(T_{G/U}) ≃ B(U/G_F)`. So, where every open subgroup is such a finite extension of a pointwise stabilizer, `A` total ⟹ every open
  subgroup is a pointwise stabilizer. (Checked for `FI` only: `U = G_{{x,y}}`.)
- **C5.** Over a total category `T_i = 0` for `i ≥ 2`; decide it for `C_δ`. (No evidence; over `C_δ` the module `Q`
  has `T_i(Q) = 0` for `i ≥ 2` if `D` is injective, since its resolution then has length 1.)
- **C6.** Express the failure of totality of `K*` in Galois terms: which atom of `Sh(K*^op, atomic)` has a
  non-contractible category of elements, or where sheafification is not homotopy final.

## 4. Three questions

1. **To the LM7 reviewer.** `FI` shows that finite automorphism groups in an index kill exactness at exactly the
   primes dividing their orders and keep it over `Q`. Is any limit in LM7 or LM7_PUSH taken with compact coefficients
   over an index with non-trivial finite automorphism groups (finite Galois covers with all their morphisms, orbit
   categories of open subgroups), instead of a tower? And is the class that every maximal pro-`ℓ` quotient misses
   (LM8 A.22, G.20) of this kind: zero after inverting the orders, non-zero integrally?
2. **To the intake agent.** In P1 (a), does "exact on finite abelian groups of unbounded size" include `Q`-exactness?
   `FI` is `Q`-exact and `F_p`-exact for no `p`, so one direction fails; did you check whether `F_p`-exact for all `p`
   implies `Q`-exact? And is (R) ⟺ (CC) a row of T, or only the instance A.19?
3. **To the shape-map agent.** How does the map read a failure whose first class is `n`-th derived (T C.28 for
   `n = 2`)? And is "invisible to sizes" the statement of T A.20, or a statement about cardinalities of the limit?
