# Leads 1–5: verified algebra and exact scope

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No claim of priority. These notes do not settle the main implication.

## Sources actually read and dependencies verified

We read the full task prompt; TOTEX_return/TOTEX_paper.tex, A.1–A.5, B.1–B.7, D.13; TOTASPH/TOTASPH_C.tex, especially C.3–C.6 and C.11–C.13; TOTASPH/TOTASPH_D.tex, the affine criterion proof; and the supplied Isbell–Mitchell (1976) PDF, pp. 289–296, §§1–3 and the start of §4, using its text extraction. In Isbell–Mitchell (1976), Lemma 2.2 and Proposition 2.3 appear on p. 293; Theorem 3.1 is on p. 294, its proof continues on p. 295; Proposition 3.3 is on p. 295 and the coefficient-ring remark is on p. 296.

The R1 step actually used is the integral bar identification: the degree-n generators of the simplicial replacement of Z[H] are pairs consisting of a composable n-chain in A and a starting element of H. These are exactly the nerve simplices of El_A(H), with the same faces. Totality therefore implies T_i(Z[H])=0 for i>0. This needs all components but does not require H to be connected or nonempty. The source's dependent-sum construction correctly transfers an action on an element component to an action on A; its cyclic-cover argument is correctly confined to unrestricted actions. We make no substitution of an arbitrary module for Z[H].

The R2 step used is Isbell–Mitchell's Theorem 3.1: exact colimits are equivalent to filtered components of Aff_Z(A). Proposition 3.3 identifies this with I and III. The proof's passage from a finite sum with disparate targets to one target uses I only to obtain a common successor within the relevant component. Extending an A-module affinely preserves its colimit, since x−Σn_i f_i x=Σn_i(x−f_i x) when Σn_i=1. These checks fix both the variance and the required finiteness.

The R4 step used is I+IV for a total category and its inheritance by each connected A-set. In TOTEX A.4, I follows by applying the common-successor argument to the total element category p/A. Pair affine equalization follows from the pair presentation and H_1 vanishing, with common successors combining its finite augmentation witnesses. In Isbell–Mitchell Lemma 2.2, connectedness of an A-set plus I reduces a zigzag to a common image; Proposition 2.3 then transfers IV. A direct proof of the latter transfer is given below, so the proof does not rest on its 'reader may verify' wording.

The R7 calculations have been checked directly: write J for the image of the relation map, use the two short exact sequences involving J, and use the fact that the induced relation map on representable colimits is zero. The row kernel lies in P_q^2 and cannot be replaced by the column kernel L⊂P_q. All our uses preserve this distinction.

## General conventions

A is any small category unless additional hypotheses are stated. Modules are covariant functors A→Ab; natural transformations of such functors are the module maps below. P_x=Z[A(x,−)] is projective, with the canonical augmentation identification colim_A P_x=Z. We write T_i=L_i colim_A. For a submodule E⊂P_x, ε(E) is the image of colim E→Z, not merely the union of pointwise augmentation images. A finite collection of objects in one connected component has a common successor when A satisfies I: a finite zigzag between two objects can be shortened by completing spans, and induction handles finitely many objects. This also holds for a total category by R4.

For every short exact sequence 0→U→V→W→0 we use the standard long exact sequence of T_i. In particular, if V is T-acyclic, T_1(W)=ker(colim U→colim V), while T_i(W)=T_{i−1}(U) for i≥2. When both V and W are acyclic, U is acyclic and colim U→colim V is injective.

## Lead 1 — proved

Let A be total, let a_0,a_1,a_2:p→q be ordinary arrows, z_i=a_i−a_0, K_i=ker(P_q→P_p,t↦tz_i), L=K_1∩K_2, S=K_1+K_2, and C=P_q/S. Then the R7 surjection is canonically an isomorphism

T_1(C) ≅ Z/ε(L).

For each i set H_i=A(p,−)/(ca_0∼ca_i) and J_i=im(P_q→P_p,t↦tz_i). The free abelian functor preserves the displayed set coequalizer, so 0→J_i→P_p→Z[H_i]→0 is exact in Ab^A. Totality makes its last term acyclic. Its colimit map Z=colim P_p→colim Z[H_i]=Z is the identity, because El_A(H_i) is connected: every object is reached from the distinguished element at p. Hence colim J_i=0 and T_j(J_i)=0 for j>0. The sequence 0→K_i→P_q→J_i→0 consequently identifies colim K_i→Z with an isomorphism and proves T_j(K_i)=0 for j>0.

The pointwise exact sequence 0→L→K_1⊕K_2→S→0 has maps l↦(l,−l) and (u,v)↦u+v. Right exactness gives

colim S ≅ Z²/{(n,−n):n∈ε(L)}.

The map colim S→colim P_q=Z is induced by (a,b)↦a+b. Its kernel is precisely {(n,−n):n∈Z}/{(n,−n):n∈ε(L)}, canonically Z/ε(L) through (n,−n)↦n. Since P_q is projective, this kernel is T_1(C). This is exactly R7's map, rather than an unrelated abstract isomorphism.

For the alternative derivation, define D=im(P_q→J_1⊕J_2,t↦(tz_1,tz_2)). Its kernel is L, so D≅P_q/L. There is an explicit natural isomorphism

P_q/(K_1+K_2) → (J_1⊕J_2)/D,
[t] ↦ [(tz_1,0)].

It is surjective: a pair (uz_1,vz_2), modulo (vz_1,vz_2)∈D, is ((u−v)z_1,0). It has the stated kernel: (tz_1,0)=(wz_1,wz_2) forces w∈K_2 and t−w∈K_1; the converse follows by this same equation. These are natural Z-linear maps at every object, hence an isomorphism in Ab^A. Since J_1⊕J_2 is acyclic with colimit zero, its exact sequence with D and C gives T_1(C)≅colim D=Z/ε(L).

## Lead 2 — proved, componentwise and including the empty category

Assume A satisfies I, with no connectedness or nonemptiness assumption. The following are equivalent:

1. colim_A:Ab^A→Ab is exact.
2. For every p,r∈A and every z∈Z[A(p,r)] of augmentation zero, there exist s∈A and t∈Z[A(r,s)] with aug(t)=1 and tz=0.

Moreover, without hypothesis I, for J=P_r z⊂P_p and E=ann(z)=ker(P_r→P_p,t↦tz), there is a canonical isomorphism

T_1(P_p/J) ≅ Z/ε(E).

Indeed, the map colim P_r=Z→colim P_p=Z induced by multiplication by z is multiplication by aug(z)=0. Right exactness of 0→E→P_r→J→0 gives colim J=Z/ε(E), and its map to colim P_p is zero. The sequence 0→J→P_p→P_p/J→0 then gives the displayed formula. With common successors in the component of r, ε(E)=Z is equivalent to an actual affine annihilator by combining the finitely many representatives of augmentation 1. Thus (1) implies (2).

Conversely, for any parallel affine arrows α,β:p→r, z=α−β has augmentation zero, so (2) gives an affine t equalizing them. I ensures common successors in every component; Aff_Z(A) has the same components as A. These two facts make each component of Aff_Z(A) filtered. Isbell–Mitchell Theorem 3.1 therefore gives exactness. Equivalently, for sufficiency one may extend every A-module affinely and compute its unchanged colimit over filtered components, whose colimits and componentwise direct sums are exact.

For a total category, z=c−c′ is the pair case of Lead 3 or of R4, hence has such an annihilator. A triple result by itself does not supply (2): after applying an affine equalizer to three ordinary arrows, the remaining comparisons involve affine rather than ordinary arrows. We claim no induction from triples here.

The case z=0 is consistent: E=P_r, its augmentation image is Z, the Tor group is zero, and id_r is an annihilator. If A(p,r)=∅, the only z is zero, so it causes no exception. For the empty category both conditions are vacuous and the zero colimit functor is exact. Multiple components are handled separately.

## Lead 3 — proved in the full asserted generality

Let A be arbitrary, k≥0 finite, and a_0,…,a_k:p→q. Put z_i=a_i−a_0 for 1≤i≤k, and define the natural module map

d^T:P_q→P_p^k,    (d^T)_x(t)=(tz_1,…,tz_k).

Put L=ker d^T, D=im d^T and Q_a=coker d^T. Then

T_1(Q_a) ≅ Z/ε(L),
T_2(Q_a) ≅ ker(colim L→Z),
T_i(Q_a) ≅ T_{i−2}(L)  (i≥3).

The first exact sequence 0→L→P_q→D→0 gives colim D=Z/ε(L), T_1(D)=ker(colim L→Z), and T_j(D)=T_{j−1}(L) for j≥2. The induced map colim D→colim P_p^k=Z^k is zero: its composite with the epimorphism Z=colim P_q→colim D is the vector of augmentations of z_i, all zero. Apply the long exact sequence to 0→D→P_p^k→Q_a→0. Its projective middle term gives exactly the three formulas. Their canonicity is supplied by the boundary maps and the representable augmentations.

If objects in the component of q have common successors, ε(L)=Z iff there is one element t∈L(r) of augmentation 1: transport and sum the finite representative family. Thus T_1(Q_a)=0 iff this particular finite ordinary family has a simultaneous affine equalizer. For k=0, P_p^0=0, L=P_q and Q_a=0; every formula still holds and the equalization condition is vacuous.

The row map d:P_q^k→P_p, (t_i)↦Σ_i t_i z_i has cokernel Z[H], H=A(p,−)/(ca_0∼⋯∼ca_k). This follows objectwise because the kernel of free abelianization of a set quotient is generated by differences of identified elements. Its relation submodule is exactly the image of d. For total A its cokernel is therefore T-acyclic by R1. No conclusion about the distinct cokernel Q_a follows merely by transposing the matrix.

The presentation of Q_a has k free generators x_i at object p and one module relation at q, namely Σ_i z_i x_i=0. Explicitly x_i is the identity basis element in the i-th P_p summand, and z_i x_i means applying the linear extension of the A-action to that generator. This is a relation in (P_p^k)(q), not a sum of arrows with mismatched codomains.

## Lead 4 — proved quantified assertions; interpretive qualification

Assume A is quasi-filtered. If M:A→Ab, q∈A, and α,β∈M(q) represent the same element of colim_Set UM, then an affine t:q→s satisfies M(t)α=M(t)β.

Proof. Let X⊂UM be their connected A-set component. Condition I on A and connectedness of X give arrows f,g:q→r with M(f)α=M(g)β, by reducing the finite zigzag connecting them using commuting squares. Condition IV on A gives an affine v:r→s with vf=vg in Z[A(q,s)]. Put t=vf=vg. Then

M(t)α=M(v)M(f)α=M(v)M(g)β=M(t)β.

This directly proves the precise instance of Isbell–Mitchell Proposition 2.3 that is needed. Equally, applying it to a general A-set X and then its linearization proves the inherited IV statement.

Now assume only I. A is exact iff for every M:A→Ab and every α,β∈M(q) equal in colim_Ab M, an affine t:q→s equalizes α,β.

For necessity, extend M to Aff_Z(A), whose connected components are filtered by Theorem 3.1. The canonical colimit comparison is an isomorphism of abelian groups. The underlying set of a filtered colimit of abelian groups is its filtered colimit of sets: the elementary representative construction transports finitely many elements to one object, and equality is witnessed after one transition. Thus α and β admit a single Aff_Z(A)-arrow t equalizing them. The argument takes place within the component of q; direct sums over other components do not change their equality.

For sufficiency, apply the property to M=P_p and to any parallel affine α,β:p→q. Both have image 1 in colim P_p=Z. The resulting t equalizes them. With I this makes components of Aff_Z(A) filtered, hence colimits exact. One may alternatively apply it to an arbitrary augmentation-zero z∈P_p(q) and β=0 and invoke Lead 2.

There is a canonical map θ_M:colim_Set UM→U(colim_Ab M). In a connected category with common successors it is surjective: every element of the abelian colimit is a finite sum of representatives, which can be transported to one target and added there. In a disconnected category it need not be surjective because sums can involve different components, so the surjectivity assertion is explicitly confined to each component. Under I+IV, ordinary set-connectedness gives affine equalization; exactness asks for affine equalization throughout each fibre of θ_M. This is the precise useful content of the closing sentence of Lead 4.

One must not strengthen that sentence to 'exactness iff θ_M is injective' or to 'exactness iff set colimits preserve finite products.' These stronger assertions are false already for exact Δ_inj. With M=P_[0], a finite integer vector on an ordered ordinal is carried by injections to a vector with extra zero entries. Its ordered list of nonzero coefficients is an invariant of its component in colim_Set UM. At [2], α=(1,1,−1) and β=(1,0,0) therefore lie in different set-colimit components, but both have augmentation 1 and hence the same abelian-colimit image. Δ_inj also fails siftedness, as independently verified in R3. We do not treat the prompt's informal wording as asserting either of these false stronger equivalences.

## Lead 5 — proved algebraic statements, with the coefficient-cycle interpretation made precise

Fix a_0,a_1,a_2:p→q, z_i=a_i−a_0, K=ker(P_q²→P_p,(t_1,t_2)↦t_1z_1+t_2z_2), K_i=ann(z_i), and K_3=ann(z_2−z_1). Let ρ_1,ρ_2,ρ_3∈P_q(s) all have augmentation 1, with ρ_1z_1=0, ρ_2z_2=0, and ρ_3(z_2−z_1)=0. Define κ=(ρ_1−ρ_3,ρ_3−ρ_2)∈P_q(s)².

### (i) The class of κ

Direct expansion gives

(ρ_1−ρ_3)z_1+(ρ_3−ρ_2)z_2
=ρ_1z_1−ρ_2z_2+ρ_3(z_2−z_1)=0.

Thus κ∈K(s), and its two augmentations are zero. For total A the checked R7 row computation identifies colim K→Z² with an isomorphism, so [κ]=0 in colim K. The maps are the two restrictions of the representable augmentations; no identification with L=K_1∩K_2 is used.

### (ii) Finite parallel-difference normal form

Let A be connected and satisfy I, F:A→Ab, s∈A, and κ∈F(s). Then [κ]=0 in colim F iff there exist an object y, an arrow u:s→y, finitely many parallel pairs e_j,e'_j:x_j⇉y, and k_j∈F(x_j), such that

F(u)κ=Σ_j(F(e_j)−F(e'_j))k_j in F(y).

In fact common successors for finite sets of objects suffice. The colimit is the quotient of ⊕_x F(x) by the subgroup generated by i_v F(f)k−i_w k for arrows f:w→v. If [κ]=0, choose a finite expression

i_s κ=Σ_j(i_{v_j}F(f_j)k_j−i_{w_j}k_j).

Absorb integer coefficients and signs into k_j. Choose a common successor y of s and all v_j,w_j and one arrow h_x:x→y for each distinct object x appearing. Apply the homomorphism from this finite direct sum to F(y) with components F(h_x). Then u=h_s, e_j=h_{v_j}f_j and e'_j=h_{w_j} have the required sources and common target. Conversely every displayed parallel difference has zero class in the colimit, and [F(u)κ]=[κ]. This proves both directions without assuming any injectivity of F's transition maps.

### (iii) Affine annihilation of κ

If t∈Z[A(s,r)] is affine and F=K gives K(t)κ=0, then tρ_1=tρ_3 and tρ_3=tρ_2 in P_q(r). Their common value has augmentation 1 and annihilates z_1 and z_2, so it is an affine equalizer of the triple.

If the normal form from (ii) has a common affine equalizer v:y→r for all pairs (e_j,e'_j), applying F(v) makes F(vu)κ=0; vu is affine. In a quasi-filtered category a normal form with one term has such a v by IV, so in particular this conclusion holds for total A. The one-term implication requires this pair-equalizer hypothesis; I alone would not supply it.

### (iv) The mixed-cycle quotient

Define ψ:K_1⊕K_2⊕K_3→K by ψ(k_1,k_2,k_3)=(k_1−k_3,k_2+k_3). It is a natural Z-linear map since its image satisfies k_1z_1+k_2z_2+k_3(z_2−z_1)=0. Its kernel consists precisely of (l,−l,l), with l∈L=K_1∩K_2; such l automatically lies in K_3. Thus the inclusion L→K_1⊕K_2⊕K_3, l↦(l,−l,l), identifies its kernel canonically.

Suppose A is total. Put S=im ψ and C=K/S. Each K_i is acyclic with augmentation colimit Z, by the pair calculation in Lead 1, including i=3 applied to (a_1,a_2). The row calculation gives that K is acyclic with colimit Z². Hence

colim S ≅ Z³/{(n,−n,n):n∈ε(L)},

and its map to colim K is induced by f:Z³→Z², f(a,b,c)=(a−c,b+c). The map f is surjective and has kernel {(n,−n,n):n∈Z}. The exact sequence 0→S→K→C→0 therefore identifies

T_1(C) ≅ Z/ε(L).

More precisely the isomorphism sends the class n mod ε(L) under the connecting map to the class of (n,−n,n) in colim S. In particular the class of κ in colim S corresponds to 1 mod ε(L), because κ=ψ(ρ_1,−ρ_2,ρ_3). This element is nonzero exactly when the triple has no affine equalizer (common successors are available).

The same argument supplies the useful extension

T_2(C) ≅ ker(colim L→Z),
T_j(C) ≅ T_{j−2}(L)  (j≥3).

Indeed 0→L→K_1⊕K_2⊕K_3→S→0 gives T_1(S)=ker(colim L→Z³)=ker ε, and T_i(S)=T_{i−1}(L) for i≥2; then use acyclicity of K. Thus all positive derived colimits of C have the same canonical descriptions as those of Q_a, though this alone does not construct an isomorphism C≅Q_a.

For the graph interpretation, at x define a bipartite multigraph G_x with vertices A(q,x)⊔A(p,x) and, for each g:q→x and i=0,1,2, an edge (g,i) directed from g to ga_i. Repeated endpoints retain distinct edges. Its C_1 is P_q(x)^3 and its boundary sends (t_0,t_1,t_2) to (−t_0−t_1−t_2, t_0a_0+t_1a_1+t_2a_2). The natural map

K(x)→Z_1(G_x;Z),   (t_1,t_2)↦(−t_1−t_2,t_1,t_2)

is an isomorphism, with inverse taking the last two coordinates. The cycles of the 0–1, 0–2 and 1–2 edge subgraphs are respectively the images of K_1, K_2 and K_3 under ψ. Consequently C(x) is exactly the cycle lattice modulo these three bicolour cycle lattices. This remains valid when arrows act noninjectively, or some ga_i coincide; the graph is a multigraph and the induced graph map may identify vertices and edges.

The last geometric sentence of Lead 5 must be read with coefficients. The nonzero element of T_1(C)=H_1(B_*(A,C)) corresponding to 1 mod ε(L) is represented by a bar 1-cycle with coefficients in C. Lift its finitely many coefficients to K; its bar boundary then lies in S and represents κ in colim S. This is the exact sense in which mixed cycles transport the null-homology of κ. It is not an assertion of a nonzero ordinary class in H_1(BA;Z), which vanishes for a total category.

## Further main-question attempts recorded so far

1. The graph quotient C in Lead 5 provides a concrete alternative coefficient functor with precisely the same positive T-groups as Q_a. It is not generally a permutation module: its pointwise description is a quotient of integral cycle lattices, with transition maps induced by possibly identifying graph maps. No natural permutation basis has been supplied, so declaring C acyclic would be an unsupported step.
2. The augmentation ideal I(M)=ker(Z[UM]→Z) is acyclic under totality. Its tensor powers are also acyclic: I⊗Z[H] is the kernel of the epimorphism Z[UM×H]→Z[H], and iteration of the same split pointwise tensor sequence gives the claim. The canonical map I(M)→M has kernel I(M)^2 when Z[UM] is regarded as the group ring of the additive group M. However acyclicity of I⊗I does not imply acyclicity of its multiplication image I². The unresolved image step is precisely outside the allowed resolving closure.
3. The simplicial free-abelian comonad resolution has all terms permutation modules, but its extra degeneracy is only a map of underlying sets. After taking abelian colimits it does not automatically give a chain contraction. In degree zero the counit is not the linearization of the face obtained by forgetting a free generator, which prevents treating the whole resulting resolution as the free group on one contracted simplicial set.
4. The totality comparison for Eilenberg–Mac Lane diagrams can compute T_1(M) as stable homology, but does not prove its vanishing: the colimit of their underlying simplicial sets can acquire positive homotopy. Exact, nonsifted Δ_inj already prevents assuming truncation preservation.

5. The three-colour graph of Lead 5 admits a natural Čech description. Cover G_x by G_01,G_02,G_12. Each double intersection is a one-colour forest with component set A(p,x); the triple intersection is the discrete vertex set A(q,x)⊔A(p,x). Taking component groups gives a three-term complex of permutation modules with terms P_q⊕P_p, P_p³, and Z[H_01]⊕Z[H_02]⊕Z[H_12]. Its homology in degree 2 is L (the common annihilator); its degree-1 homology is the mixed-cycle quotient C, by the Mayer–Vietoris spectral sequence, and its degree-0 homology is Z[H_3]. After colimit under totality the complex is Z²→Z³→Z³, with a Z in degree2. This recreates the obstruction T_1(C)=Z/ε(L); it does not prove it zero. The unresolved step remains a special closure under the image/quotient involved.
6. For the proposed reduction G_F(P)=colim_Set Hom(P,F(a)), a common successor gives surjectivity of G_F(P⊕Q)→G_F(P)×G_F(Q), but not injectivity. In the presheaf element category, cospan components between (P,x),(Q,y) are indexed by the fibre of this map: any cospan (P,x)→(R,z)←(Q,y) receives the canonical cospan based on (P⊕Q,G_F(i⊕j)z), and arrows preserve this joint class. Consequently a shear-endomorphism argument must not infer equality of joint tuples from equality of individual coordinate classes. Δ_inj already has relative-order invariants that prevent this.
7. The parent proposed coefficient detection (integral exactness iff exactness over Q and every F_p), and we independently checked it. For objectwise torsionfree modules, the bar complex is Z-flat, and the UCT in degree i+1 gives that H_i has no p-torsion for any p, whereas rational exactness makes H_i torsion; therefore H_i=0. Torsion diagrams decompose into their functorial p-primary parts, each a filtered union of bounded-exponent subdiagrams with F_p layers. Extension and filtered-colimit closure settle these, then the torsion/torsionfree short exact sequence settles all modules. This does not settle any individual field case.
8. The literature agent proposed I plus a local Ramsey property implies integral exactness. We checked its dual-certificate proof: if E=Σ_r aug ker D_r is proper, choose c≠0 in R/Z annihilating E. The map D_r(t)↦c aug(t) extends from im D_r to the whole free abelian codomain by injectivity of R/Z. Coordinate potentials then define a finite colouring by small boxes in (R/Z)^k; a Ramsey copy makes the sum of potential differences have distance less than dist(c,0), contradicting that it equals c. This uses the local Ramsey property for the chosen finite family and k≥1. The agent owns the result and its primary Ramsey citations.

## Supplementary searches made by this agent

Search engine 2 queries: `"acts" "homologically flat" monoid`; `"monoid" "permutation modules" "flat"`; `"Z-flat" acts monoid linearization`.
Search engine 1 queries: `monoid acts linearization flat modules homology permutation flatness`; `"homological" "flatness" "acts"`; `"permutation modules" "Tor" "flat" monoids`.
No source giving a test theorem from Tor-vanishing on all permutation modules to integral flatness was obtained. Results concerned ordinary set-act flatness and strongly flat acts, or unrelated permutation-module representation theory. We did not infer the contents of unopened sources. The primary Wiley result returned a substantial excerpt of *The flat cover conjecture for monoid acts*, DOI 10.1112/jlms.70404, but this agent did not open its full page or use it for a mathematical claim; the literature agent was given the URL and search record.
