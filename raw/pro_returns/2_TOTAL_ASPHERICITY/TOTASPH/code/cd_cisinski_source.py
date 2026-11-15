"""Check the supplied published primary source; text cache stays outside deliverables."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[2]
cache = root / 'source_followup'
cache.mkdir(exist_ok=True)
pdf = root / 'background' / 'papers' / 'Cisinski_Ast308' / 'smf_ast_308.pdf'
text = cache / 'Cisinski2006_published.txt'
subprocess.run(['pdftotext', '-layout', str(pdf), str(text)], check=True)
content = text.read_text()
for marker in ['Corollaire 9.2.15.', 'Proposition 9.2.17.']:
    assert marker in content, marker
    print('Verified printed marker:', marker)
print('Primary PDF:', pdf.relative_to(root))
print('PDF bytes:', pdf.stat().st_size)
print('Text cache:', text.name)
print('Previous remote 40MB scan retrieval stopped; supplied published PDF used instead.')
print('Source cache excluded from deliverables.')
