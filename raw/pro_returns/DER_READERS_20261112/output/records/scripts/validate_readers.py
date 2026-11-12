#!/usr/bin/env python3
"""Validate exact source projections, coverage, notes, anchors and apparatus.

This audit does not infer mathematical truth from successful typesetting.
Every mathematical emendation remains tied to its supplied correction record.
"""
import argparse,collections,csv,hashlib,json,re
from pathlib import Path
import build_readers as B

def digest(b):return hashlib.sha256(b).hexdigest()
def table(p):
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def strip_marks(s):return re.sub(r'\n(?:\\DERmark\{[^}]+\})+\n','',s)
def active(s):return re.sub(r'(?<!\\)%[^\n]*','',s)

def audit_language(lang,require_pdf=True):
    master=B.OUT/lang/f'DER_{lang}_annotated_master.tex';data=B.read_master(master)
    if require_pdf:
        plan=json.loads((B.RECORDS/('FR_CORRECTION_PLAN.json' if lang=='FR' else 'EN_CHANGE_PLAN.json')).read_text())
        assert {e['id']:e for e in plan['edits']}=={e['id']:e for u in data['units'] for e in u['variants']},('master does not contain the current final plan',lang)
    source=B.WORK/('fr/transcription' if lang=='FR' else 'en/translation')
    checks=[];chapters=collections.OrderedDict();issues=[];unitids=[];variantids=[]
    expected_lua='return {\n'+',\n'.join('{'+','.join(B.lua_quote(x) for x in p)+'}' for p in data['pieces'])+'\n}\n'
    raw=master.read_text();stored_lua=raw.split('\n%%DER_LUA_PAYLOAD_BEGIN%%\n',1)[1].split('%%DER_LUA_PAYLOAD_END%%',1)[0]
    assert stored_lua==expected_lua,('Lua/JSON master projection mismatch',lang)
    forms={}
    for i,name in enumerate(B.NAMES[lang]):
        p=master.parent/(name+'.tex');expected='% Generated solely from '+master.name+': DERform='+str(i)+'\n'+B.preamble(lang)+''.join(x[i] for x in data['pieces'])
        assert p.read_text()==expected,('reader drift from master',name)
        rec={'tex_sha256':digest(p.read_bytes()),'bytes':p.stat().st_size}
        if require_pdf:
            c=json.loads((B.RECORDS/'build'/f'{name}.json').read_text())
            assert c['compiled_without_errors'] and not c['passes'][-1]['missing_glyphs'],('failed compilation or missing glyphs',name)
            assert not c['passes'][-1]['undefined'] and not c['passes'][-1]['unsettled'],('unresolved references or unfinished passes',name)
            assert c['source_tex_sha256']==rec['tex_sha256'],('stale PDF source',name)
            assert digest(p.with_suffix('.pdf').read_bytes())==c['pdf_sha256'],('stale PDF hash',name)
            rec.update(pages=c['pages'],pdf_sha256=c['pdf_sha256'],warnings=len(c['passes'][-1]['warnings']),overfull_hboxes=c['passes'][-1]['overfull_hbox'],overfull_vboxes=c['passes'][-1]['overfull_vbox'])
        forms[name]=rec
    for u in data['units']:
        rel=u['unit'];unitids.append(rel);original=(source/rel).read_text();es=u['variants'];variantids.extend(e['id'] for e in es)
        assert digest(original.encode())==u['source_sha256'],('source hash',lang,rel)
        assert B.clean(original)==u['original_source'],('stored source differs',lang,rel)
        regenerated,notes,repairs,assembly=B.build_unit(original,rel,lang,es)
        assert regenerated['forms']==u['forms'],('nonreproducible projection',lang,rel)
        anchors=B.anchor_list(B.body_split(original)[1])
        assert all(B.anchor_list(s)==anchors for s in u['forms']),('anchor drift',lang,rel)
        for e in es:
            assert e['sources'] and all(e['sources']),('missing variant source',e['id'])
            assert e['before']!=e['after'],('identity apparatus entry',e['id'])
        marks=re.findall(r'\\DERmark\{([^}]+)\}',u['forms'][1]);assert collections.Counter(marks)==collections.Counter(e['id'] for e in es),('marker coverage',lang,rel)
        assert not re.search(r'\\DERmark\{(?:FRV|ENV|ENC)',u['forms'][0]+u['forms'][2]),('apparatus mark in another form',lang,rel)
        original_body=B.body_split(B.known_repairs(original,rel)[0])[1]
        corrected_body=B.body_split(B.known_repairs(B.patch_exact(original,es),rel)[0])[1]
        oldnotes=B.editor_notes(original_body,lang,False,rel)[1]
        newnotes=B.editor_notes(corrected_body,lang,False,rel)[1]
        # Explicitly signed prose outside typewriter brackets is editorial
        # material too: contents note, chapter front notes, XIV afterword,
        # and XVIII's signed footnotes. Compare their complete exact spans.
        oldnotes+=B.editors_front(original_body,lang,True)[1]
        newnotes+=B.editors_front(corrected_body,lang,True)[1]
        oldnotes+=B.editorial_sections(original_body,rel,lang,True)[1]
        newnotes+=B.editorial_sections(corrected_body,rel,lang,True)[1]
        if [n['before'] for n in oldnotes]!=[n['before'] for n in newnotes]:
            issues.append({'kind':'editorial_note_changed','language':lang,'unit':rel,'before':[n['before'] for n in oldnotes],'after':[n['before'] for n in newnotes]})
        chapter=Path(rel).parts[0];ch=chapters.setdefault(chapter,{'units':0,'variants':collections.Counter(),'edition_anchors':0,'manuscript_anchors':0,'reading_omissions':collections.Counter(),'neutral_signs':0})
        ch['units']+=1;ch['edition_anchors']+=sum(k=='printedpage' for k,v in anchors);ch['manuscript_anchors']+=sum(k in ('msp','mspin') for k,v in anchors)
        for e in es:ch['variants'][e.get('kind','edition_slip_kept')]+=1
        for n in notes:ch['reading_omissions'][n['kind']]+=1;ch['neutral_signs']+=int(r'\DERlacuna' in n.get('after',''))
        checks.append({'unit':rel,'source_sha256':u['source_sha256'],'variants':len(es),'editorial_notes_exact':not any(x['unit']==rel for x in issues),'anchor_sequence_sha256':digest(json.dumps(anchors,ensure_ascii=False).encode()),'all_projections_reproduced':True})
    assert len(unitids)==243 and len(set(unitids))==243,('unit coverage',lang)
    assert len(variantids)==len(set(variantids)),('duplicate variant ids',lang)
    register=''.join(x[1] for x in data['pieces']);items=re.findall(r'\\DERapparatusitem\{([^}]+)\}',register)
    assert collections.Counter(items)==collections.Counter(variantids),('apparatus register coverage',lang)
    inventory={'language':lang,'units':len(unitids),'variants':len(variantids),'master_sha256':digest(master.read_bytes()),'forms':forms,'chapters':chapters,'unit_checks':checks,'issues':issues}
    (B.RECORDS/f'VALIDATION_{lang}.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    return inventory

def audit_coverage():
    p=json.loads((B.RECORDS/'FR_CORRECTION_PLAN.json').read_text());rows=p['rows'];ids={e['id'] for e in p['edits']}
    assert len(rows)==1879 and len({r['id'] for r in rows})==1879
    assert set(r['status'] for r in rows)<={'applied','merged','no_change','rejected'},'Unfinished French correction decisions'
    for r in rows:
        assert r.get('reason'),('missing decision reason',r['id'])
        if r['status'] in ('applied','merged'):assert r['edit_ids'] and set(r['edit_ids'])<=ids,('uncovered correction',r['id'])
    conventions=table(B.RECORDS/'CONVENTIONS_AUDIT.tsv');assert len(conventions)==223
    en=json.loads((B.RECORDS/'EN_CHANGE_PLAN.json').read_text());enrows=en['rows'];enids={e['id'] for e in en['edits']}
    assert len(enrows)==1879 and {r['id'] for r in enrows}=={r['id'] for r in rows}
    assert set(r['status'] for r in enrows)<={'applied','no_english_effect','merged','already_applied'},'Unfinished English transfer decisions'
    for r in enrows:
        assert r.get('reason'),('missing English transfer reason',r['id'])
        assert set(r.get('edit_ids',[]))<=enids,('missing English variant',r['id'])
        if r['status'] in ('applied','merged'):assert r['edit_ids'],('uncovered English correction',r['id'])
    return {'edition_slip_rows':1879,'french_status_counts':dict(collections.Counter(r['status'] for r in rows)),'english_status_counts':dict(collections.Counter(r['status'] for r in enrows)),'convention_rows':len(conventions),'convention_tables':dict(collections.Counter(r['table'] for r in conventions))}

def counts_markdown(inventories):
    out=['# Apparatus counts','', 'Counts use exact variant records in each annotated master. One printed marker and one register item exist for every variant. A source correction row may specify several disjoint changes; duplicate source rows can share a variant. Common composition repairs and the reading text’s editorial omissions have their own records.', '']
    for inv in inventories:
        lang=inv['language'];out+=['## '+lang,'','| Chapter | Kind | Diplomatic entries | Corrected entries | Reading entries |','|---|---|---:|---:|---:|']
        for chapter,ch in inv['chapters'].items():
            if not ch['variants']:out.append(f'| {B.chapter_title(chapter,lang)} | no variants | 0 | 0 | 0 |')
            for kind,n in sorted(ch['variants'].items()):out.append(f'| {B.chapter_title(chapter,lang)} | {kind} | 0 | {n} | 0 |')
        out+=['',f"Total corrected apparatus entries: **{inv['variants']:,}**.",'','| Chapter | Edition anchors in each form | Manuscript anchors in each form | Reading omissions | Neutral signs |','|---|---:|---:|---:|---:|']
        for chapter,ch in inv['chapters'].items():out.append(f"| {B.chapter_title(chapter,lang)} | {ch['edition_anchors']} | {ch['manuscript_anchors']} | {sum(ch['reading_omissions'].values())} | {ch['neutral_signs']} |")
        out+=['']
    (B.RECORDS/'APPARATUS_COUNTS.md').write_text('\n'.join(out)+'\n')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--language',choices=['FR','EN','both'],default='both');ap.add_argument('--sources-only',action='store_true');a=ap.parse_args()
    inv=[audit_language(l,not a.sources_only) for l in (['FR','EN'] if a.language=='both' else [a.language])]
    coverage=audit_coverage() if not a.sources_only else {'state':'intermediate source audit'}
    result={'coverage':coverage,'languages':[{k:v for k,v in x.items() if k not in ('chapters','unit_checks')} for x in inv],'issues':sum(len(x['issues']) for x in inv)}
    (B.RECORDS/'VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');counts_markdown(inv)
    print(json.dumps({'languages':[(x['language'],x['units'],x['variants']) for x in inv],'issues':result['issues']}))
    assert not result['issues'],'Review reported editorial-note changes before delivery'

if __name__=='__main__':main()
