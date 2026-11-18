# Independent audit of the entire-unit linear obstruction

15 November 2026. AI-produced by GPT-6 Astra (OpenAI).

**Status: passed.** This note independently verifies D.2.36 and its
Moore-restriction consequence. It does not assert that the remaining
paired relative coefficient vanishes.

Write

    H* K(F2,2) = F2[u2,v3,w5,t9,s17,...],
    v=Sq1u, w=Sq2v, t=Sq4w, s=Sq8t.

An actual map Sigma5 B -> Sigma2 B induces a degree-minus-three
Steenrod-linear map phi on reduced cohomology. No multiplication
compatibility for phi is used. Suppose phi(u^3)=v.

The first five Cartan identities are

    Sq4 u^2=u^4;
    Sq3(uv)=uv^2+vw;
    Sq2 u^3=u^4+uv^2;
    Sq6 v^2=v^4;
    Sq4(vw)=vt+v^4.

Because phi(u^2) has degree one, phi(u^4)=0. The third identity gives
phi(uv^2)=w. The second then gives phi(vw)=w, since Sq3 of the
degree-two value phi(uv) is zero. Similarly Sq6 phi(v^2)=0 by
instability, so phi(v^4)=0. Hence phi(vt)=t exactly.

The remaining identities are

    Sq10(uvw)=u^2 v^2 w^2;
    Sq9(ut)=ut^2+vs;
    Sq8(vt)=vs;
    Sq4(uwt)=ut^2+u^2 v^2 w^2.

The first gives phi(u^2 v^2 w^2)=0, because phi(uvw) has degree
seven. The second gives phi(ut^2)=phi(vs), because phi(ut) has
degree eight. The third gives phi(vs)=s. The last would therefore
give Sq4 phi(uwt)=s. But phi(uwt) has degree thirteen, which has
no algebra generator, and Cartan preserves decomposables. This is
impossible. Thus phi(u^3)=0.

The exact generator identities used above were also checked:

    Sq1 w=v^2; Sq2 w=Sq3 w=0;
    Sq1 t=w^2; Sqj t=0 for 2<=j<=7;
    Sq8 t=s; Sq9 t=t^2.

They follow from the indicated definitions, Adem, instability, and
Cartan. In particular the non-top term in Sq4(uwt) is precisely
Sq2u Sq1w Sq1t = u^2 v^2 w^2.

There is no auxiliary prescribed coefficient hidden in this proof.
Indeed phi(v^2)=phi(Sq2 u^2)=0 automatically. Since H6B has basis
u^3,v^2, the ordinary map is zero on H8. The unit Sigma B -> QSigma B
is an isomorphism on H4, so restriction proves the same statement
for every Sigma4 QSigma B -> Sigma2 B.

For the double adjunct, the primitive degree-six basis in T is
b^2,k,p3. Double homology suspension detects only the p3 coefficient;
it is therefore zero. Sq2 of the source class is zero, while
Sq2 b^2=a^2 and Sq2 k=0. Consequently the only possible degree-six
image is epsilon k. This verifies the exact strengthened statement
in the final TeX, not only the exclusion of one chosen unit map.

## Moore restriction and the remaining finite test

Let M=M(Z/2,3) be the bottom Moore subcomplex of Sigma B and let
U=Omega4(Y<7>). The actual groups pi3U=Z/4{alpha} and
pi4U=Z/4{rho} give the Moore Puppe sequence

    0 -> coker(2 on pi4U) -> [M,U]
      -> ker(2 on pi3U) -> 0.

Both displayed nonzero groups have order two. For a fixed bottom
value, the nontrivial top action is rho followed by the top pinch;
its doubly suspended mod-two homology value is
r=b^2+k+p3. Thus the entire-unit linear vanishing removes that
top toggle. A dangerous map, with commutator coefficient one,
has exactly the canonical Moore restriction, up to homotopy.

One may consequently restrict a putative full map to C4M and compare
with the canonical E4 extension of that Moore map. Its ordinary
difference factors through C4M/M, lifts to the five-connected cover
V=U<6>, and yields the finite stable arity-two test recorded in
EH5_k4_relative_square.md. This controls the scope: no identification
of the entire infinite unit is required.

The finite top is a noncycle for the first Bockstein. Its possible
paired coefficient cannot be dismissed by the existing spherical
diagonal variation or by an unspecified integral cohomology lift.
The value of that relative test remains unresolved here.

## Audit references

The original Serre calculation and CLM operation conventions are the
same primary sources cited and opened in D.2.36 and D.2.29. This is an
independent hand verification of the nine displayed identities and
their topological interfaces. Root's exact linear algebra certificate
is code/D2_k4_linear_module.py with its retained degree-24 output;
the argument above does not rely on the numerical certificate alone.
