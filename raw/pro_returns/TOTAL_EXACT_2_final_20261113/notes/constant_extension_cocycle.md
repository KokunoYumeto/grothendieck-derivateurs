# The additive obstruction after the constant-group covering has split

AI-produced by GPT-6 Astra (OpenAI), 13 November 2026.
This is a precise H2-level reformulation of the attempted covering
argument. It supplies no proof that the obstruction vanishes for a
total category.

Let A be nonempty, connected, and quasi-filtered. Put T=R/Z, regarded
as an abelian group. Consider an extension of covariant modules

    0 -> constant T -> E -> M -> 0.

## 1. A natural set section exists already under quasi-filteredness

The functor El_A E -> El_A M is a covering of categories. Above any
element m in M(a), its objects form a T-torsor. An arrow f:a->b gives
a T-equivariant map between the torsors over m and M(f)m. Such a map
is bijective, because the action of the constant T is unchanged.
Consequently arrows lift uniquely both forward and backward once
one endpoint lift is specified.

Every component of El_A M is simply connected under quasi-filteredness.
Thus this covering is trivial on each component. Choose one lift in
each component and extend by path lifting. This gives a natural map
of A-sets s:UM->UE with projection composed with s equal to identity.
On the component containing the zero section choose the zero lift;
then s_a(0)=0 for every a. Other choices differ by a natural function
UM->constant T, with no additivity assertion.

This step uses only pi_1 of categories of elements. Higher homology
vanishing supplied by totality has not yet entered.

## 2. The defect is a natural symmetric two-cocycle

Define

    c_a(x,y)=s_a(x)+s_a(y)-s_a(x+y) in T.

It is natural as a map of A-sets UM x UM -> constant T. It is
normalized, symmetric, and satisfies

    c_a(x,y)+c_a(x+y,z)=c_a(y,z)+c_a(x,y+z).

Every identity follows by expanding the four occurrences of s.
Conversely, a natural normalized symmetric function satisfying this
identity defines an extension with underlying A-set T x UM by

    (u,x)+(v,y)=(u+v+c_a(x,y),x+y),
    E(f)(u,x)=(u,M(f)x).

Associativity is the displayed cocycle identity, commutativity is
symmetry, the identity is (0,0), and inverses exist by the same
formula. The constants T form the kernel and the quotient is M.

To make s additive one needs a *natural* function f:UM->constant T,
f(0)=0, with

    c_a(x,y)=f_a(x)+f_a(y)-f_a(x+y).

Then s-f is a splitting in Ab^A. Each individual c_a is such a
coboundary, since T is injective and the extension at a splits as
abelian groups. Objectwise choices of these f_a need not be natural.

## 3. Where the cohomology class lives

Form the reduced simplicial set

    K_n = colim_A^Set U(M^n),

using the usual bar faces (addition of adjacent coordinates, and
deletion of end coordinates) and degeneracies (insertion of zero).
These maps are natural before taking colimits, so K is genuinely a
simplicial set. Nonempty connectedness of A makes K_0 a singleton.

The natural cocycle c factors through K_2 and defines a normalized
degree-two simplicial cohomology class [c] in H^2(K;T). A normalized
one-cochain on K is exactly a natural set-valued function f as above.
Therefore [c]=0 if and only if the extension splits additively in
Ab^A. Choices of the set section s change c by such a coboundary.
The extension classes are precisely the classes admitting these
normalized symmetric representatives; the construction in section 2
provides the inverse construction. In particular their map into
ordinary H^2(K;T) is injective.

This explicitly identifies the typing issue in the attempted proof:
[c] is a cohomology class in the *simplicial bar direction* after
taking set colimits. It is not an H2 class of El_A(M^n) for one fixed
n. Vanishing H2 of all those individual element categories does not
directly say that [c] vanishes.

## 4. Relation with the derived-colimit obstruction

For every abelian diagram M, projective resolution and the adjunction
colim_A left adjoint to constant diagrams give

    Ext^i_(Ab^A)(M, constant T)
        = Hom_Z(T_i(M), T).

Indeed apply Hom(-,constant T) to a projective resolution P_* of M.
Its cochain complex is exactly Hom_Z(colim_A P_*,T). Injectivity of T
identifies its cohomology with Hom of the homology of colim_A P_*.
No assumption that constant T itself is injective in Ab^A is made.
The latter would already amount to the desired exactness condition.

Thus vanishing of the above natural symmetric two-cocycle obstruction
for every M is equivalent to exactness, because T is an injective
cogenerator and hence detects a nonzero T_1(M).

Under totality there is also a useful double-complex description.
At bar degree n, the horizontal A-chain complex is the normalized
chain complex computing T_i(Z[U(M^n)]). Totality makes its positive
homology vanish. The horizontal-first spectral sequence therefore
reduces to the ordinary chain complex Z[K_*]. This is exactly how
totality identifies K with the homotopy colimit of the spaces B M(a).

In the other spectral sequence, the E2 term is

    E2_(p,q)=T_p(H_q(BM(-);Z)).

The term E2_(1,1)=T_1(M) survives in total degree two when A is total:
there are no outgoing differentials because their first index is
negative, and the only possible incoming differential comes from
T_3(constant Z), which vanishes. It is the quotient of the degree-two
homology filtration after the contribution from colim H_2(BM(a)).
An objectwise split extension gives a class that vanishes on that
pointwise contribution, leaving exactly its character on T_1(M).

Both spectral sequences describe the same obstruction. Collapsing
the A-direction by the acyclicity of permutation modules does not
make the surviving T_1(M) term vanish; it moves the problem into the
bar-direction cohomology of K. An additional argument about these
symmetric cocycles is required.

## 5. Why individual graph models do not close this argument

One might try to use the fact that certain diagrams of free groups
have objectwise one-dimensional classifying spaces. The missing
requirement is a *natural diagram of one-dimensional simplicial
models*, with natural objectwise weak equivalences to the classifying
space diagram. Choosing free bases or graph collapses separately at
each object does not provide it.

The AKR column-module counterexample makes this warning concrete:
its groups can be chosen free with free-factor transition embeddings,
yet their abelianizations have nonzero T_1. The nerve BG is a natural
simplicial model, but is not one-dimensional. Relative free-factor
decompositions or collapses need not be compatible with all arrows.
Producing compatible one-dimensional models would be a substantive
new theorem, not an automatic use of the objectwise freeness.

## Status

The genuinely total-specific missing statement is now explicit:
prove that every natural symmetric two-cocycle above is a natural
coboundary when all components of all El_A H are acyclic. No such
proof or counterexample is supplied here. The note explains why
the simpler constant-group covering split and the individual
H2(El_A M^n)=0 statements do not already establish it.
