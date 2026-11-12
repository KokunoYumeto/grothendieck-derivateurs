#!/usr/bin/env python3
"""Build all reader forms from two self-contained, annotated LuaLaTeX masters.

Inputs are the three supplied ZIPs, extracted as work/fr, work/en, work/comp.
All decisions are exact-offset edits against verified original unit strings.
The emitted masters contain a Lua data table below \\endinput.  Each unit holds
its source hash, variants and the three generated projections.  DERform=0/1/2
selects diplomatic/apparatus/reading.  emit_master() reads that same table's
JSON representation; it never edits the projections independently.
"""
from __future__ import annotations
import argparse, ast, collections, csv, difflib, hashlib, json, re, sys
from pathlib import Path
import reader_support as S

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'work'
OUT=ROOT/'output'
RECORDS=OUT/'records'
BD=r'\begin{document}'
ED=r'\end{document}'
FORMS=['diplomatic','apparatus','reading']
NAMES={
 'FR':['DER_FR_diplomatique','DER_FR_corrige_apparat','DER_FR_texte_de_lecture'],
 'EN':['DER_EN_diplomatic','DER_EN_corrected_apparatus','DER_EN_reading'],
}
MARGIN_LABEL_PLACEMENTS=[
 dict(id='BUILD-MARGIN-FR-XV-58',language='FR',unit='Der-ChXV-05-11-10/Der-ChXV-05-11-10_p056-060.tex',command='printedpage',argument='58',horizontal_shift_pt=6,
      observed_pdf='DER_FR_texte_de_lecture',observed_physical_page=603,observed_pdf_sha256='688e48b970216c6b8d0187a9bdb07608d894238ac54ccf351bef21b69d752d9c',
      reason='Move the edition label right of the author comma after W(1,2,3,6,7,8); retain the exact anchor call and body in all three forms.'),
 dict(id='BUILD-MARGIN-EN-XIIb-152',language='EN',unit='Der-ChXIIb-012/Der-ChXIIb-012_p061-065.tex',command='msp',argument='page 152',horizontal_shift_pt=20,
      observed_pdf='DER_EN_diplomatic',observed_physical_page=438,observed_pdf_sha256='c173784fcbe138d28bb1c6d4770730793b6899c25a1214beb2f0f0487558018c',
      reason='Move the manuscript label right of the final X_0 and punctuation in the smoothness equivalence; retain the exact anchor call and body in all three forms.'),
]
EMAIL=re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}')
LOCAL=re.compile(r'(?:[A-Za-z]:[\\/](?:Users|home)[\\/][^\s\n"<>]+|/(?:Users|home|root|workspace|tmp|opt|usr|var)/[^\s\n"<>]+)')
PP=re.compile(r'\\(printedpage|msp|mspin)\s*\{')
TEX_ESCAPE={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$','&':r'\&','#':r'\#','_':r'\_','%':r'\%','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}

def clean(s):
    return LOCAL.sub('[local path removed]',EMAIL.sub('[e-mail address removed]',s))

def tx(s,breaks=False):
    chunks=[]
    for c in str(s):
        token=r'\space{}' if breaks and c=='\n' else TEX_ESCAPE.get(c,c)
        if breaks and c in '\\{}_()[]/,;:=^.$&\n':token+=r'\allowbreak{}'
        if breaks and c==' ':token=r'\allowbreak{} '+token[1:]
        chunks.append(token)
    return ''.join(chunks)

def write_tsv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader()
        for r in rows:w.writerow({k:clean(str(v)) if not isinstance(v,(list,dict)) else clean(json.dumps(v,ensure_ascii=False)) for k,v in r.items()})

def file_order():
    s=(WORK/'fr/transcription/LesDerivateurs_transcription.tex').read_text()
    return [Path(x).parts[0] for x in re.findall(r'\\input\{([^}]+)\}',s)]

def chapter_title(folder,lang):
    if folder=='dertbmt':return 'Table des matières de l’édition' if lang=='FR' else 'The edition’s table of contents'
    m=re.search(r'Ch(XIIapp|[IVX]+[abc]?)',folder)
    if m:num=m.group(1)
    else:num={'der-ch16':'XVI','der-ch17':'XVII','der-ch18':'XVIII','der-ch19':'XIX'}[folder]
    if num.startswith('XII'):
        num={'XIIa':'XII, 1–4','XIIb':'XII, 5','XIIc':'XII, 6','XIIapp':'XII, appendice' if lang=='FR' else 'XII, appendix'}.get(num,num)
    return ('Chapitre ' if lang=='FR' else 'Chapter ')+num

def anchor_list(s):
    vals=[]
    for m in PP.finditer(s):
        e=S.brace_end(s,m.end()-1);vals.append((m.group(1),s[m.end():e-1]))
    return vals

def part_page(s,pos):
    vals=[m for m in re.finditer(r'\\printedpage\{([^}]+)\}',s[:pos])]
    return vals[-1].group(1) if vals else 'front matter'

def body_split(s):
    a=s.index(BD);b=s.rindex(ED)
    return s[:a],s[a+len(BD):b]

def patch_exact(s,edits):
    last=0
    for e in sorted(edits,key=lambda x:(x['start'],x['end'])):
        assert e['start']>=last,('overlapping edits',e['id'])
        assert s[e['start']:e['end']]==e['before'],('stale edit',e['id'])
        assert e['before']!=e['after'],('identity variant',e['id'])
        last=e['end']
    for e in sorted(edits,key=lambda x:x['start'],reverse=True):s=s[:e['start']]+e['after']+s[e['end']:]
    return s

def known_repairs(s,rel):
    events=[]
    before=r'\mathbf{\Delta}';after=r'\boldsymbol{\Delta}'
    for m in re.finditer(re.escape(before),s):
        events.append(dict(page=part_page(s,m.start()),place=rel+'; bold capital Delta encoding',before=before,after=after,source='BUILD-FONT-DELTA; conventions/TYPESETTING.csv:2; companion_corrections/DER_I-a_corrections.csv:1'))
    s=s.replace(before,after)
    if rel.endswith('Der-ChXIIc-30-03-03_p061-064.tex'):
        before=r'baseline=(\tikzcdmatrixname-2-1.base)'
        after=r'baseline=(\tikzcdmatrixname-2-2.base)'
        # Only the first diagram has an empty cell at (2,1). The English fixed
        # unit supplies the corrected baseline; the later diagram remains (2,1).
        if s.count(before)==2:
            pos=s.index(before);s=s[:pos]+after+s[pos+len(before):]
            events.append(dict(page='XIIc 61–64',place=rel,before=before,after=after,source='BUILD-FIX-XIIc; checks/FIXES.jsonl'))
    return s,events

def editors_front(body,lang,reading=False):
    contents_phrase=(r'\textsc{Note}. Dans cette table de matières' if lang=='FR' else r'\textsc{Note}. In this table of contents')
    note_at=body.find(contents_phrase)
    if note_at>=0:
        a=body.rfind(r'{\footnotesize',0,note_at);assert a>=0
        b=S.brace_end(body,a)
        separator=re.search(r'\\bigskip\s*\\noindent\s*\\rule\{4cm\}\{0\.4pt\}\s*$',body[:a])
        aa=separator.start() if separator else a
        if reading:
            return body[:aa]+body[b:],[dict(kind='editorial_contents_note',before=body[aa:b],after='')]
        label='Note des éditeurs de l’édition transcrite' if lang=='FR' else 'Note by the editors of the transcribed edition'
        return body[:a]+r'\par\noindent\textbf{'+label+r'.}\par'+'\n'+body[a:],[]
    needle='Ce texte a été déchiffré' if lang=='FR' else 'This text was deciphered'
    a=body.find(needle)
    if a<0:
        # Some English units use the present perfect.
        if lang=='EN':
            m=re.search(r'This text (?:has been|was) deciphered',body);a=m.start() if m else -1
    if a<0:return body,[]
    sig=re.search(r'G\.(?:~|\s|\\\s)*Maltsiniotis',body[a:])
    # The initial credit names the editor too; the signature is the last name
    # before the first numbered edition page.
    numeric=re.search(r'\\printedpage\{[^}]*\d[^}]*\}',body[a:])
    stop=a+numeric.start() if numeric else len(body)
    hits=list(re.finditer(r'G\.(?:~|\s|\\\s)*Maltsiniotis',body[a:stop]))
    if not hits:raise ValueError('Missing editorial signature')
    b=a+hits[-1].end()
    # Keep wrappers (center/flushright etc.) balanced by replacing prose only.
    before=body[a:b]
    if reading:
        # Structural wrappers within the removed prose have to disappear with
        # their partners. Expand to the entire page bounded by page breaks.
        left=list(S.PAGEBREAK.finditer(body,0,a));aa=left[-1].end() if left else a
        right=S.PAGEBREAK.search(body,b);bb=right.start() if right else b
        chunk=body[aa:bb]
        anchors='\n'.join(m.group(0) for m in re.finditer(r'\\printedpage\{[^}]*\}',chunk))
        return body[:aa]+anchors+'\n'+body[bb:],[dict(kind='editorial_front_note',before=chunk,after=anchors)]
    label='Note des éditeurs de l’édition transcrite' if lang=='FR' else 'Note by the editors of the transcribed edition'
    return body[:a]+r'\par\noindent\textbf{'+label+r'.}\par'+'\n'+body[a:],[]

def texttt_groups(s):
    groups=[]
    active=re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),s)
    for m in re.finditer(r'\\(?:texttt|edbr)\s*\{',active):
        e=S.brace_end(s,m.end()-1)
        groups.append(dict(a=m.start(),b=e,inner_a=m.end(),inner_b=e-1,t=s[m.end():e-1]))
    return groups

def editorial_sections(body,rel,lang,reading=False):
    """Handle explicitly attributed editorial prose outside bracketed notes."""
    if not reading:return body,[]
    events=[]
    if rel.startswith('Der-ChXIV-07-10-10/'):
        heading=r'\section*{Postface des éditeurs}' if lang=='FR' else r"\section*{Editors' afterword}"
        a=body.find(heading)
        if rel.endswith('_p011-011.tex'):a=0
        if a>=0:
            before=body[a:];retained=[]
            for m in PP.finditer(before):
                end=S.brace_end(before,m.end()-1);retained.append(before[m.start():end])
            after='\n'.join(retained)+'\n'
            events.append(dict(kind='editorial_afterword',before=before,after=after))
            body=body[:a]+after
    if rel=='Der-ChVI-345/Der-ChVI-345_p121-125.tex':
        # At manuscript pp.197–198 two triangles share one seven-column
        # matrix. The first three cells of BOTH rows are Grothendieck's
        # diagram; the editor's alternative occupies columns four to seven.
        # A contiguous bracket span would wrongly consume the author’s
        # second row. Project the exact first three source cells of each row.
        pattern=r'(\\begin\{tikzcd\}\[column sep=small\])([\s\S]*?)(\\end\{tikzcd\})'
        candidates=[m for m in re.finditer(pattern,body) if r'\texttt{[Plutôt' in m.group() or r'\texttt{[Rather' in m.group()]
        assert len(candidates)==1,(lang,rel,'interleaved diagram')
        m=candidates[0];rows=m.group(2).split(r'\\')
        assert len(rows)==2 and all(len(row.split('&'))==7 for row in rows)
        projected=r'\\'.join('&'.join(row.split('&')[:3]) for row in rows)
        after=m.group(1)+projected+'\n'+m.group(3)
        events.append(dict(kind='interleaved_editorial_diagram',before=m.group(),after=after))
        body=body[:m.start()]+after+body[m.end():]
    selected=[]
    for m in re.finditer(r'\\footnote(?:\[[^\]]*\])?\s*\{',body):
        end=S.brace_end(body,m.end()-1);inner=body[m.end():end-1]
        if not re.search(r'N\.(?:~|\s)*Éd\.|Ed\.(?:~|\s)*note\.',inner[:70]):continue
        a=m.start();b=end;after='';kind='signed_editorial_footnote'
        if rel=='der-ch18/der-ch18_p046-050.tex':
            # The editors explicitly quote two of Grothendieck's marginal
            # annotations. Keep those exact author words, including the
            # marginal corollary, while removing only editorial framing.
            if lang=='FR':qa=inner.index('“');qb=inner.index('”',qa+1)+1;head=r'\textbf{Corollaire.}'
            else:qa=inner.index('``');qb=inner.index("''",qa+2)+2;head=r'\textbf{Corollary.}'
            ca=inner.index(head)
            after=m.group()+inner[qa:qb]+r'\par'+'\n'+inner[ca:]+'}'
            kind='editorial_framing_author_quotes_retained'
        else:
            if '[' not in m.group():after=r'\stepcounter{footnote}'
            if a>0 and body[a-1]==',':a-=1
            elif a>0 and b<len(body) and body[a-1]=='(' and body[b]==')':a-=1;b+=1
        selected.append(dict(a=a,b=b,kind=kind,before=body[a:b],after=after))
    for n in reversed(selected):body=body[:n['a']]+n['after']+body[n['b']:]
    events+=selected
    return body,events

def finish_editor_structure(s,a,b):
    """Include only closing syntax for structures opened inside an editor note.

    Some notes put their closing printed bracket inside the final cell of an
    array or diagram. Its end-array, right delimiter and end-display still
    belong to that note, and must leave the reading projection with it.
    """
    active=re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),s)
    stack=[];braces=0;inline=False;display=0;paren=0
    pat=r'\\(?:begin|end)\{[^}]+\}|\\\[|\\\]|\\\(|\\\)|\\[A-Za-z@]+|\\.|[{}$]'
    for m in re.finditer(pat,active[a:b]):
        tok=m.group()
        if tok.startswith(r'\begin{'):stack.append(tok[7:-1])
        elif tok.startswith(r'\end{'):
            if stack and stack[-1]==tok[5:-1]:stack.pop()
        elif tok==r'\[':display+=1
        elif tok==r'\]':display-=1
        elif tok==r'\(':paren+=1
        elif tok==r'\)':paren-=1
        elif tok=='{':braces+=1
        elif tok=='}':braces-=1
        elif tok=='$':inline=not inline
    while stack or braces>0 or display>0 or paren>0 or inline:
        p=b
        while p<len(active) and active[p].isspace():p+=1
        rest=active[p:]
        if stack and rest.startswith(r'\end{'+stack[-1]+'}'):
            token=r'\end{'+stack.pop()+'}';b=p+len(token);continue
        m=re.match(r'\\right\s*(?:\\[{}]|[.()\[\]|])',rest)
        if m:b=p+m.end();continue
        if braces>0 and rest.startswith('}'):braces-=1;b=p+1;continue
        if display>0 and rest.startswith(r'\]'):display-=1;b=p+2;continue
        if paren>0 and rest.startswith(r'\)'):paren-=1;b=p+2;continue
        if inline and rest.startswith('$'):inline=False;b=p+1;continue
        break
    return b

def editor_notes(body,lang,reading=False,rel=None):
    """Locate paired typewriter brackets, including notes split around math.

    The note macro \\pl occurs in one unit and is expanded from that unit's
    documented literal definition. The \\edbr wrapper in XVIII is parsed by
    its original argument boundaries. Original units remain intact in the master.
    """
    pl='plutôt' if lang=='FR' else 'rather'
    pl_replacement=r'\texttt{['+pl+'}'
    pl_starts=set();delta=0
    for m in re.finditer(r'\\pl(?![A-Za-z])',body):
        pl_starts.add(m.start()+delta);delta+=len(pl_replacement)-len(m.group())
    expanded=re.sub(r'\\pl(?![A-Za-z])',lambda m:pl_replacement,body)
    gs=texttt_groups(expanded);notes=[];active=None;level=0
    special=[]
    for m in re.finditer(re.escape(r'\texttt{['+pl+'}'),expanded):
        if m.start() not in pl_starts:continue
        eol=expanded.find('\n',m.end());eol=len(expanded) if eol<0 else eol
        comment=re.search(r'(?<!\\)%',expanded[m.end():eol])
        if comment:eol=m.end()+comment.start()
        j=expanded.find(']',m.end(),eol)
        if j>=0 and not any(g['inner_a']<=j<g['inner_b'] for g in gs):
            special.append(dict(a=m.start(),b=j+1,before=expanded[m.start():j+1],kind='editorial_note',neutral=False))
    for g in gs:
        if any(n['a']<=g['a']<n['b'] for n in special):continue
        for i,c in enumerate(g['t']):
            if c=='[':
                if active is None:active=g
                level+=1
            elif c==']' and active is not None:
                level-=1
                if level==0:
                    a=active['a'];b=g['b'];raw=expanded[a:b]
                    # A manuscript page repeated in running text is an anchor,
                    # not a word to be retained in the plain running text.
                    page=bool(re.fullmatch(r'\\texttt\{\[page\s+[^\]]+\]\}',raw))
                    missing=bool(re.search(r'illisible|illégible|illegible|unreadable|manque|missing|mot\(s\).*illisible',raw,re.I))
                    notes.append(dict(a=a,b=b,before=raw,kind='inline_page_duplicate' if page else 'editorial_note',neutral=missing))
                    active=None
    if active is not None:
        # The special \\pl in a diagram cell closes with a plain bracket.
        # This is processed below from the source-delimited line only.
        pass
    # Standalone \\pl notes with a plain ']' in a text box have no final texttt.
    covered=[(n['a'],n['b']) for n in notes]
    for m in re.finditer(re.escape(r'\texttt{['+pl+'}'),expanded):
        if any(a<=m.start()<b for a,b in covered):continue
        if m.start() not in pl_starts:continue
        endline=expanded.find('\n',m.end());endline=len(expanded) if endline<0 else endline
        comment=re.search(r'(?<!\\)%',expanded[m.end():endline])
        if comment:endline=m.end()+comment.start()
        j=expanded.find(']',m.end(),endline)
        if j>=0:
            notes.append(dict(a=m.start(),b=j+1,before=expanded[m.start():j+1],kind='editorial_note',neutral=False))
    notes+=special
    # The edition's own front note defines a question mark in square brackets
    # as editorial uncertainty about the preceding word. Several such marks
    # lack a texttt wrapper; DER_XVIII-b:49 independently confirms this usage.
    active=re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),expanded)
    for m in re.finditer(r'\[(?:\s|\\[,;:! ]|~)*\?(?:\s|\\[,;:! ]|~)*\]',active):
        notes.append(dict(a=m.start(),b=m.end(),before=expanded[m.start():m.end()],kind='plain_editorial_doubt',neutral=False))
    notes.sort(key=lambda n:n['a'])
    # A nested texttt bracket is part of the containing note.
    merged=[]
    for n in notes:
        if merged and n['a']<merged[-1]['b']:continue
        n['b']=finish_editor_structure(expanded,n['a'],n['b'])
        n['before']=expanded[n['a']:n['b']]
        merged.append(n)
    if not reading:return body,merged
    for n in reversed(merged):
        replacement=r'\DERlacuna{}' if n['neutral'] else ''
        # VI ms160 opens an editorial insertion in the optional item label
        # and closes it in the first prose word: \item[\texttt{[1)}]
        # \texttt{Soit]}. Retain the item argument's own closing bracket.
        if re.search(r'\\item\[\s*$',expanded[:n['a']]) and n['before'].startswith(r'\texttt{['):
            first_end=S.brace_end(n['before'],n['before'].index('{'))
            if n['before'][first_end:].lstrip().startswith(']'):replacement=']'+replacement
        if n['kind']=='inline_page_duplicate':
            value=n['before'][len(r'\texttt{['):-2]
            # Seven inline page numbers duplicate immediately preceding
            # manuscript anchors; a page declared absent has no such anchor.
            if not re.search(r'\\msp\{'+re.escape(value)+r'\}\s*$',expanded[:n['a']]):
                if not n['neutral']:replacement=r'\DERinlinepage{'+value+'}'
        # An edition-page boundary can occur inside a long editorial note.
        # Its argument and position in the anchor sequence still belong to
        # the reader, even when the editorial prose is omitted.
        retained=[]
        for m in PP.finditer(n['before']):
            e=S.brace_end(n['before'],m.end()-1)
            retained.append(n['before'][m.start():e])
        replacement+=''.join(retained)
        n['after']=replacement
        expanded=expanded[:n['a']]+replacement+expanded[n['b']:]
    # An editorial formula can occupy an entire display. Removing its words
    # leaves blank paragraph tokens in math mode unless its empty wrapper is
    # removed too. The wrapper carries no authorial symbols.
    empty_displays=[]
    for m in re.finditer(r'\\\[\s*\\\]',expanded):
        empty_displays.append(dict(a=m.start(),b=m.end(),before=m.group(),after='',kind='editorial_display_wrapper',neutral=False))
    for n in reversed(empty_displays):expanded=expanded[:n['a']]+expanded[n['b']:]
    merged+=empty_displays
    # An editor-only footnote leaves no authorial content after its note is
    # removed. Its now-empty marker and immediately enclosing parentheses are
    # part of that editorial intervention and disappear with it.
    empty=[]
    for m in re.finditer(r'\\footnote(?:text)?(?:\[[^\]]*\])?\s*\{',expanded):
        end=S.brace_end(expanded,m.end()-1)
        if expanded[m.end():end-1].strip():continue
        a=m.start();b=end
        if a>0 and b<len(expanded) and expanded[a-1]=='(' and expanded[b]==')':a-=1;b+=1
        replacement=r'\stepcounter{footnote}' if m.group().startswith(r'\footnote{') else ''
        empty.append(dict(a=a,b=b,before=expanded[a:b],after=replacement,kind='editorial_footnote_marker',neutral=False))
    for n in reversed(empty):expanded=expanded[:n['a']]+n['after']+expanded[n['b']:]
    merged+=empty
    return expanded,merged

def boundary_marks(s,edits):
    """Attach each variant to the end of its containing complete TeX block.

    A boundary is outside braces, math, and displayed/alignment environments.
    This avoids passing a TikZ alignment through a macro argument. Every mark
    links to exactly one apparatus item, whose source locus is also explicit.
    """
    requests=[];delta=0
    bd=s.index(BD)+len(BD)
    for e in sorted(edits,key=lambda x:x['start']):
        p=e['start']+delta+len(e['after']);delta+=len(e['after'])-len(e['before'])
        requests.append((max(bd,p),e['id']))
    if not requests:return s
    # Work in the selected body; preamble variants attach at body opening.
    a=bd;b=s.rindex(ED);body=s[a:b];safe=[0];depth=0;math=False;display=False;env=[];i=0
    forbidden={'tikzcd','tikzpicture','scope','picture','pgfpicture','pgfscope','aligned','align','align*','gather','gather*','array','tabular','equation','equation*','multline','multline*','matrix','pmatrix','bmatrix','cases'}
    while i<len(body):
        c=body[i]
        if c=='%':
            j=body.find('\n',i);i=len(body) if j<0 else j;continue
        if c=='\\':
            m=re.match(r'\\(begin|end)\{([^}]+)\}',body[i:])
            if m:
                op,name=m.groups()
                if op=='begin':env.append(name)
                elif env and env[-1]==name:env.pop()
                i+=m.end();continue
            if body[i:i+2] in (r'\[',r'\]'):
                display=body[i+1]=='[';i+=2;continue
            if body[i:i+2] in (r'\(',r'\)'):
                math=body[i+1]=='(';i+=2;continue
            m=re.match(r'\\[A-Za-z@]+|\\.',body[i:]);i+=len(m.group(0)) if m else 1;continue
        if c=='{':depth+=1
        elif c=='}':depth-=1
        elif c=='$':
            if body[i:i+2]=='$$':display=not display;i+=1
            else:math=not math
        elif c=='\n' and depth==0 and not math and not display and not any(x in forbidden for x in env):
            prev=body[:i].rstrip().split('\n')[-1] if body[:i].strip() else ''
            if prev and not prev.lstrip().startswith('%') and not re.match(r'^\\(?:begin|item|section|subsection|printedpage|msp)',prev):safe.append(i)
        i+=1
    safe.append(len(body));marks=collections.defaultdict(list)
    for pos,id_ in requests:
        target=next((p for p in safe if p>=max(0,pos-a)),len(body));marks[target].append(id_)
    # A marker needs its own line: a preceding inline source comment otherwise
    # consumes it even though the TeX block itself has ended safely.
    for p,ids in sorted(marks.items(),reverse=True):body=body[:p]+'\n'+''.join(r'\DERmark{'+i+'}' for i in ids)+'\n'+body[p:]
    return s[:a]+body+s[b:]

def audit_diff(before,after,unit,source):
    # Line-level hunks preserve full contexts and are reproducible, including
    # representation changes (groups, definitions, and common page reflow).
    a=before.splitlines(keepends=True);b=after.splitlines(keepends=True);out=[]
    for op,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        if op!='equal':out.append(dict(page=part_page(before,sum(map(len,a[:i]))),place=f'{unit}; source lines {i+1}–{max(i+1,j)}',before=''.join(a[i:j]),after=''.join(b[k:l]),source=source))
    return out

def margin_placement_definition(placement):
    # A unit-scoped override changes one label's horizontal ink position only.
    # Its exact argument is compared as TeX tokens; every other argument uses
    # the existing shared macro. The original body and anchor calls are intact.
    command=placement['command'];argument=placement['argument']
    shift=str(placement['horizontal_shift_pt'])
    fallback='derpp' if command=='printedpage' else 'dermsp'
    style=(r'\raggedright\footnotesize\color{black!55}' if command=='printedpage'
           else r'\raggedright\footnotesize\ttfamily')
    label=r'p.~#1' if command=='printedpage' else '[#1]'
    return ['% Shared placement decision '+placement['id'],
            r'\def\DERmargintarget{'+argument+r'}%',
            '\\def\\'+command+r'#1{\def\DERmarginarg{#1}\ifx\DERmarginarg\DERmargintarget'
            r'\marginpar{'+style+r'\hspace*{'+shift+r'pt}'+label+r'}'
            '\\else\\'+fallback+r'{#1}\fi}%']

def build_unit(original,rel,lang,edits):
    placement=next((p for p in MARGIN_LABEL_PLACEMENTS if p['language']==lang and p['unit']==rel),None)
    if placement:
        assert anchor_list(body_split(original)[1]).count((placement['command'],placement['argument']))==1,('margin target',lang,rel)
    repaired,repair_events=known_repairs(original,rel)
    # Apply edits to original coordinates before shared repair. This ordering
    # prevents the repair from moving a subsequent source coordinate.
    corrected=patch_exact(original,edits)
    marked=boundary_marks(corrected,edits)
    corrected,_=known_repairs(corrected,rel)
    marked,_=known_repairs(marked,rel)
    docs=[repaired,marked,corrected];forms=[];notes=[];audit=[]
    for form,doc in zip(FORMS,docs):
        pre,body=body_split(doc)
        body,front=editors_front(body,lang,form=='reading')
        body,sections=editorial_sections(body,rel,lang,form=='reading')
        body,note_rows=editor_notes(body,lang,form=='reading',rel)
        if form=='reading':notes=front+sections+note_rows
        # The page number arguments remain unchanged; only placement is shared.
        body=S.PAGEBREAK.sub(r'\\par',body)
        defs=S.definitions(pre)
        if placement:defs.extend(margin_placement_definition(placement))
        # Mathtools is loaded globally. Local page macros are redirected to the
        # shared margin implementation after all local definitions.
        defs.append(r'\let\mspin\DERmspin%')
        own_fn=r'\thefootnote' in pre
        if own_fn:defs.append(r'\edef\derfnsaved{\the\value{footnote}}\setcounter{footnote}{0}%')
        head='\n'.join(defs)+'\n'
        tail=('\n'+r'\setcounter{footnote}{\derfnsaved}%' if own_fn else '')+'\n'+r'\endgroup'+'\n'
        text='% BEGIN UNIT '+rel+'\n'+head+body+tail+'% END UNIT '+rel+'\n'
        forms.append(clean(text))
        if form=='apparatus':audit=audit_diff(corrected,text,rel,'BUILD-ASSEMBLY'+('; '+placement['id'] if placement else ''))
    # Validate the exact semantic anchor sequence in every source projection.
    anchors=anchor_list(body_split(original)[1])
    for f,text in zip(FORMS,forms):
        actual=anchor_list(text)
        if actual!=anchors:raise ValueError(f'Anchor drift in {rel}, {f}: {len(anchors)} -> {len(actual)}')
    return dict(unit=rel,source_sha256=hashlib.sha256(original.encode()).hexdigest(),original_source=clean(original),variants=edits,forms=forms),notes,repair_events,audit

def preamble(lang):
    p=S.PREAMBLE
    if lang=='FR':
        p=p.replace('[french,english]{babel}','[english,french]{babel}')
        p=p.replace('Les Dérivateurs (English translation)','Les Dérivateurs (transcription française)')
        p=p.replace('English translation of the edition by','Transcription française de l’édition de')
    p=p.replace(r'\usepackage{amsmath}',r'\usepackage{amsmath}'+'\n'+r'\usepackage{mathtools}')
    # Queue adjacent margin labels together. Standard marginpars overlapped
    # beside the large Chapter II chart; the marginfix projection was checked
    # on both source languages before the complete reader rebuild.
    p=p.replace(r'\usepackage{marginnote}',r'\usepackage{marginnote}'+'\n'+r'\usepackage{marginfix}')
    # Floating margin notes separate anchors sharing a source baseline. The
    # existing reader's placement is retained; mspin is the single boxed case.
    p+=r'''
\usepackage{luacode}
\providecommand{\DERform}{0}
\newcommand{\DERmspin}[1]{\marginnote{\raggedright\scriptsize\ttfamily[#1]}}
\newcommand{\DERinlinepage}[1]{\marginpar{\raggedright\footnotesize\ttfamily[#1]}}
\newcommand{\DERlacuna}{\ifmmode\mathord{[\ldots]}\else[\ldots]\fi}
\newfontfamily\DERappfont{DejaVu Sans}[Scale=MatchLowercase]
\newfontfamily\DERcodefont{DejaVu Sans Mono}[Scale=MatchLowercase]
\DeclareRobustCommand{\DERmark}[1]{\ifmmode\text{\hyperlink{app-#1}{\textsuperscript{\sffamily\tiny[#1]}}}\else\hyperlink{app-#1}{\textsuperscript{\sffamily\tiny[#1]}}\fi\allowbreak}
\newcommand{\DERapparatusitem}[5]{\par\medskip{\DERappfont\noindent\hypertarget{app-#1}{}\textbf{#1}\quad #2\par
  {\footnotesize\noindent\textbf{Print / imprimé:}\ {\DERcodefont #3}\par
  \noindent\textbf{Correction:}\ {\DERcodefont #4}\par
  \noindent\textbf{Source:}\ #5\par}}}
'''
    return p

def front(lang,form):
    fr=lang=='FR'
    title={'FR':['Texte diplomatique','Texte corrigé avec apparat','Texte de lecture'],'EN':['Diplomatic text','Corrected text with apparatus','Plain reading text']}[lang][FORMS.index(form)]
    credits_fr=r'''\textbf{Crédits.} Auteur : Alexander Grothendieck, \emph{Les Dérivateurs} (1990–1991).
L’édition transcrite est celle de M.~Künzer, J.~Malgoire et G.~Maltsiniotis (Universités de Montpellier~II et Paris~VII).
Le déchiffrement, l’édition et les notes des éditeurs leur appartiennent.
Transcription produite par IA (\emph{AI-transcribed}) : Claude Opus~5.5 (Anthropic).
Commentaire du compagnon et corrections produits par IA (\emph{AI-produced corrections}) : GPT-6 Astra
(OpenAI, ChatGPT Pro mode), vérifiés et intégrés par Claude Opus~5.5 (Anthropic).
Huit blocs de commentaire des parties II-a, III-V et XIIb-a, sept paragraphes d’autres blocs, dix-neuf lignes du registre
des assertions (II-a, III-V, VII-c, VIII-X, XIIb-a) et trois entrées bibliographiques sont produits par Claude Fable~5.2
(Anthropic) à partir de réponses de GPT-6 Astra qu’il a examinées ; chaque ligne concernée indique réponse et examen.
Les corrections des définitions de macros et les modifications des textes vérifiés absentes des tables ont été
comparées aux pages de l’édition par Claude Opus~5.5 (\texttt{transcription/DECISIONS.md}).
Traduction anglaise produite par IA (\emph{AI-translated}) : GPT-6.1 Sol (OpenAI, effort max) ; glossaire de Claude
Fable~5.2 et Claude Opus~5.5 ; consigne, contrôles, corrections, comparaison d’intégralité et livre anglais de
Claude Opus~5.5 (Anthropic). Réponses de recherche brutes produites par GPT-6 Astra ; examens par Claude Fable~5.2.
Le présent assemblage des lecteurs, leur apparat et leur audit sont de GPT-6 Astra (OpenAI, ChatGPT Pro mode).'''
    credits_en=r'''\textbf{Credits.} Author: Alexander Grothendieck, \emph{Les Dérivateurs} (1990–1991).
The edition transcribed is the electronic edition by M.~Künzer, J.~Malgoire and G.~Maltsiniotis
(Universités de Montpellier~II et Paris~VII). The deciphering, edition and editors’ notes are theirs.
AI-transcribed by Claude Opus~5.5 (Anthropic). Companion commentary and AI-produced corrections by GPT-6 Astra
(OpenAI, ChatGPT Pro mode), checked and integrated by Claude Opus~5.5 (Anthropic).
Eight commentary blocks in II-a, III-V and XIIb-a, seven paragraphs of other blocks, nineteen rows of the claims
register (II-a, III-V, VII-c, VIII-X, XIIb-a) and three bibliography entries are AI-produced by Claude Fable~5.2
(Anthropic) from GPT-6 Astra’s answers that it reviewed; each relevant row names the answer and reviewer.
Macro-definition corrections and changes in the checked texts absent from their tables were compared against the
edition’s pages by Claude Opus~5.5 (\texttt{transcription/DECISIONS.md}).
AI-translated: translated by GPT-6.1 Sol (OpenAI, effort max). Glossary by Claude Fable~5.2 and Claude Opus~5.5;
prompt, checks, fixes, completeness comparison and the published English book by Claude Opus~5.5 (Anthropic).
Raw research answers AI-produced by GPT-6 Astra; reviews by Claude Fable~5.2.
This reader build, apparatus and audit are by GPT-6 Astra (OpenAI, ChatGPT Pro mode).'''
    rights=(WORK/'fr/repo/RIGHTS_NOTICE.md').read_text().split('---')
    rights_text=rights[1].strip() if fr else rights[0].replace('# Rights notice','').strip()
    how_fr=r'''\textbf{Lecture.} Les marques marginales \texttt{p. n} donnent les pages de l’édition ; les marques
\texttt{[page n]} donnent les pages du manuscrit. Les arguments et l’ordre des ancres sont conservés.
Les mots entre crochets en caractères de machine à écrire appartiennent aux éditeurs de l’édition transcrite.
Les points d’interrogation isolés entre crochets signalent aussi leurs doutes, selon la convention exposée dans leur préface.
Les variantes de notre apparat portent un identifiant FRV ou ENV et un lien vers le relevé final ; elles donnent
la lecture imprimée, la correction et sa source. Pour identifier sans ambiguïté les symboles et les macros propres
à chaque unité, les deux lectures de l’apparat sont citées en code \LaTeX{} exact. Les notes originales ne sont
pas réécrites. Les trois formes proviennent d’un seul maître annoté. Les réparations de composition communes
aux trois formes sont consignées séparément des variantes textuelles.'''
    how_en=r'''\textbf{Reading.} Margin marks \texttt{p. n} locate edition pages; \texttt{[page n]} locates manuscript
pages. Anchor arguments and order are retained. Typewriter words in square brackets are the original editors’
notes. Isolated question marks in square brackets also record the editors’ doubts, under the convention stated in their preface.
Our apparatus variants carry an FRV or ENV identifier linked to the final register, with the printed
reading, correction and source. To identify symbols and unit-specific macros exactly, the readings in that
register are quoted as literal \LaTeX{} source. The original notes are preserved verbatim. All three forms
come from one annotated master. Typesetting repairs common to the three forms are recorded separately from
textual variants.'''
    if form=='reading':
        how_fr=r'''\textbf{Note sur ce texte de lecture.} Ce volume donne le texte corrigé sans notre apparat et sans
les notes des éditeurs de l’édition transcrite, y compris leurs indications de passages barrés, biffés ou rayés.
La postface des éditeurs au chapitre XIV est omise. Les répertoires du chapitre XIII restent attribués aux éditeurs.
Deux citations d’annotations marginales de Grothendieck, transmises dans la note 58 du chapitre XVIII,
sont conservées dans cette note, sans le commentaire des éditeurs qui les encadre.
Les autres mots et les notes de l’auteur sont conservés. Le signe neutre $[\ldots]$ marque les emplacements où
les éditeurs signalent des mots illisibles ou du texte manquant. Les numéros des pages de l’édition et du manuscrit
figurent seulement dans la marge ; leur ordre et leurs arguments sont conservés. Les décisions et les sources
des corrections se trouvent dans le volume avec apparat et les relevés joints.'''
        how_en=r'''\textbf{Preface to the reading text.} This volume gives the corrected text without our apparatus
and without the original editors’ notes, including their reports of words or passages struck out.
The editors’ afterword to Chapter XIV is omitted. The reference sections in Chapter XIII remain credited to the editors.
Two quotations from Grothendieck’s marginal annotations, transmitted in note 58 of Chapter XVIII,
are retained in that note with the surrounding editorial commentary removed. All other
words and the author’s footnotes are retained. The neutral sign $[\ldots]$ marks places where the editors report
illegible words or missing text. Edition and manuscript page numbers appear only in the margin; their order
and arguments are retained. The apparatus volume and accompanying records provide the correction decisions
and their sources.'''
    return r'\begin{document}'+'\n'+r'''\pagestyle{plain}
\hypersetup{pageanchor=false}
\begin{titlepage}\centering\vspace*{0.16\textheight}
{\Large Alexander Grothendieck\par}\vspace{2em}
{\Huge\bfseries Les Dérivateurs\par}\vspace{2em}
{\Large '''+title+r'''\par}\vspace{1em}
{\large '''+('Français' if fr else 'English translation')+r'''\par}\vfill
{\normalsize '''+('Édition de' if fr else 'Edition by')+r''' M.~Künzer, J.~Malgoire et G.~Maltsiniotis\par}
\vspace{1em}{\small 12 '''+('novembre' if fr else 'November')+r''' 2026\par}\end{titlepage}
\hypersetup{pageanchor=true}
'''+(credits_fr if fr else credits_en)+'\n\n'+r'\medskip\noindent\url{https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html}'+'\n\n'+r'\bigskip\noindent\textbf{'+('Droits' if fr else 'Rights')+r'}\par'+'\n'+rights_text+'\n\n'+r'\clearpage'+(how_fr if fr else how_en)+'\n\n'+r'\clearpage\tableofcontents\clearpage\pagestyle{derbody}'+'\n'

def apparatus(lang,units):
    title='Apparat des corrections' if lang=='FR' else 'Apparatus of corrections'
    out=[r'\clearpage\section*{'+title+r'}\addcontentsline{toc}{section}{'+title+r'}\markboth{'+title+'}{'+title+'}\n']
    folder=None
    for u in units:
        es=u['variants']
        if not es:continue
        f=Path(u['unit']).parts[0]
        if f!=folder:
            out.append(r'\subsection*{'+tx(chapter_title(f,lang))+'}\n');folder=f
        for e in es:
            source='; '.join(e.get('sources',[]))
            where=e.get('page','')+'; '+e.get('place',u['unit'])
            out.append(r'\DERapparatusitem{'+e['id']+'}{'+tx(clean(where),True)+'}{'+tx(clean(e['before']),True)+'}{'+tx(clean(e['after']),True)+'}{'+tx(clean(source),True)+'}\n')
    return ''.join(out)

def lua_quote(s):
    # Long Lua strings retain all Unicode and exact TeX bytes.
    n=0
    while ']'+('='*n)+']' in s:n+=1
    return '['+'='*n+'['+s+']'+'='*n+']'

def write_master(lang,data):
    directory=OUT/lang;directory.mkdir(parents=True,exist_ok=True)
    name=f'DER_{lang}_annotated_master.tex'
    # The JSON block is the canonical interchange representation. A generated
    # Lua table with identical projections enables direct LuaLaTeX compilation.
    # Python validates both before emitting a reader.
    lua='return {\n'+',\n'.join('{'+','.join(lua_quote(x) for x in p)+'}' for p in data['pieces'])+'\n}\n'
    loader=r'''% DERform: 0 diplomatic; 1 corrected with apparatus; 2 plain reading.
\providecommand{\DERform}{0}
'''+preamble(lang)+r'''
\begin{luacode*}
function DERemit()
local f=assert(io.open("'''+name+r'''", "rb"))
local s=f:read("*a");f:close()
local marker="%%DER_LUA_".."PAYLOAD_BEGIN%%"
local a,b=assert(s:find("\n"..marker.."\n",1,true))
local stop="%%DER_LUA_".."PAYLOAD_END%%"
local c=assert(s:find("\n"..stop,b+1,true))
local pieces=assert(load(s:sub(b+1,c-1)))()
local form=tonumber(token.get_macro("DERform"))+1
assert(form>=1 and form<=3,"DERform must be 0, 1, or 2")
for _,p in ipairs(pieces) do
  for line in (p[form].."\n"):gmatch("([^\n]*)\n") do tex.print(line) end
end
end
\end{luacode*}
\directlua{DERemit()}
\endinput
%%DER_LUA_PAYLOAD_BEGIN%%
'''+lua+'%%DER_LUA_PAYLOAD_END%%\n%%DER_JSON_PAYLOAD_BEGIN%%\n'+json.dumps(data,ensure_ascii=False,indent=1)+'\n%%DER_JSON_PAYLOAD_END%%\n'
    path=directory/name;path.write_text(loader,encoding='utf-8')
    return path

def read_master(path):
    s=path.read_text();a=s.index('\n%%DER_JSON_PAYLOAD_BEGIN%%\n')+len('\n%%DER_JSON_PAYLOAD_BEGIN%%\n');b=s.index('\n%%DER_JSON_PAYLOAD_END%%',a)
    return json.loads(s[a:b])

def emit_master(path):
    data=read_master(path);lang=data['language']
    for i,name in enumerate(NAMES[lang]):
        txt='% Generated solely from '+path.name+': DERform='+str(i)+'\n'+preamble(lang)+''.join(p[i] for p in data['pieces'])
        (path.parent/(name+'.tex')).write_text(txt,encoding='utf-8')
    return data

def build(lang,without_variants=False):
    planpath=RECORDS/('FR_CORRECTION_PLAN.json' if lang=='FR' else 'EN_CHANGE_PLAN.json')
    plan=json.loads(planpath.read_text()) if planpath.exists() and not without_variants else {'edits':[],'status':'pending; diplomatic checkpoint only'}
    # A deliberately pending plan permits a diplomatic checkpoint only.
    edits_by_unit=collections.defaultdict(list)
    for e in plan.get('edits',[]):edits_by_unit[e['unit']].append(e)
    source=WORK/('fr/transcription' if lang=='FR' else 'en/translation')
    units=[];notes=[];changes=[];assembly=[];anchors=[];pieces=[[front(lang,f) for f in FORMS]]
    assembly.append(dict(page='reader front matter',place='shared standalone preamble',before='',after=preamble(lang),source='BUILD-SHARED-PREAMBLE'))
    assembly.append(dict(page='reader front matter',place='credits, rights, preface and contents of corrected form',before='',after=pieces[0][1],source='BUILD-FRONT-MATTER'))
    for folder in file_order():
        title=chapter_title(folder,lang)
        head=r'\clearpage\setcounter{footnote}{0}\phantomsection\addcontentsline{toc}{section}{'+tx(title)+r'}\markboth{'+tx(title)+'}{'+tx(title)+'}\n'
        pieces.append([head]*3)
        assembly.append(dict(page='chapter boundary',place=folder,before='',after=head,source='BUILD-CHAPTER-BOUNDARY'))
        for p in sorted((source/folder).glob('*_p*.tex')):
            rel=p.relative_to(source).as_posix();original=p.read_text()
            es=edits_by_unit.pop(rel,[])
            unit,note_rows,repairs,audit=build_unit(original,rel,lang,es)
            units.append(unit);pieces.append(unit['forms']);assembly+=audit;changes+=repairs
            for e in es:changes.append(dict(page=e.get('page',''),place=e.get('place',rel),before=e['before'],after=e['after'],source='; '.join(e.get('sources',[]))+'; '+e['id']))
            for j,n in enumerate(note_rows,1):notes.append(dict(language=lang,unit=rel,id=f'{rel}:N{j}',kind=n['kind'],before=n['before'],after=n.get('after',r'\DERlacuna{}' if n.get('neutral') else '')))
            aa=anchor_list(body_split(original)[1]);anchors.append(dict(language=lang,unit=rel,edition=sum(k=='printedpage' for k,v in aa),manuscript=sum(k in ('msp','mspin') for k,v in aa),sequence_sha256=hashlib.sha256(json.dumps(aa,ensure_ascii=False).encode()).hexdigest(),all_forms_match=True))
    assert not edits_by_unit,('Unknown source units',list(edits_by_unit))
    register=apparatus(lang,units)
    pieces.append(['',register,'']);pieces.append([ED+'\n']*3)
    assembly.append(dict(page='apparatus register',place='complete register emitted from the annotated variant records',before='',after=register,source='BUILD-APPARATUS-REGISTER'))
    assembly.append(dict(page='reader end',place='standalone document closure',before='',after=ED+'\n',source='BUILD-DOCUMENT-CLOSURE'))
    data=dict(format='DER annotated master 1',language=lang,source_commit='f42cfdd',variants=sum(len(u['variants']) for u in units),units=units,pieces=pieces)
    master=write_master(lang,data);emit_master(master)
    changes+=assembly
    write_tsv(RECORDS/f'CHANGES_{lang}.tsv',changes,['page','place','before','after','source'])
    write_tsv(RECORDS/f'EDITORIAL_NOTES_{lang}.tsv',notes,['language','unit','id','kind','before','after'])
    write_tsv(RECORDS/f'ANCHORS_{lang}.tsv',anchors,['language','unit','edition','manuscript','sequence_sha256','all_forms_match'])
    result={'language':lang,'units':len(units),'variants':data['variants'],'edition_anchors':sum(x['edition'] for x in anchors),'manuscript_anchors':sum(x['manuscript'] for x in anchors),'reading_omissions':len(notes),'neutral_signs':sum('\\DERlacuna' in x['after'] for x in notes),'margin_placement_decisions':sum(p['language']==lang for p in MARGIN_LABEL_PLACEMENTS),'plan_status':plan.get('status','supplied')}
    (RECORDS/f'BUILD_{lang}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--language',choices=['FR','EN','both'],default='both');ap.add_argument('--emit',type=Path);ap.add_argument('--without-variants',action='store_true');args=ap.parse_args()
    if args.emit:emit_master(args.emit);return
    for lang in (['FR','EN'] if args.language=='both' else [args.language]):build(lang,args.without_variants)
    write_tsv(RECORDS/'MARGIN_PLACEMENTS.tsv',MARGIN_LABEL_PLACEMENTS,list(MARGIN_LABEL_PLACEMENTS[0]))

if __name__=='__main__':main()
