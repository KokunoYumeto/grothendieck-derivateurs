# A.4: additional uniform-generation attempts after checkpoint 03

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 18 November 2026. These are research notes, not new numbered claims in the manuscript. The equality, third-element, and set-size questions in A.4 remain unresolved. The accepted countable-separator reformulation A4.2 is a recheck of supplied background G.7 and is not counted as new stopping-rule movement.

## 1. Primary completion cannot change a nilpotent example

**Proved route exclusion.** Let p be a prime, X a connected nilpotent space, and eta:X→X_p^ a p-completion. If both X and X_p^ have zero reduced homology with Z[1/p] coefficients, then eta is a weak equivalence. No finite-type hypothesis is needed.

The exact input is Miller, *The Sullivan conjecture on maps from classifying spaces*, Annals of Mathematics 120 (1984), Theorem 1.5, printed p.45. For every connected W with reduced H_*(W;Z[1/p])=0 and every nilpotent fibrant X, completion induces a weak equivalence of based mapping spaces Map_*(W,X)→Map_*(W,X_p^). Apply this first to W=X_p^. Surjectivity on components gives a map r:X_p^→X with eta r homotopic to the identity. Apply it next to W=X. Injectivity on components and eta(r eta)=eta show that r eta is homotopic to the identity. Thus eta has a homotopy inverse.

Consequently one cannot start with a nilpotent example in the lower reversible class, complete it, and obtain a different primary source in the larger sphere-null class. A proposed rational-fibre repair also has to overcome the same mapping-space test; it is not enough merely to observe that completion preserves maps into completed spheres. No result is asserted here for a nonnilpotent source or a p-bad completion.

**Source correction check.** Miller's 1985 corrigendum was opened and read in full, pp.605–609. The odd-prime correction replaces the unstable category U by V in the algebraic input, and the second correction repairs the almost-simplicial resolution used for Fact 3.9. Neither changes Theorem 1.5. At p=2 the original category in Theorem 8.8 is unchanged; the Ext vanishing in that theorem is for all s≥0, as checked on a screenshot of printed p.78. Theorem 8.8 supplies only a sufficient criterion here; no new realized source satisfying it has been constructed.

## 2. The primary Moore-smash reduction was already supplied

For a connected primary source D and the Moore space M=M(F_p,1), the telescope argument gives minRev(D)=minRev(M smash D). The p-fold suspension self-map of Sigma D has contractible telescope; its cofiber is M smash D. If the cofiber is aspherical in a reversible class, the map is an equivalence there, and homotopy-colimit closure makes Sigma D, hence D, aspherical. The opposite inclusion is smash closure.

This argument was independently rediscovered and then located in the supplied REVLOC D.2.39n–q, in `background/REVLOC/sections/D2_tensor_moore_collapse.tex`. It is existing background, not a new theorem. Its elementary chain consequence is that the reduced integral homology of M smash D has exponent p: its cellular chain complex is the suspension of the derived tensor product of the reduced chains of D with F_p. The derived tensor product is represented by a complex of F_p-vector spaces. It is not necessary, and would be weaker, to infer only exponent p squared from the long exact homology sequence.

This permits countable, simply connected, elementary-exponent representatives when testing a primary reversible closure, but does not decide whether such a representative lies in the lower class.

## 3. Torsion-free abelian rigidity does not survive a natural primary modification

**Proved route exclusion.** For a torsion-free abelian group G, set

`C_G = cofib(p: Sigma BG -> Sigma BG)`,

where p is the natural p-fold co-H-space self-map of the suspension. Then exactly one of the following holds:

* If G/pG=0, C_G is contractible.
* If G/pG is nonzero, the finite Moore space M(F_p,2) is a homotopy retract of C_G. Moreover C_G has p-primary reduced homology, so its reversible closure is the full upper primary class.

Here is a direct proof without an unproved structure theorem for large abelian groups. Every finitely generated subgroup of G is free abelian. The filtered union of these subgroups and the usual torus calculation give natural isomorphisms H_k(BG;Z)=Lambda^k G. Exterior powers of torsion-free abelian groups are torsion-free, since they are filtered colimits of exterior powers of free finite-rank groups along injective maps. The homology sequence of the defining cofiber therefore identifies reduced H_{k+1}(C_G;Z) with (Lambda^k G)/p, for k≥1, and gives no other reduced homology. Thus all these homology groups have exponent p.

If G/pG=0, multiplication by p is bijective on G and on every positive exterior power. Hence C_G is acyclic. It is simply connected, so it is contractible.

Suppose G/pG is nonzero. Choose a nonzero linear functional lambda:G/pG→F_p and g in G with lambda(g) nonzero. There exists a homomorphism h:G→Z_p whose reduction modulo p is lambda. To verify existence directly, put one variable x_a in the compact group Z_p for each a in G, and impose the closed equations x_(a+b)=x_a+x_b and x_a mod p=lambda(a). Every finite set of these equations lies in a finitely generated free subgroup H of G. Choose a basis for H, lift lambda on that basis to Z_p, and extend linearly; this solves the finite set. Compactness of the product Z_p^G gives a simultaneous solution. In particular h(g) is a p-adic unit.

The maps Z→G→Z_p, with 1 sent first to g, induce

`M(F_p,2)=C_Z -> C_G -> C_Zp`.

For k≥2, Lambda^k Z_p is torsion-free and p-divisible: its quotient modulo p is Lambda^k(F_p)=0. Also Z_p/pZ_p=F_p. Thus C_Zp is simply connected with exactly one nonzero reduced homology group, namely H_2=F_p. The displayed composite induces multiplication by h(g) modulo p on H_2 and is consequently an integral homology equivalence. Between simply connected CW models it is a weak equivalence. Composing C_G→C_Zp with an inverse to that composite gives a retraction onto C_Z=M(F_p,2).

This treats the natural attempt to turn the large torsion-free abelian groups used in ordinary nullity constructions into primary generators by taking the cofiber of p on a suspension. It does not prove that every possible primary modification of a rigid-group construction collapses. The final statement about the upper endpoint uses the already rechecked finite-primary-generator result from REVLOC D.2.8/D.3.3.

## 4. Bounded integral homology cannot yield a nontrivial sphere-null separator

**Proved necessary condition, not a solution of A.4.** Let X be a connected space with p-primary reduced integral homology. If that homology is nonzero but bounded above, then X is not sphere-null at p. In fact if d is the greatest index with H_d(X;Z) nonzero, there exists a nonnull map X→S_(p)^(d+1).

Since X is connected, d≥1. Put A=H_d(X;Z). From 0→Z_(p)→Q→Q/Z_(p)→0, injectivity of Q, and torsion of A, one obtains

`H^(d+1)(X;Z_(p)) = Ext(A,Z_(p)) = Hom(A,Q/Z_(p)) != 0`.

The last inequality holds because the p-primary Prüfer group Q/Z_(p) is an injective cogenerator for nonzero p-primary abelian groups: a nonzero map from a cyclic subgroup extends by injectivity. Choose a nonzero class c in this cohomology group. It is represented by X→K(Z_(p),d+1), the bottom Postnikov section of S_(p)^(d+1). All obstruction groups for lifting this map through the succeeding Postnikov sections vanish. They have the form H^r(X;B) with r≥d+3; all such groups vanish for every abelian group B by the universal coefficient theorem and the bounded integral homology assumption. Choose lifts and their compatibility successively. The homotopy limit of the Postnikov tower of the simply connected localized sphere is the sphere itself, so these coherent lifts give X→S_(p)^(d+1). Its composite with the bottom Postnikov map is c and hence is not null.

No finite generation, finite CW dimension, or cardinality bound is used. If X is instead integrally acyclic, Sigma X is simply connected and acyclic, hence contractible; X already lies in the least reversible aspherical class and cannot be a separator. Thus a nontrivial A.4 separator must have nonzero integral homology in arbitrarily high degrees.

The stronger proposed assertion—that every nonacyclic primary source of bounded integral homology forces the upper primary endpoint when adjoined to BC_p—has not been proved. A nonzero map to a sphere does not imply that a finite Moore space belongs to the reversible class generated by its source. Passing from bounded cohomology to a compact retract of an arbitrary large spectrum is also unproved. The elementary necessary condition above must not be promoted to that stronger assertion.

## 5. Arbitrary powers of a fixed degreewise finite homotopy type

**Proved uniform-cardinality route exclusion.** Let X be a connected pointed space such that pi_n(X) is finite for every n≥1. For every set I, the space X^I is a filtered homotopy colimit of finite powers of X. Consequently any reversible aspherical class containing X contains X^I for every set I. The same conclusion holds for an ordinary nullification-acyclic class.

To prove this, let Part_fin(I) be the set of partitions of I into finitely many nonempty blocks, ordered by refinement. It is filtered: intersections of blocks give a common finite refinement. Associate to a partition P the finite power X^P. Refinement induces the map that repeats a coordinate on the subdivided blocks. There is a natural comparison

`hocolim_(P in Part_fin(I)) X^P -> X^I`.

Homotopy groups commute with filtered homotopy colimits of spaces. On pi_n, this comparison is the inclusion from the group of finite-image functions I→pi_n(X) into all functions I→pi_n(X). It is an isomorphism, because pi_n(X) is finite. Both sides are connected, so the comparison is a weak equivalence. The empty-index case is the one-point space and is immediate.

Finite products of aspherical objects are aspherical. In the reversible setting this also follows from the cofiber sequence X wedge Y→X times Y→X smash Y and smash closure. For ordinary nullification it follows from preservation of finite products, or directly from the mapping-space acyclicity test. Closure under the indicated homotopy colimit proves the assertion.

This argument handles arbitrary cardinal powers of a fixed such generator and finite products of families of such powers. It does not prove closure under products of arbitrarily varying homotopy types, under products when the homotopy groups of the fixed factor are infinite, or under arbitrary inverse limits. In particular it does not settle the size of the A.4 fibre. The argument is separate from the invalid principle that maps from an inverse limit to a finite target must factor through a finite stage.

## 6. Other possibilities examined but not established

* Loops on p-completed finite-group classifying spaces might be primary and BC_p-null. In periodic cases the usual sphere-fibre model forces a degree-p sphere map to become an equivalence when that loop space is declared aspherical, and so reaches the upper endpoint. Extending this argument to all finite groups would require precise completion/fibration and finite-cofiber comparisons that have not been proved here.
* Miller's algebraic Ext criterion can make a source null for all bounded-mod-p-homology nilpotent targets, but tensoring the known BC_p module with another realized module produces the already lower-class smash constructions. No algebraic module with the required properties has been realized to give a new separator.
* A uniform compact-generation argument for bounded-dimensional primary spectra would be stronger than the elementary cohomological obstruction above. It is currently an attempt, not a theorem. Stable Bousfield cardinal bounds do not supply that argument.

## Source-opening ledger for this block

1. **Miller 1984 original, opened.** Author PDF: <https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture.pdf>. Theorem 1.5, printed p.45, read at its statement and proof; Section 8, Theorems 8.7–8.8, printed pp.77–79, read. Printed p.78 also inspected as an image to check the quantifier s≥0. Web references `turn863453634view1`, `turn972473901view0`, `turn972473901view1`, `turn848364499view0`. The bibliography key AMiller already exists in the main project; no duplicate original-paper entry is created here.
2. **Miller 1985 corrigendum, opened in full.** Author PDF: <https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture-correction.pdf>, printed pp.605–609, web reference `turn270632898view0`. Exact scope is recorded in section 1. It is added to the separate bibliography fragment below.
3. **Flores search lead, not obtained.** The idus.us.es bitstream PDF returned 403 Forbidden (`turn863453634view0`). Its search snippet helped locate Miller Theorem 1.5; no theorem from the inaccessible paper is used.
4. **Search leads only, not theorem inputs.** Castellana–Crespo–Scherer, *Deconstructing Hopf spaces*, the finite-group completion literature, and searches for bounded-homology or finite-dimensional nullity classes did not supply an opened primary statement proving the desired uniform-generation theorem. No claims in these notes rely on their snippets.

## Search strings newly submitted

* `"finite dimensional" "nullity" Bousfield`
* `"finite-dimensional" "acyclic" "nullification"`
* `"finite-dimensional spectra" "localizing"`
* `"Miller spaces" "homology"`
* `"finite-dimensional" "nullification" Bousfield`
* `"nullification" "bounded homology"`
* `"nullification" "finite-dimensional complexes" Bousfield`
* `"nullity" "finite dimensional" spaces`

No claim of main-question movement is made on the basis of these route exclusions.

## 7. The Postnikov-product operation preserves relative nullity

**Proved route exclusion; not a principal-question advance.** Let X be simply connected, with each pi_n(X) a finite p-group, and put Y=product_(n>=0) P_n X. Then BC_p wedge X and BC_p wedge Y kill each other under ordinary nullification. In particular,

`minRev(BC_p wedge X) = minRev(BC_p wedge Y)`.

The inequality from Y to X follows from the homotopy retraction X→Y→X constructed in A4.4. Its proof only uses that every homotopy group of X is finite: choose a degreewise finite reduced minimal Kan model, use its coskeletal Postnikov tower, and take a nonprincipal ultrafilter limit in each finite simplicial degree. The p-primary hypothesis is not needed for this retraction.

For the converse, set A=BC_p wedge X and let X<n> be the homotopy fibre of X→P_nX. Every connected finite p-primary Postnikov space is ordinarily BC_p-acyclic. Here the fundamental group step must be included: the classifying space of a finite p-group is BC_p-acyclic by a finite central series, using BC_p itself and closure of the acyclic class under extensions by fibrations. The simply connected Postnikov layers are the p-primary Eilenberg–Mac Lane spaces killed by BC_p in A34.2. Induction through the Postnikov fibrations proves the assertion, including possible nontrivial actions. The extension argument uses the natural equivalence from constant maps Z→Map(F_b,Z) for each acyclic fibre F_b and each null target Z, so it is compatible with transport around the base; it does not assume a trivial action.

In particular Omega P_nX is connected and is such a finite Postnikov space. Its fundamental group is the finite abelian p-group pi_2(P_nX), not generally the trivial group. The fibre sequence

`Omega P_nX -> X<n> -> X`

therefore makes each X<n> A-acyclic. Their connectivities tend to infinity, and consequently the comparison from the weak product of the X<n> to their full product is a weak equivalence: on each fixed homotopy group only finitely many factors can be nonzero. Finite products and filtered homotopy colimits preserve ordinary A-acyclicity, so the full product of these covers is A-acyclic.

The power X^N is also A-acyclic. Apply the finite-partition case of A4.3 to the finite homotopy groups of X; it writes X^N as a filtered homotopy colimit of finite powers of X. Taking the product of the Postnikov fibre sequences now gives

`product_n X<n> -> X^N -> product_n P_nX = Y`.

If Z is A-null, mapping out of the A-acyclic fibres identifies Map(Y,Z) with Map(X^N,Z). The latter is naturally equivalent to Z, since X^N is A-acyclic. Thus Y is A-acyclic. Together with the retraction, this proves the asserted mutual killing and hence equality of relative reversible closures.

This strengthens the scope description of A4.4. The product of Postnikov sections can reach the upper endpoint, as it does for a finite Moore space, but after adjoining BC_p it recovers the relative ordinary nullity of the original finite-homotopy-group space. If X is already ordinarily BC_p-acyclic, the product remains so. No separator is produced by this operation without already possessing one in X. The missing background note EH5_D3.md was not available; this observation is recorded without a novelty claim.

Sources and checks are the exact finite-model and Postnikov statements already opened for A4.3–A4.4 (Barnea–Harpaz–Horel Lemma 7.2.4 and Kerodon tags 055K, 055B, 052N), the independently checked A34.2, and the explicit fibre-extension proof above. No additional inverse-limit closure is asserted.

## 8. Converse-Miller and infinite-group literature: scope checks

The source condition in this task is `Map_*(X,S^n)=*`. The term "Miller space" is also used in some literature for the different target condition `Map_*(BC_p,X)=*`. Searches mixing these conventions can produce an apparent converse that has no bearing on A.4.

Strom's published 2003 paper, Corollary 11, gives equivalence between vanishing of maps from X to all sufficiently high spheres and vanishing of maps from X to finite nilpotent complexes. The publisher PDF was opened at the corollary, its deduction from Theorem 10 and Proposition 7, and its introduction. It does not assert that such X is BC_p-acyclic. The earlier Paris-hosted manuscript has a corrupted PDF text layer and differing preliminary wording; the readable published version is used for this scope check. The relevant primary URL is <https://www.impan.pl/shop/en/publication/transaction/download/product/88494>, web references `turn724696470view0` and `turn839205964view2`. The existing project bibliography already contains Strom; no duplicate entry is needed. Parent independently opened the 2009 Oberwolfach restatement and owns that read record.

The finite-type/co-H attempt did not prove an additional implication. A criterion for the *target* X to be BC_p-null, even if expressed through locally finite mod-p cohomology, supplies no theorem saying that a Miller *source* becomes BC_p-acyclic after suspension. No preservation of co-H structures by BC_p-nullification, and no reconstruction of all BC_p-null targets from finite complexes by homotopy limits, was established. Those are missing arguments, not adopted principles.

Flores–Muro, *Torsion homology and cellular approximation*, AGT 19 (2019), 457–476, was opened in both arXiv v2 and its published version. Sections 4–5 and their relevant proofs were read. Its group-cellularity examples do not imply BC_p-cellularity of classifying spaces. The Burnside example is excluded from the primary interval by its free abelian Schur multiplier. The published §5 uses the classical bound p>10^10; Remark 5.6 explains the stronger p>665 bound appearing in the preprint. This result supplies no p=2 example. Its elementary-amenable torsion case is locally finite and hence already belongs to the known BC_p constructions. No claim about all higher homology of the Grigorchuk group is inferred from its group cellularity.

There is an independent finite certificate for the group/space distinction. In groups, S_3 belongs to the class closed under colimits and containing C_2. First form C_2*C_2=<a,b | a^2=b^2=1>. The word babab is an involution. Coequalize the two homomorphisms C_2→C_2*C_2 sending its generator to a and babab. The resulting presentation is

`<a,b | a^2=b^2=(ab)^3=1> = S_3`.

Indeed every word reduces to one of (ab)^k or (ab)^k a, 0≤k<3, and their images under a=(12), b=(23) are six distinct permutations. In contrast, the normalized bar complex over F_3 has boundary ranks 0,5,20,104 in degrees 1 through 4. Its degree-three homology has dimension 125-20-104=1. Thus BS_3 has nonzero positive mod-3 homology and cannot have 2-primary integral reduced homology. In particular it is not BC_2-acyclic. This proves directly that group-colimit constructions cannot be moved through B while preserving the homotopy-colimit and primary hypotheses needed here.

The exact program `code/A4_group_colimit_warning.py` checks the six normal forms, both coequalizer maps, every normalized bar differential composition through degree four, and the finite-field ranks. Its passing JSON is saved in `code/A4_group_colimit_warning.out`. This is a route exclusion, not a new interval element or a fibre-size bound.

### Additional opening ledger

* **Flores–Muro, published original:** <https://msp.org/agt/2019/19-1/agt-v19-n1-p11-p.pdf>, references `turn493444328view0`, `turn897319970view0`. Sections 4–5 read, including published p>10^10 scope and Remark 5.6. The arXiv version <https://arxiv.org/pdf/1707.07654> was also opened (`turn407924370view0`, `turn314830315view0`–`view3`). Two guessed publisher filenames returned different papers; those papers were not used.
* **Berrick–Casacuberta, author original:** <https://www.ub.edu/topologia/casacuberta/articles/berc1.pdf>, `turn915589659view0`, `turn839205964view1`. Section 3, Theorem 3.1 and Lemma 3.2, statements and proofs read. Their relevant mapping-space assertion assumes integral acyclicity; a connected acyclic source has contractible suspension, so these examples cannot separate reversible primary classes. No rigid-group smallness theorem is inferred.
* **Berrick–Miller strongly torsion generated groups:** search located the paper and publisher metadata, but the attempted full PDF at hcmuaf.edu.vn timed out (`turn985721226view0`). No theorem from this unopened paper is used. In particular, torsion-generated does not mean a torsion group, and no Sullivan theorem is asserted for all torsion groups.
* **Flores thesis:** the UAB PDF returned an access-denied page (`turn915589659view1`); a CiteSeer copy of the related nullification paper returned 403 (`turn985721226view1`). These unsuccessful openings supply no theorem input.
* **Neisendorfer, Algebraic Methods:** the author-PDF opening timed out (`turn839205964view0`). The search result is a lead only, and no locally-finite-cohomology criterion is imported from it.

Additional submitted searches included `"Miller spaces" "converse"`, `"Miller spaces" "acyclic"`, `"Miller space" "BZ/p-null"`, `"co-H" "BZ/p-null"`, `"Sullivan conjecture" "torsion groups"`, `"Grigorchuk" "nullification"`, and `"Sullivan conjecture" "Burnside"`. None changed the A.4 equality, third-element, or full-fibre-size status.

## 9. Finite chromatic target families collapse to the existing test

**Attempt.** For an integer n≥1, let F_n contain all simply connected finite CW complexes V with p-primary reduced integral homology and stable chromatic type at least n. Define N_n to be the sources X with Map_*(X,V) contractible for every V in F_n. These families initially appear to offer different target-defined classes in the primary interval. The following argument excludes this construction: N_n=N_1 for every finite n. On primary sources, their common test is the existing sphere-null test by the supplied REVLOC D.3.6. This does not decide the equality of that existing test with the BC_p-generated minimum.

Fix an arbitrary pointed source X in N_{n+1}. Put R_X={Y:Map_*(X,Y)≃*}; this class is closed under homotopy limits. Let V∈F_n. If V has type at least n+1, there is nothing to prove. Otherwise its suspension spectrum has type n. Hopkins–Smith's periodicity theorem, Theorem 9 (with n≥1), provides a stable self-map of strictly positive suspension degree d which is an isomorphism in K(n)-homology. After a single finite additional suspension m, compactness and the definition of stable maps between finite complexes represent it by an actual cellular map

`v: Sigma^d U -> U,       U=Sigma^m V.`

The space U is still a simply connected finite p-primary complex. We use this actual map and its actual iterates, rather than claiming that stabilization preserves inverse limits. For r≥1 define

`C_r = cofib(v^r: Sigma^(rd) U -> U).`

Each C_r is a simply connected finite p-primary CW complex. Its reduced K(i)-homology vanishes for every i≤n: for i<n both copies of U are K(i)-acyclic, and for i=n the attaching map is an isomorphism. Thus C_r∈F_{n+1}. The square with domain map Sigma^(rd)v and target map id_U commutes strictly after choosing the iterated representatives; mapping cones give a coherent tower C_{r+1}→C_r under U.

The connectivity of U→C_r tends to infinity. Indeed the cone cells being attached come from Sigma^(rd)U, whose connectivity tends to infinity because d>0. For each fixed k the maps π_kU→π_kC_r, and also those for k+1, are therefore eventually isomorphisms compatible with the tower. The Milnor exact sequence gives an equivalence

`U -> holim_r C_r.`

All C_r belong to R_X, so U belongs to R_X. This is a limit in the **targets**, where the mapping-space functor preserves it. No inference from nullity of a source inverse limit to nullity of its stages is used.

To remove the additional suspension m, retain the same v and take its finite bouquets. For every positive integer a, the map ∨^a v on ∨^a U has the same positive degree d and suspension bound m; all cofibers of its iterates remain in F_{n+1}. The preceding argument therefore puts ∨^a Sigma^m V in R_X for every finite a. Barratt's finite cone-cube construction, as proved in Strom 2012 Theorem 8, now lowers this whole finite-bouquet family one suspension at a time. At each step the space is simply connected. It follows that V∈R_X. Hence N_{n+1}⊆N_n; the reverse inclusion follows from F_{n+1}⊆F_n, and induction proves the asserted equality for every finite n.

For the primary-interval identification, N_1-nullity includes the single finite Moore target P^3(p), so REVLOC D.3.6 gives nullity of the p-completed spheres. Conversely a primary sphere-null source is null for every simply connected finite target, by the already rechecked finite-target Miller comparison, and hence belongs to N_1. The argument deliberately makes no assertion about a single arbitrary finite type-n target without the full target-family quantifier, nor about an infinite chromatic bound. It supplies no generator outside W_0 and no bound on the full fibre of T.

**Opening and proof record.** Hopkins–Smith, *Nilpotence and stable homotopy theory II*, Annals 148 (1998), 1–49, author-hosted original <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/HS.pdf>, was opened anew (`turn615157022view0`). Read Definition 8 and Theorem 9 on printed page 4; Section 3's genericity proof through Corollary 3.11, and Section 4.4's construction and proof of Theorem 4.12 (`turn261266372view0`, `turn261266372view1`). The source supplies the periodicity theorem; the unstable cofiber tower and its uniform finite-bouquet desuspension are the argument above. The bibliography already contains `AHopkinsSmith`; no duplicate bibliographic entry is introduced. Strom's published 2012 original was also opened anew (`turn113062743view0`) and its Theorem 8 proof read. The complete supplied D.3.6 Moore-tower proof was reread, with its pro-space/unstable-limit distinction retained. This is a failed candidate-family construction, not principal stopping-rule movement.
