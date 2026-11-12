#!/usr/bin/env python3
"""Validate the complete French plan against the supplied original units.

This is a structural and source-preservation audit, not a mathematical proof
checker. LuaLaTeX compilation is reported separately by the reader builder.
"""
from pathlib import Path
import collections,csv,hashlib,json,re,sys
import build_readers as B

ROOT=Path('work/fr')
OUT=Path('output/records')
PLAN=OUT/'FR_CORRECTION_PLAN.json'
PRIVATE=re.compile(r'(?:[A-Za-z]:[\\/](?:Users|home)[\\/][^\s\n"<>]+|/(?:Users|home|root|workspace|tmp|opt|usr|var)/[^\s\n"<>]+|[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,})')
TOKEN=re.compile(r'\\(?:begin|end)\{[^}]+\}|\\[A-Za-z@]+|\\.|\$\$|[{}$]')

def active(s):
    return re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),s)

def structure(s):
    s=active(s);depth=0;minimum=0;dollars=0;displays=0;parens=0;stack=[];bad=[]
    for m in TOKEN.finditer(s):
        t=m.group()
        if t=='{':depth+=1
        elif t=='}':depth-=1;minimum=min(minimum,depth)
        elif t=='$':dollars+=1
        elif t in (r'\[',r'\]'):displays+=1 if t==r'\[' else -1
        elif t in (r'\(',r'\)'):parens+=1 if t==r'\(' else -1
        elif t.startswith(r'\begin{'):stack.append(t[7:-1])
        elif t.startswith(r'\end{'):
            name=t[5:-1]
            if stack and stack[-1]==name:stack.pop()
            else:bad.append(name)
    return {'brace_balance':depth,'minimum_brace_depth':minimum,'inline_dollar_parity':dollars%2,
            'display_delimiter_balance':displays,'paren_math_balance':parens,
            'unbraced_script_chains':len(re.findall(r'(?<!\\)([_^])(?:\\[A-Za-z@]+|[A-Za-z0-9])\s*\1',s)),
            'unclosed_environments':stack,'unmatched_environment_ends':bad}

def main():
    data=PLAN.read_bytes();plan=json.loads(data);rows=plan['rows'];edits=plan['edits'];errors=[]
    expected=[]
    for p in sorted((ROOT/'companion_corrections').glob('*.csv')):
        part=p.stem.removesuffix('_corrections')
        for i,row in enumerate(csv.DictReader(p.open()),1):
            if row['kind']=='edition_slip_kept':expected.append(f'{part}:{i}')
    byrow={r['id']:r for r in rows};byedit={e['id']:e for e in edits}
    if len(rows)!=1879 or len(byrow)!=len(rows) or set(byrow)!=set(expected):errors.append('Correction-row coverage differs from the supplied CSVs.')
    terminal={'applied','merged','no_change','rejected'}
    for r in rows:
        if r['status'] not in terminal:errors.append('Nonterminal row: '+r['id'])
        if not r.get('reason'):errors.append('Missing decision reason: '+r['id'])
        if bool(r['edit_ids'])!=(r['status'] in {'applied','merged'}):errors.append('Status/variant mismatch: '+r['id'])
        for eid in r['edit_ids']:
            if eid not in byedit or r['id'] not in byedit[eid]['sources']:errors.append('Inconsistent row-to-variant link: '+r['id'])
    duplicate_keys=set();groups=collections.defaultdict(list)
    for e in edits:
        key=tuple(e[k] for k in ('unit','start','end','before','after'))
        if key in duplicate_keys:errors.append('Unmerged exact duplicate: '+e['id'])
        duplicate_keys.add(key);groups[e['unit']].append(e)
        if not e.get('sources') or not e.get('reason'):errors.append('Missing variant provenance: '+e['id'])
        for rid in e['sources']:
            if rid not in byrow or e['id'] not in byrow[rid]['edit_ids']:errors.append('Inconsistent variant-to-row link: '+e['id'])
    units=[];structural_deltas=[];new_controls=[];total_notes=0;anchor_counts=collections.Counter()
    for p in sorted((ROOT/'transcription').rglob('*_p*.tex')):
        rel=str(p.relative_to(ROOT/'transcription'));s=p.read_text();es=groups.pop(rel,[])
        try:t=B.patch_exact(s,es)
        except AssertionError as exc:errors.append(str(exc));continue
        # A point insertion at another edit's opening position is also a
        # conflict, including two insertions at the same source offset.
        ordered=sorted(es,key=lambda e:(e['start'],e['end']))
        for a,b in zip(ordered,ordered[1:]):
            if a['start']==b['start'] or a['end']>b['start']:errors.append('Overlapping source coordinates: '+a['id']+'/'+b['id'])
        _,sb=B.body_split(s);_,tb=B.body_split(t)
        anchors=B.anchor_list(sb);newanchors=B.anchor_list(tb)
        anchor_counts.update(a[0] for a in anchors)
        if anchors!=newanchors:errors.append('Page-anchor drift: '+rel)
        _,ns=B.editor_notes(sb,'FR',False,rel);_,nt=B.editor_notes(tb,'FR',False,rel)
        sn=[(n['kind'],n['before']) for n in ns];tn=[(n['kind'],n['before']) for n in nt]
        if sn!=tn:errors.append('Editorial-note drift: '+rel)
        _,sf=B.editors_front(sb,'FR',True);_,tf=B.editors_front(tb,'FR',True)
        if sf!=tf:errors.append('Editorial-front-note drift: '+rel)
        total_notes+=len(ns)
        bs,ts=structure(sb),structure(tb)
        if bs!=ts:structural_deltas.append({'unit':rel,'before':bs,'after':ts,'variants':[e['id'] for e in es]})
        # Source syntax deficits are reported, but only newly introduced
        # deficits are a failure of this exact-correction audit.
        for k,v in ts.items():
            if v and v!=bs[k]:errors.append('New TeX structure deficit '+k+': '+rel)
        oldcmd=set(re.findall(r'\\[A-Za-z@]+',active(s)))
        newcmd=set(re.findall(r'\\[A-Za-z@]+',active(t)))-oldcmd
        if newcmd:new_controls.append({'unit':rel,'commands':sorted(newcmd)})
        units.append({'unit':rel,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),
                      'corrected_sha256':hashlib.sha256(t.encode()).hexdigest(),
                      'variants':len(es),'editorial_notes':len(ns),'page_anchors':len(anchors),
                      'exact_source_slices':'pass','editorial_notes_preserved':sn==tn,
                      'page_anchors_preserved':anchors==newanchors,'source_structure':bs,'corrected_structure':ts})
    if groups:errors.append('Edits target unknown units.')
    if len(units)!=243:errors.append('Expected 243 source units.')
    privacy_files=[PLAN,OUT/'FR_CORRECTION_COVERAGE.tsv',OUT/'CORRECTIONS_DECIDED.tsv']+list((OUT/'decisions/source/french').glob('*.json'))
    privacy_count=sum(len(PRIVATE.findall(p.read_text())) for p in privacy_files)
    if privacy_count:errors.append('Private path or e-mail pattern in correction records.')
    report={'plan_sha256':hashlib.sha256(data).hexdigest(),'status':'pass' if not errors else 'fail',
            'rows_expected':len(expected),'rows_accounted':len(rows),'row_status_counts':plan['counts'],
            'actual_variants':len(edits),'unique_source_units':len(units),'editorial_notes_checked':total_notes,
            'source_anchor_counts':dict(anchor_counts),'private_pattern_matches':privacy_count,
            'errors':errors,'structure_deltas':structural_deltas,'new_control_sequences_for_compile_review':new_controls,
            'scope':'Exact source offsets, nonoverlap, nonidentity, row provenance, complete source-note text, page-anchor sequence, and whole-unit TeX structure. Compilation and mathematical decisions are documented separately.',
            'units':units}
    (OUT/'FR_CORRECTION_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    partcounts=collections.defaultdict(collections.Counter)
    for r in rows:partcounts[r['part']][r['status']]+=1
    with (OUT/'FR_CORRECTION_COUNTS.tsv').open('w',newline='') as f:
        fields=['part','applied','merged','no_change','rejected','total'];w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
        for part,c in sorted(partcounts.items()):w.writerow({'part':part,**c,'total':sum(c.values())})
    print(json.dumps({k:v for k,v in report.items() if k not in ('units','new_control_sequences_for_compile_review')},ensure_ascii=False,indent=2))
    if errors:sys.exit(1)

if __name__=='__main__':main()
