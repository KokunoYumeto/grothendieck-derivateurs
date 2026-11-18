# Independent audit of the integral square detected by the null commutator

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Independent audit of the root's canonical-cobar
argument, submitted for D.2.50. The argument proves a nonzero
integral square and an integral homology pairing. It does not
prove stable sphericity of the detecting class.

## 1. Exact model and primary interfaces

Let `L=Y<7>` be the actual six-connected cover. Choose a
six-reduced simplicial model K, and put `C=C_*(K;Z)` with the
Alexander--Whitney coproduct. Thus `C_i=0` for `1<=i<=6`.
Existence is stated explicitly in Anel--Biedermann--Finster--Joyal,
*Left-exact localizations of infinity-topoi I: Higher sheaves*,
Lemma 5.4.2, proof, printed p.43 (PDF zero-index 42), opened at

<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/ABFJ.pdf>.

The source's space convention is that its n-truncation is
contractible, which agrees with six-connected here; its separate
warning about connectivity of maps causes no shift in this use.

Hess--Parent--Scott--Tonks, *A canonical enriched Adams--Hilton
model for simplicial sets*, arXiv:math/0408216v2, printed p.3,
gives the natural integral DGA quasi-isomorphism

    Omega C(K) -> C(GK).

The exact cobar differential is defined on printed p.5:

    d_Omega=d_1+d_2,
    d_1=-s^-1 d s,
    d_2=(s^-1 tensor s^-1) reduced-Delta s.

Both passages were independently reopened at
<https://arxiv.org/pdf/math/0408216>.
Thus the argument uses an actual integral loop-chain model and
the actual Alexander--Whitney cup product. It does not require an
integral minimal Adams--Hilton model or an unproved transferred
quadratic-diagonal formula. The existing bibliography key is
`FGHHessParentScottTonks2005`; simple_higher owns the new ABFJ
entry for D.2.50.

## 2. The exact cycle/cochain pairing

Choose an integral cochain A of degree seven lifting the
fundamental `a7 in H7(L;Z4)`, and write

    dA=4B,  dB=0.

The integral class of B is `b8=beta4(a7)`. Choose an integral
seven-cycle a representing the bottom homology generator, and
an eight-chain b with `db=4a`. The coefficient pairing gives

    A(a) odd,   B(b)=A(a).

Both a and b are primitive chains: a nonzero reduced diagonal
would require total degree at least fourteen. In the cobar
algebra write `x=s^-1 a` and `y=-s^-1 b`, so `dy=4x`.
They are an allowed pair for the intrinsic comparison in D.2.49.
Consequently there is a degree-fourteen chain W such that

    d_Omega W=2(xy-yx).

All tensor generators have degree at least six. Hence W has
only lengths one and two. Write its length-one term as
`s^-1 w`, with `w in C15`, and the remaining term as W2.
Comparing length one in the differential gives `dw=0`.

Define the degree-thirteen length-two functional lambda by
pairing the underlying chain factors with `A tensor B`, with
the cobar desuspension sign. It is zero except on factors of
underlying degrees `(7,8)`. The right side then has value

    lambda(2(xy-yx)) = +/-2 A(a) B(b) = 2 mod4.

The value of `lambda(d_1 W2)` is divisible by four. This can be
checked on every possible degree-fourteen word, whose underlying
degrees are `(7,9)`, `(8,8)`, or `(9,7)`. The first contribution
uses `B(d c9)=(dB)(c9)=0`; the second uses
`A(d c8)=(dA)(c8)=4B(c8)`; the third cannot contribute to the
required `(7,8)` degrees. Equivalently this is the tensor
cochain identity using `dA=4B` and `dB=0`.

The value of `lambda(d_2(s^-1w))` is, up to the irrelevant sign,
the exact Alexander--Whitney pairing `<A cup B,w>`.
It follows that

    <a7 cup red4(b8), [w] mod4> = 2 in Z4.

D.2.45 writes this product as `i(theta)`, where
`i:F2->Z4` sends one to two. Therefore

    <theta, [w] mod2> = 1.

There is no chain-choice ambiguity: D.2.49 makes the doubled
commutator intrinsic; the functional calculation uses the chosen
actual cochains; and any alternative half-product differing by
`Sq1 H14` has the same value on an integral cycle.

## 3. Integral square and remaining stable issue

L is rationally acyclic. Indeed Y is simply connected with
two-primary reduced integral homology, and removing its low
two-primary homotopy groups preserves rational acyclicity.
Thus `[w] in H15(L;Z)` is torsion. Every integral degree-fifteen
cohomology class evaluates to zero on `[w]`. The nonzero value
of theta therefore shows theta is not an integral reduction.
The integral coefficient exact sequence and D.2.45 give

    beta_Z(theta)=b8^2 != 0.

This square has exact order two since an integral Bockstein
for multiplication by two has image annihilated by two.
The mod-four lift of theta proved in the subsequent cochain
refinement `I_Hopf_transfer_test.md`, Section 6, further forces
the particular detecting integral class to have order at least
four; it cannot be a class of order one or two.

The construction supplies a cycle in C15. It supplies no
framing, stable sphere map, or nullhomotopy of the original
element h in pi14(L). Thus it does not put `[w]` in the stable
Hurewicz image. The exact criterion
`2c in image(JH_L)` of D.2.43 remains open, as does the full
ordinary fourth-suspension extension problem.
