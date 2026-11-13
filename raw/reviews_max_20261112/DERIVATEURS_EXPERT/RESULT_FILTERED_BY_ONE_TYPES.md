# Filtered categories are the shapes over which colimits of sets and of groupoids are homotopy colimits

Claude Fable 5.2 (Anthropic), effort max, Dérivateurs expert, 12 November 2026 (about 16:35 local). Found while placing
the results of returns 2–4 into the follow-up prompts. Status: proved by me in this note; **not checked by anyone
else**; literature not searched (I do not know the statement from the sources I have read). It uses three results
of the return TOTASPH (GPT-6 Astra, effort Pro, ChatGPT Pro mode) that I checked on 12 Nov
(`..\2_TOTAL_ASPHERICITY\REVIEW.md`, rows C.5, C.11, D.16) and standard facts named below.

**Correction, 12 November 2026 (22:05 local, clock checked), after the return PRETOT (GPT-6 Astra, ChatGPT Pro mode;
items F.1, F.4) and its review by Claude Opus 5.5 (effort max).** The theorem as stated below is false for the
empty category and for a discrete category with two objects. Conditions 1 and 2 are equivalent for **non-empty
connected** `A`; for arbitrary `A`, condition 2 holds iff **every connected component of `A` is filtered**. The
error is in step (2 ⇒ 3): the colimit in `Cat` of the constant diagram `*` is the discrete category `π₀(A)`, not
a point, so condition 2 gives that each component of `A` is aspherical and gives neither connectedness nor
non-emptiness. Conditions 3 and 4 contain connectedness (total asphericity), and the equivalence 1 ⇔ 3 ⇔ 4 stands.
The rest of the proof was checked step by step in PRETOT F.4 and in that review. Also proved there: a sifted
category whose element categories have simply connected components is filtered (F.3), and abelian groups with
the colimit taken in `Ab` already detect filteredness (F.6); so the question left open in the last remark of §3
is settled.

## 1. Statement

Grothendieck (II ms. 36–36ter; XII ms. 88–89) calls a small category `A` totally `W∞`-aspherical when every
category receiving a final functor from `A` is aspherical, and conjectures that this forces `A` to be filtered.
That is false: `Δ_inj` (TOTASPH C.10; the category is Isbell–Mitchell's, 1973). By TOTASPH C.5, `A` is totally
`W∞`-aspherical iff for every `S: A → Set` the map `hocolim_A S → colim_A S` is a weak equivalence: colimits of
*sets* over `A` are homotopy colimits. The theorem says that the conjecture becomes true as soon as the same is
asked one level up.

**Theorem.** For a small category `A` the following are equivalent.
1. `A` is filtered.
2. For every functor `D: A → Cat` the canonical functor `∫_A D → colim^{Cat}_A D` from the Grothendieck
   construction to the colimit in `Cat` is a weak equivalence (is in `W∞`).
3. `A` is totally `W∞`-aspherical, and for every functor `M: A → Grp` the space `hocolim_A BM(a)` is 1-truncated
   (each component has `π_n = 0` for `n ≥ 2`).
4. `A` is totally `W∞`-aspherical, and 3 holds for the diagrams `M_{u,v}` of right-angled Artin groups of
   bipartite graphs defined in §2, one for each parallel pair `u, v` of `A`.

So: **`A` is filtered iff homotopy colimits over `A` preserve 0-truncated and 1-truncated spaces**; totality is
the 0-truncated half. `Δ_inj` has the first property and not the second.

## 2. Proof

(1 ⇒ 2) The nerve commutes with filtered colimits (`[n]` is finitely presentable in `Cat`), filtered colimits of
simplicial sets are homotopy colimits, and `N(∫_A D) ≃ hocolim_A N D` (Thomason), compatibly with the map to the
colimit.

(2 ⇒ 3) For `D = S` set-valued (discrete categories): `∫_A S = El_A(S)` and `colim^{Cat} S` is the discrete
category on `colim_A S` (the discrete-category functor is a left adjoint). So every component of every `El_A(S)`
is weakly contractible, and (`S = *`) `A` is non-empty, connected and aspherical: `A` is totally `W∞`-aspherical
by TOTASPH C.5. For `D = M` a diagram of groups, seen as one-object categories: `A` is connected, so
`colim^{Cat}_A M` has one object, with endomorphism monoid `colim^{Mon}_A M = colim^{Grp}_A M =: G` (the inclusion
`Grp → Mon` is a left adjoint); so `B(∫_A M) ≃ hocolim_A BM(a)` is weakly equivalent to `K(G, 1)`.

(3 ⇒ 4) Clear.

(4 ⇒ 1) `A` is non-empty and connected, and spans in `A` complete to commutative squares (TOTASPH C.11, D.16);
shortening zigzags, any two objects have a common successor. It remains to equalize parallel arrows. Let
`u, v: p → q`. Put `Q = A(q, −)`, `P = A(p, −)`, and `E(x) = {f ∈ Q(x) : fu = fv}`, a subfunctor of `Q`. We must
show `E(x) ≠ ∅` for some `x`.

*The diagram.* For `x ∈ A` let `Γ_x` be the graph with vertex set `V(x) = Q(x) ⊔ P(x)` and with the edges
`{f, fu}` and `{f, fv}` for `f ∈ Q(x)` (an edge joins a `Q`-vertex to a `P`-vertex; the two edges at `f` coincide
exactly when `f ∈ E(x)`). Let `M(x) = M_{u,v}(x)` be its right-angled Artin group: generators `V(x)`, relations
`[f, fu] = [f, fv] = 1`. An arrow `g: x → y` induces `w ↦ gw` on vertices and maps edges to edges, so
`M: A → Grp`. The set of edges is, naturally in `x`,

    Ed(x) = Q(x) ⊔_{E(x)} Q(x)        (two copies of Q(x) glued along E(x)).

*Homology of the stages.* The Salvetti complex of a right-angled Artin group is a `K(π, 1)` with one `k`-torus
for each `k`-clique and zero differentials. `Γ_x` is bipartite, so there are no triangles:
`H_0(M(x)) = Z`, `H_1(M(x)) = Z[V(x)]`, `H_2(M(x)) = Z[Ed(x)]`, `H_k(M(x)) = 0` for `k ≥ 3`, naturally in `x`
(the class of an edge is the image of the fundamental class of the torus of its two generators, oriented
`Q`-vertex first).

*Homology of the homotopy colimit.* Let `X = hocolim_A BM(x)`. In the Bousfield–Kan spectral sequence
`E²_{k,l} = L_k colim_A H_l(BM(x)) ⇒ H_{k+l}(X)` every coefficient functor is of the form `Z[S]`, `S: A → Set`
(`S = *, V, Ed`), and `L_k colim_A Z[S] = H_k(El_A(S); Z)`, which is `0` for `k > 0` and `Z[colim_A S]` for
`k = 0` because `A` is total. Hence `H_2(X) = Z[colim_A Ed]`, and

    colim_A Ed = colim_A Q ⊔_{colim_A E} colim_A Q = * ⊔_{colim_A E} * ,

which has one element if some `E(x)` is non-empty and two elements if all `E(x)` are empty.

*The fundamental group.* `X` is connected. `BA` is simply connected, so by van Kampen for homotopy colimits
`π_1(X) = colim^{Grp}_A M(x)`: generators `colim_A V = {q̄, p̄}`, one relation `[q̄, p̄] = 1` (the image of
`[id_q, u] = 1`). So `π_1(X) = Z²`.

*Conclusion.* By hypothesis `X` is 1-truncated, so `X ≃ K(Z², 1)` and `H_2(X) = Z`. Hence `colim_A Ed` has one
element: `E(x) ≠ ∅` for some `x`. ∎

## 3. Remarks

- For `A = Δ_inj` (all arrows monic, so no parallel pair `u ≠ v` is equalized) the proof shows
  `H_2(hocolim BM_{u,v}) = Z²` with `π_1 = Z²`: the homotopy colimit of these 2-dimensional aspherical complexes
  has `π_2 ≠ 0`. This is of the same nature as the example of the earlier review (`D([n]) = N^{[n]}`,
  `FINDINGS.md` F2-13), which the theorem explains.
- The theorem answers the question left in `FINDINGS.md` F2-13 and Part F of the draft prompt
  PRESHEAF_TOTALITY: the shapes `A` for which `∫D → colim^{Cat} D` is a weak equivalence for all `Cat`-valued
  diagrams are exactly the filtered ones. For Grothendieck's text: II ms. 36ter ("totalement `W∞`-asphérique ⟹
  filtrante") is true when "totalement asphérique" is asked of `Cat`-valued, not only of set-valued, diagrams;
  it bears on VII §10 (ms. 102–103), where colimits of categories are taken along such systems.
- Abelian test diagrams. If `A` is total and `hocolim_A K(M(a), 1)` is 1-truncated for every `M: A → Ab`, the
  same spectral sequence gives in total degree 2: `L_1 colim_A M = 0` for all `M`, so `colim_A` is exact on
  `Ab^A` (so `Aff_Z(A)` is filtered, Isbell–Mitchell 1973, Th. 1); then `colim_A (M ⊗ M') = colim_A M ⊗ colim_A M'`,
  and with `M = Z[S]`, `M' = Z[S']`: `colim_A (S × S') = colim_A S × colim_A S'`, so `A` is sifted. (Proof:
  `H_2(K(G, 1)) = Λ²G` for `G = colim_A M` abelian, the edge map `colim_A Λ²M(a) → Λ²G` is onto, and
  `E^∞_{1,1} = L_1 colim_A M`.) Whether abelian diagrams alone force filteredness is open; it would follow from
  "sifted and totally `W∞`-aspherical ⇒ filtered", which I could not decide.
- Where an error could hide: the naturality of `H_2(M(x)) = Z[Ed(x)]`; the identification of `π_1(X)`; the
  use of TOTASPH C.5 in the form `L_k colim_A Z[S] = 0` for `k > 0`.
