#!/usr/bin/env python3
"""Restore byte-identical gzip logs after extracting a FINMON checkpoint.

Usage: python FINMON_work/code/restore_checkpoint_encodings.py [EXTRACTED_ROOT]
Requires GNU gzip compatible with the recorded version. Self-contained C++
stdout recipes also require g++ with C++17 support and compatible zlib;
reconstruction of the largest records can take several minutes. Every output is
verified against its original SHA256 before it is placed at its old path.
Already-correct files are kept; conflicting existing files are never changed.
"""
from pathlib import Path
import gzip,hashlib,io,json,lzma,subprocess,sys
sys.path.insert(0,str(Path(__file__).resolve().parent/'FINMON_work/code'))
from FINMON_row_codec import decode as decode_rows, ENCODING as ROW_ENCODING
from FINMON_png_codec import regenerate as regenerate_png, ENCODING as PNG_ENCODING
from FINMON_source_hash_codec import decode as decode_source_hashes, restore_lines, source_lines, ENCODING as SOURCE_HASH_ENCODING, COLUMN_ENCODING as SOURCE_HASH_COLUMN_ENCODING
from FINMON_category_certificate_codec import decode as decode_category_certificates, ENCODING as CATEGORY_CERTIFICATE_ENCODING, PYTHON_ENCODING as PYTHON_CATEGORY_ENCODING, regenerate_python as regenerate_category_python
from FINMON_json_column_codec import decode as decode_json_columns, ENCODING as JSON_COLUMN_ENCODING, PYTHON_ENCODING as PYTHON_COLUMN_ENCODING, regenerate_python_gzip
from FINMON_hdf_run_codec import decode as decode_hdf_runs, ENCODING as HDF_RUN_ENCODING
from FINMON_zip_source_codec import decode as decode_source_zip, ENCODING as SOURCE_ZIP_ENCODING
from FINMON_cpp_recipe_codec import regenerate as regenerate_cpp_recipe, ENCODING as CPP_RECIPE_ENCODING
from FINMON_cpp_prefix_recipe_codec import regenerate as regenerate_cpp_prefix_recipe, ENCODING as CPP_PREFIX_RECIPE_ENCODING
from FINMON_python_row_gzip_codec import regenerate as regenerate_python_row_gzip, ENCODING as PYTHON_ROW_GZIP_ENCODING
from FINMON_contact_png_codec import regenerate as regenerate_contact_png, ENCODING as CONTACT_PNG_ENCODING

ROOT=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path(__file__).resolve().parent
manifest=json.loads((ROOT/'FINMON_checkpoint_encodings.json').read_text())

def sha(path):
 h=hashlib.sha256()
 with path.open('rb')as f:
  while b:=f.read(1<<20):h.update(b)
 return h.hexdigest()

last_png_entry=None;last_png_raw=None;last_shared_entry=None;last_shared_raw=None
verified_encoded={}
for record in sorted(manifest['files'],key=lambda r:(r['encoding'] in (SOURCE_HASH_ENCODING,SOURCE_HASH_COLUMN_ENCODING,SOURCE_ZIP_ENCODING,CATEGORY_CERTIFICATE_ENCODING,PYTHON_CATEGORY_ENCODING,CONTACT_PNG_ENCODING,'source-derived-category-jsonl-xz-v1'),r['archive_entry'],r['path'])):
 dest=ROOT/record['path'];encoded=ROOT/record['archive_entry']
 if encoded not in verified_encoded:verified_encoded[encoded]=sha(encoded)
 assert verified_encoded[encoded]==record['encoded_sha256'],encoded
 if dest.exists():
  assert sha(dest)==record['original_sha256'],f'Conflicting file: {dest}'
  print('Already verified:',record['path']);continue
 dest.parent.mkdir(parents=True,exist_ok=True)
 if record['encoding']=='xz-shared-raw-v1':
  if last_shared_entry!=encoded:
   last_shared_entry=encoded;last_shared_raw=lzma.decompress(encoded.read_bytes())
  assert len(last_shared_raw)==record['shared_decoded_bytes']
  begin=record['decoded_offset'];data=last_shared_raw[begin:begin+record['original_bytes']]
  assert len(data)==record['original_bytes']and hashlib.sha256(data).hexdigest()==record['original_sha256']
  restored=dest.with_name(dest.name+'.restore.tmp');restored.write_bytes(data);restored.rename(dest)
  print('Restored and verified:',record['path']);continue
 if record['encoding']=='raw-xz-v1':
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out,lzma.open(encoded,'rb')as inp:
   while block:=inp.read(1<<20):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==HDF_RUN_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in decode_hdf_runs(encoded):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==SOURCE_ZIP_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in decode_source_zip(encoded,lambda p:(ROOT/p).read_bytes()):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding'] in (SOURCE_HASH_ENCODING,SOURCE_HASH_COLUMN_ENCODING):
  source=ROOT/record['source_path'];assert sha(source)==record['source_sha256']
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out,source.open('rb')as stream:
   blocks=decode_source_hashes(encoded,iter(stream)) if record['encoding']==SOURCE_HASH_ENCODING else restore_lines(source_lines(decode_json_columns(encoded)),iter(stream))
   for block in blocks:out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']=='source-derived-category-jsonl-xz-v1':
  source=ROOT/record['source_path'];assert sha(source)==record['source_sha256']
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out,source.open('rb')as stream:
   for block in decode_category_certificates(encoded,iter(stream),record):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==PNG_ENCODING:
  if last_png_entry!=encoded:
   last_png_entry=encoded;last_png_raw=lzma.decompress(encoded.read_bytes())
  data=regenerate_png(last_png_raw,record)
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as f:f.write(data)
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==CONTACT_PNG_ENCODING:
  data=regenerate_contact_png(lzma.decompress(encoded.read_bytes()),record,lambda p:(ROOT/p).read_bytes())
  assert len(data)==record['original_bytes'] and hashlib.sha256(data).hexdigest()==record['original_sha256']
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as f:f.write(data)
  restored.rename(dest);print('Restored and verified retained-page contact:',record['path']);continue
 if record['encoding']=='literal-json-columns-xz-v1':
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in decode_json_columns(encoded):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified literal JSON:',record['path']);continue
 if record['encoding']==ROW_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in decode_rows(encoded):out.write(block)
  assert restored.stat().st_size==record['original_bytes'] and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==PYTHON_CATEGORY_ENCODING:
  source=ROOT/record['source_path'];assert sha(source)==record['source_sha256'] and record['source_gzip']
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out,gzip.open(source,'rb')as src:
   for block in regenerate_category_python(encoded,iter(src),record):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==PYTHON_ROW_GZIP_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in regenerate_python_row_gzip(encoded,record):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified transposed gzip:',record['path']);continue
 if record['encoding']==CPP_PREFIX_RECIPE_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in regenerate_cpp_prefix_recipe(encoded,record,scratch_dir=ROOT):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified frozen prefix:',record['path']);continue
 if record['encoding']==CPP_RECIPE_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in regenerate_cpp_recipe(encoded,record,scratch_dir=ROOT):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']==PYTHON_COLUMN_ENCODING:
  restored=dest.with_name(dest.name+'.restore.tmp')
  with restored.open('xb')as out:
   for block in regenerate_python_gzip(encoded,record):out.write(block)
  assert restored.stat().st_size==record['original_bytes']and sha(restored)==record['original_sha256']
  restored.rename(dest);print('Restored and verified:',record['path']);continue
 if record['encoding']=='xz-decoded-python-gzip-v1':
  if record.get('shared_decoded_bytes') is not None:
   if last_shared_entry!=encoded:last_shared_entry=encoded;last_shared_raw=lzma.decompress(encoded.read_bytes())
   assert len(last_shared_raw)==record['shared_decoded_bytes']
   begin=record['decoded_offset'];raw=last_shared_raw[begin:begin+record['decoded_bytes']]
  else:raw=lzma.decompress(encoded.read_bytes())
  assert len(raw)==record['decoded_bytes'];buf=io.BytesIO()
  with gzip.GzipFile(fileobj=buf,mode='wb',filename='',mtime=0,compresslevel=record['compresslevel'])as f:
   f.write(raw)
   if record.get('sync_flush_before_close'):f.flush()
  data=bytes.fromhex(record['original_header_hex'])+buf.getvalue()[10:]
  if record.get('restore_exact_prefix'):
   data=data[:record['regenerated_prefix_bytes']]+bytes.fromhex(record['literal_gzip_suffix_hex'])
  assert len(data)==record['original_bytes'] and hashlib.sha256(data).hexdigest()==record['original_sha256'],'Incompatible zlib regeneration'
  restored=dest.with_name(dest.name+'.restore.tmp');restored.write_bytes(data);restored.rename(dest)
  print('Restored and verified:',record['path']);continue
 assert record['encoding'] in ('xz-decoded-gnu-gzip-1','transpose-xz-decoded-gnu-gzip-1',CATEGORY_CERTIFICATE_ENCODING,JSON_COLUMN_ENCODING)
 generated=dest.with_name(dest.name+'.gnu-gzip.tmp')
 restored=dest.with_name(dest.name+'.restore.tmp')
 with generated.open('xb')as target:
  process=subprocess.Popen(['gzip','-'+str(record.get('gzip_compresslevel',1)),'-n','-c'],stdin=subprocess.PIPE,stdout=target)
  try:
   if record['encoding']==CATEGORY_CERTIFICATE_ENCODING:
    source=ROOT/record['source_path'];assert sha(source)==record['source_sha256']
    with source.open('rb')as src:
     for block in decode_category_certificates(encoded,iter(src),record):process.stdin.write(block)
   elif record['encoding']==JSON_COLUMN_ENCODING:
    for block in decode_json_columns(encoded):process.stdin.write(block)
   elif record['encoding']=='transpose-xz-decoded-gnu-gzip-1':
    for block in decode_rows(encoded):process.stdin.write(block)
   else:
    with lzma.open(encoded,'rb')as inp:
     while block:=inp.read(1<<20):process.stdin.write(block)
   process.stdin.close();assert process.wait()==0
  except BaseException:
   process.kill();process.wait();raise
 with restored.open('xb')as out,generated.open('rb')as inp:
  header=bytes.fromhex(record['original_header_hex']);out.write(header);inp.seek(10)
  suffix=bytes.fromhex(record.get('literal_gzip_suffix_hex',''))
  if 'regenerated_prefix_bytes'in record:
   assert record['regenerated_prefix_bytes']+len(suffix)==record['original_bytes']
   remaining=record['regenerated_prefix_bytes']-len(header)
   assert remaining>=0
  else:remaining=record['original_bytes']-len(header) if record.get('restore_exact_prefix') else None
  while remaining is None or remaining:
   block=inp.read((1<<20) if remaining is None else min(1<<20,remaining))
   if not block:break
   out.write(block)
   if remaining is not None:remaining-=len(block)
  assert remaining in (None,0)
  out.write(suffix)
 assert restored.stat().st_size==record['original_bytes']
 assert sha(restored)==record['original_sha256'],f'Incompatible GNU gzip: {dest}'
 restored.rename(dest);generated.unlink()
 print('Restored and verified:',record['path'])
