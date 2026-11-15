"""Exact fixed-subgraph tests in the point-pair AKR substage.

Checks every parallel pair with source size >=4 in this finite subcategory.
For each pair it also checks every fixed-point subset of two distinct copy
maps in its next repaired beta attachment, using exact collision signatures
instead of constructing the very large target.  This is finite evidence,
not an induction or a proof of totality/non-totality.
"""

from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
import argparse
import json
import time

from akr_stage_model import quotient_H
from finite_akr_intersections import build as build_old


def build(slots=(0, 1), target_name='P12'):
    C = build_old('k1')
    target = C.names.index('Q_0_1_0_1' if target_name == 'P12' else 'Q_0_1_0_2')
    edge = sorted(C.hom[1, target])[0]
    name = 'Q_K2_point_pair' if slots == (0, 1) else f'Q_K2_point_pair_{slots[0]}_{slots[1]}'
    if target_name != 'P12':
        name += '_' + target_name
    z, n = C.qfilter(name, 0, target, (edge[slots[0]],), (edge[slots[1]],), 153, 3)
    assert n == 3
    return C, C.names.index('Q_0_1_0_1'), z


def graph_data(C):
    graphs = []
    for x in range(len(C.size)):
        graph = defaultdict(set)
        for b in C.hom.get((1, x), ()):
            graph[b[0]].add(b[1])
            graph[b[1]].add(b[0])
        graphs.append(graph)
    return graphs


def disconnected_subset(graph, labels, subset):
    by_ambient = defaultdict(set)
    for v in subset:
        by_ambient[labels[v]].add(v)
    for label, vertices in by_ambient.items():
        unseen = set(vertices)
        parts = []
        while unseen:
            first = unseen.pop()
            todo = [first]
            reached = {first}
            while todo:
                v = todo.pop()
                for w in graph[v] & unseen:
                    unseen.remove(w)
                    reached.add(w)
                    todo.append(w)
            parts.append(sorted(reached))
        if len(parts) > 1:
            # A full-graph path between disconnected fixed components.
            source, target = parts[0][0], parts[1][0]
            previous = {source: None}
            queue = deque([source])
            while target not in previous:
                v = queue.popleft()
                for w in graph[v]:
                    if w not in previous:
                        previous[w] = v
                        queue.append(w)
            path = [target]
            while previous[path[-1]] is not None:
                path.append(previous[path[-1]])
            path.reverse()
            return {'ambient_component': label, 'fixed_components': parts,
                    'connecting_path_outside_subset': path}
    return None


def relation_paths(f, g):
    fixed = {x for x, y in zip(f, g) if x == y}
    edges = {x: y for x, y in zip(f, g) if x != y}
    assert len(edges) == sum(x != y for x, y in zip(f, g))
    assert len(set(edges.values())) == len(edges)
    paths = []
    for source in sorted(set(edges) - set(edges.values())):
        path = [source]
        while path[-1] in edges:
            path.append(edges[path[-1]])
        paths.append(path)
    covered = {v for p in paths for v in p}
    active = set(edges) | set(edges.values())
    cycles = []
    unseen = active - covered
    while unseen:
        source = next(iter(unseen))
        cycle = [source]
        v = edges[source]
        while v != source:
            cycle.append(v)
            v = edges[v]
        cycles.append(cycle)
        unseen.difference_update(cycle)
    return fixed, paths, cycles


def next_parameters(max_path, permitted_loss):
    n = max(1, max_path)
    if n % 2 == 0:
        n += 1
    multiplier = (permitted_loss.denominator + permitted_loss.numerator - 1) // permitted_loss.numerator
    while (3 * n * multiplier) % 4 != 1:
        multiplier += 1
    s = 3 * n * multiplier
    assert Fraction(3 * n, s) <= permitted_loss
    assert s % 4 == 1 and s % (3 * n) == 0
    return s, n


def beta(i, position, path_length, s):
    k = (s - 1) // 4
    if i <= 2 * k:
        value = position + i
        return value if value <= 2 * k else value + 2 * k - path_length + 1
    value = position - i + 6 * k - path_length + 2
    return value if value > 2 * k else position - i + 4 * k


def collision_signatures(lengths, permitted_loss):
    """Enumerate every possible same-point equality pattern for alpha_i,j.

    Every pair with a nonzero signature is discovered at a collision of
    beta(i,t,l)=beta(j,t,l).  All undiscovered pairs have zero signature.
    Thus this is exhaustive over the chosen s, not a sample of copy pairs.
    """
    s, n = next_parameters(max(lengths, default=1), permitted_loss)
    coordinates = [(length, pos) for length in lengths for pos in range(length)]
    pair_masks = defaultdict(int)
    for bit, (length, position) in enumerate(coordinates):
        fibers = defaultdict(list)
        for i in range(s):
            fibers[beta(i, position, length, s)].append(i)
        for fiber in fibers.values():
            for i, j in combinations(fiber, 2):
                pair_masks[(i, j)] |= 1 << bit
    witnesses = {}
    for pair, mask in pair_masks.items():
        witnesses.setdefault(mask, pair)
    if len(pair_masks) < s * (s - 1) // 2:
        zero_pair = next(pair for pair in combinations(range(s), 2) if pair not in pair_masks)
        witnesses[0] = zero_pair
    return {
        's': s, 'n': n, 'path_lengths': lengths,
        'copy_pairs_covered': s * (s - 1) // 2,
        'nonzero_signature_pairs': len(pair_masks),
        'distinct_signatures': len(witnesses),
        'coordinates': coordinates, 'witnesses': witnesses
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--slots', default='0,1',
                        choices=('0,1', '0,2', '1,2', '2,0', '2,1'))
    parser.add_argument('--branch', choices=('point', 'cross_13'), default='point')
    parser.add_argument('--target', choices=('P12', 'P13'), default='P12')
    parser.add_argument('--only-component-arcs', action='store_true')
    args = parser.parse_args()
    slots = tuple(int(x) for x in args.slots.split(','))
    started = time.monotonic()
    if args.branch == 'point':
        C, protected, new = build(slots, args.target)
        a_parameters = ['2', '8/5', '128/85']
        description = 'K1 s45 plus point-pair K2 s153, repaired actual path lengths'
    else:
        from akr_v3_mix import build as build_mixed
        C, new, _, metadata = build_mixed('cross_13')
        protected = C.names.index('Q_0_1_0_1')
        a_parameters = metadata['a_parameters']
        description = 'K1 s45 plus K2 sum P12+P13 plus K3 W-cross s297, repaired actual path lengths'
    last_a = Fraction(a_parameters[-1])
    next_a = (last_a + Fraction(3, 2)) / 2
    permitted_loss = 1 - next_a / last_a
    a_parameters.append(str(next_a))
    C.verify()
    vals, labels = quotient_H(C)
    graphs = graph_data(C)
    h_failures = []
    h_arrows = 0
    for (x, y), maps in C.hom.items():
        for f in maps:
            h_arrows += 1
            image = [labels[y][f[v]] for v in vals[x]]
            if len(image) != len(set(image)):
                h_failures.append({'source': C.names[x], 'target': C.names[y],
                                   'map': f, 'component_images': image})

    # Linear-time checks relevant to every W-source pair, including the
    # many pairs deliberately omitted from the larger-source loop below.
    component_arc_records = []
    w_overlap_failures = []
    for y in range(len(C.size)):
        arcs = {}
        seen_point_pair = {}
        opposite = []
        loops = []
        w_arrows = sorted(C.hom.get((1, y), ()))
        by_e = defaultdict(list)
        for index, b in enumerate(w_arrows):
            e, c = labels[y][b[0]], labels[y][b[2]]
            by_e[e].append((index, b))
            assert labels[y][b[1]] == e
            if e == c:
                loops.append({'W_arrow': b, 'component': e})
            if (c, e) in arcs and e != c:
                opposite.append({'first_arrow': arcs[(c, e)], 'second_arrow': b,
                                 'component_arc': [e, c]})
            arcs.setdefault((e, c), b)
            for point_pair in combinations(sorted(b), 2):
                if point_pair in seen_point_pair:
                    w_overlap_failures.append({'target': C.names[y],
                                                'point_pair': point_pair,
                                                'first_arrow': seen_point_pair[point_pair],
                                                'second_arrow': b})
                else:
                    seen_point_pair[point_pair] = b
        component_length_three_pairs = 0
        inflation_count = 0
        inflation_examples = []
        for i, f in enumerate(w_arrows):
            ef, cf = labels[y][f[0]], labels[y][f[2]]
            for j, g in by_e[cf]:
                eg, cg = labels[y][g[0]], labels[y][g[2]]
                if i == j or ef == cg or ef == cf or eg == cg:
                    continue
                component_length_three_pairs += 1
                has_cross_point = any(f[r] == g[s] for r in range(3)
                                      for s in range(3) if r != s)
                if not has_cross_point:
                    inflation_count += 1
                    if len(inflation_examples) < 3:
                        inflation_examples.append({'f': f, 'g': g,
                                                   'component_chain': [ef, cf, cg],
                                                   'point_path_max': 2,
                                                   'component_path_max': 3})
        if arcs:
            component_arc_records.append({'target': C.names[y],
                                           'W_arrows': len(C.hom[1, y]),
                                           'distinct_component_arcs': len(arcs),
                                           'distinct_E_components': len({e for e, c in arcs}),
                                           'distinct_C_components': len({c for e, c in arcs}),
                                           'E_equals_C': loops,
                                           'opposite_component_arcs': opposite,
                                           'W_component_path_length_three_pairs': component_length_three_pairs,
                                           'W_component_path_inflation_count': inflation_count,
                                           'W_component_path_inflation_examples': inflation_examples})

    fixed_failures = []
    next_failures = []
    component_cycles = []
    component_inflation = []
    counts = []
    signature_cache = {}
    pairs_checked = next_subsets = 0
    max_point_path = max_component_path = 1
    for (x, y), arrows in list(C.hom.items()):
        if args.only_component_arcs:
            continue
        if x == y or C.size[x] < 4 or len(arrows) < 2:
            continue
        pair_count = subset_count = 0
        arrows = sorted(arrows)
        for i, f in enumerate(arrows):
            for j, g in enumerate(arrows[:i]):
                pair_count += 1
                pairs_checked += 1
                fixed_source = {v for v in range(C.size[x]) if f[v] == g[v]}
                failed = disconnected_subset(graphs[x], labels[x], fixed_source)
                if failed:
                    fixed_failures.append({'source': C.names[x], 'target': C.names[y],
                                           'pair_indices': [i, j], 'f': f, 'g': g,
                                           'fixed_subset': sorted(fixed_source), **failed})

                fixed, paths, cycles = relation_paths(f, g)
                assert not cycles, 'the repaired attachment forbids point cycles'
                point_length = max(map(len, paths), default=1)
                max_point_path = max(max_point_path, point_length)
                f_h = [labels[y][f[v]] for v in vals[x]]
                g_h = [labels[y][g[v]] for v in vals[x]]
                if len(f_h) == len(set(f_h)) and len(g_h) == len(set(g_h)):
                    _, h_paths, h_cycles = relation_paths(f_h, g_h)
                    h_length = max(map(len, h_paths), default=1)
                    max_component_path = max(max_component_path, h_length)
                    if h_cycles:
                        component_cycles.append({'source': C.names[x], 'target': C.names[y],
                                                 'pair_indices': [i, j], 'cycles': h_cycles})
                    if h_length > point_length:
                        component_inflation.append({'source': C.names[x], 'target': C.names[y],
                                                    'pair_indices': [i, j],
                                                    'point_path_max': point_length,
                                                    'component_path_max': h_length})

                lengths = tuple(sorted({len(p) for p in paths}))
                if lengths not in signature_cache:
                    signature_cache[lengths] = collision_signatures(lengths, permitted_loss)
                sig = signature_cache[lengths]
                paths_by_length = defaultdict(list)
                for path in paths:
                    paths_by_length[len(path)].append(path)
                seen_subsets = set()
                for mask, copy_pair in sig['witnesses'].items():
                    subset = set(fixed)
                    for bit, (length, position) in enumerate(sig['coordinates']):
                        if mask & (1 << bit):
                            subset.update(path[position] for path in paths_by_length[length])
                    key = frozenset(subset)
                    if key in seen_subsets:
                        continue
                    seen_subsets.add(key)
                    subset_count += 1
                    next_subsets += 1
                    failed = disconnected_subset(graphs[y], labels[y], subset)
                    if failed:
                        next_failures.append({'source_pair_domain': C.names[x],
                                              'source_pair_target': C.names[y],
                                              'source_pair_indices': [i, j], 'f': f, 'g': g,
                                              'next_s': sig['s'], 'next_n': sig['n'],
                                              'copy_pair_indices': copy_pair,
                                              'fixed_subset_in_copy_source': sorted(subset), **failed})
                if fixed_failures or next_failures:
                    break
            if fixed_failures or next_failures:
                break
        record = {'source': C.names[x], 'target': C.names[y], 'parallel_pairs': pair_count,
                  'exact_next_fixed_subsets': subset_count}
        counts.append(record)
        print(json.dumps(record), flush=True)
        if fixed_failures or next_failures:
            break

    signature_summary = [{k: v for k, v in sig.items() if k not in ('coordinates', 'witnesses')}
                         for sig in signature_cache.values()]
    result = {
        'construction': description,
        'point_pair_slots_in_lex_first_W_arrow': slots if args.branch == 'point' else None,
        'point_pair_target': args.target if args.branch == 'point' else None,
        'admissible_parameters': {f'a{i}': value for i, value in enumerate(a_parameters)},
        'next_permitted_loss': str(permitted_loss),
        'objects': len(C.size), 'arrows_including_identities': h_arrows,
        'new_target_vertices': C.size[new],
        'new_target_edges': len(C.hom[1, new]),
        'new_target_graph_components': len(vals[new]),
        'new_target_cycle_rank': len(C.hom[1, new]) - C.size[new] + len(vals[new]),
        'protected_copies': sum(len(C.hom.get((C.names.index(name), new), ()))
                                for name in ('Q_0_1_0_1', 'Q_0_1_1_0')),
        'minimum_source_size_tested': 4,
        'fixed_subgraph_tests_run': not args.only_component_arcs,
        'parallel_pairs_checked': pairs_checked,
        'exact_next_fixed_subsets_checked': next_subsets,
        'pair_counts': counts,
        'signature_enumerations': signature_summary,
        'H_injectivity_failures': h_failures,
        'W_image_overlap_at_least_two_failures': w_overlap_failures,
        'W_component_arc_checks': component_arc_records,
        'fixed_subgraph_failures': fixed_failures,
        'next_copy_fixed_subgraph_failures': next_failures,
        'component_relation_cycles': component_cycles,
        'component_path_inflation': component_inflation,
        'maximum_point_path_vertices': max_point_path,
        'maximum_component_path_vertices': max_component_path,
        'elapsed_seconds': round(time.monotonic() - started, 3),
        'scope': 'specified finite subcategory and one further symbolic attachment per tested pair; no all-stage inference'
    }
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
