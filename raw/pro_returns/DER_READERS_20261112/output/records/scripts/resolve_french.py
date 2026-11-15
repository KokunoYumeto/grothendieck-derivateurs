#!/usr/bin/env python3
"""Resolve source correction records to exact, reversible French unit edits.

Run from the build workspace. Input paths are ZIP-relative under work/fr.
No source file is changed by this program. Exact source offsets refer to Python
Unicode strings, and every emitted before string is checked against the input.
"""
from pathlib import Path
import csv,json,re,collections,difflib,sys,hashlib

ROOT=Path('work/fr')
WORK=Path('work/corrections_fr')
OUT=Path('output/records')
DECISION_INPUTS=Path(__file__).resolve().parents[1]/'decisions'/'source'/'french'
WORK.mkdir(parents=True,exist_ok=True)
OUT.mkdir(parents=True,exist_ok=True)

def unescape(s):
    # CSV records escape TeX command slashes twice. Unit TeX has one slash.
    s=s.replace('\\\\','\\').replace('’',"'").replace('‘',"'").replace('′',"'").replace('″',"''").replace('\u00a0',' ')
    return re.sub(r"([A-Za-z0-9)])\\prime",r"\1'",s)

def strip_qualifier(s):
    s=s.strip()
    s=re.sub(r'^Intended[^:;]{0,70}:\s*','',s,flags=re.I)
    s=re.sub(r'^Intended\s+','',s,flags=re.I)
    s=re.sub(r'\s*\[(?:intended|retain|products over e)[^\]]*\]\s*$','',s,flags=re.I)
    s=re.sub(r'\s*\((?:intended|the intended|keep|kept|retained|under the appropriate|roman C retained)[^)]*\)\s*\.?$','',s,flags=re.I)
    s=re.split(r';\s*(?:keep|retain|the editors|editors|the proof|u/i has|the replacement|there are|at \$)',s,flags=re.I)[0]
    s=re.sub(r'\s*for the standard presheaf-variance mate.*$','',s)
    s=re.split(r',\s*(?:agreement with|negation|it is|uv is|the functor|the object|footnote)',s)[0]
    s=re.sub(r'\s+intended$','',s)
    return s.strip().removesuffix('.')

def candidates(r):
    a,b,e=map(unescape,(r['transcription_reads'],r['should_read'],r['evidence']))
    ans=[]
    if a!=b:
        # A literal arrow in a prose replacement records the small edit itself.
        m=re.match(r'^(.+?)\s+->\s+(.+?)(?:,\s|\s+\(|$)',b)
        if m: return [(m[1].strip(),m[2].strip(),'explicit replacement arrow')]
        if b.startswith('Intended') or not re.match(r'^(Keep|Retain|Preserve|Interpret|Use |Read |Add |Specify|Require|For |Permit|The |They |All-|Nonemptiness|Normalize)',b,re.I):
            bb=strip_qualifier(b)
            if a.rstrip().endswith('.') and b.rstrip().endswith('.') and not bb.endswith('.'):bb+='.'
            if a!=bb:ans.append((a,bb,'replacement column'))
        for pat in [r'(?:grammatical form|standard spelling|normalized spelling|normalized form|normalized agreement|normalized adverb|intended|correct reference is|the intended functor is)\s*:?\s*(.+?)(?:;|\s+\(|\s+\[|$)',r'\(kept; (?:intended|standard spelling) (.+?)\)']:
            m=re.search(pat,b,re.I)
            if m:
                bb=m[1].strip().removesuffix('.')
                while bb.endswith(')') and bb.count(')')>bb.count('('):bb=bb[:-1]
                while bb.endswith(']') and bb.count(']')>bb.count('['):bb=bb[:-1]
                if bb and a!=bb:
                    aa=a
                    if ' ' not in bb and '\\' not in bb and ' ' in a:
                        words=re.findall(r"[A-Za-zÀ-ÿ]+",a)
                        closest=sorted(words,key=lambda w:difflib.SequenceMatcher(None,w,bb).ratio(),reverse=True)
                        if closest and difflib.SequenceMatcher(None,closest[0],bb).ratio()>.5:aa=closest[0]
                    ans.append((aa,bb,'intended reading in replacement column'))
    if a==b or re.match(r'^(Keep|Retain|Preserve)',b,re.I):
        m=re.search(r'mathematical/linguistic interpretation:\s*(.+?)(?:\.\s|\.\s*$|$)',e,re.I)
        if m:ans.append((a,m[1].strip(),'intended reading in evidence'))
        # These extract a quoted lexical correction; the source occurrence must
        # still match exactly and be located uniquely in the cited context.
        for pat in [r'(?:standard spelling|standard French|grammatically|intended noun is|intended word is|standard plural|standard agreement|standard form)\s+(?:is |would be |is \'|should be \'|is ")?([^.;]+)',r"(?:word is|adjective should be|intended verb is|Agreement should be)\s+['\"]([^'\"]+)['\"]"]:
            m=re.search(pat,e,re.I)
            if m:
                bb=m[1].strip(" '\"")
                bb=re.sub(r' would be expected.*$','',bb)
                if len(bb)<100 and a!=bb:
                    aa=a
                    if ' ' not in bb and '\\' not in bb and ' ' in a:
                        words=re.findall(r"[A-Za-zÀ-ÿ]+",a)
                        closest=sorted(words,key=lambda w:difflib.SequenceMatcher(None,w,bb).ratio(),reverse=True)
                        if closest and difflib.SequenceMatcher(None,closest[0],bb).ratio()>.5:aa=closest[0]
                    ans.append((aa,bb,'lexical correction in evidence'))
    # Recover a copied line's full sic comment when the CSV excerpt was truncated.
    if '% [sic]' in a or (len(a)>100 and b.startswith('Preserve printed edition reading')):
        prefix=a.split('% [sic]')[0].strip()[:100]
        for u in parts.get(r['part'],[]):
            tt=units[u]
            if prefix and prefix in tt:
                ix=tt.index(prefix);line=tt[ix:tt.find('\n',ix) if '\n' in tt[ix:] else len(tt)]
                if '% [sic]' in line:a=line
    # Long copied source lines commonly carry an exact correction in a sic note.
    sicpairs=[]
    for m in re.finditer(r'%?\s*\[sic\]\s*(.+?)\s*(?:->|→)\s*(.+?)(?:,|;|\s*\(|$)',a):
        aa,bb=m[1].strip(),m[2].strip()
        if ' ' not in bb and '\\' not in bb and ' ' in aa:
            words=re.findall(r"[A-Za-zÀ-ÿ]+",aa)
            closest=sorted(words,key=lambda w:difflib.SequenceMatcher(None,w,bb).ratio(),reverse=True)
            if closest and difflib.SequenceMatcher(None,closest[0],bb).ratio()>.5:aa=closest[0]
        sicpairs.append((aa,bb,'Exact source sic correction associated with this record.'))
    if sicpairs and b.startswith('Preserve printed edition reading'):
        r['all_pairs_auto']=True
        return sicpairs
    ans=sicpairs+ans
    return list(dict.fromkeys(ans))

def canon(s, withmap=False, compact=False, aliases=None, depth=0):
    """Spelling/spacing search key, with a character-to-source-offset map.

    The removed characters are TeX grouping, text-style wrappers, math delimiters
    and spacing commands only. This key is used for locating; source strings are
    emitted byte-for-byte and no global text normalization is performed.
    """
    out=[]; pos=[]
    patt=re.compile(r'%[^\n]*|\\(?:textit|textbf|textrm|textsf|textmd|emph)\b|\\(?:left|right|bigl|bigr|big|Big|biggl|biggr)\b|\\(?:,|;|!|\s)|\\(?:quad|qquad|enspace|thinspace)\b|[{}$~]')
    i=0
    while i<len(s):
        if aliases and depth<5 and s[i]=='\\':
            mm=re.match(r'\\[A-Za-z]+',s[i:])
            if mm and mm[0] in aliases:
                ex=canon(aliases[mm[0]],compact=compact,aliases=aliases,depth=depth+1)
                out.extend(ex);pos.extend([(i,i+len(mm[0]))]*len(ex));i+=len(mm[0]);continue
        if s[i].isspace():
            j=i+1
            while j<len(s) and s[j].isspace():j+=1
            if not compact and (not out or out[-1]!=' '):out.append(' ');pos.append((i,j))
            i=j;continue
        m=patt.match(s,i)
        if m:i=m.end();continue
        ch=s[i]
        ch={'’':"'",'‘':"'",'′':"'",'‐':'-','–':'-','−':'-','\u00a0':' '}.get(ch,ch)
        # \prime in the records is rendered by a literal prime in many units.
        if s.startswith('\\prime',i):out.append("'");pos.append((i,i+6));i+=6;continue
        # x^{\prime} and x' render the same script; handle only the prime caret.
        if ch=='^' and re.match(r'\^\{?\\prime\}?',s[i:]):i+=1;continue
        out.append(ch);pos.append((i,i+1));i+=1
    return (''.join(out),pos) if withmap else ''.join(out)

units={str(p.relative_to(ROOT/'transcription')):p.read_text() for p in (ROOT/'transcription').rglob('*_p*.tex')}
byname={Path(k).name:k for k in units}
parts={}
for p in (ROOT/'corrected_french_20261111').glob('DER_*.tex'):
    names=re.findall(r'% ---- from (\S+)',p.read_text())
    names=[n.replace('der1_','Der-ChI-234_') for n in names]
    parts[p.stem]=list(dict.fromkeys(byname[n] for n in names if n in byname))

def brace_end(t,start):
    depth=0
    for i in range(start,len(t)):
        if t[i]=='{' and (i==0 or t[i-1]!='\\'):depth+=1
        elif t[i]=='}' and (i==0 or t[i-1]!='\\'):
            depth-=1
            if depth==0:return i+1
    return len(t)

aliases_by_unit={}
for u,t in units.items():
    head=t[:t.find('\\begin{document}')]
    dd={}
    for mm in re.finditer(r'\\(?:newcommand|renewcommand|providecommand)\*?\s*(?:\{(\\[A-Za-z]+)\}|(\\[A-Za-z]+))\s*(?:\[(\d+)\])?\s*\{',head):
        if mm[3] and mm[3]!='0':continue
        end=brace_end(head,mm.end()-1)
        val=head[mm.end():end-1]
        key=mm[1] or mm[2]
        if key not in val and '#' not in val and len(val)<120:dd[key]=val
    aliases_by_unit[u]=dd

protected={}
for u,t in units.items():
    ranges=[]
    for m in re.finditer(r'\\(?:msp|printedpage)\{',t):
        ranges.append((m.start(),brace_end(t,m.end()-1),'page anchor'))
    # This source unit's edbr wrapper is defined as textup{texttt{#1}};
    # it carries the same editorial layer as a literal texttt bracket.
    editorial_open=r'\\(?:texttt|edbr)\{\['
    body_start=t.find('\\begin{document}')+len('\\begin{document}')
    active=re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),t)
    for m in re.finditer(editorial_open,active[body_start:]):
        # A macro definition in the preamble can intentionally contain only
        # an opening bracket. It is not an editorial note spanning the body.
        start=body_start+m.start();end=body_start+m.end()
        depth=1;j=end
        while j<len(t) and depth:
            if t[j]=='[':depth+=1
            elif t[j]==']':depth-=1
            j+=1
        ranges.append((start,j,'editors note'))
    for cmd,val in aliases_by_unit[u].items():
        if '\\texttt{[' in val and val.count('[')>val.count(']'):
            for m in re.finditer(re.escape(cmd)+r'(?![A-Za-z])',t[t.find('\\begin{document}'):]):
                start=t.find('\\begin{document}')+m.start();j=t.find('\\begin{document}')+m.end();depth=1
                while j<len(t) and depth:
                    if t[j]=='[':depth+=1
                    elif t[j]==']':depth-=1
                    j+=1
                ranges.append((start,j,'editors note'))
    protected[u]=ranges

def number(s):
    m=re.search(r'\d+',s)
    return int(m.group()) if m else None

regions={}
carry={}
for u in sorted(units):
    t=units[u]
    beg=t.find('\\begin{document}')+len('\\begin{document}')
    marks=list(re.finditer(r'\\(?:msp|printedpage)\{([^}\n]+)\}',t[beg:]))
    ms=carry.get(str(Path(u).parent));pp=None; rr=[];last=beg
    for m in marks:
        k=beg+m.start()
        if k>last:rr.append((last,k,ms,pp))
        if m.group().startswith('\\msp'):ms=number(m[1])
        else:pp=number(m[1])
        last=k
    rr.append((last,len(t),ms,pp));regions[u]=rr
    carry[str(Path(u).parent)]=ms

def locate_context(r):
    place=r['place'];scope=parts[r['part']]
    ms=re.search(r'\b(?:ms\.?\s*(?:p\.?\s*)?|manuscript\s*(?:p\.?\s*)?)(\d+)',place,re.I)
    pp=re.search(r'(?:printed|edition)\s*(?:pp?\.?\s*)?(\d+)',place,re.I)
    if not pp:pp=re.search(r'\(\s*(?:edition|printed)\s*(\d+)',r['pdf_page'],re.I)
    ms=int(ms[1]) if ms else None;pp=int(pp[1]) if pp else None
    return scope,ms,pp

canon_units={u:canon(t,True) for u,t in units.items()}
compact_units={u:canon(t,True,True) for u,t in units.items()}
alias_units={u:canon(t,True,True,aliases_by_unit[u]) for u,t in units.items()}

def find_pair(r,a,b, compact=False, expand=False):
    if not a or a==b:return []
    if not r.get('manual_pair') and len(a)>150 and len(b)<len(a)/3:return []
    if not r.get('manual_pair') and len(a.split())>=4 and len(b.split())<len(a.split())/2 and not any(c in a+b for c in ['\\','$','{','}']):return []
    # Never insert the English record's metatext into French prose.
    forbidden=r"(?<!\\)\b(?:intended|printed|retain|retained|Keep|kept|equivalently|equivalent|coefficient|the|with|requires|convention|target|source|instead|where|ordinary|unqualified|same|mathematically|ambient|category|wording|correct|probably|restriction|condition|hypothesis|unchanged|editorial|unmatched|closing|parenthesis|containing|contained|comparison|which|whose|from|assuming|finite|only|after|should|must|being|relative|original|base|component|projection|is|of|and|for|since|as|all|would|distinct|repeated|grammatical|traditional|typographical|typographic|excluding|footnote|needed|error|refers|label|intention|right|every|commuting|successor|span|consistent|notation|word|or|use|this|role|accent|reference|cross-reference|preserve|typing|participle|gender|side|exponent|conclusion|nonempty|discrete|enumeration|actor|class|list|syntax|approximately|feminine|plural|transition|constant Y-diagrams|left|in|because|from|then|approximately|idiomatically|term|opfibred|weakly|stronger|nontrivial|arbitrary|canonical|object|suffices)\b"
    if not r.get('manual_pair') and re.search(forbidden,b,re.I):return []
    if not r.get('manual_pair') and ('->' in b or '...' in b or '…' in b):return []
    scope,ms,pp=locate_context(r)
    ca=canon(a,compact=compact)
    if not ca:return []
    hits=[]
    for u in scope:
        t=units[u]; ct,mp=(alias_units[u] if expand else compact_units[u] if compact else canon_units[u])
        ca=canon(a,compact=compact,aliases=aliases_by_unit[u] if expand else None)
        for m in re.finditer(re.escape(ca),ct):
            lo=mp[m.start()][0];hi=mp[m.end()-1][1]
            if lo<t.find('\\begin{document}'):continue
            # A cited word cannot be the proper prefix of a different word.
            if a and a[0].isalpha() and lo>0 and t[lo-1].isalpha():continue
            if a and a[-1].isalpha() and hi<len(t) and t[hi].isalpha():continue
            reg=next((rr for rr in regions[u] if rr[0]<=lo<rr[1]),None)
            is_protected=any(x[0]<=lo<x[1] for x in protected[u])
            score=0 if is_protected else 1000
            if ms is not None and reg:
                if reg[2]==ms:score+=100
                elif reg[2] is not None and abs(reg[2]-ms)<=2:score+=30-abs(reg[2]-ms)
            if pp is not None and reg and pp==reg[3]:score+=80
            ca_compact=canon(a,compact=True,aliases=aliases_by_unit[u] if expand else None)
            cb_compact=canon(b,compact=True,aliases=aliases_by_unit[u] if expand else None)
            if ca_compact==cb_compact and re.sub(r'\s+','',a)!=re.sub(r'\s+','',b):
                olo,ohi=lo,hi
                bal=t[lo:hi].count('{')-t[lo:hi].count('}')
                while bal>0 and hi<len(t) and t[hi]=='}':hi+=1;bal-=1
                rawnew=b.strip('$')
                old=t[lo:hi]
                if not bal and rawnew.count('{')==rawnew.count('}') and old.count('$')%2==rawnew.count('$')%2:
                    hits.append(dict(unit=u,start=lo,end=hi,before=old,after=rawnew,score=score,ms=reg[2] if reg else None,printed_page=reg[3] if reg else None))
                continue
            # The source and the record may use different whitespace and math
            # delimiters. Locate the changed interval in their search keys and
            # retain every unchanged source character outside that interval.
            cb,bmap=canon(b,True,compact,aliases_by_unit[u] if expand else None)
            pre=0
            while pre<min(len(ca),len(cb)) and ca[pre]==cb[pre]:pre+=1
            suf=0
            while suf<min(len(ca)-pre,len(cb)-pre) and ca[-suf-1]==cb[-suf-1]:suf+=1
            # Expand only inside actual alphabetic words. The search key
            # removes spacing, so key-character adjacency alone is insufficient.
            while pre>0 and pre<len(ca) and pre<len(cb):
                sp=mp[m.start()+pre][0];bp=bmap[pre][0]
                if sp>0 and bp>0 and t[sp-1].isalpha() and t[sp].isalpha() and b[bp-1].isalpha() and b[bp].isalpha():pre-=1
                else:break
            if pre>0 and ca[pre-1]=='\\':pre-=1
            while suf>0 and suf<len(ca) and suf<len(cb):
                sp=mp[m.end()-suf][0];bp=bmap[len(cb)-suf][0]
                if sp>0 and bp>0 and t[sp-1].isalpha() and t[sp].isalpha() and b[bp-1].isalpha() and b[bp].isalpha():suf-=1
                else:break
            # An expanded alias remains a single source token.
            while pre>0 and ((pre<len(ca) and mp[m.start()+pre]==mp[m.start()+pre-1]) or (pre<len(cb) and bmap[pre]==bmap[pre-1])):pre-=1
            while suf>0 and ((suf<len(ca) and mp[m.end()-suf-1]==mp[m.end()-suf]) or (suf<len(cb) and bmap[len(cb)-suf-1]==bmap[len(cb)-suf])):suf-=1
            # Keep each TeX control sequence indivisible.
            while pre>0:
                sp=mp[m.start()+pre][0] if pre<len(ca) else mp[m.end()-1][1]
                bp=bmap[pre][0] if pre<len(cb) else len(b)
                if re.search(r'\\[A-Za-z]*$',t[:sp]) or re.search(r'\\[A-Za-z]*$',b[:bp]):pre-=1
                else:break
            while suf>0:
                sp=mp[m.end()-suf-1][1] if len(ca)>suf else mp[m.start()][0]
                bp=bmap[len(cb)-suf-1][1] if len(cb)>suf else 0
                if (sp<len(t) and t[sp].isalpha() and re.search(r'\\[A-Za-z]*$',t[:sp])) or (bp<len(b) and b[bp].isalpha() and re.search(r'\\[A-Za-z]*$',b[:bp])):suf-=1
                else:break
            aend=len(ca)-suf;bend=len(cb)-suf
            # Boundary insertion belongs between the exact neighboring tokens.
            lo=mp[m.start()+pre][0] if pre<len(ca) else mp[m.end()-1][1]
            hi=mp[m.start()+aend-1][1] if aend>pre else lo
            blo=bmap[pre][0] if pre<len(cb) else len(b)
            bhi=bmap[bend-1][1] if bend>pre else blo
            old=t[lo:hi];new=b[blo:bhi]
            # Include closing groups omitted by the location key where needed.
            for which in ('source','target'):
                ss,st,en=(t,lo,hi) if which=='source' else (b,blo,bhi)
                seg=ss[st:en]
                balance=seg.count('{')-seg.count('}')
                while balance>0 and en<len(ss) and ss[en]=='}':en+=1;balance-=1
                while balance<0 and st>0 and ss[st-1]=='{':st-=1;balance+=1
                if which=='source':lo,hi=st,en;old=ss[st:en]
                else:blo,bhi=st,en;new=ss[st:en]
            if old.count('{')!=old.count('}') or new.count('{')!=new.count('}'):continue
            if old.count('$')%2 != new.count('$')%2:continue
            if not r.get('manual_pair') and old.count('$')!=new.count('$'):continue
            if old==new:continue
            hits.append(dict(unit=u,start=lo,end=hi,before=old,after=new,score=score,ms=reg[2] if reg else None,printed_page=reg[3] if reg else None))
    if not hits:
        if not compact and '\\' in a:return find_pair(r,a,b,True)
        if compact and not expand and '\\' in a:return find_pair(r,a,b,True,True)
        return []
    highest=max(h['score'] for h in hits)
    hits=[h for h in hits if h['score']==highest]
    # With a unique phrase in the specified part, the row supplies sufficient
    # context. Multiple occurrences need a manuscript or edition page match.
    if len(hits)>1 and highest%1000<80:return []
    if len(hits)>1 and not r.get('all_matches'):return []
    return hits

def main():
    rows=[]
    for p in sorted((ROOT/'companion_corrections').glob('*.csv')):
        part=p.stem.removesuffix('_corrections')
        for n,r in enumerate(csv.DictReader(p.open()),1):
            if r['kind']=='edition_slip_kept':rows.append(dict(id=f'{part}:{n}',part=part,row=n,**r))
    # Preserve the reviewed inputs in the deliverable. The packaged copies
    # also allow replay when only the original ZIPs and records are present.
    input_dir=WORK if (WORK/'manual.json').exists() else DECISION_INPUTS
    input_paths=([input_dir/'manual.json'] if (input_dir/'manual.json').exists() else [])+sorted(input_dir.glob('manual_*.json'))
    assert input_paths,'No reviewed French decision fixtures were found.'
    DECISION_INPUTS.mkdir(parents=True,exist_ok=True)
    manual={};fixture_manifest=[]
    for mpth in input_paths:
        data=mpth.read_bytes();manual.update(json.loads(data))
        if mpth.parent!=DECISION_INPUTS:(DECISION_INPUTS/mpth.name).write_bytes(data)
        fixture_manifest.append({'file':mpth.name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
    (DECISION_INPUTS/'MANIFEST.json').write_text(json.dumps(fixture_manifest,ensure_ascii=False,indent=2)+'\n')
    edits=[];result=[];unresolved=[]
    for r in rows:
        rr=dict(r); rr['status']='unresolved';rr['edit_ids']=[];rr['reason']=''
        m=manual.get(r['id'])
        if m:r['manual_pair']=True
        if m and m.get('decision_note'):rr['decision_note']=m['decision_note']
        if m and m.get('all_matches'):r['all_matches']=True
        if m and 'status' in m:
            rr.update(m);result.append(rr);continue
        opts=m.get('pairs',[]) if m else candidates(r)
        fallback_reason='Apply the amendment identified in the supplied correction record, checked against the exact local source text. Evidence recorded in the source table: '+r['evidence']
        found=[];missing_pairs=[];why=(m.get('reason') or fallback_reason) if m else fallback_reason
        for pair in opts:
            a,b=pair[:2];why=(pair[2] if len(pair)>2 and pair[2] else None) or (m.get('reason') if m else None) or fallback_reason
            hits=find_pair(r,a,b)
            if hits:
                found.extend(dict(h,reason=why) for h in hits)
                if not ((m and m.get('all_pairs')) or r.get('all_pairs_auto')):break
            elif (m and m.get('all_pairs')) or r.get('all_pairs_auto'):missing_pairs.append([a,b])
        if m and m.get('edits'):
            found=[dict(x,reason=x.get('reason') or m.get('reason') or fallback_reason,printed_page=x.get('page',''),ms=x.get('ms')) for x in m['edits']]
            missing_pairs=[]
        component_failures=[]
        if found:
            for h in found:
                assert units[h['unit']][h['start']:h['end']]==h['before'], (r['id'],h)
                assert h['before']!=h['after'], (r['id'],'identity variant')
                protected_hit=None
                for x in protected[h['unit']]:
                    if h['start']==h['end']==x[0]:continue
                    if x[0]<=h['start']<x[1] or h['start']<=x[0]<h['end']:
                        literal=units[h['unit']][x[0]:x[1]]
                        if h['start']<=x[0] and h['end']>=x[1] and h['before'].count(literal)==h['after'].count(literal):continue
                        protected_hit=x;break
                if protected_hit:
                    rr['status']='rejected';rr['reason']='The mapped change alters an '+protected_hit[2]+'. The reader instructions require this source layer to remain verbatim; the proposed amendment is therefore recorded without changing it.'
                    component_failures.append(dict(h,failure=rr['reason']))
                    continue
                h['sources']=[r['id']];h['place']=r['place'];h['page']=str(h.pop('printed_page'));h.pop('score',None)
                if h['page'] in ('','None'):
                    marks=re.findall(r'\\printedpage\{([^}]+)\}',units[h['unit']][:h['start']])
                    h['page']=marks[-1] if marks else r['pdf_page']
                h['evidence']=r['evidence'];h['id']='pending'
                duplicate=next((e for e in edits if all(e[k]==h[k] for k in ['unit','start','end','before','after'])),None)
                if duplicate:
                    
                    if r['id'] not in duplicate['sources']:duplicate['sources'].append(r['id'])
                    rr['status']='merged';rr['edit_ids'].append(duplicate['id']);rr['reason']='Same source place and correction as '+duplicate['sources'][0]
                elif any(edits_overlap(e,h) for e in edits):
                    rr['reason']='Overlapping edit requires reconciliation.'
                    component_failures.append(dict(h,failure=rr['reason']))
                else:
                    h['id']=f'FRV{len(edits)+1:04d}';edits.append(h);rr['status']='applied';rr['edit_ids'].append(h['id']);rr['reason']=h.get('reason',why)
        if component_failures:
            rr['unmapped_components']=component_failures
            if rr['edit_ids']:
                rr['status']='partial';rr['reason']='Some requested components conflict with another edit or a protected source span; all failed components are recorded.'
            elif any('Overlapping' in h['failure'] for h in component_failures):
                rr['status']='unresolved'
        if missing_pairs and rr['edit_ids']:
            rr['status']='partial';rr['reason']='Some explicitly requested correction components remain unmapped.';rr['missing_pairs']=missing_pairs
        if rr['status'] in ('unresolved','partial'):
            rr['candidates']=opts;unresolved.append(rr)
        result.append(rr)
    # Verify source identity and non-overlap; these are actual mapped variants.
    for i,e in enumerate(edits):
        assert units[e['unit']][e['start']:e['end']]==e['before']
        assert e['before']!=e['after']
        assert not any(edits_overlap(e,h) for h in edits[:i]),('overlap',e['id'])
    plan={'offset_convention':'Python Unicode character offsets in original unit files','edits':edits,'rows':result,'counts':dict(collections.Counter(r['status'] for r in result))}
    (OUT/'FR_CORRECTION_PLAN.json.tmp').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
    (OUT/'FR_CORRECTION_PLAN.json.tmp').replace(OUT/'FR_CORRECTION_PLAN.json')
    (WORK/'unresolved.json').write_text(json.dumps(unresolved,ensure_ascii=False,indent=2))
    with (OUT/'FR_CORRECTION_COVERAGE.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['id','status','edit_ids','reason'],delimiter='\t');w.writeheader()
        for r in result:w.writerow({k:(';'.join(r[k]) if isinstance(r[k],list) else r[k]) for k in w.fieldnames})
    with (OUT/'CORRECTIONS_DECIDED.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['decision_id','source_row','decision','page','place','printed_reading','proposed_reading','reason'],delimiter='\t');w.writeheader()
        n=0
        for r in result:
            if r['status'] in ('rejected','no_change') or r.get('decision_note'):
                n+=1;w.writerow(dict(decision_id=f'FRD{n:04d}',source_row=r['id'],decision=r['status'] if not r.get('decision_note') else 'applied_with_decision',page=r['pdf_page'],place=r['place'],printed_reading=r['transcription_reads'],proposed_reading=r['should_read'],reason=r.get('decision_note',r['reason'])))
    print(json.dumps({'edits':len(edits),'rows':len(result),'counts':plan['counts']},ensure_ascii=False))

def edits_overlap(a,b):
    if a['unit']!=b['unit']:return False
    if a['start']==a['end'] and b['start']==b['end']:
        return a['start']==b['start']
    if a['start']==a['end']:
        return b['start']<=a['start']<b['end']
    if b['start']==b['end']:
        return a['start']<=b['start']<a['end']
    return a['start']<b['end'] and b['start']<a['end']

if __name__=='__main__':main()
