# The suspension-of-a-groupoid example: full fixed-type contraction

Let G be any small groupoid. Form M by adjoining two objects a,b, with no arrows between them, no arrows from G to either, and exactly one arrow from a and exactly one arrow from b to each object of G. The arrows inside G are unchanged. Composition with arrows from a or b is forced by uniqueness. Mark the full cone C={b}*G and the identity of a. Thus Σ contains all objects and is composition-closed.

For every small category X there is a canonical bijection

    Hom_{M^X[Σ_X^{-1}]}(a_X,b_X) = π₀ Fun(X,G).

In particular this functor inverts W∞ for every G. Its localization mapping space is BG. Taking G=BC₂ gives a connected invariant example with nonzero π₁ of its mapping space.

Here is the proof, including arbitrary mixed-valued intermediate diagrams. Write Fτ=Fτ(a,b) with arbitrary vertical arrows and fixed endpoints. A word τ admits such a path exactly when some positive edge precedes some negative edge. In every such path c, the first departure from a is a positive edge into G. Write k(c) for the first vertex in G, and l(c) for the first vertex equal to b. The vertices k(c),...,l(c)−1 all lie in G; call this the first G interval. The first arrival at b uses a negative edge b→G. The path never returns to a: no arrow joins a and b, and the only incident nonidentity arrows at a are outgoing positive arrows into G. After its first arrival at b it lies in the cone C, with possible further b/G alternations.

The assertion that the path never returns to a uses the marking: a forward return would require a nonexistent arrow G→a, and a backward return would require a marked arrow a→G, which Σ excludes. The same reasoning excludes a return from b.

For a vertical transformation η:c→d fixing endpoints, k(d)≤k(c) and l(d)≥l(c). Indeed, at a vertex where c lies in G, its image under η must still lie in G, and at a vertex where c=a it cannot map to b. It follows that the first G interval of d contains that of c.

Define Eτ(c)=c(k(c)). Between any two vertices in a G interval there is a unique specified transport: compose the path arrows in traversal order, inverting those whose orientation is opposite to traversal. For η:c→d, define Eτ(η) as η at k(c), followed by transport in d from k(c) to k(d). Naturality of η on the G interval shows that transporting first in c or last in d gives the same arrow. Applying this equality to a composite of two transformations proves Eτ(θη)=Eτ(θ)Eτ(η). Thus Eτ is a genuine functor Fτ→G.

Define Uτ(c) to agree with c before l(c), and to be constantly b from l(c) on. The edge entering b retains its original arrow. All later edges become identities. Define Uτ(η) by η before l(c), and by the unique arrow b→Uτ(d)(j) thereafter. These arrows exist because Uτ(d)(j) is b or an object of G. The required squares either are the original naturality squares or are forced by uniqueness of arrows out of b. Hence Uτ is a functor. There is a natural transformation Uτ⇒id, whose components are identity before l(c) and the unique arrows b→c(j) thereafter.

Fix k₀ equal to the index of the first positive edge of τ and l₀ equal to the index of its last negative edge. The existence condition gives k₀<l₀. Define a section sτ:G→Fτ by a before k₀, the constant value g from k₀ through l₀−1, and b from l₀ onward. Entrance and exit use the unique cone arrows and all internal arrows are identities. On arrows of G use that arrow throughout the middle interval and identity at a,b. Then Eτsτ=id_G literally.

There is a natural transformation Uτ⇒sτEτ. At a vertex belonging to c's first G interval use transport from c(j) back to c(k(c)); on the additional middle vertices of sτEτ use the unique arrows a→Eτ(c) or b→Eτ(c); outside the middle interval use the identity. The inequalities k₀≤k(c)<l(c)≤l₀ guarantee these are all cases. The only nontrivial squares within G are the transport equations. The remaining squares follow from uniqueness of the cone arrows. Naturality in η follows from the definition of Eτ(η). Consequently

    id_Fτ ← Uτ → sτEτ,    Eτsτ=id_G.

These are explicit inverse maps in Cat_hot, for every admissible τ. Applying Fun(X,−) retains both natural transformations for every small X, so π₀Fun(X,Fτ)→π₀Fun(X,G) is a bijection with no finiteness condition on X.

For a type map u:τ→σ between admissible words, the first G interval of the pulled-back path d u meets the first G interval of d. A source edge cannot skip the complete first G interval: such a skip would pass both the positive entrance edge and the negative exit edge, whereas the image of a single source edge must have one sign throughout. It also cannot skip the first b separating that interval from the next G interval, for the same reason. Thus the two functors Eτu* and Eσ are connected by the specified transport inside the first G interval of d. This is a natural isomorphism; for successive type maps these isomorphisms compose by the transport identity. It follows that all transition maps of every sufficiently late cofinal sequence become the identity on π₀Fun(X,G) under these identifications.

The ind-path formula C.20/D.K5 now gives the displayed all-X bijection. It sends g:X→G to the roof a_X→g←b_X, so it is canonical and natural in X. Alternatively the preceding contractions explicitly reduce each finite localization word in M^X to such a roof and identify all ladder relations; mixed-valued intermediate X-diagrams have been included because Fτ and Fun(X,Fτ) were treated without restricting their vertices to constants.

The same coherent system of Eτ identifies the homotopy colimit of any cofinal path sequence with BG. By C.3 and C.7 this is precisely Map_{L(M,Σ)}(a,b). The map sends the roof a→g←b to its composite in the localization. Since Fun(X,G) depends only on Π₁X, the asserted invariance follows, including for G=BC₂.
