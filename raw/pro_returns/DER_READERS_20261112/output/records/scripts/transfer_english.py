#!/usr/bin/env python3
"""Project verified French correction intervals onto paired English source text.

The input files remain unchanged. Every output interval addresses the original
English unit; uncertain or linguistic correspondences are retained for explicit
review. Page/manuscript anchors and unchanged mathematical strings supply the
alignment. The manual decision file is part of the reproducible audit inputs.
"""
from pathlib import Path
import collections,difflib,json,re

FRROOT=Path('work/fr/transcription'); ENROOT=Path('work/en/translation')
OUT=Path('output/records'); SCRATCH=Path('work/english_conventions')
MATH=re.compile(r'\\\[[\s\S]*?\\\]|(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$[^$]*?(?<!\\)\$|\\\([\s\S]*?\\\)')
ANCHOR=re.compile(r'\\(printedpage|msp|mspin)\{([^{}]*)\}')
TEXT=re.compile(r'\\(?:text\w*|mbox|hbox|emph)\s*\{')

def blank_comments(s):return re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m[0]),s)
def comments(s):return [(m.start(),m.end()) for m in re.finditer(r'(?<!\\)%[^\n]*',s)]
def arg_end(s,p):
    depth=1;i=p+1
    while i<len(s):
        if s[i]=='\\':
            m=re.match(r'\\(?:[A-Za-z@]+|.)',s[i:]);i+=len(m[0]) if m else 1;continue
        if s[i]=='{':depth+=1
        elif s[i]=='}':
            depth-=1
            if not depth:return i+1
        i+=1
    return len(s)
def editorial_spans(s):
    spans=[];start=None;depth=0
    body=max(0,s.find('\\begin{document}'))
    # A preamble definition such as \newcommand{\pl}{\texttt{[rather}}
    # defines an editorial marker; its bracket does not open a body note.
    scanned=blank_comments(s)
    for m in re.finditer(r'\\(?:texttt|edbr)\s*\{',scanned):
        e=arg_end(s,m.end()-1);spans.append((m.start(),e))
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
def protected(s):return comments(s)+editorial_spans(s)+[(m.start(),m.end()) for m in ANCHOR.finditer(blank_comments(s))]
def intersects(a,b,spans):return any(x<b and a<y or a==b and x<a<y for x,y in spans)
def safe_change(s,a,b,after,spans):
    touched=sorted((x,y) for x,y in spans if x<b and a<y or a==b and x<a<y)
    if not touched:return True
    if any(x<a or b<y for x,y in touched):return False
    # A replacement can enclose an editorial note only when its full exact
    # original text is preserved. The caller never edits inside that note.
    return all(s[x:y] in after for x,y in touched)
def literal_matches(s,before):
    p=r'\s+'.join(re.escape(x) for x in re.split(r'\s+',before))
    return list(re.finditer(p,s))
def key(e):return '|'.join(e['sources'])+'|'+e['unit']+'|'+str(e['start'])+'|'+e['before']+'|'+e['after']
def rowkey(e):return '|'.join(e['sources'])+'|'+e['before']+'|'+e['after']
def brief(s,n=400):return re.sub(r'\s+',' ',blank_comments(s)).strip()[:n]
def page_at(s,p):
    matches=list(re.finditer(r'\\printedpage\{([^{}]*)\}',blank_comments(s[:p])))
    return matches[-1][1] if matches else 'preamble'

def norm(s,mask_text=False):
    t=blank_comments(s)
    if mask_text:
        chars=list(t)
        for m in TEXT.finditer(t):
            e=arg_end(t,m.end()-1)
            chars[m.end():e-1]=[' ']*(e-1-m.end())
        t=''.join(chars)
    inds=[i for i,c in enumerate(t) if not c.isspace()]
    return ''.join(t[i] for i in inds),inds
def anchors(s):
    seen=collections.Counter();result=[]
    for m in ANCHOR.finditer(blank_comments(s)):
        k=m[1]+':'+re.sub(r'^page\s*','',m[2]).strip()
        seen[k]+=1;result.append((k+':'+str(seen[k]),m.start(),m.end()))
    return result

class AlignedUnit:
    def __init__(self,unit):
        self.unit=unit;self.fr=(FRROOT/unit).read_text();self.en=(ENROOT/unit).read_text();self.protected=protected(self.en)
        fa=anchors(self.fr);ea={x[0]:x for x in anchors(self.en)}
        common=[(0,0)]
        for k,a,b in fa:
            if k in ea:common.append((a,ea[k][1]))
        common.append((len(self.fr),len(self.en)))
        self.segments=[]
        for (a,x),(b,y) in zip(common,common[1:]):
            if a<b and x<y:self.segments.append((a,b,x,y))
        self.mathpairs={};self.mathspans=[];self.alignments={}
        for seg in self.segments:
            a,b,x,y=seg
            fm=[(m.start()+a,m.end()+a,m[0]) for m in MATH.finditer(blank_comments(self.fr[a:b]))]
            em=[(m.start()+x,m.end()+x,m[0]) for m in MATH.finditer(blank_comments(self.en[x:y]))]
            self.mathspans.extend(fm)
            fk=[norm(v[2],True)[0] for v in fm];ek=[norm(v[2],True)[0] for v in em]
            sm=difflib.SequenceMatcher(None,fk,ek,autojunk=False)
            pairs=[]
            for tag,i,j,k,l in sm.get_opcodes():
                if tag=='equal':pairs.extend((u,k+u-i,'exact_structure') for u in range(i,j))
                elif tag=='replace' and j-i==l-k:
                    pairs.extend((u,k+u-i,'ordered_math') for u in range(i,j))
                elif tag=='replace':
                    # Only pair a nonidentical residual block when both sides
                    # uniquely identify it by high mathematical similarity.
                    for u in range(i,j):
                        scores=sorted((difflib.SequenceMatcher(None,fk[u],ek[v],autojunk=False).ratio(),v) for v in range(k,l))
                        if scores and scores[-1][0]>=.85 and (len(scores)==1 or scores[-1][0]-scores[-2][0]>.12):pairs.append((u,scores[-1][1],'unique_math_similarity'))
            used=collections.Counter(v for u,v,q in pairs)
            for u,v,q in pairs:
                if used[v]==1:self.mathpairs[(fm[u][0],fm[u][1])]=(em[v][0],em[v][1],q)

    def segment(self,a,b):
        for seg in self.segments:
            if seg[0]<=a and b<=seg[1]:return seg
        return (0,len(self.fr),0,len(self.en))

    def project(self,e):
        a,b=e['start'],e['end'];seg=self.segment(a,b)
        rec={'fr_edit_id':e['id'],'source_rows':';'.join(e['sources']),'unit':self.unit,'fr_start':a,'fr_end':b,'fr_before':e['before'],'fr_after':e['after'],'fr_context':brief(self.fr[max(seg[0],a-150):min(seg[1],b+150)],600),'en_context':brief(self.en[seg[2]:seg[3]],1600),'status':'review','reason':''}
        # The nearest retained correction comment gives a particularly precise
        # prose witness: the translator copied these source comments verbatim.
        found_comment=None
        for cm in re.finditer(r'(?<!\\)%[^\n]*',self.fr[b:min(seg[1],b+800)]):
            c=cm[0]
            hits=[m.start()+seg[2] for m in re.finditer(re.escape(c),self.en[seg[2]:seg[3]])]
            if ('[sic]' in c or 'Resolved:' in c) and len(hits)==1:
                ep=hits[0];fp=b+cm.start();start=self.en.rfind('\n\n',seg[2],ep)
                start=max(seg[2],ep-1200) if start<0 else start
                rec['en_context']=brief(self.en[start:ep],1600)
                rec['alignment_witness']='Identical retained source correction comment after this translated passage.'
                found_comment=ep;break
        if found_comment is None:
            # Narrow prose between the nearest already paired math boundaries.
            left=[(f,p) for f,p in self.mathpairs.items() if seg[0]<=f[1]<=a]
            right=[(f,p) for f,p in self.mathpairs.items() if b<=f[0]<=seg[1]]
            ex=max(left,key=lambda t:t[0][1])[1][1] if left else seg[2]
            ey=min(right,key=lambda t:t[0][0])[1][0] if right else seg[3]
            if ex<=ey:rec['en_context']=brief(self.en[max(seg[2],ex-80):min(seg[3],ey+80)],1600)
        la=a;lb=b
        while la>0 and (self.fr[la-1].isalpha() or self.fr[la-1] in "'-’"):la-=1
        while lb<len(self.fr) and (self.fr[lb].isalpha() or self.fr[lb] in "'-’"):lb+=1
        rec['fr_word_before']=self.fr[la:lb]
        rec['fr_word_after']=self.fr[la:a]+e['after']+self.fr[b:lb]
        fm=next((m for m in self.mathspans if m[0]<=a and b<=m[1]),None)
        if fm and (fm[0],fm[1]) in self.mathpairs:
            x,y,q=self.mathpairs[(fm[0],fm[1])]
            fstr=self.fr[fm[0]:fm[1]];estr=self.en[x:y]
            rec['en_context']=brief(self.en[max(seg[2],x-100):min(seg[3],y+100)],1400)
            if re.fullmatch(r'[A-Za-zÀ-ÿ-]{2,}',self.fr[la:lb]) and (la==0 or self.fr[la-1]!='\\'):
                rec['reason']='A plain alphabetic token within the display requires an explicit language or notation decision.';return rec,None
            if any(fm[0]+m.end()<=a<=b<fm[0]+arg_end(fstr,m.end()-1) for m in TEXT.finditer(fstr)):
                rec['reason']='The change is inside formula text, including a masked prose insertion; review its English correspondence.';return rec,None
            # Long replacements containing natural-language text require a
            # translated literal decision, even when their formula is aligned.
            if any(re.search(r'[A-Za-zÀ-ÿ]',e['after'][m.end():arg_end(e['after'],m.end()-1)-1]) for m in TEXT.finditer(e['after'])):
                rec['reason']='The replacement contains prose inside a formula; review its English wording.';return rec,None
            if a==b and a in (fm[0],fm[1]) and re.search(r'[^\s,;:.!?()\[\]{}]',e['after']):
                rec['reason']='The insertion adjoins a formula boundary and needs an explicit translated passage.';return rec,None
            bare=re.sub(r'\\[A-Za-z@]+',' ',e['after'])
            if re.search(r'(?<![A-Za-zÀ-ÿ])(?:pour|et|dans|sur|si|de|est|soit|sont|par|dont|un|une|le|la|les|au|aux|des|avec|telle|repr[ée]sent[ée]|restriction|cat[ée]gorie)(?![A-Za-zÀ-ÿ])',bare):
                rec['reason']='The replacement includes natural-language wording and needs an explicit English decision.';return rec,None
            ft,fi=norm(fstr,True);et,ei=norm(estr,True)
            aa=a-fm[0];bb=b-fm[0]
            left=sum(i<aa for i in fi);right=sum(i<bb for i in fi)
            # An edit of masked prose cannot be inferred from formula alignment.
            changed_nonspace=re.sub(r'\s+','',blank_comments(fstr[aa:bb]))
            if changed_nonspace and ft[left:right]!=changed_nonspace:
                rec['reason']='The French edit crosses masked formula prose.';return rec,None
            sm=difflib.SequenceMatcher(None,ft,et,autojunk=False)
            for bl in sm.get_matching_blocks():
                if bl.a<=left and right<=bl.a+bl.size and (left<right or bl.size>=4):
                    el=bl.b+left-bl.a;er=bl.b+right-bl.a
                    xx=ei[el] if el<len(ei) else len(estr)
                    yy=ei[er-1]+1 if er>el else xx
                    # A zero-width insertion immediately after a token belongs
                    # before intervening source whitespace, not at the next word.
                    if aa==bb and left>0 and fi[left-1]+1==aa:xx=yy=ei[el-1]+1
                    candidate=(x+xx,x+yy,e['after'])
                    if not intersects(candidate[0],candidate[1],self.protected):
                        rec.update(status='applied',reason='Projected through the paired '+q+' formula and its unchanged mathematical substring.',en_start=candidate[0],en_end=candidate[1],en_before=self.en[candidate[0]:candidate[1]],en_after=candidate[2]);return rec,candidate
                    rec.update(reason='The matched English interval is protected editorial text or a comment.');return rec,None
            # Detect an explicitly already-corrected entire paired formula.
            corrected=fstr[:aa]+e['after']+fstr[bb:]
            if norm(corrected,True)[0]==et:
                rec.update(status='already_incorporated',reason='The paired English formula exactly equals the corrected French formula after whitespace and prose masking.',en_before=estr,en_after=estr);return rec,None
            rec['reason']='The paired formula differs at the corrected mathematical interval.'
        else:rec['reason']='The correction is prose, punctuation, or crosses formula boundaries; compare the paired translated passage.'
        return rec,None

    def manual(self,e,rec,d):
        if 'pairs' not in d:
            rec.update(status=d['status'],reason=d['reason']);return rec,[]
        seg=self.segment(e['start'],e['end']);out=[];incorporated=True
        for before,after in d['pairs']:
            candidates=[m for m in literal_matches(self.en,before) if safe_change(self.en,m.start(),m.end(),after,self.protected)]
            near=[m for m in candidates if seg[2]<=m.start() and m.end()<=seg[3]]
            if len(near)==1:candidates=near
            if len(candidates)!=1 and not (candidates and d.get('all_matches')):
                rec.update(status='review',reason='Manual English literal has '+str(len(candidates))+' eligible original matches: '+before);return rec,[]
            for m in candidates:out.append((m.start(),m.end(),after))
            incorporated=False
        rec.update(status='already_incorporated' if incorporated else 'applied',reason=d['reason'],en_before=' || '.join(self.en[a:b] for a,b,c in out),en_after=' || '.join(c for a,b,c in out))
        return rec,out

def build(frplan=None):
    frplan=frplan or json.loads((OUT/'FR_CORRECTION_PLAN.json').read_text())
    units={};records=[];edits=[]
    manual=json.loads((OUT/'EN_TRANSFER_DECISIONS.json').read_text()) if (OUT/'EN_TRANSFER_DECISIONS.json').exists() else {}
    for e in frplan['edits']:
        u=units.setdefault(e['unit'],None)
        if u is None:u=units[e['unit']]=AlignedUnit(e['unit'])
        assert u.fr[e['start']:e['end']]==e['before'],e
        rec,candidate=u.project(e);candidates=[candidate] if candidate else []
        decisions=[manual[sid] for sid in e['sources'] if sid in manual]
        if decisions and (rec['status']=='review' or any(d.get('override_math') for d in decisions)):
            d=next((d for d in decisions if 'pairs' in d),decisions[0]);rec,candidates=u.manual(e,rec,d)
        for a,b,after in candidates:
            if u.en[a:b]==after:rec.update(status='already_incorporated',reason='The matched English token already has the corrected reading.')
            else:edits.append({'unit':e['unit'],'start':a,'end':b,'before':u.en[a:b],'after':after,'sources':e['sources'],'page':page_at(u.en,a),'place':e['place'],'reason':rec['reason'],'kind':'edition_slip','fr_edit_ids':[e['id']]})
        records.append(rec)
    SCRATCH.mkdir(parents=True,exist_ok=True)
    (SCRATCH/'transfer_provisional.json').write_text(json.dumps({'edits':edits,'rows':records},ensure_ascii=False,indent=2)+'\n')
    counts=collections.Counter(r['status'] for r in records)
    print(json.dumps(dict(counts),indent=2))
    return {'edits':edits,'rows':records,'counts':dict(counts)}
if __name__=='__main__':build()
