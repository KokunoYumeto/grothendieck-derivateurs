"""Put the independently written Part F blocks in mathematical order.
This script is idempotent and records the statement ids found.
"""
from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / 'sections' / 'F.tex'
text = p.read_text()
start = text.index(r'\subsection{Plus construction and acyclic nullification}')
end_marker = r'\begin{claim}{F.2}'
if start < text.index(end_marker):
    end = text.index(end_marker)
    inserted = text[start:end]
    text = text[:start] + text[end:] + '\n' + inserted
text = text.replace('FLawson2020', 'FLawson2019')
p.write_text(text)
print('Statement order:', ', '.join(re.findall(r'\\begin\{claim\}\{(F\.\d+)\}',text)))
