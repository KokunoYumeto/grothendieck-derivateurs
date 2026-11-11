"""Build the statement ledger for Part F from its authored claim environments."""
from pathlib import Path
import re, json

root = Path(__file__).resolve().parents[1]
source = (root / 'sections/F.tex').read_text()
deps = {
 'F.1': [],
 'F.2': ['F.1'],
 'F.3': ['F.2'],
 'F.4': ['F.2','F.3'],
 'F.5': ['F.1','F.4'],
 'F.6': ['F.1'],
 'F.7': ['F.6'],
 'F.8': ['F.6'],
 'F.9': ['F.6','F.8','B.5','B.7','B.10'],
 'F.10':['F.6','F.9','B.6'],
 'F.11':['B.5','F.7'],
 'F.12':['F.11','B.1'],
 'F.13':['F.1','F.2'],
 'F.14':['F.4','F.5','F.7','F.13'],
}
pages = {
 'F.1':'Lead 6; XII ms. 266-267',
 'F.2':'Lead 6; XVI section 3, Loc (6 a,b,c)',
 'F.3':'Lead 6 accessibility hypothesis',
 'F.4':'Part F Galois connection',
 'F.5':'Part F image and fibers',
 'F.6':'Lead 6, zero localizing subcategory; Part H interval',
 'F.7':'Lead 6 bijection refuted',
 'F.8':'Parts C,E,F: homology and nullification; XVI Loc (7 F)',
 'F.9':'Part F plus construction; Part H interval',
 'F.10':'Part F nullification at acyclic spaces',
 'F.11':'XVI ms. 1, Loc (1 bis); XIIba-A-053',
 'F.12':'XII ms. 76; XIIba-A-053',
 'F.13':'Part F generalized homology and arbitrary stable kernels',
 'F.14':'Part F residual image converse and Bousfield representability',
}
notes = {
 'F.1':'Reduced suspension spectrum at the specified cone point; includes empty and disconnected cases.',
 'F.2':'No accessibility needed for order-theoretic class; localizing kernel assumed retract closed.',
 'F.3':'Accessibility restricted to set-generated stable kernels; no Vopenka assumption.',
 'F.4':'Order preserving adjunction; RT is closure, TR is interior.',
 'F.5':'Exact formal image and fibers; does not assert every reversible localizer is RT-fixed.',
 'F.6':'Stable integral Hurewicz detects zero connective spectra.',
 'F.7':'0 versus ker(HZ smash -), or 0 versus loc(K(n)), have identical space equivalences.',
 'F.8':'Code and complete output verify BS3 and the non-surjectivity certificate; also action orbits for Part C.',
 'F.9':'Universal plus and integral homology have equal aspherical objects but different map classes.',
 'F.10':'All connected integrally acyclic nullification spaces, including contractible ones.',
 'F.11':'Arrow-category retracts; automatic for the modern relative-Theorem-A definition by Cisinski 4.2.4.',
 'F.12':'Forward gluing plus automatic retract closure suffice; reverse excision unused.',
 'F.13':'All integer degrees, unpointed E-homology defined by adjoining a disjoint basepoint X_+; E need not be a ring.',
 'F.14':'Open means unresolved in this audit. Berger-Ratkovic stable embedding requires fully faithful suspension. The loc(HFp) question is exactly equality with the a(HFp)-acyclics; the 2026 Putzstuck retract-conjecture counterexample does not settle it.',
}
rows=[]
for m in re.finditer(r'\\begin\{claim\}\{(F\.\d+)\}\{([^}]+)\}\{([^\n]+)\}\n(.*?)\\end\{claim\}', source, re.S):
    ident,status,title,body=m.groups()
    rows.append({'id':ident,'statement':title+' '+re.sub(r'\s+',' ',body).strip(),
                 'status':status,'where_proved':f'POLES_paper.tex, Part F, {ident}',
                 'depends_on':'; '.join(deps[ident]),
                 'manuscript_rows_or_pages_settled':pages[ident],
                 'notes':notes[ident]})
assert len(rows)==14, len(rows)
assert [r['id'] for r in rows]==[f'F.{i}' for i in range(1,15)]
(root / 'research/F_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print('Wrote',len(rows),'rows:', {s:sum(r['status']==s for r in rows) for s in ('Proved','Refuted','Known','Open')})
