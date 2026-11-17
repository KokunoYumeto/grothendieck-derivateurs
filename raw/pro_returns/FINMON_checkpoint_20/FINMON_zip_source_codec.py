#!/usr/bin/env python3
"""Exact ZIP bytes from original deflate instructions and retained sources.

Only literal bytes and stored blocks are obtained from separately retained
source files. Every Huffman header, LZ77 match, extra bit and padding bit is
literal original data. No deflate compressor or version match is required.
"""
import hashlib,lzma,struct
MAGIC=b'FINMON_ZIP_SOURCE_DEFLATE_1\n'
ENCODING='zip-source-deflate-instructions-xz-v1'
LEX=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0]
LBASE=[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258]
DBASE=[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577]
def dex(d):return 0 if d<4 else d//2-1
class Bits:
 def __init__(self,b):self.b=b;self.pos=0
 def take(self,n):
  i=self.pos>>3;q=int.from_bytes(self.b[i:i+3],'little');v=(q>>(self.pos&7))&((1<<n)-1);self.pos+=n;assert self.pos<=8*len(self.b);return v
class Writer:
 def __init__(self):self.b=bytearray();self.acc=0;self.n=0
 def put(self,v,n):
  assert 0<=v<(1<<n)or(n==0 and v==0);self.acc|=v<<self.n;self.n+=n
  while self.n>=8:self.b.append(self.acc&255);self.acc>>=8;self.n-=8
 def append(self,b,n):
  r=Bits(b)
  while n:k=min(n,16);self.put(r.take(k),k);n-=k
class Huffman:
 def __init__(self,lengths):
  self.lengths=lengths;self.codes=[0]*len(lengths);count=[0]*16;next_code=[0]*16
  for n in lengths:count[n]+=bool(n)
  c=0
  for n in range(1,16):c=(c+count[n-1])<<1;next_code[n]=c
  self.lookup={}
  for s,n in enumerate(lengths):
   if not n:continue
   c=next_code[n];next_code[n]+=1;v=0
   for _ in range(n):v=(v<<1)|(c&1);c>>=1
   self.codes[s]=v;self.lookup[v,n]=s
 def read(self,r):
  v=0
  for n in range(1,16):
   v|=r.take(1)<<(n-1)
   if(v,n)in self.lookup:return self.lookup[v,n]
  raise AssertionError('invalid Huffman word')
def trees(r,kind):
 if kind==1:return Huffman([8]*144+[9]*112+[7]*24+[8]*8),Huffman([5]*32)
 assert kind==2;nl=r.take(5)+257;nd=r.take(5)+1;nc=r.take(4)+4;order=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15];cl=[0]*19
 for i in range(nc):cl[order[i]]=r.take(3)
 h=Huffman(cl);lens=[]
 while len(lens)<nl+nd:
  s=h.read(r)
  if s<=15:lens.append(s)
  elif s==16:lens.extend([lens[-1]]*(r.take(2)+3))
  elif s==17:lens.extend([0]*(r.take(3)+3))
  else:assert s==18;lens.extend([0]*(r.take(7)+11))
 assert len(lens)==nl+nd and lens[256];return Huffman(lens[:nl]),Huffman(lens[nl:])
def restore_deflate(token,source,expected):
 at=0;pos=0;w=Writer()
 def var():
  nonlocal at
  v=0;shift=0
  while True:
   c=token[at];at+=1;v|=(c&127)<<shift
   if c<128:return v
   shift+=7;assert shift<64
 def raw(n):
  nonlocal at
  r=token[at:at+n];assert len(r)==n;at+=n;return r
 blocks=var();final=0
 for bi in range(blocks):
  assert not final;kind=raw(1)[0];nb=var();head=raw((nb+7)//8);r=Bits(head);final=r.take(1);assert r.take(2)==kind;w.append(head,nb)
  if kind==0:
   r.pos=nb-32
   n=r.take(16);assert(r.take(16)^n)==65535;assert var()==n and r.pos==nb and w.n==0
   w.b.extend(source[pos:pos+n]);pos+=n;continue
  lit,dist=trees(r,kind);assert r.pos==nb;nr=var();runs=[var()for _ in range(nr)];matches=[[var()for _ in range(4)]for _ in range(nr-1)]
  for i,n in enumerate(runs):
   assert pos+n<=len(source)
   for c in source[pos:pos+n]:w.put(lit.codes[c],lit.lengths[c])
   pos+=n
   if i==nr-1:w.put(lit.codes[256],lit.lengths[256]);continue
   sc,le,dc,de=matches[i];assert sc<29 and dc<30;s=sc+257;w.put(lit.codes[s],lit.lengths[s]);w.put(le,LEX[sc]);w.put(dist.codes[dc],dist.lengths[dc]);w.put(de,dex(dc));n=LBASE[sc]+le;back=DBASE[dc]+de;assert back<=pos and pos+n<=len(source)
   for j in range(n):assert source[pos+j]==source[pos+j-back]
   pos+=n
 assert final and pos==len(source);n=var();assert n<8;w.append(raw((n+7)//8),n);assert at==len(token)and w.n==0 and len(w.b)==expected;return bytes(w.b)
def exact(inp,n):
 b=inp.read(n);assert len(b)==n;return b

def decode(encoded,source_reader):
 with lzma.LZMAFile(encoded,'rb')as inp:
  assert exact(inp,len(MAGIC))==MAGIC;size,count=struct.unpack('<QI',exact(inp,12));written=0
  for _ in range(count):
   n=struct.unpack('<Q',exact(inp,8))[0];gap=exact(inp,n);written+=n;yield gap
   n=struct.unpack('<H',exact(inp,2))[0];path=exact(inp,n).decode();source_size=struct.unpack('<Q',exact(inp,8))[0];digest=exact(inp,32);expected,token_size=struct.unpack('<IQ',exact(inp,12));token=exact(inp,token_size)
   source=source_reader(path);assert len(source)==source_size and hashlib.sha256(source).digest()==digest
   raw=restore_deflate(token,source,expected);written+=len(raw);yield raw
  n=struct.unpack('<Q',exact(inp,8))[0];gap=exact(inp,n);written+=n;yield gap;assert written==size and not inp.read(1)
