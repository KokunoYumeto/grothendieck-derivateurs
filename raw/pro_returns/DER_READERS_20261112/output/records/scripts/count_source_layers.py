#!/usr/bin/env python3
"""Reproduce literal-line inventories and exact control-word source counts.

No count in this program is interpreted as a semantic count of footnotes or
editorial notes. Original unit sources are read without modification.
"""
from pathlib import Path
import collections,csv,json,re

ROOT=Path(__file__).resolve().parents[3]
COMMANDS=['printedpage','msp','mspin','footnote','footnotetext','footnotemark','footnotesize']
NEEDLES={'\\printedpage':1419,'\\msp':2266,'\\footnote':1432,'\\texttt{[':818,'% [sic]':899,'% ??':20}

def comments_removed(s):
    out=[]
    for line in s.splitlines(keepends=True):
        cut=len(line)
        for i,c in enumerate(line):
            if c!='%':continue
            k=i
            while k>0 and line[k-1]=='\\':k-=1
            if (i-k)%2==0:cut=i;break
        out.append(line[:cut]+''.join('\n' if c=='\n' else ' ' for c in line[cut:]))
    return ''.join(out)

def main():
    rows=[]
    for language,root in [('FR',ROOT/'work/fr/transcription'),('EN',ROOT/'work/en/translation')]:
        files=sorted(root.rglob('*_p*.tex'));texts=[p.read_text() for p in files]
        assert len(files)==243
        rows.append({'language':language,'scope':'complete_units','measure':'files','token':'*_p*.tex','count':len(files),'supplied_fr_inventory':243 if language=='FR' else '', 'method':'Original unit files only; edition and book masters excluded.'})
        for needle,supplied in NEEDLES.items():
            count=sum(needle in line for s in texts for line in s.splitlines())
            assert count==supplied
            rows.append({'language':language,'scope':'complete_units','measure':'source_lines_containing_literal','token':needle,'count':count,'supplied_fr_inventory':supplied if language=='FR' else '', 'method':'Each (unit, source-line number) is counted once when the literal string occurs anywhere on that line; preambles and comments included. Prefixes can match longer command names.'})
        bodies=[s.split('\\begin{document}',1)[1].rsplit('\\end{document}',1)[0] for s in texts]
        for scope,parts in [('complete_units',texts),('document_body',bodies),('document_body_without_comments',[comments_removed(s) for s in bodies])]:
            counts=collections.Counter(m.group()[1:] for s in parts for m in re.finditer(r'\\(?:[A-Za-z@]+|.)',s))
            for cmd in COMMANDS:
                rows.append({'language':language,'scope':scope,'measure':'exact_control_word_occurrences','token':'\\'+cmd,'count':counts[cmd],'supplied_fr_inventory':'','method':'TeX-style lexical control-word token; full command name must match. This is a token count, not a semantic footnote or executed-macro count.'})
            for needle in NEEDLES:
                rows.append({'language':language,'scope':scope,'measure':'literal_occurrences','token':needle,'count':sum(s.count(needle) for s in parts),'supplied_fr_inventory':'','method':'Every exact literal occurrence is counted, including repeated occurrences on one line and longer names sharing the prefix.'})
    path=ROOT/'output/records/SOURCE_LAYER_COUNTS.tsv'
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['language','scope','measure','token','count','supplied_fr_inventory','method'],delimiter='\t');w.writeheader();w.writerows(rows)
    print(json.dumps({'rows':len(rows),'languages':['FR','EN'],'units_each':243,'supplied_figures_reproduced_exactly_as_matching_line_counts':True}))

if __name__=='__main__':main()
