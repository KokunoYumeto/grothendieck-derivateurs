# The double counit and the first twelve-cell quadratic-Hopf test

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. The comparison and operation quotient below are proved.
The numerical James--Hopf value of a new stable coextension is not claimed.
The full note was independently read and passed by
`fibrations_groups`, including the join-fiber connectivity, bar
quotient, ordinary stable-range realization, and thirteen-cell caveat.

Put L=Z'=Y<7>, E=Omega²L. Thus L is six-connected and E is
four-connected, with H5(E;F2)=F2{u5}. The exact basis and operations
through degree ten are those of D.2.22 and
`FGH_D2_four_connected_cover.md`. In particular the class U2 in
degree ten is u5².

## 1. Exact connectivity of the counit

The natural evaluation map

    epsilon: Sigma²E -> L

factors as

    Sigma² Omega²L -> Sigma Omega L -> L.

For an r-connected pointed space Z, the evaluation Sigma Omega Z->Z
is (2r+1)-connected. One can see this directly from its fiber:
the homotopy pushout of two copies of the path fibration over Z is
Sigma Omega Z, and fiberwise homotopy pushout identifies its fiber
with Omega Z * Omega Z. The join is 2r-connected. This argument is
the usual first Ganea evaluation construction and uses the actual
homotopy pushout, not a homology approximation.

Apply it first to Omega L, which is five-connected. Its evaluation
is eleven-connected; suspension makes the first displayed arrow
twelve-connected. Apply it next to L: the second arrow is
thirteen-connected. Consequently

    Sigma²E -> L is twelve-connected.                    (1)

After the standard mapping-cylinder replacement, a relative CW model
therefore needs no relative cells below dimension thirteen. This
does not say that the map is an equivalence in degree twelve; it is
surjective there, and its first kernel is precisely the issue below.

## 2. The exact mod-two H12 quotient

Use the reduced bar filtration for BE=Omega L. Over F2 its first
page in filtration s is the tensor power of reduced H*(E), with
the usual multiplication differential. Every factor has degree at
least five. In total degree eleven there is only filtration one,
namely H10(E), and the only possible incoming differential is the
length-two product u5 tensor u5 -> u5². Length at least three has
total degree at least eighteen and cannot enter this calculation.
Thus the homology suspension is exactly

    H10(E;F2) / <u5²>  ≅  H11(Omega L;F2).               (2)

The next loop space has its least reduced homology in degree six.
Its first product can affect the homology suspension only in total
degree thirteen. Hence H11(Omega L)->H12(L) is an isomorphism.
Combining these statements gives the natural quotient

    H12(L;F2) ≅ H10(E;F2) / <U2>.                       (3)

The edge map is the actual double homology suspension induced by
epsilon. The same bar argument gives the required isomorphism
H6(E)->H8(L). Since Steenrod operations commute with homology
suspension, the complete fourth-square table on H12(L) is the
table on H10(E), modulo U2. The discarded class has Sq4(U2)=0
by Cartan and the connectivity of E, so this quotient is compatible
with that operation without any choice of a complement.

For example, in the notation of the established cover table,

    Sq4(T10)=E6,   Sq4(B4)=Sq4(B5)=D,

and all other degree-ten basis classes have fourth square zero.
Their double suspensions give the corresponding exact values in L.
This computes the parity of certain nu coordinates. It does not
alone identify every stable attaching component or a Hopf invariant.

## 3. Why the stable cell calculation has an actual realization here

Let L_i be the stable cell models of E used in D.2.22. After
suspending twice, their cells through L10 have dimensions seven
through twelve. Every stable attachment in this range is realized
uniquely by an ordinary attaching map: a partial complex with bottom
cell in dimension seven is six-connected, and its stabilization map
is thirteen-connected. In particular attaching spheres of dimensions
at most eleven are in the bijective range.

The resulting finite twelve-dimensional space P has a stable map
to Sigma²E and thence, by the stabilized counit, to L. Since P has
dimension at most twelve and L is six-connected, Freudenthal again
realizes that stable map by an actual map P->L. Its restrictions
on the specified lower Moore comparison agree with the desired ones
by the same stable-range uniqueness. Thus the twice-suspended
attachments of D.2.22 give genuine finite spaces and maps into L,
not merely maps to QL.

The U2 ten-cell in D.2.22 has zero attaching map, not just zero
primary detector: the complete torsion detector table there proves
that assertion. Its double suspension is consequently a free
twelve-sphere at that skeleton. A relative thirteen-cell in (1)
can remove its homology class. That does not invalidate the other
already constructed twelve-cell maps into L. A cancellation using
that free sphere can alter how a later thirteen-cell is written;
it does not turn an existing twelve-cell attachment into a different
map on the eleven-skeleton.

No claim about the higher counit relative cells is required to use
an actual stable class constructed in P: its image in L exists and
the quadratic target group is already unchanged by all cells above
dimension nine. Naturality then compares its James--Hopf value.
Conversely, a failure to find such a class in P would say nothing
about new James--Hopf images contributed by cells of dimensions
thirteen through fifteen. Sixteen-cells can change relations in
the domain group, but cannot enlarge its James--Hopf image; the
precise finite-skeleton statement is proved in Section 6 below.

## 4. The mandatory coupled nu and eta² component

The lower stable model is

    K=(M(Z4,7) vee S8_r) union_(i eta7 + 2r) e9.

Its quotient by the bottom sphere is

    K/S7 = S8_b vee M(Z2,8)_r,

and the stable connecting map to S8 is (4, eta8 q), where q pinches
the Moore summand onto S9. Thus a class in pi11(K) with quotient
(a nu8, xi) must satisfy

    4a nu8 + eta8 q(xi) = 0 in pi11(S8).                 (4)

Here q(xi) is either zero or eta9². Since eta³=4nu in the
two-primary third stable stem, an odd a necessarily occurs with
the nonzero Moore eta² coextension. An odd top-Moore nu component
cannot be attached in isolation.

This is exactly (D.2.22t5)--(D.2.22t6), shifted twice. The full group
has generators s0,z with

    pi11 K = Z8{s0} plus Z2{z},
    quotient(s0)=(nu8,eta9²),   z=r nu8,
    2s0=m,

where m is the mod-four Moore coextension with top quotient 2nu8.
These identities retain the coupling in (4); they are not inferred
from the fourth-square parity alone.

After the ten- and eleven-cell attachments, use the twice-suspended
notation of D.2.22t9--t15. The torsion group in degree eleven has
the complete detector basis

    s, z, tau, w eta10, j eta10.

The zero-boundary T12 attachment is exactly

    w eta10 + s + z,                                    (5)

and the Z12 attachment is w eta10. The eight-N cells give
2p+tau+s and 2p+j eta10; the other integral directions are exactly
the shifted D.2.22t15 table. In particular (5), whose Sq4 vector is
E8=D8+r8, uses the coupled s0 representative as well as r nu8.
The relative eta coordinates on the newly added ten-spheres and
the integral free-lattice terms must be kept in a coextension
calculation. Replacing (5) by a lone nu on the mod-four Moore top
would violate (4).

## 5. Exact remaining calculation

For a twelve-cell attached by f:S11->P11, a new stable class with
pinch a multiple of nu12 exists only if the corresponding
composition f nu11 (with that multiple) vanishes stably in P11.
The parity supplied by (3) is not this full composition test.
Once a stable lift is chosen, its target James--Hopf value must
still be computed with the coupled attachment and all lower-cell
components retained. In particular, a stable vanishing cannot be
silently replaced by an ordinary nullhomotopy: that difference is
exactly the quadratic obstruction under investigation.

The finite-layer group, its generator convention and the exact
remaining target test are in `I_quadratic_Moore_layer.md` and
D.2.43. This note proves that the twelve-cell route is legitimate
and specifies its actual input. It does not claim that 2c belongs
to, or is excluded from, the full target James--Hopf image.

## 6. An exact reduction to the actual fifteen-skeleton

This reduction was added after checkpoint 13. It is an ordinary
homotopy statement, not a presumed covariant exact sequence for
an unstable cofiber.

Choose a finite-type CW model of L with bottom dimension seven,
and write P_j for its actual j-skeleton. At the twelve-cell step,
write A=vee_i S11 and let f:A->P11 be the attaching map. The
homotopy pushout defining P12 has initial maps A->P11 and A->*,
which are respectively six-connected and eleven-connected.
Blakers--Massey therefore makes

    A -> hofib(P11 -> P12)

sixteen-connected. In degree fourteen this is an isomorphism on
homotopy groups. The homotopy-fiber exact sequence, followed by
this isomorphism, gives the exact formula

    ker(pi14 P11 -> pi14 P12)
       = sum_i im((f_i)_*:pi14 S11 -> pi14 P11)
       = < f_i nu11 >.                                  (6)

There are no extra mixed Whitehead terms in pi14(A): the first
Whitehead product of two eleven-sphere inclusions has degree
twenty-one. The notation nu11 in (6) includes its multiples in
the two-primary cyclic third stable stem.

The identical argument applies at the next three steps. At an
m-cell step, m=13,14,15, the two initial connectivities are six
and m-1, so the comparison with the fiber is (m+4)-connected.
Consequently the successive kernels in pi14 are generated by

    m=13:  f_i eta12²,
    m=14:  f_i eta13,
    m=15:  f_i and its integer multiples.                (7)

These are successively interpreted in the actual preceding
skeleton; (7) does not identify all attachments with maps into
the old nine-skeleton or discard their lower-cell choices.
The map P15->L is fifteen-connected, hence induces an isomorphism
on pi14. Thus (6)--(7), with all actual attaching components
retained, completely control the survival of the specified
class partial_K(2c) in pi14 L.

There is an equally exact formulation on the stable James--Hopf
side. Since the relative cells of P15->L have dimension at least
sixteen, pi15^s(P15)->pi15^s(L) is surjective. Since both spaces
start in dimension seven, their quadratic comparison is an
isomorphism on pi15: a relative sixteen-cell first contributes
a quadratic cross cell in dimension twenty-three. Naturality
therefore gives

    im(JH_*:pi15^s P15 -> pi15 D2L)
      = im(JH_*:pi15^s L -> pi15 D2L).                  (8)

Higher cells may impose relations on pi15^s(P15), but cannot add
an image in (8). Finiteness of P15 follows from the finite-type
CW model in this particular target; the image argument itself
does not require finiteness or any compactness assumption.

The Blakers--Massey convention is the one already used and opened
in D.2.43: Goodwillie, *Calculus II*, Section 2, pp.309--310,
especially Theorem 2.3 (bibliography key FGHGoodwillie1992).
This reduction does not compute any of the composites in (6)
or the later attachments in (7). Its purpose is to fix their
exact finite range and their ordinary-homotopy interpretation.
