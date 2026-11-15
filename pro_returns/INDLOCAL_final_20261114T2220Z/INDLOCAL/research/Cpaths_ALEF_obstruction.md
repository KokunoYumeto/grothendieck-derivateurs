# Exact local embeddings and the Higman image obstruction

Author: C/path collaborator. Written 2026-11-14.

Status: proved, with every presentation map displayed below. This note supplements the frozen A.10 and A.28 statements. No approximate relation is replaced by an exact relation.

## 1. The finite set that produces an actual presentation map

Fix a class `C` of groups. A group `T` is **locally embeddable in C** when, for every finite subset `S` of `T`, there are a group `D` in `C` and an injective map `phi:S -> D` such that

    phi(s t) = phi(s) phi(t) whenever s,t,s t all belong to S.

LEF is the case in which `C` is the class of finite groups. Neither `S` nor its image is required to be a subgroup.

Let

    P = <x_1,...,x_m | r_1,...,r_k>

be a specified finite presentation, and let `q:P -> T` be a homomorphism. Fix an element `g` of `P` and a word `u` in the letters `x_i^{±1}` representing it. Suppose `q(g) != 1`. We construct a group `D` in `C` and a homomorphism `v:P -> D` with `v(g) != 1`.

For each word `w` in the finite list `r_1,...,r_k,u`, write

    w = z_1 ... z_l,        z_j in {x_1^{±1},...,x_m^{±1}},
    p_{w,0} = 1,
    p_{w,j} = q(z_1 ... z_j) for 1 <= j <= l.

Here `q(z_j)` means the value of that generator letter in `T`; the formula is evaluated through the free-group presentation map. Define the following explicit finite subset of `T`:

    S = {1}
        union {q(x_i),q(x_i)^{-1} : 1 <= i <= m}
        union {p_{w,j} : w in {r_1,...,r_k,u}, 0 <= j <= length(w)}.

Choose an exact partial embedding `phi:S -> D` supplied by local embeddability. Since `1,1,1` occur in `S`, one has `phi(1)=phi(1)^2`, hence `phi(1)=1`. For every `i`, all three elements

    q(x_i), q(x_i)^{-1}, q(x_i) q(x_i)^{-1}=1

belong to `S`. Consequently `phi(q(x_i)^{-1})=phi(q(x_i))^{-1}`.

The assignment

    x_i |-> phi(q(x_i))

defines a unique homomorphism `v_free:F(x_1,...,x_m) -> D`. For every prefix in the chosen list, its final-letter multiplication is a multiplication whose two factors and product are in `S`:

    p_{w,j-1} q(z_j) = p_{w,j}.

Induction on `j`, using inverse preservation for negative generator letters, therefore gives the exact equality

    v_free(z_1 ... z_j) = phi(p_{w,j}).

In particular, `v_free(r_i)=phi(q(r_i))=phi(1)=1` for every defining relator. Thus the normal closure of the `r_i` lies in `ker(v_free)`. The universal property of the presented group gives an actual, uniquely determined homomorphism

    v:P -> D,       v([w])=v_free(w).

For the selected element it satisfies

    v(g)=phi(q(g)) != phi(1)=1,

by injectivity of `phi` on `S`. This proves the finite-presentation transfer: every nontrivial homomorphism from a finitely presented group to a group locally embeddable in `C` is detected by a nontrivial homomorphism to one member of `C`. No finite presentability of the image `q(P)` is assumed.

## 2. The Higman group and the finite-target calculation

Use the specified finitely presented group

    J = <a,b,c,d | a^{-1}ba=b^2, b^{-1}cb=c^2,
                       c^{-1}dc=d^2, d^{-1}ad=a^2>.

We recall the complete finite-order calculation, so the present note has no dependence on a simplicity assertion about `J`. Suppose a homomorphism from `J` sends its four displayed generators to elements of finite order. If one image is nonidentity, choose the smallest prime `p` dividing any of those four nonidentity orders, and choose a corresponding image `x`. Let `y` be the preceding generator image, so

    y^{-1} x y = x^2.

Conjugacy implies that `x` and `x^2` have the same order, so the order of `x` is odd. Iterating the equality for the finite order `m` of `y` gives `x=x^{2^m}`. Consequently `2^m=1` modulo `p`, and the multiplicative order of `2` modulo `p` divides `m`. That multiplicative order is greater than one and divides `p-1`; it has a prime divisor smaller than `p`. This smaller prime divides the order of `y`, contrary to the choice of `p`.

It follows that every homomorphism `J -> D` is trivial whenever `D` is a torsion group; finite groups are included. Apply Section 1 with `P=J`. Every homomorphism from `J` to a group locally embeddable in torsion groups is trivial. In particular,

    Hom(J,T) consists only of the trivial map for every LEF group T.

This statement concerns all homomorphisms. It does not merely rule out an injective copy of `J` in `T`.

## 3. The linear-target version

The direct matrix calculation in A.28 proves that every homomorphism

    J -> GL_d(F)

is trivial, for every field `F` and positive finite `d`. Here is the calculation again. Over an algebraic closure of `F`, conjugacy of each generator matrix `x` to `x^2` makes squaring permute its finite multiset of nonzero eigenvalues. Each eigenvalue is therefore a root of unity. In positive characteristic a suitable power of `x` is unipotent, and a further power of the characteristic is the identity. Thus all four generator images have finite order, and Section 2 applies.

In characteristic zero, choose positive integers `L,m` so that `x^L` and `y^m` are unipotent, where `y^{-1}xy=x^2`. The finite nilpotent logarithm `v=log(x^L)` obeys

    Ad(y^{-m})(v) = 2^m v.

Conjugation by the unipotent matrix `y^{-m}` is a unipotent operator on the matrix algebra: left multiplication by `y^{-m}` and right multiplication by `y^m` are commuting unipotent operators, and their product is unipotent. Its only eigenvalue is `1`. Since `2^m != 1` in characteristic zero, the displayed equation forces `v=0`, and the inverse finite exponential identity gives `x^L=1`. Section 2 again kills all four images.

Consequently Section 1 also proves that every homomorphism from `J` to a group locally embeddable in finite-dimensional linear groups is trivial. The partial embedding may use a different field and dimension for each finite subset. This conclusion is proved by the presentation map of Section 1, without an assumption of one global linear representation.

## 4. Propagation through the actual A.10 and A.28 homomorphisms

For the actual A.10 resolution over `S^2`, write its group as `H` and the homomorphisms from the inserted Higman groups as

    j_lambda:J -> H.

The normal-generation computation in the proof of A.10 states exactly

    H = normal_closure_H(union_lambda image(j_lambda)).

Indeed killing these images gives precisely `pi_1(S^2)=1`. Let `i:H -> G` be the displayed injective homomorphism in the A.28 construction. Its proved normal-generation property states

    G = normal_closure_G(image(i)).

Now let `q:G -> T` be any homomorphism, where `T` is locally embeddable in torsion groups or locally embeddable in finite-dimensional linear groups. For every `lambda`, the composite

    J --j_lambda--> H --i--> G --q--> T

is trivial by Sections 2 or 3. The normal subgroup `ker(q i)` of `H` contains every `image(j_lambda)`, and therefore it is all of `H`. Thus `q i` is the trivial map. The normal subgroup `ker(q)` of `G` now contains `image(i)` and hence is all of `G`. This proves the actual conclusion

    every homomorphism G -> T is trivial.

In particular the A.28 group over `S^2` has no nontrivial images in any LEF group, with no cardinality restriction on the target. The same calculation already applies to the initial A.10 group `H`.

## 5. Locally residually finite targets, with explicit partial embeddings

Suppose every finitely generated subgroup of `T` is residually finite. Given a finite subset `S` of `T`, put `S'=S union {1}` and `K=<S'>`. For every ordered pair of distinct elements `a,b` of `S'`, residual finiteness supplies a finite group `D_{a,b}` and a homomorphism

    rho_{a,b}:K -> D_{a,b}

with `rho_{a,b}(a^{-1}b) != 1`. Take the finite direct product

    D = product_{a,b in S', a != b} D_{a,b}

and the homomorphism `rho:K -> D` with these components; an empty direct product means the trivial group. Its restriction to `S'`, and hence to `S`, is injective, since the `(a,b)` component separates any selected distinct pair. It preserves every multiplication in `S`, being the restriction of a homomorphism. When `S'={1}` the empty product gives precisely the required map. Thus `T` is LEF, and Section 4 applies.

One can also see this particular image obstruction without a partial embedding: the image of each four-generator `J` lies in a residually finite finitely generated subgroup; a nonidentity element of that image would survive a finite quotient and contradict Section 2.

## 6. Exact limit of the argument

The constructed map `v_free` descends through the specified quotient `F(x_1,...,x_m) -> P` because every `v_free(r_i)` equals the identity in the approximating group. A map with merely small relator errors has not supplied these identities. The exact descent condition is

    normal_closure(r_1,...,r_k) <= ker(v_free).

This note supplies that condition using partial embeddings with exact multiplication. It does not claim that an arbitrary sofic, hyperlinear, or other metric approximation satisfies it. No assertion that all amenable targets or all sofic targets are excluded is made here.

## 7. Internal source and audit record

The two used internal results are the explicit Higman normal-generation computation in `sections/A.tex`, proof of A.10, and the actual inclusion and normal-generation computation in `sections/A_countable_quotients.tex`, proof of A.28. Sections 1–3 and 5 give the complete additional algebraic proofs. No downloaded third-party file is required for this note.
