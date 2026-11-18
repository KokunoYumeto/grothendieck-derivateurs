# Independent audit of Part E

Auditor: `/root/tower`; source inspected: `sections/E.tex`, all five claims and proofs, against the exact wording of Lead 4(a)–(d) and Part E in the attached prompt. This is a mathematical audit, not an inference from a previous return's status labels.

## Outcome

E.1–E.5 are valid with the explicit mapping-cylinder construction now inserted at the end of E.5. The literal second functor of Lead 4(a) is correctly refuted; the homotopy-type conclusion is correctly retained by a different argument. The quantifiers over arbitrary simplicial sets, arbitrary acts, and arbitrary target functors in totality have all been retained.

## E.1: acts and skeletal simplicial sets

The right-action convention is consistent throughout: `gf = g ∘ f`, and `(h·g)·f = h·(gf)`. For `α:[k]→[l]`, the formula `h ↦ h·(i_l α r_k)` is type-correct, has image fixed by `e_k=i_k r_k`, and composes because `r_l i_l=id`. The maps `i_k,r_k` identify the fixed-point reconstruction with restriction of a presheaf. This proves the equivalence of presheaf categories without the false assertion that the one-object monoid category itself is equivalent to `Δ_{≤n}`.

Skeletal extension is fully faithful on truncated simplicial sets. The Eilenberg–Zilber decomposition uses only existing truncated identities in dimensions at most `n`, and introduces precisely higher degeneracies. Thus uniqueness is up to isomorphism, as claimed. Finiteness in either direction and the empty act are handled correctly.

## E.2: arbitrary degeneracies and infinitely many simplices

The retract argument for `j:M_n/K_n→U_n/K` works. For `c` a retract of `d` with `ri=id_c`, the morphism `fr` gives the component of a natural transformation from the constant comma object `(d,i)` to the identity. Its component at the chosen object need not be the identity; that is not required for contraction. Naturality follows from `h(fr)=(hf)r`.

The bar model of `T_n(K)` in simplicial degree `p` is exactly the coproduct over chains `[k_0]→…→[k_p]` of `K_{k_p}×|Δ[k_0]|`. It therefore preserves arbitrary coproducts and pushouts degreewise. A monomorphism of simplicial sets is an inclusion of the corresponding summands; bar degeneracies repeat identities and likewise include summands. These observations justify relative Reedy cofibrancy and the use of cofibrations after realization. In a skeletal attachment only the map `∂Δ[m]→Δ[m]` must be monic: the attaching map to the previous skeleton may identify faces or make them degenerate. Induction over `m≤n`, with arbitrary coproducts in each dimension, covers infinite simplicial sets. The terminal object for `Δ[m]` exists because `m≤n`. No nondegenerate-face hypothesis enters this proof.

## E.3: the precise failure of the proposed functor

For `K=Δ[2]/∂Δ[2]`, the nondegenerate objects are one vertex and one 2-simplex. If the proposed target is repaired to retain only arrows given by injections between these objects, there are three vertex-to-2-simplex arrows. Its nerve is a graph with `H_1=Z²` and `H_2=0`, whereas the realization of `K` is `S²`. The asserted factorization of an injective face `[1]→[2]` through `[1]↠[0]` is impossible. For dimension one all faces of nondegenerate edges are vertices, so the free-degeneracy-completion argument does apply. The finite counterexample consequently refutes the actual universal functor statement in every `n≥2` without refuting the valid geometric comparison E.2.

## E.4: projectivity and totality

The normalized complex of `Z[K]` is free and bounded in degrees `[0,n]`. All boundary subgroups are free, including infinite-rank ones. Acyclicity splits the complex as `S⁰(Z) ⊕ ⊕_{k=1}^n D^k(B_{k-1})`. In the abelian category of complexes concentrated in `[0,n]`, maps out of `S⁰(Z)` are evaluation in degree zero; maps out of `D^k(P)` are `Hom(P,C_k)`. Thus the displayed summands are projective. This would need qualification in an unbounded category with negative degrees, but the bounded category used here is precisely the correct one.

The truncated Dold–Kan equivalence follows from the explicit inverse formula, so projectivity transfers to the truncated presheaf and then to the `Z M_n`-module through the same splitting-of-idempotents equivalence as in E.1. The two-sided bar basis agrees with the restricted-action nerve: the final `H` element, the initial `L` element, and the chain of base arrows determine its simplex. Hence the Tor calculation is exactly the one needed, with correct variance.

For a functor `p:M_n→U'`, the under-comma over `(u',c)` of `M_n/H→U'/p_!H` is the connected component indexed by `c` of the action with `L(m)=U'(u',p(m))`. The bar calculation therefore makes each such comma acyclic, and homological Theorem A applies. The argument from projectivity and connectedness back to totality does not assume acyclicity circularly: applying the same Tor calculation to `L=1` proves source acyclicity.

For weak-homotopy totality, a final functor surjects on fundamental groups by the finite zigzag lifting argument. The source is simply connected by E.2, the targets are acyclic by the preceding result, and the homological Whitehead conclusion is valid for their CW-type nerves. This proves totality for every target functor, rather than substituting arbitrary actions on `M_n/H` for restricted actions.

## E.5: group realization and preservation of dimension

The 2-dimensional cellular argument is correct: collapse a maximal tree, then acyclicity is equivalent to the exponent-sum map `Z^(R)→Z^(X)` being an isomorphism. In finite rank this is equivalent to a balanced presentation and trivial abelianization. The infinite case correctly retains the isomorphism condition; equal cardinalities alone would not suffice.

The Hopf exact sequence gives the necessary superperfectness. Conversely, for a presentation complex of a superperfect group, its free group `H_2` is generated by spherical classes. Attaching 3-cells along a basis gives an injective third cellular differential whose image is the kernel of the second. This produces an acyclic complex of dimension at most three with unchanged fundamental group, and preserves finiteness for finite presentations.

The formerly brief passage from these CW complexes to simplicial sets was made explicit during this audit. For a simplicial map `f:L→T` of abstract simplicial complexes, form the poset `P(f)=P(T) ⨿ P(L)` with additional relations `τ≤σ` exactly when `τ⊆f(σ)`. The retraction to `P(T)` is right adjoint to its inclusion, and restricts on `P(L)` to the face-poset map of `f`. A mixed chain has target maximum dimension `r` and domain minimum dimension `q` with `r≤q`; counting both portions proves `dim N P(f)≤max(dim T,dim L+1)`. Coning off the embedded `N P(L)` therefore gives a simplicial model of the homotopy cofiber with this dimension bound. Separate tags permit arbitrary families of attachments without new mixed chains. This avoids any unjustified assumption that arbitrary attaching maps preserve a chosen global vertex order. Finite simplicial approximation of attaching circles and spheres then gives the required finite or small models in dimensions two and three. The current E.5 includes this construction.

## Remaining limitations

None found in the claims of Part E after the mapping-cylinder paragraph was inserted. This audit does not certify source attributions outside the passages actually opened by their respective authors; the separate F ledger records those access statuses.
