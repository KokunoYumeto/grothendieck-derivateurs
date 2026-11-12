"""Compare regenerated outputs with the shipped ones: text files modulo CR/LF, JSON files parsed."""
import json, sys
from pathlib import Path
R = Path(sys.argv[1])
pairs = [
 ('out/akr_stages.out','shipped/akr_stages.out'),
 ('out/akr_stages_triple.out','shipped/akr_stages_triple.out'),
 ('out/akr_stages_literal.out','shipped/akr_stages_literal.out'),
 ('out/akr_stages_triple_literal.out','shipped/akr_stages_triple_literal.out'),
 ('out/akr_component_checks.out','shipped/akr_component_checks.out'),
 ('out/akr_stages_critical.out','shipped/akr_stages_critical.out'),
 ('code/akr_stages_output.json','shipped/akr_stages_output.json'),
 ('code/akr_stages_triple_output.json','shipped/akr_stages_triple_output.json'),
 ('code/akr_stages_literal_output.json','shipped/akr_stages_literal_output.json'),
 ('code/akr_stages_triple_literal_output.json','shipped/akr_stages_triple_literal_output.json'),
 ('code/akr_stages_critical_output.json','shipped/akr_stages_critical_output.json'),
 ('code/examples_colored_words.out','shipped/examples_colored_words.out'),
 ('code/examples_support_orbits.out','shipped/examples_support_orbits.out'),
 ('code/outputs/basic_shape_checks.json','shipped/outputs/basic_shape_checks.json'),
 ('code/outputs/semisimplicial_affine_checks.out','shipped/outputs/semisimplicial_affine_checks.out'),
 ('out/main_sign_reflection_check.json','shipped/outputs/main_sign_reflection_check.json'),
 ('out/main_counterexample.out','shipped/pretot_audit/outputs/main_counterexample.out'),
 ('out/independent_certificate_audit.out','shipped/pretot_audit/outputs/independent_certificate_audit.out'),
 ('code/pretot_audit/outputs/main_counterexample_data.json','shipped/pretot_audit/outputs/main_counterexample_data.json'),
 ('code/pretot_audit/outputs/projectivity_certificate.json','shipped/pretot_audit/outputs/projectivity_certificate.json'),
 ('code/pretot_audit/outputs/semisimplicial_affine_checks.out','shipped/pretot_audit/outputs/semisimplicial_affine_checks.out'),
]
for a, b in pairs:
    A, B = (R/a).read_bytes(), (R/b).read_bytes()
    if a.endswith('.json'):
        try:
            same = json.loads(A) == json.loads(B); how = 'parsed JSON'
        except Exception:
            same = A.replace(b'\r\n', b'\n') == B.replace(b'\r\n', b'\n'); how = 'text'
    else:
        same = A.replace(b'\r\n', b'\n').rstrip() == B.replace(b'\r\n', b'\n').rstrip(); how = 'text mod CRLF'
    print(('IDENTICAL' if same else 'DIFFERENT'), f'({how})', a)
