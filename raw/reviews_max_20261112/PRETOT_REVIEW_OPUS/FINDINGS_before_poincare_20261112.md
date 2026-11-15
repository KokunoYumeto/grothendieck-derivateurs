# Findings of the review of PRESHEAF_TOTALITY (PRETOT)

Review by Claude Opus 5.5 (effort max), 12 November 2026. The reviewing agent could not write this file itself (a
harness guard blocked it); the main session saved its text, as the agent gave it, on 12 November 2026. REVIEW.md
refers to these items as F1-F21.

## Mathematics

- **F1** (computed). G = ⟨a,b | a⁵b⁻³, b³(ab)⁻²⟩ ≅ 2I ≅ SL(2,5): order 120, perfect, centre {1, a⁵}; the map onto A₅
  is exactly the quotient by the centre; an isomorphism with SL(2,5) is a ↦ [[0,1],[4,3]], b ↦ [[0,4],[1,1]].
  Hatcher's Example 2.38 (opened) already states order 120 and the central kernel. Context, standard and not
  re-derived: 2I is the only nontrivial perfect finite subgroup of SU(2); the McKay correspondence pairs it with E₈;
  Σ(2,3,5) = S³/2I is the link of x²+y³+z⁵ = 0. Not asserted: P ≃ the punctured Poincaré sphere. Equal π₁ and χ = 1
  do not decide the homotopy type of a 2-complex in general.
- **F2.** Total W_Z ≠ total W∞ for presheaves (A.5); for categories the two coincide (TOTASPH C.5). For presheaves,
  total W∞ means total W_Z with U/H simply connected.
- **F3.** The classifications A.2, A.10, A.11, A.6. They explain Grothendieck's footnote at XII ms. 108 ("ni d'objet
  F … totalement W-asphérique sans être représentable"): on finite-height bases there is none.
- **F4.** F.3 refutes II Prop. 2.19 and its Corollary (Δ° totalement W∞-asphérique) directly. Among sifted
  categories, totally aspherical means filtered. This does not depend on Contre-exemple 2.20, which goes through XII
  Th. 4 Cor. 4 (false for W∞).
- **F5.** F.6 together with F.3 settles the abelian form of R8 and TOTAL_EXACT D.2.
- **F6.** R9 needs "non-empty connected" (F.1). Correct the statements in INDLOCAL R5 and TOTAL_EXACT R8.
- **F7.** W∞ fails the strong form of W(7 bis); this was already known in the project. The return supplies finite
  witnesses: Δ_inj/K^ss (35 objects, 159 arrows, π₁ = SL(2,5)) with two cone points; and B.2(iii), which falsifies
  XII ms. 85 / ms. 149 and the parenthesis at ms. 111 for W∞.
- **F8.** One XIIapp category (0 ⇉ a → b, c) appears three times: at ms. 9 ("cercle", false), ms. 10-11 (corrected
  by footnotes 5 and 7) and ms. 15 ("π₁ ≃ ℤ", false). It has type S²; with the cone points the type is S³. So the
  argument works only for W∞ and W_n with n ≥ 3. The footnote at XII ms. 103 ties it to S².
- **F9.** E.5 sharpens TOTASPH G.5 (ms. 103).
- **F10.** E.6 and E.8: the notions of XII Déf. 2 are distinct for path fibrations.
- **F11.** VII ms. 102: the transition is reversed. VII ms. 109: Grothendieck's own example is F.14.
- **F12** (computed). Ty^op is not filtered and not sifted, but the F.12 pair has the affine equalizer h₁+h₂−h₃, with
  h₁ = (0,1,2,3,3,3), h₂ = (0,0,0,1,2,3), h₃ = (0,1,2,2,2,3), into (+−+−+). Open: is Ty^op totally aspherical? It
  is a candidate for TOTAL_EXACT Part E.
- **F13.** The method of A.5 should extend to End_Δ([n]) and any finite acyclic K (not checked beyond n = 2).
- **F14.** D.2's maximality is vacuous. Its content is the characterization of homotopical cofibrations by the
  nerve-pushout comparison.
- **F15.** C.4 is open exactly: n ≥ 2, A total W_n, V a cosieve ⇒ H_n(BV) = 0? First case: n = 2, countable. The
  weakly terminal case is TOTASPH C.12-C.13; per the search abstract only (not opened), Isbell 1968 is the monoid case.

## Provenance and record

- **F16.** Not new and not credited by the return: G.1 = POLES G.19; G.2 = Grothendieck's footnote 7 and the
  expert's F-G4; F.14 = VII ms. 109 = PATHS A.4; F.13 = PATHS A.2; A.12 = Isbell-Mitchell / TOTASPH C.10; D.4 =
  Cisinski 1999; E.5 was preceded by TOTASPH G.5.
- **F17.** F.16 (open here) conflicts with PATHS A.P2/C.P2, which claims a proof; review PATHS.
- **F18.** G.3: the remark is on ms. 96, not 95, and the supporting argument is in E.7, not A.7.
- **F19.** Three slips in TOTAL_EXACT's paragraph on this return: "Theorems B.2-B.4" (B.4 is about composition, not
  separation); "§5" should be Part F; "not yet reviewed" is out of date.
- **F20.** Six web searches plus Hatcher opened; none located A.2, A.5, A.10, B.2-B.3, E.5, E.6, F.3, F.4 or F.6.
- **F21.** Reruns identical. The reviewer's own code reproduces A.3-A.5, A.9, A.14 (monoid part), B.2(v), E.8, F.12
  and G.2, and gives an independent certificate for A.5.

## Open after the review (carry into the next Dérivateurs follow-up)

C.4 (n = 2, countable); E.9 (P(R,0) → R); F.10 (Δ_inj with word substitutions); F.16 (the six-object S² poset).
Review PATHS before any prompt relies on F.16 or on PATHS A.P2/C.P2.
