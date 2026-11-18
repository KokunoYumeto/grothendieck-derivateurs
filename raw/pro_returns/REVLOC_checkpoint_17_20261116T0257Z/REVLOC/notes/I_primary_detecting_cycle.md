# A geometric half-product detector with no primary-square obstruction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Complete proof: `sections/D2_primary_undetectability.tex`,
claim D.2.52. Stable sphericity remains open.

## Actual construction

D46 and D49 give h=n(alpha sigma' +(Et)nu11) for some integer n.
Use the actual Moore map mu:M(Z4,7)->L and its normalization
mu delta=h, delta=partial(2c4). Attach a fifteen-cell to

    P0=M(Z4,7) vee S7 vee S11

by the sum delta - n sigma' - n nu11. The given three maps into L
extend over this finite actual cone P. Its top integral cycle w
defines omega in H15L.

There is an actual cofiber map

    P -> C(delta) vee C(-n sigma') vee C(-n nu11)

induced by the domain pinch S14->vee3 S14. Each top relative
degree is one. The pullbacks of a7 and red4 b8 are respectively
a_M+a_S7 and b_M. Cross products vanish in the target wedge.
The Stiefel cone comparison c24(l4)=delta gives mixed coefficient
two on C(delta), so omega has theta evaluation one. Its order
is at least four by the explicit mod-four lift of theta in D50.

## The exact suspension-image input

D31 identifies pi11Y with the F2-basis p,s,x,y. The once-adjoint
Hurewicz images of x,y in the James tensor algebra of Omega Y are
af+fa and aab+baa, of lengths two and three; p,s have zero image.
The adjunct of a suspended class Et is the James unit composed
with t, so its homology has length one. Thus Et belongs to <p,s>.

For the connected cover, D22 identifies the integral Hurewicz
images in E=Omega²L as h(p)=4N', h(s)=0, N' of order eight.
Their mod-two images already vanish there. Two homology
suspensions therefore give zero ordinary mod-two H11L image.
This argument deliberately does NOT identify sigma²(4N')
integrally or say it vanishes integrally.

## Primary operations and the exact remaining gap

P has H13=H14=0 mod two, and its only H11 class is the S11
summand. Hence Sq_*1 and Sq_*2 of its top class vanish; Sq_*4
maps into the S11 line, whose image in L is zero. Sq_*8 vanishes
by instability on dual degree-seven cohomology. The power-of-two
generators of the Steenrod algebra then annihilate omega mod two
under every positive operation.

Therefore theta is not in Sq1H14+Sq2H13+Sq4H11, which is the
entire positive-operation image in degree fifteen. This settles
the bounded primary test. It does not settle higher/integral
differentials of the stable Hurewicz AHSS. The top cycle of P
does not automatically lift to its stable homotopy: the stable
nu and twice-sigma attaching components were retained.

Root independently passed the actual cofiber-pinch/cup argument.
Fibrations independently passed the suspension-image containment,
the connected-cover mod-two interface and the primary conclusion.
The axioms agent passed the full final section, including the actual
cofiber map, all component Hurewicz interfaces, and the coefficient
calculation. The Stiefel-cone citation was corrected to the directly
opened Morisugi--Mukai source, p523; the coefficient proof is included
in the manuscript rather than left to that citation.

## A bounded next relation for the integral stable test

There is an additional exact low-degree relation, independently
checked by the fibrations agent. Double homology suspension is onto

    sigma²:H11(E;F2)->H13(L;F2),   E=Omega²L.

For the first reduced bar construction BE=Omega L, all factors have
degree at least five. In total degree twelve the only possible
length-two class is u5 tensor u5. Its first differential is the
nonzero class u5² in H10(E), so no length-two class survives there.
All higher lengths have total degree at least eighteen. Hence
H12(Omega L) is a quotient of sigma H11(E). In the second bar
construction, factors have degree at least six and length two
starts in total degree fourteen; thus H13(L) is a quotient of
sigma H12(Omega L). These are the actual homology suspensions.

Dually, sigma² is injective in degree-thirteen cohomology.
The mod-two reduction of a7 suspends twice to the bottom u5 dual,
so instability gives

    Sq6(red2 a7)=0.

The exact cover table has Sq4_*N=u5 and zero fourth square on
every other degree-nine class. Therefore the dual N11 class in
L is Sq4(red2 a7). Since Sq1(red2 a7)=0, the Adem relation gives

    Sq2(N11*)=Sq6(red2 a7)+Sq5 Sq1(red2 a7)=0.

The earlier counit range also shows that sigma²:H9(E;Z)->H11(L;Z)
is an isomorphism, so the integral Hurewicz class of the lifted p
is the nonzero order-two element sigma²(4N') in the Z8 summand.
This is relevant to the possible nu coefficient in a stable d4.
No sphere-AHSS differential or incoming indeterminacy is inferred
solely from these primary statements; fibrations owns that audit.

### Exact bar-source audit, 16 November 2026, 01:23 UTC

Opened and read Ib Madsen and R. James Milgram, *The Classifying Spaces
for Surgery and Cobordism of Manifolds* (1979), Chapter 1, Theorem 1.5
and its footnote, printed page 7 (PDF page index 14):
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/madmil.pdf .
The theorem identifies the contractible total bar construction and its
principal quasifibration; the footnote gives the natural length filtration,
whose field-coefficient E1 complex is the algebraic bar construction on
the Pontryagin homology algebra. These are precisely the model and
filtration used above. For connected loop-group models, the resulting
classifying spaces are the indicated deloopings. The filtration-one edge
map is the actual homology suspension, from the inclusion of the first
bar stage. In the two degree ranges used above there are finitely many
possible filtration terms, so convergence introduces no completion issue.

The independent fibrations audit passed both the degree-thirteen
surjectivity and the separate integral degree-eleven isomorphism.
The latter also follows directly from the 12-connected double counit
proved in `I_counit_twelve_cells.md`, so it does not depend on an
integral collapse assertion for this field-coefficient bar spectral sequence.
