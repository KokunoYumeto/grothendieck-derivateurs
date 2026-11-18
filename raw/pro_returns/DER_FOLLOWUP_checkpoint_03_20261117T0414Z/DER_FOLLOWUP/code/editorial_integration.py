#!/usr/bin/env python3
"""Idempotent final editorial integration; preserves the section audit fragments."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
changes=[]
p=ROOT/'sections'/'G.tex'
s=p.read_text();t=s.replace('GCisinski2006','Cisinski2006')
if t!=s:p.write_text(t);changes.append('Unified the Cisinski 2006 citation key in G.tex.')
p=ROOT/'notes'/'A_refs.bib';s=p.read_text()
extra=' Part G additionally opened Definitions 1.4.1 and 1.4.12, Proposition 3.4.25, Proposition 4.2.4, Definition 4.2.11, Theorem 4.2.15, Remark 4.2.16, and Theorem 6.1.18 with its proof.'
anchor='without an accessibility assumption.'
if extra not in s:
    assert anchor in s
    s=s.replace(anchor,anchor+extra,1);p.write_text(s)
    changes.append('Combined the A and G access notes for the same Cisinski book.')
p=ROOT/'notes'/'BEF_results.csv';s=p.read_text();t=s
for a,b in [('B:tail-example','B:DnotLOC'),('B:one-sequence','B:D1notD'),('B:all-implications','B:table'),('E:morita','E:acts'),('E:nondegenerate','E:ndcounter'),('E:total-acts','E:total')]:t=t.replace(a,b)
if t!=s:p.write_text(t);changes.append('Aligned source-register labels with actual TeX labels.')
out={'status':'passed','changes':changes,'scope':'Editorial citation/label integration only; no mathematical claim altered.'}
(ROOT/'code'/'outputs'/'editorial_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
