# Independent mathematical audit of Parts C and E

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), within the present collaboration. No priority is claimed. This audit read the current `sections/C.tex`, `sections/E.tex`, `sections/C_paths.tex`, `code/e_finite_checks.py`, its recorded output and category-table construction, the relevant VII-c companion proofs, and the full supplied TOTASPH G proof.

**Conclusion:** no mathematical error or unsupported strengthening was found in the requested high-risk statements. In particular C.8, E.5, the all-n version of E.7, and E.9 pass independent verification. E.12's inherited argument is complete and the compact presentation is sufficient once its verified source is retained. The main recommended addition is an explicit definition of the two lifting categories used to specify smoothness and properness. Their variance was checked against the original Maltsiniotis paper. The root-owned TeX files were not edited by this audit.

## 1. Smoothness, properness, and the strict lifting obstructions

The terminology in E.3–E.6 is mathematically consistent with the intended nerve-localizer convention. To make that convention self-contained, insert the following definition before the first use.

For p:E→B, u:b→b′, and e′ over b′, the incoming lift category has objects h:e→e′ with p(e)=b and p(h)=u. Its morphisms h→h₁ are arrows v:e→e₁ with p(v)=1_b and h₁v=h. Smoothness means that every such category has weakly contractible nerve. Dually, for e over b the outgoing lift category has objects h:e→e′ over u; a morphism h→h₁ is v:e′→e₁′ over 1_b′ with vh=h₁. Properness means that these categories are weakly contractible.

These are the comma categories for the canonical strict-fibre inclusions into the appropriate under- and over-comma categories. Maltsiniotis (2005), Theorem 1.2(b), gives the incoming version and states the duality with properness immediately afterwards. Proposition 4.7 gives closure under composition and base change. The original PDF was opened and these statements read in this audit.

E.3 uses the correct incoming/outgoing convention. A morphism from an empty path to a path of type τ requires an endpoint-preserving map from the one-vertex interval to Iτ. This forces τ empty. Thus the outgoing lift of (1₀,w):(0,0)→(0,1) cannot exist, proving failure of properness and of an opfibration. Reversal of X does not reverse the indexing category of the fibred Grothendieck construction, so the diagnosis of the manuscript's duality error is correct.

The proposed terminal incoming lift at the empty path 1 also fails. For a candidate c of type τ, the doubled path d is constant 0 on the first block and equals c on the second. The two block collapses are distinct when τ is nonempty. One pullback of c is exactly d; the other equals c on the first block and is constant 1 on the second. The pointwise inequalities needed for d to map to the latter exist in [1], and thinness supplies naturality. Both arrows commute with the unique map to the empty path 1. Hence the incoming lift category cannot have a terminal object. This is a necessary condition for a Cartesian lift, so it validly refutes a Grothendieck fibration.

The smoothness argument can also be understood directly. Given an incoming endpoint arrow and target path c, append those endpoint arrows to c, reversing the final one, to get the preferred lifted path. Padding each other lift by identity edges gives a functor with a natural transformation to that lift and a natural transformation to the preferred lift. This supplies a categorical contraction of the lift category. Its type changes have the required direction; no opposite-category shortcut is involved.

E.4's eventual-path obstruction is likewise valid. The delayed or advanced single-transition paths give actual objects of the same lift category, while a pointwise inequality would require 1→0 at a selected coordinate. The obstruction quantifies over arbitrary supports, not a fixed finite stage. Weak contractibility of filtered unions of the finite-stage lifting categories does not retain terminal or initial objects.

The rectangular-band argument E.6 is valid for the stated standard models. The naturality equations have the correct order of multiplication. In the incoming case α_iθ_i=1 is impossible whenever α_i=e₀₀; in the outgoing case θ_iα_i=1 is impossible for the same reason. The delayed-step constructions satisfy all fence-arrow equations. In the all-type model an empty target would require its two endpoint components to coincide, which is incompatible with (1,e₀₀). None of these arguments rules out a different strict bifibration; E.11 properly retains that question.

## 2. E.5 and universal homotopy base change

E.5 does not infer a homotopy-fibre theorem merely from a total-space weak equivalence. Both lifting properties are used, and they suffice.

For an arrow u:b→b′, form M_u whose objects are arrows e→e′ of E over u and whose morphisms are commuting squares with vertical components in the strict fibres. Its source and target projections to E_b and E_b′ are weak equivalences. One proves this by Quillen A: their relevant comma categories retract by precomposition or postcomposition onto the outgoing or incoming lift categories. The defining arrow gives a natural transformation between the associated maps into b\E. Combining this with the strict-fibre-to-comma equivalences shows that u*:b′\E→b\E is a weak equivalence.

The hypothesis of Quillen's Theorem B is now established. Consequently each strict fibre is the homotopy fibre of Bp at its vertex. A strict base change preserves both lift-category conditions, so the same statement holds after every base change. The strict fibre of the pullback at b″ is literally E_{v(b″)}. The induced map of homotopy fibres is therefore a weak equivalence. The fibrewise criterion for spaces over a common base shows that the base-change square is homotopy Cartesian. Empty fibres create no exception.

For σ:P(X)→X the strict fibres are weakly contractible by E.1. Therefore every base change of σ is a weak equivalence, particularly r:E(f)→A. Since ri_f=1, i_f is a weak equivalence. The map E(f)→A×X is a base change of the two-endpoint functor and hence smooth and proper. The projection A×X→X has incoming lift categories A/a and outgoing lift categories a\A, with terminal and initial objects respectively; it is smooth and proper. Closure under composition gives the assertion for p_f. The equality p_fi_f=f then transports its exact-fibre theorem to the homotopy fibres of Bf.

The functorial formula on a strictly commuting square is exact: apply its source functor to a and its target functor pointwise to the path. Constant paths and both endpoints are preserved as equalities. No Thomason cofibration, Thomason fibration, or additional right-properness axiom is needed. The current claim is correctly limited in this respect.

## 3. E.7: the extra n=1 case and the infinite family

The analytic proof works for every n≥1. The following checks distinguish its universal argument from the finite numerical checks.

The source A_n consists of the lower fence and the two upper endpoint leaves. It is a full sieve, and its nerve is a tree. The product P_n=[1]×Φ_n is contractible. Thus A_n→P_n is a weak equivalence. The specified F:A_n→C is a functor: only the lower-left horizontal and vertical edges have nonidentity images r and v; all other generating arrows map to identities at a.

The four-object C is exactly two categorical cones on the category of two parallel arrows, glued along that category. Its nerve is a suspension of the parallel-edge circle. Thus BC is homeomorphic to S², not just a space with the homology of S². Adjoining a terminal s gives the contractible D.

The sieve pushout's crossing Hom formula is correct. It is the coend of the covariant functor D(d,F−) and the contravariant functor P_n(−,u_k). For k=1 and n≥2, the predecessor diagram consists of l₀,l₁,l₂,u₀, with arrows l₀→l₁, l₂→l₁, l₀→u₀. Its map to the fork z→a,z→b is final. When n=1 there is the additional predecessor u₂, attached through l₂→u₂ and also mapping to a. Over a, its comma category is now l₁←l₂→u₂, still nonempty and connected. Over b it is a point; over z the whole tree is connected. Thus the added predecessor does not change the colimit.

The fork's inclusion into C is ordinary final. At x its comma category is the connected square with vertices (z,λ),(z,μ),(a,η),(b,θ); it is deliberately not homotopy final. Consequently the crossing Hom set to u₁ is a singleton for each d in C and empty for d=s. This calculation is a set-colimit calculation, so ordinary finality is exactly the necessary notion.

For every k≥2 the predecessor diagram is nonempty and connected and maps constantly to a. Its crossing presheaf is therefore D(−,a). All upper arrows between such complementary objects act as identities of that representable presheaf; the possible upper arrow u₂→u₁ acts by its unique map to the singleton presheaf on C. These formulas define the retraction sending every u_k with k≥2 to a. The arrows represented by 1_a give the claimed natural transformation from inclusion-after-retraction to id_Q. For n=1 there are no such extra complementary objects, so the retraction is already the identity on Q.

The retract is precisely two terminal cones on C, with no arrows between their tips. Hence BQ≃ΣBC≃S³ for every n≥1. The map A_n→D is a weak equivalence, and its pushout is the non-equivalence P_n→Q. This directly refutes the defining preservation condition for an intrinsic W∞-cofibration. The word “pushout” here never silently means homotopy pushout.

I inspected the program's coend generators and equivalence relations. For an arrow α:w→w′ the code identifies (w′,F(α)h,u) with (w,h,uα), in the correct variance. It constructs all resulting arrows, compositions, identities and composable triples, and verifies associativity. Its normalized-nerve differential omits degenerate composite faces correctly. The reported Betti numbers use rational ranks; the TeX correctly relies on the cone/retraction proof for integral homotopy type.

I reran all checks by loading the module under a non-main name and calling its three check routines. This did not rewrite the original category tables. The independent log is `research/CE_code_recheck.txt`. It reproduced 543 finite [1]-path cases, all 125 rectangular-band associativity equations, and:

| n | P_n objects/arrows | Q objects/arrows | Rational Betti numbers of Q |
|---:|---:|---:|---|
| 1 | 6 / 15 | 6 / 20 | (1,0,0,1,0) |
| 2 | 10 / 27 | 8 / 30 | (1,0,0,1,0) |
| 3 | 14 / 39 | 10 / 40 | (1,0,0,1,0) |

## 4. E.9 and the rational localizer

The pullback square and its failure are correct. The fixed-origin endpoint functor q has weakly contractible total category, and its strict fibre has type ΩBC₂, a disjoint union of two contractible components. The functor e→BC₂ is a rational homology equivalence: group homology in positive degrees vanishes because the group order is invertible in Q, while H₀ is Q. Its base change is the map from the two-component fibre to the contractible total category. On H₀ it is Q²→Q, and it is not an isomorphism.

This example does not conflict with Quillen B or with smoothness/properness. The base map e→BC₂ is not a W∞-equivalence. Homotopy pullback preserves weak homotopy equivalences but need not preserve rational homology equivalences along this map. The text correctly distinguishes the localizer-dependent preservation claim from the valid space-valued fibre theorem. It also uses a fixed-origin exact fibre category, so its morphisms have identity at the origin; omitting that condition would invalidate the contractibility assertion, but it is retained in the intended notation.

## 5. C.8: truncation, tensor product, and signs

The linear construction is correct over an arbitrary commutative ring. D^{≤0}(k) is closed under derived tensor: bounded-above flat/projective resolutions of two nonpositive complexes yield a nonpositive tensor complex. Its inclusion into D(k) is therefore strong monoidal, and its right adjoint τ_{≤0} is lax monoidal. Applying the lax structure to evaluation composition gives the required associative unital maps

\[
\tau_{\leq0}\operatorname{RHom}(b,c)\otimes^L
\tau_{\leq0}\operatorname{RHom}(a,b)
\longrightarrow\tau_{\leq0}\operatorname{RHom}(a,c).
\]

Equivalently, a map with a nonpositive source has a unique factorization through τ_{≤0} of its target in the derived category. Iterated composition has the same factorization for each parenthesization. The tensor unit is k[0], and the identity is a degree-zero cycle. This proof correctly avoids assuming that ordinary Hom complexes are K-flat.

The dg-projective model simultaneously gives strict dg composition on Hom(Qa,Qb). It computes RHom because Qa is homotopically projective and Qb→b is a quasi-isomorphism. Good truncation is compatible with the product: two retained degrees cannot sum to a positive degree, and products of degree-zero cycles are cycles. Reindexing C_i=C^{−i} gives the Dold–Kan space with π_i=H^{−i}. With cohomological shifts, H^{−i}RHom(a,b)=Hom_D(a,b[−i]); the sign in the text is correct. Its example b=k[1] is concentrated in degree −1 and indeed gives K(k,1). Suspension [1] and looping [−1] agree with the pointed mapping identities.

The composition formula is an enhancement claim in the specified dg context. It does not establish that the unrestricted literal path category has that mapping space. C.9 keeps that separate question open, so no unintended generalization occurs.

## 6. Other C statements and E.12

C.1's strict concatenation and product-preserving Ex∞ construction are valid. The Segal nerve's discrete object space makes the displayed products the correct homotopy fibre products; a Reedy fibrant replacement preserves its Segal property. C.2 retains the necessary distinction between weak-vertical hammocks and arbitrary-vertical paths.

C.3's S⁰ unit and C.4's strict zero absorption are correct: in a pointed simplicial category with tensors, the enriched maps to or from the zero object are terminal simplicial sets. Thus the zero axes really collapse, not only up to homotopy. C.6 uses genuine pullback/pushout universal properties; its representability implications have the correct directions. C.7's counterexample is valid: Map_*(K(Z,2),K(Z,2)) has no positive homotopy groups, whereas Map_*(S⁰,K(Z,2)) is K(Z,2), so its loop space is nontrivial despite all the π₁ representability data being zero. The scope qualifications in C.5, C.9 and C.10 avoid promoting unpointed or component-level information to a specified coherent pointed comparison.

The full TOTASPH G proof underlying E.12 was checked directly. Its initial-origin contraction is an actual two-step natural-transformation zigzag: replace a path by the constant initial-object path of the same type; the unique initial-object arrows give the map to the original path, and interval collapse gives the map to the empty path. Initiality proves naturality even across changes of type. The two one-edge paths ending at a and b have no common successor, because endpoint evaluation would give a common successor in the fork Y.

For ordinary finality, an object (c,α:y→end(c)) of y\P receives an arrow from the fixed-end path c followed by α backwards. Its type map collapses the appended edge and its last component is α. The exact fibre is nonempty and connected when BY is connected and simply connected, by the verified localization-word description of π₀. Thus every comma is nonempty and connected. Composing this final endpoint functor with the final fork inclusion into C produces an actual final image with type S². This proves failure of total asphericity, despite the actual Cat-hot contraction.

The compact E.12 proof contains all these mechanisms and may remain compressed; there is no need to repeat the full groupoid-completion proof. Its “moved into the fibre” phrase should be read in the exact direction just given: the fibre object maps to the arbitrary comma object. If desired, adding this arrow direction would remove the only possible ambiguity.

## 7. Exact recommendations and checked references

1. Add the explicit incoming/outgoing lift definitions from §1; retain the stated W∞ scope.
2. Keep E.7's all-n assertion and its n=1 predecessor explanation: both are verified.
3. Keep E.12's compressed source verification. Optionally state the comma arrow direction explicitly.
4. Align the composition notation across C.1 and C.P4: C.1 orders factors as (b,c)×(a,b), whereas C.P4's γ orders them in traversal order (a,b)×(b,c). The identity γ(c,d)=d*c in C.1's convention removes any ambiguity; this is not a failure of the multiplication argument.

Primary pages opened in this audit:

- Maltsiniotis, G. (2005). Structures d'asphéricité, foncteurs lisses, et fibrations. *Annales mathématiques Blaise Pascal, 12*(1), 1–39. [Original PDF](https://www.numdam.org/article/AMBP_2005__12_1_1_0.pdf). Definition 1.1, Theorem 1.2 with duality, and Proposition 4.7 checked.
- Quillen, D. (1973). Higher algebraic K-theory: I. In H. Bass (Ed.), *Algebraic K-theory I* (Lecture Notes in Mathematics, Vol. 341, pp. 85–147). Springer. [Original scan](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf). Theorems A and B, the corollary to B, and the stated variance checked. Earlier obsolete host paths failed; this relocated path worked.
- Chachólski, W., & Scherer, J. (2001). *Homotopy theory of diagrams* [Preprint, arXiv:math/0110316v1]. [Full author preprint](https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/ChacholskiSchererMemoirs.pdf). Theorem 26.8 and Corollary 26.9, including the latter's reduction to the constant-point diagram, opened for the separate C.P2–C.P3 audit. This gives a full independent source for the Grothendieck homotopy-colimit theorem; Cegarra's explicit map remains useful for conventions and naturality.
