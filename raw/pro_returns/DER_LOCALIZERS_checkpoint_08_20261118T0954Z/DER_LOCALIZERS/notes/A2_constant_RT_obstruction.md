# Auxiliary obstruction: free pointing need not reflect split maps

**Status:** complete auxiliary counterexample, recorded as a proof-route obstruction rather than an additional numbered main theorem. The parent independently checked its categorical structure. The finite torsion calculation is executable in `code/A2_verify_lattices.py`. This does not refute constant-only RT-fixedness: A2.14 proves that conclusion for this enhanced example and for all complete and cocomplete infinity categories.

## The two coefficient fibers and their Grothendieck construction

Put A0=D(Z)≥0/Z[0] and A1=D(Q)≥0/Q[0]. Let L:A0→A1 be rationalization. Its right adjoint is

R0(W→Q) = τ≥0(W×_Q Z)→Z,

where the pullback is taken in derived abelian groups. Consider the infinity categorical Grothendieck construction B of L over the ordered set 0<1. Its objects are pairs (q,s), with q∈A_s. Within each fiber mapping spaces are those of that fiber; from (q,0) to (q′,1) they are Map_A1(Lq,q′); there are no maps from label1 to label0.

B is complete and cocomplete. A diagram with at least one label1 object has colimit in fiber1, obtained after applying L to all fiber0 entries; an entirely label0 diagram has colimit in fiber0. The empty colimit is the initial fiber0 object. For limits the dual description uses R0: an entirely label1 diagram has its limit in fiber1, and a diagram with a label0 object has its limit in fiber0 after replacing fiber1 entries by R0. These descriptions follow from the displayed mapping-space formulas and the adjunction. They extend to arbitrary small shapes, including the terminal object (id_Q,1).

Let C be the full subcategory retaining all objects of A0 and only those A1 objects whose H0 augmentation is nonzero. As in A2.12, a map to a zero augmentation forces the source augmentation to vanish. In particular there is no map from an allowed label1 object to an excluded label1 object.

The inclusion C→B has right adjoint which fixes allowed objects and sends an excluded (q,1) to (R0q,0). Mapping spaces from label0 objects agree by L⊣R0; mapping spaces from allowed label1 objects are empty on both sides. Thus C has all limits. The inclusion creates all colimits: if a colimit has label1 then some input has label1, whose nonzero augmentation prevents the colimit augmentation from vanishing. A label0 colimit is always allowed. Hence C is also cocomplete.

For a zero-augmentation object q:W→Q, R0q has underlying connective complex W (regarded over Z), with zero augmentation. Indeed the extra summand is τ≥0fib(Z→Q)=0, since Z→Q is injective and its only nonzero fiber homology is Q/Z in degree −1. In particular R0(0→Q)=(0→Z), the global initial object.

## Accessibility

Every augmented connective Z or Q complex has a nonnegative free replacement and is the filtered union of bounded finite free cell subcomplexes. Label0 approximants remain label0. For a nonzero label1 augmentation, fix a degree-zero element with nonzero rational augmentation and use the cofinal finite-free approximants containing it. There is a set of these objects.

A bounded finite free label0 object is compact against filtered diagrams eventually in fiber0 by compactness over Z, and against diagrams eventually in fiber1 because its rationalization is bounded finite free over Q. A bounded finite free label1 object is compact against the cofinal label1 tail, when present; otherwise its maps into the filtered colimit and all stages are empty. These cases prove compactness and accessible generation. Consequently D_C(I)=Ho Fun(NI,C) is a strong derivator on all small categories, by the same explicit Der1–5 verification as A2.12.

## Every constant provisional test passes

A constant label0 coefficient has every nonempty constant Kan value in A0. Every relevant pullback is computed there, because no label1 object maps to a label0 object. The prestable slice A0 gives the required pullback.

For a constant label1 coefficient, every nonempty constant Kan value has nonzero augmentation and stays in A1. If the root comma category is nonempty, the two adjacent comma categories are nonempty, and the whole comparison is the prestable A1 comparison, with no resetting. If the root comma category is empty, its A1 pullback is 0→Q. Coreflection sends this to 0→Z, exactly the required global initial object. If one adjacent comma category is also empty, the mixed-label pullback is computed using R0; since R0 preserves limits and R0(0→Q)=0→Z, the same conclusion holds. If both adjacent categories are empty, all terms are initial. This covers every small constant test, not merely a finite list of fiber cardinalities. A2.1 gives the same conclusion in every shift.

## Free pointing kills a split torsion inclusion

The terminal object is (id_Q,1). Thus free pointing sends a label0 coefficient q to the label1 coproduct id_Q⊔Lq. Let

M=(id_Z,0),

N=((Z[0]⊕Z/2[0])→Z[0],0),

with augmentation the first projection. The inclusion i:M→N and projection r:N→M satisfy ri=id_M. The map i is not an equivalence: its H0 cokernel is Z/2. Rationalization kills this summand, so F(i) is an equivalence. The distinct endomorphisms id_N and ir have equal images under F. Hence F is neither faithful nor conservative on split maps.

An exact finite free model is N1=Z, N0=Z² with d1(t)=(0,2t), augmentation r0(a,b)=a, and i0(a)=(a,0). Over Q the degree-one homotopy h0(a,b)=b/2 satisfies dh+hd=id_N−ir. Over Z a contraction would require 2h0(0,1)=1, impossible modulo2. The checker verifies every displayed matrix identity using exact fractions and checks the mod2 obstruction. It does not use rational rank as a substitute for integral homology.

## The localizers differ

The pointed envelope of C is equivalent to D(Q)≥0: a point from the terminal label1 object forces label1, and the retractive objects of A1 split as Q⊕V over Q. Thus W_(D_C)_*=W_Q.

In C, the label0 coefficient id_Z detects integral chains. Every constant label0 colimit has underlying C_*(BI;Z)⊗^L V, and every constant label1 colimit has underlying C_*(BI;Q)⊗^L W. Integral homology equivalences invert both families; H0 also detects emptiness, so the labels match. Conversely id_Z detects every failure of integral homology. Hence W_D_C=W_Z, strictly smaller than W_Q; for example B(Z/2)→* separates them.

The equality W_D=W_D_* therefore cannot prove the bare constant-only RT theorem. The enhanced proof A2.14 correctly uses all retractive envelopes (C/M)_*, whose intersection recovers W_D, rather than only pointing at the terminal object.

## Source boundary

The construction, all limits/colimits, accessibility witnesses, and finite matrix calculation are explicit here. The background derived-category and homotopy-derivator constructions are exactly those already cited and opened for A2.2 and A2.12. No ordinary categorical Malcev theorem is used to justify the homotopy-theoretic conclusion. The additional primary Malcev source opened while investigating the failed faithfulness route is recorded in D_A2_source_ledger.md; it supplies no premise to this counterexample.
