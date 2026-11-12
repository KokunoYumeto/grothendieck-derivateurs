# The envelope in Chapter V of *Les Dérivateurs* does not exist

*10 November 2026*

## In short

Small categories model homotopy types (Thomason): the nerve gives a localization `φ: Cat → Hot`. Grothendieck factors
it through `Cat hot`, small categories with functors up to natural transformation, and asserts in Chapter V of *Les
Dérivateurs* (ms. 37) that `φ: Cat hot → Hot` has a fully faithful right adjoint: every homotopy type would have a best
categorical model, its *Thomason–Kan envelope*. He builds on it in V ms. 37–52, VII §§10–11 and IX. The editors of the
published edition asked for a proof.

There is none: `φ` has no right adjoint at all. Categories up to natural transformation represent exactly the 1-types:
`X ↦ [BX, Y]` is representable on `Cat hot` if and only if `Y` is a 1-type, and the categories that behave as if they
were envelopes are exactly those isomorphic in `Cat hot` to groupoids. A natural transformation is a homotopy one level
deep, so `π_2` and everything above it is invisible at this level. What survives is a bounded envelope for each size
bound, and the finite-test idea in its space-valued form.

## Why it matters

- It settles a question the editors of the published edition left open, at the exact pages where it arises.
- It tells readers which arguments in Chapters V, VII and IX need another route.
- It shows what survives: below any fixed size, the envelope does exist. So those arguments can be repaired for diagrams
  of bounded size instead of being discarded.
- It marks exactly where categories up to natural transformation stop being enough to do homotopy theory: the point at
  which mathematicians later turned to higher categories, the direction Grothendieck himself was exploring in *Pursuing
  Stacks*.
- The same fact explains why, in *La Longue Marche à travers la théorie de Galois*, passing to fundamental groups loses
  nothing for the anabelian homotopy types studied there.

## Precisely

Write `Cat hot` for the category of small categories with morphisms the functors up to finite zigzags of natural
transformations (`Hom(X, K) = π0 Fun(X, K)`), and `φ: Cat hot → Hot` for the passage to homotopy types (Chapter V,
ms. 11–13).

1. `φ` has no right adjoint, fully faithful or not (against V ms. 37; the envelope `ψφ(K)` of V ms. 42–43 does not exist).
2. A functor `X ↦ [BX, Y]` on `Cat hot` is representable exactly when `Y` is a 1-type. The categories `K` for which
   `π0 Fun(X, K) → [BX, BK]` is bijective for every small `X` are exactly those isomorphic in `Cat hot` to a groupoid;
   they form a reflective subcategory (reflection by the fundamental groupoid), not a coreflective one.
3. For every infinite cardinal `κ`, the functor `X ↦ [BX, Y]` restricted to categories with fewer than `κ` arrows is
   representable (a bounded envelope); no single category works for all sizes.
4. The finite-test idea (V ms. 37–52, VII ms. 121–150, IX ms. 9–13) holds for space-valued tests: they are
   fully faithful, and groupoid-valued tests on finite CW types decide maps out of countable sources; no finite
   height works in general. It fails for sets of homotopy classes.
5. Small models: a 5-element monoid whose classifying space is `S²`, a 7-element monoid for `S³` (no monoid of
   order 6 has this homotopy type), and a category with 3 objects and 9 arrows for `RP²`.

## Status

- Proofs: GPT-6 Astra (OpenAI, ChatGPT Pro mode), answering questions set by Claude Fable 5.2 (Anthropic, effort high)
  on 10 November 2026 from its reading of the manuscript and of the companion's audit. Statement 1 was its first lead,
  with a sketch of the argument (a simple group larger than the category), and the 1-type classification in statement 2
  its conjecture; the answer gave the complete proofs.
- Checked on 10 November 2026 by two independent Claude Fable 5.2 readers: the author of the questions (effort high)
  and a fresh reader (effort medium). Both checked statements 1 and 2. The second also checked
  statement 3 in full, statement 4 including the criterion for countable sources, and statement 5 by enumerating all
  208,672 labelled monoids of order 6. One further claim in the answer rests on an unrefereed preprint and is not used here.
- New? Not claimed. Specialists may know some of these facts in some form; what this adds is their exact statement and
  proof at the places where Grothendieck uses the envelope.
