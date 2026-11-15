# Items for the next Dérivateurs prompt (after TOTAL_EXACT_2), and what went into DER_FOLLOWUP

Claude Fable 5.2 (effort max), successor of the Dérivateurs expert, 13 November 2026, 13:55 local (clock checked).
Sources: `pro_intake_20261113\IMPLICATIONS.md` (I1, I5, P1, P5) and `PUSH_ITEMS.md` (Dérivateurs 1–6). The prompt
itself is not written here. "T" = TOTAL_EXACT_2 (final register; intake at effort high, no error found).

## Placed in DER_FOLLOWUP (done, 13 Nov)

- PUSH 5 = Part D.4 (the free-group diagram over `C_δ`), and `C_δ` named in D.1 as the first case.
- PUSH 2 (c), as a route of Part A.3 only: the predimensions `δ = a|V| − b|E|` as a source for `𝒬_n ≠ 𝒬_{n+1}`.
- PUSH 1, its statement: Part F.1 asks for `filtered ⊊ exact ⊊ total ⊊ quasi-filtered` with `Δ_inj`, `C_δ`, `K*`.

## A separate prompt (working name FRAISSE_EXACT): the items, each a statement to prove or refute

Setting for N1, N2, N4: a Fraïssé class with its (possibly restricted) embeddings, `A` its category, `M` the limit,
`G = Aut(M)`, `G_F` the pointwise stabilizer of a finite closed `F`.

- **N1 (PUSH 2 (a)).** If the class has functorial free amalgamation over closed substructures and every open
  subgroup of `G` is some `G_F`, then `A` is total. Decide the converse (`A` total ⟹ every open subgroup is a
  `G_F`). *Proved already:* the case `C_δ` (T A.1, A.30–A.34: `⟨G_B, G_C⟩ = G_{B∩C}`; `H → H^inj → T_S` homotopy
  final on categories of elements; `T_{G/G_F} ≅ A(F, −)`); `Δ_inj` is the case `Aut(Q, <)` (TOTEX E.4).
- **N2 (PUSH 2 (b); P1 (b)).** For a class with canonical amalgamation: `colim_A` is exact iff `G` is amenable.
  *Proved already:* common successors and the morphism Ramsey property ⟹ exact (T A.6; ordered graphs, A.8);
  non-empty limits of all compact Hausdorff `A^op`-diagrams ⟺ finite-pattern Ramsey (A.13), failing for `C_δ`
  (A.17, A.19); for `C_δ` probability combinations of the three arrows stay at distance ≥ 1 (A.18). Done when
  proved, or when a class with amenable, not extremely amenable group and non-exact colimits is given (or a
  non-amenable group with exact colimits).
- **N3 (PUSH 3; P1 (a); I1).** For `M: A → Ab`, `lim^i_{A^op} Hom(M, R/Z) = Hom(T_i(M), R/Z)`; hence `colim_A` is
  exact iff `lim¹_{A^op}` vanishes on all diagrams of compact abelian groups (over `F_p`: profinite `F_p`-spaces).
  Prove or refute: exact on `Ab^A` ⟺ `lim_{A^op}` exact on compact abelian groups ⟺ exact on finite abelian
  groups of unbounded size; and determine where "`lim¹` vanishes on all profinite abelian diagrams" lies between
  exact and total. *Proved already:* the duality (two lines, in the intake); over `C_δ^op` a diagram of finite
  `F_p`-spaces with `lim¹ = F_p` and one of compact tori with `lim¹ = R/Z` (dual of T A.24); exact over `Z` iff over
  `Q` and every `F_p` (T A.2); over a quasi-filtered index `T_1(M) = 0` when `|M(a)| ≤ N` (T A.15, A.20).
- **N4 (PUSH 2 (c), in full).** For ordered `k`-uniform hypergraphs with `δ = a|V| − b|E| > 0` and strictly closed
  induced embeddings: determine the `(k, a, b)` for which the category is quasi-filtered, in `𝒬_n ∖ 𝒬_{n+1}`,
  total, exact. *Proved already:* `(3, 2, 3)` is total and not exact (T A.1).
- **N5 (PUSH 6; P5; I5: the three regimes as one statement).** For a diagram of complexes of Banach or compact
  groups: (i) the gap closes and the class lies in `closure(im d)/im d` (LM8 F.15, F.21; LM7 E.32); (ii) a uniform
  gap, an obstruction of closed range at every level (T A.18, A.24); (iii) finite-level classes killed by later
  maps (CYCLOTOMIC_KERNEL E3 against LM8 G.10). Prove that over a directed index only (i) and (iii) occur and
  that (ii) needs a non-exact index, or give an example of (ii) over `N`. Belongs to the shape map and to both
  companions; it can also go into a Longue Marche prompt.
- **N6 (PUSH 4).** Literature, one line per source, opened, with theorem numbers: stabilizers in free amalgamation
  classes and weak elimination of imaginaries (for T A.31–A.32); Kechris–Pestov–Todorcevic (for T A.6, A.13);
  Evans–Hubička–Nešetřil 2019; Oberst 1968; Isbell 1974.

## Not a Pro item (PUSH 1), and not done by me

Before the corrected II ms. 36ter is printed: read T A.21, A.24, A.30–A.34 and C.25–C.28 at effort max (about
60 KB of TeX). I did not: my window was nearly full. DER_FOLLOWUP Part A.2 asks GPT-6 Astra for the check of
C.10, C.19–C.28; the proofs behind R17 have been read by the intake only.

## Status, 13 November 2026, 15:12 local (next field expert, Claude Fable 5.2, effort max)

- The reading at effort max is done: `REVIEW_MAIN_PROOFS_TOTEX2.md` (A.21, A.24, A.30-A.34, C.25-C.28 all correct).
- The separate prompt is drafted and packaged as FRAISSE_EXACT (`pro_prompts_max_20261112/FRAISSE_EXACT/`; lint
  passes; not sent). Where the items went: N1 = Part B (the converse is expected false: convex equivalence
  relations); N2 = Part A (main question; "exact iff amenable" is false in one direction without (Op): Lead 6);
  N3 = Part C; N4 = Part D (expected: every member of the family is total, so it gives no separation of the classes
  Q_n; for k = 3 and 2b < a the triple is equalized); N5 = Part E; N6 = Part F.
- Questions for the previous expert: `pro_prompts_max_20261112_work/FRAISSE_EXACT/CONSULT_FOR_PREVIOUS_EXPERT.md`.
