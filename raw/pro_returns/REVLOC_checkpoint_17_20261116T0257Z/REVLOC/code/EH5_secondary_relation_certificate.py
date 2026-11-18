#!/usr/bin/env python3
"""Exact four-term R-functional; no secondary topological conclusion is coded."""
from pathlib import Path
import json
from EH5_bottom_sigma_cobar import Comodule, mono, format_key

ROOT = Path(__file__).resolve().parent
source = ROOT / 'outputs/EH5_L15_Milnor_coaction.json'
module = Comodule(json.loads(source.read_text()))
module.check()
support = {
    (module.bottom, (mono([1]), mono([8]))),
    (module.bottom, (mono([3]), mono([6]))),
    (module.bottom, (mono([0, 1]), mono([6]))),
    (module.bottom, (mono([8]), mono([1]))),
}
columns = []
for key in module.basis(1):
    terms = module.differential(key) & support
    columns.append({'column': format_key(key),
                    'supported_terms': sorted(map(format_key, terms)),
                    'parity': len(terms) % 2})
assert len(columns) == 166
assert all(row['parity'] == 0 for row in columns)
target = (module.bottom, (mono([1]), mono([8])))
assert not module.differential(target)
assert target in support
result = {
    'relation': 'Sq1 Sq8 + Sq2 Sq1 Sq6 + Sq8 Sq1 = 0',
    'bar_cycle': '[Sq1|Sq8]a7 + [Sq2 Sq1|Sq6]a7 + [Sq8|Sq1]a7',
    'convention': 'Left Milnor coaction; cobar coaction appended at right',
    'support': sorted(map(format_key, support)),
    'input': str(source.relative_to(ROOT.parent)),
    'incoming_column_count': len(columns),
    'annihilates_all_incoming_columns': True,
    'target': format_key(target),
    'target_is_cycle': True,
    'target_pairing': 1,
    'columns': columns,
    'scope': 'Algebra only. The actual Adams d2 comparison is proved separately in D.2.61.',
}
dest = ROOT / 'outputs/EH5_secondary_relation_certificate.json'
dest.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'columns'}, indent=2))
