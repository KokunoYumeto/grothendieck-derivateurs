"""Reproduce extraction and plain-text indexing of the supplied source archive."""
from pathlib import Path
import zipfile, hashlib, subprocess, json
ROOT=Path(__file__).resolve().parents[2]
archive=ROOT/'upload/1_CATHOT_background.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='e91871632a2a856d47e993341ba56763c2bf1f8244a3c3442711ccb2a20a4c39'
base=ROOT/'background'
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        assert (base/entry.filename).resolve().is_relative_to(base.resolve())
    z.extractall(base)
output=[]
for p in sorted((base/'papers').rglob('*.pdf')):
    out=p.with_suffix('.txt')
    proc=subprocess.run(['pdftotext','-layout',str(p),str(out)],capture_output=True,text=True)
    output.append({'file':str(p.relative_to(base)),'returncode':proc.returncode,'characters':len(out.read_text(errors='replace')) if out.exists() else 0,'stderr':proc.stderr})
print(json.dumps(output,indent=2))
