# Independent audit of the finite-height counterexamples

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). This records an independent check by the Part F agent of the construction supplied by the Part B/C agent. No priority is claimed.

## Result

The construction resolves the former F.12 open statement in this audit: for every finite integer n >= 2, both truncated restricted Yoneda functors on the ordinary homotopy categories are neither faithful nor full, for finite CW tests and for all finite-category homotopy types. It does not contradict the countable-source result F.11.

## Primary input independently checked

Dicks, Kropholler, Leary, and Thomas, *Classifying spaces for proper actions of locally-finite groups*, arXiv:math/0111283, Corollary 6.10(2), printed page 21, states that for an abelian torsion group G and a nonzero o(G)-inverting ring R,

    cd_R(G) = min{aleph-rank(G) + 1, infinity}.

The primary PDF https://arxiv.org/pdf/math/0111283 was opened independently. The definition of aleph-rank is on printed page 1 and the discussion of cohomological dimension and nonzero coefficient witnesses is on printed page 4. Thus G = direct-sum_{aleph_{d-1}} C2 has rational cohomological dimension d, without an additional set-theoretic assumption.

A universe-sized witness module is available. Take the standard rational bar resolution of Q as a QG-module and let Z_d be its d-th syzygy. Since the projective dimension is exactly d, Z_{d-1} is not projective. The extension

    0 -> Z_d -> P_{d-1} -> Z_{d-1} -> 0

does not split. Its nonzero Ext^1 class gives a nonzero Ext^d_{QG}(Q,Z_d) class by dimension shifting. All modules in this construction have underlying cardinality at most max(|G|,aleph_0), so they lie in the same Grothendieck universe as G. Rational group cohomology computed with QG agrees with the usual group cohomology of the underlying G-module.

## Presheaf presentation

Let I be the index set of the elementary abelian 2-group G, and use the filtered poset of finite subsets J of I, with H_J the coordinate subgroup. For each connected finite-category test A, pi_1(A) is finitely generated and

    Map(A,BH_J) = coproduct_{Hom(pi_1 A,H_J)} BH_J

up to the usual groupoid model. This displayed formula uses that H_J is abelian; no quotient by nontrivial conjugation is needed. Every homomorphism into G has image contained in some H_J. The colimit of the automorphism groups H_J is G. All mapping spaces into these classifying spaces are 1-types. Consequently the canonical filtered-colimit map of mapping spaces is an equivalence. Disconnected finite-category tests have finitely many components, and filtered colimits commute with the required finite products. The empty test also satisfies the assertion.

It follows objectwise, and hence as a coherent presheaf statement, that

    R_n(BG) = colim_J R_n(BH_J)

for n >= 2 on finite-category tests. Each BH_J is itself a finite-category test. Truncated Yoneda therefore identifies the space of presheaf lifts over a specified map from R_n(BG) with the homotopy inverse limit of the corresponding truncated local lift spaces.

## Important truncation precision

Postnikov truncation does not preserve arbitrary homotopy pullbacks. The argument must not assert that it does.

Here the base of each local lifting problem is Map(BH_J,BG), which is a 1-type. Put m = n-1 >= 1. For a map E -> B with B an m-type, the canonical comparison

    trunc_m(fib(E -> B)) -> fib(trunc_m(E) -> B)

is an equivalence: the map on fibers before truncation is the pullback of E -> trunc_m(E), whose homotopy fibers are m-connected, and the target fiber is already an m-type. This proves precisely the fiber interchange needed in the construction.

## Nonfaithfulness

Choose d=n, a rational G-module M, and a nonzero alpha in H^n(G;M). The Borel bundle

    p: EG x_G K(M,n) -> BG

has a zero section and a section representing alpha. Its section components are H^n(G;M). For every finite H_J, averaging makes H^q(H_J;M)=0 for q>0. The local section space has only pi_n = M^{H_J}, so its (n-1)-truncation is contractible. The coherent presheaf section space is therefore a homotopy inverse limit of contractible spaces and is contractible. Both global sections have the same image as coherent transformations.

The two sections remain different as unpointed maps. Indeed p_*: Map(BG,E) -> Map(BG,BG) has a section, defined by postcomposition with the global zero section. Every loop at id_BG therefore fixes the zero component of the fiber under monodromy. The fiber components that merge in the total mapping space are precisely the monodromy orbits. The orbit of zero is the singleton zero, so the nonzero alpha section cannot merge with it. This step is necessary; distinct classes of sections alone would not have been enough.

Restriction to finite CW tests preserves the equality of coherent images, while the original unpointed maps remain distinct. Thus nonfaithfulness holds for both testing categories.

## Nonfullness

Choose d=n+1 and a nonzero k in H^{n+1}(G;M). Form the K(M,n)-fibration p_k:E_k -> BG whose obstruction class is k. One concrete construction is the fiberwise path space between the zero and k sections of EG x_G K(M,n+1) -> BG. It has no homotopy section because such a section would give a fiberwise homotopy from zero to k.

Every finite subgroup restriction has a nonempty section space, and its homotopy groups below n vanish, again by finite-group averaging. Its (n-1)-truncation is contractible. Taking the homotopy inverse limit yields a coherent presheaf section sigma of R_n(p_k).

If sigma were represented by an actual map f:BG -> E_k, then R_n(p_k f) would be homotopic to the identity. Maps into the 1-type BG are detected fully faithfully by R_n for n>=2. To justify this last statement, its space-valued restricted Yoneda presheaf is already objectwise 1-truncated. The truncation adjunction therefore identifies transformations into it with transformations for space-valued restricted Yoneda; F.7/F.8 identify those with the original mapping space. Hence p_k f is homotopic to id_BG, contradicting the nonzero obstruction k.

The same argument works after restricting sigma to finite CW tests. Merely restricting a non-realizable transformation would not on its own prove nonfullness, but the retained section equation and faithfulness for the target BG do prove it.

## Literal false positives for the two requested identities

The split example also produces endomorphisms and binary operations for which the requested equations themselves fail but their finite-height tests agree coherently. Let E = EG x_G K(M,n), with alpha nonzero in rational H^n(G;M), and let t_alpha:E -> E be fiberwise translation by the alpha section. It is a homotopy equivalence with inverse translation by -alpha. The coherent equality R_n(s_alpha) = R_n(s_0) in the slice over R_n(BG) implies R_n(t_alpha) = id. Here R_n preserves the relevant fiber product E x_BG E: objectwise its mapping-space base is the 1-type Map(A,BG), so the same relative-truncation argument applies. Products themselves are preserved as well.

The square t_alpha^2 is not homotopic to id. Composing a hypothetical equality with s_0 would equate the sections s_{2alpha} and s_0 as unpointed maps. This is impossible because H^n(G;M) is a rational vector space, hence 2alpha is nonzero, and the monodromy argument fixes the zero component. Thus T=t_alpha is a literal false positive for T^2=id at every fixed finite height n>=2.

For associativity, define m:E x E -> E by m(x,y)=t_alpha(x). The two actual composites on E^3 are t_alpha^2 composed with the first projection and t_alpha composed with the first projection. If these were homotopic, restricting along x -> (x,e_0,e_0) for a chosen point e_0 of the nonempty E and then composing with t_alpha^{-1} would force t_alpha to be homotopic to id, contradicting its action on the zero section. On finite-height presheaves, however, R_n(m) is homotopic to the first projection, so the two associativity composites are coherently homotopic as transformations. This is a statement about the coherence across the testing category; it need not assert an additional chosen operadic structure.

## Integration changes required

- Replace the former F.12 Open claim by the proved counterexample statement, with an explicit citation for the cohomological-dimension input and the arguments above.
- Change the finite-height row of the F summary table from unresolved ordinary map-class fullness/faithfulness to both false in general, retaining the countable-source exception F.11.
- Update F.13 to state that no fixed finite height provides a general equality criterion for arbitrary sources; infinity-level data do, and height two suffices for countable CW sources.
- Update F_results.csv, F_report.md, the bibliography, and integrated abstract/conclusions wherever the old open status occurs.
- Retain D.6 as unresolved: this large-source rational-cohomology argument does not settle the cardinality of [BC,S^2] for finite categories.

