# Writes ZIP_LIST.tsv next to each of the seven unsent prompts (12 Nov 2026, Derivateurs expert).
# Columns: full path (Windows) <TAB> name in the zip (flat) <TAB> why it is needed.
# Checks that every listed path exists; prints the ones that do not.
import io, os, sys

B = 'C:/Users/user/Documents/derivateurs_companion_20261109'
R = B + '/pro_reviews_max_20261112'
DX = R + '/DERIVATEURS_EXPERT'
CX = R + '/1_CATHOT'
FR = B + '/corrected_french_20261111'
RET = B + '/pro_returns_20261110'
PP = B + '/pro_prompts_20261110'
Z3 = DX + '/work/zip_3/papers'
Z2 = DX + '/work/zip_2/papers'
CL = CX + '/work/lit'
CB = CX + '/work/background/papers'
CC = CX + '/work/code'
RR = 'C:/Users/user/Documents/recent_results_20261110/papers'

def fr(ch, why):
    return (FR + '/DER_%s.tex' % ch, 'DER_%s.tex' % ch, "Grothendieck's text, corrected French transcription of 11 Nov 2026: " + why)

COMMON = (PP + '/_COMMON_BLOCK.md', '_COMMON_BLOCK.md', 'rules of proof and conventions that the prompt refers to')

T = RET + '/2_TOTAL_ASPHERICITY/TOTASPH'
P = RET + '/3_POLES/POLES'
G = RET + '/4_GALOIS/GALOIS'
C = RET + '/1_CATHOT/CATHOT'

lists = {}

lists[DX + '/PRO_PROMPTS/TOTAL_EXACT'] = [
    COMMON,
    (PP + '/2_TOTAL_ASPHERICITY/PROMPT.md', 'TOTASPH_PROMPT.md', 'the prompt that TOTASPH answered (conventions, variance)'),
    (T + '/TOTASPH_paper.pdf', 'TOTASPH_paper.pdf', 'the return: statements and proofs of R1-R6'),
    (T + '/TOTASPH_results.csv', 'TOTASPH_results.csv', 'ids C.5, C.6, C.9-C.13, D.4, D.7, D.16-D.18 used in R1-R6'),
    (T + '/TOTASPH_report.md', 'TOTASPH_report.md', 'the return: what it tried on D.7'),
    (T + '/sections/C.tex', 'TOTASPH_C.tex', 'source of C.5, C.6, C.8-C.13 (R1-R5)'),
    (T + '/sections/D.tex', 'TOTASPH_D.tex', 'source of D.4, D.7, D.16-D.18 (R2, R4, R6)'),
    (T + '/sections/D_followup.tex', 'TOTASPH_D_followup.tex', 'the return: follow-up on Part D'),
    (T + '/sections/D_general.tex', 'TOTASPH_D_general.tex', 'the return: general localizers'),
    (T + '/research/CD_report.md', 'TOTASPH_CD_report.md', 'records that the proof of C.9 came from the Open Maths lesson'),
    (R + '/2_TOTAL_ASPHERICITY/REVIEW.md', '2_TOTAL_ASPHERICITY_REVIEW.md', 'the check of R1-R6 at effort max; row D.7 has R7 and R10'),
    (DX + '/RESULT_FILTERED_BY_ONE_TYPES.md', 'RESULT_FILTERED_BY_ONE_TYPES.md', 'proof of R8 (new, unchecked): to be checked in Part D.1'),
    (DX + '/HUNCHES.md', 'HUNCHES.md', 'H1: the reasons behind Parts A-C; R7'),
    (DX + '/FINDINGS.md', 'FINDINGS.md', 'F2-5, F2-6, F2-7 (R4, R7, R9), F2-13'),
    fr('II-a', 'II ms. 30-36ter (the conjecture)'),
    fr('XIIb-a', 'XII ms. 87-103 (Definition 1, final images)'),
    (DX + '/work/lit/IsbellMitchell1973_bull.pdf', 'IsbellMitchell1973.pdf', 'Th. 1, Lemma 1, Th. 3 used in R2, R3 and Part A'),
    (DX + '/work/lit/AKR1981.pdf', 'AdamekKoubekReiterman1981.pdf', 'Theorem [1], Construction C.1, Th. C.2 used in R4 and Part C'),
]

lists[DX + '/PRO_PROMPTS/PRESHEAF_TOTALITY'] = [
    COMMON,
    (PP + '/2_TOTAL_ASPHERICITY/PROMPT.md', 'TOTASPH_PROMPT.md', 'the prompt that TOTASPH answered (conventions, variance)'),
    (T + '/TOTASPH_paper.pdf', 'TOTASPH_paper.pdf', 'the return: statements and proofs of R1-R5, R8'),
    (T + '/TOTASPH_results.csv', 'TOTASPH_results.csv', 'ids E.8, F.6-F.9, F.15, F.18-F.27, G.3, G.5, A.12'),
    (T + '/sections/A.tex', 'TOTASPH_A.tex', 'A.12 (the acyclic semi-simplicial set of R6)'),
    (T + '/sections/C.tex', 'TOTASPH_C.tex', 'C.4, C.5 (covering argument; used by RESULT_FILTERED_BY_ONE_TYPES)'),
    (T + '/sections/E.tex', 'TOTASPH_E.tex', 'E.8 (R1)'),
    (T + '/sections/F.tex', 'TOTASPH_F.tex', 'F.6-F.27 (R1-R5)'),
    (T + '/sections/F_followup.tex', 'TOTASPH_F_followup.tex', 'the return: follow-up on Part F'),
    (T + '/sections/G.tex', 'TOTASPH_G.tex', 'G.3, G.5 (R8)'),
    (R + '/2_TOTAL_ASPHERICITY/REVIEW.md', '2_TOTAL_ASPHERICITY_REVIEW.md', 'the check of R1-R5, R8 at effort max; row F.27 has R6'),
    (P + '/POLES_paper.pdf', 'POLES_paper.pdf', 'the return: B.2, H.5, H.6 (R7)'),
    (P + '/POLES_results.csv', 'POLES_results.csv', 'ids B.2, H.5, H.6'),
    (R + '/3_POLES/REVIEW.md', '3_POLES_REVIEW.md', 'the check of R7 at effort max'),
    (DX + '/RESULT_FILTERED_BY_ONE_TYPES.md', 'RESULT_FILTERED_BY_ONE_TYPES.md', 'proof of R9 (new, unchecked): to be checked in Part F.1'),
    (DX + '/HUNCHES.md', 'HUNCHES.md', 'H3: the reasons behind Part A'),
    (DX + '/FINDINGS.md', 'FINDINGS.md', 'F2-11 (R8), F2-12, F2-13 (R9), F-G4'),
    fr('II-a', 'II ms. 36ter'),
    fr('XIIb-a', 'XII ms. 87-103'),
    fr('XIIb-b', 'XII ms. 104-169 (ms. 107-114: the Dwyer-type immersions)'),
    fr('XIIapp', 'XII appendix ms. 10-18'),
    fr('VII-a', 'the path categories'),
    fr('VII-b', 'the path categories; VII section 10'),
    (Z3 + '/2205.02353/Dwyer-pushout-scat.tex', 'HORR_2205.02353.tex', 'Hackney-Ozornova-Riehl-Rovelli: discretely flat (R5)'),
    (Z3 + '/Cisinski1999_Dwyer/CTGDC_1999__40_3_227_0.pdf', 'Cisinski1999_Dwyer.pdf', 'Dwyer morphisms'),
    (Z3 + '/Cisinski_Ast308/smf_ast_308.pdf', 'Cisinski_Asterisque308.pdf', 'Prop. 9.2.17 (R7); chapter 4'),
    (CX + '/OWN_RESULTS.md', 'CATHOT_OWN_RESULTS.md', 'section 6 describes the census offered in Part A.3'),
    (CC + '/catlib.py', 'catlib.py', 'census library (Part A.3)'),
    (CC + '/enum_monoids.py', 'enum_monoids.py', 'census of monoids (Part A.3)'),
    (CC + '/enum_cats.py', 'enum_cats.py', 'census of categories (Part A.3)'),
    (CC + '/enum_monoids_upto6.out', 'enum_monoids_upto6.out', 'census output'),
    (CC + '/enum_cats_upto7.out', 'enum_cats_upto7.out', 'census output'),
]

lists[DX + '/PRO_PROMPTS/REVERSIBLE_LOCALIZERS'] = [
    COMMON,
    (PP + '/3_POLES/PROMPT.md', 'POLES_PROMPT.md', 'the prompt that POLES answered (conventions)'),
    (P + '/POLES_paper.pdf', 'POLES_paper.pdf', 'the return: statements and proofs of R1-R5'),
    (P + '/POLES_results.csv', 'POLES_results.csv', 'ids B.2, B.5, B.6, C.5, C.10, D.1, E.2, F.2-F.6, F.13, F.14, H.8, A.16'),
    (P + '/POLES_report.md', 'POLES_report.md', 'the return: what it left open'),
    (P + '/sections/00_conventions.tex', 'POLES_conventions.tex', 'conventions of the return'),
    (P + '/sections/B.tex', 'POLES_B.tex', 'B.2, B.5, B.6 (R1)'),
    (P + '/sections/C.tex', 'POLES_C.tex', 'C.5, C.10 (R4)'),
    (P + '/sections/D.tex', 'POLES_D.tex', 'D.1 (R1)'),
    (P + '/sections/E.tex', 'POLES_E.tex', 'E.2 (R3)'),
    (P + '/sections/F.tex', 'POLES_F.tex', 'F.2-F.14 (R2, R5)'),
    (P + '/sections/H.tex', 'POLES_H.tex', 'H.8 (R3)'),
    (R + '/3_POLES/REVIEW.md', '3_POLES_REVIEW.md', 'the check of R1-R5 at effort max; rows C.5, F.14 and the additions R1-R5 there have R4-prime, R6, R7'),
    (G + '/GALOIS_paper.pdf', 'GALOIS_paper.pdf', 'the return: B.6, B.7 (R9); B.14'),
    (G + '/GALOIS_results.csv', 'GALOIS_results.csv', 'ids B.6, B.7, B.14'),
    (G + '/sections/conventions.tex', 'GALOIS_conventions.tex', 'conventions of the return'),
    (G + '/sections/B_loc67.tex', 'GALOIS_B_loc67.tex', 'source of B.6, B.7 (R9)'),
    (G + '/sections/B_KT.tex', 'GALOIS_B_KT.tex', 'B.14 (the open properness question, Part E.4)'),
    (R + '/4_GALOIS/REVIEW.md', '4_GALOIS_REVIEW.md', 'the check of R9 at effort max; rows B.7, B.14 have R10'),
    (DX + '/RESULT_REVERSIBLE_NOT_STABLE.md', 'RESULT_REVERSIBLE_NOT_STABLE.md', 'proof of R6 (unchecked): to be checked in Part A'),
    (DX + '/HUNCHES.md', 'HUNCHES.md', 'H4 (R7, Parts B-D), H6 (Part E)'),
    (DX + '/FINDINGS.md', 'FINDINGS.md', 'F3-1 to F3-7, F3-11 (R1-R8)'),
    (CX + '/OWN_RESULTS.md', 'CATHOT_OWN_RESULTS.md', 'Theorem 1.1 (R11), used in Part C'),
    (DX + '/CHECK_OF_CATHOT_OWN_RESULTS_20261112.md', 'CHECK_OF_CATHOT_OWN_RESULTS_20261112.md', 'the second reading of R11'),
    fr('I-b', 'I ms. 60-126 (D-equivalences; Part G)'),
    fr('XIIb-a', 'XII ms. 75-85 (W(7), W(7 bis), Theoreme 2)'),
    fr('XIIc-b', 'XII ms. 265-275 (the appendix on W(7), W(7 bis))'),
    fr('XVI', 'XVI in full (Loc axioms, Fib_W, Loc (7 F), footnote 56)'),
    (Z3 + '/Cisinski_Ast308/smf_ast_308.pdf', 'Cisinski_Asterisque308.pdf', 'chapters 4, 6, 9 (R3; 6.1.11, 6.1.14, 9.4.5, 9.4.7)'),
    (Z3 + '/Cisinski2004_minimal/CTGDC_2004__45_2_109_0.pdf', 'Cisinski2004_minimal.pdf', 'minimality of W-infinity'),
    (Z3 + '/HausmannHusemoller1979/ens-001_1979_25__36_d.pdf', 'HausmannHusemoller1979.pdf', 'acyclic maps'),
    (Z3 + '/BerrickCasacuberta1999/berc2.pdf', 'BerrickCasacuberta1999.pdf', 'plus-construction as a nullification'),
    (CL + '/miller/miller-sullivan-conjecture.pdf', 'Miller1984.pdf', "Miller's theorem used in R6 and R11"),
]

CATHOT_NOTES = [
    (CX + '/OWN_RESULTS.md', 'OWN_RESULTS.md', "the CATHOT expert's results with full proofs"),
    (CX + '/HUNCHES.md', 'HUNCHES.md', "the CATHOT expert's hunches (partial facts and smallest undecided instances)"),
    (CX + '/REVIEW.md', 'CATHOT_REVIEW.md', 'row-by-row check of the return CATHOT at effort max'),
    (DX + '/CHECK_OF_CATHOT_OWN_RESULTS_20261112.md', 'CHECK_OF_CATHOT_OWN_RESULTS_20261112.md', 'second reading of OWN_RESULTS sections 1-5'),
    (C + '/CATHOT_paper.pdf', 'CATHOT_paper.pdf', 'the return CATHOT'),
    (C + '/CATHOT_results.csv', 'CATHOT_results.csv', 'ids of the return'),
    (C + '/CATHOT_report.md', 'CATHOT_report.md', 'report of the return'),
]

FINMON = CATHOT_NOTES + [
    (CX + '/G6_VERDICT.md', 'G6_VERDICT.md', 'complete proof of R1, R2 (both routes)'),
    (CX + '/EMAIL_CLAIMS_CHECK.md', 'EMAIL_CLAIMS_CHECK.md', 'claim-by-claim check; (d) Theorem C; (g) the small models (R3, R6)'),
    (CX + '/FINDINGS.md', 'CATHOT_FINDINGS.md', 'F1-F15, G1-G5: the findings behind R1-R10'),
    (DX + '/FINDINGS.md', 'DERIVATEURS_FINDINGS.md', 'F-G4 (R11)'),
    (C + '/sections/G.tex', 'CATHOT_G.tex', 'Part G of the return (G.1-G.17)'),
    (CC + '/catlib.py', 'catlib.py', 'census library (R7; Parts A4, C1)'),
    (CC + '/enum_monoids.py', 'enum_monoids.py', 'census of monoids (R7)'),
    (CC + '/enum_monoids_upto6.out', 'enum_monoids_upto6.out', 'output: counts and homology triples'),
    (CC + '/enum_cats.py', 'enum_cats.py', 'census of categories (R7)'),
    (CC + '/enum_cats_upto6.out', 'enum_cats_upto6.out', 'output'),
    (CC + '/enum_cats_upto7.out', 'enum_cats_upto7.out', 'output'),
    (CC + '/higher_homology.py', 'higher_homology.py', 'mod-p Betti numbers (R9, H2)'),
    (CC + '/higher_homology_order5.out', 'higher_homology_order5.out', 'output'),
    (CC + '/higher_homology_order6.out', 'higher_homology_order6.out', 'output (6.1 (e))'),
    (CC + '/models_check.py', 'models_check.py', 'checks of P2, P3, R2, Z'),
    (CC + '/models_check.out', 'models_check.out', 'output'),
    (CC + '/resolution_check.py', 'resolution_check.py', 'exact check of the projective resolutions'),
    (CC + '/resolution_check.out', 'resolution_check.out', 'output'),
    (CC + '/theoremA_test.py', 'theoremA_test.py', 'the five numerical tests of Theorem A (R3)'),
    (CC + '/theoremA_test.out', 'theoremA_test.out', 'output'),
    (CC + '/cup_products.py', 'cup_products.py', 'cup products for the monoid of R10'),
    (CC + '/cup_products.out', 'cup_products.out', 'output'),
    (CL + '/benbassat/2610.38760v1.pdf', 'BenBassat_2610.38760v1.pdf', 'the preprint (Conjecture 7.1, Theorems A-C); its TeX source was not found on disk'),
    (CL + '/miller/miller-sullivan-conjecture.pdf', 'Miller1984.pdf', 'Theorem B = Theorem 10.1 (R1)'),
    (CL + '/miller/miller-sullivan-conjecture-correction.pdf', 'Miller1985_correction.pdf', 'the correction (does not touch Theorem B)'),
    (CL + '/atiyah/PMIHES_1961__9__23_0.pdf', 'Atiyah1961.pdf', '(6.10), (6.11), (7.2), (8.1) (R1, R4)'),
    (CL + '/arxiv_2502.05276v2/2502.05276v2.pdf', 'Sweeney_2502.05276v2.pdf', 'Examples 5.2, 5.3; the homology lists'),
    (CB + '/math_0202260/agt-2-3.tex', 'Fiedorowicz2002_math0202260.tex', 'Fiedorowicz 2002'),
    (CL + '/arxiv_2511.12657v1/2511.12657v1.pdf', 'MartinianSteinberg_2511.12657v1.pdf', 'recent work on monoid homology'),
    (CL + '/arxiv_2611.09718v1/2611.09718v1.pdf', 'CarcaciaCampos_2611.09718v1.pdf', 'recent work named in the first draft'),
    (CL + '/arxiv_1512.06088v1/1512.06088v1.pdf', 'CianciOttina_1512.06088v1.pdf', 'Cor. 5.8, Th. 5.10 (R8)'),
    (CB + '/math_0611156/math_0611156.tex', 'BarmakMinian_math0611156.tex', 'minimal finite models'),
    (CB + '/Hatcher_AT/AT.pdf', 'Hatcher_AT.pdf', 'Prop. 4C.1 (R5)'),
    (CB + '/Quillen_KtheoryI/bass-seattle.pdf', 'Quillen_KtheoryI.pdf', 'Theorems A and B'),
    fr('III-V', 'V ms. 51-52 (Hot_0)'),
    fr('VII-c', 'VII ms. 121-128'),
    fr('VIII-X', 'IX ms. 9-13, 23'),
    fr('XIIapp', 'XII appendix ms. 8-11, 15'),
]
lists[CX + '/PRO_PROMPTS/FINMON'] = FINMON
lists[CX + '/@EMAIL'] = FINMON

lists[CX + '/PRO_PROMPTS/INDLOCAL'] = CATHOT_NOTES + [
    (DX + '/RESULT_FILTERED_BY_ONE_TYPES.md', 'RESULT_FILTERED_BY_ONE_TYPES.md', 'R5 (unchecked), used in Part C3'),
    (R + '/4_GALOIS/REVIEW.md', 'GALOIS_REVIEW.md', 'rows B.9-B.12: the check of Proof 2 of R2 and R3 at effort max'),
    (C + '/sections/BC.tex', 'CATHOT_BC.tex', 'B.7 (simple acyclic groups), C.1-C.6 (R1)'),
    (C + '/sections/D.tex', 'CATHOT_D.tex', 'D.1-D.9 (R1)'),
    (C + '/sections/E.tex', 'CATHOT_E.tex', 'E.4, E.6, E.14, E.17 (R1, Parts C, D)'),
    (C + '/sections/E_ind.tex', 'CATHOT_E_ind.tex', 'E.17 and its reduction'),
    (C + '/sections/E_path.tex', 'CATHOT_E_path.tex', 'E.21-E.27 (Part C4)'),
    (G + '/GALOIS_paper.pdf', 'GALOIS_paper.pdf', 'the return GALOIS: B.9-B.12 (Proof 2 of R2, R3)'),
    (G + '/GALOIS_results.csv', 'GALOIS_results.csv', 'ids B.9-B.12'),
    (G + '/sections/conventions.tex', 'GALOIS_conventions.tex', 'conventions of the return'),
    (G + '/sections/B.tex', 'GALOIS_B.tex', 'source of B.9, B.10'),
    (G + '/sections/B_KT.tex', 'GALOIS_B_KT.tex', 'source of B.11, B.12'),
    fr('III-V', 'V ms. 11-13, 37-52'),
    fr('VII-b', 'VII ms. 50-102'),
    fr('VII-c', 'VII ms. 108-150'),
    fr('VIII-X', 'IX ms. 9-13, 22-25'),
    (CB + '/Thomason1980_CatModel/CTGDC_1980__21_3_305_0.pdf', 'Thomason1980.pdf', 'the Thomason model structure'),
    (CB + '/Raptis_posets/raptis-poset.pdf', 'Raptis2010.pdf', 'posets; non-monoidality (Part D)'),
    (CB + '/MayZakharevichStephan_equivposets/May-al._58-2.pdf', 'MayStephanZakharevich2017.pdf', 'fibrant posets'),
    (CB + '/Quillen_KtheoryI/bass-seattle.pdf', 'Quillen_KtheoryI.pdf', 'Theorems A and B'),
    (Z3 + '/HausmannHusemoller1979/ens-001_1979_25__36_d.pdf', 'HausmannHusemoller1979.pdf', 'acyclic maps (R2, R3)'),
    (CL + '/arxiv_2510.16879v1/2510.16879v1.pdf', 'PalmerWu_2510.16879v1.pdf', 'summary of the Kan-Thurston theorem (Proof 1 of R2)'),
    (CL + '/arxiv_1412.0317v4/1412.0317v4.pdf', 'Shoikhet_1412.0317v4.pdf', 'named in the first draft'),
    (CL + '/arxiv_math_0110316v1/math_0110316v1.pdf', 'ChacholskiScherer_math0110316v1.pdf', 'homotopy colimits'),
    (RR + '/317_Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026.pdf', 'OpenAI_317_Thomason_nCat.pdf', 'Part E (claimed, unrefereed)'),
]

lists[CX + '/PRO_PROMPTS/S2COUNT'] = CATHOT_NOTES + [
    (C + '/sections/D.tex', 'CATHOT_D.tex', 'D.2-D.6 (R1)'),
    (C + '/sections/E.tex', 'CATHOT_E.tex', 'E.8 (R1)'),
    (CC + '/cup_products.py', 'cup_products.py', 'cup products for the monoid of R3'),
    (CC + '/cup_products.out', 'cup_products.out', 'output'),
    (CC + '/catlib.py', 'catlib.py', 'library used by the programs'),
    (CC + '/higher_homology.py', 'higher_homology.py', 'mod-p Betti numbers (R4)'),
    (CC + '/higher_homology_order6.out', 'higher_homology_order6.out', 'output (R4)'),
    (CC + '/resolution_check.py', 'resolution_check.py', 'exact check of projective resolutions'),
    (CC + '/resolution_check.out', 'resolution_check.out', 'output'),
    (CL + '/arxiv_2502.05276v2/2502.05276v2.pdf', 'Sweeney_2502.05276v2.pdf', 'Examples 5.2, 5.3 (R3)'),
    (CL + '/benbassat/2610.38760v1.pdf', 'BenBassat_2610.38760v1.pdf', 'the monoids M(Y, f) (Part A3)'),
    (CL + '/miller/miller-sullivan-conjecture.pdf', 'Miller1984.pdf', 'maps from classifying spaces'),
    (CB + '/Hatcher_AT/AT.pdf', 'Hatcher_AT.pdf', 'reference'),
    fr('III-V', 'V ms. 43-46, 51-52'),
    fr('VII-c', 'VII ms. 121-124, 129-132'),
]

missing = 0
for folder, rows in lists.items():
    if folder.endswith('/@EMAIL'):
        out = CX + '/PRO_PROMPT_EMAIL_CLAIMS_ZIP_LIST.tsv'
    else:
        out = folder + '/ZIP_LIST.tsv'
    names = [r[1] for r in rows]
    assert len(names) == len(set(names)), ('duplicate zip name', folder)
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(u'full_path\tname_in_zip\twhy_needed\n')
        for path, name, why in rows:
            if not os.path.exists(path):
                missing += 1
                print('MISSING', path)
            f.write(u'%s\t%s\t%s\n' % (path.replace('/', chr(92)), name, why))
    print(len(rows), out)
print('missing:', missing)
