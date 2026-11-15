# DER_FOLLOWUP: the questions left open by the returns on Grothendieck's *Les Dérivateurs*

To be settled: the tower of totally `W_n`-aspherical categories and the composition of totally `W_n`-dwyérienne
sieves (PRETOT C.4); for which fibred categories over Grothendieck's category of interval types the sequential
model computes the homotopy type (VII ms. 103–114); the strictly aspherical endpoint functors of path categories
(PRETOT E.9); free monoids as test diagrams for filteredness (PRETOT F.10); and the totally aspherical acts over the
monoids `End_Δ([n])` (PRETOT A.5 for every `n`).

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for the deliverables: `DER_FOLLOWUP`.
Drafted on 13 Nov 2026 by Claude Fable 5.2 (effort max), successor of the Dérivateurs expert, from the return PRETOT
(GPT-6 Astra, ChatGPT Pro mode, 12 Nov 2026; 54 statements) and its review by Claude Opus 5.5 (effort max; none of
the 54 found wrong; C.4, E.9, F.10 open), from the returns TOTASPH, TOTEX and PATHS with their reviews, and from the
expert's notes of 13 Nov 2026.

Related prompts. TOTAL_EXACT_2 (total ⇒ exact; the Adámek–Koubek–Reiterman category `K*`) is still running; its
checkpoint 02 is attached as the state of an unfinished run, read by nobody on our side. INDLOCAL (unsent) checks
PATHS C.P1–C.P4 and the comparison with the simplicial localization. Neither is to be done again here. The two
items below marked **[TOTAL_EXACT_2]** are also asked there.

## What is attached

One file, `DER_FOLLOWUP_background.zip`; `MANIFEST.tsv` at its root lists every file with its origin. Documents are
attached as LaTeX source wherever a source exists.
- `PRETOT_return/`: the return PRETOT (paper as TeX, results table, report, bibliography, `code/`). Its statements
  are cited below by their numbers A.1 to G.3. `PRETOT_REVIEW.md`, `PRETOT_FINDINGS.md`: the review (F12, F13, F15).
- `TOTEX_return/` (paper as TeX, results table, report, bibliography) and `TOTEX_REVIEW.md`.
- `TOTASPH/`: sections C, D, F of the return TOTASPH with their follow-up sections, its results table and its review.
- `PATHS_return/` (paper and all sections as TeX, results table, bibliography) and `PATHS_intake/` (review,
  findings F1–F3, the second reading of F2).
- `TOTAL_EXACT_2/PROMPT.md` and `TOTAL_EXACT_2/checkpoint02/` (results table with 62 statements, report, paper and
  all sections as TeX).
- `LEADS_DERIVATIONS.md`: the drafter's derivations behind Leads 1, 2, 3 and 5, step by step, with what was
  checked and how. `checks_drafter/lead2_walking_retraction.py` and its output: the program behind Lead 2.
- `ty_check.py`, `ty_check.out`: the enumeration behind R12.
- `arxiv/`: TeX sources of Shoikhet, *On Evrard's homotopy fibrant replacement of a functor* (1412.0317);
  Hackney–Ozornova–Riehl–Rovelli, *Pushouts of Dwyer maps are (∞,1)-categorical* (2205.02353); Charney, *An
  introduction to right-angled Artin groups* (math/0610668); Nicholson, *On CW-complexes over groups with periodic
  cohomology* (1905.12018); Chachólski–Scherer, *Homotopy theory of diagrams* (math/0110316); Gray–Steinberg,
  *Topological finiteness properties of monoids, Part 2* (1805.03413).
- `papers/`: Isbell–Mitchell, *Exact colimits*, Bull. AMS 79 (1973); Isbell–Mitchell, *Exact colimits and fixed
  points*, Trans. AMS 220 (1976) (PDF; no source exists).
- `DER_II-a.tex` (II ms. 1–53), `DER_VII-a.tex` (VII ms. 1–57), `DER_VII-b.tex` (VII ms. 50′–117),
  `DER_XIIb-a.tex` (XII ms. 59–122): Grothendieck's text, the French transcription corrected on 11 Nov 2026,
  AI-made from the edition of Künzer, Malgoire and Maltsiniotis; manuscript pages are marked `\msp{page N}`. The
  edition is the authority; where a formula looks wrong, say so and reason from the mathematics.

Not attached, and opened by nobody on our side: Isbell, Canad. Math. Bull. 11 (1968); Isbell, Ann. of Math. 100
(1974); Oberst, Math. Z. 107 (1968); the sources of R16 other than Gray–Steinberg. Adámek–Koubek–Reiterman, Czech.
Math. J. 31 (1981) is in the package of TOTAL_EXACT_2 only.

## Where this comes from

- XII ms. 88–89 (Définition 1): `A` is *totalement `W`-asphérique* when every category receiving a final functor
  from `A` is `W`-aspherical. II ms. 36ter conjectures that for `W∞` this means filtered; that is false (`Δ_inj`).
- XII ms. 109–114 (Définition 2): strictly and totally `W`-aspherical functors, `W`-dwyérienne sieves, the doubt at
  ms. 113 whether they compose, and the class wanted "pour des applications ultérieures" at ms. 114.
- XII ms. 93–97 (Proposition 8 and its converse, "je me vois mal construire un exemple") and ms. 101–103
  (Proposition 10, path fibrations, "J'en doute fort!").
- VII ms. 25–32: the category `Ty` of interval types and the fibred category `Ch(X) → Ty`. VII ms. 99–115: for a
  category `C` fibred over `T` and a cofinal sequence of objects of `T`, is `C_∞ → C` an isomorphism in `Hot`?
  (question (b) at ms. 103; "en général pas" at ms. 112; footnote 24 at ms. 113; the diagram at ms. 114).

## Results this prompt builds on (status on 13 Nov 2026)

**Notation and conventions used from here on (keep them).**

- Categories are small. `BA = |NA|`. `W∞`: functors whose nerve is a weak homotopy equivalence; `W_n`: isomorphism
  on `π_0` and on `π_i`, `1 ≤ i ≤ n`, at every base point; `W_Z`: integral homology equivalences. `u: A → B` is
  *final* when every `b\A` (objects `(a, b → u(a))`) is non-empty and connected.
- An *action* on `A` is a functor `L: A → Set`; `El_A(L)` has objects `(a, l)`, `l ∈ L(a)`, and arrows
  `f: (a, l) → (a', l')` with `L(f)l = l'`. An *action component* of `A` is a connected component of some
  `El_A(L)`. For a presheaf `H: U^op → Set`, `U/H` has arrows `a: (u, h) → (v, k)` with `H(a)k = h`, and
  `π: U/H → U` is the projection; the *restricted actions* of `H` are the categories `El_{U/H}(Lπ)`, `L: U → Set`.
- `H` is *totally `W`-aspherical* when `U'/p_!H` is `W`-aspherical for every `p: U → U'`; a category is *total
  for `W`* when its terminal presheaf is; *total* without a localizer means for `W∞`. `f: A → B` is *strictly*
  `W`-aspherical when every presheaf `B(f(−), b)` on `A` is totally `W`-aspherical, and *totally* `W`-aspherical
  when every `A/b` is a total category (XII Définition 2). Sieves and cosieves are full.
- Conditions I (every span completes to a commutative square) and IV (every parallel pair `a, b: p → q` has an
  *affine equalizer*: `t ∈ Z[A(q, r)]` of augmentation 1 with `ta = tb`). *Quasi-filtered*: non-empty, connected,
  I and IV. *Exact*: `colim_A: Ab^A → Ab` is exact; `T_i = L_i colim_A`.
- **`𝒬_n`** (`n ≥ 2`): the class of non-empty connected categories all of whose action components are
  `(n−1)`-connected. `𝒬_∞ = ⋂ 𝒬_n`. `E^◁`: the category `E` with an initial object adjoined.
- `Ty`: objects the finite words `τ` in `+, −`; `I_τ` the free category on the oriented line of `τ`; a morphism
  `τ → ρ` is a functor `I_τ → I_ρ` preserving both end points and non-decreasing on vertices (PRETOT E.1);
  equivalently `Ty(τ, ρ)` is the set of weakly increasing sign-preserving maps from the letters of `ρ` to the
  letters of `τ`. The empty word is terminal. `𝕋y`: the strict 2-category with the same objects whose
  hom-categories are the posets `P(τ, σ)` of type maps ordered by pointwise arrows of `I_σ` (PATHS C.P1). `R`: the
  reachability preorder of types (`τ ≤ σ` when `Ty(τ, σ) ≠ ∅`). For a type `r`, `r↑` is the full subcategory of
  `Ty` on the types `τ` with `Ty(r, τ) ≠ ∅`.
- For `F: Ty^op → Cat`: `∫_{Ty} F` is the category fibred over `Ty` (objects `(τ, x)`, `x ∈ F(τ)`; an arrow
  `(τ, x) → (σ, y)` is `φ: τ → σ` with `x → F(φ)y` in `F(τ)`). A *cofinal sequence* is `t = (t_0 ← t_1 ← …)` in
  `Ty` such that every type receives a map from some `t_n`; `E_t` is the fibred category of `n ↦ F(t_n)` over it,
  `C_∞(t) = colim_n F(t_n)` in `Cat`. The *comparison* for `(F, t)` is the pair `C_∞(t) ← E_t → ∫_{Ty} F`.
- `P(Y, y_0)`: objects `(τ, c)`, `c: I_τ → Y`, `c(0) = y_0`; a morphism `(τ, c) → (ρ, d)` is `(φ, η)` with
  `φ: τ → ρ` in `Ty` and `η: c ⇒ dφ`, `η_0 = id`; `q: P(Y, y_0) → Y` takes the end point, and `q(φ, η)` is the last
  component of `η`; `o` is the empty path. `R_0`: the walking retraction (objects `0, z`; `u: 0 → z`, `r: z → 0`,
  `ru = id_0`, `e = ur ≠ id_z`).
- `FreeMon ⊂ Mon`: free monoids with all monoid homomorphisms. For `M: A → FreeMon`, `q_M: ∫_A M → colim^{Mon}_A M`
  is the canonical functor to the colimit taken in `Mon`; `M_ab: A → Ab` is the abelianization, and `M^{gp}` the
  diagram of free groups on the same bases.

**The results.** None of these is to be proved again as if open. For each one you use: read the proof at the
place given and confirm the step you rely on in a paragraph of your own, or give the exact error with a repair or a
counterexample. "Checked" means: followed in full by the review named (Claude Opus 5.5 at effort max for PRETOT and
TOTEX; the Dérivateurs expert, Claude Fable 5.2 at effort max, for TOTASPH; the intake by Claude Fable 5.2 at
effort high for PATHS).

- **R1 (TOTASPH C.5; TOTEX A.1; checked).** For `A` non-empty and connected: total ⟺ total for `W_Z` ⟺ every
  action component is weakly contractible ⟺ every action component is integrally acyclic ⟺ `hocolim_A X → colim_A X`
  is a weak equivalence for every `X: A → sSet`. So `𝒬_∞` is the class of total categories.
- **R2 (TOTASPH D.12 = PRETOT C.1, C.2; checked).** For `n ≥ 2`: `A` is total for `W_n` iff `A ∈ 𝒬_n` and `BA` is
  `n`-connected. A presheaf `H` on `U` is totally `W_n`-aspherical iff `B(U/H)` is non-empty and `n`-connected and
  every component `D` of every restricted action has `H̃_q(BD; Z) = 0` for `1 ≤ q ≤ n − 1` (PRETOT C.1). If `A` is
  total for `W_n` and `V ⊂ A` is a non-empty cosieve, then `V ∈ 𝒬_n`, and `V` is total for `W_n` iff
  `H_n(BV; Z) = 0` (PRETOT C.2). Totally `W`-dwyérienne sieves compose iff non-empty cosieves of categories total
  for `W` are total for `W` (TOTASPH F.9; re-checked in PRETOT C.4).
- **R3 (TOTASPH C.11; Isbell–Mitchell 1976, Lemmas 2.1, 2.2, Prop. 2.3; Adámek–Koubek–Reiterman 1981, Theorem [1];
  TOTEX A.4, B.5, B.6; checked).** A non-empty connected category is quasi-filtered iff all its action components
  are simply connected iff all of them have `H_1 = 0`. So `𝒬_2` is the class of quasi-filtered categories.
- **R4 (TOTASPH C.12, C.13, D.13; known: Isbell–Mitchell 1976, Th. 4.1, Cor. 4.4).** A quasi-filtered category with
  a weakly terminal object is filtered. So no category with a weakly terminal object, none with finitely many
  objects and no preorder separates any two of the classes `𝒬_n`.
- **R5 (TOTEX D.21–D.26; checked, followed and not recomputed).** Total and exact are each preserved by final
  images, finite products, opfibrations with total (exact) base and fibres, passage to action components, non-empty
  cosieves, localization, idempotent completion, and filtered colimits along final functors.
- **R6 (known: Isbell–Mitchell 1973, Th. 1, Th. 3, with the proof in Isbell 1974; TOTASPH C.6, C.9–C.10; TOTEX
  E.1–E.6, checked).** Exact ⟺ `Aff_Z(A)` filtered ⟹ total. `Δ_inj` and the coloured-word categories `W_m` (finite
  words in `m` letters, strictly increasing colour-preserving maps) are exact and are neither filtered nor sifted;
  `W_2, W_3, W_4` are pairwise inequivalent and admit no final functor from `Δ_inj^r × I`, `I` filtered.
- **R7 (TOTEX D.4 = PRETOT F.3; TOTEX D.5 = PRETOT F.6; TOTEX D.7, D.9, D.10; PRETOT F.1, F.2, F.4, F.5; checked).**
  Sifted and total ⟹ filtered. For non-empty connected `A`: `∫_A D → colim^{Cat}_A D` is a weak equivalence for all
  `D: A → Cat` iff `A` is filtered iff the same holds for diagrams of groups iff for diagrams of right-angled Artin
  groups (F.4); for arbitrary `A` the condition means that every component is filtered (F.1). Diagrams of abelian
  groups with colimit in `Ab` already detect filteredness (F.6). For `n ≥ 1`, homotopy colimits over `A` preserve
  `n`-types iff every comma category of `A → ΠA` is filtered (TOTEX D.9–D.10).
- **R8 (PRETOT A.1, A.2, A.5, A.10; checked, A.5 recomputed by the reviewer's own code).** A.1:
  `H_i(B El_{U/H}(Lπ); Z) ≅ Tor_i^{ZU}(Z[H], Z[L])`; if `Z[H]` is projective or flat and `U/H` is non-empty and
  connected, `H` is totally `W_Z`-aspherical. A.2: a simplicial set `K`, as a presheaf on `Δ`, is totally
  `W_Z`-aspherical iff `|K|` is acyclic iff `K` is non-empty, connected and `Z[K]` is projective; totally
  `W∞`-aspherical iff `|K|` is weakly contractible. A.5: for the free degeneracy completion `K` of the
  two-dimensional presentation complex of `⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩`, the right act `K_2` (52 elements) over
  `End_Δ([2])` (ten elements) is totally `W_Z`-aspherical and `π_1 B(End_Δ([2])/K_2) ≅ SL(2,5)` (the group was
  identified by the reviewer). A.10: on a base with a finite height function a presheaf is totally `W_Z`-aspherical
  iff it is representable.
- **R9 (PRETOT B.2–B.4; checked).** Finite sieves separating Dwyer, totally dwyérienne, dwyérienne, discretely flat
  (Hackney–Ozornova–Riehl–Rovelli: the definition labelled `discretely flat` in the attached source, cited
  as Definition 3.4 by the review) and homotopical-cofibration sieves; `W∞`-dwyérienne sieves do not
  compose; strictly and totally aspherical functors compose for every fundamental localizer, and totally
  `W∞`-dwyérienne sieves compose (B.4).
- **R10 (PRETOT E.3–E.8; checked).** `Ty` is filtered (E.4). `q: P(Y, y_0) → Y` is totally `W∞`-aspherical iff `Y`
  is a connected thin groupoid, that is, equivalent to the point (E.6). If `q` is strictly `W∞`-aspherical then
  `|Y(y_0, y)| ≤ 1` for all `y`, and for preorders and for groupoids strict is equivalent to connected thin groupoid
  (E.7). On the full subcategory `P_{≤1}` of `P(R_0, 0)` of paths of length at most one the end-point functor is
  strictly and not totally `W∞`-aspherical (E.8). For `P(R_0, 0)` itself: `o` is terminal, and `P(R_0, 0)/z` is
  contractible (text after E.9).
- **R11 (PRETOT F.9; checked).** With colimits of free monoids taken in `Mon`: `q_M ∈ W∞` for every `M` if `A` is
  filtered; if `q_M ∈ W∞` for every `M`, then `A` is non-empty, connected and total; for the diagrams `M = F(S)`
  with `S: A → Set` (basis maps) total is also sufficient, and `H_{k+1}(B∫_A F(S)) = H_k(El_A S)`.
- **R12 (`Ty^op`; the Dérivateurs expert, 12 Nov 2026, three lines and `ty_check.py`; statement C.27 of checkpoint
  02 of TOTAL_EXACT_2, read by nobody on our side).** In `Ty` let `e, c: (+−+) → (++)` have the letter maps `(1, 3)`
  and `(1, 1)`. There are no type `σ` and `g, h: σ → (+−+)` with `eg = ch`: the letter map of `g` is strictly
  increasing (the signs alternate), so that of `eg` is injective, and that of `ch` is constant. So `Ty^op` fails I,
  is not total and not exact, and the presheaf `σ ↦ Ty(σ, (++))/(eg ∼ cg)` on `Ty` has a category of elements with
  `H_1 = Z`. The wide subcategory of `Ty^op` of injective letter maps is `W_2` (exact: R6); the preorder `R^op` is
  directed (PRETOT F.12).
- **R13 (PATHS A.2–A.4, C.P1–C.P3; all followed in the intake, C.P1–C.P3 step by step).** A.2 (= PRETOT F.13):
  `E_t → C_∞(t)` is a weak equivalence for every `F` and `t`. A.3: for `u: J → T`, `∫_J Fu → ∫_T F` is a weak
  equivalence for every `F: T^op → Cat` iff every `u/t` is weakly contractible; for `T = Ty` and a cofinal sequence
  this fails (remark of the drafter, from PRETOT F.12: for the representable presheaf of `(+)`, `∫ = Ty/(+)` is
  contractible and `colim_n Ty(t_n, (+))` has more than one element). A.4 (= PRETOT F.14; Grothendieck's own example at VII ms. 109): cofinality in the preorder
  does not suffice for a general fibred category. C.P1: each `P(τ, σ)` is empty or contractible, and `𝕋y` acts
  strictly on the path categories `τ ↦ F_τ(a, b)` of a category `M` with a wide subcategory `Σ` (interior vertical
  arrows arbitrary). C.P2: the diagram `τ ↦ BF_τ(a, b)` on `Ty^op` descends coherently to `R^op`, and over `R^op`
  both `Ty^op` and every cofinal sequence are homotopy final. C.P3: for the path diagrams the comparison is a pair
  of weak equivalences for every cofinal sequence, canonical and transitive in `Hot`.
- **R14 (checkpoint 02 of TOTAL_EXACT_2, statements C.24 and D.1; a run in progress, reviewed by nobody).** For a
  specified choice of targets in the repaired Adámek–Koubek–Reiterman construction, the union `A = ⋃ K_m` is
  quasi-filtered and `H_2(B El_A(h_V/(bv_1 ∼ bv_2)); Z) ≠ 0`. So `{total} ⊊ {quasi-filtered}`.
- **R15 (corrections of the reviews).** PRETOT A.12 is known (Isbell–Mitchell 1973; TOTASPH C.10); D.4 is
  Cisinski 1999; G.1 is POLES G.19; G.2 is Grothendieck's own footnote 7 at XIIapp ms. 11; F.14 is his example at
  VII ms. 109; the title of C.3 says `n ≥ 2` and its statement `n ≥ 1`; in G.3 the remark is at XII ms. 96 and the
  supporting argument is in E.7. PRETOT F.16 is closed by PATHS C.P1–C.P3. TOTASPH C.13 and TOTEX A.5 are
  Isbell–Mitchell 1976, Cor. 4.4, which both returns label "Proved" without the citation; TOTEX D.5 is PRETOT F.6.

- **R16 (literature found by the drafter's search of 13 Nov 2026; only Gray–Steinberg was opened, at the places
  named; the statements of the others are taken from secondary sources and are to be checked in the originals).**
  For Part D: McDuff, *On the classifying spaces of discrete monoids*, Topology 18 (1979): every path-connected space
  has the weak homotopy type of the classifying space of a discrete monoid, so asphericity of a colimit monoid is
  not automatic. Fiedorowicz, *Classifying spaces of topological monoids and categories*, Amer. J. Math. 106 (1984),
  §§4–5: the classifying space of an amalgamated free product of discrete monoids as a homotopy pushout, under
  flatness hypotheses. Gray–Steinberg (attached; abstract and the passages on amalgams read): theorems of
  Bass–Serre type for amalgamated free products of monoids under freeness or flatness hypotheses, using McDuff; they
  state that Lemma 5.2 (a) of Fiedorowicz 1984 does not hold. For Parts A and D: Adámek–Reiterman, *Exactness of the
  set-valued colim*, Comment. Math. Univ. Carolinae 17 (1976) (open at dml.cz): when `colim: Set^A → Set` preserves
  equalizers. For Part B: Dwyer–Kan, *Calculating simplicial localizations*, J. Pure Appl. Algebra 18 (1980):
  hammocks of a fixed type and the passage to all types. For Part C: Evrard, *Fibrations de petites catégories*,
  Bull. Soc. Math. France 103 (1975) 241–265 (the reference as given in Shoikhet's bibliography). For Part E:
  Kervaire, *Smooth homology spheres and their fundamental groups*, Trans. AMS 144 (1969): the finitely presented
  groups with `H_1 = H_2 = 0` are the fundamental groups of homology `n`-spheres, `n ≥ 5`; Higman's four-generator
  group has an acyclic and aspherical presentation complex. The searches found no source for Leads 1, 2, 3 or 5.

## Leads

Each is an inference of the model named. The drafter checked them on 13 Nov 2026 as far as stated under "Status"
at each Lead; nobody else has checked them, and each is to be proved or refuted in full. The derivations are in
`LEADS_DERIVATIONS.md`. Expected answer for every statement of a Lead: true, except where the Lead itself says
otherwise.

- **Lead 1 (drafter; the cone on a quasi-filtered category).** (a) Every action component of a member of `𝒬_n` is
  in `𝒬_n` (discrete opfibrations compose). (b) For `E ∈ 𝒬_n` the category `E^◁` is total for `W_n`, and `E` is a
  non-empty cosieve of it. (An action component of `E^◁` is an action component `D` of `E` with cones attached
  along sections `E → D`, whose images are cosieves of `D` isomorphic to `E`; `D` and `E` are `(n−1)`-connected.)
  (c) Hence, for each `n ≥ 2`, the implication of PRETOT C.4 (`A` total for `W_n`, `V ⊂ A` a non-empty cosieve
  ⟹ `H_n(BV) = 0`) holds iff `H_n(BE) = 0` for every `E ∈ 𝒬_n`, iff `𝒬_n = 𝒬_{n+1}`; and it holds for all
  `n ≥ 2` iff every quasi-filtered category is total. (d) With R14 it fails for `n = 2`: for
  `E = El_A(h_V/(bv_1 ∼ bv_2))` the category `E^◁` is total for `W_2` and its cosieve `E` is not. PRETOT's attempt
  (the cone on a sphere poset) failed because that poset is not quasi-filtered.
  Status: (a)–(c) re-derived a second time against the proofs they use, all read in full (PRETOT C.1, C.2; TOTEX
  D.21, D.23); no program, since by R4 no finite example exists. (d) is conditional on R14: the drafter read the
  statement and proof of C.24; its proof rests on C.5, C.10, C.16, C.20, C.21, C.23 of the checkpoint, which were
  not read; its first-stage value `H_2 ≅ Z` agrees with the review of TOTEX.
- **Lead 2 (drafter; strict end-point functors).** Let `u: y_0 → z` be an arrow of `Y`, `P = P(Y, y_0)`,
  `H = Y(q(−), z)`, `d = ((+), y_0 →u z)`, `p = ((++), y_0 →id y_0 →u z)`, and let `f, g: p → d` lie over the type
  maps with vertex maps `(0, 1, 1)` and `(0, 0, 1)`, with components `(id, u, id_z)` and `(id, id, id_z)`. Put
  `L = P(p, −)/(kf ∼ kg)`. Then by R8 (A.1)
  `H_1(El_{P/H}(Lπ)) ≅ Z[Y(z, z)] / span{γv : γ ∈ Y(y_0, z), v ∈ Y(z, y_0), vu = id}`:
  for `x` of non-empty type, `kf` and `k'g` have different type maps for all `k, k': d → x`, and the arrows
  `d → o` are the retractions `v` of `u`, each of which equalizes `f` and `g`. This group is zero only if `u` is
  invertible. The same computation for `v: z → y_0` with `((−), y_0 ←v z)` and `((−−), y_0 ←v z ←id z)` gives
  `Z[Y(z, z)] / span{γv : γ ∈ Y(y_0, z)}`, zero only if `v` has a left inverse. Hence, as in the proof of PRETOT
  E.6: `q` is strictly aspherical for `W∞`, for `W_Z` or for some `W_n`, `n ≥ 2`, iff `Y` is a connected thin
  groupoid; strict and total coincide for end-point functors of full path categories. For `R_0` the group is `Z`
  (the class of `id_z` modulo `e = ur`), so `P(R_0, 0) → R_0` is not strictly aspherical. For `Y = R_0` the weight
  splits: `Z[H] ≅ Z[P(−, o)] ⊕ q^*S` with `S` the right `ZR_0`-module `S(z) = Z`, `S(0) = 0`, `e` acting by `0`.
  Status: checked by program for `R_0`, both pairs (`checks_drafter/`): on the paths of length at most 2 the
  homology of the nerve of `El_{P/H}(Lπ)`, computed from the definition, has `H_1` of dimension 1 over `F_2`, `F_3`,
  `F_5`, `F_7` and `F_1000003`; on the paths of length at most 3 the integer kernels give the span `Z·e` exactly.
  The step for paths of every length and the classification for all `(Y, y_0)` are the derivation, re-read.
- **Lead 3 (drafter; free monoids over exact shapes).** For `A` total and `M: A → FreeMon`:
  `H_{k+1}(B∫_A M; Z) = T_k(M_ab)` for `k ≥ 0`, and `π_1 B∫_A M = Γ := colim^{Grp}_A M^{gp}`. If `A` is exact,
  `B∫_A M` is a `K(Γ, 1)` (the `Γ`-coverings of the graphs `BM(a)` have homology in degrees `0, 1` only, and all
  `T_k`, `k ≥ 1`, vanish). The same holds for every diagram of free groups, so diagrams of free groups with
  colimit in `Grp` do not detect filteredness, in contrast with right-angled Artin groups (R7). So for exact `A`:
  `q_M ∈ W∞` iff the monoid `C = colim^{Mon}_A M` has `BC ≃ K(C^{gp}, 1)`. On `Δ_inj` and `W_m` the question of PRETOT F.10 is therefore whether a colimit monoid of
  free monoids can fail to be aspherical. First example, computed by hand and checked by nobody: `M([n])` free on
  the `n + 2` edges of the interval `{−∞} ∪ [n] ∪ {+∞}`, an injection sending an edge to the product of the edges
  between the images of its end points; then `C = ⟨x, y, z | xy = x, y² = y, yz = z⟩`, `C^{gp}` is free on `x, z`,
  and `H_2(BC) = 0`: this diagram does not separate in degree 2. No expected answer for PRETOT F.10 itself.
  Status: re-derived against the proofs it uses, read in full (PRETOT F.9; TOTEX E.2 for the exactness of `W_m`,
  E.3 for the Artin-group diagram that does separate); the example is a hand computation, not machine-checked; no
  source found (R16 has the literature on classifying spaces of colimits of monoids).
- **Lead 4 (Claude Opus 5.5, review F13; (b)–(d) drafter).** For `n ≥ 1` put `M_n = End_Δ([n])`. (a) For every
  simplicial set `K` of dimension at most `n`, the functors `M_n/K_n → Δ_{≤n}/K → Δ_inj/K^{nd}` of PRETOT A.4 are
  weak equivalences, so `B(M_n/K_n) ≃ |K|`. (b) The right act `K_n` is totally `W_Z`-aspherical iff `|K|` is
  acyclic iff `Z[K_n]` is a projective `ZM_n`-module and `|K|` is non-empty and connected; it is totally
  `W∞`-aspherical iff `|K|` is weakly contractible. (c) Every right `M_n`-act is isomorphic to `K_n` for a
  simplicial set `K` of dimension at most `n`, unique up to isomorphism (the idempotent completion of `M_n` is
  `Δ_{≤n}`); so (b) classifies the totally aspherical acts over `M_n`. (d) The groups `π_1 B(M_n/H)`, `H` a finite
  totally `W_Z`-aspherical act: for `n = 1` only the trivial group; for `n = 2` the fundamental groups of finite
  acyclic 2-complexes; for `n ≥ 3` the finitely presented groups `G` with `H_1(G) = H_2(G) = 0`.
  Status: (a)–(c) re-derived against PRETOT A.1, A.2, A.4, A.5 and TOTEX D.24, all read in full; no program beyond
  the reviewer's for `n = 2`. (d) rests on the theorem of Hopf and, for comparison, on Kervaire 1969 (R16, not
  opened).
- **Lead 5 (the Dérivateurs expert's suggestion; the conditions and (b) drafter).** For `F: Ty^op → Cat` consider:
  (2F) `F` extends to a strict 2-functor on `𝕋y`, or is joined to such a functor by a zigzag of natural
  transformations that are weak equivalences at every type; (DESC) the diagram `τ ↦ BF(τ)` on `Ty^op` is
  equivalent, as a homotopy-coherent diagram, to one pulled back from `R^op`; (LOC) for every type `r` the
  inclusion of the fibre `F(r) → ∫_{r↑} F` is a weak equivalence; (𝒟) the comparison for `(F, t)` is a pair of
  weak equivalences for every cofinal sequence `t`; (𝒟₁) for one cofinal sequence. (a) (2F) ⟹ (DESC) ⟹ (𝒟) ⟹
  (𝒟₁): the proofs of PATHS C.P2–C.P3 use of the path diagrams only the strict action of `𝕋y` (the enriched
  diagram descends to `R^op` because the hom-posets are empty or contractible; `Ty^op` and every cofinal sequence
  are homotopy final over `R^op`). (b) `E_t → ∫_{Ty} F` is the sequential homotopy colimit of the inclusions
  `F(t_n) → ∫_{t_n↑} F`; so (LOC) ⟹ (𝒟), (𝒟) is a condition at infinity, and the drafter expects (𝒟) ⇏ (LOC).
  (c) (DESC) ⟹ (LOC) holds iff the categories of Part B.4 are weakly contractible; no expected answer (for
  `r = s = (+)` the category is `Δ^op`). The expert's suggestion is that (𝒟) holds exactly for the diagrams on which
  `𝕋y` acts. For presheaves of sets, (2F) says that the presheaf factors through `R`.
  Status: (a) checked against the proofs of PATHS C.P1–C.P3, read in full; the first draft of this Lead passed
  through (LOC), which the reading showed to need Part B.4. (b) and (c) re-derived, no independent check.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (objects, arrows, composition, the verification of every hypothesis and of the
failure; checked by a program when finite or finitely presented) and the strongest true statement proved in its
place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the
obstruction as an exact statement and the smallest undecided instance are the state of an item you are still
working on: record them as you go, then attack the obstruction, starting from that instance. "Known" counts only
with the derivation of the statement used here from the cited theorem, after opening the source. An item that
begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is the whole
answer.

For Part A in particular. A separation `𝒬_n ≠ 𝒬_{n+1}` is one category given completely, with a proof that
**every** component of **every** `El_E(L)` is `(n−1)`-connected, for all `L: E → Set`, and a named class in
`H_n` of a named action component with a proof that it is not zero. An equality `𝒬_n = 𝒬_{n+1}` is a proof for
every member of `𝒬_n`.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1–R16 again in place of
the items; a statement about all `n` proved for some `n`; a claimed member of `𝒬_n` whose action components are
controlled only for finitely many actions, only in homology, or only on finite stages of an infinite construction;
a statement about all `F: Ty^op → Cat` proved only for presheaves of sets or only for the path diagrams; a
statement about all `(Y, y_0)` proved only for `R_0`; a statement about all diagrams of free monoids proved only
for basis maps; restricted actions replaced by arbitrary actions on `U/H`, or the reverse, without saying so; a
step that replaces a claim by a convenient special case without naming it.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `DER_FOLLOWUP_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The tower of truncated totality (PRETOT C.4). The main question is A.3.**
1. Prove or refute Lead 1 (a), (b), (c), each step.
2. **[TOTAL_EXACT_2]** Decide the implication of PRETOT C.4 for `n = 2`. By Lead 1 (c) it is the question whether
   some quasi-filtered category `E` has `H_2(BE) ≠ 0`, which is Parts C.1 and D.1 of TOTAL_EXACT_2. Read statement
   C.24 of its checkpoint 02 and its proof in full (`sections/akr_*.tex`), confirm each step with your own argument
   or give the exact error, and write out the counterexample of Lead 1 (d): the category `E^◁`, its cosieve, and
   both verifications.
3. For every `n ≥ 3`, prove or refute: `𝒬_n ≠ 𝒬_{n+1}`; that is, there is a non-empty connected category all of
   whose action components are `(n−1)`-connected, one of which has `H_n ≠ 0`. The answer must cover every `n ≥ 3`.
   We have no expectation that we trust; the drafter expects a separation at every `n`. Routes known to us, not
   items: attach to the stages of a construction of the kind of R14 cones over diagrams of dimension at most
   `n − 1` that kill every class of degree below `n` in every action component, and show that a class of degree `n`
   survives (statements C.2, C.5 and C.26 of the checkpoint: a cone over a diagram of dimension `d` whose strict
   colimit of representables is its homotopy colimit kills no class above degree `d`; totality is a finite test on
   spheres); joins and products of categories that separate lower levels; for an equality, a proof that vanishing
   of `π_i`, `i < n`, of all action components forces vanishing of `H_n`, which for `n = 2` is false by R14.
4. State and prove the consequences for each `n ≥ 2`: whether non-empty cosieves of categories total for `W_n` are
   total for `W_n`; whether totally `W_n`-dwyérienne sieves compose (R2); the inclusions among the classes of
   categories total for `W_n`, `n ≥ 1`, and `𝒬_n`, each decided as an equality or as strict with its example; and
   the corrected statement for XII ms. 113–114.

**B. Fibred categories over the types (VII ms. 99–115).**
1. **[TOTAL_EXACT_2]** Prove or refute R12, each of its three lines, with the value `H_1 = Z`. (This is Lead 8 of
   TOTAL_EXACT_2.)
2. Determine the class of all `F: Ty^op → Cat` that satisfy (𝒟): a condition on `F`, necessary and sufficient,
   with both directions proved. Decide whether (𝒟₁) implies (𝒟).
3. Prove or refute each implication between two of the conditions (2F), (DESC), (LOC), (𝒟), (𝒟₁), in both
   directions, starting with those of Lead 5 (a), (b), (c); for every implication that fails give an explicit `F`. Do the same within presheaves of sets on `Ty`, and determine the
   presheaves of sets `S` on `Ty` for which `Ty/S` has contractible components indexed by `colim_n S(t_n)` for every
   cofinal sequence.
4. Prove or refute: for types `r ≤ s` in `R`, the full subcategory of `Ty` on the types `τ` with `r ≤ τ ≤ s` is
   weakly contractible. (Compare the comma categories of the finality statement in PATHS C.P2.)
5. State what B.2 and B.3 give at VII ms. 103 (b), 109–110, 112–114: the fibred categories over `Ty` for which
   `C_∞ → C` is an isomorphism in `Hot`, and for which it is not, with the example for each sentence of
   Grothendieck that is corrected.

**C. Strictly aspherical end-point functors (PRETOT E.9).**
1. Prove or refute Lead 2 for `(Y, y_0) = (R_0, 0)`: the object `p`, the morphisms `f, g`, the action `L`, the
   group `H_1(El_{P/H}(Lπ)) ≅ Z`, and the conclusion that `P(R_0, 0) → R_0` is not strictly `W∞`-aspherical. Check
   the finite part of the computation by a program of your own, and read the drafter's (`checks_drafter/`): say
   whether it computes what Lead 2 claims.
2. Determine all pointed small categories `(Y, y_0)` for which `q: P(Y, y_0) → Y` is strictly `W∞`-aspherical.
   Expected (Lead 2): exactly the connected thin groupoids.
3. Determine the same class for `W_Z`, for each `W_n`, `n ≥ 2`, for `W_1` and for `W_0`.
4. State the consequence for XII Définition 2 (ms. 109) and for ms. 101–103: for which `Y` the end-point functor of
   the path category is aspherical, strictly aspherical, totally aspherical, each class determined.

**D. Free monoids as test diagrams (PRETOT F.10).**
1. Prove or refute: a non-empty connected small category `A` such that `q_M ∈ W∞` for every `M: A → FreeMon`, the
   colimit taken in `Mon`, is filtered. A refutation is one non-filtered `A` with a proof that `q_M ∈ W∞` for all
   `M`; a proof gives, for every total `A` that is not filtered, a diagram `M` with `q_M ∉ W∞`, whether or not `A`
   is exact.
2. Prove or refute Lead 3, each statement, including the hand computation.
3. Prove or refute: for every `M: Δ_inj → FreeMon` the monoid `colim^{Mon}_{Δ_inj} M` has an aspherical
   classifying space. (With Lead 3 this decides whether `Δ_inj` passes the test of D.1.)

**E. Totally aspherical acts over `End_Δ([n])` (PRETOT A.5 for every `n`).**
1. Prove or refute Lead 4 (a), (b), (c) for every `n ≥ 1` and every simplicial set of dimension at most `n`, finite
   or not.
2. Determine, for each `n ≥ 1`, the class of groups `π_1 B(M_n/H)` for `H` a finite totally `W_Z`-aspherical right
   `M_n`-act, and the same without finiteness. Expected: Lead 4 (d).

**F. Statement of results.**
1. The corrected statements, each with the manuscript place and with what the returns already proved: II ms. 36ter
   (the classes `𝒬_n`, total, exact, filtered); XII ms. 93–97, 101–103, 109–114; VII ms. 99–115.
2. The literature record: for every source named in this prompt and every source you use, one line: opened, with
   the numbers of the theorems that contain or come closest to each statement you prove; or not obtained, with
   what you tried. Say nothing about the content of a source you did not open. Say what you searched for each of
   A.3, B.2, C.2, D.1 and E.2.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: quantifiers, size conditions, variance, which localizer, which
   numbered condition in which version. Do not replace it by a convenient special case. If you prove a special
   case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property
   you use (natural in which variable, a map of acts or only of modules, a functor over which base). Compositions
   must type-check; an element of a colimit is a finite sum of classes of elements at possibly different objects.
3. Every reduction ("we may assume", "replace by") comes with its comparison map and a proof that the exact
   property needed transfers in the direction needed. Passing to a nerve, a cosieve, an action component, a stage
   of a union, a truncation of a path category or a homotopy category transfers nothing by itself.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories; weak equivalence of
   a specified map; an isomorphism in `Hot`; an isomorphism on homology. An abstract isomorphism is not the
   canonical map.
5. Check the edge cases in scope: empty categories and empty presheaves, several components, the empty type and
   the empty path, types with one sign, categories with idempotents or endomorphisms, `n = 1` and `n = 2`, infinite
   simplicial sets.
6. A counterexample is given completely and, when finite or finitely presented, checked by a program whose code
   and output you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone
   shows a gap, not falsity; keep the two apart.
7. No authority. Grothendieck's assertions, the returns TOTASPH, PRETOT, TOTEX and PATHS, their reviews, the
   checkpoint of TOTAL_EXACT_2, the results R1–R16 and the Leads (inferences by Claude, Anthropic) are all to be
   checked where used; the Leads in full. If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails,
   and you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

## What to deliver

One ZIP containing:
- `DER_FOLLOWUP_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts,
  every statement numbered and labelled Proved / Refuted / Known (with citation), with complete proofs; English,
  first person plural; quote Grothendieck in French where his wording matters.
- `DER_FOLLOWUP_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `DER_FOLLOWUP_references.bib`: each entry marked opened / not opened.
- `DER_FOLLOWUP_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or
  refuted, with the statement number); then what you read, what you computed, every correction to R1–R16, to the
  Leads, to the reviews, to the checkpoint of TOTAL_EXACT_2 and to the transcription.
- `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

If the execution environment disconnects: wait and retry for ten minutes; then write every file out in the chat in full, each in its own code block, and continue the remaining parts in the chat until every part is written.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `DER_FOLLOWUP_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
