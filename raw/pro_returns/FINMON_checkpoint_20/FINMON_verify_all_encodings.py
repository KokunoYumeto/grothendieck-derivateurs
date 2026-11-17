#!/usr/bin/env python3
"""Verify every archived byte against the checkpoint manifest, once."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse,gzip,hashlib,io,json,lzma,subprocess,sys,tempfile,zipfile
sys.path.insert(0,str(Path(__file__).resolve().parent/'FINMON_work/code'))
from FINMON_row_codec import decode as decode_rows, ENCODING as ROW_ENCODING
from FINMON_png_codec import regenerate as regenerate_png, ENCODING as PNG_ENCODING
from FINMON_source_hash_codec import decode as decode_source_hashes, source_lines, restore_lines, ENCODING as SOURCE_HASH_ENCODING, COLUMN_ENCODING as SOURCE_HASH_COLUMN_ENCODING
from FINMON_category_certificate_codec import decode as decode_category_certificates, ENCODING as CATEGORY_CERTIFICATE_ENCODING, PYTHON_ENCODING as PYTHON_CATEGORY_ENCODING, regenerate_python as regenerate_category_python
from FINMON_json_column_codec import decode as decode_json_columns, ENCODING as JSON_COLUMN_ENCODING, PYTHON_ENCODING as PYTHON_COLUMN_ENCODING, regenerate_python_gzip
from FINMON_hdf_run_codec import decode as decode_hdf_runs, ENCODING as HDF_RUN_ENCODING
from FINMON_zip_source_codec import decode as decode_source_zip, ENCODING as SOURCE_ZIP_ENCODING
from FINMON_cpp_recipe_codec import regenerate as regenerate_cpp_recipe, ENCODING as CPP_RECIPE_ENCODING
from FINMON_cpp_prefix_recipe_codec import regenerate as regenerate_cpp_prefix_recipe, ENCODING as CPP_PREFIX_RECIPE_ENCODING
from FINMON_python_row_gzip_codec import regenerate as regenerate_python_row_gzip, ENCODING as PYTHON_ROW_GZIP_ENCODING
from FINMON_contact_png_codec import regenerate as regenerate_contact_png, ENCODING as CONTACT_PNG_ENCODING

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('number',type=int);parser.add_argument('archive',nargs='?',type=Path)
parser.add_argument('baseline_proof',nargs='?',type=Path)
parser.add_argument('--reuse-identical-encodings',action='store_true')
parser.add_argument('--cpp-recipe-preflight',type=Path)
parser.add_argument('--cpp-prefix-preflight',type=Path)
args=parser.parse_args();number=args.number;path=args.archive.resolve()if args.archive else root/f'FINMON_checkpoint_{number:02d}.zip'
hdf_proof=None;hdf_reused=0;outer_hdf_proofs=[]
reuse_identical=args.reuse_identical_encodings
assert not reuse_identical or args.baseline_proof is not None
previous_encodings={};previous_records={};reused_encodings=Counter()
if args.baseline_proof:
    proof_path=args.baseline_proof;hdf_proof=json.loads(proof_path.read_text())
    assert hdf_proof['result']=='PASS_REUSE_FULL_ORIGINAL_REGENERATION'
    previous_record=root/hdf_proof['source_verification_record']
    assert hashlib.sha256(previous_record.read_bytes()).hexdigest()==hdf_proof['source_verification_record_sha256']
    previous=json.loads(previous_record.read_text());assert previous['result']=='PASS'and previous['all_manifest_SHA256s_match']
    previous_archive=root/hdf_proof['source_archive'];ph=hashlib.sha256()
    with previous_archive.open('rb')as f:
        while b:=f.read(1<<20):ph.update(b)
    assert ph.hexdigest()==hdf_proof['source_archive_sha256']
    with zipfile.ZipFile(previous_archive)as pz:
        old_enc=json.loads(pz.read('FINMON_checkpoint_encodings.json'))['files']
        assert any(all(e.get(k)==hdf_proof[k]for k in ['encoding','original_bytes','original_sha256','encoded_bytes','encoded_sha256'])for e in old_enc)
        if reuse_identical:
            # The baseline must have regenerated every encoding itself. No
            # recursive or unverified cache chain is accepted here.
            assert not previous.get('encodings_verified_by_identical_previously_regenerated_bytes')
            assert not previous.get('hdf_run_encodings_verified_by_identical_previously_regenerated_bytes',0)
            assert not previous.get('hdf_run_encodings_verified_by_full_decoded_equality',[])
            assert not previous.get('deterministic_cpp_recipe_encodings_verified_by_pinned_completed_full_regeneration',[])
            assert not previous.get('deterministic_cpp_prefix_recipe_encodings_verified_by_pinned_completed_prefix_regeneration',[])
            previous_encodings={e['path']:e for e in old_enc}
            previous_records={r['path']:r for r in json.loads(pz.read('FINMON_checkpoint_manifest.json'))['files']}
def restoration_metadata(e):
    # Only the two physical location fields are irrelevant to decoding.
    # Source dependencies, compression parameters and all other metadata
    # must match literally before a previous proof can be reused.
    return {k:v for k,v in e.items()if k not in ('archive_entry','encoded_path')}
cpp_preflights={};cpp_preflight_used=[];cpp_packet_raw=None
if args.cpp_recipe_preflight:
    cpp_packet_raw=args.cpp_recipe_preflight.read_bytes();packet=json.loads(cpp_packet_raw)
    assert packet['format']=='FINMON_PINNED_FULL_CPP_RECIPE_REGENERATIONS_1'
    codec_path=Path(sys.modules[regenerate_cpp_recipe.__module__].__file__)
    assert hashlib.sha256(codec_path.read_bytes()).hexdigest()==packet['codec_sha256']
    audit_raw=packet['codec_audit_literal_utf8'].encode();assert hashlib.sha256(audit_raw).hexdigest()==packet['codec_audit_sha256']
    audit=json.loads(audit_raw);assert audit['status']=='PASS_LITERAL_EXACT_RECIPE_AND_INTEGRATION_AUDIT'
    assert audit['hashes']['code/checkpoint_cpp_recipe_codec.py']==packet['codec_sha256']
    for row in packet['files']:
        proof_raw=row['completed_proof_literal_utf8'].encode();meta_raw=row['metadata_literal_utf8'].encode()
        assert hashlib.sha256(proof_raw).hexdigest()==row['completed_proof_sha256']
        assert hashlib.sha256(meta_raw).hexdigest()==row['metadata_sha256']
        p=json.loads(proof_raw);m=json.loads(meta_raw)
        assert p['status']=='PASS_FULL_ORIGINAL_BYTE_REGENERATION'and p['actual_subprocess_exit_code']==0
        assert m['encoding']==CPP_RECIPE_ENCODING and m['self_contained']and m['regeneration_verified']and m['full_original_SHA256_verified']
        assert p['metadata_sha256']==row['metadata_sha256']and p['original_source']==m['path']==row['path']
        for key in ('original_bytes','original_sha256','encoded_bytes','encoded_sha256','actual_subprocess_exit_code','decoded_bytes','stdout_sha256'):
            assert p[key]==m[key]
        assert row['original_full_SHA256_rechecked']and row['encoded_full_SHA256_rechecked']
        assert row['path']not in cpp_preflights;cpp_preflights[row['path']]=(row,p,m)
cpp_prefix_preflights={};cpp_prefix_preflight_used=[];cpp_prefix_packet_raw=None
cpp_prefix_decoder_form=None
if args.cpp_prefix_preflight:
    cpp_prefix_packet_raw=args.cpp_prefix_preflight.read_bytes();packet=json.loads(cpp_prefix_packet_raw)
    assert packet['format']=='FINMON_PINNED_CPP_PREFIX_REGENERATIONS_1'
    audit_raw=packet['codec_audit_literal_utf8'].encode()
    assert hashlib.sha256(audit_raw).hexdigest()==packet['codec_audit_sha256']
    audit=json.loads(audit_raw)
    assert audit['status']=='PASS_LITERAL_EXACT_PREFIX_RECIPE_AND_INTEGRATION_AUDIT'
    prefix_raw=packet['prefix_codec_original_literal_utf8'].encode()
    assert hashlib.sha256(prefix_raw).hexdigest()==packet['prefix_codec_original_sha256']
    assert audit['hashes']['code/checkpoint_cpp_prefix_recipe_codec.py']==packet['prefix_codec_original_sha256']
    assert audit['hashes']['code/checkpoint_cpp_recipe_codec.py']==packet['base_codec_sha256']
    old_import=b'from checkpoint_cpp_recipe_codec import';new_import=b'from FINMON_cpp_recipe_codec import'
    assert packet['prefix_codec_known_import_rewrite']=={'before':old_import.decode(),'after':new_import.decode(),'count':1}
    assert prefix_raw.count(old_import)==1 and new_import not in prefix_raw
    standalone_raw=prefix_raw.replace(old_import,new_import,1)
    assert hashlib.sha256(standalone_raw).hexdigest()==packet['prefix_codec_standalone_sha256']
    prefix_module=sys.modules[regenerate_cpp_prefix_recipe.__module__]
    actual_prefix_raw=Path(prefix_module.__file__).read_bytes()
    assert actual_prefix_raw in (prefix_raw,standalone_raw)
    cpp_prefix_decoder_form='literal-original'if actual_prefix_raw==prefix_raw else 'exact-known-standalone-import-rewrite'
    assert prefix_module.full_regenerate is regenerate_cpp_recipe
    assert hashlib.sha256(Path(sys.modules[regenerate_cpp_recipe.__module__].__file__).read_bytes()).hexdigest()==packet['base_codec_sha256']
    for row in packet['files']:
        proof_raw=row['completed_proof_literal_utf8'].encode();meta_raw=row['metadata_literal_utf8'].encode()
        assert hashlib.sha256(proof_raw).hexdigest()==row['completed_proof_sha256']
        assert hashlib.sha256(meta_raw).hexdigest()==row['metadata_sha256']
        p=json.loads(proof_raw);m=json.loads(meta_raw)
        assert p['status']=='PASS_EVERY_FROZEN_PREFIX_BYTE_REGENERATED'and p['scientific_producer_completion_claimed']is False
        assert m['encoding']==CPP_PREFIX_RECIPE_ENCODING and m['prefix_only']is True
        assert m['self_contained']is True and m['regeneration_verified']is True and m['full_original_SHA256_verified']is True
        assert p['metadata_sha256']==row['metadata_sha256']and p['original_source']==m['path']==row['path']
        for key in ('original_bytes','original_sha256','encoded_path','encoded_bytes','encoded_sha256'):
            assert p[key]==m[key]
        stats=p['stats'];assert stats['prefix_bytes_emitted']==m['original_bytes']
        assert stats['exact_requested_prefix_reconstructed']is True and stats['remaining_generator_closed']is True
        assert stats['scientific_producer_completion_claimed']is False
        for key,value in stats.items():assert m[key]==value
        original=row['source_original_record']
        assert 'archive_encoding'not in original and original['path']==m['path']
        assert original['bytes']==m['original_bytes']and original['sha256']==m['original_sha256']
        assert row['source_archive']==str(Path(p['archive']).resolve())
        for key in ('source_archive_sha256','source_manifest_sha256'):
            assert len(row[key])==64 and all(c in '0123456789abcdef'for c in row[key])
        assert row['original_full_prefix_SHA256_rechecked']is True and row['encoded_full_SHA256_rechecked']is True
        assert row['path']not in cpp_prefix_preflights;cpp_prefix_preflights[row['path']]=(row,p,m)
with zipfile.ZipFile(path)as z:
    names=z.namelist();assert len(names)==len(set(names))
    manifest=json.loads(z.read('FINMON_checkpoint_manifest.json'))
    assert manifest['checkpoint']==number
    records=manifest['files']
    if cpp_packet_raw is not None:assert z.read('FINMON_recipe_preflight_proofs.json')==cpp_packet_raw
    if cpp_prefix_packet_raw is not None:assert z.read('FINMON_prefix_recipe_preflight_proofs.json')==cpp_prefix_packet_raw
    encoded_manifest=json.loads(z.read('FINMON_checkpoint_encodings.json'))if 'FINMON_checkpoint_encodings.json'in names else {'files':[]}
    encodings={r['path']:r for r in encoded_manifest['files']}
    assert set(names)=={r.get('archive_encoding',r['path'])for r in records}|{'FINMON_checkpoint_manifest.json'}|({'FINMON_checkpoint_encodings.json','FINMON_RESTORE_FIRST.txt'}if encodings else set())
    record_by_path={r['path']:r for r in records}
    contact_png_cached_entry=None;contact_png_cached_raw=None
    def contact_source_png(logical_path):
        global contact_png_cached_entry,contact_png_cached_raw
        source_record=record_by_path[logical_path]
        if 'archive_encoding' not in source_record:
            original=z.read(logical_path)
        else:
            source_encoding=encodings[logical_path]
            assert source_encoding['encoding']==PNG_ENCODING,logical_path
            assert source_encoding['original_bytes']==source_record['bytes']
            assert source_encoding['original_sha256']==source_record['sha256']
            entry=source_encoding['archive_entry']
            assert entry==source_record['archive_encoding']
            if contact_png_cached_entry!=entry:
                packed=z.read(entry)
                assert len(packed)==source_encoding['encoded_bytes']
                assert hashlib.sha256(packed).hexdigest()==source_encoding['encoded_sha256']==source_record['encoded_sha256']
                contact_png_cached_raw=lzma.decompress(packed)
                contact_png_cached_entry=entry
            original=bytes(regenerate_png(contact_png_cached_raw,source_encoding))
        assert len(original)==source_record['bytes'] and hashlib.sha256(original).hexdigest()==source_record['sha256']
        return original
    def referenced_source(path):
        r=record_by_path[path]
        if 'archive_encoding'in r:
            e=encodings[path];assert e['encoding']==ROW_ENCODING
            with z.open(e['archive_entry'])as stream:yield from source_lines(decode_rows(stream))
        else:
            with z.open(path)as stream:yield from stream
    if encodings:z.read('FINMON_RESTORE_FIRST.txt')
    total=0;last_png_entry=None;last_png_raw=None;last_shared_entry=None;last_shared_raw=None
    verified_encoded={}
    for index,r in enumerate(sorted(records,key=lambda r:(r.get('archive_encoding',r['path']),r['path'])),1):
        if index==1 or index%1000==0:
            print(json.dumps({'progress_payload':index,'total_payloads':len(records),'current_path':r['path'],'verified_original_bytes_so_far':total,'reused_identical_encodings':sum(reused_encodings.values()),'utc':datetime.now(timezone.utc).isoformat()}),flush=True)
        if 'archive_encoding'in r:
            e=encodings[r['path']]
            assert e['original_sha256']==r['sha256'] and e['original_bytes']==r['bytes']
            assert e['archive_entry']==r['archive_encoding']
            if e['archive_entry']not in verified_encoded:
                h=hashlib.sha256()
                with z.open(e['archive_entry'])as f:
                    while b:=f.read(1<<20):h.update(b)
                verified_encoded[e['archive_entry']]=h.hexdigest()
            assert verified_encoded[e['archive_entry']]==r['encoded_sha256']==e['encoded_sha256']
            if 'source_path'in e:
                assert record_by_path[e['source_path']]['sha256']==e['source_sha256']
            if e['encoding']==SOURCE_ZIP_ENCODING:
                for member in e['members']:
                    source_record=record_by_path[member['source_path']]
                    assert source_record['sha256']==member['source_sha256']
                    assert source_record['bytes']==member['source_bytes']
            old=previous_encodings.get(r['path']);old_record=previous_records.get(r['path'])
            if (e['encoding'] not in (CPP_PREFIX_RECIPE_ENCODING,CONTACT_PNG_ENCODING) and old is not None and old_record is not None
                and old_record['sha256']==r['sha256'] and old_record['bytes']==r['bytes']
                and restoration_metadata(old)==restoration_metadata(e)):
                reused_encodings[e['encoding']]+=1
                if e['encoding']==HDF_RUN_ENCODING:hdf_reused+=1
                total+=r['bytes'];continue
            if e['encoding']=='xz-shared-raw-v1':
                if last_shared_entry!=e['archive_entry']:
                    last_shared_entry=e['archive_entry'];last_shared_raw=lzma.decompress(z.read(last_shared_entry))
                assert len(last_shared_raw)==e['shared_decoded_bytes']
                begin=e['decoded_offset'];data=last_shared_raw[begin:begin+r['bytes']]
                assert len(data)==r['bytes']and hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']=='raw-xz-v1':
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as member,lzma.LZMAFile(member,'rb')as stream:
                    while b:=stream.read(1<<20):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==HDF_RUN_ENCODING:
                if old is not None and e.get('outer_xz_recompression'):
                    ignored={'archive_entry','encoded_path','encoded_bytes','encoded_sha256','outer_xz_recompression'}
                    compatible={k:v for k,v in old.items()if k not in ignored}=={k:v for k,v in e.items()if k not in ignored}
                    proof=e['outer_xz_recompression']
                    if compatible and proof['previous_encoded_sha256']==old['encoded_sha256']:
                        # The baseline archive passed full original regeneration.
                        # Compare EVERY decoded codec-input byte, not just metadata,
                        # before reusing that exact deterministic-decoder result.
                        decoded_hash=hashlib.sha256();decoded_count=0
                        with zipfile.ZipFile(previous_archive)as baseline:
                            with baseline.open(old['archive_entry'])as before,z.open(e['archive_entry'])as after:
                                with lzma.LZMAFile(before,'rb')as a,lzma.LZMAFile(after,'rb')as b:
                                    while block:=a.read(1<<20):
                                        assert b.read(len(block))==block
                                        decoded_hash.update(block);decoded_count+=len(block)
                                    assert not b.read(1)
                        assert decoded_count==proof['identical_full_decoded_bytes']
                        assert decoded_hash.hexdigest()==proof['identical_full_decoded_sha256']
                        outer_hdf_proofs.append({'path':r['path'],'full_decoded_bytes_compared':decoded_count,
                            'full_decoded_sha256':decoded_hash.hexdigest(),'baseline_encoded_sha256':old['encoded_sha256'],
                            'current_encoded_sha256':e['encoded_sha256'],'original_sha256':r['sha256']})
                        hdf_reused+=1;total+=r['bytes'];continue
                if hdf_proof is not None and all(e.get(k)==hdf_proof[k]for k in ['encoding','original_bytes','original_sha256','encoded_bytes','encoded_sha256']):
                    # Actual current encoded member bytes were SHA-checked above.
                    # These identical bytes already passed full original-file
                    # regeneration in the completed verified previous archive.
                    hdf_reused+=1;total+=r['bytes'];continue
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as stream:
                    for b in decode_hdf_runs(stream):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==SOURCE_ZIP_ENCODING:
                h=hashlib.sha256();decoded=0
                def zip_source(path):
                    source_record=record_by_path[path]
                    if 'archive_encoding' not in source_record:data=z.read(path)
                    else:
                        source_encoding=encodings[path]
                        with z.open(source_encoding['archive_entry'])as source_stream:
                            if source_encoding['encoding']==HDF_RUN_ENCODING:
                                data=b''.join(decode_hdf_runs(source_stream))
                            elif source_encoding['encoding']=='raw-xz-v1':
                                data=lzma.decompress(source_stream.read())
                            elif source_encoding['encoding']=='xz-shared-raw-v1':
                                raw=lzma.decompress(source_stream.read())
                                begin=source_encoding['decoded_offset'];data=raw[begin:begin+source_record['bytes']]
                            else:raise AssertionError(('Unsupported ZIP source encoding',path,source_encoding['encoding']))
                    assert len(data)==source_record['bytes']and hashlib.sha256(data).hexdigest()==source_record['sha256']
                    return data
                with z.open(e['archive_entry'])as stream:
                    for b in decode_source_zip(stream,zip_source):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding'] in (SOURCE_HASH_ENCODING,SOURCE_HASH_COLUMN_ENCODING):
                assert record_by_path[e['source_path']]['sha256']==e['source_sha256']
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as stream:
                    source=referenced_source(e['source_path'])
                    blocks=decode_source_hashes(stream,source) if e['encoding']==SOURCE_HASH_ENCODING else restore_lines(source_lines(decode_json_columns(stream)),source)
                    for b in blocks:h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']=='source-derived-category-jsonl-xz-v1':
                assert record_by_path[e['source_path']]['sha256']==e['source_sha256']
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as stream:
                    for b in decode_category_certificates(stream,referenced_source(e['source_path']),e):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']=='literal-json-columns-xz-v1':
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as stream:
                    for b in decode_json_columns(stream):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==ROW_ENCODING:
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as stream:
                    for b in decode_rows(stream):h.update(b);decoded+=len(b)
                assert decoded==r['bytes'] and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==PNG_ENCODING:
                if last_png_entry!=e['archive_entry']:
                    last_png_entry=e['archive_entry'];last_png_raw=lzma.decompress(z.read(last_png_entry))
                data=regenerate_png(last_png_raw,e)
                assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==CONTACT_PNG_ENCODING:
                for dependency in e['source_pages']:
                    source_record=record_by_path[dependency['path']]
                    assert source_record['bytes']==dependency['bytes'] and source_record['sha256']==dependency['sha256']
                recipe=lzma.decompress(z.read(e['archive_entry']))
                data=regenerate_contact_png(recipe,e,contact_source_png)
                assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==PYTHON_CATEGORY_ENCODING:
                assert e['source_gzip']
                source_record=record_by_path[e['source_path']]
                if 'archive_encoding' not in source_record:
                    source_bytes=z.read(e['source_path'])
                else:
                    source_encoding=encodings[e['source_path']]
                    assert source_encoding['encoding']==PYTHON_ROW_GZIP_ENCODING,e['source_path']
                    encoded_source=z.read(source_encoding['archive_entry'])
                    assert len(encoded_source)==source_encoding['encoded_bytes']and hashlib.sha256(encoded_source).hexdigest()==source_encoding['encoded_sha256']
                    with io.BytesIO(encoded_source)as source_stream:
                        source_bytes=b''.join(regenerate_python_row_gzip(source_stream,source_encoding))
                sh=hashlib.sha256();sh.update(source_bytes)
                assert sh.hexdigest()==e['source_sha256'] and len(source_bytes)==source_record['bytes']
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as member,gzip.GzipFile(fileobj=io.BytesIO(source_bytes),mode='rb')as src:
                    for b in regenerate_category_python(member,iter(src),e):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==PYTHON_ROW_GZIP_ENCODING:
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as member:
                    for b in regenerate_python_row_gzip(member,e):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==CPP_PREFIX_RECIPE_ENCODING:
                if r['path']in cpp_prefix_preflights:
                    row,p,m=cpp_prefix_preflights[r['path']]
                    assert restoration_metadata(m)==restoration_metadata(e)
                    assert z.getinfo(e['archive_entry']).file_size==p['encoded_bytes']
                    assert p['original_bytes']==r['bytes']and p['original_sha256']==r['sha256']
                    cpp_prefix_preflight_used.append({'path':r['path'],'completed_proof_sha256':row['completed_proof_sha256'],
                        'metadata_sha256':row['metadata_sha256'],'encoded_sha256':e['encoded_sha256'],
                        'original_sha256':r['sha256'],'original_bytes':r['bytes'],
                        'scientific_producer_completion_claimed':False,'fresh_regeneration_claimed':False})
                    total+=r['bytes'];continue
                h=hashlib.sha256();decoded=0;prefix_stats={}
                with z.open(e['archive_entry'])as member:
                    for b in regenerate_cpp_prefix_recipe(member,e,scratch_dir=root,stats=prefix_stats):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                assert prefix_stats['exact_requested_prefix_reconstructed']and not prefix_stats['scientific_producer_completion_claimed']
                total+=r['bytes'];continue
            if e['encoding']==CPP_RECIPE_ENCODING:
                if r['path']in cpp_preflights:
                    row,p,m=cpp_preflights[r['path']]
                    assert restoration_metadata(m)==restoration_metadata(e)
                    assert z.getinfo(e['archive_entry']).file_size==p['encoded_bytes']
                    assert p['original_bytes']==r['bytes']and p['original_sha256']==r['sha256']
                    cpp_preflight_used.append({'path':r['path'],'completed_proof_sha256':row['completed_proof_sha256'],
                        'metadata_sha256':row['metadata_sha256'],'encoded_sha256':e['encoded_sha256'],
                        'original_sha256':r['sha256'],'original_bytes':r['bytes']})
                    total+=r['bytes'];continue
                h=hashlib.sha256();decoded=0
                with z.open(e['archive_entry'])as member:
                    for b in regenerate_cpp_recipe(member,e,scratch_dir=root):h.update(b);decoded+=len(b)
                assert decoded==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']==PYTHON_COLUMN_ENCODING:
                h=hashlib.sha256();regenerated=0
                with z.open(e['archive_entry'])as member:
                    for block in regenerate_python_gzip(member,e):h.update(block);regenerated+=len(block)
                assert regenerated==r['bytes']and h.hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            if e['encoding']=='xz-decoded-python-gzip-v1':
                if e.get('shared_decoded_bytes') is not None:
                    if last_shared_entry!=e['archive_entry']:
                        last_shared_entry=e['archive_entry'];last_shared_raw=lzma.decompress(z.read(last_shared_entry))
                    assert len(last_shared_raw)==e['shared_decoded_bytes']
                    begin=e['decoded_offset'];raw=last_shared_raw[begin:begin+e['decoded_bytes']]
                else:raw=lzma.decompress(z.read(e['archive_entry']))
                assert len(raw)==e['decoded_bytes'];buf=io.BytesIO()
                with gzip.GzipFile(fileobj=buf,mode='wb',filename='',mtime=0,compresslevel=e['compresslevel'])as f:
                    f.write(raw)
                    if e.get('sync_flush_before_close'):f.flush()
                data=bytes.fromhex(e['original_header_hex'])+buf.getvalue()[10:]
                if e.get('restore_exact_prefix'):
                    data=data[:e['regenerated_prefix_bytes']]+bytes.fromhex(e['literal_gzip_suffix_hex'])
                assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
                total+=r['bytes'];continue
            assert e['encoding'] in ('xz-decoded-gnu-gzip-1','transpose-xz-decoded-gnu-gzip-1',CATEGORY_CERTIFICATE_ENCODING,JSON_COLUMN_ENCODING)
            with tempfile.TemporaryDirectory(prefix='.finmon-verify-',dir=root)as td:
                generated=Path(td)/'regenerated.gz';decoded=0
                with generated.open('xb')as out:
                    proc=subprocess.Popen(['gzip','-'+str(e.get('gzip_compresslevel',1)),'-n','-c'],stdin=subprocess.PIPE,stdout=out)
                    try:
                        if e['encoding']==CATEGORY_CERTIFICATE_ENCODING:
                            assert record_by_path[e['source_path']]['sha256']==e['source_sha256']
                            with z.open(e['archive_entry'])as member:
                                for b in decode_category_certificates(member,referenced_source(e['source_path']),e):decoded+=len(b);proc.stdin.write(b)
                        elif e['encoding']==JSON_COLUMN_ENCODING:
                            with z.open(e['archive_entry'])as member:
                                for b in decode_json_columns(member):decoded+=len(b);proc.stdin.write(b)
                        elif e['encoding']=='transpose-xz-decoded-gnu-gzip-1':
                            with z.open(e['archive_entry'])as member:
                                for b in decode_rows(member):decoded+=len(b);proc.stdin.write(b)
                        else:
                            with z.open(e['archive_entry'])as member,lzma.LZMAFile(member,'rb')as stream:
                                while b:=stream.read(1<<20):decoded+=len(b);proc.stdin.write(b)
                        proc.stdin.close();assert proc.wait()==0
                    except BaseException:
                        proc.kill();proc.wait();raise
                header=bytes.fromhex(e['original_header_hex']);h=hashlib.sha256(header)
                with generated.open('rb')as f:
                    f.seek(10)
                    suffix=bytes.fromhex(e.get('literal_gzip_suffix_hex',''))
                    if 'regenerated_prefix_bytes'in e:
                        assert e['regenerated_prefix_bytes']+len(suffix)==r['bytes']
                        remaining=e['regenerated_prefix_bytes']-len(header)
                        assert remaining>=0
                    else:remaining=r['bytes']-len(header) if e.get('restore_exact_prefix') else None
                    while remaining is None or remaining:
                        b=f.read((1<<20) if remaining is None else min(1<<20,remaining))
                        if not b:break
                        h.update(b)
                        if remaining is not None:remaining-=len(b)
                    assert remaining in (None,0)
                    h.update(suffix)
                assert h.hexdigest()==r['sha256'],r['path']
                if e.get('restore_exact_prefix'):assert generated.stat().st_size-10+len(header)>=e.get('regenerated_prefix_bytes',r['bytes'])
                else:assert generated.stat().st_size-10+len(header)==r['bytes']
                assert decoded==e['decoded_bytes']
            total+=r['bytes']
            continue
        info=z.getinfo(r['path']);assert info.file_size==r['bytes']
        h=hashlib.sha256();size=0
        with z.open(info)as f:
            while b:=f.read(1<<20):h.update(b);size+=len(b)
        assert size==r['bytes'] and h.hexdigest()==r['sha256'],r['path']
        total+=size
def full_count(kinds):
    if isinstance(kinds,str):kinds=(kinds,)
    return sum(e['encoding']in kinds for e in encodings.values())-sum(reused_encodings[k]for k in kinds)
assert set(cpp_preflights)=={r['path']for r in cpp_preflight_used}
assert set(cpp_prefix_preflights)=={r['path']for r in cpp_prefix_preflight_used}
result={'result':'PASS','archive':str(path),'archive_bytes':path.stat().st_size,
        'payload_files':len(records),'uncompressed_payload_bytes':total,
        'reversible_gzip_encodings_verified_by_full_regeneration':full_count(('xz-decoded-gnu-gzip-1','transpose-xz-decoded-gnu-gzip-1')),
        'reversible_row_transposes_verified_by_full_decode':full_count(ROW_ENCODING),
        'reversible_python_gzip_encodings_verified_by_full_regeneration':full_count(('xz-decoded-python-gzip-v1',PYTHON_COLUMN_ENCODING)),
        'transposed_python_gzip_encodings_verified_by_full_regeneration':full_count(PYTHON_ROW_GZIP_ENCODING),
        'deterministic_cpp_recipe_encodings_verified_by_full_original_byte_regeneration':full_count(CPP_RECIPE_ENCODING)-len(cpp_preflight_used),
        'deterministic_cpp_prefix_recipe_encodings_verified_by_every_frozen_prefix_byte':full_count(CPP_PREFIX_RECIPE_ENCODING)-len(cpp_prefix_preflight_used),
        'deterministic_cpp_prefix_recipe_encodings_verified_by_pinned_completed_prefix_regeneration':cpp_prefix_preflight_used,
        'cpp_prefix_preflight_packet_sha256':hashlib.sha256(cpp_prefix_packet_raw).hexdigest()if cpp_prefix_packet_raw is not None else None,
        'cpp_prefix_preflight_decoder_form':cpp_prefix_decoder_form,
        'deterministic_cpp_recipe_encodings_verified_by_pinned_completed_full_regeneration':cpp_preflight_used,
        'cpp_preflight_packet_sha256':hashlib.sha256(cpp_packet_raw).hexdigest()if cpp_packet_raw is not None else None,
        'reversible_PNG_encodings_verified_by_full_regeneration':full_count(PNG_ENCODING),
        'retained_page_contact_PNG_encodings_verified_by_full_regeneration':full_count(CONTACT_PNG_ENCODING),
        'source_hash_elisions_verified_by_full_regeneration':full_count((SOURCE_HASH_ENCODING,SOURCE_HASH_COLUMN_ENCODING)),
        'raw_xz_encodings_verified_by_full_decode':full_count('raw-xz-v1'),
        'shared_raw_encodings_verified_by_full_decode':full_count('xz-shared-raw-v1'),
        'source_derived_category_gzip_encodings_verified':full_count(CATEGORY_CERTIFICATE_ENCODING),
        'source_derived_python_category_gzip_encodings_verified':full_count(PYTHON_CATEGORY_ENCODING),
        'source_derived_plain_category_encodings_verified':full_count('source-derived-category-jsonl-xz-v1'),
        'literal_json_column_encodings_verified':full_count((JSON_COLUMN_ENCODING,PYTHON_COLUMN_ENCODING)),
        'plain_literal_json_column_encodings_verified':full_count('literal-json-columns-xz-v1'),
        'hdf_run_encodings_verified_by_full_original_byte_regeneration':sum(e['encoding']==HDF_RUN_ENCODING for e in encodings.values())-hdf_reused,
        'hdf_run_encodings_verified_by_identical_previously_regenerated_bytes':hdf_reused-len(outer_hdf_proofs),
        'hdf_run_encodings_verified_by_full_decoded_equality':outer_hdf_proofs,
        'hdf_full_regeneration_proof':str(proof_path) if hdf_reused else None,
        'source_derived_ZIP_encodings_verified_by_full_original_byte_regeneration':full_count(SOURCE_ZIP_ENCODING),
        'encodings_verified_by_identical_previously_regenerated_bytes':dict(reused_encodings),
        'identical_encoding_reuse_scope':'Actual complete encoded bytes, every decoding metadata field except physical path, original full SHA256 and original length matched against a fully regenerated baseline archive; baseline archive and completed proof record independently SHA256-checked.'if reused_encodings else None,
        'all_member_CRCs_valid':True,'all_manifest_SHA256s_match':True,
        'verified_utc':datetime.now(timezone.utc).isoformat()}
suffix='_repacked' if args.archive else ''
target=root/'FINMON_work/code/outputs'/f'checkpoint_{number:02d}{suffix}_verified.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
