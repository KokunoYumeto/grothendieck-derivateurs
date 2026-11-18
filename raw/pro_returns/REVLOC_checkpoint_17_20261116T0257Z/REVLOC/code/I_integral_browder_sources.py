#!/usr/bin/env python3
"""Candidate integral Browder source images; integral input is audited separately."""
import I_E2_primary_15 as a

m=a.mul;br=a.bracket;xx=a.xor;pw=a.power
A=a.A;u=a.u;k=a.k;R=a.R;aa=a.a;b=a.b;c=a.c;d=a.d;e=a.e
z=xx(e,m(aa,b)); W=pw(aa,4)
L=xx(a.named('vw'),m(b,d))
M=xx(a.named('uv2'),m(aa,a.named('v2')),m(b,e),m(aa,pw(b,2)))
J1=br(aa,d);J2=xx(br(aa,e),m(aa,k))
Pp=xx(a.named('u5'),m(aa,a.named('u4')),m(c,a.named('u3')),
       m(A,a.named('u3')),m(aa,pw(c,2)),m(pw(aa,3),c),pw(aa,5))
Pr=xx(a.named('uvw'),m(aa,a.named('vw')),m(b,a.named('uw')),m(e,d))
B1=xx(br(aa,a.named('u2v')),m(aa,br(aa,e)),m(c,k),m(b,R),m(A,k))
B2=xx(br(aa,a.named('uw')),m(aa,br(aa,d)))
B3=xx(br(b,a.named('u3')),m(c,k),m(aa,br(b,c)),m(A,k))
B5=xx(br(c,d),m(aa,br(aa,d)))
B6=xx(br(c,e),m(b,R),m(aa,br(b,c)),m(aa,br(aa,e)),m(A,k))
B8=br(aa,R)
B4=br(b,a.named('v2'));B7=br(b,k)
K1=xx(br(aa,a.named('u3')),m(aa,R));K5=br(aa,k)
Ksum=xx(br(aa,a.named('v2')),br(b,d),br(b,e))
ints10=[pw(z,2),pw(u,2),xx(pw(d,2),Pp),Pr,B2,B8,xx(B1,B3),xx(B5,B6)]
ints8=[W,xx(L,M),J1,J2]
def normalized_bracket(x,y):
    assert not [(l,r) for l,r in a.delta(y) if l and r]
    out=a.EMPTY
    for left,right in a.delta(x):
        if not left:continue
        inv=a.ONE
        for gen in right:
            word,power=a.GENS[gen]
            assert power==0 and len(word)==1
            inv=m(inv,a.antipode_label(a.LABELS[word[0]]))
        out=xx(out,m(br(frozenset({left}),y),inv))
    return out
def normalized_two_labels(x,y):
    out=a.EMPTY
    for lx,rx in a.delta(x):
        for ly,ry in a.delta(y):
            if not lx or not ly:continue
            inv=a.ONE
            for gen in rx+ry:
                word,power=a.GENS[gen]
                assert power==0 and len(word)==1
                inv=m(inv,a.antipode_label(a.LABELS[word[0]]))
            out=xx(out,m(br(frozenset({lx}),frozenset({ly})),inv))
    return out
terms=[('a_I10_'+str(i),normalized_bracket(aa,v)) for i,v in enumerate(ints10)]
terms += [('c_I8_'+str(i),normalized_bracket(c,v)) for i,v in enumerate(ints8)]
terms += [('de_R',normalized_bracket(xx(d,e),R)),
          ('f_DE',normalized_bracket(a.named('u3'),xx(a.D,a.E6))),
          ('h_u',normalized_bracket(a.named('uw'),u))]
terms += [
    ('Tor_a_N',normalized_bracket(aa,B5)),
    ('Tor_a_K1',xx(normalized_bracket(b,K1),normalized_bracket(aa,B1))),
    ('Tor_a_K5',xx(normalized_bracket(b,K5),normalized_bracket(aa,B7))),
    ('Tor_a_Ksum',xx(normalized_bracket(b,Ksum),normalized_bracket(aa,B4))),
    ('Tor_c_R',normalized_bracket(d,R)),
    ('Tor_de_DE',xx(normalized_bracket(a.named('v2'),xx(a.D,a.E6)),
                    normalized_bracket(xx(d,e),a.S))),
    ('Tor_f_u',normalized_bracket(a.named('u3'),a.D))]
terms += [('BB_de_h',normalized_two_labels(xx(d,e),a.named('uw'))),
          ('BB_f_f',normalized_two_labels(a.named('u3'),a.named('u3'))),
          ('BB_Tor_c_h',normalized_two_labels(d,a.named('uw'))),
          ('BB_Tor_de_f',xx(normalized_two_labels(xx(d,e),a.named('u2v')),
                            normalized_two_labels(a.named('v2'),a.named('u3'))))]
sp,nk=a.LSPACE[13]
span=a.Span();outs=[]
for name,x in terms:
    a.ESPACE[13].coords(a.vector(x,13))
    v=sp.coords(a.vector(x,13))>>nk
    span.add(v)
    print(name,[id for i,id in enumerate(a.LIDS[13]) if v>>i&1])
    outs.append((name,v))
piv={};ker=[]
for j,v in enumerate(span.vectors):
    x=a.EMPTY
    for i,ambient in enumerate(a.LBAS[13]):
        if v>>i&1:x=xx(x,a.poly(ambient,13))
    out=0;off=0
    for q in (1,2,4,8):
        spp,nn=a.LSPACE[13-q]
        cc=spp.coords(a.vector(a.sq(q,x),13-q))>>nn
        out^=cc<<off;off+=len(a.LBAS[13-q])
    cc=1<<j
    while out:
        j0=out.bit_length()-1
        if j0 not in piv:break
        vv,c0=piv[j0];out^=vv;cc^=c0
    if out:piv[out.bit_length()-1]=(out,cc)
    else:ker.append(cc)
print('integral action image rank',len(span.vectors),'primary intersection',len(ker))
for cc in ker:
    v=0
    for i,w in enumerate(span.vectors):
        if cc>>i&1:v^=w
    print('intersection',[id for i,id in enumerate(a.LIDS[13]) if v>>i&1])
