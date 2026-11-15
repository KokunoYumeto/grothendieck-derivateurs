"""Fetch and inventory the explicitly identified recent primary reference.

The PDF is kept in scratch, not redistributed with the deliverable.  This records
the successful alternate reader when the browser's arXiv PDF endpoint failed.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request

root = Path(__file__).resolve().parents[1]
pdf = root.parent / 'tmp' / 'f_putzstuck2026.pdf'
url = 'https://arxiv.org/pdf/2608.06104'
if not pdf.exists():
    pdf.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=45) as response:
        pdf.write_bytes(response.read())
output = pdf.with_suffix('.txt')
subprocess.run(['pdftotext', '-layout', str(pdf), str(output)], check=True)
text = output.read_text()
checks = {
    'url': url,
    'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'bytes': pdf.stat().st_size,
    'page_count': text.count('\f'),
    'has_theorem_1_1': 'Theorem 1.1.' in text,
    'has_corollary_1_2': 'Corollary 1.2.' in text,
    'has_theorem_1_4': 'Theorem 1.4.' in text,
    'mentions_conjecture_3_12': 'Conjecture 3.12' in text,
    'mentions_conjecture_9_1': 'Conjecture 9.1' in text,
    'reading_note': 'All seven pages read. The paper proves tensor-nilpotence and Bousfield-lattice cardinality results. It does not decide homological representability of loc(HFp). String checks are inventory only, not proof verification.',
}
(root / 'code' / 'f_recent_reference_check_output.json').write_text(json.dumps(checks, indent=2) + '\n')
print(json.dumps(checks, indent=2))
