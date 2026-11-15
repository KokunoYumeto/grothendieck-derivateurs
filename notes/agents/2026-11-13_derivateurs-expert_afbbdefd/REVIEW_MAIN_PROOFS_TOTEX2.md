# Referee reading of the main proofs of TOTAL_EXACT_2

Reader: Claude Fable 5.2 (Anthropic), effort max, field expert of the Dérivateurs line, 13 November 2026, 14:55 local
(clock checked). Return read: TOTAL_EXACT_2 by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checkpoint 03 = the
deliverable (89 statements; register `TOTEX2_results.csv`, source `sections/*.tex`). Numbers are those of the final
register. This is the reading at effort max asked for after the intake at effort high (`INTAKE_TOTEX2.md`).

## Result

| Statement | What it says | Verdict |
|---|---|---|
| A.21 | closure calculus for `≤_d`; free amalgams; `C_δ` has I and common successors | correct |
| A.24 | the three point arrows `V → W` have no affine equalizer over any non-zero ring; `T_1(Q) ≅ R` | correct |
| A.30 | the finite alternating bridge | correct |
| A.31 | `⟨G_B, G_C⟩ = G_{B∩C}` | correct |
| A.32 | every open subgroup of `G` is a `G_F` | correct |
| A.33 | (every open subgroup is a `G_F`) ⟹ every component of every `El(H)` is weakly contractible | correct |
| A.34 | `C_δ` and its point-and-edge-closed full subcategory are total and not exact over any non-zero ring | correct |
| C.25 | component intersections of size ≥ 2 come from actual spans with an older source | correct |
| C.26 | component transition relations are acyclic and `L_H ≤ L_U + 1` | correct |
| C.27 | every arrow of every repaired AKR construction is injective on `π_0 G_X` | correct; the compressed step is written out in §4 below and goes through |
| C.28 | every attachment preserves `colim K`; `κ_+ − κ_−` survives; the repaired `K*` is not total | correct |

No gap and no error found in these eleven statements. Read as inputs, each proof followed step by step: C.5, C.10,
C.19, C.20, C.21, C.22, C.24, C.32 (all correct as used). So `filtered ⊊ exact ⊊ total ⊊ quasi-filtered` (D.1) stands on
proofs I have followed line by line, with the following inputs taken from earlier checked work: TOTASPH C.5, C.6
(total = all action components weakly contractible; exact ⟹ total), `Δ_inj` (TOTASPH C.9, C.10), and TOTEX
Proposition C.1 (properties (9), (10), (11) of the repaired quasi-filters; I re-derived (9) and checked the visibility
table for paths with two vertices, the general table is the one checked by program in TOTEX).

Points that the companion must word with care are in §6. What I did not check is in §7.

## 1. A.21 and A.24 (the category and the triple)

`δ(U) = 2|U| − 3|E(U)|`; `A ≤_d B` means `δ(U) > δ(A)` for all `A ⊊ U ⊆ B`.

- Submodularity: the vertex term is modular and the edge count is supermodular. Checked.
- Restriction (`A ≤_d B`, `X ⊆ B` ⟹ `A∩X ≤_d X`): for `A∩X ⊊ U ⊆ X` one has `U∩A = A∩X` and `U ⊄ A`, so
  `δ(U) − δ(A∩X) ≥ δ(U∪A) − δ(A) > 0`. Also valid for `A∩X = ∅`.
- Transitivity and intersections: as written. Composition of arrows follows.
- Free amalgam `D = B ∪_A C`: an edge lying in both `B` and `C` lies in `A` (the factors are induced), so
  `δ_D(U) = δ_B(U∩B) + δ_C(U∩C) − δ_A(U∩A)`. Positivity and `B, C ≤_d D` follow from restriction. The orders merge gap
  by gap. Over the empty base this gives common successors, hence connectedness.
- A.24. `δ(point) = 2`, `δ(two points) = 4`, `δ(W) = 3`, so each `v_i` is an arrow. An arrow `W → X` is determined by its
  image, a hyperedge of `X`. For `r` distinct such hyperedges on `v` vertices, `2v > 3|E_X(U)| ≥ 3r`, so some vertex
  lies on exactly one of them; if it is `g_0 v_i`, the coefficient of the basis element `g_0 v_i ∈ A(V, X)` in
  `D(Σ c_g g)` is `(−c, −c)`, `(c, 0)` or `(0, c)` with `c = c_{g_0} ≠ 0`. So `D_X` is injective for every `X` and every
  `R ≠ 0`. From `0 → P_W → P_V² → Q → 0` and `colim D = 0`: `T_1(Q) ≅ R`. An affine equalizer `t` would have `D(t) = 0`,
  hence `t = 0`, against augmentation 1. Only actual arrows are used, so the argument holds in both categories.
- Remark: the register lists A.23 and A.34 as dependencies of A.24. There is no logical dependence.

## 2. A.30 (the alternating bridge)

Data: `B, C ≤_d D`, `F = B∩C`, arrows `d_0, d_1: D → E` equal on `F`. Factors `E, D_1, …, D_{2N−1}` on a circle of
`s = 2N` indices; overlap `(i, i+1)` is `B` for `i` even and `C` for `i` odd; at the ends through `d_0(B)` and
`d_1(C)` in `E`.

1. Classes of the generated equivalence relation (my own enumeration): points of `F`: one point in every factor;
   `x ∈ B∖C`: `{(2j, x), (2j+1, x)}`; `x ∈ C∖B`: `{(2j+1, x), (2j+2, x)}`; a point `e = d_0(b) = d_1(c)` of `E` with
   `b ∈ B∖C`, `c ∈ C∖B`: `{(2N−1, c), e, (1, b)}`; other points: singletons. The two mixed cases (`b ∈ F`, `c ∉ F` or the
   reverse) are excluded by injectivity of `d_0`, `d_1` and `d_0|_F = d_1|_F`. So every factor map is injective, every
   class meets consecutive indices only through the prescribed overlap, and non-`F` classes are arcs of at most three
   indices. Needs `N ≥ 2`; the proof takes `N ≥ 4`.
2. Inducedness: an edge of factor `j` with its three vertices in factor `i` is visible along the short arc from `j`
   to `i` (arcs of at most 3 indices on a circle of at least 8), and at each step the three vertices lie in the
   overlap base, which is induced in both neighbours (`B, C` induced in `D`; `d_0, d_1` induced embeddings). I
   checked the case that passes through `E` (from `D_1` to `D_{2N−1}`) separately.
3. Linear amalgam `L` (one overlap cut): an iterated free amalgam along bases that are `d`-closed in both sides
   (`d_0(B) ≤_d d_0(D) ≤_d E` by transitivity), so `L` is positive and every factor is `≤_d L` by A.21. Restoring the
   cut identifies at most `m = max(|B|, |C|)` pairs (the `F`-points are already single in `L`), every edge of `Z[U]`
   lifts, hence `δ_Z(U) ≥ δ_L(Ũ) − 2m`.
4. Case "some index `r` is missed by the proper visibility arcs of `U`": cut at `(r−1, r)`; lifts are unique for
   vertices and (simple hypergraph) for edges; `Z[U] ≅ L[Ũ]`; positivity, and `δ_Z(U) > δ(factor)` when `U` properly
   contains a factor.
5. Case "the arcs cover all indices": every index `k` carries a lifted non-`F` vertex, which first appears at some
   `j ∈ [k−2, k]`, so `3|J| ≥ s`; each step `j ∈ J` adds `δ(U_j) − δ(U_j ∩ A_j) ≥ 1` (restriction of `A_j ≤_d T_j` to
   `U_j ⊄ A_j`; integrality); the other steps add `≥ 0`. With `s > 3(δ(E) + 2m)`: `δ_Z(U) > δ(E) ≥ δ(D) > 0`.
6. Order: `p_t = (1−t)d_0 + t d_1` in coordinates of `E ⊂ R`; `b_{2j} = p_{j/N}`; `b_{2j+1}` = `p_{j/N}` on `B`,
   `p_{(j+1)/N}` elsewhere. `b_{2j+1}` is strictly increasing when `2M_0/N < Δ`; it agrees with `b_{2j}` on `B` and with
   `b_{2j+2}` on `(D∖B) ∪ F ⊇ C`. The overlap equations hold, so the coordinates define a function on `Z`, injective on
   each factor; any linear order refining it makes every factor map increasing.

All bounds on `N` are lower bounds. The conclusion (arrows `a_0 = (E→Z)d_0, a_1, …, a_{2N} = (E→Z)d_1`, with
`a_{2j}|_B = a_{2j+1}|_B` and `a_{2j+1}|_C = a_{2j+2}|_C`) is as stated. Correct.

## 3. A.31–A.34 (stabilizers and totality)

- The limit `M`. Evans–Hubička–Nešetřil 2019, Theorem 2.6 (opened: arXiv:1801.01165v4, LaTeX source, the theorem with
  label `FHT`; all numbered environments share one counter, and it is the sixth item of §2). Hypotheses: `(𝒦; ≤)` a strong class (a class
  of embeddings closed under composition, containing the isomorphisms, with (*): `A ≤ C`, `A ⊆ B ⊆ C`, `B ∈ 𝒦` ⟹
  `A ≤ B`); countably many isomorphism types; joint embedding and amalgamation for strong embeddings. Conclusion: rich
  sequences exist, the limit is unique, and isomorphisms between finite strong substructures of `M` extend to
  automorphisms. For `C_δ`: the language is `{<, E}`, embeddings are the increasing induced embeddings, (*) is the
  restriction property of A.21 with `X = B`, the rest is A.21. The same for the point-and-edge-closed subclass
  (it is hereditary by restriction). So the theorem applies. The extension property over an arbitrary finite closed
  `B ≤ M` (amalgamate with a stage, then use richness) is derived correctly; "closed in `M`" does not depend on the
  chain. The return also gives the construction directly; the proof does not rest on the citation.
- A.31: with `D ⊇ B∪C` and `E ⊇ D ∪ gD` finite closed, `id_D` and `g|_D` are arrows `D → E` (restriction) equal on `F`;
  the bridge `Z` embeds in `M` over `E`; the copies of `D` are closed in `M`; extensions `g_i` with `g_0 = 1`,
  `g_{2N} = g` telescope. Correct.
- A.32: minimal `B` with `G_B ≤ U`; `G_{B ∩ gB} ≤ U` forces `gB = B`; an increasing permutation of a finite chain is
  the identity. Correct. (Finite intersections of closed sets are closed: inside a common stage.)
- A.33, step by step.
  (F) `Fix_M(G_B) = B`: two copies of `D ∋ x` over `B`, freely amalgamated and embedded over the first. Correct.
  Cosieves: for `P → Z` in a non-empty full cosieve `𝒰` of `P/A_M`, `Φ(X) = X ∪_P Z` with the `X`-side before the
  `Z`-side in each gap of `P`; `Φ(u) = u ∪ id_Z` is increasing (a point stays in its gap), induced, and `d`-closed
  because `Y ∪_P Z = Y ∪_X (X ∪_P Z)` is a free amalgam of two closed embeddings of `X`; `id ⇒ Φ ⇐ const_Z`, and `Φ`
  lands in `𝒰`. Correct (the choice of labels is handled through an equivalent tagged model, which is harmless).
  `H → H^inj`: the relation "equal after some arrow" is an equivalence relation and is preserved by I; `(a,[h]) ↓ El(q)`
  receives `J: a/A_M → 𝒟`, whose comma categories are the cosieves `{g: H(g)k = H(gf)h}`, non-empty by the definition
  of the relation. Two applications of Theorem A. Correct.
  `H^inj → T_S`: `S = colim` over finite closed subsets with inclusions, `g · i_B(h) = i_{gB}(H(g|_B)h)` is well
  defined and continuous; `T_S(B) = S^{G_B}` with `T_S(f) = ` action of any extension of `f` is a functor; the comma
  categories are the cosieves `{f: T_S(f)s ∈ i_b H(b)}`, non-empty. Correct.
  Orbits: `(G/G_F)^{G_B} = {gG_F : gF ⊆ B}` by (F), and `gG_F ↦ g|_F` is a natural bijection onto `A_M(F, B)`; for
  `F = ∅` the constant functor with `El = A_M`, contractible by the same construction over the empty base. Correct.
- Theorem A in the form used. Goerss–Jardine, *Simplicial Homotopy Theory*, Theorem IV.5.6 (opened in the
  university-hosted copy named in the return's bibliography; statement read): for `F: C → D` such that every
  `α: y → y'` induces a weak equivalence `B(y'↓F) → B(y↓F)`, the square `B(y↓F) → BC`, `B(y↓D) → BD` is homotopy
  cartesian; `y↓F` has objects `(τ: y → F(x), x)`. This is the variance used (`d↓u`). With all `d↓u` weakly
  contractible the hypothesis holds, `B(d↓D)` is contractible, so every homotopy fibre of `Bu` is contractible. No
  further hypothesis. (It is also Quillen 1973, Theorem A, in its `Y\f` form.)
- A.34 assembles A.21, A.24, A.30–A.33; the subclass is closed under the amalgam and the bridge (every atom lies in a
  factor, closed there, and the factor is closed in the whole). Correct.

## 4. C.25–C.28 (the repaired AKR category is not total), with the step of C.27 written out

Source read for the inputs: Adámek–Koubek–Reiterman 1981, pp. 375–387 of the scan: Lemma B.3 (property (4)), B.4,
Construction B.5 with formulas (5)–(7) and its Lemma, Construction B.6 with (9), (10), (11), Note and Lemma B.7,
Lemma B.8, B.9, Construction C.1 with (*), Theorem C.2 with (c_m), (d_m) and the proof of (c_{m+1}) (step V.1).
What the return uses, and where:
- the shape of a stage (B.7, B.8, B.9): `K_{m+1}` adds new maximal objects with identity endomorphisms only; every
  arrow into a quasi-filter target is `α_i p` with `p` old, every arrow into a sum is `v_t p`; no arrows between
  distinct new objects. As in the source.
- (4) for every parallel pair (the relation `f(x) ↦ g(x)` has no cycle and bounded paths): preserved by B.7 and B.8,
  given (9). Used in C.26.
- (10) with the range `s − 2n ≥ 2k` (from `k ≥ n`), and (11): used in C.10, C.19, C.20.
- (c_m): its proof in the source uses only (10), (11), the factorization of arrows into a new target and (c_m) at the
  earlier stage, not (d_m). It is also C.19 for `P = W`.
- (*) of C.1: `s/3n` is an integer `≥ (1 − a_{m+1}/a_m)^{-1} > 4` (because `3/2 < a_{m+1} < a_m ≤ 2`), so `s ≥ 15n`.
(9), (10), (11) are false for the printed maps of B.6 (TOTEX C.1: the restriction of `β^3` to two points); the return
works throughout with the repaired maps (each path with its own length, one common `k`), for which TOTEX C.1 proves
them. So "`K*`" means the repaired construction.

C.5 (pushout formula for one new maximal object; `H_2(B El H) = ker(colim K → Z)`): re-derived from the two short
exact sequences. C.10 (the exact kernel): vertices of `G_X` are the points of `X`; two distinct `W`-arrows share at most
one point (by (c_m)); the visibility sets of vertices and edges are arcs or the whole circle; neighbouring lifts are
linked by exactly one source cell ((11), then (c_m)); circular fibres are exactly the equalized cells (I redid the
cancellation `d_{2k+j} = d_{2k−j}`, then `g d_0 = f d_0`, then all `d_i = d_0`); the sequence (CF) is exact cell by cell;
the two long exact sequences give `ker a = im H_1(D_•)` and the generators `(g_# − f_#)σ`. Correct. C.19, C.20, C.22:
followed (C.19 is the proof of (c_{m+1}) with a forbidden pair in place of two points of `W`; C.20 is Helly for arcs of
length `≤ w` on a circle of `s > 3w` indices; C.22 descends through generating copies and ends at `V` or at equality).

C.25. If `h` does not factor through `g`, the preimage of the component intersection under the injective `H(h)`
contains no forbidden pair of components (hypothesis 3), so it lies in one generating image (hypothesis 2); replacing
`h` by `he` keeps the intersection, which has at least two elements, so the descent cannot reach `V` (one component),
and at `W` the two components are a forbidden pair, which forces the factorization. Correct.

C.26. Induction on the generation rank of the source. If `|I| ≤ 1`: no cycle, paths of at most 3 vertices, and
`L_U ≥ 2`. If `|I| ≥ 2`: `f` does not factor through `g` (endomorphisms are identities), C.25 gives `u, v: R ⇉ S`,
`R` older, `fu = gv`, `H(fu)H(R) = I`. Injectivity of `H(f)`, `H(g)` turns a component path with `r` vertices for
`(f, g)` into one with `r − 1` vertices for `(v, u)`, and a cycle into a cycle of the same length (excluded by
induction). A point path with `p` vertices for `(v, u)` extends to one with `p + 1` vertices for `(f, g)` (the last
vertex is new by (4) and by injectivity of `g`), so `L_U(v, u) ≤ L_U(f, g) − 1`, and
`r − 1 ≤ L_H(v, u) ≤ L_U(v, u) + 1 ≤ L_U(f, g)`. Correct.

C.27. The induction carries (1) every arrow is injective on `H = π_0 G`, (2) Helly for the generating cover on
components, (3) routing of forbidden pairs of components by actual arrows. Stage 0 is immediate. From stage `m` to
`m+1`, for a new quasi-filter target `Z` of `f, g: S ⇉ T` with path bound `n`:
- `G_Z` is the strict colimit of the necklace diagram of graphs (vertices: C.32; edges: the fibre computation of
  C.10), `π_0` is a left adjoint, so `H(Z)` is the coequalizer (NC) of `H(f), H(g)`. These are injections with acyclic
  relation and paths of at most `n + 1 ≤ k` vertices (C.26 at stage `m`; `k ≥ (15n − 1)/4 ≥ n + 1`). By C.32 (with
  bound `n + 1`) the coequalizer is the repaired β-target for `(H(f), H(g))`, so every `H(α_i)` is injective, and
  (9)–(11) hold for the component necklace with bound `n + 1` (TOTEX C.1 is a statement about injections of finite
  sets). The shortest arcs are in range: `2k ≤ s − 2(n + 1)`. Proper visibility arcs of components have at most `2n`
  indices and `s ≥ 15n > 6n`, so C.20 gives (2) for `Z`. (1) for the new arrows `α_i p` follows.
- **The compressed step ((3) for the new target), written out.** Let `P ≠ V`, `c, c' ∈ H(P)` a forbidden pair of
  components, `h: P → X`, `g: Y → X` in `K_{m+1}` with `H(h)c, H(h)c' ∈ H(g)H(Y)`.
  (i) `X` old: `h, g` are old (the old stage is full, new objects are maximal); this is (3) at stage `m`.
  (ii) `X` new and `P = X`: `h = id`. If `g ≠ id` then `g` factors through a generating copy `e`, and `c, c'` both lie
  in `H(e)H(E)`, against the choice of the pair. So `g = id` and `h = g ∘ id`.
  (iii) `X = Z` a new quasi-filter target (for `φ_0, φ_1: R ⇉ T`), `P` old. Write `h = α_j h*` with `h*: P → T` old.
  If `g = id_Z` take `l = h`. Otherwise `g = α_i g*`, `g*: Y → T` old. Put `d = H(h)c`, `d' = H(h)c'`; both lie in
  `H(α_j)H(T) ∩ H(α_i)H(T)`. If `j ≠ i`, let `j'` be the next index on the shortest arc from `j` to `i`. By (10) for the
  component necklace, `d, d' ∈ H(α_j)H(T) ∩ H(α_{j'})H(T)`; by (11) for it, this overlap is the image of
  `H(α_j φ_r) = H(α_{j'} φ_t)`, where `α_j φ_r = α_{j'} φ_t` is the actual neighbour identity. `H(α_j)` is injective, so
  `H(h*)c, H(h*)c' ∈ H(φ_r)H(R)`. Now (3) at stage `m`, applied to the same pair `c, c'` of `P`, to `h*: P → T` and to
  the comparison arrow `φ_r: R → T`, gives an actual arrow `l_1: P → R` with `h* = φ_r l_1`. Hence
  `h = α_j φ_r l_1 = α_{j'} (φ_t l_1)`: the same arrow `h` now factors through the copy `j'`, and `d, d'` are unchanged.
  The rest of the arc from `j'` to `i` is again a shortest arc; after at most `2k` steps `h = α_i h̃` with `h̃: P → T`
  actual. Injectivity of `H(α_i)` gives `H(h̃)c, H(h̃)c' ∈ H(g*)H(Y)`, and (3) at stage `m` gives `l: P → Y` with
  `h̃ = g* l`, so `h = g l`.
  (iv) `X` a new sum `B_1 ⊔ B_2`, `P` old: `H(X) = H(B_1) ⊔ H(B_2)`; `h = v_a h*`, `g = v_b g*` or `g = id`; a common
  component forces `a = b`, and (3) at stage `m` applies to `h*, g*`.
  At no point is an equality of component maps used in place of an equality of arrows: the components only locate the
  overlap, and each factorization is of the arrow `h*` (or `h̃`) itself, supplied by the hypothesis at stage `m`.
  The step is correct.
- Sums: immediate. New objects are independent. So (1)–(3) hold at stage `m + 1`.

C.28. For a defining pair, the fixed vertex set is empty or `e(R)` (C.22) and the fixed subgraph is `e_# G_R`
(an edge with two fixed end points factors through `e` by (c_m)); `H(e)` injective gives (FC), so the kernel of C.10
is zero; sums have zero kernel; for several new objects the kernel is the sum of the kernels (I checked this from the
pushout formula of C.5). Stage 1: I computed the graphs: for `(v_1, v_2)` and `(v_2, v_1)` one circle through all
`s` path points, with cycle `Σ_{t ≤ 2k} α_t − Σ_{t > 2k} α_t` of augmentation 1; forests for all other targets. So
`colim_{K_1} K = Z²`, `H_2 = Z(κ_+ − κ_−)`, and the class survives all stages and the union. Correct.

The paragraph "Target choices and unused underlying points" (targets enlarged by points outside all copies) is an
extension beyond the covered construction. I followed its first half (arrows preserve and reflect "being the value of
a `V`-arrow", by (9)) and read the second half in outline only.

## 5. Sources opened for this reading

| Source | What was opened | Finding |
|---|---|---|
| Evans–Hubička–Nešetřil, Proc. LMS 119 (2019), arXiv:1801.01165v4 (LaTeX) | the subsection "Fraïssé classes" of §2 in full (Definitions 2.1–2.5, Theorem 2.6); the subsection "EPPA and amenability" of §2 (the Kechris–Rosendal theorem); Theorem 3.8 with its proof, Corollaries 3.9 and 3.11; the subsection "Amenable subgroups" of the last section (free amalgamation classes with all embeddings have amenable automorphism groups) | hypotheses of 2.6 hold for `C_δ` and the subclass; see §6 (c) for 3.8 |
| Goerss–Jardine, Simplicial Homotopy Theory | statement of Theorem IV.5.6 (copy not kept) | variance `y↓F`, as used |
| Adámek–Koubek–Reiterman, Czech. Math. J. 31 (1981) | pp. 375–387 of the scan | as described in §4 |
| TOTEX (the earlier return), Proposition C.1 | statement and proof | (9) re-derived; table checked for two-vertex paths |
| Moore, Amenability and Ramsey theory, arXiv:1106.3127 (LaTeX) | the convex Ramsey property and the last theorem | used in §6 (c) only |

## 6. Remarks for the companion (none is an error of the return)

(a) The corrected form of II ms. 36ter can be printed with the three witnesses. Word the third one as "the
Adámek–Koubek–Reiterman category with the repaired quasi-filters (TOTEX C.1), for every admissible choice of its
parameters": for the maps as printed in the 1981 paper, (11) fails and nothing is claimed.

(b) "Three independent audits" (C.28) and "independently audited" (A.30–A.34) are audits inside the run of the return.
This reading is the first outside it at full depth; the intake at effort high found the same.

(c) `Aut(M)` for `C_δ` is not amenable, in two ways. First, the graph on `M` joining two points of a common hyperedge
is 2-sparse (for finite `B`, take the hyperedges inside `B` and one further hyperedge for each remaining adjacent
pair of `B`, `t` of them; positivity of `B` with the third vertices gives `t < 2|B| − 3|E(B)|`, so there are fewer than
`2|B|` adjacent pairs in `B`), a copy `W ≤_d M` has closed points, and the `G_a`-orbit of `b` is infinite for an edge
`{a, b, c} = W` (free amalgams of copies of `W` over `a`); Evans–Hubička–Nešetřil, Theorem 3.8, then gives
non-amenability (statement and proof read; it needs only a continuous action on a `k`-sparse graph and the two
infinite orbits). Second, A.18 (uniform `ℓ¹` gap for probability combinations) contradicts the Reiter form of
Moore's convex Ramsey criterion; this second route needs the passage from Moore's theorem (all embeddings) to strong
classes and a minimax step, which I derived but did not write as a proof. The return does not state non-amenability.

(d) The method of A.21, A.30–A.33 uses only submodularity, integrality and positivity of `δ`. I expect the same
proofs for every `δ = a|V| − b|E|` on `k`-uniform hypergraphs with positive integers `a, b` (loss `a·m` at the cut),
and the private-vertex argument of A.24 for `ak/2 ≤ b < (k−1)a`. Not checked beyond reading the proofs with this in
mind; it is an item of the next prompt.

(e) A.33 is the general statement "functorial amalgamation and (every open subgroup is a `G_F`) ⟹ total". Its converse
is false as it stands: for finite linear orders with a convex equivalence relation (a Ramsey class by
Kechris–Pestov–Todorcevic, hence exact by A.6 and total), the stabilizer of an equivalence class is open and is not a
`G_F`. Derived by me, checked by nobody; also an item of the next prompt.

(f) A remark in Evans–Hubička–Nešetřil 2019 (arXiv v4, the remark after the definition of `k`-sparse graphs: the
graph joining the entries of the tuples of a `k`-sparse `n`-ary relation is `binom(kn, 2)`-sparse) is false as
stated: take a set `B` of `n` points and for each pair `{x, y} ⊆ B` one triple `(x, y, z_{xy})` with its own third
point; every subset contains at most as many triples as points, and the graph induced on `B` is complete. Their
Theorem 3.8 is not affected, and for `C_δ` the graph is sparse by the count in (c). For predimensions with
`b ≤ a(k−2)` the orientation argument has to be run on the hypergraph (hyperedges assigned to vertices). Checked by
hand only.

## 7. Not checked in this reading

- TOTASPH C.5, C.6 and the identification of "total" with Grothendieck's definition at XII ms. 88–89 (checked in the
  review of TOTASPH on 12 November; not reopened).
- TOTEX C.1 beyond what §4 says; the programs of either return (none was run; this reading wrote no program, since
  every step of the eleven statements is a finite argument that I could follow by hand).
- The rest of the register: the 42 rows that the intake read at statement level (B.2–B.10, C.2–C.5 except C.5, C.11–C.18,
  C.29–C.41 except C.32) remain at that level. A.22, A.23 (necklace and quasi-filteredness of `C_δ`) were read but are
  not needed: quasi-filteredness follows from totality.
- The wording of D.2, D.4 against the manuscript pages.
