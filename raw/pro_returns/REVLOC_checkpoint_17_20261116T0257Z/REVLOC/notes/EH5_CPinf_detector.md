# CP-infinity detects every nonzero E1 ring

Recorded 2026-11-15, 16:15 UTC. The complete manuscript proof is
`sections/D2_CPinf.tex`, claim D.2.15, following the eta-zero detector
and exact local-unit criterion in D.2.14. Root and the axioms/derivators
agent independently reviewed every interface below and accepted the proof.

## Result and consequence for the assigned finite-part question

For reduced D = Sigma-infinity CP-infinity and every unital E1 ring R,

    F(D,R)=0 implies R=0.

Consequently loc(D)=Sp. For every prime p, including 2,

    loc(Sigma-infinity B(C_{p^infinity}))
      = loc(D smash S/p)
      = loc(S/p).

Thus the degree-one divisible candidate has the full finite p-primary
thick part. It does not provide a stable ideal with zero finite part.
No assertion about the general fixed-stable-part size problem or the
strict reversible interval follows from this computation alone.

## The eta-zero input and its exact coefficient scope

The S1-equivariant Euler sequence, twisted by the negative standard
complex representation and passed to homotopy orbits, gives

    S^{-2} -> Th(-L) -> Sigma-infinity CP-infinity_+ -> S^{-1}.

The first map is an actual Thom-fiber inclusion. If F(D,R)=0 and eta_R=0,
the shifted unit S^{-2}->Sigma^{-2}R extends across Th(-L): its only
obstruction is detected on the basepoint sphere and lies in the image
of pi1S. The Thom colimit adjunction makes the extension a natural
transformation of left R-module local systems, an equivalence on the
chosen fiber and hence on every fiber because CP-infinity is connected.
Pointwise left/right module duality trivializes the positive line.
Taking its Thom colimit gives D->Sigma²R restricting to the unit on
the bottom S². D-nullity forces that unit to vanish, so R=0.

This is valid for E1, not just E-infinity, rings. It neither assumes a
commutative Picard category nor infers Eilenberg--Moore convergence.

## The reduced transfer forces nu to vanish at 2

Split CP-infinity_+ stably as S wedge D. Write t:D->S^{-1} for the
reduced part of the last map in the Euler--Thom sequence, i:S²->D for
the bottom inclusion, and b=Sigma(ti):S³->S. There are fiber maps

    fib(ti) -> fib(t) -> fib(delta)=Th(-L).

All are isomorphisms in mod-2 cohomology degrees -2 and 2. This follows
from the long exact sequences: the source maps S²->D->S wedge D are
isomorphisms in degree 2 and have no negative cohomology, while the
common S^{-1} target supplies degree -2 in the fibers. The extra
sphere summand contributes only degree 0.

For the Thom class u of degree -2, the Thom identity says

    Sq^4(u)=w4(-L)u=x²u != 0,
    w(-L)=(1+x)^{-1}, x=c1(L) mod2.

One can prove the virtual formula over CP² using a finite complement
to L in a trivial complex bundle, the ordinary Thom identity, and
desuspension. Pull back along the fiber maps. Since
fib(ti)=Sigma^{-2}C(b), the bottom-to-top Sq4 of C(b) is nonzero.
Thus b has mod-2 Hopf invariant one, so b=k nu in pi3S_(2)=Z/8 with
k odd. No normalization or sign of the transfer is needed.

For a derived 2-complete D-null ring, the reduced transfer is null
after composing with the unit. Hence k nu_R=0, and odd integers are
invertible, so nu_R=0.

## The finite endomorphism ring removes eta

Put M=R smash Ceta, a left R-module. The actual eta action on Ceta
factors through its top quotient S³, then nu:S³->S, then its bottom
inclusion. Thus nu_R=0 makes eta_M=0. The sphere-level action eta_Ceta
is itself nonzero; no universal finite eta-annihilator is asserted.

For A=End_R(M), finite duality gives the underlying spectrum

    A = (Ceta)^vee smash R smash Ceta.

The D-null class is stable and closed under finite colimits and
retracts, so A is D-null. Its eta unit class is the R-linear action
eta_M and therefore vanishes. The eta-zero E1 detector makes A=0.
Its unit is id_M, whence M=0. Now eta:Sigma R->R is an equivalence,
but eta^4=0 in the stable sphere, so R=0.

For an arbitrary D-null E1 ring, form its derived 2-completion
F(C,R), where C=fib(S->S[1/2]). Completion is monoidal, preserves
the E1 structure, and preserves D-nullity because loc(D) is a tensor
ideal. The completed ring is zero by the preceding argument.
Completion preserves the mod-2 cofiber, so R/2=0. Multiplication by
2 is therefore invertible, eta_R=0, and the eta-zero detector again
gives R=0.

## Actual localizing membership

The single-generated tensor ideal loc(D) has an accessible monoidal
localization. Its local unit L(S), viewed back in spectra, is a
D-null E-infinity ring. The detector makes it zero, so S belongs to
loc(D), which is therefore all spectra. This does not require the
localization to be smashing.

Smashing a localizing construction of S from D with S/p gives
S/p in loc(D/p). The reverse inclusion is immediate. Finally the
Pruefer-to-circle mod-p comparison and the p-inversion telescope,
proved fully in D.2.14, identify loc(Sigma-infinity B(Cp-infinity))
with loc(D/p).

## Primary-source ledger

1. Ando--Blumberg--Gepner--Hopkins--Rezk, 2014,
   <https://www.math.columbia.edu/~thaddeus/blumberg/5.pdf>.
   Opened Definitions 2.20/2.22, Theorem 2.24, Corollary 2.26.
   Supplies the Thom colimit adjunction and the full fiberwise
   orientation criterion. E1 left/right dualization is explicit in
   our proof and was independently checked.

2. Madsen--Schlichtkrull, *The circle transfer and K-theory*,
   <https://data.math.au.dk/publications/pp/1999/imf-pp-1999-17.pdf>.
   Opened first displayed fibration in Section 1. Our exact shift
   and actual Thom-fiber inclusion are additionally derived from the
   equivariant Euler sequence, avoiding convention ambiguity.

3. Milnor--Stasheff, *Characteristic Classes* (1974),
   <https://www.maths.ed.ac.uk/~v1ranick/papers/milnstas.pdf>.
   Original 13.2 MB scan downloaded and read because web extraction
   rejected its size. Section 8, Definition 8.2, printed pp.90--93;
   the precise Thom identity is on printed p.91 / PDF page93.
   The Whitney formula proof follows on pp.92--93. Original scan
   and reading image were moved to the excluded source directory;
   they are not part of deliverable archives.

4. J. F. Adams, *On the groups J(X)--IV* (1966),
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Adams-JX4.pdf>.
   Opened Example 7.17, printed pp.45--46, and Section 8,
   especially equation (8.1). The former gives pi3S=Z/24; the latter
   identifies the mod-2 Hopf invariant through the cofiber Steenrod
   square. Only its parity at 2 is used.

5. Angeltveit--Rognes, *Hopf algebra structure on topological
   Hochschild homology* (2005),
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/angeltveit-rognes.pdf>.
   Equation (8.4), printed p.1279 / PDF page57, is the exact eta_Ceta
   factorization through nu. Lemma 8.11 proof, printed p.1285 /
   PDF page63, explicitly uses eta^4=0. Both independently reopened
   by root. The manuscript also rederives the weaker factorization
   needed from the low-stem exact sequence.

6. Lurie, *Higher Algebra*, Example 2.2.1.7 and Proposition 2.2.1.9.
   Already opened and documented in `FGHLurieHA`. These give the
   monoidal localization and lax-monoidal inclusion used for the
   local unit and derived completion. No smashing assertion is used.

## Historical scope check

Hovey--Palmieri, *The structure of the Bousfield lattice*,
<https://arxiv.org/pdf/math/9801103>, discussion preceding Conjecture
8.7, reports Hopkins's proof that the smash Bousfield class of CP-infinity
is the sphere class. The paper then labels the claim a conjecture because
the authors did not know its proof. We make no novelty claim. The proof
above independently establishes actual localizing generation and does not
assume their general Section9 comparison conjecture.

Bousfield1997, <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf>,
Lemma10.4 and the following paragraph, printed p.1346, concern positive
finite transition height n and (E/p)_*K(Z,n+1)=0. At n=1 our result excludes
that CP-infinity smash-acyclic possibility. No conclusion for n>=2 is
asserted. Thus the old source discussion and the later Hopkins report
are consistent with the present computation.
