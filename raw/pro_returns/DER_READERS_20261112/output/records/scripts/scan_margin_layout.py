#!/usr/bin/env python3
"""Find possible margin-label collisions in the six completed reader PDFs.

This focused geometry audit compares identified edition/manuscript labels with
other such labels and with nonlabel text. It does not test mathematical glyphs
against one another. Bounding-box intersections are candidates for visual review.
"""
from pathlib import Path
import argparse,csv,hashlib,json,re
import fitz

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'output';RECORDS=OUT/'records'
BOOKS={'FR':['DER_FR_diplomatique','DER_FR_corrige_apparat','DER_FR_texte_de_lecture'],
       'EN':['DER_EN_diplomatic','DER_EN_corrected_apparatus','DER_EN_reading']}
LABEL=re.compile(r'^\s*(?:p\.|\[(?:page\b|p\.|\d))',re.I)

def digest(data):return hashlib.sha256(data).hexdigest()
def bounds(box):return [round(float(v),3) for v in box]
def review_key(candidate):
    """Bind a visual decision to immutable PDF bytes and the exact candidate."""
    fields=('file','pdf_sha256','page','kind','label','label_bbox','other_text','other_bbox')
    return digest(json.dumps({k:candidate[k] for k in fields},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())

def page_elements(page):
    spans=[];lines=[]
    for bi,block in enumerate(page.get_text('dict')['blocks']):
        for li,line in enumerate(block.get('lines',[])):
            ids=[]
            for si,s in enumerate(line['spans']):
                if not s['text'].strip():continue
                ids.append(len(spans));spans.append(dict(s,id=len(spans),block=bi,line=li))
            if ids:lines.append({'block':bi,'line':li,'ids':ids})
    threshold=page.rect.width-100
    labels=[];owned=set()
    for line in lines:
        for sid in line['ids']:
            span=spans[sid];text=span['text'].strip();font=span['font'];box=fitz.Rect(span['bbox'])
            is_page=bool(re.match(r'^p\.',text,re.I))
            font_ok=('Roman' in font and span['color']!=0) if is_page else ('Mono' in font)
            if box.x0<threshold or span['size']>10.1 or not LABEL.match(text) or not font_ok:continue
            ids=[sid]
            # Continue a wrapped label only within the same PDF text block,
            # with the same font/color/size and no new label prefix.
            bottom=box.y1
            for nxt in lines:
                if nxt['block']!=line['block'] or nxt['line']<=line['line']:continue
                ss=[spans[i] for i in nxt['ids']]
                if any(LABEL.match(s['text']) for s in ss):break
                if not all(s['bbox'][0]>=threshold and abs(s['bbox'][0]-box.x0)<4 and s['font']==font and s['color']==span['color'] and abs(s['size']-span['size'])<.05 for s in ss):break
                rect=fitz.Rect(ss[0]['bbox'])
                for s in ss[1:]:rect|=fitz.Rect(s['bbox'])
                if rect.y0-bottom>3 or rect.y0<bottom-3:break
                ids.extend(nxt['ids']);box|=rect;bottom=rect.y1
            owned.update(ids)
            labels.append({'text':' '.join(spans[i]['text'] for i in ids),'bbox':bounds(box),'span_ids':ids})
    body=[s for s in spans if s['id'] not in owned]
    header=' '.join(s['text'] for s in spans if s['bbox'][1]<60 and s['bbox'][0]<400)
    return labels,body,header

def overlap(a,b,min_area,min_height):
    inter=fitz.Rect(a)&fitz.Rect(b)
    if inter.is_empty or inter.width<.25 or inter.height<min_height or inter.get_area()<min_area:return None
    return {'bbox':bounds(inter),'area_pt2':round(inter.get_area(),3),'width_pt':round(inter.width,3),'height_pt':round(inter.height,3)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--minimum-area',type=float,default=1.0);ap.add_argument('--minimum-height',type=float,default=.5)
    ap.add_argument('--review-file',type=Path,default=RECORDS/'MARGIN_LAYOUT_REVIEW.json',help='Optional visual decisions keyed to the exact PDF hash and candidate geometry.')
    args=ap.parse_args()
    candidates=[];books=[];targets=[];placement_targets=[]
    for lang,names in BOOKS.items():
        for name in names:
            path=OUT/lang/(name+'.pdf');raw=path.read_bytes();sha=digest(raw)
            record=json.loads((RECORDS/'build'/(name+'.json')).read_text())
            assert record['compiled_without_errors'] and not record['passes'][-1]['errors'] and not record['passes'][-1]['missing_glyphs'],name
            assert record['source_tex_sha256']==digest(path.with_suffix('.tex').read_bytes()),('stale source',name)
            assert record['pdf_sha256']==sha,('stale PDF',name)
            total=0;counts={'label_label':0,'label_body_text':0}
            with fitz.open(stream=raw,filetype='pdf') as doc:
                for pi,page in enumerate(doc):
                    labels,body,header=page_elements(page);total+=len(labels)
                    chapter_ii=bool(re.search(r'\b(?:Chapitre|Chapter)\s+II\b(?!I)',header))
                    for label in labels:
                        compact=re.sub(r'\s+','',label['text']).lower()
                        if chapter_ii and compact in ('p.61','[page98]','[page39]'):
                            targets.append({'file':str(path.relative_to(ROOT)),'pdf_sha256':sha,'page':pi+1,'header':header,'label':label['text'],'bbox':label['bbox']})
                        placement_id=None
                        if lang=='FR' and re.search(r'\bChapitre\s+XV\b(?!I)',header) and compact=='p.58':
                            placement_id='BUILD-MARGIN-FR-XV-58'
                        if lang=='EN' and re.search(r'\bChapter\s+XII,\s*5\b',header) and compact=='[page152]':
                            placement_id='BUILD-MARGIN-EN-XIIb-152'
                        if placement_id:
                            adjacent=[s['bbox'][2] for s in body if min(s['bbox'][3],label['bbox'][3])-max(s['bbox'][1],label['bbox'][1])>=args.minimum_height]
                            placement_targets.append({'placement_id':placement_id,'file':str(path.relative_to(ROOT)),
                                'pdf_sha256':sha,'page':pi+1,'header':header,'label':label['text'],'bbox':label['bbox'],
                                'horizontal_clearance_from_adjacent_body_text_pt':round(label['bbox'][0]-max(adjacent),3) if adjacent else None})
                    for i,label in enumerate(labels):
                        for other in labels[i+1:]:
                            hit=overlap(label['bbox'],other['bbox'],args.minimum_area,args.minimum_height)
                            if hit:
                                candidates.append({'file':str(path.relative_to(ROOT)),'pdf_sha256':sha,'page':pi+1,'kind':'label_label','label':label['text'],'label_bbox':label['bbox'],'other_text':other['text'],'other_bbox':other['bbox'],**hit});counts['label_label']+=1
                        for other in body:
                            if other['bbox'][2]<label['bbox'][0]:continue
                            hit=overlap(label['bbox'],other['bbox'],args.minimum_area,args.minimum_height)
                            if hit:
                                candidates.append({'file':str(path.relative_to(ROOT)),'pdf_sha256':sha,'page':pi+1,'kind':'label_body_text','label':label['text'],'label_bbox':label['bbox'],'other_text':other['text'],'other_bbox':bounds(other['bbox']),**hit});counts['label_body_text']+=1
                books.append({'file':str(path.relative_to(ROOT)),'pdf_sha256':sha,'pages':len(doc),'recognized_margin_labels':total,'candidate_counts':counts})
            assert digest(path.read_bytes())==sha,('PDF changed while being scanned',name)
    reviews={}
    if args.review_file.is_file():
        reviews={r['candidate_key']:r for r in json.loads(args.review_file.read_text()).get('reviews',[])}
    review_counts={'no_visible_collision':0,'self_label_fragment':0,'confirmed_collision':0,'unreviewed':0}
    for i,r in enumerate(candidates,1):
        r['id']=f'MARG{i:04d}';r['candidate_key']=review_key(r)
        reviewed=reviews.get(r['candidate_key'])
        r['review_status']=reviewed['status'] if reviewed else 'unreviewed'
        r['review_reason']=reviewed['reason'] if reviewed else ''
        assert r['review_status'] in review_counts
        review_counts[r['review_status']]+=1
    status=('visible_collision_found' if review_counts['confirmed_collision'] else
            'visual_review_required' if review_counts['unreviewed'] else 'pass')
    report={'status':status,'method':'Right-margin labels beginning p., [page, [p., or a bracketed numeral, in the edition-label Roman gray font or manuscript-label monospace font. Only label/label and label/nonlabel-text intersections are tested. Text rectangles include font ascent/descent and can yield visually harmless candidates. Visual decisions are reused only for the same PDF SHA-256, page, label, other text, and both rectangles.','right_margin_origin_threshold':'page width minus 100 points','minimum_intersection_area_pt2':args.minimum_area,'minimum_intersection_height_pt':args.minimum_height,'minimum_intersection_width_pt':.25,'books':books,'targeted_chapter_ii_labels':targets,'unit_specific_placement_targets':placement_targets,'review_counts':review_counts,'candidates':candidates,'scope':'Text-label geometry only; PDF vector paths and arbitrary mathematical glyph overlap are not classified by this audit.'}
    (RECORDS/'MARGIN_LAYOUT_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    fields=['id','file','page','kind','label','label_bbox','other_text','other_bbox','area_pt2','width_pt','height_pt','pdf_sha256','candidate_key','review_status','review_reason']
    with (RECORDS/'MARGIN_LAYOUT_AUDIT.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader()
        for r in candidates:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items() if k in fields})
    print(json.dumps({'status':report['status'],'books':books,'candidates':len(candidates),'targeted_labels':len(targets),'review_counts':review_counts},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
