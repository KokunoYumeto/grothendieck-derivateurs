#!/usr/bin/env python3
"""Byte-reversible certificate encoding: derive each row hash from its source.

The original source_row and every other certificate byte are retained.
Only the 64 ASCII hexadecimal SHA256 characters are omitted. Encoding checks
each omitted value against the complete referenced source line. Decoding
recomputes precisely those characters; callers verify the full original file.
"""
from pathlib import Path
import hashlib,lzma,re

ENCODING='xz-jsonl-derived-source-sha256-v1'
COLUMN_ENCODING='json-columns-xz-derived-source-sha256-v1'
ROW=re.compile(rb'^\{"source_row":([0-9]+),"source_line_sha256":"([0-9a-f]{64})"')
EMPTY=re.compile(rb'^\{"source_row":([0-9]+),"source_line_sha256":"()"')

def source_lines(blocks):
    tail=b''
    for block in blocks:
        pieces=(tail+block).split(b'\n');tail=pieces.pop()
        for line in pieces:yield line+b'\n'
    if tail:yield tail

def encode(certificate,source,target):
    assert next(source)==b'source\ttarget\tcomposition\n'
    digest=hashlib.sha256();size=0;rows=0
    with lzma.open(target,'wb',preset=3)as out:
        for line in certificate:
            digest.update(line);size+=len(line);m=ROW.match(line)
            if m is None:
                assert not line.endswith(b'\n'),'Unexpected complete certificate row'
                out.write(line);continue
            rows+=1;assert int(m.group(1))==rows
            original=next(source)
            assert hashlib.sha256(original).hexdigest().encode()==m.group(2)
            out.write(line[:m.start(2)]+line[m.end(2):])
    return {'original_bytes':size,'original_sha256':digest.hexdigest(),'certificate_rows':rows}

def restore_lines(lines,source):
    assert next(source)==b'source\ttarget\tcomposition\n'
    rows=0
    for line in lines:
        m=EMPTY.match(line)
        if m is None:
            assert not line.endswith(b'\n'),'Unexpected complete encoded row'
            yield line;continue
        rows+=1;assert int(m.group(1))==rows
        original=next(source);digest=hashlib.sha256(original).hexdigest().encode()
        yield line[:m.start(2)]+digest+line[m.end(2):]

def decode(encoded,source):
    with lzma.open(encoded,'rb')as inp:
        yield from restore_lines(inp,source)
