"""Independent finite table checks for BISITE B.15, using the common verifier."""
import contextlib, io, json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    from bc_counterexamples import Category, poset, fundamental_presentation, le, twist


def components(C):
    unseen=set(C.objects); out=[]
    while unseen:
        component={next(iter(unseen))}
        while True:
            new=component|{C.src(a) for a in C.arrows if C.tgt(a) in component}|{C.tgt(a) for a in C.arrows if C.src(a) in component}
            if new==component:break
            component=new
        unseen-=component;out.append(component)
    return out


def lift_category(C,color,x,b,incoming):
    if incoming:
        objs=[u for u in C.arrows if C.tgt(u)==x and color(C.src(u))==b]
        ar=[(u,v,a) for u in objs for v in objs for a in C.arrows
            if C.src(a)==C.src(u) and C.tgt(a)==C.src(v) and C.compose(v,a)==u]
        ident=lambda u:(u,u,C.ident(C.src(u)))
    else:
        objs=[u for u in C.arrows if C.src(u)==x and color(C.tgt(u))==b]
        ar=[(u,v,a) for u in objs for v in objs for a in C.arrows
            if C.src(a)==C.tgt(u) and C.tgt(a)==C.tgt(v) and C.compose(a,u)==v]
        ident=lambda u:(u,u,C.ident(C.tgt(u)))
    L=Category(objs,ar,lambda a:a[0],lambda a:a[1],ident,lambda b,a:(a[0],b[1],C.compose(b[2],a[2])))
    laws=L.verify()
    ini=[z for z in objs if all(sum(L.src(a)==z and L.tgt(a)==w for a in ar)==1 for w in objs)]
    ter=[z for z in objs if all(sum(L.src(a)==w and L.tgt(a)==z for a in ar)==1 for w in objs)]
    return L,dict(laws,components=len(components(L)),initial=len(ini),terminal=len(ter))


def check_colored(C,color):
    assert all(color(C.src(a))<=color(C.tgt(a)) for a in C.arrows)
    lifts={}
    for x in C.objects:
        for b in [0,1]:
            for incoming in [False,True]:
                if (b<=color(x)) if incoming else (color(x)<=b):
                    L,result=lift_category(C,color,x,b,incoming)
                    if L.objects and len(components(L))==1 and not(result['initial'] or result['terminal']):
                        result['fundamental_presentation']=fundamental_presentation(L)
                    lifts[f'{"incoming" if incoming else "outgoing"}:{x}:{b}']=result
    fibres={b:Category([x for x in C.objects if color(x)==b],
        [a for a in C.arrows if color(C.src(a))==color(C.tgt(a))==b],C.src,C.tgt,C.ident,C.compose) for b in [0,1]}
    return {'laws':C.verify(),'lifts':lifts,'fibre_components':{b:len(components(F)) for b,F in fibres.items()},
            'fundamental_presentation':fundamental_presentation(C)}

B3ar=[('a','a',0)]+[('b','b',g) for g in [0,1]]+[('a','b',g) for g in [0,1]]
B3=Category(['a','b'],B3ar,lambda u:u[0],lambda u:u[1],lambda x:(x,x,0),lambda v,u:(u[0],v[1],(u[2]+v[2])%2))
E3ar=[(*u,z) for u in B3ar for z in [0,1]]
E3=Category([(x,z) for x in B3.objects for z in [0,1]],E3ar,
            lambda u:(u[0],u[3]),lambda u:(u[1],(u[3]+u[2])%2),lambda x:(x[0],x[0],0,x[1]),
            lambda v,u:(u[0],v[1],(u[2]+v[2])%2,u[3]))
# Both source- and target-prescribed lifts exist uniquely for every base arrow.
for u in B3.arrows:
    for x in E3.objects:
        if x[0]==B3.src(u): assert sum(a[:3]==u and E3.src(a)==x for a in E3.arrows)==1
        if x[0]==B3.tgt(u): assert sum(a[:3]==u and E3.tgt(a)==x for a in E3.arrows)==1

B4=poset(list(range(15)),lambda x,y:x==y or (x==0 and y>0 and le(1,y)) or (x>0 and y>0 and le(x,y)))
r=lambda x:1 if x==0 else x
E4ar=[(x,y,m) for x,y in B4.arrows for m in [0,1]]
E4=Category(B4.objects,E4ar,lambda u:u[0],lambda u:u[1],lambda x:(x,x,0),
            lambda v,u:(u[0],v[1],(u[2]+v[2]+twist(r(u[0]),r(u[1]),r(v[1])))%2))

Rar=[(0,0,0),(0,0,1),(0,1,0),(1,1,0)]
R=Category([0,1],Rar,lambda u:u[0],lambda u:u[1],lambda x:(x,x,0),
           lambda v,u:(u[0],v[1],(u[2]+v[2])%2 if u[0]==v[1]==0 else 0))
out={
'D3_B':check_colored(B3,lambda x:int(x=='b')),
'D3_E':check_colored(E3,lambda x:int(x[0]=='b')),
'D4_B':check_colored(B4,lambda x:int(x!=0)),
'D4_E':check_colored(E4,lambda x:int(x!=0)),
'D5_R':check_colored(R,lambda x:x)}
assert out['D3_B']['lifts']['incoming:b:0']['components']==2
assert out['D3_E']['fibre_components']=={0:2,1:1}
assert out['D4_B']['fundamental_presentation']['remaining_generators']==0
assert out['D4_E']['fundamental_presentation']['remaining_generators']==0
assert out['D4_E']['laws']['associative_triples']==2064
assert out['D5_R']['lifts']['incoming:1:0']['fundamental_presentation']['remaining_generators']==1
assert out['D5_R']['fundamental_presentation']['remaining_generators']==0
path=Path(__file__).with_suffix('.out.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
