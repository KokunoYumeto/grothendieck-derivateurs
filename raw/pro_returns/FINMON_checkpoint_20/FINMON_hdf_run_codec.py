#!/usr/bin/env python3
"""Exact HDF compressed-chunk bytes from literal decoded runs and trailers.

The stream retains every non-chunk byte and the original four Fletcher32
bytes. Chunk deflate regeneration is zlib level9; full original SHA256 must
match before accepting a restored file. NumPy is an optional acceleration.
"""
import lzma,struct,zlib
from collections import deque
from concurrent.futures import ThreadPoolExecutor
MAGIC=b'FINMON_HDF_ZLIB9_RUNS_U16_1\n'
ENCODING='hdf5-zlib9-rle-u16-xz-v1'
try:import numpy as np
except ImportError:np=None

def exact(inp,n):
 b=inp.read(n);assert len(b)==n,(len(b),n);return b

def records(inp):
 while tag:=inp.read(1):
  if tag==b'G':
   n=struct.unpack('<Q',exact(inp,8))[0]
   while n:
    b=exact(inp,min(n,1<<20));n-=len(b);yield b
  elif tag==b'C':
   size,rawsize,n=struct.unpack('<III',exact(inp,12));tr=exact(inp,4);values=exact(inp,n);short=exact(inp,2*n)
   if np is not None:
    lengths=np.frombuffer(short,dtype='<u2').astype('<u4');big=lengths==65535;k=int(big.sum())
    if k:lengths[big]=np.frombuffer(exact(inp,4*k),dtype='<u4')
    assert int(lengths.sum())==rawsize
    raw=np.repeat(np.frombuffer(values,dtype='u1'),lengths).tobytes()
   else:
    lengths=list(struct.unpack('<'+'H'*n,short));k=lengths.count(65535);big=iter(struct.unpack('<'+'I'*k,exact(inp,4*k)))
    lengths=[next(big)if x==65535 else x for x in lengths];assert sum(lengths)==rawsize
    raw=b''.join(bytes([v])*q for v,q in zip(values,lengths))
   out=zlib.compress(raw,9)+tr;assert len(out)==size;yield out
  else:raise AssertionError(('unknown record',tag))

def regenerated_chunk(size,rawsize,n,tr,values,short,long):
 if np is not None:
  lengths=np.frombuffer(short,dtype='<u2').astype('<u4');big=lengths==65535
  assert int(big.sum())*4==len(long)
  if len(long):lengths[big]=np.frombuffer(long,dtype='<u4')
  assert int(lengths.sum())==rawsize
  raw=np.repeat(np.frombuffer(values,dtype='u1'),lengths).tobytes()
 else:
  lengths=list(struct.unpack('<'+'H'*n,short));k=lengths.count(65535)
  assert 4*k==len(long);large=iter(struct.unpack('<'+'I'*k,long))
  lengths=[next(large)if x==65535 else x for x in lengths]
  assert sum(lengths)==rawsize;raw=b''.join(bytes([v])*q for v,q in zip(values,lengths))
 out=zlib.compress(raw,9)+tr;assert len(out)==size;return out

def records_parallel(inp,workers=4):
 """Regenerate independent chunks concurrently while yielding original order."""
 pending=deque()
 with ThreadPoolExecutor(max_workers=workers)as pool:
  while tag:=inp.read(1):
   if tag==b'G':
    while pending:yield pending.popleft().result()
    n=struct.unpack('<Q',exact(inp,8))[0]
    while n:
     b=exact(inp,min(n,1<<20));n-=len(b);yield b
   elif tag==b'C':
    size,rawsize,n=struct.unpack('<III',exact(inp,12));tr=exact(inp,4);values=exact(inp,n);short=exact(inp,2*n)
    k=int((np.frombuffer(short,dtype='<u2')==65535).sum())if np is not None else struct.unpack('<'+'H'*n,short).count(65535)
    long=exact(inp,4*k)
    pending.append(pool.submit(regenerated_chunk,size,rawsize,n,tr,values,short,long))
    if len(pending)>=workers*4:yield pending.popleft().result()
   else:raise AssertionError(('unknown record',tag))
  while pending:yield pending.popleft().result()

def decode(source,workers=4):
 with lzma.LZMAFile(source,'rb')as inp:
  assert exact(inp,len(MAGIC))==MAGIC
  size=struct.unpack('<Q',exact(inp,8))[0];count=0
  stream=records(inp)if workers==1 else records_parallel(inp,workers)
  for block in stream:count+=len(block);yield block
  assert count==size,(count,size)
