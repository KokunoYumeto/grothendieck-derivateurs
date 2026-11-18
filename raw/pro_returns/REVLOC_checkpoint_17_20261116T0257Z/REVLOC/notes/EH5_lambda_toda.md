# The actual lambda--eta--two Toda value

**Status, 15 November 2026, 20:48 UTC: the bracket is proved zero.**
The decisive proof is Section 5. Sections 1--4 preserve the exact reduction
and the normalization issue which preceded it. In particular the formerly
undetermined bit is `d=0`. The alternate J-Moore-top choice therefore leaves
the reference BX obstruction equal to the nonzero class p; this is still a
statement about the specified source branches, not every full-source map.

## 1. Types and the exact source comparison

Use `Z=fib(Y -> K(F2,4))`, `W=Omega Z`, `F=Omega W`, and
`E=F<5>`. Let `lambda:S8 -> W` be the nonzero element of
`pi8W=pi7F=Z/2`, whose loop-adjoint mod-two Hurewicz image is `R7`.
The established target computations give `lambda eta8=0` and

    pi10W = (Z/2)^4 = <p,x,y,s>.

Here `h_Z(p)=4N`, with `N` the order-eight integral ninth homology
generator of E; the integral Hurewicz kernel is exactly `<s>`.

Section 7 of `I_k1_eleven_source.md` gives an actual quotient comparison,
which has been read in full. The map `q_M:R9 -> S8` projects to the
J-Moore top and kills the other factors. It extends to

    q_tilde:R10 -> Ceta8 = S8 union_eta8 e10

with relative top degree zero on six integral ten-cycles and one on the
distinguished cycle `K7`. This follows from the complete source Sq2 table,
not an assumed four-cell subcomplex. The ordinary cofiber sequence gives

    pi9(Ceta8)=0,
    pi10(Ceta8)=Z_(2){gamma},   h(gamma)=2[top10].

The latter group injects into the integral top-cell group: the preceding
eta map between the first and second stable stems is an isomorphism.
Consequently the BX attachment, whose boundary is exactly `2K7`, maps to
`gamma`; all other normalized eleven-attachments map to zero.

For any extension `lambda_bar:Ceta8 -> W`, changing the J-top of the
reference map by `lambda q_M` changes only its BX obstruction, by

    lambda_bar gamma in <lambda,eta8,2> subset pi10W.

Its entire Toda indeterminacy is

    lambda pi10(S8) + 2 pi10W = <lambda eta8 eta9> + 0 = 0.

Thus this is a single well-defined homotopy class. The actual three-cell
cone `Ceta8 union_gamma e11` has zero cohomology in degrees seven and nine.
Pulling back the two lower classes defining the suspended Psi detector
therefore makes that detector zero. In particular, the bracket has no
`s` component. The integral calculation below reduces it to `0` or `p`.

## 2. The basis ambiguity which cannot be discarded

In the actual stable eight-skeleton `L8` used in D.2.22, distinguish

    n = i5 nu5, of order four,
    ell0 = R eta7, of order two.

The zero-boundary nine-cycle `Q=K2+K3+K4` has second-square detector R
and zero fourth-square detector. Hence its actual attaching map is

    ell0 + 2d n,    d in F2.

The odd-nu attachment of `N-Q` can be rescaled to n. D.2.22 was entitled
to replace the abstract torsion basis by `ell=ell0+2d n`; that replacement
does not compute the actual sphere composite `R eta7`. The newly proved
vanishing of the two *other* even-nu coefficients of K1 and K5 in D.2.31
does not determine d.

An actual nullhomotopy of `ell0` can use the chain `Q-2d(N-Q)`. Its
top-degree-two coextension has integral Hurewicz

    2Q - 4d(N-Q).

Since Q has integral order two, its final image is `d p`. The zero Psi
detector above rules out adding s. Therefore the exact remaining equality is

    <lambda,eta,2> = d p.

The alternate J-top reference map has BX obstruction `(1+d)p`. This is
the historical boundary before Section 5. In particular, neither the
normalization `ell=R eta` nor the elementary exponent of pi10W may be used
to set d to zero.

There is a different bracket which the existing calculation does determine.
In E, extend `lambda:S7 -> E` over the actual R-Moore summand
`M(Z/2,7)` of L8. Its eta coextension is the class tau of D.2.22, whose
final image is the nonzero s. The defining extension/coextension model
therefore gives

    <lambda,2,eta> = {s}.

Its indeterminacy is zero: the first term is `lambda eta^2=0`, and the
second is `pi8E composed with eta8=0`. Suspending to W preserves the
calculation and its zero indeterminacy. This companion bracket is not
`<lambda,eta,2>`; a universal Chang complex has separate coextension
generators for them, so interchanging their last two entries is invalid.

## 3. An independently checked auxiliary Chang-block construction

This paragraph audits the axioms agent's separate nonzero-lower-skeleton
branch. It does not evaluate d. Desuspend its block once, so that its
three-cell core is `C1^7=cofib(2,eta5)` and its target lower core is

    D0=(M(Z/4,5) vee S6_r) union_(alpha eta5+2r) e7.

Map the Moore part `M(Z/2,5)` to `M(Z/4,5)` with bottom degree two and
top degree one, then add `r` on its top pinch. This has top six-class
`D+r=E6` and bottom `2alpha`. It extends over the eta cell because
`2alpha eta5=0`. In `pi7(C1^7)=Z gamma + Z/2 delta`, choose quotient
coordinates `q(gamma)=(0,2)` and `q(delta)=(eta6,0)`.

The target `pi7D0` is exactly `<b,c>=(Z/2)^2`, with independent second-square
vectors D and r. The gamma image is zero because its second-square vector
is zero and there is no free target seven-degree coordinate. The delta
image is `b+c`, detected by its top six-class `D+r`. Adding R on the
seven-cell changes gamma by `2R` and leaves delta unchanged. The two
additional eight-cells can then map to the target D8 cell and to the
R-Moore top, respectively. Thus this particular full block map lands in
L8. Its image in final degree-nine homotopy has zero integral Hurewicz,
and so cannot contain p. The owner still retains the complete choice
analysis; this check concerns the explicit reference construction.

## 4. Routes checked without a conclusion

The source quotient comparison was checked against the actual cofiber
sequence, including its zero indeterminacy and all eleven-cell couplings.
Recent primary Jin--Zhu tables (arXiv:2402.11226, Theorem 1.1 and Section 4)
were reopened, but they do not directly compute this specified bracket.
The canonical eta2-smash-B map has a low quadratic F7-to-R component;
using its higher nonprimitive-label images would require all James terms,
so no diagonal-only formula has been substituted for that computation.
An extended-square mapping-torus model and a finite Chang antecedent
were considered. Neither was needed in the final argument below.

## 5. The actual Hopf antecedent and vanishing of the bracket

Write `rho_T:S6 -> T` for the actual sphere of D.2.17 and
`rho_Y:S8 -> Y` for its double adjoint. Then

    h_2(rho_T)=r=b^2+{a,b}+f+ac+a^3,
    h_2(rho_Y)=sigma^2 f.

Let `h0=eta2 smash id_B:Sigma Y -> Y`, and write
`h0':Y -> Omega Y` for its once adjoint. The exact quadratic
once-adjoint calculation used in D.2.13 gives

    h0'_*(sigma^2 f)=(sigma a)(sigma c)+(sigma c)(sigma a).

Here the reduced diagonal of f is `a tensor c + c tensor a`. The linear
component is zero because h0 is zero on reduced homology. In degree eight
there can be no tensor-length-three correction, since the bottom loop
label sigma a has degree three. Thus this calculation uses the entire
James tensor algebra in that degree and does not apply a diagonal-only
rule to a higher nonprimitive label.

The right side is exactly the once-homology suspension of R={a,c}.
By D.2.19, `pi9Y=pi7T=Z/2` and its nonzero element lambda has this
nonzero detector. Therefore the following is an equality of ACTUAL
homotopy classes, not just stable classes:

    lambda_Y = h0 composed with Sigma(rho_Y).             (17)

Next D.2.19 gives the actual relation `rho_T eta6=0`. Choose an actual
extension

    rho_bar:Ceta6=S6 union_eta6 e8 -> T.

The cofiber exact sequence gives `pi8(Ceta6)=Z_(2){Gamma}` with
`h_Z(Gamma)=2[top8]`. Indeed the preceding eta map from the first stable
stem to the second is an isomorphism, and the image in the top integral
sphere group is exactly the even integers. In particular `h_2(Gamma)=0`.
Naturality of ordinary Hurewicz gives

    h_2(rho_bar Gamma)=0 in H8(T;F2).

The decisive input is the ACTUAL injectivity proved in D.2.20:

    h_2:pi8T -> H8(T;F2) is injective.

Consequently `rho_bar Gamma=0`. This is the defining extension/coextension
representative of `<rho_T,eta6,2>`, so that bracket contains zero. No stable
surjectivity, selection of a stable lift, or hidden cell normalization is
used. In fact its full indeterminacy is zero as well:
`rho_T eta6 eta7=0` and `2 pi8T=0`.

Double suspension and the actual double-loop counit identify the adjoints
of these maps and nullhomotopies. Thus zero belongs to
`<rho_Y,eta8,2> subset pi10Y`. Suspending once more, then postcomposing
with h0, gives by Toda naturality and (17)

    0 in <lambda_Y,eta9,2> subset pi11Y.                 (18)

Finally, adjunction identifies (18) with the bracket of Section 1 in W.
Its indeterminacy was proved zero there using D.2.31. Hence

    <lambda,eta,2> = {0},    d=0.                       (19)

The companion bracket `<lambda,2,eta>={s}` remains nonzero. These two
values are compatible; their entries have not been interchanged.

For the source quotient of Section 1, equation (19) means that changing
the J-Moore top by lambda changes none of the normalized eleven-cell
obstructions. In particular BX still has the exact nonzero obstruction p.
The hypotheses on the other lower data are those of the actual quotient
comparison in `I_k1_eleven_source.md`, Section 7.
