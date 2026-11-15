# D.3.8: supported infinite-loop generator subcase

The full result is in `sections/D3_infinite_loop.tex`. It was proposed by the independent simple_higher agent from D.2.9 and audited by root and axioms_derivators.

Fix p and n >= 1. If all generators X_i are (n-1)-connected infinite-loop spaces with p-primary torsion homotopy and some H_n(X_i;Fp) is nonzero, their smallest reversible class is exactly Rev{Omega-infinity E : E in L and E n-connective}, where L is the localizing stable part. Thus there are at most countably many such classes for fixed (p,L). If L is set-generated, the reversible class is accessible even for an original class of generators.

## Exact interface

Bousfield, *Unstable localization and periodicity* (1996), Theorem 2.10 and Proposition 3.1, pp37--38, were reopened and checked. Primary URL: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf . They give P_A Omega-infinity E = Omega-infinity P_(Sigma-infinity A)^Sp E and equivalence of ordinary A-acyclicity of Omega-infinity E with spectral Sigma-infinity A-acyclicity of connective E. This is stronger than merely saying Q A belongs to the reversible closure, and is the precise reason ordinary acyclicity is available in the proof.

Each underlying E_i lies in loc Sigma-infinity X_i by Proposition 3.1 applied to the tautological ordinary X_i-acyclicity of X_i. For a small family, use A = wedge X_i and apply D.2.9. For a class family, every individual E in L belongs to the localizing subcategory of a small source subfamily: the union of all such subcategories is localizing because a small union of small families remains small. Adjoin one bottom-degree support witness before applying D.2.9. If L is set-generated, one common small source subfamily generates its stable part and therefore its canonical reversible class.

## Limits

The first nonzero integral homology being p-divisible is explicitly excluded. No assertion infers acyclicity of a connected cover from arbitrary fibre two-out-of-three. The result does not prove strictness or collapse of the Q-suspension chain, and does not settle the general fixed-stable-part cardinal bound.

## Divisible-bottom extension: limitation resolved

The initial supported-only proof is preserved verbatim in FGH_D3_infinite_loop_supported_history.md. The current theorem covers every nontrivial family of connected p-primary infinite-loop spaces. Let n be its first nonzero homotopy degree. If any bottom group is nondivisible, use the previous formula. If all bottom groups are divisible, the canonical generators are K(Cp-infinity,n) together with all Omega-infinity E for E in L and (n+1)-connective.

The essential new proof has been independently attacked by root and simple_higher. The general first sentence of Bousfield ULP Theorem2.6 (p37) says the spectral-nullification tower fibres are stable GEMs, without the supported-p-torsion hypothesis. A kills K(Cp-infinity,n) by Cor3.2 and the bottom SP-infinity retract; the nonsplit p self-extension of Cp-infinity and Lem9.13 then make K(Fp,n+1) A-acyclic. Thus C=Sigma-infinity A spectrally kills Sigma^(n+1) HFp.

For Y_i=P_(Sigma^-i C)E, the fibre F_i is C_i-null and p-primary. It is therefore null for Sigma^(n+1-i)HFp. A nonzero stable GEM summand Sigma^kHG with k>=n+1-i would receive Hom(Fp,G) in a nonnegative mapping degree, so F_i<=n-i. Comparing Y_(i+2) to Y_infinity handles both the fibre and suspended fibre; all-shift C-nullity plus membership in loc C makes Y_infinity zero. Thus P_C E<=n. Cone attachments from an n-connective source preserve (n+1)-connectivity of an already (n+1)-connective input, so P_C E=0 for E in L>=n+1.

In the reverse canonical inclusion, Sigma^n H pi_n E_i is explicitly put in L using the already available Cp-infinity generator and Proposition3.1 before taking its connective cover. The final Postnikov step uses fibre and base to obtain the total space, the valid extension direction. It does not infer fibre acyclicity from total and base.

No new large-cardinal assumption, compactness of C, or exchange of Map(C,-) with a filtered colimit occurs. The countable bound now includes both divisibility cases.
