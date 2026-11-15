#!/usr/bin/env python3
"""Extract the supplied primary PDFs for exact theorem-number checks.

Run from the parent directory containing sources/ and POLES/. The full
copyrighted source extracts are working files, not included in the deliverable.
"""
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[2]
items={
 'hatcher':'papers/Hatcher_AT/AT.pdf',
 'minimal':'papers/Cisinski2004_minimal/CTGDC_2004__45_2_109_0.pdf',
 'thomason':'papers/Thomason1980_CatModel/CTGDC_1980__21_3_305_0.pdf',
}
for name, relative in items.items():
    src=root/'sources'/relative
    dst=root/'POLES/research'/f'root_{name}.txt'
    subprocess.run(['pdftotext','-layout',str(src),str(dst)],check=True)
    print(name, 'extracted', dst.stat().st_size, 'bytes')
