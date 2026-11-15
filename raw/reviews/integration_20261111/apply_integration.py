"""Integrate the reviewed results of the Pro answers CATHOT and TOTASPH into the companion's checked files
(checks/DER_<id>/): new commentary blocks, replacement of outdated paragraphs, claim rows, bibliography.
Run once from this folder: python -I apply_integration.py   (originals are in before/; the script refuses to run twice)."""
import csv
import io
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).parent
CHK = HERE.parent.parent / 'checks'
log = []
PT = ('Pro answer TOTASPH (AI-produced by GPT-6 Astra, OpenAI, ChatGPT Pro mode), {n}; followed by Claude (Fable 5.2, '
      'Anthropic), pro_reviews_20261110/2_TOTAL_ASPHERICITY/REVIEW_author.md, 11 Nov 2026.')
PC = ('Pro answer CATHOT (AI-produced by GPT-6 Astra, OpenAI, ChatGPT Pro mode), {n}; followed by Claude (Fable 5.2, '
      'Anthropic), pro_reviews_20261110/1_CATHOT/REVIEW.md and REVIEW_author.md, 10-11 Nov 2026.')


def rw(path, fn):
    raw = path.read_bytes()
    crlf = b'\r\n' in raw
    s = raw.decode('utf-8').replace('\r\n', '\n')
    s2 = fn(s)
    assert s2 != s, path
    path.write_bytes((s2.replace('\n', '\r\n') if crlf else s2).encode('utf-8'))


BLOCK = re.compile(r'\\begin\{dcomment\}\{[^}]*\}\{[^}]*\}\{([^}]*)\}.*?\\end\{dcomment\}', re.S)


def blocks_edit(cid, newfile, paragraph_repl):
    path = CHK / f'DER_{cid}' / f'DER_{cid}_blocks.tex'
    new = (HERE / newfile).read_text(encoding='utf-8') if newfile else ''
    parts = re.split(r'^%%(BLOCK|REPLACE) (after|title)="([^"]*)"\n', new, flags=re.M)

    def fn(s):
        assert 'Total asphericity is not filteredness' not in s and 'The reflection does not exist' not in s \
            and 'A total presheaf whose category of elements is not total' not in s, 'already applied'
        for k in range(1, len(parts), 4):
            mode, title, body = parts[k], parts[k + 2], parts[k + 3].strip() + '\n'
            hits = [m for m in BLOCK.finditer(s) if m.group(1).strip() == title]
            assert len(hits) == 1, (cid, title, len(hits))
            m = hits[0]
            for nb in BLOCK.finditer(body):
                log.append(f'{cid}: {"replaced block" if mode == "REPLACE" else "new block"} "{nb.group(1)}"'
                           + (f' (was "{title}")' if mode == 'REPLACE' else f' after "{title}"'))
            if mode == 'BLOCK':
                s = s[:m.end()] + '\n\n' + body.rstrip('\n') + s[m.end():]
            else:
                s = s[:m.start()] + body.rstrip('\n') + s[m.end():]
        for old, newp in paragraph_repl:
            assert s.count(old) == 1, (cid, s.count(old), old[:80])
            s = s.replace(old, newp)
            log.append(f'{cid}: paragraph updated: "{old[:70]}..."')
        return s
    rw(path, fn)


def rows_edit(cid, edits):
    path = CHK / f'DER_{cid}' / f'DER_{cid}_claims.csv'
    raw = path.read_bytes()
    crlf = b'\r\n' in raw
    text = raw.decode('utf-8')
    rows = list(csv.reader(io.StringIO(text, newline='')))
    head = rows[0]
    ix = {h: i for i, h in enumerate(head)}
    seen = set()
    for r in rows[1:]:
        if r and r[0] in edits:
            seen.add(r[0])
            for col, val in edits[r[0]].items():
                if col.endswith('+'):
                    c = col[:-1]
                    r[ix[c]] = (r[ix[c]].rstrip() + ' ' + val).strip()
                else:
                    r[ix[col]] = val
            log.append(f'{cid}: row {r[0]} updated ({", ".join(edits[r[0]])}); proof_status now "{r[ix["proof_status"]]}"')
    assert seen == set(edits), set(edits) - seen
    out = io.StringIO(newline='')
    csv.writer(out, lineterminator='\r\n' if crlf else '\n').writerows(rows)
    path.write_bytes(out.getvalue().encode('utf-8'))


def bib_add(cid, entries):
    path = CHK / f'DER_{cid}' / f'DER_{cid}_references.bib'

    def fn(s):
        for key, entry in entries:
            assert key + ',' not in s, (cid, key)
            s = s.rstrip('\n') + '\n\n' + entry.strip() + '\n'
            log.append(f'{cid}: bibliography entry {key} added')
        return s
    rw(path, fn)


AKR = ('AdamekKoubekReiterman1981', r"""
@article{AdamekKoubekReiterman1981,
  author = {Ad{\'a}mek, Ji{\v r}{\'\i} and Koubek, V{\'a}clav and Reiterman, Jan},
  title = {Embeddings into categories with fixed points in representations},
  journal = {Czechoslovak Mathematical Journal},
  volume = {31},
  number = {3},
  pages = {368--389},
  year = {1981},
  doi = {10.21136/CMJ.1981.101753},
  url = {https://dml.cz/handle/10338.dmlcz/101753},
  note = {verified: scan at dml.cz, statements of A.4 and A.5 (p. 370), Construction C.1 (p. 384) and Theorem C.2 (p. 385); the proofs were not checked}
}""")
C04 = ('Cisinski2004Minimal', r"""
@article{Cisinski2004Minimal,
  author = {Cisinski, Denis-Charles},
  title = {Le localisateur fondamental minimal},
  journal = {Cahiers de Topologie et G{\'e}om{\'e}trie Diff{\'e}rentielle Cat{\'e}goriques},
  volume = {45},
  number = {2},
  pages = {109--140},
  year = {2004},
  url = {https://www.numdam.org/item/CTGDC_2004__45_2_109_0/},
  note = {verified: D{\'e}finition 1.1.3 and Th{\'e}or{\`e}me 2.2.11 in the published PDF}
}""")
C06 = ('Cisinski2006', r"""
@book{Cisinski2006,
  author = {Cisinski, Denis-Charles},
  title = {Les pr{\'e}faisceaux comme mod{\`e}les des types d'homotopie},
  series = {Ast{\'e}risque},
  volume = {308},
  publisher = {Soci{\'e}t{\'e} Math{\'e}matique de France},
  year = {2006},
  url = {https://cisinski.app.uni-regensburg.de/smf_ast_308.pdf},
  note = {verified: 9.2.1, Corollaire 9.2.15 and Proposition 9.2.17 with its proof (printed pp. 369--370) in the published PDF}
}""")

# ------------------------------------------------------------------ II-a
blocks_edit('II-a', 'new_II-a.tex', [
    ("The difficult direction is whether this test forces the equalization of parallel arrows. The counterexample inserted on pages~36bis--36ter withdraws the attempted negative answer; it does not prove the converse.",
     "The difficult direction is whether this test forces the equalization of parallel arrows. The counterexample inserted on pages~36bis--36ter withdraws the attempted negative answer; it does not prove the converse. The converse holds for monoids and for categories with finitely many objects and fails in general; both are proved in the commentary ``Total asphericity is not filteredness'' below."),
    ("Our literature check did not locate a resolution of the full implication $T(A)\\Rightarrow A\\text{ filtered}$ under the exact quantifier used here. This is a bounded report on the sources checked, not a claim that the question is known to be open throughout the literature.",
     "The next commentary settles it: the implication $T(A)\\Rightarrow A\\text{ filtered}$ holds when some object receives an arrow from every object, and fails for the category of finite ordinals and increasing injections."),
])
rows_edit('II-a', {
    'II-C-003': {
        'gap_or_error': 'The conjecture is false in general. The attempted negative answer of the source is withdrawn by Counterexample2.20; the counterexample below is a different one.',
        'repair': 'False in general: the category of the ordered sets [n] and strictly increasing maps satisfies T and is not filtered. True when some object receives an arrow from every object, in particular for all monoids and all categories with finitely many objects; true for preorders. Criterion: T(A) iff A is nonempty and connected and every connected component of the category of elements of every functor A\\to Set is weakly contractible (equivalently, has the integral homology of a point). Complete proofs in the commentary Total asphericity is not filteredness. Undecided: whether T(A) implies exactness of colimits of abelian groups over A (the converse holds for connected nonempty A).',
        'references': 'AdamekKoubekReiterman1981, A.5 (exact colimits over the injective ordinals, attributed to Isbell and Mitchell); Maltsiniotis2020, §§1.7,2.4; AdamekRosickyVitale2010; NunesSousa2022',
        'notes': PT.format(n='C.3-C.13, D.4, with own enumeration (affine cones for n<=3; all monoids of order <=4)') + ' The exactness of colimits over the injective ordinals is in the literature; its use to answer this question was not found there.',
    },
    'II-C-010': {
        'repair': 'Common successors: proved (commentary A necessary directedness condition). Siftedness: false; the category of the ordered sets [n] and strictly increasing maps satisfies T and its diagonal is not cofinal (three components of pairs of points). Commentary Total asphericity is not filteredness.',
        'notes': PT.format(n='C.10, C.11, C.14'),
    },
})
bib_add('II-a', [AKR])

# ------------------------------------------------------------------ XIIb-a
blocks_edit('XIIb-a', 'new_XIIb-a.tex', [
    ("This counterexample defeats the proposed pushout method; it does not refute the general converse of Proposition~8. We could not find that converse established or disproved in the primary sources checked, including the comprehensive-factorization treatments cited above. It is consequently recorded as unresolved in the audit, rather than assigning it an unsupported present-day status. The subterminal case is proved, and the obstruction to the broader argument is explicit.",
     "This counterexample defeats the proposed pushout method; it does not by itself refute the general converse of Proposition~8. That converse is false: a presheaf with three elements on a monoid with two elements is given in the commentary at ms.~97. The subterminal case is proved, and the obstruction to the broader argument is explicit."),
    ("The question about $\\underline{\\mathrm{Ch}}(Y;y_0,-)$ when $BY$ is contractible is a different question. Proposition~10 gives no implication in that case. We have not located a result settling that precise question for Grothendieck's particular path construction; a replacement by some equivalent contractible category would not answer it.",
     "The question about $\\underline{\\mathrm{Ch}}(Y;y_0,-)$ when $BY$ is contractible is a different question. Proposition~10 gives no implication in that case, and a replacement of the path category by some equivalent contractible category would not answer it. The next commentary answers it, negatively, with this same fork."),
    ("It supplies no composition theorem for arbitrary strictly or totally $W$-aspherical functors: in a composite one pulls back a weight of the second functor, whereas the lemma controls left Kan extension. The distinction identifies the mathematical content of the doubt expressed on ms.~113--114.",
     "It supplies no composition theorem for arbitrary strictly or totally $W$-aspherical functors: in a composite one pulls back a weight of the second functor, whereas the lemma controls left Kan extension. The distinction identifies the mathematical content of the doubt expressed on ms.~113--114. Composition is treated in the commentary at ms.~114: both classes of functors are stable under it, by a different argument."),
])
P48 = {
    'repair': 'For every fundamental localizer W for which a category of the homotopy type of S^3 is not W-aspherical (W_infty, W_R with R nonzero, m-equivalences with m>=3) the inclusion alpha deduced from {0}->[1] is not a W-cofibration, and a class of sieve W-cofibrations with the stability asked for contains only isomorphisms. When a category of the type of S^2 is not W-aspherical the same holds for trivial W-cofibrations. For W_0 all sieves form such a class; likewise for every fundamental localizer containing W_1 (proof not set in the commentary). Commentary ms.114, The endpoint product is not a cofibration.',
    'references': 'Cisinski2006, Proposition 9.2.17; BataninBerger2017, Lemma 1.10; Thomason1980; Cisinski1999Dwyer',
    'notes': PT.format(n='F.23-F.31, with own computation of the pushouts for n=2,3') + ' The exclusion of plain W-cofibrations for the 2-equivalences uses TOTASPH F.3 (for every fundamental localizer a W-cofibration in W is a trivial W-cofibration), followed in the review and not set in the commentary. Source status: a desideratum.',
}
rows_edit('XIIb-a', {
    'XIIb-a-B035': {
        'repair': 'No for W_infty, for the homology localizers W_R (R nonzero) and for the n-equivalences with n>=2: on the monoid {1,e}, e^2=e, the presheaf with three elements on which e is constant is totally W-aspherical for every fundamental localizer and its category of elements has a final image of the homotopy type of S^2. Yes for W_0 and W_1. Commentary ms.97, A total presheaf whose category of elements is not total. The source proves the subterminal case. Yes also for every fundamental localizer containing W_1 (proof not set in the commentary).',
        'references': 'Cisinski2004Minimal, Théorème 2.2.11',
        'notes': PT.format(n='E.1-E.5, D.19-D.20, with own enumeration') + ' The two definitions quantify over different sets of outgoing functors.',
    },
    'XIIba-C005': {
        'gap_or_error': 'The source doubts the implication; the doubt is justified.',
        'repair': 'No. For Y the outgoing fork a<-z->b and y_0=z the path category is W_infty-aspherical, its endpoint functor is final, and the fork has a final image of the homotopy type of S^2. Commentary ms.103, The path category over a contractible base need not be total.',
        'references': 'commentary p100 and p103',
        'notes': PT.format(n='G.2-G.6') + ' Source-open question.',
    },
    'XIIba-C035': {
        'repair': 'No, in both readings: the sieve {u} in the category with arrows alpha,beta:u->t, gamma:t->s, gamma alpha=gamma beta, is a trivial W-cofibration for every fundamental localizer and is not W-dwyerienne for W_infty, W_R, W_n; a fortiori it is not a Dwyer immersion. Commentary ms.111, The open questions of this page.',
        'references': 'commentary p111',
        'notes': PT.format(n='F.18, with own check of five pushouts') + ' Source-open question.',
    },
    'XIIba-C037': {
        'proof_status': 'false',
        'gap_or_error': 'False for W-cofibrations, also under W(7): the sieve {u} in the category with exactly two nonidentity arrows u->t is a W_infty- and W_R-cofibration with complement e and is not dwyerienne. The corollary of Proposition 7 concerns membership of one inclusion in W, not the cofibration property.',
        'repair': 'True for trivial W_R-cofibrations with one-point complement (commentary ms.111). For trivial W_infty-cofibrations the statement is equivalent to an undecided one: is a presheaf all of whose direct images have integrally acyclic categories of elements totally W_infty-aspherical?',
        'references': 'commentary p111; Proposition 7 corollary p85',
        'notes': PT.format(n='F.19, F.20, F.26, F.27'),
    },
    'XIIba-C038': {
        'proof_status': 'false',
        'gap_or_error': 'False: for the same two-arrow example every change of complement T_1->T gives a W_infty- and W_R-cofibration, and none with T_1 nonempty is dwyerienne. Sufficiency (dwyerienne implies the cofibration property of all i_1) is not affected.',
        'repair': 'Commentary ms.111, The open questions of this page.',
        'references': 'commentary p111; Proposition 7(b); Theorem 3',
        'notes': PT.format(n='F.19') + ' The proof in the commentary (joins of nerves) is by the reviewer; the answer argues through discretely flat functors (HackneyOzornovaRiehlRovelli2024).',
    },
    'XIIba-C045': {
        'repair': 'Totally W-dwyerienne sieves: stable under composition for W_infty and for W_R; not for W_0 and W_1 (targets with six objects). W-dwyerienne sieves: stable for W_R (one step not set in the commentary); not for W_0, W_1; undecided for W_infty, where the question is equivalent to the one recorded at XIIba-C037. Commentary ms.114, Composition of aspherical functors and of dwyerienne immersions.',
        'references': 'commentary p114',
        'notes': PT.format(n='F.5, F.6, F.9-F.12, F.26, F.27, D.21, with own enumeration of the two counterexamples') + ' Source-open question.',
    },
    'XIIba-C047': {
        'repair': 'Yes, both classes, for every fundamental localizer: restriction along a strictly W-aspherical functor preserves totally W-aspherical presheaves. Commentary ms.114, Composition of aspherical functors and of dwyerienne immersions.',
        'references': 'commentary p114',
        'notes': PT.format(n='F.7, F.8') + ' Followed once; a second reading of F.7 is advisable before quoting it elsewhere.',
    },
    'XIIba-C048': dict(P48),
    'XIIbb-A001': dict(P48),
})
bib_add('XIIb-a', [C04, C06])

# ------------------------------------------------------------------ III-V
blocks_edit('III-V', 'new_III-V.tex', [
    ("The claim on manuscript p.~47 that a corresponding union map must be a weak equivalence therefore needs an argument respecting the particular filtration hypotheses. We do not certify that inference for the full setting proposed here.",
     "The claim on manuscript p.~47 that a corresponding union map must be a weak equivalence is false, even for full inclusions of finite fibrant stages with fibrant union; the example is in the commentary at ms.~49."),
    ("We have not shown that the target stages or their union are Thomason fibrant; this construction therefore does not answer the stronger question with that additional hypothesis.",
     "We have not shown that the target stages or their union are Thomason fibrant; this construction therefore does not answer the stronger question with that additional hypothesis. The next commentary does."),
])
rows_edit('III-V', {
    'V-I026': {
        'proof_status': 'false',
        'gap_or_error': 'False: the localization Cat hot -> Hot has no right adjoint, fully faithful or not. The edition explicitly requests a proof; none exists.',
        'repair': 'Commentary ms.37, The reflection does not exist: no small K represents X -> [BX,K(Z/2,2)], by testing on the finitary alternating group of a set larger than Mor K. What exists instead: the reflection of Cat hot onto groupoids by the fundamental groupoid (it represents exactly the 1-types); Thomason fibrant replacement with the model-categorical mapping formula, which replaces the source cofibrantly.',
        'notes': PC.format(n='B.1-B.4, B.11, C.2-C.4') + ' Lead by Claude; the commentary gives the Clifford-algebra form of the non-split extension.',
    },
    'V-I054': {
        'repair+': 'The union of stages that are each isomorphic in Cat hot to a groupoid need not be so (commentary ms.49, The same ind-morphism, two different maps of the unions): fibrancy passes to the union, the envelope property does not.',
        'notes': PC.format(n='E.3, E.4') + ' Proof given in commentary; fullness is not needed for the fibrancy assertion.',
    },
    'V-I059': {
        'proof_status': 'false',
        'gap_or_error': 'False, even for full inclusions of finite Thomason-fibrant stages, each isomorphic in Cat hot to a group, with fibrant union: a shift functor induces the identity of the ind-object and is not a weak equivalence of the union.',
        'repair': 'Commentary ms.49, The same ind-morphism, two different maps of the unions. A coherent levelwise weak equivalence after cofinal reindexing remains sufficient. The assertion is true when both unions are isomorphic in Cat hot to groupoids (not set in the commentary).',
        'notes': PC.format(n='E.4, E.18'),
    },
    'V-I060': {
        'proof_status': 'false',
        'gap_or_error': 'False for Thomason-fibrant categories: the functor r from the union T of the commentary at ms.49 to the group BG is a weak equivalence between fibrant categories and is not invertible in Cat hot. True for categories isomorphic in Cat hot to groupoids.',
        'repair': 'Commentary ms.49, part (c). Retain only the isomorphism in Hot, or assume both sides isomorphic in Cat hot to groupoids.',
        'notes': PC.format(n='C.3, E.4') + ' Part (c) of the commentary is an argument of the reviewer on the example of E.4 (REVIEW.md, Consequence 1, uses a fibrant poset of the type of the circle instead); not checked by a second reader. The text itself adds sauf erreur.',
    },
    'V-I063': {
        'gap_or_error': 'Stagewise homotopies need not be compatible or uniformly bounded.',
        'repair': 'No, also when all stages and both unions are Thomason fibrant: commentary ms.49, The same ind-morphism, two different maps of the unions (homotopies of length three at every stage, incompatible). The fence construction shows the unbounded-length mechanism without fibrancy. Uniformly compatible homotopies suffice. Yes when the unions are isomorphic in Cat hot to groupoids (not set in the commentary).',
        'notes': PC.format(n='E.4, E.18, C.5'),
    },
})

# ------------------------------------------------------------------ VII-c, VIII-X (rows only)
rows_edit('VII-c', {
    'VIIc-C004': {
        'repair+': 'Independently: T^2=1 holds in Hot on the total category and on every fibre, for every admissible Sigma in the canonical model, because T^2 fixes the constant paths and the constant-path section is invertible in the homotopy category of spaces over BX x BX (not set in the commentary).',
        'notes': PC.format(n='E.22, E.25') + ' Source question, not a claim that this remains open today.',
    },
    'VIIc-C005': {
        'repair+': 'A second complete proof, with the degenerate case n=m excluded and the passage from the two lifting properties to Quillen B written out, is in the Pro answer named in the notes.',
        'notes': PC.format(n='E.20, E.21'),
    },
})
rows_edit('VIII-X', {
    'IX-037': {
        'repair': 'For Sigma = all arrows: the inclusions of the one-sided path categories are weak equivalences and the left-right composition is path concatenation, associative and unital in Hot. For a general admissible Sigma: the inclusions are weak equivalences and the operation is unital; associativity is undecided. None of this is set in the commentary yet; the comparison with the hammock localization is still not available.',
        'notes': PC.format(n='E.23, E.24 (all arrows), E.25 (general Sigma), E.27 (undecided)') + ' E.24 was followed once by the reviewer, who asks for a second reading before it is called established. Open records the source status.',
    },
})

(HERE / 'INTEGRATION_LOG.md').write_text(
    '# Integration of CATHOT and TOTASPH into the companion (11 November 2026)\n\n'
    'Applied by `apply_integration.py` to `checks\\DER_<id>\\`. Originals: `before\\`.\n\n'
    + '\n'.join('- ' + l for l in log) + '\n', encoding='utf-8')
print('\n'.join(log))
