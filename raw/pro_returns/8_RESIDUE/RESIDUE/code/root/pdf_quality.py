"""Render every final PDF page and record mechanical layout checks.

Contact sheets are deliverable audit outputs. Full-resolution page images are
reproducible intermediates in the adjacent scratch directory. Mechanical
checks do not replace the separately recorded visual inspection.
"""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PDF = ROOT / 'RESIDUE_paper.pdf'
TMP = ROOT.parent / 'tmp/pdfs/RESIDUE_final'
QA = OUT / 'qa'


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    QA.mkdir(exist_ok=True)
    for path in TMP.glob('page-*.png'):
        path.unlink()
    for path in QA.glob('contact-*.png'):
        path.unlink()
    run(['pdftoppm', '-r', '90', '-png', str(PDF), str(TMP / 'page')])
    info = run(['pdfinfo', str(PDF)])
    fonts = run(['pdffonts', str(PDF)])
    (OUT / 'pdf_info.txt').write_text(info)
    (OUT / 'pdf_fonts.txt').write_text(fonts)
    bbox = TMP / 'bounds.xhtml'
    run(['pdftotext', '-bbox', str(PDF), str(bbox)])
    # Poppler can emit legacy mathematical-font control slots as literal
    # XML-forbidden characters. Remove only those from the extraction used
    # to inspect boxes; the PDF and rendered page images are unchanged.
    bbox_text = bbox.read_text()
    forbidden_controls = re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', bbox_text)
    doc = ET.ElementTree(ET.fromstring(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', bbox_text)))
    ns = {'h': 'http://www.w3.org/1999/xhtml'}
    out_of_page = []
    for page_number, page in enumerate(doc.findall('.//h:page', ns), 1):
        width, height = float(page.attrib['width']), float(page.attrib['height'])
        for word in page.findall('h:word', ns):
            box = [float(word.attrib[k]) for k in ('xMin','yMin','xMax','yMax')]
            if min(box[:2]) < 5 or box[2] > width - 5 or box[3] > height - 5:
                out_of_page.append({'page': page_number, 'word': word.text, 'box': box})
    pages = sorted(TMP.glob('page-*.png'))
    reader = PdfReader(PDF)
    assert len(pages) == len(reader.pages)
    counts = [len((page.extract_text() or '').split()) for page in reader.pages]
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 19)
    cell_w, cell_h, margin = 355, 530, 18
    sheets = []
    for offset in range(0, len(pages), 16):
        selected = pages[offset:offset + 16]
        rows = (len(selected) + 3) // 4
        sheet = Image.new('RGB', (4 * cell_w + 2 * margin, rows * cell_h + 2 * margin), '#d8dde3')
        draw = ImageDraw.Draw(sheet)
        for index, path in enumerate(selected):
            im = Image.open(path).convert('RGB')
            im.thumbnail((cell_w - 16, cell_h - 38))
            x = margin + (index % 4) * cell_w + (cell_w - im.width) // 2
            y = margin + (index // 4) * cell_h
            sheet.paste(im, (x, y))
            draw.text((x, y + im.height + 6), f'Page {offset + index + 1}', font=font, fill='#111827')
        dest = QA / f'contact-{offset // 16 + 1:02d}.png'
        sheet.save(dest, optimize=True)
        sheets.append(str(dest.relative_to(ROOT)))
    rawlog = (ROOT / 'RESIDUE_paper.log').read_text(errors='replace')
    status = {
        'pdf_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'page_count': len(reader.pages),
        'all_pages_rendered': len(pages) == len(reader.pages),
        'words_per_page': counts,
        'empty_pages': [i + 1 for i, n in enumerate(counts) if n == 0],
        'words_outside_page_safety_bound': out_of_page,
        'legacy_math_font_controls_removed_from_bbox_xml_only': len(forbidden_controls),
        'font_table_file': 'code/root/pdf_fonts.txt',
        'all_fonts_embedded': all(re.search(r'\s+yes\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$', line)
                                  for line in fonts.splitlines()[2:] if line.strip()),
        'overfull_boxes': rawlog.count('Overfull \\hbox') + rawlog.count('Overfull \\vbox'),
        'underfull_boxes': rawlog.count('Underfull \\hbox') + rawlog.count('Underfull \\vbox'),
        'missing_characters': rawlog.count('Missing character:'),
        'font_loader_fallback_notice': 'Error in luaotfload: reverting to OT1' in rawlog,
        'contact_sheets': sheets,
        'visual_review': 'Recorded separately after image inspection.'
    }
    (OUT / 'pdf_quality_output.json').write_text(json.dumps(status, indent=2) + '\n')
    versions = {'python': platform.python_version(), 'platform': platform.platform(),
                'packages': {name: importlib.metadata.version(name) for name in ('sympy', 'Pillow', 'pypdf')}}
    (OUT / 'runtime_versions.json').write_text(json.dumps(versions, indent=2) + '\n')
    print(json.dumps(status, indent=2))
    assert not out_of_page and not status['empty_pages']
    assert status['all_fonts_embedded'] and status['overfull_boxes'] == 0
    assert status['missing_characters'] == 0


if __name__ == '__main__':
    main()
