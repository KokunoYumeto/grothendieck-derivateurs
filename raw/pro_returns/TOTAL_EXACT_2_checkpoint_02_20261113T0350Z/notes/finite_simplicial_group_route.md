# The simplicial free-group route: a precise obstruction and a conditional test

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. This note is a new investigation after the independent audit of the current paper. It does not establish totality or nontotality of the repaired AKR category and does not settle totality ⇒ exactness. All claims marked proved below have arguments in this note; no literature priority claim is made.

## 1. What totality actually supplies

Let A be nonempty, connected and total in the manuscript's sense. For a simplicial set diagram X:A→sSet, the simplicial replacement in each internal degree n is the nerve of the category of elements of the action a↦X(a)_n. Each of its components is contractible. Consequently the replacement augmentation induces a weak equivalence

    hocolim_A X ≃ colim_A X,

where the right side is the ordinary degreewise Set-colimit. This statement does not assert that the right side is a nerve, a Kan complex, or the underlying simplicial set of a colimit in an algebraic category.

For a diagram G:A→Grp of free groups, the integral homology spectral sequence of hocolim_A BG has only rows q=0,1. They are the constant Z diagram and G_ab, respectively. Since BA is contractible, the q=0 row contributes nothing in positive columns. Thus

    H_2(hocolim_A BG;Z) ≅ T_1(G_ab).

Higher differentials cannot affect this term: the only potential incoming differential starts at H_3(BA)=0, and the target of an outgoing differential has negative first index. For the AKR free-group diagram constructed in `sections/akr_links.tex`, its abelianization is the already audited column quotient Q, and T_1(Q)=Z. If that indexing category were total, therefore,

    H_2(colim_A BG;Z) = Z.

This is entirely consistent unless some additional property of this particular ordinary simplicial colimit forces H_2 to vanish. Freeness and individual free-factor inclusions do not force that vanishing in general.

## 2. Proved counterexample to the naive ordinary-nerve claim

Let C be the category with objects 0,1 and two distinct arrows f,g:0→1. Define a free-group diagram by

    G_0 = F(a,c),       G_1 = F(a,c,b),
    f(a)=a, f(c)=c,     g(a)=ab, g(c)=cb².

Both arrows are inclusions of free factors. This is immediate for f. For g, the automorphism of F(a,c,b) defined by

    a↦ab, c↦cb², b↦b

has inverse a↦ab⁻¹, c↦cb⁻², b↦b, and carries f(G_0) to g(G_0).

### Lemma: the two image subgroups intersect trivially

Write A=F(a,c) and B=F(b), so G_1=A*B. Let w be a nonempty freely reduced word in a,c. Replace each positive a or c by ab or cb², and each negative a⁻¹ or c⁻¹ by b⁻¹a⁻¹ or b⁻²c⁻¹. All a,c letters survive reduction in the free product A*B.

The only places where b-blocks from distinct letters can merge are a positive letter followed by a negative letter. If their underlying generators coincide, the original word was not reduced. Otherwise the exponent difference is ±1, so that b-block does not vanish. No other internal b-block cancellation can eliminate an A-letter or a nonzero B-block.

If w starts with a negative letter, its image starts with a nonzero B-block. If w ends with a positive letter, its image ends with a nonzero B-block. In the remaining case it starts positive and ends negative, so it has a positive-to-negative transition, at which the preceding argument gives a nonzero B-block. Hence g(w) is not in A for any nonempty reduced w. Therefore

    f(G_0) ∩ g(G_0) = {1}.

This is a normal-form proof, not an inference from bounded word enumeration.

### Proposition: the ordinary simplicial colimit has H₂=Z

The intersection lemma implies that the two simplicial subsets Bf(BG_0) and Bg(BG_0) of BG_1 intersect only in their common basepoint. Indeed, in nerve degree n their intersection consists of tuples of elements belonging to both image subgroups. Hence the map

    BG_0 ∨ BG_0 → BG_1

induced by f and g is a monomorphism of simplicial sets. The ordinary coequalizer Y=colim_C BG is the pushout of this monomorphism along the fold map

    BG_0 ∨ BG_0 → BG_0.

This pushout is a homotopy pushout. One can verify this directly by replacing the fold map by its mapping cylinder: pushing out the resulting cylinder equivalence along a simplicial monomorphism preserves a weak equivalence. Equivalently, realizations of the displayed inclusion are inclusions of CW subcomplexes.

All three spaces BG_0, BG_1 and BG_0∨BG_0 are aspherical graphs up to homotopy, so their homology vanishes in degrees greater than one. Mayer–Vietoris gives

    H_2(Y;Z) ≅ ker[f_ab−g_ab: Z²→Z³].

In ordered bases (a,c) and (a,c,b), this difference is

    a↦−b,    c↦−2b.

Its kernel is Z·(2a−c), so H_2(Y;Z)=Z. The group colimit, in contrast, is

    colim_C G = ⟨a,c,b | a=ab, c=cb²⟩ ≅ F(a,c).

The first relation kills b, and the second then becomes redundant. In particular, the canonical map

    colim_C BG → B(colim_C G)

cannot be a weak equivalence: its target has H_2=0.

The argument can be strengthened to Y≃BF(a,c)∨S² by replacing the homotopy-pushout diagram by its rose-graph models and eliminating the b-generator with the first 2-cell. The H₂ calculation above is sufficient for the stated obstruction and does not require that stronger homotopy equivalence.

### Scope

C itself is not quasi-filtered or total; its classifying space is a circle. The example therefore does not refute the main implication or settle the AKR case. It proves exactly that the following three pieces of information are insufficient, without a further condition on the indexing diagram:

- all groups are free;
- every transition is a free-factor inclusion;
- the colimit in groups is free.

An argument for the AKR case must use additional structure of its indexing category or of the specific family of presentations. It cannot cite the three properties above as an asphericity theorem for ordinary nerve colimits.

### Reproducible exact certificates

`code/finite_freefactor_nerve.py` and `code/finite_freefactor_nerve.out` verify both Nielsen compositions on all three generators, the identities

    b = a⁻¹ r_a⁻¹ a,
    r_c = c a⁻¹ r_a² a c⁻¹,

and the exact integer Mayer–Vietoris matrix. Its rank is three, a 3×3 minor has determinant one, all five 4×4 minors vanish, and its primitive kernel is generated by (2,−1,−2,1). Hence its kernel is Z and its cokernel is Z², with no numerical rank tolerance or torsion ambiguity. The program additionally checks all 39,364 nonempty freely reduced source words of length at most nine. Those bounded checks supplement the full normal-form proof above; they are not the proof that the subgroup intersection is trivial.

## 3. Proved sufficient condition: a natural graph model

Suppose G:A→Grp is a diagram of free groups and there is a diagram X:A→sSet such that:

1. every X(a) is one-dimensional;
2. there is an objectwise weak equivalence of diagrams X→BG (or a zigzag of such natural weak equivalences).

If A is total and connected, then

    hocolim_A BG ≃ hocolim_A X ≃ colim_A X.

An ordinary colimit of one-dimensional simplicial sets remains one-dimensional: every simplex in degree ≥2 has a degenerate representative, and simplicial quotient maps preserve degeneracies. Its second homology is therefore zero. By Section 1, T_1(G_ab)=0.

This criterion would refute AKR totality if a natural one-dimensional model for the particular free-group diagram could be constructed. Individual free-group bases or individual relative collapses do not supply such a model: they need to commute with all diagram arrows and their compositions. The finite parallel-pair example in Section 2 demonstrates why replacing that compatibility requirement by pointwise freeness is unsound.

For comparison, when G=F[S] is freely generated by a covariant Set-action S, there is a natural graph model, the wedge of circles indexed by S. In that case the criterion applies; algebraically G_ab=Z[S] is already a permutation module, whose acyclicity is part of totality. The AKR group diagram has free values but no natural generating Set-action has been constructed.

## 4. Augmentation ideals: what is obtained, and what remains circular

Write I(G)=ker(Z[G]→Z) for the augmentation ideal of the group ring, regarded just as an abelian-group diagram. The identity element splits the augmentation naturally, so

    Z[G] ≅ Z ⊕ I(G)

as diagrams. For every k≥1, the natural direct-sum expansion of

    Z[G^k] ≅ Z[G]^{⊗k}

therefore contains I(G)^{⊗k} as a direct summand. Under totality all Z[G^k] are acyclic permutation modules. Thus every I(G)^{⊗k}, including I(G), is acyclic for positive derived colimits.

This does not yet prove acyclicity of G_ab. The natural quotient is

    I(G)/I(G)² ≅ G_ab.

The multiplication image I(G)² is not the ordinary tensor product I(G)⊗I(G); its kernel carries the relations. Replacing that image by the tensor product would be an error. For free G, the reduced bar complex with terms I(G)^{⊗k} has homology G_ab in degree one and zero in higher degrees. Applying colim to this acyclic-term resolution computes the derived colimit of G_ab, but does not make the resulting complex exact automatically. That would assume the result being sought.

Thus the augmentation-ideal observation produces a useful exact reduction, but it does not bypass the simultaneous-relation obstruction. No assertion that Set-colimits commute with finite products, or that ordinary colimits of group nerves are nerves, is used in this note.

## Status

The new finite free-group counterexample and the natural-graph sufficient criterion are proved. A natural graph model for the AKR free-group diagram has not been constructed, and the totality-specific augmentation-ideal route remains unresolved. This note records an obstruction to an overly broad shortcut, not a counterexample to totality ⇒ exactness.
