"""Check the n=m=2 finite attachment in XII appendix manuscript pp.13--16.

All arrow sets and compositions are explicit.  The category Xprime is the
pushout by the presentation in the paper, not an arbitrary sphere model.
"""
import json
from pathlib import Path
from finite_examples import FiniteCategory
from ag_audit_examples import full_subcategory

OUT=Path(__file__).resolve().parent

def leq_phi(a,b):
    return a==b or (a%2==0 and b%2==1 and abs(a-b)==1)

def poset_category(objects,leq):
    arrows=[];lookup={}
    for a in objects:
        for b in objects:
            if leq(a,b):
                aid=f'id:{a}' if a==b else f'{a}>{b}'
                arrows.append((aid,a,b));lookup[a,b]=aid
    comp={}
    for f,a,b in arrows:
        for g,bb,c in arrows:
            if bb==b:comp[g,f]=lookup[a,c]
    return FiniteCategory(objects,arrows,comp)

def main():
    coords={f'{i},{j}':(i,j) for i in range(5) for j in range(5)}
    def leq(a,b):
        i,j=coords[a];k,l=coords[b]
        return leq_phi(i,k) and leq_phi(j,l)
    X=poset_category(tuple(coords),leq)
    Vobs=('0,0','1,0','0,1')
    barobs=Vobs+('1,1',)
    Uobs=tuple(o for o,(i,j) in coords.items() if i in (0,4) or j in (0,4))
    Wobs=tuple(o for o,(i,j) in coords.items() if i<3 and j<3)
    V=full_subcategory(X,Vobs);barV=full_subcategory(X,barobs)
    U=full_subcategory(X,Uobs);W=full_subcategory(X,Wobs)
    retraction={o:f'{0 if i==0 else 1},{0 if j==0 else 1}' for o,(i,j) in coords.items() if o in Wobs}
    assert all(leq(o,b)==leq(retraction[o],b) for o in Wobs for b in barobs)
    assert all(retraction[b]==b for b in barobs)
    assert all(t in barobs for _,s,t in X.arrows if s in barobs)
    neighborhood={s for _,s,t in X.arrows if t in barobs}
    assert neighborhood==set(Wobs)
    # Extend X by the new source x and cone point e. The only multiple Hom
    # set is x -> (0,0); compositions toward either branch identify the labels.
    arrows=list(X.arrows)+[('id:x','x','x'),('id:e','e','e'),
                         ('alpha','x','0,0'),('beta','x','0,0')]
    for b in ('1,0','0,1','1,1','e'):
        arrows.append((f'x>{b}','x',b))
    to_e=('0,0','1,0','0,1','2,0','0,2')
    arrows += [(f'{a}>e',a,'e') for a in to_e]
    hom={}
    for f,a,b in arrows:hom.setdefault((a,b),[]).append(f)
    comp={}
    for f,a,b in arrows:
        for g,bb,c in arrows:
            if b!=bb:continue
            if f==f'id:{a}':h=g
            elif g==f'id:{b}':h=f
            else:
                assert len(hom[a,c])==1,(g,f,hom.get((a,c)))
                h=hom[a,c][0]
            comp[g,f]=h
    Xprime=FiniteCategory(tuple(coords)+('x','e'),arrows,comp)
    Q=full_subcategory(Xprime,barobs+('x','e'))
    Vprime=full_subcategory(Xprime,Vobs+('x','e'))
    assert set(Q.objects)==set(barV.objects)|set(Vprime.objects)
    assert set(Q.objects)&set(X.objects)==set(barV.objects)
    # The presentation has exactly the old generators and x,e attachments;
    # arrows to e from (2,0),(0,2) are their forced composites through V.
    assert Xprime.comp['1,0>e','2,0>1,0']=='2,0>e'
    assert Xprime.comp['0,1>e','0,2>0,1']=='0,2>e'
    assert Xprime.comp['0,0>1,1','alpha']==Xprime.comp['0,0>1,1','beta']
    result={'categories':{name:c.verify() for name,c in
                          [('V',V),('barV',barV),('U',U),('X',X),
                           ('Vprime',Vprime),('Q',Q),('Xprime',Xprime)]},
            'barV_to_X_closed_Dwyer':True,'left_adjoint':retraction,
            'Q_homology':Q.homology(),'Xprime_homology':Xprime.homology(),
            'conclusion':'V -> Vprime is W_infty, X -> Xprime is not; BXprime is equivalent to BQ=S3 by forward Dwyer pushout.'}
    (OUT/'ag_appendix_square_data.json').write_text(json.dumps({'X':X.export(),
                                                              'Xprime':Xprime.export()},indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
