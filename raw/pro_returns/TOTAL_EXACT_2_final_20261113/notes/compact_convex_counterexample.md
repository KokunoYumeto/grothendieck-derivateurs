# Compact convex inverse limits: counterexamples under totality

AI-produced by GPT-6 Astra (OpenAI), 13 November 2026.
Root proposed the layer-cake/separation route; an independent audit
verified it and sharpened the uniform gap from 1/2 to 1.

## Result and scope

Neither quasi-filteredness nor totality implies that every contravariant diagram
of nonempty compact convex sets and continuous affine maps has a
nonempty strict inverse limit. A complete counterexample uses any
repaired AKR category K* with its proved three-point expansion bound.
The same construction also applies to the ordered predimension
category C_delta, which is total by Theorem A:predimension-total.
The diagram values are finite-dimensional compact convex polytopes.
Thus this refutes the proposed inverse-limit principle even under
totality. The original AKR counterexample is retained; its universal
nontotality is now proved separately by component descent.

Full proof is in `sections/compact_convex.tex`, with labels
`CC:positive-gap` and `CC:convex-counterexample`.

## Positive approximation bound

For every nonempty finite set S of W-arrows into X, the all-ring AKR
proof establishes that the union of their three V-points has cardinality
strictly greater than (3/2)|S|. The predimension category has precisely
the same support inequality: the increasing W-arrows have distinct
hyperedge images; if U is their vertex union, then

    2|U| > 3|E_X(U)| >= 3|S|.

All vertices in U are actual V-arrows by composition, regardless of
whether unrelated raw vertices of X are d-closed. Let t_g>=0 with finite support and
sum t_g=1, and define the three probability marginals

    mu_i(v)=sum_{g:gv_i=v} t_g.

Define w(v)=max{t_g:g is incident to v}, with maximum 0 for the empty
set. Integrating the expansion inequality over the threshold sets
S_s={g:t_g>s} gives sum_v w(v)>=3/2. Since nonnegative coefficients
give w(v)<=max_i mu_i(v), and

    max_i mu_i(v) <= mu_1(v)
                    + (mu_2(v)-mu_1(v))_+
                    + (mu_3(v)-mu_1(v))_+,

equal total marginal masses imply

    3/2 <= 1 + (1/2)(||mu_2-mu_1||_1+||mu_3-mu_1||_1).

Thus the sum of the two distances is at least 1, uniformly in X and
t. For any individual finite probability support the integrated
support inequality is strict, but the uniform bound at least one is
all that the separation proof needs. The weaker 1/2 bound from the initial proposal was already enough;
using equality of the positive and negative total variations yields
the displayed sharper bound. No uniform positive gap between the
stage constants a_m and 3/2 is needed.

## The compact convex diagram

For each X let D_X[g]=([gv_2]-[gv_1],[gv_3]-[gv_1]). If W->X is
nonempty, the convex hull of these finitely many columns misses the
open l1 unit ball. Separation gives a functional lambda of linfinity
norm one with lambda(D_X[g])>=1 for every g. Equivalently there exist
two functions phi_i:Hom(V,X)->[-1,1] such that

    phi_1(gv_2)-phi_1(gv_1)
    + phi_2(gv_3)-phi_2(gv_1) >= 1

for every g:W->X. The set C(X) of all such pairs is a nonempty closed
convex subset of the finite cube. If Hom(W,X) is empty the inequalities
are vacuous and C(X) is the full cube.

An arrow u:X->Y restricts potentials by phi_i(v) -> phi_i(uv). The
constraint for g after restriction is the constraint for ug before
restriction, so this defines a contravariant diagram with continuous
affine maps.

A compatible family would satisfy phi_(i,X)(v)=phi_(i,V)(1_V) for
every v:V->X. Its functions would therefore be constant across every
point-map hom-set. The inequality at X=W, g=1_W would become 0>=1.
Hence the strict inverse limit is empty.

## Consequences for attempted proofs

This rules out an unrestricted categorical-amenability lemma deriving
compact convex inverse-limit existence from either quasi-filteredness
or totality. In particular the totality-specific bounded-potentials
hope is refuted by the explicit C_delta diagram.
In particular it cannot be used without additional hypotheses to
extend the bounded marked-cycle functionals in the AKR persistence
problem. The specific diagram arising there might still admit a
compatible point for special reasons; no assertion to the contrary
is made.

No mathematical program was needed: the proof uses only the already
audited AKR expansion inequality or the positive-predimension support
inequality, finite sums, integration of finite step functions, and
finite-dimensional convex separation.
