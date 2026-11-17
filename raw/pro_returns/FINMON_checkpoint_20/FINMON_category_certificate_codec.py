"""Restore exact certificate JSONL bytes from preserved source table rows.

Every omitted field is verified against its source before encoding. No
cohomology computation is rerun or assumed: the complete original gzip SHA256
is checked after regeneration by the caller.
"""
import hashlib,json,lzma,re,struct,zlib
ENCODING='xz-derived-category-jsonl-gnu-gzip-v1'
PYTHON_ENCODING='xz-derived-category-jsonl-python-gzip-v1'
FIELDS={b'row':b'@R@',b'objects':b'@K@',b'source':b'@S@',b'target':b'@T@',b'table':b'@M@'}
PATTERNS={k:re.compile(rb'("'+k+rb'"\s*:\s*)("[^"]*"|[0-9]+)')for k in FIELDS}

def values(source,row):
 s,t,m=source.rstrip(b'\n').split(b'\t')
 assert len(s)==len(t)and len(m)==len(s)**2
 return {b'row':str(row).encode(),b'objects':str(max(s)-48+1).encode(),
         b'source':b'"'+s+b'"',b'target':b'"'+t+b'"',b'table':b'"'+m+b'"'}

def positioned_source(source,start):
 assert next(source)==b'source\ttarget\tcomposition\n'
 for _ in range(start):next(source)
 return source

def encode(certificate,source,target,start):
 source=positioned_source(source,start);h=hashlib.sha256();total=rows=0;buffer=[];pending=0
 with lzma.open(target,'xb',preset=6)as out:
  for line in certificate:
   h.update(line);total+=len(line);assert line.endswith(b'\n')
   expected=values(next(source),start+rows)
   for key,marker in FIELDS.items():
    assert marker not in line
    matches=list(PATTERNS[key].finditer(line));assert len(matches)==1
    match=matches[0];assert match.group(2)==expected[key],(rows,key)
    line=line[:match.start(2)]+marker+line[match.end(2):]
   rows+=1;buffer.append(line);pending+=len(line)
   if pending>=1<<20:out.write(b''.join(buffer));buffer=[];pending=0
  if buffer:out.write(b''.join(buffer))
 return {'decoded_bytes':total,'decoded_sha256':h.hexdigest(),'certificate_rows':rows,'source_start_row':start}

def decode(encoded,source,record):
 source=positioned_source(source,record['source_start_row']);rows=0
 with lzma.open(encoded,'rb')as inp:
  for line in inp:
   expected=values(next(source),record['source_start_row']+rows)
   for key,marker in FIELDS.items():
    assert line.count(marker)==1
    line=line.replace(marker,expected[key])
   rows+=1;yield line
 assert rows==record['certificate_rows']

def regenerate_python(encoded,source,record):
 """Restore the literal Python gzip after substituting verified TSV fields."""
 yield bytes.fromhex(record['original_header_hex'])
 compressor=zlib.compressobj(record['compresslevel'],zlib.DEFLATED,-15)
 crc=total=0;decoded_hash=hashlib.sha256()
 for raw in decode(encoded,source,record):
  crc=zlib.crc32(raw,crc);total+=len(raw);decoded_hash.update(raw)
  block=compressor.compress(raw)
  if block:yield block
 assert total==record['decoded_bytes'] and decoded_hash.hexdigest()==record['decoded_sha256']
 if record.get('sync_flush_before_close'):yield compressor.flush(zlib.Z_SYNC_FLUSH)
 yield compressor.flush(zlib.Z_FINISH)
 yield struct.pack('<II',crc&0xffffffff,total&0xffffffff)
