"""Reconstruct one byte-exact contact PNG from retained, hashed page PNGs.

The recipe contains fixed layout parameters, literal page labels and the exact
font bytes.  It executes no saved program.  Every source and the entire output
are checked against their original size/SHA256.  Compatible Pillow, FreeType
and zlib are required; an incompatible reconstruction fails closed.
"""
from base64 import b64decode
from hashlib import sha256
from io import BytesIO
import json
import re

from PIL import Image, ImageDraw, ImageFont

ENCODING = 'xz-retained-pages-contact-png-v1'
FORMAT = 'FINMON-retained-pages-contact-PNG-1'
PARAMETERS = {
    'mode': 'RGB', 'thumbnail': [360, 510], 'thumbnail_resample': 'BICUBIC',
    'thumbnail_reducing_gap': 2.0, 'tile': [380, 550], 'columns': 3,
    'tile_color': '#e5e7eb', 'image_y': 30, 'label_xy': [10, 8],
    'label_template': 'Page {page}', 'label_fill': 'black',
    'background': 'white', 'font_size': 10, 'font_layout_engine': 'BASIC',
    'PNG_optimize': False, 'PNG_compress_level': 6,
}


def _digest(data):
    return sha256(data).hexdigest()


def _page_record(record):
    assert set(record) == {'page', 'path', 'bytes', 'sha256'}
    assert type(record['page']) is int and record['page'] > 0
    assert type(record['bytes']) is int and record['bytes'] > 0
    assert re.fullmatch(r'[0-9a-f]{64}', record['sha256'])
    path = record['path']
    assert isinstance(path, str) and not path.startswith('/')
    assert all(part not in ('', '.', '..') for part in path.split('/'))
    assert re.fullmatch(r'FINMON_work/(?:[^/]+/)*notes/checkpoint_[0-9]+_render/page_[0-9]+\.png', path)
    assert path.endswith('/page_%03d.png' % record['page'])


def regenerate(raw_recipe, record, source_reader):
    """Return the original PNG bytes; source_reader takes a logical page path.

    ``raw_recipe`` is the uncompressed JSON payload.  The archive layer must
    check the compressed recipe SHA before calling this function.
    """
    recipe = json.loads(raw_recipe)
    assert set(recipe) == {'format', 'parameters', 'font_base64', 'font_sha256',
                           'pages', 'original_bytes', 'original_sha256'}
    assert recipe['format'] == FORMAT
    assert recipe['parameters'] == PARAMETERS
    assert record['encoding'] == ENCODING
    assert record['contact_parameters'] == recipe['parameters']
    assert recipe['pages'] == record['source_pages']
    assert recipe['original_bytes'] == record['original_bytes']
    assert recipe['original_sha256'] == record['original_sha256']
    assert recipe['font_sha256'] == record['font_sha256']
    pages = recipe['pages']
    assert isinstance(pages, list) and 1 <= len(pages) <= 256
    for page in pages:
        _page_record(page)
    font_bytes = b64decode(recipe['font_base64'], validate=True)
    assert _digest(font_bytes) == recipe['font_sha256']
    font = ImageFont.truetype(BytesIO(font_bytes), size=10,
                             layout_engine=ImageFont.Layout.BASIC)
    cols = 3
    contact = Image.new('RGB', (cols*380, ((len(pages)+cols-1)//cols)*550), 'white')
    for index, page in enumerate(pages):
        data = source_reader(page['path'])
        assert isinstance(data, bytes)
        assert len(data) == page['bytes'] and _digest(data) == page['sha256'], page['path']
        with Image.open(BytesIO(data)) as source:
            assert source.format == 'PNG'
            image = source.convert('RGB')
        image.thumbnail((360, 510), resample=Image.Resampling.BICUBIC, reducing_gap=2.0)
        tile = Image.new('RGB', (380, 550), '#e5e7eb')
        tile.paste(image, ((380-image.width)//2, 30))
        ImageDraw.Draw(tile).text((10, 8), 'Page %d' % page['page'],
                                 fill='black', font=font)
        contact.paste(tile, ((index%cols)*380, (index//cols)*550))
    output = BytesIO()
    contact.save(output, format='PNG', optimize=False, compress_level=6)
    data = output.getvalue()
    assert len(data) == record['original_bytes'], 'Incompatible contact PNG reconstruction size'
    assert _digest(data) == record['original_sha256'], 'Incompatible contact PNG reconstruction SHA256'
    return data
