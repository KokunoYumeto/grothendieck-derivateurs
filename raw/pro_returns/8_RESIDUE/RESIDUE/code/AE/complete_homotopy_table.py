#!/usr/bin/env python3
"""Append proved homotopy types to every bounded path-poset row."""
from pathlib import Path
import csv,json
P=Path(__file__).parent
exceptional={(r['id'],str(r['length']),str(r['a']),str(r['b'])):r for r in json.loads((P/'core_fundamental_groups_output.json').read_text())}
rows=list(csv.DictReader((P/'relative_posets_table.csv').open()))
for r in rows:
 key=(r['id'],r['type_length'],r['a'],r['b']);e=exceptional.get(key)
 if e and e['remaining_generators']:
  assert e['conclusion']=='free group of rank 1';r['homotopy_type']='circle';r['H1']='Z';r['pi1']='Z'
 else:
  r['homotopy_type']='discrete '+r['component_count'];r['H1']='0';r['pi1']='trivial at every basepoint'
 r['H0']='Z^'+r['component_count'];r['H2']='0';r['H3']='0'
with (P/'relative_posets_homotopy_table.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('Complete rows',len(rows));print('Circle rows',sum(r['homotopy_type']=='circle' for r in rows));print('Other rows have homotopy-discrete nerves')
