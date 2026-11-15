"""Test a proposed connected-image-intersection invariant, not totality.

Only the specified finite substages are built. All pairs of distinct
incoming image sets with source cardinality >=4 are tested. Source-W
arrows are deliberately outside this run; the scope is recorded exactly.
"""
import argparse,json
from collections import defaultdict
from akr_stage_model import Cat,quotient_H


def build(mode):
    C=Cat();V=C.obj('V',1);W=C.obj('W',3)
    for i in range(3):C.hom[V,W].add((i,))
    original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
    for (x,y),fs in sorted(original.items()):
        for i,f in enumerate(fs):
            for j,g in enumerate(fs):C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
    for x in (V,W):
        for y in (V,W):C.sum(f'S_{x}_{y}',x,y)
    if mode=='selected_k2':
        target=C.names.index('Q_0_1_0_1');f,g=sorted(C.hom[W,target])[:2]
        C.qfilter('Q_K2_selected',W,target,f,g,153,3)
    if mode=='critical_k3':
        left=C.names.index('Q_0_1_0_1');right=C.names.index('Q_0_1_1_0')
        target=C.sum('S_K2_two_cycle_targets',left,right)
        lf=next(iter(C.hom[left,target]));rg=next(iter(C.hom[right,target]))
        f=tuple(lf[j] for j in sorted(C.hom[W,left])[0])
        g=tuple(rg[j] for j in sorted(C.hom[W,right])[0])
        C.qfilter('Q_K3_selected_cross_sum',W,target,f,g,297,3)
    return C


def vertices(mask):
    while mask:
        bit=mask&-mask;yield bit.bit_length()-1;mask-=bit


def check(C,closure=False):
    vals,labs=quotient_H(C);counts=[];failures=[]
    h_injective_failures=[];h_arrows_checked=0
    for (x,y),maps in C.hom.items():
        for f in maps:
            h_arrows_checked+=1
            images=[labs[y][f[h]] for h in vals[x]]
            if len(set(images))!=len(images):
                h_injective_failures.append({'source':C.names[x],'target':C.names[y],
                                             'map':f,'component_images':images})
    small_sources=[{'name':C.names[x],'size':C.size[x],
                    'H_components':len(vals[x]),
                    'has_bijective_W_arrow':any(len(set(f))==C.size[x]==3
                        for f in C.hom.get((1,x),()))}
                   for x in range(len(C.size)) if C.size[x]<=3]
    for z in range(len(C.size)):
        graph=defaultdict(set)
        for f in C.hom.get((1,z),()):
            graph[f[0]].add(f[1]);graph[f[1]].add(f[0])
        incoming={}
        for x in range(z+1):
            if C.size[x]<4:continue
            for f in C.hom.get((x,z),()):
                mask=sum(1<<v for v in f)
                incoming.setdefault(mask,(x,f))
        image_list=list(incoming);pairs=nontrivial=0;cache={}
        for index,left in enumerate(image_list):
            for right in image_list[:index]:
                pairs+=1;common=left&right
                if common.bit_count()<2:continue
                nontrivial+=1
                if common in cache:continue
                unseen=set(vertices(common));component_labels=set();parts=[]
                while unseen:
                    first=unseen.pop();todo=[first];part={first}
                    while todo:
                        v=todo.pop()
                        for w in graph[v]&unseen:
                            unseen.remove(w);part.add(w);todo.append(w)
                    label=labs[z][first]
                    parts.append(sorted(part))
                    if label in component_labels:
                        failures.append({'target':C.names[z],
                            'left_source':C.names[incoming[left][0]],
                            'right_source':C.names[incoming[right][0]],
                            'left_map':incoming[left][1],
                            'right_map':incoming[right][1],
                            'intersection':list(vertices(common)),
                            'intersection_components':parts})
                        break
                    component_labels.add(label)
                if len(cache)<100000:cache[common]=True
                if failures:break
            if failures:break
        closure_data={}
        if closure and not failures:
            known={mask:(mask,) for mask in image_list};queue=list(image_list);position=0
            closure_steps=0
            while position<len(queue) and not failures:
                current=queue[position];position+=1
                for generator in image_list:
                    closure_steps+=1;common=current&generator
                    if common.bit_count()<2 or common in known:continue
                    known[common]=known[current]+(generator,);queue.append(common)
                    if common in cache:continue
                    unseen=set(vertices(common));component_labels=set();parts=[]
                    while unseen:
                        first=unseen.pop();todo=[first];part={first}
                        while todo:
                            v=todo.pop()
                            for w in graph[v]&unseen:
                                unseen.remove(w);part.add(w);todo.append(w)
                        label=labs[z][first];parts.append(sorted(part))
                        if label in component_labels:
                            failures.append({'target':C.names[z],
                                'intersection':list(vertices(common)),
                                'number_of_arrow_images':len(known[common]),
                                'arrow_images':[list(vertices(m)) for m in known[common]],
                                'intersection_components':parts})
                            break
                        component_labels.add(label)
                    if len(cache)<100000:cache[common]=True
                    if failures:break
            closure_data={'intersection_closure_size_at_least_2':len(known),
                          'closure_steps':closure_steps,
                          'maximum_generators_in_recorded_intersection':max(map(len,known.values()),default=0)}
        counts.append({'target':C.names[z],'incoming_distinct_images':len(image_list),
                       'pairs':pairs,'intersections_size_at_least_2':nontrivial,**closure_data})
        print(json.dumps(counts[-1]),flush=True)
        if failures:break
    return {'objects':len(C.size),'minimum_source_size':4,'target_counts':counts,
            'failures':failures,'H_arrows_checked':h_arrows_checked,
            'H_injectivity_failures':h_injective_failures,
            'small_source_classification':small_sources}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',choices=['k1','selected_k2','critical_k3'],default='k1')
    ap.add_argument('--closure',action='store_true')
    args=ap.parse_args();result=check(build(args.stage),args.closure);result['stage']=args.stage
    result['finite_intersection_closure_tested']=args.closure
    print(json.dumps(result,indent=2),flush=True)
