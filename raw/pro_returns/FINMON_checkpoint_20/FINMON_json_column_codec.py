#!/usr/bin/env python3
"""Exact blocked transposition of literal JSONL value columns.

This is a byte codec: it never changes numbers, whitespace, field ordering,
or proof values. Every reconstructed line is byte-identical to its input.
"""
import lzma,re,struct,zlib
MAGIC=b'FINMON_LITERAL_JSON_COLUMNS_1\n'
MAGIC2=b'FINMON_LITERAL_JSON_COLUMNS_2\n'
ENCODING='json-columns-xz-decoded-gnu-gzip-1'
PYTHON_ENCODING='json-columns-xz-decoded-python-gzip-v1'
KEY=re.compile(rb'(?:\{|,)"[A-Za-z_][A-Za-z_0-9]*":')

def encode(stream,dest,block_rows=50000,preset=3):
 rows=0;decoded=0;blocks=0;keys=None;cols=None;count=0
 with lzma.open(dest,'xb',preset=preset)as out:
  out.write(MAGIC)
  def flush():
   nonlocal count,cols,blocks
   if not count:return
   out.write(struct.pack('<II',count,len(keys)))
   for k in keys:out.write(struct.pack('<I',len(k)));out.write(k)
   for col in cols:
    raw=b'\n'.join(col)+b'\n';out.write(struct.pack('<Q',len(raw)));out.write(raw)
   blocks+=1;count=0;cols=[[]for _ in keys]
  for line in stream:
   decoded+=len(line)
   matches=list(KEY.finditer(line))if line.startswith(b'{')and line.endswith(b'}\n')else[]
   if not matches or matches[0].start()!=0:
    flush();out.write(struct.pack('<IIQ',0,0,len(line)));out.write(line);continue
   newkeys=tuple(m.group()[1:]for m in matches)
   values=[line[m.end():(matches[i+1].start()if i+1<len(matches)else len(line)-2)]for i,m in enumerate(matches)]
   assert b'{'+b','.join(k+v for k,v in zip(newkeys,values))+b'}\n'==line
   assert all(b'\n'not in v for v in values)
   if newkeys!=keys:flush();keys=newkeys;cols=[[]for _ in keys]
   for col,value in zip(cols,values):col.append(value)
   count+=1;rows+=1
   if count==block_rows:flush()
  flush()
 return {'decoded_bytes':decoded,'json_rows':rows,'json_column_blocks':blocks,'json_column_block_rows':block_rows}

def decode(source):
 with lzma.LZMAFile(source,'rb')as inp:
  magic=inp.read(len(MAGIC))
  if magic==MAGIC2:
   yield from decode_grouped(inp);return
  assert magic==MAGIC
  while head:=inp.read(8):
   assert len(head)==8;rows,ncols=struct.unpack('<II',head)
   if rows==0:
    assert ncols==0;size=struct.unpack('<Q',inp.read(8))[0];raw=inp.read(size);assert len(raw)==size;yield raw;continue
   assert 0<rows<=1000000 and 0<ncols<1000
   keys=[]
   for _ in range(ncols):
    size=struct.unpack('<I',inp.read(4))[0];assert size<10000;k=inp.read(size);assert len(k)==size;keys.append(k)
   cols=[]
   for _ in range(ncols):
    size=struct.unpack('<Q',inp.read(8))[0];raw=inp.read(size);assert len(raw)==size
    values=raw.split(b'\n');assert len(values)==rows+1 and values[-1]==b'';cols.append(values[:-1])
   buffer=[];size=0
   for i in range(rows):
    line=b'{'+b','.join(k+col[i]for k,col in zip(keys,cols))+b'}\n';buffer.append(line);size+=len(line)
    if size>=1<<20:yield b''.join(buffer);buffer=[];size=0
   if buffer:yield b''.join(buffer)

def encode_grouped(stream,dest,block_rows=50000,preset=9):
 """Group different literal schemas within a block, saving row positions."""
 rows=decoded=blocks=count=0;groups={}
 with lzma.open(dest,'xb',preset=preset)as out:
  out.write(MAGIC2)
  def flush():
   nonlocal count,groups,blocks
   if not count:return
   out.write(struct.pack('<II',count,len(groups)))
   for keys,(positions,cols) in groups.items():
    out.write(struct.pack('<II',len(positions),len(keys)))
    for k in keys:out.write(struct.pack('<I',len(k)));out.write(k)
    out.write(struct.pack('<'+'I'*len(positions),*positions))
    for col in cols:
     raw=b'\n'.join(col)+b'\n';out.write(struct.pack('<Q',len(raw)));out.write(raw)
   blocks+=1;count=0;groups={}
  for line in stream:
   decoded+=len(line)
   matches=list(KEY.finditer(line))if line.startswith(b'{')and line.endswith(b'}\n')else[]
   if not matches or matches[0].start()!=0:
    flush();out.write(struct.pack('<IIQ',0,0,len(line)));out.write(line);continue
   keys=tuple(m.group()[1:]for m in matches)
   values=[line[m.end():(matches[i+1].start()if i+1<len(matches)else len(line)-2)]for i,m in enumerate(matches)]
   assert b'{'+b','.join(k+v for k,v in zip(keys,values))+b'}\n'==line
   assert all(b'\n'not in v for v in values)
   if keys not in groups:groups[keys]=([], [[]for _ in keys])
   positions,cols=groups[keys];positions.append(count)
   for col,value in zip(cols,values):col.append(value)
   rows+=1;count+=1
   if count==block_rows:flush()
  flush()
 return {'decoded_bytes':decoded,'json_rows':rows,'json_column_blocks':blocks,
         'json_column_block_rows':block_rows,'literal_column_format':2}

def decode_grouped(inp):
 while head:=inp.read(8):
  assert len(head)==8;rows,ngroups=struct.unpack('<II',head)
  if rows==0:
   assert ngroups==0;size=struct.unpack('<Q',inp.read(8))[0]
   raw=inp.read(size);assert len(raw)==size;yield raw;continue
  assert 0<rows<=1000000 and 0<ngroups<=rows
  lines=[None]*rows
  for _ in range(ngroups):
   n,ncols=struct.unpack('<II',inp.read(8));assert 0<n<=rows and 0<ncols<1000
   keys=[]
   for _ in range(ncols):
    size=struct.unpack('<I',inp.read(4))[0];assert size<10000
    k=inp.read(size);assert len(k)==size;keys.append(k)
   raw=inp.read(4*n);assert len(raw)==4*n;positions=struct.unpack('<'+'I'*n,raw)
   cols=[]
   for _ in range(ncols):
    size=struct.unpack('<Q',inp.read(8))[0];raw=inp.read(size);assert len(raw)==size
    values=raw.split(b'\n');assert len(values)==n+1 and values[-1]==b'';cols.append(values[:-1])
   for i,position in enumerate(positions):
    assert 0<=position<rows and lines[position]is None
    lines[position]=b'{'+b','.join(k+col[i]for k,col in zip(keys,cols))+b'}\n'
  assert all(line is not None for line in lines)
  buffer=[];size=0
  for line in lines:
   buffer.append(line);size+=len(line)
   if size>=1<<20:yield b''.join(buffer);buffer=[];size=0
  if buffer:yield b''.join(buffer)

def regenerate_python_gzip(source,record):
 """Regenerate a closed Python gzip exactly, in bounded memory."""
 assert record['encoding']==PYTHON_ENCODING and not record.get('restore_exact_prefix')
 yield bytes.fromhex(record['original_header_hex'])
 compressor=zlib.compressobj(record['compresslevel'],zlib.DEFLATED,-15)
 crc=length=0
 for block in decode(source):
  crc=zlib.crc32(block,crc);length+=len(block)
  encoded=compressor.compress(block)
  if encoded:yield encoded
 assert length==record['decoded_bytes']
 if record.get('sync_flush_before_close'):yield compressor.flush(zlib.Z_SYNC_FLUSH)
 yield compressor.flush(zlib.Z_FINISH)
 yield struct.pack('<II',crc&0xffffffff,length&0xffffffff)
