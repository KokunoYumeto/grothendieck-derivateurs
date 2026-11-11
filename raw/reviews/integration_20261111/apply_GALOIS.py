"""Integration of the reviewed Pro answer GALOIS (prompt 4) into the companion. Run once: python -I apply_GALOIS.py"""
import pathlib
import re
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from integ_lib import Run, CHK

R = Run('GALOIS', '4_GALOIS/REVIEW_author.md')
N = R.N


def bib_entry(cid, key):
    s = (CHK / f'DER_{cid}' / f'DER_{cid}_references.bib').read_bytes().decode('utf-8').replace('\r\n', '\n')
    m = re.search(r'@\w+\{' + re.escape(key) + r',.*?(?=\n@|\Z)', s, re.S)
    return m.group(0)


# ------------------------------------------------------------------ I-b
R.bib_add('I-b', [bib_entry('XVI', 'Cisinski2006')])
R.blocks_edit('I-b', 'new_I-b_GALOIS.tex')
R.overview_append('I-b', r"""
The object that these pages approach without naming it is the class $W^{\mathrm{lc}}_{\mathbb D}$ of the functors inducing an equivalence on locally constant coefficients (the 2-complete equivalences). For every derivator on all small categories it is a fundamental localizer satisfying the relative Theorem~A; the intermediate classes (1-complete, cohomological, homological) satisfy the relative Theorem~A and fail two-out-of-three, already for sets (commentary at ms.~100). For spaces all the classes coincide with the weak equivalences; for sets, truncated types, complexes over a ring and spectra they differ, and the values are tabulated in the commentary on Chapter~X, ms.~5. Replacing $\mathbb D$-equivalences by 1-complete or 2-complete ones throughout does not make the fibration statements of ms.~79--84 true: stability under composition and the detection of equivalences on fibres both fail for the substituted notions (commentary at ms.~118 and~122).
""")
AX = ('Holds for every derivator on all small categories: nerve weak equivalences induce equivalences on locally constant objects (Cisinski2009LocallyConstant, Corollary3.8), and an equivalence there implies full faithfulness and the preservation of cohomology and homology with locally constant coefficients (commentary at p100, part (a)).')
AXN = N('A.2', 'followed; Corollary 3.8 opened')
C3 = ('Among the coefficient theories computed, holds for spaces only (all classes equal W∞). Fails for sets, r-truncated types, complexes of modules over any nonzero ring, and spectra: e.g. e->BG for G a nontrivial group (acyclic where needed) is a constant-coefficient equivalence and is not 1-complete. Table in the commentary on Chapter X, ms.5.')
C3N = N('C.5, C.12, C.15', 'values derived independently in the review; C.11 and C.14 unverified and not used')
HOTN = 'Spaces are the only computed coefficient theory for which the five classes coincide (table in the commentary on Chapter X, ms.5). ' + N('C.5, C.15, D.8', 'C.5 and C.15 rederived in the review; D.8 unverified')
ENH = 'With an infinity-categorical enhancement of the coefficients the cohomological, homological and 1-complete classes coincide, without internal Homs. ' + N('C.2', 'rederived in the review')
D9 = 'The corrections of the Pro answer agree with the repair recorded here. ' + N('D.9', 'unverified; no change')
R.rows_edit('I-b', {
    'I-b-B097-03': {'repair': AX, 'notes+': AXN},
    'I-b-B098-03': {'repair': AX, 'notes+': AXN},
    'I-b-B100-03': {'repair+': AX, 'notes+': AXN},
    'Ib-C034': {'repair': AX, 'notes': AXN},
    'Ib-C036': {'repair': AX, 'notes': AXN},
    'Ib-C037': {'repair': AX, 'notes': AXN},
    'Ib-C038': {'repair': AX, 'notes': AXN},
    'Ib-C039': {'repair': AX, 'notes': AXN},
    'Ib-C087': {'repair': C3, 'notes': C3N},
    'Ib-C088': {'repair': C3, 'notes': C3N},
    'Ib-C089': {'repair': C3, 'notes': C3N},
    'Ib-C090': {'repair': C3, 'notes': C3N},
    'I-b-B079-03': {
        'repair': 'Replace the base equivalence by a 1-complete equivalence: the pullback is then a constant-coefficient D-equivalence (not a 1-complete one). Counterexamples to the original statement are supplied by Grothendieck on ms87-92. The alternative repair by restriction to completely D-aspherical test bases, recorded here before, is withdrawn: it has not been proved.',
        'notes+': N('D.2', 'unverified; the exact form of the conclusion is taken from its statement'),
    },
    'I-b-B079-04': {
        'repair+': 'As in row I-b-B079-03: a 1-complete input gives a constant-coefficient output.',
        'notes+': N('D.2', 'unverified'),
    },
    'I-b-B081-04': {
        'repair+': 'The 2-complete variant of ms.122 is not closed under composition either (commentary at p122).',
        'notes+': N('D.3, D.4', 'followed; own enumeration, checks_author/check_galois.py; D.3 is the example of the commentary at p118'),
    },
    'I-b-B084-01': {
        'notes+': 'Answer: yes. ' + N('D.7', 'followed; the companion had the same result, with proof, in the commentary at p84'),
    },
    'I-b-B084-06': {
        'repair+': 'A positive replacement: when the localizer of locally constant coefficients is accessible, the fibrations of its Thomason model structure are stable under composition and base change, and a functor of that localizer between two of them over S is in it on every fibre; right properness is not needed (commentary at p118, last paragraph). The accessibility is not verified.',
        'notes+': N('D.6; B.4 for the accessibility', 'D.6 followed from Cisinski2006, Theorem 5.2.15 (not opened in the review); B.4 unverified'),
    },
    'I-b-B084-07': {
        'notes+': 'The variant with 2-complete equivalences and complete asphericity substituted is false (commentary at p122, complement 1); the repair recorded here, with constant-coefficient equivalences over a completely D-aspherical base, is not affected. ' + N('D.5', 'followed'),
    },
    'I-b-B096-04': {
        'notes+': 'An affirmative answer under Der3a-prime is stated in the ' + N('D.8', 'unverified; the status stays conjectured until D.8 is read'),
    },
    'I-b-A069': {
        'notes+': 'For every derivator the doubled-arrow gluing step is stated to hold for the 2-complete and the 1-complete classes: ' + N('D.11', 'unverified'),
    },
    'Ib-C021': {'notes+': HOTN}, 'Ib-C026': {'notes+': HOTN}, 'Ib-C048': {'notes+': HOTN},
    'Ib-C069': {'notes+': HOTN}, 'Ib-C092': {'notes+': HOTN}, 'Ib-C096': {'notes+': HOTN},
    'Ib-C018': {'notes+': ENH}, 'Ib-C047': {'notes+': ENH}, 'Ib-C082': {'notes+': ENH},
    'I-b-B087-05': {'notes+': D9}, 'I-b-B093-04': {'notes+': D9}, 'I-b-B093-05': {'notes+': D9},
    'I-b-B095-01': {'notes+': D9}, 'Ib-C003': {'notes+': D9},
})

# ------------------------------------------------------------------ I-a
R.blocks_edit('I-a', 'new_misc_GALOIS.tex')
R.rows_edit('I-a', {
    'I-b-A020': {
        'notes+': 'The same closure pattern (composition and left cancellation, without two-out-of-three) is that of the 1-complete class of every derivator (commentary at p100, part (d)). ' + N('A.4, A.5', 'followed'),
    },
    'I-a-L063': {
        'notes+': 'The same closure pattern, without two-out-of-three, is that of the 1-complete class of every derivator (commentary on I ms.100). ' + N('A.4, A.5', 'followed'),
    },
})

# ------------------------------------------------------------------ VIII-X
R.blocks_edit('VIII-X', 'new_VIII-X_GALOIS.tex')
R.rows_edit('VIII-X', {
    'X021': {
        'repair+': 'The finer class of the functors inducing an equivalence on locally constant coefficients is also a fundamental localizer, with the relative Theorem A, for every derivator on all small categories (commentary on I ms.100).',
        'notes+': N('B.1, B.3', 'B.3 followed in full; B.1 (W_D, by Cisinski 2008, Proposition 3.7) not opened'),
    },
    'X022': {
        'notes+': 'The fibration statements of Chapter I do not extend to a general W: each of the fibration axioms Loc(7a,b,c) holds, for a localizer inside W_0, only for W∞ (commentary on XVI ms.65). ' + N('B.7', 'first half followed; agrees with POLES E.5'),
    },
    'X024': {
        'repair+': 'Confirmed: for an accessible fundamental localizer W the derivator of W-local spaces has W as its class of constant-coefficient equivalences. For a localizer that is not accessible the question is open.',
        'notes+': N('E.7', 'followed'),
    },
    'X038': {
        'repair+': 'Exact criterion: W_D is contained in W_0 if and only if D(e) is not equivalent to a preorder; the class defined by locally constant coefficients is contained in W_0 if and only if D(e) is not trivial (commentary at X ms.5, Five coefficient theories and their classes of equivalences).',
        'notes+': N('G.1, G.2', 'statements checked in the review'),
    },
    'X042': {
        'notes+': 'For the concrete meaning of La see row X038 and the commentary at X ms.5. ' + N('G.1, G.2', 'statements checked in the review'),
    },
})

# ------------------------------------------------------------------ VI-a, XIIc-a, XI-XIIa
R.blocks_edit('VI-a', 'new_misc_GALOIS.tex')
R.blocks_edit('XIIc-a', 'new_misc_GALOIS.tex')
CM = ('Coefficient meaning: for the derivator of n-truncated types the constant-coefficient equivalences are b_n, the 1-complete class is a_n and the '
      'class of equivalences on locally constant coefficients is b_{n+1}; the 1-complete class of a derivator fails two-out-of-three in general '
      '(commentary at p187, last paragraph). ' + N('C.4, C.5', 'rederived in the review') +
      ' The review\'s item 23 gives the indices as "b_n is W^lc of (n-1)-types and a_n its 1-complete class"; by the table (C.15) the 1-complete class of (n-1)-types is a_{n-1}, and the indices set here are those of the table.')
R.rows_edit('XIIc-a', {'A050': {'notes+': CM}, 'A062': {'notes+': CM}})
R.blocks_edit('XI-XIIa', 'new_misc_GALOIS.tex')

# ------------------------------------------------------------------ XVI
R.blocks_edit('XVI', 'new_misc_GALOIS.tex')
R.rows_edit('XVI', {
    'XVI-C019': {
        'repair+': 'Further examples: for every derivator the localizer of locally constant coefficients satisfies Loc(4), (6a), (8). Accessibility, Loc(9), of that localizer and of W_D is stated for the derivators of presentable coefficient theories and is open for a bare derivator.',
        'notes+': N('B.4, B.5, B.13', 'B.5 checked as a consequence of B.3; B.4 unverified; B.13 open in the answer'),
    },
})

# ------------------------------------------------------------------ XIIapp (row only)
R.rows_edit('XIIapp', {
    'XIIapp-G23': {
        'notes+': 'A precise form of the passage to higher degrees: coefficients in r-truncated types have W_r as constant-coefficient equivalences and W_{r+1} as equivalences on locally constant coefficients, so iterating gives the tower W_0, W_1, W_2, ... with intersection W∞; rationally there is the analogous tower (isomorphisms on pi_i for i<=r, rational isomorphisms above). ' + N('E.5, E.10', 'E.5 known; E.10 followed in outline, and it uses the accessibility statement B.4, unverified'),
    },
})

# ------------------------------------------------------------------ III-V
R.blocks_edit('III-V', 'new_III-V_GALOIS.tex')
KT = N('B.9-B.12', 'followed in full; Baumslag-Dyer-Heller not opened')
R.rows_edit('III-V', {
    'V-I052': {
        'notes+': 'For a small filtered index category, invariance of H under all weak equivalences forces the ind-object to be isomorphic in Ind(Cat hot) to its stagewise fundamental groupoids (commentary at V ms.46, A small ind-object that is homotopy invariant sees only 1-types). ' + KT,
    },
    'V-I053': {
        'notes+': 'See the commentary at V ms.46 for what an ind-object of Cat hot with small index can represent. ' + KT,
    },
    'V-I057': {
        'notes+': 'Consequence of the commentary at V ms.46: a homotopy invariant functor that is ind-represented in Cat hot by a small filtered system factors through the fundamental groupoid, whether or not the system is essentially constant. ' + KT,
    },
})

R.finish([
    '1 (new block at I ms.99-100): done, "The localizer of locally constant coefficients", with the proof of B.3 in five steps. The compatibility of the mates with units and counits is stated as standard, not written out (as in the review).',
    '2 (rows I-b-B097-03, B098-03, B100-03, Ib-C034, C036-C039): done; no status change.',
    '3 (rows Ib-C087-C090): done.',
    '4 (rows I-b-B079-03, B079-04): done; the alternative "completely D-aspherical test bases" is struck from the repair. D.2 itself is unverified and is cited as such.',
    '5 (row I-b-B081-04; block at ms.118): done.',
    '6 (block at ms.122): the companion already had the same tetrahedron example with proof. Added three complements (fibrewise detection, the reading of the edition, a shorter computation of the fundamental group). Nothing replaced.',
    '7 (row I-b-B084-01; block at ms.84): the companion already had the result with proof ("Universal equivalences give fully faithful restriction"). Row notes only; proof_status stays conjectured (source status), the answer yes is in repair and notes.',
    '8 (row I-b-B084-06): done; set in the last paragraph added to the block at ms.118; depends on accessibility (unverified).',
    '9 (row I-b-B084-07): done, notes only.',
    '10 (row I-b-B096-04): notes only; stays conjectured (D.8 unverified).',
    '11 (row I-b-A069): notes only (D.11 unverified).',
    '12 (rows Ib-C021, C026, C048, C069, C092, C096): notes only.',
    '13 (rows Ib-C018, C047, C082): notes only.',
    '14 (rows I-b-B087-05, B093-04, B093-05, B095-01, Ib-C003): notes only, no change of content.',
    '15 (overview of I-b): done, one paragraph.',
    '16 (I-a block at ms.61; rows I-a-L063, I-b-A020): done.',
    '17 (row X021): done. 18 (row X024): done. 19 (rows X038, X042): done. 21 (row X022): done.',
    '20 (new block at X ms.5): done, "Five coefficient theories and their classes of equivalences". The table is stated without derivations; the arithmetic criterion (C.9) is proved in the block by an argument written at the integration from the review\'s indication: a second reader should check it.',
    '22 (VI-a): one paragraph added to the status block at ms.40 (not to the blocks at ms.32-38 and 65-69). Rows VIa-141, 146, 148, 160: no change, as the review says.',
    '23 (XIIc-a block at ms.187; rows A050, A062): done, with the indices of the table C.15 (the review\'s sentence has an index slip, recorded in the row notes).',
    '24 (XI-XIIa, opening block): done; D.8 and D.1 are entered as stated, not verified.',
    '25 (row XVI-C019): done.',
    '26 (XVI ms.124): done as a further example at the end of the block "No homology localizer has enough intrinsic fibrations": the case k = Q is proved (the review\'s own test); the general statement for a ring k is entered as stated (properness half of B.7 unverified).',
    '27 (XVI ms.17-prime): done, stated without proof (B.6).',
    '28 (XVI block at ms.78): NOT changed: the [sic] on the order relation is the edition\'s reading and is already marked in the transcription; nothing mathematical to add.',
    '29 (row XIIapp-G23): done, notes only.',
    '30 (III-V rows V-I052, V-I053, V-I057; new block at V ms.46): done, "A small ind-object that is homotopy invariant sees only 1-types". The Kan-Thurston statement with a cardinal bound (B.10, B.11) is stated and NOT proved in the commentary; the lemma (B.9) and the proposition (B.12) are proved. The last step (isomorphism of ind-objects) is written out at the integration.',
])
