"""Integration of the reviewed Pro answer PATHS (prompt 6) into the companion. Run once: python -I apply_PATHS.py"""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from integ_lib import Run, HERE

R = Run('PATHS', '6_PATHS/REVIEW_author.md')
N = R.N

# two corrections of wording in the block file before it is applied (idempotent)
p = HERE / 'new_misc_PATHS.tex'
s = p.read_text(encoding='utf-8')
for old, new in (
    (' The inclusion holds in fact only for $W_\\infty$ and for the class of all functors (commentary on Chapter~XVI, ms.~65).', ''),
    ('there is a sieve inclusion obtained in this way whose pushout along a functor from a contractible source is a category with six objects and twenty arrows having the homology of $S^3$.',
     'there is a sieve inclusion obtained in this way, and a functor from its source to a category $A$, such that the pushout of a contractible category is a category with six objects and twenty arrows having the homology of $S^3$.'),
):
    if old in s:
        s = s.replace(old, new)
p.write_text(s, encoding='utf-8', newline='\n')
# the block "An interval with room at both ends" is in both overlapping chunks XIIc-a and XIIc-b
sec = s.split('%%FILE XIIc-b\n', 1)[1].split('%%FILE ', 1)[0]
(HERE / 'new_XIIc-a_interval_PATHS.tex').write_text(sec, encoding='utf-8', newline='\n')

CP = N('C.P1-C.P5', 'C.P1 and C.P5 followed in full; C.P2-C.P4 followed in outline, the passage through the homotopy coherent nerve not unfolded')

# ------------------------------------------------------------------ VII-b
R.blocks_edit('VII-b', 'new_misc_PATHS.tex')
R.rows_edit('VII-b', {
    'VIIb-C026': {
        'repair+': 'Exact condition: a base functor u:J→T induces weak equivalences of total categories for every strict F:T^op→Cat if and only if every comma category u/t is weakly contractible; for a filtered index the total category is weakly equivalent to the colimit in Cat. For the path categories the comparisons between a cofinal sequence, any other, and all types are canonical weak equivalences for every admissible Σ, by the action of the categories of maps of types (commentary at p112 and p117, last paragraphs); they are not invertible in Cat hot in general (commentary on VII ms.121).',
        'notes+': N('A.2, A.3, A.4, A.7, C.P1-C.P3, C.P5', 'A.2-A.4 followed; C.P2, C.P3 followed in outline'),
    },
})

# ------------------------------------------------------------------ VII-c
R.blocks_edit('VII-c', 'new_misc_PATHS.tex')
R.rows_edit('VII-c', {
    'VIIc-A046': {
        'repair': 'No in the general fibred setting (the FI^op comparison is not invertible even in Hot). For the geometric padding functors of the path categories: they are weak equivalences for every admissible Σ, and they are not invertible in Cat hot in general: for the four-element ordered set 0<1, 0<3, 2<1, 2<3 with all arrows marked the one-sided inclusion has no inverse modulo natural transformations. Commentary at p121, The padding functors are weak equivalences and are not invertible modulo natural transformations.',
        'notes': CP + ' Source question; not found in the sources consulted, no priority claimed.',
    },
    'VIIc-C042': {
        'repair+': 'The functor is not a Grothendieck fibration either, already for X=[1]; the variant with paths eventually constant on both sides is smooth and proper and is neither a fibration nor an opfibration (commentary at p157, last paragraph).',
        'notes+': N('E.3, E.4', 'followed; the first half of E.3 is the correction already recorded in this row'),
    },
    'VIIc-C005': {
        'notes+': 'The eventually constant path functor to X×X is smooth and proper, not a fibration or opfibration; it gives a natural factorization of every functor into a weak equivalence followed by a smooth and proper functor whose strict fibres are the homotopy fibres (compare XII ms.188-207). ' + N('E.4, E.5', 'E.4 followed for [1]; E.5 followed given CATHOT E.20-E.25'),
    },
})

# ------------------------------------------------------------------ III-V
R.blocks_edit('III-V', 'new_misc_PATHS.tex')
R.rows_edit('III-V', {
    'V-I066': {
        'repair+': 'For the path categories of Chapter VII the answer is: canonical and transitive weak equivalences (isomorphisms in Hot) for every admissible Σ, and in general no isomorphism in Cat hot (commentary on VII ms.121).',
        'notes+': CP,
    },
})

# ------------------------------------------------------------------ VIII-X
PT = 'A sufficient modern setting: pointed composition must use the smash product, with unit S^0, and cofibrant-fibrant objects of a pointed simplicial model category supply it; the transfer to the literal pointed path categories is not proved (left open in the answer, C.10). ' + N('C.3, C.4, C.10', 'C.3, C.4 followed; the identification with derived mapping spaces by citation, not opened')
LN = 'For complexes of modules over a commutative ring the truncated derived Hom gives values in D^{<=0}(k) with composition over the derived tensor product and units; the linear version of the literal path categories is left open in the answer (C.9). ' + N('C.8, C.9', 'C.8 followed; citations of Keller and the Stacks project not opened')
QN = 'The agreement of Quillen\'s fundamental groupoid with that of the derived mapping complex is cited from Quillen in the ' + N('C.5', 'unverified citation, not opened') + ' For the literal path category it depends on the open comparison with the localization (B.8).'
LP = 'Pointed infinity-categories with the needed pullbacks and pushouts have the loop and suspension formulas for mapping spaces; representability of all pi_1 functors does not imply them (full pointed subcategory on *, S^0, K(Z,2)). ' + N('C.6, C.7', 'followed; the derivator half of C.6 by citation of Groth 2013, not opened')
R.rows_edit('VIII-X', {
    'IX-037': {
        'repair': 'For every admissible Σ: the inclusions of the one-sided path categories and the padding functors are weak equivalences, and the composition they define is associative and unital in Hot, independently of the block of types (argument by the action of the categories of maps of types; followed in outline). The path categories over all types form a strictly associative and unital enrichment in Cat. The comparisons are not invertible in Cat hot in general. Comparison with the hammock localization: the hammock categories include into the path categories by a map that is injective on homotopy groups and bijective on components, a weak equivalence when Σ consists of isomorphisms or of all arrows; whether it always is one is open. Commentary on VII ms.74, ms.117 and ms.121.',
        'notes': N('C.P3, C.P4, C.P5, C.1, B.4, B.6, B.8', 'C.1, B.4, C.P5 followed in full; C.P3, C.P4, B.6 followed in outline; B.8 open in the answer') + ' This supersedes the entry from CATHOT E.23-E.27 (associativity undecided for general Σ). Open records the source status.',
    },
    'IX-080': {
        'notes+': 'If homotope means weakly equivalent, the first form of (b) is vacuous; the second fails already between finite shapes (a six-object suspension poset and a finite category with two parallel arrows). ' + N('D.1, D.5', 'followed; own check'),
    },
    'IX-081': {
        'notes+': 'The finite pointed category of ms.23 satisfies the tests at every shape; what it lacks is the product x × x (a finite category with finite products is a preorder). Invariance at all small shapes forces 1-types (commentary on V ms.46), so the tests must be read with a bound on the shapes. ' + N('D.2, D.3, D.K4, D.K5', 'followed; D.2 corrects the prompt\'s lead'),
    },
    'IX-088': {
        'notes+': 'Rectifiability on a class of shapes implies the constant-diagram form of (b) on that class; each loop identity (c) implies the corresponding representability (a). ' + N('D.4, D.6', 'followed'),
    },
    'IX-040': {'notes+': QN}, 'IX-041': {'notes+': QN}, 'IX-072': {'notes+': QN},
    'IX-044': {'notes+': PT}, 'IX-049': {'notes+': PT}, 'IX-052': {'notes+': PT},
    'IX-061': {'notes+': LN}, 'IX-065': {'notes+': LN}, 'IX-070': {'notes+': LN},
    'IX-084': {'notes+': LP}, 'IX-087': {'notes+': LP},
})

# ------------------------------------------------------------------ XIII-a
R.blocks_edit('XIII-a', 'new_misc_PATHS.tex')
R.rows_edit('XIII-a', {
    'XIIIa-A046': {
        'notes+': 'One factorization suffices for each half; with an initial object, pushouts and two-out-of-three, Cof_W and W then form a category with cofibrations in which finite direct diagrams are rectified (commentary at p11, last paragraph; proof not reproduced). ' + N('D.8, D.9', 'followed in full; the key step is this corollary'),
    },
})

# ------------------------------------------------------------------ XIIc-a, XIIc-b
R.blocks_edit('XIIc-a', 'new_misc_PATHS.tex')
R.blocks_edit('XIIc-a', 'new_XIIc-a_interval_PATHS.tex')
R.blocks_edit('XIIc-b', 'new_misc_PATHS.tex')
R.rows_edit('XIIc-a', {
    'C033': {
        'repair': 'With Liss and Prop the W-smooth and W-proper functors: the inclusion in Fib_W holds for W∞ and fails for W_0, for every W_n (n>=1), for rational homology and for the E-homology equivalences of every nonzero spectrum E. A W∞-smooth (W∞-proper) functor is W-smooth (W-proper) for every fundamental localizer W. Commentary at p225, last paragraph.',
        'references': 'Cisinski2006, 5.3.1, Corollaire 4.2.19; Maltsiniotis2005Asphericite, Théorème 1.2; commentary at p225',
        'notes': N('E.9 (with STRATA G.3 and POLES C.10)', 'followed; the case W_n, n>=1, is an argument of the reviewer, confirmed by BISITE B.9, B.10') + ' The source proposes the inclusion with a perhaps.',
    },
})

# ------------------------------------------------------------------ XVI
R.blocks_edit('XVI', 'new_misc_PATHS.tex')
R.rows_edit('XVI', {
    'XVI-C105': {
        'notes+': 'A second proof of the negative answer, and the implication from enough intrinsic fibrations to generation by aspherical objects without accessibility: ' + N('D.18, D.23', 'followed in full'),
    },
})

# ------------------------------------------------------------------ II-a, VI-c
R.blocks_edit('II-a', 'new_misc_PATHS.tex')
R.rows_edit('VI-c', {
    'VIc-C022': {
        'notes+': 'The two path functors over the five-element monoid are not the missing bifibration: the eventually constant one is neither a fibration nor an opfibration, the all-type one is not an opfibration. ' + N('E.6, E.11', 'E.6 followed; E.11 open'),
    },
})

R.finish([
    '1 (rows VIIc-A046, V-I066; new block at VII ms.121): done, "The padding functors are weak equivalences and are not invertible modulo natural transformations". C.P5 is proved in the block; C.P3 and C.P4 are stated there as followed in outline.',
    '2 (row VIIb-C026; VII ms.99-110): done by paragraphs at the end of the blocks at ms.112 (A.2, A.3, A.4) and ms.117 (the categories P(tau, sigma), C.P1-C.P3, stated as followed in outline). No separate new block.',
    '3 (rows VIIc-C042, VIIc-C005): done, with a paragraph at the end of the block at ms.157 (E.3 second half, E.4, E.5).',
    '4 (block at VII ms.74): done (A.P1, B.3, B.4, B.6, B.8 stated as open).',
    '5 (row IX-037): done. proof_status stays "open" (the source\'s status, as the convention has it); the answer is in repair. The review asks "status to proved": not followed, because C.P4 was followed in outline only and the column records the source.',
    '6 (rows IX-080, IX-081, IX-088): done, notes only. 7 (rows IX-040, 041, 072, 044, 049, 052, 061, 065, 070, 084, 087): done, notes only; C.5 as an unverified citation.',
    '8 (block at V ms.46): done, one paragraph at the end of the GALOIS block (D.K5).',
    '9 (XIII block at ms.10-11; row XIIIa-A046): done, statement without proof (D.8), with D.9.',
    '10 (row C033 of XIIc-a; block at ms.225): done; the W_0 and W_n cases are set with their arguments, rational homology and W_E stated as not reproduced.',
    '11 (row XVI-C105; block): done; added to the block at ms.124 (the review names the block at ms.87).',
    '12 (XII ms.228-234): done, one paragraph in the block "An interval with room at both ends" of XIIc-a and XIIc-b (E.7, n = 1).',
    '13 (II-a; XIIb-a): done in II-a (A.2, A.5, A.7, A.8 open) at the end of "Total asphericity is not filteredness". XIIb-a NOT changed: its TOTASPH blocks do not treat colimits in Cat.',
    '14 (row VIc-C022): done, notes only.',
    'Not integrated because unverified in the review and bearing on no row: B.9, D.15, D.21. Not set in the commentary: Part D items D.10-D.17, D.19, D.20 (no item of the review\'s list asks for them).',
])
