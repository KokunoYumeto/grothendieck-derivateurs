"""Extract the supplied PDF sources used in BISITE Parts D and G."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[2]
items = {
    'HA': 'background/papers/Lurie_HA/HA.pdf',
    'HTT': 'background/papers/Lurie_HTT/HTT.pdf',
    'Jansen': 'background/papers/2308.09551/2308.09551v2.pdf',
}
out = root / 'research' / 'dg'
out.mkdir(parents=True, exist_ok=True)
lines=[]
for name, rel in items.items():
    target=out / (name+'.txt')
    subprocess.run(['pdftotext','-layout',str(root/rel),str(target)],check=True)
    lines.append(f'{name}: {len(target.read_text().splitlines())} extracted lines from {rel}')
log=root/'BISITE/code/dg_extract_sources.out.txt'
log.write_text('\n'.join(lines)+'\n')
print(log.read_text())
