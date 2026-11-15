"""Compare the regenerated outputs of the PRETOT programs with the shipped ones.

Usage: python -I compare_outputs.py <shipped_outputs_dir> <regenerated_outputs_dir> <report_file>
Text files are compared after line-ending normalization; JSON files are compared
as parsed objects, ignoring only the key 'runtime_seconds'.
Written by Claude Opus 5.5 for the PRETOT review, 12 Nov 2026.
"""
import json
import sys
from pathlib import Path

shipped = Path(sys.argv[1])
regen = Path(sys.argv[2])
report = Path(sys.argv[3])
NOT_REGENERATED = {'assemble_results.out', 'build_pdf.out', 'document_validation.json', 'environment.json',
                   'latex_final.out', 'latex_format_bootstrap.out', 'latex_pass_1.out', 'latex_pass_2.out',
                   'latex_pass_3.out', 'results_validation.json'}


def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if k != 'runtime_seconds'}
    if isinstance(o, list):
        return [strip(v) for v in o]
    return o


lines = []
for f in sorted(shipped.iterdir()):
    name = f.name
    if name in NOT_REGENERATED:
        lines.append(f'{name}: not regenerated (build/assembly/environment record)')
        continue
    g = regen / name
    if not g.exists():
        lines.append(f'{name}: MISSING in rerun')
        continue
    if name.endswith('.json'):
        same = strip(json.loads(f.read_text(encoding='utf-8'))) == strip(json.loads(g.read_text(encoding='utf-8')))
        lines.append(f'{name}: {"identical (parsed JSON, runtime ignored)" if same else "DIFFERENT"}')
    else:
        a = f.read_text(encoding='utf-8').replace('\r\n', '\n')
        b = g.read_text(encoding='utf-8').replace('\r\n', '\n')
        if a == b:
            lines.append(f'{name}: identical')
        else:
            al, bl = a.splitlines(), b.splitlines()
            diff = [(i, x, y) for i, (x, y) in enumerate(zip(al, bl)) if x != y]
            lines.append(f'{name}: DIFFERENT ({len(diff)} differing lines of {len(al)}/{len(bl)})')
            for i, x, y in diff[:6]:
                lines.append(f'    line {i + 1}: shipped: {x[:150]}')
                lines.append(f'    line {i + 1}: rerun  : {y[:150]}')
extra = sorted(set(p.name for p in regen.iterdir()) - set(p.name for p in shipped.iterdir()))
lines.append(f'files produced by the rerun and not shipped: {extra}')
report.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
