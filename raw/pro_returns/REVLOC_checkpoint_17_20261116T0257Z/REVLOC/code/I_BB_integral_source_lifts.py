#!/usr/bin/env python3
"""Integral tensor/Tor candidate sources in H12(B smash B), with primary tests."""
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
with redirect_stdout(StringIO()):import I_integral_browder_sources as b
a=b.a
DB={};DI={}
for n in range(4,13):
    DB[n]=[(x,y) for x in a.LABELS for y in a.LABELS
           if a.bpoly.deg(x)+a.bpoly.deg(y)==n]
    DI[n]={v:i for i,v in enumerate(DB[n])}
def labels(p):
    ans=[]
    for m in p:
        assert len(m)==1
        w,r=a.GENS[m[0]];assert not r and len(w)==1
        ans.append(a.LABELS[w[0]])
    return ans
def tensor(x,y):
    n=a.pdegree(x)+a.pdegree(y);out=0
    for l in labels(x):
        for r in labels(y):out^=1<<DI[n][(l,r)]
    return out
def flip(v,n=12):
    return sum(1<<DI[n][(y,x)] for i,(x,y) in enumerate(DB[n]) if v>>i&1)
def op(k,v,n=12):
    if n-k<4:return 0
    out=0
    for i,(x,y) in enumerate(DB[n]):
        if not(v>>i&1):continue
        for j in range(k+1):
            xx=a.sq(j,a.label(x));yy=a.sq(k-j,a.label(y))
            if xx and yy:out^=tensor(xx,yy)
    return out
def image(v):
    p=a.EMPTY
    for i,(x,y) in enumerate(DB[12]):
        if v>>i&1:p=a.xor(p,b.normalized_two_labels(a.label(x),a.label(y)))
    a.ESPACE[13].coords(a.vector(p,13))
    sp,nk=a.LSPACE[13]
    return sp.coords(a.vector(p,13))>>nk
src=[]
for name,x,y in [('a_p',a.a,a.named('u5')),('a_r',a.a,a.named('uvw')),
                 ('c_i',a.c,a.named('u4')),
                 ('c_jl',a.c,a.xor(a.named('uv2'),a.named('vw'))),
                 ('de_h',a.xor(a.d,a.e),a.named('uw'))]:
    v=tensor(x,y);src.extend([(name,v),(name+'_flip',flip(v))])
src.append(('f_f',tensor(a.named('u3'),a.named('u3'))))
tors=[('a_mn',tensor(a.b,a.xor(a.named('u3v'),a.named('u2w')))^tensor(a.a,a.named('u2v2'))),
      ('a_t',tensor(a.b,a.named('t'))^tensor(a.a,a.named('w2'))),
      ('c_h',tensor(a.d,a.named('uw'))),
      ('de_f',tensor(a.named('v2'),a.named('u3'))^tensor(a.xor(a.d,a.e),a.named('u2v')))]
for name,v in tors:src.extend([('Tor_'+name,v),('Tor_'+name+'_flip',flip(v))])
span=a.Span()
for name,v in src:
    assert op(1,v)==0,name
    assert span.add(v),name
assert len(src)==19 and len(DB[12])==34
piv={};kernel=[]
for j,(name,v) in enumerate(src):
    out=0;off=0
    for k in (1,2,4,8):
        out^=op(k,v)<<off;off+=len(DB[12-k])
    c=1<<j
    while out:
        i=out.bit_length()-1
        if i not in piv:break
        w,d=piv[i];out^=w;c^=d
    if out:piv[out.bit_length()-1]=(out,c)
    else:kernel.append(c)
isp=a.Span();rows=[]
for c in kernel:
    v=0;names=[]
    for j,(name,s) in enumerate(src):
        if c>>j&1:v^=s;names.append(name)
    im=image(v);isp.add(im)
    rows.append({'integral_source_combination':names,
                 'image':[id for j,id in enumerate(a.LIDS[13]) if im>>j&1]})
report={'status':'PASS','source_mod2_dimension':34,
        'candidate_integral_reduction_dimension':19,
        'primitive_subspace_dimension':len(kernel),
        'primitive_image_dimension':len(isp.vectors),'primitive_sources':rows,
        'scope':'Integral input and actual normalized-map interface audited separately.'}
dest=Path(__file__).parent/'outputs'/'I_BB_integral_source_lifts.json'
dest.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
