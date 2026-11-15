"""Reproduce the local PDF text extraction used for Part F source review.

Run from the workspace root containing the extracted attached background.
The deliverable ZIP does not duplicate the user's source archive.
"""
from pathlib import Path
import subprocess

for directory, name in [('Keel1992','keel.pdf'),
                        ('Grothendieck_Esquisse','EsquisseFr.pdf'),
                        ('HatcherLochakSchneps2000','HLS.pdf')]:
    source=Path('background/papers')/directory/name
    target=Path('tmp')/f'F_{directory}.txt'
    target.parent.mkdir(exist_ok=True)
    subprocess.run(['pdftotext','-layout',str(source),str(target)],check=True)
    data=target.read_text(errors='replace')
    controls=sum(ord(c)<32 and c not in '\n\r\t\f' for c in data)
    print(f'{source}: {len(data)} text characters; {controls} unexpected control characters')
    if controls:
        print('  Extraction is corrupted; no mathematical assertion is based on this extracted text.')
