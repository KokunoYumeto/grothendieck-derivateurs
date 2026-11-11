#!/usr/bin/env python3
"""Exact finite checks for Lead 3 and rectangular-band classifications.

Multiplication g*f means composition g after f.  Integral chain groups are
normalized nerve chains.  The proof of higher homotopy types is in the paper;
finite truncations here are independent checks, not substitutes for that proof.
"""
from itertools import product
from pathlib import Path
import json

from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

from ag_finite_examples import Cat


def monoid(elements, multiply):
    arrows = [dict(name=str(m), source='*', target='*', identity=(m == '1'))
              for m in elements]
    index = {m: i for i, m in enumerate(elements)}
    table = {(index[g], index[f]): index[multiply(g, f)]
             for g, f in product(elements, repeat=2)}
    return Cat(['*'], arrows, table)


def elements_category(cat, values, action):
    objects = [(a, h) for a in cat.objects for h in values[a]]
    arrows, tags = [], []
    for i, a in enumerate(cat.arrows):
        for h in values[a['source']]:
            arrows.append(dict(name=f"{a['name']}@{h}",
                               source=(a['source'], h),
                               target=(a['target'], action[i, h]),
                               identity=a['identity']))
            tags.append((i, h))
    index = {x: i for i, x in enumerate(tags)}
    table = {}
    for f, a in enumerate(arrows):
        for g, b in enumerate(arrows):
            if a['target'] == b['source']:
                gi, _ = tags[g]
                fi, h = tags[f]
                table[g, f] = index[cat.composites[gi, fi], h]
    return Cat(objects, arrows, table)


def collage(cat, values, action):
    arrows = [dict(a) for a in cat.arrows]
    arrows.append(dict(name='id_x', source='x', target='x', identity=True))
    cross = {}
    for a in cat.objects:
        for h in values[a]:
            cross[a, h] = len(arrows)
            arrows.append(dict(name=f'x->{a}:{h}', source='x', target=a, identity=False))
    table = dict(cat.composites)
    reverse = {i: (a, h) for (a, h), i in cross.items()}
    for f, a in enumerate(arrows):
        for g, b in enumerate(arrows):
            if a['target'] != b['source'] or (g, f) in table:
                continue
            if a['identity']:
                result = g
            elif b['identity']:
                result = f
            else:
                _, h = reverse[f]
                result = cross[b['target'], action[g, h]]
            table[g, f] = result
    return Cat(cat.objects + ['x'], arrows, table)


def homology(cat, max_degree=4):
    chains = [[(a,) for a in cat.objects]]
    nonids = [i for i, a in enumerate(cat.arrows) if not a['identity']]
    chains.append([(i,) for i in nonids])
    for n in range(2, max_degree + 2):
        chains.append([s+(i,) for s in chains[-1] for i in nonids
                       if cat.arrows[s[-1]]['target'] == cat.arrows[i]['source']])
    boundaries = [zeros(0, len(chains[0]))]
    smiths = [[]]
    for n in range(1, max_degree + 2):
        rows = {s:i for i,s in enumerate(chains[n-1])}
        d = zeros(len(rows), len(chains[n]))
        for j,s in enumerate(chains[n]):
            if n == 1:
                a = cat.arrows[s[0]]
                faces = [((a['target'],), 1), ((a['source'],), -1)]
            else:
                faces = [(s[1:],1), (s[:-1],(-1)**n)]
                for k in range(1,n):
                    comp = cat.composites[s[k],s[k-1]]
                    if not cat.arrows[comp]['identity']:
                        faces.append((s[:k-1]+(comp,)+s[k+1:],(-1)**k))
            for face,sign in faces:
                d[rows[face],j] += sign
        assert boundaries[-1]*d == zeros(boundaries[-1].rows,d.cols)
        boundaries.append(d)
        sd = smith_normal_form(d,domain=ZZ)
        smiths.append([abs(int(sd[i,i])) for i in range(min(sd.shape)) if sd[i,i]])
    return dict(simplex_counts=[len(x) for x in chains],
                homology=[dict(degree=n,
                               free_rank=len(chains[n])-len(smiths[n])-len(smiths[n+1]),
                               torsion=[a for a in smiths[n+1] if a>1])
                          for n in range(max_degree+1)],
                boundary_squared_zero=True)


def export(cat):
    return dict(objects=cat.objects,arrows=cat.arrows,
                composites=[dict(after=g,before=f,result=h)
                            for (g,f),h in sorted(cat.composites.items())])


def main():
    def multiply(g,f):
        return f if g=='1' else g if f=='1' else f
    m = monoid(['1','e','f'],multiply)
    values = {'*':['h','i']}
    action = {(i,h):h if a['identity'] else 'i'
              for i,a in enumerate(m.arrows) for h in values['*']}
    for g,f in product(range(3),repeat=2):
        for h in values['*']:
            assert action[g,action[f,h]]==action[m.composites[g,f],h]
    e = elements_category(m,values,action)
    c = collage(m,values,action)
    records = {}
    for name,cat,expected in [('right_zero_monoid',m,[1,0,0,0,0]),
                              ('element_category',e,[1,1,0,0,0]),
                              ('final_collage',c,[1,0,1,0,0])]:
        record = dict(validation=cat.validate(), chains=homology(cat))
        assert [h['free_rank'] for h in record['chains']['homology']]==expected
        assert all(not h['torsion'] for h in record['chains']['homology'])
        records[name] = record
    bands = []
    for r,s in product(range(1,4),repeat=2):
        es = ['1']+list(product(range(r),range(s)))
        def mult(g,f):
            return f if g=='1' else g if f=='1' else (g[0],f[1])
        band = monoid(es,mult)
        band.validate()
        filtered = all(any(mult(c,a)==mult(c,b) for c in es) for a,b in product(es,repeat=2))
        cofiltered = all(any(mult(a,c)==mult(b,c) for c in es) for a,b in product(es,repeat=2))
        assert filtered==(s==1)
        assert cofiltered==(r==1)
        bands.append(dict(rows=r,columns=s,order=len(es),filtered=filtered,cofiltered=cofiltered))
    records['rectangular_band_checks'] = bands
    directory=Path(__file__).resolve().parent
    (directory/'root_monoid_data.json').write_text(json.dumps({n:export(cat) for n,cat in [('M',m),('El',e),('collage',c)]},indent=2))
    print(json.dumps(records,indent=2))


if __name__=='__main__':
    main()
