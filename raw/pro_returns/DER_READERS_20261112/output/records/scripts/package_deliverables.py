#!/usr/bin/env python3
"""Create the three deterministic ZIPs after a passing final delivery validation.

Run validate_delivery.py first, after all PDFs, the README, and PDF_VISUAL_QA.md
are final. Every archived byte is checked against DELIVERY_MANIFEST.tsv. The
manifest excludes itself; an external receipt hashes each complete ZIP.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
import zipfile

import validate_delivery as V

csv.field_size_limit(100000000)
FIXED_ZIP_TIME = (1980,1,1,0,0,0)
MAX_ARCHIVE_BYTES = 100000000


def package(destination: Path):
    V.compile_gate()
    report_path = V.RECORDS/'DELIVERY_VALIDATION.json'
    V.require(report_path.is_file(),'Run final validate_delivery.py before packaging.')
    report = json.loads(report_path.read_text())
    V.require(report.get('status') == 'pass' and report.get('preliminary') is False and not report.get('issues'),
              'Only a passing final delivery validation authorizes packaging.')
    base = V.payload_records(V.collect_payload(include_delivery=False,include_manifest=False))
    V.require(V.fingerprint(base) == report.get('input_payload_fingerprint'),'Payload changed after final validation; rerun validate_delivery.py.')
    V.require(V.MANIFEST.is_file(),'Final delivery manifest is missing.')
    with V.MANIFEST.open(newline='') as f:
        manifest = list(csv.DictReader(f,delimiter='\t'))
    expected = {(r['archive'],r['path']):(int(r['bytes']),r['sha256']) for r in manifest}
    V.require(len(expected)==len(manifest),'Duplicate manifest rows.')
    files = V.collect_payload(include_delivery=True,include_manifest=True)
    actual_without_self = {(e.archive,e.archive_path) for e in files if e.source != V.MANIFEST}
    V.require(set(expected)==actual_without_self,'Payload member set differs from the final manifest.')
    for row in V.payload_records([e for e in files if e.source != V.MANIFEST]):
        V.require(expected[(row['archive'],row['path'])] == (row['bytes'],row['sha256']),
                  f"Payload bytes changed after manifest creation: {row['path']}")
    destination.mkdir(parents=True,exist_ok=True)
    receipts = []
    for archive in V.ARCHIVES:
        members = [e for e in files if e.archive==archive]
        temporary = destination/(archive+'.tmp')
        final = destination/archive
        with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9,allowZip64=True) as z:
            for entry in sorted(members,key=lambda e:e.archive_path):
                info = zipfile.ZipInfo(entry.archive_path,FIXED_ZIP_TIME)
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info,entry.source.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
        V.require(temporary.stat().st_size < MAX_ARCHIVE_BYTES,f'Archive exceeds 100 MB: {archive}')
        member_receipts = []
        with zipfile.ZipFile(temporary,'r') as z:
            V.require(z.testzip() is None,f'ZIP CRC verification failed: {archive}')
            V.require(z.namelist()==sorted(e.archive_path for e in members),f'ZIP member list differs: {archive}')
            V.require(len(z.namelist())==len(set(z.namelist())),f'Duplicate ZIP member: {archive}')
            by_name = {e.archive_path:e for e in members}
            for info in z.infolist():
                entry = by_name[info.filename]
                data = z.read(info)
                digest = hashlib.sha256(data).hexdigest()
                if entry.source == V.MANIFEST:
                    target = entry.source.stat().st_size,V.sha_file(entry.source)
                else:
                    target = expected[(archive,info.filename)]
                V.require((len(data),digest)==target,f'Reopened ZIP member differs: {archive}/{info.filename}')
                V.require(info.date_time==FIXED_ZIP_TIME,f'ZIP timestamp is nondeterministic: {archive}/{info.filename}')
                member_receipts.append(dict(path=info.filename,bytes=len(data),sha256=digest,crc32=f'{info.CRC:08x}'))
        temporary.replace(final)
        receipts.append(dict(archive=archive,bytes=final.stat().st_size,sha256=V.sha_file(final),members=len(member_receipts),
                             below_100_MB=True,crc_verified=True,all_member_bytes_and_hashes_verified=True,member_receipts=member_receipts))
        print(json.dumps({k:v for k,v in receipts[-1].items() if k!='member_receipts'}),flush=True)
    receipt = dict(format='DER delivery archive receipt 1',archives=receipts,
        validation_sha256=V.sha_file(report_path),manifest_sha256=V.sha_file(V.MANIFEST),
        deterministic_zip=dict(order='lexicographic archive member names',timestamp=list(FIXED_ZIP_TIME),permissions='regular file 0644',compression='DEFLATE level 9'),
        cycle_avoidance='This outer archive receipt is outside all three ZIPs. The manifest excludes its own row; each reopened ZIP verifies the manifest bytes too.')
    receipt_path = destination/'DER_READERS_ARCHIVES.json'
    receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination',type=Path,default=V.ROOT/'deliverables')
    args = parser.parse_args()
    try:
        package(args.destination)
    except (V.DeliveryError,ValueError,KeyError,UnicodeError,zipfile.BadZipFile) as exc:
        message = str(exc).replace(str(V.ROOT),'[workspace]')
        message = V.EMAIL.sub('[e-mail address removed]',V.PERSONAL_PATH.sub('[local path removed]',message))
        print(json.dumps(dict(status='blocked',reason=message)),file=sys.stderr)
        raise SystemExit(1)


if __name__=='__main__':
    main()
