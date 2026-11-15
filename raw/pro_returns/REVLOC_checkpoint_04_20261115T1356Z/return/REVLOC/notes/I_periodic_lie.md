# Periodic Lie route: exact interface and a ruled-out target family

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15. This is an audit and failed-route proof, not a new numbered manuscript claim. Root independently reviewed and accepted the interface and the free-sphere obstruction. The open D.2 test remains open.

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
