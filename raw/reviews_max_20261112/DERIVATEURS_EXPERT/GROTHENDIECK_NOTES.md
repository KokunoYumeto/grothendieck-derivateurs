# Grothendieck, *Les Dérivateurs*: reading notes

Reader: Claude Fable 5.2 (effort max), 12 Nov 2026 onward. Source read: `corrected_french_20261111\DER_*.tex`
(checked French transcription of the Künzer–Malgoire–Maltsiniotis edition). Locations are "chapter ms. N"
(manuscript page, the `\msp{page N}` marks), which is how the prompts and returns cite the text.

Reading log (what was read in full, in which order) is at the end of this file. A part not listed there was NOT read.

## Global conventions of the manuscript (fixed in Chapter I, used throughout)

- Coefficients on an index category `I` are *presheaves*: the model case is `D_{M,Σ}(I) = Hom(I°, M)[Σ_I^{-1}]`
  (I ms. 12, 42). So `(f_* F)_y = Γ(X/y, F|X/y)` (Der 4 (g), I ms. 46) and `(f_! F)_y` is computed on `y\X`.
- `f_*` right adjoint of `f^*` = "image directe cohomologique"; `f_!` left adjoint = "image directe homologique".
  "Dérivateur à gauche": has all `f_*` (I ms. 6, 44); "à droite": has all `f_!`. (Opposite of today's usage,
  where a *right* derivator has right Kan extensions... in fact it agrees: his "à gauche" = left *exact* side.)
- Open immersion ("immersion ouverte") = inclusion of a sieve; closed immersion = inclusion of a cosieve (I ms. 1-2, 7).
- `X/y` (for `f: X → Y`) = pairs `(x, f(x) → y)`; `y\X` = pairs `(x, y → f(x))`.
- "hot-équivalence stricte": all `X/y` contractible (later: *asphérique*); "costricte": all `y\X` contractible
  (later: *coasphérique*) (I ms. 32, 65 and footnote 27).
- "cohomologiquement cofinal" `α: X' → X`: all `x\X'` contractible (I ms. 47). With presheaf coefficients this is
  exactly what makes `Γ(X, F) → Γ(X', α^*F)` an isomorphism for all `F`.

## Chapter I. Généralités sur les (pré)dérivateurs (I-a: ms. 1–66; I-b: ms. 67–126)

### I §1 (ms. 1–3). Presheaf categories and multiple adjoints
- `A(I) = Hom(I°, A)`; for `f: I → J` the chain `f^? ⊣ f_! ⊣ f^* ⊣ f_* ⊣ f^!` when it exists.
- (a) `f_*`, `f_!` exist given the relevant limits. (b) Bi-adjoints need not exist even for `A = Ab` (examples with the
  three-element posets). (c) `f` closed immersion and `A` pointed ⇒ `f^!` exists; `f` open ⇒ `f^?` exists; for an
  immersion `f_*`, `f_!` are fully faithful. (d), (e) Gluing squares for complementary `i: Y → S ← U : j`
  (closed/open): square (1) `j_!j^*F → F → i_*i^*F` bicartesian over `e` in the pointed case; square (2)
  `i_*i^!F = Ker(F → j_*j^*F)`. (f) The simplex categories `Δ_i`: adjoint strings of length `2i+7` (editors: not
  quite true as stated).

### I §2 (ms. 4–32, then restart ms. 41–60). Heuristics and axioms
- ms. 4–5: `Dia ⊂ Cat` full, containing at least the posets; a derivator is a strict 2-functor `D: Dia° → Cat`
  (contravariant on 1-cells and on 2-cells: `u: f → g` gives `u^*: g^* → f^*`).
- ms. 6: **Der_1** `f^*` has both adjoints. Left derivator: all `f_*`, and `f_!` only for open immersions. Right
  derivator: all `f_!`, and `f_*` for closed immersions. "Ce sont sans doute les dérivateurs à gauche qui sont les
  plus importants."
- ms. 7: **Der_2** bi-adjoints `f^!` (closed immersions), `f^?` (open immersions); footnote: only for pointed
  derivators, "HOT n'y satisfait pas". **Der'_2**: `D(I ⊔ J) ≃ D(I) × D(J)`.
- ms. 8–10: `D(I × J) → Hom(J°, D(I))`; "la philosophie des dérivateurs": every diagram of type `K` in `D(I)` that
  arises naturally should come canonically from an object of `D(I × K°)`. The gluing squares (1), (2) are to be
  lifted to `D(I × Δ_1 × Δ_1)`.
- ms. 11: base category `A_D = D(e)`; **Der_3**: `D(I) → Hom(I°, A)` is conservative (footnote: "n'a aucune envie
  d'être fidèle").
- ms. 12–13: all known derivators come from `(M, Σ)`: `D_{M,Σ}(I) = M_I Σ_I^{-1}`. Existence of `f_!, f_*` is
  attributed to Thomason for Quillen model categories. `HOT` := the derivator of simplicial presheaves; base `Hot`.
- ms. 14–16: morphisms of derivators; left exact = commutes with `f_*`, right exact = commutes with `f_!`. `HOTAB`,
  abelianization `HOT → HOTAB` (footnotes: not left exact).
- ms. 17: dual derivator `D°(I) = D(I°)°`. ms. 18–21: induced derivator `D_I(J) = D(I × J)`; `f^*`, `f_*`, `f_!` as
  morphisms `D_{I'} → D_I`, `D_I → D_{I'}`.
- ms. 23–29: `f^*` is exact; `f_*` left exact, in general not right exact (presheaves of sets; an abelian example
  with the square minus its terminal vertex). **Perplexité** (ms. 29): a notion of "dérivateur triangulé" for which
  left and right exactness of morphisms coincide.
- ms. 29–32: base-change morphism `c_γ: p^* f_* → f'_* q^*` for a square with a 2-cell `γ: fq → pf'`. **Der_4**
  (first form): iso for the square `I/j_0 → I, e → J`. **Der_5** (first form, ms. 32): `f` strict hot-equivalence ⇒
  `f^*` fully faithful — his own footnote: "totalement canulé", true only for constant coefficients. ms. 33–40
  suppressed by him.
- ms. 41–52 (the restart; these are the axioms he uses later):
  - prederivator = 2-functor on `Dia`; `Dia` contains finite posets, is stable under finite limits and sums and
    complements of open/closed full subcategories.
  - **Der 1**: (a) `D(I ⊔ J) ≃ D(I) × D(J)`, (b) `D(∅)` final. **Der 2**: conservativity of
    `D(I) → Hom(I°, D(e))`. **Der 3 (g)/(d)**: `f_*` / `f_!` exist. **Der 4_0** (ms. 45; becomes a theorem):
    `i_*` fully faithful with image `{F : j^*F final}`; `j_!` fully faithful with image `{F : i^*F initial}`.
    **Der 4 (g)** (ms. 46): `(f_*F)_y ≅ Γ_D(X/y, q^*F)`. **Der 5 (g)** (ms. 47): if all `x\X'` are contractible then
    `Γ_D(X, F) ≅ Γ_D(X', α^*F)`; the variant with `X'/x` is struck out ("Faux!").
  - Cor. 1 (g): `X` contractible ⇒ `M ≅ f_*f^*M`. Cor. 2 (g) (strict hot-equivalence ⇒ `F ≅ f_*f^*F`): struck,
    false except for constant coefficients. Cor. 4 (g) (ms. 49): base change for a 2-square holds if every
    `X'/y' → X/p(y')` is a *costrict* hot-equivalence. Cor. 5 (g): `f` fully faithful ⇒ `f^*f_* ≅ id`. Cor. 3 (ms. 50):
    if `Z` has a final object `e_Z` then `Γ(Z, F) ≅ F_{e_Z}`.
- ms. 53–60. **Homotopically proper / smooth functors.** `f: X → Y` is *homotopiquement propre* when every
  `X_y → X/y` is a costrict hot-equivalence, equivalently every fibre of `x\X → f(x)\Y` is contractible; *lisse* is
  the dual (`X_y → y\X` strict; fibres of `X/x → Y/f(x)` contractible). Stable under base change and composition;
  closed immersions are proper; an equivalence of categories need not be proper; `X → e` and projections are both.
  A proper or smooth map with contractible fibres is a hot-equivalence, strict and costrict (Cor. 2, ms. 56).
  **Théorème (g)** (ms. 56–58): in a cartesian square, base change `p^*f_* → f'_*q^*` is an isomorphism when `f` is
  proper or `p` is smooth. Expected converse; four characterizations a)–d) of proper functors (ms. 59). Product
  squares always satisfy base change (ms. 59–60). The "très gros canular" (ms. 60): `F ≅ f_*f^*F` for a strict
  hot-equivalence holds only for constant `F`.
- ms. 61–66. **D-équivalence** (Déf. 1): `f: X → Y` such that `f^*` is fully faithful on *constant* coefficients;
  ⇔ iso on `H^*_D(−, N)` for all `N ∈ D(e)` (if `p_*` exist) ⇔ iso on `H_*^D(−, N)` (if `p_!` exist) (Prop. 1).
  Homotopic functors (same component of `Hom(X, Y)`) are D-equivalences together (Rem. 2); two-out-of-three (Prop. 2).
  **D-asphérique = D-contractile** (Déf. 2): `X → e` is a D-equivalence. For `D = HOT`: `H^*(X, M) = Hom(hot X, M)`,
  `H_*(X, M) = hot(X) × M`, and HOT-equivalences are the weak equivalences. Second Prop. 2 (ms. 63): for a left
  derivator, equivalent: (a) `f` is a D-equivalence universally under local isomorphisms `Y' → Y`; (b) all
  `X/y → Y/y` are D-equivalences; (c) all `X/y` are D-contractible; footnote: (d) `M_Y ≅ f_*f^*M_Y` for constant
  `M_Y`, (d') the same for *locally constant* coefficients. Prop. 2′ dual. Déf. 3: strict D-equivalence =
  "D-asphérique", costrict = "D-coasphérique" (footnote 27). Prop. 4 (ms. 66): for a right derivator, if all `y\X` are
  D-contractible then `H^*_D(Y, F) ≅ H^*_D(X, f^*F)` for **all** `F`, and conversely.

(I-b, ms. 67–126: not yet read; see the reading log.)


## Chapter II. Cofinalité (à droite et à gauche) (II-a: ms. 1–53; II-b: ms. 45–99)

### II §1 (ms. 1–10). Cofinalité cohomologique
- `α: C' → C`, `F` a presheaf on `C`; when is `lim_C F → lim_{C'} α^*F` an isomorphism ("α cofinal", SGA 4 I 8.1)?
  Sufficient: every `x\C'` "faiblement filtrante à gauche" (ms. 1); improved in the Remark (ms. 5–6): it suffices
  (and by Prop. 3.2 it is equivalent) that every `x\C'` be 0-connected. The stronger `F ≅ α_*α^*F` needs the same
  for all `C'/x_0 → C/x_0`.
- ms. 3–5: "la bonne philosophie": replace "faiblement filtrante" by "contractile" (spirit of Der_5). **Question**
  (ms. 5): for `α` a costrict hot-equivalence and `F` an abelian presheaf, is `H^i(X, F) ≅ H^i(X', α^*F)`?
- ms. 7–10: the presheaf `π_0(C'/C): x ↦ π_0(x\C')`, with `lim_{C'} α^*F ≅ Hom(π_0(C'/C), F)`; derived analogues
  `RΓ(C', α^*F) ≅ RHom(Lα_!(k_{C'}), F)` and the HOT version; the "internal adjunction formula"
  `α_*(Hom(G', α^*F)) ≅ Hom(α_!G', F)`, reduced to the projection formula `G ⊗ α_!G' ≅ α_!(α^*G ⊗ G')` (stated as
  something to be checked).

### II §2 (ms. 11–36ter). Locally filtered = locally totally 0-connected; the question on total asphericity
- Irreducible / locally irreducible topos; for `X ∈ Cat`: `Top(X)` irreducible ⇔ `Ord(X)` filtering to the left.
  Several of his first equivalences are marked false by himself (counterexample `0 ⇉ 1`).
- Prop. 2.1 (ms. 14): equivalent conditions for `Top(X)` locally irreducible = PS 1 (every cospan `x → s ← y`
  completes to a commutative square).
- Déf. 2.2 (ms. 15–16): faiblement filtrante (= pseudo-filtrante), localement faiblement filtrante (préfiltrante,
  PS 1), filtrante à gauche = cofiltrante (non-empty, PS 1′, PS 2), localement filtrante.
- Prop. 2.3, Déf. 2.4 (ms. 17–18): a topos is **totalement 0-connexe** when products of 0-connected objects are
  0-connected; for `X ∈ Cat`: `X ≠ ∅` and every `x × y ∈ X^` 0-connected, i.e. `diag: X → X × X` is co-cofinal.
  His claim that this implies `W∞`-asphericity is marked **Faux** by himself (footnote 25).
- Prop. 2.5: totally 0-connected ⇒ irreducible. Example: `Δ` is totally 0-connected, not locally irreducible.
- Théorème 2.6 (ms. 19–29) with Cor. 2.7, 2.8, Lemmas 2.9, 2.10, Perplexité 2.11, Cor. 2.12, Déf. 2.13:
  `X` filtering to the left ⇔ `Top(X)` totally 0-connected and locally irreducible; "localement totalement
  0-connexe" ⇔ a generating family of 0-connected objects is locally cofiltering. Conditions c), c′) are strictly
  weaker (footnotes 28–30, 36: `X = B_G`).
- ms. 30–32: a 0-connected locally totally 0-connected topos has trivial coverings and trivial cohomology with
  constant coefficients (spectral sequence of a covering).
- Prop. 2.15 (ms. 32–34; SGA 4 I 8): `X` filtered ⇔ the final object of `X^` is ind-representable.
- **Cor. 2.16** (ms. 34): for a fundamental localizer `W` with the limit axiom Loc (8), filtered and cofiltered
  categories are `W`-aspherical. **Cor. 2.17**: under the same hypothesis every filtered category `X` is
  **totalement W-asphérique**: for every `f: X → Y` the presheaf `f_!(e_X) = (y ↦ π_0(y\X))` on `Y` is
  `W`-aspherical; in fact `Y/f_!(e_X)` is filtered (it is the filtered colimit of the `Y/f(x_i)`). Cor. 2.18:
  `F ∈ X^` is ind-representable ⇔ `X/F` is filtered.
- **Question (ms. 36)** [audit row II-C-003]: if `X` is totally `W∞`-aspherical (equivalently: every `Y` receiving
  a functor `X → Y` with all `y\X` 0-connected — a *cofinal* functor in his sense, Déf. 3.3 — is `W∞`-aspherical),
  is `X` filtered? "Ça ne m'étonnerait pas." Footnote 42: the `f_!(e)` are always 1-connected (XII p. 101), so
  the weaker variant must read "2-connexe".
- Prop. 2.19 (ms. 36), marked **Faux** by himself: `diag_X` cofinal ⇒ `X` totally `W∞`-aspherical; its corollary
  (`Δ°` totally `W∞`-aspherical) falls with it.
- **Contre-exemple 2.20 (ms. 36bis–36ter)** — this is the "collage test" of the TOTASPH prompt (Lead 1), and it is
  Grothendieck's own: adjoin to `X` a closed final point `e` by a presheaf `H ∈ X^` (`H(x) = Hom_{X'}(x, e)`,
  `X/e ≅ X/H`); `i: X → X'` is co-cofinal iff `H` is 0-connected. If `X` is `W∞`-aspherical and `X'` too, then
  `i ∈ W∞`, and "by XII th. 4 cor. 4 (p. 149)" `X/H` would be `W∞`-aspherical; false for `X = Δ`. He concludes:
  "Cela me fait soupçonner que la conjecture `X` totalement `W∞`-asphérique ⟹ `X` filtrante pourrait être valable."
  [My remark: from `i ∈ W∞` only the *acyclicity* of `X/H` follows (`BX' ≃ BX ∪ Cone(B(X/H))`); the step through
  XII Th. 4 Cor. 4 is the "reverse half" of the cofibration axiom, the subject of POLES. The counterexample itself
  stands: take `H` 0-connected with `ΣB(Δ/H)` not contractible, e.g. the boundary of the 2-simplex.]

### II §3 (ms. 37–49). Retour sur la cofinalité
- `W_0 = {f : π_0(f) bijective}`, the coarsest localizer with the connectedness axiom Loc 5; `HOT_{W_0} ≃ D_{(Ens)}`
  (3.1)–(3.6). Table (3.8) of the "W_0-fourbi": W_0-asphérique (all `I'/i` 0-connected), W_0-coasphérique (all
  `i\I'` 0-connected), W_0-propre, W_0-lisse, W_0-équivalence universelle, W_0-fibration (strong, weak).
- Prop. 3.1: characterizations of universal W_0-equivalences and W_0-fibrations. Étale coverings are W_ω-perfect but
  not W_0-fibrations.
- **Prop. 3.2 / Déf. 3.3 (ms. 43–45)**: `u: I' → I` is **cofinal** ⇔ `colim_{I'} u^*F ≅ colim_I F` for all
  covariant `F` ⇔ `lim_I F ≅ lim_{I'} u^*F` for all presheaves `F` ⇔ all `i\I'` are 0-connected (= W_0-coasphérique).
  So his "cofinal" is the usual *final* functor; "co-cofinal" = all `I'/i` 0-connected = *initial*.
- Cor. 3.4: F 0, F 1, F 2 criteria; if `I'` is filtered and `u` cofinal then `I` is filtered and the `i\I'` are
  filtered.

### II §4 (ms. 49–53, continued in II-b). Foncteurs biasphériques
- `u` is M-connexe (= M-biasphérique) when `u^*: M(I) → M(I')` is fully faithful. Prop. 4.1: equivalent for all
  `M` ⇔ for `M = Ens` ⇔ all `I'/i → I/i` cofinal ⇔ all `i\I' → i\I` cofinal ⇔ for every arrow `α: i_0 → i_1` the
  bi-induced category `i_0\I'/i_1` over `α` is 0-connected ("W_0-connexe").

(II-b, ms. 45–99: §4 continued, §5 Dualité formelle, §6 Transporteurs, noyaux, stabiliseurs relatifs à W,
§7 Morphismes cofiltrants et localement cofiltrants — not yet read.)

## Chapter XII, second part (XIIb-a: ms. 59–122; XIIb-b: ms. 115–169). Recollement, sommes amalgamées, W-cofibrations

Standing hypothesis from ms. 75: `W` a fundamental localizer = W(1), W(2 bis), W(3) in the numbering of XII
(= Loc(1, 2, 3 bis) of XVI). Not assumed: W(4) fibration axiom, W(5) connectedness axiom, W(6) inductive limits.

### XII §1 (ms. 59–74). Open–closed decompositions of a category
- Prop. 1 (ms. 60): triples `(X, U, T)` (`U` open = sieve, `T` the complementary closed = cosieve) ≃ triples
  `(U, T, H)` with `H: U° × T → Ens`, `H(u, t) = Hom_X(u, t)`; no condition on `H`. Induced triples along
  functors into `U` and into `T` (ms. 60–61).
- §1.2 (ms. 61–64): topos gluing `φ = j^*i_*: U^ → T^`; Prop. 2 and Cor.: the glued topos is of the form `X^` iff
  `φ` has a left adjoint; `φ(F)(t) = Hom_{U^}(H(t), F)`.
- §1.3 Prop. 3 (ms. 66): functors out of a glued `X`. §1.4 **Théorème 1** (ms. 69–70): the colimit in `Cat` of
  `U1 ← U → X ← T → T1` is glued from `U1`, `T1` by `H1 = (f_U° × f_T)_!(H)`;
  `Hom(u1, t1) = π_0(((u1\U) × (T/t1)°)/H)` (boxed (*), ms. 72); when `T1 = T`:
  **`Hom(u1, t) = π_0(u1\U/t)`** ((**), ms. 72).
- Prop. 4 (ms. 75): the boundary `Ṫ = T ∩ Ū` is the same before and after cobase change. Prop. 5: pushouts of
  open (closed) immersions in `Cat` are open (closed) immersions and the square is also cartesian.

### XII §2 (ms. 75–120). Sommes amalgamées et W-équivalences
- **W(7 bis)** (axiome du carré cocartésien, ms. 75–76): for opens `U, V` with `U ∪ V = X`:
  `(U ∩ V → V) ∈ W ⇔ (U → X) ∈ W`. Corollary: (a ∧ b) ⇒ c and (b ∧ c) ⇒ a for the asphericity of
  `U ∩ V`, of `U` and `V`, of `X`.
- **W(7)** (axiome du cube / lemme des cinq, ms. 76–77): for a map of such squares, two of {the map on the
  intersections ∈ W; the maps on the two opens ∈ W; the map on the unions ∈ W} imply the third.
  Prop. 6: W(7) ⇒ W(7 bis).
- **Théorème 2 (ms. 78): "`W∞` satisfait à W(7)"** — asserted from Artin–Mazur and Mayer–Vietoris, "je n'ai pas
  écrit la vérification". [My check: false as stated. Take `X = A ⋆ {t, s}` (two incomparable objects above a
  category `A` that is connected, acyclic and not aspherical); `U = A ∪ {t}`, `V = A ∪ {s}` are sieves,
  `U → X` is in `W∞` (both contractible: `BX` is the suspension of `BA`), `U ∩ V = A → V` is not. Only the
  direct halves hold for `W∞`. This is the subject of POLES.]
- Remarque (ms. 79–80): the direction "intersection map ∈ W ⇒ `U → X` ∈ W" "va de soi"; the converse
  "m'apparaît comme un trait très particulier du dérivateur HOT_W (quand il le possède), et notamment de HOT".
- §2.2 (ms. 80–87). The "grand traquenard": in a pushout of `U → X` (open immersion) along `p: U → U1` one can
  have `i ∈ W` without `i1 ∈ W`, and `p ∈ W` without `q ∈ W`. **Prop. 6 (second of that number, ms. 81)**: if
  `U → Ū` and `U1 → Ū1` are in `W` then `i ∈ W ⇔ i1 ∈ W` (given W(7 bis)) and `p ∈ W ⇔ q ∈ W` (given W(7)).
  **Prop. 7** (ms. 84) and its **Corollaire (ms. 85)** = Th. 4 Cor. 4 (ms. 149): given W(7 bis) in its strong
  form, if `X ∖ U = {t}` is a point then `i ∈ W ⇔ U/t` is `W`-aspherical. ms. 86: `W`-asphericity of `U → Ū` is
  not stable under cobase change.
- **§2.3 (ms. 87–103). Totally W-aspherical objects.**
  - **Définition 1 (ms. 88–89)**: (a) `H ∈ U^` is *totalement W-asphérique* if for every `p: U → U1` the
    category of elements of `p_!H` is `W`-aspherical; (b) `V ∈ Cat` is totally `W`-aspherical if its final
    presheaf is: for every `f: V → V1`, the category of elements `π_0(V/V1)` of `f_!(e_V) = (v ↦ π_0(v\V))`
    is `W`-aspherical. Editors: not the notion of Pursuing Stacks.
  - ms. 89–93: the canonical factorization `V → π_0(V/V1) → V1`, characterized by: second map a discrete
    fibration, first map with 0-connected comma categories `ṽ\V` (= comprehensive factorization; he says "il
    doit être facile").
  - **Prop. 8 (ms. 93)**: `U/H` totally `W`-aspherical ⇒ `H` totally `W`-aspherical. Converse asked (ms. 94–97)
    [audit row B035]; holds for `H` subterminal (ms. 96); his example `E_G → B_G` shows the natural proof fails;
    "je me vois mal construire un exemple".
  - **Prop. 9 (ms. 97)**: (a) a category with a final object is totally `W`-aspherical (the image of a final
    object in `π_0(V/V1)` is final); (b) union of two opens — marked false by himself, as is its "rectification"
    Cor. 1 (retractions) and **Cor. 2 (`Ψ = a ← 0 → b` totally W-aspherical): "Faux"**. Footnote: "Je conjecture
    à présent que ce sont les seules!" corrected to: filtered categories too (if `W` has the limit axiom).
  - ms. 100–103: a `W∞`-aspherical category that is not totally `W∞`-aspherical. Remark: if `X` is 1-connected
    and `X → Y` has 0-connected `y\X`, then `Y` is 1-connected (coverings pull back fully faithfully); so a
    counterexample needs a non-zero `π_i(Y)`, `i ≥ 2`. **Prop. 10 (ms. 103)**: for `Y` 1-connected,
    `Ch(Y; y_0, −)` is `W∞`-aspherical and its target functor to `Y` has 0-connected `y\X` (it is `W∞`-parfait
    with fibre `Ω(Y, y_0)`); so it is not totally `W∞`-aspherical unless `Y` is aspherical. Footnote: `Ψ` is a
    more striking example. **Question (ms. 103)** [row C005]: does `Y` `W∞`-aspherical imply `Ch(Y; y_0, −)`
    totally `W∞`-aspherical? "J'en doute fort!"
  - ms. 104–107, Prop. 11: examples with `i ∈ W`, `i1 ∉ W` and `p ∈ W`, `q ∉ W` (the second uses the Corollary
    of ms. 85, hence the strong W(7 bis); for `W∞` it needs re-examination: the pushout is `U1` with a cone on a
    copy of `Y`, where `U1` = `Y` plus a final object).
- **§2.4 (ms. 107–114). Immersions dwyériennes.**
  - **Théorème 3 (ms. 107–108)**: if for every `t ∈ Ṫ` the presheaf `i^*(t) = Hom_X(−, t)|U` is totally
    `W`-aspherical, then for every `p: U → U1` the immersion of `U1` in its closure is again such ("strictement
    W-asphérique"), hence in `W`; so `i ∈ W ⇔ i1 ∈ W` (W(7 bis)) and `p ∈ W ⇔ q ∈ W` (W(7)). Proof (ms. 112):
    the crossing presheaf after cobase change is `p_!` of the one before, and the Lemma: total asphericity of
    `F` (resp. of `U/F`) passes to `p_!F` (resp. to the category of elements of `p_!F`).
  - Cor. 1: under W(7) such an `i` is a **W-cofibration** (cobase change along `i` preserves `W`).
  - **Définition 2 (ms. 109–110)**: (a) `f: X → Y` *strictement W-asphérique*: every `f^*(y)` totally
    `W`-aspherical in `X^`; *totalement W-asphérique*: every `X/y` totally `W`-aspherical. (b) an open immersion
    is *W-dwyérienne* (resp. *totalement*) if `U → Ū` is strictly (resp. totally) `W`-aspherical; closed
    immersions by duality. (c) *W-cofibration*. (d) *W-cofibration triviale = W-équivalence couniverselle*.
  - Cor. 2 (ms. 111): under W(7) a W-dwyérienne open immersion is a trivial W-cofibration iff it is in `W`.
  - **Questions ouvertes (ms. 111–112)** [row C035]: (a) is an open immersion that is a W-cofibration, or even a
    couniversal W-equivalence, necessarily W-dwyérienne (footnote: or even a Dwyer immersion)? Known to him when
    `T = e` (through the Corollary of ms. 85). (b) a good notion covering all immersions?
  - Cor. 3 (ms. 113): W-dwyérienne and totally W-dwyérienne immersions are stable under cobase change (no extra
    axiom). **Commentaire (ms. 113–114)** [rows C045, C047]: not clear that they, or the strictly / totally
    W-aspherical functors, are stable under composition; Dwyer immersions are.
  - **ms. 114** [row C048 = XIIbb-A001]: he wants a class of open immersions that are W-cofibrations and stable
    under `(U × I) ∪ (X × ε) → X × I` for `ε = {0, 2n} → Φ_n = (0 → 1 ← 2 → … ← 2n)`, `n ≥ 2`; Dwyer immersions
    fail it already for `{0} → Δ^1`.
- §2.5 (ms. 115–120): Prop. 11 (second of that number): `f: X → I` W-proper (W(5) assumed), `i_0` final in `I`,
  fibre over `i_0` totally `W`-aspherical ⇒ `X` totally `W`-aspherical. Prop. 12: `π_0(X) = colim_I π_0(X_i)`.
  Cor. 1: `p_!(e_X) = colim_I p_{i!}(e_{X_i})`. Cor. 3 (ms. 120): `Z` totally `W`-aspherical and `I` with a
  final object ⇒ `Z × I` totally `W`-aspherical.

### XII §3 (ms. 121–169). Sommes amalgamées et intégration
- §3.1: for `X_1 ← X_0 → X_2` the integrated (fibred) category `𝒳 = ∫` over `Φ = (1 → 0 ← 2)`; Prop. 13
  (ms. 125–126): under W(7 bis), `α_1 ∈ W ⇔ i_2 ∈ W` (footnote 85: ⇒ needs only the direct form = Loc(6'a) of
  XVI). Corollary: cube lemma for integrals under W(7).
- §3.2 Déf. 3 (ms. 131): a commutative square is **W-homotopiquement cocartésien** when `φ_Q: 𝒳 → Y` is in `W`.
- §3.3 Prop. 14 (ms. 140–143): smooth and proper integration, `Q` and `Q°`, give the same notion (through the
  functor `Σ(X)` with `Σ(X) → X`, `Σ(X) → X°` both `W`-aspherical; I ms. 72–75).
- **§3.4 Théorème 4 (ms. 146–157)**: (a) `φ_Q` is W-smooth iff `f_0, f_1, f_2` are; (b) fibres of `φ_Q` are the
  integrals of the fibres. His later footnotes: the direct parts and Cor. 1–3 need no extra axiom; **Cor. 4 and
  5 need W(7 bis) in its strong form** (footnotes 104, 105). Cor. 1: smooth (or proper) legs and aspherical
  integrated fibres ⇒ W-cocartesian. Cor. 2: a `Cat`-pushout along an open immersion `α_1` with `f_1` smooth is
  W-cocartesian. Cor. 3: `X = U_1 ∪ U_2` (opens) is a W-cocartesian square. **Cor. 4 (ms. 149–150)**: `T = e`:
  `i ∈ W ⇔ U/t` W-aspherical (the square `U/t → X/t`, `U → X` is W-cocartesian; then strong W(7 bis)).
  Cor. 5: variant with a closed point `t_0`.
- §3.5 Prop. 15 (ms. 158): characterization of `Cat`-pushout squares along an open immersion (cartesian, the
  closed complements isomorphic, and `(p/t)_!(e) = e`). Cor. 1, 2. **Théorème 5 (ms. 167–168)**: a pushout
  square in `X^` along a monomorphism gives a cartesian and cocartesian square of the `X/F` in `Cat`,
  W-cocartesian under W(7 bis); monomorphisms of `X^` are `W_X`-cofibrations.

## Appendix to Chapter XII (XIIapp: ms. 1–18)

- ms. 1–4: a "Proposition" marked false by himself: a category `X` with objects `b, c` such that `b × c` is in
  `X` and every object maps to `b` and to `c` would be `W∞`-aspherical. He proves 1-connectedness (in the
  fundamental groupoid `b × c` becomes final) and computes, for the category with objects `b`, `b × b` and
  `End(b) = G` a monoid: `H²(X, M) = Hom_mon(G, M)`. So `X` is 2-connected iff the abelianization of `G` is zero.
- Corollary (ms. 4): **`Ψ = (b_0 ← a_0 → c_0)` is not totally `W∞`-aspherical**: a diagram of type `Ψ` in `X`
  whose pushout in `X^` is `e_X` does not force `X` to be aspherical.
- **Question (ms. 5)**: are there totally `W∞`-aspherical categories other than those with a final object?
  "Je suspecte à présent que non — donc que l'on ne peut améliorer substantiellement sur la notion déjà connue
  d'immersion ouverte de Dwyer." (Superseded by II Cor. 2.17 and the footnotes of XII ms. 100, 108: filtered
  categories.)
- ms. 5–7: finite examples for XII ms. 104–107 (`i ∈ W`, the cobase change `i1 ∉ W`; `p ∈ W`, `q ∉ W`), built
  from that two-object category with `G = {±1}`; the second again quotes the unproved Corollary of XII ms. 85.
- ms. 8–12 (**§2.6 Contre-exemples pour la totale asphéricité**): `Z = (0 ⇉ a → b, a → c)` with
  `βλ = βμ`, `γλ = γμ` (6 non-identity arrows); `Ψ → Z` has `b ⊔_a c = e_Z` in `Z^` (so it is cofinal in his
  sense) and `Z` is not aspherical. His first claim that `Z` retracts onto `0 ⇉ a` (type `S¹`) is corrected by
  his footnote 7: `Z` is the suspension of `⇉`, of type `S²`. [The same slip stands uncorrected for `V` on ms. 9
  and for `V'_0` on ms. 15, where he writes `π_1(V'_0) ≅ Z`; `V'_0 = Z` is of type `S²`.]
- ms. 12–16, **Proposition**: for `n, m ≥ 2`, the boundary `U = ∂X` of the "square" `X = Φ_n × Φ_m` is an open
  immersion with all `U/t` (`t` on the boundary of `U`) aspherical: `e`, or `Φ` (final object), or at the four
  corners `Ψ̃ = (a' → a ← 0 → b ← b')`, which has no final object. So `U → X` is not a Dwyer immersion; claim:
  **it is not a W-cofibration**. Proof: the corner `V ≅ Ψ` is closed-Dwyer in `U`; `V̄ = Δ¹ × Δ¹` is
  closed-Dwyer in `X`; cobase change of `V → V̄` along `V → V1 := (Z plus a final object)` gives `V̄1` not
  aspherical; he concludes through Cor. 4 of XII ms. 149 (strong W(7 bis)) and "`π_1 ≅ Z`". [My check for `W∞`:
  `V̄1` is `V1` with a cone attached along `V1/t ≅ Z ≃ S²`, and `V1` is itself a cone on `Z`, so `V̄1 ≃ S³`:
  not `W∞`-aspherical, without the corollary. For `W_1` and `W_2` it is aspherical, so his parenthesis "dans le
  cas où `W ⊆ W_1`" is wrong as stated.]
- **ms. 17–18, the gluing question** (used by STRATA and by Lead 1 of TOTASPH): `X_0 ⊂ X` open, `X_1` the closed
  complement, `X̃_01 ⊂ Fl(X)` the arrows from `X_0` to `X_1`, with `p: X̃_01 → X_0` (a fibration with fibres
  `x_0\X_1`) and `q: X̃_01 → X_1` (a cofibration with fibres `X_0/x_1`). **Question**: is the square
  `X̃_01 → X_0, X_1 → X` W-cocartesian, i.e. is `φ: ∫(X_0 ← X̃_01 → X_1) → X` in `W`? Yes if `i` is
  W-aspherical or `j` W-coaspherical. In general he proves `φ ∈ W_1` (coverings glue), sketches `W_2`, and
  **conjectures `φ ∈ W∞`**. False if arrows are replaced by paths `x_0 ⇝ x_1` (unless `i` or `j` is in `W∞`).
  "Une situation topologique tout à fait spéciale à la catégorie de modèles Cat."

## Chapter II §7 (II-b ms. 90–99), statements only

- Déf. 7.1: `f: X → Y` is *cofiltrant* (resp. localement, faiblement, pré-) when every `y\X` is cofiltered
  (resp. …); dually *filtrant* through the `X/y`. Rem. 7.2: stable under co-étale base change; étale morphisms
  are locally filtering. Prop. 7.3 and Cor.: if `f` and `Y` are cofiltering so is `X`; stable under composition.
  Rem. 7.4: not stable under base change (`e → Δ¹` at 1); a cofiltering functor is W-coaspherical for every `W`
  with the limit axiom Loc (8), in particular cofinal. Prop. 7.4, Lemma 7.5 (for an étale `h: X1 → X`, each
  component of `x\X1` has an initial object). Only the statements were read (the prompt of TOTASPH calls the
  section marginal); the proofs and the rest of II-b (§§4–6) are still to be read for BISITE.


## Chapter XI §1 (ms. 127–136): Hot-fibrations in Cat  [file DER_XI-XIIa.tex, lines 91–407]

- **Théorème 1.** For `f: X → Y` in Cat the following are equivalent: a) base change along `f` preserves
  Hot-equivalences (`Y'' → Y'` over `Y`); a′) same with `Y'' = e` and `Y'` with final object; a″) dual (initial
  object); b′) all `X_y → X/y` and all `X/y → X/y'` are Hot-equivalences, universally (the first suffices);
  b″) dual; c) for every locally constant `F` on `X`: `f_*F` (sets), `R¹f_*F` (groups), `R^i f_*F` (abelian) are
  locally constant and computed fibre by fibre, universally. Proof of c ⇒ a by the Artin–Mazur cohomological
  criterion (torsors, gerbes, Leray).
- Déf. 1: such an `f` is a **Hot-fibration**. Prop. 1: stable under base change and composition; `f` is one iff
  `f°` is. Prop. 2: `s ↦ hot(X_s)` is a local system on `S`.
- **Théorème 2.** For `f: X' → X` over `S`, both Hot-fibrations over `S`, and `S_0 ⊂ Ob S` meeting every component:
  `f` is a Hot-equivalence iff the `f_s`, `s ∈ S_0`, are. Uses the Lemme: for `S` 0-connected there is a
  Hot-aspherical `S̄` with a Hot-fibration `S̄ → S` (namely `Ch_∞(S; s_0, −)` with the target functor; VII p. 152).
  Remark: proper and smooth functors must be developed without HOT.

## Chapter XII part I (ms. 1–18; dated 19.11.90): characterization of `W∞`  [DER_XI-XIIa.tex, lines 408–850]

- **Axioms on `W ⊂ Fl(Cat)`.** W(1) saturation: a) identities, b) two out of three, c) `fg, gf ∈ W ⇒ f, g ∈ W`.
  W(2) localization (= L4 bis of Pursuing Stacks): a morphism over `S` that is in `W` locally over `S` (after base
  change to every `S/s`) is in `W`. W(2 bis) weak form: `W`-aspherical (all `X/y` `W`-aspherical) ⇒ in `W`.
  Prop. 1: equivalent: `X × Δ¹ → X ∈ W` for all `X`; a category with final object is `W`-aspherical; homotopisms
  are in `W`. W(3): the final-element axiom. Cor. 1–3. Prop. 2: `f ∈ W ⇒ f° ∈ W` (via `Φ(X)` of I p. 75).
- **W-fibrations (ms. 4).** a) ultraforte: base change by `f` preserves `W`; a′) forte; a_1 gauche; a_2 droite.
  **W(4)** (fibration axiom): a left `W`-fibration is ultraforte. Prop. 3 (no W(4), needs strong W(2)): a
  morphism of `W`-fibred categories that is in `W` fibrewise is in `W`; corollary with a set `S_0` of base points.
  Lemme (with W(4)): `Ch(S; s_0, −) → S` is a strong `W`-fibration with `W`-aspherical source. Prop. 4: under
  W(1, 2, 3, 4), a morphism in `W` between `W`-fibred categories has all its fibres `f_s` in `W`.
- **W(5)** (connectedness): `f ∈ W ⇒ π_0(f)` bijective. Lemma (ms. 12): `X` `W`-aspherical ⇒ `Ω(X, x_0) =
  Ch(X; x_0, x_0)` and all `Ω^n` are `W`-aspherical; with W(5), `X` is then `W∞`-aspherical.
- **Théorème 1 (ms. 12): W(1, 2, 3, 4, 5) ⇒ `W ⊂ W∞`.** Footnotes: W(4 b″) suffices; instead of W(5) it suffices
  that `W ≠ Fl(Cat)` (Théorème 2, ms. 20). Corollary: `W∞` is the largest such class.
- ms. 13–14: seven variants of W(4): a = a_1 ⇔ a_2; a′ (a `W`-parfait morphism is ultraforte); a″ (a
  `W_ω`-parfait morphism is ultraforte); b (conclusion of Prop. 4); b′; **b″**: for `f` `W_ω`-parfait, `f ∈ W ⇒`
  the fibres of `f` are `W`-aspherical. Here `W_ω ⊂ W ∩ W∞` is the smallest class with W(1), W(2 bis), W(3)
  (footnote 32: take W(2 bis), to get `W_ω` as small as possible). Implications a ⇒ a′ ⇒ a″ ⇒ b ⇒ b′ ⇒ b″;
  marginal note "en fait, toutes ces conditions sont équivalentes"; footnote 33: return to these at ms. 53–56.
- **W(6)** (filtered limits, ms. 14): a filtered colimit in Cat of `W`-aspherical categories is `W`-aspherical.
  Prop. 5: with W(1)–W(4 b″) and W(6), a filtered colimit of morphisms in `W` is in `W` (canonical factorization
  `X → X̄ → Y` through `Ch`, which commutes with filtered colimits).
- **Conjecture (ms. 15, "hardie? sotte?")**: W(1)–W(6), with W(4) in the form b″ (and perhaps W(2 bis) for W(2)),
  imply `W = W∞`. He adds that W(1) may have to be strengthened by closure under retracts.
- **Remarque (ms. 16–17) on the truncated classes.** `W_n` = maps bijective on `π_0` and on `π_i`, `0 < i ≤ n`.
  `W_n ⊄ W∞`, so `W_n` cannot satisfy W(1)–W(4 b″). W(1) (strongly), W(2) (Artin–Mazur and Leray), W(3), W(5),
  W(6) hold; the fibration axiom fails: for a fibration in `W_n`, `π_n(X_s) = Coker(π_{n+1}(X) → π_{n+1}(Y))`.
  The variant `W′_n` (in addition `π_{n+1}` surjective; i.e. homotopy fibres `n`-connected) has the same
  aspherical objects and satisfies W(4 b″) but is not saturated (`gf, g ∈ W′_n` does not give `f ∈ W′_n`); "ne
  mérite pas le nom de localiseur". `W_n` "me paraît excellent". W(1), W(2), W(3) hold for every `W_D` of a
  derivator; W(4), W(5), W(6) are "de nature plus spéciale" and are not part of the notion of fundamental localizer.

## Chapter XII part II (ms. 18–22): "Perplexités sur les axiomes et la terminologie"  [lines 852–928]

- Earlier (Chapter I, and "la plupart du temps") he assumed `W_D ⊇ W∞`. With W(4 b″) this forces `W_D = W∞`: the
  fibration axiom is "pratiquement une caractérisation de `W∞`". The D-fibrations of I ms. 111–126 test condition a)
  only on `W∞`-aspherical `Y'', Y'` (weaker than strong `W`-fibration). Footnote 39: the good notion of
  `W`-fibration without `W∞ ⊂ W` is in Th. 3 and Déf. 3, ms. 51–52.
- **Théorème 2 (ms. 20).** If `W` satisfies W(1, 2, 3, 4 b″) and not W(5), then `W = Fl(Cat)`. (Footnote 41: a
  more general result at XV 9.12, ms. 133 bis; footnote 42: the proof uses W(4) in a stronger form than b″.)
  Proof: reduce over the discrete category `π_0(Y)`; if `π_0(f)` is not surjective, `∅ → Y ∈ W` with `Y ≠ ∅`, so
  `∅ → Y × Z ∈ W`, the projection `Y × Z → Y` is in `W` and a `W`-fibration, hence `Z` is `W`-aspherical for all
  `Z`; if not injective, reduce to `X` `W`-aspherical with `card π_0(X) ≥ 2` and use the diagonal.
  Corollaire: W(1, 2, 3, 4 b″) and `W ≠ Fl(Cat)` ⇒ W(5), hence `W ⊂ W∞`.

## Chapter XII part III (ms. 22–58): remarkable classes of functors attached to `W`  [lines 934–1630]

- **Definition (ms. 22): "localiseur fondamental"** = W(1) saturation, W(3) final element, W(2 bis) weak
  localization (formerly L4′ in Pursuing Stacks). These three "ont suffi pour pratiquement tout" in Pursuing
  Stacks, except one use of a weakened W(2) (cartesian functors between fibred categories).
- Prop. 1 / Déf. 1 (ms. 22–23): `f` is **`W`-asphérique** iff `f'` is in `W` after every base change by a local
  isomorphism `Y' → Y`, iff all `X/y` are `W`-aspherical; **`W`-coasphérique** iff `f°` is aspherical (all `y\X`
  aspherical). Remark: a left adjoint is aspherical, a right adjoint coaspherical; in general the "generalized
  adjoint" `g: Y → X^` with `X/y ≃ X/g(y)`: `f` is aspherical iff the presheaves `g(y)` are `W`-aspherical.
- Prop. 2 (ms. 24): aspherical functors compose; `gf` and `f` aspherical ⇒ `g` aspherical. Rappel: local
  isomorphisms (`S'/s' ≅ S/s`), stable under composition and base change. Cor. 1: aspherical functors are stable
  under base change by local isomorphisms. NB (ms. 25): not under arbitrary base change (`{y_0} → Y` is aspherical
  iff `y_0` is initial, under W(5)). Cor. 2: equivalences are aspherical and coaspherical.
- Prop. 3 (ms. 26): equivalent conditions for the later Déf. of `W`-lisse: a) each `X_y → X/y` is coaspherical;
  b) for every `x_0`, `x_0\X → y_0\Y` has `W`-aspherical fibres; c) for every `Δ¹ → Y`, the inclusion of the closed
  fibre `X'_1 → X'` is coaspherical; d) for every arrow `u_0: y_0 → y_1` and `x_0` over `y_0`, the category
  `X(x_0; u_0)` of liftings of `u_0` with source `x_0` is `W`-aspherical. (Continued below.)

- Déf. 2 (ms. 28): `f` is **`W`-propre** under the conditions of Prop. 3; **`W`-lisse** iff `f°` is `W`-propre
  (the inclusions `X_y → y\X` are aspherical). Remark: a (weakly) Cat-cofibred `X/Y` is `W`-propre, a (weakly)
  Cat-fibred one is `W`-lisse, for every `W`.
- Prop. 4 (ms. 28–29): proper morphisms are stable under composition and base change; local coisomorphisms
  (closed immersions) are proper; dually for smooth (open immersions are smooth). Lemma: `f` proper ⇒ each
  `x\f: x\X → y\Y` proper. Footnote 43: if `gf` and `f` are smooth, `g` is smooth at the points of `Im f`.
- **Prop. 5 (ms. 29–30):** `f` proper or smooth with `W`-aspherical fibres ⇒ `f ∈ W` universally. Corollary
  (needs W(2)): an `S`-morphism between two proper (or two smooth) `S`-categories that is in `W` fibrewise is in `W`.
- Prop. 6 (ms. 31–32): base change of an aspherical `f` along a smooth `p` is aspherical. Corollary: base change
  along a smooth `p: S' → S` maps `W^g_S` (in `W` locally on `S`, on the left) into `W^g_{S'}`; dually for proper
  `p` and `W^d`.
- ms. 33–36: for `f: X → S` proper (it suffices: **`W`-prépropre** = the `X_s → X/s` are in `W` universally,
  footnote 45) the functor `λ = hot_*^{X/S, W}: S → Hot_W`, `s ↦ hot_W(X_s)`; dually for smooth / **prélisse**
  a contravariant `λ°`. **Prop. 7**: if both hold universally, `λ` and `λ°` send every arrow to an isomorphism and
  `λ°(u) = λ(u)^{-1}`.
- ms. 37–40: the list of notions of fibration by test maps `Y'' → Y'` over `Y`: a_1 (`Y'` with final object,
  `Y'' = e`), a_2 (initial object), a_0 (`Y' = Δ¹`, `Y'' = e`: **`W`-pseudofibration**), b (`Y'`, `Y''`
  contractible: "`W`-fibration hot-forte"), b′ (`Y'` `W`-aspherical), c (all of `W`: ultraforte).
  Déf. 3: **`W`-parfait** = proper and smooth. For `W∞` all variants except a_0 are equivalent.
- **Prop. 8 (ms. 41):** left `W`-fibration (a_1) ⇔ prépropre and all `X/s_0 → X/s_1` in `W` ⇔ prépropre and
  pseudofibration. Footnote 49: for Cat-cofibred `f`, ⇔ all `u_*: X_{s_0} → X_{s_1}` in `W`.
- Question (ms. 42): for `f` `W`-parfait, `S` contractible, is `X_s → X` in `W`? Answer via the Lemme (ms. 44):
  for `X ∈ Fib_0 S`, `f ↦ f^*X` maps the arrows of `Hom(S', S)` into `W^d_{S'}`; Cor. 1: factorization through the
  fundamental groupoid of `Hom(S', S)`; Cor. 2: for a homotopism `f`, `f^*: HOT^lc_W(S) → HOT^lc_W(S')` is an
  equivalence. **Prop. 9 (ms. 48):** a left `W`-fibration is a `W`-fibration in the sense b); footnotes 56–58:
  correct for `W` strongly saturated (one only gets that `hot_W(X'') → hot_W(X')` is an isomorphism).
- **Théorème 3 (ms. 51), for `W` with W(1, 2, 3):** the eight conditions a (contractible `S'' → S'`), a′ (fibre
  inclusions over contractible `S'`), a_1, a_2, b_1 (prépropre and `X/s_0 → X/s_1 ∈ W`), b_2 (prélisse and
  `s_1\X → s_0\X ∈ W`), c_1 (prépropre and pseudofibration), c_2 (prélisse and pseudofibration) are equivalent;
  they imply d) (homotopisms `S'' → S'` give `hot_W`-isomorphisms; equivalent if `W` is strongly saturated).
  **Déf. 4 (ms. 52): `W`-fibration.** Cor. 1: for `f` proper or smooth, ⇔ pseudofibration. Cor. 2: for a
  Cat-fibred `f`, ⇔ all `u^*: X_{s'} → X_s` in `W`. Cor. 3: prépropre and prélisse (e.g. parfait) ⇒ fibration.
  Prop. 10: a morphism of `W`-fibred categories (or of two prépropres, or two prélisses) that is fibrewise in `W`
  is in `W`.

## Chapter XII part IV (ms. 53–58): the axiom W(4) and its variants  [DER_XI-XIIa.tex, lines 1631–1767]

- New list (different letters from ms. 13–14): **W(4a)** every `W`-fibration is ultraforte (cartesian square, `f`
  a `W`-fibration, `p ∈ W` ⇒ `q ∈ W`); W(4a′) the same for `f` `W_ω`-parfait; **W(4b)** a morphism `f ∈ W`
  between `W`-fibrations over `S` has all `f_s ∈ W`; W(4b′) for split fibred categories and cartesian `f`; W(4b″)
  for `p, q` `W`-parfaits; **W(4c)** `f ∈ Fib_W ∩ W` ⇒ fibres `W`-aspherical; W(4c′) the same for
  `f ∈ Parf_ω ∩ W` (the old W(4b″)). Implications a ⇒ a′ ⇒(doubtful) b ⇒ b′, b″, c ⇒ c′.
  "J'ai surtout sué pour montrer que c′) ⇒ c), ou c) ⇒ b), sans y arriver."
- Prop. 1 (ms. 54): for `W` strongly saturated, a ⇔ a′ ⇔ b (b ⇒ a via: W(4b) ⇒ `p^*_lc: HOT^lc_W(S) →
  HOT^lc_W(S')` is an equivalence for `p ∈ W`, VI p. 204; Corollaire ms. 56: `H_•(S', p^*ξ) ≅ H_•(S, ξ)` for
  locally constant `ξ`).
- Small points (ms. 56–58): fibrewise smooth does not give smooth except for split fibred categories and strictly
  cartesian functors; Prop. 2: for `S = (a ← 0 → b)`, `Φ(Z)` is proper over `S` iff `Z = ∅`; Prop. 3: a strictly
  cartesian functor of split fibred categories that is `W`-fibrant fibrewise is `W`-fibrant if `W` satisfies W(4a).

*Remarks for the POLES review.* (i) Théorème 1 of XII (ms. 12) and Théorème 2 (ms. 20) together say: W(1, 2, 3)
plus the fibration axiom in the form b″ (old numbering) and `W ≠ Fl(Cat)` give `W ⊂ W∞`. Since every fundamental
localizer contains `W∞` (Cisinski 2004, Th. 2.2.11), this is `W = W∞`: the fibration axiom characterizes `W∞`
among the proper fundamental localizers. (ii) Grothendieck's own count of what is proved: he does not prove the
equivalence of the variants c′, c, b; the Conjecture of ms. 15 (W(1)–W(6) ⇒ `W = W∞`) is superseded by (i) once
minimality of `W∞` is known. (iii) The remark on `W_n` at ms. 16–17 is the origin of the "poles" picture: `W∞`
(fibration axiom) at one end; the localizers `W_D ⊇ W∞` of derivators, which need not satisfy it.


## Chapter XII part VI (ms. 171–234): criterion of `W∞`-asphericity for the `Ω^n(X, x)`  [DER_XIIc-a.tex]

- **§1 (ms. 171–187), "Cogitations sur `W_n`".** `W_0`: `π_0(f)` bijective ⇔ `H^0` bijective on constant
  coefficients ⇔ `f^*` fully faithful on constant presheaves. `W_1`: `Π(f)` an equivalence ⇔ `H^0` bijective for
  locally constant sheaves of sets and `H^1` for sheaves of groups (b′: constant groups and `H^1` surjective
  suffice) ⇔ `f^*` an equivalence on locally constant sheaves of sets. `π_n(X, x) := π_0(Ω^n(X, x))` with
  `Ω(X, x) = Ch(X; x, x)`.
- Théorème 1 (ms. 172) is **withdrawn by Grothendieck** (footnote 112: "sans doute faux"; b ⇒ a probably false
  already for `n = 2` unless `X`, `Y` are 1-connected); Lemme ms. 177 also "sans doute faux" (footnote 115).
  ms. 173–176: the `Ω(X, x)` are the fibres of the `W_ω`-parfait `Ω(X, −) → X` (pull-back of `Ch(X) → X × X` along
  the diagonal), with a canonical section; question whether a `W`-fibration with a section gives a functor
  `X → Hot^•_W` (pointed); sketch only.
- **"Théorème 1 rectifié" (ms. 178–187).** For `n ≥ 2` and `f: X → Y` (in Cat, Top, `Δ^`):
  `a_n`: every homotopy fibre `Z` of `f` is `n`-connected (`π_i(Z) = 0`, `0 ≤ i ≤ n`);
  `b_n`: `π_0(f)` bijective and `π_i(f, x)` bijective for `1 ≤ i ≤ n` (one `x` per component);
  `c_n`: `H^i(Y, F) → H^i(X, f^*F)` bijective for `i ≤ n` and `F` locally constant (sets for `i = 0`, groups for
  `i = 1`, abelian for `i ≥ 2`).
  Then **`a_n ⇒ b_n ⇒ c_n ⇒ a_{n−1}`**, "et je présume que chacune de ces implications est stricte".
  Footnote 116: `b_n ⇒ c_n` is "vraiment prouvé" for `X`, `Y` 1-connected; otherwise verifications remain.
  Footnote 117: even for `X`, `Y` 1-connected `c_n ⇒ b_n` is unclear ("il faut montrer que `π_n(Z) → π_n(X)` est
  nul, et on trouve seulement que le composé avec `π_n(X) → H_n(X)` est nul. Je présume qu'il y a des
  contre-exemples"). Proofs: `a_n ⇔ b_n` + surjectivity of `π_{n+1}(f)` (strict: `K(π, n+1)`); `b_n ⇒ c_n` by the
  Leray spectral sequence and Hurewicz, with the pairing `H^n(X, G) → Hom_π(π_n(X, x), G_x)` "à vérifier" for twisted
  `F` (complete for `n = 2` via universal coverings); `c_n ⇒ a_{n−1}` by Leray and
  `Hom_π(π_{n−1}(Z), M) = 0` for all `π`-modules `M`.
  Closing remark (ms. 187): "le « bon » localiseur `W_n`, celui qui doit définir les « n-types d'homotopie »
  comme objets de `Hot_{W_n}`, est défini par la condition `a_n`" (sic: by the homotopy fibres being
  `n`-connected; compare XII ms. 16–17 where the class so defined, `W′_n`, was found not to be saturated).
- **§2 (ms. 187–190), Théorème 2 (?):** for `X` in Cat and `n ≥ 1`: (`X` 0-connected and `π_i(X, x) = 0` for
  `1 ≤ i ≤ n`) ⇔ (`G ≅ H^0(X, G_X)`, `H^1(X, G_X) = 0` for all groups `G`, `H^i(X, G_X) = 0` for `i ≤ n`, `G`
  abelian). Proof inside Cat by the `W∞`-fibration `Ch(X; x, −) → X` with aspherical total space and fibre
  `Ω(X, x)`. Corollaire: `X` is `W∞`-aspherical iff `X` is 0-connected and all `Ω^i(X, x)`, `i ≥ 1`, are
  0-connected.
- **§3 (ms. 191–207), "philosophie des fibres homotopiques".** Functorial factorizations `X → C(X) → S` with
  `i_X ∈ W`, `C(X) ∈ Fib_W S`; the category `𝒞_S` of pairs `(C, i)`; it is filtered (`C ∘ C'`), monoidal without
  unit; with W(4b) every arrow of `𝒞` gives an isomorphism of the functors `Cat/S → HOT^lc_W(S)`; question whether
  `𝒞` is 1-connected. The intrinsic statement: `(Fib_W S)(W^f_S)^{-1} → (Cat/S)W_S^{-1}` is an equivalence
  ((∗∗), ms. 204–206, "un fait tout à fait remarquable").
- **§4 (ms. 207–218), axiomatization in a general `(M, W)` with fibre products.** `Fib_W` := ultrastrong
  fibrations (base change along `f` preserves `W`); `Ho^!_W(S) = (M/S)W_S^{-1}`;
  `Ho^lc_W(S) = (Fib_W S)(W^u_S)^{-1}` (`W^u_S` = universally in `W`), contravariant in `S` for all maps.
  Axiom (a) "de la fibre homotopique": `Ho^lc_W(S) → Ho^!_W(S)` is an equivalence. Axiom (b): `W^u_S = W_S` on
  `Fib_W S`. Variant (c): the same for every full `F` between `Fib_W S` and `M/S`. In Cat: "c'est l'axiome des
  fibrations sur `W`, sous sa forme forte W(4a), qui est la clef de voûte" (footnote 122: W(4b) should suffice).
- **§5 (ms. 218–227), non locally constant relative types.** A class `L` of "local isomorphisms" (contains
  isomorphisms, stable under composition and base change), `W^L_S` (in `W` after every base change in `L`),
  `Ho^L_W(S) = (M/S)(W^L_S)^{-1}`. In Cat: `L` = local isomorphisms gives `W^g_S`; its saturation `L^` contains
  `Liss_W` ("J'ignore s'il est égal"); `HOT°_W(S) = (Cat/S)(W^g_S)^{-1} ≃ (Prop_W S)(W^u_S)^{-1}` and
  `HOT_W(S) = (Cat/S)(W^d_S)^{-1} ≃ (Liss_W S)(W^u_S)^{-1}`: smooth and proper maps play complementary roles;
  proposed axioms (a), (b), (c) for a pair `Liss, Prop ⊂ Fl(M)`; question whether `Δ^` or Top has such a duality.
- **§6 (ms. 227–234), "Cofibre `W`-homotopique dans Cat"** (the passage the POLES prompt calls the mapping
  cylinder). Standing hypothesis: **`W` satisfies W(7 bis)** (and W(7) for one implication, footnote 124:
  a) open Dwyer immersions are `W`-cofibrations; b) in a cocartesian square on an open Dwyer immersion `i`,
  `i ∈ W ⇔ i' ∈ W` and `p ∈ W ⇔ q ∈ W`; c) they are stable under cobase change and composition).
  Interval `I = Φ_n = (0 → 1 ← 2 → … ← 2n)`, `n ≥ 2`, so that `{0, 2n} → I` is an open Dwyer immersion.
  Cylinder `Z(f) = (X × I) ⊔_{X} Y` (glued along `inj_0`), factorization `X → Z(f) → Y` with `i_f` an open Dwyer
  immersion and `p_f ∈ W` (p_f is a retraction of `Y → Z(f)`, a cobase change of `inj_0`).
  **Proposition 16** (ms. 231): on `Cofib_W(S) ⊂ S\Cat`, a map in `W` between two `W`-cofibrations under `S` stays
  in `W` after every cobase change `S → S'`. ms. 232–234: a cocartesian square on a `W`-cofibration is
  "`W`-cocartésien" (in the sense of Déf. 3, ms. 131, i.e. homotopy cocartesian), via a) squares on Dwyer
  immersions, b) squares with two opposite sides in `W`, c) composition.
  *Caution for the reviews (corrected after POLES):* open Dwyer immersions ARE `W`-cofibrations for every fundamental localizer in the sense of Cisinski, and the factorization holds for all of them (POLES B.4, A.11); what fails for `W-infinity` is only the reverse half of footnote 124 b) (`i' in W => i in W`, `q in W => p in W`), by the cylinder of `A -> e`, `A` acyclic not contractible (POLES B.8).

- **§6 continued (ms. 234–239)** [DER_XIIc-b.tex]. Prop. 17: a commutative square `Q` is `W`-cocartesian iff the
  inclusion `𝒳 → 𝒳_Q` (integral of the span into the integral of the square over `Δ¹ × Δ¹`) is in `W`.
  Prop. 18 (under W(7 bis); footnote 127: "devrait être vrai dans toute catégorie de modèles ayant assez de
  cofibrations"): pasting law for `W`-cocartesian squares (square 1 cocartesian ⇒ (2 ⇔ 3)); the step (∗∗) uses
  W(7 bis) for closed immersions. Corollaire: under W(7 bis) a cocartesian square on a `W`-cofibration is
  `W`-cocartesian. Conclusion (ms. 239): "Il y a une telle théorie [des cofibres `W`-homotopiques] dans Cat,
  pourvu seulement que `W` satisfasse à W(7 bis)".
- **§7 (ms. 240–264), "Retour sur l'axiomatique de la fibre `W`-homotopique".** For `(M, W)`, `W` weakly
  saturated, with final object and fibre products: **left factorization axiom**: every `f` factors as `p_f i_f`,
  `i_f ∈ W`, `p_f ∈ Fib_W` (ultrastrong fibrations). Footnote 129: then `(M, W, Fib_W)` is a "catégorie à
  cofibrations [sic: fibrations] de K. S. Brown–Anderson, et tout est O.K."; footnote 130: sufficient only when
  every object is `W`-fibrant over `e`. Dual: **right factorization axiom** (`j_f ∈ Cofib_W`, `q_f ∈ W`).
  Under left factorization: homotopy fibre of `X_1/S` at `X_2/S` is symmetric (ms. 241–242);
  `Ho_W(I) := M(I)W(I)^{-1}`, `M(I) = Hom(I°, M)`; Prop. 18 (second of that number, ms. 246): the product
  `Ho^lc_W(S) × Ho^lc_W(S) → Ho_{W,S}(Φ)`, computed after fibrant replacement; Corollaire: it is the cartesian
  product in `Ho^lc_W(S)`. Lemme (ms. 248): an adjoint pair compatible with localizers induces an adjoint pair
  on the localizations. **Théorème (ms. 253):** `i^*: Ho_W(Ψ~) → Ho_W(Ψ)` has a right adjoint `i_*`, computed by
  the fibre product after replacing one leg by a `W`-fibration (modulo Lemmes 1 and 2, ms. 249, 251, whose proofs
  are postponed: "Je le ferai demain"); left adjoint `i_!` by the initial object. Cor. 1: `p_{Ψ *} = ε_3^* i_*`
  (homotopy fibre product = homotopy limit). **Prop. 19 / Définition (ms. 258–259): `W`-cartesian squares**
  (independent of the factorization); Cor. 1: `Q ≅ i_* i^* Q` (converse if `W` strongly saturated); Cor. 2:
  pasting; Cor. 2 (bis): if `p_i ∈ W` then `Q` is `W`-cartesian iff `f_i ∈ W`. Dual theory of `W`-cocartesian
  squares under right factorization. **Prop. 20 (ms. 262):** in Cat, for `W` with W(7 bis), `Q` is
  `W`-cocartesian in the general sense iff `φ_Q: 𝒳_Q = ∫(X_1 ← S → X_2) → X_3` is in `W` (the "integral"
  definition of ms. 131). Footnote 134: uses "W(3) (forme forte), i.e. Loc (3 bis) avec les notations de XVI".
- **§8 (ms. 265–275), "Appendice : retour sur les axiomes W(7), W(7 bis)"** (footnote 135: "Réflexion
  provisoire, supplantée par XVI"). The text says "On a vu (prop. 6, p. 78) que W(7 bis) implique W(7)"; this is backwards: Prop. 6 is W(7) ⇒ W(7 bis) (POLES G.15). **Proposition (ms. 265):**
  assume W(7 bis); for a morphism `f = (f_0, f_1, f_2, f_3)` of `W`-cocartesian squares `X → Y`, with
  a) `f_0 ∈ W`, b) `f_1, f_2 ∈ W`, c) `f_3 ∈ W`: **a & b ⇒ c; b & c ⇒ a; and a & c ⇒ b if `W` is stable under
  direct factors (retracts).** Proof: reduce to `f_i` open Dwyer immersions; cofibre ("mapping-cone")
  `Z(g) = T ⊔_S e`; W(7 bis) gives `g ∈ W ⇔ Z(g)` `W`-aspherical for `g ∈ Cof_W`; Lemma (ms. 268): the square
  of cofibres `Z_•` is `W`-cocartesian ("déploiement des diagrammes cubiques", not written; only W(7 bis)
  needed); then: a′ & b′ ⇒ c′ by the direct part of W(7 bis); **b′ & c′ ⇒ a′ by "la partie inverse
  (« inhabituelle ») de W(7 bis)"** (ms. 270: `j_2 ∈ W ⇒ i_2 ∈ W`); c′ & a′ ⇒ b′ by cobase change to `Z_0 = e`,
  where `Z_2` is a retract of `Z_3`.
  **Footnote 136 (ms. 266):** "C'est un peu vif, car il n'est pas clair que `X'_1 ⊔_{X_0} X'_2 → X_1 ⊔_{X_0} X_2`
  soit dans `W`, sans utiliser déjà un des trois ingrédients de W(7) (savoir `f_0, f_1, f_2 ∈ W ⇒ f_3 ∈ W`). Il
  semble donc que notre argument ne marche que moyennant une hypothèse supplémentaire de cet ordre … Mais il y a
  le lemme de Brown, cf. XVI §3, notamment p. 20."
  **Théorème (ms. 272–274), general `(M, W)` with a theory of `W`-homotopy cofibres** (footnote: for `(Cat, W)`
  this is known only with the weak form of W(7); "le lemme de Brown sauve la situation, cf. XV [sic] §3"):
  1°) a & b ⇒ c. 2°) (with final object `e`) b & c ⇒ a for all `f` ⇔ **axiom of conservative `W`-cocartesian
  squares** (`j_1 ∈ W ⇒ i_1 ∈ W` in a `W`-cocartesian square) ⇔ **Cons 1** (for `f: S → T` in `Cof_W` with
  cofibre `U = T ⊔_S e`: `U ∈ Asph_W ⇒ f ∈ W`) **and Cons 2** (for a [co]cartesian square with `i_1, i_2 ∈ Cof_W`:
  `Z_1, Z_2, Z_3` aspherical ⇒ `Z_0` aspherical). 3°) if direct factors of `W`-aspherical objects are
  `W`-aspherical and `M` has a final object: c & a ⇒ b; Cor. 1: equivalent to: in a `W`-cocartesian square,
  `Z_0, Z_3` aspherical ⇒ `Z_1, Z_2` aspherical (also with `Z_0 = e`). Cor. 2: under all three, two of a, b, c
  imply the third.

*Remarks for the POLES review.* (i) Cons 1 is the **cofibre criterion** (POLES Lead 1): a cofibration with
`W`-aspherical cofibre is in `W`. For `W∞` it fails (acyclic non-contractible `X`: `∅ ≠ pt → X`… more exactly a
map whose cofibre is contractible need not be a weak equivalence, e.g. `X → pt` suspended; the plus
construction); for `W_Z` (integral homology) it holds by the long exact sequence. So Cons 1 separates the
homological localizers from `W∞`. (ii) "inhabituelle" (ms. 270) is Grothendieck's own word for the converse
direction of W(7 bis); TOTASPH A.13 showed that `W∞` fails exactly this. (iii) The proof on ms. 265–272 has the
gap he flags in footnote 136; XVI §3 (Brown's lemma) is where he repairs it.


## Chapter XVI (ms. 1–124): "Les localiseurs fondamentaux"  [DER_XVI.tex; edition of 18 March 2019]

The axioms are renumbered here; **the numbering differs from Chapter XII** (old W(1), W(2 bis), W(3) = new
Loc (1), Loc (3), Loc (2); old W(2) = Loc (3 bis); old W(5) = Loc (5); old W(7 bis) = Loc (6′); old W(7) ≈ Loc (6);
old W(4) = Loc (7); old W(6) = Loc (8)).

### §1 (ms. 1–8): Loc (1)–Loc (3)

- **Loc (1)** saturation: a) isomorphisms; b) two out of three; c) `gf, fg ∈ W ⇒ f, g ∈ W`. (a, b = "saturation
  faible"; a, b, c = "saturation modérée".) **Loc (1 bis)**: in addition d) `W` stable under direct factors
  (retracts). **Loc (1 ter)**: `W` strongly saturated (`hot_W(f)` iso ⇒ `f ∈ W`). Notation `W^♮` for the strong
  saturation (used at 3.5.2).
- **Loc (2)** final object ⇒ `W`-aspherical. **Loc (2_0)**: `Δ¹` is `W`-aspherical.
- **Loc (3)** localization, weak form: a `W`-aspherical `f: X → S` (all `X/s` `W`-aspherical) is in `W`.
  Footnote 1: "il faudrait intervertir les notations pour Loc (3) et pour Loc (3 bis), car ce dernier m'apparaît
  comme le plus important"; it holds for every `W_D`, `D` a derivator (or a prederivator with Der 2, 4, 5).
  **Loc (3 bis)** strong form: an `S`-morphism `f: X → Y` with all `f/s: X/s → Y/s` in `W` is in `W`.
- Rappel 1: Loc (1, 2, 3) ⇒ `W = W°`. **Déf. 1.1: localiseur fondamental = Loc (1, 2, 3).** Rappel 1.2:
  homotopisms are in `W`; homotopic maps have the same image in `Hot_W`.
- Prop. 1.3: Loc (1, 2, 3) ⇔ Loc (1, 2_0, 3′); Loc (1, 2, 3 bis) ⇔ Loc (1, 2_0, 3′ bis), where Loc (3′) =
  (a) a split fibred category over `S` with `W`-aspherical fibres maps to `S` by a map in `W`, and (b)
  `i_X: X → Φ_S(X)` is in `W`; Loc (3′ bis) = (a) a cartesian functor of split fibred categories that is in `W`
  fibrewise is in `W`, and (b).

### §2 (ms. 8–15′): Loc (4), Loc (5)

- **Loc (4)** direct sums: `∐ f_i ∈ W ⇔` all `f_i ∈ W`. = Loc (4 a) (if) + Loc (4 b) (the inclusion of a direct
  summand `S_0 ⊂ S` is in `Fib_W`). Cor. 2.2: the finite form Loc (4 a_0) ⇔ every object is `W`-cofibrant
  (`∅ → X ∈ Cof_W`). Rappel 2.3: finite products of maps of `W` are in `W` (editors: needs Loc (3 bis)).
  Prop. 2.4: finite products exist in `Hot_W`, and sums under Loc (4 a). Lemmas 2.5, 2.6 (adjoint pairs
  compatible with localizers).
- **Loc (5)** connectedness / non-triviality: `f ∈ W ⇒ π_0(f)` bijective. Prop. 2.7: ⇔ `π_0` factors through
  `Hot_W` ⇔ `Hot_W \ {∅}` is not equivalent to a point ⇔ `Hot_W` is not equivalent to `e` or `Δ¹`. Footnote:
  if `W` is strongly saturated, ⇔ `W` is neither `Fl(Cat)` nor `Fl(Cat^*) ∪ {id_∅}`; if `W` satisfies
  Loc (7 D_{W_ω}), ⇔ `W ≠ Fl(Cat)` (XII Th. 2, ms. 20). Prop. 2.8: under Loc (5), `π_0: Hot_W → Ens` is both left
  and right adjoint to `I ↦ I_W`; `Hom_W(e_W, X) ≅ π_0(X)` (2.8.4). Cor. 2.13: `∅` is a strict initial object of
  `Hot_W`. Lemma 2.14.
- Commentaire final (ms. 15′): Loc (5) is the only axiom that is not a stability axiom (all others hold for
  `W = Fl(Cat)`). Loc (4 a_0) follows from Loc (6 a); Loc (4 a) from Loc (6 a) + Loc (8); Loc (4 b) from Loc (7).

### §3 (ms. 16′–27): Loc (6), the axiom of `W`-cofibrations (cocartesian squares, "Mayer–Vietoris")

- **Loc (6)**: for a morphism `f = (f_0, f_1, f_2, f_3)` between two **MV squares** (`X_3 = X_1 ∪ X_2` union of
  two open subcategories [sieves], `X_0 = X_1 ∩ X_2`):
  **a)** `f_0, f_1, f_2 ∈ W ⇒ f_3 ∈ W`; **b)** `f_1, f_2, f_3 ∈ W ⇒ f_0 ∈ W`; **c)** `f_0, f_3 ∈ W ⇒ f_1, f_2 ∈ W`.
  Footnote 13: "Je vais désigner par Loc (6) l'axiome Loc (6 a, b), sans y inclure c." Footnote 10: for (6 a) it
  seems enough to take `f_0, f_2` isomorphisms. NB (ms. 17′): `W_0` (bijections on `π_0`) satisfies a) and not
  b); "je présume (sans avoir vérifié) que c'est pareil pour les `W_n`".
- **Loc (6′)** (Mayer–Vietoris, = old W(7 bis)): in an MV square, **a)** `i_1 ∈ W ⇒ j_1 ∈ W`; **b)**
  `j_1 ∈ W ⇒ i_1 ∈ W`.
- Prop. 3.1: (6 a) ⇒ (6′ a); (6 b) ⇒ (6′ b); (6 c) ⇒ (6′ a, b) [even ⇒ (6 a, b)].
- Commentaire 3.2: (6 a) is the "minimum vital" for a theory of `W`-homotopy cofibres: with it, open Dwyer
  immersions are in `Cof_W` and MV squares are `W`-cocartesian. He admits the proof in XII Appendix (ms. 265 ff.)
  is incomplete (it tacitly assumes Dwyer immersions are in `Cof_W`).
- **Lemme 3.2.1 (K. S. Brown, "cité par Baues")**: `(M, W)` with `W` moderately saturated and `C ⊂ Fl(M)` such
  that 1) `C` is stable under composition and cobase change, contains the isomorphisms; 2) `M` has an initial
  object and every `∅ → X` is in `C`; 3) every map factors as `p i`, `i ∈ C`, `p ∈ W`; 4) `C ∩ W` is stable
  under cobase change. Then **`C ⊂ Cof_W`**. ("Mais je ne sais pas prouver le lemme…") Cor. 3.2.2: under 1–3:
  (4) ⇔ `C ∩ W ⊂ W^univ` ⇔ `C ⊂ Cof_W` ⇔ cobase change of `p ∈ W` along `i ∈ C` is in `W`.
  Applied to Cat with `C` = open Dwyer immersions: 4) follows from Loc (6′) ("on a besoin apparemment de
  Loc (6′ a et b)").
- **Prop. 3.3**: Loc (6′) ⇔ Loc (6 a, b); both are implied by Loc (6 c); if `W` is stable under direct factors
  (Loc (1 bis)), Loc (6′) ⇔ Loc (6 c) ⇔ Loc (6 a, b, c).
- Commentaire 3.4: under Loc (6′) the theory is "de nature très particulière, puisque les carrés
  `W`-cocartésiens sont « réversibles »". **Question (ms. 23, marked "?‖"): does Loc (6′ a) imply that the
  `W`-trivial open Dwyer immersions are stable under cobase change** (equivalently Loc (6 a))? "Je ne vois aucun
  moyen de le prouver." Footnote 18: yes in the presence of Loc (8, 9).
- 3.5 summary: (6 c) ⇒ (6) ⇔ (6′); if `W = W^♮`, all three equivalent; (6 a) ⇒ (6′ a), converse unknown.
- **Prop. 3.6**: Loc (6 a) ⇔ **Loc (6 A)** (Cat has enough `W`-cofibrations: every `f = p i`, `i ∈ Cof_W`,
  `p ∈ W`; then `(Cat, W, Cof_W)` is a Brown–Anderson category with cofibrations) + **Loc (6 B)** (MV squares are
  `W`-cocartesian). Footnote 19: (6 B) follows from (6 A), so (6 A) ⇔ (6 a) (sketch at 4.4.15, ms. 66–68).
  **Loc (6 A′)**: every Dwyer morphism is in `Cof_W`. **Cor. 3.7**: Loc (6) ⇔ (6 A) + (6 B) + **Loc (6 C)**
  (in a `W`-cocartesian square, `j ∈ W ⇒ i ∈ W`). ms. 27: "je soupçonne que Loc (6 c) n'est guère vérifiée que si
  `W = W^♮`".


### §4 (ms. 27–70): Loc (7), the axiom of `W`-fibrations

- 4.1: **weak `W`-fibration** (the "`W`-fibration" of XII Th. 3, ms. 51–52; "désormais détrônée"): (Ff) for
  all `S'' → S'` over `S` with `S', S''` contractible, `X'' → X'` is in `W`; `Fibf_W`. **`Fib_W`** = the
  `W`-fibrations proper: base change along `f` maps `W_S` into `W_{S'}` (the "ultrafortes" of XII).
  Classes (4.2.1): `Parf_{W_0} ⊂ Parf_W ⊂ Fibf_W ⊃ 𝓕_W := Catfib^W` (Cat-fibrations whose transition functors
  are in `W`) `⊃ 𝓕_{W_0}`; `Fib_W ⊂ Fibf_W`; `W_0 ⊂ W` a reference localizer (`W_ω`, or `W∞`, or `W`).
  Every map factors as `p i` with `i ∈ W_ω`, `p ∈ Parf_ω` (path categories, VII), also with `p ∈ Catfib^ω_0`.
- 4.3: **Loc (7)**: **a)** `𝓕_W ⊂ Fib_W`; **b)** a map `f ∈ W` between two objects of `𝓕_W` over `S` is
  fibrewise in `W`; **c)** `𝓕_W ∩ W ⊂ W^u` (fibres `W`-aspherical); **F)** Cat has enough `W`-fibrations (every
  `f = p i`, `i ∈ W`, `p ∈ Fib_W`): `(Cat, W, Fib_W)` is a category with fibrations (text says "à cofibrations",
  sic). a ⇒ b ⇒ c (⇒ F). Footnote 24: the functors `f_!` for `HOT_W` need only Loc (3 bis). ms. 37: "Il me
  semble peu probable que Loc (7 b), ni même Loc (7), implique Loc (6 a), ni même Loc (6′ a)".
- 4.4: for a class `𝓕`: **A(𝓕)**: `𝓕 ⊂ Fib_W`; **B(𝓕)**: `Fl(𝓕_S) ∩ W_S ⊂ W^u_S`; **C(𝓕)**: `𝓕 ∩ W ⊂ W^u`.
  Lemma 4.4.1 (any model category): if every map is `p i`, `i ∈ W`, `p ∈ 𝓕`, then A(𝓕) ⇒ enough fibrations ⇒
  B(Fib_W) ⇒ B(𝓕). Lemma 4.4.3 (**dual Brown lemma**): if `𝓕` is stable under base change and composition,
  contains isomorphisms and all `X → e`, and every map is `p i` (`i ∈ W`, `p ∈ 𝓕`), then A(𝓕) ⇔ B(𝓕) ⇔ C(𝓕).
  Cor. 4.4.4: for `Parf_W`, `Parf_{W_0}` the three are equivalent: conditions **D = D_W**, **D_{W_0}**
  (`Parf_{W_0} ∩ W ⊂ W^u`, equivalently `Parf_{W_0} ⊂ Fib_W`). Cor. 4.4.5: A ⇒ B ⇒ C and
  A ⇔ C + Comp(𝓕_W) ⇔ C + Comp(Fibf_W). Lemma 4.4.9, Cor. 4.4.10: A(𝓕_W) ⇔ A(Fibf_W), same for B, C.
  Cor. 4.4.11–12: if `W_0` satisfies Loc (8 bis), D_{W_0} ⇒ A_{W_0}; if `W` and `W_0` do, D_{W_0} ⇒ A (uses the
  infinite-path factorization `Φ_∞` of VI ms. 193 ff.).
- **Théorème 4.4.13** (summary): (1) A ⇒ B ⇒ C ⇒ D ⇒ D_{W_0}, A_{W_0} ⇒ B_{W_0} ⇒ C_{W_0} ⇒ D_{W_0},
  X ⇒ X_{W_0}; the weakest is **D_{W_ω}**: `Parf_{W_ω} ∩ W ⊂ W^u`; D_{W_0} ⇒ F. (2) If `W`, `W_0` satisfy
  Loc (8 bis) the eight conditions are equivalent. (3) If `W_0` satisfies Loc (8 bis), the four `_{W_0}`
  conditions are equivalent. (4) a) if `W_0` satisfies Loc (7 F), A_{W_0} ⇔ B_{W_0} ⇔ C_{W_0}; **b) if `W` is
  strongly saturated and satisfies Loc (3 bis), B ⇒ A** (XII Prop. 1, ms. 54; uses `HOT_W` and `f_!`).
- 4.4.14 (ms. 63–66): open questions: D ⇒ A without Loc (8 bis)? D_{W_0} ⇒ A? and "la plus substantielle":
  **F ⇒ A?** — answered at 4.16: **false**, by `W_0` (bijections on `π_0`, written **W**_0): it satisfies
  Loc (1 ter, 2, 3 bis, 4, 5, 6 a, 8, 9) and Loc (7 F), but not Loc (6 b) and not D_{W_ω} (the `n`-fold covering
  `S¹ → S¹` realized by a `W_ω`-parfait map; I ms. 87). Factorization for **W**_0: `X̄ = ∐_{α ∈ π_0 X} Y_{f(α)}`.
  ms. 70: "peut-être même Loc (7 F) — il faudrait que je teste sur les **W**_n".
- 4.4.15 (ms. 66–68): if Cat has enough `W`-cofibrations (Loc (6 A)), then under Loc (3 bis) (perhaps
  Loc (1 ter)) open MV squares are `W`-cocartesian, i.e. Loc (6 A) ⇒ Loc (6 a) ("sans vérifier avec soin").

### §5 (ms. 71–83): Loc (8) limits, Loc (9) accessibility

- **Loc (8)**: `W` stable under filtered colimits; **Loc (8 bis)**: under countable (sequential) ones.
  The canonical factorization `f = p i` (`i ∈ W_ω`, `p ∈ Parf_{W_ω}`) commutes with filtered colimits.
  Prop. 5.1: under Loc (7 D_{W_ω}), Loc (8) ⇔ `Asph_W` is stable under filtered colimits.
- **Loc (9)**: `W` is an accessible subset of `Fl(Cat)` (XVIII §§8, 13). Prop. 5.3.1, Cor. 5.3.2: for `W`
  stable under filtered colimits, `π`-accessible ⇔ every `f ∈ W` is a `π`-filtered union of maps `f_j ∈ W`
  between subcategories of cardinal ≤ π.
- **Théorème 5.4 (ms. 79):** `W∞` satisfies Loc (9), "en fait, il satisfait à tous les axiomes vus jusqu'à
  présent, savoir Loc (1 ter, 2, 3 bis, 4, 5, 6, 7, 8, 9)"; it is `ℵ_0`-accessible. Proof sketched via Lemma 5.5
  (reduction to `Asph_W` under D_{W_ω}), Lemma 5.6 (`W_0` is `ℵ_0`-accessible) and the criterion "all `Ω^n(X, x)`
  0-connected" (XII ms. 190).
  *Note:* "Loc (6)" for `W∞` in this list includes Loc (6 b) (= (6′ b), the converse Mayer–Vietoris direction for
  sieves), which TOTASPH A.13 shows false for `W∞`. So **Théorème 5.4 as stated is false in its parenthesis**
  (Loc (6 a), (6′ a) hold; (6 b), (6′ b), (6 c) fail). To be checked against what POLES says.

### §6 (ms. 83–96): Loc (5, 7 D_{W_ω}) implies `W ⊂ W∞`

- **Théorème 6.1 (ms. 83):** a fundamental localizer satisfying D_{W_ω} is `Fl(Cat)` (if Loc (5) fails) or is
  contained in `W∞`. Lemma 6.2: if `W` satisfies D_{W_ω}, then `W ⊂ W'` ⇔ `Asph_W ⊂ Asph_{W'}`. Proof of 6.1 via
  `Ω¹(X, x)` = fibre of `Ch(X; x, −) → X`. **Cor. 6.3: `W∞` is the largest fundamental localizer satisfying
  Loc (5, 7 D_{W_ω})**, hence also the largest satisfying Loc (5, 7). Announced: a characterization by a
  "descent axiom" Loc (10).
- **6.4 (ms. 86–91).** a) All localizers used so far contain `W∞` (`W_n`, homological, rational…), so none except
  `W∞` satisfies even D_{W_ω}. b) Does a fundamental localizer strictly inside `W∞` exist? "Je n'ai pas même
  prouvé que `W_ω ≠ W∞`, alors que je n'ai pas le moindre doute" — editors: **Cisinski proved `W_ω = W∞`**.
  `W̃∞` := the smallest localizer satisfying Loc (1 ter, 2, 3 bis, 4, 6, 7, 8); conjecture `W̃∞ ≠ W∞`
  (editors: "non par Cisinski"); suspected relation with Whitehead's simple homotopy types (footnote 41:
  "Canulé (?)"). c) Loc (7 F) is not a stability axiom; D_{W_ω} is the "minimum vital" for handling homotopy
  fibres; "Il est remarquable que ceci implique `W ⊂ W∞`, et que cela exclut toutes les variantes considérées à
  ce jour de la notion de type d'homotopie".
- 6.5 (ms. 92–96): the Whitehead idea "s'évanouit" (footnote 44: perhaps not); homotopism in Cat is strictly
  finer than homotopy of realizations (`I` = boundary of the 2-simplex as a poset, `sd(I)` the hexagon: no
  order-preserving `I → sd(I)` is a homotopism; ms. 94 is missing in the edition). Question: is `sd(I)`
  homotopic to `I` in Cat? A hypothetical "Whitehead localizer".

### §7 (ms. 97–124): comments on the axioms

- 7.1 questions: 1) when is `(Cat, W, Cof_W)` / `(Cat, W, Fib_W)` a category with cofibrations / fibrations;
  1 bis) when is `W` part of a closed Quillen triple; 2) existence of `f_!`, `f_*`, exactness; 3) which Der
  axioms hold for `HOT_W`; 4) when is `HOT_W` a derivator on all of Cat.
- 7.2: Loc (6 a) ⇒ cofibration structure (necessary under Loc (3 bis)); functorial mapping-cylinder
  factorization with `i` an open Dwyer immersion. 7.3: the `f_!` exist under Loc (3 bis) alone: Der (4*, 5*);
  Der (6*) with Loc (6 a). 7.4: Loc (7 F) is known only via D_{W_ω} (or for **W**_0); "l'axiome Loc (7 D_{W_ω})
  me paraît de nature considérablement plus forte que Loc (6 a), lequel (si je ne m'abuse) est vérifié pour tous
  les localiseurs qui ont été envisagés jusqu'à présent".
- **7.5:** if `W` satisfies **Loc (6 a, 8, 9)** (footnote 50: even **Loc (6′ a, 8, 9)**), `HOT_W` is a
  derivator on all of Cat (via a test category `A`, `W_A ⊂ Fl(A^)`, closed Quillen triple with
  `C = Mono(A^)`; XV 8.4, 7.4, 10.1; XIX 2.3, 2.6, 2.9), and `W` is strongly saturated. These axioms do not
  imply Loc (7) (example **W**_0); whether they imply Loc (7 F) is left open ("Je ne hasarderais aucune
  conjecture").
- 7.6 table: cofibration structure: Loc (6) (+ (3 bis)?); fibration structure: D_{W_ω}; Der (4*, 5*):
  Loc (3 bis); Der (4*, 5*, 6*): Loc (3 bis, 6 a) or Loc (6′ a, 8, 9); Der (4, 5, 6) on Cat "et tout le reste":
  Loc (6′ a, 8, 9); Der (4, 5, 6) on finite posets: D_{W_ω} (or only Loc (7 F)). Der (1): no hypothesis;
  Der (2): Loc (6 a) or D_{W_ω}; Der (3): Loc (3 bis) or Loc (6′ a, 8, 9). An `f: S → T` is a
  `HOT_W`-equivalence iff `hot_W(f)` is an isomorphism (under Loc (3 bis)).
- 7.7: Prop. 7.7.1 (closed Quillen triples "spéciaux" / "très spéciaux" give Der axioms; `W_D` is a fundamental
  localizer with Loc (1 ter, 3 bis)); Cor. 7.7.2: Loc (6′ a, 8, 9) ⇒ Loc (1 ter, 3 bis) — footnote 56:
  "**Loc (3 bis) pas prouvé, probablement faux**"; footnotes 55, 58: the recovery `W = W_{HOT_W}` is proved only
  with Loc (3 bis) ("Gare au cercle vicieux").
- **7.8 (ms. 119–123):** Loc (3 bis) ⇒ Der (4*, 5*); Loc (3 bis, 6 a) ⇒ Der (1, 2, 3, 4*, 5*, 6*);
  **Loc (6′ a, 8, 9) ⇒ all derivator axioms (+ Loc (1 ter))**. Definition: **"localiseur (fondamental)
  spécial"** = Loc (6′ a, 8, 9) (footnote 57: perhaps add Loc (3 bis)). Loc (4), (5), (7), (6 b) "n'interviennent
  absolument pas". Question (ms. 122–123): is the smallest localizer `W ⊂ W∞` satisfying Loc (6′ a, 8) (or
  Loc (3 bis, 6′ a, 8)) special, and is it `≠ W∞`? ("Je suis persuadé que c'est le cas".)
- 7.9: Thomason's closed model structure for `W∞`; does it extend to localizers satisfying Loc (6′ a, 8, 9)?
  That would give Loc (6 a) and Loc (7 F). To test: homological equivalences, **W**_n.

*Remarks for the POLES review (mine).*
1. By Cisinski (2004, Th. 2.2.11; recalled by the editors at ms. 87) `W_ω = W∞`: every fundamental localizer
   contains `W∞`. With Théorème 6.1 this gives: **the only fundamental localizers satisfying D_{W_ω} are `W∞` and
   `Fl(Cat)`**; so `W̃∞ = W∞`, the question of ms. 122–123 b) has answer "equal", and Grothendieck's expectation
   of a world of localizers below `W∞` is void. "Two poles": fibration side (only `W∞`) and cofibration side
   (Loc (6′)-type axioms, homological localizers).
2. Loc (6′ b) / Loc (6 b) / Loc (6 C) (reversibility) fails for `W∞` (TOTASPH A.13: `A ⋆ {t, s}` with `A`
   acyclic not aspherical) and holds for `W_Z`-type localizers; Grothendieck did not know this for `W∞`
   (Th. 5.4 lists Loc (6) for `W∞`). The proper accessible localizers containing `W∞` correspond (Cisinski,
   Ast. 308) to left Bousfield localizations of spaces; the reversible ones should be the "stable"/homological
   ones: this is POLES Leads 2, 3, 6.
3. Loc (6′ a) for sieves is **weaker than it looks for `W∞`-like classes**: the class of Dwyer immersions used
   by Grothendieck is the one of XII ms. 107–114 (crossing presheaves), and TOTASPH F shows which sieves are
   `W`-cofibrations. Question 3.4 (ms. 23) "(6′ a) ⇒ (6 a)?" is answered by footnote 18 only under Loc (8, 9).

## Chapter I, second half (ms. 60-126)  [DER_I-b.tex; read for return 4, GALOIS]

- ms. 60 ("tres gros canular"): for a strict hot-equivalence f, F -> f_* f^* F is an isomorphism only for
  CONSTANT F; false in general already for the inclusion of an initial object.
- Def. 1 (ms. 61): **D-equivalence**: f^* fully faithful on constant coefficients, i.e.
  Hom(q^*M, q^*N) -> Hom(p^*M, p^*N) bijective for all M, N in D(e). Prop. 1: iff iso on D-cohomology (or
  D-homology) with constant coefficients. Rem. 2: invariant under homotopy of f. Prop. 2: two out of three.
  Def. 2: X is D-aspherical (D-contractile) if X -> e is a D-equivalence. Example: HOT-equivalence = weak
  equivalence.
- Prop. 2 (second, ms. 63) for a left derivator: (a) f is a D-equivalence universally for local isomorphisms
  Y' -> Y  <=>  (b) all X/y -> Y/y are D-equivalences  <=>  (c) all X/y are D-contractile. Footnote 25: also
  (d) M_Y = f_* f^* M_Y for constant M_Y, (d') same for locally constant. Prop. 2' dual. Def. 3 (ms. 65):
  strict / costrict D-equivalence; footnote 27: better names D-aspherique / D-coaspherique.
- Prop. 4, **Theoreme 1 (ms. 66-67)**: equivalent: (a) all y\X are D-contractile; (b) for EVERY F in D(Y),
  H^*_D(Y, F) = H^*_D(X, f^*F); (c) f_!(M_X) -> M_Y iso for all M.
- ms. 67-68: axioms renumbered: Der 1, Der 2; **Der 3** (X contractile => p^* fully faithful; footnote 28:
  variants Der 3 a) b) c) at ms. 97 and 111-112); Der 4 (g), (d) existence of f_*, f_!; Der 5 (g), (d) fibres.
- **Theoreme 2 (ms. 68-69)**: equivalent conditions on f: (a) X_{y0} -> X/y0 costrict D-equivalences;
  (b) x0\X -> y0\Y has D-contractile fibres; (c) formation of f_* commutes with every base change,
  universally; (c'), (c''); (d) base change of a coaspherical p is coaspherical; (d'), (d'').
  [this is the later "D-propre".]
- Def. 4 (ms. 70): **D-propre** (conditions of Th. 2), dual **D-lisse**. Cor. 2: proper or smooth with
  D-contractile fibres => universal D-equivalence. Cor. 3: then f^* is fully faithful on all of D(Y). Prop. 5:
  stability under base change and composition; closed immersions proper, open immersions smooth. Prop. 6:
  fibrewise D-equivalence between two proper (or two smooth) S-categories is a D-equivalence. Th. 3 (ms. 72):
  base change p^* f_* = f'_* q^* if f proper or p smooth.
- ms. 72-75, "Comparaison de X et X^o": Phi(X) (objects: arrows of X; twisted arrow category), p_X: Phi(X) -> X
  (target), q_X: Phi(X) -> X^o (source); Phi(X^o) = Phi(X); fibres (X/x)^o and y\X. Prop. 1: p_X, q_X are strict
  hot-equivalences. Cor. 1-2: X is D-contractile iff X^o is; f is a D-equivalence iff f^o is.
- **D-fibrations (ms. 76-78).** Prop. 1: equivalent: (a) X_y -> X/y and X/y_1 -> X/y_0 are D-equivalences;
  (b) for constant F on Y, f_* f^* F is locally constant and computed fibrewise. (Footnote 33: "localement
  constant" = restriction maps G_{y'} -> G_y isomorphisms; whether such G is constant on each Y/y needs
  Der 3 a').) Def. 1: **D-fibration cohomologique (gauche)**; dual **homologique (droite)**. Stable under base
  change by local isomorphisms / D-smooth maps (resp. dual), not under arbitrary base change (footnote 34:
  "donner exemple!"); ms. 77-78: attempt at an example over Delta_1, not conclusive.
- **Prop. 2 (ms. 79-81)**: for f: X -> Y: (a) base change of f preserves D-equivalences (Y'' -> Y' over Y);
  (b) f is universally a cohomological D-fibration; (b') universally a homological one. He claims a <=> b <=> b'.
  **His own footnotes 35-37: b) => a) is "canulee"** (counterexample ms. 89); a) must be restricted to Y', Y''
  Hot-aspherical (ms. 96) with axiom Der 3 a') (ms. 97); what is proved is a'): for Y'', Y' D-aspherical and
  1-connected (or with final objects, resp. initial objects). "Mais ca marche pour les derivateurs D_i associes
  aux localisateurs fondamentaux W_i (i-types)". Def. 2 (ms. 81): **D-fibration**. Prop. 3: (a) stable under
  base change and composition (footnote 38: "La stabilite par composition n'est pas claire"); (b) fibrewise
  D-equivalence between D-fibrations (or two left fibrations, or two right, or proper, or smooth) is a
  D-equivalence. Question (ms. 82): for a D-fibration f and ANY F, is f_* f^* F computed fibrewise?
- Prop. 4 (ms. 83): for f proper: D-fibration iff all X/y_1 -> X/y_0 are D-equivalences; "D-fibrations
  parfaites" = proper and smooth D-fibrations. Cor.: a Cat-cofibration is a D-fibration iff the transition
  functors are D-equivalences. Prop. 5: universal D-equivalence <=> D-fibration with D-contractile fibres.
  Def. 3: D-fibration triviale. **Prop. 6 (ms. 84)**: (a) for two left (or two right) D-fibrations over S, f is a
  D-equivalence if the f_s are, for s in a set S_0 meeting every component (Lemma ms. 85: f_{s_1} is a
  D-equivalence iff f_{s_0} is); **(b) "cette condition est aussi necessaire": footnotes 40-41: "Pas prouve!",
  then "Faux, cf. contre-exemple p. 87".**
- **Counterexample (ms. 87-90)**: the Klein bottle as a fibration X -> S = S^1 with fibre S^1 and monodromy
  z -> z^{-1}, realized by finite posets (S = the 4-element circle poset; X glued from S' x S-bar, S'' x S-bar by
  u_a = id, u_b = the reflection); f is proper and smooth, even Cat-fibrant and Cat-cofibrant; for
  D = Der(k-Mod) with 2 invertible in k, f is a D-equivalence (R f_* k = k + k[1]^twisted and
  H^*(S, k^twisted) = 0) but the fibre S^1 is not D-contractile. Footnote 43: simpler: the two-sheeted covering
  S^1 -> S^1 (n-sheeted if n invertible in k). Footnote 42: a still simpler one at ms. 93-94 (non-connected
  fibres).
- ms. 90: so the Klein-bottle f satisfies b), b') of Prop. 2 and not a): X x_S X -> X is not a D-equivalence
  although X -> S is. **Second counterexample (ms. 90-92)**: G finite of order n > 1 acting on Z, S = B_G,
  X = E_G x_G Z -> B_G; with n invertible in k, e -> B_G and E_G -> B_G are D-equivalences (all three are
  D-aspherical), X -> B_G is a proper and smooth D-fibration, H^*(X, k) = H^*(Z, k)^G -> H^*(Z, k) is not an
  isomorphism in general (G = Z/2 on S^1 by reflection): a D-fibre bundle over a D-ASPHERICAL base whose fibre
  inclusion is not a D-equivalence. ms. 93-95: poset version: E = S^2 with antipodal action, B = RP^2 (which is
  D-aspherical for 2 invertible), Z = S^1; barycentric subdivision of the globular poset (octahedron); 52
  vertices. Also contradicts Prop. 6 b).
- **ms. 96-100: the repair.** "il ne reste plus rien de la proposition 2". New condition a): test only on
  Y'' -> Y' with both **Hot-aspherical**. **Der 3 a)**: Z Hot-aspherical => Z -> e is a D-equivalence.
  **Der 3 b)**: Hot-equivalences are D-equivalences. **Der 3 a')**: for Z Hot-aspherical, moreover the
  essential image of D(e) in D(Z) is the locally constant objects (F with all F_{z'} -> F_z isomorphisms).
  He notes a') becomes false if "Hot-aspherical" is replaced by "D-aspherical" as soon as D-equivalence is
  weaker than Hot: "meme si D = D_i, la categorie des objets localement constants sur Z s'exprime en termes du
  (i+1)-type d'homotopie, mais pas en termes de son i-type seul" (ms. 97-98). **Der 3 b')**: a Hot-equivalence
  induces an equivalence on locally constant coefficients (footnote 50: b'_0 faithful, b'_1 fully faithful,
  b'_2 equivalence). Footnote 51: 0-complete left/right. Footnote 52: 1-completeness follows from the
  cohomological statement if LC has internal Homs compatible with inverse images.
  **Definition (ms. 99-100): f is a 1-complete D-equivalence if f^* is fully faithful on locally constant
  coefficients; 2-complete if f^* induces an equivalence of the categories of locally constant coefficients;
  Z is "completement D-aspherique" if Z -> e is 2-complete.** Der 3 a') <=> Hot-aspherical => completely
  D-aspherical; Der 3 b') <=> Hot-equivalences are 2-complete. **Der 3 a'')**: Z with a final or an initial
  object is completely D-aspherical. New definition of D-fibration (ms. 100): base change of 1-complete
  D-equivalences Y'' -> Y' gives D-equivalences; equivalent to b), b') of Prop. 2 under Der 3 a'').
- ms. 101-102: Def. 1: **D-equivalence cohomologique (complete)**: H^*(Y, F) = H^*(X, f^*F) for all locally
  constant F; dual homologique. Footnote 53: Der 3 b'_1 => Hot-equivalences are cohomological D-equivalences.
  Prop. 1 (sorites: composition; gf, f => g; gf cohomological and g 2-complete => f cohomological). Def. 2:
  **D-fibration cohomologique complete** (X_y -> X/y and X/y' -> X/y cohomological D-equivalences, universally).
  Prop. 2: then f_* F is locally constant for locally constant F on X, commutes with base change. Cor. 1: base
  change of a cohomological D-equivalence along a cohomological D-fibration is one.
- ms. 103-106: Prop. 3: complete cohomological D-fibrations are stable under base change and composition (via
  Cor. 2: f is one iff base change along it preserves cohomological D-equivalences). **Prop. 4 (under
  Der 3 a')**: equivalent: complete cohomological D-fibration; f_* F locally constant, fibrewise, universally,
  for locally constant F; preservation of cohomological D-equivalences; same tested on e -> Y' with Y' having a
  final object. Def. 3: **D-fibration complete** = cohomological and homological complete. He considers the
  stronger notion "base change of 1-complete D-equivalences is 1-complete" and says he cannot give interesting
  examples "faute d'avoir une description cohomologique ou homologique de la notion de D-equivalence
  1-complete" (ms. 105-106). ms. 106: if the LC_D(X) have a tensor product with internal Homs compatible with
  inverse images, then cohomological D-equivalence <=> 1-complete, hence also homological.
- ms. 107-110: search for HOT-fibrations. **Lemme (ms. 109), not proved by him**: f is a HOT-equivalence iff it
  is a Hot-equivalence, "et alors f est meme une HOT-equivalence 2-complete"; footnote 57: "Est-ce vrai aussi
  pour les derivateurs D_i?" He says the 2-completeness "me parait une propriete delicate du derivateur HOT".
- **ms. 111-113 (11.11.90): list of the variants of Der 3**: a), a'), b), b'_1), b'_2), b''_coh), b''_hom);
  implications b'_2 => b'_1 => b''_coh, b''_hom => b => a; b'_2 => a' => a. "Dans tous les cas a ma
  connaissance, les derivateurs satisfont la condition la plus forte Der 3 b'_2."
- Def. 1 (ms. 113): the four notions and their diagram: 2-complete => 1-complete => cohomological, homological
  => D-equivalence; with tensor and internal Hom: 1-complete <=> cohomological => homological (ms. 115).
  "Dans D = HOT, toutes ces notions devraient etre equivalentes ... Mais je ne connais que HOT comme derivateur
  ou la D-equivalence implique deja la D-equivalence cohomologique (complete)..."
- ms. 115-116: Prop. 1, Def. 2: the old "D-fibration cohomologique" renamed **D-fibration cohomologique
  faible**; Prop. 2: stable under smooth base change (dually proper); "Je devrais construire un exemple" where
  it is lost after base change.
- ms. 116-118: Prop. 3 (fibrewise criterion on a set S_0 of base points for weak cohomological fibrations);
  Prop. 4; **Prop. 5 (ms. 117)**: conditions a (test on Hot-aspherical Y'', Y'), a' (test on Hot-equivalences),
  a_1 (Y' with final object, Y'' = e), a_2 (initial object), b_1, b_2 (universally weak cohomological /
  homological fibration): a' => a => a_1 <=> b_1, a => a_2 <=> b_2; under Der 3 a') all but a' are equivalent;
  under Der 3 b'_1 (or b''_coh or b''_hom) all are equivalent. **Def. 3: D-fibration** (under Der 3 a')).
  Prop. 6: for f proper (resp. smooth): D-fibration <=> weak cohomological (homological) fibration <=>
  X/y' -> X/y D-equivalences <=> f_* f^* F locally constant for constant F <=> same for locally constant F.
  ms. 118: "il est douteux qu'elle [la notion de D-fibration] soit stable par composition" (footnote 60: yes if
  D-equivalences are Hot-equivalences); "j'ai omis de faire un contre-exemple, avec des derivateurs
  Der(k-Mod) disons"; and it is not clear that f_* f^* F, f_! f^* F are computed fibrewise.
- **Prop. 7 (ms. 119)**: universal D-equivalence <=> D-fibration with D-aspherical fibres (Def. 4: triviale).
  Warning: a D-fibration that is a D-equivalence need not be trivial (ms. 87 ff.); even under the strongest
  Der 3 b_2, base change of a D-equivalence along a D-fibration need not be a D-equivalence.
  **Prop. 8 (ms. 120)**: f is a D-fibration <=> base change of 1-complete D-equivalences gives D-equivalences.
  Corollaire: if every D-equivalence is 1-complete ("je ne connais que HOT... quasiment caracteristique de
  HOT") then D-fibrations are those preserving D-equivalences under base change, and compose.
- **Prop. 9, Def. 5 (ms. 120-121)**: D-fibration cohomologique (base change preserves cohomological
  D-equivalences; f_* F locally constant and fibrewise for locally constant F on X, universally), homologique,
  **D-fibration forte** = both; stable under composition. ms. 122-123: D-fibrations 1-completes / 2-completes
  (X'' -> X' 1- or 2-complete for Y'', Y' Hot-aspherical): "a le grand tort de ne pas etre stable par
  composition (que je sache!)"; the variant "1-complete => 1-complete" is stable under composition but
  "inutilisable ... n'etant pas en mesure de decrire les D-equivalences 1-completes".
- **ms. 124-126: Der 3 c_1)** every D-equivalence is cohomological; c_2) homological; **c')** 1-complete;
  **c'')** 2-complete; c'' => c' => c_1, c_2. "Je ne connais que HOT pour satisfaire c_1, c_2", and HOT should
  satisfy c''. Prop. 10: under c_1, D-fibration = cohomological D-fibration, stable under composition. Cor. 2:
  under c_1, c_2 one notion. The chapter ends announcing a direct treatment of Hot-fibrations (= XI section 1).

*Remarks for the GALOIS review (mine).* The object the prompt calls `W_D^lc` is Grothendieck's class of
2-complete D-equivalences (ms. 99-100, 113), `W_D^1` the 1-complete ones; his axioms Der 3 b'_1, b'_2 say
`W-infinity` is contained in them; Der 3 c', c'' say `W_D` equals them. His explicit open points: is HOT
2-complete on Hot-equivalences (Lemme ms. 109); the same for D_i (footnote 57); a description of 1-complete
D-equivalences (ms. 105, 123); examples for footnote 34, ms. 116, ms. 118 (failure of base change /
composition); whether f_* f^* F is fibrewise for D-fibrations (ms. 82, 118). His remark at ms. 97-98 already
contains Lead 2 for n-types: locally constant objects for D_i see the (i+1)-type.

## Chapter X ms. 1-5 [DER_VIII-X.tex, lines 1121-1217]: D-asphericity and the localizer W_D

- Recalls (i) D-aspherical object, (ii) D-equivalence, (iii) D-aspherical / D-coaspherical functor, (iv) D-smooth,
  D-proper, (v) D-fibration (test on Hot-aspherical Y'', Y'; trivial iff fibres aspherical iff universal
  D-equivalence), (vi) left / right (weak cohomological / homological) D-fibrations. "Toute cette kyrielle de
  notions se deduit de la seule notion de D-equivalence": **W_D** = the class of D-equivalences (domain: all of
  Cat). Checks the Pursuing Stacks axioms: L 1 saturation (W_D is the class inverted by X -> constant
  coefficients on X); L 2 (Delta^1 aspherical over e); L 3; L 4 (X/y -> Y/y in W for all y => f in W; "C'est
  OK"); L 5 (cartesian morphisms of fibred categories, fibrewise in W; = I Prop. 6 ms. 71). **L a)**: f in W =>
  pi_0(f) bijective: "pas satisfait pour tous les W_D" (zero derivator), "mais pour les derivateurs utiles en
  pratique, cela semble toujours satisfait". L b), c): Cat -> Cat W^{-1} commutes with finite sums and
  products (not checked by him for W_D). L d): f in W => f^o in W (I Cor. 2 ms. 75).
