# Part A.4: continuing search and exact gates

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 18 November 2026. This is a record of attempted routes, not a declaration that A.4 is complete.

## Current gates

The proved bounds in A4.1 remain

`W_rev(BC2) ⊆ W_S ∩ W_Z[1/2] ⊊ W_Z[1/2]`.

All three classes have stable part `loc(S/2)`. The first inclusion is not proved strict or an equality. The questions about a third element and about the size of the full fibre of T are distinct; equality in the displayed first inclusion would not rule out other intermediate classes.

The exact separation target is a pointed sphere-null space X with 2-primary suspension spectrum and `P_BC2(Sigma X) != *`. We rechecked REVLOC D.2.7 in full, then opened Bousfield (1996), Theorem 3.3, and Bousfield (1997), Lemmas 8.13 and 9.13, at their actual statements and proofs. They justify `A_minRev(BC2) = {X : P_BC2(Sigma X) = *}`. The proof uses the symmetric-product term in Theorem 3.3 to establish desuspension closure; BC2 kills every simply connected p-primary GEM, so that term is acyclic. This is a genuine equivalence, not the false inference that ordinary BC2-nullification alone defines the reversible minimum. The initial suspension must be retained. The numbered reduction being integrated into the paper records this audited gate.

## Routes examined in this run

1. **Finite additions and finite-dimensional detectors.** The already supplied finite-primary and bounded-target collapses were checked at the steps used in A.5--A.9 and in the A.3 notes. The finite Moore witness distinguishes the upper endpoint from the sphere-null intersection, but adjoining that witness reaches the upper endpoint. It does not construct a third point. Increasing a cardinal bound on finite-dimensional targets is not a new separator.

2. **Infinite-loop generators.** The opened Levy Theorem 3.2 makes a connected infinite-loop space of a p-primary spectrum ordinarily BCp-acyclic. Such generators therefore cannot separate the lower endpoint in the primary interval. Goodwillie approximations involve inverse limits, whereas the reversible closure has the stated homotopy-colimit closure. No passage through that inverse limit has been proved.

3. **Large families of rigid abelian groups.** We opened Stanley's preprint Section 8, including the complete proofs of Proposition 8.3 and Corollary 8.4 and the proof outline of Theorem 8.5. Its separators use orthogonality to positive shifts of Eilenberg--Mac Lane objects. The section explicitly distinguishes this from closure under desuspensions. Those tests cannot be used unchanged to distinguish reversible closures. Thus its proper-class result does not answer the fixed-stable-part question. No claim about the unopened original Shelah construction is required here.

4. **Vopenka and coreflectivity.** We opened Casacuberta--Gutierrez--Rosicky, especially Theorems 3.7 and 3.9 and the discussion following Corollary 4.3. A theorem assigning a small generating set to each individual class does not bound the sizes of generating sets uniformly across all classes. Nor does a semilocalizing result automatically impose the cofiber/desuspension conditions here. This route currently gives no set-size conclusion for a fibre of T.

5. **Acyclic classes of maps in infinity-topoi.** We opened Anel--Biedermann--Finster--Joyal III, including its acyclic-class definition and small-generation discussion. Those classes are required to be closed under base change. Reversibility in this task is a reverse *pushout* condition, and the needed base-change hypothesis has not been proved. Applying their left-exact classification would change the question.

6. **Fibre and join estimates.** We examined Chacholski--Scherer--Werndli's homotopy-excision theorem and Strom's general resolving-class theorem. The former controls a total fibre by a join and a looped pushout defect; the latter requires an appropriate smash/suspension-closed target family and finite cone length. Neither supplies nullity in the missing infinite-cone-length case. These hypotheses are kept visible rather than treating arbitrary wedges of finite complexes as finite cone length.

7. **Alternative p-primary spaces.** Finite p-groups, primary Eilenberg--Mac Lane spaces and connected infinite-loop spaces stay within the known lower-endpoint constructions. Finite Moore spaces fail the sphere-null test. Completed spheres need not have p-primary integral homology and cannot simply be inserted into the interval. No valid separator was obtained from these alternatives.

8. **Nonrepresentable homology kernels.** We opened Casacuberta, *Depth and simplicity of Ohkawa's argument*, Sections 2, 6 and 7, including the proof of Theorem 7.1 and Corollary 7.2. Its cardinal-indexed exact functor is `F_alpha(A)=A^alpha/{functions with image of cardinality < alpha}`. Composing with reduced integral homology gives proper-class many kernels. These kernels fail the wedge closure required here: all circles are killed for infinite alpha, but their alpha-fold wedge is not. Intersecting with the p-primary class does not repair this: each finite p-Moore space remains killed, so the reversible closure reaches the upper primary endpoint. The theorem about functors preserving filtered colimits for one fixed regular cardinal supplies no uniform cardinal for the present fibre. This route is excluded, not a solution of the size question.

9. **Nilpotent Postnikov and polyGEM cellularity.** We opened Chacholski--Dror Farjoun--Flores--Scherer, *Cellular properties of nilpotent spaces*, especially Proposition 6.2 and Theorems 6.4 and 6.6 with proofs. The Postnikov result constructs a nilpotent Postnikov section from the original space by homotopy colimits. It does not reconstruct the original space from its Postnikov sections by those colimits; that direction would need the unproved inverse-limit passage. We also reread the supplied REVLOC D3_abelian section in full: its polyGEM countability result is existing background, not new movement. Castellana--Crespo--Scherer's *Postnikov pieces and BZ/p-homotopy theory*, Lemma 1.1 and Theorem 1.2 with proofs, supplies no missing inverse-limit step in the scope checked.

10. **Recent stable Bousfield results.** Initial arXiv web fetches for Putzstuck, arXiv:2608.06104, and Barthel--Castellana--Heard--Sanders--Zou, arXiv:2608.26876, repeatedly returned DisabledError. Ordinary public-PDF downloads then succeeded (356221 and 761737 bytes), superseding that access gap. We read Putzstuck's Theorem 1.4 and its complete proof, including the countable annihilator construction in Lemma 4.2. It bounds smash-homology kernels and expresses each by a sum of countable spectra; it does not give countable generators for every localizing subcategory or every reversible unstable class. We read BCHSZ Section 2 through Proposition 2.23 and Section 9 through Corollary 9.11, including proofs. Their Remarks 2.9--2.10 explicitly keep separate the general size and representability questions for stable cohomological classes. No implication from either stable size result to the requested unstable fibre has been proved. The corresponding supplied REVLOC literature-update paragraph is now rechecked against the originals, rather than adopted from the return alone.

11. **Reversibilizing the known nonaccessible coefficient example.** We reread the supplied REVLOC H.1--H.4 in full. The explicit membership condition (H.3.1) only tests components, fundamental groups and a reflection of the second homotopy group. Independently of the set-theoretic argument producing that reflector, a class with this membership condition contains every sphere collapse above dimension two. Any reversible fundamental localizer containing such a collapse is total: repeated reversible desuspension makes S0 aspherical, and the pointed cell/homotopy-colimit construction makes every pointed space aspherical, including the cofiber test for the empty-to-point map. Thus this particular nonaccessibility construction loses the relevant distinction on reversible closure. We do not infer accessibility of all reversible localizers from that failure, and do not use the unread original set-theoretic proofs as inputs to this elementary exclusion.

12. **Generalized accessibility and nullity.** Rezk's author draft dated 13 April 2021, introduction and Section 7, was opened. Its filtration-class/nullity comparison does not assert a set bound for the reversible classes in question; its smallness notion starts from an essentially small doctrine, without a uniform bound across doctrines. The draft itself flags technical gaps, including a proof placeholder in Lemma 7.8. No unproved draft assertion is imported into the present argument. This is a scope check, not a new theorem or a reduction of A.4.

## Submitted search strings

- `"acyclic classes" "suspension" nullification BZ/p`
- `"Miller spaces" "nullification" BCp`
- `"localizing subcategories" "spaces" "proper class" suspension`
- `"Are all localizing subcategories" coreflective arxiv`
- `"Miller spaces" "BZ/p" nullification characterization`
- `"proper class" "nullity classes" Stanley`
- `"nullification" "BU(n)" "K" Bousfield`
- `"phantom maps" "infinite loop spaces" wedge`
- `"Invariants of t-structures and classification of nullity classes" Stanley pdf`
- `"spherical" "BZ/p" "nullification" acyclic classes`
- `"Miller spaces" "acyclic" "nullification"`
- `"reversible" "localizers" homology`
- `"Miller spaces" "classification"`
- `"spherical null" spaces homotopy`
- `"Miller" "Anick spaces"`
- `"Miller spaces" "Kahn"`
- `"Miller spaces" nullification`
- `"cohomotopy" "BZ/p" "acyclic"`
- `"acyclic classes" "cofiber" spaces suspension`
- `"nullification" "sphere" "Miller" converse`
- `"sphere" "acyclic classes" "Bousfield"`
- `"suspension" "nullity classes" "proper class"`
- `"Miller space" "acyclic"`
- `"Miller spaces" "converse"`
- `"BZ/p-null" "homology" "torsion"`
- `"Miller spaces" "loop"`
- `"Depth and simplicity of Ohkawa" Casacuberta year`
- `"BZ/p-nullification" "suspension" "acyclic"`
- `Putzstuck Bousfield lattice 2026 cardinality countable spectra`
- `"cohomological Bousfield" "2026"`
- `"Local Bousfield classes via homological support" pdf`
- `"nullity classes" "set" spaces Bousfield`
- `"acyclic classes" "proper class" spaces homotopy`
- `"Bousfield classes" "spaces" "set" nullification`

Search-result snippets and unopened papers are not used as theorem statements. The searches have not decided any of the three current A.4 gates. The work continues with detectors beyond finite-dimensional targets and with the ordinary-nullification versus reversible-closure comparison kept explicit.
