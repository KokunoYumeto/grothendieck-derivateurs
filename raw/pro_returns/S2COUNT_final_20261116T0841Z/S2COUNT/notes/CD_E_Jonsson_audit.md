# Jónsson construction audit

The current constructive question is whether a nontrivial acyclic group with an actual two-dimensional CW classifying space can have no countable images. Amalgamating two such groups over an infinite cyclic subgroup would supply the desired sphere homology. An uncountable Jónsson group would have no countable images: at cardinality aleph-one, a proper kernel and a countable image would both be countable, forcing the group itself to be countable.

## Corson–Obraztsov: explicit large homology

Samuel M. Corson, *Jónsson groups of various cardinalities*, Proc. Amer. Math. Soc. 150 (2022), 2771–2775, DOI 10.1090/proc/15871, arXiv:2101.11035v5. The original five-page preprint was read in full. Theorem 1 obtains a simple torsion-free Jónsson group from a Jónsson algebra. Proposition 5 is a specialization of Obraztsov's 1996 Theorem A; the proof uses one infinite cyclic factor per element of the Jónsson algebra.

Viatcheslav N. Obraztsov, *A new embedding scheme for groups and some applications*, J. Austral. Math. Soc. (Series A) 61 (1996), 267–288, DOI 10.1017/S1446788700000252. The original publisher PDF was read through its theorem, construction, and the relevant proof; p. 277 was also inspected as an image to verify the formula. Exact primary URL:

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DFBA898D83ED52744723EF3C0322A11C/S1446788700000252a.pdf/new_embedding_scheme_for_groups_and_some_applications.pdf

The defining family (2.2) on p. 277 has an affine dependence on the parameter k in its exponent sums. For one special period A=a[a,c]^t, the formal combination R_6−2R_7+R_8 has zero exponent sum. Distinct cyclic-factor pairs give disjoint relator supports. Diagrammatic reduction preserves signed relator multiplicities, so Hopf's formula makes these actual independent group homology classes. The standalone proof in `sections/CD_E_Jonsson_obstruction.tex` concludes H_2(J_kappa;Z)=Z^(kappa) for the literal construction used by Corson. It has been sent to the E agent for independent audit.

This is a calculation for that construction, not a nonexistence theorem for all Jónsson groups. Obraztsov's term “diagrammatically aspherical” also applies to his torsion variants; no actual two-dimensional K(G,1) is inferred merely from that term. The homology obstruction does not need that inference.

The reduction convention was checked in the accessible primary source Alexey Muranov, *Finitely generated infinite simple groups of infinite commutator width*, Int. J. Algebra Comput. 17 (2007), 607–659, arXiv:math/0608688v4. Section 6, p. 34, explicitly identifies Olshanskii's version with diagrammatic asphericity and gives Definition 60 by diamond moves to elementary two-face spheres. Definition 33 on p. 17 preserves face characteristic boundaries and c-contours and gives a face bijection; Definitions 38–40, pp. 19–20, define the corresponding cancellations. The signed-relator-count argument therefore has the required convention. The original Olshanskii book chapter itself was not accessible beyond its publisher preview, and is not represented as independently read.

`code/CD_E_Jonsson_cycles.py` verifies the exact word exponent formula after free reduction, and the integral second-difference cycle, for 108 small parameter choices. Those choices are algebraic checks only; the proof uses the symbolic identity and the source's admissible large parameters.

## Poór–Rinot: scope still limited

The 2025 paper *A Shelah group in ZFC*, Forum Math. Pi 13, e13, DOI 10.1017/fmp.2025.5, constructs torsion-free groups with the necessary cardinal image restriction. Its “two-dimensional construction scheme” on p. 4 is an ordinal grid of amalgams, not a statement about geometric dimension. Lemma 3.4, pp. 7–11, supplies C'(1/10) quotients of amalgamated products; no global controlled H_2 or actual two-dimensional CW model is stated there.

One possible additional homology obstruction is visible locally. The block relation is h^-1 rho(ba,b^2a), where rho(x,y)=xyx^2y...x^80y. Its exponent sum is -[h]+3320[a]+3400[b]. Whenever a runs through powers a^m with the same other data, the boundaries again vary affinely in m. The defining conditions in 5.13–5.14 make this plausible, but carrying those cycles through the coherent amalgam grid requires an additional homology-injectivity or global relative-asphericity argument. No global H_2 assertion for the Poór–Rinot group has been proved in this audit.

## Other exclusions

The torsion group in Corson–Olshanskii–Varghese, *Steep uncountable groups*, Bull. Lond. Math. Soc. 56 (2024), 701–710, DOI 10.1112/blms.12959, arXiv:2305.02953, cannot have a finite-dimensional actual CW classifying space because it has nontrivial finite cyclic subgroups.

An uncountable Jónsson group cannot be locally free. Nishinaka's theorem supplies a free subgroup of the same cardinality in every uncountable locally free group. The Jónsson condition would make it the whole group, whereas an uncountable free group has proper subgroups of its own cardinality.
