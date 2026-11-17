#!/usr/bin/env python3
"""Restore only a specified, previously frozen compressed stdout prefix.

The underlying self-contained compiler/input bundle and gzip implementation
are the unchanged full-recipe codec.  Reaching the exact requested prefix
closes that generator and deliberately stops any remaining producer work.
This establishes no producer completion and no scientific census completion.
The caller must check every original prefix byte by its size and SHA256.
"""
from FINMON_cpp_recipe_codec import regenerate as full_regenerate

ENCODING = 'deterministic-cpp-stdout-python-gzip-prefix-v1'

def regenerate(source, record, scratch_dir=None, stats=None):
    assert record['encoding'] == ENCODING
    assert record['prefix_only'] is True
    limit = record['original_bytes']
    assert isinstance(limit, int) and limit > 0
    # Full-stream completion expectations cannot be applied to a prefix.
    base = {key: record[key] for key in ('original_header_hex', 'compresslevel')}
    if 'sync_flush_before_close' in record:
        base['sync_flush_before_close'] = record['sync_flush_before_close']
    inner_stats = {}
    stream = full_regenerate(source, base, scratch_dir=scratch_dir, stats=inner_stats)
    emitted = 0
    try:
        for block in stream:
            take = block[:limit-emitted]
            if take:
                emitted += len(take)
                yield take
            if emitted == limit:
                break
    finally:
        # GeneratorExit enters the original codec's cleanup path: a live
        # subprocess is terminated and waited for, then temporary files go.
        stream.close()
    assert emitted == limit, ('Producer ended before requested prefix', emitted, limit)
    if stats is not None:
        stats.update(prefix_bytes_emitted=emitted,
                     exact_requested_prefix_reconstructed=True,
                     remaining_generator_closed=True,
                     scientific_producer_completion_claimed=False)

