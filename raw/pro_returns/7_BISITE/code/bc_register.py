"""Rebuild the B/C result registers and check local claim and citation integrity."""
from pathlib import Path
import re,csv,json
ROOT=Path(__file__).resolve().parents[1]
DATA={
'B.1':('B.3; Cisinski 2006, 3.3.8','VI ms.81--84; XII ms.222','Presheaf test is s\\X; covariant test is X/s.'),
'B.2':('Cisinski 2019, 4.4.14 and 4.4.29--30; Lurie 2009, 2.2.1.2','Lead 1; VI ms.81--84','All total objects allowed; literal slices require a quasicategorical base.'),
'B.3':('B.2; Cisinski 2019, 7.3.8--10','Lead 1; VI ms.81--84','Enhanced localization equivalence; no unsupported Quillen claim for the raw nerve.'),
'B.4':('B.2; Lurie 2009, 2.1.4.9','Lead 1','Explicit inner-horn base; finite simplex intersections checked.'),
'B.5':('Cisinski 2019, 4.4.36; Cisinski errata 2026; Lurie 2009, 4.1.2.8--9','I ms.54; XII ms.224--225','Grothendieck-proper equals Lurie-smooth; ordinary nerve criterion unaffected by erratum.'),
'B.6':('B.1; Maltsiniotis 2005, Theorem 1.2(c)','XII ms.222; II ms.66 and 88--89','Maximal class equality settled with covariant manuscript variance, without accessibility.'),
'B.7':('B.5; Cisinski 2019, 4.6.2 and 4.6.5','XII ms.225--226; STRATA D.5--D.6','Diamond and V finite separators; strict pullback class distinguished from bifibrations.'),
'B.8':('B.7','VII ms.161--169; PATHS E.9','Fully specified integer-fence category; all lift contractions proved.'),
'B.9':('B.7; Cisinski 2006, 4.2.15, 4.2.19, 5.3.13--14','XII ms.225--226; POLES E.5; STRATA G.5','Only minimal and total localizers; no accessibility.'),
'B.10':('B.8; B.12','XII ms.225--226; POLES C.8--C.9; STRATA G.3--G.4','W0 finite covering; all finite truncations by specified sphere path model.'),
'B.11':('B.5 lifting criterion','XII ms.225--226; POLES C.10; PATHS E.9','One covering and one free-group endomorphism work for every nonzero spectrum, including nonconnective spectra.'),
'B.12':('B.7; Rivera--Wierstra--Zeinalian 2021, Theorem 3','GALOIS D.4--D.5; XII ms.225--226','Finite gerbe and self-pullback; exact nonabelian group presentations checked.'),
'B.13':('B.7; B.8; B.11; B.12','GALOIS D.3; POLES C.10; PATHS E.9','Coverings preserve W1 and rational local-system equivalences, unlike all homology localizers.'),
'B.14':('B.7; exact Kan comma formulas','I ms.117--118; GALOIS D.2 and D.9','Neither containment for proper versus strong cohomological, and dually.'),
'B.15':('B.12; B.13; B.14','GALOIS D.3--D.5; I ms.117--123','Every named finite map tested for W1 and rational locally constant complexes.'),
'B.16':('B.6; Cisinski 2006, 5.2.15; Cisinski 2019, 7.9.8','VI ms.81--84; XII ms.222--226','Accessible coefficient presentation; no presentability claimed for arbitrary inaccessible W.'),
'B.17':('Cisinski 2006, 6.2.3, 9.2.1 and 9.2.15','POLES C.8--C.9; STRATA G.4','Proper-localizer hypothesis explicitly verified; elementary W0 criterion also proved.'),
'B.18':('B.11','POLES C.10; XII ms.225--226','Bounds for intrinsic homology fibrations; simplex tests insufficient.'),
'B.19':('B.7; B.8','VII ms.161--169; PATHS E.4--E.5','Independent all-ended fence proof and functorial factorization; not a strict bifibration.'),
'B.20':('Exact all-type category definition','VII ms.161--166; PATHS E.3','Smoothness proved by padding and contractible slice; empty outgoing lift and two incoming type maps refute stronger claims.'),
'B.21':('B.19; exact rectangular-band multiplication','STRATA E.11; PATHS E.6 and E.11','Open only for existence of some alternative bifibration; standard path obstruction checked.'),
'B.22':('B.2; B.7; B.9; B.16; Cisinski 2019, 4.4.4 and 4.4.18','Lead 1; XII ms.222--226','All simplicial bases using true covariant structures; accessible coefficient extension and rigidity.'),
'C.1':('B.1; Cisinski 2006, 4.2.15 and 4.2.18','VI ms.83; XII ms.224--225','Two specified elements-based candidates, not an unstated unique notion.'),
'C.2':('C.1; B.3 last-vertex comparison','XII ms.224--225; Part C','Candidate duality fails already on the test category Delta; does not deny directed simplicial opposition.'),
'C.3':('C.1; categorical lifting definitions','XII ms.224--225; Part C','All maps elementwise smooth; proper iff naturality squares cartesian for W subset W0.'),
'C.4':('E.1-type formal pullback recipe; B.22','VI ms.84; XII ms.224--225','Exact sufficient duality data; changing index to its opposite is distinct from simplex reversal.'),
'C.5':('Ara--Maltsiniotis 2018, Theorem 5.2 and Remark 5.3; 2022 Corollary 6.8','Recent-results family 317; Part C','Opened exact Theorem A references and slice conventions; independent of model claim.'),
'C.6':('C.5; Ara--Maltsiniotis 2022, Theorem 6.6','Recent-results family 317; XII ms.224--225','Formal fine duality for every strict dimension, with total-cell reversal.'),
'C.7':('C.6; Ara--Maltsiniotis 2022, 6.4 and 6.6','Recent-results family 317; Part C','All cell dualities and universal preservation definitions; no unproved lifting characterization.'),
'C.8':('Ara--Maltsiniotis 2014, Theorem 6.27 and Corollary 6.32','Recent-results family 317','Verified published dimension-two theorem, not reliance on September 2026 claim.'),
'C.9':('C.8 for n=2; conditional OpenAI2026Thomason for n>2','VI ms.83; Recent-results family 317','Precise coarse slice consequence only.'),
'C.10':('C.5--C.9; B.4','Recent-results family 317; Parts C and E','Open relative Street-nerve recognition and higher base-change criterion; exact missing comparisons stated.')}
fields=['id','statement','status','where_proved','depends_on','manuscript_rows_or_pages_settled','notes']
counts={}
seen=[]
for part in ['B','C']:
    text=(ROOT/'sections'/f'{part}.tex').read_text()
    matches=list(re.finditer(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}\s*([\s\S]*?)\\end\{claim\}',text))
    rows=[]
    for m in matches:
        id,status,title,statement=m.groups()
        assert status in ['Proved','Refuted','Known','Open']
        assert id in DATA and id not in seen
        seen.append(id)
        deps,pages,notes=DATA[id]
        rows.append(dict(zip(fields,[id,re.sub(r'\s+',' ',statement).strip(),status,f'sections/{part}.tex, claim {id}',deps,pages,notes])))
        counts[status]=counts.get(status,0)+1
    with (ROOT/f'{part}_results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
assert set(seen)==set(DATA)
bib_path=ROOT/'BISITE_references.bib'
if not bib_path.exists():
    bib_path=ROOT/'BC_references.bib'
bib=bib_path.read_text()
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
cited=set()
for part in ['B','C']:
    text=(ROOT/'sections'/f'{part}.tex').read_text()
    for match in re.findall(r'\\cite\w*\s*(?:\[[^]]*\])?\s*\{([^}]+)\}',text):
        cited.update(match.split(','))
assert cited<=keys,sorted(cited-keys)
assert len(re.findall(r'note\s*=\s*\{(?:verified|unverified)(?::|[ -])',bib,re.I))==len(keys)
output={'claims':len(seen),'status_counts':counts,'citation_keys':sorted(cited),'all_citations_resolved':True,'all_bibliographic_entries_flagged':True}
(ROOT/'code/bc_register.out.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
