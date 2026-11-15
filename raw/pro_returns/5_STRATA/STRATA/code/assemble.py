"""Assemble the result register and bibliography; audit cross-file consistency.

Run from the extracted STRATA directory: python3 code/assemble.py.
If a LuaLaTeX .aux file is present, PDF page numbers are included in the CSV.
The audit fragments are authored inputs, not external manuscript authority.
"""
from pathlib import Path
import csv
import re
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
sections = sorted((ROOT / 'sections').glob('*.tex'))
claims = {}
for file in sections:
    text = file.read_text()
    for m in re.finditer(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}\{(.*?)\}\s*(.*?)\\end\{statement\}', text, re.S):
        ident, status, title, body = m.groups()
        assert ident not in claims, ident
        claims[ident] = dict(id=ident, status=status, title=' '.join(title.split()),
                            body=' '.join(body.split()), source=str(file.relative_to(ROOT)))
assert all(c['status'] in {'Proved','Known','Refuted','Open'} for c in claims.values())

# id | short statement | dependencies | manuscript scope | audit note
root_data = r'''
0.1|Presheaf variance uses downset opens and minimum-vertex stratification; geometric exits have the opposite variance.|Definitions|I ms.1–9; XII ms.59–63|The abstract convention is universal; geometric qualifications are retained.
A.1|For every small poset, diagrams of spaces are Alexandrov hypersheaves; ordinary sheaves agree for finite principal downsets.|BGH Proposition3.12.11 and Example3.12.15|Lead1; Alexandrov dictionary|Set-valued comparison has no finiteness restriction.
A.2|Ordinary Alexandrov sheaves equal diagrams for every small or merely interval-locally-finite poset.|Aoki ExampleA.13|Lead1 unrestricted clause|Refuted by the opposite of the countable ordinal sum of two-point antichains; compactness distinguishes the categories.
A.3|The Alexandrov hypersheaf equivalence holds for every presentable coefficient infinity-category.|A.1; mapping-space Yoneda|PartA presentable coefficients|Ordinary sheaves agree when every principal downset is finite.
A.4|Finite minimum-vertex realizations have contractible strata, opposite-poset exits, and the stated ordinary constructible-sheaf category.|LurieHA; Kerodon6.3.6.2; HPTcoarsening|Lead1 finite geometric clause|Explicit cone-product charts justify ordinary raw exits; locallyfinite order complexes follow locally.
A.5|Geometric coefficient exodromy holds for compactly assembled coefficients and stable presentable coefficients in the finite case.|A.4; HPT4.1.15|PartA coefficient range|For every other presentable coefficient category the canonical diagram-image functor is fully faithful.
A.6|Unrestricted presentable coefficients and unrestricted infinite ordinary geometric sheaves satisfy the same essential-surjectivity assertion.|A.5; A.12|Lead1 remaining geometric clauses|Open in this audit; raw exit computation A.12 does not prove ordinary sheaf exodromy.
A.7|Restriction has both intrinsic Kan adjoints with the correct opposite-comma formulas.|Pointwise Kan extension|I ms.47–56; PartA|Empty fibres and nonsurjective components use empty colimits and limits.
A.8|Strict-fibre formulas hold exactly under the indicated homotopy-final/initial comma comparisons.|A.7; QuillenTheoremA|I ms.49–56|Incoming lift tests govern left Kan extension; outgoing tests govern right Kan extension.
A.9|Locally constant coefficients factor through BS and the inclusion has both adjoints, including Grothendieck's reflection.|Cisinski2009Theorem3.13; groupoidification|VI ms.32–69; GALOISA.6,A.8,C.1|A bare derivator and an enhanced coefficient category are distinguished.
A.10|On the interval reflection and coreflection select opposite endpoint values; strict colimit cannot replace homotopy colimit without a hypothesis.|A.9|VI ms.65–69; TOTASPH reminder|Triangle-boundary face poset gives strict colimit point and homotopy colimit circle.
A.11|A bare derivator gives a cellular coefficient theory; actual topological sheaves require a defined enhancement and comparison.|Der1–4; Cisinski3.13|Lead4 and PartA|No strongness assumed; no reconstruction of mapping spaces from bare axioms.
A.12|For every small poset, the raw minimum-vertex exit infinity-category of its weak CW realization is the opposite poset.|A.4; finite-subcomplex property|Lead1 unrestricted raw-exit clause|Filtered union proves raw exit calculation only; geometric ordinary sheaves remain qualified.
B.1|An ordinary category is conservative over a poset exactly when it is EI; strata have the types of automorphism-group classifying spaces.|Elementary inverse calculation; BGHlayeredcategories|Lead2 EI clause|General layered infinity-categories can have nondiscrete mapping spaces.
B.2|Every EI category has the exact intrinsic constructible-coefficient and stratified-presheaf-topos dictionary.|B.1; openclosed restriction|Lead2 abstract dictionary|Geometric realizations require exodromy; the bimodule and composition data are retained.
B.3|Finite acyclic categories have literal minimum-object geometric realizations with constructible presheaf coefficients.|A.4; Kerodonlocalization; explicitcone charts|Lead2 finite acyclic clause|Parallel arrows are retained as distinct cells.
B.4|The three-object category R2 realizes RP2 with its projective-flag stratification and the claimed constructible category.|B.3; octahedral quotient|CATHOTG.11 follow-up|Nine-arrow category, integral H1=Z/2, and free C2 quotient all checked.
B.5|Every unrestricted EI minimum-isomorphism-class realization has the full ordinary geometric sheaf dictionary.|B.1–B.3|Lead2 unrestricted geometric clause|Open in this audit; mixed two-object four-arrow C2-to-terminal category and the infinite layered poset are explicit tests.
B.6|Enhanced presheaf categories recover idempotent completion; a layered target forces the source to be EI.|Atomic objects and Yoneda density|PartB Morita invariant|The proof does not pass to a bare ordinary homotopy category.
B.7|Every small category can be an exodromic usual stratified model with equivalent enhanced coefficients.|B.6|Lead2 noninvertible endomorphisms|Refuted by the one-object two-arrow absorbing-idempotent monoid, although its classifying space contracts.
B.8|Every small category has a marked-poset localization presentation; unmarked subdivision alone does not recover all coefficients.|KerodonTheorem6.3.6.1|Lead2 subdivision clause|Markings impose equivalence conditions on coefficient arrows.
B.9|Morita equivalence implies classifying-space equivalence, but not conversely; locally constant coefficients see the latter.|B.6; A.9; QuillenA|PartB two invariants|Point and interval have equivalent classifying spaces but two versus three subterminal presheaves.
B.10|Coarse reconstruction requires the specified constant functor or enhanced evaluation; the latter recovers the loop algebra.|Yoneda; BarrBeck|GALOISF.1–F.3|R is commutative; finite-set systems carry only finite-action information.
B.11|The specified restriction detects W(r+1) for r-types, W-infinity for spaces/integral/spectral coefficients, and pi1-rational equivalences for rational coefficients.|B.10; RWZTheorem3; free-object tests|GALOISC.4,C.7,C.9,C.10,C.13,C.15|Cotensors recover mapping spaces for specified restriction on homotopy categories; all components and zero coefficients treated.
B.12|Bare ordinary coefficient categories, without the indicated extra data, reconstruct the same fine and coarse invariants.|B.6; B.10; B.11|GALOISF.8 retained|Open in this audit; no counterexample or mathematical-novelty claim.
G.1|The two fine variances correspond to directed coefficient theories and are exchanged by base opposition, without supplying Verdier duality.|A.9; B.1; B.7|VI fine localizations; PartG|No dualizing object or finiteness condition is supplied by index opposition.
G.2|Total W-infinity asphericity is exactly the canonical homotopy-colimit to strict-colimit equivalence for every simplicial diagram on a connected base.|C.3; comprehensive factorization; cyclic covers|XII ms.88–89; TOTASPHB.11|A contractible fork fails the test; a four-object element circle verifies the obstruction.
G.3|Wn has the locally constant (n-1)-type sheaf meaning for n>=1, but fails universal ordinary homotopy-pullback stability.|B.11|GALOISC.4; POLESE.5|Loop Eilenberg–MacLane example; finite C2 translation-groupoid example at n=0.
G.4|Intrinsic Wn fibrations are precisely the functors whose strict pullback comparisons are pullbacks of n-types.|Cisinski9.2.1,9.2.15,6.2.3|POLESC.8–C.9; XVI truncation questions|Includes an independent complete pi0 component-and-lift proof.
G.5|Universal ordinary homotopy-pullback stability of a fundamental localizer forces W-infinity or the total class.|Cisinskiminimality; E.2; iteratedloop argument|POLESE.4–E.5; XVI Loc7|No accessibility needed; this is distinct from pullbacks in the localized homotopy theory.
G.6|Product-stable accessible localizations of spaces realize the corresponding constant-coefficient classes without implying a left-exact sheaf localization.|Cisinski1.4.3,4.2.15; Yoneda|GALOISE.7; PartG|The coefficient interpretation survives even when ordinary geometric base-change stability fails.
G.7|Conically smooth atlases, dimension, tubular data and dualizing objects are additional geometric structures not supplied by the categorical dictionary.|D.5–D.8; one-stratum contractible manifolds|PartG|This is a precise absence of automatic reconstruction, not a claim about all possible enhancements.
'''
rows = {}
for line in root_data.strip().splitlines():
    ident, statement, deps, scope, notes = line.split('|')
    c = claims[ident]
    rows[ident] = dict(id=ident, statement=statement, status=c['status'],
                      where_proved=f"{c['source']}, {ident}", depends_on=deps,
                      manuscript_rows_or_pages_settled=scope, notes=notes)
for part in ('CD','E','F'):
    with (ROOT/'audit'/f'{part}_results.csv').open(newline='') as f:
        for row in csv.DictReader(f):
            ident = row['id']
            assert ident in claims and ident not in rows, ident
            assert row['status'] == claims[ident]['status'], (ident,row['status'],claims[ident]['status'])
            rows[ident] = row
assert set(rows) == set(claims), (set(claims)-set(rows),set(rows)-set(claims))
aux = ROOT/'STRATA_paper.aux'
pages = {}
if aux.exists():
    for ident, page in re.findall(r'\\newlabel\{st:([^}]+)\}\{\{[^}]*\}\{([^}]+)\}',aux.read_text()):
        pages[ident] = page
    for ident, row in rows.items():
        if ident in pages:
            row['where_proved'] += f"; STRATA_paper.pdf p. {pages[ident]}"
def order(ident):
    a,b = ident.split('.')
    return (a,int(b))
fields = ['id','statement','status','where_proved','depends_on','manuscript_rows_or_pages_settled','notes']
with (ROOT/'STRATA_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows[i] for i in sorted(rows,key=order))

# Use one HTT entry for the two independently audited citations.
for file in sections:
    original=file.read_text()
    normalized=original.replace('{CDLurie2009}','{FLurieHTT2009}')
    normalized=re.sub(r'\\section\{[A-G]\. ',r'\\section{',normalized)
    if normalized != original:
        file.write_text(normalized)
bib_entries={}
for fragment in ('root','CD','E','F'):
    text=(ROOT/'audit'/f'{fragment}_references.bib').read_text()
    for block in re.split(r'(?=^@\w+\{)',text,flags=re.M):
        if not block.strip(): continue
        key=re.match(r'@\w+\{([^,]+),',block).group(1)
        if key=='CDLurie2009': continue
        assert key not in bib_entries, key
        assert re.search(r'(?<!un)verified:',block) or 'unverified:' in block, key
        bib_entries[key]=block.strip()
(ROOT/'STRATA_references.bib').write_text('\n\n'.join(bib_entries.values())+'\n')
all_tex='\n'.join(f.read_text() for f in sections)
cited=set()
for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',all_tex):
    cited.update(k.strip() for k in m.group(1).split(','))
assert not(cited-set(bib_entries)), sorted(cited-set(bib_entries))
summary={
    'statements':len(claims), 'statuses':dict(Counter(c['status'] for c in claims.values())),
    'sections':dict(Counter(c['id'].split('.')[0] for c in claims.values())),
    'numbered_open_statements':[i for i in sorted(rows,key=order) if rows[i]['status']=='Open'],
    'bibliography_entries':len(bib_entries), 'cited_entries':len(cited),
    'unverified_entries':[k for k,v in bib_entries.items() if 'unverified:' in v],
    'missing_citation_keys':sorted(cited-set(bib_entries)),
    'pdf_statement_pages_found':len(pages),
}
print(json.dumps(summary,indent=2))
