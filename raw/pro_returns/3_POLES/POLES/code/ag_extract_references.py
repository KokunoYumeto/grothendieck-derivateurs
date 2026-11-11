"""Reproduce primary-source text and page-image inspections for Parts A/G.

The supplied papers remain user source files. Full extracted copyrighted texts
and page images are intermediate research material, excluded from deliverables.
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'POLES' / 'research'
jobs = [
    ('sources/papers/Cisinski_Ast308/smf_ast_308.pdf', 'ag_cisinski308.txt'),
    ('sources/papers/Cisinski1999_Dwyer/CTGDC_1999__40_3_227_0.pdf', 'ag_dwyer.txt'),
    ('sources/papers/Brown1973/1973.0186.pdf', 'ag_brown.txt'),
]
for source, target in jobs:
    subprocess.run(['pdftotext','-layout',str(ROOT/source),str(OUT/target)],check=True)
    print('Extracted',source,'to',target,'bytes', (OUT/target).stat().st_size)
renders = [
    ('sources/papers/Brown1973/1973.0186.pdf',10,'ag_brown_428'),
    ('sources/grothendieck/DER_XIIc-b/DER_XIIc-b_pages.pdf',34,'ag_xii273'),
]
for source, page, target in renders:
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','2000',
                    '-singlefile','-png',str(ROOT/source),str(OUT/target)],check=True)
    print('Rendered',source,'PDF page',page,'to',target+'.png')
print('Brown is a scan; page-image inspection, not the near-empty text extraction, verified the cited lemmas.')
