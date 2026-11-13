# Independent audit of universal component injectivity and C.1 survival

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026.
Reviewer: the `main_compact_duality` branch. No priority claim.

## Status and files read

**Passed.** I read the complete proposed proof in `sections/akr_universal_components_draft.tex`, together with its full point-level descent dependency `sections/akr_birth_cover_descent.tex`. After the independent audits, the proof was promoted to `sections/akr_universal_components.tex`, with labels C:component-two-intersection, C:component-path-inflation, C:universal-components, and C:universal-nontotal; the original draft is retained as an audit record. I also rechecked the strict graph-colimit/fixed-path statement in `sections/akr_attachment_fixed_paths.tex` and the set-necklace threshold in `sections/akr_component_necklace.tex`.

The component intersection lemma, the path bound L_H≤L_U+1, the simultaneous induction, and the universal repaired-C.1 survival conclusion are valid with the stated hypotheses. No mathematical repair was identified. The proof uses the full generated-stage convention, the actual-path-length repair, the original point bounded-chain property, the prescribed incoming generators, and the C.1 numerical bounds. It does not assert the same conclusion for the unrepaired general Part B construction or for arbitrary graph embeddings.

## 1. The maintained data and their permanence

For each old object X, the graph G_X is permanent after its birth: later stages add only new maximal targets and do not add arrows between old objects. Thus H(X)=π_0G_X and the generating H-cover at birth remain the same sets and maps at every subsequent stage. It is legitimate to refer to a fixed forbidden pair of source components while routing its entire actual arrow through later target copies.

The three maintained assertions have different jobs:

1. H-injectivity permits inverse images of component-image intersections and cancellation of H(copy maps).
2. The Helly assertion puts an entire component intersection in one incoming source image.
3. Forbidden-pair routing produces an equality of actual arrows, not merely an equality of their H-images.

The proof keeps these distinctions throughout.

## 2. Exact intersection spans when the overlap has at least two components

If h factors through g, its entire H-image is already contained in the H-image of g, so the immediate factorization span represents the whole intersection.

Otherwise, let I be their H-image intersection. Its preimage under injective H(h) cannot contain a forbidden pair, since the routing assertion would then factor h through g. The Helly property puts the entire preimage in one incoming H-cover image H(e)(H(E)). Replacing h by he does not enlarge its H-image and retains every point of I. Hence its new intersection with the H-image of g is exactly I, not merely a nonempty subset of I.

The source e:E→P is strictly earlier in generation history. Use a rank assigning V below W and every newly created object above all its old incoming sources. At every unsuccessful factorization step this rank strictly decreases. If |I|≥2, the descent cannot reach V, whose H-value is a singleton. At W, its two H-components are forbidden for its singleton birth cover, so retaining both already forces factorization. Thus the descent must stop in an actual factorization. Its composites give hu=gv and H(hu)(H(R))=I.

For a distinct parallel pair f,g:S⇉T, a factorization f=gq would make q an endomorphism of S. Every such endomorphism is the identity in the generated construction, so this is impossible. At least one strict source-descent step therefore occurs, exactly as needed for the later induction on source rank.

The restriction |I|≥2 is essential and is correctly retained. A one-component intersection need not provide any common underlying point, so the proof does not pretend to lift that case to an actual arrow span.

## 3. The reduced pair has the correct direction

For the actual span fu=gv, the reduced partial relation is v(r)→u(r), both on points and on H-components. This is the correct reversal.

Indeed, if an original component path has source components C_i with

    H(f)C_i=D_i,   H(g)C_i=D_(i+1),

then its internal match H(g)C_i=H(f)C_(i+1) lies in I. Exact representation of I by H(fu)=H(gv), followed by injectivity of H(f) and H(g), supplies a component of R whose v-image is C_i and whose u-image is C_(i+1). Thus r original path vertices give r−1 reduced path vertices. The C_i remain distinct because their f-images are the distinct D_i.

For an original nontrivial component cycle, the closing internal match supplies the last reduced transition as well. It gives a reduced nontrivial cycle of the same length. Strict descent of the source therefore rules out all original nontrivial component cycles before L_H is used as a finite path maximum. No acyclicity of the original component relation is assumed in order to prove it.

## 4. The one-longer point path, including the endpoint issue

Suppose x_0→⋯→x_(p−1) is a nonconstant point path for the reduced pair (v,u), where p≥2. The span identity gives g(x_i)=f(x_(i+1)), so

    f(x_0)→f(x_1)→⋯→f(x_(p−1))→g(x_(p−1))

is an original point-transition walk. The first p vertices are distinct by f-injectivity.

The final vertex cannot equal f(x_j) for j<p−1: that would give a nontrivial directed point cycle, contrary to the established AKR point bounded-chain property. It also cannot equal f(x_(p−1)). In that case the preceding reduced match says f(x_(p−1))=g(x_(p−2)), so g-injectivity would force x_(p−1)=x_(p−2), contrary to the reduced path. This separate last-loop check is necessary; it is explicitly present in the draft and correct.

Thus every nonconstant reduced point path gains exactly one new vertex, proving L_U(v,u)≤L_U(f,g)−1. If there is no nonconstant reduced point path, its conventionally defined maximum is one, and f≠g implies L_U(f,g)≥2, so the same inequality holds.

When |I|≤1, a component cycle of length at least two cannot occur and a component path has at most three vertices. Since f≠g has L_U≥2, this gives the desired bound. When |I|≥2, source induction and the reduced path give

    r−1 ≤ L_H(v,u) ≤ L_U(v,u)+1 ≤ L_U(f,g).

The cases r≤2 are immediate. This proves L_H(f,g)≤L_U(f,g)+1 in every case. The previously observed finite case with point length two and component length three is compatible with, and shows the possible sharpness of, the +1 bound.

## 5. The simultaneous stage induction is not circular

At an old stage, all three structural assertions are assumed. The source-rank lemma then proves component acyclicity and the path bound for every old parallel pair, simultaneously over all its targets. Only after obtaining that bound does the proof construct a new attachment.

For its defining pair, L_U≤n gives L_H≤n+1. The source's numerical inequality gives s=4k+1≥15n and hence k≥n+1. The strict graph-colimit description passes to components because π_0 preserves graph colimits. Thus H of the new target is the actual set coequalizer of the old component necklace, with the same neighboring identities.

The old component maps are injective and their relation is acyclic with paths of size at most n+1≤k. The strict set-colimit lemma therefore identifies this new component diagram with the repaired beta construction at its actual component path lengths. It follows that the new copy maps are injective, that their adjacent intersections are the prescribed source-component images, and that their proper visibility intervals have at most 2(n+1)−2=2n indices. These assertions are proved before the routing induction uses them.

Since s≥15n>6n, the circular-interval Helly argument applies. Full visibility sets impose no restrictions, and proper ones are short enough that a pairwise intersecting family has a common copy. The component birth cover therefore has the maintained Helly property.

To extend forbidden-pair routing, locate the two source components along the shortest index arc from the current copy to the comparison copy. The newly established component overlap description and H-copy injectivity place both old images in the old neighboring leg. The old routing assertion then factors the **actual** arrow through that leg. The actual necklace equation reroutes the entire arrow to the next copy. Repeating reaches the comparison copy, where the old routing assertion applies once more. Equality of H-maps is not used as a substitute for equality of arrows.

For a newly born source itself, only its identity can be an arrow from it into its birth stage; any proper incoming comparison factors through one generating copy and cannot contain a forbidden pair. Distinct new targets have no arrows between them. These observations supply the new-source base case without using a later-stage assertion.

Disjoint sums preserve H-injectivity and have disjoint component covers; routing reduces to the unique common summand. Thus all structural assertions hold at the new stage. The source-rank lemma can then be applied there. Both inductions are well-founded and used in the required order.

## 6. The exact fixed-path kernel now vanishes universally

The previously proved pointwise equalizer descent writes any nonempty equalizer of f,g:S⇉T as e(R) for an actual old arrow e:R→S with fe=ge. Routing makes its graph the induced graph image of G_R. The universal H-injectivity just established for e says that its distinct source graph components stay distinct in G_S. Therefore the fixed subgraph meets each source component in a connected set or not at all.

This is precisely the sufficient condition in the exact fixed-path kernel theorem. Consequently each quasi-filter attachment has zero kernel on the entire old colimit of K, and hence on the old binary H_2. Sum attachments have zero kernel as well. Multiple targets born in one stage contribute a direct sum of the independent attachment relations, since no arrows run between them; the individual zero kernels therefore give the asserted full-stage injection.

At the first stage the only nonzero K-values occur at the two protected cyclic targets. Their cycle generators can both be oriented to augmentation one, giving the map Z²→Z, (a,b)↦a+b. Its kernel contains the nonzero class κ_+−κ_−. It survives every stage by the just-proved injection. Finite nerve chains occur in finite stages, so homology commutes with the increasing union and this class remains nonzero in the final category of elements.

## Final scope of the audit

The universal quantifier over all repaired C.1 admissible numerical choices is justified: the proof uses only the original lower bound s≥15n, not any additional selected diameter or ordering threshold. It proves that every such repaired AKR category is not total, with an explicit persistent binary second-homology class. The older selected-target proof remains a valid special case, but its additional choices are no longer needed for this conclusion.

This does not retroactively validate the unrepaired common-n formula where exact consecutive overlaps fail, and it does not assert that arbitrary graph embeddings satisfy the component path bound. The required forbidden-pair routing is a property of the actual generated arrows and their birth covers.

## Optional unused-point extension, audited separately

After the canonical proof was accepted, I read the added paragraph allowing extra unused underlying points while retaining exactly the prescribed generating arrows. Its represented-point argument is valid under that convention. Call a point represented when it is the value of a V-arrow. Preservation is immediate, and reflection follows inductively: for old defining maps f,g, the two endpoints f(x),g(x) have exactly the represented status of x. Thus every entire point-transition path has constant status; the repaired beta maps, fixed pieces, and private pieces cannot mix statuses. Fresh unused points lie outside every generating image and are unrepresented.

Restricting to represented points therefore retains whole actual-length path pieces and their exact overlap formulas. It does not make the invalid common-n truncation. The graph vertices are precisely these represented points and its edges remain the actual W-arrows, so the strict graph colimit and the component induction are unchanged.

For the equalizer step, one must use fixed **represented** points. Their birth cover is complete, and forbidden-pair routing still factors entire actual arrows. If the current actual composites differ, source descent continues; at V, a nonempty represented fixed set forces equality of the concrete singleton maps. If equality occurs earlier, the represented image of that descent arrow is exactly the retained fixed set. This does not assume that restricting an arrow to represented points is faithful. The point-path maximum in the source-rank proof remains the maximum on the full underlying set, so distinct actual arrows still have a nonconstant point transition.

I requested one textual precision in the final survival proof: for this optional enlargement it should refer to the represented-fixed-set variant just proved, rather than applying the raw point-equalizer proposition without qualification. This clarification has been included in the promoted final file. The canonical supplied C.1 construction has every point represented and needs no such amendment.
