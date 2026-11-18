# Residual first-cone coefficient after D.2.16

GPT-6 Astra (OpenAI / ChatGPT Pro), 2026-11-15.

This is a direct calculation toward the ordinary nullification problem,
not a proof of first-cone cup-product vanishing or of nullification survival.
The exact eta attachment is excluded by D.2.16, but the following common
coefficient remains after the low-dimensional primary constraints.

## 1. The all-map low-degree consequence

Put B=K(F2,2), X=Sigma B, A=QX, Y=Sigma^2 B and T=Omega^2 Y.
Use labels a,b,c,d,e,f,x in H_*(B;F2) dual respectively to
u,v,u^2,w,uv,u^3,v^2, where v=Sq1 u and w=Sq2 v. Their images
in T have those same names. In H_*(X), and subsequently in H_*(A),
write A0=σa, B0=σb, C=σc, D=σd, E=σe and X7=σx.

For an arbitrary ordinary map g:A -> T, restriction to C4 X and
D.2.16 kill the coefficient of xi a in g_*(C). In fact g_*(C)=0.
The primitive subspace in target degree five is

    span{xi a, d, e+ab}.

Bockstein naturality kills the e+ab coefficient, since βC=0 and
β(e+ab)=a^2. Sq2 naturality kills the d coefficient: Sq2 C=A0,
g_*(A0)=0 (its only possible target is b, with nonzero βb=a), and
Sq2 d=b. Thus the xi coefficient was the last possibility.

The source identity Sq2 X7=C now implies that the xi b coefficient
of g_*(X7) is zero. The only target degree-seven class whose Sq2
has an indecomposable xi a coefficient is xi b itself, with Sq2 xi b=xi a.
Finally βX7=D+E. Only xi b can contribute the pure bracket
k={a,b} to a degree-seven Bockstein. Consequently the coefficients
of k in g_*(D) and g_*(E) must be equal.

This permits a common coefficient epsilon. The eta adjunct has the
unequal pair (0,1), so it is excluded; the low primary calculation does
not exclude the pair (1,1).

## 2. Complete primitive-space check

The degree-six primitive subspace is

    span{b^2, k={a,b}, p3=f+ac+a^3}.

The third class really is primitive. In its reduced diagonal the
terms a tensor c and c tensor a cancel, and so do a^2 tensor a and
a tensor a^2. Its Bockstein is zero, and Sq2 p3=a^2.
Thus no argument may silently omit p3.

In degree seven, put g7 dual to u^2 v and h7 dual to uw. A primitive
basis is

    xi b, {a,c}, P=g7+ae+bc+a^2b, Q=h7+ad.

Here βP=p3, βQ=0, Sq2P=Sq2Q=e+ab and Sq3P=a^2.
These formulas and the primitive bases were independently checked by
the axioms agent. They give only equality of the two k coefficients,
not their vanishing.

Equivalently, if K in H^6(T;F2) is the polynomial-basis functional
dual to k, then on the unit X the possible pullback is

    j^*g^*K = epsilon σ(w+uv).

The exact target identities Sq1K=V and Sq2U=V, where U and V are
dual to xi a and xi b, explain the equality: D.2.16 makes g^*U=0
in degree five, hence g^*V=0 and Sq1(g^*K)=0. On X, both Sq1w
and Sq1(uv) equal v^2.

## 3. Integral meaning of the residual class

Mahowald, *On the normal bundle of a manifold*, Pacific J. Math.
14 (1964), 1335--1341, Section 2.3, p.1336, proves

    rho2 beta4 P(z) = Sq^(2k) Sq1(z) + z Sq1(z),   |z|=2k,

where P is the Pontryagin square with coefficients Z/4 and beta4
is the integral Bockstein. The proof uses the integral cup-one
coboundary, not a heuristic Bockstein identity. In the proof of
Lemma 6.1, p.1340, Mahowald identifies H^5(K(Z/2,2);Z)=Z/4 and its
generator beta4 P(u). Both pages were inspected in the original scan:

<https://msp.org/pjm/1964/14-4/pjm-v14-n4-p20-p.pdf>.

Thus

    w+uv = rho2 beta4 P(u)

is the reduction of the actual order-four integral generator. This
identifies the residual possibility but does not kill it. A class that
is not integrally liftable on the target can have an integrally liftable
pullback; naturality alone does not reverse that implication.

For higher-Bockstein bookkeeping, β1X7=D+E, so [D+E]=0 on the
second page. The possible order-four differential is on the common
class [D]=[E], not on [D+E]. The target identity β2[b^2]=[xi a] is now proved by the integral
configuration-chain calculation below. Naturality with g(C)=0 constrains
the coefficient of b^2+k. It does not by itself kill the chain-level
common bracket coefficient, because b^2+k=β1(xi b).

## 4. Current boundary

No assertion has been made that the product of the lifted degree-four
and degree-five target classes vanishes after an arbitrary first
simultaneous attachment. One must still analyze the common epsilon
above, attachments from other suspension exponents, and the dependence
of the relevant Hopf invariant on choices of lifts. The new D.2.16
argument does settle the actual eta extension for all choices; it does
not automatically settle these separate questions.


## 5. Verified integral second Bockstein

The axioms agent found the following explicit chain calculation, and I
independently checked all signs. It sharpens the earlier circle-cover
argument. Take the bottom Moore inclusion M=P^3(2) -> B. Its reduced
integral cellular chains have generators a in degree2 and b in degree3,
with db=2a. The arity-two configuration circle has free transposition
cells e0,e1 and differential de1=(tau-1)e0. In its coinvariant tensor
with the two Moore labels, the transposition uses Koszul signs:

    tau(a tensor b)=b tensor a,    tau(b tensor b)=-b tensor b.

Set

    x=e0(b tensor b), h=e1(a tensor b), z=e1(a tensor a).

The total differential gives

    dx = 2(e0(a tensor b)-e0(b tensor a)),
    dh = e0(b tensor a)-e0(a tensor b)-2z,
    dz = 0.

Consequently d(x+2h)=-4z. The corrected chain x+2h has the same
mod-two reduction as x, namely the Pontryagin square b^2. Its boundary
divided by four reduces to xi a. Naturality along the free E2 map
C2 M -> C2 B ~ Omega^2 Sigma^2 B proves

    beta2[b^2] = [xi a].

Moreover d(e1(b tensor b))/2 reduces to b^2+k, where
k={a,b}; hence beta1(xi b)=b^2+k and [b^2]=[k] on the second
Bockstein page. Thus beta2[k]=[xi a] has the same meaning there.
The mod-two target basis already shows that xi a is not a beta1
boundary. This is not a claim that the uncorrected chain x has boundary
divisible by four; the correction 2h is essential.

No integral arity-one correction interferes in the relevant dimensions:
the Moore label space has cells only in degrees two and three, whereas
x,h,z are in degrees six,six,five. The configuration model and the
connected-label equivalence to the double loop suspension are the free
E2 inputs used throughout D.2.13--16.

## 6. What the second Bockstein does and does not remove

Write s for the a^2 coefficient of g(B0), and epsilon for the common
bracket coefficient of g(D),g(E). The exact primitive/Steenrod relations,
followed by the second Bockstein, give

    g(D) = epsilon(b^2+k) + (s+epsilon)p3,
    g(E) = epsilon(b^2+k+p3).

Here the source common Bockstein class [D]=[E] maps by beta2 to C,
whose image is zero. Hence the coefficients of b^2 and k agree.

On homology suspension into Omega Y, b^2 disappears, k becomes the
old tensor commutator, and p3 becomes the old linear f-label. If s=0,
the bracket coefficient agrees with that linear coefficient, so these
classes do not give a pure commutator boundary. The combination
s=epsilon=1 remains potentially dangerous: it has one image with a
pure commutator and another with commutator plus linear f-label.
This does not prove that a map realizing those coefficients exists.
It also does not yet eliminate it. The other suspension exponents and
later attachment stages remain separate issues.
