#!/usr/bin/env python3
"""Exact deterministic C++ stdout reconstruction, then literal Python gzip.

The encoded bundle contains every compiler input and every source-data byte.
No network or external mathematical data is used. A compatible C++17 compiler
and zlib are required. The caller must verify the full original gzip SHA256.
"""
from pathlib import Path
import hashlib,json,lzma,struct,subprocess,tempfile,time,zlib
ENCODING='deterministic-cpp-stdout-python-gzip-v1'
FORMAT='FINMON_SELF_CONTAINED_CPP_STDOUT_RECIPE_1'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def regenerate(source,record,scratch_dir=None,stats=None):
 start=time.monotonic();stats={}if stats is None else stats
 with lzma.LZMAFile(source,'rb')as f:bundle=json.load(f)
 assert bundle['format']==FORMAT and bundle['compiler_flags']==['-O3','-std=c++17']
 assert len(bundle['arguments'])==3 and all(isinstance(x,int)for x in bundle['arguments'])
 with tempfile.TemporaryDirectory(prefix='.finmon-cpp-restore-',dir=scratch_dir)as td:
  d=Path(td);names=set()
  for item in bundle['files']:
   name=item['name'];assert name==Path(name).name and name not in names and name not in ('.','..');names.add(name)
   raw=item['content'].encode('utf-8');assert len(raw)==item['bytes']and hashlib.sha256(raw).hexdigest()==item['sha256'];(d/name).write_bytes(raw)
  assert bundle['main']in names and bundle['input']in names
  binary=d/'regenerate';compiled=subprocess.run(['g++',*bundle['compiler_flags'],str(d/bundle['main']),'-o',str(binary)],capture_output=True)
  assert compiled.returncode==0,('C++17 reconstruction compilation failed',compiled.returncode,compiled.stderr[-4000:].decode(errors='replace'))
  catalog=d/'right_catalog.jsonl';stderr=d/'producer.stderr';header=bytes.fromhex(record['original_header_hex']);yield header
  compressor=zlib.compressobj(record['compresslevel'],zlib.DEFLATED,-15);crc=decoded=lines=0;rawhash=hashlib.sha256()
  with (d/bundle['input']).open('rb')as inp,stderr.open('wb')as log:
   child=subprocess.Popen([str(binary),*map(str,bundle['arguments']),str(catalog)],stdin=inp,stdout=subprocess.PIPE,stderr=log)
   try:
    assert child.stdout
    while raw:=child.stdout.read(1<<20):
     decoded+=len(raw);lines+=raw.count(b'\n');rawhash.update(raw);crc=zlib.crc32(raw,crc);block=compressor.compress(raw)
     if block:yield block
    child.stdout.close();code=child.wait();stats['actual_subprocess_exit_code']=code
    assert code==0,('Reconstruction producer failed',code,stderr.read_text(errors='replace')[-4000:])
   except BaseException:
    if child.poll()is None:child.terminate();child.wait()
    raise
  stats.update(decoded_bytes=decoded,stdout_lines=lines,stdout_sha256=rawhash.hexdigest(),right_catalog_bytes=catalog.stat().st_size,right_catalog_sha256=sha(catalog),seconds=time.monotonic()-start)
  for key in ('decoded_bytes','stdout_sha256','right_catalog_bytes','right_catalog_sha256'):
   if key in record:assert stats[key]==record[key],(key,stats[key],record[key])
  if record.get('sync_flush_before_close'):yield compressor.flush(zlib.Z_SYNC_FLUSH)
  yield compressor.flush(zlib.Z_FINISH);yield struct.pack('<II',crc&0xffffffff,decoded&0xffffffff)
