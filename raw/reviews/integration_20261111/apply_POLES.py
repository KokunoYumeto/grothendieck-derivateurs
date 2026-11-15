"""Integration of the reviewed Pro answer POLES (prompt 3) into the companion. Run once: python -I apply_POLES.py"""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from integ_lib import Run

R = Run('POLES', '3_POLES/REVIEW_author.md')
N = R.N

# ------------------------------------------------------------------ XVI
R.blocks_edit('XVI', 'new_XVI_POLES.tex')
R.overview_append('XVI', r"""
The chapter's axioms fall into two groups that cannot be held together, and the commentary now proves this. The fibration axiom Loc~(7) holds only for $\mathbf W_\infty$ and for the class of all functors (commentary at ms.~65). The reverse excision axiom Loc~(6b), already in its single-square form, forces a localizer to contain every integral homology equivalence; the class $W_{H\mathbb Z}$ of those is the least localizer satisfying it, the localizers satisfying it are not all the localizers above $W_{H\mathbb Z}$ (the localizer $W_0$ is not one), and such a localizer, unless it is the class of all functors, makes no sphere aspherical and never has enough intrinsic fibrations (commentary at ms.~27). In particular no homology localizer $W_E$, $E$ a nonzero spectrum, satisfies Loc~(7F) (commentary at ms.~124), whereas the truncation localizers $\mathbf W_n$ satisfy Loc~(7F) and fail reverse excision. Theorem~5.4 is therefore false in the entry Loc~(6) of its list and correct in the others, and the conjectured $\widetilde{\mathbf W}_\infty$ is $\mathbf W_\infty$, or does not exist, or is the class of all functors, according to the reading (commentary at ms.~87).
""")
R.rows_edit('XVI', {
    'XVI-C105': {
        'repair': 'No, for every generalized homology theory: for a spectrum E not zero, the localizer W_E of the E-homology equivalences (in particular W_R for a nonzero ring R, and the integral homology localizer) has not enough intrinsic fibrations. Proof in the commentary at ms.124, No homology localizer has enough intrinsic fibrations, which uses the commentary at ms.27, Reverse excision excludes the fibration axioms. For cohomology with coefficients in a field the class of equivalences is the same as for homology; no statement is made for other cohomological classes. The finite n-equivalence cases are affirmative (row XVI-C048).',
        'references': 'commentary at p27 and p124; Cisinski2006, Theorem5.2.15, Example6.1.14 and Proposition4.2.4',
        'notes': N('C.4, C.5, F.8, H.8 and the necessity half of E.2', 'followed step by step; own check that the endomorphism alpha of the free group is not surjective (checks_author/check_poles.py)') + ' The source asks for examples, not a precise theorem for a fixed coefficient theory. Not found in the sources consulted; no priority is claimed.',
    },
    'XVI-C073': {
        'repair': 'No: the integral homology localizer satisfies Loc6a, Loc8 and Loc9 and has not enough intrinsic fibrations (commentary at ms.124). Affirmative for accessible proper localizers: right properness identifies the model fibrations with intrinsic ones. A Quillen realization by itself is insufficient.',
        'references': 'commentary at p124; Cisinski2006, Theorem5.2.15 and Example6.1.14',
        'notes': N('C.2, C.3, C.5', 'C.3 and C.5 followed; the accessibility of the homology localizers (C.2) is taken as standard and was not followed') + ' Do not silently conflate this with the now-solved model-existence question.',
    },
    'XVI-B099': {
        'repair': 'Affirmative for every finite n>=0, as in row XVI-C048 (commentary at ms.124): W_n is accessible and proper, and its Thomason model structure has intrinsic fibrations. Stated in the Pro answer named in the notes and not verified: p:T->B is in Fib_{W_n} if and only if for every X->B the n-truncation of B(T x_B X) is the homotopy pullback of the n-truncations of BT and BX over that of BB.',
        'references': 'Cisinski2006, §9.2.1, Corollaries4.3.28 and9.2.15, Theorem5.2.15, Example6.1.14; commentary at p124',
        'notes+': N('C.9', 'unverified') + ' The affirmative answer does not depend on C.9.',
    },
    'XVI-C038': {
        'repair+': 'Third reading, without the bound inside W∞ and with the literal list: the intersection of the localizers satisfying it is Fl(Cat) (commentary at p87).',
        'notes': N('D.4', 'followed, except the reduction (E.4) behind Loc7 holding only for W∞ and Fl(Cat), for which the companion has its own argument at ms.65'),
    },
    'XVI-C039': {
        'notes+': 'Without the bound inside W∞ the literal list gives Fl(Cat) (commentary at p87). ' + N('D.2, D.4', 'followed'),
    },
    'XVI-C040': {
        'repair+': 'Without the bound inside W∞, the intersection for the literal list is Fl(Cat). The conjecture is false in each of the three readings.',
        'notes': N('D.4', 'followed'),
    },
    'XVI-A092': {
        'notes+': 'For fundamental localizers satisfying the relative axiom (3 bis), (6a) and (6-prime a) both hold outright, by forward gluing from the relative Theorem A. Under the weak axioms of Definition 1.1 the question depends on whether Loc(1,2,3) imply Loc(3 bis); that implication was left open in the answer (A.16) and is refuted for the literal axioms by BISITE A.32 (literature check not done; see the commentary at ms.2-3). ' + N('A.11, A.16, B.2', 'B.2 followed; A.11 unverified'),
    },
    'XVI-A112': {
        'notes+': 'For fundamental localizers satisfying the relative axiom (3 bis) the forward cube axiom holds outright; the weak-axiom form depends on POLES A.16 (see row XVI-A092). ' + N('A.11, B.2', 'B.2 followed; A.11 unverified'),
    },
})

# ------------------------------------------------------------------ XIIb-a
R.blocks_edit('XIIb-a', 'new_XIIb-a_POLES.tex')
DW = ('The failure of W(7 bis) for W∞ persists when the inclusions are Dwyer maps, and a localizer satisfying W(7 bis) contains every '
      'integral homology equivalence (commentary on XVI ms.27); the hypothesis cannot be dropped. '
      + N('B.5, B.6, B.8', 'followed; the 141-object model of the Dwyer-map version was not recomputed'))
R.rows_edit('XIIb-a', {
    'XIIba-A-053': {
        'repair': 'Yes, without W(7 bis) and without its converse half, for every fundamental localizer satisfying the relative axiom (such a localizer is strongly saturated): if the intersection K is empty, W is the class of all functors; otherwise e->K is in W, forward gluing identifies the union with the wedge of U and V in the localization, and U->e is a retract of the map from the wedge to e. Outline in the commentary at ms.76, Ordinary covers yield homotopy pushouts, with one direction of excision; the retract step is written out in the commentary at ms.272.',
        'references': 'GrothendieckDerivateursXVI, section3; commentary at p76 and at XII ms.272',
        'notes': N('F.11, F.12', 'argument followed and completed for the empty intersection') + ' For the weak axioms without the relative Theorem A no statement is made.',
    },
    'XIIb-a-B002': {'notes+': DW},
    'XIIb-a-B003': {'notes+': DW},
    'XIIb-a-B012': {'notes+': DW},
    'XIIb-a-B015': {'notes+': DW},
})

# ------------------------------------------------------------------ XIIb-b
R.blocks_edit('XIIb-b', 'new_XIIb-b_POLES.tex')
G8 = ('A second counterexample for W∞ to the reverse direction without strong W(7 bis) (110 objects, 1051 arrows) is stated in the '
      + N('G.8', 'unverified; not compared with the witness of the commentary at ms.157'))
R.rows_edit('XIIb-b', {
    'XIIbb-A045': {
        'repair+': 'Stronger conclusion: under the same hypothesis every functor inducing isomorphisms on integral homology lies in W, and these functors form the least such class (complement at the end of the commentary at ms.126; commentary on XVI ms.27).',
        'notes+': N('B.5, B.6', 'followed; the companion has an independent proof with the cube axiom at XVI ms.27'),
    },
    'XIIb-b-B036': {'notes+': G8},
    'XIIbb-C019': {'notes+': G8},
})

# ------------------------------------------------------------------ XIIc-a
R.blocks_edit('XIIc-a', 'new_XIIc-a_POLES.tex')
R.rows_edit('XIIc-a', {
    'A029': {
        'repair+': 'The middle arrow is strict for every n>=3: the inclusion of S^2 v S^{n-1} into S^2 x S^{n-1} satisfies c_n and not b_n (commentary at p187).',
        'notes+': N('E.7', 'unverified in the review; the short proof set in the commentary was written at the integration and has not been read by a second reader'),
    },
})

# ------------------------------------------------------------------ XIIc-b (row only)
R.rows_edit('XIIc-b', {
    'XIIcb-C028': {
        'notes+': 'A direct proof from the factorization hypothesis alone, by a finite Reedy calculus, is given in the ' + N('G.26', 'unverified; long, to be read before it is set in the commentary') + ' The answer by Cisinski2010 stands independently of it.',
    },
})

R.finish([
    '1 (row XVI-C105; new block at ms.124): done. Block "No homology localizer has enough intrinsic fibrations"; the lemma and Proposition 2 it uses are in the new block at ms.27.',
    '2 (block at ms.124 on properness): done by a paragraph at its end. Only the necessity of aspherical generation is proved in the commentary; the equivalence with right properness (POLES E.2) is stated as not checked.',
    '3 (row XVI-C073): done. Accessibility of the homology localizers is stated as standard, not proved.',
    '4 (row XVI-B099): done; the description of Fib_{W_n} (C.9) is entered as stated and not verified.',
    '5 (block at ms.27): done by two results at its end: the single-square form with the cofibre test (proved for weak localizers; the equivalence with the cube forms under (3 bis) is stated, not reproduced), and W_0 as a non-reversible localizer above the integral homology localizer.',
    '6 (new block at ms.27): done, "Reverse excision excludes the fibration axioms" (POLES D.3, C.4, H.8, D.2). The inclusion of a non-total reversible localizer in W_0 (Loc 5) is stated and not reproduced.',
    '7 (block at ms.87; rows C038, C039, C040): done.',
    '8 (optional block on localizing subcategories of spectra): NOT done. The review makes it conditional on a check of F.9, which has not been made.',
    '9 (overview of XVI): done, one paragraph.',
    '10 (rows XVI-A092, A112): done; A.16 is cited as open in POLES and refuted for the literal axioms by BISITE A.32, literature check not done.',
    '11 (row XIIba-A-053; block at ms.76): done; the argument is set in outline in an exposition block, with the pointer to ms.272.',
    '12 (blocks at ms.78 and ms.79; rows XIIb-a-B002, B003, B012, B015): done; the Dwyer-map version is stated as not reproduced; no status change.',
    '13 (row XIIbb-A045; block at ms.126): done, with a complete proof in the cosieve form of that block.',
    '14 (rows XIIb-b-B036, XIIbb-C019): done in the notes only; G.8 is unverified and was not compared with the block at ms.157.',
    '15 (row A029 of XIIc-a; block at ms.187): done. POLES E.7 is unverified in the review; the proof in the commentary (cell structure and cup products) was written at the integration: a second reader should check it.',
    '16 (row XIIcb-C028): done in the notes only (G.26 unverified). Rows C011, C020, C038: no change, as the review says.',
])
