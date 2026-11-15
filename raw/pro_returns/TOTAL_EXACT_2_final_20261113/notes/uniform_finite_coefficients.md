# Uniformly finite coefficient diagrams

Status: proved restricted vanishing, not a solution of A.1 or A.2.

Let A be a nonempty connected small quasi-filtered category, and let M:A→Ab be a covariant diagram such that one integer N bounds |M(a)| for all objects a. Then T_1^A(M)=0. If A is total, then T_i^A(M)=0 for every i>0. In particular, under quasi-filteredness a prime-field column obstruction Q_a cannot have uniformly bounded finite dimension unless its affine-equalizer obstruction vanishes.

## The quotient category and filteredness

Define B to have the same objects as A and

    B(a,b) = image(A(a,b) → Hom_Ab(M(a),M(b))).

These are typed hom-sets; equal coefficient groups at different objects are not identified. Composition is composition of the displayed homomorphisms, and u:A→B is the identity on objects and surjective on every hom-set. The functor M factors as u* Mbar for Mbar:B→Ab.

Conditions I and IV pass to B: lift a span or parallel pair to A, use the respective ordinary commuting square or affine equalizer there, and apply u. For a fixed object a,

    |B(a,b)| ≤ N^{|M(a)|} ≤ N^N

for every b. The opened Isbell–Mitchell (1976), Proposition 4.5, therefore equalizes every finite ordinary parallel family out of a by an ordinary arrow. Conditions I and connectedness give common successors, so B is filtered. This uses the bounded-hom theorem on the quotient B, not on the original A.

## Comma categories and the homological comparison

For b∈B define the A-set H_b(a)=B(b,u(a)). Its category of elements is b↓u. The object (b,id_b) is weakly initial: a morphism β:b→u(a) has an A-lift f:b→a since u is hom-surjective. Thus b↓u is nonempty and connected. Under quasi-filteredness it is simply connected by the audited element-category form of I and IV. Under totality it is weakly contractible.

Here is an explicit low-degree derived comparison, so that ordinary finality is not silently used as homological finality. Take a projective bar resolution P_*→constant Z in right ZA-modules. Left Kan extension along u^op sends right representables to right representables, so

    K_* = Lan_(u^op)(P_*)

is a bounded-below complex of projective right ZB-modules. Its homology at b is the homology of (b↓u)^op, canonically identified with that of b↓u. Consequently H_0(K_*)=constant Z on B and H_1(K_*)=0. Under totality all H_j(K_*) for j>0 vanish.

The coend adjunction gives an isomorphism of chain complexes

    K_* ⊗_(ZB) Mbar  ≅  P_* ⊗_(ZA) u* Mbar.

The hyper-Tor spectral sequence for the left side has

    E^2_(p,q)=Tor_p^(ZB)(H_q(K_*),Mbar)
    ⇒ T_(p+q)^A(M).

Because B is filtered, its constant right Z-module is flat. The terms of total degree one therefore vanish: the (1,0) term vanishes by that flatness and the (0,1) term by H_1(K_*)=0. This proves T_1^A(M)=0. Under totality the spectral sequence is concentrated at q=0, giving all positive-degree vanishing. The argument does not require pointwise freeness of M.

## Precise limit of this reduction

For an F_p-valued column module Q, a uniform bound on its vector-space dimension gives the required uniform cardinal bound. Thus nonzero T_1(Q) forces unbounded dimensions as the object varies. The already constructed AKR column module has unbounded values and is not excluded.

An arbitrary prime-field diagram is not thereby covered. Passing to El_A(M^d) does give a tautological subspace diagram of dimension at most d, but a finite bar cycle in M need not lift to that element category with all its comparison relations intact. Such a lift would require a natural common tuple through all relevant arrows. The existing coefficient-pinning counterexample shows why preserving a relation after this change of category cannot be assumed. Nor is an arbitrary diagram a filtered colimit of uniformly bounded subdiagrams: the orbit span of a finite set of coefficient vectors under the A-arrows can have unbounded dimension. This is the unresolved step in trying to remove the bound.

No priority is claimed. The proof uses the opened bounded-representable theorem of Isbell–Mitchell; the additional quotient and low-degree Kan-extension argument is recorded here as a deduction.
