# Compact inverse limits and the finite-pattern Ramsey reduction

AI-produced research note, GPT-6 Astra (OpenAI), 13 November 2026.
This note does **not** prove that totality implies exactness. It identifies
precisely an extra compactness assertion that would imply exactness, proves
its Ramsey reformulation, and proves a limited bounded-fibre case. No
counterexample to the extra assertion for a total category was found.

## 1. Definitions

Let A be a small category in which every finite set of objects has a common
successor. In the present application this follows from nonemptiness,
connectedness, and condition I.

Write **CL(A)** for the assertion that every contravariant diagram

    X : A^op -> CompHaus

of nonempty compact Hausdorff spaces has a nonempty strict inverse limit.

Write **FPR(A)** for the following finite-pattern morphism Ramsey property:
for any objects p,q, finite subset S of A(p,q), and positive integer c,
there is an object r such that every colouring

    chi : A(p,r) -> {1,...,c}

admits g:q->r for which chi is constant on gS. Empty S causes no problem:
one can take r=q and g=1_q. For finite hom-sets FPR is precisely the usual
morphism Ramsey property, because one can take S=A(p,q).

## 2. Compact inverse limits are equivalent to finite-pattern Ramsey

**Proposition.** Under the common-successor hypothesis, CL(A) and FPR(A)
are equivalent. No finite-hom-set hypothesis is required.

### CL implies FPR

Suppose FPR fails for p,q,S,c. Necessarily S is nonempty. For every object
a let X(a) consist of all c-colourings of A(p,a) that are nonconstant on
gS for every g:q->a. This is a closed subset of the compact product
{1,...,c}^{A(p,a)}: the bad event that the finite set gS is monochromatic
is clopen. By the assumed failure of FPR, X(a) is nonempty for every a.

For u:a->b, define X(u):X(b)->X(a) by precomposition with
A(p,u):A(p,a)->A(p,b). It preserves the prescribed avoidance condition,
since u(gS)=(ug)S. Thus X is a contravariant nonempty compact Hausdorff
diagram.

A compatible point (chi_a)_a would satisfy

    chi_a(h) = chi_p(1_p)     (h:p->a).

Indeed this is the compatibility equation for the arrow h, evaluated at
1_p. Therefore chi_q is constant on S, contradicting the requirement
for g=1_q. Hence CL fails. This proves the implication by contraposition.

### Finite witnesses for one Ramsey target

If r is a target for p,q,S,c, the clopen sets

    U_g = {chi : chi is constant on gS},       g:q->r,

cover the compact colouring space {1,...,c}^{A(p,r)}. A finite subcover
therefore exists. In other words, one may choose a finite set
G subset A(q,r) such that every colouring is witnessed by some g in G.
This observation is what removes a finite-hom-set restriction from the
iteration below.

### Simultaneous finite-pattern Ramsey

Suppose there are finitely many source objects p_1,...,p_m, finite
S_j subset A(p_j,q), and colour counts c_j. There is a target r such that
every family of colourings chi_j:A(p_j,r)->{1,...,c_j} admits one
g:q->r for which every chi_j is constant on gS_j.

Construct r_0=q inductively. At step j use FPR for the finite pattern

    S_j^(j-1) = union {h_(j-1)...h_1 S_j : h_i in G_i, 1<=i<j}

in A(p_j,r_(j-1)), choosing a target r_j and a finite witness set
G_j subset A(r_(j-1),r_j) as above. The union is finite; for j=1 it
means S_1. Put r=r_m.

Given the final colourings, choose h_m in G_m witnessing chi_m first.
Then choose h_(m-1) witnessing the pullback of chi_(m-1) along h_m,
and continue backwards. Put g=h_m...h_1. For each j, the selected prefix
h_(j-1)...h_1 S_j lies in S_j^(j-1), so the monochromaticity obtained at
step j survives the subsequent choice of this prefix. Thus g works
simultaneously for all j.

### FPR implies CL

Let X:A^op->CompHaus be objectwise nonempty. Its inverse limit is the
intersection, inside the compact product product_a X(a), of the closed
sets imposed by the equations

    x_a = X(f)(x_b),         f:a->b.

It is enough to satisfy every finite collection of these equations up
to arbitrarily small entourages. More explicitly, fix a finite set E
of arrows and, for each source a occurring in E, a neighbourhood U_a of
the diagonal in X(a) x X(a). Compact Hausdorff spaces have their unique
compatible uniformity. Choose a finite cover of X(a) by sets whose
Cartesian squares lie in U_a; for instance first shrink the entourage
and take a finite cover by sufficiently small open neighbourhoods.
Assign each point to one containing cover member to obtain a finite
colouring of X(a). The colouring need not be continuous.

Choose a common successor q of all objects occurring in E and arrows
j_a:a->q. For each source a define the finite pattern

    S_a = {j_a} union {j_b f : (f:a->b) in E}.

Apply simultaneous FPR to these patterns and their cover colour counts,
obtaining r. Choose any z in X(r), possible by nonemptiness. Colour an
arrow h:a->r by the cover colour of X(h)(z). Choose g:q->r supplied by
the simultaneous Ramsey property, and set

    x_a = X(gj_a)(z)

for the finitely many participating objects. For each f:a->b in E,
x_a and X(f)(x_b)=X(gj_b f)(z) have the same cover colour, so their pair
lies in U_a. Assign arbitrary coordinates to the other objects.

Thus every finite set of compatibility equations can be met to arbitrary
uniform accuracy. Compactness turns this into exact compatibility: for
each equation take the closed inverse images of closed entourages of its
diagonal; these closed sets have the finite intersection property by the
construction, and their total intersection is exactly the inverse limit.
Consequently the inverse limit is nonempty.

## 3. FPR implies integral exactness

The circle-character proof already recorded in
`sections/ordered_graphs.tex` applies with S={a_0,...,a_k} instead of the
whole hom-set. It also does not need finite hom-sets if one uses the
injectivity of the divisible abelian group R/Z.

Here are the precise steps. At a Ramsey target r for
c=(3k+1)^k, form

    D : Z[A(q,r)] -> Z[A(p,r)]^k,
    D[g] = ([ga_i]-[ga_0])_(i=1,...,k).

Let augmentation(ker D)=dZ. If d != 1, choose theta=1/2 for d=0 and
theta=floor(d/2)/d for d>=2. Then 1/3<=theta<=1/2, and

    Dt |-> theta * augmentation(t) mod Z

is a well-defined character of im D. Extend it to Z[A(p,r)]^k using
divisibility/injectivity of R/Z. This gives circle-valued potentials
lambda_i on A(p,r), with representatives in [0,1), satisfying

    sum_i (lambda_i(ga_i)-lambda_i(ga_0)) = theta mod Z

for every g:q->r. Colour h:p->r by the k-tuple of integers
floor((3k+1)lambda_i(h)). FPR gives a g whose displayed family has one
colour; then the absolute value of that sum is less than
k/(3k+1)<1/3. This contradicts the circle equation. Therefore d=1,
so the family has an integral affine equalizer. Common successors and
simultaneous affine equalization make Aff_Z(A) filtered, hence A exact.

Consequently the compact route would establish the desired implication
if totality implied CL, or equivalently FPR. That implication remains
unproved here. The argument does not establish its converse, nor that
exactness itself implies FPR. In particular, signed integer measures
must not silently be replaced by probability measures or genuine points.

## 4. A bounded finite-fibre case follows already from quasi-filteredness

**Proposition.** Suppose A is nonempty, connected, and quasi-filtered.
If X:A^op->FinSet is objectwise nonempty and |X(a)|<=N for one finite N,
then lim X is nonempty.

**Proof.** Define A_X with the same objects as A, identifying parallel
arrows f,g:a->b precisely when X(f)=X(g) as functions X(b)->X(a).
This is a congruence because X is a functor. Conditions I and IV descend:
lift representatives of a span or parallel pair to A, use the required
commutative square or integral affine equality there, then pass to the
quotient. Hence A_X is quasi-filtered. For each fixed object a,

    |A_X(a,b)| <= |X(a)|^{|X(b)|} <= |X(a)|^N

for every b. Isbell--Mitchell (1976), Proposition 4.5, therefore says
that every finite family of parallel arrows out of a is equalized by an
ordinary arrow. Connectedness and I supply common successors, so A_X is
filtered. The diagram X factors through A_X^op, and its strict limit is
unchanged by identifying arrows on which X already agrees.

Finally a contravariant diagram of nonempty compact spaces over a filtered
category has a nonempty inverse limit. For any finite family of its
compatibility equations, filteredness supplies a genuine cocone on the
finite indexing diagram; any point at its vertex yields a solution of
those finitely many equations. The closed compatibility conditions in
the product therefore have the finite intersection property. Compactness
proves the assertion. QED.

The uniform cardinality bound is material to this proof. For general
finite-valued X, the quantity |X(a)|^{|X(b)|} need not be bounded as b
varies. No bound follows from finiteness of the individual values.
Thus a finite-valued obstruction to CL for a quasi-filtered category
must have unbounded fibre cardinalities. This observation does not rule
out the bad-colouring diagrams of section 2, whose cardinalities can
grow with the relevant hom-sets.

## 5. Why the Boolean-algebra shortcut is unfinished

For a Stone-space diagram X, its clopen Boolean algebras form a covariant
diagram B(a)=Clop(X(a)). A nonempty inverse limit amounts to a nontrivial
Boolean-algebra colimit admitting an ultrafilter. Quasi-filteredness and
the fixed-point property constrain the complement involution on the
underlying A-set of B: no connected component can be invariant under a
fixed-point-free complement involution. This does not identify the set
colimit with the Boolean-algebra colimit. Boolean multiplication can
create further identifications after the set-colimit relations have
been imposed. The missing step is exactly such a compatibility argument,
not an application of compactness by itself.

Likewise, affine equalizers can construct signed finite measures of total
mass one satisfying a prescribed finite family of linear compatibility
equations. Negative coefficients prevent an inference that a compatible
point exists. A proof using probabilities would require an additional
positivity argument not supplied by integral affine equalizers.

### A precise obstruction to pinning Boolean coefficients

Passing to a category of elements to hold an arbitrary multiplicative
coefficient fixed does not preserve the needed colimit relation. This
fails even for the exact, total category Delta_inj. Let B(n) be the free
Boolean algebra on generators x_0,...,x_(n-1), and let injections rename
the generators. Its maps are injective unital Boolean homomorphisms:
their maps on finite valuation spaces are surjections. In B(2), x_0 and
x_1 are the two images of the sole generator in B(1), so their underlying
set-colimit classes are equal. Set c=x_0. The tuples (c,x_0) and (c,x_1)
are in different components of El_A(UB x UB), because equality of their
two coordinates is preserved and reflected by every transition, and it
holds for only the first tuple.

One can also see that the original relation is lost in the abelian
colimit after this reindexing. The component E of El_A UB containing a
generator consists precisely of (n,x_j): an injective renaming cannot
turn a nongenerator Boolean expression into a generator. At (n,x_j),
evaluate Boolean expressions at the assignment x_j=1 and x_i=0 for
i != j. These evaluations form a natural additive map B|E -> F_2,
because any arrow of E preserves the designated generator. At
(2,x_0), the evaluations of x_0 and x_1 are 1 and 0. Therefore those
elements have different abelian-colimit classes over E as well.

The typing obstruction is that the old incoming maps witnessing
x_0~x_1 need not lift to maps with the chosen coefficient tuple. In a
finite Boolean-ring certificate, affine postcomposition leaves terms
B(g)(c_i) multiplying the relation values, and these coefficients vary
with the support arrow g. Reindexing through their category of elements
would make them constant only at the cost of the unproved lifted tuple
relations just refuted in general. A special argument using the whole
certificate is not ruled out, but it has not been supplied here.

## 6. Literature check and status

A finite local test illustrates the signed-measure issue. Let T be the
proper three-colourings of the five-cycle, written as strings of length
five in cyclic vertex order. The signed combination

    (01012) + (20210) - (21210) + (10202)
            - (10212) + (12010) - (12012)

has augmentation one and all five vertex marginals equal to the point
mass at colour 0. Every summand is a proper colouring, and there is no
constant proper colouring. The three differences alter just vertices
1, 3, and 4, respectively, changing their marginal in the initial
colouring 01012 to colour 0. Thus even simultaneous integral balancing
of a finite system's entire vertex family does not itself yield a
monochromatic configuration. This is **not** an exact-category
counterexample: one would still have to complete the finite constraint
system to a category satisfying all exactness conditions while
preserving its bad colourings, and no such completion is proved here.

The program `code/main_coloring_cycles.py` and its output verify this
certificate and use exact integer Hermite normal form to compute the
augmentation subgroup for all proper three-colourings of cycles of
length 3 through 9. The generators are 3 for length 3 and 1 for lengths
4 through 9. Those enumerations are finite exploratory data only.

Searches for exact colimits together with Ramsey/fixed compact-point
terminology did not locate an opened primary source settling CL for
total or exact categories. The search surfaced Nguyen Van The's
*Fixed points in compactifications and combinatorial counterparts*
(Annales Henri Lebesgue 2, 2019, 149--185; DOI 10.5802/ahl.16), whose
abstract describes the Ramsey/extreme-amenability correspondence for
topological groups. Its article body was not opened in this subtask,
and none of its theorems is invoked in the proofs above. The category
theoretic equivalence in section 2 is proved directly, without claiming
priority. The bounded-fibre result invokes only the opened
Isbell--Mitchell 1976 Proposition 4.5 already audited in the main work.

**Unresolved:** total => CL/FPR; exact => CL/FPR or a counterexample;
total => integral exactness; the rational and prime-field variants.
