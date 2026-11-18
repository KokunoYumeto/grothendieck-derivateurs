# Smash of a primary GEM with BZ/p: the candidate collapses

Status: proved, 2026-11-15. Authored by GPT-6 Astra. Main proof is
`sections/D2_smash_collapse.tex`, claim D.2.37. Root reviewed the core
argument before the manuscript write. The axioms agent independently
passed the exact theory variance, all-component group-fiber argument,
rigidification, GEM retract detection and suspension count.

## Statement and intended application

For any prime p and n >= 1, let G=K(Fp,1), B=K(Fp,n), X=G smash B.
Then Sigma²B is ordinarily X-acyclic, and minRev(X)=minRev(B).
Consequently RP² smash K(F2,2) is already in minRev(BZ/2 smash K(F2,2)).
The proposed tensoring of the BZ/2 versus RP² counterexample does not
produce a new reversible class with zero finite stable part.

The argument does not need a conclusion about ordinary acyclicity of
Sigma B, nor a calculation of the complete ordinary X-nullity class.
The two suspensions suffice for reversible closure.

## Complete proof and component repair

Ordinary acyclic classes are closed under pointed homotopy colimits,
smashing with arbitrary spaces, and finite products. For products, use
U vee V -> U times V -> U smash V and the derived mapping-space
fibration. Iterated bar constructions therefore show that every
K(Fp,n), n>=1, is ordinarily BZ/p-acyclic.

If Z is X-null, Map(B,Z) is G-null. Since B is G-acyclic,
Map(B,Map(B,Z))=Map(B smash B,Z)=*. Hence B smash B and all smash powers
of B of weight >=2 are X-acyclic. A finite fat-wedge filtration gives
X-acyclicity of B^r/(vee_r B).

**The initial unlooped argument had a real gap.** Contractibility of
Map(B^r/(vee B),Z) only controls the fiber over the constant tuple in
Map(B^r,Z)->Map(B,Z)^r. A general tuple of maps into Z need not extend
from the wedge to the product. Nothing in X-nullity alone identifies
the other components with that fiber.

Repair: replace the target by a simplicial group H equivalent to Omega Z.
It is still X-null. Restriction Map(B^r,H)->Map(B,H)^r is a simplicial
group map and Kan fibration, since the wedge inclusion is a simplicial
cofibration. Every tuple extends by ordered multiplication of the maps
on the separate coordinates. Thus it is onto components. Translation
by a chosen extension identifies every fiber with its contractible
zero fiber. Restriction is therefore a weak equivalence on all components.
Ordered multiplication need not be a group-homomorphic section; only
existence of extensions is required.

Use the strict simplicial Fp-module model of B. Let T be the opposite
of the category of finite free Fp-vector spaces. It has all matrices,
not just the maps of a Gamma semi-theory. The product projections in T
are opposite coordinate inclusions Fp -> Fp^r. Consequently

    T -> simplicial sets,   Fp^r |-> Map(B^r,H)

is a strict diagram whose weak product maps are exactly the restrictions
just proved to be equivalences. Badzioch rigidification makes it a
strict algebra over T, so its value at Fp is weakly equivalent to a
simplicial Fp-vector space. Dold--Kan and splitting over a field give

    K=Map(B,Omega Z) ~= product_{i>=0} K(V_i,i).

This equivalence respects the zero operation/basepoint. Arbitrary
cardinality of the vector spaces and disconnected K are permitted.

But Map(G,K)=Map(X,Omega Z)=*. Each positive GEM factor is a retract,
and for i>=1,

    pi_{i-1} Map(G,K(V_i,i)) = H¹(G;V_i) = V_i.

One can use the periodic resolution over Fp[t]/t^p with differentials
t and t^(p-1) to compute all H^j(G;V_i)=V_i, j>=1. Thus V_i=0 for
i>=1. The remaining discrete V_0 disappears after looping, giving
Map(Sigma²B,Z)=Omega K=*. This proves ordinary X-acyclicity of Sigma²B.

Desuspension closure puts B in minRev(X), and smash closure puts X in
minRev(B). Hence the reversible classes agree.

## Primary source opened and proof checked

Bernard Badzioch, *Algebraic theories in homotopy theory*, Annals of
Mathematics 155 (2002), 895--913. DOI 10.2307/3062135.
Primary author manuscript: https://arxiv.org/pdf/math/0110101
(version 2, containing the published paper).

- Definitions 1.1--1.2, pp.895--896: a theory with a distinguished
  product decomposition; a homotopy algebra is an actual diagram whose
  indicated product comparison maps are weak equivalences.
- Theorem 1.3, pp.896--897: rigidification to a strict algebra, with the
  homotopy-algebra structure respected. There is no connectivity or
  finite-type hypothesis.
- Notation 1.7, p.898: spaces here are simplicial sets.
- Theorem 6.4 and Lemma 6.5, pp.910--912, including the proof: the
  unit is a local equivalence for cofibrant diagrams; finite free sums,
  filtered sums, simplicial tensorings and the free resolution prove
  the Quillen equivalence.

The variance is essential: we use (finite free vector spaces)^op,
and the actual functor sends a matrix B^r -> B^s to precomposition
Map(B^s,H) -> Map(B^r,H). Its theory projections are coordinate
restrictions. Treating the same construction as merely a special
Gamma-space would prove only an infinite-loop-space conclusion, which
would not suffice for the positive-homotopy detection above.

## Scope

No assertion is made that arbitrary maps B^r -> Z split over a wedge,
or that an arbitrary infinite-loop space is a GEM. Both statements
would invalidate the proof. The H-group target and the full Fp-linear
theory, respectively, are the exact repairs. The proof is uniform at
odd primes: it only uses Fp-linearity and the group cohomology of Cp.

The stable-part comparison motivating the candidate is unchanged:
loc(Sigma-infinity BZ/2)=loc(S/2), and Sigma-infinity B is two-primary,
so both BZ/2 smash B and RP² smash B generate the same stable ideal
as B. The theorem establishes more: their proposed reversible
separation already fails on the source-class level.
