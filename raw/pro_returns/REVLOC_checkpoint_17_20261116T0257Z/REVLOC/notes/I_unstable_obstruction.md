# D.2.12: a nonlinear obstruction for the suspended stabilization unit

**Status:** proved for every integer r >= 1 at p = 2. The full proof is in `sections/D2_unstable_obstruction.tex`.

**Attribution:** GPT-6 Astra (OpenAI / ChatGPT Pro). The original odd-r calculation, its even-r extension, and the shorter uniform proof were developed collaboratively by the simple_higher, axioms_derivators and root agents. No human priority is claimed.

## Exact conclusion

Put B = K(F2,2), X = Sigma^r B, A_r = QX, n = r+2. Every map Sigma A_r -> Sigma X is zero on H_(n+1)(-;F2). Therefore Sigma(X -> QX) has no homotopy retraction, and the stable counit projection cannot be represented as such an ordinary map.

This does **not** prove that Map(A_r,Sigma X) is contractible. It does **not** evaluate P_(A_r)(Sigma X). A transfinite nullification may alter later mapping obstructions; the proof only constrains the bottom homology map of individual maps from one suspension.

## Uniform proof and the decisive coefficient

Serre gives H2(B)=<u>, H3(B)=<v=Sq1u>, H4(B)=<u^2>, H5(B)=<uv,w=Sq2v>. In V=H~_*(X), let a,b,d be dual to the suspended u,v,w, with d zero on suspended uv. Then their degrees are n,n+1,n+3 and

    Sq1_* b = a, Sq2_* b = 0, Sq1_* d = 0, Sq2_* d = b.

Every c in V_(n+2) satisfies Sq1_*c=0: its image is a multiple of b, while applying Sq1_* again is zero and Sq1_*b=a is nonzero.

The James model gives H_*(Omega Sigma X)=T(V), and V is primitive because r>=1. Operations preserve word length and satisfy Cartan. The unit X -> A_r gives primitive barred versions of a,b,d in the homotopy-commutative source, so

    Sq2_*(bar b bar d) = bar b^2,
    Sq1_*(bar b^2) = bar a bar b + bar b bar a = 0.

For an arbitrary map f:A_r -> Omega Sigma X that hits the bottom class, f(bar a)=a and f(bar b)=b. No H-map assumption is made. Let lambda extract b on V, mu=lambda Sq2_*, t=ell1 f(bar d), and z=ell2 f(bar b bar d). Then mu(t)=1 and lambda Sq1_*=0. Diagonal naturality says

    z + swap(z) = b tensor t + t tensor b.

Apply lambda tensor mu. The result is 1. By Cartan this is exactly the bb coefficient of Sq2_* z, and hence of ell2 f(bar b^2).

But length-two words of degree 2n+2 are only bb and a c,c a with c in V_(n+2). Under Sq1_*, only bb contributes ab+ba; the other words contribute zero. Thus Sq1_* f(bar b^2) has a nonzero length-two component, contrary to source commutativity and naturality.

At n=3, f(bar d) can include aa. This causes no difficulty: ell1 removes it, and it does not contribute to the length-(1,1) projection of the displayed diagonal equation. No degree restriction is silently imposed on f(bar b bar d); any higher word lengths are discarded by the projection and cannot mix with length two under Steenrod operations.

The root and axioms agents independently reviewed this uniform argument. Both explicitly checked the n=3 issue and the absence of an H-map assumption. The proof supersedes the odd-r-only version below.

## Original odd-r proof, checked independently

When r is odd, n is odd. In source homology Sq1_*(bar a bar b)=bar a^2. Diagonal naturality forces the aa coefficient in f(bar a^2) to be 1: the ab and ba coefficients in f(bar a bar b) must sum to 1.

On the other hand, Q^(n+1)(bar a) is primitive. This follows from the diagonal Cartan formula and Q^s(1)=0 for s>0. The Nishida relation gives

    Sq1_* Q^(n+1)(bar a) = n Q^n(bar a) = bar a^2.

Its image must be primitive in degree 2n+1 of T(V). In that degree a primitive is a length-one class plus a multiple of ab+ba, because 2n+1<3n. Applying Sq1_* to such a primitive has aa coefficient zero, contradicting the preceding forced coefficient.

This proof uses no commutation of f with Dyer--Lashof operations: Q^(n+1)(bar a) is an element chosen in the source, and only diagonal and Steenrod naturality are applied to f. The Nishida coefficient vanishes for even n, so this original argument alone did not cover even r. The uniform proof above uses the b,d block and source commutativity instead.

## Opened primary sources and exact loci

1. Jean-Pierre Serre, *Cohomologie modulo 2 des complexes d'Eilenberg--MacLane*, Comment. Math. Helv. 27 (1953), 198--232.

   https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf

   Section 2 no.8, Theorem 2 and its induction/transgression proof, printed pp.203--204; no.9 on p.204 explicitly lists u2, Sq1u2, Sq2Sq1u2, etc. Section 1 nos.2.1--2.6, p.199, gives naturality, suspension compatibility, Cartan and the Bockstein; Section 4 no.32.2, p.224, contains Sq1Sq1=0. Both this agent and axioms_derivators opened the source; the latter also visually checked p.204. Root independently reviewed the derived low-degree table.

2. I. M. James, *Reduced product spaces*, Ann. Math. (2) 62 (1955), 170--197.

   https://webhomes.maths.ed.ac.uk/~v1ranick/papers/jamesred.pdf

   Section 3, pp.178--180, especially Theorems 3.1--3.6, the cone contraction/Mayer--Vietoris proof, and the multiplication recursion (3.3)--(3.4). Theorem 5.6 and Corollary 5.7, with proof pp.183--187, identify the reduced product with the suspension loop space; Lemma 5.5 identifies the one-letter multiplication, and its construction/proof is in Section 7, pp.189--193. These proofs were opened and read. The same field-coefficient argument has no Tor terms and gives the tensor algebra, with product concatenation. Naturality of the one-letter inclusion and Cartan give the coalgebra/Steenrod assertions directly. James's countability hypothesis is satisfied by the standard countable CW model of the finite-group Eilenberg--MacLane space and its finite suspensions.

3. F. R. Cohen, T. J. Lada and J. P. May, *The Homology of Iterated Loop Spaces*, Lecture Notes in Mathematics 533, Springer (1976).

   https://www.math.uchicago.edu/~may/BOOKS/homo_iter.pdf

   Chapter I, Theorem 1.1(4)--(6),(9), printed pp.5--6; proof pp.7--9. The exact page 6 scan was rendered and checked: the diagonal Cartan formula and beta Q^s=(s-1)Q^(s-1) at p=2 appear explicitly. Unit and top operation formulas are on p.5. These justify the original odd-r alternative; they are not required for the stronger uniform proof. The author-hosted 15.5 MB original is downloaded under `notes/I_sources/`, excluded from distributable originals. Publisher metadata was opened at https://link.springer.com/book/10.1007/BFb0080464.

## Remaining problem

The direct stable-retraction route to ordinary nullification collapse is now obstructed in every positive suspension degree at the prime 2. There may still be different maps, higher suspensions, or successive nullification attachments that kill the target. Neither inequality nor equality of the reversible classes is established by D.2.12.

## Added first-cone corollary (14:53 UTC)

The axioms agent supplied, wrote, and independently checked the following extension; this agent checked every step, including the integral universal-coefficient argument. Root requested its integration.

For every k>=0, every map h:Sigma^k A_r -> Y=Sigma^(r+1)B is zero in mod-two target homology degrees n+1,n+2,n+3. In degree n+4 its image is contained in the line dual to the suspended class uv. No map hitting this last line is constructed.

For k=0, restrict h along X=Sigma^r B -> QX, an isomorphism on H_(n+1) by Freudenthal because n>=3. A bottom hit would induce j*(sigma^(r+1)u)=sigma^r v. Applying Sq2 forces j*(sigma^(r+1)u²)=sigma^r w. Applying Sq1 contradicts Sq1(u²)=0 and Sq1(w)=Sq1 Sq2(v)=Sq3(v)=v²!=0. The k=1 case is the main proof and k>=2 follows from connectivity.

The homology identities Sq1_* b_Y=a_Y and Sq2_* c_Y=a_Y propagate bottom vanishing to the next two degrees. In degree n+4, Sq2_* detects the w-dual coefficient, leaving only the uv-dual line.

Therefore the cofiber of h preserves the first three mod-two homology groups of Y injectively. The same holds for any small wedge of such maps, including the first simultaneous cone attachment on every homotopy class of maps from every Sigma^k A_r. The integral bottom group is Z/2, and its map into the cofiber is also injective: reduction to mod-two homology detects every nonzero image into that group. No higher integral claim is made.

The altered cofiber is not known to retain the Steenrod/Hopf-algebra properties used in the obstruction. Thus this is a first-stage result only and gives no induction through the nullification tower.
