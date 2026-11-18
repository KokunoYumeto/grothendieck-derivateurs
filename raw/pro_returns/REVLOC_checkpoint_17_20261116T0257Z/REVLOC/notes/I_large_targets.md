# D.3 large-target constructions

The full proved construction is in `sections/D3_large_targets.tex`, claim D.3.4. It contains two families and explicitly does not claim strictness over the BZ/2-generated lower endpoint.

## Infinite Moore wedges

For infinite kappa and d>=3 let Y_kappa^d be the wedge of kappa copies of P^d(2). The null class of this single target is desuspension-closed for arbitrary source spaces.

Partition kappa into three kappa-sized blocks and apply Hilton--Milnor with these three whole connected wedges as letters. Its [[1,2],3] factor is loops on the suspension of the triple smash. Project the kappa-cubed finite-smash summands to kappa diagonal triples. Each suspended triple smash of P^(d-1)(2) has P^(3d-3)(2) as an actual retract, by the elementary spherical commutator and L3 calculation. Hence Omega Y_kappa^(3d-3) retracts Omega Y_kappa^d. This includes d=3 and uses no finite-type or localization convention for RP2: the commutator sphere comes from changing the middle-cell attaching row (2,-2) to (2,0), and the suspended triple smash is simply connected finite 2-primary.

The higher infinite wedge is two equal copies of itself. The two-copy James/resolution lemma from D.1.8, followed by Barratt finite cone cubes, gives the original unlooped wedge. There is no invalid replacement of infinitely many same-connectivity Hilton--Milnor factors by a product. Only finitely many large spaces are used as letters at each application.

Intersecting the cofiber localizer with R(loc(S/2)) gives a reversible localizer with stable part exactly loc(S/2), containing W_rev and strictly below the homological upper endpoint. Miller gives BZ/2-nullity, and the finite Moore summand detects the strict upper inclusion. The lower inclusion is not known strict.

The stronger collapse test succeeds: every infinite Moore wedge gives exactly the null class of one Moore target, for arbitrary sources. D.1.8 gives all finite Moore bouquets. For countable X exhausted by finite subcomplexes X_i, the HM factor F_q=Sigma(P^(d-1))^smash q has finite 2-primary homotopy groups. Its mapping tower [X_i,Omega F_q] consists of finite groups and has inverse limit zero because Omega F_q is already X-null. Hence it is pro-zero. At any fixed finite X_i only finitely many lengths q are visible, so one later stage kills every factor type simultaneously, regardless of infinitely many word labels. The countable-wedge weak-product HM tower is therefore pro-zero. All suspensions satisfy the same statement, so Milnor gives loop-wedge nullity; the desuspension theorem above gives the unlooped wedge. Maps from countable sources to any larger wedge factor through a countable subwedge.

For arbitrary X, the G.7 compact-level Kan model and bounded extension lemma apply to the 2-complete finite Moore target and all its loops. Thus every countable subcomplex of a Moore-null source lies in a countable Moore-null subcomplex. The filtered homotopy colimit of these is X, proving the same wedge nullity. This rules out the entire infinite-Moore-wedge cardinal route; no large-source separator exists in that family. Fibrations_groups supplied and checked the compact shrinking step; simple_higher checked the HM/pro-zero step.

## All bounded-cardinality finite-dimensional targets

For infinite kappa take all simply connected finite-dimensional CW targets with at most kappa cells. The family is closed under finite wedges, suspensions, and finite smash products. The finite weight truncations of every iterated James splitting stay in that family. Therefore Omega-target nullity implies target nullity by the simply connected Omega-Sigma resolution, proving desuspension closure for arbitrary sources. Intersection with R(loc(S/2)) again gives the same stable part and a strict upper inclusion, but no strict lower inclusion is proved.

For finite-type sources all these classes agree: they include all spheres, and Strom2012 Theorem1 then forces nullity into every simply connected finite-dimensional target. Universal phantom targets of the form wedge Sigma X_n generally have unbounded dimension, so they do not by themselves separate this family.

## Active zero-finite-part candidate

The candidate A=Q(Sigma K(Fp,2)), W=minrev(A), X=K(Fp,2) has T(W)=loc(Sigma-infinity K(Fp,2)) by Snaith. Lee's stable-cohomotopy vanishing shows this nonzero stable part has no nonzero finite spectra. Unlike QK2, QSigmaK2 has no evident infinite-loop retraction onto K2 because its lowest degree is3. Axioms_derivators proved the exact reduction: A kills SP-infinity A, whose H3=Fp factor gives K(Fp,3); hence the Bousfield arithmetic criterion makes minrev(A) equal {X:P_A Sigma^2 X is contractible}. Thus the needed separator is precisely P_A Sigma^2 K(Fp,2) noncontractible. No proof of this noncontractibility has been obtained.

Finite targets cannot currently detect this candidate. They are already null from K2 by the generalized Sullivan theorem. A direct infinite-target or nullification calculation is still needed. The cohomology filtration of the infinite-loop source versus suspended K2 was considered, but no complete obstruction was established.

## Moore versus completed spheres

Claim D.3.6 is written in sections/D3_Moore_spheres.tex and was independently accepted by root after opening the Isaksen statements and proofs. It is integrated after D.3.5. For any prime, a single simply connected prime Moore target forces nullity into all p^r Moore targets. The smash-closed family consists of all suspensions of smash powers of P^3(p); two-copy retractions at arbitrarily high dimensions plus James resolution and Barratt descent put it in the resolving kernel. Strom Theorem7 and Corollary11 give its finite cone complexes. The attaching map P^n(p) -> S^n -> P^(n+1)(p^r) has cofiber P^(n+1)(p^(r+1)); its cellular boundary [[p^r,1],[0,p]] exhibits the actual unstable cancellation.

The inverse Moore tower is proved to be the unstable p-completed sphere by Isaksen's pro-space completion model, not by the stable identity. Take all finite Postnikov sections of the tower. Their homotopy groups are finite p-groups, so their Postnikov towers refine into finitely many principal Fp-EM fibrations. A strict fibrant replacement is therefore fibrant for Isaksen's cohomological and homological models. The map from the constant sphere is a pro-Fp-homology equivalence because the bottom mod-p class has identity transition while the top class has zero transition. Isaksen Proposition7.3 compares with the BK tower, and the right Quillen inverse-limit functor gives holim_r P^(n+1)(p^r)=S_p^n.

The reverse implication holds for rationally acyclic sources by arithmetic fracture and the localized-sphere resolving argument. In particular after intersection with R(loc S/2), the single Moore target and all infinite same-dimension Moore wedges give exactly W_S intersect R(loc S/2). This is another collapse result, not a strict intermediate.

## Product and inverse-limit routes: assessment at checkpoint 03

No new separator was proved. Products of p-torsion GEMs are infinite loop spaces, so the connective obstruction in D.2.9 already covers them when the required stable membership and connectivity hold. Products of suspended GEMs are possible nonlinear spaces, but there is no proof that their suspension spectra belong to I_p = loc(Sigma-infinity K(Fp,2)); a localizing subcategory need not be closed under products. Finite products, little-cubes iterates Omega^r Sigma^r K(Fp,2), and the natural projection fibers are already in the reversible class or have the wrong stable chromatic part.

For an inverse-limit candidate, stable membership and unstable nonnullity must both be established. The stable inverse-limit identity alone does not supply an unstable one. The successful Isaksen argument in D.3.6 controls a specific Moore tower through pro-homology and finite Postnikov stages; no analogous argument for a nonlinear K(Fp,2)-suspension tower has been obtained.

The remaining exact test is still P_{Q Sigma K(Fp,2)} Sigma^2 K(Fp,2) noncontractible. A proof of this would separate W_1 from its RT closure. Neither the product exploration nor the literature checked below proves it.

## Finite-category mapping hypotheses: primary scope audit

Opened Hiroshi Kihara, "Groups of homotopy classes of phantom maps", Algebraic & Geometric Topology 18 (2018), 583--612, DOI 10.2140/agt.2018.18.583, publisher PDF https://msp.org/agt/2018/18-1/agt-v18-n1-p18-s.pdf. The source and target classes are defined on p.586. Proposition 6.3 and Corollary 6.4, pp.605--607, were read, including the proof and its references to McGibbon's 1996 generalized Miller theorem. Its source class contains connected infinite loop spaces with torsion fundamental group and their iterated suspensions. The target class is nilpotent finite complexes, classifying spaces of compact Lie groups, and their iterated loop spaces. It does not contain arbitrary finite-LS-category suspensions merely because their category is one.

The blanket proposed extension is false even for finite-type p-torsion infinite loop sources: put B=K(Fp,2). The identity of Sigma B is a nonzero, nonphantom element of pi_1 Map_*(B,Sigma B), since it is already detected on the bottom homology class. Both source and target satisfy the proposed torsion/finite-type conditions, and the target is a simply connected suspension of LS category one. Thus a valid result for A_1=Q Sigma B must use a property beyond being an infinite loop space, or a stronger target restriction.

Searches located McGibbon, "Infinite loop spaces and Neisendorfer localization", Proc. AMS 125 (1997), 309--313, and "A note on Miller's theorem about maps out of classifying spaces", Proc. AMS 124 (1996), 3241--3245. Their search abstracts concern finite-dimensional or finite nilpotent targets, not arbitrary finite-category targets. The full original PDFs were not obtained in this pass, so these abstracts are not used as new proof inputs.

For Y a finite wedge/smash combination of positive suspensions of B, every homotopy group is finite p-primary. Consequently a phantom map from a countable finite-type source to Y vanishes by the finite-group Mittag--Leffler argument. This observation removes phantom ambiguity but does not prove that all maps from A_1 or its suspensions are phantom. Steenrod/cup-product obstructions considered for bottom-degree A_1 -> Sigma B do not automatically handle Sigma A_1 -> Sigma^2 B, all higher mapping groups, or the iterations in nullification. No stronger conclusion is recorded.
