#!/usr/bin/env python3
"""Primitive preimages in the integral-reduction subspace of H12(B smash E)."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
    import I_integral_browder_sources as b
a=b.a

DB={};DI={}
for n in range(7,13):
    basis=[]
    for ex in a.LABELS:
        j=n-a.bpoly.deg(ex)
        if j<5:continue
        for i in range(len(a.ESPACE[j].vectors)):basis.append((ex,j,i))
    DB[n]=basis;DI[n]={v:i for i,v in enumerate(basis)}

def tensor(x,y):
    n=a.pdegree(x)+a.pdegree(y);j=a.pdegree(y)
    co=a.ESPACE[j].coords(a.vector(y,j));out=0
    for m in x:
        assert len(m)==1
        w,r=a.GENS[m[0]];assert r==0 and len(w)==1
        ex=a.LABELS[w[0]]
        for i in range(len(a.ESPACE[j].vectors)):
            if co>>i&1:out^=1<<DI[n][(ex,j,i)]
    return out

def operation(k,v,n):
    if n-k<7:return 0
    out=0
    for i,(ex,j,idx) in enumerate(DB[n]):
        if not(v>>i&1):continue
        x=a.label(ex);y=a.poly(a.ESPACE[j].vectors[idx],j)
        for r in range(k+1):
            xx=a.sq(r,x);yy=a.sq(k-r,y)
            if xx and yy:out^=tensor(xx,yy)
    return out

def image(v):
    out=a.EMPTY
    for i,(ex,j,idx) in enumerate(DB[12]):
        if v>>i&1:
            out=a.xor(out,b.normalized_bracket(a.label(ex),a.poly(a.ESPACE[j].vectors[idx],j)))
    sp,nk=a.LSPACE[13]
    return sp.coords(a.vector(out,13))>>nk

src=[]
src += [(f'a_I10_{i}',tensor(a.a,y)) for i,y in enumerate(b.ints10)]
src += [(f'c_I8_{i}',tensor(a.c,y)) for i,y in enumerate(b.ints8)]
src += [('de_R',tensor(a.xor(a.d,a.e),a.R)),
        ('f_DE',tensor(a.named('u3'),a.xor(a.D,a.E6))),
        ('h_u',tensor(a.named('uw'),a.u))]
src += [('Tor_a_N',tensor(a.a,b.B5)),
        ('Tor_a_K1',tensor(a.b,b.K1)^tensor(a.a,b.B1)),
        ('Tor_a_K5',tensor(a.b,b.K5)^tensor(a.a,b.B7)),
        ('Tor_a_Ksum',tensor(a.b,b.Ksum)^tensor(a.a,b.B4)),
        ('Tor_c_R',tensor(a.d,a.R)),
        ('Tor_de_DE',tensor(a.named('v2'),a.xor(a.D,a.E6))^tensor(a.xor(a.d,a.e),a.S)),
        ('Tor_f_u',tensor(a.named('u3'),a.D))]
sp=a.Span()
for name,v in src:assert sp.add(v)
assert len(src)==22 and len(DB[12])==35
piv={};ker=[]
for j,(name,v) in enumerate(src):
    out=0;off=0
    for k in (1,2,4):
        out^=operation(k,v,12)<<off;off+=len(DB[12-k])
    c=1<<j
    while out:
        i=out.bit_length()-1
        if i not in piv:break
        w,d=piv[i];out^=w;c^=d
    if out:piv[out.bit_length()-1]=(out,c)
    else:ker.append(c)

rows=[];isp=a.Span()
for c in ker:
    v=0;names=[]
    for j,(name,s) in enumerate(src):
        if c>>j&1:v^=s;names.append(name)
    im=image(v);isp.add(im)
    rows.append({'integral_source_combination':names,
                 'image':[id for j,id in enumerate(a.LIDS[13]) if im>>j&1]})
report={'status':'PASS','source_mod2_dimension':35,
        'candidate_integral_reduction_dimension':22,
        'primitive_subspace_dimension':len(ker),
        'primitive_image_dimension':len(isp.vectors),'primitive_sources':rows,
        'scope':'Exact tensor Cartan and normalized-Browder algebra; actual map and integral source inputs require the accompanying audit.'}
dest=Path(__file__).parent/'outputs'/'I_browder_source_lifts.json'
dest.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
