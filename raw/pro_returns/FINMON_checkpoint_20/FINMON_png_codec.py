"""Byte-exact PNG storage codec; no image pixels or original bytes are changed."""
import hashlib,struct,zlib

ENCODING='xz-png-scanlines-v1'

def unpack_png(data):
    assert data[:8]==b'\x89PNG\r\n\x1a\n'
    chunks=[];i=8
    while i<len(data):
        n=int.from_bytes(data[i:i+4],'big');typ=data[i+4:i+8]
        assert zlib.crc32(data[i+4:i+8+n])&0xffffffff==int.from_bytes(data[i+8+n:i+12+n],'big')
        chunks.append((i,typ,n));i+=n+12
    assert i==len(data)
    ids=[j for j,c in enumerate(chunks)if c[1]==b'IDAT']
    assert ids and ids==list(range(ids[0],ids[-1]+1))
    start=chunks[ids[0]][0];last=chunks[ids[-1]];end=last[0]+last[2]+12
    stream=b''.join(data[i+8:i+8+n]for i,t,n in chunks if t==b'IDAT')
    return {'original_header_hex':data[:start].hex(),'original_suffix_hex':data[end:].hex(),
            'idat_sizes':[chunks[j][2]for j in ids]},stream,zlib.decompress(stream)

def deflate(raw,level,memlevel,strategy):
    compressor=zlib.compressobj(level,zlib.DEFLATED,15,memlevel,strategy)
    return compressor.compress(raw)+compressor.flush()

def regenerate(raw,record):
    if 'shared_decoded_bytes' in record:
        assert len(raw)==record['shared_decoded_bytes']
        begin=record['decoded_offset']
        raw=raw[begin:begin+record['decoded_bytes']]
    assert len(raw)==record['decoded_bytes']
    stream=deflate(raw,record['compresslevel'],record['memlevel'],record['strategy'])
    assert len(stream)==sum(record['idat_sizes'])
    output=bytearray.fromhex(record['original_header_hex']);offset=0
    for size in record['idat_sizes']:
        part=b'IDAT'+stream[offset:offset+size];offset+=size
        output.extend(struct.pack('>I',size)+part+struct.pack('>I',zlib.crc32(part)&0xffffffff))
    output.extend(bytes.fromhex(record['original_suffix_hex']))
    assert len(output)==record['original_bytes']
    assert hashlib.sha256(output).hexdigest()==record['original_sha256'],'Incompatible zlib regeneration'
    return output
