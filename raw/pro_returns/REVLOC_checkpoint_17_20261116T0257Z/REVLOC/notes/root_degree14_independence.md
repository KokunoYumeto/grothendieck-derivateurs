# Three exact degree-fourteen tests in the actual fiber

Root calculation, 16 November 2026, 00:14--00:18 UTC.
This advances the actual integral-cover spectral-sequence calculation;
it does not by itself decide the integral square or stable Hurewicz image.

## 1. The actual retraction and its low projection

Use B=K(F2,2), Y=Sigma²B, T=Omega²Y, and the three-connected
fiber F from D.2.18. The proved space equivalence B x F -> T
is (b,f) |-> j(b)f, with j the double-suspension unit and product
in T. Choose its homotopy inverse and write r:T->F for the second
projection. It is an actual map of spaces, so it commutes with
diagonals and Steenrod operations; it need not be an H-map.

In H*(B;F2)=F2[u2,v3,w5,t9,...], v=Sq1 u, w=Sq2 v,
t=Sq4 w. Use homology labels

| label | dual monomial |
| --- | --- |
| a2 | u |
| b3 | v |
| c4 | u² |
| d5 | w |
| e5 | uv |
| x6 | v² |
| g7 | u²v |
| h7 | uw |
| i8 | u⁴ |
| t9 | the generator t9 |
| s10 | w² |

The reuse of t9 as a dual homology label follows the existing code;
degrees and the displayed duality distinguish it from the generator.
Products of labels denote the Pontryagin product in T, never the
product of homology labels inside the base B.

The complete H7(F) basis is V=xi b, R={a,c},
P=g+ae+bc+a²b, Q=h+ad. Also A4=a² and z5=e+ab are fiber classes.
The actual product equivalence implies

    r_*g=r_*h=0,
    r_*(a²b)=0,
    r_*(ae+a²b)=0.

The first line is the section, the second is the mixed class b A4,
and the third is the mixed class a z5. Consequently r_*ae=0,
r_*bc=P and r_*ad=Q. On the polynomial part of H7(T),
r^*P* detects bc, r^*Q* detects ad, and r^*V* is zero.
For completeness that polynomial part has basis g,h,ae,bc,ad,a²b;
the remaining H7(T) directions are V,R and the mixed class a xi a.
In degree four r_*a²=A4 and r_*c=0.

## 2. Three actual test classes

Set

    ZP=r_*(x6 i8),  ZQ=r_*(c4 s10),  ZR=r_*(d5 t9) in H14(F;F2).

These definitions use actual homology classes and the actual
retraction. No unproved normal form for H14(F) is needed.
Let theta1=V*+P*, theta2=P*+Q*, and
S=Sq6 Sq3 Sq1(A4*) in H14(F;F2).

Dual Frobenius (the diagonal coefficient dual to cup-square) sends
x i to bc and c s to ad. Indeed Delta x has the equal middle term
b tensor b, Delta i has c tensor c, Delta c has a tensor a, and
Delta s has d tensor d. Both d and t are primitive labels; their
product has no diagonal term in bidegree (7,7). It follows that

    <theta1²,(ZP,ZQ,ZR)> = (1,0,0),
    <theta2²,(ZP,ZQ,ZR)> = (1,1,0).

Here the squared cohomology functionals are pulled back under r;
the low projection above, not a purported multiplicativity of r,
is what identifies their evaluations on the T diagonal.

## 3. The reverse Steenrod chain, by hand

Evaluation of S reverses the operation order, so we apply
Sq_*6, then Sq_*3, then Sq_*1 to each test representative in T.
All formulas below follow from Serre's polynomial algebra,
instability, and Cartan, as in D.2.17--D.2.20.

For x i, the only contribution to Sq_*6 is
(Sq_*2 x)(Sq_*4 i)=c². In detail Sq_*1 x=d+e,
Sq_*2 x=c, Sq_*3 x=b, whereas Sq_*5 i=Sq_*3 i=Sq_*6 i=0.
Every odd homological square of a product square is zero by Cartan;
therefore Sq_*3(c²)=0.

For c s, the only contribution is
(Sq_*2 c)(Sq_*4 s)=a x. The identities are
Sq2 u=u² and Sq4(v²)=w²; Sq_*6 s=0 by instability of
the possible source u². Then Sq_*3(a x)=a b, using
Sq3 v=v², and Sq_*1(a b)=a², using Sq1 u=v.

For d t, the only contribution is
(Sq_*2 d)(Sq_*4 t)=b d. These use Sq2 v=w and Sq4 w=t.
Then Sq_*3(b d)=(Sq_*1 b)(Sq_*2 d)=a b, and
Sq_*1(a b)=a². No other summand is allowed by the known
generator formulas and instability.

Naturality with r and r_*a²=A4 now gives

    <S,(ZP,ZQ,ZR)>=(0,1,1).

Thus the complete matrix, with test classes as rows and
(theta1²,theta2²,S) as columns, is

    [[1,1,0], [0,1,1], [0,0,1]].

It has determinant one over F2. All three cohomology classes
are nonzero and linearly independent. In particular any three
classes in the actual cover Z whose double cohomology
suspensions are these classes must also be independent.
The identification of those classes is a separate naturality
step in the integral-cover calculation; no injectivity of a
general Postnikov projection is assumed here.

## 4. Reproducible finite certificate

`code/D2_degree14_pairing_check.py` imports the previously audited
Serre/Cartan implementation, adds every monomial label through
degree fourteen, and checks both the full diagonal evaluation
and all three intermediate reverse Steenrod operations. Output:
`code/outputs/D2_degree14_pairing_check.json`.
The code is an algebraic certificate for the displayed finite
calculation. The geometric split and the low projection identities
are justified above and in D.2.18, separately from the code.

## Independent reviews

The simple/higher and fibrations/groups agents separately checked the
actual projection identities, all three reverse Steenrod chains, and
the diagonal pairing matrix. Both returned PASS. The root ran the
exact certificate successfully; it reports rank three and the matrix
displayed above. No integral extension conclusion was included in
either review.
