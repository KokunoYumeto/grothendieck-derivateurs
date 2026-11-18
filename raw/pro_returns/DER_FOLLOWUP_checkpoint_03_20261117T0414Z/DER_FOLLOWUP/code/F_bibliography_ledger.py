#!/usr/bin/env python3
"""Build the one-line access ledger from the annotated bibliography.

Brace parsing preserves the actual source notes; no access status is inferred
from another paper's citation to the source.
"""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]

def braced(text,start):
    assert text[start]=='{'
    depth=1;i=start+1
    while depth:
        if text[i]=='{' and (i==0 or text[i-1]!='\\'):depth+=1
        if text[i]=='}' and (i==0 or text[i-1]!='\\'):depth-=1
        i+=1
    return text[start+1:i-1],i

def entries(text):
    result=[];pos=0
    while (m:=re.search(r'@(\w+)\s*\{\s*([^,]+),',text[pos:])):
        begin=pos+m.start();endstart=pos+m.end()
        body,end=braced(text,begin+text[begin:].index('{'))
        key=body.split(',',1)[0].strip();body=body.split(',',1)[1]
        fields={};p=0
        while (f:=re.search(r'\b(\w+)\s*=\s*',body[p:])):
            fname=f.group(1).lower();vstart=p+f.end()
            if body[vstart]=='{':value,p=braced(body,vstart)
            elif body[vstart]=='"':
                p=body.index('"',vstart+1)+1;value=body[vstart+1:p-1]
            else:
                q=body.find(',',vstart);p=len(body) if q<0 else q;value=body[vstart:p].strip()
            fields[fname]=value
        result.append((key,fields));pos=end
    return result

def plain(s):
    s=s.replace('\\_','_').replace('\\&','&')
    s=s.replace('{\\infty}','∞')
    s=re.sub(r"\{?\\[\'`^\"~]\{?([A-Za-z])\}?\}?",r'\1',s)
    s=s.replace('{','').replace('}','')
    return re.sub(r'\s+',' ',s).strip().replace('|','\\|')

items=entries((ROOT/'DER_FOLLOWUP_references.bib').read_text())
lines=['# Consolidated primary and supplied-source ledger','',
 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Audit date: 17 November 2026. No priority is claimed. “Opened” means the mathematical body at the specified passages was inspected; an abstract, catalogue record, or inherited access claim is not counted. Exact attempts and proof audits are retained in the section source logs.', '',
 '| Source key | Source | Access and closest inspected statements |',
 '|---|---|---|']
checks=[]
for key,fields in items:
    note=plain(fields.get('note',''))
    assert note,('missing access note',key)
    unopened=bool(re.search(r'not (?:opened|obtained)|body (?:was )?not obtained|full text not obtained',note,re.I))
    opened=('opened' in note.lower() or 'read' in note.lower()) and not unopened
    assert opened or unopened,('unclear access status',key,note)
    title=plain(fields.get('title',key))
    year=plain(fields.get('year',''))
    author=plain(fields.get('author',''))
    label=f'{author}, *{title}*'+(f' ({year})' if year else '')
    url=fields.get('url')
    if url:label+=f' [primary route]({url})'
    lines.append(f'| `{key}` | {label} | {note} |')
    checks.append({'key':key,'access':'not opened / body not obtained' if unopened else 'opened'})
lines+=['','## Search ledgers by requested problem','',
 '| Prompt item | Exact-query and source-audit record |','|---|---|',
 '| A.3 | `notes/A_sources.md`; historical checks in `notes/F_A_source_ledger.md`. Cocycle Fraïssé structures, all-action realization, higher homotopy of theories, and open-stabilizer support were searched. |',
 '| B.2 | `notes/BE_sources.md`, `notes/B_interval_sources.md`, and `notes/F_B_general_source_ledger.md`. Searched homotopy colimits over colored words, cofinal sequences, type descent, and fixed-type/all-type hammocks. |',
 '| C.2 | `notes/CD_sources.md`. Searched strict asphericity of path endpoints, Evrard replacements, and ordinary versus strict path-fibration tests. |',
 '| D.1 | `notes/CD_sources.md` and the C-delta attempt logs. Searched free-monoid colimits over exact or semicosimplicial indices, classifying spaces, amalgams, and positive-word diagrams. |',
 '| E.2 | `notes/BE_sources.md`; independent proof audit in `notes/E_independent_audit.md`. Searched superperfect groups, acyclic complexes in dimensions two and three, truncated simplicial acts, and Kervaire. |',
 '| G.1 and G.2 | `notes/G_sources.md`. Searched weak basic localizers, finite products, homotopy Kan adjoints, and the exact Cisinski theorem chain. |',
 '| G.4 | `notes/G_sources.md`. Searched localization and infinite products, calculus of fractions, and Zhang\'s exact 2026 title; unavailable full text is recorded without theorem-level claims. |','',
 'The bibliography distinguishes repeated editions or separately audited parts. A citation here is not a claim of formal verification: the present independent programs and the externally reported Lean checks are identified separately.']
(ROOT/'notes'/'F_source_ledger.md').write_text('\n'.join(lines)+'\n')
out={'entries':len(checks),'opened':sum(x['access']=='opened' for x in checks),'not_opened_body':sum(x['access']!='opened' for x in checks),'entries_access':checks}
(ROOT/'code'/'outputs'/'F_bibliography_ledger.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='entries_access'},indent=2))
