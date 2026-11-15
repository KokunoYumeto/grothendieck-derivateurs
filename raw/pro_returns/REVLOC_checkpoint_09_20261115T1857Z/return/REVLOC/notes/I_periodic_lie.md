# Periodic Lie route: exact interface, joint generation, and exclusion of all K(2)-local targets

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15. This is an audit and failed-route proof, not a new numbered manuscript claim. Root independently reviewed and accepted the interface and the free-sphere obstruction. The final section adds a complete joint-generation proof, independently accepted by root and the axioms agent at 14:12 UTC. It closes the K(2)-local target route; the ordinary D.2 nullification test remains open.

## Question and notation

Fix a prime p. Put B = K(F_p,2), E_r = Sigma^r Sigma-infinity B, and A_r = Omega-infinity E_r = Q Sigma^r B. The active zero-finite-part question is whether

    P_{A_r}(Sigma^{r+1} B)

is noncontractible, equivalently whether the adjacent reversible classes in D.2.9 are strictly different. A possible method would find an A_r-null target receiving an essential map from the indicated suspension of B. Merely distinguishing an abelian spectral Lie algebra from a free one does not do this: a complete derived mapping-space vanishing result is required.

The letter L_n^f below has Heuts's meaning: nullification at a suitable finite type-(n+1) suspension V_{n+1}. It does not mean unstable homological localization at T(0) wedge ... wedge T(n). Those two uses of the same notation occur in different sources and cannot be interchanged.

## Exact ordinary-to-Lie mapping interface

Use the embedding of S_{v_2} in pointed p-local spaces chosen in Heuts, Definition 3.11. Let d_3 be its connectivity parameter; the finite nullifiers may be chosen with d_2 <= d_3. If r+1 >= d_3, then A_r is d_3-connected.

The source has zero rational and v_1-periodic homotopy. Here is a justification that does not assume a height-2 telescope conjecture. The reduced K(1)-homology of B vanishes by Bousfield 1997, Section 10.11. Snaith splitting expresses the suspension spectrum of Q Sigma^r B as a sum of extended powers of E_r. Each is K(1)-acyclic: acyclic spectra form a tensor ideal, and homotopy orbits preserve the acyclicity. Thus A_r is K/p-acyclic, using the usual equality of the K/p and K(1) Bousfield classes at p. Bousfield's Corollary 11.12, applied to the connected H-space A_r, makes its v_1-periodic homotopy zero. Rational triviality follows in the same way, or from its p-primary homotopy groups. Equivalently, one may use Phi_i Omega-infinity = L_{T(i)} and the established height-1 telescope result.

Heuts's Theorem 3.7 at height 1 now gives L_1^f A_r = *. Proposition 3.6 says that L_2^f A_r remains d_3-connected. The identity L_1^f L_2^f = L_1^f, used explicitly in the proof of Lemma 3.12, implies that L_2^f A_r is also L_1^f-acyclic. Hence it belongs to S_{v_2}, and the defining monochromatic functor satisfies

    M A_r = L_2^f A_r.

Every Z in S_{v_2} is L_2^f-local. Therefore ordinary nullification adjunction, followed by fullness of the chosen embedding, gives

    Map_*(A_r,Z) = Map_*(L_2^f A_r,Z)
                = Map_{S_{v_2}}(M A_r,Z).

This is the step that would fail for an arbitrary source: S_{v_2} is generally a colocalization inside L_2^f-local spaces, and M is not an unrestricted reflection from all pointed spaces.

The natural map E_r -> L_{T(2)} E_r induces a v_2-equivalence on its infinite-loop spaces, by the identity Phi Omega-infinity = L_{T(2)} recorded on Heuts p.4. Consequently

    M A_r = Omega-infinity_{T(2)} L_{T(2)} E_r.

Heuts's Theorem 2.6 and the identification on p.8 of Omega-infinity_{T(n)} with the trivial-Lie functor give the exact equivalence

    Map_*(A_r,Z)
       = Map_{Lie(Sp_{T(2)})}
           (triv L_{T(2)} E_r, Phi_Lie Z).                 (1)

For a target F in Lie(Sp_{K(2)}), let Z_F be its corresponding space in M_{K(2)}, viewed as an object of S_{v_2}. Corollary 2.8 and Proposition 4.26 identify the K(2)-local reflection of Lie algebras with K(2)-localization of their underlying spectra. This reflection carries a trivial Lie algebra to the trivial Lie algebra on the localized spectrum. Thus (1) specializes to

    Map_*(A_r,Z_F)
       = Map_{Lie(Sp_{K(2)})}(triv L_{K(2)} E_r,F).        (2)

All these are derived mapping spaces; no replacement by homomorphisms of homotopy Lie algebras has been made.

## Free Lie algebras on localized spheres cannot be separators

Let C = Sp_{K(2)}, let ell be any integer, and set

    F = Free_Lie^C(L_{K(2)} S^ell).

Heuts's Corollary 4.23, with its proof through Theorems 4.13 and 4.22, gives a finite weight decomposition. At height 2 its possibly nonzero weights are at most p^2 for odd ell, and at most 2p^2 for even ell. Applying the symmetric monoidal K(2)-local reflection retains this bound. Weight 1 is L_{K(2)} S^ell and is nonzero. Choose the largest index m whose weight J = F_m is nonzero.

The weight-at-least-m part is a Lie subalgebra: every operation sends a tuple of input weights to their sum. It has just one nonzero underlying weight, J. Each operation of arity at least two lands in weight at least 2m > m and is zero. This is an assertion in the category of graded operadic algebras, so the inherited higher coherences are included; it is not merely a calculation of the binary bracket. Equivalently, replace the contractible higher graded pieces by zero within that graded category. The resulting subalgebra is triv J. We obtain a Lie map

    triv J -> F

whose underlying spectrum map has the weight projection F -> J as a retraction. The projection need not be a Lie map and is used only after forgetting the Lie structure.

Put E = L_{K(2)} E_r. This is a nonzero dualizable object of C, for every r and every prime p. Dualizability follows directly from Hovey--Strickland, Corollary 8.8: B is a connected p-local loop space with finite homotopy groups, nonzero in only one degree. Nonvanishing follows from the Eilenberg--Mac Lane K(n)-homology criterion in Bousfield 1997, Section 10.11, at n = i = 2. That paragraph explicitly includes p = 2 and directs the reader to the additional sources for that prime. Ravenel--Wilson 1980 gives the original explicit finite calculation for odd primes; its introduction restricts to odd p, so it is not by itself cited as a proof for p = 2.

By duality in C,

    Hom_C(E,J) = D_C E tensor_C J.

Both factors have nonzero K(2)-homology. The field Kunneth isomorphism therefore makes this function spectrum nonzero. The next argument is needed to pass from a nonzero spectrum to a noncontractible mapping space; that passage cannot be assumed for a general spectrum.

Every nonzero K(2)-local spectrum U has nonzero homotopy groups in arbitrarily high degrees. Suppose instead that U were bounded above. Choose a finite spectrum V of type 2 with a positive-degree v_2 self-map Sigma^d V -> V, whose existence follows from Hopkins--Smith, Theorem 9. Mapping into the K(2)-local U makes this self-map an equivalence, so Hom(V,U) is d-periodic. It is also bounded above because V is finite. A bounded-above periodic spectrum is zero. But Hom(V,U) = D V smash U, and field Kunneth gives

    K(2)_*(D V smash U)
       = K(2)_*(D V) tensor_{K(2)_*} K(2)_*U != 0,

a contradiction. Apply this to U = Hom_C(E,J). It follows that Map_C(E,J) = Omega-infinity Hom_C(E,J) has nonzero positive homotopy groups.

Now consider

    Map_C(E,J)
       -> Map_{Lie(C)}(triv E,triv J)
       -> Map_{Lie(C)}(triv E,F)
       -> Map_C(E,J).

The first arrow applies the trivial-Lie functor. The second uses the top-weight inclusion. The last forgets Lie structure and then projects to weight m. The composite is the identity. Hence Map_{Lie(C)}(triv E,F) is noncontractible; indeed it has the indicated nonzero positive homotopy groups as retracts.

For r+1 >= d_3, equation (2) proves that Z_F is not A_r-null. The same conclusion holds for every smaller r: choose R >= r with R+1 >= d_3. D.2.9 proves that A_r ordinarily kills A_R by iterated bar constructions. Thus any A_r-null target would be A_R-null, contradicting what was just proved. This rules out all the free K(2)-local Lie algebras on sphere shifts as A_r-null separators, for all r >= 0.

## What remains unresolved

The finite-weight argument applies to free Lie algebras on localized sphere shifts. It has not been proved here for a free Lie algebra on an arbitrary finite type-2 spectrum: its weight decomposition may be unbounded, so a highest nonzero weight need not exist. No claim of vanishing of maps from a trivial Lie algebra to such a free Lie algebra is justified by the words "abelian" and "free", by a rational analogy, or by naive restricted-power operations on homotopy groups. Derived coherences remain part of the problem.

A useful new target would need both a proved vanishing of the full mapping space in (1) or (2) and a nonzero map from the relevant suspension of B. A BZ/p-null target cannot do the latter: B is ordinarily BZ/p-acyclic, as is A_r. Likewise a finite target or an old sphere-null target does not automatically give a new separator. No target satisfying both requirements has been produced.

The exact open calculation is still P_{Q Sigma K(F_p,2)} Sigma^2 K(F_p,2) != *. The interface above makes one proposed route precise; the free-sphere calculation closes a tempting subcase negatively.

## Opened primary sources and exact locations

- Gijs Heuts, *Lie algebras and v_n-periodic spaces*, Annals of Mathematics 193 (2021), 223--301, DOI 10.4007/annals.2021.193.1.3. Opened author/arXiv v2 of 29 October 2020: <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/heuts2.pdf>. Its own page numbers: pp.4--5 (Phi Omega-infinity, Theorems 2.2--2.6); p.8 (trivial-Lie identification); pp.9--15 (Definitions 3.1 and 3.11, Proposition 3.6, Theorem 3.7, Lemma 3.12 and the colocalization proof); pp.17--18 (Proposition 3.19 and Remark 3.20); pp.36--37 (Theorem 4.22 and Corollary 4.23, including the negative-shift duality argument); pp.40--41 (Proposition 4.26 and proof). Corollary 2.8 is on p.6. Beware that its Definition 2.1 is a definition, not the source of the Phi Omega-infinity identity.
- Mark Hovey and Neil P. Strickland, *Morava K-theories and localisation*, Memoirs AMS 139 (1999), no.666, DOI 10.1090/memo/0666. Opened <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/kn.pdf>. Theorem 8.6 and its proof, pp.47--48, give the finite-K-homology dualizability criterion; Corollary 8.8 and proof, p.48, give the exact loop-space application used above. Their prime p is arbitrary.
- A. K. Bousfield, *Homotopical localizations of spaces*, American Journal of Mathematics 119 (1997), 1321--1354. Opened <https://www.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf>. Section 10.11, p.1348, gives the all-prime K(n)-acyclicity criterion; Corollary 11.12, p.1352, supplies the H-space K/p-to-v_1 implication. Section 10.12 also explains the stable-cohomotopy acyclicity of B used elsewhere in this project.
- Douglas C. Ravenel and W. Stephen Wilson, *The Morava K-theories of Eilenberg--Mac Lane spaces and the Conner--Floyd conjecture*, American Journal of Mathematics 102 (1980), 691--748. Opened <https://www.sas.rochester.edu/mth/sites/doug-ravenel/mypapers/emspace.pdf>. Theorem 11.1(a), summarized near p.695 and proved in Section 11, gives the original finite nonzero calculation for odd p. The odd-prime restriction in the introduction was checked. The all-prime conclusion above instead uses the explicitly all-prime statements of Hovey--Strickland and Bousfield.
- Michael J. Hopkins and Jeffrey H. Smith, *Nilpotence and stable homotopy theory II*, Annals of Mathematics 148 (1998), 1--49, DOI 10.2307/120991. Opened <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/HS.pdf>. Definition 8 and Theorem 9, p.4, are the precise positive-degree periodicity input. The PDF has one preliminary JSTOR page, so printed p.4 is PDF page 5.

Additional source checked to prevent a notation error: Barkan--Heuts--Shi, arXiv:2604.10867, Corollary 1.8 and Sections 5.2--5.4, <https://arxiv.org/pdf/2604.10867>. Its L_n^f denotes the indicated homological localization. Its Chevalley--Eilenberg and nilcompletion statements do not by themselves compute the derived Lie mapping space required here.

## Further reduction and the exact unresolved join condition (13:56 UTC)

The source comparison can be strengthened for a target assumed to be A_r-null. Write C_0 = Sigma-infinity B and E_0 = L_{K(2)} C_0. The explicit Ravenel--Wilson formula at n=q=2 and j=1 gives unreduced rank p, hence reduced rank p-1, all in even degrees. The extension of this calculation to p=2 is explicitly recorded in Hopkins--Ravenel--Wilson, *Morava Hopf algebras and spaces K(n)-equivalent to finite Postnikov systems*, Remark 4.4, p.36 of the opened author manuscript <https://www.sas.rochester.edu/mth/sites/doug-ravenel/mypapers/hrw.pdf>. Its Corollary 1.3 also records the even-degree conclusion. Thus the categorical Euler characteristic of E_0 is a K(2)-equivalence of the local unit: on K(2)-homology it is multiplication by p-1. At p=2 one can compute this trace after extension to the commutative Morava E-theory and then reduce modulo the maximal ideal; this avoids assuming that the original K(2) ring spectrum at p=2 is homotopy commutative. Coevaluation followed by evaluation therefore exhibits the K(2)-local unit as a retract of E_0 tensor D E_0.

Let U be any K(2)-local spectrum. Choose N arbitrarily large and put

    V = tau_{>=N}(D E_0 tensor U),
    H = C_0 smash V.

Every bounded-above spectrum is T(2)-acyclic: if W is such a spectrum and T(2) is the telescope of a positive-degree v_2 self-map on a finite type-2 V_2, the groups of the telescope terms Sigma^{-kd}(V_2 smash W) vanish in any fixed degree once k is large. They are therefore also K(2)-acyclic. It follows that L_{K(2)} V = D E_0 tensor U. The spectrum H belongs to I_p, is p-primary, and becomes arbitrarily connective with N. D.2.9 therefore makes Omega-infinity H ordinarily A_r-acyclic. Its lower periodic homotopy vanishes because C_0 is T(0)- and T(1)-acyclic. The high-connectivity argument of (2) applies to H as well as E_r.

Consequently, if Z_F in M_{K(2)} is A_r-null, then

    Map_{Lie(Sp_{K(2)})}(triv(E_0 tensor D E_0 tensor U), F) = *.

The unit retract just constructed makes triv U a retract of the source. Hence

    Map_{Lie(Sp_{K(2)})}(triv U,F) = * for every U.         (3)

This reduces the entire K(2)-periodic-target route to a categorical detection question: are there nonzero spectral Lie algebras right orthogonal to all trivial Lie algebras? It does not answer that question.

A relevant new primary source was obtained in full: Max Blans and Gijs Heuts, *A characterization of the spectral Lie operad*, arXiv:2606.17313v1, 15 June 2026, <https://arxiv.org/html/2606.17313v1> and <https://arxiv.org/pdf/2606.17313>. Corollary 4.8, p.21, proves that cartesian products of spectral Lie algebras preserve weakly contractible colimits separately. Theorem 4.16, p.24, proves universality of these colimits, and Corollary 4.17, p.25, is Mather's second cube lemma. The proof on pp.25--26 was read. These properties pass to K(2)-local Lie algebras: the algebra localization of Heuts Proposition 4.26 is left exact because its underlying spectral localization is exact. The downloaded original and extraction are stored only in notes/I_sources/ for source auditing and exclusion from the deliverable archive.

The tempting next inference is not yet valid. A free Lie algebra on a sphere shift has a finite weight filtration with trivial successive fibres. If the nullification kernel generated by all triv U were closed under fibre/base-to-total extensions, those free Lie algebras would all be killed, and their generation of Lie algebras under colimits would force F=0 in (3). The needed extension closure has not been established merely by the cube theorem.

The exact additional hypothesis appears in David Chataur and Jerome Scherer, *Fibrewise nullification and the cube theorem*, opened <https://arxiv.org/pdf/math/0303062>. Theorems 3.3 and 3.5 of that manuscript require the join axiom, equivalently product preservation by the particular nullification, in addition to the cube axiom. Their Section 4 explicitly does not assert this join axiom for arbitrary operad algebras. (The published version, *Fiberwise localization and the cube theorem*, Commentarii Mathematici Helvetici 81 (2006), 171--189, has expanded numbering 5.3 and 5.5.) For the current family the missing assertion is that

    X * triv U

is nullified by all trivial Lie algebras for every X and U. Closure of the generator family under products triv U times triv V = triv(U direct-sum V) does not give this assertion with arbitrary X.

Two possible shortcuts were checked and do not remove that gap. Hoyois's *Topoi of parametrized objects*, Corollary 5, <https://hoyois.app.uni-regensburg.de/papers/loci.pdf>, requires van Kampen colimits, a stronger descent statement than mere universality. Even after constructing a parametrized topos, internal nullity must not be silently identified with external mapping-space orthogonality. Similarly, Andrew Macpherson's *Fibrations and Koszul duality in locally Cartesian localisations*, Definition 3.9, <https://arxiv.org/pdf/2105.12316>, defines nullification using all product projections X times A -> X. Its locally Cartesian conclusion cannot be applied to localization generated only by A -> 0 without first proving the product condition. The joint-detection question and the original D.2 separator remain unresolved.


## Joint generation by trivial algebras: the action-bar argument (14:12 UTC)

The remaining join question can be bypassed. The following proof uses only finite-product closure of a specifically constructed class and an explicit realization of a fibre sequence. It never assumes that an arbitrary nullification in Lie algebras is a modality or that its kernel is closed under fibre/base-to-total extensions.

### Statement

Let p be a prime and n a finite positive chromatic height. Let V be either Sp_{T(n)} or Sp_{K(n)}, and let L = Lie(V). The smallest replete full class C in L containing every trivial Lie algebra triv(U), U in V, and closed under small colimits and retracts is all of L. Consequently, if Z in L satisfies

    Map_L(triv(U),Z) = * for every U in V,

then Z = 0.

For the application here only n=2 and V=Sp_{K(2)} are needed. The proof of this categorical statement is independent of the Ravenel--Wilson trace calculation used to pass from A_r-nullity to orthogonality to all trivial sources.

### Product preservation after chromatic localization

Blans--Heuts Corollary B gives preservation of weakly contractible colimits by the cartesian product separately in each variable in Lie(Sp). In the downloaded original PDF this is Corollary 4.8; the arXiv v1 HTML inserts an additional Remark 4.8 and numbers the same result Corollary 4.9. The statement and its proof were opened in both formats. Cite Corollary B to avoid this numbering discrepancy.

The same property holds in L. Indeed, the exact symmetric monoidal localization Sp -> V induces a reflective localization of spectral Lie algebras whose underlying-spectrum functor is that spectral localization. One can construct its algebra structure by localizing each operation: the natural maps

    L_E(O(k) smash A^{smash k})
        = L_E(O(k) smash (L_E A)^{smash k}) -> L_E A

supply all the operations and their coherences. The tensor-ideal property of E-acyclic spectra justifies the displayed equivalence. The resulting reflection is left exact, since limits of Lie algebras are created on underlying spectra and stable Bousfield localization is exact. This is the construction used explicitly by Heuts, Proposition 4.26, for the K(n)-local reflection from T(n)-local Lie algebras; the same construction gives the reflection from ordinary spectra.

For a weakly contractible diagram D of local Lie algebras and a local X, apply that left exact reflection to the ordinary equivalence

    X times colim D = colim (X times D).

The localized colimits are the colimits in L, and the reflected products are the products in L. This proves the required property in both variants of V.

### The generated class C is closed under finite products

The zero algebra belongs to C. First fix a trivial algebra A. Let D_A be the class of X such that X times A lies in C. This class contains every trivial algebra, because

    triv(U) times triv(V) = triv(U direct-sum V).

It is closed under retracts. To prove closure under an arbitrary small colimit of objects X_i in D_A, extend the indexing category I to I^{triangleleft} by adjoining an initial vertex, and extend the diagram by the zero algebra at that vertex. The colimit of the extended diagram is still colim_I X_i, including when I is empty. Its indexing category is weakly contractible. Product preservation therefore identifies

    (colim_I X_i) times A
       = colim_{I^{triangleleft}} (X'_i times A).

Every value on the right belongs to C: the new initial value is 0 times A = A, which is in C, and the remaining values do so by the hypothesis on X_i. Hence the colimit belongs to C. This proves D_A contains C.

Now fix any Y in C. Repeat the same argument for the class of X with X times Y in C. It contains every trivial algebra by the preceding paragraph, is closed under retracts, and is closed under arbitrary colimits because the additional initial value is now Y, still in C. Thus C is closed under binary products, and hence under all finite products.

The extra initial vertex is essential. We have not claimed that product preserves arbitrary colimits, or that the product of the extended diagram is the extension of the original product diagram by zero. Its initial value is A or Y, as explicitly used above.

### A fibre sequence is an action-bar realization

Let F -> E -> B be a fibre sequence in L. There is an augmented simplicial Lie algebra with q-simplices

    D_q = F times (Omega B)^q

and augmentation |D_bullet| -> E, and this augmentation is an equivalence. The face maps encode the canonical action of Omega B on F; a product decomposition of the individual simplicial levels does not assert that the action is trivial.

Here is a complete construction and verification. Take the Cech nerve of 0 -> B in L, whose q-th term is the (q+1)-fold fibre product of 0 over B. It is the bar construction of the internal group object Omega B. Its realization is B. To check the last assertion, use the conservative forgetful functor U:L -> V. It preserves finite limits and geometric realizations: the spectral Lie monad preserves sifted colimits, since the localized tensor product preserves colimits separately. Thus the assertion is reduced to the stable category V, where the realization of the bar construction on Omega U(B) is Sigma Omega U(B) = U(B).

Pull the entire augmented Cech nerve back along E -> B. The q-th object is canonically equivalent to F times (Omega B)^q, by the usual finite-limit description of the Cech group action. The augmentation to E becomes an equivalence after applying U. Indeed, in a stable category a geometric realization commutes with finite limits (finite limits are finite colimits), so the realized pullback is

    U(E) times_{U(B)} |U(Cech(0 -> B))| = U(E).

Since U is conservative, |D_bullet| -> E is an equivalence in L. This also shows that no general pushout universality or join axiom is needed for this particular realization.

It follows that

    F in C and Omega B in C  ==>  E in C.                 (4)

Every level F times (Omega B)^q is in C by finite-product closure, and C is closed under the geometric realization. Notice the loop on B in (4). We are not replacing this premise by B in C.

### Finite weight filtrations, with all loops tracked

Let S_V be the unit of V and take any integer ell. Put

    G = Free_Lie^V(S_V^ell).

Heuts, Theorem 4.22 and Corollary 4.23, show that G has its standard positive weight grading and all weights above m=2p^n vanish; for odd ell one can use m=p^n. This includes negative ell. For the K(n)-local variant, apply the symmetric monoidal K(n)-local reflection to the T(n)-local formula.

For each 0 <= j <= m, form the graded quotient G_{<=j} by setting weights above j equal to zero. Positive weight addition makes this an algebra quotient: operations whose total input weight exceeds j have zero output, compatibly with all operadic compositions. There are fibre sequences

    triv(G_j) -> G_{<=j} -> G_{<=j-1},

with G_{<=0}=0. The fibre is trivial as an operadic algebra, including its coherences: all its inputs have weight j, so every operation of arity at least two lands in weight at least 2j>j and hence is zero. One can state this entirely in the category of positively graded algebras before forgetting the grading.

We prove simultaneously, by induction on j, that

    Omega^k G_{<=j} is in C for every integer k >= 0.       (5)

The assertion is immediate for j=0. At stage j, apply Omega^k to the displayed fibre sequence. Its fibre is

    Omega^k triv(G_j) = triv(Sigma^{-k} G_j),

which belongs to C by definition. The loop of its base is Omega^{k+1} G_{<=j-1}, which belongs to C by the induction hypothesis, for this same k. Formula (4) therefore proves Omega^k G_{<=j} belongs to C. This proves (5) for every k without assuming that C is generally closed under loops. At j=m, G_{<=m}=G, so every free Lie algebra on a shift of the localized sphere belongs to C.

### Generation and joint detection

The localized sphere shifts generate V under small colimits: present any spectrum as a colimit of sphere cells and apply the localization. Since the free Lie functor preserves colimits, all free Lie algebras in L lie in C. Finally, every Lie algebra is the geometric realization of its usual free-forgetful monadic bar resolution. Each simplicial term is free, so it lies in C, and therefore every Lie algebra lies in C. This proves C=L.

If Z is orthogonal to all triv(U), the class of X with Map_L(X,Z)=* is closed under colimits and retracts. It therefore contains C=L. Taking X=Z makes the identity map of Z nullhomotopic. In a pointed infinity-category this implies Z=0: the two maps between Z and the zero object are inverse equivalences up to homotopy. This proves joint detection.

### Consequence for the active D.2 route

Apply this with n=2 and V=Sp_{K(2)} to equation (3). Every A_r-null target lying in the fully faithful unstable K(2)-local subcategory M_{K(2)} is contractible. For r below the connectivity cutoff, use the already established ordinary A_r-acyclicity of A_R for sufficiently large R; an A_r-null target is then A_R-null, so the conclusion remains valid.

In particular, choosing a free target on a finite type-2 spectrum with an unbounded weight decomposition does not evade the obstruction. The proof does not truncate that target. Instead, it builds the category from free Lie algebras on sphere shifts, each of which has a finite weight filtration. Likewise the join X * triv(U) is now in C because every Lie algebra is; this is a consequence of joint generation, not an assumed step of the proof.

This rules out the entire K(2)-periodic-target method for separating B from the reversible class generated by A_r. It does not prove that P_{A_r}(Sigma^{r+1}B) is contractible as an ordinary space. A nonzero nullification can have no such periodic local targets, and no passage from this categorical statement to ordinary-space equivalence has been asserted.


The final formal statement is D.2.11 in sections/D2_periodic_lie.tex. Its proof improves the argument above in two ways: it specifies a countable generating set closed under finite products, and at p=2 uses rank-one coevaluation to split the unit, avoiding any commutative Morava-E refinement. The high-connectivity source H is chosen separately for every r, so the ordinary-target exclusion covers all r directly. The root and axioms agent independently checked the action-bar and simultaneous-loop induction.

Final source-interface check: Bousfield1997 Theorem11.3 (p.1350) turns the K(1)-equivalence of connected H-spaces QB→* into a virtual K(1)-equivalence. The paragraph immediately before Theorem11.11 (p.1352) explicitly identifies virtual K(1)- and virtual complex K/p-equivalences; Theorem11.11 then gives v1-triviality. The formal D2.11 proof now cites this exact chain, avoiding an uncited Adams-splitting identification. Opened the statements and proofs. Axioms independently passed the complete ordinary-source reduction and the p=2 rank-one coevaluation argument.
