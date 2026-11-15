#!/usr/bin/env python3
"""Render a specified PDF page sample and contact sheets for visual inspection.

This prepares review images; it does not assert that a human/model review passed.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
import argparse
import json
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser()
parser.add_argument('--pages', required=True, help='Comma-separated one-based pages')
parser.add_argument('--checkpoint', type=int, required=True)
args = parser.parse_args()
pages = sorted(set(int(x) for x in args.pages.split(',')))
out = ROOT / 'logs' / 'rendered'
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(ROOT / 'INDLOCAL_paper.pdf')
assert all(1 <= p <= len(doc) for p in pages)
thumbs = []
for p in pages:
    pix = doc[p - 1].get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
    path = out / f'page_{p:02d}.png'
    pix.save(path)
    im = Image.open(path).convert('RGB')
    im.thumbnail((500, 710))
    tile = Image.new('RGB', (520, 742), 'white')
    tile.paste(im, ((520 - im.width) // 2, 26))
    ImageDraw.Draw(tile).text((12, 8), f'Page {p}', fill='black')
    thumbs.append(tile)
contacts = []
for n in range(0, len(thumbs), 6):
    group = thumbs[n:n + 6]
    sheet = Image.new('RGB', (1040, 742 * ((len(group) + 1) // 2)), '#d7d7d7')
    for k, tile in enumerate(group):
        sheet.paste(tile, ((k % 2) * 520, (k // 2) * 742))
    path = out / f'checkpoint_{args.checkpoint:02d}_contact_{n // 6 + 1}.png'
    sheet.save(path)
    contacts.append(str(path.relative_to(ROOT)))
record = {'checkpoint': args.checkpoint, 'total_pages': len(doc),
          'rendered_pages': pages, 'contact_sheets': contacts,
          'status': 'RENDERED; visual review still required'}
(ROOT / 'logs' / f'checkpoint_{args.checkpoint:02d}_render_record.json').write_text(
    json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
