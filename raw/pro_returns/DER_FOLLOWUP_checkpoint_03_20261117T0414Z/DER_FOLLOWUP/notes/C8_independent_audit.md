# Independent audit of C.8

Auditor: `/root/tower`, 17 November 2026. Inspected `sections/C.tex`, Claim C.8 and its full proof, the exact R19/Part C coefficient convention, and the cited passages of the two Cisinski originals. Outcome: **the argument is valid as stated for the fixed coefficient derivator satisfying Der 1–4 on all small categories.** No strongness axiom or implicit quantification over all shifted coefficient theories is needed for its objectwise-to-Grothendieck step.

## Primary-source hypotheses actually checked

- Cisinski, *Locally constant functors* (2009), author PDF `https://www.math.univ-toulouse.fr/~dcisinsk/lcmodcat3.pdf`: §3.1 explicitly permits an arbitrary subcategory `S`; Theorem 3.6 is its localized universal property; Corollary 3.8 gives nerve invariance for every derivator. Lemma 3.9, Proposition 3.10, and Theorem 3.13 prove the cocontinuity/projector argument. Their proof extends from all arrows to the specified `S`, because objectwise homotopy colimits still invert each arrow of `S`.
- Cisinski, *Propriétés universelles et extensions de Kan dérivées* (2008), author PDF `https://www.math.univ-toulouse.fr/~dcisinsk/puhot.pdf`: Definitions 0.1–0.2 use Der 1–4, with both Kan extensions; Proposition 3.12 proves the extra cofinality condition used by Theorem 3.24/Corollary 3.26. These are not strongness hypotheses. Corollary 3.26 is the presheaf universal property in the required variance.

These source checks establish the input. The following detailed checks are a direct audit of the new C.8 proof.

## 1. Arbitrary specified arrows and both projectors

Use the contravariant convention `D(T)=Fun(T^op,C)` in represented cases. Thus to represent objects of `D(T)` by the presheaf universal property one sets the source category in Cisinski's notation to `A=T^op`; the localized simplicial-presheaf category is then presheaves **on `T^op`**, as C.8 says. If the given subcategory `R⊂T` is not wide, add all identities; this changes no inversion condition. It is still small.

Let `P` be the simplicial-presheaf derivator and let `γ:P→P_R` be localization at the specified representable maps. Its right adjoint `i:P_R→P` is fully faithful. A diagram in its image in every shift is precisely an objectwise `R`-inverting diagram. Homotopy colimits of such diagrams are `R`-inverting, since the map corresponding to each `r∈R` is an objectwise equivalence of diagrams. Hence `i` preserves homotopy colimits, and consequently left Kan extensions. Both `γ` and `i` therefore belong to the cocontinuous 2-category used in the internal-Hom argument.

Precomposition reverses the adjunction: the inclusion of `R`-inverting `D`-objects is induced by `γ`, while precomposition by `i` supplies its left adjoint. Apply the same statement to `D^op` and `R^op` to obtain the right adjoint. Applying the universal property on every shift makes these adjunctions compatible with restrictions. There is no hypothesis that `D` itself comes from a model category; the simplicial-presheaf model is the universal source of the construction.

## 2. Left Kan extension from a fibre has the required direction

Let `E:I→Cat`, `T=∫_I E`, and `j_i:E(i)→T`. Write an object of `T` as `x∈E(k)`. A morphism `x→j_i(z)` has a specified base arrow `α:k→i` and a fibre arrow `α_!x→z`. Therefore

`(x/j_i) ≅ ⨿_{α:k→i} (α_!x / E(i))`.

Every component has initial object `(α_!x,id)`. In the contravariant convention the left-Kan formula is the homotopy colimit over the **opposite** comma category. Its components consequently have terminal objects, so

`((j_i)_! Z)_x ≅ ⨿_{α:k→i} Z_{α_!x}`.

This is C.8.3 with the correct base direction. If `x→x'` is vertical, the induced map on every summand is the value of `Z` on the transported vertical arrow. It is an isomorphism when `Z` is locally constant. Thus `(j_i)_!` takes fibre-local constants to vertical constants. The assertion would generally have the wrong direction under a silent switch to covariant diagrams; no such switch is made in C.8.

## 3. The projector square is a canonical isomorphism

Let `VC(T)` denote vertical constants and `LC(E(i))` fibre-local constants. Restriction `j_i^*` sends `VC(T)` into `LC(E(i))`. By the preceding point the restricted left Kan extension is its left adjoint.

For `Z∈LC(E(i))` and `X∈D(T)`, the following natural chain proves the claimed identity without relying on a merely suggestive square:

`Hom_LC(Z, j_i^* R_T X)`

` ≅ Hom_VC((j_i)_! Z, R_T X)`

` ≅ Hom_D(T)((j_i)_! Z, X)`

` ≅ Hom_D(E(i))(Z, j_i^* X)`

` ≅ Hom_LC(Z, R_E(i) j_i^* X)`.

Yoneda gives the canonical isomorphism `j_i^*R_T ≅ R_E(i)j_i^*`. Since the Hom isomorphisms are those of the actual adjunctions, this is the mate isomorphism and is compatible with their units and counits, exactly as needed later.

## 4. Right Kan extension along the Grothendieck functor

For a natural transformation `u:E→F` and `x∈F(i)`, an object of `(ū/x)` is `(k,y,α:k→i,v:F(α)u_k(y)→x)`. Send it to `(E(α)y,v)` in `(u_i/x)`, using naturality `u_i E(α)=F(α)u_k`. The cocartesian arrow from `(k,y)` to `(i,E(α)y)` is the unit. The cocartesian universal property gives the adjunction between this transport functor and the strict-fibre inclusion.

Thus `(u_i/x)→(ū/x)` has a **left** adjoint. Its opposite is a left adjoint, hence homotopy initial for the limit formula. In the contravariant convention right Kan extension is computed over `(ū/x)^op`, so fibre restriction gives precisely

`(j_i')^* ū_* ≅ (u_i)_* j_i^*`.

This verifies C.8.5, including its direction. No local-constancy hypothesis is needed for this Kan comparison.

## 5. Fixed `D` versus all shifts

On vertical-constant categories the right adjoint to `ū^*` is `R_T' ū_*`. The two canonical comparisons just checked identify the restrictions of its unit and counit with those of

`u_i^*:LC(F(i),D) ⇄ LC(E(i),D):R_F(i)(u_i)_*`.

The hypothesis `u_i∈W_D` says these fibre adjunctions are equivalences for the **fixed `D`**. Their units and counits are therefore isomorphisms. Evaluating the global unit/counit at each object in each fibre gives isomorphisms; Der 2 makes the global maps isomorphisms. This uses no premise that `u_i∈W_{D^J}` for every `J`. The shifts in the projector construction provide coherent functors; they do not strengthen the theorem's equivalence hypothesis.

## 6. Passage from vertical to full local constancy

For `α:i→k`, the cocartesian natural transformation `j_i'⇒j_k' F(α)` induces, by contravariance, a map

`F(α)^*(Y|_F(k)) → Y|_F(i)`

in `D(F(i))`. When `Y` is vertically constant, both sides are locally constant on `F(i)`. Pulling back along `u_i` produces the analogous comparison for `ū^*Y`. Since the fixed fibre equivalence `u_i^*` reflects isomorphisms, full local constancy of `ū^*Y` implies full local constancy of `Y`. The reverse implication is direct. Every total-category arrow factors into a cocartesian arrow followed by a vertical arrow, so these are all the tests required. The established equivalence on vertical constants therefore restricts to the full locally constant subcategories.

## 7. Span realization and the exact inclusion

For the two diagrams `E=(P→U,P→P)` and `F=(P→U,P→V)`, objectwise `W_D` equivalence gives `∫E→∫F∈W_D`. The endofunctor moving the second `P` copy to the first has the two indicated natural transformations; hence `U→∫E` is a nerve homotopy equivalence.

If `X=U∪V` is a full open-sieve cover, every nerve simplex belongs to one sieve: the last vertex does, and sieve closure pulls all earlier vertices and arrows into it. Consequently `NX=NU∪_{NP}NV`. Both inclusions from `NP` are monomorphisms, so this is a homotopy pushout. The Grothendieck construction of the span realizes that homotopy pushout, giving `∫F→X∈W_∞⊂W_D`. The composite is the specified inclusion `U→X`, rather than an unrelated map between the same objects. Empty intersections and degenerate coefficient theories cause no exception to these steps.

## Conclusion

No gap found. For maximal readability, the Hom chain in §3 could be added after C.8.4, and one sentence could state explicitly that only the fixed-`D` fibre equivalences are used in the Der 2 step. These are optional clarifications; the present proof already supplies the needed ingredients.
