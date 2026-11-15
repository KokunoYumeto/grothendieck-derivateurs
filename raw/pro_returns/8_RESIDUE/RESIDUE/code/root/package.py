"""Validate completed evidence, create checksums, and package one research ZIP.

This validates the recorded computations and document consistency. It does not
claim to machine-check the paper's mathematical proofs.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re
import zipfile

from assemble import claims

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
TOP_FILES = {
    'README.md', 'RESIDUE_paper.tex', 'RESIDUE_paper.pdf', 'RESIDUE_paper.bbl',
    'RESIDUE_results.csv', 'RESIDUE_references.bib', 'RESIDUE_report.md'
}
EXCLUDED_NAMES = {'monoids', 'dwyer_kan_read.txt', 'jansen_extract.txt'}


def read_json(relative):
    return json.loads((ROOT / relative).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def included_files():
    paths = []
    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if '__pycache__' in relative.parts or path.name in EXCLUDED_NAMES:
            continue
        if relative.parts[0] in {'code', 'sections', 'tables'} or str(relative) in TOP_FILES:
            paths.append(path)
    return sorted(paths)


def main():
    rows = list(csv.DictReader((ROOT / 'RESIDUE_results.csv').open()))
    expected_columns = ['id','statement','status','where_proved','depends_on',
                        'manuscript_rows_or_pages_settled','notes']
    assert list(rows[0]) == expected_columns
    source_rows = []
    for letter in 'ABCDEFGHIJ':
        source_rows.extend(claims((ROOT / f'sections/{letter}.tex').read_text()))
    assert [(r['id'], r['status']) for r in rows] == [(r[1], r[2]) for r in source_rows]
    assert len({r['id'] for r in rows}) == len(rows)
    assembly = read_json('code/root/assembly_output.json')
    assert assembly['statements'] == len(rows)
    assert assembly['statuses'] == dict(Counter(r['status'] for r in rows))
    assert all(r['status'] in {'Proved','Refuted','Known','Open'} for r in rows)
    assert assembly['citation_keys_resolved']
    build = read_json('code/root/pdf_build.json')
    assert build['returncode'] == 0 and build['pdf_exists']
    assert not build['tex_error_lines'] and not build['undefined_control_sequence']
    assert not build['undefined_citations'] and build['overfull_boxes'] == 0
    assert build['missing_characters'] == 0
    quality = read_json('code/root/pdf_quality_output.json')
    visual = read_json('code/root/pdf_visual_audit.json')
    assert quality['pdf_sha256'] == sha(ROOT / 'RESIDUE_paper.pdf')
    assert visual['pdf_sha256'] == quality['pdf_sha256']
    assert quality['all_pages_rendered'] and quality['all_fonts_embedded']
    assert not quality['empty_pages'] and not quality['words_outside_page_safety_bound']
    assert visual['all_pages_visually_inspected'] and visual['unresolved_layout_defects'] == []
    provenance = read_json('code/root/input_provenance.json')
    assert provenance['status'] == 'PASS' and provenance['manifest_members'] == 431
    assert not provenance['hash_and_size_failures']
    posets = read_json('code/GHIJ/poset_direct_image_summary_max5.json')
    assert not posets['failures']
    assert posets['totals'] == {'monotone_maps': 1349916, 'proper_maps': 96372,
                                'stalk_coefficient_tests': 5536094}
    ae = read_json('code/AE/verification_output.json')
    assert ae['verified_beat_certificates'] == 5313
    monoids = read_json('code/AE/monoids_classification.json')['summary']
    assert monoids['monoid_isomorphism_classes'] == 273
    assert len(monoids['non_1_types']) == 1
    table = list(csv.DictReader((ROOT / 'tables/D_BISITE_B15.csv').open()))
    assert len(table) == 8
    historical = list(csv.DictReader((ROOT / 'sections/BC_historical_audit.csv').open()))
    assert len(historical) == 36
    required_evidence = [
        'code/BC/verification_output.json', 'code/root/D_output.json',
        'code/root/F_output.json', 'code/root/coverings_output.json',
        'code/AE/relative_posets_certificates.json',
        'code/AE/relative_posets_homotopy_table.csv',
        'code/AE/core_fundamental_groups_output.json',
        'code/GHIJ/marked_curve_lifts.csv',
        'code/GHIJ/marked_curve_presentations.json',
        'code/GHIJ/small_counterexamples.json'
    ]
    assert all((ROOT / name).is_file() for name in required_evidence)
    validation = {
        'status': 'PASS', 'statements': len(rows), 'statuses': assembly['statuses'],
        'bibliography_records': assembly['bibliography_records'],
        'pdf_pages': quality['page_count'], 'pdf_sha256': quality['pdf_sha256'],
        'register_matches_source': True, 'all_citation_keys_resolved': True,
        'all_pages_rendered_and_visually_inspected': True,
        'all_fonts_embedded': True, 'undefined_citations': False,
        'overfull_boxes': 0, 'missing_characters': 0,
        'optional_font_loader_fallback_notice': build['optional_font_loader_fallback_notice'],
        'input_manifest_members_verified': 431,
        'historical_audit_rows': len(historical),
        'poset_direct_image_counts': posets['totals'],
        'relative_path_certificates': 5313, 'monoid_isomorphism_classes': 273,
        'scope': 'Document/evidence consistency, not a proof-assistant verification. Open obligations and omitted searches remain as stated.'
    }
    (OUT / 'package_output.json').write_text(json.dumps(validation, indent=2) + '\n')
    files = included_files()
    assert all((ROOT / name) in files for name in TOP_FILES)
    assert not any(path.name in EXCLUDED_NAMES for path in files)
    manifest = ROOT / 'MANIFEST.sha256'
    manifest.write_text(''.join(f'{sha(path)}  {path.relative_to(ROOT).as_posix()}\n' for path in files))
    archive = ROOT.parent / 'RESIDUE.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in files + [manifest]:
            z.write(path, (Path(ROOT.name) / path.relative_to(ROOT)).as_posix())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(files) + 1
        for path in files:
            name = (Path(ROOT.name) / path.relative_to(ROOT)).as_posix()
            assert hashlib.sha256(z.read(name)).hexdigest() == sha(path)
    print(json.dumps({**validation, 'archive': str(archive),
                      'archive_members': len(files) + 1,
                      'archive_bytes': archive.stat().st_size,
                      'archive_sha256': sha(archive)}, indent=2))


if __name__ == '__main__':
    main()
