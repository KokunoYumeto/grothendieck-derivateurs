#!/usr/bin/env python3
"""Audit supplied DER conventions and build exact English change plans.

Inputs are the ZIP-relative trees extracted to work/fr, work/en and work/comp.
All edit offsets address the unchanged UTF-8 Python strings of translation units.
No translated running text is regenerated. Every accepted edit is a finite,
explicit replacement with its source row and a reason. Run from the build root.
"""
from pathlib import Path
import argparse, collections, csv, difflib, hashlib, json, re, unicodedata

ROOT=Path('.')
ENROOT=ROOT/'work/en/translation'; FRROOT=ROOT/'work/fr/transcription'
CONV=ROOT/'work/comp/conventions'; OUT=ROOT/'output/records'


def read(p): return p.read_text(encoding='utf-8-sig')
def table(name): return list(csv.DictReader((CONV/name).open(encoding='utf-8-sig')))
def write_tsv(name,rows,fields):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
        w.writeheader();w.writerows(rows)
def comments(s):return [(m.start(),m.end()) for m in re.finditer(r'(?<!\\)%[^\n]*',s)]
def blank_comments(s):return re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),s)
def arg_end(s,p):
    assert s[p]=='{'
    depth=1;i=p+1
    while i<len(s):
        if s[i]=='\\':
            m=re.match(r'\\(?:[A-Za-z@]+|.)',s[i:]);i+=len(m.group()) if m else 1;continue
        if s[i]=='{':depth+=1
        if s[i]=='}':
            depth-=1
            if not depth:return i+1
        i+=1
    raise ValueError('Unclosed brace')
def editorial_spans(s):
    """Protect complete typewriter arguments and multi-box bracket notes."""
    spans=[];start=None;depth=0
    body=max(0,s.find('\\begin{document}'))
    for m in re.finditer(r'\\(?:texttt|edbr)\s*\{',blank_comments(s)):
        try:e=arg_end(s,m.end()-1)
        except ValueError:continue
        spans.append((m.start(),e))
        if m.start()<body:continue
        arg=s[m.end():e-1]
        if '[' in arg and start is None:start=m.start()
        if start is not None:
            depth+=arg.count('[')-arg.count(']')
            if depth<=0:spans.append((start,e));start=None;depth=0
    for m in re.finditer(r'\\pl(?![A-Za-z])',blank_comments(s[body:])):
        a=body+m.start();b=s.find(']',body+m.end())
        if b>=0:spans.append((a,b+1))
    return spans

def page_at(s,p):
    pages=list(re.finditer(r'\\printedpage\{([^{}]*)\}',blank_comments(s[:p])))
    return pages[-1].group(1) if pages else 'preamble'

def flatten(s):
    s=blank_comments(s)
    if '\\begin{document}' in s:s=s.split('\\begin{document}',1)[1].rsplit('\\end{document}',1)[0]
    math=re.compile(r'\\\[.*?\\\]|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$.*?(?<!\\)\$|\\\(.*?\\\)',re.S)
    extra=[]
    def masked(m):
        for a in re.finditer(r'\\(?:text\w*|emph|mbox|hbox|shortstack|tl|tls|lab)\s*\{',m.group()):
            try:extra.append(m.group()[a.end():arg_end(m.group(),a.end()-1)-1])
            except ValueError:pass
        return ' § '
    s=math.sub(masked,s)+' '+' '.join(extra)
    s=re.sub(r'\\(?:printedpage|msp|label|tag|ref|setcounter|vspace|hspace)\*?(?:\[[^\]]*\])?\{[^{}]*\}',' ',s)
    s=re.sub(r'\\(?:begin|end)\{[^{}]*\}(?:\[[^\]]*\])?',' ',s)
    s=re.sub(r'\\[A-Za-z@]+\*?','',s).replace('{','').replace('}','').replace('~',' ')
    s=re.sub(r'\s+',' ',s)
    return re.sub(r'§\s*-\s*','§-',s)

def load_terms():
    result={}
    for l in read(ROOT/'work/en/scripts/terms_DER.txt').splitlines():
        if not l.strip() or l.startswith('#'):continue
        vals=re.split(r'\s;;(?:\s|$)',l)
        if len(vals)==3:result[vals[0]]=vals[2]
    return result

NOTATION_FLAGS={
1:('Replacing \\mathbf{D} by \\mathbb{D} would change the chapter-specific printed letter; the entry itself records the variation and an outstanding manuscript check.','Keep the derivator letter of each source unit.'),
2:('Replacing source \\mathsf{HOT} by \\mathrm{HOT} would change the source alphabet.','Keep each source occurrence of HOT and its indices.'),
3:('Inserting parentheses around Cat would insert tokens absent from the transcribed edition.','Keep Cat, (Cat), and each source macro exactly at its original occurrences.'),
4:('Inserting parentheses around Hot would insert tokens absent from the transcribed edition.','Keep Hot, (Hot), and all existing indices.'),
5:('Replacing Ens by Sets would change the named notation preserved by the current reader instruction.','Keep Ens wherever the edition writes Ens.'),
6:('Replacing Dia by Diag would change the chapter-I name rather than translate surrounding prose.','Keep the source Dia/Diag spelling at each occurrence.'),
7:('Replacing superscript o by \\circ would change a source glyph; the entry reports that the early chapters were not checked against the print.','Keep the source opposite-category superscript.'),
14:('Replacing \\mathbb{N}, \\mathbb{Z}, \\mathbb{R} by \\mathbf forms would change the source alphabet.','Keep each source number alphabet.'),
15:('Replacing \\mathcal{U} by \\mathfrak{U} would change a source alphabet without an occurrence-specific correction.','Keep the source universe symbol.'),
19:('Replacing \\subseteq by \\subset would remove the printed equality stroke. The present task explicitly preserves the edition notation.','Keep \\subset and \\subseteq at their source occurrences.'),
20:('Replacing \\leqslant by \\leq would change the source inequality sign.','Keep source \\leq, \\leqslant and corresponding greater-than forms.'),
21:('Replacing arrows by text/display position would change printed arrow lengths without a correction row.','Keep source arrow commands and lengths.'),
25:('Replacing all single quotation marks by double marks conflicts with TYPESETTING.csv row 8, which preserves the edition single/double choice.','Keep each source single/double quotation choice; encoding alone can vary.'),
}
TYPESETTING_FLAGS={
3:('The suggested global \\mathrm-to-\\operatorname substitution changes spacing. The table supplies no occurrence-level printed correction, while the current instruction preserves notation.','Keep existing roman operator encodings and their source spacing.'),
4:('One shared definition would change meaning where a macro name has different chapter-local definitions; the table itself records six definitions of Ob and Hom.','Use one book preamble with the unchanged unit-local definitions scoped separately.'),
5:('The entry expressly says the print was not compared mark by mark. Replacing accents by letter size would change unverified source marks.','Keep each source tilde/bar encoding.'),
6:('Replacing hand-built limit signs globally would change source construction and placement; no individual defective occurrence is identified by this row.','Keep existing \\varinjlim, \\varprojlim and hand-built limit signs.'),
}


def convention_plan():
    units={str(p.relative_to(ENROOT)):read(p) for p in sorted(ENROOT.rglob('*_p*.tex'))}
    edits=[];skipped=[]
    def add(unit,a,b,after,source,reason,kind='glossary'):
        s=units[unit]
        if any(a<y and b>x for x,y in comments(s)+editorial_spans(s)):
            skipped.append({'source':source,'unit':unit,'page':page_at(s,a),'before':s[a:b],'after':after,'reason':'Protected editors text or source comment; no alteration.'});return
        if s[a:b]==after:return
        edits.append({'id':'','unit':unit,'start':a,'end':b,'before':s[a:b],'after':after,'sources':[source],'page':page_at(s,a),'place':('local macro definition' if a<s.find('\\begin{document}') else 'running text or formula'),'reason':reason,'kind':kind})
    # Lexical exceptions verified in paired French contexts.
    rules=[
      ('Der-ChVII-456/Der-ChVII-456_p096-100.tex','projective system','inverse system','GLOSSARY_DER:91','French source says système projectif; the supplied glossary prescribes inverse system.'),
      ('der-ch19/der-ch19_p016-020.tex','Filtered inductive limits','Filtering direct limits','GLOSSARY_DER:89;GLOSSARY_DER:92','French source says limites inductives filtrantes; the glossary gives direct limits and filtering.'),
      ('der-ch19/der-ch19_p016-020.tex','filtered','filtering','GLOSSARY_DER:92','French source uses filtrantes; the supplied glossary prescribes filtering.'),
    ]
    for unit,before,after,source,reason in rules:
        s=units[unit]
        for m in re.finditer(re.escape(before),s):add(unit,m.start(),m.end(),after,source,reason)
    # The single-volume first use is in chapter II; subsequent unit-local glosses repeat it.
    for unit in ['Der-ChVI-345/Der-ChVI-345_p101-105.tex','Der-ChVII-456/Der-ChVII-456_p051-055.tex','Der-ChVIII-567/Der-ChVIII-567_p006-010.tex','Der-ChXIIc-30-03-03/Der-ChXIIc-30-03-03_p016-020.tex']:
        s=units[unit]
        for m in re.finditer(r' (?=\(gear\))\(gear\)',s):add(unit,m.start(),m.end(),'','GLOSSARY_DER:164','The first use in chapter II retains fourbi (gear). The same gloss added by the translation at later unit first uses is removed for the single book; the French wording is retained.')
    # Explicit finite encoding repairs, preserving each intended printed letter or word.
    for unit,s in units.items():
        for m in re.finditer(r'\\mathscr\{X\}',s):
            add(unit,m.start(),m.end(),r'\mathcal{X}','TYPESETTING:1','The supplied row reports direct edition-page checks (II p.9 and XIIb PDF p.53) establishing the ordinary calligraphic X; this exact token replacement repairs the transcription encoding.', 'typesetting')
        for m in re.finditer(r'\\mathbf\{\\Delta\}',s):
            add(unit,m.start(),m.end(),r'\boldsymbol{\Delta}','TYPESETTING:2;DER_I-a:1','Use the explicit bold-Delta encoding from the supplied typesetting row. DER_I-a correction row 1 reports missing U+0001 glyphs under the requested fontspec/LuaLaTeX build and the boldsymbol repair.', 'typesetting')
        for m in re.finditer(r'\\(?:text|textup|textit)\{(?:\\upshape )?def\}',s):
            add(unit,m.start(),m.end(),r'\mathrm{def}','TYPESETTING:7;NOTATION_DER:17','The English definition abbreviation is def; the supplied convention specifies roman math lettering. The abbreviation and its equality-sign position are preserved.', 'typesetting')
    edits.sort(key=lambda e:(e['unit'],e['start'],e['end']))
    for i,e in enumerate(edits,1):e['id']=f'ENC{i:04d}'
    for a,b in zip(edits,edits[1:]):
        assert a['unit']!=b['unit'] or a['end']<=b['start'],(a,b)
    glossary=table('GLOSSARY_DER.csv');notation=table('NOTATION_DER.csv');typesetting=table('TYPESETTING.csv')
    terms=load_terms();flat=' '.join(flatten(s) for s in units.values())
    after_units=units.copy()
    for u in units:
        for e in reversed([e for e in edits if e['unit']==u]):after_units[u]=after_units[u][:e['start']]+e['after']+after_units[u][e['end']:]
    after_flat=' '.join(flatten(s) for s in after_units.values())
    audit=[];flagged=[]
    for i,r in enumerate(glossary,1):
        source=f'GLOSSARY_DER:{i}';changes=[e['id'] for e in edits if any(source in x.split(';') for x in e['sources'])]
        audit.append({'table':'GLOSSARY_DER.csv','row':i,'entry':r['french'],'requested_rendering':r['english'],'decision':'applied' if changes else 'retained','matches_before':len(re.findall(terms[r['french']],flat,re.I)),'matches_after':len(re.findall(terms[r['french']],after_flat,re.I)),'edit_ids':';'.join(changes),'reason':'English form checked with the supplied terms_DER.txt pattern on comment-free prose and formula text. Counts are lexical matches, not a claim that every sense was independently proved. Source spelling and agreement corrections are transferred separately. Editors wording is protected.'})
    for i,r in enumerate(notation,1):
        source=f'NOTATION_DER:{i}';changes=[e['id'] for e in edits if any(source in x.split(';') for x in e['sources'])]
        if i in NOTATION_FLAGS:
            reason,proposed=NOTATION_FLAGS[i];decision='flagged_preserve_source'
            flagged.append({'table':'NOTATION_DER.csv','row':i,'entry':r['object'],'requested_rendering':r['english_form'],'reason':reason,'proposed_rendering':proposed})
        else:reason='Checked against source-preservation and existing English macro conventions; original letter, abbreviation, indices, delimiters and emphasis retained.';decision='applied' if changes else 'retained'
        audit.append({'table':'NOTATION_DER.csv','row':i,'entry':r['object'],'requested_rendering':r['english_form'],'decision':decision,'matches_before':'','matches_after':'','edit_ids':';'.join(changes),'reason':reason})
    for i,r in enumerate(typesetting,1):
        source=f'TYPESETTING:{i}';changes=[e['id'] for e in edits if any(source in x.split(';') for x in e['sources'])]
        if r['work']!='DER':decision='outside_DER_scope';reason='This row is explicitly labeled LM; the present books are DER.'
        elif i in TYPESETTING_FLAGS:
            reason,proposed=TYPESETTING_FLAGS[i];decision='flagged_preserve_source'
            flagged.append({'table':'TYPESETTING.csv','row':i,'entry':r['written_form'],'requested_rendering':r['unified_form'],'reason':reason,'proposed_rendering':proposed})
        elif i==2:decision='common_build_repair';reason='The missing-glyph repair is shared by diplomatic, corrected and reading builds. It preserves the printed bold Delta and is recorded separately from variants.'
        elif changes:decision='applied';reason='Exact token replacements are individually enumerated with original offsets and retained-source provenance.'
        else:decision='retained';reason='Source notation and quote multiplicity retained; French p. ex. is translated as e.g. in the English. N.B. remains as printed.'
        audit.append({'table':'TYPESETTING.csv','row':i,'entry':r['written_form'],'requested_rendering':r['unified_form'],'decision':decision,'matches_before':'','matches_after':'','edit_ids':';'.join(changes),'reason':reason})
    common_build_repairs=[e for e in edits if e['before']==r'\mathbf{\Delta}']
    edits=[e for e in edits if e['before']!=r'\mathbf{\Delta}']
    plan={'common_build_repairs':common_build_repairs,'offset_convention':'Python Unicode character offsets in the ORIGINAL translation unit','units':len(units),'edits':edits,'rows':[],'counts':{'conventions_edits':len(edits),'common_build_repairs':len(common_build_repairs),'flagged_entries':len(flagged),'audited_entries':len(audit),'protected_candidates':len(skipped)},'protected_candidates':skipped}
    (OUT/'EN_CONVENTIONS_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
    write_tsv('GLOSSARY_FLAGGED.tsv',flagged,['table','row','entry','requested_rendering','reason','proposed_rendering'])
    write_tsv('CONVENTIONS_AUDIT.tsv',audit,['table','row','entry','requested_rendering','decision','matches_before','matches_after','edit_ids','reason'])
    write_tsv('EN_CONVENTIONS_PROTECTED.tsv',skipped,['source','unit','page','before','after','reason'])
    return plan

def combined_plan(conventions,transfer,frplan):
    """Compose only exact, source-verified nested amendments; preserve all provenance."""
    unique={}
    for original in conventions['edits']+transfer['edits']:
        e=dict(original);e['sources']=[s for x in e['sources'] for s in x.split(';')]
        e['fr_edit_ids']=list(e.get('fr_edit_ids',[]))
        k=(e['unit'],e['start'],e['end'],e['before'],e['after'])
        if k in unique:
            for field in ['sources','fr_edit_ids']:
                unique[k][field]=list(dict.fromkeys(unique[k][field]+e[field]))
        else:unique[k]=e
    candidates=sorted(unique.values(),key=lambda e:(e['unit'],e['start'],-e['end']))
    merged=[]
    for e in candidates:
        if not merged or merged[-1]['unit']!=e['unit'] or merged[-1]['end']<=e['start']:
            if merged and merged[-1]['unit']==e['unit'] and merged[-1]['start']==merged[-1]['end']==e['start']==e['end']:
                raise ValueError(('Distinct insertions at the same original position',merged[-1],e))
            merged.append(e);continue
        outer=merged[-1]
        assert outer['start']<=e['start'] and e['end']<=outer['end'],('Crossing original intervals',outer,e)
        assert e['before'],('Unresolved nested insertion',outer,e)
        relative_start=e['start']-outer['start'];relative_end=e['end']-outer['start']
        only_child=outer['before'][:relative_start]+e['after']+outer['before'][relative_end:]
        if outer['after']==only_child:
            pass
        elif outer['after'].count(e['before'])==1:
            outer['after']=outer['after'].replace(e['before'],e['after'],1)
        elif e['after'] and outer['after'].count(e['after'])==1:
            pass
        else:raise ValueError(('Nested change has no unique retained witness',outer,e))
        for field in ['sources','fr_edit_ids']:outer[field]=list(dict.fromkeys(outer[field]+e[field]))
        outer['reason']+=' '+e['reason']
        outer.setdefault('composed_changes',[]).append({'before':e['before'],'after':e['after'],'sources':e['sources']})
    from transfer_english import protected,safe_change
    unit_text={};source_ids=collections.defaultdict(list);fr_ids=collections.defaultdict(list)
    for i,e in enumerate(merged,1):
        e['id']=f'ENV{i:04d}'
        s=unit_text.setdefault(e['unit'],read(ENROOT/e['unit']))
        assert s[e['start']:e['end']]==e['before'],('Original source mismatch',e)
        assert safe_change(s,e['start'],e['end'],e['after'],protected(s)),('Protected source altered',e)
        assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',e['after']),('Control character in replacement',e)
        for sid in e['sources']:source_ids[sid].append(e['id'])
        for fid in e['fr_edit_ids']:fr_ids[fid].append(e['id'])
    transfer_rows=transfer['rows']
    bysource=collections.defaultdict(list)
    for r in transfer_rows:
        r['english_edit_ids']=';'.join(fr_ids[r['fr_edit_id']])
        for sid in r['source_rows'].split(';'):bysource[sid].append(r)
    rows=[]
    for fr in frplan['rows']:
        sid=fr['id'];trs=bysource[sid];effects=source_ids[sid]
        r={'id':sid,'source_status':fr['status'],'page':fr['pdf_page'],'place':fr['place'],'status':'','edit_ids':effects,'fr_edit_ids':[t['fr_edit_id'] for t in trs],'reason':''}
        if any(t['status']=='review' for t in trs):r.update(status='review',reason='An English correspondence still requires explicit review.')
        elif fr['status'] in ('unresolved','partial'):r.update(status='awaiting_french_decision',reason=fr['reason'])
        elif effects:r.update(status='applied',reason='The corresponding English source changes are enumerated by the listed exact original-offset variants; duplicate effects share one variant.')
        elif trs:r.update(status='no_english_effect',reason=' '.join(dict.fromkeys(t['reason'] for t in trs)))
        else:r.update(status='no_english_effect',reason='No French source variant was adopted. '+fr['reason'])
        rows.append(r)
    counts={'english_variants':len(merged),'conventions_edits_before_composition':len(conventions['edits']),'common_build_repairs':len(conventions['common_build_repairs']),'french_variants':len(frplan['edits']),'transfer_statuses':dict(collections.Counter(r['status'] for r in transfer_rows)),'source_row_statuses':dict(collections.Counter(r['status'] for r in rows))}
    plan={'offset_convention':conventions['offset_convention'],'units':conventions['units'],'common_build_repairs':conventions['common_build_repairs'],'edits':merged,'rows':rows,'counts':counts,'input_sha256':{'FR_CORRECTION_PLAN.json':hashlib.sha256((OUT/'FR_CORRECTION_PLAN.json').read_bytes()).hexdigest(),'EN_TRANSFER_DECISIONS.json':hashlib.sha256((OUT/'EN_TRANSFER_DECISIONS.json').read_bytes()).hexdigest()}}
    fields=['fr_edit_id','source_rows','unit','fr_start','fr_end','fr_before','fr_after','fr_context','en_context','status','english_edit_ids','en_before','en_after','reason','alignment_witness']
    write_tsv('EN_TRANSFER_AUDIT.tsv',transfer_rows,fields)
    write_tsv('EN_SOURCE_ROW_AUDIT.tsv',[dict(r,edit_ids=';'.join(r['edit_ids']),fr_edit_ids=';'.join(r['fr_edit_ids'])) for r in rows],['id','source_status','page','place','status','edit_ids','fr_edit_ids','reason'])
    (OUT/'EN_TRANSFER_AUDIT.json').write_text(json.dumps({'rows':transfer_rows,'counts':counts},ensure_ascii=False,indent=2)+'\n')
    # Point the conventions audit to the final apparatus identifiers, while
    # keeping shared build repairs visibly outside that apparatus.
    with (OUT/'CONVENTIONS_AUDIT.tsv').open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t');audit_fields=list(reader.fieldnames);audit=list(reader)
    common_sources=collections.defaultdict(list)
    for e in conventions['common_build_repairs']:
        for x in e['sources']:
            for sid in x.split(';'):common_sources[sid].append(e['id'])
    for r in audit:
        sid=r['table'].removesuffix('.csv')+':'+r['row']
        r['edit_ids']=';'.join(source_ids[sid])
        r['common_build_repair_ids']=';'.join(common_sources[sid])
    write_tsv('CONVENTIONS_AUDIT.tsv',audit,audit_fields+['common_build_repair_ids'])
    return plan

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--conventions-only',action='store_true');args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    plan=convention_plan()
    if not args.conventions_only:
        from transfer_english import build
        frplan=json.loads((OUT/'FR_CORRECTION_PLAN.json').read_text())
        plan=combined_plan(plan,build(frplan),frplan)
    (OUT/'EN_CHANGE_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(plan['counts'],indent=2))
