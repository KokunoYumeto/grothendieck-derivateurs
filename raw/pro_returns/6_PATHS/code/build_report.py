#!/usr/bin/env python3
"""Assemble the complete, standalone research report."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
text=(root/'research/ROOT_report.md').read_text()
parts=[('A_report.md','Detailed record: total categories and the small-index obstruction'),
       ('B_report.md','Detailed record: localization and coherent path comparison'),
       ('D_report.md','Detailed record: rectification and enhancement')]
for filename,title in parts:
    part=(root/'research'/filename).read_text()
    part=re.sub(r'^# [^\n]+\n','',part,count=1)
    part=re.sub(r'(?m)^(#{2,5}) ',r'#\1 ',part)
    text+='\n\n## '+title+'\n\n'+part.strip()+'\n'
(root/'PATHS_report.md').write_text(text)
print('Wrote PATHS_report.md;',len(text.split()),'words;',len(text.encode()),'UTF-8 bytes.')
