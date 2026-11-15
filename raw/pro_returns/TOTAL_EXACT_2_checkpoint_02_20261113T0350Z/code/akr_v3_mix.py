"""Two admissible repaired AKR substages mixing the third W-coordinate.

These are finite substages, not complete later stages. The point branch
uses v1 versus v3 in P12; the cross branch uses the sum P12+P13.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import json
from akr_stage_model import Cat, quotient_H, run


def stage_one():
    C = Cat()
    V = C.obj('V', 1)
    W = C.obj('W', 3)
    for i in range(3):
        C.hom[V, W].add((i,))
    original = {(x, y): sorted(fs) for (x, y), fs in C.hom.items()}
    for (x, y), fs in sorted(original.items()):
        for i, f in enumerate(fs):
            for j, g in enumerate(fs):
                C.qfilter(f'Q_{x}_{y}_{i}_{j}', x, y, f, g, 45, 3)
    for x in (V, W):
        for y in (V, W):
            C.sum(f'S_{x}_{y}', x, y)
    return C


def build(mode):
    C = stage_one()
    left = C.names.index('Q_0_1_0_1')
    if mode in ('point_v3', 'point_13_edge'):
        if mode == 'point_13_edge':
            left = C.names.index('Q_0_1_0_2')
        b = sorted(C.hom[1, left])[0]
        f, g = (b[0],), (b[2] if mode == 'point_v3' else b[1],)
        old_count = len(C.size)
        name = 'Q_K2_point_pair_v1_v3' if mode == 'point_v3' else 'Q_K2_P13_binary_edge_pair'
        z, n = C.qfilter(name, 0, left, f, g, 153, 3)
        parameters = ['2', '8/5', '128/85']
        assert Fraction(9, 153) <= 1 - Fraction(128, 85) / Fraction(8, 5)
        pair = {'source': 'V', 'target': C.names[left], 'f': f, 'g': g}
    elif mode == 'cross_13':
        right = C.names.index('Q_0_1_0_2')
        t = C.sum('S_K2_P12_P13', left, right)
        lf = next(iter(C.hom[left, t]))
        rg = next(iter(C.hom[right, t]))
        f = tuple(lf[j] for j in sorted(C.hom[1, left])[0])
        g = tuple(rg[j] for j in sorted(C.hom[1, right])[0])
        old_count = len(C.size)
        z, n = C.qfilter('Q_K3_cross_P12_P13', 1, t, f, g, 297, 3)
        a2 = Fraction(8, 5) * Fraction(64, 65)
        a3 = a2 * Fraction(32, 33)
        assert a2 > Fraction(3, 2) and a3 > Fraction(3, 2)
        assert Fraction(9, 297) <= 1 - a3 / a2
        parameters = ['2', '8/5', str(a2), str(a3)]
        pair = {'source': 'W', 'target': C.names[t], 'f': f, 'g': g}
    else:
        raise ValueError(mode)
    assert n == 3
    return C, z, old_count, {'mode': mode, 'a_parameters': parameters, 'pair': pair}


def graph_summary(C, z):
    vals, labels = quotient_H(C)
    edges = C.hom[1, z]
    endpoints = {v for e in edges for v in e[:2]}
    thirds = {e[2] for e in edges}
    protected = [C.names.index(name) for name in ('Q_0_1_0_1', 'Q_0_1_1_0')]
    cycle_rank = len(edges) - len(C.hom[0, z]) + len(vals[z])
    protected_copies = sum(len(C.hom.get((p, z), ())) for p in protected)
    component_sizes = Counter(labels[z].values())
    return {
        'objects': len(C.size), 'arrows': sum(len(fs) for fs in C.hom.values()),
        'top': C.names[z], 'top_size': C.size[z],
        'vertices': len(C.hom[0, z]), 'edges': len(edges),
        'graph_components': len(vals[z]),
        'component_size_histogram': dict(sorted(Counter(component_sizes.values()).items())),
        'graph_cycle_rank': cycle_rank, 'protected_copies': protected_copies,
        'quotient_M_rank': cycle_rank - protected_copies,
        'third_points_also_edge_endpoints': len(thirds & endpoints),
        'total_third_points': len(thirds),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('point_v3', 'point_13_edge', 'cross_13'))
    parser.add_argument('--nerve', action='store_true')
    args = parser.parse_args()
    C, z, old_count, metadata = build(args.mode)
    C.verify()
    metadata['graph'] = graph_summary(C, z)
    print(json.dumps(metadata, sort_keys=True), flush=True)
    if args.nerve:
        result = run(C, 'K1_plus_' + args.mode, old_count)
        Path(__file__).with_name('akr_v3_mix_' + args.mode + '.json').write_text(
            json.dumps({'metadata': metadata, 'nerve': result}, indent=2))


if __name__ == '__main__':
    main()
