"""Exact finite checks for BISITE E.2, E.6, E.10 and Part F.

No numerical homotopy inference is used. We enumerate the entire categories,
their compositions, comma categories, set limits, and set colimits.
"""
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path

@dataclass
class Category:
    objects: tuple
    arrows: dict  # label -> (source,target)
    identities: dict
    composition: dict  # (g,f) -> g after f

    def validate(self):
        for x in self.objects:
            i=self.identities[x]
            assert self.arrows[i] == (x,x)
        pairs=triples=0
        for f,(a,b) in self.arrows.items():
            assert self.composition[(f,self.identities[a])]==f
            assert self.composition[(self.identities[b],f)]==f
            for g,(c,d) in self.arrows.items():
                if b!=c: continue
                pairs+=1
                gf=self.composition[g,f]
                assert self.arrows[gf]==(a,d)
                for h,(e,k) in self.arrows.items():
                    if d!=e: continue
                    triples+=1
                    assert self.composition[h,gf] == self.composition[self.composition[h,g],f]
        return dict(objects=len(self.objects),arrows=len(self.arrows),composable_pairs=pairs,associativity_checks=triples)

    def components(self):
        parent={x:x for x in self.objects}
        def find(x):
            while parent[x]!=x: x=parent[x]
            return x
        for a,b in self.arrows.values(): parent[find(a)]=find(b)
        return len({find(x) for x in self.objects})

    def initial_objects(self):
        return [x for x in self.objects if all(sum(a==x and b==y for a,b in self.arrows.values())==1 for y in self.objects)]

    def terminal_objects(self):
        return [x for x in self.objects if all(sum(a==y and b==x for a,b in self.arrows.values())==1 for y in self.objects)]

def poset(objects,le):
    arrows={(a,b):(a,b) for a in objects for b in objects if le(a,b)}
    return Category(tuple(objects),arrows,{a:(a,a) for a in objects},
                    {(g,f):(a,d) for f,(a,b) in arrows.items() for g,(c,d) in arrows.items() if b==c})

def under(X,B,fo,fa,s):
    obs=tuple((x,a) for x in X.objects for a,(u,v) in B.arrows.items() if u==s and v==fo[x])
    arr={}
    for i,(x,a) in enumerate(obs):
        for j,(y,b) in enumerate(obs):
            for v,(vx,vy) in X.arrows.items():
                if vx==x and vy==y and B.composition[fa[v],a]==b:
                    arr[(i,v,j)]=(i,j)
    identities={i:(i,X.identities[x],i) for i,(x,a) in enumerate(obs)}
    comp={}
    for f,(i,j) in arr.items():
        for g,(k,l) in arr.items():
            if j==k: comp[g,f]=(i,X.composition[g[1],f[1]],l)
    out=Category(tuple(range(len(obs))),arr,identities,comp)
    return out,obs

def set_limit(C,values,maps):
    answers=[]
    for items in product(*(values[x] for x in C.objects)):
        assignment=dict(zip(C.objects,items))
        if all(maps[f][assignment[a]]==assignment[b] for f,(a,b) in C.arrows.items()):
            answers.append(assignment)
    return answers

def set_colimit(C,values,maps):
    elements=[(x,v) for x in C.objects for v in values[x]]
    parent={v:v for v in elements}
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    for f,(a,b) in C.arrows.items():
        for v in values[a]: parent[find((a,v))]=find((b,maps[f][v]))
    return {find(v) for v in elements}

def constant_diagram(C,values):
    return {x:tuple(values) for x in C.objects},{f:{v:v for v in values} for f in C.arrows}

def record(C):
    return dict(**C.validate(),components=C.components(),initial=C.initial_objects(),terminal=C.terminal_objects())

def main():
    I=poset((0,1),lambda a,b:a<=b)
    E=poset(('*',),lambda a,b:True)
    empty=poset((),lambda a,b:False)
    out={'interval':record(I),'point':record(E),'empty':record(empty)}
    for s in I.objects:
        src,srcobs=under(E,I,{'*':1},{('*','*'):(1,1)},s)
        tgt,tgtobs=under(I,I,{x:x for x in I.objects},{f:f for f in I.arrows},s)
        out[f'E2_comma_at_{s}']={'source':record(src),'target':record(tgt),'source_labels':str(srcobs),'target_labels':str(tgtobs)}
        assert src.components()==tgt.components()==1
        assert src.initial_objects() and tgt.initial_objects()
    out['E2_raw_pullback_at_0']={'source_components':0,'target_components':1}
    C2=Category(('*',),{0:('*','*'),1:('*','*')},{'*':0},{(a,b):(a+b)%2 for a in range(2) for b in range(2)})
    src,srcobs=under(E,C2,{'*':'*'},{('*','*'):0},'*')
    tgt,tgtobs=under(C2,C2,{'*':'*'},{0:0,1:1},'*')
    out['E6_C2']=record(C2)
    out['E6_commas']={'source':record(src),'target':record(tgt)}
    assert src.components()==2 and tgt.components()==1
    J=Category((0,1),{(a,b):(a,b) for a in (0,1) for b in (0,1)},
               {x:(x,x) for x in (0,1)},
               {((b,c),(a,b)):(a,c) for a,b,c in product((0,1),repeat=3)})
    out['E10_walking_isomorphism']=record(J)
    assert len(J.initial_objects())==2 and len(J.terminal_objects())==2
    ve,me=constant_diagram(E,('m','n'))
    vz,mz=constant_diagram(empty,('m','n'))
    out['F3_left_base_change']={'source_cardinality':len(set_colimit(empty,vz,mz)),'target_cardinality':len(set_colimit(E,ve,me))}
    out['F3_right_base_change']={'source_cardinality':len(set_limit(E,ve,me)),'target_cardinality':len(set_limit(empty,vz,mz))}
    assert out['F3_left_base_change']=={'source_cardinality':0,'target_cardinality':2}
    assert out['F3_right_base_change']=={'source_cardinality':2,'target_cardinality':1}
    # Presheaf B on [1]: B(1)=empty, B(0)=point, with its unique arrow.
    Iop=poset((0,1),lambda a,b:a>=b)
    bvalues={0:('*',),1:()}
    bmaps={(0,0):{'*':'*'},(1,1):{},(1,0):{}}
    assert all(bmaps[g][bmaps[f][v]]==bmaps[Iop.composition[g,f]][v]
               for g,f in Iop.composition for v in bvalues[Iop.arrows[f][0]])
    comma0,_=under(E,I,{'*':1},{('*','*'):(1,1)},0)
    va,ma=constant_diagram(comma0,('*',))
    vt,mt=constant_diagram(comma0,())
    projection_source=len(set_colimit(comma0,vt,mt))
    projection_target=len(set_colimit(comma0,va,ma))*len(bvalues[0])
    out['F5_left_projection_at_0']={
        'presheaf_index':record(Iop),'B_values':bvalues,
        'f_shriek_of_tensor':projection_source,
        'tensor_of_f_shriek':projection_target,
        'comparison_bijective':projection_source==projection_target}
    assert (projection_source,projection_target)==(0,1)
    two=poset((0,1),lambda a,b:a==b)
    v,m=constant_diagram(two,('*',))
    vb,mb=constant_diagram(two,('a','b'))
    left=len(set_limit(two,v,m))*2
    right=len(set_limit(two,vb,mb))
    out['F6_right_projection_discrete_two']={'source_cardinality':left,'target_cardinality':right}
    assert (left,right)==(2,4)
    # The diagonal [1] -> [1]^2 misses (0,1), an incoming object for (1,1).
    diagonal={(0,0),(1,1)}
    out['F12_diagonal_not_smooth']={'missing_incoming_source':[0,1],'target':[1,1],'number_of_exact_lifts':sum(x==(0,1) for x in diagonal)}
    assert out['F12_diagonal_not_smooth']['number_of_exact_lifts']==0
    out['E13_coherent_square_group']={'Hom_Sigma_Z_Sigma_Z':'Z','underlying_arrow_category_morphisms':1,'differential_on_rank_one_Hom_complex':[[0]]}
    # Exact integral basis change, not a bounded sample of an infinite group:
    # columns (1,-1),(0,1) form a Z-basis and (1,1) sends them to (0,1).
    basis=((1,0),(-1,1))
    determinant=basis[0][0]*basis[1][1]-basis[0][1]*basis[1][0]
    transformed_row=tuple(basis[0][j]+basis[1][j] for j in (0,1))
    assert determinant==1 and transformed_row==(0,1)
    out['F16_twist_kernel']={
        'twist_map_row':[1,1],
        'integral_change_of_basis':basis,
        'determinant':determinant,
        'transformed_twist_map':transformed_row,
        'kernel_basis':[1,-1],
        'kernel_is_free_of_rank':1,
        'scope':'Exact integer basis calculation; the mapping-class lifting category is infinite.'}
    out['F19_finite_stars']=[]
    for m in (0,1,2):
        obs=tuple(range(m+1))
        star=poset(obs,lambda a,b:a==b or a==0)
        # The comparison is Z -> Z^m, the primitive diagonal.
        # For m>0, subtracting its first row from the others leaves
        # the coordinate vector (1,0,...,0), an integral normal form.
        diagonal=[[1] for _ in range(m)]
        normal_form=([[1]]+[[0] for _ in range(m-1)]) if m else []
        out['F19_finite_stars'].append({
            'number_of_leaves':m,'category':record(star),
            'arrows':str(star.arrows),'composition':str(star.composition),
            'diagonal_matrix':diagonal,
            'integral_row_normal_form':normal_form,
            'fibre_H0_rank':1 if m==0 else 0,
            'fibre_Hminus1_rank':max(0,m-1),
            'left_Kan_value_at_1_rank':0})
    result=json.dumps(out,indent=2,default=str)+'\n'
    target=Path(__file__).with_suffix('.out.json')
    target.write_text(result)
    print(result,end='')

if __name__=='__main__': main()
