# Additional raw-gate observations during the CP07 build

18 November 2026. This is a research note, not another numbered result or a claim
that C.raw_gate has been settled. Main C.27 and its metadata were frozen for the
checkpoint build before this note was written.

## A projective normalized unit is finitely presented in the corollary

In the module-category setting, canonical normalization and the adjunction give
End_M(1)=Hom_k(phi(1),k)=k, with scalar multiplication corresponding to the
ordinary scalar endomorphism. In particular phi is faithful on End_M(1).

Suppose 1 is projective. Split a projective-generator epimorphism to obtain maps
u:1 -> direct_sum_i h_i and v:direct_sum_i h_i -> 1 with vu=id. Write u_i for the
coordinate maps and v_i for the summand maps. Applying the cocontinuous phi sends
u to k -> direct_sum_i phi(h_i), so its image has finite support S. For i outside
S, phi(v_i u_i)=0, hence v_i u_i=0. Since M is a module category, the equality
vu=sum_i v_i u_i is evaluated on each element by a finite sum. All nonzero
summands lie in S, so id_1=sum_{i in S}v_i u_i. Thus 1 retracts a finite sum of
representables and is finitely presented projective. No pointwise formula for
the internal tensor is required for this observation.

This only supplies the unit factorization condition in C.27 when an appropriate
flat interval presentation is already available. It does not show the unit is
projective, show an arbitrary interval is flat, or supply a finite projective
resolution of the covariant weight phi. In particular it must not be promoted to
an FP-infinity statement about phi.

## Why a coproduct-lift variant adds no projective-unit case here

There is a mild variant of the C.27 proof. If alpha lifts to the canonical
epimorphism direct_sum_i P_i -> J, the large coproduct is projective, so the
pointwise pure unit inclusion into it splits over k. Its adjunction retraction
exists just as in C.27. A homology class has finite support among the P_i
summands. Move those finitely many summands to one later stage where their sum
vanishes, leaving the other summands unchanged and using an extra copy of that
later stage. This gives a new projective coproduct and a new lift of alpha; its
retraction kills the original class. Coherence of retractions is again not used.

A projective unit provides such a lift. However the preceding argument already
makes that unit finitely presented under the normalized corollary hypotheses,
so it is already covered by C.27's stated stage-factorization condition. This is
not counted as a new domain of the theorem.

## Remaining obstruction

Removing the flat-interval presentation would require an additional argument.
A projective cover P -> J and a lift of alpha do give pointwise split inclusions
into P after scalar purity, but P tensor X need not be null. Replacing the
filtered presentation by a projective resolution introduces higher terms rather
than later-stage vanishing. The total complex of their F-images is not F of one
object with the required adjunction retraction. We have not supplied that
missing comparison. Similarly, a null-homotopy F -> F(J tensor -)[1] does not
reverse the direction of the counit-extension problem.
