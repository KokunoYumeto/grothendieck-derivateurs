# The conditional once-suspended branch: exact source data in dimension twelve

GPT-6 Astra, 15 November 2026, 20:43 UTC.

**Update, 20:51 UTC.** The actual cone comparison in
`I_lambda_toda_zero.md` proves Delta=0; it has independently passed
all three agents and root. Thus the conditional full-map branch
examined below is excluded by D.2.33. The exact source data and
partial target compatibility remain recorded, but no further
twelve-cell attack is needed for the once-suspended coefficient.

**Original scope.** D.2.33 reduces a possible full epsilon-one map to the
condition Delta=<lambda,eta,2>=p and the nonreference J-Moore top.
This note continues only that conditional branch. It gives source
homology, primary operations, and one exact third Bockstein. It
does not claim that a twelve-cell obstruction is nonzero, that the
conditional eleven-stage map extends farther, or that the main
nullification test has been settled.

Use the source labels of D.2.32, with A3,B4,C5,D6,E6,F7,X7,
G8,H8,I9,J9,L9 the suspended labels dual respectively to
u,v,u²,w,uv,u³,v²,u²v,uw,u⁴,uv²,vw. This note uses J9 for
the unit label, not the earlier order-four J7=AB+Q4A.
The source under examination is the actual quadratic extended
power D2X, X=Sigma K(F2,2). No arbitrary map is assumed to
preserve a product or a Dyer--Lashof operation.

## 1. Complete quadratic degree-twelve primary table

The weight-two dimensions in degrees9,...,13 are 5,7,9,13,18.
There is no iterated Dyer--Lashof generator in this range. The
complete degree-twelve basis and its operations are as follows.
All entries are homology operations over F2.

| Class | beta | Sq2 | Sq4 |
|---|---|---|---|
| Q7C | 0 | 0 | Q5A |
| Q8B | Q7B | Q6B+Q7A | B² |
| Q9A | 0 | Q7A | Q5A |
| AJ9 | AH | AF | 0 |
| AI9 | 0 | AF | AC |
| AL9 | AH | 0 | 0 |
| E² | 0 | 0 | 0 |
| DE | 0 | BE | 0 |
| BH | AH | BE | 0 |
| CF | 0 | AF | 0 |
| CX | CD+CE | AX+C² | AC |
| BG | AG+BF | AF+BE | 0 |
| D² | 0 | 0 | B² |

All sixth squares are zero. The source uses the ordinary
Nishida formula inside the free E-infinity algebra, while the
product rows are Cartan and the label rows are Serre's polynomial
calculation. For example

    Sq4(Q8B)=B²,       Sq2(Q8B)=Q6B+Q7A,
    Sq4(CX)=AC,        beta(CX)=CD+CE,
    Sq4(D²)=B².

The previous degree-eleven rows relevant to the new block are

    beta(CD)=beta(CE)=0,
    Sq2(CD)=AD+BC,      Sq4(CD)=AB,
    Sq2(CE)=AE,         Sq4(CE)=0.

The authored certificate `code/I_k1_twelfth_source.py` reuses the
already audited Serre/Cartan/Nishida implementation, restricts it
to arity two, and records the complete tables through degree13 in
`code/outputs/I_k1_twelfth_source.json`. Its first-Bockstein ranks
in degrees9,...,13 are 2,3,4,4,8. This is a finite algebraic
certificate, not a test of geometric realization.

For the reference lower map with its J-top toggled, the earlier
values are AC -> R8, Q5A -> 0, and B² -> 0. Thus AI9 already
requires a target degree-twelve homology class with beta=Sq2=0
and Sq4=R8 if AF is kept zero. This is a concrete next target
module test, not an established contradiction. In the ambient
E2 homology, the leading bracket combination {a,i}+{c,f}
has precisely the needed qualitative pattern; its full fiber
correction and possible target relations must be checked before
inferring anything from it.

## 2. Exact integral source groups

The reduced integral chains of X through degree nine split over
Z_(2), up to chain homotopy, into Moore complexes with homology

    Z2[3], Z4[5], Z2[6], Z2[7], Z2[8], Z8[9], Z2[9].

Here [d] denotes a bottom homology degree, not a claimed spatial
Moore decomposition. The degree-nine groups use the opened
Clément calculation; the preceding ones follow from the known
Serre/Bockstein table and UCT. Any source homology above degree
nine first contributes to D2X in degree thirteen, because X
starts in degree three.

The integral chain functor for the extended square is the signed
derived coinvariant square

    P_*(C2) tensor_(Z[C2]) (C_*(X) tensor C_*(X)).

A free-chain homotopy equivalence remains an equivariant
quasi-isomorphism after tensor square; the derived coinvariant
complex therefore preserves the indicated chain decomposition.
For a direct sum of Moore blocks, its extended square decomposes
as the sum of each block's extended square and the ordinary
derived tensor of every pair of distinct blocks. A pair with
moduli m,n contributes Z/gcd(m,n) in degrees d+e and d+e+1.
The signed single-block squares are computed by the exact
periodic C2 resolution in `I_k1_extended_power.py`, whose
integral differentials and Smith decompositions are checked.

The resulting groups are

    H8(D2X;Z_(2))  = (Z2)^2,
    H9(D2X;Z_(2))  = (Z2)^3,
    H10(D2X;Z_(2)) = (Z2)^4,
    H11(D2X;Z_(2)) = Z8 plus (Z2)^4,
    H12(D2X;Z_(2)) = (Z2)^8.

The certificate checks the UCT dimensions against the complete
mod-two basis in every overlapping degree. The H11 order-eight
summand comes from the extended square of the odd Moore-four
block in degree five. The four remaining H11 summands come from
D2 of the bottom degree-three Moore block and the distinct-block
tensors in degrees (3,7), (3,8), and (5,6). This computation
asserts integral homology of the stable extended-power summand;
it supplies no unstable attaching map by itself.

## 3. An exact third Bockstein, with chain representative

Let C have degree five, let D have degree six, and set dD=4C,
dC=0 in the odd Moore-four chain block. Write e_i for the
standard periodic C2 resolution. In the total derived-coinvariant
complex, signed interchange gives

    d e1(CC) = -2 e0(CC),
    d e0(CD) = -4 e0(CC),
    d e0(DD) = 4e0(CD)+4e0(DC),
    d e1(CD) = e0(DC)-e0(CD)+4e1(CC).

Consequently

    J11 = 2e1(CC)-e0(CD),            dJ11=0,
    d(e0(DD)-4e1(CD)) = -8 J11.

The integral class of J11 has exact order eight by the Smith
calculation above, and reduces modulo two to CD. The top chain
reduces to D². Thus the precise spectral-sequence statement is

    beta3[D²] = [CD]

in the third Bockstein page, after the first two differentials
vanish on the indicated classes. This uses only a source chain
calculation and naturality of Bocksteins for an ordinary map.

This relation does not, by itself, force a nonzero target image
of D². A homomorphism Z8 -> Z2 may send the integral CD generator
nontrivially and have an even top coefficient on its Moore map;
its top mod-two image is then zero. Equivalently, an image of CD
which is already a first-Bockstein boundary becomes zero on the
third page, which is compatible with sending D² to zero. This
is a concrete limitation of using the displayed beta3 relation
without the full target filtration.

## 4. The unresolved target comparison

The existing target calculation gives beta3[B5]=beta3[B6]=N
in E and in F. Thus the combination B5+B6 has zero third
Bockstein. Its primary values, after homology suspension to W,
are beta=0, Sq2=J1+J2+J3, and Sq4=d+e. This is compatible with
the theta coefficient required of the image of CD once the
available J2 nine-cell value is retained. Changing a nine-cell
filling by the actual J2 sphere was not excluded in D.2.33;
its eta composite is zero, so it cannot be discarded merely
by the previous eleven-cell test.

This paragraph records why the first tempting beta3 argument
is incomplete. It does not assert that B5+B6 is the image of
an actual map, does not supply its full integral order in W,
and does not assert a twelve-stage extension. The exact next
obligations are the degree-eleven fiber/degree-twelve W primary
table and the integral compatibility of the eleven-cell choices.
Those are separate from the actual target bracket Delta being
computed by the fibrations agent.

## 5. The first primary demand has an exact target solution

The AI9 row of Section 1 does not by itself obstruct the conditional
branch. Here is an actual homology class satisfying its three required
operations, with a short hand calculation.

In the established ambient T=Omega²Sigma²B notation put

    R={a,c},
    P8=i+j+l+a(f+x)+b(d+e),
    V11={a,P8}+cR.

All symbols on this display are the old B-labels in H_*T; in
particular the lowercase d,e have degree five. Let rho denote
the right H_*B coaction induced by T->B. The base Pontryagin
product is the divided-power product dual to the primitive
Serre generators. Expanding the ordinary label diagonals and
the Browder Cartan law gives

    rho({a,P8}) - {a,P8} tensor1
        = aR tensor a + R tensor c,
    rho(cR) - cR tensor1
        = aR tensor a + R tensor c.

The two terms cancel. Thus V11 is a fiber class in H11F, using
the established product-coalgebra splitting T~B times F.
This calculation requires no assumption that the unit B->T
preserves multiplication.

The label operations and Cartan give

    beta P8=0,     Sq2 P8=ac+b²,     Sq4 P8=c.

Since beta c=0, Sq2 c=a, and all positive squares of R relevant
here are zero, the Browder derivation law then gives

    beta V11=0,
    Sq2 V11={a,ac+b²}+aR=0,
    Sq4 V11=R.

In particular {a,b²}=0 in characteristic two. Homology suspension
F=Omega W -> W produces

    v12=sigma V11,   beta v12=Sq2 v12=0,   Sq4 v12=R8.

The last nonzero value proves that v12 itself is nonzero. No
Eilenberg--Moore convergence or indecomposable-injectivity assertion
is needed for that conclusion.

The finite certificate `code/I_k1_bracket_fiber.py` independently
expands all one-Browder-bracket ambient terms through degree eleven,
checks the exact coaction and the three operation values, and checks
beta squared and the Sq2 Adem identity on that sector. Its output is
`code/outputs/I_k1_bracket_fiber.json`. This is deliberately a
partial target calculation: it does not enumerate every target
class, specify an actual spherical representative, or construct a
map satisfying all the degree-twelve source relations.

## 6. Ordinary versus stable range for the next obstruction

After D.2.33 excludes the nonzero bottom-six value, the conditional
quadratic map can be made constant there and factored through its
collapse. The resulting source is six-connected. Its twelve-cell
attaching group is in the ordinary stable range.

The map lifts to the five-connected cover W' of W. This cover is
itself a loop space: it is Omega of the six-connected cover of Z.
Its first possible suspension kernel, in pi11W', is generated by
bottom Whitehead products. These vanish in the H-space W'. More
explicitly, the James pair (JW',W') has first relative group
pi12=H6W' tensor H6W', and its boundary is the bottom Whitehead
product by naturality from the bottom six-sphere. The homotopy
sequence and stability of Sigma W' therefore give

    pi11W' -> pi11 Sigma-infinity W'  is an isomorphism.

This identifies the actual twelve-cell obstruction group with a
stable group of this particular cover. It does not identify the
stable groups of W and W', or the whole mapping problem with a
stable one. Nor does it identify this group with pi10 of the
suspension spectrum of E; suspension and looping comparisons at
the next dimension have their own quadratic terms.
