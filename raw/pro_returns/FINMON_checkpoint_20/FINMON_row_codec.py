#!/usr/bin/env python3
"""Byte-reversible blocked transpose for fixed-width category-census TSVs.
The format contains the literal header and every complete or partial row.
It needs only Python's standard library; no mathematical record is deleted.
"""
from pathlib import Path
import gzip,hashlib,json,lzma,struct,sys,time
MAGIC=b'FINMON_TSV_TRANSPOSE_1\n'
RUN_MAGIC=b'FINMON_TSV_TRANSPOSE_RUNS_1\n'
ENCODING='fixed-row-transpose-xz-v1'


def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb')as f:
  while b:=f.read(1<<20):h.update(b)
 return h.hexdigest()


def encode(source,dest,block_rows=131072,preset=3,gzip_input=False):
 source=Path(source);dest=Path(dest);h=hashlib.sha256();size=0;blocks=0
 with (gzip.open(source,'rb') if gzip_input else source.open('rb'))as inp:
  header=inp.readline();first=inp.readline();width=len(first)
  assert header==b'source\ttarget\tcomposition\n' and first.endswith(b'\n')
  inp.seek(len(header));h.update(header);size+=len(header)
  with lzma.open(dest,'xb',preset=preset)as out:
   out.write(MAGIC);out.write(struct.pack('<QQQ',width,block_rows,len(header)));out.write(header)
   while data:=inp.read(width*block_rows):
    h.update(data);size+=len(data);rows=len(data)//width;end=rows*width
    assert data[width-1:end:width]==b'\n'*rows
    out.write(struct.pack('<Q',len(data)))
    out.write(b''.join(data[col:end:width]for col in range(width)))
    out.write(data[end:]);blocks+=1
 return {'encoding':ENCODING,'original_bytes':size,'original_sha256':h.hexdigest(),
         'encoded_bytes':dest.stat().st_size,'encoded_sha256':digest(dest),
         'width':width,'block_rows':block_rows,'blocks':blocks,'preset':preset}


def decode(source):
 with lzma.LZMAFile(source,'rb')as inp:
  magic=inp.readline();assert magic in (MAGIC,RUN_MAGIC)
  raw=inp.read(24);assert len(raw)==24
  width,block_rows,header_size=struct.unpack('<QQQ',raw)
  assert 0<width<100000 and 0<block_rows<=4000000 and header_size<100000
  header=inp.read(header_size);assert len(header)==header_size;yield header
  while raw:=inp.read(8):
   assert len(raw)==8;size=struct.unpack('<Q',raw)[0];assert 0<size<=width*block_rows
   rows=size//width;end=rows*width
   if magic==MAGIC:
    data=inp.read(size);assert len(data)==size
   else:
    nruns,nlong=struct.unpack('<QQ',inp.read(16));assert 0<nruns<=size and nlong<=nruns
    values=inp.read(nruns);shorts=inp.read(2*nruns);longs=inp.read(4*nlong)
    assert len(values)==nruns and len(shorts)==2*nruns and len(longs)==4*nlong
    try:
     import numpy as np
     lengths=np.frombuffer(shorts,dtype='<u2').astype(np.int64);mask=lengths==65535
     assert int(mask.sum())==nlong;lengths[mask]=np.frombuffer(longs,dtype='<u4')
     assert int(lengths.sum())==size and np.all(lengths>0)
     data=np.repeat(np.frombuffer(values,dtype=np.uint8),lengths).tobytes()
    except ImportError:
     from array import array
     lengths=array('H');lengths.frombytes(shorts);large=array('I');large.frombytes(longs)
     if sys.byteorder!='little':lengths.byteswap();large.byteswap()
     result=bytearray();large_index=0
     for value,length in zip(values,lengths):
      if length==65535:length=large[large_index];large_index+=1
      assert length>0;result.extend(bytes([value])*length)
     assert large_index==nlong and len(result)==size;data=bytes(result)
   restored=bytearray(size)
   for col in range(width):restored[col:end:width]=data[col*rows:(col+1)*rows]
   restored[end:]=data[end:];yield bytes(restored)


if __name__=='__main__':
 t=time.monotonic();r=encode(sys.argv[1],sys.argv[2]);h=hashlib.sha256();n=0
 for b in decode(sys.argv[2]):h.update(b);n+=len(b)
 assert n==r['original_bytes'] and h.hexdigest()==r['original_sha256']
 r['regeneration_verified']=True;r['seconds']=time.monotonic()-t
 print(json.dumps(r,indent=2))
