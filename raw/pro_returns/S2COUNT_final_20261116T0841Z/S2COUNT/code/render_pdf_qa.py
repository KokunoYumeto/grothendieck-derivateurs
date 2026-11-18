#!/usr/bin/env python3
"""Render a PDF with Poppler and make numbered contact sheets for visual QA."""
import argparse
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('pdf', type=Path)
parser.add_argument('output', type=Path)
parser.add_argument('--dpi', type=int, default=65)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
for pattern in ('page-*.png', 'contact-*.png'):
    for previous_render in args.output.glob(pattern):
        previous_render.unlink()
subprocess.run(['pdftoppm', '-r', str(args.dpi), '-png', str(args.pdf),
                str(args.output / 'page')], check=True)
pages = sorted(args.output.glob('page-*.png'))
if not pages:
    raise SystemExit('No pages were rendered')
thumb_width, thumb_height = 430, 610
label_height, margin = 24, 16
cols, rows = 3, 3
for start in range(0, len(pages), cols * rows):
    batch = pages[start:start + cols * rows]
    sheet = Image.new('RGB', (cols * (thumb_width + margin) + margin,
                             rows * (thumb_height + label_height + margin) + margin),
                      '#c8c8c8')
    draw = ImageDraw.Draw(sheet)
    for j, page in enumerate(batch):
        im = Image.open(page).convert('RGB')
        im.thumbnail((thumb_width, thumb_height))
        x = margin + (j % cols) * (thumb_width + margin)
        y = margin + (j // cols) * (thumb_height + label_height + margin)
        draw.text((x, y), f'Page {start + j + 1}', fill='black')
        sheet.paste(im, (x, y + label_height))
    destination = args.output / f'contact-{start // (cols * rows) + 1:02}.png'
    sheet.save(destination)
print(f'Rendered {len(pages)} pages; created {(len(pages) + 8) // 9} contact sheets')
