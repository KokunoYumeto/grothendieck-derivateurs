"""Finite stress test for the singular binary word v[a,u]v^-1.

The computation is only a finite certificate.  No universal group statement
is inferred from a failure to find a collapsing range.
"""

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def alternating_tables(n):
    perms = np.array(
        [p for p in itertools.permutations(range(n))
         if sum(p[i] > p[j] for i in range(n) for j in range(i+1,n)) % 2 == 0],
        dtype=np.int16,
    )
    powers = n ** np.arange(n, dtype=np.int64)
    lookup = np.full(n**n, -1, dtype=np.int32)
    lookup[(perms * powers).sum(axis=1)] = np.arange(len(perms))
    prod = np.empty((len(perms),len(perms)),dtype=np.int16)
    for i,p in enumerate(perms):
        prod[i] = lookup[(p[perms] * powers).sum(axis=1)]
    inv = lookup[(np.argsort(perms,axis=1) * powers).sum(axis=1)]
    conj = prod[prod,inv[:,None]]
    comm = prod[conj,inv[None,:]]
    identity = int(lookup[(np.arange(n) * powers).sum()])
    return perms,prod,inv,conj,comm,identity


def run(n, depth, width, trials, seed):
    perms,prod,inv,conj,comm,identity = alternating_tables(n)
    rng = np.random.default_rng(seed)
    order = len(perms)
    full = np.arange(order,dtype=np.int16)

    def transform(r,a):
        comm_values = np.unique(comm[a,r])
        return np.unique(conj[r[:,None], comm_values[None,:]])

    # One representative for every conjugacy class gives an exhaustive
    # certificate for the cardinalities of T_a(F,F).
    unseen = set(range(order)) - {identity}
    initial = []
    representatives = []
    while unseen:
        a = min(unseen)
        cl = set(map(int,conj[:,a]))
        unseen.difference_update(cl)
        representatives.append(a)
        r = transform(full,a)
        initial.append({"a":int(a),"permutation":perms[a].tolist(),
                        "class_size":len(cl),"range_size":len(r)})
    smallest_class = min(initial,key=lambda z:z["range_size"])["a"]
    critical_coefficients = list(map(int,np.unique(conj[:,smallest_class])))
    beam = [(full,[])]
    layers = []
    witness = None
    for k in range(depth):
        candidates = {}
        for r,path in beam:
            aa = representatives + critical_coefficients + list(map(int,rng.choice(order,trials,replace=False)))
            for a in aa:
                if a == identity:
                    continue
                # In a fixed-root diagonal prefix the non-root coefficients
                # are distinct. Keep this stronger test constraint.
                if a in [pair[0] for pair in path]:
                    continue
                s = transform(r,a)
                for b in [identity,*map(int,rng.choice(order,4,replace=False))]:
                    out = np.sort(prod[s,b])
                    key = out.tobytes()
                    if key not in candidates:
                        candidates[key] = (out,path+[[int(a),int(b)]])
        vals = list(candidates.values())
        rng.shuffle(vals)
        vals.sort(key=lambda v:len(v[0]))
        beam=vals[:width]
        best_r,best_path=beam[0]
        layers.append({"depth":k+1,"minimum_sampled_range":len(best_r),
                       "distinct_candidates":len(vals),"path":best_path})
        print(json.dumps(layers[-1]),flush=True)
        if len(best_r)==1:
            witness={"path":best_path,"value":int(best_r[0])}
            break
    return {"group":f"A_{n}","order":order,"seed":seed,
            "binary_word":"v[a,u]v^-1",
            "iteration":"R_next={v[a,u]v^-1 b : u,v in R}",
            "initial_class_certificate":initial,"sampled_layers":layers,
            "constant_range_witness":witness,
            "scope":"Only the initial conjugacy-class computation is exhaustive; later layers are a deterministic finite search."}


if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=7)
    p.add_argument("--depth",type=int,default=8)
    p.add_argument("--width",type=int,default=4)
    p.add_argument("--trials",type=int,default=5)
    p.add_argument("--seed",type=int,default=20261114)
    p.add_argument("--output",default="INDLOCAL/research/Cpaths_binary_ranges.json")
    a=p.parse_args()
    result=run(a.n,a.depth,a.width,a.trials,a.seed)
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"initial":result["initial_class_certificate"],
                      "witness":result["constant_range_witness"]}),flush=True)
