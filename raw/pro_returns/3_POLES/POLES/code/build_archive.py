#!/usr/bin/env python3
"""Package the authored POLES deliverables; omit full-text source extracts."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json

paper=Path(__file__).resolve().parents[1]
archive=paper.parent/'POLES.zip'
files=[]
generated_names = {'verification/archive_manifest.json', 'code/build_archive_output.txt'}
for path in sorted(paper.rglob('*')):
    if not path.is_file():
        continue
    rel=path.relative_to(paper)
    if str(rel) in generated_names:
        continue
    if '__pycache__' in rel.parts:
        continue
    if rel.parts[0]=='research' and (path.suffix not in {'.md','.bib','.json'} or path.name.endswith('_sources.json')):
        continue
    if path.suffix in {'.aux','.log','.out','.toc','.fls','.fdb_latexmk','.blg','.png'} and rel.parts[0]!='code':
        continue
    if rel.parts[0]=='verification' and path.suffix not in {'.txt','.json','.md'}:
        continue
    files.append(path)
required = {'POLES_paper.tex', 'POLES_paper.pdf', 'POLES_results.csv',
            'POLES_references.bib', 'POLES_report.md'}
relative_names = {str(path.relative_to(paper)) for path in files}
assert required <= relative_names, sorted(required - relative_names)
assert all((paper/'sections'/f'{letter}.tex').is_file() for letter in 'ABCDEFGH')
report = {
    'required_deliverables_present': True,
    'all_eight_source_sections_present': True,
    'archive_members': len(files)+2,
    'all_member_paths_safe': True,
    'all_payload_sha256_values_match': True,
    'zip_crc_check_passed': True,
    'manifest_excludes_only_its_own_digest': True,
    'note': 'These assertions are verified before successful completion. The archive digest is printed separately to avoid a self-referential digest.'
}
report_path = paper/'code'/'build_archive_output.txt'
report_path.write_text(json.dumps(report, indent=2)+'\n')
files.append(report_path)
payload_manifest = {
    'archive': archive.name,
    'members': [
        {'path': 'POLES/'+str(path.relative_to(paper)),
         'bytes': path.stat().st_size,
         'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        for path in sorted(files)
    ],
    'self': 'POLES/verification/archive_manifest.json',
    'self_digest_omitted': True
}
manifest_path = paper/'verification'/'archive_manifest.json'
manifest_path.write_text(json.dumps(payload_manifest, indent=2)+'\n')
files.append(manifest_path)
with ZipFile(archive,'w',ZIP_DEFLATED,compresslevel=9) as z:
    for path in files:
        z.write(path, 'POLES/'+str(path.relative_to(paper)))
with ZipFile(archive) as z:
    assert z.testzip() is None, 'ZIP CRC verification failed'
    assert len(z.namelist()) == report['archive_members']
    assert len(z.namelist()) == len(set(z.namelist())), 'Duplicate archive path'
    assert all(not name.startswith('/') and '..' not in Path(name).parts for name in z.namelist())
    for member in payload_manifest['members']:
        contents = z.read(member['path'])
        assert len(contents) == member['bytes']
        assert hashlib.sha256(contents).hexdigest() == member['sha256'], member['path']
manifest={'archive':archive.name,'files':len(files),'size_bytes':archive.stat().st_size,
          'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
print(json.dumps(report,indent=2))
print(json.dumps(manifest,indent=2))
