# Precise boundaries of C_delta positive-word attempts

AI-produced by GPT-6 Astra, ChatGPT Pro mode, 17 November 2026. These are failed-route checks, not a solution of the requested all-FreeMon subcase.

## 1. One fixed positive ratio chart cannot work globally

For an ordered edge `(a,b,c)`, the group relation is

`u_b u_a^{-1} = v_a v_c^{-1}`.

The most direct one-edge positive chart adjoins the common ratio `t_e`, with

`u_b = t_e u_a`, `v_a = t_e v_c`.

Suppose this particular ratio were a positive nonempty word for every actual one-edge embedding, in a common positive realization of a finite object. Set `U_i = length(u_i)` and `W_i = -length(v_i)`. Then every edge gives

`U_b - U_a = W_c - W_a > 0`.

Consider the ordered 13-vertex hypergraph with edges

`(0,4,5), (0,1,9), (1,2,10), (2,3,11), (3,4,12), (5,6,7), (7,8,9)`.

It is a C_delta object, and all seven one-edge embeddings are strictly closed. The independent program `code/CD_ratio_chart_obstruction.py` checks all 8,191 nonempty vertex subsets: the minimum predimension is 2, the whole predimension is 5, and every proper superset of each edge has predimension greater than 3.

The first two edge equations imply `U_4-U_1 = W_5-W_9`. The next three imply `U_1<U_2<U_3<U_4`, whereas the last two imply `W_5<W_7<W_9`. This is impossible. Nonemptiness is justified in a faithful realization of the displayed free-group diagram because the edge ratio is nontrivial and its image is retained by the proved free-factor inclusion.

This excludes only that fixed ratio-positive chart. A general Levi decomposition can have `u_b=P R`, `u_a=Q R`, `v_a=P S`, `v_c=Q S`, with both `P` and `Q` nonempty. The suffix chart `s_e=u_a^{-1}v_c` is another possibility and is not excluded. Therefore the computation is not a counterexample to all compatible positive bases, much less to every FreeMon diagram.

## 2. Equidivisibility alone gives no asphericity theorem

Let `P={1} ∪ {(i,j):i,j∈{0,1}}`, with `(i,j)(k,l)=(i,l)` and adjoined identity. It is equidivisible: whenever `ab=cd`, either `a=cw,d=wb` or `c=aw,b=wd` for some `w`.

If all four entries are nonunits, equality gives equal left rows and equal right columns; choosing `w=(row(d),column(a))` yields `a=cw,d=wb`. If `a=1`, choose `w=c` in the second alternative; if `c=1`, choose `w=a` in the first. For nonunit `a,c`, if `b=1` choose `w=d` in the first alternative, and if `d=1` choose `w=b` in the second. These cover all cases. The independent program `code/CD_band_levi.py` verifies associativity on 125 triples and the Levi alternatives on all 145 equal-product quadruples.

Nevertheless `BP` has the homotopy type of `S²`: Fiedorowicz, *A counterexample to a group completion conjecture of J. C. Moore*, AGT 2 (2002), 33–35, DOI10.2140/agt.2002.2.33, unnumbered lemma on pp.33–34. The opened primary proof gives a length-two projective resolution whose tensor with the trivial module has the homology of `S²`; all generators are idempotent, so the group completion is trivial, and Hurewicz supplies the conclusion. This is the same opened source already in `CD_references.bib`.

Thus a Levi/equidivisibility statement for a positive colimit cannot, by itself, prove that its classifying space is aspherical. In the merely total case even target asphericity is not necessary for the desired comparison: a positive diagram might have nonzero derived abelianized colimits and a target monoid with the same higher homology. The comparison comma itself remains the object to control.
