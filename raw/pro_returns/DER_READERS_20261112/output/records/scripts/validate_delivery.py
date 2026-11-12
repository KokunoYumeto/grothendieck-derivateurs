#!/usr/bin/env python3
"""Validate the complete reader delivery and create its manifest.

Run only after all eight reader/master compile records are current and valid.
Use --preliminary to inspect PDFs before the final README and visual-QA report
are complete. Preliminary runs never authorize packaging or write a manifest.
"""
from __future__ import annotations

import argparse
import collections
import csv
from dataclasses import dataclass
import hashlib
import io
import json
from pathlib import Path
import re
import sys

csv.field_size_limit(100000000)
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output'
RECORDS = OUT / 'records'
ARCHIVES = ('DER_READERS_FR.zip', 'DER_READERS_EN.zip', 'DER_READERS_RECORDS.zip')
STEMS = {
    'FR': ('DER_FR_diplomatique', 'DER_FR_corrige_apparat', 'DER_FR_texte_de_lecture', 'DER_FR_annotated_master'),
    'EN': ('DER_EN_diplomatic', 'DER_EN_corrected_apparatus', 'DER_EN_reading', 'DER_EN_annotated_master'),
}
COMPANION = 'LesDerivateurs_companion'
MANIFEST = RECORDS / 'DELIVERY_MANIFEST.tsv'
README = RECORDS / 'README.md'
TEXT_EXTENSIONS = {'.md','.txt','.tsv','.csv','.json','.jsonl','.py','.sh','.lua','.tex','.bib','.bbl','.sty','.log','.yaml','.yml','.toml','.rst','.ini','.cfg'}
COMPANION_EXTENSIONS = {'.tex','.pdf','.bib','.bbl','.sty','.md'}
EXCLUDED_PARTS = {'__pycache__','preview','previews','glyph_debug','stale','raw','raw_logs','rawlogs','build_raw'}
REQUIRED_RECORDS = (
    'README.md','CHANGES_FR.tsv','CHANGES_EN.tsv','CORRECTIONS_DECIDED.tsv',
    'GLOSSARY_FLAGGED.tsv','APPARATUS_COUNTS.md','CONVENTIONS_AUDIT.tsv',
    'FR_CORRECTION_PLAN.json','FR_CORRECTION_VALIDATION.json','FR_CORRECTION_COVERAGE.tsv',
    'FR_CORRECTION_COUNTS.tsv','EN_CHANGE_PLAN.json','EN_PLAN_VALIDATION.json',
    'EN_TRANSFER_AUDIT.json','EN_TRANSFER_AUDIT.tsv','EN_TRANSFER_DECISIONS.json',
    'EN_SOURCE_ROW_AUDIT.tsv','VALIDATION.json','VALIDATION_FR.json','VALIDATION_EN.json',
    'ANCHORS_FR.tsv','ANCHORS_EN.tsv','EDITORIAL_NOTES_FR.tsv','EDITORIAL_NOTES_EN.tsv',
    'BUILD_FR.json','BUILD_EN.json','INPUT_ARCHIVES.json','MANIFEST_VERIFIED.tsv',
    'APPENDIX_VALIDATION.json','APPENDIX_COMPILE_STATUS.json','APPENDIX_QA.md',
    'APPENDIX_SOURCE_EXTRACTS.md','APPENDIX_TYPESETTING_MAP.tsv',
    'APPENDIX_READER_NOTES_AUDIT.json','APPENDIX_READER_NOTES_AUDIT.md',
    'decisions/source/french/MANIFEST.json','decisions/source/french/README.txt',
    'scripts/verify_inputs.py','scripts/build_readers.py','scripts/reader_support.py',
    'scripts/resolve_french.py','scripts/resolve_english.py','scripts/transfer_english.py',
    'scripts/validate_french_plan.py','scripts/audit_english_plan.py','scripts/validate_readers.py',
    'scripts/compile_books.py','scripts/build_appendix.py','scripts/build_appendix_compile.py',
    'scripts/build_appendix_reader_audit.py','scripts/validate_delivery.py','scripts/package_deliverables.py',
)
EMAIL = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}')
PERSONAL_PATH = re.compile(r'(?:[A-Za-z]:[\\/]+(?:Users|home)[\\/]+[^\s\n"<>]+|/(?:Users|home|root|workspace|tmp|private|var|opt|usr)/[^\s\n"<>]+)')
WEB_URL = re.compile(r'https?://[^\s<>"{}]+')
GENERIC_CODE_PREFIXES = ('/usr/share/texlive/', '/usr/share/texmf', '/usr/bin/', '/bin/', '/opt/codex/')
PENDING = re.compile(r'\b(?:PENDING(?:_[A-Z0-9_]+)?|TODO|TBD)\b')


class DeliveryError(RuntimeError):
    pass


@dataclass(frozen=True)
class PayloadFile:
    archive: str
    archive_path: str
    source: Path


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(name: str):
    return json.loads((RECORDS / name).read_text(encoding='utf-8'))


def require(condition, message):
    if not condition:
        raise DeliveryError(message)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def excluded(path: Path, base: Path) -> bool:
    parts = path.relative_to(base).parts
    return any(part.startswith('.') or part.lower() in EXCLUDED_PARTS for part in parts) or any(
        label in path.name.lower() for label in ('preview', 'glyph_debug', '.pyc', '.pyo', '.stale', 'raw_reader'))


def collect_payload(*, include_delivery=True, include_manifest=True):
    """Return only explicitly approved archive members, with no filesystem metadata."""
    files = []
    for language, stems in STEMS.items():
        archive = f'DER_READERS_{language}.zip'
        for stem in stems:
            for suffix in ('.tex','.pdf'):
                path = OUT / language / (stem + suffix)
                files.append(PayloadFile(archive, relative(path), path))
    for path in sorted((OUT/'companion').rglob('*')):
        if path.is_file() and not excluded(path, OUT/'companion') and path.suffix.lower() in COMPANION_EXTENSIONS:
            files.append(PayloadFile(ARCHIVES[2], relative(path), path))
    for path in sorted(RECORDS.rglob('*')):
        if not path.is_file() or excluded(path, RECORDS):
            continue
        if path.name.startswith('DELIVERY_PRELIMINARY'):
            continue
        if not include_delivery and path.name.startswith('DELIVERY_'):
            continue
        if path == MANIFEST and not include_manifest:
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {'LICENSE','COPYING','NOTICE'}:
            continue
        if path.suffix.lower() == '.log' and path.parent != RECORDS/'build' and not path.name.startswith('APPENDIX_'):
            continue
        if path.suffix.lower() == '.log' and path.parent == RECORDS/'build':
            match = re.fullmatch(r'(DER_(?:FR|EN)_[A-Za-z_]+)\.pass(\d+)\.log',path.name)
            if match is None or not path.with_name(match[1]+'.json').is_file():
                continue
            current = json.loads(path.with_name(match[1]+'.json').read_text())
            if int(match[2]) not in {p['pass'] for p in current.get('passes',[])}:
                continue
        files.append(PayloadFile(ARCHIVES[2], relative(path), path))
    for archive in ARCHIVES:
        files.append(PayloadFile(archive, 'README.md', README))
    files.sort(key=lambda x: (x.archive, x.archive_path))
    seen = set()
    for entry in files:
        key = entry.archive, entry.archive_path
        require(key not in seen, f'Duplicate archive member: {entry.archive}/{entry.archive_path}')
        seen.add(key)
        require(entry.source.is_file(), f'Missing payload file: {relative(entry.source)}')
        require(not entry.source.is_symlink(), f'Symbolic link is not an approved payload file: {relative(entry.source)}')
        require(not entry.archive_path.startswith('/') and '..' not in Path(entry.archive_path).parts, 'Unsafe archive member name')
    return files


def payload_records(files):
    cache = {}
    result = []
    for entry in files:
        if entry.source not in cache:
            cache[entry.source] = (entry.source.stat().st_size, sha_file(entry.source))
        size, digest = cache[entry.source]
        result.append(dict(archive=entry.archive, path=entry.archive_path, bytes=size, sha256=digest))
    return result


def fingerprint(records):
    return sha_bytes(json.dumps(records, sort_keys=True, separators=(',',':'), ensure_ascii=False).encode())


def compile_gate():
    """A failed or stale master build blocks every final delivery action."""
    records = {}
    for language, stems in STEMS.items():
        for stem in stems:
            path = RECORDS/'build'/(stem+'.json')
            require(path.is_file(), f'Build record is not ready: build/{stem}.json')
            record = json.loads(path.read_text())
            require(record.get('compiled_without_errors') is True, f'Build is not valid: {stem}')
            passes = record.get('passes', [])
            require(bool(passes), f'Build has no pass record: {stem}')
            last = passes[-1]
            require(last.get('returncode') == 0, f'Build returned an error: {stem}')
            for field in ('errors','missing_glyphs','undefined','unsettled'):
                require(not last.get(field), f'Final build has {field}: {stem}')
            tex = OUT/language/(stem+'.tex')
            pdf = tex.with_suffix('.pdf')
            require(tex.is_file() and pdf.is_file(), f'Source or PDF missing: {stem}')
            require(record.get('source_tex_sha256') == sha_file(tex), f'Stale compiled source: {stem}')
            require(record.get('pdf_sha256') == sha_file(pdf), f'Stale compiled PDF: {stem}')
            require(record.get('pdf_bytes') == pdf.stat().st_size, f'PDF byte count differs: {stem}')
            require(isinstance(record.get('pages'), int) and record['pages'] > 0, f'No PDF page count: {stem}')
            records[stem] = record
    companion = read_json('APPENDIX_COMPILE_STATUS.json')
    pdf = OUT/'companion'/(COMPANION+'.pdf')
    require(pdf.is_file(), 'Companion PDF missing')
    require(companion.get('latex_errors') == 0, 'Companion compile has errors')
    require(companion.get('missing_glyph_warnings') == 0, 'Companion compile has missing glyphs')
    require(companion.get('undefined_references_or_citations') == 0, 'Companion compile has unresolved references')
    require(all(run.get('exit_code') == 0 for run in companion.get('runs',[])), 'Companion run history contains a failed program')
    require(companion.get('pdf_sha256') == sha_file(pdf), 'Companion PDF hash differs from its build record')
    require(companion.get('pdf_bytes') == pdf.stat().st_size, 'Companion PDF byte count differs')
    records[COMPANION] = companion
    return records


def privacy_scan(text, file, *, code=False, page=None, component='text'):
    """Report locations and hashes, never reproduce a private value in a log."""
    hits = []
    ignored = collections.Counter()
    urls = [(m.start(),m.end()) for m in WEB_URL.finditer(text)]
    for rule, pattern in [('email',EMAIL),('local_path',PERSONAL_PATH)]:
        for m in pattern.finditer(text):
            value = m.group().rstrip("),.;'}]")
            if rule == 'local_path' and any(a <= m.start() < b for a,b in urls):
                ignored['public_url_component'] += 1
                continue
            if rule == 'local_path' and code:
                if any(value.startswith(prefix) for prefix in GENERIC_CODE_PREFIXES):
                    ignored['generic_runtime_constant'] += 1
                    continue
                if any(token in value for token in ('[^','(?:','[A-','[a-','\\s','\\n','\\w')):
                    ignored['path_detection_regular_expression'] += 1
                    continue
            hits.append(dict(file=file, component=component, page=page, rule=rule,
                             line=text.count('\n',0,m.start())+1, offset=m.start(), value_sha256=sha_bytes(value.encode())))
    return hits, dict(ignored)


def tex_data(path):
    text = path.read_text()
    payload = text.split('\n%%DER_JSON_PAYLOAD_BEGIN%%\n',1)[1].split('\n%%DER_JSON_PAYLOAD_END%%',1)[0]
    return json.loads(payload)


def source_and_record_checks(builds, *, preliminary):
    for name in REQUIRED_RECORDS:
        require((RECORDS/name).is_file(), f'Required record missing: {name}')
        require((RECORDS/name).stat().st_size > 0, f'Required record is empty: {name}')
    pending = []
    for name in ('README.md','PDF_VISUAL_QA.md'):
        path = RECORDS/name
        problem = not path.is_file() or not path.read_text().strip() or bool(PENDING.search(path.read_text()))
        if problem:
            if preliminary:
                pending.append(name)
            else:
                raise DeliveryError(f'Final release record is missing or contains placeholders: {name}')
    fr = read_json('FR_CORRECTION_PLAN.json')
    en = read_json('EN_CHANGE_PLAN.json')
    fr_check = read_json('FR_CORRECTION_VALIDATION.json')
    en_check = read_json('EN_PLAN_VALIDATION.json')
    require(fr_check.get('status') == 'pass' and not fr_check.get('errors'), 'French plan validation does not pass')
    require(fr_check.get('plan_sha256') == sha_file(RECORDS/'FR_CORRECTION_PLAN.json'), 'French plan validation is stale')
    require(fr_check.get('rows_expected') == fr_check.get('rows_accounted') == 1879, 'French source-row count is not 1879')
    require(len(fr['rows']) == 1879 and len({r['id'] for r in fr['rows']}) == 1879, 'French row IDs are incomplete or duplicated')
    require({r['status'] for r in fr['rows']} <= {'applied','merged','no_change','rejected'}, 'French decisions are incomplete')
    require(all(r.get('reason') for r in fr['rows']), 'A French decision lacks a reason')
    require(en_check.get('fr_plan_sha256') == sha_file(RECORDS/'FR_CORRECTION_PLAN.json'), 'English audit uses a stale French plan')
    require(en_check.get('en_plan_sha256') == sha_file(RECORDS/'EN_CHANGE_PLAN.json'), 'English audit uses a stale English plan')
    for key in ('every_french_variant_accounted_for','every_source_row_accounted_for','all_original_offsets_and_protected_text_verified'):
        require(en_check.get(key) is True, f'English audit failed: {key}')
    for name, digest in en.get('input_sha256', {}).items():
        require((RECORDS/name).is_file() and sha_file(RECORDS/name) == digest, f'English plan input changed: {name}')
    root_validation = read_json('VALIDATION.json')
    require(root_validation.get('issues') == 0, 'Root source validation has issues')
    require(root_validation.get('coverage',{}).get('edition_slip_rows') == 1879, 'Root validation has incomplete row coverage')
    note_check = read_json('APPENDIX_READER_NOTES_AUDIT.json')
    require(note_check.get('all_checks_passed') is True, 'Independent note audit does not pass')
    require(note_check.get('builder_sha256') == sha_file(RECORDS/'scripts/build_readers.py'), 'Independent note audit uses an older builder')
    by_root = {x['language']:x for x in root_validation['languages']}
    by_notes = {x['language']:x for x in note_check['languages']}
    expected_ids = {}
    units = {}
    for language, plan in [('FR',fr),('EN',en)]:
        master = OUT/language/f'DER_{language}_annotated_master.tex'
        data = tex_data(master)
        require(data.get('units') and len(data['units']) == 243, f'Master has wrong unit count: {language}')
        plan_ids = [e['id'] for e in plan['edits']]
        master_ids = [e['id'] for u in data['units'] for e in u['variants']]
        require(len(plan_ids) == len(set(plan_ids)), f'Duplicate variant ID: {language}')
        require(set(plan_ids) == set(master_ids) and len(plan_ids) == len(master_ids), f'Master variants differ from plan: {language}')
        expected_ids[language] = sorted(plan_ids)
        units[language] = len(data['units'])
        for summary in (by_root[language],read_json(f'VALIDATION_{language}.json'),by_notes[language]):
            require(summary.get('master_sha256') == sha_file(master), f'Stale master validation: {language}')
            require(summary.get('units') == 243 and summary.get('variants') == len(plan_ids), f'Validation counts differ: {language}')
            require(not summary.get('issues'), f'Validation reports issues: {language}')
        # The independent audit hashes read_text() output: its CSV line endings
        # are canonically decoded before hashing, whereas the manifest hashes bytes.
        notes_digest = sha_bytes((RECORDS/f'EDITORIAL_NOTES_{language}.tsv').read_text().encode())
        require(by_notes[language].get('notes_sha256') == notes_digest, f'Note ledger changed after audit: {language}')
        for source in by_notes[language]['standalone_files']:
            require(source.get('master_projection_exact') is True, f'Master projection failed: {source["file"]}')
            require(source['sha256'] == sha_file(OUT/language/source['file']), f'Stale independent source audit: {source["file"]}')
        for stem in STEMS[language][:3]:
            v = by_root[language]['forms'][stem]
            require(v['tex_sha256'] == builds[stem]['source_tex_sha256'], f'Stale root source validation: {stem}')
            require(v.get('pdf_sha256') == builds[stem]['pdf_sha256'], f'Stale root PDF validation: {stem}')
            require(v.get('pages') == builds[stem]['pages'], f'Stale root PDF page count: {stem}')
    changes = {}
    for language in ('FR','EN'):
        with (RECORDS/f'CHANGES_{language}.tsv').open(newline='') as f:
            reader = csv.DictReader(f,delimiter='\t')
            require(reader.fieldnames == ['page','place','before','after','source'], f'Change-log columns differ: {language}')
            rows = list(reader)
        require(all(r['source'] and r['before'] != r['after'] for r in rows), f'Empty source or identity in change log: {language}')
        ids = collections.Counter(id_ for r in rows for id_ in re.findall(r'\b'+('FRV' if language=='FR' else 'ENV')+r'\d+\b',r['source']))
        require(set(ids) == set(expected_ids[language]) and set(ids.values()) == {1}, f'Change log variant coverage differs: {language}')
        changes[language] = dict(rows=len(rows),variant_rows=sum(ids.values()),assembly_or_common_rows=len(rows)-sum(ids.values()))
    appendix = read_json('APPENDIX_VALIDATION.json')
    appendix_tex = (OUT/'companion/appendix_new_results.tex').read_text()
    labels = list(map(int,re.findall(r'\\label\{nr:entry(\d+)\}',appendix_tex)))
    require(labels == list(range(1,13)), 'Appendix does not contain exactly entries 1–12')
    require(appendix.get('section_count') == appendix.get('reading_count') == 12, 'Appendix validation count differs')
    require(len(appendix.get('entries',[])) == 12 and all(e.get('statement_preserved') is True for e in appendix['entries']), 'Appendix statement-preservation record fails')
    require(appendix_tex.count(r'\subsection*{GPT-6 Astra\textquotesingle s reading}') == 12, 'Appendix reading paragraphs are incomplete')
    require('No priority is claimed.' in appendix_tex and 'Our search was limited' in appendix_tex, 'Appendix framing missing')
    require(r'\section*{Statements found to be known}' in appendix_tex, 'Appendix known-results list missing')
    require(r'\input{appendix_new_results}' in (OUT/'companion'/f'{COMPANION}.tex').read_text(), 'Companion master does not input appendix')
    part_files = sorted((OUT/'companion/parts').glob('*.tex'))
    require(len(part_files) == 64, 'Companion part/definition file count differs from 64')
    require(builds[COMPANION].get('byte_identical_source_part_files') == 64, 'Companion source-preservation record fails')
    return dict(source_rows=1879,units=units,variants={k:len(v) for k,v in expected_ids.items()},
                changes=changes,appendix_entries=12,companion_part_files=64,pending_release_records=pending),expected_ids


def compile_summary(builds):
    rows = []
    for language, stems in STEMS.items():
        for stem in stems:
            record = builds[stem]
            last = record['passes'][-1]
            rows.append(dict(book=stem,language=language,pages=record['pages'],passes=len(record['passes']),
                errors=len(last.get('errors',[])),missing_glyphs=len(last.get('missing_glyphs',[])),
                unresolved=len(last.get('undefined',[])),rerun_requests=len(last.get('unsettled',[])),
                latex_package_warnings=len(last.get('warnings',[])),backend_warnings=len(last.get('backend_warnings',[])),
                overfull_hboxes=last.get('overfull_hbox',0),overfull_vboxes=last.get('overfull_vbox',0),
                underfull_hboxes=last.get('underfull_hbox',0),underfull_vboxes=last.get('underfull_vbox',0),
                maximum_overfull_hbox_pt=last.get('largest_overfull_hbox_pt',0),maximum_overfull_vbox_pt=last.get('largest_overfull_vbox_pt',0),
                source_tex_sha256=record['source_tex_sha256'],source_hash_basis='compile record',pdf_sha256=record['pdf_sha256']))
    c = builds[COMPANION]
    log = (RECORDS/'APPENDIX_compile.log').read_text()
    rows.append(dict(book=COMPANION,language='companion',pages=c['pages'],passes=sum(r['program']=='LuaLaTeX' for r in c['runs']),
        errors=c['latex_errors'],missing_glyphs=c['missing_glyph_warnings'],unresolved=c['undefined_references_or_citations'],
        rerun_requests=len(re.findall(r'Label\(s\) may have changed|Rerun to get cross-references right|Rerun to get outlines right',log)),
        latex_package_warnings=c['package_or_latex_warnings'],backend_warnings=len(re.findall(r'^warning\s+\([^\n]*',log,re.M|re.I)),
        overfull_hboxes=c['overfull_hboxes'],overfull_vboxes=c['overfull_vboxes'],
        underfull_hboxes=len(re.findall(r'Underfull \\hbox',log)),underfull_vboxes=len(re.findall(r'Underfull \\vbox',log)),
        maximum_overfull_hbox_pt=c['largest_overfull_hbox_pt'],maximum_overfull_vbox_pt=c['largest_overfull_vbox_pt'],
        source_tex_sha256=sha_file(OUT/'companion'/f'{COMPANION}.tex'),
        source_hash_basis='current source snapshot; companion legacy build record has no source hash',pdf_sha256=c['pdf_sha256']))
    with (RECORDS/'COMPILE_STATUS.tsv').open('w',newline='') as f:
        w = csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    return rows


def release_layout_checks(builds, *, preliminary):
    """Bind the two concrete margin repairs to their final visual evidence."""
    if preliminary:
        return dict(status='not_enforced_in_preliminary',
                    reports=['MARGIN_LAYOUT_AUDIT.json','MARGIN_REFINEMENT_COMPARISON.json'])
    for name in ('MARGIN_LAYOUT_AUDIT.json','MARGIN_LAYOUT_AUDIT.tsv','MARGIN_LAYOUT_REVIEW.json',
                 'MARGIN_PLACEMENTS.tsv','MARGIN_REFINEMENT_COMPARISON.json',
                 'MARGIN_REFINEMENT_COMPARISON.md','scripts/compare_margin_refinement.py'):
        require((RECORDS/name).is_file(),f'Final margin evidence is missing: {name}')
    margin = read_json('MARGIN_LAYOUT_AUDIT.json')
    require(margin.get('status') == 'pass','Final margin-layout audit does not pass')
    require(margin.get('review_counts',{}).get('confirmed_collision') == 0,'Final margin review contains a confirmed collision')
    require(margin.get('review_counts',{}).get('unreviewed') == 0,'Final margin review has unreviewed candidates')
    standalone = {f'output/{language}/{stem}.pdf':stem for language,stems in STEMS.items() for stem in stems[:3]}
    margin_books = margin.get('books',[])
    require(len(margin_books)==6 and {b.get('file') for b in margin_books}==set(standalone),
            'Margin audit does not cover exactly the six current standalone PDFs')
    for book in margin_books:
        stem = standalone[book['file']]
        require(book.get('pdf_sha256') == builds[stem]['pdf_sha256'],f'Stale margin audit PDF: {stem}')
        require(book.get('pages') == builds[stem]['pages'],f'Stale margin audit page count: {stem}')
    targets = margin.get('unit_specific_placement_targets',[])
    require(len(targets)==6 and {t.get('file') for t in targets}==set(standalone),
            'Final margin audit does not identify all six repaired standalone labels')
    for target in targets:
        stem = standalone[target['file']]
        require(target.get('pdf_sha256') == builds[stem]['pdf_sha256'],f'Stale repaired-label evidence: {stem}')
        gap = target.get('horizontal_clearance_from_adjacent_body_text_pt')
        require(isinstance(gap,(int,float)) and gap>0,f'Repaired label lacks positive horizontal clearance: {stem}')
    comparison = read_json('MARGIN_REFINEMENT_COMPARISON.json')
    require(comparison.get('schema') == 'margin-refinement-comparison-v1' and comparison.get('status') == 'PASS',
            'Final margin refinement comparison does not pass')
    require(comparison.get('script') == 'output/records/scripts/compare_margin_refinement.py',
            'Unexpected margin comparison script identity')
    require(comparison.get('script_sha256') == sha_file(RECORDS/'scripts/compare_margin_refinement.py'),
            'Margin comparison script changed after its report')
    require(comparison.get('placement_record') == 'output/records/MARGIN_PLACEMENTS.tsv',
            'Unexpected margin placement record identity')
    require(comparison.get('placement_record_sha256') == sha_file(RECORDS/'MARGIN_PLACEMENTS.tsv'),
            'Margin placement rules changed after comparison')
    expected = {stem:language for language,stems in STEMS.items() for stem in stems}
    books = comparison.get('books',[])
    require(len(books)==8 and {b.get('book') for b in books}==set(expected),
            'Refinement comparison does not cover exactly the eight reader/master PDFs')
    pixel_count = 0
    for book in books:
        stem = book['book'];language = expected[stem];build = builds[stem]
        require(book.get('language') == language and book.get('status') == 'PASS',f'Refinement comparison failed: {stem}')
        require(not book.get('unexpected_differences'),f'Refinement contains unpermitted differences: {stem}')
        after = book.get('after',{});before = book.get('before',{})
        require(after.get('file') == f'output/{language}/{stem}.pdf',f'Unexpected refinement PDF path: {stem}')
        require(after.get('sha256') == build['pdf_sha256'] and after.get('pdf_bytes') == build['pdf_bytes'],
                f'Stale refinement PDF identity: {stem}')
        require(after.get('source_tex_sha256') == build['source_tex_sha256'],f'Stale refinement source identity: {stem}')
        require(after.get('build_record') == f'output/records/build/{stem}.json',f'Unexpected refinement build record: {stem}')
        require(after.get('build_record_sha256') == sha_file(RECORDS/'build'/(stem+'.json')),
                f'Build record changed after refinement comparison: {stem}')
        require(before.get('pages') == after.get('pages') == build['pages'],f'Refinement page counts differ: {stem}')
        require(book.get('exactly_unchanged_pages') == build['pages']-1,f'Refinement changed an unexpected number of pages: {stem}')
        moved = book.get('targets',[]);changed = book.get('changed_pages',[])
        require(len(moved)==1 and moved[0].get('status')=='PASS',f'Refinement does not verify exactly one moved label: {stem}')
        require(moved[0].get('vertical_coordinates_exactly_unchanged') is True,f'Margin repair moved vertical coordinates: {stem}')
        require(len(changed)==1 and changed[0].get('physical_page')==moved[0].get('physical_page'),
                f'Refinement changed a page beyond its permitted label: {stem}')
        components = book.get('component_sha256',{})
        require(book.get('all_components_equal_after_restoring_only_permitted_label') is True
                and bool(components.get('before'))
                and components.get('before') == components.get('after_with_permitted_label_restored'),
                f'Refinement component identities do not match after the one permitted restoration: {stem}')
        samples = book.get('reviewed_sample_pixels',[])
        required_samples = comparison.get('reviewed_sample_specification',{}).get(stem)
        require(isinstance(required_samples,list) and sorted(s.get('physical_page') for s in samples)==sorted(required_samples),
                f'Refinement raster sample coverage differs: {stem}')
        for sample in samples:
            a=sample.get('before',{});b=sample.get('after',{})
            require(sample.get('exactly_equal') is True and bool(a.get('pixel_sha256')) and a==b,
                    f'Refinement raster pixels or dimensions differ: {stem}, page {sample.get("physical_page")}')
        pixel_count += len(samples)
    expected_totals = dict(books=8,pages=sum(builds[s]['pages'] for s in expected),
                           exactly_unchanged_pages=sum(builds[s]['pages']-1 for s in expected),
                           permitted_labels=8,unexpected_differences=0,raster_samples=68,raster_samples_equal=68)
    require(comparison.get('totals') == expected_totals and pixel_count==68,
            'Final refinement totals or the 68 matching raster samples differ')
    return dict(status='pass',standalone_margin_books=6,confirmed_collisions=0,unreviewed_candidates=0,
                positive_clearance_targets=6,refinement_totals=expected_totals,
                margin_audit_sha256=sha_file(RECORDS/'MARGIN_LAYOUT_AUDIT.json'),
                refinement_comparison_sha256=sha_file(RECORDS/'MARGIN_REFINEMENT_COMPARISON.json'))


def inspect_pdfs(builds):
    import fitz
    summaries = {}
    texts = {}
    privacy = []
    for language, stems in list(STEMS.items()) + [('companion',(COMPANION,))]:
        for stem in stems:
            path = OUT/language/(stem+'.pdf')
            page_texts = []
            page_geometry = []
            with fitz.open(path) as doc:
                require(not doc.is_encrypted, f'PDF is encrypted: {stem}')
                require(doc.page_count == builds[stem]['pages'], f'PDF page count differs from build record: {stem}')
                metadata = json.dumps(doc.metadata,sort_keys=True,ensure_ascii=False)+'\n'+doc.get_xml_metadata()
                hits,_ = privacy_scan(metadata,relative(path),component='PDF metadata');privacy += hits
                for index,page in enumerate(doc):
                    text = page.get_text('text',sort=False)
                    page_texts.append(text)
                    page_geometry.append(dict(rect=list(page.rect),mediabox=list(page.mediabox),cropbox=list(page.cropbox),rotation=page.rotation))
                    hits,_ = privacy_scan(text,relative(path),page=index+1,component='PDF page text');privacy += hits
                    for link in page.get_links():
                        if link.get('uri'):
                            hits,_ = privacy_scan(link['uri'],relative(path),page=index+1,component='PDF link URI');privacy += hits
                summaries[stem] = dict(file=relative(path),pages=doc.page_count,pdf_sha256=sha_file(path),
                    text_sha256=sha_bytes('\f'.join(page_texts).encode()),
                    page_text_sha256=[sha_bytes(t.encode()) for t in page_texts],
                    page_geometry_sha256=sha_bytes(json.dumps(page_geometry,sort_keys=True).encode()),
                    metadata_sha256=sha_bytes(metadata.encode()))
            texts[stem] = (page_texts,page_geometry)
            print(json.dumps(dict(pdf=stem,pages=len(page_texts),extracted_all_pages=True)),flush=True)
    comparisons = {}
    for language, stems in STEMS.items():
        standalone,master = stems[0],stems[3]
        a,ag = texts[standalone];b,bg = texts[master]
        differences = []
        for index in range(max(len(a),len(b))):
            if index >= len(a) or index >= len(b):
                differences.append(dict(page=index+1,kind='page_count'))
            elif a[index] != b[index] or ag[index] != bg[index]:
                differences.append(dict(page=index+1,text_equal=a[index]==b[index],geometry_equal=ag[index]==bg[index],
                    standalone_text_sha256=sha_bytes(a[index].encode()),master_text_sha256=sha_bytes(b[index].encode())))
        comparisons[language] = dict(standalone=standalone,master=master,pages=len(a),exact_text_and_page_sequence=not differences,differences=differences)
    return summaries,comparisons,privacy


def pdf_object(value):
    return value.get_object() if hasattr(value,'get_object') else value


def destination_name(value):
    value = pdf_object(value)
    if isinstance(value,bytes):
        return value.decode('utf-8',errors='replace')
    if isinstance(value,str):
        return value.lstrip('/')
    return None


def destination_key(value):
    value = pdf_object(value)
    if isinstance(value,dict) and '/D' in value:
        value = pdf_object(value['/D'])
    if not isinstance(value,(list,tuple)):
        return None
    def atom(x):
        if hasattr(x,'idnum'):
            return ('ref',x.idnum,x.generation)
        if x is None or str(x) == 'NullObject':
            return 'null'
        return str(x)
    return tuple(atom(x) for x in value)


def named_destination_pairs(reader):
    pairs = []
    seen = set()
    def walk(reference):
        if hasattr(reference,'idnum'):
            key = reference.idnum,reference.generation
            require(key not in seen,'Cyclic or repeated PDF destination-name tree')
            seen.add(key)
        node = pdf_object(reference)
        names = pdf_object(node.get('/Names',[]))
        require(len(names)%2==0,'Malformed PDF destination name array')
        pairs.extend((destination_name(names[i]),names[i+1]) for i in range(0,len(names),2))
        for kid in pdf_object(node.get('/Kids',[])):
            walk(kid)
    catalog = pdf_object(reader.trailer['/Root'])
    names = pdf_object(catalog.get('/Names',{}))
    if names.get('/Dests') is not None:
        walk(names['/Dests'])
    legacy = pdf_object(catalog.get('/Dests',{}))
    pairs.extend((str(k).lstrip('/'),v) for k,v in legacy.items())
    return pairs


def apparatus_links(language, expected_ids):
    import fitz
    from pypdf import PdfReader
    stem = STEMS[language][1]
    path = OUT/language/(stem+'.pdf')
    reader = PdfReader(path)
    pairs = named_destination_pairs(reader)
    counts = collections.Counter(name for name,_ in pairs)
    expected = {'app-'+id_:id_ for id_ in expected_ids}
    actual = {name for name,_ in pairs if name and re.fullmatch(r'app-(?:FRV|ENV)\d+',name)}
    resolved = reader.named_destinations
    direct = collections.defaultdict(list)
    for name,value in pairs:
        key = destination_key(value)
        if key is not None:
            direct[key].append(name)
    inbound = collections.defaultdict(list)
    unexpected_links = []
    with fitz.open(path) as doc:
        for index,page in enumerate(reader.pages):
            for reference in pdf_object(page.get('/Annots',[])):
                annotation = pdf_object(reference)
                if annotation.get('/Subtype') != '/Link':
                    continue
                action = pdf_object(annotation.get('/A',{}))
                if '/Dest' in annotation:
                    dest = annotation['/Dest']
                elif action.get('/S') == '/GoTo':
                    dest = action.get('/D')
                else:
                    continue
                name = destination_name(dest)
                if name is None:
                    aliases = [n for n in direct.get(destination_key(dest),[]) if n in expected]
                    if len(aliases)==1:
                        name = aliases[0]
                if name not in expected:
                    if name and name.startswith('app-'):
                        unexpected_links.append(dict(page=index+1,destination=name))
                    continue
                rect = annotation.get('/Rect')
                label_ok = False
                if rect and len(rect)==4:
                    clip = fitz.Rect([float(x) for x in rect])*doc[index].transformation_matrix
                    label = doc[index].get_textbox(clip+(-2,-2,2,2))
                    label_ok = expected[name] in re.sub(r'\s+','',label)
                inbound[name].append(dict(page=index+1,visible_marker_label_verified=label_ok))
    rows = []
    issues = []
    if unexpected_links:
        issues.append(dict(kind='unexpected_apparatus_link_targets',links=unexpected_links))
    if actual != set(expected):
        issues.append(dict(kind='destination_set',missing=sorted(set(expected)-actual),unexpected=sorted(actual-set(expected))))
    for name,id_ in sorted(expected.items()):
        page = None
        if name in resolved:
            page = reader.get_destination_page_number(resolved[name])
            if page is not None:
                page += 1
        links = inbound.get(name,[])
        ok = counts[name]==1 and isinstance(page,int) and page>0 and len(links)==1 and all(x['visible_marker_label_verified'] for x in links)
        row = dict(language=language,id=id_,destination=name,destination_count=counts[name],destination_page=page,
                   inbound_marker_links=len(links),marker_pages=','.join(str(x['page']) for x in links),
                   visible_marker_labels_verified=bool(links) and all(x['visible_marker_label_verified'] for x in links),passed=ok)
        rows.append(row)
        if not ok:
            issues.append(dict(kind='apparatus_link',**row))
    return dict(pdf=relative(path),expected_entries=len(expected),named_entries=len(actual),
                verified_entries=sum(r['passed'] for r in rows),issues=issues),rows


def write_tsv(path, rows, fields):
    with path.open('w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)


def report_markdown(report):
    lines = ['# Delivery validation','',f"**Status: {report['status']}.**",'',
             'The validation binds the source plans, annotated masters, standalone sources, compiled PDFs, and delivery payload by SHA-256. All paths are archive-relative.', '',
             '| PDF | Pages | Full-page text and metadata scanned |','|---|---:|---|']
    for stem,pdf in report.get('pdfs',{}).items():
        lines.append(f"| `{stem}` | {pdf['pages']} | Yes |")
    lines += ['', '## Apparatus links', '', '| Language | Expected destinations | Verified destination and one visible inbound marker |', '|---|---:|---:|']
    for lang,item in report.get('apparatus_links',{}).items():
        lines.append(f"| {lang} | {item['expected_entries']} | {item['verified_entries']} |")
    lines += ['', 'Every expected ID must occur once in the PDF destination name tree, resolve to a page, and receive exactly one link annotation whose rectangle contains that visible marker ID. Per-ID evidence is in `DELIVERY_APPARATUS_LINKS.tsv`.', '',
              '## Default master projections', '']
    for lang,item in report.get('master_pdf_comparison',{}).items():
        lines.append(f"- {lang}: {'exact' if item['exact_text_and_page_sequence'] else 'DIFFERENCES'}; {item['pages']} pages compared, including each page’s exact extracted text and geometry.")
    lines += ['', '## Final margin-repair evidence', '']
    layout = report.get('release_layout_checks',{})
    if layout.get('status') == 'pass':
        totals = layout['refinement_totals']
        lines += [f"The six standalone margin audits pass with zero confirmed collisions and zero unreviewed candidates. All six repaired labels have positive horizontal clearance. The refinement comparison is bound to the current eight PDF, TeX, and compile-record hashes; it covers {totals['pages']} pages, permits exactly one specified label translation per book, and confirms identical pixels and dimensions for all {totals['raster_samples']} reviewed samples."]
    else:
        lines += ['These final release gates are deferred in preliminary mode. Final validation requires the completed, current margin and refinement reports.']
    lines += ['', '## Privacy and payload', '',
              f"Privacy findings: **{len(report.get('privacy_findings',[]))}**. Full payload text, all PDF pages, PDF metadata, and link URIs are scanned. Detection regular expressions and generic runtime constants in code are classified separately; private values are never copied into this report.", '',
              'The whitelist excludes generated TeX auxiliary files, raw reader logs, caches, preview images, glyph-debug material, stale files, and preliminary delivery reports. Language archives contain exactly four `.tex` and four `.pdf` files plus their root README. The records archive contains the approved records and companion source tree.', '',
              'The final manifest records archive name, archive-relative member path, byte length, and SHA-256. It includes the completed validation reports. `DELIVERY_MANIFEST.tsv` excludes its own row to avoid self-reference; the archive receipt outside the ZIPs records each complete archive’s SHA-256 and protects the manifest as an archive member.', '',
              '## Pending release records', '']
    pending = report.get('source_checks',{}).get('pending_release_records',[])
    lines += ['- '+x for x in pending] if pending else ['None.']
    lines += ['', '## Issues', '']
    lines += ['- '+x for x in report.get('issues',[])] if report.get('issues') else ['None.']
    return '\n'.join(lines)+'\n'


def validate(*, preliminary=False):
    builds = compile_gate()
    checks,ids = source_and_record_checks(builds,preliminary=preliminary)
    layout_checks = release_layout_checks(builds,preliminary=preliminary)
    compile_rows = compile_summary(builds)
    pdfs,comparisons,pdf_privacy = inspect_pdfs(builds)
    link_summaries = {}
    link_rows = []
    for language in ('FR','EN'):
        summary,rows = apparatus_links(language,ids[language])
        link_summaries[language] = summary;link_rows += rows
        print(json.dumps(dict(apparatus=language,verified=summary['verified_entries'],expected=summary['expected_entries'])),flush=True)
    links_path = RECORDS/('DELIVERY_PRELIMINARY_APPARATUS_LINKS.tsv' if preliminary else 'DELIVERY_APPARATUS_LINKS.tsv')
    write_tsv(links_path,link_rows,list(link_rows[0]))
    files = collect_payload(include_delivery=False,include_manifest=False)
    privacy = list(pdf_privacy)
    ignored = collections.Counter()
    scanned = set()
    for entry in files:
        if entry.source in scanned or entry.source.suffix.lower()=='.pdf':
            continue
        scanned.add(entry.source)
        text = entry.source.read_text(encoding='utf-8')
        hits,allow = privacy_scan(text,relative(entry.source),code=entry.source.suffix.lower() in {'.py','.sh','.lua'})
        privacy += hits;ignored.update(allow)
    inputs = payload_records(files)
    issues = []
    if privacy:
        issues.append('Privacy scan found candidate private data; see redacted locations in privacy_findings.')
    for language,item in comparisons.items():
        if not item['exact_text_and_page_sequence']:
            issues.append(f'{language} default master PDF differs from the standalone diplomatic PDF.')
    for language,item in link_summaries.items():
        if item['issues']:
            issues.append(f'{language} apparatus destination or inbound marker-link audit failed.')
    report = dict(format='DER delivery validation 1',status='fail' if issues else ('preliminary' if preliminary else 'pass'),
        preliminary=preliminary,source_checks=checks,release_layout_checks=layout_checks,compile_summary=compile_rows,pdfs=pdfs,
        apparatus_links=link_summaries,master_pdf_comparison=comparisons,
        privacy_findings=privacy,privacy_code_classifications=dict(ignored),text_payload_files_scanned=len(scanned),
        input_payload_fingerprint=fingerprint(inputs),input_payload=inputs,issues=issues,
        manifest_self_exclusion='DELIVERY_MANIFEST.tsv omits its own inventory row. Complete archive hashes are recorded outside the ZIPs in DER_READERS_ARCHIVES.json.')
    stem = 'DELIVERY_PRELIMINARY' if preliminary else 'DELIVERY_VALIDATION'
    report_path = RECORDS/(stem+'.json')
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    report_path.with_suffix('.md').write_text(report_markdown(report))
    for path in (report_path,report_path.with_suffix('.md'),links_path,RECORDS/'COMPILE_STATUS.tsv'):
        hits,_ = privacy_scan(path.read_text(),relative(path))
        require(not hits,f'Generated report failed privacy check: {path.name}')
    if not preliminary and not issues:
        final_files = collect_payload(include_delivery=True,include_manifest=False)
        final_rows = payload_records(final_files)
        write_tsv(MANIFEST,final_rows,['archive','path','bytes','sha256'])
        hits,_ = privacy_scan(MANIFEST.read_text(),relative(MANIFEST))
        require(not hits,'Generated manifest failed privacy check')
    print(json.dumps(dict(status=report['status'],pdfs=len(pdfs),issues=len(issues),privacy_findings=len(privacy),report=relative(report_path))),flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preliminary',action='store_true',help='Check completed PDFs but leave README/visual-QA readiness pending; do not write a final manifest.')
    args = parser.parse_args()
    try:
        report = validate(preliminary=args.preliminary)
    except (DeliveryError,ValueError,KeyError,UnicodeError) as exc:
        # Exception messages may originate in a parser; strip runtime locations.
        message = str(exc).replace(str(ROOT),'[workspace]')
        message = EMAIL.sub('[e-mail address removed]',PERSONAL_PATH.sub('[local path removed]',message))
        print(json.dumps(dict(status='blocked',reason=message)),file=sys.stderr)
        raise SystemExit(1)
    raise SystemExit(1 if report['issues'] else 0)


if __name__ == '__main__':
    main()
