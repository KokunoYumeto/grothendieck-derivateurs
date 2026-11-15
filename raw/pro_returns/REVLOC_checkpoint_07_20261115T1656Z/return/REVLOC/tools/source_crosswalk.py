#!/usr/bin/env python3
"""Keep one explicit literature-comparison row per numbered manuscript claim."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
special = {
    'D.2.16': ('Cohen--Lada--May ChapterIII Theorems1.2--1.4 and3.1--3.2, Lemma3.8, and Serre1953 Section2 nos8--9 are opened. The ordinary-map deviation obstruction is proved here.', 'Exact target Steenrod/cup identities produce three inconsistent constraints on an actual map from the double-suspended smash. An exhaustive 512-vector source certificate agrees with the independent hand proofs. Every fourth-stage map has zero specified Hopf coefficient; no coherent symmetry or H-map hypothesis is imposed, and general iterated nullification survival is not inferred.'),
    'D.2.15': ('Milnor--Stasheff Section8 pp91--93, Adams1966 Example7.17 and Eq8.1, Angeltveit--Rognes2005 Eq8.4 and Lemma8.11, and ABGHR2014 Theorem2.24 are opened. Hovey--Palmieri report the smash-Bousfield equality before Conjecture8.7.', 'The reduced transfer forces nu to vanish in a CP-infinity-null complete ring; a finite module endomorphism ring removes eta. Completion and the local monoidal unit give actual localizing generation without the general Bousfield-order comparison conjecture. The Pruefer ideal is the full primary ideal at every prime.'),
    'D.2.14': ('The Euler--Thom sequence is derived here and compared with Madsen--Schlichtkrull Section1. ABGHR2014 Definitions2.20/2.22 and Theorem2.24 and LurieHA Proposition2.2.1.9 are opened.', 'A shifted unit extends to an actual orientation when eta vanishes; E1 left/right module duality gives the contradiction. The exact derived-complete local-unit criterion and odd-primary Pruefer equality are proved, then extended by D.2.15.'),
    'D.2.13': ('Cohen--Lada--May ChapterIII pp216--219, the stated James and Serre inputs, and the homology-suspension interface are opened.', 'The canonical second-stage extension fails at stage4, while a low-dimensional positive range and finite-stage/subpair detection are proved. Its remaining arbitrary-map correction is subsequently excluded by D.2.16, without discarding the canonical positive-range calculation.'),
    'D.2.12': ('Serre1953 Section2, no.8, Theorem2 and no.9, pp.203–204, and James1955 Section3 and Theorem5.6/Corollary5.7 are opened. The unstable obstruction is derived here.', 'Naturality of the coproduct and Sq2 forces coefficient1 on the tensor word bb, while Sq1 and source commutativity force coefficient0. This excludes every map hitting bottom homology for all r≥1, including arbitrary higher-weight corrections, without assuming an H-map or using Dyer–Lashof operations. It does not imply that the entire mapping space is trivial or that ordinary nullification survives.'),
    'D.2.11': ('Blans–Heuts2026 Corollary B and Proposition4.11, Heuts2021 Theorem4.22/Corollary4.23 and Proposition4.26, Hovey–Strickland1999 Corollary8.8, Ravenel–Wilson1980 Theorem11.1(a), and Hopkins–Ravenel–Wilson1998 Remark4.4 are opened and combined here.', 'An explicit countable family of trivial Lie algebras generates every positive finite-height periodic Lie category by colimits and retracts. The action-bar proof uses the loop of the base, and a simultaneous all-loops induction through finite weights, without a join axiom. The ordinary-space application checks lower acyclicity and connective covers before using periodic adjunction; no commutation with ordinary nullification is asserted.'),
    'D.2.10': ('Bergsaker–Rognes2023 Theorem1.1, Carlsson1992 Corollary2.3, Arone–Mahowald1999 Theorem2.1, Goodwillie1992 Example4.3 and Goodwillie2003 Theorem1.13 are opened and combined here.', 'The Segal/tom Dieck/Sylow argument puts finite-group orbit spectra and their localizations in coloc(S); genuine finite partition coefficients and the convergent identity tower then turn stable sphere annihilation into unstable finite-target nullity. This rules out sphere-test separation for the zero-finite-part candidate without proving RT-fixedness.'),
    'A.1': ('Derived from the opened EHP statement, not printed there as a null-class theorem.', 'The mapping-space descent, including dimension two.'),
    'A.3': ('The cofiber interface is already in POLES B.2/B.5; the stated application is checked here.', 'Retracts, relative comma diagrams, disconnected and empty cases.'),
    'A.5': ('Kahn--Priddy and Snaith give the stated input splittings; the localizing-subcategory identity is derived here.', 'Space section, bar construction, connective cover and Moore cofiber.'),
    'A.7': ('The cyclic-prime version is in Kahn--Priddy 1978 p.103; the stable equality is derived here.', 'The transfer-homology coefficient and the same stable generation steps.'),
    'B.1': ('Not located as this combined bounded closure lemma in the opened comparison sources.', 'All three cofiber cases, homotopy-colimit closure and explicit desuspension enlargement.'),
    'B.3': ('The assertion left open in POLES F.14 is refuted here.', 'The countable accessible example and its finite unstable separator.'),
    'B.4': ('Not located as this exact reversible-closure theorem in the opened comparison sources.', 'A uniform small-arrow generating set; object projections alone are not substituted.'),
    'C.1': ('R7 states the proposed closure operations; their required derivations are supplied here.', 'The distinction between finite loop-suspension converse and Q-converse.'),
    'C.6': ('Same proved conclusion as C.9, retained to identify the original question.', 'See C.8--C.9.'),
    'C.7': ('PRETOT supplies the proposed acyclic example; R11 does not imply the locality conclusion.', 'Independent finite category and group checks and an explicit identity-map obstruction.'),
    'D.0': ('The prompt proposes the correspondence; the opened Bousfield statements do not identify equal object null classes with equal localizers.', 'Acyclic nullification and the braid-to-circle counterexample.'),
    'D.1.7': ('CMN provides loop retractions; the single-target desuspension conclusion is derived here.', 'The P3 Whitehead/Bockstein calculation, overlapping dimension intervals and convergent unlooping.'),
    'D.1.8': ('Chen--Wu and Wu supply the spherical class and looped Lie retracts; the two-copy retract and nullity classification are derived here.', 'Explicit geometric maps, two independent eleven-letter certificates, a wedge retraction and arbitrary-source unlooping.'),
    'D.1.9': ('Hilton--Milnor and Strom Corollary12(a) supply the resolving-class inputs; the odd-prime fundamental-group conclusion is derived here.', 'The suspension unit forces maps to lift to the null universal cover; the RP2 failure is an explicit factorial telescope.'),
    'D.2.7': ('Bousfield1996 Theorem3.3 and Bousfield1997 Lemma8.13 give the suspension identity and GEM inputs; the reversible-generation formula is derived here.', 'Uniform finite suspension, every cofiber implication, arbitrary sources and the divisible degree-one endpoint.'),
    'D.2.8': ('Derived from Bousfield\'s comparison as restated and proved in Barkan--Heuts--Shi2026 Theorem4.1.', 'The finite-primary generator gives its full stable localizing class on arbitrary sources, without a telescope-conjecture assumption.'),
    'D.2.9': ('Bousfield1996 Theorem2.6 gives the one-degree spectral fibers; the connective-localizing comparison is proved here.', 'Coconnective fiber bounds replace an invalid commutation of a mapping space with a filtered colimit; the nonlinear suspended-space test remains undecided.'),
    'D.3.3': ('Derived from Arone--Mahowald Theorems2.1/4.1 and Proposition3.1, Bousfield2001 Corollary4.8, and Levy2025 Theorem3.2.', 'Odd-sphere Goodwillie stages, exact connectivity, ordinary-nullification fibers and the finite Moore cofiber force the upper endpoint.'),
    'D.3.4': ('Chen--Wu, the finite Moore calculation and Hilton--Milnor supply the finite retractions; the cardinal-collapse assertion is proved here.', 'Three whole wedges, diagonal smash projection, uniform finitely many factor types and countable compact shrinking; no strict intermediate is asserted.'),
    'D.3.5': ('Strom2012 Proposition4(b) and Corollary12(a)/(b) give the pro-zero and resolving inputs; the arbitrary-source primary statement is derived here.', 'Finite-cell exhaustions, unsuspended phantom components, arithmetic comparison and alternating countable saturation.'),
    'D.3.6': ('Isaksen2004 Theorems3.3/6.3/6.7/7.2 and Proposition7.3 supply the pro-completion interfaces; the unstable Moore-tower and nullity comparison are derived here.', 'Actual higher-exponent cofiber matrix, finite principal Postnikov refinements and a right-derived inverse limit, with the rational-source qualification retained.'),
    'D.3.7': ('Stanley2006 Theorem8.5 supplies the ordinary-nullity proper-class contrast; Bousfield1997 Lemma9.13 and CFFS2015 Proposition6.2(4) supply the GEM and polyGEM inputs. The reversible cardinal bound is proved here.', 'A countable arithmetic normal form for arbitrary abelian groups, rational cofiber comparisons at degree one, Ext-complete groups without a separatedness assumption, and actual bar quotients; the general fixed-stable-part question remains open.'),
    'D.3.8': ('Bousfield1996 Theorems2.6/2.10 and Proposition3.1 give the general GEM-error and ordinary space--spectrum interfaces; both canonical formulas are derived here.', 'All connected p-primary infinite-loop generator families are determined by stable part, least degree and divisibility flag; the divisible case uses a two-stage connectivity comparison, and class families reduce objectwise to small subfamilies.'),
    'E.1': ('The proposed criterion is in the prompt, not a verified theorem of an opened primary source.', 'Four-object strict-pullback counterexample.'),
    'E.6': ('Derived from the opened properness/aspherical-generation equivalence; the unit-fiber formulation is proved here.', 'Both directions for every localization unit.'),
    'E.8': ('Not located as this bounded unit-fiber criterion in the opened sources.', 'Bounded subfibration catalogue, coherent section obstruction and strict Cat realization.'),
    'F.1': ('Refutes the implication left open in POLES A.16.', 'Finite relative-A witness plus separate checks of saturation, (8), (9) and failure of forward gluing.'),
    'F.1.1': ('Repairs XVI Corollary7.7.2 without its circular derivator argument; not attributed verbatim to Cisinski.', 'Simplicial transfer and double collages; Loc (9) is unnecessary.'),
    'F.3a': ('The asserted transfer is in the supplied unrefereed AI return 317.', 'Independent audit of the specific proof steps and primary-source interfaces; no Lean run claimed.'),
    'F.3b': ('A consequence of the opened model-localization and fundamental-localizer correspondence theorems.', 'The exact set-generated scope and the strict higher-nerve transport.'),
    'F.3c': ('CSS gives the obstruction; the model-localization assertion is an additional verified step here.', 'Stanculescu criterion, idempotent radical and universe-relative nonaccessibility.'),
    'G.1': ('Cisinski--Tabuada supplies the canonical spectrum action; the stated formula for W_D is derived here.', 'Constant-coefficient evaluation and cofiber detection for an arbitrary strong stable derivator.'),
    'G.2': ('Cisinski supplies accessible localization models; the exact coefficient-realization equality is derived here.', 'Mapping-space/Yoneda detection, retaining the relative-Theorem-A convention.'),
    'G.4': ('A consequence of G.6--G.7, not inferred from existence of a set of coorthogonal targets.', 'Unconditional small-universe existence for the full sphere class.'),
    'G.7': ('Not located as this compact-target accessibility theorem in the opened comparison sources.', 'Degreewise compact completion models and countable extension compactness.'),
    'H.2': ('The relevant accessibility statement is Cisinski Scholie4.2.17; its application is derived here.', 'The two-universe and class-parameter qualification.'),
    'H.3': ('CSS Proposition6.2 supplies the reduced-product input; the locally constant derivator example is constructed here.', 'Derivator verification, monadic restriction and bounded cochains.'),
    'H5.1': ('The groupoid equivalence is CGT2006 Theorem1.3; Bousfield gives the homological group inputs.', 'The exact INDLOCAL B.3/B.4/B.6 interface used in this return.'),
    'H5.8': ('Derived from the opened CGT group localization statements.', 'The corrected accessible component-preserving interval and inverse correspondence.'),
    'H5.9': ('Not located as this completion-accessibility assertion in the opened sources.', 'Heisenberg reduced products, finite-rank coefficient functionals and the measurable-cardinal obstruction.'),
    'I.1': ('The finite core theorem is standard and is compared with opened Barmak--Minian Section2.', 'A complete direct proof in the precise adjunction-zigzag formulation, including the empty case.'),
    'I.2': ('Barmak--Minian Corollary4.18 supplies the preserved invariant; the requested equivalence is refuted here.', 'The explicit 22-point example and exact stabilized-core relation.'),
    'I.3': ('Barmak--Minian Theorem3.10 gives the simple-type comparison.', 'The stated arbitrary one-point weak-equivalence formulation and exact Dwyer condition.'),
    'I.312': ('The elementary-expansion argument is in the supplied unrefereed AI return 312; Henry supplies the comparison theorem.', 'The proof and source interfaces are audited without claiming an independent formalization.'),
    'I.8a': ('The noncofibrant Dwyer example uses May--Stephan--Zakharevich Lemma3.13 and Proposition6.2.', 'Its exact consequence for the proposed equality on finite posets.'),
    'I.9c': ('The claimed construction is in supplied INDLOCAL D.16--D.17.', 'Explicit old/new horn-pushout order calculation and identity-rigidity verification.'),
}

fields = ['id', 'status', 'where_proved', 'exact_inputs_or_source_locations',
          'relation_to_opened_sources', 'verification_or_added_derivation',
          'manuscript_pages_settled', 'comparison_scope']
rows = []
for row in csv.DictReader((root/'REVLOC_results.csv').open(newline='')):
    ident = row['id']
    if row['status'] == 'Open':
        relation = 'Unresolved in this return; no opened theorem is represented as settling this statement.'
        extra = row['notes'] or 'Partial results and failed approaches are recorded in the named proof section and research notes.'
    else:
        relation, extra = special.get(ident, (
            'Established by the proof here from the specified opened inputs; no claim that its exact formulation is printed in those inputs.',
            'The claim and its following proof give the complete derivation, including the stated qualifications.'
        ))
    rows.append(dict(zip(fields, [ident, row['status'], row['where_proved'], row['depends_on'],
                                relation, extra, row['manuscript_pages_settled'],
                                'Opened locations in the bibliography and Part J only; not a novelty or exhaustive-literature assertion.'])))
with (root/'REVLOC_source_crosswalk.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(f'Wrote source comparisons for {len(rows)} numbered statements.')
