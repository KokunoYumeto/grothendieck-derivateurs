#!/usr/bin/env python3
"""Regenerate an original Python gzip from its exact transposed TSV bytes."""
import struct, zlib
from FINMON_row_codec import decode

ENCODING = 'transpose-xz-decoded-python-gzip-v1'

def regenerate(source, record):
    assert record['encoding'] == ENCODING
    yield bytes.fromhex(record['original_header_hex'])
    compressor = zlib.compressobj(record['compresslevel'], zlib.DEFLATED, -15)
    crc = decoded = 0
    for block in decode(source):
        decoded += len(block)
        crc = zlib.crc32(block, crc)
        data = compressor.compress(block)
        if data:
            yield data
    assert decoded == record['decoded_bytes']
    if record.get('sync_flush_before_close'):
        yield compressor.flush(zlib.Z_SYNC_FLUSH)
    yield compressor.flush(zlib.Z_FINISH)
    yield struct.pack('<II', crc & 0xffffffff, decoded & 0xffffffff)

