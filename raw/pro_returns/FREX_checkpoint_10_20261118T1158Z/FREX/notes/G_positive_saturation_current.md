# Positive saturation as a stricter construction condition

Exploratory status, 2026-11-18, after checkpoint09. No global construction or amalgamation theorem is claimed.

For an injective free-monoid map i:H→P whose induced group map is injective, call its positive image saturated when

    i(H)=P ∩ i(H^gp)

inside P^gp. This is stronger than bifixness. A saturated positive submonoid is left and right unitary, so the image of its free basis is bifix. G.39 does not satisfy this condition: its group images are the entire target groups but its monoid images are proper.

The successful finite G.22 model DOES satisfy positive saturation for all11 point images and all6 edge-chart images in its rank1213 target. The exact script G_twisted_positive_saturation.py builds the folded subgroup graph, compares its positive loop language with the star of the original image words by a finite product automaton, and exhausts all reachable states. Counts are257–268 for point charts and449–528 for edge charts. These are finite language-equivalence checks only, not a global extension.

Two additional finite warnings have now been checked exactly. They remain
construction-scope notes, not main-gate results or new integrated theorems.

1. Saturation plus bifixness and group free-factor embeddings alone still fails even ordinary injective positive amalgamation. Take i(x,y,z)=(ab,ac,bd). Its positive core has exactly these3 first-return paths; adjoin b for a free-group basis. Take j(x,y,z)=(ACBDE,AB,CD), whose positive core likewise has exactly3 first-return paths; adjoin A,C for a free-group basis. The first length cone requires |x|<|y|+|z|, since the difference is |c|+|d|. The second requires |x|>|y|+|z|, since the difference is |E|. In any proposed locally free amalgam all the finitely many positive images and equations fit one finite free chart, whose word length would satisfy both strict inequalities. Thus no such amalgam exists. The proposed remedy would therefore also need compatibility of the abelian positive cones.

2. Even with compatible positive lengths, demanding saturated OUTPUT maps makes the full saturated class unsuitable for unrestricted amalgamation. Inputs i(x,y,z)=(ab,ac,d), j(x,y,z)=(B,AC,AD) are saturated bifix free-factor maps. In any common target the images of a and A both prefix the common image of y, so they are comparable. If a prefixes A, then a prefixes d=AD, contrary to saturation of the first target chart (its distinct atoms cannot become prefix-comparable). If A prefixes a, then A prefixes B=ab, contradicting saturation of the second chart. An ordinary injective monoid amalgam does exist: target Free(a,b,e,C,D), with A=ae,c=eC,d=aeD,B=ab. Thus this second example only refutes closure under saturated amalgam maps, not ordinary injective amalgamation.

The exact prefix constraints of the particular predimension diagram may be more restrictive than arbitrary spans; none of these statements proves that the G22 diagrams cannot extend globally.

## Exact certificates, 11:53 UTC

`code/G_saturated_amalgamation_checks.py` and its `.out` / `.json` files
verify the four saturation assertions by exhaustive product automata.
The reachable state counts are3,6,2,2 respectively. The same script
checks all34 two-sided free-group inverse identities for the following
bases, so each source group is a free factor of its ambient target.

For the first left target, add t=b to x=ab,y=ac,z=bd. The inverse is
a=xt^{-1}, b=t, c=tx^{-1}y, d=t^{-1}z. For the first right target,
add t=A,u=C to x=ACBDE,y=AB,z=CD. The inverse is
A=t, B=t^{-1}y, C=u, D=u^{-1}z,
E=z^{-1}uy^{-1}tu^{-1}t^{-1}x.

For the second left target add t=a: a=t,b=t^{-1}x,c=t^{-1}y,d=z.
For its right target add t=A: A=t,B=x,C=t^{-1}y,D=t^{-1}z.
The ordinary amalgam in item2 satisfies all3 source equations.
Its two target maps are injective by exact Sardinas–Patterson
residual-word exhaustion (the right map is already a prefix code);
independent4×4 unit minors also certify full abelian rank.

In the saturated-output contradiction, saturation is used in its full
group sense. For example, if the ambient image of a prefixes that of d,
the positive quotient a^{-1}d belongs to the embedded first target
group, hence would have to belong to its positive monoid. This is
impossible for distinct source basis letters. The other comparison is
dual in the second target. Input saturation alone does not supply this
property after an arbitrary ordinary amalgam, exactly as the displayed
successful ordinary amalgam demonstrates.

These finite certificates have been run in this session. No claim is
made that a cone-compatible saturated-input span always amalgamates;
that narrower question remains unproved here.

Literature search: “bifix code saturated subgroup free factor amalgamation free monoid”, “bifix saturated free factor”, and “bifix saturation theorem” located the primary paper Acyclic, connected and tree sets (arXiv1308.4260), Theorems5.1 and5.2 in the returned author-PDF excerpt. Those concern freeness and saturation relative to an acyclic language S, not the unrestricted positive saturation P∩H^gp used here and not the desired amalgamation theorem. The full primary proof has not yet been opened in this subtask, and is not used.

Further searches in both engines for “equidivisible cancellative monoid
locally free positive length ordered abelian group”, “locally free monoid
equidivisible”, and “equidivisible free group submonoid” returned the
known discrete-grading criterion (already opened in Lawson–Wallis) but
did not supply the stronger proposed characterization using local group
freeness and a pointed abelian cone. No such converse is asserted.
