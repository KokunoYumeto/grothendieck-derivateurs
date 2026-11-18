# Strengthening of C.16 — independently audited and integrated as C.17

The integrated C.16 was frozen for checkpoint 2. The coordinating agent independently audited the following strengthening, and it is now integrated with a full proof as C.17 after that checkpoint.

Keep the chosen resolving adjunction F ⊣ G from C.6 and assume every F(α⊗X) is degreewise pure. Instead of requiring finite evaluation components for F itself, assume there exists another exact cocontinuous resolving functor F0 computing Lφ such that every (F0)_n is a retract of a finite sum of evaluations. Then the same raw G is homotopical and gives the inverse equivalence, over every commutative k.

Proof modification: define E(Q)=F0 G(∏_m D^m Q_m). Its degree-n representer on the coefficient-sequence category has m-coordinate a retract of the finite sum of F(h_a)_(m−1), using the finite evaluation presentation of (F0)_n. These are projective k-modules by C.6. For pure-injective coefficients, use the counit of F ⊣ G, not F0: extending it across F(α⊗GDI) makes GDI a retract of J⊗GDI. Condition (d) then gives F0 GDI≈0 since F0 computes Lφ. Coordinatewise pure-injective detection makes the representing cochain complex pure acyclic; Šťovíček Cor5.5 contracts it. Thus F0 GP≈0 for every acyclic projective complex P, equivalently Lφ GP=0. C.10 completes the proof for the original F,G.

No claim that a finite-evaluation resolution F0 always exists is being made. In module-functor language this is an FP-infinity type assumption on φ's representing module. The consequence would be that one such resolution settles all projective resolving adjunctions, rather than only the finite one chosen.
