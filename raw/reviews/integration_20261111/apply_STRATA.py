"""Integration of the reviewed Pro answer STRATA (prompt 5) into the companion. Run once: python -I apply_STRATA.py"""
import pathlib
import re
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from integ_lib import Run, CHK, HERE

R = Run('STRATA', '5_STRATA/REVIEW_author.md')
N = R.N
RET = HERE.parent.parent / 'pro_returns_20261110' / '5_STRATA' / 'STRATA' / 'STRATA_references.bib'


def entry(path, key):
    s = path.read_bytes().decode('utf-8').replace('\r\n', '\n')
    m = re.search(r'@\w+\{' + re.escape(key) + r',.*?(?=\n@|\Z)', s, re.S)
    return m.group(0).rstrip()


def chunk_entry(cid, key):
    return entry(CHK / f'DER_{cid}' / f'DER_{cid}_references.bib', key)


# ------------------------------------------------------------------ VI-c
R.blocks_edit('VI-c', 'new_VI-c_STRATA.tex')
R.overview_append('VI-c', r"""
Three notions of a well-behaved functor to the base must be kept apart in these pages: the bifibrations (Grothendieck fibrations that are also opfibrations), the functors that are proper and smooth (conditions on categories of lifts, satisfied by every bifibration and by the perfect objects), and the weak fibrations. A four-element poset over the interval is proper, smooth and a fibration without being an opfibration, and a filtered colimit of bifibrations need not be a fibration. For the question of ms.~186, whether bifibrations suffice to present the locally constant theory, the commentary now proves essential surjectivity for $W_\infty$ over every base in which all arrows are monomorphisms or all are epimorphisms (in particular over every poset), over every base whose classifying space is a 1-type, and for local systems of 1-types; the general case is undecided, with a five-element monoid of the homotopy type of the 2-sphere as first test, and the equivalence half of the question is untouched.
""")
R.rows_edit('VI-c', {
    'VIc-C022': {
        'repair': 'For W∞, essential surjectivity is proved: (a) when every arrow of S is a monomorphism, or every arrow an epimorphism, in particular for every poset (commentary at p186, Bifibrations over posets and over bases with cancellation); (b) when BS is a 1-type, which contains the groupoid case of the commentary and the bases with an initial or terminal object; (c) for local systems whose values are 1-types, over every base. Undecided in general: first test, the five-element monoid {1, e_ij} of the homotopy type of S^2 with the path local system; a strict diagram with fibration transitions cannot represent it. The equivalence half of the question is not addressed. Free cloven bifibrations exist for every p:X→S but their unit is not known to be fibrewise in W.',
        'references': 'commentary at p186; ClarkeSchererZeilberger2025',
        'notes': N('E.5, E.6, E.8, E.9, E.10, E.11', 'E.10 followed in full; E.8, E.9 followed; E.11 open in the answer; the remark on idempotents is the reviewer\'s') + ' The STRATA files call this row VIc-C008 (numbering of the first return). Open is the manuscript status. Not found in the sources consulted; no priority is claimed.',
    },
    'VIc-C023': {
        'notes+': 'The construction of the commentary at p186 is functorial on strict simplicial models once a bound on the sizes of the fibrant replacements is fixed, over bases with cancellation only. ' + N('E.10', 'followed'),
    },
    'VIc-C019': {
        'notes+': 'A bifibration is proper and smooth, with adjoint transition functors; the converse fails (four-element poset over [1]: proper, smooth, a fibration, not an opfibration; commentary at p186, Lemma 1). ' + N('E.1, D.6', 'followed; own enumeration'),
    },
    'VIc-C021': {
        'notes+': 'A fibration is an opfibration exactly when its transition functors have left adjoints; so the transition functors of a bifibration are weak equivalences without further hypothesis (commentary at p186, Lemma 1). ' + N('E.1', 'followed'),
    },
    'VIc-C044': {
        'repair+': 'For W∞ this holds without W(6 bis) as a separate axiom: lifting categories commute with filtered colimits. The limit is not in general a bifibration (commentary at p194, last paragraph).',
        'notes+': N('E.3, E.4', 'E.3 followed in outline and not compared line by line with this row; E.4 followed, own check'),
    },
    'VIc-C045': {
        'repair+': 'For W∞ this holds without W(6 bis) as a separate axiom.',
        'notes+': N('E.3', 'followed in outline'),
    },
})

# ------------------------------------------------------------------ I-a
R.bib_add('I-a', [entry(RET, 'BGH2020'), entry(RET, 'Aoki2023')])
R.blocks_edit('I-a', 'new_misc_STRATA.tex')
R.rows_edit('I-a', {
    'I-a-E024': {
        'notes+': 'Categories with finitely many arrows in which every arrow is monic and the only endomorphisms are identities are the ones with a literal stratified realization over the poset of their objects, parallel arrows included; the three-object, nine-arrow category whose classifying space is the real projective plane is an example (commentary at p4, item 6). ' + N('B.1, B.3, B.4', 'B.1 and B.4 followed, own check; the coarsening step of B.3 unverified'),
    },
    'I-a-L014': {
        'notes+': 'Converse for space-valued coefficients: right base change along all strict pullbacks characterizes properness (commentary at p52, last paragraph). ' + N('D.3, D.4', 'followed'),
    },
})

# ------------------------------------------------------------------ VI-a, VI-b, XIIb-a
R.blocks_edit('VI-a', 'new_misc_STRATA.tex')
R.blocks_edit('VI-b', 'new_misc_STRATA.tex')
R.blocks_edit('XIIb-a', 'new_misc_STRATA.tex')

# ------------------------------------------------------------------ XIIapp
R.bib_add('XIIapp', [entry(RET, 'CDDouteauWaas2022')])
R.blocks_edit('XIIapp', 'new_misc_STRATA.tex')
R.rows_edit('XIIapp', {
    'XIIapp-G11': {
        'notes+': 'The category of crossing arrows is the homotopy link of BB in BX (Douteau-Waas), and the gluing formula has a second proof at the level of categories, valid for every fundamental localizer with the relative Theorem A and using no reverse excision (commentary at p18, complements). ' + N('C.2, C.3, C.5 (and POLES G.19)', 'C.2 known, source opened; C.3 followed; C.5 followed in outline'),
    },
})

# ------------------------------------------------------------------ XIIc-a, XVI, XI-XIIa
R.bib_add('XIIc-a', [chunk_entry('XVI', 'Cisinski2006')])
R.blocks_edit('XIIc-a', 'new_misc_STRATA.tex')
R.blocks_edit('XVI', 'new_misc_STRATA.tex')
R.blocks_edit('XI-XIIa', 'new_misc_STRATA.tex')

R.finish([
    '1 (row VIc-C022): done; status stays open.',
    '2 (new block at VI ms.186): done, "Bifibrations over posets and over bases with cancellation": E.1, E.5, E.6 as lemmas, E.10 with its proof, E.8 and E.9 stated without proof, E.11 with the reviewer\'s remark on idempotents. Placed after "What the bifibration question asks" (the review names a block "Perfect maps and strict bifibrations", which does not exist under that title).',
    '3 (row VIc-C023): done. 4 (rows VIc-C019, C021; block): done; the separating poset is set as x<a,b<c with x over 0 and a,b,c over 1 (the assignment was reconstructed at the integration: fibration, not opfibration, lifting posets with greatest elements).',
    '5 (rows VIc-C044, C045; E.4 in the block at ms.194): done.',
    '6 (overview of VI-c): done, one paragraph.',
    '7 (I-a block at ms.52-54; row I-a-L014): done. Rows I-a-L018 to L023: no change, as the review says.',
    '8 (I-a block at ms.2): done; Groth 2013 was NOT opened at the integration; the paragraph says that the statement numbers were not checked.',
    '9 (new block at I ms.4): done as a STATUS block without proofs, "Ordered sets as stratified spaces: what is proved" (A.1, A.2, A.4, A.11, D.5, D.7, D.8, B.3, B.4, B.7). The coarsening step (A.4, B.3) is marked as not opened; the extension of D.8 to all proper maps (BISITE D.11) is marked as unverified.',
    '10 (row I-a-E024): done. 11 (row Ib-C003): no change needed.',
    '12 (VI-a): one paragraph added to the block at ms.69 (B.9, B.10, B.12, A.10). Rows VIa-267, VIb-A006: no change.',
    '13 (VI-b, block at ms.83): done (G.1, B.7).',
    '14 (row XIIba-A-003): no change needed. 15 and 16 (XIIb-a block at ms.62): done in one paragraph (C.6, C.7, C.8 and the sentence on discrete flatness).',
    '17 and 18 (XIIapp block at ms.18; row XIIapp-G11): done (C.2, C.5, C.3). C.4 is already the example of the next block ("Why replacing arrows by all paths changes the answer"); nothing added for it.',
    '19 (XII ms.88-89, G.2): no change needed (second proof of a statement already integrated).',
    '20 (XIIc-a block at ms.187): done (G.4, G.3 with the translation-groupoid example).',
    '21 (XVI): the sentence from E.12 is added to the block at ms.43. The pointer to G.5 at ms.83-85 was NOT added (a third account of a dichotomy the chunk already proves twice).',
    '22 (XI-XIIa, block at ms.131): done.',
])
